# Paper frame — authoritative scientific register

**Updated:** 2026-09-03
**Status:** this frame replaces the BTF-3 hindsight frame, which was stopped on
2026-09-03. See `RESEARCH_HISTORY.md` for why, and
`SECOND_LEAD_EXPLICIT_OUTCOME_PARADOX.md` for the one hindsight result that is
kept as a separate, unconfirmed lead.

Historical development is in `RESEARCH_HISTORY.md`; experiment bookkeeping is in
`EXPERIMENTS.md`; the full result tables are in `PROSPECTIVE_EXCLUSION_FINDINGS.md`
and `stages/`.

## 1. The question

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

This is an ordinary situation, not a benchmark construct. A policy almost always
exists before the data it governs arrives:

- a system prompt forbids using unauthorised sources, and retrieval happens later;
- a court rules evidence inadmissible before the record is read out;
- an agent is told which memories or tools are off-limits before any of them is
  fetched;
- a reviewer is told to disregard information that will appear later in a file.

In every case the instruction precedes its target. The scientific object is
**whether a stated exclusion policy actually governs the decision**, and what
determines when it does.

## 2. The headline finding

The prediction we preregistered — from the human literature on inadmissible
evidence, where an instruction to disregard arrives *after* the evidence and works
poorly — was that post-evidence exclusion would be the hard case.

**It reversed.** Across 12 instruction-tuned models from four vendors, plus two
masked diffusion language models, on 144 frozen items spanning five task families:

> **Telling a model to ignore evidence *after* it has read it works well.
> Telling it the same thing *before* the evidence arrives does not.**

`Δ_time` (post minus pre) is negative in all twelve instruct models and ten of
twelve intervals exclude zero. Under a matched *admitting* rule, order does not
matter anywhere.

The models are not confused about the rule. Asked separately what weight the
evidence should receive, **every model answers exactly 0 on 100% of items, in both
arms** — and then, with the rule stated first, gives that same evidence up to 0.64
of its normal causal weight.

> **A model can hold a correct, fully stated exclusion policy and still route the
> excluded evidence into its decision.**

## 3. What the failure is not

Four candidate explanations are ruled out by experiments that were run to
discriminate, not to defend:

- **Not memory or retrieval.** The declarative policy probe is at 100% in both
  arms, and rule-to-evidence delay out to ~1,000 tokens leaves the gap intact in
  four of six models. This separates the effect from prospective-memory failure,
  which asks whether the model remembers to act at all.
- **Not distance or recency.** Rule-to-answer distance has no main effect in any
  model; within the prospective arm, moving the rule *further* from the answer
  helps. A rule 587 tokens away but placed after the evidence beats a rule 156
  tokens away placed before it.
- **Not the causal mask.** The asymmetry survives in LLaDA-8B and Dream-7B, whose
  prompt attention is bidirectional. Dream shows the largest asymmetry measured.
- **Not one wording, and not inclusion implicature.** Eight ruling constructions
  give a positive gap in 40 of 40 model × wording cells; the counterfactual
  phrasing is the *worst* prospectively. An explicit presentation policy stating
  that display does not imply relevance rescues no model.

## 4. Sharper regularity — the failure is specific to complete suppression

One identical sentence at every level, so prohibition and attenuation are worded
the same way: *"The causal weight assigned to X is exactly w% of its normal
evidential weight."*

The pre-minus-post gap is large at `w = 0` and vanishes everywhere else. Pooled
over models with a cluster bootstrap over (model × case skeleton):

> (gap at w=0) − (mean gap over the eight non-zero weights)
> = **+0.295 [+0.185, +0.405], p < 1e-4** (n = 422 item-model pairs)

On Qwen3-8B the ratio `gap(0)/gap(1%)` is a factor of **38**. The sharpest reading
is within a column: retrospectively a model treats "exactly 0" as categorical,
prospectively it does not. **Zero registers as special only once its target
exists.**

The boundary condition is equally informative. On a task where an item's
contribution is stated arithmetically and is therefore actually implementable,
prospective nullification is **perfect** — a pre-post gap of exactly 0.000 in four
of five models. The failure is about gating soft evidential integration, not about
binding rules to future objects in general.

## 5. The explanatory variable — what the policy can bind to

This is the conceptual centre of the paper.

**A named future referent is not enough, and makes things worse.** Holding the rule
identical and varying only how much of its target exists when it is stated: never
mentioning the object is *better* than announcing it, and adding the item's type or
even its direction does not recover. This inverts the obvious prediction and is
uniform across all six models tested. Only presenting the content first is reliably
good.

**What the rule binds to is propositional content, not a string and not a topic.**
A preview of the evidence before the rule restores suppression, and the rescue is
ordered by entailment rather than by surface form. `ExclusionEffect` is the rating
points the rule removes on top of whatever the preview already did, so the
redundancy a preview creates on its own is held separate (two models, 75 items):

| relation of preview to the actual evidence | Qwen3-8B | Gemma-3-12B |
|---|---|---|
| preview entails the evidence (more specific) | **+29.4** | **+18.7** |
| mutual entailment (true paraphrase) | **+27.1** | **+15.2** |
| evidence entails the preview (gist only) | +14.1 | +8.4 |
| polarity reversed | +15.6 | +1.6 (n.s.) |
| one argument changed | +9.3 | +4.0 |
| high lexical overlap, different meaning | +9.6 | +1.2 (n.s.) |
| unrelated | +9.0 | +8.5 |
| no preview | +8.0 | +9.4 |

What both models share is the part that matters: the two entailment relations sit
far above everything else, and surface similarity without shared meaning sits at or
below the no-preview baseline. The middle rows differ — Qwen keeps a substantial
effect under polarity reversal where Gemma has none — and that difference is
reported, not smoothed. In the earlier four-model similarity ladder the same
ordering (`exact ≈ paraphrase > entailing summary ≈ 0 > same-direction different
fact`) holds in all four models tested.

A separate duplicate control shows that the redundancy a preview creates on its own
runs the *opposite* way — a repeated fact keeps only 6–18% of its marginal weight
with no rule involved — so the rescue is not second-presentation decay. Finding
that confound, and moving the metric from a ratio to raw rating points because of
it, is part of the record.

**A policy carried on the evidence itself is executed prospectively.** When the
policy names a class and the class marker travels with each item — `[unverified]`
printed on the evidence block — leakage falls from 0.48 with no policy to
approximately zero, **in both arms**, across five models. The prospective case
stops being the broken one.

> **An exclusion policy governs the decision when it can be resolved against the
> content it governs; a policy that must be held as a pending intention about a
> named future item does not.**

## 6. It is the same failure in an agent

The vignette result transfers to real chat roles: `SYSTEM` carries the policy, the
document arrives later in a `TOOL` message, the assistant then answers.

- A system-level identifier policy — the highest-authority, persistent instruction
  the interface offers — is worth **nothing** in two of three models (+1.014 vs
  +0.991 with no policy at all).
- Delivering the identical policy after the tool output is much better in all three.
- **Suppression follows the proposition, not the identifier.** When the same content
  arrives under a different document ID, an ID-only policy is helpless while a
  policy that stated the proposition still suppresses it.

This is where the finding matters practically: the agent case, in which the policy
is necessarily fixed before retrieval, is the *solvable* one — provided the policy
attaches to content or provenance rather than to an identifier.

## 7. Mechanism — where the gating fails

The mechanism answers the headline failure rather than sitting beside it
(Qwen3-8B, 75 items from the two families where a fixed-position readout tracks the
behavioural one).

**The excluded evidence is still read at the decision.** Blocking every query
position downstream of the evidence from attending to the evidence span returns the
answer to Base: REI +0.46 → −0.12 prospectively, +0.32 → −0.08 retrospectively,
p < 1e-4 both. Cutting that one path removes the entire residual influence. This is
a decision-gating failure, not a comprehension failure.

**The gating decision is made late.** Answer-position patching recovers none of the
pre/post gap below layer 18, reaches 50% at layer 21 and ≈85% by layer 27, of 36.

**The binding state is causally exchangeable.** With chronology and token length
matched — the two runs differ only in whether the preview before the rule is a
paraphrase of the evidence or an unrelated pad — rule-span interchange transfers in
both directions at layers 14–18: failure → success **+13.3 [+8.1, +18.9]** rating
points, success → failure **−3.6 [−5.9, −1.4]**, against a near-null admit arm.

## 8. The one experiment still worth running

Section 7 shows the binding state can be exchanged between a bound and an unbound
*preview* condition. It does not yet show the same for the two structures the paper
actually contrasts: a policy bound to a named future identifier versus a policy
bound to a class marker carried on the evidence.

> **G16.** Interchange the late rule/evidence binding state between the tag-bound
> and identifier-bound conditions, in both directions, with matched chronology,
> matched length, and a matched control direction.

If tag-bound → identifier-bound removes the prospective leakage and the reverse
restores it, the mechanism closes on the headline: the difference between a policy
that works before the evidence and one that does not is a specific, causally
manipulable internal state.

That is one experiment answering one question. It is not a control battery, and no
further model, prompt, benchmark or mitigation round is planned.

## 9. The explanatory arc

```text
Can a model commit in advance to ignore evidence it has not seen?
                ↓
No — and the reverse of the human pattern: exclusion after the
evidence works, exclusion before it fails, while the model states
the policy perfectly in both cases
                ↓
Not memory, not distance, not the causal mask, not wording
                ↓
The failure is specific to driving a contribution to exactly zero,
and disappears when the contribution is arithmetically implementable
                ↓
What decides it is what the policy can bind to: a named future
referent fails, propositional content and evidence-carried class
markers succeed — in vignettes and in an agent
                ↓
The excluded evidence is still read at the decision, gating happens
late, and the binding state can be causally exchanged
```

## 10. Scope

- 144 frozen items over five task families, built from 10 independent legal case
  skeletons; the `procedural_hearsay` arm collapsed to 2 usable items and is
  effectively untested.
- Item screening was performed on Qwen3-8B alone; the frozen set transfers well
  (133–144 of 144 usable on every other model) but was not screened on them.
- The mechanism is established on Qwen3-8B.
- The external Ramsey and Baron-Hershey/Aiyer materials are **boundary checks**,
  not an independently authored held-out tier.
- The effect is about soft evidential integration; where a contribution is
  explicitly computable, prospective nullification is exact.

## 11. Naming discipline

The paper's object is **advance commitment to ignore evidence**. `Prospective
binding failure` is the low-level technical name for the mechanism and belongs in
methods and analysis, not in the title or introduction. Terms from the abandoned
frames — `information set`, `out-of-set intrusion`, `retrospective outcome
entrainment`, `recipient-conditioned decision state` — do not belong in this paper
at all.
