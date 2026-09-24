# G23C-R preregistration draft — fresh-material joint replication of the RQ3 mechanism

**Created:** 2026-09-23; revised 2026-09-24 after G24B completed.

**Status:** **HOLD — DESIGN PRESERVED, NO COMPUTE.**  
The design is technically valid, but the parent G23C/G24B mechanism claim was
downgraded from headline novelty after a G18-style reviewer-obvious audit.
**NO G23C-R MODEL FORWARD PASS, ACTIVATION CAPTURE, OR PATCHING COMPUTE IS AUTHORIZED.**

G23C-R was designed as the final RQ3 mechanism replication. It is now parked.
It does **not** introduce a new mechanistic story, and replication of the same
reviewer-obvious parent claim is not sufficient reason to execute it. It jointly replicates, on a material set frozen before Stage 5/G23C/G24B:

1. **G23C:** the causal efficacy of the rule-time zero-vs-full policy state is larger
   when the semantic target is available during policy processing;
2. **G24B:** with the recipient prompt fixed, matched-target donor states carry a larger
   causally transportable zero-vs-full policy effect than unrelated-target donor states.

The second endpoint was added before G23C-R freeze because G24B resolved the major
donor-state-vs-recipient-sensitivity confound after the original G23C-R draft was written.
Running a fresh replication of G23C alone would leave the stronger G24B claim tied to the
same Stage-5 discovery materials.

---

## 1. Frozen parent results

### G23C v1 — completed

Design tag:
`g23c-target-conditioned-policy-state-design-v1`.

Frozen primary result on the Stage-5 75-item set:

- `PolicyTransfer_M = +13.03 [+11.69,+14.31]`;
- `PolicyTransfer_U = +4.89 [+3.73,+6.18]`;
- `TargetConditioning = +8.15 [+6.91,+9.44]`;
- model-level TC positive in 2/2;
- L4 TC `-0.03`;
- L24 TC `+0.07`;
- identity patch max absolute error `0.0000`.

Frozen verdict:
`target-conditioned-policy-state`.

Licensed synthesis:

> **the causal efficacy of the rule-time zero-vs-full policy state is
> target-conditioned.**

### G24B v1 — completed

Design tag:
`g24b-donor-recipient-factorization-design-v1`.

Frozen primary result on the same Stage-5 75-item set:

- `DonorPolicy_M = +10.81 [+8.31,+13.41]`;
- `DonorPolicy_U = +6.79 [+5.22,+8.78]`;
- `DonorTargetInteraction = +4.02 [+2.27,+6.14]`;
- model-level DTI positive in 2/2;
- L4 DTI `-0.15`;
- L24 DTI `+0.07`;
- identity patch max absolute error `0.0000`.

Frozen verdict:
`donor-conditioned-policy-state`.

Licensed synthesis:

> **with the recipient prompt held fixed, rule-end states from matched-target donors
> carry a larger causally transportable zero-versus-full policy effect than rule-end
> states from unrelated-target donors: target availability during policy processing
> changes what policy information the rule-time state itself contains.**

G23C-R tests whether these two frozen properties reproduce on disjoint materials.

---

## 2. Why a fresh-material replication is still required

Stage 5 localized the causal window on `items_v1`.

G23C then established a new policy-state property on those same items.

G24B resolved G23C's donor/recipient factorization on those same items.

All three designs were preregistered/frozen and their interventions differ, so this is
not post-hoc overfitting of the estimand. However, a reviewer can still compress the
mechanism section as:

> “localization, policy-state characterization, and donor-state factorization were all
> established on the same discovery materials.”

G23C-R removes that material reuse for **both** confirmatory mechanism properties.

---

## 3. Materials — pre-existing, frozen, disjoint

Use only `data/items/g18_v1.jsonl`:

- `legal_judgment`: 40 items / 10 frozen skeletons;
- `evidence_inference`: 30 items / 10 frozen skeletons;
- total: **70 items / 20 independent skeletons**.

Exclude the 30 G18 `ranking_selection` items because the Stage-5/G23C/G24B direct
mechanism substrate was validated only for legal judgment and evidence inference.

These 70 items:
- were frozen before G23C/G24B;
- are disjoint from `items_v1.jsonl` at the item/skeleton level under the G18 freeze;
- are included exhaustively;
- are never selected by G18 effect size, bridge effect, G23C effect, G24B effect, or any
  model output from this round.

Cluster key is the frozen G18 `meta["skeleton"]`.

Direction sign:
- `s=+1` for `critical_direction == "increase"`;
- `s=-1` for `critical_direction == "decrease"`.

---

## 4. Frozen preview construction

For every item:

```text
M preview = item.meta["previews"]["para"]
U preview = item.meta["previews"]["unrel"]
```

Reuse these strings byte-for-byte.

No new paraphrase, no new filler, no LLM-generated preview, no manual repair.

Important interpretation discipline:

G18's matched paraphrase can itself instantiate the target proposition behaviorally.
That is acceptable here. G23C-R does **not** ask whether semantic knowledge is
non-evidential. It asks whether the already-defined Stage-5/G23C/G24B target-available
vs unrelated-preview mechanism replicates on independent materials.

---

## 5. Mandatory tokenizer/site audit before freeze

Before any target-model forward pass, run a tokenizer-only audit on both frozen models.

For all 70 items × 4 cells × 2 models:

1. every cell compiles;
2. `rule_end` exists;
3. `rule_end` precedes the first later-evidence token;
4. within M, 0% vs 100% cells differ only in the rule block;
5. within U, 0% vs 100% cells differ only in the rule block;
6. at fixed policy value, M vs U cells differ only in the frozen preview block;
7. absolute M-vs-U difference in `rule_end` token position is recorded.

Position gate:

> if more than **5% of item/model pairs** have an absolute M-vs-U
> `rule_end` position difference greater than **4 tokens**, the design stops before
> model compute.

Do not pad, truncate, rewrite, or drop individual items to repair this gate.

All 70 items remain in scope or the round is redesigned and re-frozen before compute.

---

## 6. Four frozen cells

Use the exact G23C/G24B semantics:

```text
ME = M0    G18 para preview  -> weight 0%   rule -> evidence -> answer
MA = M100  G18 para preview  -> weight 100% rule -> evidence -> answer

UE = U0    G18 unrel preview -> weight 0%   rule -> evidence -> answer
UA = U100  G18 unrel preview -> weight 100% rule -> evidence -> answer
```

The rule is the existing `uniform_weight_rule(item, 0.0 | 1.0)`.

The answer readout is the same fixed-position direct digit expectation used in Stage 5,
G23C and G24B.

No chain-of-thought readout, no generated rationale, no new prompt variant.

---

## 7. Models, site and layers

Exactly the completed RQ3 panel:

- Qwen3-8B;
- Mistral-Small-24B.

Patch site:
- `rule_end` only.

Frozen layers:
- L4 negative control;
- **L14 primary**;
- L24 negative control.

No:
- model addition;
- model replacement after output;
- layer search;
- site search;
- head search;
- learned steering direction;
- orthogonal-vector search.

---

## 8. Phase 1 — fresh behavioral bridge

Before any activation patching, run only the four direct cells.

Per item:

```text
PolicyEffect_M = s · [Y(MA) - Y(ME)]
PolicyEffect_U = s · [Y(UA) - Y(UE)]

TargetPolicyInteraction =
    PolicyEffect_M - PolicyEffect_U
```

Bridge gates are exactly the G23C/G24B parent gates:

1. pooled `PolicyEffect_M >= 5.0` and 95% CI lower bound > 0;
2. pooled `TargetPolicyInteraction >= 5.0` and 95% CI lower bound > 0;
3. both quantities have positive model means in 2/2 models.

If any bridge gate fails:

> **VERDICT = bridge-failed. STOP BEFORE ALL PATCHING.**

Do not inspect a subset, alter previews, change direct readout, or relax gates.

---

## 9. Phase 2 — one capture, joint G23C + G24B replication

If and only if the bridge passes, capture every cell's `rule_end` state at L4/L14/L24
and run the union of the frozen parent interventions.

### 9.1 G23C within-preview reciprocal transfer

Required unique directions:

```text
MA -> ME
ME -> MA

UA -> UE
UE -> UA
```

Define the original G23C donor-direction-aligned switches and:

```text
PolicyTransfer_M =
    mean(Switch_M_100to0, Switch_M_0to100)

PolicyTransfer_U =
    mean(Switch_U_100to0, Switch_U_0to100)

TargetConditioning =
    PolicyTransfer_M - PolicyTransfer_U
```

### 9.2 G24B fixed-recipient donor grid

Recipients are frozen to policy-0 cells:

```text
R ∈ {ME, UE}
```

Every cell is a donor:

```text
ME -> ME     MA -> ME     UE -> ME     UA -> ME
ME -> UE     MA -> UE     UE -> UE     UA -> UE
```

Per recipient:

```text
DonorPolicy_M(R) =
    s · [Y(MA -> R) - Y(ME -> R)]

DonorPolicy_U(R) =
    s · [Y(UA -> R) - Y(UE -> R)]

DonorTargetInteraction(R) =
    DonorPolicy_M(R) - DonorPolicy_U(R)
```

Primary per-item quantities pool the two recipients exactly as G24B:

```text
DonorPolicy_M =
    mean_R DonorPolicy_M(R)

DonorPolicy_U =
    mean_R DonorPolicy_U(R)

DonorTargetInteraction =
    mean_R DonorTargetInteraction(R)
```

Recipient-specific DTIs are report-only.

### 9.3 Unique patch table

Do not duplicate forward passes unnecessarily.

The union of G23C + G24B scientific patch directions contains exactly:

```text
ME -> ME
MA -> ME
UE -> ME
UA -> ME

ME -> UE
MA -> UE
UE -> UE
UA -> UE

ME -> MA
UE -> UA
```

= **10 unique donor→recipient scientific patches per layer/item**.

In addition, identity checks are required for all four cells at all three layers:

```text
ME -> ME
MA -> MA
UE -> UE
UA -> UA
```

Identity cells already present in the 10-patch grid may be reused computationally, but
the analyzer must still report all 4 × 3 identity checks explicitly.

---

## 10. Frozen inference

For both parent replications:

- seed `20260924`;
- 10,000 percentile bootstrap resamples;
- cluster by G18 frozen `meta["skeleton"]`;
- pooled resampling keeps both models' observations from one skeleton together;
- per-model statistics reported;
- no trimming;
- no winsorisation;
- no behavioral-gap selection;
- no ratio normalization.

Meaningful floor:
- `3.0` raw rating points for mechanism estimands.

Bridge floor:
- `5.0`.

Identity tolerance:
- `0.5` rating points.

---

## 11. Frozen G23C replication classifier

Use the completed G23C logic unchanged.

At L14:

### `g23c-replicated`

Requires:
1. `PolicyTransfer_M >= 3.0`, CI lower > 0, positive in 2/2 model means;
2. `TargetConditioning >= 3.0`, CI lower > 0, positive in 2/2 model means;
3. at both L4 and L24, the parent G23C control clause holds:
   - `PASS(TargetConditioning)` is false, **or**
   - L14 pooled TC exceeds that control layer by at least +3.0;
4. identity checks pass.

Other parent-style outcomes are reported descriptively:
- `g23c-generic-policy-state`;
- `g23c-target-readiness-only`;
- `g23c-unresolved`.

For overall replication status, only `g23c-replicated` counts as replication of the
parent headline.

Licensed G23C replication statement:

> **On a disjoint frozen material set, the causal efficacy of the rule-time
> zero-vs-full policy state is again stronger when the target proposition is available
> during policy processing.**

---

## 12. Frozen G24B replication classifier

Use the completed G24B logic unchanged.

At L14:

### `g24b-replicated`

Requires:
1. `DonorPolicy_M` passes the 3-point / CI / 2-of-2 rule;
2. `DonorTargetInteraction >= 3.0`, CI lower > 0, positive in 2/2 model means;
3. at both L4 and L24, the parent G24B control clause holds:
   - `PASS(DonorTargetInteraction)` is false, **or**
   - L14 pooled DTI exceeds that control layer by at least +3.0;
4. identity checks pass.

Other parent-style outcomes are reported descriptively:
- `g24b-donor-generic-policy-state`;
- `g24b-no-donor-policy-state`;
- `g24b-unresolved`.

For overall replication status, only `g24b-replicated` counts as replication of the
parent headline.

Licensed G24B replication statement:

> **On a disjoint frozen material set and with the recipient prompt held fixed,
> matched-target donor states again carry a larger causally transportable
> zero-versus-full policy effect than unrelated-target donor states.**

Do not strengthen this to a universal vector claim or claim that all target semantics
and policy information are localized in one state.

---

## 13. Overall replication verdict

Decision order:

1. if the Phase-1 bridge fails:
   - **`bridge-failed`**
   - no patching;
2. otherwise evaluate both parent replications.

### `jointly-replicated`

```text
G23C replication = g23c-replicated
AND
G24B replication = g24b-replicated
```

Licensed paper-level synthesis:

> **The RQ3 mechanism replicates on a material set frozen independently of the
> discovery set: target availability during policy processing modulates both the causal
> efficacy and the donor-side policy content of the rule-time state.**

### `partial-replication`

Exactly one parent headline replicates.

Consequence:
- retain the replicated property;
- explicitly scope the non-replicated property to the original Stage-5 material set;
- do not launch a rescue mechanism round.

### `not-replicated`

Neither parent headline replicates despite a passing bridge.

Consequence:
- retain the original frozen G23C/G24B results as material-specific;
- remove the general fresh-material mechanism claim;
- do not launch a rescue mechanism round.

---

## 14. Interpretation discipline

G23C-R can establish replication of the completed **causal intervention properties**.

It cannot establish:
- that the entire target × policy conjunction lives in one hidden token;
- that downstream context has no role;
- a universal function vector;
- all architectures share the same layer;
- standing gating vs retrospective cancellation;
- semantic knowledge vs evidential instantiation.

The strongest safe joint interpretation is:

> **target availability during policy processing changes the causally transportable
> policy information available at the rule-time state, and this property reproduces on
> disjoint materials.**

Only use the final clause if the overall verdict is `jointly-replicated`.

---

## 15. Program-level stop rule

G23C-R is the final planned RQ3 mechanism experiment.

After the frozen outcome:
- `jointly-replicated` -> close RQ3 experiments and write;
- `partial-replication` -> scope the mechanism claim and write;
- `not-replicated` -> downgrade generality and write/reassess;
- `bridge-failed` -> report fresh-material substrate failure and write/reassess.

No automatic G23D follows any outcome.

The paper-scale audit's RQ2 question is assessed only after complete Sections 4/5/6 are
written. It is not a license to add another experiment now.

---

## 16. Authorization boundary and freeze checklist

Before any G23C-R target-model forward pass:

- [ ] implement G18 70-item loader using frozen `meta["skeleton"]`;
- [ ] implement byte-for-byte G18 `para` / `unrel` preview reuse;
- [ ] implement and pass the tokenizer/site/position audit in §5;
- [ ] implement Phase-1 bridge;
- [ ] implement the 10 unique scientific patch directions;
- [ ] implement all four identity checks × all three layers;
- [ ] implement G23C and G24B parent estimands/classifiers without changing their
      scientific gates;
- [ ] implement overall `jointly-replicated / partial-replication /
      not-replicated / bridge-failed` logic;
- [ ] tests lock cell construction, patch table, sign conventions, skeleton clustering,
      fixed layers/site/models, identity abort, both parent classifiers, overall verdict,
      and Phase-1 stop rule;
- [ ] commit the complete design/harness;
- [ ] create an annotated dedicated design tag;
- [ ] explicitly update `STATUS.md` after the tag to authorize exact compute.

Until all boxes are satisfied:

> **NO G23C-R COMPUTE.**
