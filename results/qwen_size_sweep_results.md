# Qwen3.5 within-family size analysis — results

**Design tag:** `g2-qwen-size-sweep-design-v1` (frozen before any new
checkpoint produced output). Analysis:
`results/qwen_size_sweep_analysis.json`.

Named as preregistered: **within-family size analysis across the available
dense Qwen3.5 checkpoints (4B, 9B, 27B)**. `Qwen3.5-2B` was preregistered but
unavailable in the frozen offline environment, and the run script skipped it
by that rule, not by choice after seeing results. This is not a scaling study
and no scaling law is fitted.

All three sizes ran the frozen 256-unit artifact (SHA-256 `0b6fd8d0…acf0901d`)
through the unchanged runner: same prompts, decoding, parser, thresholds, and
estimator. 9B is the existing large-replication output, reused rather than
re-run. Longest prompt 4,445 tokens; **0 decision-parse and 0 probe-parse
failures at every size**.

## Per size

| size | revision | parse | boundary recognition | responsiveness | `OutOfSetIntrusion` (95% CI) | qualified | intrusion pass |
|---|---|---|---|---|---|---|---|
| 4B | `851bf6e8…` | 1024/1024 | **99.61%** | 41.50 [36.77, 46.15] | **32.00 [28.40, 35.65]** | yes | **yes** |
| 9B | `c2022362…` | 1024/1024 | **99.22%** | 47.27 [45.04, 49.48] | **16.02 [14.18, 17.89]** | yes | **yes** |
| 27B | `fc05daec…` | 1024/1024 | **100.00%** | 41.01 [37.43, 44.60] | **36.75 [33.50, 39.93]** | yes | **yes** |

Aligned `ALLOWED_WITH` is 100.00 / 99.96 / 100.00 — all three sizes use the
licensed evidence essentially perfectly.

## Paired size contrasts (same 256 questions)

| contrast | Δ intrusion (95% CI) | Δ boundary accuracy |
|---|---|---|
| 9B − 4B | **−15.98 [−19.39, −12.58]** | −0.39 pp |
| 27B − 9B | **+20.73 [+17.41, +24.06]** | +0.78 pp |
| 27B − 4B | **+4.75 [+0.73, +8.71]** | +0.39 pp |

## What this shows

1. **Scale does not remove the failure.** Every size qualifies and every size
   clears the 5-point SESOI. The largest checkpoint is the *most* contaminated
   one (36.75), and the 27B − 4B contrast is positive, not negative.
2. **The trend is non-monotone.** 32.00 → 16.02 → 36.75, with both adjacent
   contrasts large and their intervals far from zero. With three size points
   and one family, no story is fitted to this shape; it is reported as a
   non-monotone within-family trend. The 9B checkpoint is the outlier, not the
   endpoint of a decline.
3. **Recognition is saturated everywhere while enforcement is not.** Boundary
   accuracy is 99.2–100% at 4B, 9B and 27B — it has no room to vary — while
   intrusion moves across a 20-point range at the same time. Recognition and
   enforcement clearly do not track each other within this family.

## Permitted claim

> Across the available dense Qwen3.5 checkpoints (4B, 9B, 27B) on the same 256
> questions, boundary recognition is saturated (99.2–100%) at every size while
> out-of-set intrusion varies non-monotonically from 16.0 to 36.8 points, with
> the largest checkpoint the most contaminated. There is no evidence that scale
> alone removes hindsight contamination within this family.

Not claimed: any scaling law, slope, or correlation; any statement about other
families; any explanation of why 9B sits low — three points cannot support one.
