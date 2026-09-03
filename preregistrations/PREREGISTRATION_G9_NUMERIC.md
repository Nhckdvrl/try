# G9 preregistration — A second task type: numeric pastcasting

**Created:** 2026-09-01
**Status:** design frozen. Tags `g9-numeric-design-v1` (this document, adapter,
freeze script, analyzer, tests) and `g9-numeric-freeze-v1` (the frozen item
artifact), both before any target-model output exists for this track.

---

## 1. The sub-question

Sub-question of `PAPER_FRAME.md` §1:

> Is hindsight contamination a property of *reconstructing a past judgment*, or
> a property of the probability-of-YES readout we happen to have measured it
> with?

Every number in the project so far comes from one task type: a binary
forecasting question answered as `P(YES)`. A reviewer is entitled to ask
whether the effect follows the *scientific object* or the *instrument*. BTF-3
ships a second track — 392 numeric questions asking for a quantity — with the
same pastcasting protocol, the same provenance, and the same kind of
post-cutoff resolution explanation.

This round is a **replication in a different task type**, not a new phenomenon
hunt. Its value is entirely in whether it reproduces.

## 2. The transformation, and the one thing it adds

Each numeric question is turned into a threshold question by a frozen rule:

```text
Will the resolved value be strictly less than <cutpoint_3> <units>?
```

`cutpoint_3` is **the source's own middle cutpoint**, chosen by the dataset's
authors. Nothing about the choice consults a model, a resolution, or an anchor.
The source's `question` text is carried verbatim under a `QUANTITY BEING
MEASURED` header and its `resolution_criteria` verbatim under the usual header,
so the threshold sentence is the only text this transform adds.

Everything downstream is inherited byte-identically from the binary track: the
four cells, the boundary probe, the system prompt, greedy decoding at
temperature 0 with `max_tokens` 8, both parsers, `s = 2r − 1` with `r = 1` when
the resolved value is below the cutpoint, and the 95% percentile cluster
bootstrap over `question_id` at seed `20260829`.

### Source filtering, defined before selection

Of 392 numeric rows, **347** pass source validation. The only substantive
exclusion is **45 rows whose resolved value sits exactly on `cutpoint_3`**,
where "strictly less than" is a knife-edge; they are dropped rather than
resolved by convention. `338` of the 347 also carry the anchor field.

## 3. Item selection, frozen

**128 units: 64 with the resolved value below the cutpoint, 64 above**, drawn
from the 347 valid rows that also have a non-null `sota_forecast_cdf_3`, by a
seeded deterministic shuffle (seed `20260901`) within each stratum. The
artifact's SHA-256 is recorded in the freeze report before any run.

Selection uses only source fields. No target-model output participates, and no
unit is added, dropped, or swapped after any model has seen the artifact.

## 4. Review provenance — stated plainly, not buried

The binary 256-unit artifact received a per-item human review (LLM-assisted,
without external lookup) plus a completed factuality audit against real
citations on a hash-fixed 64-item subsample: 63 PASS, 1 material error, 0
unverifiable.

**This round does not have that.** Its review consists of:

- the automated source validator (every required field present and non-empty,
  cutoff-encoding invariant, present-date ordering, no knife-edge resolutions);
- `validate_candidate_against_source`, which regenerates all four prompts from
  the pinned source row and fails on any drift, plus the packet-leak checks —
  run on **all 347** candidates, all passing;
- a **32-item spot audit** on the frozen 128, sampled by a recorded seed, using
  the same protocol as `PROTOCOL_BTF3_PACKET_FACTUALITY_AUDIT.md`.

The paper reports this round as a **replication in a second task type with
lighter review provenance than the primary round**, and says so wherever it
appears. It is not presented as an independently reviewed benchmark.

## 5. Estimands and gates — inherited, not restated

Per model: `Responsiveness`, `OutOfSetIntrusion`, boundary-probe accuracy, and
decision parse rate, computed by the same analyzer as the large replication.

Qualification, scaled to 128 units at the same rates as the primary round:
parse rate ≥ 96.875% (`496/512`), boundary-probe accuracy ≥ 87.5% (`224/256`),
mean responsiveness ≥ 15.0, mean aligned `ALLOWED_WITH` ≥ 70.0.

**Replication gate, fixed now:** the round replicates if at least **2 of 3**
qualified models have `OutOfSetIntrusion` with a 95% CI lower bound strictly
above the 5.0-point SESOI — the same `intrusion_pass` rule as every earlier
round.

Models: `qwen35-9b`, `gemma3-12b`, `mistral-small-24b`. Volume: 3 × 128 × 4
decisions + 3 × 128 × 2 probes = **2,304 generations**.

## 6. Secondary, and predicted now

The anchor `sota_forecast_cdf_3` is by construction the SOTA forecaster's
`P(value < cutpoint_3)` — the *exact* quantity the model is asked for, which
the binary track's anchor was only indirectly. The G7 analysis is therefore
re-run here without modification.

Recorded prediction, given G7's outcome on the binary track: `rho_without` will
again be **low** (the models are weak pastcasters), and `Δ_dev` will again be
**negative**. If either comes out differently on the numeric track, that
difference is itself reportable and the binary-track G7 write-up is amended to
say so.

## 7. Interpretation, fixed in advance

| outcome | permitted conclusion |
|---|---|
| gate met | The effect follows the scientific object, not the readout: the same recognition–enforcement dissociation appears in a different task type on independently drawn source rows. |
| gate not met, models qualified | The effect is **specific to the binary probability-of-YES task** as instantiated here. That is a substantial limitation and the paper's scope narrows to it explicitly. |
| models unqualified | The instrument does not transfer to this task type. Reported as an instrument limit; no claim either way about the phenomenon. |

## 8. What this does not do

- It is **not** a second natural family. The boundary is still temporal and the
  source is still BTF-3. It varies the task type and the item pool, nothing else.
- It does not re-open, re-review, or re-select anything in the binary round.
- It does not run the G3, G5, G6, or G8 manipulations on this track. If the
  gate is met, extending one of them is a separate preregistration.

## 9. Freeze checklist

- [x] `PREREGISTRATION_G9_NUMERIC.md` committed
- [x] `src/adapters/btf3_numeric.py` committed
- [x] `scripts/freeze_btf3_numeric.py` committed
- [x] `tests/test_btf3_numeric.py` committed and passing
- [x] no new analyzer: `src/analyze_btf3_large_replication.py` is reused verbatim with
      `--expected-artifact-sha256 cb0c925ade9b76eee71f9a6f9dc695da44fb717510e15a5156e6416967ef6b15`
- [x] frozen artifact built; SHA-256 `cb0c925ade9b76eee71f9a6f9dc695da44fb717510e15a5156e6416967ef6b15`
- [ ] `g9-numeric-design-v1` and `g9-numeric-freeze-v1` tagged
- [ ] first generation only after both tags exist
