# Batch 02 re-audit summary (g24a_confb_reaudit)

Source: `blind_batch_02.jsonl` (50 claim/evidence pairs), audited independently from the supplied text only — no other repo files, metadata, prior reviews, or model outputs were read.

Output: `audit_batch_02.jsonl` — **50 records, 50 unique IDs** (verified programmatically; schema keys exactly: id, relation_a, relation_b, pair_valid, naturalness, issue).

## Counts

| Field | Value |
|---|---|
| relation_a | support 20 / refute 29 / ambiguous 1 / neutral 0 |
| relation_b | support 30 / refute 20 / ambiguous 0 / neutral 0 |
| pair_valid | true 49 / false 1 |
| naturalness | natural 39 / awkward 10 / broken 1 |

## Invalid pair (1)

- **g24cfb_105** (Fabio / Survivor: Nicaragua): evidence_a says "Jud outlasted Chase"; Fabio's real name is Jud (Jud Birza), so A likely supports the claim rather than refuting it. If so both evidences support and there is no genuine contradiction; in-text the referent "Jud" is unlinked, so relation_a marked `ambiguous`.

## Notable valid-but-flagged pairs (genuine conflict, with caveats)

- **g24cfb_074** – B conflicts only by substituting "terror" for "depression" inside Pile's quote (no explicit denial).
- **g24cfb_101** – A substitutes "infected" for "destroyed"; adjacent outcomes, not an explicit denial.
- **g24cfb_072, g24cfb_127** – conflicting values are not strictly mutually exclusive (politician/astrologer; Wellston is a St. Louis suburb).
- **g24cfb_083, g24cfb_104** – conflict depends on dated/boundary readings (2012 vs 2017; "before March 6" vs on-date).
- **g24cfb_140, g24cfb_136** – support side is approximate ("generally positive" vs "rave"; "shocked" vs "perturbed").
- **g24cfb_092** – claim's "defeating the Nevada Wolf Pack" appears in neither evidence (omission in both; does not affect the support/refute split).
- **g24cfb_116** – neither evidence names Moldova (country referent omitted).

## Naturalness flags

- **broken (1):** g24cfb_124 — "264 bytes" is a corrupted rendering of 2^64 in claim and both evidences.
- **awkward (10):** g24cfb_075 (subject–verb disagreement), g24cfb_078 (vague claim phrasing), g24cfb_080 (garbled "overwhelming laughable reviews"), g24cfb_090 (B says "three" but lists four titles), g24cfb_092 (non-idiomatic claim + absent Nevada detail), g24cfb_108 (lowercased "washington redskins"), g24cfb_109 (unnatural "until before 1968"), g24cfb_112 (vandalized-looking producer name "kulbir yadav"), g24cfb_135 (title typo "Eigh Below"), g24cfb_144 (broken punctuation "Aircrafts . :").

No original data was modified and no replacement pairs were selected.
