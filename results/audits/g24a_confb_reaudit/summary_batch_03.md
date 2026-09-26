# Re-audit summary — batch 03 (`g24a_confb_reaudit`)

Scope: 50 claim/evidence pairs (`g24cfb_147`–`g24cfb_222`) from `blind_batch_03.jsonl`.
Judged independently from the pair text only; no other repository files, metadata, prior reviews, or model outputs were read. No original data was modified and no replacement pairs were selected.

Output: `results/audits/g24a_confb_reaudit/audit_batch_03.jsonl`

## Verification
- Records written: **50**
- Unique IDs: **50** (no duplicates, no missing IDs)
- Schema: exactly `id, relation_a, relation_b, pair_valid, naturalness, issue` on every line; all values from the allowed enums.

## Counts

| Field | Value |
|---|---|
| `relation_a` | support 25 · refute 24 · ambiguous 1 · neutral 0 |
| `relation_b` | support 24 · refute 24 · ambiguous 2 · neutral 0 |
| `pair_valid` | true 47 · false 3 |
| `naturalness` | natural 29 · awkward 20 · broken 1 |

## Pairs judged invalid (3)

| id | reason |
|---|---|
| `g24cfb_149` | Evidence B says "nine National Championships" but enumerates ten title years — internally inconsistent, so it cannot cleanly support "less than ten". Evidence A (ten titles) does contradict the claim. |
| `g24cfb_210` | Claim "One band member quit … in 2004" vs evidence B listing three members quitting. Contradicts only under an exactly-one reading; under an existential reading B is compatible. Relation marked ambiguous; also typo "gutarist". |
| `g24cfb_211` | Evidence A changes "first **confirmed** case" to first "**possible** case". The two statuses are not mutually exclusive (the same patient can be both), so A neither entails nor clearly contradicts the claim. Evidence B does support it. |

## Borderline but retained as valid (flagged in `issue`)

- `g24cfb_169` — B substitutes Reliance Entertainment for Image Nation and never denies Image Nation; the conflict holds only if the "in association with" credits list is exhaustive.
- `g24cfb_189` — metric mismatch: A's 3-win margin is regulation/overtime wins (41–38), B's 1-win margin is total wins (44–43); the claim does not say which.
- `g24cfb_174` — "mixed" vs "negative" is a conflict of overall characterization, weaker than a hard factual opposition.
- `g24cfb_173` — B only denies the 505 ft distance and never addresses the "longest in park history" clause directly.
- `g24cfb_198` — claim conflates actress Clara Rugaard with the character named "Daughter"; conflict is on naming.
- `g24cfb_196` — evidence A is hedged ("perhaps second … at least after China").

## Text-quality flags

- **broken (1):** `g24cfb_177` — mojibake in the scores (`2i??2`), plus unspecified referent "United".
- **awkward (20):** `g24cfb_152` garbled quotation nesting; `g24cfb_158` claim has no referent for "cases"; `g24cfb_161` referent given only as surname "Kgositsile"; `g24cfb_163` agreement error "The Steelers has" + missing context; `g24cfb_176`/`g24cfb_178` glued sentence boundaries; `g24cfb_179` missing citation punctuation; `g24cfb_180`/`g24cfb_192` stray commas; `g24cfb_189` metric mismatch; `g24cfb_196` hedged/awkward phrasing; `g24cfb_198` actress/character conflation; `g24cfb_200` unnatural article "the COVID-19"; `g24cfb_201` odd glosses; `g24cfb_202` truncated citation fragment; `g24cfb_203` dangling "( or ;" fragment; `g24cfb_210` typo "gutarist"; `g24cfb_212` fabricated term "Edgar economics"; `g24cfb_217` asterisk used as list separator; `g24cfb_218` wikitext braces leaked into text.
