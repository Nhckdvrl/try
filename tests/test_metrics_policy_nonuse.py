import math

import pytest

from src.metrics_policy_nonuse import paired_cluster_bootstrap_mean


def test_cluster_estimand_weights_semantic_units_equally():
    summary = paired_cluster_bootstrap_mean(
        [0.0, 0.0, 0.0, 10.0],
        ["many", "many", "many", "single"],
        n_resamples=200,
        seed=7,
    )
    assert summary["mean"] == 5.0
    assert summary["n_observations"] == 4
    assert summary["n_clusters"] == 2


def test_copying_a_rendering_does_not_change_estimate_or_bootstrap():
    original = paired_cluster_bootstrap_mean(
        [2.0, 8.0], ["a", "b"], n_resamples=500, seed=19
    )
    duplicated = paired_cluster_bootstrap_mean(
        [2.0] * 10 + [8.0], ["a"] * 10 + ["b"], n_resamples=500, seed=19
    )
    for key in ("mean", "ci_low", "ci_high"):
        assert duplicated[key] == original[key]


def test_multiple_renderings_are_averaged_inside_cluster_first():
    summary = paired_cluster_bootstrap_mean(
        [0.0, 4.0, 8.0], ["a", "a", "b"], n_resamples=100, seed=3
    )
    assert math.isclose(summary["mean"], 5.0)  # mean(mean(0,4), mean(8))
    assert summary["cluster_size_min"] == 1
    assert summary["cluster_size_max"] == 2


def test_empty_cluster_id_is_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        paired_cluster_bootstrap_mean([1.0], [""], n_resamples=10)
