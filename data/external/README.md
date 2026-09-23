# External source data

This directory is the entry point for the source-native Information-Set
Reasoning benchmark. It is separate from `data/items`, which contains CDS-v1's
controlled compiler outputs.

## Reproduce the raw cache

Use the repository's existing local environment:

```bash
/home/xiang/miniconda3/envs/fgvd/bin/python scripts/fetch_external_sources.py
PYTHONPATH=src /home/xiang/miniconda3/envs/fgvd/bin/python src/audit_external_sources.py
```

`raw/` is intentionally ignored by Git. The fetcher pins immutable revisions
and verifies SHA-256 for every file. The 737MB BTF-3 scraped-pages auxiliary
file is not downloaded because the first schema audit does not need it.

## Current human review

The BTF-3 candidate contract is in `BTF3_TRANSFORMATION_CONTRACT.md`. Rebuild
the balanced eight-item review packet with:

```bash
/home/xiang/miniconda3/envs/fgvd/bin/python scripts/build_btf3_review.py
```

Reviewers edit `review/btf3_temporal_pilot_v0.1.md`. The companion JSONL stores
the exact four prompts and is a review artifact, not a frozen benchmark.

## Status meanings

- `READY_TO_AUDIT`: official files are pinned and locally readable. It does not
  mean the source has been transformed into benchmark items.
- `BLOCKED_PENDING_*_CONTRACT`: source fields are understood, but the causal
  intervention is not yet proven to hold task, target, and utility fixed.
- `DO_NOT_IMPORT_YET`: reuse terms or canonical materials remain unresolved.

Publicly viewable material is not treated as permission to redistribute it.

## Required output schema

Every eventual JSONL record is validated by `src/information_set_schema.py` and
must contain:

```text
source_id
independent_unit_id
boundary_type
reference_context
oob_variant
admissible_variant
provenance
transformation_id
```

There is no shared `admit_rule` / `exclude_rule` compiler. Each adapter must
preserve its source's native task language and freeze a source-specific
transformation contract before export.

## G24A natural-evidence sources (added 2026-09-24)

Pinned by `scripts/fetch_external_sources.py` (SHA-256 verified on every run):

| file | official source | sha256 |
| --- | --- | --- |
| `raw/fever/shared_task_dev.jsonl` | `https://fever.ai/download/fever/shared_task_dev.jsonl` | `e89865bf…78df7` |
| `raw/fever/train.jsonl` | `https://fever.ai/download/fever/train.jsonl` | `eba7e8f8…e588b6` |
| `raw/fever/wiki-pages.zip` | `https://fever.ai/download/fever/wiki-pages.zip` | `4b06d95d…9665f2` |
| `raw/scifact/data.tar.gz` | `https://scifact.s3-us-west-2.amazonaws.com/release/latest/data.tar.gz` | `11c62128…6d76be` |

Licensing (from the official dataset cards, not inferred):

- **FEVER v1.0** — data CC-BY-SA-3.0, code GPL-3.0 (`fever/fever` card);
  `raw/fever/wiki-pages/license.html` is the notice shipped inside the archive.
- **SciFact** — CC-BY-NC-2.0 (`allenai/scifact` card): non-commercial research
  use only.

Derived G24A artifacts (resolved evidence text, candidate pool, frozen items)
are produced by audited scripts under `scripts/` + `src/` and reviewed under
`review/`; the raw cache itself stays ignored by Git.
