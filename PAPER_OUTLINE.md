# Paper outline — current submission narrative

**Updated:** 2026-09-03

The paper follows one explanatory descent. Historical dead ends belong in `RESEARCH_HISTORY.md` and the appendix, not as equal-weight main sections.

## Recommended title

> **Can Language Models Unsee the Future? Retrospective Epistemic Reconstruction After Outcomes Are Known**

Possible shorter subtitle:

> **Information-Set Conditioning Under Hindsight**

Avoid making “retrospective outcome entrainment” the whole title-level object. It is an important operational phenomenon, but the paper should survive disagreement about that name.

## Abstract draft

A reasoner who already knows how an event turned out may still be asked to reconstruct a judgment using only information that was available beforehand. We study whether language models can perform this **retrospective information-set conditioning**. On 256 independently sampled natural forecasting questions, we manipulate within item the presence and admissibility of the same post-cutoff evidence. Three open checkpoints identify at 99.2–100% accuracy that this evidence lies outside the target historical information set, yet their reconstructed probabilities still shift by 7.5–27.7 points. The effect survives removal of explicit resolution-verdict sentences. We then ask what kind of future information drives the failure. Replacing a question's resolution packet with a packet from a different resolved event still causes substantial movement and donor-directed pull; after explicit verdict redaction, much of this pull survives in two of three primary models. In a paired intervention, replacing a NO-supporting irrelevant packet with a YES-supporting packet raises the same recipient probability in all three models, although magnitude is strongly model-dependent and the preregistered 5-point panel gate is indeterminate. Finally, in the strong-effect model, donor outcome is decodable in packet states but the tested one-dimensional packet-local interchange does not transfer behavior. A fresh preregistered confirmation instead finds that outcome influence becomes causally actionable after recipient contextualization in a late answer-position decision state, where one-dimensional interchange transfers 35–48% of the behavioral contrast and a matched orthogonal direction does not. These results show that explicit recognition of an information boundary is insufficient to enforce it in retrospective judgment, and localize the resulting future-outcome influence without claiming a universal hindsight circuit.

## 1. Introduction

Open with the natural operation:

> After learning the outcome, can a model still judge from only what was knowable before?

Then distinguish three neighboring questions immediately:

1. **temporal leakage / ex-ante inference:** does the model possess or use later knowledge at all?
2. **irrelevant-context robustness:** do distractors change answers?
3. **our object:** can the model condition a judgment on a counterfactual earlier information set while later evidence remains explicitly available?

Concede that prior work already shows temporal-rule knowledge can coexist with wrong temporal application. The novelty is not the gap by itself; it is the controlled causal measurement and the subsequent explanatory descent.

End the introduction with three contributions, not a laundry list:

- a prospectively replicated recognition–enforcement dissociation under a within-item same-evidence intervention;
- a directional regularity in which outcome-shaped evidence from unrelated resolved events pulls reconstructed judgments, including a paired outcome-class intervention with heterogeneous strength;
- a Gemma-specific mechanistic discrimination showing late recipient-conditioned causal expression rather than the tested one-dimensional packet-local bottleneck.

## 2. Task and causal estimand

Introduce BTF-3 only after the scientific object.

Explain the 2×2 design:

- packet absent vs. present;
- historical/ex-ante information set vs. retrospective/licensed information set.

Define `Responsiveness`, `OutOfSetIntrusion`, and boundary recognition.

Emphasize that the packet can remain true, useful, and remembered; the requirement is that it have zero causal effect on the historical judgment when it lies outside the target information set.

## 3. Prospectively replicated recognition–enforcement gap

Lead with the 256-unit fresh replication; mention 8-item discovery and 64-item confirmation as chronology/prospective validation.

Main table:

| model | recognition | OutOfSetIntrusion |
|---|---:|---:|
| Qwen3.5-9B | 99.22% | 16.02 |
| Gemma-3-12B-it | 99.80% | 27.73 |
| Mistral-Small-24B | 100.00% | 7.46 |

Then compactly report verdict redaction and within-family scale as characterization, not separate discoveries.

## 4. Outcome-shaped future context from unrelated events

### 4.1 G8: relevance is not enough

Foreign packets from unrelated resolved questions cause 50.7–100.1% as much absolute movement as real packets and produce donor-directed pull.

State the frozen result honestly: continuous estimates are positive across all three models, but only Gemma clears the preregistered 5pp strong-form threshold.

### 4.2 G11: explicit verdict copying is insufficient

After verdict redaction, donor pull retains 73.9% in Qwen and 67.1% in Gemma, but only 35.0% in Mistral.

Define **retrospective outcome entrainment** operationally here, not in the opening sentence of the paper.

## 5. G12: direct directional intervention within recipient

For the same recipient history, compare a verdict-redacted irrelevant packet supporting NO with a different verdict-redacted irrelevant packet supporting YES.

Report:

- Qwen +4.41pp
- Gemma +17.50pp
- Mistral +1.55pp

All paired intervals are positive; magnitude is heterogeneous; frozen 5pp panel gate is indeterminate.

Use precise wording:

> “Replacing NO-supporting irrelevant future evidence with YES-supporting irrelevant future evidence raises the same reconstructed probability.”

Do **not** say “changing only donor outcome,” because packet identity and semantics also change.

## 6. G13–G15: where outcome influence becomes causal

Present competing algorithms first:

- packet-local scalar transport;
- recipient-conditioned decision-state construction.

### 6.1 Packet site

G13: donor outcome is decodable, but the tested one-dimensional packet-span interchange has no preregistered causal transfer window.

### 6.2 Answer site

Explain chronology explicitly:

- G14 discovered a late answer-site pattern but failed its inherited global representation gate by 0.008;
- G14 therefore generated the refined recipient-conditioned paired hypothesis;
- G15 preregistered that estimand before fresh outputs/activations and rebuilt donor assignment.

G15 confirmed:

- fresh behavior +18.84pp [12.94, 24.97];
- late paired representation ordering;
- +6.52 / +9.04 / +7.73 / +8.34pp causal transfer at layers 29 / 35 / 41 / 47;
- up to 48% behavioral-effect recovery;
- bidirectionality;
- orthogonal control near zero.

End with the bounded claim:

> **In Gemma, future-outcome influence becomes causally actionable after recipient contextualization in a late answer-position decision state rather than through the tested one-dimensional packet-local bottleneck.**

## 7. What this does and does not explain

The mechanism closes the question “where/how does outcome influence become causally actionable?”

It does **not** yet explain the deeper puzzle:

> Why does a boundary the model can recognize fail to gate this pathway?

This unresolved point belongs in Discussion/Future Work, not as a reason to dilute the current paper with extra defensive experiments.

## 8. Related work

Organize by conceptual neighborhood, not chronological bibliography:

1. ex-ante reasoning / temporal leakage;
2. distraction, irrelevant context, and contextual conflict;
3. knowledge/recognition–action gaps;
4. mechanistic work on contextualization, competing pathways, and causal abstraction.

Use `RELATED_WORK_2026.md` as the binding novelty note.

## 9. Limitations

Must include:

- one primary natural substrate;
- failed FANToM/FOMC generalization attempts;
- G7 weak pastcasting and failed external-fidelity prediction;
- source-packet factuality audit covers a hash-fixed 64-item subsample rather than certifying all 256;
- verdict-redacted packets may still semantically entail the outcome;
- G12 does not isolate an abstract outcome bit holding packet semantics fixed;
- mechanism is established in Gemma only;
- late-state mechanism does not establish whether a clean ex-ante estimate was built earlier.

## Figures

1. **Natural operation + 2×2 causal design + replicated recognition/intrusion gap.**
2. **Explanatory descent:** own packet → foreign packet → verdict-redacted foreign packet → paired YES/NO-supporting replacement.
3. **Per-model heterogeneity:** donor pull and redaction retention, with Mistral exception visible.
4. **Mechanism:** packet-site non-transfer versus late answer-site transfer on fresh G15 assignment, including orthogonal control.

## Appendix compression

Move or keep compact:

- G3 exclusion reasons;
- G4 breadth;
- G5/G6/G7/G9/G10 failures;
- G13/G14 discovery chronology details;
- early Unring-the-Bell / Stage 2–5 controlled history;
- failed source engineering.

## Forbidden overclaims

- first temporal recognition–behavior gap;
- robust/universal outcome entrainment across models;
- “changing only the outcome” for G12;
- dedicated hindsight axis/circuit;
- full mechanism of hindsight contamination;
- external ex-ante fidelity;
- clean ex-ante state absence/override.
