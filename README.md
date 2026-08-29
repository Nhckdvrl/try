# Known, but Out of Bounds

## Can LLMs know information without using it in a decision?

> **Scope reset — 2026-08-29.**  
> This project began from the human **Unring the Bell** problem: after a decision maker has seen inadmissible evidence, can an instruction really remove that evidence from the final decision? The first preregistered LLM experiment did **not** reproduce the expected human temporal pattern. It inverted it. A large controlled follow-up then uncovered a sharper prospective-nullification failure and a causal signature inside open models.
>
> The controlled result is real and reproducible. **What is not yet established is that it is a broad, natural LLM decision-making failure.** The present 144-item suite is heavily constructed and reuses a small number of latent templates. One independently sourced invalid-information paradigm is handled almost perfectly by the tested models; the existing natural outcome-bias anchor is only one scenario. Therefore the next phase is a **dataset/external-validity rebuild before any further broad mechanism claim**.

Start here:

- **[DATASET_REDESIGN.md](DATASET_REDESIGN.md)** — why the current data are insufficient as primary evidence and exactly how EVS-v1 will replace that role.
- **[PREREGISTRATION_G1.md](PREREGISTRATION_G1.md)** — freeze protocol for the new external validation phase.
- **[RELATED_WORK_2026.md](RELATED_WORK_2026.md)** — updated novelty boundary, including ICF-Bench, curse-of-knowledge work, continued-influence research, AgentSecBench/Fides/CoPriva/NeuroTaint.
- **[FINDINGS.md](FINDINGS.md)** — full controlled-suite results and mechanism history.
- **[PREREGISTRATION_G0.md](PREREGISTRATION_G0.md)** — what was frozen before the first exclusion experiment.
- **[REPRODUCE.md](REPRODUCE.md)** — reproduction instructions for the existing experiments.

---

# 1. Mother question

The core distinction is:

> **Information retention can remain; decision influence must disappear.**

Suppose a model has already learned some information `E`. A later policy says that `E` is outside the information set permitted for a particular decision `Y`.

A successful model does **not** need to forget `E`. It may still be able to quote it, recognize it, or answer a memory probe about it. What it must do is make the specified decision as though changes in `E` no longer causally matter.

We call the target property **policy-conditioned causal non-use**.

This is the clean conceptual separation from literal forgetting:

```text
memory(E) may remain high
policy_knowledge(E is forbidden for Y) should be high
causal_effect(E -> Y | deny policy) should be ~0
```

---

# 2. Why this is not just ICF / “please forget”

Qian et al., **Do LLMs Forget What They Should? Evaluating In-Context Forgetting in Large Language Models** (ICLR 2026), introduce ICF-Bench with 2,000 multi-turn dialogues and study whether models can selectively forget interfering contextual information.

That makes the naive version of this project unavailable as a contribution:

```text
Tom likes blue
-> please forget Tom's favorite color
-> what color does Tom like?
```

If our paper were only “the model was told to forget/ignore something but later still used or recalled it,” it would be too close to ICF and neighboring correction/retraction work.

Our intended target state is different. In a legal case, a confidential evaluation, an ex-ante decision review, or a perspective-taking task, the information can remain **true and known** while being **out of bounds for this decision**.

The paper only becomes distinct if we measure the retention/non-use dissociation directly.

---

# 3. Where the project actually went

## G0 — preregistered Unring-the-Bell test

The original design froze 144 of 180 candidate items before any exclusion condition was generated or run. Screening used only Base/Admit behavior and an independent Admit rule probe on Qwen3-8B.

Five controlled families were included:

- legal judgment;
- numerical aggregation;
- ranking/selection;
- evidence-based inference;
- ex-ante outcome evaluation.

The primary conditions were:

```text
Base          B -> judgment
Admit-Pre     B -> allow rule -> E -> judgment
Admit-Post    B -> E -> allow rule -> judgment
Exclude-Pre   B -> deny rule -> E -> judgment
Exclude-Post  B -> E -> deny rule -> judgment
```

Rule and memory probes were separate calls.

### The preregistered timing hypothesis failed — in the opposite direction

Across twelve autoregressive instruct checkpoints from multiple families, plus two masked diffusion LMs, the pattern was not:

```text
Post exclusion is harder than Pre exclusion
```

It was consistently:

```text
Pre exclusion leaks more than Post exclusion
```

For example, in the original controlled suite:

| model | REI Exclude-Pre | REI Exclude-Post | pre - post |
|---|---:|---:|---:|
| Qwen3-8B | +0.45 | +0.12 | +0.33 |
| Gemma-3-12B | +0.43 | +0.07 | +0.36 |
| Qwen2.5-32B | +0.30 | +0.00 | +0.30 |
| Mistral-Small-24B | +0.19 | -0.03 | +0.22 |
| Qwen3-14B | +0.49 | -0.07 | +0.56 |

The exact table, confidence intervals, all models, and replication are in [FINDINGS.md](FINDINGS.md).

This killed the first story. The controlled finding became:

> **The models did not primarily fail to “unring” already-seen evidence. Several failed to pre-commit to making a specific future item causally inert.**

---

# 4. What the controlled follow-ups established

The stages below are **mechanistic discovery on CDS-v1**, not yet proof of a natural general phenomenon.

## 4.1 Rule knowledge can be correct while causal use is wrong

In a separate declarative probe, multiple models stated that the critical item's required decision weight was exactly `0%` on essentially all items. Yet in the prospective arm the decision could still carry a large fraction of the evidence's normal effect.

This is the strongest conceptual result from the controlled suite:

```text
knowing the policy != implementing the policy in the decision
```

## 4.2 The zero-weight case is unusually sharp

A weight sweep used the same sentence and varied only the requested weight. The Pre/Post gap was largest at exactly zero and mostly collapsed once the requested weight was non-zero.

This is **not** a clean claim that models accurately implement arbitrary fractional weights — they do not. It is evidence that complete nullification behaves differently from ordinary attenuation in this construction.

## 4.3 Delay is not the main explanation

Moving the prospective rule farther from the evidence did not monotonically worsen the failure in most tested models. The effect can already be large when the rule immediately precedes its target.

That argues against a simple prospective-memory-decay account.

## 4.4 A name or placeholder is not enough

Telling the model that an item `E7` will appear later, adding a placeholder, or describing its type/direction does not reliably rescue prospective suppression. In several models it makes the failure worse.

Having the **specific proposition** available before the rule can help.

## 4.5 Semantic relation matters more than string identity

A paraphrase of the future evidence can support later suppression about as well as the exact same text, while high lexical overlap with a different proposition does not.

Stage 3E then exposed an important confound: previewing the same fact also makes a second presentation redundant. After switching from unstable ratios to raw marginal rating points, the semantic exclusion boost remained and dissociated from redundancy.

The resulting controlled interpretation is narrower than “content-addressed” in a loose sense: a sufficiently specific proposition available at rule time can change how strongly the later rule suppresses matching information.

## 4.6 Prospective selective routing is not generally impossible

A tagged numeric stream provides a crucial falsification. When each report carries a meaningful local status and the policy says which class to use, several models can route the stream prospectively with almost zero leakage.

Therefore the broad claim

> “LLMs cannot apply exclusion rules prospectively”

is false.

The controlled bug is more specific: certain rules about making a **specific future content item** causally inert behave very differently from policies that can be resolved locally when evidence arrives.

## 4.7 The agent interface reproduces part of the failure

In Stage 4, a persistent `SYSTEM` policy names a future document and the document later arrives through a `TOOL` message. In some models an identifier-only future policy removes almost none of the retrieved document's marginal influence, whereas a policy delivered after retrieval works much better.

This is practically interesting, but the underlying semantic items are still inherited from the same controlled legal/inference pool. It is an **interface transfer**, not an independent data replication.

---

# 5. Existing mechanism result — and its current scope

On Qwen3-8B, evidence-span attention blocking can remove the residual influence in controlled legal/inference items. Answer-position patching localizes a late decision difference. Same-chronology rule-span patching then finds a causal state in middle layers before the evidence is processed.

A replication on Mistral-Small-24B reproduces the middle-network localization and strong causal effect, although the symmetry of rescue/break interventions differs from Qwen.

This licenses:

> A model-internal state associated with successful versus failed controlled suppression exists and can causally alter the later decision.

It does **not** yet license:

> This is the universal mechanism by which LLMs fail to ignore forbidden information in natural tasks.

The latter requires external behavioral replication first, followed by mechanism transfer onto independently authored items.

No more large mechanism campaign should be prioritized before that gate.

---

# 6. The data problem

The repository reached a point where model breadth was much stronger than data breadth.

The 144 frozen items sound large, but the semantic support is much smaller:

- legal: 10 authored cases crossed with six evidence types;
- numeric: a programmatic aggregation generator under multiple surface skins;
- ranking: one latent near-tie/scoring construction rendered as vendors/applicants/apartments/etc.;
- inference: a small number of two-hypothesis diagnostic templates;
- outcome: a small set of authored decision stories.

Most conditions also share the same compiler grammar:

```text
BACKGROUND
RULING
ADDITIONAL INFORMATION
TASK
```

That uniformity is useful for causal control, but it means a cross-domain average can still be a **cross-skin average of one experimental language**.

Running twelve models on the same stimuli does not repair this.

---

# 7. The external validation already tells us to be cautious

Two held-out directions have been tried.

## Ramsey/Liu/Trueblood-style invalid numeric reports

The repository adapted an independently authored human invalid-information paradigm. Under the tested versions, Qwen3-8B, Gemma-3-12B, and Mistral-Small-24B almost perfectly remove the flagged fabricated report.

That is a **negative external replication** of a broad gating-failure claim.

It should remain in the paper as a boundary condition.

Also note the provenance issue: the repo preserves source instructions/task structure but sweeps newly generated numeric offsets because the original outliers have too little leverage on these LLMs. It should not be described as fully verbatim external data.

## Baron-Hershey / Aiyer outcome bias

The verbatim bypass-surgery vignette does show residue in the small anchor, but the repository currently has only four framing/outcome cells from one semantic scenario.

That is suggestive, not a dataset.

These two facts are why the next phase changes.

---

# 8. New data strategy: natural first, controlled second

The existing dataset is now named:

> **CDS-v1 — Controlled Discovery Suite**

Its job is to isolate variables and support causal mechanism work.

The main behavioral evidence must come from:

> **EVS-v1 — External Validation Suite**

built from independently authored experimental materials and natural source texts.

Highest-priority sources currently identified:

1. **Engel, Golder & Rahal (2026)** — inadmissible character/wiretap evidence in 1,432 human participants.
2. **Aiyer et al. (2023) / Baron & Hershey** — outcome bias, open materials/data/code, `N=692` replication.
3. **The “curse of knowledge” when predicting others’ knowledge (2022)** — 40 trivia items with independently measured novice difficulty and open OSF data/code.
4. **Open continued-influence/retraction materials** — a false/invalid-information contrast family, not the conceptual center.
5. **Oien & Goernert (2003) forbidden-information employee selection** — excellent conceptual fit if the original stimuli can be legally obtained/reused.

See [DATASET_REDESIGN.md](DATASET_REDESIGN.md) and the provenance-first [source manifest](data/external/source_manifest.json).

We will not fix this problem by writing more synthetic court cases.

---

# 9. New primary metric: counterfactual forbidden sensitivity

For a natural item with two critical-information values `E+` and `E-`, the preferred G1 design is:

```text
ALLOW(E+)   ALLOW(E-)
DENY(E+)    DENY(E-)
```

Then measure in raw output units:

```text
AllowedSensitivity   = Y[ALLOW(E+)] - Y[ALLOW(E-)]
ForbiddenSensitivity = Y[DENY(E+)]  - Y[DENY(E-)]
PolicySuppression    = AllowedSensitivity - ForbiddenSensitivity
```

A correct policy-conditioned decision should show:

```text
AllowedSensitivity != 0
ForbiddenSensitivity ~= 0
```

The normalized leakage fraction is secondary and is only defined when the allowed contrast is large enough. The implementation is in [`src/metrics_policy_nonuse.py`](src/metrics_policy_nonuse.py).

This avoids making a fragile Base-anchored ratio the primary result and directly tests causal invariance to forbidden content.

---

# 10. Updated novelty boundary

The following claims are **not** available as novelty:

- “models fail to forget contextual information” — ICF-Bench is directly adjacent;
- “auxiliary knowledge biases LLM judgments” — ComplexEval and other curse-of-knowledge work already show this;
- “models can violate information boundaries” — agent privacy/security work already studies this;
- “noninterference is a useful formal view” — Fides and AgentSecBench explicitly use information-flow/noninterference ideas;
- “semantic influence should be tracked in agents” — NeuroTaint explicitly includes causal influence in its notion of flow;
- “structured labels/projections are better than prompt-only policy” — security work already motivates enforced information-flow controls.

The possible contribution, **if EVS-v1 succeeds**, is narrower:

> LLM decisions can remain causally sensitive to information that is still known but explicitly out of bounds for that decision; this can be separated from policy knowledge and memory, quantified by counterfactual semantic sensitivity, and traced inside the model's decision computation.

The full map is in [RELATED_WORK_2026.md](RELATED_WORK_2026.md).

---

# 11. G1 stop/go logic

The project should now be willing to die cleanly.

### A. Two or more independent true-but-disallowed external families leak

Proceed with the broad paper. Replicate mechanism on external items before generalizing the CDS-v1 internal story.

### B. Only one natural family leaks

Narrow the paper to that family (for example outcome bias or privileged-state contamination).

### C. Only the controlled future-target failure survives

Retitle the object to the **prospective nullification gap** and validate it in realistic agent/tool policies over independently sourced documents. Do not call it generic evidence gating.

### D. External families are clean

Stop the broad interpretability story. Preserve CDS-v1 as a controlled diagnostic result rather than explaining a natural phenomenon that is not there.

This gate is preregistered in [PREREGISTRATION_G1.md](PREREGISTRATION_G1.md).

---

# 12. Repository map

```text
README.md                       current scientific status
DATASET_REDESIGN.md             external-validity redesign
RELATED_WORK_2026.md            novelty boundary
PREREGISTRATION_G0.md           frozen original test
PREREGISTRATION_G1.md           next external-validation freeze protocol
FINDINGS.md                     full controlled-suite findings
STAGE3*.md / STAGE4.md / STAGE5.md
                                exploratory/mechanistic history
REPRODUCE.md                    existing reproduction guide

data/items/                     CDS-v1 and controlled derivative items
data/external/source_manifest.json
                                provenance plan for EVS-v1
src/gen_*.py                    controlled/current generators
src/conditions_*.py             condition compilers
src/metrics_policy_nonuse.py    G1 raw causal-sensitivity metrics
src/mech/                       controlled mechanism code
results/                        existing result tables/raw outputs
logs/                           execution logs
```

Old findings are intentionally not rewritten away. The research history matters because several attractive explanations were falsified or corrected by later controls.

---

# 13. Immediate next work

The priority order is now:

1. acquire original external materials and verify reuse terms;
2. record hashes/provenance before transformations;
3. build source-specific importers with minimal policy injection;
4. audit semantic units and cluster structure by hand;
5. finalize and freeze G1 before any `DENY` run;
6. run behavior only on a small multi-family model panel;
7. decide Gate A/B/C/D;
8. **only then** return to activation patching, attention analysis, training, or mitigation.

The key methodological correction is:

> **Natural data establish whether the phenomenon exists. Controlled synthetic data explain it after it exists.**

That is the research program from this point forward.
