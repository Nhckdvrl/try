# G30: A diagnostic-signal anchor for admissibility versus influence

Registered 2026-09-27 before G30 model inference. Exploratory theory-anchor pilot motivated by Gonçalves, Libgober, and Willis (2026), not an independent natural-evidence confirmation. G29/G29B and their model-specific results are already known. Data construction and the row-by-row audit are delegated to local OpenCode from [the frozen brief](g30_local_data_agent_brief.md); model inference waits for completed, hashed items.

## Question

Does the G29B dissociation occur when the judgment is an ordinary probability forecast over a state with a known Bayesian answer, instead of a 0–9 truth rating about a Wikipedia claim? The synthetic design deliberately removes prior factual knowledge and ambiguity about evidence strength. A null effect here would narrow our interpretation of G29B to natural semantic evidence or its rating protocol, rather than invalidate ConfB.

## Conditions and target

Forty factorial cases vary P(Blue), report reliability, and the final valid report E2. E1 always reports the opposite state. Conditions: **D** only E2; **N** same-device E1 explicitly invalid from first display; **I** same-format E1 about an unrelated device, also invalid from first display; **R** same-device E1 initially valid and later randomly revoked. N/I/R end with identical admissible information: prior plus E2. Invalidation is stipulated independent of the state and report value. The Bayesian target is therefore the same in every condition of a case.

Three already-used model snapshots: Mistral-Small-24B, Qwen3-8B, Gemma-3-12B. Separate deterministic calls per condition. Obtain an explicit 0–100 probability of Blue and a forced Blue/Yellow choice, without a preceding rationale. Keep prompts and raw text in every row. This directly tests a meaningful probability forecast, while acknowledging verbalized probability is still an elicited number.

## Frozen comparisons

Primary descriptive contrasts are paired N−I probability difference signed toward the content of E1, its absolute magnitude, and direct choice disagreement. Report each model and E2 direction. Compare R−N the same way to test whether status history adds to mere exposure. Compare D, N, I, R to the Bayesian posterior using absolute forecast error, and report between-condition differences in absolute error. Do not select cases by model response, posterior extremity, parse success, or G29 behavior. Report all parsing failures as failures; no silent drops. Use case-cluster bootstrap intervals over the 40 cases as descriptive uncertainty, with the factorial structure and small N stated.

Possible outcomes: N≠I with R≈N supports status-independent semantic exposure in this formal setting; N≈I with R≠N points to revocation-status processing; all three equal suggests the natural-language G29B effect requires richer semantic evidence or its response protocol. No direction is precommitted for N−I: residual pull toward E1 and contrast enhancement away from E1 are both scientifically informative. The pilot is not a test of a neural mechanism.
