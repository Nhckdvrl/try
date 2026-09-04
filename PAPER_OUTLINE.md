# Paper outline — deferred-control composition version

**Updated:** 2026-09-04 after the second mainline audit.
**Status:** G20 v3 pending; G21 removed from the paper center.

## Working title candidates

Primary:
> **Can Language Models Commit to Ignore Future Evidence?**

Alternative:
> **When Exclusion Comes Too Early: Deferred Control Composition in Language Models**

Technical:
> **Non-Commutative Control Composition in Prospective Evidence Exclusion**

Avoid:
- Target Addressability in the title;
- source/provenance scope as the paper identity;
- generic “instruction position matters” language.

## Abstract structure

1. Policies often precede the evidence they govern.
2. Broad result: exclusion-before-evidence is systematically weaker than identical
   exclusion-after-evidence across 12 instruct + 2 diffusion models / five families.
3. Policy access alone does not explain the effect in at least some models; exact
   prospective arithmetic weighting can nevertheless succeed.
4. G18 factorization: making target semantics available before the rule restores much
   of prospective exclusion even though the actual evidence remains later.
5. **If G20 v3 passes:** late target resolution after the rule does not reconstruct the
   same exclusion control despite correct target comprehension; replaying the exclusion
   operator selectively restores it.
6. **If checkpoint mechanism passes:** after both target and rule are available,
   target-first and rule-first contexts still carry different causal control states.
7. Implication: current LLMs behave more like eager target-conditioned control compilers
   than reliable deferred policy executors.

Do not write “semantic target descriptions improve exclusion” as the novelty.

---

# 1. Introduction

Opening:

> Policies often exist before the objects they govern. A reliable model should be able
> to store an exclusion rule, resolve its target later, and apply the rule when that
> target appears.

Natural examples:
- system policy before retrieval;
- source/evidence rule before testimony arrives;
- tool governance before a tool result exists.

Question:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

The surprising result is not just that prospective exclusion is imperfect. It is that
the **same rule** works substantially better after the target has appeared.

Core idea:

> retrospective and prospective conditions reverse the order of two computations:
> target representation and exclusion.

Contribution list, conditional on G20:
1. broad prospective exclusion reversal;
2. factorization showing target-before-rule semantics restores exclusion;
3. novelty-bearing deferred-composition failure with selective rule replay;
4. causal target-conditioned control state, strengthened at a shared post-resolution
   checkpoint.

---

# 2. Experimental setup

## 2.1 G0 broad set
144 frozen items / five families.

Conditions:
- Base
- Admit-before / after
- Exclude-before / after

## 2.2 G18 fresh factorization set
100 items / 30 skeletons / three families / five models.

Six pre-rule target representations with per-condition no-rule baselines.

## 2.3 G20 v3 fresh deferred-composition set
Planned:
- 120 items
- 36 skeletons
- three families
- semantic target preview P
- length-matched unrelated block U
- exclusion operator X
- neutral shared checkpoint C
- later evidence E

Raw sign-aligned rating points for G18/G20.

---

# 3. A paradox of prospective exclusion

**Figure 1.**

Show:
- 12 instruct models: Exclude-before vs Exclude-after
- Admit control
- optional diffusion inset

Claim:

> **Models are worse at pre-committing to exclusion than at excluding the same evidence
> after seeing it.**

Compact supporting paragraph:
- declarative policy probe;
- on-policy Qwen/Gemma dissociation;
- wording/distance controls;
- masked diffusion replication.

Boundary:
explicit arithmetic future weighting can succeed exactly, so the failure is not generic
future-rule execution.

---

# 4. Factorizing the reversal: target semantics before the rule

Retrospective:

```
target → EXCLUDE
```

Prospective:

```
EXCLUDE → target
```

G18 changes prospective control to:

```
target-semantic preview → EXCLUDE → later target evidence
```

Report:
- Delta_semantic +8.91 [7.15,10.76], 5/5 positive;
- para-empty +12.85 [10.32,15.42];
- lexical wrong / unrelated controls;
- deconfounded no-rule preview baselines.

Interpretation:

> **Target semantics available at exclusion processing materially change later causal
> evidence suppression.**

Do not call this the final novelty.

Stage 4 can appear here or in appendix:
control follows proposition across D7→D9 more reliably than arbitrary identifier alone,
supporting a content-conditioned target representation.

---

# 5. Deferred Control Composition

**Figure 2 — novelty-bearing if confirmed.**

## 5.1 Order factor

```
TARGET-FIRST:
P → X → U → C → E → question

RULE-FIRST:
U → X → P → C → E → question
```

At C, both arms have all required information.

Primary claim if confirmed:

> **Late target resolution does not reconstruct the same exclusion control: target-first
> and rule-first histories remain behaviorally different even after both target and
> rule are available.**

## 5.2 Comprehension

Full-context RULE-FIRST probe:
which later proposition/item does the earlier exclusion rule apply to?

Need high accuracy.

A trajectory-level resolved-target statement is preferable if it can be implemented
cleanly.

## 5.3 Rule replay

```
RULE-FIRST + replay X
TARGET-FIRST + replay X
```

Critical result:
replaying X selectively repairs RULE-FIRST.

Add target-replay control if feasible:
repeating P should not explain the same rescue.

## 5.4 Positive deferred-composition controls

At least two:
- Admit / use-select;
- arithmetic weighting;
- optional routing/select.

These show the model can combine an earlier unresolved rule with a later target in other
operations.

## 5.5 Interpretation

If the pattern qualifies:

> **LLM exclusion behaves like eager target-conditioned compilation rather than a
> deferred predicate that is reliably evaluated when its target later appears.**

This is the central non-obvious computation.

---

# 6. Policy knowledge is not control composition

Keep concise.

Existing:
- separate policy probe near ceiling;
- Qwen/Gemma can state 0% on-policy while still leaking;
- teacher-forced 0% does not fully restore them;
- Phi is a counterexample to universalizing the dissociation.

G20 extension:

> the model can correctly resolve a late target while still failing to compose it with
> the earlier exclusion operator.

This section connects declarative understanding to causal enforcement without claiming
all models behave identically.

---

# 7. Mechanism

**Figure 3.**

## 7.1 Existing Stage 5

Matched chronology:

```
FAILURE: unrelated preview → X → E
SUCCESS: target paraphrase → X → E
```

Qwen:
L14–18 / 36.

Mistral:
L12–16 / 40.

Claim already licensed:

> **A target-dependent control state forms during exclusion processing and causally
> changes later evidence suppression.**

No universal steering direction claim.

## 7.2 New post-resolution checkpoint

At C in G20:

- both TARGET-FIRST and RULE-FIRST have target + rule available;
- positions are matched;
- composition history differs.

Tests:
- target resolution correct in both;
- C-state interchange target-first → rule-first;
- reverse interchange;
- matched Admit/control patching;
- after rule replay, does rule-first C become more like the target-first control state?

Strong claim if confirmed:

> **The order-dependent control state persists after target resolution and is causally
> responsible for later suppression.**

This is the anti-causal-mask mechanism.

---

# 8. Discussion

## 8.1 Beyond instruction position

Prior work moves instructions and measures compliance.

Our variable is the order of:
- target semantic resolution;
- exclusion-operator processing.

The strongest test occurs after both are available.

## 8.2 Beyond prospective memory

Prospective-memory benchmarks ask whether a latent instruction is remembered and
triggered.

Here the rule can be accessible and the target can be recognized, yet the required
causal non-use relation is not composed.

## 8.3 Beyond in-context forgetting

ICF-Bench asks models to forget information that has already appeared.

Our original asymmetry is the opposite direction:
can the model pre-commit before the governed evidence exists?

## 8.4 Beyond generic binding

Entity/relational binding work studies which entity is associated with which attribute.

Our object is an operator-target relation:
can an exclusion operator remain deferred until its semantic target is instantiated?

## 8.5 Architectural implication

If the post-resolution checkpoint is causal, decoder masking is not the full
explanation: downstream states have access to all inputs but preserve the wrong
composition history.

Diffusion replication would strengthen this further.

---

# 9. Related work

Organize around:
1. instruction position and constraint order;
2. prospective memory;
3. in-context forgetting / selective context control;
4. negative constraints and identify-then-ignore;
5. entity/relational binding;
6. instruction states and causal contextualization;
7. provenance/source work as secondary relevance.

Closest conceptual paper:
**Racing Thoughts**.

Positioning sentence:

> Prior work shows that instruction order matters and that contextual computations can
> exhibit dependency-order failures. We study a distinct control dependency: whether an
> exclusion operator can be processed before its evidential target is resolved and then
> reliably composed with that target later.

---

# 10. Method opening

Do not revive ReGround.

The scientific result should instead motivate:

> **order-invariant deferred policy–target composition.**

Future directions:
- factorized persistent policy operator + target instance;
- temporal-permutation invariance objective;
- typed deferred-control state instantiated at evidence arrival;
- external reference monitor;
- activation/routing mechanism that reconstructs the correct post-resolution control
  state.

---

# 11. Limitations

Before G20:
- G20 is pending;
- controlled authored tasks;
- on-policy access/enforcement dissociation is heterogeneous;
- current mechanism is two architectures;
- G18 oversuppression is descriptive and not fully explained.

After G20:
update based on actual results.

---

# Main figure hierarchy

Figure 1 — broad prospective exclusion reversal

Figure 2 — G20 target-first vs rule-first + selective rule replay

Figure 3 — existing rule-state mechanism + post-resolution checkpoint interchange

Optional compact bridge panel — G18 semantic factorization

No G21 main figure.

---

# Appendix

- full G0 model×family tables
- wording / distance / delay
- arithmetic / transform boundaries
- full G18 factorial and redundancy decomposition
- Stage 3D content×identity
- Stage 3E relation matrix
- on-policy trajectories
- Stage 4 D7→D9
- masked diffusion details
- failed shared steering direction
- G21 design retained as future-work provenance
- cancelled ReGround G19 design as repository provenance

The main text must read as one question becoming progressively more mechanistic, not as
an experiment ledger.
