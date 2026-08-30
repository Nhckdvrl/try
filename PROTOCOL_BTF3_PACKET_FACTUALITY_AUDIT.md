# Protocol — BTF-3 packet factuality audit v1

**Created:** 2026-08-31
**Status:** frozen before any citation is opened. Tag
`g2-packet-factuality-audit-protocol-v1` identifies this document, the
deterministic sampler, and the drawn subsample. Audit verdicts are recorded
only after that tag exists.

## The objection this answers

The large-replication review ledger states plainly that its reviewer of record
was an LLM assistant working without external lookup, while one of the four
gates it applied is called *exact-packet factual validity*. BTF-3's
`resolution_explanation` is machine-generated and, by the source card's own
admission, only partially spot-checked. A reviewer is therefore entitled to
ask: on what basis is it claimed that 256 packets are factually valid, when
nobody opened the citations?

This protocol answers that question directly, at a fixed and disclosed cost,
without touching the primary sample.

## Hard constraint: the primary sample does not change

Model outputs for all 256 units already exist (`g1-btf3-large-replication-freeze-v1`,
artifact SHA-256 `0b6fd8d0304f6b7cde336a6518b1058983a9b93529e90cbb577d1878acf0901d`).
Removing or replacing items after seeing outputs would destroy the
preregistration. Therefore:

- **no audited item is removed from the 256**, whatever the audit finds;
- the audit's only outputs are a reported error rate, a per-item ledger, and —
  clearly labelled secondary — a leave-flagged-out sensitivity estimate;
- the primary intrusion estimates in `results/btf3_large_replication_v1_analysis.json`
  stand as the preregistered result regardless of the audit's outcome.

## Sample: 64 items, fixed by hash before any lookup

`scripts/sample_btf3_factuality_audit.py` draws, from the frozen 256:

```text
h_i = SHA256("btf3-factual-audit-v1:" + question_id)
```

ascending within each realized-outcome bucket, first **32 realized YES + 32
realized NO = 64**. The drawn IDs and their hashes are recorded in
`data/external/review/btf3_factuality_audit_v1_sample.json`, and the audit
packets are `btf3_factuality_audit_v1_{yes,no}.md`. Both are committed and
tagged before any citation is opened, so the audited subsample cannot drift.

## What the auditor does

External lookup is **required** — that is the entire point of this exercise.
The auditor must not consult any target-model output. Per item, five checks:

1. the recorded realized outcome is correct against the cited/primary evidence;
2. the cited sources exist and actually support what the packet says they support;
3. no cited evidence postdates the question's resolution deadline in a way the
   packet's reasoning depends on;
4. no temporal-logic error inside the packet;
5. the resolution criteria and the claimed outcome genuinely align.

One verdict per item:

- **PASS** — no material error;
- **MATERIAL_ERROR** — one or more checks fail in a way that changes the
  outcome or removes its support (a cosmetic slip that leaves outcome and
  support intact is not material and is recorded as PASS with a note);
- **UNVERIFIABLE** — the cited sources cannot be reached or no longer exist.

MATERIAL_ERROR and UNVERIFIABLE require exactly one line of reason. Verdicts
go in `data/external/review/btf3_factuality_audit_v1_verdicts.md`, whose header
names the auditor and states what tooling and lookup access were used.

## Decision rule, fixed now

Let `E` be the count of MATERIAL_ERROR verdicts among the 64.

| result | action |
|---|---|
| `E ≤ 2` (≤ 3.1%) | acceptable. Report the audited rate and its exact binomial 95% interval in the paper; no further audit. |
| `3 ≤ E ≤ 6` (4.7–9.4%) | report the rate, and run the leave-flagged-out sensitivity below. Still no membership change. |
| `E ≥ 7` (> 10%) | stop and commission a **full-256 external audit**; report the result as a limitation and sensitivity analysis, and state the packet-error rate prominently in the paper's limitations. |

UNVERIFIABLE items are reported separately and are **not** counted into `E`;
if UNVERIFIABLE exceeds 8/64, that fact is itself reported as a limitation on
auditability rather than as a packet-error rate.

## Secondary sensitivity analysis (never primary)

`scripts/analyze_btf3_factuality_audit.py` recomputes each model's
`OutOfSetIntrusion` over the 256 minus the audit-flagged items, with the same
estimator, seed, and resamples as the primary analysis. This is descriptive
robustness only: it is computed after model outputs exist, on a subsample
defined by a post-output audit, and can never replace or override the
preregistered primary estimate. It is reported as "excluding the `k` items
flagged in the factuality audit, the estimate moves from X to Y."

## What gets reported in the paper

One short paragraph, regardless of outcome: how the 64 were drawn, who audited
them with what access, the PASS / MATERIAL_ERROR / UNVERIFIABLE counts with an
exact binomial interval on the error rate, and the sensitivity estimate if the
rule above calls for one. This is artifact hygiene, not a scientific
contribution, and is written as such.
