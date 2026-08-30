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

### NO-55. `75a9b157-4271-5ef6-a7d8-789e69325b07`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-56. `c3e01c3f-e0a8-5be2-88c6-d160793cba8d`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-57. `1059ecce-7633-59cc-9bab-df341bfe35b6`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-58. `65ab10c3-bb24-5e73-873f-da584796c42e`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-59. `93c5cdba-1ced-53ca-895d-4b748609c8dc`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-60. `0bcf7af9-981a-5207-8be0-4b8d54c62a52`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-61. `2366975e-e87b-5f7c-8483-d27184f9efe4`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-62. `e32addcd-ec31-5bb1-9ba9-4965c5e32803`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The final rule set the regulatory effective date to July 20, 2026 with July 1 only as optional early implementation, which reads equally well as a deferral of the default effective date past July 1 (YES) or as preservation of July 1 disbursements (NO), so the criteria admit two materially different readings.

### NO-63. `6c9e6111-3b05-5c07-ab7c-4ef8b079d788`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-64. `cf5c503c-6607-5653-ac22-a85f845c9baf`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-65. `e2c55fd1-b9c6-58bc-8fab-d85a2d4cecbc`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-66. `f0c57160-d1d9-552b-9d20-41ea4b4902d0`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-67. `97cec3a5-eaeb-5fb0-9ef4-20df60713baa`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-68. `bfb0572f-9cfc-5cb0-beaf-d5fbcf4fc46d`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-69. `c5099a67-5abb-548a-b92a-dd50c8e65064`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The packet itself concedes that the nationwide Sudanese airspace suspension of roughly May 4–8 could have closed Port Sudan to commercial flights for more than 48 hours, so the outcome rests on an acknowledged alternative reading rather than a single one.

### NO-70. `8d8a890a-dec3-51a4-afe2-bb5a8d58c88d`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-71. `f2d5546e-d35e-59de-a8d4-dd5de3effa61`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-72. `a0968428-9c0e-54e0-872c-32d96e222aaa`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-73. `01a607b2-d68c-5e0d-9bd8-efe79748b96e`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-74. `83077271-dd90-5017-8107-0d3fba6b8872`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-75. `a3478df7-22b6-5473-a74a-00a0cd521090`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-76. `009885f8-406c-570a-adbd-e63606108fea`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-77. `759e8c52-ee97-5e2b-a4eb-190fbd22775f`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-78. `c25aff37-8182-557f-8968-564b01f226a2`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-79. `5c6c82e6-d614-5f2b-915a-b62348cb4cda`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-80. `17e0010e-2915-5ccc-8f2e-370b5620a78f`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-81. `d95064ce-6216-5e03-8b91-7d74a9e7b723`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-82. `786d93d1-0fe1-5295-931c-5016ba7b7a4e`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-83. `354884fe-183d-5a76-b6b3-bc013a60ce41`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-84. `3c29a467-1406-55a9-8808-e1b3616c145e`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-85. `2baf84ab-2795-5ade-a60f-0187fdeef939`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-86. `559e0736-ec8f-51b2-88cc-9991be4c568c`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-87. `48ff1ce4-a365-5a5b-8824-c1cd5d2d4f80`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-88. `b37ed4ff-8c07-5ba3-a337-fb226eda2710`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-89. `78050dfe-7991-5192-b1f3-8404b08c9253`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-90. `5cdc8c75-bf10-53ff-96fc-f49682d368ba`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-91. `bc47e02a-e496-5031-9149-0baf0084a2db`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-92. `b7d5e885-04c6-543a-ab87-65ab3ae7885e`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-93. `b5bbd8cf-fce9-5d15-8c2d-b62df1e9f7f1`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-94. `010a7e76-7d92-50a7-926e-2732f299c585`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-95. `2d86237a-cccc-5df6-9d54-5af3e37a7de8`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-96. `317e8d9e-7f48-555a-a979-e49b07c2cde4`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-97. `d2c5fcaa-b273-5787-9846-32c25c11f11b`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-98. `49907cf8-ca9f-505f-9a20-e0471c9b2493`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-99. `a52206db-3c2f-5e6e-a7c8-9c995b9e0b93`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-100. `7a1ef715-5b39-5429-b0e8-5adf684581dd`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-101. `752483bd-c61e-58a0-9fd5-6033eceea25f`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-102. `fef6f75e-bd18-5994-b56f-99b3925acf4b`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

## Handoff point

Assistant-conducted review stops after **NO-102**. Everything from **NO-103**
onward in the realized-NO queue, and the entire realized-YES queue from
**YES-1**, is reviewed by the project author, appended below in the same format
and the same frozen queue order. NO-103, NO-104 and NO-105 were rendered on
screen during the assistant's session but no decision was recorded for them;
they are undecided and are the author's to judge.

Running totals at the handoff: 102 realized-NO candidates reviewed, **97
ACCEPT / 5 REJECT / 0 UNSURE** (rejects: NO-4, NO-17, NO-24, NO-62, NO-69).
31 more ACCEPTs are needed to reach the 128 quota in this bucket.

