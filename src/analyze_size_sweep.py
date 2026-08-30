"""Within-family size trend for Qwen3.5 on the frozen 256-unit artifact.

Every size runs the identical artifact, prompts, decoding, parser, and
thresholds as the large-replication round, so per-size estimates are directly
comparable and every unit is shared across sizes. That pairing is used for the
adjacent-size contrasts; it is *not* used to fit a scaling law — with four
size points that would be overreach, and the preregistration says so.

Reported per size:

    I_s = OutOfSetIntrusion      R_s = Responsiveness      B_s = boundary accuracy

plus paired contrasts  Delta = I_larger - I_smaller  over the shared units.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import random
import statistics as st

try:
    from .analyze_btf3_large_replication import THRESHOLDS, load_result, unit_scores
    from .information_set_metrics import compute_metrics
    from .metrics_policy_nonuse import paired_cluster_bootstrap_mean
except ImportError:  # direct script execution
    from analyze_btf3_large_replication import THRESHOLDS, load_result, unit_scores
    from information_set_metrics import compute_metrics
    from metrics_policy_nonuse import paired_cluster_bootstrap_mean

SEED = 20260829
N_RESAMPLES = 10_000

# Preregistered family and sizes. Parameter counts are the family's nominal
# dense sizes, used only as the x-axis of a descriptive trend.
FAMILY = "Qwen3.5 dense"
SIZE_BILLIONS = {
    "qwen35-2b": 2.0,
    "qwen35-4b": 4.0,
    "qwen35-9b": 9.0,
    "qwen35-27b": 27.0,
}


def per_unit(path: Path) -> dict:
    metadata, rows = load_result(path)
    decisions = [row for row in rows if row["record_type"] == "decision"]
    probes = [row for row in rows if row["record_type"] == "boundary_probe"]
    complete, aligned = unit_scores(rows)
    intrusion = {unit: compute_metrics(scores).out_of_set_intrusion for scores, unit in complete}
    responsiveness = {unit: compute_metrics(scores).responsiveness for scores, unit in complete}
    return {
        "model_tag": metadata["model_tag"],
        "model_id": metadata["model_id"],
        "model_revision": metadata["model_revision"],
        "artifact_sha256": metadata["artifact_sha256"],
        "parse_rate": sum(row["value"] is not None for row in decisions) / len(decisions),
        "boundary_accuracy": sum(bool(row.get("correct")) for row in probes) / len(probes),
        "mean_allowed_with_alignment": st.mean(aligned) if aligned else None,
        "intrusion": intrusion,
        "responsiveness": responsiveness,
    }


def summarize(values: dict[str, float]) -> dict:
    units = sorted(values)
    return paired_cluster_bootstrap_mean(
        [values[unit] for unit in units], units, n_resamples=N_RESAMPLES, seed=SEED
    )


def paired_delta(larger: dict[str, float], smaller: dict[str, float]) -> dict:
    units = sorted(set(larger) & set(smaller))
    diffs = [larger[unit] - smaller[unit] for unit in units]
    rng = random.Random(SEED)
    draws = sorted(st.mean(rng.choice(diffs) for _ in diffs) for _ in range(N_RESAMPLES))
    lo = max(0, int(0.025 * N_RESAMPLES))
    hi = min(N_RESAMPLES - 1, int(0.975 * N_RESAMPLES) - 1)
    return {
        "mean": st.mean(diffs),
        "ci_low": draws[lo],
        "ci_high": draws[hi],
        "n_shared_units": len(units),
        "n_resamples": N_RESAMPLES,
        "seed": SEED,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("results", nargs="+", type=Path, help="one large-replication result file per size")
    parser.add_argument("--expected-artifact-sha256", required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    sizes = {}
    for path in args.results:
        info = per_unit(path)
        if info["artifact_sha256"] != args.expected_artifact_sha256:
            raise ValueError(f"{path}: not run on the frozen large-replication artifact")
        tag = info["model_tag"]
        if tag not in SIZE_BILLIONS:
            raise ValueError(f"{tag} is not a preregistered size of {FAMILY}")
        sizes[tag] = info

    ordered = sorted(sizes, key=lambda tag: SIZE_BILLIONS[tag])
    per_size = []
    for tag in ordered:
        info = sizes[tag]
        intrusion = summarize(info["intrusion"])
        responsiveness = summarize(info["responsiveness"])
        qualified = bool(
            info["parse_rate"] >= THRESHOLDS["minimum_decision_parse_rate"]
            and info["boundary_accuracy"] >= THRESHOLDS["minimum_boundary_accuracy"]
            and responsiveness["mean"] >= THRESHOLDS["minimum_mean_responsiveness_points"]
            and info["mean_allowed_with_alignment"] >= THRESHOLDS["minimum_allowed_with_alignment_points"]
        )
        per_size.append({
            "model_tag": tag,
            "model_id": info["model_id"],
            "model_revision": info["model_revision"],
            "parameters_billions": SIZE_BILLIONS[tag],
            "log10_parameters": math.log10(SIZE_BILLIONS[tag] * 1e9),
            "decision_parse_rate": info["parse_rate"],
            "boundary_accuracy": info["boundary_accuracy"],
            "mean_allowed_with_alignment": info["mean_allowed_with_alignment"],
            "responsiveness": responsiveness,
            "out_of_set_intrusion": intrusion,
            "qualified": qualified,
            "intrusion_pass": bool(qualified and intrusion["ci_low"] > THRESHOLDS["intrusion_sesoi_points"]),
            "n_units": intrusion["n_clusters"],
        })

    contrasts = []
    for smaller, larger in zip(ordered, ordered[1:], strict=False):
        contrasts.append({
            "contrast": f"{larger} - {smaller}",
            "intrusion_delta": paired_delta(sizes[larger]["intrusion"], sizes[smaller]["intrusion"]),
            "boundary_accuracy_delta": sizes[larger]["boundary_accuracy"] - sizes[smaller]["boundary_accuracy"],
        })
    if len(ordered) > 2:
        contrasts.append({
            "contrast": f"{ordered[-1]} - {ordered[0]} (extremes)",
            "intrusion_delta": paired_delta(sizes[ordered[-1]]["intrusion"], sizes[ordered[0]]["intrusion"]),
            "boundary_accuracy_delta": sizes[ordered[-1]]["boundary_accuracy"] - sizes[ordered[0]]["boundary_accuracy"],
        })

    intrusions = [row["out_of_set_intrusion"]["mean"] for row in per_size]
    boundaries = [row["boundary_accuracy"] for row in per_size]
    report = {
        "preregistration": "PREREGISTRATION_G2_QWEN_SIZE_SWEEP.md",
        "family": FAMILY,
        "expected_artifact_sha256": args.expected_artifact_sha256,
        "thresholds": THRESHOLDS,
        "per_size": per_size,
        "adjacent_and_extreme_contrasts": contrasts,
        "trend": {
            "sizes_billions": [row["parameters_billions"] for row in per_size],
            "intrusion_means": intrusions,
            "boundary_accuracies": boundaries,
            "intrusion_monotone_decreasing": all(a >= b for a, b in zip(intrusions, intrusions[1:], strict=False)),
            "intrusion_monotone_increasing": all(a <= b for a, b in zip(intrusions, intrusions[1:], strict=False)),
            "boundary_accuracy_min": min(boundaries),
            "sizes_with_intrusion_pass": sum(row["intrusion_pass"] for row in per_size),
            "note": "descriptive within-family trend over few size points; no scaling law is fitted and no correlation test is reported",
        },
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for row in per_size:
        metrics = row["out_of_set_intrusion"]
        print(
            f'{row["model_tag"]:12s} {row["parameters_billions"]:5.1f}B  '
            f'boundary={row["boundary_accuracy"]:.4f}  R={row["responsiveness"]["mean"]:6.2f}  '
            f'I={metrics["mean"]:6.2f} [{metrics["ci_low"]:.2f}, {metrics["ci_high"]:.2f}]  '
            f'{"PASS" if row["intrusion_pass"] else "no"}'
        )
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
