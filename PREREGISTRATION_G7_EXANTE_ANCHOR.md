# G7 preregistration — Measured against an independent ex-ante forecast

**Created:** 2026-09-01
**Status:** design frozen. Tag `g7-exante-anchor-design-v1`. Written **before
any model output was joined to the anchor field**; the only source contact so
far is the coverage count in §3, which is a property of the dataset and not of
any model.

---

## 1. The sub-question, and the objection it answers

Sub-question of `PAPER_FRAME.md` §1:

> When the future evidence moves the model, does it move it *away from what a
> competent forecaster could have said at the time*?

Every intrusion number in this project so far is a **self-difference**: the
same model, same question, packet present versus absent. That is the right
causal estimand and it is not being replaced. But it invites two objections
that self-differences cannot answer:

1. **"Maybe the WITHOUT cell is noise."** If the uncontaminated answer is not
   itself a sensible ex-ante forecast, the contrast measures a shift away from
   nothing in particular.
2. **"Using the later evidence makes the answer more accurate. So what?"** It
   does — that is not in dispute and never was. The task is not to be right
   about the outcome; it is to say what was warranted before it. Without an
   external ex-ante reference, that distinction is asserted rather than shown.

BTF-3 ships exactly the reference needed: `sota_forecast_probability`, a
proprietary forecasting system's probability produced under the same pastcasting
protocol, i.e. **without** the resolution evidence. It is not ground truth about
what was warranted — no such thing exists — but it is an independent
competent judgment made from the same information set, which is what both
objections require.

**No new generations.** This is a re-analysis of output that already exists,
against a source column that no round has touched.

## 2. Competing readings this separates

- **Displacement.** The packet moves the model away from an independent ex-ante
  judgment while moving it toward the realized outcome. The two move in
  opposite directions, and hindsight is therefore visible as *infidelity to the
  ex-ante state*, not as error.
- **Improvement-only.** The WITHOUT cell is far from the reference too, and the
  packet simply moves an already-poor forecast toward the truth. Under this
  reading the project measures a model that cannot forecast, not one that
  cannot reconstruct.

These make opposite predictions about §4's primary quantity, and the second is
a genuine risk the project has never checked.

## 3. Units and join

The anchor is joined by `question_id` = `independent_unit_id` from
`data/external/raw/btf3/btf3_binary_questions_and_forecasts.parquet`
(SHA-256 recorded in each item's provenance,
`b28f8fe5634f81afa8e4b37d815f875b6e33c24edf590484f1948efea8db051a`).

All 256 frozen units join. **239 of 256 have a non-null
`sota_forecast_probability`** (117 realized-NO, 122 realized-YES); the remaining
17 are excluded, and that exclusion is defined entirely by a source field —
no model output participates in it. Both counts are reported.

## 4. Quantities, fixed now

Write `a_i` for the anchor, `p_i[c]` for the model's answer in cell `c`, and
`r_i ∈ {0,1}` for the realized resolution with `s_i = 2r_i − 1`.

**(V) Instrument validity — reported first, and it can invalidate the rest.**

```text
rho_without = Spearman( p[oob_without], a )        over the 239 units
MAD_without = mean |p[oob_without] - a|
```

Prediction recorded now: `rho_without` is **positive and substantial** — the
uncontaminated cell behaves like an ex-ante forecast rather than noise. If
`rho_without ≤ 0.3` in a model, that model's remaining G7 quantities are
reported but carry an explicit warning that its WITHOUT cell is a weak ex-ante
judgment, and no displacement claim is made from it.

**(D) Displacement from the ex-ante reference — primary.**

```text
Delta_dev = mean( |p[oob_with] - a| ) - mean( |p[oob_without] - a| )
```

paired per unit, 95% percentile cluster bootstrap over `question_id`, 10,000
resamples, seed `20260829`. Positive means the packet moves the model away from
the independent ex-ante judgment.

**(A) Accuracy against the realized outcome — the deliberate contrast.**

```text
Brier[c] = mean ( p[c]/100 - r )^2
Delta_brier = Brier[oob_with] - Brier[oob_without]
```

Prediction recorded now: **`Delta_brier` is negative** — the packet makes the
answer *more* accurate about the outcome. This is expected, is not a finding,
and exists so that the paper can put it in the same table as `Delta_dev` rather
than be asked for it.

**(C) Confidence.** `mean |p[c] - 50|` in each cell, reported descriptively.

**(L) Licensed-frame reference.** All of the above recomputed for
`allowed_with` / `allowed_without`, where movement toward the outcome is
licensed and expected. It is a reference column, not a test.

## 5. Decision rules

- **Displacement established** for a model if `Delta_dev ≥ 3.0` points and its
  95% CI excludes 0. The 3.0-point SESOI is half the intrusion SESOI, because
  shifting an answer by `x` points changes `|p − a|` by at most `x` and
  typically by less.
- **No displacement** if the CI lies within `[−3.0, +3.0]`.
- Anything else is indeterminate.
- Panel rule: ≥ 2 of 3 published models for the headline; the G4 breadth panel
  is reported as an extension once its outputs exist.

### Interpretation table, fixed in advance

| `Delta_dev` | `Delta_brier` | permitted conclusion |
|---|---|---|
| displacement | negative | The packet makes the model **more accurate about the outcome and less faithful to what was knowable**. This is the sentence the paper is allowed to write, and it is the point of the whole project. |
| displacement | ≥ 0 | Displacement without accuracy gain. Report both; it strengthens the infidelity claim and is not what we predicted. |
| no displacement | any | The packet does not move the model away from an independent ex-ante judgment. The self-difference result stands unchanged, but the paper may **not** claim infidelity to the ex-ante state, only sensitivity to unlicensed evidence. |
| indeterminate | any | Report the interval; conclude nothing. |

## 6. What this does not do

- It does **not** treat the anchor as ground truth. It is one competent system's
  ex-ante probability, produced by a proprietary method we cannot inspect, and
  the paper says so wherever it appears.
- It does **not** re-define `OutOfSetIntrusion`. The self-difference remains the
  primary estimand of the paper; this is corroboration from an independent
  reference.
- It does **not** select, drop, or re-review units on any model-dependent basis.
- It does **not** claim the model should match the anchor. Matching is not the
  target; the target is not being moved by evidence that did not exist yet.

## 7. Freeze checklist

- [x] `PREREGISTRATION_G7_EXANTE_ANCHOR.md` committed
- [x] `src/analyze_exante_anchor.py` committed
- [x] `tests/test_exante_anchor.py` committed and passing
- [ ] `g7-exante-anchor-design-v1` tagged
- [ ] first join of model output to the anchor only after the tag exists
