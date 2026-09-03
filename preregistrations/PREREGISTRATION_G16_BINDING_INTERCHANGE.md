# G16 preregistration — is prospective binding one causally exchangeable state?

**Created:** 2026-09-03, before any G16 generation or activation capture.
**Status:** DRAFT — not frozen. This document authorises nothing until it is
committed and tagged `g16-binding-interchange-design-v1`. No target model may be
run against these conditions before that tag exists.

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

This is one experiment answering one question. It is not a control, and no
further round is planned regardless of its outcome.

## 2. Conditions — the only manipulated variable is what the policy binds to

Both conditions state the policy **before** the evidence, use the frozen 144-item
set, and share chronology. From `src/conditions_v3.py`:

| condition | policy | evidence block |
|---|---|---|
| `id_pre` (FAILURE) | `Evidence E7 has decision weight 0` | untagged |
| `cls_pre` (SUCCESS) | `Any item in this file marked as coming from an unauthorised source …` | carries `[source: unauthorised]` |

The two prompts differ by the policy sentence and by the presence of the tag on the
evidence header. The tag string is short and fixed; the policy sentences are **not**
length-matched by construction, so a token-length-matched filler is inserted into
`id_pre` so the two runs match to within a tolerance fixed here: **≤ 4 tokens per
item**, using the existing `filler_block` from `src/conditions_v2.py`. Items whose
matched pair exceeds the tolerance are dropped before any output is inspected, and
the dropped list is reported.

A matched **admitting** arm (`id_pre_admit`, `cls_pre_admit`) is run for both, so the
quantity of interest is the 2×2 interaction rather than a raw difference that a tag
alone could produce.

## 3. Model, families, readout — all inherited unchanged

Qwen3-8B at the revision already used for the mechanism work; families
`legal_judgment` + `evidence_inference`, the two where the fixed-position readout
tracks the behavioural one (item-level r = 0.76, 0.90); the greedy two-sentence
rationale followed by the digit-expectation readout at a fixed position; the
cluster bootstrap over case skeletons at seed `20260829` with 10,000 resamples.
Runner: `src/mech/patch_matched.py`, unmodified except for the condition pair.

## 4. Patch sites and layers, fixed in advance

Semantic positions present in both runs, from the existing `SITES` list:
`rule_end`, `rule_span`, `evidence_end`, `answer`.

`rule_end` is the primary site and the reason the experiment is worth running: at
that position the evidence has not been read yet, so anything transferred there is a
state the *policy* established, not a re-reading of the evidence.

Layers: every fourth decoder layer, `[4, 8, 12, 16, 20, 24, 28, 32]`, plus layers
14 and 18 because Stage 5's matched interchange peaked at 14–18. No layer is added
after seeing results.

## 5. Estimands

All in sign-aligned rating points, on items with a behavioural gap of at least 2
points, pooled as in Stage 5.

- **Bridge.** `ExclusionEffect(cls_pre) − ExclusionEffect(id_pre)`, the behavioural
  gap the interchange must transfer.
- **Break.** `cls_pre` receives `id_pre`'s state at site `s`, layer `l`. Positive =
  moved toward leakage.
- **Rescue.** `id_pre` receives `cls_pre`'s state. Negative = moved toward
  suppression.
- **Admit control.** The same interchange in the admitting arm, which should be near
  null.
- **Direction control.** Interchange along a deterministic matched-norm direction
  orthogonal to the empirical difference, at the same site and layer.

## 6. Gates, frozen

`confirmed-binding-state` requires **all** of:

1. **bridge** ≥ 5 rating points with bootstrap CI lower bound > 0;
2. **bidirectionality** — break > 0 and rescue < 0, each with a CI excluding zero,
   at a common (site, layer);
3. **magnitude** — |break| ≥ 3 rating points at that (site, layer);
4. **adjacency** — the same sign pattern at a neighbouring layer;
5. **specificity** — at the strongest qualifying (site, layer), the effect minus the
   orthogonal-direction effect has a CI excluding zero, and the admit-arm effect
   does not itself clear gate 3.

If gates 1–5 pass at `rule_end`, the verdict is
`confirmed-binding-state-established-by-policy`. If they pass only at
`evidence_end` or `answer`, the verdict is `confirmed-binding-state-late-only`,
which is a weaker and different claim and must be reported as such.

Anything else is `not-established`. A failed G16 is reported as a failed G16; the
behavioural programme does not depend on it, and the paper's mechanism section
falls back to Stage 5 plus the span gate.

## 7. What may be claimed under each verdict

| verdict | permitted claim |
|---|---|
| `…established-by-policy` | The policy establishes a state before the evidence is read whose interchange transfers prospective suppression in both directions. |
| `…late-only` | The two policies differ in a late state at or after the evidence, exchangeable in both directions. No claim about when the state is established. |
| `not-established` | The tested one-dimensional interchange does not transfer the tag/identifier difference at the tested sites and layers. No claim that no such state exists. |

## 8. Volume and cost

144 items × 2 policies × 2 admissibility arms = 576 baseline generations, plus
2 directions × 4 sites × 10 layers × the qualifying item subset for patched runs.
Single checkpoint, single node, one GPU. No new dataset, no new model, no
new annotation.

## 9. Freeze checklist

- [ ] condition pair and filler tolerance implemented and unit-tested on prompts only
- [ ] item drop list produced from prompts alone, before any generation
- [ ] this document committed and tagged `g16-binding-interchange-design-v1`
- [ ] only then: baselines, then patched runs
