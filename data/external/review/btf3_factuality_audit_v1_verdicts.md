# BTF-3 packet factuality audit v1 — verdict ledger

**Auditors of record:** mixed; see batch-specific provenance below.
**Audit dates:** 2026-08-31.
**Access used:** see batch-specific provenance below.
**Model outputs inspected:** none. No auditor opened any file under `results/raw/`.

**Protocol:** `PROTOCOL_BTF3_PACKET_FACTUALITY_AUDIT.md`. Sample:
`btf3_factuality_audit_v1_sample.json` (32 realized YES + 32 realized NO, fixed
by hash before any citation was opened). Packets audited:
`btf3_factuality_audit_v1_yes.md` and `btf3_factuality_audit_v1_no.md`.

Nothing recorded here changes the frozen 256-unit primary sample.

## Verdict format

Exactly one box per item. `scripts/analyze_btf3_factuality_audit.py` parses
this file, applies the frozen decision rule, and computes the secondary
leave-flagged-out sensitivity. `MATERIAL_ERROR` and `UNVERIFIABLE` entries
include a one-line reason.

## First batch — 16 items

These 16 items were audited first; their original reviewer provenance and
notes are retained below.

**Auditor of record:** Claude Opus 5, with live web search and page fetching,
working under the project author's direction. This is the same model that
produced the selection review, so it is **not an independent-party audit**;
what is new is external lookup, which the selection review explicitly lacked.
**Model outputs inspected:** none.

**Audit dates:** 2026-08-31.

**Result: 16 examined, 16 PASS, 0 MATERIAL_ERROR, 0 UNVERIFIABLE.**
One non-material numeric slip noted inline (YES-14).

### YES-1. `513056b4-1fab-57a0-817f-480e1d55b703`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: WHA79.2 confirmed to be a resolution (not a decision, which the criteria exclude); US named re: arrears.

### YES-2. `24fd6da5-881c-52a4-8ba1-072443ea34a3`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: ECB press release 11 Jun 2026: all three rates +25bp to 2.25/2.40/2.65, effective 17 Jun. Matches packet exactly.

### YES-3. `7d4620a7-e855-5c4a-86af-3856e7176d02`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: Guardian 16 May and Euronews 3 Jun: scheme extended to 1 Oct 2026; Home Office confirmed.

### YES-4. `741b4bed-7502-5cd2-9cbe-949fbc70f857`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: Wale elected 26-22 and sworn in 15 May 2026 as Manele's successor.

### YES-5. `66bb32a9-f09d-5c2e-80e8-73da6d84ac4c`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: PM Silina resigned 14-15 May 2026 over the stray-drone affair; inside the window.

### YES-6. `ec471fcf-d34d-5284-939d-d94961d6436d`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: Aaron Rai won the 2026 PGA at Aronimink, his first major.

### YES-7. `e6bf3057-e9c0-58b7-b18d-b737760937a9`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: MacRumors/Gurman article of 31 May 2026 fetched directly; price range, four frame designs, colours, no in-lens AR, late-2027 timeline all as described.

### YES-8. `54b20761-0b2d-50b0-b7d6-7242e6c9cbda`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: MTA and the five LIRR unions reached a tentative deal on 18 May 2026, ending the three-day strike.

### YES-9. `ce975c54-f33a-55c6-a098-cc572538baf7`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: Council of the EU press release 25 Jun 2026: final adoption of the two implementing regulations.

### YES-10. `d345aa2e-74af-55d1-9b2e-e62e78291dd4`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: Nice cour d'assises d'appel, 13 May 2026: 18 years for 'viols par surprise' — qualification maintained.

### YES-11. `a605b42c-6c3a-5d87-bae3-7b8b37a42bc8`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: House Small Business Committee markup 20 May 2026 ordered H.R. 8881 reported.

### YES-12. `82f810af-002d-5361-bec4-2546bb30b9df`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: Heavy fighting near Baidoa on 30 May 2026 between federal forces and Laftagareen loyalists.

### YES-13. `ee51ff77-017d-5b54-8523-09a424b7bee0`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: Polis signed SB 26-189 on 14 May 2026; the algorithmic-discrimination duty is removed.

### YES-14. `ac8fbd78-aafd-573c-bddb-0b5f251d9fb4`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: Junts voted for the entregas-a-cuenta decreto-ley on 18 Jun 2026. Non-material slip: packet writes ~151,731 million euros, reporting says 157,731 million; the outcome does not depend on the figure.

### YES-16. `e9efc313-b658-5f08-9131-d6ebdeba1e68`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: SpaceX Flight 12 launched 22 May 2026 from Starbase, first V3 vehicle.

### YES-18. `769d43d1-f7c7-5f51-bb05-562a4222c358`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Note: Fitch upgraded Argentina to 'B-' from 'CCC+', stable outlook, 5 May 2026.

## Remaining 48 — external audit

**Auditor of record:** ChatGPT (GPT-5.6 Sol, OpenAI).
**Audit date:** 2026-08-31.
**Access used:** live public-web search and publicly accessible webpages,
official records, and public source pages; no authenticated or paywalled-source
login was available.
**Model outputs inspected:** none. No file under `results/raw/` was opened.
**Scope:** only the 48 previously unreviewed items in
`btf3_factuality_audit_v1_remaining.md`; the 16 verdicts above retain their
original Claude Opus 5 provenance.

**Result: 48 examined, 47 PASS, 1 MATERIAL_ERROR, 0 UNVERIFIABLE.**
The sole material error is YES-31, where an outcome-changing conflict between
the natural-language question window and the resolution-criteria window makes
the recorded YES depend on an event outside the window stated in the question.

### YES-15. `630b345d-eb03-534c-a3e5-5de067aaed7b`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-17. `f8b8e64a-1462-56e8-8e51-2378eaca309f`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-19. `9e807f3f-c7c7-515d-895a-a18fbb170141`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-20. `e35b83e5-edc5-5778-9c3a-7ac64e877a6f`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-21. `fe39b56b-8133-5518-918a-09f312b235df`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-22. `96632c8c-1bdd-5deb-9f65-deab719ac39b`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-23. `3f5d8fa9-7140-5215-b8b9-b71c501c738d`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-24. `72178d56-46a3-5048-a419-1a9d38fdba05`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-25. `614badaa-58d1-51b1-a5a1-9faa933aa46d`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-26. `b5a5f3eb-c6ff-53b8-af90-165b7a6edd91`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-27. `d41b3f25-a551-57fd-a6f6-4a0c91bd91f7`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-28. `a1ec0332-9728-5b5b-9120-43f5f7c13a43`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-29. `a653ccb0-0617-5d42-b6c1-5d05e8b8fbb9`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-30. `81d4c81e-bbd1-5da2-bd1a-d4f7677ea272`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-31. `bd90f010-d501-5c54-a6a0-f4ed25ba1757`
- Verdict: `[ ] PASS  [x] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason: The packet's sole qualifying release was 20 May 2026, but the question asks for a release between 5 and 19 June; the criteria silently move the start to 12 May, so the YES depends on an outcome-changing question/criteria date conflict.

### YES-32. `555d2be7-6581-5345-9052-655b8c898df0`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-1. `d2c5fcaa-b273-5787-9846-32c25c11f11b`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-2. `987d2afa-d57c-55fd-aba5-1121bac875c0`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-3. `1059ecce-7633-59cc-9bab-df341bfe35b6`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-4. `752483bd-c61e-58a0-9fd5-6033eceea25f`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-5. `2d86237a-cccc-5df6-9d54-5af3e37a7de8`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-6. `82a5ef9e-4c98-5f0e-b972-dd99c657be88`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-7. `1fb9b683-64a4-5c17-8ab3-ff891d17af08`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-8. `a60885bc-7464-5844-abe0-7a49c0c4d6c4`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-9. `1aae92e0-bdac-565e-bfed-2ed0be71c16d`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-10. `97cec3a5-eaeb-5fb0-9ef4-20df60713baa`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-11. `4402e54f-60b1-59e6-a3de-d596b5319933`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-12. `c291b187-a2de-5dfc-af3b-6d61a5c703f8`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-13. `2366975e-e87b-5f7c-8483-d27184f9efe4`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-14. `a0fb8e02-15ac-5a1d-aa1d-ada77a5268e4`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-15. `bc18b8dc-6ab4-5cc2-98a1-8c73306d10a3`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-16. `5b13d31d-7672-5d4e-838b-264df5817a7a`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-17. `f0c57160-d1d9-552b-9d20-41ea4b4902d0`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-18. `b37ed4ff-8c07-5ba3-a337-fb226eda2710`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-19. `17e0010e-2915-5ccc-8f2e-370b5620a78f`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-20. `83077271-dd90-5017-8107-0d3fba6b8872`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-21. `0e804a1b-4785-5fce-8f74-048fe941ac52`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-22. `ee5e37c7-f82f-5d49-95b2-86ad466c9d50`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-23. `467952fd-881f-5403-ad3f-a9d6c89e07ee`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-24. `6c9e6111-3b05-5c07-ab7c-4ef8b079d788`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-25. `49907cf8-ca9f-505f-9a20-e0471c9b2493`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-26. `1d1d4a2b-b89a-5008-85e4-4fd4c53176c0`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-27. `e0385127-5ec1-592f-8846-2c8b36ffe68f`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-28. `f96455a1-a3a2-5180-a110-d9c931bd3934`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-29. `1f4fcd81-59ce-5b8f-a614-453f9d871d80`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-30. `65ab10c3-bb24-5e73-873f-da584796c42e`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-31. `a51291e6-e7a6-551f-ae98-84c0fd9ba7ca`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-32. `826dafc3-01da-575f-97af-e3c07a999d0f`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`
