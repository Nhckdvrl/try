# G24A P2 — claim-level center compression M_k (discovery artifact v1, 2026-09-26)

Registered by user ruling 2026-09-26 (before P3). Descriptive only: no gate, no claim selection, no p-values, nothing filtered — all 200 discovery claims, all 5 panel models, read from the committed frozen cells csv (`g24a_p2_analysis_v1_cells.csv`). Discovery-only lineage per `g24a_p2_figures_v1.md` §0.

## 0. Definition

$$M_k = \frac{Y_{k,+} + Y_{k,-}}{2}$$ — the center, across the two polarity arms, of the SAME claim after retraction operator $k$ (each $Y$ a 5-model mean; $Y_0$ the shared evidence-free Base).

Reference points: restoration to the counterfactual would give $M_k = Y_0$ exactly (corr = 1, slope = 1, intercept = 0, $|M_k - 50| = |Y_0 - 50|$); a flat neutral attractor would give corr = 0 with $M_k = 50$.

## 1. Numbers (claim-level, n = 200)

Baseline: mean $Y_0$ = 50.24, mean $|Y_0 - 50|$ = 22.55.

| operator k | corr($M_k$, $Y_0$) | OLS $M_k$ = a + b·$Y_0$ | mean $|M_k - 50|$ | compressed claims $|M_k-50| < |Y_0-50|$ |
|---|---:|---:|---:|---:|
| Exclude | 0.526 | 23.77 + 0.282·$Y_0$ | 15.58 | 60% |
| StrongExclude | 0.713 | 20.82 + 0.442·$Y_0$ | 14.88 | 68% |
| CounterfactualDelete | 0.701 | 25.84 + 0.385·$Y_0$ | 12.57 | 72% |

Per-model corr($M_{CF}$, $Y_0$) (robustness row): gemma3-12b 0.436, llama31-8b 0.308, mistral-small-24b 0.585, qwen3-8b 0.504, qwen35-9b 0.570.

## 2. Reading (descriptive)

- **Claim-dependent**: corr($M_{CF}$, $Y_0$) = 0.701 — the landing center is NOT a flat 50; claims keep part of their prior ordering.
- **Strongly compressed**: slope 0.385 (restoration = 1), mean $|Y_0-50|$ 22.55 → mean $|M_{CF}-50|$ 12.57 (44% contraction toward the midpoint), monotone in instruction strength (Exclude → StrongExclude → CounterfactualDelete).
- **Not restoration**: the attractor line has intercept 25.84 and slope 0.385; mean $M_{CF}$ = 45.20 vs mean $Y_0$ = 50.24 (a small shared downward shift of -5.04 rides on top of the compression).
- Form: **claim-specific prior → strongly compressed prior** ("retraction-induced confidence contraction"), not counterfactual restoration.

Converging context (already committed): polarity separation 56.32 → 12.01 across arms at CF (79% of evidence-specific direction erased, `g24a_p2_figures_v1.md`); CF moves judgments > 20 points even where Admit did nothing (102/186 support, 75/143 refute cells); §10 rationale reading found `still_uses_evidence` at only 4/106 under CF while numerical residual stays large, and `exclusion_implies_distrust` = 0/530 — the evidence's *content* is largely gone while the *act of being asked to retract* still moves the number.

Motivation for the next step: P3 operator-only control (registration §11) — does the compressed attractor need actual evidence at all, or does the retraction / evidence-unavailable language frame induce the contraction by itself?

## 3. Provenance

- Script: `scripts/analyze_g24a_p2_compression.py` (asserts: 5 models × 200 claims, pooled mean $Y_0$ = 50.24, mean $|Y_0-50|$ = 22.55, and the quoted CF figures 0.701 / 25.84 / 0.385 / 12.57).
- Machine-readable: `results/g24a/g24a_p2_compression_v1.json`.
- No model was run for this artifact; inputs are the frozen P2 raws already checked by `check_g24a_p2_raws.py --require5`.
