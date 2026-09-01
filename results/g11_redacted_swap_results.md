# G11 verdict-redacted foreign-packet swap — results

**Design tag:** `g11-redacted-swap-design-v1`. The tag precedes every target
generation. New volume: 1,536 generations (3 models × 256 decisions × decision
plus boundary probe). All prompts use frozen artifact SHA-256 `0b6fd8d0…acf0901d`
and frozen G8 pairing SHA-256 `a51b80c…cec1c2`.

## Question

G8 showed that a packet from an unrelated question perturbs the current
judgment and, descriptively in all three models, pulls it toward the donor
question's outcome. G11 asks whether that directional import is only explicit
YES/NO copying. It applies G2's frozen mechanical verdict redaction to G8's
same donor packets and changes nothing else.

The transform removed 368 verdict sentences; 19 of 256 packets contained no
matched verdict and were unchanged. No assertive verdict survived the audit.

## Results

All three models qualify. Decision parse rates are 99.61–100%; boundary
recognition is 100% in every model. Recipient-own pull remains within the
preregistered `[-5,+5]` validity interval.

| model | full donor pull | redacted donor pull | retention | explicit-label contribution | row |
|---|---:|---:|---:|---:|---|
| Qwen3.5-9B | 4.97 [2.11, 7.81] | **3.67 [0.84, 6.42]** | **73.9%** | 1.30 [-1.05, 3.83] | survives |
| Gemma-3-12B-it | 12.26 [9.64, 14.93] | **8.23 [5.92, 10.67]** | **67.1%** | 4.03 [2.34, 5.89] | survives |
| Mistral-Small-24B | 2.93 [1.71, 4.22] | 1.03 [0.10, 1.99] | 35.0% | 1.91 [0.82, 3.08] | verdict-dependent |

**Preregistered panel verdict: `survives` (2/3; all 3 qualified).**

Permitted claim:

> Explicit answer copying is insufficient: an irrelevant question's outcome
> evidence still pulls the judgment toward that question's outcome.

This is a panel claim, not a universality claim. Mistral is a real exception:
its explicit verdict contributes most of its already-small donor pull. Gemma
also has a nonzero explicit-label contribution, even though most of its effect
survives. Redaction does not hide the outcome; remaining evidence can entail
it. The result separates explicit verdict copying from outcome-evidence
integration, not known from unknown outcomes.

### Post-result transformation audit

Nineteen packets had no matched explicit verdict and were unchanged. Restricting
descriptively to the 236–237 packets where redaction actually changed the text
gives donor pull 3.92 [0.92, 6.93] for Qwen, 8.84 [6.27, 11.43] for Gemma, and
1.32 [0.35, 2.34] for Mistral. This was not a preregistered gate and is labelled
post-result; it shows that unchanged packets do not drive the survival result.
