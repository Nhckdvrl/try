# Paper outline — v3 target-state factorization

**Updated:** 2026-09-04.
**Current authority:** [SCIENTIFIC_REGISTER_2026-09-04_V3.md](SCIENTIFIC_REGISTER_2026-09-04_V3.md)

## Working title

Primary:
> **Can Language Models Commit to Ignore Future Evidence?**

Do not title around:
- target addressability;
- scope collapse;
- generic binding;
- instruction order.

---

# 1. Introduction

Natural problem:
policies often precede the evidence they govern.

Question:
> **Can a language model commit in advance to ignore evidence it has not yet seen?**

Broad finding:
the same exclusion rule works worse before evidence than after evidence.

The paper then asks:
> **what must exist at policy-processing time for exclusion to become effective?**

---

# 2. G0 — prospective exclusion reversal

Figure 1.

- 144 frozen items;
- five families;
- 12 instruct models;
- two masked diffusion LMs;
- matched Admit controls.

Headline:
> **Prospective exclusion is systematically harder than retrospective exclusion.**

---

# 3. What the reversal is not

Compact characterization:
- not one wording;
- not simple distance decay;
- not causal decoder masking;
- not lack of declarative policy access;
- not inability to execute any future numeric rule.

Use:
- wording;
- delay;
- diffusion;
- policy probes;
- on-policy zero-state dissociation;
- arithmetic boundary.

Do not turn these into separate contributions.

---

# 4. What target information matters?

## 4.1 Object-existence ladder

Identifier/name/content-pending/type/direction do not reliably rescue.
Full content before rule does.

## 4.2 G18

Confirmed semantic-preview effect:
`Delta_semantic = +8.91 [7.15,+10.76]`, 5/5 positive.

Critical correction:
semantic previews also substantively assert the target proposition.

Therefore G18 does not isolate target knowledge from evidential instantiation.

## 4.3 Stage 4

Content-conditioned transfer across IDs.

Use as support for semantic target representation only.

---

# 5. The missing factorization

Main conceptual figure before new results:

```
UNRESOLVED
policy → future target

KNOWN-BUT-NON-EVIDENTIAL
target semantics known → policy → future evidence

EVIDENTIALLY-INSTANTIATED
target proposition already evidence → policy → later matching evidence
```

Question:
> **Is semantic knowledge enough, or must the target proposition already be in the
> evidential state?**

This is the new central scientific fork.

---

# 6. G22 — novelty-bearing experiment if the design passes

Figure 2.

Three target states:
- U unresolved;
- K known-but-non-evidential;
- I evidentially instantiated.

Mandatory:
- per-state no-rule baseline;
- per-state target-only baseline;
- raw-point exclusion effect;
- frozen neutrality gate for K.

The result determines the paper branch.

---

# 7A. If K rescues — deferred target composition

Then test:
- early vs late mapping;
- correct late mapping comprehension;
- shared post-resolution checkpoint;
- processing buffer;
- operator replay vs mapping replay.

Claim if confirmed:

> **Correctly resolving a future target after policy processing does not reconstruct the
> same causal exclusion state.**

Mechanism:
Racing-Thoughts-style critical-window / backpatch / frozen-backpatch logic.

---

# 7B. If only I rescues — retrospective evidence-state revision

Then test:
- target present + exclusion + no later evidence;
- matched Admit/neutral rule;
- passive future gate vs active target-specific cancellation.

Claim if confirmed:

> **Knowing future evidence is insufficient; natural-language exclusion becomes
> effective mainly by revising an already-instantiated evidence state.**

Mechanism:
Stage5 target-dependent rule state + constructive cancellation interventions.

---

# 7C. If neither cleanly separates

Do not invent a new center.

Use D22-A to deconfound tagged routing and reassess the mainline.

---

# 8. Policy knowledge vs causal enforcement

Keep concise.

Existing:
- policy probe;
- Qwen/Gemma on-policy dissociation;
- Phi heterogeneity.

If route A survives, add:
> late target recognition ≠ causal composition.

If route B survives, add:
> future target knowledge ≠ evidential control.

---

# 9. Mechanism

Figure 3.

Existing Stage5:
- Qwen3-8B;
- Mistral-Small-24B;
- causal target-dependent rule-time state.

New mechanism depends on G22 branch.

Do not pre-name the state as:
- binding;
- gate;
- cancellation;
- revision.

---

# 10. Discussion

## 10.1 Beyond instruction position
The paper isolates a target-state dependency, not generic position.

## 10.2 Beyond prospective memory
The model may remember the policy yet fail causal non-use.

## 10.3 Beyond generic binding
The object is future evidence control, not entity-attribute association.

## 10.4 Beyond policy benchmarks
The paper explains one specific computation behind standing-policy failure.

---

# 11. Method opening

General question:

> **How should future evidence policies be represented so they remain executable before
> their target exists?**

Possible routes:
- persistent structured rule state;
- factorized policy operator / target instance;
- delayed instantiation;
- external rule runtime;
- training objective for future-target control.

No ReGround contribution.

---

# 12. Main figure hierarchy

Figure 1 — G0 broad reversal.

Figure 2 — G22 target-state factorization.

Figure 3 — mechanism conditional on the surviving G22 branch.

Supporting:
- G18;
- Stage4;
- arithmetic;
- policy-access dissociation.

No G21 main figure.

---

# 13. Appendix

- full model×family G0;
- wording/delay;
- diffusion;
- requested-weight sweep;
- arithmetic;
- object-existence ladder;
- G18 full decomposition;
- Stage3B routing + correction note;
- Stage4;
- Stage5;
- failed shared steering;
- G20/G21/G19 historical designs.

The main text must remain narrative-first, not experiment chronology.
