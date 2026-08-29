# G1 preregistration — Information-Set Reasoning

**Created:** 2026-08-29  
**Status:** FROZEN for the two-family exploratory pilot. The immutable Git tag
`g1-pilot-freeze-v1` identifies the exact code, artifacts, and analysis policy
before the first target-model OOB run.

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
