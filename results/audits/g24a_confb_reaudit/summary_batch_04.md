# Blind re-audit summary — batch 04 (`g24a_confb_reaudit`)

File: `results/audits/g24a_confb_reaudit/audit_batch_04.jsonl`

Method: each of the 50 claim/evidence pairs was judged independently from its own text only (no repository files, metadata, prior reviews, or model outputs consulted). A pair counts as valid only if one evidence genuinely supports the claim and the other genuinely contradicts it; omission or mere non-mention was treated as `neutral`, not `refute`.

## Counts

| Metric | Value |
|---|---|
| Records written | 50 |
| Unique IDs | 50 (verified; no duplicates) |
| IDs matching input batch order/set | 50 / 50 |
| `pair_valid = true` | 47 |
| `pair_valid = false` | 3 |

### Relations

| | support | refute | neutral | ambiguous |
|---|---|---|---|---|
| `relation_a` | 21 | 27 | 1 | 1 |
| `relation_b` | 28 | 20 | 1 | 1 |

### Naturalness

| natural | awkward | broken |
|---|---|---|
| 41 | 8 | 1 |

## Invalid pairs (`pair_valid = false`)

| id | reason |
|---|---|
| `g24cfb_224` | evidence_a only lists other broadcasters and omits Al-Hayat — omission, not contradiction (`neutral`); only evidence_b supports. |
| `g24cfb_231` | evidence_b says disciple of "Bang"; Bang is Silver Fang, i.e. apparently the same master as "Fang", so it does not genuinely contradict (`ambiguous`). |
| `g24cfb_245` | evidence_a is hedged ("may be a Guru in a Gurukul") and never identifies the claim's referent; evidence_b names a Pathsala without denying a Gurukul role (`ambiguous` / `neutral`). |

## Flagged text quality

- **broken (1):** `g24cfb_233` — injected URL/query fragment (`? detail=writerid & page=1 …`) between name and birth date in both evidence strings.
- **awkward (8):**
  - `g24cfb_236` — typo "eigth-wealthiest" in evidence_a.
  - `g24cfb_245` — hedged wording; generic "He"/"Pandit" referent unclear.
  - `g24cfb_246` — garbled name fragment "( I. Juan Weiner )" in evidence_a.
  - `g24cfb_248` — both texts truncated mid section-header ("==NBA re" / "==NB").
  - `g24cfb_253` — clumsy claim phrasing ("after the age of 49 years, after 2001"); evidence omits the film title.
  - `g24cfb_258` — evidence_a scale internally inconsistent ("four-and-a-half out of four stars"), though it matches the claim.
  - `g24cfb_281` — claim typo "New York Jest" (Jets).
  - `g24cfb_297` — claim garbles the verb "band" into a noun ("the band was under four evacuees").
- **Missing/shifted referents noted in `issue` (relations still judged):** `g24cfb_229` (no country named, "there"), `g24cfb_256` (claim says Los Angeles, evidence gives metro-area population), `g24cfb_287` (claim's "Tremaine" never appears in evidence), plus minor subject/film-title omissions in fragments (`g24cfb_237`, `g24cfb_253`, `g24cfb_255`, `g24cfb_262`).

## Borderline judgments worth review

- `g24cfb_228` — evidence_a's "up to £1 billion" (2009) implicitly exceeds the claimed £440m ceiling: judged `refute`, but no explicit range is stated.
- `g24cfb_237` — evidence_a's September 2018 release judged `refute` for "summer 2018" (borderline only up to the ~22 Sep equinox).
- `g24cfb_232` — evidence counts deaths outside *mainland* China while the claim says *outside China* (Hong Kong counting nuance); intended directions kept.
- `g24cfb_275` — evidence_b's "on loan from Boca Juniors" conflicts with the claim under a current-club reading; loan nuance noted.

No original data files were modified and no replacement pairs were selected.
