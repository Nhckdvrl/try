"""Pilot P4 irrelevant-visible evidence control (registration §12, user ruling 2026-09-26).

P4 completes RQ3: it decomposes the post-retraction state into (i) the
operator/frame, (ii) having seen *any* visible decision-irrelevant content,
(iii) having seen decision-relevant evidence.  Exactly two cells:

* ``irrelevant_visible`` — CLAIM + ``EVIDENCE E`` (a natural but
  decision-irrelevant text; material rule frozen in §12) + the original
  question; NO ruling.  Block layout byte-mirrors P3's ``withheld_only``
  with content present.
* ``irrelevant_cf``      — the same evidence block + the
  CounterfactualDeletePost ruling, character-identical to P1/P2.
  Block layout byte-mirrors P3's ``withheld_cf``.

Unlike P3 (whose withheld block is a module constant), the EVIDENCE E
content is per-claim and IS read from ``item.critical_evidence`` — which the
build script fills ONLY with the screened irrelevant text sampled from
*other* rows of the audited P2 pool (page-disjoint + no shared length≥5
token; seeded ``Random("20260928:<p2_id>")``; rule frozen in §12 pre-run).
The build script and the verifier both assert that the target claim's own
two evidence texts never appear in any P4 prompt.

Dispatch happens on the condition name BEFORE the g24a branch inside
``schema._blocks`` — the same pattern proven for g25 / g26 / g24p1 /
g24p3.  No existing condition name collides, so every other item file
keeps its prompts bit-for-bit.

Wording + material rule frozen in registration §12 (2026-09-26, pre-run).
Usage: python scripts/verify_g24a_p4_prompts.py checks these invariants.
"""

import conditions_g24a as g24a
import conditions_g24p1 as g24p1

G24P4_CONDITIONS = ["irrelevant_visible", "irrelevant_cf"]


def is_g24p4(cond: str) -> bool:
    return cond in G24P4_CONDITIONS


def blocks(item, cond: str) -> list[str]:
    """Ordered context blocks for one Pilot P4 irrelevant-visible cell."""
    B = g24a.CLAIM_HEADER + "\n" + item.base_context
    E = g24a.EVIDENCE_HEADER + "\n" + item.critical_evidence
    if cond == "irrelevant_visible":
        return [B, E]
    if cond == "irrelevant_cf":
        return [B, E, "RULING\n" + g24p1.CF_DELETE_RULE]
    raise ValueError(f"unknown G24P4 condition {cond!r}")
