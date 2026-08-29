# FANToM perspective transformation contract — candidate v0.1

**Status:** transformation PASS and final v0.1r4 source set accepted. Pilot-ready after repository-wide preregistration freeze.

## Scientific target

FANToM natively asks what a participant believes when part of a multi-party conversation occurred during that participant's absence. The evaluator sees the whole conversation and therefore knows more than the target character. This candidate transformation tests whether a model can keep those information sets distinct.

It does **not** use `factQA` as the allowed condition and `beliefQA` as the outside condition. That shortcut would change the target question and target subject at the same time. Instead, all four cells retain one first-order inaccessible belief question and the same two source-authored answer candidates.

## Eligible source rows

An eligible row must have:

- exactly one first-order `beliefQA` labeled `inaccessible` whose question names the `joining_speaker`;
- one source-native binary information-accessibility question for that speaker with answer `no`;
- non-empty and distinct source `correct_answer` and `wrong_answer` belief candidates;
- non-empty fact question, correct fact answer, and fact distractor.

The source `wrong_answer` for the inaccessible belief question normally describes the truth-tracking belief the character would hold if informed. This answer is called the **truth-belief candidate** in the transformation; it must receive human semantic-alignment review before use.

## Four-cell intervention

The conversation, belief question, candidate answers, candidate order, output scale, and exact fact packet are held fixed.

| Target character's information set | No separate fact packet | Exact fact packet supplied |
|---|---|---|
| End of source conversation; evaluator-only packet was never heard by target | `OOB_WITHOUT` | `OOB_WITH` |
| After source conversation; supplied packet is explicitly told to target | `ALLOWED_WITHOUT` | `ALLOWED_WITH` |

The packet is constructed only from the source-native fact QA:

```text
Question: {factQA.question}
Answer: {factQA.correct_answer}
```

The model returns a 0–100 probability that the truth-belief candidate correctly describes the target person's belief. Candidate A/B order is fixed deterministically from `set_id` before any model output.

Expected behavior:

- outside target set: the probability of the truth-belief candidate stays low with or without the evaluator-only packet;
- allowed target set: the probability stays low without a briefing and rises when the target is explicitly told the packet.

Thus:

```text
Responsiveness      = p_allowed_with - p_allowed_without
OutOfSetIntrusion   = p_oob_with - p_oob_without
BoundarySelectivity = Responsiveness - OutOfSetIntrusion
```

## Source-native probes

- **Boundary knowledge:** the official binary `infoAccessibilityQA` for the joining speaker; expected answer `no`.
- **Fact availability:** the official `factQA` with its source correct answer and distractor.
- **Task utility:** positive allowed responsiveness under explicit post-conversation briefing.

Probe rendering and parse thresholds must be frozen in G1 before the first target-model OOB run.

## Independent unit and selection

`part_id` is the provisional independent semantic unit because multiple `set_id` rows share a latent conversation part. The review sampler selects at most one eligible `set_id` per `part_id`, then samples parts by a seeded hash. No model behavior participates in eligibility or selection.

Before a broad freeze, shared content across different `part_id` values must still be audited. Pilot inference clusters on `part_id` and never treats answer variants as independent situations.

## Authorship and reuse status

- conversation, belief question, both belief candidates, fact question, fact answer, and boundary probe are copied from FANToM;
- section labels, target-information-set framing, counterfactual post-conversation briefing, probability readout, and deterministic option order are authored by this project;
- the resulting task is a source-anchored causal transformation, not an untouched reproduction of the original FANToM score;
- the official repository is MIT and its README says samples should be used for evaluation. The committed transformed artifacts are explicitly evaluation-only, retain source attribution, and must not be represented as an original FANToM score reproduction.

## Human rejection rules

Reject a row if:

- the target character did hear or learn the fact in the displayed conversation;
- the source correct belief candidate does not represent the target's unbriefed belief;
- the truth-belief candidate does not represent the belief induced by the exact fact packet;
- the packet is incomplete, ambiguous, or conflicts with the displayed conversation;
- explicitly telling the packet would not make the truth-belief candidate correct;
- the question changes meaning between unbriefed and briefed evaluation points;
- any full prompt differs beyond registered target framing or packet insertion;
- unsafe/private content appears.

Reviewer decisions are made without model outputs. A failure in the causal alignment blocks the item even when the original FANToM question itself is valid.

## Review outcome

- v0.1 transformation: PASS
- original v0.1 units: 6 ACCEPT / 2 REJECT
- replacement-only reviews rejected Jamie and Kasey, accepted Camryn and Phoebe
- final v0.1r4 artifact: 8 accepted `part_id` units
- final JSONL: `data/external/review/fantom_perspective_pilot_v0.1r4.jsonl`
- target-model outputs inspected before freeze: none
