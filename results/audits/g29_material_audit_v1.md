# G29 blind material audit and freeze

Before G29 model inference. Mechanical source shortlist: 160 new VitaminC pairs. Local OpenCode MiMo v2.6 Flash audited blind batches 01–04 and 07–08; Longcat 2.5 Preview audited batches 05–06 after MiMo batch 05 stalled. A separate blind follow-up completed batch 05's initially empty issue explanations. These are LLM-assisted judgments, not human gold. Source roles were revealed only by this freeze script.

- Eligible on pair validity, naturalness, and original role alignment: 98/160.
- Frozen in seed order for model run: 80 (first 80 eligible if available).
- Flagged invalid pair: 35; non-natural: 37; orientation mismatch: 35 (overlapping categories).
- Selected seed ranks: [0, 1, 3, 4, 7, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19, 20, 22, 23, 26, 27, 28, 32, 33, 34, 35, 37, 38, 41, 42, 45, 46, 48, 51, 52, 53, 54, 57, 60, 62, 65, 68, 69, 70, 74, 77, 78, 80, 82, 83, 84, 86, 87, 88, 89, 91, 92, 93, 94, 96, 100, 101, 102, 104, 105, 106, 107, 109, 110, 113, 114, 116, 117, 118, 119, 122, 125, 126, 127, 128, 129].

All 160 candidate texts, all eight blind batches, and every auditor verdict remain in `data/items/`. No outcome-based filtering or replacements are permitted.
