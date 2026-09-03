# Project status — main line, claims, evidence

**As of:** 2026-09-03, end of the G17 round. **Target:** ARR 2026-10-12 → NAACL 2027.

This is the single consolidated snapshot: what the paper claims, what backs each claim,
what is disputed, and what is not claimed. `PAPER_FRAME.md` is the narrative register;
this file is the ledger.

---

## 1. The question

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

A policy nearly always exists before the data it governs — a system prompt forbids a
source before retrieval runs, a court excludes evidence before the record is read, an
agent is told which memories are off-limits before any is fetched. The scientific
object is **whether a stated exclusion policy actually governs the decision**, and what
determines when it does.

## 2. The main line, and what carries each step

| # | Step | Evidence | Breadth | Status |
|---|---|---|---|---|
| 1 | **Advance exclusion fails where post-hoc exclusion succeeds** — the reverse of the human pattern | `Δ_time` negative in all 12 instruct models, 10/12 CIs exclude 0; admit control flat | 12 instruct + 2 masked diffusion, 4 vendors, 5 task families, 144 items | **solid** |
| 2 | **The rule is held and ignored** | declarative probe returns "exactly 0" on **100%** of items in both arms, against REI up to **+0.64** prospectively | 6 models | **solid** |
| 3 | **Not memory, distance, causal mask, wording, or implicature** | delay intact to ~1,000 tok (4/6); distance no main effect, further *helps*; largest asymmetry in bidirectional Dream-7B; 40/40 model×wording cells; presentation policy rescues none | 4–12 models per test | **solid** |
| 4 | **The failure is specific to complete suppression** | pooled discontinuity **+0.295 [+0.185, +0.405]**, p<1e-4, n=422; and pre-post gap exactly **0.000** in 4/5 models when the contribution is arithmetically implementable | 6 models / 5 models | **solid** |
| 5 | **Binding decides it — a named future referent is worse than silence** | L0–L5 ladder, uniform inversion | 6 models | **solid** |
| 6 | **Binding is to propositional content, graded by entailment** | similarity ladder `exact ≈ para > summary ≈ 0 > same-direction different fact`; proposition relation matrix with entailment rows far above surface-overlap rows | 4 models / 2 models | **solid** |
| 7 | **A class marker carried on the evidence works prospectively** | tagged stream: leakage **0.406–0.536 → ≈0 in both arms**, exact ground truth | 5 models | **solid** |
| 8 | **The same dissociation in an agent** | `SYSTEM` identifier policy worth nothing (+1.014 vs +0.991 naive); same policy after the tool output much better; suppression follows the proposition, not the document ID | 3 models, real `SYSTEM`/`TOOL` roles | **solid** |
| 9 | **Excluded evidence is still read at the decision** | span gate returns the answer to Base: +0.46→−0.12 pre, +0.32→−0.08 post, p<1e-4 | Qwen3-8B | **solid, single model** |
| 10 | **Gating is resolved late** | answer-position patching: nothing <L18, 50% at L21, ≈85% by L27 of 36 | Qwen3-8B | **solid, single model** |
| 11 | **A binding state is causally exchangeable** | matched-chronology, length-matched rule-span interchange, both directions at L14–18: **+13.3 [+8.1, +18.9]** / **−3.6 [−5.9, −1.4]**, admit arm null | Qwen3-8B | **solid, single model** |

## 3. Open seam

**Are steps 4 and 7 one regularity or two?** The linking hypothesis is that driving a
contribution to exactly zero requires identifying which content to remove, and binding
is what identifies it, while attenuation needs no identification.

G17 crossed binding × requested weight (2,400 generations, 4 models). Result is
**split** and both halves are on the record:

- **frozen verdict `no-rescue`** — but on a ratio estimand that blows up (one item at
  REI 8,492), a failure mode Stage 3E had already documented and solved;
- **robust re-analysis in raw rating points**, the Stage 3E estimator: rescue
  **+10.09 [+7.03, +13.26]** at w=0, **+0.94 [−1.24, +3.14]** at w=0.25,
  **+0.64 [−1.60, +2.85]** at w=0.50, interaction **Δ = +9.30 [+6.11, +12.65]**.

The pattern is exactly what was predicted, but it comes from a post-result estimator
switch. **The paper does not claim unification.** §4 and §5 stay separate until a
prospective confirmation with the correct estimand. See
`results/g17_binding_by_weight_results.md`.

## 4. What is explicitly not claimed

- **Not** that the mechanism explains class-marker binding. The fixed-position
  mechanism readout is **blind to that contrast** (−0.503 behavioural vs +0.045 direct
  on identical prompts). Its reach is rule position and content-preview binding — the
  latter being §5.2, the paper's central binding claim.
- **Not** that the tag-bound and identifier-bound policies differ in one exchangeable
  state. G16 stopped at its bridge gate; no method available here can test it.
- **Not** that §4 and §5 are one regularity (§3 above).
- **Not** anything mechanistic beyond Qwen3-8B.

## 5. Negative and corrected results, all on the record

| item | what happened |
|---|---|
| G0's original prediction | Reversed. The human ordering does not hold for models. The reversal is the paper. |
| G16 | Frozen, run, stopped at gate 1. 300 baselines, 0 patched generations. Cause traced to the readout, not the construction. |
| G17 | Frozen verdict `no-rescue` on a defective estimand; robust re-analysis supports the hypothesis; reported as suggestive only. |
| Stage 3E duplicate control | Found a real confound in Stage 3D and forced the metric from REI to raw rating points. |
| Stage 5 | An earlier recovery-fraction analysis overstated the effect and was withdrawn. |
| External materials | Reclassified from a held-out tier to boundary checks after a provenance audit. |
| Readout pilots | Three failed before the freeze; single-token readouts can anti-correlate with the model's own reasoning. |

## 6. Stopped branch

The BTF-3 hindsight paper was stopped on 2026-09-03 (`RESEARCH_HISTORY.md` §5). Its
data and verdicts are retained. Two integrity corrections are on the record
(`preregistrations/POSTHOC_REDACTION_AUDIT_CORRECTION.md`): the verdict redactor leaves
34/256 packets asserting the outcome and its own audit could not detect it; and the
Llama boundary figure was reported at single-frame scope. Neither changes a
preregistered verdict. The G4 breadth panel will not be completed.

One result is held as a separate, unconfirmed lead
(`SECOND_LEAD_EXPLICIT_OUTCOME_PARADOX.md`): removing an explicit outcome statement
makes later evidence *more* influential, 3/3 models.

## 7. Assessment against the five standards

1. **Natural claim, not covered, right width** — met. Searched: the reversal is
   unpublished for LLMs; ACL 2024 Findings *Instruction Position Matters* found the same
   sign but attributed it to forgetting, which step 2 refutes; prospective-memory work
   asks a different question (step 3 separates them); the w=0 discontinuity and the
   content-vs-identifier variable return nothing.
2. **Main line coherent** — met for steps 1–3 and 5–11; one seam open (§3 above),
   identified by audit and honestly unresolved.
3. **Workload and breadth** — met and above median: 12+2 models, 4 vendors, 2
   architectures, 5 families, 144 frozen items, ~12 preregistered rounds, 3 intervention
   types.
4. **No downgrade under disappointing results** — the claims that moved, moved because
   data required it, and one earlier over-correction was reversed: the mechanism *does*
   reach the paper's central binding claim.
5. **No defensive experiment sprawl** — every round in the main line discriminates
   between live accounts or answers a positive question; §3 is written as a positive
   localisation, not a list of denials.

## 8. Next step

**No further experiment is scheduled.** The one candidate — a prospective confirmation
of the G17 crossing with raw rating points as the primary estimand, a leverage floor
fixed in advance, and per-preview baseline cells — is a decision for the author, not a
default.

The remaining work is writing (`PAPER_OUTLINE.md`).
