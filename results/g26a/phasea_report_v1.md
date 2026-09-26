# G26A Phase A — selector gate funnel
- date: 2026-09-25
- run sha256: `becf1ee6bb153ff92d02fb02fb1a180472c1277f7dda63016ef3e8493637f9be` (rows 14560/14560, selector mistral-small-24b, exactly one parsed row per item x kind)
- items: `data/items/g26_phasea_pool_v1.jsonl` n=3640 sha256=`ad0ac715a609f49f`
- blindness: PASS — 0 rule-cell rows, 0 probe rows
- drops: {'unknown_item': 0}
- funnel (gates passed 0/1/2/3): [1197, 1773, 667, 3]
- full 3-gate items: 3 (threshold 200) -> **HARD STOP**
- selected: 0 <= 300, ids sha256 `None`
- NOTE: gates computed ONLY from Y0/YA/YB/YAB; no rule cell or probe exists in this file (selection blindness, §5).
