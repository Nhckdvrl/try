# Related-work and novelty boundary — 2026-08-29

> **Information-set scope reset.** The paper-level object is whether models
> construct the licensed information set for a target decision across temporal,
> perspective, procedural, role/access, and decision-scope boundaries.
> Policy-conditioned causal non-use is one mechanistic subcase, not the mother
> contribution.

Claims explicitly unavailable as novelty include selective contextual forgetting
(ICF-Bench), ex-ante use of future information (ExAnte), multi-party information
asymmetry (FANToM), the invariant-to-forbidden/responsive-to-licensed causal
contract (Resist and Update), and conditional-rule update failure
(MedPIC-Bench). Novelty is conditional on source-native cross-boundary evidence,
held-out transfer, and the resulting shared-capability versus fragmented-
heuristics test.

This note exists to prevent the project from drifting into a claim that adjacent work has already occupied.

## 1. The core distinction

Our intended object is **not** “can the model forget a fact?” It is:

> The information remains available and recallable, but an explicit policy says it must make no causal contribution to a particular downstream decision.

The cleanest phrase is **policy-conditioned causal non-use**. A formal noninterference view is useful, but the term/noninterference framing itself is not novel.

---

## 2. In-context forgetting: directly adjacent, but a different target state

### Qian et al. (ICLR 2026), ICF-Bench

**Do LLMs Forget What They Should? Evaluating In-Context Forgetting in Large Language Models**

- ICF is defined as selectively forgetting interference information while retaining useful contextual knowledge, without parameter updates.
- ICF-Bench contains 2,000 multi-turn dialogues drawn from realistic scenarios.
- The desired behavior is often that the forgotten information should cease to be available for the later task.

URL: https://proceedings.iclr.cc/paper_files/paper/2026/hash/b13d00a62d438856cfe6fbd13b6b2cb8-Abstract-Conference.html

### Boundary

Our successful model is allowed to answer a memory probe about the excluded information. The normative requirement is instead:

```text
memory(E) may remain high
causal_effect(E -> specified decision | deny policy) should be ~0
```

Therefore a paper that only says “the model still uses something after being told to forget/ignore it” is not enough. The retention/non-use dissociation must be explicit.

---

## 3. Human inadmissible-evidence research: origin and external anchor

### Steblay et al. (2006)

Meta-analysis of judicial instructions to disregard inadmissible evidence: 48 studies, 8,474 participants, 175 hypothesis tests. The human effect is robust enough to motivate the question, but the individual paradigms are heterogeneous.

### Kassin & Sommers (1997)

A particularly important moderator: exclusion because evidence is **unreliable** does not behave like exclusion because otherwise-informative evidence was **illegally obtained**. That maps naturally onto `false_or_unreliable` versus `true_but_forbidden`.

### Engel, Golder & Rahal (2026)

**Who Is Afraid of the Pink Elephant? Evidence on (Not) Ignoring Inadmissible Evidence and Debiasing Interventions**

- 1,432 US participants.
- Studies prior-conviction character evidence and wiretap-confession evidence.
- The manipulations do not all yield the same bias.
- Multiple debiasing interventions reduce some effects without making the entire problem disappear.

URL: https://doi.org/10.1002/bdm.70064

### Boundary

The project should not be sold as “LLMs have a human cognitive bias.” Human work supplies natural experimental structures and expected heterogeneity. The LLM contribution must concern model behavior/computation.

---

## 4. Outcome bias: a true-but-temporally-out-of-bounds family

### Aiyer et al. (2023)

**Outcomes Affect Evaluations of Decision Quality: Replication and Extensions of Baron and Hershey's (1988) Outcome Bias Experiment 1**

- preregistered replication, `N=692`;
- successful outcome-bias replication;
- the effect remains even among participants who explicitly state that outcomes should not matter;
- materials/data/code are available at OSF `knjhu`.

URL: https://osf.io/knjhu/

### Why it matters here

The outcome can be entirely true and perfectly remembered, yet it is logically outside the information set that should determine an **ex-ante** decision-quality judgment. This is much closer to our mother phenomenon than ordinary misinformation correction.

---

## 5. Curse of knowledge / privileged-state contamination

### Human work: predicting others' knowledge

**The “curse of knowledge” when predicting others’ knowledge** (2022)

- four experiments;
- 40 general-knowledge trivia questions;
- independent novice accuracy from 100 participants;
- learning the answers contaminates estimates of what uninformed others know;
- data and analysis code available at OSF `2ngbq`.

URL: https://osf.io/2ngbq/

This is a high-priority external source because it has a measured target and no legal wrapper.

### LLM work: ComplexEval (Findings of EMNLP 2025)

**Curse of Knowledge: When Complex Evaluation Context Benefits yet Biases LLM Judges**

ComplexEval systematically studies auxiliary-information-induced biases in LLM judges across multiple scenarios.

URL: https://aclanthology.org/2025.findings-emnlp.805/

### Very recent LLM work: answer-side intrusion (arXiv 2026-08-26)

**The “Curse of Knowledge” in LLM Query Simulation: Concept Provenance for Tracing Answer-Side Intrusion**

- 77,004 generated queries;
- 100 UQV100 topics;
- 8 LLMs and 5 prompt conditions;
- detects concepts originating from answer-side documents that should be outside the simulated pre-search user's information state.

URL: https://arxiv.org/abs/2608.25245

### Boundary

These works make “models are contaminated by auxiliary/privileged knowledge” an unsafe novelty claim by itself. Our distinctive test must include an explicit **decision-use policy**, direct causal sensitivity measurement, and the retention-vs-use dissociation.

---

## 6. Continued influence / misinformation retraction

The Continued Influence Effect (CIE) is the persistent use of misinformation after correction/retraction. It is important but lives mainly on the **epistemic invalidation** side of our taxonomy.

A useful timing result is Buczel et al. (2024): in two experiments (`N=337`), forewarnings reduced later reliance on misinformation, whereas post-warnings did not produce the same protection, despite memory for the retraction.

URL: https://doi.org/10.3758/s13421-024-01520-z

### Boundary

This literature is a reason **not** to make the controlled CDS-v1 Pre/Post sign universal. It also demonstrates that false/retracted information is already a mature research area. Our strongest novelty should come from true-but-disallowed information and policy-conditioned decision influence.

---

## 7. Forbidden information in selection

### Oien & Goernert (2003)

**The Role of Intentional Forgetting in Employee Selection**

Participants evaluated four applicants; one contained both job-relevant and forbidden information. Some participants were told before reviewing applications which information types were forbidden and were instructed to disregard them.

URL: https://doi.org/10.1080/00221300309601278

### Boundary

This is an excellent natural prospective paradigm, but the source is not obviously open for stimulus redistribution. It is a candidate to obtain from the authors/library, not a license to recreate the exact materials from a paywalled paper.

---

## 7b. Temporal legal reasoning: the closest published neighbour (2026)

### *When Do LLMs Apply the Wrong Law? Diagnosing LLM Failures in Temporal Legal Reasoning* (arXiv 2608.14610)

This is now the nearest published work to our headline framing, and it must be
treated as such rather than discovered by a reviewer. It reports that models
are strongly biased toward the most recent version of a statute; that the same
models can state the temporal-applicability rule correctly and demonstrate
knowledge of the older statute; and that they nevertheless apply the wrong
(newer) law when deciding a concrete case.

That is structurally the same shape as our recognition–enforcement gap, on a
different substrate.

### Consequence for our claims — binding

We must **stop writing** any version of:

> We are the first to show that models understand a temporal boundary yet fail
> to obey it.

That sentence is no longer defensible. The surviving distinction is about the
*object of measurement*, not about who noticed the phenomenon first:

- their failure is **version selection**: among several candidate legal texts,
  the model retrieves and applies the wrong-vintage one;
- ours is a **causal manipulation of one fixed piece of evidence**: the same
  judgment, the same question, the same packet, present or absent, admissible
  or inadmissible, with the effect measured as a continuous probability shift
  on hundreds of independently sampled natural questions.

The locked formulation is:

> **We causally manipulate the presence and admissibility of the same explicit
> in-context future evidence, measuring how much that later evidence shifts an
> otherwise identical reconstructed historical judgment.**

Two further separations survive and should be stated positively rather than as
priority claims: our boundary recognition is measured per item and is at
ceiling (99.2–100%), so the gap is quantified rather than inferred; and the
positional and verdict-redaction experiments ask *why* the gap exists and
whether it reduces to answer copying, which version-selection work does not
address.

### Boundary

Adjacent and partially overlapping in phenomenon. Different in domain,
different in manipulation, different in estimand. Cite prominently, concede the
overlap in the introduction, and do not compete on novelty of the observation.

## 7c. Self-anchoring on one's own prior answer (2026)

*Competing Biases underlie Overconfidence and Underconfidence in LLMs* (Nature
Machine Intelligence, 2026; doi:10.1038/s42256-026-01217-9) reports that
exposing a model to its own prior answer induces choice-supportive anchoring
that makes it hold that answer more firmly.

This is why the M3 "restate your prior assessment" manipulation is dropped
rather than redesigned: any reduction in intrusion under such a design is
confounded between the intended temporal-state persistence and plain
self-anchoring, and a non-numeric variant does not remove the confound. The
decision is recorded in `PREREGISTRATION_G2_HINDSIGHT_DEPTH.md`.

## 8. Agent security and information-flow control: noninterference is already occupied

### Fides / Microsoft Research (2025)

**Securing AI Agents with Information-Flow Control**

Fides attaches confidentiality/integrity labels, tracks information flow, and deterministically enforces policies. It explicitly argues for system-level information-flow control rather than trusting natural-language prompt instructions as a security boundary.

URL: https://arxiv.org/abs/2505.23643

### AgentSecBench (2026)

**AgentSecBench: Measuring Prompt Injection, Privacy Leakage, and Tool-Use Integrity in LLM Agents**

The framework explicitly uses a notion of **intent-to-execution noninterference with permitted leakage**, and distinguishes prompt annotations from enforcing projections. Its exact-marker games concern disclosure and forbidden actions under adversarial conditions.

URL: https://arxiv.org/abs/2605.26269

### Ghost in the Agent / NeuroTaint (2026)

**Ghost in the Agent: Redefining Information Flow Tracking for LLM Agents**

NeuroTaint treats LLM-agent flow as including semantic transformation and **causal influence on decisions**, not only literal string transfer. TaintBench spans 400 scenarios over 20 agent frameworks.

URL: https://arxiv.org/abs/2604.23374

### CoPriva (EMNLP 2025)

CoPriva evaluates contextual non-disclosure policies with 4,184 QA pairs and direct/indirect attacks, grounded in meeting-style contexts.

URL: https://github.com/hwanchang00/CoPriva

### Boundary

We must not claim:

- that LLM agents lack information-flow boundaries as a new observation;
- that “noninterference” is a new framing;
- that structured labels/projections are a new mitigation concept;
- that semantic causal influence from untrusted information has never been studied.

A viable distinction is:

| Security / privacy work | This project, if validated |
|---|---|
| secret disclosure / prompt injection / forbidden action | continuous semantic change in an otherwise legitimate decision |
| adversarial untrusted source | information may be accurate and benign, but out of bounds for this decision |
| application/system enforcement | model's own policy implementation and internal computation |
| marker/action success criteria | causal sensitivity of decision to counterfactual forbidden content |
| often secrecy/integrity | procedural, temporal, access, perspective, and epistemic reasons |

This distinction is meaningful only if it survives independent external data.

---

## 9. Generic irrelevant-context / distractor work

There is already substantial literature showing that irrelevant context can alter LLM reasoning, including mechanistic work on competing contextual signals. Therefore “irrelevant information influences the answer” is not a sufficient contribution.

Our experiment must establish all three simultaneously:

1. the information would be useful if allowed;
2. the model correctly knows that it is disallowed for the specified decision;
3. changing that disallowed information still changes the decision.

That third counterfactual is the causal quantity the redesigned dataset should prioritize.

---

## 10. What we can safely claim today

From the controlled suite, we can say:

- the original human-like post-exclusion hypothesis did not reproduce; it reversed;
- several open models exhibit a **prospective nullification gap** under tightly controlled future-target rules;
- declarative policy answers can be correct while the model's decision still depends on the information;
- the controlled effect is sensitive to semantic availability/addressability and can be manipulated causally in mid/upper model layers;
- structured/local routing can remove the controlled failure.

We **cannot yet** say:

- that this is a general failure of LLMs on naturally occurring disallowed-information decisions;
- that the same mechanism explains outcome bias, legal inadmissibility, privileged knowledge, and false-information retraction;
- that the identified patching state is a universal “exclusion representation”;
- that a prompt-level structured ledger is a security guarantee.

---

## 11. Proposed novelty sentence, conditional on EVS-v1 succeeding

A defensible target is:

> **We study whether LLM decisions are causally invariant to information that remains known but is explicitly out of bounds for that decision. Across independently authored true-but-disallowed paradigms, we separate policy knowledge and memory from causal use, measure counterfactual forbidden-information sensitivity, and trace when a model's internal decision computation violates that policy.**

That is narrower than “forgetting,” narrower than generic “irrelevant context,” and different in object from security-oriented leakage/action noninterference.

---

## 12. Locked novelty sentence (supersedes §11 for the temporal paper)

§11 was written while the project still targeted several boundary families.
The pilot narrowed it to temporal, and §7b now constrains what may be claimed.
The sentence the paper actually defends is:

> **Language models identify with near-ceiling accuracy that a piece of
> evidence postdates the historical moment they are asked to reason from, and
> are nevertheless causally moved by it: supplying that same evidence shifts
> their reconstructed ex-ante judgment by a large, replicable margin across
> hundreds of independently sampled natural forecasting questions.**

What this claims, and what it does not:

- **claimed:** a quantified recognition–enforcement gap under a within-item
  causal manipulation (packet present/absent × admissible/inadmissible), with
  per-item recognition measured rather than assumed;
- **claimed:** that the gap is position-sensitive, and — pending Experiment B —
  that it does not reduce to copying an explicitly revealed verdict;
- **not claimed:** priority over the observation that models can state a
  temporal rule and still violate it (see §7b);
- **not claimed:** any statement about internal representations being
  overwritten; no such evidence is collected;
- **not claimed:** generality beyond the temporal family. FANToM failed
  qualification, the FOMC external attempt failed its preregistered gate, and
  both are reported as such.
