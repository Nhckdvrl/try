"""Pilot P1 retraction-operator conditions (Layer 2, user ruling 2026-09-25).

Two new POST-admit operators over the G24A natural-evidence materials:

* ``strong_exclude_post`` — a *strong wording control*: exclusion stated as
  forcefully as possible while still being a pure "do not use" instruction,
  so an advantage of the counterfactual operator over the ordinary one
  cannot be dismissed as "you just wrote a stronger instruction";
* ``counterfactual_delete_post`` — explicit counterfactual deletion
  ("judge as if Evidence E had never been shown").  It is informationally
  identical to the two exclusion wordings.

Block layout is the G24A POST arm exactly (CLAIM, EVIDENCE E, RULING).
``base`` / ``admit_post`` / ``exclude_post`` are NOT re-implemented here:
P1 items keep the g24a_* task_family, so those three conditions fall
through to the *unmodified* ``conditions_g24a.blocks`` in
``schema._blocks`` and stay character-identical to G24A by construction.
The two new names dispatch on the condition name BEFORE the g24a
task_family branch — the same pattern already proven for g25/g26 (no
existing condition name collides, so every other item file keeps its
prompts bit-for-bit).

Rulings are module constants (identical across all items by construction,
testable against this file).  No token-length matching filler: per the
user's ruling this is an exploratory discriminator, so the two new
wordings only need to be roughly comparable in length to each other.

Usage: python scripts/verify_g24a_p1_prompts.py checks these invariants.
"""

import conditions_g24a as g24a

STRONG_EXCLUDE_RULE = (
    "Evidence E is inadmissible. Completely disregard it when judging the "
    "claim. It must have no influence on your judgment in either direction, "
    "directly or indirectly. Judge the claim using only information "
    "available without relying on Evidence E.")

CF_DELETE_RULE = (
    "Evaluate the claim exactly as you would have if Evidence E had never "
    "been shown. Reconstruct the judgment you would have made before "
    "encountering Evidence E. Evidence E must have no influence on the "
    "answer in either direction, directly or indirectly.")

G24P1_CONDITIONS = ["strong_exclude_post", "counterfactual_delete_post"]


def is_g24p1(cond: str) -> bool:
    return cond in G24P1_CONDITIONS


def blocks(item, cond: str) -> list[str]:
    """Ordered context blocks for one Pilot P1 operator (G24A POST layout)."""
    B = g24a.CLAIM_HEADER + "\n" + item.base_context
    E = g24a.EVIDENCE_HEADER + "\n" + item.critical_evidence
    if cond == "strong_exclude_post":
        return [B, E, "RULING\n" + STRONG_EXCLUDE_RULE]
    if cond == "counterfactual_delete_post":
        return [B, E, "RULING\n" + CF_DELETE_RULE]
    raise ValueError(f"unknown G24P1 condition {cond!r}")
