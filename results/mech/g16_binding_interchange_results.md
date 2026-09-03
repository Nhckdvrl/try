# G16 — binding-state interchange: **bridge-failed**

**Frozen design:** `preregistrations/PREREGISTRATION_G16_BINDING_INTERCHANGE.md`,
tags `g16-binding-interchange-design-v1` / `-v1.1` (Amendment A1, readout).
**Sources:** `results/mech/g16_freeze_checklist.json`, `g16_baselines.json`,
`g16_analysis.json`.

## Verdict

Gate 1 is a stopping rule and it failed. **The patched phase was not executed.**

| quantity | value |
|---|---|
| bridge `ExclusionEffect(cls) − ExclusionEffect(id)` | **−8.11 [−11.47, −5.07]** |
| gate 1 floor | +5.00, CI lower bound > 0 |
| n | 75 items, 15 clusters |

Under the frozen estimand the permitted claim is exactly one sentence: *the padded
2×2 construction did not reproduce the Stage 3A behavioural gap.* Nothing about
mechanism follows, in either direction.

## What happened — post-result diagnostic

Explicitly post-result; changes no gate and no verdict.

The frozen estimand anchors each arm on **its own** admit cell. That is only valid if
both admit cells actually restore full evidential weight. They do not:

| quantity | value |
|---|---|
| admit-anchor gap, `id_admit − cls_admit` (sign-aligned) | **+8.00 [+5.00, +10.82]** |

`cls_admit` tells the model that *an item marked as coming from an unauthorised
source carries the full decision weight of a verified item*. That is close to
self-contradictory, and the model does not comply: the tagged item stays discounted
by 8 points even under an admitting rule. The class arm's anchor therefore collapses
toward its own exclude cell, which shrinks `ExclusionEffect(cls)` to +2.91 for a
reason that has nothing to do with binding.

Re-scoring both arms against a **common** anchor — the estimator Stage 3A used —
removes the artifact:

| estimator | id-bound | class-bound | bridge |
|---|---|---|---|
| frozen, per-arm anchor | +11.01 [6.47, 16.14] | +2.91 [−0.83, 6.88] | −8.11 [−11.47, −5.07] |
| **common anchor (post-result)** | **+11.01 [6.47, 16.14]** | **+10.91 [5.57, 15.77]** | **−0.11 [−5.62, +5.20]** |

So the honest reading is **not** that the class-bound policy is worse. It is a
precise null: on these 75 items, with the mechanism readout, **the two policies
suppress equally**.

## Why — resolved by follow-up, and it is not the construction

Three differences from Stage 3A could have carried the null: readout, sample, or
G16's 17-token pad. Both follow-ups are zero-to-minimal cost and both are conclusive.

**Sample: excluded.** On G16's own two families the behavioural class advantage is
**−0.290 [−0.408, −0.164]** pooled over six models, slightly *larger* than in the
three families G16 omitted (−0.245 [−0.366, −0.126]). On Qwen3-8B alone it is
**−0.503 [−0.754, −0.249]**.

**Padding: excluded. Readout: confirmed.** Running Stage 3A's byte-identical prompts,
with no padding, through the direct readout reproduces the null:

| readout | `oe_L0` | `cls_pre` | class advantage |
|---|---|---|---|
| behavioural | 0.571 | 0.067 | **−0.503 [−0.754, −0.249]** |
| direct | 0.405 | 0.450 | **+0.045 [−0.124, +0.232]** |

**G16's construction was sound.** The mechanism readout is simply blind to this
contrast — see `results/mech/readout_validity_binding_results.md`. The direct readout
does track rule position (r = 0.76 / 0.90) and content-preview binding (Stage 5: +8.56
gap, −12.11 interaction); it is the class-marker form specifically that it misses,
plausibly because that advantage is expressed in deliberation.

**Consequences.** §5's class-marker claim rests on **Stage 3B**'s tagged stream —
exact ground truth, five models, both arms — which no readout question touches. The
mechanism section's scope is the position contrast and content-preview binding, and
it must say so.

## What was deliberately not done

The construction was **not** adjusted and re-run. The preregistration says a bridge
failure "is a fact about the instrument and must not be repaired by adjusting the
construction after the fact", and searching for the variant that restores the gap is
how a garden path starts. The diagnostic above uses only the 300 generations already
produced.

The follow-ups above were diagnostics on the instrument, not attempts to make the
bridge pass — and their outcome is the unfavourable one.

**There is no viable successor with this method.** Redoing the interchange under the
behavioural readout is not a compute problem but a methods problem: matched-chronology
interchange requires aligned token positions, and a generated rationale differs per
condition and per item. No successor is scheduled.

## Volume

300 baseline generations (75 items × 4 conditions). Zero patched generations. One
GPU, one checkpoint.
