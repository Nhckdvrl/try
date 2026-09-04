# ReGround — post-retrieval policy grounding

**Status:** implemented and preregistered; no G19 model output has been observed.
**Role if successful:** practical method / fourth contribution of the paper.
**Preregistration:** [preregistrations/PREREGISTRATION_G19_REGROUND.md](preregistrations/PREREGISTRATION_G19_REGROUND.md)

## 1. Why this method follows from the paper

The paper establishes:

1. prospective exclusion is harder than post-evidence exclusion;
2. target addressability governs prospective exclusion;
3. target availability changes a causal rule state before later evidence is processed.

A direct engineering implication is therefore to **delay target resolution, not the
policy itself**.

The policy still exists prospectively. ReGround waits until retrieval instantiates the
candidate information, resolves the policy against those concrete documents, and only
then compiles a decision-time exclusion ledger.

This is different from a generic reminder:
- the prospective policy is not simply repeated;
- the resolver identifies which actual document carries the governed proposition;
- the compiled message contains only document IDs, not a repeated target proposition;
- the method can follow the target across D7→D9;
- a lexical-overlap / wrong-proposition D7 is an explicit false-positive test.

## 2. Algorithm

### Inputs

- prospective policy visible to the decision model;
- structured semantic target descriptor stored by the policy layer;
- retrieved documents.

### Resolver

A short greedy call receives only:

- the semantic target descriptor;
- retrieved document IDs and texts.

It returns matching IDs or NONE.

The final question is **not** shown to the resolver.

### Compiler

The predicted IDs become a trusted POLICY COMPILATION message listing only the
matched document IDs and instructing the decision model to assign those documents zero
evidential weight.

For a non-match the compiler emits EXCLUDED DOCUMENTS: NONE.

The semantic descriptor itself is not copied into the final decision prompt. This
prevents ReGround from winning simply because it repeats the prohibited proposition.

### Decision

The original model receives:

SYSTEM prospective policy
→ USER background/question
→ TOOL retrieved documents
→ trusted compiled ledger
→ answer

No training or weight update is used.

## 3. Method variants

- **ReGround-Gold** — gold document match; upper bound on the compiler.
- **ReGround-Self** — the same checkpoint performs the short resolver pass, then
  answers using the compiled ledger.

The paper's method claim, if the frozen gates pass, is about **ReGround-Self**.
Gold is an explanatory upper bound.

## 4. Baselines

The method evaluation deliberately includes baselines that isolate what ReGround buys:

- **Naive:** no exclusion policy.
- **ID-Pre:** identifier-only prospective system policy.
- **Semantic-Pre:** expose the semantic descriptor prospectively to the decision model.
- **Generic-Repeat:** same prospective ID policy plus a generic post-retrieval reminder.
- **ID-Restate:** explicitly restate D7 after retrieval.
- **Sanitation-Gold:** remove the matched document; ceiling/reference.

Thus:
- Self > Generic asks whether grounding adds more than recency/reminding;
- Self > ID-Restate asks whether semantic resolution beats literal identifier scope;
- Self vs Semantic-Pre asks whether post-retrieval grounding adds value beyond simply
  putting more semantic content in the original policy;
- Self vs Gold measures resolver headroom.

## 5. Evaluation cases

Every item receives three retrieval variants.

### same-D7

The governed proposition arrives under the identifier named by the prospective policy.

### same-D9

The **same proposition** arrives under a new identifier. This is the Stage-4
counterfactual turned into a method test.

### wrong-D7

D7 contains G18's **high-lexical-overlap, different-proposition** control.

A useful method must exclude same-D7 and same-D9 while leaving wrong-D7 alone.

## 6. Data and model panel

Materials:
- 100 G18 confirmation items;
- 30 independent skeletons;
- three task families.

The method conditions themselves are new and no G19 generation existed when the
design was frozen.

Models:
- Qwen3-8B
- Gemma-3-12B
- Phi-4-mini
- Qwen3.5-27B
- Mistral-Small-24B

Approximate volume:
- about 12,000 decision generations;
- 1,500 short resolver calls;
- no training.

## 7. Primary metrics

### Positive-target error

For same-D7 and same-D9:

TargetError = absolute value of Y_method - Y_base

This is deliberately absolute: both residual use and over-suppression are errors.

Primary rescue:

Improvement = TargetError(ID-Pre) - TargetError(ReGround-Self)

### Hard-negative collateral

For wrong-D7:

Collateral = absolute value of Y_method_wrong - Y_naive_wrong

The method should not distort the answer merely because the wrong document has similar
vocabulary.

### Resolver accuracy

Exact document-set accuracy:
- same-D7 → D7
- same-D9 → D9
- wrong-D7 → NONE

## 8. Frozen success gates

See the preregistration for authoritative wording.

In short, success requires:

1. ReGround-Self improves over ID-Pre by at least 5 raw rating points, CI lower > 0,
   with positive model-wise improvement in at least 4/5 models;
2. it beats Generic-Repeat by at least 3 points with CI lower > 0;
3. resolver accuracy at least 90% and wrong-D7 collateral at most 5 points.

No gate requires beating sanitation.

## 9. Implementation

- src/reground.py — prompt/compiler logic
- src/run_reground.py — two-pass vLLM runner
- src/analyze_reground.py — frozen metrics and gates
- tests/test_reground.py — prompt/parser hard-negative tests

Expected raw outputs:

results/raw/<tag>_reground.jsonl

Analysis command:

PYTHONPATH=src python3 src/analyze_reground.py qwen3-8b gemma3-12b phi4-mini qwen3.5-27b mistral-small-24b

Outputs:

- results/reground_analysis.json
- results/reground_results.md

## 10. Paper role

If **success**:
the paper gains a final arc:

phenomenon
→ target addressability
→ causal mechanism
→ ReGround mitigation

This brings the structure closer to ACL 2025 Outstanding Llama See, Llama Do and ACL
2026 Main Do LLMs Know Tool Irrelevance?, where mechanistic explanation leads to a
behavior-changing intervention.

If **partial**:
ReGround is reported as proof-of-concept mitigation, not a general method.

If **no-benefit**:
the method is an honest negative and is removed from the contribution list. No
successor method is scheduled.
