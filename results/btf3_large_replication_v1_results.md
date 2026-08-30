# BTF-3 Large Replication v1 — results

**Freeze tag:** `g1-btf3-large-replication-freeze-v1`. All three model outputs
were generated against
`data/external/review/btf3_temporal_large_replication_v1.jsonl` (SHA-256
`0b6fd8d0304f6b7cde336a6518b1058983a9b93529e90cbb577d1878acf0901d`): **256
entirely fresh `question_id`, 128 realized YES / 128 realized NO**, none of
which appears in the 8-unit pilot, the 64-unit confirmatory sample, or even the
prior confirmatory candidate queue.

## Execution check

| model | decision parse rate | boundary-probe accuracy | complete units |
|---|---|---|---|
| Qwen3.5-9B | 1024/1024 | 508/512 (99.22%) | 256 |
| Gemma-3-12B-it | 1023/1024 (99.90%) | 511/512 (99.80%) | 255 |
| Mistral-Small-24B | 1024/1024 | 512/512 (100%) | 256 |

All comfortably above the preregistered floors (`992/1024`, `448/512`).
Longest prompt 4,197 tokens against the frozen 8,192 budget; the full pre-run
token census over all 4,608 prompts passed with no truncation.

## Per-model results (`results/btf3_large_replication_v1_analysis.json`)

| model | qualified | responsiveness (95% CI) | `OutOfSetIntrusion` (95% CI) | intrusion pass |
|---|---|---|---|---|
| Qwen3.5-9B | yes | 47.27 [44.0, 50.6] | **16.02 [14.18, 17.89]** | **yes** |
| Gemma-3-12B-it | yes | 46.89 [43.6, 50.2] | **27.73 [25.15, 30.39]** | **yes** |
| Mistral-Small-24B | yes | 39.31 [35.5, 43.1] | **7.46 [5.41, 9.57]** | **yes** |

**`qualified_models: 3/3`, `intrusion_pass_models: 3/3`, `panel_complete: true`,
`btf3_large_replication_v1: true`.**

## What replicated, and what changed

The preregistered gate is met by the 256 units alone — no pooling was needed
and none was used to reach this verdict. Two things are worth stating plainly:

1. **Recognition is at ceiling while enforcement is not.** Boundary-probe
   accuracy is 99.2–100%: these models can say, per item, that the packet lies
   outside the target information set. They are nonetheless moved by it, by
   7.5 to 27.7 probability points.
2. **Mistral crossed the line this time.** On the 64-unit confirmatory sample
   Mistral's intrusion was 3.28 [-1.17, 7.58] — not clearing the 5-point
   SESOI. On 256 units it is 7.46 [5.41, 9.57], clearing it. The
   round-stratified contrast (`results/btf3_cross_round_replication.json`,
   secondary and non-gating) puts the change at +4.18 [-0.53, 8.92]: consistent
   with a stable underlying effect estimated more precisely, not with a
   demonstrated increase. The honest reading is that Mistral's effect was
   always small and the 64-unit sample could not resolve it.

## Cross-round stability (secondary, non-gating)

| model | confirmatory (n=64) | large replication (n=256) | Δ = large − confirmatory | pooled (n≈320) |
|---|---|---|---|---|
| Qwen3.5-9B | 12.75 [8.50, 16.98] | 16.02 [14.18, 17.89] | +3.27 [-1.44, 7.98] | 15.36 |
| Gemma-3-12B-it | 27.20 [22.00, 32.34] | 27.73 [25.15, 30.39] | +0.53 [-5.43, 6.41] | 27.63 |
| Mistral-Small-24B | 3.28 [-1.17, 7.58] | 7.46 [5.41, 9.57] | +4.18 [-0.53, 8.92] | 6.62 |

Every Δ interval contains zero: no model contradicts its own earlier estimate.
The pooled column excludes the 8 discovery-pilot units and is descriptive only
— it played no part in the replication verdict, exactly as preregistered.

## Standing caveats

- The 256-unit human review was LLM-assisted and conducted without external
  lookup, which its ledger states. That gap is now closed by a completed
  audit against real citations on a hash-fixed 64-item subsample
  (`results/btf3_factuality_audit_v1_results.md`): 63 PASS, 1 material error,
  0 unverifiable (1/64, exact 95% CI [0.04%, 8.40%]), below the preregistered
  expanded-review trigger. The single error is a question/criteria window
  contradiction, not a fabricated event, and excluding that unit moves no
  model's estimate materially (e.g. Qwen 16.02 → 15.92). Sample membership is
  unchanged, as the protocol requires.
- Most packets state the outcome explicitly, so this round on its own cannot
  distinguish evidence integration from reading a revealed label. That is what
  the verdict-redaction experiment in `PREREGISTRATION_G2_HINDSIGHT_DEPTH.md`
  is for.
