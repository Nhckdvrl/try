"""Stage-3A: giving the phenomenon its correct name.

Stage 2 showed the failure is not distance (H-A) and not mainly directional
anaphora (H-C), and that it appears only when the requested weight is zero.
But the w=0 rule in Stage 2 was also the only *prohibition* in the family, so
"exact zero is special" and "suppressive semantics are special" are still
confounded, and generic prospective binding is too broad an account: a model
that can prospectively apply w=0.25 to future evidence clearly can bind a rule
to an object that does not exist yet.

These experiments separate those:

  A  near-zero sweep, one identical sentence, only the number changes
  B  rule->evidence delay (Stage 2 only varied rule->answer distance)
  C  object-existence ladder: how much of E7 exists when the rule is stated
  D  non-multiplicative transforms (sign flip, cap) at the same positions
  F  item-specific rule vs class-wide policy
  G  task preview: is the missing binding target the evidence or the objective
  (E is a probe, see schema.compile_probe: wprobe_*)
"""
from conditions_v2 import filler_block, stable_seed

# --------------------------------------------------------------------------
# A. near-zero sweep.  ONE sentence template; only the percentage changes, so
#    prohibition and attenuation are worded identically.
# --------------------------------------------------------------------------
NZ_LEVELS = {"nz0000": 0.0, "nz0010": 0.01, "nz0025": 0.025, "nz0050": 0.05,
             "nz0100": 0.10, "nz0250": 0.25, "nz0500": 0.50, "nz0750": 0.75,
             "nz1000": 1.00}


def _pct(w):
    return f"{w * 100:g}"


def uniform_weight_rule(item, w):
    return ("RULING\nThe causal weight assigned to " + item.critical_label +
            f" is exactly {_pct(w)}% of its normal evidential weight.")


NZ_CONDITIONS = [f"{k}_{a}" for k in NZ_LEVELS for a in ("pre", "post")]

# --------------------------------------------------------------------------
# B. rule -> evidence delay.  Stage 2 moved the rule away from the ANSWER;
#    this moves it away from the EVIDENCE it governs.
# --------------------------------------------------------------------------
RD_LEVELS = {"k0": 0, "k4": 4, "k12": 12, "k40": 40}   # filler units, ~25 tokens each
RD_CONDITIONS = [f"rd_{a}_{k}" for a in ("pre", "post") for k in RD_LEVELS]

# --------------------------------------------------------------------------
# C. object-existence ladder.  Same rule sentence at every level; what changes
#    is how much of E7 exists at the moment the rule is stated.
# --------------------------------------------------------------------------
OE_RULE = "RULING\nEvidence E7 has decision weight 0."
OE_LEVELS = ["oe_L0", "oe_L1", "oe_L2", "oe_L3", "oe_L4", "oe_L5"]


def oe_stub(item, level):
    lab = item.critical_label
    dirn = "raise" if item.critical_direction == "increase" else "lower"
    if level == "oe_L0":
        return None
    if level == "oe_L1":
        return "NOTICE\nYou will later receive Evidence E7."
    if level == "oe_L2":
        return "EVIDENCE E7\n[content pending]"
    if level == "oe_L3":
        return f"EVIDENCE E7\n[{lab}; content pending]"
    if level == "oe_L4":
        return (f"EVIDENCE E7\n[{lab}. If used, this item would {dirn} your rating. "
                "Content pending]")
    return None   # L5 places the full content before the rule


# --------------------------------------------------------------------------
# D. non-multiplicative transforms at both positions
# --------------------------------------------------------------------------
TRANSFORMS = {
    "trflip": ("RULING\nThe contribution of {lab} must be reversed in sign: count it "
               "with the same magnitude but in the opposite direction to its face value."),
    "trcap": ("RULING\nThe contribution of {lab} must be capped: let it move your rating "
              "by no more than one point on the answer scale, in the direction it "
              "supports."),
}
TR_CONDITIONS = [f"{k}_{a}" for k in TRANSFORMS for a in ("pre", "post")]

# --------------------------------------------------------------------------
# F. item-specific rule vs class-wide policy
# --------------------------------------------------------------------------
CLS_SOURCE_TAG = "[source: unauthorised]"
CLS_RULE = ("RULING\nAny item in this file marked as coming from an unauthorised source "
            "has decision weight 0.")
CLS_CONDITIONS = ["cls_pre", "cls_post"]

# --------------------------------------------------------------------------
# G. task preview
# --------------------------------------------------------------------------
TP_CONDITIONS = ["tp_pre", "tp_post"]

ALL_V3 = NZ_CONDITIONS + RD_CONDITIONS + OE_LEVELS + TR_CONDITIONS + CLS_CONDITIONS + TP_CONDITIONS
# anchors that must be run alongside so every family has its own base/full-weight pair
V3_ANCHORS = ["base", "id_base", "id_admit_pre", "id_admit_post"]


def blocks(item, cond, B, E, ID_B, ID_E, ID_ADMIT):
    """Return the ordered content blocks for a stage-3 condition."""
    seed = stable_seed(item.item_id)

    # ---- A ----
    if cond in NZ_CONDITIONS:
        key, arm = cond.rsplit("_", 1)
        R = uniform_weight_rule(item, NZ_LEVELS[key])
        return [B, R, E] if arm == "pre" else [B, E, R]

    # ---- B ----
    if cond in RD_CONDITIONS:
        _, arm, k = cond.split("_")
        R = uniform_weight_rule(item, 0.0)
        f = filler_block(RD_LEVELS[k], seed)
        mid = [f] if f else []
        return [B, R] + mid + [E] if arm == "pre" else [B, E] + mid + [R]

    # ---- C ----
    if cond in OE_LEVELS:
        if cond == "oe_L5":
            return [ID_B, ID_E, OE_RULE]          # full content already present
        stub = oe_stub(item, cond)
        pre = [ID_B] + ([stub] if stub else []) + [OE_RULE, ID_E]
        return pre

    # ---- D ----
    if cond in TR_CONDITIONS:
        key, arm = cond.rsplit("_", 1)
        R = "\n".join(TRANSFORMS[key].format(lab=item.critical_label).split("\n"))
        return [B, R, E] if arm == "pre" else [B, E, R]

    # ---- F ----
    if cond in CLS_CONDITIONS:
        Etag = ID_E.split("\n")[0] + " " + CLS_SOURCE_TAG + "\n" + "\n".join(ID_E.split("\n")[1:])
        return [ID_B, CLS_RULE, Etag] if cond == "cls_pre" else [ID_B, Etag, CLS_RULE]

    # ---- G ----
    if cond in TP_CONDITIONS:
        prev = ("TASK PREVIEW\nAt the end of this file you will be asked: "
                + item.question + " " + item.output_spec)
        R = uniform_weight_rule(item, 0.0)
        return [prev, B, R, E] if cond == "tp_pre" else [prev, B, E, R]

    raise ValueError(cond)


# probe used by experiment E: declarative policy state, asked in a separate call
WEIGHT_PROBE_Q = ("According to the instructions above, what decision weight should "
                  "{lab} receive? Answer with a single number from 0 to 100, as a "
                  "percentage of its normal evidential weight.")
WEIGHT_PROBES = ["wprobe_pre", "wprobe_post"]
