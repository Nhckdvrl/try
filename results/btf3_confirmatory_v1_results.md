# BTF-3 confirmatory replication — results

**Freeze tag:** `g1-btf3-confirmatory-freeze-v1` (commit `45cae52`). All
three model outputs were generated at commit `45cae523fb56233b8d63798e34cf2a7ec763dcf2`
against `data/external/review/btf3_temporal_confirmatory_v1.jsonl`
(SHA-256 `850b40f6bb46f390fd3f59d4bcdb8ea50672cc0a299d48deedbd0b83384f273c`),
64 fresh independent `question_id` (32 realized NO / 32 realized YES), none
reused from the 8-unit pilot.

## Execution check

All three files: decision parse rate `1.0`, boundary-probe accuracy `1.0`,
zero invalid outputs — comfortably above the confirmatory floor
(`248/256` and `112/128` respectively). Longest prompt 4,197 tokens
(Gemma), well inside the frozen `max_model_len=8192`.

## Per-model results (`results/btf3_confirmatory_v1_analysis.json`)

| model | qualified | responsiveness (mean, 95% CI) | intrusion (mean, 95% CI) | intrusion pass |
|---|---|---|---|---|
| Qwen3.5-9B | yes | 44.4 [39.5, 49.1] | 12.75 [8.5, 17.0] | **yes** |
| Gemma-3-12B-it | yes | 49.2 [44.6, 53.8] | 27.2 [22.0, 32.3] | **yes** |
| Mistral-Small-24B | yes | 38.9 [31.9, 45.6] | 3.3 [-1.2, 7.6] | no |

**`qualified_models: 3/3`, `intrusion_pass_models: 2/3`,
`panel_complete: true`, `btf3_temporal_replicates: true`.**

## Interpretation

The pilot-level pattern replicates cleanly on a fresh, independently-drawn,
4x larger, held-out sample: all three models qualify (perfect parse rate,
perfect boundary-probe accuracy, strong responsiveness, perfect or
near-perfect aligned `ALLOWED_WITH` score), and the same two models that
showed intrusion in the pilot (Qwen, Gemma) show it again here, with
much tighter confidence intervals (as expected at n=64 vs n=8) and
comparable point estimates (Gemma's intrusion mean is essentially
unchanged: 27.2 vs the pilot's 26.25, similar magnitude; Qwen's came down
somewhat, 12.75 vs 16.25, but its CI lower bound is still comfortably
clear of the 5-point SESOI). Mistral again qualifies but does
not show intrusion (CI crosses zero, same as the pilot's [-7.5, 10.0]).

Per `PREREGISTRATION_G1.md`'s confirmatory stop/go rule: **BTF-3 temporal
information-set intrusion replicates.** This is not the pilot's
two-family broad gate (FANToM failed qualification in the pilot, and the
parallel SCOTUS second-source search failed its own calibration gate
before any sample existed) — it is confirmation that the temporal-boundary
finding itself is not a pilot-scale artifact.

## What this does and doesn't authorize next

Per the frozen mechanism gate in `PREREGISTRATION_G1.md`, external causal
patching still requires the same model to show validated intrusion in **at
least two families** (boundary types — temporal, perspective, procedural
— not sources/datasets within one family), which remains unmet: only the
temporal family has confirmed intrusion, and the project is deliberately
not narrowing back to perspective/procedural to chase that old gate. A
second independent temporal-boundary **source** (e.g. a future FOMC
replication) would not unlock this gate either way — it would instead
answer a different, more immediate question: whether the confirmed
intrusion is specific to BTF-3's forecasting-question construct or
generalizes to a genuinely different kind of temporal decision. That
question, not mechanism work, is the deliberate next priority.
