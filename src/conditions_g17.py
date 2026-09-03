"""G17: binding x requested weight, fully crossed.

Frozen design: preregistrations/PREREGISTRATION_G17_BINDING_BY_WEIGHT.md.

The paper's two regularities have never been crossed. Every weight-sweep condition
addresses a named referent, and every binding manipulation runs at w = 0. This module
crosses them:

    preview in {none, para}  x  requested weight in {0.00, 0.25, 0.50}

with the rule always stated before the evidence, plus a no-rule base and a w = 1.00
admit anchor. The rule string comes from `uniform_weight_rule` at every level, so
prohibition and attenuation are worded identically; the preview comes from
`preview_text`, unchanged from Stage 3D.
"""
from __future__ import annotations

try:
    from .conditions_v3 import uniform_weight_rule
    from .conditions_v6 import preview_text
except ImportError:  # direct use with PYTHONPATH=src
    from conditions_v3 import uniform_weight_rule
    from conditions_v6 import preview_text

WEIGHTS = {"w000": 0.0, "w025": 0.25, "w050": 0.50}
PREVIEWS = ("none", "para")

G17_CONDITIONS = [f"g17_{w}_{p}" for w in WEIGHTS for p in PREVIEWS] + [
    "g17_base",
    "g17_admit",
]
G17_FAMILIES = ("legal_judgment", "evidence_inference")


def blocks(item, cond: str, B: str, E: str) -> list[str]:
    """Ordered content blocks for a G17 condition.

    `B` is the standard BACKGROUND block and `E` the standard evidence block, both
    supplied by schema._blocks so nothing about them is G17-specific.
    """
    if cond == "g17_base":
        return [B]
    if cond == "g17_admit":
        return [B, uniform_weight_rule(item, 1.0), E]

    _, wkey, rung = cond.split("_")
    rule = uniform_weight_rule(item, WEIGHTS[wkey])
    preview = preview_text(item, rung)
    out = [B]
    if preview:
        out.append("PRELIMINARY NOTE\n" + preview)
    out += [rule, E]
    return out
