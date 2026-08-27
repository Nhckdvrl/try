# Stage-1 follow-ups — qwen3-14b

REI: 0 = decided as if the evidence had never been seen, 1 = used it fully.

condition                   n            REI mean [95% CI]
exclude_pre               143       +0.485 [+0.371,+0.594]
exclude_pre_repeat        143       +0.100 [+0.003,+0.196]
exclude_post              143       -0.068 [-0.189,+0.041]
exclude_post_reencode     143       -0.021 [-0.127,+0.083]
ledger                    143       -0.030 [-0.133,+0.069]
sanitation                143       -0.098 [-0.196,-0.013]
admit_pre                 143       +1.022 [+0.986,+1.055]
admit_post                143       +0.978 [+0.944,+1.014]
admit_pre_repeat          143       +1.087 [+1.029,+1.149]

Paired contrasts (positive = the first condition leaks more):
  exclude_pre - exclude_pre_repeat       +0.385 [+0.279,+0.483] p=0.0000   (does repeating the rule after the evidence rescue Pre?)
  exclude_pre - exclude_post             +0.553 [+0.450,+0.674] p=0.0000   (the temporal asymmetry itself)
  exclude_post - exclude_post_reencode    -0.047 [-0.121,+0.017] p=0.1572   (does restating E as excluded help Post?)
  exclude_pre - ledger                   +0.515 [+0.421,+0.611] p=0.0000   (Pre vs structured evidence ledger)
  exclude_post - ledger                   -0.038 [-0.162,+0.070] p=0.5238   (Post vs structured evidence ledger)
  exclude_pre - sanitation               +0.584 [+0.440,+0.732] p=0.0000   (Pre vs full context sanitation)
  admit_pre - admit_pre_repeat         -0.064 [-0.137,+0.002] p=0.0628   (order control: repeating an ADMIT rule)
