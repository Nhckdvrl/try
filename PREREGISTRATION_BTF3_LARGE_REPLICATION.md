# Preregistration — BTF-3 Large Replication v1

**Created:** 2026-08-31
**Status:** design frozen before any queue generation, human review, or model
output. The immutable Git tag `g1-btf3-large-replication-design-v1` identifies
the exact prereg, sampling code, analyzers, and tests below. A second tag,
`g1-btf3-large-replication-freeze-v1`, identifies the reviewed and audited data
artifact and must exist before the first target-model generation of this round.

## Why this round exists

The BTF-3 temporal effect currently rests on one preregistered confirmatory
sample: **64** fresh `question_id`s (`btf3_temporal_confirmatory_v1.jsonl`, 32
YES / 32 NO), on which 3/3 models qualified and 2/3 (Qwen, Gemma) showed
`OutOfSetIntrusion` clearing the 5-point SESOI. Everything else run since is
either exploratory (the 8-unit discovery pilot), a failed second source (FOMC
pilot, gate fail), or a **paired causal manipulation of those same 64 units**
(M1, positional control, M2-v2). Factorization adds causal depth, not
independent natural units. So the honest answer to "how many independent
natural examples support the headline phenomenon?" is today **64**.

That is statistically sufficient for the effect and thin for a main-conference
claim, and it leaves one fair criticism intact: the headline phenomenon and
every mechanism experiment ultimately trace to the same 64 questions. This
round removes that criticism by adding a third, independent evidence layer:

```text
8-item discovery pilot
  → 64-item preregistered confirmatory
    → 256-item fresh large replication (128 YES / 128 NO)
      → factorization / positional mechanism on the frozen 64
```

Headline evidence then rests on 64 + 256 = 320 confirmatory/replication natural
units, with the strongest single sentence being: *the effect independently
replicated on a further 256 unseen questions*.

## What is collected

**N = 256 = 128 realized-YES + 128 realized-NO**, all entirely new
`question_id`s. This round's primary analysis uses **only** these 256 units.
The confirmatory 64 do not enter this round's primary inference, and the 8
discovery-pilot units are never pooled into anything.

Nothing about the task changes. The transformation, prompts, four-cell design,
readout, parsing, decoding, models, and runtime are byte-identical to the
confirmatory round — a 64 → 256 sample expansion, not a new experiment.

## Strict freshness

Stricter than the confirmatory round, which only had to exclude units a model
had actually seen. Permanently excluded here (union = **138** IDs, all derived
mechanically from committed artifacts and their SHA-256, never hand-typed
except the two historical rejects):

1. the 8 discovery-pilot IDs (`btf3_temporal_pilot_v0.2r2.jsonl`);
2. the 64 frozen confirmatory IDs (`btf3_temporal_confirmatory_v1.jsonl`);
3. the **entire** 128-ID prior confirmatory candidate queue
   (`btf3_confirmatory_v1_candidates.json`) — including the tail that was never
   reviewed because quota was reached first;
4. every prior REJECT/UNSURE decision (13, from
   `btf3_confirmatory_v1_reviewed.md`);
5. the two historical pilot rejects `b6fc94e7-…` and `34d3588a-…`.

Categories 2 and 4 are subsets of category 3; discarding the whole prior
candidate universe is deliberately stricter than necessary and is affordable
because the pool is large. It licenses a hard claim: **none of the 256
large-replication questions appeared in the pilot, in the prior confirmatory
sample, or even in the prior confirmatory candidate queue.**

## Census before sampling (hard gate)

`scripts/census_btf3_large_replication.py` runs first and mechanically counts
the pool: raw rows, automatic-eligibility failures, YES/NO totals, the
exclusion funnel step by step, exact-normalized-question duplicates, and the
final eligible YES/NO counts. Output:
`results/btf3_large_replication_pool_census.json`.

**Hard gate:** if fewer than 128 eligible candidates remain in *either*
realized-outcome bucket, the round stops. No eligibility gate may be relaxed,
reworded, or waived to reach the quota.

Census result at design freeze (source SHA-256
`b28f8fe5634f81afa8e4b37d815f875b6e33c24edf590484f1948efea8db051a`): 1,515 raw
binary questions, 0 automatic-eligibility failures, 1,014 NO / 501 YES; after
the 138 exclusions and the duplicate rule, **943 NO and 431 YES eligible**.
Gate passed with wide margin.

## Automatic eligibility (inherited verbatim)

Unchanged from `BTF3_TRANSFORMATION_CONTRACT.md`: binary resolution ∈ {0,1};
`present_date < expected_resolution_date`; the source cutoff-encoding invariant
for the UTC day containing `present_date`; unique `question_id`; non-empty
question / criteria / background / resolution packet; schema validation; exact
resolution packet never rewritten; source question unresolved at cutoff. The
questions are not re-optimized now that the phenomenon is known.

Causal design, unchanged:

| Target information set | packet absent | exact future packet present |
|---|---|---|
| Ex ante | `OOB_WITHOUT` | `OOB_WITH` |
| Retrospective | `ALLOWED_WITHOUT` | `ALLOWED_WITH` |

With realized outcome `r ∈ {0,1}` and `s = 2r − 1`:

```text
I = s * (p_OOB_WITH     − p_OOB_WITHOUT)
R = s * (p_ALLOWED_WITH − p_ALLOWED_WITHOUT)
BoundarySelectivity = R − I
```

**No prompt text changes.** Any prompt edit would end the strict-replication
claim.

## Complete immutable queue (no pool size)

Improving on the confirmatory round's fixed-size pool with a deterministic
append-on-shortfall tail: here the **entire** eligible pool is ordered once.
For every eligible candidate,

```text
h_i = SHA256("20260831:" + question_id)
```

ascending, separately within each realized-outcome bucket
(`scripts/build_btf3_large_replication_queue.py`). Written before any review:

- `data/external/review/btf3_large_replication_v1_yes_queue.json`
- `data/external/review/btf3_large_replication_v1_no_queue.json`
- `data/external/review/btf3_large_replication_v1_queue.json` (manifest)
- `data/external/review/btf3_large_replication_v1_queue.sha256`

The manifest records the source parquet path and SHA-256, seed `20260831`, the
full exclusion universe with per-artifact SHA-256, eligibility counts, each
bucket's complete ordering, every duplicate drop, each queue file's SHA-256,
and its own SHA-256. Because the order is complete from the start, the question
"the pool ran out, may we regenerate?" cannot arise.

## Hard-duplicate rule (applied before review)

Two candidates are hard duplicates when their whitespace-collapsed, casefolded
question text is identical. The rule is mechanical and fixed in advance: the
candidate with the earlier global hash rank is kept, every later one is dropped
from the queue, and each drop is recorded in the manifest. A candidate whose
normalized question text matches a question already used in the pilot or the
confirmatory 64 is likewise dropped as not fresh. At design freeze this removes
3 candidates within-round and 0 against prior rounds.

Semantic near-duplicate removal (e.g. cosine similarity > 0.9) is **not** used:
the threshold is too discretionary to sit upstream of primary selection. Near
duplication may be reported as an appendix sensitivity analysis only.

## Human review gate (unchanged strength)

BTF-3's `resolution_explanation` is machine-generated and only partially
spot-checked, and prior review caught real factual and temporal-logic errors in
exact packets. The gate is therefore not relaxed at 256 units. All four gates
must hold to ACCEPT:

1. **pre-cutoff intact** — question unresolved at `present_date`; background
   carries no post-cutoff leakage;
2. **realized outcome valid** — source YES/NO is correct;
3. **exact packet factually valid** — no factual, sourcing, or temporal-logic
   error in `resolution_explanation`; **packets are never hand-repaired**;
4. **criteria unambiguous** — the outcome satisfies the source criteria under
   exactly one reasonable reading.

Otherwise `REJECT` or `UNSURE`, with exactly one line of reason. Review is
conducted with no target-model output of any kind visible. The reviewer of
record is named in the ledger header; if any part of the packet-factual review
is LLM-assisted, that assistance is disclosed in the ledger and in the paper.

Review is displayed in chunks of 64 (`*_yes_review_001-064.md`, …), but
**chunking is presentation only**: selection order is defined solely by the
immutable queue manifest, and a chunk boundary carries no statistical meaning.
Further chunks are rendered from the same frozen queue if needed.

## First-128-ACCEPT rule

Walk each bucket's queue from position 1. ACCEPT increments the count; REJECT
and UNSURE permanently consume the slot. Stop that bucket at exactly 128
ACCEPTs. Final artifact: 128 + 128 = 256.

Forbidden, without exception: choosing better-looking questions; balancing
domains; excluding a question for being famous or for disclosing its outcome
too directly; any replacement made after seeing model output; deciding how much
more to collect after inspecting the effect in a partial sample; re-reading a
gate to rescue a rejected item.

Expected workload, extrapolating the confirmatory round's accept rates (NO
32/36, YES 32/41): roughly 144 NO and 164 YES reviews, ≈300–320 candidates
total. This, not GPU time, is the round's real cost.

## No domain stratification

Selection balances realized YES/NO **only** — as the 64 were drawn. Introducing
domain quotas now would change the sampling distribution mid-project and hand
back selection freedom. Topic, cutoff year, resolution horizon, packet length,
background length, and source/domain distribution are audited *descriptively
after* selection and never alter membership. If the source later exposes an
explicit cluster ID, cluster sensitivity can be added as a secondary analysis.

## Freeze audit (fail-closed)

`scripts/freeze_btf3_large_replication.py` emits
`data/external/review/btf3_temporal_large_replication_v1.jsonl`;
`scripts/audit_btf3_large_replication.py` then writes
`BTF3_LARGE_REPLICATION_V1_FREEZE_REPORT.md` **only** if every check passes:

- exactly 256 items, exactly 128 YES / 128 NO, 256 unique `question_id`;
- zero overlap with the pilot, the confirmatory 64, the prior candidate queue,
  the historical rejects, and every prior REJECT/UNSURE;
- source parquet SHA-256 matches the pinned revision; queue manifest and both
  queue files unchanged since queue freeze;
- the artifact is independently re-derived as exactly the first-128-ACCEPT
  prefix of each frozen queue;
- schema validation passes; all four prompt cells present and equal to the
  registered transform; the exact packet appears exactly once in each `WITH`
  cell and never in a `WITHOUT` cell;
- outcome sign mapping and `realized_resolution` correct; no NaN or malformed
  field; no duplicate normalized question.

## Token census before any generation

`scripts/token_census_btf3_large_replication.py` counts **every** prompt —
256 units × (4 decision cells + 2 boundary probes) × 3 chat templates = 4,608
prompts — with no sampling, and fails closed if any prompt plus the frozen
8-token output allowance would exceed `max_model_len = 8192`. Truncation is
never permitted. (Confirmatory longest prompt: 4,197 tokens.)

## Model panel and runtime (unchanged)

The same three frozen checkpoints, no additions, no substitutions:

| tag | model | revision |
|---|---|---|
| `qwen35-9b` | `Qwen/Qwen3.5-9B` | `c202236235762e1c871ad0ccb60c8ee5ba337b9a` |
| `gemma3-12b` | `google/gemma-3-12b-it` | `96b6f1eccf38110c56df3a15bffe176da04bfd80` |
| `mistral-small-24b` | `mistralai/Mistral-Small-24B-Instruct-2501` | `9527884be6e5616bdd54de542f9ae13384489724` |

`scripts/run_btf3_large_replication.sh` is the confirmatory launcher with only
the artifact path, output path, and log names changed: same system prompt,
greedy decoding at temperature 0, seed 0, 8 max tokens, `max_model_len` 8192,
same tokenizer modes and GPU settings. Call volume: 256 × 6 = 1,536 requests
per model, 4,608 generations total.

## Qualification thresholds (mechanically scaled)

Inherited from the confirmatory round at exactly the same ratios:

- decision parse rate ≥ **992/1024** (= 248/256 = 31/32);
- boundary-probe accuracy ≥ **448/512** (= 112/128 = 14/16);
- mean responsiveness ≥ 15 probability points;
- mean outcome-aligned `ALLOWED_WITH` score ≥ 70.

All frozen before any model output exists.

## Primary analysis

Each `question_id` is one independent cluster. Equal question weighting; 95%
percentile cluster bootstrap; 10,000 resamples; seed `20260829`; raw
probability-point effects primary; SESOI = 5 points. Per model, report mean `I`
with 95% CI (and `R`, `BoundarySelectivity`).

- a qualified model shows intrusion iff the bootstrap **CI lower bound > 5**;
- **panel replication gate (unchanged):** ≥ 2/3 models qualify **and** ≥ 2/3
  qualified models pass intrusion;
- no pooled p-value across models, no multiplicity adjustment; all three
  model-level estimates and intervals are reported regardless of outcome.

Analyzer: `src/analyze_btf3_large_replication.py`, which refuses to score any
result file whose recorded `artifact_sha256` is not the frozen artifact's.

## The 256 alone decide replication

- **PASS:** if the 256 units on their own satisfy the panel gate
  (`btf3_large_replication_v1 = true`), the effect has independently replicated
  at scale.
- **FAIL:** if they do not, the round is reported as a failed replication —
  *earlier confirmation succeeded, the large replication did not meet the
  preregistered gate*. A pooled 320-unit CI clearing 5 does **not** convert
  this into a success. This is written down now, before any output exists.

## Secondary: 320-unit cross-round analysis

`src/analyze_btf3_cross_round.py`, explicitly secondary and never a gate,
excluding the 8 discovery-pilot units:

- **A. pooled question-level**, N = 64 + 256 = 320, all questions weighted
  equally;
- **B. round-stratified**, reporting confirmatory (N=64) and large replication
  (N=256) separately plus `Δ = I_256 − I_64` with a percentile bootstrap CI
  (rounds resampled independently, seed `20260829`), answering whether the
  effect magnitude is stable across rounds.

## Factorization does not scale to 256

M1, the positional control, and M2-v2 stay on the pre-frozen confirmatory 64.
Prevalence/replication and mechanism experiments answer different questions and
need not share a sample size; re-running the manipulations at 256 would
multiply cost without adding evidence for either claim.

## Order of operations

1. prereg + sampling code + analyzers + tests + census (hard gate, mechanical
   and pre-sampling; its result is recorded above) → **tag
   `g1-btf3-large-replication-design-v1`**;
2. build the immutable queue + review chunks from the tagged code;
3. human review in queue order until 128 ACCEPTs per bucket;
4. freeze → fail-closed audit → freeze report;
5. **tag `g1-btf3-large-replication-freeze-v1`**, verified local + remote, with
   commit SHA and artifact SHA-256 recorded;
6. token census (fail closed);
7. first target-model generation — not before step 5 exists.

## Freeze checklist

- [x] round definition, N, and balance fixed (256 = 128 YES + 128 NO, all fresh)
- [x] strict-freshness exclusion universe derived mechanically from committed artifacts
- [x] census script + hard gate, run before any sampling
- [x] automatic eligibility and prompts inherited unchanged
- [x] complete immutable queue design, seed `20260831`
- [x] hard-duplicate rule fixed before review
- [x] four human gates retained at full strength; chunking is presentation only
- [x] first-128-ACCEPT rule and forbidden-actions list
- [x] fail-closed freeze audit and freeze report
- [x] token census before generation
- [x] model panel and runtime unchanged
- [x] qualification thresholds scaled at the confirmatory ratios
- [x] primary inference, replication gate, and failure language
- [x] secondary 320-unit cross-round analysis defined as non-gating
- [x] design tag before queue generation: `g1-btf3-large-replication-design-v1`
- [ ] human review complete (128 ACCEPT per bucket)
- [ ] data freeze tag before first model output: `g1-btf3-large-replication-freeze-v1`
