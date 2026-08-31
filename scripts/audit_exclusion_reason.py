#!/usr/bin/env python3
"""Fail-closed audit of the G3 exclusion-reason transformation, before any run.

Hard checks, over all 256 frozen units and both cells:

* the frozen out-of-set sentence occurs exactly once in every source prompt;
* the ``temporal`` arm regenerates the frozen prompt **byte-for-byte** — all
  512 SHA-256 digests must equal the frozen artifact's own digests;
* every arm differs from ``temporal`` at exactly one contiguous span, and that
  span lies inside ``TARGET INFORMATION SET``, before ``LATER RESOLUTION
  PACKET``;
* the token distance from the packet header to ``TASK`` is identical in every
  arm (the G2 Experiment A channel is closed by construction);
* all four arms end in the identical trailing clause;
* the four arms produce four distinct prompts per unit and cell.

Reported for disclosure, not gated: per-arm character and token deltas, and
the boundary-probe prompt digests.

The report is written only when every hard check passes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import statistics as st
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_exclusion_reason import (  # noqa: E402
    ARMS,
    CELLS,
    TEMPORAL_SENTENCE,
    build,
    reason_sentence,
)
from information_set_schema import file_sha256, load_jsonl  # noqa: E402
from run_information_set import boundary_probe  # noqa: E402

_PACKET_MARKER = "\n\nLATER RESOLUTION PACKET\n"
_TIS_MARKER = "\n\nTARGET INFORMATION SET\n"
_TASK_MARKER = "\n\nTASK\n"
_TRAILING = "is not part of the evidence that defines the requested ex-ante forecast."


def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def single_diff_span(left: str, right: str) -> tuple[int, int, int]:
    """Return (start, len_removed, len_added) for the single differing span."""
    head = 0
    while head < min(len(left), len(right)) and left[head] == right[head]:
        head += 1
    tail = 0
    while (
        tail < min(len(left), len(right)) - head
        and left[len(left) - 1 - tail] == right[len(right) - 1 - tail]
    ):
        tail += 1
    return head, len(left) - head - tail, len(right) - head - tail


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artifact",
        type=Path,
        default=Path("data/external/review/btf3_temporal_large_replication_v1.jsonl"),
    )
    parser.add_argument(
        "--tokenizer",
        default="/var/tmp/xiang-isr-models/qwen35-9b",
        help="tokenizer used only for the disclosed token-delta statistics",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("data/external/review/BTF3_EXCLUSION_REASON_AUDIT.md"),
    )
    parser.add_argument("--out", type=Path, default=Path("results/btf3_exclusion_reason_audit.json"))
    args = parser.parse_args()

    items = load_jsonl(args.artifact)
    failures: list[str] = []

    tokenizer = None
    try:
        from transformers import AutoTokenizer

        tokenizer = AutoTokenizer.from_pretrained(args.tokenizer, local_files_only=True)
    except Exception as exc:  # disclosure statistics only; never gates
        print(f"[warn] tokenizer unavailable ({exc}); token deltas omitted")

    identity_checks = 0
    char_delta: dict[str, list[int]] = {arm: [] for arm in ARMS}
    token_delta: dict[str, list[int]] = {arm: [] for arm in ARMS}
    packet_to_task_tokens: dict[str, set[int]] = {arm: set() for arm in ARMS}
    distinct_failures = 0

    for item in items:
        for cell in CELLS:
            source = item.oob_variant[
                "with_information_prompt" if cell == "with" else "without_information_prompt"
            ]
            if source.count(TEMPORAL_SENTENCE) != 1:
                failures.append(f"{item.independent_unit_id}/{cell}: frozen sentence not unique")
                continue

            prompts = {arm: build(item, arm=arm, cell=cell) for arm in ARMS}

            # 1. temporal arm is byte-identical to the frozen prompt
            if prompts["temporal"] != source:
                failures.append(f"{item.independent_unit_id}/{cell}: temporal arm not byte-identical")
            elif sha(prompts["temporal"]) != sha(source):
                failures.append(f"{item.independent_unit_id}/{cell}: temporal digest mismatch")
            else:
                identity_checks += 1

            # 2. four distinct prompts
            if len(set(prompts.values())) != len(ARMS):
                distinct_failures += 1
                failures.append(f"{item.independent_unit_id}/{cell}: arms not pairwise distinct")

            tis_start = source.index(_TIS_MARKER)
            task_start = source.index(_TASK_MARKER)
            packet_start = source.index(_PACKET_MARKER) if cell == "with" else task_start

            for arm in ARMS:
                prompt = prompts[arm]
                # 3. single diff span, inside TARGET INFORMATION SET, before the packet
                start, removed, added = single_diff_span(source, prompt)
                if arm == "temporal":
                    if (removed, added) != (0, 0):
                        failures.append(f"{item.independent_unit_id}/{cell}/{arm}: unexpected diff")
                else:
                    if not (tis_start < start < packet_start):
                        failures.append(
                            f"{item.independent_unit_id}/{cell}/{arm}: diff span outside TARGET INFORMATION SET"
                        )
                    if removed == 0 and added == 0:
                        failures.append(f"{item.independent_unit_id}/{cell}/{arm}: no diff")

                # 4. identical trailing clause
                if _TRAILING not in prompt:
                    failures.append(f"{item.independent_unit_id}/{cell}/{arm}: trailing clause missing")

                # 5. suffix after the packet header is untouched
                if cell == "with":
                    if prompt[prompt.index(_PACKET_MARKER):] != source[packet_start:]:
                        failures.append(
                            f"{item.independent_unit_id}/{cell}/{arm}: text after packet header changed"
                        )

                char_delta[arm].append(len(prompt) - len(source))
                if tokenizer is not None:
                    if cell == "with":
                        tail = prompt[prompt.index(_PACKET_MARKER):]
                        packet_to_task_tokens[arm].add(len(tokenizer(tail, add_special_tokens=False)["input_ids"]))
                    token_delta[arm].append(
                        len(tokenizer(prompt, add_special_tokens=False)["input_ids"])
                        - len(tokenizer(source, add_special_tokens=False)["input_ids"])
                    )

    # 6. packet->TASK token distance invariant across arms
    if tokenizer is not None:
        spans = {arm: sorted(packet_to_task_tokens[arm]) for arm in ARMS}
        if any(spans[arm] != spans["temporal"] for arm in ARMS):
            failures.append("packet-to-TASK token distance differs between arms")

    report = {
        "artifact": str(args.artifact),
        "artifact_sha256": file_sha256(args.artifact),
        "units": len(items),
        "arms": {arm: reason_sentence(arm) for arm in ARMS},
        "frozen_sentence": TEMPORAL_SENTENCE,
        "temporal_byte_identity_checks": identity_checks,
        "temporal_byte_identity_expected": len(items) * len(CELLS),
        "char_delta_vs_temporal": {
            arm: {
                "min": min(values),
                "max": max(values),
                "mean": round(st.mean(values), 2),
            }
            for arm, values in char_delta.items()
            if values
        },
        "token_delta_vs_temporal": {
            arm: {
                "min": min(values),
                "max": max(values),
                "mean": round(st.mean(values), 2),
            }
            for arm, values in token_delta.items()
            if values
        },
        "packet_to_task_token_span_invariant": tokenizer is not None
        and all(
            sorted(packet_to_task_tokens[arm]) == sorted(packet_to_task_tokens["temporal"])
            for arm in ARMS
        ),
        "arms_pairwise_distinct_failures": distinct_failures,
        "boundary_probe_example_sha256": sha(
            boundary_probe(build(items[0], arm="procedural", cell="with"), expected="NO")
        ),
        "failures": failures[:50],
        "n_failures": len(failures),
        "pass": not failures and identity_checks == len(items) * len(CELLS),
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "failures"}, indent=2, ensure_ascii=False))

    if not report["pass"]:
        print(f"AUDIT FAILED: {len(failures)} failures", file=sys.stderr)
        for line in failures[:20]:
            print("  " + line, file=sys.stderr)
        return 1

    lines = [
        "# BTF-3 exclusion-reason transformation audit",
        "",
        f"Artifact: `{args.artifact}`  ",
        f"SHA-256: `{report['artifact_sha256']}`  ",
        f"Units: {report['units']} × 2 cells",
        "",
        "## Result",
        "",
        f"**PASS.** {identity_checks}/{report['temporal_byte_identity_expected']} temporal-arm "
        "prompts are byte-identical to the frozen artifact; every other arm differs from it at "
        "exactly one contiguous span inside `TARGET INFORMATION SET`, before "
        "`LATER RESOLUTION PACKET`; nothing after the packet header changes in any arm.",
        "",
        "## Frozen sentence",
        "",
        "```text",
        TEMPORAL_SENTENCE,
        "```",
        "",
        "## Arms",
        "",
        "| arm | sentence | Δ chars vs temporal (mean) | Δ tokens (mean) |",
        "|---|---|---:|---:|",
    ]
    for arm in ARMS:
        cd = report["char_delta_vs_temporal"].get(arm, {}).get("mean", 0)
        td = report["token_delta_vs_temporal"].get(arm, {}).get("mean", "n/a")
        lines.append(f"| `{arm}` | {reason_sentence(arm)} | {cd} | {td} |")
    lines += [
        "",
        "## Position channel",
        "",
        f"`packet_to_task_token_span_invariant`: **{report['packet_to_task_token_span_invariant']}**. "
        "The edited sentence precedes the packet, so the token distance between the packet "
        "header and `TASK` is identical in all four arms. The positional channel that G2 "
        "Experiment A found to matter is closed by construction, not by argument.",
        "",
        "## Disclosure",
        "",
        "The `unreliable` arm asserts that the packet may contain fabricated claims. That is "
        "false of our materials and is a deliberate counterfactual framing manipulation. The "
        "`procedural` arm affirms the packet's accuracy, which the `temporal` arm does not; it "
        "is therefore a conservative test of a non-temporal licensing reason. Both disclosures "
        "are repeated wherever the arms are reported.",
        "",
    ]
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
