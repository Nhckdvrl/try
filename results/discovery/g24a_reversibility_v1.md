# G24A evidence reversibility / direction-asymmetry audit v1

**Layer 1 (discovery). No KILL gates; every stratum is reported. Observations only — not confirmatory claims, no new model runs, no prereg.**

Lineage: Rows are the 2026-09-25 full re-run (commit e4319cb) on the corrected item file (92d8cd0). The SELECTION pass still used pre-fix claims, so this artifact is discovery-only and is NOT a strict prereg-confirmatory rerun; confirmatory lineage for paper RQ1 is an open governance item.

Estimands (non-shared-baseline): `A_pre = s*(admit_pre - base)`, `A_post = s*(admit_post - base)`; `C_pre = s*(exclude_pre - admit_pre)`, `C_post = s*(exclude_post - admit_post)`. `C = 0`: exclusion changed nothing; `C = -A`: exactly back to baseline; `C < -A`: overshoot beyond baseline.

## 0. Data and integrity

| quantity | value |
|---|---|
| rows (item x model) | 3000 |
| exact-evidence groups (both directions present) | 53 |
| items in groups | 111 (55 increase / 56 decrease) |
| group size dist (inc,dec) | {"(1, 1)": 48, "(1, 2)": 3, "(2, 1)": 2} |
| group x model pairs | 265 |

Detection = byte-exact `critical_evidence` equality, groups must contain at least one claim of each direction. Within a group the evidence text is fixed, so the inc-vs-dec contrast cannot be driven by evidence identity.

## 1. Cross-baseline correlation panel (replaces shared-Y0 rho)

- rho(A_post, C_pre) = -0.206
- rho(A_pre, C_post) = -0.174
- rho(C_pre, C_post) = +0.405

Spearman over all 3000 complete rows; matches the independent recomputation exactly. `rho(E, L*)` (0.643/0.542 pre/post) is mechanically inflated by the shared Y_base and stays DEMOTED.

## 2. CORE: exact-evidence matched pairs

`dC = mean(C | increase side) - mean(C | decrease side)` within group, per model. n = 265 pairs.

| scope | n | median dC_pre | % dC_pre<0 | median dC_post | % dC_post<0 |
|---|---|---|---|---|---|
| **pooled** | 265 | -3.03 | 69.4% | -42.28 | 89.1% |
| gemma3-12b | 53 | -1.10 | 56.6% | -25.76 | 86.8% |
| llama31-8b | 53 | -2.42 | 64.2% | -28.43 | 81.1% |
| mistral-small-24b | 53 | -38.16 | 92.5% | -52.66 | 98.1% |
| qwen3-8b | 53 | -0.26 | 77.4% | -28.57 | 84.9% |
| qwen35-9b | 53 | -0.16 | 56.6% | -75.69 | 94.3% |

By model x source (median dC_post):

| model/source | n | median dC_post | % neg |
|---|---|---|---|
| gemma3-12b/fever | 28 | -24.48 | 82.1% |
| gemma3-12b/scifact | 25 | -28.27 | 92.0% |
| llama31-8b/fever | 28 | -27.15 | 75.0% |
| llama31-8b/scifact | 25 | -29.40 | 88.0% |
| mistral-small-24b/fever | 28 | -47.42 | 96.4% |
| mistral-small-24b/scifact | 25 | -60.72 | 100.0% |
| qwen3-8b/fever | 28 | -2.50 | 78.6% |
| qwen3-8b/scifact | 25 | -96.44 | 92.0% |
| qwen35-9b/fever | 28 | -70.92 | 89.3% |
| qwen35-9b/scifact | 25 | -89.56 | 100.0% |

Context: median C_post by model x source x direction (all rows):

| cell | n | median C_post |
|---|---|---|
| gemma3-12b/fever/increase | 200 | -33.43 |
| gemma3-12b/fever/decrease | 200 | -0.00 |
| gemma3-12b/scifact/increase | 100 | -29.26 |
| gemma3-12b/scifact/decrease | 100 | +1.61 |
| llama31-8b/fever/increase | 200 | -43.42 |
| llama31-8b/fever/decrease | 200 | -8.29 |
| llama31-8b/scifact/increase | 100 | -40.58 |
| llama31-8b/scifact/decrease | 100 | +1.20 |
| mistral-small-24b/fever/increase | 200 | -74.65 |
| mistral-small-24b/fever/decrease | 200 | -14.83 |
| mistral-small-24b/scifact/increase | 100 | -71.73 |
| mistral-small-24b/scifact/decrease | 100 | -2.60 |
| qwen3-8b/fever/increase | 200 | -0.20 |
| qwen3-8b/fever/decrease | 200 | +0.00 |
| qwen3-8b/scifact/increase | 100 | -39.95 |
| qwen3-8b/scifact/decrease | 100 | +0.00 |
| qwen35-9b/fever/increase | 200 | -78.45 |
| qwen35-9b/fever/decrease | 200 | -1.89 |
| qwen35-9b/scifact/increase | 100 | -91.24 |
| qwen35-9b/scifact/decrease | 100 | -2.43 |

Reading: negative dC_post = the SUPPORTED (increase) side is retracted MORE than the CONTRADICTED (decrease) side under the same evidence text; a contradicted claim's post-retraction residual stays near zero (C_dec ~ 0 = `seen and never comes back`) while the supported side overshoots negative.

## 3. Claim-pair contradiction taxonomy

PENDING: `_claim_pairs.csv` not present yet.

## 4. Rationale paired coding

PENDING: `_coding_*.jsonl` not present yet.

## 5. Baseline / leverage common support

Pair differences of the potential confounds:

| quantity | n | p10 | median | p90 |
|---|---|---|---|---|
| dY0 (Y_base inc - dec) | 265 | -40.2 | +1.5 | +68.6 |
| dA_post (A_post inc - dec) | 265 | -58.3 | -2.7 | +72.0 |
| dA_pre | 265 | -64.1 | -5.4 | +71.2 |

dC_post inside common-support strata (descriptive, no cutoffs gating anything):

| subset | n | median dC_post | % neg |
|---|---|---|---|
| |dY0|<=5 | 76 | -37.09 | 86.8% |
| |dY0|<=10 | 98 | -40.54 | 86.7% |
| |dY0|<=20 | 129 | -40.26 | 88.4% |
| |dA_post|<=10 | 55 | -33.03 | 85.5% |
| |dA_post|<=20 | 91 | -45.36 | 87.9% |
| |dY0|<=10 and |dA_post|<=10 | 12 | -29.90 | 83.3% |

## Provenance

- inputs: `results/discovery/g24a_phenomenology_v1_itemmodel.csv` (columns A/C from commit 7feb552), `data/items/g24a_v1.jsonl` (item file at 92d8cd0), rows from rerun e4319cb
- pairs CSV: results/discovery/g24a_reversibility_v1_pairs.csv
- taxonomy: results/discovery/g24a_reversibility_v1_claim_pairs.csv (hand-classified, section 3)
- coding: results/discovery/g24a_reversibility_v1_coding_<model>.jsonl (section 4)

