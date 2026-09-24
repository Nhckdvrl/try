# VitaminC zero-model triplet audit (v1)

- date: 2026-09-25
- criteria (pre-registered before download): `results/audits/vitaminc_triplet_audit_criteria_v1.md`
- source: tals/vitaminc @ `be6febb761b0b2807687e61e0b5282e459df2fa0` (0 model calls)
- verdict: **CLEAN**

## A. Purity
- rows total 488904 (train/dev/test), revision_type values: {'real': 325724, 'synthetic': 163180}
- real rows 325724; malformed dropped 0 (0.0000%) -> A1 PASS
- FEVER_id leaks among kept: 0 (0.0000%) -> A2 pass

## B. Volume
- **N_SR = 92764** (by split: {'train': 70911, 'dev': 11978, 'test': 9875}); canonical 1S+1R 92735, anomalous 29, same-text contradictions 1
- bands: kill < 300, marginal < 1000 -> pass

## C. Minimality (canonical SR-pairs)
- median similarity **0.9333** (p10 0.8148, min 0.0)
- bands: kill < 0.8, marginal < 0.9 -> pass

## D. Structure (reported)
- cases 106954 (straddling splits 0), (case, claim) groups 163485
- evidences per case hist: {1: 1302, 2: 105652}
- rows per group hist: {1: 1312, 2: 162140, 4: 33}
- evidences per group hist: {1: 1312, 2: 162173}
- label marginal (kept rows): {'SUPPORTS': 163272, 'NOT ENOUGH INFO': 69291, 'REFUTES': 93161}
- distinct claim texts among SR-pairs 91240, reused across cases 1254
- template-claim rate 0.4642 (regex `(less than|more than|fewer than|over|under|at least|at most)\b[^.]{0,20}\d`), pages 15029, top-page share 0.0264
- duplicate (claim, evidence, label) rows 1609
- claim words p50/p90 13/22;
  evidence-pair words p50/p90 53/90

## Verdict rule
KILL > CLEAN > MARGINAL; KILL if A1/A2 fail or N_SR<300 or median sim<0.80; CLEAN if N_SR>=1000 and median sim>=0.90; else MARGINAL
