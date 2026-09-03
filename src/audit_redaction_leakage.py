"""Independent audit of the frozen explicit-verdict redactor.

The frozen pre-run audit (``data/external/review/BTF3_EVR_REDACTION_AUDIT.md``)
reports ``assertive verdict sentences surviving redaction: 0`` under a hard gate.
That number is produced by the same conditional-marker heuristic that decides
what to delete, so it cannot detect the failure mode it shares:

``adapters/btf3_hindsight_depth.redact_verdicts`` treats a sentence as a
criteria restatement -- and keeps it whole -- as soon as ``_CONDITIONAL_RE``
matches anywhere in it::

    if _CONDITIONAL_RE.search(normalized) or not _VERDICT_RE.match(normalized):

A sentence such as *"Because the resolution criteria state the question resolves
NO \"if ...\", and that is exactly what happened, the correct resolution is NO
(0)."* contains ``criteria state``, so it bypasses the verdict patterns entirely
and survives with the outcome fully disclosed.

This module re-audits the frozen packets with a detector that is independent of
the redactor's own classification, and re-estimates the affected experiments on
the leak-free subset. It changes no frozen artifact, threshold, seed or raw
output; it is an explicitly post-result correction.

Run::

    PYTHONPATH=src python3 src/audit_redaction_leakage.py
"""
from __future__ import annotations

import json
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from adapters.btf3_hindsight_depth import redact_verdicts  # noqa: E402
from adapters.btf3_packet_swap import extract_packet  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ARTIFACT = ROOT / "data/external/review/btf3_temporal_large_replication_v1.jsonl"
BOOTSTRAP_SEED = 20260829
N_RESAMPLES = 10_000

# An outcome assertion, detected without consulting the redactor's own
# conditional-marker heuristic.
_VERDICT_MENTION = re.compile(
    r"resolves?\s+(?:as\s+|to\s+)?(?:\*\*)?(?:YES|NO)\b"
    r"|resolution\s+is\s+(?:\*\*)?(?:YES|NO)\b"
    r"|resolution\s*:\s*(?:\*\*)?(?:YES|NO)\b"
    r"|answer\s+is\s+(?:\*\*)?(?:YES|NO)\b"
)
# A genuine criteria restatement keeps its verdict under an unresolved
# antecedent; these words must govern the verdict for it to stay hypothetical.
_HYPOTHETICAL = re.compile(r"\b(if|unless|when|should|would)\b", re.IGNORECASE)
# ... unless the same sentence also asserts that the antecedent obtained.
_ASSERTED = re.compile(
    r"\b(therefore|thus|hence|accordingly|per the|this resolves"
    r"|that is exactly what happened|default applies|correct resolution"
    r"|since no|because no)\b",
    re.IGNORECASE,
)
_SENTENCES = re.compile(r"(?<=[.!?])\s+")


def leaking_sentence(redacted: str) -> str | None:
    """Return the first sentence that still asserts the outcome, if any."""
    for sentence in _SENTENCES.split(redacted):
        match = _VERDICT_MENTION.search(sentence)
        if not match:
            continue
        window = sentence[: match.start()] + sentence[match.end() : match.end() + 40]
        if _ASSERTED.search(sentence) or not _HYPOTHETICAL.search(window):
            return sentence.strip()
    return None


def load_items() -> list[dict]:
    with ARTIFACT.open() as handle:
        return [json.loads(line) for line in handle]


def audit_packets(items: list[dict]) -> dict:
    leaks: list[dict] = []
    for item in items:
        packet = extract_packet(item["oob_variant"]["with_information_prompt"])
        sentence = leaking_sentence(redact_verdicts(packet).text)
        if sentence:
            leaks.append(
                {
                    "independent_unit_id": item["independent_unit_id"],
                    "outcome_alignment_sign": int(
                        item["reference_context"].get("outcome_alignment_sign", 1)
                    ),
                    "surviving_sentence": sentence,
                }
            )
    yes = sum(1 for leak in leaks if leak["outcome_alignment_sign"] == 1)
    return {
        "n_units": len(items),
        "n_leaking": len(leaks),
        "leak_rate": len(leaks) / len(items),
        "leaking_realized_yes": yes,
        "leaking_realized_no": len(leaks) - yes,
        "leaking_unit_ids": [leak["independent_unit_id"] for leak in leaks],
        "examples": leaks[:10],
    }


def bootstrap(values: list[float]) -> tuple[float, float]:
    rng = random.Random(BOOTSTRAP_SEED)
    n = len(values)
    draws = sorted(
        sum(rng.choice(values) for _ in range(n)) / n for _ in range(N_RESAMPLES)
    )
    return draws[int(0.025 * N_RESAMPLES)], draws[int(0.975 * N_RESAMPLES)]


def summarise(values: list[float]) -> dict:
    low, high = bootstrap(values)
    return {
        "n": len(values),
        "mean": sum(values) / len(values),
        "ci_low": low,
        "ci_high": high,
    }


def _decisions(path: Path) -> list[dict]:
    with path.open() as handle:
        return [
            row
            for row in map(json.loads, handle)
            if row.get("record_type") == "decision"
        ]


def reanalyse_g12(leaking: set[str]) -> dict:
    """Paired YES-donor minus NO-donor, with and without leaking donors."""
    out = {}
    for path in sorted((ROOT / "results/raw").glob("isr_*_g12_donor_outcome.jsonl")):
        rows = _decisions(path)
        paired: dict[str, dict] = {}
        for row in rows:
            if row.get("value") is None:
                continue
            paired.setdefault(row["independent_unit_id"], {})[row["donor_outcome"]] = (
                float(row["value"]),
                row["donor_unit_id"],
            )
        every, clean = [], []
        for cells in paired.values():
            if "YES" not in cells or "NO" not in cells:
                continue
            delta = cells["YES"][0] - cells["NO"][0]
            every.append(delta)
            if cells["YES"][1] not in leaking and cells["NO"][1] not in leaking:
                clean.append(delta)
        out[rows[0]["model_tag"]] = {
            "all_pairs": summarise(every),
            "leak_free_pairs": summarise(clean),
        }
    return out


def reanalyse_g2b(items: list[dict], leaking: set[str]) -> dict:
    """Redaction amplification HC_red - HC_direct, with and without leaks."""
    signs = {
        item["independent_unit_id"]: int(
            item["reference_context"].get("outcome_alignment_sign", 1)
        )
        for item in items
    }
    out = {}
    for tag in ("qwen35-9b", "gemma3-12b", "mistral-small-24b"):
        base_path = ROOT / f"results/raw/isr_{tag}_btf3_large_replication_v1.jsonl"
        red_path = ROOT / f"results/raw/isr_{tag}_g2_evr_oob.jsonl"
        if not (base_path.exists() and red_path.exists()):
            continue
        base: dict[str, dict[str, float | None]] = {}
        for row in _decisions(base_path):
            if row["condition"] in ("oob_without", "oob_with"):
                value = row.get("value")
                base.setdefault(row["independent_unit_id"], {})[row["condition"]] = (
                    None if value in (None, "None") else float(value)
                )
        redacted = {}
        for row in _decisions(red_path):
            value = row.get("value")
            redacted[row["independent_unit_id"]] = (
                None if value in (None, "None") else float(value)
            )
        every, clean = [], []
        for unit, cells in base.items():
            if cells.get("oob_with") is None or cells.get("oob_without") is None:
                continue
            if redacted.get(unit) is None:
                continue
            sign = signs[unit]
            direct = sign * (cells["oob_with"] - cells["oob_without"])
            red = sign * (redacted[unit] - cells["oob_without"])
            every.append(red - direct)
            if unit not in leaking:
                clean.append(red - direct)
        out[tag] = {
            "all_units": summarise(every),
            "leak_free_units": summarise(clean),
        }
    return out


def main() -> None:
    items = load_items()
    packet_audit = audit_packets(items)
    leaking = set(packet_audit["leaking_unit_ids"])
    report = {
        "note": "post-result correction; no frozen artifact, threshold or raw output changed",
        "artifact": str(ARTIFACT.relative_to(ROOT)),
        "bootstrap": {"seed": BOOTSTRAP_SEED, "n_resamples": N_RESAMPLES},
        "packet_audit": packet_audit,
        "g12_paired_donor_contrast": reanalyse_g12(leaking),
        "g2b_redaction_amplification": reanalyse_g2b(items, leaking),
    }
    destination = ROOT / "results/btf3_redaction_leakage_audit.json"
    destination.write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n")
    print(
        f"{packet_audit['n_leaking']}/{packet_audit['n_units']} packets still assert "
        f"the outcome after redaction ({packet_audit['leak_rate']:.1%})"
    )
    print(f"wrote {destination.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
