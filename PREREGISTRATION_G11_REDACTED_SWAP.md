# G11 preregistration — Does irrelevant outcome evidence survive verdict redaction?

**Created:** 2026-09-01. The design, builder, runner, analyzer, and tests are
frozen before any target-model generation in this condition.

## 1. Scientific sub-question

G8 replaced each question's future packet with the packet from a different
question. The foreign packet caused 50.7–100.1% as much undirected movement as
the real packet, and its donor-outcome pull was positive in every model. That
rules out a purely own-question diagnostic account, but it leaves two
explanations confounded:

- **H-explicit-label:** the model copies an explicit YES/NO resolution verdict
  from the foreign packet;
- **H-outcome-evidence:** outcome-shaped evidence from an irrelevant question
  influences the judgment even without an explicit verdict sentence.

This experiment further answers how a model reconstructs a past epistemic
state contaminated by later knowledge by separating explicit answer copying
from integration of irrelevant outcome evidence.

## 2. Manipulation

Use the exact frozen G8 derangement (`seed=20260901`). Before inserting donor
packet `pi(i)` into recipient question `i`, apply the exact frozen G2
mechanical verdict-redaction function. Everything outside the donor packet is
byte-identical to G8. No item, pairing, or redaction rule is selected using
target-model output.

Only `redacted_swap_with` and its unchanged out-of-set boundary probe are new.
The reference `oob_without` cell is the frozen 256-item replication; the full
foreign-packet condition is frozen G8 output.

Volume: 3 models x 2 records x 256 units = **1,536 generations**.

## 3. Estimands

For recipient baseline `b_i`, redacted-swap answer `p_i`, donor sign `t_i`, and
full-swap answer `q_i`:

```text
I_donor_red  = mean_i t_i (p_i - b_i)
I_donor_full = mean_i t_i (q_i - b_i)       # frozen G8
Delta_label  = mean_i t_i (q_i - p_i)
S_red        = mean_i |p_i - b_i|
Retention    = I_donor_red / I_donor_full
```

The own-outcome pull is checked first and must have its 95% CI within
`[-5,+5]`, as in G8. Inference uses the unchanged 10,000-draw paired cluster
bootstrap over question ID, seed `20260829`. Qualification is unchanged:
decision parse rate at least `248/256`, boundary accuracy at least `224/256`.

## 4. Frozen decision rules

Per qualified model:

- **survives:** `I_donor_red` has a 95% CI lower bound above 0 and retention is
  at least 0.5;
- **verdict-dependent:** `Delta_label` has a 95% CI lower bound above 0 and
  retention is below 0.5;
- otherwise **indeterminate**.

Panel conclusion requires at least 2 of 3 qualified models in the same row.

Permitted conclusions:

- survives: explicit answer copying is insufficient; an irrelevant question's
  outcome evidence still pulls the judgment toward that question's outcome;
- verdict-dependent: G8's directional import mainly depends on the explicit
  verdict sentence;
- indeterminate: redaction does not adjudicate the pair.

The experiment does **not** claim that redacted packets conceal their outcomes:
the remaining evidence can still entail them. That is the manipulation's point:
explicit label versus evidential outcome content, not outcome-known versus
outcome-unknown.

## 5. Freeze checklist

- [x] preregistration written
- [x] builder and runner written
- [x] analyzer written
- [x] tests written
- [x] tests and dry-run pass (31 focused tests; 256 units, 512 prompts; longest
  prompt 4,223 tokens; 368 verdict sentences removed; 19 packets unchanged)
- [x] design commit `1ef0746` and tag `g11-redacted-swap-design-v1` precede
  first generation
