# ACL / EMNLP / NAACL alignment standard

The target is **strong Main / Outstanding-shaped work**, not the median accepted paper and not Findings as the aspiration.

The most important lesson from the reference papers is not “run more controls” and not “add mechanistic interpretability.” It is:

> **Start from a natural scientific question, discover something non-obvious about it, and make every major experiment deepen the explanation.**

## Reference papers

### ACL 2025 Outstanding — *Llama See, Llama Do*
https://aclanthology.org/2025.acl-long.791/

The broad problem is **LLM distraction**. The paper then discovers contextual entrainment: prior token occurrence itself raises the token's propensity, even for random tokens. The new phenomenon is useful because it explains something about distraction; the attention-head work then connects the internal mechanism back to that phenomenon.

**Lesson:** natural problem → surprising regularity → mechanism that explains the regularity.

### EMNLP 2025 Outstanding — *Causal Interventions Reveal Shared Structure Across English Filler–Gap Constructions*
https://aclanthology.org/2025.emnlp-main.1271/

The question is whether apparently different constructions share abstract structure. Causal interchange is valuable because it answers that theory question and reveals where the shared-structure story breaks or changes.

**Lesson:** the scientific question exists before the method.

### EMNLP 2025 Outstanding — *Mind the Value-Action Gap*
https://aclanthology.org/2025.emnlp-main.154/

The question is immediately understandable: **do LLMs act in alignment with the values they state?** The paper matters because it separates two natural quantities that prior evaluation often conflated.

**Lesson:** a strong paper can advance the field by defining the right object of study; it does not need a circuit as decoration.

### NAACL 2025 Main — *Racing Thoughts*
https://aclanthology.org/2025.naacl-long.155/

The paper is about **contextualization errors**. The race-condition hypothesis is valuable because it offers an algorithmic explanation and makes causal predictions about processing order.

**Lesson:** mechanism should explain the headline failure, not sit beside it.

### ACL 2026 Main — *Do LLMs Know Tool Irrelevance?*
https://aclanthology.org/2026.acl-long.1473/

The natural problem is whether a model can refrain from invoking an irrelevant tool. Structural alignment bias is the explanatory variable beneath the failure; SABEval is built to separate structural alignment from semantic relevance; competing pathways then explain the wrong action.

**Lesson:** latent variables and experiments descend from the natural question. The dataset is an instrument, not the paper's identity.

## What strong papers do structurally

### 1. A short natural question

The question should make sense before introducing a benchmark, metric, layer, causal estimator, or newly coined term.

Good level of abstraction:

- Why do irrelevant contexts distract language models?
- Do different syntactic constructions share a mechanism?
- Do models act according to their stated values?
- Why does contextualization fail?
- Why do models invoke tools they know are irrelevant?

For this project:

> **After a language model learns how something turned out, can it still judge the past without hindsight?**

The scientific object is simply **hindsight in language-model reasoning**.

Terms such as `information set`, `out-of-set intrusion`, `retrospective outcome entrainment`, and `recipient-conditioned decision state` belong at progressively lower explanatory levels. They must not replace the natural object.

### 2. Positive explanatory descent

The main paper should read:

```text
natural question
    ↓
important phenomenon
    ↓
sharper regularity
    ↓
causal discrimination
    ↓
mechanistic explanation
```

It should **not** read:

```text
claim
    ↓
reviewer objection A → control
    ↓
reviewer objection B → control
    ↓
reviewer objection C → control
```

Controls are useful only when they reveal something scientifically new or are necessary for the validity of the central result. They are not the narrative.

### 3. One or two real explanatory moves beat many narrow claims

A strong paper does not maximize the number of statements it can defend. It identifies the smallest set of results that changes how we understand the phenomenon.

For this project, the key move is not “we ruled out copying, scale, wording, etc.” The key move is:

> **Known outcomes distort judgments of the past, and the distortion has a directional structure: outcome-shaped later context pulls judgments toward the outcome it supports, even across unrelated events.**

The mechanism then asks how that outcome influence enters the decision.

### 4. Mechanism earns its place by explaining the phenomenon

Opening the model is justified when it distinguishes genuinely different algorithms or explains the headline behavior. More probes, patching, neurons, or layers do not automatically increase paper quality.

For this project, G13–G15 matter because they distinguish packet-local transport from contextual construction of the late decision variable. The mechanism should be narrated as an answer to **how hindsight enters the decision**, not as a separate MI section seeking technical prestige.

### 5. Limitations are compact, not a second paper

Precision matters, but defensive prose should not dominate the introduction, abstract, result headings, or conclusion. Detailed gate failures, preregistration thresholds, unsuccessful branches, and qualification rules belong in the experiment registry, appendix, or limitations when needed.

The main text should state the strongest result supported by the data in ordinary scientific language.

## Current project against this bar

### Natural question

> **Can language models judge the past without hindsight once they know the outcome?**

This is strong enough to carry the paper without any bespoke terminology.

### Main explanatory arc

```text
known outcomes alter judgments of the past
although models know the evidence came later
    ↓
outcomes from unrelated events still pull the judgment
in the direction they support
    ↓
changing the outcome direction of later evidence changes
which way the same judgment moves
    ↓
in Gemma, this influence becomes causal only after the
later evidence is integrated with the current question
```

This is the paper's core. Scale sweeps, prompt-reason manipulations, failed mitigation, and broad source attempts are secondary.

## Decision rule for future work

The default is **write the paper, not defend it with more experiments**.

Run something new only when it answers a new scientific question that materially deepens our understanding of hindsight. “A reviewer may ask for another control/model/benchmark” is not sufficient justification.
