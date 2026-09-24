# VitaminC exclusion pilot r1 — spec v1

- Date: 2026-09-25 (written BEFORE the pool file and BEFORE any model output).
- Status per user: **SERIOUS EXPLORATORY — absolutely not prereg-ready.**
- This is a cheap pilot document, not a preregistration. It exists so that the
  selection rule, prompts, gates and flow are frozen before any output exists.
  Any change after the first model output requires a new version + erratum and
  the runs are not comparable.

## RQ (user's phrasing — the answer must not be baked into the question)

> When instructed to exclude evidence, does an LLM remove that evidence's
> contribution, merely attenuate it, or reverse it as if it were
> counter-evidence?

## Estimand (user-defined)

- `s = +1` if the target evidence is the SUPPORTS row of the pair, `s = -1`
  if it is the REFUTES row (defined by label, not by revision orientation).
- `C_excl = s * (Y_excl - Y0)`, where `Y` is the digit-expectation readout on
  the 0–100 scale.
- `C_excl > 0` → leakage / retention; `C_excl ≈ 0` → removal;
  `C_excl < 0` → inversion (the interesting structural error).
- Role of `Y-`: it certifies that the negative direction is the correct
  counter-evidence direction for this natural contrast. It is **not** a
  symmetric distance anchor — the `Y0 / Y+ / Y-` geometry is asymmetric
  (parametric priors), and distance-to-anchors would lie.

## User rulings (2026-09-25) — four, all executed verbatim below

1. Model: **mistral-small-24b, local weights**, one model only.
2. Selection: **train file order, first 200 qualifying pairs**, evidence-pair
   token similarity ≥ 0.80, canonical 1S+1R, dedup by claim text (keep first).
3. Stage-1a gates (0–100 scale), fixed NOW:
   - **G1**: median(Y+ − Y0) ≥ **+10**
   - **G2**: median(Y0 − Y−) ≥ **+10**
   - **G3**: ≥ **60%** of items strictly ordered `Y+ > Y0 > Y−`
   Any gate red → **immediate KILL of the VitaminC route, no rescue.**
4. Flow: all gates green → **auto-run +400 rows** (`EXCL_pre(E+)`,
   `EXCL_pre(E−)`) and report the full 1000; any gate red → stop, report KILL.

## Data (mechanical filter chain, in order)

Source: `data/external/raw/vitaminc/train.jsonl` (sha256
`7461c6fd1a13459590317c5ccdc8651dd2daf7c1ad8ae4b10ccd88d164fccd5a`, pinned via
`scripts/fetch_external_sources.py`; audit: results/audits/vitaminc_triplet_audit_v1.json).

- **F1** keep rows with `revision_type == "real"` (synthetic excluded by rule).
- **F2** group by `(case_id, claim)`; keep groups with **exactly one** SUPPORTS
  row and **exactly one** REFUTES row, evidence texts different (canonical 1S+1R).
- **F3** `difflib.SequenceMatcher(..., autojunk=False)` ratio over
  whitespace-tokenized evidence pair ≥ **0.80**.
- **F4** dedup by exact claim text; keep first occurrence.
- **F5** take the **first 200** groups in train file order (group position =
  line number of its first row). Deterministic; never effect-sorted.

Output: `results/pilots/vitaminc_pilot_r1/pool_v1.jsonl`, 200 rows,
fields `pilot_id` (`p0001..p0200`), `case_id`, `claim`, `evidence_s`
(SUPPORTS text), `evidence_r` (REFUTES text), `sim`, `page`. sha256 recorded
in the run report.

## Prompt template (frozen — G0/G24A lineage constants verbatim)

- `SYSTEM` = "You are a careful decision maker. Follow every instruction in the
  context exactly. Answer with the requested format and nothing else."
- `QUESTION` = "Considering everything above, rate the likelihood that the
  claim is true."
- `OUTPUT_SPEC` = "Use a scale from 0 to 9, where 0 means certainly false and
  9 means certainly true."
- reasoning tail (mode=reasoned) = "Think in at most two short sentences. Then
  write a final line of exactly this form:\nANSWER: <your answer>"
- Blocks joined with `\n\n`; user prompt = `blocks + "\n\nTASK\n" + QUESTION +
  "\n" + OUTPUT_SPEC + "\n" + tail`. Messages = `[SYSTEM, user]` through the
  model's chat template with `add_generation_prompt=True`
  (mirrors `src/run_model.py::chat_ids`).
- `RULING` block (byte-fixed for this pilot):
  `RULING\nThe evidence shown below is excluded. It must not influence your
  final judgment.`

Cells (headers uppercase, layout as listed):

| cell | blocks |
| --- | --- |
| `y0` | `CLAIM\n{claim}` |
| `yplus` | `EVIDENCE\n{evidence_s}` + `CLAIM\n{claim}` |
| `yminus` | `EVIDENCE\n{evidence_r}` + `CLAIM\n{claim}` |
| `exclpre_plus` | `RULING` + `EVIDENCE\n{evidence_s}` + `CLAIM\n{claim}` |
| `exclpre_minus` | `RULING` + `EVIDENCE\n{evidence_r}` + `CLAIM\n{claim}` |

Stage-1a = `y0, yplus, yminus` (200×3 = **600 rows**). Stage-1b (only after
gates green) = `exclpre_plus, exclpre_minus` (+400 rows).

## Engine (frozen)

- `LLM(model=local mistral shim, tensor_parallel_size=1,
  gpu_memory_utilization=0.85, max_model_len=2048, dtype=bfloat16,
  max_logprobs=40, disable_log_stats=True)`; prompts passed as token ids.
- Stage 1 (rationale): `temperature=0, max_tokens=110, stop=["ANSWER:"]`.
- Stage 2 (readout): append `rationale.rstrip() + "\nANSWER: "`,
  `temperature=0, max_tokens=1, logprobs=40` → **digit expectation over token
  positions 0–9, rescaled ×100/9** (`digit_expectation_0_100`, the G0/G24A
  readout used by G25A/G26A). Continuous, deterministic, no parsing.
- Per row recorded: `pilot_id, cell, kind="digit", reasoning,
  reason_truncated, raw, value, mass, readout, model_tag`.

## Stage-1a gates (mechanical, evaluated by the pilot analyzer)

Computed over items with all three values present (`n_complete` reported;
any anomaly < 200 stops for user review — it would mean unparsed readouts,
which the digit expectation should never produce):

- **G1** median(yplus − y0) ≥ +10.0 → else KILL
- **G2** median(y0 − yminus) ≥ +10.0 → else KILL
- **G3** count(yplus > y0 AND y0 > yminus) / n_complete ≥ 0.60 → else KILL

KILL means: no +400 stage, no rescue, no threshold changes, route closed
until the user reopens it.

## Stage-1b reporting (no numeric gate — user set none)

Report only: per side, median/mean of `C+ = +(exclpre_plus − y0)` and
`C− = −(exclpre_minus − y0)`, fraction of items with `C < 0`, and the joint
quadrants against the pure-evidence effects. Interpretation rules (user's,
recorded verbatim in intent):

- If all that shows is attenuation (`Y0 < Y_excl < Y+`) → **not a headline
  RQ**; at most "another quantification of RQ1"; stop.
- If inversion appears on one side only → first suspects are response
  floor/ceiling, truth prior, label bias — **no story** before those are
  checked.
- The attractive finding would be `C_pre < 0` on a substantial fraction of
  items, on both sides, symmetric — later contrasted with retrospective
  `C_post ≈ 0` (retrospective cells are NOT in this pilot).

## Banned until the user lifts them

tokenizer work; filler; bootstrap; multi-model; prereg; elaborate analyzer;
thousands of manual audits; any post-hoc gate/threshold change; G26A Phase B
(any form); touching frozen G26A files.

## Known limitations (stated upfront)

- ~46% of VitaminC claims are threshold-template style (audit D4).
- One model, one prompt phrasing, temp 0 — pilot grade by construction.
- Digit-expectation prompt is 0–9; the readout is continuous on 0–100.
- No floor/ceiling model is fitted; distributions are reported instead.
