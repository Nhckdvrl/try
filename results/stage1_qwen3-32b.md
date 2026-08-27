# Stage-1 follow-ups — qwen3-32b

REI: 0 = decided as if the evidence had never been seen, 1 = used it fully.

condition                   n            REI mean [95% CI]
exclude_pre               143       +0.215 [+0.086,+0.342]
exclude_pre_repeat        143       -0.026 [-0.126,+0.068]
exclude_post              143       -0.092 [-0.191,-0.002]
exclude_post_reencode     143       -0.110 [-0.211,-0.015]
ledger                    143       -0.079 [-0.173,+0.006]
sanitation                143       -0.062 [-0.130,-0.003]
admit_pre                 143       +0.949 [+0.879,+0.998]
admit_post                143       +1.037 [+1.002,+1.081]
admit_pre_repeat          143       +1.081 [+1.027,+1.141]

Paired contrasts (positive = the first condition leaks more):
  exclude_pre - exclude_pre_repeat       +0.241 [+0.144,+0.346] p=0.0000   (does repeating the rule after the evidence rescue Pre?)
  exclude_pre - exclude_post             +0.307 [+0.204,+0.424] p=0.0000   (the temporal asymmetry itself)
  exclude_post - exclude_post_reencode    +0.017 [-0.044,+0.074] p=0.5548   (does restating E as excluded help Post?)
  exclude_pre - ledger                   +0.293 [+0.189,+0.409] p=0.0000   (Pre vs structured evidence ledger)
  exclude_post - ledger                   -0.014 [-0.062,+0.033] p=0.5520   (Post vs structured evidence ledger)
  exclude_pre - sanitation               +0.277 [+0.153,+0.401] p=0.0000   (Pre vs full context sanitation)
  admit_pre - admit_pre_repeat         -0.132 [-0.248,-0.042] p=0.0010   (order control: repeating an ADMIT rule)
