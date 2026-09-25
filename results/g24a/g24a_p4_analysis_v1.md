# G24A Pilot P4 — irrelevant-visible evidence control (v1, 2026-09-26)

Frozen comparisons per registration §12 (wording + material rule frozen pre-run, user 2026-09-26): A1 IrrelVisible vs WithheldOnly, A2 IrrelVisible vs Base, B1 IrrelCF vs WithheldCF, B2 IrrelCF vs M_CF^actual, and the position on the WithheldCF → M_CF^actual segment. Descriptive only — **no gates, no claim selection (all 200), no p-values, nothing filtered**; the three §12 branches are read by hand and have no decision role. Integrity: `check_g24a_p4_raws.py --require5` green (2000 rows = 200 claims × 2 cells × 5 models). Discovery-only lineage as before.

## 1. Trajectory — mean Y (0..100), pooled over 5 models × 200 claims

| anchor | Base | WithheldOnly | IrrelVisible | WithheldCF | IrrelCF | M_CF^actual |
|---|---:|---:|---:|---:|---:|---:|
| pooled | 50.51 | 37.87 | 14.94 | 49.18 | 46.07 | 45.20 |
| mistral-small-24b | 41.28 | 22.04 | 9.46 | 43.26 | 41.21 | 40.25 |
| llama31-8b | 56.04 | 43.30 | 29.87 | 49.02 | 45.40 | 43.82 |
| qwen3-8b | 53.87 | 32.66 | 17.07 | 46.80 | 47.76 | 38.51 |
| qwen35-9b | 41.91 | 45.13 | 5.15 | 52.60 | 41.50 | 50.07 |
| gemma3-12b | 59.46 | 46.23 | 13.13 | 54.21 | 54.48 | 53.39 |

Dispersion (pooled, mean|Y−50|): Base 35.93 → WithheldOnly 28.69 → IrrelVisible 41.55; WithheldCF 26.80 → IrrelCF 29.00 vs M_CF^actual 12.57 (Y0 reference 22.55).

## 2. Reference scales

- temp-0 noise floor (committed): same-prompt re-run mean|diff| = 1.84, corr 0.986 — every Δ below is read against this.
- anchors: WithheldCF (frame only) 49.18; IrrelCF 46.07; M_CF^actual (relevant evidence) 45.20.

## 3. A1 — IrrelVisible vs WithheldOnly (frame alone)

- mean(Y_IrrelVisible − Y_WithheldOnly) = **-22.93**; mean|Δ| = 29.17
- per-model mean Δ: mistral-small-24b -12.58, llama31-8b -13.43, qwen3-8b -15.59, qwen35-9b -39.98, gemma3-12b -33.09
- claim-mean Δ quantiles [p10…p90]: -45.6 … -3.2 (median -22.4); claim-level corr 0.561

## 4. A2 — IrrelVisible vs Base

- mean(Y_IrrelVisible − Y_Base) = **-35.58**; mean|Δ| = 40.49
- per-model mean Δ: mistral-small-24b -31.82, llama31-8b -26.17, qwen3-8b -36.80, qwen35-9b -36.76, gemma3-12b -46.33
- claim-mean Δ quantiles [p10…p90]: -64.1 … -6.7 (median -32.9); claim-level corr 0.492

## 5. B1 — IrrelCF vs WithheldCF (frame-only anchor)

- mean(Y_IrrelCF − Y_WithheldCF) = **-3.11** (paired over 5×200 cells); mean|Δ| = 20.28
- per-model mean Δ: mistral-small-24b -2.05, llama31-8b -3.62, qwen3-8b +0.97, qwen35-9b -11.09, gemma3-12b +0.27
- claim-mean Δ quantiles [p10…p90]: -21.9 … +16.5 (median -3.0); claim-level corr 0.729

## 6. B2 — IrrelCF vs the actual-evidence center M_CF^actual

- mean: IrrelCF 46.07 vs M_CF^actual 45.20 → mean diff **+0.87**; mean|diff| (claim-level) = 13.42
- claim-level corr(IrrelCF, M_CF^actual) = 0.686; OLS IrrelCF = -0.56 + 1.032·M_CF^actual
- mean|Y−50|: IrrelCF 19.44 vs M_CF^actual 12.57 (Y0 reference 22.55)
- claim-mean diff quantiles [p10…p90]: -20.2 … +22.5 (median -1.0)
- per-model (M_CF^actual, IrrelCF, Δ): mistral-small-24b (40.2, 41.2, +1.0); llama31-8b (43.8, 45.4, +1.6); qwen3-8b (38.5, 47.8, +9.3); qwen35-9b (50.1, 41.5, -8.6); gemma3-12b (53.4, 54.5, +1.1)

## 7. Position on the WithheldCF → M_CF^actual segment

- WithheldCF 49.18 → IrrelCF 46.07 → M_CF^actual 45.20: span fraction = **0.782** (0 = identical to the frame-only anchor, 1 = identical to the relevant-evidence anchor; values outside [0,1] mean IrrelCF sits outside the segment).
- distance to each anchor: |IrrelCF − WithheldCF| = 3.11, |IrrelCF − M_CF^actual| = 0.87 (noise floor 1.84).

## 8. §12 branches (read by hand — no decision role)

- *IrrelCF ≈ WithheldCF* → only decision-relevant evidence leaves the extra trace.  Observed Δ = -3.11 (1.7× the 1.84 floor).
- *IrrelCF ≈ M_CF^actual* → seeing any evidence-like content and then retracting produces the distortion.  Observed Δ = +0.87 (0.5× the 1.84 floor).
- *in between* → frame + visible-content + relevance contribute in three layers (span 0.782 above).

## 9. Caveats

- All numbers are descriptive condition means; the §12 branches are interpretation aids, not gates.  A1/B1 are cross-run paired comparisons (P4 vs P3), each cell being its own run of the same claims — the noise floor in §2 calibrates run-to-run drift.
- The irrelevant text is mechanically screened (page-disjoint, no shared length≥5 token, seeded) but is naturally phrased evidence, not adversarially constructed; zero model involvement in selection (material rule §12, asserted per item by the verifier).
- Discovery-only claims; nothing here is confirmatory; no RQ declared or implied.  After P4: discovery stops (§12).
