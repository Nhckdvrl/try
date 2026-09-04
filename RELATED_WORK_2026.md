# Related work — prospective exclusion after scientific register v3

**Updated:** 2026-09-04.
**Current scientific question:** what target state must exist when an exclusion policy is
processed for future evidence to become causally inert?

This document is a positioning map, not a priority claim.

---

# 1. Generic instruction position / order

### Instruction Position Matters — ACL 2024 Findings
https://aclanthology.org/2024.findings-acl.693/

### Order Matters — ACL 2025 Findings
https://aclanthology.org/2025.findings-acl.646/

Occupied:
- later instructions can be easier;
- constraint order matters;
- recency/locality can affect instruction following.

Implication:
G0's sign alone is not the novelty.

Our target is a more specific dependency between:
- future-target state;
- exclusion-policy processing;
- later causal evidence use.

---

# 2. Constraint specificity / identify-then-ignore

### Chain-of-Specificity — COLING 2025
https://aclanthology.org/2025.coling-main.164/

### I3C — NAACL 2024 Main
https://aclanthology.org/2024.naacl-long.379/

Occupied:
- more specific constraints improve adherence;
- identify irrelevant conditions then explicitly ignore them.

Implication:
“semantic target information helps” cannot carry the paper.
ReGround remains cancelled.

---

# 3. Prospective memory / standing instructions

Recent prospective-memory and standing-instruction work establishes that models often
fail deferred constraints and long-lived instructions.

Relevant examples:
- prospective-memory / trigger benchmarks;
- long-horizon standing-instruction evaluations.

Our distinction must be stronger than:
> the model forgot the rule.

Existing policy probes and on-policy trajectories already show that rule access can be
correct while evidence still influences decisions.

The missing question is whether a future evidence-control relation is **causally
instantiated**, not merely remembered.

---

# 4. In-context forgetting / selective forgetting

Recent in-context-forgetting work studies instructions to forget or disregard
information that has already appeared.

That chronology is typically:

```
information → forgetting instruction → later query
```

Our original question is the prospective reverse:

```
exclusion policy → later information → judgment
```

Do not claim first selective forgetting.

The scientific gap is what changes when the policy arrives before the evidence state it
must control.

---

# 5. Generic binding

### Representational Analysis of Binding in Language Models — EMNLP 2024 Main
https://aclanthology.org/2024.emnlp-main.967/

### relational / cell-based binding — ACL 2026 Main
https://aclanthology.org/2026.acl-long.2194/

Occupied:
- entity-attribute binding;
- relational binding representations;
- causal editing of binding states.

Do not claim first binding.

If the G22 route later supports deferred composition, frame it specifically as:
> future evidence-policy target composition.

---

# 6. Eager instruction representations

### Patches of Nonlinearity — ACL 2026 Main
https://aclanthology.org/2026.acl-long.559/

This work is especially important for the current fork.

It shows that instruction-tuned models can form localized instruction
representations/digests before later query processing, with nonlinear causal effects and
circuit-selection behavior.

Therefore do not claim:
> LLMs eagerly process instructions.

The useful open consequence for our setting is:

> **What happens when an eagerly processed instruction requires target information that
> does not yet exist?**

Stage 5's target-dependent rule-time state makes this a concrete mechanistic question.

But the paper must still distinguish:
- target knowledge;
- evidential instantiation;
before asserting an eager-composition failure.

---

# 7. Dependency-order mechanisms

### Racing Thoughts — NAACL 2025 Main
https://aclanthology.org/2025.naacl-long.155/

Closest methodological neighbor.

Useful transferable ideas:
- critical processing windows;
- causal backpatching;
- frozen backpatching;
- separating “more computation” from “correct computation order.”

Do not merely borrow the phrase race condition.

If G22 later supports target knowledge sufficiency and a late-mapping failure, this
methodology can test whether:
- extra neutral processing time repairs control; or
- the exclusion operator must be reprocessed after target resolution.

---

# 8. Negative constraints / constructive semantic mechanisms

Recent mechanistic negation work suggests that negative language can involve
constructive representations rather than only passive suppression.

Use this as a methodological analogy only.

If G22 shows that evidential instantiation is required, a useful question becomes:

> does successful exclusion passively gate later evidence, or actively construct a
> target-specific revision/cancellation state?

Do not claim evidence exclusion is negation.

---

# 9. Source labels / semantic labels

Recent work on source-label effects and label-definition adherence shows that model
behavior can be strongly shaped by the pretrained semantics of labels, and that models
may resist arbitrary redefinitions.

This is directly relevant to the Stage 3B correction.

Existing Stage 3B has:
- semantic `[verified]/[unverified]` labels + policy;
- a no-policy control that removes labels.

Therefore it does not isolate standing-policy execution.

A supporting diagnostic may compare:
- semantic labels without policy;
- matching/reversed policies;
- nonce labels.

But label semantics cannot become the paper's novelty.

---

# 10. Provenance / source work

TROVE, GenProve, provenance-role work, source-label trust, and provenance-aware agent
memory occupy substantial space around:
- source attribution;
- provenance tracking;
- source-role separation;
- trust conditioned on source labels.

This is why G21 remains a future side branch rather than current mainline.

---

# 11. Policy / guideline systems

Recent guideline-following and standing-policy work increasingly externalizes or
structures rule applicability rather than leaving it implicit in free-form reasoning.

This supports the final systems motivation:

> future evidence policies may need persistent structured state rather than prose alone.

But the paper first needs a behavioral law explaining why G0 fails.

---

# 12. Exact current novelty boundary

Do not claim:
- first instruction-order effect;
- first prospective-memory failure;
- first forgetting benchmark;
- first binding mechanism;
- first semantic-label effect;
- first policy failure;
- first provenance-aware control;
- first result that specificity helps.

The currently unoccupied scientific question we are trying to isolate is narrower:

> **When a policy must make future evidence causally inert, is exact semantic knowledge
> of that future target sufficient, or does the target proposition need to be already
> instantiated as evidence before exclusion becomes effective?**

Only if semantic knowledge is sufficient do we proceed to the next dependency:

> **Can a target-policy relation be composed after the policy has already been
> processed?**

Targeted search has not identified a paper directly isolating this exact two-stage
factorization. Treat that as positioning, not proof of priority.

---

# 13. Historical branches

### Target Addressability
Confirmed diagnostic, retired novelty.

### G20 deferred composition
Live conditional hypothesis, not currently authorized.

### G21 source/proposition scope
Future-paper candidate only.

### ReGround G19
Cancelled before generation.
