# Post-result correction — explicit-verdict redaction audit

**Status:** explicitly post-result. No frozen artifact, threshold, seed, sampling
rule, assignment or raw model output was changed. The original frozen audit
`data/external/review/BTF3_EVR_REDACTION_AUDIT.md` is retained unchanged as the
historical record of what was believed at freeze time; this file records what a
later independent audit found.

**Date:** 2026-09-03. **Audit code:** `src/audit_redaction_leakage.py`.
**Machine-readable result:** `results/btf3_redaction_leakage_audit.json`.

## 1. What the frozen audit claimed

The pre-run audit reports, under a hard gate:

> assertive verdict sentences surviving redaction: **0**

That number is not independent evidence. It is produced by the same
conditional-marker heuristic that decides what the redactor deletes, so it cannot
detect a failure mode the two share.

## 2. The defect

In `src/adapters/btf3_hindsight_depth.py`, `redact_verdicts` treats a sentence as
a criteria restatement — and keeps it whole — as soon as `_CONDITIONAL_RE` matches
*anywhere* in it:

```python
if _CONDITIONAL_RE.search(normalized) or not _VERDICT_RE.match(normalized):
```

`_CONDITIONAL_RE` matches on markers such as `criteria state`, `only if`,
`will resolve`. A sentence that restates the criteria **and then asserts that the
antecedent obtained** therefore bypasses `_VERDICT_RE` entirely and survives with
the outcome fully disclosed. The residual screen `_RESIDUAL_RE` then classifies
the same survivor as "conditional", which is why the audit reports zero.

## 3. Independent re-audit

`src/audit_redaction_leakage.py` re-detects outcome assertions without consulting
the redactor's own classification: a surviving `resolves YES/NO` mention counts as
a leak unless an unresolved antecedent governs it, and an explicit assertion
marker (`therefore`, `per the`, `that is exactly what happened`,
`the criteria's default applies`, `since no`, `because no`, `correct resolution`)
overrides the hypothetical reading.

**Result: 34 of 256 redacted packets (13.3%) still assert the realized outcome.**
The leak is close to balanced by realized outcome — 20 YES, 14 NO — against a
128/128 pool, so it is not a directional confound at the pool level.

Representative survivors:

| unit | surviving sentence (abridged) |
|---|---|
| `f4e752d2` | "…and that is exactly what happened, **the correct resolution is NO (0)**." |
| `0f63f1fc` | "Per the stated NO conditions (…), **this resolves NO**." |
| `01a607b2` | "Therefore, since no Chipotle restaurant … **the question resolves NO**." |
| `47cc7236` | "…the criteria's default applies: **the question resolves NO**." |
| `009885f8` | "Under the resolution criteria, **the question resolves NO** because oral arguments had not concluded…" |

## 4. Effect on the affected estimates

Every experiment that used `redact_verdicts` was re-estimated on the leak-free
subset, from the existing raw outputs. Nothing was regenerated.

### G12 — paired donor-outcome contrast (YES donor − NO donor, pp)

A pair is dropped if *either* of its two donor packets leaks.

| model | all pairs | leak-free pairs |
|---|---|---|
| Gemma-3-12B | +17.50 [14.73, 20.35] (n=255) | **+16.00 [13.12, 19.03]** (n=192) |
| Llama-3.1-8B | +18.03 [14.33, 21.68] (n=253) | **+17.66 [13.64, 21.76]** (n=189) |
| Qwen3.5-9B | +4.41 [1.32, 7.47] (n=256) | **+3.73 [0.15, 7.35]** (n=192) |
| Mistral-Small-24B | +1.55 [0.56, 2.60] (n=256) | **+1.64 [0.39, 2.93]** (n=192) |

The direction, the ordering across models and the sign of every interval are
unchanged. The G12 result is not an artifact of the leak.

### G2 Experiment B — redaction amplification (`HC_red − HC_direct`, pp)

A unit is dropped if its own redacted packet leaks.

| model | all units | leak-free units |
|---|---|---|
| Qwen3.5-9B | +7.33 [5.80, 8.88] (n=256) | **+8.09 [6.50, 9.81]** (n=222) |
| Gemma-3-12B | +6.91 [5.21, 8.69] (n=255) | **+7.23 [5.35, 9.25]** (n=221) |
| Mistral-Small-24B | +2.72 [1.25, 4.19] (n=256) | **+3.22 [1.58, 4.87]** (n=222) |

The amplification is **larger** on the leak-free subset in all three models, as
the direction of the defect predicts: a surviving verdict makes a "redacted"
packet behave more like an unredacted one, which attenuates the contrast. The
frozen estimate is therefore conservative.

## 5. What this changes, and what it does not

**Changed.** The claim "zero assertive verdicts survive redaction" is withdrawn.
Any statement that the redacted conditions contain *no* explicit outcome must be
replaced by "13.3% of packets retain an outcome assertion; results are reported
both on the full sample and on the leak-free subset."

**Not changed.** No preregistered verdict is revised. G11's `survives` row, G12's
`indeterminate` panel verdict, and G2 Experiment B's
`contamination_survives_redaction: true` all stand, and each is robust to
excluding the leaking units.

**Not repaired in place.** The redactor is not being patched and re-run. Repairing
a frozen instrument after seeing its outputs would convert a disclosed defect into
an undisclosed one. Any future experiment on this question must start from a fresh,
independently audited evidence-only packet set rather than from a regex redactor —
see `SECOND_LEAD_EXPLICIT_OUTCOME_PARADOX.md`.

## 6. Companion correction — Llama boundary-probe reporting

Separately, earlier drafts of `PAPER_FRAME.md` reported the canonical panel as
recognising the time boundary at "97.7–100%". That range mixed measurement scopes.

| model | probes | boundary accuracy |
|---|---|---|
| Qwen3.5-9B | 512 (both frames) | 99.22% |
| Gemma-3-12B | 512 (both frames) | 99.80% |
| Mistral-Small-24B | 512 (both frames) | 100% |
| Llama-3.1-8B | 512 (both frames) | **73.63%** |
| Llama-3.1-8B | 256 (out-of-set frame only) | 97.66% |

Llama's licensed-frame arm is **127/256 = 49.61%**, at chance: it answers `NO` in
both frames rather than tracking the boundary. Reporting Llama's single-frame
97.66% alongside the other models' two-frame figures overstated the panel and is
withdrawn. `results/llama_behavioral_extension_analysis.json` recorded the
per-condition breakdown correctly throughout; the error was confined to the
narrative documents, which have been corrected.
