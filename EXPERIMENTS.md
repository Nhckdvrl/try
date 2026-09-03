# Experiment registry

This is the single live index of the experimental program.

The repository previously kept one top-level `PREREGISTRATION_*.md` file for nearly every round. That was useful while experiments were being designed, but it made the project hard to read once the scientific story stabilized. The original preregistration files remain recoverable from Git history and their freeze commits/tags; this file records what each round asked, what happened, and what role it has in the paper. Historical preregistrations must not be retrospectively rewritten.

## A. Main paper sequence

### A1. Natural hindsight effect — BTF-3 confirmation and large replication

**Question.** After a model learns how an event ended, does that later evidence change its judgment of the event as it looked beforehand?

**Design.** The same historical question is evaluated with and without a post-cutoff resolution packet. A separate probe checks whether the model recognizes that the packet comes from after the target time. The effect was discovered on 8 items, prospectively confirmed on 64 fresh items, and then replicated on 256 additional fresh items.

**Result.** In the 256-item round, the three primary open checkpoints recognize the time boundary at 99.2–100%, yet the later evidence still shifts the past judgment by 7.46–27.73 probability points.

**Paper role.** Headline phenomenon: models show a strong hindsight effect even when they know which evidence came later.

### A2. G8 — foreign resolved events

**Question.** Is the hindsight effect tied to evidence about the target event, or can the mere shape of a known outcome pull another judgment?

**Design.** Replace the target event's future packet with the resolution packet of a different event.

**Result.** Foreign packets still cause substantial movement (50.7–100.1% of the absolute movement caused by real packets), and donor-directed pull is positive across the three primary models, though its magnitude is heterogeneous.

**Paper role.** First explanatory step below generic hindsight: the influence is organized by the outcome supported by later context, not only by evidence diagnostic of the target event.

### A3. G11 — outcome evidence without an explicit verdict

**Question.** Does the donor-directed pull require a literal YES/NO resolution sentence?

**Design.** Remove explicit verdict sentences from the foreign future packets while retaining the remaining post-outcome evidence.

**Result.** Qwen and Gemma retain most of the donor-directed pull; Mistral is much more verdict-dependent.

**Paper role.** Shows that the directional effect is carried by outcome-shaped evidence, not only by copying a visible answer label.

### A4. G12 — paired outcome-direction intervention

**Question.** Does replacing NO-supporting later evidence with YES-supporting later evidence systematically change the same recipient judgment?

**Design.** Hold the recipient history and non-packet prompt fixed; replace a verdict-redacted irrelevant packet supporting NO with a different verdict-redacted irrelevant packet supporting YES.

**Result.** The recipient YES probability rises by +4.41pp (Qwen), +17.50pp (Gemma), and +1.55pp (Mistral). The direction is consistent; magnitude is strongly model-dependent.

**Paper role.** Direct behavioral evidence that outcome direction controls the pull. The experiment does not isolate a single abstract outcome bit because the two donor packets are different pieces of text.

### A5. G13 → G14 → G15 — where outcome influence becomes causal

**Question.** Is donor outcome carried forward as a shared packet-local scalar, or does it become a causal decision variable only after the packet is interpreted in the recipient context?

**G13.** Donor outcome is decodable from packet states, but the preregistered one-dimensional packet-span interchange does not produce a causal transfer window.

**G14.** Moving the intervention to the answer position reveals a late transfer pattern. Its inherited composite gate misses because the global representation criterion falls 0.008 below threshold; this round is discovery for the recipient-conditioned hypothesis.

**G15.** Before observing fresh outputs or activations, the recipient-conditioned paired estimand is preregistered on a fresh donor assignment. The fresh behavioral contrast is +18.84pp [12.94, 24.97]. Late answer-position interchange transfers +6.52 to +9.04pp at layers 29–47, works in both directions, and is near zero on a matched orthogonal direction.

**Paper role.** In Gemma, the outcome influence becomes causally expressed in a late recipient-conditioned decision state; the tested one-dimensional packet-local bottleneck is not supported.

## B. Supporting characterization

These experiments sharpen the main result but should not become separate narrative branches in the paper.

### B1. Verdict redaction on the target event

Removing the explicit resolution verdict from the target event's own future packet does not eliminate the hindsight effect. This motivated the later foreign-packet decomposition.

### B2. Qwen3.5 size sweep

Qwen3.5 4B/9B/27B all show the effect, with a strongly non-monotonic pattern (32.00 → 16.02 → 36.75pp). This is characterization, not a scaling-law claim.

### B3. G3 — exclusion reason

Changing the stated reason for ignoring the packet (temporal, procedural, unreliable, or no reason) does not reduce the effect at panel level. This helped move the project away from a narrow story about one temporal instruction wording.

### B4. G4 — model breadth

Broader checkpoint testing shows that recognizing the boundary and resisting outcome influence are not the same capability axis. This supports the behavioral dissociation but is not the paper's conceptual center.

## C. Historical rounds that changed or narrowed the project

These are retained because they explain how the project arrived at the current question, not because they belong in the main narrative.

### C1. G0 — *Can LLMs Unring the Bell?*

The original preregistered prediction was that excluding evidence after seeing it would be harder than excluding it in advance. The result reversed: post-evidence exclusion was generally easier. This killed the original headline and led to the prospective-nullification line of work.

### C2. G1 and factorization rounds — broad Information-Set Reasoning

The project tried to generalize the phenomenon across multiple kinds of information boundaries. BTF-3 temporal tasks qualified; the perspective-family FANToM branch did not. This forced a narrower, natural hindsight paper rather than a broad information-set benchmark paper.

### C3. G5 — deliberation/state scaffold

The preregistered instrument did not cleanly qualify because of truncation/design problems. It is indeterminate and not part of the main paper.

### C4. G6 — early mechanism attempt

Layer-window masking localized access from packet to answer but did not distinguish the internal accounts it was meant to separate. It was superseded by the G13–G15 question.

### C5. G7 — external ex-ante anchor

The preregistered prediction failed in the opposite direction: later evidence moved model judgments closer to BTF-3's independent ex-ante forecast. The round removed an unnecessary claim about objective forecast fidelity and left the within-item hindsight effect untouched.

### C6. G9 — numeric second-task attempt

The task did not pass its qualification gate and therefore provides no replication verdict.

### C7. G10 — worked-example mitigation

Results were heterogeneous across models. This is not a main contribution and should not be used to turn the paper into a mitigation study.

## D. Data and audit artifacts

The BTF-3 transformation contract, factuality-audit protocol, frozen data artifacts, result files, analysis code, and raw outputs remain in their existing locations. These are provenance and reproduction materials, not paper-navigation documents.

## E. How to recover an original preregistration

The individual preregistration files were consolidated out of the repository root on 2026-09-03. Their exact historical text remains in Git history and, where used, the corresponding freeze commits/tags. To inspect one, use Git history for its former filename (for example `PREREGISTRATION_G15_DECISION_CONFIRMATION.md`) rather than reconstructing it from this summary.
