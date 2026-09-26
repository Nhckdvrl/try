# Blind LLM-assisted audit of G28A/G28B irrelevant controls

Local OpenCode MiMo v2.6 Flash inspected 200 claim/control-sentence pairs in four 50-item batches, without evidence-polarity labels or model outputs. Some CLI attempts failed at startup or after a batch file was written; only four independently validated complete output files are counted. Batch 01 used the synonymous label `genuinely irrelevant` for all 50 records; this summary maps that string to `irrelevant` without editing the raw audit file. This is LLM-assisted review, not human gold. Frozen controls and full-run analyses are unchanged.

Every batch has exactly 50 unique IDs matching its blind input; 200 distinct IDs overall. Every blind claim and control sentence exactly matches the frozen selected/rendered data.

| Category | Count |
|---|---:|
| Relevance: irrelevant | 199 |
| Relevance: potentially_relevant | 1 |
| Relevance: relevant | 0 |
| Naturalness: natural | 162 |
| Naturalness: awkward | 30 |
| Naturalness: broken | 8 |

## Potentially relevant or relevant controls

- `g24cfb_240` (potentially_relevant): March 2003 announcement that David Newman would score 'the film' is production-timeline context plausibly concerning Two Brothers, consistent with but not confirming a 2004 premiere; film unnamed so link is indirect.

A control-restricted reanalysis, if used, is explicitly post hoc and cannot replace the frozen full-sample result. The audit does not establish source provenance or factual truth of the control sentence.
