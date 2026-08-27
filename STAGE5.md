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

## Both directions localise to layers 12–20, at the rule

Recovery fraction: 1.0 means the patched run answers like the donor condition,
0.0 like its own. Median over items.

| layer | preview end | rule end | **rule SPAN** | evidence end | answer |
|---:|---|---|---|---|---|
| | | *success → failure (does it rescue?)* | | | |
| 10 | +0.01 | −0.03 | +0.02 | +0.07 | −0.02 |
| 12 | +0.06 | +0.00 | +0.18 | +0.11 | −0.02 |
| 14 | +0.00 | +0.14 | **+0.43** | +0.14 | +0.00 |
| 16 | −0.09 | +0.18 | **+0.54** | +0.14 | +0.05 |
| 18 | −0.05 | +0.24 | **+0.46** | +0.09 | +0.10 |
| 20 | −0.01 | +0.22 | +0.19 | +0.07 | +0.33 |
| 22 | −0.00 | +0.03 | +0.04 | +0.00 | +0.74 |
| | | *failure → success (does it break it?)* | | | |
| 10 | −0.01 | −0.02 | −0.08 | +0.03 | +0.02 |
| 12 | −0.02 | +0.02 | +0.37 | +0.04 | +0.04 |
| 14 | −0.04 | +0.16 | **+0.92** | +0.08 | +0.09 |
| 16 | −0.11 | +0.26 | **+0.88** | +0.18 | +0.08 |
| 18 | −0.08 | +0.25 | **+0.57** | +0.10 | +0.19 |
| 20 | −0.02 | +0.10 | +0.12 | +0.04 | +0.45 |
| 22 | −0.00 | −0.00 | +0.01 | −0.00 | +0.82 |

Reading this:

* **At the rule block, in layers 12–20, there is a state that differs between the
  two runs and is causally responsible for the difference in suppression.**
  Transplanting it from the successful run into the failing one recovers 54% of
  the gap at layer 16; transplanting it the other way destroys 92% of the
  successful suppression at layer 14.
* **It exists before the evidence the decision reads has been processed.** The
  rule block ends before the evidence block begins in both runs.
* **It is not just the preview's content sitting in context.** Patching the
  preview-end position transfers nothing at any layer (−0.11 to +0.06).
* **It is not the readout.** The answer position shows the expected trivial
  late-layer transfer (0.74–0.97 from layer 22), and the rule-span effect has
  already collapsed to zero by then. The two are separate.
* **Breaking is easier than creating** (0.92 against 0.54). A single-position
  patch at the rule's last token transfers only about a quarter of the gap in
  either direction, so the state is distributed across the rule block rather than
  summarised at its end.

## What this licenses, and what it does not

Licensed: by the time the exclusion rule has been read, the model has formed a
state, distributed over the rule tokens and living in the middle layers, whose
content depends on whether a proposition matching the rule's target was available
— and that state is bidirectionally causal for whether the later evidence is
suppressed.

Not licensed: any claim about what that state *represents*. Patching shows it
carries the difference; it does not show it is an "exclusion tag bound to a
proposition" rather than, say, a general readiness state that happens to covary.
Distinguishing those needs probing or a feature-level decomposition, which is not
done here.

Single model (Qwen3-8B) and single readout position. The direct readout is
validated against the behavioural one for these two families (r = 0.76 / 0.90),
but the mechanism result should be replicated on at least one other family of
model before it carries weight.
