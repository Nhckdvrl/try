# G0 results — qwen3-14b

REI: 0 = ignored the excluded evidence, 1 = used it as if admitted.
Winsorised at +/-3; CIs are 10,000-resample item-level paired bootstraps.

## Pooled
ALL   n=143/144  median|L|=28.2
    RuleAcc  exclude-pre 0.874  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.485 [+0.370,+0.595] p=0.0000
    REI_post  -0.068 [-0.188,+0.042] p=0.2526
    d_time    -0.555 [-0.651,-0.463] p=0.0000   items with post>pre: 0.08
    UTB_norm  -0.492 [-0.607,-0.378] p=0.0000
    items with REI_post>0.2: 0.37

## By task family
evidence_inference   n=30/30  median|L|=32.2
    RuleAcc  exclude-pre 0.796  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.550 [+0.449,+0.649] p=0.0000
    REI_post  -0.003 [-0.139,+0.123] p=0.9926
    d_time    -0.553 [-0.663,-0.440] p=0.0000   items with post>pre: 0.03
    UTB_norm  -0.543 [-0.659,-0.424] p=0.0000
    items with REI_post>0.2: 0.37

legal_judgment   n=44/45  median|L|=33.3
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.297 [+0.022,+0.573] p=0.0376
    REI_post  -0.345 [-0.627,-0.083] p=0.0080
    d_time    -0.613 [-0.822,-0.419] p=0.0000   items with post>pre: 0.09
    UTB_norm  -0.678 [-0.910,-0.459] p=0.0000
    items with REI_post>0.2: 0.30

numeric_aggregation   n=21/21  median|L|=5.9
    RuleAcc  exclude-pre 0.857  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.130 [-0.021,+0.345] p=0.1358
    REI_post  -0.025 [-0.137,+0.071] p=0.6804
    d_time    -0.155 [-0.421,+0.057] p=0.1892   items with post>pre: 0.24
    UTB_norm  +0.085 [-0.285,+0.484] p=0.6766
    items with REI_post>0.2: 0.14

outcome_evaluation   n=21/21  median|L|=21.8
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.565 [+0.203,+0.781] p=0.0048
    REI_post  +0.294 [-0.087,+0.543] p=0.1264
    d_time    -0.341 [-0.535,-0.199] p=0.0000   items with post>pre: 0.05
    UTB_norm  -0.201 [-0.450,-0.009] p=0.0388
    items with REI_post>0.2: 0.81

ranking_selection   n=27/27  median|L|=42.4
    RuleAcc  exclude-pre 0.670  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.934 [+0.864,+0.998] p=0.0000
    REI_post  -0.005 [-0.197,+0.174] p=0.9766
    d_time    -0.939 [-1.115,-0.772] p=0.0000   items with post>pre: 0.00
    UTB_norm  -0.807 [-0.973,-0.647] p=0.0000
    items with REI_post>0.2: 0.33

## By exclusion reason
access_control   n=34/34  median|L|=28.0
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.601 [+0.421,+0.814] p=0.0000
    REI_post  -0.092 [-0.338,+0.102] p=0.4290
    d_time    -0.605 [-0.853,-0.377] p=0.0000   items with post>pre: 0.09
    UTB_norm  -0.528 [-0.805,-0.256] p=0.0000
    items with REI_post>0.2: 0.32

epistemic_invalidation   n=43/44  median|L|=28.9
    RuleAcc  exclude-pre 0.581  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.621 [+0.395,+0.828] p=0.0000
    REI_post  -0.098 [-0.274,+0.066] p=0.2668
    d_time    -0.718 [-0.865,-0.575] p=0.0000   items with post>pre: 0.02
    UTB_norm  -0.683 [-0.863,-0.473] p=0.0000
    items with REI_post>0.2: 0.30

procedural_illegality   n=18/18  median|L|=33.3
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   -0.103 [-0.489,+0.211] p=0.5922
    REI_post  -0.635 [-1.067,-0.279] p=0.0000
    d_time    -0.627 [-0.961,-0.356] p=0.0000   items with post>pre: 0.11
    UTB_norm  -0.660 [-1.081,-0.289] p=0.0000
    items with REI_post>0.2: 0.00

procedural_policy   n=20/20  median|L|=34.7
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.609 [+0.457,+0.754] p=0.0000
    REI_post  +0.060 [-0.143,+0.253] p=0.5350
    d_time    -0.548 [-0.672,-0.422] p=0.0000   items with post>pre: 0.00
    UTB_norm  -0.458 [-0.580,-0.328] p=0.0000
    items with REI_post>0.2: 0.45

temporal_irrelevance   n=26/26  median|L|=17.4
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.457 [+0.156,+0.674] p=0.0052
    REI_post  +0.245 [-0.078,+0.463] p=0.1096
    d_time    -0.270 [-0.439,-0.143] p=0.0000   items with post>pre: 0.12
    UTB_norm  -0.133 [-0.337,+0.031] p=0.1340
    items with REI_post>0.2: 0.69

## True-but-forbidden vs false-or-unreliable
false_or_unreliable   n=43/44  median|L|=28.9
    RuleAcc  exclude-pre 0.581  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.621 [+0.395,+0.828] p=0.0000
    REI_post  -0.098 [-0.274,+0.066] p=0.2668
    d_time    -0.718 [-0.865,-0.575] p=0.0000   items with post>pre: 0.02
    UTB_norm  -0.683 [-0.863,-0.473] p=0.0000
    items with REI_post>0.2: 0.30

true_but_forbidden   n=100/100  median|L|=26.9
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.427 [+0.295,+0.553] p=0.0000
    REI_post  -0.055 [-0.207,+0.081] p=0.4584
    d_time    -0.484 [-0.608,-0.370] p=0.0000   items with post>pre: 0.10
    UTB_norm  -0.410 [-0.548,-0.273] p=0.0000
    items with REI_post>0.2: 0.40

