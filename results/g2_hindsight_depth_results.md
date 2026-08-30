# G2 hindsight-depth — results

**Design tag:** `g2-hindsight-depth-design-v1`; **transformation freeze:**
`g2-hindsight-depth-freeze-v1`. Six conditions × 3 frozen checkpoints × 256
units (9,216 generations) against artifact SHA-256 `0b6fd8d0…acf0901d`.
Analysis: `results/g2_hindsight_depth_analysis.json`.

## Qualification — one condition disqualified one model

Preregistered rule: parse rate ≥ `992/1024` and boundary-probe accuracy ≥
`448/512` **in each condition of that model**.

| model | failing condition | detail |
|---|---|---|
| Gemma-3-12B-it | none | all six conditions pass |
| Mistral-Small-24B | none | all six conditions pass (1.0000 everywhere) |
| Qwen3.5-9B | `evr_allowed` | probes 221/256 = **86.33%**, below the 87.5% floor |

Qwen answered `NO` on 35 licensed-frame probes after redaction, against
252/256 = 98.4% on the same probe with the unredacted packet. Removing the
verdict sentence made Qwen more likely to deny that the packet belongs to the
licensed information set at all. That is a real side-effect of the
manipulation and is reported as such.

Applied as written, this disqualifies Qwen for **both** experiments —
including Experiment A, whose own four conditions Qwen passes (probes
98.8–100%).

## Experiment A — positional replication: **the panel gate is not met**

`PE_exclude = mean s·(p[repeat-before] − p[repeat-after])`

| model | qualified | `PE_exclude` (95% CI) | `I_before` | `I_after` | replicates |
|---|---|---|---|---|---|
| Qwen3.5-9B | **no** (see above) | **7.16 [5.89, 8.54]** | 17.59 | 10.43 | not counted |
| Gemma-3-12B-it | yes | **5.75 [4.42, 7.20]** | 21.71 | 16.01 | **yes** |
| Mistral-Small-24B | yes | 0.90 [−0.19, 1.98] | 6.54 | 5.64 | no |

**`experiment_a_replicates: false` — 1 of 3, below the preregistered ≥2/3
bar.** That is the primary result and it stands.

Two things must be said alongside it, neither of which changes the verdict:

1. **The raw effects reproduce the 64-unit pattern in the same two models.**
   Qwen 5.31 → 7.16, Gemma 9.72 → 5.75, Mistral −0.70 → 0.90 (null then, null
   now). Reinstating the constraint *after* the future evidence again lowers
   intrusion relative to stating it before.
2. **Disclosed post-hoc sensitivity, not primary.** If qualification were
   assessed per experiment rather than across all six conditions, Qwen would
   qualify for A (it fails only a condition belonging to B) and A would read
   2/3 and pass. The preregistration says "in each condition", so the primary
   number is 1/3. Both readings are reported; the gate is not redefined after
   the fact.

### The specificity control does **not** support exclusion-specificity

`PE_allowed`: Gemma −0.01 [−0.03, 0.00], Qwen 0.00 [0.00, 0.00], Mistral
**4.23 [2.10, 6.59]**.

Qwen and Gemma sit at aligned `ALLOWED_WITH` ≈ 99.96 — their licensed cells are
pinned at ceiling, so their zero is a measurement artifact, exactly as
anticipated in amendment A1. Mistral is the only model with headroom (93.12),
and in Mistral position affects the **licensed** frame too, positively.

Therefore: **no claim is made that position selectively matters for exclusion.**
The permitted sentence is that the control is uninformative under ceiling for
two models and points the other way in the one model that can move.

## Experiment B — explicit verdict redaction: **gate met, direction unanticipated**

Leverage gate `R_red ≥ 15` passes in all three models (45.3–47.2), so the
redacted packets remain fully usable evidence.

| model | `R_red` | `HC_red` (95% CI) | `HC_direct` | `HC_direct − HC_red` |
|---|---|---|---|---|
| Qwen3.5-9B | 47.17 | **23.35 [20.99, 25.73]** | 16.02 | −7.33 [−8.88, −5.82] |
| Gemma-3-12B-it | 46.85 | **34.55 [31.96, 37.07]** | 27.73 | −6.91 [−8.68, −5.25] |
| Mistral-Small-24B | 45.27 | **10.18 [7.43, 13.00]** | 7.46 | −2.72 [−4.16, −1.25] |

On the pre-frozen 237-unit changed subset: 23.87 / 35.92 / 10.40 — every model
higher still, so the effect is not carried by the 19 no-op packets.

**`experiment_b_contamination_survives_redaction: true` (2/3 qualified models),
`experiment_b_survival_headline_permitted: true` (the changed subset agrees).**

Permitted claim, in the exact frozen wording:

> Hindsight contamination persists after explicit YES/NO resolution verdicts
> are removed — the effect is not reducible to copying an explicit resolution
> label.

**Unanticipated:** contamination is not merely preserved but *larger* without
the verdict, in all three models, by 2.7–7.3 points. The preregistered
interpretation table did not include this direction. Two honest readings, both
untested:

- the verdict sentence may act as a salient marker that the packet is a
  post-hoc resolution artifact, which the model then partly discounts; without
  it the same evidence reads as ordinary context;
- redaction shortens the packet (97.9% of characters retained), which slightly
  changes the distance between the evidence and the task. Given that
  Experiment A shows position matters, this is a genuine alternative
  explanation and cannot be ruled out with these runs.

No mechanism is claimed. Nothing here licenses "models are contaminated even
when the evidence does not reveal the answer" — surviving evidence still
entails the outcome, and this experiment does not test that.

## What is now writable, and what is not

- **Writable:** the recognition–enforcement gap and its 256-unit replication
  (unchanged, independent of G2); "contamination is not reducible to copying an
  explicit resolution label" (Experiment B, with the amplification direction
  reported as unanticipated).
- **Not writable:** "the position-sensitive mechanism independently
  replicates" — Experiment A did not clear its own panel gate, and the
  specificity control failed. The 64-unit positional finding stands as a
  discovery-sample result that reproduced in raw magnitude in 2/3 models and
  did not meet the preregistered replication bar.
