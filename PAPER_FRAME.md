# Paper frame — deferred-control composition candidate

**Updated:** 2026-09-04 after the second mainline audit.
**Status:** G0/G18/Stage4/Stage5 complete; G20 v3 is the only current
novelty-bearing experiment. G21 has been downgraded from the paper center.

Read:
- [MAINLINE_AUDIT_2026-09-04_V2.md](MAINLINE_AUDIT_2026-09-04_V2.md)
- [NEXT_EXPERIMENTS_POST_RESET.md](NEXT_EXPERIMENTS_POST_RESET.md)

## 1. Natural question

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

This remains the paper's scientific identity.

Real systems frequently have:
- a policy before a retrieval result;
- an exclusion rule before testimony arrives;
- a system rule before a tool output exists.

The paper should not drift into a general provenance or source-scope paper.

## 2. Stable entry phenomenon

Across 12 instruction-tuned models, two masked diffusion LMs, four vendors, and five
task families, the same exclusion rule is substantially weaker when stated before the
evidence than after it. The matched Admit rule does not show the same order effect.

This remains Figure 1.

Headline:

> **Language models are systematically worse at pre-committing to evidence exclusion
> than at excluding the same evidence after it appears.**

## 3. The key factorization: G0 changes composition order

Retrospective G0:

```
target evidence → EXCLUDE rule → judgment
```

Prospective G0:

```
EXCLUDE rule → target evidence → judgment
```

This suggests a more specific question than generic instruction position:

> **Does exclusion depend on whether target semantics exist before the exclusion
> operator is processed?**

That question grows directly from the original reversal.

## 4. G18 is diagnostic evidence for the factorization

G18 prospectively confirms that pre-rule target semantics change exclusion:

Delta_semantic = **+8.91 [+7.15,+10.76]** rating points, positive in 5/5 models.

The important reading is not:

> more specific target information helps.

It is:

```
target semantics → EXCLUDE rule → later evidence
```

restores much of the suppression even though the actual evidence used by the decision
still arrives after the rule.

Therefore G18 supports:

> what matters may be the order in which target semantics and the exclusion operator
> are composed.

The below-preview-baseline oversuppression remains an informative clue that successful
control is content-level rather than a literal deletion of one later occurrence, but it
is not being expanded into a separate scope-collapse contribution.

## 5. Stage 4 identifies what the target representation is

The system→tool D7→D9 counterfactual shows that proposition-targeted suppression can
follow the same content across an identifier change, while identifier-specific protection
does not.

This is diagnostic evidence that the effective target representation is substantially
semantic/content-conditioned.

Do not write:
> semantic policies are always better.

Write:
> **the control state is strongly conditioned on propositional content rather than
> being a purely symbolic identifier rule.**

## 6. Candidate central mechanism — eager target-conditioned control compilation

The current unified hypothesis is:

> **When processing an exclusion rule, the model constructs a target-conditioned
> control state from whatever target representation is already available. If the target
> has not yet been semantically instantiated, the rule remains under-composed; later
> target recognition does not reliably reconstruct the same control state.**

Equivalent compact formulation:

> **Prospective exclusion is non-commutative: target → EXCLUDE works better than
> EXCLUDE → target.**

This explains:
- G0 timing reversal;
- G18 pre-rule semantic rescue;
- Stage 4 content-conditioned transfer;
- Stage 5 target-dependent rule state;
- arithmetic success as a boundary showing deferred control is not generically
  impossible.

This remains a hypothesis until G20 v3 tests late target resolution directly.

## 7. Candidate Contribution 2 — Deferred Control Composition

**First priority, pending G20 v3.**

Core behavioral conditions:

```
TARGET-FIRST:
P → EXCLUDE → U → CHECKPOINT → EVIDENCE → QUESTION

RULE-FIRST:
U → EXCLUDE → P → CHECKPOINT → EVIDENCE → QUESTION
```

By the shared CHECKPOINT, both arms have seen the same target semantics, rule, and neutral
block.

This is crucial: the scientific claim is not that an earlier rule token cannot attend
future target tokens. The question is whether the model reconstructs the same control
once both operands are available downstream.

### Claim if confirmed

> **Exclusion is history-dependent even after target resolution: models can correctly
> identify a target revealed after the rule yet still fail to compose that target with
> the earlier exclusion operator.**

### Rule replay

If the same exclusion rule is replayed after target resolution:

```
U → EXCLUDE → P → EXCLUDE → CHECKPOINT → EVIDENCE
```

it should selectively repair RULE-FIRST.

A matched TARGET-FIRST replay condition is mandatory to separate targeted recomposition
from generic repetition/recency.

A target-replay control is desirable:
if repeating P does little while replaying EXCLUDE repairs the failure, the missing
operation is not simply target salience.

### Positive controls

At least two matched deferred-composition controls:
- Admit / use-select routing;
- explicit arithmetic weighting.

The result is strongest if those operations late-compose successfully while semantic
exclusion does not.

## 8. Mechanism

Existing Stage 5:

- matched success/failure chronology;
- target-dependent rule-span state;
- Qwen3-8B mid-layer window;
- Mistral-Small-24B replication;
- causal interchange changes later suppression;
- no universal shared steering direction.

This already supports:

> **rule processing is a critical computational event.**

The new mechanism should move downstream to a shared post-resolution checkpoint.

At that checkpoint:
- both orders have all relevant information;
- token position can be matched;
- only composition history differs.

Ideal result:

> TARGET-FIRST and RULE-FIRST remain causally distinct after target resolution, and
> interchanging the checkpoint state changes later evidence suppression.

That would directly establish an order-dependent control state rather than an
architectural causal-mask triviality.

## 9. Policy access vs enforcement

Separate policy probes often recover the intended zero weight.

The stronger dissociation is model-heterogeneous:
- Qwen3-8B / Gemma-3-12B can state zero and still use prospective evidence;
- Phi-4-mini does not show the same strong dissociation.

G20 should extend this distinction:

> **late target resolution can be declaratively correct without becoming effective
> causal control.**

This is more important than claiming perfect policy memory.

## 10. G21 status

Source–Proposition Scope Entanglement is **downgraded**.

It is potentially interesting, but it asks whether successful semantic control preserves
source scope. That does not explain why prospective exclusion is weaker in G0.

Therefore:
- no main contribution;
- no main figure;
- no current generation budget;
- retain as possible future work / secondary consequence.

## 11. Literature-facing positioning

Occupied:
- instruction position / constraint order;
- prospective memory;
- in-context forgetting of already-seen information;
- identify-then-ignore;
- constraint specificity;
- entity / relational binding;
- localized instruction states;
- source provenance.

The exact candidate dependency is:

> **whether an exclusion operator can be deferred and later composed with a target that
> becomes semantically resolved only after the operator was first processed.**

Closest conceptual comparator:
Racing Thoughts — dependency ordering can matter even when all information is eventually
available.

Our new dependency is control-specific:
target semantics must be composed with an exclusion operator, and that composition may
remain history-dependent downstream.

## 12. Candidate final arc

Can models pre-commit what future evidence should not matter?
    ↓
Broadly, exclusion-before-evidence is weaker than exclusion-after-evidence.
    ↓
G0 is a target/operator order reversal.
    ↓
G18 shows that restoring target semantics before the rule restores control.
    ↓
G20 v3 asks whether late target resolution reconstructs the same control after both
objects are available.
    ↓
If not, rule replay selectively restores it: exclusion behaves like eager
target-conditioned compilation rather than deferred execution.
    ↓
Stage 5 + post-resolution checkpoint patching identify the causal state that carries the
order dependence.
    ↓
Method problem: build order-invariant deferred policy–target composition.

## 13. Programme status

ReGround G19 remains cancelled before generation.

Active work:
1. build/audit/freeze **G20 v3 Deferred Control Composition**;
2. run no G21 mainline experiment;
3. run the post-resolution mechanism only after behavioral qualification;
4. add no breadth for its own sake.
