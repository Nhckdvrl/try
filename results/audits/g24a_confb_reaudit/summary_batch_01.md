# Batch 01 re-audit summary — g24a_confb (blind_batch_01)

Independent audit of 50 claim/evidence pairs. No repository files, metadata, prior
reviews, or model outputs were consulted; judgments derive only from the attached
`blind_batch_01.jsonl` content. No original data was modified and no replacements selected.

## Output

- `results/audits/g24a_confb_reaudit/audit_batch_01.jsonl`
- 50 lines, 50 unique IDs, IDs match the attached batch exactly (0 missing, 0 extra)
- Fields: `id`, `relation_a`, `relation_b`, `pair_valid`, `naturalness`, `issue`

## Counts

| Metric | Value |
| --- | --- |
| Records | 50 |
| Unique IDs | 50 |
| `pair_valid = true` (exactly one support + one genuine contradiction) | 47 |
| `pair_valid = false` | 3 |

### relation_a

| Value | Count |
| --- | --- |
| support | 21 |
| refute | 27 |
| neutral | 1 |
| ambiguous | 1 |

### relation_b

| Value | Count |
| --- | --- |
| support | 27 |
| refute | 22 |
| neutral | 1 |
| ambiguous | 0 |

### naturalness

| Value | Count |
| --- | --- |
| natural | 38 |
| awkward | 10 |
| broken | 2 |

## Invalid pairs (3)

- **g24cfb_001** — claim "unreasonable reviews": A ("mixed reviews") neither entails nor
  contradicts that wording; only B matches. Odd claim wording.
- **g24cfb_010** — claim "more than the second smallest" has an unclear comparison
  direction, so A (third smallest) cannot be scored decisively; B (exactly second
  smallest) refutes under either reading. B also has a missing area value.
- **g24cfb_054** — A refutes (3–0 vs 2–0), but B only reports an *interim* 2–0 lead,
  not a completed loss, so B does not entail the claim. Claim is additionally
  impossible as written (a best-of-7 WCF cannot be lost 2–0).

## Text-quality flags

- **broken (2):** g24cfb_027 (claim "row German" for *Low German*; A contains a
  vandalized/vulgar definition of a different word), g24cfb_047 (A substitutes
  "Railroad" for "Raymond" in several names and carries a broken URL fragment).
- **awkward (10):** g24cfb_001, 002 (mojibake `ï¿½` in scores), 009 (claim has no
  referent), 010 (ambiguous comparison; missing area), 040 (garbled evidence with
  stray URL), 048 (stray "; Algeria" fragment; unnatural passive), 051 (missing birth
  date, "persepolise F C"), 054 (impossible claim), 055 ("Dublin Shamrocks of the
  NFL" mismatch), 061 (claim name "Ryan Urie" looks like a corruption of Ryan Ross).
- **Other notes recorded per-record in `issue`:** several claims omit context or
  referents (e.g., g24cfb_028 series-vs-film activation year; g24cfb_038 pragmatic
  conflict with "used to"); g24cfb_025 and g24cfb_061 rely on implicit rather than
  explicit contradiction.
