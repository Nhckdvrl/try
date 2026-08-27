"""Condition blocks for the verifiable linear-weighting task (kept out of the
generator so `schema` can import it without a circular import)."""

LINEAR_WEIGHTS = {"lw0000": 0.0, "lw0010": 0.01, "lw0250": 0.25,
                  "lw0500": 0.50, "lw0750": 0.75, "lw1000": 1.00}
LINEAR_CONDITIONS = [f"{k}_{a}" for k in LINEAR_WEIGHTS for a in ("pre", "post")] + ["lin_base"]


def blocks(item, cond):
    B = "BACKGROUND\n" + item.base_context
    E = "ADDITIONAL INFORMATION\n" + item.critical_evidence
    if cond == "lin_base":
        return [B]
    key, arm = cond.split("_")
    w = LINEAR_WEIGHTS[key]
    R = ("RULING\nThe causal weight assigned to item E7 is exactly "
         f"{w * 100:g}% of its normal evidential weight.")
    return [B, R, E] if arm == "pre" else [B, E, R]


def target(item, w):
    return item.meta["base"] + w * item.meta["delta"]


