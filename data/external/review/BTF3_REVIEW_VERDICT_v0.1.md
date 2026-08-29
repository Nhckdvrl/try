# BTF-3 temporal pilot v0.1 — human review verdict

**Review date:** 2026-08-29  
**Source revision:** `4b426627e19cd86202de69a40bc9dadb7f5ccd59`  
**Model outputs inspected:** none.

This is a reviewer ledger for `btf3_temporal_pilot_v0.1.md` and its immutable four-cell JSONL. It does **not** authorize a model run.

## Item decisions

| # | question_id | outcome | decision | background pre-cutoff | resolution support | note |
|---:|---|---|---|---|---|---|
| 1 | `b6fc94e7-a0b9-56b6-87a1-ba94f29781e9` | NO | **REJECT** | pass | **fail packet integrity** | The NO outcome is correct, but the exact packet says the 2026 Travelers Championship concluded June 28. Official PGA TOUR reporting shows weather pushed the playoff to Monday June 29. Because v0.1 injects the source packet verbatim, retain the audit artifact but do not use this unit. |
| 2 | `d72e1700-1552-5775-83d9-80ba7723f068` | NO | **ACCEPT** | pass | pass | Sources support that the special-counsel bill did not pass a plenary vote by July 1. |
| 3 | `84569bb0-4029-5ddd-9ce5-b787dc0d41e0` | NO | **ACCEPT** | pass | pass | Official Federal Reserve minutes were published May 20 and contain neither target term. |
| 4 | `0c1f9c71-e9da-5093-9eb8-05244ca3f49e` | NO | **ACCEPT** | pass | pass | Official ATP reporting shows both German semifinalists lost; the final was Fritz–Tiafoe. |
| 5 | `e6927299-6264-5334-be53-ec3a46dd0e78` | YES | **ACCEPT** | pass | pass | SpaceX's official page identifies the May 22 launch as Flight 12 and the first Starship/Super Heavy V3 flight. |
| 6 | `482705b8-b542-5934-abed-599fd4d27302` | YES | **ACCEPT** | pass | pass | Bank of Korea's May 28 release explicitly revises 2026 growth from 2.0% to 2.6%. |
| 7 | `4181856c-d761-5721-a7dc-a4698f1fb1ac` | YES | **ACCEPT** | pass | pass | Official Camera records show committee examination concluded June 24 and the bill entered Assembly discussion June 26. |
| 8 | `b0102690-c6ec-5482-8452-0151f77289b9` | YES | **ACCEPT** | pass | pass | The Venezuelan foreign ministry's May 4 statement explicitly reiterates historical territorial rights over Guayana Esequiba. |

## Global transformation finding

The source card describes `date_cutoff_end` as encoding the end of the UTC day containing `present_date`. In BTF-3 rows such as `present_date=2026-05-02 ...`, `date_cutoff_end=2026-05-03` is the boundary representing the end of May 2. The v0.1 adapter instead says the information set ends at the **close of UTC day `date_cutoff_end`**, which can be read as granting one extra calendar day. This is an adapter-level off-by-one wording bug.

Therefore:

- the **source-unit review result is 7 ACCEPT / 1 REJECT**;
- the existing v0.1 JSONL remains an immutable review artifact and must not be run;
- the adapter/contract must use the UTC day containing `present_date` (with `date_cutoff_end` as the source boundary encoding), not the close of the following calendar date;
- regenerate a v0.2 candidate set after the wording fix;
- replace the rejected NO unit so v0.2 is again balanced 4 YES / 4 NO;
- rerun schema/date/transformation tests and human-review the replacement unit before any model output is produced.

## External verification notes

Independent checks used authoritative sources where possible: PGA TOUR for Cameron Young/Travelers, Federal Reserve for the FOMC minutes, ATP Tour for Halle, SpaceX for Flight 12, Bank of Korea for the May outlook, Camera dei Deputati for A.C. 2822, and Venezuela's MPPRE for the Essequibo statement. Negative legislative resolution in South Korea was cross-checked against contemporaneous reporting and the source packet's National Assembly reference.
