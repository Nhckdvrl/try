# Reproduction map

Use the frozen source files and analysis reports, rather than a root-level paper draft, to reproduce a claim. The incoming formal HEAD was `ebe1dd42507e89f0fbea60b1ef1df1230f3baec9`.

## ConfB held-out result

- Material: `data/items/g24a_confb_selected_v1.jsonl` plus rendered `data/items/g24a_confb_v1.jsonl` and ID lists. The source census, selection, and blinded review are documented under `data/items/` and `data/external/review/`.
- Frozen run: `scripts/run_g24a_confb.sh`; raw per-model output in `results/raw/*_g24a_confb_*.jsonl`.
- Frozen analysis: `results/g24a/g24a_confb_analysis_v1.md` and its cells CSV. Later item-level controls: `python3 scripts/analyze_g24a_confb_restoration_controls.py`.
- Independent LLM-assisted material re-audit: `python3 scripts/prepare_g24a_confb_blind_reaudit.py`; four OpenCode output batches in `results/audits/g24a_confb_reaudit/`; `python3 scripts/summarize_g24a_confb_blind_reaudit.py`; `python3 scripts/analyze_g24a_confb_reaudit_sensitivity.py`. This is post hoc and does not change the frozen sample.

## Staged path experiments

- G28A registration: `results/discovery/g28a_path_v1_registration.md`. Full run: `scripts/run_g28a_path.sh <gpu> <tag>` on fvcrc10 with the pinned `verl-clean` environment. Each model generates 600 initial and 1,600 final rows. Validate each raw file with `python3 scripts/verify_g28a_path_raw.py results/raw/<tag>_g28a_path_v1.jsonl`. Analyze with `python3 scripts/analyze_g28a_path.py`.
- G28B is explicitly a post-G28A exploratory follow-up: registration `results/discovery/g28b_read_control_registration.md`; run `scripts/run_g28b_read_control.sh <gpu> <tag>`, then `python3 scripts/analyze_g28b_read_control.py`. It reuses the G28A RR rows and adds 400 IR rows/model.
- Qwen3.5-9B could not load on the CUDA-driver-compatible environment. The failed launch log remains in `logs/g28a_path_qwen35-9b.log`. Llama-3.1-8B is a disclosed unplanned substitute; keep three planned runnable models separate in reports.

Old project reproduction details are preserved in [the archived prior guide](archive/legacy_root_docs_2026_09_27/REPRODUCE.md).

## Fresh status/content path discrimination

- G29 registration: `results/discovery/g29_revocation_status_registration.md`; source shortlist and label-blind per-item audit under `data/items/g29_*`. Recreate the mechanical shortlist with `python3 scripts/prepare_g29_materials.py` only if audit inputs are being reconstructed; preserve the frozen files for exact replication. Audit verdicts live in `data/items/g29_blind_audit_v1/`. `python3 scripts/freeze_g29_after_audit.py` checks all 160 verdicts and freezes the first 80 eligible pairs.
- On fvcrc10 with the pinned `verl-clean` environment, run `bash scripts/run_g29_revocation.sh <gpu> <tag>` for `mistral-small-24b`, `qwen3-8b`, `gemma3-12b`; output is `results/raw/<tag>_g29_revocation_v1.jsonl` (1,280 rows/model). `python3 scripts/analyze_g29_revocation.py` verifies row/prompt integrity and writes `results/g29/g29_revocation_analysis_v1.md`.
- G29B, registered after G29 results: `results/discovery/g29b_excluded_content_registration.md`; `python3 scripts/prepare_g29b_irrelevant.py` creates deterministic donor candidates, local OpenCode verdicts are under `data/items/g29b_blind_irrelevance_v1/`, and `python3 scripts/freeze_g29b_irrelevant.py` checks and freezes 80 irrelevant controls. Run `bash scripts/run_g29b_irrelevant.sh <gpu> <tag>` on the same three model snapshots (320 rows/model). `python3 scripts/analyze_g29b_irrelevant.py` verifies N/I prompt matching and writes the paired analysis. `python3 scripts/plot_g29_status_content.py` creates the two-panel figure. Run `python3 scripts/make_g29_manifest.py` after all analyses/figure for all 56 file hashes, including the 2-pair Qwen smoke. The [integrated assessment](results/g29/g29_g29b_integrated_assessment.md) states the outcome and claim boundary.
