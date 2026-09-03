# G17 preregistration — are the paper's two regularities one regularity?

**Created:** 2026-09-03, before any G17 generation.
**Status:** DRAFT until committed and tagged `g17-binding-by-weight-design-v1`. No
target model may be run against these conditions before that tag exists.

## 1. The gap this closes

The paper currently asserts two regularities side by side and never connects them:

- **§4.** The prospective failure exists only at a requested weight of exactly zero.
  Pooled discontinuity **+0.295 [+0.185, +0.405]**; at every non-zero level the
  pre/post gap is ≈0, and models land near an effective weight of ~0.45 whatever
  fraction is requested.
- **§5.** Whether a prospective policy governs the decision depends on what it can
  bind to. A content preview before the rule rescues suppression, graded by
  entailment; a named future referent does not.

Nothing in the repository crosses them. Every weight-sweep condition uses a named
referent (`uniform_weight_rule` addresses `item.critical_label`), and every binding
manipulation is run at `w = 0`. So the paper has two facts where it may have one.

**The linking hypothesis.** Driving a contribution to *exactly zero* requires the
model to identify precisely which content to remove, and identification is what
binding supplies. Attenuation requires no such identification — a generic discount
suffices, which is consistent with models landing near 0.45 regardless of the
fraction requested.

> **If the hypothesis holds, the binding requirement should appear at `w = 0` and
> nowhere else.** §4 and §5 then become one mechanism, and the paper's main line
> closes instead of branching.

## 2. Design

Frozen 75-item semantic-addressability set (`data/items/frozen_semaddr.json`),
families `legal_judgment` + `evidence_inference`. Behavioural readout (two-sentence
rationale then digit expectation at a fixed position) — **not** the mechanism readout,
which `results/mech/readout_validity_binding_results.md` shows can be blind to a
binding contrast.

Full crossing of **binding × requested weight**, rule always stated *before* the
evidence:

| factor | levels |
|---|---|
| preview placed before the rule | `none`, `para` (proposition-matched paraphrase) |
| requested weight | `0.00`, `0.25`, `0.50` |

plus two anchors: `base` (no rule) and `admit` (`w = 1.00`, no preview). Eight
conditions per item.

Everything else is inherited byte-identical: `uniform_weight_rule` for the rule
string at every level (so prohibition and attenuation are worded identically),
`preview_text(item, rung)` for the preview, block order, answer format, greedy
decoding.

**Models.** The four checkpoints that already have the Stage 3D ladder, so the new
cells are comparable to existing ones: Qwen3-8B, Gemma-3-12B, Phi-4-mini,
Qwen3.5-27B.

**Volume.** 8 × 75 × 4 = **2,400 generations**. One node, idle cards only.

## 3. Estimands

`REI = s · (y_cond − y_base) / |admit − base|`, the project's standard measure:
0 = decided as if the evidence had never been seen, 1 = used as when admitted. Items
with non-positive signed leverage are dropped, as everywhere else.

For each weight `w`:

```text
Rescue(w) = REI(w, none) − REI(w, para)
```

positive = the preview moved the decision toward suppression.

The test of the linking hypothesis is the **interaction**:

```text
Δ = Rescue(0.00) − mean[ Rescue(0.25), Rescue(0.50) ]
```

Inference: cluster bootstrap over case skeletons, seed `20260829`, 10,000 resamples,
per model and pooled over (model × skeleton).

## 4. Gates, frozen

**`unified`** requires all of:

1. `Rescue(0.00)` ≥ 0.15 with CI lower bound > 0, in at least 3 of 4 models;
2. pooled `Δ` ≥ 0.15 with CI lower bound > 0;
3. pooled `Rescue(0.25)` and `Rescue(0.50)` each have a CI containing zero.

**`partial`**: gates 1 and 2 pass but a non-zero level shows a rescue CI excluding
zero. Binding matters most at complete suppression but is not exclusive to it.

**`independent`**: gate 2 fails. The two regularities are separate facts and the
paper keeps them separate.

**`no-rescue`**: gate 1 fails. The Stage 3D rescue did not reproduce on this set;
that would be a replication failure of §5.2 and must be reported as one.

## 5. What may be claimed under each verdict

| verdict | permitted claim |
|---|---|
| `unified` | The prospective failure and the binding requirement are one phenomenon: complete suppression needs the target identified, and binding is what identifies it. §4 and §5 merge. |
| `partial` | Binding matters most at complete suppression. Reported as a gradient, not a discontinuity, with the non-zero rescue shown. |
| `independent` | Two separate regularities, reported separately, exactly as the paper does now. No loss. |
| `no-rescue` | §5.2's rescue does not replicate on this set under this readout. Reported as a replication failure; the entailment ladder's status is then reopened. |

## 6. Why this is not a defensive experiment

It is not a control and it does not protect an existing claim. It asks whether two
established results are the same result — the kind of question that either tightens a
paper's main line or shows it genuinely has two branches. Both outcomes change what
the paper says.

It is also the only such gap identified in an audit of the full chain. §3's four
exclusions, §5.1's ladder, §5.2's entailment grading, §5.3's stream, §6's agent
transfer and §7's mechanism each already connect to a neighbour; §4 and §5 do not.

`no-rescue` and `independent` are real possible outcomes and are pre-committed above.
Neither will be re-run with an adjusted construction.

## 7. Freeze checklist

- [ ] conditions implemented and exercised on prompts only
- [ ] this document committed and tagged `g17-binding-by-weight-design-v1`
- [ ] only then: generation
