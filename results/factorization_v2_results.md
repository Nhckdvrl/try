# G1 factorization v2 — results

**Tag:** `g1-factorization-v2` (commit `2383901`, confirmed to exist before
any model output — the process gap disclosed in v1 was not repeated). All
6 new runs (2 conditions × 3 models: `m1_before`, `m2v2`) executed
cleanly, 128 rows each, 0 parse failures. `REPEAT-AFTER` reuses v1's
already-collected `m1` results unchanged, as preregistered.

## Headline result: outcome combination 3 (of the four preregistered)

```
PositionalEffect: 2/3 models (Qwen, Gemma) -> VALIDATED
M2-v2:            1/3 models (Gemma only)  -> not validated
```

Per `PREREGISTRATION_G1_FACTORIZATION_V2.md`'s stop/go rule, this is
outcome **3**: *"`PositionalEffect` CI lower bound > 0, but `M2-v2` not
validated: the positional/overwriting account is strengthened as the
paper's mechanism story; partitioning is reported as not (yet) an
effective mitigation, without further redesign in this document."*

## Priority 1 — M1 positional control: VALIDATED, clean

| model | PositionalEffect mean [95% CI] | boundary acc (before/after) | position matters |
|---|---|---|---|
| Qwen3.5-9B | 5.31 [2.73, 8.00] | 1.00 / 1.00 | **yes** |
| Gemma-3-12B-it | 9.72 [6.03, 13.75] | 1.00 / 0.97 | **yes** |
| Mistral-Small-24B | -0.70 [-2.11, 0.63] | 1.00 / 1.00 | no |

`PositionalEffect = Intrusion_REPEAT-BEFORE - Intrusion_REPEAT-AFTER`. In
both models that showed baseline intrusion, the identical reminder text
is significantly more effective placed *after* the future evidence than
*before* it — the 95% CI excludes zero cleanly for both, and by a wide
margin for Gemma (9.72, roughly 2/3 of its v1 `M1` reduction of 13.97 is
attributable specifically to position, not repetition alone). Mistral,
which never showed baseline intrusion, correctly shows no positional
effect either (CI straddles zero, point estimate near zero) — exactly
the selective pattern that distinguishes a real mechanism from a
processing artifact. Boundary-probe accuracy stays at or near 1.00 in
both conditions for all three models, so this is not explained by one
position confusing comprehension more than the other.

**This directly answers the reviewer objection the design was built to
pre-empt.** It is not merely true that "repeating the instruction helps"
— *where* the repetition sits relative to the inadmissible evidence
matters, and matters in the direction the displacement/overwriting
account predicts: an exclusion rule stated only before the evidence
loses behavioral control after the evidence arrives; restating it after
partially restores that control. `M1`'s v1 result can now be reported as
a genuine partial mechanism finding, not just an effective mitigation of
unknown origin.

## Priority 2 — M2, corrected: partially replicates, not validated at 2/3

| model | Delta_M2v2 mean [95% CI] | boundary acc | meaningfully reduces |
|---|---|---:|---|
| Qwen3.5-9B | -1.88 [-4.84, 0.83] | 1.000 | no |
| Gemma-3-12B-it | 6.72 [2.92, 10.66] | 1.000 | **yes** |
| Mistral-Small-24B | -0.31 [-2.19, 1.48] | 1.000 | no |

The fix worked exactly as diagnosed: boundary-probe accuracy is 1.000 for
all three models this time (vs. 0.0–0.5 in v1's broken implementation),
confirming the missing framing paragraph was indeed the root cause of
v1's failure — this is now a genuine, valid test of temporal
partitioning, not an artifact of a broken prompt. Gemma shows a real,
meaningful reduction (6.72 points, about half its baseline intrusion of
27.2). Qwen shows no reduction (point estimate is actually slightly
negative, CI comfortably includes zero) and Mistral is unaffected as
expected. **1 of 3 models clears the bar — below the preregistered 2-of-3
threshold, so `M2-v2` is not validated as a general partial mechanism**,
though it is not a clean null either: explicit temporal partitioning
helped exactly the model with the largest baseline intrusion, just not
the other one.

## What this establishes for the paper

Per the preregistered stop/go rule (outcome 3): the project's depth
contribution now rests on a genuinely mechanistic result, not a bare
mitigation. The reportable story is:

> Models recognize the temporal boundary (boundary-probe accuracy ≈100%
> throughout every condition tested) but fail to enforce it
> (`OutOfSetIntrusion` significantly positive in 2/3 models). This
> failure is position-sensitive: the same exclusion rule, repeated
> verbatim, is significantly less effective when stated only before the
> inadmissible evidence than when restated after it (`PositionalEffect`
> validated in 2/3 models, matching exactly the two models that show
> baseline intrusion). Explicit temporal partitioning of admissible and
> inadmissible evidence reduces contamination in one of those two models
> but not the other, and is reported as a partial, not general,
> mitigation.

No manipulation is redesigned or re-run within this document, per the
preregistration's own discipline. `M3` remains deferred, as
preregistered — its redesign (non-numeric evidence-state
externalization) is out of scope here.
