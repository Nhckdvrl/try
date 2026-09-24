# Paper outline — prospective semantic exclusion

**Updated:** 2026-09-24 after the G18-style triviality re-audit; RQ2 reframed
same day per `PAPER_RQ2_BOUNDARY_REFRAME.md`.

## Working title

> **Can Language Models Commit to Ignore Future Evidence?**

---

## 1. Introduction

Natural setup: policies often precede the information they govern.

Mother question:

> **Can an LLM commit now to make future evidence causally irrelevant?**

Current contribution structure:

1. **Prospective exclusion asymmetry / natural-evidence leak.**
2. **Sharp exact-zero boundary vs smooth weighting in semantic prospective
   control** (pending the natural-evidence confirmatory; see
   `PAPER_RQ2_BOUNDARY_REFRAME.md`).

Stage 5 / G23C / G24B are supporting causal evidence, not a third headline contribution.

A third RQ is optional and remains open. Add it only if it passes the reviewer-obvious
veto.

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

Reframed per `PAPER_RQ2_BOUNDARY_REFRAME.md` (2026-09-24). The old form
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

### 4.3 Confirmatory — fresh natural near-zero sweep (planned, STATUS-gated)

Held-out items from the frozen G24A candidate pool, **disjoint from the
selected 600**, reusing existing Base/Admit-only selection outputs (no new
selection compute; selector blind to Exclude). `w ∈ {0,1,2,5,10,25,100} ×
{PRE,POST}`; primary estimands `Gap(0)−mean[Gap(1),Gap(2),Gap(5)]` and
`Gap(0)−Gap(1)`. Both outcomes informative: sharp jump → boundary headline;
smooth curve → boundary downgraded and folded into RQ1. Design only until the
five gates close and STATUS flips. Details: `PAPER_RQ2_BOUNDARY_REFRAME.md` §6.

### 4.4 Policy-access controls

Correct rule recall / requested-weight access shows that simple forgetting is
insufficient. Supporting evidence only.

### Finding 2 (draft — pending confirmatory)

> **Semantic prospective control exhibits a sharp exact-zero boundary rather
> than a smooth difficulty curve: the pre/post timing gap is flat across
> requested weights from 1% to 50% but jumps discontinuously at exactly 0% —
> although 0% and 1% require nearly identical suppression — and exact zero is
> executed perfectly when the contribution is explicitly arithmetic.**

Licensed form that must stay reachable (register §12.3):

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

## 6. Open third question — only if non-trivial

Current candidate: **scope of a prospective exclusion policy** — can a model
exclude one future evidence piece without leaking through it or collaterally
suppressing related evidence? Systematic novelty audit **complete: PROCEED
with narrowing, no parent-level prior found** (`PAPER_RQ3_SCOPE_NOVELTY_AUDIT.md`).
Still **not registrable** — it must survive the gates below first.

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
