# Experiment registry

The single live index of the experimental programme.

Original preregistrations are preserved **unchanged** in
[`preregistrations/`](preregistrations/). Full result tables for the main line are
in [`PROSPECTIVE_EXCLUSION_FINDINGS.md`](PROSPECTIVE_EXCLUSION_FINDINGS.md) and
[`stages/`](stages/). Use this file to see what each round asked, what happened,
and what role it has; open a preregistration when you need exact hypotheses,
estimands, thresholds or freeze chronology.

---

> **Consolidated snapshot:** [`STATUS.md`](STATUS.md) — main line, per-claim evidence,
> what is explicitly not claimed, and the one open seam.

# A. Main paper sequence — advance evidence exclusion

## A1. G0 — the reversal

**Question.** Is an exclusion instruction harder to follow when it arrives after
the evidence, as it is for people?

**Design.** 144 frozen items, five task families, five conditions plus independent
rule and memory probes. 12 instruct models from four vendors, plus LLaDA-8B and
Dream-7B (masked diffusion, bidirectional prompt attention).

**Result.** Reversed. `Δ_time` negative in all twelve instruct models, ten of twelve
intervals excluding zero; the admit control is flat everywhere. The rule is not
forgotten — a separate probe returns "exactly zero" on 100% of items in both arms —
and the asymmetry is largest in a bidirectional diffusion model.

**Paper role.** Headline phenomenon.
**Prereg.** `PREREGISTRATION_G0.md`. **Results.** `PROSPECTIVE_EXCLUSION_FINDINGS.md`,
`results/g0_*.json|md`, `results/cluster_robustness.md`.

## A2. Stage 2 — distance, anaphora, and the first sight of the weight sweep

**Question.** Is the asymmetry decision proximity, linguistic scope, or something
about binding a rule to an object that does not exist yet?

**Result.** Distance has no main effect in any model and within the prospective arm
more distance helps. Removing every directional referent shrinks the effect but
leaves it significant in 3 of 4 models. A coarse weight sweep already shows the
asymmetry only at zero.

**Paper role.** Section 3.3 — rules out the two obvious accounts.
**Results.** `results/stage2_tables.md`, `stages/STAGE3.md` §context.

## A3. Stage 3A — naming the phenomenon

**Question.** What exactly fails?

**Results.**
- **Declarative policy is perfect, the decision ignores it.** 100% "exactly zero"
  in six models, against REI up to +0.64 prospectively.
- **Zero is a discontinuity.** Nine requested weights worded identically; pooled
  `(gap at 0) − (mean gap over eight non-zero levels)` =
  **+0.295 [+0.185, +0.405], p < 1e-4** (n = 422 item-model pairs). Descriptively
  uniform; the formal kink term is identified in only 2 of 6 models, and that is
  reported.
- **Not prospective-memory decay.** Rule-to-evidence delay to ~1,000 tokens leaves
  the gap intact in 4 of 6 models; Gemma-3-12B is a real exception.
- **Announcing the object makes it worse.** L0–L5 ladder, uniform across six models.
- **A class policy on the evidence works.** Beats the item-specific rule
  prospectively in 5 of 6 models. **This single-item comparison did not replicate
  in G16** (A9) under matched grammar, matched length and the mechanism readout;
  the claim is carried by A4's tagged stream instead.
- **Not one sentence.** Eight ruling constructions, 40 of 40 model × wording cells
  positive.

**Paper role.** Sections 3.2, 4, 5.1, 5.3.
**Results.** `stages/STAGE3.md`, `results/stage3_tables.md`, `results/stage3_pooled.md`,
`results/paraphrase_tables.md`.

## A4. Stage 3B — tagged evidence stream

**Question.** Does a policy resolved against a marker travelling with each item
survive being stated in advance?

**Design.** 48 numeric items, 2/4/8/16 reports, half `[verified]` and half
`[unverified]`, policy before or after the stream; exact ground truth, so leakage is
the regression coefficient on the excluded group mean.

**Result.** Leakage 0.406–0.536 with no policy, ≈0 in **both** arms with the policy,
across five models. Caveat: Qwen3-8B is unstable prospectively at N=16.

**Paper role.** Section 5.3 — the structural fix.
**Results.** `results/routing_tables.md`.

## A5. Stage 3C — attacking the narrow claim

**Results.**
- **Inclusion implicature rejected.** An explicit presentation policy stating that
  display does not imply relevance rescues no model; the relevance-*positive*
  control produces gaps as large or larger in 4 of 5.
- **The discontinuity is bounded.** On a task where the requested contribution is
  arithmetically implementable, the pre-post gap at `w=0` is exactly **0.000** in 4
  of 5 models. Phi-4-mini fails retrospectively instead.

**Paper role.** Section 3.3 and Section 4's boundary condition.
**Results.** `stages/STAGE3C.md`.

## A6. Stage 3D / 3E — semantic addressability, and the confound that changed the metric

**Question.** Does the rule need the target's text, or its meaning?

**Results.** The similarity ladder gives `exact ≈ paraphrase > entailing summary ≈ 0
> same-direction different fact` in all four models. The proposition relation matrix
(two models) puts both entailment relations far above everything else, with surface
overlap at or below the no-preview baseline; the middle rows differ between models
and are reported that way.

**Correction inside the round.** A duplicate control found that a fact already read
keeps only 6–18% of its marginal weight on second presentation with no rule
involved. That confound made the ratio metric unstable and the analysis moved to raw
rating points, separating `marg(no rule)` from `ExclusionEffect`. An earlier
similarity ladder built on a weak rule form was discarded and rebuilt before
reporting.

**Paper role.** Section 5.2.
**Results.** `stages/STAGE3D.md`, `stages/STAGE3E.md`, `results/semaddr_tables.md`,
`results/stage7_tables.md`, `results/onpolicy_tables.md`.

## A7. Stage 4A — the same failure in an agent

**Design.** `SYSTEM` policy before retrieval → document in a `TOOL` message →
assistant answers. 75 items, legal + inference.

**Result.** An identifier-only system policy is worth nothing in 2 of 3 models
(+1.014 vs +0.991 naive). The same policy after the tool output is much better in
all three. Suppression follows the proposition, not the identifier: the same content
arriving as `D9` defeats an ID-only policy but not a proposition policy.

**Paper role.** Section 6.
**Results.** `stages/STAGE4.md`, `results/agent_tables.md`, `results/agent_marginal.md`.

## A8. Mechanism — span gate, late gating, and matched interchange

**Models.** Qwen3-8B and Mistral-Small-24B, 75/45 items from the two families where a fixed-position readout
tracks the behavioural one (item-level r = 0.76 and 0.90).

**Results.**
- **Evidence-span causal gate.** Blocking downstream attention to the evidence span
  returns the answer to Base: +0.46 → −0.12 prospectively, +0.32 → −0.08
  retrospectively, p < 1e-4 both. A decision-gating failure, not a comprehension
  failure.
- **Late resolution.** Answer-position patching recovers nothing below layer 18, 50%
  at 21, ≈85% by 27 of 36.
- **Matched-chronology interchange, replicated across architectures.** With evidence
  after the rule on both sides and the unrelated preview padded to the paraphrase's
  token length, rule-span transfer runs both ways in a mid-network window:
  Qwen3-8B at layers 14–18 of 36 (relative depth 0.39–0.50), break **+13.3
  [+8.1, +18.9]**, rescue **−3.6 [−5.9, −1.4]**; **Mistral-Small-24B** at layers 12–16
  of 40 (relative depth 0.30–0.40), behavioural gap **+18.2**, interaction **−15.6**,
  break **+15.7**, rescue **−13.4**, null above depth 0.45. The overlapping
  mid-network window is the invariant; Qwen's rescue/break asymmetry is not.
- **Attention correlate.** The rule:evidence per-token attention ratio at the answer
  position tracks the behavioural rescue (2.14 → 2.68 → 2.64). Reported as a
  correlate, not an explanation.

**Correction inside the round.** The first version reported medians of a recovery
fraction whose denominator is often a few points; it overstated the effect and was
replaced by rating-point shifts on the pooled 70 items.

**Paper role.** Section 7.
**Results.** `stages/STAGE5.md`, `results/mech/`.

## A9. G16 — binding-state interchange: **bridge-failed**

**Question.** Is the difference between a policy that works before the evidence and
one that does not a specific, causally manipulable internal state?

**Design.** Interchange the late binding state between tag-bound and
identifier-bound prospective conditions, both directions, matched chronology,
matched length, matched control direction. Frozen at
`g16-binding-interchange-design-v1.1` before any generation; Amendment A1 corrected
the readout to the mechanism's fixed-position direct readout, also before any output.

**Result.** Gate 1 was a preregistered stopping rule and it failed, so **the patched
phase was never executed** (300 baselines, 0 patched generations). The frozen
per-arm-anchor bridge is −8.11 [−11.47, −5.07] against a +5 floor. A post-result
diagnostic shows why: `cls_admit` asks the model to give an item marked unauthorised
the full weight of a verified one, and it does not comply, so that anchor collapses
(gap +8.00 [+5.00, +10.82]). Re-scored against a common anchor — Stage 3A's own
estimator — the bridge is a precise null, **−0.11 [−5.62, +5.20]**.

**Cause, resolved in A10.** Not the construction — the readout. §5's class-marker
claim rests on **Stage 3B** (A4), whose tagged-stream result has exact ground truth,
five models and both arms, and which no readout question touches. The mechanism
section closes on Stage 5 plus the span gate.

**Results.** `results/mech/g16_binding_interchange_results.md`,
`g16_freeze_checklist.json`, `g16_baselines.json`, `g16_analysis.json`.

## A10. Readout validity on the binding contrast — **the mechanism readout is blind to it**

**Question.** Did G16's null come from its padded construction, its sample, or the
fixed-position readout every mechanism round in this project uses?

**Design.** Two diagnostics. (i) Split the existing six-model Stage 3A data by family.
(ii) Run Stage 3A's byte-identical prompts — no padding, no changed grammar — through
the direct readout on Qwen3-8B and compare with the behavioural numbers already on
disk. Interpretation pre-committed in the script docstring before running.

**Result.** Sample excluded: on G16's own two families the behavioural class advantage
is −0.290 [−0.408, −0.164], slightly larger than in the three omitted families
(−0.245 [−0.366, −0.126]). Padding excluded, readout confirmed: on identical prompts,
behavioural gives −0.503 [−0.754, −0.249] and direct gives **+0.045 [−0.124, +0.232]**.

The direct readout is not globally blind to binding — it tracks rule position at
r = 0.76 / 0.90 and content-preview binding at +8.56 with a −12.11 interaction
(Stage 5). It misses the class-marker form specifically.

**Paper role.** A scope limit that must be stated next to the readout description, not
in an appendix: the mechanism speaks to rule position and content-preview binding, not
to class-marker binding. It also extends B4 — `metric_audit.md` warned before the
freeze that single-token readouts can dissociate from the model's own reasoning; this
is a concrete instance found in our own results.

**No successor.** Matched-chronology interchange needs aligned token positions, and a
generated rationale differs per condition and per item. This is a methods limit, not a
compute limit.

**Results.** `results/mech/readout_validity_binding_results.md`,
`readout_validity_binding.json`; code `src/mech/readout_validity_binding.py`.

## A11. G17 — is the binding requirement specific to complete suppression?

**Question.** The paper asserts two regularities (A3's w=0 discontinuity, A4/A6's
binding requirement) and never crosses them. Are they one?

**Design.** Preview `{none, para}` × requested weight `{0.00, 0.25, 0.50}`, rule always
before the evidence, plus a no-rule base and a w=1.00 admit anchor. 2,400 generations,
four checkpoints. Frozen at `g17-binding-by-weight-design-v1` before any generation.

**Result — split, both halves reported.** The frozen verdict is **`no-rescue`**, on a
REI estimand that blows up (one item at REI 8,492) — the ratio instability Stage 3E had
already documented and solved. The post-result re-analysis in raw rating points, the
Stage 3E estimator, gives rescue **+10.09 [+7.03, +13.26]** at w=0 and null at both
non-zero weights, interaction **Δ = +9.30 [+6.11, +12.65]** — exactly the predicted
pattern.

**Paper role.** None yet. A post-result estimator switch that produces the predicted
answer is not a confirmation. §4 and §5 stay separate; the paper says why. A prospective
confirmation with raw points as the primary estimand, a leverage floor fixed in advance,
and per-preview baseline cells would settle it.

**Results.** `results/g17_binding_by_weight_results.md`,
`results/g17_binding_by_weight_analysis.json`; code `src/conditions_g17.py`,
`src/analyze_g17.py`.

## A12. G18 — prospective semantic targeting: **confirmed**

**Question.** Does prospective exclusion succeed only when the model has a
sufficiently specific *semantic* representation of the target at rule time, as opposed
to a reference to it, a lexically similar description with a different meaning, or
nothing?

**Why it exists.** The centrepiece regularity was discovered through a chain that
rebuilt the design (Stage 3D) and changed the metric (Stage 3E) in response to what
each round showed. Every change was justified; together they meant the claim had never
been measured by a design built for it, on items it was not discovered on.

**Design.** 6 × 3 factorial: target representation `{none, ident, empty, para, entail,
unrel}` × rule state `{preview only, preview+evidence, preview+rule+evidence}`. Every
level carries its own no-rule baseline. Raw sign-aligned rating points, no ratio.
**100 fresh items, 30 independent skeletons**, three families, disjoint from
`items_v1.jsonl` by build-time assertion. Five checkpoints, four vendors, 9,000
generations. Frozen at `g18-semantic-targeting-design-v1` before any run.

**Result.** Both gates pass. Pooled `ExclusionEffect`: entail 31.16, para 30.93,
ident 26.27, unrel 22.06, none 21.84, empty 18.08. **Δ_semantic = +8.91
[+7.15, +10.76], positive in 5 of 5 models**; the length- and lexically-matched
contrast **para − empty = +12.85 [+10.32, +15.42]**, positive in 5 of 5 (interval
excludes zero in 4; Phi-4-mini is +3.50 [−1.06, +8.57]).

**The decomposition, reported in the paper not the appendix.** Under a semantic
preview the evidence is largely redundant (`marg(no rule)` falls from ~32 to ~3), and
the rule then drives the judgment ~28 points **below** the preview-only baseline —
negative in 5/5 under `para`, positive in 5/5 under `empty`. With a semantic target,
exclusion follows the proposition into text the rule never named.

**Paper role.** Contribution 2, confirmed. Per the preregistration this **closes the
experimental programme**.

**Results.** `results/g18_semantic_targeting_results.md`,
`results/g18_semantic_targeting_analysis.json`; code `src/gen_g18.py`,
`src/conditions_g18.py`, `src/analyze_g18.py`; items `data/items/g18_v1.jsonl`.

---

# B. Supporting characterisation

Sharpens the main result; must not become separate narrative branches.

- **B1. Ruling paraphrases.** Eight constructions × five models; the counterfactual
  phrasing is the *worst* prospectively. `results/paraphrase_tables.md`.
- **B2. Cluster robustness.** Resampling the 38 case skeletons rather than items
  barely widens intervals. `results/cluster_robustness.md`.
- **B3. Reproducibility.** Qwen3-8B run twice end to end; aggregate estimates move by
  at most 0.06 REI against effects of 0.2–0.6, but 6.9% of cells differ by >5 points
  because vLLM batching is not bitwise deterministic.
- **B4. Readout methodology.** Three piloted readouts failed before the freeze:
  greedy integers collapse to four values; a single-token rating can anti-correlate
  with the model's own stated reasoning; a 6σ outlier is silently discarded even
  when the rule says to use it. `results/metric_audit.md`.
- **B5. External boundary checks.** Ramsey/Liu/Trueblood medication reports and the
  Baron-Hershey/Aiyer vignettes. Retained as **boundary checks**, not an
  independently authored held-out tier — see the provenance correction at the top of
  `results/external_tables.md` and `stages/DATASET_REDESIGN.md`.

---

# C. Stopped branch — BTF-3 hindsight

Stopped 2026-09-03. Retained in full for provenance and because one result is held
as a separate lead. Not part of the current paper. Reasons are in
`RESEARCH_HISTORY.md` §5.

- **C1. BTF-3 temporal replication.** 8-item discovery → 64-item prospective
  confirmation → 256-item fresh replication. Qwen 16.02, Gemma 27.73, Mistral 7.46pp.
  `results/btf3_large_replication_v1_results.md`.
- **C2. G2 Experiment B — verdict redaction.** Contamination *increases* when the
  explicit verdict is removed, 3/3 models. **Held as the second lead** —
  `SECOND_LEAD_EXPLICIT_OUTCOME_PARADOX.md`.
- **C3. G2 Experiment A — positional replication.** Panel gate not met (1/3); the raw
  effects reproduce the earlier pattern in the same two models. This is the natural-
  substrate echo of the main line's positional result and is *not* claimed as a
  replication of it.
- **C4. G8 / G11 / G12.** Foreign-packet, verdict-redacted, and paired
  outcome-direction rounds. G12's original Qwen/Gemma/Mistral panel verdict is
  `indeterminate`. All three are robust to excluding the 34 leaking packets.
- **C5. G13 → G14 → G15.** Packet-local null, answer-site discovery, fresh
  preregistered confirmation of a late recipient-conditioned decision state
  (Gemma-only). `results/mech/g1[345]_*`.
- **C6. G3 exclusion reason, G4 model breadth, Qwen3.5 size sweep.** G4 analysed 5 of
  a preregistered 17 checkpoints. **The remaining 12 will not be run** — completing a
  preregistration for a stopped branch is bookkeeping, not science.
- **C7. Indeterminate or failed rounds.** G5 deliberation, G6 early mechanism, G7
  ex-ante anchor (prediction failed in the opposite direction), G9 numeric, G10
  worked-example mitigation.
- **C8. Data-integrity corrections.**
  `preregistrations/POSTHOC_REDACTION_AUDIT_CORRECTION.md` — the redactor's
  conditional-marker bypass leaves 34/256 packets asserting the outcome and the
  frozen audit could not detect it; and the Llama boundary-probe figure was reported
  at single-frame scope (73.63% over both frames, licensed arm 49.61%). Neither
  changes a preregistered verdict.

---

# D. Earlier narrowing rounds

- **D1. G1 and the factorization rounds.** The attempt to generalise across boundary
  types. BTF-3 qualified; FANToM did not; FOMC failed its gate. This forced the
  detour described in `RESEARCH_HISTORY.md` §4.

---

# E. Preregistrations

Exact text in [`preregistrations/`](preregistrations/), indexed by its README. Git
freeze commits and tags remain the authority for chronology relative to model
outputs.
