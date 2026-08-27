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
