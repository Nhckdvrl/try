# Research history — how the question moved, and why it moved back

This file preserves **why the question changed**, including the part where we
changed it away from a good result and later changed it back. It is not the paper
narrative and does not replace the original preregistrations in
[`preregistrations/`](preregistrations/).

## 1. Starting question — advance exclusion

The project began from the human literature on inadmissible evidence: a
meta-analysis over 48 studies and 8,474 participants finds that people told to
disregard evidence they have already heard retain its influence.

G0 preregistered the same ordering for models: exclusion **after** the evidence
would be the hard case.

**The result reversed.** Across twelve instruct models from four vendors, exclusion
after the evidence was followed well; the identical rule stated *before* it was
not. `Δ_time` was negative in all twelve models.

Two things made the reversal a finding rather than a failure. Models state the
policy perfectly — 100% "exactly zero" on the separate probe, in both arms — and
still route the evidence into the decision. And the asymmetry survives in
bidirectional masked diffusion models, so it is not the causal attention mask.

## 2. The controlled programme that followed

Stages 2–5 did not add controls to defend the reversal; they tried to say what it
was. In order:

- **distance** — no main effect; within the prospective arm, more distance helps;
- **directional anaphora** — stripping every `preceding`/`following` referent
  shrinks the effect but leaves it significant in 3 of 4 models;
- **requested weight** — the asymmetry exists only at exactly zero, pooled
  discontinuity **+0.295 [+0.185, +0.405]**;
- **an arithmetically implementable task** — the discontinuity disappears entirely,
  which bounds the claim;
- **inclusion implicature** — explicitly denying that display implies relevance
  rescues no model;
- **the announcement ladder** — naming a future item makes suppression *worse* than
  never mentioning it, uniformly across six models;
- **semantic addressability** — the rule binds to propositional content, graded by
  entailment, not by lexical overlap;
- **a duplicate control** — which found a real confound in the previous step, and
  forced the metric from REI to raw rating points;
- **class/tag policies** — a marker travelling with the evidence takes stream
  leakage from 0.48 to ≈0 in both arms;
- **an agent setting** — the same dissociation with real `SYSTEM`/`TOOL` roles;
- **mechanism** — span gating, late answer-position patching, and matched-chronology
  bidirectional interchange, including a correction that withdrew an earlier
  overstated recovery-fraction analysis.

At this point the line had a natural question, a reversed prediction, five
discriminating explanations, a working structural fix, and a mechanism.

## 3. Why we left it anyway

The concern was that the work was tied to a synthetic prompt grammar — "a future
item receives weight zero" — and that the materials were authored vignettes rather
than natural text. That concern was real, but the response was too large: instead
of naturalising the materials, the project changed the question.

## 4. The detour — Information-Set Reasoning, then hindsight

The question was generalised to "can a model reason using only the information that
belongs to a specified situation." Several boundary families were tried. The
temporal BTF-3 branch qualified; the FANToM perspective branch did not; a later
FOMC source attempt failed its gate.

The surviving temporal branch was reframed as **hindsight**: given a resolved
forecasting question and its resolution packet, can the model still judge the
earlier situation? That produced a real programme — an 8-item discovery, a 64-item
prospective confirmation, a 256-item fresh replication, foreign-packet and
verdict-redaction decompositions, a paired outcome-direction intervention, and a
three-round mechanistic sequence ending in a fresh preregistered confirmation.

## 5. Why the hindsight paper was stopped on 2026-09-03

Reviewed against the reference papers and the 2025–2026 literature, the branch had
three problems that were not fixable by rewriting:

1. **The instrument stopped matching the question.** The prompts are explicit
   information-set contracts — `TARGET INFORMATION SET`, `LATER RESOLUTION PACKET`,
   `date_cutoff_end=…` — and the boundary probe's answer is stated verbatim in the
   prompt it probes. What is measured is compliance with an engineered exclusion
   contract, not hindsight.
2. **The headline was covered.** ExAnte and the temporal-leakage line already
   establish that models violate stated cutoffs; work on auxiliary-information bias
   and on prompting models to ignore biasing information already reports failure and
   backfire. The genuinely new material sat in the middle of the paper.
3. **The panel narrowed under its results.** The original Qwen/Gemma/Mistral G12
   verdict is `indeterminate`; Llama was added afterwards and the three
   largest-effect models were labelled canonical in the same commit that added the
   Llama numbers, with the one model that fully passes the recognition check moved
   to an appendix. That is exactly the failure mode this project set out to avoid.

Two data-integrity defects were found in the same review and are corrected in
[`preregistrations/POSTHOC_REDACTION_AUDIT_CORRECTION.md`](preregistrations/POSTHOC_REDACTION_AUDIT_CORRECTION.md):
the redactor's conditional-marker bypass leaves 34/256 packets asserting the
outcome, and the frozen audit could not detect it because it used the same
heuristic; and the Llama boundary-probe figure was reported at single-frame scope
alongside other models' two-frame scope. Neither changes a preregistered verdict,
and both are now on the record.

## 6. What the detour produced that survives

- **One strong unconfirmed discovery.** Removing the explicit verdict sentence
  makes contamination *larger*, in all three models, without reducing the packet's
  evidential value. It is preserved as a separate lead in
  [`SECOND_LEAD_EXPLICIT_OUTCOME_PARADOX.md`](SECOND_LEAD_EXPLICIT_OUTCOME_PARADOX.md)
  with the single clean experiment that would confirm or kill it.
- **A methodological lesson that transfers.** The `outcome_evaluation` family in the
  original G0 items is the one family with order-*independent* residue — ordinary
  outcome bias, behaving like the human effect rather than like the positional one.
  The hindsight branch was, in retrospect, an eighteen-round expansion of that one
  family.
- **Provenance discipline.** Freeze tags, artifact hashes, human review gates and
  post-result corrections that the main line now inherits.

## 7. Current paper

The project has returned to the question it started with, without the human
analogy in the title and without the original prediction:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

```text
advance exclusion fails where post-hoc exclusion succeeds,
while the model states the policy perfectly
        ↓
not memory, distance, causal masking, wording, or implicature
        ↓
the failure is specific to complete suppression
        ↓
what the policy can bind to decides it — content and
evidence-carried class markers work, named future items do not
        ↓
the same dissociation in an agent
        ↓
excluded evidence is still read at the decision; gating is late
and the binding state is causally exchangeable
```

The history explains how we found this, lost it, and came back. It should not
dictate the structure of the paper.
