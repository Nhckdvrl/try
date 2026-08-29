# FANToM perspective v0.1 — human review request

**Do not run models.** The full source text and four-cell JSONL are committed evaluation artifacts. Review them at:

- `data/external/review/fantom_perspective_pilot_v0.1.md`
- `data/external/review/fantom_perspective_pilot_v0.1.jsonl`

Source attribution: Kim et al., *FANToM: A Benchmark for Stress-testing Machine Theory of Mind in Interactions* (EMNLP 2023), official repository revision `1cae6fa30f5ba04ca0fff5f5716b5ba7055e2e85` under MIT. These prompts are a project-authored evaluation transformation, not an original FANToM score reproduction.

## Decision A — transformation contract

- Decision: `[ ] PASS  [ ] FAIL  [ ] UNSURE`
- Reason:

Verify:

- [ ] The same first-order belief question and two source answer candidates remain fixed in all four cells.
- [ ] `OOB_WITH` makes the fact visible only to the evaluator; the target character never receives it.
- [ ] `ALLOWED_WITH` explicitly tells the exact same packet to the target after the conversation.
- [ ] The no-packet cells define the corresponding unbriefed target state coherently.
- [ ] Asking for probability of the truth-belief candidate supports the registered responsiveness/intrusion contrasts.
- [ ] The allowed post-conversation briefing is a legitimate perspective information-set intervention, not an unacceptable change of task semantics.
- [ ] The design is described as a source-anchored causal transformation, not as the untouched original FANToM benchmark.
- [ ] Exact reconstruction and packet-once/packet-absent checks are sufficient to fail closed on prompt drift.

## Decision B — source units

For every row, check that the target did not already learn the exact packet, the unbriefed source answer remains defensible, and explicit briefing would make the truth-belief candidate correct.

### 1. part `202-1` / set `202-1-0` — Bryant

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason:
- [ ] Verify that Bryant's “heard snippets about video games” does not give him the earlier entertainment-industry and music topics named by the packet.
- [ ] Candidate/packet semantic alignment passes.

### 2. part `244-0` / set `244-0-0` — Nina

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason:
- [ ] Resolve the source inconsistency: Elena leaves, Nina later says “I’m back,” and Collin replies “welcome back, Elena.”
- [ ] Decide whether this identity error invalidates the target's information set. Do not silently repair it.

### 3. part `115-1` / set `115-1-1` — Madelyn

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason:
- [ ] Madelyn says she was intrigued by the discussion; verify that this does not imply access to the specific personal experiences in the packet.
- [ ] Candidate/packet semantic alignment passes.

### 4. part `179-0` / set `179-0-0` — Kyleigh

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason:
- [ ] Verify that “we were just talking about our experiences” reveals only the topic, not Dallas's and Allyson's specific stories/motivations.
- [ ] Candidate/packet semantic alignment passes.

### 5. part `252-0` / set `252-0-0` — Tatiana

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason:
- [ ] Tatiana says it is motivating to hear their experiences and how networks helped; verify whether she nevertheless lacks the exact divorce/job-loss/anxiety mapping asked by the question.
- [ ] Reject if the source's categorical “does not know” answer is too strong for the displayed dialogue.

### 6. part `212-0` / set `212-0-0` — Julie

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason:
- [ ] Verify that the post-join fashion-icon discussion does not reveal the earlier specific controversy stories.
- [ ] Candidate/packet semantic alignment passes.

### 7. part `255-0` / set `255-0-0` — Sierra

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason:
- [ ] Verify that the book title is never repeated after Sierra joins.
- [ ] Candidate/packet semantic alignment passes despite the malformed source turn split around `"Blink"`.

### 8. part `168-2` / set `168-2-0` — Cesar

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason:
- [ ] Cesar hears a high-level summary and contributes his own strategies; verify the source-correct partial-belief candidate captures this correctly.
- [ ] Verify that explicit briefing with the full packet makes the broader truth-belief candidate correct.

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
