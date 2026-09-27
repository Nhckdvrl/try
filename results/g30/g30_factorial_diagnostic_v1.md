# G30 factorial diagnostic: the pooled R−N mean is misleading

Post hoc read of all 480 frozen raw outputs. This report adds no model inference, sample exclusion, or revised registration. Source hashes are checked against the [G30 manifest](g30_manifest_v1.json).

## Prior and reliability responses

Exact copy uses a tolerance of 0.01 percentage points. Each model has 40 cells; each prior × E2 group has four reliability levels.

| Model | R exactly prior | R prior or complement | R constant across reliability | N constant across reliability | Mean R range across reliability |
|---|---:|---:|---:|---:|---:|
| qwen3-8b | 4/40 | 7/40 | 0/10 | 0/10 | 22.85 pp |
| gemma3-12b | 32/40 | 40/40 | 10/10 | 1/10 | 0.00 pp |
| mistral-small-24b | 0/40 | 0/40 | 0/10 | 0/10 | 24.85 pp |

## Valid E2 uptake by reliability

Each E2 separation is mean P(Blue | Blue report) minus P(Blue | Yellow report), matched on prior and reliability. The Bayesian column is the normative separation.

| Model | Reliability | Bayes E2 sep | D | N | I | R | Signed R−N | Signed N−I |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| qwen3-8b | 0.65 | 24.95 | 27.00 | 28.80 | 24.80 | 35.80 | -3.50 | -2.00 |
| qwen3-8b | 0.75 | 42.68 | 36.00 | 48.20 | 35.20 | 40.40 | +3.90 | -6.50 |
| qwen3-8b | 0.85 | 62.41 | 51.00 | 59.00 | 44.60 | 53.40 | +2.80 | -7.20 |
| qwen3-8b | 0.95 | 85.86 | 67.40 | 62.60 | 73.60 | 74.70 | -6.05 | +5.50 |
| gemma3-12b | 0.65 | 24.95 | 48.70 | 43.33 | 48.00 | 18.00 | +12.67 | +2.33 |
| gemma3-12b | 0.75 | 42.68 | 45.20 | 47.61 | 53.80 | 18.00 | +14.80 | +3.10 |
| gemma3-12b | 0.85 | 62.41 | 48.80 | 49.54 | 59.67 | 18.00 | +15.77 | +5.06 |
| gemma3-12b | 0.95 | 85.86 | 69.60 | 58.40 | 70.46 | 18.00 | +20.20 | +6.03 |
| mistral-small-24b | 0.65 | 24.95 | 31.04 | 29.37 | 26.56 | 25.20 | +2.08 | -1.41 |
| mistral-small-24b | 0.75 | 42.68 | 48.14 | 46.84 | 44.34 | 34.71 | +6.07 | -1.25 |
| mistral-small-24b | 0.85 | 62.41 | 65.86 | 60.15 | 57.31 | 50.49 | +4.83 | -1.42 |
| mistral-small-24b | 0.95 | 85.86 | 84.56 | 80.34 | 79.69 | 74.41 | +2.96 | -0.32 |

## Interpretation

Gemma's R forecast is exactly the prior in 32/40 cells and either the prior or its complement in 40/40. Its R forecast is constant across all four reliability levels for every one of the ten prior × E2 groups. The R condition therefore places Gemma in a discrete prior-based response mode on this prompt. Its large signed R−N should not be read as a clean graded effect of revoked E1 content. Qwen and Mistral show different, smaller patterns. The pooled +6.38 pp hides these regimes.

The four reliability cells within each prior × E2 group share nearly identical wording, so this is a controlled within-prompt diagnostic. It does not establish an internal mechanism; the rendered R history is longer than N and could alter prompt processing. The stable ConfB suppression–restoration result is unaffected.
