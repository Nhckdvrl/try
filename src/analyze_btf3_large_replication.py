"""Analyze the preregistered BTF-3 Large Replication v1 (256 fresh units).

Identical estimands, inference, and gates to the 64-unit confirmatory round;
only the parse-rate and boundary-probe denominators scale with sample size, at
exactly the confirmatory ratios (248/256 -> 992/1024, 112/128 -> 448/512).

The replication verdict is decided by these 256 units alone. Pooling with the
confirmatory 64 is a separate, explicitly secondary analysis
(``analyze_btf3_cross_round``) and can never rescue a failed replication.
"""

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
    "minimum_decision_parse_rate": 992 / 1024,
    "minimum_boundary_accuracy": 448 / 512,
    "minimum_mean_responsiveness_points": 15.0,
    "minimum_allowed_with_alignment_points": 70.0,
    "intrusion_sesoi_points": 5.0,
    "minimum_qualified_models": 2,
    "minimum_intrusion_models": 2,
}
EXPECTED_MODELS = {"qwen35-9b", "gemma3-12b", "mistral-small-24b"}
CONDITIONS = {"oob_without", "oob_with", "allowed_without", "allowed_with"}


def load_result(path: Path) -> tuple[dict, list[dict]]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    metadata = next(row for row in rows if row["record_type"] == "metadata")
    return metadata, [row for row in rows if row["record_type"] != "metadata"]


def unit_scores(rows: list[dict]) -> tuple[list[tuple[InformationSetScores, str]], list[float]]:
    by_unit: dict[str, dict[str, dict]] = {}
    for row in rows:
        if row["record_type"] == "decision":
            by_unit.setdefault(row["independent_unit_id"], {})[row["condition"]] = row
    complete: list[tuple[InformationSetScores, str]] = []
    allowed_with_alignment: list[float] = []
    for unit, conditions in by_unit.items():
        if set(conditions) != CONDITIONS:
            continue
        if any(row["value"] is None for row in conditions.values()):
            continue
        direction = int(conditions["oob_without"].get("direction", 1))
        complete.append((
            InformationSetScores(
                allowed_pos=conditions["allowed_with"]["value"],
                allowed_neg=conditions["allowed_without"]["value"],
                outside_pos=conditions["oob_with"]["value"],
                outside_neg=conditions["oob_without"]["value"],
                direction=direction,
            ),
            unit,
        ))
        value = conditions["allowed_with"]["value"]
        allowed_with_alignment.append(value if direction == 1 else 100.0 - value)
    return complete, allowed_with_alignment


def analyze_one(path: Path, *, expected_artifact_sha256: str) -> dict:
    metadata, rows = load_result(path)
    if metadata["artifact_sha256"] != expected_artifact_sha256:
        raise ValueError(
            f"{path}: artifact hash {metadata['artifact_sha256']} is not the frozen "
            f"large-replication artifact {expected_artifact_sha256}"
        )
    decisions = [row for row in rows if row["record_type"] == "decision"]
    probes = [row for row in rows if row["record_type"] == "boundary_probe"]
    parse_rate = sum(row["value"] is not None for row in decisions) / len(decisions)
    boundary_accuracy = sum(bool(row.get("correct")) for row in probes) / len(probes)

    complete, allowed_with_alignment = unit_scores(rows)
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
        qualified and metrics["out_of_set_intrusion"]["ci_low"] > THRESHOLDS["intrusion_sesoi_points"]
    )
    return {
        "path": str(path),
        "model_tag": metadata["model_tag"],
        "model_id": metadata["model_id"],
        "model_revision": metadata["model_revision"],
        "artifact_sha256": metadata["artifact_sha256"],
        "n_decisions": len(decisions),
        "n_probes": len(probes),
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
    parser.add_argument(
        "--expected-artifact-sha256",
        required=True,
        help="SHA-256 of the frozen artifact recorded in the freeze report, tagged before any model run",
    )
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    analyses = [
        analyze_one(path, expected_artifact_sha256=args.expected_artifact_sha256)
        for path in args.results
    ]
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
        "round_id": "btf3_large_replication_v1",
        "thresholds": THRESHOLDS,
        "expected_artifact_sha256": args.expected_artifact_sha256,
        "results": analyses,
        "qualified_models": qualified,
        "intrusion_pass_models": intrusion,
        "observed_models": sorted(observed_models),
        "panel_complete": panel_complete,
        "btf3_large_replication_v1": replicates,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(
        {
            "qualified_models": qualified,
            "intrusion_pass_models": intrusion,
            "panel_complete": panel_complete,
            "btf3_large_replication_v1": replicates,
        },
        indent=2,
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
