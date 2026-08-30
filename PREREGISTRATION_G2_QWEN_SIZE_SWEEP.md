# G2 secondary preregistration — Qwen3.5 within-family size sweep

**Created:** 2026-08-31
**Status:** design frozen before any output from any new checkpoint. Tag
`g2-qwen-size-sweep-design-v1`. Priority **P2**: below the positional
replication (P0) and explicit-verdict redaction (P1) in
`PREREGISTRATION_G2_HINDSIGHT_DEPTH.md`. It widens the model axis; it does not
answer the causal questions those two experiments answer.

## Question

> Does hindsight contamination disappear with scale, within one model family?

Not "does a bigger model also fail" — that framing invites a model zoo. All
sizes are declared **now**, together, so no size can be added or omitted after
seeing a result.

## Design

One family, four dense sizes, one frozen dataset:

| tag | checkpoint | status |
|---|---|---|
| `qwen35-2b` | `Qwen/Qwen3.5-2B` | **new** — no local snapshot yet (see below) |
| `qwen35-4b` | `Qwen/Qwen3.5-4B`, revision `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a` | new |
| `qwen35-9b` | `Qwen/Qwen3.5-9B`, revision `c202236235762e1c871ad0ccb60c8ee5ba337b9a` | **existing result, not re-run** |
| `qwen35-27b` | `Qwen/Qwen3.5-27B`, revision `fc05daec18b0a78c049392ed2e771dde82bdf654` | new |

Every size runs the **frozen 256-unit large-replication artifact**
(SHA-256 `0b6fd8d0304f6b7cde336a6518b1058983a9b93529e90cbb577d1878acf0901d`)
through the unchanged `src/run_information_set.py`: same four cells, same two
boundary probes, same system prompt, greedy decoding at temperature 0, seed 0,
8 max tokens, `max_model_len` 8192, same strict parser, same qualification
thresholds (`992/1024`, `448/512`, responsiveness ≥ 15, aligned `ALLOWED_WITH`
≥ 70), same estimator (95% percentile cluster bootstrap, 10,000 resamples,
seed `20260829`). **Not one word of prompt or one threshold changes.** No new
human review is required, because no new data is collected.

9B is not re-run: its large-replication output already exists under the freeze
tag, and re-running it would add sampling noise to a frozen result rather than
information.

### Availability disclosure, written before any run

`Qwen3.5-2B` has no local snapshot and this environment is offline. If it
cannot be obtained, the sweep is reported as **4B / 9B / 27B**, and this
paragraph — written before any new checkpoint produced output — is the record
that the omission is a checkpoint-availability constraint, not a choice made
after seeing results. `scripts/stage_qwen_sweep_models.sh` prints the exact
revision hash it stages for each size; any size whose revision is not pinned in
the table above must have its hash recorded in the results write-up before
analysis.

## Reported quantities

Per size `s`, on the same 256 questions:

```text
I_s = OutOfSetIntrusion      R_s = Responsiveness      B_s = boundary-probe accuracy
```

each with its 95% CI, plus decision parse rate, aligned `ALLOWED_WITH`,
qualification, and whether `CI_lower(I_s) > 5`.

Because every size answers the *same* questions, sizes are paired unit by unit.
Secondary, and reported for every pair regardless of outcome:

```text
Delta = I_larger - I_smaller       (adjacent sizes, plus the extreme pair)
```

with a paired bootstrap CI on the shared units. No multiplicity adjustment is
claimed and every contrast is shown.

## The plot that matters

Two panels against `log10(parameters)`: boundary-probe accuracy (recognition)
and `OutOfSetIntrusion` (enforcement). The scientifically interesting shape is
a **dissociation** — recognition already saturated at the small end while
enforcement keeps moving — because two capacities with different trajectories
is direct evidence that recognition and enforcement are not the same capacity.

## Analysis discipline, fixed now

With four size points (three if 2B is unavailable) we will **not** fit a
scaling law, report a slope, or quote a rank correlation. The analysis is
descriptive: per-size estimates with intervals, paired adjacent contrasts,
monotonicity stated as an observation, and the two-panel trend. The write-up
calls this a *within-family size trend*, never a scaling law.

## Interpretation table, fixed in advance

| observed | claim licensed |
|---|---|
| 27B intrusion stays high (roughly 13–18) | the recognition–enforcement gap is not a small-model limitation |
| intrusion falls but `CI_lower` still > 5 | scale attenuates but does not eliminate hindsight contamination |
| 27B intrusion collapses toward 0 while boundary accuracy stays near ceiling at every size | temporal *enforcement* improves with scale although temporal *recognition* is already saturated — the cleanest possible dissociation |
| non-monotone or noisy | reported as a non-monotone within-family trend; no story is fitted to four points |

Every one of these is publishable; none of them is a reason to add or drop a
size afterwards.

## Order of operations

1. this document + analyzer + run scripts → **tag `g2-qwen-size-sweep-design-v1`**;
2. `scripts/stage_qwen_sweep_models.sh`, recording each staged revision hash;
3. `scripts/run_qwen_size_sweep.sh` (9B excluded by construction);
4. `src/analyze_size_sweep.py` with the frozen artifact SHA-256, over all
   available sizes including the reused 9B output.

## Freeze checklist

- [x] family, sizes, and checkpoints declared together before any new output
- [x] frozen 256-unit artifact, unchanged prompts, decoding, parser, thresholds
- [x] 9B result reused rather than re-run, stated explicitly
- [x] paired size contrasts specified; no scaling law, slope, or correlation
- [x] 2B availability constraint disclosed in advance
- [ ] checkpoints staged with revision hashes recorded
- [ ] runs executed and analyzed
