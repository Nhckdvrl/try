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

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

The scientific object is simply **whether a stated exclusion policy governs the decision**.

`Prospective binding failure` is the mechanism's name and sits at a lower explanatory level; it must not replace the natural object. Terms from the abandoned hindsight frame — `information set`, `out-of-set intrusion`, `retrospective outcome entrainment`, `recipient-conditioned decision state` — do not belong in this paper at all.

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

For this project, the key move is not “we ruled out distance, wording, masking, implicature.” Those tests earn their place because each was run to discriminate between live explanations, but they are Section 3, not the paper. The key move is:

> **An exclusion policy governs the decision when it can be resolved against the content it governs; a policy held as a pending intention about a named future item does not — and naming that item is worse than saying nothing.**

The mechanism then asks where that binding difference becomes causal.

### 4. Mechanism earns its place by explaining the phenomenon

Opening the model is justified when it distinguishes genuinely different algorithms or explains the headline behavior. More probes, patching, neurons, or layers do not automatically increase paper quality.

For this project, the span gate, the late patching curve and the matched-chronology interchange matter because they show that excluded evidence is still *read* at the decision, that gating is resolved late, and that the binding state is exchangeable. The mechanism should be narrated as an answer to **why a stated policy fails to gate**, not as a separate MI section seeking technical prestige. G16 is the one experiment that would close it on the paper's own contrast.

### 5. Limitations are compact, not a second paper

Precision matters, but defensive prose should not dominate the introduction, abstract, result headings, or conclusion. Detailed gate failures, preregistration thresholds, unsuccessful branches, and qualification rules belong in the experiment registry, appendix, or limitations when needed.

The main text should state the strongest result supported by the data in ordinary scientific language.

## Current project against this bar

### Natural question

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

This is strong enough to carry the paper without any bespoke terminology, and it
describes a structure — a policy that precedes the data it governs — that occurs in
every agent, RAG and system-prompt deployment.

### Main explanatory arc

```text
exclusion stated after the evidence is followed; the identical
exclusion stated before it is not, while the model states the
required weight as exactly zero on 100% of items
    ↓
not memory, not distance, not the causal mask, not one wording,
not inclusion implicature
    ↓
the failure is specific to complete suppression, and disappears
where the contribution is arithmetically implementable
    ↓
what the policy can bind to decides it: naming a future item is
worse than saying nothing; propositional content and class markers
carried on the evidence work — in vignettes and in an agent
    ↓
excluded evidence is still read at the decision, gating is resolved
late, and the binding state is causally exchangeable
```

This is the paper's core. Paraphrase sweeps, cluster robustness, readout
methodology and external boundary checks are secondary.

### Where it stands against each reference paper

| reference | the move it models | our counterpart | status |
|---|---|---|---|
| *Llama See, Llama Do* | phenomenon → regularity → mechanism that acts on it | reversal → binding → span gate and interchange | present |
| filler–gap interchange | causal interchange answers a theory question | Stage 5, and G16 on the paper's own contrast | Stage 5 done, G16 designed |
| *Value-Action Gap* | separate two quantities prior work conflated | stated policy vs enforced policy, at 100% vs +0.64 | present |
| *Racing Thoughts* | mechanism explains the headline failure | mechanism targets the pre/post gap itself | present |
| *Tool Irrelevance* | latent variable beneath the failure | what the policy can be resolved against | present |

### Honest weak points

- The mechanism is Qwen3-8B only, and G16 does not change that.
- The materials are authored vignettes from 10 legal skeletons; the external sets are
  boundary checks, not a held-out tier.
- `procedural_hearsay` collapsed to 2 usable items and that arm is untested.
- Item screening was done on Qwen3-8B alone.

These go in Limitations in four sentences. They are not fixed by adding models.

## Decision rule for future work

The default is **write the paper, not defend it with more experiments**.

The only planned experiment is G16, and it is planned because it closes the
mechanism on the headline contrast — not because a reviewer might ask for it. “A
reviewer may ask for another control/model/benchmark” is not sufficient
justification, and neither is “a preregistration in the repository was left
unfinished.”
