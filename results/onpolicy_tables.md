# On-policy state externalisation

16 samples per item at T=0.8. Trajectories are split by what the model wrote on
its own `ITEM DECISION WEIGHT` line; the decision is then read at a fixed position.

| model | arm | trajectories stating 0% | REI when it stated 0% | REI when it stated >0% |
|---|---|---:|---|---|
| qwen3-8b | rule PRE | 31% | **+0.225** [+0.028, +0.455] (n=57) | +0.506 |
| qwen3-8b | rule POST | 72% | **+0.100** [-0.082, +0.296] (n=117) | +0.685 |
| gemma3-12b | rule PRE | 55% | **+0.592** [+0.361, +0.831] (n=83) | +0.742 |
| gemma3-12b | rule POST | 66% | **+0.059** [-0.117, +0.254] (n=102) | +0.475 |
| phi4-mini | rule PRE | 54% | **+0.022** [-0.423, +0.473] (n=109) | +0.495 |
| phi4-mini | rule POST | 57% | **-0.035** [-0.434, +0.362] (n=124) | +0.251 |
