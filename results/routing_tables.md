# Stage 3B — prospective selective routing

`Y ~ a + b*mean_admitted + c*mean_excluded`. b = fidelity to admitted evidence
(correct: 1.0). c = leakage from excluded evidence (correct: 0.0). Cluster
bootstrap over surface x size cells.

# qwen3-8b

| condition | n | b (admitted) | c (leakage) | mean abs error vs oracle answer |
|---|---:|---|---|---|
| oracle (only admitted shown) | 48 | +0.998 [+0.987, +1.007] | **+0.003** [-0.002, +0.010] p=0.2200 | 0.4 |
| naive (all reports, no policy) | 48 | +0.526 [+0.327, +0.698] | **+0.480** [+0.334, +0.620] p=0.0000 | 21.1 |
| policy BEFORE the reports | 48 | +0.774 [+0.229, +1.005] | **-0.174** [-0.610, +0.005] p=0.5627 | 7.6 |
| policy AFTER the reports | 48 | +0.996 [+0.983, +1.006] | **+0.004** [-0.000, +0.010] p=0.1000 | 0.3 |

Leakage coefficient c by number of reports in the stream:

| N reports | policy BEFORE | policy AFTER |
|---:|---|---|
| 2 | -0.000 [-0.000, +0.000] | -0.000 [-0.000, +0.000] |
| 4 | +0.000 [-0.000, +0.000] | +0.000 [-0.000, +0.000] |
| 8 | +0.011 [-0.002, +0.024] | +0.018 [-0.001, +0.033] |
| 16 | -0.528 [-2.544, +0.215] | -0.001 [-0.007, +0.005] |
- RuleAcc, policy first: says NO with p = 1.000
- RuleAcc, policy last: says NO with p = 1.000

# mistral-small-24b

| condition | n | b (admitted) | c (leakage) | mean abs error vs oracle answer |
|---|---:|---|---|---|
| oracle (only admitted shown) | 48 | +1.002 [+0.998, +1.007] | **+0.001** [-0.004, +0.006] p=0.8073 | 0.2 |
| naive (all reports, no policy) | 48 | +0.456 [+0.237, +0.630] | **+0.536** [+0.420, +0.659] p=0.0000 | 22.4 |
| policy BEFORE the reports | 48 | +1.002 [+1.000, +1.005] | **+0.001** [-0.002, +0.003] p=0.5913 | 0.1 |
| policy AFTER the reports | 48 | +1.002 [+0.999, +1.005] | **+0.001** [-0.002, +0.002] p=0.6127 | 0.2 |

Leakage coefficient c by number of reports in the stream:

| N reports | policy BEFORE | policy AFTER |
|---:|---|---|
| 2 | -0.000 [-0.000, +0.000] | -0.000 [-0.000, +0.000] |
| 4 | +0.000 [-0.000, +0.000] | +0.000 [-0.000, +0.000] |
| 8 | -0.002 [-0.008, +0.001] | -0.003 [-0.006, +0.003] |
| 16 | +0.003 [-0.002, +0.007] | +0.002 [-0.002, +0.007] |
- RuleAcc, policy first: says NO with p = 1.000
- RuleAcc, policy last: says NO with p = 1.000
