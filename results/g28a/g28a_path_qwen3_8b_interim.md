# G28A equal-final-evidence path experiment

Exploratory, reused ConfB claims. See `results/discovery/g28a_path_v1_registration.md`.
200 claims × 1 models × 11 rows = 2200 rows. Claim-cluster paired bootstrap, 5,000 draws, seed fixed in analyzer. Scores 0–100.

## Integrity

| Model | Rows | Unparsed | Digit mass <0.5 | Rationale cap |
|---|---:|---:|---:|---:|
| qwen3-8b | 2200 | 0 | 0 | 0 |

## Registered primary contrast

T = sign(revoked relevant E1) × (RJ − IJ). Positive means polarity-aligned carryover; negative means overcorrection. The RJ and IJ final turns use identical retraction wording and E2.

| Model | Both E2 directions | E2 support | E2 refute |
|---|---:|---:|---:|
| qwen3-8b | -12.41 [-15.69, -9.22] | 2.06 [-0.44, 4.72] | -26.88 [-32.99, -20.99] |
| pooled | -12.41 [-15.69, -9.22] | 2.06 [-0.44, 4.72] | -26.88 [-32.99, -20.99] |

## History and direct path

| Model | abs(RJ−D) | abs(IJ−D) | abs(RR−D) | T_read (RR−IJ) |
|---|---:|---:|---:|---:|
| qwen3-8b | 13.00 [10.36, 15.64] | 17.59 [14.47, 20.96] | 12.87 [10.31, 15.54] | -9.31 [-12.59, -6.03] |
| pooled | 13.00 [10.36, 15.64] | 17.59 [14.47, 20.96] | 12.87 [10.31, 15.54] | -9.31 [-12.59, -6.03] |

## Final evidence use and threshold flips

Separation = mean Y(E2 support) − mean Y(E2 refute). Flip = percent of final scores crossing 50 relative to D on the same claim and E2.

| Model | D separation | RJ separation | IJ separation | RR separation | RJ flip % | IJ flip % | RR flip % |
|---|---:|---:|---:|---:|---:|---:|---:|
| qwen3-8b | 64.22 [57.90, 70.25] | 77.55 [71.54, 83.00] | 52.72 [46.05, 59.55] | 71.35 [65.51, 76.87] | 13.0 | 17.5 | 14.0 |
| pooled | 64.22 [57.90, 70.25] | 77.55 [71.54, 83.00] | 52.72 [46.05, 59.55] | 71.35 [65.51, 76.87] | 13.0 | 17.5 | 14.0 |

Limits: D differs in dialogue length and retraction frame. RJ−IJ is the matched-frame primary contrast. RR differs from IJ in both E1 relevance and absence of an initial generated answer; it is a diagnostic, not an isolated content intervention. Initial judgments are included in raw output for later mediation analysis, but that analysis was not preregistered. All model responses are generated from textual histories; no persistent hidden state is tested.
