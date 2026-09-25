# G24A results — g24a-v1

REI: 0 = ignored the excluded evidence, 1 = used it as admitted. Winsorised at +/-3; CIs are 10,000-resample **cluster** bootstraps over evidence clusters (seed 20260924); cluster key = `source/first-evidence-page-or-doc_id`.
Prereg: `preregistrations/PREREGISTRATION_G24A_NATURAL_EVIDENCE.md` (tag `g24a-natural-evidence-confirmation-design-v1`).
Selection model `mistral-small-24b` is excluded from pooled-4 (item set conditioned on its own Admit leverage).

## Verdict
**prospective-only**

Natural evidence leaks even when the zero-use ruling precedes it, but the retrospective arm is not distinguishable from zero.

- P1 (REI_pre pooled-4 CI lower > 0): PASS — +0.541 [+0.478,+0.604] p=0.0000
- P2 (REI_post pooled-4 CI lower > 0): FAIL — -0.072 [-0.161,+0.017] p=0.1170
- C1 (both REI points > 0 in ≥4/5 models): FAIL — 2/5 (gemma3-12b, qwen3-8b)
- C2 (both REI points > 0 within each source): FAIL — fever=fail, scifact=fail
- Sufficiency gate (pooled-4 usable items ≥ 300): PASS — 592/600 selected items

## pooled-4 (primary)
n=2007/2400 items=592 clusters=467  median|L|=32.7  alignment=0.84
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.974)
    REI_pre   +0.541 [+0.478,+0.604] p=0.0000
    REI_post  -0.072 [-0.161,+0.017] p=0.1170
    d_time    -0.559 [-0.627,-0.492] p=0.0000   items post>pre: 0.32
    UTB_norm  -0.535 [-0.606,-0.465] p=0.0000
    items REI_post>0.2: 0.55

## pooled-5 (incl. selection model)
n=2592/3000 items=600 clusters=472  median|L|=33.4  alignment=0.86
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.978)
    REI_pre   +0.380 [+0.322,+0.438] p=0.0000
    REI_post  -0.100 [-0.185,-0.016] p=0.0176
    d_time    -0.437 [-0.496,-0.381] p=0.0000   items post>pre: 0.36
    UTB_norm  -0.414 [-0.475,-0.354] p=0.0000
    items REI_post>0.2: 0.52

## model gemma3-12b
n=542/600 items=542 clusters=432  median|L|=33.3  alignment=0.90
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.187 [+0.078,+0.290] p=0.0010
    REI_post  +0.159 [+0.040,+0.274] p=0.0070
    d_time    -0.051 [-0.160,+0.061] p=0.3780   items post>pre: 0.52
    UTB_norm  +0.027 [-0.084,+0.141] p=0.6198
    items REI_post>0.2: 0.60

## model llama31-8b
n=460/600 items=460 clusters=384  median|L|=33.5  alignment=0.77
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.998)
    REI_pre   +0.480 [+0.366,+0.592] p=0.0000
    REI_post  -0.274 [-0.416,-0.136] p=0.0000
    d_time    -0.717 [-0.845,-0.588] p=0.0000   items post>pre: 0.30
    UTB_norm  -0.694 [-0.833,-0.554] p=0.0000
    items REI_post>0.2: 0.42

## model mistral-small-24b
n=585/600 items=585 clusters=461  median|L|=39.6  alignment=0.97
    RuleAcc  exclude-pre 0.999  exclude-post 0.999  (admit-control p(YES) 0.992)
    REI_pre   -0.171 [-0.270,-0.074] p=0.0008
    REI_post  -0.195 [-0.304,-0.090] p=0.0002
    d_time    -0.020 [-0.097,+0.056] p=0.6248   items post>pre: 0.49
    UTB_norm  +0.002 [-0.079,+0.085] p=0.9572
    items REI_post>0.2: 0.44

## model qwen3-8b
n=503/600 items=503 clusters=412  median|L|=36.0  alignment=0.84
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.913)
    REI_pre   +0.772 [+0.670,+0.867] p=0.0000
    REI_post  +0.329 [+0.198,+0.456] p=0.0000
    d_time    -0.414 [-0.524,-0.304] p=0.0000   items post>pre: 0.31
    UTB_norm  -0.455 [-0.565,-0.343] p=0.0000
    items REI_post>0.2: 0.71

## model qwen35-9b
n=502/600 items=502 clusters=402  median|L|=16.8  alignment=0.84
    RuleAcc  exclude-pre 1.000  exclude-post 0.999  (admit-control p(YES) 0.984)
    REI_pre   +0.747 [+0.654,+0.836] p=0.0000
    REI_post  -0.538 [-0.691,-0.389] p=0.0000
    d_time    -1.108 [-1.228,-0.984] p=0.0000   items post>pre: 0.14
    UTB_norm  -1.078 [-1.204,-0.949] p=0.0000
    items REI_post>0.2: 0.47

## pooled-4 fever
n=1326/1600 items=395 clusters=314  median|L|=33.6  alignment=0.83
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.967)
    REI_pre   +0.540 [+0.458,+0.618] p=0.0000
    REI_post  -0.092 [-0.202,+0.020] p=0.1050
    d_time    -0.582 [-0.662,-0.500] p=0.0000   items post>pre: 0.30
    UTB_norm  -0.559 [-0.645,-0.473] p=0.0000
    items REI_post>0.2: 0.56

## pooled-4 scifact
n=681/800 items=197 clusters=153  median|L|=31.3  alignment=0.85
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.986)
    REI_pre   +0.544 [+0.440,+0.643] p=0.0000
    REI_post  -0.033 [-0.186,+0.120] p=0.6786
    d_time    -0.515 [-0.627,-0.403] p=0.0000   items post>pre: 0.36
    UTB_norm  -0.490 [-0.606,-0.374] p=0.0000
    items REI_post>0.2: 0.52

## pooled-4 fever/SUPPORTS
n=694/800 items=198 clusters=182  median|L|=26.5  alignment=0.87
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.998)
    REI_pre   +0.236 [+0.116,+0.350] p=0.0000
    REI_post  -0.718 [-0.851,-0.585] p=0.0000
    d_time    -0.897 [-1.015,-0.777] p=0.0000   items post>pre: 0.22
    UTB_norm  -0.907 [-1.027,-0.786] p=0.0000
    items REI_post>0.2: 0.37

## pooled-4 fever/REFUTES
n=632/800 items=197 clusters=173  median|L|=40.0  alignment=0.79
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.934)
    REI_pre   +0.874 [+0.790,+0.955] p=0.0000
    REI_post  +0.596 [+0.483,+0.705] p=0.0000
    d_time    -0.236 [-0.320,-0.153] p=0.0000   items post>pre: 0.39
    UTB_norm  -0.176 [-0.268,-0.085] p=0.0000
    items REI_post>0.2: 0.78

## pooled-4 scifact/SUPPORT
n=363/400 items=100 clusters=94  median|L|=26.5  alignment=0.91
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.998)
    REI_pre   +0.241 [+0.081,+0.392] p=0.0020
    REI_post  -0.872 [-1.039,-0.708] p=0.0000
    d_time    -1.019 [-1.160,-0.881] p=0.0000   items post>pre: 0.19
    UTB_norm  -1.029 [-1.166,-0.892] p=0.0000
    items REI_post>0.2: 0.25

## pooled-4 scifact/CONTRADICT
n=318/400 items=97 clusters=86  median|L|=38.9  alignment=0.80
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.972)
    REI_pre   +0.889 [+0.800,+0.979] p=0.0000
    REI_post  +0.924 [+0.814,+1.033] p=0.0000
    d_time    +0.061 [-0.047,+0.166] p=0.2558   items post>pre: 0.55
    UTB_norm  +0.126 [+0.019,+0.230] p=0.0218
    items REI_post>0.2: 0.84

## Integrity
- models present: ['gemma3-12b', 'llama31-8b', 'mistral-small-24b', 'qwen3-8b', 'qwen35-9b'] (frozen panel required)
- per-model completeness ledger: {"gemma3-12b": {"expected": 600, "complete": 600, "partial": 0, "absent": 0}, "llama31-8b": {"expected": 600, "complete": 600, "partial": 0, "absent": 0}, "mistral-small-24b": {"expected": 600, "complete": 600, "partial": 0, "absent": 0}, "qwen3-8b": {"expected": 600, "complete": 600, "partial": 0, "absent": 0}, "qwen35-9b": {"expected": 600, "complete": 600, "partial": 0, "absent": 0}}
- all selected items have complete five-condition rows in all five models

