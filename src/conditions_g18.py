"""G18 conditions — target representation × rule, with a per-preview baseline.

Six target representations by three rule states, eighteen cells per item:

                     preview only      preview + evidence     preview + rule + evidence
    none             g18_none_only     g18_none_norule        g18_none_excl
    ident            g18_ident_only    g18_ident_norule       g18_ident_excl
    empty            ...
    para             ...
    entail           ...
    unrel            ...

The `only` cells are the per-preview baselines Stage 3E showed are required: a
preview makes the later evidence partly redundant, so the evidence's marginal effect
must be measured against that preview's own baseline rather than a global one.

    marg(level, rule) = Y(level, rule, +evidence) − Y(level, only)
    ExclusionEffect(level) = marg(level, no rule) − marg(level, exclude)

Everything is in raw sign-aligned rating points. No REI ratio is computed anywhere
in this round.
"""
from __future__ import annotations

LEVELS = ("none", "ident", "empty", "para", "entail", "unrel")
RULE_STATES = ("only", "norule", "excl")

G18_CONDITIONS = [f"g18_{lv}_{rs}" for lv in LEVELS for rs in RULE_STATES]
G18_FAMILIES = ("legal_judgment", "evidence_inference", "ranking_selection")


def blocks(item, cond: str, B: str, E: str) -> list[str]:
    """Ordered content blocks. `B` is BACKGROUND, `E` the evidence block."""
    _, level, state = cond.split("_", 2)
    out = [B]
    if level != "none":
        out.append(item.meta["previews"][level])
    if state == "only":
        return out
    if state == "excl":
        out.append(item.exclude_rule)
    out.append(E)
    return out
