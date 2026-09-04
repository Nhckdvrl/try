# ReGround — post-retrieval policy grounding

**Status:** implemented and preregistered; no G19 model output has been observed.
**Role if successful:** mechanism-guided mitigation / fourth paper contribution.
**Preregistration:** [preregistrations/PREREGISTRATION_G19_REGROUND.md](preregistrations/PREREGISTRATION_G19_REGROUND.md)

## 1. Method idea

The paper shows that prospective exclusion depends on target addressability. ReGround
turns that explanation into a simple inference-time system:

> **keep the policy prospective, but resolve its semantic scope against the concrete
> documents only after retrieval has instantiated them.**

Pipeline:

semantic prospective policy
→ retrieval
→ semantic policy resolver
→ matched document IDs
→ trusted exclusion ledger
→ original model decision

No model weights are changed.

## 2. Fair input design

ReGround must not win because it secretly receives more semantic information than its
baseline.

Therefore Semantic-Pre, Semantic-Generic, Semantic-Restate, ReGround-Gold and
ReGround-Self all receive the same semantic exclusion policy in the SYSTEM message.
The semantic descriptor is G18's frozen paraphrase representation.

The only additional operation in ReGround is explicit **policy-to-document
resolution after retrieval**.

Identifier-only conditions remain practical baselines, but they are secondary rather
than the primary fairness comparison.

## 3. Resolver

The short resolver pass sees:

- the semantic policy target;
- retrieved document IDs and texts.

It does **not** see the final answer question.

It returns matching IDs or NONE.

ReGround-Self uses the same checkpoint for this call. ReGround-Gold uses the known
experimental match and measures the upper bound of the compiler independent of
resolver errors.

## 4. Compiler

The resolver output is converted to a trusted decision-time ledger such as:

    POLICY COMPILATION (trusted)
    EXCLUDED DOCUMENTS: D9
    Only the listed retrieved documents are excluded by this policy.
    Treat their contents as having zero evidential weight.

If there is no semantic match:

    EXCLUDED DOCUMENTS: NONE

This representation is deliberately document-specific. It resolves the previously
prospective semantic policy to the objects that now actually exist.

## 5. Retrieval variants

The method is not evaluated only on an easy same-ID case.

### same-D7

The governed proposition arrives under D7.

### same-D9

The same proposition arrives under a different document identifier. A successful
semantic resolver should follow the information to D9.

### wrong-D9

D7 is absent. D9 contains the G18 high-lexical-overlap but different-proposition hard
negative. The correct resolver output is NONE.

This cleanly tests false semantic matching without conflicting with the literal D7
identifier policy.

## 6. Baselines

### Anchors

- Base
- Naive
- Sanitation-Gold

### Identifier controls

- ID-Pre
- ID-Restate

### Equal-information semantic controls

- **Semantic-Pre:** semantic policy only.
- **Semantic-Generic:** same semantic policy plus a same-position,
  comparable-length generic post-retrieval reminder, with no resolved match.
- **Semantic-Restate:** same semantic policy repeated after retrieval.

### Method

- ReGround-Gold
- ReGround-Self

The load-bearing method comparisons are Self vs Semantic-Pre and Self vs
Semantic-Generic.

## 7. Evaluation

Materials:
- 100 G18 items;
- 30 independent skeletons;
- 3 task families.

Models:
- Qwen3-8B
- Gemma-3-12B
- Phi-4-mini
- Qwen3.5-27B
- Mistral-Small-24B

Exact volume:
- 27 decision conditions per item/model;
- 13,500 decision conditions total;
- 1,500 short resolver calls.

No training.

## 8. Metrics

### Positive targets

For same-D7 / same-D9:

TargetError = absolute distance from the no-critical-document Base answer.

This is preferable to signed leakage because it penalizes both continued evidence use
and over-suppression.

Primary improvement is reduction in TargetError relative to **Semantic-Pre**.

### Generic-reminder comparison

ReGround must also reduce TargetError relative to Semantic-Generic, showing that the
gain is not merely due to another post-retrieval policy message.

### Hard-negative precision

For wrong-D9, total collateral is the absolute difference from the Naive answer.

The resolver also has a direct exact-set target:
- D7
- D9
- NONE

## 9. Frozen success bar

Success requires all three:

1. Self improves over Semantic-Pre by at least +3.0 rating points, pooled CI lower >0,
   and the model-wise improvement is positive in at least 4/5 models.
2. Self improves over Semantic-Generic by at least +2.0 points, pooled CI lower >0.
3. Resolver exact-set accuracy is at least 90% and wrong-D9 total collateral is at
   most 5 rating points.

Semantic-Restate, ID baselines, Gold and sanitation are reported as secondary
comparisons and bounds.

## 10. Implementation

- src/reground.py — method/compiler
- src/run_reground.py — two-pass vLLM runner
- src/analyze_reground.py — frozen metrics/gates
- tests/test_reground.py — prompt, control and hard-negative tests
- preregistrations/PREREGISTRATION_G19_REGROUND.md — authoritative design

Expected outputs:

- results/raw/<tag>_reground.jsonl
- results/reground_analysis.json
- results/reground_results.md

## 11. Scientific role

If successful, ReGround gives the paper an Outstanding-shaped final descent:

prospective exclusion failure
→ target addressability
→ causal target-dependent rule state
→ **explicitly re-ground the policy after retrieval and improve the behavior**

This is the same kind of positive closure that makes Llama See, Llama Do and Tool
Irrelevance especially satisfying: the explanation tells us what intervention to make.

If only partial, ReGround remains a proof of concept.

If the primary rescue fails, it is a negative result and does not alter the phenomenon,
G18, or mechanism. No successor method is scheduled.
