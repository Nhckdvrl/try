# Non-Obviousness-First Research-Question Search — 2026-09-06 V12

**Target:** NAACL Main, calibrated against ACL / EMNLP / NAACL Main and especially Best / Outstanding / Best Theme work.  
**Status:** current research-question search authority after the V11 data-first reconstruction.  
**Important:** **NO APPROVED PAPER MAINLINE. NO COMPUTE AUTHORIZED BY V12.**

---

# 0. Why V12 exists

V10/V11 correctly elevated data provenance, but one additional failure mode remained:

> a question can be natural, novel, and supported by excellent D0–D2 data while still being scientifically unsurprising.

The clearest example is the current CK formulation:

> finite mutual knowledge is not common knowledge; do LLMs preserve the distinction?

That is a legitimate scientific distinction, but the question itself risks being a textbook competence check. Good data do not make that question Main-level.

V12 therefore adds a hard **Non-Obviousness / Scientific-Tension Gate** to the governing methodology.

The target shape is not:

> “X and Y differ. Does the model know this?”

The target shape is closer to recent high-level work:

- irrelevant information changes generation (**NAACL 2025 Semantic Leakage**);
- stated values fail to predict actions (**EMNLP 2025 Outstanding Value–Action Gap**);
- equivalent risky-choice content produces qualitatively different behavior under description vs experience, with a reasoning/conversational split (**ACL 2026 Outstanding DH Gap**);
- a learned teleological prior overrides the licensed semantic distinction (**ACL 2026 Best Imperfective Paradox**).

These questions contain a tension before any result is observed.

References:
- https://aclanthology.org/2025.naacl-long.35/
- https://aclanthology.org/2025.emnlp-main.154/
- https://aclanthology.org/2026.acl-long.479/
- https://2026.aclweb.org/program/best_papers/
- https://aclanthology.org/2026.acl-long.689/

---

# 1. V12 executive decision

| object | V12 verdict | reason |
|---|---|---|
| **IFG — Task-Conditioned Evidence Weighting / Inference–Forecast Gap** | **SERIOUS CANDIDATE / D2 / CONTINUE FRONT-END AUDIT / NO COMPUTE YET** | naturally surprising task-invariance violation; published human paradigm + exact Bayesian benchmark |
| **CK — Finite Mutual Knowledge vs Common Knowledge** | **KILL CURRENT FORMULATION** | excellent D2 data, but core question fails the new non-obviousness gate |
| **HOM — Plural Homogeneity / Truth-Value Gaps** | **DEMOTE / SEARCH-ONLY / NO COMPUTE** | data excellent, but current RQ still risks “does the model know a formal-semantic distinction?” |
| **PD — Partition Dependence / Representation-Induced Probability Prior** | **SCREENED / NOT ACTIVE** | non-obvious and D2, but strong compression to generic framing/cognitive-bias/confidence-distortion work |
| **Hindsight bias** | **KILL** | already directly present in broad LLM cognitive-bias evaluation |
| **Dependent-evidence / copy-counting** | **KILL** | direct August 2026 RAG collision |
| **AE** | **KILL (V11)** | D4/gold risk |
| **GRN** | **KILL (V11)** | natural-data version loses novelty; novel version loses data naturalness |

There is currently **one serious candidate, IFG**. This is not a mainline approval.

---

# 2. High-level question-shape calibration

## 2.1 NAACL 2025 Main — Semantic Leakage

Question shape:

> Why does information that is irrelevant to the intended completion systematically leak into generation?

The paper is not “can models identify irrelevant facts?” It discovers a model behavior that violates an intuitive relevance invariance and shows it across languages/models/settings.

Reference:
https://aclanthology.org/2025.naacl-long.35/

## 2.2 EMNLP 2025 Outstanding — Value–Action Gap

Question shape:

> Can a model’s stated values actually predict its actions?

The tension is between two readouts that are often implicitly assumed equivalent.

Reference:
https://aclanthology.org/2025.emnlp-main.154/

## 2.3 ACL 2026 Outstanding — Mind the (DH) Gap!

Question shape:

> Does the same risky prospect induce different choices depending on whether it is explicitly described or learned from experience?

The contribution is strengthened by the discovered reasoning-vs-conversational regime split.

Reference:
https://aclanthology.org/2026.acl-long.479/

## 2.4 ACL 2026 Best — Imperfective Paradox

Question shape:

> Do model inferences follow compositional event semantics, or does a learned goal-completion prior override it?

The paper becomes high-level through the model-side **Teleological Bias**, not through the existence of a known linguistic distinction.

Reference:
https://2026.aclweb.org/program/best_papers/

## 2.5 V12 takeaway

A high-level behavioral RQ often exposes one of:

1. an invariance that unexpectedly fails;
2. two readouts that should reflect the same state but diverge;
3. a formally irrelevant factor that causally changes behavior;
4. a learned prior that defeats a licensed computation;
5. a qualitative training/model-regime split.

This does not mean every Main paper must have a “gap” name. It means the **question itself must contain scientific tension, not just a category boundary**.

---

# 3. CK re-audit under the non-obviousness gate

## 3.1 Current RQ

> How do LLMs represent the qualitative boundary between finite mutual knowledge and genuine common knowledge?

## 3.2 Why V11 liked it

- common knowledge is a real scientific object;
- PNAS 2026 supplies excellent D2 human materials;
- gold and manipulations are independently grounded;
- LLM higher-order ToM work does not clearly own the exact finite-vs-common boundary.

## 3.3 Why that is no longer sufficient

The shortest explanation of CK is:

> finite mutual knowledge is not common knowledge; test whether LLMs distinguish them.

An informed reviewer can reasonably answer:

> “Yes, those are definitionally/theoretically different. You built a diagnostic of whether the model respects the distinction.”

That is a **capability check**, not yet a discovery question.

The attractive model-side possibilities from V11—overclosure, recognition/use dissociation, reasoning-model split—are **possible results**, not a pre-existing reason why CK is scientifically non-obvious. Authorizing compute in the hope that one appears would be effect hunting.

## 3.4 Reviewer compression

> “This is another higher-order ToM benchmark testing a textbook common-knowledge distinction.”

Under V12, current CK cannot rebut this *before results*.

## 3.5 Verdict

> **KILL CURRENT CK FORMULATION.**

The PNAS data remain useful scientific material, but data quality is not promotion evidence.

CK may return only if a genuinely different pre-motivated question is found in which common knowledge is a substrate rather than the contribution—for example, an independently established coordination phenomenon that makes two plausible computational accounts disagree. Do not run PNAS materials merely to search for such an effect.

---

# 4. HOM re-audit

## 4.1 Current RQ

> When natural-language semantics licenses a truth-value gap, do LLMs preserve “neither true nor false,” or collapse it into binary truth conditions?

## 4.2 Strengths retained

- mature independent semantic object;
- D2 human experiments;
- independent adult judgments;
- two diagnostic methods;
- strong universal/existential controls;
- no direct plural-homogeneity LLM paper located in V11.

## 4.3 New concern

The question can still compress to:

> “Natural language has a known non-bivalent phenomenon; do models represent it?”

That is structurally similar to the CK problem.

“Bivalent Collapse” would be interesting if discovered, but it cannot be used retroactively as the reason the question was Main-level before the experiment.

## 4.4 Verdict

> **DEMOTE / SEARCH-ONLY / NO COMPUTE.**

HOM can return only if we find an independently motivated higher-level tension—e.g. a real downstream setting where two evaluation interfaces imply contradictory truth judgments despite identical complete evidence—and the homogeneity paradigm becomes a clean identification substrate.

Do not run the D2 materials merely because they are convenient.

---

# 5. Serious Candidate Card — IFG

Working label:

**IFG — Task-Conditioned Evidence Weighting / Inference–Forecast Gap**

Human scientific anchor:
Tony Q. Fan, Yucheng Liang, Cameron Peng, *The Inference-Forecast Gap in Belief Updating*, Econometrica 2026.

Reference:
https://onlinelibrary.wiley.com/doi/10.3982/ECTA23334

Replication package:
https://doi.org/10.5281/zenodo.18928459

## 5.1 Research Question

> **Does an LLM weight the very same evidence differently depending on whether it is asked what is true now or what will happen next?**

More technical:

> **When inference about a latent state and forecast revision are normatively linked by the same Bayesian update, does changing only the target statistic change the model’s evidence-weighting rule?**

## 5.2 One-sentence version

> Give the model the same prior, same data-generating process, and same observed signal; does it update one way when inferring the hidden state and a different way when forecasting the next observation?

## 5.3 Why this is not obvious

This is not the textbook distinction “inference ≠ prediction.”

The Econometrica design creates paired problems in the **same information environment**:
- same DGP;
- same prior;
- same realized signal.

Under the Law of Iterated Expectations, the rational update in the inference answer maps directly onto the rational forecast revision. Even the *same non-Bayesian inference rule*, if consistently propagated into forecasting, satisfies the no-gap relation.

Therefore a gap means more than numerical error:

> the task changes the computation used to process the same evidence.

Humans show an especially surprising directional pattern:
- inference: underreaction;
- forecast revision: overreaction.

The paper attributes much of the gap to different simplifying heuristics triggered by the target statistic.

## 5.4 Paper Identity

**Scientific / behavioral discovery about LLM belief updating**, with direct relevance to forecasting and agent decision support.

Not a benchmark/resource paper.

Not “LLMs versus humans on one cognitive bias.”

## 5.5 Why NLP/LLM researchers should care

LLMs are increasingly asked to do both:
- infer hidden states from evidence (“What is likely true?”);
- forecast downstream outcomes from the same evidence (“What happens next?”).

If their evidence weighting is task-dependent, there may be no single stable “belief state” recoverable from ordinary elicitation. A model could appear conservative as an analyst and extrapolative as a forecaster without receiving different evidence.

That matters for:
- forecasting agents;
- diagnostic assistants;
- scientific reasoning;
- risk analysis;
- multi-step agent pipelines where latent inference feeds downstream prediction;
- calibration evaluation.

## 5.6 Natural example

Suppose a firm is either Good or Bad. Good and Bad firms generate monthly growth rates from known distributions. The model sees the pool composition and one realized growth signal.

Ask A:
> What is the probability the firm is Good?

Ask B, with the same DGP and signal:
> What growth rate do you expect next month?

The two answers are mathematically linked. If the model uses one coherent posterior over firm quality, B should be obtained from A through the known expectation mapping.

The scientific question is whether task wording/target statistic makes the model abandon that coherent update.

## 5.7 Scientific object

**Task-conditioned belief updating under normatively linked readouts.**

The human IFG is the scientific anchor, but the LLM object is broader:

> whether different linguistic task interfaces reveal one coherent posterior or invoke different evidence-processing computations.

## 5.8 Competing hypotheses

**H1 — Coherent latent-belief account.**  
The model may be Bayesian or biased, but inference and forecast revision express the same underlying posterior after the known transformation. No systematic gap.

**H2 — Human-like task-conditioned heuristics.**  
Inference and forecasting trigger different heuristics; models underreact in inference and overreact in forecast revision.

**H3 — Model-specific task-conditioned heuristic switch.**  
A systematic gap exists, but its direction/modes differ from humans (e.g. extrapolation in both tasks, or forecast underreaction).

**H4 — Training-regime dependence.**  
Reasoning/post-training changes cross-task coherence: some regimes preserve the no-gap mapping while others switch heuristics across tasks.

**H5 — Arithmetic implementation failure.**  
The apparent gap arises only because the model fails to apply the deterministic inference-to-forecast mapping. A standalone LoIE/comprehension control should explain the effect.

## 5.9 Prediction-changing axis

Broad Bayesian-reasoning work predicts better/worse updating accuracy.

IFG asks something different:

> after controlling the information environment and normative update, does the *requested target statistic itself* change the update rule?

Decisive discrimination:
- same prior;
- same likelihood/DGP;
- same realized signal;
- paired inference and forecast revision;
- compute each answer’s update relative to its mathematically matched rational benchmark;
- test whether the direction/magnitude/mode is task-conditioned.

## 5.10 High-Level Calibration Set

### ACL 2026 Outstanding — Mind the (DH) Gap!
Strongest paper-shape anchor.
Both ask whether a representation/task interface changes behavior when the underlying decision/evidence structure is tightly linked. DH Gap becomes high-level through a reasoning-vs-conversational regime split and matched human baseline.

### EMNLP 2025 Outstanding — Value–Action Gap
Shows that two outputs often treated as manifestations of one latent property can diverge.

### NAACL 2025 Main — Semantic Leakage
Shows that an ostensibly irrelevant factor can systematically change model output.

### ACL 2026 Best — Imperfective Paradox
Shows a model-specific heuristic/prior overriding a principled computation.

IFG should be judged against these paper identities, not against generic Bayesian QA benchmarks.

## 5.11 Closest LLM neighbors / novelty assassination

### BayesBench (June 2026)

BayesBench evaluates LLM belief trajectories across:
1. Bayesian estimation;
2. Bayesian prediction;
3. latent-framed Bayesian prediction.

It reports that improvements in latent inference do not reliably carry over to downstream prediction.

This is the strongest collision.

However, BayesBench does **not** currently own the IFG estimand:
- its estimation and prediction tasks are instantiated in different environments/tasks;
- it does not pair the same DGP + same realized signal under inference and forecast-revision elicitation;
- it does not define the Econometrica no-inference-forecast-gap mapping;
- it does not test a matched underreaction ↔ overreaction switch caused only by the target statistic.

Reference:
https://arxiv.org/abs/2606.30850

### Hypothesis generation and updating in LLMs (May 2026)

This work probes one inferred posterior through posterior prediction, hypothesis evaluation, and generation, and reports an evaluation–generation gap plus thinking-mode changes.

This is conceptually close because it questions whether one coherent posterior explains different readouts.

Threat:
> IFG cannot claim “different probes reveal inconsistent beliefs” as a new abstraction.

Surviving axis:
> matched inference-vs-forecast evidence weighting with an exact normative mapping and directional updating errors.

Reference:
https://arxiv.org/abs/2605.05851

### Bayesian teaching / other Bayesian reasoning work

These occupy general Bayesian competence, belief updating, calibration, and elicitation—not the exact matched task-conditioned update rule.

## 5.12 Parent abstraction

> **Do LLMs possess one task-invariant belief state, or does the linguistic target of the question select a different evidence-processing computation?**

This is a stronger parent than “can LLMs do Bayesian reasoning?”

## 5.13 Reviewer compression sentence

> **“This is just another Bayesian reasoning / cognitive-bias benchmark.”**

## 5.14 Rebuttal condition

The compression is valid if the paper reports:
- inference accuracy;
- forecast accuracy;
- average human/LLM bias;
- a new named cognitive bias.

It is not valid if the decisive result is a **within-evidence computational dissociation**, such as:

> the same evidence is underweighted in latent-state inference but overweighted in forecast revision, despite the model correctly applying the deterministic mapping when its inference answer is explicitly supplied.

That identifies task-conditioned computation rather than generic probability error.

## 5.15 Existing data

Econometrica 2026 provides:
- exact experimental design;
- paired inference / forecast-revision problems;
- multiple DGPs;
- comprehension controls;
- robustness treatments;
- human response distributions;
- public replication package on Zenodo;
- published experimental instructions.

## 5.16 Data provenance tier

**D2.**

The human paradigm, stimuli/DGPs, analysis, gold, and response modes all predate this LLM hypothesis.

## 5.17 Gold source

Gold is mathematical:
- Bayes rule;
- Law of Iterated Expectations;
- known DGP.

The no-gap mapping is independently defined by the human paper.

No subjective author labeling is required.

## 5.18 Data construction risk

**Low for primary pilot** if the original information environments/instructions are reused with only interface adaptation.

Do not invent new finance stories before the published paradigm is exhausted.

## 5.19 Human validation requirement

No new human experiment for P0. Published human data supply the reference.

Any substantial simplification of instructions must preserve comprehension and the no-gap mapping.

## 5.20 Artifact risks

- arithmetic burden differs between tasks;
- models may misread expected value as probability;
- output scale/bounds differ;
- “future” wording could trigger generic extrapolation;
- long instructions may create formatting errors;
- direct numeric elicitation may be prompt-sensitive.

The human paper already contains controls that help:
- deterministic-outcome treatment;
- binary-signal treatment;
- explicit inference-to-expectation relationship;
- comprehension checks;
- treatments reducing similarity to heuristic-inducing statistics.

## 5.21 Contamination risk

The Econometrica article is extremely recent (first published July 29, 2026), but earlier working-paper versions date back several years.

Therefore exact-text memorization cannot be assumed absent.

Mitigation:
- preserve DGP mathematics but vary neutral surface framing only after primary reproduction;
- do not mention “inference-forecast gap,” underreaction, or human findings in prompts;
- test whether response geometry follows the exact mathematical mappings rather than textbook prose;
- use multiple DGPs from the replication package.

## 5.22 Outcome robustness

Scientific informativeness:

**A. Human-like IFG + model-regime split** — very strong.  
Potential Main shape, especially if reasoning models preserve coherence while conversational models switch heuristics.

**B. Stable model-specific gap with different direction/modes** — strong.  
Suggests task-conditioned evidence processing specific to LLMs.

**C. Human-like gap in all models** — interesting but high risk of “humans show X, models too.” Needs an additional LLM-specific law to reach Main.

**D. No gap across models** — clean negative result but probably not Main by itself; likely KILL.

Thus IFG is not outcome-robust enough to pre-approve a paper. It is strong enough to continue front-end audit.

## 5.23 What would be trivial even if positive?

- models make Bayesian errors;
- forecast answers are less accurate than inference answers;
- one model has a statistically significant difference;
- models replicate the human mean gap without a model-specific structural finding;
- explicit CoT improves arithmetic;
- prompted with the LoIE formula, models improve.

## 5.24 Main-scale growth path

Only if C1 is non-trivial:

**C1 — Task-conditioned evidence-weighting law.**  
Establish whether matched inference and forecast revision expose one coherent update or different heuristic regimes.

**C2 — Rule out implementation complexity.**  
Use the published infer-then-LoIE / deterministic / similarity controls.

**C3 — Regime / training law.**  
If naturally present, test matched reasoning vs conversational / thinking vs non-thinking models in the style justified by ACL 2026 DH Gap.

**C4 — External validity.**  
Only then test a natural forecasting/diagnostic substrate where the same evidence supports state inference and outcome forecasting.

No mechanism work unless C1–C3 justify it.

## 5.25 Data Alignment Matrix

| field | IFG | ACL 2026 DH Gap | BayesBench 2026 | Econometrica IFG |
|---|---|---|---|---|
| data source | published human experiment | established risky-choice paradigms + matched human experiment | purpose-built simulation benchmark | human experiments |
| existed before LLM hypothesis | yes | human paradigm yes | benchmark built for LLMs | yes |
| gold | exact Bayes + LoIE | expected-payoff rational reference + humans | Bayesian posterior trajectories | exact Bayes + LoIE |
| matched information | yes, load-bearing | matched prospect structure across representation | not same environment across all task types | yes |
| human baseline | published full human data | matched human subjects | no load-bearing matched human law | direct |
| data tier | D2 | paradigm-first / human calibrated | synthetic formal benchmark | source paradigm |
| core tension | target statistic changes evidence weighting | representation changes risky choice | latent inference may not transfer to prediction | human inference underreaction vs forecast overreaction |
| Main-level burden | requires model-side structural law | achieved regime split | benchmark/scientific analysis | human mechanism paper |

## 5.26 Pilot policy

**V12 does not yet authorize target-model compute.**

Before pilot:
1. retrieve the replication package/instructions;
2. reconstruct the exact paired estimand;
3. finish a line-by-line BayesBench / hypothesis-updating comparison;
4. search 2025–2026 forecasting/calibration work for task-framing versions;
5. confirm no paper already reports matched same-evidence inference/forecast directional reversal.

If those survive, authorize only the minimum paired pilot.

## 5.27 Explicit kill criteria

KILL IFG before or after P0 if:
1. a recent LLM paper is found that already owns the same matched inference–forecast estimand;
2. BayesBench or another neighbor contains an equivalent paired same-evidence experiment after full inspection;
3. the task difference cannot be made computationally comparable for LLMs;
4. apparent gap disappears when the model’s inference answer is supplied to the forecast step;
5. all interesting effects reduce to numeric output bounds or prompt format;
6. strongest result is “LLMs are imperfect Bayesians”;
7. strongest result is merely a human replication with no model-specific law.

## 5.28 Current verdict

> **SERIOUS CANDIDATE / RANK 1 / D2 / CONTINUE FRONT-END NOVELTY + DATA AUDIT.**
>
> **NO COMPUTE YET. NOT AN APPROVED MAINLINE.**

---

# 6. Partition Dependence (PD) — screened, not active

## 6.1 Attractive RQ

> **Can the model assign a different probability to the same event merely because the rest of the state space is partitioned differently?**

Classic example:
- “Probability Sunday is hotter than every other day” naturally cues a two-way partition;
- “Probability the hottest day is Sunday” cues seven mutually exclusive days.

The target event is extensionally the same, but human judgments shift toward the corresponding ignorance prior (1/2 vs 1/7).

Human evidence is strong:
- classic Fox/Rottenstreich/Fox-Clemen work;
- 2025 Registered Report, N=603, mostly successful replication.

References:
- https://pubmed.ncbi.nlm.nih.gov/12741740/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12308232/

## 6.2 Why it initially looks strong

- one-minute intelligible;
- genuinely non-obvious;
- exact invariance violation;
- D2 materials;
- quantitative prediction (attraction toward 1/M), not arbitrary effect hunting;
- relevant to LLM probability elicitation and candidate-set interfaces.

## 6.3 Why it is not active

The neighboring LLM space is already dense:
- broad cognitive-bias evaluations;
- prompt-framing / choice-set effects;
- MCQA option-set sensitivity;
- EMNLP 2025 Findings *Self-Ensemble* directly documents confidence distortion as the number of choices grows and mitigates it by partitioning answer choices into groups.

Reference:
https://aclanthology.org/2025.findings-emnlp.902/

Reviewer compression:

> “This is another choice-set / prompt-framing confidence distortion effect, now connected to support theory.”

The exact ignorance-prior prediction appears not directly owned in the searches so far, but that may be **exact-cell novelty** rather than Main-level novelty.

## 6.4 Verdict

> **SCREENED / NOT ACTIVE / NO COMPUTE.**

Continue literature search only if a broader, genuinely model-specific “representation-induced prior” law can be motivated independently of the classic bias name.

---

# 7. Newly killed search lanes

## 7.1 Simple LLM hindsight bias

KILL.

A 2025 ACL-associated broad benchmark already includes explicit Hindsight Bias among 30 cognitive biases and evaluates 20 LLMs / 30k tests.

Reference:
https://aclanthology.org/2025.nlp4dh-1.50/

A ForecastBench-based version would need a genuinely different self-reconstruction or temporal-information axis; simple “outcome knowledge changes ex-ante probability” is not available.

## 7.2 Dependent evidence / copied-source corroboration

KILL.

The attractive natural question was:

> if eight sources repeat one originating claim, does the model treat them as eight independent pieces of evidence?

But August 2026 work directly studies confidence inflation from dependent/copied evidence in RAG (“Counting Copies as Evidence: Confidence Inflation from Dependent Evidence in RAG”).

This is too direct a collision for an active lane.

## 7.3 Generic “different probe, different belief”

Do not use this as IFG novelty.

The 2026 hypothesis-generation/updating paper already finds an evaluation–generation gap across multiple probes of a posterior.

IFG survives only at the specific matched inference-vs-forecast evidence-weighting axis.

---

# 8. Current search state

There is no approved paper mainline.

There is no requirement to maintain three candidates.

Current state:

1. **IFG — one serious candidate under front-end audit.**
2. **HOM — demoted; no compute.**
3. **PD — screened but not active.**
4. **CK — current formulation killed.**
5. everything else remains killed/archive unless a genuinely new scientific tension appears.

---

# 9. V12 one-sentence authority

> **A Main-level candidate must be interesting before we run it: excellent data and an unoccupied distinction are insufficient when the research question is merely “does the model know X ≠ Y”; prefer questions where identical relevant evidence, ostensibly equivalent representations, or multiple readouts of one latent state make competing computations predict a non-obvious qualitative divergence.**
