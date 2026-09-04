# Next experiments after mainline audit — v3

**Status:** design document only, not a preregistration.
**Updated:** 2026-09-04 after the mainline audit that downgraded G21.

The next experiment must explain the original G0 reversal:

> the same exclusion rule is weaker before evidence than after evidence.

G21 Source–Proposition Scope Entanglement is no longer the current paper-defining
experiment because it asks a different question about scope precision.

The active hypothesis is now:

> **LLMs may construct a target-conditioned exclusion state when the rule is processed,
> rather than storing a deferred exclusion operator that is reliably composed with a
> target once that target becomes available later.**

Equivalent behavioral hypothesis:

> **target → EXCLUDE and EXCLUDE → target are not equivalent.**

No generation is authorized by this document.

---

# Priority 1: G20 v3 — Deferred Control Composition

## Scientific question

> **If an exclusion rule is processed before its semantic target is resolved, can the
> model later compose the two once the target becomes available, before the governed
> evidence arrives?**

This directly explains G0 if true.

Retrospective G0:

```
target evidence → EXCLUDE → decision
```

Prospective G0:

```
EXCLUDE → target evidence → decision
```

G18 already shows that giving target semantics before the rule can rescue prospective
exclusion while the actual evidence remains later.

G20 v3 tests the missing direction:

> does target information revealed **after** the rule reconstruct the same effective
> control?

## Why v3 is stronger than the old binding-deadline design

A decoder-only model's earlier rule-token state cannot attend to later target tokens.
That fact is trivial.

Therefore the decisive test must occur at a point where **both target and rule are
already in context**.

G20 v3 inserts a shared post-resolution checkpoint before the governed evidence.

## Materials

Fresh set:
- 120 items / 36 skeletons / three families;
- legal judgment;
- evidence inference;
- ranking / selection;
- no overlap with G0/G18 skeletons.

Each item contains:
- a semantic target preview `P`;
- a length-matched unrelated neutral block `U`;
- an exclusion rule `X`;
- a byte-identical neutral checkpoint `C`;
- later actual evidence `E`, semantically matched to `P`;
- final decision question.

`P` is explicitly non-evidential metadata / preview. Each order receives its own
no-rule baseline, as in G18.

## Core order factor

### TARGET-FIRST

```
P → X → U → C → E → question
```

### RULE-FIRST

```
U → X → P → C → E → question
```

`P` and `U` must be tokenizer-length matched closely enough that `C` lands at the
same or nearly identical token position.

At `C`, both arms have already seen:
- the same target semantics;
- the same exclusion rule;
- the same neutral block.

Thus any remaining order effect is not merely “the earlier rule token cannot see the
future.” The model now has a downstream position from which all required information is
available.

## Mandatory late-target comprehension

On an independent full-context probe for RULE-FIRST, ask which later proposition/item
the earlier exclusion rule applies to.

The main claim requires high accuracy.

A stronger trajectory-level variant should also be prepared:

> after `P`, require or observe an explicit resolved-target statement, then test
> whether later `E` is still causally used.

This directly tests:

> late target resolution can be correct while causal control remains wrong.

## Rule reprocessing factor

### RULE-FIRST + RULE-REPLAY

```
U → X → P → X → C → E
```

### TARGET-FIRST + RULE-REPLAY

```
P → X → U → X → C → E
```

Use matched neutral material in no-replay cells.

The critical effect is not “repetition helps.” It is:

> **reprocessing X after P should preferentially repair RULE-FIRST.**

Primary replay interaction:

```
[EE(RULE-FIRST+REPLAY) - EE(RULE-FIRST)]
-
[EE(TARGET-FIRST+REPLAY) - EE(TARGET-FIRST)]
```

## Target-replay control

If feasible, include:

```
U → X → P → P → C → E
```

with a matched replay in TARGET-FIRST.

This distinguishes:
- missing target salience;
- missing reapplication of the exclusion operator.

Strong pattern:

> rule replay repairs substantially more than target replay.

## Positive deferred-composition controls

At least two should be present.

### 1. Admit / use-select control

Use the same unresolved target relation, but require the later matched item to be used
or admitted.

If RULE-FIRST works here while exclusion fails, the result is not generic inability to
late-bind a target.

### 2. Arithmetic control

Earlier rule defines a weight/operation over a future variable; later `P` resolves the
variable before the numeric evidence arrives.

Existing Stage 3C already shows exact prospective arithmetic weighting in 4/5 models;
the new control should preserve the same temporal structure as G20 where feasible.

### Optional 3. Routing/select control

Earlier rule:
> when the item matching target X appears, select/use it.

Later `P` defines X.

This is another positive late-composition task without semantic nullification.

## Behavioral estimands

Use sign-aligned raw rating points and a no-rule baseline for each order.

`ExclusionEffect` as in G18.

Primary:

```
CompositionOrderGap = EE(TARGET-FIRST) - EE(RULE-FIRST)
```

Replay:

```
ReplayRescueRuleFirst =
EE(RULE-FIRST+RULE-REPLAY) - EE(RULE-FIRST)
```

Specific replay interaction:

```
SpecificReplayInteraction =
[EE(RULE-FIRST+RULE-REPLAY) - EE(RULE-FIRST)]
-
[EE(TARGET-FIRST+RULE-REPLAY) - EE(TARGET-FIRST)]
```

If target replay is included:

```
OperatorReplayAdvantage =
ReplayRescue(rule replay) - ReplayRescue(target replay)
```

## Post-resolution checkpoint mechanism

This is the most important redesign.

Capture the residual state at the identical checkpoint `C`.

By `C`, both orders contain all necessary information.

### Behavioral qualification

Only mechanism-analyze models where:
- target comprehension is high;
- TARGET-FIRST > RULE-FIRST behavior is present.

### Causal interchange

At selected layers / relative-depth windows:

1. TARGET-FIRST `C` → RULE-FIRST recipient;
2. RULE-FIRST `C` → TARGET-FIRST recipient;
3. identical interchange in Admit/control arms.

The ideal result:

- target-first checkpoint state rescues rule-first suppression;
- rule-first checkpoint state breaks target-first suppression;
- Admit/control interchange is much smaller or opposite;
- after rule replay, RULE-FIRST checkpoint becomes less distinguishable causally from
  TARGET-FIRST.

This would license:

> **The order in which target semantics and exclusion are composed leaves a causal
> history-dependent control state even after both are available.**

That is stronger than earlier rule-token localization and avoids the trivial causal-mask
claim.

## Relation to existing Stage 5

Stage 5 already proves:
- target-dependent rule state;
- mid-network localization;
- causal effect before later evidence;
- replication in Qwen3-8B and Mistral-Small-24B.

G20 v3 should not re-discover a layer window.

Its new mechanism question is:

> **does the control state converge after late target resolution, or does the earlier
> composition order remain causally encoded?**

## Masked diffusion

Dream/LLaDA remain useful architecture controls.

They are no longer solely responsible for defeating the causal-mask objection because
the shared checkpoint is downstream of both operands.

Still, replication in at least one bidirectional masked-diffusion LM would strengthen
the claim that this is a learned control strategy rather than a decoder-only quirk.

## Main-claim requirements

G20 v3 becomes the novelty-bearing paper result only if most of the following hold:

1. RULE-FIRST target comprehension is high.
2. TARGET-FIRST > RULE-FIRST exclusion on the fresh set.
3. Rule replay selectively repairs RULE-FIRST.
4. Preferably, rule replay beats target replay.
5. Admit/arithmetic/routing late composition works substantially better.
6. The post-resolution checkpoint remains causally order-dependent.
7. The pattern is not confined to one model family.

## What kills G20 v3

Kill or demote the composition story if:
- RULE-FIRST ≈ TARGET-FIRST;
- late target mapping itself is poorly understood;
- replay helps both orders equally;
- target replay helps just as much as rule replay;
- matched positive operations fail in the same way;
- checkpoint interchange has no exclusion-specific causal effect.

---

# G21 — Source–Proposition Scope Entanglement

## Status: DOWNGRADED / NOT CURRENTLY AUTHORIZED

The design remains scientifically interesting:

> excluding Source A may suppress an allowed Source B when B expresses the same
> proposition.

But it does not explain the original G0 prospective reversal.

Therefore:
- do not run it as the next experiment;
- do not allocate a main figure or contribution to it;
- keep the design as a future-paper / secondary-consequence candidate;
- only revisit if the final G20 story independently motivates a scope follow-up.

The previous deconfounded metric remains the correct one if G21 is ever revived:

```
BMarginal_no = Y(A+B) - Y(A)
BMarginal_source = Y(A+SourcePolicy+B) - Y(A+SourcePolicy)
SourceSpillover = BMarginal_no - BMarginal_source
```

Do not revert to B-alone comparisons.

---

# ReGround G19

Still cancelled before generation.

Do not run or revive it as the current method contribution.

---

# Recommended execution order

1. Build and audit G20 v3 materials.
2. Freeze the behavioral design before generation.
3. Run the smallest model panel needed to qualify the effect.
4. Only if behavior passes, run the shared-checkpoint mechanism.
5. Expand to the full planned model panel only if needed for the main claim.
6. Do not run G21 in parallel.

---

# Do not run

- G21 as current mainline;
- ReGround G19;
- another semantic-specificity ladder;
- another generic reminder study;
- model-size sweeps;
- third-mechanism-model breadth before the G20 behavior qualifies;
- source/provenance experiments that do not explain G0.

The next gain must be a **direct explanation of the prospective/retrospective
exclusion reversal**.
