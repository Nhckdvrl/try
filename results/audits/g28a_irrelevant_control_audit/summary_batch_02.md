# Summary — Batch 02 blind relevance audit (g28a irrelevant-control)

- **Input:** `blind_batch_02.jsonl` (attachment only; no other repo files, old labels, or model outputs were opened)
- **Output:** `results/audits/g28a_irrelevant_control_audit/audit_batch_02.jsonl`
- **Records:** 50 written, 50 unique IDs, ID set and order match the attachment exactly (verified programmatically)
- **Fields:** `id`, `relevance`, `naturalness`, `issue`

## Relevance distribution

| Label | Count | Share |
|---|---|---|
| irrelevant | 50 | 100% |
| potentially_relevant | 0 | 0% |
| relevant | 0 | 0% |

Every sentence was judged against its claim on decision-relevance (support, refutation, or context, including indirect/entity-adjacent links). None of the 50 sentences mentioned the claim's entity or supplied any information bearing on the claim's truth value.

### Closest-to-relevant cases (still irrelevant)

- `g24cfb_089` — sentence discusses someone's parentage (Kinberg's parents) while the claim is about Goran Dragić's father: same *relation type*, different people.
- `g24cfb_076` — athlete bio sentence (boxer Carl Frampton) vs. a claim about Lamar Jackson's position: same *genre* (sports bio), different person.
- `g24cfb_103` — a chart-ranking statement vs. a box-office-ranking claim: same *shape* (rank assertion), different subject.
- `g24cfb_082`, `g24cfb_127`, `g24cfb_092`, `g24cfb_108` — same domain (2015 films, U.S. geography, film reviews) but no entity or fact overlap with the claim.

## Naturalness distribution

| Label | Count | Share |
|---|---|---|
| natural | 43 | 86% |
| awkward | 7 | 14% |
| broken | 0 | 0% |

Awkward items (text defects noted in `issue`):

- `g24cfb_080` — fused run-on, missing space after "38."
- `g24cfb_088` — stray trailing punctuation (". ,")
- `g24cfb_101` — garbled numeral "2,9662,966"
- `g24cfb_116` — ordinal typo "1th" plus mangled quotation marks
- `g24cfb_124` — section heading fused into the sentence ("Select Revenue MeasuresCrowley")
- `g24cfb_142` — citation fragment with repeated name and stray quotes
- `g24cfb_145` — convoluted, internally contradictory clause structure

No sentence was judged `broken`: each remained interpretable despite local defects. Several factually odd sentences (e.g., mismatched bios at `g24cfb_094`, `g24cfb_100`, `g24cfb_144`) are fluent English, so they were scored `natural` — naturalness reflects linguistic well-formedness, not factual accuracy.

## Integrity

- 50/50 records parse as valid JSON with exactly the required fields
- 50 unique IDs; no missing or extra IDs relative to the attachment
- Enums restricted to allowed values; every `issue` non-empty
- No frozen data was edited; only the two new files were written
