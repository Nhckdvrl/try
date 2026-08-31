# Reasoning Within Bounds

## After a model has learned how something turned out, can it still say what it was reasonable to believe before?

> **Status — 2026-09-01.** The paper-level object is **reconstruction of a past
> epistemic state under hindsight**. The phenomenon is settled and has been
> replicated on 256 fresh natural questions; the current work is explanatory,
> not further prevalence measurement.
>
> **`PAPER_FRAME.md` is the authoritative register** — what the paper claims,
> which competing accounts are live, and which experiments are allowed to
> exist. This README records where the repository has been; the frame records
> where it is going. `WORKLOG.md` is the running record of the current campaign.

Start here:

- **[PAPER_FRAME.md](PAPER_FRAME.md)** — the natural question, the scientific
  object, the six competing accounts and which are eliminated, and the standing
  rule that an experiment must be writable as a sub-question of the headline.
- **[PAPER_OUTLINE.md](PAPER_OUTLINE.md)** — title, abstract, section plan, and
  the list of sentences the paper must not write.
- **[WORKLOG.md](WORKLOG.md)** — what has been run, why, and what came out.
- **[RELATED_WORK_2026.md](RELATED_WORK_2026.md)** — novelty boundary and the
  locked novelty sentence; the nearest published neighbour is conceded by name.

### What is established

On 256 fresh, independently sampled natural forecasting questions, with the
same evidence manipulated present/absent × licensed/unlicensed within item:

| round | result |
|---|---|
| large replication | recognition 99.2–100% per item; intrusion 7.5–27.7 points; gate passed 3/3 |
| G2-B verdict redaction | effect survives removal of the explicit YES/NO verdict, and grows (10.2–34.6) |
| Qwen3.5 size analysis | 4B/9B/27B: 32.0 / 16.0 / 36.8 — scale does not remove it; largest is most contaminated |
| **G3 exclusion reason** | **no stated reason is enforced** — not temporal, not a non-temporal licensing reason, not one that undercuts the evidence's truth |
| G7 ex-ante anchor | the preregistered displacement test **failed in the opposite direction**; kept, with the limitation it exposes |

### Preregistrations, in order

`PREREGISTRATION_G0` → `_G1` → `_G1_FACTORIZATION(_V2)` →
`_BTF3_LARGE_REPLICATION` → `_G2_HINDSIGHT_DEPTH` → `_G2_QWEN_SIZE_SWEEP` →
`_G3_EXCLUSION_REASON` → `_G4_MODEL_BREADTH` → `_G5_DELIBERATION` →
`_G6_MECHANISM` → `_G7_EXANTE_ANCHOR` → `_G8_RELEVANCE`.

Every one was frozen and tagged before the first generation of its round, and
each names in advance what it may and may not conclude.

### Earlier documents

- **[DATA_AUDIT.md](DATA_AUDIT.md)** — first-wave source, schema, hash, license.
- **[DATASET_REDESIGN.md](DATASET_REDESIGN.md)** — source-native architecture.
- **[FINDINGS.md](FINDINGS.md)** — full controlled-suite results and mechanism history.
- **[REPRODUCE.md](REPRODUCE.md)** — reproduction instructions.

The sections below are the earlier scope-reset narrative and are kept because
several attractive explanations in them were falsified by later controls.

---

# 1. Mother question

A target decision defines an information set: facts, observations, roles, and
time slices that are licensed to affect the answer. A model may possess more
information than that set. The capability under test is whether it can construct
and reason within the correct set.

The contract is bidirectional:

```text
Responsiveness:         ΔY_allowed != 0
Out-of-set invariance:  ΔY_outside ≈ 0
```

Failure is **out-of-set intrusion**. This abstraction covers temporal,
perspective, procedural, role/access, and decision-scope boundaries without
claiming that they necessarily share one internal mechanism.

---

# 2. Claim boundary

ICF-Bench already studies selective contextual forgetting; ExAnte studies use of
post-cutoff information; FANToM studies multi-party information asymmetry;
Resist and Update states the invariant-to-forbidden/responsive-to-licensed causal
contract; MedPIC-Bench studies conditional-rule updating. None of those pieces
alone is our novelty.

The proposed contribution is conditional on evidence: a source-native,
cross-boundary evaluation of whether information-set reasoning behaves as a
general competence or fragmented family-specific heuristics, followed by
cross-boundary transfer and gated mechanistic tests.

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

# 8. Source-native data strategy

CDS-v1 remains the Controlled Discovery Suite. New primary evidence is built
from independent sources without passing them through `src/schema.py`.

The first wave is FANToM (perspective), BTF-3 and ForecastBench (temporal), and
Aiyer (outcome/ex-ante evaluation). Procedural and decision-scope families are
added only after materials and reuse terms are verified. The exact audit is in
[DATA_AUDIT.md](DATA_AUDIT.md); pinned sources are in the
[manifest](data/external/source_manifest.json).

Each source keeps its native task and receives its own adapter and transformation
contract. `READY_TO_AUDIT` does not mean ready to run.

---

# 9. Primary behavioral contract and inference

```text
Responsiveness        = Y(allowed E+) - Y(allowed E-)
OutOfSetIntrusion     = Y(outside E+) - Y(outside E-)
BoundarySelectivity   = Responsiveness - OutOfSetIntrusion
```

Implementations are in `src/information_set_metrics.py`; legacy G1 names remain
in `src/metrics_policy_nonuse.py` for compatibility. New external inference
first averages within each independent semantic unit, then bootstraps equally
weighted cluster means. G0 analysis is unchanged.

---

# 10. G1 and transfer gates

The broad project continues only if at least two distinct natural families show
normal utility, correct boundary knowledge, retained/available information, and
non-zero out-of-set intrusion in a 2–3 open-model pilot.

If that gate passes, the main capability experiment trains on temporal +
procedural + perspective and holds decision-scope out completely. Transfer
supports a shared learnable competence; no transfer supports fragmented
heuristics. Both outcomes precede external mechanism work.

---

# 11. Repository map

```text
README.md                       current scientific status
RESEARCH_PLAN.md                phased paper and experiment plan
DATA_AUDIT.md                   exact first-wave source audit
DATASET_REDESIGN.md             source-native benchmark architecture
RELATED_WORK_2026.md            novelty boundary
PREREGISTRATION_G0.md           frozen original test
PREREGISTRATION_G1.md           information-set freeze protocol
FINDINGS.md                     full controlled-suite findings
STAGE3*.md / STAGE4.md / STAGE5.md
                                exploratory/mechanistic history
REPRODUCE.md                    existing reproduction guide

data/items/                     CDS-v1 and controlled derivative items
data/external/                  raw-cache instructions and source manifest
src/gen_*.py                    controlled/current generators
src/conditions_*.py             condition compilers
src/information_set_schema.py   external source-native schema
src/information_set_metrics.py  responsiveness/intrusion metrics
src/adapters/                   source-specific native readers
src/mech/                       controlled mechanism code
results/                        existing result tables/raw outputs
logs/                           execution logs
```

Old findings are intentionally not rewritten away. The research history matters because several attractive explanations were falsified or corrected by later controls.

---

# 12. Immediate next work

The priority order is now:

1. review and freeze a BTF-3 temporal transformation contract;
2. construct a small human-readable paired audit sample;
3. design the FANToM matched intervention without changing the target question;
4. resolve Aiyer material terms and the allowed-responsiveness condition;
5. freeze G1 before any target-model OOB run;
6. run only the small behavioral gate;
7. add families, cross-boundary tuning, and mechanism only if the gate passes.
