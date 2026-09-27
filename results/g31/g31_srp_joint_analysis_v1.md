# G31 joint S/R/P pilot analysis

Frozen selected items: 60. Three completed models (Llama substituted for Mistral after documented NCCL failure); 4320 complete raw outputs. Claim-cluster bootstrap, 5,000 draws. All items and rows included. This is an exploratory pilot on reused G29 natural E2 pairs and locally constructed, audited X notes.

## Direct X suppression and paired restoration

| Model | Active X separation A | Excluded X separation N | Absolute X effect A / N | A−N absolute X effect | N−D absolute CRE | I−D absolute frame cost | N−I absolute | Binary X disagreement A / N |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| pooled | +14.32 [+9.43,+19.02] | -4.80 [-9.37,-0.34] | +25.56 [+21.02,+30.14] / +15.78 [+11.94,+19.82] | +9.78 [+3.94,+15.67] | +17.27 [+13.68,+21.14] | +12.73 [+9.18,+16.58] | +13.41 [+10.62,+16.49] | 0.247 / 0.167 |
| qwen3-8b | +17.00 [+10.51,+23.86] | -1.92 [-8.01,+4.14] | +21.70 [+15.76,+27.84] / +12.07 [+7.09,+17.55] | +9.63 [+2.64,+16.60] | +14.75 [+10.20,+19.70] | +12.97 [+7.69,+18.52] | +10.11 [+6.36,+14.04] | 0.333 / 0.175 |
| gemma3-12b | +14.72 [+7.25,+22.47] | -1.40 [-7.22,+4.08] | +20.40 [+14.05,+27.48] / +10.87 [+6.08,+16.23] | +9.53 [+1.53,+17.87] | +13.27 [+8.59,+18.63] | +9.48 [+5.15,+14.38] | +12.91 [+8.13,+18.36] | 0.225 / 0.133 |
| llama31-8b | +11.25 [+3.75,+19.17] | -11.07 [-18.82,-2.74] | +34.58 [+25.83,+43.75] / +24.41 [+17.98,+31.07] | +10.18 [-0.48,+21.43] | +23.80 [+17.96,+30.34] | +15.72 [+9.83,+22.12] | +17.20 [+12.98,+21.37] | 0.183 / 0.192 |

## Valid E2 preservation

Leverage is the support-E2 minus refute-E2 probability on the same claim. Absolute leverage differences are item-wise before averaging.

| Model | D leverage | I leverage | N leverage, X+ | N leverage, X− | Mean absolute D−I leverage error | Mean absolute N−D leverage error | Mean absolute N−I leverage error | X×E2 interaction N | Binary leverage D / I / N |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| pooled | +62.99 [+52.48,+72.85] | +52.26 [+42.43,+61.96] | +54.27 [+43.53,+64.48] | +47.18 [+36.99,+57.44] | +24.30 [+17.41,+31.55] | +29.41 [+23.67,+35.65] | +25.68 [+20.46,+31.26] | +7.09 [-2.92,+17.04] | 0.683 / 0.589 / 0.550 |
| qwen3-8b | +61.92 [+48.57,+75.15] | +42.40 [+30.55,+55.17] | +54.48 [+42.27,+66.85] | +43.78 [+31.47,+56.42] | +25.95 [+15.38,+37.03] | +29.50 [+20.39,+39.41] | +20.13 [+12.64,+27.98] | +10.70 [-1.03,+22.92] | 0.683 / 0.500 / 0.508 |
| gemma3-12b | +73.62 [+62.22,+84.97] | +55.65 [+43.35,+67.87] | +53.57 [+41.50,+65.60] | +57.50 [+45.65,+69.58] | +18.83 [+10.12,+28.63] | +23.28 [+15.15,+32.02] | +22.50 [+14.40,+31.54] | -3.93 [-15.25,+7.15] | 0.750 / 0.667 / 0.600 |
| llama31-8b | +53.45 [+38.45,+68.33] | +58.73 [+46.27,+70.63] | +54.77 [+41.43,+68.10] | +40.25 [+25.00,+55.00] | +28.12 [+17.30,+39.42] | +35.46 [+27.00,+43.89] | +34.41 [+25.97,+42.74] | +14.52 [-3.82,+32.85] | 0.617 / 0.600 / 0.542 |

## Interpretation boundary

S is supported only if the active X separation is substantial and the excluded X separation and item-wise absolute X effect are small. R uses the shorter direct D baseline, so I−D exposes some frame/length cost. P is measured by E2 response-profile differences, not a single final-score shift. Analyze each model before pooling and do not turn a model-specific regime into a cross-model law. Historical G29/G30 outcomes motivated the pilot; none of these new joint estimates is a fresh independent confirmation.
