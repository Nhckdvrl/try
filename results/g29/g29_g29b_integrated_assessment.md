# Fresh revocation-status and excluded-content experiments: integrated assessment

Date: 2026-09-27. Read [G29 registration](../discovery/g29_revocation_status_registration.md), [G29B registration](../discovery/g29b_excluded_content_registration.md), [blind material audit](../audits/g29_material_audit_v1.md), [irrelevant-control audit](../audits/g29b_irrelevance_audit_v1.md), [full G29 analysis](g29_revocation_analysis_v1.md), [full G29B analysis](g29b_excluded_content_analysis_v1.md), and [checksummed manifest](g29_manifest_v1.json). G29B was registered after seeing G29 and is explicitly exploratory. The ConfB suppression–restoration result remains a separate held-out confirmation.

The two readouts side by side: [figure (PNG)](../../figures/g29_status_content_v1.png), [publication-ready PDF](../../figures/g29_status_content_v1.pdf).

## What was tested

The source is pinned VitaminC natural Wikipedia revisions, but item text quality was screened before inference. A deterministic, case/claim-disjoint shortlist of 160 new same-claim support/refute pairs was blind-reviewed **item by item** using local OpenCode free models. Of 160, 98 passed audited semantic validity, source-role agreement, and naturalness; the first 80 in seed order were frozen. MiMo v2.6 Flash completed six batches, Longcat 2.5 Preview two after a MiMo stall. Longcat's incomplete explanatory fields were filled by a blind follow-up before freeze. This is LLM-assisted audit, not human gold. G29B's 80 irrelevant source sentences were selected with a separate zero-lexical-overlap screen and independent blind audit; all 80 targets remained.

For each claim, E1 is the revision opposite to final valid evidence E2. The model sees the same E1 and E2 under three status histories: **R**, E1 initially admissible then revoked; **N**, identical E1 already inadmissible from first display; **A**, E1 remains admissible. **D** receives only E2. G29B adds **I**, a natural irrelevant E1 that is never admissible; I and N have identical three-turn format, status instructions, fixed acknowledgment, final E2, and output task. Each condition is measured with a separate direct TRUE/FALSE prompt and 0–9 rating prompt. Three models completed all 80 pairs in both E2 directions: Mistral-Small-24B, Qwen3-8B, Gemma-3-12B. G29 has 3,840 output rows and G29B adds 960. Every binary/rating answer parses, all digit mass is ≥0.5, and no R/N/I rationale is truncated. Two Mistral A-reference rationales reached the 110-token cap; all rows remain included.

Mistral sometimes appended a period to its binary `ANSWER` line (189/640 G29 and 36/160 G29B binary rows). The parser accepts `ANSWER: TRUE.` / `ANSWER: FALSE.` as the same direct decision; no binary response contained an additional rationale or ambiguous choice.

## Decisive contrast 1: revocation status has little coherent directional effect

R and N expose the model to the **same contradictory E1** and end with the **same admissible `{C,E2}`**. The status history differs.

| Paired R−N, three models × 80 claims × 2 E2 directions | Estimate [95% claim-bootstrap CI] |
|---|---:|
| Signed TRUE/FALSE contrast, aligned to old E1 | +0.021 [−0.002,+0.044] |
| Direct decisions differ between R and N | 6.2% [4.0%,8.7%] |
| Signed 0–100 rating contrast, aligned to old E1 | +1.40 [−0.40,+3.26] |
| Absolute rating difference | 5.08 [3.53,6.80] |

The predicted G28-like negative R−N contrast does **not** appear. There are 30 discordant binary cells among 480: in 10, R chooses the E2-implied answer and N does not; in 20, N chooses E2 and R does not. Thus the status wording/history does affect some items, but it does not support a robust revocation-specific *contrast enhancement* law. A simple equivalence claim would also overstate the result. Active E1 makes a large difference: E2-aligned decisions are 62.5% in A versus 78.3% in R and 80.4% in N, and E2 rating separation is 12.09 in A versus 73.13/75.93 in R/N. The models respond to the admissibility instruction, even while R−N is small on directional aggregates.

## Decisive contrast 2: inadmissible content still shapes later graded judgments

N and I are both **never-admissible** histories. Their only prompt difference is the old E1 sentence: N shows same-claim contradictory evidence, I shows an audited irrelevant natural sentence. Both end with `{C,E2}`.

| Paired N−I, same three models and 80 claims | Estimate [95% claim-bootstrap CI] |
|---|---:|
| Signed 0–100 rating contrast, aligned to old E1 | **−5.68 [−8.37,−3.15]** |
| Increase in E2 rating separation in N versus I | **+11.35 [6.31,16.73]** |
| Absolute rating difference | 11.49 [8.92,14.25] |
| Direct TRUE/FALSE decisions differ | 14.0% [11.0%,17.1%] |
| Signed binary contrast, aligned to old E1 | −0.010 [−0.048,+0.027] |

The graded contrast is concentrated on refuting E2: N−I signed rating −7.45 [−10.79,−4.28] versus −3.91 [−8.64,+0.42] for supporting E2. Qwen3-8B (−9.03) and Gemma-3-12B (−7.41) show clear negative pooled rating contrasts; Mistral-Small-24B is near zero (−0.59). This is a **two-of-three-model graded pattern**, not a uniform law. The direct decisions are content-sensitive item by item (67 of 480 N/I cells differ), but flips have no shared direction: 36 cells choose E2 only in N, 31 only in I. The binary evidence supports consequential instance-level sensitivity, not directional overcorrection on choices.

## Revised scientific interpretation

G28A/B showed apparent overcorrection after revoked contradictory E1. G29 now shows that *revocation is not necessary* for the graded contrast in this fresh setting: N, where the same E1 was declared inadmissible immediately, behaves similarly to R; N still differs from matched irrelevant I in a direction consistent with enhanced E2 separation. This supports a **status-independent exposure account for graded evidence use**, within these prompts and sources. It does not establish that the same process explains every part of G28; G28 used a different item set and protocol, and Mistral's fresh N−I contrast is weak.

The paper's established center remains the **suppression–restoration gap** in ConfB. G29/G29B add a useful second layer: formal admissibility can strongly gate a conflicting old evidence item (A versus R/N), yet previously displayed *inadmissible* content can still alter the weighting of later valid evidence (N versus I), especially graded confidence. This gives a natural two-stage account of why behavioral forgetting metrics need a same-item counterfactual: success at suppressing a disallowed item's overt polarity is not a guarantee that downstream judgment uses only the admissible evidence set. The latter sentence is a behavioral interpretation, not an internal-state mechanism.

The novelty boundary needs care. [Kumaran et al. 2026](https://doi.org/10.1038/s42256-026-01217-9) already document overweighting of *opposing advice*, so generic contrast enhancement alone is not ours. G29B's additional question is whether even **explicitly never-admissible contradictory content** changes later judgments relative to matched excluded irrelevant content. [ReviseQA](https://openreview.net/pdf?id=Z4KBiAYXlI) and [Breaking Contextual Inertia](https://aclanthology.org/2026.findings-acl.313/) cover dynamic fact/rule removal and earlier reasoning traces. More importantly, the *never-observed counterfactual* itself is **not a new concept**: [Gonçalves et al., Review of Economic Studies 2026](https://academic.oup.com/restud/article/93/1/476/8159675) test it in human belief-updating experiments and also study new evidence after retraction. Our candidate contribution must be specific to LLM in-context natural evidence: the **suppression-versus-restoration evaluation split**, the scale and structure of the gap, and the status/content decomposition here. We should not claim first invention of counterfactual restoration or history dependence.

## What would raise or lower the paper ceiling

The behavioral/evaluation story is clearer than before, but G29B does not yet justify a broad decision-level overcorrection claim. The next valuable test, if pursued, should target a domain where a *graded* change itself has natural consequences (e.g., ranking evidence, confidence-sensitive recommendation, or selective review), or test whether the N−I contrast generalizes beyond VitaminC revision pairs and this output format. More prompt variants or internal patching on the current 80 would add less insight. A future multi-domain test should keep the same final admissible set and audited irrelevant-content match; otherwise it would regress to generic correction benchmarks.
