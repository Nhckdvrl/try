# Project status — 2026-09-25, G24A/G24B COMPLETE / G25A COMPLETE — `order-artifact` NO-CLAIM ACCEPTED, NO RESCUE, headline withdrawn / G26A RULINGS 1–4 IMPLEMENTED — SUITE 451 GREEN — AWAITING USER REVIEW OF THE TEST-SYNC COMMIT → PHASE-A TAG → FLIP #1 / NOVELTY RESTRUCTURE ACTIVE

> **NO APPROVED PAPER MAINLINE.**
>
> **G23A v3 COMPLETE:** `zero-amplified`, `Δ_zero = +8.83 [+4.39,+13.33]`.
>
> **G23B v1 STOPPED AT THE FROZEN PHASE-A CARRIER GATE:** `carrier-invalid`.
>
> **G23C v1 COMPLETE:** frozen verdict `target-conditioned-policy-state`,
> L14 `TargetConditioning = +8.15 [+6.91,+9.44]`.
>
> **G24A v1 COMPLETE (2026-09-24):** frozen verdict `prospective-only` —
> pooled-4 `REI_pre = +0.541 [+0.477,+0.603]` (P1 PASS) vs
> `REI_post = −0.067 [−0.158,+0.021]` (P2 FAIL); sufficiency gate 595/600;
> integrity ledger 5/5 models × 600 items complete. Report:
> `results/g24a/g24a_analysis_v1.{md,json}`. Licensed §8 wording applies
> verbatim; no other claim language is authorized from this round.
>
> **G24B v1 COMPLETE (2026-09-24):** frozen verdict
> `donor-conditioned-policy-state` — L14 primary
> `DonorTargetInteraction = +4.02 [+2.27,+6.14]` (floor 3.0, positive in
> 2/2 models: qwen3-8b +3.17, mistral-small-24b +4.88);
> `DonorPolicy_M = +10.81 [+8.31,+13.41]`, `DonorPolicy_U = +6.79
> [+5.22,+8.78]` both pass; controls L4 `dti = −0.15` / L24 `dti = +0.07`
> both absent → clause OK; identity `max |Δ| = 0.0000` over 1,800 checks;
> bridge PASS with the §12 cross-check against frozen G23C gates; 75/75
> items × 2 models complete, zero drops. Report:
> `results/mech/g24b_analysis.json`. Licensed §8 wording applies verbatim;
> no other claim language is authorized from this round.
>
> **G25A DESIGN TAGGED (record — NO COMPUTE AUTHORIZED YET):** near-zero
> sweep — prereg `preregistrations/PREREGISTRATION_G25A_NEAR_ZERO.md`, tag
> `g25a-near-zero-design-v1` (commit `04a17bb`, tagged before any G25A
> forward pass). §12 freeze checklist complete with the §11.4 pre-tag
> clarifications recorded: RuleAcc := pooled within-2pp fraction over the
> O3 probes (unparsed rows stay in the denominator; probe-absent fails I2
> → `order-artifact`); CLAIM/RULING/EVIDENCE E block rendering
> (`g25_norule` has no RULING); cluster key `source/cluster`; §8 top-down
> row precedence; gradedness can never gate (`classify` signature-locked
> to its six gate inputs). Frozen materials: `data/items/g25_v1.jsonl`
> sha256 `7c6993244d7808d8e65696c00a55f4fc14c7f3011f34f0266e450f1367173147`
> (400 = 150/150/100, byte-identical to candidates, 342 clusters, 126
> shared with G24A disclosed as-is), selection anchor `0b38e0837ed9fd60`,
> examined 889/2139/200. Tests: `tests/test_g25a.py` 33/33 green; full
> suite **418 passed / 953.65 s with zero `--ignore` flags** (supersedes
> the 334/849 s five-flag baseline). Harness `scripts/run_g25a_main.sh`
> (16 cells + 2 O3 probes, pooled-4, pinned snapshots, items-sha
> preflight) refuses to run until the flip entry below appends the
> concatenated token `G25A-FLIP=` + `RECORDED` — split here on purpose so
> this design-tag record cannot open the gate it documents as closed.
> **Step 8 — the STATUS flip authorizing ≤ 28,800 rows (25,600 condition
> + 3,200 O3 probe rows, 4 pooled models, no retries-by-outcome) — is
> USER-OWNED and NOT yet recorded.** After the flip: run the harness once
> per pooled model → `src/analyze_g25.py` → verdict → (only then) the RQ2
> section draft.
>
> **G25A STATUS FLIP RECORDED (2026-09-24) — COMPUTE AUTHORIZED (step 8,
> user decision):** token `G25A-FLIP=RECORDED`.
>
> Design tag `g25a-near-zero-design-v1` @ `04a17bb` (§12 checklist complete
> except this box; items sha256 `7c6993244d7808d8e65696c00a55f4fc14c7f3011f34f0266e450f1367173147`
> locked; `tests/test_g25a.py` 33/33; full suite 418 passed / 953.65 s
> with zero `--ignore` flags). This entry releases **≤ 28,800 rows** =
> 400 items × (16 decision cells + 2 O3 probes) × 4 pooled models
> (qwen3-8b, gemma3-12b, llama31-8b, qwen35-9b), no retries-by-outcome,
> selector mistral-small-24b never pooled, prereg unchanged from the tag.
> Order: 4× `scripts/run_g25a_main.sh <gpu> <model-tag>` → all four raws
> complete (7,200 rows each, 28,800 total) → frozen `src/analyze_g25.py`
> → outcome-map verdict → **only after the verdict** the RQ2 section
> draft.
>
> **G25A RUN RECORDED (2026-09-24) — VERDICT `order-artifact` (frozen §8
> map; NO claim licensed; RQ2 section NOT drafted):** flip `8a33722` →
> 4× `scripts/run_g25a_main.sh` all EXIT=0 (7,200 rows each = 28,800
> total, unparsed 0, 18 kinds × 400 verified per model) → frozen
> `src/analyze_g25.py` → `results/g25a/g25a_analysis_v1.{md,json}`
> (`f15ce35`). Gates: **I1 FAIL** Gap(100) −1.06 [−1.93, −0.21] · I2 PASS
> RuleAcc 0.949 over 3,200 probes · **S1 FAIL** 354/400 (need 360) ·
> **G1 PASS** Δ_local0 +3.58 [+1.33, +5.79] (boot_p 0.0014) · **G2 FAIL
> on floor** Gap01 2.83 < 3.0 [+0.49, +5.11] · G3 PASS 3/4 both.
> Gradedness descriptive only: `graded`, GradedPos +20.81 [+19.12,
> +22.50]. §8's required action executed — integrity investigation
> `src/audit_g25a_integrity.py` →
> `results/audits/g25a_integrity_investigation_v1.json` (`ad27bb5`; all
> citation asserts 1e-9 vs analysis v1): the offset is tail-concentrated
> (median −0.00; non-argmax-flip rows −0.14; **217/1391 = 15.6% argmax
> digit flips at the inert anchor** carry mean −6.04; |gap|≥50 = 48 rows
> = 3.5% → −0.547 of −1.061, buckets sum exactly), 4/4 models negative
> and leave-one-out all negative (not one model), readout valid
> (digit-mass<0.5 = 0/2,782; G0–G24A `digit_expectation_0_100` lineage
> asserted), anchor parse w100 0.9375 / w000 0.9606 within ±2pp; rule→
> answer distance pre median 133 [98, 345] vs post 89.5 [86, 92]. S1
> anatomy {0:4, 1:10, 2:32, 3:99, 4:255}, drops exclusively
> nonpositive_anchor (llama 78 / qwen3 50 / qwen35 57 / gemma 24).
> **No correction, no re-run, no reclassification — verdict unchanged.
> Remediation decision received same day: ACCEPTED no-claim, no rescue —
> see the pinned RQ2/G25A RULING below.**
>
> **RQ2/G25A RULING (2026-09-24, user decision — PINNED; future agents:
> do not reopen):** G25A frozen verdict `order-artifact` **ACCEPTED**.
> **No rerun, no correction, no bias-subtraction, no G25B, no
> remediation compute — ever, absent a fresh explicit user decision.**
> The natural-data headline *"natural semantic control has a sharp
> exact-zero boundary"* is **WITHDRAWN**. Rationale of record: the
> observed natural ladder is smooth (Gap(w) = 10.58 → 7.76 → 6.90 →
> 6.36 → 5.60 → 3.59 → −1.06 over w = 0…100%) with graded
> GradedPos +20.81 [+19.12, +22.50]; even setting I1 aside, S1
> (354/400 < 360) and G2 (2.83 < floor 3.0) independently block
> `exact-zero-boundary` — so this is not "almost passed, patch and
> rerun"; fixing the anchor/readout/floor/n now would be post-hoc
> story-saving. **G23A survives as controlled-material SUPPORTING
> structural analysis** (on controlled materials zero carries extra
> prospective amplification, Δ_zero +8.83 [+4.39, +13.33], and explicit
> arithmetic prospective zero is exactly executable) — demoted from
> second headline RQ to supporting evidence. Honest reporting plan for
> paper/appendix: a preregistered natural-data confirmation that became
> non-interpretable under its own frozen integrity criterion (100%
> anchor showed a small but systematic order effect); local contrasts
> suggestive (G1 PASS +3.58 [+1.33, +5.79]) but did not satisfy the
> complete preregistered gate set. The RQ2 section = that no-claim
> report, drafted whenever the paper reaches it — no other RQ2 prose.
>
> **G26A O5 RULED (2026-09-24, `4eeb7e2`):** options 1/2/3 rejected;
> equivalence demoted from primary-branch requirement to **secondary
> characterization only** (CI ⊆ ±1.5 → may add "compatible with
> negligible gain"; never a branch, never `unresolved`); primaries
> answered by positive gates (CI low > 0 **and** point ≥ 3.0); δ = 1.5
> secondary / n ≤ 300 pinned unchanged; §7 procedure + §8 table
> rewritten; §12A O5 box ticked. Phase A still NOT tagged at that point.
>
> **G26A O1–O9 ALL SIGNED (2026-09-24, user sign-off, v2 wording incl.,
> no item changed):** O1 mistral selector · O2 pooled-4 · O3 10 cells ·
> O4 train-only / cap 300 / S1 ≥ 200 · O5 positive gates (CI low > 0 +
> point ≥ 3.0) with δ = 1.5 secondary-characterization-only · O6
> per-model chain-effect usability ≥ 5 · O7 shared filler multiset ±10 ·
> O8 title-pair clusters · O9 Phase A = 3,642 train survivors. G26A
> **enters the implementation/freeze path now**: builder + selector
> harness + analyzer + tests (train-only 3642, mention-direction A/B,
> shared filler, ±10 distance, Phase-A blindness to rule cells, the
> three selection gates, floor 3.0, ROPE wording-only-never-branch,
> cluster bootstrap, outcome-map order) → full suite green → **Phase-A
> design tag** → **STATUS flip #1** → Phase A mistral ≤ 14,560 rows →
> raw sha256 freeze + gate funnel → **≥ 200** → frozen-order cap 300,
> lock selected IDs + sha256, **flip #2** → Phase B ≤ 14,400 rows → frozen
> analyzer one-shot RQ3 verdict ; **< 200 → HARD STOP** (no 15/5/5
> loosening, no dev split, no MuSiQue — project-level escalation).
> **RQ3 = sole active headline candidate; next compute = G26A Phase A.**
>
> **Pre-tag corrections (user-ruled 2026-09-24, implementation audit):**
> O3's "11 cells" was a **typo for 10** — the enumeration
> (`Y0/YA/YB/YAB + EXCL×3 + ADMIT×3`) is complete (every §5/§6/O6
> quantity computable; no estimand named an 11th cell); Phase B restated
> 300 × 10 × 4 = 12,000 + 2,400 probes = **≤ 14,400 rows** (the old
> 13,200/15,600 figures are void). **Rule-probe timing pinned to T0**
> (one probe per rule type, 2,400 rows). Both recorded in prereg
> §0/§3/§11/§12B before any tag.
>
> **G26A FILLER-FEASIBILITY GATE + PHASE-A POOL WRITTEN (2026-09-24,
> user ruling: "freeze the feasibility criterion, not 100% coverage" —
> zero-model, outcome-blind, commits `17dfcac`/`6ab4a7e`/`7ac6b49`/
> `c911e79`, pushed):** deterministic census of the 3,642 structural
> survivors under frozen FILLER_BANK v2 + frozen search budget →
> **N_A = 3,640 feasible**; exactly 2 excluded as
> `tokenizer_geometry_infeasible` (uids `3dbe1a3e-…-2e3a2ada88bc`,
> `4b84c748-…-b6bab6e8759040` — Georgian-evidence twins, funnel-passed,
> best effort **13 > 10 on llama31-8b both arms, other 3 tokenizers
> ≤ 10**; deterministic re-run reproduces the failure in
> `tests/test_g26a.py`). Pool `data/items/g26_phasea_pool_v1.jsonl`
> sha256 `ad0ac715a609f49f9ad98af5cf6a3022a1b1e6f904d7a1f22ae2d490a7e2c95c`
> (n = 3,640 = 3,571 fwd + 69 reversed; 2,319 title-pair clusters = the
> twins' shared pair removed from 2,320). Prereg amended pre-tag: §0
> feasibility-gate bullet (excluded uids + vectors + outcome-independence
> + post-tag freeze: no added sentences, no ±10 relaxation, no
> item-specific/per-model filler, no criterion edits), O9 → 3,640, O4 →
> 2,319 clusters, §3 cross-ref, §11 → **≤ 14,560 rows** + SHA-before-
> gates + exactly-one-parsed-row-per-item-kind, §12A census box ticked.
> Analyzer Phase A hardened (sha first → structural exit 3 for rule
> cell/probe/stray/duplicate/unknown/wrong-model/budget → mechanical
> exit 4 for missing/unparsed → gates → < 200 HARD STOP exit 2; ≥ 200 =
> frozen pool order cap 300, ids sha256, never effect-sorted). Harness
> `scripts/run_g26a_phasea.sh`: runtime gate greps THIS file for the
> flip-1 marker token — after FLIP #1 below, `grep -c` reads **exactly
> 1** (the flip record itself; never passing prose). 2026-09-25 audit:
> the literal had once been embedded in this block's own description,
> which would have opened the gate while flip #1 was NOT recorded —
> removed then; kinds locked to the 4 no-rule
> cells, pool-sha pin, exact 14,560-row assert, refuses overwrites.
> Tests `tests/test_g26a.py` **33/33 green (98.33 s)**; full suite
> **451 passed / 1043.99 s / zero `--ignore` / exit 0** (= 418
> pre-G26A + 33, zero regressions). Manual spot-check: 20 ordinary
> items × 12 invariants = 240 checks, 0 failures; reversed census
> consistent.
>
> **G26A PRE-TAG RULINGS 1–4 IMPLEMENTED (2026-09-24/25, commits
> `19f7d89`/`01766ff`/`41426ce`/`ecac51e`/`915021e`, pushed):**
> (1) §12A baseline → measured 451/1043.99/zero-ignore, box ticked;
> (2) §2/§9.3 reversed erratum — 75 orientation-unique / 72 pooled
> survivors / 69 train + Phase-A pool, both feasibility exclusions
> forward, A/B always by mention direction; (3) S1 confirmed ≥ 200
> items usable on ≥ 3 of the fixed pooled-4 + hardening: exact
> pooled-4 model-set assertion (extra/unknown model → structural exit
> 3; missing pooled model → mechanical exit 4), dynamic
> `min(3, n_models)` DELETED (threshold is the constant 3); (4)
> integrity taxonomy split — missing/incomplete/unparsed rows or probes
> → **mechanical exit 4, NO verdict**, complete probes + RuleAcc < 0.8
> → `rule-legibility-failure` (NO CLAIM), I3 fail → `order-artifact`
> (only gate licensing it), I1/I2 fail → `structural-integrity-failure`
> (label priority structural → legibility → order). Tests re-synced to
> the new semantics (the old missing-probes→order-artifact test was
> replaced by the 33-test taxonomy battery); §12A records the measured
> numbers. User review of the test-sync `ecac51e` PASSED 2026-09-25
> (rulings 1–4 accepted; pre-tag scientific/design audit PASS; the
> ledger's stale-authority cleanup landed in `f8173f0`). Phase-A
> design tag `g26a-load-bearing-phasea-design-v1` (annotated; tag
> object `8b941e0ae3bf07b530d80416d2700a2dfa11c7f4`) created 2026-09-25
> on commit `61d0eaf`. At flip time: tag→HEAD diff excluding this file
> verified EMPTY (this flip commit touches STATUS.md only), Phase-A
> rows = 0, design/code/tests immutable from the tag onward.
>
> **FLIP #1 (user-signed 2026-09-25, verbatim authorization: "批准
> G26A Phase A flip #1。"): G26A-FLIP1=RECORDED.** Gate open BY DESIGN
> for Phase A only. Authorizes EXACTLY: `scripts/run_g26a_phasea.sh`
> one-shot — mistral-small-24b selector, the frozen 4 no-rule cells
> (Y0/YA/YB/YAB) × the 3,640 frozen pool items = ≤ 14,560 rows, pool
> sha256 `ad0ac715a609f49f9ad98af5cf6a3022a1b1e6f904d7a1f22ae2d490a7e2c95c`
> pinned by the harness (prereg §12A line: "STATUS flip #1 recorded
> (ledger: authorizes Phase A ≤ 14,560 rows)" — this ledger record is
> that entry). Nothing else is authorized; Phase B stays blocked on
> funnel ≥ 200 → §12B recording → flip #2. Rows at flip time: 0.**
>
> **ACTIVE:** novelty-first paper restructure under
> `PAPER_SCALE_AUDIT_2026-09-23.md`.
>
> **CURRENT HEADLINE STRUCTURE (re-ruled 2026-09-24 after G25A):**
> **RQ1 — sole standing headline finding:** prospective exclusion
> asymmetry / natural-evidence prospective leak.
> **RQ2 — controlled-material supporting structural analysis only:**
> G23A zero amplification + arithmetic-zero executability; the
> natural-data confirmatory returned `order-artifact` NO-CLAIM and the
> natural exact-zero-boundary headline is WITHDRAWN (no rescue — see the
> pinned RQ2/G25A RULING above).
> **RQ3 — sole active headline candidate:** load-bearing vs mere
> presence (G26A, O1–O9 signed); next compute = G26A Phase A after the
> Phase-A tag + STATUS flip #1.
>
> **Stage 5 / G23C / G24B are SUPPORTING MECHANISTIC EVIDENCE, not a third
> headline novelty claim. G23C-R is HOLD / NO COMPUTE.**
>
> **G24A AUTHORIZED EXPERIMENT (record — EXECUTED AND COMPLETE):** source-grounded
> natural-evidence confirmation on FEVER + SciFact — prereg
> `preregistrations/PREREGISTRATION_G24A_NATURAL_EVIDENCE.md`, tag
> `g24a-natural-evidence-confirmation-design-v1` (commit `25316a9`, tagged
> before any G24A forward pass), source audit
> `data/external/review/G24A_SOURCE_DATA_AUDIT_v1` PASS 53/53, candidates
> `data/items/g24a_candidates_v1.jsonl` (13,283 items). Compute authorized =
> prereg §11 layout only: selection pass (`base,admit_pre,admit_post`,
> `mistral-small-24b`, no Exclude/probe rows) → selected ≤600-item file per
> §5 quotas (200/200/100/100, τ=10.0, seed 20260924) → main pass (5 frozen
> panel models × 8 kinds, reasoned, max-model-len 4096, 4 local GPUs) →
> `src/analyze_g24a.py`. Nothing else.
>
> Executed exactly once per this authority: selection pass
> `results/raw/g24a_mistral-small-24b_selection.jsonl` (39,849 rows,
> Base/Admit-only) → selected 600/600
> `data/items/g24a_v1.jsonl` sha256 `b0d02f7a…`, report
> `data/items/g24a_selection_report_v1.{md,json}` (shortfall0; a selector
> early-stop bug was found by structural audit and fixed back to prereg §5.4
> before selection — see commit `b3fe84d`) → main pass5 ×4,800 rows =
> 24,000/24,000 → verdict above.
>
> **G24B AUTHORIZED EXPERIMENT (record — EXECUTED AND COMPLETE):** donor-state vs
> recipient-context factorization — prereg
> `preregistrations/PREREGISTRATION_G24B_DONOR_RECIPIENT_FACTORIZATION.md`,
> tag `g24b-donor-recipient-factorization-design-v1` (commit `a1c787f`,
> tagged before any G24B forward pass). Compute authorized = prereg §4/§6/§9
> layout only: bridge phase (the four Stage-5 cells, direct readout, no hooks,
> the two frozen models × 75 items) → gate read with the §12 boolean-triple
> cross-check against frozen `results/mech/g23c_bridge_analysis.json` (abort on
> mismatch) → only if the bridge passes, patch phase (four baselines with
> rule-end state capture + 8 donor×recipient grid patches × layers (4,14,24) +
> four-cell identity patches, the same two models × 75 items) →
> `src/mech/analyze_g24b.py --phase bridge|full`. Nothing else. Scientific gap:
> G23C's within-preview interchange cannot separate state-side target
> conditioning from matched-recipient sensitivity; this round fixes the
> recipient prompt and varies only the donor state.
>
> **NO OTHER TARGET-MODEL COMPUTE AUTHORIZED.**

> **AUTHORITY NOTE (2026-09-25): the CURRENT authoritative story is the
> header line, the G26A ledger blocks and `CURRENT HEADLINE STRUCTURE`
> above. Everything below this note is retained historical/operational
> governance; where it conflicts, the above wins.** Specifically
> superseded: (a) "Headline finding 2 — KEEP" → G23A exact-zero
> amplification is controlled-material SUPPORTING structural analysis
> only, never a headline; (b) "active candidate = paper restructure +
> search for a genuinely non-obvious third RQ" → that third RQ exists
> and is frozen as G26A (load-bearing vs mere presence), the SOLE
> active headline candidate; (c) blanket "Not authorized: any new
> target-model generation" → G26A Phase A ≤ 14,560 rows IS authorized,
> but ONLY after the Phase-A design tag + the user-owned STATUS flip #1
> (Phase B likewise only after flip #2). Current story, restated:
> **RQ1 = sole standing headline (prospective exclusion
> leak/asymmetry) · G23A = supporting only · G25A natural exact-zero
> headline = WITHDRAWN / NO RESCUE · Stage 5 / G23C / G24B = supporting
> mechanism only · G26A = sole active headline candidate (the repo
> historically labels it RQ3) · no target-model compute before tag +
> flip #1.** Pinned historical G25A/G23A/G24A/G24B records below are
> NOT modified — only their authority precedence is clarified here.

Current selection standard:
[NATURAL_MAIN_RQ_STANDARD_2026-09-06_V17.md](NATURAL_MAIN_RQ_STANDARD_2026-09-06_V17.md)

Current kill authority:
[archive/KILLED_RQ_LEDGER_2026-09-06_V17.md](archive/KILLED_RQ_LEDGER_2026-09-06_V17.md)

V16 local-prior provenance:
[SASANO_LAB_LOCAL_PRIOR_RQ_SEARCH_2026-09-06_V16.md](SASANO_LAB_LOCAL_PRIOR_RQ_SEARCH_2026-09-06_V16.md)

---

## V17 governing rule

The previous methodology accumulated too many overlapping gates.

V17 compresses selection into five hard questions:

1. **REAL OBJECT** — Is the NLP/language question naturally important and durable?
2. **NEW AXIS** — Is there one non-obvious structural relation with at least two plausible accounts?
3. **GOOD DATA** — Are the data simple/credible and the gold independent?
4. **NEW PARENT** — Does parent-level novelty survive “This is just X”?
5. **DECISIVE PAPER** — Are several outcomes informative, and can C1→C2→C3 grow naturally with manageable work?

If any core answer is clearly NO:

> **KILL BEFORE COMPUTE.**

---

## Search prior

> **Search locally, judge globally.**

Use recent Sasano-Lab work to keep candidate generation near concrete NLP/language objects:
- lexical / compositional semantics;
- factual/parametric knowledge;
- language understanding/inference;
- structured semantic/NLP resources and relations;
- stable evaluation/measurement questions;
- representation/generation only when tied to a concrete language object.

Use ACL / EMNLP / NAACL Main / Best / Outstanding to set the scientific bar.

Do not copy labmates' exact topics.

---

## Data rule

Strong preference:
1. existing natural dataset/corpus/resource;
2. published human/linguistic materials;
3. small controlled theory-grounded stimuli when necessary.

Strong negative prior:
- large bespoke synthetic worlds;
- LLM-generated main datasets;
- LLM judge as gold;
- complicated author-created contrasts.

> **Data validity can kill a topic before novelty does.**

---

## Current candidate state

| object | status |
|---|---|
| IFG | **KILL** |
| DRP | **KILL** |
| TCR | **KILL / ARCHIVE** |
| HOM | **KILL CURRENT FORMULATION** |
| CK | **KILL** |
| PD | **ARCHIVE / DO NOT ACTIVATE** |
| Unring the Bell / G23A | **COMPLETE — zero-amplified** (SUPPORTING structural analysis only — never a headline; see CURRENT HEADLINE STRUCTURE RQ2) |
| Unring the Bell / G23B v1 | **STOPPED — carrier-invalid at Phase A** |
| Unring the Bell / G23C | **COMPLETE — target-conditioned-policy-state** |
| Unring the Bell / G23C-R | **HOLD — parent mechanism claim is not headline novelty** |
| active candidate | **G26A — load-bearing vs mere presence (sole active headline candidate; Phase A only after the design tag `g26a-load-bearing-phasea-design-v1` + user flip #1)** — SUPERSEDED 2026-09-25: the earlier "paper restructure + search for a genuinely non-obvious third RQ" entry was stale; the third RQ was found and frozen as G26A |
| approved mainline | **NONE** |

The clean-slate policy remains the default. G23A is a single explicit exception after
the legacy Unring line was re-audited, the old paper stories were archived, and a
decisive fresh pilot was frozen. This is **not** an approved paper mainline.

TCR is now killed because too much source auditing/database reconstruction and cross-linguistic inference are required before the scientific estimand is even secured.

HOM is now killed because the current question remains a competence check of an established semantic distinction despite excellent data.

---

## Compute boundary

G23A v3, G23B v1, G23C v1, G24A v1 and G24B v1 are closed rounds.

The previous “three-RQ paper expansion” and “G23C-R as next compute” roadmap is
superseded by the novelty audit.

### Current paper state

*(2026-09-25: pre-novelty-audit snapshot retained as history; superseded
wherever it conflicts with `CURRENT HEADLINE STRUCTURE` above — RQ1 is
the sole standing headline and Headline finding 2 is withdrawn.)*

**Headline finding 1 — KEEP (= RQ1, the sole standing headline finding)**

> Prospective evidence exclusion is systematically weaker than retrospective exclusion,
> and natural/source-grounded evidence still leaks under a prior zero-use ruling.

Evidence:
- G0 breadth / wording / delay / Admit / diffusion controls;
- Stage-4A system-policy -> tool-output setting;
- G24A source-grounded FEVER + SciFact round, with its frozen
  `prospective-only` verdict.

Do not overclaim model/dataset uniformity: G24A C1 and C2 failed.

**Headline finding 2 — SUPERSEDED 2026-09-25 (previously "KEEP, but
only in contrastive form"): WITHDRAWN as a headline.** G23A exact-zero
amplification + arithmetic-zero executability = controlled-material
SUPPORTING structural analysis only (CURRENT HEADLINE STRUCTURE RQ2);
the natural-data confirmatory returned `order-artifact` NO-CLAIM and
the G25A natural exact-zero headline is withdrawn with NO RESCUE — see
the pinned RQ2/G25A RULING above. Historical text retained below for
the record only:

> Complete semantic causal exclusion has an additional prospective cost, even though
> the same models can execute prospective zero exactly when the contribution is
> explicit/verifiable.

Evidence:
- G23A zero amplification;
- explicit exact arithmetic / numerical weighting boundaries;
- policy-access probes as controls.

Do not promote generic “policy access != enforcement” as novelty.

**Mechanism evidence — SUPPORTING, NOT HEADLINE**

Stage 5, G23C and G24B are valid causal results, but the obvious-reviewer compression

> “if target semantics are already present, the resulting rule state can naturally be
> more target-specific / carry more target-conditioned policy information”

makes the current mechanism finding too obvious to serve as the third headline
contribution.

G24B resolves the donor-vs-recipient technical confound; it does not by itself defeat
that novelty compression.

### G23C-R status

**HOLD. NO COMPUTE.**

A fresh replication would improve robustness of the same parent mechanism claim but
would not repair its novelty if the parent claim remains reviewer-obvious.

G23C-R may be reconsidered only if:
1. a non-trivial parent mechanistic question is first identified; and
2. the fresh replication becomes necessary evidence for that question.

### Active work *(updated 2026-09-25 — the earlier blanket target-model
ban is superseded by the tagged two-phase G26A plan)*

Authorized now:
- paper restructuring and writing;
- novelty audit / literature search;
- G26A zero-model work (design, analyzer, tests, records) — the third RQ
  question was found and frozen as G26A; no further "search for a
  genuinely non-obvious third RQ" is pending;
- design-only thought experiments and no-model checks;
- **G26A Phase A ≤ 14,560 rows (mistral-small-24b selector) — ONLY after
  the Phase-A design tag `g26a-load-bearing-phasea-design-v1` AND the
  user-owned STATUS flip #1; G26A Phase B likewise ONLY after flip #2.**

Not authorized:
- G23C-R forward passes;
- any target-model generation outside the tagged, flipped G26A plan
  (explicitly supersedes the earlier blanket "any new target-model
  generation" ban, which would have wrongly refused the approved G26A
  Phase A);
- new layer/site/model sweeps;
- carrier redesign;
- experiments whose headline reduces to “give target semantics, then the state is more
  target-specific.”

Any future compute must first pass the G18 triviality veto:
treatment-does-not-contain-the-answer, reviewer one-line test, two live accounts under
the same visible task content, and an unexpected-result requirement.
