# Pilot P1 — retraction-operator discrimination (Layer 2)

Frozen readout: `g24a_competing_accounts_v1.md` §4 — A = s(Y_Admit − Y_Base), C_k = s(Y_k − Y_Admit), R_k = s(Y_k − Y_Base), D_k = |Y_k − Y_Base|; ideal removal R_k = 0 / C_k = −A; no-effect C_k = 0; s = +1 increase, −1 decrease.  No gates, no p-values, no bootstrap, no selection — leverage bands are descriptive only.

## Integrity

- rows: 4800 (5 models × 960) — expected 4,800
- unparsed decisions: 0
- digit-mass < 0.5: 0
- rationale hit token cap: 0
- per model: mistral-small-24b=960, llama31-8b=960, gemma3-12b=960, qwen3-8b=960, qwen35-9b=960
- per-item identity C_k = R_k − A asserted on every cell

## 1. Trajectories — mean Y (0..100), pooled over 5 models

| polarity | Base | AdmitPost | ExcludePost | StrongExcludePost | CounterfactualDeletePost |
|---|---|---|---|---|---|
| increase | 79.09 | 92.44 | 50.24 | 60.12 | 60.62 |
| decrease | 22.78 | 20.15 | 17.36 | 24.14 | 26.06 |
| all | 50.94 | 56.30 | 33.80 | 42.13 | 43.34 |

Per model (all):

| polarity | Base | AdmitPost | ExcludePost | StrongExcludePost | CounterfactualDeletePost |
|---|---|---|---|---|---|
| mistral-small-24b | 44.57 | 52.44 | 24.44 | 38.21 | 40.72 |
| llama31-8b | 52.53 | 62.02 | 44.54 | 44.23 | 39.90 |
| gemma3-12b | 54.09 | 55.99 | 44.00 | 51.81 | 50.60 |
| qwen3-8b | 54.30 | 58.21 | 33.10 | 35.57 | 38.84 |
| qwen35-9b | 49.19 | 52.83 | 22.94 | 40.82 | 46.63 |

Per polarity, per model:

| polarity | Base | AdmitPost | ExcludePost | StrongExcludePost | CounterfactualDeletePost |
|---|---|---|---|---|---|
| mistral-small-24b inc | 75.77 | 91.52 | 34.84 | 56.90 | 58.36 |
| llama31-8b inc | 77.29 | 90.12 | 56.14 | 48.45 | 44.06 |
| gemma3-12b inc | 78.07 | 91.57 | 67.61 | 68.93 | 57.26 |
| qwen3-8b inc | 82.76 | 94.69 | 57.94 | 60.64 | 60.19 |
| qwen35-9b inc | 81.57 | 94.32 | 34.69 | 65.68 | 83.24 |
| mistral-small-24b dec | 13.36 | 13.36 | 14.05 | 19.51 | 23.07 |
| llama31-8b dec | 27.76 | 33.92 | 32.94 | 40.01 | 35.74 |
| gemma3-12b dec | 30.11 | 20.40 | 20.40 | 34.70 | 43.93 |
| qwen3-8b dec | 25.85 | 21.72 | 8.25 | 10.50 | 17.50 |
| qwen35-9b dec | 16.81 | 11.34 | 11.18 | 15.96 | 10.03 |

## 2. Frozen quantities (pooled over 5 models × 192 claims)

| quantity | ExcludePost | StrongExcludePost | CounterfactualDeletePost |
|---|---|---|---|
| A (leverage) | 7.99 | 7.99 | 7.99 |
| C_k | -19.71 | -18.15 | -18.86 |
| R_k | -11.72 | -10.16 | -10.87 |
| D_k | 28.26 | 22.64 | 23.64 |
| C_k / -A (display) | 2.47 | 2.27 | 2.36 |

A by polarity: increase 13.35, decrease 2.63

| polarity x k | ExcludePost | StrongExcludePost | CounterfactualDeletePost |
|---|---|---|---|
| increase C_k | -42.20 | -32.32 | -31.82 |
| decrease C_k | 2.79 | -3.99 | -5.91 |
| increase R_k | -28.85 | -18.97 | -18.47 |
| decrease R_k | 5.42 | -1.36 | -3.27 |
| increase D_k | 36.46 | 25.14 | 27.59 |
| decrease D_k | 20.07 | 20.15 | 19.69 |

## 3. Per model — A, C_k, R_k

| model | A | C ExcludePost | C StrongExcludePost | C CounterfactualDeletePost | R ExcludePost | R StrongExcludePost | R CounterfactualDeletePost |
|---|---|---|---|---|---|---|---|
| mistral-small-24b | 7.87 | -28.69 | -20.39 | -21.44 | -20.81 | -12.51 | -13.56 |
| llama31-8b | 3.34 | -16.50 | -23.88 | -23.94 | -13.16 | -20.54 | -20.60 |
| gemma3-12b | 11.61 | -11.98 | -18.47 | -28.92 | -0.37 | -6.86 | -17.31 |
| qwen3-8b | 8.03 | -11.63 | -11.41 | -15.14 | -3.60 | -3.38 | -7.11 |
| qwen35-9b | 9.11 | -29.73 | -16.63 | -4.89 | -20.63 | -7.52 | 4.22 |

## 4. Within-pair dC_k = C_k^inc − C_k^dec

| k | pooled mean | % negative | n | mistral-small-24b | llama31-8b | gemma3-12b | qwen3-8b | qwen35-9b |
|---|---|---|---|---|---|---|---|---|
| ExcludePost | -44.98 | 86.7% | 480 | -55.99 | -34.97 | -23.97 | -50.22 | -59.79 |
| StrongExcludePost | -28.33 | 71.0% | 480 | -28.46 | -35.58 | -8.34 | -45.26 | -24.02 |
| CounterfactualDeletePost | -25.91 | 69.8% | 480 | -23.44 | -44.24 | -10.78 | -38.72 | -12.39 |

## 5. Leverage bands (descriptive only — nothing filtered)

| A band | n | mean A | C/R ExcludePost | C/R StrongExcludePost | C/R CounterfactualDeletePost |
|---|---|---|---|---|---|
| (-inf, 0) | 363 | -15.47 | -1.5 / -17.0 | 1.0 / -14.5 | -2.2 / -17.7 |
| (0, 10) | 318 | 1.99 | -26.4 / -24.4 | -21.6 / -19.6 | -21.3 / -19.3 |
| (10, 20) | 75 | 12.73 | -26.7 / -14.0 | -29.7 / -17.0 | -29.7 / -17.0 |
| (20, 30) | 46 | 23.74 | -36.9 / -13.1 | -38.0 / -14.2 | -38.2 / -14.4 |
| (30, 40) | 36 | 34.65 | -31.4 / 3.3 | -33.0 / 1.7 | -34.3 / 0.3 |
| (40, inf) | 122 | 76.72 | -42.2 / 34.5 | -47.3 / 29.4 | -43.5 / 33.2 |

## 6. P/Q/R/S discriminating quantities (pre-registered reading aids)

Map: `g24a_competing_accounts_v1.md` §4. Values below are the frozen quantities each pattern discriminates on:

- **P** (disregard ≠ act-as-if-unseen): ExcludePost C/−A large, StrongExclude still large, CounterfactualDelete close to −1 with decrease-side R near 0 → per k: C/−A and decrease-side R_k.
- **Q** (generic instruction strength): StrongExclude and CounterfactualDelete improve similarly → gap between their C/−A.
- **R** (contradiction persists / Account A): neither new operator rescues — C_k ≈ 0 while Y_intervention ≈ Y_Admit on the decrease side.
- **S** (exclusion semantically misimplemented): CounterfactualDelete brings both sides to Base while ordinary exclusion overshoots (C/−A > 1) or sticks (≈ 0).

Numbers (per polarity, C_k / −A):

| polarity | ExcludePost | StrongExcludePost | CounterfactualDeletePost |
|---|---|---|---|
| increase | 3.16 | 2.42 | 2.38 |
| decrease | -1.06 | 1.51 | 2.24 |
| all | 2.47 | 2.27 | 2.36 |

Decrease-side R_k (residual vs Base; 0 = ideal return): ExcludePost=5.42, StrongExcludePost=-1.36, CounterfactualDeletePost=-3.27

## 7. Caveats

- Exploratory discriminator (no KILL gate by ruling); any item-level statement carries the temp-0 retest caveat (`g24a_data_quality_audit_v1.md` §E).
- `e3e954d` lineage is discovery-only; this pilot's items are strict-fresh and validity-reviewed zero-model.
- No rationale coding in this round (deferred by ruling).
