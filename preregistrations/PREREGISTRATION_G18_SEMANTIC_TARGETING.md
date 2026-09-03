# G18 preregistration — prospective semantic targeting, confirmatory

**Created:** 2026-09-03, before any G18 generation.
**Status:** DRAFT until committed and tagged `g18-semantic-targeting-design-v1`.
No model may be run against these conditions before that tag exists.

## 1. Why this experiment exists

The paper's central explanatory claim is that prospective exclusion succeeds or
fails according to **how the future target is represented at rule time**. That claim
is currently supported by a chain of discovery rounds — Stage 3A's ladder, Stage 3C's
rejection of the structural/local-binding reading, Stage 3D's rebuilt similarity
ladder and content × identity 2×2, Stage 3E's deconfounding — each of which changed
the design or the metric in response to what the previous one showed.

Every one of those changes was scientifically justified and is documented. Together
they still mean the paper's centrepiece regularity has never been measured by a
design built to measure it correctly from the start, on items it was not discovered
on.

> **G18 is that design.** One factorial, fresh items, fresh skeletons, the metric
> Stage 3E arrived at, and the per-preview baseline it showed is required.

This is the last planned GPU round. If it confirms, the experimental programme is
closed and the paper is written. If it does not, the semantic-targeting explanation
cannot carry the paper and the project is re-evaluated rather than re-narrated.

## 2. The question

> **When an exclusion policy is stated before its target arrives, does the policy
> govern that target's later causal contribution only when the model already has a
> sufficiently specific *semantic* representation of it — as opposed to a reference
> to it, a lexically similar but semantically different description, or nothing?**

## 3. Materials — fresh, and disjoint from the discovery set

`data/items/g18_v1.jsonl`, built by `src/gen_g18.py`.

| | |
|---|---|
| items | **100** |
| independent skeletons | **30** |
| families | `legal_judgment` 40, `evidence_inference` 30, `ranking_selection` 30 |
| overlap with `items_v1.jsonl` | **none** — asserted at build time on both item id and skeleton |

The ten legal case skeletons (pharmacy, wildfire, bribery, doping, counterfeit,
poaching, datatheft, foodsafety, arttheft, taxevasion), the ten inference domains and
the ten selection scenarios are all new. This removes the dependence on the ten legal
skeletons that carried Stage 3D's 2×2.

Directions are mixed within every family, so a level cannot win by pushing ratings in
one direction.

## 4. Design — 6 × 3, fully crossed

Six **target representations**, placed before the rule. The later evidence the
decision reads is byte-identical across all six; only what the model knows about that
target at rule time changes.

| level | what it supplies |
|---|---|
| `none` | nothing |
| `ident` | a referential stub naming the future item, no content |
| `empty` | high lexical overlap with the evidence, **different proposition** |
| `para` | the same proposition, different words |
| `entail` | a more specific statement that entails the evidence |
| `unrel` | unrelated content, padded to the `para` length |

Three **rule states**: `only` (preview, no evidence, no rule), `norule`
(preview + evidence), `excl` (preview + exclusion rule + evidence). Eighteen cells per
item.

The exclusion rule is the assertive weight form
(`The causal weight assigned to <label> is exactly 0% of its normal evidential
weight`), because Stage 3D established that the bare identity form is too weak to
leave suppression headroom.

**Length note.** `empty` is on average *longer* than `para` (215 vs 162 characters),
so any advantage that mere preview length could confer runs against the hypothesis on
the decisive contrast. `ident` is intrinsically short because it carries no content;
`unrel` is padded to `para`.

## 5. Estimand — raw rating points, per-preview baseline, no ratio

For sign `s = +1` if the evidence pushes the rating up and `−1` otherwise:

```text
marg(level, norule) = s · [ Y(level, norule) − Y(level, only) ]
marg(level, excl)   = s · [ Y(level, excl)   − Y(level, only) ]

ExclusionEffect(level) = marg(level, norule) − marg(level, excl)
```

`ExclusionEffect` is the rating points the **rule** removes, over and above whatever
the preview already did on its own. `marg(level, norule)` is reported separately for
every level, because that is where preview-induced redundancy lives; Stage 3E showed
this is the term that must be held apart.

**No REI, no leverage-normalised ratio, anywhere in this round.** G17 failed on that
metric for a reason this project had already documented.

## 6. Frozen prediction

> Target representations that fix the evidence's **proposition** (`para`, `entail`)
> produce a larger `ExclusionEffect` than representations that merely refer to it
> (`ident`), resemble it lexically without meaning it (`empty`), or are unrelated
> (`unrel`).

Primary estimand, pooled over (model × skeleton) with a cluster bootstrap over
skeletons, seed `20260829`, 10,000 resamples:

```text
Δ_semantic = mean[ ExclusionEffect(para), ExclusionEffect(entail) ]
           − mean[ ExclusionEffect(ident), ExclusionEffect(empty), ExclusionEffect(unrel) ]
```

Secondary, all reported in full regardless of outcome:

- `ExclusionEffect` for all six levels, per model and pooled;
- `marg(level, norule)` for all six levels, per model and pooled;
- the ordering `entail ≥ para > empty ≈ ident ≈ unrel` as a descriptive pattern;
- `ExclusionEffect(para) − ExclusionEffect(empty)`, the single length- and
  lexically-matched contrast.

## 7. Gates

**`confirmed`** requires both:

1. pooled `Δ_semantic` ≥ **3.0 rating points** with bootstrap CI lower bound > 0;
2. the sign of `Δ_semantic` is positive in **at least 4 of 5** models.

**`partial`**: gate 1 passes, gate 2 does not. The regularity holds at panel level but
is not uniform; reported as such, with the dissenting model named.

**`not-confirmed`**: gate 1 fails.

No per-cell significance is required in any model. The primary estimand is the pooled
contrast; per-model effects are reported in full and are expected to vary in size.

## 8. Model panel — frozen, and chosen before any G18 output

Five checkpoints, four vendors: **Qwen3-8B, Gemma-3-12B, Phi-4-mini,
Qwen3.5-27B, Mistral-Small-24B**.

The first four are exactly the panel that carried Stage 3C and 3D; Mistral-Small-24B
is added because it independently replicated the Stage 5 mechanism. The panel is not
selected by expected effect size, and no checkpoint will be swapped after seeing
results. A checkpoint that fails to load is reported by name, not replaced.

**Volume:** 18 × 100 × 5 = **9,000 generations**, behavioural readout
(two-sentence rationale then digit expectation at a fixed position), greedy decoding.

## 9. What each outcome means for the project

| verdict | consequence |
|---|---|
| `confirmed` | The centrepiece regularity is established prospectively on fresh items and skeletons. **The experimental programme closes.** No G19, no further models, no frontier API, no mitigation study, no third mechanism model. Write. |
| `partial` | The paper reports it as a panel-level regularity with a named exception, exactly as it reports Mistral's exception elsewhere. Programme still closes. |
| `not-confirmed` | Semantic target grounding cannot serve as the paper's unified explanation. What remains is the instruction-position reversal plus fragmented observations, in a neighbourhood already occupied by I³C, IHEval, COMPASS, Instruction Position and prospective-memory work. The project is then re-evaluated for termination or reduction to a smaller paper — **not re-narrated a sixth time.** |

## 10. Freeze checklist

- [x] fresh items generated, disjointness from `items_v1.jsonl` asserted at build time
- [x] conditions implemented and prompt assembly verified on all eighteen cells
- [ ] this document, the generator, the frozen artifact and the conditions committed
      and tagged `g18-semantic-targeting-design-v1`
- [ ] only then: generation
