# Paper outline — prospective semantic exclusion

**Updated:** 2026-09-24 after the G18-style triviality re-audit; RQ2 reframed
same day per `PAPER_RQ2_BOUNDARY_REFRAME.md`; **G25A ruling recorded later
2026-09-24 — natural confirmatory verdict `order-artifact` accepted as
NO-CLAIM (no rerun / no correction / no G25B), natural exact-zero-boundary
headline WITHDRAWN; RQ2 = controlled-material supporting analysis; RQ3
(G26A, O1–O9 signed) = sole active headline candidate.**

## Working title

> **Can Language Models Commit to Ignore Future Evidence?**

---

## 1. Introduction

Natural setup: policies often precede the information they govern.

Mother question:

> **Can an LLM commit now to make future evidence causally irrelevant?**

Current contribution structure (post-G25A ruling, 2026-09-24):

1. **Prospective exclusion asymmetry / natural-evidence leak.** — sole
   standing headline finding.
2. ~~Sharp exact-zero boundary vs smooth weighting in semantic prospective
   control~~ — **WITHDRAWN as a headline.** The preregistered natural
   confirmatory (G25A) returned the frozen verdict `order-artifact`
   (no-claim; smooth ladder + graded response observed; S1 and G2 also
   independently failed) and no rescue is authorized. G23A's zero
   amplification + arithmetic-zero executability survive as
   **controlled-material supporting structural analysis** (§4).

Stage 5 / G23C / G24B are supporting causal evidence, not a third headline contribution.

**RQ3 — load-bearing emergence (G26A) — is now the sole active headline
candidate** (§6; `PAPER_RQ3_CANDIDATE_AUDIT_2026-09-24.md`): must an
exclusion policy's target already be decision-effective through
composition when the policy is processed. O1–O9 signed 2026-09-24;
implementation/freeze path active (Phase A = mistral selector, ≤ 14,568
rows, STATUS-gated). It enters the paper only if its prereg gates clear;
otherwise fall back to the one-finding + supporting-analysis paper.

---

## 2. Common setup and distinction from prior work

Define:
- evidence causal eligibility;
- prospective vs retrospective exclusion;
- why this is not generic instruction position, memory availability, belief revision,
  or in-context unlearning.

Keep the novelty object on **future evidence use**, not generic policy compliance.

---

## 3. RQ1 — Can models pre-commit to ignore future evidence?

### 3.1 Controlled breadth

G0:
- 144 items;
- five task families;
- broad instruction-model panel;
- matched Admit control.

### 3.2 Obvious-explanation controls

- wording robustness;
- rule-to-evidence delay;
- policy probes;
- masked-diffusion comparison.

These are controls, not separate findings.

### 3.3 Agent-like role structure

System policy -> future tool output -> assistant decision.

### 3.4 Source-grounded natural evidence

G24A:
- FEVER + SciFact;
- 600 selected items;
- five models;
- frozen verdict `prospective-only`.

Report exact scope:
- pooled prospective leak passes;
- retrospective leak is not distinguishable from zero;
- model/source consistency is heterogeneous.

### Finding 1

> **Prospective exclusion is systematically weaker than retrospective exclusion, and
> source-grounded future evidence can remain influential despite a prior zero-use
> ruling.**

---

## 4. RQ2 — Smooth weighting problem, or an exact-zero control boundary?

**Status after G25A (ruling 2026-09-24): CONTROLLED-MATERIAL SUPPORTING
ANALYSIS — the natural-data boundary headline is withdrawn and this
section sells no boundary.** Reframed per `PAPER_RQ2_BOUNDARY_REFRAME.md`
(2026-09-24). The old form
(“what is special about `w=0`”) dies to the one-liner *“zero is a stricter
requirement than partial use.”*

> **RQ2: Is prospective exclusion a smooth evidence-weighting problem, or is
> exact semantic zero a qualitatively different control boundary?**

### 4.1 The weight ladder — flat, then a jump at exactly zero

G23A pooled ladder (raw sign-aligned points, cluster bootstrap):

- `Gap(100)=−0.27 [−2.26,+1.86]` — admit anchor: no generic order effect;
- `Gap(50)=+4.51 [+2.47,+6.50]`, `Gap(25)=+4.99 [+3.09,+6.95]`,
  `Gap(1)=+5.59 [+2.77,+8.36]` — flat plateau;
- `Gap(0)=+13.86 [+8.54,+19.18]` — decisive contrast is **0 vs 1**:
  one point of demanded suppression, **8.27 points of gap**;
- `Delta_zero=+8.83 [+4.39,+13.33]`; attenuation mean `+5.03 [+3.16,+6.83]`;
  3/3 model means positive (mistral model-level CI crosses 0 — claim pooled only).

Step sizes do not track suppression demand (100→50 costs 50 points of
suppression for ≈+4.8; 1→0 costs 1 point for +8.27) → the graded-demand
account fails descriptively. Do not sell “zero is harder”.

### 4.2 Exact zero is not intrinsically difficult — arithmetic boundary

Stage-3C: contribution stated explicitly as `base + w·delta`. **4/5 models
execute prospective `w=0` exactly**; Qwen3.5-27B exact at every weight in both
arms. This refutes the prohibition-cost account and pins the object: the
failure emerges when zero applies to the *inferred causal contribution* of
semantic evidence.

### 4.3 Confirmatory — natural near-zero sweep: EXECUTED, VERDICT `order-artifact`, NO CLAIM

Ran exactly once as preregistered (G25A, tag `g25a-near-zero-design-v1`,
STATUS flip recorded; 400 disjoint held-out items × 7 weights × pre/post ×
pooled-4 = 28,800 rows; frozen analyzer, seed 20260924, B = 10,000,
cluster bootstrap). Frozen verdict: **`order-artifact`** —

- **I1 FAIL**: Gap(100) = −1.06 [−1.93, −0.21] — the 100% anchor showed a
  small but systematic order effect (4/4 models negative; integrity
  investigation: tail-concentrated in 15.6% argmax-digit flips, digit-mass
  valid, G0–G24A readout lineage — a real position effect, not a bug);
- **S1 FAIL** 354/400 < 360 and **G2 FAIL** on the 3.0 floor
  (2.83 [+0.49, +5.11]) — each independently blocking
  `exact-zero-boundary`; G1 passed (+3.58 [+1.33, +5.79]), I2 RuleAcc
  0.949, G3 3/4;
- the natural ladder came out **smooth** — 10.58 → 7.76 → 6.90 → 6.36 →
  5.60 → 3.59 → −1.06 across w = 0…100% — with graded
  GradedPos +20.81 [+19.12, +22.50] (descriptive; never a gate).

**Ruling (2026-09-24): accepted as no-claim. No rerun, no correction, no
bias subtraction, no G25B.** Reported honestly: a preregistered
natural-data confirmation that became non-interpretable under its own
frozen integrity criterion; local contrasts suggestive but incomplete
against the preregistered gate set. §4.1–4.2 (G23A + Stage-3C) remain as
controlled-material supporting analysis.

### 4.4 Policy-access controls

Correct rule recall / requested-weight access shows that simple forgetting is
insufficient. Supporting evidence only.

### Finding 2 — WITHDRAWN as a natural-data headline (ruling 2026-09-24)

> ~~**Semantic prospective control exhibits a sharp exact-zero boundary
> rather than a smooth difficulty curve: the pre/post timing gap is flat
> across requested weights from 1% to 50% but jumps discontinuously at
> exactly 0% — although 0% and 1% require nearly identical suppression —
> and exact zero is executed perfectly when the contribution is
> explicitly arithmetic.**~~

**Withdrawn** — the natural confirmatory (§4.3) returned
`order-artifact` NO-CLAIM with a smooth graded ladder; no natural-boundary
sentence ships. What survives is the register §12.3 licensed form,
**scoped to its actual evidence base (controlled materials + arithmetic
executability)**:

> **Complete semantic causal exclusion shows an additional prospective cost
> even though prospective zero can be executed exactly when the contribution is
> explicit and verifiable.**

---

## 5. Mechanistic evidence for the behavioral findings

This section is explanatory, not a separate contribution.

### 5.1 Stage 5 — rule-time causal window

Same chronology; target-context manipulation; two architectures.

### 5.2 G23C — policy-state interchange

Report the preregistered L14 target-conditioning effect and negative-layer controls.

### 5.3 G24B — donor/recipient factorization

Fix recipient prompt and show donor-side policy interaction remains:
`DTI = +4.02 [+2.27,+6.14]`.

### Interpretation limit

These results show causal involvement of the rule-time state.

They do **not** by themselves yield a surprising law that “target-present states are
more target-conditioned”; that consequence is too close to the visible manipulation.

G23C-R is HOLD until a stronger parent question exists.

---

## 6. Third question — candidate chosen: load-bearing emergence

Six-candidate novelty screen complete (2026-09-24), decision record
`PAPER_RQ3_CANDIDATE_AUDIT_2026-09-24.md`:

- **SURVIVOR → prereg-draft track: load-bearing emergence** —

  > **RQ3: Does prospective exclusion require the target evidence merely to
  > be present, or must it already be load-bearing through composition when
  > the policy is processed?**

  HoVer 2-hop, timings T0/T1/T2 (rule before A / between A,B / after B) with
  identical final context; no-rule gates force a genuine composition
  (`joint ≥ 15`, singles `≤ 5`); outcome = `PresenceGain` /
  `LoadGain` against the `Y_B` counterfactual; distance-matched +
  admit-timing controls pre-registered. Branches content-bound /
  relevance-bound / staged / flat — all informative.
- **BACKUP pilot only:** exclusion vs negation (gold semantics dirty on
  natural evidence).
- **KILLED:** hop depth (crowded + trivial), post-training origin (parent
  collision), scope/collateral suppression (this section's former candidate —
  superseded after a broader prior pass; see banner in
  `PAPER_RQ3_SCOPE_NOVELTY_AUDIT.md`), inferential closure (semantic-IFC
  parent).

Before any new experiment, require:

1. treatment does not contain the answer;
2. two plausible accounts differ under the same visible content;
3. reviewer cannot dismiss the expected finding in one obvious sentence;
4. the result would materially change the paper's scientific understanding, not just
   increase robustness.

If no candidate passes, omit this section and keep a two-finding paper.

---

## 7. Related work

- instruction position / forgetting;
- evidence use / belief revision;
- in-context unlearning / knowledge suppression;
- contextualization race conditions;
- latent task/function states.

---

## 8. Discussion

Emphasize:
- knowing a rule is not the contribution; semantic causal control is;
- zero is not intrinsically hard; semantic causal zero is;
- mechanism evidence is suggestive/explanatory but not inflated into novelty.

---

## 9. Conclusion

> **LLMs can understand a future evidence policy yet fail to make later semantic
> evidence causally inert; the failure is specifically stronger for complete semantic
> exclusion than for explicit/verifiable prospective zero.**
