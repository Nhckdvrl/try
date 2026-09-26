# Research audit: evidence retraction and counterfactual restoration

Date: 2026-09-27. Formal evidence source: `ebe1dd42507e89f0fbea60b1ef1df1230f3baec9`. This is a new research assessment, not a rewrite of prior registrations. The working tree already contained unrelated uncommitted logs and G26A outputs before this audit.

## 1. One-sentence question and current answer

**When a model sees evidence and is then told to retract it, does its judgment match the judgment made without ever seeing that evidence?** In the registered ConfB setting, no. Retraction removes most of the support-versus-refute separation, while leaving large error against the same item's no-evidence judgment. This is a robust *behavioral distinction* on one task, not yet an established law of internal state inversion or multi-turn history dependence.

The most precise current label is **suppression–restoration gap**. `CRE=|Y_retracted−Y0|` is a useful item-level criterion; for the two-polarity design, the registered `|Y0−(CF+ + CF−)/2|` is a **center error**, and should be named as such. It can cancel opposite arm errors and must be accompanied by arm-wise error and residual polarity separation.

## 2. Evidence ledger, with provenance

| Source | Materials and scope | Decision rows | Standing conclusion |
|---|---:|---:|---|
| Discovery G24A | 600 FEVER/SciFact natural claim/evidence items, five models, 8 kinds | 24,000 | Discovery only after selection/review/rerun lineage. Prospective leakage and polarity-asymmetry headlines do not survive later tests. |
| P1 | 96 fresh same-evidence opposite-claim groups, 192 claims, five models × 5 conditions | 4,800 | Exploratory operator comparison; two different claims remain a confound. |
| P2 | 200 VitaminC real-revision same-claim support/refute pairs, five models × 9 cells | 9,000 | Discovery: separation 56.32→12.01; center retains rank but is compressed. |
| P3 | Same 200 P2 claims, no evidence content, five models × 5 cells | 5,000 | Discovery: frame and ruling themselves move judgments; PriorOnly has small **signed** mean but large item-wise changes. |
| P4 | Same 200 P2 claims, irrelevant visible evidence, five models × 2 cells | 2,000 | Discovery: irrelevant content produces a large negative visible-evidence effect; IrrelCF mean is near actual CF mean, but distributions differ. |
| ConfA | 500 fresh FEVER/SciFact items, six models × 5 cells | 15,000 | Held-out: prospective signed ExcludePre−Base −0.15 [−1.68,1.40], so earlier prospective-leakage headline fails; retrospective ExcludePost overshoots −15.94 [−18.19,−13.78]. |
| ConfB | 200 fresh VitaminC pairs, 600 item records, six models × 7 cells | 8,400 | Held-out main support: admit separation 62.95; CF separation 8.33 (86.8% reduction); center CRE 29.96 [28.15,31.81]; `corr(M_CF,Y0)=.635`, slope .320. |
| §14 | P2's **discovery** 200 claims, six models × 13 cells | 15,600 | MNR and random-reason wording do not materially improve CRE; MNR increases polarity separation. This is an explanation test on discovery items, not another held-out confirmation. |

VitaminC source is `tals/vitaminc` at pinned revision `be6febb...`, all train/dev/test files. Initial zero-model census: 488,904 rows; 325,724 real revisions; 92,764 real same-claim support/refute groups; 92,735 canonical 1S+1R groups. These are **candidate pool counts**, not experimental sample sizes. The P2 active 200 included train/dev/test = 156/23/21. ConfB froze a new seed, excluded P2's complete 280-row active-plus-reserve pool by case and normalized claim, and used a blinded evidence-validity review with same-order reserve replacements. All six models received all 200 final pairs. ConfA was separately sampled from a 13,283-item FEVER/SciFact candidate pool and reviewed before model runs.

The only held-out replication of the main phenomenon is ConfB. The six models are Mistral-Small-24B, Llama-3.1-8B, Gemma-3-12B, Qwen3-8B, Qwen3.5-9B, and Qwen3-32B. The registered readout averages model×claim cells; claim-level correlation and slope first average the six models. ConfB integrity checker reports 8,400/8,400 rows. §14 reports 15,600/15,600, unparsed 0. Existing G26A files are an unrelated/incomplete prior line: its local phase-A report says only 3 of 3,640 items pass all three selector gates, hard stop at 200; it contributes no support to this question.

## 3. What survives, what failed, what needs qualification

1. **Survives:** suppression and restoration are empirically distinct. ConfB separation 62.95→8.33, while item-level center error is 29.96, much larger than the reported 1.84-point same-prompt rerun scale. Six of six models show separation reduction, positive center/base correlation, and slope below one.
2. **Survives descriptively:** actual relevant evidence adds compression beyond the generic retraction setting. ConfB `mean|I−50|−mean|M_CF−50|=10.68 [9.32,12.04]`, six of six models. **Does not survive:** the predicted monotonic Withheld→Irrelevant ordering; `dW−dI=−0.53 [−1.60,.53]`, three of six models in expected direction. Mean landing points W=43.59, I=43.96, M=43.25 are close, but mean proximity does not imply item-wise equivalence.
3. **Failed:** prospective exclusion leakage as the headline (ConfA signed effect near zero); negative/contradictory evidence being intrinsically harder to retract (same-claim and leverage analysis undercut it); MNR/event-as-meta-evidence as the dominant explanation (§14 CRE differences −.32 [−1.62,.99] and −.07 [−.82,.68], while MNR separation rises from 10.81 to 25.38).
4. **Important metric caution:** the existing P3 statement “PriorOnly does not recalibrate” is too strong: its signed mean is −.47, but mean absolute item-level movement is 15.67. P4 IrrelVisible mean 14.94 versus Base 50.51 is a very large content/frame interaction. Neither can be flattened into a single simple “frame effect.”
5. **Prompt format limit:** the main G24A/P2/ConfB conditions are single rendered prompts `CLAIM → EVIDENCE → RULING → judgment`. Admit and retract judgments are obtained in separate runs, without a model-generated intermediate judgment in the retraction run. Thus `R_E(U_E(S)) ≠ S` is an illuminating behavioral analogy, not yet a demonstrated composition of two model-state operators or a genuinely staged dialogue result.
6. **Data limit, now independently re-audited:** VitaminC revision pairs are naturally sourced from Wikipedia revision data, yet some individual claims are awkward, threshold-heavy, ambiguous, or include corrupt encoding. A local OpenCode MiMo v2.6 Flash label-blind reassessment of the **final** ConfB 200 marked 190 pair-valid, 189 matching the frozen S/R roles, 147 natural, and 142 valid + label-consistent + natural. It found ten potentially invalid pairs. This is LLM-assisted review, not human gold; notes and exact ID flags are in `results/audits/g24a_confb_reaudit/`. The post hoc stricter 142-pair sensitivity leaves admit separation 67.83, CF separation 9.36, and center CRE 30.09, close to full-sample 62.95, 8.33, 29.96. Do not retroactively replace the 200-pair held-out sample. The right wording is “natural-source revisions with audited semantic validity,” not “fully natural fluent evidence.”

## 4. New full-data reanalysis (explicitly exploratory)

`scripts/analyze_g24a_confb_restoration_controls.py` reads the committed ConfB per-cell CSV, applies no filters, and bootstraps over all 200 claims (5,000 draws). Full output: `results/audits/g24a_confb_restoration_controls_v1.md`.

| Quantity | 0–100 points; mean [95% CI] |
|---|---:|
| Registered center CRE | 29.96 [28.14,31.79] |
| Mean absolute error across CF+ and CF− arms | 30.88 [29.10,32.64] |
| Error of WithheldCF vs Y0 | 21.03 [19.61,22.45] |
| Error of IrrelevantCF vs Y0 | 25.82 [24.04,27.72] |
| Error of constant-50 reference vs Y0 | 35.99 [34.58,37.42] |
| Actual CF center error minus IrrelevantCF error | +4.14 [2.37,5.92] |
| Actual CF center error minus WithheldCF error | +8.93 [7.18,10.67] |

Only 153/1,200 model×claim cells put **both** CF arms within 5 points of Y0 (208/1,200 within 10). This sharpens the current puzzle: decision-relevant evidence appears to make restoration worse than a no-content retraction frame, even though it suppresses direction. The W/I/CF prompts differ, so these contrasts characterize behavior and do not isolate a causal mechanism. The constant-50 comparison is a sanity baseline, not an alternative algorithm.

## 5. Paper-taste audit and closest precedents

The strongest papers move from an anomaly to a **testable distinction or explanatory law**. We currently have the anomaly and distinction, but lack a demonstrated law across histories/tasks and lack a mechanism that predicts new observations.

| Paper | Contribution step worth learning; relation to us |
|---|---|
| [Ji et al., ACL 2025 Best Paper](https://aclanthology.org/2025.acl-long.1141/) | Defines elasticity, derives a compression account, and predicts scale/data effects. Our “compression” is currently a descriptive slope, with no comparable predictive explanation. |
| [Sivaprasad et al., ACL 2025 Best Paper](https://aclanthology.org/2025.acl-long.1454/) | Separates descriptive and prescriptive components of response sampling, then varies each in a fictional-concept setting and checks real domains. We need similarly independent manipulation of history and final valid information. |
| [Hahn & Rofin, ACL 2024 Best Paper](https://aclanthology.org/2024.acl-long.800/) | Uses sensitivity-constrained loss geometry to unify multiple transformer biases. A bare “non-invertible” metaphor has no such unifying predictions. |
| [Shen et al., EMNLP 2025 Outstanding](https://aclanthology.org/2025.emnlp-main.154/) | Turns stated-value versus action discrepancy into a concrete paired evaluation framework, 14.8k actions across cultures/topics. Our suppression versus restoration distinction can become an evaluation contribution if it works beyond one score format and mirrors a real intended use. |
| [Tutek et al., EMNLP 2025 Outstanding](https://aclanthology.org/2025.emnlp-main.504/) | Defines faithfulness by intervention and verifies intervention efficacy/specificity before reading answer effects. Our criterion is also counterfactual, but currently behavioral and prompt-level; mechanism claims would require controlled causal interventions. |
| [Xie et al., ACL 2025](https://aclanthology.org/2025.acl-long.868/) | Near-perfect editing efficacy masks original answers; early residual and later attention effects are causally tested. A late-layer persistence finding alone would repeat this and Takashiro; our distinctive target must be restoration of an in-context no-evidence judgment. |
| [Yang et al., ACL 2025](https://aclanthology.org/2025.acl-long.745/) | Evaluates model editing under natural QA and autoregressive decoding; exposes teacher-forcing inflation. Shows how a metric critique becomes compelling by tying failure to intended use, not merely raising the bar. |
| [Takashiro et al., Findings ACL 2025](https://aclanthology.org/2025.findings-acl.1276/) | Fine-tuned in-context knowledge unlearning suppresses target answers while knowledge persists until late layers. Different object (parametric knowledge and “forgot” output), but a direct warning against presenting late suppression as our new mechanism. |
| [Wilie et al., EMNLP 2024](https://aclanthology.org/2024.emnlp-main.586/) | Belief-R adds premises that force maintenance or revision of an inference. Its “retraction” is of a *conclusion through new premises*, not explicit revocation of a previously shown evidence item or return to the same-item no-evidence output. |
| [Obiso et al., CoNLL 2025](https://aclanthology.org/2025.conll-1.21/) | Epistemic friction formalizes resistance to integrating new propositions in dialogue. We should not use “friction” or “hysteresis” as if new without showing an exclusion-specific behavioral law. |
| [Wang et al., ACL 2026 CAP](https://aclanthology.org/2026.acl-long.1882/) | Prompt optimization for selective unlearning with restoration on prompt revocation. It strengthens the case that a stronger ignore prompt or simple SFT is not a novel method; its “restoration” concerns revoking the unlearning prompt, unlike our no-evidence counterfactual. |
| [Bertsch et al., NAACL 2025](https://aclanthology.org/2025.naacl-long.605/) | Systematically manipulates demonstration number, label space, and context structure under one mother question. Its lesson is coherent factorization and new predictions, not more separate RQs. |

Additional nearby work to track: [In-Context Unlearning (2023)](https://arxiv.org/abs/2310.07579), [Unlearning Isn't Deletion (2025)](https://arxiv.org/abs/2505.16831), and human retraction/continued-influence work including [Retractions: Updating from Complex Information](https://doi.org/10.1093/restud/rdaf032). Their objects differ, but they prevent broad “first evidence retraction failure” language.

**Novelty escalation found in the second search:** [ReviseQA (ICML 2025 Workshop)](https://openreview.net/pdf?id=Z4KBiAYXlI) includes adding/removing facts and rules across dialogue turns; [Breaking Contextual Inertia (Findings ACL 2026)](https://aclanthology.org/2026.findings-acl.313/) explicitly contrasts multi-turn correction with a single-turn full-information anchor and attributes errors to prior reasoning traces; [Revoked but Still Authoritative (arXiv, September 2026)](https://arxiv.org/abs/2609.08258) tests revoked records in agent-memory retrieval systems; [Unraveling Misinformation Propagation (Findings EMNLP 2025)](https://aclanthology.org/2025.findings-emnlp.627/) studies explicit correction of wrong user inputs during math reasoning. Therefore **“same final information, different history” alone is not a safe novelty claim**. Our potential distinction must be the paired *suppression versus restoration* behavior after explicit retraction of natural, claim-relevant evidence, plus a discriminating result beyond generic multi-turn inertia. No priority claim is frozen.

Additional direct challenge found while G28A was running: [Competing Biases underlie Overconfidence and Underconfidence in LLMs (Nature Machine Intelligence, 2026)](https://doi.org/10.1038/s42256-026-01217-9) reports overweighting of *opposing* advice and a countervailing visible-prior-answer bias. Thus a G28A correction or overcorrection after the second, contradictory evidence cannot be called a new general belief-revision mechanism without a contrast that separates evidence revocation from ordinary contradiction/answer visibility. G28A should be used as a falsification/characterization test of the current abstraction, not a novelty victory.

## 6. Priority-ranked research paths

### Priority 1: Equal-final-information path dependence

- **Question:** If two histories end with the same admissible information `{C,E2}`, does a previously displayed and revoked `E1` still change the judgment about C or use of E2?
- **Why nontrivial:** It predicts an item-specific consequence of revocation that cannot be reduced to the center CRE on a single rating. It gives “inverse update” a direct operational meaning. Strongest prior: ReviseQA for fact/rule removal, Breaking Contextual Inertia for single-turn anchors and past-response inertia, and human continued-influence effects. The claim can only go beyond these if **revoked evidence polarity and restoration** reveal a structure not explained by generic prior-response inertia.
- **First discriminating experiment:** Use semantically audited same-claim support/refute revision pairs. Compare `C→E2→judge` with `C→E1→explicitly revoke E1→E2→judge`; include an irrelevant-revoked `E1` history matched in format, and both polarities of E1/E2. Prefer a genuinely staged two-turn version in which the model first produces a judgment after E1, then receives retraction and E2; separately test a single-rendered-prompt version to connect to ConfB. Freeze pairs and all contrasts before running. Measure final score, choice threshold, E2 leverage, and whether past E1 predicts the signed difference after controlling for the irrelevant history.
- **Interpretation changers:** No difference beyond irrelevant-history and repeated-prompt noise would limit the phenomenon to calibration under a terminal retraction instruction. Similar shifts for relevant and irrelevant revoked E1 would support a generic frame/history effect rather than evidence-specific path dependence. A shift predicted by E1 polarity, with final E2 held fixed, supports substantive history dependence. If observed only in single-rendered prompts but not staged dialogue, reconsider the operator/state framing.
- **Potential paper:** behavioral science + evaluation. A method is unnecessary at this stage.

### Priority 2: Does the gap change decisions?

- **Question:** Does restoration failure survive a natural decision output, or is much of the ~30-point effect an artifact of the 0–9 rating and rationale-to-digit procedure?
- **First experiment:** On the same audited material and equal-final-information histories, elicit a predeclared binary decision or evidence choice in a matched task; compare paired decision flips and proper use of E2. Keep rating as a secondary bridge. Include a no-E1 final-evidence baseline. Do not choose cases by model score.
- **Interpretation changers:** If rating gaps persist but decisions and evidence use do not move, limit the claim to calibration/evaluation. If decisions diverge on identical final valid information, practical relevance rises sharply.
- **Strong prior and paper type:** Belief-R and The Mirage of Model Editing; behavior/evaluation paper.

### Priority 3: Mechanism only after Priority 1 distinguishes accounts

- **Question:** Is the path effect due to late output override, early recomputation into a compressed state, or generic uncertainty triggered by revoked content?
- **First experiment:** Select a small predeclared set from the behavior study, then causal patching/interchange between matched no-history and revoked-history prompts at token/layer positions, measuring both restoration and E2 leverage. A layerwise logit lens alone is a diagnostic, not an explanation.
- **Interpretation changers:** If patching only the readout recovers Y0, late override gains support; if early states must be exchanged, state recomputation/path dependence gains support. If neither transports behavior reliably, the proposed localization is wrong.
- **Strong prior and paper type:** Xie et al. and Takashiro et al.; mechanism paper only if it explains restoration-specific behavior and predicts a new condition.

### Deprioritized: immediate prompt/SFT method

§14 did not repair CRE. Training directly to mimic clean-C output presupposes the target and risks benchmark imitation; CAP and in-context unlearning already occupy prompt methods. Reconsider only after a general intervention point is identified and checked for normal evidence-use preservation.

## 7. What was completed after this audit

1. The independent blind LLM-assisted review of final ConfB 200 found 190 pair-valid, 189 frozen-role-consistent, and 142 simultaneously valid, label-consistent, and natural. The full-sample CRE and suppression pattern remain in the post hoc strict-stratum sensitivity. Source data and selection were not changed. See `results/audits/g24a_confb_reaudit/`.
2. [G28A](../discovery/g28a_path_v1_registration.md) staged the same claim and final E2 after a relevant or irrelevant revoked E1 and an actual first assistant judgment. Three of four planned models could load in the driver-compatible environment; all three completed 200 claims × 11 rows with zero parse/cap issues. Qwen3.5-9B's infrastructure failure and unplanned Llama substitute are disclosed. The registered contrast is **−10.92 [−12.82,−9.06]**, opposite the simple stale-evidence persistence prediction; refuting E2 drives most of the result.
3. [G28B](../discovery/g28b_read_control_registration.md), explicitly registered **after** G28A preliminary results, added the matched irrelevant-read history. The three-model full-sample matched content contrast is **−4.66 [−6.22,−3.05]**; strict material sensitivity is −4.48 [−6.27,−2.68]. This weakens a pure prior-answer-anchor explanation but does not isolate revocation from generic opposing-evidence overweighting. Read the [integrated assessment](../g28a/g28a_g28b_integrated_assessment.md) and [figure](../../figures/g28a_path_profiles_v1.png).
4. The earlier priority has therefore advanced from a proposed experiment to a completed exploratory boundary test. The strongest next discriminator is a **fresh** natural-source set with better fluency/validity, a direct decision outcome, and a matched contrast between explicit revocation and exposure to already inadmissible contradictory content. A mechanism or method is premature before this semantic boundary is resolved. A separate post hoc blind OpenCode audit of 200 irrelevant-control sentences found 199 irrelevant, one potentially relevant (`g24cfb_240`), 162 natural, 30 awkward, and eight broken; see `results/audits/g28a_irrelevant_control_audit/`.
