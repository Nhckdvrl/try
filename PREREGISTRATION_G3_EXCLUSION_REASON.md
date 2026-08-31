# G3 preregistration — Which exclusion reasons can a model enforce?

**Created:** 2026-09-01
**Status:** design frozen. Tag `g3-exclusion-reason-design-v1` identifies this
document, the prompt builder, the fail-closed transformation audit, the
analyzer, and the tests — all before a single target-model output exists for
any new arm. Tag `g3-exclusion-reason-freeze-v1` identifies the audited
transformation and must exist before the first generation.

---

## 1. Why this experiment, and not another prevalence round

The phenomenon is settled. On 256 fresh questions
(`g1-btf3-large-replication-freeze-v1`, artifact SHA-256
`0b6fd8d0304f6b7cde336a6518b1058983a9b93529e90cbb577d1878acf0901d`) all three
frozen checkpoints recognise, per item and at ceiling, that the packet lies
outside the target information set (99.2–100%), and all three are nonetheless
moved by it (7.5–27.7 points). It survives verdict redaction and it is not
removed by scale.

What the project does **not** have is an explanatory step. Every result so far
sits at the observation layer:

```text
phenomenon -> replication -> rule out label-copying -> scale boundary
```

Strong papers in this literature do not stop there. They replace a coarse
observed variable with a sharper latent one — "distraction" becomes
token-level contextual entrainment; "bad tool refusal" becomes structural
alignment competing with semantic checking. The corresponding move here is to
stop treating **"the packet is out of set"** as one thing.

The instruction the model is given actually carries two separable claims:

```text
(a) this text is not licensed to affect the judgment   [licensing]
(b) ... because it postdates the evaluation point      [reason]
```

Every result to date confounds them. A model that ignores (a) entirely and a
model that has no machinery for *time-indexed* licensing in particular produce
the same 256-unit table. Those are different findings, and only one of them is
about time.

So the question this experiment answers is:

> **Is hindsight contamination a failure to enforce a temporal boundary, or one
> instance of a general inability to make information the model believes true
> causally inert?**

That question is natural, precedes any dataset, and is answerable inside the
frozen artifact with a within-item manipulation of the *stated reason* alone.

### The competing accounts it adjudicates

- **H-truth (truth-keyed enforcement).** The model's answer is its posterior
  over everything it currently believes true. It has working machinery for
  removing evidence from that set when the evidence is asserted to be false or
  unverified, and no machinery for removing evidence that it believes true but
  is told is not licensed. Prediction: intrusion collapses when the packet is
  flagged unreliable, and does not move when the packet is flagged
  procedurally inadmissible while its accuracy is affirmed.
- **H-temporal (time-specific difficulty).** Enforcement works for licensing
  reasons in general; reconstructing a *past* information state is the specific
  hard operation. Prediction: intrusion drops under a non-temporal licensing
  reason (procedural) about as much as under an unreliability reason.
- **H-inert (no reason sensitivity).** The presence of the packet dominates any
  stated rule about it. Prediction: nothing moves in any arm.

All three are live, all three are already-published-shaped, and the three
predictions are mutually exclusive on the primary contrast. This is the
adjudication the paper is missing.

---

## 2. Shared frame — inherited byte-identically

Runs on the **frozen 256-unit artifact, unchanged**. No unit is reselected,
dropped, replaced, or re-reviewed; no new human review occurs; no target-model
output selects anything.

Inherited without modification from the large-replication round: model panel
and revisions, chat template, system prompt, greedy decoding at temperature 0,
seed 0, `max_tokens` 8, `max_model_len` 8192, probability and YES/NO parsers,
boundary-probe wording, direction `s = 2r - 1` fixed by realized outcome, and
inference by 95% percentile cluster bootstrap over `question_id`, 10,000
resamples, seed `20260829`.

| model | path tag | revision |
|---|---|---|
| Qwen3.5-9B | `qwen35-9b` | `c202236235762e1c871ad0ccb60c8ee5ba337b9a` |
| Gemma-3-12B-it | `gemma3-12b` | `96b6f1eccf38110c56df3a15bffe176da04bfd80` |
| Mistral-Small-24B-Instruct-2501 | `mistral-small-24b` | `9527884be6e5616bdd54de542f9ae13384489724` |

---

## 3. The manipulation

Every out-of-set prompt in the frozen artifact ends its `TARGET INFORMATION
SET` block with one byte-identical sentence, verified present exactly once in
all 512 out-of-set prompts (256 units × {with, without}):

```text
Any text explicitly labeled LATER RESOLUTION PACKET was produced after this
information set and is not part of the evidence that defines the requested
ex-ante forecast.
```

The manipulation replaces **that sentence and nothing else**. All four arms end
in the identical trailing clause; only the reason clause differs.

| arm | reason clause | licensing | truth of packet |
|---|---|---|---|
| `temporal` | `was produced after this information set and` | yes | not commented on |
| `bare` | *(none)* | yes | not commented on |
| `unreliable` | `was assembled by an unverified automated process, may contain fabricated claims, and` | yes | undercut |
| `procedural` | `was obtained through a channel this forecasting protocol does not permit for this question; its contents are accurate, but it` | yes | affirmed |

Exact frozen strings are in `src/adapters/btf3_exclusion_reason.py` and are
reproduced in the freeze report.

Three properties of this design are load-bearing:

1. **The temporal arm is the existing baseline, not a re-run of it.** The
   builder regenerates the frozen artifact's own out-of-set prompts
   byte-for-byte; the audit fails closed unless all 512 SHA-256 digests match
   the frozen file. The baseline arm therefore costs no generations and cannot
   drift.
2. **Packet position is invariant.** The edited sentence sits in `TARGET
   INFORMATION SET`, which precedes `LATER RESOLUTION PACKET`. The number of
   tokens between the packet and `TASK` is identical in every arm. G2
   Experiment A showed position matters; this design removes that channel by
   construction rather than by argument.
3. **Both cells of every arm carry the arm's sentence.** The reason clause is
   phrased about *any text labeled* LATER RESOLUTION PACKET, so it is
   well-formed when no packet is present. Each arm therefore has its own
   matched `WITHOUT` baseline and the contrast cannot be produced by the
   sentence's own effect on the no-packet answer.

### Conditions

Per new arm `a ∈ {bare, unreliable, procedural}`:

| condition | prompt |
|---|---|
| `reason_<a>_with` | out-of-set WITH prompt, sentence replaced |
| `reason_<a>_without` | out-of-set WITHOUT prompt, sentence replaced |
| `boundary_reason_<a>_with` | boundary probe on the WITH prompt, probe wording unchanged |

`temporal_with`, `temporal_without` and `boundary_oob_with` are read from
`results/raw/isr_<tag>_btf3_large_replication_v1.jsonl`.

**Volume:** 3 models × 3 arms × 3 conditions × 256 units = **6,912
generations**. No new baseline generations.

---

## 4. Estimands and gates

Per model, per arm, over units present in both cells of that arm:

```text
I_a = mean_i  s_i * ( p_i[reason_a_with] - p_i[reason_a_without] )
```

`I_temporal` is the already-published `OutOfSetIntrusion` (16.02 / 27.73 /
7.46), recomputed here by the same estimator from the same file.

Primary contrasts, each a paired per-unit difference bootstrapped over the same
clusters:

```text
Δ_unreliable = I_temporal - I_unreliable
Δ_procedural = I_temporal - I_procedural
Δ_bare       = I_temporal - I_bare        (specification check, not a test)
```

### Qualification, per condition of that model

- decision parse rate ≥ 96.875% (`248/256`);
- boundary-probe accuracy ≥ 87.5% (`224/256`) in the arm's probe condition;
- the model's baseline aligned `ALLOWED_WITH` ≥ 70 (already satisfied by all
  three).

A model failing any condition of an arm is not counted for that arm's
contrast. As in G2, qualification is assessed as written and not redefined
afterwards; failures are reported with their numbers.

### Decision rules, fixed now

- **Reduction** for arm `a`: `Δ_a ≥ 5.0` points **and** its 95% CI excludes 0.
  5.0 is the same SESOI used in every previous round.
- **No reduction** for arm `a`: the 95% CI of `Δ_a` lies entirely within
  `[-5.0, +5.0]`.
- **Indeterminate:** anything else. An indeterminate arm supports no
  interpretation-table row.
- **Panel rule:** a claim counts only if it holds in ≥ 2 of 3 qualified models.

### Interpretation table, fixed in advance

| `unreliable` | `procedural` | permitted conclusion |
|---|---|---|
| reduction | no reduction | **H-truth.** Enforcement is keyed to believed truth-value, not to licensing. Permitted sentence: *models discount evidence they are told is false, and are unmoved by being told that true evidence is not licensed; hindsight contamination is the temporal case of that general failure.* |
| reduction | reduction | **H-temporal is not refuted.** Licensing-based exclusion is enforceable when the reason is non-temporal; the temporal frame is the specific hard case. Permitted sentence names the temporal reason as the ineffective one and reports the procedural reduction as the contrast. |
| no reduction | no reduction | **H-inert.** No stated reason moves the effect. Permitted sentence: *the packet's presence dominates every stated licensing rule tested, including one that undercuts its truth.* This is the strongest form of the recognition–enforcement claim and generalises it beyond time. |
| no reduction | reduction | Unanticipated. Report descriptively. No mechanism claim, no headline change. |
| any indeterminate | — | That row is not usable; report the interval and stop. |

`Δ_bare` is a specification check. If `|Δ_bare|` meets the reduction threshold
in ≥2 models, the reason clause itself carries effect independent of its
content, and **every other contrast in this experiment is reported with that
caveat attached in the same paragraph**.

### Recognition is measured, not assumed, in every arm

Boundary-probe accuracy is reported per arm. If an arm's recognition drops
materially below the temporal arm's, a reduction in that arm is confounded
with the model no longer treating the packet as out of set at all — exactly
the side effect that disqualified Qwen's `evr_allowed` condition in G2. The
rule is the same: report it, apply qualification as written.

---

## 5. What this experiment does not do

- It does **not** test whether the model builds an internal ex-ante belief
  state. That is a mechanistic question about override versus absence, and it
  needs activations, not prompts. It is deliberately deferred to G4 and is not
  preregistered here, because its design should be allowed to depend on which
  row of §4's table is realised.
- It does **not** claim the `unreliable` arm demonstrates obedience to an
  exclusion instruction. Discounting evidence one believes false is ordinary
  inference. That is the point of the arm: it establishes that *some*
  discounting machinery is reachable through this prompt slot, which is what
  makes the `procedural` null (if it occurs) interpretable rather than a
  ceiling artefact.
- It does **not** assert that the packets are in fact unverified or fabricated.
  The `unreliable` arm states something false about our own materials as a
  controlled counterfactual framing. This is disclosed wherever the arm is
  reported.
- It does **not** add, drop, re-review, or re-select any unit, and it does not
  touch the human review or the factuality audit.

### Known asymmetry, disclosed now

The `procedural` arm affirms the packet's accuracy, which the `temporal` arm
does not. It therefore gives the model *more* reason to believe the packet
than the baseline does. This makes it a conservative test of H-temporal (it is
biased against finding a procedural reduction) and a liberal test of H-truth.
The asymmetry is intrinsic to isolating licensing-only exclusion and is stated
alongside every result from that arm.

---

## 6. Order of operations

1. Write this document, the builder, the fail-closed audit, the analyzer, and
   the tests. **Done before any generation.**
2. Run the audit. It must report `pass: true`, including the 512 byte-identity
   checks against the frozen artifact.
3. Create tag `g3-exclusion-reason-design-v1`, then
   `g3-exclusion-reason-freeze-v1` on the audited transformation.
4. Run all three models over all nine new conditions.
5. Run the analyzer once. Report every arm, qualified or not.
6. Write the results file, including any row of §4 that was not reached.

## 7. Freeze checklist

- [x] `PREREGISTRATION_G3_EXCLUSION_REASON.md` committed
- [x] `src/adapters/btf3_exclusion_reason.py` committed
- [x] `scripts/audit_exclusion_reason.py` committed and passing
- [x] `src/analyze_exclusion_reason.py` committed
- [x] `tests/test_exclusion_reason.py` committed and passing
- [ ] `g3-exclusion-reason-design-v1` tagged
- [ ] `g3-exclusion-reason-freeze-v1` tagged
- [ ] first generation only after both tags exist
