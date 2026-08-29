# BTF-3 confirmatory v1 — human review ledger

**Review date:** 2026-08-30  
**Model outputs inspected during this review:** none.  
**Candidate source:** `data/external/review/btf3_confirmatory_v1_candidates.md`  
**Protocol:** walk each frozen realized-outcome queue in order and stop when the first 32 ACCEPTs are reached. ACCEPT means all four registered gates pass: pre-cutoff integrity, realized-outcome validity, exact-packet factual validity, and unambiguous resolution criteria. REJECT/UNSURE permanently consumes that queue slot; no source text or later packet is repaired by hand.

This ledger intentionally records only the prefix actually reviewed to reach quota. The unused queue tail remains unreviewed and must not be treated as accepted or rejected.

## Outcome

- Realized NO: reviewed NO-1 through NO-36; **32 ACCEPT / 4 REJECT / 0 UNSURE**. Quota reached at NO-36.
- Realized YES: reviewed YES-1 through YES-41; **32 ACCEPT / 9 REJECT / 0 UNSURE**. Quota reached at YES-41.
- Final eligible confirmatory set implied by this review: **64 fresh question_ids, 32 NO / 32 YES**.
- This review ledger does **not** itself freeze the final JSONL and does **not** authorize a model run. `scripts/freeze_btf3_confirmatory.py` and the registered audit/freeze steps still need to be run separately.

## Realized NO reviewed prefix

### NO-1. `f8a6fd09-c315-50e3-9383-da38927ac12d`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The packet is internally ambiguous about whether pre-existing reconciliation funding counts toward the required full-year DHS/ICE/Border Patrol funding, while the key regular appropriations law was signed before the stated qualifying window; criteria/packet alignment is not clean enough for confirmatory use.

### NO-2. `985a9576-773a-5122-b880-d70cd192f452`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-3. `85389e81-ba1e-521c-b039-c7985ba14539`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-4. `71ff25b3-b13b-5b64-ba88-7eb29725956f`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-5. `1076a71a-98c2-50b3-a429-446bdd0a1219`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-6. `a4bcf029-c92f-50ff-bb5f-ef40c610daf9`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-7. `d9696e36-8d71-5946-ba3c-8c8f4fed03ee`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-8. `fa200512-4bb4-5b4b-ad70-94d68896f0a5`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-9. `297aef8b-6fa0-5ee0-888f-0a0774b1661a`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-10. `0d27e684-1770-578a-98d6-7fa0c753fe08`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-11. `309c0d3e-ea2b-5913-98c0-50772902b585`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-12. `91f14139-ce9a-5d28-b703-a1c1c06b48f4`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-13. `02886efb-22f2-5622-8bc8-a78d909755ab`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-14. `0851f82c-aabd-57f0-abbb-4a23f99963c2`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-15. `dfa437fb-3ad7-5911-81a1-44e7cc139529`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The negative adjudication of a Turkish ground incursion in SDF-held Hasakah relies mainly on Wikipedia/SDF-aligned reporting plus absence-of-report reasoning, not the registered two-source international-news standard; the exact packet is not sufficiently well-grounded for this high-stakes territorial claim.

### NO-16. `069fb1fe-06a9-5ded-8358-e2b928395697`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-17. `ff6e9a2c-091f-5eae-a9a1-1577928b6773`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-18. `bb016b0a-3c20-574a-a5a1-c4069fcb7fe2`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-19. `b391d13e-3bcb-5d84-9bb2-9589ae6511be`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-20. `72f98c43-a74c-5082-a4b9-c7f0283f4668`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-21. `7f5d5d22-2242-5bd2-bdd4-52561369221a`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-22. `bc22ea66-ffbb-5ada-b4f3-bcb1d807a21a`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-23. `4fe12714-226c-5680-8c3b-a4745fbc2bd2`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-24. `6391fee9-e6c1-5fa7-8631-2c68c0992883`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-25. `f0d071cf-f3d0-5b3b-8e35-1a84f4deb16a`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The AUSSOM negative depends on ambiguous authorized-versus-deployed troop baselines and broad absence-of-announcement reasoning across five countries rather than a definitive per-country official status record; the exact packet is not strong enough to lock the factual gate.

### NO-26. `97b7a6bc-9b95-5b72-9d44-b68293be5063`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-27. `8f1436c8-ba9b-52b7-81a3-2a7af0d0ef4a`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-28. `b17b9a62-68a4-5e02-b9ca-bb87b54dfa45`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-29. `c4a47c34-2572-512d-850a-c329bd0a14b7`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-30. `f167e83b-1f1e-52de-b01d-2b05598fc474`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-31. `d7a1ae25-6951-51ae-b118-189a4c81c15f`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-32. `69db632e-fd4d-571b-9447-9c6841c4c537`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-33. `b22bf1df-08f3-53f0-b37e-45125d5019fc`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-34. `62be25b5-7b18-56dc-a644-b5402a0d6aca`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### NO-35. `8e0b857a-9cb2-55d0-87df-06b7105267c8`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The IAEA-strike negative packet itself acknowledges that an automated pass relied on unverified secondary reporting and does not provide a direct official IAEA record establishing the claimed negative; exact-packet factual grounding fails closed.

### NO-36. `25a5ce74-d39c-5da1-bcee-003609679986`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

## Realized YES reviewed prefix

### YES-1. `10a0455b-c9fc-58f0-87e8-22172f97c898`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The packet treats the May 8 third reading of an enabling special act setting a budget cap as the requested “special defense budget bill,” while separately noting a later first-batch budget bill; that act-versus-budget distinction makes the resolution criterion materially ambiguous.

### YES-2. `38cef1e5-68c6-5c07-9b49-5d1412ec8476`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-3. `c4eaa5f2-042c-52d9-921c-fff5cd40f9b1`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-4. `1ecfe907-7a50-5127-ad5b-7da4af090af0`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-5. `f3c346a9-8b98-51a7-b357-b1ec25db0060`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-6. `3fd22636-7d1e-537d-816c-bb3603f02e72`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-7. `d9d76db9-8595-57de-96b7-45cff90786ef`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-8. `acab71ad-031c-53fd-85e2-9743575d627d`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-9. `15422167-f6bd-50d5-96db-943773bc45e5`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The registered source rule permits secondary reporting only if the IDWR site is unavailable, but the packet says the official site was reachable yet simply did not show the May entry and then substitutes news reports; the source-validity condition is not met as written.

### YES-10. `442a44a9-fcca-5d4d-b31d-87a4b40ff000`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-11. `c8bfecd4-d906-5331-b98c-62a73ed87f14`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-12. `658805d0-23e8-5df3-a2f1-f618addff9ae`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-13. `a27193ba-4066-52fc-829e-7b3702351118`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The criteria require a qualifying law/ordinance to be published in the state official gazette, but the packet establishes parliamentary passage/press reporting for Niedersachsen and Hamburg without the required gazette-publication evidence; it silently treats passage as enactment.

### YES-14. `a6287619-a64c-5fa5-9f22-88ecb28c8f07`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-15. `4dab8b55-b59a-51e5-9c96-88fb9f245af7`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-16. `daf08eba-d005-5c37-a9a5-561338ce6768`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-17. `24ee233d-c9b2-58a1-99bd-98d9a6d812b4`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-18. `2c0f5892-9b6f-5a01-b5cb-d969eaeb3033`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-19. `36edec34-1405-56ee-99d0-75b8bb922f38`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-20. `d74eb890-70be-58e7-b639-bb99ddb05de6`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-21. `c78c35c2-c526-59f4-a0f8-9c1cb7a9ca12`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The packet resolves a June 1 obligation threshold using AAMC data only through May 15 and then argues that a jump by June 1 is implausible; data that predate the resolution time cannot establish the literal threshold at the deadline.

### YES-22. `adb8e6fb-5f80-5d2b-8773-818a1c7db8e6`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The “unanimous” criteria contradict themselves about whether a separate concurrence defeats unanimity; because Justice Thomas filed a concurrence, the two readings yield different classifications and the criterion is not unambiguous.

### YES-23. `97a98e4a-2bbf-58ea-99cb-b698f1612af5`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-24. `6c85961f-c812-5dee-a6ae-0d2985e879a4`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-25. `6b8f801e-30ec-5a81-b2c5-0b88c6c97ce7`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-26. `e54a0372-5d92-57ab-9c83-46f38c02bc0e`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-27. `1177ed01-9dc4-594d-9656-3eac4d014d42`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-28. `9e9cf5a3-dfab-5943-b397-54498888c051`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-29. `4e8b4e0d-1cb7-5305-a840-4665db0b29ac`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-30. `cfb43147-d9d2-5bd9-903f-f449e9a5aecf`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-31. `d75175b0-3f42-5ba9-a8c5-9f437b449e05`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: “An increase ... beyond the 206,000 bpd already approved for May” can mean either any June level above May or a June increment exceeding 206,000 bpd; the packet chooses the former even though the announced June increment was 188,000 bpd, so the criterion admits materially different readings.

### YES-32. `9ec5b3fa-b926-5bcc-b26f-49c3280202be`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-33. `1ba30f57-cc76-594f-b992-b6e654eac5cb`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-34. `11be9241-3523-5920-aeff-adafe8e61320`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The packet says Gabbard’s resignation was effective June 30 and that she remained DNI until then, but also says an acting DNI replaced her on June 2 and the current ODNI page lists that replacement; the timeline is internally inconsistent.

### YES-35. `4a21678b-b6de-5b2a-8dd1-5e972372447d`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-36. `6fc68401-489f-553c-b103-de9df602be49`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-37. `87d5e6a2-d228-55a7-8516-58dcf6412493`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The packet does not actually supply the registered official White House/State text or two qualifying wire-service reports; it relies on NBC/CNN/Fortune/Britannica and two inconsistent signing narratives, so the exact agreement claim is not grounded to the source standard the item itself requires.

### YES-38. `e7bc952c-31bb-5b53-ba45-9279b608efb1`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: The guilty-verdict packet relies on Just Stop Oil, a local outlet, and an advocacy outlet rather than an official court record or the mainstream credible-news class named by the criteria; the factual outcome may be plausible, but this packet is not sufficiently source-secure for confirmatory inclusion.

### YES-39. `444b8215-8b25-5b43-9625-2de4476e49b7`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-40. `0559055f-bb51-5d22-897a-603ee0a3a265`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`

### YES-41. `97b85a7c-7b00-5c52-9df4-3fa2ebf7f394`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`
