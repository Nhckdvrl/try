# Worklog — alignment campaign

Running record of what is being done, why, and what came out. Newest section
last. Every entry names the artifact it produced so nothing is claimed without
a file behind it.

---

## 2026-09-01 — Session opened

**Goal set by the user:** align the project to ACL / EMNLP / NAACL Main and
Outstanding standards — not only in framing but in *experimental volume* — and
extend it into an actual method. Compute released: this node (4× RTX PRO 6000)
plus any idle GPUs on `fvcrc10/11/12/13/15/20`.

### 1. Read the whole project

Read `README.md`, `RESEARCH_PLAN.md`, `DATASET_REDESIGN.md`,
`RELATED_WORK_2026.md`, the G1/G2 preregistrations, and every results file.
State on arrival:

- **Phenomenon (settled).** 256 fresh natural forecasting questions; 3
  checkpoints; boundary recognition 99.2–100%; out-of-set intrusion 7.5–27.7
  points; 3/3 preregistered gates passed.
- **Not answer-copying.** Verdict redaction leaves it intact and in fact larger
  (10.2–34.6).
- **Not a scale artefact.** Qwen3.5 4B/9B/27B: 32.0 / 16.0 / 36.8, largest
  most contaminated.
- **Missing:** any explanatory step. The chain was
  `phenomenon → replication → rule-out → boundary`, with no adjudication
  between competing accounts.

### 2. Diagnosis

Every result so far confounds two claims that the single out-of-set sentence
carries at once:

```text
(a) this text is not licensed to affect the judgment    [licensing]
(b) ... because it postdates the evaluation point       [reason]
```

A model with no licensing machinery at all, and a model with no *time-indexed*
licensing machinery, produce exactly the same 256-unit table. Only one of those
findings is about time. Splitting them is the observation → latent-variable
move that the reference papers all make.

### 3. Written: `PAPER_FRAME.md`

The authoritative register. Answers all eight gates explicitly, names six
competing accounts (two already eliminated), fixes the rule that mechanism is
opened only for a behaviorally undecidable pair, and states the standing rule
that a proposed experiment must be writable as a sub-question of the headline
or it does not run.

### 4. Written and frozen: G3 — exclusion-reason factorization

**Question:** is hindsight contamination a failure to enforce a *temporal*
boundary, or one instance of a general inability to make information the model
believes *true* causally inert?

Replaces the reason clause of the frozen out-of-set sentence and nothing else,
in both cells, on the frozen 256-unit artifact:

| arm | reason clause | truth of packet |
|---|---|---|
| `temporal` | `was produced after this information set and` | not commented on |
| `bare` | *(none)* | not commented on |
| `unreliable` | `was assembled by an unverified automated process, may contain fabricated claims, and` | undercut |
| `procedural` | `was obtained through a channel this forecasting protocol does not permit for this question; its contents are accurate, but it` | affirmed |

Artifacts: `PREREGISTRATION_G3_EXCLUSION_REASON.md`,
`src/adapters/btf3_exclusion_reason.py`, `src/run_exclusion_reason.py`,
`src/analyze_exclusion_reason.py`, `scripts/audit_exclusion_reason.py`,
`scripts/run_exclusion_reason.sh`, `tests/test_exclusion_reason.py`.

**Audit result (`results/btf3_exclusion_reason_audit.json`): PASS.**
512/512 temporal-arm prompts byte-identical to the frozen artifact (so the
published baseline is read, not re-run, and cannot drift); single contiguous
diff span inside `TARGET INFORMATION SET` in every arm; nothing after the
packet header changes; packet→`TASK` token span invariant across all four arms
(this closes, by construction, the positional channel that G2 Experiment A
showed matters). Token deltas vs temporal: bare −7, unreliable +8, procedural
+15.

Tests: 21 new, 107 total, all passing. Tagged `g3-exclusion-reason-design-v1`
and `g3-exclusion-reason-freeze-v1` **before** the first generation.

**Launched** 3 models × 6 conditions × 256 units = 6,912 generations, local
GPUs 0–2.

### 5. Compute survey

| node | GPUs | state | usable |
|---|---|---|---|
| this node | 4× RTX PRO 6000 (driver 580) | 3 busy with G3 | yes |
| `fvcrc20` | 4× RTX PRO 6000 (driver 580) | mostly idle | **yes — env works as-is** |
| `fvcrc15` | 4× A100 80GB | fully idle | driver 12.4; `fgvd` torch needs newer — needs its own env |
| `fvcrc10`, `fvcrc11` | 4× A100 each | 54–100% busy | partial |
| `fvcrc12`, `fvcrc13` | 2–4× A100 | full | no |

Home and the HF cache are shared NFS, so remote nodes read the same weights and
the same frozen artifact.

### 6. Calibrating against the reference papers' actual volume

Read the ACL 2025 Outstanding paper's full text to size the workload honestly
rather than by impression. *Llama See, Llama Do*: **5 models** (Llama-3.1-8B,
Llama-3.1-8B-Instruct, Llama-2-7B, Llama-2-13B, GPT-2 XL), 15 LRE relations, 4
context conditions (related / irrelevant / random / counterfactual), roughly
**11,000–15,000 queries**, plus differentiable-mask head discovery over 1,024
heads, ablation, and downstream-capability retention checks.

Where this project stands against that:

| round | generations |
|---|---:|
| large replication (3 models × 256 units × 4 conditions + probes) | 4,608 |
| G2 hindsight depth (3 × 6 conditions) | 9,216 |
| Qwen3.5 size analysis (2 new sizes) | 3,072 |
| **G3 exclusion reason** (3 × 6 conditions) | 6,912 |
| **G4 breadth** (12 new checkpoints × 4 conditions + probes) | 18,432 |
| **G5 deliberation** (3 × 8 conditions, 640 tokens each) | 9,216 |

The volume gap is not the real gap — the totals already exceed the reference
paper's. The gap was structural, and G3/G5/G6 are what close it.

### 7. Frozen and launched: G4 breadth panel

`PREREGISTRATION_G4_MODEL_BREADTH.md` + `data/model_panel_g4.json`. 17
checkpoints, 8 families, 3.8B–35B, one MoE. Estimands, thresholds, and the
`intrusion_pass` rule are read out of the existing large-replication analyzer
rather than restated, so the panel cannot be graded on a different scale than
the published three. Prediction recorded before running: **no reliable
recognition–intrusion correlation across the panel** (Spearman with a
permutation interval).

Tagged `g4-model-breadth-design-v1`, then dispatched 12 checkpoints across five
GPUs — four lanes on `fvcrc20`, one lane locally.

### 8. Frozen: G5 deliberation and the ex-ante state scaffold

`PREREGISTRATION_G5_DELIBERATION.md`. Replaces only the `TASK` block, which is
byte-identical across all 1,024 frozen prompts and sits at the end of each one.

- `cot` — free-form "reason step by step, then answer";
- `state` — a fixed three-step scaffold: list what was available at the
  evaluation point, name what lies outside it, then answer from step 1 only.

The deciding contrast is **`state` vs `cot`**, not either against the direct
baseline — otherwise a reduction is just "deliberation helps" and says nothing
about state construction. It separates H-absent from H-truth, and doubles as
the paper's first mitigation baseline so any later inference-time method has a
measured number to beat.

A **utility guard** is preregistered as a veto: an arm that lowers intrusion
while dropping licensed responsiveness below 15 points or below 70% of the
direct arm's is reported as damaging the task, not enforcing the boundary.

Parser hardening found by test: `ANSWER: 240` was being read as 24 by a regex
that matched a valid prefix. The number is now captured whole and range-checked,
so an out-of-range answer is an unparsed record. Tagged
`g5-deliberation-design-v1`.

### 9. Built: mechanism capture harness (tooling only, no experiment yet)

`src/mech/capture_hindsight.py` — HF-hooks capture of, per item and condition,
the residual stream at the final prompt position for every layer (fp16) and a
logit-lens readout restricted to the ten digit tokens. This is the instrument
the G6 override-vs-absence test will consume. It is deliberately **not** an
experiment: per `PAPER_FRAME.md` §8, the mechanism design is not frozen until
G3 and G5 have resolved, because which internal question is worth asking
depends on whether enforcement turns out to be truth-keyed.

---

## 2026-09-01 — First results

### 10. G3 result: **H-inert**. This is the round that changed the paper.

6,912 generations. All twelve conditions of all three models qualified;
boundary-probe accuracy 97.3–100% in every arm, so nothing below is the model
losing track of what the packet is.

| model | `temporal` | `bare` | `unreliable` | `procedural` |
|---|---|---|---|---|
| Qwen3.5-9B | 16.02 | 19.38 | 15.04 | 16.68 |
| Gemma-3-12B-it | 27.73 | 28.05 | **35.44** | **35.79** |
| Mistral-Small-24B | 7.46 | 8.34 | 6.34 | 7.14 |

**No arm reduces intrusion in any model.** The frozen table's `H-inert` row is
realized, 3/3 and 2/3 and 2/3.

Three things follow, and together they are a much larger claim than the paper
had before:

1. **It is not about time.** A non-temporal licensing reason — wrong channel,
   contents affirmed accurate — is enforced no better than the temporal one.
2. **It is not about belief.** Telling the model the packet "may contain
   fabricated claims" does not reduce its influence anywhere, and *raises* it
   in Gemma. The discounting an ordinary inference would do is not reached
   through this slot.
3. **It is not about the reason being unstated.** The `bare` arm behaves like
   the temporal arm; in Qwen, stating any reason is 3.4 points better than
   stating none, which is the only sense in which reasons help at all.

Unanticipated, reported as such: in Gemma, both arms that add a clause about
the packet raise intrusion by ~8 points. That lines up with G2-B, where
*removing* the verdict sentence also raised it. A salience reading is available
and is explicitly **not** claimed — it is a hypothesis about attention, which
is what the mechanism phase is for.

Written up in `results/g3_exclusion_reason_results.md`.

### 11. G7 result: the preregistered test **failed, in the opposite direction**

No new generations — a re-analysis against BTF-3's own
`sota_forecast_probability`, an independent ex-ante forecast, on the 239 units
that carry it.

Predicted: the packet moves the model *away* from a competent ex-ante judgment.
Found: `Δ_dev` = **−6.84 / −9.27 / −4.61** — it moves them *closer*. Panel
verdict indeterminate; by the frozen rule nothing is concluded.

The validity check says why, and is the more useful number: `rho_without` =
**0.28 / 0.29 / 0.33**. The uncontaminated cell is a weak ex-ante forecast —
hedged toward 50 (`|p − 50|` ≈ 14) and under-committed against the anchor by
about 19 points. Brier improves with the packet in all three models, as
predicted, because moving toward the outcome is what the packet does.

Consequences, both recorded:

- **The paper loses a sentence it wanted.** It may not claim infidelity to an
  independent ex-ante reference.
- **The paper gains a limitation it now states itself**: these models are not
  strong pastcasters on BTF-3, and a reader is entitled to know the judgment
  being contaminated is a weak one. Better found here than by a reviewer.
- **The primary estimand is untouched.** `OutOfSetIntrusion` is a within-item
  causal contrast and nothing in G7 bears on it.

Written up in `results/g7_exante_anchor_results.md`.

### 12. Running

- **G4 breadth**: 2 of 12 checkpoints done (`qwen25-14b`, `llama31-8b`). The
  large ones are bottlenecked on NFS — four 30–70GB checkpoints loading over
  one mount. Staged the next models to node-local NVMe on both nodes so the
  second model in each lane loads from disk.
- **G5 deliberation**: launched on all three models as soon as G3 freed the
  GPUs; first condition landing.

### 13. Built: `src/mech/span_mask.py`

Attention-span masking on the frozen prompts — char span → token span under the
model's own chat template (cross-checked against the untouched tokenizer path),
an additive mask blocking answer positions from attending to the packet, and
forward pre-hooks to apply it in a layer window only.

The method framing matters and is deliberate: **masking, not deleting.**
Deleting the packet changes the prompt so the model can no longer be asked
about it. Masking leaves the text in context — the boundary probe still works —
while removing its causal path into the decision. That is precisely the
contract the project measures: `memory(E)` retained, `causal_effect(E → decision)`
removed.

### 14. Frozen: G6 mechanism — the layer-window masking sweep, and the method

`PREREGISTRATION_G6_MECHANISM.md`, tagged `g6-mechanism-design-v1`.

G3's `H-inert` is what makes mechanism legitimate here. Exactly one pair
survives it and no output can separate the two:

- **H-override** — an ex-ante judgment is computed and overwritten late;
- **H-absent** — none is ever computed; recognition runs beside the answer.

**The primary test is causal, not a probe.** Masking the packet's tokens from
the answer positions in a suffix window `[fL, L)` and sweeping `f` asks *how
late the intervention can be and still restore the no-packet answer*. Late-only
restoration means an uncontaminated trajectory existed and was overwritten;
restoration only at full depth means the packet was in the estimate from the
start. Opposite predictions, one number per window, `f*` read off a frozen rule.

Probing is deliberately demoted to secondary, with its limit written into the
document rather than left for a reviewer: decodability shows the answer is
*available* in the activations, not that the model *computes* it.

Two instrument checks are part of the design, not afterthoughts: full-depth
masking must restore the no-packet answer (or nothing else in the round is
usable), and the HF-vs-vLLM disagreement rate is *measured*, with the analysis
using the HF unmasked run as its own reference so a framework difference cannot
masquerade as an effect.

**The method** is enforcement by masking, with the honesty requirement frozen
alongside it: the `delete` reference sits in the same table, and what is claimed
is selective, reversible enforcement *with the evidence still in context and
still answerable*. The baseline it must beat is prompting — and G3 showed
prompting does nothing at all, including a prompt that undercuts the packet's
truth. A `wrong-span` control of identical token length is what separates
enforcement from damage.

17 tests, including that the masking path tokenizes byte-identically to the
path every previous round used.

### 15. Compute reality check

`fvcrc20` turned out **not** to be idle: four other users' processes at
320–430% CPU for 5–7 hours, load average 22–25, and the vLLM engine cores
sitting in uninterruptible-sleep — blocked on NFS, not on GPU. Two 30–60GB
checkpoints spent an hour past weight-loading with zero generation.

Response: stopped the lane that had not begun loading to free NFS bandwidth,
kept the two that had, and moved the remaining small checkpoints to local NVMe
staging on this node instead. The breadth panel is descriptive; the core rounds
(G5, G8, G6) run on locally staged weights and are not exposed to that
contention.

Breadth so far: 8 of 17 checkpoints have output — `gemma3-4b`, `gemma3-12b`,
`llama31-8b`, `mistral-small-24b`, `qwen25-14b`, `qwen35-4b`, `qwen35-9b`,
`qwen35-27b`.
