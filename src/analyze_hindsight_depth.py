"""Analyze both G2 hindsight-depth experiments on the frozen 256 units.

Experiment A — positional replication:

    PE_exclude = mean_i  s_i * (p_i[pos_oob_before]     - p_i[pos_oob_after])
    PE_allowed = mean_i  s_i * (p_i[pos_allowed_before] - p_i[pos_allowed_after])

The shared baseline cancels inside the difference, so PE needs no
``OOB_WITHOUT`` term; the baseline is still used for descriptive intrusion
levels and for the licensed-frame qualification check.

Experiment B — explicit verdict redaction:

    R_red  = mean_i s_i * (p_i[evr_allowed] - p_i[allowed_without])
    HC_red = mean_i s_i * (p_i[evr_oob]     - p_i[oob_without])
    Amplification = HC_direct - HC_red        (paired, same units)

All intervals are 95% percentile cluster bootstraps over question_id, 10,000
resamples, seed 20260829 — identical to every earlier round.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import random
import statistics as st

try:
    from .metrics_policy_nonuse import paired_cluster_bootstrap_mean
except ImportError:  # direct script execution
    from metrics_policy_nonuse import paired_cluster_bootstrap_mean


SEED = 20260829
N_RESAMPLES = 10_000
PARSE_RATE_FLOOR = 992 / 1024
BOUNDARY_FLOOR = 448 / 512
MIN_RESPONSIVENESS = 15.0
MIN_ALLOWED_WITH_ALIGNMENT = 70.0
INTRUSION_SESOI = 5.0
EQUIVALENCE_MARGIN = 5.0
MIN_MODELS = 2
EXPECTED_MODELS = {"qwen35-9b", "gemma3-12b", "mistral-small-24b"}


def load(path: Path) -> tuple[dict, list[dict]]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    metadata = next(row for row in rows if row["record_type"] == "metadata")
    return metadata, [row for row in rows if row["record_type"] != "metadata"]


def condition_file(path: Path) -> dict:
    metadata, rows = load(path)
    decisions = [row for row in rows if row["record_type"] == "decision"]
    probes = [row for row in rows if row["record_type"] == "boundary_probe"]
    return {
        "model_tag": metadata["model_tag"],
        "condition": metadata["condition"],
        "artifact_sha256": metadata["artifact_sha256"],
        "values": {row["independent_unit_id"]: row["value"] for row in decisions if row["value"] is not None},
        "directions": {row["independent_unit_id"]: int(row.get("direction", 1)) for row in decisions},
        "parse_rate": sum(row["value"] is not None for row in decisions) / len(decisions),
        "boundary_accuracy": sum(bool(row.get("correct")) for row in probes) / len(probes) if probes else 0.0,
    }


def baseline_file(path: Path) -> dict:
    metadata, rows = load(path)
    by_condition: dict[str, dict[str, float]] = {}
    directions: dict[str, int] = {}
    for row in rows:
        if row["record_type"] != "decision" or row["value"] is None:
            continue
        by_condition.setdefault(row["condition"], {})[row["independent_unit_id"]] = row["value"]
        directions[row["independent_unit_id"]] = int(row.get("direction", 1))
    return {
        "model_tag": metadata["model_tag"],
        "artifact_sha256": metadata["artifact_sha256"],
        "conditions": by_condition,
        "directions": directions,
    }


def paired_effect(
    left: dict[str, float], right: dict[str, float], directions: dict[str, int], units: list[str] | None = None
) -> dict | None:
    """Cluster-bootstrapped mean of s * (left - right) over shared units."""
    shared = sorted(set(left) & set(right) & set(directions))
    if units is not None:
        shared = [unit for unit in shared if unit in set(units)]
    if not shared:
        return None
    values = [directions[unit] * (left[unit] - right[unit]) for unit in shared]
    result = paired_cluster_bootstrap_mean(values, shared, n_resamples=N_RESAMPLES, seed=SEED)
    result["units"] = len(shared)
    return result


def difference_ci(left: list[float], right: list[float], clusters: list[str]) -> dict:
    """Paired difference of two per-unit effect vectors on the same clusters."""
    rng = random.Random(SEED)
    paired = [a - b for a, b in zip(left, right, strict=True)]
    draws = []
    for _ in range(N_RESAMPLES):
        draws.append(st.mean(rng.choice(paired) for _ in paired))
    draws.sort()
    lo = max(0, int(0.025 * N_RESAMPLES))
    hi = min(N_RESAMPLES - 1, int(0.975 * N_RESAMPLES) - 1)
    return {
        "mean": st.mean(paired),
        "ci_low": draws[lo],
        "ci_high": draws[hi],
        "n_clusters": len(set(clusters)),
        "n_resamples": N_RESAMPLES,
        "seed": SEED,
    }


def analyze_model(
    *,
    model_tag: str,
    conditions: dict[str, dict],
    baseline: dict,
    redaction_subset: list[str] | None,
) -> dict:
    directions = baseline["directions"]
    oob_without = baseline["conditions"]["oob_without"]
    allowed_without = baseline["conditions"]["allowed_without"]
    oob_with = baseline["conditions"]["oob_with"]
    allowed_with = baseline["conditions"]["allowed_with"]

    aligned = [
        value if directions[unit] == 1 else 100.0 - value
        for unit, value in allowed_with.items()
        if unit in directions
    ]
    mean_allowed_with = st.mean(aligned) if aligned else None

    quality = {
        name: {
            "parse_rate": info["parse_rate"],
            "boundary_accuracy": info["boundary_accuracy"],
            "passes": info["parse_rate"] >= PARSE_RATE_FLOOR and info["boundary_accuracy"] >= BOUNDARY_FLOOR,
        }
        for name, info in conditions.items()
    }
    qualified = bool(
        all(entry["passes"] for entry in quality.values())
        and mean_allowed_with is not None
        and mean_allowed_with >= MIN_ALLOWED_WITH_ALIGNMENT
    )

    # ---- Experiment A
    pe_exclude = paired_effect(
        conditions["pos_oob_before"]["values"], conditions["pos_oob_after"]["values"], directions
    )
    pe_allowed = paired_effect(
        conditions["pos_allowed_before"]["values"], conditions["pos_allowed_after"]["values"], directions
    )
    intrusion_before = paired_effect(conditions["pos_oob_before"]["values"], oob_without, directions)
    intrusion_after = paired_effect(conditions["pos_oob_after"]["values"], oob_without, directions)
    positional_replicates = bool(qualified and pe_exclude and pe_exclude["ci_low"] > 0)
    allowed_equivalent = bool(
        pe_allowed
        and pe_allowed["ci_low"] > -EQUIVALENCE_MARGIN
        and pe_allowed["ci_high"] < EQUIVALENCE_MARGIN
    )

    # ---- Experiment B
    r_red = paired_effect(conditions["evr_allowed"]["values"], allowed_without, directions)
    hc_red = paired_effect(conditions["evr_oob"]["values"], oob_without, directions)
    hc_direct = paired_effect(oob_with, oob_without, directions)
    r_direct = paired_effect(allowed_with, allowed_without, directions)

    shared = sorted(
        set(conditions["evr_oob"]["values"]) & set(oob_with) & set(oob_without) & set(directions)
    )
    amplification = difference_ci(
        [directions[u] * (oob_with[u] - oob_without[u]) for u in shared],
        [directions[u] * (conditions["evr_oob"]["values"][u] - oob_without[u]) for u in shared],
        shared,
    ) if shared else None

    redacted_only = None
    if redaction_subset:
        redacted_only = {
            "n_units_declared": len(redaction_subset),
            "hc_red": paired_effect(conditions["evr_oob"]["values"], oob_without, directions, units=redaction_subset),
            "r_red": paired_effect(conditions["evr_allowed"]["values"], allowed_without, directions, units=redaction_subset),
        }

    evr_leverage_ok = bool(r_red and r_red["mean"] >= MIN_RESPONSIVENESS)
    evr_contamination = bool(qualified and evr_leverage_ok and hc_red and hc_red["ci_low"] > INTRUSION_SESOI)

    return {
        "model_tag": model_tag,
        "condition_quality": quality,
        "mean_allowed_with_alignment": mean_allowed_with,
        "qualified": qualified,
        "experiment_a": {
            "positional_effect_exclude": pe_exclude,
            "positional_effect_allowed": pe_allowed,
            "intrusion_repeat_before": intrusion_before,
            "intrusion_repeat_after": intrusion_after,
            "positional_replicates": positional_replicates,
            "allowed_control_equivalent": allowed_equivalent,
        },
        "experiment_b": {
            "responsiveness_redacted": r_red,
            "responsiveness_direct": r_direct,
            "hindsight_contamination_redacted": hc_red,
            "hindsight_contamination_direct": hc_direct,
            "amplification_direct_minus_redacted": amplification,
            "redacted_subset_only": redacted_only,
            "leverage_gate_passed": evr_leverage_ok,
            "contamination_survives_redaction": evr_contamination,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", nargs="+", type=Path, required=True, help="large-replication raw results, one per model")
    parser.add_argument("--condition", nargs="+", type=Path, required=True, help="all G2 condition files, any order")
    parser.add_argument("--redaction-audit", type=Path, default=Path("results/btf3_evr_redaction_audit.json"))
    parser.add_argument("--expected-artifact-sha256", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    baselines = {}
    for path in args.baseline:
        info = baseline_file(path)
        if info["artifact_sha256"] != args.expected_artifact_sha256:
            raise ValueError(f"{path}: baseline is not the frozen large-replication artifact")
        baselines[info["model_tag"]] = info

    by_model: dict[str, dict[str, dict]] = {}
    for path in args.condition:
        info = condition_file(path)
        if info["artifact_sha256"] != args.expected_artifact_sha256:
            raise ValueError(f"{path}: condition file is not built on the frozen artifact")
        by_model.setdefault(info["model_tag"], {})[info["condition"]] = info

    required = {"pos_oob_before", "pos_oob_after", "pos_allowed_before", "pos_allowed_after", "evr_oob", "evr_allowed"}
    redaction_subset = None
    if args.redaction_audit.exists():
        audit = json.loads(args.redaction_audit.read_text(encoding="utf-8"))
        redaction_subset = [
            row["question_id"] for row in audit["per_item"] if row["verdict_sentences_removed"] > 0
        ]

    results = []
    for model_tag, conditions in sorted(by_model.items()):
        missing = required - set(conditions)
        if missing:
            raise ValueError(f"{model_tag}: missing condition files {sorted(missing)}")
        if model_tag not in baselines:
            raise ValueError(f"{model_tag}: no baseline large-replication file supplied")
        results.append(analyze_model(
            model_tag=model_tag,
            conditions=conditions,
            baseline=baselines[model_tag],
            redaction_subset=redaction_subset,
        ))

    observed = {row["model_tag"] for row in results}
    panel_complete = observed == EXPECTED_MODELS
    qualified = [row for row in results if row["qualified"]]
    positional_models = sum(row["experiment_a"]["positional_replicates"] for row in results)
    allowed_equivalent_models = sum(row["experiment_a"]["allowed_control_equivalent"] for row in results)
    evr_models = sum(row["experiment_b"]["contamination_survives_redaction"] for row in results)

    report = {
        "preregistration": "PREREGISTRATION_G2_HINDSIGHT_DEPTH.md",
        "expected_artifact_sha256": args.expected_artifact_sha256,
        "thresholds": {
            "parse_rate_floor": PARSE_RATE_FLOOR,
            "boundary_accuracy_floor": BOUNDARY_FLOOR,
            "minimum_mean_allowed_with_alignment": MIN_ALLOWED_WITH_ALIGNMENT,
            "minimum_mean_responsiveness_points": MIN_RESPONSIVENESS,
            "intrusion_sesoi_points": INTRUSION_SESOI,
            "equivalence_margin_points": EQUIVALENCE_MARGIN,
            "minimum_models": MIN_MODELS,
        },
        "results": results,
        "observed_models": sorted(observed),
        "panel_complete": panel_complete,
        "qualified_models": len(qualified),
        "experiment_a_positional_models": positional_models,
        "experiment_a_allowed_equivalent_models": allowed_equivalent_models,
        "experiment_a_replicates": bool(panel_complete and positional_models >= MIN_MODELS),
        "experiment_b_models": evr_models,
        "experiment_b_contamination_survives_redaction": bool(panel_complete and evr_models >= MIN_MODELS),
        "redacted_subset_units": len(redaction_subset) if redaction_subset else None,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        key: report[key]
        for key in (
            "panel_complete",
            "qualified_models",
            "experiment_a_positional_models",
            "experiment_a_allowed_equivalent_models",
            "experiment_a_replicates",
            "experiment_b_models",
            "experiment_b_contamination_survives_redaction",
        )
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
