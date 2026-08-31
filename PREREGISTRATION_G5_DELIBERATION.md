# G5 preregistration — Does deliberation reconstruct the ex-ante state?

**Created:** 2026-09-01
**Status:** design frozen. Tag `g5-deliberation-design-v1` identifies this
document, the builder, the audit, the analyzer, and the tests — all before any
generation in any arm.

---

## 1. The sub-question, and the pair it separates

Sub-question of `PAPER_FRAME.md` §1:

> If the model is made to reason explicitly — and in particular, if it is made
> to *reconstruct the information state* before judging — does the hindsight
> contamination go away?

This is the experiment a reviewer asks for first, and it is not merely a
robustness check. It separates two of the accounts in `PAPER_FRAME.md` §4:

- **H-absent** says no time-indexed belief state is ever constructed; the
  answer runs on the single current, fully-informed belief while recognition
  runs beside it. Prediction: **forcing** explicit construction of the ex-ante
  state supplies what is missing, and the `state` arm reduces intrusion
  substantially more than free-form `cot`.
- **H-truth** says the model's answer is its posterior over what it believes
  true, and no amount of reasoning about *when* a true fact arrived removes it
  from that posterior. Prediction: `state` behaves like `cot`; whatever
  reduction appears is the generic benefit of deliberation, not of state
  construction.

The contrast that decides it is `state` versus `cot`, not either arm versus
the direct baseline. That is why free-form `cot` is in the design: without it,
any reduction under `state` is uninterpretable.

**It is simultaneously the paper's first mitigation baseline.** Any
inference-time method proposed later must beat what a well-written prompt
already achieves, and this experiment measures that number instead of assuming
it.

## 2. The manipulation

The frozen artifact's `TASK` block is byte-identical in all 1,024 prompts and
sits at the very end of every one of them. Each arm replaces that block and
nothing else.

| arm | `TASK` block |
|---|---|
| `direct` | frozen baseline, unchanged (read, not re-run) |
| `cot` | "Reason step by step first, then answer." |
| `state` | fixed three-step scaffold: (1) list the facts available at the evaluation point; (2) state which text is outside that set and must not affect the answer; (3) answer using only step 1 |

Both new arms end with the identical instruction to finish with a line
`ANSWER: N`, so one strict parser serves both and neither gets a laxer readout
than the other.

Exact strings are in `src/adapters/btf3_deliberation.py`.

### Conditions

Both frames are run, because a mitigation that also destroys the model's use of
*licensed* evidence is not a mitigation:

```text
{cot, state} × {oob, allowed} × {with, without}   = 8 new conditions
```

plus, per arm and frame, the unchanged boundary probe on the `with` prompt
(4 probe conditions). The `direct` arm's four cells and two probes are read from
`results/raw/isr_<tag>_btf3_large_replication_v1.jsonl`.

**Volume:** 3 models × 12 conditions × 256 units = **9,216 generations**, at
`max_tokens` 640 for decision records in the new arms (probes stay at 8).

## 3. Frame, and the two things that necessarily change

Inherited unchanged: artifact and SHA-256, model panel and revisions, system
prompt, chat template with thinking disabled, temperature 0, seed 0,
`max_model_len` 8192, direction `s = 2r − 1`, boundary-probe wording, and the
95% percentile cluster bootstrap over `question_id`, 10,000 resamples, seed
`20260829`.

Two things change, and both are disclosed rather than hidden:

1. **Generation length.** Decision records in `cot` and `state` generate up to
   640 tokens instead of 8. A truncated completion with no `ANSWER:` line is an
   unparsed record and counts against the parse-rate floor.
2. **Readout.** The strict `0–100` full-match parser cannot read a reasoning
   completion. The frozen replacement is: take the **last** `ANSWER: N` line;
   no other extraction, no fallback to a bare number elsewhere in the text, no
   manual repair. Both new arms are read identically, so the `state`-vs-`cot`
   contrast is unaffected by this choice; comparisons against `direct` carry the
   readout difference as a caveat and are reported with it.

## 4. Estimands and gates

Per model, per arm `a`, per frame:

```text
I_a  = mean_i s_i * ( p_i[a, oob, with]     - p_i[a, oob, without]     )
R_a  = mean_i s_i * ( p_i[a, allowed, with] - p_i[a, allowed, without] )
```

**Primary contrast (the adjudication):**

```text
D = I_cot - I_state
```

paired per unit, bootstrapped over the same clusters.

**Secondary (mitigation size, reported with the readout caveat):**

```text
M_cot   = I_direct - I_cot
M_state = I_direct - I_state
```

**Utility guard, preregistered as a veto.** A reduction in `I` counts as
mitigation only if that arm's licensed responsiveness holds up:
`R_a ≥ 15.0` points and `R_a ≥ 0.7 · R_direct` in the same model. An arm that
lowers intrusion while failing the guard is reported as **damaging the task,
not enforcing the boundary**, and its reduction is not called mitigation.

### Qualification, per condition

Decision parse rate ≥ 96.875% (`248/256`); boundary-probe accuracy ≥ 87.5%
(`224/256`) in that arm and frame. Applied as written; failures reported with
their numbers.

### Decision rules, fixed now

- `D` shows **state-specific benefit** if `D ≥ 5.0` and its 95% CI excludes 0.
- `D` shows **no state-specific benefit** if its 95% CI lies within `[−5, +5]`.
- Anything else is indeterminate and supports no row.
- Panel rule: ≥ 2 of 3 qualified models.

### Interpretation table, fixed in advance

| `D` | permitted conclusion |
|---|---|
| state-specific benefit | Consistent with **H-absent**: what the model lacks is a constructed ex-ante state, and supplying the construction step recovers part of the judgment. Reported together with how much intrusion still remains under `state` — a partial reduction is not a solution. |
| no state-specific benefit | Consistent with **H-truth**: deliberation about *when* a fact arrived does not remove a believed-true fact from the posterior. Any reduction under either arm is generic deliberation benefit, and the paper says so. |
| indeterminate | No row. Report the interval. |
| either arm fails the utility guard | That arm is reported as task damage, whatever its intrusion number. |

## 5. What this does not do

- It does not claim the `state` scaffold is a deployable method. It is a
  prompt-level baseline, measured so that any later inference-time method has a
  number to beat.
- It does not test reasoning-mode ("thinking") checkpoints; the chat template
  keeps thinking disabled exactly as in every previous round, and the
  deliberation here is elicited in the visible completion where it can be
  parsed and audited.
- It does not re-select, drop, or re-review any unit.

## 6. Order of operations

1. Freeze this document, builder, audit, analyzer, tests. Tag
   `g5-deliberation-design-v1`.
2. Run the audit; it must pass, including the byte-identity check of the
   `direct` arm against the frozen artifact.
3. Generate. 4. Analyze once. 5. Report every arm and both frames.

## 7. Freeze checklist

- [x] `PREREGISTRATION_G5_DELIBERATION.md` committed
- [x] `src/adapters/btf3_deliberation.py` committed
- [x] `src/run_deliberation.py` committed
- [x] `src/analyze_deliberation.py` committed
- [x] `tests/test_deliberation.py` committed and passing
- [ ] `g5-deliberation-design-v1` tagged
- [ ] first generation only after the tag exists
