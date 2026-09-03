# G16 preregistration — is prospective binding one causally exchangeable state?

**Created:** 2026-09-03. Written and frozen before any G16 generation or activation
capture. The prompt-only freeze checklist below was run with the tokenizer alone; no
model weights were loaded and no output was produced.

**Freeze tag:** `g16-binding-interchange-design-v1`. Nothing in this design may be
changed after that tag exists.

## 1. The question

The behavioural programme establishes that an exclusion policy stated before the
evidence governs the decision when it can be resolved against the content it
governs, and does not when it names a future item. Stage 5 shows that a *binding
state* is causally exchangeable — but between a paraphrase-preview run and an
unrelated-preview run, which is not the contrast the paper is built on.

G16 asks the closing mechanistic question directly:

> **Is the difference between an identifier-bound and a class-bound prospective
> policy carried by a specific internal state that can be interchanged in both
> directions?**

This is one experiment answering one question. It is not a control, and no further
round is planned regardless of its outcome.

## 2. Conditions — the exclusion grammar is held fixed

All four conditions state the policy **before** the evidence, share the background
block and `ID_PREAMBLE`, and carry byte-identical evidence content. Both exclusion
rules use the same `has decision weight 0` predicate, so the manipulated variable is
the binding structure and not the wording of prohibition.

| condition | RULING block | evidence header |
|---|---|---|
| `id_exclude` (FAILURE) | `Evidence E7 has decision weight 0.` | `EVIDENCE E7` |
| `cls_exclude` (SUCCESS) | `Any item in this file marked as coming from an unauthorised source has decision weight 0.` | `EVIDENCE E7 [source: unauthorised]` |
| `id_admit` | `Evidence E7 has the full decision weight of a verified item.` | `EVIDENCE E7` |
| `cls_admit` | `Any item in this file marked as coming from an unauthorised source has the full decision weight of a verified item.` | `EVIDENCE E7 [source: unauthorised]` |

The two admitting rules are written here to parallel the exclusion rules'
construction exactly. They are therefore **new strings**, not `conditions_v2.ID_ADMIT`,
and this round's admit anchor is not byte-comparable to earlier rounds' anchors. That
is a deliberate choice — a matched 2×2 needs matched grammar in all four cells — and
it is recorded rather than left implicit.

### Length matching

The class arm is longer by a constant **17 tokens** (longer rule plus the tag). The
identifier arm is padded with the frozen clerical filler (`conditions_v2.filler_block`
at `stable_seed(item_id)`), truncated at token granularity and decoded — the same
construction Stage 5 used. The pad sits in its own `ADMINISTRATIVE RECORD` block
**upstream of the rule**, so it can never come between the policy and the evidence it
governs. Token-level truncation can cut a final word; this is accepted, matches the
Stage 5 precedent, and is controlled by the admit arm.

The pad budget is solved against the assembled prompts rather than estimated, to at
most 8 iterations per item.

### Frozen sample — `results/mech/g16_freeze_checklist.json`

Families `legal_judgment` + `evidence_inference`, the two where the fixed-position
readout tracks the behavioural one (item-level r = 0.76, 0.90).

| quantity | value |
|---|---|
| items considered | 75 |
| **items kept** | **75** |
| items dropped for length | **0** |
| tolerance | ±4 tokens |
| residual gap after padding | 0–1 tokens (exclude and admit arms) |
| site-resolution failures | 0 |
| prompt length range | 225–364 tokens |

Because the pad is upstream, `evidence_end` lands at the **same absolute token index**
in both arms; `rule_end` differs by construction, which is why the patch sites are
semantic rather than positional.

## 3. Model, readout, statistics — inherited unchanged

Qwen3-8B at the revision already used for the mechanism work. Cluster bootstrap over
case skeletons, seed `20260829`, 10,000 resamples. Runner
`src/mech/binding_interchange.py`, built on the unmodified `patch_matched.py` design.

**Readout — see Amendment A1.** The mechanism readout is the fixed-position
`ANSWER_FORMATS["direct"]` one-token digit expectation, not the behavioural
two-sentence-rationale readout.

### Amendment A1 — readout, made before any generation

**2026-09-03, after tag `g16-binding-interchange-design-v1`, before any G16 model
output exists.**

Section 3 as first frozen described the readout as "greedy two-sentence rationale
followed by the digit-expectation readout at a fixed position". That is the
*behavioural* readout used in G0 and the stage rounds. Every mechanism experiment in
this project — the span gate, the answer-position patching curve, and Stage 5's
matched interchange — uses the fixed-position `ANSWER_FORMATS["direct"]` one-token
digit expectation instead, which was validated against the behavioural readout on
exactly these two families (item-level r = 0.76 and 0.90,
`results/mech/direct_readout.json`).

G16 uses the direct readout, so that its numbers are comparable to Stage 5 and to
the span-gate analysis. The original sentence was a drafting error, not a design
choice, and correcting it makes G16 consistent with the rounds it must be read
against.

This amendment is recorded rather than applied silently, and it is made while the
generation count for this round is still zero. Tag `g16-binding-interchange-design-v1.1`
supersedes `-v1`; the v1 tag is retained so the original text stays recoverable.

## 4. Patch sites and layers, fixed in advance

Sites, all present in both arms: `rule_end`, `rule_span`, `evidence_end`, `answer`.

`rule_end` and `rule_span` are the primary sites and the reason the experiment is
worth running: at those positions the evidence has not been read yet, so anything
transferred there is a state the *policy* established.

Layers: `[4, 8, 12, 16, 20, 24, 28, 32]`, plus `14` and `18` because Stage 5's
matched interchange peaked at 14–18. Ten layers of 36. No layer is added after seeing
results.

## 5. Estimands

Sign-aligned rating points, on items with a behavioural gap of at least 2 points,
pooled as in Stage 5.

- **Bridge.** `ExclusionEffect(cls_exclude) − ExclusionEffect(id_exclude)`, where
  `ExclusionEffect` is measured against that arm's own admit anchor. This is the gap
  the interchange must transfer.
- **Break.** `cls_exclude` receives `id_exclude`'s state at site *s*, layer *l*.
  Positive = moved toward leakage.
- **Rescue.** `id_exclude` receives `cls_exclude`'s state. Negative = moved toward
  suppression.
- **Admit control.** The same interchange between `id_admit` and `cls_admit`.
- **Direction control.** Interchange along a deterministic matched-norm direction
  orthogonal to the empirical difference, at the same site and layer.

## 6. Gates, frozen

`confirmed-binding-state` requires **all** of:

1. **bridge** ≥ 5 rating points with bootstrap CI lower bound > 0;
2. **bidirectionality** — break > 0 and rescue < 0, each with a CI excluding zero, at
   a common (site, layer);
3. **magnitude** — |break| ≥ 3 rating points at that (site, layer);
4. **adjacency** — the same sign pattern at a neighbouring tested layer;
5. **specificity** — at the strongest qualifying (site, layer), the effect minus the
   orthogonal-direction effect has a CI excluding zero, and the admit-arm effect does
   not itself clear gate 3.

If gates 1–5 pass at `rule_end` or `rule_span`, the verdict is
`confirmed-binding-state-established-by-policy`. If they pass only at `evidence_end`
or `answer`, the verdict is `confirmed-binding-state-late-only`, which is a weaker and
different claim and must be reported as such.

Anything else is `not-established`. A failed G16 is reported as a failed G16; the
behavioural programme does not depend on it, and the paper's mechanism section falls
back to Stage 5 plus the span gate.

**Gate 1 is a stopping rule.** If the bridge fails, the patched runs are not executed
and the round is reported as `bridge-failed` — the padded 2×2 did not reproduce the
Stage 3A behavioural difference, which is a fact about the instrument and must not be
repaired by adjusting the construction after the fact.

## 7. What may be claimed under each verdict

| verdict | permitted claim |
|---|---|
| `…established-by-policy` | The policy establishes a state before the evidence is read whose interchange transfers prospective suppression in both directions. |
| `…late-only` | The two policies differ in a late state at or after the evidence, exchangeable in both directions. No claim about when the state is established. |
| `not-established` | The tested one-dimensional interchange does not transfer the tag/identifier difference at the tested sites and layers. No claim that no such state exists. |
| `bridge-failed` | Nothing about mechanism. The padded construction did not reproduce the behavioural gap. |

## 8. Volume

75 items × 4 conditions = **300 baseline generations**. Patched runs: 2 directions ×
4 sites × 10 layers over the qualifying item subset, plus the orthogonal control at
the strongest qualifying (site, layer). Single checkpoint, one GPU, no new dataset,
no new annotation.

## 9. Freeze checklist

- [x] condition pair and filler tolerance implemented and exercised on prompts only
- [x] item drop list produced from prompts alone, before any generation
      (`results/mech/g16_freeze_checklist.json` — 75/75 kept, 0 dropped)
- [x] site resolution verified in all four conditions for every kept item
- [ ] this document committed and tagged `g16-binding-interchange-design-v1`
- [ ] only then: baselines, gate 1, then patched runs
