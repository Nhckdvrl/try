import pandas as pd
import pytest

from src.adapters.btf3_temporal import (
    build_candidate,
    deterministic_candidate_queue,
    deterministic_review_sample,
    render_confirmatory_queue,
    validate_candidate_against_source,
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
    validate_candidate_against_source(item, row())


def test_four_cell_contract_rejects_serialized_prompt_drift():
    source = row()
    item = build_candidate(source)
    item.oob_variant["with_information_prompt"] += "\nUNREGISTERED"
    with pytest.raises(ValueError, match="unregistered prompt drift"):
        validate_candidate_against_source(item, source)


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


def test_candidate_queue_is_deterministic_and_excludes_pilot_ids():
    frame = pd.DataFrame([row(f"yes-{i}", 1.0) for i in range(10)] + [row(f"no-{i}", 0.0) for i in range(10)])
    excluded = ["yes-0", "no-0"]
    a = deterministic_candidate_queue(frame, pool_size=6, seed=9, exclude_question_ids=excluded)
    b = deterministic_candidate_queue(frame, pool_size=6, seed=9, exclude_question_ids=excluded)
    assert [r["question_id"] for r in a[0]] == [r["question_id"] for r in b[0]]
    assert [r["question_id"] for r in a[1]] == [r["question_id"] for r in b[1]]
    assert len(a[0]) == 6 and len(a[1]) == 6
    assert "yes-0" not in {r["question_id"] for r in a[1]}
    assert "no-0" not in {r["question_id"] for r in a[0]}


def test_candidate_queue_prefix_is_stable_when_pool_size_grows():
    frame = pd.DataFrame([row(f"yes-{i}", 1.0) for i in range(10)] + [row(f"no-{i}", 0.0) for i in range(10)])
    small = deterministic_candidate_queue(frame, pool_size=3, seed=9)
    large = deterministic_candidate_queue(frame, pool_size=6, seed=9)
    assert [r["question_id"] for r in small[0]] == [r["question_id"] for r in large[0]][:3]
    assert [r["question_id"] for r in small[1]] == [r["question_id"] for r in large[1]][:3]


def test_confirmatory_queue_renders_four_gates_per_candidate():
    frame = pd.DataFrame([row("yes-1", 1.0), row("no-1", 0.0)])
    queue = deterministic_candidate_queue(frame, pool_size=1, seed=9)
    text = render_confirmatory_queue(queue, artifact_label="t", quota_per_resolution=1)
    assert "pre-cutoff intact" in text
    assert "realized outcome valid" in text
    assert "exact packet factually valid" in text
    assert "criteria unambiguous" in text
    assert "`yes-1`" in text and "`no-1`" in text


def test_multiple_rejected_questions_can_be_excluded_without_losing_balance():
    frame = pd.DataFrame([row(f"yes-{i}", 1.0) for i in range(6)] + [row(f"no-{i}", 0.0) for i in range(6)])
    initial = deterministic_review_sample(frame, n_per_resolution=2, seed=9)
    rejected = [x["question_id"] for x in initial if int(x["resolution"]) == 0]
    replacement = deterministic_review_sample(
        frame,
        n_per_resolution=2,
        seed=9,
        exclude_question_ids=rejected,
    )
    assert not set(rejected) & {x["question_id"] for x in replacement}
    assert [int(x["resolution"]) for x in replacement].count(0) == 2
    assert [int(x["resolution"]) for x in replacement].count(1) == 2
