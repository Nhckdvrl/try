# Section 3 draft (RQ1) — Can models pre-commit to ignore future evidence?

**Updated:** 2026-09-24. **Status:** section-level draft for the novelty-first
skeleton (`PAPER_OUTLINE.md` §3). Every number is copied from frozen result
files (paths cited inline); licensed wording is quoted verbatim; `⚠` marks a
pre-submission flag (collected in the final subsection).

---

## 3.0 Setup and estimand (recap; full definitions in §2)

Two orderings of the same rule and the same evidence:

```text
PRE:   Base → Exclude rule → Evidence E → judgment      (pre-commitment)
POST:  Base → Evidence E → Exclude rule → judgment      (cancellation)
matched: admit rule in both positions (no exclusion)
```

**REI** (relative evidence influence) is the effective weight the judgment gives
E: `0` = judged as if E had never been admitted, `1` = used exactly as when the
admit rule permits it; signed by the item's admit leverage `L = mean(admit_pre,
admit_post) − base`, winsorised at ±3. CIs: 10,000-resample item-level paired
bootstrap (cluster bootstrap over evidence clusters in §3.4). The **timing
gap** is always reported as `REI_pre − REI_post` (positive = prospective leak
larger). Sign conventions of source tables are preserved and labeled.

## 3.1 The same exclusion rule is weaker when it precedes its evidence (G0)

**Materials.** 144 frozen items across five task families — evidence inference
(30), legal judgment (45), numeric aggregation (21), outcome evaluation (21),
ranking/selection (27) — with a matched admit anchor per item. Panel: 12
instruction-tuned models from four vendors (Phi-4-mini; Gemma-3-4B/12B;
Qwen2.5-7B/32B; Mistral-Small-24B; Qwen3-4B/8B/14B/32B; Qwen3.5-9B/27B), plus
an independent replicate run of Qwen3-8B. Rules are understood: RuleAcc for the
exclude rule is 0.82–1.00 in both positions, and the admit-control pass rate is
≈1.0 in every family.

**Result.** In every model the exclusion rule is less effective when stated
before the evidence (Table 1). The paired timing gap is positive and
significant in **12/12 models** (`+0.15` … `+0.55`, all p < .05), and the
replicate run reproduces it (`+0.38 [+0.26,+0.51]`, p < .0001). Descriptively,
the direction `pre > post` holds in **59 of 65 model × family cells** (2 ties,
4 reversals; evidence-inference 13/13, legal 12/13, ranking 12/13, outcome
11/13, numeric 11/13) — see Appendix table A1.

**Table 1 — G0 main result** (`results/cross_model_tables.md` §1, §3;
REI means and paired pre−post contrasts; `n` = usable items of 144):

| model | REI_pre | REI_post | pre − post [95% CI] | p | n |
|---|---:|---:|---:|---:|---:|
| Phi-4-mini | +0.50 | +0.24 | **+0.26** [+0.08, +0.43] | .0052 | 138 |
| Gemma-3-4B | +0.43 | +0.28 | **+0.15** [+0.02, +0.29] | .0238 | 133 |
| Gemma-3-12B | +0.43 | +0.07 | **+0.36** [+0.27, +0.44] | <.0001 | 141 |
| Qwen2.5-7B | +0.54 | +0.22 | **+0.32** [+0.17, +0.48] | <.0001 | 134 |
| Qwen2.5-32B | +0.30 | +0.00 | **+0.30** [+0.16, +0.46] | <.0001 | 140 |
| Mistral-Small-24B | +0.19 | −0.03 | **+0.22** [+0.13, +0.32] | <.0001 | 141 |
| Qwen3-4B | +0.58 | +0.14 | **+0.44** [+0.27, +0.61] | <.0001 | 137 |
| Qwen3-8B | +0.45 | +0.12 | **+0.33** [+0.22, +0.45] | <.0001 | 144 |
| Qwen3-14B | +0.49 | −0.07 | **+0.55** [+0.45, +0.67] | <.0001 | 143 |
| Qwen3-32B | +0.21 | −0.09 | **+0.31** [+0.20, +0.42] | <.0001 | 143 |
| Qwen3.5-9B | +0.07 | −0.18 | **+0.26** [+0.06, +0.44] | .0156 | 136 |
| Qwen3.5-27B | −0.05 | −0.29 | **+0.24** [+0.10, +0.39] | .0002 | 142 |
| *Qwen3-8B (replicate)* | +0.49 | +0.10 | **+0.38** [+0.26, +0.51] | <.0001 | 144 |

The same exclusion rule, in the same words, against the same evidence, is
weaker when it must govern evidence the model has not yet seen. The phenomenon
is not specific to “bad” evidence: among items whose exclusion reason is
*true-but-forbidden* (normatively excludable despite being true), the timing
gap persists (e.g., Qwen3-8B `+0.37 / +0.20` pre/post; Appendix A2), so the
effect is not a shortcut that drops evidence judged unreliable.

> **Reviewer flag F1:** register §E1 says “12/12 direction, **10/12**
> intervals exclude zero”; direct recomputation gives 12/12 significant
> paired contrasts (§3 of the source table) and 11/12 excluding-zero CIs on
> the `delta_time` column (§1). Three numbers, two estimators — resolve and
> pin one estimator before submission (see flags).

## 3.2 Controls: the gap is not generic order, forgetting, or availability

### 3.2.1 Matched admit has no analogous order effect

Under the admit rule, REI stays at ceiling in both positions for every model
(`admit_pre` 0.91–1.02, `admit_post` 0.96–1.08). The admit order difference is
`−0.17 … +0.04` (mean ≈ −0.03) — same direction as “pre less effective”, but
**~10× smaller** than the exclusion gaps in the same models (`+0.15 … +0.55`),
and bounded by the anchor ceiling. A generic “earlier instructions work worse”
account predicts a comparable shift for the admit rule; it is absent at
comparable magnitude.

### 3.2.2 Eight rule wordings preserve the gap

Eight independent rule constructions (legal-formal, plain, causal,
counterfactual, weighting, policy, relevance, procedural), each with its own
admit anchor, in five models (`results/paraphrase_tables.md`). The mean
pre−post gap per wording ranges `+0.26 … +0.54`, and the gap is positive in
**5/5 models for every one of the eight wordings**. The asymmetry is a property
of prospective exclusion, not of any sentence.

### 3.2.3 Delay and distance do not create the gap

Two independent manipulations (`results/stage2_tables.md`,
`stages/STAGE3.md` §B):

- *Rule → answer distance* (qwen3-8b, exclusion arm, n = 858): the position
  effect is large (`Before = +0.379 [+0.225,+0.538]`, p < .0001) while the
  distance slope is null (`−0.003 [−0.020,+0.013]` per 100 tok, p = .75). The
  gap persists at the largest distance (`pre .272` vs `post .095` at ≈626 tok).
- *Rule → target distance* (filler between the rule and its evidence, 0 →
  ≈1000 tok; three models): the **prospective arm is flat** — qwen3-8b
  `+.517 / +.471 / +.487 / +.583`, gemma3-12b `+.436 / +.325 / +.364 / +.327`,
  phi4-mini `+.635 / +.689 / +.665 / +.643` — it fails at full size with the
  rule directly abutting the evidence and is no worse a thousand tokens
  earlier. The retrospective arm is the one that decays (qwen post
  `.175 → .280`; gemma `.085 → .389`), so delay narrows the gap only by
  degrading the working arm, never by rescuing the failing one
  (`stages/STAGE3.md`: “not a maintenance or recall failure”).

This also blocks the **evidence-freshness** one-liner (in PRE the evidence sits
closer to the judgment): if freshness of E drove use, retrospective leak should
*fall* as filler grows (E moves away from the judgment); it *rises*
(`.085 → .389` in gemma-12b). Admit cells are at ceiling in both positions, and
the system-persistent policy in §3.3 is present at decision time by
construction. (`⚠ F6`: no single matched-adjacency control exists; the block is
convergent, not decisive.)

### 3.2.4 Policy access is not sufficient for enforcement

Models can often state the policy they are failing to apply. In G0, Qwen3-8B
re-states the exclude rule correctly in 0.997 of pre trials while still leaking
`REI_pre = +0.45`. In the frozen G23A round, `requested_weight_access_ok = true`
and the preregistered dissociation outcome D fired: the model can state the
requested weight while only the zero condition leaks. Trajectory probes show
Qwen3-8B and Gemma-3-12B explicitly writing that the evidence should receive
zero weight while the evidence still moves the judgment (Phi-4-mini does not
show this strong dissociation — scope the claim: *at least in some models*).
Remembering/stating the exclusion policy is not sufficient for making the
excluded evidence causally inert.

### 3.2.5 Restating the rule after the evidence restores exclusion

Condition `exclude_pre_repeat` (`B → R → E → R`: the rule is also restated
after the evidence, just before the judgment). Restatement pulls the pre arm
down to post-arm levels (Qwen3-8B `.45 → .07`; paired `pre − pre_repeat`
`+0.18 … +0.47`, significant in 13/13 rows; matched admit restate changes only
`−0.15 … +0.08`, ceiling-bounded, `⚠ F8`). Read correctly this is not a decay
result: a rule re-delivered *after* the evidence is a fresh retrospective
rule — the same operation as the POST arm. The scientific object is whether the
**prior statement alone** binds; §3.3 keeps a policy that is present at
decision time by construction and still fails.

### 3.2.6 The gap is not a causal-attention artifact

Under an identical fixed-position readout, two masked-diffusion LMs show the
same asymmetry: LLaDA-8B `pre − post = +0.31 [+0.21,+0.43]`, p < .0001;
Dream-7B `+0.42 [+0.35,+0.49]`, p < .0001 — alongside causal controls
(+0.17 … +0.43) in the same table (`results/cued_diffusion_tables.md`).
Bidirectional decoding does not remove the prospective cost.

*(Cross-reference, §4: when the contribution is stated arithmetically,
prospective `w=0` is executed exactly by 4/5 models — the failure is not a
generic inability to execute a future zero rule.)*

## 3.3 The same failure under agent-like roles (Stage-4A)

Real chat roles, 75 legal/inference items: `SYSTEM` carries a policy about a
document that has not been retrieved yet; the document arrives in a `TOOL`
message; the assistant then answers. REI is anchored on the no-policy and
admit baselines (`stages/STAGE4.md`, `results/agent_marginal.md`).

**The temporal reversal transfers.** Delivering the *identical* policy after
the tool output improves exclusion in all three models: Qwen3-8B `1.014 →
0.380`, Gemma-3-12B `0.386 → 0.191`, Phi-4-mini `0.940 → −0.156` (ID-only
policy, pre vs post delivery). The policy is a persistent system message —
present at decision time by construction — yet in Qwen3-8B and Phi-4-mini an
ID-only system policy leaves the document's influence at naive levels
(`+1.014` vs `+0.991`; `+0.940` vs `+1.038`): availability and recency of the
policy are fully controlled and the exclusion still fails.

**Policy content matters, heterogeneously.** A policy that quotes the
document's full proposition reduces influence in Qwen3-8B (`1.014 → 0.602`) and
Phi-4-mini (`0.940 → 0.753`) but not in Gemma-3-12B (ID-only `0.386` is its
best cell). In the deconfounded readout that credits the policy only for
suppressing the *later* tool marginal (`AgentExclusionEffect`, marginal
influence of the document given the policy already in context): Qwen3-8B
ID-only `−0.3 [−3.1,+2.3]`, p = .85 vs proposition `+10.3 [+6.3,+14.6]`,
p < .0001; Gemma-3-12B ID-only `+15.8 [+12.2,+19.6]`, p < .0001, proposition
`+17.4 [+13.7,+21.2]`. Which policy form suffices is model-dependent; the
temporal reversal itself is not (`⚠ F9`: report both cells — “an ID-only
system policy can do nothing” is a Qwen/Phi result, not a universal one).

## 3.4 Source-grounded natural evidence (G24A)

Templated vignettes are the easiest reviewer target, so the same pre/post
design runs on human-annotated claims and evidence: FEVER + SciFact, 600
selected items (quotas 200/200/100/100, selection blind to Exclude outcomes,
τ = 10.0, seed 20260924), five frozen panel models; the selection model
(mistral-small-24b) is excluded from the primary pooled-4 because the item set
was conditioned on its own Admit leverage. Influence is measured against each
item's signed leverage; CIs are 10,000-resample cluster bootstraps over
`source/doc` clusters (469 clusters; median |L| = 32.7). Sufficiency gate:
595/600 items usable; RuleAcc 1.000 in both arms; admit-control pass 0.974
(`results/g24a/g24a_analysis_v1.{md,json}`; prereg
`g24a-natural-evidence-confirmation-design-v1`).

**Frozen verdict: `prospective-only`.** Licensed claim, verbatim (prereg §8):

> **Natural evidence leaks even when the zero-use ruling precedes it, but the
> retrospective arm is not distinguishable from zero.**

Numbers: pooled-4 `REI_pre = +0.541 [+0.477,+0.603]`, p < .0001 (P1 PASS);
`REI_post = −0.067 [−0.158,+0.021]`, p = .13 (P2 FAIL);
`d_time = −0.543 [−0.613,−0.474]`. Pooled-5 (incl. selector): `+0.395 /
−0.081`. **Consistency clauses failed and must be reported as such** (register
§12.2: do not claim uniform replication): C1 (both REI > 0 in ≥4/5 models)
failed — 2/5 (gemma3-12b `+0.214/+0.139`; qwen3-8b `+0.750/+0.295`;
llama31-8b `+0.453/−0.290`; qwen35-9b `+0.762/−0.450`; selector
`−0.100/−0.129`); C2 failed — FEVER post `−0.106` (fail) vs SciFact post
`+0.007` (pass); prospective leaks are strong in both sources (FEVER
`+0.523`, SciFact `+0.575`). Label strata (descriptive, Appendix A3):
contradiction-direction evidence leaks even retrospectively (FEVER/REFUTES
`+0.846 / +0.590`; SciFact/CONTRADICT `+0.923 / +0.968`), while
support-direction cells show negative retrospective values (FEVER/SUPPORTS
post `−0.732`; SciFact/SUPPORT post `−0.879`) — the timing asymmetry lives in
the support-direction strata; no claim is licensed beyond §8 wording.

### Finding 1 (register §12.2, verbatim)

> **Prospective evidence exclusion is systematically weaker than retrospective
> exclusion, and source-grounded natural evidence can still remain influential
> under a prior zero-use ruling.**

## 3.5 Figure and table allocation

| slot | content | source |
|---|---|---|
| **Fig. 1** (page 1–2) | PRE/POST/admit schematic + per-model timing-gap forest plot (12 models + replicate + 2 diffusion LMs) | Table 1, `cued_diffusion_tables` |
| **Table 1** (main) | G0 per-model REI pre/post, paired gap, RuleAcc, n | `cross_model_tables` §1/§3 |
| **Table 2** (main) | Controls matrix: admit / wording ×8 / delay ×2 / probes / restatement / diffusion — one row each, key statistic, account it blocks | §3.2 sources |
| **Fig. 3** (main) | G24A per-model REI_pre vs REI_post with CIs + pooled-4/pooled-5 | `g24a_analysis_v1.md` |
| **Table 3** (main) | Stage-4A: key rows (naive / ID / proposition / after-tool) × 3 models + deconfounded effects | `STAGE4.md`, `agent_marginal` |
| Appendix A1–A3 | family cells (65), true-but-forbidden stratum, G24A source×label strata | cited tables |

(Sasano calibration: main results in the main paper; strata detail is
appendix.)

## 3.6 Nearest-prior defense and reviewer one-liners

**Three axes kept separate** (register §4):

```text
forgetting / unlearning:      is the information available or output?
belief revision:              what should currently be believed?
this paper:                   may this evidence causally contribute to this decision?
```

Nearest priors and the exact delta:

- **Instruction position** (Findings ACL 2024): generic pre/post instruction
  effects in generation. Delta: matched admit (§3.2.1), distance-null
  (§3.2.3), probes (§3.2.4), natural evidence (§3.4), persistent system policy
  (§3.3) — the object is *causal eligibility of future evidence*, not
  instruction recency.
- **In-context unlearning** — Takashiro et al. (Findings ACL 2025;
  query-conditioned “forgetting” with late-layer representation intact),
  Youssef et al. (NAACL 2025; reversing an existing in-context edit),
  Pawelczyk et al. (ICML 2024; in-context approximation of training-data
  removal). Their objects are availability/output or parametric influence;
  ours is whether *current-context evidence* may contribute to *this*
  decision — and, prospectively, whether a *prior* policy binds at all.
- **Belief revision** (EMNLP 2024): what to believe given new premises; here
  evidence can be fully believed yet causally excluded (true-but-forbidden
  stratum, §3.1).
- **Representation vs deployment** (ACL 2026 Main): generic flexibility of
  in-context representations. We never claim that frame; every claim stays on
  temporal direction of causal eligibility of future evidence.

**Strongest one-liner compressions → blocking data:**

| “这不是当然的吗？” | blocked by |
|---|---|
| “instructions earlier just work worse” (recency/position) | admit gap ~10× smaller; distance slope null; retrospective leak *rises* with E-distance (opposite of freshness); persistent system policy still fails |
| “they forgot the rule” | RuleAcc/probes access; restatement works; arithmetic future-zero exact (4/5) |
| “toy templates” | G24A natural evidence pooled `+0.541`; agent role setting |
| “cherry-picked models” | 12 models × 4 vendors + replicate + 2 diffusion, direction 12/12, 59/65 family cells |
| “any pre-instruction is weaker” | admit control magnitude (§3.2.1) — position effect is exclusion-specific |
| “zero is just stricter” | → §4 (0-vs-1 boundary + arithmetic control) |

## ⚠ Pre-submission flags (resolve before writing the final text)

1. **F1 — 10/12 vs 11/12 vs 12/12.** Register E1 says “10/12 intervals
   exclude zero”; `cross_model.json` `delta_time` CIs give 11/12;
   `cross_model_tables` §3 paired contrasts give 12/12 significant. Register
   written 2026-09-04 from data unchanged since 2026-08-27 — the 10/12 does
   not reproduce from either table. Pin one estimator, correct the register or
   the text.
2. **F2 — estimator mismatch.** Per-model `delta_time` in `cross_model.json`
   (e.g., phi4 −0.30) equals neither the difference of REI means (−0.26) nor
   the paired contrast (+0.26 magnitude). Direction always agrees. Document the
   estimator actually used in the paper.
3. **F3 — G24A wording lock.** Only the prereg §8 `prospective-only` sentence
   is licensed claim language; C1/C2 failures and selector exclusion must be
   stated; no “consistent across models/datasets” phrasing anywhere.
4. **F4 — family cells are descriptive.** 59/65 has no cell-level CIs; do not
   attach significance language to it.
5. **F5 — RuleAcc_pre < 0.90 in four models** (qwen2.5-7B .822, qwen3-14B
   .874, qwen3-32B .861, gemma-12B .889): policy re-statement is imperfect in
   the pre arm for some models; E2 claim stays scoped to “some models”.
6. **F6 — evidence-freshness** has no direct matched-adjacency control; the
   stage-3B/stage-2 arguments are convergent but indirect (§3.2.3).
7. **F7 — restatement compression** (“just restate the policy at decision
   time”): defense = restate-after-E *is* retrospective cancellation; the
   binding question is whether the prior statement alone binds — and the
   persistent system policy shows failure even with the policy present.
8. **F8 — admit restate controls** significant in 3/13 rows (qwen2.5-32B
   p = .001, qwen3.5-9B p = .0068, qwen3.5-27B p = .0052), ceiling-bounded;
   report the range, not a universal null.
9. **F9 — Stage-4A ID-only policy** helps only Gemma; keep both cells visible
   whenever the agent result is summarized.
