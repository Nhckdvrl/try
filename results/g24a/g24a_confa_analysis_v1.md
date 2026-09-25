# G24A Confirmation A — RQ1/F1 replication (v1, 2026-09-26)

Registration §13.5 estimands on 500 fresh FEVER/SciFact items x 5 cells x 6 models (incl. the frozen Qwen3-32B) = 15,000 rows; effects sign-normalized by critical_direction (+1 increase / -1 decrease). **Reporting, NOT gates**: paired percentile bootstrap 95% CIs over claims (B = 10,000, seed `g24a_confa_ci_v1`), per-model consistency n/6, no p-values, no thresholds, no selection — every item and model is included. Integrity: `check_g24a_confa_raws.py --require6` green (15000 rows).

## 1. All five cell means (pooled, 0..100)

| cell | pooled | 95% CI | per-model (6) |
|---|---:|---:|---|
| base | 57.45 | [54.32, 60.62] | 53.8, 58.9, 62.1, 57.1, 59.7, 53.1 |
| admit_pre | 62.21 | [58.43, 65.94] | 59.3, 64.1, 65.5, 61.6, 60.7, 62.0 |
| admit_post | 62.41 | [58.59, 66.18] | 60.5, 66.0, 64.6, 60.9, 60.5, 61.9 |
| exclude_pre | 52.29 | [49.22, 55.39] | 38.1, 57.6, 56.4, 57.3, 54.1, 50.3 |
| exclude_post | 37.33 | [35.18, 39.52] | 25.1, 46.6, 42.2, 22.4, 47.4, 40.3 |

## 2. Primary estimands (signed by direction)

| estimand | pooled | 95% CI | registered expectation |
|---|---:|---:|---|
| E1 signed(ExcludePre − Base) | -0.15 | [-1.68, +1.40] | prospective leakage > 0 |
| E2 signed(ExcludePost − Base) | -15.94 | [-18.19, -13.78] | retrospective leakage, expected small vs E1 |
| E3 signed(AdmitPre − Base) | +9.68 | [+7.83, +11.53] | timing-matched admitted baseline |
| E4 signed(AdmitPost − Base) | +9.80 | [+8.00, +11.65] | timing-matched admitted baseline |
| E1 − E2 | +15.80 | [+14.20, +17.43] | > 0 (E1 ≫ E2) |
| E1 / E3 | -0.02 | [-0.20, +0.13] | > 0 (substantially > 0) |
| E2 / E4 | -1.63 | [-2.12, -1.26] | close to 0 (no registered sign) |

## 3. Per-model consistency (n/6)

- E1 − E2 > 0: **6 / 6**
- E1 / E3 > 0: **5 / 6**
- E2 / E4 < E1 / E3 (the ≈0 estimand's sign-free consistency: registered quantities only): **6 / 6**

Per-model values:

| model | E1 | E2 | E3 | E4 | E1−E2 | E1/E3 | E2/E4 |
|---|---:|---:|---:|---:|---:|---:|---:|
| mistral-small-24b | -17.55 | -29.64 | +7.36 | +7.05 | +12.10 | -2.384 | -4.204 |
| llama31-8b | +1.78 | -14.27 | +6.74 | +7.43 | +16.06 | +0.265 | -1.922 |
| qwen3-8b | +8.19 | -2.77 | +10.78 | +11.46 | +10.95 | +0.759 | -0.242 |
| qwen35-9b | +5.27 | -32.24 | +8.47 | +8.84 | +37.51 | +0.622 | -3.646 |
| gemma3-12b | +0.20 | -2.35 | +13.67 | +12.82 | +2.55 | +0.015 | -0.184 |
| qwen3-32b | +1.23 | -14.38 | +11.05 | +11.22 | +15.61 | +0.111 | -1.281 |

## 4. Reading rules (registered)

- Everything above is reported as-is whatever the outcome (§13.5 interpretation rule); CIs quantify claim-sampling uncertainty, n/6 shows whether a pattern spans the panel rather than resting on one model.
- Leak fractions E1/E3 and E2/E4 divide pooled signed means; the bootstrap recomputes the ratio inside each resample (NaN-denominator replicates skipped: 0/10000).
- After ConfA + ConfB are reported: experiments stop (§13.1).
