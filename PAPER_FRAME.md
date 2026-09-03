# Paper frame — authoritative scientific register

**Updated:** 2026-09-03, after G18 confirmed the centrepiece regularity.
**Experimental programme: closed.** The remaining work is writing.

Historical development is in `RESEARCH_HISTORY.md`; the experiment ledger is
`EXPERIMENTS.md`; the consolidated snapshot is `STATUS.md`; full result tables are in
`PROSPECTIVE_EXCLUSION_FINDINGS.md` and `stages/`.

## 1. The question

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

A policy nearly always exists before the data it governs. A system prompt forbids a
source before retrieval runs; a court excludes evidence before the record is read; an
agent is told which memories are off-limits before any is fetched.

## 2. The claim

> **A policy can be available to the model without being addressable to the
> information it is supposed to govern.**

Prospective exclusion does not fail because the model forgets the rule, or because the
rule sits in the wrong place. It fails when, at the moment the rule is processed, the
model has no sufficiently specific *semantic* representation of what the rule is
about. Knowing that some future item must be ignored is not enough; what matters is
whether the model already knows **which content**.

## 3. Contribution 1 — the prospective exclusion gap

We preregistered the human ordering — from the inadmissible-evidence literature,
where an instruction to disregard arrives *after* the evidence and works poorly — and
found the reverse.

Across **12 instruction-tuned models from four vendors, two masked diffusion language
models, and five task families**, exclusion stated after the evidence is followed
well; the identical instruction stated before it is not. `Δ_time` is negative in all
twelve instruct models, ten of twelve intervals exclude zero, and the matched
*admitting* rule shows no order effect anywhere.

The models are not confused about the rule. Asked separately what weight the evidence
should receive, **every model answers exactly 0 on 100% of items, in both arms** — and
then, with the rule stated first, gives that evidence up to 0.64 of its normal causal
weight.

> **A model can hold a correct, fully stated exclusion policy and still route the
> excluded evidence into its decision.**

### What the gap is not

Four experiments localise it, and together they say something positive rather than
four negative things: whatever fails is not a property of the instruction or of where
it sits.

- **Not memory.** The declarative probe is at 100% in both arms; rule-to-evidence
  delay out to ~1,000 tokens leaves the gap intact in four of six models.
- **Not distance.** No main effect in any model; within the prospective arm, moving
  the rule *further* from the answer helps.
- **Not the causal mask.** The asymmetry survives in LLaDA-8B and Dream-7B, whose
  prompt attention is bidirectional; Dream shows the largest asymmetry measured.
- **Not one wording.** Eight ruling constructions, positive in 40 of 40 model ×
  wording cells; the counterfactual phrasing is the *worst* prospectively.

### One characterisation, not a section of its own

The gap is specific to demanding **exactly zero**: pooled discontinuity
**+0.295 [+0.185, +0.405]**, p < 1e-4, and it vanishes at every non-zero requested
weight. On a task where the requested contribution is arithmetically implementable it
disappears entirely — a pre-post gap of exactly **0.000** in four of five models.

This is a boundary condition and it is all it needs to be. The failure is not a
generic inability to follow future-directed instructions; it is about making
semantically integrated evidence causally inert.

## 4. Contribution 2 — target addressability decides it

This is the centre of the paper, and it is confirmed prospectively.

### The confirmation (G18)

One 6 × 3 factorial on **100 fresh items over 30 independent skeletons** — none of
which appears in the discovery set — across three families and five checkpoints from
four vendors. The later evidence is byte-identical across all six conditions; only the
**target representation** available when the rule is processed changes. Every level
carries its own no-rule baseline, so preview-induced redundancy is measured separately
from what the rule removes. Raw rating points; no ratio.

| target representation before the rule | ExclusionEffect (pooled) |
|---|---|
| a more specific statement that **entails** the evidence | **31.16 [27.99, 34.40]** |
| the same **proposition**, different words | **30.93 [28.19, 33.66]** |
| a referential stub naming the future item | 26.27 [23.65, 28.96] |
| unrelated content, length-matched | 22.06 [19.16, 24.97] |
| nothing | 21.84 [19.21, 24.66] |
| high lexical overlap, **different proposition** | 18.08 [15.71, 20.57] |

> **Δ_semantic = +8.91 [+7.15, +10.76]**, positive in **5 of 5** models.
> The length- and lexically-matched contrast, **para − empty = +12.85
> [+10.32, +15.42]**, positive in 5 of 5.

Reference is not enough, and surface similarity is worse than nothing.

### Why it is a semantic relation and not a string

The discovery rounds established the shape that G18 confirms. A rule that names a
future item is *worse* than never mentioning it, uniformly across six models, and no
partial stub recovers it. A semantically empty tag predicate (`if tag is Z9`) leaks
exactly as badly as an identity predicate (`if ID is E7`), which rules out local
checkability as the explanation. In the content × identity 2×2, **matching content
under the wrong label suppresses better than the right label with the wrong content**,
in all four models tested. The rescue is graded by entailment, not by lexical overlap.

### With a semantic target, exclusion follows the proposition

G18's decomposition adds a result the discovery rounds could not see. Under a
proposition-matched preview the rule drives the judgment **~28 points below the
preview-only baseline** — below where the model sat with the preview alone and no
evidence at all. The rule named the later block; the model discounts the content
wherever it appears.

`marg(exclude)` is negative in **5 of 5** models under `para` and positive in **5 of 5**
under `empty`. A lexically similar preview with the wrong proposition produces no such
drop, and neither does a referential stub.

## 5. Contribution 2, in an agent

`SYSTEM` carries the policy before retrieval, the document arrives in a `TOOL`
message, the assistant answers. The finding is **not** that identifiers never work —
in Gemma-3-12B and Qwen3.5-27B an identifier-only system policy does suppress. What
holds across all four models is sharper:

> When the same proposition arrives under a **different document identifier**, an
> identifier-only policy stops protecting against it, while a policy that stated the
> proposition suppresses the content under the new identifier almost as well as under
> the old one.

**Identifier policies are identifier-specific; semantic policies follow the
information across surface identity.** This is contribution 2 in a deployment shape,
and it is the practical payoff: a policy fixed before retrieval works if it attaches
to content or provenance, not to a name.

## 6. Contribution 3 — the causal mechanism

The mechanism targets the headline failure and is replicated across two architectures.

- **Excluded evidence is still read at the decision.** Blocking downstream attention
  to the evidence span returns the answer to Base: +0.46 → −0.12 prospectively,
  +0.32 → −0.08 retrospectively, p < 1e-4 both. A gating failure, not a comprehension
  failure.
- **Gating resolves late.** Answer-position patching recovers nothing below layer 18,
  50% at 21, ≈85% by 27 of 36.
- **The rule state depends causally on whether matching target content was available
  before the rule.** With chronology and length matched, the two runs differing only
  in whether the preview is a paraphrase of the evidence or an unrelated pad,
  rule-span interchange transfers in both directions:

| model | behavioural gap | window | break | rescue |
|---|---|---|---|---|
| Qwen3-8B (36 layers) | +13.2 [+8.6, +18.1] | L14–18, depth 0.39–0.50 | +13.3 [+8.1, +18.9] | −3.6 [−5.9, −1.4] |
| Mistral-Small-24B (40 layers) | +18.2 | L12–16, depth 0.30–0.40 | +15.7 | −13.4 |

> **A mid-network rule state carries whether the policy found a semantic target, and
> manipulating that state changes whether later evidence is suppressed.**

The overlapping mid-network window in two architectures is the invariant. Qwen's
weaker rescue relative to break does not generalise, and is reported as
model-specific rather than smoothed.

## 7. The arc

```text
Can a model commit in advance to ignore evidence it has not seen?
                ↓
No — and the reverse of the human ordering, while the model
states the required weight as exactly zero on 100% of items
                ↓
Not memory, distance, causal masking, or wording; strongest
where the demand is to make integrated evidence causally inert
                ↓
What decides it is whether the policy has a semantic target:
proposition and entailment work, reference and lexical
similarity do not — confirmed on fresh items and skeletons
                ↓
And in an agent, semantic policies follow the proposition
across document identity where identifier policies do not
                ↓
A mid-network rule state carries whether a target was found;
interchanging it changes later suppression, in two architectures
```

## 8. Scope and limits

- The confirmation covers three families, 30 skeletons, five checkpoints, four
  vendors. The 12+2-model headline breadth belongs to contribution 1; contribution 2's
  breadth is the G18 panel, and the paper says so rather than borrowing.
- `para − empty` does not exclude zero in Phi-4-mini (+3.50 [−1.06, +8.57]).
- `ExclusionEffect` does not measure the same thing at every level; at the semantic
  levels there is little evidence influence left to remove and the quantity is
  dominated by suppression below baseline. The decomposition is reported in the text.
- Mechanism is Qwen3-8B and Mistral-Small-24B.
- The fixed-position mechanism readout tracks rule position and content-preview
  binding but is blind to class-marker binding; that limitation is stated next to the
  readout, and it is why no mechanistic claim is made about class markers.
- Materials are controlled items plus a real `SYSTEM`/`TOOL` agent setting, not a
  naturally occurring corpus.

## 9. Naming discipline

The object is **advance commitment to ignore evidence**, and the explanatory variable
is **target addressability**. `Prospective binding failure` and `semantic target
grounding` are the technical names for the mechanism and belong in the body. Terms
from the abandoned hindsight frame do not appear in this paper.

## 10. Programme status

**Closed.** G18 confirmed the centrepiece under its frozen gates, and the
preregistration commits us to stopping there: no G19, no further models, no frontier
API, no mitigation study, no third mechanism model, no successor to G16 or G17.
