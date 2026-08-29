# External review artifacts

## BTF-3 temporal pilot

- `btf3_temporal_pilot_v0.1.jsonl` — immutable four-cell transformation artifact generated before human review. **Do not modify or run.** It contains the v0.1 cutoff-wording bug.
- `btf3_temporal_pilot_v0.1.md` — completed item-by-item human review decisions/checklists, replacing the unchecked working copy.
- Original full 56 KB v0.1 source-text packet — preserved in Git history at commit `413b1ae461d8f636273a12978412e0aecd24c3c1`, path `data/external/review/btf3_temporal_pilot_v0.1.md`, blob `d795df186bc5e7fb825402ea10fb596721df2f16`.
- `btf3_temporal_pilot_v0.1_reviewed.md` — duplicate completed decision sheet retained for an explicit reviewed filename.
- `BTF3_REVIEW_VERDICT_v0.1.md` — concise audit ledger and transformation-level verdict.
- `btf3_temporal_pilot_v0.1_source_packet.md` — pointer to the immutable Git-history copy of the original source-text packet.

Human review found 7 accepted source units and 1 rejected source unit. The artifact as a whole is blocked because the v0.1 ex-ante wording can grant an extra UTC calendar day by misreading `date_cutoff_end`.

- `btf3_temporal_pilot_v0.2.jsonl` and `.md` — immutable first regeneration round. The corrected cutoff wording passed automatic checks, but its Argentine Senate replacement packet failed human factual-integrity review. **Do not modify or run.**
- `BTF3_REVIEW_VERDICT_v0.2.md` — rejection ledger for that replacement.
- `btf3_temporal_pilot_v0.2r2.jsonl` and `.md` — second deterministic replacement round using the same v0.2 transformation and excluding both rejected IDs.
- `BTF3_REVIEW_REQUEST_v0.2r2.md` — minimal handoff: review the one new BRICS source unit and the regenerated four-cell integrity; the seven retained units do not need their source facts re-audited.

The v0.2r2 review request is now complete: the BRICS replacement is ACCEPT and transformation integrity is PASS. The manifest records `HUMAN_REVIEW_PASSED_PILOT_READY`. This closes the BTF-3-specific gate, but no model run is authorized until the multi-family requirements and preregistration-wide freeze are completed.
