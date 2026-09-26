# G28B matched irrelevant-read control

Exploratory, registered after observing preliminary G28A results. Reuses every frozen G28A RR score and adds 400 IR scores per model; no item selection. Post hoc audit-restricted sensitivity on 142/200 items.
Claim-cluster paired bootstrap, 5,000 draws. Scores 0–100. Llama-3.1-8B is an unplanned substitute for unsupported Qwen3.5-9B.

## G28B raw integrity

| Model | New IR rows | Unparsed | Digit mass <0.5 | Rationale caps |
|---|---:|---:|---:|---:|
| mistral-small-24b | 400 | 0 | 0 | 0 |
| qwen3-8b | 400 | 0 | 0 | 0 |
| gemma3-12b | 400 | 0 | 0 | 0 |

## Matched read contrast

T_read_matched = sign(revoked relevant E1) × (RR−IR). RR and IR both contain a read-only first turn and identical acknowledgment and final turn.

| Model | Both directions | E2 support | E2 refute | Mean abs(RR−IR) | RR sep | IR sep | 50-threshold flip % |
|---|---:|---:|---:|---:|---:|---:|---:|
| mistral-small-24b | -5.69 [-8.10,-3.30] | -1.19 [-4.21,1.61] | -10.18 [-14.65,-5.82] | 10.13 [7.67,12.71] | 82.44 [77.84,86.58] | 71.07 [65.05,77.12] | 10.2 |
| qwen3-8b | -5.48 [-8.83,-2.11] | -1.68 [-5.05,1.41] | -9.28 [-15.30,-3.18] | 13.12 [10.11,16.09] | 75.89 [69.79,81.97] | 64.93 [58.39,71.48] | 12.7 |
| gemma3-12b | -2.29 [-4.82,0.41] | 0.62 [-2.45,3.58] | -5.19 [-9.73,-0.43] | 12.21 [9.82,14.62] | 62.42 [56.30,68.31] | 57.84 [51.68,63.99] | 12.3 |
| pooled | -4.48 [-6.27,-2.68] | -0.75 [-2.58,1.01] | -8.22 [-11.49,-4.84] | 11.82 [10.11,13.57] | 73.58 [69.07,78.01] | 64.61 [59.56,69.73] | 11.7 |

A negative contrast indicates stronger movement toward opposing new evidence after relevant E1 than after irrelevant E1. This comparison isolates prior *content relevance* within read-only histories, but it does not isolate the causal contribution of the *retraction instruction* from general opposing-evidence sensitivity. The reused 200 claims and post-G28A registration prevent a confirmatory claim.
