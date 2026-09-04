# G19 preregistration — ReGround: post-retrieval policy grounding

**Created:** 2026-09-04, before any G19 model generation.
**Status:** **CANCELLED BEFORE GENERATION on 2026-09-04. No G19_FREEZE.md was created and no G19 model output exists.**

This round reopens the experimental programme exactly once, by explicit author
decision, for a positive method evaluation derived from the confirmed mechanism.
It is not a repair of G18, G16 or G17. Every possible G19 verdict closes the
programme permanently.

## 1. Motivation

The paper establishes three facts:

1. prospective exclusion is harder than post-evidence exclusion;
2. G18 confirms that target addressability governs prospective exclusion;
3. a target-dependent rule state causally controls later evidence suppression.

The method question follows directly:

> **Can a system make a prospective semantic policy more reliable by explicitly
> resolving that policy against the documents that actually arrived after retrieval,
> before the final decision?**

Earlier G0 controls already show that a post-evidence repeat and an oracle
[ADMISSIBLE]/[EXCLUDED] ledger can work. G19 is not another repetition experiment.
It asks whether semantic target addressability can be turned into an end-to-end
**policy compiler** that identifies the instantiated target, compiles a selective
ledger, follows the target across identifier changes, and rejects a lexically similar
semantic non-match.

## 2. Method — ReGround

The system owns a prospective policy with a semantic scope. After retrieval and before
answer generation, ReGround performs:

1. **Resolve.** Match the policy's semantic target descriptor against the retrieved
   document contents and return matching document IDs.
2. **Compile.** Emit a trusted ledger containing only those IDs.
3. **Decide.** Let the original model answer with the original semantic policy plus
   the grounded ledger.

No model weights are trained or changed.

Two versions:

- **ReGround-Gold:** gold document match; upper bound on grounded enforcement.
- **ReGround-Self:** the same checkpoint performs a short greedy resolver call, then
  answers with its own compiled IDs. This is the method evaluated by the primary gates.

## 3. Equal-information principle

A central design requirement is that ReGround must not win merely because it receives
semantic information unavailable to its baseline.

Therefore the following conditions all receive the **same semantic exclusion policy
in the SYSTEM message**:

- Semantic-Pre
- Semantic-Generic
- Semantic-Restate
- ReGround-Gold
- ReGround-Self
- Sanitation-Gold

The semantic target descriptor is G18's frozen paraphrase representation.

ReGround differs from Semantic-Pre only by adding a post-retrieval document-resolution
step and compiled ledger. Semantic-Generic adds a same-position, comparable-length
post-retrieval reminder but supplies **no document-policy match**.

Identifier-only policies remain as weaker practical baselines and identity-scope
controls; they are not the primary fairness comparison.

## 4. Materials

Use the **100 G18 confirmation items / 30 independent skeletons / three families**.
No G19 method condition has been run on these items before the freeze.

Families:
- legal judgment: 40
- evidence inference: 30
- ranking / selection: 30

Each item is wrapped as a SYSTEM → USER → TOOL → decision interaction with neutral
filler documents and one of three critical retrieval variants:

1. **same-D7:** the governed proposition appears as D7;
2. **same-D9:** the same governed proposition appears under the new identifier D9;
3. **wrong-D9:** D7 is absent; D9 contains G18's high-lexical-overlap,
   different-proposition hard negative.

The wrong-D9 design is important. Because the prospective identifier baseline names
D7, placing the hard negative under D7 would make literal ID exclusion correct and
would not be a clean semantic false-positive test. Under D9, the correct semantic
resolver output is NONE.

## 5. Conditions

### Anchors

- **Base:** no critical document and no exclusion policy.
- **Naive:** critical document, no exclusion policy.
- **Sanitation-Gold:** positive target removed, with the same semantic policy retained;
  reference ceiling, not a required baseline to beat.

### Identifier baselines

- **ID-Pre:** "Document D7 must not influence..." before retrieval.
- **ID-Restate:** ID-Pre plus a post-retrieval D7 restatement.

### Equal-information semantic baselines

- **Semantic-Pre:** semantic policy before retrieval; no post-retrieval intervention.
- **Semantic-Generic:** the same semantic policy plus a post-retrieval generic reminder.
  The reminder is in the same message position and is deliberately comparable in
  character length to the compiled ledger, but contains no resolved document IDs.
- **Semantic-Restate:** the same semantic policy repeated explicitly after retrieval.
  This is a strong "just repeat the semantic rule" baseline.

### Proposed method

- **ReGround-Gold**
- **ReGround-Self**

Every non-sanitization method is evaluated on same-D7, same-D9 and wrong-D9.

## 6. ReGround-Self resolver

The resolver sees only:

- the semantic target descriptor;
- retrieved document IDs and texts.

It **does not see the final decision question**.

It outputs matching IDs separated by commas or NONE.

Frozen correct sets:
- same-D7 → D7
- same-D9 → D9
- wrong-D9 → NONE

This makes the resolver test semantic matching rather than answer-direction reasoning.

## 7. Model panel

Identical to G18 and frozen before G19 output:

- Qwen3-8B
- Gemma-3-12B
- Phi-4-mini
- Qwen3.5-27B
- Mistral-Small-24B

Five checkpoints, four vendors, roughly 3.8B–27B.

## 8. Primary behavioral metrics

All primary quantities are **raw 0–100 rating points**. No REI or
leverage-normalized ratio is used.

### 8.1 Positive-target error

For same-D7 and same-D9:

TargetError(method) = absolute value of Y_method - Y_base

Lower is better. Absolute error penalizes both residual evidence use and
over-suppression.

Primary improvement:

Improvement(method) = TargetError(Semantic-Pre) - TargetError(method)

Thus the primary method claim uses an equal-information baseline.

### 8.2 Generic-reminder separation

For same-D7 and same-D9:

ReminderGain = TargetError(Semantic-Generic) - TargetError(ReGround-Self)

This tests whether explicit grounding contributes beyond simply placing another policy
message after retrieval.

### 8.3 Hard-negative collateral

For wrong-D9:

TotalCollateral(method) = absolute value of Y_method_wrong - Y_naive_wrong

This is the end-to-end cost of applying the method when no retrieved document matches
the semantic policy.

Also report, but do not gate on:

AddedCollateral = absolute value of Y_method_wrong - Y_semantic_pre_wrong

which separates compiler-specific change from any effect of merely mentioning the
semantic policy.

### 8.4 Resolver accuracy

Report:
- exact-set accuracy;
- false-positive document IDs;
- false-negative document IDs.

### 8.5 Efficiency

Report:
- resolver prompt tokens;
- final decision prompt tokens;
- resolver batch wall-clock time / call count as an implementation-level overhead
  indicator.

## 9. Frozen success criteria

**ReGround succeeds** only if all three gates pass.

### Gate 1 — behavioral rescue over equal-information baseline

Pooled ReGround-Self improvement over Semantic-Pre:

- mean at least **+3.0 rating points**;
- 95% cluster-bootstrap CI lower bound > 0;
- model-wise improvement positive in at least **4/5** models.

### Gate 2 — grounding, not merely another reminder

Pooled ReGround-Self improvement over Semantic-Generic:

- mean at least **+2.0 rating points**;
- 95% cluster-bootstrap CI lower bound > 0.

### Gate 3 — selective grounding

- resolver exact-set accuracy at least **90% pooled**;
- pooled wrong-D9 **TotalCollateral ≤ 5.0 rating points**.

No gate requires ReGround to beat Sanitation-Gold or Semantic-Restate.

## 10. Secondary comparisons

Reported regardless of result:

- ReGround-Self vs Semantic-Restate;
- ReGround-Self vs ID-Pre;
- ReGround-Self vs ID-Restate;
- ReGround-Self vs ReGround-Gold;
- same-D7 vs same-D9 separately;
- all per-model effects;
- total and added wrong-D9 collateral;
- resolver FP/FN structure;
- overhead.

## 11. Verdicts

- **success:** all three gates pass. ReGround becomes the paper's practical
  mechanism-guided mitigation / fourth contribution.
- **partial:** Gate 1 passes but at least one other gate fails. Report as a
  proof-of-concept mitigation with the failed dimension named.
- **no-benefit:** Gate 1 fails. G19 remains a negative result and is removed from the
  paper's contribution list.

Every verdict closes the experimental programme permanently. No ReGround-v2 is
scheduled.

## 12. Exact volume

Per item/model the runner produces:

- 1 Base condition;
- 8 non-sanitization methods × 3 retrieval variants = 24 conditions;
- 2 Sanitation-Gold positive-target conditions.

Total = **27 decision conditions per item**.

Across 100 items × 5 models:
- **13,500 decision conditions**;
- **1,500 short resolver calls** for ReGround-Self.

No training.

## 13. Freeze implementation

The frozen tree must contain:

- this preregistration;
- src/reground.py;
- src/run_reground.py;
- src/analyze_reground.py;
- tests/test_reground.py;
- METHOD_REGROUND.md;
- G19_FREEZE.md.

Because the files were authored through sequential repository commits, the freeze
authority is **the final G19_FREEZE.md commit over the complete tree**, not an earlier
individual file commit. No model generation may occur before that freeze commit.


## 14. Cancellation record

This preregistered design was abandoned before execution after a novelty audit.
The reason is scientific, not technical: the proposed operation—resolve a semantic
policy after retrieval and compile the matching document IDs—is a reasonable
engineering mitigation but too normal to justify reopening the paper around a new
method contribution.

Because no freeze marker and no generations exist, no statistical result is attached
to this design. Preserve this file unchanged from this point as evidence of the
cancelled pre-run plan.

Active next hypotheses:
- G20 Binding Deadline / Late Target Revelation
- G21 Source-Scope Collapse / Semantic Spillover

See NOVELTY_RESET_2026-09-04.md and NEXT_EXPERIMENTS_POST_RESET.md.
