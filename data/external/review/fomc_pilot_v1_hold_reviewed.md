# FOMC HOLD candidate queue — pilot v1 human review

**Review date:** 2026-08-30  
**Model outputs inspected during this review:** none.  
**Candidate source:** `data/external/review/fomc_pilot_v1_hold_candidates.md`  
**Protocol:** review the frozen deterministic HOLD queue top-to-bottom. ACCEPT means all four registered gates jointly pass: scheduled+adjacency provenance, statement/source identity against the pinned manifest, correct next-statement action label, and no extraction/source mismatch. The HOLD queue was already mechanically prefiltered against the frozen CHANGE-reserved meetings; within-HOLD meeting collisions are handled by `freeze-hold`, not by changing human decisions.

Review stopped as soon as 12 meeting-disjoint ACCEPTs were reached. `HOLD-1` through `HOLD-12` are mutually meeting-disjoint and all passed the four human gates, so quota is reached exactly at `HOLD-12`. Queue tail `HOLD-13+` remains unreviewed.

### HOLD-1. `20140129_20140319`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### HOLD-2. `20181219_20190130`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### HOLD-3. `20150318_20150429`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### HOLD-4. `20110622_20110809`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### HOLD-5. `20100623_20100810`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### HOLD-6. `20140730_20140917`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### HOLD-7. `20211103_20211215`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### HOLD-8. `20170614_20170726`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### HOLD-9. `20240320_20240501`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### HOLD-10. `20111213_20120125`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### HOLD-11. `20130619_20130731`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### HOLD-12. `20230920_20231101`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`
