# Next experiments after scientific register v3

**Status:** design-audit document only.
**Updated:** 2026-09-04.
**Authoritative ledger:** [SCIENTIFIC_REGISTER_2026-09-04_V3.md](SCIENTIFIC_REGISTER_2026-09-04_V3.md)  
**Latest mainline audit:** [MAINLINE_AUDIT_2026-09-05_V4.md](MAINLINE_AUDIT_2026-09-05_V4.md)

No model generation is authorized by this document.

The next experiment must explain:

> **Why is the same exclusion rule less effective before evidence than after evidence?**

Do not run a new experiment merely because it is surprising.

---

# Priority 1 — G22: Target Knowledge vs Evidential Instantiation (branching discriminator)

## Scientific question

> **Is knowing exactly what future evidence will say enough to pre-exclude it, or does
> exclusion become effective only once that proposition has already entered the model
> as evidence?**

This is the clean missing factor between G0 and G18.

G18 mixed:
- semantic knowledge of the target;
- substantive assertion of the target proposition.

G22 must separate them.

## Core target-state factor

### U — unresolved target

Ordinary prospective structure:

```
BACKGROUND
→ EXCLUDE future target
→ actual evidence E
→ decision
```

The model does not know the target content when the rule is processed.

### K — known but non-evidential target

Before the rule, provide a representation that fixes exactly what the future target
will contain **without asserting it as case evidence**.

Conceptual form:

```
BACKGROUND
→ NON-EVIDENTIAL TARGET SPECIFICATION(P)
→ EXCLUDE target
→ actual evidence E(P)
→ decision
```

This is the critical new condition.

The carrier must:
- identify the exact future target proposition;
- not present P as a fact to be used in the judgment;
- have near-zero direct effect on the no-evidence judgment;
- not itself say “ignore” / “exclude” / “irrelevant”;
- not become an implicit second policy;
- not trivially reveal the correct answer.

Possible carrier families to audit:
- retrieval manifest describing the payload that a future record would contain;
- interface/schema metadata mapping a document identifier to a payload description;
- quoted non-evidential template explicitly marked as a description of the future
  record, not a claim that the event occurred.

Do not choose the carrier by intuition alone. Pilot only on non-outcome-exposing
neutrality checks before preregistration.

### I — evidentially instantiated target

Before the rule, assert P as substantive case information:

```
BACKGROUND
→ EVIDENTIAL ASSERTION(P)
→ EXCLUDE target
→ actual evidence E(P)
→ decision
```

This is the conceptual analogue of G18 `para/entail`.

## Mandatory per-state baselines

For each target-state level U/K/I, collect:

1. target-state only;
2. target-state + actual evidence, no rule;
3. target-state + exclusion + actual evidence.

This permits:

```
EvidenceMarginal_no_rule(state)
EvidenceMarginal_exclude(state)
ExclusionEffect(state)
```

Use sign-aligned raw rating points.

Do not use REI ratios when state changes evidence leverage.

## Critical neutrality gate for K

Before looking at exclusion effects, K must satisfy a frozen neutrality criterion.

Conceptually:

```
|Y(K only) - Y(U only)| <= small threshold
```

pooled and on a large majority of items.

The exact threshold must be set before generation.

If K materially changes judgment, the design fails to separate target knowledge from
evidential instantiation and must be rebuilt before any exclusion claim.

## Competing predictions

### H-A — target knowledge is sufficient

Prediction:
- K exclusion substantially approaches I exclusion;
- U remains weaker.

Consequence:
semantic knowledge itself is enough, but **this is not automatically a novelty-bearing
headline**. G22 becomes the bridge to a second experiment on when the policy-target
relation is composed. The stronger target is correct late understanding without causal
reconstruction of the exclusion relation.

### H-B — evidential instantiation is required

Prediction:
- K remains close to U;
- I is much stronger.

Consequence:
if K is neutral and correctly understood, this is itself a non-obvious mainline result:
knowing future evidence is insufficient, while an already-instantiated matching
evidential state enables exclusion. The mechanism story becomes retrospective
revision/cancellation, not generic deferred binding.

### H-C — neither target knowledge nor prior evidence is the whole story

Prediction:
K and I do not yield the expected separation, or effects depend strongly on how
control-relevant semantics are locally encoded.

Consequence:
revisit local semantic control / label routing before constructing a mainline claim.

## Positive controls

G22 should preserve existing boundaries rather than add broad new model sweeps.

Useful:
- matched Admit condition where order should not create the same discontinuity;
- explicit arithmetic future weighting on the same temporal pattern if a clean matched
  version can be constructed.

Do not add many unrelated controls.

## Model panel

Do not freeze yet.

A reasonable audit panel is the established five-model cross-vendor set:
- Qwen3-8B;
- Gemma-3-12B;
- Phi-4-mini;
- Qwen3.5-27B;
- Mistral-Small-24B.

Final panel is chosen only after material design is complete and before outcomes.

## Materials

Fresh skeletons preferred.

No requirement for another large breadth sweep.

The important work is:
- target-state purity;
- leverage;
- semantic-neutrality of K;
- matched proposition content across K/I/E;
- mixed evidence directions.

---

# Conditional Priority 2A — only if G22 supports target knowledge sufficiency

## Mapping timing / deferred composition

Only run if K already shows that non-evidential semantic target knowledge is sufficient.

Then hold all semantic propositions constant and vary only when the mapping from policy
referent to proposition becomes available.

Conceptual design:

```
catalog contains P and Q in both conditions

EARLY-MAP:
mapping(D7→P) → EXCLUDE D7 → ...

LATE-MAP:
EXCLUDE D7 → mapping(D7→P) → ...
```

Both prompts contain the same P/Q semantic content.

Mandatory:
- full-context mapping comprehension is high in LATE-MAP;
- no difference in target evidentiality;
- no target-to-evidence recency confound;
- shared post-resolution checkpoint after mapping.

Only here does a rule-replay condition become scientifically useful.

### Operator replay

If LATE-MAP fails despite correct mapping:

```
EXCLUDE → late mapping → EXCLUDE
```

Compare against:
- EARLY-MAP + replay;
- target/mapping replay without exclusion replay;
- neutral processing buffer.

The key distinction:

> does extra computation time rescue, or must the exclusion operator itself be
> re-executed after target resolution?

This is where Racing-Thoughts-style critical-window logic becomes useful.

---

# Conditional Priority 2B — only if G22 supports evidential-instantiation dependence

## Passive gate vs active revision

If K≈U but I≫U/K, test:

> does exclusion merely prevent later evidence from being read, or does it actively
> construct a target-specific counteracting state once the proposition already exists?

Candidate behavioral clue:
G18 semantic exclusion falls far below preview-only baseline.

Required deconfounding:
- include target-present + rule + **no later evidence**;
- compare exclusion with matched Admit and neutral rule;
- distinguish changing belief in P from changing whether P may be used.

Mechanism:
- patch successful target-present exclusion state into target-absent contexts;
- test whether the state shifts judgment even without later E;
- compare with attention/span gating.

Do not call this “phantom exclusion” in the paper unless a robust law is established.
The no-evidence cell is a mechanism discriminator, not novelty by itself.

---

# Supporting diagnostic — D22-A tagged routing deconfound

This is not a main experiment.

Existing Stage 3B cannot separate standing-policy execution from local semantics of
`[unverified]`.

Use the same exact numeric routing substrate.

Candidate cells:

1. semantic labels, no policy;
2. semantic labels, matching policy;
3. semantic labels, reversed policy;
4. nonce labels, policy defining which tag is excluded;
5. optional nonce labels with explicit semantic definitions.

Question:

> does the earlier standing policy add causal routing beyond what the incoming label
> already does locally?

If semantic-label/no-policy already gives near-zero leakage, old Stage3B should be
treated mainly as local semantic routing evidence.

If policy adds strong value and can reverse natural label semantics, H-C weakens.

Do not turn the answer into the paper center.

---

# G20 status

Previous G20 versions are historical design provenance.

Do not run:
- old PRE/LATE target swap;
- current P/U swap;
- rule replay in isolation.

The deferred-composition idea remains conditional on G22 demonstrating that target
knowledge can be cleanly separated from evidential instantiation.

---

# G21 status

Source–Proposition Scope Entanglement:
- interesting;
- deconfounded design retained;
- not current paper;
- no generation.

---

# ReGround G19

Cancelled before generation.

Do not run.

---

# Freeze sequence for G22

Before any model outcome is observed:

1. choose a K carrier that is genuinely non-evidential;
2. build fresh materials;
3. inspect all prompts manually;
4. define K neutrality gate;
5. define leverage qualification;
6. freeze U/K/I estimands;
7. state H-A/H-B/H-C predictions;
8. preregister;
9. implement analyzer and tests;
10. commit/tag;
11. only then generate.

If the design cannot cleanly separate K from I, do not run it.
