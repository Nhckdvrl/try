# G3 exclusion-reason factorization — results

**Design tag:** `g3-exclusion-reason-design-v1`; **transformation freeze:**
`g3-exclusion-reason-freeze-v1`. Six new conditions × 3 frozen checkpoints ×
256 units (6,912 generations) against artifact SHA-256 `0b6fd8d0…acf0901d`.
Analysis: `results/g3_exclusion_reason_analysis.json`. Transformation audit:
`results/btf3_exclusion_reason_audit.json` (PASS, 512/512 byte-identity).

## The question

Every earlier result confounds two claims carried by one sentence: that the
packet is not licensed, and that the reason is that it postdates the evaluation
point. This round replaces the **reason clause and nothing else**, in both
cells, and asks which kind of boundary a model can enforce at all.

## Execution

All twelve conditions of all three models qualified. Decision parse rates
99.61–100%, boundary-probe accuracy **97.27–100%** in every arm — recognition
stays at ceiling under every reason, so nothing below is explained by the model
ceasing to treat the packet as out of set.

## Results

`I_a` is `OutOfSetIntrusion` in arm `a`; `Δ = I_temporal − I_a`, paired per unit.

| model | `temporal` (baseline) | `bare` | `unreliable` | `procedural` |
|---|---|---|---|---|
| Qwen3.5-9B | 16.02 [14.18, 17.89] | 19.38 [17.26, 21.49] | 15.04 [13.04, 17.11] | 16.68 [14.78, 18.61] |
| Gemma-3-12B-it | 27.73 [25.15, 30.39] | 28.05 [25.40, 30.66] | **35.44 [32.99, 37.88]** | **35.79 [33.21, 38.37]** |
| Mistral-Small-24B | 7.46 [5.41, 9.57] | 8.34 [6.16, 10.59] | 6.34 [3.75, 8.94] | 7.14 [4.73, 9.56] |

| model | Δ vs `bare` | Δ vs `unreliable` | Δ vs `procedural` |
|---|---|---|---|
| Qwen3.5-9B | −3.36 [−4.57, −2.15] → no reduction | +0.97 [−0.29, +2.17] → no reduction | −0.66 [−1.70, +0.34] → no reduction |
| Gemma-3-12B-it | −0.38 [−1.60, +0.90] → no reduction | −7.81 [−9.91, −5.78] → indeterminate | −8.16 [−9.97, −6.45] → indeterminate |
| Mistral-Small-24B | −0.88 [−1.68, −0.08] → no reduction | +1.12 [−0.06, +2.40] → no reduction | +0.32 [−0.74, +1.45] → no reduction |

**Panel verdict, by the frozen rule: `no_reduction` for all three arms
(3/3, 2/3, 2/3). Interpretation row: H-inert.**

## Permitted claim, in the frozen wording

> No stated reason moves the effect. The packet's presence dominates every
> licensing rule tested here, including one that undercuts its truth.

This is the strongest form of the recognition–enforcement claim and it
generalises the result beyond time. Three separate things are now established
about the same 256 items:

1. **It is not about time.** A non-temporal licensing reason — the packet came
   through a channel the protocol does not permit, its contents being accurate
   — is enforced no better than the temporal one. The failure is not a
   difficulty with reconstructing a *past* state specifically.
2. **It is not about the model believing the evidence.** Telling the model the
   packet "was assembled by an unverified automated process, may contain
   fabricated claims" does not reduce its influence in any model, and
   substantially *increases* it in one. The discounting machinery that ordinary
   inference would use here is not reached by this instruction.
3. **It is not about the reason being unstated.** The `bare` arm, with the
   licensing asserted and no reason at all, behaves like the temporal arm in
   Gemma and Mistral. In Qwen it is 3.36 points *worse* than having a reason —
   the only sense in which stating a reason helps is that stating any reason is
   marginally better than stating none.

Under the frozen specification check, `bare` shows no reduction in any model, so
no caveat attaches to the other contrasts.

## Unanticipated, and reported as such

In Gemma-3-12B, both arms that add a clause about the packet — `unreliable` and
`procedural` — **raise** intrusion by about 8 points (35.4 and 35.8 against a
27.7 baseline). The frozen rule classifies these as indeterminate, not as
reductions, and no row of the interpretation table is claimed from them. Two
observations, neither tested here:

- It lines up with G2 Experiment B, where *removing* the verdict sentence also
  made contamination larger. In both cases a manipulation that changes how much
  the prompt talks about the packet moves the effect upward.
- A parsimonious reading is that additional text referring to the packet raises
  its salience, and salience is what drives the effect. That is a hypothesis
  about attention, not a result; it is exactly the kind of claim that requires
  the mechanism phase, and it is not asserted here.

## What this does not license

- No claim that the models *cannot* discount evidence they believe false in
  general. This experiment shows only that this prompt slot does not reach that
  machinery on this task. A dedicated falsity manipulation with its own utility
  check would be needed, and was not run.
- No claim about *why* Gemma amplifies. Two conditions cannot distinguish
  salience from length from wording.
- No mechanism claim of any kind.

## Disclosures, repeated from the preregistration

- The `unreliable` arm asserts that the packet may contain fabricated claims.
  That is false of our materials; it is a deliberate counterfactual framing
  manipulation.
- The `procedural` arm affirms the packet's accuracy, which the `temporal` arm
  does not. It therefore gives the model *more* reason to believe the packet,
  making it a conservative test of a non-temporal licensing reason — and it
  still shows no reduction.
- The arms differ in length (−7 / +8 / +15 tokens against temporal). The edited
  sentence precedes the packet, so the packet→`TASK` token span is identical in
  all four arms; the positional channel found in G2 Experiment A is closed by
  construction, and the audit verifies it per item.
