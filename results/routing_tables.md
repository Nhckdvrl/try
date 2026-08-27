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

# gemma3-12b

| condition | n | b (admitted) | c (leakage) | mean abs error vs oracle answer |
|---|---:|---|---|---|
| oracle (only admitted shown) | 48 | +0.997 [+0.986, +1.003] | **+0.003** [-0.002, +0.011] p=0.3013 | 0.3 |
| naive (all reports, no policy) | 48 | +0.469 [+0.319, +0.611] | **+0.475** [+0.370, +0.575] p=0.0000 | 20.1 |
| policy BEFORE the reports | 48 | +0.999 [+0.987, +1.011] | **-0.014** [-0.037, +0.001] p=0.1200 | 0.5 |
| policy AFTER the reports | 48 | +0.996 [+0.980, +1.011] | **-0.019** [-0.048, -0.000] p=0.0440 | 1.6 |

Leakage coefficient c by number of reports in the stream:

| N reports | policy BEFORE | policy AFTER |
|---:|---|---|
| 2 | -0.000 [-0.000, +0.000] | -0.000 [-0.000, +0.000] |
| 4 | +0.000 [-0.000, +0.000] | +0.000 [-0.000, +0.000] |
| 8 | -0.000 [-0.002, +0.004] | -0.001 [-0.008, +0.007] |
| 16 | -0.036 [-0.134, +0.002] | -0.065 [-0.236, +0.046] |
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

# phi4-mini

| condition | n | b (admitted) | c (leakage) | mean abs error vs oracle answer |
|---|---:|---|---|---|
| oracle (only admitted shown) | 48 | +1.004 [+0.996, +1.016] | **+0.002** [-0.006, +0.008] p=0.6067 | 0.5 |
| naive (all reports, no policy) | 48 | +0.547 [+0.432, +0.672] | **+0.496** [+0.443, +0.559] p=0.0000 | 21.0 |
| policy BEFORE the reports | 48 | +1.013 [+0.987, +1.051] | **+0.016** [-0.000, +0.044] p=0.0613 | 0.8 |
| policy AFTER the reports | 48 | +0.998 [+0.992, +1.005] | **+0.003** [-0.002, +0.008] p=0.2460 | 0.3 |

Leakage coefficient c by number of reports in the stream:

| N reports | policy BEFORE | policy AFTER |
|---:|---|---|
| 2 | +0.036 [-0.024, +0.502] | -0.000 [-0.000, +0.000] |
| 4 | +0.000 [-0.000, +0.000] | +0.003 [-0.000, +0.014] |
| 8 | +0.007 [-0.007, +0.034] | +0.007 [+0.001, +0.019] |
| 16 | +0.010 [+0.004, +0.016] | +0.002 [-0.017, +0.018] |
- RuleAcc, policy first: says NO with p = 0.998
- RuleAcc, policy last: says NO with p = 0.997

# qwen3.5-9b

| condition | n | b (admitted) | c (leakage) | mean abs error vs oracle answer |
|---|---:|---|---|---|
| oracle (only admitted shown) | 48 | +0.996 [+0.989, +1.000] | **+0.001** [-0.002, +0.005] p=0.4100 | 0.2 |
| naive (all reports, no policy) | 48 | +0.501 [+0.282, +0.702] | **+0.406** [+0.316, +0.504] p=0.0000 | 18.6 |
| policy BEFORE the reports | 48 | +1.000 [+1.000, +1.001] | **-0.000** [-0.001, +0.000] p=0.1560 | 0.0 |
| policy AFTER the reports | 48 | +1.000 [+0.999, +1.001] | **-0.001** [-0.003, -0.000] p=0.0147 | 0.1 |

Leakage coefficient c by number of reports in the stream:

| N reports | policy BEFORE | policy AFTER |
|---:|---|---|
| 2 | -0.000 [-0.000, +0.000] | -0.000 [-0.000, +0.000] |
| 4 | +0.000 [-0.000, +0.000] | +0.000 [-0.000, +0.000] |
| 8 | -0.000 [-0.001, +0.000] | -0.001 [-0.001, -0.000] |
| 16 | -0.001 [-0.001, -0.000] | -0.004 [-0.005, -0.001] |
- RuleAcc, policy first: says NO with p = 1.000
- RuleAcc, policy last: says NO with p = 1.000
