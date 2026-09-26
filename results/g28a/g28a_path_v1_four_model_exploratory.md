# G28A equal-final-evidence path experiment

Exploratory, reused ConfB claims. See `results/discovery/g28a_path_v1_registration.md`.
Full frozen sample. 200 run claims × 4 models × 11 rows = 8800 raw rows. Claim-cluster paired bootstrap, 5,000 draws, seed fixed in analyzer. Scores 0–100.

## Integrity

| Model | Rows | Unparsed | Digit mass <0.5 | Rationale cap |
|---|---:|---:|---:|---:|
| mistral-small-24b | 2200 | 0 | 0 | 0 |
| qwen3-8b | 2200 | 0 | 0 | 0 |
| gemma3-12b | 2200 | 0 | 0 | 0 |
| llama31-8b | 2200 | 0 | 0 | 0 |

## Registered primary contrast

T = sign(revoked relevant E1) × (RJ − IJ). Positive means polarity-aligned carryover; negative means overcorrection. The RJ and IJ final turns use identical retraction wording and E2.

| Model | Both E2 directions | E2 support | E2 refute |
|---|---:|---:|---:|
| mistral-small-24b | -7.70 [-10.49, -5.03] | -3.49 [-7.11, -0.09] | -11.92 [-16.28, -7.62] |
| qwen3-8b | -12.41 [-15.69, -9.22] | 2.06 [-0.44, 4.72] | -26.88 [-32.99, -20.99] |
| gemma3-12b | -12.65 [-15.57, -9.73] | -4.35 [-7.77, -1.11] | -20.96 [-26.35, -15.83] |
| llama31-8b | -5.71 [-9.12, -2.39] | -3.43 [-7.71, 0.75] | -8.00 [-14.31, -1.71] |
| pooled | -9.62 [-11.28, -8.02] | -2.30 [-4.29, -0.46] | -16.94 [-20.06, -14.01] |

## History and direct path

| Model | abs(RJ−D) | abs(IJ−D) | abs(RR−D) | T_read (RR−IJ) |
|---|---:|---:|---:|---:|
| mistral-small-24b | 11.86 [9.47, 14.39] | 11.39 [9.21, 13.70] | 12.37 [9.99, 14.91] | -5.63 [-8.39, -2.96] |
| qwen3-8b | 13.00 [10.36, 15.64] | 17.59 [14.47, 20.96] | 12.87 [10.31, 15.54] | -9.31 [-12.59, -6.03] |
| gemma3-12b | 15.83 [13.44, 18.40] | 15.64 [12.82, 18.61] | 14.91 [12.66, 17.30] | -6.87 [-9.66, -4.02] |
| llama31-8b | 21.12 [17.91, 24.39] | 19.86 [16.91, 23.01] | 21.17 [18.23, 24.24] | -1.16 [-4.38, 2.02] |
| pooled | 15.45 [13.70, 17.24] | 16.12 [14.43, 17.84] | 15.33 [13.84, 16.88] | -5.74 [-7.40, -4.15] |

## Final evidence use and threshold flips

Separation = mean Y(E2 support) − mean Y(E2 refute). Flip = percent of final scores crossing 50 relative to D on the same claim and E2.

| Model | D separation | RJ separation | IJ separation | RR separation | RJ flip % | IJ flip % | RR flip % |
|---|---:|---:|---:|---:|---:|---:|---:|
| mistral-small-24b | 71.23 [65.71, 76.41] | 83.46 [79.28, 87.13] | 68.05 [62.34, 73.57] | 79.30 [74.73, 83.43] | 11.5 | 11.0 | 11.8 |
| qwen3-8b | 64.22 [57.90, 70.25] | 77.55 [71.54, 83.00] | 52.72 [46.05, 59.55] | 71.35 [65.51, 76.87] | 13.0 | 17.5 | 14.0 |
| gemma3-12b | 54.05 [47.78, 60.10] | 71.34 [66.14, 76.40] | 46.03 [39.43, 52.17] | 59.77 [54.68, 64.71] | 16.0 | 16.2 | 14.8 |
| llama31-8b | 45.46 [39.40, 51.25] | 47.74 [41.45, 53.93] | 36.32 [30.28, 42.44] | 38.64 [32.47, 44.72] | 23.5 | 21.0 | 22.0 |
| pooled | 58.74 [53.97, 63.31] | 70.02 [66.00, 73.83] | 50.78 [46.39, 55.14] | 62.26 [58.07, 66.22] | 16.0 | 16.4 | 15.6 |

Limits: D differs in dialogue length and retraction frame. RJ−IJ is the matched-frame primary contrast. RR differs from IJ in both E1 relevance and absence of an initial generated answer; it is a diagnostic, not an isolated content intervention. Initial judgments are included in raw output for later mediation analysis, but that analysis was not preregistered. All model responses are generated from textual histories; no persistent hidden state is tested.
