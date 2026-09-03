# G17 — does the binding requirement exist only at complete suppression?

**Frozen design:** `preregistrations/PREREGISTRATION_G17_BINDING_BY_WEIGHT.md`, tag
`g17-binding-by-weight-design-v1`, committed before any generation.
**Sources:** `results/g17_binding_by_weight_analysis.json`,
`results/raw/{qwen3-8b,gemma3-12b,phi4-mini,qwen35-27b}_g17.jsonl` (2,400 generations).

## Frozen verdict: `no-rescue`

Under the preregistered estimand (REI, a leverage-normalised ratio) gate 1 passes in
only 2 of 4 models and gate 2 fails. **The frozen verdict is `no-rescue`** and it is
recorded as such.

| model | rescue w=0 | rescue w=0.25 | rescue w=0.50 |
|---|---|---|---|
| Qwen3-8B | −3.85 [−13.08, +0.44] | −31.79 [−102.01, +0.08] | −0.78 [−2.26, +0.03] |
| Gemma-3-12B | +6.39 [+0.04, +19.72] | +5.18 [−0.15, +16.43] | −0.08 [−0.13, −0.03] |
| Phi-4-mini | −3.82 [−12.73, +0.28] | +0.27 [−0.01, +0.75] | −2.24 [−7.02, +0.05] |
| Qwen3.5-27B | +0.49 [+0.28, +0.71] | +0.16 [−0.07, +0.43] | +0.24 [+0.09, +0.41] |

## The frozen estimand is defective, and the defect was already known

Those intervals are not credible. A rescue of −31.79 with a 95% interval of
[−102.01, +0.08] is a ratio blowing up, not a behavioural effect.

`REI` divides by each item's leverage `|admit − base|`. On this set that denominator
collapses on a small minority of items — **1 of 75 has leverage ≈ 0 and produces
REI = 8,492**, which alone destroys every pooled estimate and interval.

This failure mode is **not new to the project**. Stage 3E found it, wrote it down, and
solved it by abandoning the ratio for raw rating points:

> "Under a preview, the admit anchor `|L|` shrinks a lot, so REI (a ratio) becomes
> unstable — the earlier Stage-3D table produced values like −1.25 for that reason.
> Everything here is reported in **raw rating points** instead."

The G17 preregistration specified REI anyway. That is a design error on my part, made
before any data was seen. It is not a post-result rationalisation, but it does mean the
frozen verdict measures the instrument rather than the hypothesis.

## Post-result re-analysis with the Stage 3E estimator

Same data, same conditions, same cluster bootstrap. The only change is dropping the
ratio and reporting the rescue in raw sign-aligned rating points, which is what
Stage 3E adopted for this exact failure mode.

| requested weight | preview rescue (rating points) |
|---|---|
| **w = 0.00** | **+10.09 [+7.03, +13.26]** |
| w = 0.25 | +0.94 [−1.24, +3.14] |
| w = 0.50 | +0.64 [−1.60, +2.85] |

Interaction, per item, pooled over (model × case skeleton):

```text
Δ = rescue(0) − mean[rescue(0.25), rescue(0.50)] = +9.30 [+6.11, +12.65]
```

This is the pattern the preregistration predicted, and it is unambiguous: a content
preview removes ten rating points of leakage when the policy demands **exactly zero**,
and nothing at all when it demands a fraction.

## Status: suggestive, not confirmed

Both facts are true at once and both must be reported:

- the **preregistered test returned `no-rescue`**, on a metric that cannot support any
  verdict here;
- the **robust re-analysis supports the linking hypothesis**, with a large effect and
  an interval far from zero — but it is a post-result change of estimator.

**The paper may not claim `unified` on this evidence.** A post-result estimator switch
that produces the predicted answer is exactly the move that preregistration exists to
discipline, and the fact that the switch has an independent precedent in Stage 3E makes
it defensible, not confirmatory.

What this licenses is a **prospective confirmation**: the same crossing, a fresh
preregistration naming raw rating points as the primary estimand, a leverage floor
fixed in advance, and per-preview baseline cells so the Stage 3E `ExclusionEffect`
decomposition is available. That is one clean experiment, not a fishing expedition, and
its outcome would either close the paper's main seam or leave §4 and §5 as two separate
regularities.

Until then the paper keeps §4 and §5 separate and says why.

## Design lessons recorded

1. **Carry forward the project's own metric decisions.** Stage 3E's move off REI was
   documented and I did not apply it. Any future round on preview-bearing conditions
   uses raw rating points.
2. **A ratio estimand needs a leverage floor stated in advance.** The project's standard
   `build_table` exposes `min_leverage_frac` and every caller leaves it at 0.0; that is
   a latent hazard across the REI-based rounds, not only here.
3. **Include the baseline cells the decomposition needs.** G17 has no
   "preview + evidence, no rule" cell, so `marg(no rule)` is not identifiable and the
   Stage 3E decomposition cannot be computed from this data at all.
