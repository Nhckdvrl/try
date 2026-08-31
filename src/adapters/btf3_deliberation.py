"""Prompt builders for PREREGISTRATION_G5_DELIBERATION.md.

Two manipulations of the ``TASK`` block, and nothing else, on the frozen
256-unit artifact. The single ``TASK`` block is byte-identical across all 1,024
prompts of the artifact (256 units × 2 frames × 2 cells), verified at build
time, so replacing it is a well-defined operation.

* ``cot``   — think before answering, free-form.
* ``state`` — reconstruct the ex-ante information state first, in a fixed
  three-step scaffold, then answer.

Both end with the same frozen answer line, so one strict parser serves every
arm and the direct baseline's readout discipline is preserved.

Nothing here consults any target-model output.
"""
from __future__ import annotations

import re
from typing import Any

try:
    from ..information_set_schema import InformationSetItem
except ImportError:  # direct use with PYTHONPATH=src
    from information_set_schema import InformationSetItem

TASK_BLOCK = (
    "\n\nTASK\nWhat probability should be assigned to this question resolving "
    "YES? Return only one number from 0 to 100."
)

_ANSWER_LINE = (
    "Finish with a final line of exactly the form `ANSWER: N`, where N is one "
    "number from 0 to 100 and nothing else follows it."
)

TASK_BLOCKS: dict[str, str] = {
    # The frozen direct readout, unchanged. Present so the builder can emit the
    # baseline and be checked byte-for-byte against the artifact.
    "direct": TASK_BLOCK,
    "cot": (
        "\n\nTASK\nWhat probability should be assigned to this question "
        "resolving YES? Reason step by step first, then answer. "
        + _ANSWER_LINE
    ),
    "state": (
        "\n\nTASK\nWhat probability should be assigned to this question "
        "resolving YES?\n"
        "Work in three steps.\n"
        "1. List the facts that were available at the evaluation point defined "
        "in TARGET INFORMATION SET.\n"
        "2. State which text in this prompt is outside that information set and "
        "must not affect the answer.\n"
        "3. Using only the facts from step 1, give the probability.\n"
        + _ANSWER_LINE
    ),
}

ARMS = tuple(TASK_BLOCKS)
FRAMES = ("oob", "allowed")
CELLS = ("with", "without")

_CELL_KEY = {"with": "with_information_prompt", "without": "without_information_prompt"}

# Strict final-answer parser. The completion must contain at least one
# `ANSWER: N` line; the last one wins, so a model that restates the format
# earlier in its reasoning is not penalised. The number is captured whole --
# never truncated to a valid prefix -- and then range-checked, so "ANSWER: 240"
# is an unparsed record rather than a silent 24.
_ANSWER_RE = re.compile(r"ANSWER\s*:\s*(\d+(?:\.\d+)?)\s*%?", re.IGNORECASE)


def parse_answer_line(text: str) -> float | None:
    matches = _ANSWER_RE.findall(text)
    if not matches:
        return None
    value = float(matches[-1])
    return value if 0.0 <= value <= 100.0 else None


def build(item: InformationSetItem, *, arm: str, frame: str, cell: str) -> str:
    if arm not in TASK_BLOCKS:
        raise ValueError(f"unknown arm {arm!r}")
    if frame not in FRAMES:
        raise ValueError(f"unknown frame {frame!r}")
    if cell not in CELLS:
        raise ValueError(f"unknown cell {cell!r}")
    variant: dict[str, Any] = item.oob_variant if frame == "oob" else item.admissible_variant
    prompt = variant[_CELL_KEY[cell]]
    if not prompt.endswith(TASK_BLOCK):
        raise ValueError(
            f"frozen TASK block not found at the end of {item.independent_unit_id} "
            f"({frame}/{cell})"
        )
    return prompt[: -len(TASK_BLOCK)] + TASK_BLOCKS[arm]


assert TASK_BLOCKS["direct"] == TASK_BLOCK
