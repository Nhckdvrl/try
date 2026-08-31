# Data audit: current temporal-hindsight paper

This note summarizes the data provenance that matters for the current paper.
Earlier source-search iterations are intentionally compressed; detailed contracts
and failed designs remain in the repository for auditability.

## 1. Primary source: BTF-3

BTF-3 is the only natural source contributing positive primary evidence to the
current paper.

Pinned source facts:

- Hugging Face revision: `4b426627e19cd86202de69a40bc9dadb7f5ccd59`;
- license: CC BY-NC 4.0;
- 1,907 independent question IDs total;
- 1,515 binary questions and 392 numeric questions;
- the paper uses only binary questions;
- native fields separate historical cutoff information, realized outcome, and a
  source-native resolution explanation.

The exact temporal transformation is documented in
[`BTF3_TRANSFORMATION_CONTRACT.md`](BTF3_TRANSFORMATION_CONTRACT.md).

## 2. Frozen BTF-3 evidence rounds

### Discovery pilot

- 8 accepted independent questions;
- 4 realized YES / 4 realized NO;
- two earlier candidate packets were permanently rejected for material factual /
  temporal problems before target-model output.

### Confirmatory round

- 64 fresh independent questions;
- 32 YES / 32 NO;
- no overlap with the 8-item pilot;
- selection and review completed before confirmatory target-model output.

### Large replication

- 256 additional fresh independent questions;
- 128 YES / 128 NO;
- no overlap with the pilot, the 64-item confirmatory artifact, or the old
  confirmatory candidate queue;
- deterministic queue, prospective review, immutable freeze tag;
- full schema / overlap / transformation audit passed;
- all 4,608 rendered prompts across the three frozen chat templates were counted
  before model execution and fit under the 8,192-token limit.

The primary replication verdict is computed on the 256 units alone.

See:

- [`PREREGISTRATION_BTF3_LARGE_REPLICATION.md`](PREREGISTRATION_BTF3_LARGE_REPLICATION.md)
- [`data/external/review/BTF3_LARGE_REPLICATION_V1_FREEZE_REPORT.md`](data/external/review/BTF3_LARGE_REPLICATION_V1_FREEZE_REPORT.md)
- [`results/btf3_large_replication_v1_token_census.json`](results/btf3_large_replication_v1_token_census.json)

## 3. Human / LLM-assisted review caveat

The large-replication candidate review was LLM-assisted and performed without
external web lookup. That is a real provenance limitation because one review
gate concerns exact-packet factual validity.

To quantify the risk without changing sample membership after model output, a
separate protocol fixed a 64-item audit subsample by hash **before any citation
was opened**.

External factuality audit result:

- 63 PASS;
- 1 MATERIAL_ERROR;
- 0 UNVERIFIABLE;
- material-error rate: 1/64 = 1.56%;
- Clopper–Pearson exact 95% CI: [0.04%, 8.40%].

The single material error is a question/criteria date-window contradiction in a
Western Balkans Growth Plan item. The cited event itself is real; the source item
is internally inconsistent about which date window binds.

Excluding that item in a secondary sensitivity analysis changes the primary
intrusion estimates negligibly:

| model | primary | excluding flagged unit |
|---|---:|---:|
| Qwen3.5-9B | 16.02 | 15.92 |
| Gemma-3-12B-it | 27.73 | 27.65 |
| Mistral-Small-24B | 7.46 | 7.59 |

The preregistered expanded-review trigger was not reached. This is **not** a
claim that all 256 packets are externally validated.

See [`results/btf3_factuality_audit_v1_results.md`](results/btf3_factuality_audit_v1_results.md).

## 4. Resolution-packet design caveat

Most original BTF-3 resolution packets explicitly state the realized YES/NO
outcome. Therefore the baseline large-replication result by itself cannot tell
whether the model is integrating post-cutoff evidence or merely copying an
explicit verdict.

G2 addresses this with a frozen subtractive verdict-redaction transformation:

- 368 assertive verdict sentences removed across 256 packets;
- zero assertive verdict sentences survive the fail-closed audit;
- 97.9% of packet characters retained on average;
- 19 packets are no-ops because they did not contain an explicit verdict
  sentence.

The remaining evidence still has strong allowed-frame leverage, and
contamination survives. This licenses the narrower statement that the effect is
**not reducible to copying an explicit resolution label**.

It does not license the stronger claim that redacted packets contain no
outcome-entailing evidence.

## 5. Other sources: current status only

The repository explored several alternatives while the project still targeted a
broader information-set story. None contributes positive primary evidence to the
current paper.

| source | final status | paper role |
|---|---|---|
| FANToM | perspective pilot failed qualification | historical negative / scope boundary |
| ForecastBench | unsuitable for the required source-native later packet and independence structure | source-audit rejection |
| SCOTUS | full transcript design exceeded context budget by a large margin | mechanical calibration failure |
| FOMC | 24-unit temporal pilot failed preregistered source-qualification gate | external replication attempt, inconclusive |
| Aiyer outcome-bias materials | too little independent semantic support for the current primary design | historical anchor only |

These failures are retained because they constrain the claims: **the current
paper has strong within-source replication, not cross-source replication.**

## 6. Statistical unit

For current external analyses, the independent unit is the original BTF-3
`question_id`. Each question receives equal weight.

Inference uses paired question-level effects and 10,000-resample cluster
bootstraps. Replicated renderings or conditions never receive extra weight merely
because they produce more rows.

Historical G0 controlled-suite inference remains unchanged and should not be
mixed with the BTF-3 primary estimates.

## 7. Current data claim

Safe wording:

> The phenomenon was prospectively confirmed on 64 fresh BTF-3 questions and
> independently replicated on a further 256 unseen questions (128 YES / 128 NO)
> using the same frozen temporal-admissibility design.

Unsafe wording:

- "replicated across datasets / sources";
- "all packets were externally verified";
- "the benchmark covers general information-set reasoning";
- "verdict redaction removes all answer disclosure".