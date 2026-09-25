# G24A Pilot P3 — operator-only control readout (v1, 2026-09-26)

Frozen comparisons per registration §11 (wording frozen pre-run, user 2026-09-26): C1 prior_only vs base, C2 withheld_only vs base, C3 withheld_cf vs M_CF^actual. Descriptive only — **no gates, no claim selection (all 200), no p-values, nothing filtered**; interpretation branches have no decision role. Integrity: `check_g24a_p3_raws.py --require5` green (5000 rows = 200 claims × 5 cells × 5 models). Discovery-only lineage as before.

## 1. Trajectory — mean Y (0..100), pooled over 5 models × 200 claims

| cell | Base | PriorOnly | WithheldOnly | WithheldStrong | WithheldCF |
|---|---:|---:|---:|---:|---:|
| pooled | 50.51 | 50.05 | 37.87 | 50.06 | 49.18 |
| mistral-small-24b | 41.28 | 43.75 | 22.04 | 36.65 | 43.26 |
| llama31-8b | 56.04 | 47.73 | 43.30 | 53.11 | 49.02 |
| qwen3-8b | 53.87 | 50.52 | 32.66 | 50.77 | 46.80 |
| qwen35-9b | 41.91 | 49.86 | 45.13 | 51.76 | 52.60 |
| gemma3-12b | 59.46 | 58.38 | 46.23 | 58.00 | 54.21 |

Dispersion around the neutral midpoint (pooled, mean|Y−50|): Base 35.93 → PriorOnly 35.49, WithheldOnly 28.69 (see §§3-4); for reference P2's actual-evidence M_CF mean|M−50| = 12.57 (committed compression artifact).

## 2. Base re-run vs P2 Base — temp-0 noise floor

- claim-level corr(rerun, P2 base) = 0.986; mean diff = +0.27; mean|diff| = 1.84 (p10..p90: -1.5 … +2.6)
- mean|Y−50|: rerun 21.98 vs P2 22.55
- This is the scale against which C1/C2 must be read: two temp-0 runs of the *same* prompt differ by the mean|diff| above.

## 3. C1 — PriorOnly vs Base

- mean(Y_PriorOnly − Y_Base) = **-0.47** (paired over 5×200 cells); mean|Δ| = 15.67
- per-model mean Δ: mistral-small-24b +2.47, llama31-8b -8.31, qwen3-8b -3.36, qwen35-9b +7.95, gemma3-12b -1.09
- claim-mean Δ quantiles [p10…p90]: -15.6 … +15.8 (median -0.1)
- claim-level corr(PriorOnly, Base) = 0.895

## 4. C2 — WithheldOnly vs Base

- mean(Y_WithheldOnly − Y_Base) = **-12.64**; mean|Δ| = 25.99
- per-model mean Δ: mistral-small-24b -19.24, llama31-8b -12.74, qwen3-8b -21.21, qwen35-9b +3.21, gemma3-12b -13.24
- claim-mean Δ quantiles [p10…p90]: -35.7 … +6.9 (median -12.0)
- claim-level corr(WithheldOnly, Base) = 0.779

## 5. C3 — WithheldCF vs the actual-evidence center M_CF^actual

- mean: WithheldCF 49.18 vs M_CF^actual 45.20 → mean diff **+3.97**; mean|diff| (claim-level) = 12.86
- claim-level corr(WithheldCF, M_CF^actual) = 0.667; OLS WithheldCF = 5.36 + 0.969·M_CF^actual
- mean|Y−50|: WithheldCF 17.59 vs M_CF^actual 12.57 (P2 Y0 reference: 22.55)
- claim-mean diff quantiles [p10…p90]: -16.5 … +25.4 (median +3.0)
- per-model (M_CF^actual, WithheldCF, Δ): mistral-small-24b (40.2, 43.3, +3.0); llama31-8b (43.8, 49.0, +5.2); qwen3-8b (38.5, 46.8, +8.3); qwen35-9b (50.1, 52.6, +2.5); gemma3-12b (53.4, 54.2, +0.8)

Companion (descriptive): WithheldStrong vs M_strong^actual — mean 50.06 vs 43.02 (+7.04), corr 0.770, mean|Y−50| 18.79 vs 14.88.

## 6. Caveats

- All numbers are descriptive condition means; the §11 interpretation branches (operator-induced recalibration vs state-dependent trace vs non-equivalent base) are read by hand against §§2-5, not by any threshold.
- Discovery-only claims; nothing here is confirmatory; no RQ declared or implied.
- WithheldCF never shows evidence content (leakage-asserted 2,000× pre-run); its Δ vs M_CF^actual is bounded below by the temp-0 floor in §2.
