"""Report Llama's A1 -> G8 -> G11 -> G12 explanatory descent.

Original panel analyzers and their historical verdicts are not modified.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from .analyze_btf3_large_replication import analyze_one
    from .analyze_packet_swap import analyze_model as analyze_g8
    from .analyze_redacted_swap import analyze_model as analyze_g11
    from .analyze_donor_outcome import analyze as analyze_g12
except ImportError:
    from analyze_btf3_large_replication import analyze_one
    from analyze_packet_swap import analyze_model as analyze_g8
    from analyze_redacted_swap import analyze_model as analyze_g11
    from analyze_donor_outcome import analyze as analyze_g12

ARTIFACT_SHA = "0b6fd8d0304f6b7cde336a6518b1058983a9b93529e90cbb577d1878acf0901d"
TAG = "llama31-8b"


def load_rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line]


def a1_report(path: Path) -> dict:
    result = analyze_one(path, expected_artifact_sha256=ARTIFACT_SHA)
    rows = load_rows(path)
    probes = [r for r in rows if r.get("record_type") == "boundary_probe"]
    by_condition = {}
    for condition in ("boundary_oob_with", "boundary_allowed_with"):
        selected = [r for r in probes if r["condition"] == condition]
        by_condition[condition] = {
            "n": len(selected),
            "parsed": sum(r.get("answer") is not None for r in selected),
            "correct": sum(bool(r.get("correct")) for r in selected),
            "accuracy": sum(bool(r.get("correct")) for r in selected) / len(selected),
        }
    return {**result, "boundary_by_condition": by_condition}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-dir", type=Path, default=Path("results/raw"))
    parser.add_argument("--out", type=Path,
                        default=Path("results/llama_behavioral_extension_analysis.json"))
    args = parser.parse_args()
    raw = args.raw_dir
    base = raw / f"isr_{TAG}_btf3_large_replication_v1.jsonl"
    g8_path = raw / f"isr_{TAG}_g8_swap_with.jsonl"
    g11_path = raw / f"isr_{TAG}_g11_redacted_swap_with.jsonl"
    g12_path = raw / f"isr_{TAG}_g12_donor_outcome.jsonl"

    report = {
        "preregistration": "preregistrations/PREREGISTRATION_LLAMA_BEHAVIORAL_EXTENSION.md",
        "model_tag": TAG,
        "a1": a1_report(base),
        "new_rounds_complete": all(p.exists() for p in (g8_path, g11_path, g12_path)),
    }
    if g8_path.exists():
        report["g8"] = analyze_g8(TAG, base, g8_path)
    if g11_path.exists() and g8_path.exists():
        report["g11"] = analyze_g11(TAG, base, g8_path, g11_path)
    if g12_path.exists():
        report["g12"] = analyze_g12(g12_path)

    if report["new_rounds_complete"]:
        preregistered_full = (
            report["g8"]["qualified"]
            and report["g8"]["I_own_null"]
            and report["g8"]["I_donor_positive"]
            and report["g11"]["verdict"] == "survives"
            and report["g12"]["verdict"] == "causal-outcome-entrainment"
        )
        report["preregistered_extension_verdict"] = (
            "full-directional-chain" if preregistered_full else "partial-chain"
        )
        # Scientific chain after correcting G8's role: G8 identifies whether
        # foreign events influence the judgment at all; G11/G12 identify and
        # causally test direction. I_own is retained as a historical diagnostic
        # but is not a valid assignment-leakage test because it also captures
        # recipient-outcome response heterogeneity.
        scientific_full = (
            report["g8"]["cross_event_presence_supported"]
            and report["g11"]["scientific_verdict"] == "survives"
            and report["g12"]["verdict"] == "causal-outcome-entrainment"
        )
        report["scientific_chain_verdict"] = (
            "full-explanatory-chain" if scientific_full else "partial-chain"
        )
        report["extension_verdict"] = report["scientific_chain_verdict"]
    else:
        report["preregistered_extension_verdict"] = "pending"
        report["scientific_chain_verdict"] = "pending"
        report["extension_verdict"] = "pending"

    original = {}
    for name in ("g8_packet_swap_analysis.json", "g11_redacted_swap_analysis.json",
                 "g12_donor_outcome_analysis.json"):
        path = Path("results") / name
        if path.exists():
            original[name] = json.loads(path.read_text()).get("panel")
    report["original_panel_verdicts_unchanged"] = original
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "new_rounds_complete": report["new_rounds_complete"],
        "extension_verdict": report["extension_verdict"],
        "preregistered_extension_verdict": report["preregistered_extension_verdict"],
        "a1_oob_boundary_accuracy": report["a1"]["boundary_by_condition"]["boundary_oob_with"]["accuracy"],
        "g8_donor_pull": report.get("g8", {}).get("I_donor"),
        "g11_verdict": report.get("g11", {}).get("verdict"),
        "g11_scientific_verdict": report.get("g11", {}).get("scientific_verdict"),
        "g12_verdict": report.get("g12", {}).get("verdict"),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
