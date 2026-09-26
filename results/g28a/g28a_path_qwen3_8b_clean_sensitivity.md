# G28A equal-final-evidence path experiment

Exploratory, reused ConfB claims. See `results/discovery/g28a_path_v1_registration.md`.
Post hoc audit-restricted sensitivity: 142/200 claims; not a new confirmation. 200 run claims × 1 models × 11 rows = 2200 raw rows. Claim-cluster paired bootstrap, 5,000 draws, seed fixed in analyzer. Scores 0–100.

## Integrity

| Model | Rows | Unparsed | Digit mass <0.5 | Rationale cap |
|---|---:|---:|---:|---:|
| qwen3-8b | 2200 | 0 | 0 | 0 |

## Registered primary contrast

T = sign(revoked relevant E1) × (RJ − IJ). Positive means polarity-aligned carryover; negative means overcorrection. The RJ and IJ final turns use identical retraction wording and E2.

| Model | Both E2 directions | E2 support | E2 refute |
|---|---:|---:|---:|
| qwen3-8b | -14.18 [-18.01, -10.36] | 0.18 [-2.49, 2.68] | -28.53 [-35.81, -21.39] |
| pooled | -14.18 [-18.01, -10.36] | 0.18 [-2.49, 2.68] | -28.53 [-35.81, -21.39] |

## History and direct path

| Model | abs(RJ−D) | abs(IJ−D) | abs(RR−D) | T_read (RR−IJ) |
|---|---:|---:|---:|---:|
| qwen3-8b | 13.06 [10.00, 16.36] | 16.30 [12.82, 20.02] | 12.77 [9.53, 16.20] | -10.49 [-14.74, -6.43] |
| pooled | 13.06 [10.00, 16.36] | 16.30 [12.82, 20.02] | 12.77 [9.53, 16.20] | -10.49 [-14.74, -6.43] |

## Final evidence use and threshold flips

Separation = mean Y(E2 support) − mean Y(E2 refute). Flip = percent of final scores crossing 50 relative to D on the same claim and E2.

| Model | D separation | RJ separation | IJ separation | RR separation | RJ flip % | IJ flip % | RR flip % |
|---|---:|---:|---:|---:|---:|---:|---:|
| qwen3-8b | 68.21 [61.47, 74.81] | 83.27 [77.52, 88.62] | 54.91 [47.33, 62.49] | 75.89 [69.39, 81.96] | 13.7 | 15.5 | 14.4 |
| pooled | 68.21 [61.47, 74.81] | 83.27 [77.52, 88.62] | 54.91 [47.33, 62.49] | 75.89 [69.39, 81.96] | 13.7 | 15.5 | 14.4 |

Limits: D differs in dialogue length and retraction frame. RJ−IJ is the matched-frame primary contrast. RR differs from IJ in both E1 relevance and absence of an initial generated answer; it is a diagnostic, not an isolated content intervention. Initial judgments are included in raw output for later mediation analysis, but that analysis was not preregistered. All model responses are generated from textual histories; no persistent hidden state is tested.
