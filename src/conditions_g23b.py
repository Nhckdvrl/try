"""G23B: standing gate vs retrospective cancellation — U / K / I target states.

Frozen design: preregistrations/PREREGISTRATION_G23B_GATE_VS_CANCELLATION.md.

Phase A — carrier qualification, **no exclusion rule appears anywhere**:

    g23b_b   BACKGROUND -> judgment
    g23b_p   BACKGROUND -> PROFFER(E) -> judgment
    g23b_e   BACKGROUND -> EVIDENCE(E) -> judgment
    g23b_pe  BACKGROUND -> PROFFER(E) -> EVIDENCE(E) -> judgment

Phase B — branch test, only after the frozen Phase-A carrier gate passes:

    g23b_u   BACKGROUND -> RULE(exclude E) -> EVIDENCE(E) -> judgment
    g23b_k   BACKGROUND -> PROFFER(E) -> RULE(exclude E) -> EVIDENCE(E) -> judgment
    g23b_i   BACKGROUND -> EVIDENCE(E) -> RULE(exclude E) -> judgment

The rule block is `item.exclude_rule` — the reopened line's categorical
exclusion (G0 construction: reason clause + "must not play any role"). All
three rule cells read the same item field and add the same header, so the rule
is **byte-identical across U/K/I**; only block order (and the proffer in K)
differs, exactly as §5 freezes it.

The K carrier is the prereg §4 offer of proof. Its payload is literally
`item.critical_evidence`, i.e. the same proposition as E, so the proffer can
never disagree with the evidence about *what* is true — only its institutional
role differs. The wrapper never calls the payload uncertain, hypothetical, false
or unreliable, and never says "ignore this because it is inadmissible": §4
forbids both, because either would change the proposition's status inside the
carrier rather than only its evidential role.

Slot rendering (§4 freezes the semantics, this file freezes the bytes): the
draft's `the later [evidence label] is expected to report the following` cannot
be filled literally with a label like "the intercom recordings" (the later the
intercom recordings is expected ...). The rendering keeps every element —
purpose, label, later-presentation, expectation modality, indented payload,
closing status sentence — in an agreement-safe oblique construction; flagged for
review before the design tag.
"""
from __future__ import annotations

# prereg §4, rendered (see module docstring)
PROFFER_TMPL = (
    "OFFER OF PROOF — NOT EVIDENCE\n\n"
    "For the limited purpose of deciding admissibility, counsel states the content "
    "expected from {label} when that evidence is later presented:\n\n"
    "    {payload}\n\n"
    "This proffer is not admitted evidence and must not affect the merits judgment."
)

# phase -> cell letters, in the prereg's own notation
PHASE_A_CELLS = ("b", "p", "e", "pe")
PHASE_B_CELLS = ("u", "k", "i")
CELLS = PHASE_A_CELLS + PHASE_B_CELLS

PHASE_A = [f"g23b_{c}" for c in PHASE_A_CELLS]
PHASE_B = [f"g23b_{c}" for c in PHASE_B_CELLS]
G23B_CONDITIONS = PHASE_A + PHASE_B

# families this round runs: §3, one natural domain only
G23B_FAMILIES = ("legal_judgment",)


def proffer(item) -> str:
    """The K carrier: same payload as E, non-evidential role wrapper."""
    return PROFFER_TMPL.format(label=item.critical_label,
                               payload=item.critical_evidence)


def blocks(item, cond: str, B: str, E: str) -> list[str]:
    """Ordered content blocks for one G23B cell.

    `B` and `E` come from `schema._blocks`, so background and evidence are
    byte-identical to every other round's; only block order and the one rule
    block ever change.
    """
    if cond == "g23b_b":
        return [B]
    if cond == "g23b_p":
        return [B, proffer(item)]
    if cond == "g23b_e":
        return [B, E]
    if cond == "g23b_pe":
        return [B, proffer(item), E]

    rule = "RULING\n" + item.exclude_rule
    if cond == "g23b_u":
        return [B, rule, E]
    if cond == "g23b_k":
        return [B, proffer(item), rule, E]
    if cond == "g23b_i":
        return [B, E, rule]
    raise ValueError(cond)
