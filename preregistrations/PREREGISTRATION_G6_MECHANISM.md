# G6 preregistration — Where does the packet enter, and is there a judgment to protect?

**Created:** 2026-09-01
**Status:** design frozen. Tag `g6-mechanism-design-v1`, before any activation
is captured or any masked generation is produced.

---

## 1. Why mechanism is allowed here at all

`PAPER_FRAME.md` §8 permits opening a model only when two accounts make the
same behavioral prediction and differ only internally. After G3 that condition
is met, and it is met sharply.

G3 established `H-inert`: no stated reason reduces the effect. Not the temporal
reason, not a non-temporal licensing reason with the packet's accuracy
affirmed, not one that undercuts the packet's truth — while per-item
recognition stays at 97–100% in every arm. Two accounts survive that, they
predict the same outputs, and nothing measurable at the output can separate
them:

- **H-override.** An ex-ante judgment *is* computed — the model does build an
  estimate from the licensed evidence — and the packet's contribution
  overwrites it later in the network.
- **H-absent.** No ex-ante judgment is ever computed. From early on there is a
  single estimate, formed with the packet already in it, and the recognition
  computation runs beside it rather than upstream of it.

This is the pair that mechanism is for. G5 addresses it behaviorally by forcing
the state construction in the prompt; this experiment addresses it internally,
and its design does **not** depend on how G5 comes out.

## 2. The decisive test is causal, not a probe

The obvious move — train a probe to decode the uncontaminated answer from the
contaminated run's activations — is deliberately **not** the primary test.
Decodability shows information is *available*, not that an ex-ante estimate is
computed and then overridden; a probe can reconstruct a counterfactual from
question content alone. That limit is stated here rather than discovered by a
reviewer, and the probe is demoted to a secondary, descriptive quantity (§5).

The primary test uses masking, which is causal by construction.

**The logic.** Let the model run normally on the out-of-set WITH prompt, except
that in a chosen window of layers the answer positions are forbidden from
attending to the packet's tokens. Suppose masking **only the last quarter of
the layers** restores the answer toward the no-packet value. Then through
three quarters of the network the computation had not yet committed to the
packet: an uncontaminated trajectory existed and was overwritten late. That is
`H-override`. Suppose instead that restoration requires masking from the
earliest layers, and late-only masking does nothing. Then the packet is in the
estimate from the start and there was never a separate ex-ante trajectory to
protect. That is `H-absent`.

The two accounts therefore make **opposite predictions about the same sweep**,
and the sweep is a single quantity per window.

## 3. The instrument

`src/mech/span_mask.py`, already committed. For each frozen prompt it maps the
packet's character span to token indices under the model's own chat template,
cross-checked against the untouched tokenizer path used by every previous
round; builds an additive causal mask that forbids query positions from the
`TASK` header onward from attending to those packet columns; and applies it
either to all layers or, through forward pre-hooks, to a layer window only.
Outside the window each layer keeps the mask the model built for it, so a
window result is never confounded with a different masking implementation.

**Masking, not deletion — and this is the point, not a convenience.** Deleting
the packet changes the prompt, so the model can no longer be asked about it.
Masking leaves the text in context: the boundary probe still runs, unmasked,
on the same prompt. That is exactly the contract this project measures —
`memory(E)` retained, `causal_effect(E → decision)` removed — and it is why the
method in §6 is stated as masking.

Decoding is greedy at temperature 0 with the frozen strict numeric readout.
Models run in `bfloat16` with an attention implementation that accepts an
additive 4D mask; the implementation used is recorded per run.

## 4. Experiment A — layer-window sweep (primary)

Windows are **suffix windows**: `[⌊fL⌋, L)` for
`f ∈ {0, 1/8, 1/4, 3/8, 1/2, 5/8, 3/4, 7/8}`, where `L` is the number of
decoder layers. `f = 0` is the full-depth mask. Suffix windows are used rather
than disjoint bands because the question is *how late can the intervention be
and still work*, which is exactly what a suffix answers.

Per unit and window, with `p_with` and `p_without` the frozen large-replication
values for that unit and model:

```text
restored_i(f) = ( p_i[mask(f)] - p_i[oob_with] ) / ( p_i[oob_without] - p_i[oob_with] )
R(f)          = mean over units with | p_without - p_with | >= 5   of  restored_i(f)
```

The 5-point leverage filter is fixed now and is defined entirely by the two
frozen baseline cells; no masked output participates in selecting it. Units
failing it are counted and reported. `R(f) = 1` means the mask fully restored
the no-packet answer; `R(f) = 0` means it changed nothing.

Intervals: 95% percentile cluster bootstrap over `question_id`, 10,000
resamples, seed `20260829`.

### Decision rule, fixed now

Let `f* = max{ f : R(f) ≥ 0.5 with its 95% CI excluding 0.5 from below }` —
the latest window that still restores at least half the effect.

| `f*` | permitted conclusion |
|---|---|
| `f* ≥ 1/2` | **H-override.** Masking confined to the second half of the network restores at least half the judgment; through the first half the computation had not committed to the packet. |
| `f* ≤ 1/8` and `R(1/2) < 0.25` | **H-absent.** Only near-full-depth masking works; the packet is in the estimate from the start. |
| anything else | Intermediate. Report the curve; name no account. |

Panel rule: ≥ 2 of 3 models. Models: `qwen35-9b`, `gemma3-12b`,
`mistral-small-24b` — the frozen panel, unchanged.

### Sanity conditions, run in the same sweep

- `R(0)` under full-depth masking must be close to 1. If full-depth masking
  does **not** restore the no-packet answer, the instrument is not doing what
  it claims and no row of the table above is usable. This is checked first.
- The unmasked run must reproduce the frozen `p_with` values. Any unit where
  the HF path and the vLLM path disagree by more than 1 point is reported and
  the disagreement rate is stated; the analysis uses the HF unmasked run as its
  own `p_with` so a framework difference cannot masquerade as an effect.

## 5. Experiment B — logit-lens trajectory and the availability probe (secondary)

Both are descriptive and neither can carry a conclusion on its own.

**B1, trajectory.** At each layer, the logit-lens readout at the final prompt
position, restricted to the ten single-digit tokens. Reported as the layer at
which the WITH answer's leading digit overtakes the WITHOUT answer's, on units
where those digits differ.

**B2, availability probe.** Ridge regression from the layer-`ℓ` residual at the
final position of the **WITH** run to the model's own **WITHOUT** answer,
5-fold cross-validated over units, with a 1,000-draw unit-permutation null, and
with `p_with` regressed out first. Reported as *availability*, never as use:
**a positive result licenses only the sentence "the uncontaminated answer is
linearly recoverable from the contaminated run's activations", and explicitly
not "the model computes it".**

## 6. Experiment C — enforcement by span masking (the method)

Full-depth masking of the packet span for answer positions, evaluated as a
deployable inference-time enforcement mechanism rather than as an analysis.

| quantity | what it must show |
|---|---|
| `I_mask` | out-of-set intrusion under the method, computed exactly as every other round |
| `R_mask` (licensed frame, unmasked) | licensed responsiveness is untouched — the method is applied only to spans the policy declares out of set |
| boundary probe, unmasked | recognition still ≈ ceiling: the text is still there and still readable |
| `wrong-span` control | masking a background span of the **same token length**, chosen by a frozen rule (the span immediately preceding the packet header), must **not** reduce intrusion |
| `delete` reference | the frozen `oob_without` answer — the ceiling any masking method can reach |

The `wrong-span` control is what makes this enforcement rather than damage. If
masking an arbitrary equal-length span reduces intrusion as much as masking the
packet, the method is degrading the model, not enforcing a boundary.

**Honesty requirement, fixed now.** Masking the packet is close to deleting it,
and the `delete` reference is in the table precisely so that the comparison is
visible. The contribution claimed is **not** "we can remove the effect by
removing the evidence" — that is trivial. It is that the removal can be made
*selective and reversible at inference time while the evidence remains in
context and answerable*, which prompting demonstrably cannot achieve: G3 showed
that no stated reason, including one that undercuts the packet's truth, reduces
the effect at all. The method's value is measured against that prompting
baseline and against G5's scaffold, not against deletion.

## 7. Volume

- Experiment A: 8 windows × 256 units × 3 models = **6,144** masked generations,
  plus 256 × 3 unmasked HF reference runs.
- Experiment B: 2 conditions × 256 units × 3 models activation captures.
- Experiment C: 3 conditions (`mask`, `wrong-span`, licensed unmasked) × 256 ×
  3 = **2,304**, of which the full-depth mask is reused from Experiment A's
  `f = 0`.

## 8. What this does not do

- No head-level attribution, no differentiable masking, no circuit discovery.
  None of those separates `H-override` from `H-absent`, which is the only pair
  that licenses opening the model at all.
- No claim that the masked span is "the" locus of anything. A suffix sweep
  localizes *when*, not *where*.
- No claim about models outside the frozen three.

## 9. Freeze checklist

- [x] `PREREGISTRATION_G6_MECHANISM.md` committed
- [x] `src/mech/span_mask.py` committed
- [x] `src/mech/run_span_sweep.py` committed
- [x] `src/mech/analyze_span_sweep.py` committed
- [x] `tests/test_span_mask.py` committed and passing
- [ ] `g6-mechanism-design-v1` tagged
- [ ] first masked generation only after the tag exists
