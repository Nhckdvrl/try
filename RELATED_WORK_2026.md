# Related work — binding future evidence control

The post-reset paper asks two questions:

> **Can an exclusion rule be late-bound when its target becomes identifiable only
> after the rule has already been processed?**

and

> **When exclusion binds semantically, does it preserve the source/occurrence scope of
> the policy or spread to semantically equivalent evidence outside that scope?**

These questions deliberately avoid three occupied/obvious claims:
- later instructions can be easier to follow;
- more specific semantic constraints can help;
- identifying irrelevant information and then telling the model to ignore it can
  improve performance.

## 1. Why the old "semantic target helps" story is insufficient

### Instruction Position Matters — ACL 2024 Findings
https://aclanthology.org/2024.findings-acl.693/

Moving the task instruction after the input can improve sequence-generation
instruction following, motivated by instruction locality/forgetting.

Implication:
our G0 sign alone is not novel.

### Chain-of-Specificity — COLING 2025
https://aclanthology.org/2025.coling-main.164/

Emphasizing and progressively refining specific constraints improves constraint
adherence.

Implication:
"make the target more specific" is an occupied engineering idea and cannot be our
headline explanation.

### I3C — NAACL 2024 Main
https://aclanthology.org/2024.naacl-long.379/

I3C identifies candidate irrelevant conditions, verifies them, and then explicitly
instructs the model to ignore them.

Implication:
"identify what should be ignored, then explicitly mark it" is already occupied in
spirit. This is why the cancelled ReGround design is not a paper-level method novelty.

## 2. Prospective memory

### Did You Forget What I Asked? — 2026
https://arxiv.org/abs/2603.23530

Deferred formatting constraints degrade under concurrent task load; salience-enhanced
formatting with a trailing reminder restores much of the lost compliance.

Our distinction:
G20 does not ask whether a remembered rule is repeated near answer time. The rule stays
fixed, the semantic target is revealed after it but before evidence/decision, and the
test asks whether **target resolution can retroactively update an already processed
control rule**.

If LATE-BIND works as well as PRE-BIND, we should concede that prospective-memory /
ordinary context integration is a sufficient story and drop the binding-deadline claim.

## 3. Generic binding is occupied

### Representational Analysis of Binding in Language Models — EMNLP 2024 Main
https://aclanthology.org/2024.emnlp-main.967/

Studies entity–attribute Binding IDs and localizes a low-rank binding subspace; editing
that subspace causally changes which attribute is bound to an entity.

Our distinction:
we do not claim to discover binding in general. The object is a **control relation**
between a policy and a future evidence instance/source.

The critical G20 question is temporal:
can that control relation be formed after the rule has already been processed?

The critical G21 question is scopal:
does the relation bind to an evidence instance/source or collapse onto proposition
identity?

## 4. Instruction representations are occupied

### Patches of Nonlinearity — ACL 2026 Main
https://aclanthology.org/2026.acl-long.559/

Localizes instruction representations and shows non-linear causal interaction;
instruction vectors act as circuit selectors conditioned on earlier task
representations.

Our distinction:
Stage 5's mid-layer rule state is not novelty by itself. It matters because it suggests
a specific computation at rule time. G20 can test whether **later target information
fails to reconstruct that state unless the rule is replayed**.

## 5. Negative constraints

### Semantic Gravity Wells — 2026
https://arxiv.org/abs/2601.08070

Studies negative output constraints, where explicitly naming forbidden tokens can
increase semantic pressure toward those tokens and late layers can override
constraint-compliant computation.

Our distinction:
the governed object here is not an output token. It is the **causal contribution of
contextual evidence**, with source/occurrence scope explicitly measurable.

G21's potential scope spillover is therefore not simply forbidden-token priming.

## 6. Provenance and source identity

Several recent papers establish that LLMs can represent or be evaluated on provenance,
and that source labels affect decisions.

### TROVE — ACL 2025 Main
https://aclanthology.org/2025.acl-long.577/

Traces generated sentences back to fine-grained source sentences and classifies the
relation between generation and source.

### GenProve — ACL 2026 Main
https://aclanthology.org/2026.acl-long.228/

Trains generation with fine-grained provenance.

### GAVEL — ACL 2026 Findings
https://aclanthology.org/2026.findings-acl.1789/

Uses evidence contracts that bind atomic subclaims to explicit evidence units and
mechanically validates provenance.

### Label Effects — ACL 2026 Main
https://aclanthology.org/2026.acl-long.1495/

Shows counterfactually that source labels themselves alter human and LLM trust
judgments.

These works occupy:
- provenance tracing;
- evidence attribution;
- source-label trust;
- provenance-grounded generation.

They do **not** directly ask G21's control question:

> If Source A is explicitly excluded and independent Source B is explicitly allowed,
> does B lose causal evidential weight merely because it expresses the same
> proposition as A?

That distinction matters. Correct provenance tracking is compatible with incorrect
policy scope: a model may know that a statement came from B and still apply A's
semantic exclusion to it.

## 7. Provenance-role separation in agent memory

### MemIR — Mitigating Provenance-Role Collapse in Long-Term Agents (arXiv 2026)
https://arxiv.org/abs/2605.25869

MemIR identifies provenance-role collapse in long-term agent memory and introduces a
typed intermediate representation that separates raw evidence, retrieval cues, and
truth-bearing claims, with provenance-scoped utilization.

This is a serious neighboring concept. It means our paper should **not** coin
"provenance collapse" or claim that LLM systems have never been shown to blur source
roles.

The remaining distinction is narrower and behavioral:
MemIR studies memory representation and source-monitoring architecture; G21 asks
whether a natural-language **source-scoped exclusion policy**, even when Source B is
explicitly marked admissible, causally discounts B's contribution when B is
semantically equivalent to excluded Source A.

The direct factorization between source-scoped and proposition-scoped policies, with
redundancy-deconfounded conditional evidence marginals, is therefore essential.

## 8. Decision-time exclusion / non-use governance

A very recent non-peer-reviewed preprint, **Certified Amnesia: A Decision-Evidence
Protocol for Provable Context Exclusion in AI Agents** (July 2026), explicitly
distinguishes syntactic context exclusion from stronger semantic non-use and proposes
provenance-backed certificates for showing that forbidden items were absent from a
decision's effective context.

This is an important adjacent systems/governance reference.

Our question is complementary:
- Certified Amnesia asks how a system can **guarantee/certify** that forbidden
  provenance was not admitted to effective context;
- we empirically ask what an LLM does when the forbidden and allowed evidence are both
  present and a natural-language rule is supposed to make only one source causally
  inert.

If G21 succeeds, it provides a behavioral reason why provenance-preserving external
enforcement may be necessary: semantic in-model exclusion may not preserve
source-specific scope.

Do not claim priority over decision-time context exclusion as a systems problem.

## 9. Contextualization / dependency-order mechanisms

### Racing Thoughts — NAACL 2025 Main
https://aclanthology.org/2025.naacl-long.155/

Explains contextualization errors through a race-condition hypothesis in which
computations that should condition later processing do not resolve in the necessary
order.

This is the closest narrative/mechanistic neighbor to G20.

The distinction:
our proposed dependency is between **target resolution and rule compilation**. The same
semantic target is available before final decision in both PRE and LATE conditions;
only whether it crossed the rule-processing boundary changes.

A positive replay interaction would make this much more than generic prompt order.

### Llama See, Llama Do — ACL 2025 Outstanding
https://aclanthology.org/2025.acl-long.791/

Turns broad distraction into the sharper regularity of contextual entrainment and then
causally localizes entrainment heads.

Narrative lesson:
the paper needs a new regularity underneath the coarse failure. "Semantic target helps"
does not meet that bar; binding deadline or scope collapse potentially does.

### Do LLMs Know Tool Irrelevance? — ACL 2026 Main
https://aclanthology.org/2026.acl-long.1473/

Turns tool-irrelevance errors into a conflict between structural alignment and semantic
relevance, with a dedicated factorized benchmark and causal pathway analysis.

Narrative lesson:
our factorization should concern **binding strength vs scope precision**, not simply
identifier vs semantic content.

## 10. Policy/hierarchy benchmarks

### IHEval — NAACL 2025 Main
System/user/history/tool instruction conflicts.

### COMPASS — ACL 2026 Main
Organization-specific policy alignment; prohibition/denylist behavior can be weak.

These establish that policy compliance is difficult. Our novelty cannot be "models
fail policies".

Our question concerns the internal referent/scope of a valid exclusion policy:
- when can the policy acquire its future target?
- once acquired, does it remain bound to the correct source/occurrence?

## 11. Novelty position after the audit

The paper should **not** claim:
- first evidence-exclusion work;
- first policy-following failure;
- first study of binding;
- first provenance-aware LLM work;
- first discovery that more specific instructions help.

The candidate missing dependency, after targeted search, is narrower:

> **Whether a natural-language control rule can be late-bound after its semantic
> target is revealed across the rule-processing boundary, and whether successful
> semantic binding preserves source/occurrence scope when independently sourced
> evidence expresses the same proposition.**

We have not found an ACL/EMNLP/NAACL paper directly isolating these two dependencies.
That is a search result, not a proof of priority; final writing should say "we study"
rather than "we are the first".

## 12. Cancelled method

ReGround G19 was cancelled before freeze/generation.

Reason:
post-retrieval target resolution followed by an explicit exclusion ledger is a
reasonable systems response, but it is too close to ordinary policy evaluation and
identify-then-ignore pipelines to be the scientific novelty.

Do not include it in the paper's contribution list.
