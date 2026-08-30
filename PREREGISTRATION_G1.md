# G1 preregistration — Information-Set Reasoning

**Created:** 2026-08-29  
**Status:** FROZEN for the two-family exploratory pilot. The immutable Git tag
`g1-pilot-freeze-v1` identifies the exact code, artifacts, and analysis policy
before the first target-model OOB run. `g1-pilot-freeze-v1.1` is an
infrastructure-only amendment that is itself invalidated (see below) after
producing one incidental Qwen BTF-3 output and no usable Mistral/Gemma output;
`g1-pilot-freeze-v1.2` is the corrected executable state and the one all
six model-family runs are generated under.

## Research question

Can an LLM construct the information set that defines a target decision: remain
responsive to licensed evidence while invariant to information outside that
set?

## Confirmatory scope

G1 primary evidence uses independently authored, source-native tasks from at
least two boundary families. CDS-v1 is excluded from primary confirmation and
used only for controlled mechanistic follow-up.

Each source must have a pinned manifest entry, exact file hash, reuse status,
independent-unit rule, source-specific adapter, and reviewed transformation
contract. No item is selected using target-model OOB behavior.

## Primary outcomes

For paired critical-information values:

```text
Responsiveness       = Y(allowed E+) - Y(allowed E-)
OutOfSetIntrusion    = Y(outside E+) - Y(outside E-)
BoundarySelectivity  = Responsiveness - OutOfSetIntrusion
```

Direction alignment is fixed by source semantics before model runs. Raw outcome
units or preregistered probability/logit margins are primary. Normalized ratios
are secondary and omitted below a frozen responsiveness floor.

## Source-specific validity checks

Every family freezes:

- task utility/accuracy criterion;
- boundary or policy knowledge probe;
- information availability/memory probe where meaningful;
- exact prompt and readout;
- invalid parse/refusal policy;
- fields allowed to differ between paired variants.

Strong evidence requires utility and boundary knowledge to pass while
OutOfSetIntrusion remains non-zero. A failure caused by task misunderstanding or
missing memory is not counted as information-set intrusion.

## Inference

The independent semantic source unit is the cluster. Per-unit renderings are
averaged first; the point estimand and bootstrap equally weight cluster means.
Report each family before any pooled estimate. Model checkpoints are repeated
measurement factors, not independent dataset replications.

Historical G0 inference is unchanged.

## Exploratory pilot gate

Run 2–3 open models only after the data freeze. Continue to broad G1 if at least
two materially different natural families satisfy:

1. source-specific utility passes;
2. boundary knowledge passes;
3. relevant information remains available;
4. raw OutOfSetIntrusion is non-zero with a cluster-aware interval excluding the
   preregistered smallest effect of interest or meeting its Bayesian analogue.

If one family passes, narrow to that phenomenon. If none pass, stop the broad
claim. Do not generate more synthetic items to force the gate.

## Frozen pilot artifacts

| family | artifact | independent units | SHA-256 |
|---|---|---:|---|
| temporal | `data/external/review/btf3_temporal_pilot_v0.2r2.jsonl` | 8 `question_id` | `113e3b0dfa553f4bb5f3b4db0d94ed673f2590ec707c5b490413bce9b902dd8c` |
| perspective | `data/external/review/fantom_perspective_pilot_v0.1r4.jsonl` | 8 `part_id` | `dd5a5eb7c87996360aa65a31d3dbcd13f4a40acbe26ed52222549cf345512dd1` |

All source selection, factual review, causal-alignment review, rejection, and
replacement occurred before target-model outputs. No post-output item removal
or replacement is permitted. The final excluded IDs remain in the manifest and
review ledgers.

## Frozen open-model panel

| tag | model | exact Hugging Face revision |
|---|---|---|
| `qwen35-9b` | `Qwen/Qwen3.5-9B` | `c202236235762e1c871ad0ccb60c8ee5ba337b9a` |
| `gemma3-12b` | `google/gemma-3-12b-it` | `96b6f1eccf38110c56df3a15bffe176da04bfd80` |
| `mistral-small-24b` | `mistralai/Mistral-Small-24B-Instruct-2501` | `9527884be6e5616bdd54de542f9ae13384489724` |

The panel was selected before outputs to cover three instruction-tuned model
families and a useful size range while fitting the available local GPUs. No
checkpoint is replaced based on pilot behavior. A load/runtime failure is
reported; it does not authorize substituting a favorable model.

## Frozen execution and parse policy

### Pre-output infrastructure amendment (2026-08-30)

The first frozen launch produced no model outputs. Qwen and Gemma remained at
checkpoint shard 0 while reading snapshots from the `/home` NFS mount, and
Mistral failed during vLLM initialization because the installed
`mistral_common` tokenizer wrapper lacks the `is_fast` attribute expected by
the installed vLLM version. Before any target-model output existed, the launch
was stopped and the following infrastructure-only amendment was frozen:

- exact revision snapshots may be staged byte-for-byte on local NVMe and passed
  through model-path environment variables;
- Mistral uses vLLM `tokenizer_mode=hf`, backed by the same snapshot
  `tokenizer.json` that the runner uses to construct the frozen prompt token
  IDs;
- Qwen and Gemma retain vLLM `tokenizer_mode=auto`.

This amendment does not change artifacts, item inclusion, prompts, prompt token
IDs, models or revisions, decoding, parsing, thresholds, inference, or the
stop/go rule. The original freeze tag is retained as an audit record of the
zero-output failed launch; a new freeze tag identifies the executable amended
state.

### v1.1 run invalidated; second infrastructure-only amendment (2026-08-30)

Tag `g1-pilot-freeze-v1.1` launched with the amendment above. Qwen completed
BTF-3 (48 rows, 0 decision/probe parse failures) before the launcher process
was killed with the terminal session that started it, leaving Gemma with no
output and Mistral still failing. `vllm tokenizer_mode=hf` for Mistral, as
frozen in v1.1, does **not** work: the installed vLLM (`0.23.0`) wraps the
Transformers (`5.12.1`) `MistralCommonBackend` in a caching subclass that goes
through `PreTrainedTokenizerBase.__getattr__` for any attribute the wrapper
does not already have, and `MistralCommonBackend` implements neither
`is_fast` nor the `get_added_vocab` that vLLM's incremental detokenizer calls
on every decode step. A one-line `is_fast` shim clears initialization but
still crashes at first-token detokenization on `get_added_vocab`. Because a
real Qwen BTF-3 output already existed once this failure was confirmed, the
entire v1.1 run is invalidated, not repaired in place: that output is
isolated under `results/raw/_archive_v1.1_incomplete/` and excluded from all
analysis, and Gemma/Mistral are not back-filled against it.

The actual fix does not touch `tokenizer_mode=hf` at all: it runs Mistral
under vLLM's native `tokenizer_mode=mistral`, which uses `mistral_common`
directly against the snapshot's `tekken.json` and never instantiates the
broken `MistralCommonBackend` wrapper. This was verified by an isolated
initialization + generation smoke test on a neutral prompt
(`"The capital of France is"` → `" Paris. It is known for its iconic"`)
before either benchmark artifact was touched, and again by tokenizing a
neutral chat-template prompt through the same `AutoTokenizer` path
`src/run_information_set.py` uses for the frozen prompt token IDs and passing
those `prompt_token_ids` through the `tokenizer_mode=mistral` engine. Prompt
construction is unaffected: prompt token IDs are still produced by
`AutoTokenizer.from_pretrained` reading the snapshot's `tokenizer.json`
exactly as before; only vLLM's internal detokenizer backend for Mistral
changes. Qwen and Gemma remain `tokenizer_mode=auto`, unchanged. All three
models load from the local NVMe snapshots under `/var/tmp/xiang-isr-models/`
(unchanged from the first amendment).

This second amendment does not change artifacts, item inclusion, prompts,
prompt token IDs, models or revisions, decoding, parsing, thresholds,
inference, or the stop/go rule. `g1-pilot-freeze-v1.1` is retained as an
audit record of the invalidated run (one incidental Qwen output, no Gemma
output, Mistral still broken); `g1-pilot-freeze-v1.2` identifies the
corrected executable state that all six model-family files are generated
under, with no reuse of any v1.1 output.

- runner: `src/run_information_set.py`;
- each model loads from the exact local snapshot matching the revision above;
- chat template with thinking disabled where supported;
- system prompt: `Follow the target information set defined in the task exactly. Return only the requested answer format and no explanation.`;
- direct greedy decoding, temperature `0`, seed `0`, maximum 8 generated tokens;
- maximum model context: 8192 tokens; the runner fails before generation if any prompt plus output allowance exceeds it;
- decisions use strict full-string parsing of a number in `[0,100]`, optionally followed by `%`; explanatory text is invalid;
- boundary probes use strict full-string `YES` or `NO` parsing; invalid probes count as incorrect;
- a decision unit contributes to causal metrics only when all four cells parse;
- all invalid outputs, raw strings, token counts, and complete-unit counts are reported;
- minimum decision parse rate for model-family qualification: `31/32`;
- no LLM judge, repair prompt, retry, or result-conditioned rerun is allowed.

Each item additionally receives two boundary probes using the exact `WITH`
prompt with the decision task replaced: OOB target expects `NO`; allowed target
expects `YES`. This directly checks whether the model distinguishes packet
eligibility under the two target information sets.

## Frozen family validity thresholds

A model-family result is **qualified** only when all applicable conditions hold:

- decision parse rate at least `31/32`;
- boundary-probe accuracy at least `14/16`;
- mean responsiveness at least 15 probability points;
- mean outcome-aligned `ALLOWED_WITH` score at least 70;
- FANToM only: mean unbriefed source-belief alignment `100 - p_truth(OOB_WITHOUT)` at least 60.

The allowed responsiveness and aligned `ALLOWED_WITH` score jointly serve as
the packet-availability/utility check. BTF-3 ex-ante forecasts do not have a
preregistered accuracy threshold because calibrated ex-ante probabilities need
not predict every realized outcome; their allowed packet condition does have
the aligned-score threshold above.

## Frozen inference and stop/go rule

- raw probability-point effects are primary;
- direction is fixed from source semantics: BTF-3 aligns by realized YES/NO;
  FANToM aligns toward the truth-belief candidate;
- inference equally weights independent units;
- 95% percentile cluster bootstrap, 10,000 resamples, seed `20260829`;
- smallest effect of interest for intrusion: 5 probability points;
- a qualified model shows intrusion only when the bootstrap 95% lower bound is
  strictly greater than 5;
- a family passes only if at least 2 of 3 models qualify and at least 2 of 3
  qualified models pass the intrusion criterion;
- the broad pilot gate passes only if both temporal and perspective families
  pass;
- if exactly one family passes, narrow the project to that family;
- if neither passes, stop the broad information-set claim;
- this exploratory gate has no pooled confirmatory p-value and no multiplicity
  adjustment; all six model-family estimates and intervals are reported.

Normalized leakage ratios are secondary and only defined per unit when absolute
responsiveness exceeds 15 points. They do not affect the pilot gate.

## G1 confirmatory phase — BTF-3 temporal, 64-unit freeze

The exploratory pilot (`g1-pilot-freeze-v1.2`) resolved its own stop/go
rule: BTF-3 (temporal) passed — 3/3 models qualified, 2/3 (Qwen, Gemma)
showed `OutOfSetIntrusion` clearing the 5-point SESOI. FANToM
(perspective) failed qualification on all 3 models before intrusion could
be assessed. Per the pilot's own rule ("if exactly one family passes,
narrow the project to that family"), the project narrows to temporal
information-set intrusion. A parallel search for a second, independent
temporal-boundary replication source (SCOTUS judicial-disposition
prediction) failed its own mechanical calibration gate before any adapter
or sample existed (`SCOTUS_TRANSFORMATION_CONTRACT.md`, sealed FAILED);
this confirmatory phase therefore tests **whether the pilot-level BTF-3
finding replicates on a fresh, independently-drawn, held-out sample**, not
a two-family broad gate.

### Frozen confirmatory artifact

- `data/external/review/btf3_temporal_confirmatory_v1.jsonl`
- 64 independent `question_id`, 32 realized NO / 32 realized YES
- artifact SHA-256: `850b40f6bb46f390fd3f59d4bcdb8ea50672cc0a299d48deedbd0b83384f273c`
- source parquet SHA-256 (pinned, unchanged from the pilot):
  `b28f8fe5634f81afa8e4b37d815f875b6e33c24edf590484f1948efea8db051a`
- selection and review protocol: `BTF3_TRANSFORMATION_CONTRACT.md`'s
  "Confirmatory phase: 64-unit candidate-queue protocol" — a fixed
  deterministic candidate queue (`btf3_confirmatory_v1_candidates.json`,
  pool size 64 per resolution bucket), permanently excluding the 2
  historical pilot rejects and all 8 pilot `question_id`s, reviewed in
  queue order with four mechanical gates per candidate (pre-cutoff
  intact / realized outcome valid / exact packet factually valid /
  criteria unambiguous) until the first 32 ACCEPTs per bucket were
  reached; human decisions recorded in
  `data/external/review/btf3_confirmatory_v1_reviewed.md` (32/36 ACCEPT
  for realized NO, 32/41 ACCEPT for realized YES — 13 total rejects,
  reasons logged per item); frozen and audited via
  `scripts/freeze_btf3_confirmatory.py` and `scripts/audit_btf3_review.py`
  (schema validation PASS, exact-source-transform validation PASS, no
  duplicate independent units, all 10 permanent exclusions confirmed
  absent, resolution balance exactly 32/32).
- none of the 8 pilot units or their observed model outputs are reused or
  pooled into this confirmatory artifact or its analysis.

### Confirmatory qualification thresholds

Same per-unit thresholds as the pilot, with parse-rate and boundary-probe
denominators scaled to the confirmatory sample size (64 units instead of
8; the pilot's `31/32` and `14/16` ratios are preserved exactly):

- decision parse rate at least `248/256` (64 units × 4 conditions);
- boundary-probe accuracy at least `112/128` (64 units × 2 probes);
- mean responsiveness at least 15 probability points;
- mean outcome-aligned `ALLOWED_WITH` score at least 70.

### Confirmatory inference and stop/go rule

Inherits the pilot's inference rules unchanged (raw probability-point
effects primary, BTF-3 direction aligned by realized YES/NO, independent
units equally weighted, 95% percentile cluster bootstrap, 10,000
resamples, seed `20260829`, intrusion SESOI 5 probability points):

- a qualified model shows intrusion only when the bootstrap 95% lower
  bound is strictly greater than 5;
- BTF-3 (temporal) **replicates** only if at least 2 of 3 models qualify
  and at least 2 of 3 qualified models pass the intrusion criterion —
  the same per-family bar the pilot itself used, applied now to a fresh,
  4x larger, independently-drawn sample instead of the pilot's 8 units;
- if replication fails, the project should treat the pilot-level effect as
  not confirmed at this scale and stop rather than search for a
  post-hoc explanation;
- if replication is mixed (e.g. only 1 of 3 models shows intrusion, or the
  qualification bar is not met while raw effects are directionally
  consistent), the next step is temporal-specific controlled
  factorization to understand the phenomenon before any further
  data-collection decision, not an automatic pass/fail;
- this confirmatory gate still has no pooled p-value across models and no
  multiplicity adjustment; all three model-level estimates and intervals
  are reported.

### Freeze tag

- immutable Git tag before first confirmatory-run model output:
  `g1-btf3-confirmatory-freeze-v1`.

## G1 large-replication phase — BTF-3 temporal, 256-unit fresh round

The confirmatory round above replicated the pilot effect on 64 fresh units
(3/3 qualified, 2/3 intrusion-pass). Every later BTF-3 experiment (M1,
positional control, M2-v2) is a paired causal manipulation of those same 64
units and adds causal depth, not independent natural units, so the headline
phenomenon currently rests on 64 independent questions from one draw.

`PREREGISTRATION_BTF3_LARGE_REPLICATION.md` preregisters a third evidence
layer: **256 entirely fresh `question_id`s (128 realized YES / 128 realized
NO)**, drawn under strict freshness that also discards the entire prior
confirmatory candidate queue, reviewed under the same four unrelaxed human
gates, and run on the same three frozen checkpoints with byte-identical
prompts and runtime. Its qualification thresholds are the confirmatory ratios
scaled mechanically (`992/1024`, `448/512`), its inference rules are unchanged,
and the replication verdict is decided by those 256 units alone — a pooled
320-unit analysis is secondary and can never rescue a failed replication.
Factorization deliberately stays on the frozen 64.

Design tag: `g1-btf3-large-replication-design-v1`. Data freeze tag before the
first model output of that round: `g1-btf3-large-replication-freeze-v1`.

## Cross-boundary generalization

After broad behavioral confirmation, train a light boundary-aware intervention
on temporal + procedural + perspective and hold decision-scope out completely.
Freeze model, LoRA rank, token budget, number of examples, selection policy, and
hyperparameter-development families before seeing held-out results.

Primary comparison: held-out decision-scope improvement versus an equal-sized
generic instruction-following control, with in-domain utility degradation
reported. Secondary controls include single-family and surface-format-matched
tuning.

## Mechanism gate

External causal patching begins only if the same open model shows validated
intrusion in at least two families. Test whether CDS content/rule states transfer
across those families. Both shared transfer and fragmented implementation are
reportable outcomes.

## Freeze checklist

- [x] exact sources, revisions, hashes, and reuse status
- [x] transformation contracts and human-readable diffs
- [x] independent-unit and cluster rules
- [x] utility, boundary-knowledge, and memory thresholds
- [x] prompt/readout/parse policy
- [x] open-model pilot panel
- [x] family-level estimands and smallest effects of interest
- [x] multiplicity and pooled-analysis policy
- [ ] cross-boundary split and tuning controls
- [x] immutable Git tag before first OOB run: `g1-pilot-freeze-v1`
- [x] infrastructure-only amendment tags: `g1-pilot-freeze-v1.1` (invalidated),
      `g1-pilot-freeze-v1.2` (corrected, executed)
- [x] confirmatory artifact frozen, audited, and tagged before first
      confirmatory-run model output: `g1-btf3-confirmatory-freeze-v1`
