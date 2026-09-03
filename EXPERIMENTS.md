# Experiment registry

This is the single live index of the experimental program.

The original preregistration documents are preserved **unchanged** in [`preregistrations/`](preregistrations/). Use this file to understand what each round asked, what happened, and what role it has in the paper; open an original preregistration when you need exact hypotheses, estimands, thresholds, sampling rules, qualification gates, or frozen analysis plans.

## A. Main paper sequence

### A1. Natural hindsight effect — BTF-3 confirmation and large replication

**Question.** After a model learns how an event ended, does that later evidence change its judgment of the event as it looked beforehand?

**Design.** The same historical question is evaluated with and without a post-cutoff resolution packet. A separate probe checks whether the model recognizes that the packet comes from after the target time. The effect was discovered on 8 items, prospectively confirmed on 64 fresh items, and then replicated on 256 additional fresh items.

**Result.** In the 256-item round, the three primary open checkpoints recognize the time boundary at 99.2–100%, yet the later evidence still shifts the past judgment by 7.46–27.73 probability points.

**Paper role.** Headline phenomenon: models show a strong hindsight effect even when they know which evidence came later.

### A2. G8 — foreign resolved events

**Question.** Is the hindsight effect tied to evidence about the target event, or can the outcome of another resolved event pull the judgment too?

**Design.** Replace the target event's future packet with the resolution packet of a different event.

**Result.** Foreign packets still cause substantial movement (50.7–100.1% of the absolute movement caused by real packets), and donor-directed pull is positive across the three primary models, though its magnitude is heterogeneous.

**Paper role.** First explanatory step below generic hindsight: later context carries a directional outcome influence even when it is about another event.

### A3. G11 — outcome evidence without an explicit verdict

**Question.** Does the donor-directed pull require a literal YES/NO resolution sentence?

**Design.** Remove explicit verdict sentences from the foreign future packets while retaining the remaining post-outcome evidence.

**Result.** Qwen and Gemma retain most of the donor-directed pull; Mistral is much more verdict-dependent.

**Paper role.** Shows that the directional effect can be carried by outcome-shaped evidence, not only by copying a visible answer label.

### A4. G12 — paired outcome-direction intervention

**Question.** Does replacing NO-supporting later evidence with YES-supporting later evidence systematically change the same recipient judgment?

**Design.** Hold the recipient history and non-packet prompt fixed; replace a verdict-redacted irrelevant packet supporting NO with a different verdict-redacted irrelevant packet supporting YES.

**Result.** The recipient YES probability rises by +4.41pp (Qwen), +17.50pp (Gemma), and +1.55pp (Mistral). The direction is consistent; magnitude is strongly model-dependent.

**Paper role.** Direct behavioral evidence that outcome direction controls the pull.

### A5. G13 → G14 → G15 — where outcome influence becomes causal

**Question.** Is donor outcome carried forward as a shared packet-local scalar, or does it become a causal decision variable only after the packet is interpreted in the recipient context?

**G13.** Donor outcome is decodable from packet states, but the preregistered one-dimensional packet-span interchange does not produce a causal transfer window.

**G14.** Moving the intervention to the answer position reveals a late transfer pattern. Its inherited composite gate misses because the global representation criterion falls 0.008 below threshold; this round is discovery for the recipient-conditioned hypothesis.

**G15.** Before observing fresh outputs or activations, the recipient-conditioned paired estimand is preregistered on a fresh donor assignment. The fresh behavioral contrast is +18.84pp [12.94, 24.97]. Late answer-position interchange transfers +6.52 to +9.04pp at layers 29–47, works in both directions, and is near zero on a matched orthogonal direction.

**Paper role.** In Gemma, the outcome influence becomes causally expressed in a late recipient-conditioned decision state.

## B. Supporting characterization

These experiments sharpen the main result but should not become separate narrative branches in the paper.

### B1. Verdict redaction on the target event

Removing the explicit resolution verdict from the target event's own future packet does not eliminate the hindsight effect. This motivated the later foreign-packet decomposition.

### B2. Qwen3.5 size sweep

Qwen3.5 4B/9B/27B all show the effect, with a strongly non-monotonic pattern (32.00 → 16.02 → 36.75pp). This is characterization, not the paper's conceptual center.

### B3. G3 — exclusion reason

Changing the stated reason for ignoring the packet (temporal, procedural, unreliable, or no reason) does not reduce the effect at panel level. This helped move the project away from a narrow story about one temporal instruction wording.

### B4. G4 — model breadth

Broader checkpoint testing shows that recognizing the boundary and resisting outcome influence are not the same capability axis. This supports the headline dissociation but is not a separate story.

## C. Historical rounds that changed or narrowed the project

These are retained because they explain how the project arrived at the current question, not because they belong in the main narrative.

### C1. G0 — *Can LLMs Unring the Bell?*

The original preregistered prediction was that excluding evidence after seeing it would be harder than excluding it in advance. The result reversed: post-evidence exclusion was generally easier. This killed the original headline and led to the prospective-nullification line of work.

### C2. G1 and factorization rounds — broad Information-Set Reasoning

The project tried to generalize the phenomenon across multiple kinds of information boundaries. BTF-3 temporal tasks qualified; the perspective-family FANToM branch did not. This forced a narrower empirical program and ultimately returned the project to the natural question of hindsight.

### C3. G5 — deliberation/state scaffold

The preregistered instrument did not cleanly qualify because of truncation/design problems. It is indeterminate and not part of the main paper.

### C4. G6 — early mechanism attempt

Layer-window masking localized access from packet to answer but did not distinguish the internal accounts it was meant to separate. It was superseded by the G13–G15 question.

### C5. G7 — external ex-ante anchor

The preregistered prediction failed in the opposite direction: later evidence moved model judgments closer to BTF-3's independent ex-ante forecast. This removed an unnecessary claim about objective forecast fidelity and left the within-item hindsight effect untouched.

### C6. G9 — numeric second-task attempt

The task did not pass its qualification gate and therefore provides no replication verdict.

### C7. G10 — worked-example mitigation

Results were heterogeneous across models. This is not a main contribution and should not turn the paper into a mitigation study.

## D. Data and audit artifacts

The BTF-3 transformation contract, factuality-audit protocol, frozen data artifacts, result files, analysis code, and raw outputs remain in their existing locations. These are provenance and reproduction materials, not paper-navigation documents.

## E. Original preregistrations

Exact preregistration text is in [`preregistrations/`](preregistrations/), organized by [`preregistrations/README.md`](preregistrations/README.md). The corresponding Git freeze commits/tags remain the authority for chronology relative to model outputs.

## F. Active prospective extension

**Llama-3.1-8B explanatory descent.** A1 already exists from the frozen G4
panel: hindsight intrusion is +28.23pp, OOB boundary recognition is 250/256,
but the original stronger two-frame G4 qualification failed because the model
misread the licensed/all-information boundary check. The prospectively frozen
extension runs the unchanged G8, G11, and G12 instruments to locate how far the
Meta family follows the positive explanatory chain. Mistral and every original
panel verdict remain unchanged.
