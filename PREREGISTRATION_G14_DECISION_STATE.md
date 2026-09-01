# G14 preregistration — Where does outcome become a causal decision variable?

**Created:** 2026-09-01. No G14 target activation/output may be generated before
the design, implementation, tests, and audit are committed and tagged.

## 1. Scientific question

G13 found a donor-general outcome direction in packet-span residuals (held-out
balanced accuracy 0.758) but exchanging it did not causally transfer behavior.
This rules out the simplest packet-scalar bottleneck and motivates a specific
transformation hypothesis:

> Is outcome evidence converted into a recipient-conditioned causal decision
> variable only after it is integrated at the answer position?

- **H-decision-state:** across unrelated donor packets, the answer-position
  residual contains a shared outcome direction whose exchange transfers the
  reconstructed judgment.
- **H-distributed:** the G12 effect remains distributed/content-specific; even
  at the answer position, no donor-general one-dimensional decision variable is
  causally sufficient.

## 2. Frozen design

Model, revision, G12 prompts, 190/64/2 donor-disjoint split, test digest, layers
`[5, 11, 17, 23, 29, 35, 41, 47]`, mean-difference axis, orthogonal-axis control,
greedy 0--100 readout, bootstrap, and all numeric gates are inherited unchanged
from `PREREGISTRATION_G13_SHARED_OUTCOME.md`.

The only manipulated scientific factor is site:

- G13 learned and exchanged the mean residual over packet tokens.
- G14 learns the outcome axis from the **final prompt token**, where the model
  must integrate the recipient question and context immediately before answering.
  On held-out recipients, it replaces only that token's one-dimensional
  projection with its paired opposite-donor value. YES -> NO and NO -> YES are
  both run; all orthogonal dimensions and all other token states remain fixed.

G13's already frozen 128 Transformers baseline generations are reused after
hash/unit/condition validation. Volume is 8 × 64 × 2 × 2 = **2,048 patched
generations**, plus 512 answer-position activation captures.

## 3. Frozen decision rule

G13's gates apply verbatim:

- baseline bridge: >=62/64 parses per condition, contrast >=10pp, CI lower >0;
- held-out representation balanced accuracy >=0.75 at one layer;
- meaningful transfer at a layer: bidirectional mean >=3pp and CI lower >0;
- causal window: at least two adjacent candidate layers meaningful;
- at the strongest qualifying layer, outcome-axis minus orthogonal-axis transfer
  has CI lower >0.

All gates must pass to claim a **recipient-conditioned causal outcome decision
state**. Decodability without transfer is reported only as representation.

## 4. Freeze checklist

- [x] question, competing explanations, site contrast, and inherited gates fixed
- [x] implementation tests and no-model dry audit pass (4 focused tests; 256
  units, 512 prompts, 190/64/2 split, exact 128-row G13 baseline reuse)
- [x] design commit `d2703bd` and tag `g14-decision-state-design-v1`
  precede all target activations/output
