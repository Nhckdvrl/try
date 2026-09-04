> **SUPERSEDED INTERPRETATION NOTICE — later 2026-09-04**
>
> This audit is preserved as research-history provenance. Its recommendation to center
> G20 v3 / non-commutative deferred exclusion was subsequently downgraded after a deeper
> prompt/data audit found that G18 semantic previews mix **target knowledge** with
> **evidential instantiation**, and that the G20 P/U swap still mixes target-state and
> distance.
>
> Current authority:
> [SCIENTIFIC_REGISTER_2026-09-04_V3.md](SCIENTIFIC_REGISTER_2026-09-04_V3.md).
>
> G20 remains a conditional hypothesis only. The registered next design audit is G22
> Target Knowledge vs Evidential Instantiation. No generation is authorized.

# Mainline audit v2 — 2026-09-04

**Status:** scientific audit after rejecting G21 as a paper-center candidate.

## Executive verdict

G21 Source–Proposition Scope Entanglement is **not the natural continuation of G0**.
It may be an interesting secondary consequence of semantic control, but it asks a new
question—source/proposition scope precision—rather than explaining why the same
exclusion rule is weaker before evidence than after evidence.

The paper should instead stay on the original question:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

The strongest current explanation is:

> **LLMs appear to construct a target-conditioned exclusion state when the exclusion
> rule is processed, rather than storing a deferred exclusion operator that is reliably
> composed with a target once that target becomes available later.**

This yields a sharper computational hypothesis:

> **Prospective evidence exclusion is a non-commutative control-composition problem:
> target → EXCLUDE works substantially better than EXCLUDE → target.**

This is a candidate mechanism hypothesis, not yet a finding. A redesigned G20 must test
it directly.

---

## 1. The natural causal graph

### G0 is already an order-of-composition experiment

Retrospective exclusion:

```
TARGET EVIDENCE → EXCLUDE RULE → JUDGMENT
```

Prospective exclusion:

```
EXCLUDE RULE → TARGET EVIDENCE → JUDGMENT
```

The broad empirical reversal is therefore naturally read as an asymmetry in composing
two objects:

1. a semantic representation of the target evidence;
2. an exclusion/control operator.

The important question is not generic instruction position. It is whether the model can
defer the composition until both operands exist.

### Why G18 now fits the original paper naturally

G18 semantic preview:

```
TARGET SEMANTICS → EXCLUDE RULE → later TARGET EVIDENCE → JUDGMENT
```

The actual evidence used by the decision remains after the rule, but a proposition at
least as specific as that evidence already exists when the rule is processed.

Thus G18 can be re-read as a **factorization of G0**:

> Retrospective exclusion may work not because the final evidence block is earlier, but
> because target semantics exist before the exclusion operator is processed.

The fact that lexical overlap, gist, arbitrary identifiers, and unrelated previews do
not reproduce the effect makes this more specific than a generic position or salience
story.

### Stage 4 identifies the target representation

In the system→tool agent setting, exclusion that has access to the proposition follows
that proposition across D7→D9, while an identifier-specific policy does not.

The safe interpretation is:

> the control relation is strongly content-conditioned; symbolic identity alone is not
> a universal carrier of the effective exclusion state.

This is diagnostic, not a separate paper topic.

### Stage 5 identifies the computation time

Matched chronology:

```
FAILURE: unrelated preview → EXCLUDE → evidence → answer
SUCCESS: target paraphrase → EXCLUDE → evidence → answer
```

The later evidence is after the rule in both arms. A target-dependent causal state is
localized around the rule span in the middle of the network, before that later evidence
is processed, in Qwen3-8B and Mistral-Small-24B.

This is exactly what the eager-composition hypothesis predicts.

---

## 2. Unified mechanism hypothesis

### Eager target-conditioned control compilation

A compact version:

> **When processing an exclusion rule, the model constructs a content-conditioned
> control state from whatever target representation is already available. If the target
> has not yet been semantically instantiated, the rule remains under-composed; later
> recognition of the target does not reliably reconstruct the same control state.**

This accounts for the established observations:

- **G0 timing reversal:** retrospective has target semantics before the rule;
  prospective does not.
- **G18 semantic rescue:** a pre-rule paraphrase/entailing preview supplies the target
  representation needed to construct the stronger control state.
- **G18 below-baseline oversuppression:** successful control is content-level rather
  than a clean deletion of one later occurrence; a strong content-conditioned state can
  suppress more than the literal marginal of the repeated evidence block.
- **Stage 4 cross-ID behavior:** the effective target representation is substantially
  semantic rather than purely identifier-based.
- **Stage 5 causal state:** the critical target-dependent state is formed during rule
  processing before later evidence integration.
- **Arithmetic boundary:** explicit `base + w*delta` weighting can be deferred and
  executed exactly, showing the problem is not a generic inability to apply any
  future-directed rule.

This is narrower and more useful than generic “binding,” and broader than “semantic
target information helps.”

---

## 3. G21 verdict

### Paper-center verdict: KILL / DOWNGRADE

G21 asks:

> does a source-scoped exclusion spill into a different allowed source expressing the
> same proposition?

This is non-obvious and potentially publishable in its own right, but it does not
explain the G0 prospective/retrospective reversal.

Its strongest bridge to the current paper is only:

> semantic control may sometimes overgeneralize.

That is a consequence of successful semantic control, not the root cause of prospective
failure.

Therefore:

- do **not** run G21 as the next paper-defining experiment;
- do **not** allocate a main contribution or main figure to source/proposition scope;
- retain the design as a possible future project / secondary consequence if later work
  needs it;
- do not use G21 to justify the current paper title, abstract, or mechanism.

---

## 4. G20 should be redesigned, not merely reprioritized

The old “binding deadline” formulation still risks the trivial objection:

> an earlier decoder hidden state cannot attend to later target tokens.

The stronger experiment must test **history dependence after both target and rule are
already available**.

### G20 v3 — Deferred Control Composition / Non-Commutative Exclusion

Core semantic materials:

- target-semantic preview `P`;
- matched unrelated neutral block `U`;
- exclusion rule `X`;
- actual evidence `E`, semantically matched to `P`;
- a byte-identical neutral **post-resolution checkpoint** `C` before `E`.

Conditions:

```
TARGET-FIRST:
P → X → U → C → E → question

RULE-FIRST:
U → X → P → C → E → question
```

By checkpoint `C`, both arms have seen the same semantic target, the same exclusion
rule, and the same neutral block. A decoder model is now architecturally able to combine
all of them in either arm.

The main behavioral question is:

> **Does exclusion remain weaker in RULE-FIRST even after the model has all information
> needed to resolve the target?**

### Mandatory target-resolution probe

On the full RULE-FIRST context, the model must correctly identify which proposition the
earlier exclusion rule governs.

A stronger trajectory-level version should be considered:

> after late target revelation, require/observe an explicit target-mapping statement,
> then test whether later evidence is nevertheless still used.

This would extend the established “policy access ≠ enforcement” result to
“late target resolution ≠ control composition.”

### Rule reprocessing test

```
RULE-FIRST + REPLAY:
U → X → P → X → C → E

TARGET-FIRST + REPLAY:
P → X → U → X → C → E
```

The important estimand is the interaction:

> replay should preferentially repair RULE-FIRST, not merely improve both arms through
> recency or repetition.

Also include a **target-replay** control if feasible:

```
U → X → P → P → C → E
```

If repeating the target does little while repeating the exclusion operator repairs the
failure, that sharply supports the claim that the missing computation is the
operator–target composition rather than target salience.

### Positive deferred-composition controls

At least two controls should show that the model can combine an earlier unresolved rule
with a later-resolved target in other operations:

- Admit / use-select routing;
- explicit arithmetic weighting.

Existing arithmetic evidence already provides a strong boundary; the new experiment
should preserve the same temporal factorization where possible.

### Masked diffusion

Masked-diffusion replication remains valuable, but it no longer has to carry the entire
anti-causal-mask argument. The post-resolution checkpoint makes the decoder-only test
scientifically meaningful because the state being tested occurs **after both operands
are available**.

---

## 5. The mechanism experiment that would actually complete the story

The best new mechanism is not another patch at the earlier rule token.

Use the shared checkpoint `C`.

At `C`:

- TARGET-FIRST and RULE-FIRST have identical information available;
- token position can be matched by length-matching `P` and `U`;
- only composition history differs.

Test:

1. whether target identity is decodable / probe-correct in both arms at `C`;
2. whether checkpoint states differ specifically in Exclude, not matched Admit/control;
3. TARGET-FIRST → RULE-FIRST checkpoint interchange: does it rescue later suppression?
4. RULE-FIRST → TARGET-FIRST interchange: does it break suppression?
5. after rule replay, does the RULE-FIRST checkpoint state become behaviorally/causally
   more like TARGET-FIRST?

This would establish a much stronger statement than the existing Stage 5 alone:

> **Even after target resolution is available, the model preserves an order-dependent
> control state; causal interchange of that post-resolution state changes how later
> evidence is weighted.**

That is not the trivial statement that an earlier token cannot see the future.

---

## 6. Main claims if G20 v3 confirms

### Claim 1 — broad phenomenon

> **Language models are systematically worse at pre-committing to evidence exclusion
> than at excluding the same evidence after it appears.**

Evidence:
G0, Admit timing control, 12 instruct models, two diffusion LMs, five families.

### Claim 2 — novelty-bearing computational law

> **Exclusion is non-commutative in context: models form effective control when target
> semantics precede the exclusion operator, but often fail to reconstruct the same
> control when the target is resolved later—even before the governed evidence arrives.**

Evidence:
G18 factorization + new G20 v3.

### Claim 3 — knowledge is not composition

> **A model can know the policy and correctly resolve the late target while still
> failing to make the later evidence causally inert.**

Evidence:
existing on-policy/teacher-forced policy-state results + G20 late-target probe /
trajectory-level resolution + arithmetic/routing positive controls.

### Claim 4 — causal mechanism

> **A target-conditioned control state is formed around exclusion processing and
> remains history-dependent after target resolution; changing that state changes later
> evidence suppression.**

Evidence:
existing Stage 5 + post-resolution checkpoint mechanism.

---

## 7. Literature positioning

The exact novelty is not any of the following:

- generic instruction position: Liu et al., Findings ACL 2024,
  https://aclanthology.org/2024.findings-acl.693/
- generic constraint order: Zeng et al., Findings ACL 2025,
  https://aclanthology.org/2025.findings-acl.646/
- prospective-memory recall: TriggerBench 2026,
  https://arxiv.org/abs/2606.23459
- retrospective/in-context forgetting of already-seen information: ICF-Bench, ICLR
  2026, https://proceedings.iclr.cc/paper_files/paper/2026/hash/b13d00a62d438856cfe6fbd13b6b2cb8-Abstract-Conference.html
- identify-then-ignore: I3C, NAACL 2024,
  https://aclanthology.org/2024.naacl-long.379/
- more specific constraints: Chain-of-Specificity, COLING 2025,
  https://aclanthology.org/2025.coling-main.164/
- generic entity/relational binding: Dai et al., EMNLP 2024 and ACL 2026,
  https://aclanthology.org/2024.emnlp-main.967/
  https://aclanthology.org/2026.acl-long.2194/
- localized instruction states: Patches of Nonlinearity, ACL 2026,
  https://aclanthology.org/2026.acl-long.559/

The closest conceptual predecessor is Racing Thoughts, NAACL 2025:
https://aclanthology.org/2025.naacl-long.155/

That paper shows a dependency-ordering failure in contextualization. The present
candidate contribution is a distinct dependency:

> **semantic target resolution must be composed with an exclusion operator, and current
> LLMs may fail to perform that deferred composition after the operator has already
> been processed.**

This is the correct comparison point, not a claim of “first binding.”

---

## 8. Method opening

If the result holds, the natural follow-up method problem is:

> **How do we make policy–target composition order-invariant, so a policy can remain
> executable while its target is unresolved and be instantiated only when the target
> later appears?**

Promising future directions:

- factorized representations for persistent policy operator vs target instance;
- an auxiliary objective enforcing equivalence of
  `target→policy` and `policy→target` after target resolution;
- a typed deferred-control state that is instantiated at evidence arrival;
- external policy runtimes / reference monitors that evaluate the policy on the actual
  evidence object instead of asking the LM to precompile it in prose;
- activation- or routing-level reconstruction of the post-resolution control state.

This follows directly from the failure. It is not “retrieve and repeat the rule.”

---

## 9. Outstanding-shaped bar

If G20 v3 shows all of the following:

1. high late-target comprehension;
2. TARGET-FIRST > RULE-FIRST exclusion on a fresh multi-family set;
3. selective rule-replay rescue, ideally stronger than target replay;
4. matched Admit/arithmetic/routing late composition works;
5. a post-resolution checkpoint remains causally order-dependent;
6. the result is not confined to one model family;

then the paper has the desired descent:

```
natural pre-commitment question
→ broad prospective/retrospective reversal
→ target/operator factorization
→ non-commutative deferred-control failure
→ causal post-resolution state
→ order-invariant deferred control as the method problem
```

That is substantially more coherent than the G21 branch and substantially less obvious
than “semantic target information helps.”
