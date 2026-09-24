# VitaminC exclusion pilot r1 — spec v2

- Date: 2026-09-25. **Supersedes spec_v1** (both written before ANY model
  output; v1's selection rule and gate semantics are replaced by the user's
  second ruling pass, recorded here). No model output exists at this point.
- Status per user: **SERIOUS EXPLORATORY — absolutely not prereg-ready.**
- Speed directive: 600 rows, kill once; alive → +400 rows, kill again. No
  further engineering polish before the first model output.

## RQ (answer must not be baked into the question)

> When instructed to exclude evidence, does an LLM remove that evidence's
> contribution, merely attenuate, or reverse it as if it were
> counter-evidence?

## Estimand (unified sign convention, both sides)

- `A_S = Y_S − Y_0`, `A_R = Y_0 − Y_R` (pure evidence effects, stage 1a).
- `C^S_pre = Y_EXCL-pre(S) − Y_0`, `C^R_pre = Y_0 − Y_EXCL-pre(R)` (stage 1b).
- In both pairs, **positive = the target evidence still pushes the decision in
  its own direction (leakage), 0 = removal, negative = inversion.**
- `Y` = digit-expectation readout ×100/9 (0–100, continuous).
- The REFUTES evidence certifies that the negative direction is the correct
  counter-evidence direction of this natural contrast; it is **not** a
  symmetric distance anchor (the Y0/Y+/Y− geometry is asymmetric).

## User rulings (2026-09-25, second pass — this is the operative set)

1. Model: **mistral-small-24b local**, one model. Exploratory; phenomenon
   first, representativeness later.
2. Selection (replaces v1's file-order+0.80): train → real → canonical 1S+1R
   → **sim ≥ 0.90** → **normalized dedup** → **non-template claims** →
   **at most 1 row per revision/case** → **fixed-seed random sample of 200**.
   200, not 300.
3. Stage-1a gate semantics (replaces v1's G1/G2/G3): per item usable iff
   `A_S ≥ 10 AND A_R ≥ 10`; continue iff **≥ 120 of 200 usable**; **< 120 →
   KILL VitaminC route** — no threshold change, no resampling, no selector
   swap to rescue.
4. Stage-1b continuation gate (frozen BEFORE the +400 runs): treat inversion
   as a serious phenomenon — and only then is `EXCL_post(S/R)` (+400, a
   future stage) justified — iff **mean(C^S_pre) ≤ −3 AND mean(C^R_pre) ≤ −3**.
   - `C_pre > 0` on both sides → attenuation/leakage only → **headline KILL.**
   - Only one side ≤ −3 → **no inversion story**; first suspects are
     truth-prior / floor-ceiling / label asymmetry.
5. Flow: 600 rows → gate → alive → auto +400 (`EXCL_pre(S)`, `EXCL_pre(R)`)
   → evaluate continuation gate → report 1000. Post cells do NOT run in this
   pilot.

## Data (mechanical filter chain, in order — pool_v2)

Source: `data/external/raw/vitaminc/train.jsonl` (sha256
`7461c6fd1a13459590317c5ccdc8651dd2daf7c1ad8ae4b10ccd88d164fccd5a`).

- **F1** `revision_type == "real"`; label in {SUPPORTS, REFUTES, NOT ENOUGH
  INFO}; claim and evidence non-empty.
- **F2** group by `(case_id, claim)`; exactly one SUPPORTS row and exactly one
  REFUTES row, evidence texts different (canonical 1S+1R).
- **F3** `difflib.SequenceMatcher(..., autojunk=False).ratio()` over
  whitespace-tokenized evidence pair ≥ **0.90**.
- **F4** normalized-dedup key on the claim:
  `re.sub(r"\s+", " ", claim).strip().casefold().rstrip(" .")` — keep first
  occurrence (file order).
- **F5** non-template: drop claims matching
  `(?i)(less than|more than|fewer than|over|under|at least|at most)\b[^.]{0,20}\d`
  (the audit's D4 regex).
- **F6** at most one qualifying claim per `case_id` (revision) — keep first.
- **F7** fixed-seed sample: `random.Random(20260925).sample(candidates, 200)`
  over the candidate list in first-encounter file order; selected items are
  then sorted by `train_first_lineno` for `pilot_id` assignment. Deterministic,
  never effect-sorted.

Output: `results/pilots/vitaminc_pilot_r1/pool_v2.jsonl` (fields unchanged
from v1: `pilot_id, case_id, claim, evidence_s, evidence_r, sim, page,
train_first_lineno`). Pool sha256 recorded in the run report. `pool_v1.jsonl`
is superseded and unused.

## Prompt template (frozen — identical to spec v1, G0/G24A lineage verbatim)

- `SYSTEM`, `QUESTION`, `OUTPUT_SPEC`, reasoning tail: byte-identical to
  spec v1 §"Prompt template".
- `RULING` block: `RULING\nThe evidence shown below is excluded. It must not
  influence your final judgment.`
- User prompt = `"\n\n".join(blocks) + "\n\nTASK\n" + QUESTION + "\n" +
  OUTPUT_SPEC + "\n" + tail`; messages `[SYSTEM, user]` through the chat
  template with `add_generation_prompt=True` (mirrors `src/run_model.py`).

| cell | blocks |
| --- | --- |
| `y0` | `CLAIM\n{claim}` |
| `yplus` | `EVIDENCE\n{evidence_s}` + `CLAIM\n{claim}` |
| `yminus` | `EVIDENCE\n{evidence_r}` + `CLAIM\n{claim}` |
| `exclpre_plus` | `RULING` + `EVIDENCE\n{evidence_s}` + `CLAIM\n{claim}` |
| `exclpre_minus` | `RULING` + `EVIDENCE\n{evidence_r}` + `CLAIM\n{claim}` |

Stage-1a = `y0, yplus, yminus` (600 rows). Stage-1b = `exclpre_plus,
exclpre_minus` (+400). `EXCL_post` is OUT of scope for this pilot.

## Engine (frozen — identical to spec v1)

- `LLM(model="data/mistral_small_24b_hf", tp=1, gpu_memory_utilization=0.85,
  max_model_len=2048, dtype=bfloat16, max_logprobs=40, disable_log_stats=True)`.
- Stage 1: `temp=0, max_tokens=110, stop=["ANSWER:"]`.
- Stage 2: append `rationale.rstrip() + "\nANSWER: "`, `temp=0, max_tokens=1,
  logprobs=40` → digit expectation over 0–9 tokens ×100/9.

## Gates (mechanical — evaluated by the pilot analyzer, printed as numbers)

- **Stage-1a**: `n_usable = |{items: A_S ≥ 10 and A_R ≥ 10}|`; **≥ 120 →
  continue, < 120 → KILL** (route closed; no rescue moves).
- **Stage-1b**: `mean(C^S_pre)` and `mean(C^R_pre)` both ≤ −3 → inversion is
  serious (would justify the future `EXCL_post` stage); both > 0 → headline
  KILL (attenuation/leakage only); mixed/one-sided → no inversion story
  (truth-prior / floor-ceiling / label asymmetry first).
- Also reported (not gates): full A_S/A_R/C distributions, per-side fraction
  of usable/inverted items, unparsed/mass/truncation counts.

## Banned until the user lifts them

tokenizer work; filler; bootstrap; multi-model; prereg; elaborate analyzer;
thousands of manual audits; any post-hoc gate/threshold/seed change; running
`EXCL_post` before the continuation gate passes and the user rules; G26A
Phase B (any form); touching frozen G26A files.

## Known limitations (stated upfront)

- One model, one prompt phrasing, temp 0 — pilot grade by construction.
- Template claims are excluded by rule (F5), so the pool covers only the
  ~54% non-template claim style; results generalize to that subset.
- No floor/ceiling model is fitted; distributions are reported instead.
