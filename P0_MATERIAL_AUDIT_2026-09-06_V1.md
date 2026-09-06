# P0 Material Audit — 2026-09-06 V1

**Scope:** pre-generation material audit and exact discovery-pilot freeze for the three
V7 survivors:

- A — Choice-set-conditioned preference evidence;
- B — Source competence × reporting fidelity;
- L — Source-conditioned confidence semantics.

**Paper mainline:** **NONE**.

**Purpose of P0:** discover whether there is a stable, non-obvious structural law. P0 is
not a mechanism study and is not a benchmark expansion.

---

# 0. Shared P0 rules

All three pilots use the same discipline.

## 0.1 Independent unit

The independent statistical unit is the **semantic skeleton / matched history pair**.

Not independent:
- paraphrases;
- name swaps;
- item-order swaps;
- answer-position swaps;
- prompt-format variants.

Those are audit variants only.

## 0.2 Model breadth

Use exactly three genuinely different modern families for the discovery pass:

1. Qwen family;
2. Gemma family;
3. Mistral family.

Use one reasonably capable current instruction model per family. Do not run a scale zoo.

Closed models may be used later as external validation, but are not required for P0.

## 0.3 Output

Prefer forced-choice / exact token output.

No LLM judge.

No chain-of-thought grading.

Record:
- raw answer;
- parsed exact answer;
- invalid-format flag.

## 0.4 Counterbalancing

For every skeleton:
- source/person names counterbalanced;
- target item/source side counterbalanced;
- answer order counterbalanced;
- superficial label assignment counterbalanced;
- no semantic item is systematically associated with the correct side.

## 0.5 Freeze policy

Before target generation:
- manually inspect every skeleton;
- run deterministic structural validators;
- freeze the JSON/JSONL;
- record hash;
- do not modify failing examples after seeing target-model outputs.

Any material failure discovered after output invalidates that skeleton from confirmatory P0;
it may be repaired only in a new version.

---

# 1. Operational P1–P12 gates

This document uses the Promotion Standard plus two operational gates needed for freezing.

## P1 — One-minute intelligibility

Can a technical reader understand the distinction and one example immediately?

## P2 — Independent scientific axis

Is the variable scientifically meaningful beyond our terminology?

## P3 — Outcome robustness

Would at least three qualitatively different outcomes remain informative?

## P4 — Research-space width

Are there at least three natural follow-up axes around the same object?

## P5 — Literature survival

Has the load-bearing C1/C2 survived conceptual assassination?

## P6 — Simple natural substrate

Can the question be instantiated in 1–5 sentences without invented ontology?

## P7 — Non-triviality

Would a positive result teach more than the direct semantics of the manipulation?

## P8 — Direct gold / measurement integrity

Is the expected answer deterministic under the stated assumptions?

## P9 — Believable independent data

Are skeletons semantically independent rather than template pseudo-replication?

## P10 — Reviewer compression

Can the strongest reviewer kill sentence be answered by the decisive design itself?

## P11 — Explicit kill criteria

Is it clear what empirical outcome kills or demotes the candidate?

## P12 — Discovery openness

Does the pilot distinguish multiple possible laws rather than confirm only one favorite
hypothesis?

All P1–P12 must pass before target output.

---

# 2. A — Choice-set-conditioned preference evidence

## 2.1 Core material principle

Within each pair:
- the selected-item sequence is identical;
- the number of choice events is identical;
- wording structure is matched;
- only the available alternatives change;
- the feasible sets imply opposite pairwise rankings for the future target pair.

The model is told only a minimal natural assumption:

> The person has a stable preference ranking and, each time, chooses the option they most
> prefer among those available.

This makes the gold deterministic without directly stating the target relation.

## 2.2 Exact P0 size

- **40 independent skeletons**
- **4 domains × 10 skeletons**
- each skeleton has **2 matched histories**
- each history has **3 choice events**
- each skeleton ends with the same future two-option choice

Total target decisions per model:
- 40 × 2 = **80** primary decisions.

Audit-only paraphrases do not count as independent observations.

## 2.3 Domains

Use shallow ordinary domains:
1. drinks / snacks;
2. commute / route options;
3. leisure / activity options;
4. everyday service / shopping options.

Avoid:
- moral choices;
- health decisions;
- high-stakes finance;
- domain knowledge where one item has obvious normative superiority.

## 2.4 Structural template

Let target pair be X vs Y.

History arm H_X:
- event 1 yields X > Y directly or via a short transitive chain;
- chosen sequence = c1, c2, c3.

History arm H_Y:
- exact same chosen sequence c1, c2, c3;
- alternative sets instead imply Y > X.

Every skeleton must pass a symbolic partial-order validator:
- no cycles;
- target relation uniquely determined;
- no extra assumption beyond stable transitive ranking.

## 2.5 Example skeletons

### A1 — Drinks

Assumption: Nora always picks her most-preferred available drink.

H1:
- Tea vs Coffee → Tea
- Juice vs Tea → Juice
- Coffee vs Water → Coffee

Gold future {Tea, Coffee}: **Tea**

H2, same chosen sequence Tea → Juice → Coffee:
- Tea vs Water → Tea
- Juice vs Coffee → Juice
- Coffee vs Tea → Coffee

Gold future {Tea, Coffee}: **Coffee**

Audit:
- naturalness: PASS;
- deterministic gold: PASS;
- observable chosen sequence matched: PASS;
- no unavailable/sold-out lexical cue: PASS.

### A2 — Snacks

H1:
- Crackers vs Cookies → Crackers
- Fruit vs Crackers → Fruit
- Cookies vs Nuts → Cookies

Gold {Crackers, Cookies}: **Crackers**

H2, same selected sequence:
- Crackers vs Nuts → Crackers
- Fruit vs Cookies → Fruit
- Cookies vs Crackers → Cookies

Gold: **Cookies**

### A3 — Commute

H1:
- Bus vs Tram → Bus
- Bike vs Bus → Bike
- Tram vs Walk → Tram

Gold {Bus, Tram}: **Bus**

H2:
- Bus vs Walk → Bus
- Bike vs Tram → Bike
- Tram vs Bus → Tram

Gold: **Tram**

### A4 — Leisure

H1:
- Museum vs Cinema → Museum
- Park vs Museum → Park
- Cinema vs Cafe → Cinema

Gold {Museum, Cinema}: **Museum**

H2:
- Museum vs Cafe → Museum
- Park vs Cinema → Park
- Cinema vs Museum → Cinema

Gold: **Cinema**

### A5 — Shopping

H1:
- Notebook vs Pen Set → Notebook
- Mug vs Notebook → Mug
- Pen Set vs Tote Bag → Pen Set

Gold {Notebook, Pen Set}: **Notebook**

H2:
- Notebook vs Tote Bag → Notebook
- Mug vs Pen Set → Mug
- Pen Set vs Notebook → Pen Set

Gold: **Pen Set**

### A6 — Breakfast

H1:
- Toast vs Cereal → Toast
- Yogurt vs Toast → Yogurt
- Cereal vs Oatmeal → Cereal

Gold {Toast, Cereal}: **Toast**

H2:
- Toast vs Oatmeal → Toast
- Yogurt vs Cereal → Yogurt
- Cereal vs Toast → Cereal

Gold: **Cereal**

### A7 — Local transport

H1:
- Subway vs Bus → Subway
- Bicycle vs Subway → Bicycle
- Bus vs Walk → Bus

Gold {Subway, Bus}: **Subway**

H2:
- Subway vs Walk → Subway
- Bicycle vs Bus → Bicycle
- Bus vs Subway → Bus

Gold: **Bus**

### A8 — Evening activity

H1:
- Reading vs TV → Reading
- Game vs Reading → Game
- TV vs Music → TV

Gold {Reading, TV}: **Reading**

H2:
- Reading vs Music → Reading
- Game vs TV → Game
- TV vs Reading → TV

Gold: **TV**

These are skeletons, not the final dataset. Final items must be manually varied so the 40
units are not mere noun substitution.

## 2.6 Lexical-shortcut audit

Mandatory checks:
- do not use "forced", "unavailable", "sold out", "only choice";
- target items appear equal numbers of times;
- target answer side is balanced;
- no target item is always the earlier/later selected item;
- final question wording identical across matched arms;
- item frequency matched within pair.

## 2.7 P1–P12 decision for A

- **P1 PASS** — one matched pair explains the question.
- **P2 PASS** — opportunity set changes the evidential meaning of action.
- **P3 PASS** — conditioned updating, overwrite, asymmetric leakage, and
  behavior/memory dissociation are all meaningful.
- **P4 PASS** — behavior, latent preference representation, memory writing,
  transfer and intervention are natural.
- **P5 PASS** — APOLLO/personalization and discrete-choice work are close, but no located
  LLM work isolates the matched chosen-history identification law.
- **P6 PASS** — three ordinary pairwise choices; no synthetic world.
- **P7 PASS** — success requires reversal under identical selected behavior, not merely
  reading a constraint word.
- **P8 PASS** — symbolic ranking validator gives direct gold.
- **P9 PASS CONDITIONALLY** — final 40 must be manually diverse, not noun-swapped copies.
- **P10 PASS** — reviewer compression "menu matters" is directly challenged by identical
  selected histories with opposite future predictions.
- **P11 PASS** — kill rules frozen below.
- **P12 PASS** — pilot can reveal correct conditioning, overwrite, partial conditioning,
  or model-family heterogeneity.

## 2.8 Primary estimand

Code each arm's answer relative to its exact gold.

Primary:
- **paired reversal success** = both matched arms correct.

Secondary descriptive contrast:
- probability of choosing target X in H_X minus H_Y after answer-side normalization.

Do not headline raw single-arm accuracy.

## 2.9 Statistics

For each model:
- report paired-reversal success over 40 skeletons;
- 95% bootstrap CI resampling skeletons;
- exact binomial interval for both-arm success;
- per-domain descriptive rates.

Cross-family claim requires:
- same qualitative direction in at least 2/3 families;
- no single domain contributes >50% of all successful reversals;
- no answer-side imbalance.

No prompt variant is a replicate.

## 2.10 Frozen kill criteria

**KILL / NO MAINLINE** if any:
1. effect disappears after natural wording audit;
2. performance is driven by one domain/template family;
3. models simply repeat latest chosen target regardless of feasible-set structure;
4. only explicit unavailability vocabulary creates the effect;
5. fewer than 2/3 families show stable above-chance paired reversals;
6. post-result novelty search finds direct prior cover;
7. strongest result sentence is only "choice sets matter."

---

# 3. B — Source competence × reporting fidelity

## 3.1 Core material principle

Within each matched pair:
- public report sequence identical;
- ground-truth sequence identical;
- total report accuracy identical;
- report positions/errors identical.

Only the **location of the causal error** differs.

Arm C (competence/information failure):
- source privately observes/believes the same wrong value they publicly report on error
  trials;
- reporting is faithful.

Arm R (reporting-fidelity failure):
- source privately observes/believes the correct value;
- public report departs from that belief on the same error trials.

The receiver gets a natural audit trail that reveals both the private observation and
public report after each historical case.

## 3.2 Exact P0 size

- **32 independent matched history pairs**
- **4 domains × 8 skeletons**
- **8 historical trials per source**
- report sequence and truth sequence fixed within pair
- same report accuracy, default target **6/8**
- one final intervention decision

Total target decisions per model:
- 32 × 2 = **64**.

## 3.3 Domains

Use simple low-knowledge monitoring/reporting contexts:
1. temperature / threshold readings;
2. inventory / count status;
3. visual inspection of simple binary state;
4. schedule / presence-status reporting.

Avoid:
- medical diagnosis;
- moral honesty framing;
- legal testimony;
- expert titles;
- adversarial spy stories.

## 3.4 Intervention question

Two interventions:
- **Improve information:** guarantee the source's private observation is correct.
- **Improve reporting fidelity:** guarantee the public report exactly matches the source's
  private belief/observation.

Ask:

> Which single intervention would remove the type of error this source repeatedly made?

Gold:
- competence/information arm → **Improve information**;
- reporting arm → **Improve reporting fidelity**.

Do not use "honest", "liar", "incompetent", "expert".

## 3.5 Example skeletons

### B1 — Temperature monitor

Historical truth/report pattern:
T, T, F, T, F, T, T, T
Public reports:
T, F, F, T, T, T, T, T
= 6/8 correct.

Arm C audit:
- on wrong trials, Dana's sensor display itself showed the wrong state;
- Dana reported exactly what the display showed every time.

Gold repair: **better information/sensor**.

Arm R audit:
- on every trial Dana's display matched the truth;
- on the two wrong public reports, Dana reported the opposite of the display.

Gold repair: **reporting fidelity**.

### B2 — Stock availability

Truth and public report sequences matched.
Arm C: shelf scanner is wrong on the two report errors; clerk relays scanner faithfully.
Arm R: scanner is right; clerk's public report diverges on those two positions.

Gold repairs reverse.

### B3 — Room occupied/free

Arm C: camera/private observation is wrong on error trials; report matches private read.
Arm R: private camera read is right; public report is wrong on same trials.

### B4 — Train on-time/delayed

Arm C: internal status feed is wrong on error trials; reporter faithfully relays it.
Arm R: feed is correct; reporter distorts same two reports.

### B5 — Package arrived/not arrived

Arm C: private tracking display wrong; public message faithful.
Arm R: private display correct; public message diverges.

### B6 — Light on/off inspection

Arm C: obstructed view yields wrong private observation; public report matches it.
Arm R: clear/correct private observation; public report differs.

### B7 — Seat available/unavailable

Arm C: private seat map is wrong on error trials.
Arm R: seat map is correct but public message differs.

### B8 — Device connected/disconnected

Arm C: internal indicator is wrong on error trials.
Arm R: internal indicator is right but public report changes it.

Final dataset must vary event structure and prose, not just nouns.

## 3.6 Naturalness audit

Pass only if:
- the "private observation" has a plausible trace/log;
- receiver access to the audit is natural (e.g. later audit record);
- no trait adjective names the source type;
- public behavior really is identical within pair;
- each intervention has symmetric wording length/complexity.

## 3.7 P1–P12 decision for B

- **P1 PASS** — same accuracy, different reason for error, different repair.
- **P2 PASS** — belief formation and reporting policy are independent stages in testimony.
- **P3 PASS** — factorized, scalar, asymmetric, represented-but-unused outcomes all matter.
- **P4 PASS** — behavior, transfer, representation, causal repair and intervention are natural.
- **P5 PASS** — source-reliability literature is crowded, but no located work fixes scalar
  report reliability while varying error stage and testing targeted repair.
- **P6 PASS CONDITIONALLY** — audit trail must remain short and ordinary.
- **P7 PASS** — no explicit honesty/competence labels; scalar reliability cannot solve the pair.
- **P8 PASS** — intervention gold follows directly from the generated causal history.
- **P9 PASS CONDITIONALLY** — 32 histories must be genuinely independent.
- **P10 PASS** — matched public behavior defeats "trust the more accurate source."
- **P11 PASS** — kill rules frozen.
- **P12 PASS** — scalar collapse, clean factorization and asymmetric factorization are all
  discoverable.

## 3.8 Primary estimand

Primary:
- **targeted-repair crossover accuracy** across matched error-generator pairs.

Equivalent interaction score:
- competence arm preference for information repair
minus
- reporting arm preference for information repair.

A perfect factorized receiver switches repair across the pair.

## 3.9 Statistics

Per model:
- matched-pair both-correct rate;
- bootstrap CI over 32 skeletons;
- repair-choice difference-in-differences;
- per-domain descriptive interaction.

Cross-family law:
- same crossover direction in at least 2/3 families;
- no domain-only effect;
- invalid-format rate reported.

## 3.10 Frozen kill criteria

**KILL / NO MAINLINE** if:
1. repair choice tracks wording rather than error stage;
2. removing honesty/competence adjectives removes the effect because those adjectives were
   doing the work;
3. histories are only solvable with explicit project ontology;
4. scalar public accuracy or latest error predicts responses;
5. fewer than 2/3 families show stable crossover;
6. one domain drives the interaction;
7. newly found work directly covers matched-accuracy targeted repair;
8. result compresses to "LLMs distinguish expertise from honesty."

---

# 4. L — Source-conditioned confidence semantics

## 4.1 Core material principle

Within each matched source pair:
- same eight historical questions;
- same correctness vector;
- same total accuracy;
- same count of each confidence label;
- same current confidence value;
- current answers conflict.

Only the **assignment of confidence labels to correct vs incorrect historical reports**
changes.

Thus:
- marginal source accuracy is matched;
- marginal confidence frequency is matched;
- current confidence is matched;
- only conditional mapping P(correct | confidence, source) differs.

## 4.2 Exact P0 size

- **32 independent history skeletons**
- **4 domains × 8 skeletons**
- **8 historical trials**
- two confidence bins in core P0: **90%** and **60%**
- each source uses each label 4 times
- each source is correct on the same 6/8 positions
- current disagreement; both sources say **90% confident**

Total target decisions per model:
- **32** primary conflict decisions.

A swapped-mapping counterbalance creates the matched opposite-gold arm, yielding 64 raw
decisions if both mappings are instantiated. Statistical unit remains 32 skeletons.

## 4.3 Canonical mapping

Correctness positions are identical for A and B:
- six correct, two incorrect.

Confidence allocation:

Source A:
- 90%: 4/4 correct
- 60%: 2/4 correct
- overall: 6/8

Source B:
- 90%: 2/4 correct
- 60%: 4/4 correct
- overall: 6/8

Current:
- A says answer X, 90%.
- B says answer Y, 90%.

Gold weighting: A's current 90% carries stronger historical evidence.

Matched opposite arm swaps the calibration mapping between names while preserving:
- current content;
- current confidence;
- total source accuracy;
- confidence frequencies.

Gold source reverses.

## 4.4 Domains

Use questions whose truth is explicitly revealed after each historical trial:
1. simple colored-symbol classification;
2. short factual lookup supplied in the prompt;
3. schedule/status binary facts;
4. simple arithmetic/comparison statements.

The receiver should not need external world knowledge to judge historical correctness.

Current conflict should also have prompt-provided direct gold structure, but P0 asks whom
to weight / which answer is better supported by source history, not whether the model
knows the external fact.

## 4.5 Example skeletons

### L1 — Weather-symbol forecaster

Eight past binary forecasts; truth is revealed after each.
A and B are correct on exactly the same six cases.

A's 90% labels occur on four correct cases.
B's 90% labels occur on two correct + two incorrect cases.

Both now disagree on the ninth case and both say 90%.

Gold: favor A.

### L2 — Inventory predictor

Same correctness positions and confidence frequencies.
Only conditional allocation differs.
Current 90% conflict.
Gold: source whose historical 90% reports were more reliable.

### L3 — Schedule checker

Historical claims about event present/absent.
Truth revealed.
Overall accuracy matched.
90%-conditional reliability differs.

### L4 — Arithmetic checker

Past judgments such as "37+18=55" with truth supplied after response.
Same correctness vector.
Confidence mapping differs.

### L5 — Sensor-status classifier

Binary connected/disconnected cases with revealed truth.

### L6 — Route delay classifier

Binary delayed/on-time judgments with revealed outcomes.

### L7 — Document lookup helper

Each historical item includes a short provided sentence; source reports yes/no and confidence.
Truth is explicit from the sentence.

### L8 — Shape-property helper

Simple prompt-defined facts; truth revealed after each.
No world knowledge.

## 4.6 Confidence-format audit

Core uses numeric 90/60 because exact conditional calibration is transparent.

Before target output, prepare audit-only paraphrases:
- "very confident" / "somewhat confident";
- "high confidence" / "moderate confidence".

If the law exists only for literal percentages and vanishes under a natural verbal mapping,
L is downgraded or killed.

Do **not** mix many confidence scales in P0.

## 4.7 P1–P12 decision for L

- **P1 PASS** — two equally accurate sources say 90%; one source's 90 historically means more.
- **P2 PASS** — source-conditioned semantics is distinct from source reliability and current confidence.
- **P3 PASS** — conditional semantics, universal scalar, reliability-only, and asymmetric learning all matter.
- **P4 PASS** — behavior, source representation, generalization, causal readout and agent aggregation follow naturally.
- **P5 PASS** — ECL/KAIROS/MAD confidence work is close, but no located work matches both
  marginal reliability and current confidence while varying only source-specific calibration.
- **P6 PASS** — eight short revealed-outcome trials; no invented ontology.
- **P7 PASS** — neither "trust the accurate source" nor "trust higher confidence" can solve the pair.
- **P8 PASS** — empirical conditional history gives exact ordering.
- **P9 PASS CONDITIONALLY** — final 32 skeletons require content diversity.
- **P10 PASS** — the decisive interaction survives only if source × confidence is learned.
- **P11 PASS** — kill rules frozen.
- **P12 PASS** — universal-scalar collapse is as scientifically interpretable as factorization.

## 4.8 Primary estimand

Primary:
- **source-conditioned confidence reversal** under mapping swap.

For each skeleton:
- mapping M1 makes A's current 90% more diagnostic;
- mapping M2 makes B's current 90% more diagnostic;
- current answers, current confidence and total source accuracy remain matched.

Pair success = model switches its evidential preference in the correct direction.

Do not headline raw trust in 90%.

## 4.9 Statistics

Per model:
- both-arm reversal success over 32 skeletons;
- 95% bootstrap CI over skeletons;
- conditional source-choice contrast under mapping swap;
- per-domain descriptive rates.

Cross-family claim requires:
- same interaction direction in at least 2/3 families;
- no numeric-position artifact;
- no source-name bias;
- verbal-confidence audit retains qualitative direction.

## 4.10 Frozen kill criteria

**KILL / NO MAINLINE** if:
1. model ignores history and treats equal current confidence identically;
2. model uses only overall accuracy;
3. mapping-swap reversal is unstable or driven by one content domain;
4. numeric confidence wording alone creates the effect and verbal paraphrase kills it;
5. explicit "well calibrated" labels are needed;
6. fewer than 2/3 families show stable conditional weighting;
7. a new paper already establishes matched-marginal source-specific confidence semantics;
8. result compresses to "calibration matters."

---

# 5. Shared material-generation checklist

Before any target model call, for each dataset:

- [ ] every skeleton manually read by a human;
- [ ] exact structural validator passes;
- [ ] target gold uniquely determined;
- [ ] no answer-side imbalance;
- [ ] no name-item association;
- [ ] no lexical condition label;
- [ ] pair observables verified matched by script;
- [ ] no duplicated semantic skeleton;
- [ ] domain counts balanced;
- [ ] final prompt is 1–5 sentences per event block and remains readable;
- [ ] no LLM-generated gold;
- [ ] no target model used during material repair;
- [ ] frozen file hash recorded.

---

# 6. Generation order

Run in current priority order:

1. **A**
2. **B**
3. **L**

Reason:
- A has the shallowest substrate and strongest directly matched behavior.
- B has the cleanest causal repair signature but slightly more audit complexity.
- L is conceptually clean but under the greatest "this is just calibration" pressure.

A failure does not automatically promote B/L to a paper.
A success does not stop B/L unless resources or updated literature justify stopping.

---

# 7. P0 stopping rule

P0 ends as soon as enough evidence exists to classify the candidate as one of:

- stable non-obvious structural law;
- trivial/lexical effect;
- model-family-specific curiosity;
- null/scalar-collapse result;
- material-design failure;
- direct literature collision discovered post-freeze.

Do not add new conditions to rescue a weak result.

---

# 8. After P0

If a candidate passes empirically:

1. write the law in one sentence without numbers;
2. run **post-result literature assassination** on that exact law;
3. verify cross-family reality;
4. only then design C2;
5. mechanism work is allowed only if it explains C1/C2 and predicts an intervention.

No SAE, patching or steering is authorized merely because a P0 effect is statistically
non-zero.

---

# 9. Current authorization

> **A-P0: FROZEN IN PRINCIPLE / MATERIAL BUILD AUTHORIZED**
>
> **B-P0: FROZEN IN PRINCIPLE / MATERIAL BUILD AUTHORIZED**
>
> **L-P0: FROZEN IN PRINCIPLE / MATERIAL BUILD AUTHORIZED**

"Frozen in principle" means the design, unit counts, estimands and kill rules are fixed by
this audit. The actual material files still require manual construction, deterministic
validation and hash freeze before target output.

> **No approved paper mainline.**
