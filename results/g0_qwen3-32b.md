# G0 results — qwen3-32b

REI: 0 = ignored the excluded evidence, 1 = used it as if admitted.
Winsorised at +/-3; CIs are 10,000-resample item-level paired bootstraps.

## Pooled
ALL   n=143/144  median|L|=29.5
    RuleAcc  exclude-pre 0.861  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.215 [+0.085,+0.343] p=0.0012
    REI_post  -0.092 [-0.189,-0.004] p=0.0432
    d_time    -0.288 [-0.390,-0.193] p=0.0000   items with post>pre: 0.23
    UTB_norm  -0.364 [-0.479,-0.254] p=0.0000
    items with REI_post>0.2: 0.23

## By task family
evidence_inference   n=30/30  median|L|=33.0
    RuleAcc  exclude-pre 0.945  exclude-post 0.999  (admit-control p(YES) 1.000)
    REI_pre   +0.247 [+0.108,+0.390] p=0.0000
    REI_post  -0.100 [-0.187,-0.025] p=0.0078
    d_time    -0.347 [-0.469,-0.232] p=0.0000   items with post>pre: 0.17
    UTB_norm  -0.381 [-0.522,-0.255] p=0.0000
    items with REI_post>0.2: 0.03

legal_judgment   n=45/45  median|L|=30.3
    RuleAcc  exclude-pre 0.920  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.416 [+0.226,+0.602] p=0.0000
    REI_post  +0.078 [-0.043,+0.204] p=0.2268
    d_time    -0.337 [-0.465,-0.212] p=0.0000   items with post>pre: 0.20
    UTB_norm  -0.382 [-0.527,-0.237] p=0.0000
    items with REI_post>0.2: 0.38

numeric_aggregation   n=21/21  median|L|=6.1
    RuleAcc  exclude-pre 0.734  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.210 [+0.019,+0.506] p=0.0128
    REI_post  +0.011 [-0.175,+0.149] p=0.8188
    d_time    -0.142 [-0.442,+0.026] p=0.3930   items with post>pre: 0.10
    UTB_norm  -0.232 [-0.594,+0.023] p=0.1410
    items with REI_post>0.2: 0.14

outcome_evaluation   n=20/21  median|L|=30.2
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.008 [-0.404,+0.319] p=0.8758
    REI_post  -0.117 [-0.528,+0.202] p=0.5668
    d_time    -0.080 [-0.259,+0.108] p=0.3932   items with post>pre: 0.45
    UTB_norm  -0.503 [-0.876,-0.182] p=0.0008
    items with REI_post>0.2: 0.40

ranking_selection   n=27/27  median|L|=27.0
    RuleAcc  exclude-pre 0.667  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.001 [-0.481,+0.445] p=1.0000
    REI_post  -0.430 [-0.733,-0.164] p=0.0006
    d_time    -0.405 [-0.771,-0.038] p=0.0288   items with post>pre: 0.30
    UTB_norm  -0.311 [-0.692,+0.055] p=0.0892
    items with REI_post>0.2: 0.15

## By exclusion reason
access_control   n=34/34  median|L|=28.0
    RuleAcc  exclude-pre 0.993  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.174 [-0.110,+0.418] p=0.2100
    REI_post  -0.105 [-0.334,+0.079] p=0.3288
    d_time    -0.278 [-0.448,-0.109] p=0.0002   items with post>pre: 0.18
    UTB_norm  -0.241 [-0.440,-0.050] p=0.0128
    items with REI_post>0.2: 0.21

epistemic_invalidation   n=44/44  median|L|=24.8
    RuleAcc  exclude-pre 0.555  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.625 [+0.409,+0.854] p=0.0000
    REI_post  -0.032 [-0.181,+0.110] p=0.6746
    d_time    -0.615 [-0.847,-0.407] p=0.0000   items with post>pre: 0.14
    UTB_norm  -0.677 [-0.891,-0.477] p=0.0000
    items with REI_post>0.2: 0.25

procedural_illegality   n=18/18  median|L|=37.1
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.071 [-0.118,+0.235] p=0.4262
    REI_post  -0.086 [-0.240,+0.052] p=0.2272
    d_time    -0.156 [-0.259,-0.066] p=0.0002   items with post>pre: 0.22
    UTB_norm  -0.206 [-0.333,-0.087] p=0.0002
    items with REI_post>0.2: 0.22

procedural_policy   n=20/20  median|L|=32.6
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   -0.292 [-0.642,+0.023] p=0.0684
    REI_post  -0.278 [-0.526,-0.077] p=0.0040
    d_time    +0.015 [-0.188,+0.241] p=0.9426   items with post>pre: 0.40
    UTB_norm  +0.035 [-0.179,+0.272] p=0.7738
    items with REI_post>0.2: 0.05

temporal_irrelevance   n=25/26  median|L|=23.5
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.010 [-0.311,+0.251] p=0.8638
    REI_post  -0.090 [-0.416,+0.164] p=0.5802
    d_time    -0.064 [-0.214,+0.089] p=0.3990   items with post>pre: 0.36
    UTB_norm  -0.479 [-0.822,-0.191] p=0.0000
    items with REI_post>0.2: 0.32

## True-but-forbidden vs false-or-unreliable
false_or_unreliable   n=44/44  median|L|=24.8
    RuleAcc  exclude-pre 0.555  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.625 [+0.409,+0.854] p=0.0000
    REI_post  -0.032 [-0.181,+0.110] p=0.6746
    d_time    -0.615 [-0.847,-0.407] p=0.0000   items with post>pre: 0.14
    UTB_norm  -0.677 [-0.891,-0.477] p=0.0000
    items with REI_post>0.2: 0.25

true_but_forbidden   n=99/100  median|L|=32.0
    RuleAcc  exclude-pre 0.998  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.032 [-0.121,+0.169] p=0.6488
    REI_post  -0.119 [-0.245,-0.009] p=0.0374
    d_time    -0.142 [-0.230,-0.053] p=0.0008   items with post>pre: 0.27
    UTB_norm  -0.224 [-0.348,-0.105] p=0.0000
    items with REI_post>0.2: 0.22

