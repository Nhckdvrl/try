# G1 preregistration — Information-Set Reasoning

**Created:** 2026-08-29  
**Status:** draft; must be frozen after source transformation audit and before
the first target-model OOB run.

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

- [ ] exact sources, revisions, hashes, and reuse status
- [ ] transformation contracts and human-readable diffs
- [ ] independent-unit and cluster rules
- [ ] utility, boundary-knowledge, and memory thresholds
- [ ] prompt/readout/parse policy
- [ ] open-model pilot panel
- [ ] family-level estimands and smallest effects of interest
- [ ] multiplicity and pooled-analysis policy
- [ ] cross-boundary split and tuning controls
- [ ] Git commit hash and timestamp before first OOB run
