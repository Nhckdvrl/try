# G24A results — g24a-v1

REI: 0 = ignored the excluded evidence, 1 = used it as admitted. Winsorised at +/-3; CIs are 10,000-resample **cluster** bootstraps over evidence clusters (seed 20260924); cluster key = `source/first-evidence-page-or-doc_id`.
Prereg: `preregistrations/PREREGISTRATION_G24A_NATURAL_EVIDENCE.md` (tag `g24a-natural-evidence-confirmation-design-v1`).
Selection model `mistral-small-24b` is excluded from pooled-4 (item set conditioned on its own Admit leverage).

## Verdict
**prospective-only**

Natural evidence leaks even when the zero-use ruling precedes it, but the retrospective arm is not distinguishable from zero.

- P1 (REI_pre pooled-4 CI lower > 0): PASS — +0.541 [+0.477,+0.603] p=0.0000
- P2 (REI_post pooled-4 CI lower > 0): FAIL — -0.067 [-0.158,+0.021] p=0.1334
- C1 (both REI points > 0 in ≥4/5 models): FAIL — 2/5 (gemma3-12b, qwen3-8b)
- C2 (both REI points > 0 within each source): FAIL — fever=fail, scifact=pass
- Sufficiency gate (pooled-4 usable items ≥ 300): PASS — 595/600 selected items

## pooled-4 (primary)
n=2014/2400 items=595 clusters=469  median|L|=32.7  alignment=0.84
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.974)
    REI_pre   +0.541 [+0.477,+0.603] p=0.0000
    REI_post  -0.067 [-0.158,+0.021] p=0.1334
    d_time    -0.543 [-0.613,-0.474] p=0.0000   items post>pre: 0.32
    UTB_norm  -0.518 [-0.593,-0.446] p=0.0000
    items REI_post>0.2: 0.55

## pooled-5 (incl. selection model)
n=2610/3000 items=600 clusters=472  median|L|=33.4  alignment=0.87
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.978)
    REI_pre   +0.395 [+0.339,+0.449] p=0.0000
    REI_post  -0.081 [-0.164,+0.001] p=0.0514
    d_time    -0.430 [-0.489,-0.373] p=0.0000   items post>pre: 0.36
    UTB_norm  -0.401 [-0.464,-0.339] p=0.0000
    items REI_post>0.2: 0.53

## model gemma3-12b
n=539/600 items=539 clusters=434  median|L|=33.2  alignment=0.90
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.214 [+0.105,+0.319] p=0.0002
    REI_post  +0.139 [+0.014,+0.261] p=0.0308
    d_time    -0.057 [-0.169,+0.054] p=0.3130   items post>pre: 0.52
    UTB_norm  -0.001 [-0.114,+0.115] p=0.9976
    items REI_post>0.2: 0.60

## model llama31-8b
n=465/600 items=465 clusters=388  median|L|=33.1  alignment=0.78
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.998)
    REI_pre   +0.453 [+0.336,+0.565] p=0.0000
    REI_post  -0.290 [-0.425,-0.159] p=0.0004
    d_time    -0.708 [-0.843,-0.573] p=0.0000   items post>pre: 0.28
    UTB_norm  -0.656 [-0.801,-0.509] p=0.0000
    items REI_post>0.2: 0.42

## model mistral-small-24b
n=596/600 items=596 clusters=469  median|L|=39.9  alignment=0.99
    RuleAcc  exclude-pre 0.999  exclude-post 0.999  (admit-control p(YES) 0.992)
    REI_pre   -0.100 [-0.197,-0.009] p=0.0322
    REI_post  -0.129 [-0.236,-0.026] p=0.0154
    d_time    -0.047 [-0.117,+0.021] p=0.1800   items post>pre: 0.50
    UTB_norm  -0.004 [-0.083,+0.074] p=0.9274
    items REI_post>0.2: 0.45

## model qwen3-8b
n=509/600 items=509 clusters=412  median|L|=35.2  alignment=0.85
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.914)
    REI_pre   +0.750 [+0.646,+0.851] p=0.0000
    REI_post  +0.295 [+0.163,+0.423] p=0.0000
    d_time    -0.418 [-0.528,-0.310] p=0.0000   items post>pre: 0.32
    UTB_norm  -0.433 [-0.549,-0.317] p=0.0000
    items REI_post>0.2: 0.69

## model qwen35-9b
n=501/600 items=501 clusters=402  median|L|=17.9  alignment=0.83
    RuleAcc  exclude-pre 1.000  exclude-post 0.999  (admit-control p(YES) 0.984)
    REI_pre   +0.762 [+0.668,+0.852] p=0.0000
    REI_post  -0.450 [-0.599,-0.301] p=0.0000
    d_time    -1.040 [-1.165,-0.915] p=0.0000   items post>pre: 0.16
    UTB_norm  -1.034 [-1.160,-0.908] p=0.0000
    items REI_post>0.2: 0.47

## pooled-4 fever
n=1326/1600 items=397 clusters=315  median|L|=33.4  alignment=0.83
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.967)
    REI_pre   +0.523 [+0.442,+0.601] p=0.0000
    REI_post  -0.106 [-0.218,+0.000] p=0.0512
    d_time    -0.553 [-0.639,-0.468] p=0.0000   items post>pre: 0.30
    UTB_norm  -0.534 [-0.624,-0.445] p=0.0000
    items REI_post>0.2: 0.55

## pooled-4 scifact
n=688/800 items=198 clusters=154  median|L|=30.9  alignment=0.86
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.988)
    REI_pre   +0.575 [+0.477,+0.672] p=0.0000
    REI_post  +0.007 [-0.148,+0.159] p=0.9270
    d_time    -0.524 [-0.639,-0.406] p=0.0000   items post>pre: 0.36
    UTB_norm  -0.488 [-0.612,-0.362] p=0.0000
    items REI_post>0.2: 0.54

## pooled-4 fever/SUPPORTS
n=698/800 items=199 clusters=182  median|L|=27.5  alignment=0.87
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.998)
    REI_pre   +0.233 [+0.113,+0.347] p=0.0000
    REI_post  -0.732 [-0.864,-0.598] p=0.0000
    d_time    -0.875 [-0.995,-0.756] p=0.0000   items post>pre: 0.21
    UTB_norm  -0.893 [-1.013,-0.770] p=0.0000
    items REI_post>0.2: 0.36

## pooled-4 fever/REFUTES
n=628/800 items=198 clusters=174  median|L|=38.7  alignment=0.79
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.932)
    REI_pre   +0.846 [+0.765,+0.923] p=0.0000
    REI_post  +0.590 [+0.476,+0.702] p=0.0000
    d_time    -0.195 [-0.291,-0.101] p=0.0004   items post>pre: 0.40
    UTB_norm  -0.135 [-0.238,-0.032] p=0.0080
    items REI_post>0.2: 0.77

## pooled-4 scifact/SUPPORT
n=358/400 items=100 clusters=94  median|L|=25.0  alignment=0.90
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.998)
    REI_pre   +0.255 [+0.106,+0.391] p=0.0014
    REI_post  -0.879 [-1.045,-0.714] p=0.0000
    d_time    -1.090 [-1.236,-0.945] p=0.0000   items post>pre: 0.18
    UTB_norm  -1.083 [-1.229,-0.940] p=0.0000
    items REI_post>0.2: 0.25

## pooled-4 scifact/CONTRADICT
n=330/400 items=98 clusters=87  median|L|=36.2  alignment=0.82
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 0.976)
    REI_pre   +0.923 [+0.831,+1.023] p=0.0000
    REI_post  +0.968 [+0.860,+1.080] p=0.0000
    d_time    +0.090 [-0.023,+0.205] p=0.1156   items post>pre: 0.55
    UTB_norm  +0.158 [+0.028,+0.294] p=0.0182
    items REI_post>0.2: 0.86

## Integrity
- models present: ['gemma3-12b', 'llama31-8b', 'mistral-small-24b', 'qwen3-8b', 'qwen35-9b'] (frozen panel required)
- per-model completeness ledger: {"gemma3-12b": {"expected": 600, "complete": 600, "partial": 0, "absent": 0}, "llama31-8b": {"expected": 600, "complete": 600, "partial": 0, "absent": 0}, "mistral-small-24b": {"expected": 600, "complete": 600, "partial": 0, "absent": 0}, "qwen3-8b": {"expected": 600, "complete": 600, "partial": 0, "absent": 0}, "qwen35-9b": {"expected": 600, "complete": 600, "partial": 0, "absent": 0}}
- all selected items have complete five-condition rows in all five models

