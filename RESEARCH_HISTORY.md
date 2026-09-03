# Research history — from *Unring the Bell* to retrospective epistemic reconstruction

This document preserves the scientific evolution of the project so obsolete stage-by-stage narrative files can be removed without erasing why the current question exists.

It is **history, not the current paper frame**. For live claims, read `PAPER_FRAME.md`.

## 0. Starting point: *Can LLMs Unring the Bell?*

The original project was motivated by a human-style “Unring the Bell” intuition: if evidence is later declared inadmissible, perhaps a model will continue to use it because it has already incorporated it.

G0 preregistered a broad controlled study over 144 frozen items and multiple task families/models. The central temporal prediction was **reversed**. Models were generally better at suppressing evidence when the exclusion rule came **after** the evidence than when the same rule was stated **before** it.

That killed the original headline. The important surviving observation was not “LLMs cannot unring the bell,” but a prospective nullification problem: models could often state the exclusion rule correctly yet still let supposedly zero-weight evidence influence a later decision.

This reversal is the first important epistemic transition in the project. It must remain visible because the current paper was not designed backwards from the final result.

## 1. Controlled-mechanism phase: prospective nullification gap

Stages 2–5 tried to understand the reversed effect in controlled synthetic tasks.

The program tested whether the failure was explained by distance/recency, exact-zero discontinuity, prospective memory, object identity/addressability, class predicates, explicit weight retrieval, semantic tags, and internal rule representations. Several early interpretations were overturned by later controls.

Useful lessons survived, but the phase became too tied to a particular controlled prompt grammar. In particular:

- exact-zero suppression behaved differently from non-zero attenuation;
- declarative knowledge of the rule did not guarantee causal non-use;
- some apparently promising “class routing” explanations were artifacts of semantic tags;
- mechanistic interventions could localize states in the controlled setup, but the scientific object was becoming narrower than the natural question that motivated the work.

These experiments are scientifically useful provenance, not the submission narrative.

## 2. Broad reframing: Information-Set Reasoning

The project then generalized the problem away from a particular “zero-weight rule.” The broader question became whether a model can reason from a **specified information set** while possessing information outside it.

A multi-family program was designed across temporal, perspective, procedural/access, and other candidate boundaries. The intended object was selective causal use of information rather than forgetting or factual recall.

This was a conceptual improvement: the project stopped asking whether one wording works and started asking whether a reasoner can condition a judgment on the correct epistemic state.

However, the broad program did not survive qualification cleanly.

## 3. Natural-substrate narrowing: temporal reconstruction on BTF-3

BTF-3 provided a natural measurement window with:

- a historical forecasting question;
- information available before a cutoff;
- a later resolution packet;
- a continuous probability judgment;
- a realized outcome.

The perspective-family FANToM pilot failed qualification. A FOMC external-source attempt later failed its preregistered source-qualification gate. Those failures forced the project to **narrow rather than overclaim**.

The paper therefore became temporal-only: can a model reconstruct a historical judgment while explicit post-cutoff evidence is present but defined as outside the target information set?

## 4. Replicated phenomenon: recognition without enforcement

The BTF-3 effect was accumulated prospectively:

1. 8-item discovery pilot;
2. 64-item preregistered confirmation;
3. 256-item preregistered fresh large replication.

In the 256-unit round, three primary open checkpoints recognized the temporal boundary at 99.2–100% accuracy, yet the future packet still shifted the reconstructed ex-ante probability by roughly 7.5–27.7 points.

This established a strong behavioral dissociation: **recognizing that evidence is outside the target information set does not make that evidence causally inert in the decision.**

Verdict redaction showed that the effect was not reducible to copying an explicit YES/NO resolution sentence. A within-family Qwen3.5 size sweep showed no monotonic disappearance with scale.

At this point the paper had a replicated phenomenon, but not yet a sufficiently sharp explanatory step.

## 5. Failed and narrowing accounts: G3–G7

The next rounds are important mainly because they prevented an easy but wrong story.

### G3 — exclusion reason

Changing why the packet should be excluded — temporal, procedural, unreliable, or no stated reason — did not reduce intrusion at panel level. This weakened a simple “temporal rule is uniquely hard” story.

But G3 does **not** prove a general belief-insensitive mechanism: telling a model that a packet may be unreliable does not establish that the model internally treated it as false.

### G4 — breadth

Broader checkpoint testing showed that recognition and intrusion are not simply the same capability axis. This is characterization, not the paper’s core explanatory advance.

### G5 — deliberation

The preregistered deliberation/state-scaffold test suffered an instrument/design failure and is kept as indeterminate rather than repaired post hoc.

### G6 — early mechanism attempt

Layer-window masking localized packet access but could not actually distinguish whether a clean ex-ante state had existed and was overwritten versus never constructed. It was therefore excluded from the main mechanistic story.

### G7 — external ex-ante anchor

This preregistered test failed in the **opposite direction**: adding the packet moved model judgments closer to BTF-3’s independent ex-ante forecast, not farther away. The uncontaminated judgments correlated only about 0.28–0.33 with that forecast.

This killed any claim that the packet makes models less faithful to an objective/competent ex-ante reference. The paper’s valid object became more precise: **causal invariance to information that is outside the target information set**, not objective forecast quality.

This is why the current natural question should avoid overloading the word “reasonable.”

## 6. Explanatory turn: from generic contamination to outcome-shaped pull

### G8 — foreign future packets

Each recipient question received a post-cutoff resolution packet from a **different question**. These unrelated packets still caused substantial movement, and their effects tended to pull the recipient judgment toward the donor question’s outcome.

This showed that the phenomenon was not limited to integrating evidence diagnostic of the recipient event itself.

The preregistered strong-form threshold was not uniformly met, so the frozen conclusion remained weak/heterogeneous rather than universal.

### G11 — verdict-redacted foreign packets

Removing explicit YES/NO verdict sentences preserved much of the donor-directed pull in Qwen and Gemma, but much less in Mistral. Explicit label copying was therefore insufficient as a panel-level explanation, while model dependence remained real.

This motivated the operational term **retrospective outcome entrainment**: outcome-shaped later context can pull a reconstructed past judgment toward the outcome it supports even when the context comes from another resolved event.

The term is useful, but the paper’s deeper scientific object remains retrospective epistemic reconstruction.

## 7. Direct directional intervention: G12

G12 held the recipient history fixed and replaced a verdict-redacted foreign packet supporting NO with a different verdict-redacted foreign packet supporting YES.

The recipient probability increased in all three primary models, but magnitude was strongly heterogeneous (+4.41pp Qwen, +17.50pp Gemma, +1.55pp Mistral). The preregistered 5pp panel gate was indeterminate.

Critical precision:

> G12 changes the **outcome class of the irrelevant future evidence**, but the YES-supporting and NO-supporting packets are different packets. Packet identity, lexical content, event semantics, and other features are not held fixed.

Therefore the safe result is directional control by outcome-shaped evidence class, **not** isolation of an abstract outcome bit with all other semantics fixed.

## 8. Mechanistic discrimination: G13 → G14 → G15

The mechanistic question became where donor outcome information is transformed into something that causally controls the recipient answer.

### G13 — packet-local scalar hypothesis

Preregistered hypothesis: donor outcome is compressed into a shared one-dimensional packet-local scalar that is transported to the answer.

Result: donor outcome was decodable from packet states, but the preregistered packet-span interchange did not produce the required causal transfer window. The tested packet-local one-dimensional bottleneck was therefore **not established**.

### G14 — answer-site discovery

Moving the analysis to the answer position revealed a late, bidirectional causal transfer pattern, but the inherited global representation criterion missed its preregistered threshold by 0.008. G14 therefore remained a failed composite gate while generating a refined hypothesis: the relevant variable may be **recipient-conditioned**, so within-recipient paired ordering is the correct estimand.

### G15 — prospective confirmation

Before observing fresh outputs/activations, G15 preregistered that refined recipient-conditioned estimand, kept the strict threshold, and rebuilt a fresh donor assignment.

The fresh behavioral contrast was +18.84pp [12.94, 24.97]. Late layers showed strong paired ordering; one-dimensional causal interchange at the answer position transferred 6.52–9.04pp across layers 29–47, worked bidirectionally, and disappeared on a matched orthogonal direction.

The resulting claim is strong but bounded:

> **In the strong-effect model, future-outcome influence becomes causally actionable after recipient contextualization in a late answer-position decision state; the tested one-dimensional packet-local bottleneck is not supported.**

It is not evidence for a dedicated hindsight circuit, and it does not establish whether a clean ex-ante state was constructed earlier.

## 9. Current paper: retrospective epistemic reconstruction

The current scientific object is best stated as:

> **After learning how something turned out, can a language model still condition a reconstructed past judgment only on the information that was available beforehand?**

The submission narrative is now:

```text
information-set boundary is recognized
    ↓
unlicensed future evidence still changes the judgment
    ↓
unrelated outcome-shaped evidence produces directional pull
    ↓
paired outcome-class replacement controls direction, heterogeneously
    ↓
in Gemma, the influence becomes causal in a late recipient-conditioned decision state
```

BTF-3 is the measurement window. The scientific object is retrospective information-set conditioning under hindsight.

## 10. What remains open

For an ACL/EMNLP Main submission, the experimental program can stop here.

The unresolved higher-level puzzle is:

> **Why does a represented/recognized information boundary fail to gate the late outcome pathway?**

A future Outstanding-ambition experiment is justified only if it prospectively distinguishes algorithms that all explain G0–G15, for example:

- a genuine admissibility gate exists but is too weak/bypassed;
- boundary recognition and outcome integration are parallel computations and the decision readout ignores the former;
- boundary “recognition” is only a probe-readable/readout state with no causal role in the historical judgment.

Do not run another condition merely because it is easy. The next experiment, if any, must answer this algorithmic question.
