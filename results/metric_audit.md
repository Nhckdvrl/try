# Metric audit

Every ratio still reported, checked for denominator fragility. `|L|` is the
denominator: the leverage the critical evidence has under an admitting rule.

## Main REI (Stage 0-2): denominator was frozen by screening

| model | n | median \|L\| | 10th pct | frac \|L\|<10 | REI_pre all / \|L\|>10 / \|L\|>15 | Δ_time all / >10 / >15 |
|---|---:|---:|---:|---:|---|---|
| qwen3-8b | 144 | 31.0 | 9.7 | 0.10 | +0.45 / +0.48 / +0.52 | -0.32 / -0.33 / -0.39 |
| gemma3-12b | 141 | 33.2 | 8.0 | 0.13 | +0.43 / +0.53 / +0.59 | -0.35 / -0.40 / -0.37 |
| phi4-mini | 138 | 28.3 | 5.6 | 0.22 | +0.50 / +0.60 / +0.65 | -0.30 / -0.26 / -0.28 |
| mistral-small-24b | 141 | 30.3 | 6.2 | 0.15 | +0.19 / +0.27 / +0.32 | -0.21 / -0.22 / -0.23 |
| qwen3-32b | 143 | 29.5 | 8.1 | 0.13 | +0.21 / +0.25 / +0.29 | -0.29 / -0.31 / -0.33 |
| qwen3.5-27b | 142 | 36.8 | 6.1 | 0.18 | -0.05 / -0.03 / +0.01 | -0.22 / -0.18 / -0.12 |
| qwen2.5-32b | 140 | 33.2 | 7.0 | 0.15 | +0.30 / +0.26 / +0.30 | -0.26 / -0.21 / -0.24 |

A ratio is safe here because screening required `sign(direction)*(admit-base) >= 8` before any Exclude condition existed, so the denominator cannot be near zero by construction, and the conclusions do not move when the floor is raised to 10 or 15.
