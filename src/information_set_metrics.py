"""Boundary-agnostic behavioral contract for information-set reasoning."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from math import isfinite
from typing import Iterable

try:
    from .metrics_policy_nonuse import paired_cluster_bootstrap_mean
except ImportError:  # direct script execution
    from metrics_policy_nonuse import paired_cluster_bootstrap_mean


@dataclass(frozen=True)
class InformationSetScores:
    allowed_pos: float
    allowed_neg: float
    outside_pos: float
    outside_neg: float
    direction: int = 1

    def __post_init__(self) -> None:
        values = (self.allowed_pos, self.allowed_neg, self.outside_pos, self.outside_neg)
        if not all(isfinite(float(value)) for value in values):
            raise ValueError("all scores must be finite")
        if self.direction not in (-1, 1):
            raise ValueError("direction must be +1 or -1")


@dataclass(frozen=True)
class InformationSetMetrics:
    responsiveness: float
    out_of_set_intrusion: float
    boundary_selectivity: float

    def to_dict(self) -> dict:
        return asdict(self)


def compute_metrics(scores: InformationSetScores) -> InformationSetMetrics:
    sign = float(scores.direction)
    responsiveness = sign * (scores.allowed_pos - scores.allowed_neg)
    intrusion = sign * (scores.outside_pos - scores.outside_neg)
    return InformationSetMetrics(
        responsiveness=responsiveness,
        out_of_set_intrusion=intrusion,
        boundary_selectivity=responsiveness - intrusion,
    )


def summarize(
    rows: Iterable[tuple[InformationSetScores, str]],
    *,
    n_resamples: int = 10_000,
    seed: int = 0,
) -> dict:
    computed, clusters = [], []
    for scores, independent_unit_id in rows:
        computed.append(compute_metrics(scores))
        clusters.append(independent_unit_id)
    if not computed:
        raise ValueError("no rows")

    def boot(name: str) -> dict:
        return paired_cluster_bootstrap_mean(
            [getattr(row, name) for row in computed],
            clusters,
            n_resamples=n_resamples,
            seed=seed,
        )

    return {
        "responsiveness": boot("responsiveness"),
        "out_of_set_intrusion": boot("out_of_set_intrusion"),
        "boundary_selectivity": boot("boundary_selectivity"),
    }
