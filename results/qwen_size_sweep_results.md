# Within-family size analysis — Qwen3.5 (4B, 9B, 27B)

**Design tag:** `g2-qwen-size-sweep-design-v1`, frozen before any new
checkpoint produced output. Analysis: `results/qwen_size_sweep_analysis.json`.

**Qwen3.5-2B was preregistered but unavailable** in this offline environment
(no local snapshot), a constraint recorded in the preregistration before any
run. This is therefore an analysis across the **available** dense Qwen3.5
checkpoints, not a 2B–27B scaling study, and it is named that way everywhere.

Every size ran the frozen 256-unit artifact (SHA-256 `0b6fd8d0…acf0901d`)
through the unchanged runner: same prompts, same greedy decoding, same parser,
same thresholds. 9B is the existing large-replication result, reused rather
than re-run. Revisions: 4B `851bf6e806ef…`, 9B `c202236235762e1…`,
27B `fc05daec18b0…`.

## Result

| size | qualified | parse rate | boundary accuracy | responsiveness | `OutOfSetIntrusion` (95% CI) | intrusion pass |
|---|---|---|---|---|---|---|
| 4B | yes | 1024/1024 | **99.61%** | 41.50 | **32.00 [28.40, 35.65]** | yes |
| 9B | yes | 1024/1024 | **99.22%** | 47.27 | **16.02 [14.18, 17.89]** | yes |
| 27B | yes | 1024/1024 | **100%** | 41.01 | **36.75 [33.50, 39.93]** | yes |

Paired contrasts on the same 256 questions:

| contrast | Δ intrusion (95% CI) | Δ boundary accuracy |
|---|---|---|
| 9B − 4B | **−15.98 [−19.39, −12.58]** | −0.39 pp |
| 27B − 9B | **+20.73 [17.41, 24.06]** | +0.78 pp |
| 27B − 4B | +4.75 [0.73, 8.71] | +0.39 pp |

## What this shows

1. **Scale does not remove the failure.** All three sizes qualify and all three
   clear the 5-point SESOI. The largest checkpoint is the **most** contaminated
   model measured anywhere in this project — 36.75 points, above Gemma-3-12B's
   27.73 — while answering every single boundary probe correctly.
2. **Recognition is saturated at every size; enforcement is not.** Boundary
   accuracy moves within 0.8 points (99.22–100%) across a 6.75× parameter
   range, while intrusion swings by more than 20 points. Two capacities that
   move independently over the same range are not one capacity, which is the
   cleanest evidence in this project that recognition ≠ enforcement.
3. **The trend is non-monotone**, and the preregistration says what to do with
   that: report it and fit no story. Intrusion falls sharply from 4B to 9B and
   rises further above the 4B level at 27B.

## What this does not show

- **No scaling law, no slope, no correlation.** Three points in one family.
  The preregistration forbade fitting any of these before the numbers existed,
  and the numbers are exactly the kind that would tempt it.
- **The U-shape is not established as a property of scale.** With three
  checkpoints it is equally consistent with checkpoint-specific training
  differences within the 3.5 family; nothing here identifies 27B rather than
  9B as the unusual one.
- **No claim about other families.** Gemma and Mistral were not swept.

The honest one-line summary: *within the Qwen3.5 family, temporal recognition
is saturated at every available size while out-of-set intrusion varies
non-monotonically by more than 20 points, and the largest checkpoint shows the
strongest contamination measured in this study.*
