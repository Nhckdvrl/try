# G25A preregistration — natural near-zero sweep (RQ2 confirmatory)

**DRAFT — NOT FROZEN. NOT TAGGED. NO COMPUTE AUTHORIZED.**
Born 2026-09-24 under `STATUS = paper writing + novelty audit + third-RQ
search only` (no target-model compute). **This document does not authorize
itself**: no harness, no design tag, no forward pass until (i) the §0 open
items are signed off, (ii) the §12 freeze checklist is complete with the
design tag recorded, and (iii) STATUS flips explicitly in the ledger.

**Proposed experiment id:** `G25A` / `g25` (name only — the repo reserves no
other G25; `PAPER_SCALE_AUDIT_2026-09-23.md` §"no automatic G25/G23D").

**Final design audit (user, 2026-09-24):** O1–O6 **signed**; O7 upgraded to
**mandatory** (no-model power/sensitivity note before tag); a
**positive-weight gradedness diagnostic added** (§6 — zero new cells, not a
gate); H0/interpretation wording corrected so H0 stays live on the semantic
domain (§1/§8). Cleared for **implementation → tests → freeze/tag → STATUS
flip** once O7's note and §12 are complete. This is the designated **first
compute of the project** after the STATUS flip.

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

## 0. Open items — O1–O6 signed (user, 2026-09-24); O7 **completed** 2026-09-24 (§7 power note)

| # | Item | Proposal (defaults, until overruled) |
|---|---|---|
| O1 | Panel | G24A's four non-selector models as the pooled primary: `qwen3-8b`, `gemma3-12b`, `llama31-8b`, `qwen35-9b`. `mistral-small-24b` is the pool's selector and is excluded from pooled inference (G24A discipline); its existing base/admit outputs stay reference-only. |
| O2 | `norule` cell | **Include** (evidence, no rule — separates "any ruling sentence" cost from weight effects; G23A precedent). 16 cells/item. |
| O3 | Probes | G23A-style requested-weight-access probe, `pre` arm only, at `w=0` and `w=100` (≤ 2 probe cells/item). |
| O4 | Floors | Both primary gates: CI low > 0 **and** point ≥ 3.0 (G23A floor). Sufficiency: ≥ 360/400 items usable on ≥ 3/4 pooled models. RuleAcc ≥ 0.8. |
| O5 | Naming | files `data/items/g25_v1.jsonl`, raw `results/raw/g25_<model>.jsonl`. |
| O6 | Seed | `20260924` (G23A used `20260923`). |
| O7 | Power/sensitivity note — **DONE 2026-09-24** (was: mandatory before freeze, final design audit "不要 optional") | No-model detectable-effect note at 400 items / 342 clusters from the frozen G23A CI: SE 1.017, MDE80 2.85 pts, floor-3.0 resolvable to ≤1.5× SE inflation, +8 expected effect ≥97.5% at 2× — full table + caveats in §7; reproducible via `src/note_g25a_power.py` → `results/audits/g25a_power_note_v1.json`. |

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
| H0 | Models don't grade intermediate weights at all — or parse the semantic rule **categorically** (zero vs nonzero) | any `w>0` ≈ admit, or all positive `w` collapse to one common response. **Stays live for the semantic domain:** the arithmetic task proves only *capability under explicit, verifiable contributions* — it cannot show that semantic 1/2/5/25% are quantitatively executed. H0 vs H3 is decided by the §6 gradedness diagnostic, **not** by arithmetic. |

Both outcomes informative (reframe §3 decision table), now with the
**three-way interpretation split mandated by the final design audit** — a
replicated zero-jump is read *through the §6 gradedness diagnostic*:

1. **boundary + graded positive-weight response** → strong claim: a sharp
   zero boundary *over graded* semantic weighting;
2. **boundary + flat positive-weight response** → discontinuity still
   licensed, but the mechanism sentence **downgrades to a categorical
   zero-vs-nonzero semantic-control regime** — never "a dedicated semantic
   nullification operation" (blocks the reviewer one-liner: *"you only found
   that models treat 0 and nonzero as two linguistic categories"*);
3. **smooth response** → boundary claim killed; RQ2 downgraded and
   re-audited (reframe §3).

The split uses **no new cells** — it is computed from conditions already in
this design (§6).

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

**Secondary gradedness diagnostic (added by the final design audit; zero new
cells; not a gate):**

```text
Resp(w)   = mean(ResInf_pre_w, ResInf_post_w)              level at weight w
GradedPos = Resp(100) − mean[ Resp(1), Resp(2), Resp(5) ]   low-end attenuation
```

Report `Resp(w)` for all seven weights with cluster-bootstrap CIs (per-arm
table in the supplement) and describe monotonicity — **never assume
rating-point linearity in weight** (register §8 discipline; the
`TargetDeviation` precedent is descriptive only). `GradedPos` CI strictly
above 0 = low weights genuinely carry less influence → graded control exists
on semantic materials; `GradedPos` ≈ 0 with a flat `Resp(w)` = categorical
zero-vs-nonzero parsing. Feeds the §1/§8 interpretation split directly.
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

**O7 power/sensitivity note — COMPLETED 2026-09-24** (design-stage, no
simulation, zero model calls; reproducible: `src/note_g25a_power.py` →
`results/audits/g25a_power_note_v1.json`). Frozen input: G23A Δ_zero
cluster-bootstrap CI [+4.39, +13.33] at n = 190 / 68 clusters →
SE_G23A = 2.281; per-cluster variance transferred to G25A's 342 clusters →
**SE_G25A = 1.017** (assumption: equal per-cluster variance across material
sets — explicitly stress-tested below).

| SE inflation | SE | MDE80 (pts) | P(CI low>0 \| true 3.0) | P(CI low>0 \| true +8) |
|---|---|---|---|---|
| 1.0× | 1.017 | **2.85** | 0.84 | ~1.00 |
| 1.5× | 1.525 | 4.27 | 0.50 | 0.999 |
| 2.0× | 2.034 | 5.70 | 0.31 | 0.976 |

- **The O4 floor (3.0) is not arbitrary:** it stays CI-resolvable under up
  to ~1.5× SE inflation (≈2.3× variance). At equal variance, n = 400 / 342
  clusters is exactly what pulls MDE80 (2.85) *below* the floor — G23A's
  own 68 clusters would leave MDE80 = 6.39 > floor, i.e. unresolvable.
- The design-stage expected effect (~+8; Δ_zero +8.83, Gap(0)−Gap(1) = 8.27)
  is detected with ≥ 97.5% probability even under 2× SE inflation.
- Honest fallback: if realized variance inflates beyond 2× **and** the true
  effect is small (< ~5.7 pts), §8's `unresolved` branch exists for exactly
  this case — reported, never forced.

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
| `exact-zero-boundary` | I1 I2 S1 **G1 G2** (+G3 for cross-model sentence) | Finding 2 upgrade licensed, **interpretation split by §6 GradedPos**: graded positives → "sharp zero boundary over graded semantic weighting"; flat positives → discontinuity licensed but mechanism wording = **categorical zero-vs-nonzero semantic control** (never "nullification operation"); ship the `Resp(w)` table either way. Register §12.3 form remains the verbatim licensed claim; word strictly to the object (causal eligibility of future evidence). |
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
here. **Freeze-time manual pass COMPLETED 2026-09-24 — novelty residual
closed** (record: `gate5_novelty_search.md` §"Freeze-time manual pass":
ACL-2026 official event listing 6,422 titles / 6,365 abstracts three-tier
screened + arXiv 4 phrase-query families (41 hits) + OpenAlex/S2 retries —
every hit read, no owning or near-owning prior; S2/OpenAlex 429 and
websearch-down coverage caveats on record).

## 11. Authorization boundary

**Today (STATUS):** this draft, its review, and edits to it. Nothing else.

**Before any G25A forward pass** (allowed only after an explicit STATUS flip):

1. §0 open items signed off; §12 checklist complete with design tag recorded;
2. dispatch/conditions module + items build + selection + analyzer + tests
   implemented and green;
3. full suite green (baseline at tag time: **418 passed / 953.65 s with
   zero `--ignore` flags**, 2026-09-24 — a strict superset of the earlier
   334 / 849 s five-flag baseline; those five flags only skipped 51 tests
   that pass unconditionally, so the zero-ignore figure is stated).

**Compute budget (to be authorized by the STATUS flip, stated up front):**
≤ 400 items × 16 cells × 4 models = **25,600** condition rows, plus ≤ 3,200
probe rows (O3) → **≤ 28,800** rows, four models, no retries-by-outcome.

### 11.4 Pre-tag clarifications (recorded 2026-09-24, design-stage; none
adds compute, cells, models or outcomes)

1. **RuleAcc (I2) is defined operationally**: the pooled fraction of §4
   requested-weight-access probe rows (`wprobe_g25_pre_w000`,
   `wprobe_g25_pre_w100`) whose parsed numeric answer lies within
   `PROBE_TOL_PP = 2.0` percentage points of the requested weight.
   Unparsed rows stay in the denominator and count against RuleAcc (no
   silent dropping). Absent probe data fails I2 → verdict `order-artifact`
   (integrity event), *not* `unresolved`.
2. **Block headers are `CLAIM` / `EVIDENCE E`** (G24A materials lineage;
   §3's `BACKGROUND`/`EVIDENCE` notation is schematic). The rule sentence is
   its own `RULING` block, rendered between `CLAIM` and `EVIDENCE E`; the
   `g25_norule` control cell renders `CLAIM` + `EVIDENCE E` with no
   `RULING` block. Prompt-diff tests pin: pre/post cells differ in block
   order only, all 15 non-base cells share one tail, one number per rule.
3. **Cluster key = `source/cluster`** (G24A namespacing on `meta.source` +
   `meta.cluster`). This reproduces the §5 dry-run anchors exactly: 342
   clusters over the 400 selected items, 126 shared with G24A; the cluster
   bootstrap resamples whole clusters under this key (seed 20260924,
   B = 10,000).
4. **§8 row precedence is top-down**: `boundary-not-replicated` (G1 fails
   while Gap(0)'s CI lies strictly above 0) is evaluated *before*
   `partial-boundary`; a precheck that no evaluable data exists yields
   `unresolved` and is not an integrity event; failed I2 (probe data absent)
   yields `order-artifact`.
5. **Gradedness can never gate (user ruling, this session)**: `classify()`
   takes exactly `(i1, i2, s1, g1, g2, gap0)` — no gradedness input;
   `Resp(w)`/`GradedPos` are §6 interpretation labels shipped alongside a
   verdict that is byte-identical under graded vs flat positives. Pinned by
   an explicit signature-lock test.

## 12. Freeze checklist and record

- [x] §0 open items O1–O7 signed off (2026-09-24)
- [x] manual nearest-prior pass (Anthology/arXiv) done and recorded (2026-09-24, gate5 §"Freeze-time manual pass")
- [x] rule/condition byte-strings pinned; identity tests green (`tests/test_g25a.py`: rule == `conditions_v3.uniform_weight_rule`, same function object as G23A's, exact one-number wording; only-number-changes; pre/post order-only; single tail)
- [x] selection determinism test green (`0b38e0837ed9fd60`, n=400, 150/150/100; real full-walk rerun + census regression both green)
- [x] items file built; sha256 + strata counts recorded here: `data/items/g25_v1.jsonl` sha256 = `7c6993244d7808d8e65696c00a55f4fc14c7f3011f34f0266e450f1367173147`, strata fever/SUPPORTS 150 + fever/REFUTES 150 + scifact/SUPPORT 100 = 400, byte-identical to candidates, 342 `source/cluster` keys, 126 shared with G24A (disclosed as-is, no cluster-disjointness demanded — user decision)
- [x] analyzer + outcome-map tests green (both-direction sign test; usability drops; RuleAcc; §8 10-branch decision order incl. row precedence)
- [x] gradedness diagnostic (`Resp`/`GradedPos`) implemented + tested (signature-lock: `classify` has no gradedness input; graded vs flat e2e produce the identical verdict, only the §6 label differs)
- [x] **power/sensitivity note recorded (O7 — mandatory, no-model; done 2026-09-24, §7 + `results/audits/g25a_power_note_v1.json`)**
- [x] full test suite green at updated baseline: **418 passed / 953.65 s,
  zero `--ignore` flags** (2026-09-24; = 385 pre-existing + 33
  `tests/test_g25a.py`; supersedes the 334 / 849 s five-flag baseline)
- [x] **design tag assigned:** `g25a-near-zero-design-v1` (recorded here +
  ledger; git tag points at this commit — no G25A forward pass exists
  before it)
- [ ] **STATUS flip recorded** (ledger entry authorizing ≤ 28,800 rows)

No boxes may be checked after the design tag is set (prereg freeze rule);
this file is immutable from the tag onward.
