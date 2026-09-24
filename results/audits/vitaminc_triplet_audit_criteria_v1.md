# VitaminC zero-model triplet audit — pre-registered criteria (v1)

- Date written: 2026-09-25 (BEFORE any download, before any census output was computed)
- Scope: **zero-model** — no GPU, no LLM calls, pure-Python row census only.
- Question this audit answers (and ONLY this): can the **real-revision subset** of the
  official VitaminC release furnish **enough clean natural contrastive triplets**
  `Y+ (supporting evidence) ↔ Y0 (claim alone) ↔ Y− (opposing evidence)` for the
  candidate "Exclusion ≠ Negation" question?
- Explicit non-goals: no experiment design, no prompt writing, no effect peeking,
  no thresholds changed after seeing the data. Any threshold change must be ruled
  by the user and recorded as a dated erratum below.
- Data source (pinned): `https://huggingface.co/datasets/tals/vitaminc` (official
  release by the paper's first author; `train.jsonl`, `dev.jsonl`, `test.jsonl`).
  License: CC-BY-SA-3.0 for annotations (Wikipedia-derived), per the release LICENSE.
- Exclusion rule: **only `revision_type == "real"` rows** enter the census. Synthetic /
  FEVER-derived rows are excluded by rule, never by inspection of their content.

## Unit definitions

- **case**: one Wikipedia revision (`case_id`), expected to carry two evidence versions
  (pre-edit and post-edit). This expectation is VERIFIED, not assumed (D1).
- **group**: rows sharing `(case_id, claim)` — expected to be the same claim evaluated
  under the case's two evidence versions (D2).
- **SR-pair**: a group with ≥1 SUPPORTS row and ≥1 REFUTES row, where the supporting
  and refuting rows carry **different evidence texts**. This is the natural
  `Y+ ↔ Y−` contrast.
- **triplet**: an SR-pair plus `Y0 = claim alone` (no-evidence cell needs no data row;
  it is constructible for free for every claim).
- **N_SR**: number of distinct SR-pairs (deduplicated by `(case_id, claim)`).

## Acceptance criteria (fixed before download)

**A. Purity (hard, applies to all kept rows)**
  kept row ⇔ `revision_type == "real"` ∧ `label ∈ {SUPPORTS, REFUTES, NOT ENOUGH INFO}`
  ∧ non-empty `claim` ∧ non-empty `evidence`.
  - A1: mechanically dropped malformed real rows ≤ 5% of real rows, else **FAIL (dirty)**.
  - A2: non-empty `FEVER_id` among kept rows ≥ 1% of kept rows → **FAIL (dirty)**;
        0 < count < 1% → report, no fail (semantics of FEVER_id on real rows unverified).

**B. Volume**
  - N_SR ≥ 1000 → **CLEAN** (enough headroom above a future ≥200-style Phase-A threshold)
  - 300 ≤ N_SR < 1000 → **MARGINAL** (user rules: 升 or 杀)
  - N_SR < 300 → **KILL** (cannot support a 200-threshold funnel; 不救)
  Rationale: G26A taught that the pool must dwarf the eventual threshold; 300 is the
  smallest band where a ≥200 threshold is even arithmetically reachable.

**C. Minimality / "nearly identical" (hard)**
  Similarity of the two evidence texts of an SR-pair = `difflib.SequenceMatcher` ratio
  over whitespace-tokenized texts; statistic = median over SR-pairs.
  - median ≥ 0.90 → pass
  - 0.80 ≤ median < 0.90 → MARGINAL (user rules)
  - median < 0.80 → **KILL** (evidence pairs are not near-identical; the contrastive
    property that motivated this source is absent)

**D. Structure sanity (reported, no threshold)**
  D1 rows per case; distinct evidences per case (expect 2).
  D2 rows per (case, claim) group (expect 2) and distinct evidences per group (expect 2).
  D3 label marginals; per-split N_SR (train/dev/test) and pooled N_SR.
  D4 claim templating: fraction matching a threshold-template regex
  (`less than|more than|fewer than|over|under` + number) — reported, not gated.
  D5 claim/evidence length distributions; duplicate `(claim, evidence)` counts;
  distinct claim texts among SR-pairs; claim reuse across cases; top-page concentration.
  D6 orientation note: each SR-pair natively provides BOTH `exclude(E+)` and
  `exclude(E−)` sides for the same claim (the symmetric ± version is free by
  construction); which evidence version is pre- vs post-edit is NOT identifiable from
  the release schema alone — recorded as a known limitation, not gated.

**Verdict rule (evaluated in this order): KILL > CLEAN > MARGINAL.**
  - KILL if A1/A2 fail, or N_SR < 300, or C < 0.80.
  - CLEAN if (not KILL) and N_SR ≥ 1000 and C ≥ 0.90.
  - MARGINAL otherwise.

## Scope of pooling

All three splits are pooled for the count (the audit is about data availability, not
model training); per-split numbers are reported so a later design can restrict splits
if desired.
