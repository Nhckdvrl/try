# Dataset redesign: from discovery suite to external causal validation

**Status: 2026-08-29**

This document changes the role of the current 144-item dataset. It does **not** invalidate the experiments already run. The current suite remains useful because its conditions are tightly matched and it has already supported falsification, controls, and causal interventions. What changes is what the suite is allowed to establish.

## Decision

The existing `frozen_v1` data are henceforth the **Controlled Discovery Suite (CDS-v1)**, not the primary evidence for a broad claim about real LLM decision making.

The next phase must build an **External Validation Suite (EVS-v1)** from independently authored human-experiment materials and naturally occurring corpora. No further broad mechanistic claim about “evidence gating in LLMs” should be made until the behavioral effect survives that external tier.

The reason is simple: mechanistic analysis is only as meaningful as the behavior whose mechanism it explains.

---

## 1. What is good about the current data

CDS-v1 has properties we should preserve:

- `Base / Admit-Pre / Admit-Post / Exclude-Pre / Exclude-Post` are deterministically compiled from the same latent item.
- Exclusion outcomes were not used to select the original frozen items.
- Rule and memory probes are separate calls.
- The critical information has measurable leverage under `Admit`.
- The suite permits exact counterfactual interventions and activation patching.
- It exposed an unexpected result rather than merely confirming the original hypothesis: the preregistered human-like Unring-the-Bell ordering reversed.

Those are strengths of an **experimental instrument**.

---

## 2. Why it is not enough as the main empirical dataset

### 2.1 Nominal item count overstates semantic independence

The 60 legal candidates are 10 newly written case skeletons crossed with six evidence types. The controlled families similarly reuse a small number of latent generators under multiple surface skins. The 144 surviving items therefore do not constitute 144 independent real-world situations.

Cluster bootstrap helps uncertainty estimation, but it cannot create external validity that the stimulus pool does not contain.

### 2.2 Most domains share one artificial discourse protocol

Across legal, ranking, inference, and other families, the compiler repeatedly presents blocks such as `BACKGROUND`, `RULING`, `ADDITIONAL INFORMATION`, and `TASK`, under a system instruction to follow the context exactly.

That is excellent for control. It is also a possible shared cause of the phenomenon. Eight ruling paraphrases rule out one sentence; they do **not** rule out the common interaction grammar.

### 2.3 Discovery and explanation repeatedly reuse the same substrate

Stage 2 through Stage 5 generated increasingly sharp hypotheses using the same small frozen semantic pool. This is legitimate exploratory mechanism work, but later significance tests on the same substrate should not be read as fresh independent confirmation of the broad phenomenon.

### 2.4 The current external checks already show heterogeneity

The Ramsey/Liu/Trueblood-style medication-report validation is almost perfectly handled by the tested models once the bad report is explicitly flagged. The Baron-Hershey/Aiyer outcome-bias anchor shows residue, but currently contains only four cells from one scenario.

This is not an inconvenience to hide. It is evidence that “known but disallowed information” is **not one homogeneous phenomenon**. The new dataset should be designed to discover the boundary conditions, not to force all tasks into one effect.

### 2.5 Agent Stage 4 is an interface generalization, not an independent data generalization

Moving the policy to `SYSTEM` and the document to `TOOL` is valuable. But the underlying content is still inherited from the same authored legal/inference items. It supports a deployment interpretation of the controlled failure; it is not yet an external replication.

---

## 3. Refined scientific object

The mother question remains:

> Can a model retain information while making a downstream decision that is causally invariant to that information when an explicit policy says the information is out of bounds?

Call the property **policy-conditioned causal non-use**.

This is deliberately different from literal forgetting. A successful model may be able to quote the excluded information perfectly. What should disappear is its **causal contribution to a specified decision**.

Do not claim that the phrase “noninterference” itself is novel. Contemporary agent-security work already uses formal information-flow and noninterference language. Our potential contribution is narrower: measuring **semantic decision influence**, separating declarative rule knowledge from causal use, and tracing the internal computation when the model violates that decision policy.

---

## 4. Replace the old ratio-first design with paired counterfactual sensitivity

REI was useful for CDS-v1, but Stage 3E exposed the weakness of ratio metrics when the leverage denominator changes. EVS-v1 should therefore make a **raw paired effect** the primary statistic.

Whenever the source material permits a matched pair of critical-information values `E+` and `E-`, use four primary conditions:

```text
ALLOW(E+)   A + E+ + policy permitting E
ALLOW(E-)   A + E- + policy permitting E
DENY(E+)    A + E+ + policy forbidding E
DENY(E-)    A + E- + policy forbidding E
```

Define:

```text
AllowedSensitivity   = Y[ALLOW(E+)] - Y[ALLOW(E-)]
ForbiddenSensitivity = Y[DENY(E+)]  - Y[DENY(E-)]
PolicySuppression    = AllowedSensitivity - ForbiddenSensitivity
```

The normative target is:

```text
AllowedSensitivity != 0
ForbiddenSensitivity ~= 0
```

A normalized leakage fraction may be reported secondarily:

```text
LeakageFraction = ForbiddenSensitivity / AllowedSensitivity
```

but **only** for pairs whose absolute `AllowedSensitivity` clears a frozen leverage threshold. Always report the raw effects beside it.

Why this is stronger than `Base -> Admit -> Exclude` alone:

1. it directly asks whether the decision changes when only forbidden content changes;
2. it does not require an excluded run to land exactly on one potentially noisy Base score;
3. it makes semantic non-use a causal invariance statement;
4. it naturally supports continuous outcomes, logits, probabilities, rankings, and calibrated human targets.

Keep a no-critical-information `Base` arm when it is scientifically meaningful, especially for comparison with CDS-v1 and for mechanism work.

---

## 5. Three evidence tiers

### Tier C — Controlled Discovery Suite (existing)

Purpose: isolate variables, falsify mechanisms, run patching/ablation, test repairs.

Contents:

- `frozen_v1` legal / numeric / ranking / inference / outcome items;
- routing and linear-weighting tasks;
- semantic-addressability and duplicate controls;
- agent role variants.

**Allowed claim:** a tightly controlled model behavior exists under these constructions.

**Not allowed claim:** the same failure is common in naturally occurring decisions.

### Tier E — Independently authored experimental materials (new primary tier)

The first EVS-v1 candidates are chosen because the underlying phenomena and stimuli predate this project.

#### E1. Inadmissible legal evidence

Priority source: Engel, Golder & Rahal (2026), *Who Is Afraid of the Pink Elephant?* Their 1,432-participant experiments contrast character evidence and illegal-wiretap evidence and test several debiasing interventions.

Use the authors' open materials if the redistribution terms permit it. Preserve the original wording and experimental unit. Do **not** manufacture 30 near-duplicate court cases and call them 30 independent replications.

Important boundary condition: their prior-conviction manipulation and wiretap manipulation do not behave identically in humans. Preserve that heterogeneity.

#### E2. Outcome bias / ex-ante evaluation

Priority source: Aiyer et al. (2023), a preregistered replication of Baron & Hershey with `N=692`, open materials/data/code at OSF `knjhu`.

The current repository uses only four cells from one bypass-surgery scenario. EVS-v1 should ingest the source materials with provenance and, if legally redistributable, include the full set available from the original/replication materials rather than proliferating our own analogues.

This is a strong **true-but-temporally-out-of-bounds** family: the outcome is true and remembered, but it should not determine the ex-ante quality of the decision.

#### E3. Curse-of-knowledge / privileged-state reasoning

Priority source: *The “curse of knowledge” when predicting others’ knowledge* (2022), with data/code on OSF `2ngbq` and 40 general-knowledge questions whose novice difficulty was independently measured on 100 participants.

This gives a useful independently grounded task:

- the model may know or be explicitly shown the correct answer;
- it must estimate what an uninformed novice would know;
- the answer-side fact is available to the model but outside the target person's information state;
- the target can be compared with measured novice accuracy rather than an LLM judge.

This family is especially valuable because it is neither a courtroom vignette nor a retraction task.

#### E4. Continued-influence / retraction materials as a contrast family

Open misinformation/retraction paradigms can supply the **false-or-invalid** side of the taxonomy. They should be a contrast, not the conceptual center, because belief correction is adjacent to ICF and continued-influence research rather than our strongest novelty boundary.

A recent human result is itself useful for the timing question: Buczel et al. (2024, `N=337`) found forewarnings reduced misinformation reliance whereas post-warnings did not. That ordering is the opposite of the CDS-v1 prospective-nullification gap. EVS-v1 should therefore treat timing as an empirical moderator, not as a universal law.

#### E5. Forbidden information in employee selection

Oien & Goernert (2003) directly studied applicants containing “forbidden” versus job-relevant information, including a condition where the forbidden categories were announced before applications were reviewed. This is conceptually excellent for prospective non-use.

However, the article is not obviously open for stimulus redistribution. Use it only if the original materials can be obtained under terms that allow our intended use. **Do not reconstruct the copyrighted stimulus from the paper merely to increase dataset size.**

### Tier N — Naturally occurring corpus-derived decisions (secondary validation)

After Tier E is working, add real documents where we inject only the minimum policy manipulation. Candidate areas include:

- evaluation from real reports/reviews with metadata that is available to the model but outside the allowed decision basis;
- real multi-document agent/tool traces where provenance determines admissibility;
- decision records with genuine post-outcome information for an ex-ante evaluation.

Rules for Tier N:

1. source text must be independently authored;
2. policy injection must be minimal and auditable;
3. target/score must not require an LLM judge if a deterministic or human-grounded target exists;
4. never inflate sample size by surface paraphrase and then treat paraphrases as independent items;
5. cluster by original document/event/person, not by rendered prompt.

---

## 6. What NOT to do next

Do not respond to the current validity problem by simply writing 20 more legal skeletons or 100 more vendor/apartment skins.

Do not choose external items because they already show leakage on Qwen3-8B.

Do not use an LLM to generate “naturalistic” cases and then present them as external evidence.

Do not run another large patching campaign before an external behavioral family reproduces the effect.

Do not make “noninterference” the novelty claim; security papers such as Fides and AgentSecBench already occupy that language.

Do not hide negative external replications. Ramsey-like success is a boundary condition we need to explain.

---

## 7. EVS-v1 acceptance rules

A source family can enter the **primary external tier** only if all of the following are recorded before deny-condition results are inspected:

1. **Provenance:** paper/DOI/repository/OSF link and exact source file.
2. **Reuse status:** license or a conservative note that redistribution is not permitted/unclear.
3. **Independent unit:** what counts as one semantic experimental unit.
4. **Normative exclusion basis:** why E should not affect Y; not merely “we told the model to ignore it.”
5. **Leverage basis:** published human effect, deterministic verifier, or an `ALLOW`-only pilot whose rule is frozen before any `DENY` run.
6. **Outcome:** deterministic target, human-grounded target, or parseable model decision. No LLM judge in the primary analysis.
7. **Counterfactual pair:** if an `E+/E-` edit is introduced by us, document exactly what was changed and why the pair remains natural.
8. **Cluster ID:** original source unit used for bootstrap/mixed-effects inference.

Every imported source gets a manifest entry and a content hash.

---

## 8. Screening and freeze policy

EVS-v1 is meant to be harder to overfit than G0.

### Preferred: no target-model screening

For published experimental manipulations with a documented human effect, include all legally reusable source units and report them all.

### If leverage screening is unavoidable

Use only `ALLOW` arms and/or an independent verifier. Never inspect `DENY` outcomes during selection.

Freeze:

- source files and hashes;
- transformation scripts;
- cluster IDs;
- condition compiler;
- output readout;
- leverage thresholds;
- primary models;
- primary statistics.

Then run `DENY` for the first time.

---

## 9. Readout audit

CDS-v1 showed that an immediate one-token score can disagree with the model's own short reasoning, while a coarse 0–100 greedy integer can quantize badly. That lesson remains useful, but the two-sentence rationale readout can itself alter the phenomenon.

For EVS-v1, preregister two readouts on a small allow-only calibration set:

1. **Primary natural response:** the shortest format native to the task (number, choice, probability, ranking).
2. **Secondary fixed-position readout:** when open models permit logit access, a fixed-position probabilistic readout without an LLM judge.

If a rationale is required for stable behavior, treat “reasoning before answer” as an experimental factor, not invisible measurement plumbing.

---

## 10. Main hypotheses for G1

The broad question should be tested before the prospective-nullification mechanism.

### G1-H1: Policy knowledge

The model correctly identifies whether the critical information is permitted for the target decision.

### G1-H2: Retention

Under deny conditions, the model can still recall/recognize the critical information. This distinguishes causal non-use from deletion/forgetting.

### G1-H3: Forbidden sensitivity

Within at least some independently authored **true-but-disallowed** families, changing forbidden information changes the decision even when the policy is understood:

```text
ForbiddenSensitivity != 0
```

### G1-H4: Selectivity

The same critical-information manipulation has a substantially larger effect when it is allowed than when it is denied:

```text
|AllowedSensitivity| > |ForbiddenSensitivity|
```

This tests whether the policy does anything, rather than merely whether it is imperfect.

### G1-H5: Reason heterogeneity

True-but-disallowed, false/retracted, temporal, and access/procedural exclusions need not produce the same leakage. This is a planned moderator, not a nuisance.

### Secondary: timing

Pre vs Post is retained as a diagnostic factor. No universal direction is preregistered for EVS-v1 because existing human paradigms and CDS-v1 already suggest that the sign depends on the task.

---

## 11. Stop/go gates

After EVS-v1, choose the paper honestly.

### Gate A — broad effect survives

If at least **two independent true-but-disallowed source families** show reliable forbidden sensitivity with high rule knowledge and retained memory, proceed with the broad semantic non-use paper. Then replicate mechanism on at least two external families before generalizing the CDS-v1 patching story.

### Gate B — only one natural phenomenon survives

If leakage is concentrated in outcome bias, perspective/privileged knowledge, or one legal manipulation, narrow the paper to that phenomenon. Do not average heterogeneous zeros and effects into “general gating failure.”

### Gate C — only the controlled prospective bug survives

Then the scientific object becomes the **prospective nullification gap for future-target policies**, not generic known-information non-use. Its validation target should be realistic agent/tool policies over independently sourced documents.

### Gate D — external suite is clean

If strong models succeed on the external materials and only the authored CDS-v1 prompts fail, stop the broad interpretability project. The controlled result may remain a useful diagnostic note, but it should not be mechanistically overinterpreted as a general LLM defect.

---

## 12. Immediate execution order

1. **Freeze the current repository as discovery history.** Do not rewrite old result files to make the story cleaner.
2. **Acquire source materials and licenses** for Engel 2026, Aiyer/Baron-Hershey, OSF `2ngbq`, and one open CIE source.
3. Store a source manifest before importing content.
4. Write source-specific importers that preserve original units and generate minimal policy/counterfactual variants.
5. Hand-audit every transformed external item for semantic validity.
6. Freeze `EVS-v1` and `PREREGISTRATION_G1.md` before any deny run.
7. Run a small model panel first for behavior only.
8. Only if Gate A/B/C says the phenomenon is real, return to mechanism.

The key change is methodological, not cosmetic:

> **We stop asking the current synthetic suite to prove that the phenomenon is natural. We use natural, independently authored data to establish the phenomenon, and use the synthetic suite only for the causal experiments it is actually good at.**
