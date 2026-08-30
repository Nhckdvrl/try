# FOMC CHANGE candidate queue — pilot v1 human review

**Review date:** 2026-08-30  
**Model outputs inspected during this review:** none.  
**Candidate source:** `data/external/review/fomc_pilot_v1_change_candidates.md`  
**Protocol:** review the frozen deterministic CHANGE queue top-to-bottom. ACCEPT means all four registered gates jointly pass: scheduled+adjacency provenance, statement/source identity against the pinned manifest, correct next-statement action label, and no extraction/source mismatch. A valid ACCEPT may still be mechanically collision-skipped by `freeze-change`; collision is not a human-rejection reason.

Review stopped as soon as the prefix contained 12 meeting-disjoint ACCEPTs under the frozen walk. All reviewed candidates below passed the four human gates. `CHANGE-7` and `CHANGE-11` are valid ACCEPTs but are expected to be mechanically collision-skipped because they reuse meetings already reserved by earlier ACCEPTs. The 12 selected CHANGE units should therefore be reached at `CHANGE-14`. Queue tail `CHANGE-15+` remains unreviewed.

### CHANGE-1. `20220615_20220727`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### CHANGE-2. `20230614_20230726`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### CHANGE-3. `20170201_20170315`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### CHANGE-4. `20180801_20180926`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### CHANGE-5. `20230322_20230503`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### CHANGE-6. `20171101_20171213`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### CHANGE-7. `20220504_20220615`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### CHANGE-8. `20241107_20241218`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### CHANGE-9. `20251029_20251210`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### CHANGE-10. `20220126_20220316`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### CHANGE-11. `20240918_20241107`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### CHANGE-12. `20151028_20151216`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### CHANGE-13. `20250730_20250917`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### CHANGE-14. `20240731_20240918`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`
