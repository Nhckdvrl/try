# The mechanism readout is blind to class-marker binding

**Code:** `src/mech/readout_validity_binding.py`.
**Data:** `results/mech/readout_validity_binding.json`,
`results/raw/qwen3-8b_stage3.jsonl`.
**Status:** diagnostic, run to explain G16's bridge failure. Interpretation was
pre-committed in the script docstring before the run.

## The question

Every mechanism result in this project uses the fixed-position one-token `direct`
readout: the span gate, the answer-position patching curve, Stage 5's matched
interchange, and G16. That readout was validated against the behavioural readout on
the **position** contrast only — `results/mech/direct_readout.json` contains `base`,
`admit_pre/post` and `exclude_pre/post`, and nothing else.

G16 returned a precise null on the class-versus-identifier contrast where the
behavioural readout shows a large effect in six models. Two candidates remained:
G16's 17-token length pad, or the readout.

## The test

Stage 3A's **unmodified** prompts — `id_base`, `id_admit_pre`, `id_admit_post`,
`oe_L0`, `cls_pre`, no padding, no changed grammar — run through the direct readout
on Qwen3-8B, against the behavioural numbers already on disk for the same prompts.

## Result — it is the readout

| readout | `oe_L0` (specific) | `cls_pre` (class) | class advantage |
|---|---|---|---|
| behavioural (two-sentence rationale) | 0.571 | 0.067 | **−0.503 [−0.754, −0.249]** |
| direct (one token, fixed position) | 0.405 | 0.450 | **+0.045 [−0.124, +0.232]** |

n = 69 / 72 usable items, `legal_judgment` + `evidence_inference`, cluster bootstrap
over case skeletons. Lower REI = more suppression; a negative advantage means the
class policy suppresses more.

**G16's construction was not at fault.** Its 17-token pad is exonerated: the null
appears on byte-identical Stage 3A prompts with no padding at all. What differs is
only whether the model writes a rationale before the readout position.

The sample explanation was already excluded separately: on G16's own two families the
behavioural class advantage is **−0.290 [−0.408, −0.164]** pooled over six models,
slightly *larger* than in the three families G16 omitted (−0.245 [−0.366, −0.126]).

## What this does and does not mean

**The direct readout is not globally blind to binding.** Stage 5's contrast —
a proposition-matched preview versus a length-matched unrelated one before the same
rule — is a binding manipulation, and the direct readout sees it clearly: a
behavioural gap of +8.56 rating points and a 2×2 interaction of −12.11 on the same
checkpoint. It also tracks the position contrast at item-level r = 0.76 and 0.90.

So the pattern is specific:

| binding manipulation | direct readout |
|---|---|
| position of the rule (pre vs post) | tracks it |
| content present before the rule (preview) | tracks it |
| **class marker travelling with the evidence** | **blind** |

The natural reading is that the class-marker advantage is **expressed in
deliberation** — the model has to resolve "is this item in the prohibited class?"
in its rationale — while content-preview binding and rule position are already
expressed in the immediate next-token distribution. This is consistent with
`results/metric_audit.md`, which documented before the dataset was frozen that a
single-token rating readout can anti-correlate with the model's own stated reasoning.

That reading is post-hoc and is offered as an interpretation, not a result.

## Consequences for the paper

1. **The mechanism section cannot speak to class-marker binding**, and must not
   imply that it does. Its scope is the position contrast and content-preview
   binding.
2. **G16 is not re-runnable as designed.** Redoing it with the behavioural readout is
   not a small change: matched-chronology interchange needs aligned token positions,
   and a generated rationale differs per condition and per item, which breaks the
   alignment the method depends on. This is a methods problem, not a compute problem,
   and it is very likely why the project used the direct readout for all mechanism
   work in the first place.
3. **This limitation must be stated in the paper**, next to the readout description,
   not buried in an appendix. A reviewer who asks "what else might your readout miss?"
   is asking a fair question, and the honest answer is that we found one such case and
   report it.
