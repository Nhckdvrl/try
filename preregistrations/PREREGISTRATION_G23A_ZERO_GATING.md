# G23A preregistration — gating is not merely reweighting

**Created:** 2026-09-23, before any G23A generation.
**Status:** REVISION PENDING FREEZE.
The original v1 design was committed/tagged before generation, but a 2026-09-23
pre-generation audit found two inferential issues: pooled clustering and over-strong
wording of the zero-vs-nonzero claim. No G23A target-model generation occurred.
This corrected design must be committed and tagged `g23a-zero-gating-design-v2`
before any target model is run.

Governing direction:
[../SCIENTIFIC_REGISTER_2026-09-04_V3.md](../SCIENTIFIC_REGISTER_2026-09-04_V3.md) §6.
This file does not supersede the repository-wide V17 authority in `README.md` /
`STATUS.md`; it is the frozen design for the one reopened legacy line.

## 1. Why this experiment exists

The reopened line has a broad, replicated phenomenon (G0: the same exclusion rule is
less effective before the evidence than after it, 12/12 instruct models, matched Admit
controls clean) and a promising but never prospectively tested boundary: the timing gap
looked like it lived at exactly `w = 0`.

The old evidence for that boundary is a **ratio**:

> `gap(w=0) − mean(gap(non-zero)) = +0.295 [+0.185, +0.405]` REI units.

That is the same estimator that produced G17's `−31.79 [−102.01, +0.08]` and was
abandoned in Stage 3E. It is suggestive, not load-bearing, and the register says so
explicitly: the kink was not individually identified in every model.

So the project currently has a candidate law, a defective estimator, and a paper story
(`prospective gating vs retrospective cancellation`) that only deserves to continue if
the candidate law survives on fresh items in raw rating points.

> **G23A is that test.** One factor (`w`), two block orders, fresh items, fresh
> skeletons, raw points, frozen exclusions, frozen gates.

## 2. The question

> **Is the prospective/retrospective asymmetry specific to making the evidence
> completely non-causal (`w = 0`), or does the same timing failure appear when the
> model is merely asked to attenuate the evidence by a non-zero amount?**

If complete exclusion carries an additional timing penalty beyond non-zero attenuation,
the paper gains a computational boundary that is not a restatement of instruction
position:

> **Categorical exclusion has an extra prospective timing cost beyond ordinary
> attenuation.**

This is deliberately narrower than “prospective weighting works”: PRE/POST equality at
a non-zero weight does not prove that either arm numerically implemented that weight.

If it is not, the gate-vs-cancellation story weakens before any mechanism work is
spent on it.

## 3. Materials — fresh, and disjoint from every earlier set

`data/items/g23a_v1.jsonl`, built by `src/gen_g23a.py`.

| | |
|---|---|
| items | **72** |
| independent skeletons | **72** — one item per skeleton, so every cluster is an independent case |
| families | `legal_judgment` 24, `evidence_inference` 24, `ranking_selection` 24 |
| directions | 12 `increase` / 12 `decrease` **inside every family** (36/36 overall) |
| overlap with `items_v1`, `g18_v1`, `linear_v1` | **none** — asserted at build time on item id, surface domain and skeleton |
| gold | **none** — no LLM judge, no labelled answer; the judgment is the model's own rating |

Twenty-four new legal cases, twenty-four new diagnostic domains and twenty-four new
selection scenarios. The three families are the ones the old programme already
validated for continuous judgments; the `outcome_evaluation` family is deliberately
**not** used, because its known order-independent residue would sit inside the very
contrast G23A measures.

Directions are mixed inside every family, so no requested weight can win by pushing
ratings in one direction.

## 4. Design — one number, two block orders

Twelve decision cells per item:

```
g23a_base        BACKGROUND → judgment
g23a_norule      BACKGROUND → EVIDENCE → judgment            (full influence, no rule)

for w in {0, 1, 25, 50, 100}:
  g23a_pre_<w>   BACKGROUND → weight rule(w) → EVIDENCE → judgment
  g23a_post_<w>  BACKGROUND → EVIDENCE → weight rule(w) → judgment
```

The rule is `conditions_v3.uniform_weight_rule` at **every** level:

> The causal weight assigned to `<evidence label>` is exactly **w%** of its normal
> evidential weight.

Prohibition and attenuation are therefore worded identically and differ in one
character run — the construction the historical near-zero sweep used, kept byte for
byte. The register's `Evidence E` template is instantiated with the item's own evidence
label in place of `Evidence E`, because the label *is* the referring expression for the
evidence block; using a bare "Evidence E" would silently drop target binding, which G18
showed is not neutral. Only the number varies.

`pre` and `post` are byte-identical multisets of blocks; only their order differs.

`w = 100` in both orders is the matched Admit anchor. `g23a_norule` is the full-
influence cell and also supplies the leverage sign; `g23a_base` supplies the zero point.

**Probes — asked as separate calls, never inside a decision run:**

| probe | cells | reads |
|---|---|---|
| `wprobe_g23a_<arm>_<w>` | 2 × 5 = 10 | the weight the model *states* it was asked for, as a percentage |
| `rule_probe_g23a_w000_pre`, `rule_probe_g23a_w000_post` | 2 | may the evidence influence the judgment? (should be NO) |
| `rule_probe_g23a_w100_pre` | 1 | may the evidence influence the judgment? (should be YES) |

The numeric probes are what makes **Outcome D** readable: a model that reports the
right number at every `w` while only `w = 0` still leaks.

## 5. Estimand — raw sign-aligned judgment points, no ratio

For sign `s = +1` if the evidence pushes the rating up and `−1` otherwise:

```text
ResInf(arm, w) = s · [ Y(arm, w) − Y(base) ]

Gap(w) = ResInf(pre, w) − ResInf(post, w)

Δ_zero = Gap(0) − mean[ Gap(1), Gap(25), Gap(50) ]
```

`ResInf` is the evidence influence still reaching the judgment under the rule.
`Gap(w)` is how much *more* of it survives when the rule is stated before the evidence
than when it follows — the G0 reversal, measured at that requested weight. Because
both arms subtract the same `Y(base)`, `Gap(w) = s·[Y(pre,w) − Y(post,w)]`; the base is
still computed and reported, because `ResInf(pre, ·)` and `ResInf(post, ·)` are the
terms a reviewer needs to see to know the gap is not an artefact of one arm sitting at
a floor.

`Δ_zero` is the primary experiment: does complete gating carry an **additional**
timing penalty beyond non-zero attenuation?

`w=100` is the matched Admit anchor, not an attenuation level, so it is reported
separately rather than averaged into `Δ_zero`.

A separate frozen descriptor checks numerical implementation rather than merely order
sensitivity:

```text
TargetDeviation(arm,w) = ResInf(arm,w) − w · Leverage
AbsTargetDeviation(arm,w) = |TargetDeviation(arm,w)|
```

These remain raw rating points and use no denominator. They prevent a zero PRE/POST gap
at 25% from being mis-described as successful 25% weighting when both arms ignore the
numerical rule. They are descriptive and do not change the primary verdict.

**No REI, no leverage-normalised ratio, no other denominator anywhere in this round.**
No trimming, no winsorisation, no post-hoc item dropping.

**Frozen exclusion criteria — exactly two:**

| | criterion | reason |
|---|---|---|
| E1 | all twelve decision cells present and parseable for the item | incomplete cases cannot produce a paired `Gap` |
| E2 | signed leverage `s · [ Y(norule) − Y(base) ] > 0` | an item whose evidence does not move its own rating has no influence to gate; this is the project's standing criterion |

Counts under each criterion are reported for every model. An item that fails a criterion
is dropped for that model's whole row, not cell by cell.

**Inference:** cluster bootstrap over independent skeletons, **seed `20260923`**,
**10,000 resamples**, percentile 95% intervals.

- per model: cluster = skeleton;
- pooled: cluster = **skeleton**, with all model observations for the same item kept
  inside the same resampled cluster.

The pooled analysis must not treat `model × skeleton` as independent because the three
model outputs share the same underlying item. The 72 skeletons are the independent
material units.

## 6. Frozen prediction

> **Complete exclusion carries an additional timing penalty.** `Gap(0)` is larger
> than the average gap under true attenuation levels `w ∈ {1,25,50}`.

Non-zero gaps are still reported individually. They are allowed to be non-zero; if they
are positive, the interpretation is “generic timing cost plus an extra categorical-
exclusion cost,” not “only zero is affected.” `w=100` remains the Admit anchor.

Primary estimand: pooled `Δ_zero`, cluster bootstrap as above.

Reported in full regardless of outcome, no selection:

- `Gap(w)` for all five weights, per model and pooled;
- `ResInf(pre, w)` and `ResInf(post, w)` for all five weights, per model and pooled;
- mean signed leverage, and the per-model exclusion counts under E1/E2;
- `Gap(1)`, `Gap(25)`, and `Gap(50)` individually, plus separate `Gap(100)` as the
  Admit anchor;
- `TargetDeviation` and `AbsTargetDeviation` for PRE/POST at every weight, so order
  symmetry cannot be mistaken for correct numerical weighting;
- stated-weight error per `w` and both permission probes, per model;
- family-level `Gap(0)` as a descriptive check that one family is not carrying it.

## 7. Gates — frozen

**Gate 1a:** pooled `Δ_zero` interval lower bound > 0.
**Gate 1b:** pooled `Δ_zero` ≥ **3.0 rating points** (the same pooled floor G18 used
for a primary contrast in raw points).
**Gate 2:** sign of `Δ_zero` positive in **at least 2 of 3** models.

| verdict | rule | consequence |
|---|---|---|
| `zero-amplified` | 1a + 1b + 2 | Outcome A. **Complete exclusion has an additional timing penalty beyond non-zero attenuation.** This is the only verdict that automatically authorises a G23B preregistration (standing gate vs retrospective cancellation). Non-zero timing gaps may still exist and must be reported. |
| `model-dependent` | 1a + 1b, not 2 | Outcome A at panel level with a named dissenting model. Reported as a panel regularity with the exception named; G23B may be preregistered only with the dissenting model named **in advance** and retained in the analysis. No checkpoint is dropped after seeing results. |
| `sub-threshold` | 1a only | Direction correct but below the frozen floor. Report the estimate and the interval honestly; **do not** promote the law and **do not** run G23B. |
| `smooth-timing` | 1a fails, and the pooled mean of attenuation gaps `Gap(1), Gap(25), Gap(50)` has lower bound > 0 | **Outcome B.** Attenuation itself has a timing gap and there is no identified extra zero penalty. This is generic prospective weighting / instruction-timing failure rather than evidence for a distinct categorical component. Reassess before mechanism work. |
| `no-replication` | 1a fails and the attenuation gaps are also consistent with zero | **Outcome C.** The fresh `w = 0` gap does not replicate. **Do not rescue it with mechanism.** Return to the stable G0 phenomenon and reassess the mainline. |

No per-cell significance is required in any model. The primary estimand is the pooled
contrast; per-model effects are reported in full.

**Outcome D** is a descriptor, not a verdict. If a `zero-amplified` or `model-dependent`
verdict coincides with every requested weight being stated within ±2 percentage points
(median absolute error), the analysis prints the dissociation explicitly:

> policy access + quantitative weighting competence ≠ ability to make the semantic
> evidence causally inert at `w = 0`.

That would connect the register's C2 (policy access ≠ enforcement) to C3 (categorical
gating) in one dataset.

## 8. Model panel — frozen, three checkpoints

**Qwen3-8B, Gemma-3-12B, Mistral-Small-24B.** The three the register names: the first
two carry the E2 dissociation, the third independently replicated the Stage 5 mechanism
and connects this round to the existing mechanism assets. Chosen before any G23A
output; not selected by expected effect size; no checkpoint swapped after seeing
results. A checkpoint that fails to load is reported by name, not replaced.

**Volume:** 12 decisions × 72 items × 3 models = **2,592 decisions**,
plus 13 probes × 72 × 3 = **2,808 probe calls** → **5,400 generations** total.
Behavioural readout (two-sentence rationale then digit expectation at a fixed
position), greedy decoding; probes are 1–8 token greedy calls.

## 9. What each outcome means for the project

| verdict | what may be claimed |
|---|---|
| `zero-amplified` | Complete exclusion is computationally different from ordinary prospective reweighting, established on fresh items and skeletons in raw rating points. The new paper story has its law; G23B becomes the next question. |
| `model-dependent` | The boundary holds at panel level with a named exception, exactly as Mistral's exception is reported elsewhere. |
| `sub-threshold` | The direction replicates; the magnitude does not reach the frozen floor. Reported as a weak effect, not a law. |
| `smooth-timing` | The timing failure is general across requested weights. Gating as a distinct object is not established; mechanism work on a gate is not justified. |
| `no-replication` | The zero-specific story is not stable enough to carry a paper. No rescue attempt. |

**Not authorised by this file:** G23B before a `zero-amplified` (or explicitly scoped
`model-dependent`) verdict; any revival of G18/addressability, G20, G21, the old G22 or
ReGround G19 as paper centres; any mechanism-first feature search.

## 10. Freeze checklist

- [x] fresh items generated (72 / 72 skeletons, 12-12 direction per family),
      disjointness from `items_v1` / `g18_v1` / `linear_v1` asserted at build time
      — `data/items/g23a_v1.jsonl`, sha256
      `03be16945cc03da60b06ec44d25f047d1e214e9e078b91f72cf583abd4eeb433`
- [x] conditions implemented and prompt assembly verified on all twelve cells and all
      thirteen probes — `src/conditions_g23a.py`, `tests/test_g23a.py`
- [x] analyzer implemented against the frozen estimator, exclusions, seed and gates —
      `src/analyze_g23a.py`
- [x] this document, the generator, the materials and the analyzer committed and
      original v1 committed/tagged before generation; corrected design must be
      committed and tagged `g23a-zero-gating-design-v2`
- [ ] only then: generation
