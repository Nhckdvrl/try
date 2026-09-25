# G24A data-quality audit v1 (line-by-line, integrity only)

Generated 2026-09-25 12:56:56 — 99.5s. Scope: data integrity. **No scientific gates, no findings selection** — section D is observation only and can never fail the audit.

**Verdict: INTEGRITY OK**

## 0. Prereg literals vs code constants

| constant | prereg text == code |
|---|---|
| ADMIT_RULE | OK |
| EXCLUDE_RULE | OK |
| QUESTION | OK |
| OUTPUT_SPEC | OK |
| RULE_PROBE_QUESTION | OK |
| CLAIM_HEADER | OK |
| EVIDENCE_HEADER | OK |
| TAIL_is_schema_reasoned | OK |
| SYSTEM | OK |
| MEMORY_empty | OK |

## A. Row integrity (per model)

| model | rows | kinds 8x600 | unique | field viol. | mass<0.9 | mass<0.5 | trunc | empty rat. | raw-value anom. |
|---|---|---|---|---|---|---|---|---|---|
| mistral-small-24b | 4800 | True | True | 0 | 1 | 0 | 1 | 0 | 4 |
| llama31-8b | 4800 | True | True | 0 | 0 | 0 | 1 | 0 | 1728 |
| qwen3-8b | 4800 | True | True | 0 | 0 | 0 | 0 | 0 | 246 |
| qwen35-9b | 4800 | True | True | 0 | 0 | 0 | 4 | 0 | 975 |
| gemma3-12b | 4800 | True | True | 0 | 0 | 0 | 0 | 0 | 285 |

Probe raw token distincts (per model): mistral-small-24b: {'NO': 1200, 'YES': 600}; llama31-8b: {'NO': 1200, 'YES': 600}; qwen3-8b: {'NO': 1251, 'YES': 549}; qwen35-9b: {'NO': 1200, 'YES': 600}; gemma3-12b: {'NO': 1200, 'YES': 600}

Value-vs-raw-grid deviation (mass ≥ 0.99; value is the digit-bucket EV, raw is the single argmax token — divergence means the digit distribution is spread across spellings/buckets, not corruption):

- mistral-small-24b: max dev 9.763 — bands {'<=1': 29, '1-3': 13, '3-10': 4}
- llama31-8b: max dev 51.768 — bands {'<=1': 540, '3-10': 1229, '1-3': 732, '10-30': 475, '>30': 24}
- qwen3-8b: max dev 43.782 — bands {'<=1': 2501, '3-10': 214, '1-3': 253, '>30': 4, '10-30': 28}
- qwen35-9b: max dev 46.086 — bands {'1-3': 748, '<=1': 1277, '10-30': 297, '3-10': 652, '>30': 26}
- gemma3-12b: max dev 27.795 — bands {'<=1': 2325, '3-10': 249, '10-30': 36, '1-3': 390}

Truncated rationales (110-token cap; answer cue still appended, readout unaffected):

- mistral-small-24b: ['g24a_fever_219033/base']
- llama31-8b: ['g24a_scifact_169/exclude_pre']
- qwen35-9b: ['g24a_fever_215510/exclude_pre', 'g24a_fever_32505/admit_pre', 'g24a_fever_32505/admit_post', 'g24a_fever_32505/exclude_pre']

## B. Prompt reconstruction (prereg-literal rebuild -> token count)

| model | prompts checked | byte == compile_prompt | n_prompt_tokens exact | rule_to_answer_tokens exact |
|---|---|---|---|---|
| mistral-small-24b | 4800 | 4800 | 4800 | 3000 |
| llama31-8b | 4800 | 4800 | 4800 | 3000 |
| qwen3-8b | 4800 | 4800 | 4800 | 3000 |
| qwen35-9b | 4800 | 4800 | 4800 | 3000 |
| gemma3-12b | 4800 | 4800 | 4800 | 3000 |

Every prompt was rebuilt from the **preregistration text** (independent of src/), checked byte-equal against compile_prompt/compile_probe, then tokenized through the exact chat-template path run_model used (mirror of chat_ids) and compared to the recorded n_prompt_tokens. 600 items x 8 kinds x 5 models.

## C. Item file (600)

- unique ids 600/600; unique claim texts 600/600
- identical ADMIT rule: 600/600; identical EXCLUDE rule: 600/600
- identical tail (question+output+probe+empty memory): 600/600
- strata: {'fever/SUPPORTS': 200, 'fever/REFUTES': 200, 'scifact/SUPPORT': 100, 'scifact/CONTRADICT': 100}
- directions: {'increase': 300, 'decrease': 300}; families: {'g24a_fever': 400, 'g24a_scifact': 200}
- mapping violations: 0
- documented direction flips (manual review; label-derived mapping overridden): ['g24a_fever_20847', 'g24a_fever_24795', 'g24a_fever_58608', 'g24a_fever_90151']
- ground_truth values: ['None']
- evidence == claim: 0
- empty required fields: 0

## D. Coherence (observation only — cannot fail)

### mistral-small-24b
- ntok(admit_pre) − ntok(exclude_pre): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(admit_post) − ntok(exclude_post): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(exclude_pre) − ntok(exclude_post): {'n': 600, 'min': 0, 'p1': 0, 'p10': 0, 'p50': 0, 'p90': 0, 'p99': 0, 'max': 0}
- base shorter than admit_pre: 600/600
- admit_post − admit_pre value: {'n': 600, 'min': -51.65380609265956, 'p1': -21.40356318525201, 'p10': -2.5343313987941656, 'p50': 0.005692004078746732, 'p90': 5.66601666815215, 'p99': 75.01363618034723, 'max': 99.76371835504978} (|Δ|>20: 25)
- exact 0/100/50 counts: {'base': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}}
- digit mass: {'n': 3000, 'min': 0.8533284619804906, 'p1': 0.9606009906016855, 'p10': 0.9718493578607791, 'p50': 0.980721153572488, 'p90': 0.9874285642721663, 'p99': 0.9902006686252073, 'max': 0.9924357641042209}

### llama31-8b
- ntok(admit_pre) − ntok(exclude_pre): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(admit_post) − ntok(exclude_post): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(exclude_pre) − ntok(exclude_post): {'n': 600, 'min': 0, 'p1': 0, 'p10': 0, 'p50': 0, 'p90': 0, 'p99': 0, 'max': 0}
- base shorter than admit_pre: 600/600
- admit_post − admit_pre value: {'n': 600, 'min': -93.94245382045001, 'p1': -87.9652687389362, 'p10': -5.330013551012067, 'p50': 1.0275303081551783, 'p90': 12.39724875699622, 'p99': 88.98109398391097, 'max': 97.30995061165727} (|Δ|>20: 80)
- exact 0/100/50 counts: {'base': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}}
- digit mass: {'n': 3000, 'min': 0.9919417475751395, 'p1': 0.9994240663491559, 'p10': 0.9996999973072331, 'p50': 0.9999490922193888, 'p90': 0.9999850117709388, 'p99': 0.9999921350856856, 'max': 0.9999972392417223}

### qwen3-8b
- ntok(admit_pre) − ntok(exclude_pre): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(admit_post) − ntok(exclude_post): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(exclude_pre) − ntok(exclude_post): {'n': 600, 'min': 0, 'p1': 0, 'p10': 0, 'p50': 0, 'p90': 0, 'p99': 0, 'max': 0}
- base shorter than admit_pre: 600/600
- admit_post − admit_pre value: {'n': 600, 'min': -99.99998026866001, 'p1': -56.84327540736881, 'p10': -0.9793151972309033, 'p50': 1.7351453607261647e-11, 'p90': 7.086217845123102, 'p99': 65.82425315497572, 'max': 99.99951410735576} (|Δ|>20: 58)
- exact 0/100/50 counts: {'base': {'eq_0': 33, 'eq_100': 51, 'eq_50': 0}, 'admit_pre': {'eq_0': 69, 'eq_100': 118, 'eq_50': 0}, 'admit_post': {'eq_0': 66, 'eq_100': 131, 'eq_50': 0}, 'exclude_pre': {'eq_0': 85, 'eq_100': 71, 'eq_50': 0}, 'exclude_post': {'eq_0': 77, 'eq_100': 26, 'eq_50': 0}}
- digit mass: {'n': 3000, 'min': 0.999999856104069, 'p1': 0.9999999125127027, 'p10': 0.9999999605402083, 'p50': 1.0000000000963565, 'p90': 1.0000000421672954, 'p99': 1.0000000902377784, 'max': 1.000000165211802}

### qwen35-9b
- ntok(admit_pre) − ntok(exclude_pre): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(admit_post) − ntok(exclude_post): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(exclude_pre) − ntok(exclude_post): {'n': 600, 'min': 0, 'p1': 0, 'p10': 0, 'p50': 0, 'p90': 0, 'p99': 0, 'max': 0}
- base shorter than admit_pre: 600/600
- admit_post − admit_pre value: {'n': 600, 'min': -99.37777804874845, 'p1': -44.35441218843731, 'p10': -1.2696520205839674, 'p50': -0.0008283006140885618, 'p90': 3.2592306325575064, 'p99': 77.6705468378605, 'max': 99.97440106865486} (|Δ|>20: 28)
- exact 0/100/50 counts: {'base': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}}
- digit mass: {'n': 3000, 'min': 0.9992306585815358, 'p1': 0.9998928011387838, 'p10': 0.9999445618901172, 'p50': 0.999983285143093, 'p90': 0.9999949662125763, 'p99': 0.9999973194136809, 'max': 0.9999984843426984}

### gemma3-12b
- ntok(admit_pre) − ntok(exclude_pre): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(admit_post) − ntok(exclude_post): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(exclude_pre) − ntok(exclude_post): {'n': 600, 'min': 0, 'p1': 0, 'p10': 0, 'p50': 0, 'p90': 0, 'p99': 0, 'max': 0}
- base shorter than admit_pre: 600/600
- admit_post − admit_pre value: {'n': 600, 'min': -99.99983850133951, 'p1': -22.299433580527634, 'p10': -5.554327921689108, 'p50': -9.427691893968668e-05, 'p90': 6.880865388261199, 'p99': 73.95944328734981, 'max': 99.99663088832885} (|Δ|>20: 35)
- exact 0/100/50 counts: {'base': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}}
- digit mass: {'n': 3000, 'min': 0.9999992843118026, 'p1': 0.9999998444740031, 'p10': 0.9999999295661003, 'p50': 1.000000001088883, 'p90': 1.000000070187595, 'p99': 1.0000001235188043, 'max': 1.0000001691827995}

## E. Retest: selection pass vs main pass (mistral, temp 0, identical prompts)

- decode-relevant runner args identical: True  (selection: {'--mode': 'reasoned', '--reason-tokens': '110', '--max-model-len': '4096', '--tp': '1', '--temperature': None, '--gpu-frac': '0.85', '--enforce-eager': True}; main: {'--mode': 'reasoned', '--reason-tokens': '110', '--max-model-len': '4096', '--tp': '1', '--temperature': None, '--gpu-frac': '0.85', '--enforce-eager': True})
- item drift vs candidates: 56 items — exactly the documented 52 claim rewrites (base_context) + 4 direction flips (critical_direction); 544/600 items byte-identical, undocumented drift = 0 (anything else hard-stops)
- retest scope: 548/600 items (the 52 rewritten-claim items are excluded: their selection-pass prompts differ by design); joined 1644 rows; n_prompt_tokens equal 1644/1644 — prompts identical across passes
- value bands: ==0 1181 (71.8%), <=1 257, <=10 143, 10-50 52, >50 11
- raw argmax flips: 106 (6.4%), by kind {'base': 64, 'admit_pre': 15, 'admit_post': 27}
- pearson(value_selection, value_main) = 0.981191
- rows with |Δ|>50: [{'item': 'g24a_fever_156102', 'kind': 'base', 'd_value': 98.555721}, {'item': 'g24a_fever_228350', 'kind': 'base', 'd_value': 94.776765}, {'item': 'g24a_fever_226113', 'kind': 'base', 'd_value': 89.246501}, {'item': 'g24a_fever_63435', 'kind': 'base', 'd_value': 87.53454}, {'item': 'g24a_scifact_1288', 'kind': 'admit_post', 'd_value': 83.436348}, {'item': 'g24a_fever_209092', 'kind': 'admit_post', 'd_value': 81.498734}, {'item': 'g24a_fever_74555', 'kind': 'admit_pre', 'd_value': 68.865172}, {'item': 'g24a_fever_211799', 'kind': 'base', 'd_value': 68.423073}, {'item': 'g24a_fever_24795', 'kind': 'admit_pre', 'd_value': 62.97332}, {'item': 'g24a_fever_199817', 'kind': 'admit_post', 'd_value': 56.027872}, {'item': 'g24a_fever_17278', 'kind': 'base', 'd_value': 50.500062}]
- diagnosis: prompts identical across passes on all 548 non-rewritten items (n_prompt_tokens 1644/1644, prompt-relevant item text byte-identical, runner args identical) yet values differ -> temp-0 vLLM is not batch-composition invariant; the divergence amplifies through the two-stage greedy decode (rationale flips). The 52 claim-rewritten items ran pre-rewrite prompts in the selection pass and are excluded from the retest; single-cell values remain run-specific near boundaries.

Worst row (g24a_fever_156102 / base):

- **selection**: raw=9 value=99.691 mass=0.9835833598349168 ntok=115
  - reasoning: 'Keith Stanfield was born on March 12, 1991. This is a well-documented fact. The claim is true.\n\n'
- **main**: raw=0 value=1.135 mass=0.9867005292944856 ntok=115
  - reasoning: 'Keith Stanfield was born on August 12, 1991. The claim is incorrect.\n'

Same prompt (identical n_prompt_tokens, byte-identical item text), same decode args — the greedy rationale itself diverged between the two temp-0 passes (see above), which then flips the final digit. Single-cell values are therefore run-specific near decision boundaries; aggregates over 600 items are unaffected (pearson above).

## F. Byte fidelity vs git HEAD

- `results/raw/mistral-small-24b_g24a.jsonl`: identical
- `results/raw/llama31-8b_g24a.jsonl`: identical
- `results/raw/qwen3-8b_g24a.jsonl`: identical
- `results/raw/qwen35-9b_g24a.jsonl`: identical
- `results/raw/gemma3-12b_g24a.jsonl`: identical
- `data/items/g24a_v1.jsonl`: identical
- `results/raw/g24a_mistral-small-24b_selection.jsonl`: identical

## Provenance timeline (from git log / mtimes)

- `25316a9` 09-24 03:16 — g24a harness frozen (conditions/builder/selector/analyzer)
- `b3fe84d` 09-24 04:22 — selection pass + selector early-stop fix (selector script only)
- `1ffd52d`/`59ec3c4`/`6eb405a`/`c661db0` 09-24 04:27–04:36 — five main-pass raws committed at creation
- `92d8cd0` 09-25 12:31 — manual-review dispositions applied to the item file (52 claim rewrites + 4 direction flips; 56 lines); `52b583f` — all pre-rerun analyses discarded; `e4319cb` 09-25 12:47 — full 600-item x 5-model main-pass re-run on the corrected item file (selection pass intentionally NOT rerun: candidate pool unchanged; this audit is computed on the regenerated raws)
- `git diff c661db0..HEAD -- src/schema.py src/conditions_g24a.py src/run_model.py` — only additive G25A/G26A dispatch; the G24A path is bit-for-bit unchanged (audited separately)
- source provenance: `data/external/review/G24A_SOURCE_DATA_AUDIT_v1` (09-24 02:33) — pinned SHA-256 of official FEVER/SciFact releases, exact row counts, refs resolved 3462/3462, failures=[]

