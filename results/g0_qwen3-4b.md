# G0 results — qwen3-4b

REI: 0 = ignored the excluded evidence, 1 = used it as if admitted.
Winsorised at +/-3; CIs are 10,000-resample item-level paired bootstraps.

## Pooled
ALL   n=137/144  median|L|=24.2
    RuleAcc  exclude-pre 0.942  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.582 [+0.408,+0.747] p=0.0000
    REI_post  +0.142 [-0.022,+0.305] p=0.0966
    d_time    -0.390 [-0.560,-0.222] p=0.0000   items with post>pre: 0.23
    UTB_norm  -0.375 [-0.559,-0.181] p=0.0002
    items with REI_post>0.2: 0.49

## By task family
evidence_inference   n=30/30  median|L|=36.7
    RuleAcc  exclude-pre 0.933  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.653 [+0.558,+0.743] p=0.0000
    REI_post  +0.109 [-0.076,+0.277] p=0.2242
    d_time    -0.543 [-0.749,-0.361] p=0.0000   items with post>pre: 0.07
    UTB_norm  -0.641 [-0.896,-0.423] p=0.0000
    items with REI_post>0.2: 0.47

legal_judgment   n=40/45  median|L|=19.7
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.452 [+0.042,+0.810] p=0.0340
    REI_post  +0.052 [-0.379,+0.448] p=0.7846
    d_time    -0.347 [-0.653,-0.039] p=0.0218   items with post>pre: 0.30
    UTB_norm  -0.241 [-0.607,+0.121] p=0.1968
    items with REI_post>0.2: 0.60

numeric_aggregation   n=21/21  median|L|=5.7
    RuleAcc  exclude-pre 0.955  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.484 [+0.071,+0.826] p=0.0212
    REI_post  -0.073 [-0.406,+0.137] p=0.7244
    d_time    -0.671 [-1.017,-0.362] p=0.0000   items with post>pre: 0.14
    UTB_norm  -0.683 [-1.039,-0.344] p=0.0002
    items with REI_post>0.2: 0.19

outcome_evaluation   n=20/21  median|L|=28.4
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.823 [+0.509,+1.151] p=0.0000
    REI_post  +0.426 [+0.273,+0.583] p=0.0000
    d_time    -0.397 [-0.761,-0.084] p=0.0116   items with post>pre: 0.20
    UTB_norm  -0.345 [-0.805,+0.132] p=0.1356
    items with REI_post>0.2: 0.65

ranking_selection   n=26/27  median|L|=28.1
    RuleAcc  exclude-pre 0.808  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.594 [+0.059,+1.104] p=0.0296
    REI_post  +0.271 [-0.204,+0.751] p=0.2632
    d_time    -0.049 [-0.637,+0.558] p=0.8632   items with post>pre: 0.42
    UTB_norm  -0.051 [-0.656,+0.567] p=0.8788
    items with REI_post>0.2: 0.46

## By exclusion reason
access_control   n=33/34  median|L|=32.3
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.954 [+0.637,+1.241] p=0.0000
    REI_post  +0.275 [-0.025,+0.559] p=0.0736
    d_time    -0.661 [-0.980,-0.318] p=0.0000   items with post>pre: 0.12
    UTB_norm  -0.459 [-0.795,-0.088] p=0.0186
    items with REI_post>0.2: 0.58

epistemic_invalidation   n=41/44  median|L|=24.2
    RuleAcc  exclude-pre 0.806  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.519 [+0.154,+0.842] p=0.0076
    REI_post  -0.097 [-0.446,+0.229] p=0.5884
    d_time    -0.493 [-0.838,-0.138] p=0.0088   items with post>pre: 0.20
    UTB_norm  -0.678 [-1.029,-0.310] p=0.0006
    items with REI_post>0.2: 0.44

procedural_illegality   n=16/18  median|L|=18.4
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.028 [-0.656,+0.584] p=0.8872
    REI_post  -0.169 [-0.899,+0.545] p=0.6570
    d_time    -0.190 [-0.761,+0.389] p=0.5046   items with post>pre: 0.44
    UTB_norm  +0.001 [-0.658,+0.683] p=1.0000
    items with REI_post>0.2: 0.38

procedural_policy   n=20/20  median|L|=33.5
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.295 [-0.081,+0.630] p=0.1274
    REI_post  +0.306 [-0.028,+0.686] p=0.0798
    d_time    +0.064 [-0.258,+0.473] p=0.8042   items with post>pre: 0.35
    UTB_norm  -0.118 [-0.539,+0.348] p=0.6026
    items with REI_post>0.2: 0.45

temporal_irrelevance   n=25/26  median|L|=22.2
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.737 [+0.469,+1.016] p=0.0000
    REI_post  +0.344 [+0.212,+0.486] p=0.0000
    d_time    -0.393 [-0.692,-0.134] p=0.0026   items with post>pre: 0.20
    UTB_norm  -0.342 [-0.717,+0.040] p=0.0738
    items with REI_post>0.2: 0.52

## True-but-forbidden vs false-or-unreliable
false_or_unreliable   n=41/44  median|L|=24.2
    RuleAcc  exclude-pre 0.806  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.519 [+0.154,+0.842] p=0.0076
    REI_post  -0.097 [-0.446,+0.229] p=0.5884
    d_time    -0.493 [-0.838,-0.138] p=0.0088   items with post>pre: 0.20
    UTB_norm  -0.678 [-1.029,-0.310] p=0.0006
    items with REI_post>0.2: 0.44

true_but_forbidden   n=96/100  median|L|=24.3
    RuleAcc  exclude-pre 1.000  exclude-post 1.000  (admit-control p(YES) 1.000)
    REI_pre   +0.608 [+0.410,+0.792] p=0.0000
    REI_post  +0.244 [+0.059,+0.421] p=0.0132
    d_time    -0.347 [-0.539,-0.151] p=0.0008   items with post>pre: 0.25
    UTB_norm  -0.246 [-0.467,-0.025] p=0.0346
    items with REI_post>0.2: 0.51

