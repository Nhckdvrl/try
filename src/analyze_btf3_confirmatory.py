"""Analyze the preregistered BTF-3 confirmatory replication (64 fresh units)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import statistics as st

try:
    from .information_set_metrics import InformationSetScores, summarize
except ImportError:  # direct script execution
    from information_set_metrics import InformationSetScores, summarize


THRESHOLDS = {
    "minimum_decision_parse_rate": 248 / 256,
    "minimum_boundary_accuracy": 112 / 128,
    "minimum_mean_responsiveness_points": 15.0,
    "minimum_allowed_with_alignment_points": 70.0,
    "intrusion_sesoi_points": 5.0,
    "minimum_qualified_models": 2,
    "minimum_intrusion_models": 2,
}
EXPECTED_MODELS = {"qwen35-9b", "gemma3-12b", "mistral-small-24b"}
EXPECTED_ARTIFACT_SHA256 = "850b40f6bb46f390fd3f59d4bcdb8ea50672cc0a299d48deedbd0b83384f273c"


def load_result(path: Path) -> tuple[dict, list[dict]]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    metadata = next(row for row in rows if row["record_type"] == "metadata")
    return metadata, [row for row in rows if row["record_type"] != "metadata"]


def analyze_one(path: Path) -> dict:
    metadata, rows = load_result(path)
    decisions = [row for row in rows if row["record_type"] == "decision"]
    probes = [row for row in rows if row["record_type"] == "boundary_probe"]
    if metadata["artifact_sha256"] != EXPECTED_ARTIFACT_SHA256:
        raise ValueError(f"unexpected confirmatory artifact hash in {path}")
    parse_rate = sum(row["value"] is not None for row in decisions) / len(decisions)
    boundary_accuracy = sum(bool(row.get("correct")) for row in probes) / len(probes)

    by_unit: dict[str, dict[str, dict]] = {}
    for row in decisions:
        by_unit.setdefault(row["independent_unit_id"], {})[row["condition"]] = row
    complete = []
    allowed_with_alignment = []
    for unit, conditions in by_unit.items():
        if set(conditions) != {"oob_without", "oob_with", "allowed_without", "allowed_with"}:
            continue
        if any(row["value"] is None for row in conditions.values()):
            continue
        direction = int(conditions["oob_without"].get("direction", 1))
        scores = InformationSetScores(
            allowed_pos=conditions["allowed_with"]["value"],
            allowed_neg=conditions["allowed_without"]["value"],
            outside_pos=conditions["oob_with"]["value"],
            outside_neg=conditions["oob_without"]["value"],
            direction=direction,
        )
        complete.append((scores, unit))
        with_value = conditions["allowed_with"]["value"]
        allowed_with_alignment.append(with_value if direction == 1 else 100.0 - with_value)

    metrics = summarize(complete, n_resamples=10_000, seed=20260829) if complete else None
    mean_allowed = st.mean(allowed_with_alignment) if allowed_with_alignment else None
    qualified = bool(
        metrics
        and parse_rate >= THRESHOLDS["minimum_decision_parse_rate"]
        and boundary_accuracy >= THRESHOLDS["minimum_boundary_accuracy"]
        and metrics["responsiveness"]["mean"] >= THRESHOLDS["minimum_mean_responsiveness_points"]
        and mean_allowed >= THRESHOLDS["minimum_allowed_with_alignment_points"]
    )
    intrusion_pass = bool(
        qualified
        and metrics["out_of_set_intrusion"]["ci_low"]
        > THRESHOLDS["intrusion_sesoi_points"]
    )
    return {
        "path": str(path),
        "model_tag": metadata["model_tag"],
        "model_id": metadata["model_id"],
        "model_revision": metadata["model_revision"],
        "artifact_sha256": metadata["artifact_sha256"],
        "decision_parse_rate": parse_rate,
        "boundary_accuracy": boundary_accuracy,
        "complete_units": len(complete),
        "mean_allowed_with_alignment": mean_allowed,
        "metrics": metrics,
        "qualified": qualified,
        "intrusion_pass": intrusion_pass,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("results", nargs="+", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    analyses = [analyze_one(path) for path in args.results]
    observed_models = {result["model_tag"] for result in analyses}
    panel_complete = observed_models == EXPECTED_MODELS
    qualified = sum(result["qualified"] for result in analyses)
    intrusion = sum(result["intrusion_pass"] for result in analyses)
    replicates = bool(
        panel_complete
        and qualified >= THRESHOLDS["minimum_qualified_models"]
        and intrusion >= THRESHOLDS["minimum_intrusion_models"]
    )
    report = {
        "thresholds": THRESHOLDS,
        "results": analyses,
        "qualified_models": qualified,
        "intrusion_pass_models": intrusion,
        "observed_models": sorted(observed_models),
        "panel_complete": panel_complete,
        "btf3_temporal_replicates": replicates,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(
        {
            "qualified_models": qualified,
            "intrusion_pass_models": intrusion,
            "panel_complete": panel_complete,
            "btf3_temporal_replicates": replicates,
        },
        indent=2,
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
