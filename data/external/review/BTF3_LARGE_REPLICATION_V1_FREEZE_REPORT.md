# BTF-3 Large Replication v1 — freeze report

- artifact: `data/external/review/btf3_temporal_large_replication_v1.jsonl`
- artifact SHA-256: `0b6fd8d0304f6b7cde336a6518b1058983a9b93529e90cbb577d1878acf0901d`
- source: `data/external/raw/btf3/btf3_binary_questions_and_forecasts.parquet` (SHA-256 `b28f8fe5634f81afa8e4b37d815f875b6e33c24edf590484f1948efea8db051a`)
- queue manifest: `data/external/review/btf3_large_replication_v1_queue.json` (SHA-256 `116a166926fc25a4751bcfe63698e55c294ff82a5a96dd80dc713af6234ec551`)
- units: 256 (128 realized YES / 128 realized NO)

Every check below is fail-closed: this report is only written when all of them pass.

| check | detail |
|---|---|
| source SHA-256 matches the pinned revision | b28f8fe5634f81afa8e4b37d815f875b6e33c24edf590484f1948efea8db051a |
| queue manifest SHA-256 unchanged since queue freeze | 116a166926fc25a4751bcfe63698e55c294ff82a5a96dd80dc713af6234ec551 |
| NO queue file unchanged since queue freeze | 241771b91ab37a8322ad65e184895e0688858843eeffb6319610d571d5e78ec7 |
| YES queue file unchanged since queue freeze | af010c7deea6b6d3af1a5048032b5c18156d93d6b9a34fa6820a501e0a7efe9e |
| schema validation | PASS |
| exact item count | 256 |
| unique independent units | 256 unique |
| zero overlap with pilot_v0_2r2 | 0 of 8 excluded IDs present |
| zero overlap with confirmatory_v1_frozen | 0 of 64 excluded IDs present |
| zero overlap with confirmatory_v1_candidate_queue | 0 of 128 excluded IDs present |
| zero overlap with confirmatory_v1_review_reject_or_unsure | 0 of 13 excluded IDs present |
| zero overlap with historical_pilot_rejects | 0 of 2 excluded IDs present |
| NO bucket reached quota in frozen queue order | 128 ACCEPTs |
| YES bucket reached quota in frozen queue order | 128 ACCEPTs |
| artifact is exactly the first-N ACCEPT prefix of the frozen queue | 256 IDs re-derived independently |
| four prompt cells present, exact-transform and packet-leakage validation | PASS (all items) |
| outcome sign mapping and realized_resolution | PASS (all items) |
| no duplicate normalized question | 256 distinct questions |
| realized-outcome balance | 128 YES / 128 NO |

No target-model output was inspected or generated at any point in selection, review, freeze, or audit for this round.
