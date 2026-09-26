# Summary — Batch 04 (g28a irrelevant-control audit)

- Input (sole source): `blind_batch_04.jsonl` — 50 claim/sentence pairs.
- Output: `audit_batch_04.jsonl` — 50 records, 50 unique IDs, IDs match the blind file exactly and in order.
- Fields: `id`, `relevance`, `naturalness`, `issue`. Schema validated (no extra/missing keys, enum values only).
- Frozen data untouched; no other repo files were consulted.

## Relevance distribution

| relevance | count |
|---|---|
| irrelevant | 49 |
| potentially_relevant | 1 |
| relevant | 0 |

## Naturalness distribution

| naturalness | count |
|---|---|
| natural | 40 |
| awkward | 6 |
| broken | 4 |

## Potentially relevant (1)

- `g24cfb_240` — claim: *Two Brothers premiered in 2004*; sentence: *"On March 25, 2003, it was announced that David Newman would compose the music for the film."* Production-timeline context (Mar 2003 composer announcement for "the film") is plausibly about the same film and consistent with a 2004 premiere, but the film is unnamed, so the link is indirect rather than confirmatory.

## Naturalness flags

**Awkward (6):** `g24cfb_223` (missing punctuation in role list), `g24cfb_224` ("Donner building", trailing `*`), `g24cfb_234` (nested/mismatched quote marks), `g24cfb_239` (stray unmatched quote mark), `g24cfb_273` ("pass reflections", "first and only pass"), `g24cfb_294` ("born on an unconfirmed year on April 19").

**Broken (4):** `g24cfb_237` (wiki markup artifacts `|Cuban`, `] ]`), `g24cfb_250` (citation author names spliced into sentence), `g24cfb_256` (heavy nested quote artifacts plus tense clash), `g24cfb_272` (Russian fragment spliced into sentence).

## Notes on borderline calls

- `g24cfb_281` (Devin Smith/Jets vs. 2006 Texans releasing Williams): same league and transaction type, but different player, team, and year — no decision-relevant bearing, kept **irrelevant**.
- `g24cfb_292` (Yesterday critic count vs. Sony Pictures corporate blurb): film-industry context only, no bearing on critic count or the film's identity — **irrelevant**.
- `g24cfb_233` (Pardison Fontaine birth date vs. Dave Evans' birth date): topic-adjacent (birth dates) but about a different person — **irrelevant**.
- All other pairs show no shared entity, event, quantity, or temporal link between sentence and claim.
