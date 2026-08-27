# Stage 2 — separating proximity, prospective binding and scope

REI is the effective weight the model gives the critical evidence: 0 = decided
as if it had never been seen, 1 = used as fully as when the rule permits it.

# qwen3-8b

## 1. Rule-position factorial   (n usable = 143)

| condition | rule->answer tokens (median) | REI [95% CI] |
|---|---:|---|
| `pos_adm_pre_d0` | 149 | +0.981 [+0.946, +1.019] |
| `pos_adm_pre_d1` | 300 | +0.952 [+0.874, +1.031] |
| `pos_adm_pre_d2` | 615 | +0.889 [+0.819, +0.961] |
| `pos_adm_post_d0` | 105 | +1.019 [+0.981, +1.054] |
| `pos_adm_post_d1` | 266 | +1.024 [+0.952, +1.098] |
| `pos_adm_post_d2` | 579 | +0.966 [+0.891, +1.035] |
| `pos_exc_pre_d0` | 156 | +0.463 [+0.359, +0.567] |
| `pos_exc_pre_d1` | 309 | +0.350 [+0.235, +0.463] |
| `pos_exc_pre_d2` | 626 | +0.272 [+0.144, +0.391] |
| `pos_exc_post_d0` | 110 | +0.088 [-0.006, +0.177] |
| `pos_exc_post_d1` | 274 | +0.109 [+0.001, +0.207] |
| `pos_exc_post_d2` | 587 | +0.095 [-0.010, +0.196] |

Exclusion arm only, REI ~ Distance + Before + Distance:Before (n = 858 item-conditions, cluster bootstrap):

| term | coef | 95% CI | p |
|---|---|---|---|
| intercept | +0.1071 | [+0.0082, +0.2133] | 0.0405 |
| Distance (per 100 tok) | -0.0030 | [-0.0199, +0.0129] | 0.7520 |
| Before (rule precedes E) | +0.3788 | [+0.2247, +0.5376] | 0.0000 |
| Distance x Before | -0.0311 | [-0.0616, -0.0038] | 0.0245 |

## 2. Identifier binding, no directional anaphora   (n = 139)

| condition | REI [95% CI] |
|---|---|
| `id_exclude_pre` | +0.213 [+0.107, +0.320] |
| `id_exclude_post` | -0.001 [-0.099, +0.094] |
| `id_exclude_pre_marker` | +0.323 [+0.210, +0.436] |

- pre - post with an identical rule sentence: +0.214 [+0.133, +0.299] p=0.0000
- pre - pre_with_binding_marker: -0.111 [-0.204, -0.017] p=0.0250

## 3. Requested weight vs effective weight   (n = 144)

| requested w | effective w, rule BEFORE evidence | effective w, rule AFTER |
|---:|---|---|
| 0.00 | +0.478 [+0.354, +0.595] | -0.048 [-0.184, +0.083] |
| 0.25 | +0.570 [+0.491, +0.649] | +0.469 [+0.385, +0.555] |
| 0.50 | +0.578 [+0.500, +0.655] | +0.484 [+0.423, +0.545] |
| 0.75 | +0.845 [+0.790, +0.901] | +0.817 [+0.752, +0.889] |
| 1.00 | +0.951 [+0.898, +1.000] | +1.049 [+1.000, +1.100] |

Absolute error |w_effective - w_requested|, averaged over the five levels:
- rule BEFORE evidence: 0.384 [0.357, 0.414]
- rule AFTER  evidence: 0.329 [0.300, 0.362]

# gemma3-12b

## 1. Rule-position factorial   (n usable = 141)

| condition | rule->answer tokens (median) | REI [95% CI] |
|---|---:|---|
| `pos_adm_pre_d0` | 131 | +0.992 [+0.943, +1.039] |
| `pos_adm_pre_d1` | 304 | +0.972 [+0.918, +1.031] |
| `pos_adm_pre_d2` | 634 | +0.929 [+0.856, +1.005] |
| `pos_adm_post_d0` | 106 | +1.007 [+0.961, +1.055] |
| `pos_adm_post_d1` | 274 | +0.997 [+0.927, +1.065] |
| `pos_adm_post_d2` | 600 | +0.957 [+0.868, +1.034] |
| `pos_exc_pre_d0` | 142 | +0.459 [+0.307, +0.594] |
| `pos_exc_pre_d1` | 316 | +0.443 [+0.297, +0.571] |
| `pos_exc_pre_d2` | 645 | +0.404 [+0.251, +0.540] |
| `pos_exc_post_d0` | 113 | +0.080 [-0.047, +0.196] |
| `pos_exc_post_d1` | 283 | +0.234 [+0.114, +0.338] |
| `pos_exc_post_d2` | 608 | +0.135 [+0.009, +0.250] |

Exclusion arm only, REI ~ Distance + Before + Distance:Before (n = 846 item-conditions, cluster bootstrap):

| term | coef | 95% CI | p |
|---|---|---|---|
| intercept | +0.1438 | [+0.0324, +0.2515] | 0.0155 |
| Distance (per 100 tok) | +0.0017 | [-0.0093, +0.0137] | 0.7500 |
| Before (rule precedes E) | +0.3338 | [+0.1934, +0.4687] | 0.0000 |
| Distance x Before | -0.0129 | [-0.0289, +0.0039] | 0.1315 |

## 2. Identifier binding, no directional anaphora   (n = 136)

| condition | REI [95% CI] |
|---|---|
| `id_exclude_pre` | +0.281 [+0.151, +0.402] |
| `id_exclude_post` | +0.120 [-0.007, +0.243] |
| `id_exclude_pre_marker` | +0.306 [+0.205, +0.399] |

- pre - post with an identical rule sentence: +0.160 [+0.048, +0.272] p=0.0080
- pre - pre_with_binding_marker: -0.025 [-0.148, +0.076] p=0.7060

## 3. Requested weight vs effective weight   (n = 142)

| requested w | effective w, rule BEFORE evidence | effective w, rule AFTER |
|---:|---|---|
| 0.00 | +0.582 [+0.447, +0.711] | +0.151 [-0.020, +0.313] |
| 0.25 | +0.578 [+0.436, +0.713] | +0.671 [+0.559, +0.773] |
| 0.50 | +0.646 [+0.542, +0.746] | +0.685 [+0.574, +0.794] |
| 0.75 | +0.826 [+0.735, +0.921] | +0.860 [+0.757, +0.963] |
| 1.00 | +0.974 [+0.900, +1.047] | +1.026 [+0.953, +1.100] |

Absolute error |w_effective - w_requested|, averaged over the five levels:
- rule BEFORE evidence: 0.472 [0.432, 0.515]
- rule AFTER  evidence: 0.445 [0.405, 0.491]

# mistral-small-24b

## 1. Rule-position factorial   (n usable = 141)

| condition | rule->answer tokens (median) | REI [95% CI] |
|---|---:|---|
| `pos_adm_pre_d0` | 128 | +1.010 [+0.982, +1.036] |
| `pos_adm_pre_d1` | 303 | +0.938 [+0.885, +0.993] |
| `pos_adm_pre_d2` | 622 | +0.898 [+0.812, +0.976] |
| `pos_adm_post_d0` | 104 | +0.990 [+0.964, +1.018] |
| `pos_adm_post_d1` | 273 | +0.982 [+0.892, +1.061] |
| `pos_adm_post_d2` | 586 | +0.938 [+0.844, +1.022] |
| `pos_exc_pre_d0` | 141 | +0.241 [+0.109, +0.364] |
| `pos_exc_pre_d1` | 316 | +0.191 [+0.086, +0.291] |
| `pos_exc_pre_d2` | 631 | +0.163 [+0.063, +0.260] |
| `pos_exc_post_d0` | 113 | +0.012 [-0.105, +0.121] |
| `pos_exc_post_d1` | 280 | +0.041 [-0.049, +0.124] |
| `pos_exc_post_d2` | 592 | +0.000 [-0.116, +0.108] |

Exclusion arm only, REI ~ Distance + Before + Distance:Before (n = 846 item-conditions, cluster bootstrap):

| term | coef | 95% CI | p |
|---|---|---|---|
| intercept | +0.0304 | [-0.0657, +0.1207] | 0.5095 |
| Distance (per 100 tok) | -0.0038 | [-0.0232, +0.0139] | 0.6845 |
| Before (rule precedes E) | +0.2215 | [+0.1218, +0.3282] | 0.0000 |
| Distance x Before | -0.0107 | [-0.0289, +0.0059] | 0.2110 |

## 2. Identifier binding, no directional anaphora   (n = 139)

| condition | REI [95% CI] |
|---|---|
| `id_exclude_pre` | +0.006 [-0.103, +0.109] |
| `id_exclude_post` | -0.008 [-0.116, +0.089] |
| `id_exclude_pre_marker` | -0.043 [-0.131, +0.037] |

- pre - post with an identical rule sentence: +0.014 [-0.076, +0.100] p=0.7590
- pre - pre_with_binding_marker: +0.050 [-0.029, +0.116] p=0.1815

## 3. Requested weight vs effective weight   (n = 142)

| requested w | effective w, rule BEFORE evidence | effective w, rule AFTER |
|---:|---|---|
| 0.00 | +0.058 [-0.073, +0.180] | -0.041 [-0.164, +0.070] |
| 0.25 | +0.478 [+0.369, +0.571] | +0.401 [+0.291, +0.497] |
| 0.50 | +0.512 [+0.426, +0.589] | +0.490 [+0.400, +0.571] |
| 0.75 | +0.720 [+0.621, +0.809] | +0.673 [+0.602, +0.735] |
| 1.00 | +1.014 [+0.976, +1.058] | +0.977 [+0.918, +1.024] |

Absolute error |w_effective - w_requested|, averaged over the five levels:
- rule BEFORE evidence: 0.347 [0.315, 0.382]
- rule AFTER  evidence: 0.307 [0.275, 0.341]

# qwen3.5-27b

## 1. Rule-position factorial   (n usable = 141)

| condition | rule->answer tokens (median) | REI [95% CI] |
|---|---:|---|
| `pos_adm_pre_d0` | 153 | +0.992 [+0.915, +1.053] |
| `pos_adm_pre_d1` | 311 | +1.062 [+1.008, +1.127] |
| `pos_adm_pre_d2` | 638 | +1.035 [+0.977, +1.102] |
| `pos_adm_post_d0` | 109 | +0.980 [+0.903, +1.044] |
| `pos_adm_post_d1` | 276 | +0.925 [+0.823, +1.009] |
| `pos_adm_post_d2` | 601 | +0.983 [+0.898, +1.058] |
| `pos_exc_pre_d0` | 160 | -0.013 [-0.175, +0.148] |
| `pos_exc_pre_d1` | 320 | -0.095 [-0.277, +0.080] |
| `pos_exc_pre_d2` | 648 | -0.099 [-0.273, +0.066] |
| `pos_exc_post_d0` | 114 | -0.293 [-0.444, -0.149] |
| `pos_exc_post_d1` | 284 | -0.227 [-0.375, -0.088] |
| `pos_exc_post_d2` | 608 | -0.238 [-0.391, -0.096] |

Exclusion arm only, REI ~ Distance + Before + Distance:Before (n = 846 item-conditions, cluster bootstrap):

| term | coef | 95% CI | p |
|---|---|---|---|
| intercept | -0.2777 | [-0.4097, -0.1548] | 0.0000 |
| Distance (per 100 tok) | +0.0074 | [-0.0066, +0.0215] | 0.3030 |
| Before (rule precedes E) | +0.3028 | [+0.1541, +0.4580] | 0.0000 |
| Distance x Before | -0.0323 | [-0.0574, -0.0041] | 0.0240 |

## 2. Identifier binding, no directional anaphora   (n = 136)

| condition | REI [95% CI] |
|---|---|
| `id_exclude_pre` | -0.059 [-0.199, +0.073] |
| `id_exclude_post` | -0.205 [-0.329, -0.086] |
| `id_exclude_pre_marker` | -0.023 [-0.139, +0.090] |

- pre - post with an identical rule sentence: +0.146 [+0.023, +0.283] p=0.0260
- pre - pre_with_binding_marker: -0.036 [-0.125, +0.053] p=0.4405

## 3. Requested weight vs effective weight   (n = 140)

| requested w | effective w, rule BEFORE evidence | effective w, rule AFTER |
|---:|---|---|
| 0.00 | -0.069 [-0.229, +0.083] | -0.205 [-0.350, -0.069] |
| 0.25 | +0.333 [+0.195, +0.461] | +0.217 [+0.051, +0.367] |
| 0.50 | +0.537 [+0.422, +0.650] | +0.503 [+0.388, +0.612] |
| 0.75 | +0.682 [+0.578, +0.777] | +0.725 [+0.630, +0.814] |
| 1.00 | +0.954 [+0.899, +0.996] | +1.042 [+1.003, +1.088] |

Absolute error |w_effective - w_requested|, averaged over the five levels:
- rule BEFORE evidence: 0.406 [0.366, 0.452]
- rule AFTER  evidence: 0.392 [0.348, 0.437]
