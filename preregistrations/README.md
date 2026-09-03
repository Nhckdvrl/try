# Original preregistrations

This folder contains the **original experiment preregistration documents**, moved here
without rewriting their historical contents.

Use [`../EXPERIMENTS.md`](../EXPERIMENTS.md) for the compact scientific overview. Come
here when you need the exact frozen design: hypotheses, estimands, thresholds,
qualification gates, sampling rules, planned analyses, or the chronology of a
particular round.

The files intentionally preserve the language used at the time each experiment was
designed. A later result may have overturned the motivating interpretation; that is
scientific history, not an inconsistency to edit away.

## Main paper line — advance evidence exclusion

- `PREREGISTRATION_G0.md` — the original advance-exclusion test whose prediction
  reversed. This is the main paper's headline round.
- `PREREGISTRATION_G16_BINDING_INTERCHANGE.md` — **DRAFT, not frozen.** The one
  planned new experiment: does the identifier-bound / class-bound difference reduce to
  one causally exchangeable state? Authorises nothing until tagged
  `g16-binding-interchange-design-v1`.

The Stage 2–5 controlled rounds were designed in `RESEARCH_PLAN.md` and the stage
documents rather than as separate preregistration files; their frozen records are in
[`../stages/`](../stages/) and their tables in `../results/`.

## Stopped branch — BTF-3 hindsight

Retained for provenance. The branch was stopped on 2026-09-03; see
[`../RESEARCH_HISTORY.md`](../RESEARCH_HISTORY.md) §5.

- `PREREGISTRATION_BTF3_LARGE_REPLICATION.md`
- `PREREGISTRATION_G8_RELEVANCE.md`, `PREREGISTRATION_G11_REDACTED_SWAP.md`,
  `PREREGISTRATION_G12_DONOR_OUTCOME.md`
- `PREREGISTRATION_G13_SHARED_OUTCOME.md`, `PREREGISTRATION_G14_DECISION_STATE.md`,
  `PREREGISTRATION_G15_DECISION_CONFIRMATION.md`
- `PREREGISTRATION_G2_HINDSIGHT_DEPTH.md` — its Experiment B is the surviving second
  lead, `../SECOND_LEAD_EXPLICIT_OUTCOME_PARADOX.md`
- `PREREGISTRATION_G2_QWEN_SIZE_SWEEP.md`, `PREREGISTRATION_G3_EXCLUSION_REASON.md`,
  `PREREGISTRATION_G4_MODEL_BREADTH.md` (5 of 17 checkpoints run; **the remainder will
  not be run**)
- `PREREGISTRATION_LLAMA_BEHAVIORAL_EXTENSION.md`

## Earlier narrowing and failed rounds

- `PREREGISTRATION_G1.md`, `PREREGISTRATION_G1_FACTORIZATION.md`,
  `PREREGISTRATION_G1_FACTORIZATION_V2.md`
- `PREREGISTRATION_G5_DELIBERATION.md`, `PREREGISTRATION_G6_MECHANISM.md`,
  `PREREGISTRATION_G7_EXANTE_ANCHOR.md`, `PREREGISTRATION_G9_NUMERIC.md`,
  `PREREGISTRATION_G10_FEWSHOT.md`

## Post-result corrections

Explicitly labelled post-result. They change no frozen artifact, threshold, seed or
raw output.

- `POSTHOC_REDACTION_AUDIT_CORRECTION.md` — the verdict redactor's conditional-marker
  bypass leaves 34/256 packets asserting the outcome; the frozen audit shared the
  heuristic and could not detect it. Includes leak-free re-estimates and the Llama
  boundary-probe scope correction.
- `ANALYSIS_CORRECTION_G8_VALIDITY.md` — G8's assignment-leakage interpretation and
  the legacy `0.` parser bug.

Git freeze commits and tags remain the authority for when each preregistration became
immutable relative to model outputs.
