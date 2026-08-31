# G5 deliberation — results

**Design tag:** `g5-deliberation-design-v1`. 9,216 generations, 3 models × 8
conditions × 256 units. Analysis: `results/g5_deliberation_analysis.json`.

## Panel verdict: indeterminate

By the frozen rule, no row of the interpretation table applies. Two separate
things prevented one, and both are execution problems rather than findings.

| model | arm | `I` | `R` (licensed) | retained | parse rate | qualified |
|---|---|---|---:|---:|---:|---|
| Qwen3.5-9B | direct | 16.02 [14.18, 17.89] | 47.27 | 1.00 | 1.0000 | yes |
| | cot | 10.23 [4.97, 15.80] | 41.61 | 0.88 | **0.1523** | no |
| | state | 2.08 [−3.03, 6.95] | 13.84 | **0.29** | **0.1719** | no |
| Gemma-3-12B | direct | 27.73 [25.15, 30.39] | 46.88 | 1.00 | 0.9961 | yes |
| | cot | 22.98 [20.25, 25.80] | 46.35 | 0.99 | **0.8555** | no |
| | state | 11.11 [8.97, 13.25] | 9.60 | **0.20** | 0.9805 | yes |
| Mistral-24B | direct | 7.46 [5.41, 9.57] | 39.31 | 1.00 | 1.0000 | yes |
| | cot | 15.04 [12.92, 17.18] | 37.76 | 0.96 | **0.9648** | no |
| | state | 6.88 [5.40, 8.44] | 4.25 | **0.11** | 0.9961 | yes |

## 1. The readout failed, badly, in the `cot` arm

`max_tokens` was frozen at 640 and the arms were required to end with
`ANSWER: N`. Qwen3.5-9B produced a parsable answer in **15%** of `cot` records
and 17% of `state` records; Gemma managed 86% on `cot`. Those conditions fail
the preregistered parse floor and are excluded, which is why the panel is
indeterminate.

This is an instrument failure, not a result about deliberation. The frozen
budget was too small for these models to finish reasoning and still emit the
answer line, and the strict last-`ANSWER:` parser — chosen so both arms are read
identically — has no fallback by design. Any future deliberation round needs a
larger budget and a pilot on parse rate before the full run.

## 2. The utility guard fired on `state` in all three models — and part of that is a design flaw of ours

Licensed responsiveness under the `state` scaffold collapses: 47.3 → 13.8,
46.9 → 9.6, 39.3 → 4.3, retaining 29%, 20% and 11%. The preregistered guard
therefore refuses to call the intrusion reduction mitigation, in every model.

The guard is doing its job, but the honest reading is narrower than "state
scaffolding damages the task". The scaffold's step 2 asks the model to *state
which text lies outside the information set and must not affect the answer* —
and it was applied unchanged to the **licensed** frame, where nothing lies
outside. In that frame the instruction is ill-posed, and the models appear to
respond by discounting the packet anyway. The responsiveness collapse is
therefore confounded with our own prompt being incoherent in the control frame.

What the round does **not** establish, and what a corrected version would need:
a licensed-frame scaffold whose step 2 is well-posed (naming that nothing is out
of set), so that the utility guard measures the scaffold's cost rather than its
incoherence.

## 3. What survives

`D = I_cot − I_state` is positive in all three models — 13.25 [5.62, 21.38],
10.98 [8.22, 13.84], 8.22 [6.07, 10.37] — so the state scaffold reduces
intrusion well beyond free-form deliberation wherever both were measured. Under
the frozen rule that is `state_specific_benefit` in each model taken alone. It
is **not** claimed as the panel result, because the arms it is computed from
failed qualification in most cells and because §2 shows the scaffold buys part
of that reduction by suppressing evidence use in general.

Free-form `cot` is not a fix: it reduces intrusion by 3.8 and 4.7 points in two
models and **increases** it by 7.7 in Mistral.

## 4. Consequence for the paper

G5 cannot be reported as a mitigation result. Its usable content is:

- deliberation as ordinarily elicited does not fix hindsight contamination, and
  makes it worse in one model;
- a scaffold that forces ex-ante state construction moves the number a long way,
  but not without cost, and this round cannot separate that cost from a flaw in
  how the scaffold was written for the control frame;
- the prompt-level mitigation baseline the method section needs is therefore
  still **G10's worked examples**, not this round.

The round is reported with its failures rather than trimmed to the two cells
that qualified.
