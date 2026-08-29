# Research plan: Reasoning Within Bounds

## Mother question

> Do language models reason using the information set that actually defines the
> target task?

The behavioral contract has two directions:

```text
Responsiveness:         ΔY_allowed != 0
Out-of-set invariance:  ΔY_outside ≈ 0
```

The failure is **out-of-set intrusion**: information that the model sees or
knows changes a decision that is not licensed to depend on it.

## Scope

The planned paper asks whether information-set reasoning is a cross-boundary
capability across temporal, perspective, procedural, role/access, and
decision-scope tasks. It does not claim that this behavioral contract or any one
ignore failure is new. Novelty must come from source-native cross-boundary
evidence and tests of generalization.

CDS-v1 remains a Controlled Discovery Suite. Its prospective-nullification gap
and causal mechanism are retained as a later mechanistic section, not the
paper's dataset identity or title-level contribution.

## Phase 1 — source engineering (current)

1. Pin official files, revisions, hashes, and reuse status.
2. Audit the actual native schema and define the independent semantic unit.
3. Write one adapter and transformation contract per source.
4. Reject transformations that alter task target, normative boundary, and
   critical information simultaneously.
5. Validate JSONL with `src/information_set_schema.py`; run all unit tests.

No target-model DENY/OOB output may be used to select items.

## Phase 2 — exploratory behavioral gate

Use only 2–3 open models. For each family separately require:

- task utility above a frozen threshold;
- boundary/policy knowledge above a frozen threshold;
- memory/availability of the out-of-set fact where applicable;
- non-zero raw out-of-set intrusion on independent source units.

Proceed only if at least two materially different natural families pass. If not,
shrink the paper rather than adding synthetic variants to rescue the narrative.

## Phase 3 — broaden and freeze G1

Add procedural (Engel) and decision-scope (hiring) only after licenses and
source materials are verified. Freeze prompts, parsing, models, exclusions,
cluster rules, family-level tests, and stop/go thresholds before broad runs.

## Phase 4 — cross-boundary generalization

Primary capability test:

```text
train: temporal + procedural + perspective
test:  decision-scope (fully held out)
```

Use a light LoRA or comparably controlled intervention. Compare against:

- equal-sized single-family tuning;
- surface-format matched tuning;
- generic instruction-following tuning;
- no-tuning baseline.

Positive transfer supports a shared learnable competence. No transfer supports
a fragmented-heuristics account. Either result is informative if the held-out
family and hyperparameter policy are frozen.

## Phase 5 — external mechanism

Only after the behavioral gate, select one open model with failures in at least
two families. Test whether CDS rule/content states causally transfer across
temporal, perspective, and procedural tasks. Report either shared state transfer
or shared behavioral contract with fragmented implementations.

## Immediate next task

BTF-3 v0.2r2 has passed source and transformation review. Review the FANToM
perspective counterfactual without conflating fact QA with belief QA, resolve
full-text redistribution coverage, then freeze the two-family pilot's models,
parsing, probes, thresholds, estimands, and smallest effects before the first
target-model OOB output.
