"""Analyze the FOMC 12+12 source-qualification pilot (temporal replication candidate)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import statistics as st

try:
    from .information_set_metrics import InformationSetScores, summarize
except ImportError:  # direct script execution
    from information_set_metrics import InformationSetScores, summarize


# Ratios scaled from BTF-3's own pilot ratios (31/32, 14/16) to N=24 units:
# 4 decisions/unit -> 96 decisions, 2 probes/unit -> 48 probes. See
# FOMC_TRANSFORMATION_CONTRACT.md's "Frozen pilot qualification thresholds".
THRESHOLDS = {
    "minimum_decision_parse_rate": 93 / 96,
    "minimum_boundary_accuracy": 42 / 48,
    "minimum_mean_responsiveness_points": 15.0,
    "minimum_allowed_with_alignment_points": 70.0,
    "intrusion_sesoi_points": 5.0,
    "minimum_qualified_models": 2,
    "minimum_intrusion_models": 2,
}
EXPECTED_MODELS = {"qwen35-9b", "gemma3-12b", "mistral-small-24b"}
EXPECTED_ARTIFACT_SHA256 = "d628ee999424bc6c8820089e5244c850c45d377da20808cb63aba2e97e7020e4"


def load_result(path: Path) -> tuple[dict, list[dict]]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    metadata = next(row for row in rows if row["record_type"] == "metadata")
    return metadata, [row for row in rows if row["record_type"] != "metadata"]


def _next_meeting_year(independent_unit_id: str) -> str:
    # independent_unit_id is "{previous_date}_{next_date}", both YYYYMMDD.
    return independent_unit_id.split("_")[1][:4]


def analyze_one(path: Path) -> dict:
    metadata, rows = load_result(path)
    decisions = [row for row in rows if row["record_type"] == "decision"]
    probes = [row for row in rows if row["record_type"] == "boundary_probe"]
    if metadata["artifact_sha256"] != EXPECTED_ARTIFACT_SHA256:
        raise ValueError(f"unexpected FOMC pilot artifact hash in {path}")
    parse_rate = sum(row["value"] is not None for row in decisions) / len(decisions)
    boundary_accuracy = sum(bool(row.get("correct")) for row in probes) / len(probes)

    by_unit: dict[str, dict[str, dict]] = {}
    for row in decisions:
        by_unit.setdefault(row["independent_unit_id"], {})[row["condition"]] = row
    complete_by_year = []  # (scores, year) -- PRIMARY clustering
    complete_by_unit = []  # (scores, unit) -- secondary sensitivity clustering
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
        complete_by_year.append((scores, _next_meeting_year(unit)))
        complete_by_unit.append((scores, unit))
        with_value = conditions["allowed_with"]["value"]
        allowed_with_alignment.append(with_value if direction == 1 else 100.0 - with_value)

    metrics_year = summarize(complete_by_year, n_resamples=10_000, seed=20260829) if complete_by_year else None
    metrics_unit = summarize(complete_by_unit, n_resamples=10_000, seed=20260829) if complete_by_unit else None
    mean_allowed = st.mean(allowed_with_alignment) if allowed_with_alignment else None
    qualified = bool(
        metrics_year
        and parse_rate >= THRESHOLDS["minimum_decision_parse_rate"]
        and boundary_accuracy >= THRESHOLDS["minimum_boundary_accuracy"]
        and metrics_year["responsiveness"]["mean"] >= THRESHOLDS["minimum_mean_responsiveness_points"]
        and mean_allowed >= THRESHOLDS["minimum_allowed_with_alignment_points"]
    )
    intrusion_pass = bool(
        qualified
        and metrics_year["out_of_set_intrusion"]["ci_low"]
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
        "complete_units": len(complete_by_unit),
        "mean_allowed_with_alignment": mean_allowed,
        "metrics_primary_year_clustered": metrics_year,
        "metrics_secondary_unit_clustered": metrics_unit,
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
    fomc_temporal_pilot_qualifies = bool(
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
        "fomc_temporal_pilot_qualifies": fomc_temporal_pilot_qualifies,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(
        {
            "qualified_models": qualified,
            "intrusion_pass_models": intrusion,
            "panel_complete": panel_complete,
            "fomc_temporal_pilot_qualifies": fomc_temporal_pilot_qualifies,
        },
        indent=2,
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
