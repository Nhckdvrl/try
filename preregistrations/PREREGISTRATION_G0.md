# G0 preregistration — frozen before any Exclude condition was run

**Frozen:** 2026-08-27, commit of `data/items/frozen_v1.json`.

## What had been run at freeze time
Only `base`, `admit_pre`, `admit_post` and `rule_probe_admit_post`, on Qwen3-8B.
The `exclude_pre` / `exclude_post` conditions had never been generated or run for
any model. It is therefore structurally impossible for the Unring-the-Bell effect
to have entered the dataset through item selection.

## Readout (fixed at freeze time)
* Four rating families: the model writes at most two sentences of greedily decoded
  rationale, then the answer is read as the **expectation of the next-token
  distribution over the digits 0-9** at the fixed position after `ANSWER: `,
  rescaled to 0-100. Deterministic, continuous, no parsing, no LLM judge.
* `numeric_aggregation`: same rationale stage, then a greedy numeric parse.
* Rule and memory probes are always **separate calls** so they cannot act as an
  extra reminder inside a decision run.

Two readouts were piloted and rejected before freezing, both on Base/Admit only:
a greedy 0-100 integer (values collapsed onto 20/45/65/85) and a one-token 0-9
answer with no rationale (on `ranking_selection` the model reasons to 0 and emits
9 with p=0.98). Both rejections are recorded in `logs/` and in `FINDINGS.md`.

## Screening rules (applied to Qwen3-8B Base/Admit only)
1. `base` not at floor/ceiling: within [15, 85] on the 0-100 scale; for the
   numeric family, `|base - mean(valid readings)| <= 0.75 x naive_shift`.
2. Evidence leverage: `sign(direction) * (admit - base) >= 8` points; for the
   numeric family `>= 0.40 x naive_shift`.
3. Direction stability: no reversal in either admit order (ties allowed, since
   ratings are quantised).
4. Rule comprehension under Admit: `p(YES) >= 0.80` on the independent probe.

144 of 180 items survived. `admit = mean(admit_pre, admit_post)`.

## Metrics
* `L = Y_admit - Y_base`, `s = sign(L_intended)`, `D_c = s (Y_c - Y_base)`,
  `REI_c = D_c / |L|`.
* Temporal asymmetry: `Delta_time = REI_post - REI_pre`.
* Order-adjusted interaction:
  `UTB = s[(Y_ExcludePost - Y_ExcludePre) - (Y_AdmitPost - Y_AdmitPre)]`.

## Hypotheses
* **H1** Rule knowledge: `p(NO)` on the independent exclude probe is high.
* **H2** Residual influence: `REI_post > 0`, not driven by a few extreme items.
* **H3** Temporal asymmetry: `REI_post > REI_pre`.
* **H4** Not a mere order effect: `UTB > 0`.
* **H5** (secondary) `true_but_forbidden` shows more residue than
  `false_or_unreliable`.

Inference: item-level paired bootstrap (10,000 resamples), percentile CIs,
computed per family and pooled. Items are weighted equally; REI is winsorised at
+/-3 for reporting robustness and the unwinsorised version is reported alongside.
