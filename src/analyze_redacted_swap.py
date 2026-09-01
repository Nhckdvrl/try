"""Analyze G11 against frozen G8 and large-replication outputs."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from .analyze_exante_anchor import bootstrap_mean
    from .analyze_packet_swap import load
except ImportError:
    from analyze_exante_anchor import bootstrap_mean
    from analyze_packet_swap import load

PARSE_FLOOR = 248 / 256
BOUNDARY_FLOOR = 224 / 256
EXPECTED_MODELS = ("qwen35-9b", "gemma3-12b", "mistral-small-24b")


def analyze_model(tag: str, baseline_path: Path, full_path: Path, red_path: Path) -> dict:
    base_meta, base_rows = load(baseline_path)
    full_meta, full_rows = load(full_path)
    red_meta, red_rows = load(red_path)
    if len({base_meta["artifact_sha256"], full_meta["artifact_sha256"], red_meta["artifact_sha256"]}) != 1:
        raise ValueError(f"{tag}: artifact mismatch")
    if full_meta["pairing_sha256"] != red_meta["pairing_sha256"]:
        raise ValueError(f"{tag}: pairing mismatch")

    without = {r["independent_unit_id"]: r["value"] for r in base_rows
               if r["record_type"] == "decision" and r["condition"] == "oob_without" and r["value"] is not None}
    full = {r["independent_unit_id"]: r for r in full_rows
            if r["record_type"] == "decision" and r["value"] is not None}
    red = {r["independent_unit_id"]: r for r in red_rows
           if r["record_type"] == "decision" and r["value"] is not None}
    decisions = [r for r in red_rows if r["record_type"] == "decision"]
    probes = [r for r in red_rows if r["record_type"] == "boundary_probe"]
    parse_rate = sum(r["value"] is not None for r in decisions) / len(decisions)
    boundary_accuracy = sum(bool(r.get("correct")) for r in probes) / len(probes)
    units = sorted(set(without) & set(full) & set(red))
    own_red = [red[u]["direction"] * (red[u]["value"] - without[u]) for u in units]
    donor_red = [red[u]["donor_direction"] * (red[u]["value"] - without[u]) for u in units]
    donor_full = [full[u]["donor_direction"] * (full[u]["value"] - without[u]) for u in units]
    label_delta = [a - b for a, b in zip(donor_full, donor_red)]
    s_red = [abs(red[u]["value"] - without[u]) for u in units]
    i_own = bootstrap_mean(own_red)
    i_red = bootstrap_mean(donor_red)
    i_full = bootstrap_mean(donor_full)
    delta = bootstrap_mean(label_delta)
    retention = i_red["mean"] / i_full["mean"] if i_full["mean"] else None
    qualified = parse_rate >= PARSE_FLOOR and boundary_accuracy >= BOUNDARY_FLOOR
    validity = i_own["ci_low"] >= -5 and i_own["ci_high"] <= 5
    if qualified and validity and i_red["ci_low"] > 0 and retention >= 0.5:
        verdict = "survives"
    elif qualified and validity and delta["ci_low"] > 0 and retention < 0.5:
        verdict = "verdict-dependent"
    else:
        verdict = "indeterminate"
    return {
        "model_tag": tag, "units": len(units), "parse_rate": parse_rate,
        "boundary_accuracy": boundary_accuracy, "qualified": qualified,
        "own_pull_redacted": i_own, "donor_pull_redacted": i_red,
        "donor_pull_full": i_full, "explicit_label_contribution": delta,
        "S_redacted": bootstrap_mean(s_red), "retention": retention,
        "pairing_validity_ok": validity, "verdict": verdict,
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--raw-dir", type=Path, default=Path("results/raw"))
    p.add_argument("--out", type=Path, default=Path("results/g11_redacted_swap_analysis.json"))
    p.add_argument("--models", nargs="*", default=list(EXPECTED_MODELS))
    args = p.parse_args()
    per_model = {}
    for tag in args.models:
        red = args.raw_dir / f"isr_{tag}_g11_redacted_swap_with.jsonl"
        if red.exists():
            per_model[tag] = analyze_model(
                tag, args.raw_dir / f"isr_{tag}_btf3_large_replication_v1.jsonl",
                args.raw_dir / f"isr_{tag}_g8_swap_with.jsonl", red)
    counted = [m for m in per_model.values() if m["qualified"] and m["pairing_validity_ok"]]
    tally = {v: sum(m["verdict"] == v for m in counted)
             for v in ("survives", "verdict-dependent", "indeterminate")}
    panel = next((v for v in ("survives", "verdict-dependent") if tally[v] >= 2), "indeterminate")
    sentences = {
        "survives": "Explicit answer copying is insufficient: an irrelevant question's outcome evidence still pulls the judgment toward that question's outcome.",
        "verdict-dependent": "The directional import of an irrelevant question's outcome mainly depends on its explicit verdict sentence.",
        "indeterminate": "Verdict redaction does not adjudicate explicit label copying against irrelevant outcome-evidence integration.",
    }
    report = {"preregistration": "PREREGISTRATION_G11_REDACTED_SWAP.md",
              "per_model": per_model, "panel": {"tally": tally, "qualified_models": len(counted), "verdict": panel},
              "permitted_sentence": sentences[panel]}
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report["panel"], indent=2))
    print(sentences[panel])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

