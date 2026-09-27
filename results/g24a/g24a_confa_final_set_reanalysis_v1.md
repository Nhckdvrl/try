# ConfA final-admissible-set reanalysis

**Post hoc analysis of the original frozen 15,000 cells.** The registered ConfA signed estimands and failed prospective-leakage headline remain unchanged. This reanalysis asks a different question: whether each excluded-evidence response matches the same item's Base response when the final admissible evidence is the same.

Source SHA-256: `a333c0caf5d945c69af54d90dabd9a3704d1b1b27272d2408409ab910ce68899`. All 500 items, six models and five cells per item/model are included. No model inference or item filtering was performed.

| Group | Signed ExcludePre−Base | Absolute ExcludePre−Base | Signed ExcludePost−Base | Absolute ExcludePost−Base | Pre ≥10 pp | Pre ≥20 pp |
|---|---:|---:|---:|---:|---:|---:|
| pooled | -0.15 [-1.68, +1.40] | +19.50 [+18.13, +20.88] | -15.94 [-18.14, -13.73] | +29.91 [+28.39, +31.40] | 43.7% | 31.7% |
| FEVER | +2.14 [+0.29, +3.94] | +18.48 [+16.77, +20.25] | -11.58 [-14.11, -9.12] | +26.75 [+24.81, +28.67] | 37.4% | 28.3% |
| SciFact | -4.74 [-7.38, -2.07] | +21.55 [+19.80, +23.35] | -24.72 [-28.63, -20.55] | +36.28 [+34.01, +38.53] | 56.4% | 38.4% |
| gemma3-12b | +0.20 [-2.15, +2.61] | +16.36 [+14.55, +18.27] | -2.35 [-5.13, +0.38] | +21.20 [+19.20, +23.28] | 52.2% | 30.4% |
| llama31-8b | +1.78 [-0.87, +4.46] | +19.09 [+17.09, +21.11] | -14.27 [-16.99, -11.55] | +26.91 [+25.08, +28.80] | 46.4% | 33.8% |
| mistral-small-24b | -17.55 [-20.40, -14.80] | +25.12 [+22.79, +27.47] | -29.64 [-32.83, -26.44] | +36.19 [+33.53, +38.87] | 57.8% | 43.2% |
| qwen3-32b | +1.23 [-1.58, +4.21] | +18.32 [+15.88, +20.85] | -14.38 [-17.21, -11.37] | +24.62 [+22.33, +26.88] | 39.4% | 29.4% |
| qwen3-8b | +8.19 [+5.00, +11.47] | +20.43 [+17.69, +23.32] | -2.77 [-6.68, +1.25] | +27.46 [+24.24, +30.76] | 38.0% | 31.6% |
| qwen35-9b | +5.27 [+2.08, +8.42] | +17.67 [+14.91, +20.51] | -32.24 [-36.52, -28.01] | +43.10 [+39.70, +46.51] | 28.4% | 21.6% |

## Mapping of Base judgments

OLS slopes below 1 describe compression of the 0–100 output range relative to the same-item Base rating. This is a behavioral description, not an internal-state claim.

| Group | AdmitPre slope | AdmitPost slope | ExcludePre slope | ExcludePost slope | ExcludePre correlation |
|---|---:|---:|---:|---:|---:|
| pooled | 0.771 | 0.778 | 0.672 | 0.435 | 0.678 |
| FEVER | 0.779 | 0.785 | 0.685 | 0.482 | 0.706 |
| SciFact | 0.640 | 0.650 | 0.611 | 0.299 | 0.557 |
| gemma3-12b | 0.872 | 0.858 | 0.722 | 0.638 | 0.739 |
| llama31-8b | 0.691 | 0.715 | 0.665 | 0.419 | 0.681 |
| mistral-small-24b | 0.866 | 0.871 | 0.517 | 0.267 | 0.653 |
| qwen3-32b | 0.810 | 0.809 | 0.720 | 0.526 | 0.709 |
| qwen3-8b | 0.677 | 0.706 | 0.673 | 0.611 | 0.634 |
| qwen35-9b | 0.741 | 0.741 | 0.710 | 0.192 | 0.696 |

Bootstrap intervals resample items (5,000 draws), retaining all models for each item. The source mixes 334 FEVER and 166 SciFact items. Signed effects use the original critical-direction normalization; absolute effects use the raw 0–100 readout. The full JSON also reports admitted-evidence absolute shifts and post-exclusion thresholds.

This comparison is a behavioral final-set criterion under each frozen prompt. Prompt framing differs from Base, and a nonzero absolute difference alone does not identify the mechanism. It does directly test the item-wise invariance target that the original signed mean cannot establish.
