# Stage-1 follow-ups — qwen3-4b

REI: 0 = decided as if the evidence had never been seen, 1 = used it fully.

condition                   n            REI mean [95% CI]
exclude_pre               137       +0.582 [+0.408,+0.747]
exclude_pre_repeat        137       +0.117 [-0.055,+0.284]
exclude_post              137       +0.142 [-0.031,+0.304]
exclude_post_reencode     137       +0.108 [-0.059,+0.267]
ledger                    137       +0.121 [-0.019,+0.261]
sanitation                137       -0.162 [-0.286,-0.045]
admit_pre                 137       +0.971 [+0.878,+1.056]
admit_post                137       +1.007 [+0.916,+1.090]
admit_pre_repeat          137       +1.017 [+0.883,+1.145]

Paired contrasts (positive = the first condition leaks more):
  exclude_pre - exclude_pre_repeat       +0.465 [+0.321,+0.609] p=0.0000   (does repeating the rule after the evidence rescue Pre?)
  exclude_pre - exclude_post             +0.440 [+0.269,+0.611] p=0.0000   (the temporal asymmetry itself)
  exclude_post - exclude_post_reencode    +0.034 [-0.071,+0.150] p=0.5490   (does restating E as excluded help Post?)
  exclude_pre - ledger                   +0.461 [+0.278,+0.639] p=0.0000   (Pre vs structured evidence ledger)
  exclude_post - ledger                   +0.021 [-0.129,+0.149] p=0.7514   (Post vs structured evidence ledger)
  exclude_pre - sanitation               +0.743 [+0.531,+0.962] p=0.0000   (Pre vs full context sanitation)
  admit_pre - admit_pre_repeat         -0.046 [-0.176,+0.099] p=0.5056   (order control: repeating an ADMIT rule)
