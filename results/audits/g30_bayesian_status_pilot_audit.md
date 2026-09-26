# G30 Bayesian-status pilot — pre-inference item audit

**Artifact audited:** `data/items/g30_bayesian_status_pilot_v1.jsonl`
**Scope of this document:** mechanical, item-by-item verification of all 40 rows before any model
inference is run. **No model inference was run.** No model outputs, logs, or prior item pools were
read; the only inputs were the brief (`g30_local_data_agent_brief.md`) and the generator/auditor
script written for this task. The agent wrote temporary working files under `/tmp/opencode/`;
the only repository outputs during construction were the two named in the brief. The generator/auditor
source was archived in `scripts/generate_g30_bayesian_status.py` after the audit completed.

**Status: FROZEN — all 40 rows pass all checks.**

**SHA-256 of final JSONL:** `69b2df166a9307ea9fcc4c0e35392b0640ac6db89e13d042040ce735bee59fcb`

---

## 1. What was built

A transparent theory-anchor pilot for evidence admissibility using a binary diagnostic signal.
Rows are produced by an exact deterministic nested loop over the required factorial — no handpicked
or ad hoc examples:

```
for prior in [0.20, 0.35, 0.50, 0.65, 0.80]:        # 5
    for reliability in [0.65, 0.75, 0.85, 0.95]:     # 4
        for e2_report in ["Blue", "Yellow"]:         # 2
            -> one row                                # 5 x 4 x 2 = 40
```

Row schema: `id`, `prior_blue`, `reliability`, `e2_report`, `e1_report`, `bayes_p_blue_after_e2`
(0–1 scale, consistent with `prior_blue`/`reliability`), plus audit-support fields
`bayes_p_blue_after_e2_pct`, `bayes_p_blue_after_e2_fraction` (exact rational),
`final_admissible_set`, `turn_counts`, `e1_target`, `e1_status_at_first_display`, and the four
stimuli `stimulus_D`, `stimulus_N`, `stimulus_I`, `stimulus_R`.

Update rule used (equal sensitivity/specificity):
`P(report=Blue | state=Blue) = reliability`, `P(report=Blue | state=Yellow) = 1 - reliability`.
All probabilities appear as percentages inside the prompts; `bayes_p_blue_after_e2` is never
displayed in any stimulus.

## 2. Checks performed

| # | Check | Method | Result |
|---|-------|--------|--------|
| 1 | Exact factorial coverage (5x4x2) | Set of `(prior, reliability, e2)` tuples compared against the full Cartesian product | PASS — 40/40 cells, no duplicates, no gaps |
| 2 | Exactly 40 rows / unique IDs | Line count after re-reading the frozen file from disk; `len(set(id))` | PASS — 40 lines, 40 unique IDs |
| 3 | E1 always opposite E2 | `e1_report == opposite(e2_report)` for every row | PASS — 40/40 |
| 4 | Prior/reliability values in the required sets | Membership test against `(0.2, 0.35, 0.5, 0.65, 0.8)` and `{0.65,0.75,0.85,0.95}` | PASS — 40/40 |
| 5 | Numeric Bayesian values independently recomputed | **Four independent paths:** (a) float Bayes rule, (b) exact `Fraction` arithmetic vs. stored fraction string, (c) odds form `post-odds = prior-odds x LR`, (d) stored proportion vs. stored percentage consistency | PASS — all four agree to <1e-12 on all 40 rows |
| 6 | No leaked answer in stimuli | Every `%` token in every prompt must be one of exactly the 5 header values; every non-`%` numeric token must be in `{0, 1, 2, 100}`; forbidden-word blacklist (`bayes`, `posterior`, `likelihood`, `odds`, `multiply`, `combine`, `increases`, `decreases`, ...) | PASS — 160/160 stimuli |
| 7 | No prior/reliability mismatch | Regex re-parses `Prior probability ... : N% (Yellow: M%)` and `reliability N%: ... correct N% ... wrong M%` out of each prompt and compares to the row fields | PASS — 160/160 stimuli |
| 8 | N/R/I identical final admissible set | `final_admissible_set` compared across N, I, R (and D); `Final rule:` sentence compared for byte-identity across all four conditions | PASS — all equal `["prior_blue","e2_report"]`, sentence identical |
| 9 | N/I differ in target relevance and no other intended factor | Line-by-line diff: exactly one line may differ, and it must reduce to the substitution `this device` <-> `a separate unrelated device`; task-instruction block and question block compared for identity; turn counts compared | PASS — 1 differing line only, instructions and questions byte-identical, turn counts 2 = 2 |
| 10 | Instruction naturalness / clarity | ASCII-only, no leftover `{ }` placeholders, no double spaces, trimmed, plausible length (500–1400 chars), correct termination on the forced-choice line, identical task instructions across D/N/I/R, identical final-rule and question blocks across D/N/I/R | PASS — 40/40 rows |
| 11 | Structural condition rules | D contains no E1 and no invalidation language; N/I carry `invalid from the moment of display`; R shows E1 as `valid` on turn 1 then revokes it and disclaims state/value/reliability (>=3 `unrelated`) including E2 reliability; all end on the same E2; `An invalid report supplies zero valid information` present in N, I, R | PASS — 160/160 stimuli |
| 12 | Independence statement present | Each prompt states reports' errors are independent | PASS — 160/160 |

## 3. Item-by-item results (all 40 rows)

Every cell below was evaluated mechanically, row by row and condition by condition.

| # | id | prior | rel | E2 | E1 | P(B given E2) % | exact | factorial | unique id | E1 opposite | numeric recompute | D | N | I | R | no leak | N=I pair | admissible set |
|---|----|-------|-----|----|----|-----------------|-------|-----------|-----------|--------------|-------------------|---|---|---|---|---------|----------|----------------|
| 1 | `g30_p020_r065_e2blue` | 0.20 | 0.65 | Blue | Yellow | 31.7073 | 13/41 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 2 | `g30_p020_r065_e2yellow` | 0.20 | 0.65 | Yellow | Blue | 11.8644 | 7/59 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 3 | `g30_p020_r075_e2blue` | 0.20 | 0.75 | Blue | Yellow | 42.8571 | 3/7 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 4 | `g30_p020_r075_e2yellow` | 0.20 | 0.75 | Yellow | Blue | 7.6923 | 1/13 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 5 | `g30_p020_r085_e2blue` | 0.20 | 0.85 | Blue | Yellow | 58.6207 | 17/29 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 6 | `g30_p020_r085_e2yellow` | 0.20 | 0.85 | Yellow | Blue | 4.2254 | 3/71 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 7 | `g30_p020_r095_e2blue` | 0.20 | 0.95 | Blue | Yellow | 82.6087 | 19/23 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 8 | `g30_p020_r095_e2yellow` | 0.20 | 0.95 | Yellow | Blue | 1.2987 | 1/77 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 9 | `g30_p035_r065_e2blue` | 0.35 | 0.65 | Blue | Yellow | 50.0000 | 1/2 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 10 | `g30_p035_r065_e2yellow` | 0.35 | 0.65 | Yellow | Blue | 22.4771 | 49/218 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 11 | `g30_p035_r075_e2blue` | 0.35 | 0.75 | Blue | Yellow | 61.7647 | 21/34 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 12 | `g30_p035_r075_e2yellow` | 0.35 | 0.75 | Yellow | Blue | 15.2174 | 7/46 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 13 | `g30_p035_r085_e2blue` | 0.35 | 0.85 | Blue | Yellow | 75.3165 | 119/158 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 14 | `g30_p035_r085_e2yellow` | 0.35 | 0.85 | Yellow | Blue | 8.6777 | 21/242 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 15 | `g30_p035_r095_e2blue` | 0.35 | 0.95 | Blue | Yellow | 91.0959 | 133/146 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 16 | `g30_p035_r095_e2yellow` | 0.35 | 0.95 | Yellow | Blue | 2.7559 | 7/254 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 17 | `g30_p050_r065_e2blue` | 0.50 | 0.65 | Blue | Yellow | 65.0000 | 13/20 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 18 | `g30_p050_r065_e2yellow` | 0.50 | 0.65 | Yellow | Blue | 35.0000 | 7/20 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 19 | `g30_p050_r075_e2blue` | 0.50 | 0.75 | Blue | Yellow | 75.0000 | 3/4 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 20 | `g30_p050_r075_e2yellow` | 0.50 | 0.75 | Yellow | Blue | 25.0000 | 1/4 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 21 | `g30_p050_r085_e2blue` | 0.50 | 0.85 | Blue | Yellow | 85.0000 | 17/20 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 22 | `g30_p050_r085_e2yellow` | 0.50 | 0.85 | Yellow | Blue | 15.0000 | 3/20 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 23 | `g30_p050_r095_e2blue` | 0.50 | 0.95 | Blue | Yellow | 95.0000 | 19/20 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 24 | `g30_p050_r095_e2yellow` | 0.50 | 0.95 | Yellow | Blue | 5.0000 | 1/20 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 25 | `g30_p065_r065_e2blue` | 0.65 | 0.65 | Blue | Yellow | 77.5229 | 169/218 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 26 | `g30_p065_r065_e2yellow` | 0.65 | 0.65 | Yellow | Blue | 50.0000 | 1/2 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 27 | `g30_p065_r075_e2blue` | 0.65 | 0.75 | Blue | Yellow | 84.7826 | 39/46 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 28 | `g30_p065_r075_e2yellow` | 0.65 | 0.75 | Yellow | Blue | 38.2353 | 13/34 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 29 | `g30_p065_r085_e2blue` | 0.65 | 0.85 | Blue | Yellow | 91.3223 | 221/242 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 30 | `g30_p065_r085_e2yellow` | 0.65 | 0.85 | Yellow | Blue | 24.6835 | 39/158 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 31 | `g30_p065_r095_e2blue` | 0.65 | 0.95 | Blue | Yellow | 97.2441 | 247/254 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 32 | `g30_p065_r095_e2yellow` | 0.65 | 0.95 | Yellow | Blue | 8.9041 | 13/146 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 33 | `g30_p080_r065_e2blue` | 0.80 | 0.65 | Blue | Yellow | 88.1356 | 52/59 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 34 | `g30_p080_r065_e2yellow` | 0.80 | 0.65 | Yellow | Blue | 68.2927 | 28/41 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 35 | `g30_p080_r075_e2blue` | 0.80 | 0.75 | Blue | Yellow | 92.3077 | 12/13 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 36 | `g30_p080_r075_e2yellow` | 0.80 | 0.75 | Yellow | Blue | 57.1429 | 4/7 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 37 | `g30_p080_r085_e2blue` | 0.80 | 0.85 | Blue | Yellow | 95.7746 | 68/71 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 38 | `g30_p080_r085_e2yellow` | 0.80 | 0.85 | Yellow | Blue | 41.3793 | 12/29 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 39 | `g30_p080_r095_e2blue` | 0.80 | 0.95 | Blue | Yellow | 98.7013 | 76/77 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |
| 40 | `g30_p080_r095_e2yellow` | 0.80 | 0.95 | Yellow | Blue | 17.3913 | 4/23 | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK | OK |

## 4. Flaws found and fixed (before freezing)

The audit was run repeatedly; defects it surfaced are recorded here rather than silently discarded.

| Flaw | Class | Fix |
|------|-------|-----|
| Reliability sentence `matches ... with reliability 65%, meaning it is correct 65% of the time` did not state that accuracy is equal for Blue and Yellow devices, leaving the equal-sensitivity/specificity assumption implicit. | Stimulus clarity | Reworded to `reliability 65%: whether the device is Blue or Yellow, the report is correct 65% of the time and wrong 35% of the time`. |
| R's revocation line read `Report E1 supplies zero valid information`, not matching the N/I generic formulation. | Cross-condition wording | Reworded to `Report E1 is now invalid; an invalid report supplies zero valid information; do not use it.` so N, I and R all contain the same generic sentence. |
| Auditor's bare-number regex backtracked inside `20%` and reported spurious numbers. | Audit tooling | Anchored look-arounds with `[0-9%]` so digit runs cannot be split. |
| Auditor indexed R's turn-1 line by a hard-coded offset. | Audit tooling | Located the line by its `Turn 1 - ` prefix. |
| Auditor expected R to repeat the E1 colour twice; R names the colour once and then refers to `report E1` by label, which is unambiguous. | Audit expectation (item was correct) | Expectation corrected to a single colour mention; R text left as-is. |
| Odds-form cross-check used `LR = reliability` instead of `LR = reliability / (1 - reliability)` and flagged 20 correct rows. | Audit tooling | Corrected the LR; the check is what independently validated the other three paths. |

No defect remained in the frozen file: the final run reports `rows_with_failures = 0`.

## 5. Observations recorded (not defects)

- **Prior = 0.50 rows (8 of 40).** When the prior is 50%, the posterior equals the reliability
  (E2 = Blue) or its complement (E2 = Yellow), so for rows 17–24 the correct answer coincides with a
  number that already appears in the header. This is an arithmetic identity, not a leak: the value
  is present only in its reliability/complement role, no sentence associates it with the answer, and
  the leak check (#6) still passes because the token count and positions are unchanged. It is
  recorded because a reader should know these 8 items are easier to guess for a reason external to
  the intended behavioral contrast.
- **Two rows share posterior 1/2** (row 9: prior 0.35 / rel 0.65 / E2 Blue, and row 26: prior 0.65 /
  rel 0.65 / E2 Yellow). Coincidental across distinct factorial cells; IDs and stimuli remain unique.
- **Turn counts:** D = 1 turn (it shows only E2, as specified); N = I = R = 2 turns. N/I turn counts
  are matched as required; D is intentionally shorter by design, not by accident.
- **Posterior range:** 1.2987% to 98.7013% — no item is at or near a 0/100 floor or ceiling.

## 6. Condition structure summary

| | D | N | I | R |
|---|---|---|---|---|
| Turn count | 1 | 2 | 2 | 2 |
| E1 shown | no | yes | yes | yes |
| E1 target | — | this device | separate unrelated device | this device |
| E1 status at first display | — | invalid | invalid | valid, then revoked |
| Revocation rationale | — | — | — | procedural random audit, unrelated to device state, report value, and report reliability (incl. E2) |
| Final admissible set | prior + E2 | prior + E2 | prior + E2 | prior + E2 |
| Closing report | E2 | E2 | E2 | E2 |
| Task instructions / question block | identical across all four conditions |||

## 7. Caveat

This task is **constructed**. It is a theory anchor for evidence admissibility, not a natural
evidence-use case, and it tests **transfer of the behavioral distinction** between information that
is invalid at the moment it appears, information later revoked, information about an irrelevant
target, and information never shown at all. Real-world evidence status is rarely this clean:
adjudications are usually contested, revocations are rarely declared as procedural with the report
still visible, and "invalid from the moment of display" is a legal-fiction idealisation. Results
from this pilot should therefore be read as evidence about how a binary-status distinction is
handled under a controlled prompt, **not** as independent confirmation of any substantive claim
about VitaminC or any other real-world evidence base, and not as a new natural-language benchmark.
No model inference has been run at the time of freezing; the numeric values in §3 are the analytic
answers computed from the generative model, not observed model behaviour.
