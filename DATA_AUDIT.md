# Information-set data audit — 2026-08-29

## Decision

No external source is yet a frozen G1 benchmark. Four official first-wave
sources have been pinned, hashed, read with source-specific adapters, and
classified by what remains unresolved. This is the intended pre-model gate.

## Environment

All audits use the existing local environment:

```text
/home/xiang/miniconda3/envs/fgvd/bin/python (Python 3.12.13)
```

No new experiment environment is required.

## FANToM v1

- Official tarball SHA-256 matches the hash hard-coded by the authors:
  `1d08dfa...e1253a4`.
- 870 rows, 368 `part_id` values, 253 conversation IDs, and 1,540 belief QAs.
- Belief accessibility labels: 993 inaccessible, 547 accessible.
- The row count is not the independent-unit count. `part_id` is the provisional
  cluster, subject to a deeper latent-conversation audit.
- A fact QA and a belief QA cannot be treated as a clean allowed/out-of-set pair
  without proof: they change the target question as well as the information set.

Candidate v0.1 now keeps one first-order inaccessible belief question fixed and
uses the same exact fact packet in a 2 × 2 evaluator-only versus explicitly
briefed-target intervention. Full-text artifacts remain local because the
official README restricts intended use to evaluation and redistribution
coverage still needs resolution. Eight deterministic `part_id`-clustered items
await human causal-alignment review.

Status: transformation review pending; no model run authorized.

## ForecastBench

- Dataset repository pinned to commit
  `d4834ccc58310539400974fc4664923db7b71417` under CC BY-SA 4.0.
- Audited the matched named set `2025-03-02-llm.json`: 997 question rows and
  7,836 resolution rows.
- 496 question rows are combination questions whose `id` is a list. Dataset
  templates also expand over multiple `resolution_dates`.
- There are 1,628 direct scalar-ID resolution matches, but positional joining is
  invalid. A composite key and cutoff policy must be frozen first.

Status: source readable; keyed join/cutoff transformation blocked.

## BTF-3

- Hugging Face revision pinned to
  `4b426627e19cd86202de69a40bc9dadb7f5ccd59`, CC BY-NC 4.0.
- 1,515 binary plus 392 numeric questions = 1,907 independent question IDs.
- No missing resolutions; no cross-track ID overlap.
- The native schema explicitly separates `present_date`, cutoff dates,
  resolution, and resolution explanation, making it the cleanest temporal pilot
  source. The causal injection/removal of post-cutoff information still needs a
  transformation audit.

After two rejected source packets and one corrected cutoff regeneration, the
v0.2r2 eight-item artifact passed human source-validity and transformation
review: 8 accepted units, 4 NO / 4 YES, corrected UTC-day semantics, no model
outputs inspected.

Status: human-review passed and pilot-ready, but not yet a frozen G1 benchmark.

## Aiyer outcome-bias replication

- The article is CC BY 4.0, but the OSF node itself reports no project license.
  Files therefore remain local-only until material-level terms are confirmed.
- The participant CSV has 709 physical rows: two Qualtrics metadata rows plus
  707 response rows before the paper's exclusions, not 709 independent items.
- The QSF supplies the exact physician/patient × success/failure stimuli and is
  the authoritative stimulus source. Its server SHA-256 matches locally.
- All four cells derive from one medical bypass vignette. This family is one
  semantic unit, useful as a natural anchor but incapable of supporting broad
  item-level inference alone.
- The source task directly supports out-of-set outcome sensitivity. A matched
  allowed-responsiveness task is not present and must not be invented casually.

Status: source readable; benchmark export blocked pending allowed-task contract
and material-license confirmation.

## Statistical audit

The previous `paired_cluster_bootstrap_mean` weighted a sampled cluster by its
number of rendered observations. It now:

1. averages observations inside each independent cluster;
2. estimates the unweighted mean of cluster means;
3. bootstraps those cluster means.

Unit tests prove that copying one rendering ten times leaves both the point
estimate and seeded interval unchanged. Frozen G0 item-level inference in
`src/analyze.py` is untouched.

## Gate outcome

The repository is ready for transformation design, not model execution. BTF-3
is the strongest candidate for the first temporal adapter; FANToM needs the most
careful matched-intervention design; Aiyer is a one-unit anchor; ForecastBench
requires a correct composite join before any prompt exists.
