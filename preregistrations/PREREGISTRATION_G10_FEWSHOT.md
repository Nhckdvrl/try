# G10 preregistration — What actually fixes it?

**Created:** 2026-09-01. Tag `g10-fewshot-design-v1` before any generation.

*(A length control for G3's Gemma amplification was drafted and dropped. It
could only ever weaken a side observation, never produce a finding, and it was
not worth 4,608 generations. This replaces it.)*

---

## 1. The question

G3 showed that no *stated reason* reduces the effect. That leaves the strongest
prompt-level intervention available untested: **showing the model what the
correct behaviour looks like.**

> Do worked demonstrations of correct ex-ante reasoning — the packet present,
> visibly not used — reduce hindsight contamination?

Both answers are worth having. If demonstrations work, that is a cheap,
deployable fix and a positive result. If they do not, then together with G3
nothing that can be *said* to the model works, and the inference-time method in
G6 is the only thing left that does.

## 2. The manipulation

Three worked demonstrations are prepended to the out-of-set prompt, in both
cells. Each demonstration is a **held-out** BTF-3 binary question — none of the
328 units used by the pilot, confirmatory, or large-replication rounds — shown
in the same shape as the task and answered with **the dataset's own SOTA ex-ante
forecast probability**, so the demonstrated answer is not our invention.

Demonstrations are compacted by a frozen rule so three of them fit the 8,192
budget: the question, the out-of-set sentence, the first three sentences of the
packet, and `ANSWER: <sota>`. No background, no resolution criteria.

Selection, fixed before any run: two realized-NO and one realized-YES,
**ranked by how far the dataset's own ex-ante forecast sits from the realized
outcome**, `|anchor − 100·resolution|`, largest gaps first. A demonstration only
teaches the behaviour if the warranted answer is visibly *not* the outcome the
packet reveals; the chosen three are packet-says-NO/answer-93,
packet-says-YES/answer-3, and packet-says-NO/answer-92. Both fields are source
fields and no model output participates; the seed only breaks ties. Prefix
digest `e44dfbde…`, 925 tokens; longest resulting prompt 5,428 tokens against
the frozen 8,192 budget.

### Conditions

`fewshot_oob_with`, `fewshot_oob_without`, and the unchanged boundary probe on
the `with` prompt. Both reference cells are the frozen large-replication output.

**Volume:** 3 models × 3 conditions × 256 units = **2,304 generations**.

## 3. Estimand and decision rule

```text
I_fewshot = mean_i s_i ( p_i[fewshot_with] - p_i[fewshot_without] )
M         = I_temporal - I_fewshot        (paired, same units)
```

- **Works** if `M ≥ 5.0` and its 95% CI excludes 0, in ≥ 2 of 3 qualified
  models.
- **Does not work** if `M`'s 95% CI lies within `[−5, +5]` in ≥ 2 of 3.
- Otherwise indeterminate.

Qualification and inference are G3's, unchanged: parse rate ≥ `248/256`,
boundary probe ≥ `224/256`, 95% percentile cluster bootstrap over `question_id`,
10,000 resamples, seed `20260829`.

**Utility guard.** Reported alongside: the demonstrations must not simply drag
every answer toward the demonstrated numbers. A reduction counts only if
`Responsiveness` in the licensed frame is not run — instead, the guard here is
that `p[fewshot_without]` must not collapse toward the demonstration answers:
the correlation between `p[fewshot_without]` and `p[oob_without]` is reported,
and a reduction accompanied by a correlation below 0.5 is reported as the model
copying the demonstrations rather than reasoning.

## 4. Freeze checklist

- [x] `PREREGISTRATION_G10_FEWSHOT.md`
- [x] `src/adapters/btf3_fewshot.py`
- [x] `src/run_fewshot.py`
- [x] `src/analyze_fewshot.py`
- [x] `tests/test_fewshot.py`
- [ ] `g10-fewshot-design-v1` tagged
- [ ] first generation only after the tag exists
