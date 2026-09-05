> **2026-09-06 supersession notice:** this file began as the related-work map for
> the G22/prospective-exclusion mainline. That framing is historical. Current research
> priority is governed by [MAINLINE_AUDIT_2026-09-06_V8.md](MAINLINE_AUDIT_2026-09-06_V8.md).
> G22 is killed and no new generation is authorized. The V8 addendum at the end records
> the current novelty threats for simple-data RQ search.
>
# Related work — prospective exclusion after scientific register v3

**Updated:** 2026-09-04.
**Current scientific question:** what target state must exist when an exclusion policy is
processed for future evidence to become causally inert?  
**Latest mainline audit:** [MAINLINE_AUDIT_2026-09-05_V4.md](MAINLINE_AUDIT_2026-09-05_V4.md)

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

The novelty role is outcome-dependent. If semantic knowledge is sufficient, that fact
alone is not the intended headline; we proceed to the stronger dependency:

> **Can a target-policy relation be composed after the policy has already been
> processed, even when the late target is correctly understood?**

If semantic knowledge is neutral and correctly understood but insufficient while an
already-instantiated evidence state succeeds, the stronger mainline becomes:

> **Natural-language exclusion behaves like a transformation of an existing evidence
> state rather than a standing future gate.**

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


---

# V8 addendum — current novelty-threat map (2026-09-06)

This addendum does **not** revive the old prospective-exclusion mainline.

## A. Publicness / common-knowledge intersection

### MindGames — EMNLP Findings 2023
Occupied:
- controlled dynamic epistemic / S5 reasoning in LMs;
- public announcements in generated premises;
- higher-order belief hypotheses.

Kills:
- first public-announcement benchmark;
- first recursive epistemic benchmark;
- generic "LLMs struggle with higher-order knowledge."

### Logical Reasoning in Evolving Scenarios — Knowledge-Based Systems 2026
Occupied:
- Muddy Children and Cheryl's Birthday;
- public announcements;
- recursive knowledge updating;
- 2,784 difficulty-controlled instances;
- answer prediction + role playing;
- failures attributed to recursive perspective-taking / logical implications.

Kills:
- "Can LLMs solve common-knowledge puzzles?"
- benchmark-only modernization of Muddy Children.

### OmniToM — 2026
Occupied:
- explicit belief modeling;
- order 0–3;
- Private / Shared / Public knowledge-access labels.

Kills:
- "LLMs cannot distinguish public and private information."
- "knowledge access is a new ToM factor."

### SimpleToM — ICLR 2026
Occupied:
- explicit mental-state inference vs applied ToM;
- behavior prediction / judgment dissociation.

Kills:
- generic recognition→application novelty.

### Human common-knowledge work — PNAS 2019 / PNAS 2026
Establishes the theoretical distinction:
- finite recursive mentalizing is capacity limited;
- public salience can license implicit arbitrary-depth common knowledge;
- humans can also over-extrapolate finite/private knowledge.

Implication:
the human distinction itself is not novel. A surviving LLM paper needs a new
LLM-specific **publicness law**, not "models also show the human effect."

### Surviving gap, still HIGH-RISK
Current search has not found a modern LLM paper whose load-bearing manipulation is:

> matched first-order factual knowledge + finite private/reciprocal nesting vs public
> joint observability, specifically to test whether publicness recruits a computational
> shortcut to recursive closure distinct from finite ToM.

This is an **intersection gap**, not a clean empty field.

## B. Sampling / observation-process conditioning — killed

Direct threats:
- CROWN-QA / *When Absence Is Evidence* (2026): completeness-sensitive negative
  reasoning;
- *Hypothesis generation and updating in LLMs* (2026): explicit sampling assumptions /
  strong-sampling bias;
- BayesBench / Bayesian-teaching / QUITE / diagnostic evidence updating.

Verdict: KILL as paper identity.

## C. Additional killed broad RQs

Killed before generation:
- source reliability / undercutting;
- conflict vs ignorance;
- value of information / ask-before-act;
- disjunctive / set-valued uncertainty;
- joint intention / joint commitment;
- pluralistic ignorance;
- informational cascades / herding;
- screening-off / Markov independence;
- reversible vs irreversible action / preserving optionality.

## D. Linguistic substrates not promoted

### Free-choice permission
No exact LLM free-choice paper located in current search, but deontic/modal reasoning is
crowded. Keep SECONDARY SEARCH ONLY.

### Homogeneity / truth-value gaps
No exact LLM homogeneity paper located in current search. This is **not** enough for a
candidate. Presupposition/pragmatics evaluation and reasoning-vs-human-semantics gaps
are already active 2026 topics. Require a larger new LLM-specific law before any pilot.
