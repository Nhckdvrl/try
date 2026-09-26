# G22 design audit — Target Knowledge vs Evidential Instantiation

**Experiment ID:** G22
**Registered:** 2026-09-04
**Status:** DESIGN AUDIT ONLY
**Preregistration:** none
**Freeze:** none
**Generation:** NOT AUTHORIZED

**Scientific authority:** [SCIENTIFIC_REGISTER_2026-09-04_V3.md](SCIENTIFIC_REGISTER_2026-09-04_V3.md)

---

# 1. Why G22 exists

G0 shows:

```
EXCLUDE → evidence
```

is systematically weaker than:

```
evidence → EXCLUDE
```

The project then found:
- arbitrary future identifiers / content-pending stubs do not reliably rescue;
- full content before the rule does;
- G18 semantic previews strongly increase exclusion;
- Stage 5 finds a target-dependent causal state during rule processing.

But G18 contains a crucial ambiguity.

Its semantic previews both:
1. tell the model what the future target means;
2. substantively assert almost the same proposition as the later evidence.

Behavior confirms this: the later evidence's no-rule marginal collapses from ~32 to ~3.

Therefore the missing factor is:

> **target knowledge vs evidential instantiation.**

G22 exists only to separate those.

---

# 2. Scientific question

> **If a model knows exactly what a future evidence item will say, but that information
> is not itself evidence for the current judgment, can it pre-commit to excluding the
> later evidence?**

This question directly explains G0.

It is not:
- another semantic-specificity study;
- another instruction-order study;
- another source-scope study;
- a label-semantics study.

---

# 3. Competing hypotheses

## H-A — semantic target knowledge is sufficient

The exclusion mechanism needs a semantic representation of its target at policy
processing, but not an already-evidential representation.

Prediction:
`K` approaches `I`.

If supported:
deferred target-policy composition becomes the next main question.

## H-B — evidential instantiation is required

Exclusion is not reliably represented as a future gate. It becomes effective mainly
after the matching proposition is already instantiated in the judgment/evidence state.

Prediction:
`K ≈ U`, while `I` is substantially stronger.

If supported:
the next main question is passive gating vs active revision/cancellation.

## H-C — carrier/local semantics dominate

The behavior depends strongly on how the target state is encoded locally rather than on
the abstract knowledge/evidence distinction.

Prediction:
results vary with carrier semantics or fail the intended U/K/I ordering.

If supported:
G22 does not license a mainline claim; deconfound local semantic control first.

---

# 4. Required target states

## U — unresolved

The model has no semantic knowledge of the future target when exclusion is processed.

Conceptual order:

```
BACKGROUND
EXCLUSION POLICY(target ID)
ACTUAL EVIDENCE E(P)
QUESTION
```

## K — known but non-evidential

The model receives exact semantic information sufficient to identify what future
evidence E will contain, but that carrier is explicitly not case evidence.

Conceptual order:

```
BACKGROUND
NON-EVIDENTIAL TARGET SPECIFICATION(P)
EXCLUSION POLICY(target ID)
ACTUAL EVIDENCE E(P)
QUESTION
```

The specification must not:
- assert P as true evidence;
- itself request exclusion;
- imply P should be discounted;
- provide the target's decision weight;
- become a second policy;
- materially change the judgment on its own.

## I — evidentially instantiated

The same target proposition is presented before the rule as substantive case
information.

Conceptual order:

```
BACKGROUND
EVIDENTIAL ASSERTION(P)
EXCLUSION POLICY(target ID)
ACTUAL EVIDENCE E(P)
QUESTION
```

This is the conceptual analogue of G18 semantic preview conditions.

---

# 5. Exact minimum cell structure

For every state S in {U,K,I}:

### S-only

```
BACKGROUND
STATE(S)
QUESTION
```

Purpose:
measure direct effect of the target-state carrier.

### S-no-rule

```
BACKGROUND
STATE(S)
ACTUAL EVIDENCE
QUESTION
```

Purpose:
measure later-evidence marginal under that target state.

### S-exclude

```
BACKGROUND
STATE(S)
EXCLUSION POLICY
ACTUAL EVIDENCE
QUESTION
```

Purpose:
measure rule-specific removal beyond the state baseline.

Strongly preferred:
matched S-admit if prompt budget permits without making the factorial unwieldy.

---

# 6. Estimands

For evidence direction sign `s`:

```
Marginal_no_rule(S)
  = s * [Y(S-no-rule) - Y(S-only)]

Marginal_exclude(S)
  = s * [Y(S-exclude) - Y(S-only)]

ExclusionEffect(S)
  = Marginal_no_rule(S) - Marginal_exclude(S)
```

Use raw sign-aligned rating points.

Do not use a leverage-normalized ratio.

Primary scientific contrasts are not yet frozen, but the design audit should converge on
at least:

```
KnowledgeRescue = ExclusionEffect(K) - ExclusionEffect(U)

InstantiationIncrement = ExclusionEffect(I) - ExclusionEffect(K)
```

Both must be reported regardless of outcome.

---

# 7. The load-bearing neutrality gate

The experiment is invalid if K itself moves the judgment materially.

Before looking at rule effects, freeze a criterion for:

```
KDirect = s * [Y(K-only) - Y(U-only)]
```

Requirements:
- pooled effect near zero;
- no large systematic family-specific directional shift;
- high target-identification comprehension.

Exact numerical thresholds must be preregistered before generation.

If the chosen K carrier fails:
- do not inspect exclusion outcomes as evidence for H-A/H-B;
- redesign the carrier;
- refreeze before any new generation.

---

# 8. Carrier design audit

Candidate K carriers must be manually audited.

Possible forms:

### Retrieval manifest

A system-generated manifest states what payload a future document is configured to
return, explicitly distinguishing the manifest from evidence about the world.

Risk:
the model may still treat the payload description as evidence.

### Interface/schema metadata

A structured mapping specifies that D7 corresponds to a proposition template/content
slot without asserting the proposition as true.

Risk:
too abstract; may not supply full target semantics.

### Quoted future-record description

The prompt quotes the text that a future record would contain and explicitly says the
quotation describes the future record, not whether the quoted claim is true.

Risk:
quotation may still prime the judgment.

No carrier is accepted because it sounds non-evidential to humans. It must pass the
behavioral neutrality gate.

---

# 9. Required comprehension checks

Independent probes, never inserted into the decision trajectory unless separately
preregistered:

### Target identity
Which future evidence item does the policy govern?

### Target content
What proposition will that evidence item report?

### Evidential status
Does the pre-rule K carrier itself count as evidence for the judgment?

G22 is interesting only if the model can answer all three correctly at high rates.

---

# 10. Branch-specific follow-ups

## If H-A is supported

Register a separate follow-up, not silently extend G22.

Question:
> can the same known target be mapped to the policy after policy processing?

Required:
- same semantic catalog in all conditions;
- early vs late mapping only;
- high late-mapping comprehension;
- shared post-resolution checkpoint;
- neutral processing buffer;
- only then operator replay.

Mechanism:
critical-window / backpatch / frozen-backpatch style tests.

## If H-B is supported

Register a separate follow-up.

Question:
> is successful exclusion a passive gate or active evidence-state revision?

Required:
- target present + exclusion + no later repeated evidence;
- Admit/neutral controls;
- belief vs decision-use probes;
- causal state intervention from Stage 5 window.

## If H-C dominates

Do not force a G22 main claim.

Run the supporting D22-A routing deconfound only if needed.

---

# 11. What does not count as success

The following are insufficient:

- K improves exclusion but also strongly changes judgment by itself;
- rule replay helps without showing K itself is sufficient;
- semantic labels work better than nonce labels;
- a full evidential paraphrase works better than an identifier;
- a late target is correctly named but no clean target-state separation exists;
- one model exhibits a striking anomaly.

G22 succeeds scientifically only if it cleanly separates the target state.

---

# 12. Material quality requirements

Before preregistration:
- fresh skeletons or clearly justified reuse;
- no accidental lexical cue that marks K as unreliable/irrelevant;
- same proposition content matched across K/I/E;
- mixed evidence directions;
- sufficient baseline leverage;
- manually inspected prompts across every family;
- tokenizer-length/position audit where timing is later manipulated.

---

# 13. Model policy

Do not choose models by expected outcome.

A likely primary panel is the established five-model cross-vendor set:
- Qwen3-8B;
- Gemma-3-12B;
- Phi-4-mini;
- Qwen3.5-27B;
- Mistral-Small-24B.

This is not frozen.

No 70B/frontier sweep unless the final scientific question requires it.

---

# 14. Authorization checklist

Before generation all boxes must be checked:

- [ ] K carrier chosen
- [ ] manual non-evidential audit complete
- [ ] target/content/status probes designed
- [ ] neutrality threshold frozen
- [ ] leverage qualification frozen
- [ ] U/K/I cells frozen
- [ ] primary contrasts frozen
- [ ] H-A/H-B/H-C predictions written
- [ ] analyzer implemented
- [ ] dummy tests pass
- [ ] dedicated preregistration committed
- [ ] dataset/materials committed
- [ ] freeze tag created

Until then: **NO GENERATION.**
