# G25A preregistration — natural near-zero sweep (RQ2 confirmatory)

**DRAFT — NOT FROZEN. NOT TAGGED. NO COMPUTE AUTHORIZED.**
Born 2026-09-24 under `STATUS = paper writing + novelty audit + third-RQ
search only` (no target-model compute). **This document does not authorize
itself**: no harness, no design tag, no forward pass until (i) the §0 open
items are signed off, (ii) the §12 freeze checklist is complete with the
design tag recorded, and (iii) STATUS flips explicitly in the ledger.

**Proposed experiment id:** `G25A` / `g25` (name only — the repo reserves no
other G25; `PAPER_SCALE_AUDIT_2026-09-23.md` §"no automatic G25/G23D").

Parent documents (all frozen or closed):

- `PAPER_RQ2_BOUNDARY_REFRAME.md` — question, H1/H2/H3/H0, decision table;
- `PAPER_RQ2_SWEEP_STRATUM_AUDIT_2026-09-24.md` — feasibility + **Option B
  quotas (user decision)**;
- `gate5_novelty_search.md` — nearest prior, CLOSED as PASS, wording hazards;
- `PREREGISTRATION_G23A_ZERO_GATING.md` + `PREREGISTRATION_G24A_NATURAL_EVIDENCE.md`
  — the two designs this one crosses.

**One-sentence design identity:** *G23A's weight-ladder conditions, byte for
byte, run on G24A's source-grounded natural materials — exactly one factor
changes (materials), so the boundary question is asked of nature rather than
of our synthetic rounds.*

---

## 0. Open items to sign off before freeze

| # | Item | Proposal (defaults, until overruled) |
|---|---|---|
| O1 | Panel | G24A's four non-selector models as the pooled primary: `qwen3-8b`, `gemma3-12b`, `llama31-8b`, `qwen35-9b`. `mistral-small-24b` is the pool's selector and is excluded from pooled inference (G24A discipline); its existing base/admit outputs stay reference-only. |
| O2 | `norule` cell | **Include** (evidence, no rule — separates "any ruling sentence" cost from weight effects; G23A precedent). 16 cells/item. |
| O3 | Probes | G23A-style requested-weight-access probe, `pre` arm only, at `w=0` and `w=100` (≤ 2 probe cells/item). |
| O4 | Floors | Both primary gates: CI low > 0 **and** point ≥ 3.0 (G23A floor). Sufficiency: ≥ 360/400 items usable on ≥ 3/4 pooled models. RuleAcc ≥ 0.8. |
| O5 | Naming | files `data/items/g25_v1.jsonl`, raw `results/raw/g25_<model>.jsonl`. |
| O6 | Seed | `20260924` (G23A used `20260923`). |
| O7 | Power check (optional, pre-freeze) | bootstrap-based detectable-effect note using G23A resampling constants; dry-run below already implies ≫ G23A's cluster count. |

---

## 1. Scientific question

> **RQ2: Is prospective exclusion a smooth evidence-weighting problem, or is
> exact semantic zero a qualitatively different control boundary?**

Decisive contrast **0% vs 1%** — one percentage point of demanded suppression,
8.27 rating points of timing gap on G23A (13.86 vs 5.59). The confirmatory
asks whether that shape survives on source-grounded natural evidence.

| | Account | Predicts on this sweep |
|---|---|---|
| H1 | Smooth suppression-demand | `Gap(w)` graded with `w`; biggest step 100→50, smallest 1→0 |
| H2 | Generic prohibition cost | jump at 0 vs any non-zero, **also** at arithmetic zero (refuted already by Stage-3C: 4/5 models exact at prospective `w=0`) |
| H3 | Semantic-nullification boundary | flat plateau 1–50, discontinuous jump exactly at 0; `Gap(100)≈0`; arithmetic zero exact |
| H0 | Models don't grade intermediate weights at all | any `w>0` ≈ admit — separated from H3 by the arithmetic task (grading exists there) |

Both outcomes informative (reframe §3 decision table): sharp jump → boundary
headline; smooth → boundary downgraded honestly and RQ2 re-audited (see §8).

## 2. Data (audited and frozen; nothing new is built)

- **Materials:** `data/items/g24a_candidates_v1.jsonl` — 13,283 candidates,
  source audit `G24A_SOURCE_DATA_AUDIT_v1` PASS 53/53, source manifest and
  gold labels already frozen. Strata via `meta.stratum`.
- **Disjointness:** selection excludes every item_id in
  `data/items/g24a_v1.jsonl` (the 600; sha256 `b0d02f7a…`) — enforced in code
  and tested. House wording: *"disjoint, independently frozen"* materials,
  **never** "fresh data" (G18 rule).
- **Selection outputs reused:** `results/raw/g24a_mistral-small-24b_selection.jsonl`
  (39,849 rows = 13,283 × {`base`,`admit_pre`,`admit_post`}) — selection for
  this sweep is pure filtering; **no new selection compute of any kind**, and
  no `exclude_*` row is ever read (blindness by construction).
- **Cluster keys:** `meta.cluster` (Wikipedia page / source doc) — frozen,
  used for the bootstrap and for the overlap disclosure below.

## 3. Items and conditions

**Cells per item (16, O2):**

```text
g25_base        BACKGROUND -> judgment                      (no critical evidence)
g25_norule      BACKGROUND -> EVIDENCE -> judgment          (full influence, no rule)
g25_{arm}_{w}   BACKGROUND -> [rule | EVIDENCE] -> [EVIDENCE | rule] -> judgment
                arm ∈ {pre, post};  w ∈ {0, 1, 2, 5, 10, 25, 100}%
```

- `pre`: rule before evidence; `post`: rule after evidence (G23A layout).
- Rule string = `conditions_v3.uniform_weight_rule(item, w)` **verbatim**:
  `"RULING\nThe causal weight assigned to {critical_label} is exactly
  {w*100:g}% of its normal evidential weight."` — one sentence, one number
  varying (G23A construction; `critical_label = "evidence E"`).
- The candidates' precomputed `admit_rule`/`exclude_rule` strings (G24A
  wording lineage) are **not used** — deliberate: the sweep changes materials,
  not rule wording, so any difference from G23A is attributable to nature.
- Same question, output spec and answer format across all cells (test).

## 4. Models (O1)

Pooled primary: **`qwen3-8b`, `gemma3-12b`, `llama31-8b`, `qwen35-9b`** —
G24A's four non-selector models (G24A raw files confirm the panel ran).
Selector `mistral-small-24b` excluded from pooled inference because item
selection conditioned on its own Admit leverage (G24A §4 discipline); its
existing selection outputs are reported as reference leverage only. No other
model, no size sweep, no layer/site/carrier additions.

## 5. Selection rule (Base/Admit only)

- **Eligibility:** `select_g24a.leverage(item, rows) ≥ TAU = 10.0`, all three
  values present — byte-identical rule function, imported, not reimplemented.
- **Quotas (Option B, user-confirmed):** `fever/SUPPORTS 150`,
  `fever/REFUTES 150`, `scifact/SUPPORT 100` → **n = 400**.
  (`scifact/CONTRADICT` dropped: 1 eligible item remains at τ=10 — pool
  exhaustion documented in the stratum audit; the drop is a pre-outcome pool
  fact, disclosed in the paper in one sentence.)
- **Order:** candidates file frozen order, first-eligible fill, shortfall
  reported and **never** topped up post hoc.
- **Dry-run anchor (2026-09-24, executed under this draft for power/design
  reasoning only):** quotas fill **400/400** (150/150/100), **342 distinct
  clusters**, leverage min/p50/max = 10.0 / 36.8 / 99.9, sha256[:16] of the
  sorted selected id list = **`0b38e0837ed9fd60`**. 126 of the 342 clusters
  are shared with the G24A 600 (item-level disjointness holds; G24A's own
  selection was item-level first-eligible, 600 items / 472 clusters — cluster
  overlap is disclosed, not hidden; all primaries are within-item contrasts
  and the bootstrap keeps clusters whole). The harness re-run must reproduce
  this id list exactly (determinism test) and record the authoritative sha.

## 6. Estimands

Per item × model, `s` = gold-label sign (identical mapping code path as
G0/G24A), values on the 0–100 scale. **Primary metric: raw sign-aligned
points** (G23A discipline; avoids ratio instability documented by Stage 3E).

```text
ResInf_c = s · (value_c − base)                       raw points
Gap(w)   = ResInf(pre_w) − ResInf(post_w)             timing gap at weight w
L        = mean(w100_pre, w100_post) − base            anchor leverage (w=100)
```

**Co-primary contrasts:**

1. `Δ_local0 = Gap(0) − mean[ Gap(1), Gap(2), Gap(5) ]` — the local
   boundary contrast;
2. `Gap(0) − Gap(1)` — the sharpest 0-vs-1 form.

Context curve (reported, not gated): `Gap(10), Gap(25), Gap(100)`.
Secondary: `REI_c = s·(value_c − base)/|L|` (winsorised ±3, G0/G24A
convention), for continuity with the G24A headline.
Usability: all 16 values present and `sL > 0` for that model, else unusable
**for that model only**, reported `n/n_total` — never filtered post hoc on an
outcome. Note: `w ∈ {2,5,10}%` are new cells by design (G23A measured
{1,25,50}); the plateau interpolation for Δ_local0's expectation is an
assumption the sweep exists to test, not a license.

## 7. Frozen inference

- **Cluster bootstrap** over `meta.cluster`: each resample draws K clusters
  with replacement (K = observed cluster count) and pools all rows — items ×
  models — of the drawn clusters; a cluster never splits across the resample
  (tested, G24A check #6).
- `seed = 20260924`, `B = 10,000`, percentile 95% CIs, two-sided bootstrap
  p (`boot_p`, G0 convention).
- **Co-primary gate logic is intersection–union:** both co-primaries must
  pass §8 G-gates → no multiplicity correction; single-passing outcomes fall
  into `partial-boundary` and are claimed only for the passing contrast.
- Strata reported: pooled-4, per model, per stratum (3), per label direction;
  per-stratum numbers are descriptive unless explicitly gated.
- No item removed after results exist; reruns only for mechanical
  incompleteness, never selective by outcome.

**Power note (design-stage, no simulation):** dry-run gives 400 items /
342 clusters with within-item paired contrasts — vs G23A's n=190 / 68
clusters whose Δ_zero CI was [+4.39, +13.33]. Under replication of the G23A
shape the expected Δ_local0 is ≈ +8 (plateau ~5 interpolated); the O4 floor
of 3.0 sits well inside the expected CI. Optional O7 before freeze.

## 8. Outcome map

Order of evaluation: **integrity → sufficiency → co-primaries.**

- **I1** `Gap(100)` 95% CI contains 0 (order symmetry at the anchor);
  **I2** pooled RuleAcc ≥ 0.8 (O4).
- **S1** ≥ 360/400 items usable on ≥ 3/4 pooled models.
- **G1** Δ_local0: CI low > 0 and point ≥ 3.0; **G2** Gap(0)−Gap(1): same.
- **G3** ≥ 3/4 pooled model means positive on each primary (model-level
  claims only where the model CI excludes 0).

| Verdict | Conditions | Required action |
|---|---|---|
| `exact-zero-boundary` | I1 I2 S1 **G1 G2** (+G3 for cross-model sentence) | Finding 2 upgrade licensed; register §12.3 form remains the verbatim licensed claim; word strictly to the object (causal eligibility of future evidence). |
| `boundary-not-replicated` | I ok, S1 ok, **G1 fails** while `Gap(0)>0` | Boundary claim **withdrawn for natural materials**; RQ2 re-audited as "smooth semantic weighting failure under prospective control" (possibly folded into RQ1); §12.3 sentence re-scoped to its actual evidence base or withdrawn pending register revision. Same question, honest answer. |
| `partial-boundary` | I ok, S1 ok, exactly one of G1/G2 passes | Claim strictly the passing contrast; the word "boundary" only if G1 passes; no plateau sentence unless the full curve supports it. |
| `no-natural-gap` | I ok, S1 ok, `Gap(0)` CI contains 0 | G23A timing gap does not manifest on natural materials at zero (G24A measured levels, not this timing shape); Finding 2 rescoped to synthetic; report as-is. |
| `order-artifact` | I1 or I2 fails | No claim; integrity investigation before any interpretation. |
| `unresolved` | S1 fails, or CIs straddle gates ambiguously | Report everything; no verdict. |

## 9. Controls and integrity checks

1. **One sentence, one number:** rule strings differ across weight cells only
   in the percentage; pre/post forms character-identical (construction
   constant + test, G24A check #1 pattern).
2. **Selector blindness:** selection path provably reads no `exclude_*` kind
   (existing test reused) and never touches sweep outputs (none exist at
   selection time).
3. **Disjointness test:** selected ∩ G24A-600 = ∅.
4. **Selection determinism test:** harness selection reproduces dry-run id
   list (sha256[:16] `0b38e0837ed9fd60`, n=400, quotas exact).
5. **G24A/G0 non-regression:** existing item files and dispatch unchanged
   (regression over frozen first records).
6. **Same readout, same tail:** all cells share question/output spec/format
   (test); digit-mass diagnostics reported.
7. **Sign convention:** `s` identical to G0/G24A mapping (analyzer test, both
   directions).
8. **Cluster integrity** in the pooled bootstrap (test).
9. **No scope creep:** no new layer/site/model/carrier; no probe beyond O3;
   no LLM-generated data or judgments.
10. **Wording hazards** of `gate5_novelty_search.md` are binding on every
    draft sentence (never generic "representation-vs-deployment"; the object
    is the causal eligibility of future evidence under a prior policy).

## 10. Relation to nearest prior

Gate 5 **CLOSED as PASS** (`gate5_novelty_search.md`: round 1, 30+ query
families, Tables A/B; round 2, OpenReview + ACL-Anthology site-restricted +
S2 + full abstracts of the two closest neighbors): no owning prior for a
*weight-ladder boundary under prospective exclusion*. Instruction-position
work establishes order effects, not weight-ladder shapes; ACL 2026 Main owns
the generic representation-vs-deployment frame and is **not** repackaged
here. **Residual:** one manual Anthology/arXiv pass at freeze (session
websearch unavailable — coverage caveat on record).

## 11. Authorization boundary

**Today (STATUS):** this draft, its review, and edits to it. Nothing else.

**Before any G25A forward pass** (allowed only after an explicit STATUS flip):

1. §0 open items signed off; §12 checklist complete with design tag recorded;
2. dispatch/conditions module + items build + selection + analyzer + tests
   implemented and green;
3. full suite green (current baseline: 334 passed / 849 s with the five
   standard `--ignore` flags).

**Compute budget (to be authorized by the STATUS flip, stated up front):**
≤ 400 items × 16 cells × 4 models = **25,600** condition rows, plus ≤ 3,200
probe rows (O3) → **≤ 28,800** rows, four models, no retries-by-outcome.

## 12. Freeze checklist and record

- [ ] §0 open items O1–O7 signed off
- [ ] manual nearest-prior pass (Anthology/arXiv) done and recorded
- [ ] rule/condition byte-strings pinned; identity tests green
- [ ] selection determinism test green (`0b38e0837ed9fd60`, n=400, 150/150/100)
- [ ] items file built; sha256 + strata counts recorded here
- [ ] analyzer + outcome-map tests green (both-direction sign test)
- [ ] full test suite green at updated baseline
- [ ] **design tag assigned:** ____________________ (recorded here + ledger)
- [ ] **STATUS flip recorded** (ledger entry authorizing ≤ 28,800 rows)

No boxes may be checked after the design tag is set (prereg freeze rule);
this file is immutable from the tag onward.
