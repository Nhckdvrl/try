# G24A §10 matched qualitative reading — behavioral labels (v1)

Round run per registration §10 (`results/discovery/g24a_competing_accounts_v1.md`), zero
gate, descriptively read against the frozen spec. Labels are **behavioral description
only — explicitly not mechanism**. Single question the round was designed to answer:
**why does the claim drop below its own Base after support evidence is retracted?**

## 1. Protocol

- **Sample** (mechanical, `scripts/sample_g24a_p1_qual_cells.py`, seed 20260927 applied
  per draw as `Random("20260927:<model>:<stratum>")` over group_sha-sorted candidates):
  three strata on the increase-side trajectory of each (model, group) cell, thresholds
  frozen pre-reading, first match wins — overshoot `R_CF <= -10`; exclude-bad-improved
  `R_Exc <= -15 and R_Strong >= R_Exc + 10 and R_CF >= R_Exc + 10`; near-base
  `|R_CF| <= 5`. Frame = 480 cells → overshoot 293, exclude-bad-improved 60,
  near-base 53, ineligible 74.
- **Draw**: 4/stratum/model with all-available-if-<4 and shortfalls reported (§10).
  Final = **53 cells** (shortfalls: mistral/near-base 3, llama/excl 3, llama/near-base 3,
  gemma/excl 1, qwen3/excl 3) × both claims × 5 conditions = **530 rationale readings**
  (spec anticipated 600 at 60 cells). Sampling + reading material: commit `99b66e7`
  (`data/items/g24a_p1_qual_cells_v1.jsonl`, `results/g24a/g24a_p1_qual_review_v1.md`).
- **Reading**: every rationale read line-by-line from the review file; one label per
  rationale from the frozen six-label vocabulary, assigned by the stated basis of the
  rating (not by the numeric value; numbers were read only as recorded context):
  - `still_uses_evidence` (UE) — the rationale rests on E's content/direction, including
    verbatim reproduction of E under Exclude/Strong/CF.
  - `no_evidence=>uncertain` (UN) — stated basis is inability to know without E
    ("cannot determine/verify/assess", suspension language, near-neutral mapping).
  - `no_evidence=>claim_less_likely` (CL) — absence of support is given as a reason the
    claim is unlikely/false (penalization wording: "unsubstantiated", "no reason to
    believe", "rate 0/low as there is no evidence").
  - `exclusion_implies_distrust` (ED) — the exclusion ruling itself is used as a reason
    to distrust the claim or the material.
  - `reconstructs_prior/world_knowledge` (RK) — judgment carried by prior/world
    knowledge, external literature, or explicit knowledge-fallback after setting E aside.
  - `other` (OT) — task-confused or claim-internal-plausibility text that fits none.
  - Tie-breaks applied uniformly: explicit conclusion/limitation clause decides;
    a limitation on truth/certainty → UN, a limitation on extent/quantification with
    truth asserted → RK; absence as the *sole* stated reason for a low rating → CL,
    absence alongside substantive knowledge → RK; recital of E followed by an explicit
    suspension conclusion → UN, recital with E's direction operative → UE.
  - Base rationales (no E in prompt) labeled by the same vocabulary; Admit+use-E = UE
    even though admissible there (behavioral description, not norm judgment).
- **Validity**: weak-but-direction-correct readings kept with a note; no replacements
  needed (no direction errors, broken texts, or bearing failures among the 530; two
  `other` readings are odd-but-intact outputs, kept and flagged).

## 2. Coverage and totals

Cells: mistral 11 (4/4/3), llama31-8b 10 (4/3/3), gemma3-12b 9 (4/1/4),
qwen3-8b 11 (4/3/4), qwen35-9b 12 (4/4/4) — overshoot/exclude-bad/near-base.
Labels: 530, unique keys 530, 10 per cell, vocabulary clean.

Pooled label totals (530):

| label | n | share |
|---|---:|---:|
| reconstructs_prior/world_knowledge | 203 | 38.3% |
| no_evidence=>uncertain | 158 | 29.8% |
| still_uses_evidence | 148 | 28.3% |
| no_evidence=>claim_less_likely | 19 | 3.6% |
| exclusion_implies_distrust | 0 | 0% |
| other | 2 | 0.4% |

By condition (both polarities pooled; n=106 per condition):

| condition | UE | UN | CL | RK | OT |
|---|---:|---:|---:|---:|---:|
| base | – | 22 | 2 | 81 | 1 |
| admit_post | 103 | – | – | 3 | – |
| exclude_post | 34 | 43 | 5 | 24 | – |
| strong_exclude_post | 7 | 53 | 2 | 44 | – |
| counterfactual_delete_post | 4 | 40 | 10 | 51 | 1 |

## 3. Diagnostic payoff — the §10 question

§10's hypothesis pattern ("without E supporting, the claim is less likely" ⇒
`remove support ⇒ penalize claim`) is the CL label. **Increase-side, by stratum,
Exclude / Strong / CF:**

| stratum | condition | UE | UN | CL | RK |
|---|---|---:|---:|---:|---:|
| overshoot | exclude | 6 | 9 | 1 | 4 |
| overshoot | strong | 0 | 13 | 1 | 6 |
| overshoot | **CF** | 0 | **9** | **3** | **8** |
| exclude-bad-improved | exclude | 1 | 12 | 2 | 0 |
| exclude-bad-improved | strong | 0 | 8 | 1 | 6 |
| exclude-bad-improved | CF | 1 | 6 | 1 | 7 |
| near-base | exclude | 4 | 7 | 0 | 7 |
| near-base | strong | 1 | 9 | 0 | 8 |
| near-base | **CF** | 1 | **6** | **1** | **11** |

Three descriptive observations, no inferential claims:

1. **Articulated penalization is rare.** In the overshoot stratum's CF readings
   (the exact cells where Y_CF < Y0), only 3/20 rationales verbally execute
   remove-support⇒penalize; 9/20 verbalize suspension (UN), 8/20 reconstruct from
   prior knowledge (RK). Pooled across all 530 readings, CL = 19 (3.6%), and those
   concentrate in two models: llama31-8b 9/19, qwen3-8b 6/19.
   CL examples (verbatim):
   - llama31-8b 01df2d47f2, overshoot, inc CF: "Without any information, I would rate
     the likelihood of the claim being true as 0, as there is no evidence to support
     the existence of a ship called Mirny in the Russian Empire's navy."
   - qwen3-8b fd26d2a715, overshoot, inc CF: "Before encountering Evidence E, the claim
     … lacks direct support from known biological mechanisms or prior epidemiological
     data. The claim introduces a specific hypothesis that has not been previously
     established in the absence of this evidence."
   - llama31-8b f360f8b694, overshoot, inc Strong: "There is no information provided to
     support the claim, and the inadmissible evidence does not provide any relevant
     information. The claim appears to be unsubstantiated."

2. **Prose–number divergence: the displacement is usually not articulated.** Several
   overshoot readings *say* suspension while the recorded number plunges far below
   Base — e.g. qwen35-9b 87f335a320 inc Exclude ("…removing the only provided data
   supporting the claim. Without this evidence or any other supporting information, the
   claim cannot be verified as true." — Y 99.2 → 2.7); mistral e66817f338 inc Exclude
   ("without direct evidence linking ART to reduced infectiveness, it is difficult to
   assess the claim's validity." — Y 88.5 → 30.3); qwen3-8b a1314c14e5 inc Exclude
   ("The claim is directly stated in the evidence, which is excluded. Therefore, the
   claim's truth value cannot be determined…" — Y 100.0 → 0.0). The verbalized policy
   at Exclude is overwhelmingly "cannot determine", yet the number moves as if the
   evidence still counted against the claim. Conversely, `still_uses_evidence` rationales
   under Exclude (34/106) usually explain *upward* or *direction-faithful* movement
   (e.g. llama 01df2d47f2 dec Exclude: "Evidence E clearly states that it was a ship of
   the Imperial Russian Navy, there is a clear contradiction" — Y 7.1 → 1.8).

3. **Near-base recovery runs through prior-knowledge reconstruction, not through
   suspension.** Near-base CF readings are RK 11/20 with UN 6/20; overshoot CF readings
   are UN 9/20 with RK 8/20. Cells that return to their own Base typically re-anchor on
   world knowledge ("Based on general knowledge … commonly known as a geographical
   location, not a type of landform" — qwen3-8b b05287b62f inc CF, Y 0.2 → 0.1;
   "…a well-established medical fact supported by extensive prior research…" —
   qwen35-9b 62a595ceec inc CF, Y 98.3 → 96.8). Cells that overshoot mostly fail to
   produce that re-anchor: they suspend in prose while the number drifts down.

## 4. Evidence attrition gradient (UE outside Admit)

Explicit quotation/reliance on E when the ruling forbids its use, by condition
(denominator 106 each):

- exclude_post: **34/106 (32%)** — the exclusion ruling still leaves E as the
  rationale's working material in a third of readings ("The evidence explicitly states
  that Trollhunters was created by Guillermo del Toro, a person. Therefore …" —
  gemma 3ac4b52efa inc Exclude, Y = 100.0).
- strong_exclude_post: 7/106 (7%).
- counterfactual_delete_post: **4/106 (4%)** — strongest instructions drive explicit
  E-use near zero, but not to zero: e.g. qwen3-8b f360f8b694 dec CF still recites E's
  distinctive content after deletion ("the film features female actors such as Holly
  Hunter and Audrey Hepburn" — E's cast list verbatim; Y 0.0 → 0.0), and qwen35-9b
  af4a78996c inc CF asserts "The claim is directly supported by the evidence stating
  that PKG-I plays an essential role…" (Y 90.9 → 98.6).

## 5. Null / flagged findings

- **`exclusion_implies_distrust` = 0/530.** No rationale treats the exclusion ruling
  itself as evidence of a problem with the claim or the material (no "since it was
  excluded, I'm suspicious of it" moves anywhere in the sample).
- **`other` = 2/530**: llama f360f8b694 inc Base (prompt-echo/entity confusion; kept
  per weak-but-intact rule) and qwen35-9b af4a78996c dec CF (rating explicitly deferred
  to "the claim's internal plausibility" — no vocabulary label fits).
- **Admit is uniformly UE (103/106)** with 3 RK readings that ignore E entirely —
  Admit-use is behaviorally clean.
- Per-model texture (descriptive): llama31-8b and qwen3-8b produce all the explicit
  penalization prose (15/19 CL); qwen35-9b and gemma3-12b almost never do; mistral
  mixes UN/RK.

## 6. Caveats carried

- Single label per rationale forces a primary label on genuinely mixed texts; tie-break
  rules (§1) were applied uniformly and are reproducible from the review file.
- Labels describe rationale prose, not numeric behavior; where they disagree (§3.2) the
  disagreement is itself the finding and is reported, not resolved.
- Behavioral description only — no mechanism claims; no selection, no gates, no
  p-values; 53 < 60 cells only from reported stratum shortfalls.
- Reading round covers P1 rationales only (frozen P1 outcome map untouched); P2 numbers
  referenced nowhere in label assignment.
