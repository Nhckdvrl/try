# BTF-3 v0.2r2 — minimal human review request

**Do not run models.** This round uses the unchanged corrected v0.2 transformation and replaces the second rejected NO source unit. Please review exactly two things: the new BRICS unit's source validity and the regenerated artifact's transformation integrity.

## Decision 1 — new source unit

- Question ID: `b92bacb5-8086-5dd2-a64f-9ec00c427248`
- Realized outcome: NO
- Present date: `2026-05-13 22:16:46.060251`
- Eligible source day: through end of UTC day `2026-05-13`
- Source boundary encoding: `date_cutoff_end=2026-05-14`
- Expected resolution date: `2026-06-01 00:00:00`
- Reviewer decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reviewer reason（拒绝或不确定时必须写）:

### What to verify

- [ ] The May 14–15 meeting had not begun by the present timestamp.
- [ ] Every claim in the background was available by the end of May 13 UTC.
- [ ] The resolution criterion distinguishes a joint statement/communiqué/declaration from a chair's statement or outcome document unambiguously.
- [ ] By July 1, no qualifying joint product had been published.
- [ ] The exact packet contains no false, misleading, temporally impossible, or unsupported supporting claim.
- [ ] The packet informs the outcome without changing the question's interpretation.
- [ ] No safety/privacy concern.

### Independent precheck already completed

This is a precheck, not a substitute for the requested human decision.

- India's Ministry of External Affairs listed the meeting for May 14–15 and later published a document titled **“Chair's Statement and Outcome Document at BRICS Foreign Ministers' Meeting (May 15, 2026)”**: <https://www.mea.gov.in/bilateral-documents.htm?dtl/41144>.
- The linked official PDF's first-page title was independently downloaded and text-extracted; it says **“Chair's Statement and Outcome Document,”** not joint statement/communiqué/declaration: <https://d2jiw2zrmmyqt8.cloudfront.net/wp-content/uploads/2026/05/15173225/BRICS_Chairs_Statement_May15_2026.pdf>.
- AP explicitly reports that the meeting ended without a joint statement: <https://apnews.com/article/india-brics-iran-war-c2239256c5f08ad15739fb528a53aedd>.
- Reuters independently reports that BRICS failed to issue a joint statement and India released only a chair's statement: <https://www.internazionale.it/ultime-notizie-reuters/2026/05/15/brics-talks-end-without-joint-statement-exposing-divisions-over-war-in-iran-2>.

The complete verbatim question, criteria, background, resolution packet, and condition checklist are in section 4 of `btf3_temporal_pilot_v0.2r2.md`. The four complete serialized prompts are in the matching JSONL record. Do not edit the source packet when deciding.

## Decision 2 — regenerated transformation integrity

- Artifact decision: `[ ] PASS  [ ] FAIL  [ ] UNSURE`
- Reviewer reason（失败或不确定时必须写）:

Check the JSONL as a whole:

- [ ] Exactly 8 independent `question_id` values, balanced 4 NO / 4 YES.
- [ ] Both rejected IDs are absent:
  - `b6fc94e7-a0b9-56b6-87a1-ba94f29781e9`
  - `34d3588a-ffb0-5290-b964-bceb68be18f1`
- [ ] The seven v0.1-accepted IDs are retained; only the NO replacement changed.
- [ ] Every ex-ante prompt says information is available through the UTC day containing `present_date`, not through the calendar day named by `date_cutoff_end`.
- [ ] Within each target-set row, `WITH` differs from `WITHOUT` only by insertion of the exact source `resolution_explanation` under `LATER RESOLUTION PACKET`.
- [ ] Across target-set rows, the source question, criteria, background, packet text, task, and 0–100 scale are fixed; only target-information-set framing changes.
- [ ] No prompt contains an unregistered rewrite of source-native question, criteria, background, or packet text.

### Automatic checks already passed

- local tests: `25 passed`;
- pinned source SHA-256: `b28f8fe5634f81afa8e4b37d815f875b6e33c24edf590484f1948efea8db051a`;
- v0.2r2 JSONL SHA-256: `113e3b0dfa553f4bb5f3b4db0d94ed673f2590ec707c5b490413bce9b902dd8c`;
- schema: PASS;
- exact source-to-four-cell reconstruction for all 8 records: PASS;
- rejected IDs absent: PASS;
- required BRICS replacement present: PASS;
- balance: 4 NO / 4 YES;
- immutable v0.1 JSONL Git blob still equals the blob at commit `413b1ae`: `75a296f42c7605271ac4adb4cad0bff3938cebec`.

Automatic tests cannot certify factual packet integrity. A model run remains blocked until both decisions above are completed and the manifest is explicitly advanced.
