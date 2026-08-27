# G0 results — qwen3-8b

REI: 0 = ignored the excluded evidence, 1 = used it as if admitted.
Winsorised at +/-3; CIs are 10,000-resample item-level paired bootstraps.

## Pooled
ALL   n=144/144  median|L|=31.0
    RuleAcc  exclude-pre 0.997  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.451 [+0.342,+0.563] p=0.0000
    REI_post  +0.119 [+0.023,+0.211] p=0.0154
    d_time    -0.319 [-0.430,-0.212] p=0.0000   items with post>pre: 0.30
    UTB_norm  -0.347 [-0.465,-0.224] p=0.0000
    items with REI_post>0.2: 0.43

## By task family
evidence_inference   n=30/30  median|L|=41.0
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.508 [+0.378,+0.636] p=0.0000
    REI_post  +0.098 [+0.016,+0.186] p=0.0174
    d_time    -0.410 [-0.542,-0.276] p=0.0000   items with post>pre: 0.23
    UTB_norm  -0.590 [-0.738,-0.446] p=0.0000
    items with REI_post>0.2: 0.33

legal_judgment   n=45/45  median|L|=29.2
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.526 [+0.286,+0.760] p=0.0000
    REI_post  +0.245 [+0.013,+0.482] p=0.0390
    d_time    -0.281 [-0.447,-0.110] p=0.0012   items with post>pre: 0.27
    UTB_norm  -0.319 [-0.489,-0.141] p=0.0004
    items with REI_post>0.2: 0.53

numeric_aggregation   n=21/21  median|L|=6.1
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.190 [-0.072,+0.535] p=0.2160
    REI_post  -0.073 [-0.280,+0.063] p=0.4680
    d_time    -0.177 [-0.529,+0.089] p=0.2608   items with post>pre: 0.19
    UTB_norm  -0.039 [-0.480,+0.358] p=0.8876
    items with REI_post>0.2: 0.10

outcome_evaluation   n=21/21  median|L|=21.1
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.392 [+0.197,+0.574] p=0.0002
    REI_post  +0.399 [+0.240,+0.535] p=0.0000
    d_time    +0.007 [-0.156,+0.165] p=0.9116   items with post>pre: 0.57
    UTB_norm  -0.083 [-0.275,+0.129] p=0.4182
    items with REI_post>0.2: 0.76

ranking_selection   n=27/27  median|L|=33.2
    RuleAcc  exclude-pre 0.981  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.511 [+0.206,+0.777] p=0.0014
    REI_post  -0.136 [-0.336,+0.054] p=0.1708
    d_time    -0.647 [-0.988,-0.275] p=0.0008   items with post>pre: 0.30
    UTB_norm  -0.569 [-0.916,-0.200] p=0.0024
    items with REI_post>0.2: 0.37

## By exclusion reason
access_control   n=34/34  median|L|=32.4
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.404 [+0.207,+0.595] p=0.0004
    REI_post  +0.136 [-0.001,+0.270] p=0.0528
    d_time    -0.267 [-0.436,-0.100] p=0.0016   items with post>pre: 0.26
    UTB_norm  -0.259 [-0.444,-0.075] p=0.0072
    items with REI_post>0.2: 0.44

epistemic_invalidation   n=44/44  median|L|=26.1
    RuleAcc  exclude-pre 0.989  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.629 [+0.360,+0.889] p=0.0000
    REI_post  -0.074 [-0.283,+0.118] p=0.4954
    d_time    -0.663 [-0.877,-0.458] p=0.0000   items with post>pre: 0.14
    UTB_norm  -0.669 [-0.897,-0.440] p=0.0000
    items with REI_post>0.2: 0.30

procedural_illegality   n=18/18  median|L|=32.2
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.376 [+0.117,+0.639] p=0.0046
    REI_post  +0.236 [-0.065,+0.614] p=0.1534
    d_time    -0.139 [-0.445,+0.177] p=0.3782   items with post>pre: 0.39
    UTB_norm  -0.123 [-0.428,+0.196] p=0.4434
    items with REI_post>0.2: 0.33

procedural_policy   n=20/20  median|L|=41.0
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.291 [-0.005,+0.526] p=0.0556
    REI_post  +0.033 [-0.173,+0.221] p=0.7160
    d_time    -0.258 [-0.593,+0.092] p=0.1520   items with post>pre: 0.40
    UTB_norm  -0.415 [-0.775,-0.021] p=0.0466
    items with REI_post>0.2: 0.45

temporal_irrelevance   n=26/26  median|L|=19.1
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.333 [+0.168,+0.491] p=0.0000
    REI_post  +0.331 [+0.195,+0.458] p=0.0000
    d_time    -0.002 [-0.133,+0.128] p=0.9722   items with post>pre: 0.46
    UTB_norm  -0.029 [-0.220,+0.184] p=0.7484
    items with REI_post>0.2: 0.65

## True-but-forbidden vs false-or-unreliable
false_or_unreliable   n=44/44  median|L|=26.1
    RuleAcc  exclude-pre 0.989  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.629 [+0.360,+0.889] p=0.0000
    REI_post  -0.074 [-0.283,+0.118] p=0.4954
    d_time    -0.663 [-0.877,-0.458] p=0.0000   items with post>pre: 0.14
    UTB_norm  -0.669 [-0.897,-0.440] p=0.0000
    items with REI_post>0.2: 0.30

true_but_forbidden   n=100/100  median|L|=31.7
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.372 [+0.263,+0.477] p=0.0000
    REI_post  +0.204 [+0.108,+0.307] p=0.0000
    d_time    -0.168 [-0.282,-0.051] p=0.0042   items with post>pre: 0.37
    UTB_norm  -0.205 [-0.333,-0.074] p=0.0026
    items with REI_post>0.2: 0.49

