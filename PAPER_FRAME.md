# Paper frame — final scientific story

**Updated:** 2026-09-04, after G18.
**Experimental programme: closed.**

Historical development belongs in RESEARCH_HISTORY.md. This file records only the
final intellectual structure of the paper.

## 1. Natural question

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

Policies commonly precede the information they govern: a system prompt constrains a
source before retrieval, a court excludes evidence before it is introduced, and an
agent can be told which information must not affect a later decision.

The paper asks whether such a stated exclusion policy actually governs the later
decision, and what determines whether it succeeds.

## 2. Main claim

> **Prospective exclusion depends on target addressability. A policy can be explicitly
> available to a model without reliably controlling later evidence; control becomes
> substantially stronger when the policy is processed with a sufficiently specific
> semantic representation of the information it will govern.**

“Target addressability” is the explanatory variable. It should not be turned into a
grand theory of all instruction following. The paper is about one natural failure:
making future evidence causally inert.

## 3. Contribution 1 — a broad prospective exclusion gap

We preregistered a prediction motivated by human instructed-disregard research: once
evidence has already been seen, excluding it should be harder. The model result is the
opposite ordering.

Across **12 instruction-tuned models from four vendors, two masked diffusion language
models, and five task families**, the same exclusion instruction works substantially
better after the evidence than before it. Delta_time has the same sign in all twelve
instruct models, with ten of twelve intervals excluding zero. The matched Admit rule
does not show the same order effect.

This contribution establishes the phenomenon, not the final explanation.

### Explicit policy access is not enough

The separate declarative probe recovers the required zero-weight policy at ceiling,
but the stronger result is on-policy: in Qwen3-8B and Gemma-3-12B, prospective
evidence can still influence the decision even on trajectories that explicitly state
zero weight; teacher-forcing the correct zero-weight statement also does not fully
restore suppression.

The paper therefore says:

> **Explicit access to the policy is not sufficient for causal enforcement.**

It does **not** say that every model perfectly preserves an internal policy state and
then “ignores” it.

### Supporting localisation

Distance, rule-to-evidence delay, eight ruling wordings, and two bidirectional masked
diffusion models jointly show that ordinary recency, one fragile wording, or a
left-to-right causal mask is not a sufficient account. These are supporting
characterisations, not four independent claims.

### Boundary condition: hard suppression

The timing asymmetry is sharply concentrated in the hard-suppression regime. A
same-wording requested-weight sweep shows a large zero-point discontinuity, while an
arithmetically explicit contribution task is implemented prospectively with a zero
pre/post gap in four of five models.

This should be stated as:

> **The asymmetry is strongest when the model must make semantically integrated
> evidence causally inert, and disappears when the required contribution is explicitly
> computable.**

Do not claim a universal “only exactly zero” law: cap/sign-flip manipulations retain
smaller timing gaps, and many non-zero multiplicative weights were not faithfully
implemented.

## 4. Contribution 2 — target addressability

This is the conceptual centre of the paper.

### 4.1 Confirmatory G18

G18 was designed after Stage 3C–3E had discovered the final explanatory variable and
the correct raw-point estimand. It was frozen before any generation and used entirely
fresh items and skeletons.

Design:
- 100 fresh items / 30 fresh skeletons / three families;
- five checkpoints across four vendors;
- six target representations before the rule: none, identifier stub,
  lexical-overlap/wrong proposition, paraphrase, entailing-specific statement, and
  unrelated length-matched content;
- three rule states per preview, so every preview has its own no-rule baseline;
- raw sign-aligned rating points only.

Pooled ExclusionEffect:

| representation available at rule time | ExclusionEffect |
|---|---:|
| more-specific statement entailing the evidence | **31.16 [27.99,34.40]** |
| same proposition, different wording | **30.93 [28.19,33.66]** |
| referential identifier stub | 26.27 [23.65,28.96] |
| unrelated length-matched content | 22.06 [19.16,24.97] |
| nothing | 21.84 [19.21,24.66] |
| high lexical overlap, different proposition | 18.08 [15.71,20.57] |

Primary frozen contrast:

> **Delta_semantic = +8.91 [+7.15,+10.76] rating points, positive in 5/5 models.**

The clean para-minus-empty contrast is **+12.85 [+10.32,+15.42]**, positive in 5/5
models and individually excluding zero in 4/5.

The intended interpretation is graded, not binary. Referential identity provides
some control, but a specific matching semantic representation provides substantially
more; lexical resemblance without the proposition does not.

### 4.2 Discovery evidence that explains the G18 factor

Earlier rounds give the shape behind the confirmation:
- merely announcing a future identifier, type, or direction does not recreate
  post-evidence suppression;
- a semantically empty tag behaves like an identity predicate, ruling out “local tag”
  structure by itself;
- a content×identity 2×2 shows that matching content under the wrong label suppresses
  better than the right label carrying the wrong content in all four tested models;
- Stage 3E separates semantic targeting from duplicate/redundancy effects.

These experiments are discovery support; G18 is the load-bearing confirmation.

### 4.3 A surprising consequence: suppression extends beyond the named block

G18 decomposes ExclusionEffect into the later evidence's marginal contribution with
and without the exclusion rule.

Under a semantic preview, the later evidence is already almost redundant:
marg(no rule) is about +3 rating points. Yet marg(exclude) is about -28 points under
paraphrase/entailment, below the preview-only baseline. The sign is negative in 5/5
models for paraphrase and positive in 5/5 for the lexical-overlap/wrong-proposition
control.

This licenses:

> **Once the target is semantically identified, exclusion can extend beyond the
> literal later block named by the rule.**

It does not distinguish proposition-level generalisation from answer-level
overcorrection, so the paper reports both as possible readings.

## 5. Contribution 2 in an agent

The same distinction appears in a natural SYSTEM→TOOL interaction.

A SYSTEM policy is stated before retrieval, a document arrives in a TOOL message, and
the assistant makes a judgment. Identifier-only policies are not universally useless:
Gemma-3-12B and Qwen3.5-27B can suppress their named D7.

The invariant across all four agent models is the counterfactual identity swap:

> **When the same proposition arrives as D9, identifier-only protection does not
> transfer, while a proposition policy continues to suppress the information under the
> new identifier.**

Thus symbolic identity and semantic content create different control relations.
Semantic policies follow information across surface identity changes.

This is an externalisation of Contribution 2, not a deployment benchmark.

## 6. Contribution 3 — causal mechanism

The mechanism is required to explain the target-addressability contrast, not to add MI
prestige.

### 6.1 The excluded evidence still reaches the decision

In Qwen3-8B, blocking downstream access to the excluded evidence span returns the
answer toward the no-evidence Base condition. The residual behavioral effect therefore
depends causally on reading that evidence at/after the decision.

### 6.2 Gating is resolved late

Answer-position patching finds little recovery in lower layers and strong recovery
later, locating the final decision-level resolution downstream of the rule.

### 6.3 A target-dependent rule state is causal

The key matched-chronology comparison is:

unrelated padded preview → rule → later evidence

versus

paraphrase preview → rule → later evidence

The evidence used for the decision is after the rule in both conditions; preview
length is matched. Rule-span interchange changes later suppression before the later
evidence has been processed.

- Qwen3-8B: causal window L14–18 of 36, relative depth 0.39–0.50.
- Mistral-Small-24B: L12–16 of 40, relative depth 0.30–0.40.

The shared finding is a **mid-network, target-dependent rule state whose interchange
changes subsequent evidence suppression**. Qwen's stronger break than rescue does not
replicate and is model-specific.

Do not claim a reusable “semantic binding vector” or a dedicated TARGET_FOUND circuit;
the held-out shared-direction steering test failed.

## 7. Practical implications — actionable, not a mitigation contribution

The paper does not introduce a new deployment algorithm, but the completed experiments
already imply three actionable design principles:

1. **Restate exclusion after retrieval when feasible.** The same policy is much more
   effective after the evidence has appeared.
2. **Address policies to meaningful information/provenance rather than assuming a
   resource name is semantic protection.** Meaningful evidence-carried criteria and
   semantic target descriptions support stronger prospective control.
3. **Treat identifier scope and semantic scope as different.** The D7→D9 agent
   counterfactual shows that an identifier policy does not automatically follow the
   information it was intended to protect against.

These are supported design implications, not a claim of a fully evaluated mitigation
system. A future engineering direction is a post-retrieval policy compiler that
re-instantiates prospective policies against retrieved content, but this paper does
not evaluate such a method.

## 8. Outstanding-shaped alignment

The aspiration is Outstanding-shaped scientific organisation, not an Outstanding
award claim.

- **ACL 2025 Outstanding — Llama See, Llama Do:** broad distraction problem →
  contextual entrainment regularity → semantic modulation → entrainment heads →
  head ablation attenuates the behavior. Our analogue is prospective exclusion →
  target addressability → G18 factorization → causal rule state.
- **EMNLP 2025 Outstanding — Causal Interventions Reveal Shared Structure:** a theory
  question exists before the MI method; interchange intervention answers the theory
  question rather than merely localising activations. Our matched rule-state
  interchange is used for the same reason: it tests the target-dependent explanation.
- **ACL 2024 Outstanding — CausalGym:** causal interpretability is evaluated by its
  ability to change behavior, not by probe accuracy alone. Our strongest mechanism
  claims therefore come from span gating and interchange, not decoding a state.
- **NAACL 2025 Main — Racing Thoughts:** natural failure → algorithmic hypothesis →
  correlational and causal evidence → inference implication. This is the closest NAACL
  structural reference.
- **ACL 2026 Main — Do LLMs Know Tool Irrelevance?:** coarse failure → factorized
  explanatory variable → controlled benchmark → competing internal pathways →
  mitigation. G18 plays the same centerpiece role as the factorization experiment.

Our main remaining gap relative to the most actionable Outstanding/Main examples is
that we do not evaluate a new mitigation algorithm. This is **not required for the
scientific paper**: the EMNLP Outstanding filler–gap paper is theory-advancing causal
interpretability without a deployment method. We should therefore strengthen the
Discussion's actionable implications, not reopen experiments.

## 9. Final arc

Can a model commit in advance to ignore evidence it has not seen?
    ↓
A broad prospective-exclusion gap appears across models, architectures and tasks.
    ↓
Explicit access to the policy is not sufficient for enforcement; simple locality and
forgetting do not explain the phenomenon.
    ↓
G18 identifies the decisive explanatory variable: target addressability. Matching
semantic representations support substantially stronger prospective exclusion than
reference or surface resemblance alone.
    ↓
In an agent, semantic control follows the proposition across document identity.
    ↓
A target-dependent mid-network rule state causally controls later evidence suppression
in two architectures.

## 10. Programme status

**Closed.** No further experiment is required before submission. The remaining work is
figures, writing, appendix organisation and reviewer simulation.
