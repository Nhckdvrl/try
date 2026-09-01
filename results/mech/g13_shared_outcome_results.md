# G13 — donor-general packet outcome axis

G13 tested whether verdict-redacted packets from unrelated questions share a
one-dimensional packet-local outcome variable that causally drives the G12
effect. Gemma-3-12B was fixed before activation collection because its G12
paired contrast passed the 5pp causal-entrainment gate.

The Transformers bridge reproduced the behavior on all 64 donor-disjoint test
recipients: YES donor − NO donor = **+16.84pp [11.67, 22.31]**, with 64/64
parses in both conditions. A mean-difference outcome axis learned from 190
recipients generalized to unseen donor identities at layer 29 (balanced
accuracy **0.758**), passing the frozen representation gate.

The causal result did not pass. Exchanging only that axis across every packet
token produced the following bidirectional transfer:

| layer | outcome axis (pp) | 95% CI | orthogonal axis (pp) |
|---:|---:|---:|---:|
| 5 | +0.94 | [-0.35, 2.46] | +0.47 |
| 11 | +1.64 | [-0.27, 3.67] | -0.04 |
| 17 | +0.55 | [-1.17, 2.48] | +0.31 |
| 23 | +1.10 | [-0.70, 2.89] | +0.04 |
| 29 | +0.31 | [-0.55, 1.29] | -0.27 |
| 35 | -0.30 | [-0.90, 0.20] | -0.27 |
| 41 | -0.12 | [-0.66, 0.31] | -0.20 |
| 47 | -0.27 | [-0.86, 0.16] | -0.27 |

No layer reached the preregistered 3pp threshold, so there was no adjacent
causal window and the frozen verdict is **not-established**. The result is a
representation--causality dissociation: donor outcome becomes cross-topic
decodable in packet states, but this packet-mean scalar is not shown to be the
behavioral bottleneck. The next hypothesis is therefore narrower and positive:
outcome evidence may be transformed into a recipient-conditioned decision
variable at the answer position rather than transported as a packet-local
scalar.

Frozen design: `g13-shared-outcome-design-v1`. Sources:
`g13_shared_outcome.json`, `g13_shared_outcome_analysis.json`; activation cache
`g13_shared_outcome_states.npz` is regenerable and is not required to verify the
reported generated-output estimands.
