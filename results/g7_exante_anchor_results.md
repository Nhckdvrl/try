# G7 ex-ante anchor — results

**Design tag:** `g7-exante-anchor-design-v1`, frozen before any join of model
output to the anchor column. No new generations. Analysis:
`results/g7_exante_anchor_analysis.json`.

Anchor: `sota_forecast_probability` from
`btf3_binary_questions_and_forecasts.parquet` — a proprietary forecasting
system's probability produced under the same pastcasting protocol, without the
resolution evidence. Present for **239 of the 256 frozen units** (117
realized-NO, 122 realized-YES); the 17 exclusions are defined by the source
field alone.

## The preregistered test did not pass, and it failed in the opposite direction

| model | n | `rho_without` | MAD without | MAD with | `Δ_dev` (95% CI) | verdict |
|---|---:|---:|---:|---:|---|---|
| Qwen3.5-9B | 239 | 0.281 | 26.56 | 19.72 | **−6.84 [−9.18, −4.55]** | indeterminate |
| Gemma-3-12B-it | 238 | 0.293 | 27.53 | 18.26 | **−9.27 [−12.61, −5.81]** | indeterminate |
| Mistral-Small-24B | 239 | 0.329 | 25.04 | 20.43 | **−4.61 [−6.51, −2.77]** | indeterminate |

`Δ_dev` was predicted to be **positive** — the packet moving the model away
from an independent competent ex-ante judgment. It is negative in all three
models: the packet moves the answers **closer** to the anchor.

**Panel verdict: indeterminate. Nothing is concluded from the displacement
test, exactly as the frozen rule requires.**

## The validity check explains it, and it is the more important number

`rho_without` — the Spearman correlation between the model's uncontaminated
answer and the independent ex-ante forecast — is **0.28, 0.29, 0.33**. Two of
three models sit below the preregistered 0.3 validity floor.

The uncontaminated cell is a **weak ex-ante forecast**. The models sit near the
middle of the scale (`|p − 50|` = 13.8 / 13.8 / 18.4) while the anchor is
confident and directionally right (mean 16.3 on realized-NO, 62.5 on
realized-YES). Against the anchor the models are systematically
under-committed: the outcome-aligned signed gap `s·(p − a)` is **−19.2 / −19.4
/ −19.0** points in the WITHOUT cell.

So on this measure the packet does not push the model away from a good ex-ante
judgment — it pushes a hedged, weakly informative judgment toward one that is
both closer to the anchor and closer to the truth.

## Accuracy against the realized outcome, as predicted

| model | Brier without | Brier with | `Δ_brier` |
|---|---:|---:|---|
| Qwen3.5-9B | 0.2364 | 0.1187 | −0.1177 [−0.1344, −0.1012] |
| Gemma-3-12B-it | 0.2393 | 0.0732 | −0.1660 [−0.1879, −0.1447] |
| Mistral-Small-24B | 0.2587 | 0.2266 | −0.0321 [−0.0520, −0.0130] |

Negative in all three, as recorded in advance. The packet makes the answers
more accurate about the outcome. That was never in dispute and is not a
finding.

## What this changes about what the paper may claim

**Removed.** The paper may **not** write any version of "hindsight makes the
model less faithful to what was knowable, as judged against an independent
ex-ante reference." That sentence was the intended payoff of this round and it
is not supported.

**Unchanged.** The self-difference estimand is untouched. `OutOfSetIntrusion`
is a within-item causal contrast — same model, same question, packet present
versus absent — and nothing here bears on it. The recognition–enforcement
dissociation, its 256-unit replication, its survival under verdict redaction,
its persistence across scale, and the G3 finding that no stated reason moves it
all stand exactly as reported.

**Added, and it must go in the limitations.** These models are not strong
pastcasters on BTF-3. Their uncontaminated answers correlate only ~0.3 with a
competent ex-ante forecast and are hedged toward 50. A reader is entitled to
know that the judgment being contaminated is a weak one to begin with. Finding
this ourselves is better than having a reviewer find it.

## One descriptive observation, not preregistered

The analyzer also computes the outcome-aligned signed gap to the anchor, which
§4 of the preregistration lists only implicitly. It is reported here as
descriptive and post hoc, and no claim rests on it: WITHOUT → WITH moves the
signed gap from −19.2 to −3.5 (Qwen), −19.4 to **+7.7** (Gemma), and −19.0 to
−11.6 (Mistral). Gemma is the one model that crosses the anchor and ends up
*more* outcome-aligned than a forecaster who could not see the outcome. That is
suggestive of overshoot rather than repair, but with one model and no
preregistration it is an observation and nothing more.
