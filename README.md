# Evidence retraction and counterfactual restoration

Research repository for the question: **after seeing evidence that is later withdrawn, does an LLM return to the judgment it would have made without seeing it?** The current empirical focus is the distinction between suppressing an evidence-specific effect and restoring the same item's no-evidence judgment. ACL / EMNLP / NAACL Main is the intended venue level; no paper claim or method is frozen.

## Start here

1. [Current status](STATUS.md) and [research audit](results/audits/research_audit_2026_09_27.md): current evidence, failures, caveats, prior work, and ranked next steps.
2. [Fresh ConfB analysis](results/g24a/g24a_confb_analysis_v1.md): main held-out result on 200 same-claim VitaminC pairs and six models.
3. [ConfA analysis](results/g24a/g24a_confa_analysis_v1.md): fresh failed replication of the older prospective-exclusion headline.
4. [G24A competing accounts](results/discovery/g24a_competing_accounts_v1.md), [P2](results/g24a/g24a_p2_analysis_v1.md), [P3](results/g24a/g24a_p3_analysis_v1.md), [P4](results/g24a/g24a_p4_analysis_v1.md), and [§14 meta-evidence test](results/g24a/g24a_meta_analysis_v1.md).
5. [G28A/G28B integrated assessment](results/g28a/g28a_g28b_integrated_assessment.md): completed staged equal-final-evidence path experiment and matched read-only follow-up, exploratory on the same 200 ConfB claims. [Figure](figures/g28a_path_profiles_v1.png).

## Evidence and provenance

`preregistrations/`, `data/items/`, and `results/raw/` preserve the experiment lineage; do not treat an earlier failure as confirmation. `results/audits/` contains later checks and reanalyses, explicitly labeled post hoc. The original project began with prospective exclusion; its historical registry remains in [EXPERIMENTS.md](EXPERIMENTS.md) and [RESEARCH_HISTORY.md](RESEARCH_HISTORY.md). Superseded root-level paper drafts and RQ searches are in [the archive](archive/legacy_root_docs_2026_09_27/README.md). Git history preserves their original locations.

## Current claim ceiling

ConfB supports a **behavioral suppression–restoration gap** in a single rendered prompt: admit support/refute separation 62.95 drops to 8.33 under retraction, while mean absolute error of the retracted center against each item's no-evidence score remains 29.96. This does not yet prove a hidden state operator is non-invertible, a general multi-turn history law, or a method failure across tasks. New work must report data validity, complete cell counts, paired item-level metrics, and prior-work overlap.

The completed exploratory staged path study found that a revoked *relevant* history can **amplify** use of a later contradictory evidence item relative to a revoked irrelevant history. This direction is opposite the simple stale-evidence-persistence prediction and is not yet separable from ordinary contradictory-advice sensitivity. See the [integrated assessment](results/g28a/g28a_g28b_integrated_assessment.md) for numbers and limits.
