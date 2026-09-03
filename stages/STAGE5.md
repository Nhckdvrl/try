# Stage 5 — same-chronology bidirectional patching

The earlier Post→Pre patch had donor and recipient in different token orders, so
a layer effect could have been ordinary sequence-order information. Stage 3E
supplies a matched pair in which the evidence the decision reads sits **after the
rule on both sides**, and only the preview differs:

```
FAILURE   unrelated preview   → rule (weight 0%) → evidence → answer
SUCCESS   paraphrase preview  → rule (weight 0%) → evidence → answer
```

The unrelated preview is padded to the paraphrase's token length per item, so the
two runs match to within a few tokens (e.g. 382 vs 383). Qwen3-8B, 45 items from
`legal_judgment` + `evidence_inference`, restricted to the 29 with a behavioural
gap of at least 2 rating points.

* behavioural gap, failure − success: **+13.2 [+8.6, +18.1]** rating points
* 2×2 interaction `(ME−MA) − (UE−UA)`, sign-aligned: **−18.3 [−23.7, −12.9]**

The interaction is the quantity of interest: a preview alone changes the answer,
so what matters is that the matched preview enlarges the *exclude-minus-admit*
difference, not that it lowers the rating.

## Correction: the first version of this section overstated the effect

The numbers first reported here (54% rescue, 92% break) were medians of a
*recovery fraction*, `(patched − own) / (donor − own)`. For a substantial share of
items that denominator is only a few points, so the ratio explodes and its median
swings with the item subset. This is the same instability that forced Stage 3E off
REI and onto raw rating points; it was not applied to the mechanism analysis at
the time. Pooling all 70 items now available and reporting the shift in **rating
points**, with the fraction alongside on items whose gap is at least 5 points:

### Rule-span transfer, whole span, one layer at a time

| layer | SUCCESS → FAILURE (rescue) | FAILURE → SUCCESS (break) | ADMIT arm, matched → unrelated |
|---:|---|---|---|
| 12 | −0.4 [−2.1, +1.4] | +0.8 [−3.7, +4.9] | −0.8 [−1.5, −0.1] |
| 14 | **−3.6 [−5.9, −1.4]** | **+13.3 [+8.1, +18.9]** | −0.6 [−1.3, +0.1] |
| 16 | **−3.3 [−5.6, −1.2]** | **+11.5 [+6.3, +17.1]** | **+2.5 [+1.9, +3.1]** |
| 18 | **−3.9 [−6.1, −2.0]** | **+8.2 [+4.0, +12.9]** | **+1.9 [+1.4, +2.4]** |
| 20 | −1.6 [−2.7, −0.6] | +2.4 [+0.3, +5.0] | +1.3 [+1.1, +1.6] |

n = 44 / 24 / 25. Sign-aligned points; negative means moved toward suppression.
Median gap fractions: rescue 0.09–0.21, break 0.54–0.85.

What survives and what does not:

* **The localisation survives.** Layers 14–18 at the rule span, nothing at 12 or
  22, in both directions, before the evidence has been read.
* **Breaking survives at full strength.** Transplanting the failing run's rule
  state into the succeeding one adds +13.3 points of leakage at layer 14 — about
  85% of the behavioural gap. The earlier 92% was close to right for this
  direction.
* **Rescue does not.** The honest figure is −3.6 points, roughly **15%** of the
  gap, not 54%. Installing a working suppression state is much harder than
  destroying one.
* **It is not purely proposition information.** The same transfer run inside the
  Admit arm moves the answer +2.5 points at layer 16 — the *opposite* sign to the
  −3.3 it produces in the Exclude arm. So the state is not simply "the preview's
  content"; but both effects are small, so this is modest evidence of
  exclusion-specificity rather than strong evidence.

### A shared steering direction does not transfer

`v_l = mean over training items of [(h_ME − h_MA) − (h_UE − h_UA)]`, estimated on
35 items and applied to 35 disjoint held-out items at the rule span, at α from
0.05 to 0.4 of the layer's mean activation magnitude. Adding it to the failing run
should have increased suppression and subtracting it from the succeeding run
should have reduced it. **Neither happened.** Both manipulations increase leakage
at almost every layer (e.g. layer 6, α = 0.4: UE +8.1 points; layer 14: ME +7.7),
which is what generic perturbation damage looks like, not a control knob.

So the causal state found by patching is, on this evidence, **item-specific**. A
single reusable direction for it was looked for and not found.

## What this licenses, and what it does not

Licensed: by the time the exclusion rule has been read, the model has formed a
state, distributed over the rule tokens and living in layers 14–18, whose content
depends on whether a proposition matching the rule's target was available. That
state is causally sufficient to *destroy* later suppression (85% of the gap) and
causally contributes to *creating* it (15%), and it behaves differently in the
Admit arm, so it is not simply the preview's content.

Not licensed: any claim about what that state *represents*, and no claim that it
is a reusable feature — the held-out steering test above failed. Patching shows
the state carries the difference for that item; it does not show it is an
"exclusion tag bound to a proposition" rather than a general readiness state that
happens to covary, and the direction does not generalise across items.

### Replication on other models

The fixed-position readout the patching requires must first reproduce the
behavioural contrast, and it does not do so everywhere:

| model | behavioural gap, failure − success | 2×2 interaction |
|---|---|---|
| Qwen3-8B | +13.2 [+8.6, +18.1] | −18.3 [−23.7, −12.9] |
| Mistral-Small-24B | +18.5 [+9.3, +28.2] | −19.6 [−29.0, −10.9] |
| Phi-4-mini | +4.8 [−0.1, +10.0] | −2.7 [−7.2, +1.7] |
| Gemma-3-12B | −2.1 [−7.6, +3.5] | −4.3 [−9.0, +0.7] |

Gemma-3-12B and Phi-4-mini show the effect under the *reasoned* readout
(Stage 3E: Gemma's matched-preview ExclusionEffect is +14.1 against +8.7 for an
unrelated preview) but not under the fixed-position readout, so patching them
would have nothing to localise. That is a readout limitation, not evidence that
they lack the mechanism. Mistral-Small-24B does show it, and is the replication target.

### Mistral-Small-24B replicates the localisation, and rescues where Qwen does not

40 layers, 45 items, 36 with a gap ≥ 2 points. Behavioural gap +18.2
[+10.0, +26.9]; interaction −20.0 [−28.4, −11.6] — both close to Qwen3-8B's.
Rule-span transfer in sign-aligned rating points:

| layer | relative depth | SUCCESS → FAILURE | FAILURE → SUCCESS |
|---:|---:|---|---|
| 8 | 0.20 | +1.1 [−1.6, +4.8] | +12.5 [+8.3, +16.8] |
| 10 | 0.25 | −1.7 [−5.2, +2.4] | +15.8 [+11.1, +21.1] |
| 12 | 0.30 | **−8.1 [−14.9, −2.6]** | **+18.3 [+12.6, +24.5]** |
| 14 | 0.35 | **−16.1 [−24.2, −9.0]** | **+17.7 [+12.5, +23.1]** |
| 16 | 0.40 | **−9.3 [−16.1, −3.9]** | +2.9 [+1.2, +4.9] |
| 18 | 0.45 | −0.3 [−0.8, +0.2] | +0.2 [−0.2, +0.5] |
| 20-38 | 0.50-0.95 | ≈ 0 | ≈ 0 |

Three properties replicate exactly:

* a rule-span causal effect confined to the **middle of the network** — depth
  0.30–0.40 here against 0.39–0.50 for Qwen3-8B — and nothing at all above it;
* it is present **before the evidence the decision reads has been processed**;
* **breaking is complete**: +18.3 points against a behavioural gap of +18.2.

One property does not. **Rescue is also nearly complete in Mistral** (−16.1
against a gap of +18.2, roughly 88%) where in Qwen3-8B it was ~15%. So the
asymmetry between destroying and creating the suppression state is a property of
Qwen3-8B, not a general one. What generalises across the two architectures is the
localisation and the necessity, not the insufficiency.
