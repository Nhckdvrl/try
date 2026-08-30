# FOMC HOLD candidate queue — pilot v1

> Fixed deterministic order (seed 20260829). Review top-to-bottom until 12 ACCEPTs that are also meeting-disjoint from earlier selections are reached. A REJECT/UNSURE consumes its queue slot permanently and is never resampled or reconsidered. Never reject for salience/fame -- only the four gates below.

For each unit, tick exactly one of ACCEPT / REJECT / UNSURE for all four gates jointly (all four must hold to ACCEPT). On REJECT or UNSURE, write exactly one line giving the reason.

### HOLD-1. `20140129_20140319`

- Previous meeting: 20140129 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20140129a.htm (sha256 `693f1c3d951cb33e210ecf7dd7e011843801ce614f45afa4caba9ba7824fb164`)
- Next meeting: 20140319 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20140319a.htm (sha256 `92d0ecfed5533785c904115be57de5a3c3f67c73932085433173c7bdcefd9480`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `maintain-current`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-2. `20181219_20190130`

- Previous meeting: 20181219 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20181219a.htm (sha256 `e7ebe302078abf08c70681490bc01407afe4c7e874eb0875c6abd46fa98b2ee6`)
- Next meeting: 20190130 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20190130a.htm (sha256 `f9caed1e443a1488e9bc7e5a8aa9ab121695e2a68abf71ee3963d9cfc3ed225b`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `verb`; announced range: `2-1/4 to 2-1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-3. `20150318_20150429`

- Previous meeting: 20150318 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20150318a.htm (sha256 `5dafe41e99b56313721e528cb75af0c8aca443ba64aabda43ae4624b8adb8be9`)
- Next meeting: 20150429 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20150429a.htm (sha256 `f04ecbdef31c329924fd28233b13b7a8ac10bb5b946f3321bd07ab57ee46992a`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `reaffirm-current`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-4. `20110622_20110809`

- Previous meeting: 20110622 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20110622a.htm (sha256 `5a026f69ef40a8426e99c6c09e693cc8c4aaa115a12f2fa9a5b0b82fa84c5d11`)
- Next meeting: 20110809 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20110809a.htm (sha256 `57b3e2f1ca25b14c914c28cd9f9e7045113774ea4e96aa0bb77db288302c832c`)
- Next statement's own action verb: `keep` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-5. `20100623_20100810`

- Previous meeting: 20100623 — https://www.federalreserve.gov/newsevents/press/monetary/20100623a.htm (sha256 `fc19b88fa89dca3deb0b1cec2c4b3ade2145dd484b46761c162d0eae48cbb51c`)
- Next meeting: 20100810 — https://www.federalreserve.gov/newsevents/press/monetary/20100810a.htm (sha256 `5ed5ef3073ecea349089ceee681348527a93c310f7721106c693732a075381a3`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `will-maintain`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-6. `20140730_20140917`

- Previous meeting: 20140730 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20140730a.htm (sha256 `a56526d0daf54bd3e999418c2eac7593479834ab12bc1011e8f0364800be1c67`)
- Next meeting: 20140917 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20140917a.htm (sha256 `511ca4bf78b9ba68f42fb6c75ce947d859884d61e706409e3c7077d23f9736c4`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `maintain-current`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-7. `20211103_20211215`

- Previous meeting: 20211103 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20211103a.htm (sha256 `936a0793b8ee66a16083455747c28ee097fea9ec2b8a13bf915c98ed2b3fb0e7`)
- Next meeting: 20211215 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20211215a.htm (sha256 `33faca803de62bec9114be46ff24300a33e84c3c9eb04a3432c048f7a4e990b2`)
- Next statement's own action verb: `keep` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-8. `20170614_20170726`

- Previous meeting: 20170614 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20170614a.htm (sha256 `a769b065dca8eb7e913f78ee02b153d7aef80f23bf7346a372662b1143dbdfc3`)
- Next meeting: 20170726 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20170726a.htm (sha256 `dcf672065edadc2606cf4644c1d2b800b0db8557763fb31caf66db98d19b801a`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `verb`; announced range: `1 to 1-1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-9. `20240320_20240501`

- Previous meeting: 20240320 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20240320a.htm (sha256 `3142be71341a9a7fbfb14722d29350f67efe34e56ea8252782de37990596078d`)
- Next meeting: 20240501 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20240501a.htm (sha256 `6b522e3c9e37b7c75dcd45cc6f8fad5a7e3d0e4fbfa5b7593ea3a5043fe360ea`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `verb`; announced range: `5-1/4 to 5-1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-10. `20111213_20120125`

- Previous meeting: 20111213 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20111213a.htm (sha256 `4209185c6dadd0bfa5fe5e8b6b902c9c20730345484d0da87de460f6da35c2a3`)
- Next meeting: 20120125 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20120125a.htm (sha256 `c08878a2371938e6eb40c02d609efe256efa056fe01c5135412b18f821126fbc`)
- Next statement's own action verb: `keep` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-11. `20130619_20130731`

- Previous meeting: 20130619 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20130619a.htm (sha256 `e09eb6e6de87d8eebeaa71be2b7ddbdb0a246665aa8047ba3c82923726b66d29`)
- Next meeting: 20130731 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20130731a.htm (sha256 `217c5b461b2a8c2da0b464017b0c654e08caa857f440d72d182524901fc8ddb4`)
- Next statement's own action verb: `keep` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-12. `20230920_20231101`

- Previous meeting: 20230920 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20230920a.htm (sha256 `112f7689b242c9a1694785b00c4421b4eed4ced44b1d03b04aa8de6c063fb296`)
- Next meeting: 20231101 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20231101a.htm (sha256 `29fe8005c004117d1aaf6875ae6f9795874033f0f4e08ed2edbcfdc566d932ff`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `verb`; announced range: `5-1/4 to 5-1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-13. `20150617_20150729`

- Previous meeting: 20150617 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20150617a.htm (sha256 `9dc68f1b61efa76692865cd2ca44617711f8ce69a91976fbb7d25029348bcbba`)
- Next meeting: 20150729 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20150729a.htm (sha256 `8c975096f430eeeca51190deebe331ab8b21abd81cb130c8b1f7795b6a3beb98`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `reaffirm-current`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-14. `20130501_20130619`

- Previous meeting: 20130501 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20130501a.htm (sha256 `422dbaeeca733f8c4de72cddcb042377a2b54f34aa58397d650e6e447e8eafb6`)
- Next meeting: 20130619 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20130619a.htm (sha256 `e09eb6e6de87d8eebeaa71be2b7ddbdb0a246665aa8047ba3c82923726b66d29`)
- Next statement's own action verb: `keep` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-15. `20120801_20120913`

- Previous meeting: 20120801 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20120801a.htm (sha256 `0dec33215a49b3e510569e3a291a776b18d28181cf8ffecc982b776f0ce04b68`)
- Next meeting: 20120913 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20120913a.htm (sha256 `67c213f7cef686b060e7453cc5700780f4078b5b9c216c17b0ca63f5a68de6a4`)
- Next statement's own action verb: `keep` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-16. `20120425_20120620`

- Previous meeting: 20120425 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20120425a.htm (sha256 `b4b837731172e84b36bcfccbc85d9d26bba09114b0dba75e4ba6571a764dcf00`)
- Next meeting: 20120620 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20120620a.htm (sha256 `8ee45c7664f988160c491be6733feda2446a426cb58d37890a47ef7c44205725`)
- Next statement's own action verb: `keep` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-17. `20191211_20200129`

- Previous meeting: 20191211 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20191211a.htm (sha256 `243b6952b8b4c45d4dc382fa613335f8c6392b88879ec7f491292d144863d282`)
- Next meeting: 20200129 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20200129a.htm (sha256 `db99d98d7d00380f39a2feb96066535a0f88ce3e831d04467fce956a2ef62292`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `verb`; announced range: `1‑1/2 to 1-3/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-18. `20160615_20160727`

- Previous meeting: 20160615 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20160615a.htm (sha256 `1350f25351209ba9be0ef5b5f2233350be38162565a05125d7a72c36a856a660`)
- Next meeting: 20160727 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20160727a.htm (sha256 `4dc45370e7a9b7c148e163724f14ae4c8cbe4796dadc5f43714aab63acf87564`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `verb`; announced range: `1/4 to 1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-19. `20130320_20130501`

- Previous meeting: 20130320 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20130320a.htm (sha256 `57045d7da7581fb5dbff87d5da34126d14f49e61dc3f2d096809507625f1bff4`)
- Next meeting: 20130501 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20130501a.htm (sha256 `422dbaeeca733f8c4de72cddcb042377a2b54f34aa58397d650e6e447e8eafb6`)
- Next statement's own action verb: `keep` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-20. `20150128_20150318`

- Previous meeting: 20150128 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20150128a.htm (sha256 `4ea465f6f5200c2a5fa5cd54c3e5d77b4c4e8f67d0d593eedf7f59e010a65a32`)
- Next meeting: 20150318 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20150318a.htm (sha256 `5dafe41e99b56313721e528cb75af0c8aca443ba64aabda43ae4624b8adb8be9`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `reaffirm-current`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-21. `20091104_20091216`

- Previous meeting: 20091104 — https://www.federalreserve.gov/newsevents/press/monetary/20091104a.htm (sha256 `d37d4686f9a0014d096e8dea663a6f0f155772da725fea66acaddc8caf52a4f8`)
- Next meeting: 20091216 — https://www.federalreserve.gov/newsevents/press/monetary/20091216a.htm (sha256 `0a7e218ecf9f8cefe81d084d1514bc970f52b6a4da222379a88c78ccaa8aca5d`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `will-maintain`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-22. `20200916_20201105`

- Previous meeting: 20200916 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20200916a.htm (sha256 `2af9e2e7be8ce799bd4b8482503ef0ed1b3ea958ec3841b951cef06b46323898`)
- Next meeting: 20201105 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20201105a.htm (sha256 `554da55b09153c4bf0705621139f288a3b17e07f7bd4cf806a23b64a0bbe3eba`)
- Next statement's own action verb: `keep` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-23. `20090923_20091104`

- Previous meeting: 20090923 — https://www.federalreserve.gov/newsevents/press/monetary/20090923a.htm (sha256 `12bf7126f177f5b246480763b7401bf69bd02cc20c3a3f667d7041cc130190c4`)
- Next meeting: 20091104 — https://www.federalreserve.gov/newsevents/press/monetary/20091104a.htm (sha256 `d37d4686f9a0014d096e8dea663a6f0f155772da725fea66acaddc8caf52a4f8`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `will-maintain`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-24. `20200610_20200729`

- Previous meeting: 20200610 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20200610a.htm (sha256 `f2b88155e705cc2ae005faf3b4afdb2c13510735fd793d818144f7d345f4870b`)
- Next meeting: 20200729 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20200729a.htm (sha256 `0391d603a5644b308a27173a40e539b2b385f05cc622857cc5d5cf053023851a`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-25. `20210922_20211103`

- Previous meeting: 20210922 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20210922a.htm (sha256 `13f2884751b55e791220feef7dd65b1f491833c2730d2eed99b6d65be70173d4`)
- Next meeting: 20211103 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20211103a.htm (sha256 `936a0793b8ee66a16083455747c28ee097fea9ec2b8a13bf915c98ed2b3fb0e7`)
- Next statement's own action verb: `keep` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-26. `20201216_20210127`

- Previous meeting: 20201216 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20201216a.htm (sha256 `9be9df94c80a5008bec2cc01727f73679e8849e26751f9fe0bea484d918dcfc2`)
- Next meeting: 20210127 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20210127a.htm (sha256 `d51e9beb76c6ba2ad93bc10e73e928ae712d9dc84c5f6520b1d91aa4bf32610f`)
- Next statement's own action verb: `keep` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-27. `20210127_20210317`

- Previous meeting: 20210127 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20210127a.htm (sha256 `d51e9beb76c6ba2ad93bc10e73e928ae712d9dc84c5f6520b1d91aa4bf32610f`)
- Next meeting: 20210317 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20210317a.htm (sha256 `3c6d197b336b0f9463d58557d5f2437d979dfab081caf2dda09b43341cf29235`)
- Next statement's own action verb: `keep` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-28. `20131218_20140129`

- Previous meeting: 20131218 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20131218a.htm (sha256 `1ca9e219e45cd2eae1877e86eaa54dc6941ccbae42f1c6a2aaabe1de03bffc8f`)
- Next meeting: 20140129 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20140129a.htm (sha256 `693f1c3d951cb33e210ecf7dd7e011843801ce614f45afa4caba9ba7824fb164`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `reaffirm-of`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-29. `20121024_20121212`

- Previous meeting: 20121024 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20121024a.htm (sha256 `6f3fcc35f56e1db8a8e2d076b6ba6d5300f5d276972750925e192629cad76ab1`)
- Next meeting: 20121212 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20121212a.htm (sha256 `341feb26fdaf3e930874edbb498ca13bfd5d610eeb3130d0d5a40419da3aa561`)
- Next statement's own action verb: `keep` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-30. `20250129_20250319`

- Previous meeting: 20250129 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20250129a.htm (sha256 `83ad3a2880375cd1c2323bb63e5c50cd5fc0a1413cdb156ff7102ee296f14cbb`)
- Next meeting: 20250319 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20250319a.htm (sha256 `ac1009bcbddd9b0204e72dc755ed31e950ab835af4017fffde473e204c069449`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `verb`; announced range: `4-1/4 to 4-1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-31. `20231213_20240131`

- Previous meeting: 20231213 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20231213a.htm (sha256 `40c68afb9cf936b29a00f077468a814328299c566093eaed9578fee4fa2a9de8`)
- Next meeting: 20240131 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20240131a.htm (sha256 `b97ad7e3cc65d78f42dd7c459a176adafb038143177ce544d640296c36cdea73`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `verb`; announced range: `5-1/4 to 5-1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-32. `20140319_20140430`

- Previous meeting: 20140319 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20140319a.htm (sha256 `92d0ecfed5533785c904115be57de5a3c3f67c73932085433173c7bdcefd9480`)
- Next meeting: 20140430 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20140430a.htm (sha256 `64fb61e70d6731fdc636973f1c6a57ee069e8bc05cfe19b55b0dacfaec834bd0`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `maintain-current`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-33. `20190320_20190501`

- Previous meeting: 20190320 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20190320a.htm (sha256 `186cb96852bcb72fc968d31ee05349dd4c984540ef767931b0ceb2679b1af6a7`)
- Next meeting: 20190501 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20190501a.htm (sha256 `658c0e8785bee64abd980b8bf3cdd595d13a13ea1153de70e36152e3f9bcd25d`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `verb`; announced range: `2-1/4 to 2-1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-34. `20100428_20100623`

- Previous meeting: 20100428 — https://www.federalreserve.gov/newsevents/press/monetary/20100428a.htm (sha256 `81ac0d8b98921581a94500da4900839d65d79776a8d967835438de5f90ff98bf`)
- Next meeting: 20100623 — https://www.federalreserve.gov/newsevents/press/monetary/20100623a.htm (sha256 `fc19b88fa89dca3deb0b1cec2c4b3ade2145dd484b46761c162d0eae48cbb51c`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `will-maintain`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-35. `20150729_20150917`

- Previous meeting: 20150729 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20150729a.htm (sha256 `8c975096f430eeeca51190deebe331ab8b21abd81cb130c8b1f7795b6a3beb98`)
- Next meeting: 20150917 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20150917a.htm (sha256 `030957e7f9fceca535180eb882ffbcb5bb9378060cee1bd38cb927393913e2b7`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `reaffirm-current`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-36. `20160427_20160615`

- Previous meeting: 20160427 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20160427a.htm (sha256 `3b8e69eb3d635ba66c7c41d8d605e98ff14aeec43df5a3f0c1cf942bb9ab3f83`)
- Next meeting: 20160615 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20160615a.htm (sha256 `1350f25351209ba9be0ef5b5f2233350be38162565a05125d7a72c36a856a660`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `verb`; announced range: `1/4 to 1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-37. `20210317_20210428`

- Previous meeting: 20210317 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20210317a.htm (sha256 `3c6d197b336b0f9463d58557d5f2437d979dfab081caf2dda09b43341cf29235`)
- Next meeting: 20210428 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20210428a.htm (sha256 `e4473c10cd19d66dc78b06855a73844b31f54e5472abdca65c0b0820ce901a48`)
- Next statement's own action verb: `keep` → label `HOLD`
- Extraction method: `verb`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-38. `20240131_20240320`

- Previous meeting: 20240131 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20240131a.htm (sha256 `b97ad7e3cc65d78f42dd7c459a176adafb038143177ce544d640296c36cdea73`)
- Next meeting: 20240320 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20240320a.htm (sha256 `3142be71341a9a7fbfb14722d29350f67efe34e56ea8252782de37990596078d`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `verb`; announced range: `5-1/4 to 5-1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-39. `20150429_20150617`

- Previous meeting: 20150429 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20150429a.htm (sha256 `f04ecbdef31c329924fd28233b13b7a8ac10bb5b946f3321bd07ab57ee46992a`)
- Next meeting: 20150617 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20150617a.htm (sha256 `9dc68f1b61efa76692865cd2ca44617711f8ce69a91976fbb7d25029348bcbba`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `reaffirm-current`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### HOLD-40. `20090812_20090923`

- Previous meeting: 20090812 — https://www.federalreserve.gov/newsevents/press/monetary/20090812a.htm (sha256 `fa8bc659b9fb1550da93098890ebd22d8fd03d35ed8bdc7d1d1893df39ac09a0`)
- Next meeting: 20090923 — https://www.federalreserve.gov/newsevents/press/monetary/20090923a.htm (sha256 `12bf7126f177f5b246480763b7401bf69bd02cc20c3a3f667d7041cc130190c4`)
- Next statement's own action verb: `maintain` → label `HOLD`
- Extraction method: `will-maintain`; announced range: `0 to 1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):
