# G30: a formal probability anchor changes the account

Date: 2026-09-27. Exploratory follow-up after G29/G29B. See the [pre-inference registration](../discovery/g30_bayesian_status_registration.md), [local OpenCode construction brief](../discovery/g30_local_data_agent_brief.md), [item-by-item audit](../audits/g30_bayesian_status_pilot_audit.md), [full analysis](g30_bayesian_status_analysis_v1.md), its JSON companion, and the [checksummed manifest](g30_manifest_v1.json). The frozen 40-case data SHA-256 is `69b2df166a9307ea9fcc4c0e35392b0640ac6db89e13d042040ce735bee59fcb`. All 480 outputs from Qwen3-8B, Gemma-3-12B, and Mistral-Small-24B parsed; no case was dropped. The generator/auditor written by local OpenCode is archived in `scripts/generate_g30_bayesian_status.py`.

## Why this pilot matters

G29B found that a semantically relevant but never-admissible contradictory sentence changes later 0–9 truth ratings relative to a similarly excluded irrelevant sentence. That result could depend on natural Wikipedia revision semantics or on the rating task. G30 asks the same admissibility question in a different inferential environment: a prior over Blue/Yellow, a diagnostic report with stated reliability, a single final admissible report E2, and an exact Bayesian posterior. The final response is an explicit probability forecast and a Blue/Yellow decision. The 40 cells are the complete factorial of five priors, four reliabilities, and two E2 directions. This is a controlled anchor, not a natural dataset or a new benchmark.

## Main observations

| Contrast, pooled across three models | Result | Reading |
|---|---:|---|
| Never-admissible relevant E1 **N** minus never-admissible irrelevant E1 **I**, signed toward E1 | +0.16 pp [−1.18,+1.57] | No common directional content effect in probability forecasts |
| Absolute N−I probability difference | 3.91 pp [2.44,5.69] | Some case-specific sensitivity remains |
| N/I direct-choice disagreement | 4% [1%,7%] | Decision changes are uncommon here |
| Initially valid then revoked **R** minus N, signed toward E1 | +6.38 pp [4.67,8.05] | Clear pooled movement toward old E1, mainly Gemma |
| Bayesian absolute error, D / I / N / R | 7.49 / 8.69 / 10.05 / 14.20 pp | R has the largest error; paired R−N = +4.15 pp [2.45,5.82] |

The pooled N−I near-zero is genuinely heterogeneous: Qwen −2.55 pp, Gemma +4.13 pp, and Mistral −1.10 pp. It **does not reproduce G29B's common negative N−I direction**. Even the formal task is not perfectly content-invariant item by item, but this is far below G29B's 14% N/I direct-choice disagreement, and the current direct choice effect has no shared polarity.

R−N also varies sharply: Qwen −0.71 pp [−5.31,+2.65], Gemma +15.86 pp [12.74,18.99], Mistral +3.98 pp [2.52,5.53]. Gemma's R responses often fall back toward the prior. Its uptake of the final **valid** E2, measured as mean P(Blue) after Blue E2 minus after Yellow E2 at matched prior/reliability, falls from 49.72 pp in N to 18.00 pp in R; D is 53.08 pp. Pooled E2 separation falls from 51.18 pp in N to 38.43 pp in R. The signed R−N contrast is therefore better described as **weakened use of E2 after a revoked report** in this task than as direct reuse of E1. Qwen has one large outlying R/N pair (N=100, R=25 for a 5% Bayesian posterior); it remains in every estimate.

## What changed in our explanation

The results resist a single simple rule. Natural same-claim evidence in G29 showed R≈N, while N differed from I on graded ratings, with stronger uptake of contradictory E2 in N. Here, with a formal probability model and a verbal probability outcome, N≈I on the signed aggregate, while R differs from N, with weaker E2 uptake especially in Gemma. Thus neither “revocation status is always irrelevant” nor “excluded contradictory content always causes contrast enhancement” survives transfer unchanged.

A stronger question is now **how exclusion changes the integration of still-valid evidence**. ConfB demonstrated that direct polarity suppression does not restore the never-seen judgment. G29B and G30 show two possible residual patterns: amplification of later valid evidence after never-admissible contradictory natural content, and attenuation of later valid evidence after a revoked formal signal. This suggests a family of *admissibility–integration interactions*, rather than a single signed history effect. It is a behavioral synthesis and hypothesis, not a demonstrated universal law or internal mechanism.

The formal pilot has a clear limitation: its “Turn 1 / Turn 2” histories are **rendered in one user message**, rather than executed as a multi-turn chat. R is also longer than N because the random revocation is spelled out. The R−N contrast therefore cannot yet be attributed uniquely to a revocation event rather than the processing cost or framing of the longer history. The 40 cells are a designed grid, not independent natural examples. Verbalized probability remains an elicited number, albeit one with a normative answer and ordinary forecasting semantics. Mistral's existing tokenizer emits a known regex warning; this run used the same checkpoint/environment family as G29 and retained all its rows.

## Research decision

Keep the confirmed ConfB suppression–restoration gap as the empirical center. Treat G29B's “never-admissible content modulates later evidence use” as a natural-evidence candidate with model heterogeneity. G30 does **not** confirm that direction; it supplies a useful boundary and a normative decomposition. Do not rename the project around a generic status-independent content effect, nor claim a universal retraction-status effect from this constructed pilot.

The most valuable next experiment is a **fresh natural probability-forecast task** with genuinely relevant and irrelevant excluded material, an explicit final admissible set, and a natural scoring interpretation. It should test *E2 uptake* and same-item restoration alongside the forecast, rather than add more wording on VitaminC. A small multi-turn variant of G30 is useful only if we want to elevate its R−N result; it is not required to establish the ConfB core.

Relevant prior: [Gonçalves et al.](https://academic.oup.com/restud/article/93/1/476/8159675) already use a never-observed comparator and examine later updating in humans; [Kumaran et al.](https://www.nature.com/articles/s42256-026-01217-9) already show LLM overweighting of opposing advice; [Jang et al.](https://arxiv.org/abs/2602.18505) and [Unlearning as Distribution Restoration](https://arxiv.org/abs/2607.19442) already distinguish suppression from a stronger restoration/deletion criterion in other settings. Our proposed contribution must stay specific to in-context evidence admissibility, paired same-item judgments, and effects on later valid evidence integration.
