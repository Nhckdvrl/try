# BTF-3 Large Replication v1 — human review ledger

**Review date:** 2026-08-31
**Reviewer of record:** Claude Opus 5, working under the project author's
direction inside Claude Code, reading each candidate packet in the frozen queue
order. This round's packet-factual review is therefore **LLM-assisted and
disclosed as such**, per `PREREGISTRATION_BTF3_LARGE_REPLICATION.md`; the
author spot-checks entries afterwards. No external lookup was used: every
decision rests on the candidate's own question, criteria, background, and exact
resolution packet, exactly as the confirmatory round's ledger did.
**Target-model outputs inspected during this review:** none — none exist for
this round.

**Candidate source:** the immutable queue
`data/external/review/btf3_large_replication_v1_queue.json`
(SHA-256 `116a166926fc25a4751bcfe63698e55c294ff82a5a96dd80dc713af6234ec551`),
displayed in `btf3_large_replication_v1_{yes,no}_review_*.md`.

**Protocol:** walk each realized-outcome queue strictly in order and stop when
that bucket reaches its first 128 ACCEPTs. ACCEPT requires all four registered
gates to pass: pre-cutoff integrity, realized-outcome validity, exact-packet
factual validity, and unambiguous resolution criteria. REJECT/UNSURE
permanently consumes the queue slot; no source text or later packet is ever
repaired by hand. This ledger records only the prefix actually reviewed; the
unreviewed queue tail is neither accepted nor rejected.

This ledger does not itself freeze the artifact and does not authorize a model
run: `scripts/freeze_btf3_large_replication.py`,
`scripts/audit_btf3_large_replication.py`, the token census, and the
`g1-btf3-large-replication-freeze-v1` tag are separate, later steps.

## Standard applied to absence-based negatives

Many realized-NO packets establish their outcome by absence of a qualifying
event. The gate applied uniformly across this round is:

- **ACCEPT** when the packet cites sources that either cover the window to (or
  past) its close, or establish an affirmative state of the world in the late
  window that makes the qualifying event's absence directly evidenced (e.g. a
  documented postponement, a denied motion, an official index with no entries).
- **REJECT** when the packet's own cited evidence demonstrably stops well
  before the window closes and the packet nonetheless asserts coverage of that
  period, so the negative rests on nothing for a substantial stretch.

This standard was fixed while reviewing the first candidates and applied to
every later one; where an earlier decision was inconsistent with it, the
correction is recorded inline on that entry.

## Realized NO reviewed prefix

### NO-1. `ee5e37c7-f82f-5d49-95b2-86ad466c9d50`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-2. `c6c6f543-0d08-5e88-a85f-bb106cb74263`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-3. `4e1869f7-70cc-5b9c-9cb5-e6d6fbfc77a5`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-4. `286335f7-a12d-58b6-8a45-1e4c2caace90`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The packet's own "canonical tracking source" (the Arctic Sentry Wikipedia article) was last edited 6 May 2026 yet is used to exclude any qualifying contribution announcement through 1 June 2026, so the negative is not actually evidenced over the second half of the window.

### NO-5. `88ed1cd7-f3d5-5320-ae05-5f5aafe3cf9a`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-6. `9b7a20e1-e3de-5c0c-bd03-993cad053b72`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-7. `d3d630d3-ef28-5e29-b290-885c2a9dbcac`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-8. `6ea80da1-bcbd-5d3d-ba24-5b48c681ca16`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-9. `47cc7236-9764-5aa9-b180-2806b827d4dd`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-10. `4402e54f-60b1-59e6-a3de-d596b5319933`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-11. `e1798612-8370-5d8c-9f6f-0053f800090d`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-12. `6265737e-5024-5011-9af0-711be49976f8`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-13. `65802f66-e893-52c9-a10a-8fd12374a93b`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-14. `488722fe-1ce5-5cac-8b87-ff4cd8fba0b8`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-15. `0a5a5a39-e2e8-5361-bf66-e7868c1f293e`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-16. `2058d309-9cef-5fa3-b643-a1fce9f8ed92`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-17. `f8cd60e3-28bc-599c-a50b-0388e95f0057`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: Both sides did formally agree to a Victory Day ceasefire, but for May 9–11 rather than the criteria's May 8–10, so the question ("will both formally agree to observe a Victory Day ceasefire") admits two materially different readings — mutual agreement occurred, exact-window agreement did not.

### NO-18. `c7af6cd2-33ce-5896-b390-ca06202a7129`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-19. `ca85ca1e-7405-5af3-8e40-656a508b9a40`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-20. `1d1d4a2b-b89a-5008-85e4-4fd4c53176c0`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-21. `dc811e76-fe74-53b5-90ec-b2c88c20dc67`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-22. `17f370f7-3250-5cf8-bc16-d8c931876975`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-23. `c0f5bb94-9b70-5dfc-a10c-cf370cd53cea`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-24. `5daf5ef8-77b1-5320-a841-0645fc751f03`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The negative turns on reading ISW's May 14 "advanced into central Zakitne" as short of control and on an uncited assertion that the assessed-control map never flipped, so the criterion admits a second reasonable reading and the packet does not ground the map claim.

### NO-25. `8652505a-de8f-568a-9506-3db07316451c`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-26. `f4e752d2-cbc1-5cc4-b1ed-306106fa8b12`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-27. `188a20b2-d582-5f07-8279-4ed1926e4635`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-28. `470e6be8-2f05-56ac-b19c-fa9a23937985`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-29. `2117e428-00b0-5612-995d-2b1640f2eb56`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Note: initially marked REJECT for tracker staleness, corrected to ACCEPT while reviewing NO-36 to keep one consistent standard across the round; see "Standard applied to absence-based negatives" below. Correction made before any freeze and before any model output existed.

### NO-30. `fc6adee8-aed5-5cbd-97d3-7cdb5cbee281`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-31. `aa7f75d8-920e-5854-9a33-03e9c4c39cfa`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-32. `8758751a-d682-598a-bd20-6b94b89ace13`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-33. `1179a6da-9199-516e-90a7-d881fb0f3a26`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-34. `1ed76e90-dfbe-5bd5-b06b-bf0e9f967cad`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-35. `60f7e95d-8c28-5a32-8c34-0561f5fec83c`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-36. `dab08b7f-71f1-5bc2-bfbe-6fcc9bf104d3`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-37. `ec27a645-8361-5543-a733-f69babdb45cb`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-38. `7c1af7e2-2451-5e22-b3a1-ef809bbb2331`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-39. `4eb17908-c440-599b-ae0f-516c6d773f9f`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-40. `f9563ff5-0a53-5e56-9496-c35d44a3a20b`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-41. `70297794-e5ee-5a40-9314-bc7086064088`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-42. `72756beb-1bb9-55ae-a234-0db387e40c56`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-43. `f0011a23-22b3-550c-adc4-b233fd79a574`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-44. `5b13d31d-7672-5d4e-838b-264df5817a7a`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-45. `0e804a1b-4785-5fce-8f74-048fe941ac52`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-46. `43502e3a-7715-5a68-acc8-2a7f4cf3006f`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-47. `a983bf40-5c05-5b94-b9d2-65ac640809e3`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-48. `a0fb8e02-15ac-5a1d-aa1d-ada77a5268e4`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-49. `0f63f1fc-815c-508c-86a8-b453230dadbb`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-50. `7ca74fd1-4826-50f4-8864-7487b115cb5e`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-51. `f7391cde-9b66-52b0-9561-a9e12d5fbc60`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-52. `1aae92e0-bdac-565e-bfed-2ed0be71c16d`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-53. `d49e58a9-5b58-54a1-a971-1d7227483f8c`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-54. `b5577074-7a36-5fe1-be5f-e27a6b69ab5c`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

