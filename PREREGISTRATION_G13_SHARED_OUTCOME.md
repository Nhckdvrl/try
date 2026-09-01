# G13 preregistration — Is there a shared causal outcome variable?

**Created:** 2026-09-01. No G13 target-model activation or output may be
generated before this document, code, audit, and tests are committed and tagged.

## 1. Scientific question and competing explanations

G12 directly changes the outcome supported by an irrelevant future packet while
holding the historical question fixed. The paired effect is positive in all
three models and large in Gemma-3-12B (+17.50pp). G13 asks:

> Do semantically unrelated future packets form a shared internal outcome
> variable that causally drives reconstruction of the past?

- **H-shared:** evidence from different questions is compressed into a
  donor-general outcome variable; exchanging that variable should transfer the
  packet's directional influence.
- **H-item-specific:** each packet affects the answer through content-specific
  semantic integration; outcome may be decodable, but no donor-general scalar
  is causally transferable.

The mechanism is not the headline object. It adjudicates why the manipulated
future outcome in G12 changes the same reconstructed judgment.

## 2. Frozen model, units, and split

The target is `google/gemma-3-12b-it` at revision
`96b6f1eccf38110c56df3a15bffe176da04bfd80`, selected before G13 because it is
the sole G12 model passing the 5pp causal-entrainment gate. Prompts are exactly
G12's verdict-redacted YES/NO donor pair.

A deterministic graph-connected test set contains 64 recipients. Starting from
the recipient with minimum SHA-256 of `g13-test|unit_id`, repeatedly add the
minimum-hash unselected recipient sharing either donor with the selected set.
Training contains every remaining recipient whose two donor identities never
occur in test; the two boundary recipients are unused. Frozen counts: 190 train,
64 test, 2 buffer; 65 unique test donors. Test-set digest:
`9141b929425aa1bcb6b393eab767b93e19113e78aabab7d3eb16f3ae96b13dcb`.
Thus no donor question used to learn the axis occurs in the causal test.

## 3. Representation and intervention

Candidate decoder layers are `[5, 11, 17, 23, 29, 35, 41, 47]` (zero-based).
At each layer, average the residual stream over the mechanically located packet
span. On the 190 training recipients, define the unit vector

```text
v_l = normalize(mean(h_l | donor YES) - mean(h_l | donor NO)).
```

Donor-general readout is the balanced accuracy on the 64 held-out recipients
using the midpoint of the two training projection means as the frozen threshold.

For each held-out recipient and layer, exchange only this one-dimensional packet
component in both directions. For NO -> YES:

```text
h_NO,t' = h_NO,t + (<hbar_YES,v_l> - <hbar_NO,v_l>) v_l
```

for every packet token `t`; YES -> NO is symmetric. All orthogonal residual
content, every token outside the packet, and the prompt remain unchanged. The
model then greedily generates the same strict 0--100 answer. A deterministic
unit vector orthogonal to `v_l` receives the identical source-to-target
projection exchange and is the single causal-specificity control.

Volume on test: 128 unpatched baselines plus 8 layers × 64 recipients × 2
directions × 2 axes = 2,176 patched generations (2,304 total). Activations for
the 190 train, 64 test, and 2 buffer recipients are captured once. Batch size may
change only for memory; prompts, outputs, layers, and estimands may not.

## 4. Estimands and gates

All intervals use a 10,000-draw paired bootstrap over recipient (`seed=20260829`).

- **Bridge:** the Transformers baseline must parse at least 62/64 per condition
  and reproduce a YES-minus-NO contrast of at least 10pp with CI lower > 0.
- **Shared representation:** held-out balanced accuracy must be at least 0.75 at
  one candidate layer.
- At layer `l`, bidirectional causal transfer is

```text
E_l = mean_i 0.5 * [(patched_NO->YES - NO)
                  + (YES - patched_YES->NO)].
```

  A layer has meaningful transfer when `E_l >= 3pp` and CI lower > 0.
- **Causal window:** at least two adjacent candidate layers must have meaningful
  transfer. Among qualifying layers, the one with largest `E_l` is the frozen
  peak (ties earlier).
- **Axis specificity:** at the peak, the paired difference between outcome-axis
  transfer and orthogonal-axis transfer must have CI lower > 0.

G13 supports **H-shared** only if the bridge, representation, causal-window, and
axis-specificity gates all pass. Otherwise it supports neither internal account;
decodability alone is never called a mechanism. Direction-specific effects and
recovery `E_l / baseline_contrast` are descriptive.

## 5. Freeze checklist

- [x] question and competing explanations fixed
- [x] model, split, layers, intervention, estimands, and gates fixed
- [x] implementation tests and no-model dry audit pass (3 focused tests; 256
  units, 512 paired prompts; longest 5,341 tokens; packet spans 132--3,463)
- [x] design commit `9d6539f` and tag `g13-shared-outcome-design-v1`
  precede all target activations/output
