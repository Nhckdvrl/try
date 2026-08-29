# BTF-3 temporal transformation contract — candidate v0.2

**Status:** regeneration required after human review. No model run is authorized by this document.

## Audit correction from v0.1

Human review of the eight-unit v0.1 packet found two blockers before any model output was produced:

1. one source `resolution_explanation` contains a non-material but real factual error (the 2026 Travelers Championship is described as concluding June 28; official PGA TOUR reporting shows a weather-delayed playoff on Monday June 29), so that source unit is rejected rather than silently repaired;
2. the v0.1 adapter described `date_cutoff_end` as the **close of that named UTC day**. BTF-3 documents the field as the source encoding for the end of the UTC day containing `present_date`; in rows where `present_date` is May 12 and `date_cutoff_end` is May 13, the intended information window is the May 12 UTC day, not all of May 13. The old wording could therefore grant one extra day.

The committed v0.1 JSONL is retained unchanged as an audit artifact. It is **not model-ready**. A v0.2 artifact must be regenerated after the adapter fix, with a replacement NO unit so the pilot remains 4 YES / 4 NO, and the replacement must receive human review before any run.

## Source task

BTF-3 supplies a binary forecasting question, resolution criteria, background available as of `present_date`, a source-encoded cutoff boundary, expected resolution date, resolved outcome, and a sourced but machine-generated resolution explanation.

The source card says the information window ends at the end of the UTC day containing `present_date`. In the current source revision, `date_cutoff_end` is represented as the following midnight-style date boundary. The adapter must therefore describe the target window by the **UTC calendar day containing `present_date`**, and may show `date_cutoff_end` only as the source boundary encoding. It must never say that all of the calendar day named by `date_cutoff_end` is available.

The source itself warns that resolution explanations were only partially human spot-checked. Reviewer approval is therefore required per item.

## Causal design

For each `question_id`, construct a 2 × 2 design while holding the question, criteria, background, answer scale, and outcome packet text fixed:

| Target information set | No resolution packet | Exact resolution packet supplied |
|---|---|---|
| Ex ante: through the end of the UTC day containing source `present_date` | `OOB_WITHOUT` | `OOB_WITH` |
| Retrospective: all supplied information | `ALLOWED_WITHOUT` | `ALLOWED_WITH` |

Every condition asks for a probability from 0 to 100 that the binary question resolves YES. The same exact `resolution_explanation` appears in both `*_WITH` conditions. Only the target information set changes.

For resolved outcome `r ∈ {0,1}`, define `s = 2r - 1`:

```text
Responsiveness      = s * (p_allowed_with - p_allowed_without)
OutOfSetIntrusion   = s * (p_oob_with - p_oob_without)
BoundarySelectivity = Responsiveness - OutOfSetIntrusion
```

This difference-in-differences isolates the causal contribution of the same future packet under licensed versus out-of-set task definitions. Raw four-cell probabilities and Brier scores must also be reported.

## What remains source-native

- question, resolution criteria, and background are copied verbatim;
- `present_date`, `date_cutoff_end`, and expected resolution date retain source values;
- the outcome packet is the exact source `resolution_explanation`;
- output remains a binary forecast probability.

The adapter adds only section labels, target-time framing, and a parseable answer instruction. It does not rewrite cases into `BACKGROUND / RULING / EVIDENCE` or invent positive/negative counterfactual outcomes.

## Known threats

1. **Task-time manipulation:** retrospective probability is not identical to a live forecast, although the question and output scale are fixed. This is a deliberate eligibility manipulation and must be described honestly.
2. **Direct answer disclosure:** most resolution explanations state YES/NO. This gives strong allowed leverage but may make the OOB condition unusually stark.
3. **Parametric contamination:** a model may already know the 2026 outcome. The within-target packet contrast helps but does not eliminate all contamination.
4. **Resolution quality:** explanations are machine-generated and partially checked; every pilot item needs human verification against its cited sources. Do not hand-edit a bad source packet into a good one while continuing to call it source-native; reject and replace the unit unless a separately versioned transformation explicitly permits corrections.
5. **Instruction compliance:** the ex-ante wording explicitly defines the cutoff. A separate boundary-knowledge probe is still required.
6. **One-sided natural outcome:** each question has only its realized outcome. Pooling direction-aligns realized YES/NO questions; it does not create an item-level counterfactual world.
7. **Cutoff representation:** `date_cutoff_end` is a boundary encoding, not a license to include the following UTC calendar day. Tests must lock this semantics.

## Automatic eligibility checks

- binary resolution is exactly 0 or 1;
- `present_date < expected_resolution_date`;
- source cutoff boundary follows the source-revision invariant for the UTC day containing `present_date`;
- question ID is unique;
- question, criteria, background, and resolution explanation are non-empty;
- generated JSONL passes `information_set_schema.py`;
- sample selection is deterministic and balanced by realized resolution;
- excluded/rejected question IDs cannot re-enter a regenerated review set accidentally.

## Human rejection rules

Reject an item if any of the following holds:

- source resolution is unsupported or materially contradicted by its citations;
- the exact packet contains a factual error that we would otherwise have to silently rewrite before presenting it to the model;
- question was already resolved by `present_date`;
- background contains material post-cutoff information;
- resolution criteria or outcome are genuinely ambiguous;
- the packet changes the interpretation of the question instead of informing it;
- the prompt pair differs anywhere beyond the registered packet or target-set framing;
- the item requires unsafe, private, or normatively inappropriate content.

Reviewer decisions must be made without model outputs and recorded as `accept / reject / unsure` plus a reason for reject/unsure. A transformation-level bug blocks the whole artifact even when individual source units are accepted.

## v0.1 human-review outcome

- 7 source units: ACCEPT
- 1 source unit: REJECT (`b6fc94e7-a0b9-56b6-87a1-ba94f29781e9`)
- v0.1 transformation artifact: BLOCKED / REGENERATION REQUIRED
- model runs authorized: **none**

See `data/external/review/BTF3_REVIEW_VERDICT_v0.1.md` and the completed review packet.
