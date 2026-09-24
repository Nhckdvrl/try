# RQ2 near-zero sweep — stratum feasibility audit (pre-design)

**Date:** 2026-09-24
**Status:** FACT-FINDING ONLY — no prereg, no design tag, no compute (STATUS
still authorizes paper writing + novelty audit only). Quota decision pending.
**Trigger:** the design sketch in `PAPER_RQ2_BOUNDARY_REFRAME.md` §6 proposes
≈400 items stratified `FEVER SUPPORT / FEVER REFUTE / SciFact SUPPORT /
SciFact CONTRADICT`. Standing rule: verify the data line by line **before**
the numbers get frozen into a prereg.

---

## 1. Method (zero target-model compute, zero Exclude output)

Pure filtering over artifacts that already exist:

- candidates: `data/items/g24a_candidates_v1.jsonl` (13,283, frozen);
- excluded set: `data/items/g24a_v1.jsonl` (the 600 G24A items — the sweep's
  required disjointness set);
- leverage: `results/raw/g24a_mistral-small-24b_selection.jsonl`
  (39,849 rows = 13,283 × (`base`, `admit_pre`, `admit_post`)). The G24A
  selection pass scored **every** candidate, so the eligibility of every
  held-out item is already known — selection for the sweep is a filter, not a
  computation;
- eligibility recomputed by importing `src/select_g24a.py` itself
  (`TAU = 10.0`; `leverage = s·(mean(admit_pre, admit_post) − base)`, `None`
  if any value missing) → byte-identical to the frozen G24A selection rule;
- stratum from the candidates' `meta.stratum`.

No `exclude_*` row is read at any point: the selector's blindness is
preserved by construction.

## 2. Held-out pool eligibility by stratum

Remaining = candidates minus the 600 selected. Counts are items with
signed leverage ≥ τ at the stated floor (0 missing values anywhere):

| stratum | remaining | ≥0 | ≥1 | ≥2 | ≥3 | ≥5 | **≥10 (frozen τ)** |
|---|---:|---:|---:|---:|---:|---:|---:|
| fever/SUPPORTS | 6,126 | 4,346 | 2,843 | 2,588 | 2,445 | 2,224 | **1,871** |
| fever/REFUTES | 6,122 | 3,983 | 2,076 | 1,797 | 1,596 | 1,302 | **804** |
| scifact/SUPPORT | 317 | 244 | 241 | 235 | 227 | 204 | **169** |
| scifact/CONTRADICT | 118 | 46 | 41 | 35 | 33 | 26 | **1** |

Cross-check: remaining + selected per stratum reproduces the frozen pool
counts 6,326 / 6,322 / 417 / 218 (sum 13,283) exactly.

## 3. Finding 1 — `scifact/CONTRADICT` is exhausted (blocking for 4×100)

- Cell size in the frozen pool: **218** items. Of these, exactly **101** ever
  met τ = 10; G24A's frozen quota took **100** → **1 eligible item remains**
  (only 118 items remain in the cell at all).
- Even at the weakest direction-sane floor, τ ≥ 0 (admit at least moves the
  judgment in the gold direction on the selection model): **46 < 100**. The
  other 72 of 118 have *negative* signed leverage — the admitted evidence
  pushes against the gold direction — which cannot anchor a signed
  exclusion-gap estimand (nothing coherent left to exclude).
- ⇒ **the proposed 4 strata × 100 items is infeasible under any defensible
  eligibility floor.** (An unlimited floor would technically reach 118, but
  ≥62% of that cell would be direction-misaligned noise — indefensible.)

This is a property of the pool, not a power judgment: our own G24A selection
consumed the cell. The 417/218 source split is the frozen source corpus's
label structure; expanding the cell would require new data engineering outside
this prereg's authorization boundary (and STATUS authorizes no such work).

Cluster structure (secondary check — did G24A dedupe clusters?): its 600
items span **472 distinct clusters**, i.e. quotas were item-level,
first-eligible in frozen order, **not** cluster-deduplicated. Held-out
τ=10-eligible items, cluster overlap with those 472:

| stratum | items @τ=10 | distinct clusters | clusters also seen in the 600 |
|---|---:|---:|---:|
| fever/REFUTES | 804 | 512 | 168 |
| fever/SUPPORTS | 1,871 | 799 | 255 |
| scifact/SUPPORT | 169 | 150 | 60 |
| scifact/CONTRADICT | 1 | 1 | 0 |

⇒ **item-level disjointness (the design requirement) holds everywhere**;
cluster-level overlap exists and is disclosed here. Making the sweep
cluster-disjoint as well is affordable for `fever/*` and marginal for
`scifact/SUPPORT` (150 clusters vs a 100 quota, 60 already seen); it is not
required — every primary estimand is a within-item contrast, and the frozen
cluster bootstrap keeps clusters whole either way. Pin at prereg.

## 4. Options for the frozen quotas (decision pending)

| # | Strata × quota | τ floor | Total | For | Against |
|---|---|---|---:|---|---|
| **B (recommended)** | fever/S 150, fever/R 150, scifact/S 100 → **3 strata** | 10 (unchanged) | 400 | eligibility rule byte-identical to the G23A/G24A materials → the confirmatory compares like with like; FEVER carries **both** label directions, SciFact still represented; all strata comfortably powered (pools 1,871 / 804 / 169) | loses the SciFact-refute cell (disclosed pool fact, one sentence in the paper) |
| A1 | 150/150/100 + scifact/C 26 → 4 strata | 5 (global) | 426 | keeps all four source×label cells | lowers the floor for **every** cell vs the materials that produced the G23A boundary; CONTRADICT n=26 is descriptive-only |
| A2 | 150/150/100 + scifact/C 46 → 4 strata | 10 global, τ=0 only for CONTRADICT | 416 | maximally preserves the user's 4-cell sketch | **mixed eligibility floors across strata** — differential item quality, and the first reviewer question ("why is that cell's floor different?") answers with "pool exhaustion", which signals fragility |
| C | fever/S 200, fever/R 200 → FEVER only | 10 | 400 | single-source cleanest | drops SciFact entirely, though G24A showed source heterogeneity matters (C2: fever-fail / scifact-pass) |

**Recommendation: B.** Rationale: (1) the primary estimands are pooled,
within-item contrasts — a small secondary cell buys little, while a
changed or heterogeneous eligibility rule costs the one thing this
confirmatory exists to protect, comparability with G23A/G24A; (2) mixed or
relaxed floors are exactly the post-hoc-looking knob the triviality audit
exists to prevent; (3) the missing cell is an honest, one-sentence pool
artifact of our own prior selection, not a silent gap.

Regardless of choice: quotas fill **first-eligible in frozen candidate
order** (G24A discipline), shortfalls are reported and never topped up
post hoc, and gate floors / panel / `n`-power reasoning stay separate open
questions (`PAPER_RQ2_BOUNDARY_REFRAME.md` §6, items 1 and 3).

## 5. Reproduction

```bash
PYTHONPATH=src python - <<'EOF'
import json, collections, select_g24a as S
cands = {json.loads(l)["item_id"]: json.loads(l)
         for l in open("data/items/g24a_candidates_v1.jsonl")}
sel   = {json.loads(l)["item_id"] for l in open("data/items/g24a_v1.jsonl")}
rows  = S.load_rows(["results/raw/g24a_mistral-small-24b_selection.jsonl"])
# per stratum: count remaining with S.leverage(cands[i], rows[i]) >= tau
EOF
```

## 6. What this does NOT change

- RQ2's question, hypotheses, decision table, primary estimands and metric
  (`PAPER_RQ2_BOUNDARY_REFRAME.md` §3/§6) — untouched;
- no outcome data of any kind was inspected (none exists — no sweep has run);
- still: no prereg tag, no harness, no forward pass until an explicit STATUS
  flip; this file is evidence for the quota decision only.
