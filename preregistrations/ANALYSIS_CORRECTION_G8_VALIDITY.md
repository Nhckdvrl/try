# Analysis correction — G8 validity and explanatory role

**Created:** 2026-09-03, after observing the original G8 and Llama extension
outputs. This is an explicitly post-result correction, not a preregistration.
The frozen G8 verdict and the frozen Llama-extension verdict remain preserved.

## The error

G8 defined

```text
I_own = mean_i s_i (p_i[foreign packet] - p_i[no packet])
```

and treated an interval outside `[-5, 5]` as proof that the donor assignment
leaked recipient outcomes. That interpretation is incorrect. `I_own` is a
model-output quantity: it combines the assignment with any genuine difference
in how strongly the model reacts to foreign packets on realized-YES versus
realized-NO recipient questions. It can therefore be nonzero even when the
assignment was fixed before generation, is a bijection, and never gives a unit
its own packet. It is not an assignment-only leakage test.

This mattered for Llama: its foreign-packet donor pull was positive, but the
`I_own` interval crossed the frozen equivalence bound. Calling the entire G8
cross-event result invalid confuses response heterogeneity with assignment
leakage. G11 inherited the same invalidity interpretation for
`own_pull_redacted`; the same correction therefore applies there.

## Correct separation of scientific roles

The paper's experiments already identify three different claims:

1. **G8 — cross-event presence:** does a packet about another event still move
   the judgment substantially? Use qualification plus
   `S_swap >= 0.5 * S_real`. This is an undirected estimand and does not require
   `I_own = 0`.
2. **G11 — verdict-independent direction:** after removing explicit verdicts,
   does outcome-shaped evidence pull toward the donor outcome, and how much of
   the full-packet donor pull is retained? Qualification, positive redacted
   donor pull, and retention answer this question. The recipient-aligned
   quantity remains reported as heterogeneity, not assignment leakage.
3. **G12 — causal outcome direction:** within the same recipient, does replacing
   a NO-supporting packet with a YES-supporting packet change the judgment?
   This paired design is the valid causal test of donor outcome direction and
   includes its own recipient-aligned validity check.

No threshold is changed. No seed, unit, or output is selected. The original G8
and G11 fields and legacy verdicts remain reported. The corrected scientific-chain
verdict requires G8 cross-event presence, corrected G11 `survives`, and G12
`causal-outcome-entrainment`.

## Parser correction

The strict probability parser also rejected syntactically valid completions
such as `0.`. Analyses now reparse immutable raw text when a legacy stored
value is null. Explanatory prose remains unparsed. Raw generation files are not
rewritten.
