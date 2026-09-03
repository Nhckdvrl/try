# Paper frame — authoritative scientific register

**Updated:** 2026-09-03

This file defines what the paper is about. Historical development is in `RESEARCH_HISTORY.md`; submission-quality standards are in `ACL_EMNLP_ALIGNMENT_STANDARD.md`.

## 1. Natural question

> **After learning how something turned out, can a language model still condition a reconstructed past judgment only on the information that was available beforehand?**

This wording deliberately avoids claiming that our target is the objectively “reasonable” or externally correct ex-ante belief. G7 showed that the uncontaminated model judgment is only weakly aligned with BTF-3's independent ex-ante forecast.

## 2. Scientific object

**Retrospective epistemic reconstruction / information-set conditioning under hindsight.**

The object is the operation of producing a judgment as if conditioned only on an earlier information set while the reasoner currently possesses later information.

BTF-3 is a natural measurement window for this operation, not the paper's identity.

## 3. Core established phenomenon

On 256 fresh natural forecasting questions, the three primary open checkpoints:

- recognize per item, at 99.2–100%, that the supplied resolution evidence postdates the target historical cutoff;
- nevertheless allow that evidence to shift the reconstructed ex-ante probability by 7.46–27.73 points;
- remain sensitive after explicit resolution-verdict sentences are removed;
- show no monotonic disappearance of the effect over tested Qwen3.5 4B/9B/27B checkpoints.

The main behavioral dissociation is therefore:

> **boundary recognition does not imply causal enforcement of that boundary in the judgment.**

This is not claimed as a priority result by itself; temporal leakage and rule-knowledge/behavior gaps already exist in prior work.

## 4. The explanatory descent

### 4.1 From target evidence to unrelated outcome-shaped evidence

G8 replaces the recipient's own future packet with a packet from a different resolved question. Foreign packets still induce substantial absolute movement (50.7–100.1% of real-packet movement) and donor-directed pull.

G8's continuous donor-pull estimates are positive in all three primary models, but only one clears the preregistered 5pp strong-form threshold; the frozen panel row is therefore weak/heterogeneous, not universally strong.

### 4.2 Explicit verdict copying is insufficient

G11 removes explicit YES/NO verdict sentences from those foreign packets. Donor pull retains 73.9% in Qwen and 67.1% in Gemma, but only 35.0% in Mistral. The preregistered panel verdict is `survives` (2/3).

Safe claim:

> **Outcome-shaped future evidence from another resolved event can directionally pull the reconstructed judgment even when explicit verdict copying is insufficient to explain the effect.**

We use **retrospective outcome entrainment** as an operational name for this regularity. The paper's deeper object remains retrospective epistemic reconstruction.

### 4.3 Direct within-recipient directional intervention

G12 keeps the recipient history and all non-packet prompt material fixed, but replaces a verdict-redacted irrelevant future packet supporting NO with a different verdict-redacted irrelevant future packet supporting YES.

Paired shifts:

- Qwen: +4.41pp
- Gemma: +17.50pp
- Mistral: +1.55pp

All move in the same direction, but magnitude is strongly model-dependent and the frozen 5pp panel gate is indeterminate.

**Do not write “changing only the donor outcome.”** The YES-supporting and NO-supporting packets differ in packet identity, event semantics, lexical content, and other properties. The supported result is that **outcome-shaped evidence class controls direction**, not that an abstract outcome bit was isolated holding all packet semantics fixed.

## 5. Mechanistic discrimination

The behavioral evidence motivates two internal accounts with similar output predictions:

1. **packet-local transport:** donor outcome is compressed into a shared packet-local scalar and carried to the answer;
2. **recipient-conditioned decision-state construction:** packet semantics are integrated with the recipient question before a causal outcome coordinate appears.

### G13 — packet-local scalar test

Donor outcome is decodable from packet states, but the preregistered one-dimensional packet-span interchange does not establish a causal transfer window.

Safe conclusion:

> **The tested donor-general one-dimensional packet-local bottleneck is not supported.**

Do not generalize this to “packet representations are non-causal.”

### G14 → G15 chronology

G14 discovered a late answer-position transfer pattern but failed its inherited composite gate because the global representation criterion missed threshold by 0.008. That result motivated a refined **recipient-conditioned paired estimand**.

G15 preregistered that refinement before fresh outputs/activations and rebuilt a fresh donor assignment. It confirmed:

- fresh behavioral contrast: +18.84pp [12.94, 24.97];
- strong late-layer within-recipient paired ordering;
- causal transfer of +6.52 to +9.04pp at layers 29–47;
- up to 48% recovery of the behavioral contrast;
- correct transfer in both directions;
- matched orthogonal direction near zero.

Safe mechanism claim:

> **In the strong-effect model (Gemma), future-outcome influence becomes causally actionable after recipient contextualization in a late answer-position decision state rather than through the tested one-dimensional packet-local bottleneck.**

This does **not** establish a dedicated hindsight circuit and does **not** establish whether a clean ex-ante state was built earlier and later overwritten.

## 6. What failed or narrowed the paper

These results remain visible but do not form equal-weight main sections:

- **G3:** changing the stated reason for exclusion does not reduce intrusion at panel level; this weakens a specifically temporal-reason account but does not prove the model internally disbelieved the “unreliable” packet.
- **G5:** deliberation/state-scaffold instrument failure; indeterminate.
- **G6:** masking localized access but did not distinguish clean-state override from absence; excluded from the main mechanism claim.
- **G7:** preregistered external ex-ante-anchor prediction failed in the opposite direction; external-fidelity claim is dropped.
- **G9:** second task did not qualify.
- **G10:** heterogeneous/indeterminate mitigation result.
- **FANToM:** perspective-family pilot failed qualification.
- **FOMC:** external-source attempt failed its preregistered qualification gate.

Failures are provenance and limitation evidence, not material to be hidden.

## 7. Novelty boundary

The paper is **not**:

- the first evidence that LLMs use future information;
- the first recognition–behavior gap for temporal rules;
- another irrelevant-context robustness paper;
- a generic “hindsight bias in LLMs” benchmark paper;
- a universal information-set reasoning claim.

The distinctive explanatory sequence is:

```text
recognized information boundary
    ↓
unlicensed future evidence still causally changes the same reconstructed judgment
    ↓
unrelated outcome-shaped future evidence induces donor-directed pull
    ↓
outcome-class replacement controls direction, heterogeneously across models
    ↓
in Gemma, influence becomes causally actionable in a late recipient-conditioned answer state
```

## 8. Scope of the main paper

The primary positive natural substrate is BTF-3. Scope should be stated as:

> **evidence for retrospective information-set conditioning failure in one natural retrospective-forecasting substrate, with mechanistic analysis in the strong-effect model.**

Do not write “universal mechanism of hindsight reasoning.”

## 9. Main-vs-Outstanding assessment

Against the reference papers in `ACL_EMNLP_ALIGNMENT_STANDARD.md`, the current project is **Main-shaped** because it has:

- a natural question independent of the benchmark;
- prospectively replicated causal behavioral evidence;
- an explanatory move below generic temporal leakage;
- a direct directional intervention;
- a prospectively confirmed mechanistic discrimination between internal-site accounts.

The unresolved explanatory closure is:

> **Why does a boundary the model can represent/recognize fail to gate the late outcome pathway?**

G15 explains where/how outcome influence becomes causally actionable, not why recognized admissibility fails to control that pathway.

## 10. Standing rule for new experiments

The default is **stop experiments and write the paper**.

A new experiment is permitted only if, before running it, we can state two algorithms that both explain every result through G15 but make opposite causal predictions under one clean intervention.

The only currently justified high-ambition branch is **boundary representation × outcome pathway**. Candidate conceptual accounts include:

- a real causal gate that is too weak or bypassed;
- parallel boundary-recognition and outcome-integration computations whose decision readout favors the latter;
- a recognition/readout representation that is probe-accessible but causally irrelevant to the historical judgment.

If an experiment cannot distinguish such accounts, it is another condition rather than another explanation and should not run.

## 11. Sentences the paper must not write

- “We are the first to show that LLMs know a temporal rule but violate it.”
- “Changing only the donor outcome causes the effect.”
- “We establish robust outcome entrainment across models.”
- “We discovered a dedicated hindsight axis/circuit.”
- “Future evidence contaminates the past through *the* mechanism ...” without the Gemma/late-state qualification.
- “The packet moves models away from a competent ex-ante forecast.”
- “A clean ex-ante representation is absent/overwritten.”
