# G24A Confirmation B — RQ2/F2 + RQ3/F3 replication (v1, 2026-09-26)

Registration §13.5 estimands on 200 fresh VitaminC SR pairs (3 items each) x 7 cells x 6 models (incl. the frozen Qwen3-32B) = 8,400 rows. **Reporting, NOT gates**: paired percentile bootstrap 95% CIs over claims (B = 10,000, seed `g24a_confb_ci_v1`), per-model consistency n/6, no p-values, no thresholds, no selection — every claim and model is included. Integrity: `check_g24a_confb_raws.py --require6` green.

## 1. All seven cell means (pooled, 0..100)

| cell | pooled | 95% CI | per-model (6) |
|---|---:|---:|---|
| Y0 | 48.07 | [44.31, 51.83] | 39.8, 53.1, 51.3, 45.9, 58.7, 39.6 |
| A+ | 89.85 | [87.43, 92.11] | 91.3, 82.1, 91.1, 91.1, 87.6, 95.8 |
| CF+ | 47.42 | [45.24, 49.60] | 40.4, 41.2, 44.3, 60.3, 52.9, 45.4 |
| A- | 26.90 | [23.08, 30.78] | 22.9, 33.6, 33.3, 19.8, 35.3, 16.5 |
| CF- | 39.08 | [37.09, 41.10] | 36.8, 44.8, 32.8, 26.1, 53.1, 40.9 |
| W | 43.59 | [40.64, 46.54] | 40.8, 43.4, 40.5, 48.6, 50.7, 37.6 |
| I | 43.96 | [41.07, 46.90] | 39.1, 43.3, 41.1, 36.1, 53.4, 50.7 |

## 2. RQ2 / F2 — suppression vs restoration

| estimand | pooled | 95% CI | registered expectation |
|---|---:|---:|---|
| separation_admit = mean(A+ − A−) | +62.95 | [+58.33, +67.38] | admitted direction effect |
| separation_cf = mean(CF+ − CF−) | +8.33 | [+6.64, +10.07] | post-retraction direction effect |
| gap = separation_cf − separation_admit | -54.62 | [-59.05, -50.01] | < 0 (cf ≪ admit) |
| erased fraction = 1 − cf/admit | +0.868 | [+0.840, +0.894] | descriptive |
| mean(Y0 − M_CF) | +4.82 | [+1.87, +7.73] | ≠ ~0 (no registered sign) |
| mean|Y0 − M_CF| | +29.96 | [+28.15, +31.81] | still large (≠ ~0) |

## 3. RQ3 / F3 — new inference state (claim-level)

| estimand | pooled | 95% CI | registered expectation |
|---|---:|---:|---|
| corr(M_CF, Y0) | +0.635 | [+0.541, +0.717] | > 0 |
| OLS slope (M_CF ~ Y0) | +0.320 | [+0.250, +0.389] | < 1 |
| OLS intercept | +27.87 | [+24.36, +31.50] | descriptive |
| center mean W (WithheldCF) | +43.59 | [+40.64, +46.54] | > I ≈ M_CF |
| center mean I (IrrelCF) | +43.96 | [+41.07, +46.90] | ≈ M_CF |
| center mean M_CF | +43.25 | [+41.35, +45.19] | anchor |
| W − I | -0.36 | [-2.44, +1.61] | > 0 |
| W − M_CF | +0.34 | [-1.80, +2.50] | > 0 |
| I − M_CF | +0.71 | [-1.44, +2.90] | ≈ 0 (no registered sign) |
| dW = mean|W − 50| | +27.22 | [+25.69, +28.71] | > dI > dM |
| dI = mean|I − 50| | +27.75 | [+26.42, +29.11] | middle |
| dM = mean|M_CF − 50| | +17.07 | [+15.95, +18.21] | smallest |
| dW − dI | -0.53 | [-1.60, +0.53] | > 0 |
| dI − dM | +10.68 | [+9.32, +12.04] | > 0 |

- Descriptive scale reference (committed, discovery): temp-0 noise floor mean|diff| = 1.84 — every reconstruction/center gap above is read against this, calibration only (never a gate).

## 4. Per-model consistency (n/6)

- separation_cf < separation_admit: **6 / 6**
- mean(Y0 − M_CF) on the pooled sign (≈0 has no registered sign): **5 / 6**
- corr(M_CF, Y0) > 0: **6 / 6**
- OLS slope < 1: **6 / 6**
- W − I > 0: **3 / 6**
- W − M_CF > 0: **4 / 6**
- I − M_CF on the pooled sign (≈0 has no registered sign): **5 / 6**
- dW − dI > 0: **3 / 6**
- dI − dM > 0: **6 / 6**

Per-model values:

| model | sep_adm | sep_cf | erased | Y0−MCF | |Y0−MCF| | r | slope | W | I | M_CF | W−I | I−M | dW−dI | dI−dM |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| mistral-small-24b | 68.43 | 3.56 | 0.948 | +1.25 | 27.35 | +0.470 | +0.192 | 40.85 | 39.11 | 38.57 | +1.73 | +0.54 | +1.10 | +9.59 |
| llama31-8b | 48.49 | -3.58 | 1.074 | +10.03 | 31.08 | +0.271 | +0.186 | 43.40 | 43.27 | 43.03 | +0.13 | +0.24 | -2.74 | +4.29 |
| qwen3-8b | 57.89 | 11.47 | 0.802 | +12.77 | 33.26 | +0.400 | +0.245 | 40.45 | 41.11 | 38.57 | -0.66 | +2.54 | -9.08 | +20.58 |
| qwen35-9b | 71.34 | 34.24 | 0.520 | +2.70 | 34.09 | +0.333 | +0.220 | 48.57 | 36.14 | 43.21 | +12.43 | -7.07 | +2.56 | +11.81 |
| gemma3-12b | 52.35 | -0.21 | 1.004 | +5.65 | 23.65 | +0.424 | +0.141 | 50.73 | 53.41 | 53.01 | -2.68 | +0.40 | -1.57 | +5.25 |
| qwen3-32b | 79.21 | 4.50 | 0.943 | -3.50 | 30.30 | +0.433 | +0.214 | 37.57 | 50.71 | 43.12 | -13.14 | +7.59 | +6.56 | +12.55 |

## 5. Reading rules (registered)

- Everything above is reported as-is whatever the outcome (§13.5 interpretation rule); CIs quantify claim-sampling uncertainty, n/6 shows whether a pattern spans the panel rather than resting on one model.
- Pooled means average all (model, claim) cells (discovery convention); corr/slope and the center/dispersion ordering use claim-level series first averaged over the 6 models.
- `mean|Y0 − M_CF|` takes the cell-level absolute value before averaging; the bootstrap recomputes every ratio and correlation inside each resample (NaN replicates skipped: 0/10000).
- After ConfA + ConfB are reported: experiments stop (§13.1).
