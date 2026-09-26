# G29 revocation status vs prior contradictory exposure

Fresh material: 80 audited pairs, both E2 directions. Paired claim-cluster bootstrap (5,000 draws); interval is over claims, models fixed. Binary contrasts use proportions; scores are 0–100. Registration predates all G29 outputs.

## Raw integrity

| Model | Rows | Binary unparsed | Rating unparsed | Rating mass<.5 | Rationale caps |
|---|---:|---:|---:|---:|---:|
| mistral-small-24b | 1280 | 0 | 0 | 0 | 2 |
| qwen3-8b | 1280 | 0 | 0 | 0 | 0 |
| gemma3-12b | 1280 | 0 | 0 | 0 | 0 |

## Primary paired R−N contrast

`T` is aligned with old E1; negative means stronger uptake of opposite E2 in the revoked history.

| Models | E2 | Signed binary T | Binary disagreement | R E2 choice rate | N E2 choice rate | Signed rating T | Mean absolute rating difference |
|---|---|---:|---:|---:|---:|---:|---:|
| pooled | both | 0.021 [-0.002, 0.044] | 0.062 [0.040, 0.087] | 0.783 [0.740, 0.825] | 0.804 [0.765, 0.844] | 1.402 [-0.404, 3.257] | 5.079 [3.528, 6.798] |
| pooled | support | 0.012 [-0.017, 0.042] | 0.054 [0.025, 0.087] | 0.863 [0.800, 0.921] | 0.875 [0.821, 0.925] | 1.170 [-1.325, 3.958] | 5.124 [2.883, 7.816] |
| pooled | refute | 0.029 [-0.008, 0.067] | 0.071 [0.037, 0.108] | 0.704 [0.629, 0.779] | 0.733 [0.662, 0.796] | 1.634 [-0.367, 3.918] | 5.033 [3.209, 7.159] |
| mistral-small-24b | both | 0.037 [0.000, 0.075] | 0.075 [0.037, 0.119] | 0.831 [0.769, 0.887] | 0.869 [0.812, 0.919] | -0.062 [-3.907, 3.397] | 6.517 [3.600, 10.087] |
| mistral-small-24b | support | 0.050 [0.000, 0.113] | 0.075 [0.025, 0.138] | 0.800 [0.713, 0.887] | 0.850 [0.762, 0.925] | -1.399 [-6.414, 3.183] | 7.118 [2.837, 12.080] |
| mistral-small-24b | refute | 0.025 [-0.037, 0.087] | 0.075 [0.025, 0.138] | 0.863 [0.787, 0.938] | 0.887 [0.812, 0.950] | 1.275 [-2.651, 5.329] | 5.916 [2.727, 10.198] |
| qwen3-8b | both | 0.000 [-0.037, 0.037] | 0.050 [0.019, 0.087] | 0.713 [0.656, 0.769] | 0.713 [0.656, 0.769] | 2.168 [-0.369, 4.973] | 4.271 [2.015, 7.036] |
| qwen3-8b | support | 0.013 [-0.025, 0.062] | 0.037 [0.000, 0.087] | 0.900 [0.838, 0.963] | 0.912 [0.850, 0.975] | 1.809 [-1.238, 5.902] | 3.779 [0.775, 7.805] |
| qwen3-8b | refute | -0.013 [-0.075, 0.037] | 0.062 [0.013, 0.125] | 0.525 [0.412, 0.637] | 0.512 [0.412, 0.625] | 2.528 [-0.689, 6.385] | 4.763 [1.816, 8.538] |
| gemma3-12b | both | 0.025 [-0.013, 0.062] | 0.062 [0.031, 0.100] | 0.806 [0.750, 0.856] | 0.831 [0.781, 0.881] | 2.099 [0.409, 4.100] | 4.448 [2.789, 6.496] |
| gemma3-12b | support | -0.025 [-0.075, 0.025] | 0.050 [0.013, 0.100] | 0.887 [0.812, 0.950] | 0.863 [0.787, 0.938] | 3.100 [0.575, 6.521] | 4.476 [2.048, 7.857] |
| gemma3-12b | refute | 0.075 [0.025, 0.138] | 0.075 [0.025, 0.138] | 0.725 [0.625, 0.825] | 0.800 [0.713, 0.887] | 1.099 [-1.232, 3.971] | 4.420 [2.332, 7.063] |

## Reference conditions

| Models | Condition | E2-aligned direct choice rate | Rating E2 separation |
|---|---|---:|---:|
| pooled | R | 0.783 [0.740, 0.825] | 73.127 [66.917, 78.805] |
| pooled | N | 0.804 [0.765, 0.844] | 75.931 [69.847, 81.509] |
| pooled | A | 0.625 [0.583, 0.669] | 12.091 [8.137, 16.149] |
| pooled | D | 0.838 [0.796, 0.877] | 68.863 [62.023, 75.191] |
| mistral-small-24b | R | 0.831 [0.769, 0.887] | 79.267 [71.699, 86.100] |
| mistral-small-24b | N | 0.869 [0.812, 0.919] | 79.143 [70.788, 86.565] |
| mistral-small-24b | A | 0.731 [0.669, 0.787] | 16.152 [8.950, 23.665] |
| mistral-small-24b | D | 0.863 [0.812, 0.906] | 77.283 [69.193, 84.799] |
| qwen3-8b | R | 0.713 [0.656, 0.769] | 76.207 [67.161, 84.081] |
| qwen3-8b | N | 0.713 [0.656, 0.769] | 80.543 [72.355, 88.231] |
| qwen3-8b | A | 0.544 [0.487, 0.600] | 12.908 [5.573, 20.394] |
| qwen3-8b | D | 0.812 [0.756, 0.863] | 69.844 [60.609, 78.339] |
| gemma3-12b | R | 0.806 [0.750, 0.856] | 63.907 [55.982, 71.453] |
| gemma3-12b | N | 0.831 [0.781, 0.881] | 68.105 [60.462, 75.203] |
| gemma3-12b | A | 0.600 [0.537, 0.662] | 7.214 [0.977, 13.681] |
| gemma3-12b | D | 0.838 [0.787, 0.887] | 59.461 [50.141, 68.805] |

## Interpretation boundary

Mistral's active-conflict reference has two 110-token rationale caps; the registered R−N comparison has no capped rows. No rows are dropped.

R and N differ in admissibility history and the words that convey it. Any R−N effect is behavioral evidence for status/history sensitivity after identical E1 exposure; it does not localize an internal state or show a universal law. The A reference intentionally has a different final admissible set. All materials were fixed before model inference; the G29 direction was motivated by observed G28 outcomes.
