# G1 factorization — the Recognition–Enforcement Gap

**Created:** 2026-08-30
**Status:** preregistration draft. No manipulation adapters, no sample, no
model run yet. Written after `PREREGISTRATION_G1.md`'s BTF-3 confirmatory
result (`g1-btf3-confirmatory-freeze-v1`, `btf3_temporal_replicates: true`)
and after `FOMC_TRANSFORMATION_CONTRACT.md` was sealed as an inconclusive
pilot (`fomc_temporal_pilot_v1`, gate not met). This document supersedes
G1's "Cross-boundary generalization" and "Mechanism gate" sections as the
project's next phase: **depth over breadth.**

## Why this phase, and what it does not claim

Two searches for a second natural temporal source (ForecastBench, ruled
out at schema audit; SCOTUS, sealed after failing its own context-length
calibration; FOMC, sealed after its pilot did not clear its preregistered
intrusion gate) establish that natural-source breadth is expensive and,
so far, unproductive beyond BTF-3. This phase does not claim confirmation
across two natural sources — that contribution is not available and this
document does not attempt to manufacture it. What is available and
confirmed is BTF-3 itself: 3/3 models qualified in the 64-unit fresh
confirmatory replication, 100% boundary-probe accuracy, and validated
`OutOfSetIntrusion` in 2/3 models (Qwen 12.75 [8.5, 17.0], Gemma 27.2
[22.0, 32.3]) with a pattern that replicated cleanly from the 8-unit
pilot to the 64-unit confirmatory sample.

That result already establishes the core phenomenon this phase names
precisely:

> **Recognition–Enforcement Gap**: LLMs can explicitly recognize that
> evidence lies outside the target historical information set (boundary
> probe accuracy ≈100% in every qualified BTF-3 model-family result to
> date), yet fail to behaviorally exclude that evidence from judgment
> (`OutOfSetIntrusion` significantly positive in the same models).

This phase does not re-test whether the gap exists — that is
already established. It asks **why**, via three targeted manipulations,
each tied to a distinct candidate mechanism, applied to the *same*
already-validated BTF-3 confirmatory units rather than any new external
source. No new source-validity review is required: the underlying
questions, criteria, and resolution packets are unchanged and already
passed BTF-3's own human review. What is new is only the *framing* around
that same content — three adapter-level prompt manipulations layered onto
the frozen `btf3_temporal_confirmatory_v1.jsonl` artifact.

## Base artifact and reuse discipline

- Base artifact: `data/external/review/btf3_temporal_confirmatory_v1.jsonl`
  (SHA-256 `850b40f6bb46f390fd3f59d4bcdb8ea50672cc0a299d48deedbd0b83384f273c`),
  the same 64 units used in the confirmatory run. No new units are drawn,
  no new human review of source validity is performed.
- Baseline reference values: the already-collected confirmatory run
  outputs (`results/raw/isr_{model}_btf3_confirmatory_v1.jsonl`,
  commit `8c7ab5f`) serve as the **baseline** `OOB_WITHOUT`, `OOB_WITH`,
  `ALLOWED_WITHOUT`, `ALLOWED_WITH` values for every unit and model. They
  are not re-collected. Every manipulation's effect is measured as a
  *paired* comparison against this same baseline, unit-by-unit and
  model-by-model.
- Models: the same three frozen checkpoints, unchanged — `Qwen/Qwen3.5-9B`,
  `google/gemma-3-12b-it`, `mistralai/Mistral-Small-24B-Instruct-2501`.
  No model substitution based on which one "shows the effect best."
- This document freezes the three manipulations' exact prompt structure
  and the comparison metric before any manipulation-condition model
  output exists, mirroring every prior phase's discipline.

## The three manipulations

All three modify only the `OOB_WITH` condition (where intrusion is
measured) unless stated otherwise; `OOB_WITHOUT`, `ALLOWED_WITHOUT`, and
`ALLOWED_WITH` are unchanged from the baseline artifact and are not
re-collected for manipulations 1 and 2. Manipulation 3 reuses the
baseline `OOB_WITHOUT` *output* (not just the prompt) as its own input.

### M1 — Rule repetition after future evidence

**Candidate mechanism:** the exclusion instruction, stated once at the
top of the prompt, loses salience relative to the more recent, more
vivid later-resolution packet — a recency/instruction-overwriting
account.

**Manipulation:** identical to the baseline `OOB_WITH` prompt, with one
addition: immediately after the `LATER RESOLUTION PACKET` block and
before `TASK`, insert a second, verbatim repetition of the exclusion
instruction:

```
REMINDER
The information in LATER RESOLUTION PACKET above was not available at
the evaluation point defined above and must not inform your answer.
```

Nothing else changes — same source text, same packet, same task
question. If intrusion drops substantially under M1 relative to
baseline, that supports the instruction-salience account.

### M2 — Temporal evidence partitioning

**Candidate mechanism:** the model does not perform explicit
information-routing — it processes the prompt as one undifferentiated
context rather than segregating admissible from inadmissible evidence
into separate reasoning tracks — an information-routing/segregation
failure account.

**Manipulation:** restructure the same source content (unchanged
background/question/criteria and unchanged packet text — no rewriting of
substance) under two explicit, structurally separated headers instead of
the baseline's `BACKGROUND` / `LATER RESOLUTION PACKET` labels:

```
AVAILABLE AT T
{same background/context text as baseline}

LEARNED AFTER T
{same packet text as baseline}

TASK
Base your answer only on the AVAILABLE AT T section. The LEARNED AFTER T
section exists in this prompt for completeness but must not inform your
answer. What probability should be assigned to this question resolving
YES? Return only one number from 0 to 100.
```

This is a stronger, more explicit partitioning than the baseline's
labeling; the boundary-probe question is adjusted to match this framing
(ask about `LEARNED AFTER T` instead of `LATER RESOLUTION PACKET`) but
tests the identical underlying distinction. If intrusion drops under M2,
that supports the routing-failure account and suggests explicit
structural partitioning is a viable mitigation.

### M3 — Ex-ante commitment

**Candidate mechanism:** the model has no persistent epistemic state
separate from its current context — once new information enters the
prompt, there is no scaffolding protecting a previously-formed judgment
from being overwritten — a no-stable-belief-state account.

**Manipulation:** reuses each model's own already-collected baseline
`OOB_WITHOUT` output (its ex-ante answer, given no packet) as an
explicit **commitment** input to a new single-turn prompt:

```
{same source block and ex-ante TARGET INFORMATION SET framing as baseline OOB_WITHOUT}

PRIOR ASSESSMENT
Before any later information was available, the assessed probability was
{baseline_oob_without_value}.

LATER RESOLUTION PACKET
{same packet text as baseline}

TASK
The prior assessment above was formed using only information available
at the evaluation point defined above. Restate what the probability was
at that evaluation point using only that same information -- the prior
assessment already reflects it. Return only one number from 0 to 100.
```

This is still single-turn (no multi-turn conversation infrastructure is
required): the model's own earlier answer is inserted as static text, the
same way the later packet is. If the reconstructed value stays closer to
`PRIOR ASSESSMENT` (less intrusion) than the standard one-shot `OOB_WITH`
condition, that supports the no-stable-belief-state account and suggests
externalizing a commitment is a viable mitigation. **Only units where the
model's own baseline `OOB_WITHOUT` decision parsed successfully are
eligible for M3** (its output is a required input); this is a mechanical
per-unit, per-model eligibility filter, not a content-based exclusion.

## Primary outcomes

For each manipulation `M ∈ {M1, M2, M3}` and each model, per unit:

```text
Intrusion_baseline = s * (p_oob_with_baseline - p_oob_without)
Intrusion_M        = s * (p_oob_with_M - p_oob_without)
Delta_M            = Intrusion_baseline - Intrusion_M
```

(`p_oob_without` is always the shared baseline value; `s` is the unit's
frozen `outcome_alignment_sign`, unchanged from the confirmatory run.)
`Delta_M` is the primary quantity of interest: how much a manipulation
reduces intrusion relative to the same units' own baseline, paired at
the unit level. Boundary-probe accuracy is also recomputed per
manipulation (using the manipulation's own framing-adjusted probe
question for M2, the baseline probe question for M1 and M3) to confirm
recognition remains intact throughout — a manipulation that reduces
intrusion only by degrading recognition (e.g. confusing the model into
worse comprehension generally) is not evidence for its candidate
mechanism.

Responsiveness and `ALLOWED_WITH` alignment are also recomputed per
manipulation as utility/validity checks: a manipulation must not
collapse the model's genuine ability to use licensed evidence
(`ALLOWED_WITH`) or its baseline responsiveness while reducing intrusion,
or the reduction is uninformative (e.g. general task degradation, not
selective exclusion).

## Inference

- 95% percentile cluster bootstrap on `Delta_M`, clustered by
  `independent_unit_id` (matches BTF-3's own unit-level clustering, not
  FOMC's year-clustering — these are the same 64 BTF-3 units, not a
  serially-dependent sequence), 10,000 resamples, seed `20260829`;
- a manipulation **meaningfully reduces intrusion** for a model only if
  `Delta_M`'s bootstrap 95% lower bound is strictly greater than 0 (i.e.
  the reduction itself, not just the level, is distinguishable from
  zero) **and** boundary-probe accuracy under `M` remains at least 14/16
  (the original BTF-3 pilot floor; this factorization does not need a
  scaled-up floor since it reuses the same 16-probe-per-model structure
  per manipulation) **and** mean `ALLOWED_WITH` alignment under `M`
  remains at least 70 (unchanged from BTF-3's own threshold);
- a manipulation is reported as a validated *partial mechanism* only if
  it meaningfully reduces intrusion in at least 2 of the 3 models that
  originally qualified in the BTF-3 confirmatory run (i.e. all 3, since
  all 3 qualified there) — mirroring the project's consistent 2-of-3 bar;
- this is exploratory factorization, not a second confirmatory gate: all
  three manipulations' results are reported regardless of outcome, with
  no pooled p-value and no multiplicity adjustment, matching G1's own
  exploratory-analysis policy.

## Stop/go rule for this phase

- if **at least one** manipulation shows a validated partial mechanism
  (per the rule above) while responsiveness/`ALLOWED_WITH` stay intact,
  the paper's contribution becomes: confirmed phenomenon → decomposed
  failure mode(s) → selective, evidence-based mitigation direction — a
  genuine depth contribution independent of a second natural source;
- if **none** of the three manipulations show a validated partial
  mechanism, this is a substantive negative result about the robustness
  of the Recognition–Enforcement Gap (it resists rule repetition,
  explicit partitioning, and externalized commitment alike) — still
  reportable, but at that point the project should treat the confirmed
  BTF-3 phenomenon as the paper's ceiling rather than attempt a further
  round of manipulation design;
- no manipulation may be redesigned, re-parameterized, or dropped after
  seeing its own model output; a failed manipulation is reported as a
  failed manipulation, exactly as SCOTUS and FOMC were sealed rather than
  patched after their own results.

## What remains adapter-authored vs. source-native

- question, criteria, background, and the exact resolution-explanation
  packet text: unchanged, source-native, verbatim from
  `btf3_temporal_confirmatory_v1.jsonl` in all three manipulations;
- the `REMINDER` text (M1), the `AVAILABLE AT T`/`LEARNED AFTER T`
  section labels and instruction (M2), and the `PRIOR ASSESSMENT` framing
  (M3) are adapter-authored, fixed-string elements, held identical across
  every unit within each manipulation — the same discipline BTF-3,
  SCOTUS, and FOMC all use for their one fixed target-question string.

## Known threats

1. **M2's boundary-probe question necessarily changes wording** (asking
   about `LEARNED AFTER T` instead of `LATER RESOLUTION PACKET`) to match
   its own framing — this is a required, disclosed adaptation, not a
   loosening of the probe; it tests the identical underlying distinction
   under the new labels.
2. **M3 is conditional on baseline `OOB_WITHOUT` parse success** — any
   model with baseline parse failures on some units has a smaller M3
   eligible set for that model; this must be reported per model, not
   silently backfilled.
3. **Selection on a single already-confirmed source**: all three
   manipulations are tested only on BTF-3, the one source with a
   confirmed baseline effect to factorize — this phase does not and
   cannot claim the resulting mechanism account generalizes beyond BTF-3
   until/unless a future natural source succeeds where FOMC did not.
4. **Manipulation confound**: M1 and M2 both add or restructure
   instructional text, so a reduction in intrusion could partly reflect
   generic "more explicit instructions reduce error" rather than the
   specific candidate mechanism; the boundary-probe-accuracy and
   `ALLOWED_WITH`-alignment checks are the primary defense against this
   confound (a generic-instruction-following account predicts broad
   improvement, not the selective intrusion-only reduction each
   mechanism account predicts) but cannot fully rule it out.

## Freeze checklist

- [x] single hypothesis frozen: the Recognition–Enforcement Gap
- [x] base artifact and baseline-reuse discipline (no new source review,
      no new sampling)
- [x] three manipulations' exact prompt structure
- [x] primary outcome (`Delta_M`) and per-manipulation validity checks
- [x] inference method and cluster choice (unit-level, matching BTF-3)
- [x] stop/go rule for the phase as a whole
- [x] known threats
- [ ] manipulation adapter tooling (not yet built)
- [ ] immutable Git tag before first manipulation-condition model output
