> **Interpretation correction — 2026-09-04 scientific register v3**
>
> The numerical G18 result below remains valid and prospectively confirmed.
> Its earlier interpretation is narrowed: `para/entail` previews themselves
> substantively assert almost the same proposition as the later evidence and reduce the
> later evidence's no-rule marginal from ~32 to ~3 points. Therefore G18 does **not**
> isolate non-evidential knowledge of a future target from prior evidential
> instantiation.
>
> Current role: diagnostic evidence motivating G22 Target Knowledge vs Evidential
> Instantiation. The below-baseline semantic suppression is a mechanism clue, not proof
> of source/proposition scope collapse.
>
> Current authority:
> [../SCIENTIFIC_REGISTER_2026-09-04_V3.md](../SCIENTIFIC_REGISTER_2026-09-04_V3.md)

# G18 — prospective semantic targeting: **confirmed**

**Frozen design:** `preregistrations/PREREGISTRATION_G18_SEMANTIC_TARGETING.md`,
tag `g18-semantic-targeting-design-v1`, committed before any generation.
**Materials:** `data/items/g18_v1.jsonl` — 100 fresh items, 30 independent skeletons,
three families, disjoint from `items_v1.jsonl` by construction.
**Volume:** 9,000 generations, five checkpoints, four vendors.
**Sources:** `results/g18_semantic_targeting_analysis.json`,
`results/raw/*_g18.jsonl`.

## Verdict

Both frozen gates pass.

| gate | requirement | result |
|---|---|---|
| 1 | pooled `Δ_semantic` ≥ 3.0 points, CI lower > 0 | **+8.91 [+7.15, +10.76]** ✓ |
| 2 | sign positive in ≥ 4 of 5 models | **5 of 5** ✓ |

**Verdict: `confirmed`.**

## `ExclusionEffect` by target representation

Rating points the *rule* removes, over and above what the preview did on its own,
each level scored against its own preview-only baseline. No ratio anywhere.

| model | none | ident | empty | **para** | **entail** | unrel | Δ_semantic |
|---|---|---|---|---|---|---|---|
| Qwen3-8B | 17.08 | 24.88 | 14.28 | **37.52** | **29.21** | 15.05 | +15.29 [+10.67, +19.80] |
| Gemma-3-12B | 16.82 | 21.54 | 15.91 | **25.72** | **22.91** | 12.79 | +7.57 [+4.15, +10.90] |
| Phi-4-mini | 5.19 | 7.96 | 7.03 | **10.53** | **12.45** | 5.51 | +4.66 [+1.88, +7.59] |
| Qwen3.5-27B | 41.95 | 46.83 | 30.30 | **48.02** | **56.17** | 47.93 | +10.41 [+6.13, +15.01] |
| Mistral-Small-24B | 28.16 | 30.12 | 22.89 | **32.87** | **35.07** | 29.04 | +6.62 [+3.54, +9.59] |
| **pooled** | 21.84 | 26.27 | 18.08 | **30.93** | **31.16** | 22.06 | **+8.91 [+7.15, +10.76]** |

The decisive contrast is `para` versus `empty`: same template shape, comparable
length — `empty` is on average *longer* — and high lexical overlap, differing only in
whether the preview states the evidence's proposition.

> **para − empty = +12.85 [+10.32, +15.42]** pooled, positive in 5 of 5 models
> (+23.24, +9.81, +3.50, +17.72, +9.97). The interval excludes zero in four; on
> Phi-4-mini it is +3.50 [−1.06, +8.57] and does not.

A referential stub (`ident`) does not behave like a semantic representation. It sits
at 26.27 pooled, between the null levels and the semantic ones, and below both.

## The decomposition changes what the claim is

`ExclusionEffect` is a difference of two margins, and both must be read.

| level | marg(no rule) | marg(exclude) | ExclusionEffect |
|---|---|---|---|
| none | +32.51 | +10.67 | +21.84 [+19.21, +24.66] |
| ident | +35.05 | +8.78 | +26.27 [+23.65, +28.96] |
| empty | +32.48 | +14.40 | +18.08 [+15.71, +20.57] |
| **para** | **+3.27** | **−27.66** | **+30.93 [+28.19, +33.66]** |
| **entail** | **+2.90** | **−28.26** | **+31.16 [+27.99, +34.40]** |
| unrel | +32.83 | +10.77 | +22.06 [+19.16, +24.97] |

Two things follow, and the second is the more interesting.

**1. Stage 3E's confound is real and large, and the design nets it out.** Under a
semantic preview the later evidence is almost entirely redundant: its marginal effect
with no rule falls from ~32 points to ~3. Any analysis without a per-preview baseline
would have attributed that to the rule. This is exactly why the estimand was
specified this way and why G17's ratio metric could not work.

**2. With a semantic target, exclusion goes *below* the preview-only baseline.**
Under `para` and `entail`, `marg(exclude)` is about **−28**: the rule drives the
judgment roughly 28 points below where it sat with the preview alone and no evidence.

A perfectly literal reading of the rule would leave the model at that baseline — the
rule names the later evidence block, and the preview was never excluded. Instead the
model discounts the proposition *wherever it appears*, including in text the rule did
not cover.

This is uniform and it is specific:

| | marg(exclude) under `para` | under `empty` |
|---|---|---|
| Qwen3-8B | −31.41 | +20.99 |
| Gemma-3-12B | −22.31 | +13.21 |
| Phi-4-mini | −6.82 | +23.57 |
| Qwen3.5-27B | −48.09 | +7.19 |
| Mistral-Small-24B | −29.67 | +7.03 |

**Negative in 5 of 5 under `para`; positive in 5 of 5 under `empty`.** A lexically
similar preview with the wrong proposition produces no such drop. Neither does a
referential stub, unrelated content, or no preview at all.

The honest reading has two candidates and they are not far apart. Either the policy
attaches to the proposition and generalises across blocks, or the model overcorrects
when the target is clearly identified. Both require that the target be semantically
identified in the first place, which is the claim under test; neither is available to
an identifier-only policy, which has no way to know the preview carries the same
content. This is the same shape as the Stage 4A agent result, where a proposition
policy still suppresses content that arrives under a different document identifier.

**What must not be said:** that `ExclusionEffect` measures the same thing at every
level. At the semantic levels there is almost no evidence influence left to remove,
and the quantity is dominated by suppression below baseline. The estimand was frozen
in advance and is well defined, but its interpretation differs by level, and the
decomposition above is what makes that visible. It is reported in the paper, not in
an appendix.

## Scope

Five checkpoints, four vendors; 100 fresh items over 30 independent skeletons and
three families. Mistral-Small-24B required the HF-tokenizer conversion of the same
checkpoint (`data/mistral_small_24b_hf`), as in earlier rounds; the
`/var/tmp` snapshot fails to load under this vLLM build. No checkpoint was replaced.

Directions are mixed within every family, so no level can win by pushing ratings in
one direction.

## Consequence

Per the preregistration, `confirmed` closes the experimental programme. No G19, no
further models, no frontier API, no mitigation study, no third mechanism model, no
successor to G16 or G17.
