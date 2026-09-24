# HoVer Zero-Model Structural Audit — 2026-09-24

**Ordered by:** user design audit of 2026-09-24 (G26A `DO NOT FREEZE` banner,
item 2): "HoVer zero-model structural audit FIRST … if not clean: do not
rescue HoVer — evaluate MuSiQue directly."

**Verdict: PASS at the structural layer.** 4,105 post-rule survivors in 2,683
title-pair clusters (2,710 hpqa clusters) — **13.4× the planned selector floor
of 200** — with A/B sentences reconstructable under a validated deterministic
reconstruction of the official sentence indexing.

**Zero model calls. Deterministic (no RNG). STATUS untouched — this document
authorizes no compute.** Record of truth = `src/audit_hover.py` →
`results/audits/hover_structural_v1.json` (rerun: `python3 src/audit_hover.py`).

---

## 1. Sources (all pinned in `data/external/source_manifest.json`, entry
`hover_v1.1`)

| file | bytes | sha256 (first 16) | note |
|---|---|---|---|
| `hover_train_release_v1.1.json` | 9,205,582 | `1f1cd57abd616fa0` | 18,171 claims |
| `hover_dev_release_v1.1.json` | 2,153,439 | `67c14858f2d7fcdb` | 4,000 claims |
| `hover_test_release_v1.1.json` | 898,814 | `c58e7fc59b496221` | **blind** (no labels/num_hops/supporting_facts) → excluded everywhere |
| `wiki_wo_links.db` | 2,156,273,664 | `c37ee397916ec0bf` | official evidence DB, frozen 2020-11-03, `nlp.cs.unc.edu` |

Byte sizes match the GitHub API listing exactly. License: CC BY-SA 4.0
(official HF card `hover-nlp/hover`); Wikipedia-derived text under CC BY-SA.
Raw cache is gitignored per house policy; the manifest carries URL+sha256.

Schema: `uid / claim / supporting_facts=[[title,sent_idx],…] / label ∈
{SUPPORTED, NOT_SUPPORTED} / num_hops / hpqa_id`. Evidence **text is not in
the JSONs** — `supporting_facts` are pointers into `wiki_wo_links.db`.

## 2. Method

Funnel (claims level): 2-hop → `n_sf==2` → distinct titles → materialize
pages → reconstruct sentences → apply structural rules:

```
R1 orientation-unique bridge   (exactly one of the two sentences mentions the
                                other's page entity)
R2 8 ≤ words ≤ 80              (both sentences)
R3 single-sentence leak recall < 0.9
```

**Sentence reconstruction.** The DB stores *unsplit prose*; gold indices were
annotated against a CoreNLP-style split (HoVer README: "We use Corenlp to
split the sentences"). We reconstruct with a deterministic abbreviation-aware
splitter (`smart_sents`, v2) that refuses to break after single-letter name
initials (`Robert W. Derminer`, `William S. Hart`) and common abbreviations.
It is an APPROXIMATION, validated three ways (T8): gold-vs-rotated controls,
v1-naive baseline, and manual one-by-one reads.

**Lookup quirk.** DB ids are NFD-normalized, JSON titles are NFC: a naive
exact match reports 249 false missings (all diacritic names, e.g.
`Marko Dmitrović`). Lookup chain raw → NFD → NFC recovers **all 9,189/9,189**
funnel titles (0 true missing).

## 3. Claims-level results (C1–C6)

- Funnel: train 6,153 (S 4,479 / NS 1,674) + dev 759 (S 355 / NS 404)
  = **6,912** candidates. (`n_sf != num_hops` for ~31% of 2-hop claims —
  the `n_sf==2` rule is load-bearing, not cosmetic.)
- Clusters: 4,798 title-pairs (3,204 singletons, max freq 7), 4,843 hpqa_ids.
- Labels: only `SUPPORTED(+1) / NOT_SUPPORTED(−1)` — sign mapping stable, no
  unmapped labels.
- Integrity: uids unique within/across splits; claim cross-overlap 0;
  **hpqa_id cross-split overlap 77** (one HotpotQA question → multiple claims;
  train has 6,109 unique hpqa for 18,171 claims) → cluster unit =
  hpqa_id/title-pair, and any future draw should stay **within one split**.
- Comparison-regex flags 6.3% of funnel claims as possible parallel topology
  (rough proxy; final topology = T3/T4).

## 4. Text-level results (T1–T8)

- **T1 coverage:** 9,189/9,189 found (raw 8,940 + NFD 249). True missing: 0.
- **T2 sentences:** 6,832/6,912 materialized; **80 OOB (1.16%)** excluded
  (gold index beyond our split ⇒ page-version or segmentation mismatch).
  Words: median 23, p5 10, p95 45, max 152.
- **T3 orientation (of 6,832):** `sf0→sf1` 4,195 (61.4%), `sf1→sf0` 75 (1.1%),
  `both` 135 (2.0%), `neither` 2,427 (35.5%).
  → among orientation-unique items the **listed order is chain order in
  4,195/4,270 = 98.2%** — but the 75 reversals mean A/B orientation must be
  set **by mention direction, never blind list order**.
- **T4 topology:** bridge 4,405 (64.5%); orientation-unique 4,270. The
  `neither` bucket absorbs parallel/comparison items *and* alias-bridges our
  strict exact-title matching misses — the chain rule is deliberately
  conservative.
- **T5 leak:** mean max single-sentence claim recall 0.521; ≥0.9: 77 items;
  **=1.0: 36** (one sentence contains every claim content word — near
  paraphrase) → excluded by R3.
- **T8 alignment controls** (gold vs rotated-neighbour index):

  | label | n | recall gold/rot | bridge gold/rot |
  |---|---|---|---|
  | SUPPORTED | 4,778 | 0.536 / 0.283 | 0.609 / 0.166 (3.7×) |
  | NOT_SUPPORTED | 2,054 | 0.488 / 0.264 | 0.728 / 0.203 (3.6×) |

  v2 beats the v1-naive baseline on gold recall AND bridge for both labels
  (v1 bridge: 0.554 / 0.664) → v2 is the reconstruction of record.
- **T7 reuse:** 9,232 unique (title, idx) evidence slots, max reuse 7, 63
  slots reused ≥5 — minor cross-item sentence sharing; handled by clustering.

## 5. Defect taxonomy (every item below was read line-by-line)

**Class A — splitter drift (our reconstruction), fixed in v2.**
`Micah Ohlman` (dev `71006039`): v1 split at `Micah D.` / `William S.` →
gold idx 3 pointed at a fragment; v2 idx 3 = *"While attending UNLV, Ohlman
earned a spot on the … 1992–93 UNLV Runnin' Rebels basketball team…"* — exact
match to the claim (basketball vs claim's "baseball"). `Rob Tyner`
(`961688da`): v1 produced the fragment `Robert W.` as sentence 0; v2 correct.
Residual Class A = the 80 OOB (excluded by rule).

**Class B — DB page text shorter than at annotation time.**
`Harrier (dog)` stored text *ends mid-clause* (`…of the hound class,`).
`Traveling Wilburys Vol. 3` page has a single stored sentence while gold
index = 1 → OOB. `Gary Sinise` (`c679a81c`) page has only bio + awards —
*the The-Stand sentence is absent entirely*, so its gold B is useless; this
item has **no bridge direction and is excluded by R1**. Class B never reaches
the survivor set uncaught (OOB by rule, or killed by R1/R2).

**Class C — claim/gold noise (structural layer cannot fix; selector gates are
the empirical backstop).**
1. **`961688da` (dev, needs human adjudication):** label `SUPPORTED` for
   claim *"Gregg Rolie and Rob Tyner, are not a keyboardist."* while its own
   gold A says Rolie *"is an American singer and keyboardist"* — apparent
   claim/label/gold contradiction. Already excluded from survivors (no
   bridge direction).
2. `b065d90b` (dev): *"…the manager of the Aston Villa that began at Aston
   Villa Football Club"* — parse-dependent garble; defensible as SUPPORTED
   under a charitable reading. Chain-clean otherwise.
3. Decoy-A pattern in NOT_SUPPORTED (`c0c18f1c` Robsahm: gold A is a bio
   sentence that carries no load; falsity lives in B's cast list) — fine:
   G26A's `|Y_A−Y_0|≤5` + `|Y_B−Y_0|≤5` + `|Y_AB−Y_0|` sufficiency gates
   decide empirically which items behave as designed.
4. Subtle-falsity NS items (`6234c127`-class: falsity in a single modifier
   such as "country" or a date) and A-near-sufficient conjunctive SUPPORTED
   items (leak 0.7–0.8) — all left to the selector, as designed.

**Topology.** Parallel/comparison claims exist (e.g. *"Greater Swiss Mountain
Dog and Harrier are both dog breeds"*) and break the T1/T2 load-bearing
construct — they carry no bridge and are removed by R1 (the `neither` bucket,
35.5%, is a superset of them).

**One-by-one read of 20 constructed survivors** (deterministic random sample,
seed 20260924): 20/20 structurally clean — correct sentences at gold indices,
unique orientation, jointly-bearing pairs; zero fragments, zero misaligned
indices, zero label contradictions. Items with single-side sufficiency risk
(e.g. dev `…` A-near-verbatim conjuncts, B-refutes-date cases) are present by
construction and are exactly what the selector's Y_A/Y_B gates filter.
Disclosure: the review dump used a leaner stoplist than the script and listed
4,114 vs the record's 4,105 (9 boundary flips at leak=0.9); **the script's
4,105 is the number of record.**

## 6. Post-rule funnel (headline)

| stage | items |
|---|---|
| 2-hop, n_sf==2, distinct titles | 6,912 |
| pages materialized (after NFD fix) | 6,832 |
| orientation-unique bridge (R1) | 4,270 |
| + word range 8..80 (R2) + leak <0.9 (R3) | **4,105** |

Survivors by cell: train S 2,506 / NS 1,136 · dev S 195 / NS 268.
**Clusters: 2,683 title-pairs (1,635 singletons), 2,710 hpqa_ids.**
Selector floor = 200 → **PASS (13.4×)**. MuSiQue evaluation: **not
triggered** (no kill condition fired).

## 7. What this audit does NOT establish

- Reconstruction ≠ byte-identical CoreNLP; alignment is established
  statistically (controls) + per-item for survivors (bridge confirmation),
  not by proof of segmentation identity.
- R2/R3 thresholds (8..80 words, 0.9) are design choices → must be pinned as
  prereg open items before G26A freeze.
- NOT_SUPPORTED sufficiency (whether A+B actually move a verifier) is
  **not** shown here — that is the selector phase's `Y_AB` gate.
- Claim-level gold noise exists (Class C) at unknown rate; two-phase
  authority (selector-only Phase A → funnel check → separate flip for Phase B)
  remains mandatory.
- Draw hygiene: use one split only; cluster on hpqa_id/title-pair.

## 8. Consequences for G26A (design edits already banner'd on the draft)

1. Chain-only materials are available at scale → the construct rewrite to
   **load-bearing emergence / compositional activation** (banner item 1) is
   supported by data, not just by argument.
2. Fixed A/B orientation rule: **mention direction**, not list order
   (98.2% agree, but 75 reversed items exist).
3. Padding, ROPE power note, two-phase authority: unchanged by this audit;
   still required (banner items 3–5).
4. Next sequence: user signs G26A banner items → wording rewrite → power
   notes → prereg freeze path. **First compute of the project remains G25A.**

## 9. Reproduce

```
python3 src/audit_hover.py          # writes results/audits/hover_structural_v1.json
```

Flagged uids for reference: `961688da…` (Class C1, adjudicate), `b065d90b…`
(C2), `c679a81c…` (Class B), OOB examples `8f982acc…`, `ba6b6f11…`.
