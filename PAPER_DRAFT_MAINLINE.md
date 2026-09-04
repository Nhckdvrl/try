# Paper mainline draft — deferred-control composition version

**Status:** provisional mother draft after the 2026-09-04 mainline audit.
**Target:** Outstanding-shaped organisation; NAACL Main as realistic acceptance target.

The paper remains about one question:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

The previous center—“semantic target information improves exclusion”—was retired as
too obvious. G21 source-scope collapse has also been downgraded because it does not
naturally explain the original prospective/retrospective reversal.

The active candidate explanation is:

> **LLMs construct a target-conditioned exclusion state when the rule is processed,
> rather than reliably storing a deferred exclusion operator that can be composed with
> a target later.**

Equivalent shorthand:

> **target → EXCLUDE works better than EXCLUDE → target.**

The new G20 v3 must earn this claim.

---

# 0. Candidate abstract

> Policies often precede the evidence they are meant to govern. We find that language
> models are systematically worse at excluding evidence when an exclusion rule is
> stated before the evidence than after it, across twelve instruction-tuned models, two
> masked diffusion language models, and five task families. The asymmetry is not a
> generic inability to obey future rules: models can execute explicit future arithmetic
> weighting exactly, and in some models explicit policy access can remain correct even
> while excluded evidence still influences the decision. A semantic factorization shows
> that prospective exclusion becomes much stronger when the target proposition is
> instantiated before the rule, even though the actual governed evidence still arrives
> later. This suggests that the relevant computation is not generic instruction
> position but the order in which target semantics and exclusion control are composed.
> We therefore test whether a target revealed after the rule can be correctly resolved
> yet fail to reconstruct the same causal exclusion state, and whether reprocessing the
> exclusion operator after target resolution restores control. Existing causal
> interchange experiments localize a target-dependent mid-network state during rule
> processing; a post-resolution checkpoint test asks whether this history dependence
> persists after both target and rule are available. Together, the results test whether
> current LLMs behave as eager target-conditioned control compilers rather than reliable
> executors of deferred evidence policies.

The G20-dependent sentences enter the final abstract only if confirmed.

---

# 1. The natural problem

A policy can exist before the object it governs.

Examples:
- a system policy is written before retrieval;
- a source may be ruled inadmissible before its testimony is fetched;
- an agent may be told that a future tool result must not affect a decision.

A normal symbolic system can represent the policy now and evaluate it once the target
appears.

The question is whether an LLM can do the same.

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

The simplest test compares the same exclusion instruction in two orders.

Retrospective:
```
evidence → exclusion rule → judgment
```

Prospective:
```
exclusion rule → evidence → judgment
```

If exclusion were represented as a persistent executable rule, those orders should not
produce a large systematic difference once all information is available for the final
decision.

They do.

---

# 2. Established phenomenon — prospective exclusion fails

## 2.1 Dataset

G0 uses 144 frozen items across five families:
- legal judgment;
- evidence inference;
- ranking / selection;
- outcome evaluation;
- numeric aggregation.

Every item provides:
- Base;
- Admit-before / Admit-after;
- Exclude-before / Exclude-after.

The evidence and rule content are matched across timing conditions.

## 2.2 Model breadth

- 12 instruction-tuned checkpoints;
- four vendors;
- roughly 3.8B–32B parameters;
- two masked diffusion LMs.

## 2.3 Result

The exclusion timing gap has the same sign in all 12 instruct models; 10/12 confidence
intervals exclude zero.

Representative REI:
- Phi-4-mini: pre +0.50 vs post +0.24
- Gemma-3-12B: +0.43 vs +0.07
- Qwen2.5-32B: +0.30 vs +0.00
- Mistral-Small-24B: +0.19 vs −0.03
- Qwen3-8B: +0.45 vs +0.12
- Qwen3-14B: +0.49 vs −0.07
- Qwen3.5-27B: −0.05 vs −0.29

Matched Admit order is approximately flat.

### Headline

> **Language models are systematically worse at pre-committing to evidence exclusion
> than at excluding the same evidence after it has appeared.**

This is Figure 1.

---

# 3. The problem is not simply forgetting the rule

A separate declarative probe recovers the intended zero-weight policy at or near
ceiling.

The stronger on-policy result is model-heterogeneous:
- Qwen3-8B and Gemma-3-12B can spontaneously state zero weight while prospective
  evidence still affects the answer;
- Phi-4-mini largely mediates the behavior through whether zero is stated.

Teacher-forcing the correct zero-weight state does not fully restore Qwen/Gemma
prospective suppression.

Supporting controls:
- ~1,000-token rule-to-evidence delay does not monotonically worsen the effect;
- eight rule wordings preserve the gap;
- masked diffusion models preserve the broad asymmetry.

### Conclusion

> **Policy accessibility and policy enforcement can separate.**

Do not universalize the strongest dissociation.

---

# 4. The failure is not generic future-rule execution

Stage 3C introduces an explicit arithmetic task:

```
answer = base + w * delta
```

When models are qualified on intermediate weights, four of five tested models execute
prospective `w=0` exactly.

Thus:

> **Models can prospectively apply an explicit future-directed zero operation when the
> target contribution is symbolically specified.**

The difficult case is semantic evidence whose contribution must be inferred and then
made causally inert.

This boundary becomes crucial for the new story: deferred composition is possible in
principle, but semantic exclusion appears to use a different control computation.

---

# 5. G0 factorized: target semantics before exclusion

G0 reverses the order of:
1. target representation;
2. exclusion rule.

Retrospective:
`target → EXCLUDE`

Prospective:
`EXCLUDE → target`

Stage 3C/3D/G18 ask whether the actual evidence itself must be early.

It does not.

A semantic preview can appear before the rule while the actual evidence used by the
decision remains after it:

```
target-semantic preview → EXCLUDE → later evidence → judgment
```

## 5.1 G18

G18 uses:
- 100 fresh items;
- 30 fresh skeletons;
- three families;
- five checkpoints / four vendors;
- 9,000 generations;
- six target representations with their own no-rule baselines;
- raw sign-aligned rating points.

Pooled ExclusionEffect:
- entail: **31.16 [27.99,34.40]**
- paraphrase: **30.93 [28.19,33.66]**
- identifier: 26.27 [23.65,28.96]
- unrelated: 22.06 [19.16,24.97]
- none: 21.84 [19.21,24.66]
- lexical-overlap / wrong proposition: 18.08 [15.71,20.57]

Frozen semantic contrast:

> **+8.91 [7.15,10.76]**, positive in 5/5 models.

This result is not itself the novelty.

The scientific interpretation is:

> **Prospective exclusion becomes much stronger when a sufficiently specific target
> proposition already exists when the exclusion rule is processed.**

Lexical overlap and vague gist are not enough.

## 5.2 Why this explains more of G0 than generic position

The actual governed evidence is still after the rule.

Therefore the important temporal variable is not simply:
> is the evidence block before or after the instruction?

It is:
> **does the model already have a semantic representation of what is to be excluded
> when it processes the exclusion operator?**

That is the direct bridge from G0 to mechanism.

## 5.3 Oversuppression as a clue, not a new paper

Under paraphrase preview:
- marg(no-rule) is only about +3 points;
- marg(exclude) is about −28 points relative to preview-only baseline.

This suggests successful exclusion is not implemented as a perfectly local deletion of
one repeated evidence occurrence.

A safe interpretation:

> the successful control state is content-level and can be stronger than merely
> cancelling the later block's marginal contribution.

Do not turn this anomaly into the separate G21 source-scope story.

---

# 6. Stage 4: the effective target is content-conditioned

In a system→tool setting:
- identifier-only policy can work on its named D7 in some models;
- when the same proposition moves D7→D9, ID-specific protection does not follow;
- proposition-targeted suppression does follow the content.

This does not imply that semantic policy is always better.

Its role in the paper is narrower:

> **The effective exclusion target is substantially tied to propositional content, not
> solely to a symbolic identifier.**

That is exactly the kind of target representation G18 places before the rule.

---

# 7. Candidate central law — deferred control composition

The existing results motivate:

> **When an exclusion rule is processed, the model constructs a target-conditioned
> control state from whatever target representation is already available. If the target
> is unresolved, later target recognition may not reconstruct the same state.**

This is an eager-composition hypothesis.

It predicts a non-obvious asymmetry:

> target semantics arriving after the rule but before the governed evidence should be
> understood, yet exclusion may remain weaker until the exclusion operator is processed
> again.

G20 v3 tests this directly.

---

# 8. G20 v3 — Non-Commutative Exclusion

## 8.1 Core order

Fresh materials:
- semantic target preview P;
- length-matched unrelated U;
- exclusion rule X;
- neutral shared checkpoint C;
- later evidence E.

Conditions:

```
TARGET-FIRST:
P → X → U → C → E → question

RULE-FIRST:
U → X → P → C → E → question
```

By C, both arms have seen:
- P;
- X;
- U.

Thus both have all information required to construct the intended control state.

This is the key redesign against the causal-mask objection.

## 8.2 Mandatory comprehension

On the full RULE-FIRST context, the model must correctly identify which later target the
earlier exclusion rule applies to.

A stronger same-trajectory resolved-target statement should be used if it can be
implemented without creating a new confound.

If comprehension is low, the experiment does not support deferred-composition failure.

## 8.3 Behavior

Primary:

```
CompositionOrderGap = EE(TARGET-FIRST) - EE(RULE-FIRST)
```

The novelty-bearing result is:

> **TARGET-FIRST remains stronger even though RULE-FIRST has correctly resolved the
> target before evidence and before the final decision.**

That is a much stronger statement than “later instructions work better.”

## 8.4 Reprocessing the operator

```
RULE-FIRST + replay:
U → X → P → X → C → E

TARGET-FIRST + replay:
P → X → U → X → C → E
```

Critical interaction:

> the second X should preferentially repair RULE-FIRST.

This tests whether the missing computation is reapplication of exclusion after the
target becomes available.

## 8.5 Target replay

Desirable control:

```
U → X → P → P → C → E
```

If target replay produces much less rescue than rule replay, simple target salience is
not enough.

## 8.6 Positive operations

At least two matched deferred-composition controls:
- Admit / use-select;
- arithmetic weighting;
- optional routing/select.

The strongest pattern is:

> the same model can late-compose an earlier rule with a later target for positive or
> explicit operations, but semantic nullification remains history-dependent.

## 8.7 Claim if confirmed

> **Exclusion is non-commutative in context: models can know a late-resolved target yet
> fail to compose it with an earlier exclusion operator. Reprocessing the operator after
> target resolution reconstructs control.**

This is the main novelty-bearing behavioral result.

---

# 9. Causal mechanism

## 9.1 Existing Stage 5

Matched chronology:

```
FAILURE:
unrelated preview → X → evidence → answer

SUCCESS:
target paraphrase → X → evidence → answer
```

The evidence is after X in both arms.

Qwen3-8B:
- behavioral gap +13.2 [8.6,18.1];
- causal rule-state window L14–18 / 36;
- L14 break +13.3 [8.1,18.9];
- rescue about −3.6 [−5.9,−1.4].

Mistral-Small-24B:
- behavioral gap +18.2 [10.0,26.9];
- causal window L12–16 / 40;
- break +18.3 [12.6,24.5];
- rescue −16.1 [−24.2,−9.0].

Invariant:

> **A target-dependent mid-network rule state forms before later evidence is processed,
> and causal interchange changes later suppression.**

Do not claim:
- a universal steering vector;
- a TARGET_FOUND neuron;
- a universal rescue/break asymmetry.

## 9.2 Why existing Stage 5 is not yet the final mechanism

The earlier rule span in RULE-FIRST cannot see future P in a decoder.

Therefore the new causal test should occur at C, after both P and X are available.

## 9.3 Post-resolution checkpoint

At C:
- target mapping should be correct in both orders;
- token positions are matched;
- all operands are available.

Causal tests:
1. TARGET-FIRST C → RULE-FIRST recipient;
2. RULE-FIRST C → TARGET-FIRST recipient;
3. identical Admit/control interchange;
4. compare RULE-FIRST before and after rule replay.

Strong result:

> **The two histories do not converge to the same control state after target
> resolution; checkpoint interchange changes later evidence suppression.**

This would connect the broad reversal to a causal downstream state without relying on
the trivial earlier-token causal mask.

---

# 10. Higher-level scientific statement

If G20 v3 and checkpoint mechanism pass, the paper can say:

> **LLMs do not reliably treat exclusion policies as deferred predicates over future
> evidence. Effective exclusion is constructed in a target-conditioned manner, making
> control depend on whether the target representation exists when exclusion is
> processed.**

That is broader than a prompt trick and narrower than generic binding.

A memorable shorthand:

> **LLMs can remember the rule and recognize the target, yet still fail to compose the
> two in time.**

---

# 11. Related-work boundary

Do not claim novelty from:
- instruction position;
- constraint order;
- prospective memory;
- in-context forgetting;
- generic entity binding;
- instruction-state localization;
- identify-then-ignore;
- source provenance;
- negative output constraints.

Closest conceptual prior:
Racing Thoughts.

The distinct dependency here is:
> **deferred composition of an exclusion operator with a future semantic evidence
> target.**

ICF-Bench is especially important to distinguish:
it studies forgetting already-seen information after a later forgetting instruction;
our core question is the prospective reverse.

---

# 12. Method opening

Do not revive ReGround as the paper method.

The result naturally creates a stronger method problem:

> **How can a model preserve an exclusion operator in a deferred, executable form and
> compose it with a target only when that target later becomes available?**

Future directions:
- factorized policy-operator and target representations;
- training objective enforcing post-resolution equivalence of target→policy and
  policy→target;
- typed deferred-control state instantiated at evidence arrival;
- external reference monitor / policy runtime;
- activation or routing method that reconstructs the target-conditioned state after
  late resolution.

This follows from the computation rather than bolting on a reminder.

---

# 13. What is not the paper

### G21
Source–Proposition Scope Entanglement is not the current paper center.

It may be a future follow-up, but it does not explain G0.

### G19
ReGround was cancelled before freeze/generation.

### Generic semantic specificity
Not a contribution.

### Another model sweep
Not needed unless G20 behavior requires breadth confirmation.

---

# 14. Main claims if G20 confirms

### Claim 1
> **Prospective exclusion is systematically harder than retrospective exclusion.**

G0.

### Claim 2
> **The reversal reflects target/operator order: target semantics before exclusion
> enable strong control, while late target resolution after exclusion does not reliably
> reconstruct it.**

G18 + G20.

### Claim 3
> **Policy/target knowledge is not enough: models can know the rule and resolve the
> target while excluded evidence remains causally active; other deferred operations can
> still succeed.**

On-policy + G20 comprehension + positive controls.

### Claim 4
> **A target-conditioned causal control state forms during exclusion processing and
> remains history-dependent after target resolution.**

Stage 5 + checkpoint mechanism.

---

# 15. Figure plan

Figure 1:
G0 prospective vs retrospective exclusion + Admit.

Figure 2:
G20 target-first vs rule-first + rule replay + target replay/control.

Figure 3:
Stage 5 rule-time causal state + G20 post-resolution checkpoint interchange.

Compact bridge:
G18 target-semantic factorization.

No G21 main figure.

---

# 16. Outstanding-shaped criterion

The paper is strong enough only if the descent is visible:

```
natural question
→ broad reversal
→ factorization of the reversal
→ non-obvious deferred-composition law
→ causal state carrying that law
→ method problem implied by the law
```

If G20 fails, do not replace it with G21 merely because G21 is interesting.
Reconsider the mainline instead.
