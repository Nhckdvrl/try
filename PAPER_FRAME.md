# Paper frame — target-state factorization

**Updated:** 2026-09-04 after the third mainline audit.
**Authoritative ledger:** [SCIENTIFIC_REGISTER_2026-09-04_V3.md](SCIENTIFIC_REGISTER_2026-09-04_V3.md)

The paper has one scientific identity:

> **Can a language model commit in advance to ignore evidence it has not yet seen?**

The current paper is **not** committed to a final mechanism label. The next job is to
separate three states that earlier experiments mixed together:

1. the future target is unresolved;
2. the future target is semantically known but not evidence;
3. the target proposition is already instantiated as evidence.

---

# 1. Entry phenomenon

Across 12 instruction-tuned models, two masked diffusion LMs, four vendors, and five
task families, the same exclusion rule is substantially weaker before the evidence than
after it. Matched Admit controls do not show the same order effect.

Headline:

> **Models are systematically worse at pre-committing to evidence exclusion than at
> excluding the same evidence after it appears.**

This remains Figure 1 and the paper's natural hook.

---

# 2. What the existing evidence rules out

The reversal is not adequately explained by:
- generic instruction position alone;
- simple rule forgetting;
- rule-to-evidence distance;
- one wording;
- causal decoder masking;
- inability to execute any future zero rule;
- lack of declarative policy access.

Important established boundaries:
- masked diffusion LMs preserve the asymmetry;
- Qwen/Gemma can state zero yet still use prospective evidence;
- explicit future arithmetic weighting can succeed exactly;
- arbitrary names / future identifiers / content-pending stubs do not reliably rescue.

---

# 3. G18 — strong result, narrower interpretation

G18 prospectively confirms a strong target-state effect:

`Delta_semantic = +8.91 [7.15,+10.76]`, positive in 5/5 models.

But the `para/entail` previews themselves assert almost the same proposition as the
later evidence. Their no-rule later-evidence marginal collapses from ~32 to ~3 points.

Therefore G18 supports:

> **Having the target proposition already represented before exclusion materially
> changes later suppression.**

It does not yet tell us whether:
- semantic knowledge alone is sufficient; or
- the proposition must already have entered the judgment as evidence.

That unresolved distinction is now the central scientific gap.

The ~−28 point below-baseline semantic suppression is retained as an anomaly that may
later distinguish passive gating from active revision/cancellation, but it is not a
scope-collapse claim.

---

# 4. Stage 4 and Stage 5 under the corrected frame

## Stage 4

Proposition-targeted policies can follow content across D7→D9 while identifier-only
protection does not universally follow.

Use as evidence that effective control can be content-conditioned.

Do not use it as proof of future semantic binding: the proposition is explicitly
embedded in the system policy.

## Stage 5

Qwen3-8B and Mistral-Small-24B show a target-dependent causal rule-time state before
later evidence integration.

This remains a strong mechanism asset.

Correct claim:

> **Target availability changes a causal state formed around exclusion processing.**

What that state implements remains open.

---

# 5. Stage 3B correction

Tagged routing remains empirically successful, but its old interpretation is no longer
licensed.

The existing no-policy control removes `[verified]/[unverified]` labels. Therefore the
experiment cannot distinguish:
- persistent standing-policy execution; from
- local semantic discounting caused by the incoming `[unverified]` label itself.

This matters because it prevents us from casually asserting:

> future gating works whenever the policy is class-based.

A small diagnostic may later deconfound this, but it is not the paper's main question.

---

# 6. Current root-cause fork

The next experiment must answer:

> **What must exist when exclusion is processed for future evidence to become causally
> inert?**

## H-A — deferred target binding / eager control compilation

Semantic target knowledge is sufficient, but the target must be available when
exclusion is processed. Late target resolution may be understood without reconstructing
the same control state.

## H-B — evidential instantiation / retrospective revision

Knowing exactly what future evidence will say is not enough. Strong exclusion requires
a matching evidence representation already present in the judgment state, suggesting
revision/cancellation rather than a future gate.

## H-C — local semantic control

Prospective control may succeed when the arriving evidence itself exposes a meaningful
control feature, but not when a novel policy→future-object relation must be carried
across time.

None is established.

---

# 7. G22 — the next novelty-bearing factorization candidate

**G22: Target Knowledge vs Evidential Instantiation**

Status:
- registered;
- design audit only;
- not preregistered;
- not frozen;
- no generation authorized.

Core target states:

```
UNRESOLVED:
EXCLUDE → future E(P)

KNOWN-BUT-NON-EVIDENTIAL:
non-evidential specification(P) → EXCLUDE → future E(P)

EVIDENTIALLY-INSTANTIATED:
asserted evidence(P) → EXCLUDE → future E(P)
```

The middle condition is the entire point.

Its carrier must:
- identify P exactly;
- not assert P as evidence;
- have near-zero effect on judgment without the later evidence.

If that separation cannot be achieved, G22 should not run.

---

# 8. Conditional scientific descent

## If semantic knowledge alone is sufficient

Then the paper can naturally continue:

```
G0 reversal
→ target knowledge is the missing operand
→ early vs late target-policy mapping
→ correct late mapping but failed causal composition
→ operator reprocessing / critical-window mechanism
```

Only then does the deferred-binding / eager-compilation story become central.

## If only evidential instantiation is sufficient

Then the stronger story becomes:

```
G0 reversal
→ knowing future evidence is not enough
→ exclusion works mainly after matching evidence state exists
→ passive gate vs active revision/cancellation
→ causal target-specific revision state
```

This would be a deeper distinction than “semantic target information helps.”

## If neither cleanly separates

Reassess. Do not pivot to G21, labels, or another nearby phenomenon merely because it
is interesting.

---

# 9. Main claims today

### Claim 1 — established

> **Models are systematically worse at pre-committing to evidence exclusion than at
> excluding the same evidence after it appears.**

### Claim 2 — open

> **What target state must exist for exclusion to become effective?**

G22 decides this.

### Claim 3 — established with heterogeneity

> **Explicit policy access can be insufficient for causal enforcement.**

### Claim 4 — established at two-model mechanism scope

> **Target availability changes a causal rule-time state that affects later evidence
> suppression.**

Do not yet name that state as binding, cancellation, or gating.

---

# 10. Natural method opening

The paper should ultimately motivate a method only after the behavioral law is known.

The broad engineering question is:

> **How should a system represent future evidence policies so they remain executable
> when the target does not yet exist?**

Possible future directions, depending on G22:
- persistent policy operator separated from target instance;
- explicit evolving policy state;
- delayed policy instantiation at evidence arrival;
- target-aware runtime / reference monitor;
- training objectives enforcing correct future policy application;
- causal-state reconstruction after late target resolution.

Do not revive ReGround as the main method.

---

# 11. What is not the paper

- semantic specificity as novelty;
- G21 source/proposition scope;
- generic label semantics;
- generic instruction order;
- generic binding;
- generic policy failure;
- ReGround;
- another model-size sweep.

The paper must remain one natural question becoming progressively more computational.
