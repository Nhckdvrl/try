# Durable Research-Question Search — 2026-09-06 V7

**Purpose:** record the post-V6 literature assassination, kill obsolete search lanes, and
authorize only the smallest discovery pilots that currently survive the Promotion Standard.

**Paper mainline:** **NONE**.

**Current discovery-pilot priority:** **A > B > L**.

V7 supersedes V6 as the current durable-RQ search and verdict authority. V1–V6 remain
provenance and must not be deleted or rewritten.

---

# 0. Decision correction

V6 reopened Hamdi-style missing-axis search but still ranked IF / DM highly because the
new candidate search had not yet finished.

The subsequent conversation-level search has now moved beyond that ledger.

The correct current state is:

> **No approved paper mainline. Three new questions have survived enough conceptual and
> material scrutiny to justify tiny frozen discovery pilots: A, B, and L.**

They are not papers, and positive pilot results do not promote them automatically.
Each successful P0 must undergo a fresh post-result novelty assassination before any
mechanism work or expanded benchmark.

Historical CK / IF / DM assets remain provenance. They do not automatically refill a
slot if A/B/L fail.

---

# 1. Governing scientific pattern

The desired object is not an exact benchmark cell. It is a latent variable that changes
what an observed event means.

The strongest current search heuristic is:

```
matched observable behavior/statistics
but
different hidden generative cause
↓
future counterfactual / repair / weighting must diverge
```

This directly tests whether the model tracks surface regularities or the underlying
generative structure.

The three surviving candidates instantiate this in different domains:

- **A:** identical chosen-item sequence, different feasible sets → different preference evidence;
- **B:** identical public reports and report accuracy, different error stage → different repair;
- **L:** identical overall source accuracy and current confidence, different
  source-specific confidence semantics → different evidential weight.

---

# 2. Current verdict table

| candidate / lane | V7 verdict | direct reason |
|---|---|---|
| **A. Choice-set-conditioned preference evidence** | **SMALL PILOT** | LLM personalization work uses implicit behavior, but no located work isolates identical chosen histories whose preference implication reverses only because the feasible sets differ. |
| **B. Source competence × reporting fidelity** | **SMALL PILOT** | Source reliability/trust work is close, but no located receiver-LLM work matches public report accuracy while separating world→belief error from belief→report error and testing selective repair. |
| **L. Source-conditioned confidence semantics** | **SMALL PILOT** | Confidence weighting/calibration work is close, but no located work matches overall accuracy and current confidence while changing only the source-specific confidence→correctness mapping. |
| **C. Epistemic × deontic authority routing** | **KILL** | Remaining claim compresses to authority bias × instruction hierarchy; removing lexical authority cues requires manufactured legitimacy/scope institutions. |
| **D. Coverage-conditioned negative evidence** | **KILL — EXACT COVER** | CROWN-QA already fixes question/observed facts while varying query-relative completeness and tests negative-vs-unknown reasoning. |
| preference drift vs temporary/noisy behavior | **KILL — DIRECT COLLISION** | CAPTURE explicitly separates genuine preference drift from temporary context, ambiguity and poisoning with a latent user-state tracker and counterfactual audit. |
| preference uncertainty / same preference, different certainty | **KILL as replacement** | OPEN already brings Bayesian uncertainty and active elicitation to LM preference learning; personalized preference-distribution work further crowds the axis. |
| belief × preference from actions / inverse planning | **KILL** | Reviewer compression is ordinary inverse planning / action-and-motive inference on LLMs. |
| numerical identity × qualitative sameness | **HIGH-RISK / NO PILOT** | Dynamic entity tracking/rebinding is too close; explicit identity cues trivialize, implicit cues weaken direct gold. |
| sampling/selection mechanism × observed sample | **HIGH-RISK / NO PILOT** | Mature selection-bias / causal object; no LLM-specific law found that defeats the parent-computation compression. |
| descriptive × injunctive norms / preference × conformity | **KILL** | Too close to existing norm/conformity work and risks becoming human-phenomenon replication. |
| habitual × goal-directed control | **KILL** | Existing LLM cognitive-psychology work already uses classical sequential-decision paradigms for model-free/model-based distinctions. |

---

# 3. Candidate Card A — Choice-set-conditioned preference evidence

## 3.1 Research Question

> **When an LLM infers a user's preferences from observed choices, does it condition the
> evidential meaning of a choice on which alternatives were actually available?**

The scientific axis is:

```
latent preference
×
feasible choice set
→
observed choice
```

A chosen item is not preference evidence in isolation. Its evidential meaning depends on
what could have been chosen instead.

## 3.2 Why it matters

Long-running personalized assistants infer user state from behavioral traces. A system
that stores "chose tea" without conditioning on whether coffee was available can turn
forced or weakly informative actions into durable false preferences.

The contribution is not "constraints matter." The question is whether the model performs
the identification step required to infer preference from choice.

## 3.3 One example

Assume a person has a stable ranking and always chooses the most-preferred available item.

History 1:
- {Tea, Coffee} → Tea
- {Juice, Tea} → Juice
- {Coffee, Water} → Coffee

This implies Tea > Coffee.

History 2 has the **same selected sequence** Tea → Juice → Coffee:
- {Tea, Water} → Tea
- {Juice, Coffee} → Juice
- {Coffee, Tea} → Coffee

This implies Coffee > Tea.

The future choice set is {Tea, Coffee}. Correct predictions must reverse.

## 3.4 Literature-Axis Matrix

| prior work / area | axis varied | held fixed / entangled | coverage | missing load-bearing axis |
|---|---|---|---|---|
| Chen et al. 2026, **APOLLO / Towards Preference Following in Tool Calling Language Agents** | explicit vs implicit preferences in interaction history; preference-following in tool use | observed selection is treated as preference-bearing behavior; feasible-set identification is not isolated | behavior / benchmark / RL | identical selected history with opposite preference implication caused only by feasible sets |
| Shen et al. 2025, **MiCRo** | heterogeneous/personalized preference distributions and context-aware routing | preference data already encodes comparisons; not an identification test from constrained action traces | preference modeling | whether action is informative conditional on opportunity set |
| Handa et al. 2024, **OPEN / Bayesian Preference Elicitation** | uncertainty and active query selection | elicit preferences through designed questions | Bayesian elicitation | retrospective evidence value of naturally constrained choices |
| Tomlinson et al. 2021, **Choice Set Confounding in Discrete Choice** | assignment mechanism of choice sets | not an LLM receiver / memory computation | theory + empirical discrete choice | whether an LLM actually conditions user-state updating on the feasible set |
| discrete-choice context-effect literature | preferences can depend on the option set itself | context effect and identification can be entangled | behavioral choice modeling | distinguish "set changes preference" from "set changes what a fixed choice tells us about preference" |
| recommender / personalization memory work | interaction histories, clicks, selections | often stores/uses action traces as direct preference evidence | application behavior | causal identification from identical action traces under different opportunities |
| inverse-planning / theory-of-mind work | infer latent goals/preferences from actions | many tasks vary action and environment jointly | behavioral inference | matched action sequence with feasible-set-only reversal |

### Assassination result

The theoretical parent is old and real: preference inference from choices necessarily
depends on opportunities. That does **not** kill A.

The surviving LLM-specific axis is computational:

> Does the model update a latent user preference from an action trace by conditioning on
> the opportunity set, or does it overwrite memory from the chosen item itself?

No located LLM paper currently makes the decisive matched comparison the load-bearing
object.

## 3.5 Outcome Robustness

Scientifically distinct outcomes:

1. clean availability-conditioned updating;
2. systematic forced-choice overwrite;
3. partial conditioning with asymmetric leakage;
4. correct explicit reasoning but downstream preference memory ignores the set;
5. representation contains feasible-set information but preference readout does not;
6. strong family heterogeneity;
7. only lexical "unavailable/sold out" cues drive the effect — **kill**.

## 3.6 Minimal Discovery Substrate

Frozen separately in `P0_MATERIAL_AUDIT_2026-09-06_V1.md`.

Shape:
- 40 independent semantic skeletons;
- 4 shallow domains;
- paired histories;
- selected-item sequence exactly identical within pair;
- feasible alternatives swapped to imply opposite pairwise preference;
- future common two-item choice;
- deterministic gold from revealed-preference constraints;
- counterbalanced names, item order and answer side;
- 3 modern model families;
- no judge.

## 3.7 Adjacent Concepts

- implicit personalization;
- preference memory;
- revealed preference;
- inverse planning;
- choice-set confounding;
- context effects;
- constraint-aware planning.

## 3.8 Novelty Threat Map

**High:** APOLLO / implicit preference following; discrete-choice identification.

**Medium:** inverse planning and user modeling.

**Low as direct cover:** generic recommendation memory or preference classification.

The key defense is not an exact 2×2 gap. It is the matched-action identification law:
the same behavioral trace must update preference differently because its feasible set
changes the evidence.

## 3.9 Reviewer Kill Sentence

> **"This just shows that menu information matters when predicting preference."**

## 3.10 Is that compression valid?

It becomes valid if the result is merely:
- models can read unavailable options;
- explicit constraints improve prediction;
- menus with different words change outputs.

It is **not** the intended claim if identical choice sequences, with lexical structure
counterbalanced, produce the theoretically required opposite latent preference update and
that update predicts a later common choice.

## 3.11 Research-space width

Natural follow-ups around one object:
1. behavior: opportunity-conditioned updating;
2. representation: raw action memory vs inferred latent preference;
3. generalization: transfer across domains and novel item labels;
4. dissociation: explicit inference correct but persistent memory wrong, or vice versa;
5. causal mechanism: identify the writer that commits inferred preference to memory;
6. intervention: selectively prevent forced-choice evidence from overwriting preference.

## 3.12 What would be trivial?

- repeated tea choices predict tea;
- explicit "coffee was unavailable" changes an answer;
- longer history helps;
- the model can repeat the menu;
- a preference label is linearly decodable.

## 3.13 Data risks

- natural histories may imply only a partial order;
- lexical salience of one alternative may drive output;
- one domain may dominate;
- stable-transitive-preference assumption must be stated without turning the task into a
  puzzle about our invented rule;
- template variants are not independent units.

## 3.14 Pilot Kill Criteria

Kill A as a mainline candidate if:
- the paired reversal disappears under natural paraphrase / item relabeling;
- only explicit unavailable/sold-out wording creates the effect;
- fewer than two of three modern families show the same structural direction;
- held-out domains collapse to chosen-item copying;
- a newly found paper already establishes the matched feasible-set identification law;
- the strongest post-result statement reduces to "choice sets matter."

## 3.15 Growth Path

```
C1: feasible sets gate what observed choices count as preference evidence
→
C2: latent preference state dissociates from raw interaction memory / chosen-item trace
→
C3: a selective update mechanism controls what behavioral evidence is written into
    persistent preference state
```

## 3.16 Verdict

> **SMALL PILOT**

---

# 4. Candidate Card B — Source competence × reporting fidelity

## 4.1 Research Question

> **When an LLM learns about a source from past testimony, does it distinguish errors in
> forming a belief from errors in reporting that belief?**

Generative structure:

```
world truth
↓ competence / information quality
source belief
↓ reporting fidelity / sincerity
public report
```

The alternative is one scalar "source reliability" inferred only from report accuracy.

## 4.2 Why it matters

A receiver should respond differently to two equally accurate sources if their errors come
from different stages. Better information repairs the first source; truthful reporting
repairs the second.

This matters for multi-agent systems, RAG, tool agents, testimony, delegation and memory:
the correct intervention depends on the error generator, not only historical accuracy.

## 4.3 One example

Two analysts have the same public report sequence and the same 6/8 report accuracy.

Audit trail A shows that wrong reports occur when the analyst's instrument/private
observation is wrong, while the report faithfully matches that observation.

Audit trail B shows that the analyst observes the truth, but the wrong public reports are
generated when the report departs from the private observation.

Ask which upgrade prevents the recurrent errors:
- **perfect information / observation**, or
- **truthful reporting of the current belief**.

Correct intervention reverses across the matched pair.

## 4.4 Literature-Axis Matrix

| prior work / area | axis varied | held fixed / entangled | coverage | missing load-bearing axis |
|---|---|---|---|---|
| Hwang et al. 2025, **RA-RAG** | heterogeneous source reliability estimated across sources | reliability largely scalar at document/source level | source estimation + retrieval/aggregation | factorization of equal report reliability into distinct error generators |
| Zhou et al. 2026, **Epistemic Context Learning (ECL)** | historical peer reliability; trustworthy vs unreliable peer behavior | peer trustworthiness learned mainly from observed success/failure | multi-agent behavior | matched report accuracy with competence-stage vs report-stage decomposition |
| Song et al. 2026, **KAIROS** | historical peer impressions, reliability, social influence | source quality / rapport effects not matched by error generator | benchmark + mitigation | targeted repair predicted by latent source model |
| Cheng et al. 2026, **Accommodation and Epistemic Vigilance** | pragmatic factors including source reliability | competence and reporting fidelity not independently generated | receiver behavior | whether receiver learns which stage causes source error |
| Mammen et al. 2026, **Trust Me, I'm an Expert** | perceived expertise of endorsement source | expertise is a cue to credibility; sincerity/report policy not matched | behavior + mechanism + steering | equal-accuracy source types with selective causal repair |
| classic source-credibility / persuasion literature | expertise/competence and trustworthiness are separable dimensions | human persuasion setting; often explicit role/trait cues | human behavior | history-derived generative source model inside receiver LLM |
| deception / honesty evaluations | truthful vs deceptive reports | source knowledge/competence frequently controlled or assumed | behavior / generation | joint receiver inference over belief formation and reporting policy |
| multi-agent trust / weighted aggregation | peer reliability and confidence | typically scalar reliability or empirical success | system behavior | counterfactual repair under matched scalar reliability |

### Assassination result

The parent distinction competence vs trustworthiness is not novel. The possible novelty is
the receiver computation under a matched-observable design:

> identical report sequence + identical truth sequence + identical scalar report accuracy,
> but different hidden error stage → different optimal repair.

No located work currently establishes that counterfactual source-model factorization in
LLM receivers.

## 4.5 Outcome Robustness

1. clean factorization and targeted-repair crossover;
2. complete collapse to scalar report accuracy;
3. asymmetric factorization: competence tracked, reporting policy ignored;
4. reverse asymmetry;
5. explicit behavioral crossover but no shared representation;
6. representation separates source types but downstream repair choice ignores it;
7. only "honest/incompetent" lexical labels work — **kill**.

## 4.6 Minimal Discovery Substrate

- 32 independent paired source histories;
- 4 shallow domains;
- within pair: public report sequence, ground-truth sequence and total report accuracy all
  identical;
- only the audit trail locating the error stage changes;
- two targeted repairs;
- exact forced-choice gold;
- source names, side, truth labels and repair order counterbalanced;
- 3 modern model families;
- no judge.

## 4.7 Adjacent Concepts

- source credibility;
- expertise;
- trustworthiness;
- epistemic vigilance;
- deception/honesty;
- peer reliability;
- RAG source weighting;
- multi-agent trust.

## 4.8 Novelty Threat Map

**High:** ECL/KAIROS/RA-RAG and general source reliability.

**High parent-concept threat:** classic expertise × trustworthiness credibility theory.

**Medium:** authority bias, deception, sycophancy.

B survives only because the proposed law concerns error-generation structure under equal
observable reliability, not merely semantic separation of "competent" and "honest."

## 4.9 Reviewer Kill Sentence

> **"LLMs distinguish expertise from honesty, which source-credibility research has done
> for decades."**

## 4.10 Is that compression valid?

Yes if the experiment uses labels ("expert", "honest", "liar", "incompetent") or asks
trait classification.

No if the load-bearing result is a selective-repair crossover from matched public
behavior, learned only from audit history, where scalar reliability provably cannot solve
the pair.

## 4.11 Research-space width

1. behavior: factorized vs scalar source model;
2. generalization: transfer the learned source state across task domains;
3. dissociation: source identity/reliability vs competence/reporting factors;
4. representation: belief-formation and reporting-policy state;
5. causal use: intervene on one component and predict selective change;
6. practical consequence: choose information-quality vs reporting-policy repair.

## 4.12 What would be trivial?

- experts are trusted more;
- "honest" people are trusted more;
- higher historical accuracy increases trust;
- explicit liar labels flip a response;
- source reliability is decodable.

## 4.13 Data risks

- audit histories may sound artificial;
- exposing private observation too explicitly can reduce the task to symbolic bookkeeping;
- one repair may be linguistically more salient;
- history length can become the difficulty rather than the source model;
- source/error labels must not leak the answer.

## 4.14 Pilot Kill Criteria

Kill B if:
- scalar report accuracy predicts responses once wording is counterbalanced;
- the crossover disappears when trait words are removed;
- participants only solve histories with explicit "observation/report" terminology;
- less than two of three modern families show a stable interaction;
- domains differ because of world knowledge rather than source modeling;
- literature search finds an existing matched-accuracy targeted-repair receiver experiment;
- the result reduces to "LLMs distinguish expertise from honesty."

## 4.15 Growth Path

```
C1: receiver LLMs factor source errors by stage rather than only scalar reliability
→
C2: competence and reporting-policy states transfer / dissociate independently
→
C3: selective intervention on one source-state component predicts which repair changes
    downstream trust
```

## 4.16 Verdict

> **SMALL PILOT**

---

# 5. Candidate Card L — Source-conditioned confidence semantics

## 5.1 Research Question

> **Does an LLM interpret a source's confidence report through that source's learned
> calibration history, or treat the same numerical/verbal confidence as a universal
> scalar across sources?**

Scientific structure:

```
source identity/history
×
reported confidence
→
evidential meaning
```

## 5.2 Why it matters

"90% confident" is useful evidence only if the receiver knows what 90% means for that
source. Two agents can have equal overall accuracy and emit the same confidence value now
while that value has very different empirical meaning in their histories.

This is a durable object for multi-agent systems, human-AI collaboration and tool
orchestration: confidence communication only helps if receivers interpret confidence
conditionally, not as a context-free number.

## 5.3 One example

Both Source A and Source B were correct on the same six of eight historical questions.

Both used "90%" four times and "60%" four times.

But the confidence labels are assigned differently:
- A: 90% was correct 4/4; 60% was correct 2/4.
- B: 90% was correct 2/4; 60% was correct 4/4.

Overall accuracy is 6/8 for both.

On a new binary question A and B disagree, and **both report 90%**.

A receiver that learned source-conditioned confidence semantics should weight A's current
90% report more strongly, despite equal overall source accuracy and equal current
confidence.

## 5.4 Literature-Axis Matrix

| prior work / area | axis varied | held fixed / entangled | coverage | missing load-bearing axis |
|---|---|---|---|---|
| Zhou et al. 2026, **ECL** | historical peer reliability | reliable/unreliable peer histories differ in scalar performance | history-aware trust | same scalar reliability but different meaning of a confidence level |
| Song et al. 2026, **KAIROS** | peer reliability, self-confidence, rapport/social influence | calibration semantics are not isolated under matched reliability | social multi-agent behavior | source-specific confidence→correctness mapping |
| Zhu et al. 2026, **Demystifying Multi-Agent Debate** | explicit calibrated confidence communication and confidence-modulated updates | confidence is intended as calibrated evidence | theory + behavior | receiver learning that identical confidence values have different source-conditioned meanings |
| ACL 2026 **Confidence Estimation for LLMs in Multi-turn Interactions** | confidence estimation across turns | focuses on estimating model confidence | confidence measurement | cross-source semantics learned from history |
| Kumaran 2026, **Reported Confidence in LLMs Tracks Commitment More Than Correctness** | verbal confidence vs correctness / commitment | confidence is generated by the model itself | behavior + mechanism | receiver-side learning of another source's idiosyncratic confidence semantics |
| general confidence calibration literature | calibration of probability/confidence reports | calibrates a source/model globally or per setting | calibration | whether another LLM conditions interpretation on source identity/history |
| scalar trust / reliability aggregation | weight sources by historical performance/confidence | reliability and confidence value often enter as separate scalars | aggregation | interaction: source × confidence meaning after matching both marginals |

### Assassination result

The strongest threat is ECL plus confidence-weighted multi-agent reasoning. Those works
already show that historical peer performance and confidence can affect receiver behavior.

The missing axis is narrower but load-bearing:

> **hold overall source reliability fixed; hold current confidence fixed; change only
> the historical mapping from that confidence value to correctness.**

This changes the meaning of the current report without changing either scalar.

## 5.5 Outcome Robustness

1. source-conditioned confidence semantics;
2. universal-confidence scalar: 90% treated identically across sources;
3. receiver learns only source reliability and ignores conditional calibration;
4. asymmetric use: learns bad calibration but not good calibration;
5. explicit behavior correct, persistent source representation absent;
6. family-specific differences;
7. effect only appears when told "A is well calibrated" — **kill**.

## 5.6 Minimal Discovery Substrate

- 32 independent matched histories;
- 4 shallow domains;
- two sources with identical overall correctness pattern;
- equal frequency of confidence labels;
- confidence labels reassigned so only conditional calibration differs;
- current disagreement with identical current confidence;
- exact binary gold;
- names, sides, answer labels and confidence-label order counterbalanced;
- 3 modern model families;
- no judge.

## 5.7 Adjacent Concepts

- calibration;
- uncertainty communication;
- confidence weighting;
- peer reliability;
- trust learning;
- multi-agent debate;
- verbal confidence;
- epistemic context learning.

## 5.8 Novelty Threat Map

**Highest:** ECL and confidence-modulated MAD.

**Medium:** KAIROS / social trust.

**Conceptual threat:** source-specific calibration is statistically standard.

L survives only if the LLM question is about receiver-side semantics under matched
marginals, not about inventing a new calibration method.

## 5.9 Reviewer Kill Sentence

> **"This is just calibration: a receiver should trust confidence values that were better
> calibrated in the past."**

## 5.10 Is that compression valid?

The parent principle is indeed standard. Therefore L must not claim statistical novelty.

The possible scientific contribution is whether LLM receivers actually learn a
source-conditioned semantics for confidence, versus collapsing:
- source reliability, and
- current confidence

into independent global scalars.

The matched design makes these computational alternatives empirically separable.

## 5.11 Research-space width

1. behavior: source × confidence interaction under matched marginals;
2. generalization: transfer learned confidence semantics across task domains;
3. representation: source reliability vs calibration mapping;
4. dissociation: internal mapping present but social influence ignores it;
5. causal use: selectively alter source-conditioned confidence readout;
6. practical consequence: robust multi-agent weighting when peers use confidence
   idiosyncratically.

## 5.12 What would be trivial?

- higher confidence gets more weight;
- historically accurate sources get more weight;
- explicitly calibrated sources are trusted;
- confidence is decodable;
- confidence-weighted voting improves accuracy.

## 5.13 Data risks

- small empirical calibration tables may be treated as arithmetic puzzles;
- numeric confidence may cue normative Bayesian reasoning instead of learned semantics;
- current-answer content must not differ in plausibility;
- label frequencies must be exactly matched;
- "90%" vs "60%" may have strong pretrained priors;
- the source-specific mapping must survive paraphrases using verbal confidence bins.

## 5.14 Pilot Kill Criteria

Kill L if:
- current confidence alone dominates after history;
- overall source accuracy explains responses despite matched accuracy;
- the interaction disappears under confidence-label relabeling / verbal paraphrase;
- only explicit "well calibrated" descriptors produce the effect;
- fewer than two of three model families show stable conditional weighting;
- newly located work already performs matched-marginal source-specific calibration learning;
- the post-result claim reduces to "calibration matters."

## 5.15 Growth Path

```
C1: the evidential meaning of confidence is source-conditioned rather than universal
→
C2: source reliability and confidence semantics are behaviorally / representationally
    dissociable
→
C3: selective readout/intervention changes how a source's confidence influences
    downstream belief without changing generic trust
```

## 5.16 Verdict

> **SMALL PILOT**

---

# 6. Candidate C — Epistemic × deontic authority routing

## Research Question

> Does the model represent authority over what to believe separately from authority over
> what to do?

## Literature-Axis Matrix

| prior work / area | axis already covered | remaining compression |
|---|---|---|
| Mammen et al. 2026, **Trust Me, I'm an Expert** | expertise/authority changes acceptance of endorsements; mechanism is decodable and steerable | epistemic authority already has a direct mechanistic LLM treatment |
| Geng et al. 2026, **Control Illusion** | system/user instruction priority and societal authority/expertise/consensus effects on instruction behavior | deontic/instruction routing already directly interacts with social authority |
| instruction-hierarchy literature | conflicting instruction sources / priority | deontic channel is crowded |
| sycophancy / social-influence work | deference to user/peer/social cues | generic deference already has multiple behavioral formulations |
| KAIROS / peer-reliability work | trust and social influence from peer history | role/history-derived influence is not empty territory |

## Reviewer Kill Sentence

> **"This crosses authority bias with instruction hierarchy and asks whether the two
> effects share a representation."**

That compression is currently accurate enough to kill the mainline.

## Data failure

The cleanest natural examples rely on lexical/social roles such as:
- expert;
- scientist;
- manager;
- supervisor.

Removing those cues requires histories that establish:
- legitimate directive scope;
- epistemic expertise;
- institutional authority boundaries.

At that point the dataset begins to manufacture the legitimacy/scope institution needed
to define the question.

## Verdict

> **KILL — REVIEWER COMPRESSION + DATA FAILURE**

Do not revive by renaming "authority" as routing, deference type, mandate, legitimacy or
scope unless a genuinely different prediction/causal structure is found.

---

# 7. Direct kill ledger

## D — Coverage-conditioned negative evidence

> **KILL — EXACT COVER**

**Collision:** Min et al. 2026, *When Absence Is Evidence: Evaluating
Completeness-Sensitive Negative Reasoning in Large Language Models* / CROWN-QA.

CROWN-Synth fixes the question and observed facts while varying query-relative coverage
and directly tests when absence licenses a negative answer versus when the answer must
remain unknown. It also includes a real-document contrast set and multiple model families.

**Reviewer compression:** exact.

**Permanent note:**

> Renaming completeness as coverage, closure, negative-evidence gating, or evidential
> sufficiency does not create a new axis.

## Preference drift vs temporary/noisy behavior

> **KILL — DIRECT COLLISION**

**Collision:** CAPTURE (2026-09-02).

It explicitly separates genuine preference drift from temporary context shifts, ambiguity
and memory poisoning with a latent user-state formulation, clarification and counterfactual
audit.

Do not revive by swapping "drift" for update, persistence, authenticity or memory
stability.

## Preference uncertainty

> **KILL as replacement**

OPEN already treats preference uncertainty and active elicitation as a core object.
Mixture/distributional personalized-preference work further reduces the remaining space.
A new benchmark cell is not enough.

## Belief × preference from actions

> **KILL**

Without a sharper LLM-specific law, this is inverse planning / action-and-motive inference.

## Numerical identity × qualitative sameness

> **HIGH-RISK / NO PILOT**

Close to entity tracking/rebinding. Explicit identity facts make the distinction trivial;
removing them makes direct gold unstable.

## Sampling/selection mechanism × observed sample

> **HIGH-RISK / NO PILOT**

Selection mechanism is a mature statistical/causal object. No current LLM-specific
structural law defeats the reviewer compression.

## Descriptive × injunctive norms / preference × conformity

> **KILL**

Too close to existing norms and conformity work; high risk of replicating human
psychology without a new model computation.

## Habitual × goal-directed control

> **KILL**

Classical model-free/model-based sequential-decision paradigms have already been applied
to GPT/LLM behavior; no independent new axis currently survives.

---

# 8. Historical candidate policy

CK / IF / DM remain useful search provenance and may contain reusable materials or
conceptual lessons.

They are **not** default replacements for a killed A/B/L candidate.

- CK remains historically SMALL PILOT AUTHORIZED / NOT MAINLINE under V9.
- IF remains historical SERIOUS SEARCH LEAD / NO PILOT.
- DM remains historical SERIOUS SEARCH LEAD / NO PILOT.

V7 priority overrides their old ranking for current mainline reconstruction.

---

# 9. Pilot authorization

The only newly authorized experiments from V7 are the **frozen P0 discovery pilots for
A, B, and L**, subject to every material gate in
[P0_MATERIAL_AUDIT_2026-09-06_V1.md](P0_MATERIAL_AUDIT_2026-09-06_V1.md).

P0 explicitly does **not** authorize:
- SAE;
- activation patching;
- steering;
- LoRA / RL;
- huge benchmark expansion;
- 10-model scale sweeps;
- LLM judges;
- post-hoc condition additions.

P0 asks only:

> **Is there a stable, non-obvious structural law under a matched-observable design?**

If no, kill.

If yes, re-run novelty assassination before mechanism.

---

# 10. Literature references used in this V7 decision

- Chen et al. 2026, *Towards Preference Following in Tool Calling Language Agents*:
  https://aclanthology.org/2026.findings-acl.1676/
- Shen et al. 2025, *MiCRo: Mixture Modeling and Context-aware Routing for Personalized
  Preference Learning*: https://aclanthology.org/2025.emnlp-main.882/
- Handa et al. 2024, *Bayesian Preference Elicitation with Language Models / OPEN*:
  https://arxiv.org/abs/2403.05534
- Tomlinson et al. 2021, *Choice Set Confounding in Discrete Choice*:
  https://doi.org/10.1145/3447548.3467378
- Hwang et al. 2025, *Retrieval-Augmented Generation with Estimation of Source
  Reliability*: https://aclanthology.org/2025.emnlp-main.1738/
- Cheng et al. 2026, *Accommodation and Epistemic Vigilance*:
  https://aclanthology.org/2026.acl-long.736/
- Zhou et al. 2026, *Epistemic Context Learning*:
  https://arxiv.org/abs/2601.21742
- Song et al. 2026, *KAIROS / Measuring and Mitigating Rapport Bias...*:
  https://arxiv.org/abs/2508.18321
- Mammen et al. 2026, *Trust Me, I'm an Expert*:
  https://arxiv.org/abs/2601.13433
- Geng et al. 2026, *Control Illusion*:
  https://doi.org/10.1609/aaai.v40i36.40339
- Zhu et al. 2026, *Demystifying Multi-Agent Debate: The Role of Confidence and
  Diversity*: https://aclanthology.org/2026.findings-acl.1694/
- Kumaran 2026, *Reported Confidence in LLMs Tracks Commitment More Than Correctness*:
  https://arxiv.org/abs/2606.29490
- Min et al. 2026, *When Absence Is Evidence / CROWN-QA*:
  https://arxiv.org/abs/2608.04591
- Hossain et al. 2026, *CAPTURE*:
  https://arxiv.org/abs/2609.02265

---

# 11. Conference calibration

The target remains NAACL Main, calibrated to ACL / EMNLP / NAACL Main and especially
Best / Outstanding work.

The calibration lesson is not "add more experiments." Recent outstanding papers show
that a crisp object can carry the paper when:
- the distinction is scientifically legible;
- the decisive experiment truly isolates it;
- causal/mechanistic work explains the main law rather than decorating it.

Examples used as shape calibration include:
- EMNLP 2025 Outstanding *Mind the Value-Action Gap*;
- EMNLP 2025 Outstanding *MiCRo*;
- EMNLP 2025 Outstanding *Causal Interventions Reveal Shared Structure Across English
  Filler-Gap Constructions*.

The project therefore keeps P0 deliberately small.

---

# 12. Governing rule after V7

```
new scientific axis
→ matched-observable material audit
→ tiny frozen P0
→ actual law
→ post-result novelty assassination
→ only then representation / causal mechanism / intervention
```

> **No approved paper mainline.**
>
> **A/B/L are discovery pilots, not papers.**
>
> **KILL means record the collision and reason so the same idea cannot return under new
> terminology.**
