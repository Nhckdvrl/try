# G15 preregistration — Fresh-assignment confirmation of a causal decision state

**Created:** 2026-09-01. This confirmatory design is written after G14 and before
any output or activation under the fresh donor assignment.

## 1. Confirmatory question

G14 found a late, bidirectional, orthogonal-specific causal window at the answer
position, but its composite gate inherited an absolute cross-recipient classifier
from the packet-local hypothesis. That classifier peaked at 0.742 (<0.75), while
the post-result paired diagnostic matched the stated recipient-conditioned
hypothesis. G15 therefore asks, on unseen packet pairings:

> Does a recipient-conditioned outcome decision coordinate reappear and
> causally transfer the influence of future evidence on the reconstructed past?

## 2. Fresh construction and fixed analysis

Rebuild G12's balanced verdict-redacted YES/NO donor pairs with the new seed
`20260902`. Assignment SHA-256 is
`3040ff14a931a7a1020e24b6d96b666c2e531e1a4a1c3d5a3ecc8d3c850e498f`.
No G12/G14 output determines a donor. The deterministic connected split again
contains 190 train, 64 test, and 2 buffer recipients, with 65 unique held-out
donors; test digest is
`36e52bf1f65f20b1751d3f59addbc6a74597be899d23c2a84447487d18632309`.

Gemma revision, explicit-verdict redaction, answer-position site, candidate
layers `[5,11,17,23,29,35,41,47]`, mean-difference axis learned only on train,
one-dimensional paired interchange, deterministic orthogonal control, two
directions, greedy numeric readout, and bootstrap are identical to G14. All 128
baselines and 2,048 patched generations are newly generated.

## 3. Representation estimand corrected before confirmation

For held-out recipient `i` at layer `l`:

```text
D_il = <h_i,YES - h_i,NO, v_l>.
```

The recipient-conditioned representation gate passes at a layer only if:

- `mean(D_il)` has bootstrap CI lower > 0; and
- at least 75% of held-out pairs have `D_il > 0`.

This is not a lowered G14 threshold: 0.75 is retained. The estimand changes from
an absolute midpoint across different questions to the paired ordering implied
by the hypothesis and by the causal interchange itself.

## 4. Confirmatory causal gates

- fresh baseline bridge: >=62/64 parses per condition, YES-minus-NO >=10pp and
  CI lower >0;
- paired representation gate above;
- meaningful transfer: bidirectional mean >=3pp and CI lower >0;
- at least two adjacent candidate layers meaningful, with at least one in
  G14's late window `{29,35,41,47}`;
- at the strongest qualifying layer, outcome-axis minus orthogonal-axis transfer
  has CI lower >0.

All gates must pass for the permitted claim:

> Across a fresh assignment of unrelated future evidence, outcome information
> is converted into a recipient-conditioned late decision coordinate whose
> causal interchange bidirectionally transfers its influence on reconstructed
> past judgments.

## 5. Freeze checklist

- [x] fresh assignment, split, paired estimand, and causal gates fixed
- [x] implementation tests and dry audit pass (5 focused tests; 256 units,
  512 fresh prompts; 190/64/2 donor-disjoint split; longest 4,823 tokens)
- [x] design commit `1ba3662` and tag `g15-decision-confirm-design-v1`
  precede all fresh-assignment activation/output
