# Stage 3C — attacking the narrow claim


# qwen3-8b

## P0-1 Inclusion implicature (H-D)

Presentation policy at the top of the file; it never mentions the item, exclusion, or zero. Rule is always `weight = exactly 0%`.

| presentation policy | REI pre | REI post | pre - post |
|---|---|---|---|
| `none` (n=141) | +0.486 | +0.187 | **+0.299** [+0.161, +0.439] p=0.0000 |
| `auto` (n=136) | +0.379 | +0.242 | **+0.137** [+0.037, +0.235] p=0.0080 |
| `audit` (n=138) | +0.411 | +0.146 | **+0.265** [+0.123, +0.428] p=0.0005 |
| `relev` (n=138) | +0.383 | +0.138 | **+0.245** [+0.119, +0.382] p=0.0000 |

- Rescue from the audit policy, prospective arm (`none_pre` - `audit_pre`): **+0.089** [-0.019, +0.191] p=0.1015

## P0-3 State externalisation

| condition | REI pre | REI post | pre - post | stated weight (pre) |
|---|---|---|---|---|
| decision only | +0.485 | +0.184 | **+0.301** [+0.167, +0.434] p=0.0000 | — |
| model writes ITEM DECISION WEIGHT first | +0.425 | +0.296 | **+0.129** [+0.022, +0.227] p=0.0200 | 37.41% |
| weight teacher-forced to 0% | +0.434 | +0.357 | **+0.077** [-0.049, +0.185] p=0.2020 | 0.00% |

## P0-4 Identity predicate vs arbitrary-tag predicate

Both conditional, both locally checkable when the item arrives, tag `Z9` carries no semantics.

| predicate | REI pre | REI post | pre - post |
|---|---|---|---|
| `if ID is E7 -> weight 0` (n=142) | +0.717 | +0.644 | **+0.073** [-0.064, +0.204] p=0.2810 |
| `if tag is Z9 -> weight 0` (n=144) | +0.704 | +0.550 | **+0.154** [-0.006, +0.319] p=0.0615 |

## P1-7 Salience control: the same preview stubs with NO rule

Effective weight of the evidence when nothing forbids it. If previews raise this, the Stage-3A ladder result is salience, not binding.

- `sal_L0`: leverage-normalised weight +0.704
- `sal_L1`: leverage-normalised weight +0.700
- `sal_L2`: leverage-normalised weight +0.749
- `sal_L3`: leverage-normalised weight +0.763
- `sal_L4`: leverage-normalised weight +0.732

## P1-8 Occurrence vs content binding

- `E -> rule -> E again` (full content present when the rule is stated): REI +0.148
- reference: rule-first +0.485, rule-last +0.184

# gemma3-12b

## P0-1 Inclusion implicature (H-D)

Presentation policy at the top of the file; it never mentions the item, exclusion, or zero. Rule is always `weight = exactly 0%`.

| presentation policy | REI pre | REI post | pre - post |
|---|---|---|---|
| `none` (n=139) | +0.439 | +0.162 | **+0.277** [+0.095, +0.452] p=0.0035 |
| `auto` (n=139) | +0.399 | +0.163 | **+0.236** [+0.073, +0.401] p=0.0015 |
| `audit` (n=136) | +0.502 | +0.270 | **+0.233** [+0.078, +0.396] p=0.0025 |
| `relev` (n=137) | +0.471 | +0.163 | **+0.309** [+0.124, +0.492] p=0.0010 |

- Rescue from the audit policy, prospective arm (`none_pre` - `audit_pre`): **-0.033** [-0.151, +0.074] p=0.5425

## P0-3 State externalisation

| condition | REI pre | REI post | pre - post | stated weight (pre) |
|---|---|---|---|---|
| decision only | +0.447 | +0.154 | **+0.292** [+0.118, +0.465] p=0.0005 | — |
| model writes ITEM DECISION WEIGHT first | +0.632 | +0.198 | **+0.434** [+0.234, +0.619] p=0.0000 | 25.24% |
| weight teacher-forced to 0% | +0.540 | +0.121 | **+0.419** [+0.201, +0.621] p=0.0000 | 0.00% |

## P0-4 Identity predicate vs arbitrary-tag predicate

Both conditional, both locally checkable when the item arrives, tag `Z9` carries no semantics.

| predicate | REI pre | REI post | pre - post |
|---|---|---|---|
| `if ID is E7 -> weight 0` (n=141) | +0.789 | +0.840 | **-0.051** [-0.203, +0.094] p=0.5100 |
| `if tag is Z9 -> weight 0` (n=140) | +0.720 | +0.881 | **-0.161** [-0.400, +0.046] p=0.1330 |

## P1-7 Salience control: the same preview stubs with NO rule

Effective weight of the evidence when nothing forbids it. If previews raise this, the Stage-3A ladder result is salience, not binding.

- `sal_L0`: leverage-normalised weight +0.717
- `sal_L1`: leverage-normalised weight +0.698
- `sal_L2`: leverage-normalised weight +0.734
- `sal_L3`: leverage-normalised weight +0.794
- `sal_L4`: leverage-normalised weight +0.799

## P1-8 Occurrence vs content binding

- `E -> rule -> E again` (full content present when the rule is stated): REI +0.231
- reference: rule-first +0.447, rule-last +0.154

# phi4-mini

## P0-1 Inclusion implicature (H-D)

Presentation policy at the top of the file; it never mentions the item, exclusion, or zero. Rule is always `weight = exactly 0%`.

| presentation policy | REI pre | REI post | pre - post |
|---|---|---|---|
| `none` (n=131) | +0.642 | +0.312 | **+0.330** [+0.142, +0.538] p=0.0000 |
| `auto` (n=133) | +0.519 | +0.256 | **+0.264** [+0.121, +0.412] p=0.0000 |
| `audit` (n=133) | +0.553 | +0.327 | **+0.226** [+0.060, +0.386] p=0.0085 |
| `relev` (n=133) | +0.499 | +0.265 | **+0.234** [+0.081, +0.383] p=0.0025 |

- Rescue from the audit policy, prospective arm (`none_pre` - `audit_pre`): **+0.095** [-0.090, +0.280] p=0.3330

## P0-3 State externalisation

| condition | REI pre | REI post | pre - post | stated weight (pre) |
|---|---|---|---|---|
| decision only | +0.623 | +0.206 | **+0.417** [+0.223, +0.622] p=0.0000 | — |
| model writes ITEM DECISION WEIGHT first | +0.031 | -0.035 | **+0.055** [-0.101, +0.185] p=0.4385 | 10.46% |
| weight teacher-forced to 0% | +0.003 | -0.012 | **+0.015** [-0.064, +0.075] p=0.6160 | 0.00% |

## P0-4 Identity predicate vs arbitrary-tag predicate

Both conditional, both locally checkable when the item arrives, tag `Z9` carries no semantics.

| predicate | REI pre | REI post | pre - post |
|---|---|---|---|
| `if ID is E7 -> weight 0` (n=136) | +0.765 | +0.573 | **+0.192** [-0.076, +0.489] p=0.1635 |
| `if tag is Z9 -> weight 0` (n=136) | +0.689 | +0.749 | **-0.059** [-0.223, +0.087] p=0.4550 |

## P1-7 Salience control: the same preview stubs with NO rule

Effective weight of the evidence when nothing forbids it. If previews raise this, the Stage-3A ladder result is salience, not binding.

- `sal_L0`: leverage-normalised weight +0.761
- `sal_L1`: leverage-normalised weight +0.906
- `sal_L2`: leverage-normalised weight +0.768
- `sal_L3`: leverage-normalised weight +0.893
- `sal_L4`: leverage-normalised weight +0.881

## P1-8 Occurrence vs content binding

- `E -> rule -> E again` (full content present when the rule is stated): REI +0.487
- reference: rule-first +0.623, rule-last +0.206

# mistral-small-24b

## P0-1 Inclusion implicature (H-D)

Presentation policy at the top of the file; it never mentions the item, exclusion, or zero. Rule is always `weight = exactly 0%`.

| presentation policy | REI pre | REI post | pre - post |
|---|---|---|---|
| `none` (n=137) | +0.100 | +0.011 | **+0.090** [-0.019, +0.212] p=0.1125 |
| `auto` (n=136) | +0.061 | +0.088 | **-0.027** [-0.166, +0.101] p=0.7335 |
| `audit` (n=140) | -0.015 | -0.060 | **+0.045** [-0.038, +0.138] p=0.2795 |
| `relev` (n=137) | +0.093 | -0.031 | **+0.123** [+0.025, +0.235] p=0.0075 |

- Rescue from the audit policy, prospective arm (`none_pre` - `audit_pre`): **+0.131** [-0.023, +0.299] p=0.1055

## P0-3 State externalisation

| condition | REI pre | REI post | pre - post | stated weight (pre) |
|---|---|---|---|---|
| decision only | +0.078 | +0.005 | **+0.073** [-0.014, +0.157] p=0.0960 | — |
| model writes ITEM DECISION WEIGHT first | -0.017 | -0.103 | **+0.086** [+0.000, +0.168] p=0.0485 | 13.50% |
| weight teacher-forced to 0% | -0.071 | -0.178 | **+0.107** [+0.019, +0.204] p=0.0145 | 0.00% |

## P0-4 Identity predicate vs arbitrary-tag predicate

Both conditional, both locally checkable when the item arrives, tag `Z9` carries no semantics.

| predicate | REI pre | REI post | pre - post |
|---|---|---|---|
| `if ID is E7 -> weight 0` (n=137) | +0.073 | +0.412 | **-0.339** [-0.479, -0.198] p=0.0000 |
| `if tag is Z9 -> weight 0` (n=139) | +0.086 | +0.391 | **-0.304** [-0.470, -0.147] p=0.0000 |

## P1-7 Salience control: the same preview stubs with NO rule

Effective weight of the evidence when nothing forbids it. If previews raise this, the Stage-3A ladder result is salience, not binding.

- `sal_L0`: leverage-normalised weight +0.842
- `sal_L1`: leverage-normalised weight +0.841
- `sal_L2`: leverage-normalised weight +0.825
- `sal_L3`: leverage-normalised weight +0.905
- `sal_L4`: leverage-normalised weight +0.862

## P1-8 Occurrence vs content binding

- `E -> rule -> E again` (full content present when the rule is stated): REI -0.079
- reference: rule-first +0.078, rule-last +0.005

# qwen3.5-27b

## P0-1 Inclusion implicature (H-D)

Presentation policy at the top of the file; it never mentions the item, exclusion, or zero. Rule is always `weight = exactly 0%`.

| presentation policy | REI pre | REI post | pre - post |
|---|---|---|---|
| `none` (n=138) | -0.047 | -0.224 | **+0.177** [+0.057, +0.313] p=0.0025 |
| `auto` (n=135) | -0.162 | -0.358 | **+0.196** [+0.065, +0.341] p=0.0010 |
| `audit` (n=136) | -0.166 | -0.246 | **+0.080** [-0.048, +0.206] p=0.2130 |
| `relev` (n=138) | -0.140 | -0.313 | **+0.173** [+0.055, +0.299] p=0.0050 |

- Rescue from the audit policy, prospective arm (`none_pre` - `audit_pre`): **+0.145** [-0.006, +0.299] p=0.0590

## P0-3 State externalisation

| condition | REI pre | REI post | pre - post | stated weight (pre) |
|---|---|---|---|---|
| decision only | -0.054 | -0.267 | **+0.213** [+0.079, +0.366] p=0.0010 | — |
| model writes ITEM DECISION WEIGHT first | +0.034 | -0.157 | **+0.191** [+0.110, +0.274] p=0.0000 | 8.70% |
| weight teacher-forced to 0% | +0.031 | -0.150 | **+0.181** [+0.101, +0.264] p=0.0000 | 0.00% |

## P0-4 Identity predicate vs arbitrary-tag predicate

Both conditional, both locally checkable when the item arrives, tag `Z9` carries no semantics.

| predicate | REI pre | REI post | pre - post |
|---|---|---|---|
| `if ID is E7 -> weight 0` (n=132) | -0.264 | -0.143 | **-0.121** [-0.298, +0.039] p=0.1415 |
| `if tag is Z9 -> weight 0` (n=130) | -0.376 | -0.124 | **-0.253** [-0.391, -0.137] p=0.0000 |

## P1-7 Salience control: the same preview stubs with NO rule

Effective weight of the evidence when nothing forbids it. If previews raise this, the Stage-3A ladder result is salience, not binding.

- `sal_L0`: leverage-normalised weight +0.837
- `sal_L1`: leverage-normalised weight +0.726
- `sal_L2`: leverage-normalised weight +0.723
- `sal_L3`: leverage-normalised weight +0.763
- `sal_L4`: leverage-normalised weight +0.722

## P1-8 Occurrence vs content binding

- `E -> rule -> E again` (full content present when the rule is stated): REI -0.312
- reference: rule-first -0.054, rule-last -0.267
