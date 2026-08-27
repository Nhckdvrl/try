"""Stage-3C: adversarial tests of the narrow claim.

Stage 3A narrowed the failure to "a prospective rule that must hold a reference
to a specific future item and demands its causal weight be exactly zero". Four
attacks on that claim, plus two controls for results it rests on.

P0-1  INCLUSION IMPLICATURE (H-D).  A single alternative account explains A, C
      and F at once: presenting an item at all signals that it is relevant, and
      w=0 is the only condition where presentation and stated weight contradict
      each other. Neutralise the implicature with a presentation policy that
      never mentions the item, exclusion, or zero.
P0-3  STATE EXTERNALISATION.  Does the declarative policy control the decision
      once the model has written it into its own generation state?
P0-4  IDENTITY vs ARBITRARY-TAG PREDICATE.  The Stage-3A class rule changed three
      things at once. This is the clean 2x2: both conditional, both locally
      checkable at arrival, semantically empty tag.
P1-7  SALIENCE CONTROL for the object-existence ladder: does previewing an item
      raise its leverage even with no rule at all?
P1-8  OCCURRENCE vs CONTENT BINDING: E -> rule -> E again.
"""
from conditions_v3 import uniform_weight_rule, oe_stub

# --------------------------------------------------------------------------
# P0-1 inclusion implicature
# --------------------------------------------------------------------------
PRESENTATION = {
    "none": None,
    "auto": ("PRESENTATION POLICY\nThis system displays every record in the file "
             "automatically, regardless of the role that record plays in the judgment."),
    "audit": ("PRESENTATION POLICY\nFor audit purposes every record in the file is "
              "reproduced in full, regardless of the role it plays in the judgment. "
              "That a record is displayed does not indicate that it bears on the judgment."),
    # relevance-positive control: should make the implicature stronger, not weaker
    "relev": ("PRESENTATION POLICY\nThis system displays only records that bear on the "
              "final judgment."),
}
INC_CONDITIONS = [f"inc_{v}_{s}" for v in PRESENTATION for s in ("base", "full", "pre", "post")]

# --------------------------------------------------------------------------
# P0-3 state externalisation (handled with a two-line answer format)
# --------------------------------------------------------------------------
SC_CONDITIONS = ["sc_a_pre", "sc_a_post", "sc_b_pre", "sc_b_post", "sc_c_pre", "sc_c_post"]
# on-policy version: the model is sampled, and we condition on the trajectories in
# which it states the correct zero weight of its own accord. Teacher-forcing a
# reasoning step can push a model off-policy, so a forced-state result should not
# be read as a natural-runtime causal claim on its own.
OP_CONDITIONS = ["op_pre", "op_post"]
SC_TWOLINE = ("Reply with exactly two lines, in this order:\n"
              "ITEM DECISION WEIGHT: <percentage>\nFINAL DECISION: <your answer>")
SC_FORCED = "ITEM DECISION WEIGHT: 0%"

# --------------------------------------------------------------------------
# P0-4 identity predicate vs arbitrary tag predicate
# --------------------------------------------------------------------------
IDP_RULE_0 = "RULING\nIf an item's ID is E7, assign it decision weight 0."
IDP_RULE_1 = "RULING\nIf an item's ID is E7, assign it decision weight 1."
TAGP_RULE_0 = "RULING\nIf an item's tag is Z9, assign it decision weight 0."
TAGP_RULE_1 = "RULING\nIf an item's tag is Z9, assign it decision weight 1."
PRED_CONDITIONS = [f"{p}_{w}_{a}" for p in ("idp", "tagp")
                   for w in ("z", "f") for a in ("pre", "post")]

# --------------------------------------------------------------------------
# P1-7 salience control: preview stubs with NO rule at all
# --------------------------------------------------------------------------
SAL_CONDITIONS = ["sal_L0", "sal_L1", "sal_L2", "sal_L3", "sal_L4"]

# --------------------------------------------------------------------------
# P1-8 occurrence vs content binding
# --------------------------------------------------------------------------
OCC_CONDITIONS = ["occ_prevx"]

ALL_V5 = (INC_CONDITIONS + SC_CONDITIONS + OP_CONDITIONS + PRED_CONDITIONS
          + SAL_CONDITIONS + OCC_CONDITIONS)
V5_ANCHORS = ["base"]


def blocks(item, cond, B, E, ID_B):
    # ---- P0-1 ----
    if cond in INC_CONDITIONS:
        _, variant, slot = cond.split("_")
        head = PRESENTATION[variant]
        pre = [head] if head else []
        if slot == "base":
            return pre + [B]
        if slot == "full":
            return pre + [B, E, uniform_weight_rule(item, 1.0)]
        R = uniform_weight_rule(item, 0.0)
        return pre + ([B, R, E] if slot == "pre" else [B, E, R])

    # ---- P0-3 ----
    if cond in SC_CONDITIONS + OP_CONDITIONS:
        arm = cond.split("_")[-1]
        R = uniform_weight_rule(item, 0.0)
        return [B, R, E] if arm == "pre" else [B, E, R]

    # ---- P0-4 ----
    if cond in PRED_CONDITIONS:
        pred, w, arm = cond.split("_")
        if pred == "idp":
            R = IDP_RULE_0 if w == "z" else IDP_RULE_1
            Etag = "EVIDENCE [ID=E7]\n" + item.critical_evidence
            head = (ID_B + "\nItems in this file are shown with their ID.")
        else:
            R = TAGP_RULE_0 if w == "z" else TAGP_RULE_1
            Etag = "EVIDENCE [TAG=Z9]\n" + item.critical_evidence
            head = (B + "\nItems in this file are shown with their tag.")
        return [head, R, Etag] if arm == "pre" else [head, Etag, R]

    # ---- P1-7 ----
    if cond in SAL_CONDITIONS:
        stub = oe_stub(item, cond.replace("sal_", "oe_"))
        return [B] + ([stub] if stub else []) + [E]     # no rule at all

    # ---- P1-8 ----
    if cond == "occ_prevx":
        return [B, "PREVIEW\n" + item.critical_evidence,
                uniform_weight_rule(item, 0.0), E]

    raise ValueError(cond)
