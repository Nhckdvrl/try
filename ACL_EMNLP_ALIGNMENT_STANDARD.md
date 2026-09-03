# ACL / EMNLP / NAACL alignment standard

This is the quality bar for the project. The target is **strong Main / Outstanding-shaped work**, not the median accepted paper and not Findings as the aspiration.

## Reference papers to emulate

### ACL 2025 Outstanding — *Llama See, Llama Do*
https://aclanthology.org/2025.acl-long.791/

What to learn: the paper does not stop at “irrelevant context distracts models.” It identifies a lower-level regularity — prior token occurrence itself raises propensity for that token, even for random tokens — and then connects a mechanistic intervention back to the behavioral failure.

### EMNLP 2025 Outstanding — *Causal Interventions Reveal Shared Structure Across English Filler–Gap Constructions*
https://aclanthology.org/2025.emnlp-main.1271/

What to learn: the scientific question predates the interpretability method. Causal interchange is valuable because it adjudicates whether apparently different constructions share abstract structure. Mechanism is evidence for a theory question, not an end in itself.

### EMNLP 2025 Outstanding — *Mind the Value-Action Gap*
https://aclanthology.org/2025.emnlp-main.154/

What to learn: a top paper can advance the field by changing the evaluation object. “What a model says it values” and “what it does” are different scientific quantities. The conceptual separation matters more than having a circuit diagram.

### NAACL 2025 Main — *Racing Thoughts*
https://aclanthology.org/2025.naacl-long.155/

What to learn: propose an algorithmic hypothesis that makes directional causal predictions. Backpatching/frozen-backpatching is strong because it manipulates processing order and rules out the simpler “more computation” account.

### ACL 2026 Main — *Do LLMs Know Tool Irrelevance?*
https://aclanthology.org/2026.acl-long.1473/

What to learn: define latent variables first, then build an instrument that orthogonalizes them. Structural alignment and semantic relevance are independently controlled; competing pathways then directly explain why the wrong action wins.

### ACL 2025 Main — *Stochastic Chameleons*
https://aclanthology.org/2025.acl-long.1458/

What to learn: generic irrelevant-context failure is already crowded territory. A publishable explanatory step needs a more specific regularity or abstraction than “distractors hurt.”

### NAACL 2025 Main — *SCIURus*
https://aclanthology.org/2025.naacl-long.618/

What to learn: mechanism answers a crisp alternatives question — shared or separate circuitry for factuality and uncertainty — across multiple models/datasets.

### NAACL 2025 Main — *The LLM Language Network*
https://aclanthology.org/2025.naacl-long.544/

What to learn: the natural question is functional specialization; ablation is used to establish causal task relevance, not to manufacture novelty after the fact.

### EMNLP 2025 Main — *Reason to Rote*
https://aclanthology.org/2025.emnlp-main.437/

What to learn: ask how two phenomena relate algorithmically (memorization and reasoning) rather than looking for a “memorization neuron.” A surprising relationship can itself be the explanatory contribution.

### ACL 2026 Main — *Privacy Collapse*
https://aclanthology.org/2026.acl-long.400/

What to learn: first establish a natural, consequential phenomenon, then use mechanism to explain differential fragility. The paper identity is the phenomenon, not the probe.

### ACL 2026 Main — *How Memory Management Impacts LLM Agents*
https://aclanthology.org/2026.acl-long.27/

What to learn: a strong Main paper can be organized around a newly characterized behavioral regularity (experience-following) when that regularity explains downstream failures and design consequences.

## The eight gates for this project

A proposed main-paper claim should pass all eight.

1. **Natural question.** Can be stated in one sentence without dataset, metric, model, or method names.
2. **Scientific object.** Exists independently of the chosen benchmark.
3. **Instrument follows the question.** Dataset/manipulation is built to isolate an already-defined variable, not vice versa.
4. **Novel explanatory step.** Goes below the coarse known failure into a sharper variable, relation, or algorithmic distinction.
5. **Related-work separation.** The novelty is not “prior work did not test our benchmark/model.” State what conceptual variable or causal relation is new.
6. **Experiment coherence.** Main experiments form one descending explanatory tree; failed/dead-end conditions do not become equal-weight sections.
7. **Claim robustness.** A failed favorite mechanism should not force us to change the natural question after seeing results.
8. **Mechanism necessity.** Open the model only when two accounts predict the same outputs but differ internally, or when the intervention directly explains the headline failure.

## Current project score against the bar

### Natural question — strong

> After learning how something turned out, can a language model still condition a reconstructed past judgment only on the information available beforehand?

This is broader and cleaner than forecasting accuracy. It is a question about **retrospective epistemic reconstruction / information-set conditioning under hindsight**.

### Current explanatory descent — Main-shaped

```text
recognized temporal boundary
    ↓
future evidence still causally changes the reconstructed judgment
    ↓
unrelated outcome-shaped future evidence produces donor-directed pull
    ↓
paired donor-outcome replacement controls direction, with heterogeneous magnitude
    ↓
in the strong-effect model, influence becomes causally actionable in a late recipient-conditioned answer state
```

This is substantially stronger than “future information leaks” or “irrelevant context distracts.”

### Where the paper is not yet Outstanding-closed

The late decision-state result explains **where/how outcome influence becomes causally actionable**, but not yet **why an information boundary the model can recognize fails to gate that pathway**.

That missing closure should not be patched with more benchmark breadth or prompt controls. If we pursue it, the experiment must discriminate competing algorithms for boundary/outcome interaction.

## Strict claim language

Prefer:

- “outcome-shaped future evidence from unrelated resolved events produces directional retrospective pull”;
- “replacing a NO-supporting irrelevant packet with a YES-supporting packet raises the same reconstructed probability”;
- “magnitude is strongly model-dependent; the preregistered 5pp panel gate is indeterminate”;
- “in Gemma, future-outcome influence becomes causally actionable in a late recipient-conditioned answer-position state.”

Avoid:

- “changing only the outcome” (packet identity/semantics also change in G12);
- “robust causal outcome entrainment across models”;
- “a dedicated hindsight axis/circuit”;
- “the mechanism of hindsight contamination” without qualification;
- “we are first to show models know a temporal rule but violate it.”

## Decision rule for further work

For a Main submission, the default is to **stop adding experiments** and improve paper density, figures, novelty boundaries, and wording.

For an Outstanding-level attempt, run a new experiment only if all existing evidence through G15 is consistent with two explicitly stated algorithms and a prospective intervention makes opposite predictions. The most promising question is whether the boundary/admissibility representation causally gates, competes with, or merely coexists with the late outcome pathway.
