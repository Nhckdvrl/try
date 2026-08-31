"""Prompt builder for PREREGISTRATION_G3_EXCLUSION_REASON.md.

One manipulation, applied to the frozen 256-unit large-replication artifact
without reselecting, dropping, or rewriting a single unit: the *reason* clause
of the out-of-set sentence is replaced, and nothing else in the prompt moves.

Every out-of-set prompt in the frozen artifact ends its ``TARGET INFORMATION
SET`` block with the byte-identical sentence in ``TEMPORAL_SENTENCE``. Each arm
substitutes a different reason clause into the same sentence frame, so all four
arms share the identical trailing clause and the identical position in the
prompt. The edited sentence precedes ``LATER RESOLUTION PACKET``, so the token
distance between the packet and ``TASK`` is invariant across arms.

The ``temporal`` arm regenerates the frozen prompt byte-for-byte; the audit in
``scripts/audit_exclusion_reason.py`` fails closed unless every one of the 512
digests matches the frozen file.

Nothing here consults any target-model output.
"""
from __future__ import annotations

from typing import Any

try:
    from ..information_set_schema import InformationSetItem
except ImportError:  # direct use with PYTHONPATH=src
    from information_set_schema import InformationSetItem

# The sentence as it appears in the frozen artifact, in both the WITH and the
# WITHOUT out-of-set prompt of all 256 units.
TEMPORAL_SENTENCE = (
    "Any text explicitly labeled LATER RESOLUTION PACKET was produced after "
    "this information set and is not part of the evidence that defines the "
    "requested ex-ante forecast."
)

_PREFIX = "Any text explicitly labeled LATER RESOLUTION PACKET "
_SUFFIX = "is not part of the evidence that defines the requested ex-ante forecast."

# Reason clauses, frozen. Each is spliced between _PREFIX and _SUFFIX, so the
# arms differ in the reason and in nothing else.
REASON_CLAUSES: dict[str, str] = {
    # Identity: _PREFIX + this + _SUFFIX == TEMPORAL_SENTENCE.
    "temporal": "was produced after this information set and ",
    # No reason at all: licensing asserted, nothing said about why.
    "bare": "",
    # Licensing asserted and the packet's truth undercut.
    "unreliable": (
        "was assembled by an unverified automated process, may contain "
        "fabricated claims, and "
    ),
    # Licensing asserted for a non-temporal reason, with truth affirmed.
    "procedural": (
        "was obtained through a channel this forecasting protocol does not "
        "permit for this question; its contents are accurate, but it "
    ),
}

ARMS = ("temporal", "bare", "unreliable", "procedural")
CELLS = ("with", "without")

_CELL_KEY = {"with": "with_information_prompt", "without": "without_information_prompt"}


def reason_sentence(arm: str) -> str:
    """The full replacement sentence for ``arm``."""
    if arm not in REASON_CLAUSES:
        raise ValueError(f"unknown arm {arm!r}")
    return _PREFIX + REASON_CLAUSES[arm] + _SUFFIX


def build(item: InformationSetItem, *, arm: str, cell: str) -> str:
    """Out-of-set prompt for ``arm`` in ``cell``.

    Raises if the frozen sentence is not present exactly once, so a change to
    the artifact can never be silently absorbed.
    """
    if cell not in CELLS:
        raise ValueError(f"unknown cell {cell!r}")
    variant: dict[str, Any] = item.oob_variant
    prompt = variant[_CELL_KEY[cell]]
    if prompt.count(TEMPORAL_SENTENCE) != 1:
        raise ValueError(
            f"frozen out-of-set sentence not found exactly once in "
            f"{item.independent_unit_id} ({cell})"
        )
    return prompt.replace(TEMPORAL_SENTENCE, reason_sentence(arm))


# Sanity guard evaluated at import: the temporal arm must be the identity.
assert reason_sentence("temporal") == TEMPORAL_SENTENCE
