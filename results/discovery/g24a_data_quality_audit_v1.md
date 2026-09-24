# G24A data-quality audit v1 (line-by-line, integrity only)

Generated 2026-09-25 04:30:48 — 97.3s. Scope: data integrity. **No scientific gates, no findings selection** — section D is observation only and can never fail the audit.

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
| mistral-small-24b | 4800 | True | True | 0 | 0 | 0 | 1 | 0 | 4 |
| llama31-8b | 4800 | True | True | 0 | 0 | 0 | 2 | 0 | 1705 |
| qwen3-8b | 4800 | True | True | 0 | 0 | 0 | 0 | 0 | 258 |
| qwen35-9b | 4800 | True | True | 0 | 0 | 0 | 3 | 0 | 982 |
| gemma3-12b | 4800 | True | True | 0 | 0 | 0 | 0 | 0 | 288 |

Probe raw token distincts (per model): mistral-small-24b: {'NO': 1200, 'YES': 600}; llama31-8b: {'NO': 1200, 'YES': 600}; qwen3-8b: {'NO': 1252, 'YES': 548}; qwen35-9b: {'NO': 1200, 'YES': 600}; gemma3-12b: {'NO': 1200, 'YES': 600}

Value-vs-raw-grid deviation (mass ≥ 0.99; value is the digit-bucket EV, raw is the single argmax token — divergence means the digit distribution is spread across spellings/buckets, not corruption):

- mistral-small-24b: max dev 9.763 — bands {'<=1': 29, '1-3': 7, '3-10': 4}
- llama31-8b: max dev 53.352 — bands {'<=1': 537, '3-10': 1233, '1-3': 758, '10-30': 445, '>30': 27}
- qwen3-8b: max dev 43.782 — bands {'<=1': 2471, '3-10': 218, '1-3': 271, '>30': 6, '10-30': 34}
- qwen35-9b: max dev 47.667 — bands {'1-3': 775, '<=1': 1243, '10-30': 310, '3-10': 649, '>30': 23}
- gemma3-12b: max dev 26.344 — bands {'<=1': 2325, '3-10': 247, '10-30': 41, '1-3': 387}

Truncated rationales (110-token cap; answer cue still appended, readout unaffected):

- mistral-small-24b: ['g24a_fever_219033/base']
- llama31-8b: ['g24a_fever_25290/base', 'g24a_scifact_169/exclude_pre']
- qwen35-9b: ['g24a_fever_215510/exclude_pre', 'g24a_fever_32505/admit_post', 'g24a_fever_32505/exclude_pre']

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
- ground_truth values: ['None']
- evidence == claim: 0
- empty required fields: 0

## D. Coherence (observation only — cannot fail)

### mistral-small-24b
- ntok(admit_pre) − ntok(exclude_pre): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(admit_post) − ntok(exclude_post): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(exclude_pre) − ntok(exclude_post): {'n': 600, 'min': 0, 'p1': 0, 'p10': 0, 'p50': 0, 'p90': 0, 'p99': 0, 'max': 0}
- base shorter than admit_pre: 600/600
- admit_post − admit_pre value: {'n': 600, 'min': -51.65380609265956, 'p1': -30.8026250899741, 'p10': -2.81371226914532, 'p50': 0.00679756344933935, 'p90': 6.415671502320709, 'p99': 81.11221739977233, 'max': 99.76371835504978} (|Δ|>20: 32)
- exact 0/100/50 counts: {'base': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}}
- digit mass: {'n': 3000, 'min': 0.9337603628941281, 'p1': 0.9606009906016855, 'p10': 0.9717956158221517, 'p50': 0.9806038902488105, 'p90': 0.9874065742637514, 'p99': 0.9901676112860744, 'max': 0.9923887986158011}

### llama31-8b
- ntok(admit_pre) − ntok(exclude_pre): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(admit_post) − ntok(exclude_post): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(exclude_pre) − ntok(exclude_post): {'n': 600, 'min': 0, 'p1': 0, 'p10': 0, 'p50': 0, 'p90': 0, 'p99': 0, 'max': 0}
- base shorter than admit_pre: 600/600
- admit_post − admit_pre value: {'n': 600, 'min': -93.28758656048332, 'p1': -87.98356623863292, 'p10': -4.832478301153884, 'p50': 1.1923453969990732, 'p90': 11.837536759610046, 'p99': 86.67965130701712, 'max': 96.97327645210021} (|Δ|>20: 78)
- exact 0/100/50 counts: {'base': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}}
- digit mass: {'n': 3000, 'min': 0.9913084512611803, 'p1': 0.9993537513242235, 'p10': 0.9997005776725769, 'p50': 0.9999487289297766, 'p90': 0.9999850800873716, 'p99': 0.9999922191613976, 'max': 0.9999973350943228}

### qwen3-8b
- ntok(admit_pre) − ntok(exclude_pre): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(admit_post) − ntok(exclude_post): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(exclude_pre) − ntok(exclude_post): {'n': 600, 'min': 0, 'p1': 0, 'p10': 0, 'p50': 0, 'p90': 0, 'p99': 0, 'max': 0}
- base shorter than admit_pre: 600/600
- admit_post − admit_pre value: {'n': 600, 'min': -99.99998026866001, 'p1': -56.82953962471534, 'p10': -2.4730784774952213, 'p50': 1.4210854715202004e-11, 'p90': 6.555684731542648, 'p99': 67.1806111825855, 'max': 99.99951410735576} (|Δ|>20: 64)
- exact 0/100/50 counts: {'base': {'eq_0': 29, 'eq_100': 48, 'eq_50': 0}, 'admit_pre': {'eq_0': 64, 'eq_100': 111, 'eq_50': 0}, 'admit_post': {'eq_0': 63, 'eq_100': 128, 'eq_50': 0}, 'exclude_pre': {'eq_0': 76, 'eq_100': 69, 'eq_50': 0}, 'exclude_post': {'eq_0': 74, 'eq_100': 23, 'eq_50': 0}}
- digit mass: {'n': 3000, 'min': 0.9999998400825694, 'p1': 0.9999999053095969, 'p10': 0.999999962488369, 'p50': 1.0000000001069587, 'p90': 1.0000000435790595, 'p99': 1.0000000913670033, 'max': 1.0000001504161502}

### qwen35-9b
- ntok(admit_pre) − ntok(exclude_pre): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(admit_post) − ntok(exclude_post): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(exclude_pre) − ntok(exclude_post): {'n': 600, 'min': 0, 'p1': 0, 'p10': 0, 'p50': 0, 'p90': 0, 'p99': 0, 'max': 0}
- base shorter than admit_pre: 600/600
- admit_post − admit_pre value: {'n': 600, 'min': -99.37777804874845, 'p1': -49.49754168362654, 'p10': -1.4205827534173885, 'p50': 0.0007391484823459646, 'p90': 3.59115053738914, 'p99': 77.6705468378605, 'max': 99.97440106865486} (|Δ|>20: 33)
- exact 0/100/50 counts: {'base': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}}
- digit mass: {'n': 3000, 'min': 0.9994943167496378, 'p1': 0.9998931858795546, 'p10': 0.9999445618901172, 'p50': 0.9999829797051736, 'p90': 0.9999945997498849, 'p99': 0.9999973525933831, 'max': 0.9999984843426984}

### gemma3-12b
- ntok(admit_pre) − ntok(exclude_pre): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(admit_post) − ntok(exclude_post): {'n': 600, 'min': 6, 'p1': 6, 'p10': 6, 'p50': 6, 'p90': 6, 'p99': 6, 'max': 6}
- ntok(exclude_pre) − ntok(exclude_post): {'n': 600, 'min': 0, 'p1': 0, 'p10': 0, 'p50': 0, 'p90': 0, 'p99': 0, 'max': 0}
- base shorter than admit_pre: 600/600
- admit_post − admit_pre value: {'n': 600, 'min': -99.99983850133951, 'p1': -38.384340789023724, 'p10': -5.554327921689108, 'p50': -8.129475212071136e-05, 'p90': 8.024734238407325, 'p99': 72.24727299630682, 'max': 99.99663088832885} (|Δ|>20: 34)
- exact 0/100/50 counts: {'base': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'admit_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_pre': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}, 'exclude_post': {'eq_0': 0, 'eq_100': 0, 'eq_50': 0}}
- digit mass: {'n': 3000, 'min': 0.9999996139688307, 'p1': 0.9999998459925299, 'p10': 0.9999999285352427, 'p50': 1.0000000012406582, 'p90': 1.0000000708397097, 'p99': 1.0000001262712395, 'max': 1.0000001971750767}

## E. Retest: selection pass vs main pass (mistral, temp 0, identical prompts)

- decode-relevant runner args identical: True  (selection: {'--mode': 'reasoned', '--reason-tokens': '110', '--max-model-len': '4096', '--tp': '1', '--temperature': None, '--gpu-frac': '0.85', '--enforce-eager': True}; main: {'--mode': 'reasoned', '--reason-tokens': '110', '--max-model-len': '4096', '--tp': '1', '--temperature': None, '--gpu-frac': '0.85', '--enforce-eager': True})
- item text drift vs candidates: 0 (600/600 byte-identical when present)
- joined 1800 rows; n_prompt_tokens equal 1800/1800 — prompts identical across passes
- value bands: ==0 1287 (71.5%), <=1 282, <=10 157, 10-50 65, >50 9
- raw argmax flips: 127 (7.1%), by kind {'base': 72, 'admit_pre': 23, 'admit_post': 32}
- pearson(value_selection, value_main) = 0.984145
- rows with |Δ|>50: [{'item': 'g24a_fever_223352', 'kind': 'admit_pre', 'd_value': 99.629919}, {'item': 'g24a_fever_228350', 'kind': 'base', 'd_value': 94.776765}, {'item': 'g24a_fever_63435', 'kind': 'base', 'd_value': 87.53454}, {'item': 'g24a_scifact_1288', 'kind': 'admit_post', 'd_value': 83.436348}, {'item': 'g24a_fever_209092', 'kind': 'admit_post', 'd_value': 81.498734}, {'item': 'g24a_fever_151957', 'kind': 'admit_post', 'd_value': 77.163896}, {'item': 'g24a_fever_74555', 'kind': 'admit_pre', 'd_value': 68.865172}, {'item': 'g24a_fever_199817', 'kind': 'admit_post', 'd_value': 56.027872}, {'item': 'g24a_fever_45014', 'kind': 'base', 'd_value': 52.41687}]
- diagnosis: prompts identical (n_prompt_tokens 1800/1800, item text byte-identical, runner args identical) yet values differ -> temp-0 vLLM is not batch-composition invariant; the divergence amplifies through the two-stage greedy decode (rationale flips)

Worst row (g24a_fever_223352 / admit_pre):

- **selection**: raw=0 value=0.179 mass=0.9857771795777277 ntok=167
  - reasoning: 'The film was released in 2017, so it is 6 years old. Therefore, the claim that it is 8 years old is certainly false.\n\n'
- **main**: raw=9 value=99.809 mass=0.9857555789591587 ntok=167
  - reasoning: 'The film "The Disaster Artist" was released in 2017, so it is 8 years old as of 2023. This makes the claim true.\n\n'

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
- `git diff c661db0..HEAD -- src/schema.py src/conditions_g24a.py src/run_model.py` — only additive G25A/G26A dispatch; the G24A path is bit-for-bit unchanged (audited separately)
- source provenance: `data/external/review/G24A_SOURCE_DATA_AUDIT_v1` (09-24 02:33) — pinned SHA-256 of official FEVER/SciFact releases, exact row counts, refs resolved 3462/3462, failures=[]

