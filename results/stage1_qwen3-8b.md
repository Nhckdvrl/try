# Stage-1 follow-ups — qwen3-8b

REI: 0 = decided as if the evidence had never been seen, 1 = used it fully.

condition                   n            REI mean [95% CI]
exclude_pre               144       +0.451 [+0.341,+0.561]
exclude_pre_repeat        144       +0.074 [-0.034,+0.182]
exclude_post              144       +0.119 [+0.025,+0.213]
exclude_post_reencode     144       +0.015 [-0.075,+0.101]
ledger                    144       -0.011 [-0.077,+0.055]
sanitation                144       -0.026 [-0.107,+0.050]
admit_pre                 144       +0.986 [+0.955,+1.017]
admit_post                144       +1.014 [+0.983,+1.045]
admit_pre_repeat          144       +1.013 [+0.957,+1.072]

Paired contrasts (positive = the first condition leaks more):
  exclude_pre - exclude_pre_repeat       +0.377 [+0.282,+0.471] p=0.0000   (does repeating the rule after the evidence rescue Pre?)
  exclude_pre - exclude_post             +0.332 [+0.217,+0.453] p=0.0000   (the temporal asymmetry itself)
  exclude_post - exclude_post_reencode    +0.104 [+0.045,+0.164] p=0.0006   (does restating E as excluded help Post?)
  exclude_pre - ledger                   +0.462 [+0.345,+0.580] p=0.0000   (Pre vs structured evidence ledger)
  exclude_post - ledger                   +0.130 [+0.049,+0.215] p=0.0020   (Post vs structured evidence ledger)
  exclude_pre - sanitation               +0.477 [+0.361,+0.591] p=0.0000   (Pre vs full context sanitation)
  admit_pre - admit_pre_repeat         -0.027 [-0.091,+0.037] p=0.4018   (order control: repeating an ADMIT rule)
