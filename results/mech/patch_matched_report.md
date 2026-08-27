# Stage 5 — same-chronology bidirectional patching

FAILURE = unrelated preview -> rule(0%) -> evidence -> answer
SUCCESS = paraphrase preview -> rule(0%) -> evidence -> answer
Length-matched to within a few tokens; the evidence the decision reads sits after
the rule on both sides, so token order is not the difference.

n = 29 of 45 items with a behavioural gap >= 2 points.
- behavioural gap, failure - success: +13.2 [+8.6, +18.1] rating points
- 2x2 interaction (ME-MA)-(UE-UA), sign-aligned: -18.3 [-23.7, -12.9]

## patch SUCCESS state into the FAILURE run (does it rescue?)

Recovery fraction: 1.0 = the patched run answers like the donor condition, 0.0 = like its own.

| layer | preview end | rule end | rule SPAN | evidence end | answer |
|---:|---|---|---|---|---|
| 0 | -0.05 | -0.01 | -0.01 | -0.00 | -0.00 |
| 2 | -0.02 | +0.00 | -0.06 | +0.00 | -0.00 |
| 4 | +0.00 | -0.01 | -0.03 | +0.01 | -0.00 |
| 6 | -0.03 | -0.09 | -0.13 | +0.02 | -0.00 |
| 8 | -0.00 | -0.01 | -0.13 | +0.02 | -0.01 |
| 10 | +0.01 | -0.03 | +0.02 | +0.07 | -0.02 |
| 12 | +0.06 | +0.00 | +0.18 | +0.11 | -0.02 |
| 14 | +0.00 | +0.14 | +0.43 | +0.14 | +0.00 |
| 16 | -0.09 | +0.18 | +0.54 | +0.14 | +0.05 |
| 18 | -0.05 | +0.24 | +0.46 | +0.09 | +0.10 |
| 20 | -0.01 | +0.22 | +0.19 | +0.07 | +0.33 |
| 22 | -0.00 | +0.03 | +0.04 | +0.00 | +0.74 |
| 24 | -0.00 | +0.02 | -0.00 | -0.00 | +0.78 |
| 26 | -0.00 | +0.00 | -0.00 | +0.00 | +0.82 |
| 28 | +0.00 | -0.00 | -0.00 | -0.00 | +0.84 |
| 30 | -0.00 | +0.00 | -0.00 | -0.00 | +0.88 |
| 32 | -0.00 | +0.00 | -0.00 | -0.00 | +0.88 |
| 34 | -0.00 | +0.00 | +0.00 | -0.00 | +0.97 |

## patch FAILURE state into the SUCCESS run (does it break it?)

Recovery fraction: 1.0 = the patched run answers like the donor condition, 0.0 = like its own.

| layer | preview end | rule end | rule SPAN | evidence end | answer |
|---:|---|---|---|---|---|
| 0 | +0.01 | +0.02 | +0.00 | +0.00 | -0.01 |
| 2 | -0.05 | +0.00 | -0.08 | -0.01 | +0.00 |
| 4 | +0.06 | -0.02 | -0.04 | -0.01 | +0.00 |
| 6 | -0.02 | -0.08 | -0.11 | -0.00 | +0.00 |
| 8 | -0.04 | -0.02 | -0.12 | -0.00 | -0.00 |
| 10 | -0.01 | -0.02 | -0.08 | +0.03 | +0.02 |
| 12 | -0.02 | +0.02 | +0.37 | +0.04 | +0.04 |
| 14 | -0.04 | +0.16 | +0.92 | +0.08 | +0.09 |
| 16 | -0.11 | +0.26 | +0.88 | +0.18 | +0.08 |
| 18 | -0.08 | +0.25 | +0.57 | +0.10 | +0.19 |
| 20 | -0.02 | +0.10 | +0.12 | +0.04 | +0.45 |
| 22 | -0.00 | -0.00 | +0.01 | -0.00 | +0.82 |
| 24 | -0.00 | -0.01 | -0.01 | -0.00 | +0.86 |
| 26 | -0.00 | -0.01 | +0.00 | -0.00 | +0.88 |
| 28 | +0.00 | -0.01 | +0.00 | -0.00 | +0.90 |
| 30 | -0.00 | -0.00 | -0.00 | -0.00 | +0.92 |
| 32 | -0.00 | -0.00 | -0.00 | +0.00 | +0.92 |
| 34 | +0.00 | +0.00 | +0.00 | +0.00 | +0.96 |

