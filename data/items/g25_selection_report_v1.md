# G25A selection report v1

- eligibility: imported G24A rule — signed mean Admit leverage ≥ 10.0 readout points (Base/Admit rows only, model `mistral-small-24b`; no Exclude/probe row read)
- quotas (Option B): fever/SUPPORTS, fever/REFUTES, scifact/SUPPORT → 400; `scifact/CONTRADICT` dropped (pool exhaustion, stratum audit §3)
- disjointness: every item_id of the G24A 600 excluded before eligibility (item-level; cluster overlap disclosed, not hidden)
- selected 400 / quota 400; all quotas filled: True
- clusters (`source/cluster`): 342 (anchor 342; shared with G24A 600: see anchor check)
- selected-item leverage: min 10.0, p50 36.8, max 99.9
- selected ids sha256[:16]: `0b38e0837ed9fd60` (expected `0b38e0837ed9fd60`) — anchor_ok: True

| stratum | pool | excluded | examined | eligible | selected | shortfall | missing | <τ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fever/SUPPORTS | 6326 | 200 | 889 | 150 | 150 | 0 | 0 | 739 |
| fever/REFUTES | 6322 | 200 | 2139 | 150 | 150 | 0 | 0 | 1989 |
| scifact/SUPPORT | 300 | 100 | 200 | 100 | 100 | 0 | 0 | 100 |

Census (full pool, exclusion first; audit §2 reproduction):

| stratum | pool | excluded (=remaining sub) | remaining | missing | <τ | eligible |
| --- | --- | --- | --- | --- | --- | --- |
| fever/SUPPORTS | 6326 | 200 | 6126 | 0 | 4255 | 1871 |
| fever/REFUTES | 6322 | 200 | 6122 | 0 | 5318 | 804 |
| scifact/SUPPORT | 417 | 100 | 317 | 0 | 148 | 169 |
| scifact/CONTRADICT | 218 | 100 | 118 | 0 | 117 | 1 |

selected file sha256: `7c6993244d7808d8e65696c00a55f4fc14c7f3011f34f0266e450f1367173147`
