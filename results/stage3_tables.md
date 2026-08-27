# Stage 3A — naming the phenomenon

REI is the effective causal weight the model gives the critical evidence.
0 = decided as if it had never been seen; 1 = full normal evidential weight.

# qwen3-8b

## A. Near-zero sweep — is zero a discontinuity?   (n = 143)

One identical sentence; only the percentage changes.

| requested w | rule BEFORE evidence | rule AFTER evidence | pre - post |
|---:|---|---|---|
| 0 | +0.511 [+0.418, +0.608] | +0.181 [+0.087, +0.272] | **+0.331** [+0.231, +0.437] p=0.0000 |
| 0.01 | +0.430 [+0.325, +0.531] | +0.422 [+0.328, +0.521] | **+0.009** [-0.077, +0.092] p=0.8355 |
| 0.025 | +0.452 [+0.362, +0.545] | +0.439 [+0.345, +0.530] | **+0.012** [-0.057, +0.084] p=0.7455 |
| 0.05 | +0.468 [+0.387, +0.550] | +0.445 [+0.354, +0.540] | **+0.023** [-0.065, +0.111] p=0.6180 |
| 0.1 | +0.466 [+0.381, +0.552] | +0.496 [+0.408, +0.584] | **-0.030** [-0.111, +0.052] p=0.4615 |
| 0.25 | +0.464 [+0.384, +0.542] | +0.489 [+0.408, +0.571] | **-0.025** [-0.086, +0.041] p=0.4570 |
| 0.5 | +0.475 [+0.399, +0.550] | +0.528 [+0.463, +0.593] | **-0.053** [-0.128, +0.021] p=0.1570 |
| 0.75 | +0.646 [+0.585, +0.712] | +0.694 [+0.627, +0.765] | **-0.048** [-0.102, +0.016] p=0.1405 |
| 1 | +0.926 [+0.878, +0.978] | +1.060 [+0.981, +1.121] | **-0.135** [-0.239, -0.006] p=0.0375 |

`REI ~ w + Before + w:Before + I[w=0]:Before`, cluster bootstrap:

| term | coef | 95% CI | p |
|---|---|---|---|
| intercept | +0.3538 | [+0.2519, +0.4544] | 0.0000 |
| w | +0.5847 | [+0.4804, +0.6786] | 0.0000 |
| Before | +0.0521 | [-0.0215, +0.1254] | 0.1587 |
| w x Before | -0.1826 | [-0.2980, -0.0720] | 0.0067 |
| **I[w=0] x Before** | +0.1054 | [+0.0175, +0.1876] | 0.0160 |

gap(0) = +0.331 vs gap(1%) = +0.009  ->  ratio 38.3x

## B. Rule-to-evidence delay   (n = 143)

Stage 2 moved the rule away from the ANSWER; this moves it away from the EVIDENCE it governs. Rule is always `weight = 0%`.

| filler between rule and evidence | rule BEFORE | rule AFTER | pre - post |
|---|---|---|---|
| 0 units (~0 tok) | +0.517 | +0.175 | +0.342 [+0.236, +0.454] |
| 4 units (~100 tok) | +0.471 | +0.139 | +0.331 [+0.221, +0.447] |
| 12 units (~300 tok) | +0.487 | +0.212 | +0.275 [+0.168, +0.390] |
| 40 units (~1000 tok) | +0.583 | +0.280 | +0.303 [+0.192, +0.420] |

## C. Object-existence ladder   (n = 137)

Identical rule (`Evidence E7 has decision weight 0.`) at every level; what changes is how much of E7 exists when the rule is stated. L5 is the retrospective anchor (full content already present).

- `L0 E7 never mentioned`: REI +0.561 [+0.462, +0.660]
- `L1 'you will later receive E7'`: REI +0.754 [+0.653, +0.858]
- `L2 [E7: content pending]`: REI +0.848 [+0.756, +0.941]
- `L3 + item type`: REI +0.804 [+0.690, +0.909]
- `L4 + type and direction`: REI +0.754 [+0.660, +0.849]
- `L5 full content BEFORE the rule`: REI +0.329 [+0.205, +0.453]

## D. Non-multiplicative transforms

| transform | rule BEFORE | rule AFTER | pre - post |
|---|---|---|---|
| `trflip` (target -1.0) | +0.636 | +0.496 | +0.140 [+0.039, +0.248] p=0.0085 |
| `trcap` | +0.361 | +0.222 | +0.139 [+0.076, +0.203] p=0.0000 |

## E. Declarative policy state vs causal use

Separate call, same context, asked what weight E should get. The decision run never sees this question.

| arm | says weight (mean %) | says exactly 0 (%) | REI in the decision run |
|---|---:|---:|---|
| rule PRE | 0.00 | 100.0 | +0.511 [+0.417, +0.605] |
| rule POST | 0.00 | 100.0 | +0.181 [+0.080, +0.276] |

## F. Item-specific rule vs class-wide policy   (n = 137)

- specific `E7 has weight 0`, rule first: REI +0.561 [+0.459, +0.656]
- specific, rule last: REI +0.329 [+0.202, +0.452]
- class policy `any unauthorised item has weight 0`, rule first: REI +0.100 [-0.037, +0.227]
- class policy, rule last: REI +0.145 [+0.009, +0.276]

## G. Task preview   (n = 143)

- no preview, rule first: REI +0.511 [+0.419, +0.609]
- TASK PREVIEW, rule first: REI +0.642 [+0.536, +0.742]
- no preview, rule last: REI +0.181 [+0.084, +0.276]
- TASK PREVIEW, rule last: REI +0.197 [+0.073, +0.313]
- rescue from task preview (pre): -0.131 [-0.220, -0.039] p=0.0065

# gemma3-12b

## A. Near-zero sweep — is zero a discontinuity?   (n = 141)

One identical sentence; only the percentage changes.

| requested w | rule BEFORE evidence | rule AFTER evidence | pre - post |
|---:|---|---|---|
| 0 | +0.419 [+0.291, +0.539] | +0.076 [-0.112, +0.259] | **+0.343** [+0.187, +0.511] p=0.0000 |
| 0.01 | +0.416 [+0.291, +0.539] | +0.382 [+0.252, +0.510] | **+0.035** [-0.057, +0.141] p=0.5465 |
| 0.025 | +0.392 [+0.273, +0.508] | +0.444 [+0.312, +0.569] | **-0.053** [-0.132, +0.026] p=0.1915 |
| 0.05 | +0.392 [+0.276, +0.500] | +0.409 [+0.267, +0.543] | **-0.016** [-0.138, +0.117] p=0.7460 |
| 0.1 | +0.398 [+0.264, +0.527] | +0.477 [+0.364, +0.582] | **-0.080** [-0.178, +0.007] p=0.0785 |
| 0.25 | +0.429 [+0.306, +0.543] | +0.499 [+0.384, +0.607] | **-0.070** [-0.190, +0.032] p=0.2110 |
| 0.5 | +0.599 [+0.497, +0.699] | +0.472 [+0.338, +0.595] | **+0.126** [+0.017, +0.250] p=0.0205 |
| 0.75 | +0.725 [+0.643, +0.819] | +0.693 [+0.602, +0.778] | **+0.032** [-0.084, +0.165] p=0.6435 |
| 1 | +0.960 [+0.864, +1.052] | +1.023 [+0.943, +1.106] | **-0.063** [-0.246, +0.108] p=0.4900 |

`REI ~ w + Before + w:Before + I[w=0]:Before`, cluster bootstrap:

| term | coef | 95% CI | p |
|---|---|---|---|
| intercept | +0.3184 | [+0.1780, +0.4439] | 0.0000 |
| w | +0.5996 | [+0.4734, +0.7441] | 0.0000 |
| Before | +0.0378 | [-0.0427, +0.1291] | 0.3827 |
| w x Before | -0.0555 | [-0.1985, +0.1041] | 0.4973 |
| **I[w=0] x Before** | +0.0630 | [-0.0186, +0.1414] | 0.1207 |

gap(0) = +0.343 vs gap(1%) = +0.035  ->  ratio 9.9x

## B. Rule-to-evidence delay   (n = 141)

Stage 2 moved the rule away from the ANSWER; this moves it away from the EVIDENCE it governs. Rule is always `weight = 0%`.

| filler between rule and evidence | rule BEFORE | rule AFTER | pre - post |
|---|---|---|---|
| 0 units (~0 tok) | +0.436 | +0.085 | +0.351 [+0.200, +0.514] |
| 4 units (~100 tok) | +0.325 | +0.309 | +0.016 [-0.174, +0.198] |
| 12 units (~300 tok) | +0.364 | +0.396 | -0.032 [-0.180, +0.106] |
| 40 units (~1000 tok) | +0.327 | +0.389 | -0.062 [-0.207, +0.081] |

## C. Object-existence ladder   (n = 136)

Identical rule (`Evidence E7 has decision weight 0.`) at every level; what changes is how much of E7 exists when the rule is stated. L5 is the retrospective anchor (full content already present).

- `L0 E7 never mentioned`: REI +0.836 [+0.748, +0.924]
- `L1 'you will later receive E7'`: REI +0.921 [+0.853, +0.988]
- `L2 [E7: content pending]`: REI +0.923 [+0.853, +0.994]
- `L3 + item type`: REI +0.918 [+0.820, +1.012]
- `L4 + type and direction`: REI +0.912 [+0.808, +1.024]
- `L5 full content BEFORE the rule`: REI +0.596 [+0.471, +0.715]

## D. Non-multiplicative transforms

| transform | rule BEFORE | rule AFTER | pre - post |
|---|---|---|---|
| `trflip` (target -1.0) | +0.784 | +0.859 | -0.076 [-0.240, +0.108] p=0.4060 |
| `trcap` | +0.596 | +0.408 | +0.188 [+0.089, +0.290] p=0.0005 |

## E. Declarative policy state vs causal use

Separate call, same context, asked what weight E should get. The decision run never sees this question.

| arm | says weight (mean %) | says exactly 0 (%) | REI in the decision run |
|---|---:|---:|---|
| rule PRE | 0.00 | 100.0 | +0.419 [+0.289, +0.539] |
| rule POST | 0.00 | 100.0 | +0.076 [-0.115, +0.258] |

## F. Item-specific rule vs class-wide policy   (n = 136)

- specific `E7 has weight 0`, rule first: REI +0.836 [+0.749, +0.917]
- specific, rule last: REI +0.596 [+0.478, +0.713]
- class policy `any unauthorised item has weight 0`, rule first: REI +0.532 [+0.415, +0.646]
- class policy, rule last: REI +0.328 [+0.181, +0.477]

## G. Task preview   (n = 141)

- no preview, rule first: REI +0.419 [+0.291, +0.539]
- TASK PREVIEW, rule first: REI +0.505 [+0.343, +0.662]
- no preview, rule last: REI +0.076 [-0.105, +0.254]
- TASK PREVIEW, rule last: REI +0.085 [-0.107, +0.274]
- rescue from task preview (pre): -0.086 [-0.215, +0.052] p=0.2260

# mistral-small-24b

## A. Near-zero sweep — is zero a discontinuity?   (n = 142)

One identical sentence; only the percentage changes.

| requested w | rule BEFORE evidence | rule AFTER evidence | pre - post |
|---:|---|---|---|
| 0 | +0.085 [-0.042, +0.203] | +0.003 [-0.123, +0.116] | **+0.083** [-0.028, +0.194] p=0.1495 |
| 0.01 | +0.105 [-0.044, +0.240] | +0.067 [-0.067, +0.186] | **+0.039** [-0.049, +0.130] p=0.4080 |
| 0.025 | +0.237 [+0.105, +0.358] | +0.202 [+0.068, +0.323] | **+0.035** [-0.068, +0.137] p=0.4980 |
| 0.05 | +0.318 [+0.196, +0.430] | +0.201 [+0.063, +0.327] | **+0.117** [+0.015, +0.231] p=0.0215 |
| 0.1 | +0.300 [+0.161, +0.430] | +0.258 [+0.147, +0.356] | **+0.041** [-0.067, +0.157] p=0.4835 |
| 0.25 | +0.415 [+0.282, +0.537] | +0.352 [+0.256, +0.438] | **+0.062** [-0.053, +0.184] p=0.2905 |
| 0.5 | +0.585 [+0.485, +0.673] | +0.568 [+0.471, +0.658] | **+0.017** [-0.063, +0.105] p=0.7160 |
| 0.75 | +0.673 [+0.570, +0.773] | +0.691 [+0.634, +0.748] | **-0.018** [-0.123, +0.081] p=0.7510 |
| 1 | +1.007 [+0.961, +1.056] | +0.993 [+0.944, +1.039] | **+0.014** [-0.076, +0.108] p=0.7675 |

`REI ~ w + Before + w:Before + I[w=0]:Before`, cluster bootstrap:

| term | coef | 95% CI | p |
|---|---|---|---|
| intercept | +0.1155 | [+0.0004, +0.2315] | 0.0493 |
| w | +0.8549 | [+0.7209, +0.9845] | 0.0000 |
| Before | +0.0883 | [+0.0100, +0.1875] | 0.0247 |
| w x Before | -0.1063 | [-0.2072, -0.0148] | 0.0227 |
| **I[w=0] x Before** | -0.1183 | [-0.2284, -0.0192] | 0.0193 |

gap(0) = +0.083 vs gap(1%) = +0.039  ->  ratio 2.1x

## B. Rule-to-evidence delay   (n = 142)

Stage 2 moved the rule away from the ANSWER; this moves it away from the EVIDENCE it governs. Rule is always `weight = 0%`.

| filler between rule and evidence | rule BEFORE | rule AFTER | pre - post |
|---|---|---|---|
| 0 units (~0 tok) | +0.107 | -0.001 | +0.108 [-0.009, +0.223] |
| 4 units (~100 tok) | +0.096 | -0.005 | +0.102 [+0.030, +0.178] |
| 12 units (~300 tok) | +0.145 | +0.016 | +0.129 [+0.027, +0.235] |
| 40 units (~1000 tok) | +0.106 | +0.082 | +0.023 [-0.082, +0.122] |

## C. Object-existence ladder   (n = 138)

Identical rule (`Evidence E7 has decision weight 0.`) at every level; what changes is how much of E7 exists when the rule is stated. L5 is the retrospective anchor (full content already present).

- `L0 E7 never mentioned`: REI -0.046 [-0.202, +0.103]
- `L1 'you will later receive E7'`: REI +0.327 [+0.170, +0.477]
- `L2 [E7: content pending]`: REI +0.906 [+0.800, +1.006]
- `L3 + item type`: REI +0.829 [+0.693, +0.961]
- `L4 + type and direction`: REI +0.757 [+0.638, +0.877]
- `L5 full content BEFORE the rule`: REI +0.041 [-0.094, +0.170]

## D. Non-multiplicative transforms

| transform | rule BEFORE | rule AFTER | pre - post |
|---|---|---|---|
| `trflip` (target -1.0) | +0.054 | -0.210 | +0.264 [+0.062, +0.479] p=0.0080 |
| `trcap` | +0.406 | +0.254 | +0.152 [+0.052, +0.242] p=0.0035 |

## E. Declarative policy state vs causal use

Separate call, same context, asked what weight E should get. The decision run never sees this question.

| arm | says weight (mean %) | says exactly 0 (%) | REI in the decision run |
|---|---:|---:|---|
| rule PRE | 0.00 | 100.0 | +0.085 [-0.040, +0.204] |
| rule POST | 0.00 | 100.0 | +0.003 [-0.121, +0.121] |

## F. Item-specific rule vs class-wide policy   (n = 138)

- specific `E7 has weight 0`, rule first: REI -0.046 [-0.204, +0.105]
- specific, rule last: REI +0.041 [-0.097, +0.182]
- class policy `any unauthorised item has weight 0`, rule first: REI -0.077 [-0.217, +0.054]
- class policy, rule last: REI -0.108 [-0.278, +0.062]

## G. Task preview   (n = 142)

- no preview, rule first: REI +0.085 [-0.040, +0.203]
- TASK PREVIEW, rule first: REI +0.035 [-0.118, +0.182]
- no preview, rule last: REI +0.003 [-0.114, +0.120]
- TASK PREVIEW, rule last: REI -0.089 [-0.224, +0.039]
- rescue from task preview (pre): +0.050 [-0.039, +0.146] p=0.2880

# qwen3.5-27b

## A. Near-zero sweep — is zero a discontinuity?   (n = 139)

One identical sentence; only the percentage changes.

| requested w | rule BEFORE evidence | rule AFTER evidence | pre - post |
|---:|---|---|---|
| 0 | -0.021 [-0.189, +0.135] | -0.301 [-0.459, -0.141] | **+0.280** [+0.153, +0.416] p=0.0000 |
| 0.01 | -0.260 [-0.431, -0.099] | -0.313 [-0.492, -0.138] | **+0.054** [-0.075, +0.191] p=0.4095 |
| 0.025 | -0.189 [-0.366, -0.027] | -0.294 [-0.479, -0.121] | **+0.105** [+0.008, +0.215] p=0.0440 |
| 0.05 | -0.159 [-0.326, +0.004] | -0.284 [-0.470, -0.114] | **+0.125** [+0.015, +0.241] p=0.0335 |
| 0.1 | -0.123 [-0.307, +0.056] | -0.195 [-0.378, -0.016] | **+0.071** [-0.055, +0.215] p=0.2890 |
| 0.25 | +0.094 [-0.073, +0.264] | -0.082 [-0.263, +0.101] | **+0.176** [+0.046, +0.327] p=0.0075 |
| 0.5 | +0.453 [+0.286, +0.616] | +0.360 [+0.205, +0.512] | **+0.093** [-0.058, +0.246] p=0.2345 |
| 0.75 | +0.634 [+0.499, +0.759] | +0.562 [+0.421, +0.700] | **+0.072** [-0.068, +0.211] p=0.3155 |
| 1 | +0.978 [+0.924, +1.034] | +1.008 [+0.927, +1.074] | **-0.030** [-0.149, +0.103] p=0.6195 |

`REI ~ w + Before + w:Before + I[w=0]:Before`, cluster bootstrap:

| term | coef | 95% CI | p |
|---|---|---|---|
| intercept | -0.3351 | [-0.5156, -0.1581] | 0.0000 |
| w | +1.2946 | [+1.1307, +1.4617] | 0.0000 |
| Before | +0.1067 | [+0.0107, +0.2104] | 0.0300 |
| w x Before | -0.0823 | [-0.2396, +0.0653] | 0.3073 |
| **I[w=0] x Before** | +0.2073 | [+0.0668, +0.3544] | 0.0060 |

gap(0) = +0.280 vs gap(1%) = +0.054  ->  ratio 5.2x

## B. Rule-to-evidence delay   (n = 139)

Stage 2 moved the rule away from the ANSWER; this moves it away from the EVIDENCE it governs. Rule is always `weight = 0%`.

| filler between rule and evidence | rule BEFORE | rule AFTER | pre - post |
|---|---|---|---|
| 0 units (~0 tok) | -0.041 | -0.299 | +0.258 [+0.130, +0.399] |
| 4 units (~100 tok) | -0.134 | -0.414 | +0.280 [+0.155, +0.410] |
| 12 units (~300 tok) | -0.134 | -0.339 | +0.205 [+0.073, +0.345] |
| 40 units (~1000 tok) | -0.132 | -0.349 | +0.217 [+0.085, +0.364] |

## C. Object-existence ladder   (n = 134)

Identical rule (`Evidence E7 has decision weight 0.`) at every level; what changes is how much of E7 exists when the rule is stated. L5 is the retrospective anchor (full content already present).

- `L0 E7 never mentioned`: REI +0.041 [-0.128, +0.201]
- `L1 'you will later receive E7'`: REI +0.043 [-0.115, +0.197]
- `L2 [E7: content pending]`: REI +0.473 [+0.331, +0.605]
- `L3 + item type`: REI +0.480 [+0.328, +0.625]
- `L4 + type and direction`: REI +0.346 [+0.169, +0.507]
- `L5 full content BEFORE the rule`: REI -0.206 [-0.355, -0.069]

## D. Non-multiplicative transforms

| transform | rule BEFORE | rule AFTER | pre - post |
|---|---|---|---|
| `trflip` (target -1.0) | -0.735 | -0.857 | +0.122 [-0.053, +0.306] p=0.1795 |
| `trcap` | +0.223 | +0.086 | +0.136 [+0.036, +0.239] p=0.0055 |

## E. Declarative policy state vs causal use

Separate call, same context, asked what weight E should get. The decision run never sees this question.

| arm | says weight (mean %) | says exactly 0 (%) | REI in the decision run |
|---|---:|---:|---|
| rule PRE | 0.00 | 100.0 | -0.021 [-0.187, +0.135] |
| rule POST | 0.00 | 100.0 | -0.301 [-0.471, -0.147] |

## F. Item-specific rule vs class-wide policy   (n = 134)

- specific `E7 has weight 0`, rule first: REI +0.041 [-0.132, +0.200]
- specific, rule last: REI -0.206 [-0.355, -0.065]
- class policy `any unauthorised item has weight 0`, rule first: REI -0.262 [-0.433, -0.107]
- class policy, rule last: REI -0.297 [-0.448, -0.155]

## G. Task preview   (n = 139)

- no preview, rule first: REI -0.021 [-0.183, +0.135]
- TASK PREVIEW, rule first: REI -0.196 [-0.362, -0.037]
- no preview, rule last: REI -0.301 [-0.471, -0.145]
- TASK PREVIEW, rule last: REI -0.303 [-0.459, -0.151]
- rescue from task preview (pre): +0.175 [+0.032, +0.325] p=0.0215

# qwen3-32b

## A. Near-zero sweep — is zero a discontinuity?   (n = 140)

One identical sentence; only the percentage changes.

| requested w | rule BEFORE evidence | rule AFTER evidence | pre - post |
|---:|---|---|---|
| 0 | +0.237 [+0.137, +0.335] | -0.083 [-0.184, +0.013] | **+0.321** [+0.213, +0.435] p=0.0000 |
| 0.01 | +0.318 [+0.211, +0.419] | +0.123 [-0.000, +0.247] | **+0.194** [+0.051, +0.323] p=0.0040 |
| 0.025 | +0.339 [+0.248, +0.429] | +0.217 [+0.119, +0.314] | **+0.122** [+0.036, +0.206] p=0.0060 |
| 0.05 | +0.282 [+0.181, +0.370] | +0.207 [+0.104, +0.304] | **+0.075** [-0.058, +0.189] p=0.2300 |
| 0.1 | +0.393 [+0.317, +0.469] | +0.276 [+0.182, +0.366] | **+0.117** [+0.025, +0.208] p=0.0100 |
| 0.25 | +0.425 [+0.332, +0.512] | +0.360 [+0.290, +0.427] | **+0.064** [-0.031, +0.163] p=0.1670 |
| 0.5 | +0.496 [+0.428, +0.563] | +0.412 [+0.350, +0.469] | **+0.084** [+0.019, +0.155] p=0.0175 |
| 0.75 | +0.651 [+0.570, +0.722] | +0.665 [+0.613, +0.724] | **-0.013** [-0.121, +0.070] p=0.8620 |
| 1 | +1.045 [+1.004, +1.090] | +0.955 [+0.911, +0.996] | **+0.091** [+0.004, +0.181] p=0.0360 |

`REI ~ w + Before + w:Before + I[w=0]:Before`, cluster bootstrap:

| term | coef | 95% CI | p |
|---|---|---|---|
| intercept | +0.1121 | [+0.0118, +0.2190] | 0.0280 |
| w | +0.7906 | [+0.6563, +0.9148] | 0.0000 |
| Before | +0.1681 | [+0.0388, +0.2954] | 0.0107 |
| w x Before | -0.1548 | [-0.2872, -0.0203] | 0.0240 |
| **I[w=0] x Before** | -0.0430 | [-0.1328, +0.0570] | 0.3920 |

gap(0) = +0.321 vs gap(1%) = +0.194  ->  ratio 1.6x

## B. Rule-to-evidence delay   (n = 140)

Stage 2 moved the rule away from the ANSWER; this moves it away from the EVIDENCE it governs. Rule is always `weight = 0%`.

| filler between rule and evidence | rule BEFORE | rule AFTER | pre - post |
|---|---|---|---|
| 0 units (~0 tok) | +0.231 | -0.087 | +0.318 [+0.216, +0.430] |
| 4 units (~100 tok) | +0.248 | -0.032 | +0.280 [+0.161, +0.403] |
| 12 units (~300 tok) | +0.139 | +0.026 | +0.113 [+0.016, +0.208] |
| 40 units (~1000 tok) | +0.233 | +0.011 | +0.222 [+0.074, +0.345] |

## C. Object-existence ladder   (n = 142)

Identical rule (`Evidence E7 has decision weight 0.`) at every level; what changes is how much of E7 exists when the rule is stated. L5 is the retrospective anchor (full content already present).

- `L0 E7 never mentioned`: REI +0.481 [+0.364, +0.599]
- `L1 'you will later receive E7'`: REI +0.701 [+0.587, +0.808]
- `L2 [E7: content pending]`: REI +0.844 [+0.769, +0.923]
- `L3 + item type`: REI +0.865 [+0.770, +0.959]
- `L4 + type and direction`: REI +0.797 [+0.698, +0.892]
- `L5 full content BEFORE the rule`: REI -0.007 [-0.137, +0.118]

## D. Non-multiplicative transforms

| transform | rule BEFORE | rule AFTER | pre - post |
|---|---|---|---|
| `trflip` (target -1.0) | +0.252 | -0.057 | +0.308 [+0.104, +0.502] p=0.0045 |
| `trcap` | +0.373 | +0.265 | +0.108 [+0.048, +0.175] p=0.0000 |

## E. Declarative policy state vs causal use

Separate call, same context, asked what weight E should get. The decision run never sees this question.

| arm | says weight (mean %) | says exactly 0 (%) | REI in the decision run |
|---|---:|---:|---|
| rule PRE | 0.00 | 100.0 | +0.237 [+0.137, +0.338] |
| rule POST | 0.00 | 100.0 | -0.083 [-0.183, +0.017] |

## F. Item-specific rule vs class-wide policy   (n = 142)

- specific `E7 has weight 0`, rule first: REI +0.481 [+0.359, +0.594]
- specific, rule last: REI -0.007 [-0.134, +0.115]
- class policy `any unauthorised item has weight 0`, rule first: REI +0.113 [-0.016, +0.235]
- class policy, rule last: REI -0.153 [-0.291, -0.021]

## G. Task preview   (n = 140)

- no preview, rule first: REI +0.237 [+0.137, +0.336]
- TASK PREVIEW, rule first: REI +0.276 [+0.164, +0.379]
- no preview, rule last: REI -0.083 [-0.181, +0.012]
- TASK PREVIEW, rule last: REI -0.094 [-0.207, +0.013]
- rescue from task preview (pre): -0.038 [-0.128, +0.061] p=0.4140

# phi4-mini

## A. Near-zero sweep — is zero a discontinuity?   (n = 138)

One identical sentence; only the percentage changes.

| requested w | rule BEFORE evidence | rule AFTER evidence | pre - post |
|---:|---|---|---|
| 0 | +0.644 [+0.512, +0.779] | +0.387 [+0.230, +0.539] | **+0.256** [+0.104, +0.421] p=0.0000 |
| 0.01 | +0.527 [+0.383, +0.662] | +0.481 [+0.349, +0.612] | **+0.047** [-0.131, +0.228] p=0.6305 |
| 0.025 | +0.592 [+0.446, +0.736] | +0.459 [+0.312, +0.602] | **+0.133** [-0.025, +0.284] p=0.0935 |
| 0.05 | +0.632 [+0.486, +0.774] | +0.385 [+0.243, +0.519] | **+0.247** [+0.082, +0.419] p=0.0085 |
| 0.1 | +0.553 [+0.416, +0.688] | +0.617 [+0.505, +0.723] | **-0.064** [-0.211, +0.070] p=0.3470 |
| 0.25 | +0.546 [+0.405, +0.680] | +0.490 [+0.359, +0.616] | **+0.056** [-0.106, +0.206] p=0.4720 |
| 0.5 | +0.653 [+0.508, +0.797] | +0.550 [+0.440, +0.661] | **+0.104** [-0.059, +0.255] p=0.1945 |
| 0.75 | +0.774 [+0.637, +0.904] | +0.721 [+0.612, +0.825] | **+0.053** [-0.110, +0.204] p=0.5060 |
| 1 | +1.056 [+0.984, +1.131] | +0.904 [+0.791, +1.003] | **+0.152** [-0.011, +0.344] p=0.0870 |

`REI ~ w + Before + w:Before + I[w=0]:Before`, cluster bootstrap:

| term | coef | 95% CI | p |
|---|---|---|---|
| intercept | +0.4315 | [+0.3247, +0.5318] | 0.0000 |
| w | +0.4138 | [+0.2972, +0.5252] | 0.0000 |
| Before | +0.0936 | [-0.0155, +0.1961] | 0.0907 |
| w x Before | +0.0080 | [-0.1215, +0.1549] | 0.9133 |
| **I[w=0] x Before** | +0.1186 | [-0.0277, +0.2879] | 0.1200 |

gap(0) = +0.256 vs gap(1%) = +0.047  ->  ratio 5.5x

## B. Rule-to-evidence delay   (n = 138)

Stage 2 moved the rule away from the ANSWER; this moves it away from the EVIDENCE it governs. Rule is always `weight = 0%`.

| filler between rule and evidence | rule BEFORE | rule AFTER | pre - post |
|---|---|---|---|
| 0 units (~0 tok) | +0.635 | +0.390 | +0.245 [+0.064, +0.430] |
| 4 units (~100 tok) | +0.689 | +0.456 | +0.233 [+0.084, +0.377] |
| 12 units (~300 tok) | +0.665 | +0.510 | +0.155 [+0.022, +0.286] |
| 40 units (~1000 tok) | +0.643 | +0.517 | +0.126 [-0.044, +0.297] |

## C. Object-existence ladder   (n = 136)

Identical rule (`Evidence E7 has decision weight 0.`) at every level; what changes is how much of E7 exists when the rule is stated. L5 is the retrospective anchor (full content already present).

- `L0 E7 never mentioned`: REI +0.778 [+0.568, +0.971]
- `L1 'you will later receive E7'`: REI +0.948 [+0.754, +1.129]
- `L2 [E7: content pending]`: REI +0.995 [+0.834, +1.146]
- `L3 + item type`: REI +0.855 [+0.665, +1.027]
- `L4 + type and direction`: REI +0.864 [+0.695, +1.023]
- `L5 full content BEFORE the rule`: REI +0.184 [-0.022, +0.376]

## D. Non-multiplicative transforms

| transform | rule BEFORE | rule AFTER | pre - post |
|---|---|---|---|
| `trflip` (target -1.0) | +0.466 | +0.313 | +0.152 [+0.029, +0.282] p=0.0180 |
| `trcap` | +0.742 | +0.404 | +0.338 [+0.169, +0.516] p=0.0005 |

## E. Declarative policy state vs causal use

Separate call, same context, asked what weight E should get. The decision run never sees this question.

| arm | says weight (mean %) | says exactly 0 (%) | REI in the decision run |
|---|---:|---:|---|
| rule PRE | 0.00 | 100.0 | +0.644 [+0.510, +0.777] |
| rule POST | 0.00 | 100.0 | +0.387 [+0.233, +0.545] |

## F. Item-specific rule vs class-wide policy   (n = 136)

- specific `E7 has weight 0`, rule first: REI +0.778 [+0.582, +0.969]
- specific, rule last: REI +0.184 [-0.021, +0.378]
- class policy `any unauthorised item has weight 0`, rule first: REI +0.557 [+0.375, +0.733]
- class policy, rule last: REI +0.240 [+0.045, +0.428]

## G. Task preview   (n = 138)

- no preview, rule first: REI +0.644 [+0.513, +0.779]
- TASK PREVIEW, rule first: REI +0.722 [+0.591, +0.856]
- no preview, rule last: REI +0.387 [+0.231, +0.546]
- TASK PREVIEW, rule last: REI +0.336 [+0.186, +0.489]
- rescue from task preview (pre): -0.078 [-0.198, +0.038] p=0.1925
