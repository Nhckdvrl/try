# G24A Layer-2 registration: candidate RQ + competing-accounts prediction table

**Status**: Layer 2 entered (user ruling, 2026-09-25, after review of the reversibility-audit commits `7feb552` → `3d5e644` → `0eac70d` → `b72a006`). This document registers wording and discriminating predictions. **No prereg, no model runs, no kill gates are created here.** Candidate wording, NOT a paper claim.

Inputs this document quotes (all recomputed/verified before quoting): `results/g24a/g24a_analysis_v1.{md,json}` (post-fix full rerun `e4319cb` → analysis `e3e954d`), `results/discovery/g24a_reversibility_v1.{md,json}` (`3d5e644`/`0eac70d`), rationale coding `b72a006`, fresh-pair census `99d1580`/`9fc55fe`.

## 0. Registered candidate RQ (wording; not frozen)

> **Superseded 2026-09-25 post-P1 (user ruling) — retained for provenance, see §7.3.**
> The old analytic reading ("contradictory evidence is harder to un-integrate") was withdrawn as insufficiently supported (A_dec = 2.63; 363/960 claim×model cells with A<0). The live candidate RQ2 is now the counterfactual-reconstruction question in §7.3.

- **RQ (analytic)**: Is retrospective evidence exclusion genuinely effective, or does apparent success mask a polarity-dependent asymmetry in evidence reversibility?
- **RQ (experiment)**: Can LLMs retract supporting and contradicting evidence symmetrically once instructed to disregard it?
- **中文**: LLM 在已经使用一条 evidence 后，能否对支持性证据和反驳性证据进行对称的撤销？
- **Candidate finding (NOT a claim)**: Retrospective exclusion appears successful in aggregate because opposite errors cancel: supporting evidence is often over-retracted, whereas contradicting evidence remains behaviorally active. *(This cancellation sentence survives P1 — see §7.3 — but its old mechanistic gloss does not.)*

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

**Executed 2026-09-25**: 4,800 rows, integrity PASS (`c4c930f`), frozen readout `results/g24a/g24a_p1_analysis_v1.{md,json,_cells.csv}` (`e7800bc`); interpretation and RQ2 reframing in §7.

## 5. Novelty first pass (user-run 2026-09-25): SERIOUS PASS, no direct owner found yet

- Belief-R (EMNLP 2024): revision after *new* evidence — not deletion of an already-used evidence with polarity comparison.
- Dynamic Epistemic Friction (CoNLL 2025): integration resistance of conflicting propositions — integration/update, not retraction asymmetry.
- ConflictScore (arXiv 2026) / HealthContradict (2026): simultaneous supporting+contradicting evidence handling — conflict acknowledgement, not reversibility of the same evidence.
- Over-Searching (EACL 2026): negative evidence especially affects abstention — a related signal (negative evidence has strong behavioral effect), but not reversibility.
- Human-judgment parent (1990, professional auditors update more from negative evidence): the *broad* positive/negative evidence asymmetry is NOT claimed as novel.
- **Scope discipline**: novelty must land on *LLM inference-time evidence control / explicit retrospective exclusion / same-evidence reversibility*. A wider search is still required before any freeze (pending).
- **Second pass (same day, post-P1)**: see §8 — CAP (ACL 2026), In-Context Knowledge Unlearning (Findings ACL 2025), EMNLP 2025 misinformation correction, human continued-influence effect. Scope narrowed to *counterfactual correctness of evidence-control operators*.

## 6. Governance

- All numbers in §1–§3 are discovery-layer observations from the post-fix full rerun; `e3e954d` lineage is discovery-only, not a strict prereg-confirmatory rerun (selection pass ran on the old claims) — carry this caveat in any write-up.
- Any item-level claim must carry the temp-0 retest caveat (selection vs main pass, identical prompts, 548 non-rewritten items / 1,644 rows: exact-equal 71.8% of rows, argmax flips 6.4%, pearson 0.981 — `g24a_data_quality_audit_v1.md` §E).
- No models run, no prereg created, no gates added by this document. Pilot P1 was ruled by the user on 2026-09-25 and is executed per §4 (spec frozen pre-run at `1497c63`).
- Post-P1 update (2026-09-25): RQ2 reframing (§7), novelty second pass (§8), Pilot P2 spec (§9), and matched qualitative reading spec (§10) all ruled by the user after P1 results; this document still creates no prereg, no gates, and no model runs by itself — P2 material selection is zero-model and the A≥10-style gates stay permanently dead (§9).

## 7. P1 outcome + RQ2 reframing (user ruling, 2026-09-25, post-P1)

P1 executed per §4: 4,800 rows, integrity PASS (`c4c930f`), frozen readout `results/g24a/g24a_p1_analysis_v1.{md,json,_cells.csv}` (`e7800bc`). No gates, no p-values, no bootstrap, no selection.

### 7.1 The four quantities (pooled, 5 models × 192 claims)

| quantity | ExcludePost | StrongExcludePost | CounterfactualDeletePost |
|---|---|---|---|
| A (leverage) | 7.99 | 7.99 | 7.99 |
| C_k | −19.71 | −18.15 | −18.86 |
| R_k | −11.72 | −10.16 | −10.87 |
| D_k = abs(Y_k − Y_base) | 28.26 | 22.64 | 23.64 |
| C_k / −A (display) | 2.47 | 2.27 | 2.36 |

A by polarity: increase 13.35, decrease 2.63. **363/960 claim×model cells have A<0** (kept and displayed as leverage; never filtered).

Trajectories (mean Y, pooled): increase **79.09 → 92.44 → 50.24 / 60.12 / 60.62**; decrease 22.78 → 20.15 → 17.36 / 24.14 / 26.06 (Base → Admit → Exclude / Strong / CF).

Per polarity: inc C_k −42.20 / −32.32 / −31.82, inc R_k −28.85 / −18.97 / −18.47, inc C/−A 3.16 / 2.42 / 2.38; dec C_k +2.79 / −3.99 / −5.91, dec R_k +5.42 / −1.36 / −3.27.

Within-pair dC_k = C_inc − C_dec: ExcludePost **−44.98 (86.7% negative)** → Strong **−28.33 (71.0%)** → CF **−25.91 (69.8%)**; mean negative in all 15 model×operator cells (discovery replicate: −42.28 / 89.1%).

Descriptive reading vs the §4 map: closest to **Q** — Strong and CF improve similarly and a lot; not P/S in full (increase side never returns to Base under any operator: R_inc −28.85/−18.97/−18.47, C/−A 3.16/2.42/2.38, i.e. overshoot below Base); not R (both new operators are effective); residual polarity asymmetry persists under both new operators → instruction strength explains a large part, not all.

### 7.2 Withdrawn reading

**"Contradictory evidence is harder to un-integrate" / "negative belief persistence" is withdrawn as a candidate finding.** Grounds: A_dec = 2.63 (admit effect at floor) and 363/960 cells with A<0 — many decrease claims already score low at Base, so retraction-era low scores cannot be interpreted as persistence of a negative update. Any reviewer would reject it on those numbers.

### 7.3 Reframed candidate RQ2 (supersedes §0; wording as ruled by user, 2026-09-25)

- **RQ2 (analytic)**: Can language models recover the counterfactual no-evidence judgment after evidence has already been observed?
- **RQ2 (中文)**: LLM 看过一条 evidence 后，能否通过自然语言撤销指令，恢复到“如果从未看过这条 evidence”时本应有的判断？
- **Ideal target**: Y_retract ≈ Y_base. P1 answer: **usually not** — D_k = 28.26 / 22.64 / 23.64, including under the explicit wording “exactly as you would have if Evidence E had never been shown”.
- **Core observation**: **Natural-language retraction is not counterfactual deletion.** remove(E) ≠ return to the pre-E state; retraction can **overcorrect**: support side 79.09 → 92.44 → 60.62 — after deleting E the claim sits ≈18 points below its own pre-evidence baseline (admit was worth +13; deletion costs −18 relative to Base).
- **Strong ≈ CF** (dC −44.98 → −28.33 → −25.91): “act as if unseen” did **not** provide a special deletion operator; the gain is generic instruction strength/compliance, and a large direction-dependent distortion remains.
- **Cancellation reading preserved**: REI_post ≈ 0 does not mean retrospective exclusion works — it can be **support over-correction + contradiction-side under-correction ≈ 0**.
- **Candidate finding (NOT a claim)**: “Retrospective exclusion does not reconstruct the no-evidence counterfactual. Stronger exclusion instructions reduce some of the apparent polarity asymmetry, but judgments remain systematically displaced from their pre-evidence baseline, including substantial over-correction after supporting evidence.”
- **Paper layer**: RQ1 prospective exclusion → no, substantial prospective leakage; RQ2 retrospective → does not necessarily restore the no-evidence judgment; aggregate success conceals non-neutral retraction behavior.

## 8. Novelty second pass (user-run 2026-09-25; scope narrowed)

Prior work to address positively:

- **CAP (ACL 2026)** — prompt-driven unlearning: RL optimizes prompts to suppress target knowledge; knowledge recovers after prompt removal. → We do **not** package as prompt unlearning (no parametric deletion, no optimized prompts).
- **In-Context Knowledge Unlearning (Findings ACL 2025)** — test-time selective forgetting via fine-tuning; the “forgetting” may be last-layer output suppression. → Different object: fine-tuned suppression vs. causal removal of a *just-observed context evidence* that already changed judgment.
- **EMNLP 2025 (misinformation in reasoning)** — LLMs contaminated during reasoning correct poorly when later explicitly asked; earlier correction works better. → “LLM 看过东西以后改不回来” is **not** novel by itself.
- **Continued influence effect (human cognition)** — retracted misinformation keeps influencing reasoning even when the retraction is believed. → The broad phenomenon is old; **not claimed**.

**Scope discipline (what we claim)**: not parametric knowledge deletion, not optimized forget scores, not “first to observe retracted information still influences reasoning”. The object is a specific evidence just admitted into context that already changed a judgment, removed by a natural-language ruling, scored by **counterfactual correctness** — restoring the exact no-evidence judgment. The novelty target: *evidence-control operators exhibit residual, overshoot, and polarity-dependent distortion* (incl. support-side over-correction), i.e. removal ≠ counterfactual deletion.

Verdict: **SERIOUS, no direct owner found.** Wider search with this narrowed scope still required before any freeze (pending).

## 9. Pilot P2 — same-claim counterfactual reconstruction (spec as ruled; frozen pre-run; user 2026-09-25)

**Why**: P1's largest confound — increase and decrease are *two different claims* (parametric prior, linguistic form, credibility differ); A_dec ≈ 0 exposes it. P2 **locks the claim**: same claim, same Y0, opposite evidence polarities.

**Material**: VitaminC real-revision SR pairs — same claim + one natural SUPPORT evidence + one natural REFUTE evidence (zero-model audit `results/audits/vitaminc_triplet_audit_v1.md`: CLEAN, N_SR = 92,764, 1S+1R canonical 92,735). **G27A removal-vs-negation hypothesis stays KILL — this reuses material only, not the hypothesis and none of its gates.**

**Selection (zero-model data validity only; fixed seed in the freeze script)**: 200 brand-new real-revision same-claim pairs. Criteria: real revision; same claim; one natural SUPPORT evidence; one natural REFUTE evidence; dedup; as non-template as practical. **No model-conditioned filtering of any kind. The old “both directions A≥10” gate is permanently dead and must not be resurrected.** A is displayed as a continuous variable only.

**Cells (9 per claim)**: `Base` (claim only — evidence-free, renders byte-identical for both arms, so Y0 is *the same number* by construction) + {AdmitPost, ExcludePost, StrongExcludePost, CounterfactualDeletePost} × {arm+ (E_support), arm− (E_refute)}. G24A `AdmitPost`/`ExcludePost` wording character-identical; Strong/CF verbatim as in §4.

**Run**: 5 panel models × 200 claims × 9 cells = **9,000 decision rows**; full panel, no scientific stop, no gates, no staged running. (Runner mechanics: arm+ items × all 5 kinds, arm− items × 4 kinds — verified base prompt evidence-free.)

**Estimands** (evidence polarity e ∈ {+1 support, −1 refute}, shared Y0):
- A_e = e · (Y_admit,e − Y0) — leverage, displayed continuous, never filtered
- R_{k,e} = e · (Y_k,e − Y0) — polarity-aligned residual
- **Ideal deletion: R_{k,+} = R_{k,−} = 0** (and the between-polarity gap R_{k,+} − R_{k,−} = 0)

**Both outcomes informative (not a lottery)**: (a) same-claim asymmetry persists → evidence polarity itself affects reversibility; (b) asymmetry largely disappears → P1/G24A asymmetry was mainly claim prior/form (Account B), not evidence polarity.

## 10. Matched qualitative reading — one small precise round (user 2026-09-25)

Purpose (single question): **why does the claim drop below its own Base after support evidence is retracted?** Not a full 4,800-row coding.

- **Sample**: 12 group×model cells per model × 5 models = **60 cells**, mechanically covering three trajectory strata. Strata (all computed on the increase/support-side trajectory of one (group, model) cell from `g24a_p1_analysis_v1_cells.csv`; thresholds fixed here pre-reading; first match wins):
  1. **overshoot** — R_CF ≤ −10 (CFDelete pushes the support claim below its own Base);
  2. **exclude-bad-improved** — R_Exc ≤ −15 and R_Strong ≥ R_Exc + 10 and R_CF ≥ R_Exc + 10;
  3. **near-base** — |R_CF| ≤ 5.
  4/stratum/model, fixed-seed sample within stratum (all available if <4; report shortfalls). No hypothesis-flattering substitutions.
- **Per cell**: read *both* claims' rationales at Base, Admit, Exclude, Strong, CF (10 rationale readings/cell → 600 total).
- **Labels (behavioral description only — explicitly NOT mechanism)**: `still_uses_evidence`, `no_evidence=>uncertain`, `no_evidence=>claim_less_likely`, `exclusion_implies_distrust`, `reconstructs_prior/world_knowledge`, `other`.
- **Diagnostic payoff**: if support-overshoot rationales say “without E supporting, the claim is less likely”, the model is executing `remove support ⇒ penalize claim` rather than counterfactual belief restoration — explaining Y_CF < Y0.

## 11. Pilot P3 — operator-only control (spec as ruled; wording frozen pre-run; user 2026-09-26)

**Motivation (post-P2 reading, user 2026-09-26)**: the structure that grew out of P2 is not “refute is harder to retract” but a more basic one — retraction largely erases evidence polarity (56.32 → 12.01 separation) yet does **not** restore Y0; it lands the judgment at a **claim-dependent but strongly compressed** center (artifact `results/g24a/g24a_p2_compression_v1.md`: corr(M_CF, Y0) = 0.701, M_CF ≈ 25.84 + 0.385·Y0, mean|Y0−50| = 22.55 → mean|M_CF−50| = 12.57) — *retraction-induced confidence contraction*. P3 asks the one question this leaves open: **is the compressed attractor a state trace of the processed evidence, or does the retraction / evidence-unavailable language frame itself recalibrate confidence?**

**Design (no new dataset, no fresh sample — still explaining the discovery phenomenon)**: the same **200 discovery claims** (discovery-only lineage, `g24a_p2_figures_v1.md` §0), 5 panel models, **no arms** (support/refute evidence never rendered). **5 conditions × 200 claims × 5 models = 5,000 decision rows.**

**Conditions (wording FROZEN here before any output; exact literals live in `src/conditions_g24p3.py`, verified verbatim by `scripts/verify_g24a_p3_prompts.py`):**

1. **base (Base-rerun)** — byte-identical to the P2 Base prompt (claim only). Re-run absorbs temp-0 variation instead of comparing against last round's Base.
2. **prior_only** — no Evidence E block; one note block, exactly: `No additional evidence is available. Judge the claim using only your existing/background knowledge.` — does merely *instructing* prior-only judgment contract the score?
3. **withheld_only** — `EVIDENCE E` / `[Content unavailable.]` block, then the original question, **no ruling** — does “an evidence exists but you cannot see it” frame induce uncertainty?
4. **withheld_strong** — same `[Content unavailable.]` block + the P1/P2 **StrongExcludePost** ruling verbatim (`conditions_g24p1.STRONG_EXCLUDE_RULE`).
5. **withheld_cf** — same `[Content unavailable.]` block + the P1/P2 **CounterfactualDeletePost** ruling verbatim (`conditions_g24p1.CF_DELETE_RULE`).

**Safety invariants (verifier-enforced)**: the base prompt is byte-identical to the P2 base prompt for every claim; the two rulings are byte-identical to the P1 module constants; **no real evidence text appears in any P3 prompt** (asserted against all 200 source evidence pairs); the withheld block is byte-identical across the three withheld conditions.

**Core comparisons (descriptive; no gates, no claim selection, no evidence cell may ever be added)**:

- **C1**: Y_prior_only − Y_base — if this alone contracts substantially, bare `Base` and “explicitly use prior knowledge” are not calibration-equivalent and RQ2 wording must account for it.
- **C2**: Y_withheld_only − Y_base — if this contracts toward 50, merely *knowing* an evidence exists but is unavailable induces uncertainty contraction.
- **C3**: Y_withheld_cf vs **M_CF^actual** (the P2 claim-level center) — if the two coincide, the attractor needs no actual evidence: **operator-induced recalibration, not persistent evidence content**; if withheld_cf ≈ Y0 while actual-evidence CF stays off Y0, processed evidence leaves a state-dependent trace.
- Also read descriptively: withheld_strong vs M_strong^actual, and the base rerun vs P2 base (temp-0 drift calibrates C1/C2).

*(These are interpretation branches with no decision role — explicitly not gates.)*

**Candidate finding wording (not frozen, not an RQ, no prereg)**: “Natural-language retraction largely removes evidence-specific direction but does not restore the pre-evidence judgment; it contracts beliefs toward a more uncertain, claim-dependent state” — upgraded only if C3 lands as above.

**Run**: 5 panel models, full 5,000 rows, one invocation per model, same runner args as P2 (mode reasoned, reason-tokens 110, max-model-len 4096, temp-0 digit expectation). Integrity via `check_g24a_p3_raws.py --require5`; analysis reports the three comparisons + the 5-condition trajectory, per-model, nothing else. **No freeze of any RQ. Run, report, stop (user: 跑完停).**

## 12. Paper shape + P4 + fresh confirmation (user ruling, 2026-09-26, post-P3)

**Structure (frozen): 3 RQs ↔ 3 headline findings, 1:1. No RQ4/RQ5, ever.** (Sasano taste: parent question a reviewer gets in one glance, most surprising finding first, no RQ/count inflation, no control-count inflation.)

- **RQ1 → F1**: *Can LLMs commit in advance to exclude evidence they have not yet seen?* **No — prospective exclusion systematically leaks.** Correct rule paraphrase at probe time, yet future evidence still enters the decision; retrospective exclusion is significantly more effective.
- **RQ2 → F2**: *After evidence has been observed, can natural-language retraction restore the counterfactual no-evidence judgment?* **No — retraction suppresses much of the evidence effect but does not reconstruct the no-evidence state.** Same-claim P2: polarity separation 56.3 → 12.0 (~79% erased) while both arms land back near Y0 in only **11/200 claims**. Headline paradox: *the model forgets the evidence's direction but not the judgment.*
- **RQ3 → F3 (promoted from candidate to headline)**: *What does retraction do instead of restoring the prior judgment?* **It behaves as a new inference operation — a confidence-compressed / recalibrated judgment state, not an undo.** P2: M_CF ≈ 25.84 + 0.385·Y0 (claim ordering kept, strongly compressed). P3: prior-only does not re-calibrate (−0.47, ≈ noise floor 1.84); the withheld frame alone moves judgments (−12.64); zero-content CF reproduces most of the attractor (WithheldCF − M_CF = +3.97, OLS slope 0.969); actual processed evidence adds extra distortion (~4 points lower, more compressed).
- **Everything else is supporting evidence, explicitly NOT an RQ**: rule-probe near-perfection; pooled REI_post ≈ 0 = cancellation; polarity asymmetry; stronger wording helps; §10 rationale CF still-use rarity; withheld-only down-pull; actual-vs-zero-content extra distortion; model heterogeneity.

**Paper experiment shape**: Exp1 prospective exclusion (**No**) → Exp2 retrospective reconstruction (**No** — direction erased, judgment not restored) → Exp3 what retraction does instead (**compressed/recalibrated state: operator/frame component + processed-evidence component**) → held-out replication (fresh items + stronger model).

### P4 — irrelevant-visible evidence control (completes RQ3; NOT a defensive confound control)

**Purpose**: decompose the post-retraction state into (i) operator/frame, (ii) having seen *any* visible decision-irrelevant content, (iii) having seen decision-relevant evidence.

**Cells (exactly 2; wording frozen here pre-run)**:

1. **`irrelevant_visible`** — CLAIM + `EVIDENCE E` (a natural but decision-irrelevant text, material rule below) + the original question; **NO ruling**. Block layout byte-mirrors P3's `withheld_only` with content present.
2. **`irrelevant_cf`** — the same evidence block + the **CounterfactualDeletePost ruling verbatim** (`conditions_g24p1.CF_DELETE_RULE`). Block layout byte-mirrors P3's `withheld_cf`.

**Material rule (mechanical, zero-model, FROZEN here pre-run)**: for each of the 200 discovery claims, the irrelevant text is drawn from the *other* rows of the audited P2 pool (`data/items/g24a_p2_pool_v1.csv`, both arms' evidence texts). Candidates must (a) come from a **different Wikipedia page** than the claim, and (b) share **no content token** — lowercased alphabetic tokens of length ≥ 5 — with the claim text or the claim's page name. Deterministic pick: per-claim RNG seeded `Random("20260928:<p2_id>")` shuffling the pool-ordered candidates, first hit wins. Screens re-asserted per item by the verifier; the target's own two evidence texts asserted absent from every P4 prompt.

**Run**: 200 claims × 2 cells × 5 panel models = **2,000 rows**, same snapshots/runner args as P2/P3.

**Read (frozen comparisons; branches have no decision role — no gates, no claim selection)**:

- `IrrelCF ≈ WithheldCF` → only decision-relevant evidence leaves the extra trace;
- `IrrelCF ≈ M_CF^actual` → seeing any evidence-like content and then retracting produces the distortion;
- in between → frame + visible-content + relevance contribute in three layers.
- Plus `IrrelVisible` vs `WithheldOnly` / `Base` (does visible irrelevant content move judgments beyond the frame alone?).

**After P4: discovery stops. No P5/P6.**

### Fresh confirmation (required before Main submission; both parts ruled)

- **Confirmation A (RQ1)**: 400–600 FEVER/SciFact natural items that **never entered discovery**; cells **Base, AdmitPost, ExcludePre, ExcludePost only**; directly confirm prospective leakage ≫ retrospective leakage. No mechanism cells, no new gates.
- **Confirmation B (RQ2+RQ3)**: **200 fresh VitaminC same-claim pairs** from the unused pool (fresh seed; blind zero-model validity review exactly as in P2). Cells ≈ 7: `Base`, `Admit+`, `CF+`, `Admit−`, `CF−`, `WithheldCF`, and `IrrelevantCF` **only if P4 shows it earns the cell (user decides post-P4)**. Confirms: admission moves judgment; retraction does not restore Y0; the contraction / operator-control pattern replicates on fresh claims.
- **Model**: add **≥ 1 ~30B modern strong model** (Qwen3-32B if present in the local cache) **to the confirmation runs only** — to answer "does this survive on a substantially stronger model?"; no mechanical 70B chase.
- **After P4 + confirmation: stop experiments; enter the paper narrative phase.**

## 13. Final confirmation freeze (user ruling, 2026-09-26, post-P4) — SUPERSEDES §12's confirmation sketch

**Discovery is DONE.** P4 was the last discovery pilot (§12 honored: no P5/P6, no new RQ, no new finding-hunting). The story is fixed at **3 RQs / 3 findings**; everything else stays supporting evidence. Risk acknowledged: all pretty results are discovery-lineage — fresh confirmation now outranks any fourth finding.

**F3 final wording (refined by P4):**
> *Retraction does not undo an evidence update. Behaviorally, it induces a new inference state: generic evidence-control framing recenters judgments, visible evidence-like content largely determines the landing point, while decision-relevant evidence produces additional confidence compression.*

`IrrelVisible = 14.94` is **explicitly demoted to supporting evidence** — NOT a headline, NOT its own section claim (risk: reviewer rabbit-hole on the EVIDENCE E header pragmatics). Headlines remain **retraction ≠ restoration** and **new compressed state**.

### 13.1 The final 3 RQ / 3 findings (frozen)

- **RQ1 — Prospective control**: Can a model commit in advance not to use evidence it has not yet seen?
  **F1 — Prospective exclusion leaks.** The model understands the ruling, yet future evidence still enters the judgment.
- **RQ2 — Counterfactual restoration**: After evidence has been observed, can retraction recover the judgment that would have existed had the evidence never appeared?
  **F2 — Suppression is not restoration.** P2: support/refute separation 56.3 → 12.0 (~79% of the evidence-direction effect erased), yet few claims return to their original no-evidence state (11/200 both arms near Y0). *forget evidence direction ≠ recover prior judgment*.
- **RQ3 — What does retraction do instead?**: If it does not undo the update, what behavioral operation does it perform?
  **F3 — Retraction produces a new, compressed inference state.** P2/P3/P4 chained: claim prior is compressed (M_CF ≈ 25.84 + 0.385·Y0); `PriorOnly` alone does not do this; control/retraction framing produces clear recentering; visible irrelevant content followed by retraction lands close to the actual mean (IrrelCF − M_CF = +0.87, within the 1.84 floor); decision-relevant evidence adds further compression (mean|Y−50|: WithheldCF 26.80 → IrrelCF 19.44 → M_CF 12.57).

No RQ4/RQ5, ever. After both confirmations run: **stop experiments regardless of outcome**; enter paper narrative phase.

### 13.2 Confirmation A — RQ1/F1 replication (frozen)

- **Material**: **500 completely fresh FEVER/SciFact natural items** from `g24a_candidates_v1.jsonl` (13,283 frozen candidates), freshness = (a) item_id in **no** item file ever rendered by any model run in this repo, AND (b) `critical_evidence` byte-disjoint from the evidence of every item file ever rendered (currently 8,985 qualify: 8,776 fever + 209 scifact).
- **Strata**: mirror discovery/P1's 2:1 — **334 fever + 166 scifact**. Per-source order: candidate ids sorted, seeded shuffle `Random("20260930:<source>")`, first 334/166 = active, remainder of the source stays in seed order as the **same-source reserve** (data-validity swaps only, decided by the zero-model review below; never by hypothesis-fitting). Normalized-claim dedup inside the sample (first seed-rank wins).
- **Cells (5, per §12 amendment — AdmitPre added as the timing-matched control)**: `base, admit_pre, admit_post, exclude_pre, exclude_post` — all wordings already frozen (G24A standard five, registered prereg §3/§9.3); items render through the **unmodified G24A module**.
- **Rows**: 500 × 5 cells × **6 models** = **15,000**.
- **Audit**: zero-model blind review — claim + evidence shown **without labels**; reviewer judges from text whether E as a matter of fact SUPPORTS or REFUTES the claim (fixed decision rule; entailment/omission/compatibility/non-unique/reversed/NEITHER → invalid), then the build compares against the official direction: agreement = keep, mismatch/NEITHER = data error → swap from same-source reserve in seed order. No model output is read at any point (asserted by the freeze/build scripts).
- **No mechanism cells.**

### 13.3 Confirmation B — RQ2/F2 + RQ3/F3 replication (frozen)

- **Material**: **200 completely fresh VitaminC real-revision same-claim support/refute pairs**, case/claim **disjoint from everything P2/P3/P4 used**. Same filter chain as `freeze_g24a_p2.py` (F1 purity, F2 canonical 1S+1R, F4 claim dedup, F5 non-template, F6 one claim per case, F7 freshness) with F7 **extended**: additionally drop any `case_id` OR normalized claim in `data/items/g24a_p2_pool_v1.csv` (all 280 P2 rows — active+reserve, covers P2/P3/P4) plus the prior VitaminC pools already in the script. **New seed `20260929`** (P2's 20260927 untouched). Active 200 + reserve 80, same-source replacement rule as P2.
- **Cells (7, frozen)**: `base`, `admit_post` (arm+), `counterfactual_delete_post` (arm+), `admit_post` (arm−), `counterfactual_delete_post` (arm−), `withheld_cf`, `irrelevant_cf`.
  - **`irrelevant_cf` IS in** (user: P4 proved it is F3's key evidence, not a pad control); **`irrelevant_visible` is OUT** (the 14.94 down-pull stays discovery/supporting).
  - Arms render through the unmodified G24A/P1 modules (byte-frozen wordings); `withheld_cf` via conditions_g24p3 (content-free); `irrelevant_cf` via conditions_g24p4 reading the **control arm** item's `critical_evidence`, which carries an irrelevant text sampled by §12's frozen material rule (page-disjoint + len≥5 token-disjoint + `Random("20260929:<p2_id>")`).
  - Three items per claim: `plus` (support evidence), `minus` (refute evidence), `control` (irrelevant text) — 600 items; `base` issued on `plus` only.
- **Rows**: 200 × 7 cells × **6 models** = **8,400**.
- **Audit**: P2's blind protocol exactly — claim + Evidence A + Evidence B **unlabeled**; one must as a matter of fact support and the other refute the claim (fixed decision rule); invalid → same-source reserve swap in seed order. Zero model output.

### 13.4 Model + run args (frozen)

- **Panel**: the existing 5 (mistral-small-24b, llama31-8b, qwen3-8b, qwen35-9b, gemma3-12b) **+ Qwen3-32B ONLY** (`models--Qwen--Qwen3-32B/snapshots/9216db5781bf21249d130ec9da846c4624c16137`, 62G complete in cache). **No Qwen3.5-27B, no model-zoo expansion.** The single goal: one reviewer-proof sentence — *"the findings also hold on a substantially stronger 32B model."*
- **Runner args**: identical to P2–P4 (mode reasoned, reason-tokens 110, max-model-len 4096, tp 1, gpu-frac 0.85, eager, temp-0 digit expectation). Qwen3-32B runs at the same args; tp 1 on one A100.

### 13.5 Primary estimands + expected directions (registered pre-run; reporting, NOT gates)

**No KILL gates, no thresholds, no "must pass" lines — nothing like 70% / 10 points may be introduced.** What is frozen here is only *what gets reported* and the *expected direction*; results are reported with **paired bootstrap 95% CIs (over claims)** and **per-model consistency (n/6)** — this CI reporting is the user's explicit order for confirmation and supersedes the standing no-bootstrap rule *for these two reports only* (still: no p-values, no selection).

- **ConfA (RQ1)** — sign-normalize every effect by `critical_direction` (+1 increase, −1 decrease; signed effect = d × (Y_cell − Y_base)). Report all five cell means, then:
  - **E1** `signed(ExcludePre − Base)` — prospective leakage; **E2** `signed(ExcludePost − Base)` — retrospective leakage; **E3** `signed(AdmitPre − Base)` and **E4** `signed(AdmitPost − Base)` — timing-matched admitted baselines; leak fractions E1/E3 and E2/E4.
  - **Expected**: E1 ≫ E2 (prospective leaks ≫ retrospective); E2/E4 close to 0 (retrospective ≈ removal); E1/E3 substantially > 0. CIs + per-model consistency for E1−E2, E1/E3, E2/E4.
- **ConfB (RQ2)** — (i) **separation_admit** = mean(Y_Admit+ − Y_Admit−) vs **separation_cf** = mean(Y_CF+ − Y_CF−): expected separation_cf ≪ separation_admit (direction erased); (ii) **reconstruction error** = mean|Y0 − M_CF| and mean(Y0 − M_CF) with M_CF = (Y_CF+ + Y_CF−)/2: expected still large (≠ ~0) — suppression without restoration. CIs + per-model consistency on both.
- **ConfB (RQ3)** — claim-level contraction: corr(M_CF, Y0) > 0 with OLS slope < 1 (discovery: 0.701 / 0.385); center ordering expected `WithheldCF > IrrelCF ≈ M_CF` in mean and `WithheldCF > IrrelCF > M_CF` in mean|Y−50| (discovery: 49.18 / 46.07 / 45.20 and 26.80 / 19.44 / 12.57). CIs on the ordering gaps; per-model consistency.

**Interpretation rule**: whatever comes back — full replication, shrunk effects, or a reversed detail — gets reported as-is. **After ConfA + ConfB run and report: experiments stop.** Paper structure stands (exclude future evidence → No; undo observed evidence → not by restoring; what instead → a new, compressed inference state).

**§13 pre-sampling erratum (same day, BEFORE any material was written or inspected)**: the ConfA freeze script's reserve-safety floor is ≥ 40 items per source (scifact qualifies 209 → 166 active + 43 reserve; the initial script floor of +100 was arithmetic over-tight). Strata (334/166), seeds, cells, estimands, everything else in §13 unchanged. `freeze_g24a_confa.py` failed on the floor assertion before writing any pool/review file — nothing was sampled or seen.

## 14. RQ3 explanation experiment — second-order / meta-evidence hypothesis + Meta-Neutral Retraction (user ruling, 2026-09-26, post-ConfA+ConfB) — SUPERSEDES §13.1/§13.5's "experiments stop" clause FOR THIS EXPERIMENT ONLY

**The ruling.** ConfA + ConfB are reported (§13.5 readouts, `eaa2194`). The user rules the experiment phase does **not** end there: the paper currently is a strong behavioral finding paper, and the missing step is phenomenon → explanation → intervention. One reopening only, framed as **RQ3's explanation experiment** — NOT RQ4, no new RQ, no new finding-hunting. §13.1's "no RQ4/RQ5, ever" **stands**; the 3 RQ / 3 F freeze **stands**; this experiment either supplies a mechanism-level explanation for F3 or comes back negative, reported as-is either way.

**The hypothesis (registered before any run).** The retraction ruling does two things at once: (a) it suppresses the first-order content of E (already ~87% of direction erased), and (b) it *adds* second-order information R = "an evidence was shown here and then retracted." The model may comply with (a) while still *conditioning on R itself*: it computes f(C, R), not f(C). Prediction shape: neutralizing the informational content of R improves counterfactual restoration (CRE ↓, reconstruction slope ↑ toward 1) while support/refute separation stays ≈ 0 — first-order suppression is unchanged, only the meta-evidence is removed.

### 14.1 Material (no new sampling)

- **Pool**: the original 200 discovery same-claim pairs — `data/items/g24a_p2_v1.jsonl` (400 arm items) + P2's id lists, byte-reused. No new claims, no new evidence, no new validity review (P2's blind audit already covers this material).
- **Y0 anchor**: `base` re-issued on the `plus` arm in the same run (byte-identical to P2's Base prompt) — same-batch absorption of temp-0 drift, exactly P3's precedent.

### 14.2 Operators (wording frozen verbatim, pre-run)

- **`meta_neutral_post` (MNR)** — G24A POST layout (CLAIM, EVIDENCE E, RULING); RULING =
  > Evidence E must have no influence on your judgment. Importantly, the fact that Evidence E was shown, withheld, or retracted is itself purely procedural and provides no information about the claim or about the truth or reliability of Evidence E. Judge exactly as if neither Evidence E nor any retraction event had occurred.

  (user's three sentences, verbatim; the middle sentence is the second-order neutralizer)
- **`random_reason_post`** — RULING = `CF_DELETE_RULE + " " + RANDOM_PROCEDURAL_REASON`, i.e. P1's CF-delete text **byte-identical** (first-order suppression held fixed) + user's sentence:
  > Evidence E was excluded by a random administrative procedure that is independent of its content, truth, reliability, and the claim.

  Composition decision (flagged for veto): reason appended to the CF core so the only difference from the CF baseline is the second-order reason information; without it the single sentence's "was excluded" would leave first-order suppression implicit.
- **Reserved, NOT run this round**: the reverse control "Evidence E was excluded because its reliability is uncertain." (`uncertain_reason_post`) — user: not urgent. It can be added later as a 2,400-row follow-up (2 cells × 200 × 6) without re-running anything else.
- Dispatch: new module `conditions_g24meta`, condition-name-first branch in `schema._blocks` (same proven pattern as g24p1/g24p3/g24p4); the four legacy operators render through the **unmodified** G24A/P1 modules, so their prompts are character-identical to P1/P2 by construction (verified pre-run).

### 14.3 Cells + rows (frozen)

- **13 cells per claim**: `base` (plus only) + {`admit_post`, `exclude_post`, `strong_exclude_post`, `counterfactual_delete_post`, `meta_neutral_post`, `random_reason_post`} × {plus, minus}.
- The four legacy operators are **re-run in this batch** (not read from committed P1/P2 raws) so the whole CRE table is self-contained and 6-model complete — including Qwen3-32B, which P1/P2 never ran — and every cell shares one batch's temp-0 anchor. Cost accepted: 200 × 13 × 6 = **15,600 rows** (plus 1,400/model, minus 1,200/model).
- **Models + runner args**: §13.4 unchanged (5 + Qwen3-32B snapshot `9216db5781bf21249d130ec9da846c4624c16137`; reasoned, 110, 4096, tp1, 0.85, eager, temp-0).

### 14.4 Estimands + expected directions (registered pre-run; reporting, NOT gates)

Same discipline as §13.5: **no thresholds, no p-values, no gates, no selection**; paired bootstrap 95% CIs over claims (B = 10,000, seed `g24a_meta_ci_v1`) + per-model consistency n/6; registered expectations are quoted, never evaluated as pass/fail; everything reported as-is.

- **CRE table (the intervention-layer criterion)** — for op ∈ {exclude_post, strong_exclude_post, counterfactual_delete_post, meta_neutral_post, random_reason_post}: **CRE_op = mean|Y0 − Y_op|** (pooled over (model, claim); M_op = (Y_op+ + Y_op−)/2) and signed mean(Y0 − M_op). Registered expectation: **CRE(MNR) < CRE(CF)**, **CRE(random) < CRE(CF)**; trajectory relative to the committed CF restoration error is reported for context.
- **Separation** — separation_op = mean(Y_op+ − Y_op−) per operator: expected **separation(MNR) ≈ separation(CF) ≈ 0, ≪ separation(admit)** (meta-neutralization must NOT re-open the first-order direction).
- **Reconstruction trajectory** — claim-level corr(M_op, Y0) and OLS slope(M_op, Y0) for every operator: expected **slope(MNR) > slope(CF)** moving toward 1 (discovery CF: 0.701 / 0.385; fresh ConfB: 0.635 / 0.320), same direction for corr.
- **Registered conceptual framing**: the report introduces **Counterfactual Restoration Error (CRE) = |Y_R − Y0|** as *the* retraction-success criterion — evidence suppression (forget rate) ≠ successful retraction; the ConfB pair (87% direction erased, ~30-point restoration error) is the standing motivating example. Internal (layerwise / patching) analysis is explicitly **out of scope for this round** — it is a later step only if this round warrants it, decided by the user.

**Interpretation rule**: full restoration, partial restoration, or none — reported as-is with CIs and n/6. If MNR does not restore, F3 stands as a behavioral finding without the second-order explanation, and that is the report. Machinery/verification discipline (pytest before machinery commits, every step pushed, banned lines, housekeeping) unchanged from §13.

### 14.5 Run-environment addendum (registered pre-run, 2026-09-26; user order: use the free cards on fvcrc10–15 — "只要是空的卡能用就行")

- **Census (verified pre-run)**: this working node **fvcrc20** (4× RTX PRO 6000 96GB, driver 580.82.07) fully occupied by another user's serving processes; **fvcrc13/fvcrc15** (4× A100 80GB each) occupied by another user's vLLM serves; **fvcrc11** refuses SSH (direct and via the fvcrc00 proxy); **fvcrc14** has one failed GPU (NVML "Unknown Error"; 3× RTX A6000 48GB usable, not needed); **fvcrc10 = 4× A100 80GB PCIe free, fvcrc12 = 2× A100 80GB PCIe free → six free cards, one per model**. (fvcrc16–19 — 4× 48GB each, free — exist beyond the user's list; not needed, and 48GB cannot host mistral-small-24b or Qwen3-32B under the frozen 0.85 frac.)
- **Driver constraint**: every reachable fvcrc1x node runs driver 550.54.14 (max CUDA 12.4). The frozen fgvd env (PyPI vllm 0.23.0 default wheel = CUDA-13 build, torch 2.11.0+cu130) cannot initialize CUDA there — reproduced pre-run: `RuntimeError: The NVIDIA driver on your system is too old (found version 12040)` and `vllm._C` → `libcudart.so.13: cannot open shared object file`.
- **Reconstruction** — `/home/xiang/.venvs/vllm023-cu128` (built 2026-09-26): same package **versions** as fgvd, different CUDA **build tags** only — vllm **0.23.0** (official release wheel `vllm-0.23.0+cu129`), torch **2.11.0+cu129**, torchaudio **2.11.0+cu129**, torchvision **0.26.0+cu129**, transformers **5.12.1** (load-bearing: `run_model` compiles prompts via `apply_chat_template`, so this pin is the byte-identical-prompt guarantee), huggingface-hub **1.20.1**, tokenizers **0.22.2**. CUDA-12.9-on-driver-12.4 relies on CUDA-12 minor-version compatibility and is validated end-to-end by the smoke run below.
- **Invocation**: `G24A_META_PY=/home/xiang/.venvs/vllm023-cu128/bin/python scripts/run_g24a_meta.sh <gpu> <tag>` — the script's default `PY` remains the frozen fgvd path; the override is a parameter, not an edit of the contract.
- **Unchanged (frozen)**: model snapshots incl. Qwen3-32B `9216db5781bf21249d130ec9da846c4624c16137`; runner args (reasoned, 110, 4096, tp1, 0.85, eager, temp-0); prompts/items/id lists (verifier green: 2,800 prompts, wordings verbatim, legacy cells byte-identical); the 13-cell / 15,600-row contract; estimands + bootstrap seed `g24a_meta_ci_v1`; no-gates discipline.
- **What changes vs §12–13**: GPU architecture (A100 Ampere vs RTX PRO 6000 Blackwell), driver, and CUDA build tags. All six models of this panel run on this one substrate, so every §14 contrast is internally consistent and Y0-anchored within the batch; committed discovery/ConfB numbers remain descriptive context only, as registered in §14.4.
- **Machinery validation (pre-run)**: smoke = qwen3-8b on fvcrc10 GPU0 with the reconstruction env → both arms written (28+24 rows), unparsed=0, digit-mass<0.5=0, checker `--smoke` exit=0.
- **Cell assignment**: fvcrc10 — GPU0 mistral-small-24b, GPU1 qwen3-32b, GPU2 llama31-8b, GPU3 qwen3-8b; fvcrc12 — GPU0 qwen35-9b, GPU1 gemma3-12b.
- **Flagged risk (accepted as-is; frac stays frozen)**: 0.85×80GB = 68GB vs Qwen3-32B ≈65.6GB weights + 4096-ctx KV/activations — tight; an OOM would be reported as-is and surfaced to the user.
