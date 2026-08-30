#!/usr/bin/env python3
"""Fail-closed audit of the explicit-verdict redaction, before any model run.

Checks, over all 256 frozen units:

* zero surviving **assertive** verdict sentences in any redacted packet;
* redaction is subtractive — every redacted packet's surviving sentences all
  appear in the original, except clause-preserved rewrites, which are listed;
* the four prompt cells still differ only where they are supposed to;
* per-item statistics (sentences removed, characters retained), the no-op set
  (packets that never stated an explicit verdict), and a sample of surviving
  conditional criteria restatements for human inspection.

Writes the report only when every hard check passes.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import statistics as st
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import pandas as pd  # noqa: E402

from adapters.btf3_factorization import extract_packet  # noqa: E402
from adapters.btf3_hindsight_depth import (  # noqa: E402
    ALLOWED_REMINDER,
    EXCLUDE_REMINDER,
    build_evr,
    build_positional,
    redact_verdicts,
    residual_verdict_hits,
)
from adapters.btf3_large_replication import file_sha256  # noqa: E402
from information_set_schema import load_jsonl  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", type=Path, default=Path("data/external/review/btf3_temporal_large_replication_v1.jsonl"))
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("data/external/raw/btf3/btf3_binary_questions_and_forecasts.parquet"),
    )
    parser.add_argument("--report", type=Path, default=Path("data/external/review/BTF3_EVR_REDACTION_AUDIT.md"))
    parser.add_argument("--out", type=Path, default=Path("results/btf3_evr_redaction_audit.json"))
    args = parser.parse_args()

    items = load_jsonl(args.artifact)
    frame = pd.read_parquet(args.source)
    source_rows = {str(row["question_id"]): row for row in frame.to_dict("records")}

    per_item = []
    conditional_examples: list[str] = []
    for item in items:
        unit = item.independent_unit_id
        packet = extract_packet(item.oob_variant["with_information_prompt"])
        if packet != str(source_rows[unit]["resolution_explanation"]):
            raise ValueError(f"AUDIT FAILED — packet does not match the pinned source for {unit}")
        redaction = redact_verdicts(packet)

        hits = residual_verdict_hits(redaction.text)
        assertive = [hit["sentence"] for hit in hits if hit["assertive"]]
        if assertive:
            raise ValueError(f"AUDIT FAILED — assertive verdict survived redaction in {unit}: {assertive[0]!r}")
        conditional_examples.extend(hit["sentence"] for hit in hits if not hit["assertive"])

        # Redaction must be subtractive: everything kept, other than the
        # clause-preserved rewrites, is literally present in the original.
        for line in redaction.text.split("\n"):
            stripped = line.strip()
            if not stripped or stripped in packet:
                continue
            if any(clause in stripped for clause in redaction.preserved_clauses):
                continue
            fragments = [part for part in stripped.split(". ") if part]
            if not all(fragment.strip(". ") in packet for fragment in fragments):
                raise ValueError(f"AUDIT FAILED — redacted text is not a subset of the source packet for {unit}")

        for frame_name in ("oob", "allowed"):
            evr_prompt, _ = build_evr(item, frame=frame_name)
            if redaction.n_removed and packet in evr_prompt:
                raise ValueError(f"AUDIT FAILED — original packet still present in EVR {frame_name} prompt for {unit}")
            if redaction.text not in evr_prompt:
                raise ValueError(f"AUDIT FAILED — redacted packet missing from EVR {frame_name} prompt for {unit}")
            before = build_positional(item, frame=frame_name, position="before")
            after = build_positional(item, frame=frame_name, position="after")
            reminder = EXCLUDE_REMINDER if frame_name == "oob" else ALLOWED_REMINDER
            if before.replace(reminder, "", 1) != after.replace(reminder, "", 1):
                raise ValueError(f"AUDIT FAILED — positional pair differs by more than reminder position for {unit}")
            if before.count(reminder) != 1 or after.count(reminder) != 1:
                raise ValueError(f"AUDIT FAILED — reminder is not inserted exactly once for {unit}")

        per_item.append({
            "question_id": unit,
            "verdict_sentences_removed": redaction.n_removed,
            "clauses_preserved": len(redaction.preserved_clauses),
            "source_chars": len(packet),
            "redacted_chars": len(redaction.text),
            "retained_char_ratio": len(redaction.text) / len(packet),
            "removed_sentences": redaction.removed_sentences,
        })

    removed = [row["verdict_sentences_removed"] for row in per_item]
    ratios = [row["retained_char_ratio"] for row in per_item]
    noop = [row["question_id"] for row in per_item if row["verdict_sentences_removed"] == 0]
    report = {
        "artifact": str(args.artifact),
        "artifact_sha256": file_sha256(args.artifact),
        "units": len(per_item),
        "assertive_verdict_residuals": 0,
        "conditional_residual_sentences": len(conditional_examples),
        "verdict_sentences_removed": {
            "total": sum(removed),
            "mean": st.mean(removed),
            "max": max(removed),
            "items_with_none_removed": len(noop),
        },
        "retained_char_ratio": {"mean": st.mean(ratios), "min": min(ratios)},
        "no_op_units": noop,
        "clause_preserved_units": [row["question_id"] for row in per_item if row["clauses_preserved"]],
        "per_item": per_item,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# BTF-3 explicit-verdict redaction — pre-run audit",
        "",
        f"- artifact: `{args.artifact}` (SHA-256 `{report['artifact_sha256']}`)",
        f"- units: {report['units']}",
        f"- assertive verdict sentences surviving redaction: **{report['assertive_verdict_residuals']}** (hard gate: must be 0)",
        f"- verdict sentences removed: {report['verdict_sentences_removed']['total']} "
        f"(mean {report['verdict_sentences_removed']['mean']:.2f}, max {report['verdict_sentences_removed']['max']})",
        f"- packets that stated no explicit verdict at all: **{report['verdict_sentences_removed']['items_with_none_removed']}** "
        "(kept in the sample; reported, never dropped)",
        f"- characters retained: mean {report['retained_char_ratio']['mean']:.3f}, min {report['retained_char_ratio']['min']:.3f}",
        f"- clause-preserved rewrites (\"resolves NO because X\" → \"X.\"): {len(report['clause_preserved_units'])} units",
        f"- surviving conditional criteria restatements: {report['conditional_residual_sentences']} sentences",
        "",
        "Conditional restatements are kept deliberately: they paraphrase the",
        "question's own resolution rules and disclose no outcome. Removing them",
        "would strip the criteria rather than the answer.",
        "",
        "## Surviving conditional restatements (first 10, for inspection)",
        "",
    ]
    lines.extend(f"- {sentence}" for sentence in conditional_examples[:10])
    lines.extend([
        "",
        "## Hard checks passed",
        "",
        "| check | result |",
        "|---|---|",
        "| packets byte-match the pinned source | PASS |",
        "| zero assertive verdict sentences survive | PASS |",
        "| redaction is subtractive (no added or paraphrased content) | PASS |",
        "| original packet absent wherever a verdict was removed | PASS |",
        "| redacted packet present in every EVR prompt | PASS |",
        "| positional pairs differ only by reminder position | PASS |",
        "| reminder inserted exactly once per positional prompt | PASS |",
        "",
        "No target-model output was consulted or produced by this audit.",
        "",
    ])
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k not in {"per_item", "no_op_units", "clause_preserved_units"}}, indent=2, sort_keys=True))
    print(f"wrote {args.report} and {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
