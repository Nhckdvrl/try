# G4 preregistration — How wide is the recognition–enforcement dissociation?

**Created:** 2026-09-01
**Status:** design frozen. Tag `g4-model-breadth-design-v1` identifies this
document, the frozen panel (`data/model_panel_g4.json`), the dispatcher, and
the analyzer — all before any new checkpoint produces output.

---

## 1. The sub-question

This experiment answers one sub-question of the headline question in
`PAPER_FRAME.md` §1:

> Is the recognition–enforcement dissociation a property of three checkpoints,
> or of contemporary instruction-tuned language models generally?

It is the same branch that a strong phenomenon paper always carries: after
establishing that the effect is real on one panel, show whether it is a
property of the class. It answers a reviewer question that no amount of extra
units on three models can answer.

It is explicitly **descriptive breadth**, not a gate on the project. The
headline claim of the paper does not become true or false here; it becomes
narrower or wider.

## 2. Panel, frozen before any run

`data/model_panel_g4.json` — 17 checkpoints, 8 families/generations, 3.8B to
35B, one MoE, listed with the exact HF snapshot revision present in the shared
cache at freeze time.

Five of the 17 already have output from earlier preregistered rounds
(`qwen35-4b`, `qwen35-9b`, `qwen35-27b`, `gemma3-12b`, `mistral-small-24b`).
They are **reused, not re-run**: their prompts, decoding, parser, and estimator
are byte-identical to what this round dispatches, and the file each is read
from is named in the analysis output. The 12 marked `new` are what this round
generates: 12 × 1,024 decisions + 12 × 512 probes = **18,432 generations**.

The panel is frozen as a whole. A checkpoint that fails to load or does not fit
the frozen 8,192-token budget is reported as such by tag; it is not silently
dropped and it is not replaced by a different checkpoint after the fact.

## 3. Everything else is inherited unchanged

Artifact (256 units, SHA-256 `0b6fd8d0…acf0901d`), the four conditions
(`oob_without`, `oob_with`, `allowed_without`, `allowed_with`), the two
boundary probes, the system prompt, chat templating with thinking disabled
where the template supports it, greedy decoding at temperature 0, seed 0,
`max_tokens` 8, `max_model_len` 8192, both parsers, direction `s = 2r − 1`, and
the 95% percentile cluster bootstrap over `question_id` with 10,000 resamples
at seed `20260829`. The runner is `src/run_information_set.py`, unmodified.

## 4. Estimands and qualification — identical to the large replication

Per checkpoint:

```text
Responsiveness    = mean_i s_i * ( p_i[allowed_with] - p_i[allowed_without] )
OutOfSetIntrusion = mean_i s_i * ( p_i[oob_with]     - p_i[oob_without]     )
```

Qualification, unchanged from `PREREGISTRATION_BTF3_LARGE_REPLICATION.md`:
decision parse rate ≥ `992/1024`, boundary-probe accuracy ≥ `448/512`, mean
responsiveness ≥ 15.0 points, mean aligned `ALLOWED_WITH` ≥ 70.0.

An unqualified checkpoint is reported with its numbers and excluded from the
panel counts. Qualification is a statement about whether the instrument works
on that checkpoint, not about whether the checkpoint is contaminated.

## 5. Primary reported quantities, fixed now

1. **Prevalence.** The number of qualified checkpoints passing the
   large-replication analyzer's own `intrusion_pass` rule — 95% CI lower bound
   strictly above the 5.0-point SESOI — out of the number qualified. The rule
   is inherited verbatim from `src/analyze_btf3_large_replication.py` and is
   not redefined here.
2. **The dissociation, quantified across the panel.** Spearman rank
   correlation between boundary-probe accuracy and `OutOfSetIntrusion` over
   qualified checkpoints, with a permutation CI. Prediction, recorded now:
   **no reliable negative relationship** — recognition is at or near ceiling
   everywhere while intrusion varies widely, so the two do not track each
   other. A reliable negative correlation would falsify that prediction and
   must be reported as such.
3. **Family and size spread.** Intrusion by family and by parameter count,
   reported as a table. **No scaling law is fitted and no slope is reported.**
   The Qwen3.5 size analysis already showed the within-family trend is
   non-monotone; this panel confounds size with family and cannot resolve it.

## 6. What may and may not be concluded

**May be concluded**, if prevalence is high: that the dissociation is a
property of contemporary instruction-tuned models across families and training
recipes, not of three checkpoints.

**May not be concluded:** anything about *why* a particular checkpoint sits
high or low; any scaling claim; any claim about base versus instruction-tuned
models (the panel contains no base checkpoints, by design, because the task
requires instruction following); any claim about closed models.

**Anticipated and disclosed now:** some checkpoints will fail qualification —
small models in particular may not clear the responsiveness floor, i.e. they do
not use the licensed evidence properly and therefore cannot be asked whether
they wrongly use unlicensed evidence. That is an instrument limit and is
reported as one.

## 7. Order of operations

1. Freeze this document and the panel JSON; tag `g4-model-breadth-design-v1`.
2. Dispatch the 12 new checkpoints.
3. Run the analyzer once over all 17.
4. Report every checkpoint, qualified or not, including load failures.

## 8. Freeze checklist

- [x] `PREREGISTRATION_G4_MODEL_BREADTH.md` committed
- [x] `data/model_panel_g4.json` committed
- [x] `scripts/run_model_breadth.sh` committed
- [x] `src/analyze_model_breadth.py` committed
- [ ] `g4-model-breadth-design-v1` tagged
- [ ] first new-checkpoint generation only after the tag exists
