# Paper outline — draft against results in hand

**Created:** 2026-09-01. Updated after G5 and G8–G11. The paper now follows one
forward explanatory tree; defensive rounds are compressed or moved to the
appendix.

---

## Title

Recommended:

> **Can Language Models Unsee the Future? Retrospective Outcome Entrainment in
> Reconstructed Past Judgments**

Alternatives:

- *Recognized but Not Enforced: Hindsight Contamination in Reconstructed
  Past Judgments*
- *The Future Pulls the Past: Outcome Entrainment in Language Models*

The recommended title names the natural operation and the newly isolated
phenomenon; it names no dataset, metric, or method.

## Abstract (draft)

> A reasoner who has learned how something turned out is often asked what it
> was reasonable to believe before. We study whether language models can do
> this: reconstruct a judgment from the information available at a past moment
> while holding a piece of evidence that postdates that moment causally inert.
> On 256 independently sampled natural forecasting questions we manipulate,
> within item, the presence and admissibility of the same explicit post-cutoff
> evidence. Three open checkpoints identify per item, at 99.2–100% accuracy,
> that the evidence lies outside the target information set, and are
> nonetheless moved by it by 7.5 to 27.7 probability points. The effect
> survives mechanical removal of the explicit resolution verdict — indeed it
> grows. We then isolate a lower-level phenomenon. Replacing each question's
> future packet with the resolution packet of a different question still causes
> 50.7–100.1% as much absolute movement as the real packet and pulls judgments
> toward the donor question's outcome. Removing explicit verdict sentences
> preserves 67–74% of this donor pull in two of three models, yielding a
> preregistered panel result. We call this **retrospective outcome
> entrainment**: outcome-shaped later context enters reconstruction even when it
> is irrelevant to the judgment being reconstructed. The finding shifts the
> explanation from failure to state a temporal rule to failure to keep an
> irrelevant future outcome causally outside the reconstructed past.

## Sections

### 1. Introduction

Opens on the question, not the dataset. Concedes the nearest neighbour by name
in the second paragraph — *When Do LLMs Apply the Wrong Law?* (arXiv 2608.14610)
already owns the observation that models can state a temporal rule and violate
it — and states what is different here: a within-item causal manipulation of
one fixed piece of evidence, per-item measured recognition, and the
factorization of the boundary into licensing and reason.

### 2. Task and instrument

BTF-3 as a **measurement window**, explicitly not the contribution. Independent
semantic unit, the four cells, the boundary probe, the estimator. The
transformation contract and the 64-item factuality audit (63 PASS / 1 material
error / 0 unverifiable) go here, with the LLM-assisted-review caveat stated
rather than buried.

### 3. The phenomenon and its replication

8 discovery → 64 confirmatory → **256 entirely fresh** units passing the
preregistered gate 3/3, with cross-round intervals that all contain zero. The
recognition–enforcement table is the paper's first figure.

### 4. Depth and scope of the phenomenon

Report compactly, without making this the narrative spine:

- **not answer-copying** — verdict redaction (G2-B), effect survives and grows;
- **not a scale artefact** — 4B/9B/27B within one family, non-monotone,
  largest most contaminated;
- **not a property of three checkpoints** — the breadth panel (G4).

The breadth panel also separates two failures the paper had only ever seen
together: checkpoints that cannot reliably recognise the boundary (probe
56–74%) and checkpoints that recognise it at ceiling and are moved anyway. Only
the second is the dissociation, and the paper says so.

### 5. Stated reasons do not control the surviving influence (G3)

The section leads with the normalized effect, not the raw points: the evidence
moves a licensed retrospective judgment 39–47 points and an ex-ante judgment
7.5–27.7, so the instruction is doing something — and what G3 shows is that how
much it does is insensitive to why. The section states in the same paragraph
that the licensed frame also changes the target question and is a normalizer,
not a minimal pair. Gemma is the stated exception, in the same arms as its
amplification.

The licensing/reason factorization, the byte-identity audit, and the result:
**no stated reason is enforced**. The `unreliable` arm is the section's hinge —
a model that discounts evidence it is told may be fabricated would show it
here, and none does. The Gemma amplification is reported as unanticipated and
tied to the same direction as G2-B.

This is characterization, not the core explanation. No reason reduces
intrusion at panel level; Gemma's added clauses increase it. The section avoids
claiming the model believed an `unreliable` packet false.

### 6. Retrospective outcome entrainment (G8 + G11 — the core section)

G8 first orthogonalizes relevance and donor outcome. A foreign packet causes
50.7–100.1% as much absolute movement as a real packet. Donor pull is positive
with intervals above zero in all three models (2.93, 4.97, 12.26 points), while
the preregistered 5-point strong-form rule is met only by Gemma; report both the
frozen `H-presence-weak` row and the continuous estimates.

G11 then applies the already frozen verdict-redaction transform to the same
foreign packets. Qwen retains 73.9% and Gemma 67.1% of donor pull; Mistral is
verdict-dependent at 35.0%. The preregistered panel verdict is `survives`.

The conceptual result is positive: outcome-shaped future context entrains a
reconstructed past judgment even when the outcome belongs to a different
question and is expressed as evidence rather than an explicit verdict.

### 7. Boundaries and failed interventions

G5 is an instrument failure, G9 does not qualify as a second-task replication,
and G10 is heterogeneous. G7 shows weak uncontaminated pastcasting. These are
reported transparently but do not create main sections or motivate more
defensive experiments.

### 8. Mechanism boundary

No neural mechanism section is promised. The frozen G6 mask can localize direct
packet access but cannot determine whether an ex-ante state was constructed and
overridden or never constructed, because packet information can first move into
other token residuals. It is deferred until a causally identified internal
variable would advance the headline explanation.

### 10. Limitations

Written from the record, not composed at the end:

- **G7.** The models are weak pastcasters: their uncontaminated answers
  correlate only 0.28–0.33 with BTF-3's independent ex-ante forecast, and the
  preregistered displacement test failed in the opposite direction. The paper
  reports this and drops the claim it was meant to support.
- **One family of boundary.** Temporal, on one source. G3's `procedural` arm
  extends the claim to a non-temporal licensing reason *within* that substrate,
  which is not the same as a second natural family. FANToM failed
  qualification and the FOMC attempt failed its preregistered gate; both are
  reported as failures.
- **Review provenance.** The 256-unit review was LLM-assisted without external
  lookup; the audit that closes that gap covers a hash-fixed 64-item
  subsample.
- **G2 Experiment A** did not clear its own replication bar, and its
  specificity control pointed the other way. It is reported as a discovery-sample
  result, not as a mechanism.

## Figures and tables

1. The natural operation and causal 2×2 design; recognition beside intrusion on
   the 256-unit replication.
2. The explanatory sequence: own packet → foreign packet → verdict-redacted
   foreign packet, with own- and donor-direction estimands separated.
3. Per-model donor pull and retention under redaction, keeping Mistral's
   verdict-dependent exception visible.
4. Compact appendix tables: cross-round stability, breadth, size, G3, and failed
   interventions.

## What the paper must not say

Carried verbatim from `RELATED_WORK_2026.md` §12 and the round write-ups:

- not "we are the first to show models state a temporal rule and violate it";
- not "hindsight makes the model less faithful than an independent ex-ante
  reference" (G7 failed);
- not "the position-sensitive mechanism replicates" (G2-A did not);
- not any claim that models cannot discount evidence they believe false *in
  general* — G3 shows only that this prompt slot does not reach that machinery;
- not any statement that an ex-ante representation is absent or overwritten;
  the current G6 intervention does not identify that contrast.
