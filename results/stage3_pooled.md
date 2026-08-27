# Pooled zero-discontinuity test

Models pooled: qwen3-8b, gemma3-12b, phi4-mini.  n = 7596 item-conditions.
Cluster bootstrap over (model x case skeleton); model fixed effects included.

| term | coef | 95% CI | p |
|---|---|---|---|
| intercept | +0.3495 | [+0.2652, +0.4313] | 0.0000 |
| w | +0.5338 | [+0.4643, +0.6062] | 0.0000 |
| Before | +0.0609 | [+0.0118, +0.1134] | 0.0107 |
| w x Before | -0.0778 | [-0.1522, -0.0002] | 0.0493 |
| **I[w=0] x Before** | +0.0955 | [+0.0344, +0.1599] | 0.0047 |
| model[gemma3-12b] | -0.0214 | [-0.1400, +0.0931] | 0.7427 |
| model[phi4-mini] | +0.0766 | [-0.0258, +0.1798] | 0.1400 |

## Headline contrast

Per item: (pre-post gap at w=0) minus (mean pre-post gap over the eight non-zero weights). Cluster bootstrap over (model x case skeleton).

**+0.295 [+0.185, +0.405] p = 0.0000**  (n = 422 items)

Mean pre-post gap per requested weight, averaged over models:

| requested w | mean gap | per-model |
|---:|---|---|
| 0 | +0.310 | qwen3-8b: +0.331, gemma3-12b: +0.343, phi4-mini: +0.256 |
| 0.01 | +0.030 | qwen3-8b: +0.009, gemma3-12b: +0.035, phi4-mini: +0.047 |
| 0.025 | +0.031 | qwen3-8b: +0.012, gemma3-12b: -0.053, phi4-mini: +0.133 |
| 0.05 | +0.084 | qwen3-8b: +0.023, gemma3-12b: -0.016, phi4-mini: +0.247 |
| 0.1 | -0.058 | qwen3-8b: -0.030, gemma3-12b: -0.080, phi4-mini: -0.064 |
| 0.25 | -0.013 | qwen3-8b: -0.025, gemma3-12b: -0.070, phi4-mini: +0.056 |
| 0.5 | +0.059 | qwen3-8b: -0.053, gemma3-12b: +0.126, phi4-mini: +0.104 |
| 0.75 | +0.012 | qwen3-8b: -0.048, gemma3-12b: +0.032, phi4-mini: +0.053 |
| 1 | -0.016 | qwen3-8b: -0.135, gemma3-12b: -0.063, phi4-mini: +0.152 |
