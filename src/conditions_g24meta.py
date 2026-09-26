"""§14 RQ3 explanation experiment: second-order retraction operators
(meta-evidence hypothesis; user ruling 2026-09-26, post-ConfA+ConfB).

Two new POST-admit operators over the G24A natural-evidence materials:

* ``meta_neutral_post`` — **Meta-Neutral Retraction (MNR)**: the first-order
  suppression instruction plus the second-order neutralizer — the retraction
  *event* itself is declared purely procedural, carrying no information about
  the claim or about the truth/reliability of Evidence E.  Hypothesis under
  test: the model conditions on R ("an evidence was shown and retracted") as
  meta-evidence; removing R's informational content improves counterfactual
  restoration without reopening the first-order direction.
* ``random_reason_post`` — P1's ``CF_DELETE_RULE`` **byte-identical** (the
  first-order suppression core is held fixed against the CF baseline) + the
  random-procedural reason sentence: the exclusion happened for reasons
  independent of content, truth, reliability, and the claim.  The only
  difference from ``counterfactual_delete_post`` is the second-order reason.

Both rulings are module constants (identical across all items by
construction, testable against this file).  Wording frozen verbatim in
registration §14 (2026-09-26, pre-run).

Block layout is the G24A POST arm exactly (CLAIM, EVIDENCE E, RULING).
``base`` / ``admit_post`` / ``exclude_post`` fall through to the unmodified
``conditions_g24a.blocks``; ``strong_exclude_post`` /
``counterfactual_delete_post`` fall through to the unmodified
``conditions_g24p1.blocks`` — all four legacy operators therefore render
character-identical to P1/P2 by construction (verified pre-run by
``scripts/verify_g24a_meta_prompts.py``).  The two new names dispatch on the
condition name BEFORE the g24a task_family branch — the same pattern proven
for g24p1/g24p3/g24p4; no existing condition name collides, so every other
item file keeps its prompts bit-for-bit.

Usage: python scripts/verify_g24a_meta_prompts.py checks these invariants.
"""

import conditions_g24a as g24a
import conditions_g24p1 as g24p1

# Registration §14.2 — verbatim.
META_NEUTRAL_RULE = (
    "Evidence E must have no influence on your judgment. Importantly, the "
    "fact that Evidence E was shown, withheld, or retracted is itself purely "
    "procedural and provides no information about the claim or about the "
    "truth or reliability of Evidence E. Judge exactly as if neither "
    "Evidence E nor any retraction event had occurred.")

RANDOM_PROCEDURAL_REASON = (
    "Evidence E was excluded by a random administrative procedure that is "
    "independent of its content, truth, reliability, and the claim.")

G24META_CONDITIONS = ["meta_neutral_post", "random_reason_post"]


def is_g24meta(cond: str) -> bool:
    return cond in G24META_CONDITIONS


def random_reason_rule() -> str:
    """CF core byte-identical to P1, then the second-order reason sentence."""
    return g24p1.CF_DELETE_RULE + " " + RANDOM_PROCEDURAL_REASON


def blocks(item, cond: str) -> list[str]:
    """Ordered context blocks for one §14 operator (G24A POST layout)."""
    B = g24a.CLAIM_HEADER + "\n" + item.base_context
    E = g24a.EVIDENCE_HEADER + "\n" + item.critical_evidence
    if cond == "meta_neutral_post":
        return [B, E, "RULING\n" + META_NEUTRAL_RULE]
    if cond == "random_reason_post":
        return [B, E, "RULING\n" + random_reason_rule()]
    raise ValueError(f"unknown G24META condition {cond!r}")
