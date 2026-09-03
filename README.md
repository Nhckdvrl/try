# Advance commitment to ignore evidence

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

A policy almost always exists before the data it governs: a system prompt forbids a
source before retrieval runs, a court excludes evidence before the record is read
out, an agent is told which memories are off-limits before any is fetched.

We preregistered the human pattern — that an instruction to disregard arriving
*after* the evidence is the hard case — and found the reverse. Across twelve
instruction-tuned models from four vendors, two masked diffusion language models and
five task families, exclusion stated **after** the evidence is followed well, while
the identical instruction stated **before** it leaves up to 0.64 of the evidence's
normal causal weight in the decision — even though every model, asked separately,
states the required weight as exactly zero on 100% of items.

What decides it is not memory, distance, the attention mask or the wording. It is
what the policy can bind to.

**Start here:** [`STATUS.md`](STATUS.md) — consolidated snapshot of the main line,
the evidence behind each claim, and what is explicitly not claimed.

## Read these first

1. [`PAPER_FRAME.md`](PAPER_FRAME.md) — the authoritative scientific story.
2. [`PAPER_OUTLINE.md`](PAPER_OUTLINE.md) — narrative, sections and figures.
3. [`EXPERIMENTS.md`](EXPERIMENTS.md) — registry of every round and its role.
4. [`ACL_EMNLP_ALIGNMENT_STANDARD.md`](ACL_EMNLP_ALIGNMENT_STANDARD.md) — the bar.
5. [`RELATED_WORK_2026.md`](RELATED_WORK_2026.md) — neighbours and positioning.
6. [`RESEARCH_HISTORY.md`](RESEARCH_HISTORY.md) — how the question moved, and why it
   moved back.

## Results

- [`PROSPECTIVE_EXCLUSION_FINDINGS.md`](PROSPECTIVE_EXCLUSION_FINDINGS.md) — the G0
  headline, the model panel, the mechanism.
- [`stages/`](stages/) — the controlled stages that say what the failure is.
- `results/` — machine-readable analyses and tables; `results/mech/` for
  interventions; `results/raw/` for raw generations.

## Status, 2026-09-03

**Main line.** Prospective evidence exclusion. The behavioural programme and the
mechanism are complete. G16, the one planned experiment, was frozen, run, and
**stopped at its preregistered bridge gate** — see
[`results/mech/g16_binding_interchange_results.md`](results/mech/g16_binding_interchange_results.md).
It cost the paper the single-item form of the class-marker claim, which now rests on
the tagged-stream result instead. No successor is scheduled.

**Stopped branch.** The BTF-3 hindsight paper was stopped. Its data, results and
preregistrations are retained; see `RESEARCH_HISTORY.md` §5 for why and
`EXPERIMENTS.md` §C for what is where. The preregistered G4 breadth panel will not
be completed — finishing a preregistration for a stopped branch is bookkeeping, not
science.

**Second lead.**
[`SECOND_LEAD_EXPLICIT_OUTCOME_PARADOX.md`](SECOND_LEAD_EXPLICIT_OUTCOME_PARADOX.md)
— removing an explicit outcome statement makes later evidence *more* influential,
in all three models tested. Held for one clean prospective test; not part of the
current paper.

**Corrections on the record.**
[`preregistrations/POSTHOC_REDACTION_AUDIT_CORRECTION.md`](preregistrations/POSTHOC_REDACTION_AUDIT_CORRECTION.md)
— the verdict redactor's conditional-marker bypass leaves 34/256 packets asserting
the outcome and the frozen audit could not detect it; and the Llama boundary-probe
figure was reported at single-frame scope. Neither changes a preregistered verdict;
both are disclosed rather than repaired in place.

## Reproduction

See [`REPRODUCE.md`](REPRODUCE.md). Frozen items are in `data/items/frozen_v1.json`;
every round names its freeze commit or tag, and Git tags remain the authority for
chronology relative to model outputs.
