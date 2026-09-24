# G24A Prospective Exclusion Phenomenology Map (discovery layer)

**Layer 1 of the three-layer process (discovery -> hypothesis formation -> confirmation). No KILL gates: every stratum is reported, small or messy. Observations only — these numbers may seed hypothesis formation but are NOT confirmatory claims.**

Unit: item x model. Definitions (G0-compatible):

- `Y_admit = (admit_pre + admit_post)/2`
- `E = s*(Y_admit - Y_base)` — evidence leverage (s = +1 increase / -1 decrease; G0 `signed_L`)
- `L_pre = s*(Y_exclude_pre - Y_base)` — prospective residual
- `L_post = s*(Y_exclude_post - Y_base)` — retrospective residual
- `gain = L / E` (ratio; unbounded as E -> 0, so medians/strata are used, never the mean)

Identity reference lines: `L = E` (residual equals the full admitted effect = as-if-not-excluded), `L = 0` (removal), `L < 0` (opposite to the annotated direction).

## 0. Data and integrity

| models | items | rows | complete | incomplete | unparsed cells | mass<0.5 rows |
|---|---|---|---|---|---|---|
| 5 | 600 | 3000 | 3000 | 0 | 0 | 0 |

Duplicate (item, kind) rows: 0.

## 1. Definition cross-check vs `g24a_analysis_v1` (informational)

| quantity | published | recomputed | match |
|---|---|---|---|
| alignment | 0.84 | 0.8392 | OK |
| n_usable | 2014 | 2014 | OK |
| median_absL | 32.7 | 32.6927 | OK |
| REI_pre | 0.541 | 0.5411 | OK |
| REI_post | -0.067 | -0.0673 | OK |
| frac_post_gt_pre | 0.32 | 0.3227 | OK |

## 2. Distributions (all rows, no exclusions)

| quantity | n | mean | p10 | p25 | med | p75 | p90 |
|---|---|---|---|---|---|---|---|
| `E` | 3000 | +32.45 | -0.5 | +3.7 | +26.6 | +55.5 | +89.0 |
| `L_pre` | 3000 | +19.59 | -24.7 | -0.1 | +11.1 | +44.4 | +81.9 |
| `L_post` | 3000 | +7.17 | -52.2 | -17.6 | +3.0 | +34.1 | +66.7 |
| `Y_base` | 3000 | +53.96 | +2.9 | +22.2 | +55.6 | +88.4 | +99.1 |
| `Y_admit` | 3000 | +55.45 | +0.0 | +5.2 | +77.8 | +98.2 | +100.0 |
| `gain_pre_Egt0`  (mean poisoned by E->0 tails; use quantiles) | 2610 | +9368467437.28 | -1.3 | +0.0 | +0.9 | +1.0 | +1.2 |
| `gain_post_Egt0`  (mean poisoned by E->0 tails; use quantiles) | 2610 | -3800061447.60 | -6.0 | -0.7 | +0.3 | +1.0 | +1.1 |

### gain stratified by |E| (E>0; ratio stability strata)

| abs(E) stratum | n | gain_pre p25/med/p75 | gain_post med | med L_pre |
|---|---|---|---|---|
| absE [0,10) | 550 | -1.49 / +0.94 / +1.02 | -3.67 | +0.2 |
| absE [10,20) | 351 | -1.04 / +0.72 / +1.00 | -0.46 | +9.8 |
| absE [20,40) | 560 | -0.06 / +0.69 / +1.00 | +0.12 | +20.2 |
| absE [40,60) | 472 | +0.05 / +0.81 / +1.00 | +0.67 | +38.1 |
| absE [60,101) | 677 | +0.44 / +0.98 / +1.00 | +0.52 | +73.1 |

## 3. E vs residual structure (binned; identity = full leak)

Pooled: spearman(E, L_pre) = +0.640, spearman(E, L_post) = +0.525 (n=3000).

Note: bins with E < 0 are rows where the admitted evidence moved against its annotated direction; for them `gain = L/E` is pure (E, L) geometry — a positive gain means L shares E's negative sign, not 'leakage in the annotated sense'.

### gemma3-12b  (n=600, rho(E,L_pre)=+0.585, rho(E,L_post)=+0.594)

| E bin | n | mean E | med L_pre | med gain_pre | med L_post |
|---|---|---|---|---|---|
| [-100, -90) | 1 | -95.0 | +0.2 | -0.00 | +0.1 |
| [-80, -70) | 1 | -74.2 | -58.1 | +0.78 | -84.2 |
| [-50, -40) | 6 | -45.3 | -32.3 | +0.69 | -29.4 |
| [-40, -30) | 7 | -34.4 | -2.3 | +0.07 | +0.1 |
| [-30, -20) | 6 | -24.1 | +1.3 | -0.05 | +25.7 |
| [-20, -10) | 8 | -14.3 | +18.3 | -1.43 | +28.1 |
| [-10, 0) | 32 | -4.0 | -0.1 | +1.23 | -0.3 |
| [0, 10) | 91 | +3.1 | -0.1 | -0.27 | -10.4 |
| [10, 20) | 70 | +12.6 | +0.5 | +0.04 | -11.0 |
| [20, 30) | 87 | +23.7 | +11.2 | +0.48 | +11.9 |
| [30, 40) | 73 | +34.1 | +20.2 | +0.55 | +12.8 |
| [40, 50) | 73 | +45.1 | +20.3 | +0.46 | +38.5 |
| [50, 60) | 78 | +54.8 | +48.5 | +0.90 | +55.2 |
| [60, 70) | 21 | +64.3 | +53.1 | +0.80 | +60.2 |
| [70, 80) | 9 | +77.1 | +65.3 | +0.84 | +76.5 |
| [80, 90) | 15 | +87.2 | +36.6 | +0.43 | +60.5 |
| [90, 100) | 22 | +98.8 | +78.0 | +0.83 | +94.1 |

### llama31-8b  (n=600, rho(E,L_pre)=+0.612, rho(E,L_post)=+0.475)

| E bin | n | mean E | med L_pre | med gain_pre | med L_post |
|---|---|---|---|---|---|
| [-90, -80) | 2 | -84.7 | -37.3 | +0.44 | +1.6 |
| [-80, -70) | 5 | -76.6 | -48.3 | +0.62 | -32.0 |
| [-70, -60) | 3 | -65.8 | -21.4 | +0.35 | -56.9 |
| [-60, -50) | 6 | -54.3 | -23.2 | +0.42 | -6.5 |
| [-50, -40) | 4 | -43.7 | -32.7 | +0.77 | +0.6 |
| [-40, -30) | 14 | -35.9 | -10.8 | +0.30 | +1.1 |
| [-30, -20) | 17 | -24.8 | +1.0 | -0.05 | -1.0 |
| [-20, -10) | 20 | -14.8 | +12.1 | -0.72 | -2.5 |
| [-10, 0) | 64 | -3.1 | -1.9 | +0.75 | -5.9 |
| [0, 10) | 108 | +4.0 | +1.3 | +0.35 | -21.7 |
| [10, 20) | 45 | +14.8 | +13.6 | +0.93 | -19.5 |
| [20, 30) | 59 | +24.7 | +21.5 | +0.90 | -11.1 |
| [30, 40) | 62 | +34.7 | +28.0 | +0.83 | -2.2 |
| [40, 50) | 61 | +44.1 | +25.4 | +0.60 | +6.7 |
| [50, 60) | 38 | +54.4 | +38.1 | +0.72 | +13.8 |
| [60, 70) | 23 | +64.7 | +50.9 | +0.79 | +19.1 |
| [70, 80) | 24 | +73.9 | +61.3 | +0.81 | +27.9 |
| [80, 90) | 28 | +84.8 | +49.9 | +0.59 | +43.1 |
| [90, 100) | 17 | +94.1 | +91.1 | +0.98 | +52.2 |

### mistral-small-24b  (n=600, rho(E,L_pre)=+0.554, rho(E,L_post)=+0.467)

| E bin | n | mean E | med L_pre | med gain_pre | med L_post |
|---|---|---|---|---|---|
| [-20, -10) | 1 | -14.3 | -2.3 | +0.16 | +14.3 |
| [-10, 0) | 3 | -3.2 | -41.9 | +7.12 | -31.7 |
| [0, 10) | 18 | +7.2 | -15.7 | -1.75 | -3.6 |
| [10, 20) | 132 | +14.8 | -12.9 | -0.83 | -15.7 |
| [20, 30) | 77 | +24.8 | -7.8 | -0.29 | +0.2 |
| [30, 40) | 71 | +35.2 | +1.3 | +0.04 | +3.0 |
| [40, 50) | 70 | +45.1 | +3.2 | +0.07 | -6.6 |
| [50, 60) | 43 | +54.1 | +20.1 | +0.38 | +28.6 |
| [60, 70) | 37 | +65.7 | +21.7 | +0.34 | +19.6 |
| [70, 80) | 36 | +75.3 | +23.4 | +0.30 | +25.7 |
| [80, 90) | 39 | +85.7 | +33.2 | +0.39 | +10.3 |
| [90, 100) | 73 | +96.0 | +33.6 | +0.35 | +23.2 |

### qwen3-8b  (n=600, rho(E,L_pre)=+0.806, rho(E,L_post)=+0.581)

| E bin | n | mean E | med L_pre | med gain_pre | med L_post |
|---|---|---|---|---|---|
| [-90, -80) | 2 | -89.1 | -85.5 | +0.96 | -86.1 |
| [-80, -70) | 1 | -75.5 | +22.1 | -0.29 | +22.1 |
| [-70, -60) | 2 | -61.1 | -62.4 | +1.03 | -9.0 |
| [-60, -50) | 3 | -54.3 | -49.1 | +0.88 | -0.0 |
| [-50, -40) | 5 | -45.0 | +20.9 | -0.45 | +52.9 |
| [-40, -30) | 6 | -34.4 | +28.0 | -0.82 | +37.4 |
| [-30, -20) | 6 | -26.1 | -26.7 | +1.02 | -43.1 |
| [-20, -10) | 14 | -12.2 | +4.5 | -0.27 | +6.4 |
| [-10, 0) | 52 | -0.8 | -0.0 | +0.72 | -0.0 |
| [0, 10) | 136 | +1.2 | +0.0 | +1.00 | +0.0 |
| [10, 20) | 39 | +13.5 | +11.5 | +1.00 | +11.1 |
| [20, 30) | 45 | +24.0 | +22.2 | +1.00 | +21.8 |
| [30, 40) | 50 | +34.3 | +33.5 | +1.00 | +32.7 |
| [40, 50) | 38 | +44.9 | +44.5 | +1.00 | +43.9 |
| [50, 60) | 42 | +54.9 | +55.5 | +1.00 | +53.7 |
| [60, 70) | 27 | +66.6 | +66.6 | +1.00 | +66.5 |
| [70, 80) | 29 | +75.9 | +77.8 | +1.00 | +75.8 |
| [80, 90) | 25 | +86.4 | +87.4 | +1.00 | +84.9 |
| [90, 100) | 78 | +99.5 | +100.0 | +1.00 | +100.0 |

### qwen35-9b  (n=600, rho(E,L_pre)=+0.875, rho(E,L_post)=+0.602)

| E bin | n | mean E | med L_pre | med gain_pre | med L_post |
|---|---|---|---|---|---|
| [-100, -90) | 2 | -93.8 | -42.9 | +0.48 | -42.8 |
| [-90, -80) | 2 | -83.6 | -84.9 | +1.02 | +11.3 |
| [-50, -40) | 4 | -43.4 | -63.3 | +1.38 | -40.9 |
| [-40, -30) | 5 | -34.1 | -22.4 | +0.70 | -46.7 |
| [-30, -20) | 9 | -23.8 | -5.6 | +0.26 | -13.6 |
| [-20, -10) | 7 | -12.7 | -17.0 | +1.41 | -3.7 |
| [-10, 0) | 70 | -1.6 | -0.2 | +0.71 | -9.4 |
| [0, 10) | 197 | +2.9 | +1.5 | +0.98 | -49.9 |
| [10, 20) | 65 | +14.1 | +13.0 | +1.00 | +9.9 |
| [20, 30) | 16 | +23.4 | +22.9 | +1.00 | +9.7 |
| [30, 40) | 20 | +35.2 | +36.1 | +1.00 | +28.0 |
| [40, 50) | 12 | +45.4 | +47.7 | +1.02 | +8.5 |
| [50, 60) | 17 | +55.3 | +55.0 | +1.00 | +42.6 |
| [60, 70) | 15 | +65.3 | +65.2 | +1.01 | +62.3 |
| [70, 80) | 38 | +75.4 | +75.9 | +1.00 | +7.3 |
| [80, 90) | 32 | +85.4 | +84.4 | +1.00 | +46.0 |
| [90, 100) | 89 | +96.0 | +96.5 | +1.00 | +36.1 |

## 4. Regions vs the reference lines (counts)

Legend: `L_neg` = L < 0 (opposite to annotated direction); `E_nonpos` = E <= 0 (admitted evidence moves wrong way); `L_gt_E` = L > E (beyond full admitted effect); `L_mid` = E/2 <= L <= E (large residual); `L_small` = 0 <= L < E/2 (small residual).

| scope | arm | n | L_neg | E_nonpos | L_gt_E | L_mid | L_small | frac L_neg |
|---|---|---|---|---|---|---|---|---|
| pooled | pre | 3000 | 827 | 148 | 738 | 879 | 408 | +0.276 |
| pooled | post | 3000 | 1257 | 137 | 519 | 654 | 433 | +0.419 |
| gemma3-12b | pre | 600 | 186 | 27 | 97 | 167 | 123 | +0.310 |
| gemma3-12b | post | 600 | 213 | 32 | 125 | 168 | 62 | +0.355 |
| llama31-8b | pre | 600 | 174 | 54 | 128 | 161 | 83 | +0.290 |
| llama31-8b | post | 600 | 298 | 49 | 65 | 66 | 122 | +0.497 |
| mistral-small-24b | pre | 600 | 239 | 1 | 58 | 146 | 156 | +0.398 |
| mistral-small-24b | post | 600 | 246 | 2 | 85 | 127 | 140 | +0.410 |
| qwen3-8b | pre | 600 | 115 | 33 | 227 | 207 | 18 | +0.192 |
| qwen3-8b | post | 600 | 199 | 33 | 173 | 164 | 31 | +0.332 |
| qwen35-9b | pre | 600 | 113 | 33 | 228 | 198 | 28 | +0.188 |
| qwen35-9b | post | 600 | 301 | 21 | 71 | 129 | 78 | +0.502 |

## 5. Pre/post item-level correspondence

spearman(L_pre, L_post) = +0.642; quadrants: L_pre_<0, L_post_<0 = 650, L_pre_<0, L_post_>=0 = 177, L_pre_>=0, L_post_<0 = 607, L_pre_>=0, L_post_>=0 = 1566.

## 6. Stratified grid (model / source / direction)

| stratum | n | frac E>0 | med E | med L_pre | med L_post | med gain_pre | rho(E,L_pre) |
|---|---|---|---|---|---|---|---|
| gemma3-12b/fever/decrease | 200 | +0.83 | +45.2 | +21.7 | +31.9 | +0.89 | +0.59 |
| gemma3-12b/fever/increase | 200 | +0.94 | +22.2 | +0.3 | -0.3 | +0.11 | +0.67 |
| gemma3-12b/scifact/decrease | 100 | +0.89 | +43.4 | +11.2 | +44.3 | +0.50 | +0.36 |
| gemma3-12b/scifact/increase | 100 | +0.94 | +22.2 | +10.8 | -2.2 | +0.46 | +0.41 |
| llama31-8b/fever/decrease | 200 | +0.66 | +11.0 | +10.6 | +2.2 | +0.76 | +0.62 |
| llama31-8b/fever/increase | 200 | +0.83 | +25.0 | +7.0 | -5.8 | +0.67 | +0.72 |
| llama31-8b/scifact/decrease | 100 | +0.71 | +22.3 | +20.1 | +11.7 | +0.82 | +0.39 |
| llama31-8b/scifact/increase | 100 | +0.95 | +26.8 | +15.4 | -8.4 | +0.74 | +0.61 |
| mistral-small-24b/fever/decrease | 200 | +0.98 | +29.6 | +13.9 | +19.5 | +0.58 | +0.67 |
| mistral-small-24b/fever/increase | 200 | +0.99 | +64.9 | +6.6 | -1.6 | +0.09 | +0.68 |
| mistral-small-24b/scifact/decrease | 100 | +1.00 | +37.5 | +22.1 | +32.8 | +0.59 | +0.69 |
| mistral-small-24b/scifact/increase | 100 | +1.00 | +38.9 | -23.9 | -33.3 | -0.67 | +0.64 |
| qwen3-8b/fever/decrease | 200 | +0.82 | +30.1 | +44.1 | +34.2 | +1.00 | +0.86 |
| qwen3-8b/fever/increase | 200 | +0.86 | +14.8 | +3.9 | -0.0 | +1.00 | +0.84 |
| qwen3-8b/scifact/decrease | 100 | +0.83 | +34.9 | +55.6 | +56.0 | +1.00 | +0.58 |
| qwen3-8b/scifact/increase | 100 | +0.89 | +23.3 | +11.1 | -22.5 | +0.99 | +0.82 |
| qwen35-9b/fever/decrease | 200 | +0.82 | +12.2 | +12.4 | +8.2 | +1.00 | +0.90 |
| qwen35-9b/fever/increase | 200 | +0.85 | +2.0 | +1.9 | -19.6 | +1.00 | +0.89 |
| qwen35-9b/scifact/decrease | 100 | +0.87 | +18.5 | +18.4 | +15.9 | +1.00 | +0.85 |
| qwen35-9b/scifact/increase | 100 | +0.80 | +8.2 | +3.9 | -71.6 | +1.00 | +0.75 |

## 7. Y_base deciles

| Y_base range | n | med E | med L_pre | med gain_pre | frac E>0 |
|---|---|---|---|---|---|
| [0.0, 2.8] | 300 | +1.7 | +1.2 | +0.96 | +0.75 |
| [2.9, 16.0] | 300 | +13.2 | +10.7 | +0.97 | +0.89 |
| [16.1, 31.6] | 300 | +21.9 | +16.3 | +0.83 | +0.92 |
| [31.7, 47.1] | 300 | +36.6 | +22.0 | +0.62 | +0.90 |
| [47.2, 55.6] | 300 | +44.4 | +25.6 | +0.71 | +0.92 |
| [55.6, 66.6] | 300 | +33.7 | +18.7 | +0.55 | +0.90 |
| [66.6, 77.9] | 300 | +23.4 | +18.9 | +0.64 | +0.93 |
| [78.0, 90.3] | 300 | +11.4 | +8.3 | +0.57 | +0.88 |
| [90.4, 99.1] | 300 | +3.7 | +2.4 | +0.96 | +0.86 |
| [99.1, 100.0] | 300 | +0.1 | +0.1 | +1.00 | +0.75 |

## 8. Floor (<=5) / ceiling (>=95) counts per cell

| model | kind | base | admit_pre | admit_post | exclude_pre | exclude_post |
|---|---|---|---|---|---|---|
| gemma3-12b | floor<=5 | 39 | 156 | 150 | 104 | 149 |
| gemma3-12b | ceiling>=95 | 42 | 149 | 136 | 57 | 47 |
| llama31-8b | floor<=5 | 45 | 74 | 66 | 80 | 61 |
| llama31-8b | ceiling>=95 | 52 | 104 | 155 | 50 | 16 |
| mistral-small-24b | floor<=5 | 50 | 165 | 151 | 59 | 96 |
| mistral-small-24b | ceiling>=95 | 30 | 178 | 183 | 17 | 5 |
| qwen3-8b | floor<=5 | 114 | 205 | 203 | 267 | 331 |
| qwen3-8b | ceiling>=95 | 171 | 265 | 273 | 208 | 138 |
| qwen35-9b | floor<=5 | 100 | 220 | 207 | 215 | 225 |
| qwen35-9b | ceiling>=95 | 205 | 277 | 283 | 251 | 46 |

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
| qwen3-8b | g24a_fever_89240 | fever/REFUTES | decrease | 100.0 | 0.0 | 0.0 | 0.0 | +100.0 | +100.0 | +100.0 | Billboard Dad was only released in 1968. |
| qwen3-8b | g24a_fever_204020 | fever/REFUTES | decrease | 100.0 | 0.0 | 0.0 | 0.0 | +100.0 | +100.0 | +100.0 | Down with Love is only a book. |
| qwen3-8b | g24a_fever_12421 | fever/SUPPORTS | increase | 0.0 | 100.0 | 100.0 | 100.0 | +100.0 | +100.0 | +100.0 | Catherine Keener was in the cast of Into the Wild. |
| qwen3-8b | g24a_fever_195503 | fever/SUPPORTS | increase | 0.0 | 100.0 | 100.0 | 100.0 | +100.0 | +100.0 | +100.0 | Offers of appointment to the Supreme Court of the United Sta |
| qwen3-8b | g24a_fever_76869 | fever/SUPPORTS | increase | 0.0 | 100.0 | 100.0 | 0.0 | +100.0 | +100.0 | +0.0 | Jonah Hill was featured in 21 Jump Street. |
| qwen3-8b | g24a_fever_120520 | fever/SUPPORTS | increase | 0.0 | 100.0 | 100.0 | 99.6 | +100.0 | +100.0 | +99.6 | Aarhus is found on the east coast of the Jutland peninsula. |

### smallest_abs_L_pre

| model | item | stratum | dir | Y0 | adm | excl_pre | excl_post | E | L_pre | L_post | claim |
|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3-8b | g24a_fever_219033 | fever/REFUTES | decrease | 0.0 | 0.0 | 0.0 | 0.0 | +0.0 | +0.0 | +0.0 | Savages had no director. |
| qwen3-8b | g24a_fever_132766 | fever/REFUTES | decrease | 0.0 | 0.0 | 0.0 | 0.0 | +0.0 | -0.0 | +0.0 | Wilhelmina Slater's middle name is Natasha. |
| qwen3-8b | g24a_fever_193873 | fever/SUPPORTS | increase | 100.0 | 100.0 | 100.0 | 100.0 | +0.0 | -0.0 | -0.0 | Bea Arthur's date of birth was May 13th, 1922. |
| qwen3-8b | g24a_fever_91976 | fever/REFUTES | decrease | 0.0 | 0.0 | 0.0 | 0.0 | +0.0 | +0.0 | +0.0 | Bank of America withholds products and services. |
| qwen3-8b | g24a_fever_4737 | fever/SUPPORTS | increase | 100.0 | 100.0 | 100.0 | 100.0 | +0.0 | -0.0 | -0.0 | Sausage Party was directed by Greg Tiernan and Conrad Vernon |
| qwen3-8b | g24a_fever_163970 | fever/SUPPORTS | increase | 100.0 | 100.0 | 100.0 | 100.0 | +0.0 | +0.0 | -0.0 | Veeram is a film from 2014. |

### L_pre_negative_flips

| model | item | stratum | dir | Y0 | adm | excl_pre | excl_post | E | L_pre | L_post | claim |
|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3-8b | g24a_fever_27148 | fever/SUPPORTS | increase | 100.0 | 100.0 | 0.0 | 22.3 | +0.0 | -100.0 | -77.7 | Melilla has an area of 12.3 km2 within Africa. |
| qwen35-9b | g24a_fever_16224 | fever/SUPPORTS | increase | 99.1 | 99.4 | 0.8 | 6.8 | +0.3 | -98.3 | -92.3 | Email filtering output is capable of throwing messages away. |
| qwen35-9b | g24a_scifact_277 | scifact/SUPPORT | increase | 99.3 | 99.7 | 2.9 | 5.5 | +0.4 | -96.3 | -93.7 | Commelina yellow mottle virus (ComYMV) has three typical bad |
| qwen35-9b | g24a_fever_196986 | fever/SUPPORTS | increase | 99.3 | 99.4 | 4.5 | 2.8 | +0.1 | -94.8 | -96.5 | Knowledge over ignorance is signified spiritually through Di |
| qwen35-9b | g24a_scifact_71 | scifact/SUPPORT | increase | 96.7 | 98.4 | 4.7 | 35.1 | +1.7 | -92.0 | -61.6 | Activation of the Rac1 homolog CED-10 kills viable cells in  |
| qwen3-8b | g24a_scifact_957 | scifact/SUPPORT | increase | 89.0 | 89.2 | 0.0 | 0.0 | +0.2 | -89.0 | -89.0 | Podocytes are motile and migrate in the presence of injury. |

### E_nonpositive

| model | item | stratum | dir | Y0 | adm | excl_pre | excl_post | E | L_pre | L_post | claim |
|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen35-9b | g24a_fever_105216 | fever/SUPPORTS | increase | 97.4 | 0.1 | 99.9 | 98.0 | -97.3 | +2.5 | +0.6 | Night of the Living Dead is not a series of seven zombie hor |
| gemma3-12b | g24a_fever_209092 | fever/REFUTES | decrease | 0.2 | 95.3 | 0.0 | 0.1 | -95.0 | +0.2 | +0.1 | Stadium Arcadium was released without John Frusciante. |
| qwen35-9b | g24a_fever_146157 | fever/REFUTES | decrease | 8.9 | 99.1 | 97.3 | 95.1 | -90.2 | -88.4 | -86.2 | The New England Patriots lost five Super Bowls. |
| qwen3-8b | g24a_fever_168999 | fever/REFUTES | decrease | 0.0 | 89.3 | 82.1 | 83.4 | -89.3 | -82.1 | -83.4 | Manmohan Singh was a prime minister after the first Prime Mi |
| qwen3-8b | g24a_fever_174033 | fever/REFUTES | decrease | 0.0 | 89.0 | 88.9 | 88.9 | -89.0 | -88.9 | -88.9 | The Endless River is an album by a band formed in London in  |
| qwen35-9b | g24a_fever_21033 | fever/REFUTES | decrease | 11.4 | 97.0 | 100.0 | 1.6 | -85.6 | -88.6 | +9.8 | Victoria Palace Theatre is on the same side of Victoria Stat |

### E_ge40_smallest_abs_L_pre

| model | item | stratum | dir | Y0 | adm | excl_pre | excl_post | E | L_pre | L_post | claim |
|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3-8b | g24a_fever_162743 | fever/SUPPORTS | increase | 0.0 | 100.0 | 0.0 | 0.0 | +100.0 | +0.0 | +0.0 | Aeneas appeared in the Iliad by Homer. |
| qwen3-8b | g24a_fever_68483 | fever/SUPPORTS | increase | 0.0 | 100.0 | 0.0 | 90.5 | +100.0 | +0.0 | +90.5 | Villa Park hosted the 90th FA Community Shield in 2012. |
| gemma3-12b | g24a_fever_177838 | fever/SUPPORTS | increase | 0.0 | 50.0 | 0.0 | 0.0 | +50.0 | +0.0 | +0.0 | Milk is a film. |
| gemma3-12b | g24a_fever_42026 | fever/REFUTES | decrease | 55.6 | 1.8 | 55.5 | 8.1 | +53.7 | +0.0 | +47.4 | Gray Matters was released in May of 2006. |
| gemma3-12b | g24a_fever_86019 | fever/SUPPORTS | increase | 55.6 | 100.0 | 55.5 | 2.4 | +44.4 | -0.0 | -53.1 | Wildfang was established in 2010. |
| qwen35-9b | g24a_fever_63846 | fever/REFUTES | decrease | 98.5 | 2.6 | 98.5 | 0.0 | +95.9 | +0.0 | +98.5 | Edmund H. North died March 12, 1911. |

### E_ge40_L_closest_to_E

| model | item | stratum | dir | Y0 | adm | excl_pre | excl_post | E | L_pre | L_post | claim |
|---|---|---|---|---|---|---|---|---|---|---|---|
| qwen3-8b | g24a_fever_131971 | fever/REFUTES | decrease | 99.7 | 50.0 | 0.0 | 0.0 | +49.7 | +99.7 | +99.7 | Colin Kaepernick is not a starter for the San Francisco 49er |
| qwen3-8b | g24a_scifact_781 | scifact/CONTRADICT | decrease | 100.0 | 50.0 | 0.0 | 0.0 | +50.0 | +100.0 | +100.0 | Mice that lack Interferon-γ or its receptor exhibit high res |
| qwen35-9b | g24a_fever_208917 | fever/REFUTES | decrease | 99.4 | 53.7 | 5.3 | 32.5 | +45.7 | +94.1 | +66.8 | The Monster is only an album. |
| qwen35-9b | g24a_scifact_1137 | scifact/CONTRADICT | decrease | 97.4 | 54.1 | 6.1 | 20.6 | +43.3 | +91.3 | +76.8 | TNFAIP3 is a tumor suppressor in glioblastoma. |
| qwen35-9b | g24a_scifact_149 | scifact/CONTRADICT | decrease | 99.1 | 47.9 | 0.0 | 3.8 | +51.3 | +99.1 | +95.4 | Autophagy deficiency in the liver increases vulnerability to |
| qwen35-9b | g24a_fever_137040 | fever/REFUTES | decrease | 99.1 | 47.9 | 0.0 | 33.5 | +51.3 | +99.1 | +65.6 | The Raven (2012 film) was released in Ireland in April 2012. |

## 11. Histograms (raw counts)

### L_pre (width 5, range [-100, 100))

  -100.0:7  -95.0:4  -90.0:10  -85.0:10  -80.0:9  -75.0:11  -70.0:8  -65.0:15  -60.0:20  -55.0:20  -50.0:21  -45.0:41  -40.0:31  -35.0:52  -30.0:37  -25.0:78  -20.0:40  -15.0:81  -10.0:80  -5.0:252  0.0:442  5.0:157  10.0:204  15.0:109  20.0:154  25.0:71  30.0:135  35.0:78  40.0:92  45.0:66  50.0:69  55.0:91  60.0:32  65.0:61  70.0:42  75.0:56  80.0:34  85.0:60  90.0:43  95.0:177

### L_post - L_pre (width 5, range [-100, 100))

  -100.0:119  -95.0:52  -90.0:32  -85.0:25  -80.0:31  -75.0:32  -70.0:38  -65.0:35  -60.0:37  -55.0:32  -50.0:51  -45.0:85  -40.0:89  -35.0:73  -30.0:81  -25.0:96  -20.0:93  -15.0:120  -10.0:154  -5.0:624  0.0:471  5.0:122  10.0:104  15.0:75  20.0:49  25.0:44  30.0:44  35.0:31  40.0:39  45.0:21  50.0:19  55.0:34  60.0:7  65.0:5  70.0:5  75.0:5  80.0:3  85.0:7  90.0:7  95.0:9

### gain_pre, E>0 (width 0.1 over [-1, 2); tails listed after)

  -1.0:19  -0.9:20  -0.8:10  -0.7:21  -0.6:25  -0.5:22  -0.4:26  -0.3:33  -0.2:28  -0.1:75  +0.0:126  +0.1:65  +0.2:70  +0.3:83  +0.4:64  +0.5:79  +0.6:77  +0.7:82  +0.8:121  +0.9:520  +1.0:409  +1.1:68  +1.2:49  +1.3:27  +1.4:26  +1.5:14  +1.6:13  +1.7:11  +1.8:9  +1.9:112

  tails: below -1.0 = 306 rows; at/above 1.9 (incl. >=2.0 clipped into 1.9 display bin) = 112 rows; raw >=2.0 = 0 rows.

## 12. Figures

- `results/discovery/figs/E_vs_Lpre.png`
- `results/discovery/figs/E_vs_Lpost.png`
- `results/discovery/figs/Lpre_vs_Lpost.png`
