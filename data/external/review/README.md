# External review artifacts

## BTF-3 temporal pilot

- `btf3_temporal_pilot_v0.1.jsonl` — immutable four-cell transformation artifact generated before human review. **Do not modify or run.** It contains the v0.1 cutoff-wording bug.
- `btf3_temporal_pilot_v0.1.md` — completed item-by-item human review decisions/checklists, replacing the unchecked working copy.
- Original full 56 KB v0.1 source-text packet — preserved in Git history at commit `413b1ae461d8f636273a12978412e0aecd24c3c1`, path `data/external/review/btf3_temporal_pilot_v0.1.md`, blob `d795df186bc5e7fb825402ea10fb596721df2f16`.
- `btf3_temporal_pilot_v0.1_reviewed.md` — duplicate completed decision sheet retained for an explicit reviewed filename.
- `BTF3_REVIEW_VERDICT_v0.1.md` — concise audit ledger and transformation-level verdict.
- `btf3_temporal_pilot_v0.1_source_packet.md` — pointer to the immutable Git-history copy of the original source-text packet.

Human review found 7 accepted source units and 1 rejected source unit. The artifact as a whole is blocked because the v0.1 ex-ante wording can grant an extra UTC calendar day by misreading `date_cutoff_end`.

Next step is to run `scripts/build_btf3_review.py` against the pinned local BTF-3 parquet. It now generates `v0.2`, excludes the rejected Cameron Young question by default, restores a deterministic 4 NO / 4 YES sample, and uses the corrected source-window wording. **The newly selected replacement and all v0.2 prompts still require human review before model execution.**
