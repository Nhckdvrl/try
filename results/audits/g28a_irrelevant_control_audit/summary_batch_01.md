# Summary — batch 01 (g28a irrelevant-control audit)

- **Output:** `results/audits/g28a_irrelevant_control_audit/audit_batch_01.jsonl`
- **Records:** 50 (ids `g24cfb_000` … `g24cfb_063`, exactly the 50 pairs in the attachment)
- **Evidence used:** the attached `blind_batch_01.jsonl` only. No other repo file, label file, prior model output, or external source was read.
- **Fields:** `id`, `relevance`, `naturalness`, `issue`.

## Decision rules applied

- **relevant** — the sentence shares an entity, event, place, date, or relation with the claim and bears on whether the claim is true (direct or indirect link).
- **potentially relevant** — the sentence touches part of the claim's subject matter or a shared entity but does not itself settle it.
- **genuinely irrelevant** — no shared entity, event, place, date, or relation; nothing the sentence says could confirm or weaken the claim.
- **naturalness** — `natural` = reads as a well-formed sentence; `awkward` = parseable but with artifacts (markup noise, splices, tense/attachment problems, missing verb); `broken` = the intended reading cannot be recovered cleanly.
- **issue** — any defect observed in the pair (sentence-level by default; claim-side defects and close-call notes flagged explicitly). `none` when nothing notable.

## Distributions

| Field | Value | Count |
|---|---|---|
| relevance | genuinely irrelevant | 50 |
| relevance | potentially relevant | 0 |
| relevance | relevant | 0 |
| naturalness | natural | 42 |
| naturalness | awkward | 7 |
| naturalness | broken | 1 |

Non-`natural` sentences (8): `g24cfb_003`, `g24cfb_012`, `g24cfb_026`, `g24cfb_032` (broken), `g24cfb_046`, `g24cfb_054`, `g24cfb_058`, `g24cfb_063`. Records carrying a non-`none` issue: 16.

## Closest calls (checked, then rejected)

These were the only pairs with any surface overlap; each was rejected as genuinely irrelevant because the overlap is not a link to the claim:

1. **g24cfb_035** — both texts are review scores, but the sentence rates an iPad Mini on TechRadar while the claim is about critics' reception of *Kaththi Sandai*. Domain coincidence only.
2. **g24cfb_051** — the sentence names "Iran" among COVID high-risk areas; the claim's subject is an Iranian footballer. Nationality is never stated in the text and the sentence says nothing about any player or club.
3. **g24cfb_054** — claim and sentence both sit in 2018, but a basketball conference final and an album's sales units share no entity or event.
4. **g24cfb_061** — both use the phrase "the band", but the sentence's band (the *Sempiternal* act) is a different group from the claim's band.
5. **g24cfb_030 / g24cfb_063** — both concern staged fights; the claim is about *Rocky IV*, the sentences are about a different film's characters (Alice/Micky).
6. **g24cfb_008 / g24cfb_007 / g24cfb_014** — shared "release/confirmation date after year" shape across unrelated subjects (book vs. album; song vs. rookie contract; purse vs. case counts). Template overlap, not evidential overlap.

Repeated-sentence check: `g24cfb_021` and `g24cfb_056` carry identical sentence text, and `g24cfb_030`/`g24cfb_063` are near-duplicates; each was judged on its own claim and none was relevant.

## Verification

- 50 records written, one JSON object per line, all parse as JSON.
- Exactly 50 unique `id` values; zero duplicates, zero missing, zero extra relative to the attachment; order matches the attachment.
- Every record has exactly the four required keys with in-vocabulary values.
- No input file was modified.
