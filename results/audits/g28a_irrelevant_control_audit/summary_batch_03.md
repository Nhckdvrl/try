# Summary — Batch 03 (g28a irrelevant-control audit)

**Input:** `blind_batch_03.jsonl` (attached pair list, 50 records)
**Output:** `audit_batch_03.jsonl` (50 records) — verified: 50 lines, 50 unique IDs, ID set identical to input, all JSON valid, fields exactly `id` / `relevance` / `naturalness` / `issue`.
**Method:** Each claim–sentence pair judged independently from the attachment only. No other repo files, prior labels, or model outputs were consulted. Frozen data was not modified.

## Totals

| Relevance | Count |
|---|---|
| irrelevant | 50 |
| potentially_relevant | 0 |
| relevant | 0 |

| Naturalness | Count |
|---|---|
| natural | 42 |
| awkward | 7 |
| broken | 1 |

## Rationale

Every sentence in this batch was judged **irrelevant**: none provides support, refutation, or decision-relevant context for its paired claim. The mismatches are cross-domain (e.g., a UK road description vs. a film-review claim, a wrestler biography vs. a Quebec surveillance claim), and no indirect link was found that could shift a verdict on the claim.

Closest calls considered and rejected as genuinely irrelevant:

- `g24cfb_155` — sentence mentions Florida/Georgia (Orlando Magic's state), but only as band members' hometowns; no bearing on Ben Gordon's last team.
- `g24cfb_190` — sentence concerns Universal Music Group/Vivendi; B'Day is a Columbia/Sony release, so label context does not bear on its sales figure.
- `g24cfb_206` — sentence gives drummer Mike Mangini's 1963 birth date; a different person, so it says nothing about Fabrizio Moretti's birth year.
- `g24cfb_173` / `g24cfb_189` — review-verdict sentences with anaphoric "It" that cannot refer to the ballpark/home-run claim or to the Canadiens–Buffalo win totals.

## Naturalness flags

- **broken (1):** `g24cfb_177` — caption fragment with stray `'' ''` artifacts and no predicate.
- **awkward (7):**
  - `g24cfb_158` — dropped entity in "known in Japan as ,"
  - `g24cfb_169` — truncated mid-list, trailing comma, run-on ("Harris ) The group")
  - `g24cfb_174` — casing typo "wEST"
  - `g24cfb_189` — typo "priase" plus chain of "while" clauses
  - `g24cfb_200` — typos "good timed" / "fantasic", unbalanced quotes
  - `g24cfb_201` — missing space "2012–13.Notable" (run-on)
  - `g24cfb_217` — heading glued to text "MeasuresCrowley"
- Remaining 42 sentences are grammatical, fluent, self-contained statements (their irrelevance is topical, not linguistic).
