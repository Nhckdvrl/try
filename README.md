# Can LLMs Unsee the Future?

## Hindsight contamination despite correct temporal-boundary recognition

This repository now supports a **temporal hindsight-contamination paper**, not the
older cross-boundary *Information-Set Reasoning* program that originally motivated
some of the exploratory work.

The central question is simple:

> **After a language model learns what happened later, can it still reconstruct
> the judgment that should have been made from what was knowable at the time?**

Our main finding is a **recognition–enforcement gap**. Models can identify with
near-ceiling accuracy that a piece of evidence lies outside the target historical
information set, while that same future evidence still causally shifts the
model's reconstructed ex-ante probability.

The current paper-level contribution is therefore narrower than generic
"information-set reasoning", "future-information leakage", or "hindsight bias":
we **hold the question and evidence fixed and causally manipulate the presence
and admissibility of the same explicit future evidence**.

---

# 1. Main causal design

The primary source is BTF-3. For each independently sampled binary forecasting
question, we construct a 2×2 design:

| target information set | future packet absent | same future packet present |
|---|---|---|
| ex ante: only information available at the historical cutoff | `OOB_WITHOUT` | `OOB_WITH` |
| retrospective: all supplied information is licensed | `ALLOWED_WITHOUT` | `ALLOWED_WITH` |

Every condition asks for a 0–100 probability that the original question resolves
YES. The packet is the source-native BTF-3 resolution explanation; the same packet
is used in both `*_WITH` cells.

For realized outcome `r ∈ {0,1}`, let `s = 2r - 1`:

```text
Responsiveness      = s * (p_allowed_with - p_allowed_without)
OutOfSetIntrusion   = s * (p_oob_with - p_oob_without)
BoundarySelectivity = Responsiveness - OutOfSetIntrusion
```

A separate per-item probe asks whether the future packet belongs to the target
information set. This lets us distinguish **recognizing the temporal boundary**
from **actually enforcing it in the judgment**.

---

# 2. Evidence chain

## 2.1 Discovery → confirmation → large replication

The BTF-3 evidence was accumulated prospectively in three stages:

- **8-item discovery pilot**;
- **64-item preregistered confirmation**, entirely fresh relative to the pilot;
- **256-item preregistered large replication**, 128 realized YES + 128 realized
  NO, entirely fresh relative to the pilot, the 64-item confirmatory sample, and
  even the prior confirmatory candidate queue.

The 256-unit round passes its preregistered gate **on its own**, without pooling:

| model | boundary recognition | responsiveness | `OutOfSetIntrusion` (95% CI) |
|---|---:|---:|---:|
| Qwen3.5-9B | 99.22% | 47.27 | **16.02 [14.18, 17.89]** |
| Gemma-3-12B-it | 99.80% | 46.89 | **27.73 [25.15, 30.39]** |
| Mistral-Small-24B | 100.00% | 39.31 | **7.46 [5.41, 9.57]** |

All three models qualify and all three clear the preregistered 5-point SESOI.
The earlier 64-unit estimates are statistically compatible with the 256-unit
round; no cross-round contrast excludes zero.

See:

- [`results/btf3_confirmatory_v1_results.md`](results/btf3_confirmatory_v1_results.md)
- [`results/btf3_large_replication_v1_results.md`](results/btf3_large_replication_v1_results.md)
- [`results/btf3_cross_round_replication.json`](results/btf3_cross_round_replication.json)

## 2.2 The effect is not reducible to copying an explicit YES/NO verdict

G2 removes explicit resolution-verdict sentences from the future packet while
retaining the remaining post-cutoff evidence. A fail-closed audit removed 368
verdict sentences across the 256 frozen packets and retained 97.9% of packet
characters on average.

The redacted packets remain useful when licensed (`Responsiveness` ≈ 45–47
points), and hindsight contamination survives the manipulation. The
preregistered survival gate passes. Raw estimates are:

| model | direct packet | verdict-redacted packet |
|---|---:|---:|
| Qwen3.5-9B | 16.02 | 23.35 |
| Gemma-3-12B-it | 27.73 | 34.55 |
| Mistral-Small-24B | 7.46 | 10.18 |

The safe claim is:

> **Hindsight contamination is not reducible to copying an explicit resolution
> label.**

The larger redacted effects were **not predicted**. We do not claim a mechanism
for that increase: removing verdict sentences may also make the packet look less
obviously retrospective and slightly changes evidence-to-task distance.

See [`results/g2_hindsight_depth_results.md`](results/g2_hindsight_depth_results.md).

## 2.3 Scale does not remove the failure within Qwen3.5

On the same frozen 256 questions, available dense Qwen3.5 checkpoints show:

| checkpoint | boundary recognition | `OutOfSetIntrusion` (95% CI) |
|---|---:|---:|
| 4B | 99.61% | **32.00 [28.40, 35.65]** |
| 9B | 99.22% | **16.02 [14.18, 17.89]** |
| 27B | 100.00% | **36.75 [33.50, 39.93]** |

The trend is strongly non-monotone, so we do **not** fit or claim a scaling law.
What the data support is narrower: boundary recognition is saturated at every
size while enforcement varies by more than 20 probability points, and the
largest checkpoint is not less contaminated.

See [`results/qwen_size_sweep_results.md`](results/qwen_size_sweep_results.md).

---

# 3. What did not become a headline result

## Positional reminder effect

On the 64-item factorization set, repeating the same exclusion reminder **after**
the future evidence was more effective than repeating it **before** the evidence
for Qwen and Gemma. The same raw pattern appeared again on 256 items.

However, the preregistered G2 panel gate did **not** pass because Qwen was
formally disqualified by a boundary-probe failure in a separate G2 condition,
and the licensed-frame specificity control did not establish that the positional
effect is exclusion-specific.

Therefore the paper may report the 64-item finding and the 256-item raw pattern,
but **must not claim an independently replicated positional mechanism**.

## FOMC external-source attempt

A prospectively designed 24-unit FOMC qualification pilot produced positive
intrusion point estimates but failed its frozen source-qualification gate. That
version is sealed as **inconclusive / not validated**. It is useful as a reported
external-replication attempt, not as evidence of cross-source generality.

## FANToM / broad multi-family framing

The perspective-family pilot failed qualification, so the original plan for a
broad multi-boundary Information-Set Reasoning paper was abandoned. The current
paper makes **no claim of generality beyond the temporal family**.

---

# 4. Data quality and audit trail

The large-replication sample was selected by a frozen deterministic queue and
reviewed before target-model output. The final artifact contains 256 unique,
fresh question IDs and passed all fail-closed schema / overlap / transformation
checks and a full pre-run token census.

Because the original large-replication review did not use external lookup, we
later preregistered a hash-fixed 64-item factuality audit before opening any
citations. The external audit returned:

- **63 PASS**;
- **1 MATERIAL_ERROR**;
- **0 UNVERIFIABLE**.

The one error is a question/criteria date-window contradiction, not a fabricated
event. Excluding it changes no model estimate materially. This audit did not
trigger the preregistered expanded-review rule, but it is **not** a certificate
that all 256 packets are factually valid.

See:

- [`data/external/review/BTF3_LARGE_REPLICATION_V1_FREEZE_REPORT.md`](data/external/review/BTF3_LARGE_REPLICATION_V1_FREEZE_REPORT.md)
- [`results/btf3_factuality_audit_v1_results.md`](results/btf3_factuality_audit_v1_results.md)
- [`PROTOCOL_BTF3_PACKET_FACTUALITY_AUDIT.md`](PROTOCOL_BTF3_PACKET_FACTUALITY_AUDIT.md)

---

# 5. Novelty boundary

The paper does **not** claim to be the first observation that a model can state a
temporal rule correctly and still violate it. Recent temporal-legal reasoning
work already reports that pattern for statute-vintage selection.

The paper's distinctive object of measurement is:

> **the causal effect of one fixed piece of explicit future evidence on an
> otherwise identical historical judgment, while independently measuring whether
> the model recognizes that the evidence lies outside the target information
> set.**

This also differs from generic in-context forgetting, distractor robustness,
misinformation retraction, and security-oriented information-flow work. Those
literatures are discussed in [`RELATED_WORK_2026.md`](RELATED_WORK_2026.md).

Claims we explicitly do **not** make:

- universal failure across all LLMs or all tasks;
- cross-source replication;
- generality across perspective / procedural / role boundaries;
- a neural or representation-level mechanism;
- a scaling law;
- that verdict redaction removes all answer-revealing evidence;
- that the factuality audit establishes complete source validity.

---

# 6. Current paper structure

The scientific story is now stable enough to write as a paper:

1. **Problem:** reconstructing a past judgment after later evidence is known.
2. **Method:** same-evidence presence × admissibility causal design.
3. **Main result:** near-perfect temporal-boundary recognition coexists with
   substantial causal contamination.
4. **Replication:** 64-item confirmation followed by an independent 256-item
   large replication.
5. **Depth:** contamination survives removal of explicit YES/NO verdict labels.
6. **Scale:** larger models within Qwen3.5 do not monotonically become less
   contaminated.
7. **Boundaries:** FOMC does not validate cross-source generalization; the
   positional factorization does not clear its preregistered replication gate.

The next priority is **paper consolidation** — figures, tables, introduction,
related work, limitations, and appendix organization — rather than adding more
unplanned manipulations.

---

# 7. Reproduce / inspect

Current paper-level entry points:

```text
README.md                                current scientific summary
RESEARCH_PLAN.md                         frozen claim / writing plan
RELATED_WORK_2026.md                     novelty boundary and closest neighbours
BTF3_TRANSFORMATION_CONTRACT.md          source-native temporal transformation
PREREGISTRATION_BTF3_LARGE_REPLICATION.md
                                         256-unit large-replication design
PREREGISTRATION_G2_HINDSIGHT_DEPTH.md    verdict-redaction / positional depth tests
PREREGISTRATION_G2_QWEN_SIZE_SWEEP.md    within-family size analysis
PROTOCOL_BTF3_PACKET_FACTUALITY_AUDIT.md factuality-audit protocol
REPRODUCE.md                             reproduction notes

results/btf3_large_replication_v1_results.md
results/g2_hindsight_depth_results.md
results/qwen_size_sweep_results.md
results/btf3_factuality_audit_v1_results.md
```

Raw outputs needed for the current analyses are tracked under `results/raw/`.
The analysis scripts live under `src/` and `scripts/`.

---

# 8. Historical material

The repository contains substantial earlier controlled-suite and source-search
work (`PREREGISTRATION_G0.md`, `STAGE*.md`, `FINDINGS.md`, FANToM / SCOTUS / FOMC
contracts, and older redesign notes). Those files are retained for auditability
and to document falsified hypotheses, but **they are not the current paper
narrative**.

For a reader interested in the present submission, the files listed in §7 are
the recommended path.