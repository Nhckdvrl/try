# Mainline Audit 2026-09-06 V8 — publicness/common-knowledge search after another novelty kill round

**Status:** current research-question / experiment-priority authority.  
**Supersedes:** V7 for prioritization. V1–V7 remain historical provenance.  
**Target:** NAACL / ACL / EMNLP Main-level paper.

> **There is still no approved paper mainline.**
>
> **No new target-model generation is authorized.**
>
> V8 records a deliberately negative but scientifically useful result: V7's best
> search shape (observation/sampling-process conditioning) is now killed by direct
> 2026 work. A new candidate around **publicness and common-knowledge closure**
> survives the current literature audit, but only as a HIGH-RISK PRE-PILOT search
> shape. It has not earned a model run.

---

# 1. Executive decisions

| object | V8 verdict | reason |
|---|---|---|
| New paper mainline | **NONE** | no candidate has passed all novelty/scale/data gates |
| Publicness → common-knowledge closure | **HIGH-RISK PRE-PILOT SEARCH — current #1** | clean scientific distinction; current search has not found an LLM paper directly testing publicness as a shortcut to arbitrary-depth recursive knowledge; dangerous neighbors remain |
| Observation / sampling-process conditioning | **KILL AS PAPER IDENTITY** | CROWN-QA directly studies completeness-sensitive negative reasoning; Xiong (2026) directly studies LLM sampling assumptions / strong-sampling bias; generic Bayesian-update angle already crowded |
| Free-choice / permission strengthening | **SECONDARY SEARCH ONLY** | exact LLM study not located, but deontic/modal reasoning is crowded and free choice itself is a classic phenomenon; accuracy-only paper would be too narrow |
| Explicit-outcome paradox | **HIGH-RISK ARCHIVE ANOMALY / NO PILOT** | still counterintuitive, but hindsight-format literature plus ACL-2026 Outstanding “Lying with Truths” makes the explicit-vs-distributed evidence neighborhood substantially more crowded |
| BTF3 G12→G15 | **MECHANISTIC ASSET / SUPPORTING ONLY** | strong Gemma mechanism, panel behavioral heterogeneity, neighboring decision-subspace / interference work |
| G0 | **STRONG EMPIRICAL ASSET / PAPER IDENTITY HIGH-RISK** | robust, but prospective instruction / forgetting / order / context-control literature remains crowded |
| zero/nonzero | **KILL AS PAPER IDENTITY** | V7 decision unchanged |
| G18 | **SUPPORTING ONLY** | V7 decision unchanged |
| G22 | **KILL / DO NOT RUN** | V7 decision unchanged |

The key project-state sentence remains:

> **A candidate is not a mainline because no exact paper was found. It becomes a
> mainline only after its abstraction, novelty, scale, and data all survive.**

---

# 2. V7's sampling-process lead is now killed

V7's best search shape was:

> Does a model condition the evidential value of an observation on how it was
> generated, selected, censored, or could have been observed?

That was a legitimate search question. It is no longer a good paper identity.

## 2.1 Direct threat 1: completeness-sensitive absence reasoning

Min et al. (2026), **When Absence Is Evidence: Evaluating Completeness-Sensitive
Negative Reasoning in Large Language Models**, explicitly asks when non-observation
licenses a negative conclusion.

Its controlled core fixes:
- the question;
- the observed facts;

and varies whether the available evidence **covers the query scope**.

The paper distinguishes justified negative conclusions from Unknown and reports a
systematic failure to reason about incomplete/partial coverage.

This directly occupies a major version of the proposed:

> high-detectability non-observation vs low-detectability non-observation

story.

The exact probabilistic parameterization is different. That is not enough to rescue
conceptual novelty.

## 2.2 Direct threat 2: sampling assumption itself is already an LLM research variable

Xiong (2026), **Hypothesis generation and updating in large language models**,
studies hypothesis updating in the Number Game and explicitly characterizes a
systematic **strong-sampling assumption** in LLM behavior.

This is particularly damaging because the proposed candidate was not merely "absence
reasoning"; its intended upper-level object was whether a model conditions inference
on the evidence-generating / sampling process.

That abstraction is already being studied.

## 2.3 Upper-level crowding

Even without those two direct papers, the candidate must compete with:
- BayesBench-style belief-trajectory work;
- Bayesian teaching;
- QUITE;
- diagnostic-test posterior updating;
- information discernment / reliability weighting;
- nonlinear evidence integration.

A weak result would be immediately compressible to:

> another Bayesian updating failure under a different likelihood construction.

## Verdict

> **KILL AS PAPER IDENTITY.**

Do not rescue it by changing:
- foxes to medical tests;
- detectability to sampling;
- sampling to censoring;
- binary observations to examples.

The scientific abstraction is now too occupied.

---

# 3. Additional candidates killed before generation

This section extends V7's kill ledger.

## 3.1 Undercutting vs rebutting evidence — KILL broad RQ

Candidate shape:

> Does the model distinguish evidence that P is false from evidence that the source
> for P is unreliable?

This is clean, but the upper-level object is already heavily occupied.

**Information Discernment in Large Language Models** evaluates 13 models on roughly
670K trials and directly separates:
- source discernment: update more for reliable sources;
- truth discernment: update more when the new claim moves toward truth.

It finds source reliability is poorly used and popularity can dominate reliability.

Therefore:
> "models fail to use source reliability correctly"

is dead as a headline.

The finer undercutter/rebutter distinction is not enough by itself to justify a paper.

**Verdict: KILL broad RQ.**

---

## 3.2 Conflict vs ignorance — KILL broad RQ

Candidate shape:

> The same 50/50 confidence can come from no evidence or from strong balanced
> conflicting evidence. Do models distinguish the epistemic states?

This is conceptually clean but already occupied by:
- conflict-aware uncertainty work;
- evidential uncertainty decompositions that explicitly separate conflict and
  ignorance;
- evidence-sufficiency / conflicting-evidence benchmarks;
- credal / imprecise uncertainty work.

**Verdict: KILL broad RQ.**

---

## 3.3 Value of information / ask-before-act — KILL broad RQ

Candidate shape:

> Does the model know when information is worth acquiring before committing to an
> action?

This is already a 2025–2026 research object:
- Value-of-Information frameworks for human-agent communication;
- partial-observability information-seeking benchmarks;
- epistemic competence / active information acquisition;
- work showing thinking can improve evidence use without improving information
  seeking.

**Verdict: KILL broad RQ.**

---

## 3.4 Disjunctive / set-valued uncertainty — KILL broad RQ

Candidate shape:

> Can a model preserve "P or Q" as an unresolved set of possible worlds rather than
> prematurely collapsing onto one concrete world?

Direct threats include:
- ACL 2025 **Large Language and Reasoning Models are Shallow Disjunctive Reasoners**;
- underspecification / abstention benchmarks;
- imprecise-probability / set-valued uncertainty work.

**Verdict: KILL broad RQ.**

---

## 3.5 Joint intention / joint commitment — KILL broad RQ

Candidate shape:

> Alice intends to move the table and Bob intends to move the table does not imply
> that they have formed a joint intention to move it together.

This is natural and important, but current competition is too direct.

Decision-Oriented Dialogue already reports failures where a language model verbally
commits to one joint course of action and then proposes a different one.

More importantly, a public Fall-2026 research project explicitly titled
**Joint Commitment Eval** is already developing process-level LLM cooperation
evaluation from cognitive-science theories of joint commitment.

**Verdict: KILL broad RQ.**

---

## 3.6 Pluralistic ignorance — KILL exact RQ

Candidate shape:

> A group can privately reject a norm while publicly appearing to endorse it.

This was killed immediately by August-2026 work:

**Everyone Conforms, No One Believes: Pluralistic Ignorance in LLM Agent
Populations** evaluates 8 models over 100 scenarios and explicitly studies private
opposition, public conformity, second-order beliefs, and norm-entrepreneur cascades.

NAACL 2025 had already separately studied LLM false-consensus effects.

This is the cleanest possible novelty kill.

**Verdict: KILL. No exact-condition argument is allowed.**

---

## 3.7 Informational cascades / herding — KILL broad RQ

Candidate shape:

> An agent has a private signal but observes predecessors' public actions; does it
> rationally infer from those actions or simply herd?

Direct LLM work already exists:
- 2025 Federal Reserve experiments replicate classic herd behavior with LLM agents
  and private information;
- 2026 LLM-agent market work explicitly records private signals and classifies
  actions that contradict the signal while following market/leader information as
  herding;
- 2026 information-asymmetry multi-agent forecasting work discusses deliberation
  collapsing into herding under shared evidence.

**Verdict: KILL broad RQ.**

---

## 3.8 Collective/distributive plurality — KILL

DistNLI and later plural-interpretation / plural-reference work already occupy the
basic language phenomenon.

**Verdict: KILL.**

---

# 4. Current #1 search shape: publicness and common-knowledge closure

## Status

> **HIGH-RISK PRE-PILOT SEARCH ONLY.**
>
> **No target-model generation.**

This candidate has survived more novelty pressure than the other new candidates in
this round. That is not the same as approval.

The important distinction is not:

> private information vs public information.

OmniToM already studies that.

It is not:

> first-order vs second-order Theory of Mind.

Many benchmarks already study that.

It is not:

> can LLMs coordinate.

LLM-Coordination and other multi-agent work already study that.

The potentially new research object is the **transition from finite recursive
knowledge to common knowledge under public observability**.

---

# 5. Why common knowledge is not "just higher-order ToM"

For two agents A and B:

```
A knows P
B knows P
```

does not imply:

```
A knows that B knows P
B knows that A knows P
```

and even mutual second-order knowledge does not by itself imply arbitrary recursive
closure.

Common knowledge of P requires:

```
everyone knows P
everyone knows everyone knows P
everyone knows everyone knows everyone knows P
...
```

The formal distinction is old and foundational.

The interesting empirical/cognitive point is that finite agents do not literally
enumerate an infinite tower. Human work argues that **public observability can act as
a shortcut that licenses common-knowledge inference**, while explicit recursive
mentalizing remains depth-limited.

The August-2026 PNAS paper **Recursive mentalizing and public salience in the
perception of common knowledge** makes this especially relevant now:
- humans track a few levels of recursive knowledge;
- publicly witnessed events license much deeper common-knowledge judgments;
- the paper distinguishes capacity-limited recursion from a public-salience
  heuristic.

This creates a clean computational question for language models.

---

# 6. Candidate CK — six-field audit

## 6.1 Research Question

> **Do language models derive common knowledge from public observability through a
> distinct publicness mechanism, or only through finite nested-belief reasoning?**

A more behavioral wording:

> **Does making the same fact public create an arbitrary-depth epistemic closure that
> cannot be explained by simply adding one more layer of Theory of Mind?**

This is the current candidate wording. It is intentionally narrower than "LLMs
understand common knowledge."

---

## 6.2 One-example

Private version:

> Alice receives a private message: “The meeting is at 3.”  
> Bob separately receives the same private message: “The meeting is at 3.”

Public version:

> Alice and Bob are together when a loudspeaker announces: “The meeting is at 3.”

In both versions Alice knows the meeting time and Bob knows the meeting time.

But only the public event straightforwardly supports:

> Alice knows that Bob knows that Alice knows that Bob knows … that the meeting is
> at 3.

This fits in Figure 1 without invented metadata.

---

## 6.3 Minimal Dataset

Do not build an ontology.

A possible discovery core should use no more than four information structures,
adapted from established human designs:

1. **Private / duplicated:** A and B separately receive P.
2. **Reciprocal:** A receives P and is told B received P; B analogously knows A
   received P.
3. **Doubly reciprocal:** one more explicitly encoded finite recursion layer.
4. **Public:** A and B jointly witness the same announcement/event.

The factual proposition P remains identical.

Queries should be generated at recursive depths 1–5:

```
Does Alice know P?
Does Alice know that Bob knows P?
Does Alice know that Bob knows that Alice knows P?
...
```

The critical comparison is not raw accuracy.

It is the **shape of degradation with depth under finite-recursion conditions versus
public conditions**.

A second, optional behavioral bridge should be a minimal coordination decision whose
optimal action changes only when P is common knowledge, not merely individually known.
This bridge must remain simple; if it requires a complicated game-theory tutorial, do
not use it.

---

## 6.4 Gold

The gold is deterministic from dynamic epistemic logic / Kripke accessibility.

No LLM judge.

No subjective annotation.

For the core:
- private duplicated messages create first-order knowledge but not automatic mutual
  recursive knowledge;
- finite reciprocal conditions license only the explicitly supported depths;
- a truthful public announcement jointly witnessed under the stated visibility
  assumptions creates common knowledge.

Every generated item can be checked symbolically.

This is a strong data property.

---

## 6.5 Novelty Threat Map

### Threat 1 — CogToM, ACL 2026

CogToM is an unusually broad ToM benchmark:
- >8K bilingual items;
- 46 paradigms;
- false belief, 2nd-order false belief, See-Know, reader knowledge, etc.

A direct audit of its public dataset found no common-knowledge / public-announcement
paradigm.

**Threat level:** serious general ToM neighbor, not exact kill.

### Threat 2 — OmniToM, 2026

OmniToM is more dangerous.

It labels belief propositions along:
- recursive order 0–3;
- truth status;
- **knowledge access: Private / Shared / Public**;
- representation;
- content;
- source;
- context.

It reports especially weak performance on knowledge-access classification.

Therefore these claims are dead:

> "LLMs cannot tell public from private information."

> "LLMs struggle to track who has access to a belief."

The candidate survives only by testing what OmniToM does not center:
**whether publicness changes the computation of arbitrary-depth recursive closure.**

### Threat 3 — higher-order ToM benchmarks

HI-ToM, TimeToM, CogToM, OmniToM and strategic-reasoning work all study nested
beliefs.

Therefore:
> "models fail at third-order belief"

is not novel.

The scientific contrast must be:
> finite recursive mentalizing vs publicness-induced common-knowledge closure.

### Threat 4 — LLM-Coordination, NAACL 2025 Findings

This benchmark studies pure coordination, ToM and joint planning.

It does not appear to manipulate private vs reciprocal vs public information to isolate
common knowledge.

Therefore:
> "LLMs fail coordination"

is dead, but the information-structure mechanism remains potentially open.

### Threat 5 — common-ground NLP

NAACL 2024 Grounding Gaps, ACL 2025 grounding work, the 2025 common-ground survey,
and a 2026 human-AI common-ground benchmark study:
- grounding acts;
- repair;
- shared views;
- referential conventions;
- situation awareness;
- collaborative puzzle solving.

This kills any attempt to market the paper as simply:
> "common ground in LLMs."

Common ground and common knowledge are related but not interchangeable.

### Threat 6 — public-announcement logic for LLM agents

A 2026 Journal of Logic and Computation paper proposes an **external epistemic state
management framework** inspired by public-announcement and graded modal logic.

That is a method/framework paper for maintaining explicit epistemic state. It is not
evidence that an unmodified LLM internally derives common-knowledge closure.

Still, it raises the bar for any method claim: "use PAL to track knowledge" is already
available.

### Threat 7 — human common-knowledge literature

The distinction and publicness heuristic are not new scientific ideas. Human work,
including PNAS 2019 and PNAS 2026, already studies them.

Therefore a paper whose contribution is:

> "LLMs also show a publicness effect"

would be too weak for our target.

The novelty must be an LLM-specific empirical law or mechanistic dissociation.

---

# 7. What result could actually carry novelty?

The pilot must not be designed to force one of these results. They are examples of
paper-worthy *shapes*.

## Shape A — Publicness closure dissociation

Models may fail explicit higher-order belief recursion rapidly with depth, yet remain
stable at deep orders after a public event.

Then the claim is not:
> models are good at common knowledge.

It is:

> **common-knowledge behavior dissociates from explicit recursive ToM: public
> observability induces a qualitatively different computation from finite belief
> nesting.**

That is potentially memorable.

## Shape B — Publicness illusion

The opposite could be more interesting:

> models treat jointly observed events as common knowledge even when one participant's
> observability is explicitly broken or ambiguous.

This would define a **publicness illusion**:
surface public cues trigger recursive closure even when the epistemic preconditions fail.

This could be analogous in shape to a strong systematic bias rather than a benchmark
accuracy result.

However, do not contaminate discovery by overbuilding hidden-observer cases before a
simple first pilot establishes anything.

## Shape C — Reasoning/publicness tradeoff

A reasoning-tuned model might perform better on explicit finite nesting but worse at
using natural public cues, or vice versa.

This would need to survive comparison to:
- ACL 2026 Outstanding Mind the (DH) Gap;
- ICML 2025 Mind Your Step;
- PaCE / pragmatic-context work.

Generic "reasoning changes human-like behavior" is already occupied. Only a
common-knowledge-specific law would count.

## Shape D — behavioral/representational dissociation

A model might:
- correctly classify an event as public;
- correctly answer low-order nested-belief probes;
- yet fail the deep closure / coordination consequence.

That would separate:
```
publicness recognition
≠ finite ToM
≠ common-knowledge use
```

This is more promising than simply reporting accuracy.

---

# 8. Growth path if the behavioral law is real

Only after a fresh small discovery establishes a stable non-obvious law:

```
C1 — phenomenon
A sharp publicness-specific law in recursive knowledge / coordination,
not a generic ToM depth effect.

↓

C2 — dissociation / computational characterization
Separate publicness recognition, finite nested-belief computation,
common-knowledge closure, and coordination consequence.
Test across simple semantic domains and modern model families.

↓

C3 — mechanism / causal intervention
On 1–2 open models:
locate whether public events recruit a publicness/common-knowledge state
distinct from ordinary nested-belief states;
test causal interchange / patching;
ask whether adding/removing that state selectively creates/removes deep closure
without changing first-order factual knowledge.
```

The existing project's causal-analysis expertise is reusable here.

The old prospective-exclusion paper story is not.

---

# 9. Kill criteria for common-knowledge candidate

Kill or strongly demote **before pilot** if continued literature search finds:

1. a modern LLM study already orthogonally manipulating public vs finitely mutual
   information and measuring recursive closure;
2. a benchmark where "Public" explicitly entails and tests arbitrary-depth common
   knowledge rather than merely access labels;
3. a multi-agent coordination study whose central result already links public
   observability to common-knowledge-specific coordination.

Kill **after a future pilot** if:

4. performance is just a monotonic generic ToM-depth curve with no publicness-specific
   structure;
5. public vs private differences disappear after controlling simple lexical cues;
6. only one model family shows the effect;
7. strong models are at ceiling everywhere and there is no meaningful phenomenon;
8. the only claim becomes "public information is easier";
9. a coordination extension requires a complicated artificial game;
10. a mechanism story is required to make a weak behavioral effect look important.

---

# 10. Free-choice permission — secondary search only

A second independent search shape remains:

> "You may take an apple or a pear" normally licenses each option individually,
> despite the corresponding classical modal inference not being generally valid.

The exact free-choice phenomenon has not been located in current LLM searches.

However, this is **not enough**.

Current deontic/modal neighbors include:
- normative reasoning benchmarks;
- EACL 2026 deontic Wason reasoning;
- ModalBench 2026;
- DeonticBench 2026.

The human semantic phenomenon itself is decades old.

Therefore the following paper is too small:

> "We benchmark free-choice inference in LLMs."

A surviving contribution would require a larger LLM-specific law, e.g. a stable
dissociation between formal modal competence and natural-language permission
strengthening that predicts behavior across constructions.

Generic "reasoning models are less human-like / more formal" is also crowded by
Mind the (DH) Gap, Mind Your Step, PaCE and related work.

**Verdict:** SECONDARY SEARCH ONLY. No pilot.

---

# 11. Explicit-outcome paradox after ACL-2026 award comparison

The old anomaly remains empirically interesting:

> removing an explicit verdict increases contamination from a later packet.

But ACL-2026 Outstanding **Lying with Truths** establishes a broad and striking
neighbor:
- truthful evidence fragments can be strategically composed to drive false beliefs;
- the effect is broad across model families;
- stronger reasoning can increase susceptibility.

This does not directly test:
> explicit conclusion vs equally diagnostic distributed evidence under an exclusion
> instruction.

So it is not an exact kill.

But it makes a generic:
> "distributed evidence is harder to resist than a label"

story substantially less novel.

Together with old hindsight research showing outcome-information format matters, the
bar is now very high.

**Verdict:** retain as HIGH-RISK ARCHIVE ANOMALY. Do not spend a clean pilot on it
unless a future conceptual argument separates it sharply from montage/contextual
evidence manipulation.

---

# 12. Current ranking

| rank | object | verdict |
|---:|---|---|
| 0 | approved mainline | **NONE** |
| 1 | publicness → common-knowledge closure | **HIGH-RISK PRE-PILOT SEARCH / NO GENERATION** |
| 2 | free-choice / semantic–reasoning interface | **SECONDARY SEARCH ONLY** |
| asset | G12→G15 recipient-conditioned decision state | **MECHANISTIC ASSET** |
| asset | G0 prospective exclusion | **STRONG EMPIRICAL ASSET / unsafe identity** |
| anomaly | explicit-outcome paradox | **HIGH-RISK ARCHIVE ANOMALY** |
| killed | observation/sampling-process conditioning | **KILL paper identity** |
| killed | pluralistic ignorance | **KILL exact RQ** |
| killed | informational cascades/herding | **KILL broad RQ** |
| killed | joint intention/commitment | **KILL broad RQ** |
| killed | conflict vs ignorance | **KILL broad RQ** |
| killed | undercutting/source reliability | **KILL broad RQ** |
| killed | value of information | **KILL broad RQ** |
| killed | disjunctive/set-valued uncertainty | **KILL broad RQ** |
| killed | zero/nonzero | **KILL paper identity** |
| killed | G22 | **KILL / DO NOT RUN** |

---

# 13. Experiment authorization

Still **no new target-model generation**.

Authorized:
- continue common-knowledge novelty assassination;
- inspect public datasets / published outputs from CogToM, OmniToM, ToM and
  coordination work without new target generations;
- search for another independent RQ;
- design symbolic gold / dummy generators without looking at target-model outcomes;
- maintain the kill ledger;
- audit old assets when they motivate a genuinely new RQ.

Not authorized:
- common-knowledge pilot;
- free-choice pilot;
- sampling-process pilot;
- explicit-outcome pilot;
- zero replication;
- G22;
- G0 rescue controls;
- new G12/G15 mechanism work.

---

# 14. Current decision rule

The project has now killed multiple candidates that passed the one-example test.

That is expected.

A one-example test only establishes **naturalness**. It does not establish novelty.

The current standard is:

```
natural one-example
AND conceptual gap
AND non-obvious possible law
AND direct gold
AND C1→C2→C3 growth path
AND no stronger existing paper compression
```

The current common-knowledge candidate has passed the first, fourth, and plausibly the
fifth. It has **not yet fully passed the second, third, or sixth**.

Therefore:

> **keep searching, do not run.**


---

# 15. Same-day amendment — exact common-knowledge threats found after V8 freeze

**Status correction:** the publicness/common-knowledge candidate remains alive only as
a **HIGH-RISK INTERSECTION LEAD**. The original V8 wording "current #1" should not be
read as pilot approval or as evidence that public-announcement reasoning is unstudied.

Three additional direct neighbors were identified after the first V8 write.

## 15.1 MindGames (EMNLP Findings 2023) already uses public-announcement logic

Sileo & Lernould, **MindGames: Targeting Theory of Mind in Large Language Models
with Dynamic Epistemic Modal Logic**, generates controlled epistemic-reasoning
problems with SMCDEL / S5 announcement logic.

Its generated premises explicitly include forms such as:

> "It is publicly announced that ..."

and its hypotheses vary higher-order belief depth.

Therefore all of these candidate headlines are dead:

- "first LLM benchmark of public announcements";
- "first controlled LLM benchmark of recursive epistemic reasoning";
- "public announcements can be used to test higher-order ToM in LLMs."

The surviving gap, if any, must be about a **publicness-specific computational
dissociation**, not the underlying logic formalism.

## 15.2 Li, Luo & Liao (Knowledge-Based Systems 2026) directly benchmarks DEL puzzles

**Logical reasoning in evolving scenarios: Evaluating LLMs with dynamic epistemic
logic puzzles** constructs 2,784 instances from Muddy Children and Cheryl's Birthday.
The Muddy Children setup centrally relies on public announcements and recursive
knowledge updates. The paper varies agents / rounds and reports a 20–30% drop as
complexity rises, attributing failures to recursive perspective-taking and precise
logical implication.

This kills:

> "Can LLMs solve common-knowledge / Muddy-Children reasoning?"

It also makes a benchmark-only extension with more modern models scientifically weak.

What the paper does **not** appear to orthogonalize is the human-cognition question
raised by De Freitas, Huang & Pinker (PNAS 2026):

> holding the first-order fact constant, does **public observability itself** produce a
> qualitatively different route to deep recursive knowledge than finite
> private/reciprocal nesting?

That intersection is the only reason the candidate remains open.

## 15.3 SimpleToM (ICLR 2026) kills generic recognition→application novelty

SimpleToM establishes a strong explicit-ToM vs applied-ToM gap: models can infer a
character's mental state yet fail to use that state to predict or judge behavior.

Therefore a future common-knowledge paper cannot claim novelty from:

> "the model recognizes that information is public but fails to use it for
> coordination."

That would be another instance of the already-established explicit-vs-applied ToM gap.

A surviving contribution must establish a **publicness-specific law** that is not
predicted by generic ToM application failure.

## 15.4 Revised candidate wording

The only research question still worth assassinating is:

> **When first-order knowledge is matched, does public observability induce a
> qualitatively distinct shortcut to recursive epistemic closure in LLMs, separable
> from ordinary finite-depth Theory-of-Mind reasoning?**

This is substantially narrower and higher risk than:

> "Do LLMs understand common knowledge?"

## 15.5 Revised pre-pilot verdict

> **HIGH-RISK INTERSECTION LEAD / NO GENERATION.**

Before authorizing even a 50–100 item discovery run, require one more exact search for:
- public vs private/reciprocal announcement manipulations in neural/LLM ToM;
- public-salience heuristics in machine cognition;
- common-knowledge-specific coordination in LLM agents;
- mechanistic representations of common knowledge/publicness.

If any modern work already contrasts **finite mutual knowledge vs public common
knowledge** as the load-bearing variable, kill the candidate.

## 15.6 Additional killed / unpromoted search shapes

### Screening-off / conditional relevance
**KILL broad RQ.** Recent LLM causal-cognition work already compares 20+ models to
classic human Markov-violation / explaining-away / screening-off paradigms. A new
three-node verbal task would be an instance, not a paper.

### Reversible vs irreversible action / preserving optionality
**KILL broad RQ.** AgentAbstain, streaming-agent reversibility work, commit-point
safety frameworks, and current proactive-agent decision frameworks already center
irreversible actions, abstention, waiting and future option value.

### Homogeneity / truth-value gaps
**UNASSESSED SUBSTRATE, NOT A CANDIDATE.** Exact LLM homogeneity work was not located
in the current search, but:
- homogeneity is a classic linguistic phenomenon;
- generic pragmatics and presupposition evaluation is crowded;
- CoNLL 2026 Outstanding work already finds a reasoning-vs-human-semantic/pragmatic
  mismatch on presupposition in conditionals.

Do not run a homogeneity benchmark merely because the exact phenomenon appears
unoccupied. It must first motivate a larger LLM-specific law that is not generic
"reasoning models are less human-like."
