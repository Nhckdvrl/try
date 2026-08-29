# External review artifacts

## BTF-3 temporal pilot

- `btf3_temporal_pilot_v0.1.jsonl` — immutable four-cell transformation artifact generated before human review. **Do not modify or run.** It contains the v0.1 cutoff-wording bug.
- `btf3_temporal_pilot_v0.1.md` — original full source-text human-review packet generated with v0.1.
- `btf3_temporal_pilot_v0.1_reviewed.md` — completed item-by-item human decisions and checklists.
- `BTF3_REVIEW_VERDICT_v0.1.md` — concise audit ledger and transformation-level verdict.

Human review found 7 accepted source units and 1 rejected source unit. The artifact as a whole is blocked because the v0.1 ex-ante wording can grant an extra UTC calendar day by misreading `date_cutoff_end`.

Next step is to run `scripts/build_btf3_review.py` against the pinned local BTF-3 parquet. It now generates `v0.2`, excludes the rejected Cameron Young question by default, restores a deterministic 4 NO / 4 YES sample, and uses the corrected source-window wording. **The newly selected replacement and all v0.2 prompts still require human review before model execution.**
