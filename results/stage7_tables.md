# Stage 3E — duplicate control and the proposition relation matrix


# qwen3-8b

## P0-A Duplicate control

`marginal leverage` is the shift the *later* evidence produces given that the preview is already present: `Y(preview + E) - Y(preview alone)`, sign-aligned. If a preview simply made the second presentation redundant, this would collapse under no rule too.

| preview | marginal leverage, no rule | marginal leverage, admit rule | REI under exclude |
|---|---|---|---|
| `none` (n=74) | +32.06 pts | +37.89 pts | **+0.611** [+0.458, +0.749] |
| `exact` (n=73) | +5.97 pts | +13.43 pts | **-1.203** [-1.668, -0.706] |
| `para` (n=74) | +17.88 pts | +25.71 pts | **-0.973** [-1.315, -0.605] |
| `indep` (n=75) | +18.07 pts | +25.00 pts | **-0.719** [-1.021, -0.419] |
| `unrel` (n=73) | +34.19 pts | +38.90 pts | **+0.637** [+0.489, +0.799] |

Marginal leverage is in raw rating points, measured against the preview-only baseline for that same preview, so a preview that merely made the later evidence redundant would show a reduced value in the *no rule* column.

## P0-B Proposition relation matrix

`ExclusionEffect` is the rating points the RULE removes on top of whatever the preview already did: `marg(no rule) - marg(exclude)`, both measured against that preview's own baseline. The redundancy a preview creates on its own is in the `marg(no rule)` column, so the two are separated.

| relation between preview and actual evidence | marg, no rule | **ExclusionEffect** | p |
|---|---|---|---|
| no preview (n=75) | +31.9 pts | **+8.0** [+4.1, +11.8] | 0.0005 |
| mutual entailment (true paraphrase) (n=75) | +18.1 pts | **+27.1** [+21.8, +32.2] | 0.0000 |
| preview entails actual (more specific) (n=75) | +10.7 pts | **+29.4** [+22.3, +36.5] | 0.0000 |
| actual entails preview (gist only) (n=75) | +26.3 pts | **+14.1** [+9.0, +19.5] | 0.0000 |
| one argument changed (n=75) | +21.9 pts | **+9.3** [+4.2, +14.5] | 0.0000 |
| polarity reversed (n=75) | +47.2 pts | **+15.6** [+8.3, +22.9] | 0.0000 |
| high lexical overlap, different meaning (n=75) | +30.7 pts | **+9.6** [+4.6, +14.8] | 0.0000 |
| unrelated (n=75) | +33.2 pts | **+9.0** [+5.8, +12.4] | 0.0000 |

### legacy ratio view (unstable when the preview shrinks |L|)
| relation | REI | rescue vs no preview | p |
|---|---|---|---|
| no preview | +0.610 | — | — |
| mutual entailment (true paraphrase) | +0.275 | **+0.335** [+0.188, +0.498] | 0.0000 |
| preview entails actual (more specific) | +0.296 | **+0.314** [+0.107, +0.499] | 0.0065 |
| actual entails preview (gist only) | +0.700 | **-0.090** [-0.258, +0.069] | 0.2660 |
| one argument changed | +0.621 | **-0.011** [-0.140, +0.114] | 0.8965 |
| polarity reversed | +0.510 | **+0.100** [-0.039, +0.244] | 0.1600 |
| high lexical overlap, different meaning | +0.547 | **+0.063** [-0.071, +0.199] | 0.3755 |
| unrelated | +0.648 | **-0.038** [-0.147, +0.074] | 0.4765 |

# gemma3-12b

## P0-A Duplicate control

`marginal leverage` is the shift the *later* evidence produces given that the preview is already present: `Y(preview + E) - Y(preview alone)`, sign-aligned. If a preview simply made the second presentation redundant, this would collapse under no rule too.

| preview | marginal leverage, no rule | marginal leverage, admit rule | REI under exclude |
|---|---|---|---|
| `none` (n=74) | +32.82 pts | +36.61 pts | **+0.512** [+0.319, +0.694] |
| `exact` (n=75) | +1.88 pts | +11.99 pts | **-0.912** [-1.228, -0.662] |
| `para` (n=75) | +10.29 pts | +19.10 pts | **-0.610** [-0.907, -0.306] |
| `indep` (n=74) | +7.61 pts | +16.23 pts | **-0.594** [-0.936, -0.234] |
| `unrel` (n=71) | +33.01 pts | +37.01 pts | **+0.529** [+0.327, +0.715] |

Marginal leverage is in raw rating points, measured against the preview-only baseline for that same preview, so a preview that merely made the later evidence redundant would show a reduced value in the *no rule* column.

## P0-B Proposition relation matrix

`ExclusionEffect` is the rating points the RULE removes on top of whatever the preview already did: `marg(no rule) - marg(exclude)`, both measured against that preview's own baseline. The redundancy a preview creates on its own is in the `marg(no rule)` column, so the two are separated.

| relation between preview and actual evidence | marg, no rule | **ExclusionEffect** | p |
|---|---|---|---|
| no preview (n=75) | +32.4 pts | **+9.4** [+4.7, +14.5] | 0.0000 |
| mutual entailment (true paraphrase) (n=75) | +10.5 pts | **+15.2** [+11.9, +18.7] | 0.0000 |
| preview entails actual (more specific) (n=75) | +8.7 pts | **+18.7** [+14.3, +22.9] | 0.0000 |
| actual entails preview (gist only) (n=75) | +17.0 pts | **+8.4** [+3.9, +13.3] | 0.0000 |
| one argument changed (n=75) | +21.4 pts | **+4.0** [+0.0, +8.6] | 0.0500 |
| polarity reversed (n=75) | +43.3 pts | **+1.6** [-0.9, +4.0] | 0.1885 |
| high lexical overlap, different meaning (n=75) | +30.9 pts | **+1.2** [-0.9, +3.2] | 0.2900 |
| unrelated (n=75) | +30.6 pts | **+8.5** [+4.1, +12.7] | 0.0000 |

### legacy ratio view (unstable when the preview shrinks |L|)
| relation | REI | rescue vs no preview | p |
|---|---|---|---|
| no preview | +0.519 | — | — |
| mutual entailment (true paraphrase) | +0.331 | **+0.188** [+0.006, +0.351] | 0.0425 |
| preview entails actual (more specific) | +0.340 | **+0.180** [-0.008, +0.359] | 0.0585 |
| actual entails preview (gist only) | +0.712 | **-0.192** [-0.352, -0.055] | 0.0040 |
| one argument changed | +0.617 | **-0.098** [-0.311, +0.079] | 0.3140 |
| polarity reversed | +0.649 | **-0.130** [-0.289, +0.018] | 0.0910 |
| high lexical overlap, different meaning | +0.683 | **-0.164** [-0.324, -0.016] | 0.0255 |
| unrelated | +0.512 | **+0.008** [-0.103, +0.134] | 0.9675 |
