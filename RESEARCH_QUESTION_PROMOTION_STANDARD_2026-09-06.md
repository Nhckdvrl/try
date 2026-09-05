# Research-Question Promotion Standard — 2026-09-06

**Purpose:** long-term selection authority for new mainline research questions.  
**Target:** NAACL / ACL / EMNLP Main-level work, with Outstanding/Best-Paper-level problem selection as the aspirational bar.  
**Relation to mainline audits:** mainline audits decide the current project state; this document defines **what a research question must look like before it deserves to be promoted**. It is intended to remain useful even when individual candidates are killed.

---

# 0. Core correction

The project previously over-weighted an attractive experimental pattern:

> find an anomaly → ask whether it replicates → build a paper around the anomaly.

That is a dangerous search strategy because the scientific value of the project becomes
conditional on a narrow empirical direction being present.

The preferred strategy is:

> **find a durable scientific object first → ask broad but precise questions about its
> representation / computation / causal role → use simple experiments to discover the
> actual law.**

This is the key distinction between an **outcome-dependent phenomenon hunt** and an
**outcome-robust research program**.

A candidate should ideally remain interesting under several plausible outcomes.

For example, the following is weak as a research program:

> Do models show a sharp 0%-vs-1% discontinuity in evidence weighting?

If the discontinuity disappears, the problem largely disappears with it.

By contrast:

> Do language models represent whether an entity is real or fictional separately from
> whether they know facts about it?

remains scientifically meaningful if:
- the representations are shared;
- they are separate;
- they are entangled;
- they differ between base and instruction-tuned models;
- they are causally used;
- or they are behaviorally bypassed.

Likewise:

> What internal computation distinguishes arbitrary/random choice from deterministic
> choice?

is not dependent on first observing a specific switch/dial mechanism. The discovered
mechanism can take several forms and still answer an interesting question.

**Project rule: prefer questions for which multiple plausible answers would teach us
something important.**

---

# 1. What the Hamdi research pattern actually teaches us

A direct reading of Slack **#r_hamdi** suggests a stronger lesson than merely
"simple synthetic data is okay."

## 1.1 The research object comes before the effect

The real-vs-fictional project was framed around a scientific distinction:

> Does the model represent an entity's ontological status separately from epistemic
> access / knowledge?

The question is meaningful before measuring:
- a probe AUC;
- a specific SAE latent;
- a steering effect;
- a familiarity interaction.

The random-choice project follows the same pattern:

> Does the model internally represent that it is being asked to make an arbitrary
> choice, what is the structure of that state, and how is it causally used?

The later switch-vs-dial decomposition is a **finding**, not the definition of the
research question.

This is the pattern to copy.

---

## 1.2 A good question supports a method lattice, not one experiment

For real/fictional:

- behavioral judgment;
- linear representation;
- SAE latents;
- cross-domain transfer;
- familiarity/knowledge dissociation;
- base vs instruction-tuned comparison;
- causal steering;
- weight/activation intervention;
- contextual nonce entities;
- representation-vs-behavior dissociation.

For random choice:

- behavioral output distribution;
- domain-general state probe;
- held-out-domain transfer;
- SAE;
- reader/writer decomposition;
- attribution;
- causal steering;
- gated intervention;
- comparison to LoRA;
- representation-level fine-tuning predicted by the mechanism.

The paper grows because the **object has depth**, not because conditions are added.

A candidate that offers only:

> compare condition A with condition B

is usually too small.

A strong research question should naturally admit at least three different kinds of
investigation from this set:

1. behavior;
2. representation;
3. generalization;
4. dissociation;
5. causal mechanism;
6. intervention;
7. training/tuning consequences;
8. model-family / architecture comparison;
9. interaction with instruction tuning / reasoning;
10. practical downstream consequence.

This does **not** mean all ten belong in one paper. It means the scientific object is
large enough that the researcher can discover which 2–4 are load-bearing.

---

## 1.3 Simple data should isolate the object, not manufacture it

Hamdi's strongest examples are shallow:

- Paris vs Hogwarts;
- elephant vs dragon;
- gold vs kryptonite;
- "Pick a random digit";
- "Flip a coin";
- "Choose any color";
- nonce entities such as daxon / torbin placed in scientific, news, fictional or
  imagination frames.

The dataset is not the scientific achievement.

The dataset simply makes the scientific variable legible.

The complexity then moves into:
- representation;
- transfer;
- dissociation;
- mechanism;
- intervention.

Project standard:

> **The research question may be deep; the discovery substrate should usually be
> embarrassingly simple.**

---

## 1.4 Controls should separate adjacent concepts, not create a new ontology

The real/fictional work asks whether ontology is distinct from:
- familiarity;
- known/unknown;
- proposition truth;
- genre/context.

These are obvious alternative axes that could destroy the interpretation.

That is a good use of controls.

The project should not instead invent:
- five latent states;
- interface metadata;
- artificial evidence carriers;
- process-specific ontologies;
- many reviewer-imagined corner conditions.

Rule:

> **A control is justified when collapsing two concepts would destroy the scientific
> object.**

Do not add a control merely because it can be imagined.

---

## 1.5 Unexpected outcomes should deepen the question, not destroy the project

In #r_hamdi, unfamiliar names in factual contexts did **not** acquire the expected
"real" internal tag. That did not invalidate the broader ontology question. Instead it
revealed:
- contextual rigidity;
- skeptical behavioral responses;
- internal/behavioral dissociation;
- differences between testimony and latent status.

This is what outcome-robustness looks like.

A healthy candidate should permit:
- expected positive result;
- null representational result;
- surprising dissociation;
- architecture difference;
- opposite-direction human/model gap;

without immediately becoming scientifically meaningless.

---

# 2. Three levels of candidate status

The project must distinguish **interesting idea**, **pilot-worthy question**, and
**paper-worthy mainline**.

---

## 2.1 SEARCH LEAD

A SEARCH LEAD is only a question worth investigating conceptually.

Requirements:
- one-sentence RQ;
- one-example test;
- simple possible substrate;
- no obvious exact kill after initial search.

A search lead gets:
- literature work;
- conceptual decomposition;
- maybe public-data inspection.

It does **not** automatically get GPU generation.

Most ideas should die here.

---

## 2.2 SMALL PILOT

A SMALL PILOT is a question that deserves a cheap attempt at discovery.

It must pass all **Pilot Gates** below.

Pilot purpose:

> **discover whether there is a stable, non-obvious law**, not confirm a favored
> phenomenon.

The pilot should usually be:
- 2–4 model families;
- 20–100 independent semantic skeletons;
- minimal conditions;
- deterministic/direct gold;
- no mechanism work yet;
- pre-written kill rules.

Pilot success only earns another audit.

It does not establish a paper.

---

## 2.3 MAINLINE CANDIDATE

A candidate may become a mainline only after a phenomenon has been observed **and then
survives a fresh post-result novelty audit**.

The key question is:

> If we remove the condition names and experimental terminology, is the actual result
> a new, memorable scientific statement?

Examples of potentially adequate shapes:

> Models represent X but systematically fail to use X when Y.

> Stronger reasoning improves explicit inference while weakening an independent
> pragmatic computation.

> Publicly observed information enters a qualitatively different recursive state than
> finitely shared information.

> A model uses separate reader and writer mechanisms for deciding *when* a policy
> applies and *how* the output distribution should change.

Bad shapes:

> Condition A was 8% worse than condition B.

> Depth 6 was harder than depth 2.

> Giving more explicit information helped.

> Longer context hurt.

> Stronger models did better.

---

# 3. The Pilot Gates

A candidate receives a SMALL PILOT only if **all** gates pass.

---

## Gate P1 — One-minute intelligibility

Can a technically literate reader understand:
- what distinction is being studied;
- why it matters;
- and one concrete example

within one minute?

If the explanation requires internal project vocabulary, fail.

Good:

> A model knows many facts about Hogwarts, but Hogwarts is not real. Does it internally
> distinguish knowing about an entity from representing that it exists?

Good:

> When asked to pick an arbitrary digit, a model strongly prefers 7. Does it represent
> that it is in "arbitrary choice" mode separately from the mechanism that shapes the
> output distribution?

Bad:

> We distinguish U/K/I target states using a non-evidential manifest carrier...

---

## Gate P2 — Outcome robustness

Ask:

> **Would at least three qualitatively different plausible outcomes still answer an
> interesting scientific question?**

If only one narrow direction makes the project interesting, fail.

Strong:
- X and Y are represented separately;
- X and Y are entangled;
- representation exists but is behaviorally bypassed;
- representation differs across training regimes.

Weak:
- a special discontinuity must appear exactly at 0;
- one prompt ordering must outperform another;
- one weird interaction must replicate.

This is one of the most important new project gates.

---

## Gate P3 — Research-space width

Before running the model, write at least **three independent scientific follow-up
axes** that would be meaningful if the object exists.

Examples:
- representation;
- causal role;
- cross-domain generalization;
- instruction-tuning effect;
- architecture comparison;
- intervention;
- practical consequence.

These axes must investigate the **same scientific object**, not add unrelated benchmark
conditions.

If the only growth path is:
- more models;
- more prompts;
- more domains;

fail.

---

## Gate P4 — Conceptual novelty

The question must survive **conceptual**, not exact-manipulation, assassination.

Required search:
1. exact phenomenon;
2. parent abstraction;
3. neighboring cognitive/linguistic construct;
4. mechanism literature;
5. benchmark literature;
6. 2025–2026 preprints/conference work;
7. adjacent fields when relevant: cognitive science, logic, HCI, multi-agent systems,
   ML, alignment, philosophy of language, statistics.

Required reviewer test:

> Could a knowledgeable reviewer summarize our result as "X, already known, on a new
> substrate"?

If yes, usually fail.

---

## Gate P5 — Stable object, not terminology novelty

The object must be understandable without our invented term.

A candidate does not become novel because we name it:
- target addressability;
- publicness blindness;
- evidence-state inertia;
- closure failure;
- commitment leakage.

Before promotion, rewrite the claim with ordinary language.

If it becomes an existing phenomenon, kill it.

---

## Gate P6 — Simple discovery substrate

Default budget:
- 2–4 core information structures/conditions;
- 1–5 sentence examples;
- binary/scalar/directly checkable gold;
- 20–100 genuinely independent skeletons for a pilot;
- no LLM judge if avoidable;
- no complicated corpus joins;
- no invented world ontology;
- no more metadata than analysis actually needs.

Fail if the experiment requires a complicated world to instantiate the question.

---

## Gate P7 — Non-triviality

Ask before running:

> If the proposed effect occurs, could a reviewer reasonably say "of course"?

Default-kill findings:
- explicit target cues improve target handling;
- longer context is harder;
- harder task reduces accuracy;
- explicit explanation helps;
- direct mention increases attention;
- more evidence changes the answer more;
- known entities are easier than unknown entities.

A strong candidate need not predict a surprising result, but the **research question**
must allow findings that teach something beyond the manipulation itself.

---

## Gate P8 — Direct gold / measurement integrity

The phenomenon should be measurable without a fragile estimator.

Prefer:
- exact match;
- mathematical gold;
- deterministic symbolic validation;
- observable behavioral distribution;
- paired raw effects.

Avoid building the paper on:
- unstable ratios;
- judge-model preferences;
- hand-labeled latent categories;
- post-hoc selected subsets;
- pseudo-replicated template variants.

The independent unit must be defined before output.

---

## Gate P9 — Importance independent of benchmark

Ask:

> Why would the field care if this distinction exists?

The answer must refer to the model, not the dataset.

Examples:
- tells us what kind of world/agent state the model tracks;
- explains a general failure of reasoning/control;
- distinguishes representation from policy/compliance;
- reveals a reusable internal computation;
- changes how models should be trained or intervened on.

Bad:
- improves accuracy on our benchmark;
- creates a new leaderboard;
- fills a missing dataset category.

---

## Gate P10 — Honest falsifiability

Before output, write:
- what result would kill the question;
- what result would reduce it to prior work;
- what result would be too small/trivial;
- what model heterogeneity would invalidate a universal claim.

A project without a plausible kill outcome is probably being protected rather than
tested.

---

# 4. The Mainline Gates

Passing the pilot gates is not sufficient.

After observing results, a candidate becomes a **MAINLINE CANDIDATE** only if the
following all hold.

---

## Gate M1 — A memorable law exists

The main behavioral result can be stated in one sentence **without numbers**.

The sentence should sound like a scientific result, not an experiment report.

---

## Gate M2 — The law is not the experimental manipulation

Bad:

> When told that both agents publicly heard P, models are more likely to answer that
> both know P.

Good shape:

> Models correctly recognize public access but do not convert it into recursive
> common-knowledge closure.

The second teaches a computational distinction.

---

## Gate M3 — Cross-family reality

For a behavioral headline:
- at least several modern model families;
- practically meaningful magnitude;
- no one-template/domain dependence;
- heterogeneity explicitly characterized.

Do not convert "2/6 models" into a universal law.

---

## Gate M4 — A stronger second claim naturally follows

The paper should not end at C1.

A viable mainline should offer a natural stronger question:

C1 phenomenon  
→ C2 general law / dissociation / boundary  
→ C3 mechanism or predicted intervention.

If C2 requires inventing a new unrelated benchmark, the object is too small.

---

## Gate M5 — Mechanism is explanatory, not decorative

Probing/SAE/patching/steering must answer:

> why does C1 occur?

not merely:

> where can we decode condition labels?

A mechanistic result should make a prediction:
- which condition changes;
- which intervention rescues/fails;
- what transfers;
- what remains invariant.

---

## Gate M6 — The paper survives title stripping

Remove:
- model names;
- dataset names;
- condition names;
- method names.

Ask what remains.

If it is still a meaningful scientific statement, good.

If nothing remains except:
> "we benchmark X"

the mainline is weak.

---

## Gate M7 — Post-result novelty assassination

Novelty must be checked **again after the result**.

The observed law may map to literature that the original RQ did not.

Example:
- before experiment: "common-knowledge compression" seems open;
- after experiment: actual result is simply "private information is over-attributed";
- EAST already reports that;
- therefore kill even though the original RQ was novel.

This gate is mandatory.

---

# 5. Outcome-Robustness Test

For every candidate, write a table like:

| plausible outcome | still scientifically useful? | what is learned? |
|---|---|---|
| clean separation | yes/no | ... |
| no separation | yes/no | ... |
| behavioral/internal dissociation | yes/no | ... |
| model-family heterogeneity | yes/no | ... |
| training-regime difference | yes/no | ... |

A candidate is strong when several rows lead to meaningful but different scientific
stories.

A candidate is weak when four rows say "project dies" and one row says "paper."

This does **not** mean we avoid falsification. A good question can still be killed by
data. It means the scientific question is not defined as one desired effect.

---

# 6. Research-Space Width Test

Before promotion, sketch the **research program**, not the experiment list.

A strong object should support questions like:

## Behavioral layer
- Does the distinction matter to outputs?
- Under what natural contexts?
- Is there a qualitative law?

## Representational layer
- Is the state internally represented?
- Is it linear / low-dimensional / distributed?
- Is it domain-general?

## Structural layer
- Is it distinct from nearby concepts?
- Does it compose with other states?
- Is it a switch, dial, pointer, router, value slot, etc.?

## Causal layer
- Is the representation used?
- What happens under interchange/ablation/steering?
- Can behavior change while the representation remains fixed?

## Training layer
- Does pretraining already contain it?
- Does instruction tuning change its use rather than its existence?
- Do reasoning/RL stages alter the representation or readout?

## Intervention layer
- Does the mechanism predict a smaller/better intervention?
- Can it improve behavior selectively?
- Does it reveal a low-rank or modular policy?

A candidate need not use every layer. But if only the first layer makes sense, it is
probably a benchmark question rather than a durable scientific object.

---

# 7. Anti-patterns

## 7.1 The anomaly trap

> We saw a strange curve; what story can explain it?

Use anomalies as clues, not automatic research questions.

---

## 7.2 The latent-state inflation trap

> To distinguish explanations we need U, K, I, K2, K3...

If the reader must learn our taxonomy before caring, stop.

---

## 7.3 The exact-gap trap

> Nobody has tested these exact four cells.

Exact-cell novelty is not conceptual novelty.

---

## 7.4 The human-bias replication trap

> Humans show bias X; do LLMs also show X?

This is usually too weak unless:
- LLMs show a new law;
- a qualitative divergence appears;
- scaling/training changes the phenomenon unexpectedly;
- mechanism reveals a new computation.

---

## 7.5 The benchmark-width trap

> The research space is broad because we have ten domains and ten models.

That is breadth of evaluation, not breadth of scientific object.

---

## 7.6 The mechanism-decoration trap

> Probe AUC is high, so now we have a mechanism paper.

Decodability alone is not mechanism.

---

## 7.7 The endless-search trap

High standards should not become paralysis.

Once a question:
- survives direct and conceptual novelty search;
- is outcome-robust;
- has broad research space;
- has simple data;
- has direct gold;
- has explicit kill criteria;

a **small discovery pilot is appropriate**.

The pilot is how we learn the empirical law.

---

# 8. Required candidate card

Every future candidate must contain:

## 1. Research Question
One sentence.

## 2. Why it matters
One or two sentences, independent of a benchmark.

## 3. One-example
At most 1–3 short sentences.

## 4. Scientific object
What persistent model property/computation/state is being studied?

## 5. Nearby distinctions
What concepts could it be confused with?

## 6. Outcome-Robustness Table
At least four plausible outcomes.

## 7. Research-Space Map
At least three meaningful axes beyond the first behavior experiment.

## 8. Minimal Dataset
2–4 primary structures if possible.

## 9. Gold
Why the answer is direct and robust.

## 10. Novelty Threat Map
Closest 3–10 works and the reviewer kill sentence.

## 11. Non-triviality Test
Why a positive result would not be obvious from the manipulation.

## 12. Pilot Kill Criteria
What outcomes stop the project.

## 13. Growth Path
C1 → C2 → C3.

## 14. Verdict
One of:
- KILL
- SEARCH LEAD
- HIGH-RISK
- SMALL PILOT
- MAINLINE CANDIDATE
- SUPPORTING ONLY

No "promising" without a verdict.

---

# 9. How CK should be interpreted under this standard

CK currently passes the **pilot** standard because the research object is not defined
as one desired anomaly:

> how public observability changes recursive epistemic computation relative to finite
> nested belief.

Possible outcomes include:
- publicness-specific compression;
- closure failure despite publicness recognition;
- finite-to-common overclosure;
- architecture/training-specific divergence;
- near-perfect performance.

Several outcomes would still teach something, but not all would support a paper.

Therefore CK-P1 is legitimate discovery.

However, CK is **not yet a mainline**.

If its actual result reduces to:
- generic nesting difficulty;
- private/mutual confusion;
- generic recognition→application failure;
- simple wording ease;

it must be killed under M7 even though the original question passed the pilot gates.

---

# 10. The target profile for future searches

The project should preferentially search for questions with this shape:

> **There is a basic computational/semantic/epistemic variable that language models
> plausibly must track to function, but the field has not yet characterized whether it
> is internally represented, how it is structured, whether it is causally used, and
> how training changes its use.**

Ideal properties:
- intuitive to ordinary readers;
- persistent across tasks;
- simple natural examples;
- distinct from obvious neighboring axes;
- several plausible empirical outcomes;
- representation/mechanism/intervention depth;
- no dependence on a custom benchmark;
- current literature has not already made it the load-bearing object.

Examples of the *shape*, not approved topics:
- ontological status vs knowledge;
- arbitrary-choice mode vs distribution writer;
- finite nested knowledge vs public/common-knowledge compression.

This is a much better search template than:

> find a weird behavioral interaction no one has reported.

---

# 11. Final promotion rule

A question is worth pushing when:

> **the question itself would still be worth asking if we did not know the answer,
> several possible answers would be scientifically informative, the data can remain
> simple, the object supports behavioral and mechanistic depth, and a current-literature
> reviewer cannot compress it into an existing phenomenon.**

In compact form:

**Durable object  
× conceptual novelty  
× outcome robustness  
× simple substrate  
× broad research space  
× falsifiable discovery  
× deep explanatory path**

must all be present.

A large effect is not a substitute for any one of them.
