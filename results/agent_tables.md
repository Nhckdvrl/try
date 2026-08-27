# Stage 4A — system policy, tool output, answer

SYSTEM carries the policy before anything is retrieved; the document arrives in a
TOOL message; the assistant then answers. REI is anchored on `ag_base` (document
not retrieved) and `ag_padmit_same_d7` (document retrieved and endorsed).


## qwen3-8b   (n usable = 56)

| condition | REI |
|---|---|
| no policy at all (naive) | **+0.991** [+0.898, +1.091] |
| policy names D7 only | **+1.014** [+0.926, +1.128] |
| policy names D7 + a gist of it | **+0.870** [+0.658, +1.056] |
| policy names D7 + its full proposition | **+0.602** [+0.351, +0.856] |
| policy delivered AFTER the tool output | **+0.380** [+0.241, +0.526] |
| ID-only policy, D7 arrives paraphrased | **+0.666** [+0.440, +0.868] |
| proposition policy, D7 arrives paraphrased | **+0.720** [+0.475, +0.960] |
| ID-only policy, D7 carries a DIFFERENT proposition | **+0.910** [+0.668, +1.117] |
| proposition policy, D7 carries a DIFFERENT proposition | **+1.008** [+0.739, +1.245] |
| ID-only policy, same proposition arrives as D9 | **+0.906** [+0.833, +0.975] |
| proposition policy, same proposition arrives as D9 | **+0.678** [+0.436, +0.930] |

## gemma3-12b   (n usable = 74)

| condition | REI |
|---|---|
| no policy at all (naive) | **+0.839** [+0.756, +0.912] |
| policy names D7 only | **+0.386** [+0.209, +0.586] |
| policy names D7 + a gist of it | **+0.751** [+0.625, +0.864] |
| policy names D7 + its full proposition | **+0.454** [+0.317, +0.593] |
| policy delivered AFTER the tool output | **+0.191** [+0.106, +0.293] |
| ID-only policy, D7 arrives paraphrased | **+0.317** [+0.165, +0.485] |
| proposition policy, D7 arrives paraphrased | **+0.372** [+0.247, +0.509] |
| ID-only policy, D7 carries a DIFFERENT proposition | **+0.445** [+0.232, +0.691] |
| proposition policy, D7 carries a DIFFERENT proposition | **+0.572** [+0.384, +0.776] |
| ID-only policy, same proposition arrives as D9 | **+0.851** [+0.781, +0.920] |
| proposition policy, same proposition arrives as D9 | **+0.424** [+0.295, +0.554] |

## phi4-mini   (n usable = 73)

| condition | REI |
|---|---|
| no policy at all (naive) | **+1.038** [+0.892, +1.171] |
| policy names D7 only | **+0.940** [+0.742, +1.123] |
| policy names D7 + a gist of it | **+1.064** [+0.892, +1.246] |
| policy names D7 + its full proposition | **+0.753** [+0.513, +0.974] |
| policy delivered AFTER the tool output | **-0.156** [-0.412, +0.070] |
| ID-only policy, D7 arrives paraphrased | **+0.324** [+0.098, +0.536] |
| proposition policy, D7 arrives paraphrased | **+0.810** [+0.532, +1.085] |
| ID-only policy, D7 carries a DIFFERENT proposition | **+1.050** [+0.834, +1.266] |
| proposition policy, D7 carries a DIFFERENT proposition | **+0.979** [+0.758, +1.197] |
| ID-only policy, same proposition arrives as D9 | **+0.849** [+0.617, +1.050] |
| proposition policy, same proposition arrives as D9 | **+0.712** [+0.498, +0.913] |
