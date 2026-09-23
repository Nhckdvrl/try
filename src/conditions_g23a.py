"""G23A: is the prospective timing gap specific to complete gating (`w = 0`)?

Frozen design: preregistrations/PREREGISTRATION_G23A_ZERO_GATING.md.

One rule sentence, one number varying. For each requested weight
`w in {0, 1, 25, 50, 100}`:

    g23a_pre_<w>    BACKGROUND -> weight rule(w) -> EVIDENCE -> judgment
    g23a_post_<w>   BACKGROUND -> EVIDENCE -> weight rule(w) -> judgment

plus the two anchors every item needs to be scoreable at all:

    g23a_base       BACKGROUND -> judgment
    g23a_norule     BACKGROUND -> EVIDENCE -> judgment      (full influence, no rule)

The rule string is `conditions_v3.uniform_weight_rule` at every level, so the
prohibition (`0%`) and every attenuation are worded identically and differ only
in the percentage — the historical near-zero sweep's construction, kept byte for
byte so the fresh round stays comparable to the old one.

No preview, no second factor, no ratio: G23A's whole question is the shape of the
timing gap as a function of `w`.
"""
from __future__ import annotations

try:
    from .conditions_v3 import uniform_weight_rule
except ImportError:  # direct use with PYTHONPATH=src
    from conditions_v3 import uniform_weight_rule

# key -> fraction handed to `uniform_weight_rule`
WEIGHTS = {"w000": 0.0, "w001": 0.01, "w025": 0.25, "w050": 0.50, "w100": 1.00}
# order is the preregistered contrast order: 0 first, then the non-zero levels
WKEYS = ("w000", "w001", "w025", "w050", "w100")
NONZERO_WKEYS = ("w001", "w025", "w050", "w100")
ARMS = ("pre", "post")

G23A_CONDITIONS = ["g23a_base", "g23a_norule"] + [
    f"g23a_{arm}_{w}" for w in WKEYS for arm in ARMS
]
G23A_FAMILIES = ("legal_judgment", "evidence_inference", "ranking_selection")

# Policy access, asked as separate calls so a probe can never act as a reminder
# inside a decision run (README section 3.1). The numeric probes read the model's
# stated weight for each requested `w` in both block orders; the yes/no probes ask
# whether the evidence may influence the judgment at all.
G23A_NUMERIC_PROBES = [f"wprobe_g23a_{arm}_{w}" for w in WKEYS for arm in ARMS]
G23A_RULE_PROBES = [
    "rule_probe_g23a_w000_pre",
    "rule_probe_g23a_w000_post",
    "rule_probe_g23a_w100_pre",
]
G23A_PROBES = G23A_NUMERIC_PROBES + G23A_RULE_PROBES


def blocks(item, cond: str, B: str, E: str) -> list[str]:
    """Ordered content blocks for one G23A condition.

    `B` and `E` come from `schema._blocks`, so the background and evidence text
    are byte-identical to every other round's; only block order and the one
    number in the rule ever change.
    """
    if cond == "g23a_base":
        return [B]
    if cond == "g23a_norule":
        return [B, E]

    _, arm, wkey = cond.split("_")
    rule = uniform_weight_rule(item, WEIGHTS[wkey])
    return [B, rule, E] if arm == "pre" else [B, E, rule]
