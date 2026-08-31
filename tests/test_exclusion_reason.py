"""Tests for the G3 exclusion-reason builder and its frozen decision rules."""

from __future__ import annotations

from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_exclusion_reason import (  # noqa: E402
    ARMS,
    CELLS,
    TEMPORAL_SENTENCE,
    build,
    reason_sentence,
)
from analyze_exclusion_reason import contrast, interpretation, verdict  # noqa: E402
from information_set_schema import load_jsonl  # noqa: E402

ARTIFACT = ROOT / "data/external/review/btf3_temporal_large_replication_v1.jsonl"
TRAILING = "is not part of the evidence that defines the requested ex-ante forecast."


@pytest.fixture(scope="module")
def items():
    return load_jsonl(ARTIFACT)


def test_temporal_arm_is_the_identity():
    assert reason_sentence("temporal") == TEMPORAL_SENTENCE


def test_every_arm_shares_the_trailing_clause():
    for arm in ARMS:
        assert reason_sentence(arm).endswith(TRAILING)


def test_arms_are_pairwise_distinct():
    sentences = {reason_sentence(arm) for arm in ARMS}
    assert len(sentences) == len(ARMS)


def test_temporal_arm_reproduces_the_frozen_prompts_byte_for_byte(items):
    for item in items:
        for cell in CELLS:
            key = "with_information_prompt" if cell == "with" else "without_information_prompt"
            assert build(item, arm="temporal", cell=cell) == item.oob_variant[key]


def test_edit_is_confined_to_the_target_information_set(items):
    item = items[0]
    for arm in ARMS:
        for cell in CELLS:
            prompt = build(item, arm=arm, cell=cell)
            key = "with_information_prompt" if cell == "with" else "without_information_prompt"
            source = item.oob_variant[key]
            tis = source.index("\n\nTARGET INFORMATION SET\n")
            assert prompt[:tis] == source[:tis]
            if cell == "with":
                marker = "\n\nLATER RESOLUTION PACKET\n"
                assert prompt[prompt.index(marker):] == source[source.index(marker):]


def test_unknown_arm_and_cell_are_rejected(items):
    with pytest.raises(ValueError):
        reason_sentence("nope")
    with pytest.raises(ValueError):
        build(items[0], arm="temporal", cell="sideways")


def test_missing_frozen_sentence_fails_closed(items):
    item = items[0]
    item.oob_variant["with_information_prompt"] = item.oob_variant[
        "with_information_prompt"
    ].replace(TEMPORAL_SENTENCE, "something else")
    with pytest.raises(ValueError):
        build(item, arm="bare", cell="with")


# --- frozen decision rules -------------------------------------------------


@pytest.mark.parametrize(
    "delta,expected",
    [
        ({"mean": 8.0, "ci_low": 3.0, "ci_high": 12.0}, "reduction"),
        ({"mean": 8.0, "ci_low": -1.0, "ci_high": 15.0}, "indeterminate"),  # CI includes 0
        ({"mean": 4.0, "ci_low": 1.0, "ci_high": 7.0}, "indeterminate"),  # below SESOI
        ({"mean": 1.0, "ci_low": -2.0, "ci_high": 4.0}, "no_reduction"),
        ({"mean": 0.0, "ci_low": -5.0, "ci_high": 5.0}, "no_reduction"),  # exactly at margin
        ({"mean": 0.0, "ci_low": -6.0, "ci_high": 5.0}, "indeterminate"),
    ],
)
def test_verdict_rule(delta, expected):
    assert verdict(delta) == expected


@pytest.mark.parametrize(
    "unreliable,procedural,row",
    [
        ("reduction", "no_reduction", "H-truth"),
        ("reduction", "reduction", "H-temporal-not-refuted"),
        ("no_reduction", "no_reduction", "H-inert"),
        ("no_reduction", "reduction", "unanticipated"),
        ("indeterminate", "reduction", "indeterminate"),
        ("reduction", "indeterminate", "indeterminate"),
    ],
)
def test_interpretation_table_is_exhaustive_and_fixed(unreliable, procedural, row):
    assert interpretation(unreliable, procedural)[0] == row


def test_contrast_is_paired_and_signed():
    left = {"a": 10.0, "b": 20.0, "c": 30.0}
    right = {"a": 4.0, "b": 12.0, "c": 21.0}
    result = contrast(left, right)
    assert result["units"] == 3
    assert result["mean"] == pytest.approx((6.0 + 8.0 + 9.0) / 3)
    assert result["ci_low"] <= result["mean"] <= result["ci_high"]


def test_contrast_ignores_units_missing_on_one_side():
    result = contrast({"a": 5.0, "b": 5.0}, {"a": 1.0})
    assert result["units"] == 1
    assert result["mean"] == pytest.approx(4.0)
