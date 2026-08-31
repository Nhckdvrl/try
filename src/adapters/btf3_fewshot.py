"""Few-shot demonstration prefix for PREREGISTRATION_G10_FEWSHOT.md.

Three worked demonstrations of correct ex-ante reasoning are prepended to the
frozen out-of-set prompt, in both cells. Each demonstration is a held-out BTF-3
binary question — never one of the 328 units any round has used — shown in the
same shape as the task, with the packet present and visibly not used, and
answered with the dataset's own SOTA ex-ante forecast probability.

Demonstrations are compacted by a frozen rule so three fit the 8,192 budget:
question, the out-of-set sentence, the first three sentences of the packet, and
the answer. No background and no resolution criteria.
"""
from __future__ import annotations

import hashlib
import random
import re
from typing import Any, Iterable

try:
    from .btf3_exclusion_reason import TEMPORAL_SENTENCE
except ImportError:  # direct use with PYTHONPATH=src
    from adapters.btf3_exclusion_reason import TEMPORAL_SENTENCE

SELECTION_SEED = 20260903
N_NO, N_YES = 2, 1
PACKET_SENTENCES = 3
ANCHOR = "sota_forecast_probability"

_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")

HEADER = (
    "WORKED EXAMPLES\n"
    "Each example shows the same task: a forecasting question, a packet that "
    "postdates the evaluation point, and the probability that was warranted "
    "from what was knowable at the time — which does not use the packet.\n"
)


def _first_sentences(text: str, n: int) -> str:
    parts = [p.strip() for p in _SENTENCE_SPLIT.split(str(text).strip()) if p.strip()]
    return " ".join(parts[:n])


def render_demonstration(row: dict[str, Any], index: int) -> str:
    return (
        f"\nExample {index}\n"
        f"FORECASTING QUESTION\n{row['question']}\n"
        f"TARGET INFORMATION SET\n{TEMPORAL_SENTENCE}\n"
        f"LATER RESOLUTION PACKET\n{_first_sentences(row['resolution_explanation'], PACKET_SENTENCES)}\n"
        f"ANSWER: {int(round(float(row[ANCHOR])))}\n"
    )


def select_demonstrations(
    rows: Iterable[dict[str, Any]], used_unit_ids: set[str], *, seed: int = SELECTION_SEED
) -> list[dict[str, Any]]:
    """Two realized-NO and one realized-YES held-out row, chosen to be instructive.

    A demonstration only teaches the behaviour if the warranted ex-ante answer
    is visibly *not* the outcome the packet reveals. Rows are therefore ranked by
    how far the dataset's own ex-ante forecast sits from the realized outcome,
    ``|anchor - 100 * resolution|``, and the largest gaps are taken. Both fields
    are source fields; no model output participates, and the rule is fixed
    before any run.

    ``seed`` only breaks ties, so the selection is deterministic either way.
    """
    eligible = [
        row
        for row in rows
        if str(row["question_id"]) not in used_unit_ids
        and row.get(ANCHOR) is not None
        and row[ANCHOR] == row[ANCHOR]
        and str(row.get("resolution_explanation", "")).strip()
    ]

    def gap(row: dict[str, Any]) -> float:
        return abs(float(row[ANCHOR]) - 100.0 * float(row["resolution"]))

    rng = random.Random(seed)
    order = {str(row["question_id"]): rng.random() for row in eligible}
    ranked = sorted(eligible, key=lambda r: (-gap(r), order[str(r["question_id"])]))
    no = [r for r in ranked if float(r["resolution"]) == 0.0]
    yes = [r for r in ranked if float(r["resolution"]) == 1.0]
    if len(no) < N_NO or len(yes) < N_YES:
        raise ValueError(f"not enough held-out demonstrations: no={len(no)} yes={len(yes)}")
    chosen = no[:N_NO] + yes[:N_YES]
    # Present in a fixed order that does not group the labels together.
    return [chosen[0], chosen[2], chosen[1]]


def build_prefix(demonstrations: list[dict[str, Any]]) -> str:
    body = "".join(render_demonstration(row, i + 1) for i, row in enumerate(demonstrations))
    return HEADER + body + "\nNOW YOUR TASK\n\n"


def prefix_digest(prefix: str) -> str:
    return hashlib.sha256(prefix.encode()).hexdigest()


def build(prompt: str, prefix: str) -> str:
    """Prepend the demonstration prefix to a frozen out-of-set prompt."""
    if TEMPORAL_SENTENCE not in prompt:
        raise ValueError("prompt is not a frozen out-of-set prompt")
    return prefix + prompt
