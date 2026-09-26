# Current research status — 2026-09-27

Formal incoming HEAD: `ebe1dd42507e89f0fbea60b1ef1df1230f3baec9`. This status supersedes the old prospective-exclusion paper framing; original registrations and results remain unchanged.

## What is established

- Fresh held-out ConfB: 200 VitaminC same-claim support/refute pairs, six local models, 8,400 decision rows. Admit polarity separation is 62.95; retraction separation is 8.33 (86.8% smaller). Mean absolute error of the two-arm retracted center versus the same claim's no-evidence judgment is 29.96 [28.15,31.81]; reported same-prompt rerun noise is about 1.84. Center-versus-base correlation .635, slope .320. See [analysis](results/g24a/g24a_confb_analysis_v1.md).
- Frame and visible irrelevant content contribute to the landing point, but relevant evidence adds compression. This is descriptive, not a complete mechanism.
- §14 meta-neutral and random-reason prompts fail to improve absolute restoration. MNR increases residual evidence separation. The proposed retraction-event-as-meta-evidence explanation is not supported as dominant.
- Fresh ConfA refutes the earlier **prospective exclusion systematically leaks** headline: signed ExcludePre−Base = −0.15 [−1.68,1.40]. Do not revive the older discovery claim.
- A later full-data reanalysis shows the two-arm center can cancel arm errors: 29.96 center error versus 30.88 mean arm-wise error. WithheldCF and IrrelevantCF are also imperfect restoration controls. See [reanalysis](results/audits/g24a_confb_restoration_controls_v1.md).
- Independent LLM-assisted blind re-audit of ConfB's final 200 marks 190 valid, 147 natural, and 142 both valid, label-consistent, and natural. This is a challenge to material quality, not a replacement gold or retroactive sample filter. See [audit](results/audits/g24a_confb_reaudit/reaudit_summary.md).
- A separate blind audit of the 200 G28A/G28B irrelevant controls marked 199 irrelevant and one potentially relevant; 162 sentences were natural. Full-sample results remain primary. See [control audit](results/audits/g28a_irrelevant_control_audit/control_audit_summary.md).

## Completed exploratory path experiment

[G28A](results/discovery/g28a_path_v1_registration.md) compares direct judgment on `{C,E2}` with histories containing a relevant or irrelevant `E1`, an actual prior judgment, explicit revocation, then the same admissible `E2`. Three planned models ran on all 200 claims; Qwen3.5-9B could not load under the driver-compatible stack, and Llama-3.1-8B was run as a disclosed unplanned substitute. The three-model registered contrast is **−10.92 [−12.82,−9.06]**: contrary to simple stale-evidence inertia, revoked relevant history moves final ratings toward the new opposing E2, especially for refuting E2. The [G28B matched read-only follow-up](results/discovery/g28b_read_control_registration.md), registered after preliminary G28A results, is also negative: **−4.66 [−6.22,−3.05]**. Read [the integrated assessment](results/g28a/g28a_g28b_integrated_assessment.md) and [figure](figures/g28a_path_profiles_v1.png). Both experiments reuse ConfB claims and are exploratory.

## Boundaries and next decision

The main ConfB prompt is one rendered prompt, not a staged model update. G28A tests a genuine prior assistant response but still operates through textual dialogue, not a persistent hidden state. [ReviseQA](https://openreview.net/pdf?id=Z4KBiAYXlI) and [Breaking Contextual Inertia](https://aclanthology.org/2026.findings-acl.313/) already cover broad multi-turn revision/inertia, and [opposing-advice overweighting](https://doi.org/10.1038/s42256-026-01217-9) is a direct alternative explanation. The [research audit](results/audits/research_audit_2026_09_27.md) details competing abstractions, strongest priors, and decision points. The most valuable next step is a fresh, cleaner natural-source set with a direct decision and a contrast isolating revocation from mere contradictory-evidence exposure.

Historical experiment registry: [EXPERIMENTS.md](EXPERIMENTS.md). Historical paper and planning documents: [archive index](archive/legacy_root_docs_2026_09_27/README.md).
