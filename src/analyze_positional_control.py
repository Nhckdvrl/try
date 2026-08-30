"""Analyze the M1 positional control (REPEAT-BEFORE vs REPEAT-AFTER).

Per PREREGISTRATION_G1_FACTORIZATION_V2.md:

    PositionalEffect = Intrusion_before - Intrusion_after

paired per unit against the same shared baseline OOB_WITHOUT value.
REPEAT-AFTER reuses v1's already-collected M1 results; only REPEAT-BEFORE
is new data collected under this document.
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
MINIMUM_MODELS_FOR_POSITIONAL_EFFECT = 2


def _load(path: Path) -> tuple[dict, list[dict]]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    metadata = next(row for row in rows if row["record_type"] == "metadata")
    return metadata, [row for row in rows if row["record_type"] != "metadata"]


def _baseline_oob_without(path: Path) -> dict[str, dict]:
    _, rows = _load(path)
    out = {}
    for row in rows:
        if row["record_type"] == "decision" and row["condition"] == "oob_without" and row["value"] is not None:
            out[row["independent_unit_id"]] = {
                "value": row["value"],
                "direction": int(row.get("direction", 1)),
            }
    return out


def _condition_values(path: Path) -> tuple[dict[str, float], float, list[dict]]:
    """Returns (unit -> decision value, boundary_probe_accuracy, boundary probe rows)."""
    metadata, rows = _load(path)
    decisions = {r["independent_unit_id"]: r["value"] for r in rows if r["record_type"] == "decision" and r["value"] is not None}
    probes = [r for r in rows if r["record_type"] == "boundary_probe"]
    accuracy = sum(bool(r.get("correct")) for r in probes) / len(probes) if probes else 0.0
    return decisions, accuracy, metadata


def analyze_one_model(
    *, before_path: Path, after_path: Path, baseline_path: Path, allowed_with_mean: float
) -> dict:
    baseline = _baseline_oob_without(baseline_path)
    before_values, before_acc, before_meta = _condition_values(before_path)
    after_values, after_acc, after_meta = _condition_values(after_path)

    deltas, clusters = [], []
    for unit, base in baseline.items():
        if unit not in before_values or unit not in after_values:
            continue
        s = base["direction"]
        intrusion_before = s * (before_values[unit] - base["value"])
        intrusion_after = s * (after_values[unit] - base["value"])
        deltas.append(intrusion_before - intrusion_after)
        clusters.append(unit)

    bootstrap = paired_cluster_bootstrap_mean(deltas, clusters, n_resamples=10_000, seed=20260829) if deltas else None
    position_matters = bool(
        bootstrap
        and bootstrap["ci_low"] > 0
        and before_acc >= BOUNDARY_PROBE_FLOOR
        and after_acc >= BOUNDARY_PROBE_FLOOR
        and allowed_with_mean >= MINIMUM_ALLOWED_WITH_ALIGNMENT
    )
    return {
        "model_tag": before_meta["model_tag"],
        "n_paired_units": len(deltas),
        "repeat_before_boundary_accuracy": before_acc,
        "repeat_after_boundary_accuracy": after_acc,
        "baseline_mean_allowed_with_alignment": allowed_with_mean,
        "positional_effect_bootstrap": bootstrap,
        "position_matters": position_matters,
    }


def _mean_allowed_with_alignment(baseline_path: Path) -> float | None:
    _, rows = _load(baseline_path)
    by_unit: dict[str, dict] = {}
    for row in rows:
        if row["record_type"] == "decision":
            by_unit.setdefault(row["independent_unit_id"], {})[row["condition"]] = row
    values = []
    for conditions in by_unit.values():
        if set(conditions) != {"oob_without", "oob_with", "allowed_without", "allowed_with"}:
            continue
        if any(r["value"] is None for r in conditions.values()):
            continue
        direction = int(conditions["oob_without"].get("direction", 1))
        with_value = conditions["allowed_with"]["value"]
        values.append(with_value if direction == 1 else 100.0 - with_value)
    return st.mean(values) if values else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        action="append",
        nargs=3,
        metavar=("REPEAT_BEFORE_JSONL", "REPEAT_AFTER_JSONL", "BASELINE_JSONL"),
        required=True,
    )
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    results = []
    for before, after, baseline in args.model:
        allowed_mean = _mean_allowed_with_alignment(Path(baseline))
        results.append(
            analyze_one_model(
                before_path=Path(before), after_path=Path(after), baseline_path=Path(baseline),
                allowed_with_mean=allowed_mean,
            )
        )

    count = sum(r["position_matters"] for r in results)
    verdict = {
        "models_with_position_effect": count,
        "of_models_tested": len(results),
        "positional_effect_validated": count >= MINIMUM_MODELS_FOR_POSITIONAL_EFFECT,
    }
    report = {"results": results, "verdict": verdict}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
