"""Secondary cross-round analysis: confirmatory (64) vs large replication (256).

This is explicitly **not** a gate. The large-replication verdict is decided by
its own 256 units in ``analyze_btf3_large_replication``; a pooled estimate can
never convert a failed replication into a success. What this answers is a
different, descriptive question: is the effect magnitude stable across rounds?

Two views are reported per model:

A. pooled question-level, N = 64 + 256 = 320, every question equally weighted
   (the 8 discovery-pilot units are never pooled);
B. round-stratified, with the between-round difference
   ``delta = I_large_replication - I_confirmatory`` and a percentile bootstrap
   CI from independently resampling the clusters of each round.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import random
import statistics as st

try:
    from .analyze_btf3_large_replication import load_result, unit_scores
    from .information_set_metrics import compute_metrics
    from .metrics_policy_nonuse import paired_cluster_bootstrap_mean
except ImportError:  # direct script execution
    from analyze_btf3_large_replication import load_result, unit_scores
    from information_set_metrics import compute_metrics
    from metrics_policy_nonuse import paired_cluster_bootstrap_mean


SEED = 20260829
N_RESAMPLES = 10_000
METRICS = ("responsiveness", "out_of_set_intrusion", "boundary_selectivity")


def round_values(path: Path) -> dict[str, dict[str, float]]:
    """Per-unit metric values for one model-round result file."""
    _, rows = load_result(path)
    complete, _ = unit_scores(rows)
    out: dict[str, dict[str, float]] = {}
    for scores, unit in complete:
        metrics = compute_metrics(scores)
        out[unit] = {name: getattr(metrics, name) for name in METRICS}
    return out


def difference_ci(
    left: list[float], right: list[float], *, seed: int = SEED, n_resamples: int = N_RESAMPLES
) -> dict:
    """Percentile bootstrap CI for mean(left) - mean(right), rounds resampled independently."""
    rng = random.Random(seed)
    draws = []
    for _ in range(n_resamples):
        a = st.mean(rng.choice(left) for _ in left)
        b = st.mean(rng.choice(right) for _ in right)
        draws.append(a - b)
    draws.sort()
    lo = max(0, int(0.025 * n_resamples))
    hi = min(n_resamples - 1, int(0.975 * n_resamples) - 1)
    return {
        "delta": st.mean(left) - st.mean(right),
        "ci_low": draws[lo],
        "ci_high": draws[hi],
        "n_left": len(left),
        "n_right": len(right),
        "n_resamples": n_resamples,
        "seed": seed,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--confirmatory", nargs="+", type=Path, required=True)
    parser.add_argument("--large-replication", nargs="+", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    def by_model(paths: list[Path]) -> dict[str, Path]:
        mapping: dict[str, Path] = {}
        for path in paths:
            metadata, _ = load_result(path)
            mapping[metadata["model_tag"]] = path
        return mapping

    confirmatory = by_model(list(args.confirmatory))
    large = by_model(list(args.large_replication))
    shared = sorted(set(confirmatory) & set(large))
    if not shared:
        raise ValueError("no model appears in both rounds")

    results = {}
    for tag in shared:
        conf = round_values(confirmatory[tag])
        rep = round_values(large[tag])
        overlap = sorted(set(conf) & set(rep))
        if overlap:
            raise ValueError(f"{tag}: rounds share question_ids, which must never happen: {overlap[:5]}")
        pooled_units = {**conf, **rep}
        entry: dict[str, object] = {
            "confirmatory_path": str(confirmatory[tag]),
            "large_replication_path": str(large[tag]),
            "n_confirmatory_units": len(conf),
            "n_large_replication_units": len(rep),
            "n_pooled_units": len(pooled_units),
            "pooled_question_level": {},
            "round_stratified": {},
        }
        for name in METRICS:
            units = sorted(pooled_units)
            entry["pooled_question_level"][name] = paired_cluster_bootstrap_mean(  # type: ignore[index]
                [pooled_units[unit][name] for unit in units],
                units,
                n_resamples=N_RESAMPLES,
                seed=SEED,
            )
            conf_values = [conf[unit][name] for unit in sorted(conf)]
            rep_values = [rep[unit][name] for unit in sorted(rep)]
            entry["round_stratified"][name] = {  # type: ignore[index]
                "confirmatory": paired_cluster_bootstrap_mean(
                    conf_values, sorted(conf), n_resamples=N_RESAMPLES, seed=SEED
                ),
                "large_replication": paired_cluster_bootstrap_mean(
                    rep_values, sorted(rep), n_resamples=N_RESAMPLES, seed=SEED
                ),
                "delta_large_minus_confirmatory": difference_ci(rep_values, conf_values),
            }
        results[tag] = entry

    report = {
        "status": "SECONDARY — descriptive only; never a replication gate",
        "seed": SEED,
        "n_resamples": N_RESAMPLES,
        "discovery_pilot_pooled": False,
        "models": results,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(
        {
            tag: {
                "pooled_intrusion_mean": entry["pooled_question_level"]["out_of_set_intrusion"]["mean"],  # type: ignore[index]
                "delta": entry["round_stratified"]["out_of_set_intrusion"]["delta_large_minus_confirmatory"],  # type: ignore[index]
            }
            for tag, entry in results.items()
        },
        indent=2,
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
