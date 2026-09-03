# Related work — hindsight in language-model reasoning

The paper asks:

> **After a language model learns how something turned out, can it still judge the past without hindsight?**

Related work is best understood as four neighboring questions rather than a list of claims we need to defend against.

## 1. Hindsight, outcome bias, and the curse of knowledge

The broad scientific problem predates language models. Human judgments of earlier decisions can change after outcomes are revealed, and people who know an answer can struggle to reconstruct the perspective of someone who did not know it. Hindsight bias, outcome bias, and the curse of knowledge all study versions of this asymmetry between knowing now and judging then.

This literature motivates the paper's natural question. Our experiments do not assume that LLMs reproduce the same cognitive process as humans; they use controlled outcome information to ask whether a similar retrospective distortion appears in model judgments and, if so, what structure it has.

A useful modern replication of classic outcome-bias work is Aiyer et al. (2023), which shows that outcome information changes evaluations of earlier decisions even when participants can explicitly state that outcomes should not matter.

## 2. Ex-ante and temporal reasoning in language models

### ExAnte — EACL 2026

https://aclanthology.org/2026.eacl-long.72/

ExAnte evaluates whether models can reason under an earlier temporal cutoff despite possessing later knowledge in their parameters. Across stock prediction, QA, event generation, and publication generation, models often use post-cutoff information.

This establishes **ex-ante reasoning under future knowledge** as an important LLM capability problem.

Our paper asks a complementary, more directly causal hindsight question. Instead of relying on whatever future knowledge the model happened to internalize during training, we explicitly control the later evidence shown in context and measure how revealing a known outcome changes the same earlier judgment.

### *When Do LLMs Apply the Wrong Law?* — 2026

https://arxiv.org/abs/2608.14610

This work studies temporal applicable-law determination. Models often favor the newest statute even for earlier cases, despite understanding temporal scope and knowing historical laws.

The conceptual connection is strong: explicit knowledge of the relevant time boundary need not determine the final judgment. Our paper develops the hindsight side of that problem using resolved events and continuous judgments, then follows the effect into directional outcome influence and internal decision states.

## 3. Contextual distraction and structured influence

Later outcome information is also a form of context, so work on distraction and misleading context is an important neighbor.

### *Llama See, Llama Do* — ACL 2025 Outstanding

https://aclanthology.org/2025.acl-long.791/

Niu et al. show that distraction has a primitive regularity: tokens that have appeared in context receive increased output propensity even when they are random or semantically irrelevant. They call this **contextual entrainment** and identify attention heads that causally support it.

The lesson for our work is conceptual. A coarse behavioral failure becomes more informative when one discovers the regularity underneath it. Our analogous descent is from “known outcomes alter judgments of the past” to the finding that **outcome-shaped later context produces directional pull even across unrelated events**.

The two phenomena are not identical: our effect depends on semantic interpretation of outcome evidence rather than token occurrence alone.

### *Stochastic Chameleons* — ACL 2025 Main

https://aclanthology.org/2025.acl-long.1458/

This work shows that irrelevant contextual cues can cause structured class-based misgeneralization rather than arbitrary noise, and links that behavior to competing internal computations.

It reinforces why our paper should not be framed merely as “irrelevant context hurts.” The distinctive object is hindsight: information known *now* reshaping a judgment about *then*. The foreign-packet experiments are useful because they reveal the directional structure of that hindsight influence.

## 4. Mechanistic explanations of contextualization and decision competition

### *Racing Thoughts* — NAACL 2025 Main

https://aclanthology.org/2025.naacl-long.155/

Racing Thoughts asks why contextualization errors occur and proposes a race-condition account based on dependencies between token-processing steps. Causal interventions on processing order support the explanation.

The paper is an important methodological model for us: mechanism earns its place by explaining the behavioral phenomenon. Our G13–G15 sequence similarly asks how later outcome information becomes part of the current decision, comparing packet-local transport with contextual construction of a late decision variable.

### *Do LLMs Know Tool Irrelevance?* — ACL 2026 Main

https://aclanthology.org/2026.acl-long.1473/

This work separates semantic relevance from structural alignment and identifies competing internal pathways whose relative strength determines tool invocation. It is a strong example of a natural problem leading to an explanatory variable, then to a mechanism.

For our paper, the comparable conceptual move is not a new benchmark or another exclusion prompt. It is the discovery that known outcomes exert a directional pull and that, in Gemma, this influence becomes causally effective only after contextual integration.

### *Reason to Rote* — EMNLP 2025 Main

https://aclanthology.org/2025.emnlp-main.437/

Reason to Rote asks how memorization relates to reasoning and finds that memorization can build on generalizable reasoning computations rather than replacing them. It is another useful example of mechanism answering a relationship between natural phenomena rather than hunting for a dedicated neuron or circuit label.

## 5. Position of the present paper

The surrounding literature establishes three important facts:

1. models struggle with ex-ante reasoning when later knowledge is available;
2. models can understand a temporal rule yet still make a temporally inappropriate decision;
3. contextual information can exert structured, mechanistically interpretable influence on model outputs.

Our paper connects these threads through **hindsight**. We directly manipulate known outcomes while holding the earlier judgment task fixed, then show that the resulting distortion has a directional structure: outcome-shaped later context pulls judgments toward the outcome it supports, even across unrelated resolved events. In the strongest-effect model, we then trace that influence to a late contextualized decision state.

That is the positive positioning the introduction and related-work section should preserve.
