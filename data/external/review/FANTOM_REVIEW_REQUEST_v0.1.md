# FANToM perspective v0.1 — human review request

**Do not run models.** The full source text and four-cell JSONL are committed evaluation artifacts. Review them at:

- `data/external/review/fantom_perspective_pilot_v0.1.md`
- `data/external/review/fantom_perspective_pilot_v0.1.jsonl`

Source attribution: Kim et al., *FANToM: A Benchmark for Stress-testing Machine Theory of Mind in Interactions* (EMNLP 2023), official repository revision `1cae6fa30f5ba04ca0fff5f5716b5ba7055e2e85` under MIT. These prompts are a project-authored evaluation transformation, not an original FANToM score reproduction.

## Decision A — transformation contract

- Decision: `[x] PASS  [ ] FAIL  [ ] UNSURE`
- Reason: PASS. The transformation keeps one source first-order inaccessible belief question, both source-authored belief candidates, candidate order, and the 0–100 readout fixed across all four cells. `OOB_WITH` exposes the exact fact packet only as an evaluator annotation that the target never receives; `ALLOWED_WITH` counterfactually briefs the target with that same packet after the source conversation. The no-packet cells define the matching unbriefed target state. This is a legitimate source-anchored causal perspective intervention rather than an untouched FANToM benchmark score. The registered adapter reconstructs the complete candidate from the pinned source row and rejects any object-level drift; packet-once / packet-absent checks fail closed on leakage.

Verify:

- [x] The same first-order belief question and two source answer candidates remain fixed in all four cells.
- [x] `OOB_WITH` makes the fact visible only to the evaluator; the target character never receives it.
- [x] `ALLOWED_WITH` explicitly tells the exact same packet to the target after the conversation.
- [x] The no-packet cells define the corresponding unbriefed target state coherently.
- [x] Asking for probability of the truth-belief candidate supports the registered responsiveness/intrusion contrasts.
- [x] The allowed post-conversation briefing is a legitimate perspective information-set intervention, not an unacceptable change of task semantics.
- [x] The design is described as a source-anchored causal transformation, not as the untouched original FANToM benchmark.
- [x] Exact reconstruction and packet-once/packet-absent checks are sufficient to fail closed on prompt drift.

## Decision B — source units

For every row, check that the target did not already learn the exact packet, the unbriefed source answer remains defensible, and explicit briefing would make the truth-belief candidate correct.

### 1. part `202-1` / set `202-1-0` — Bryant

- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason: Bryant joins only after the conversation has already moved to video games. His statement that he “heard snippets about video games” gives him at most the immediately preceding game topic; it does not reveal the earlier entertainment-industry discussion or the music preferences that constitute the packet. The source-correct unbriefed candidate therefore remains defensible, and explicit briefing with the exact packet would make the truth-belief candidate correct.
- [x] Verify that Bryant's “heard snippets about video games” does not give him the earlier entertainment-industry and music topics named by the packet.
- [x] Candidate/packet semantic alignment passes.

### 2. part `244-0` / set `244-0-0` — Nina

- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: REJECT. The displayed source dialogue has a material identity inconsistency exactly at the access-boundary transition: Elena leaves; a new turn is labeled Nina saying “I’m back”; Collin immediately replies “Good to have you back, Elena!”. This makes it unclear whether Nina is genuinely a distinct late joiner or Elena has been mislabeled. Because the target identity determines whether the New Year's Eve tradition was already heard, the target information set is not well-defined without silently repairing the source.
- [x] Resolve the source inconsistency: Elena leaves, Nina later says “I’m back,” and Collin replies “welcome back, Elena.”
- [x] Decide whether this identity error invalidates the target's information set. Do not silently repair it.

### 3. part `115-1` / set `115-1-1` — Madelyn

- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason: Madelyn's entry only signals that she is aware of a rich discussion about social justice at a high level. The exact earlier personal-experience mapping in the packet—Darren/racial injustice, Adan/low-income immigrant economic inequality, Alondra/racial and gender discrimination plus climate justice, and Juan/disabled-Latino intersectionality—is not stated to her after she joins. Her visible post-join exchange is strategy-focused, so the source-correct unbriefed candidate is defensible for this transformed contrast; explicit briefing supplies the missing specific experiences and makes the broader truth-belief candidate correct.
- [x] Madelyn says she was intrigued by the discussion; verify that this does not imply access to the specific personal experiences in the packet.
- [x] Candidate/packet semantic alignment passes.

### 4. part `179-0` / set `179-0-0` — Kyleigh

- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason: Dallas tells Kyleigh only that they had been “talking about our experiences with social justice.” That reveals the broad topic but not Dallas's observed-racial-profiling motivation or Allyson's low-income / higher-education barriers. The exact personal stories and motivations remain inaccessible until the packet is explicitly supplied.
- [x] Verify that “we were just talking about our experiences” reveals only the topic, not Dallas's and Allyson's specific stories/motivations.
- [x] Candidate/packet semantic alignment passes.

### 5. part `252-0` / set `252-0-0` — Tatiana

- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: REJECT. Tatiana's first turn says it is “truly motivating to hear your experiences and how your support networks effectively helped you all overcome your difficult times.” That is stronger than merely learning the generic topic after joining and directly indicates access to the earlier experience discussion. The source-correct candidate categorically says she “does not know or is unaware” of the personal experiences. Even if the dialogue does not prove she can map every person to divorce/job-loss/anxiety, the categorical unawareness claim is too strong for the displayed conversation, so the causal alignment gate fails rather than being silently repaired.
- [x] Tatiana says it is motivating to hear their experiences and how networks helped; verify whether she nevertheless lacks the exact divorce/job-loss/anxiety mapping asked by the question.
- [x] Reject if the source's categorical “does not know” answer is too strong for the displayed dialogue.

### 6. part `212-0` / set `212-0-0` — Julie

- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason: Julie rejoins knowing only that the discussion concerns fashion choices and immediately redirects to fashion icons. Paris's oversized neon coats, Jane's daring high-profile-event dress, and their controversy/confidence discussion are never repeated after Julie returns. The unbriefed ignorance candidate and the exact packet therefore align cleanly.
- [x] Verify that the post-join fashion-icon discussion does not reveal the earlier specific controversy stories.
- [x] Candidate/packet semantic alignment passes.

### 7. part `255-0` / set `255-0-0` — Sierra

- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason: Sierra joins only after the malformed source turn split in which `"Blink"` is divided across Gina's and Claire's turns. The book title is not repeated after Sierra joins. The malformed split is source noise but does not alter who had access to the title, and the exact packet cleanly induces the truth-belief candidate if explicitly told to Sierra.
- [x] Verify that the book title is never repeated after Sierra joins.
- [x] Candidate/packet semantic alignment passes despite the malformed source turn split around `"Blink"`.

### 8. part `168-2` / set `168-2-0` — Cesar

- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason: Cesar receives only Ty's high-level summary (“working smart, not hard” / work-life balance) before contributing his own concrete strategies. He is not told the earlier Pomodoro, task-decomposition, Eisenhower Box, and detailed break/quality strategies. The source-correct candidate captures the concrete strategies available in Cesar's own post-join segment, while the packet supplies the missing broader strategy set; after explicit briefing the truth-belief candidate is appropriate.
- [x] Cesar hears a high-level summary and contributes his own strategies; verify the source-correct partial-belief candidate captures this correctly.
- [x] Verify that explicit briefing with the full packet makes the broader truth-belief candidate correct.

## Human review outcome

- Transformation contract: **PASS**.
- Source units: **6 ACCEPT / 2 REJECT / 0 UNSURE**.
- Rejected source units requiring replacement-only review:
  - part `244-0` / set `244-0-0` — Nina identity/access-boundary inconsistency.
  - part `252-0` / set `252-0-0` — Tatiana's dialogue contradicts the categorical unawareness candidate strongly enough to invalidate causal alignment.
- No model outputs were inspected. Do not freeze this FANToM pilot or run target models until the two rejected units are replaced and those replacements alone pass human review.

## Automatic checks already passed

- local tests: `29 passed`;
- official archive SHA-256: `1d08dfa0ea474c7f83b9bc7e3a7b466eab25194043489dd618b4c5223e1253a4`;
- extracted official JSON SHA-256: `6a898e95df9fa48608232e45a8eb8f531e4d633aaf1a023a2b910991a6bc7c6e`;
- committed full-text review Markdown SHA-256: `d7860a60aac74e18116e41ed0443786f1c4bf4dda187657cab29fadef0e6b82e`;
- committed serialized four-cell JSONL SHA-256: `9af1e00115f3ab021e4e669a0fbf8d7990a29bf0cf69c25cf9d5be9beeff7273`;
- 8 distinct provisional independent `part_id` units;
- pinned source eligibility audit: 636 eligible rows across 335 provisional `part_id` units;
- one eligible first-order inaccessible QA per selected source row;
- one source-native `no` accessibility probe for each target;
- exact source-to-four-cell reconstruction: PASS;
- exact fact packet occurs once in each `WITH` and never in `WITHOUT`;
- model outputs inspected: none.

Automatic checks do not resolve dialogue inconsistencies, answer/packet semantic alignment, or the legitimacy of the allowed briefing manipulation. Those remain human gates.
