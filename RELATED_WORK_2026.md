# Related work and novelty boundary — 2026 paper

This is the binding novelty note for the current paper. The paper studies **retrospective epistemic reconstruction / information-set conditioning under hindsight**.

Core question:

> **After learning how something turned out, can a language model still condition a reconstructed past judgment only on information that was available beforehand?**

The novelty is not generic future-information leakage, generic irrelevant-context sensitivity, or the fact that a model can state a temporal rule and still violate it.

## 1. Ex-ante reasoning and temporal leakage

### ExAnte (EACL 2026)
https://aclanthology.org/2026.eacl-long.72/

ExAnte studies reasoning under an explicit historical cutoff when model parameters may already contain later knowledge. It establishes ex-ante inference and temporal leakage as existing objects.

Therefore we cannot claim:

> “LLMs accidentally use future knowledge when asked to reason about the past.”

Our distinction is that later knowledge is **explicitly manipulated in context** and its causal effect is measured within the same recipient judgment.

### *When Do LLMs Apply the Wrong Law?* (2026)
https://arxiv.org/abs/2608.14610

This work shows that models can know a temporal applicability rule and the historical law yet still prefer a newer statute version.

Therefore we cannot claim priority for:

> “models know the temporal rule but fail to obey it.”

Our contribution begins below that observation: same-evidence causal sensitivity, unrelated outcome-shaped evidence, paired donor-outcome-class replacement, and late causal expression.

## 2. Irrelevant context, distraction, and contextual conflict

Generic irrelevant-context sensitivity is a crowded area. The paper must not be framed as “irrelevant future evidence distracts LLMs.”

### ACL 2025 Outstanding — *Llama See, Llama Do*
https://aclanthology.org/2025.acl-long.791/

This paper moves below generic distraction to **contextual entrainment**: prior token occurrence increases propensity for that token even for random tokens, with identifiable entrainment heads.

Lesson for our positioning: the valuable move is from a coarse failure to a sharper regularity. Our corresponding move is **not** “future packets distract,” but that **outcome-shaped evidence from unrelated resolved events exerts donor-directed pull on a reconstructed historical judgment**.

The analogy is methodological, not one-to-one. Llama See isolates a more primitive token-occurrence law than our semantically interpreted outcome-shaped evidence.

### ACL 2025 Main — *Stochastic Chameleons*
https://aclanthology.org/2025.acl-long.1458/

This work already studies structured misgeneralization driven by irrelevant contextual cues. It is another reason the paper cannot be sold as a generic distractor-robustness result.

### Authority / source-conflict work

Work on source preference and authority bias similarly shows that competing contextual sources can steer answers. Our distinction is that the excluded information may be accurate and highly diagnostic, but is **definitionally outside the epistemic state being reconstructed**.

That is different from ordinary semantic irrelevance.

## 3. Knowledge/recognition–action gaps

### EMNLP 2025 Outstanding — *Mind the Value-Action Gap*
https://aclanthology.org/2025.emnlp-main.154/

This paper demonstrates why declarative self-report and actual behavior are distinct scientific quantities.

Our recognition probe plays a similar conceptual role: a model's ability to identify that evidence is outside the target information set is not equivalent to enforcing that fact in the downstream judgment.

But recognition–enforcement dissociation alone is **not** our full novelty claim because temporal rule/application gaps already exist. It is the starting phenomenon for the explanatory analysis.

## 4. Mechanistic contextualization and competing pathways

### NAACL 2025 Main — *Racing Thoughts*
https://aclanthology.org/2025.naacl-long.155/

Racing Thoughts proposes an algorithmic race-condition hypothesis for contextualization errors and tests it with interventions that change processing dependencies. Its strength is that the mechanism directly explains the headline failure.

This is the right benchmark for our remaining open question. G15 localizes where outcome influence becomes causal, but does not yet explain why a recognized information boundary fails to gate it.

### ACL 2026 Main — *Do LLMs Know Tool Irrelevance?*
https://aclanthology.org/2026.acl-long.1473/

This work first orthogonalizes **semantic relevance × structural alignment**, then identifies competing semantic-checking and structural-matching pathways whose balance predicts tool invocation.

The important lesson is design-level factorization of latent variables. It also motivates the only plausible next mechanistic branch for our project: whether boundary/admissibility computation causally gates, competes with, or merely coexists with the late outcome pathway.

### EMNLP 2025 Outstanding — filler–gap causal abstraction
https://aclanthology.org/2025.emnlp-main.1271/

Here causal interchange is valuable because it directly adjudicates a pre-existing theoretical question about shared abstract structure across constructions. This is the standard for using mechanistic tools: the method must answer the scientific question rather than serve as a credential.

### NAACL 2025 Main — SCIURus
https://aclanthology.org/2025.naacl-long.618/

SCIURus asks whether uncertainty and factuality arise from shared or separate circuitry and uses causal tracing/ablation to adjudicate the alternatives across models and datasets.

### NAACL 2025 Main — The LLM Language Network
https://aclanthology.org/2025.naacl-long.544/

This work starts from functional specialization and uses ablation to establish causal task relevance. Again, the object comes before the interpretability method.

### EMNLP 2025 Main — *Reason to Rote*
https://aclanthology.org/2025.emnlp-main.437/

This work asks how memorization relates to generalizable reasoning machinery and finds that memorization builds on distributed reasoning computation rather than simply locating a separate memorization mechanism. It is a useful model for relationship-first mechanistic questions.

## 5. Natural phenomena with mechanism as explanation

### ACL 2026 Main — *Privacy Collapse*
https://aclanthology.org/2026.acl-long.400/

The paper first establishes a natural consequential phenomenon — benign fine-tuning selectively damages contextual privacy — then uses mechanism to explain differential fragility.

### ACL 2026 Main — *How Memory Management Impacts LLM Agents*
https://aclanthology.org/2026.acl-long.27/

This paper is organized around a behavioral regularity, **experience-following**, which explains error propagation and memory-management consequences. It shows that a strong Main paper does not require a complete circuit when the scientific regularity itself is clear and explanatory.

## 6. Human hindsight / outcome bias

Human hindsight and outcome-bias literatures motivate the natural question that knowledge of an outcome can distort reconstruction or evaluation of earlier judgments.

We do **not** claim that LLMs instantiate the same psychological mechanism. “Hindsight” is descriptive/motivational language; our measured object is causal information-set sensitivity.

## 7. In-context forgetting and information-flow control

In-context forgetting asks whether a model can selectively forget or suppress contextual information. Security/privacy work studies noninterference and forbidden information flow.

Our desired behavior is narrower:

```text
later evidence may remain visible, true, useful, and recallable
but
its causal effect on a reconstructed earlier judgment should be approximately zero
```

The target is **decision conditioning**, not erasure from memory.

## 8. Current novelty statement

The defensible novelty is the full explanatory sequence, not any one isolated observation:

> **We prospectively show that explicit future evidence causally changes an otherwise identical reconstructed historical judgment despite near-ceiling recognition that it lies outside the target information set; we then show that outcome-shaped evidence from unrelated resolved events produces directional pull, including under a paired outcome-class intervention, and in the strong-effect model localize this influence to a late recipient-conditioned answer state rather than the tested one-dimensional packet-local bottleneck.**

## 9. Important precision boundaries

### G12

Do not write “changing only donor outcome.” YES-supporting and NO-supporting packets are different packets; event semantics, lexical content, and other packet properties co-vary.

Safe wording:

> “Replacing a NO-supporting irrelevant future packet with a YES-supporting irrelevant future packet raises the same reconstructed probability.”

### Cross-model strength

G12 direction is positive in all three primary models, but effect magnitude is highly heterogeneous and the preregistered 5pp panel gate is indeterminate.

Do not write “robust causal outcome entrainment across models.”

### Mechanism

G15 is strong evidence in Gemma for a late recipient-conditioned causal decision state. It does not establish a dedicated hindsight circuit or the full mechanism of boundary failure.

### External fidelity

G7 failed in the opposite direction and uncontaminated judgments correlate only weakly with BTF-3's independent ex-ante forecast. Do not claim the packet makes the model less faithful to an objective ex-ante forecast.

## 10. Main vs. higher-ambition closure

The current paper is Main-shaped under the standard in `ACL_EMNLP_ALIGNMENT_STANDARD.md`.

The unresolved higher-level question is:

> **Why does a represented/recognized information boundary fail to gate the late outcome pathway?**

Only a clean prospective causal discrimination among competing algorithms for this interaction would materially deepen the paper toward the explanatory closure of Racing Thoughts / Tool Irrelevance. More prompts, datasets, models, mitigations, or generic-axis controls are not automatically useful.
