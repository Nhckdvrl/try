# Llama-3.1-8B behavioral extension

**Frozen design:** `llama-behavioral-extension-design-v1`
**Model:** `NousResearch/Meta-Llama-3.1-8B-Instruct` at revision
`d10aef7999a2b5ba950ab3974312feeedbfe0b77`

This prospective extension asks how far a canonical Meta-family checkpoint
follows the paper's explanatory descent from natural hindsight to directional
outcome influence. It does not replace Mistral or alter any verdict from the
original Qwen/Gemma/Mistral panels.

## Results

| level | result | frozen interpretation |
|---|---|---|
| A1: natural hindsight | +28.23pp [24.53, 31.85]; OOB timing recognition 250/256 (97.66%) | strong headline effect; original G4 two-frame qualification remains failed because the licensed/all-information probe was only 127/256 |
| G8: foreign packet | 256/256 parsed; donor pull +10.10pp [6.24, 13.97]; absolute movement is 70.1% of own-packet movement | cross-event presence supported |
| G11: verdict-redacted foreign packet | 255 complete units; donor pull +11.69pp [8.29, 15.10]; 115.6% retention | corrected scientific verdict `survives` |
| G12: paired outcome direction | 254 complete pairs; YES-supporting minus NO-supporting packet: +18.06pp [14.45, 21.68]; recipient-aligned validity -0.25pp [-4.42, 4.04] | `causal-outcome-entrainment` |

The corrected scientific verdict is **`full-explanatory-chain`**. The original
preregistered extension verdict remains **`partial-chain`** in the analysis
artifact because G8 treated a model-dependent recipient-response quantity as
an assignment-leakage test. The same legacy check narrowly fails in G11 after
valid `0.` outputs are recovered. The post-result correction is documented in
`preregistrations/ANALYSIS_CORRECTION_G8_VALIDITY.md`; no threshold, seed,
unit, or raw output was changed.

The experiments now answer separate successive questions: G8 establishes that
foreign events still move the judgment, G11 shows that the donor-direction
signal survives explicit-verdict removal, and G12 identifies its causal effect
within the same recipient.

## Paper interpretation

Llama strengthens the paper at the two levels that matter most for its main
arc: it shows a large natural hindsight effect, and a clean paired manipulation
of verdict-redacted outcome evidence changes the direction of the same
historical judgment. Together with G11, the result shows that this influence
does not depend on a visible YES/NO verdict.

It does **not** license a claim that every intermediate gate passed or that the
original three-model G12 panel became positive. The original panel remains
`indeterminate`; Mistral remains a genuine weak, verdict-dependent case.

## Integrity and artifacts

- Design commit/tag precedes all new generations: `5f3b469` /
  `llama-behavioral-extension-design-v1`.
- Data artifact SHA-256: `0b6fd8d0...acf0901d`.
- G8/G11 pairing SHA-256: `a51b80c7...cec1c2`.
- G12 assignment SHA-256: `19ce7ce1...a6c1`.
- New volume: 2,048 generations; no regeneration was required for the parser
  and estimator corrections. Full machine-readable analysis is in
  `results/llama_behavioral_extension_analysis.json`.
