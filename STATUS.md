# Project status — main line, claims, evidence

**As of:** 2026-09-03, after G18. **Experimental programme: CLOSED.**
**Target:** ARR 2026-10-12 → NAACL 2027.

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
| 6 | **The policy needs a semantic target — reference and lexical similarity do not suffice** | **G18, prospective**: pooled ExclusionEffect entail 31.16 / para 30.93 vs ident 26.27 / unrel 22.06 / none 21.84 / empty 18.08; **Δ_semantic +8.91 [+7.15, +10.76], 5/5 models**; para − empty **+12.85 [+10.32, +15.42]**. Discovery support: similarity ladder, semantically-empty tag = identity predicate, content × identity 2×2 | **100 fresh items, 30 fresh skeletons, 3 families, 5 models, 4 vendors** | **confirmed** |
| 6b | **With a semantic target, exclusion follows the proposition beyond the named block** | `marg(exclude)` −27.66 under `para` vs +14.40 under `empty`; negative in 5/5 under `para`, positive in 5/5 under `empty` | 5 models | **solid** |
| 7 | **A class marker carried on the evidence works prospectively** | tagged stream: leakage **0.406–0.536 → ≈0 in both arms**, exact ground truth | 5 models | **solid** |
| 8 | **The same dissociation in an agent** | `SYSTEM` identifier policy worth nothing (+1.014 vs +0.991 naive); same policy after the tool output much better; suppression follows the proposition, not the document ID | 3 models, real `SYSTEM`/`TOOL` roles | **solid** |
| 9 | **Excluded evidence is still read at the decision** | span gate returns the answer to Base: +0.46→−0.12 pre, +0.32→−0.08 post, p<1e-4 | Qwen3-8B | **solid, single model** |
| 10 | **Gating is resolved late** | answer-position patching: nothing <L18, 50% at L21, ≈85% by L27 of 36 | Qwen3-8B | **solid, single model** |
| 11 | **A mid-network rule state carries whether a semantic target was found, and interchanging it changes later suppression** | Qwen3-8B L14–18/36 (depth 0.39–0.50) break +13.3 [+8.1, +18.9], rescue −3.6 [−5.9, −1.4]; **Mistral-Small-24B** L12–16/40 (depth 0.30–0.40) gap +18.2, break +15.7, rescue −13.4, null above 0.45 | **2 models, 2 architectures** | **solid** |

## 3. The seam that was open, and what happened to it

Steps 4 and 6 were asserted side by side and never crossed. G17 tried to unify them
and its frozen verdict was `no-rescue` on a defective ratio estimand; a robust
re-analysis in raw points matched the prediction (+9.30 [+6.11, +12.65]) but only
post-result. **The paper does not claim unification and does not need to.** `w = 0`
is written as a boundary condition serving step 6, not as a competing regularity:
the failure is not a generic inability to follow future-directed instructions, it is
about making semantically integrated evidence causally inert. See
`results/g17_binding_by_weight_results.md`.

## 4. What is explicitly not claimed

- **Not** that the mechanism explains class-marker binding. The fixed-position
  mechanism readout is **blind to that contrast** (−0.503 behavioural vs +0.045 direct
  on identical prompts). Its reach is rule position and content-preview binding — the
  latter being §5.2, the paper's central binding claim.
- **Not** that the tag-bound and identifier-bound policies differ in one exchangeable
  state. G16 stopped at its bridge gate; no method available here can test it.
- **Not** that steps 4 and 6 are one regularity (§3 above).
- **Not** anything mechanistic beyond Qwen3-8B and Mistral-Small-24B.
- **Not** that `ExclusionEffect` measures the same thing at every G18 level; at the
  semantic levels little evidence influence remains to remove and the quantity is
  dominated by suppression below baseline. The decomposition is in the paper text.
- **Not** that identifier policies never work — they do in Gemma-3-12B and
  Qwen3.5-27B. What holds in all four agent models is that they fail when the same
  proposition arrives under a new identifier.

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
| G18 `para − empty` | Does not exclude zero in Phi-4-mini (+3.50 [−1.06, +8.57]); positive in 5/5, interval excludes zero in 4/5. |
| Mistral G18 load | The `/var/tmp` snapshot fails under this vLLM build; the HF-tokenizer conversion of the same checkpoint was used, as in earlier rounds. No checkpoint replaced. |

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
2. **Main line coherent** — met. Steps 1→3→4→6→8→11 form one line: a gap, a
   localisation, a boundary condition, the explanatory variable **confirmed
   prospectively on fresh items**, its deployment form, and a causal mechanism in two
   architectures. The one seam that was open is now written as a boundary condition
   rather than a competing regularity (§3).
3. **Workload and breadth** — met and above median: 12+2 models for the phenomenon,
   5 models / 4 vendors / 100 fresh items / 30 fresh skeletons for the centrepiece,
   2 architectures for the mechanism, ~13 preregistered rounds, 3 intervention types.
4. **No downgrade under disappointing results** — the claims that moved, moved because
   data required it; one earlier over-correction was reversed (the mechanism *does*
   reach the central claim); and rather than settle for the discovery chain, the
   centrepiece was re-run prospectively on fresh materials and **confirmed**.
5. **No defensive experiment sprawl** — every round in the main line discriminates
   between live accounts or answers a positive question; §3 is written as a positive
   localisation, not a list of denials.

## 8. Next step

**The experimental programme is closed.** G18's preregistration commits us to stopping
on `confirmed`: no G19, no further models, no frontier API, no mitigation study, no
third mechanism model, no successor to G16 or G17, no naturally-occurring corpus.

The remaining work is writing (`PAPER_OUTLINE.md`).
