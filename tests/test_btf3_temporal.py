import pandas as pd
import pytest

from src.adapters.btf3_temporal import (
    build_candidate,
    deterministic_review_sample,
    validate_source_row,
)


def row(qid="q1", resolution=1.0):
    return {
        "question_id": qid,
        "question": "Will event X occur by June 1?",
        "resolution_criteria": "YES iff X occurs by June 1.",
        "background": "As of May 1, X had not occurred.",
        "present_date": "2026-05-01 12:00:00",
        "date_cutoff_end": "2026-05-02",
        "expected_resolution_date": "2026-06-01T00:00:00",
        "resolution": resolution,
        "resolution_explanation": "RESOLUTION: YES. X occurred on May 20.",
    }


def test_four_cells_hold_source_text_and_packet_fixed():
    item = build_candidate(row())
    oob = item.oob_variant
    allowed = item.admissible_variant
    assert "RESOLUTION: YES" not in oob["without_information_prompt"]
    assert "RESOLUTION: YES" not in allowed["without_information_prompt"]
    assert "RESOLUTION: YES" in oob["with_information_prompt"]
    assert "RESOLUTION: YES" in allowed["with_information_prompt"]
    for prompt in (
        oob["without_information_prompt"], oob["with_information_prompt"],
        allowed["without_information_prompt"], allowed["with_information_prompt"],
    ):
        assert row()["question"] in prompt
        assert "Return only one number from 0 to 100" in prompt


def test_ex_ante_prompt_uses_present_utc_day_not_cutoff_calendar_day():
    item = build_candidate(row())
    prompt = item.oob_variant["without_information_prompt"]
    assert "through the end of UTC day 2026-05-01" in prompt
    assert "date_cutoff_end=2026-05-02" in prompt
    assert "Do not treat the following UTC calendar day as available" in prompt
    assert "close of UTC day 2026-05-02" not in prompt
    assert item.reference_context["source_utc_day"] == "2026-05-01"


def test_cutoff_encoding_must_be_next_midnight_boundary():
    bad = row()
    bad["date_cutoff_end"] = "2026-05-01"
    with pytest.raises(ValueError, match="unexpected BTF-3 cutoff encoding"):
        validate_source_row(bad)


def test_realized_no_has_negative_alignment_sign():
    item = build_candidate(row(resolution=0.0))
    assert item.reference_context["outcome_alignment_sign"] == -1


def test_review_selection_is_balanced_and_deterministic():
    frame = pd.DataFrame([row(f"yes-{i}", 1.0) for i in range(6)] + [row(f"no-{i}", 0.0) for i in range(6)])
    a = deterministic_review_sample(frame, n_per_resolution=2, seed=9)
    b = deterministic_review_sample(frame, n_per_resolution=2, seed=9)
    assert [x["question_id"] for x in a] == [x["question_id"] for x in b]
    assert [int(x["resolution"]) for x in a].count(0) == 2
    assert [int(x["resolution"]) for x in a].count(1) == 2


def test_rejected_question_can_be_excluded_without_losing_balance():
    frame = pd.DataFrame([row(f"yes-{i}", 1.0) for i in range(6)] + [row(f"no-{i}", 0.0) for i in range(6)])
    initial = deterministic_review_sample(frame, n_per_resolution=2, seed=9)
    rejected_no = next(x["question_id"] for x in initial if int(x["resolution"]) == 0)
    replacement = deterministic_review_sample(
        frame,
        n_per_resolution=2,
        seed=9,
        exclude_question_ids=[rejected_no],
    )
    assert rejected_no not in {x["question_id"] for x in replacement}
    assert [int(x["resolution"]) for x in replacement].count(0) == 2
    assert [int(x["resolution"]) for x in replacement].count(1) == 2
