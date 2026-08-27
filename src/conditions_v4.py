"""Ruling paraphrases (publication hardening, run in parallel with Stage 3A).

Eight hand-written wordings covering distinct construction types, frozen before
running. A single wording was the largest surface-validity risk once the headline
became "rule position matters": the obvious attack is that the effect belongs to
one sentence. Each paraphrase gets a matched admit form so the leverage anchor is
worded in the same register as the exclusion it is paired with.
"""

PARAPHRASES = {
    "pp1": dict(kind="legal formal",
                exc="The court rules that {lab} is inadmissible. It must not be taken into "
                    "account in reaching your decision.",
                adm="The court rules that {lab} is admissible. It must be taken into account "
                    "in reaching your decision."),
    "pp2": dict(kind="plain",
                exc="Do not use {lab} when you decide.",
                adm="Do use {lab} when you decide."),
    "pp3": dict(kind="causal",
                exc="{lab} must have no influence on your decision.",
                adm="{lab} must have its full influence on your decision."),
    "pp4": dict(kind="counterfactual",
                exc="Decide exactly as you would if {lab} had never appeared in this file.",
                adm="Decide exactly as you would if {lab} were an ordinary verified part of "
                    "this file."),
    "pp5": dict(kind="weighting",
                exc="Assign {lab} a decision weight of 0.",
                adm="Assign {lab} a decision weight of 1."),
    "pp6": dict(kind="policy",
                exc="Policy requires that {lab} be excluded from the decision.",
                adm="Policy requires that {lab} be included in the decision."),
    "pp7": dict(kind="relevance",
                exc="Treat {lab} as a non-contributing item: it does not enter the decision.",
                adm="Treat {lab} as a contributing item: it enters the decision."),
    "pp8": dict(kind="procedural",
                exc="{lab} may be remembered, but it cannot enter the judgment.",
                adm="{lab} may be remembered, and it does enter the judgment."),
}

PP_CONDITIONS = [f"{k}{s}_{a}" for k in PARAPHRASES for s in ("x", "a") for a in ("pre", "post")]
PP_ANCHORS = ["base"]


def blocks(item, cond, B, E):
    key = cond[:3]
    sense = cond[3]                     # 'x' exclude, 'a' admit
    arm = cond.split("_")[1]
    tmpl = PARAPHRASES[key]["exc" if sense == "x" else "adm"]
    R = "RULING\n" + tmpl.format(lab=item.critical_label)
    return [B, R, E] if arm == "pre" else [B, E, R]
