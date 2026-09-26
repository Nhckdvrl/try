# G28A equal-final-evidence path experiment

Exploratory, reused ConfB claims. See `results/discovery/g28a_path_v1_registration.md`.
Post hoc audit-restricted sensitivity: 142/200 claims; not a new confirmation. 200 run claims × 3 models × 11 rows = 6600 raw rows. Claim-cluster paired bootstrap, 5,000 draws, seed fixed in analyzer. Scores 0–100.

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
| mistral-small-24b | -7.65 [-10.72, -4.75] | -2.03 [-6.14, 2.22] | -13.27 [-18.36, -8.47] |
| qwen3-8b | -14.18 [-18.01, -10.36] | 0.18 [-2.49, 2.68] | -28.53 [-35.81, -21.39] |
| gemma3-12b | -11.66 [-15.09, -8.36] | -4.65 [-8.37, -1.26] | -18.67 [-25.04, -12.54] |
| pooled | -11.16 [-13.43, -8.96] | -2.17 [-4.37, -0.03] | -20.16 [-24.49, -15.82] |

## History and direct path

| Model | abs(RJ−D) | abs(IJ−D) | abs(RR−D) | T_read (RR−IJ) |
|---|---:|---:|---:|---:|
| mistral-small-24b | 10.90 [7.98, 13.98] | 10.84 [8.11, 13.78] | 10.95 [8.18, 13.76] | -5.81 [-9.04, -2.86] |
| qwen3-8b | 13.06 [10.00, 16.36] | 16.30 [12.82, 20.02] | 12.77 [9.53, 16.20] | -10.49 [-14.74, -6.43] |
| gemma3-12b | 15.50 [12.51, 18.51] | 14.41 [11.50, 17.61] | 14.65 [12.12, 17.39] | -5.31 [-8.75, -1.97] |
| pooled | 13.15 [10.99, 15.40] | 13.85 [11.87, 15.81] | 12.79 [10.79, 14.82] | -7.20 [-9.44, -5.10] |

## Final evidence use and threshold flips

Separation = mean Y(E2 support) − mean Y(E2 refute). Flip = percent of final scores crossing 50 relative to D on the same claim and E2.

| Model | D separation | RJ separation | IJ separation | RR separation | RJ flip % | IJ flip % | RR flip % |
|---|---:|---:|---:|---:|---:|---:|---:|
| mistral-small-24b | 74.71 [68.25, 80.77] | 86.11 [82.20, 89.65] | 70.82 [64.13, 77.12] | 82.44 [77.96, 86.80] | 9.9 | 10.2 | 10.2 |
| qwen3-8b | 68.21 [61.47, 74.81] | 83.27 [77.52, 88.62] | 54.91 [47.33, 62.49] | 75.89 [69.39, 81.96] | 13.7 | 15.5 | 14.4 |
| gemma3-12b | 58.97 [52.09, 65.88] | 75.12 [69.27, 80.61] | 51.79 [44.34, 59.05] | 62.42 [56.29, 68.27] | 15.5 | 14.1 | 14.8 |
| pooled | 67.30 [61.78, 72.63] | 81.50 [77.40, 85.30] | 59.17 [53.69, 64.39] | 73.58 [68.87, 78.03] | 13.0 | 13.3 | 13.1 |

Limits: D differs in dialogue length and retraction frame. RJ−IJ is the matched-frame primary contrast. RR differs from IJ in both E1 relevance and absence of an initial generated answer; it is a diagnostic, not an isolated content intervention. Initial judgments are included in raw output for later mediation analysis, but that analysis was not preregistered. All model responses are generated from textual histories; no persistent hidden state is tested.
