# Next experiments after novelty reset

**Status:** design document, not yet a preregistration.
**Purpose:** replace the obvious "semantic target information helps" story with direct
tests of two less obvious computational claims.

No generation is authorized by this document. Freeze each round separately before
running.

---

# G20 — Binding Deadline / Late Target Revelation

## Scientific question

> **If a target becomes semantically identifiable after an exclusion rule has already
> been processed—but still before the actual evidence arrives—can the model
> retroactively bind the earlier rule to that target?**

The obvious account predicts yes: if semantic target information is simply useful
context, it should help whenever it arrives before the decision.

The **binding-deadline** account predicts no: the target must be available when the
rule is processed; later revelation will not fully repair the rule unless the rule is
processed again.

## Materials

Build a new set:
- **120 fresh items**
- **36 independent skeletons**
- 3 families: legal judgment / evidence inference / ranking-selection, 40 each
- no item or skeleton overlap with G0/G18

Each item has a matched paraphrase P of the critical proposition and a matched
unrelated statement U. P and U should be length-matched within a narrow token tolerance
for every tested tokenizer.

## Core permutation design

Use a fixed skeleton:

BLOCK1 → RULE1 → BLOCK2 → POLICY-SLOT → EVIDENCE → QUESTION

The evidence is always after the rule.

### PRE-BIND
P → RULE → U → neutral-slot → E

### LATE-BIND
U → RULE → P → neutral-slot → E

The rule and evidence occupy approximately the same positions. Only whether the
matching target proposition appears before or after the rule changes.

### PRE-BIND + REPLAY
P → RULE → U → RULE(replay) → E

### LATE-BIND + REPLAY
U → RULE → P → RULE(replay) → E

The second rule is byte-identical to the first. In no-replay conditions, POLICY-SLOT
contains a length-matched neutral policy-status block.

This yields a clean 2×2:
- target available before first rule: yes / no
- rule reprocessed after both blocks: yes / no

## Strong explicit-link condition

A separate diagnostic makes the late mapping maximally clear:

U → RULE → "The following statement is exactly the information referred to by the
preceding rule:" + P → E

Use a matched pre-bind control with the same linking language before the rule.

If even explicit late resolution fails, "the model did not realize P was the target"
becomes a much weaker alternative.

## Controls

### Admit control

Repeat the same order/replay factorial with the matched Admit rule.

Purpose: show that any deadline is specific to exclusion/control rather than a generic
cost of moving a relevant proposition across the rule.

### Arithmetic control

On a compact subset, use the already validated explicit arithmetic task with a future
symbolic target mapping.

Purpose: show that the models can combine an earlier rule with a later target
definition when the operation is explicitly computable.

### Masked-diffusion control

Run Dream/LLaDA on the core PRE vs LATE comparison if their prompt/readout setup
supports the new materials.

This is important because in a bidirectional prompt encoder, the result cannot be
dismissed as "earlier rule tokens cannot attend to later target tokens."

## Model panel

Primary:
- Qwen3-8B
- Gemma-3-12B
- Phi-4-mini
- Qwen3.5-27B
- Mistral-Small-24B

Architecture control:
- Dream-7B
- LLaDA-8B

## Estimand

Use raw sign-aligned rating points with per-order no-rule baselines, exactly as learned
from Stage 3E/G18.

For each target-order/replay cell:

ExclusionEffect = marginal evidence effect without exclusion − marginal effect with
exclusion.

Primary contrast:

DeadlineGap = EE(PRE-BIND, no replay) − EE(LATE-BIND, no replay)

Primary replay result:

LateReplayRescue = EE(LATE,replay) − EE(LATE,no replay)

The binding-deadline account predicts:
- DeadlineGap > 0
- replay preferentially rescues LATE and strongly shrinks the PRE/LATE gap.

## Success pattern required for a main claim

Do not set a numeric threshold until a pilot-free design audit confirms the new
rating-point scale.

The scientific pattern required:
1. PRE-BIND > LATE-BIND in pooled EE with CI excluding zero;
2. direction positive in at least 4/5 instruct models;
3. LATE-BIND + replay materially restores exclusion and closes a large share of the
   PRE/LATE gap;
4. Admit order effect is substantially smaller;
5. if diffusion models are available, at least one preserves the core PRE>LATE effect.

## What would kill the story

If LATE-BIND is approximately as effective as PRE-BIND, the normal explanation wins:
semantic target information helps whenever it appears before decision time. Do not use
"binding deadline" language.

If replay adds equal benefit to PRE and LATE without closing the gap, the specific
"recompile after target resolution" account is unsupported.

---

# G21 — Source-Scope Collapse / Semantic Spillover

## Scientific question

> **When an exclusion rule is scoped to one evidence source or occurrence, does
> successful semantic binding preserve that scope—or does suppression spread to
> independently admissible evidence expressing the same proposition?**

This is motivated by the G18 below-baseline result but tests source precision directly.

## Natural intuition

If Source A is inadmissible but Source B independently reports the same fact, a
source-scoped policy should remove A's contribution while preserving B's.

A model that instead suppresses B has confused:
- **the evidence instance that is excluded**
with
- **the proposition that the evidence expresses**.

That is a qualitatively different failure.

## Materials

Build **100 fresh dual-source items / 30–36 skeletons / 3 families**.

Each item has:
- Base context;
- critical proposition p;
- Source A statement A(p);
- Source B statement with one of five semantic relations to A:
  1. exact paraphrase / mutual entailment;
  2. B more specific but entails p;
  3. gist only;
  4. lexical overlap, different proposition;
  5. unrelated control.

A and B must be explicitly framed as **independent sources**.

## Policy

Prospective source-scoped rule:

> **Evidence from Source A is excluded and must have zero evidential weight. Evidence
> from other sources, including Source B, remains fully admissible and should retain
> its normal evidential weight.**

Use an identifier version and a meaningful-provenance version in secondary analyses,
but the primary claim is source scope, not ID wording.

## Core conditions

For every semantic relation:
1. Base
2. B only, no exclusion policy
3. A only + exclusion policy
4. A + B + exclusion policy
5. A + B + explicit B-admissible reminder
6. A + B, no exclusion policy

The critical comparison is not whether A is suppressed. It is whether **B survives**
when an excluded A expresses semantically equivalent content.

## Metric

Define B's independent leverage:

BLeverage = Y(B only) − Y(Base)

Define B's retained leverage under source-scoped exclusion:

BRetained = Y(A+B+ExcludeA) − Y(A+ExcludeA)

Primary spillover:

Spillover = BLeverage − BRetained

Positive Spillover means the allowed Source B loses influence merely because the
excluded Source A carries related content.

Primary semantic contrast:

SemanticSpillover = mean(Spillover[para, entail]) −
mean(Spillover[lexical-wrong, unrelated])

The explicit-B-admissible condition asks whether the error survives a direct statement
that Source B remains valid evidence.

## Strongest possible result

A compelling pattern would be:
- A is successfully excluded;
- B alone has large leverage;
- B's leverage collapses only when B expresses the same proposition as excluded A;
- lexical overlap without proposition identity does not cause collapse;
- explicitly saying "Source B remains admissible" does not fully restore it.

That would directly establish **semantic scope collapse**.

## Model panel

Same five-model panel as G18/G20.

If the effect is broad, add the two masked-diffusion models only if the source-labelled
format is supported cleanly.

## Agent transfer

If the controlled result passes, reproduce it in a real SYSTEM→TOOL setting:

- SYSTEM: Source/Document D7 is disallowed; D9 remains allowed.
- TOOL D7: proposition p
- TOOL D9: paraphrase of p
- assistant decision

The correct behavior is to preserve D9's independent evidence contribution.

This turns the earlier D7→D9 result on its head: the question is no longer whether a
semantic policy can follow content; it is whether a **source-scoped** policy improperly
follows content when it should not.

## Mechanism follow-up — only after behavioral confirmation

Use a matched pair:

SUCCESSFUL SCOPE:
- Source A excluded;
- Source B carries unrelated/different proposition.

SCOPE COLLAPSE:
- identical policy/source structure;
- Source B is a paraphrase of A's proposition.

Candidate tests:
1. patch rule-span states to see whether semantic equivalence changes the same
   mid-network control state;
2. patch Source-B content span vs Source-B source-label span at decision time;
3. test whether causal effects track proposition identity more strongly than source
   identity.

The mechanism claim would be:

> the control state is semantically keyed strongly enough that it overrides provenance
> scope.

Do not run this unless the behavioral scope effect is real.

---

# Recommended sequence

## First: G20

Why:
- it directly tests whether the old normal "semantic info helps" explanation is wrong;
- it is tightly predicted by the existing Stage-5 rule-state result;
- a null result is highly informative and prevents overclaiming.

## Second: G21

Why:
- it tests the most surprising implication of G18's oversuppression;
- it creates a real-world source/provenance failure rather than another prompt
  specificity study;
- it can become the new centerpiece if the effect is strong.

## Do not run

- the cancelled ReGround G19 design;
- more semantic-preview ladders;
- more model-size breadth;
- another generic reminder/restatement experiment;
- another "identifier vs proposition" comparison without source-scope stakes.

The next paper-quality gain must come from **a new phenomenon**, not another robustness
table.
