# Paper outline

**Updated:** 2026-09-03

The paper is one investigation of one question. The arc is:

> **advance exclusion fails → not the obvious causes → only at exactly zero →
> binding determines it → same failure in an agent → causal gating mechanism**

## Title

Recommended:

> **Can Language Models Commit in Advance to Ignore Evidence?**

Other viable forms:

- *Why Language Models Fail to Exclude Evidence Before They See It*
- *Told in Advance, Ignored Anyway: Prospective Evidence Exclusion in LLMs*

Keep **advance commitment to ignore evidence** as the object. `Prospective binding
failure` is the mechanism's name and belongs in the body, never in the title.

## Abstract draft

> A policy usually exists before the data it governs: a system prompt forbids a
> source before retrieval runs, a court excludes evidence before the record is
> read. We ask whether a language model can commit in advance to ignore evidence it
> has not yet seen. Borrowing the design of the human inadmissible-evidence
> literature, we preregistered the human pattern — that an instruction arriving
> *after* the evidence is the hard case — and found the opposite. Across twelve
> instruction-tuned models from four vendors, two masked diffusion language models,
> and five task families, exclusion stated after the evidence is followed well,
> while the identical instruction stated before it leaves up to 0.64 of the
> evidence's normal causal weight in the decision. This is not a failure to hold
> the rule: asked what weight the evidence should receive, every model answers
> exactly zero on 100% of items in both conditions. It is not distance, not the
> causal attention mask — the asymmetry is largest in a bidirectional diffusion
> model — and not one wording. The failure is specific to driving a contribution to
> exactly zero, and disappears entirely when that contribution is arithmetically
> computable. What decides the outcome is what the policy can bind to: naming a
> future item makes suppression worse than not mentioning it at all, a preview
> rescues it in proportion to entailment rather than surface overlap, and a class
> marker carried on the evidence itself drives leakage to zero whether the policy
> is stated before or after. The same dissociation appears in an agent, where a
> system-level identifier policy is worth nothing and suppression follows the
> proposition rather than the document ID. Mechanistically, the excluded evidence
> is still read at the decision — blocking that one attention path removes the
> entire residual — gating is resolved in the upper-middle layers, and a binding
> state transfers causally between matched runs in both directions.

## 1. Introduction — a rule that arrives before its target

Open on the ordinary structure: policies precede the data they govern. Give the
three concrete cases (system prompt before retrieval, inadmissibility before
testimony, agent memory restrictions before lookup).

State the human baseline honestly, because it is what we predicted: a meta-analysis
over 48 studies and 8,474 participants finds that jurors told to disregard evidence
they have already heard retain its influence. Our preregistration predicted the
same ordering in models.

Then the question and the reversal.

Three contributions, positively:

1. **Phenomenon.** Exclusion stated before the evidence fails where the identical
   exclusion stated after it succeeds — the reverse of the human pattern — while
   the model states the policy perfectly in both cases.
2. **Explanation.** The failure occurs only at complete suppression, and is
   governed by what the policy can bind to: propositional content and
   evidence-carried class markers work prospectively, named future identifiers do
   not. The same dissociation holds in an agent.
3. **Mechanism.** Excluded evidence is still read at the decision; gating is
   resolved late; a binding state is causally exchangeable between matched runs.

Do not enumerate ruled-out accounts here. Section 3 does that as science.

## 2. Measuring whether a rule governs a decision

Introduce the instrument after the question.

- 144 frozen items, five task families, built from 10 legal case skeletons plus
  inference, ranking, outcome-evaluation and numeric-aggregation families.
- Five conditions plus independent rule and memory probes.
- `REI` = 0 means the model decided as if it had never seen the evidence; 1 means
  it used the evidence as fully as when told it was admissible.
- Readout: a greedily decoded two-sentence rationale followed by the expectation of
  the next-token distribution over digits at a fixed position. Deterministic,
  continuous, no parsing, no LLM judge. The three piloted readouts that failed and
  why belong in the appendix — they are a genuine methodological contribution.
- The mechanism sections use a one-token variant of the same readout at the same
  position, because patching needs a single forward pass. It tracks the behavioural
  readout on rule position (r = 0.76, 0.90) and on content-preview binding, but we
  found it **blind to class-marker binding** (−0.503 behavioural vs +0.045 direct on
  identical prompts). Say this here, in two sentences. It bounds the mechanism's scope
  and it is why §7 makes no claim about class markers.

## 3. Advance exclusion fails, and the obvious explanations do not survive

### 3.1 The reversal

Lead with the twelve-model table and the two diffusion models. `Δ_time` negative in
all twelve; matched admit control flat. **Figure 1.**

### 3.2 The rule is held, and ignored

The declarative probe at 100% exactly-zero in both arms, against REI up to +0.64
prospectively. This is the sentence the paper is built on.

### 3.3 What it is not

Distance (no main effect; further helps), rule-to-evidence delay (intact to ~1,000
tokens in 4/6), bidirectional attention (largest asymmetry in Dream-7B), wording
(40/40 cells), inclusion implicature (rescues no model). Keep this compact: one
paragraph per account, one number each. These earn their place because each
predicts a different result and each was run to discriminate.

## 4. The failure is specific to complete suppression

The weight sweep, worded identically at every level. Pooled discontinuity
**+0.295 [+0.185, +0.405], p < 1e-4**. Report the honest caveat that the formal
kink term is identified in only two of six models while the descriptive pattern is
uniform.

Then the boundary condition: on an arithmetically implementable task the pre-post
gap is exactly 0.000 in four of five models. This is what makes the claim specific
rather than a general statement about future-directed instructions.

## 5. Binding decides it

The conceptual centre. **Figure 2.**

### 5.1 A named referent makes it worse

The L0–L5 ladder, uniform across six models, inverting the obvious prediction.

### 5.2 The rule binds to propositional content

The similarity ladder (four models) and the proposition relation matrix (two
models), with the duplicate control that separates rescue from redundancy — and the
metric change that confound forced.

### 5.3 A class marker carried on the evidence works prospectively

Lead with the tagged evidence-stream result: exact ground truth, five models, leakage
from 0.406–0.536 to ≈0 in **both** arms. That is the load-bearing evidence.

The single-item class-versus-specific comparison (five of six models in Stage 3A) is
reported as the weaker form, together with the fact that it did **not** replicate in
G16 under matched grammar, matched length and the mechanism readout: −0.11
[−5.62, +5.20]. Do not lead with it and do not omit the failure.

State the regularity here:

> An exclusion policy governs the decision when it can be resolved against the
> content it governs; a policy held as a pending intention about a named future
> item does not.

## 6. The same failure in an agent

`SYSTEM` policy → `TOOL` document → answer. The identifier-only system policy worth
nothing; the same policy after the tool output much better; suppression following
the proposition rather than the document ID when the content reappears as D9.

This section is short and it is the practical payoff. It is not a deployment study
and should not be written as one.

## 7. Mechanism — where the gating fails

**Figure 3.**

1. **Evidence-span gate.** Blocking downstream attention to the evidence span
   returns the answer to Base in both arms. The residual is carried by direct reads
   at and after the decision.
2. **Late resolution.** Answer-position patching: nothing below layer 18, 50% at
   21, ≈85% by 27 of 36.
3. **Binding state is exchangeable.** Matched-chronology, length-matched rule-span
   interchange transfers in both directions at layers 14–18.
4. **G16 did not close it, and the reason is a scope limit worth stating.** The
   tag/identifier interchange stopped at its preregistered bridge gate. Follow-up
   showed the cause is the fixed-position readout, not the construction: on identical
   prompts the behavioural readout gives −0.503 and the direct readout +0.045. The
   readout does track rule position and content-preview binding. Put this next to the
   readout description in §2, in two sentences, and repeat it in Limitations. What the
   paper claims is that *a* binding state is causally exchangeable between matched
   runs; class-marker binding is outside what this method can reach.

Report the Stage-5 correction — the first version of this analysis reported medians
of an unstable recovery fraction and overstated the effect — in the text, not
buried. It is short and it is what makes the rest credible.

## 8. Related work

Positive positioning, four neighbourhoods: human inadmissible-evidence and
instructed disregard; instruction following and instruction position; distraction
and irrelevant context; mechanistic accounts of contextualisation and competing
pathways. See `RELATED_WORK_2026.md`.

The positioning sentence:

> Prior work asks whether models follow instructions and whether irrelevant context
> distracts them. We ask whether a stated exclusion policy actually governs the
> decision, show that the answer depends on what the policy can bind to rather than
> on whether the model holds it, and trace the difference to a causally
> manipulable late gating state.

## 9. Discussion and limitations

What it means for agent policy design (attach policies to content or provenance,
not identifiers; a post-retrieval restatement is cheap and works), and for any
evaluation that assumes a stated constraint is an enforced one.

Limitations, compact: 10 independent legal skeletons; `procedural_hearsay` at 2
usable items; screening on Qwen3-8B only; mechanism on Qwen3-8B; external materials
are boundary checks, not a held-out tier; the effect is about soft evidential
integration.

## Figures

**Figure 1 — The reversal.** Same rule, two positions, twelve instruct models plus
two diffusion models; matched admit control flat. The reader should see the sign
flip without reading a number.

**Figure 2 — Binding.** One row per binding structure — named future identifier,
gist, content preview, class marker on the evidence — with leakage before and after.
The point is that the prospective bar collapses as binding becomes resolvable.

**Figure 3 — Where gating happens.** Span-gate bar (ungated vs gated, both arms),
the layer-wise patching curve, and the bidirectional interchange.

## Appendix

- full 12-model × 5-family tables and the cluster-robustness check;
- diffusion-model implementation notes (Dream's shift convention, mask block);
- the three failed readouts and why single-token rating readouts can anti-correlate
  with the model's own reasoning;
- ruling paraphrase tables (8 wordings × 5 models);
- Stage 3C alternative-account tests in full;
- the duplicate-control confound and the REI → rating-points metric change;
- the Stage-5 recovery-fraction correction;
- external boundary checks and their provenance correction;
- dataset limitations and the frozen-set screening caveat;
- the abandoned BTF-3 hindsight branch and the redaction-audit correction, as
  research history and data-integrity record only.
