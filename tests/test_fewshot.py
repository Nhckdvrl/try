"""Tests for the G10 few-shot demonstration prefix."""

from __future__ import annotations

from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_exclusion_reason import TEMPORAL_SENTENCE  # noqa: E402
from adapters.btf3_fewshot import (  # noqa: E402
    build,
    build_prefix,
    prefix_digest,
    render_demonstration,
    select_demonstrations,
)


def _rows():
    """Anchor gap: 90, 80, 95 (yes), 10 (yes), plus one already used."""
    return [
        {"question_id": "n1", "resolution": 0.0, "sota_forecast_probability": 90.0,
         "question": "Q1?", "resolution_explanation": "The question resolves NO. Alpha. Beta. Gamma."},
        {"question_id": "n2", "resolution": 0.0, "sota_forecast_probability": 80.0,
         "question": "Q2?", "resolution_explanation": "The question resolves NO. Delta."},
        {"question_id": "n3", "resolution": 0.0, "sota_forecast_probability": 5.0,
         "question": "Q3?", "resolution_explanation": "Resolves NO."},
        {"question_id": "y1", "resolution": 1.0, "sota_forecast_probability": 5.0,
         "question": "Q4?", "resolution_explanation": "The question resolves YES."},
        {"question_id": "y2", "resolution": 1.0, "sota_forecast_probability": 95.0,
         "question": "Q5?", "resolution_explanation": "The question resolves YES."},
        {"question_id": "used", "resolution": 0.0, "sota_forecast_probability": 99.0,
         "question": "Q6?", "resolution_explanation": "Resolves NO."},
    ]


def test_selects_the_largest_gaps_and_skips_used_units():
    chosen = select_demonstrations(_rows(), {"used"})
    ids = [r["question_id"] for r in chosen]
    assert set(ids) == {"n1", "n2", "y1"}
    assert "used" not in ids
    assert "n3" not in ids  # smallest gap among the NO rows


def test_labels_are_not_grouped():
    resolutions = [float(r["resolution"]) for r in select_demonstrations(_rows(), set())]
    assert resolutions == [0.0, 1.0, 0.0]


def test_selection_is_deterministic():
    a = [r["question_id"] for r in select_demonstrations(_rows(), set())]
    b = [r["question_id"] for r in select_demonstrations(_rows(), set())]
    assert a == b


def test_demonstration_shows_the_packet_and_an_answer_that_is_not_the_outcome():
    row = _rows()[0]
    text = render_demonstration(row, 1)
    assert "LATER RESOLUTION PACKET" in text
    assert TEMPORAL_SENTENCE in text
    assert text.rstrip().endswith("ANSWER: 90")
    # the packet reveals NO while the demonstrated answer is 90 -- the whole point
    assert "resolves NO" in text


def test_packet_is_truncated_to_three_sentences():
    text = render_demonstration(_rows()[0], 1)
    packet_line = [ln for ln in text.splitlines() if ln.startswith("The question resolves NO.")][0]
    assert packet_line == "The question resolves NO. Alpha. Beta."
    assert "Gamma" not in text  # fourth sentence dropped


def test_prefix_is_stable_and_prepended_before_the_task():
    prefix = build_prefix(select_demonstrations(_rows(), set()))
    assert prefix_digest(prefix) == prefix_digest(build_prefix(select_demonstrations(_rows(), set())))
    prompt = f"FORECASTING QUESTION\nreal one\n{TEMPORAL_SENTENCE}\n\nTASK\nanswer."
    built = build(prompt, prefix)
    assert built.startswith(prefix)
    assert built.endswith(prompt)


def test_build_rejects_a_prompt_that_is_not_a_frozen_out_of_set_prompt():
    with pytest.raises(ValueError):
        build("no such sentence here", "prefix")


def test_not_enough_demonstrations_fails_closed():
    with pytest.raises(ValueError, match="not enough"):
        select_demonstrations(_rows()[:1], set())
