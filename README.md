# Evidence retraction and counterfactual restoration

Research repository for the question: **after seeing evidence that is later withdrawn, does an LLM return to the judgment it would have made without seeing it?** The held-out ConfB result motivates a more precise current question: when clean-context restoration fails, is the problem continued use of excluded evidence, a hypothetical-self query, or a changed judgment rule? ACL / EMNLP / NAACL Main is the intended venue level; no paper claim or method is frozen. The suppression–restoration gap by itself is not a novelty claim after the nearest-prior audit.

## Start here

1. [Current status](STATUS.md), [research diagnosis](results/audits/research_diagnosis_2026_09_28.md), and [literature audit](results/audits/literature_diagnosis_2026_09_28.md): current evidence, novelty ceiling, and ranked next steps.
2. [G32 construct-identification assessment](results/g32/g32_construct_identification_assessment.md): direct exclusion, hypothetical-self prediction, redacted-frame effects and legal-E leverage on crossed E/X materials. [Registration](results/discovery/g32_construct_identification_registration.md) and [material audit](results/audits/g32_material_audit_v1.md).
3. [Fresh ConfB analysis](results/g24a/g24a_confb_analysis_v1.md): main held-out result on 200 same-claim VitaminC pairs and six models.
4. [ConfA analysis](results/g24a/g24a_confa_analysis_v1.md): fresh failed replication of the older prospective-exclusion headline.
5. [G24A competing accounts](results/discovery/g24a_competing_accounts_v1.md), [P2](results/g24a/g24a_p2_analysis_v1.md), [P3](results/g24a/g24a_p3_analysis_v1.md), [P4](results/g24a/g24a_p4_analysis_v1.md), and [§14 meta-evidence test](results/g24a/g24a_meta_analysis_v1.md).
6. [G28A/G28B integrated assessment](results/g28a/g28a_g28b_integrated_assessment.md): completed staged equal-final-evidence path experiment and matched read-only follow-up, exploratory on the same 200 ConfB claims. [Figure](figures/g28a_path_profiles_v1.png).
7. [G29/G29B integrated assessment](results/g29/g29_g29b_integrated_assessment.md): fresh audited 80-pair comparison of revoked versus always-inadmissible old evidence, then a matched irrelevant-content control. G29B is a post-G29 exploratory follow-up.

## Evidence and provenance

`preregistrations/`, `data/items/`, and `results/raw/` preserve the experiment lineage; do not treat an earlier failure as confirmation. `results/audits/` contains later checks and reanalyses, explicitly labeled post hoc. The original project began with prospective exclusion; its historical registry remains in [EXPERIMENTS.md](EXPERIMENTS.md) and [RESEARCH_HISTORY.md](RESEARCH_HISTORY.md). Superseded root-level paper drafts and RQ searches are in [the archive](archive/legacy_root_docs_2026_09_27/README.md). Git history preserves their original locations.

## Current claim ceiling

ConfB supports a **behavioral suppression–restoration gap** in a single rendered prompt: admit support/refute separation 62.95 drops to 8.33 under retraction, while mean absolute error of the retracted center against each item's no-evidence score remains 29.96. [Self-Blinding](https://arxiv.org/abs/2601.14553) reports a close prior version of this contrast, so the gap alone cannot be the paper's new idea. G32 shows a model-specific hypothetical-query effect with legal-E controls, while also showing that direct X leakage is not universally absent. It does not yet explain the retrospective ConfB gap. New work must report data validity, complete cell counts, paired item-level metrics, and prior-work overlap.

The exploratory G28 path study found that a revoked *relevant* history can **amplify** graded use of a later contradictory evidence item relative to revoked irrelevant history. Fresh G29 finds little coherent directional difference between *revoked* and *never-admissible* exposure to that same E1. Post-G29 G29B finds a graded content effect even when E1 was excluded from first display: N−I signed rating −5.68 [−8.37,−3.15] on three models, with direct choices differing itemwise but no consistent signed direction. This supports a content-exposure interpretation for graded judgments, while leaving the robust ConfB suppression–restoration gap as the paper's center.
