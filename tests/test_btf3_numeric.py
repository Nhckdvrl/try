"""Tests for the G9 numeric-track adapter and its frozen artifact."""

from __future__ import annotations

from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_numeric import (  # noqa: E402
    ANCHOR,
    CUTPOINT,
    build_candidate,
    threshold_sentence,
    validate_candidate_against_source,
    validate_source_row,
)
from information_set_schema import load_jsonl  # noqa: E402

ARTIFACT = ROOT / "data/external/review/btf3_numeric_v1.jsonl"
ARTIFACT_SHA = "cb0c925ade9b76eee71f9a6f9dc695da44fb717510e15a5156e6416967ef6b15"
needs_artifact = pytest.mark.skipif(not ARTIFACT.exists(), reason="artifact not built")


def _row(**overrides):
    row = {
        "question_id": "abc",
        "question": "What will X be?",
        "resolution_criteria": "Resolves as X per the official source.",
        "background": "Some background.",
        "present_date": "2026-05-03 08:14:35.140819",
        "date_cutoff_end": "2026-05-04 00:00:00",
        "expected_resolution_date": "2026-05-08 00:00:00",
        "units": "percent",
        CUTPOINT: 4.3,
        "resolution": 4.1,
        "resolution_explanation": "The official release reported 4.1 percent.",
        ANCHOR: 55.0,
    }
    row.update(overrides)
    return row


def test_threshold_sentence_uses_the_source_cutpoint_and_units():
    assert threshold_sentence(_row()) == (
        "Will the resolved value be strictly less than 4.3 percent?"
    )


def test_knife_edge_resolutions_are_rejected():
    with pytest.raises(ValueError, match="exactly on the cutpoint"):
        validate_source_row(_row(resolution=4.3))


def test_cutoff_encoding_invariant_is_enforced():
    with pytest.raises(ValueError, match="cutoff encoding"):
        validate_source_row(_row(date_cutoff_end="2026-05-06 00:00:00"))


def test_present_date_must_precede_resolution():
    with pytest.raises(ValueError, match="must precede"):
        validate_source_row(_row(expected_resolution_date="2026-05-01 00:00:00"))


def test_empty_required_field_is_rejected():
    with pytest.raises(ValueError, match="is empty"):
        validate_source_row(_row(background="   "))


@pytest.mark.parametrize("resolution,sign", [(4.1, 1), (4.9, -1)])
def test_direction_follows_below_the_cutpoint(resolution, sign):
    item = build_candidate(_row(resolution=resolution))
    assert item.reference_context["outcome_alignment_sign"] == sign
    assert item.reference_context["realized_resolution"] == (1 if sign == 1 else 0)


def test_packet_appears_only_in_the_with_prompts():
    row = _row()
    item = build_candidate(row)
    validate_candidate_against_source(item, row)
    packet = row["resolution_explanation"]
    for variant in (item.oob_variant, item.admissible_variant):
        assert packet not in variant["without_information_prompt"]
        assert variant["with_information_prompt"].count(packet) == 1


def test_source_question_is_carried_verbatim():
    row = _row()
    item = build_candidate(row)
    assert row["question"] in item.oob_variant["with_information_prompt"]
    assert row["resolution_criteria"] in item.oob_variant["with_information_prompt"]


def test_prompt_drift_is_detected():
    row = _row()
    item = build_candidate(row)
    item.oob_variant["with_information_prompt"] += " extra"
    with pytest.raises(ValueError, match="prompt drift"):
        validate_candidate_against_source(item, row)


# --- the frozen artifact ----------------------------------------------------


@needs_artifact
def test_frozen_artifact_shape():
    items = load_jsonl(ARTIFACT)
    assert len(items) == 128
    signs = [i.reference_context["outcome_alignment_sign"] for i in items]
    assert signs.count(1) == 64 and signs.count(-1) == 64
    assert len({i.independent_unit_id for i in items}) == 128


@needs_artifact
def test_frozen_artifact_hash_is_the_recorded_one():
    from information_set_schema import file_sha256

    assert file_sha256(ARTIFACT) == ARTIFACT_SHA


@needs_artifact
def test_frozen_artifact_shares_no_unit_with_the_binary_rounds():
    numeric = {i.independent_unit_id for i in load_jsonl(ARTIFACT)}
    binary = {
        i.independent_unit_id
        for name in (
            "btf3_temporal_large_replication_v1.jsonl",
            "btf3_temporal_confirmatory_v1.jsonl",
        )
        for i in load_jsonl(ROOT / "data/external/review" / name)
    }
    assert not (numeric & binary)


@needs_artifact
def test_every_frozen_unit_carries_an_anchor():
    for item in load_jsonl(ARTIFACT):
        anchor = item.reference_context["exante_anchor"]
        assert anchor is not None and 0.0 <= anchor <= 100.0


@needs_artifact
def test_every_frozen_unit_has_the_out_of_set_sentence_used_by_every_round():
    sentence = (
        "Any text explicitly labeled LATER RESOLUTION PACKET was produced after "
        "this information set and is not part of the evidence that defines the "
        "requested ex-ante forecast."
    )
    for item in load_jsonl(ARTIFACT):
        for key in ("with_information_prompt", "without_information_prompt"):
            assert item.oob_variant[key].count(sentence) == 1
