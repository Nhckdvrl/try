# ConfB blind re-audit sensitivity (post hoc)

The independent local OpenCode audit saw claim and randomly swapped evidence A/B, without previous labels or model output. These strata were defined **after** the held-out ConfB results. They cannot constitute a new confirmation, and LLM-assisted semantic labels are not human gold. The primary analysis retains all 200 frozen pairs.

All six models are kept for every selected claim. Each interval is a claim-cluster bootstrap (3,000 draws within stratum); small flagged strata have unstable intervals. Scores are 0–100.

| Stratum | n claims | Admit sep | CF sep | Center CRE | Arm-wise error |
|---|---:|---:|---:|---:|---:|
| All frozen 200 | 200 | 62.95 [58.31,67.26] | 8.33 [6.60,10.12] | 29.96 [28.08,31.79] | 30.88 [29.07,32.65] |
| Audit pair-valid | 190 | 64.60 [60.15,68.85] | 8.56 [6.76,10.33] | 30.10 [28.18,32.07] | 31.04 [29.18,32.94] |
| Audit relation-consistent | 189 | 65.33 [61.14,69.57] | 8.79 [7.08,10.50] | 30.06 [28.18,31.96] | 31.00 [29.20,32.85] |
| Audit valid + relation-consistent + natural | 142 | 67.83 [63.03,72.43] | 9.36 [7.23,11.46] | 30.09 [28.00,32.35] | 31.08 [29.02,33.31] |
| Audit flagged invalid | 10 | 31.56 [8.74,53.88] | 3.98 [-2.99,10.73] | 27.20 [20.25,33.86] | 27.75 [21.07,34.11] |

The audit's main material concern is semantic entailment, not whether a model judges the evidence strongly. If the main result remains in the stricter stratum, that reduces dependence on obvious malformed pairs but does not remove residual measurement or benchmark-format concerns.
