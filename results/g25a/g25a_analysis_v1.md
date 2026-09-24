## Verdict
**order-artifact**

An integrity gate failed (I1 anchor symmetry, or I2 RuleAcc below 0.8 — including absent probe data): no claim is licensed; integrity investigation precedes any interpretation.

- I1 (Gap(w100) 95% CI contains 0): FAIL — -1.06 [-1.93, -0.21]
- I2 (pooled RuleAcc ≥ 0.8): PASS — 0.949 over 3200 parsed probe rows (unparsed: 0)
- S1 (≥ 360 items usable on ≥ 3/4 models): FAIL — 354/400
- G1 (Δ_local0 CI low > 0 and point ≥ 3.0): PASS — +3.58 [+1.33, +5.79] (boot_p=0.0014)
- G2 (Gap(0)−Gap(1) CI low > 0 and point ≥ 3.0): FAIL — +2.83 [+0.49, +5.11] (boot_p=0.0140)
- G3 (≥ 3/4 model means positive, per primary; cross-model sentence only): Δ_local0 PASS (3/4), Gap01 PASS (3/4)

## Gap(w) — pooled decomposition
  w        ResInf(pre)  ResInf(post)                Gap(w)
  w000          +20.72        +10.14   +10.58 [+8.36, +12.82]
  w001          +19.49        +11.74    +7.76 [+6.21, +9.30]
  w002          +21.76        +14.86    +6.90 [+5.59, +8.21]
  w005          +22.12        +15.76    +6.36 [+5.08, +7.66]
  w010          +23.00        +17.40    +5.60 [+4.33, +6.90]
  w025          +24.45        +20.86    +3.59 [+2.54, +4.65]
  w100          +37.90        +38.96    -1.06 [-1.93, -0.21]

## Co-primaries (pooled-4)
- Δ_local0 = Gap(0) − mean[Gap(1), Gap(2), Gap(5)]: +3.58 [+1.33, +5.79] n_clusters=339 seed=20260924 B=10000
- Gap(0)−Gap(1): +2.83 [+0.49, +5.11] n_clusters=339

## Usability ledger (§6: all 16 cells + s·L > 0, per model)
{"gemma3-12b": {"drops": {"nonpositive_anchor": 24}, "rows_in_file": 7200, "usable": 376}, "llama31-8b": {"drops": {"nonpositive_anchor": 78}, "rows_in_file": 7200, "usable": 322}, "qwen3-8b": {"drops": {"nonpositive_anchor": 50}, "rows_in_file": 7200, "usable": 350}, "qwen35-9b": {"drops": {"nonpositive_anchor": 57}, "rows_in_file": 7200, "usable": 343}}

