# Project status — scientific register v3

**As of:** 2026-09-04.
**Target:** NAACL / ACL / EMNLP Main-level paper.
**Authoritative scientific ledger:** [SCIENTIFIC_REGISTER_2026-09-04_V3.md](SCIENTIFIC_REGISTER_2026-09-04_V3.md)  
**Latest mainline audit:** [MAINLINE_AUDIT_2026-09-05_V4.md](MAINLINE_AUDIT_2026-09-05_V4.md)

The project is in a **mainline factorization audit**, not an experiment-running phase.

The paper identity remains:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

The current task is to explain the original G0 prospective/retrospective reversal
without drifting into a different paper.

---

## 1. Established empirical core

### G0 — prospective exclusion reversal

- 144 frozen items;
- five task families;
- 12 instruction-tuned models / four vendors;
- two masked diffusion LMs;
- same exclusion rule before vs after evidence;
- timing-gap direction same in 12/12 instruct models;
- 10/12 intervals exclude zero;
- matched Admit order effect is absent.

Established headline:

> **Models are systematically worse at pre-committing to evidence exclusion than at
> excluding the same evidence after it appears.**

### Policy access vs enforcement

Separate policy probes recover the intended zero weight at or near ceiling.

Qwen3-8B / Gemma-3-12B can explicitly state zero on-policy while prospective evidence
still affects judgment. Phi-4-mini does not show the same strong dissociation.

Established:

> **Explicit policy access is not sufficient for causal enforcement in at least some
> models.**

### Explicit arithmetic boundary

On the verifiable linear task, four of five models execute prospective `w=0` exactly
on qualified items; Qwen3.5-27B tracks all tested weights exactly.

Established:

> **The failure is not a generic inability to obey future numeric rules.**

### Object-existence ladder

Identifier/name/content-pending/type/direction before the rule do not reliably rescue;
full target content before the rule does.

Established:

> **A future referent or coarse description is not sufficient for strong prospective
> exclusion.**

### G18 — confirmed result, downgraded interpretation

G18:
- 100 fresh items;
- 30 independent skeletons;
- three families;
- five models / four vendors;
- 9,000 generations.

Frozen primary:
`Delta_semantic = +8.91 [7.15,+10.76]`, 5/5 positive.

However, `para/entail` previews themselves substantively assert the target proposition.
Their no-rule later-evidence marginal collapses from ~32 to ~3 points.

Therefore G18 currently establishes:

> **Having the target proposition already represented before exclusion strongly changes
> later suppression.**

It does **not** establish that merely knowing what a future target will mean is enough.

### Stage 4 — content-conditioned target

Proposition-targeted policies can follow content across D7→D9 while identifier-only
protection does not universally follow.

Use only as evidence that effective control can be content-conditioned.

### Stage 5 — causal rule-time state

A target-dependent mid-network rule state causally changes later suppression:
- Qwen3-8B L14–18 / 36;
- Mistral-Small-24B L12–16 / 40.

Established:

> **Target availability changes a causal state formed around exclusion processing.**

No universal steering vector was found.

---

## 2. Important downgraded conclusions

### “Target Addressability Governs Prospective Exclusion”

**Retired as paper novelty.**

Reason:
semantic specificity helping is too obvious/occupied, and G18 semantic previews also
instantiate substantive evidence content.

### G21 Source–Proposition Scope Entanglement

**Downgraded before generation.**

Interesting future question, but it does not explain G0.

### G20 v3 as the authorized next experiment

**Downgraded back to hypothesis/design status.**

Its P/U swap still mixes target knowledge, evidential instantiation, and
target-to-evidence distance.

### G18 oversuppression ⇒ scope collapse

**Not licensed.**

The semantic preview itself is evidence-like.

### Tagged routing proves standing prospective policy execution

**Not identified.**

Stage 3B lacks a semantic-labels-present/no-policy cell. Its successful routing may
partly or wholly reflect local semantics of `[unverified]`.

### ReGround G19

Cancelled before freeze/generation. Do not run.

---

## 3. Current root-cause fork

The active question is:

> **What must exist when an exclusion policy is processed for future evidence to become
> causally inert later?**

Three live accounts:

### H-A — deferred target binding / eager control compilation

Target semantics may need to exist when exclusion is processed. Late target resolution
may be understood without reconstructing the same control state.

### H-B — evidential instantiation / retrospective revision

Knowing future content may be insufficient. Exclusion may become effective only after a
matching evidential representation has already entered the model's judgment state.

### H-C — local semantic control vs standing relational control

Prospective control may work when incoming evidence carries a locally meaningful
control feature, but fail when the model must preserve a novel policy→future-object
relation.

None of these is currently established.

---

## 4. Registered next experiment

### G22 — Target Knowledge vs Evidential Instantiation

**Status: BRANCHING DISCRIMINATOR / DESIGN-AUDIT CANDIDATE ONLY.**
**No generation authorized.**

G22 is not assumed to carry novelty in every outcome. If clean non-evidential target
knowledge K already rescues exclusion, G22 is a bridge and the novelty-bearing question
moves to late policy-target composition. If K is fully understood and neutral but only
an already-instantiated evidential state rescues, G22 itself can support the stronger
retrospective-revision account.

Core factor:

1. unresolved future target;
2. future target semantically **known but explicitly non-evidential**;
3. same proposition **already evidentially instantiated** before the rule.

The known-but-non-evidential carrier must pass a preregistered judgment-neutrality gate.

Interpretation branch:

- if semantic knowledge alone rescues → only then test mapping-before vs mapping-after
  and deferred composition;
- if only evidential instantiation rescues → test retrospective state
  revision/cancellation;
- if neither rescues → reassess rather than pivot to another adjacent phenomenon.

See:
[SCIENTIFIC_REGISTER_2026-09-04_V3.md](SCIENTIFIC_REGISTER_2026-09-04_V3.md)

Dedicated design registration:
[G22_DESIGN_AUDIT.md](G22_DESIGN_AUDIT.md)

---

## 5. Registered supporting diagnostic

### D22-A — Tagged routing deconfound

Supporting only, not headline novelty.

Need:
- semantic labels + no policy;
- semantic labels + matching policy;
- semantic labels + reversed policy;
- nonce labels + standing policy;
- optional nonce labels + definitions.

Purpose:
determine whether Stage 3B reflects standing-policy execution or local label semantics.

---

## 6. Mechanism authorization

No new mechanism run yet.

Mechanism depends on G22 branch:

- H-A → post-resolution checkpoint / backpatch / frozen-backpatch / buffer vs
  operator-reprocessing;
- H-B → passive gate vs active cancellation/revision;
- H-C → local semantic circuit-selection test.

Existing Stage 5 remains an asset, not a complete explanation.

---

## 7. Current paper-claim status

| claim | status |
|---|---|
| prospective exclusion is harder than retrospective exclusion | **established** |
| policy access can dissociate from enforcement | **established, heterogeneous** |
| explicit future arithmetic control can work | **established boundary** |
| semantic target information alone is sufficient | **not established** |
| exclusion is non-commutative / deferred binding fails | **live hypothesis** |
| exclusion is retrospective evidence-state revision | **live hypothesis** |
| semantic local cues explain successful routing | **live hypothesis** |
| source/proposition scope collapse | **downgraded** |
| target-dependent causal rule-time state exists | **established, 2 architectures** |

---

## 8. Current authorization

Allowed:
- literature search;
- design audit;
- non-outcome-exposing material drafting;
- dummy/synthetic analyzer tests;
- repository cleanup.

Not allowed:
- G20 generation;
- G21 generation;
- G22 generation;
- D22-A generation;
- ReGround;
- new mechanism runs.

Before generation:
design → competing predictions → baselines → gates → preregistration → analyzer/tests →
commit/tag → generation.
