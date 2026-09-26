# G28B matched irrelevant-read control

Exploratory, registered after observing preliminary G28A results. Reuses every frozen G28A RR score and adds 400 IR scores per model; no item selection. Post hoc audit-restricted sensitivity on 199/200 items.
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
| mistral-small-24b | -5.72 [-8.41,-3.14] | -0.52 [-3.80,2.66] | -10.91 [-15.07,-6.94] | 12.59 [10.21,15.03] | 79.22 [74.57,83.55] | 67.78 [62.28,73.13] | 12.6 |
| qwen3-8b | -4.41 [-7.02,-1.80] | -0.53 [-3.50,2.50] | -8.29 [-12.97,-3.54] | 13.01 [10.44,15.64] | 71.21 [65.42,76.68] | 62.38 [56.68,68.13] | 12.8 |
| gemma3-12b | -3.48 [-5.75,-1.21] | -0.92 [-3.79,1.77] | -6.04 [-9.95,-2.06] | 12.60 [10.62,14.65] | 59.68 [54.50,64.74] | 52.72 [47.17,58.29] | 13.1 |
| pooled | -4.54 [-6.12,-2.97] | -0.66 [-2.52,1.09] | -8.42 [-11.10,-5.67] | 12.73 [11.22,14.22] | 70.04 [65.75,74.16] | 60.96 [56.45,65.63] | 12.8 |

A negative contrast indicates stronger movement toward opposing new evidence after relevant E1 than after irrelevant E1. This comparison isolates prior *content relevance* within read-only histories, but it does not isolate the causal contribution of the *retraction instruction* from general opposing-evidence sensitivity. The reused 200 claims and post-G28A registration prevent a confirmatory claim.
