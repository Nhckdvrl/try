# Pilot P2 — same-claim counterfactual reconstruction (Layer 2)

Frozen readout: `g24a_competing_accounts_v1.md` §9 — e = +1 arm+ (E_support) / −1 arm− (E_refute); A_e = e(Y_Admit,e − Y0), R_k,e = e(Y_k,e − Y0), C_k,e = e(Y_k,e − Y_Admit,e), D_k,e = |Y_k,e − Y0|; ideal deletion R_k,+ = R_k,− = 0 (gap = 0).  Y0 is a single evidence-free Base row per (claim, model) — byte-identical prompt for both arms, shared by construction.  A is continuous, never filtered; no gates, no p-values, no bootstrap, no selection.

Sign reading: aligned A < 0 = evidence moved against its own direction; aligned R < 0 = over-correction past Base (support retraction leaves Y < Y0; refute retraction leaves Y > Y0).

## Integrity

- rows: 9000 (5 models × 1,800) — expected 9,000
- unparsed decisions: 0
- digit-mass < 0.5: 0
- rationale hit token cap: 5
- per file: gemma3-12b/minus=800, gemma3-12b/plus=1000, llama31-8b/minus=800, llama31-8b/plus=1000, mistral-small-24b/minus=800, mistral-small-24b/plus=1000, qwen3-8b/minus=800, qwen3-8b/plus=1000, qwen35-9b/minus=800, qwen35-9b/plus=1000
- per-cell identity C = R − A asserted on every cell
- shared-Y0: exactly one Base row per (claim, model), arm− file contains no base rows (asserted)

## 1. Trajectories — mean Y (0..100), pooled over 5 models × 200 claims

| arm | Base | AdmitPost | ExcludePost | StrongExcludePost | CounterfactualDeletePost |
|---|---|---|---|---|---|
| arm+ (support) | 50.24 | 89.34 | 47.40 | 46.59 | 51.21 |
| arm- (refute) | 50.24 | 33.02 | 28.52 | 39.45 | 39.20 |

Per model × arm:

| model | arm | Base | AdmitPost | ExcludePost | StrongExcludePost | CounterfactualDeletePost |
|---|---|---|---|---|---|---|
| mistral-small-24b | arm+ (support) | 40.75 | 90.68 | 26.25 | 36.80 | 41.99 |
| mistral-small-24b | arm- (refute) | 40.75 | 23.94 | 21.32 | 32.49 | 38.50 |
| llama31-8b | arm+ (support) | 55.35 | 83.13 | 55.56 | 47.35 | 42.13 |
| llama31-8b | arm- (refute) | 55.35 | 44.17 | 49.36 | 53.16 | 45.50 |
| gemma3-12b | arm+ (support) | 59.39 | 88.82 | 65.42 | 57.37 | 53.51 |
| gemma3-12b | arm- (refute) | 59.39 | 40.16 | 34.02 | 54.69 | 53.27 |
| qwen3-8b | arm+ (support) | 54.26 | 92.22 | 55.07 | 42.72 | 47.78 |
| qwen3-8b | arm- (refute) | 54.26 | 33.27 | 19.59 | 30.70 | 29.23 |
| qwen35-9b | arm+ (support) | 41.45 | 91.84 | 34.69 | 48.71 | 70.66 |
| qwen35-9b | arm- (refute) | 41.45 | 23.54 | 18.34 | 26.19 | 29.48 |

## 2. Leverage A_e (pooled, continuous — nothing filtered)

| quantity | arm+ (support) | arm- (refute) |
|---|---|---|
| A_e (aligned) | 39.10 | 17.23 |
| A_e raw (Y_admit - Y0) | 39.10 | -17.23 |
| cells with aligned A < 0 | 138 / 1000 | 354 / 1000 |

## 3. Residuals R_k,e (pooled; ideal = 0, gap = 0)

| k | arm+ (support) | arm- (refute) | gap R+ - R- | C_k | D_k | C/-A |
|---|---|---|---|---|---|---|
| ExcludePost | -2.84 | 21.72 | -24.56 | -41.94 / 4.49 | 31.97 / 33.99 | 1.07 / -0.26 |
| StrongExcludePost | -3.65 | 10.80 | -14.45 | -42.75 / -6.43 | 28.15 / 27.63 | 1.09 / 0.37 |
| CounterfactualDeletePost | 0.97 | 11.04 | -10.07 | -38.13 / -6.18 | 30.14 / 31.11 | 0.98 / 0.36 |

Unaligned (raw) means — the pooled cancellation view:

| quantity (unaligned mean) | ExcludePost | StrongExcludePost | CounterfactualDeletePost |
|---|---|---|---|
| R+ raw (support arm) | -2.84 | -3.65 | 0.97 |
| R− raw (refute arm) | -21.72 | -10.80 | -11.04 |
| R raw (both arms pooled) | -12.28 | -7.22 | -5.04 |

## 4. Over-correction cell counts (descriptive, /1000 cells per (k, arm))

| cell class (aligned) | arm+ (support) | arm- (refute) |
|---|---|---|
| ExcludePost: R < 0 (over-correction past Base) | 506 / 1000 | 308 / 1000 |
| StrongExcludePost: R < 0 (over-correction past Base) | 544 / 1000 | 391 / 1000 |
| CounterfactualDeletePost: R < 0 (over-correction past Base) | 530 / 1000 | 381 / 1000 |

## 5. Per model — A and R

| model | A arm+ (support) | A arm- (refute) | R ExcludePost (arm+ (support)) | R StrongExcludePost (arm+ (support)) | R CounterfactualDeletePost (arm+ (support)) | R ExcludePost (arm- (refute)) | R StrongExcludePost (arm- (refute)) | R CounterfactualDeletePost (arm- (refute)) |
|---|---|---|---|---|---|---|---|---|
| mistral-small-24b | 49.93 | 16.81 | -14.50 | -3.95 | 1.24 | 19.43 | 8.26 | 2.25 |
| llama31-8b | 27.78 | 11.18 | 0.21 | -8.00 | -13.22 | 5.99 | 2.19 | 9.85 |
| gemma3-12b | 29.43 | 19.24 | 6.02 | -2.02 | -5.89 | 25.38 | 4.71 | 6.12 |
| qwen3-8b | 37.96 | 20.99 | 0.81 | -11.55 | -6.49 | 34.68 | 23.56 | 25.03 |
| qwen35-9b | 50.39 | 17.91 | -6.76 | 7.26 | 29.20 | 23.11 | 15.26 | 11.97 |

## 6. Leverage bands on aligned A (descriptive only — nothing filtered)

| A band (aligned) | n+ / n- | mean A+ / A- | R+ / R- ExcludePost | R+ / R- StrongExcludePost | R+ / R- CounterfactualDeletePost |
|---|---|---|---|---|---|
| (-inf, 0) | 138 / 354 | -13.1 / -31.0 | -26.5 / 1.2 | -22.7 / -3.5 | -18.8 / -5.8 |
| (0, 10) | 227 / 207 | 2.4 / 2.9 | -33.4 / 1.8 | -30.0 / -6.8 | -27.5 / -6.4 |
| (10, 20) | 68 / 61 | 13.1 / 14.1 | -19.6 / 9.1 | -17.7 / 3.6 | -21.0 / 7.5 |
| (20, 30) | 63 / 36 | 23.7 / 24.1 | -12.3 / 22.1 | -15.6 / 12.6 | -12.9 / 11.5 |
| (30, 40) | 54 / 29 | 33.8 / 33.8 | -1.4 / 27.2 | -13.0 / 11.1 | -10.8 / 8.4 |
| (40, inf) | 450 / 313 | 80.3 / 79.6 | 23.5 / 60.1 | 20.4 / 39.8 | 28.1 / 42.6 |

## 7. Reading aid (both outcomes informative — §9)

(a) if the same-claim asymmetry persists (|gap| large relative to |A|), evidence polarity itself affects reversibility; (b) if it largely disappears, P1/G24A's asymmetry was mainly claim prior/form (Account B), not evidence polarity.  Numbers: ExcludePost gap=-24.56, StrongExcludePost gap=-14.45, CounterfactualDeletePost gap=-10.07.

## 8. Caveats

- Temp-0 retest caveat carries over (`g24a_data_quality_audit_v1.md` §E).
- Zero-model validity review applied pre-run (44/200 replacements from frozen reserve order); no model-conditioned selection.
- P1/P2 outcome maps are separate; P1's frozen map is untouched.
- No rationale coding in this round (60-cell §10 reading is a separate P1-based step).
