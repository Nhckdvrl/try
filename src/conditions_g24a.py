"""G24A natural-evidence confirmation (FEVER + SciFact).

The five standard conditions re-rendered over natural materials:

* the background block is the bare **claim** (header ``CLAIM``);
* the critical evidence is the frozen annotated block (header ``EVIDENCE E``);
* the two rulings are the IDBIND-style admit / zero-use pair — one constant
  string each, character-identical between the PRE and the POST arm, so the
  only difference between arms is the position of the rule relative to the
  evidence (preregistration §3).

Dispatch happens on ``item.task_family`` (``g24a_fever`` / ``g24a_scifact``)
inside ``schema._blocks``; condition names are the G0 five, so the runner,
the rule probes and the G0 estimand plumbing are inherited unchanged.
"""

ADMIT_RULE = ("Evidence E is admitted. It must be given the full weight of a "
              "verified item in your final judgment.")
EXCLUDE_RULE = ("Evidence E is excluded. It must have zero influence on your "
                "final judgment.")

CLAIM_HEADER = "CLAIM"
EVIDENCE_HEADER = "EVIDENCE E"

# Documented metadata literals (prereg §3). Neither field is an analysis stratum.
EXCLUSION_REASON = "none_stated"
EVIDENCE_TRUTH = "true_but_forbidden"

QUESTION = "Considering everything above, rate the likelihood that the claim is true."
OUTPUT_SPEC = ("Use a scale from 0 to 9, where 0 means certainly false and "
               "9 means certainly true.")
RULE_PROBE_QUESTION = ("According to the ruling above, are you permitted to use "
                       "evidence E when you reach your rating? Answer with "
                       "exactly one word: YES or NO.")
# No memory probe in G24A (prereg §3): field kept for schema completeness only.
MEMORY_QUESTION = ""

G24A_TASK_FAMILIES = ("g24a_fever", "g24a_scifact")
G24A_CONDITIONS = ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"]


def is_g24a(item) -> bool:
    return getattr(item, "task_family", "") in G24A_TASK_FAMILIES


def blocks(item, cond: str) -> list[str]:
    """Ordered context blocks for one G24A condition.

    ``item.admit_rule`` / ``item.exclude_rule`` carry the constants (the
    builder fills them from this module), so the identical-text guarantee of
    prereg §9.1 holds per item and is testable per item.
    """
    B = CLAIM_HEADER + "\n" + item.base_context
    E = EVIDENCE_HEADER + "\n" + item.critical_evidence
    Radm = "RULING\n" + item.admit_rule
    Rexc = "RULING\n" + item.exclude_rule
    if cond == "base":
        return [B]
    if cond == "admit_pre":
        return [B, Radm, E]
    if cond == "admit_post":
        return [B, E, Radm]
    if cond == "exclude_pre":
        return [B, Rexc, E]
    if cond == "exclude_post":
        return [B, E, Rexc]
    raise ValueError(f"unknown G24A condition {cond!r}")
