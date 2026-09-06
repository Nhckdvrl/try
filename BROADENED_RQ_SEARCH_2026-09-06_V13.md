# Broadened Research-Question Search — 2026-09-06 V13

**Target:** NAACL Main, calibrated against ACL / EMNLP / NAACL Main and especially Best / Outstanding / Best Theme work.  
**Status:** current research-question/search authority after V12.  
**Important:** **NO APPROVED PAPER MAINLINE. NO TARGET-MODEL COMPUTE AUTHORIZED.**

---

# 0. Why V13 exists

V12 fixed an important failure mode: a question can be natural, novel, and supported by excellent D0–D2 data while still being scientifically obvious.

This round adds two further corrections.

First, repeated 2024–2026 collision search shows that **"gap", "consistency", or "invariance violation" is no longer a sufficient novelty unit by itself**. Many recent papers already own broad cross-readout consistency, task-framing sensitivity, belief/action coherence, elicitation consistency, and related parent questions.

Second, the search had become too concentrated on behavioral/mechanistic LLM phenomena. That is unnecessarily restrictive and risks entering crowded areas. The project therefore broadens paper identity to include:

- scientific / behavioral discovery;
- mechanistic discovery;
- **methodological discovery**;
- **measurement / evaluation methodology**;
- **human-science-at-scale methods**;
- **old scientific workflows made newly feasible by LLMs**;
- benchmark/resource work only when the benchmark itself changes what can be scientifically concluded;
- critical audit / negative result;
- use-inspired scientific work.

The advisor-level heuristic motivating this expansion is:

> Look for an old, important human/scientific problem whose method was historically bottlenecked, and ask whether LLMs change the feasible research design.

This is not permission for:
> "LLM replaces annotator/interviewer/crowd worker."

The method must change the scientific capability, estimand, or falsifiability of the workflow—not merely reduce labor cost.

---

# 1. V13 governing additions

## 1.1 Structural Specificity Gate

A surprising gap is not enough.

For any candidate built around two readouts, tasks, interfaces, or representations, ask:

> **What object-specific mathematical, causal, linguistic, statistical, or decision-theoretic relation makes this particular divergence scientifically diagnostic?**

If recent work already owns the parent notion of cross-readout inconsistency, a new readout pair is presumed non-novel unless it induces at least one of:

1. a distinct structural estimand;
2. a distinct causal law;
3. a distinct competing-theory diagnostic;
4. a theorem/normative mapping whose violation rules out a plausible account;
5. a diagnostic subset where competing accounts make different qualitative predictions.

Default weak form:

> "A and B should be consistent, but maybe LLMs differ."

Default response:

> **KILL unless the A↔B relation itself supplies new scientific identification.**

IFG's current survival is due largely to the exact LoIE bridge, not because "inference and prediction may disagree."

## 1.2 Crowdedness / Workload Gate

Novelty is not the only practical concern.

Prefer directions where:
- the parent field is not already saturated with many interchangeable LLM papers;
- the core contribution can be identified with a small number of decisive experiments;
- the project does not require building a large platform, collecting a new benchmark from scratch, or running an agent/RL/model-zoo arms race merely to be competitive;
- there is a credible Main-level story before adding scale.

High-crowding neighborhoods currently include:
- generic LLM-as-annotator;
- generic LLM interviewer / conversational survey;
- generic AI-generated experimental stimuli;
- generic cognitive-bias benchmarking;
- generic prompt/readout consistency;
- generic agentic scientific discovery;
- generic LLM-as-judge.

A new direction in one of these neighborhoods must have an unusually strong structural distinction to survive.

## 1.3 Old-Problem / New-Method Gate

For "LLM changes an old scientific method" candidates, require all of:

A. **Old bottleneck:** What important scientific workflow/problem existed well before LLMs?

B. **LLM-specific affordance:** What becomes feasible now that was genuinely difficult before?  
Natural-language generation, adaptive interaction, broad linguistic transfer, tool-mediated search, or structured synthesis may qualify. Mere cheap labeling does not.

C. **Scientific delta:** What scientific conclusion/design becomes possible, not merely cheaper?

D. **External substrate:** Can evaluation use data, gold, archives, expert analyses, or experiments that existed independently of our method?

E. **Reviewer compression:** Why is this not simply "use an LLM to automate X"?

F. **Workload realism:** Can C1 be established without a giant new data-collection campaign?

---

# 2. Current candidate state

| object | V13 verdict |
|---|---|
| **IFG — Task-Conditioned Evidence Weighting / Inference–Forecast Gap** | **SERIOUS CANDIDATE / D2 / FRONT-END AUDIT / NO COMPUTE** |
| **HOM — Plural Homogeneity / Truth-Value Gaps** | **SEARCH-ONLY / NO COMPUTE** |
| **Field-linguistics adaptive elicitation** | **PROMISING SEARCH LANE ONLY / NOT A CANDIDATE** |
| **Comparative-method / historical-linguistics workflow** | **PROMISING SEARCH LANE ONLY / NOT A CANDIDATE** |
| **LLM + theory-discriminating experimental design for language science** | **SEARCH LANE ONLY / HIGH HUMAN-VALIDATION RISK** |
| **PD — Partition Dependence** | **KILL** |
| **CK current formulation** | **KILL** |
| **AE / GRN** | **KILL** |

There is still only one serious candidate.

No candidate has been approved as the paper mainline.

---

# 3. IFG source-level BayesBench audit

BayesBench is a substantially stronger collision than V12's abstract-level description suggested.

Its recommender-system environment:
- observes one fixed rating history;
- directly elicits an LLM latent-type posterior;
- predicts a held-out movie rating;
- computes an exact Bayesian type posterior and predictive reference;
- tests explicit conditioning on the inferred type;
- contains infrastructure for posterior-weighted marginalization over type-conditioned predictions.

Its paper-level result is therefore already stronger than:
> "estimation and prediction are different benchmark tasks."

BayesBench owns:
> **better latent inference does not automatically yield better downstream prediction.**

However, the current surviving IFG distinction remains meaningful.

In BayesBench, the target movie is intentionally omitted from the profile information. Going from an elicited user type to the held-out rating still requires generalization to an unseen movie. The two readouts are therefore not connected by the same minimal exact mapping that defines the Econometrica inference–forecast design.

IFG instead seeks:
- same DGP;
- same prior;
- same realized signal;
- paired latent-state inference and next-outcome forecast;
- exact normative mapping through the DGP / Law of Iterated Expectations;
- evidence-weighting direction as the estimand.

Therefore IFG may not claim:
- generic inference/prediction inconsistency;
- generic latent-state readout failure;
- generic "knows but cannot use";
- generic Bayesian competence.

Its surviving axis is only:

> **Does changing only the requested target statistic select a different evidence-weighting computation even when the two readouts are linked by an exact inference→forecast mapping?**

Verdict remains:

> **SERIOUS / NO COMPUTE.**

BayesBench or another paper still kills IFG if full paper analysis reveals an equivalent same-evidence paired estimand.

---

# 4. PD final decision

## PD — Partition Dependence

V12 listed PD as screened/not active.

Subsequent search found a much more direct 2026 collision:

> **Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models**

The neighboring space already owns LLM statistical consistency under changing partitions/aggregations, on top of broader prompt-framing, choice-set, and confidence-distortion work.

The remaining support-theory / ignorance-prior cell is too vulnerable to exact-cell novelty.

Verdict:

> **KILL.**

Do not revive via a different partition example, support-theory terminology, or candidate-set interface.

---

# 5. Newly assassinated structural-gap lanes

The following directions were attractive under V12 but fail the Structural Specificity / novelty gates.

## 5.1 Evidence order / Bayesian commutativity

Attractive tension:
Bayesian evidence combination is order-invariant while sequential language processing may not be.

Why not active:
- mature LLM order-sensitivity literature;
- 2026 work already studies evidence order / intermediate judgments in decision settings;
- reviewer compression becomes "a more semantic order-sensitivity benchmark."

Verdict:
> **DO NOT ACTIVATE.**

## 5.2 Stopping-rule invariance / optional stopping

Attractive tension:
same observed sample can arise under different stopping rules; likelihood-principle/Bayesian accounts may treat them similarly.

Why not promoted:
- the normative status is genuinely contested and prior/calibration dependent;
- no clean D0–D2 paired substrate was found comparable to IFG;
- a result could be interpreted as choosing a statistical philosophy rather than exposing an LLM-specific computation.

Verdict:
> **SEARCH CLOSED FOR CURRENT FORMULATION / NO COMPUTE.**

## 5.3 Martingale / Reflection / future-belief coherence

Direct parent occupation:
- NeurIPS 2025 Martingale Score;
- 2026 belief-drift/coherence follow-up work.

Verdict:
> **KILL.**

## 5.4 Probability–quantile / binary–numeric forecasting duality

Attractive exact relations exist between a predictive distribution, CDF values, and quantiles.

Why killed:
- forecasting-consistency work already audits logically related forecasts;
- 2026 forecasting work directly reports elicitation divergence across numerical/binary formats.

A CDF↔quantile instantiation would be a stricter exact cell inside an occupied parent.

Verdict:
> **KILL.**

## 5.5 Selection / sampling-mechanism neglect

Human paradigms and old scientific theory are strong.

But 2026 LLM work directly studies:
> selected evidence, omitted information, and belief updating in LLM decision support.

Verdict:
> **KILL.**

## 5.6 Production–comprehension / speaker–listener duality

Direct 2026 collision:
> listener–speaker asymmetries in LLM pragmatic competence.

A more Bayesian reference-game implementation would not recover the parent RQ.

Verdict:
> **KILL.**

## 5.7 Verbal vs numerical uncertainty → action

Recent LLM literature already studies epistemic markers/verbal probabilities, numerical interpretations, and downstream decisions/evaluations.

The remaining "matched translation but different policy" cell is too exact-cell-like.

Verdict:
> **KILL.**

## 5.8 Belief–utility separation

This was one of the strongest question shapes found:
same evidence should determine belief; costs should change the action threshold, not reported probability.

Direct 2026 collision:
> **When Policies Change Probabilities**

The paper already fixes evidence, manipulates downstream cost, and shows large changes in reported failure probability.

This occupies the parent RQ, decisive intervention, and structural law.

Verdict:
> **DIRECT KILL.**

## 5.9 Self-policy contamination of other-person prediction

Attractive human-science design:
causally change one's own policy and test whether predictions of a distinct other person move with it.

But 2025 LLM work already directly tests Simulation Theory in LLM Theory of Mind using interventions/perspective manipulations, with adjacent work comparing own decisions and simulated/predicted human decisions.

Verdict:
> **KILL.**

## 5.10 Irrelevant evidence / dilution

Classic human paradigm, natural invariance violation.

But it compresses into:
- Semantic Leakage;
- irrelevant-information sensitivity;
- recent causal-judgment robustness work.

No independent structural law survived search.

Verdict:
> **DO NOT ACTIVATE.**

---

# 6. Broad-paper-identity search: what was tried and rejected

## 6.1 Generic LLM-generated experimental stimuli

This is now an active literature:
- automated psycholinguistic stimulus construction;
- validity/acceptability studies;
- STAGS / scope testing with AI-generated stimuli;
- general social-science stimulus generation.

STAGS explicitly connects generative AI to the old language/stimulus generalizability problem and representative design.

Therefore:
> "LLMs let us generate many stimuli and test generalizability"

is already a parent method.

Verdict:
> **GENERIC VERSION KILL / TOO CROWDED.**

A future version would need a qualitatively different scientific objective such as explicit competing-theory discrimination, not just more stimulus diversity.

## 6.2 Open-ended survey measurement

Recent work already:
- scales open-ended responses with LLM pairwise comparisons;
- studies open-vs-closed question form;
- uses LLM/computational coding to make open-ended survey analysis scalable.

Verdict:
> **DO NOT ENTER. CROWDED MINI-FIELD.**

## 6.3 AI conversational / cognitive interviewing

By 2025–2026 there are multiple direct LLM interviewer, adaptive interview, semi-structured interview, and AI cognitive-interview methods.

Verdict:
> **KILL GENERIC VERSION / TOO CROWDED.**

## 6.4 LLM annotation for valid group/scientific inference

Important problem, but parent literature is already strong:
- valid statistical inference with uncertain LLM annotations;
- debiasing LLM-based parameter estimates;
- non-random annotation error linked to subject characteristics;
- demographic/context-dependent annotation bias;
- emerging measurement-theory treatments.

Therefore:
> "high annotation accuracy may still bias group comparisons"

is no longer an unoccupied parent RQ.

Verdict:
> **DO NOT ACTIVATE WITHOUT A NEW STRUCTURAL ESTIMAND.**

## 6.5 Generic LLM as psycholinguistic norming/crowd worker

2024–2026 work already directly evaluates LLM-generated psycholinguistic norms and whether LLMs can replace/augment human ratings.

Verdict:
> **TOO OCCUPIED.**

## 6.6 Cross-cultural test translation/adaptation

LLM-based psychometric test adaptation has already been empirically validated with human samples and measurement-invariance analysis.

Verdict:
> **DO NOT ENTER GENERIC VERSION.**

## 6.7 Generic autonomous corpus linguistics

2026 work already proposes an LLM agent that formulates hypotheses, queries corpora, interprets results, and iteratively refines analysis.

Verdict:
> **GENERIC "LLM scientist for corpus linguistics" IS OCCUPIED.**

---

# 7. Promising broadened search lane A — Target-language-adaptive field elicitation

This is **not yet a candidate**.

## 7.1 Old scientific problem

Descriptive/field linguistics has always faced an acquisition-budget problem:

> Given limited access to an informant, what sentence/question should the linguist elicit next to distinguish competing grammatical hypotheses?

Historical computational work already attempted structured elicitation:
- Project Boas / "field linguist in a box";
- structurally diverse minimal elicitation corpora;
- active learning for language documentation.

One known limitation of fixed source-language elicitation corpora is **source-language bias**:
target-language-specific distinctions may be missed when the fixed elicitation inventory is derived from structures salient in the source language.

## 7.2 Why LLMs might genuinely change the method

LLMs could in principle:
- maintain explicit competing grammar hypotheses;
- generate target-language-adaptive semantic/communicative probes;
- choose the next elicitation based on which answer would best distinguish hypotheses;
- update the hypothesis set from the informant response.

This is qualitatively different from a fixed questionnaire.

## 7.3 High-level alignment

EMNLP 2025 Outstanding **LingGym** shows that "thinking like a field linguist" is a legitimate high-level NLP paper identity.

Recent language-documentation surveys explicitly identify LLMs as a likely new part of documentary/descriptive workflows.

## 7.4 Major collision

ICML 2025 **Adaptive Elicitation of Latent Information Using Natural Language** already owns the generic:
> use language to actively choose informative questions about a latent entity.

Therefore novelty cannot be:
> "LLM asks informative questions."

The only plausible surviving axis is field-linguistics-specific:

> **Can target-language-adaptive hypothesis testing overcome the source-language bias of fixed elicitation inventories?**

## 7.5 Current fatal unresolved issue

Evaluation/oracle.

Weak versions are unacceptable:
- using another LLM as the "native speaker";
- inventing a synthetic language/world;
- hand-authoring a grammar oracle;
- using only generated responses.

A strong version needs:
- replayable archival field data;
- an existing pool of independently collected elicitation responses;
- or another D0–D2-quality substrate where query→answer is externally grounded.

A pool-selection version using existing IGT is easier but risks collapsing into generic active learning/adaptive elicitation.

## 7.6 Current verdict

> **PROMISING SEARCH LANE / NO COMPUTE / NOT SERIOUS UNTIL DATA-ORACLE PATH IS SOLVED.**

Kill if the only workable implementation needs an LLM informant or bespoke grammar simulator.

---

# 8. Promising broadened search lane B — Comparative Method as an auditable hypothesis cycle

This is **not yet a candidate**.

## 8.1 Old scientific problem

The comparative method is one of linguistics' oldest scientific workflows:
- identify cognates;
- infer regular sound correspondences;
- set aside irregular forms;
- reconstruct proto-forms;
- use systematic correspondence evidence to justify relationships and reconstructions.

Computational historical linguistics has automated many modules for decades.

Recent resources improve the data situation:
- Lexibench (2025) aggregates 63 multilingual wordlists with expert cognacy annotations;
- modern computational historical-linguistics workflows provide explicit sound-correspondence and protoform benchmarks.

## 8.2 Why an LLM might change the feasible workflow

The potentially interesting use of an LLM is not end-to-end protoform prediction.

It is an **auditable hypothesis cycle**:

```
propose correspondence hypothesis
→ identify which cognate sets should follow it
→ search held-out data for counterexamples
→ classify exception vs evidence against the rule
→ revise the correspondence system
→ reconstruct
```

Natural-language/metalinguistic reasoning could make explicit hypothesis revision possible rather than only optimizing a black-box predictor.

## 8.3 Why this is not yet strong enough

Major reviewer compression:

> "This is an agent wrapper around existing computational historical linguistics."

Existing work already:
- performs automatic cognate detection;
- learns sound correspondences;
- reconstructs protoforms;
- identifies irregular cognate sets with leave-one-out correspondence analysis.

So the LLM must enable a scientifically different capability, not just narrate those steps.

## 8.4 Data strengths

Unlike many behavioral candidates, historical linguistics has:
- expert cognate annotations;
- multiple language families;
- known/accepted protoforms in some datasets;
- in some cases an attested ancestor (e.g. Latin), enabling objective reconstruction evaluation.

## 8.5 Major risk: contamination

Pretrained LLMs may have memorized:
- etymologies;
- cognate sets;
- Latin/Romance relations;
- published reconstruction datasets.

Anonymizing language names does not necessarily remove lexical memorization.

Aggressive symbol substitution may remove exactly the phonological knowledge that motivates using an LLM.

This is a load-bearing risk.

## 8.6 Current verdict

> **PROMISING SEARCH LANE / NOT A CANDIDATE.**

Promote only if we find:
1. a capability that classical computational methods genuinely cannot provide;
2. a contamination-resistant evaluation;
3. a Main-scale methodological claim beyond "agentic comparative method."

---

# 9. Search lane C — LLM-guided theory-discriminating experimental design

This is also **not a candidate**.

## 9.1 Old scientific problem

Psychology/cognitive science has a mature literature on adaptive/Bayesian optimal experimental design:
choose the experiment/stimulus maximizing expected information gain between competing models.

Psycholinguistics and linguistic experiments often have a more difficult search space:
the design variable is a structured natural-language stimulus, not a low-dimensional numeric parameter.

## 9.2 Potential LLM affordance

LLM as a proposal/search operator over natural-language stimuli, while a principled model-discrimination objective—not the LLM itself—scores which candidates best separate competing theories.

Potential identity:

> **Use LLM generation to search a combinatorial natural-language design space for maximally theory-discriminating experiments.**

This is stronger than generic stimulus generation because the objective is falsification/model discrimination.

## 9.3 Collisions

Generic pieces already exist:
- Bayesian optimal experimental design;
- LLM + BOED / adaptive elicitation;
- AI-generated stimuli;
- automated experimental design / scientific agents.

No direct parent was found in this search that clearly owns:
> natural-language psycholinguistic stimulus search specifically for competing-theory discrimination.

But exact absence is not promotion evidence.

## 9.4 Main risk

To prove that generated items genuinely discriminate human cognitive/linguistic theories usually requires new human data.

Without a human experiment, the method risks optimizing disagreement between computational proxies rather than scientific theories.

That creates a high workload and validation burden.

## 9.5 Verdict

> **SEARCH-ONLY / HIGH HUMAN-VALIDATION RISK.**

Do not promote unless an existing large human-response dataset can serve as a replayable oracle or the target theories make externally checkable predictions on pre-existing materials.

---

# 10. Lessons from the broadened search

## 10.1 "Method paper" is not an escape hatch

A weak method paper:
> LLM does an expensive human task cheaper.

A stronger method paper:
> LLM changes which experiment, measurement, or scientific inference is feasible.

## 10.2 Avoid newly crowded "LLM-for-science" subfields

2025–2026 already contain:
- AI scientists;
- scientific hypothesis generation benchmarks;
- claim/evidence validation;
- automated corpus research;
- social-science experiment prediction;
- LLM interviewers;
- LLM survey coding;
- LLM stimulus generation.

Entering these requires a sharply independent scientific axis.

## 10.3 Older fields can be useful precisely because they expose old bottlenecks

The desirable pattern is:

> old workflow + explicit historical limitation + new LLM affordance + existing external data + falsifiable improvement.

Not:

> old task + ChatGPT.

---

# 11. Next search priorities

Priority A:
**Continue old-method/new-affordance search** in relatively uncrowded language-science workflows.

Particularly:
- field linguistics / active elicitation;
- comparative/historical linguistics;
- other expert linguistic workflows where free-form language generation changes the query space.

Priority B:
**Search for replayable-oracle datasets.**

The next promotion bottleneck is often not the idea but whether a natural externally grounded experiment can be run without new bespoke data.

Priority C:
**Continue IFG assassination independently.**

IFG is not protected by the broadened search.

Priority D:
**Search non-mechanistic Main/Outstanding paper identities.**

Use strong papers such as:
- LingGym;
- CxMP;
- Generative or Discriminative?;
- strong evaluation/resource/methodology papers;
not only mechanistic or "Gap" papers.

---

# 12. V13 current authority

> **Do not constrain the project to mechanistic/behavioral gap papers. Search across scientific discovery, methodology, measurement, resources, and old human-science workflows newly enabled by LLMs. But a method earns Main-level attention only if it changes the scientific capability—not merely the labor cost—and any new gap/consistency result must be backed by an object-specific structural estimand or competing-theory diagnostic.**

And the original three rules remain:

> **The scientific object should exist before us.**  
> **The data should exist before our hypothesis.**  
> **The scientific tension should exist before the result.**

Add two V13 rules:

> **The structural relation should exist before the gap.**  
> **The new method should change what science can test, not just who performs the work.**
