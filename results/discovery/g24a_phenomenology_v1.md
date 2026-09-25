# G24A Prospective Exclusion Phenomenology Map (discovery layer)

**Layer 1 of the three-layer process (discovery -> hypothesis formation -> confirmation). No KILL gates: every stratum is reported, small or messy. Observations only — these numbers may seed hypothesis formation but are NOT confirmatory claims.**

Unit: item x model. Definitions (G0-compatible):

- `Y_admit = (admit_pre + admit_post)/2`
- `E = s*(Y_admit - Y_base)` — evidence leverage (s = +1 increase / -1 decrease; G0 `signed_L`)
- `L_pre = s*(Y_exclude_pre - Y_base)` — prospective residual
- `L_post = s*(Y_exclude_post - Y_base)` — retrospective residual
- `gain = L / E` (ratio; unbounded as E -> 0, so medians/strata are used, never the mean)
- `A_pre = s*(Y_admit_pre - Y_base)`, `A_post = s*(Y_admit_post - Y_base)` — admitted effect per phase (baseline Y_base)
- `C_pre = s*(Y_exclude_pre - Y_admit_pre)`, `C_post = s*(Y_exclude_post - Y_admit_post)` — retraction from the admitted judgment after the exclude ruling; its baseline is the corresponding Y_admit_* phase, NOT Y_base (`C = 0`: no change; `C = -A`: exactly back to baseline; `C < -A`: overshoot)

Identity reference lines: `L = E` (residual equals the full admitted effect = as-if-not-excluded), `L = 0` (removal), `L < 0` (opposite to the annotated direction).

**Standing caveat (2026-09-25): `rho(E, L*)` shares `Y_base` mechanically and is DEMOTED to non-primary — treat it as description, not evidence. The primary cross-baseline quantities are `A*`/`C*` (section 3 note; matched-pair audit in `g24a_reversibility_v1`).**

## 0. Data and integrity

| models | items | rows | complete | incomplete | unparsed cells | mass<0.5 rows |
|---|---|---|---|---|---|---|
| 5 | 600 | 3000 | 3000 | 0 | 0 | 0 |

Duplicate (item, kind) rows: 0.

## 1. Definition cross-check vs `g24a_analysis_v1` (informational)

| quantity | published | recomputed | match |
|---|---|---|---|
| alignment | 0.84 | 0.8363 | OK |
| n_usable | 2007 | 2007 | OK |
| median_absL | 32.7 | 32.6769 | OK |
| REI_pre | 0.541 | 0.5412 | OK |
| REI_post | -0.072 | -0.0718 | OK |
| frac_post_gt_pre | 0.32 | 0.3214 | OK |

## 2. Distributions (all rows, no exclusions)

| quantity | n | mean | p10 | p25 | med | p75 | p90 |
|---|---|---|---|---|---|---|---|
| `E` | 3000 | +32.21 | -0.7 | +2.7 | +26.4 | +55.6 | +89.0 |
| `L_pre` | 3000 | +19.20 | -26.5 | -0.1 | +11.1 | +44.4 | +81.5 |
| `L_post` | 3000 | +6.62 | -53.4 | -17.6 | +2.4 | +33.7 | +66.7 |
| `A_pre` | 3000 | +32.33 | -0.3 | +2.5 | +26.5 | +56.0 | +89.7 |
| `A_post` | 3000 | +32.08 | -0.5 | +2.2 | +25.5 | +55.6 | +89.9 |
| `C_pre` | 3000 | -13.13 | -57.7 | -30.5 | -0.7 | +0.0 | +5.6 |
| `C_post` | 3000 | -25.46 | -85.9 | -54.9 | -16.4 | -0.0 | +9.0 |
| `Y_base` | 3000 | +53.89 | +2.4 | +21.9 | +55.6 | +88.7 | +99.1 |
| `Y_admit` | 3000 | +55.39 | +0.0 | +4.7 | +79.0 | +98.5 | +100.0 |
| `gain_pre_Egt0`  (mean poisoned by E->0 tails; use quantiles) | 2592 | +3098646266.98 | -1.3 | +0.0 | +0.9 | +1.0 | +1.2 |
| `gain_post_Egt0`  (mean poisoned by E->0 tails; use quantiles) | 2592 | -3065708045.88 | -7.1 | -0.7 | +0.3 | +1.0 | +1.1 |

### gain stratified by |E| (E>0; ratio stability strata)

| abs(E) stratum | n | gain_pre p25/med/p75 | gain_post med | med L_pre |
|---|---|---|---|---|
| absE [0,10) | 558 | -1.96 / +0.92 / +1.02 | -4.88 | +0.1 |
| absE [10,20) | 346 | -1.02 / +0.70 / +1.01 | -0.16 | +9.7 |
| absE [20,40) | 545 | -0.06 / +0.68 / +1.00 | +0.11 | +20.2 |
| absE [40,60) | 454 | +0.01 / +0.81 / +1.00 | +0.63 | +38.7 |
| absE [60,101) | 689 | +0.47 / +0.97 / +1.00 | +0.54 | +72.0 |

## 3. E vs residual structure (binned; identity = full leak)

Pooled: spearman(E, L_pre) = +0.643, spearman(E, L_post) = +0.542 (n=3000).

**Status of these rho values: DEMOTED (2026-09-25). `E` and `L*` both contain `Y_base`, so `rho(E, L*)` is mechanically inflated by the shared baseline — descriptive only, NOT primary evidence.**

Non-shared-baseline cross-correlations (Spearman, all complete rows, n=3000): rho(A_post, C_pre) = -0.206, rho(A_pre, C_post) = -0.174, rho(C_pre, C_post) = +0.405.

Note: bins with E < 0 are rows where the admitted evidence moved against its annotated direction; for them `gain = L/E` is pure (E, L) geometry — a positive gain means L shares E's negative sign, not 'leakage in the annotated sense'.

### gemma3-12b  (n=600, rho(E,L_pre)=+0.578, rho(E,L_post)=+0.592)

| E bin | n | mean E | med L_pre | med gain_pre | med L_post |
|---|---|---|---|---|---|
| [-100, -90) | 1 | -95.0 | +0.1 | -0.00 | -45.2 |
| [-50, -40) | 4 | -46.2 | -39.1 | +0.83 | -57.3 |
| [-40, -30) | 8 | -34.1 | -0.9 | +0.02 | -8.5 |
| [-30, -20) | 7 | -22.9 | +1.6 | -0.07 | +22.2 |
| [-20, -10) | 11 | -13.8 | +11.2 | -1.02 | +33.7 |
| [-10, 0) | 27 | -2.5 | -0.0 | +0.02 | -0.0 |
| [0, 10) | 88 | +3.1 | -0.6 | -0.34 | -3.5 |
| [10, 20) | 71 | +12.9 | +1.3 | +0.10 | -0.5 |
| [20, 30) | 86 | +24.1 | +11.2 | +0.46 | +12.9 |
| [30, 40) | 74 | +34.0 | +11.4 | +0.33 | +3.9 |
| [40, 50) | 71 | +45.1 | +20.5 | +0.46 | +39.1 |
| [50, 60) | 78 | +54.7 | +52.0 | +0.96 | +55.2 |
| [60, 70) | 21 | +63.9 | +33.2 | +0.54 | +62.5 |
| [70, 80) | 11 | +76.7 | +66.0 | +0.87 | +66.1 |
| [80, 90) | 17 | +87.2 | +35.4 | +0.42 | +60.5 |
| [90, 100) | 25 | +98.6 | +77.9 | +0.80 | +89.9 |

### llama31-8b  (n=600, rho(E,L_pre)=+0.633, rho(E,L_post)=+0.512)

| E bin | n | mean E | med L_pre | med gain_pre | med L_post |
|---|---|---|---|---|---|
| [-90, -80) | 5 | -84.4 | -10.3 | +0.12 | -28.8 |
| [-80, -70) | 4 | -77.2 | -24.4 | +0.31 | -33.8 |
| [-70, -60) | 6 | -66.4 | -31.1 | +0.47 | -27.4 |
| [-60, -50) | 5 | -54.5 | -49.5 | +0.88 | -8.4 |
| [-50, -40) | 6 | -44.5 | -25.2 | +0.57 | -6.1 |
| [-40, -30) | 12 | -36.0 | -5.2 | +0.18 | +3.7 |
| [-30, -20) | 13 | -25.2 | +1.3 | -0.06 | +0.6 |
| [-20, -10) | 18 | -14.6 | +3.4 | -0.22 | -6.0 |
| [-10, 0) | 71 | -3.4 | -1.8 | +0.98 | -7.6 |
| [0, 10) | 110 | +4.1 | +1.3 | +0.35 | -27.7 |
| [10, 20) | 46 | +15.2 | +14.1 | +0.86 | -18.5 |
| [20, 30) | 53 | +25.5 | +23.1 | +0.92 | -5.2 |
| [30, 40) | 58 | +34.5 | +30.7 | +0.90 | -2.0 |
| [40, 50) | 61 | +44.0 | +26.5 | +0.59 | +4.5 |
| [50, 60) | 37 | +54.3 | +28.7 | +0.55 | +13.4 |
| [60, 70) | 25 | +64.9 | +51.4 | +0.84 | +19.9 |
| [70, 80) | 22 | +74.9 | +46.2 | +0.63 | +30.6 |
| [80, 90) | 29 | +84.6 | +53.0 | +0.65 | +45.6 |
| [90, 100) | 19 | +94.0 | +89.0 | +0.95 | +48.2 |

### mistral-small-24b  (n=600, rho(E,L_pre)=+0.592, rho(E,L_post)=+0.500)

| E bin | n | mean E | med L_pre | med gain_pre | med L_post |
|---|---|---|---|---|---|
| [-100, -90) | 1 | -91.7 | -4.2 | +0.05 | -5.0 |
| [-30, -20) | 4 | -23.1 | -32.9 | +1.39 | -31.7 |
| [-20, -10) | 1 | -12.0 | -5.4 | +0.45 | +14.3 |
| [-10, 0) | 9 | -2.9 | -22.0 | +7.54 | -21.4 |
| [0, 10) | 24 | +5.1 | -36.6 | -6.88 | -18.8 |
| [10, 20) | 132 | +14.9 | -11.6 | -0.85 | -15.0 |
| [20, 30) | 67 | +25.0 | -7.8 | -0.28 | +0.1 |
| [30, 40) | 73 | +35.0 | +1.1 | +0.03 | -2.7 |
| [40, 50) | 68 | +45.4 | +5.7 | +0.13 | -0.6 |
| [50, 60) | 38 | +53.8 | +17.9 | +0.34 | +20.5 |
| [60, 70) | 38 | +65.2 | +30.4 | +0.47 | +17.6 |
| [70, 80) | 33 | +75.4 | +24.8 | +0.33 | +20.8 |
| [80, 90) | 40 | +85.5 | +29.2 | +0.35 | +9.2 |
| [90, 100) | 72 | +96.0 | +34.3 | +0.36 | +22.3 |

### qwen3-8b  (n=600, rho(E,L_pre)=+0.790, rho(E,L_post)=+0.603)

| E bin | n | mean E | med L_pre | med gain_pre | med L_post |
|---|---|---|---|---|---|
| [-100, -90) | 1 | -100.0 | +0.0 | -0.00 | +0.0 |
| [-90, -80) | 1 | -89.0 | -88.9 | +1.00 | -88.9 |
| [-80, -70) | 1 | -74.4 | +22.1 | -0.30 | +22.1 |
| [-70, -60) | 1 | -69.2 | -100.0 | +1.45 | -100.0 |
| [-60, -50) | 2 | -53.9 | -26.7 | +0.50 | +4.0 |
| [-50, -40) | 6 | -44.7 | +36.9 | -0.79 | +53.4 |
| [-40, -30) | 9 | -34.3 | +0.1 | -0.00 | +27.4 |
| [-30, -20) | 5 | -25.6 | -0.0 | +0.00 | -22.2 |
| [-20, -10) | 13 | -12.4 | +14.7 | -1.09 | +14.7 |
| [-10, 0) | 58 | -0.8 | -0.0 | +0.25 | -0.0 |
| [0, 10) | 133 | +1.2 | +0.0 | +1.00 | +0.0 |
| [10, 20) | 34 | +14.2 | +13.3 | +1.00 | +11.8 |
| [20, 30) | 46 | +23.8 | +22.3 | +1.00 | +22.0 |
| [30, 40) | 48 | +33.9 | +33.5 | +1.00 | +32.5 |
| [40, 50) | 36 | +45.3 | +44.9 | +1.00 | +44.3 |
| [50, 60) | 36 | +55.3 | +55.5 | +1.00 | +54.5 |
| [60, 70) | 34 | +66.1 | +66.6 | +1.00 | +64.3 |
| [70, 80) | 31 | +75.2 | +77.5 | +1.00 | +73.9 |
| [80, 90) | 29 | +86.3 | +87.4 | +1.00 | +84.7 |
| [90, 100) | 76 | +99.6 | +100.0 | +1.00 | +100.0 |

### qwen35-9b  (n=600, rho(E,L_pre)=+0.875, rho(E,L_post)=+0.613)

| E bin | n | mean E | med L_pre | med gain_pre | med L_post |
|---|---|---|---|---|---|
| [-100, -90) | 3 | -92.6 | +2.5 | -0.03 | +0.6 |
| [-90, -80) | 2 | -82.8 | -84.9 | +1.03 | +11.0 |
| [-60, -50) | 1 | -51.0 | -96.4 | +1.89 | -27.6 |
| [-50, -40) | 4 | -44.6 | -57.6 | +1.22 | -14.0 |
| [-40, -30) | 3 | -32.4 | -24.2 | +0.71 | -82.0 |
| [-30, -20) | 5 | -24.0 | -12.0 | +0.48 | -0.9 |
| [-20, -10) | 7 | -15.1 | -17.0 | +1.05 | -5.3 |
| [-10, 0) | 73 | -1.6 | -0.2 | +0.38 | -9.3 |
| [0, 10) | 203 | +2.8 | +1.5 | +0.98 | -58.8 |
| [10, 20) | 63 | +14.1 | +12.5 | +1.00 | +10.7 |
| [20, 30) | 21 | +24.6 | +24.0 | +1.00 | +18.2 |
| [30, 40) | 19 | +34.6 | +33.2 | +1.00 | +14.2 |
| [40, 50) | 13 | +44.6 | +46.6 | +1.02 | +16.0 |
| [50, 60) | 16 | +54.4 | +54.0 | +0.99 | +44.2 |
| [60, 70) | 12 | +65.4 | +67.3 | +1.00 | +63.2 |
| [70, 80) | 33 | +75.8 | +75.6 | +1.00 | +1.2 |
| [80, 90) | 37 | +85.7 | +85.2 | +1.00 | +46.2 |
| [90, 100) | 85 | +96.0 | +96.6 | +1.00 | +44.2 |

## 4. Regions vs the reference lines (counts)

Legend: `L_neg` = L < 0 (opposite to annotated direction); `E_nonpos` = E <= 0 (admitted evidence moves wrong way); `L_gt_E` = L > E (beyond full admitted effect); `L_mid` = E/2 <= L <= E (large residual); `L_small` = 0 <= L < E/2 (small residual).

| scope | arm | n | L_neg | E_nonpos | L_gt_E | L_mid | L_small | frac L_neg |
|---|---|---|---|---|---|---|---|---|
| pooled | pre | 3000 | 839 | 152 | 732 | 878 | 399 | +0.280 |
| pooled | post | 3000 | 1271 | 135 | 495 | 663 | 436 | +0.424 |
| gemma3-12b | pre | 600 | 177 | 31 | 93 | 171 | 128 | +0.295 |
| gemma3-12b | post | 600 | 210 | 28 | 119 | 171 | 72 | +0.350 |
| llama31-8b | pre | 600 | 178 | 50 | 133 | 160 | 79 | +0.297 |
| llama31-8b | post | 600 | 306 | 46 | 69 | 67 | 112 | +0.510 |
| mistral-small-24b | pre | 600 | 255 | 1 | 50 | 140 | 154 | +0.425 |
| mistral-small-24b | post | 600 | 258 | 3 | 76 | 118 | 145 | +0.430 |
| qwen3-8b | pre | 600 | 115 | 35 | 221 | 214 | 15 | +0.192 |
| qwen3-8b | post | 600 | 189 | 36 | 165 | 179 | 31 | +0.315 |
| qwen35-9b | pre | 600 | 114 | 35 | 235 | 193 | 23 | +0.190 |
| qwen35-9b | post | 600 | 308 | 22 | 66 | 128 | 76 | +0.513 |

## 5. Pre/post item-level correspondence

spearman(L_pre, L_post) = +0.653; quadrants: L_pre_<0, L_post_<0 = 655, L_pre_<0, L_post_>=0 = 184, L_pre_>=0, L_post_<0 = 616, L_pre_>=0, L_post_>=0 = 1545.

## 6. Stratified grid (model / source / direction)

| stratum | n | frac E>0 | med E | med L_pre | med L_post | med gain_pre | rho(E,L_pre) |
|---|---|---|---|---|---|---|---|
| gemma3-12b/fever/decrease | 200 | +0.85 | +49.7 | +22.1 | +33.2 | +0.90 | +0.58 |
| gemma3-12b/fever/increase | 200 | +0.95 | +22.2 | +0.3 | -0.2 | +0.11 | +0.66 |
| gemma3-12b/scifact/decrease | 100 | +0.85 | +42.6 | +11.4 | +44.4 | +0.40 | +0.34 |
| gemma3-12b/scifact/increase | 100 | +0.97 | +22.8 | +9.3 | -2.2 | +0.34 | +0.31 |
| llama31-8b/fever/decrease | 200 | +0.68 | +12.9 | +13.0 | +3.5 | +0.92 | +0.65 |
| llama31-8b/fever/increase | 200 | +0.81 | +26.4 | +6.0 | -6.3 | +0.64 | +0.75 |
| llama31-8b/scifact/decrease | 100 | +0.68 | +22.7 | +18.7 | +12.5 | +0.83 | +0.42 |
| llama31-8b/scifact/increase | 100 | +0.94 | +27.8 | +16.8 | -7.4 | +0.79 | +0.62 |
| mistral-small-24b/fever/decrease | 200 | +0.95 | +28.3 | +10.7 | +14.8 | +0.51 | +0.71 |
| mistral-small-24b/fever/increase | 200 | +0.98 | +64.2 | +7.2 | -2.1 | +0.11 | +0.69 |
| mistral-small-24b/scifact/decrease | 100 | +0.99 | +36.2 | +22.1 | +30.3 | +0.56 | +0.66 |
| mistral-small-24b/scifact/increase | 100 | +1.00 | +36.9 | -25.3 | -33.4 | -0.77 | +0.63 |
| qwen3-8b/fever/decrease | 200 | +0.81 | +30.4 | +43.9 | +37.4 | +1.00 | +0.87 |
| qwen3-8b/fever/increase | 200 | +0.85 | +9.7 | +1.5 | +0.0 | +1.00 | +0.83 |
| qwen3-8b/scifact/decrease | 100 | +0.80 | +35.9 | +55.4 | +55.7 | +1.00 | +0.56 |
| qwen3-8b/scifact/increase | 100 | +0.90 | +24.9 | +11.2 | -22.1 | +1.00 | +0.73 |
| qwen35-9b/fever/decrease | 200 | +0.81 | +12.5 | +12.3 | +7.8 | +1.00 | +0.93 |
| qwen35-9b/fever/increase | 200 | +0.86 | +2.0 | +2.0 | -19.9 | +1.00 | +0.90 |
| qwen35-9b/scifact/decrease | 100 | +0.85 | +16.1 | +14.0 | +15.3 | +1.00 | +0.82 |
| qwen35-9b/scifact/increase | 100 | +0.82 | +6.7 | +2.2 | -75.4 | +0.99 | +0.70 |

## 7. Y_base deciles

| Y_base range | n | med E | med L_pre | med gain_pre | frac E>0 |
|---|---|---|---|---|---|
| [0.0, 2.4] | 300 | +0.6 | +0.5 | +0.98 | +0.72 |
| [2.4, 15.2] | 300 | +12.8 | +10.7 | +0.94 | +0.86 |
| [15.3, 30.2] | 300 | +21.2 | +16.0 | +0.85 | +0.90 |
| [30.2, 46.5] | 300 | +36.3 | +23.3 | +0.68 | +0.92 |
| [46.6, 55.6] | 300 | +44.4 | +25.6 | +0.69 | +0.93 |
| [55.6, 66.7] | 300 | +33.9 | +21.2 | +0.53 | +0.92 |
| [66.7, 79.0] | 300 | +23.2 | +19.3 | +0.64 | +0.91 |
| [79.2, 90.6] | 300 | +11.1 | +7.0 | +0.51 | +0.89 |
| [90.6, 99.1] | 300 | +2.8 | +2.2 | +0.97 | +0.83 |
| [99.1, 100.0] | 300 | +0.1 | +0.1 | +1.00 | +0.75 |

## 8. Floor (<=5) / ceiling (>=95) counts per cell

| model | kind | base | admit_pre | admit_post | exclude_pre | exclude_post |
|---|---|---|---|---|---|---|
| gemma3-12b | floor<=5 | 43 | 161 | 156 | 105 | 160 |
| gemma3-12b | ceiling>=95 | 39 | 154 | 138 | 56 | 46 |
| llama31-8b | floor<=5 | 49 | 69 | 64 | 83 | 65 |
| llama31-8b | ceiling>=95 | 53 | 112 | 161 | 52 | 12 |
| mistral-small-24b | floor<=5 | 59 | 171 | 159 | 57 | 81 |
| mistral-small-24b | ceiling>=95 | 28 | 184 | 187 | 19 | 5 |
| qwen3-8b | floor<=5 | 115 | 210 | 208 | 278 | 334 |
| qwen3-8b | ceiling>=95 | 175 | 272 | 282 | 214 | 153 |
| qwen35-9b | floor<=5 | 95 | 221 | 211 | 219 | 235 |
| qwen35-9b | ceiling>=95 | 209 | 284 | 292 | 261 | 40 |

## 9. Rule-probe context (stated knowledge of the ruling)

| model | p_yes exclude_pre | p_yes exclude_post | p_yes admit_post |
|---|---|---|---|
| gemma3-12b | +0.000 | +0.000 | +1.000 |
| llama31-8b | +0.000 | +0.000 | +0.998 |
| mistral-small-24b | +0.001 | +0.001 | +0.992 |
| qwen3-8b | +0.000 | +0.000 | +0.912 |
| qwen35-9b | +0.000 | +0.001 | +0.984 |

## 10. Reading samples (descriptive selections)

### largest_L_pre

| model | item | stratum | dir | Y0 | adm | excl_pre | excl_post | E | L_pre | L_post | claim |
|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3-8b | g24a_fever_211799 | fever/REFUTES | decrease | 100.0 | 0.0 | 0.0 | 0.0 | +100.0 | +100.0 | +100.0 | Brick (film) is a 2006 film only. |
| qwen3-8b | g24a_fever_89240 | fever/REFUTES | decrease | 100.0 | 0.0 | 0.0 | 0.0 | +100.0 | +100.0 | +100.0 | Billboard Dad was only released in 1968. |
| qwen3-8b | g24a_fever_204020 | fever/REFUTES | decrease | 100.0 | 0.0 | 0.0 | 0.0 | +100.0 | +100.0 | +100.0 | Down with Love is only a book. |
| qwen3-8b | g24a_fever_12421 | fever/SUPPORTS | increase | 0.0 | 100.0 | 100.0 | 100.0 | +100.0 | +100.0 | +100.0 | Catherine Keener was in the cast of Into the Wild. |
| qwen3-8b | g24a_fever_195503 | fever/SUPPORTS | increase | 0.0 | 100.0 | 100.0 | 100.0 | +100.0 | +100.0 | +100.0 | Offers of appointment to the Supreme Court of the United Sta |
| qwen3-8b | g24a_fever_7744 | fever/REFUTES | decrease | 100.0 | 0.0 | 0.0 | 0.0 | +100.0 | +100.0 | +100.0 | Mount Hood is not Oregon's highest mountain. |

### smallest_abs_L_pre

| model | item | stratum | dir | Y0 | adm | excl_pre | excl_post | E | L_pre | L_post | claim |
|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3-8b | g24a_fever_4737 | fever/SUPPORTS | increase | 100.0 | 100.0 | 100.0 | 100.0 | +0.0 | -0.0 | -0.0 | Sausage Party was directed by Greg Tiernan and Conrad Vernon |
| qwen3-8b | g24a_fever_219033 | fever/REFUTES | decrease | 0.0 | 0.0 | 0.0 | 0.0 | +0.0 | +0.0 | +0.0 | Savages had no director. |
| qwen3-8b | g24a_fever_200371 | fever/SUPPORTS | increase | 100.0 | 100.0 | 100.0 | 100.0 | +0.0 | -0.0 | -0.0 | Tom DeLonge formed Blink-182. |
| qwen3-8b | g24a_fever_91976 | fever/REFUTES | decrease | 0.0 | 0.0 | 0.0 | 0.0 | +0.0 | +0.0 | +0.0 | Bank of America withholds products and services. |
| qwen3-8b | g24a_fever_163970 | fever/SUPPORTS | increase | 100.0 | 100.0 | 100.0 | 100.0 | +0.0 | +0.0 | -0.0 | Veeram is a film from 2014. |
| qwen3-8b | g24a_fever_177838 | fever/SUPPORTS | increase | 100.0 | 100.0 | 100.0 | 100.0 | +0.0 | +0.0 | -0.0 | Milk is a film. |

### L_pre_negative_flips

| model | item | stratum | dir | Y0 | adm | excl_pre | excl_post | E | L_pre | L_post | claim |
|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3-8b | g24a_fever_27148 | fever/SUPPORTS | increase | 100.0 | 100.0 | 0.0 | 22.3 | +0.0 | -100.0 | -77.7 | Melilla has an area of 12.3 km2 within Africa. |
| qwen3-8b | g24a_scifact_810 | scifact/SUPPORT | increase | 99.9 | 100.0 | 0.0 | 99.9 | +0.1 | -99.9 | -0.0 | Mouse models can be generated using androgenetic haploid emb |
| qwen35-9b | g24a_fever_16224 | fever/SUPPORTS | increase | 99.1 | 99.4 | 0.8 | 1.2 | +0.3 | -98.3 | -97.8 | Email filtering output is capable of throwing messages away. |
| qwen3-8b | g24a_scifact_1348 | scifact/SUPPORT | increase | 96.4 | 100.0 | 0.0 | 0.0 | +3.6 | -96.4 | -96.4 | Upon viral challenge, influenza-specific memory CD4+ T cells |
| qwen35-9b | g24a_scifact_277 | scifact/SUPPORT | increase | 99.0 | 99.7 | 2.9 | 5.5 | +0.6 | -96.1 | -93.5 | Commelina yellow mottle virus (ComYMV) has three typical bad |
| qwen35-9b | g24a_fever_196986 | fever/SUPPORTS | increase | 99.3 | 99.4 | 4.5 | 2.8 | +0.1 | -94.8 | -96.5 | Knowledge over ignorance is signified spiritually through Di |

### E_nonpositive

| model | item | stratum | dir | Y0 | adm | excl_pre | excl_post | E | L_pre | L_post | claim |
|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3-8b | g24a_scifact_910 | scifact/CONTRADICT | decrease | 0.0 | 100.0 | 0.0 | 0.0 | -100.0 | +0.0 | +0.0 | PKG-I does not have a large impact on expression of spinal l |
| qwen35-9b | g24a_fever_105216 | fever/SUPPORTS | increase | 97.4 | 0.1 | 99.9 | 98.0 | -97.3 | +2.5 | +0.6 | Night of the Living Dead is not a series of seven zombie hor |
| gemma3-12b | g24a_fever_209092 | fever/REFUTES | decrease | 0.2 | 95.3 | 0.1 | 45.4 | -95.0 | +0.1 | -45.2 | Stadium Arcadium was released without John Frusciante. |
| mistral-small-24b | g24a_fever_20847 | fever/SUPPORTS | decrease | 0.6 | 92.3 | 4.8 | 5.6 | -91.7 | -4.2 | -5.0 | Tripartite Alliance is a part of the South African Communist |
| qwen35-9b | g24a_fever_146157 | fever/REFUTES | decrease | 8.9 | 99.1 | 97.3 | 95.1 | -90.2 | -88.4 | -86.2 | The New England Patriots lost five Super Bowls. |
| qwen35-9b | g24a_fever_20847 | fever/SUPPORTS | decrease | 6.6 | 96.7 | 3.8 | 4.9 | -90.1 | +2.8 | +1.7 | Tripartite Alliance is a part of the South African Communist |

### E_ge40_smallest_abs_L_pre

| model | item | stratum | dir | Y0 | adm | excl_pre | excl_post | E | L_pre | L_post | claim |
|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3-8b | g24a_fever_68483 | fever/SUPPORTS | increase | 0.0 | 100.0 | 0.0 | 85.2 | +100.0 | -0.0 | +85.2 | Villa Park hosted the FA Community Shield in 2012. |
| qwen3-8b | g24a_fever_162743 | fever/SUPPORTS | increase | 0.0 | 100.0 | 0.0 | 0.0 | +100.0 | +0.0 | +0.0 | Aeneas appeared in the Iliad by Homer. |
| gemma3-12b | g24a_fever_177838 | fever/SUPPORTS | increase | 0.0 | 50.0 | 0.0 | 0.0 | +50.0 | +0.0 | +0.0 | Milk is a film. |
| gemma3-12b | g24a_fever_156102 | fever/REFUTES | decrease | 55.6 | 0.0 | 55.6 | 0.0 | +55.6 | +0.0 | +55.5 | Keith Stanfield was born on March 12, 1991. |
| gemma3-12b | g24a_fever_103545 | fever/REFUTES | decrease | 55.6 | 0.0 | 55.6 | 55.4 | +55.5 | +0.0 | +0.1 | Annabelle is at The Museum of Natural History. |
| gemma3-12b | g24a_fever_42026 | fever/REFUTES | decrease | 55.6 | 1.8 | 55.6 | 19.5 | +53.7 | +0.0 | +36.0 | Gray Matters was released in May of 2006. |

### E_ge40_L_closest_to_E

| model | item | stratum | dir | Y0 | adm | excl_pre | excl_post | E | L_pre | L_post | claim |
|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3-8b | g24a_fever_47792 | fever/REFUTES | decrease | 100.0 | 56.7 | 0.0 | 0.0 | +43.3 | +100.0 | +100.0 | Half Girlfriend's principal photography began in May of 2016 |
| qwen35-9b | g24a_fever_208917 | fever/REFUTES | decrease | 99.4 | 56.8 | 4.2 | 32.5 | +42.6 | +95.1 | +66.8 | The Monster is only an album. |
| qwen35-9b | g24a_fever_131971 | fever/REFUTES | decrease | 94.6 | 50.7 | 0.1 | 37.7 | +43.9 | +94.5 | +56.8 | Colin Kaepernick is not a starter for the San Francisco 49er |
| qwen3-8b | g24a_scifact_781 | scifact/CONTRADICT | decrease | 100.0 | 50.0 | 0.0 | 0.0 | +50.0 | +100.0 | +100.0 | Mice that lack Interferon-γ or its receptor exhibit high res |
| qwen35-9b | g24a_scifact_149 | scifact/CONTRADICT | decrease | 99.1 | 48.9 | 0.0 | 29.5 | +50.2 | +99.1 | +69.7 | Autophagy deficiency in the liver increases vulnerability to |
| qwen35-9b | g24a_fever_137040 | fever/REFUTES | decrease | 99.1 | 47.9 | 0.0 | 33.5 | +51.3 | +99.1 | +65.6 | The Raven (2012 film) was released in Ireland in April 2012. |

## 11. Histograms (raw counts)

### L_pre (width 5, range [-100, 100))

  -100.0:12  -95.0:3  -90.0:9  -85.0:7  -80.0:8  -75.0:16  -70.0:11  -65.0:13  -60.0:16  -55.0:27  -50.0:16  -45.0:50  -40.0:30  -35.0:55  -30.0:34  -25.0:73  -20.0:49  -15.0:74  -10.0:73  -5.0:263  0.0:452  5.0:155  10.0:190  15.0:102  20.0:151  25.0:93  30.0:114  35.0:75  40.0:101  45.0:68  50.0:73  55.0:87  60.0:41  65.0:59  70.0:33  75.0:57  80.0:29  85.0:60  90.0:50  95.0:171

### L_post - L_pre (width 5, range [-100, 100))

  -100.0:119  -95.0:55  -90.0:35  -85.0:21  -80.0:32  -75.0:30  -70.0:37  -65.0:30  -60.0:37  -55.0:35  -50.0:54  -45.0:83  -40.0:83  -35.0:87  -30.0:72  -25.0:89  -20.0:77  -15.0:123  -10.0:158  -5.0:654  0.0:486  5.0:122  10.0:104  15.0:49  20.0:58  25.0:48  30.0:39  35.0:34  40.0:35  45.0:19  50.0:21  55.0:33  60.0:5  65.0:5  70.0:4  75.0:6  80.0:4  85.0:6  90.0:4  95.0:7

### gain_pre, E>0 (width 0.1 over [-1, 2); tails listed after)

  -1.0:16  -0.9:21  -0.8:14  -0.7:15  -0.6:27  -0.5:20  -0.4:22  -0.3:29  -0.2:37  -0.1:72  +0.0:112  +0.1:71  +0.2:80  +0.3:69  +0.4:67  +0.5:82  +0.6:80  +0.7:82  +0.8:111  +0.9:523  +1.0:413  +1.1:77  +1.2:39  +1.3:27  +1.4:26  +1.5:20  +1.6:11  +1.7:13  +1.8:11  +1.9:95

  tails: below -1.0 = 310 rows; at/above 1.9 (incl. >=2.0 clipped into 1.9 display bin) = 95 rows; raw >=2.0 = 0 rows.

## 12. Figures

- `results/discovery/figs/E_vs_Lpre.png`
- `results/discovery/figs/E_vs_Lpost.png`
- `results/discovery/figs/Lpre_vs_Lpost.png`
