# G1 preregistration — external validation before further mechanism

**Created:** 2026-08-29  
**Status:** DESIGN ONLY. This file must be finalized and source hashes committed before any G1 `DENY` condition is run.

G0 was a valid preregistered test on a controlled authored suite, but it discovered an unexpected prospective-nullification effect rather than the original human-like Unring-the-Bell ordering. G1 is a new experiment with a different purpose: determine whether the broader mother phenomenon survives independently authored, natural experimental materials.

---

## 1. Research question

When a model has access to information `E` and an explicit policy says `E` is outside the information set permitted for a particular decision `Y`, can the model:

1. correctly state the policy;
2. retain/recall `E`;
3. nevertheless make `Y` causally invariant to `E`?

The target is **policy-conditioned causal non-use**, not memory deletion.

---

## 2. Dataset tiers

G1 primary inference is performed only on the **External Validation Suite (EVS-v1)**. The existing 144-item suite is CDS-v1 and is excluded from G1 primary confirmation.

Before running models, every EVS source must be registered in `data/external/source_manifest.json` with:

- canonical citation/URL;
- local source filename or retrieval instruction;
- content hash when material is imported;
- reuse/license status;
- independent-unit definition;
- transformation script;
- cluster identifier rule.

Candidate families and their current priority are documented in `DATASET_REDESIGN.md`.

---

## 3. Inclusion policy

### 3.1 Preferred external source

An item family is primary if its underlying semantic content was independently authored before this project and the normative information boundary follows from the source task rather than being invented solely to create leakage.

Examples:

- inadmissible evidence in an existing legal experiment;
- outcome information when judging ex-ante decision quality;
- answer-side knowledge when predicting an uninformed person's knowledge;
- retracted/invalid information in an existing CIE experiment.

### 3.2 No deny-based item selection

No item may be included/excluded based on `DENY` outcomes from any target model.

### 3.3 Leverage

Preferred: use all source units when the original experiment or a deterministic verifier establishes that the critical-information manipulation matters.

If a model-specific leverage screen is unavoidable, it must use **ALLOW only**, with a threshold frozen before any DENY output exists. The primary report must also include the unscreened result.

### 3.4 Independent units

Surface variants, paraphrases, repeated presentations, or condition cells derived from the same original vignette are one cluster. Inference resamples/clusters at the original semantic unit.

---

## 4. Primary condition design

Whenever a natural matched critical-information pair is available, compile:

```text
ALLOW_POS
ALLOW_NEG
DENY_POS
DENY_NEG
```

where `POS/NEG` denote opposing or meaningfully different values of the critical information, not necessarily positive/negative sentiment.

If the original human paradigm instead supplies `control / critical-information / retraction` cells that cannot be cleanly counterfactually paired, retain the source design and use its source-specific raw contrast. Do not force a synthetic `E-` merely to satisfy one schema.

Pre/Post order is a secondary factor and is included only when the manipulation remains natural in both orders.

---

## 5. Primary outcomes

For paired counterfactual designs:

```text
AllowedSensitivity   = Y(ALLOW_POS) - Y(ALLOW_NEG)
ForbiddenSensitivity = Y(DENY_POS)  - Y(DENY_NEG)
PolicySuppression    = AllowedSensitivity - ForbiddenSensitivity
```

Direction-align before pooling when the source defines a direction.

### Primary reporting

- raw `AllowedSensitivity`;
- raw `ForbiddenSensitivity`;
- raw `PolicySuppression`;
- cluster-bootstrap confidence intervals;
- family-level results before any pooled average.

### Secondary normalized statistic

```text
LeakageFraction = ForbiddenSensitivity / AllowedSensitivity
```

Only report as a primary-looking number for units/families where `|AllowedSensitivity|` exceeds the frozen leverage floor. Never report a ratio without its raw numerator and denominator.

For categorical tasks, use a preregistered probability/logit-margin analogue instead of coercing the output into a 0–100 score.

---

## 6. Policy and memory probes

Decision, rule, and memory probes are separate calls.

### Rule probe

Question whether the critical information is permitted for the specified decision. Report exact/probabilistic rule accuracy.

### Memory probe

Test recognition/recall of the critical information after the deny context.

A strong mother-phenomenon case is:

```text
Rule knowledge: high
Memory of E: high
ForbiddenSensitivity: non-zero
```

A low-memory case is not evidence for the retention/non-use dissociation.

---

## 7. Hypotheses

### H1 — Policy knowledge

Rule accuracy under `DENY` is high.

### H2 — Information retention

Critical information remains recoverable under `DENY`.

### H3 — Causal leakage exists in at least some independently authored true-but-disallowed families

`ForbiddenSensitivity` differs from zero in the direction of the critical-information manipulation.

This is a family-level claim. G1 does **not** preregister that every family must leak.

### H4 — Policies are partially effective

`|ForbiddenSensitivity| < |AllowedSensitivity|` on average within leaking families.

This distinguishes incomplete gating from total failure to respond to the rule.

### H5 — exclusion reason is heterogeneous

`true_but_forbidden`, `temporal/perspective`, and `false_or_invalid` families may differ substantially. Report the interaction rather than hiding it under a pooled mean.

### H6 — timing is exploratory/secondary

No universal sign is preregistered for `Pre - Post`. CDS-v1 and human CIE work already give opposite orderings. Any timing result must be reported by family.

---

## 8. Readout freeze

Before the first DENY run, each family must specify:

- exact prompt/output format;
- parse function or fixed-position score;
- whether reasoning is requested;
- temperature/sampling;
- retries/error policy;
- treatment of refusals/invalid parses.

If both direct and reasoned formats are used, one is declared primary in advance and the other is a robustness condition.

No LLM judge is used for G1 primary outcomes.

---

## 9. Model panel

The exact panel must be frozen before DENY runs. It should include multiple model families and at least two open-weight models suitable for later mechanism work.

Do not use model count to compensate for low source diversity: the experimental unit for the broad claim is the external source/item structure, not the number of checkpoints run on it.

---

## 10. Statistical inference

Primary:

- paired contrasts within semantic units;
- cluster bootstrap over original source units;
- family-level confidence intervals;
- pooled estimate only after showing family heterogeneity.

Formal version:

- mixed-effects model with source/family and semantic unit as grouping structure where the source design supports it;
- model family/checkpoint as another factor, not 12 independent replications of one item set.

Multiple source-specific tests must be labeled primary/secondary before the freeze.

---

## 11. Confirmatory gate before mechanism

### Broad-mechanism gate

To interpret the existing CDS-v1 patching result as a candidate mechanism for a general phenomenon, require:

- at least two independent **true-but-disallowed** EVS families with reliable forbidden sensitivity;
- high policy knowledge;
- high memory of E;
- at least one open-weight model that exhibits the external effect.

Then run mechanism first on a small external subset and ask whether the controlled causal signature transfers.

### Narrow-mechanism gate

If only a single external family reproduces, mechanism claims must be family-specific.

### Stop gate

If the external suite is clean and leakage is confined to CDS-v1, do not continue broad activation patching under the label of a general evidence-gating defect.

---

## 12. Freeze checklist

Do not mark G1 frozen until every box is satisfied:

- [ ] external source materials obtained legally
- [ ] source manifest completed
- [ ] raw/material hashes committed
- [ ] transformations audited by hand
- [ ] cluster IDs frozen
- [ ] condition compiler frozen
- [ ] readout frozen
- [ ] model panel frozen
- [ ] leverage rule frozen
- [ ] primary/secondary hypotheses frozen
- [ ] no target-model DENY output has been inspected

At freeze time, replace the `Status` line at the top with the date and commit SHA.
