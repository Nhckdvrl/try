# G24A preregistration — source-grounded natural-evidence confirmation

**Created:** 2026-09-24, after `G24A_SOURCE_DATA_AUDIT_v1` passed 53/53 gates
(commit `802e915`).

**Status:** FROZEN DESIGN — this file, its code and its tests are committed and
tagged `g24a-natural-evidence-confirmation-design-v1` before any G24A forward
pass (including the selection pass). §12 records the freeze and the design
points settled before tagging.
**NO G24A TARGET-MODEL COMPUTE IS AUTHORIZED BY THIS FILE.**
Repository-level authority for any compute lives in `STATUS.md` only.

G24A is the RQ1 (generality) confirmatory slot named in
`PAPER_SCALE_AUDIT_2026-09-23.md` §7: replace author-created stories with
**human-annotated claim/evidence pairs from two existing datasets** and test
whether the zero-use exclusion law replicates on natural materials.

---

## 1. Scientific question

G0 established, on authored items, that evidence which a ruling excludes still
moves the judgment (`REI > 0`), and that the leak is larger when the rule
arrives before the evidence than after it.

G24A asks:

> **Does excluded natural, human-annotated evidence still influence
> claim-likelihood judgments, under the same prospective-vs-retrospective
> zero-use contrast?**

Short form:

> **natural-evidence confirmation**

This is a confirmation/generalization experiment, not a benchmark submission.
FEVER and SciFact are used purely as carriers of *natural* claim/evidence
structure; no fact-checking accuracy, no leaderboard, no new task.

---

## 2. Data (audited and frozen)

Pinned inputs (SHA-256 re-verified in the audit):

| file | sha256 |
| --- | --- |
| `fever/shared_task_dev.jsonl` | `e89865bfe1b4dd054e03dd57d7241a6fde24862905f31117cf0cd719f7c78df7` |
| `fever/train.jsonl` | `eba7e8f87076753f8494718b9a857827af7bf73e76c9e4b75420207d26e588b6` |
| `fever/wiki-pages.zip` | `4b06d95da6adf7fe02d2796176c670dacccb21348da89cba4c50676ab99665f2` |
| `scifact/data.tar.gz` | `11c621288d41ac144d29b13b0f8503b3820b7d6e8b1f6ff24dff335c196d76be` |

Construction audit: `data/external/review/G24A_SOURCE_DATA_AUDIT_v1.json`
(`74ec9680…c98d70b`), `…v1.md` (`bfadcf08…914234c3`) — **AUDIT PASS, 53/53
gates**, committed before this prereg.

Frozen pools:

- **FEVER: 12,648** (SUPPORTS 6,326 / REFUTES 6,322) — verifiable dev records
  with unique claim text, evidence block = annotated **group 0**, page refs
  resolved under NFC, reading order, text-quality gates applied (well-formed
  sentences, paired quotes, balanced parentheses, no wiki residue).
- **SciFact: 635** (SUPPORT 417 / CONTRADICT 218) — evidence-bearing,
  single-document, single-label claims; rationale = union of annotated
  sentences.
- Cross-dataset claim-text overlap: 0.

**Frozen cluster keys** (G23C-style skeleton clustering):

- FEVER → first evidence wiki page of the group-0 block, NFC form;
- SciFact → evidence `doc_id`;
- pooled key = `(source, cluster)`; all models' observations of all items that
  share a cluster stay in one bootstrap cluster.

**Direction sign** (`s`, identical to G0): `+1` for SUPPORTS/SUPPORT,
`−1` for REFUTES/CONTRADICT.

---

## 3. Items and conditions

Candidate file: `data/items/g24a_candidates_v1.jsonl` — **all 13,283 pool
records** as G24A items (`task_family` `g24a_fever` / `g24a_scifact`).

Item field mapping (documented literals; nothing is LLM-written):

- `base_context` = the claim text; the background block header is **`CLAIM`**;
- `critical_evidence` = the frozen evidence block; the evidence block header is
  **`EVIDENCE E`**;
- `critical_label` = `evidence E`;
- `critical_direction` = `increase`/`decrease` by gold label (§2 sign `s`);
- `exclusion_reason` = `none_stated` — the ruling gives no reason, exactly as
  in IDBIND (v2);
- `evidence_truth` = `true_but_forbidden` for every item (the annotated
  evidence is dataset-gold truthful text; under the exclude rule it is
  forbidden);
- `admit_rule` / `exclude_rule` = the two constants below (identical across
  all items);
- `question` = `Considering everything above, rate the likelihood that the
  claim is true.`
- `output_spec` = `Use a scale from 0 to 9, where 0 means certainly false and
  9 means certainly true.`
- `rule_probe_question` = `According to the ruling above, are you permitted to
  use evidence E when you reach your rating? Answer with exactly one word:
  YES or NO.`
- `memory_question` = `""` — **no memory probe is run in G24A** (mechanism is
  out of RQ1 scope);
- `ground_truth` = `null`; gold label, source id, cluster key and construction
  facts live in `meta`.

The two ruling constants (IDBIND wording, `E7` → `E`):

```text
ADMIT_RULE   = Evidence E is admitted. It must be given the full weight of a
               verified item in your final judgment.
EXCLUDE_RULE = Evidence E is excluded. It must have zero influence on your
               final judgment.
```

The five conditions reuse the G0 condition names; block rendering dispatches on
`task_family` (`src/conditions_g24a.py`, wired in `src/schema.py::_blocks`).
G0/other item files are bit-for-bit unaffected (regression-tested).

```text
base         [ CLAIM ]
admit_pre    [ CLAIM, RULING(ADMIT_RULE),   EVIDENCE E ]
admit_post   [ CLAIM, EVIDENCE E, RULING(ADMIT_RULE) ]
exclude_pre  [ CLAIM, RULING(EXCLUDE_RULE), EVIDENCE E ]
exclude_post [ CLAIM, EVIDENCE E, RULING(EXCLUDE_RULE) ]
```

Design constraints enforced by construction and by test:

1. the ADMIT text is **character-identical** in pre and post;
2. the EXCLUDE (zero-use) text is **character-identical** in pre and post —
   only the position relative to `EVIDENCE E` differs;
3. the prompt tail (question, output spec, answer format) is identical across
   all five conditions.

Readout is the standard G0 machinery: `mode=reasoned`, greedy rationale to the
`ANSWER:` cue, then the next-token expectation over digit tokens rescaled to
0–100 (`digit_expectation`). No LLM judge anywhere.

Probes: the standard rule triple (`rule_probe_exclude_pre`,
`rule_probe_exclude_post`, `rule_probe_admit_post`) runs with the main pass on
all selected items; `memory_probe_exclude_post` is **not** run.

---

## 4. Models (frozen panel subset)

Five checkpoints, all from the frozen G4 panel
(`data/model_panel_g4.json`), all verified present in the local HF cache at
their frozen revisions:

| tag | model id | revision | params | role |
| --- | --- | --- | --- | --- |
| `mistral-small-24b` | `mistralai/Mistral-Small-24B-Instruct-2501` | `9527884b…9724` | 23.6B | **selection model** + analysis |
| `llama31-8b` | `NousResearch/Meta-Llama-3.1-8B-Instruct` | `d10aef79…0b77` | 8.0B | analysis |
| `qwen3-8b` | `Qwen/Qwen3-8B` | `b968826d…218` | 8.2B | analysis |
| `qwen35-9b` | `Qwen/Qwen3.5-9B` | `c2022362…7b9a` | 9.0B | analysis |
| `gemma3-12b` | `google/gemma3-12b-it` | `96b6f1ef…fd80` | 12.2B | analysis |

Five families (Llama-3.1, Qwen3, Qwen3.5, Gemma-3, Mistral), 8.0–23.6B.
No model may be added, dropped, or swapped after the tag.

Runner settings (frozen): `--mode reasoned --reason-tokens 110
--max-model-len 4096 --tp 1`, temperature 0 for decisions and probes.

---

## 5. Selection rule (Base/Admit only — no Exclude outcome is ever seen)

Selection exists only to guarantee **measurable Admit leverage** (audit §7).
It is fully mechanical.

1. **Candidate order.** The candidate file is written stratum by stratum in
   the order `[fever/SUPPORTS, fever/REFUTES, scifact/SUPPORT,
   scifact/CONTRADICT]`; within each stratum, records are shuffled with a
   single `random.Random(20260924)` stream applied in that stratum order.
2. **Selection pass.** Run **`mistral-small-24b`** (frozen revision), greedy
   reasoned readout, over the candidates file with exactly three kinds:
   `base,admit_pre,admit_post`. The selection pass contains **zero exclude
   conditions and zero probes**.
3. **Eligibility.** With `s` from the gold label and values on the 0–100
   readout scale, an item is eligible iff all three values are non-null and

   ```text
   s · ( mean(value_admit_pre, value_admit_post) − value_base )  ≥  τ
   τ = 10.0
   ```

   This is exactly the signed leverage `sL` whose sign rule the G0 analyzer
   applies per model; τ = 10 readout points ≈ one full digit step.
4. **Quotas (first-eligible, never ranked by effect size).** Walk each
   stratum's shuffled candidate list in order and take eligible items until:

   | stratum | quota |
   | --- | --- |
   | FEVER SUPPORTS | 200 |
   | FEVER REFUTES | 200 |
   | SciFact SUPPORT | 100 |
   | SciFact CONTRADICT | 100 |
   | **total** | **600** |

5. **Shortfall rule.** If a stratum's whole pool is exhausted before its quota,
   keep every eligible item found and report the shortfall. The quotas, τ, the
   rule, or the order are **not** changed afterwards. The selected file
   (`data/items/g24a_v1.jsonl`) and a selection report
   (`data/items/g24a_selection_report_v1.{md,json}`, including per-stratum
   examined/eligible counts and the sha256 of the selected file) are written
   before any analysis-model run starts.

No Exclude outcome, no probe output, and no analysis-model output may enter
selection. The selection model's own Exclude results are used only in the
final analysis, never to revisit the selected set.

---

## 6. Estimands (inherited from G0)

Per item × model, with `s` the gold-label sign, values on the 0–100 scale:

```text
L      = mean(admit_pre, admit_post) − base
sL     = s · L                       (usable iff sL > 0, per item per model)
REI_c  = s · (value_c − base) / |L|  for each non-base condition c
D_time = REI_exclude_post − REI_exclude_pre
UTB    = s · [ (exclude_post − exclude_pre) − (admit_post − admit_pre) ] / |L|
```

`REI = 0` means the excluded evidence was ignored; `REI = 1` means it was used
exactly as if admitted. Ratio cell values are winsorised at ±3 before
aggregation (G0 convention). Items with any of the five condition values
missing, or `sL ≤ 0` for a given model, are unusable **for that model only**
and are reported in `n/n_total` exactly as in G0. Usable-cell values are never
post-hoc filtered on any outcome.

Reported alongside: RuleAcc (`1 − p(YES)` on the exclude probes,
`p(YES)` on the admit probe), median `|L|`, alignment rate (`sL > 0`), digit
mass diagnostics.

---

## 7. Frozen inference

- **Cluster bootstrap** over the frozen cluster keys of §2: each resample draws
  `K` clusters with replacement (K = number of clusters in the stratum) and
  computes the mean over all rows (items × models for pooled statistics) of
  the drawn clusters — a cluster's items and all their model observations move
  together;
- seed `20260924`, `B = 10,000`, percentile 95% CIs, two-sided bootstrap p as
  in G0 `boot_p`;
- pooled primary inference uses the **four non-selection models**
  (`llama31-8b`, `qwen3-8b`, `qwen35-9b`, `gemma3-12b`); the selection model
  `mistral-small-24b` is reported separately as a reference, because its item
  set was conditioned on its own Admit leverage;
- strata reported: pooled-4, pooled-5, per model, per source
  (FEVER/SciFact), per source × gold label;
- no item is removed after results exist; missing/unparsed rows may be rerun
  only for mechanical incompleteness, never selectively by outcome.

**Primary endpoints (both must pass; intersection–union, no multiplicity
correction needed):**

- **P1:** pooled-4 `REI_exclude_pre` — cluster-bootstrap 95% CI lower bound
  strictly > 0;
- **P2:** pooled-4 `REI_exclude_post` — cluster-bootstrap 95% CI lower bound
  strictly > 0.

**Consistency clauses (part of the confirmatory verdict):**

- C1: `REI_exclude_pre > 0` and `REI_exclude_post > 0` as point estimates in
  at least **4 of 5** individual models;
- C2: pooled-4 point estimates of both REIs are > 0 **within FEVER and within
  SciFact** separately.

**Data-sufficiency gate:** if the pooled-4 usable items number fewer than
**300 of 600** selected, the verdict is `unresolved` (leverage failed to
transfer across models), regardless of endpoint values.

---

## 8. Outcome map

Decision order, strictly literal:

### `natural-evidence-leak`

P1 ∧ P2 ∧ C1 ∧ C2, with the sufficiency gate passed.

Licensed claim:

> **Excluded, human-annotated natural evidence still moves claim-likelihood
> judgments under a standing zero-use ruling, both when the ruling precedes
> the evidence and when it follows it — the G0 exclusion law replicates on
> source-grounded materials across models and datasets.**

### `natural-evidence-leak-inconsistent`

P1 ∧ P2 pass, but C1 or C2 fails.

Licensed claim:

> The leak replicates on natural evidence in the pooled panel, but it is not
> uniform across models or datasets.

Do not call this a general confirmation.

### `prospective-only`

P1 passes, P2 does not.

Licensed claim:

> Natural evidence leaks even when the zero-use ruling precedes it, but the
> retrospective arm is not distinguishable from zero.

### `retrospective-only`

P2 passes, P1 does not.

Licensed claim:

> Natural evidence leaks only when the model has seen it before the ruling
> arrives (contradicts the G0 prospective-cost pattern on natural materials).

### `not-confirmed`

Neither endpoint passes (sufficiency gate passed).

Licensed claim:

> On human-annotated natural evidence, excluded evidence did not measurably
> move judgments in this design.

### `unresolved`

Licensed claim:

> Design not evaluable as preregistered (sufficiency gate or data completeness
> failed); no confirmation claim is licensed.

Anything else, including the sufficiency gate failing.

---

## 9. Controls and integrity checks

1. **Rule identity:** ADMIT text and EXCLUDE text are each character-identical
   between their pre and post forms (construction constant + test).
2. **Selection blindness:** the selection pass provably contains no
   `exclude_*` kind (selector input check + test); quotas are filled
   first-eligible in frozen order.
3. **G0 non-interference:** prompts for existing item files are unchanged by
   the `task_family` dispatch (regression test over `items_v1` first record).
4. **Same readout, same tail:** all five conditions share question, output
   spec and answer format (test).
5. **Sign convention:** gold-label `s` identical to G0's
   `critical_direction` mapping (analyzer test with both directions).
6. **Cluster integrity:** pooled bootstrap keeps every item of an evidence
   cluster — across all models — inside one resampled cluster (test).
7. **No scope creep:** no new layer/site/model search, no new carrier, no
   probe beyond the standard rule triple, no LLM-generated data or judgments.

---

## 10. Relation to nearest prior

FEVER and SciFact are normally used to score verification/NLI accuracy. G24A
uses their *annotations* only to obtain natural claims with gold evidence
direction, and measures **compliance with an exclusion ruling**, an estimand
absent from the fact-checking literature. Nothing here competes on benchmark
accuracy; nothing here re-estimates G0 on authored items — the materials,
carriers and selection regime are all new, the estimand and readout are
deliberately identical to G0 so the comparison is interpretable.

---

## 11. Authorization boundary

Before any G24A target-model forward pass — **including the Base/Admit
selection pass**:

1. implement `src/conditions_g24a.py` + `src/schema.py` dispatch;
2. implement `src/build_g24a_items.py` (pool → candidates file, frozen order)
   and verify the candidate strata counts (6,326 / 6,322 / 417 / 218);
3. implement `src/select_g24a.py` (eligibility, quotas, shortfall report) and
   `src/analyze_g24a.py` (estimands, cluster bootstrap, outcome classifier);
4. add `tests/test_g24a.py` covering §9's checks, the outcome classifier's
   decision order, the sufficiency gate and the prereg wording lock;
5. commit everything and tag `g24a-natural-evidence-confirmation-design-v1`;
6. explicitly update `STATUS.md`.

Until the tag and the STATUS update both exist:

> **NO G24A COMPUTE.**

Compute layout (authorized only after §11.6): four local GPUs (98 GB each) —
GPU0 runs the mistral selection pass then the mistral main pass; GPU1 runs
`llama31-8b` then `gemma3-12b`; GPU2 `qwen3-8b`; GPU3 `qwen35-9b`. Main pass
kinds: `base,admit_pre,admit_post,exclude_pre,exclude_post` + the rule triple
(8 kinds × selected items). Expected main-pass volume: ≤ 600 × 8 × 5 =
24,000 prompts — a single overnight window.

---

## 12. Freeze checklist and record

Design-audit points settled before tagging (no G24A model output of any kind
exists: no selection pass, no decision, no probe):

- **§3 headers:** `CLAIM` / `EVIDENCE E`; no ID preamble (one evidence block,
  binding is trivial). `exclusion_reason = none_stated`,
  `evidence_truth = true_but_forbidden` uniformly; both are documented
  metadata literals, never analysis strata.
- **§4 selection model = `mistral-small-24b`** — rationale frozen: largest
  panel model, so eligibility requires evidence to move even the strongest
  judge; its own results are excluded from the pooled primary (§7).
- **§5 τ = 10.0** readout points on the signed mean leverage, matching the
  analysis `L` definition exactly; **quotas 200/200/100/100 = 600**;
  shortfall rule as written; candidate shuffle seed **20260924**.
- **§2 cluster keys:** FEVER first group-0 evidence page (NFC), SciFact
  `doc_id`; pooled key `(source, cluster)`; all model observations of a
  cluster travel together.
- **§7 sufficiency gate:** pooled-4 usable ≥ 300/600, else `unresolved`.
- **§8 decision order:** `natural-evidence-leak` →
  `natural-evidence-leak-inconsistent` → `prospective-only` →
  `retrospective-only` → `not-confirmed` → `unresolved`, evaluated strictly in
  that order.
- **§11 wiring:** selection pass =
  `python src/run_model.py --kinds base,admit_pre,admit_post --items data/items/g24a_candidates_v1.jsonl`
  → `python src/select_g24a.py …`; main pass =
  `python src/run_model.py --kinds base,admit_pre,admit_post,exclude_pre,exclude_post,rule_probe_exclude_pre,rule_probe_exclude_post,rule_probe_admit_post --items data/items/g24a_v1.jsonl --max-model-len 4096 …`;
  analysis = `python src/analyze_g24a.py …` → `results/g24a/g24a_analysis_v1.{md,json}`.

Freeze checklist (§11):

- [x] §11.1 `conditions_g24a` + schema dispatch, G0 regression test green;
- [x] §11.2 builder + candidates file, strata counts verified
      (6,326 / 6,322 / 417 / 218);
- [x] §11.3 selector + analyzer, tests green (`tests/test_g24a.py`, 25 tests);
- [x] §11.4 tests cover §9.1–§9.6, the outcome decision order and the
      sufficiency gate;
- [x] §11.5 this document, code and tests committed and tagged
      `g24a-natural-evidence-confirmation-design-v1`, before any forward pass;
- [ ] §11.6 `STATUS.md` updated in the commit immediately following the tag —
      only that repository-level authority can permit compute.
