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
