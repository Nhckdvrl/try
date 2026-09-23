# G24A selection report v1

- selection model: `mistral-small-24b` (kinds: admit_post, admit_pre, base — no Exclude, no probes)
- eligibility: signed mean Admit leverage ≥ 10.0 readout points; candidate order = builder shuffle seed 20260924
- selected 600 / quota 600; all quotas filled: True
- selected-item leverage (selection model): min 10.0, p50 40.1, max 99.8

| stratum | pool | examined | eligible | selected | shortfall | missing | <τ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fever/SUPPORTS | 6326 | 666 | 200 | 200 | 0 | 0 | 466 |
| fever/REFUTES | 6322 | 1338 | 200 | 200 | 0 | 0 | 1138 |
| scifact/SUPPORT | 417 | 148 | 100 | 100 | 0 | 0 | 48 |
| scifact/CONTRADICT | 216 | 216 | 100 | 100 | 0 | 0 | 116 |

selected file sha256: `b0d02f7ab1ae835149aa0e726dbe4b0c4186256c94f46d03d978632f9c951b34`
