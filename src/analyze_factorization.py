"""Analyze M1/M2/M3 manipulations against the already-confirmed BTF-3 baseline.

Per PREREGISTRATION_G1_FACTORIZATION.md: Delta_M = Intrusion_baseline -
Intrusion_M, paired per unit against the already-collected confirmatory
baseline (not re-collected). A manipulation "meaningfully reduces
intrusion" for a model only if Delta_M's bootstrap 95% lower bound is
strictly greater than 0 AND the manipulation's own boundary-probe
accuracy stays at least at the BTF-3 pilot floor ratio (14/16 = 0.875,
applied as a rate since manipulation runs collect one probe per unit
rather than the original two) AND the model's baseline mean ALLOWED_WITH
alignment (carried over, not re-collected, since manipulations never
touch the ALLOWED cells) stays at least 70.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import statistics as st

try:
    from .metrics_policy_nonuse import paired_cluster_bootstrap_mean
except ImportError:  # direct script execution
    from metrics_policy_nonuse import paired_cluster_bootstrap_mean


BOUNDARY_PROBE_FLOOR = 14 / 16
MINIMUM_ALLOWED_WITH_ALIGNMENT = 70.0
MINIMUM_MODELS_FOR_VALIDATED_MECHANISM = 2


def _load(path: Path) -> tuple[dict, list[dict]]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    metadata = next(row for row in rows if row["record_type"] == "metadata")
    return metadata, [row for row in rows if row["record_type"] != "metadata"]


def _baseline_by_unit(path: Path) -> dict[str, dict]:
    _, rows = _load(path)
    by_unit: dict[str, dict] = {}
    for row in rows:
        if row["record_type"] != "decision":
            continue
        by_unit.setdefault(row["independent_unit_id"], {})[row["condition"]] = row
    result = {}
    for unit, conditions in by_unit.items():
        if set(conditions) != {"oob_without", "oob_with", "allowed_without", "allowed_with"}:
            continue
        if any(row["value"] is None for row in conditions.values()):
            continue
        direction = int(conditions["oob_without"].get("direction", 1))
        with_value = conditions["allowed_with"]["value"]
        result[unit] = {
            "oob_without": conditions["oob_without"]["value"],
            "oob_with": conditions["oob_with"]["value"],
            "direction": direction,
            "allowed_with_alignment": with_value if direction == 1 else 100.0 - with_value,
        }
    allowed_alignment = [v["allowed_with_alignment"] for v in result.values()]
    mean_allowed = st.mean(allowed_alignment) if allowed_alignment else None
    return result, mean_allowed


def analyze_one(manipulation_path: Path, baseline_path: Path) -> dict:
    metadata, rows = _load(manipulation_path)
    manipulation = metadata["manipulation"]
    baseline, mean_allowed = _baseline_by_unit(baseline_path)

    decisions = {row["independent_unit_id"]: row for row in rows if row["record_type"] == "decision"}
    probes = [row for row in rows if row["record_type"] == "boundary_probe"]
    boundary_accuracy = sum(bool(row.get("correct")) for row in probes) / len(probes) if probes else 0.0

    deltas, clusters = [], []
    for unit, decision in decisions.items():
        if unit not in baseline:
            continue
        if decision["value"] is None:
            continue
        base = baseline[unit]
        s = base["direction"]
        intrusion_baseline = s * (base["oob_with"] - base["oob_without"])
        intrusion_m = s * (decision["value"] - base["oob_without"])
        deltas.append(intrusion_baseline - intrusion_m)
        clusters.append(unit)

    bootstrap = paired_cluster_bootstrap_mean(deltas, clusters, n_resamples=10_000, seed=20260829) if deltas else None
    meaningfully_reduces = bool(
        bootstrap
        and bootstrap["ci_low"] > 0
        and boundary_accuracy >= BOUNDARY_PROBE_FLOOR
        and mean_allowed is not None
        and mean_allowed >= MINIMUM_ALLOWED_WITH_ALIGNMENT
    )
    return {
        "manipulation": manipulation,
        "model_tag": metadata["model_tag"],
        "model_id": metadata["model_id"],
        "n_paired_units": len(deltas),
        "boundary_probe_accuracy": boundary_accuracy,
        "baseline_mean_allowed_with_alignment": mean_allowed,
        "delta_bootstrap": bootstrap,
        "meaningfully_reduces_intrusion": meaningfully_reduces,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manipulation-result",
        action="append",
        nargs=2,
        metavar=("MANIPULATION_JSONL", "BASELINE_JSONL"),
        required=True,
        help="repeatable: one manipulation-run file paired with that model's confirmatory baseline file",
    )
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    analyses = [analyze_one(Path(m), Path(b)) for m, b in args.manipulation_result]
    by_manipulation: dict[str, list[dict]] = {}
    for result in analyses:
        by_manipulation.setdefault(result["manipulation"], []).append(result)

    manipulation_verdicts = {}
    for manipulation, results in by_manipulation.items():
        count = sum(r["meaningfully_reduces_intrusion"] for r in results)
        manipulation_verdicts[manipulation] = {
            "models_with_meaningful_reduction": count,
            "of_models_tested": len(results),
            "validated_partial_mechanism": count >= MINIMUM_MODELS_FOR_VALIDATED_MECHANISM,
        }

    any_validated = any(v["validated_partial_mechanism"] for v in manipulation_verdicts.values())
    report = {
        "results": analyses,
        "manipulation_verdicts": manipulation_verdicts,
        "at_least_one_manipulation_validated": any_validated,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"manipulation_verdicts": manipulation_verdicts, "at_least_one_manipulation_validated": any_validated}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
