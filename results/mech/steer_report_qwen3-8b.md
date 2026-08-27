# Exclusion-specificity and transferability of the rule-span state — qwen3-8b

28 of 35 held-out items with a behavioural gap >= 2 points; the
steering direction was estimated on 35 disjoint training items.

## 1. Is the transfer exclusion-specific?

Whole rule-span transfer inside each arm. If the matched preview transferred only
proposition information, `MA -> UA` would move as much as `ME -> UE`.

| layer | ME -> UE (exclude arm) | MA -> UA (admit arm) |
|---:|---|---|
| 0 | +0.00 | +0.00 |
| 2 | -0.07 | -0.07 |
| 4 | -0.15 | -0.12 |
| 6 | -0.17 | -0.11 |
| 8 | -0.06 | -0.05 |
| 10 | -0.10 | -0.05 |
| 12 | -0.07 | -0.00 |
| 14 | -0.05 | -0.00 |
| 16 | +0.06 | +0.23 |
| 18 | +0.07 | +0.15 |
| 20 | +0.05 | +0.09 |
| 22 | +0.00 | +0.00 |
| 24 | -0.01 | +0.00 |
| 26 | -0.00 | -0.00 |
| 28 | -0.00 | -0.00 |
| 30 | +0.00 | -0.00 |
| 32 | -0.00 | -0.00 |
| 34 | +0.00 | -0.00 |

## 2. Does a direction estimated on other items control suppression?

`v_l = mean[(h_ME - h_MA) - (h_UE - h_UA)]` over training items, added to the
failing run's rule span and subtracted from the succeeding run's. alpha is a
fraction of that layer's mean activation magnitude. Values are the change in the
sign-aligned rating, in points; negative means more suppression.

| layer | UE +0.05v | UE +0.1v | UE +0.2v | UE +0.4v | ME −0.05v | ME −0.1v | ME −0.2v | ME −0.4v |
|---:|---|---|---|---|---|---|---|---|
| 0 | +0.1 | +0.4 | +0.5 | +1.0 | +0.3 | +0.5 | -0.5 | -0.3 |
| 2 | +0.6 | +1.0 | +2.2 | +4.2 | -0.4 | -0.9 | -1.2 | -0.4 |
| 4 | -0.1 | +0.3 | +1.1 | +1.9 | -0.8 | -0.9 | -1.0 | -2.0 |
| 6 | +1.1 | +1.9 | +4.1 | +8.1 | -0.7 | -2.2 | -2.3 | +2.1 |
| 8 | +0.6 | +1.1 | +2.8 | +5.7 | -0.9 | -1.8 | -3.2 | -4.3 |
| 10 | -0.2 | +0.3 | +0.8 | +3.1 | -0.0 | +0.1 | -0.3 | +0.8 |
| 12 | +0.5 | +0.6 | +1.6 | +4.1 | +0.8 | +1.1 | +2.6 | +5.8 |
| 14 | +0.4 | +1.0 | +2.2 | +4.8 | +0.5 | +0.6 | +3.3 | +7.7 |
| 16 | -0.1 | -0.0 | +0.4 | +3.2 | +0.6 | +1.2 | +2.6 | +5.3 |
| 18 | -0.3 | -0.2 | -0.3 | +0.2 | +0.5 | +0.9 | +1.9 | +3.9 |
| 20 | -0.2 | -0.1 | -0.1 | +0.4 | +0.1 | +0.4 | +0.7 | +2.2 |
| 22 | +0.0 | +0.1 | +0.2 | +0.5 | +0.1 | -0.3 | -0.2 | -0.1 |
| 24 | +0.1 | +0.1 | +0.0 | +0.7 | +0.1 | -0.2 | -0.2 | -0.1 |
| 26 | -0.1 | -0.1 | -0.1 | -0.1 | +0.0 | +0.2 | -0.0 | +0.3 |
| 28 | -0.1 | -0.0 | -0.1 | +0.1 | +0.1 | +0.0 | -0.0 | +0.3 |
| 30 | -0.1 | -0.2 | -0.1 | -0.1 | +0.3 | +0.0 | +0.2 | -0.0 |
| 32 | -0.1 | -0.1 | -0.0 | -0.1 | +0.1 | +0.1 | +0.1 | +0.0 |
| 34 | -0.1 | -0.0 | -0.1 | +0.0 | +0.1 | +0.0 | +0.4 | +0.0 |

Strongest layer 26, largest alpha: adding the held-out direction to the failing run changes the sign-aligned rating by **-0.1 [-0.3, +0.0]** points.
