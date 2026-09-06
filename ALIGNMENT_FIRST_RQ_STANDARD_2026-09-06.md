# Alignment-First Research Question Selection Standard — 2026-09-06

**Target:** NAACL Main, calibrated against ACL / EMNLP / NAACL Main and especially Best / Outstanding / Best Theme papers.  
**Status:** current project-level RQ-selection standard.  
**Supersedes for future promotion decisions:** the earlier promotion standard when the two conflict. Older files remain provenance.

---

# 0. Governing rule

Research-question selection must be calibrated against **real high-level papers before experiment design**.

The project must not ask only:

> Has anyone run this exact condition?

It must ask:

> Does the question itself belong naturally beside current high-level ACL / EMNLP / NAACL work, and does the proposed new axis change an observable or causal prediction?

The workflow is:

```
high-level paper calibration
→ paper identity
→ important scientific object
→ unresolved independent axis / framing / mechanism
→ prediction-changing contrast
→ literature assassination
→ reviewer compression
→ minimum decisive pilot
→ actual one-sentence law
→ post-result literature re-audit
→ Main-vs-Findings re-calibration
```

---

# 1. Human cognition / linguistics / philosophy are valid sources of research questions

A concept being old in humans does **not** kill an LLM/NLP paper.

Recent high-level examples make this explicit:

- EMNLP 2025 Outstanding **Mind the Value-Action Gap** studies a classic psychology-style value/action distinction in LLMs.
- ACL 2026 Outstanding **Mind the (DH) Gap!** transfers a classic description–experience distinction from human risky choice and finds a new reasoning-vs-conversational model regime split.
- ACL 2026 Best Paper **The Imperfective Paradox in Large Language Models** takes a classic semantic phenomenon and discovers a pervasive LLM-specific Teleological Bias.
- ACL 2026 Main **CogToM** builds a ToM benchmark directly inspired by 46 human-cognition paradigms and analyzes LLM/human cognitive divergence.
- ACL 2026 Best Theme **CoSToM** studies ToM with causal intervention.

Therefore:

> **Human-origin phenomenon is a theoretical anchor, not a novelty failure.**

What is weak is only:

> “Humans show X; LLMs also show X.”

A human-origin question becomes strong when the AI study reveals a new system-level law, such as:

- a model-family / training regime split;
- a systematic divergence from humans or a normative theory;
- a stable structural failure;
- a recognition/use or representation/behavior dissociation specific to models;
- a model-specific causal mechanism;
- a downstream consequence important for deployed assistants/agents.

References:
- https://2025.emnlp.org/program/awards/
- https://aclanthology.org/2025.emnlp-main.154/
- https://aclanthology.org/2026.acl-long.479/
- https://2026.aclweb.org/program/best_papers/
- https://aclanthology.org/2026.acl-long.1448/
- https://aclanthology.org/2026.acl-long.421/

---

# 2. Mandatory High-Level Calibration Set

Before a serious candidate is experiment-authorized, collect:

- at least 3 high-level same-identity anchors when available;
- 3–5 strong Main / direct neighboring papers;
- very recent 2025–2026 assassination papers.

For each anchor record:

| field | required question |
|---|---|
| paper identity | behavioral discovery / mechanistic discovery / method / benchmark / audit / use-inspired / theory |
| one-sentence RQ | what does the paper actually ask? |
| why important | why care without method or dataset names? |
| novelty type | new axis / framing / mechanism / method / benchmark / audit |
| claims | how many load-bearing claims? |
| data | why this scale/complexity? |
| models | why this breadth? |
| decisive evidence | what identifies C1? |
| mechanism | necessary / optional / irrelevant? |
| Main case | why is this more than a narrow sound result? |

---

# 3. Paper identity comes before evidence burden

There is no universal Main-paper template.

Possible identities:
1. Scientific / Behavioral Discovery
2. Mechanistic Discovery
3. Method / Algorithm
4. Benchmark / Resource
5. Critical Audit / Negative Result
6. Use-Inspired Scientific Work
7. Theory / Formalization
8. Measurement / Evaluation Methodology
9. Human-Science-at-Scale / Old-Workflow-New-Method

Rules:
- behavioral discovery does not automatically require mechanistic intervention;
- mechanistic discovery requires causal evidence as load-bearing support;
- method papers must identify and repair a real limitation;
- benchmark/resource papers need principled coverage, validity, and usefulness;
- negative-result papers must change understanding of an important expectation.

Do not invent an experiment burden stricter than comparable successful papers.

---

# 4. Candidate gates

## P1 — High-Level Alignment
Real high-level same-identity anchors exist and were compared.

## P2 — Interesting Question
Deleting dataset/method/model names leaves a question the community should care about.

## P3 — One-Minute Intelligibility
No project ontology is required to explain it.

## P3b — Non-Obviousness / Scientific-Tension Gate

A Main-level behavioral/scientific question must be interesting **before** the model is run.

Default KILL form:

> “Theory says X and Y are different. Does the model know/distinguish X and Y?”

This is usually a textbook-capability check even when the distinction is real, the dataset is excellent, and the exact LLM experiment is novel.

Before compute, every serious candidate must state:

1. **What is the tension?** Which two individually plausible principles, representations, or behaviors make different predictions?
2. **Why is the answer not obvious from the definition of the construct?**
3. **What would surprise an informed ACL/EMNLP/NAACL reader?**
4. **Why does the question matter even if the model gets the textbook distinction correct?**
5. **What structural model law could the design identify without result-hunting?**

High-level positive shapes include:
- **invariance violation:** the same relevant information yields different behavior under an ostensibly irrelevant representation/task change;
- **representation–use / statement–action dissociation:** the model can express the right rule/state yet behavior does not follow it;
- **irrelevant-information leakage:** information that should not matter systematically changes generation or judgment;
- **prior–semantics conflict:** a learned model prior overrides a licensed linguistic/semantic computation;
- **training-regime split:** a natural computation changes qualitatively with post-training/model regime;
- **unexpected causal dependence:** an intervention reveals that the apparent competence is supported by a different computation.

Calibration examples:
- NAACL 2025 *Semantic Leakage*: irrelevant information changes generation.
- EMNLP 2025 Outstanding *Value-Action Gap*: stated values and actions diverge.
- ACL 2026 Outstanding *Mind the (DH) Gap!*: equivalent risky-choice content behaves differently under description vs experience, with a reasoning/conversational regime split.
- ACL 2026 Best *Imperfective Paradox*: a model-specific Teleological Bias overrides the compositional distinction.

**Rule:** good data cannot rescue an obvious question.

## P3c — Structural Specificity Gate

A generic gap, inconsistency, or invariance violation is no longer sufficient novelty by itself.

Before promotion, ask:

> **What object-specific mathematical, causal, linguistic, statistical, or decision-theoretic relation makes this divergence scientifically diagnostic?**

If recent work already owns the parent notion of cross-readout/task consistency, a new readout pair is presumed non-novel unless it provides at least one of:

1. a distinct structural estimand;
2. a distinct causal law;
3. a distinct competing-theory diagnostic;
4. an independently grounded mapping whose violation rules out a plausible account;
5. a diagnostic subset where competing accounts make different qualitative predictions.

Default weak form:

> “A and B should be consistent; do LLMs violate this?”

That is generally an exact cell.

**Rule:** the structural relation should exist before the gap.

## P3d — Old-Problem / New-Method Gate

Methodological papers are explicitly welcome, including old human/language-science workflows newly enabled by LLMs.

But “LLM automates X” is not enough.

A serious method candidate must state:

1. **Old bottleneck:** what scientifically important workflow/problem existed before LLMs?
2. **LLM-specific affordance:** what is genuinely newly feasible now?
3. **Scientific delta:** what experiment, measurement, falsification, or inference becomes possible—not merely cheaper?
4. **External substrate:** what independently existing data/gold/archive validates the method?
5. **Reviewer compression:** why is this not “use ChatGPT to do X”?
6. **Workload realism:** can the load-bearing claim be established without building a giant platform or collecting a bespoke benchmark?

Strong pattern:

> old workflow + explicit historical limitation + new LLM affordance + external data + falsifiable scientific improvement.

Weak pattern:

> old task + LLM substitution.

## P3e — Crowdedness / Workload Gate

Independent novelty is necessary but not sufficient when the surrounding field is already saturated.

Treat heavy 2025–2026 crowding as a negative prior, especially when many papers differ mainly by dataset or prompt.

Currently high-risk generic neighborhoods include:
- LLM-as-annotator;
- LLM interviewer / conversational survey;
- generic AI-generated stimuli;
- generic cognitive-bias benchmarking;
- generic prompt/readout consistency;
- generic agentic scientific discovery;
- generic LLM-as-judge.

Prefer questions whose decisive C1 can be established with a small, principled experiment and which do not require an agent/RL/model-zoo arms race merely to look competitive.

## P4 — Correct Paper Identity
The expected contribution type is explicit.

## P5 — Appropriate Scope
Scope is calibrated against real Main / Outstanding papers, not intuition.

## P6 — Independent Scientific Novelty
The novelty is not merely an exact benchmark cell.

## P7 — Prediction Difference
Write:

```
existing account predicts: ...
new axis predicts: ...
decisive case where they disagree: ...
```

If no prediction or intervention changes, the axis is probably taxonomy rather than contribution.

## P8 — Literature Survival
Search exact phenomenon, parent abstraction, adjacent construct, same prediction, same causal mechanism, same benchmark family, recent work, and neighboring disciplines.

## P9 — Reviewer Compression Survival
Write:

> “This is just X.”

A valid rebuttal needs a different prediction, dissociation, causal implication, or intervention—not a different dataset.

## P10 — Outcome Robustness
For discovery work, several plausible outcomes should teach us something:
factorized / shared / asymmetric / represented-but-unused / systematic negative / family split.

## P11 — Strong Inference
State H1/H2/H3 before pilot and design a test that discriminates them.

## P12 — Data Fit / Data-First Gate
Data is part of the research question, not an implementation detail.

Prefer, in order:
- **D0:** existing dataset already measures the construct;
- **D1:** existing natural dataset, new annotation/readout only;
- **D2:** independently published human/linguistic experimental materials with minimal adaptation;
- **D3:** natural-corpus retrieval plus minimal controlled edits;
- **D4:** new hand-written/template minimal pairs;
- **D5:** custom synthetic world/ontology created to make the effect exist.

Promotion policy:
- D0–D2 are strong advantages;
- D3 is acceptable with auditable local interventions and independent validation;
- D4 is high risk and requires same-identity high-level precedent, strong human/native validation, lexical/template diversity, and a second substrate;
- D5 is default KILL for behavioral/scientific-discovery work unless the synthetic formal system is itself the scientific object.

Synthetic material may isolate a natural variable; it may not manufacture the ontology that makes the question exist.

Before compute, record:
1. exact source/provenance of the data or materials;
2. why they existed independently of our hypothesis;
3. what is original vs transformed vs newly generated;
4. source of gold labels;
5. expected human disagreement and validation plan;
6. template/artifact risk;
7. contamination risk;
8. second-substrate/generalization plan when the claim requires it.

**Rule:** the question may be deep; the data path must be shallow.

## P13 — Non-Trivial Result Space
Write before experiments:

> **What would be trivial even if positive?**

## P14 — Claim-Matched Model Coverage
`claim breadth → model breadth`. No fixed model count.

## P15 — Realistic Evidence Burden
Follow actual high-level papers, not imagined reviewer requests.

## P16 — Research-Space Depth
The scientific object should naturally support a coherent Main-scale story without becoming an experiment zoo.

## P17 — Explicit Kill Rules
Know before running what would terminate the direction.

---

# 5. Required Candidate Card

Every serious candidate records:

1. Research Question
2. Paper Identity
3. Why it matters
4. One-example explanation
5. Scientific axis
6. Generative structure
7. Competing hypotheses
8. Decisive prediction
9. High-Level Calibration Set
10. Top-Paper Alignment Matrix
11. Literature-Axis Matrix
12. Adjacent concepts
13. Reviewer Kill Sentence
14. Is that compression valid?
15. Outcome Robustness
16. Research-space width
17. Minimal Discovery Substrate
18. Data risks
19. What would be trivial?
20. Model-coverage rationale
21. Claim architecture
22. Pilot Kill Criteria
23. Post-result re-audit rule
24. Expected Main-level growth path
25. Verdict

---

# 6. Pilot rule

Pilot is a **discovery instrument**, not a mini paper.

Its purpose is:

> Is there an actual structural law here worth building a paper around?

Use the minimum experiment that distinguishes the competing accounts.

After the pilot:
1. write one sentence, without numbers: **“Models …”**
2. assassinate that exact law against the latest literature;
3. compare the law again to high-level anchors;
4. decide Main / Findings / supporting evidence / KILL;
5. only then design C2/C3.

No SAE / patching / steering / model zoo is authorized merely because a behavioral effect is non-zero.

---

# 7. Kill hygiene

Every killed lane must record:
- direct scientific reason;
- collision / parent axis;
- reviewer compression;
- data failure when applicable;
- explicit note against terminology-based resurrection.

A killed neighborhood can return only with a genuinely different prediction-changing axis.

---

# 8. Project-specific warning

This repository has repeatedly over-valued:
- exact-gap novelty;
- large effects;
- elegant matched-observation designs;
- mechanistic assets;
- code/data readiness;
- sunk cost.

Those are not promotion arguments.

Priority is:

```
high-level-paper-calibrated importance
>
clear paper identity
>
independent prediction-changing axis / framing
>
outcome robustness
>
clean identification
>
**data provenance / naturalness / gold robustness**
>
non-obvious finding space
>
Main-scale depth
>
appropriate mechanism
>
appropriate model breadth
>
defensive completeness
```

---

# 9. One-sentence authority

> **A candidate earns compute only when real high-level papers establish that its question is appropriately scaled and non-obvious before results, its novelty is a load-bearing scientific difference rather than an exact gap, its axis exposes a genuine tension and changes predictions, multiple outcomes remain informative, its substrate does not manufacture the object, and its evidence burden matches its actual paper identity.**
