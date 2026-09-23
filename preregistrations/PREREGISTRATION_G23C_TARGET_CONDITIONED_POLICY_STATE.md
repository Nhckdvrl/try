# G23C preregistration draft — target-conditioned policy-state interchange

**Created:** 2026-09-23, after G23B v1 stopped as `carrier-invalid`.

**Status:** DESIGN / PREREGISTRATION DRAFT ONLY.  
**NO G23C TARGET-MODEL OR PATCHING COMPUTE IS AUTHORIZED BY THIS FILE.**

G23C does **not** attempt another exact-semantic-but-non-evidential K carrier. G23B v1
showed that this behavioral factorization is not identified by the tested natural-language
carrier: the proffer itself shifted the merits judgment by
`+8.07 [+4.86,+11.23]` rating points.

The next question therefore moves to the existing causal state.

---

## 1. Scientific question

Stage 5 established that changing target availability before a zero-use rule changes a
mid-network rule-time state that causally affects later evidence suppression.

What Stage 5 did **not** establish is whether this state carries an **executable
target × policy relation**, rather than merely target/context readiness.

G23C asks:

> **Does the rule-time causal state encode the policy value in a target-conditioned
> form that can be causally exchanged before the evidence arrives?**

Short form:

> **target-conditioned policy-state interchange**

---

## 2. Why this is the missing link

The current paper spine is:

1. G0: prospective exclusion is weaker than retrospective exclusion.
2. C2 controls: this is not simple instruction forgetting.
3. G23A: the prospective timing cost is discontinuously amplified at `w=0`.
4. Stage 5: target availability changes a causal rule-time state before later evidence.

The missing mechanistic link is:

> **Is that rule-time state actually carrying the executable exclusion policy for this
> target, or is it only a generic consequence of seeing a matching preview?**

G23C tests this directly without constructing a judgment-neutral semantic preview.

---

## 3. Existing 2×2 substrate

Reuse the exact Stage-5 matched chronology and the same two models for which the direct
readout reproduces the behavioral contrast:

- Qwen3-8B;
- Mistral-Small-24B.

Use the existing Stage-5 frozen items from:
- `legal_judgment`;
- `evidence_inference`.

Four cells:

```text
M0     matched semantic preview   -> weight 0%   rule -> evidence -> answer
M100   matched semantic preview   -> weight 100% rule -> evidence -> answer

U0     unrelated length-matched preview -> weight 0%   rule -> evidence -> answer
U100   unrelated length-matched preview -> weight 100% rule -> evidence -> answer
```

These are the Stage-5 ME / MA / UE / UA cells, renamed only for clarity.

The preview content is held fixed when policy value is swapped. Therefore a
within-preview policy-state intervention cannot be explained by the preview's direct
evidential effect.

No new behavioral dataset is created.

---

## 4. Baseline bridge, before patching

For sign `s=+1` when the evidence raises the judgment and `s=-1` when it lowers it:

```text
PolicyEffect_M = s · [Y(M100) - Y(M0)]
PolicyEffect_U = s · [Y(U100) - Y(U0)]

TargetPolicyInteraction =
    PolicyEffect_M - PolicyEffect_U
```

Positive `TargetPolicyInteraction` means the 0-vs-100 policy distinction has a larger
behavioral consequence when the target proposition was available before the rule.

### Frozen bridge gate

Patching is interpretable only if, on the direct readout used by Stage 5:

1. pooled `PolicyEffect_M >= 5.0` and its 95% CI lower bound > 0;
2. pooled `TargetPolicyInteraction >= 5.0` and its 95% CI lower bound > 0;
3. both quantities have positive model means in 2/2 models.

If this bridge fails, stop before policy-state interchange.

The gate is checked on all complete items; do not preselect items by behavioral gap.

---

## 5. Intervention

Patch only a **single rule-summary position**: the final token of the rule block
(`rule_end`).

Reason:
- it is a semantic site shared by all four conditions;
- it sits after the complete rule has been processed but before evidence;
- unlike whole-span patching, it does not require token-wise alignment between the
  `0%` and `100%` rule strings.

Primary layer: **layer 14 in both models**.

This layer is fixed from the already-completed Stage-5 localization:
- Qwen3-8B has a strong rule-time effect at L14–18;
- Mistral-Small-24B has a strong effect at L12–16.

Negative layer controls:
- layer 4;
- layer 24, or the nearest valid layer if a model has fewer than 25 layers.

No layer search is performed in G23C.

---

## 6. Four policy-value interchanges

Within each preview condition, exchange only the rule-end hidden state:

```text
M100 -> M0
M0   -> M100

U100 -> U0
U0   -> U100
```

Define donor-direction-aligned switch effects:

```text
Switch_M_100to0 = s · [Y(patch M100 -> M0) - Y(M0)]
Switch_M_0to100 = s · [Y(M100) - Y(patch M0 -> M100)]

Switch_U_100to0 = s · [Y(patch U100 -> U0) - Y(U0)]
Switch_U_0to100 = s · [Y(U100) - Y(patch U0 -> U100)]
```

Positive means the recipient moved toward the donor policy's behavioral effect.

Then:

```text
PolicyTransfer_M =
    mean(Switch_M_100to0, Switch_M_0to100)

PolicyTransfer_U =
    mean(Switch_U_100to0, Switch_U_0to100)

TargetConditioning =
    PolicyTransfer_M - PolicyTransfer_U
```

All quantities are raw sign-aligned rating points. No recovery fractions and no
division by behavioral gaps.

---

## 7. Frozen inference

- cluster bootstrap over independent case skeletons;
- seed `20260923`;
- 10,000 percentile resamples;
- pooled inference keeps model observations from the same skeleton in one cluster;
- per-model results reported separately;
- no trimming / winsorisation / post-result item filtering.

Meaningful floor: **3.0 rating points**.

---

## 8. Outcome map

### `target-conditioned-policy-state`

Requires at primary L14:

1. `PolicyTransfer_M >= 3.0`, CI lower > 0, positive in 2/2 models;
2. `TargetConditioning >= 3.0`, CI lower > 0, positive in 2/2 models;
3. the same signed pattern is absent or substantially weaker at the frozen negative
   layers 4 and 24.

Licensed claim:

> **When the target proposition is available during policy processing, the rule-time
> state carries causally exchangeable information about whether that target should have
> zero or full decision weight.**

This is stronger than Stage 5's current “target availability changes a causal state”
claim and directly connects the behavioral exclusion law to a policy-specific
mechanism.

Do not call it a universal function vector or a single reusable direction.

### `generic-policy-state`

`PolicyTransfer_M` and `PolicyTransfer_U` both pass, but
`TargetConditioning` does not.

Licensed claim:

> the rule-time state carries policy value, but the intervention does not show that
> policy encoding depends on target availability.

This weakens the target-conditioned mechanism story.

### `target-readiness-only`

The baseline bridge passes but `PolicyTransfer_M` does not.

Licensed claim:

> Stage 5's transferable state is not shown to carry the policy value itself; it may
> instead reflect target/context readiness or another covarying state.

Do not continue to call it an executable control state.

### `bridge-failed`

The frozen behavioral bridge fails. Stop before patching.

### `unresolved`

Any other pattern.

---

## 9. Controls

Required implementation checks:

1. **identity patch**: patch a condition's own rule-end state back into itself; output
   must match its baseline within numerical tolerance;
2. exact same item, model, prompt and readout between donor/recipient except policy value
   inside each M or U pair;
3. evidence has not been processed at the patch site;
4. frozen negative layers 4 and 24;
5. report both patch directions separately before averaging.

Do not add orthogonal-direction or learned-vector controls unless this primary
interchange first succeeds; the old held-out shared steering direction already failed.

---

## 10. Relation to nearest prior

This experiment is not a generic function-vector search. Function-vector work shows
that task information can be causally transported in latent states. G23C asks a
different conditional-composition question: whether a **policy value becomes causally
executable for a particular semantic target only when that target is available during
policy processing**.

It is also distinct from generic instruction-position work and from contextualization
race-condition work: the outcome is the causal eligibility of later evidence under a
standing zero-use policy, and the intervention is on the rule-time policy state.

---

## 11. Authorization boundary

Before any G23C model forward pass or activation patch:

1. verify exact Stage-5 cell reconstruction;
2. implement the four policy-value patch directions;
3. implement the frozen bridge and classifier above;
4. add tests for sign conventions, identity patch, pooled skeleton clustering, fixed
   layers and stop rule;
5. commit and tag a dedicated G23C design freeze;
6. explicitly update `STATUS.md`.

Until then:

> **NO G23C COMPUTE.**
