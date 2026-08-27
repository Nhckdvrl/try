# P0.5 Semantic addressability

Structure: `preview(E') -> rule: E7 has weight 0 -> EVIDENCE E7 (fixed) -> judgment`.
Only the preview changes. Rescue is how much of the no-preview failure the preview
removes; large rescue means that preview was enough for the rule to bind.

# qwen3-8b   (n usable = 75)

| preview placed before the rule | REI | rescue vs no preview | p |
|---|---|---|---|
| no preview (the failure) | +0.566 | — | — |
| exact same text | +0.243 | **+0.323** [+0.157, +0.480] | 0.0000 |
| lexical paraphrase, same proposition | +0.255 | **+0.310** [+0.187, +0.451] | 0.0000 |
| entailing summary, no verbatim content | +0.601 | **-0.035** [-0.144, +0.067] | 0.4945 |
| different fact, same entity and same direction | +0.836 | **-0.270** [-0.464, -0.104] | 0.0010 |
| high lexical overlap, different meaning | +0.509 | **+0.057** [-0.058, +0.173] | 0.3310 |
| same case, unrelated procedural fact | +0.613 | **-0.047** [-0.133, +0.037] | 0.2990 |
| unrelated fact | +0.550 | **+0.016** [-0.075, +0.111] | 0.7535 |

## Content x identity (legal items only)

Preview is always the original evidence. The rule always names E7. The item the decision reads varies in content and in label.

| preview content matches? | label matches the rule? | REI |
|---|---|---|
| yes | yes (E7) | +0.480 [+0.330, +0.646]  (n=45) |
| yes | no (E9) | +0.637 [+0.527, +0.766]  (n=44) |
| no | yes (E7) | +0.739 [+0.656, +0.819]  (n=45) |
| no | no (E9) | +0.920 [+0.815, +1.064]  (n=45) |

# gemma3-12b   (n usable = 74)

| preview placed before the rule | REI | rescue vs no preview | p |
|---|---|---|---|
| no preview (the failure) | +0.451 | — | — |
| exact same text | +0.327 | **+0.124** [-0.008, +0.250] | 0.0650 |
| lexical paraphrase, same proposition | +0.343 | **+0.108** [-0.030, +0.239] | 0.1250 |
| entailing summary, no verbatim content | +0.694 | **-0.243** [-0.426, -0.087] | 0.0000 |
| different fact, same entity and same direction | +0.985 | **-0.534** [-0.816, -0.290] | 0.0000 |
| high lexical overlap, different meaning | +0.629 | **-0.177** [-0.310, -0.052] | 0.0055 |
| same case, unrelated procedural fact | +0.520 | **-0.069** [-0.143, -0.003] | 0.0410 |
| unrelated fact | +0.438 | **+0.014** [-0.068, +0.109] | 0.8445 |

## Content x identity (legal items only)

Preview is always the original evidence. The rule always names E7. The item the decision reads varies in content and in label.

| preview content matches? | label matches the rule? | REI |
|---|---|---|
| yes | yes (E7) | +0.492 [+0.254, +0.687]  (n=45) |
| yes | no (E9) | +0.669 [+0.559, +0.764]  (n=44) |
| no | yes (E7) | +0.856 [+0.767, +0.947]  (n=45) |
| no | no (E9) | +0.944 [+0.917, +0.975]  (n=45) |

# phi4-mini   (n usable = 73)

| preview placed before the rule | REI | rescue vs no preview | p |
|---|---|---|---|
| no preview (the failure) | +0.677 | — | — |
| exact same text | +0.534 | **+0.143** [-0.082, +0.388] | 0.2250 |
| lexical paraphrase, same proposition | +0.460 | **+0.217** [+0.071, +0.366] | 0.0015 |
| entailing summary, no verbatim content | +0.754 | **-0.077** [-0.224, +0.065] | 0.2820 |
| different fact, same entity and same direction | +0.949 | **-0.271** [-0.466, -0.087] | 0.0040 |
| high lexical overlap, different meaning | +0.599 | **+0.078** [-0.083, +0.243] | 0.3425 |
| same case, unrelated procedural fact | +0.652 | **+0.025** [-0.102, +0.150] | 0.6620 |
| unrelated fact | +0.671 | **+0.006** [-0.106, +0.110] | 0.9150 |

## Content x identity (legal items only)

Preview is always the original evidence. The rule always names E7. The item the decision reads varies in content and in label.

| preview content matches? | label matches the rule? | REI |
|---|---|---|
| yes | yes (E7) | +0.505 [+0.301, +0.695]  (n=44) |
| yes | no (E9) | +0.533 [+0.359, +0.672]  (n=44) |
| no | yes (E7) | +0.839 [+0.747, +0.922]  (n=44) |
| no | no (E9) | +0.882 [+0.820, +0.944]  (n=45) |

# qwen3.5-27b   (n usable = 74)

| preview placed before the rule | REI | rescue vs no preview | p |
|---|---|---|---|
| no preview (the failure) | +0.156 | — | — |
| exact same text | -0.385 | **+0.541** [+0.351, +0.759] | 0.0000 |
| lexical paraphrase, same proposition | -0.383 | **+0.540** [+0.328, +0.791] | 0.0000 |
| entailing summary, no verbatim content | -0.058 | **+0.214** [+0.069, +0.371] | 0.0045 |
| different fact, same entity and same direction | +0.486 | **-0.330** [-0.672, -0.088] | 0.0005 |
| high lexical overlap, different meaning | +0.221 | **-0.064** [-0.280, +0.136] | 0.5485 |
| same case, unrelated procedural fact | -0.055 | **+0.211** [+0.028, +0.425] | 0.0170 |
| unrelated fact | +0.034 | **+0.123** [-0.003, +0.280] | 0.0535 |

## Content x identity (legal items only)

Preview is always the original evidence. The rule always names E7. The item the decision reads varies in content and in label.

| preview content matches? | label matches the rule? | REI |
|---|---|---|
| yes | yes (E7) | -0.463 [-0.731, -0.176]  (n=45) |
| yes | no (E9) | +0.068 [-0.328, +0.465]  (n=44) |
| no | yes (E7) | +0.490 [+0.265, +0.719]  (n=45) |
| no | no (E9) | +0.961 [+0.905, +1.002]  (n=45) |
