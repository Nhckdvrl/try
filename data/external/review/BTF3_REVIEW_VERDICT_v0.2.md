# BTF-3 temporal pilot v0.2 — replacement review verdict

**Review date:** 2026-08-29

**Source revision:** `4b426627e19cd86202de69a40bc9dadb7f5ccd59`

**Model outputs inspected:** none.

This ledger records the source-validity review of the one new NO unit selected after the v0.1 audit. The seven source units accepted in v0.1 were retained unchanged. The corrected v0.2 cutoff semantics and four-cell construction passed the local automatic checks, but this exact source packet does not pass the no-silent-repair rule.

## Replacement decision

| question_id | outcome | decision | background pre-cutoff | resolution support | exact-packet integrity |
|---|---|---|---|---|---|
| `34d3588a-ffb0-5290-b964-bceb68be18f1` | NO | **REJECT** | pass | outcome appears supported | **fail** |

The question asks whether an Argentine Senate committee issued a formal electoral-reform `dictamen` by July 1. Official Senate reporting shows only an informational meeting followed by `cuarto intermedio` on May 13, and contemporaneous reporting supports that treatment remained delayed. The packet's NO conclusion therefore appears correct.

However, its conclusion also says that the congressional winter recess "running through late July" precludes a **late-June** committee report. Contemporaneous reporting placed the winter recess in July. A later July recess cannot prevent an event in late June. Because the transformation supplies `resolution_explanation` verbatim, the unit is rejected rather than silently edited.

## Consequence

- preserve `btf3_temporal_pilot_v0.2.*` as the failed replacement audit artifact;
- exclude this question ID as well as the v0.1 Cameron Young ID from future deterministic samples;
- generate `v0.2r2` with the unchanged corrected transformation and another NO replacement;
- retain 4 NO / 4 YES balance;
- review only the new replacement's source validity plus the regenerated artifact's transformation integrity;
- authorize no model run yet.
