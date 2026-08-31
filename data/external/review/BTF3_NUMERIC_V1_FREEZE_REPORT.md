# BTF-3 numeric v1 — freeze report

Source: `btf3_numeric_questions_and_forecasts.parquet`, SHA-256 `1bee10210dabcfcc41d052e7d6458d3674f87b40e1a8f07ab1796fc040ca0747` (matches the pinned value).
Artifact: `/home/xiang/research_hun/try_clone/data/external/review/btf3_numeric_v1.jsonl`  
**Artifact SHA-256: `cb0c925ade9b76eee71f9a6f9dc695da44fb717510e15a5156e6416967ef6b15`**

## Source filtering

- rows in source: 392
- pass source validation: 347
- also carry `sota_forecast_cdf_3`: 338
- below cutpoint: 150; above cutpoint: 188

Rejections, by reason:

- 45: resolution sits exactly on the cutpoint

## Selection

64 below + 64 above = 128 units, by seeded deterministic shuffle (seed `20260901`) within each stratum, over rows sorted by `question_id`. Selection uses only source fields; no target-model output participates.

## Verification run on every candidate

All four prompts of every selected unit were regenerated from the pinned source row and compared byte-for-byte; the later packet is absent from both WITHOUT prompts and present exactly once in each WITH prompt.

## Review provenance

This artifact has **automated validation plus a 32-item spot audit** (seed `20260902`, ids in `btf3_numeric_v1_audit_sample.json`) — not the per-item human review the 256-unit binary artifact received. It is reported as a replication in a second task type with lighter review provenance, per `PREREGISTRATION_G9_NUMERIC.md` §4.
