# Stage 3E — duplicate control, and what "content" actually means

Two holes in the Stage-3D claim. The first turned out to be a real and large
confound; the second gives the phenomenon a much sharper definition.

## The metric had to change

Under a preview, the admit anchor `|L|` shrinks a lot, so REI (a ratio) becomes
unstable — the earlier Stage-3D table produced values like −1.25 for that reason.
Everything here is reported in **raw rating points** instead:

* `marg(rule)` = the shift the *later* evidence produces given the preview is
  already present: `Y(preview + rule + E) − Y(preview alone)`, sign-aligned.
* **`ExclusionEffect` = `marg(no rule) − marg(exclude)`** — the points the *rule*
  removes on top of whatever the preview already did.

This separates the two effects that were previously entangled.

## P0-A The redundancy confound is real — and it is not the explanation

Marginal leverage of the later evidence, **with no rule at all**:

| preview | Qwen3-8B | Gemma-3-12B | Phi-4-mini |
|---|---|---|---|
| no preview | 32.8 pts | 32.4 | 28.5 |
| exact same text | **5.5** | **2.3** | **2.1** |
| lexical paraphrase | 16.7 | 11.2 | 6.1 |
| independent second source | 17.5 | 7.8 | 11.8 |
| unrelated (control) | 33.7 | 31.5 | 25.9 |

A fact the model has already read keeps only 6–18% of its marginal weight on a
second presentation, with no rule involved. The unrelated-preview control is
unmoved, so this is content redundancy, not "an extra block". **Any rescue
measured as a ratio was partly this.**

But the rule's own contribution moves in a different direction:

| preview | Qwen3-8B | Gemma-3-12B | Phi-4-mini |
|---|---|---|---|
| no preview | +8.5 | +8.9 | +5.9 |
| unrelated (control) | +9.5 | +8.7 | +1.7 (n.s.) |
| exact same text | **+26.7** | **+14.2** | **+11.5** |
| lexical paraphrase | **+26.9** | **+14.1** | **+11.2** |
| independent second source | **+28.3** | **+14.0** | **+14.3** |

All p < 1e-4 except the two noted. In every model a content-matched preview makes
the exclusion rule remove **2–3× as many rating points**, while an unrelated
preview leaves it at the no-preview level.

The decisive argument is the dissociation between the two tables. Across preview
types the redundancy varies by a factor of three (5.5 → 17.5 on Qwen3-8B) while
the ExclusionEffect barely moves (26.7 → 28.3). If the rescue were redundancy,
they would track each other. The "independent second source" preview makes this
sharpest: it is explicitly framed as a second, independent report, it retains the
most marginal leverage of the three matched previews, and it produces the
*largest* exclusion boost.

**The duplicate/redundancy account is rejected.**

## P0-B What relation must hold — the direction of entailment matters

Seven semantic relations between preview and the (fixed) actual evidence, each
with its own preview-only and no-rule conditions so the redundancy is netted out.

| relation preview → actual evidence | Qwen3-8B marg / **ExclEff** | Gemma-3-12B marg / **ExclEff** |
|---|---|---|
| no preview | 31.9 / **+8.0** | 32.4 / **+9.4** |
| mutual entailment (true paraphrase) | 18.1 / **+27.1** | 10.5 / **+15.2** |
| preview entails actual (more specific) | 10.7 / **+29.4** | 8.7 / **+18.7** |
| actual entails preview (gist only) | 26.3 / **+14.1** | 17.0 / **+8.4** |
| one argument changed | 21.9 / **+9.3** | 21.4 / **+4.0** |
| polarity reversed | 47.2 / **+15.6** | 43.3 / **+1.6** |
| high lexical overlap, different meaning | 30.7 / **+9.6** | 30.9 / **+1.2** |
| unrelated | 33.2 / **+9.0** | 30.6 / **+8.5** |

The pattern that replicates in both models:

> **preview ⇒ actual  ≈  mutual entailment  ≫  actual ⇒ preview  ≈  one argument
> changed  ≈  lexical overlap  ≈  unrelated  ≈  no preview**

Three things follow.

* **The direction of entailment matters.** A preview that *entails* the evidence
  — a paraphrase, or a more specific version — lets the rule bind. A preview that
  is merely *entailed by* it, a gist, does not (Gemma +8.4 against a +9.4
  baseline; Qwen partial at +14.1). What the rule needs is a representation at
  least as specific as its target, not merely one about it.
* **It is not lexical and not referential.** High lexical overlap with a different
  meaning, and the same proposition with one argument changed, both sit at the
  no-preview baseline in both models.
* **Polarity is unresolved.** A contradicting preview raises the later evidence's
  own leverage sharply (47.2 / 43.3 points, the highest in the table) and the two
  models disagree on the exclusion boost (+15.6 vs +1.6). Not interpreted here.

## The claim this licenses

Not "content-addressed" in a loose sense, and not string matching:

> A natural-language exclusion rule binds to a **proposition at least as specific
> as its target**. If such a proposition has been instantiated when the rule is
> read, the rule removes two to three times as much of the evidence's causal
> contribution, whatever the surface form; if only a more abstract, lexically
> similar, or referentially adjacent representation is available, the rule
> performs no better than with no preview at all.

Redundancy is a separate, large, and independently real effect that must be netted
out before any of this is visible — reporting it in ratio form hides it.

Still running: Phi-4-mini and Qwen2.5-32B on the de-confounded matrix;
Qwen3.5-27B has only the earlier condition set.
