# RQ2 reframe — exact semantic zero as a control boundary

**Updated:** 2026-09-24 (user-directed restructure).
**Status:** DRAFT FOR REVIEW. Supersedes the RQ2 framing in `PAPER_OUTLINE.md` §4
and `PAPER_FRAME.md` once accepted. **No experiment registered; no compute
authorized** (STATUS currently permits paper writing + novelty audit only).

---

## 1. Old framing and why it dies

Old RQ: *"Why is `w=0` harder than other weights?"* (G23A `Δ_zero` headline)

Reviewer one-liner: **"完全不用当然比部分使用严格 — zero is a stricter
requirement than partial use."** Under the triviality veto
(`PAPER_SCALE_AUDIT_2026-09-23.md` gate 2) this is fatal as a headline: the
question itself smuggles in the answer.

## 2. New RQ

> **RQ2: Is prospective exclusion a smooth evidence-weighting problem, or is
> exact semantic zero a qualitatively different control boundary?**

(模型只是随着要求的权重越来越小而越来越难执行，还是"让语义证据彻底变成零影响"
本身发生了一个类别变化？)

The decisive contrast is **0% vs 1%** — not 0 vs 50. The targets differ by one
percentage point of demanded suppression, yet the timing gap differs by
**13.86 − 5.59 = 8.27 rating points**. That directly attacks the "zero is
stricter" dismissal: 0% and 1% require *nearly identical* suppression.

## 3. Competing hypotheses (all live a priori on natural evidence)

| | Account | Predicts |
|---|---|---|
| **H1** | **Smooth suppression-demand.** Asymmetry grows as demanded suppression grows. | `Gap(w)` changes monotonically/smoothly with `w`; the largest step should sit where suppression demand changes most (100→50 = 50 points), the smallest step at 1→0 (1 point). |
| **H2** | **Generic prohibition cost.** Any "must not use this" rule is prospectively harder to execute. | Jump at `w=0` vs non-zero, **but also prospective failure at arithmetic zero** (a prohibition is a prohibition). |
| **H3** | **Semantic-nullification boundary.** Exact zero applied to the *inferred causal contribution* of semantic evidence is a qualitatively different control operation. | Flat plateau across non-zero `w`, discontinuous jump exactly at 0; no jump retrospectively; **arithmetic zero executed exactly**; policy remains accessible (probes) while failing. |

**Nuisance account H0** — *models do not implement intermediate weights at all,
so any `w>0` behaves like admit and the "boundary" is a binary-implementation
artifact* (stage-3 finding: on semantic materials the models do not grade
attenuations). H0 is separated from H3 by the arithmetic task: there,
intermediate weights **are** tracked (screened) and `w=0` is still executed
exactly — so graded control is possible when the contribution is explicit, and
the residual jump on semantic materials cannot be reduced to "cannot execute
zero".

Decision table for the confirmatory (both outcomes informative):

- **Sharp jump replicates on natural evidence** → RQ2 boundary headline licensed.
- **Curve is smooth** → the G23A boundary is downgraded; RQ2 becomes "general
  semantic weighting failure under prospective control" and must be re-audited
  (possibly folded into RQ1 as a boundary analysis). Same question, either way.

## 4. Evidence already in hand (all frozen)

### 4.1 G23A v3 weight ladder — flat, then a jump at exactly zero

`results/g23a_zero_gating_analysis.json`, design tag `g23a-zero-gating-design-v3`,
seed 20260923, 10,000-resample cluster bootstrap by skeleton,
n = 190 item-conditions / 68 clusters, panel `qwen3-8b`, `gemma3-12b`,
`mistral-small-24b`. `Gap(w) = ResInf(PRE_w) − ResInf(POST_w)` in raw
sign-aligned rating points (register §6.4).

| requested `w` | `Gap(w)` [95% CI] | demanded-suppression step into the next row |
|---:|---|---:|
| 100 (admit anchor) | −0.27 [−2.26, +1.86] | 50 points |
| 50 | +4.51 [+2.47, +6.50] | plateau |
| 25 | +4.99 [+3.09, +6.95] | plateau |
| 1 | +5.59 [+2.77, +8.36] | **1 point** |
| 0 | **+13.86 [+8.54, +19.18]** | — |

- 100→50 step ≈ +4.8 for **50** points of demanded suppression;
- 50→1 plateau (CIs overlap);
- **1→0 step = +8.27 for 1 point of demanded suppression.**

Step size does **not** track suppression demand → H1 fails descriptively on
these synthetic materials already; the confirmatory tests whether this shape
survives on source-grounded natural evidence.

Frozen contrasts (all three prereg gates passed):

- `Δ_zero = Gap(0) − mean[Gap(1),Gap(25),Gap(50)] = +8.83 [+4.39, +13.33]`;
- attenuation mean `+5.03 [+3.16, +6.83]`;
- model means all positive: qwen3-8b `+12.95 [+2.88,+23.33]`,
  gemma3-12b `+9.43 [+4.01,+14.89]`, mistral-small-24b `+4.44 [−1.03,+9.97]`
  (mistral's own CI crosses zero — scope every claim to the pooled estimate);
- `requested_weight_access_ok = true`, `dissociation_outcome_D = true`
  (the model can state the requested weight while only zero leaks);
- verdict `zero-amplified`; `Gap(100) ≈ 0` rules out a generic order effect at
  full weight.

Old-sweep converging descriptives (register E3): `gap(w=0) − mean(gap non-zero)
= +0.295 [+0.185,+0.405]` (n = 422); regression `I[w=0]×Before = +0.0955
[+0.0344,+0.1599]`, p = 0.0047.

### 4.2 Exact zero is not intrinsically difficult — the arithmetic boundary

Stage-3C P0-2, 48-item verifiable task, exact answer `base + w·delta`,
screened per item on whether the model tracks `w` at 0.25/0.5/0.75
retrospectively:

| model | items tracking `w` | `w=0` rule BEFORE | `w=0` rule AFTER | pre − post |
|---|---:|---:|---:|---:|
| Qwen3-8B | 13/48 | +0.000 | +0.000 | +0.000 |
| Gemma-3-12B | 34/48 | +0.000 | +0.000 | +0.000 |
| Mistral-24B | 29/48 | +0.000 | +0.000 | +0.000 |
| Qwen3.5-27B | 48/48 | +0.000 | +0.000 | +0.000 |
| Phi-4-mini | 16/48 | +0.000 | +0.438 | −0.438 (fails retrospectively; weakest tracker) |

**4/5 models execute prospective `w=0` exactly**; Qwen3.5-27B is exact at every
weight in both arms (register E3). This refutes H2 (generic prohibition cost)
and pins H3's object: the failure emerges **when zero must be applied to the
inferred causal contribution of semantic evidence** — not to numbers.

## 5. Triviality-veto pre-check (five gates)

1. **Treatment-does-not-contain-the-answer** — the manipulation is the
   requested number; the claimed explanation (a control boundary of semantic
   nullification) is not supplied by writing "0". **PASS.**
2. **Reviewer one-line test** — "zero is stricter" is blocked by the 0-vs-1
   contrast (1 point of demand, 8.27 points of gap) and the flat 1–50 plateau;
   "models just can't grade partial weights" (H0) is blocked by the arithmetic
   task where grading is demonstrated and zero still executed exactly.
   **PASS**, with one residual risk noted in §7 (nearest-prior searches owed).
3. **Two live accounts under the same visible task content** — on synthetic
   materials G23A already favors H3; on source-grounded natural evidence H1
   (smooth) is genuinely live, because G24A showed natural-evidence behavior
   departs from synthetic rounds (retrospective arm not distinguishable from
   zero; label-stratified differences). The confirmatory decides. **PASS.**
4. **Unexpected-result requirement** — a smooth natural-evidence curve would be
   a real (publishable-as-downgrade) surprise; sharp-vs-smooth is not
   determined by the manipulation. **PASS.**
5. **Nearest-prior audit** — instruction-position work (Findings ACL 2024)
   establishes order effects, not weight-ladder boundaries; ACL 2026 Main
   (representation learned in-context, struggles to use it) owns the *generic*
   representation-vs-deployment frame, which we must not repackage — our object
   stays **causal eligibility of future evidence under a prior policy**.
   **Searches run and archived** in `gate5_novelty_search.md` (round 1: 30+
   query families, Tables A/B; round 2: OpenReview, ACL-Anthology
   site-restricted, Semantic Scholar retry, full abstracts of the two closest
   neighbors): no owning prior in any reachable channel → **gate 5 = CLOSED
   (PASS)**, with the wording hazards in that file binding, and one final
   manual Anthology/arXiv pass at prereg-freeze time (recorded residual).

## 6. Proposed confirmatory — fresh natural near-zero sweep (design sketch)

**Not registered. No compute.** Requires its own prereg + design tag + STATUS
flip after this document is accepted.

- **Materials.** Held-out items from the frozen G24A candidate pool
  (`data/items/g24a_candidates_v1.jsonl`, 13,283 candidates; source audit
  `G24A_SOURCE_DATA_AUDIT_v1` PASS 53/53), **disjoint from the 600 selected
  G24A items** (`data/items/g24a_v1.jsonl`, sha256 `b0d02f7a…`). Selection
  outputs already exist (`results/raw/g24a_mistral-small-24b_selection.jsonl`,
  39,849 rows, `base/admit_pre/admit_post` only) → **no new selection compute**,
  and the selector never saw Exclude outcomes (blindness preserved). House rule
  applies: describe as *"disjoint, independently frozen"* materials, never as
  "fresh data".
- **Conditions.** `w ∈ {0,1,2,5,10,25,100}% × {PRE, POST}`, wording fixed
  except the number (G23A §6.3 style); `w=100` in both arms is the admit anchor
  + order-symmetry control on natural evidence (`Gap(100) ≈ 0` expected);
  plus the per-item `base` readout for signed leverage (selection guarantees
  measurable leverage, τ = 10.0).
- **Primary estimands (preregistered):**
  1. `Gap(0) − mean[Gap(1), Gap(2), Gap(5)]`
  2. `Gap(0) − Gap(1)` — the sharpest form
  with the full `Gap(w)` curve (incl. 10, 25, 100) as context.
- **Metric.** Raw sign-aligned influence points `s · (value_c − base)` as
  primary (G23A raw-points discipline; avoids the ratio instability Stage 3E
  documented under small anchors). `REI = s·(value_c−base)/|L|` secondary, for
  continuity with the G24A headline. Pin at prereg.
- **Decision table.** §3 above; both outcomes answer the same question.
- **Compute boundary.** STATUS authorizes **no** target-model compute today.
  Design work (this doc, then a prereg draft) is allowed; harness/tests/tag only
  after an explicit STATUS flip.

Open questions to resolve in the prereg draft (deliberately not decided here):

1. Panel: G23A-style minimal trio vs G24A's frozen 5-model panel with the
   selector excluded from pooled (recommended for comparability with G24A).
2. `n` and FEVER/SciFact + label-direction quotas — G24A showed
   label-stratified structure (REFUTES leaks far more than SUPPORTS), so balance
   evidence direction explicitly. **Feasibility audited 2026-09-24:** the
   `scifact/CONTRADICT` cell is exhausted by G24A's own selection (of 218 pool
   items only 101 ever met τ=10, 100 taken → **1 left**; only 46 at any
   direction-sane floor) → the sketched 4 strata × 100 is **infeasible**.
   Options + recommendation in `PAPER_RQ2_SWEEP_STRATUM_AUDIT_2026-09-24.md`;
   quota decision pending (no tag before it is made).
3. Gates: propose CI > 0 + a floor (G23A used 3.0 points) + positive model
   means 3/3 or 5/5 — set only after power reasoning, before any forward pass.

## 7. Draft finding wording (subject to confirmatory outcome)

If the boundary replicates:

> **Semantic prospective control exhibits a sharp exact-zero boundary rather
> than a smooth difficulty curve: the pre/post timing gap is flat across
> requested weights from 1% to 50% but jumps discontinuously at exactly 0% —
> although 0% and 1% require nearly identical suppression — and exact zero is
> executed perfectly when the contribution is explicitly arithmetic.**

Register §12.3 licensed form (must remain reachable verbatim):

> **Complete semantic causal exclusion shows an additional prospective cost
> even though prospective zero can be executed exactly when the contribution is
> explicit and verifiable.**

## 8. Explicit non-claims

- Not "zero is harder" as such (that framing stays dead).
- Not generic representation-vs-deployment dissociation — ACL 2026 Main owns
  that frame; our object is future-evidence causal eligibility, and every
  sentence must keep that object.
- Not "models implement non-zero weights correctly" (`TargetDeviation` is
  descriptive only; linearity of rating points in weight is an assumption).
- Not gate-vs-cancellation identification (G23B stopped carrier-invalid).
- No model-level significance claims where the model CI crosses zero
  (mistral-small-24b `Δ_zero`).

## 9. Paper-skeleton consequences

- `PAPER_OUTLINE.md` §4 / `PAPER_FRAME.md` RQ2 subsection get rewritten to this
  frame once accepted.
- RQ3 candidate = **scope of a prospective exclusion policy** (selective
  exclusion / leakage vs collateral suppression) — novelty check running; not
  registrable until that audit returns.
- G23C-R remains HOLD / NO COMPUTE (`c051821`); Stage-5 / G23C / G24B stay
  supporting evidence regardless of RQ2's outcome.
