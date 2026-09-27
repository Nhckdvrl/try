# Final-admissible-set sufficiency: working research abstraction

Date: 2026-09-27. This is a **post-G30 synthesis**, not a retrospective registration or a new confirmation. Historical experiment outcomes and original estimands remain in their frozen reports. Read the [ConfB analysis](../g24a/g24a_confb_analysis_v1.md), [ConfA final-set reanalysis](../g24a/g24a_confa_final_set_reanalysis_v1.md), [G29 integrated assessment](../g29/g29_g29b_integrated_assessment.md), and [G30 factorial diagnostic](../g30/g30_factorial_diagnostic_v1.md).

## The question in one sentence

**After evidence is explicitly declared inadmissible, does the model judge from the final admissible evidence set, or can excluded content and its history still change its judgment?**

Let C denote the claim and stable task context, A the final admissible evidence set, H the displayed history, and Y the model's judgment. The operational target is *history invariance conditional on C and A*:

`P(Y | C, A, H1) ≈ P(Y | C, A, H2)` whenever H1 and H2 differ only in content or status that the task explicitly says is excluded. Deterministic temperature-zero judgments give a paired behavioral approximation. Stochastic models require output-distribution comparisons and a repeat-run baseline. This is a normative evidence-control criterion, not a claim that a transformer has a persistent hidden-state operator.

The simplest case has A empty: compare `(C)` with `(C, E, exclude E)`. A second case adds new valid E2: compare `(C, E2)` or `(C, excluded E1, E2)` with another history ending in exactly the same `{C,E2}`. For paired support/refute E2, compare the **leverage of valid E2** under each history; a single signed shift cannot cover every failure mode.

## Two tests that should not be conflated

1. **Local suppression / compliance.** Does the direct support-versus-refute effect of E shrink after exclusion? Does a signed average appear to return to zero? These are useful operational checks, but they can cancel across polarities, items, or models.
2. **Final-set sufficiency.** Is the same-item judgment close to the no-exposure or matched-final-set judgment? Does a later valid E2 have the same effect across histories? Use paired absolute deviations alongside signed ones. For deterministic scores, `D(H1,H2)=|Y(C,A,H1)-Y(C,A,H2)|`; for later evidence, compare matched E2 response profiles or within-history updates if a pre-E2 judgment is observed.

The distinction matters because an exclusion rule often aims to make a piece of information *irrelevant to the final decision*, not merely prevent an obvious citation or direct directional effect. The comparison must preserve the task and final admissible set. Prompt wording itself can affect responses; that is a plausible behavioral cause of an invariance failure, not proof that the excluded semantic content persisted internally.

## Evidence ledger for this abstraction

| Source | What is established | What it does not establish |
|---|---|---|
| **ConfB, held-out VitaminC, 200 same-claim pairs × 6 models** | Admit polarity separation 62.95 falls to 8.33 under counterfactual deletion (86.8% suppression), yet the retracted center is 29.96 points from the same-item no-evidence judgment. Strict post hoc material sensitivity on 142 audited pairs leaves the gap about 30. | An internal inverse-update operator or a generic multi-turn law. |
| **ConfA, held-out FEVER/SciFact, 500 items × 6 models; post hoc final-set reanalysis** | Original signed ExcludePre−Base is −0.15 [−1.68,+1.40], so the earlier prospective signed-leakage hypothesis failed. Paired **absolute** ExcludePre−Base is 19.50 [18.13,20.88]; 43.7% of item-model cells differ by at least 10 points. ExcludePost absolute deviation is 29.91 [28.39,31.40]. Both domains and all six models show large item-wise deviations. ExcludePre-vs-Base OLS slopes are 0.517–0.722 across models, below their AdmitPre slopes in all six; this is descriptive compression. | A preregistered confirmation of the new metric, or attribution of the deviation specifically to excluded content rather than the exclusion frame. The original prospective-leakage headline remains rejected. |
| **G29/G29B, fresh audited natural pairs** | Revoked R and never-admissible N have no stable directional difference. N versus excluded irrelevant I alters graded final E2 judgments, with model heterogeneity and no common signed binary shift. | A universal revocation-specific trace or directional overcorrection law. |
| **G30, audited formal probability grid** | N−I has no common signed direction; the pooled R−N shift is substantially a Gemma-specific mode: its R output equals the prior or complement in 40/40 cells and is reliability-insensitive in every prior × E2 group. | A second general retraction effect, or a mechanism shared by the three models. |

The empirical center is still ConfB. ConfA now supplies **a separate natural-domain instance-wise evaluation warning**, using previously frozen data, but its new estimand is explicitly post hoc. Its mean 19.50-point ExcludePre deviation has a 5.92-point median and 43.7% of item-model cells at or above 10 points: the effect is heterogeneous, not a large shift on every item. For context, the corresponding mean absolute AdmitPre−Base difference is 17.06 points. The [source-data audit](../../data/external/review/G24A_SOURCE_DATA_AUDIT_v1.md) passed, and the [500-item review material](../../data/items/g24a_confa_review_v1.md) was frozen before these outputs. These facts strengthen provenance; they do not separate exclusion framing from semantic influence. G29/G30 show why the second-level story should concern invariance and valid-evidence integration rather than the sign of a residual bias.

## Novelty boundary

The no-exposure counterfactual itself was used in [Gonçalves et al.'s human retraction experiments](https://academic.oup.com/restud/article/93/1/476/8159675). Suppression versus restoration/deletion is also discussed in [machine unlearning](https://arxiv.org/abs/2602.18505). [Kim et al., NAACL 2025](https://aclanthology.org/2025.naacl-long.531/) test LLM belief changes across evidence informativeness, reliability, and irrelevance. [Tsujimura et al., ACL 2026](https://aclanthology.org/2026.acl-long.1860/) test belief consistency as a logical context extends, including rejection of an option. [ReviseQA](https://openreview.net/pdf?id=Z4KBiAYXlI) tests addition and removal of facts/rules in multi-turn logical reasoning; [Breaking Contextual Inertia](https://aclanthology.org/2026.findings-acl.313/) tests reliance on old reasoning traces after new constraints.

The candidate contribution is the **intersection** of explicit *in-context evidence eligibility*, apparent local suppression success, **paired same-item final-set restoration**, and subsequent integration of still-admissible evidence in natural language tasks. Do not claim first invention of counterfactual restoration, belief consistency, or Bayesian updating benchmarks. Our strongest fresh empirical distinction remains suppression succeeding while same-item restoration fails.

## Next discriminating experiment

Choose a natural task where the final action or graded forecast is meaningful. Before inference, source and audit every item with the local free OpenCode model, keeping source text, licensing, time order, relation labels, and rejected candidates. For each target, construct two or three matched histories that end with identical `C` and admissible `E2`: directly see E2; first see a relevant E1 explicitly excluded from first display then E2; first see a similarly excluded irrelevant item then E2. If naturally available, include an admitted-then-revoked E1 to separate status history from content exposure. Measure the final paired decision/forecast and the response profile to E2 across its support/refute or strength levels. Report model-specific results before pooling and preserve the original item set regardless of outcome.

The decisive result is **same-final-set divergence that survives a natural output task and appears alongside obvious local compliance**. Its sign need not agree across models. A null across fresh audited natural material would narrow the second-level claim; ConfB's suppression–restoration gap would remain intact.
