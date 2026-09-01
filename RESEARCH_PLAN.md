# Current paper plan: hindsight contamination in LLM historical reasoning

This document replaces the older cross-boundary *Information-Set Reasoning*
roadmap. That broader program was narrowed after the perspective-family pilot
failed qualification and the FOMC source did not pass its preregistered
qualification gate.

The current paper is temporal and asks:

> **After a model has seen what happened later, can it still reconstruct the
> judgment that should have been made using only what was knowable at the time?**

## 1. Primary claim and explanatory step

The replicated starting phenomenon is a **recognition–enforcement gap**:

> Language models can correctly identify that future evidence lies outside the
> target historical information set while nevertheless allowing that same
> evidence to causally shift their reconstructed ex-ante judgment.

The causal estimand is `OutOfSetIntrusion`, measured by supplying or withholding
one fixed future packet while keeping the question and historical context
unchanged.

The paper does **not** claim priority over the general observation that models can
state a temporal rule correctly and still violate it. The novelty is the
within-item causal manipulation and continuous effect measurement on hundreds of
independently sampled natural forecasting questions.

The paper's forward contribution is the lower-level phenomenon isolated beneath
that gap:

> **Retrospective outcome entrainment:** outcome-shaped future context pulls a
> reconstructed past judgment toward the outcome it supports even when the
> context concerns a different question and contains no explicit verdict.

This is the ACL-shaped explanatory step: observed hindsight contamination → a
controlled, donor-directed regularity. The paper is not organized around a list
of alternative explanations that were eliminated.

## 2. Evidence hierarchy

### P0 — large-scale replication of the main phenomenon

This is the paper's strongest result.

- discovery pilot: 8 BTF-3 units;
- preregistered confirmation: 64 fresh units;
- preregistered large replication: 256 additional fresh units, balanced 128 YES
  / 128 NO;
- 256-unit round: 3/3 models qualify and 3/3 clear the 5-point intrusion SESOI;
- boundary recognition remains 99.2–100% while intrusion ranges from 7.46 to
  27.73 probability points.

Primary paper reporting should lead with the 256-unit replication. The 64-unit
round establishes prospective confirmation and cross-round stability; the 8-item
pilot is discovery history, not primary evidence.

### P1 — retrospective outcome entrainment (G8 + G11)

G8 replaces each question's packet with the packet from a different question.
Foreign packets produce 50.7–100.1% as much absolute movement as real packets;
donor pull is positive with intervals above zero in all three models
(2.93–12.26 points). The frozen strong-form rule requires a 5-point mean, so
G8's preregistered panel row is `H-presence-weak`, not strong.

G11 removes explicit verdict sentences from the same foreign packets. Qwen and
Gemma retain 73.9% and 67.1% of donor pull; Mistral retains 35.0%. The
preregistered panel verdict is `survives` (2/3, all qualified).

Permitted headline claim:

> **An irrelevant question's outcome evidence can pull a reconstructed past
> judgment toward that question's outcome; explicit verdict copying is
> insufficient to explain the effect.**

### P2 — donor outcome is a within-question causal variable (G12)

Holding the recipient history and all non-packet tokens fixed, replace a
verdict-redacted packet supporting NO with one supporting YES. The same
judgment rises by +4.41pp in Qwen, +17.50pp in Gemma, and +1.55pp in Mistral;
all intervals exclude zero, while the frozen 5pp panel gate is indeterminate.
The paper reports both: direction is controlled across models, magnitude is
model-dependent.

### P3 — recipient-conditioned late decision state (G15)

On a fresh donor assignment, Gemma reproduces the behavioral contrast
(+18.84pp [12.94, 24.97]). A donor-general answer-position outcome coordinate
orders 79.7–98.4% of held-out pairs from layers 23–47. Causal interchange is
near zero in early layers and transfers +6.52 to +9.04pp at layers 29–47,
recovering up to 48% of the behavior; bidirectionality and orthogonal-axis
specificity both pass. This supports contextual decision-state construction
over packet-local scalar transport.

### Supporting — own-packet explicit-verdict redaction

The strongest depth result is that contamination survives removal of explicit
YES/NO verdict sentences from the future packet while the remaining evidence
retains strong allowed-frame leverage.

Permitted claim:

> **The effect is not reducible to copying an explicit resolution label.**

The increase in contamination after redaction was unanticipated and should be
reported without a mechanism claim.

### Characterization — within-family size analysis

Qwen3.5 4B / 9B / 27B all show near-ceiling boundary recognition and all clear
the intrusion SESOI on the same 256 items. Intrusion is non-monotone
(32.00 → 16.02 → 36.75).

Permitted claim:

> **There is no evidence that scale alone removes hindsight contamination within
> the available dense Qwen3.5 checkpoints.**

Do not fit a scaling law, slope, or cross-family conclusion to three size points.

### Secondary — positional reminder effect

The 64-unit factorization round found that an identical exclusion reminder is
more effective after future evidence than before it for Qwen and Gemma. The raw
pattern appears again on 256 items, but the preregistered G2 panel gate fails
because Qwen is formally disqualified by a probe failure in another G2 condition,
and the licensed-frame specificity control is not supportive.

Therefore this result is **descriptive / hypothesis-generating**, not a headline
replicated mechanism.

## 3. Boundaries that must remain visible

### FOMC

The FOMC v0.1a pilot is sealed as `inconclusive / not validated`. Positive point
estimates do not override the failed preregistered source-qualification gate.
The paper may report it as a failed external-source replication attempt, but not
as cross-source support.

### FANToM

The perspective pilot failed qualification. It is historical evidence against a
broad multi-family claim and should not be revived merely to widen the paper.

### Packet factuality

A preregistered, hash-fixed 64-item external factuality audit found 63 PASS, 1
material source/specification error, and 0 unverifiable items. The error does not
materially affect any primary estimate, but the audit cannot certify the full
256-item source as factually perfect.

### Closest temporal neighbour

Recent temporal-legal reasoning work already shows that models can know the
applicable temporal rule yet apply the wrong statute vintage. We therefore do not
claim to be first to observe recognition without obedience. Our distinction is
the same-evidence causal manipulation and measured probability shift.

## 4. Paper claim set

The main text should be organized around one phenomenon, its causal
factorization, and one algorithmic explanation:

1. **Recognition–Enforcement Gap.** Near-perfect temporal-boundary recognition
   coexists with substantial causal hindsight contamination.
2. **Retrospective Outcome Entrainment.** Outcome-shaped future context causes
   donor-directed influence even when it belongs to another question; in two
   of three models the influence survives explicit-verdict redaction.
3. **Late Contextual Decision State.** In the strong-effect model, future
   outcome information is not causally transported as a packet-local scalar;
   after integration with the recipient question it forms a late decision
   coordinate whose interchange transfers the judgment on a fresh assignment.

Verdict redaction on own packets, size, breadth, and exclusion reasons are
supporting characterization. They are not equal-weight headline claims.

The following are explicitly **not** paper claims:

- universal failure across LLMs or tasks;
- cross-source replication;
- a general information-set reasoning capability/failure;
- absence or overwriting of a clean ex-ante representation;
- a replicated exclusion-specific positional mechanism;
- a scaling law;
- complete factual validation of all BTF-3 packets.

## 5. Planned paper structure

### Introduction

Motivate historical reconstruction: auditing past decisions, evaluating prior
forecasts, and asking what was reasonable to believe at an earlier time. State
the core difficulty: the model currently possesses information that should not
belong to the reconstructed historical information state.

Introduce the causal design before naming datasets. The conceptual punchline is:

> **recognition of a temporal boundary is not sufficient for behavioral
> enforcement of that boundary.**

### Method

- BTF-3 source and transformation contract;
- 2×2 packet-presence × admissibility design;
- boundary probes;
- `Responsiveness`, `OutOfSetIntrusion`, and paired bootstrap inference;
- prospective sampling, freeze tags, and qualification rules.

### Results

1. 64-unit confirmation and 256-unit large replication;
2. recognition vs enforcement dissociation;
3. G8 relevance × donor-outcome intervention;
4. G11 explicit-verdict decomposition of donor pull;
5. G12 paired causal manipulation of donor outcome;
6. G15 fresh-confirmed late decision-state mechanism;
7. compact characterization and transparent boundaries.

### Related work

Lead with ExAnte / temporal leakage and the recent temporal-legal neighbour.
Then distinguish in-context forgetting, hindsight/outcome bias, irrelevant
context, and security information-flow work.

### Limitations

- primary positive evidence is one natural source;
- FOMC failed its preregistered gate;
- source-native resolution packets may contain defects;
- redacted evidence can still entail the outcome;
- only open checkpoints are tested;
- mechanism is established in Gemma only and does not prove prior construction
  or overwriting of a clean ex-ante state.

## 6. Remaining work

The experimental program is closed after the fresh-confirmed G15 mechanism.
Remaining work is consolidation:

1. freeze the paper-level claim table and terminology;
2. build Figure 1 around the natural question, 2×2 design, and replicated gap;
3. build Figure 2 as the explanatory figure: real packet → foreign packet →
   verdict-redacted foreign packet, with own- and donor-direction arrows;
4. build the mechanism figure as packet-site non-transfer versus late
   answer-site causal transfer, led by the fresh confirmation;
5. move scale, G3, G13/G14 development history, and failed interventions to
   compact tables / appendix;
6. draft Introduction and Related Work around the locked novelty boundary;
7. move exploratory controlled-suite history and failed source engineering to
   the appendix / repository rather than the main narrative;
8. run a final adversarial ACL/EMNLP reviewer simulation of the locked paper.

No defensive experiment is added merely to answer a possible reviewer objection.
No new experiment runs unless the locked headline claim itself is found invalid.
