# Paper outline — post-G18 writing blueprint

**Updated:** 2026-09-04

This outline follows the final intellectual structure, not the chronological order of
experiments.

## Working title

> **Can Language Models Commit in Advance to Ignore Evidence?**

Alternative:
- *Before the Evidence Arrives: Target Addressability in Prospective Exclusion*
- *What Can an Exclusion Policy Refer To? Prospective Evidence Control in LLMs*

The title should stay natural. “Target addressability” is the explanatory variable,
not a replacement for the question.

## Abstract structure

The abstract should contain exactly five moves:

1. **Natural problem.** Policies often precede the information they govern.
2. **Phenomenon.** Across 12 instruct models, two masked diffusion LMs and five task
   families, the same exclusion rule works better after evidence than before it.
3. **Key dissociation.** Explicit policy access is not sufficient for enforcement.
4. **Centerpiece explanation.** G18 prospectively confirms target addressability on
   fresh materials: semantic target representations improve exclusion by
   **+8.91 [7.15,10.76] rating points** relative to referential/surface controls, with
   the effect positive in all five models.
5. **Mechanism.** A target-dependent mid-network rule state causally changes later
   suppression in Qwen3-8B and Mistral-Small-24B.

Do not claim “the policy is perfectly held and ignored,” “only zero works,”
“identifiers never work,” or a dedicated semantic-binding circuit.

## 1. Introduction — policies arrive before their targets

Opening examples:
- system policy before retrieval;
- inadmissibility before later evidence;
- agent restriction before memory/tool output.

Question:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

Human instructed-disregard work motivates the original prediction, but the paper
should say only that the LLM ordering **reversed our human-motivated preregistered
prediction**, not that it exactly reverses a matched human experiment.

### Contributions

1. **Prospective exclusion gap.** A broad before/after asymmetry across models,
   architectures and tasks.
2. **Target addressability.** A fresh prospectively frozen factorial shows that a
   sufficiently specific semantic target supports substantially stronger prospective
   exclusion than reference or surface resemblance alone; the same distinction
   transfers to an agent.
3. **Causal mechanism.** Target-matched context changes a mid-network rule state, and
   interchanging that state changes later evidence suppression in two architectures.

The Introduction should not enumerate every control.

## 2. Measuring evidence influence

### 2.1 G0 materials

- 144 frozen items.
- five task families: legal judgment, evidence inference, ranking/selection,
  outcome evaluation, numeric aggregation.
- screened only on Base/Admit before any Exclude condition was generated.
- Base, Admit-before/after, Exclude-before/after plus independent probes.

### 2.2 Readout

Explain the behavioral rating readout and REI only for G0/discovery rounds.
Emphasize:
- deterministic continuous readout;
- no LLM judge;
- matched Admit anchors.

G18 uses a different, cleaner estimand:
- raw sign-aligned rating points;
- every preview has a preview-only and no-rule baseline;
- ExclusionEffect is the number of rating points removed by the rule beyond the
  preview's own effect.

The transition from REI in discovery to raw points in G18 should be framed as a
methodological lesson learned and then prospectively fixed, not hidden.

## 3. Phenomenon — prospective exclusion is harder

### 3.1 Broad reversal

**Figure 1A.** 12 instruct models + two masked diffusion models.

Show:
- Exclude-before;
- Exclude-after;
- matched Admit-before/after.

Headline:
> the exclusion timing gap is widespread; generic rule order is not.

### 3.2 Explicit access is not sufficient

Use only the strongest evidence:
- declarative zero-weight probe is near/at ceiling;
- on-policy trajectories in Qwen/Gemma can explicitly state zero weight while the
  evidence still influences the decision;
- teacher-forcing the correct zero-weight statement does not fully restore
  prospective suppression.

Conclusion:
> **policy accessibility and policy enforcement are separable.**

### 3.3 Compact localisation paragraph

One paragraph, not four subsections:
- delay up to ~1,000 tokens does not systematically worsen prospective failure;
- rule-to-answer distance has no main effect;
- eight wording families preserve the gap;
- bidirectional masked diffusion models preserve it.

Conclusion:
> ordinary forgetting, wording fragility, and a causal prompt mask are insufficient
> explanations; the next question is what the rule can target.

### 3.4 Boundary condition

A short subsection:
- timing gap is sharply concentrated at hard suppression;
- explicit arithmetic contributions can be prospectively zeroed exactly;
- non-multiplicative cap/sign-flip retain smaller effects.

Do not promote “zero discontinuity” into a separate contribution.

## 4. Target addressability — the centerpiece

This is the longest behavioral section and **Figure 2**.

### 4.1 Why a confirmation was necessary

In two sentences:
- Stage 3C–3E discovered the semantic-target account and the correct raw-point
  estimand through iterative design;
- G18 therefore re-tests the final claim prospectively on fresh items and skeletons.

### 4.2 G18 design

**Figure 2A: factorial schematic.**

Six target representations before the rule:
- none;
- identifier stub;
- lexical-overlap but wrong proposition;
- paraphrase;
- more-specific entailment;
- unrelated length-matched.

Three rule states per level:
- preview only;
- preview + evidence;
- preview + exclusion rule + evidence.

Five models / four vendors / 100 fresh items / 30 fresh skeletons / three families.

### 4.3 Primary result

**Figure 2B: ExclusionEffect by target representation.**

Report:
- entail 31.16 [27.99,34.40]
- para 30.93 [28.19,33.66]
- ident 26.27 [23.65,28.96]
- unrel 22.06 [19.16,24.97]
- none 21.84 [19.21,24.66]
- empty 18.08 [15.71,20.57]

Primary frozen contrast:
> **Delta_semantic = +8.91 [7.15,10.76], positive in 5/5 models.**

Decisive surface-matched contrast:
> **para - empty = +12.85 [10.32,15.42]**, positive in 5/5; 4/5 individual CIs
> exclude zero.

Interpretation:
> target representation matters; reference helps somewhat, but matching semantic
> content supports substantially stronger control than reference or lexical form.

### 4.4 Decomposition

**Figure 2C.**

Show only the memorable comparison:
- empty: marg(no rule) ~+32, marg(exclude) ~+14;
- para: marg(no rule) ~+3, marg(exclude) ~-28.

State two findings:
1. semantic preview redundancy is real and large, and G18's baseline design nets it
   out;
2. once the target is semantically identified, exclusion extends beyond the literal
   later block, producing below-baseline suppression.

Do not decide between proposition-level generalisation and overcorrection.

### 4.5 Discovery support

Move most Stage 3A/3D/3E detail to appendix. In main text give one compact panel or
paragraph:
- paraphrase beats lexical wrong-meaning;
- content×identity 2×2 favors matching content over matching label;
- semantically empty Z9 does not reproduce meaningful provenance/class effects.

These explain why G18 was designed as it was; they are not separate contributions.

## 5. Agent counterfactual — semantic scope survives identifier change

**Figure 3A** or a small panel attached to Figure 2.

Structure:
SYSTEM policy → TOOL document → assistant decision.

Do not headline “identifier policies fail.” Instead show:
- identifier policies can suppress their named D7 in some models;
- when the same proposition arrives as D9, that identifier-specific protection does
  not transfer;
- proposition policies continue to suppress the content under D9.

Conclusion:
> **identifier scope and semantic scope are different control relations.**

Practical implication:
a pre-retrieval policy cannot be assumed to follow information merely because the
information is logically “the same thing” as a named resource.

## 6. Mechanism — how target availability changes later gating

**Figure 3B–D.**

### 6.1 Evidence span is causally read

Span gate in Qwen3-8B:
blocking downstream access to the excluded evidence returns the decision toward Base.

Purpose:
establish that residual influence is carried by evidence access, not merely by a
previously changed hidden state.

### 6.2 Late answer-level resolution

Answer-position patching:
little recovery in lower layers, increasing recovery later.

Purpose:
separate the earlier rule-state difference from the later final decision resolution.

### 6.3 Target-dependent rule-state interchange

Matched chronology:
- unrelated padded preview → rule → evidence;
- paraphrase preview → rule → evidence.

At rule time the later evidence is not yet processed in either run.

Causal transfer:
- Qwen3-8B: L14–18/36, break +13.3 [8.1,18.9], rescue -3.6 [-5.9,-1.4];
- Mistral-Small-24B: L12–16/40, break +15.7, rescue -13.4, null above depth 0.45.

Headline:
> **a target-dependent mid-network rule state causally carries the
> successful-vs-failed prospective exclusion contrast.**

Avoid:
- reusable semantic-binding vector;
- dedicated TARGET_FOUND circuit;
- universality beyond the two architectures.

### 6.4 What failed mechanistically

Keep to 3–4 sentences:
- shared steering direction did not generalise;
- G16 class-marker bridge failed because the fixed-position readout was blind to that
  behavioral contrast;
- therefore mechanism scope is content-target addressability only.

Detailed correction history goes to appendix.

## 7. Discussion — what this changes

### 7.1 Scientific implication

Instruction following is not only about whether a rule is represented or remembered.
For prospective information-control policies, the relation between a rule and a
not-yet-instantiated target can be a separate bottleneck.

### 7.2 Agent/policy implication

Existing experiments support:
- post-retrieval restatement;
- meaningful semantic/provenance policy targets;
- separating identifier scope from semantic scope.

Do not call these a new mitigation algorithm.

### 7.3 From mechanism to methods

Outstanding/Main references show two legitimate endpoints:
- actionable mitigation, as in *Llama See, Llama Do*, *Racing Thoughts*, and
  *Tool Irrelevance*;
- theory-advancing causal explanation without a deployment method, as in the EMNLP
  Outstanding filler–gap paper and ACL Outstanding CausalGym.

Our paper belongs primarily to the second category, with actionable design
implications from existing behavioral experiments. A future method could re-ground a
prospective policy against retrieved content after tool return, but this is future
work, not an untested contribution.

## 8. Related work

Organize around occupied questions, then the missing dependency:
1. irrelevant-information identification (I3C);
2. hierarchy/policy compliance (IHEval, COMPASS);
3. instruction position and prospective memory;
4. long-context cue/trigger dependencies;
5. negative constraints and in-context suppression;
6. mechanistic instruction representations;
7. contextualization/distraction mechanisms.

Positioning sentence:

> Prior work studies whether models identify irrelevant information, remember
> deferred instructions, obey policy hierarchies, or represent instructions
> internally. We ask what happens when a valid policy is processed **before its
> evidential target exists**, and show that the target representation itself is a
> causal determinant of later enforcement.

## 9. Limitations

Keep compact:
- controlled authored materials, not a naturally occurring corpus;
- G18 explanation breadth: five models / three families, not the full 14-model G0
  panel;
- Phi-4-mini para-empty individual CI overlaps zero despite the panel effect;
- mechanism on two architectures;
- G18 below-baseline suppression has two viable interpretations;
- screening details and collapsed minor families in appendix.

## Main figures

**Figure 1 — The phenomenon.**
Broad model panel, Exclude-before vs Exclude-after, Admit control.

**Figure 2 — The centerpiece.**
A: G18 factorial schematic.
B: ExclusionEffect by target representation.
C: decomposition (empty vs para).

**Figure 3 — Generalisation and mechanism.**
A: agent D7→D9 counterfactual.
B: span gate.
C: layer-wise rule-state interchange for Qwen and Mistral.

## Appendix priorities

- full G0 model×family tables;
- rule wording and distance/delay characterization;
- requested-weight sweep / arithmetic boundary;
- Stage 3 discovery ladders and content×identity tables;
- Stage 3E redundancy/metric correction;
- tagged stream;
- on-policy trajectory analysis;
- full agent tables;
- G16/G17;
- Stage 5 correction and failed shared direction;
- readout pilots and validity;
- stopped hindsight branch only as repository provenance, not paper appendix unless
  required for artifact transparency.
