# G28A equal-final-evidence path experiment

Exploratory, reused ConfB claims. See `results/discovery/g28a_path_v1_registration.md`.
Post hoc audit-restricted sensitivity: 199/200 claims; not a new confirmation. 200 run claims × 3 models × 11 rows = 6600 raw rows. Claim-cluster paired bootstrap, 5,000 draws, seed fixed in analyzer. Scores 0–100.

## Integrity

| Model | Rows | Unparsed | Digit mass <0.5 | Rationale cap |
|---|---:|---:|---:|---:|
| mistral-small-24b | 2200 | 0 | 0 | 0 |
| qwen3-8b | 2200 | 0 | 0 | 0 |
| gemma3-12b | 2200 | 0 | 0 | 0 |

## Registered primary contrast

T = sign(revoked relevant E1) × (RJ − IJ). Positive means polarity-aligned carryover; negative means overcorrection. The RJ and IJ final turns use identical retraction wording and E2.

| Model | Both E2 directions | E2 support | E2 refute |
|---|---:|---:|---:|
| mistral-small-24b | -7.74 [-10.52, -4.99] | -3.51 [-7.01, 0.07] | -11.97 [-16.41, -7.58] |
| qwen3-8b | -12.22 [-15.44, -9.02] | 2.07 [-0.50, 4.72] | -26.51 [-32.48, -20.73] |
| gemma3-12b | -12.50 [-15.43, -9.67] | -4.37 [-7.75, -0.95] | -20.64 [-26.02, -15.44] |
| pooled | -10.82 [-12.66, -8.97] | -1.94 [-3.82, -0.08] | -19.71 [-23.23, -16.28] |

## History and direct path

| Model | abs(RJ−D) | abs(IJ−D) | abs(RR−D) | T_read (RR−IJ) |
|---|---:|---:|---:|---:|
| mistral-small-24b | 11.92 [9.53, 14.46] | 11.44 [9.25, 13.84] | 12.42 [10.04, 15.05] | -5.66 [-8.50, -2.92] |
| qwen3-8b | 12.86 [10.24, 15.48] | 17.64 [14.57, 21.03] | 12.72 [10.17, 15.32] | -9.11 [-12.40, -5.84] |
| gemma3-12b | 15.68 [13.23, 18.25] | 15.70 [12.92, 18.68] | 14.81 [12.57, 17.19] | -6.74 [-9.50, -3.94] |
| pooled | 13.48 [11.62, 15.40] | 14.93 [13.11, 16.81] | 13.32 [11.62, 15.09] | -7.17 [-8.95, -5.33] |

## Final evidence use and threshold flips

Separation = mean Y(E2 support) − mean Y(E2 refute). Flip = percent of final scores crossing 50 relative to D on the same claim and E2.

| Model | D separation | RJ separation | IJ separation | RR separation | RJ flip % | IJ flip % | RR flip % |
|---|---:|---:|---:|---:|---:|---:|---:|
| mistral-small-24b | 71.09 [65.49, 76.36] | 83.38 [79.23, 87.10] | 67.90 [62.17, 73.46] | 79.22 [74.58, 83.46] | 11.6 | 11.1 | 11.8 |
| qwen3-8b | 64.45 [58.26, 70.41] | 77.43 [71.42, 83.03] | 52.99 [46.41, 59.61] | 71.21 [65.33, 76.85] | 12.8 | 17.6 | 13.8 |
| gemma3-12b | 54.30 [47.69, 60.28] | 71.21 [65.90, 76.33] | 46.20 [39.84, 52.64] | 59.68 [54.43, 64.99] | 15.8 | 16.3 | 14.6 |
| pooled | 63.28 [58.19, 68.12] | 77.34 [73.13, 81.26] | 55.70 [50.98, 60.42] | 70.04 [65.68, 74.27] | 13.4 | 15.0 | 13.4 |

Limits: D differs in dialogue length and retraction frame. RJ−IJ is the matched-frame primary contrast. RR differs from IJ in both E1 relevance and absence of an initial generated answer; it is a diagnostic, not an isolated content intervention. Initial judgments are included in raw output for later mediation analysis, but that analysis was not preregistered. All model responses are generated from textual histories; no persistent hidden state is tested.
