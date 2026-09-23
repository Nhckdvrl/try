# G23C-R preregistration draft — fresh-material replication of target-conditioned policy-state interchange

**Created:** 2026-09-23, after the frozen G23C v1 result.

**Status:** DESIGN / PREREGISTRATION DRAFT ONLY.  
**NO G23C-R MODEL FORWARD PASS OR PATCHING COMPUTE IS AUTHORIZED BY THIS FILE.**

G23C v1 passed its frozen verdict on the Stage-5 discovery materials:

- bridge `PolicyEffect_M = +34.08 [+32.16,+36.21]`;
- bridge `TargetPolicyInteraction = +11.31 [+8.26,+15.04]`;
- L14 `PolicyTransfer_M = +13.03 [+11.69,+14.31]`;
- L14 `PolicyTransfer_U = +4.89 [+3.73,+6.18]`;
- L14 `TargetConditioning = +8.15 [+6.91,+9.44]`;
- L4 `TargetConditioning = -0.03`;
- L24 `TargetConditioning = +0.07`;
- identity patch max absolute error = 0 over 1,800 checks;
- frozen verdict: `target-conditioned-policy-state`.

The design tag is
`g23c-target-conditioned-policy-state-design-v1` at commit `ddaf7ff`; no
runner/analyzer/prereg/test file changed between that tag and the result commit.

G23C-R is **not a new mechanistic story**. It asks whether the same frozen intervention
replicates on materials that were created and frozen independently of Stage 5.

---

## 1. Why one replication is still worth doing

G23C v1 is internally strong, but its primary layer (L14) was chosen from the earlier
Stage-5 localization and G23C reused the same 75 Stage-5 items.

That is acceptable for establishing a new causal property, because:
- the policy-value interchange was new and preregistered;
- the estimator and classifier were frozen;
- negative layers were frozen;
- no item was selected on the G23C effect.

However, a reviewer can still compress the mechanism evidence as:

> “the same materials that localized the layer were reused to confirm the new property.”

G23C-R removes that dependence.

---

## 2. Materials — existing, frozen, and disjoint

Use only the already-frozen G18 materials from
`data/items/g18_v1.jsonl`:

- `legal_judgment`: 40 items / 10 skeletons;
- `evidence_inference`: 30 items / 10 skeletons;
- total: **70 items / 20 independent skeletons**.

Do not use G18 `ranking_selection` in this mechanism replication because the Stage-5
direct-readout mechanism was validated only on legal judgment and evidence inference.

These materials were created before G23C and are explicitly disjoint from
`items_v1.jsonl`, the Stage-5 discovery set, by G18's frozen preregistration.

All 70 in-scope items are included. No selection by G18 effect size, G23C prediction,
behavioral gap, or model output.

---

## 3. Frozen target-availability construction

For every item:

```text
M preview = item.meta["previews"]["para"]
U preview = item.meta["previews"]["unrel"]
```

These semantic strings are reused byte-for-byte from the frozen G18 artifact.

No new paraphrase, no LLM-generated preview, no carrier rewrite.

Before any model forward pass, a tokenizer-only audit is required on both models:

1. all 70 items compile in all four cells;
2. `rule_end` exists in every cell;
3. `rule_end` precedes every later-evidence token;
4. inside each preview condition, 0% vs 100% cells differ only in the rule block;
5. at fixed policy value, M vs U cells differ only in the frozen preview block;
6. the absolute M-vs-U difference in `rule_end` token position is reported for every
   item/model.

Because G18's `unrel` previews were authored as length controls for `para`, this
round does **not** add new filler or edit either preview after the audit.

If more than 5% of item/model pairs differ by more than **4 tokens** at `rule_end`,
the design is considered position-mismatched and stops before compute. Do not repair
the previews inside this round.

---

## 4. Four cells

Use the exact Stage-5/G23C direct-readout construction, replacing only the preview
source with the frozen G18 preview strings:

```text
M0     G18 para preview  -> weight 0% rule   -> evidence -> answer
M100   G18 para preview  -> weight 100% rule -> evidence -> answer

U0     G18 unrel preview -> weight 0% rule   -> evidence -> answer
U100   G18 unrel preview -> weight 100% rule -> evidence -> answer
```

The rule is `uniform_weight_rule(item, 0.0 | 1.0)`.

The answer readout is the same fixed-position direct digit expectation used in Stage 5
and G23C.

---

## 5. Models and layers

Exactly the G23C v1 mechanism panel:

- Qwen3-8B;
- Mistral-Small-24B.

Exactly the G23C v1 layers:

- L4 — negative control;
- **L14 — primary**;
- L24 — negative control.

Patch site:

- **`rule_end` only**.

No model addition, model replacement, layer search, or site search after any output.

---

## 6. Bridge stop rule

Before any activation patching, run the four plain cells and compute exactly the G23C
bridge quantities:

```text
PolicyEffect_M = s · [Y(M100) - Y(M0)]
PolicyEffect_U = s · [Y(U100) - Y(U0)]

TargetPolicyInteraction =
    PolicyEffect_M - PolicyEffect_U
```

Bridge passes only if all three original G23C gates pass:

1. pooled `PolicyEffect_M >= 5.0` and CI lower > 0;
2. pooled `TargetPolicyInteraction >= 5.0` and CI lower > 0;
3. both quantities have positive means in 2/2 models.

If the bridge fails:

> **G23C-R stops before patching.**

Do not alter the fresh materials or direct readout to restore the bridge.

---

## 7. Policy-state interchange

If and only if the bridge passes, execute the same four G23C directions:

```text
M100 -> M0
M0   -> M100

U100 -> U0
U0   -> U100
```

At L4 / L14 / L24, `rule_end` only.

Use the same donor-direction-aligned switch definitions and per-item estimands as G23C:

```text
PolicyTransfer_M =
    mean(Switch_M_100to0, Switch_M_0to100)

PolicyTransfer_U =
    mean(Switch_U_100to0, Switch_U_0to100)

TargetConditioning =
    PolicyTransfer_M - PolicyTransfer_U
```

Raw sign-aligned rating points only.

No recovery-fraction inference.

---

## 8. Frozen replication verdict

### `replicated`

At L14:

1. `PolicyTransfer_M >= 3.0`, CI lower > 0, positive in 2/2 model means;
2. `TargetConditioning >= 3.0`, CI lower > 0, positive in 2/2 model means;
3. at both L4 and L24, the G23C control clause holds:
   - `PASS(TargetConditioning)` is false, **or**
   - L14 pooled TC exceeds that control layer by at least +3.0 points;
4. all identity patches stay within 0.5 rating points.

Licensed synthesis with G23C v1:

> **Across the Stage-5 discovery materials and a disjoint frozen material set, the
> causal efficacy of the rule-time policy state is stronger when the target proposition
> is available during policy processing.**

Note the wording: **causal efficacy is target-conditioned**.

Do not strengthen this to:
- the entire target×policy conjunction lives in one token state;
- the rule-end state is a reusable universal vector;
- downstream context plays no role.

### `bridge-failed`

Fresh materials do not reproduce the behavioral substrate under the direct mechanism
readout. Stop before patching.

### `not-replicated`

Bridge passes but the L14 replication gates fail.

Consequence:

> G23C v1 remains a valid frozen result on its original materials, but the paper must
> treat the target-conditioning mechanism as material-dependent and not use it as a
> general closing mechanism claim.

No rescue round.

---

## 9. Inference

Same as G23C v1:

- seed `20260923`;
- 10,000 percentile-bootstrap resamples;
- cluster by G18 frozen `meta["skeleton"]`;
- pooled bootstrap keeps both models' rows from one skeleton together;
- per-model results reported in full;
- no trimming, winsorisation, ratio normalization or behavioral-gap filtering.

The 70 items contain **20 independent skeletons**.

---

## 10. Known history and interpretation discipline

These G18 materials are not outcome-naive in the behavioral sense: their semantic
preview effects were already measured in G18.

That is acceptable because G23C-R does not re-test “semantic previews help.” The new
confirmatory object is the **policy-value activation interchange at a previously frozen
layer/site**, which has never been run on these items.

All 70 eligible items are included, regardless of their prior G18 effect.

Post-G23C diagnostics on the original materials found:
- legal `TargetConditioning ≈ +7.68`;
- evidence-inference `TargetConditioning ≈ +8.86`;
- leave-one-skeleton-out pooled TC ranged approximately `+7.79` to `+8.40`.

Those diagnostics motivate confidence but do not change any G23C-R gate.

---

## 11. Stop rule for the research programme

G23C-R is the **last planned mechanism experiment**.

After its frozen outcome:

- if `replicated`: close the experimental programme and write the paper;
- if `bridge-failed`: report G23C mechanism scope as limited to the original
  Stage-5 materials and write/reassess without another mechanism rescue;
- if `not-replicated`: downgrade the mechanism claim and write/reassess.

No G23D mechanism search follows automatically from any outcome.

---

## 12. Authorization boundary

Before any G23C-R forward pass:

1. implement G18 item loading and byte-for-byte preview reuse;
2. implement the tokenizer-only position audit and the >5% / >4-token stop rule;
3. implement the bridge / patch phases with the same constants as G23C;
4. implement frozen analyzer and tests;
5. commit and tag a dedicated design freeze;
6. explicitly update `STATUS.md`.

Until then:

> **NO G23C-R COMPUTE.**
