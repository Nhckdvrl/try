# Prospective nullification gap (PNG)

`N = REI(w=0.01) - REI(w=0)` is the extra suppression bought by the smallest
possible lexical change, one digit. `PNG = N_post - N_pre`.

| model | n | N_pre | N_post | **PNG** [95% CI] | p |
|---|---:|---|---|---|---|
| qwen3-8b | 143 | -0.081 | +0.241 | **+0.322** [+0.124, +0.516] | 0.0014 |
| gemma3-12b | 141 | -0.003 | +0.306 | **+0.309** [+0.109, +0.495] | 0.0028 |
| phi4-mini | 138 | -0.117 | +0.093 | **+0.210** [-0.022, +0.449] | 0.0810 |
| mistral-small-24b | 142 | +0.020 | +0.064 | **+0.044** [-0.103, +0.185] | 0.5510 |
| qwen3.5-27b | 139 | -0.239 | -0.012 | **+0.227** [+0.065, +0.421] | 0.0036 |

Across 5 models PNG is positive in 5/5, range +0.044 to +0.322, individually significant in 3.

Read N_pre directly: it is the suppression gained by writing 'exactly 0%' instead of '1%' when the target does not exist yet.
