# BTF-3 temporal transformation contract — candidate v0.1

**Status:** human review only. No model run is authorized by this document.

## Source task

BTF-3 supplies a binary forecasting question, resolution criteria, background
available as of `present_date`, the end of that UTC information window, the
expected resolution date, a resolved outcome, and a sourced but machine-generated
resolution explanation.

The source itself warns that resolution explanations were only partially human
spot-checked. Reviewer approval is therefore required per item.

## Causal design

For each `question_id`, construct a 2 × 2 design while holding the question,
criteria, background, answer scale, and outcome packet text fixed:

| Target information set | No resolution packet | Exact resolution packet supplied |
|---|---|---|
| Ex ante: through source `date_cutoff_end` | `OOB_WITHOUT` | `OOB_WITH` |
| Retrospective: all supplied information | `ALLOWED_WITHOUT` | `ALLOWED_WITH` |

Every condition asks for a probability from 0 to 100 that the binary question
resolves YES. The same exact `resolution_explanation` appears in both `*_WITH`
conditions. Only the target information set changes.

For resolved outcome `r ∈ {0,1}`, define `s = 2r - 1`:

```text
Responsiveness      = s * (p_allowed_with - p_allowed_without)
OutOfSetIntrusion   = s * (p_oob_with - p_oob_without)
BoundarySelectivity = Responsiveness - OutOfSetIntrusion
```

This difference-in-differences isolates the causal contribution of the same
future packet under licensed versus out-of-set task definitions. Raw four-cell
probabilities and Brier scores must also be reported.

## What remains source-native

- question, resolution criteria, and background are copied verbatim;
- `present_date`, cutoff, and expected resolution date retain source values;
- the outcome packet is the exact source `resolution_explanation`;
- output remains a binary forecast probability.

The adapter adds only section labels, target-time framing, and a parseable answer
instruction. It does not rewrite cases into `BACKGROUND / RULING / EVIDENCE` or
invent positive/negative counterfactual outcomes.

## Known threats

1. **Task-time manipulation:** retrospective probability is not identical to a
   live forecast, although the question and output scale are fixed. This is a
   deliberate eligibility manipulation and must be described honestly.
2. **Direct answer disclosure:** most resolution explanations state YES/NO. This
   gives strong allowed leverage but may make the OOB condition unusually stark.
3. **Parametric contamination:** a model may already know the 2026 outcome. The
   within-target packet contrast helps but does not eliminate all contamination.
4. **Resolution quality:** explanations are machine-generated and partially
   checked; every pilot item needs human verification against its cited sources.
5. **Instruction compliance:** the ex-ante wording explicitly defines the
   cutoff. A separate boundary-knowledge probe is still required.
6. **One-sided natural outcome:** each question has only its realized outcome.
   Pooling direction-aligns realized YES/NO questions; it does not create an
   item-level counterfactual world.

## Automatic eligibility checks

- binary resolution is exactly 0 or 1;
- `present_date < expected_resolution_date`;
- question ID is unique;
- question, criteria, background, and resolution explanation are non-empty;
- generated JSONL passes `information_set_schema.py`;
- sample selection is deterministic and balanced by realized resolution.

## Human rejection rules

Reject an item if any of the following holds:

- source resolution is unsupported or contradicted by its citations;
- question was already resolved by `present_date`;
- background contains material post-cutoff information;
- resolution criteria or outcome are genuinely ambiguous;
- the packet changes the interpretation of the question instead of informing it;
- the prompt pair differs anywhere beyond the registered packet or target-set
  framing;
- the item requires unsafe, private, or normatively inappropriate content.

Reviewer decisions must be made without model outputs and recorded as
`accept / reject / unsure` plus a reason.

