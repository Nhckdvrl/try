# FOMC CHANGE candidate queue — pilot v1

> Fixed deterministic order (seed 20260829). Review top-to-bottom until 12 ACCEPTs that are also meeting-disjoint from earlier selections are reached. A REJECT/UNSURE consumes its queue slot permanently and is never resampled or reconsidered. Never reject for salience/fame -- only the four gates below.

For each unit, tick exactly one of ACCEPT / REJECT / UNSURE for all four gates jointly (all four must hold to ACCEPT). On REJECT or UNSURE, write exactly one line giving the reason.

### CHANGE-1. `20220615_20220727`

- Previous meeting: 20220615 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20220615a.htm (sha256 `0290785119572e7e8f66997c74a3c3f1257ca914dce7ae8db9ae351df2c2ec52`)
- Next meeting: 20220727 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20220727a.htm (sha256 `91e79307c10026bf9095af2c962c254a61eac51243395fd9e2e26d79eecaaccc`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `2-1/4 to 2-1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-2. `20230614_20230726`

- Previous meeting: 20230614 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20230614a.htm (sha256 `09106afb6d90dabb297545e3ca8d46c8818908c8ea0fbf0ee54715918a899308`)
- Next meeting: 20230726 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20230726a.htm (sha256 `aae263315a0d320ba6545a4f8c46cad3c5b747dc5577da2b2a4c6590b5d2628d`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `5-1/4 to 5-1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-3. `20170201_20170315`

- Previous meeting: 20170201 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20170201a.htm (sha256 `e89d076f076b955aec403deaeae1676b5851507d5fcdf14dee35953170ec8151`)
- Next meeting: 20170315 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20170315a.htm (sha256 `2286e8661cf6ca4b061166ad49a4a2e027b7b87c98263ff38b48111fd0dcf21e`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `3/4 to 1`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-4. `20180801_20180926`

- Previous meeting: 20180801 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20180801a.htm (sha256 `e3f70dc0c396f0752d39ed603324ee7f83edda5bd3e505a9ca2b2159cfb442f9`)
- Next meeting: 20180926 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20180926a.htm (sha256 `af362b4f072727f3d4afbf64445df06c5b9366ddfb918167c2eb282369c2dad4`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `2 to 2-1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-5. `20230322_20230503`

- Previous meeting: 20230322 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20230322a.htm (sha256 `e53ab2902ef0fe8a6c635be93daff56362aa5ef11906821ca22062328a2d486c`)
- Next meeting: 20230503 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20230503a.htm (sha256 `63ca1aa7fd343b477617141bc4555dec77ad3f6da07d13ae69d698d18b8814a5`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `5 to 5-1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-6. `20171101_20171213`

- Previous meeting: 20171101 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20171101a.htm (sha256 `51b5caf25c6c4ff9813a58a8609cc159718e3f802f67df10e8ca2432925f7e83`)
- Next meeting: 20171213 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20171213a.htm (sha256 `4a50b813d08cbda7adfc9ae021a461e76f0545fc2c9ed201ddf3426aba8c33be`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `1-1/4 to 1‑1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-7. `20220504_20220615`

- Previous meeting: 20220504 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20220504a.htm (sha256 `fc40506e1e896674d9ef97cd180d8b675179318b9c0d1598bf0bc8e3957c8d25`)
- Next meeting: 20220615 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20220615a.htm (sha256 `0290785119572e7e8f66997c74a3c3f1257ca914dce7ae8db9ae351df2c2ec52`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `1‑1/2 to 1-3/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-8. `20241107_20241218`

- Previous meeting: 20241107 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20241107a.htm (sha256 `b8d26df574fe8e0b1fd468b7c37b43ece74fed9b95aecb2e89232d9340d0c207`)
- Next meeting: 20241218 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20241218a.htm (sha256 `3ac7a14d4e5b5527abbec5d4e54122875a93561af19b36bb293077c2cbe40e3b`)
- Next statement's own action verb: `lower` → label `CHANGE`
- Extraction method: `verb`; announced range: `4-1/4 to 4-1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-9. `20251029_20251210`

- Previous meeting: 20251029 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20251029a.htm (sha256 `392110ee5037e236d21a423ce1c6541bbb2d0369a615a0bdab11169a0bfac71c`)
- Next meeting: 20251210 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20251210a.htm (sha256 `84812f39f054b5c91821b9e7456aeb5e2ab39f017d6c05cbcb68ee67108dc56d`)
- Next statement's own action verb: `lower` → label `CHANGE`
- Extraction method: `verb`; announced range: `3-1/2 to 3‑3/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-10. `20220126_20220316`

- Previous meeting: 20220126 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20220126a.htm (sha256 `606a27d9a318875cec833c47c78e7d576c30e9cc10b405f561471df31666e2d8`)
- Next meeting: 20220316 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20220316a.htm (sha256 `9ab15e990fdcdc31b8ca7af06ef9bd15e29937c789e575a1c58d95f43e43403c`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `1/4 to 1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-11. `20240918_20241107`

- Previous meeting: 20240918 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20240918a.htm (sha256 `125d47cb5570f96d76ddaaea679e55726c9d42785a3bbb568f828188e1aef005`)
- Next meeting: 20241107 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20241107a.htm (sha256 `b8d26df574fe8e0b1fd468b7c37b43ece74fed9b95aecb2e89232d9340d0c207`)
- Next statement's own action verb: `lower` → label `CHANGE`
- Extraction method: `verb`; announced range: `4-1/2 to 4-3/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-12. `20151028_20151216`

- Previous meeting: 20151028 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20151028a.htm (sha256 `051005ecbdc753dba81cb99c9b35278b85187e5832fe7403600dc133851340f2`)
- Next meeting: 20151216 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20151216a.htm (sha256 `639729589733f3603e19986704362f3516b21a2721e9bf74df3e085f79965882`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `1/4 to 1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-13. `20250730_20250917`

- Previous meeting: 20250730 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20250730a.htm (sha256 `25a1a8510b05673bed5694cf4bd932ec65cb2de53dbc84339fbce8e3240b6fdb`)
- Next meeting: 20250917 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20250917a.htm (sha256 `a0509ab17f8a64fd4e5574d9d7f62587c06eca627b1c26a319597ce38a9fd2af`)
- Next statement's own action verb: `lower` → label `CHANGE`
- Extraction method: `verb`; announced range: `4 to 4‑1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-14. `20240731_20240918`

- Previous meeting: 20240731 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20240731a.htm (sha256 `c69c3e663104f53b53ae6070636a5e5504a3d03f3ea43ea2e40704ebadbe4ff8`)
- Next meeting: 20240918 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20240918a.htm (sha256 `125d47cb5570f96d76ddaaea679e55726c9d42785a3bbb568f828188e1aef005`)
- Next statement's own action verb: `lower` → label `CHANGE`
- Extraction method: `verb`; announced range: `4-3/4 to 5`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-15. `20190619_20190731`

- Previous meeting: 20190619 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20190619a.htm (sha256 `e7213c142339490eaf8016c36cea47b36a26a119460d3b8f9bd812f83806b498`)
- Next meeting: 20190731 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20190731a.htm (sha256 `087a75e36145dcc32ca1eb24d2f3f8b5d58b88ef4461f93e505ec09832768468`)
- Next statement's own action verb: `lower` → label `CHANGE`
- Extraction method: `verb`; announced range: `2 to 2-1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-16. `20221214_20230201`

- Previous meeting: 20221214 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20221214a.htm (sha256 `3ec6ec16f769c3b200c22781cd746bd339f27a9ea0207f1fad76d1801cb18eb9`)
- Next meeting: 20230201 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20230201a.htm (sha256 `8faa3ad7f99d48112a0c1e49205c5df9486d274ec3f99ed2ffb32c0e2687e9b5`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `4-1/2 to 4-3/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-17. `20161102_20161214`

- Previous meeting: 20161102 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20161102a.htm (sha256 `6f8a167d618451ed073aa1d710c1d0f10ab676ef4bbf486c6ef00e3c3ded938b`)
- Next meeting: 20161214 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20161214a.htm (sha256 `2c20137b6687c3eae0819cf6071715ceb5d4bf17db4981f62c6939e8f976f817`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `1/2 to 3/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-18. `20230201_20230322`

- Previous meeting: 20230201 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20230201a.htm (sha256 `8faa3ad7f99d48112a0c1e49205c5df9486d274ec3f99ed2ffb32c0e2687e9b5`)
- Next meeting: 20230322 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20230322a.htm (sha256 `e53ab2902ef0fe8a6c635be93daff56362aa5ef11906821ca22062328a2d486c`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `4-3/4 to 5`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-19. `20220727_20220921`

- Previous meeting: 20220727 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20220727a.htm (sha256 `91e79307c10026bf9095af2c962c254a61eac51243395fd9e2e26d79eecaaccc`)
- Next meeting: 20220921 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20220921a.htm (sha256 `944df1fd9c8eea3ff43726d3707e346eabbe7519e1b0173ccf08e8fefda8e488`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `3 to 3-1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-20. `20221102_20221214`

- Previous meeting: 20221102 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20221102a.htm (sha256 `dd3dd20951dc2adaedfbd2e14caddc73af86320a5e2586a284f3e32b90d22d7d`)
- Next meeting: 20221214 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20221214a.htm (sha256 `3ec6ec16f769c3b200c22781cd746bd339f27a9ea0207f1fad76d1801cb18eb9`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `4-1/4 to 4-1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-21. `20220316_20220504`

- Previous meeting: 20220316 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20220316a.htm (sha256 `9ab15e990fdcdc31b8ca7af06ef9bd15e29937c789e575a1c58d95f43e43403c`)
- Next meeting: 20220504 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20220504a.htm (sha256 `fc40506e1e896674d9ef97cd180d8b675179318b9c0d1598bf0bc8e3957c8d25`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `3/4 to 1`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-22. `20190918_20191030`

- Previous meeting: 20190918 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20190918a.htm (sha256 `261bce8ca3f07c1d713c8af2696e474ae0ba3ff94f75ec4bc4176b61ea613670`)
- Next meeting: 20191030 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20191030a.htm (sha256 `ee37f9fcf28607e6fe3b742646dadcabd1956b7c7a07b2f87c411bab36becaea`)
- Next statement's own action verb: `lower` → label `CHANGE`
- Extraction method: `verb`; announced range: `1-1/2 to 1-3/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-23. `20250917_20251029`

- Previous meeting: 20250917 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20250917a.htm (sha256 `a0509ab17f8a64fd4e5574d9d7f62587c06eca627b1c26a319597ce38a9fd2af`)
- Next meeting: 20251029 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20251029a.htm (sha256 `392110ee5037e236d21a423ce1c6541bbb2d0369a615a0bdab11169a0bfac71c`)
- Next statement's own action verb: `lower` → label `CHANGE`
- Extraction method: `verb`; announced range: `3-3/4 to 4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-24. `20180131_20180321`

- Previous meeting: 20180131 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20180131a.htm (sha256 `e9a5fcbbe8ebae1b5ca9be93c33036c2b403210b78fbfbbb63db629d1c7a6a38`)
- Next meeting: 20180321 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20180321a.htm (sha256 `f59976dda226b3ded39824f2263cbc3edd4cda8a830d1615bca63144589f904f`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `1-1/2 to 1-3/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-25. `20190731_20190918`

- Previous meeting: 20190731 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20190731a.htm (sha256 `087a75e36145dcc32ca1eb24d2f3f8b5d58b88ef4461f93e505ec09832768468`)
- Next meeting: 20190918 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20190918a.htm (sha256 `261bce8ca3f07c1d713c8af2696e474ae0ba3ff94f75ec4bc4176b61ea613670`)
- Next statement's own action verb: `lower` → label `CHANGE`
- Extraction method: `verb`; announced range: `1-3/4 to 2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-26. `20170503_20170614`

- Previous meeting: 20170503 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20170503a.htm (sha256 `3a8b295945b418bf105db71dbc6f0a323619969bdd242c006b9337bbbfb3ff62`)
- Next meeting: 20170614 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20170614a.htm (sha256 `a769b065dca8eb7e913f78ee02b153d7aef80f23bf7346a372662b1143dbdfc3`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `1 to 1-1/4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-27. `20181108_20181219`

- Previous meeting: 20181108 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20181108a.htm (sha256 `b7285ccc4a010f7c93774eb41680ba14c0be7223cab91e426b1a5b74918eca5c`)
- Next meeting: 20181219 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20181219a.htm (sha256 `e7ebe302078abf08c70681490bc01407afe4c7e874eb0875c6abd46fa98b2ee6`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `2-1/4 to 2‑1/2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-28. `20220921_20221102`

- Previous meeting: 20220921 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20220921a.htm (sha256 `944df1fd9c8eea3ff43726d3707e346eabbe7519e1b0173ccf08e8fefda8e488`)
- Next meeting: 20221102 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20221102a.htm (sha256 `dd3dd20951dc2adaedfbd2e14caddc73af86320a5e2586a284f3e32b90d22d7d`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `3-3/4 to 4`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### CHANGE-29. `20180502_20180613`

- Previous meeting: 20180502 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20180502a.htm (sha256 `9bd776569518dddeded9d0f5ca4210da547ba00b6b1b93842beaeacf0e1bb045`)
- Next meeting: 20180613 — https://www.federalreserve.gov/newsevents/pressreleases/monetary20180613a.htm (sha256 `afe219ea7149c5d37ea659c87a66624b5cf2730cc2190d679d841d062b31ba22`)
- Next statement's own action verb: `raise` → label `CHANGE`
- Extraction method: `verb`; announced range: `1-3/4 to 2`

**Gates (all four must hold to ACCEPT):**
- [ ] scheduled + adjacency provenance correct (both meetings genuinely scheduled and calendar-adjacent per the pinned manifest)
- [ ] previous/next statement text matches the pinned SHA-256 (open the statement URL and confirm)
- [ ] next statement's action label (CHANGE/HOLD) correctly extracted
- [ ] no extraction/source mismatch between the two statements

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):
