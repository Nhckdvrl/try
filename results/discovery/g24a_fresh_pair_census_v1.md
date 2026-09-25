# G24A fresh exact-evidence-pair census v1

**Layer-2 feasibility census. Observations only — no kill gates, no model output read, nothing filtered except the explicit freshness rules below.**

Purpose (user, 2026-09-25): determine how many byte-exact same-evidence, opposite-direction claim groups exist in the frozen candidate pool OUTSIDE the 600-item discovery set, to judge whether a held-out confirmation on purely natural data is possible.

## 0. Inputs and integrity

| check | value |
|---|---|
| candidates pool lines | 13283 (== 13,283 expected) |
| discovery items | 600 |
| discovery ids found in pool | 600/600 |
| discovery opposite-direction evidence SHAs | 53 (== 53 expected) |
| candidate source split | {"fever": 12648, "scifact": 635} |

Freshness rules: (1) drop the 600 discovery item_ids; (2) group by byte-exact `critical_evidence`, require both directions present; (3) drop groups whose evidence SHA256[:10] is one of the 53 discovery pair evidences. No model output path is ever opened (asserted in code).

## 1. Fresh landscape

| quantity | value |
|---|---|
| both-direction groups before 53-SHA exclusion | 1608 |
| removed by 53-SHA exclusion | 26 |
| **fresh groups** | **1582** |
| **fresh items** | **10119** |
| fresh groups FEVER / SciFact | 1515 / 67 |
| fresh items FEVER / SciFact | 9971 / 148 |

Topology (n_inc, n_dec): cells with >=4 groups listed individually, remaining cells aggregated as a long tail; full table in the JSON (`topology_full`):

| topology | groups | items |
|---|---|---|
| (1,1) | 243 | 486 |
| (2,1) | 107 | 321 |
| (1,2) | 87 | 261 |
| (2,2) | 87 | 348 |
| (3,2) | 64 | 320 |
| (4,3) | 51 | 357 |
| (1,3) | 50 | 200 |
| (3,1) | 50 | 200 |
| (3,3) | 48 | 288 |
| (4,1) | 42 | 210 |
| (4,2) | 40 | 240 |
| (2,3) | 34 | 170 |
| (3,4) | 32 | 224 |
| (2,4) | 29 | 174 |
| (3,5) | 28 | 224 |
| (5,2) | 28 | 196 |
| (5,5) | 27 | 270 |
| (4,4) | 26 | 208 |
| (5,4) | 25 | 225 |
| (5,3) | 24 | 192 |
| (4,5) | 20 | 180 |
| (4,6) | 20 | 200 |
| (5,6) | 20 | 220 |
| (6,3) | 20 | 180 |
| (6,5) | 20 | 220 |
| (2,5) | 19 | 133 |
| (6,6) | 19 | 228 |
| (5,7) | 18 | 216 |
| (6,4) | 17 | 170 |
| (6,2) | 16 | 128 |
| (1,4) | 14 | 70 |
| (4,7) | 14 | 154 |
| (6,7) | 14 | 182 |
| (2,6) | 12 | 96 |
| (5,1) | 12 | 72 |
| (3,6) | 11 | 99 |
| (6,8) | 11 | 154 |
| (3,7) | 10 | 100 |
| (5,8) | 9 | 117 |
| (7,5) | 9 | 108 |
| (6,1) | 8 | 56 |
| (7,3) | 8 | 80 |
| (4,8) | 7 | 84 |
| (7,4) | 7 | 77 |
| (7,8) | 7 | 105 |
| (5,9) | 6 | 84 |
| (6,9) | 6 | 90 |
| (6,11) | 6 | 102 |
| (7,6) | 6 | 78 |
| (1,5) | 5 | 30 |
| (5,10) | 5 | 75 |
| (8,5) | 5 | 65 |
| (8,9) | 5 | 85 |
| (1,6) | 4 | 28 |
| (3,8) | 4 | 44 |
| (4,10) | 4 | 56 |
| (5,11) | 4 | 64 |
| (9,3) | 4 | 48 |
| long tail (31 cells, <=3 groups each) | 54 | 727 |

## 2. Freshness audit (descriptive, nothing excluded)

- 242 fresh groups have evidence text that also appears in the 600-item discovery set (but NEVER as an opposite-direction pair there — those are the 53)
- 1340 fresh groups have evidence never seen in discovery at all (strictly unseen subset)

Both numbers are reported for the user to choose from when designing a held-out confirmation; the census itself excludes only the 53, per instruction.

## 3. Automatic contradiction taxonomy (descriptive; blind audit pending)

Deterministic rules with precedence: explicit_negation > exclusive_alternative > numeric_value (number-token sets differ between claim sides) > antonym_opposite (lexical pair across sides) > indirect_contradiction (default).

| auto type | groups | % of fresh |
|---|---|---|
| explicit_negation | 490 | 31.0% |
| indirect_contradiction | 422 | 26.7% |
| exclusive_alternative | 339 | 21.4% |
| numeric_value | 312 | 19.7% |
| antonym_opposite | 19 | 1.2% |

negation_present: {"no": 1092, "yes": 490}

STATUS: automatic labels are a landscape description, NOT verified judgments. A blind sample audit (coders never see the auto labels) is the next step before any sampling decision.

## 4. Claim similarity and entity overlap (description only)

Per group: mean over all inc x dec claim pairs of (a) token Jaccard (stopwords removed) and (b) capitalized-word Jaccard (rough entity proxy). NEVER used as a filter here.

| quantity | n | p10 | p25 | median | p75 | p90 |
|---|---|---|---|---|---|---|
| claim token Jaccard | 1582 | 0.231 | 0.298 | 0.375 | 0.479 | 0.625 |
| entity overlap | 1582 | 0.250 | 0.426 | 0.614 | 0.917 | 1.000 |

## 5. Governance

- no model outputs read; no RQ kill criteria attached; this census only maps the natural-data landscape (user ruling 2026-09-25: '这里不设 <N 就 kill RQ')
- inputs frozen: candidates file = selection-pass input (unchanged since the 13,283-pool freeze); discovery item file at 92d8cd0
- outputs feed the Layer-2 held-out confirmation design decision; no experiment is authorized by this document

