# G28B matched irrelevant-read control

Exploratory, registered after observing preliminary G28A results. Reuses every frozen G28A RR score and adds 400 IR scores per model; no item selection. Full frozen 200-item sample.
Claim-cluster paired bootstrap, 5,000 draws. Scores 0–100. Llama-3.1-8B is an unplanned substitute for unsupported Qwen3.5-9B.

## G28B raw integrity

| Model | New IR rows | Unparsed | Digit mass <0.5 | Rationale caps |
|---|---:|---:|---:|---:|
| mistral-small-24b | 400 | 0 | 0 | 0 |
| qwen3-8b | 400 | 0 | 0 | 0 |
| gemma3-12b | 400 | 0 | 0 | 0 |
| llama31-8b | 400 | 0 | 0 | 0 |

## Matched read contrast

T_read_matched = sign(revoked relevant E1) × (RR−IR). RR and IR both contain a read-only first turn and identical acknowledgment and final turn.

| Model | Both directions | E2 support | E2 refute | Mean abs(RR−IR) | RR sep | IR sep | 50-threshold flip % |
|---|---:|---:|---:|---:|---:|---:|---:|
| mistral-small-24b | -5.70 [-8.39,-3.06] | -0.52 [-3.80,2.74] | -10.89 [-15.10,-6.88] | 12.54 [10.25,15.08] | 79.30 [74.55,83.63] | 67.89 [62.43,73.27] | 12.5 |
| qwen3-8b | -4.64 [-7.34,-1.93] | -0.53 [-3.49,2.56] | -8.75 [-13.58,-3.93] | 13.19 [10.64,15.84] | 71.35 [65.53,77.15] | 62.07 [56.14,67.96] | 13.0 |
| gemma3-12b | -3.63 [-5.91,-1.30] | -0.92 [-3.83,1.79] | -6.35 [-10.28,-2.48] | 12.71 [10.65,14.71] | 59.77 [54.51,64.91] | 52.50 [46.91,58.14] | 13.2 |
| llama31-8b | -5.20 [-8.40,-1.98] | 1.41 [-1.90,4.66] | -11.80 [-17.88,-5.77] | 19.18 [16.43,22.05] | 38.64 [32.76,44.81] | 28.25 [22.78,33.98] | 20.2 |
| pooled | -4.79 [-6.30,-3.25] | -0.14 [-1.86,1.51] | -9.45 [-12.09,-6.68] | 14.41 [13.12,15.70] | 62.26 [58.05,66.47] | 52.68 [48.34,56.93] | 14.8 |

A negative contrast indicates stronger movement toward opposing new evidence after relevant E1 than after irrelevant E1. This comparison isolates prior *content relevance* within read-only histories, but it does not isolate the causal contribution of the *retraction instruction* from general opposing-evidence sensitivity. The reused 200 claims and post-G28A registration prevent a confirmatory claim.
