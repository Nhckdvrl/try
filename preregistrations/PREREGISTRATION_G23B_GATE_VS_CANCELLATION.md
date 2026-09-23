# G23B preregistration — standing gate vs retrospective cancellation

**Created:** 2026-09-23, after the frozen G23A v3 verdict and before any G23B
target-model generation.

**Status:** FROZEN DESIGN — committed and tagged
`g23b-gate-vs-cancellation-design-v1` on 2026-09-23, before any G23B generation.
§14 records the freeze and the three audit flags settled before tagging.
**NO G23B TARGET-MODEL COMPUTE IS AUTHORIZED BY THIS FILE.** Repository-level
authority for any generation lives in `STATUS.md` only.

G23A v3 established the preregistered `zero-amplified` result:

> `Δ_zero = +8.83 [+4.39,+13.33]` rating points, all three gates passed,
> `3/3` model-level `Δ_zero > 0`.

The licensed G23A claim is deliberately narrow:

> **The prospective timing gap is discontinuously amplified at `w=0` relative to
> non-zero weight instructions.**

G23A does not identify why. G23B asks the next behavioral question.

---

## 1. Scientific question

> **Does effective exclusion require an already-instantiated evidence state, or can
> exact semantic knowledge of future evidence support equally effective prospective
> control before that evidence becomes part of the judgment state?**

Short form:

> **standing gate vs retrospective cancellation**

The experiment separates three states at the moment the exclusion rule is processed:

```text
U — unresolved
    the future evidence content has not appeared

K — known but non-evidential
    the exact future proposition is available in a realistic proffer / offer-of-proof
    carrier that is explicitly not evidence for the merits judgment

I — evidentially instantiated
    the evidence itself has already entered the merits record before the rule
```

The central comparison is **K vs I**, not merely U vs I.

---

## 2. Why this experiment is needed

G0 and G23A jointly establish two constraints:

1. the same exclusion instruction is much less effective prospectively than
   retrospectively;
2. that timing penalty is additionally amplified at the zero-valued instruction.

These facts are consistent with at least two computational accounts.

### H-GATE — prospective target-conditioned control

The model can maintain an exclusion relation over future information, but success
depends on sufficiently resolving the semantic target before the rule is processed.

Prediction:
- exact target semantics before the rule should substantially rescue U;
- once the target is known, prior evidential instantiation should add little.

### H-CANCEL — retrospective evidence-state cancellation / revision

Natural-language exclusion is mainly effective after the target proposition has entered
the evidential / judgment state. The rule acts on an existing evidence state rather than
maintaining a reliable pending gate over unseen evidence.

Prediction:
- exact semantic knowledge in a genuinely non-evidential carrier is insufficient;
- exclusion becomes substantially stronger when the proposition has already entered as
  evidence.

A hybrid is possible and is a valid outcome.

---

## 3. Scope — one clean natural carrier, not a broad benchmark

G23B should begin with **one natural domain: legal judgment**.

Reason:
an attorney's **proffer / offer of proof** naturally exposes what a witness or document
is expected to say before the court decides whether it is admissible, while explicitly
distinguishing that preview from evidence on the merits.

This is used as an experimental instrument, not as a claim that the phenomenon is
legal-specific.

Recommended frozen material target:

- **60 fresh legal items**;
- **60 independent skeletons**;
- 30 evidence-increases / 30 evidence-decreases;
- no overlap in item id, surface case, or skeleton with G0/G18/G23A;
- no LLM-generated gold and no LLM-as-judge;
- continuous 0–100 merits judgment using the existing readout format.

Do not add other task families in the first G23B round. A second family is a later
replication only if the branch is scientifically worth extending.

---

## 4. The K carrier

For each item, let `E` be the critical evidence proposition.

The K condition contains a pre-rule proffer with the same semantic payload:

```text
OFFER OF PROOF — NOT EVIDENCE

For the limited purpose of deciding admissibility, counsel states the content
expected from [evidence label] when that evidence is later presented:

    <semantic payload of E>

This proffer is not admitted evidence and must not affect the merits judgment.
```

Freeze note (FLAG-3, settled 2026-09-23): the original draft slot — "counsel
states that the later [evidence label] is expected to report the following" — is
ungrammatical once plural evidence labels are substituted. Only agreement was
repaired; the header, purpose sentence, label reference, later-presentation,
expectation modality, indented payload and closing sentence are unchanged. The
rendered block in `src/conditions_g23b.py` substitutes `[evidence label]` with the
item's `critical_label` and the payload with `critical_evidence`.

The later actual evidence block uses the same proposition as evidence, with a different
role wrapper.

The proffer must not be described as uncertain, hypothetical, false, or unreliable.
Those would change the proposition rather than only its evidential status.

The proffer also must not say “ignore this because it is inadmissible”; that would add a
second exclusion instruction. It only states the institutional role: **known content,
not merits evidence**.

---

## 5. Two-stage design

The whole design is frozen before any generation, but execution is staged.

### Phase A — carrier qualification, no exclusion-rule outcomes

Generate only four cells:

```text
B      BACKGROUND -> judgment

P      BACKGROUND -> PROFFER(E) -> judgment

E      BACKGROUND -> EVIDENCE(E) -> judgment

PE     BACKGROUND -> PROFFER(E) -> EVIDENCE(E) -> judgment
```

No exclusion rule appears anywhere in Phase A.

This phase is allowed to answer only:

1. Is the proffer behaviorally close to judgment-neutral?
2. Does actual evidence still have positive marginal leverage after the proffer?

It cannot reveal the G23B branch because U/K/I rule conditions have not been generated.

### Phase B — branch test

Run only if the frozen carrier gates pass.

Three rule cells:

```text
U      BACKGROUND -> RULE(exclude E) -> EVIDENCE(E) -> judgment

K      BACKGROUND -> PROFFER(E) -> RULE(exclude E) -> EVIDENCE(E) -> judgment

I      BACKGROUND -> EVIDENCE(E) -> RULE(exclude E) -> judgment
```

The exclusion rule is byte-identical across U/K/I except for unavoidable block order.

Freeze note (FLAG-2, settled 2026-09-23): `RULE(exclude E)` is the G0 categorical
inadmissibility ruling with a per-item reason clause, stored without the `RULING`
header that the condition code prepends:

```text
RULING
The court has ruled that [evidence label] [reason]. It is inadmissible:
you must not let it play any role when you reach your verdict.
```

The four `exclusion_reason` bands in the materials are `procedural_illegality`,
`epistemic_invalidation`, `access_control` and `temporal_irrelevance`, 15 items
each.

No rule replay, reminder, chain-of-thought instruction, target identifier manipulation,
or mechanism intervention is part of G23B.

---

## 6. Phase-A carrier validity

For sign `s=+1` when E increases the merits judgment and `s=-1` when E decreases it:

```text
ProfferLeak = s · [Y(P) - Y(B)]

Leverage_U = s · [Y(E) - Y(B)]

Leverage_K = s · [Y(PE) - Y(P)]
```

### Item-level frozen exclusions

E1. all required cells for the executed phase are present and parseable.

E2. `Leverage_U > 0`.

E3. `Leverage_K > 0`.

No other item dropping, trimming, winsorisation, ratio normalisation, or post-hoc
carrier filtering is allowed.

**Gate ordering (FLAG-1, settled 2026-09-23):** gates 1–4 below are computed on
the **E1 set** — Phase-A rows after E1 only, *before* E2/E3 are applied. E2 and E3
then define the eligible set for the Phase-B branch estimands (rows entering
`Supp_*` and the two contrasts). Gates 3/4 are never evaluated after E3 has been
applied: the mean of strictly positive values would satisfy them by construction.

### Aggregate carrier gate

The K carrier is considered behaviorally neutral only if:

1. pooled `ProfferLeak` 95% CI upper bound is **< +3.0 rating points**; and
2. no model has mean `ProfferLeak >= +3.0` rating points; and
3. pooled mean `Leverage_K > 0`; and
4. `Leverage_K` is positive in at least 2/3 model means.

Bootstrap:
- cluster by independent skeleton;
- pooled analysis keeps all model outputs for the same skeleton in one resampled cluster;
- seed `20260923`;
- 10,000 percentile-bootstrap resamples.

If the carrier gate fails:

> **G23B stops before any U/K/I rule output is generated.**

Do not redesign the proffer after seeing a failed carrier audit inside the same frozen
round.

---

## 7. Primary estimands

For each target state, define how much adding the exclusion rule suppresses the
evidence-driven judgment relative to its matched no-rule condition:

```text
Supp_U = s · [Y(E)  - Y(U)]

Supp_K = s · [Y(PE) - Y(K)]

Supp_I = s · [Y(E)  - Y(I)]
```

Positive = the rule moves the judgment away from the evidence-driven answer.

The two branch contrasts are:

```text
SemanticRescue =
    Supp_K - Supp_U

InstantiationPremium =
    Supp_I - Supp_K
```

Sanity contrast:

```text
RetrospectiveAdvantage =
    Supp_I - Supp_U
    = SemanticRescue + InstantiationPremium
```

All estimands are raw sign-aligned rating points. No ratio.

The meaningful-effect floor is **3.0 rating points**, matching the existing raw-point
decision floor used in the reopened line.

---

## 8. Frozen branch logic

For any positive-effect gate `X`:

```text
PASS(X):
    pooled mean(X) >= 3.0
    AND pooled 95% CI lower bound > 0
    AND mean(X) > 0 in at least 2/3 models
```

For “no meaningful additional effect”:

```text
WITHIN_FLOOR(X):
    pooled 95% CI upper bound < +3.0
```

First sanity requirement:

> `PASS(RetrospectiveAdvantage)`

must hold. If not, the U-vs-I phenomenon does not cleanly replicate in the new
materials and the branch interpretation is not promoted.

Then classify:

### `instantiation-dependent`

```text
PASS(InstantiationPremium)
AND WITHIN_FLOOR(SemanticRescue)
```

Licensed interpretation:

> **Knowing exactly what the future evidence will say is not enough to recover
> retrospective exclusion; prior evidential instantiation adds a meaningful suppression
> advantage.**

This is the strongest behavioral support for the retrospective-cancellation /
evidence-state-revision account.

It still does not prove a specific internal cancellation circuit.

### `hybrid`

```text
PASS(SemanticRescue)
AND PASS(InstantiationPremium)
```

Licensed interpretation:

> **Semantic preactivation helps prospective exclusion, but prior evidential
> instantiation adds a further independent advantage.**

Both target availability and evidence-state existence matter.

### `semantic-preactivation`

```text
PASS(SemanticRescue)
AND WITHIN_FLOOR(InstantiationPremium)
```

Licensed interpretation:

> **Exact pre-rule semantic target information is sufficient to recover exclusion
> efficacy to within the preregistered meaningful margin of retrospective exclusion.**

Do **not** call this proof of a standing gate. A non-evidential proffer may still
preactivate evidence-like internal representations. The next experiment would be late
target resolution / control composition, not a cancellation mechanism sweep.

### `unresolved`

Any other pattern after a valid carrier and successful retrospective sanity check.

Examples:
- both contrasts are positive but one is imprecise;
- one mean is non-trivial but its interval crosses zero;
- neither equivalence-to-floor nor positive-effect criteria are met.

Do not force an H-GATE/H-CANCEL verdict.

### `carrier-invalid`

Phase-A carrier gate fails.

### `branch-not-replicated`

Carrier is valid, but `PASS(RetrospectiveAdvantage)` fails.

---

## 9. Model panel

Use the same three checkpoints as G23A:

- Qwen3-8B;
- Gemma-3-12B;
- Mistral-Small-24B.

Reasons:
- direct continuity with the established G23A discontinuity;
- two carry the earlier policy-access/enforcement dissociation;
- Qwen3-8B and Mistral-Small-24B connect to existing Stage-5 causal assets.

No model replacement after seeing Phase-A or Phase-B outputs.

A checkpoint that cannot load is reported by name. The analysis does not silently
substitute another model.

---

## 10. Why this design does not repeat G18

G18's semantic previews already affected the substantive judgment and nearly duplicated
the later evidence. Therefore G18 could not distinguish semantic target knowledge from
evidential instantiation.

G23B addresses that failure in three ways:

1. the K carrier has a real institutional non-evidential role;
2. its neutrality is a **prospectively frozen gate** measured before any exclusion-rule
   output exists;
3. K has its own matched no-rule condition `PE`, and items without positive later
   evidence leverage after the proffer are excluded by a frozen rule.

If K cannot satisfy those conditions, the correct result is `carrier-invalid`, not a
new story.

---

## 11. What G23B can and cannot establish

G23B can establish a behavioral dependence on target state at rule time.

It can support:

- exact semantic preactivation helps;
- evidential instantiation adds an extra suppression advantage;
- both matter;
- neither branch is identified.

It cannot by itself establish:

- a literal gate data structure;
- a literal cancellation vector;
- that the proffer produces no evidence-like hidden representation;
- a universal mechanism across all domains;
- a one-dimensional shared direction.

Mechanism comes only after the behavioral branch is resolved.

---

## 12. Conditional next step

If `instantiation-dependent`:
- reuse Stage-5 models;
- compare successful retrospective exclusion state with prospective failure;
- test whether successful exclusion introduces an opposing / cancelling
  target-conditioned state;
- causal transfer must selectively reduce evidence contribution while preserving
  evidence recall.

If `semantic-preactivation`:
- test early vs late semantic target resolution at a shared post-resolution checkpoint;
- verify late target understanding;
- ask whether reprocessing only the exclusion operator reconstructs the missing control
  state.

If `hybrid`:
- first factor semantic preactivation and evidential instantiation causally before
  claiming either as the sole mechanism.

If `carrier-invalid`, `branch-not-replicated`, or `unresolved`:
- stop and reassess; do not rescue the mainline with a mechanism sweep.

---

## 13. Authorization boundary

This document authorizes **design work only** until all of the following exist:

1. frozen fresh materials;
2. implemented Phase-A and Phase-B conditions;
3. frozen analyzer with the exact estimands / gates above;
4. tests covering cell order, carrier gate, exclusions, bootstrap clustering and branch
   classification;
5. a committed/tagged G23B design freeze;
6. an explicit repository-level compute authorization after that freeze.

Until then:

> **NO G23B TARGET-MODEL GENERATION.**

---

## 14. Freeze checklist and record

Three items were flagged in the pre-compute design audit and settled by decision on
2026-09-23, before any G23B output exists:

- **FLAG-1 — gate ordering (§6):** carrier gates 1–4 computed on the E1 set before
  E2/E3; E2/E3 define the Phase-B branch set.
- **FLAG-2 — rule family (§5):** `RULE(exclude E)` is the G0 categorical
  inadmissibility ruling with a per-item reason clause.
- **FLAG-3 — proffer wording (§4):** agreement-safe rendering adopted; every other
  template element unchanged.

Freeze checklist:

- [x] fresh materials — `data/items/g23b_v1.jsonl`: 60 items / 60 skeletons,
      30 increase / 30 decrease, disjoint from `items_v1` / `g18_v1` / `linear_v1` /
      `g23a_v1` asserted at build (id, surface, skeleton), no LLM-generated gold;
      sha256 `8cb4cfe4dacb0e5f4368c6d1e568083fd38f05b54ae03489d0208b4b7332cda8`
- [x] conditions — `src/conditions_g23b.py`; cell keys `g23b_b`, `g23b_p`, `g23b_e`,
      `g23b_pe`, `g23b_u`, `g23b_k`, `g23b_i` realize §5's B / B→P / B→E / B→P→E /
      B→R→E / B→P→R→E / B→E→R; registered in `src/schema.py`, dispatched by
      `src/run_model.py`; no probes
- [x] analyzer — `src/analyze_g23b.py --phase a|b`; raw inputs
      `results/raw/{model}_g23b_phasea.jsonl` / `..._phaseb.jsonl`; outputs
      `results/g23b_carrier_analysis.json` / `results/g23b_branch_analysis.json`;
      seed `20260923`, 10,000 percentile resamples, clusters = skeletons; verdict
      strings exactly the six of §8 in its decision order
- [x] tests — `tests/test_g23b.py` plus a full-suite run green at freeze: cell
      orders, no rule anywhere in Phase A, byte-identical rule across U/K/I,
      proffer payload identity, `RetrospectiveAdvantage = SemanticRescue +
      InstantiationPremium` row-level identity, all four carrier gates (including
      the gate-ordering pin), all six verdicts, seed determinism
- [x] worst-case prompt = 326 tokens (cell K) under the 2048-token context
- [x] this document amended (§4, §5, §6 ordering note) and committed/tagged
      `g23b-gate-vs-cancellation-design-v1` in the same commit, before any
      generation
- [ ] only then: Phase A generation (B / P / E / PE) under repository-level
      authority from `STATUS.md`
- [ ] Phase B (U / K / I) only if the Phase-A carrier gate passes; otherwise the
      round stops here per §6
