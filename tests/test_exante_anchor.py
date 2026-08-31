"""Tests for the G7 ex-ante anchor analysis and its frozen decision rules."""

from __future__ import annotations

from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from analyze_exante_anchor import frame_stats, interpretation, verdict  # noqa: E402


@pytest.mark.parametrize(
    "delta,expected",
    [
        ({"mean": 5.0, "ci_low": 2.0, "ci_high": 8.0}, "displacement"),
        ({"mean": 2.9, "ci_low": 1.0, "ci_high": 4.5}, "indeterminate"),  # below SESOI
        ({"mean": 5.0, "ci_low": -1.0, "ci_high": 11.0}, "indeterminate"),  # CI includes 0
        ({"mean": 0.5, "ci_low": -2.0, "ci_high": 2.5}, "no_displacement"),
        ({"mean": 0.0, "ci_low": -3.0, "ci_high": 3.0}, "no_displacement"),  # at the margin
        ({"mean": 0.0, "ci_low": -4.0, "ci_high": 3.0}, "indeterminate"),
    ],
)
def test_displacement_rule(delta, expected):
    assert verdict(delta) == expected


@pytest.mark.parametrize(
    "displacement,brier,row",
    [
        ("displacement", -0.05, "displacement_with_accuracy_gain"),
        ("displacement", 0.01, "displacement_without_accuracy_gain"),
        ("no_displacement", -0.05, "no_displacement"),
        ("indeterminate", -0.05, "indeterminate"),
    ],
)
def test_interpretation_table(displacement, brier, row):
    assert interpretation(displacement, brier)[0] == row


def test_frame_stats_on_a_hand_worked_example():
    # Two units. Anchor 20/80. WITHOUT sits on the anchor; WITH is pulled 10
    # points toward the realized outcome in each.
    anchor = {"a": 20.0, "b": 80.0}
    without = {"a": 20.0, "b": 80.0}
    with_ = {"a": 10.0, "b": 90.0}
    resolution = {"a": 0.0, "b": 1.0}
    directions = {"a": -1, "b": 1}

    got = frame_stats(with_, without, anchor, resolution, directions)
    assert got["units"] == 2
    assert got["mad_without"] == pytest.approx(0.0)
    assert got["mad_with"] == pytest.approx(10.0)
    assert got["delta_dev"]["mean"] == pytest.approx(10.0)
    # moving toward the outcome must improve Brier
    assert got["delta_brier"]["mean"] < 0
    # signed gap: WITH is 10 points toward the outcome relative to the anchor
    assert got["signed_gap_without"] == pytest.approx(0.0)
    assert got["signed_gap_with"] == pytest.approx(10.0)


def test_frame_stats_only_uses_units_present_everywhere():
    got = frame_stats(
        {"a": 10.0, "b": 10.0},
        {"a": 20.0},
        {"a": 30.0, "b": 30.0},
        {"a": 0.0, "b": 0.0},
        {"a": 1, "b": 1},
    )
    assert got["units"] == 1
