# BTF-3 packet factuality audit v1 — verdict ledger

**Auditor of record:** _(fill in: name, and whether external lookup was
available — this ledger is worthless without that line)_
**Audit dates:** _(fill in)_
**Access used:** _(fill in: which sources were opened, e.g. live web, archive
snapshots, paywalled outlets unavailable)_
**Model outputs inspected:** none. The auditor must not open any file under
`results/raw/`.

**Protocol:** `PROTOCOL_BTF3_PACKET_FACTUALITY_AUDIT.md`. Sample:
`btf3_factuality_audit_v1_sample.json` (32 realized YES + 32 realized NO, fixed
by hash before any citation was opened). Packets to work through:
`btf3_factuality_audit_v1_yes.md` and `btf3_factuality_audit_v1_no.md`.

Nothing recorded here changes the frozen 256-unit primary sample.

## Verdicts

Append one block per item, in the order the packets are listed:

```markdown
### YES-1. `<question_id>`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-2. `<question_id>`
- Verdict: `[ ] PASS  [x] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason: one line, required for MATERIAL_ERROR and UNVERIFIABLE.
```

Exactly one box per item. `scripts/analyze_btf3_factuality_audit.py` parses
this file, applies the frozen decision rule, and computes the secondary
leave-flagged-out sensitivity.

## Verdicts recorded

Audit **stopped after 16 items** on the author's instruction (budget). The
remaining 48 sampled items were NOT examined and carry no verdict. They must
not be reported, summarised, or counted as passing.

**Auditor of record:** Claude Opus 5, with live web search and page fetching,
working under the project author's direction. This is the same model that
produced the selection review, so it is **not an independent-party audit**;
what is new is external lookup, which the selection review explicitly lacked.
**Model outputs inspected:** none.

**Audit dates:** 2026-08-31.

**Result so far: 16 examined, 16 PASS, 0 MATERIAL_ERROR, 0 UNVERIFIABLE.**
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
