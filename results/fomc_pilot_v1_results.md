# FOMC 12+12 source-qualification pilot — results

**Freeze tag:** `g1-fomc-pilot-freeze-v1`. All three model outputs generated
against `data/external/review/fomc_temporal_pilot_v1.jsonl`
(SHA-256 `d628ee999424bc6c8820089e5244c850c45d377da20808cb63aba2e97e7020e4`),
24 units (12 CHANGE / 12 HOLD), meeting-disjoint, human-reviewed per the
frozen four-gate protocol.

## Execution check

All three files: decision parse rate `1.0`, boundary-probe accuracy `1.0`,
zero invalid outputs — comfortably above the pilot floor (`93/96` and
`42/48` respectively). Longest prompt 2,301 tokens (Mistral), well inside
`max_model_len=8192`.

## Per-model results (`results/fomc_pilot_v1_analysis.json`)

Primary analysis clusters the bootstrap by **next-meeting calendar year**
(14 distinct years across the 24 units), per the contract's frozen choice
to account for FOMC's real serial dependence. Secondary (sensitivity-only)
clustering is per-unit, matching BTF-3/SCOTUS's own treatment.

| model | qualified | mean_allowed | responsiveness (year-clustered) | intrusion (year-clustered) | intrusion (unit-clustered, secondary) | intrusion pass |
|---|---|---:|---|---|---|---|
| Qwen3.5-9B | yes | 78.75 | 16.8 [3.9, 31.7] | 9.0 [-3.8, 23.9] | 8.1 [-2.5, 19.4] | no |
| Gemma-3-12B-it | **no** (responsiveness 11.7 < 15) | 75.4 | 11.7 [1.9, 21.2] | 7.2 [0.8, 16.3] | 6.0 [0.8, 12.3] | no |
| Mistral-Small-24B | yes | 92.5 | 20.6 [7.5, 35.0] | 10.7 [2.0, 23.0] | 11.5 [4.6, 19.8] | no |

**`qualified_models: 2/3`, `intrusion_pass_models: 0/3`,
`panel_complete: true`, `fomc_temporal_pilot_qualifies: false`.**

## Interpretation

**By the frozen gate, this pilot does not qualify**: the source-qualification
rule requires at least 2/3 models to qualify *and* at least 2/3 qualified
models to pass the intrusion criterion. 2/3 qualify (Qwen, Mistral; Gemma
misses only on responsiveness, 11.7 vs the 15-point floor), but 0/3 clear
the intrusion SESOI under the primary year-clustered bootstrap.

This is not a clean dead end the way SCOTUS was — every model's intrusion
point estimate is positive and of a similar order of magnitude to BTF-3's
confirmed effect (7–11 points here vs. 12.75–27.2 in the BTF-3
confirmatory run), and under the secondary (non-primary) unit-clustered
analysis, Mistral's 95% CI lower bound (4.6) sits just under the 5-point
SESOI and Gemma's (0.8) is directionally positive. The primary
year-clustered analysis is wider specifically because it is the more
conservative, contract-mandated choice — treating 24 observations as only
14 effectively independent year-clusters rather than 24 independent
units, precisely to avoid overstating precision given FOMC's serial
dependence (Threat 4). At N=24 split across CHANGE/HOLD and 14 years,
that conservatism costs real statistical power.

## What this does and doesn't authorize next

Per `FOMC_TRANSFORMATION_CONTRACT.md`'s Scope section, **a fresh, larger
confirmatory freeze is authorized only if this pilot qualifies** — it did
not, so that is not automatically authorized by this result. This is a
genuine judgment call for the next decision, not something this analysis
resolves on its own: the point estimates are directionally consistent
with BTF-3 and plausibly underpowered at this sample size given the
conservative primary clustering, but the frozen gate's own bar was not
met. Options consistent with the project's existing discipline (not
decided here): treat FOMC as inconclusive at pilot scale and stop:
temporal-specific factorization at BTF-3 confirmatory scale (uncontested,
already-qualified evidence) without further FOMC investment; or revisit
whether a larger disjoint FOMC sample (the census showed 21 disjoint
CHANGE and 41 disjoint HOLD are available in principle, well beyond this
pilot's 12+12) would resolve the power question — but that would be a new
decision requiring its own justification, not something the frozen
12+12 gate itself authorizes.
