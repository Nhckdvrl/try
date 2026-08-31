# Current paper plan: hindsight contamination in LLM historical reasoning

This document replaces the older cross-boundary *Information-Set Reasoning*
roadmap. That broader program was narrowed after the perspective-family pilot
failed qualification and the FOMC source did not pass its preregistered
qualification gate.

The current paper is temporal and asks:

> **After a model has seen what happened later, can it still reconstruct the
> judgment that should have been made using only what was knowable at the time?**

## 1. Primary claim

The paper's central claim is a **recognition–enforcement gap**:

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

### P1 — explicit-verdict redaction

The strongest depth result is that contamination survives removal of explicit
YES/NO verdict sentences from the future packet while the remaining evidence
retains strong allowed-frame leverage.

Permitted claim:

> **The effect is not reducible to copying an explicit resolution label.**

The increase in contamination after redaction was unanticipated and should be
reported without a mechanism claim.

### P2 — within-family size analysis

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

The main text should be organized around three claims only:

1. **Recognition–Enforcement Gap.** Near-perfect temporal-boundary recognition
   coexists with substantial causal hindsight contamination.
2. **Not explicit-label copying.** The effect survives removal of explicit
   resolution-verdict sentences while remaining evidence stays useful.
3. **Not solved by scale.** Within Qwen3.5, larger checkpoints do not
   monotonically reduce contamination despite saturated recognition.

The following are explicitly **not** paper claims:

- universal failure across LLMs or tasks;
- cross-source replication;
- a general information-set reasoning capability/failure;
- a neural mechanism or representation-overwriting story;
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
3. verdict-redaction depth test;
4. Qwen3.5 size analysis;
5. clearly labelled non-headline results / failed external attempt.

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
- no internal-mechanism claim.

## 6. Remaining work

The experimental program is effectively complete for the current submission.
Remaining work is primarily consolidation:

1. freeze the paper-level claim table and terminology;
2. build Figure 1 around the 2×2 design + recognition/enforcement result;
3. build Figure 2 for 64→256 replication and cross-model effects;
4. build Figure 3 / table for verdict redaction and the Qwen size analysis;
5. draft Introduction and Related Work around the locked novelty boundary;
6. move exploratory controlled-suite history and failed source engineering to
   the appendix / repository rather than the main narrative;
7. run a final adversarial ACL/EMNLP reviewer simulation before deciding whether
   any new experiment is actually necessary.

No new manipulation, source, or mechanism experiment should be added merely to
make the paper look larger.