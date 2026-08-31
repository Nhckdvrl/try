"""Tests for the G5 deliberation builder, parser, and frozen decision rules."""

from __future__ import annotations

from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_deliberation import (  # noqa: E402
    ARMS,
    CELLS,
    FRAMES,
    TASK_BLOCK,
    TASK_BLOCKS,
    build,
    parse_answer_line,
)
from information_set_schema import load_jsonl  # noqa: E402

ARTIFACT = ROOT / "data/external/review/btf3_temporal_large_replication_v1.jsonl"


@pytest.fixture(scope="module")
def items():
    return load_jsonl(ARTIFACT)


def test_frozen_task_block_ends_every_prompt(items):
    for item in items:
        for variant in (item.oob_variant, item.admissible_variant):
            for key in ("with_information_prompt", "without_information_prompt"):
                assert variant[key].endswith(TASK_BLOCK)


def test_direct_arm_reproduces_the_frozen_prompts(items):
    for item in items[:20]:
        for frame in FRAMES:
            for cell in CELLS:
                variant = item.oob_variant if frame == "oob" else item.admissible_variant
                key = "with_information_prompt" if cell == "with" else "without_information_prompt"
                assert build(item, arm="direct", frame=frame, cell=cell) == variant[key]


def test_only_the_task_block_changes(items):
    item = items[0]
    source = item.oob_variant["with_information_prompt"]
    head = source[: -len(TASK_BLOCK)]
    for arm in ARMS:
        prompt = build(item, arm=arm, frame="oob", cell="with")
        assert prompt.startswith(head)
        assert prompt[len(head):] == TASK_BLOCKS[arm]


def test_both_deliberation_arms_request_the_same_answer_line():
    for arm in ("cot", "state"):
        assert "ANSWER: N" in TASK_BLOCKS[arm]


def test_unknown_arm_frame_cell_rejected(items):
    for kwargs in (
        {"arm": "nope", "frame": "oob", "cell": "with"},
        {"arm": "cot", "frame": "sideways", "cell": "with"},
        {"arm": "cot", "frame": "oob", "cell": "maybe"},
    ):
        with pytest.raises(ValueError):
            build(items[0], **kwargs)


def test_missing_task_block_fails_closed(items):
    item = items[0]
    item.oob_variant["with_information_prompt"] += " trailing"
    with pytest.raises(ValueError):
        build(item, arm="cot", frame="oob", cell="with")


@pytest.mark.parametrize(
    "text,expected",
    [
        ("blah blah\nANSWER: 42", 42.0),
        ("ANSWER: 7\nsome noise\nANSWER: 12", 12.0),  # last one wins
        ("answer: 100", 100.0),
        ("ANSWER:3.5", 3.5),
        ("ANSWER: 55%", 55.0),
        ("I think it is 42.", None),  # bare number is not accepted
        ("ANSWER: one hundred", None),
        ("reasoning with no answer line", None),
        ("", None),
    ],
)
def test_strict_answer_parser(text, expected):
    assert parse_answer_line(text) == expected


def test_parser_rejects_out_of_range():
    assert parse_answer_line("ANSWER: 240") is None
