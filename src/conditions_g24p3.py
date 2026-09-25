"""Pilot P3 operator-only control conditions (registration §11, user ruling 2026-09-26).

P3 removes evidence content entirely: neither the support nor the refute
evidence of the P2 pairs is ever rendered, so there are no arms.  Five cells:

* ``base``            — NOT re-implemented here: P3 items keep task_family
                        "g24a_vitaminc", so this cell falls through to the
                        *unmodified* ``conditions_g24a.blocks`` and is
                        byte-identical to P2's Base by construction (it is a
                        re-run of the same prompt, absorbing temp-0 drift,
                        not a comparison against last round's rows);
* ``prior_only``      — no Evidence E block at all; one note telling the
                        model no additional evidence is available (does an
                        explicit prior-only instruction itself contract the
                        score?);
* ``withheld_only``   — an Evidence E block whose CONTENT is unavailable and
                        NO ruling (does the "an evidence exists but you
                        cannot see it" frame itself induce uncertainty?);
* ``withheld_strong`` — the same unavailable block + the P1/P2
                        StrongExcludePost ruling, character-identical;
* ``withheld_cf``     — the same unavailable block + the P1/P2
                        CounterfactualDeletePost ruling, character-identical.

The withheld content and the prior-only note are module constants: the blocks
NEVER read ``item.critical_evidence``, so real evidence text cannot leak into
a P3 prompt even if an item file carried it (belt and braces with the build
script, which stores the placeholder in that field anyway).

Dispatch happens on the condition name BEFORE the g24a branch inside
``schema._blocks`` — the same pattern proven for g25 / g26 / g24p1.  No
existing condition name collides, so every other item file keeps its prompts
bit-for-bit.

Wordings are frozen in registration §11 (2026-09-26, pre-run).
Usage: python scripts/verify_g24a_p3_prompts.py checks these invariants.
"""

import conditions_g24a as g24a
import conditions_g24p1 as g24p1

# The EVIDENCE E block for all three withheld cells — content unavailable.
WITHHELD_CONTENT = "[Content unavailable.]"

# The prior_only note (no header, no Evidence E block, no ruling) — verbatim
# user wording, registration §11.
PRIOR_ONLY_NOTE = ("No additional evidence is available. Judge the claim "
                   "using only your existing/background knowledge.")

G24P3_CONDITIONS = ["prior_only", "withheld_only", "withheld_strong",
                    "withheld_cf"]


def is_g24p3(cond: str) -> bool:
    return cond in G24P3_CONDITIONS


def blocks(item, cond: str) -> list[str]:
    """Ordered context blocks for one Pilot P3 operator-only cell."""
    B = g24a.CLAIM_HEADER + "\n" + item.base_context
    Ew = g24a.EVIDENCE_HEADER + "\n" + WITHHELD_CONTENT
    if cond == "prior_only":
        return [B, PRIOR_ONLY_NOTE]
    if cond == "withheld_only":
        return [B, Ew]
    if cond == "withheld_strong":
        return [B, Ew, "RULING\n" + g24p1.STRONG_EXCLUDE_RULE]
    if cond == "withheld_cf":
        return [B, Ew, "RULING\n" + g24p1.CF_DELETE_RULE]
    raise ValueError(f"unknown G24P3 condition {cond!r}")
