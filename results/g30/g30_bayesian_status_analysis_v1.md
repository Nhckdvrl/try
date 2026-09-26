# G30 Bayesian-status pilot — full analysis

40 audited factorial cases × 4 conditions × 3 models = 480 raw outputs. All parse and completion checks passed. This is an exploratory constructed-task anchor, not a fresh natural-evidence confirmation.

Frozen item SHA-256: `69b2df166a9307ea9fcc4c0e35392b0640ac6db89e13d042040ce735bee59fcb`.

Positive signed N−I or R−N means movement toward the inadmissible E1; negative means movement away from it.

| Group | N−I signed probability | N−I absolute | N/I choice disagreement | R−N signed probability | R−N absolute | R/N choice disagreement |
|---|---:|---:|---:|---:|---:|---:|
| pooled | +0.16 [-1.18, +1.57] | +3.91 [+2.44, +5.69] | +0.04 [+0.01, +0.07] | +6.38 [+4.67, +8.05] | +8.57 [+6.89, +10.65] | +0.03 [+0.00, +0.06] |
| qwen3-8b | -2.55 [-5.80, +1.15] | +5.55 [+2.85, +8.82] | +0.10 [+0.03, +0.20] | -0.71 [-5.31, +2.65] | +5.46 [+2.45, +9.84] | +0.00 [+0.00, +0.00] |
| gemma3-12b | +4.13 [+1.39, +7.63] | +4.67 [+1.99, +8.07] | +0.03 [+0.00, +0.07] | +15.86 [+12.74, +18.99] | +16.21 [+13.26, +19.14] | +0.07 [+0.00, +0.17] |
| mistral-small-24b | -1.10 [-2.08, -0.26] | +1.51 [+0.76, +2.45] | +0.00 [+0.00, +0.00] | +3.98 [+2.52, +5.53] | +4.04 [+2.58, +5.55] | +0.00 [+0.00, +0.00] |
| e2_blue | +0.87 [-0.66, +2.40] | +4.77 [+2.27, +7.90] | +0.02 [+0.00, +0.05] | +8.65 [+6.83, +10.44] | +8.99 [+7.54, +10.54] | +0.05 [+0.00, +0.10] |
| e2_yellow | -0.55 [-2.57, +1.95] | +3.04 [+1.47, +5.10] | +0.07 [+0.02, +0.13] | +4.10 [+1.46, +6.54] | +8.15 [+5.36, +12.32] | +0.00 [+0.00, +0.00] |

Choice disagreement is a fraction of paired cells. Probability contrasts and absolute error are percentage points.

## Absolute error versus Bayesian posterior

| Group | D | N | I | R | R−N error | N−I error |
|---|---:|---:|---:|---:|---:|---:|
| pooled | +7.49 [+5.78, +9.58] | +10.05 [+7.79, +12.60] | +8.69 [+6.88, +10.65] | +14.20 [+12.13, +16.50] | +4.15 [+2.45, +5.82] | +1.36 [+0.11, +2.79] |
| qwen3-8b | +8.64 [+6.40, +11.10] | +12.46 [+8.45, +17.58] | +10.06 [+7.44, +12.88] | +9.76 [+7.20, +12.50] | -2.69 [-7.22, +0.58] | +2.39 [-0.28, +5.75] |
| gemma3-12b | +7.70 [+5.45, +10.79] | +11.14 [+7.76, +15.02] | +9.55 [+6.73, +12.79] | +24.24 [+20.07, +28.63] | +13.10 [+9.60, +16.57] | +1.59 [-1.06, +4.42] |
| mistral-small-24b | +6.14 [+4.21, +8.50] | +6.55 [+4.64, +8.74] | +6.46 [+4.58, +8.60] | +8.60 [+6.44, +10.90] | +2.05 [+0.48, +3.68] | +0.10 [-0.76, +0.99] |
| e2_blue | +5.86 [+4.35, +7.44] | +8.69 [+6.24, +11.41] | +7.00 [+4.85, +9.48] | +13.66 [+11.16, +16.50] | +4.97 [+2.86, +6.96] | +1.68 [-0.10, +3.65] |
| e2_yellow | +9.13 [+6.27, +12.73] | +11.41 [+7.75, +15.80] | +10.38 [+7.75, +13.36] | +14.74 [+11.59, +18.41] | +3.33 [+0.60, +6.01] | +1.03 [-0.60, +3.16] |

## Uptake of valid E2

For matched prior/reliability cells, the table shows predicted P(Blue) after a Blue E2 minus predicted P(Blue) after a Yellow E2. This gauges whether each condition still uses E2.

| Group | D | N | I | R |
|---|---:|---:|---:|---:|
| qwen3-8b | 45.35 | 49.65 | 44.55 | 51.08 |
| gemma3-12b | 53.08 | 49.72 | 57.98 | 18.00 |
| mistral-small-24b | 57.40 | 54.17 | 51.98 | 46.21 |
| pooled | 51.94 | 51.18 | 51.50 | 38.43 |

Case-cluster bootstrap intervals use 5,000 draws. The 40 cases are a designed factorial, so these intervals describe the stimulus grid rather than population sampling.

The JSON companion contains all paired cells and source hashes. Interpretation is reported separately after examining the results; no item was removed based on outputs.
