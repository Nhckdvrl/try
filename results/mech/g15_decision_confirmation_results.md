# G15 — fresh-assignment confirmation of the late decision state

G15 rebuilt every verdict-redacted YES/NO donor pair with seed `20260902`, then
froze a new 190/64/2 donor-disjoint split before any target activation or output.
No G12/G14 generation was reused.

The fresh behavioral bridge passed: YES donor − NO donor = **+18.84pp [12.94,
24.97]**, with 64/64 parses per condition.

The recipient-conditioned representation prediction also passed. On held-out
donor identities, the learned outcome coordinate ordered paired YES above NO in
98.4% at layer 23, 90.6% at layer 29, 84.4% at layers 35 and 41, and 79.7% at
layer 47; every paired projection-gap interval at these layers was above zero.

| layer | outcome-axis transfer | 95% CI | orthogonal axis | recovery |
|---:|---:|---:|---:|---:|
| 5 | +0.08 | [-0.39, 0.55] | +0.16 | 0% |
| 11 | +0.16 | [-0.16, 0.51] | -0.04 | 1% |
| 17 | -0.19 | [-0.88, 0.41] | +0.31 | -1% |
| 23 | +1.28 | [0.59, 2.13] | +0.12 | 7% |
| 29 | **+6.52** | **[4.53, 8.59]** | +0.31 | 35% |
| 35 | **+9.04** | **[5.59, 12.95]** | +0.16 | 48% |
| 41 | **+7.73** | **[4.89, 10.72]** | +0.35 | 41% |
| 47 | **+8.34** | **[5.23, 11.66]** | +0.04 | 44% |

At peak layer 35, NO -> YES transfer is +10.03pp [5.45, 15.41] and YES -> NO
is +8.05pp [4.61, 11.72]. Outcome-axis minus orthogonal-axis transfer is
**+8.88pp [5.39, 12.81]**. Meaningful adjacent windows are 29–35, 35–41, and
41–47. Every frozen bridge, paired-representation, late-window,
bidirectionality, and specificity gate passes.

Frozen verdict: **`confirmed-recipient-conditioned-decision-state`**.

Permitted paper claim:

> Across a fresh assignment of unrelated future evidence, outcome information
> is converted into a recipient-conditioned late decision coordinate whose
> causal interchange bidirectionally transfers its influence on reconstructed
> past judgments.

Frozen design: `g15-decision-confirm-design-v1`. Sources:
`g15_decision_confirmation.json` and
`g15_decision_confirmation_analysis.json`.
