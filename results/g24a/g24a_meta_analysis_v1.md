# G24A §14 explanation experiment — second-order / meta-evidence readout (v1, 2026-09-26)

Registration §14.4 estimands on the committed 200 discovery same-claim pairs x 13 cells x 6 models (incl. the frozen Qwen3-32B) = 15,600 rows. **Reporting, NOT gates**: paired percentile bootstrap 95% CIs over claims (B = 10,000, seed `g24a_meta_ci_v1`), per-model consistency n/6, no p-values, no thresholds, no selection — every claim and model is included. Integrity: `check_g24a_meta_raws.py --require6` green. The four legacy operators were re-run in this batch (byte-identical prompts), so every contrast below is same-run, same-anchor.

## 1. All thirteen cell means (pooled, 0..100)

| cell | pooled | 95% CI | per-model (6) |
|---|---:|---:|---|
| Y0 | 49.92 | [46.09, 53.72] | 41.1, 56.6, 53.7, 41.8, 59.2, 47.1 |
| ADM+ | 90.27 | [87.91, 92.41] | 90.5, 82.9, 92.7, 92.2, 88.8, 94.5 |
| ADM- | 30.85 | [26.81, 34.94] | 24.1, 44.2, 32.6, 23.2, 39.4, 21.6 |
| EXC+ | 46.88 | [44.45, 49.27] | 25.7, 54.9, 55.5, 35.5, 65.1, 44.6 |
| EXC- | 28.63 | [26.30, 31.08] | 20.7, 48.8, 19.5, 18.6, 34.2, 30.1 |
| STR+ | 46.40 | [43.79, 48.96] | 37.0, 46.9, 42.6, 48.9, 57.6, 45.4 |
| STR- | 39.24 | [36.67, 41.87] | 32.2, 51.6, 31.0, 25.5, 54.6, 40.3 |
| CF+ | 50.55 | [48.16, 52.92] | 42.4, 43.5, 47.0, 69.9, 53.4, 47.0 |
| CF- | 39.74 | [37.56, 41.93] | 39.3, 46.5, 29.2, 29.9, 53.4, 40.2 |
| MNR+ | 61.21 | [58.40, 63.89] | 44.2, 50.9, 68.1, 76.7, 71.7, 55.7 |
| MNR- | 35.83 | [32.97, 38.72] | 32.4, 48.7, 29.3, 22.8, 42.1, 39.7 |
| RND+ | 49.45 | [47.12, 51.65] | 42.1, 43.1, 43.9, 67.7, 53.1, 46.8 |
| RND- | 40.93 | [38.70, 43.21] | 38.2, 48.1, 32.2, 31.4, 53.2, 42.5 |

## 2. CRE — counterfactual restoration error (§14.4 criterion)

| estimand | pooled | 95% CI | registered expectation |
|---|---:|---:|---|
| CRE_abs(ordinary exclude_post) = mean|Y0 − M| | +31.00 | [+29.11, +32.90] | table |
| CRE_abs(strong_exclude_post) = mean|Y0 − M| | +27.30 | [+25.67, +28.99] | table |
| CRE_abs(counterfactual_delete_post) = mean|Y0 − M| | +29.77 | [+28.09, +31.46] | table |
| CRE_abs(meta_neutral_post (MNR)) = mean|Y0 − M| | +29.44 | [+27.73, +31.20] | MNR < CF, RND < CF |
| CRE_abs(random_reason_post) = mean|Y0 − M| | +29.70 | [+27.99, +31.43] | MNR < CF, RND < CF |
| CRE_sgn(ordinary exclude_post) = mean(Y0 − M) | +12.17 | [+9.16, +15.14] | descriptive (no registered sign) |
| CRE_sgn(strong_exclude_post) = mean(Y0 − M) | +7.10 | [+4.51, +9.74] | descriptive (no registered sign) |
| CRE_sgn(counterfactual_delete_post) = mean(Y0 − M) | +4.78 | [+2.08, +7.50] | descriptive (no registered sign) |
| CRE_sgn(meta_neutral_post (MNR)) = mean(Y0 − M) | +1.40 | [-1.45, +4.23] | descriptive (no registered sign) |
| CRE_sgn(random_reason_post) = mean(Y0 − M) | +4.73 | [+2.00, +7.51] | descriptive (no registered sign) |
| CRE(MNR) − CRE(CF) | -0.32 | [-1.62, +0.99] | < 0 |
| CRE(RND) − CRE(CF) | -0.07 | [-0.82, +0.68] | < 0 |

## 3. Separation — first-order direction (must not reopen)

| estimand | pooled | 95% CI | registered expectation |
|---|---:|---:|---|
| sep(admit_post) | +59.42 | [+55.02, +63.88] | direction anchor |
| sep(ordinary exclude_post) | +18.24 | [+15.65, +20.84] | ≈ 0 (MNR/CF/RND) / table |
| sep(strong_exclude_post) | +7.17 | [+5.11, +9.20] | ≈ 0 (MNR/CF/RND) / table |
| sep(counterfactual_delete_post) | +10.81 | [+9.00, +12.62] | ≈ 0 (MNR/CF/RND) / table |
| sep(meta_neutral_post (MNR)) | +25.38 | [+22.49, +28.24] | ≈ 0 (MNR/CF/RND) / table |
| sep(random_reason_post) | +8.52 | [+6.72, +10.29] | ≈ 0 (MNR/CF/RND) / table |
| sep(MNR) − sep(admit) | -34.04 | [-38.27, -29.97] | < 0 |
| sep(MNR) − sep(CF) | +14.57 | [+11.88, +17.23] | ≈ 0 (no registered sign) |

## 4. Reconstruction trajectory (claim-level, model-averaged)

| estimand | pooled | 95% CI | registered expectation |
|---|---:|---:|---|
| corr(M_EXC, Y0) | +0.607 | [+0.506, +0.692] | > 0 |
| corr(M_STR, Y0) | +0.730 | [+0.656, +0.792] | > 0 |
| corr(M_CF, Y0) | +0.713 | [+0.641, +0.776] | > 0 |
| corr(M_MNR, Y0) | +0.659 | [+0.563, +0.739] | > 0 |
| corr(M_RND, Y0) | +0.708 | [+0.630, +0.776] | > 0 |
| OLS slope (M_EXC ~ Y0) | +0.323 | [+0.248, +0.397] | table |
| OLS slope (M_STR ~ Y0) | +0.454 | [+0.385, +0.520] | table |
| OLS slope (M_CF ~ Y0) | +0.397 | [+0.334, +0.459] | table |
| OLS slope (M_MNR ~ Y0) | +0.421 | [+0.339, +0.498] | MNR > CF, toward 1 |
| OLS slope (M_RND ~ Y0) | +0.383 | [+0.317, +0.447] | table |
| slope(MNR) − slope(CF) | +0.024 | [-0.035, +0.081] | > 0 |
| corr(MNR) − corr(CF) | -0.053 | [-0.132, +0.018] | > 0 |

- Committed context (descriptive, never a gate):
  - fresh ConfB (same-run §13.5): CRE(CF) = 29.96, sep(admit) = 62.95, sep(CF) = 8.33, slope = 0.320, corr = 0.635.
  - discovery P2 (5 models): slope(CF) = 0.385, corr(CF) = 0.701.

## 5. Per-model consistency (n/6)

- CRE(MNR) < CRE(CF): **4 / 6**
- CRE(RND) < CRE(CF): **2 / 6**
- sep(MNR) < sep(admit): **6 / 6**
- sep(MNR) on the pooled sign (≈0 has no registered sign): **6 / 6**
- slope(MNR) > slope(CF): **5 / 6**
- corr(MNR) > corr(CF): **2 / 6**

Per-model values:

| model | CRE_EXC | CRE_STR | CRE_CF | CRE_MNR | CRE_RND | sep_adm | sep_MNR | r_CF | r_MNR | slope_CF | slope_MNR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| mistral-small-24b | 30.70 | 24.18 | 27.66 | 25.38 | 27.82 | 66.44 | +11.74 | +0.462 | +0.503 | +0.220 | +0.331 |
| llama31-8b | 26.18 | 29.61 | 31.67 | 28.80 | 32.67 | 38.72 | +2.24 | +0.261 | +0.367 | +0.169 | +0.224 |
| qwen3-8b | 33.62 | 30.47 | 32.85 | 31.67 | 31.99 | 60.10 | +38.88 | +0.416 | +0.385 | +0.262 | +0.273 |
| qwen35-9b | 37.23 | 30.01 | 30.66 | 36.28 | 31.02 | 69.01 | +53.87 | +0.482 | +0.312 | +0.333 | +0.187 |
| gemma3-12b | 25.77 | 20.37 | 24.12 | 22.61 | 24.37 | 49.39 | +29.60 | +0.477 | +0.464 | +0.145 | +0.310 |
| qwen3-32b | 32.52 | 29.14 | 31.64 | 31.91 | 30.32 | 72.87 | +15.95 | +0.395 | +0.392 | +0.206 | +0.222 |

## 6. Reading rules (registered)

- Everything above is reported as-is whatever the outcome (§14.4 interpretation rule); CIs quantify claim-sampling uncertainty, n/6 shows whether a pattern spans the panel rather than resting on one model.
- Registered expectations are quoted for the reader, never evaluated as pass/fail — there are no gates, thresholds, or p-values anywhere in this report.
- Pooled means average all (model, claim) cells (discovery convention); corr/slope use claim-level series first averaged over the 6 models; `mean|Y0 − M|` takes the cell-level absolute value before averaging. The bootstrap recomputes every ratio and correlation inside each resample (NaN replicates skipped: 0/10000).
- Conceptual framing (§14.4): CRE = |Y0 − M| is proposed as *the* retraction-success criterion — evidence suppression (forget rate) and counterfactual restoration are different properties, and a retraction operator succeeds only when the judgment it leaves behind equals the judgment that never saw the evidence.
- Scope: this is RQ3's explanation experiment (§14 ruling); internal layerwise/patching analysis is out of scope this round and requires a new user ruling.
