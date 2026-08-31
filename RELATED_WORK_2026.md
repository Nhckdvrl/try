# Related work and novelty boundary — current temporal paper

This file is the **binding novelty note for the current hindsight-contamination
paper**. Earlier multi-family Information-Set Reasoning plans are no longer the
submission target.

The paper's central object is:

> **the causal effect of explicit future evidence on an otherwise identical
> reconstructed historical judgment, while separately measuring whether the
> model recognizes that the evidence lies outside the target time.**

The novelty is therefore **not** the generic observation that models use future
information, exhibit hindsight-like bias, or can state a temporal rule and still
violate it.

---

## 1. Closest neighbour: temporal legal reasoning

### *When Do LLMs Apply the Wrong Law? Diagnosing LLM Failures in Temporal Legal Reasoning* (2026)

This is the closest neighbour to the paper's recognition–enforcement framing.
It reports that models are biased toward newer statute versions; the same models
can state the temporal-applicability rule correctly and demonstrate knowledge of
the older statute, yet still apply the wrong vintage to a concrete case.

URL: https://arxiv.org/abs/2608.14610

### Binding consequence

We must **not** write:

> We are the first to show that LLMs understand a temporal boundary but fail to
> obey it.

That priority claim is unavailable.

The distinction we can defend is methodological and quantitative:

- the legal work studies **version selection** among legal texts;
- our design holds one question and one future evidence packet fixed and
  directly manipulates whether that packet is present and whether it is licensed
  for the target judgment;
- our outcome is a continuous probability shift, not only a right/wrong version
  choice;
- boundary recognition is measured per item and is near ceiling rather than
  inferred from a separate task.

Locked novelty formulation:

> **We causally manipulate the presence and admissibility of the same explicit
> in-context future evidence, measuring how much that evidence shifts an
> otherwise identical reconstructed historical judgment.**

---

## 2. Ex-ante reasoning and temporal leakage

### ExAnte (EACL 2026)

ExAnte studies whether models reason as if they were located at an earlier time
when their parameters may already contain later facts. It establishes temporal
leakage / ex-ante inference as an existing problem.

This means the paper cannot be sold as:

> LLMs know future events and accidentally use them when asked to reason about
> the past.

Our stronger distinction is that **knowledge availability is experimentally
controlled in context**. We insert the same later packet and compare its causal
effect under ex-ante versus retrospective admissibility.

This separates:

```text
Does the model possess later information?
from
Does the model use explicitly supplied later information when the task says it
lies outside the target historical information set?
```

---

## 3. Human hindsight / outcome-bias literature

Human work has long shown that knowing an outcome can distort evaluations of
what was knowable or reasonable beforehand.

### Aiyer et al. (2023)

**Outcomes Affect Evaluations of Decision Quality: Replication and Extensions of
Baron and Hershey's (1988) Outcome Bias Experiment 1**

- preregistered replication;
- `N=692`;
- outcome information changes evaluation of the prior decision;
- the effect can persist even among participants who explicitly state that
  outcomes should not matter.

URL: https://osf.io/knjhu/

### Boundary

The current paper is **not** a claim that LLMs reproduce a human psychological
bias in the same sense. Human hindsight/outcome-bias work motivates the problem;
our LLM contribution is the causal same-evidence design, per-item temporal
recognition probe, model comparison, and follow-up interventions.

Use "hindsight contamination" as an operational description, not as evidence of
human-equivalent cognition.

---

## 4. Curse of knowledge / privileged-state contamination

Several literatures already show that possessing privileged information can
contaminate judgments about an uninformed state.

### Human curse of knowledge

Work on predicting other people's knowledge shows that learning an answer can
bias estimates of what an uninformed person would know.

Example materials: https://osf.io/2ngbq/

### ComplexEval (Findings of EMNLP 2025)

**Curse of Knowledge: When Complex Evaluation Context Benefits yet Biases LLM
Judges** studies auxiliary-information-induced bias in LLM evaluation.

URL: https://aclanthology.org/2025.findings-emnlp.805/

### Answer-side intrusion in LLM query simulation (2026)

Recent work traces concepts from answer-side documents into generated queries
that are intended to simulate a pre-search user state.

URL: https://arxiv.org/abs/2608.25245

### Boundary

Therefore "LLMs are contaminated by privileged knowledge" is not a sufficient
novelty claim.

Our paper requires all three simultaneously:

1. the later information is demonstrably useful when licensed;
2. the model identifies it as outside the ex-ante information set when
   unlicensed;
3. supplying that same unlicensed information still causally changes the
   decision.

---

## 5. In-context forgetting and selective non-use

### ICF-Bench (ICLR 2026)

**Do LLMs Forget What They Should? Evaluating In-Context Forgetting in Large
Language Models** studies selective contextual forgetting while retaining useful
context.

URL: https://proceedings.iclr.cc/paper_files/paper/2026/hash/b13d00a62d438856cfe6fbd13b6b2cb8-Abstract-Conference.html

### Boundary

Our desired state is not necessarily "the model can no longer recall the fact".
The future packet may remain visible and answerable. The requirement is narrower:

```text
future evidence remains available
but
its causal effect on the ex-ante judgment should be ~0
```

So the current paper is about **decision influence under a temporal information
boundary**, not forgetting as a memory objective.

---

## 6. Continued influence and misinformation retraction

The Continued Influence Effect literature studies persistent use of
misinformation after correction or retraction. This is related but differs in
the epistemic status of the evidence.

In our core task the future evidence can be **true, useful, and perfectly
remembered**. It is excluded because it was unavailable at the historical time,
not because it is false.

This distinction matters: the model is not being asked to revise its belief that
the future packet is true; it is being asked to reconstruct a judgment from an
earlier information state.

---

## 7. Generic irrelevant-context and distractor robustness

There is extensive prior work showing that irrelevant context or competing
signals can alter LLM answers. Therefore:

> irrelevant information changes model behavior

is not a contribution by itself.

Our packet is also not "irrelevant" in the ordinary sense: the same packet is
highly useful in the retrospective licensed condition. The scientific question
is whether the model can condition **causal use** on the target time.

---

## 8. Security / information-flow work

Security and privacy research already uses information-flow and noninterference
language for LLM agents.

Examples include:

- **Fides / Securing AI Agents with Information-Flow Control** —
  https://arxiv.org/abs/2505.23643
- **AgentSecBench** — https://arxiv.org/abs/2605.26269
- **Ghost in the Agent / NeuroTaint** — https://arxiv.org/abs/2604.23374
- **CoPriva (EMNLP 2025)** — https://github.com/hwanchang00/CoPriva

We therefore do **not** claim that noninterference, taint, policy labels, or
forbidden-information flow are new framings.

The present paper differs in object:

| Security / privacy work | Current paper |
|---|---|
| disclosure, injection, forbidden action | continuous change in a legitimate probability judgment |
| often adversarial / untrusted information | accurate future evidence that is merely too late |
| system-level enforcement | model's own temporal-boundary compliance |
| leakage/action success | paired causal sensitivity of a historical judgment |

---

## 9. Self-anchoring and why the commitment experiment was dropped

*Competing Biases underlie Overconfidence and Underconfidence in LLMs* (Nature
Machine Intelligence, 2026; doi:10.1038/s42256-026-01217-9) reports that exposing
a model to its own prior answer can induce choice-supportive anchoring.

This makes a "show the model its earlier probability, then ask it to maintain the
past state" manipulation fundamentally confounded. The earlier M3 commitment
idea is therefore not part of the current paper and should not be revived as a
mechanism result.

---

## 10. Current contribution boundary

### What the paper can claim

- A preregistered **recognition–enforcement gap** under a within-item causal
  manipulation of the same future evidence.
- The effect is prospectively confirmed on 64 fresh BTF-3 questions and
  independently replicated on 256 additional unseen questions.
- Boundary recognition is 99.2–100% in the 256-unit round while future evidence
  still shifts ex-ante judgments by 7.46–27.73 probability points across the
  three primary checkpoints.
- Removing explicit YES/NO verdict sentences does not eliminate contamination,
  so the effect is **not reducible to explicit-label copying**.
- Within available dense Qwen3.5 checkpoints, scale does not monotonically
  remove the failure.

### What the paper cannot claim

- first observation of temporal-rule recognition without behavioral compliance;
- cross-source replication;
- generality across temporal, perspective, procedural, role/access, or privacy
  boundaries;
- a universal "information-set reasoning" failure;
- a neural / representation-level mechanism;
- an independently replicated exclusion-specific positional mechanism;
- a scaling law;
- that verdict-redacted evidence is non-revealing;
- complete factual certification of the BTF-3 packets.

---

## 11. One-sentence paper novelty

> **Language models can identify with near-ceiling accuracy that evidence
> postdates the historical moment they are asked to reason from, yet supplying
> that same evidence still causally shifts their reconstructed ex-ante judgment
> by a large and independently replicated margin; the effect survives removal
> of explicit resolution labels and is not eliminated by model scale within the
> tested Qwen3.5 family.**
