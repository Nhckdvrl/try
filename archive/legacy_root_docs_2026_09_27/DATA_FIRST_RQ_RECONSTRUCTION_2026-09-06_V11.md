# Data-First Research-Question Reconstruction — 2026-09-06 V11

**Target:** NAACL Main, calibrated against ACL / EMNLP / NAACL Main and especially Best / Outstanding / Best Theme work.  
**Status:** current candidate-selection authority after V10.  
**Governing methodology:** ALIGNMENT_FIRST_RQ_STANDARD_2026-09-06.md  
**Important:** **NO APPROVED PAPER MAINLINE YET.**

---

# 0. Executive decision

V11 does not preserve the V9 “final three.”

After data-first search, current active set is:

| rank | candidate | verdict |
|---:|---|---|
| 1 | **CK — Finite Mutual Knowledge vs Genuine Common Knowledge** | **CONTINUE / D2 / PILOT-ELIGIBLE ONLY** |
| 2 | **HOM — Non-bivalent Semantic Composition via Plural Homogeneity** | **CONTINUE / D2 / PILOT-ELIGIBLE ONLY** |

Removed:

- **AE — Actuality Entailment:** **KILL**. Strong scientific object, but no located reusable published human dataset directly crossing the decisive modality × aspect axis. The main experiment would still be D4 and gold-sensitive.
- **GRN — Goal-Relative Necessity / Anankastic Reasoning:** **KILL**. Natural-data version collides with existing event-step essentiality work; preserving the dynamic goal-binding novelty requires bespoke counterfactual worlds/action graphs and recreates the D4/D5 problem.

There is **no third active candidate**. Do not fill the slot for symmetry.

---

# 1. Calibration update: the data-first gate is now more important, not less

ACL 2026 Best Paper *The Imperfective Paradox in Large Language Models* is the right paper-identity anchor for formal-semantic behavioral discovery: an independently established linguistic object is probed in LLMs and the claimed contribution is a structural model-side law (“Teleological Bias”), not a benchmark score.

However, an August 2026 re-audit, *The Imperfective Paradox Is Not Necessarily in Large Language Models: A Benchmark Failure Before a Model Failure*, argues that much of the original benchmark admits alternative interpretations and reports substantial native-speaker disagreement on critical item groups.

This does **not** imply that controlled semantic diagnostics are illegitimate. It implies a stronger rule:

> If the model-side law depends on newly written gold-sensitive minimal pairs, benchmark validity becomes load-bearing scientific risk.

Therefore V11 strongly prefers CK and HOM because both can begin from human experimental materials that existed before our LLM hypothesis.

References:
- ACL 2026 Imperfective Paradox: https://aclanthology.org/2026.acl-long.689/
- August 2026 benchmark audit: https://arxiv.org/abs/2608.25005
- ACL 2026 Mind the (DH) Gap!: https://aclanthology.org/2026.acl-long.479/
- ACL 2026 CogToM: https://aclanthology.org/2026.acl-long.1448/
- ACL 2026 CoSToM: https://aclanthology.org/2026.acl-long.421/

---

# 2. Candidate Card — CK

## 2.1 Research Question

> **How do LLMs represent the qualitative boundary between finite mutual knowledge and genuine common knowledge?**

## 2.2 One-sentence version

> When everyone has only finitely nested knowledge, do models keep that state distinct from a genuinely public fact that licenses common knowledge without bound?

## 2.3 Paper Identity

**Scientific / behavioral cognitive discovery**, with a possible use-inspired coordination consequence.

Mechanism is optional for C1. It becomes useful only after a non-trivial behavioral law survives post-result novelty assassination.

## 2.4 Why the community should care

Common knowledge is not merely “deeper ToM.” It is the epistemic state that supports coordination, public commitments, shared plans, conventions, and group action. Finite mutual knowledge and common knowledge can license different actions even when lower-order beliefs look similar.

For LLM agents, the distinction matters whenever models must reason about what is merely mutually known versus what is publicly established.

## 2.5 One natural example

Two agents both privately learn the same fact and each learns that the other learned it. This can create reciprocal knowledge without genuine common knowledge. A public announcement heard by both instead licenses the recursive “everyone knows that everyone knows...” structure without requiring every finite level to be separately represented.

## 2.6 Scientific object

The independently established distinction:

**finite recursive / reciprocal knowledge ≠ common knowledge**

The object predates this project and is central in epistemic logic, coordination theory, pragmatics, and human social cognition.

## 2.7 Competing hypotheses

**H1 — Finite-recursion account.**  
Models represent only a bounded stack of nested beliefs. Performance declines with recursive depth; publicness adds no qualitatively different closure operation.

**H2 — Public-closure account.**  
Publicly salient events trigger a qualitatively distinct common-knowledge state, allowing depth-insensitive judgments that arbitrary recursive levels are licensed while finite reciprocal states remain finite.

**H3 — Finite-to-common overclosure.**  
Models incorrectly promote reciprocal or doubly reciprocal knowledge into common knowledge, especially when downstream coordination is required.

**H4 — Surface-public heuristic.**  
Models react to lexical/public cues without maintaining the epistemic structure. Apparent closure should then fail under matched non-public controls or transfer poorly to downstream use.

## 2.8 Prediction-changing axis

Existing generic higher-order ToM predicts behavior mainly as a function of recursive order and access to information.

CK predicts a **qualitative discontinuity**:

- finite reciprocal states remain bounded even when lower-order beliefs are all correct;
- genuinely public states can license arbitrary-depth common knowledge;
- the two states can therefore diverge on coordination/use even after matching low-order recognition.

## 2.9 Decisive test

Reuse the 2026 PNAS paradigms rather than inventing a world.

Primary test:
- Study 1 information conditions: **Asymmetrical / Reciprocal / Public**;
- recursive depths: 0, 2, 4, 6, plus the indirect arbitrary-depth judgment;
- estimate whether publicness changes only the level of confidence or changes the *shape* of recursion.

Replication/orthogonalization:
- Study 2: **Private / Reciprocal / Doubly Reciprocal / Public** with animated materials.

A decisive model-side law must separate:
1. finite-depth accuracy,
2. arbitrary-depth/common-knowledge attribution,
3. finite-state overclosure.

Only after this recognition test succeeds is a downstream coordination dissociation justified.

## 2.10 High-Level Calibration Set

1. **ACL 2026 Outstanding — Mind the (DH) Gap!**  
   Human-origin decision paradigm, matched humans, 20 LLMs, and a structural reasoning-vs-conversational regime split. This shows what turns cognitive transfer into a high-level behavioral discovery.

2. **ACL 2026 Main — CogToM**  
   46 human cognitive paradigms, 8,000+ bilingual instances, 49 human annotators. This is paradigm-first rather than hypothesis-first synthetic data.

3. **ACL 2026 Best Theme — CoSToM**  
   ToM with causal-oriented steering; useful to delimit paper identity and prevent CK from pretending every ToM result is novel.

4. **PNAS 2026 — Recursive mentalizing and public salience...**  
   Exact human scientific paradigm and primary D2 substrate.

## 2.11 Top-paper alignment

CK resembles strong behavioral-discovery papers only if the output is a structural law, not “accuracy on common-knowledge questions.”

The Main-level analogue is:
- old/independent human scientific object;
- clean competing accounts;
- human-calibrated substrate;
- qualitative model law or human-model divergence;
- downstream consequence only when it follows from C1.

## 2.12 Novelty assassination

Serious neighbors:

**OmniToM (2026).**  
OmniToM explicitly labels recursive belief order 0–3 and knowledge access as Private / Shared / Public. This is a direct threat to any generic framing about “higher-order ToM plus public information.”

**Common-ToM (ACL Findings 2024).**  
Natural spoken-dialog ToM grounded in common ground. This kills any claim that “common ground in natural dialogue is unstudied.”

**Grounding Gaps (NAACL 2024).**  
Shows LLM generations contain less conversational grounding and often presume common ground.

**LVLMs and Humans Ground Differently in Referential Communication (ACL 2026).**  
Directly studies common-ground formation in interactive referential communication and reports a human/model grounding gap.

**CoSToM / CogToM (ACL 2026).**  
Occupy broad ToM evaluation / representation territory.

Current surviving novelty is therefore narrow but real:

> **No located work makes the qualitative finite-mutual-vs-common-knowledge boundary itself the load-bearing LLM research question.**

This statement must be re-searched after any pilot law is observed.

References:
- OmniToM data card: https://huggingface.co/datasets/omnitom/omnitom-benchmark-review
- Common-ToM: https://aclanthology.org/2024.findings-acl.880/
- Grounding Gaps: https://aclanthology.org/2024.naacl-long.348/
- ACL 2026 referential grounding: https://aclanthology.org/2026.acl-long.410/

## 2.13 Closest papers

Closest scientific/data parent: PNAS 2026 human common-knowledge study.

Closest LLM benchmark parent: OmniToM.

Closest applied/common-ground parent: ACL 2026 referential grounding and NAACL 2024 Grounding Gaps.

Closest broad ToM parent: CogToM / CoSToM.

## 2.14 Parent abstraction

**How LLMs represent social-epistemic states needed for coordination.**

CK survives only because common knowledge is not reducible to “one more recursive depth.”

## 2.15 Reviewer compression sentence

> **“This is just another higher-order ToM / public-vs-private benchmark.”**

## 2.16 Why compression is / is not valid

It is valid if the experiment reports only accuracy by recursive depth or public/private condition.

It is not valid if the experiment demonstrates a prediction-changing boundary, e.g.:

> Models explicitly distinguish finite recursive knowledge from public information, yet systematically overclose reciprocal knowledge into common knowledge when making coordination judgments.

That is a qualitative dissociation, not a new ToM category.

## 2.17 Existing data

Primary:
- 2026 PNAS human Study 1 vignettes and response data;
- Study 2 animated videos and response data;
- survey response data released by the authors.

Potential second human-science substrate:
- 2016 bystander-effect common-knowledge experiments;
- 2019 common-knowledge / coordination work.

## 2.18 Data provenance tier

**D2** for the released PNAS human experimental materials.

The materials and human law existed before our LLM hypothesis.

## 2.19 Gold source

Gold is not authored by this project.

It comes from:
- formal distinction between finite mutual and common knowledge;
- experimentally manipulated information structure;
- published human judgments across recursive depths and publicness conditions.

## 2.20 Human validation requirement

No new human study is needed for the primary pilot if the original stimuli/interface are preserved.

If we alter modality, wording, or convert videos to text, the transformation itself must be validated or kept secondary.

## 2.21 Data construction risk

**Low for primary replication/adaptation.**

Risk rises sharply if we start inventing new Alice/Bob worlds. Do not do that for P0.

## 2.22 Artifact risk

Main artifacts to test:
- lexical cue “public” or equivalent wording;
- prompt-format response bias;
- sentence length / recursive depth confounded with token length;
- indirect arbitrary-depth question being easier than explicit recursive propositions.

Controls must preserve the PNAS manipulation while separating these.

## 2.23 Contamination risk

The exact 2026 PNAS materials are very recent: the article was published in August 2026 and its survey data were released with the paper. This makes direct training-data contamination less likely than for old benchmark materials, though not provably zero.

Use local/offline models without retrieval for cleanest evaluation and record model release/training cutoffs when known.

## 2.24 Second-substrate possibility

Strong.

Use an independently published common-knowledge consequence paradigm, preferably human coordination/bystander materials, only after C1 is established.

This provides external validity without constructing a bespoke coordination world.

## 2.25 Data Alignment Matrix

| field | CK | CogToM ACL 2026 | Mind the (DH) Gap! ACL 2026 | PNAS 2026 human anchor |
|---|---|---|---|---|
| data source | published human paradigm | 46 human cognition paradigms adapted into benchmark | established risky-choice paradigms + matched human experiment | newly published human experiments |
| pre-existing vs new | pre-existing before our LLM hypothesis | benchmark construction, paradigm-first | paradigm pre-exists paper | original human materials |
| human validation | published human responses | 49 annotators | matched human subjects | direct human participants |
| gold source | theory + human manipulations | human-cognition paradigms + annotation | normative/human reference points | experimental condition structure + judgments |
| scale | small controlled discovery first | 8k+ bilingual | 20 LLMs + human experiment | two studies |
| diversity | multiple scenarios + two modalities | 46 paradigms | multiple decision manipulations | narrative + animated studies |
| synthetic proportion | low adaptation if exact materials reused | substantial construction | controlled experiments | experimental stimuli |
| external validity | second human common-knowledge paradigm available | broad ToM coverage | human/model and regime comparison | replication across two studies |
| why burden is sufficient | qualitative boundary, not benchmark coverage | resource identity | broad behavioral law | direct scientific identification |

## 2.26 Outcome robustness

All of these teach us something:

- **finite recursion:** no qualitative common-knowledge state;
- **human-like public closure:** model mirrors a distinctive human compression strategy;
- **overclosure:** model-specific failure to preserve finite/common boundary;
- **underclosure:** public events fail to license common knowledge;
- **recognition/use dissociation:** correct epistemic classification does not govern coordination;
- **model-regime split:** post-training changes the qualitative representation/use regime.

## 2.27 What positive result would still be trivial?

- public condition accuracy is higher;
- shallower recursive questions are easier;
- models know the phrase “common knowledge”;
- a prompt explaining the theory improves performance;
- one model replicates the human mean pattern without a model-specific dissociation.

Any of these alone => **KILL as Main candidate**.

## 2.28 Main-scale growth path

C1: identify the finite/common structural law.

C2: show the law transfers across the two independent PNAS paradigms and/or an older independent human common-knowledge paradigm.

C3: if justified, show that epistemic recognition predicts or dissociates from coordination behavior.

C4 optional: explain a model-regime difference or mechanism only if C1–C3 demand it.

## 2.29 Claim architecture

A plausible Main claim architecture is:

**C1 — Qualitative epistemic boundary.**  
LLMs do / do not implement a distinct public-common-knowledge closure beyond finite recursion.

**C2 — Characteristic failure mode.**  
The dominant failure is overclosure, underclosure, or bounded-recursion collapse, not generic ToM error.

**C3 — Consequence / transfer.**  
The same boundary predicts behavior on independently published coordination-relevant materials.

No claim is pre-authorized before the pilot.

## 2.30 Pilot design

Minimum decisive pilot:
- exact PNAS Study 1 materials;
- only enough representative model regimes to determine the shape of the law, not a model zoo;
- published recursive-depth and information conditions;
- direct test of arbitrary-depth/common-knowledge judgment;
- no new synthetic worlds;
- no mechanisms.

Immediately after:
> **Models ...**

Write the strongest result sentence without numbers and assassinate that exact law.

## 2.31 Explicit kill criteria

KILL CK if:
1. strongest result is merely “public is easier”;
2. behavior is fully explained by recursive depth / token length;
3. OmniToM or another paper is found to already own the same finite-vs-common prediction;
4. no qualitative separation exists between reciprocal and public states;
5. the only interesting result requires newly invented coordination scenarios;
6. effect is prompt-fragile or disappears under the second published PNAS paradigm.

## 2.32 Final verdict

> **CONTINUE / RANK 1 / D2 / MINIMUM DECISIVE PILOT AUTHORIZED.**
>
> **NOT AN APPROVED MAINLINE.**

---

# 3. Candidate Card — HOM

Working label:

**HOM — Non-bivalent Semantic Composition via Plural Homogeneity**

Do not broaden this yet into a generic “semantic indeterminacy benchmark.”

## 3.1 Research Question

> **When natural-language semantics licenses a truth-value gap, do LLMs preserve “neither true nor false,” or collapse the sentence into ordinary binary truth conditions?**

Primary scientific substrate: plural homogeneity.

## 3.2 One-sentence version

> If only some members of a group satisfy a property, humans can judge both “the Xs are P” and “the Xs are not P” as non-true/non-false in a systematic way; do LLMs preserve that non-bivalent structure?

## 3.3 Paper Identity

**Scientific / behavioral linguistic discovery.**

The paper is not a plural benchmark and not a generic truth-probing paper. It tests whether a model’s semantic composition preserves a natural-language truth-value gap under controlled world knowledge.

## 3.4 Why the community should care

Modern LLM evaluation overwhelmingly forces propositions into binary true/false, entail/not-entail, correct/incorrect outputs.

Natural language semantics is not always bivalent. If models systematically collapse licensed indeterminacy into ordinary falsity or truth, that is a structural mismatch between fluent language modeling and semantic inference. It directly bears on NLI, verification, reasoning, and any downstream system that assumes model truth judgments correspond to linguistic truth conditions.

## 3.5 One natural example

Display four hearts: two red, two yellow.

- “The hearts are red.”
- “The hearts are not red.”

For plural homogeneity, the mixed scene is a **gap**: the positive and its negation need not behave as ordinary complements. Published human work finds characteristic non-bivalent judgments.

Contrast:
- “All the hearts are red.”

In the same mixed scene, the universal is simply false. That control is essential.

## 3.6 Scientific object

**Plural homogeneity / truth-value gaps in definite plural predication.**

This is a mature formal-semantic and experimental object, not a benchmark ontology invented for LLM evaluation.

## 3.7 Competing hypotheses

**H1 — Gap preservation.**  
Models maintain the non-bivalent structure: positive and negative definite plurals in mixed contexts behave differently from ordinary true/false controls, robustly across elicitation methods.

**H2 — Bivalent collapse.**  
Models remap homogeneity gaps into ordinary falsity / binary NLI decisions.

**H3 — Quantificational reinterpretation.**  
Models treat definite plurals as existential or universal quantifiers. Positive and negative judgments become polarity-asymmetric in the exact patterns predicted by those reinterpretations.

**H4 — Response-option compliance.**  
Models choose “neither” only when offered a ternary label, without representing the gap. This should fail the independent two-question diagnostic.

## 3.8 Prediction-changing axis

Existing LLM truth-probing work often uses “neither” for **epistemic unfamiliarity**: the model lacks enough evidence to classify a proposition as true or false.

HOM is different:

- the world is fully specified;
- the objects and predicate values are fully observable;
- “neither” arises from **linguistic semantic composition**, not missing knowledge.

Decisive case:
a fully specified mixed scene where a universal sentence is false but the definite-plural positive/negative pair exhibits a gap.

## 3.9 Decisive test

Reuse the published human paradigms.

At minimum:
1. definite plural × positive/negative;
2. homogeneous all/none scenes plus mixed gap scenes;
3. universal controls;
4. **Method A:** separately diagnose non-truth and non-falsity;
5. **Method B:** ternary true / false / neither-style judgment.

A genuine gap representation must survive both methods. Merely selecting a “neither” option is not sufficient evidence.

## 3.10 High-Level Calibration Set

1. **ACL 2026 Best — The Imperfective Paradox in Large Language Models**  
   Same paper identity: independently established formal-semantic phenomenon → controlled LLM diagnosis → seek a structural model law.

2. **TACL 2024 — Scope Ambiguities in Large Language Models**  
   Established semantic object + human judgments + direct tests of whether LLMs preserve multiple semantic readings.

3. **ACL 2026 Outstanding — Mind the (DH) Gap!**  
   Human behavioral paradigm becomes high-level because it discovers a robust model-regime law, not because the phenomenon is new in humans.

4. **Križ & Chemla 2015 / Tieu et al. 2019 human experiments**  
   Direct experimental methods and gold patterns for homogeneity/truth-value gaps.

## 3.11 Top-paper alignment

HOM is Main-shaped only if it yields a broad structural finding such as:

> **Bivalent Collapse:** models systematically erase linguistically licensed truth-value gaps even when world state is completely known, while remaining accurate on matched universal true/false controls.

That would be analogous in form—not content—to Teleological Bias.

“HOM accuracy is 63%” is not Main-shaped.

## 3.12 Novelty assassination

Exact searches performed across ACL Anthology / arXiv / web:
- “plural homogeneity” + LLM / large language model;
- “definite plural” + LLM + homogeneity;
- “truth-value gap(s)” + LLM + semantics.

No direct modern LLM paper was located whose load-bearing question is plural-homogeneity truth-value gaps.

Important neighboring collisions:

**TACL 2024 Scope Ambiguities.**  
Already studies whether LLMs preserve multiple readings. Therefore HOM cannot claim “LLMs and non-binary semantics are unstudied” in general.

**2026 presupposition papers.**  
Presupposition projection/conditional reasoning is now directly studied in LLMs. Therefore do not broaden HOM into a bag of presupposition + vagueness + ambiguity.

**The Trilemma of Truth in Large Language Models (2025).**  
Finds a third internal signal and classifies statements as true/false/neither, but its “neither” concerns model knowledge / unfamiliar factual statements rather than a linguistically licensed truth-value gap under fully specified evidence.

Surviving axis:

> **semantic indeterminacy under complete evidence vs ordinary bivalent truth conditions**

Use plural homogeneity as the primary independent D2 object. Do not claim a broad “all semantic indeterminacy” result before evidence exists.

References:
- Scope ambiguities: https://aclanthology.org/2024.tacl-1.41/
- Conditional presupposition study: https://aclanthology.org/2026.conll-main.26/
- Trilemma of Truth: https://arxiv.org/abs/2506.23921

## 3.13 Closest papers

Scientific parent:
- Križ & Chemla 2015, *Two methods to find truth-value gaps...*
- Tieu, Križ & Chemla 2019, *Children's Acquisition of Homogeneity...*
- 2025 experimental work on conjunction homogeneity / non-monotonic contexts.

LLM parent:
- TACL 2024 Scope Ambiguities.
- ACL 2026 Imperfective Paradox for paper identity.

## 3.14 Parent abstraction

**Does an LLM preserve the formal semantic structure licensed by natural language, rather than forcing every proposition into its default binary decision geometry?**

Do not elevate this abstraction to the paper title until a pilot establishes it.

## 3.15 Reviewer compression sentence

> **“This is just another formal-semantics benchmark, now for plurals.”**

## 3.16 Why compression is / is not valid

It is valid if the result is benchmark accuracy or isolated plural errors.

It is not valid if the model shows a stable **qualitative collapse law** that:
- is specific to gappy definite plurals;
- is absent on universal true/false controls;
- survives two independent human diagnostic methods;
- generalizes to a second published homogeneity substrate;
- differs systematically from human judgments.

## 3.17 Existing data

Primary D2 materials:
- Križ & Chemla 2015 experimental truth-value-gap diagnostics;
- Tieu, Križ & Chemla 2019 Experiments 1 and 2, with published full test sentences, visual scenes, positive/negative plural-definite targets, universal/existential controls, and human responses.

Additional second substrates:
- Serbian experimental homogeneity work;
- 2025 experiments on homogeneity in non-monotonic contexts;
- 2025 English conjunction-homogeneity experiments.

## 3.18 Data provenance tier

**D2.**

The experimental paradigms, stimuli structures, and human judgments existed years before this LLM hypothesis.

## 3.19 Gold source

Gold is grounded in:
- formal semantic predictions for homogeneity;
- published adult human judgments;
- experimentally controlled all / none / mixed scenes;
- matched universal and existential controls.

The project does not decide the labels after seeing model behavior.

## 3.20 Human validation requirement

For an exact-material pilot: none beyond faithfully preserving the published task.

If French items are translated into English or new lexical items are added, treat those as transformations and validate them separately. Prefer published English homogeneity materials as the second substrate rather than translating everything ourselves.

## 3.21 Data construction risk

**Low for the primary pilot.**

The 2019 paper supplies the full test-sentence set and visual paradigm. It explicitly includes controls for partial-truth, incomplete-description, and scope-ambiguity explanations.

Do not start by creating a 1,000-item templated benchmark.

## 3.22 Artifact risk

Key risks:
- models learn a response convention from the word “neither”;
- label-order bias;
- visual vs textual representation of the scene;
- negation bias;
- treating “the Xs” as universal/existential by default;
- memorized textbook examples.

Mitigation is built into the published paradigm:
- positive and negative targets;
- universal controls;
- independent binary/non-truth and ternary diagnostics;
- alternative-explanation controls.

## 3.23 Contamination risk

Higher than CK because the 2015/2019 materials are old and publicly available.

Therefore:
- do not treat item-level success as evidence of generalization;
- use multiple independently published homogeneity paradigms;
- preserve structural contrasts while avoiding explicit theory explanations in prompts;
- include a more recent independent English substrate where possible;
- interpret cross-item/cross-paradigm response geometry, not memorization-sensitive accuracy alone.

## 3.24 Second-substrate possibility

Strong.

Best route:
- primary: 2019 plural-definite visual paradigm;
- second: published English conjunction homogeneity or non-monotonic-context experiments.

This tests whether a discovered gap-preservation/collapse law is about the semantic phenomenon rather than one French stimulus set.

## 3.25 Data Alignment Matrix

| field | HOM | Imperfective Paradox ACL 2026 | Scope Ambiguities TACL 2024 | Tieu et al. 2019 |
|---|---|---|---|---|
| data source | published human homogeneity experiments | newly constructed diagnostic NLI | newly constructed semantic datasets + human judgments | human experiments |
| pre-existing vs new | pre-existing materials | new benchmark around old phenomenon | new benchmark around old phenomenon | original human materials |
| human validation | published adults + children | later benchmark audit raises gold concerns | explicit human judgments | 22/25 adult groups plus child samples |
| gold source | theory + human response pattern | linguistic analysis / benchmark labels | majority human reading preference | experimental conditions + human judgments |
| scale | small decisive pilot first | controlled diagnostic dataset | ~1,000 unique sentences | 24-trial / controlled experiments |
| diversity | polarity + determiners + multiple paradigms | semantic event classes | multiple scope-operator interactions | target + universal/existential/confound controls |
| synthetic proportion | adaptation of human stimuli | high controlled construction | high controlled construction | experimental visual stimuli |
| external validity | multiple published homogeneity paradigms | challenged by later audit | human-annotated diversity | two experiments/methods |
| why burden is sufficient | qualitative truth-geometry law | isolates aspectual inference | benchmark/semantic capability study | directly identifies gap response |

## 3.26 Outcome robustness

Informative outcomes include:

- **human-like gap preservation:** evidence LLMs capture non-bivalent composition;
- **bivalent collapse:** qualitative model-human divergence;
- **existential/universal reinterpretation:** identifies a specific alternative semantic computation;
- **method dissociation:** “neither” appears only when offered, exposing response-format mimicry;
- **recognition/use dissociation:** explicit metalinguistic knowledge without online semantic use;
- **regime split:** post-training/reasoning changes the semantic decision geometry.

## 3.27 What positive result would still be trivial?

- model says “neither” when the prompt explains homogeneity;
- model repeats a textbook definition;
- one model gets the six 2019 targets right;
- ternary prompting alone increases “neither” answers;
- a small gap-vs-control accuracy difference;
- pure human replication without a model-side law.

Any of these alone => **KILL as Main candidate**.

## 3.28 Main-scale growth path

C1: establish gap preservation vs bivalent collapse with two independent human diagnostics.

C2: distinguish collapse from existential/universal reinterpretation using polarity and quantifier controls.

C3: replicate the structural law on an independent published homogeneity paradigm.

C4 optional: connect semantic-gap behavior to internal truth representations or training regimes only if the behavioral law justifies it.

Do **not** preemptively add presupposition/vagueness/ambiguity datasets.

## 3.29 Claim architecture

Potential architecture, conditional on results:

**C1 — Non-bivalent semantic law.**  
Models preserve or collapse linguistically licensed truth-value gaps under complete evidence.

**C2 — Computational signature.**  
The error pattern is distinguishable from universal/existential reinterpretation and response-option compliance.

**C3 — External validity.**  
The same law holds across independent published homogeneity paradigms.

This is enough for a coherent scientific paper if C1 is strong; mechanism remains optional.

## 3.30 Pilot design

Minimum decisive pilot:
- exact or minimally adapted 2019 Experiment 2 materials;
- positive/negative definite plurals;
- all/none/gap scenes;
- universal/existential and confound controls;
- ternary judgment plus an independent Method-A style non-truth/non-falsity diagnosis;
- a small set of representative model regimes, selected to discriminate hypotheses rather than maximize model count;
- no new templated expansion.

Afterward write:
> **Models ...**

Then search that exact law before any scale-up.

## 3.31 Explicit kill criteria

KILL HOM if:
1. apparent gap behavior is entirely induced by providing a “neither” answer option;
2. Method A and Method B disagree qualitatively;
3. universal controls produce the same pattern;
4. behavior reduces cleanly to generic negation or quantifier errors;
5. no law survives a second published homogeneity substrate;
6. a recent paper is found already owning the same LLM truth-value-gap claim;
7. strongest sentence is only “LLMs struggle with plural homogeneity.”

## 3.32 Final verdict

> **CONTINUE / RANK 2 / D2 / MINIMUM DECISIVE PILOT AUTHORIZED.**
>
> **NOT AN APPROVED MAINLINE.**

---

# 4. AE — formal KILL

## 4.1 What survived

Actuality entailment remains a natural, mature linguistic object.

The 2025 *Annual Review of Linguistics* describes the classic interaction:
- imperfective ability modals can describe unrealized abilities;
- perfective counterparts can yield actuality entailments;
- the phenomenon remains theoretically active.

Reference:
https://www.annualreviews.org/content/journals/10.1146/annurev-linguistics-011724-121222

## 4.2 What failed

A systematic search did **not** locate a ready-to-reuse published LLM/NLP dataset or human experimental material set that directly crosses the decisive modality × aspect contrast with robust independent gold at the scale needed for our main evidence.

Published formal-semantic examples exist. Some experimental papers exist in neighboring actuality-entailment settings. But the envisioned direct PFV/IMPF lexical-event grid would still require us to:
- select/write items;
- control modal flavor;
- control lexical/event semantics;
- decide cross-linguistic comparability;
- obtain new native judgments;
- repair disagreements after seeing item behavior.

That is D4.

## 4.3 Why the 2026 benchmark audit matters

The August 2026 audit of the ACL Best imperfective benchmark demonstrates exactly how a strong linguistic object can still yield a fragile model-side claim if the benchmark’s entailment status is underspecified.

AE would begin with *more* gold complexity than the imperfective paradox because modality, aspect, context, and language interact.

## 4.4 Reviewer compression

> “This is another aspect/modality entailment diagnostic built from author-written minimal pairs.”

At present, data quality cannot rebut this.

## 4.5 Kill rule

> **KILL AE.**

No target-model compute. No hand-written 30–60-pair rescue.

Resurrection requires genuinely new evidence of a **published reusable PFV×IMPF actuality-entailment substrate with independent gold**, not merely more theoretical examples.

---

# 5. GRN — formal KILL

## 5.1 What data-first search found

Natural procedural data with independently grounded step importance do exist.

Ego4D Goal-Step, for example, contains real first-person procedural data and annotations such as essential / optional / irrelevant relative to a parent goal.

This initially looked like a route from D5 to D0/D1.

## 5.2 Why that route kills novelty

EMNLP 2023 *Are All Steps Equally Important? Benchmarking Essentiality Detection in Event Processes* already studies the core natural-data question:

> how essential is a step to the goal event?

It builds a human-annotated WikiHow corpus of goal-step pairs and evaluates models on whether steps are essential to achieving the goal.

Reference:
https://aclanthology.org/2023.emnlp-main.246/

Therefore the natural-data version of GRN compresses to an already-owned event-essentiality problem.

## 5.3 Why preserving novelty kills the data path

The proposed novel axis—goal active vs abandoned, alternative route added, “must Y” dynamically ceases to hold—requires counterfactual manipulation of the goal/action structure.

No independently grounded existing substrate was found that already contains those exact goal cancellation and alternative-route manipulations.

Reintroducing them via our own action graph means:
- we create the graph;
- create alternatives;
- create cancellation;
- create the utterance;
- define the necessity gold.

That returns to D4/D5.

## 5.4 Reviewer compression

Natural substrate version:
> “This is step essentiality / procedural reasoning.”

Novel synthetic version:
> “This is a bespoke action-graph benchmark for a distinction the authors designed.”

Neither survives.

## 5.5 Kill rule

> **KILL GRN.**

Summary:

> **Natural data → novelty dies.  
> Preserve novelty → data naturalness dies.**

Do not retain it as backup.

---

# 6. Screened but not active

These are **not backups**.

## 6.1 Generic semantic indeterminacy benchmark

Tempting abstraction:
> Do LLMs preserve non-bivalent/indeterminate meaning?

Not active because neighboring phenomena already have direct LLM literatures:
- scope ambiguity: TACL 2024;
- presupposition: multiple 2026 papers;
- vagueness/uncertainty: substantial adjacent work.

Bundling them now would look like a benchmark collection rather than one scientific discovery.

**Rule:** keep HOM narrow. Broaden only if a real post-pilot law motivates it.

## 6.2 Conditional perfection / QUD

Published 2025–2026 human work offers a D2 route, but pragmatic inference, alternatives, QUD, speaker knowledge, and scalar implicature are already crowded LLM objects.

Current reviewer compression:
> “another pragmatic-inference benchmark.”

**NOT ACTIVE.**

## 6.3 Counterfactual quantificational force

Published human experiments exist, but LLM counterfactual reasoning is extremely crowded. The surviving exact formal-semantic cell is not enough for Main-scale independence.

**NOT ACTIVE.**

## 6.4 Existential import / vacuous truth

Existing human work exists and the formal distinction is clean, but the current question appears smaller than HOM and overlaps presupposition / logic evaluation.

**NOT ACTIVE.**

---

# 7. Current forced ranking

## #1 CK

Best current combination of:
- natural high-level question;
- very recent independent D2 human materials;
- low data-construction burden;
- strong outcome robustness;
- plausible downstream consequence;
- surviving prediction-changing novelty.

Largest threat:
> generic higher-order ToM / common-ground compression.

Survival condition:
> a qualitative finite→common structural law.

## #2 HOM

Best new candidate found in V11.

Advantages:
- one-minute natural question;
- mature scientific object;
- D2 published human materials;
- independent gold;
- two diagnostic methods;
- built-in quantifier/polarity/confound controls;
- no located direct LLM plural-homogeneity paper.

Largest threat:
> “another formal-semantic benchmark.”

Survival condition:
> a broad, method-robust bivalent-collapse / non-bivalent-composition law, replicated on a second published substrate.

## No #3

Do not lower the bar.

---

# 8. Compute authorization

Allowed now:

### CK P0
Only a minimum decisive pilot on released PNAS materials.

### HOM P0
Only a minimum decisive pilot on published human homogeneity materials using both independent gap diagnostics and controls.

Not allowed:
- AE experiments;
- GRN experiments;
- broad model zoo;
- mechanism;
- SAE;
- patching;
- steering;
- LoRA/RL;
- 1,000-item synthetic expansion;
- adding new conditions after seeing weak effects.

---

# 9. Mandatory post-pilot gate

For each active candidate:

1. write the strongest result as one sentence beginning **“Models ...”** with no numbers;
2. search that exact law and its parent abstraction;
3. compare it to the high-level calibration set;
4. check whether it is a qualitative law or just benchmark performance;
5. KILL immediately if the strongest result is trivial, fragile, or already owned;
6. promote at most one paper mainline.

---

# 10. V11 one-sentence authority

> **There is still no approved mainline: only CK and HOM survive front-end audit, because both begin from independently published human scientific paradigms and can distinguish competing structural accounts without inventing a bespoke world; AE and GRN are killed because each fails the joint novelty × data-naturalness gate.**
