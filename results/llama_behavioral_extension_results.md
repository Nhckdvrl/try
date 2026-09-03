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
| G8: foreign packet | donor pull +10.07pp [6.20, 13.94]; absolute movement is 69.8% of own-packet movement | directional result is positive, but the inherited pairing-validity gate fails because recipient-own pull is -4.01pp [-8.09, 0.00] rather than wholly inside [-5, 5] |
| G11: verdict-redacted foreign packet | donor pull +11.31pp [8.01, 14.64]; 114.4% retention; explicit-label contribution -1.43pp [-4.09, 1.31] | `survives` |
| G12: paired outcome direction | YES-supporting minus NO-supporting packet: +18.03pp [14.48, 21.61]; recipient-aligned validity -0.15pp [-4.41, 4.18] | `causal-outcome-entrainment` |

The frozen overall verdict is **`partial-chain`**, solely because G8's
recipient-balance validity interval crosses the inherited equivalence bound.
The direct paired G12 intervention avoids that accidental pairing imbalance
and provides strong evidence that changing the outcome supported by later
evidence changes the same Llama judgment.

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
- New volume: 2,048 generations; full machine-readable analysis is in
  `results/llama_behavioral_extension_analysis.json`.
