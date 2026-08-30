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

## Author-directed continuation (NO-103 onward)

### NO-103. `f49fa93e-49b7-5f11-9136-ab28b9160e33`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-104. `fbf697ca-8cc1-5da1-9d74-34cd3eeaba91`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-105. `27bc0270-92bb-582a-b072-4d726c2d3bdb`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-106. `9f134ccc-d404-5b35-826c-20fc95341106`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-107. `1fb9b683-64a4-5c17-8ab3-ff891d17af08`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-108. `a51291e6-e7a6-551f-ae98-84c0fd9ba7ca`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-109. `c4c1517d-6568-553b-ab8b-0295ab652ad4`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-110. `14b34551-7149-50ad-8da2-8dc59ca988fc`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-111. `08b12512-265a-5ac4-8344-b0f7b4d9fdc7`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-112. `258540c7-f3d4-51f9-a22b-39f6d7b9f7d2`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-113. `6d2d0507-66ca-5db4-b3a6-b46578bce91d`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-114. `826dafc3-01da-575f-97af-e3c07a999d0f`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-115. `467952fd-881f-5403-ad3f-a9d6c89e07ee`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-116. `bc18b8dc-6ab4-5cc2-98a1-8c73306d10a3`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-117. `1aaaf310-8d62-578b-bf36-36af15d1bc76`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-118. `44ca8582-5f12-5404-ba92-25ba1147a5e6`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-119. `32b35b20-8a83-5d2a-8b2e-a8d81190dc73`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-120. `82a5ef9e-4c98-5f0e-b972-dd99c657be88`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-121. `a60885bc-7464-5844-abe0-7a49c0c4d6c4`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-122. `987d2afa-d57c-55fd-aba5-1121bac875c0`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-123. `1e8bebfc-0bcb-5419-a625-2cb21bc7c345`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-124. `e0385127-5ec1-592f-8846-2c8b36ffe68f`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-125. `c291b187-a2de-5dfc-af3b-6d61a5c703f8`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-126. `51ed7fc0-4e65-5768-9722-e934d6d67122`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-127. `ad67b848-c8e3-5e1d-8d73-4a844c69026e`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-128. `443a70f1-50f3-5a66-886d-75f040616085`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-129. `1f4fcd81-59ce-5b8f-a614-453f9d871d80`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-130. `5ab08383-f013-50d1-934e-d66f41489c8c`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-131. `05051656-5672-5441-a76d-fa51b8ce8273`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: Criteria's operational test ("Powell listed by name as a voter" in the statement/minutes) assumed the pre-existing Fed statement format; Warsh's June 2026 format change stopped naming any voters, so the packet's own NO rests on a literal reading it admits conflicts with the substantive fact that Powell was one of the 12 voting members — a genuine two-reading conflict, not a resolved ambiguity.

### NO-132. `f96455a1-a3a2-5180-a110-d9c931bd3934`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-133. `2fe00425-ecf9-5969-b063-8e7f02b0d6a6`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-134. `77eaf3ec-051d-517d-a7e9-13775913b49d`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

## NO bucket closed: 128/128 ACCEPT quota reached at NO-134

Realized-NO review stops here. Final NO-bucket tally across the full
continuation (NO-103 through NO-134): 32 reviewed, **31 ACCEPT / 1 REJECT**
(NO-131). Combined with the original NO-1..NO-102 tally (97 ACCEPT / 5
REJECT), the bucket total is **128 ACCEPT / 6 REJECT / 0 UNSURE** across 134
reviewed candidates. NO-135, NO-136, and all later realized-NO queue entries
are left unreviewed per the stop-at-quota rule.

## Realized-YES bucket (author-directed continuation, YES-1 onward)

### YES-1. `67bc3f9e-9e8d-509f-8c6b-3d6cfce483bb`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-2. `b68d6dee-5a6b-59e6-9e65-4490ce1e3347`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-3. `9bad90f8-e1dd-50b2-8f05-4c54ca424c84`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-4. `ce975c54-f33a-55c6-a098-cc572538baf7`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-5. `1a212384-33d7-5ab4-abf4-559c00ef7562`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-6. `30c33338-f7cd-56af-a904-85fa7b9d4ec3`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-7. `ee51ff77-017d-5b54-8523-09a424b7bee0`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-8. `769d43d1-f7c7-5f51-bb05-562a4222c358`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-9. `188b4bac-c174-5f53-ac02-2f431f9c72d4`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-10. `ee0672d3-0838-5516-9ace-cb54cf371c21`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-11. `3627cdd9-2f72-5ae1-8e2f-7eff4bc14873`
- Decision: `[ ] ACCEPT  [ ] REJECT  [x] UNSURE`
- Reason: Unlike every other packet in this queue, this one gives no URLs or bracketed evidence IDs for its central claims (the June 18 attack, the government's TV communique, and its corroboration), so the outcome cannot be checked against cited evidence.

### YES-12. `a605b42c-6c3a-5d87-bae3-7b8b37a42bc8`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-13. `614badaa-58d1-51b1-a5a1-9faa933aa46d`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-14. `8927330f-7ff8-5eb2-bf0d-1cfcb782f96a`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-15. `4867b39d-d365-54e1-b4b9-f0ee4f7ecb82`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-16. `82f810af-002d-5361-bec4-2546bb30b9df`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-17. `a260075d-f882-537e-8f6a-b2ca6d18f97c`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-18. `35b53909-8dfe-5194-b1bb-cece83ae2e51`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-19. `d8d1e6cc-35f1-5c58-9056-7eaad25ddc20`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-20. `954bb27f-4c31-57a9-bac6-1b4d9af76f68`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-21. `c642ff10-a88a-561a-a137-b1398888abde`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-22. `7d4620a7-e855-5c4a-86af-3856e7176d02`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-23. `12949926-6a31-58fb-835a-5f9580d4fc45`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-24. `3f5d8fa9-7140-5215-b8b9-b71c501c738d`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-25. `9972c169-284b-52ad-8df3-1458684b4d4a`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-26. `555d2be7-6581-5345-9052-655b8c898df0`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-27. `a1ec0332-9728-5b5b-9120-43f5f7c13a43`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-28. `a906fb0c-c6ae-52c2-8dfc-77d59967c7c7`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-29. `22f09a7e-ea1c-5fba-83c5-171df87540de`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-30. `bc1ffedf-cfa2-5d5d-a8b8-ec9eddb09483`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-31. `9f25adad-9403-5b8f-866c-4cd0739b6173`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-32. `50189e8b-1bfb-5abe-8309-ecfc8090e56b`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-33. `b221e989-edf3-5fa2-b5c4-8475fb734649`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-34. `c4687ce5-2ff1-5788-8bfd-2289d7669ed4`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-35. `59be9f45-abb0-5270-8c80-566385621c0c`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-36. `d9973659-b764-5704-90ae-24d551e89a33`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-37. `ac8fbd78-aafd-573c-bddb-0b5f251d9fb4`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-38. `bd90f010-d501-5c54-a6a0-f4ed25ba1757`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-39. `12db019b-70a3-57ef-a0b8-aa8a2396cedd`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-40. `98ffa340-0e9c-5eeb-9055-0ff082c51933`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-41. `68380f5c-6283-5398-a26a-08d73fadedcf`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-42. `bbd97208-92b3-52ec-ba73-a904586add20`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-43. `e35b83e5-edc5-5778-9c3a-7ac64e877a6f`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-44. `1604cc3c-d311-53c0-b855-95c7c78b1bba`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The packet's own cited evidence (the FIFA squad article) postdates the May 11 deadline; it infers the submission "must have" occurred in time rather than citing evidence of the actual submission date, so the outcome is not established by the cited evidence.

### YES-45. `602df88b-b1c5-52a8-ae5e-25f02886988a`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-46. `d31341a8-aa9e-557d-9e20-17a706dc1904`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-47. `8af5a841-315b-529f-b47a-70d4efa66238`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-48. `501ff822-d537-55b7-956b-60ed0a6435cc`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-49. `78660adc-2473-50fb-b817-5a1b7b1a74b1`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-50. `c8a9c650-c3b9-5b07-ad24-38e7f03e1f31`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-51. `d22bd1f1-7ea7-54ff-90fc-be0f01aee972`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-52. `642ce768-5920-5773-aee8-ba40784dcf3b`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-53. `5e0b29a5-8ee9-5e46-b208-444af77252c6`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-54. `f843833c-b0dd-515a-954d-2d466abcf0ab`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-55. `49b762aa-df15-56f0-8884-4ca7f5769565`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-56. `19c51624-fb6a-5f03-b5b0-0362c9202cd1`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-57. `d345aa2e-74af-55d1-9b2e-e62e78291dd4`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-58. `66bb32a9-f09d-5c2e-80e8-73da6d84ac4c`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-59. `b3c0c024-61af-58c4-8856-fe7dacb9f180`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-60. `e6bf3057-e9c0-58b7-b18d-b737760937a9`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-61. `a3d2afee-a683-5b3e-92d6-f78d192173d5`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-62. `4f2199de-01e2-52f1-b368-5c4765bd8c17`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-63. `04bdc911-bceb-558d-9332-272a2687bda2`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-64. `ec471fcf-d34d-5284-939d-d94961d6436d`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-65. `b41eb641-c931-50da-97bb-4711c8dd6c65`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-66. `54b20761-0b2d-50b0-b7d6-7242e6c9cbda`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-67. `4a1e4fb7-aaeb-52f1-873d-ab20125c9951`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-68. `2ac281ec-eec7-582a-998d-fc353801e484`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-69. `88b874ff-e31d-5bf7-a836-ccb1cd5f9338`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-70. `fe39b56b-8133-5518-918a-09f312b235df`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-71. `4d01045b-3518-52b2-be59-875b24046d9d`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-72. `ee1a438a-563a-55e3-a7de-6faf60495f1d`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-73. `e24fc009-8a42-5cab-b6aa-21d38b5bec34`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-74. `b5f4ddc4-6c75-57c4-a46b-224a6ae80e67`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-75. `5c0765ed-cbd1-5af5-bce0-adbfebd4e0f6`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-76. `96632c8c-1bdd-5deb-9f65-deab719ac39b`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-77. `4b901b95-42aa-5956-b877-f7d93ecc9faf`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-78. `e9efc313-b658-5f08-9131-d6ebdeba1e68`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-79. `2142164e-3686-5db9-bb27-9342b1e0ac58`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-80. `1cf01a42-0810-5a33-8697-d491d3a2b7b9`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-81. `56552737-e7f5-5c74-93af-d71bba888c59`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-82. `b5a5f3eb-c6ff-53b8-af90-165b7a6edd91`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-83. `95af7649-c12e-5421-bfc5-b4602e9140db`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-84. `1a7c4056-3f4d-5ee7-a546-20cf0603b946`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-85. `cf59bea6-ac3a-5950-9e4f-bdde52ce15df`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-86. `84e716ac-125c-5b58-b2ab-ee7ebc630885`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-87. `a653ccb0-0617-5d42-b6c1-5d05e8b8fbb9`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-88. `4a605b39-ee84-5cc4-a585-ddef7a9d139f`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-89. `d6b23695-9cd2-5e95-9716-3a51e5d73e8b`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-90. `75e58d45-3a3a-5c36-8777-9665b2b891f6`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-91. `8042e84d-abd1-5dd7-ae5f-c794cb342f5b`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-92. `6eb48c32-a4a6-5b5d-aa5d-3b42a1901d38`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-93. `de2d60ab-051f-5a69-8dfb-29a3fca92a6f`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-94. `8b63881a-0edd-5ead-b3da-376fc18e2ddf`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-95. `a7698b19-7df7-5ddf-8366-756fd5db4df3`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-96. `910c18ab-33a5-560d-a068-1dafca5e6897`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The packet's evidence comes from "arena.ai/leaderboard/text-to-image," a domain that is neither the criteria's primary URL (lmarena.ai) nor its named mirror (huggingface.co), so the outcome cannot be verified against the specified resolution source.

### YES-97. `24fd6da5-881c-52a4-8ba1-072443ea34a3`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-98. `9444f0a3-e659-545b-9140-ad18973f6d83`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-99. `a840a31b-b264-593d-bf08-d63125496da7`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-100. `74d19d30-d036-5a2b-9b5a-ea56cd98d324`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-101. `54843f56-28cd-5268-ac2a-a572144b2c03`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-102. `630b345d-eb03-534c-a3e5-5de067aaed7b`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-103. `8c1f48ad-6eab-5d12-bb1d-498e7ba1d4bc`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-104. `0e872d88-0696-5bab-bee7-8930a09e301e`
- Decision: `[ ] ACCEPT  [ ] REJECT  [x] UNSURE`
- Reason: Packet gives no URLs or verifiable citations for the claimed May 17/18, 2026 White House/USTR China trade announcement, unusually thin sourcing for a claim of this significance, so the outcome cannot be checked against the cited evidence.

### YES-105. `26ddb28f-3a4f-557e-9a35-dbbe6058f71f`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-106. `e5493956-07d2-5dc5-8278-30bd6555c1a2`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-107. `4c864e5d-4bb5-5d1b-805b-79af67f9cebf`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-108. `c72d9a92-4f4f-5a7d-a743-ba16f38cf7c9`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-109. `abd86c65-1733-557c-98c3-0b141a39781b`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-110. `08621383-abe1-5f08-a7cf-c2d428fb717f`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: Packet's own reasoning invents and argues away a "scrivener error" procedure code (2018/0329(COD)) that does not appear anywhere in the actual resolution criteria shown (which consistently reads 2025/0059(COD)), indicating confused/unreliable reasoning about the source text.

### YES-111. `1a72e885-3f5f-5b05-908f-d1917db3547e`
- Decision: `[ ] ACCEPT  [ ] REJECT  [x] UNSURE`
- Reason: Central claims (OPM's June 29 bulletin text, the State Department internal memo reported by GovExec) are given with no URLs at all, unusually thin for a question whose resolution specifically turns on verifying individual-employee notification evidence.

### YES-112. `d3a6d847-a02f-5d73-9933-26c7587b5ab2`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-113. `a0321afa-c75a-51e9-abed-473012f40eba`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-114. `cc65c42b-a42c-5592-9f73-795582542f79`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-115. `d2fd04b8-f6d3-589d-bf27-12ad2ad89b68`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-116. `f3d67bd2-328e-5071-bbb7-9488766b1c0b`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-117. `e69889d5-1620-5024-8a0c-9bc3bfc047fd`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-118. `81d4c81e-bbd1-5da2-bd1a-d4f7677ea272`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-119. `513056b4-1fab-57a0-817f-480e1d55b703`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-120. `373def81-7e87-5a53-aa5e-eddea5ca5edc`
- Decision: `[ ] ACCEPT  [ ] REJECT  [x] UNSURE`
- Reason: All cited evidence (the blog's "April 29th Update" and the support page) is undated or dated 2025; the packet assumes continuity into the May–June 2026 window without any 2026-dated confirmation that SMTP-level rejection enforcement was still active then.

### YES-121. `a0022abe-c384-5c95-bb3d-dc53e212aee1`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-122. `f1ed32cb-26da-54da-86fb-220ffdbc5b0c`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-123. `08bb3a55-c266-546d-bdd5-3a706d12ed8c`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-124. `828cf239-a556-5ff3-9467-44bf1325dfa5`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-125. `17dee13a-3f4c-5bdd-88fa-8ddff8403454`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-126. `f794d090-ae6a-5b5a-9c6b-739a0fe1b063`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: Packet claims France's points were unchanged from the April 1 static release through June 2026 despite the background's own note that FIFA introduced live rankings specifically to reflect intervening matches (including pre-World Cup friendlies); it never actually checks a live June 1 snapshot, only a stale April figure and a non-official third-party tracker.

### YES-127. `d41b3f25-a551-57fd-a6f6-4a0c91bd91f7`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-128. `485c3100-532f-57ee-ac85-37b010b3b5eb`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-129. `044eca74-078c-5b13-97a8-643d48941987`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-130. `9e807f3f-c7c7-515d-895a-a18fbb170141`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-131. `741b4bed-7502-5cd2-9cbe-949fbc70f857`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-132. `7279494c-a775-5a57-a5f2-ac22252fb286`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-133. `72178d56-46a3-5048-a419-1a9d38fdba05`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-134. `e5104a3c-9010-506f-8e58-83e40c658ed9`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-135. `f8b8e64a-1462-56e8-8e51-2378eaca309f`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-136. `827eb0fa-d233-5346-be4a-29d03e90dcbd`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

## YES bucket closed: 128/128 ACCEPT quota reached at YES-136

Realized-YES review stops here. Final YES-bucket tally across the full
continuation (YES-1 through YES-136): 136 reviewed, **128 ACCEPT / 4 REJECT /
4 UNSURE** (rejects: YES-44, YES-96, YES-110, YES-126; unsure: YES-11, YES-104,
YES-111, YES-120). YES-137 and all later realized-YES queue entries are left
unreviewed per the stop-at-quota rule.

