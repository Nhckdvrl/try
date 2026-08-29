"""Metrics for G1 policy-conditioned causal non-use.

The primary G1 statistic is deliberately a *raw paired effect*, not a ratio.
Stage 3E showed that REI-style ratios become unstable when a manipulation changes
the leverage denominator.  A normalized leakage fraction is therefore secondary
and only defined when the allowed contrast is large enough.

For one semantic unit with two counterfactual values of the critical information:

    ALLOW_POS, ALLOW_NEG, DENY_POS, DENY_NEG

we define

    allowed_sensitivity   = allow_pos - allow_neg
    forbidden_sensitivity = deny_pos  - deny_neg
    policy_suppression    = allowed_sensitivity - forbidden_sensitivity

If ``direction`` is -1, all three are sign-aligned so positive means movement in
the preregistered critical-information direction.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from math import isfinite
from typing import Iterable, Optional
import random
import statistics as st


@dataclass(frozen=True)
class CounterfactualScores:
    allow_pos: float
    allow_neg: float
    deny_pos: float
    deny_neg: float
    direction: int = 1

    def __post_init__(self) -> None:
        vals = (self.allow_pos, self.allow_neg, self.deny_pos, self.deny_neg)
        if not all(isfinite(float(v)) for v in vals):
            raise ValueError("all scores must be finite")
        if self.direction not in (-1, 1):
            raise ValueError("direction must be +1 or -1")


@dataclass(frozen=True)
class NonUseMetrics:
    allowed_sensitivity: float
    forbidden_sensitivity: float
    policy_suppression: float
    leakage_fraction: Optional[float]
    leakage_fraction_defined: bool
    leverage_floor: float

    def to_dict(self) -> dict:
        return asdict(self)


def compute_metrics(
    scores: CounterfactualScores,
    *,
    leverage_floor: float = 0.0,
) -> NonUseMetrics:
    """Compute G1 metrics for one paired semantic unit.

    ``leverage_floor`` is preregistered in *raw outcome units*.  The normalized
    leakage fraction is omitted when the allowed contrast does not clear it.
    Raw sensitivities are always returned.
    """
    if leverage_floor < 0:
        raise ValueError("leverage_floor must be non-negative")

    s = float(scores.direction)
    allowed = s * (scores.allow_pos - scores.allow_neg)
    forbidden = s * (scores.deny_pos - scores.deny_neg)
    suppression = allowed - forbidden

    defined = abs(allowed) > leverage_floor
    frac = (forbidden / allowed) if defined else None

    return NonUseMetrics(
        allowed_sensitivity=allowed,
        forbidden_sensitivity=forbidden,
        policy_suppression=suppression,
        leakage_fraction=frac,
        leakage_fraction_defined=defined,
        leverage_floor=float(leverage_floor),
    )


def paired_cluster_bootstrap_mean(
    values: Iterable[float],
    clusters: Iterable[str],
    *,
    n_resamples: int = 10_000,
    seed: int = 0,
    alpha: float = 0.05,
) -> dict:
    """Cluster bootstrap a mean without pretending rendered variants are IID.

    All observations belonging to a sampled cluster are carried together.  If a
    cluster is sampled twice, all of its observations are duplicated twice.
    Returns the observed mean and percentile interval.
    """
    vals = [float(v) for v in values]
    cls = [str(c) for c in clusters]
    if len(vals) != len(cls):
        raise ValueError("values and clusters must have the same length")
    if not vals:
        raise ValueError("no observations")
    if n_resamples <= 0:
        raise ValueError("n_resamples must be positive")
    if not (0 < alpha < 1):
        raise ValueError("alpha must be in (0, 1)")
    if not all(isfinite(v) for v in vals):
        raise ValueError("all values must be finite")

    by_cluster: dict[str, list[float]] = {}
    for v, c in zip(vals, cls):
        by_cluster.setdefault(c, []).append(v)

    cluster_ids = sorted(by_cluster)
    rng = random.Random(seed)
    boot = []
    for _ in range(n_resamples):
        sampled = [rng.choice(cluster_ids) for _ in cluster_ids]
        draw = [v for c in sampled for v in by_cluster[c]]
        boot.append(st.mean(draw))

    boot.sort()
    lo_i = max(0, int((alpha / 2) * n_resamples))
    hi_i = min(n_resamples - 1, int((1 - alpha / 2) * n_resamples) - 1)
    return {
        "mean": st.mean(vals),
        "ci_low": boot[lo_i],
        "ci_high": boot[hi_i],
        "n_observations": len(vals),
        "n_clusters": len(cluster_ids),
        "n_resamples": n_resamples,
        "alpha": alpha,
    }


def summarize_units(
    rows: Iterable[tuple[CounterfactualScores, str]],
    *,
    leverage_floor: float = 0.0,
    n_resamples: int = 10_000,
    seed: int = 0,
) -> dict:
    """Convenience summary for a family of paired units.

    ``rows`` contains ``(scores, cluster_id)`` pairs.  Raw effects are always
    summarized. Leakage fractions are summarized only over units where the
    preregistered leverage floor is cleared, and the retained count is explicit.
    """
    metrics = []
    clusters = []
    for scores, cluster in rows:
        metrics.append(compute_metrics(scores, leverage_floor=leverage_floor))
        clusters.append(str(cluster))
    if not metrics:
        raise ValueError("no rows")

    def boot(attr: str) -> dict:
        return paired_cluster_bootstrap_mean(
            [getattr(m, attr) for m in metrics],
            clusters,
            n_resamples=n_resamples,
            seed=seed,
        )

    frac_vals = []
    frac_clusters = []
    for m, c in zip(metrics, clusters):
        if m.leakage_fraction_defined:
            assert m.leakage_fraction is not None
            frac_vals.append(m.leakage_fraction)
            frac_clusters.append(c)

    return {
        "allowed_sensitivity": boot("allowed_sensitivity"),
        "forbidden_sensitivity": boot("forbidden_sensitivity"),
        "policy_suppression": boot("policy_suppression"),
        "leakage_fraction": (
            paired_cluster_bootstrap_mean(
                frac_vals,
                frac_clusters,
                n_resamples=n_resamples,
                seed=seed,
            )
            if frac_vals
            else None
        ),
        "leakage_fraction_n_defined": len(frac_vals),
        "leverage_floor": leverage_floor,
    }
