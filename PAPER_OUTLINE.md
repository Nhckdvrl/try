# Paper outline — draft against results in hand

**Created:** 2026-09-01. Written from `PAPER_FRAME.md` and the rounds that have
landed. Sections marked **pending** depend on G5, G6, or G8, which are running;
each says what it will contain under each possible outcome, so the outline does
not quietly assume a result.

---

## Title

Recommended:

> **What Was Reasonable to Believe: Language Models Recognize Out-of-Set
> Evidence and Cannot Set It Aside**

Alternatives, in case the mechanism round changes the emphasis:

- *Recognized but Not Enforced: Hindsight Contamination in Reconstructed
  Past Judgments*
- *No Reason Is Enough: Language Models Restate Exclusion Rules They Do Not
  Implement*

All three survive every outcome of G5, G6 and G8 — the gate in
`PAPER_FRAME.md` §7. None of them names a dataset, a metric, or a condition.

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
> grows — and does not diminish with model scale within a family. We then ask
> which kind of boundary a model can enforce at all, by replacing the *reason*
> for exclusion and nothing else: a non-temporal licensing reason with the
> evidence's accuracy affirmed, a reason that undercuts the evidence's truth,
> and no reason at all. **None of them reduces the effect**, while recognition
> stays at ceiling in every arm. Against the same evidence's full measurable
> influence — its effect on a licensed retrospective judgment — 41% to 81% is
> absent from the ex-ante judgment, so the instruction is not simply ignored;
> what varies is the model, not the justification it was given. The
> failure is therefore not that models ignore exclusion, and not that it is
> about time, about belief in the evidence, or about the reason being left
> unstated. [G8 sentence.] [G6 mechanism sentence.] [Method sentence.]

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

### 4. What it is not

Three eliminations, each preregistered before its round:

- **not answer-copying** — verdict redaction (G2-B), effect survives and grows;
- **not a scale artefact** — 4B/9B/27B within one family, non-monotone,
  largest most contaminated;
- **not a property of three checkpoints** — the breadth panel (G4).

The breadth panel also separates two failures the paper had only ever seen
together: checkpoints that cannot reliably recognise the boundary (probe
56–74%) and checkpoints that recognise it at ceiling and are moved anyway. Only
the second is the dissociation, and the paper says so.

### 5. Which boundary can be enforced? (G3 — the core section)

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

### 6. Does the packet have to be about this question? **(pending G8)**

- If `I_donor` is positive: the strongest result in the paper — the model
  imports an unrelated question's resolution — and the section becomes a
  contextual-entrainment argument.
- If only `S_swap` is substantial: presence perturbs the judgment without
  pointing anywhere.
- If neither: the effect needs the packet to be about the question, and §5's
  amplification needs an explanation that is not salience. Section shortens and
  says so.

### 7. Does deliberation rebuild the ex-ante state? **(pending G5)**

The `state`-vs-`cot` contrast, with the utility guard. Doubles as the prompt-level
mitigation baseline that §9 must beat.

### 8. Mechanism: overwritten or never formed? **(pending G6)**

The layer-window sweep and `f*`. Probing appears only as an availability
statement. Instrument checks (full-depth restoration; HF-vs-vLLM disagreement)
are reported before the result.

### 9. Enforcement by masking **(pending G6-C)**

The method: mask the out-of-set span for answer positions at inference. The
table carries `I_mask`, licensed responsiveness, the unmasked boundary probe
(memory retained), the wrong-span control, and the deletion reference. The
claim is selective, reversible enforcement with the evidence still in context
and still answerable — measured against prompting, which §5 showed does
nothing, and against §7's scaffold.

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

1. Recognition vs intrusion, 256 units, three checkpoints (the dissociation).
2. Cross-round stability (8 → 64 → 256) with all intervals containing zero.
3. The exclusion-reason factorization: four arms × three models, with
   recognition on a second axis.
4. Breadth panel: intrusion by checkpoint, recognition-qualified and not,
   coloured by family.
5. Restoration curve `R(f)` per model, with the wrong-span control and the
   deletion reference. **(pending G6)**
6. Mitigation table: prompting arms, the state scaffold, and masking, each with
   its utility column. **(pending G5, G6)**

## What the paper must not say

Carried verbatim from `RELATED_WORK_2026.md` §12 and the round write-ups:

- not "we are the first to show models state a temporal rule and violate it";
- not "hindsight makes the model less faithful than an independent ex-ante
  reference" (G7 failed);
- not "the position-sensitive mechanism replicates" (G2-A did not);
- not any claim that models cannot discount evidence they believe false *in
  general* — G3 shows only that this prompt slot does not reach that machinery;
- not any statement about internal representations being overwritten unless
  G6's `f*` lands in the `H-override` region.
