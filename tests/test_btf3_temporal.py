import pandas as pd

from src.adapters.btf3_temporal import build_candidate, deterministic_review_sample


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
