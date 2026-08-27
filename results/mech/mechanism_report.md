# Mechanism — Qwen3-8B (legal_judgment + evidence_inference)

75 of 75 items have usable leverage under the fixed-position readout.
REI: 0 = as if the evidence had never been seen, 1 = used as if admitted.

REI exclude_pre   +0.463 [+0.269,+0.654]
REI exclude_post  +0.320 [+0.147,+0.482]
pre - post        +0.143 [+0.051,+0.242] p=0.0016

## C. Evidence-span causal gate
Every query position downstream of the evidence is blocked from attending to it.
  exclude_pre   n=75  REI ungated +0.463 -> gated -0.116 [-0.241,+0.006]   removed +0.579 [+0.437,+0.744] p=0.0000
  exclude_post  n=75  REI ungated +0.320 -> gated -0.081 [-0.223,+0.060]   removed +0.401 [+0.307,+0.500] p=0.0000

## A. Attention at the answer position (mean over heads, summed over span)
Reported per span and normalised per token, since the spans differ in length.
  layer band    evidence pre  evidence post   rule pre  rule post
  0-8                0.00139        0.00116    0.00079    0.00089
  9-17               0.00082        0.00051    0.00064    0.00086
  18-26              0.00132        0.00096    0.00059    0.00094
  27-35              0.00012        0.00010    0.00011    0.00013

  per-token attention ratio rule:evidence, exclude_pre   median 0.55 [0.51,0.71]
  per-token attention ratio rule:evidence, exclude_post  median 0.94 [0.88,1.15]

## B. Answer-position patching (Post -> Pre), recovery toward Post
1.0 = the patched run answers like exclude_post; 0.0 = like exclude_pre.
  n=59 items with |post-pre| >= 2 points
  L00=-0.00  L01=-0.00  L02=-0.00  L03=+0.00  L04=-0.00  L05=+0.00
  L06=+0.00  L07=-0.00  L08=-0.00  L09=-0.00  L10=+0.00  L11=+0.00
  L12=-0.00  L13=-0.00  L14=-0.00  L15=-0.00  L16=-0.01  L17=-0.05
  L18=+0.01  L19=+0.15  L20=+0.36  L21=+0.45  L22=+0.56  L23=+0.73
  L24=+0.72  L25=+0.72  L26=+0.79  L27=+0.84  L28=+0.86  L29=+0.87
  L30=+0.86  L31=+0.86  L32=+0.86  L33=+0.86  L34=+0.89  L35=+1.00
  median layer at which patching first recovers >=50% of the gap: 21 / 36
