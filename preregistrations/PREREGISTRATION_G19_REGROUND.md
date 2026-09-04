# G19 preregistration — ReGround: post-retrieval policy grounding

**Created:** 2026-09-04, before any G19 model generation.
**Status:** frozen design once this document and implementation are committed.
This round reopens the experimental programme exactly once, by explicit author
decision, for a positive method evaluation derived from the confirmed mechanism. It
is not a repair of G18, G16 or G17.

## 1. Motivation

The paper now establishes three facts:

1. prospective exclusion is harder than post-evidence exclusion;
2. G18 confirms that target addressability governs prospective exclusion;
3. a target-dependent rule state causally controls later evidence suppression.

The method question is therefore natural:

> **Can a system recover reliable prospective exclusion by grounding a policy to the
> concrete retrieved information after retrieval but before the final decision?**

Earlier G0 controls already show that a post-evidence repeat and an oracle
[ADMISSIBLE]/[EXCLUDED] ledger can work. G19 is not a repeat of that result. It asks
whether the paper's semantic-target account can be turned into an **end-to-end policy
compiler** that (a) identifies the actual retrieved target, including under identifier
change, (b) compiles a grounded exclusion ledger, and (c) avoids suppressing a
lexically similar but semantically different document.

## 2. Method — ReGround

A prospective policy is stored before retrieval. After retrieval and before answer
generation, ReGround performs a short matching pass:

1. **Resolve.** Given the policy's semantic target descriptor and the retrieved
   documents, identify which document IDs state the governed proposition.
2. **Compile.** Emit a trusted ledger containing only the matched document IDs:
   `[EXCLUDED BY POLICY] D9`.
3. **Decide.** The original decision model receives the retrieved documents plus the
   compiled ledger and answers normally.

The semantic target descriptor is used only by the resolver. It is not copied into
the final decision prompt, preventing the method from receiving credit merely for
repeating the target proposition to the decision model.

Two versions are evaluated:

- **ReGround-Gold:** the ledger uses the known experimental match. This is the
  compiler upper bound and isolates the value of grounded enforcement.
- **ReGround-Self:** the same model performs the resolver pass and its predicted
  document IDs are compiled. This is the end-to-end inference-time method.

No weights are trained or updated.

## 3. Materials

Use the **100 G18 confirmation items / 30 independent skeletons / three families**.
These items were never used for any method condition. G19 adds an agentic retrieval
wrapper around them.

Families:
- legal judgment: 40
- evidence inference: 30
- ranking / selection: 30

For every item the retrieval package contains neutral filler documents plus one of
three critical variants:

1. **same-D7:** the governed proposition appears under identifier D7;
2. **same-D9:** the same governed proposition appears under a different identifier D9;
3. **wrong-D9:** D7 contains the G18 lexical-overlap / different-proposition control.

The wrong-D9 condition is deliberately difficult: surface vocabulary resembles the
target, but the proposition is different.

## 4. Policy representation

The decision model's baseline prospective policy is identifier-based:

> Document D7 must not influence any answer you give in this session.

The ReGround resolver additionally receives a **structured semantic descriptor** of
the governed proposition, using G18's frozen paraphrase representation. This models a
policy registry that stores the semantic scope of a rule even when the user-facing
instruction refers to a resource name.

A dedicated baseline exposes the same semantic descriptor directly in the prospective
SYSTEM policy (**Semantic-Pre**) to separate “extra semantic information” from
post-retrieval grounding.

## 5. Conditions

Each item is evaluated under:

### Anchors
- **Base:** no critical document.
- **Naive:** critical document, no exclusion policy.
- **Sanitation-Gold:** matched critical document removed; ceiling reference.

### Prospective baselines
- **ID-Pre:** identifier-only system policy before retrieval.
- **Semantic-Pre:** proposition-level semantic policy before retrieval.

### Post-retrieval controls
- **Generic-Repeat:** ID-Pre plus a same-length generic reminder after retrieval:
  “Apply all system policies to the retrieved documents before answering.”
- **ID-Restate:** ID-Pre plus a post-retrieval restatement that D7 is excluded.

### Proposed method
- **ReGround-Gold**
- **ReGround-Self**

Every applicable method is run on same-D7, same-D9 and wrong-D9.

## 6. Model panel

Five models, identical to G18:
- Qwen3-8B
- Gemma-3-12B
- Phi-4-mini
- Qwen3.5-27B
- Mistral-Small-24B

This avoids selecting a panel after method results and permits direct comparison to
the confirmed target-addressability experiment.

## 7. Primary behavioral metrics

All primary metrics use **raw 0–100 rating points**. No REI or leverage-normalized
ratio is used.

### 7.1 Positive-target error

For same-D7 and same-D9:

`TargetError(method) = abs(Y_method - Y_base)`

Lower is better. This penalizes both residual use and over-suppression.

Primary improvement:

`Improvement(method) = TargetError(ID-Pre) - TargetError(method)`

Pool over same-D7 and same-D9, model × skeleton, with cluster bootstrap over
skeletons.

### 7.2 Negative-match collateral

For wrong-D9:

`Collateral(method) = abs(Y_method_wrong - Y_naive_wrong)`

Lower is better. This asks whether the method distorts a document that is lexically
similar but semantically outside the policy.

### 7.3 Resolver accuracy

For ReGround-Self:
- same-D7: select D7
- same-D9: select D9
- wrong-D9: select NONE

Report exact-set accuracy and false-positive / false-negative rates.

## 8. Frozen method success criteria

**ReGround succeeds** if all three hold:

1. **Behavioral rescue:** pooled ReGround-Self improvement over ID-Pre is at least
   **5.0 rating points**, with 95% cluster-bootstrap CI lower bound > 0, and model-wise
   improvement is positive in at least 4/5 models.
2. **Beyond reminder:** ReGround-Self improves over Generic-Repeat by at least
   **3.0 rating points**, with pooled CI lower bound > 0 on same-D7 + same-D9.
3. **Selective grounding:** resolver exact-set accuracy is at least **90% pooled** and
   pooled wrong-D9 Collateral is at most **5.0 rating points**.

Secondary comparisons, reported regardless of outcome:
- ReGround-Self vs ID-Restate;
- ReGround-Self vs Semantic-Pre;
- ReGround-Self vs ReGround-Gold;
- same-D7 vs same-D9;
- all model-wise results;
- latency / extra-token overhead of the resolver pass.

No gate depends on ReGround beating Sanitation-Gold.

## 9. Interpretation of outcomes

- **success:** the mechanism-derived method becomes Contribution 4 / practical payoff.
  Experimental programme closes permanently.
- **partial:** grounding helps but resolver precision or generic-reminder separation
  fails. Report as a proof-of-concept mitigation, not a general method. Programme
  closes.
- **no-benefit:** the method section is omitted from the main contribution list; G19
  remains an honest negative result. The phenomenon, G18 and mechanism claims are
  unchanged. No successor method is scheduled.

## 10. Volume

Decision conditions are approximately 20 cells per item × 100 items × 5 models
(about 10,000 decision generations), plus resolver calls for ReGround-Self.
Greedy decoding throughout. No training.

## 11. Freeze rule

No G19 generation may occur before:
- this preregistration;
- `src/reground.py`;
- `src/run_reground.py`;
- `src/analyze_reground.py`;
- prompt/unit tests

are committed together. That commit SHA is the freeze point.
