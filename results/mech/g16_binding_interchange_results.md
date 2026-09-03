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

## What this costs the paper

The Stage 3A class-versus-specific comparison did **not** reproduce here. Three
differences from Stage 3A could carry that, and this round cannot separate them:

1. **Readout.** Stage 3A used the behavioural two-sentence-rationale readout; this
   used the fixed-position direct readout (item-level r = 0.76 / 0.90 — good, not 1).
2. **Sample.** Stage 3A pooled all 144 items across five families; this is 75 items
   in the two families where the direct readout is validated.
3. **Padding.** The identifier arm carries a 17-token clerical block upstream of the
   rule; Stage 3A's specific arm did not.

**The claim in `PAPER_FRAME.md` §5 must be narrowed accordingly.** The strong
evidence that an evidence-carried class marker works prospectively is **Stage 3B**,
not Stage 3A: the tagged evidence stream has exact ground truth, five models, and
leakage falling from 0.406–0.536 with no policy to ≈0 in **both** arms. That result
is untouched by this round. The Stage 3A single-item class-versus-specific
comparison is the weaker evidence for the same claim, and it now has a failed
same-family, length-matched replication against it.

## What was deliberately not done

The construction was **not** adjusted and re-run. The preregistration says a bridge
failure "is a fact about the instrument and must not be repaired by adjusting the
construction after the fact", and searching for the variant that restores the gap is
how a garden path starts. The diagnostic above uses only the 300 generations already
produced.

Any successor experiment must be preregistered separately, must state up front which
of the three differences it is testing, and should use the Stage 3B tagged-stream
contrast — which is robust across five models with exact ground truth — as its
behavioural bridge rather than the Stage 3A comparison that just failed to replicate.

## Volume

300 baseline generations (75 items × 4 conditions). Zero patched generations. One
GPU, one checkpoint.
