# G14 — answer-position outcome decision state

G14 moved the same donor-general one-dimensional interchange from G13's packet
span to the final prompt token, where recipient question and context have been
integrated immediately before answering. Model, prompts, donor-disjoint split,
layers, axes, controls, bridge, and numeric gates were frozen unchanged.

The causal pattern is clear and localized:

| layer | outcome-axis transfer (pp) | 95% CI | orthogonal axis (pp) | recovery |
|---:|---:|---:|---:|---:|
| 5 | -0.27 | [-0.74, 0.12] | 0.00 | -2% |
| 11 | +0.08 | [-0.35, 0.55] | -0.43 | 0% |
| 17 | -0.08 | [-0.86, 0.66] | -0.31 | 0% |
| 23 | +1.48 | [0.62, 2.58] | -0.31 | 9% |
| 29 | **+3.83** | **[2.27, 5.47]** | -0.27 | 23% |
| 35 | **+5.39** | **[3.36, 7.50]** | -0.20 | 32% |
| 41 | **+4.93** | **[2.73, 7.39]** | -0.35 | 29% |
| 47 | **+3.73** | **[1.73, 5.91]** | +0.16 | 22% |

At the peak layer 35, NO -> YES transfer is +6.33pp and YES -> NO is +4.45pp.
Outcome-axis minus orthogonal-axis transfer is +5.59pp [3.44, 7.89]. Thus the
bridge, adjacent causal-window, bidirectionality, and specificity predictions
all pass.

The frozen composite verdict is nevertheless **not-established**. Its inherited
global-midpoint representation gate required held-out balanced accuracy >=0.75;
the answer-position peak was 0.742 at layer 23. No threshold is changed. A
post-result diagnostic, explicitly outside the frozen verdict, showed why the
measurement mismatched the hypothesis: the variable is recipient-conditioned.
Within the same held-out recipient, YES projection exceeded NO projection in
89.1% at layer 23 and 82.8--85.9% at layers 29--47, with positive paired-gap
intervals. A fresh-assignment confirmatory experiment must preregister that
paired representation estimand before it can support the mechanism claim.

Frozen design: `g14-decision-state-design-v1`. Sources:
`g14_decision_outcome.json` and `g14_decision_outcome_analysis.json`.
