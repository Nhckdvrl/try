# Data-First Research Question Audit — 2026-09-06 V10

**Target:** NAACL Main, calibrated against ACL / EMNLP / NAACL Main and especially Best / Outstanding work.  
**Status:** data-risk correction to V9.  
**Governing correction:** a natural scientific object is not sufficient. The evidence substrate must itself be natural, auditable, and externally defensible.

> **NO APPROVED PAPER MAINLINE YET.**
>
> V9 overestimated "data simplicity" for AE and GRN.
>
> Current data-first ranking:
>
> 1. **CK — Finite Mutual Knowledge vs Common Knowledge: CONTINUE**
> 2. **AE — Actuality Entailment: DATA-AT-RISK / NO TARGET RUN**
> 3. **GRN — Goal-Relative Necessity: DATA-AT-RISK / REPLACEMENT SEARCH**
>
> This ranking is not a paper-mainline approval.

---

# 1. The key correction: theory naturalness != data naturalness

A research object can be old, real, and theoretically important while the dataset used to probe LLMs is still artificial, fragile, or benchmark-local.

From now on, every candidate must separately pass:

1. **Object naturalness** — the scientific distinction exists independently of our benchmark.
2. **Substrate naturalness** — the examples/materials are not invented merely to make our variable observable.
3. **Gold naturalness** — labels come from theory, independent human judgments, task structure, or pre-existing annotations rather than our own interpretation.
4. **Coverage naturalness** — scale/diversity does not come from repeating one hand-written template.
5. **External validity** — the effect survives at least one second source, paradigm, domain, or naturally occurring substrate when the claim requires it.

The project rule is now:

> **The question may be deep; the data path must be shallow.**

A candidate whose core experiment requires building a complicated synthetic world is presumptively weak for a behavioral-discovery paper even when the world is logically clean.

---

# 2. Data provenance ladder

Use the strongest available tier.

## D0 — Existing dataset already measures the construct
Best case. Reuse with minimal transformation.

## D1 — Existing natural dataset, new annotation/readout only
The underlying instances are independently collected; our contribution is a new scientifically motivated label or analysis.

## D2 — Independently published human/linguistic experimental materials
Reuse established stimuli or paradigms with minimal adaptation. This is often excellent for cognition/semantics work because the material predates our LLM hypothesis.

## D3 — Natural-corpus retrieval + minimal controlled edits
Acceptable when the natural source remains primary and the intervention is local, auditable, and independently validated.

## D4 — New hand-written/template minimal pairs
High risk. Allowed only when:
- the scientific object is independently established;
- same-identity high-level papers justify controlled diagnostics;
- human/native-speaker validation is strong;
- lexical/template diversity is sufficient;
- conclusions are replicated on a second substrate.

## D5 — Custom synthetic world/ontology created to make the effect exist
Default **KILL** for behavioral/scientific-discovery work unless the synthetic formal system is itself the legitimate scientific object (e.g. formal reasoning).

---

# 3. What recent high-level papers actually imply

## ACL 2026 Best — Imperfective Paradox
The paper uses a template-based diagnostic dataset, ImperfectiveNLI. Therefore synthetic/controlled data are not automatically disqualifying.

But the important point is *why* this works:
- the semantic phenomenon is independently established;
- the contrast is shallow;
- the gold entailment relation is crisp;
- lexical classes are controlled;
- the paper discovers a broad model-side Teleological Bias rather than reporting benchmark accuracy.

Source:
- https://aclanthology.org/2026.acl-long.689/
- https://github.com/boleima/ImperfectiveParadox

## ACL 2026 Main — CogToM
CogToM contains >8,000 bilingual instances across 46 human-cognition paradigms and was validated by 49 human annotators.

This is construction-heavy, but it is **paradigm-first rather than hypothesis-first**: the benchmark inherits independently established human cognitive tasks instead of inventing a bespoke ontology for one desired effect.

Source:
- https://aclanthology.org/2026.acl-long.1448/
- https://github.com/Beijing-AISI/CogToM

## EMNLP 2025 Outstanding — Value-Action Gap
This paper creates a large new dataset, showing that "new data" can support Outstanding-level work. But its scale, broad cultural/topic coverage, explicit framework, and socially important external construct make it very different from a small custom probe.

Source:
- https://aclanthology.org/2025.emnlp-main.154/

**Conclusion:** "existing data only" is too strict as a universal rule, but "cheap bespoke synthetic data is fine" is also wrong. New data must earn its existence.

---

# 4. Re-audit of the V9 final three

# 4.1 CK — Finite Mutual Knowledge vs Common Knowledge

## Data status: strongest of the three

The 2026 PNAS paper *Recursive mentalizing and public salience in the perception of common knowledge* already provides exactly the human-side structure we need.

Study 1 manipulates:
- Asymmetrical information;
- Reciprocal information;
- Public information;
- recursive depths including 0, 2, 4, 6, and an indirect 18-level judgment.

Study 2 uses:
- Private;
- Reciprocal;
- Doubly Reciprocal;
- Public.

The paper explicitly states that data and code are available on GitHub and provides supplementary materials.

Source:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13486529/

This changes CK materially. We should **not invent a new CK world as P0**.

### Preferred substrate
1. Reuse the published PNAS 2026 human stimuli/materials as the primary discovery substrate.
2. Preserve the exact information manipulations as far as possible.
3. Compare LLM behavior with the published human pattern, but do **not** make "LLMs replicate humans" the contribution.
4. Add only the minimum LLM-specific readout needed to distinguish:
   - finite recursion;
   - public/common-knowledge compression;
   - finite-to-common overclosure;
   - recognition vs downstream coordination.
5. Use CogToM only as an independent ToM control/generalization source, not as evidence that CogToM already measures common knowledge.

### Data tier
**D2**, potentially approaching D0/D1 if the released materials expose the exact stimuli in reusable form.

### Remaining scientific risk
The main novelty threat is not data anymore. It is reviewer compression:

> "You reran a 2026 human common-knowledge experiment on LLMs."

Therefore CK survives only if the model result yields a non-human-trivial structural law, e.g.:
- publicness causes an abrupt closure regime distinct from recursion depth;
- models overclose finite reciprocal knowledge into common knowledge;
- correct epistemic classification fails to transfer to coordination;
- reasoning vs conversational training yields a systematic regime split.

### Verdict
**CONTINUE / RANK 1 UNDER DATA-FIRST AUDIT.**

---

# 4.2 AE — Actuality Entailment

## Data status: substantially weaker than V9 claimed

The formal-semantic object is unquestionably natural. A 2025 Annual Review surveys the active literature on the interaction of modality and aspect.

Source:
- https://www.annualreviews.org/content/journals/10.1146/annurev-linguistics-011724-121222

But no ready-made NLP dataset directly measuring **modality × aspect -> actuality inference** was located in the current search.

The obvious neighbor, ImperfectiveNLI, measures a different axis:
- progressive aspect × event class -> completion.

It is useful as a control and methodological precedent, not as the AE dataset.

### Current V9 plan problem
"30–60 independent lexical/event items + manually audited translations/native validation" is **D4**, not "high data simplicity."

The cross-linguistic nature makes the gold especially delicate:
- perfective/imperfective morphology differs across languages;
- modal flavor matters;
- English lexicalized forms such as "was able to" are not equivalent to overt aspect systems;
- acceptability and actuality inference may vary by verb/context.

### Only acceptable rescue path
Before any target-model run, attempt to move AE from D4 to D2/D3:

1. build an inventory of **published examples** from the AE literature;
2. identify languages with clear overt aspect diagnostics;
3. mine naturally occurring modal+aspect examples from existing corpora;
4. obtain native-speaker judgments for actuality/contradiction diagnostics;
5. use hand-written matched pairs only as a controlled secondary test.

If the core evidence still rests on newly written 30–60 examples whose gold depends on our own semantic judgment, **KILL**.

### Verdict
**DATA-AT-RISK / DEMOTED / NO TARGET-MODEL COMPUTE.**

---

# 4.3 GRN — Goal-Relative Necessity / Anankastic Reasoning

## Data status: weakest of the three

The linguistic object is real and active. The 2026 *Linguistics and Philosophy* paper confirms that anankastic conditionals remain a live formal-semantic problem.

Source:
- https://link.springer.com/article/10.1007/s10988-026-09459-x

However, the current search did **not** locate an existing NLP benchmark or natural annotated corpus that gives the crucial gold:
- which action is genuinely necessary for the goal;
- whether necessity disappears when the goal is dropped;
- whether it disappears when an alternative route is introduced.

The V9 proposal uses "shallow explicit action graphs / ordinary scenarios." That is scientifically clean but data-wise dangerous: the graph and the sentence are both authored to instantiate our hypothesis.

### Why natural instructional text alone does not solve it
Mining phrases such as "If you want X, you need to Y" from manuals/WikiHow/forums gives natural language, but not reliable gold that Y is logically/teleologically necessary. Real instructions often contain:
- recommendations;
- defaults;
- sufficient but unnecessary steps;
- conventions;
- hidden prerequisites;
- domain assumptions.

Thus a natural corpus can still have an unusable gold layer.

### Rescue requirement
GRN survives only if an existing procedural/agent dataset can provide independently grounded goal/action dependency structure **and** natural language whose modal interpretation can be evaluated without us manufacturing the ontology.

If no such substrate is found, prefer replacement over bespoke action-graph construction.

### Data tier
Currently **D4/D5 risk**.

### Verdict
**DATA-AT-RISK / REPLACEMENT SEARCH.**
Do not run models on newly invented graph scenarios merely because they are easy to generate.

---

# 5. New mandatory Data Gate before candidate promotion

Every candidate must now answer these before compute:

1. **What exact dataset/material already exists?**
2. **Who created it and for what original purpose?**
3. **Does the scientific object exist without our labels/templates?**
4. **What fraction of the final evidence is original vs transformed vs newly generated?**
5. **Where does gold come from?**
6. **Could reasonable humans disagree with gold?**
7. **What validation is required: expert, native speaker, crowd, deterministic structure?**
8. **Can a model solve the task through template artifacts?**
9. **Can train/pretraining contamination plausibly trivialize the result?**
10. **Is there a second independent substrate?**
11. **Would the paper still make sense if all dataset names were deleted?**
12. **Would the dataset still be useful/valid if our hypothesized effect were absent?**

A candidate that cannot answer 1–7 cleanly is not experiment-authorized.

---

# 6. Search policy from now on

RQ search should be **bidirectional**, not question-only:

### Old failure mode
interesting concept
-> invent benchmark
-> validate benchmark
-> discover data problems
-> narrow claim to what the benchmark supports

### New workflow
high-level scientific object
<-> independently existing data/material/paradigm
-> unresolved prediction-changing LLM question
-> novelty assassination
-> minimum adaptation
-> pilot
-> structural law

Prefer candidates where we can say:

> "The data existed before our hypothesis."

or at minimum:

> "The experimental paradigm and gold standard existed before our hypothesis; we only adapt the interface to LLMs."

This is now a major promotion advantage.

---

# 7. Current ranking after the correction

| Candidate | Object naturalness | Existing independent substrate | Gold robustness | Construction risk | Data-first verdict |
|---|---:|---:|---:|---:|---|
| **CK** | very high | **very high** | high | **low–medium** | **CONTINUE / #1** |
| **AE** | very high | medium (published linguistic examples; no direct NLP benchmark found) | medium | **high** | **DEMOTE / DATA AUDIT** |
| **GRN** | very high | low for the exact LLM estimand | low–medium | **very high** | **REPLACEMENT SEARCH** |

The correct conclusion is therefore **not** "all synthetic data are bad."

It is:

> **A Main-level candidate should not require us to invent both the scientific question and the world that makes the answer measurable.**

CK currently clears that bar best. AE may clear it only through published/corpus-grounded materials. GRN currently does not.

---

# 8. Authority

This audit supersedes the **data-simplicity judgments** in V9 but does not erase the V9 novelty/history analysis.

Current working rule:
- CK: continue with released human materials first;
- AE: no compute until a provenance-first material audit;
- GRN: search for an independently grounded dataset; replace if none;
- continue searching for better candidates with **D0–D2 data paths** rather than forcing three theory-first questions.

> **Data is part of the research question, not an implementation detail.**
