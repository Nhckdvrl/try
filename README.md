# Can Language Models Unsee the Future?

## Retrospective epistemic reconstruction after outcomes are known

This repository studies a simple question:

> **After learning how something turned out, can a language model still condition a reconstructed past judgment only on the information that was available beforehand?**

The current paper is about **retrospective epistemic reconstruction / information-set conditioning under hindsight**. BTF-3 is the main natural measurement window; it is not the scientific identity of the project.

## Read this repository in this order

1. [`CLAUDE.md`](CLAUDE.md) — project instructions for Claude Code, environment/GPU policy, and the default research decision rule.
2. [`PAPER_FRAME.md`](PAPER_FRAME.md) — authoritative scientific claims and forbidden overclaims.
3. [`ACL_EMNLP_ALIGNMENT_STANDARD.md`](ACL_EMNLP_ALIGNMENT_STANDARD.md) — the quality bar, explicitly calibrated to strong ACL/EMNLP/NAACL Main and Outstanding papers.
4. [`RESEARCH_HISTORY.md`](RESEARCH_HISTORY.md) — how the project evolved from *Unring the Bell* to the current paper.
5. [`PAPER_OUTLINE.md`](PAPER_OUTLINE.md) — current submission narrative and figure plan.
6. [`RELATED_WORK_2026.md`](RELATED_WORK_2026.md) — novelty boundaries and closest conceptual neighbours.

Preregistrations, frozen transformation contracts, result files, and analysis artifacts remain in the repository as scientific provenance.

## Current evidence chain

### 1. Recognition does not guarantee enforcement

On a fresh 256-question BTF-3 replication, three primary open checkpoints recognize at 99.2–100% accuracy that a resolution packet postdates the target historical cutoff, yet the same future evidence still shifts reconstructed ex-ante probabilities by 7.46–27.73 points.

This is a **within-item causal effect** of explicit later evidence on an otherwise identical historical judgment.

### 2. The effect is not just explicit verdict copying

Mechanical removal of explicit resolution-verdict sentences does not eliminate the contamination. The redacted packet still has substantial causal influence.

### 3. Outcome-shaped evidence from unrelated events still pulls the judgment

G8 replaces the recipient's own packet with a future packet from a different resolved question. Foreign packets still cause large movement and donor-directed pull.

G11 removes explicit YES/NO verdict sentences from those foreign packets. Much of the donor pull survives in Qwen and Gemma; Mistral is substantially more verdict-dependent.

We call this operational regularity **retrospective outcome entrainment**.

### 4. Paired outcome-class replacement controls direction, but heterogeneously

G12 holds the recipient history fixed and replaces a verdict-redacted irrelevant packet supporting NO with a different packet supporting YES.

Paired shifts:

- Qwen: +4.41pp
- Gemma: +17.50pp
- Mistral: +1.55pp

All point in the same direction, but effect magnitude is strongly model-dependent and the preregistered 5pp panel gate is indeterminate.

Important: this does **not** isolate an abstract outcome bit while holding all packet semantics fixed.

### 5. In Gemma, influence becomes causal late after recipient contextualization

G13 tested a donor-general one-dimensional packet-local bottleneck: outcome is decodable from packet states, but the preregistered packet-span interchange does not establish a causal transfer window.

G14 then discovered a late answer-site pattern but failed its inherited composite gate by a narrow representation-threshold miss. It motivated a refined recipient-conditioned hypothesis.

G15 prospectively preregistered that refinement on a fresh donor assignment and confirmed a late causal answer-position state:

- fresh behavior: +18.84pp [12.94, 24.97];
- causal transfer at layers 29–47: +6.52 to +9.04pp;
- up to 48% behavioral-effect recovery;
- bidirectional transfer;
- matched orthogonal direction near zero.

Safe conclusion:

> **In the strong-effect model, future-outcome influence becomes causally actionable after recipient contextualization in a late answer-position decision state rather than through the tested one-dimensional packet-local bottleneck.**

## What the paper does not claim

- not the first observation that LLMs know a temporal rule but violate it;
- not universal failure across models/tasks;
- not cross-source replication;
- not a generic irrelevant-context paper;
- not robust strong-form outcome entrainment across all models;
- not “changing only the abstract outcome” in G12;
- not a dedicated hindsight circuit;
- not proof that a clean ex-ante representation is absent or overwritten;
- not fidelity to an external objective ex-ante forecast.

## What failed and why it matters

The project keeps preregistered failures rather than smoothing them away.

- the original *Unring the Bell* directional hypothesis reversed;
- broad perspective-family qualification failed;
- FOMC external-source qualification failed;
- G5 deliberation was an instrument/design failure;
- G7 external ex-ante-anchor prediction failed in the opposite direction;
- G13 packet-local causal bottleneck was not supported;
- G14's inherited composite gate failed before G15 prospectively confirmed the refined recipient-conditioned hypothesis.

See [`RESEARCH_HISTORY.md`](RESEARCH_HISTORY.md) for the full scientific transition.

## Current research decision

For an ACL/EMNLP/NAACL Main submission, the experimental program is sufficiently complete. The default is now **paper consolidation: introduction, related work, figures, tables, limitations, and adversarial reviewer simulation**.

The one unresolved higher-level mechanistic question is:

> **Why does an information boundary the model can represent/recognize fail to gate the late outcome pathway?**

A new experiment should run only if it prospectively distinguishes competing algorithms that all explain the evidence through G15. Do not add another prompt, benchmark, model, redaction, CoT, mitigation, or scale sweep merely for reviewer defense.

## Reproduction and provenance

See [`REPRODUCE.md`](REPRODUCE.md) for execution entry points. Frozen preregistrations and transformation contracts define historical experimental decisions; do not retrospectively rewrite them to fit the current narrative.
