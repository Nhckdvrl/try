# G24A Layer-2 registration: candidate RQ + competing-accounts prediction table

**Status**: Layer 2 entered (user ruling, 2026-09-25, after review of the reversibility-audit commits `7feb552` → `3d5e644` → `0eac70d` → `b72a006`). This document registers wording and discriminating predictions. **No prereg, no model runs, no kill gates are created here.** Candidate wording, NOT a paper claim.

Inputs this document quotes (all recomputed/verified before quoting): `results/g24a/g24a_analysis_v1.{md,json}` (post-fix full rerun `e4319cb` → analysis `e3e954d`), `results/discovery/g24a_reversibility_v1.{md,json}` (`3d5e644`/`0eac70d`), rationale coding `b72a006`, fresh-pair census `99d1580`/`9fc55fe`.

## 0. Registered candidate RQ (wording; not frozen)

- **RQ (analytic)**: Is retrospective evidence exclusion genuinely effective, or does apparent success mask a polarity-dependent asymmetry in evidence reversibility?
- **RQ (experiment)**: Can LLMs retract supporting and contradicting evidence symmetrically once instructed to disregard it?
- **中文**: LLM 在已经使用一条 evidence 后，能否对支持性证据和反驳性证据进行对称的撤销？
- **Candidate finding (NOT a claim)**: Retrospective exclusion appears successful in aggregate because opposite errors cancel: supporting evidence is often over-retracted, whereas contradicting evidence remains behaviorally active.

Story arc (user, 2026-09-25): RQ1 — future evidence is hard to exclude (REI_pre +0.541 [+0.478,+0.604] p=0.0000, P1 PASS) → RQ2 — after the fact, aggregate removal looks like it works (REI_post pooled −0.072 [−0.161,+0.017] p=0.1170) → **Layer 2 — the retrospective "success" is itself an artifact**: the near-zero pooled value is arithmetic cancellation of two large opposite-signed errors. RQ2 does **not** need to explain prospective failure.

## 1. The cancellation (recomputed exactly from `g24a_analysis_v1.json`)

| pooled-4 stratum | REI_post | n rows |
|---|---|---|
| fever SUPPORTS | **−0.718** [−0.851,−0.585] p=0.0000 | 694 |
| fever REFUTES | **+0.596** [+0.483,+0.705] p=0.0000 | 632 |
| scifact SUPPORT | **−0.872** [−1.039,−0.708] p=0.0000 | 363 |
| scifact CONTRADICT | **+0.924** [+0.814,+1.033] p=0.0000 | 318 |
| **pooled-4** | **−0.072** [−0.161,+0.017] p=0.1170 | 2007 |

Arithmetic identity (verified to machine precision): row-weighted mean of the four cells = −0.071823 = pooled REI_post (abs diff 2.8e−17; Σ n = 694+632+363+318 = 2007 ✓). Every |cell| ≥ 0.596 — roughly 8× the pooled magnitude. **support oversuppression + contradiction persistence ≈ 0 by construction.**

Discovery-layer companion (exact-evidence pairs, A/C estimands): pooled dC_pre −3.03 / 69.4% negative → dC_post −42.28 / 89.1% negative (per model × source all negative). Non-explicit-negation subset (170 pairs): dC_post **−55.67 / 91.2%** vs negation subset −29.40 / 85.3%. Rationale coding (265 cells): still-cites-for-falsity DEC side **136** vs INC 54; DEC > INC in all 5 models (41>27, 13>5, 13>0, 41>20, 28>2).

Prereg gates are recorded as-is and are not re-read here: P1 PASS, **P2 FAIL** (CI lower not > 0), C1/C2 FAIL. The cancellation reading is a discovery-layer interpretation of why pooled ≈ 0, not a gate revision.

## 2. Three competing accounts (operational statements)

- **A — Contradiction persistence / belief-state irreversibility.** Once E was integrated as a negative belief update, un-integrating is harder. Key prediction: post asymmetry ≫ pre asymmetry, and the asymmetry survives matched prior and matched leverage; it may still persist under explicit counterfactual deletion.
- **B — Claim-form / prior asymmetry.** Decrease claims are intrinsically more false-looking (negation-ish phrasing, odd content, lower parametric prior); once evidence is withdrawn the score reverts to prior, which mimics "evidence not withdrawn". Already weakened in discovery: byte-exact same evidence; non-negation subset *stronger* (−55.67/91.2% vs −29.40/85.3%); ΔY0 common support (|ΔY0|≤5/10/20 → dC_post −37~−40, 86.7–88.4%); joint |ΔY0|≤10 & |ΔA_post|≤10 → −29.90/83.3% (n=12). Confirmatory design must still pin it down.
- **C — Operator / instruction-semantics account (broadened 2026-09-25, pre-P1).** The model does not interpret an ordinary "exclude/disregard" ruling as a genuine counterfactual deletion of E; it executes some approximate, direction-asymmetric linguistic operation instead (the original *uncertainty-reset heuristic* is one special case of this class: "express less certainty" → 90→50 looks like successful removal for a supported claim, while an already-refuted claim at ~10 never rises back to baseline and thus displays as contradiction persistence). An instruction-interpretation artifact — no negative-belief irreversibility required. **The next experiment should primarily separate A from C.**

## 3. Prediction table (the one page)

| Manipulation / observation | A contradiction persistence | B claim prior/form | C operator / instruction semantics | discovery status (already observed?) |
|---|---|---|---|---|
| pre exclusion | asymmetry weak | asymmetry possible | asymmetry possible | **observed**: dC_pre −3.03, 69.4% negative (weak) |
| post exclusion | asymmetry strong | similar pre/post unless timing interacts | strong directional artifact | **observed**: dC_post −42.28, 89.1% negative (strong) |
| exact same evidence | survives | can survive | survives | **observed**: 53 byte-exact pairs, 265 group×model cells |
| prior/leverage matched | survives | should shrink strongly | survives | **observed**: survives (ΔY0/ΔA common support; joint n=12 → −29.90/83.3%) |
| explicit counterfactual "judge as if E never appeared" | may still persist | depends on prior | **should strongly improve** | **NOT RUN — prime A vs C discriminator** |
| direct baseline reconstruction request | difficult after contradiction | follows prior | should improve | **NOT RUN** |

Readout logic: ExcludePost vs CounterfactualDeletePost (same admissible information) on matched pairs — if counterfactual deletion returns **both** polarities to baseline, the asymmetry was instruction semantics (C, with B's prior contributing); if contradiction still fails to return, A gains direct support; B is pinned by the prior/leverage-matched subsets (rows 4) plus any baseline differences in Y_base itself.

## 4. Pilot P1 — spec as ruled (frozen pre-run; user, 2026-09-25)

**Material** (frozen at `1497c63`, seed 20260926, zero model output): **96 strictly-unseen (1,1) exact-evidence groups = 64 FEVER + 32 SciFact**, drawn only from `evidence_seen_in_discovery600=False` (pool verified 224 = 168+56). Zero-model data-integrity review only (does E actually support the increase claim and undermine the decrease claim?); semantic errors replaced by the **next group of the same source in frozen seed order** — never by hypothesis-flattering criteria. **128 strict-fresh (1,1) groups remain untouched as holdout.**

**Conditions (5)** — no selector, no Phase A, no funnel, no gates, no staged stopping:
1. `Base` — claim only.
2. `AdmitPost` — G24A post-admit, unchanged.
3. `ExcludePost` — **original G24A wording, character-identical**.
4. `StrongExcludePost` — *strong wording control* (pre-empts "you just wrote a stronger instruction"): "Evidence E is inadmissible. Completely disregard it when judging the claim. It must have no influence on your judgment in either direction, directly or indirectly. Judge the claim using only information available without relying on Evidence E."
5. `CounterfactualDeletePost` — "Evaluate the claim exactly as you would have if Evidence E had never been shown. Reconstruct the judgment you would have made before encountering Evidence E. Evidence E must have no influence on the answer in either direction, directly or indirectly."

`ExcludePost` and `CounterfactualDeletePost` are informationally identical. Lengths roughly comparable — **no ±2-token filler** (exploratory discriminator, not final confirmatory design).

**Run**: 5-model full panel (mistral-small-24b, llama31-8b, gemma3-12b, qwen3-8b, qwen35-9b) × 192 claims × 5 conditions = **4,800 decision rows**.

**Readout — four quantities, no KILL gate** (polarity s = +1 increase claim, −1 decrease claim):

A = s(Y_Admit − Y_Base) — leverage · C_k = s(Y_k − Y_Admit) — intervention effect · R_k = s(Y_k − Y_Base) — residual · D_k = |Y_k − Y_Base| — "did it return to pre-evidence?"

Ideal counterfactual removal: **R_k = 0, C_k = −A**. Within-pair: dC_k = C_k^inc − C_k^dec. No model-conditioned usable selection: small-A items are kept and displayed as leverage; leverage regions may be described post hoc, never used to filter.

**Outcome map (pre-run interpretation guide)**:
- **P**: Exclude asymmetry large, StrongExclude still large, CounterfactualDelete → Base with decrease side rescued → *ordinary exclusion does not implement counterfactual deletion* → paper: **"disregard" and "act as if unseen" are behaviorally different evidence-control operators.**
- **Q**: StrongExclude and CounterfactualDelete both improve a lot → generic instruction-strength / compliance, weaker scientific depth but explains the mechanism.
- **R**: neither rescues (especially decrease: Y_intervention ≈ Y_Admit) while support returns → **contradictory evidence genuinely persists after integration** → Account A strongly supported.
- **S**: CounterfactualDelete brings both sides to Base while ordinary exclusion overshoots/sticky → **the exclusion operator is semantically misimplemented** (not "negative evidence is stronger").

Any pattern answers the already-observed question (why retrospective exclusion behaves asymmetrically by polarity) — this is explanation-driven progression, not a lottery ticket.

**Deferred by ruling**: no full rationale coding this round — numerical trajectories first (Base→Admit→k per operator), matched qualitative reading only from discriminating patterns.

## 5. Novelty first pass (user-run 2026-09-25): SERIOUS PASS, no direct owner found yet

- Belief-R (EMNLP 2024): revision after *new* evidence — not deletion of an already-used evidence with polarity comparison.
- Dynamic Epistemic Friction (CoNLL 2025): integration resistance of conflicting propositions — integration/update, not retraction asymmetry.
- ConflictScore (arXiv 2026) / HealthContradict (2026): simultaneous supporting+contradicting evidence handling — conflict acknowledgement, not reversibility of the same evidence.
- Over-Searching (EACL 2026): negative evidence especially affects abstention — a related signal (negative evidence has strong behavioral effect), but not reversibility.
- Human-judgment parent (1990, professional auditors update more from negative evidence): the *broad* positive/negative evidence asymmetry is NOT claimed as novel.
- **Scope discipline**: novelty must land on *LLM inference-time evidence control / explicit retrospective exclusion / same-evidence reversibility*. A wider search is still required before any freeze (pending).

## 6. Governance

- All numbers in §1–§3 are discovery-layer observations from the post-fix full rerun; `e3e954d` lineage is discovery-only, not a strict prereg-confirmatory rerun (selection pass ran on the old claims) — carry this caveat in any write-up.
- Any item-level claim must carry the temp-0 retest caveat (selection vs main pass, identical prompts, 548 non-rewritten items / 1,644 rows: exact-equal 71.8% of rows, argmax flips 6.4%, pearson 0.981 — `g24a_data_quality_audit_v1.md` §E).
- No models run, no prereg created, no gates added by this document. Pilot P1 was ruled by the user on 2026-09-25 and is executed per §4 (spec frozen pre-run at `1497c63`).
