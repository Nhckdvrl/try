"""M1/M2/M3 manipulation prompt builders for PREREGISTRATION_G1_FACTORIZATION.md.

All three manipulations reuse the already-frozen and already-validated
BTF-3 confirmatory artifact's source text (question, criteria, background,
resolution-explanation packet) verbatim -- no new source content, no new
human review. Only the framing/instructions around that same content
differ per manipulation, and those additions are fixed adapter-authored
strings held identical across every unit within a manipulation.
"""
from __future__ import annotations

import re

try:
    from ..information_set_schema import InformationSetItem
except ImportError:  # direct use with PYTHONPATH=src
    from information_set_schema import InformationSetItem

_PACKET_MARKER = "\n\nLATER RESOLUTION PACKET\n"
_TASK_MARKER = "\n\nTASK\n"

M1_REMINDER = (
    "\n\nREMINDER\nThe information in LATER RESOLUTION PACKET above was not "
    "available at the evaluation point defined above and must not inform "
    "your answer."
)
M2_TASK = (
    "\n\nTASK\nBase your answer only on the AVAILABLE AT T section. The "
    "LEARNED AFTER T section exists in this prompt for completeness but "
    "must not inform your answer. What probability should be assigned to "
    "this question resolving YES? Return only one number from 0 to 100."
)
M2_BOUNDARY_TASK = (
    "\n\nBOUNDARY CHECK\nAt the evaluation point defined above, is the "
    "LEARNED AFTER T section part of the target information set? Return "
    "only YES or NO."
)
M3_PRIOR_TEMPLATE = (
    "\n\nPRIOR ASSESSMENT\nBefore any later information was available, the "
    "assessed probability was {value:g}."
)
M3_TASK = (
    "\n\nTASK\nThe prior assessment above was formed using only information "
    "available at the evaluation point defined above. Restate what the "
    "probability was at that evaluation point using only that same "
    "information -- the prior assessment already reflects it. Return only "
    "one number from 0 to 100."
)


def extract_packet(oob_with_prompt: str) -> str:
    """Pull the exact source-native packet text out of the baseline OOB_WITH prompt."""
    start = oob_with_prompt.index(_PACKET_MARKER) + len(_PACKET_MARKER)
    end = oob_with_prompt.index(_TASK_MARKER, start)
    return oob_with_prompt[start:end]


def build_m1(item: InformationSetItem) -> str:
    """REPEAT-AFTER condition: reminder inserted between the packet and TASK.

    This is the v1 M1 result, reused unchanged in v2 as the REPEAT-AFTER
    arm of the positional control (see PREREGISTRATION_G1_FACTORIZATION_V2.md)
    -- not re-run, since this function's output is identical either way.
    """
    prompt = item.oob_variant["with_information_prompt"]
    idx = prompt.index(_TASK_MARKER)
    return prompt[:idx] + M1_REMINDER + prompt[idx:]


def build_m1_repeat_before(item: InformationSetItem) -> str:
    """REPEAT-BEFORE condition: the identical reminder inserted between the
    TARGET INFORMATION SET framing and the packet, instead of after it.

    Byte-identical reminder text and position count to build_m1 -- only the
    position relative to the inadmissible evidence differs, isolating the
    positional-control variable per PREREGISTRATION_G1_FACTORIZATION_V2.md.
    """
    prompt = item.oob_variant["with_information_prompt"]
    idx = prompt.index(_PACKET_MARKER)
    return prompt[:idx] + M1_REMINDER + prompt[idx:]


def build_m2(item: InformationSetItem) -> tuple[str, str]:
    """Returns (decision_prompt, boundary_probe_prompt)."""
    ctx = item.reference_context
    packet = extract_packet(item.oob_variant["with_information_prompt"])
    source = (
        f"FORECASTING QUESTION\n{ctx['question']}\n\n"
        f"RESOLUTION CRITERIA\n{ctx['resolution_criteria']}\n\n"
        f"AVAILABLE AT T\n{ctx['background']}\n\n"
        f"LEARNED AFTER T\n{packet}"
    )
    return source + M2_TASK, source + M2_BOUNDARY_TASK


_BACKGROUND_HEADER_RE = re.compile(r"\n\nBACKGROUND AVAILABLE AS OF [^\n]*\n")


def build_m2_v2(item: InformationSetItem) -> str:
    """Minimal, surgical fix for v1 M2's missing evaluation-point framing.

    Starts from the exact, already-validated baseline OOB_WITH prompt and
    inserts exactly two label lines -- nothing else changes. The
    TARGET INFORMATION SET framing paragraph, the LATER RESOLUTION PACKET
    header (kept, not renamed, so v1's broken-antecedent bug cannot recur),
    and the TASK question are all byte-identical to baseline. The generic
    boundary_probe() from run_information_set.py is reused unmodified.
    """
    prompt = item.oob_variant["with_information_prompt"]
    background_match = _BACKGROUND_HEADER_RE.search(prompt)
    if not background_match:
        raise ValueError("could not locate the BACKGROUND header in the baseline prompt")
    insert_at = background_match.start() + 2  # right after the leading blank line
    prompt = prompt[:insert_at] + "AVAILABLE AT TARGET TIME\n\n" + prompt[insert_at:]

    packet_idx = prompt.index(_PACKET_MARKER)
    insert_at2 = packet_idx + 2
    prompt = prompt[:insert_at2] + "LEARNED AFTER TARGET TIME\n\n" + prompt[insert_at2:]
    return prompt


def build_m3(item: InformationSetItem, baseline_oob_without_value: float) -> str:
    prompt = item.oob_variant["without_information_prompt"]
    idx = prompt.index(_TASK_MARKER)
    base = prompt[:idx]
    packet = extract_packet(item.oob_variant["with_information_prompt"])
    prior = M3_PRIOR_TEMPLATE.format(value=baseline_oob_without_value)
    later = f"\n\nLATER RESOLUTION PACKET\n{packet}"
    return base + prior + later + M3_TASK
