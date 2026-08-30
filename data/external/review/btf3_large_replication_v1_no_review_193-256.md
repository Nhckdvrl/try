# btf3_large_replication_v1 — realized NO review chunk NO-193–NO-256

> Display chunk of the immutable queue (`btf3_large_replication_v1_no_queue.json`). Review strictly top-to-bottom; stop only when this bucket reaches 128 ACCEPTs overall. Do not skip ahead, reorder, or prefer better-looking questions. A REJECT/UNSURE permanently consumes its queue slot and is never resampled, re-reviewed, or hand-repaired.

All four gates must hold to ACCEPT. On REJECT or UNSURE write exactly one line of reason.

### NO-193. `085d5794-4695-59fe-8b08-4447ba24ebe5`

- Present date: `2026-05-14 04:32:07.197065`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Knesset pass the bill to split the role of the Attorney General by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the "[Splitting the Post of the Attorney General Bill, 2025](https://m.knesset.gov.il/en/news/pressreleases/pages/press291025b.aspx)" (or any substantively equivalent successor bill that splits the role of the [Attorney General of Israel](https://en.wikipedia.org/wiki/Attorney_General_of_Israel) into multiple positions) passes its third reading (Kri'ah Shlishit / קריאה שלישית) in the Knesset Plenum on or after May 12, 2026 (00:00 IDT) and on or before July 1, 2026 (23:59 IDT).

The question resolves **No** if no such bill passes its third reading by July 1, 2026 (23:59 IDT).

"Passing" is defined as the bill receiving a majority vote in its third reading in the Knesset Plenum, which constitutes final legislative approval.

**Resolution source:** The official [Knesset legislation database](https://main.knesset.gov.il/EN/activity/Pages/Legislation.aspx) or official [Knesset press releases](https://m.knesset.gov.il/EN/News/PressReleases/Pages/default.aspx). In the absence of timely updates on these pages, credible reporting from outlets such as [Times of Israel](https://www.timesofisrael.com), [Haaretz](https://www.haaretz.com), or [Jerusalem Post](https://www.jpost.com) may be used.

**Pre-cutoff background**

The Israeli government has been advancing a bill to split the role of the [Attorney General of Israel](https://en.wikipedia.org/wiki/Attorney_General_of_Israel) into three separate positions: a legal adviser to the government, a head of the state prosecution (Prosecutor General), and a representative of the state in legal proceedings. The bill, formally known as the "Splitting the Post of the Attorney General Bill, 2025," passed its preliminary reading in the Knesset Plenum on October 29, 2025 [Knesset Plenum approves in preliminary reading bill to split the post ...](https://m.knesset.gov.il/en/news/pressreleases/pages/press291025b.aspx). It was then referred to the House Committee to determine which committee would prepare it for first reading.

As of May 13, 2026, the Knesset has returned from its six-week spring recess (on May 10, 2026), and lawmakers are continuing work on this legislation as part of a broader legislative blitz of contentious bills [Coalition Prepares Blitz of Controversial Bills Ahead of Election](https://www.jfeed.com/news-israel/knesset-controversial-bills). The bill's passage through second and third readings remains uncertain due to coalition dynamics, including tensions with ultra-Orthodox parties and significant opposition from legal professionals and civil society groups who argue the bill would weaken a key check on executive power. The bill is widely seen as connected to Prime Minister Netanyahu's ongoing legal battles, as the Attorney General plays a central role in criminal prosecutions of public officials.

In the Israeli legislative process, a bill must pass a preliminary reading, first reading, committee deliberation, second reading, and third reading (final vote) in the Knesset Plenum before becoming law. As of May 13, 2026, the bill has passed only the preliminary reading stage.

**Exact later resolution packet**

RESOLUTION: NO (0). No bill splitting the role of the Attorney General passed its third reading (Kri'ah Shlishit) in the Knesset Plenum between May 12, 2026 (00:00 IDT) and July 1, 2026 (23:59 IDT).

EVIDENCE FROM OFFICIAL KNESSET LEGISLATION DATABASE:
- The original "Splitting the Post of the Attorney General Bill, 2025" (הצעת חוק פיצול תפקיד היועץ המשפטי לממשלה, התשפ"ה-2025), Knesset bill page https://main.knesset.gov.il/apps/legislation/main/bills/2226845, did NOT pass a third reading. Its status is "merged with another bill" — it was merged into a broader successor bill, "The Attorney General and Prosecutor General Bill (Appointment, Tenure, Roles and Authorities), 2026" (הצעת חוק היועץ המשפטי לממשלה והתובע הכללי (מינוי, כהונה, תפקידים וסמכויות), התשפ"ו–2026) [6aea40].
- That substantively equivalent successor bill, Knesset bill page https://main.knesset.gov.il/apps/legislation/main/bills/2197909, passed a preliminary reading (Oct 29, 2025) and a first reading (approved anew by the Constitution, Law and Justice Committee on May 25, 2026, and passed the plenum on June 1-2, 2026, by 65-47), but as of July 1, 2026 its status remained "Preparation for second and third reading" (הכנה לקריאה שנייה ושלישית). It never reached, let alone passed, a third reading by the deadline [8f9e39].

CORROBORATING NEWS (permitted outlet):
- Times of Israel article "Legislation to split and weaken role of attorney general passes first Knesset reading" (published June 2, 2026), https://www.timesofisrael.com/legislation-to-split-and-weaken-role-of-attorney-general-passes-first-knesset-reading/, confirms the bill passed ONLY its first reading and was returned to the Constitution, Law and Justice Committee for the two further readings required to become law. It notes the coalition understood the bill might not pass into law before the Knesset disbands for the September–October 2026 elections, expecting to rely on legislative "continuity" in the next Knesset [3a8b5a].

DISAMBIGUATION / POTENTIAL LOOPHOLE ADDRESSED:
- Some search snippets reference a bill passing "second and third readings" by a vote of 62-48 with one abstention. That vote refers to a SEPARATE bill — the death-penalty-for-terrorists bill passed on March 30, 2026 — not the Attorney General bill, and in any case predates the May 12 window. It is not relevant to this question.

CONCLUSION: Within the resolution window (May 12 – July 1, 2026), the AG-splitting legislation (both the original 2025 bill and its substantively equivalent 2026 successor) advanced only through a first reading and remained in committee preparation for second/third readings. No third reading occurred. The question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-194. `02f7fb4a-3be5-5dad-9174-8f4deca650d3`

- Present date: `2026-05-14 04:06:53.340988`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Northern Ireland Troubles Bill receive Third Reading in the House of Commons by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the "3rd reading" stage for the Northern Ireland Troubles Bill (Session 2024–26) is shown as completed on the bill's official stages page (https://bills.parliament.uk/bills/4022/stages) with a date on or after May 12, 2026 and on or before July 1, 2026 (by 23:59 UTC).

This question resolves **No** if, as of 23:59 UTC on July 1, 2026, the Third Reading stage has not been marked as completed on that page.

The sole source of truth is the UK Parliament bill tracking page: https://bills.parliament.uk/bills/4022/stages

**Pre-cutoff background**

The Northern Ireland Troubles Bill (Session 2024–26) seeks to repeal and replace parts of the Northern Ireland Troubles (Legacy and Reconciliation) Act 2023. As of May 13, 2026, the bill has completed the following stages in the House of Commons [https://bills.parliament.uk/bills/4022/stages](https://bills.parliament.uk/bills/4022/stages):

- **First Reading:** 14 October 2025
- **Second Reading:** 18 November 2025
- **Programme motion:** 18 November 2025
- **Money resolution:** 18 November 2025
- **Carry-over motion:** 27 April 2026

The carry-over motion ensures the bill survives prorogation and the King's Speech. The bill is currently awaiting the **Committee of the whole House** stage, for which no date has yet been announced [https://bills.parliament.uk/bills/4022/stages](https://bills.parliament.uk/bills/4022/stages). Before Third Reading can occur, the bill must still pass through Committee of the whole House and Report stage.

The government has indicated it intends to bring forward "substantial amendments" to the bill. The bill is considered contentious, with debate over legacy, justice, and reconciliation provisions for victims of the Northern Ireland Troubles.

[Third Reading](https://www.parliament.uk/about/how/laws/passage-bill/commons/coms-commons-third-reading/) is the final debate on a bill in the House of Commons, where Members decide whether to approve the bill in its final form. It typically follows immediately after Report stage, often on the same day, but this is not guaranteed for complex or contentious legislation.

**Exact later resolution packet**

The question resolves NO (0).

Resolution criteria: The question resolves YES only if the "3rd reading" stage for the Northern Ireland Troubles Bill (Session 2024–26) is shown as completed on the official UK Parliament bill tracking page (https://bills.parliament.uk/bills/4022/stages) with a date on or after 12 May 2026 and on or before 1 July 2026 (23:59 UTC). It resolves NO if, as of 23:59 UTC on 1 July 2026, the Third Reading stage has not been marked as completed.

Evidence from the sole source of truth:
- The official stages page (https://bills.parliament.uk/bills/4022/stages) lists the completed/scheduled stages as: 1st reading (14 October 2025); 2nd reading (18 November 2025); Programme motion (18 November 2025); Money resolution (18 November 2025); Carry-over motion (27 April 2026); Bill reintroduced (14 May 2026); and Committee of the whole House with date "to be announced." There is NO entry for a completed Report stage or 3rd reading stage [e0a6e8].
- The bill's main page (https://bills.parliament.uk/bills/4022) confirms the bill is still at the Committee stage (reintroduced at Committee stage on 14 May 2026), with the page last updated 17 June 2026, and the 3rd reading stage is not marked as completed [9bec4d].

Because the Committee of the whole House stage still has no announced date, and the bill must still pass Committee and Report stages before Third Reading, the Third Reading had not occurred and is not marked as completed by 23:59 UTC on 1 July 2026. Therefore the antecedent condition for YES (a completed 3rd reading within the specified window) is not met, and the question resolves NO.

Source URL: https://bills.parliament.uk/bills/4022/stages

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-195. `722ff8f3-c5b7-5bd9-b23f-0b44a8aa3eec`

- Present date: `2026-05-02 21:11:39.189118`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the NSF's terminated awards list include any new terminations added between May 1, 2026, and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the NSF terminated awards CSV file (https://nsf-gov-resources.nsf.gov/files/NSF-Terminated-Awards.csv) contains, as of 23:59 UTC on June 1, 2026, one or more award IDs that were **not** present in the version of the file captured on April 30, 2026.

To determine resolution:
1. A baseline snapshot of the CSV file shall be taken on or before April 30, 2026, recording all award IDs listed.
2. On June 1, 2026, at or before 23:59 UTC, the CSV file shall be downloaded again from the same URL.
3. If the June 1 version contains any award IDs not present in the April 30 baseline, the question resolves **Yes**.
4. If the June 1 version contains no new award IDs compared to the April 30 baseline, the question resolves **No**.
5. If the CSV file is inaccessible or the list is not updated (i.e., the file cannot be retrieved or returns an error) at any point during the May 1–June 1 window such that no comparison can be made, the question resolves **No**.

The source of truth is exclusively the CSV file at: https://nsf-gov-resources.nsf.gov/files/NSF-Terminated-Awards.csv

**Pre-cutoff background**

The U.S. National Science Foundation (NSF) has been terminating research grants as part of a portfolio review aligned with administration priorities since early 2025. The NSF maintains a publicly downloadable CSV file of terminated awards at https://nsf-gov-resources.nsf.gov/files/NSF-Terminated-Awards.csv, linked from the "Updates on NSF Priorities" page (https://www.nsf.gov/updates-on-priorities) [Updates on NSF Priorities | NSF - U.S. National Science Foundation](https://www.nsf.gov/updates-on-priorities).

As of April 6, 2026, approximately 1,363 net terminated grants (total terminations minus reinstatements) have accumulated since February 3, 2025. Notably, there have been zero new terminations reported for the weeks spanning February 2, 2026 through April 6, 2026 — a pause of over two months [NSF Report for Week of Apr 6, 2026 - Grant Witness](https://grant-witness.us/reports/2026-04-06_NSF_report.html). Earlier reporting indicated approximately 1,752 total grants terminated. The prolonged pause in new terminations creates genuine uncertainty about whether additional terminations will resume in May 2026, given ongoing legal challenges (including court injunctions that previously reinstated 114 awards), congressional pushback, and the Trump administration's proposed 54% budget cuts to NSF.

**Exact later resolution packet**

The question resolves YES only if the official NSF terminated-awards CSV (https://nsf-gov-resources.nsf.gov/files/NSF-Terminated-Awards.csv) contained, as of 23:59 UTC on June 1, 2026, one or more award IDs not present in the April 30, 2026 baseline.

Key evidence: Grant Witness, which programmatically tracks the NSF terminated-awards data, published an article on May 27, 2026 ("New Grant Disruptions at NSF") explicitly stating that "NSF has not updated its public list of terminated grants since June 2025" [New Grant Disruptions at NSF - We Need Your Help to Report!](https://grant-witness.us/posts/2026-05-27_new-nsf-terminations/). This means the official CSV file's contents (the set of award IDs) had not changed since long before the April 30 baseline, so no new award IDs could have appeared in the June 1 version relative to the April 30 version.

Furthermore, although Grant Witness independently documented roughly 19 new NSF grant disruptions/terminations in April and May 2026 (e.g., suspensions at UC Berkeley), these were collected directly from affected researchers and are NOT reflected in the official NSF CSV file [New Grant Disruptions at NSF - We Need Your Help to Report!](https://grant-witness.us/posts/2026-05-27_new-nsf-terminations/). The question's sole source of truth is the official CSV, not Grant Witness's independent database.

Corroborating: Grant Witness's weekly NSF reports for the weeks of May 4, May 11, May 18, and May 25, 2026 show zero new terminations appearing in the NSF dataset they monitor [Weekly Reports - Grant Witness](https://grant-witness.us/reports.html). The week-of-April-6 report already noted a multi-month pause with zero new terminations since early February 2026.

Therefore the June 1, 2026 version of the CSV contained no award IDs that were not in the April 30, 2026 baseline, satisfying criterion 4 (no new award IDs → NO). Resolution: NO (0).

Relevant URLs:
- https://grant-witness.us/posts/2026-05-27_new-nsf-terminations/ (states NSF list not updated since June 2025)
- https://grant-witness.us/reports/2026-05-04_NSF_report.html, /2026-05-11_, /2026-05-18_, /2026-05-25_ (weekly reports, zero new NSF terminations in May 2026)
- https://nsf-gov-resources.nsf.gov/files/NSF-Terminated-Awards.csv (the source-of-truth CSV)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-196. `9e3713e1-f221-5d16-b4a0-c3d5bf83f6d0`

- Present date: `2026-05-16 17:35:08.123186`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will at least one ASEAN member state deposit an instrument of ratification for the Cebu Protocol to Amend the ASEAN Charter with the ASEAN Secretary-General by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if at least one of the eleven ASEAN member states (Brunei Darussalam, Cambodia, Indonesia, Lao PDR, Malaysia, Myanmar, Philippines, Singapore, Thailand, Timor-Leste, or Viet Nam) deposits an instrument of ratification for the Cebu Protocol to Amend the Charter of the Association of Southeast Asian Nations with the ASEAN Secretary-General on or after May 12, 2026, and on or before July 1, 2026, 23:59 UTC. Otherwise, it resolves as **No**.

An "instrument of ratification" is a formal document whereby a state establishes its consent to be bound by a treaty, as defined under [Article 2(1)(b) of the Vienna Convention on the Law of Treaties](https://legal.un.org/ilc/texts/instruments/english/conventions/1_1_1969.pdf) and consistent with [Article 47 of the ASEAN Charter](https://asean.org/asean-charter/). "Deposit" means the formal submission of this instrument to the ASEAN Secretary-General as depositary.

The primary resolution source is the [ASEAN Secretariat Legal Instruments page](https://asean.org/category/legal-instruments/) and the [ASEAN Secretariat notifications/announcements](https://asean.org/). Secondary sources include official government press releases or foreign ministry announcements from the ratifying member state(s), or credible reporting from Reuters, AP, or similar outlets.

**Pre-cutoff background**

The [Cebu Protocol to Amend the Charter of the Association of Southeast Asian Nations](https://asean.org/cebu-protocol-to-amend-the-charter-of-the-association-of-southeast-asian-nations/) was adopted on May 8, 2026, during the 48th ASEAN Summit in Cebu, Philippines [https://asean.org/chairs-statement-of-the-48th-asean-summit/](https://asean.org/chairs-statement-of-the-48th-asean-summit/). This marks the first-ever amendment to the [ASEAN Charter](https://asean.org/asean-charter/), originally signed in 2007 [https://asean.org/cebu-protocol-to-amend-the-charter-of-the-association-of-southeast-asian-nations/](https://asean.org/cebu-protocol-to-amend-the-charter-of-the-association-of-southeast-asian-nations/).

For the protocol to enter into force, each ASEAN member state must complete its domestic ratification process and formally deposit an "instrument of ratification" — a formal document confirming a state's consent to be bound by a treaty (see [Article 47 of the ASEAN Charter](https://asean.org/asean-charter/) and the [Vienna Convention on the Law of Treaties, Article 14](https://legal.un.org/ilc/texts/instruments/english/conventions/1_1_1969.pdf)) — with the ASEAN Secretary-General, who serves as the depositary.

As of May 13, 2026, no member state has deposited an instrument of ratification [https://asean.org/chairs-statement-of-the-48th-asean-summit/](https://asean.org/chairs-statement-of-the-48th-asean-summit/). The eleven current ASEAN member states eligible to ratify are: Brunei Darussalam, Cambodia, Indonesia, Lao PDR, Malaysia, Myanmar, Philippines, Singapore, Thailand, Timor-Leste, and Viet Nam (see [ASEAN Member States](https://asean.org/member-states/)) [https://asean.org/chairs-statement-of-the-48th-asean-summit/](https://asean.org/chairs-statement-of-the-48th-asean-summit/).

Ratification timelines vary significantly across member states. Some states (e.g., Brunei, Singapore) can ratify treaties relatively quickly through executive action, while others (e.g., Indonesia, Philippines) typically require parliamentary approval. For historical context, the original ASEAN Charter was signed in November 2007 and took approximately one year for all ten then-members to ratify. However, Singapore deposited its instrument of ratification within roughly two months. The ~7-week window between adoption and July 1, 2026 makes it uncertain whether any state can complete the process in time.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question asks whether at least one of the eleven ASEAN member states deposited an instrument of ratification for the Cebu Protocol to Amend the ASEAN Charter with the ASEAN Secretary-General (the depositary) between May 12, 2026 and July 1, 2026 (23:59 UTC).

KEY DISTINCTION (signing vs. deposit of instrument of ratification): The Cebu Protocol was adopted/signed on May 8, 2026 at the 48th ASEAN Summit in Cebu, Philippines. The Protocol text itself states it "shall be subject to ratification by all ASEAN Member States in accordance with their respective internal procedures" and enters into force based on the deposit of the last instrument of ratification with the Secretary-General of ASEAN (https://asean.org/wp-content/uploads/2026/05/Adopted-Cebu-Protocol-to-Amend-the-Charter-of-the-Association-of-Southeast-Asian-Nations.pdf). Per Article 2(1)(b) of the Vienna Convention on the Law of Treaties, "ratification" is the distinct international act (via deposit of a formal instrument) whereby a State establishes its consent to be bound — separate from adoption/signature and separate from domestic (executive/parliamentary) approval steps.

EVIDENCE AGAINST ANY DEPOSIT:
1. Timor-Leste (the state most directly interested, since the Protocol formalizes its membership) is the only member state with public movement toward ratification in the window. Its Council of Ministers only "approved a draft resolution seeking ratification" of the Cebu Protocol on June 3, 2026, and that proposal "will be submitted to the National Parliament for ratification" — a domestic step, not a deposit of an instrument of ratification with the ASEAN Secretary-General [Govt approves ratification of Cebu Protocol amending the Charter of ...](https://en.tatoli.tl/2026/06/03/govt-approves-ratification-of-cebu-protocol-amending-the-charter-of-asean/17/). As of that date the process was incomplete and no instrument had been deposited.
2. The primary resolution source — the ASEAN legal instruments/agreements database (agreement.asean.org) — lists the Cebu Protocol (08 May 2026) but shows no ratification/deposit entries for it, i.e., no member state recorded as having deposited an instrument of ratification [2 - ASEAN agreements](https://agreement.asean.org/home/index/2.html) [Advance Search](https://agreement.asean.org/search/advances.html?name_of_instrument=&if_status=&id_area_cooperation=&docs_start=&docs_end=&signature_place=Cebu,%20Philippines&type=docs) [2 - ASEAN agreements](https://agreement.asean.org/home/index/2.html).
3. The ASEAN Secretariat Legal Instruments page shows no notification/announcement of any deposit of an instrument of ratification for the Cebu Protocol in May–June 2026 [https://asean.org/category/legal-instruments/](https://asean.org/category/legal-instruments/).
4. Singapore — one of the states cited as able to ratify quickly — only had PM Lawrence Wong "welcome" the Cebu Protocol; he called for swift ratification of other agreements (ASEAN Petroleum Security Agreement, upgraded ASEAN Trade in Goods Agreement), with no indication Singapore deposited an instrument of ratification for the Cebu Protocol [PM Wong calls for swift ratification of ASEAN petroleum, trade ... - CNA](https://www.channelnewsasia.com/singapore/asean-summit-cebu-lawrence-wong-middle-east-strait-hormuz-6108656).

CONCLUSION: No ASEAN member state deposited an instrument of ratification for the Cebu Protocol with the ASEAN Secretary-General on or before July 1, 2026, 23:59 UTC. The furthest any state got was a domestic cabinet-level approval (Timor-Leste, June 3, 2026), which does not satisfy the resolution's requirement of "the formal submission of this instrument to the ASEAN Secretary-General as depositary." The question therefore resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-197. `cdcbd23d-1832-5d11-84b1-cb1be656abd9`

- Present date: `2026-05-29 03:04:57.186456`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Abdiaziz Laftagareen physically return to Baidoa, Somalia, between May 12, 2026, and July 1, 2026?

**Resolution criteria**

This question resolves Yes if, on or after May 12, 2026, and on or before July 1, 2026 (23:59 UTC), there is credible reporting confirming that Abdiaziz Hassan Mohamed Laftagareen has been physically present within the city of Baidoa, Somalia.

Definitions:
- "Physically present" means Laftagareen's person is located within the city of Baidoa, the administrative capital of South West State. Transit through Baidoa airspace or brief passage through checkpoints outside the city does not count.
- "Credible reporting" means at least one report from any of the following types of sources: major international news agencies (Reuters, AP, AFP, BBC, Al Jazeera) or established Somali news outlets (Garowe Online, Radio Dalsan, Hiiraan Online, WardheerNews, Somali Guardian). Photographic or video evidence published by these outlets showing Laftagareen in Baidoa is sufficient.
- A public announcement or claim of return alone does not satisfy this criterion; his physical presence in Baidoa must be confirmed.

If no credible reporting confirms his physical presence in Baidoa by 23:59 UTC on July 1, 2026, the question resolves No.

**Pre-cutoff background**

Abdiaziz Hassan Mohamed "Laftagareen" served as President of Somalia's South West State until March 30, 2026, when he resigned after the Somali National Army took control of Baidoa, the state's administrative capital [I am the legitimate South West President, plan to return to Baidoa town](https://www.hiiraan.com/news4/2026/May/205059/laftagareen_i_am_the_legitimate_south_west_president_plan_to_return_to_baidoa_town.aspx). He had been re-elected on March 28, 2026, in a parliamentary vote that the federal government rejected [Somalia's president anoints sole candidate for Southwest presidency](https://www.somaliguardian.com/news/somalia-news/somalias-president-anoints-sole-candidate-for-southwest-presidency/).

Following his departure, Laftagareen relocated to Nairobi, Kenya. He has since claimed his resignation was made under duress and does not reflect his true position [I am the legitimate South West President, plan to return to Baidoa town](https://www.hiiraan.com/news4/2026/May/205059/laftagareen_i_am_the_legitimate_south_west_president_plan_to_return_to_baidoa_town.aspx). In an interview published May 3, 2026, he stated: "I am the legitimate South West President" and announced plans to return to Baidoa 13 days after the federal president's term expires on May 15, 2026 [I am the legitimate South West President, plan to return to Baidoa town](https://www.hiiraan.com/news4/2026/May/205059/laftagareen_i_am_the_legitimate_south_west_president_plan_to_return_to_baidoa_town.aspx). In a further interview published May 12, 2026, he declared: "I am the legally elected President of South West State" and vowed, "I will return to my regions—and I will liberate them" [Defiant Laftagareen: 'I Am Still the Legitimate President](https://wardheernews.com/defiant-laftagareen-i-am-still-the-legitimate-president/).

Meanwhile, the federal government has moved to install new leadership. On April 16, 2026, President Hassan Sheikh Mohamud anointed parliament Speaker Adan Mohamed Nur (Adan Madobe) as the sole ruling-party candidate for the South West State presidency [Somalia's president anoints sole candidate for Southwest presidency](https://www.somaliguardian.com/news/somalia-news/somalias-president-anoints-sole-candidate-for-southwest-presidency/). The Somali National Army maintains control of Baidoa.

Laftagareen reportedly retains Ethiopian backing and significant clan support, but faces a federal military presence in Baidoa. Whether he can translate his rhetoric into a physical return depends on Ethiopia-Somalia relations, federal military posture, clan dynamics, and the broader political crisis around the May 15 federal term expiration.

**Exact later resolution packet**

The question resolves NO. It required credible reporting from a specified source (Reuters, AP, AFP, BBC, Al Jazeera, Garowe Online, Radio Dalsan, Hiiraan Online, WardheerNews, or Somali Guardian) confirming that Abdiaziz Hassan Mohamed "Laftagareen" was PHYSICALLY PRESENT inside the city of Baidoa between May 12 and July 1, 2026 (23:59 UTC). A mere claim/announcement of return, or the actions of forces loyal to him, do not count.

All qualifying-source reporting across the entire window confirms that Laftagareen himself remained outside Baidoa (in Nairobi/Kenya), while only forces LOYAL to him made incursions:

- Garowe Online (May 22, 2026): reports clashes on the "outskirts of Baidoa" and explicitly states Laftagareen "is currently in Kenya" and has only "vowed to return to Baidoa." No physical presence of the man himself. [Somalia: Clashes erupt outside Baidoa between federal troops and ...](https://www.garoweonline.com/en/news/somalia/somalia-clashes-erupt-outside-baidoa-between-federal-troops-and-forces-loyal-to-ousted-southwest-leader)
- Hiiraan Online (May 22, 2026): fighting between Southwest forces and "militias loyal to" Laftagareen occurred on the outskirts (Idoow Dhagoole area, north of Baidoa); no mention of Laftagareen himself in the city. [Southwest forces clash with Laftagareen loyalists outside Baidoa](https://www.hiiraan.com/security4/2026/May/205222/southwest_forces_clash_with_laftagareen_loyalists_outside_baidoa.aspx)
- Garowe Online (May 30, 2026): "Forces loyal to ousted Southwest State President ... Laftagareen entered the regional capital of Baidoa on Friday" — the entry is explicitly attributed to "armed fighters aligned with" him, not the man; no evidence he was personally present. [Somalia: Forces Loyal to Ousted Southwest Leader Enter Baidoa as ...](https://www.garoweonline.com/en/news/somalia/somalia-forces-loyal-to-ousted-southwest-leader-enter-baidoa-as-heavy-fighting-erupts-ahead-of-elections)
- Hiiraan Online (June 1, 2026): clashes "on the outskirts of Baidoa"/"near Baidoa" between federal forces and troops loyal to Laftagareen, prompting a curfew; no evidence of Laftagareen personally in the city. [Southwest State imposes Baidoa curfew after clashes near city](https://www.hiiraan.com/news4/2026/Jun/205294/southwest_state_imposes_baidoa_curfew_after_clashes_near_city.aspx)
- WardheerNews (June 24, 2026): reports army defections to forces loyal to Laftagareen, who maintain a presence in rural areas surrounding Baidoa; no mention of Laftagareen himself in the city. [Tensions Rise Around Baidoa as Reports Emerge of Army ...](https://wardheernews.com/tensions-rise-around-baidoa-as-reports-emerge-of-army-defections-to-forces-loyal-to-former-south-west-president-laftagareen/)
- WardheerNews (June 28, 2026): defecting forces "linked up with Laftagareen's fighters" on the "outskirts of Baidoa," and his forces carried out "hit-and-run attacks targeting positions around the city"; no evidence he was inside Baidoa. [Reports Claim Security Forces Defect to Laftagareen's Armed ...](https://wardheernews.com/reports-claim-security-forces-defect-to-laftagareens-armed-movement-as-south-west-tensions-escalate/)

A Somali Guardian "rift" article likewise notes Laftagareen relocated to Nairobi after leaving office on March 30, 2026. [Rift between Somalia's president and Southwest state leader erupts ...](https://www.somaliguardian.com/news/somalia-news/rift-between-somalias-president-and-southwest-state-leader-erupts-into-violence/)

Potential red herrings ruled out:
- An AllAfrica story dated June 29, 2026 headlined "Southwest State Leader Opens Somalia Humanitarian Forum in Baidoa" is OLD content: it was originally published by Shabelle Media Network / Goobjoog and refers to the "Somalia Humanitarian Forum 2025 (CHF 2025)" from when Laftagareen was still the sitting SWS president — not a June 2026 event, and Shabelle/AllAfrica are not among the specified qualifying sources.
- Social-media posts (Instagram/Facebook) claiming Laftagareen would "land in Baidoa in a private plane" or made a "final trip" are not from qualifying sources, and no qualifying outlet corroborated a personal physical presence inside the city during the window.

Because no report from any of the specified sources confirmed Laftagareen's personal physical presence within the city of Baidoa between May 12 and July 1, 2026 — only that forces loyal to him operated on the outskirts and briefly pushed into the city — the resolution criterion for YES was not met, and the question resolves NO.

Key source URLs:
- https://www.garoweonline.com/en/news/somalia/somalia-clashes-erupt-outside-baidoa-between-federal-troops-and-forces-loyal-to-ousted-southwest-leader
- https://www.garoweonline.com/en/news/somalia/somalia-forces-loyal-to-ousted-southwest-leader-enter-baidoa-as-heavy-fighting-erupts-ahead-of-elections
- https://www.hiiraan.com/security4/2026/May/205222/southwest_forces_clash_with_laftagareen_loyalists_outside_baidoa.aspx
- https://www.hiiraan.com/news4/2026/Jun/205294/southwest_state_imposes_baidoa_curfew_after_clashes_near_city.aspx
- https://wardheernews.com/tensions-rise-around-baidoa-as-reports-emerge-of-army-defections-to-forces-loyal-to-former-south-west-president-laftagareen/
- https://wardheernews.com/reports-claim-security-forces-defect-to-laftagareens-armed-movement-as-south-west-tensions-escalate/

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-198. `ebcd3872-6eb8-53bf-8ba1-5bf15f9367d6`

- Present date: `2026-05-12 22:04:24.683987`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Zscaler's Q3 FY2026 earnings call transcript include management discussion of lost or delayed federal government contracts attributed to spending cuts or DOGE?

**Resolution criteria**

This question resolves **YES** if the official transcript of Zscaler's Q3 FY2026 earnings conference call (held May 26, 2026, at 4:30 PM ET) contains a statement—in either the prepared remarks or the Q&A session—by any Zscaler executive or in response to an analyst question, that describes one or more federal government contracts as having been **lost, canceled, delayed, paused, or formally postponed** and **explicitly attributes** that loss or delay to federal spending cuts, budget reductions, the Department of Government Efficiency ([DOGE](https://en.wikipedia.org/wiki/Department_of_Government_Efficiency)), or actions taken under DOGE's mandate.

Key definitions:
- **"Lost or delayed contract"**: A contract that has been canceled after being signed or awarded, or a procurement process that has been formally postponed or put on hold. A general mention of "federal headwinds" or "macro uncertainty" without specific reference to contract losses/delays does NOT suffice.
- **"Explicitly attributes"**: Management must directly link the contract loss or delay to spending cuts, budget reductions, or DOGE. A general mention of federal headwinds or cautious government spending environment, without naming spending cuts or DOGE as a cause of specific contract outcomes, does NOT suffice for YES resolution.
- **DOGE**: The Department of Government Efficiency, a U.S. government body established in 2025 to reduce federal spending (see: https://en.wikipedia.org/wiki/Department_of_Government_Efficiency).

The question resolves **NO** if the transcript contains no such explicit attribution, or if management denies federal contract losses/delays, or if the topic is not raised at all.

**Primary resolution source**: The official earnings call transcript published on the Zscaler Investor Relations website at https://ir.zscaler.com/financial-information/quarterly-results [Events & Presentations - Zscaler IR](https://ir.zscaler.com/news-events/events-presentations). If the transcript is not available on ir.zscaler.com by June 15, 2026 (11:59 PM ET), the fallback source shall be the transcript as published on Seeking Alpha (seekingalpha.com), Bloomberg Terminal, or FactSet.

All timestamps reference U.S. Eastern Time (ET).

**Pre-cutoff background**

Zscaler (NASDAQ: ZS) is a cloud-based cybersecurity company providing zero trust security solutions to enterprises and government agencies. The company is scheduled to report Q3 FY2026 earnings on May 26, 2026, at 4:30 PM ET, with a conference call following the release [Events & Presentations - Zscaler IR](https://ir.zscaler.com/news-events/events-presentations).

The U.S. federal government is a meaningful customer segment for Zscaler. While the company does not separately disclose exact federal revenue, it serves over 100 public sector organizations and holds key federal certifications (FedRAMP, etc.). Industry estimates suggest the federal/public sector represents roughly 10–15% of Zscaler's total revenue.

Several developments create uncertainty about Zscaler's federal business:
- CISA has faced $707 million in proposed budget reductions for FY2027, and CISA cyber partnerships face a reported "standstill" amid cuts.
- The Department of Government Efficiency ([DOGE](https://en.wikipedia.org/wiki/Department_of_Government_Efficiency)) has been terminating or reducing federal contracts across agencies.
- In March 2025, Zscaler CEO Jay Chaudhry stated the company expected to "benefit" from government efficiency measures, arguing its platform helps agencies consolidate legacy security products [Zscaler Expects To 'Benefit' From US Government Efficiency Measures](https://www.crn.com/news/security/2025/zscaler-expects-to-benefit-from-us-government-efficiency-measures-ceo-jay-chaudhry).
- However, in the Q2 FY2026 earnings call (February 26, 2026), the transcript did not contain explicit discussion of federal contract losses, DOGE impacts, or government spending cuts [Zscaler (ZS) Q2 2026 Earnings Call Transcript | The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/02/26/zscaler-zs-q2-2026-earnings-call-transcript/).

Zscaler reported Q2 FY2026 revenue of $815.8 million (up 26% YoY) and ARR of $3.4 billion (up 25% YoY). The Q3 FY2026 call will cover the quarter ending April 30, 2026—a period during which federal spending pressures have intensified.

**Exact later resolution packet**

The question resolves NO.

**Resolution source and fallback validation:** The question's primary resolution source is the official transcript on the Zscaler IR website (ir.zscaler.com). I confirmed that the IR "Quarterly Results" page hosts only the Q3 FY2026 Press Release, Supplemental Financials, a Q3'26 Shareholder Letter, and a webcast link — but NO official written transcript [Quarterly Results | Zscaler, Inc.](https://ir.zscaler.com/financial-information/quarterly-results). Since no transcript is available on ir.zscaler.com (as of today, 2026-07-01, well past the June 15, 2026 cutoff specified in the resolution criteria), the criteria authorize use of fallback published transcripts. I used the widely-syndicated official call transcripts published by The Motley Fool, Investing.com, and GuruFocus.

**What the transcript actually says about federal/public sector:** All three independent transcript sources agree that Zscaler's Q3 FY2026 (quarter ended April 30, 2026) call framed the public sector — including federal government — as a source of STRENGTH, not losses:
- CFO Kevin Rubin stated net new ARR "benefited from strength in the public sector vertical, which includes state, local, and federal government, and healthcare, including an approximate eight-digit upsell at a federal agency." [Zscaler (ZS) Q3 2026 Earnings Call Transcript | The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/05/26/zscaler-zs-q3-2026-earnings-call-transcript/) [Earnings call transcript: Zscaler beats Q3 2026 forecasts, ...](https://www.investing.com/news/transcripts/earnings-call-transcript-zscaler-beats-q3-2026-forecasts-stock-rises-93CH-4710950) [Q3 2026 Zscaler Inc Earnings Call Transcript - GuruFocus](https://www.gurufocus.com/stock/ZS/transcripts/8883608)
- CEO Jay Chaudhry cited a seven-figure upsell with a federal agency that had migrated from a legacy VPN architecture to Zscaler's Zero Trust platform. [Earnings call transcript: Zscaler beats Q3 2026 forecasts, ...](https://www.investing.com/news/transcripts/earnings-call-transcript-zscaler-beats-q3-2026-forecasts-stock-rises-93CH-4710950)

**No qualifying statement present:** None of the three transcript sources found any statement describing a specific federal government contract as lost, canceled, delayed, paused, or postponed, nor any explicit attribution of such an outcome to federal spending cuts, budget reductions, or the Department of Government Efficiency (DOGE). References to "spending" or "budget" in the call related to Zscaler's own CapEx/hardware costs and customer procurement cycles, not to federal budget cuts harming Zscaler's contracts [Earnings call transcript: Zscaler beats Q3 2026 forecasts, ...](https://www.investing.com/news/transcripts/earnings-call-transcript-zscaler-beats-q3-2026-forecasts-stock-rises-93CH-4710950).

The resolution criteria require BOTH (a) a specific federal contract described as lost/canceled/delayed/paused/postponed AND (b) explicit attribution to spending cuts/budget reductions/DOGE. Neither element is present; in fact the federal commentary was positive. Under the criteria, "the question resolves NO if the transcript contains no such explicit attribution."

Sources:
- Zscaler IR Quarterly Results page (no transcript hosted) [Quarterly Results | Zscaler, Inc.](https://ir.zscaler.com/financial-information/quarterly-results): https://ir.zscaler.com/financial-information/quarterly-results
- Motley Fool transcript [Zscaler (ZS) Q3 2026 Earnings Call Transcript | The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/05/26/zscaler-zs-q3-2026-earnings-call-transcript/): https://www.fool.com/earnings/call-transcripts/2026/05/26/zscaler-zs-q3-2026-earnings-call-transcript/
- Investing.com transcript [Earnings call transcript: Zscaler beats Q3 2026 forecasts, ...](https://www.investing.com/news/transcripts/earnings-call-transcript-zscaler-beats-q3-2026-forecasts-stock-rises-93CH-4710950): https://www.investing.com/news/transcripts/earnings-call-transcript-zscaler-beats-q3-2026-forecasts-stock-rises-93CH-4710950
- GuruFocus transcript [Q3 2026 Zscaler Inc Earnings Call Transcript - GuruFocus](https://www.gurufocus.com/stock/ZS/transcripts/8883608): https://www.gurufocus.com/stock/ZS/transcripts/8883608

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-199. `19349d5d-49e1-5328-be33-a1b04688a5b1`

- Present date: `2026-05-14 05:18:55.232336`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the DRC government announce the seizure or freezing of assets belonging to Joseph Kabila valued at over $5 million USD between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (00:00 UTC) and before July 1, 2026 (23:59 UTC), an official body of the DRC government announces the seizure or freezing of assets belonging to former President Joseph Kabila with a stated or estimated total value of at least $5 million USD.

**What counts as an official announcement:**
An announcement qualifies if it is:
1. Published on an official DRC government website or communicated via an official government press conference or gazette; OR
2. Reported by at least one major international news organization—specifically [Reuters](https://www.reuters.com/), [AFP/France24](https://www.france24.com/), [Associated Press](https://apnews.com/), [BBC](https://www.bbc.com/), or [Jeune Afrique](https://www.jeuneafrique.com/)—citing official DRC government sources or documents confirming the action.

**Valuation methodology:**
- If the announcement states a value in USD, that value is used directly.
- If the value is stated in another currency (e.g., Congolese francs, euros), it will be converted to USD using the exchange rate published by the [European Central Bank](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html) or [XE.com](https://www.xe.com/) on the date of the announcement.
- If the announcement lists non-monetary assets (e.g., real estate, vehicles, mining concessions) without a USD figure, the value reported or estimated by the announcing authority or by the credible news sources listed above will be used. If no valuation is provided by any of these sources, those assets do not count toward the $5 million threshold.

**Exclusions:**
- US sanctions-related asset freezes (already in effect as of April 30, 2026) do not count unless the DRC government itself independently announces a seizure or freeze.
- Announcements made before May 12, 2026 (00:00 UTC) do not count.

If no qualifying announcement is identified by July 1, 2026 (23:59 UTC), this question resolves **No**.

**Pre-cutoff background**

As of May 12, 2026, former Democratic Republic of the Congo (DRC) President Joseph Kabila faces escalating legal and financial pressure from multiple directions:

**Treason conviction and fugitive status:** In September 2025, a Congolese military court sentenced Kabila to death in absentia for treason, citing his alleged complicity with the M23 rebel group and the Congo River Alliance (AFC) [https://panafricanvisions.com/2026/04/dr-congo-declares-former-president-joseph-kabila-fugitive-after-treason-conviction/](https://panafricanvisions.com/2026/04/dr-congo-declares-former-president-joseph-kabila-fugitive-after-treason-conviction/). State authorities subsequently declared him a fugitive. His current whereabouts remain unclear, though he is believed to be outside the country [https://panafricanvisions.com/2026/04/dr-congo-declares-former-president-joseph-kabila-fugitive-after-treason-conviction/](https://panafricanvisions.com/2026/04/dr-congo-declares-former-president-joseph-kabila-fugitive-after-treason-conviction/).

**US sanctions:** On April 30, 2026, the United States blacklisted Kabila, accusing him of providing "financial and political support" to groups driving violence and instability in the Great Lakes region [https://www.africanews.com/2026/05/01/drcs-ex-president-joseph-kabila-dismisses-us-sanctions-as-politically-motivated/](https://www.africanews.com/2026/05/01/drcs-ex-president-joseph-kabila-dismisses-us-sanctions-as-politically-motivated/). The sanctions freeze any US-linked assets and bar American entities from transacting with him. The DRC government welcomed the sanctions, stating they would have "operational implications" restricting Kabila's capacity to mobilize finance [https://www.africanews.com/2026/05/01/drcs-ex-president-joseph-kabila-dismisses-us-sanctions-as-politically-motivated/](https://www.africanews.com/2026/05/01/drcs-ex-president-joseph-kabila-dismisses-us-sanctions-as-politically-motivated/).

**DRC government actions:** The Tshisekedi government has moved against Kabila's political party and sought to seize assets of its leaders. However, as of May 12, 2026, there are no confirmed reports of the DRC government successfully announcing a large-scale seizure or freezing of Kabila's personal assets domestically.

**Kabila's known assets:** Kabila is widely reported to control extensive assets within the DRC, including farms, ranches, real estate, and stakes in mining and other commercial enterprises. International investigations (e.g., by the Congo Research Group and The Sentry) have documented a vast portfolio. The $5 million threshold is calibrated to capture a meaningful but plausible domestic enforcement action—seizing even a few properties or bank accounts could reach this level—while remaining uncertain given the DRC government's historically weak enforcement capacity and the complexity of tracing assets held through proxies.

**Definitions:**
- "Seizure" refers to the government taking legal possession or control of assets (see [Wikipedia: Asset forfeiture](https://en.wikipedia.org/wiki/Asset_forfeiture)).
- "Freezing" refers to a legal order preventing the transfer, conversion, or movement of assets (see [Wikipedia: Asset freezing](https://en.wikipedia.org/wiki/Asset_freezing)).
- "DRC government" means any official body of the Democratic Republic of the Congo, including but not limited to the Ministry of Justice, the judiciary (including military courts), the Central Bank of the Congo (BCC), or the office of the presidency acting in an official capacity.

**Exact later resolution packet**

The question resolves **NO**. No official DRC government body announced (nor did Reuters, AFP/France24, AP, BBC, or Jeune Afrique report, citing official DRC sources) a seizure or freezing of Joseph Kabila's assets with a stated/estimated value of at least $5 million USD during the window of May 12, 2026 (00:00 UTC) to July 1, 2026 (23:59 UTC).

Detailed reasoning:

1) The prominent DRC-domestic asset action circulating during the window concerned the **Kingakati estate/domain**. However, this action is a "déclaration d'utilité publique" (public-utility declaration for urban/infrastructure expansion of Kinshasa) covering ~43,159 hectares in the Maluku commune (village of Bita), enacted by **Ministerial Decree n°116/CAB/MIN/AFF.FONC/ONM/jna/2026 signed on April 20, 2026** — i.e., BEFORE the May 12 window start. The resolution criteria explicitly state that "Announcements made before May 12, 2026 (00:00 UTC) do not count." [767bde][5ce839][493caf][d81ee7]

2) This measure is characterized by the reporting sources as an expropriation for public utility (urban expansion / "Kinshasa Kia Mona" project), NOT as a targeted punitive seizure or freezing of Joseph Kabila's personal assets. Sources note the political sensitivity because Kingakati is associated with Kabila, but do not frame it as an asset seizure against him. [493caf][d81ee7][5ce839]

3) On May 14, 2026, the management of the Parc de la Vallée de la N'Sele (Kingakati park) publicly **DENIED** any seizure of the Kingakati farm, clarifying that the April 20 decree concerned a different perimeter (Maluku/Bita) and did not constitute a seizure of Kabila's assets. This directly undercuts any claim of a confirmed within-window seizure. [45febf]

4) Crucially for valuation: none of the qualifying sources (the announcing DRC authority, or Reuters/AFP/France24/AP/BBC/Jeune Afrique) provided a USD monetary value for the Kingakati land or any within-window seizure. Per the resolution rules, non-monetary assets without a USD figure from the announcing authority or the listed news organizations "do not count toward the $5 million threshold." [767bde][493caf][d81ee7]

5) The US OFAC sanctions of April 30, 2026 (freezing US-jurisdiction assets) are explicitly excluded by the question, and the DRC merely "welcomed" them rather than independently announcing its own seizure/freeze of $5M+ in this window.

6) The original DRC seizure order of Kabila's movable and immovable assets was announced in April 2025 (and the treason conviction/damages in Sept–Oct 2025) — all well before the window and thus non-qualifying.

7) A review of the specified qualifying outlets (Reuters, France24/AFP, AP, BBC, Jeune Afrique) for the window found no report of a new DRC-domestic seizure/freeze of Kabila's assets with a ≥$5M valuation; recent Jeune Afrique coverage on Kabila does not mention such an action with a value. [9aa16f]

Because no qualifying announcement meeting all criteria (official DRC body, within window, ≥$5M valuation from the announcing authority or listed sources) was identified, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-200. `63ebcaa6-c122-5883-9d48-b201992d4ad7`

- Present date: `2026-05-14 11:32:10.652586`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the "Splitting the Post of the Attorney General Bill, 2025" pass its final (third) reading in the Knesset by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the "Splitting the Post of the Attorney General Bill, 2025" (the government-backed bill to split the Attorney General's role into separate positions, as approved in preliminary reading on October 29, 2025) passes its third and final reading in the Knesset Plenum on or after May 12, 2026, and on or before July 1, 2026 (23:59 UTC).

This question resolves as **No** if the bill has not passed its third and final reading by the end of July 1, 2026 (UTC).

"Pass" is defined as approval in the third (final) reading in the Knesset Plenum, per standard Knesset legislative procedure (see: https://m.knesset.gov.il/en/about/pages/legislation.aspx). Publication in the Official Gazette (Reshumot) is not required for resolution; the plenum vote is sufficient.

**Resolution source:** The official Knesset legislation database at https://main.knesset.gov.il/en/activity/pages/laws.aspx and/or Knesset press releases at https://m.knesset.gov.il/en/news/pressreleases/pages/default.aspx. Credible English-language reporting (e.g., Times of Israel, Jerusalem Post, Haaretz) may be used as supplementary confirmation.

**Pre-cutoff background**

On October 29, 2025, the Knesset Plenum approved the "Splitting the Post of the Attorney General Bill, 2025" in a preliminary reading, with 59 votes in favor and 44 against [Knesset Plenum approves in preliminary reading bill to split the post ...](https://m.knesset.gov.il/en/news/pressreleases/pages/press291025b.aspx). The bill proposes restructuring the Attorney General's Office by splitting the role into three separate positions: Attorney General (legal adviser to the government), Prosecutor General, and a representative of the state in legal proceedings [Knesset Plenum approves in preliminary reading bill to split the post ...](https://m.knesset.gov.il/en/news/pressreleases/pages/press291025b.aspx). Following the preliminary vote, the bill was referred to the House Committee to determine which Knesset committee would handle further deliberations [Knesset Plenum approves in preliminary reading bill to split the post ...](https://m.knesset.gov.il/en/news/pressreleases/pages/press291025b.aspx).

The Knesset returned from its six-week spring recess on May 10, 2026, and the coalition has announced plans to advance a series of contentious bills during the summer session, including this Attorney General split bill [Coalition Prepares Blitz of Controversial Bills Ahead of Election](https://www.jfeed.com/news-israel/knesset-controversial-bills). As of May 7, 2026, lawmakers are continuing work on this legislation [Coalition Prepares Blitz of Controversial Bills Ahead of Election](https://www.jfeed.com/news-israel/knesset-controversial-bills). Other competing legislative priorities include the Haredi draft exemption, the October 7 investigation bill, and media regulation legislation [Coalition Prepares Blitz of Controversial Bills Ahead of Election](https://www.jfeed.com/news-israel/knesset-controversial-bills).

Under Knesset legislative procedure, a bill must pass three readings to become law: (1) a preliminary reading (completed October 29, 2025), (2) a first reading (where the bill is presented to the plenum after committee preparation), and then after further committee work, (3) a second and third reading (which can occur in the same session). The bill's passage depends on coalition discipline and legislative bandwidth during a compressed summer session with multiple high-priority bills.

**Exact later resolution packet**

The question asks whether the "Splitting the Post of the Attorney General Bill, 2025" (הצעת חוק פיצול תפקיד היועץ המשפטי לממשלה, התשפ"ה-2025) — the specific bill approved in preliminary reading on October 29, 2025 — passed its third (final) reading in the Knesset Plenum between May 12, 2026 and July 1, 2026 (23:59 UTC). It did NOT, so the question resolves NO (0).

Legislative timeline established from sources:
- Preliminary reading passed October 29, 2025 (as stated in the question and matching the Knesset record).
- The Knesset Constitution, Law and Justice Committee approved the bill for FIRST reading on May 19, 2026, then re-voted to approve it for first reading on May 25, 2026 (Knesset press releases and committee news pages).
- The Knesset Plenum passed the bill in its FIRST reading on June 2, 2026, by a vote of 65–47, after which it was returned to the Constitution Committee for further deliberations ahead of second and third readings [c24faf].
- As of June 30, 2026 (the day before the resolution window closed), the bill was STILL in "marathon" Constitution Committee meetings to prepare for the second and third readings, and the article explicitly stated the bill "still requires two additional readings before becoming law." This confirms the third reading had not yet occurred [33af78].
- The official Knesset legislation database page for the bill (bill id 2226845) shows the bill never advanced past the preparation-for-first-reading/committee stage; it is recorded as stalled at the preparation stage for the first reading and subsequently merged into another bill (the "Attorney General and State Attorney Bill (Appointment, Tenure, Roles and Powers), 2026"). It never reached a second or third reading [df2fa9].
- Context reinforcing non-passage: in parallel, the Knesset was advancing a bill to dissolve itself (first reading passed June 2, 2026, 106–0), heading toward early elections, which interrupted the legislative process; the coalition indicated it might apply "continuity" to resume the bill in the next Knesset [c24faf].

Because on June 30, 2026 the bill still required both a second and a third reading, and because it was in committee (not on the plenum floor for final votes), it is not credible that it completed the third reading on the single remaining day (July 1, 2026). Therefore the bill did NOT pass its third and final reading within the required window, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-201. `719b3cbd-ce12-537e-a69e-7b187579d164`

- Present date: `2026-05-15 11:30:00.139468`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Northern Ireland Troubles Bill complete its Public Bill Committee stage by July 1, 2026?

**Resolution criteria**

This question resolves Yes if, on or after May 12, 2026, the Public Bill Committee stage of the Northern Ireland Troubles (Legacy and Reconciliation) Bill is marked as completed on the official UK Parliament bill tracker at https://bills.parliament.uk/bills/4022. Specifically, the Committee stage must be shown as having concluded (e.g., the bill is reported back to the House of Commons, or the stage is listed as complete rather than "In progress") by 11:59 PM UTC on July 1, 2026.

This question resolves No if the Committee stage remains "In progress" or has not yet begun reporting back to the House as of 11:59 PM UTC on July 1, 2026.

Primary resolution source: https://bills.parliament.uk/bills/4022

**Pre-cutoff background**

The Northern Ireland Troubles (Legacy and Reconciliation) Bill was introduced in the House of Commons during the 2024–26 session, sponsored by the Northern Ireland Office and Secretary of State Hilary Benn [https://bills.parliament.uk/bills/4022](https://bills.parliament.uk/bills/4022). As of May 13, 2026, the bill has passed its First Reading, Second Reading, and its Public Bill Committee stage is marked as "In progress" on the official UK Parliament bill tracker, with no confirmed dates for remaining committee sittings [https://bills.parliament.uk/bills/4022](https://bills.parliament.uk/bills/4022).

On April 27, 2026, a carry-over motion for the bill was debated in the House of Commons and passed 279–176, allowing the bill to be carried over into the next parliamentary session. During the Hansard debate, it was noted that "There is still no confirmed date for the Committee stage, which has been repeatedly delayed," reflecting significant uncertainty about the government's ability to complete this stage promptly.

The bill's progress depends on the number of committee sittings scheduled, the volume of amendments tabled, and broader political dynamics surrounding Northern Ireland legacy issues. The government has legislative tools to expedite the process, but opposition and the complexity of the subject matter have contributed to repeated delays.

**Exact later resolution packet**

The question resolves NO (0).

RESOLUTION CRITERIA: The question resolves YES only if, on or after May 12, 2026, the Public Bill Committee stage of the Northern Ireland Troubles (Legacy and Reconciliation) Bill (2024–26 session, https://bills.parliament.uk/bills/4022) is marked as completed (e.g., reported back to the House of Commons, or listed as "complete" rather than "In progress") by 11:59 PM UTC on July 1, 2026. It resolves NO if the Committee stage remains "In progress" or has not begun reporting back to the House by that deadline.

EVIDENCE FROM THE PRIMARY RESOLUTION SOURCE (https://bills.parliament.uk/bills/4022):
- Repeated queries of the official UK Parliament bill tracker confirm that the bill's "Committee stage" is still marked with the "In progress" (blue) status, not the "Complete" (green checkmark) status. The page's status key defines a grey icon as "Not yet reached," a blue icon as "In progress," and a green checkmark as "Complete." The Committee stage icon remained in the "In progress" state as of the source's last update on 17 June 2026 [92c459][a3e5fa].
- The bill was carried over into the next parliamentary session (consistent with the April 27, 2026 carry-over motion described in the question); the tracker associates the bill with both the 2024–26 and the subsequent session, but in no case is a Public Bill Committee stage recorded as completed or reported back to the House [a3e5fa][d664d3].
- There is no record on the tracker of the Committee stage having concluded or the bill being reported back to the House of Commons before the July 1, 2026 deadline [92c459][d664d3][a3e5fa].

CONCLUSION: Because the Public Bill Committee stage remained "In progress" (and was never marked complete or reported back to the House) on the official UK Parliament bill tracker as of 11:59 PM UTC on July 1, 2026, the condition for a YES resolution was not met. The question resolves NO.

VERIFICATION URLs: https://bills.parliament.uk/bills/4022 and https://bills.parliament.uk/bills/4022/stages

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-202. `b84a42db-48bc-5eeb-8d2e-39f7b193423c`

- Present date: `2026-05-03 01:20:54.265001`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Russia's 25 million tonne grain export quota (Feb 15 – June 30, 2026) be fully utilized by June 1, 2026?

**Resolution criteria**

This question resolves YES if, by 23:59 UTC on May 31, 2026, credible reporting confirms that Russia's cumulative grain exports (wheat, meslin, barley, and corn) under the tariff quota system have reached or exceeded 25 million tonnes since the quota took effect on February 15, 2026. "Fully utilized" means that at least 99% of the 25 million tonne quota (i.e., 24.75 million tonnes or more) has been shipped, OR the Russian Ministry of Agriculture, the Russian government, or a credible news source (e.g., Interfax at https://interfax.com/, Reuters, or TASS) reports that the quota has been exhausted or effectively exhausted.

The question resolves NO if, as of 23:59 UTC on May 31, 2026, no such confirmation exists, or if available data indicates cumulative exports under the quota remain below 24.75 million tonnes.

Resolution sources include:
- Russian Ministry of Agriculture (https://mcx.gov.ru/)
- Interfax (https://interfax.com/newsroom/top-stories/)
- USDA Foreign Agricultural Service (https://fas.usda.gov/)
- Global Trade Alert (https://globaltradealert.org/)

Note: Only exports on or after February 15, 2026 count toward the quota. The question asks whether the quota is exhausted on or before May 31, 2026 (i.e., before the quota's official June 30 expiry).

**Pre-cutoff background**

On December 24, 2025, Russia established a temporary export tariff quota of 20 million tonnes for grain exports (wheat, meslin, barley, and corn) for the period February 15 to June 30, 2026. The quota was distributed among 213 companies, with approximately 90% allocated based on historical export volumes [https://interfax.com/newsroom/top-stories/116160/](https://interfax.com/newsroom/top-stories/116160/). Exports to Eurasian Economic Union (EAEU) member states are excluded from the quota. The quota for rye was set at zero tonnes.

On April 10, 2026, the Russian government issued Decree No. 393, increasing the quota by an additional 5 million tonnes, bringing the total to 25 million tonnes for the same period [Russian govt confirms additional grain export quota of 5 mln tonnes ...](https://interfax.com/newsroom/top-stories/117071/) [Russia: Temporary grain export tariff quota for 2026 increased by 5 ...](https://globaltradealert.org/state-act/97322-russia-government-increases-the-2026-grain-export-tariff-quota-by-5-million-tonnes-april-2026). This increase was accompanied by adjustments to export duties: in-quota wheat and meslin export duties were zeroed from April 22 to May 13, 2026, and barley and corn duties were also reduced [Russia: Temporary grain export tariff quota for 2026 increased by 5 ...](https://globaltradealert.org/state-act/97322-russia-government-increases-the-2026-grain-export-tariff-quota-by-5-million-tonnes-april-2026). The decision to expand the quota suggests that the original 20 million tonnes was being utilized at a rapid pace.

The USDA's April 2026 Wheat Outlook raised Russia's export estimates due to an increased pace of trade. Whether the full 25 million tonnes is exhausted before June 1, 2026, depends on global wheat demand, the ruble exchange rate, logistics capacity, and the effect of the temporarily zeroed export duties on shipment pace.

For the purposes of this question, "grain" refers specifically to wheat (HS code 1001), meslin, barley (HS code 1003), and corn (HS code 1005), consistent with the commodities covered by the Russian government's quota mechanism.

**Exact later resolution packet**

The question (a straightforward binary, NOT a conditional, so no annulment applies) asks whether Russia's 25 million tonne grain export quota (Feb 15 – June 30, 2026) was "fully utilized" (≥99%, i.e. ≥24.75 million tonnes shipped, OR reported as exhausted/effectively exhausted by a credible source) by 23:59 UTC on May 31, 2026.

The evidence overwhelmingly indicates the quota was NOT exhausted by that date:

1. The quota was expanded from 20M to 25M tonnes on April 10, 2026, and in-quota wheat duties were zeroed (April 22 onward) specifically BECAUSE the export pace was sluggish — a measure to encourage shipments, not a sign of near-exhaustion (per the question description itself).

2. SovEcon's director Andrey Sizov publicly stated the 20 mmt quota "should not be restrictive and is unlikely" to bind, and SovEcon expected Russia to ship only about 15–16 million tonnes of wheat during the entire quota period (through June 30). This is far below the 24.75M-tonne threshold even for the whole period, let alone by May 31.

3. Monthly Russian wheat export estimates show a slow pace: roughly ~4.85M tonnes in March 2026, ~3.8M tonnes in April 2026, and only ~1.9M tonnes (SovEcon) to ~3.3-3.4M tonnes (IKAR) in May 2026. Reporting consistently described exports as "lagging" and curbed by a strong ruble and Black Sea logistics bottlenecks [Strong ruble and Black Sea bottlenecks curb Russia's wheat export ...](https://millermagazine.com/blog/strong-ruble-and-black-sea-bottlenecks-curb-russias-wheat-export-pace-6632). Adding the February partial month (~2-3M) plus barley and corn (small volumes), cumulative grain exports from Feb 15 to end-May were on the order of ~13-17 million tonnes — well under 24.75 million.

4. No report from the Russian Ministry of Agriculture, the Russian government, Interfax, Reuters, or TASS stated that the quota was "exhausted" or "effectively exhausted" by May 31, 2026. A review of Interfax top-stories through June 2, 2026 found no such confirmation [https://interfax.com/newsroom/top-stories/](https://interfax.com/newsroom/top-stories/). (By contrast, in prior tight years such as 2020, Russia explicitly announced quota exhaustion and a suspension of exports — no such announcement occurred for the 2026 quota.)

Therefore, neither resolution condition (≥24.75M tonnes shipped, or a credible exhaustion report) was met by the deadline, and the question resolves NO.

Sources:
- Miller Magazine, "Strong ruble and Black Sea bottlenecks curb Russia's wheat export pace" (https://millermagazine.com/blog/strong-ruble-and-black-sea-bottlenecks-curb-russias-wheat-export-pace-6632) [Strong ruble and Black Sea bottlenecks curb Russia's wheat export ...](https://millermagazine.com/blog/strong-ruble-and-black-sea-bottlenecks-curb-russias-wheat-export-pace-6632)
- Interfax top stories review (https://interfax.com/newsroom/top-stories/) [https://interfax.com/newsroom/top-stories/](https://interfax.com/newsroom/top-stories/)
- SovEcon director (Andrey Sizov) statement that the quota is non-restrictive and ~15-16 mmt of wheat expected over the quota period (https://x.com/sizov_andre/status/2003885158735532076)
- apk-inform monthly export data (https://www.apk-inform.com/en/news/1548222)
- Question description noting duty-zeroing introduced to spur a lagging pace (Global Trade Alert https://globaltradealert.org/state-act/97322).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-203. `e8a42626-3371-5e5e-9587-c8843416aec2`

- Present date: `2026-05-03 04:27:03.895676`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any sovereign nation enter into a new default on external debt between May 1, 2026 and June 1, 2026, as indicated by an S&P Global Ratings 'SD' or 'D' sovereign credit rating action?

**Resolution criteria**

This question resolves **Yes** if, between May 1, 2026 00:00 UTC and June 1, 2026 23:59 UTC, S&P Global Ratings downgrades the long-term foreign currency sovereign credit rating of any sovereign nation to 'SD' (selective default) or 'D' (default), where that sovereign was NOT already rated 'SD' or 'D' immediately prior to May 1, 2026 00:00 UTC.

Key definitions:

- **Sovereign nation**: Any state that is a member of the United Nations as listed at https://www.un.org/en/about-us/member-states.
- **External debt**: Debt denominated in foreign currency. The relevant rating is S&P Global Ratings' **long-term foreign currency** sovereign credit rating, which specifically covers external debt obligations. This excludes local-currency sovereign ratings.
- **Default**: A downgrade to 'SD' (selective default) or 'D' (default) by S&P Global Ratings. An 'SD' rating indicates that the sovereign has selectively defaulted on a specific financial obligation but is expected to continue timely payment of other obligations. A 'D' rating indicates a general default. See S&P's rating definitions at https://www.spglobal.com/ratings/en/about/understanding-credit-ratings.
- **New default**: The sovereign must NOT have been rated 'SD' or 'D' on its long-term foreign currency rating by S&P Global Ratings as of April 30, 2026 23:59 UTC. This excludes countries already in default prior to the resolution window (e.g., Belarus, Lebanon, Venezuela).

**Resolution source**: S&P Global Ratings sovereign rating action press releases, available at https://www.spglobal.com/ratings/en/products-benefits/products/sovereign-ratings. Corroborating reporting from Reuters (https://www.reuters.com), Bloomberg, or the Financial Times may also be used if S&P's page is inaccessible.

**Pre-cutoff background**

Global sovereign debt risks remain elevated in 2026. The IMF's Global Sovereign Debt Roundtable held its 6th meeting in April 2026 to address ongoing restructuring challenges. Moody's global sovereign outlook for 2026 is negative, citing policy and political risks that outweigh pockets of resilience. Rising borrowing costs, trade tensions, and fiscal stress in multiple developing countries have heightened default concerns.

As of early 2026, several countries are already in default or selective default on external obligations. The Council on Foreign Relations Sovereign Risk Tracker identifies Belarus, Lebanon, and Venezuela as currently in actual default. Other countries rated in the CCC/C range by S&P or with equivalent Moody's/Fitch ratings — including Ethiopia, Ghana, Sri Lanka, Zambia, and others undergoing restructuring — face elevated risk but are at various stages of debt treatment.

S&P Global Ratings rates 143 sovereign governments as of February 28, 2026. Sovereign defaults are relatively rare events; in a typical year, only 0–3 new sovereign defaults occur globally. However, the current environment of high interest rates, bond spread shocks, and geopolitical uncertainty elevates the probability above historical base rates. Countries with near-term external debt maturities and limited refinancing access are most vulnerable.

Resolution will be based on S&P Global Ratings sovereign credit rating actions, which are published on their press release page at https://www.spglobal.com/ratings/en/regulatory/article/sovereign-ratings-list-s101674535 and individual rating action announcements.

**Exact later resolution packet**

The question resolves YES only if S&P Global Ratings downgraded the long-term FOREIGN CURRENCY sovereign credit rating of a UN-member sovereign nation to 'SD' or 'D' between May 1, 2026 00:00 UTC and June 1, 2026 23:59 UTC, where the sovereign was NOT already rated SD/D before May 1.

Evidence gathered:

1) No qualifying sovereign downgrade was found. Extensive searches of S&P Global Ratings press releases, Reuters, Bloomberg, FT, EMTA's sovereign rating action log, and cbonds turned up no S&P sovereign long-term foreign currency downgrade to 'SD' or 'D' during the May 1–June 1, 2026 window. The S&P sovereign-related rating actions appearing in this period were corporate (e.g., "Optiv Inc. Downgraded To 'D'" on May 28, 2026; "West Technology Group LLC Downgraded To 'SD'" on May 18, 2026), not sovereign nations.

2) S&P's "Default, Transition, and Recovery: Defaults Slide For The Third Straight Month" report (published May 18, 2026, data as of Apr 30, 2026) lists only corporate defaults for 2026 and reports that defaults in the first four months of 2026 were the lowest for the period since April 2022 — well below the five-year average. No new sovereign defaults are recorded for 2026 [147964].

3) The S&P Sovereign Ratings List (data as of Feb 28, 2026) shows the sovereigns already in SD on their foreign-currency rating were Ethiopia and Lebanon (plus the previously-defaulted set noted in the question: Belarus, Venezuela), all of which pre-date and are explicitly excluded from the resolution window [82bec8].

4) The most-watched near-term default candidates avoided default ahead of the window: Senegal made its ~$471 million eurobond coupon/principal payment in March 2026 (Reuters/Bloomberg confirmed it avoided default); the Maldives successfully settled its USD 500 million sukuk on April 2, 2026 [4b2312]. Bolivia was actually upgraded by S&P to 'CCC+' in March 2026, not defaulted.

Since the antecedent event (a new sovereign foreign-currency SD/D downgrade) did not occur within the window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-204. `25f5a0fb-640d-5442-a001-e798e4f0e56e`

- Present date: `2026-04-30 11:28:28.817662`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. House of Representatives pass a reconciliation bill pursuant to S.Con.Res. 33 by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the U.S. House of Representatives, on or after April 29, 2026, and before June 1, 2026, 11:59 PM UTC, passes a reconciliation bill pursuant to S.Con.Res. 33 (the FY2026 budget resolution adopted by the Senate on April 23, 2026) under the budget reconciliation process as defined by the Congressional Budget Act of 1974 (2 U.S.C. §§ 641–645).

"Passing" means the bill receives a simple majority of votes in favor as recorded in a roll call vote on final passage in the House of Representatives.

The question resolves **No** if no such bill is passed by the House before the deadline.

**Resolution source:** Official roll call vote records published by the Clerk of the House at https://clerk.house.gov/Votes or the bill's legislative actions page on https://www.congress.gov. The bill must be identified as providing for reconciliation pursuant to S.Con.Res. 33 or the corresponding budget resolution instructions.

**Pre-cutoff background**

On April 23, 2026, the U.S. Senate adopted S.Con.Res. 33, a budget resolution for FY2026, by a 50-48 vote [https://www.politico.com/news/2026/04/23/anorexic-reconciliation-bill-could-mean-planned-parenthood-gets-re-funded-00889576](https://www.politico.com/news/2026/04/23/anorexic-reconciliation-bill-could-mean-planned-parenthood-gets-re-funded-00889576). This resolution sets up a second round of budget reconciliation ("Reconciliation 2.0") during the 119th Congress, primarily focused on funding the Department of Homeland Security (DHS), including Border Patrol and Immigration and Customs Enforcement.

The first reconciliation bill of the 119th Congress (H.R.1, pursuant to H.Con.Res. 14) was enacted as Public Law 119-21 on July 4, 2025 [H.R.1 - 119th Congress (2025-2026): An act to provide for ...](https://www.congress.gov/bill/119th-congress/house-bill/1). This new effort represents a separate reconciliation vehicle.

As of April 29, 2026, House Republican leaders are scrambling to build support for the Senate's approach, but internal GOP divisions create significant uncertainty. Key disagreements include:
- Whether the bill should remain narrowly focused on immigration enforcement ("skinny" or "anorexic" bill) or include broader provisions such as extending Planned Parenthood defunding from last year's reconciliation bill [https://www.politico.com/news/2026/04/23/anorexic-reconciliation-bill-could-mean-planned-parenthood-gets-re-funded-00889576](https://www.politico.com/news/2026/04/23/anorexic-reconciliation-bill-could-mean-planned-parenthood-gets-re-funded-00889576).
- House Budget Committee Chairman Jodey Arrington has stated that House GOP appetite for the Senate's narrow reconciliation path is "no sure bet" [https://www.politico.com/news/2026/04/23/anorexic-reconciliation-bill-could-mean-planned-parenthood-gets-re-funded-00889576](https://www.politico.com/news/2026/04/23/anorexic-reconciliation-bill-could-mean-planned-parenthood-gets-re-funded-00889576).
- Speaker Mike Johnson is expected to release policy priorities for a potential third reconciliation bill, which some members prefer as the vehicle for additional provisions.

The House has a narrow Republican majority, meaning only a few defections could sink the bill. The reconciliation process allows passage by simple majority in both chambers, bypassing the Senate filibuster, per the Congressional Budget Act of 1974.

**Exact later resolution packet**

The question resolves NO. It asks specifically whether the U.S. House passed a RECONCILIATION BILL pursuant to S.Con.Res. 33 (not the budget resolution itself) via a roll call vote on final passage, between April 29 and June 1, 2026 (11:59 PM UTC).

Key distinction: On April 29, 2026, the House adopted the budget RESOLUTION S.Con.Res. 33 by a 215-211 vote (see https://www.naco.org/news/house-clears-budget-resolution-advancing-reconciliation-20-fund-dhs-and-cbp and govtrack vote h143). This was only the budget resolution that unlocks the reconciliation process — NOT a reconciliation bill. The question explicitly requires a reconciliation bill passed pursuant to S.Con.Res. 33.

The actual reconciliation bill text (a ~$72 billion package to fund ICE/CBP and immigration enforcement) was released by Senate committees in early-mid May 2026 (around May 4-5). However, the process stalled: the Senate parliamentarian flagged Byrd-rule violations on May 14 and May 16, 2026 [00c39a]. Then, in a rare rebuke, Republicans abruptly postponed/canceled votes on the reconciliation package tied to ICE funding around May 21, 2026, pushing action until after the Memorial Day recess (Memorial Day 2026 = May 25; recess extends into early June) [4ef62a]. Politico likewise reported the House "could leave town, blowing Trump's deadline for immigration" funding, considering delaying the vote until after the Memorial Day recess (https://www.politico.com/live-updates/2026/05/21/congress/house-ponders-reconciliation-delay-00931986).

Because the reconciliation bill vote was delayed past the Memorial Day recess (into June, after the June 1, 2026 deadline) and there is no record of the House passing such a reconciliation bill before June 1, 2026, the condition for YES was not met. Resolution = NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-205. `c96dda2a-a6cc-523c-99f1-a44781c3b4ec`

- Present date: `2026-05-29 02:26:15.986158`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will any of the ~70 individuals charged in the Beirut port blast investigation be arrested or detained by Lebanese authorities between May 12, 2026, and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, between May 12, 2026 (00:00 EEST, UTC+3) and July 1, 2026 (23:59 EEST, UTC+3), at least one individual among the approximately 70 persons charged by investigative Judge Tarek Bitar in the Beirut port blast case (file concluded March 30, 2026) is arrested or detained by Lebanese authorities. This question resolves **No** otherwise.

**Key definitions:**

- **"Charged"**: Refers to the approximately 70 individuals against whom Judge Tarek Bitar filed charges upon concluding his investigation on March 30, 2026, as reported by TIMEP (https://timep.org/2026/04/22/the-prolonged-chapters-of-the-investigations-into-the-beirut-port-blast/) and L'Orient Today (https://today.lorientlejour.com/article/1501467/judge-bitar-concludes-investigation-into-beirut-port-blast.html). Should a formal indictment list be published by the Lebanese judiciary before resolution, that list shall be authoritative. Otherwise, any individual credibly reported by at least two of the verification sources below as having been charged by Bitar in the port blast case qualifies.

- **"Arrested or detained"**: Taken into physical custody by Lebanese law enforcement, judicial police, or military/security forces pursuant to a judicial order (e.g., arrest warrant, detention order). This includes: being physically apprehended and held at a police station, military facility, or prison; or being brought before a judicial authority under compulsion. It does **not** include: voluntary appearance before a judge without custodial measures, travel bans, asset freezes, fines, or summonses that are not enforced through physical custody. House arrest (i.e., confinement to a residence enforced by authorities) **does** count.

- **"Lebanese authorities"**: Any organ of the Lebanese state with law enforcement or judicial enforcement powers, including but not limited to the Internal Security Forces (ISF), the Lebanese Armed Forces (LAF), General Security, and judicial police acting under orders of Lebanese courts or prosecutors. See https://en.wikipedia.org/wiki/Internal_Security_Forces_(Lebanon) and https://en.wikipedia.org/wiki/Lebanese_Armed_Forces for reference.

- The arrest or detention must occur **on or after May 12, 2026**. Any individual already in custody or previously detained and released before this date does not count.

**Verification sources:** Resolution will be determined by credible reporting from at least one of the following:
1. Lebanon's National News Agency (NNA): https://www.nna-leb.gov.lb/en
2. L'Orient Today: https://today.lorientlejour.com/
3. Reuters: https://www.reuters.com/
4. Associated Press: https://apnews.com/
5. AFP / France 24: https://www.france24.com/en/

If none of these sources report an arrest or detention of any charged individual by July 1, 2026 (23:59 EEST), the question resolves **No**.

**Pre-cutoff background**

On August 4, 2020, a massive explosion at the Port of Beirut killed at least 218 people and caused billions of dollars in damage. Investigative Judge Tarek Bitar was assigned to lead the judicial investigation but faced years of political obstruction, including recusal claims and countercharges filed by suspects and allies [The Prolonged Chapters of the Investigations into the Beirut Port Blast](https://timep.org/2026/04/22/the-prolonged-chapters-of-the-investigations-into-the-beirut-port-blast/).

On March 30, 2026, Judge Bitar concluded his investigation and charged approximately 70 individuals—including politicians, senior security officials, and civil servants—referring the dossier to Prosecutor General Jamal Hajjar for review [The Prolonged Chapters of the Investigations into the Beirut Port Blast](https://timep.org/2026/04/22/the-prolonged-chapters-of-the-investigations-into-the-beirut-port-blast/). Hajjar must review the file and submit formal recommendations before Bitar issues an indictment ruling and refers defendants to the Judicial Council for trial. As of April 2026, indictment was expected by approximately July 2026.

Key charged figures include former ministers Ghazi Zaiter (former Minister of Public Works) and Ali Hassan Khalil (former Finance Minister). Both have historically refused to appear before Judge Bitar and filed multiple recusal claims against him. On January 16, 2025 (upheld in January 2026), the Beirut First Instance Court found them guilty of "abuse of right" for obstructing the investigation and ordered them to pay 10 billion Lebanese pounds in compensation [The Prolonged Chapters of the Investigations into the Beirut Port Blast](https://timep.org/2026/04/22/the-prolonged-chapters-of-the-investigations-into-the-beirut-port-blast/). As of the TIMEP report dated April 22, 2026, neither Zaiter nor Khalil has been arrested or detained in connection with the blast investigation. No public reporting indicates any of the ~70 charged individuals are currently in custody specifically for the port blast case.

The document notes a persistent "culture of impunity" in Lebanon whereby judicial orders against powerful political figures have historically gone unenforced [The Prolonged Chapters of the Investigations into the Beirut Port Blast](https://timep.org/2026/04/22/the-prolonged-chapters-of-the-investigations-into-the-beirut-port-blast/). However, the post-2024 political environment following the weakening of Hezbollah's influence has created new openings for judicial action. The case is now at a critical procedural juncture: the prosecutor's review and potential indictment could trigger arrest warrants, but enforcement remains uncertain.

A definitive, publicly available list of all 70 charged individuals has not been published as of May 12, 2026. The TIMEP analysis and reporting by L'Orient Today, Asharq Al-Awsat, and Shafaq News confirm the approximate number but do not enumerate all names. The list is expected to become public upon formal indictment.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question asked whether at least one of the ~70 individuals charged by Judge Tarek Bitar in the Beirut port blast case would be arrested or detained (taken into physical custody, including house arrest) by Lebanese authorities between May 12, 2026 (00:00 EEST) and July 1, 2026 (23:59 EEST), per reporting from NNA, L'Orient Today, Reuters, AP, or AFP/France 24.

KEY FINDINGS:

1. Procedural status at start of window: Bitar concluded his investigation on March 30, 2026 and referred the entire dossier to Prosecutor General Jamal Hajjar for review. Per L'Orient Today (https://today.lorientlejour.com/article/1501467/judge-bitar-concludes-investigation-into-beirut-port-blast.html) [Beirut Port explosion: Bitar closes investigation, focusing on indictment](https://today.lorientlejour.com/article/1501467/judge-bitar-concludes-investigation-into-beirut-port-blast.html) and Naharnet (https://www.naharnet.com/stories/en/319246-bitar-concludes-port-blast-probe-refers-it-to-public-prosecutor) [Bitar concludes port blast probe, refers it to public prosecutor](https://www.naharnet.com/stories/en/319246-bitar-concludes-port-blast-probe-refers-it-to-public-prosecutor), as of the referral NO ONE was in custody; Hajjar was still to review the file and give his opinion (including on whether to detain the ~70 defendants), after which the file would return to Bitar to issue his indictment ruling. An indictment was the prerequisite for the new phase of arrest warrants, and it had not been issued.

2. No indictment issued during the window: Reporting indicated the indictment was expected around the fifth anniversary (August 4) or later. Mid-June 2026 social/media posts (e.g., France 24 Arabic and MC Doualiya Instagram/Facebook items dated June 17–19, 2026: https://www.instagram.com/reel/DWjLsr2DPQA/ and https://www.facebook.com/FRANCE24.Arabic/videos/951736890683412/) show families still "awaiting the indictment ruling" ("الأهالي ناطرين القرار الاتهامي"), confirming that as of mid-to-late June 2026 the indictment had not been issued and the case was still stuck on a legal obstacle.

3. No arrest/detention reported by any allowed source: Extensive searching of NNA, L'Orient Today, Reuters, AP, and AFP/France 24 coverage found NO report of any of the ~70 charged individuals (including former ministers Ghazi Zaiter/Zeaiter and Ali Hassan Khalil) being taken into physical custody within the window. The only arrest-related news in this period concerns Igor Grechushkin, the Russian-Cypriot shipowner detained in BULGARIA (in September 2025, not by Lebanese authorities, and not within the window) — which does not qualify.

4. Historical/contextual consistency: Prior arrest warrants Bitar issued (e.g., against Khalil and Fenianos in 2021) were never enforced; these ex-ministers were never arrested. The TIMEP report (April 22, 2026) explicitly stated neither Zaiter nor Khalil had been arrested/detained and that no charged individual was in custody for the port blast — consistent with the "culture of impunity."

CONCLUSION: The antecedent event (an arrest or detention of a charged individual by Lebanese authorities between May 12 and July 1, 2026) did not occur. No allowed verification source reported any such custody. The question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-206. `e7724985-2223-549c-b3aa-cebfc366e4a9`

- Present date: `2026-05-01 19:10:48.101070`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Russian forces capture the village of Novodmytrivka (east of Kostiantynivka) by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, at any point between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), the village of Novodmytrivka (east of Kostiantynivka, Donetsk Oblast) is shown as under Russian control according to either:

1. **The DeepState interactive map** (https://deepstatemap.live/en) — the village area is shaded in the color indicating Russian-controlled territory (currently red), as opposed to the "grey zone" (contested) or Ukrainian-controlled territory; OR
2. **ISW's daily Russian Offensive Campaign Assessments** (https://understandingwar.org/research/russia-ukraine/) — the assessment explicitly states that Russian forces "captured," "seized," or "occupied" Novodmytrivka, or ISW's accompanying map shows the village within Russian-claimed control lines.

The question resolves **No** if, as of June 1, 2026 (23:59 UTC), neither source reflects Russian capture/control of the village — including if the village remains in a "grey zone" (contested), under Ukrainian control, or if control status is ambiguous.

**If primary sources become unavailable:** If both DeepState and ISW cease updating or become inaccessible before June 1, 2026, the question resolves based on the last available update from either source. If neither source has ever shown Russian control of Novodmytrivka in any update published on or after April 30, 2026, the question resolves **No**.

**Pre-cutoff background**

Novodmytrivka is a village located east of Kostiantynivka in Donetsk Oblast, Ukraine. It has become a key tactical objective for Russian forces attempting to bypass Ukrainian defenses in the Chasiv Yar sector. According to Euromaidan Press (April 27, 2026), Russian forces have shifted from armored assaults to infantry infiltration tactics to seize the village, as capturing it would cut Ukrainian reinforcement routes and provide access to the H20 highway toward Kramatorsk [https://euromaidanpress.com/2026/04/27/chasiv-yar-plan/](https://euromaidanpress.com/2026/04/27/chasiv-yar-plan/). As of April 27, 2026, the village remains under Ukrainian control but is actively contested, with the source noting "Novodmytrivka holds for now" [https://euromaidanpress.com/2026/04/27/chasiv-yar-plan/](https://euromaidanpress.com/2026/04/27/chasiv-yar-plan/). ISW assessments from mid-April 2026 report Russian forces attacking north of Kostiantynivka toward Novodmytrivka and near Minkivka. The Kostiantynivka front saw 29 Russian attacks on April 26, 2026 alone, making it one of the most active sectors. Russian infiltrations have reportedly bypassed some Ukrainian positions in the area, increasing pressure on the village's defenders.

**Exact later resolution packet**

The question resolves NO. Neither qualifying source (DeepState shaded red, OR ISW explicitly stating "captured/seized/occupied" or showing it within Russian-claimed control lines) reflected Russian control of Novodmytrivka (east of Kostiantynivka, Donetsk Oblast) at any point in the April 30 – June 1, 2026 window.

ISW evidence (none confirms Russian control of this specific village):
- April 29, 2026 (just before the window): ISW only relayed a Russian claim — "The Russian MoD claimed on April 29 that Russian forces seized Novodmytrivka (east of Kostyantynivka)," and a Kremlin-affiliated milblogger added that Russian forces "will be unable to establish full control of Novodmytrivka" without first seizing other positions. ISW did not independently confirm seizure [fb00c2].
- May 8, 2026: ISW directly contradicted the Russian claim, stating "Ukrainian forces maintain positions near Kostyantynivka in areas that Russian sources previously claimed as Russian-occupied," citing geolocated footage of Russian forces striking Ukrainian positions in southern Novodmytrivka (north of Kostyantynivka), and noting a milblogger "continued to claim on May 8 that Russian forces cleared Novodmytrivka" — i.e., still only a claim, with Ukrainian forces present [44e922].
- May 25, 27, 28, 29 ISW assessments: no statement that Russian forces captured/seized/occupied the Kostiantynivka-area Novodmytrivka; the Kostiantynivka-Druzhkivka sector was described in terms of infiltration missions and even some Ukrainian advances [aaa0ec, 4327e8, 93614c, 5741ef]. (Note: the May 28 report mentions a different Novodmytrivka "west of Popivka" in the Sumy direction — a distinct village, not the one in question [93614c].)
- ISW's May 30, 2026 "Assessed Control of Terrain near Kostyantynivka" map did not show Novodmytrivka within Russian-claimed control lines [0e5230].

DeepState / Ukrainian sources:
- DeepState reporting throughout late April–May 2026 described the Novodmytrivka area east/southeast of Kostiantynivka as a zone of Russian "infiltration"/"просочування" (grey/contested), not captured. A May 2, 2026 Reuters piece citing DeepState placed Russian control only ~1 km from Kostiantynivka's southern outskirts and noted only the Russian MoD's (unconfirmed) claim of taking Novodmytrivka.
- A comprehensive April 2026 list of occupied Donetsk settlements (using DeepState/ministry data) did NOT list a Novodmytrivka under the Kostiantynivka hromada (the Novodmytrivka it lists as occupied is in the Kurakhivska hromada, a different village) [f0f88f].

Because the Russian capture claim was never confirmed by either qualifying source as Russian-controlled during the resolution window — the village remained contested/under Ukrainian-held positions (grey zone) — the resolution criteria's NO condition is met.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-207. `319b28f3-a704-5a3f-83d6-0e7721b5539d`

- Present date: `2026-04-29 16:49:29.561012`
- Source cutoff boundary: `2026-04-30` (encodes end of UTC day `2026-04-29`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any of the four Disney CEO candidates (D'Amaro, Walden, Bergman, or Pitaro) announce their departure from Disney by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between the question's open date and June 1, 2026 (23:59 UTC), any of the following four individuals — Josh D'Amaro, Dana Walden, Alan Bergman, or Jimmy Pitaro — publicly announces or is publicly announced to be departing The Walt Disney Company.

**Definition of "departure":** A departure includes any of the following: resignation, termination, retirement, or announcement that the individual will leave Disney by a specified future date. It does NOT include a change of title or role within Disney (e.g., moving from one division to another), unless accompanied by a simultaneous announcement that the individual will ultimately leave the company. An individual moving to a temporary "advisory" or "consulting" role with a defined end date counts as a departure.

**Definition of "announcement":** The departure must be confirmed by at least one of the following:
1. An official Disney press release published on the [Disney Newsroom](https://thewaltdisneycompany.com/press-releases/);
2. An SEC filing on [Disney's EDGAR page](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1744489&type=8-K&dateb=&owner=include&count=40);
3. Credible reporting from at least two of the following outlets: The Wall Street Journal, The New York Times, Reuters, Bloomberg, Variety, The Hollywood Reporter, Deadline, or the Los Angeles Times.

The announcement must occur on or after the question's open date and on or before June 1, 2026 (23:59 UTC). If no such announcement is made within this window, the question resolves **No**.

**Pre-cutoff background**

In February 2026, The Walt Disney Company named Josh D'Amaro as the successor to CEO Bob Iger. D'Amaro officially assumed the CEO role on March 18, 2026, becoming Disney's ninth chief executive. The other three internal CEO candidates were passed over:

- **Josh D'Amaro** — Now CEO of The Walt Disney Company as of March 18, 2026. Previously chairman of Disney Experiences (parks division).
- **Dana Walden** — Named president and chief creative officer of The Walt Disney Company effective March 18, 2026, overseeing an expanded Disney Entertainment segment including film studios. Previously co-chair of Disney Entertainment.
- **Alan Bergman** — Remains as chairman of Disney Entertainment Studios, now reporting to Walden. Reports indicate Bergman is "miserable" and "sad" about the new reporting structure, per the New York Post (March 17, 2026).
- **Jimmy Pitaro** — Remains as chairman of ESPN. Bloomberg reported that Pitaro withdrew from CEO consideration prior to the announcement. He addressed ESPN staff in a memo regarding Disney layoffs in April 2026.

Historically, losing Disney CEO candidates have departed: Tom Staggs left in 2016 after being passed over, and Kevin Mayer departed in 2020. This creates a meaningful probability that at least one of the passed-over candidates may announce a departure, with Bergman appearing the most likely given reported dissatisfaction. However, the short timeframe (roughly five weeks) constrains the probability.

**Exact later resolution packet**

The question resolves NO. Between the open date (2026-04-29) and June 1, 2026 (23:59 UTC), none of the four named individuals — Josh D'Amaro, Dana Walden, Alan Bergman, or Jimmy Pitaro — announced or were announced to be departing The Walt Disney Company.

Status of each as established for the new leadership structure effective March 18, 2026:
- Josh D'Amaro became CEO of The Walt Disney Company (he is the new chief executive, not departing).
- Dana Walden became President and Chief Creative Officer (a promotion, not a departure). See Deadline (https://deadline.com/2026/02/dana-walden-disney-film-oversight-glass-ceiling-intact-1236707221/) and LA Times (https://www.latimes.com/entertainment-arts/business/story/2026-03-16/disneys-dana-walden-sets-leadership-team-bergman).
- Alan Bergman remained as Chairman of Disney Entertainment, Studios, now reporting to Walden. Disney's own press release lists him in his continuing role (https://thewaltdisneycompany.com/press-releases/the-walt-disney-company-sets-leadership-team-for-expanded-disney-entertainment-segment/). The Hollywood Reporter reported "Disney says that CEO contenders Alan Bergman and Jimmy Pitaro will keep working in their 'critical' roles." While the New York Post (March 17, 2026) reported Bergman was "miserable," reporting only a change in reporting structure — not a departure.
- Jimmy Pitaro remained Chairman of ESPN; he addressed staff regarding layoffs in April 2026 in that ongoing capacity (no departure).

Deadline's March 2026 piece explicitly characterized the transition as "drama-free," noting "Key leaders from Dana Walden to Alan Bergman down the new org chart are staying put" (https://deadline.com/2026/03/disneys-ceo-succession-drama-free-history-1236759283/).

A check of Disney's SEC/EDGAR 8-K filings found that the only executive departure filed in early 2026 was that of Chief Communications Officer Kristina Schake (terminated without cause, per the 8-K filed Feb 20, 2026; https://www.sec.gov/Archives/edgar/data/1744489/000174448926000025/dis-20260220.htm) — she is not one of the four named individuals. The May 6, 2026 8-K was a routine quarterly earnings report, not a departure filing.

No Disney Newsroom press release, SEC 8-K, or reporting from two or more of the named outlets (WSJ, NYT, Reuters, Bloomberg, Variety, THR, Deadline, LA Times) announced a departure of any of the four within the window. Therefore the consequent did not occur and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-208. `b34fbcf1-aeb7-57cf-957f-47043a721b8c`

- Present date: `2026-05-16 22:08:48.399471`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will San Francisco Proposition D (CEO pay-ratio tax) pass in the June 2, 2026 election?

**Resolution criteria**

This question resolves **Yes** if San Francisco Proposition D receives more than 50% "Yes" votes (a simple majority, as required for citizen-initiated measures under California law) in the June 2, 2026 election, as certified by the San Francisco Department of Elections [San Francisco, California, Measure D, Changes to Top Executive ...](https://ballotpedia.org/San_Francisco,_California,_Measure_D,_Changes_to_Top_Executive_Pay_Tax_Initiative_(June_2026)).

This question resolves **No** if Proposition D receives 50% or fewer "Yes" votes, is withdrawn from the ballot, or is otherwise not voted upon.

**Resolution source:** Official certified election results published by the San Francisco Department of Elections at https://sfelections.sfgov.org/ (results page: https://sf.gov/results) [https://sfelections.sfgov.org](https://sfelections.sfgov.org).

**Timing and certification:** San Francisco typically certifies election results within approximately 30 days of Election Day. If official certification has not occurred by July 1, 2026, 11:59 PM UTC, the question will resolve based on the most recent official (but not yet certified) results published by the Department of Elections as of that deadline. If a recount is initiated and not completed by July 1, 2026, 11:59 PM UTC, the question resolves based on the last official results available at that time; if a recount later changes the outcome, the resolution stands as determined at the deadline.

**Pre-cutoff background**

San Francisco's June 2, 2026 Consolidated Statewide Direct Primary Election includes Proposition D (also known as the "Overpaid CEO Act"), a citizen-initiated ballot measure that would expand and increase the city's existing tax on businesses where top executives earn disproportionately more than their workers [San Francisco, California, Measure D, Changes to Top Executive ...](https://ballotpedia.org/San_Francisco,_California,_Measure_D,_Changes_to_Top_Executive_Pay_Tax_Initiative_(June_2026)).

**Existing law:** In November 2020, San Francisco voters approved Proposition L, establishing an "Overpaid Executive Gross Receipts Tax" on businesses where the highest-paid executive earns more than 100 times the median employee's compensation, with rates of 0.1%–0.6% of gross receipts or 0.4%–2.4% of payroll expenses. These rates were subsequently reduced by Proposition M, approved in November 2024 [San Francisco, California, Measure D, Changes to Top Executive ...](https://ballotpedia.org/San_Francisco,_California,_Measure_D,_Changes_to_Top_Executive_Pay_Tax_Initiative_(June_2026)).

**What Proposition D would do:** Proposition D would increase the tax rates (gross receipts-based rates to 0.183%–1.121%; payroll-based rates to 0.75%–4.47%), change the pay-ratio calculation to include compensation of all employees rather than only San Francisco-based workers, prohibit the Board of Supervisors from reducing tax rates without voter approval, and increase the city's appropriations limit for four years [San Francisco, California, Measure D, Changes to Top Executive ...](https://ballotpedia.org/San_Francisco,_California,_Measure_D,_Changes_to_Top_Executive_Pay_Tax_Initiative_(June_2026)).

**Political dynamics:** The measure is supported by labor unions (SEIU Local 1021), U.S. Senator Bernie Sanders, former House Speaker Nancy Pelosi, and progressive groups. It is opposed by San Francisco Mayor Daniel Lurie, the San Francisco Chamber of Commerce, and several large corporations and billionaire donors [San Francisco, California, Measure D, Changes to Top Executive ...](https://ballotpedia.org/San_Francisco,_California,_Measure_D,_Changes_to_Top_Executive_Pay_Tax_Initiative_(June_2026)). A competing measure, Proposition C, has also been placed on the ballot by opponents seeking to counteract Proposition D's provisions [https://sfelections.sfgov.org](https://sfelections.sfgov.org).

Full text of Proposition D: https://www.sf.gov/documents/47869/20251031_Legal_Text_Changes_to_Business_Tax_Based_on_Comparison_of_Top.pdf

Ballotpedia page: https://ballotpedia.org/San_Francisco,_California,_Measure_D,_Changes_to_Top_Executive_Pay_Tax_Initiative_(June_2026)

**Exact later resolution packet**

San Francisco Proposition D (the "Overpaid CEO Act," officially titled "Changes to Business Tax Based on Comparison of Top Executive's Pay") FAILED in the June 2, 2026 Consolidated Statewide Direct Primary Election, receiving well under the simple majority required. Therefore the question resolves NO (0).

Key evidence (official source):
- The San Francisco Department of Elections "Final Summary Report" (certified), dated June 25, 2026, at https://www.sfelections.org/results/20260602/data/20260625/summary.pdf, lists the ballot measures. It records Measure/Proposition D receiving 118,802 "Yes" votes (47.19%) and 132,959 "No" votes (52.81%) [https://www.sfelections.org/results/20260602/data/20260625/summary.pdf](https://www.sfelections.org/results/20260602/data/20260625/summary.pdf). Since 47.19% is not strictly greater than 50%, the measure did not pass.
- This same certified report confirms the identity: Measure D corresponds to "Changes to Business Tax Based on Comparison of Top Executive's Pay" (the Overpaid CEO tax) [https://www.sfelections.org/results/20260602/data/20260625/summary.pdf](https://www.sfelections.org/results/20260602/data/20260625/summary.pdf). (The competing measure, Proposition C, also failed with 34.02% Yes [https://www.sfelections.org/results/20260602/data/20260625/summary.pdf](https://www.sfelections.org/results/20260602/data/20260625/summary.pdf).)
- These are the CERTIFIED totals, not merely uncertified results — the SF Department of Elections issued its certification letter for the June 2, 2026 election dated June 25, 2026 (CertificationLetterJun22026.pdf in the same official results directory), which is before the July 1, 2026 11:59 PM UTC deadline. The document is titled the "Final Summary Report" dated 2026-06-25 [https://www.sfelections.org/results/20260602/data/20260625/summary.pdf](https://www.sfelections.org/results/20260602/data/20260625/summary.pdf).

Corroboration:
- Wikipedia's article on 2026 San Francisco Proposition D, citing the SF Department of Elections, reports the measure failed with roughly 47.18% Yes / 52.82% No (an essentially identical near-final count) [2026 San Francisco Proposition D - Wikipedia](https://en.wikipedia.org/wiki/2026_San_Francisco_Proposition_D).
- Multiple independent news outlets (NYT, KQED "San Francisco's Overpaid CEO Tax Fails to Pass," Mission Local "SF's 'Overpaid CEO' tax fails," Fox Business, taxprofblog) all reported that SF voters rejected Proposition D.

The measure was on the ballot and was voted upon (not withdrawn), so the resolution turns purely on the vote share. With 47.19% Yes (< 50%) in the official certified results, Proposition D did NOT pass.

Resolution source URL (official SF Department of Elections): https://www.sfelections.org/results/20260602/data/20260625/summary.pdf

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-209. `f8e3872f-53ee-5261-aa44-16a85efd6a9f`

- Present date: `2026-05-14 02:27:18.613381`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-29T00:00:00`

**Question**

Will the FDA approve Unicycive Therapeutics' Oxylanthanum Carbonate (OLC) NDA by June 29, 2026?

**Resolution criteria**

This question resolves **Yes** if the U.S. Food and Drug Administration (FDA) issues an Approval Letter for Unicycive Therapeutics' New Drug Application (NDA) for Oxylanthanum Carbonate (OLC) on or after May 12, 2026, and on or before June 29, 2026 (11:59 PM Eastern Time).

This question resolves **No** if any of the following occur:
- The FDA issues a Complete Response Letter (CRL) for the OLC NDA.
- The FDA issues a Refuse to File letter or otherwise rejects the application.
- The PDUFA target action date is extended beyond June 29, 2026, and no approval is issued by that date.
- No FDA approval decision is publicly announced by 11:59 PM ET on June 29, 2026.

"FDA approval" is defined as the issuance of an official Approval Letter for the NDA, as reflected in the FDA's Drugs@FDA database (https://www.accessdata.fda.gov/scripts/cder/daf/) or confirmed via an official Unicycive Therapeutics press release on their investor relations page (https://ir.unicycive.com/news). Tentative approval does not count as approval and would resolve No.

**Pre-cutoff background**

Unicycive Therapeutics (Nasdaq: UNCY) is developing Oxylanthanum Carbonate (OLC), a next-generation lanthanum-based oral phosphate binder for the treatment of hyperphosphatemia in patients with chronic kidney disease (CKD) on dialysis. OLC is being reviewed under a 505(b)(2) New Drug Application (NDA) pathway.

In June 2025, the FDA issued a Complete Response Letter (CRL) for OLC's original NDA. The CRL cited a single deficiency related to the compliance status of Unicycive's original third-party manufacturing vendor. Crucially, the CRL was not related to OLC's safety or efficacy [Unicycive Therapeutics Announces Resubmission of New Drug ...](https://ir.unicycive.com/news/detail/116/unicycive-therapeutics-announces-resubmission-of-new-drug).

On December 29, 2025, Unicycive announced the resubmission of its NDA for OLC [Unicycive Therapeutics Announces Resubmission of New Drug ...](https://ir.unicycive.com/news/detail/116/unicycive-therapeutics-announces-resubmission-of-new-drug). On January 29, 2026, the FDA accepted the resubmission and designated it as a Class II complete response, which entails a six-month review period. The FDA assigned a Prescription Drug User Fee Act (PDUFA) target action date of June 29, 2026 [UPDATE - Unicycive Therapeutics Announces FDA Acceptance of ...](https://ir.unicycive.com/news/detail/118/update---unicycive-therapeutics-announces-fda-acceptance-of).

The resubmission is supported by data from three clinical studies (a Phase 1 study, a bioequivalence study, and a tolerability study in CKD patients on dialysis), as well as updated chemistry, manufacturing, and controls (CMC) data [UPDATE - Unicycive Therapeutics Announces FDA Acceptance of ...](https://ir.unicycive.com/news/detail/118/update---unicycive-therapeutics-announces-fda-acceptance-of). As of May 2026, the FDA review remains on track with the June 29, 2026 PDUFA date.

Key uncertainty factors include: whether the third-party manufacturing vendor has fully resolved all FDA-cited deficiencies, whether the FDA will require additional information or inspections, and the general unpredictability of FDA regulatory decisions even when prior CRL issues were manufacturing-related rather than clinical.

**Exact later resolution packet**

The question resolves **NO (0)**.

The question asked whether the FDA would issue an Approval Letter for Unicycive Therapeutics' Oxylanthanum Carbonate (OLC) NDA on or after May 12, 2026 and on or before June 29, 2026 (11:59 PM ET). The resolution criteria explicitly state the question resolves NO if the FDA issues a Complete Response Letter (CRL) or if no approval decision is publicly announced by 11:59 PM ET on June 29, 2026.

Evidence:
- Unicycive Therapeutics' official investor relations press release, titled "Unicycive Therapeutics Receives Complete Response Letter from FDA Regarding Resubmitted Oxylanthanum Carbonate (OLC) New Drug Application (NDA)" (https://ir.unicycive.com/news/detail/123/unicycive-therapeutics-receives-complete-response-letter), dated June 30, 2026, confirms that the FDA issued a Complete Response Letter (CRL), NOT an approval. The CRL was based on unresolved third-party manufacturing deficiencies (the required inspection of the third-party facility did not occur during the review period) — the same category of issue cited in the original June 2025 CRL [News - Unicycive Therapeutics, Inc. (UNCY)](https://ir.unicycive.com/news/detail/123/unicycive-therapeutics-receives-complete-response-letter).
- The corresponding GlobeNewswire press release (https://www.globenewswire.com/news-release/2026/06/30/3319541/0/en/unicycive-therapeutics-receives-complete-response-letter-from-fda-regarding-resubmitted-oxylanthanum-carbonate-olc-new-drug-application-nda.html), also dated June 30, 2026, confirms the same: a CRL was issued regarding the resubmitted NDA, tied to the June 29, 2026 PDUFA target action date. The PDUFA date was not extended; the application was rejected via issuance of a CRL [Unicycive Therapeutics Receives Complete Response Letter](https://www.globenewswire.com/news-release/2026/06/30/3319541/0/en/unicycive-therapeutics-receives-complete-response-letter-from-fda-regarding-resubmitted-oxylanthanum-carbonate-olc-new-drug-application-nda.html).

Therefore, no Approval Letter was issued by the June 29, 2026 deadline. Instead, the FDA issued a CRL, which under the resolution criteria explicitly resolves the question NO. This is a full CRL (a rejection requiring the company to seek an FDA meeting to resolve deficiencies), not a tentative approval or any form of approval.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-210. `59c41d76-8f13-5162-96cf-8111d30e0faa`

- Present date: `2026-05-13 23:39:52.213597`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-06-15T00:00:00`

**Question**

Will Lisa Murkowski vote in favor of the $72 billion immigration enforcement reconciliation bill on final Senate passage?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026, Senator Lisa Murkowski casts a "Yea" vote on the final Senate passage of the immigration enforcement reconciliation bill originating from the budget resolution S.Con.Res.33 (119th Congress). This question resolves **No** if she casts a "Nay" vote, votes "Present," or does not vote on final passage.

**Definitions:**
- **"Final Senate passage"** means the roll call vote on passage of the reconciliation bill as a whole (not on procedural motions, amendments, or cloture votes). This is the vote that, if successful, sends the bill to conference or to the President.
- **"Vote in favor"** means a recorded "Yea" vote on the official Senate roll call.

**Resolution source:** The official U.S. Senate roll call vote record, available at https://www.senate.gov/legislative/votes.htm or https://www.congress.gov/. The specific roll call vote page for the bill will be used.

If the reconciliation bill does not receive a final Senate passage vote by July 1, 2026, this question resolves **No**.

**Pre-cutoff background**

On April 23, 2026, the U.S. Senate passed a budget resolution (S.Con.Res.33) by a 50-48 vote, setting the stage for a reconciliation bill focused on immigration enforcement. Republican Senators Lisa Murkowski (R-AK) and Rand Paul (R-KY) broke ranks, joining all Democrats in voting against the resolution [Senate Committees Introduce Reconciliation Bills Funding ICE and ...](https://www.fairus.org/legislation/congress/senate-committees-introduce-reconciliation-bills-funding-ice-and-border-patrol).

On May 4, 2026, Senate Republicans released the text of a roughly $72 billion reconciliation bill. The legislation includes over $30 billion for ICE hiring, training, and removal operations; $19.1 billion for Customs and Border Protection (CBP) personnel; $7.45 billion for ICE personnel and operations; and $1 billion for U.S. Secret Service security upgrades [Senate Republicans Release $72 Billion Reconciliation Bill Funding ...](https://nlihc.org/resource/senate-republicans-release-72-billion-reconciliation-bill-funding-ice-cbp-and-white-house)[Senate Committees Introduce Reconciliation Bills Funding ICE and ...](https://www.fairus.org/legislation/congress/senate-committees-introduce-reconciliation-bills-funding-ice-and-border-patrol). Senate committees are scheduled to mark up their respective portions of the bill during the week of May 19, 2026, after which the sections will be combined into a single legislative package for a full Senate floor vote [Senate Republicans Release $72 Billion Reconciliation Bill Funding ...](https://nlihc.org/resource/senate-republicans-release-72-billion-reconciliation-bill-funding-ice-cbp-and-white-house). Congressional Republicans and President Trump have stated an aim to enact the final bill by June 1, 2026 [Senate Republicans Release $72 Billion Reconciliation Bill Funding ...](https://nlihc.org/resource/senate-republicans-release-72-billion-reconciliation-bill-funding-ice-cbp-and-white-house)[Senate Committees Introduce Reconciliation Bills Funding ICE and ...](https://www.fairus.org/legislation/congress/senate-committees-introduce-reconciliation-bills-funding-ice-and-border-patrol).

Because reconciliation allows passage with a simple majority (51 votes), the GOP can afford to lose only a small number of senators. With a 53-47 Republican majority, up to 3 Republican defections can be absorbed (with the Vice President breaking a tie). Murkowski's vote against the budget resolution signals skepticism, but she could still support the final bill depending on amendments adopted during floor debate and vote-a-rama. Her vote is therefore genuinely uncertain and potentially decisive.

**Exact later resolution packet**

The question resolves NO (0).

Chain of reasoning against every criterion:

1. The reconciliation bill originating from S.Con.Res.33 (119th Congress) is S.2, the "Secure America Act." Congress.gov confirms S.2 was reconciliation legislation submitted pursuant to the directives in S.Con.Res.33 (its measure title on the Senate vote page is "An original bill to provide for reconciliation pursuant to title II of S. Con. Res. 33") [972d82, 96a7c4].

2. The final Senate passage vote (the vote on passage of the bill as a whole, not cloture/amendments) was Senate Roll Call Vote #163 of the 119th Congress, 2nd Session. The Senate passed S.2 by a Yea-Nay vote of 52–47 [96a7c4, 972d82].

3. The vote occurred on June 5, 2026, which is on or after May 12, 2026, and on or before July 1, 2026 — squarely within the resolution window [96a7c4, 972d82].

4. Senator Lisa Murkowski (R-AK) is explicitly listed in the official Senate roll call record as having cast a "Nay" vote. E&E News independently reported that Murkowski was the only Republican to vote against the bill [96a7c4, 45c18c].

Since Murkowski cast a "Nay" (not a "Yea") vote on final passage, the question resolves NO.

Official resolution source (Senate roll call): https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00163.htm
Cross-reference (congress.gov): https://www.congress.gov/bill/119th-congress/senate-bill/2

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-211. `5d8210d4-de1a-5806-911f-e7b11179c8df`

- Present date: `2026-05-15 16:43:58.638209`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will a Zimbabwean court issue an order blocking or suspending proceedings on the Constitution of Zimbabwe Amendment (No. 3) Bill between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves **YES** if, on or after 12 May 2026 (00:00 CAT, UTC+2) and before 1 July 2026 (23:59 CAT, UTC+2), any of the following Zimbabwean courts issues a formal order — including an [injunction](https://www.law.cornell.edu/wex/injunction), [interdict](https://en.wikipedia.org/wiki/Interdict_(law)), or any order that blocks, suspends, or halts proceedings — directed at the Constitution of Zimbabwe Amendment (No. 3) Bill:

- The **Constitutional Court of Zimbabwe** (https://en.wikipedia.org/wiki/Constitutional_Court_of_Zimbabwe)
- The **Supreme Court of Zimbabwe** (https://en.wikipedia.org/wiki/Supreme_Court_of_Zimbabwe)
- The **High Court of Zimbabwe** (https://en.wikipedia.org/wiki/High_Court_of_Zimbabwe)

For purposes of this question:
- An **injunction** or **interdict** is a court order requiring a party to do or refrain from doing a specific act — here, specifically an order that prevents Parliament, a parliamentary committee, or any government body from continuing legislative proceedings (debate, committee review, voting, or assent) on the bill. See [Cornell Law Institute definition](https://www.law.cornell.edu/wex/injunction) and [Wikipedia: Interdict (law)](https://en.wikipedia.org/wiki/Interdict_(law)).
- "Blocking or suspending proceedings" means any court order that explicitly stops, delays, or suspends any stage of the legislative process for the bill, whether temporarily (interim/provisional) or permanently.
- If a court issues such an order and it is subsequently stayed or overturned within the resolution window, the question still resolves **YES**, provided the original order was issued within the specified timeframe.

This question resolves **NO** if no such order is issued by any of the above courts before 1 July 2026 (23:59 CAT).

**Resolution sources:** Official records from the Zimbabwe Judicial Service Commission (https://www.jsc.org.zw/) or credible reporting from at least one of the following outlets: [ZimLive](https://www.zimlive.com/), [NewsDay Zimbabwe](https://www.newsday.co.zw/), [NewZimbabwe.com](https://www.newzimbabwe.com/), [Reuters](https://www.reuters.com/), or [Al Jazeera](https://www.aljazeera.com/).

**Pre-cutoff background**

The Constitution of Zimbabwe Amendment (No. 3) Bill (CAB3) was approved by Cabinet on 10 February 2026 and gazetted on 16 February 2026. It proposes sweeping changes to Zimbabwe's 2013 Constitution, including replacing direct presidential elections with election by a joint sitting of Parliament, extending presidential and parliamentary terms from five to seven years, and consolidating executive control over state institutions [Constitution of Zimbabwe Amendment (No. 3) Bill - Wikipedia](https://en.wikipedia.org/wiki/Constitution_of_Zimbabwe_Amendment_(No._3)_Bill).

As of early May 2026, the bill has advanced through public consultations (held 30 March–4 April 2026, with written submissions accepted until 17 May 2026) [Constitution of Zimbabwe Amendment (No. 3) Bill - Wikipedia](https://en.wikipedia.org/wiki/Constitution_of_Zimbabwe_Amendment_(No._3)_Bill). Reports indicate the National Assembly voted overwhelmingly in favour of the bill on 28 April 2026 (131 yes, 2 no out of 156 MPs present). Formal legislative processes including committee review were scheduled to commence on or after 16 May 2026 [The Constitution of Zimbabwe Amendment Bill No.3 | ConstitutionNet](http://constitutionnet.org/news/voices/executive-consolidation-constitutional-disruption-constitution-zimbabwe).

Multiple legal challenges have been filed. Three litigants filed Constitutional Court applications challenging the ZANU-PF resolutions, the cabinet resolution, and provisions regarding incumbent preservation [The Constitution of Zimbabwe Amendment Bill No.3 | ConstitutionNet](http://constitutionnet.org/news/voices/executive-consolidation-constitutional-disruption-constitution-zimbabwe). Activists represented by Lovemore Madhuku have questioned the validity of the Cabinet's approval process, and former MP Prince Dubeko Sibanda challenged specific clauses as inconsistent with section 328 of the Constitution [Constitution of Zimbabwe Amendment (No. 3) Bill - Wikipedia](https://en.wikipedia.org/wiki/Constitution_of_Zimbabwe_Amendment_(No._3)_Bill). A Constitutional Court hearing on these challenges is reportedly scheduled for 20 May 2026. As of the most recent available information, no court has yet issued an injunction or interdict blocking or suspending the bill's proceedings [Constitution of Zimbabwe Amendment (No. 3) Bill - Wikipedia](https://en.wikipedia.org/wiki/Constitution_of_Zimbabwe_Amendment_(No._3)_Bill).

Zimbabwe's judiciary has historically been deferential to ZANU-PF, creating significant uncertainty about whether legal challenges will result in any court order halting the bill.

**Exact later resolution packet**

The question resolves NO. No Zimbabwean court (Constitutional Court, Supreme Court, or High Court) issued a formal order blocking, suspending, or halting proceedings on the Constitution of Zimbabwe Amendment (No. 3) Bill (CAB3) between 12 May 2026 (00:00 CAT) and 1 July 2026 (23:59 CAT). To the contrary, the courts DISMISSED the challenges and the legislative process proceeded unimpeded.

Key evidence (all from approved outlets or their reporting):

1. Constitutional Court challenges (war veterans, represented by Lovemore Madhuku, and former MP Prince Dubeko Sibanda): The Constitutional Court heard these in the week of 18 May 2026 and, in mid-June 2026 (17 June 2026), struck off / dismissed both challenges WITHOUT deciding the merits. Justice Bharat Patel ruled the war veterans' application did not meet requirements for direct Constitutional Court intervention and that Sibanda's application was brought prematurely, indicating the matters should first go to the High Court. No injunction or interdict was issued [25d3dd][27e51d][4df1ce][790627]. Reported by NewsDay Zimbabwe ("ConCourt dismisses challenges to Constitutional Amendment Bill No 3") and Zimbabwe Situation.

2. Youngerson Matete (Project Vote 263 founder) filed a High Court application on 26 May 2026 seeking a declaratory order/interdict requiring a national referendum before certain clauses could be enacted. This did NOT result in any court order blocking or suspending the bill's legislative proceedings; the legislative process continued [7aadf0][ca5699]. Reported by ZimLive and NewZimbabwe.com.

3. The Bill continued through Parliament without any court-ordered halt: it passed the National Assembly on 18 June 2026 (216 votes to 42) and the Senate on 24 June 2026 (75 to 4), and awaited presidential assent as of 30 June 2026 — confirming no order halted proceedings [25d3dd][27e51d]. Corroborated by Al Jazeera reporting on the National Assembly passage (aljazeera.com/news/2026/6/19).

Since the antecedent event required for YES (a court order that blocks/suspends/halts proceedings) never occurred at any point in the window, and no order was even issued and later overturned, the question resolves NO (0).

Evidence URLs:
- https://en.wikipedia.org/wiki/Constitution_of_Zimbabwe_Amendment_(No._3)_Bill
- https://www.pindula.co.zw/CAB3
- https://www.zimbabwesituation.com/news/concourt-dismisses-challenges-to-constitutional-amendment-bill-no-3/
- https://www.newsday.co.zw/local-news/article/200057114/concourt-dismisses-challenges-to-constitutional-amendment-bill-no-3
- https://pindula.co.zw/Youngerson_Matete
- https://www.zimlive.com/rights-activist-goes-to-court-to-force-referendum-on-constitutional-amendment-bill/
- https://www.newzimbabwe.com/activist-seeks-to-block-constitution-amendment-bill-no-3-changes-without-referendum/
- https://www.aljazeera.com/news/2026/6/19/zimbabwe-bill-to-scrap-presidential-elections-sparks-backlash

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-212. `31dea349-4c10-5502-87fe-ff8f42d34507`

- Present date: `2026-05-02 17:54:45.163029`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the SAF lose control of any state capital it held as of May 1, 2026, to the RSF before June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026 (00:00 UTC) and before June 1, 2026 (23:59 UTC), the RSF establishes control over any state capital that was under SAF control as of May 1, 2026 (00:00 UTC). It resolves **No** otherwise.

**Definitions:**

- **"State capital"**: The administrative center of any of Sudan's 18 states as listed at https://en.wikipedia.org/wiki/States_of_Sudan [https://en.wikipedia.org/wiki/States_of_Sudan](https://en.wikipedia.org/wiki/States_of_Sudan). The 13 SAF-held capitals forming the baseline for this question are: Khartoum, Wad Madani, Port Sudan, Kassala, El-Gadarif, El-Obeid, Ad-Damir, Dongola, Singa, Rabak, Ad-Damazin, Kadugli, and Al-Fashir.

- **"Losing control"**: The SAF is deemed to have lost control of a state capital if any of the following occur:
  (a) The RSF occupies the state government headquarters or governor's office and maintains a presence for at least 24 hours; OR
  (b) The SAF publicly announces or is credibly reported to have withdrawn its forces from the city; OR
  (c) At least two major independent international news organizations (from among Reuters, Associated Press, Agence France-Presse, BBC, or Al Jazeera) report that the RSF has captured or taken control of the city.

- Events must occur on or after May 1, 2026 (00:00 UTC) and before June 1, 2026 (23:59 UTC). Any state capital that was already under RSF control before May 1, 2026 does not count.

**Resolution sources:**
- Major international wire services: [Reuters](https://www.reuters.com/places/sudan), [AP News](https://apnews.com/hub/sudan), [Al Jazeera](https://www.aljazeera.com/where/sudan/)
- Conflict monitoring: [ACLED](https://acleddata.com/), [Sudan War Monitor](https://sudanwarmonitor.com/)
- UN situation reports: [ReliefWeb Sudan page](https://reliefweb.int/country/sdn)

**Pre-cutoff background**

The Sudanese civil war, which began in April 2023, has by early 2026 settled into what Al Jazeera describes as a "military impasse," with front lines largely hardened into a de facto partition [https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse](https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse). The Sudanese Armed Forces (SAF) control the northern, central, and eastern states, while the Rapid Support Forces (RSF) control the Darfur region and large parts of the Kordofan states [https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse](https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse).

As of April 27, 2026, the following state capitals are assessed to be under SAF control [Territorial control map - Sudan Conflict (as of April 27, 2026)](https://www.sudanspost.com/territorial-control-map-sudan-conflict-as-of-april-27-2026/) [https://en.wikipedia.org/wiki/States_of_Sudan](https://en.wikipedia.org/wiki/States_of_Sudan):

1. **Khartoum** (Khartoum State) — SAF retook Khartoum in March 2025; government returned January 2026 [Timeline of the Sudanese civil war (2026) - Wikipedia](https://en.wikipedia.org/wiki/Timeline_of_the_Sudanese_civil_war_(2026))
2. **Wad Madani** (Gezira State) — SAF controls Al-Jazirah corridor [Territorial control map - Sudan Conflict (as of April 27, 2026)](https://www.sudanspost.com/territorial-control-map-sudan-conflict-as-of-april-27-2026/)
3. **Port Sudan** (Red Sea State) — SAF stronghold and former interim capital [Territorial control map - Sudan Conflict (as of April 27, 2026)](https://www.sudanspost.com/territorial-control-map-sudan-conflict-as-of-april-27-2026/)
4. **Kassala** (Kassala State) — SAF-controlled east [Territorial control map - Sudan Conflict (as of April 27, 2026)](https://www.sudanspost.com/territorial-control-map-sudan-conflict-as-of-april-27-2026/)
5. **El-Gadarif** (Al-Qadarif State) — SAF-controlled east [Territorial control map - Sudan Conflict (as of April 27, 2026)](https://www.sudanspost.com/territorial-control-map-sudan-conflict-as-of-april-27-2026/)
6. **El-Obeid** (North Kordofan State) — under SAF control but subject to frequent RSF drone strikes [Timeline of the Sudanese civil war (2026) - Wikipedia](https://en.wikipedia.org/wiki/Timeline_of_the_Sudanese_civil_war_(2026)) [Territorial control map - Sudan Conflict (as of April 27, 2026)](https://www.sudanspost.com/territorial-control-map-sudan-conflict-as-of-april-27-2026/)
7. **Ad-Damir** (River Nile State) — SAF-controlled north [Territorial control map - Sudan Conflict (as of April 27, 2026)](https://www.sudanspost.com/territorial-control-map-sudan-conflict-as-of-april-27-2026/)
8. **Dongola** (Northern State) — SAF-controlled north [Territorial control map - Sudan Conflict (as of April 27, 2026)](https://www.sudanspost.com/territorial-control-map-sudan-conflict-as-of-april-27-2026/)
9. **Singa** (Sennar State) — SAF-controlled central/east
10. **Rabak** (White Nile State) — SAF-controlled central
11. **Ad-Damazin** (Blue Nile State) — SAF control, though Kurmuk locality saw RSF/SPLM-N activity [Timeline of the Sudanese civil war (2026) - Wikipedia](https://en.wikipedia.org/wiki/Timeline_of_the_Sudanese_civil_war_(2026)) [Territorial control map - Sudan Conflict (as of April 27, 2026)](https://www.sudanspost.com/territorial-control-map-sudan-conflict-as-of-april-27-2026/)
12. **Kadugli** (South Kordofan State) — SAF broke RSF siege in February 2026; control is fragmented in surrounding areas [Timeline of the Sudanese civil war (2026) - Wikipedia](https://en.wikipedia.org/wiki/Timeline_of_the_Sudanese_civil_war_(2026)) [Territorial control map - Sudan Conflict (as of April 27, 2026)](https://www.sudanspost.com/territorial-control-map-sudan-conflict-as-of-april-27-2026/)
13. **Al-Fashir** (North Darfur State) — contested/besieged but SAF-aligned forces maintain presence [Timeline of the Sudanese civil war (2026) - Wikipedia](https://en.wikipedia.org/wiki/Timeline_of_the_Sudanese_civil_war_(2026))

The following state capitals are assessed to be under RSF control:
- **Nyala** (South Darfur), **El Geneina** (West Darfur), **Zalingei** (Central Darfur), **Ed Daein** (East Darfur), **Al-Fulah** (West Kordofan) [Territorial control map - Sudan Conflict (as of April 27, 2026)](https://www.sudanspost.com/territorial-control-map-sudan-conflict-as-of-april-27-2026/) [https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse](https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse)

The most vulnerable SAF-held capitals are **El-Obeid**, which faces frequent RSF drone strikes and offensive pressure, **Kadugli**, where the SAF only recently broke an RSF siege, and **Al-Fashir**, which has been under sustained RSF pressure including a massacre reported on March 25, 2026 [Timeline of the Sudanese civil war (2026) - Wikipedia](https://en.wikipedia.org/wiki/Timeline_of_the_Sudanese_civil_war_(2026)). The RSF has increasingly relied on drone warfare and has opened a new front in Blue Nile state [https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse](https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse). The SAF retook Kurmuk on April 20, 2026 after it was captured by RSF/SPLM-N forces on March 24 [Timeline of the Sudanese civil war (2026) - Wikipedia](https://en.wikipedia.org/wiki/Timeline_of_the_Sudanese_civil_war_(2026)), illustrating the fluid nature of control in some areas.

**Exact later resolution packet**

The question resolves NO. It would have resolved YES only if, between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), the RSF established control over one of the 13 SAF-held state capitals (Khartoum, Wad Madani, Port Sudan, Kassala, El-Gadarif, El-Obeid, Ad-Damir, Dongola, Singa, Rabak, Ad-Damazin, Kadugli, Al-Fashir).

Evidence reviewed:

1. The Wikipedia "Timeline of the Sudanese civil war (2026)" documents fighting in May 2026 only in smaller towns and rural areas (e.g., Dukan, Keren Keren, Mogja, Al-Barka, villages in Qaysan and North Kordofan); none of the 13 listed state capitals were captured by the RSF in May 2026 [008652].

2. The most "at-risk" capital, El-Obeid (North Kordofan), was confirmed to remain under SAF control as of May 8, 2026 by a Sudan Protection Cluster note: "El Obeid remains under SAF control but is increasingly isolated by insecurity and RSF presence along key routes" [3dca30]. The SAF had previously retaken Bara and secured El-Obeid in March 2026.

3. Kadugli (South Kordofan): the SAF broke the RSF siege in early February 2026 and the city remained under SAF control, with commercial convoys entering in May 2026; no RSF capture occurred.

4. The Operation Broken Silence Sudan Crisis Guide (updated May 1, 2026) describes a hardened de facto partition and reports no new RSF capture of any SAF-held state capital during May 2026 [9534ab].

The only major state capital to fall to the RSF, Al-Fasher (North Darfur), was captured in late October 2025 — long before the May 2026 window — and so does not count.

No SAF withdrawal announcement (criterion b), RSF occupation of a governor's office for 24+ hours (criterion a), or reporting by two of Reuters/AP/AFP/BBC/Al Jazeera of an RSF capture (criterion c) occurred for any of the 13 baseline capitals during the resolution window. Therefore the question resolves NO.

Sources:
- https://en.wikipedia.org/wiki/Timeline_of_the_Sudanese_civil_war_(2026)
- https://reliefweb.int/report/sudan/sudan-protection-cluster-note-el-obeid-north-kordofan-8-may-2026
- https://operationbrokensilence.org/blog/sudan-crisis-guide
- https://www.aljazeera.com/news/2026/3/6/sudanese-army-retakes-bara-secures-el-obeid-in-north-kordofan

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-213. `d74cdd96-f90e-5874-b5f8-14c911acc01d`

- Present date: `2026-05-03 12:46:55.709527`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the United States and Iran announce a formal, permanent ceasefire agreement between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after April 30, 2026 (00:00 UTC) and no later than June 1, 2026 (23:59 UTC), the United States and the Islamic Republic of Iran publicly announce a formal ceasefire agreement intended to permanently or indefinitely end hostilities in the 2026 Iran war.

A "formal ceasefire agreement" is defined as meeting ALL of the following criteria:
1. It must be a mutual, bilateral commitment by both the US and Iranian governments to cease military hostilities against each other.
2. It must be explicitly described as permanent, indefinite, or intended to lead to a lasting end of hostilities — not merely a temporary truce, short-term extension, or humanitarian pause.
3. It must be announced via official channels of both governments (e.g., a White House statement at whitehouse.gov, a US State Department announcement at state.gov, and a corresponding official Iranian government statement from the Office of the Supreme Leader, the President, or the Ministry of Foreign Affairs). A joint statement, signed document, or simultaneous official press releases from both sides all qualify.

Resolution will be determined by confirming such announcements on official government websites (whitehouse.gov, state.gov, or their Iranian counterparts) or, if those are inaccessible, by corroborating reports from at least two of the following credible news organizations: Reuters (reuters.com), Associated Press (apnews.com), BBC (bbc.com), or The New York Times (nytimes.com).

If no such agreement meeting all three criteria above is publicly announced by 23:59 UTC on June 1, 2026, this question resolves NO.

**Pre-cutoff background**

On February 28, 2026, the United States and Israel launched coordinated military strikes on Iran, triggering retaliatory Iranian missile and drone attacks across the Middle East and initiating the 2026 Iran war [https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire). After weeks of escalating conflict, Pakistan mediated a temporary two-week ceasefire agreed on April 8, 2026. However, peace talks held in Islamabad collapsed by April 12, and the US imposed a naval blockade on Iran [https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire).

As of April 30, 2026, no permanent ceasefire agreement exists. The temporary ceasefire has been repeatedly violated by both sides [https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire). On April 21, 2026, President Trump announced a short-term extension of the truce to allow Iran to submit a proposal for ending the conflict permanently, but US officials indicated this extension was limited to only a few days [https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire). Negotiations have involved multiple mediators including Pakistan, Egypt, Turkey, and Russia, with Vice President J.D. Vance, White House envoy Steve Witkoff, and senior adviser Jared Kushner leading the US side [U.S. and Iran inch toward framework deal to end war, U.S. officials say](https://www.axios.com/2026/04/15/iran-war-negotiations-deal-pakistan). As of late April, Iran's Foreign Minister was in Russia discussing a possible new round of negotiations with the US. US officials have reported progress toward a framework deal but cautioned that "substantial differences" remain between the two sides [U.S. and Iran inch toward framework deal to end war, U.S. officials say](https://www.axios.com/2026/04/15/iran-war-negotiations-deal-pakistan). The US naval blockade remains in effect, and the overall situation is characterized by fragile, temporary truces rather than any lasting agreement.

**Exact later resolution packet**

The question requires that between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), the US and Iran publicly announce a formal ceasefire agreement explicitly described as permanent, indefinite, or intended to permanently end hostilities, announced via official channels of BOTH governments.

Evidence gathered shows this did NOT occur:

1. Throughout May 2026, the only agreements under discussion were TEMPORARY truce extensions, not permanent ceasefires. Multiple credible outlets (Reuters, Al Jazeera, CNN, PBS) reported on May 28, 2026 that US and Iranian negotiators reached a "tentative" memorandum of understanding to extend the truce for only 60 days, reopen the Strait of Hormuz, and START nuclear talks — explicitly a short-term extension and a framework for future negotiations, not a permanent end to hostilities. (Reuters: reuters.com/world/middle-east/iran-us-trade-air-strikes-after-trump-dismisses-report-hormuz-deal-2026-05-28/; Al Jazeera: aljazeera.com/news/2026/5/28/us-and-iran-reach-tentative-deal-for-60-day-truce-extension-officials-say)

2. Iran's Foreign Ministry explicitly denied that any deal had been finalized. On May 29, 2026, Iranian Foreign Ministry spokesman Esmail Baghaei stated that an agreement with the US "has not been finalised yet," directly contradicting any claim of a concluded bilateral permanent ceasefire [Iran denies ceasefire deal with US is “finalised” - Al Jazeera](https://www.aljazeera.com/video/newsfeed/2026/5/29/iran-denies-ceasefire-deal-with-us-is). (aljazeera.com/video/newsfeed/2026/5/29/iran-denies-ceasefire-deal-with-us-is)

3. The conflict remained active during the window. On May 28, 2026, the US accused Iran of an "egregious ceasefire violation," and there were reports of US-Iran air strikes — indicating hostilities were ongoing, not permanently ended (politico.com/news/2026/05/28/us-iran-ceasefire-violation-00940825).

4. As of June 1, 2026 (the close of the window), the ceasefire deal was reported as still "in doubt" (Bloomberg/YouTube "Ceasefire Deal in Doubt as Israel Steps up Lebanon Offensive 06/01/2026"), and discussions were only at a "Declaration of Principles" stage (aljazeera.com/video/the-bottom-line/2026/5/31/what-are-the-chances-for-the-iran-us-declaration-of). The Wikipedia article on the 2026 Iran war ceasefire confirms no formal, permanent, or indefinite ceasefire agreement was announced by both governments during the April 30–June 1 window; truces were temporary and repeatedly violated [2026 Iran war ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire).

Because (a) the only agreements were explicitly temporary (60-day) extensions or frameworks, (b) Iran publicly denied any deal was even finalized, and (c) no joint or simultaneous official announcement of a PERMANENT/indefinite bilateral ceasefire was made by both governments before 23:59 UTC June 1, 2026, the question's criteria are not met. Resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-214. `e6d19ad4-8431-5b8c-9f13-85c4cb45fd6a`

- Present date: `2026-04-30 13:46:29.998956`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the RSF capture or establish control over El-Obeid (North Kordofan) by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 29, 2026 and on or before June 1, 2026 (23:59 UTC), the [Rapid Support Forces (RSF)](https://en.wikipedia.org/wiki/Rapid_Support_Forces) capture or establish control over [El-Obeid](https://en.wikipedia.org/wiki/El-Obeid), the capital of North Kordofan state, Sudan.

"Capture" or "control" is established if **any one** of the following conditions is met, as reported by credible sources:
1. The RSF occupies the [5th Infantry Division](https://en.wikipedia.org/wiki/Sudanese_Armed_Forces) headquarters or the North Kordofan state government buildings in El-Obeid;
2. The SAF publicly acknowledges withdrawal from or loss of El-Obeid;
3. The RSF publicly claims control of El-Obeid **and** this claim is corroborated by at least one major international news agency (e.g., Reuters, AP, Al Jazeera, BBC); or
4. Conflict monitoring organizations report that the RSF has displaced SAF forces from El-Obeid city center and maintains a sustained presence there.

If El-Obeid remains under SAF control or contested without a clear shift to RSF control by June 1, 2026 (23:59 UTC), the question resolves **No**.

**Resolution sources:** [Sudan War Monitor](https://sudanwarmonitor.com/), [ACLED](https://acleddata.com/), or major international news agencies such as [Reuters](https://www.reuters.com/), [Al Jazeera](https://www.aljazeera.com/), [AP News](https://apnews.com/), or [BBC](https://www.bbc.com/news).

**Pre-cutoff background**

El-Obeid is the capital of [North Kordofan](https://en.wikipedia.org/wiki/North_Kordofan) state in Sudan and has been a key strategic objective in the Sudanese civil war. The [Rapid Support Forces (RSF)](https://en.wikipedia.org/wiki/Rapid_Support_Forces) previously besieged the city, but the Sudanese Armed Forces (SAF) broke the siege in February 2025 [https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse](https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse). As of April 2026, the SAF maintains control of El-Obeid, while the RSF controls large parts of the three Kordofan states and holds positions in scattered areas of North Kordofan including Umm Qarfah, Jabra al-Sheikh, Umm Badr, Hamra al-Sheikh, and Sodari [https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse](https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse). The RSF has continued drone strikes on the city throughout 2026, with strikes recorded on January 3, January 5, January 30, February 28, March 2, and April 25 [https://en.wikipedia.org/wiki/Timeline_of_the_Sudanese_civil_war_(2026)](https://en.wikipedia.org/wiki/Timeline_of_the_Sudanese_civil_war_(2026)). The SAF launched a major ground operation in Kordofan on April 18, 2026, and recaptured the nearby city of Bara in March 2026 [https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse](https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse). The overall military situation is described as an impasse [https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse](https://www.aljazeera.com/news/2026/4/16/after-three-years-of-war-sudan-army-and-rsf-locked-in-military-impasse).

**Exact later resolution packet**

The question resolves NO. The RSF did not capture or establish control over El-Obeid between April 29, 2026 and June 1, 2026 (23:59 UTC).

Key evidence:
- The Sudan Protection Cluster Note for El Obeid, North Kordofan, dated 8 May 2026 (within the resolution window), explicitly states: "El Obeid remains under SAF control but is increasingly isolated by insecurity and RSF presence along key routes." [4d240f] (https://reliefweb.int/report/sudan/sudan-protection-cluster-note-el-obeid-north-kordofan-8-may-2026)
- The Wikipedia "Timeline of the Sudanese civil war (2026)" records only a single El-Obeid-related event in the relevant May window: an RSF drone strike on Jabal Awliya, El Obeid, and Rahad al-Nuba on 1 May 2026. There is NO record of the RSF occupying the 5th Infantry Division headquarters or the North Kordofan state government buildings, no SAF acknowledgment of withdrawal/loss, no RSF claim of control corroborated by major agencies, and no conflict-monitoring report of the RSF displacing SAF from the city center and maintaining a sustained presence. [08a5d4] (https://en.wikipedia.org/wiki/Timeline_of_the_Sudanese_civil_war_(2026))

None of the four "Yes" conditions in the resolution criteria were met. The RSF activity during the window was limited to drone strikes and pressure on supply routes, while the city itself stayed under SAF control. Per the resolution criteria, "If El-Obeid remains under SAF control or contested without a clear shift to RSF control by June 1, 2026 (23:59 UTC), the question resolves No."

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-215. `de8ce771-471b-5e65-a649-119e38a72546`

- Present date: `2026-05-03 03:24:43.752541`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will ADRAS-J's orbital perigee drop below 250 km by June 1, 2026?

**Resolution criteria**

This question resolves YES if, at any time on or after May 1, 2026 00:00 UTC and before June 1, 2026 00:00 UTC, the perigee altitude of ADRAS-J (NORAD catalog number 58992) drops below 250 km, as recorded in Two-Line Element (TLE) data published by the U.S. Space Force via Space-Track.org (https://www.space-track.org/).

Specifically, the resolution source is the GP (General Perturbations) orbital element sets for catalog number 58992 available at Space-Track.org. If any TLE epoch within the resolution window shows a perigee altitude below 250 km, the question resolves YES.

If ADRAS-J undergoes full atmospheric reentry (defined as removal from the active satellite catalog and addition to the SATCAT decay list at https://www.space-track.org/basicspacedata/query/class/decay/) during the resolution window, this also resolves YES, as reentry necessarily implies the perigee dropped well below 250 km.

If neither condition is met by June 1, 2026 00:00 UTC, the question resolves NO.

All times are in UTC.

**Pre-cutoff background**

ADRAS-J (Active Debris Removal by Astroscale-Japan, NORAD ID 58992) is a commercial debris inspection satellite launched on February 18, 2024, by Astroscale. After completing its primary mission of inspecting a defunct Japanese H-2A upper stage rocket body, Astroscale announced on March 25, 2026, that ADRAS-J had begun controlled deorbit operations [Astroscale's ADRAS-J Mission Completes Operations, Begins Deorbit](https://www.astroscale.com/news/astroscales-adras-j-mission-completes-operations-begins-deorbit). The company stated the satellite had "lowered its orbital altitude to a level that allows for natural orbital decay and atmospheric re-entry within five years" [Astroscale's ADRAS-J Mission Completes Operations, Begins Deorbit](https://www.astroscale.com/news/astroscales-adras-j-mission-completes-operations-begins-deorbit), with additional orbit-lowering maneuvers planned until eventual reentry [Astroscale's ADRAS-J Mission Completes Operations, Begins Deorbit](https://www.astroscale.com/news/astroscales-adras-j-mission-completes-operations-begins-deorbit).

As of May 1, 2026, ADRAS-J remains in orbit with a perigee of approximately 332 km and an apogee of approximately 576 km [ADRAS-J Satellite details 2024-034A NORAD 58992 - N2YO.com](https://www.n2yo.com/satellite/?s=58992). At these altitudes, natural atmospheric drag is minimal and full atmospheric reentry would likely take years without further propulsive maneuvers. However, Astroscale has indicated it will continue active orbit-lowering operations [Astroscale's ADRAS-J Mission Completes Operations, Begins Deorbit](https://www.astroscale.com/news/astroscales-adras-j-mission-completes-operations-begins-deorbit), which could accelerate the descent significantly. Whether the perigee drops below 250 km by June 1, 2026, depends on the pace and extent of any remaining propulsive maneuvers and on atmospheric drag conditions (which vary with solar activity).

Orbital data for ADRAS-J (NORAD catalog number 58992) is publicly available via Space-Track.org and tracking sites such as N2YO.com (https://www.n2yo.com/satellite/?s=58992).

**Exact later resolution packet**

The question resolves YES only if ADRAS-J's (NORAD 58992) perigee altitude dropped below 250 km between May 1, 2026 00:00 UTC and June 1, 2026 00:00 UTC (per Space-Track GP/TLE data), or if it fully reentered/decayed during that window.

Evidence shows neither occurred:
- As of the question's stated baseline (May 1, 2026), the perigee was ~332 km.
- Satcat (which republishes Space-Track/US Space Force TLE data) shows the latest TLE epoch 2026-06-02 with a perigee altitude of ~317.5 km, with the satellite still in the active catalog (not decayed) [bae439].
- N2YO (also based on Space-Track TLEs) shows a current perigee of ~327.6 km with a TLE epoch of June 2, 2026 (epoch 26153), still in orbit [e55c67].

The perigee declined only gradually from ~332 km (May 1) to ~317–327 km (early June), remaining far above the 250 km threshold for the entire resolution window. The satellite did not decay/reenter and was not removed from the active catalog during the window. Therefore the perigee never dropped below 250 km before June 1, 2026 00:00 UTC, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-216. `94da7c39-86dc-57b2-a5dd-96272889dfb3`

- Present date: `2026-05-01 17:11:36.411849`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a cyclonic storm or severe cyclonic storm make landfall on the Odisha coast between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the India Meteorological Department (IMD) officially reports that a system classified as a **Cyclonic Storm** (maximum sustained wind speed ≥34 knots / 62 km/h) or any higher-intensity classification makes **landfall** on the **Odisha coast** on or after April 30, 2026 (00:00 UTC) and before June 2, 2026 (00:00 UTC).

**Key definitions:**

1. **Cyclonic Storm or higher:** A tropical cyclone with maximum sustained surface wind speed (3-minute average) of at least 34 knots (62 km/h) per the IMD classification system (https://rsmcnewdelhi.imd.gov.in/images/pdf/terminology.pdf) [[PDF] Terminology on Cyclonic disturbances over the North Indian Ocean ...](https://rsmcnewdelhi.imd.gov.in/images/pdf/terminology.pdf). This includes Cyclonic Storm, Severe Cyclonic Storm (≥48 knots / 89 km/h), Very Severe Cyclonic Storm, Extremely Severe Cyclonic Storm, and Super Cyclonic Storm.

2. **Landfall:** The center of the cyclonic storm's circulation crosses the coastline, as determined and reported by the IMD in its official bulletins or post-season reports.

3. **Odisha coast:** The coastline of the Indian state of Odisha (also spelled Orissa), extending from the Andhra Pradesh–Odisha border near Bahuda River mouth (approximately 18.3°N, 84.1°E) in the south to the Odisha–West Bengal border near Subarnarekha River mouth (approximately 21.6°N, 87.4°E) in the north, along the western Bay of Bengal.

4. **All times are in UTC.**

**Resolution source:** Official IMD cyclone bulletins, preliminary cyclone reports, and/or the RSMC New Delhi Best Track archive, accessible at:
- https://mausam.imd.gov.in/responsive/cycloneinformation.php [Cyclone Information - IMD - India Meteorological Department](https://mausam.imd.gov.in/responsive/cycloneinformation.php)
- https://mausam.imd.gov.in/responsive/cyclone_bulletin_archive.php?id=1 [All India Cyclone Bulletin - IMD - India Meteorological Department](https://mausam.imd.gov.in/responsive/cyclone_bulletin_archive.php?id=1)
- https://rsmcnewdelhi.imd.gov.in/report.php?internal_menu=MjY [Cyclone Information - IMD - India Meteorological Department](https://mausam.imd.gov.in/responsive/cycloneinformation.php)

If no such landfall is reported by IMD by the resolution date, the question resolves **No**.

**Pre-cutoff background**

May is historically a peak month for tropical cyclone activity in the Bay of Bengal, with several significant storms impacting the Odisha coast in recent years, including Cyclone Fani (2019), Cyclone Amphan (2020), and Cyclone Yaas (2021). However, cyclones do not strike Odisha every May, making the base rate for such an event roughly 15–30% in any given year.

According to the India Meteorological Department (IMD), tropical cyclones in the North Indian Ocean are classified by maximum sustained surface wind speed (3-minute average) as follows [[PDF] Terminology on Cyclonic disturbances over the North Indian Ocean ...](https://rsmcnewdelhi.imd.gov.in/images/pdf/terminology.pdf):
- **Cyclonic Storm:** 34–47 knots (62–88 km/h)
- **Severe Cyclonic Storm:** 48–63 knots (89–117 km/h)
- **Very Severe Cyclonic Storm:** 64–89 knots (118–166 km/h)
- **Extremely Severe Cyclonic Storm:** 90–119 knots (167–221 km/h)
- **Super Cyclonic Storm:** ≥120 knots (≥222 km/h)

As of April 30, 2026, the IMD has been issuing regular Tropical Weather Outlooks but no cyclone warning is active for the Bay of Bengal or the Odisha coast [Cyclone Information - IMD - India Meteorological Department](https://mausam.imd.gov.in/responsive/cycloneinformation.php). The latest bulletin in the IMD cyclone archive is dated April 30, 2026 [All India Cyclone Bulletin - IMD - India Meteorological Department](https://mausam.imd.gov.in/responsive/cyclone_bulletin_archive.php?id=1). Sea surface temperatures in the Bay of Bengal are typically warm (28–30°C) during the pre-monsoon season, which is conducive to cyclogenesis, but formation depends on additional dynamic factors such as wind shear and the Madden-Julian Oscillation.

**Exact later resolution packet**

The question resolves NO. No system classified by the IMD as a Cyclonic Storm (≥34 knots) or higher made landfall on the Odisha coast between April 30, 2026 (00:00 UTC) and June 2, 2026 (00:00 UTC).

Evidence:
- The Wikipedia "2026 North Indian Ocean cyclone season" article (last updated late May 2026) lists only ONE system for the entire 2026 season to date: "Deep Depression BOB 01," which occurred in January 2026 and made landfall over Sri Lanka — not a named cyclonic storm and not on Odisha. No cyclonic storm or higher system is listed for the April 30–June 1, 2026 window [456067, cdf219].
- IMD explicitly ruled out a cyclone for Odisha. A May 11, 2026 report quotes IMD meteorologist Dr. Rajshree saying there was "no possibility of any major cyclone in the state." A low-pressure area formed in the southwest Bay of Bengal off Sri Lanka, expected to become a depression, bringing only rain/wind to Odisha — not a cyclonic storm landfall [54468d].
- During late May 2026, the only relevant system was a Depression over the southwest Bay of Bengal off the northeast Sri Lanka coast (per IMD social media), far from Odisha and only of depression intensity (below the 34-knot Cyclonic Storm threshold).
- News coverage throughout May 2026 (ETV Bharat, AP7AM, Tripura Times) repeatedly reported IMD statements that systems would either not intensify into a cyclone or would not make landfall on the Odisha–AP coast, with max winds around 50–60 km/h (below the 62 km/h Cyclonic Storm threshold).

No IMD bulletin or report indicates a Cyclonic Storm center crossing the Odisha coastline within the resolution window. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-217. `16606d11-bde5-56dd-b366-5316fc5c040d`

- Present date: `2026-05-02 16:04:09.664892`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a new incident of suspected undersea cable sabotage in the Baltic Sea be reported between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between 00:00 UTC on May 1, 2026 and 23:59 UTC on June 1, 2026, a credible news source reports a new incident of suspected sabotage of an undersea cable in the Baltic Sea. It resolves **No** otherwise.

**Definitions and specifications:**

1. **Baltic Sea**: The body of water as defined by the International Hydrographic Organization (IHO) in *Limits of Oceans and Seas*, Special Publication N° 23 (3rd Edition, 1953), available at https://epic.awi.de/29772/1/IHO1953a.pdf [[PDF] Limits of Oceans and Seas - EPIC](https://epic.awi.de/29772/1/IHO1953a.pdf). This includes the waters bordered by Denmark, Sweden, Finland, Russia, Estonia, Latvia, Lithuania, Poland, and Germany, with western limits at the Little Belt, Great Belt, Guldborg Sound, and the Sound as specified therein.

2. **Undersea cable**: A submarine telecommunications (fiber-optic) cable or submarine power cable laid on or buried beneath the seabed, as described by the International Cable Protection Committee (https://www.iscpc.org/). Gas pipelines are excluded.

3. **Suspected sabotage**: An incident qualifies as "suspected sabotage" if at least one of the following conditions is met:
   - A government official of a Baltic Sea littoral state (Denmark, Sweden, Finland, Estonia, Latvia, Lithuania, Poland, Germany) or Russia publicly states the damage is being investigated as potential intentional or deliberate damage; OR
   - A NATO official or NATO body (e.g., SACEUR, NATO spokesperson) publicly characterizes the incident as suspected deliberate interference; OR
   - A vessel is detained, seized, or formally investigated by authorities in connection with causing damage to the cable (e.g., via anchor-dragging).
   Incidents attributed solely to natural causes (e.g., earthquakes, storms) or confirmed accidental damage (e.g., routine fishing or anchoring with no suspicion of intent) without any official statement suggesting possible deliberate action do not qualify.

4. **Credible news sources**: Reuters (https://www.reuters.com/), Associated Press (https://apnews.com/), BBC News (https://www.bbc.com/news), Bloomberg (https://www.bloomberg.com/), or official government press releases from any Baltic Sea littoral state.

5. **New incident**: The physical damage or disruption to the cable must be first reported as occurring on or after May 1, 2026 (00:00 UTC). Ongoing investigations or legal proceedings related to incidents that occurred before May 1, 2026 do not count.

**Pre-cutoff background**

The Baltic Sea has experienced a series of suspected sabotage incidents targeting undersea cables and pipelines since 2022. Key incidents include:

- **September 2022**: Nord Stream gas pipelines were destroyed by underwater explosions.
- **October 2023**: The Balticconnector gas pipeline and a telecommunications cable between Finland and Estonia were damaged.
- **November 2024**: Two submarine telecommunications cables — the BCS East-West Interlink and C-Lion1 fiber-optic cables — were disrupted [Timeline Of Suspected Underwater Sabotage In Baltic Sea - gCaptain](https://gcaptain.com/timeline-of-suspected-underwater-sabotage-in-baltic-sea/).
- **December 2024**: The Estlink 2 power cable and several telecom cables were damaged; the vessel *Eagle S* was seized by Finnish authorities on suspicion of anchor-dragging sabotage [Timeline Of Suspected Underwater Sabotage In Baltic Sea - gCaptain](https://gcaptain.com/timeline-of-suspected-underwater-sabotage-in-baltic-sea/).
- **January–February 2025**: Fiber-optic cables connecting Latvia–Sweden and Finland–Germany were damaged; the vessel *Vezhen* was investigated [Timeline Of Suspected Underwater Sabotage In Baltic Sea - gCaptain](https://gcaptain.com/timeline-of-suspected-underwater-sabotage-in-baltic-sea/).
- **December 2025**: The *Fitburg* cargo vessel was seized by Finnish special forces after suspected anchor-dragging damage to submarine cables [Timeline Of Suspected Underwater Sabotage In Baltic Sea - gCaptain](https://gcaptain.com/timeline-of-suspected-underwater-sabotage-in-baltic-sea/).

In response, NATO launched the "Baltic Sentry" mission in January 2025 to patrol and deter further incidents. Finland and other Baltic states have stepped up undersea monitoring capabilities. Despite these measures, incidents have continued, raising the question of whether the pattern will persist into mid-2026.

The Baltic Sea, as defined by the International Hydrographic Organization (IHO) in *Limits of Oceans and Seas* (Special Publication N° 23, 3rd Edition, 1953), is bordered by the coasts of Denmark, Sweden, Finland, Russia, Estonia, Latvia, Lithuania, Poland, and Germany, with its western limits defined by lines across the Little Belt, Great Belt, Guldborg Sound, and the Sound [[PDF] Limits of Oceans and Seas - EPIC](https://epic.awi.de/29772/1/IHO1953a.pdf).

**Exact later resolution packet**

Adjudicated: No new suspected sabotage of a Baltic Sea undersea cable was reported in the May 1 - June 1, 2026 window. The most recent qualifying incident in all timelines and approved-source reporting is the Dec 31, 2025 Gulf of Finland cable damage (Fitburg seizure); searches for the window return only pre-window incidents and analysis pieces. An earlier automated YES relied on a 'late-May 2026 cluster' that does not exist: the cited Telcotitans article is actually dated October 12, 2023, and that same pass conceded other 'May 2026' pages were republications of the November 2024 event.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-218. `249e1182-45bc-5643-a336-5de232710cc3`

- Present date: `2026-05-12 16:08:16.371023`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Israel officially announce the termination or suspension of the October 2025 Gaza ceasefire agreement between May 10, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 10, 2026 (00:00 UTC) and on or before July 1, 2026 (23:59 UTC), the Israeli government officially announces the termination or suspension of the October 2025 Gaza ceasefire agreement (the "Comprehensive Plan to End the Gaza Conflict" signed October 9, 2025).

An "official announcement" is defined as a public statement made by any of the following: the Prime Minister of Israel, the Israeli Minister of Defense, the Israeli Security Cabinet, or the official Israel Defense Forces (IDF) spokesperson — through official channels including official government press releases, official social media accounts, or statements delivered at press conferences.

The announcement must explicitly use language indicating that the ceasefire agreement is "terminated," "suspended," "ended," "nullified," "no longer in effect," or equivalent phrasing. Mere reports of escalation, renewed military operations, or ceasefire violations — without an explicit declaration that the agreement itself is terminated or suspended — do not qualify.

**Resolution sources:** Official Israeli government websites (e.g., https://www.gov.il/en), the IDF spokesperson's official channels, or confirmation by at least two of the following major wire services: Reuters (https://www.reuters.com), Associated Press (https://apnews.com), or Agence France-Presse.

If no such official announcement is confirmed by 23:59 UTC on July 1, 2026, this question resolves as **No**.

**Pre-cutoff background**

The "Comprehensive Plan to End the Gaza Conflict" (commonly known as the Gaza peace plan) was signed on October 9, 2025, and came into effect on October 10, 2025 [Gaza peace plan](https://en.wikipedia.org/wiki/Gaza_peace_plan). The agreement includes 20 points mandating an immediate ceasefire, the return of hostages, prisoner exchanges, demilitarization of Gaza, deployment of an International Stabilization Force (ISF), and establishment of a transitional Palestinian administration [Gaza peace plan](https://en.wikipedia.org/wiki/Gaza_peace_plan).

As of May 11, 2026, the ceasefire is described as "fraying" but has not been formally terminated [Israel threatens Gaza war resumption to force disarmament ...](https://www.aljazeera.com/news/2026/5/3/israel-threatens-gaza-war-resumption-to-force-disarmament-as-truce-frays). Negotiations are stalled due to disagreements over Hamas disarmament. Israel demands progress on Hamas's disarmament before moving to the second phase of the plan, while Hamas insists Israel must first fully implement the first phase (hostage/prisoner exchange, humanitarian aid, and withdrawal) [Gaza peace plan](https://en.wikipedia.org/wiki/Gaza_peace_plan). Israeli military officials have reportedly described renewed fighting as "almost inevitable" [Israel threatens Gaza war resumption to force disarmament ...](https://www.aljazeera.com/news/2026/5/3/israel-threatens-gaza-war-resumption-to-force-disarmament-as-truce-frays). Israel has been expanding its territorial control within Gaza along what it calls the "Yellow Line" and has moved additional troops into the region from the Lebanese front [Israel threatens Gaza war resumption to force disarmament ...](https://www.aljazeera.com/news/2026/5/3/israel-threatens-gaza-war-resumption-to-force-disarmament-as-truce-frays). Israeli security sources have stated that if Hamas does not disarm, the IDF will restart fighting to "complete their mission" [Gaza peace plan](https://en.wikipedia.org/wiki/Gaza_peace_plan). The US-led Board of Peace overseeing the agreement has reportedly indicated it will not hold Israel to truce terms if Hamas does not accept a disarmament offer. Palestinian factions have rejected disarmament demands, citing the agreement's original terms [Israel threatens Gaza war resumption to force disarmament ...](https://www.aljazeera.com/news/2026/5/3/israel-threatens-gaza-war-resumption-to-force-disarmament-as-truce-frays). Hamas leadership has also been weighing a temporary suspension of negotiations. Despite the volatile rhetoric and ongoing violations, no formal termination or suspension has been announced by either side as of May 11, 2026.

**Exact later resolution packet**

The question resolves NO. It requires that, between May 10, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), the Israeli government (PM, Defense Minister, Security Cabinet, or IDF spokesperson) officially announced that the October 2025 Gaza ceasefire agreement was "terminated," "suspended," "ended," "nullified," or "no longer in effect." No such official announcement occurred during that window.

Evidence that the ceasefire remained formally in place throughout the entire window:
- UK Foreign Secretary's statement to Parliament on 9 June 2026 explicitly stated: "The ceasefire remains formally in place, but it is being regularly violated," and called for efforts to "resuscitate the 20 Point Plan" — i.e., the agreement was still in force, not terminated [398519].
- The Associated Press (AP) explainer on the Gaza ceasefire reports that "Both sides say the agreement is still in effect and use the word 'ceasefire' in their communications," and quotes IDF military spokesperson Lt. Col. Nadav Shoshani saying "While Hamas' actions undermine the ceasefire, Israel remains fully committed to upholding it" — the opposite of a termination declaration [de1967].
- Al Jazeera's ceasefire-violations tracker, updated June 30, 2026 (covering violations through June 29, 2026), states the US insists the "ceasefire" is still holding and describes ongoing violations, but reports no official Israeli announcement terminating or suspending the agreement [336cb5].

Actions during the window that constituted violations/escalation — but NOT an official termination/suspension of the agreement — and therefore explicitly do not qualify under the resolution criteria:
- Netanyahu's late-May 2026 order for the IDF to seize/increase control to 70% of the Gaza Strip was widely reported as "violating the ceasefire deal," not ending it (BBC/Guardian coverage). Under the resolution criteria, "mere reports of escalation, renewed military operations, or ceasefire violations — without an explicit declaration that the agreement itself is terminated or suspended — do not qualify."
- Reuters coverage throughout June 2026 (e.g., June 7, 11, 15) consistently described the situation as fighting "paused since October under a ceasefire," with continued negotiations to implement further phases — again, no termination.

No statement from the Israeli PM, Defense Minister, Security Cabinet, or IDF spokesperson declaring the agreement terminated/suspended was found on official Israeli channels or cross-referenced by two or more of Reuters/AP/AFP. Because no qualifying official announcement was confirmed by 23:59 UTC on July 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-219. `b8a571c0-68ac-5dac-bb98-da79a6a0920d`

- Present date: `2026-05-12 20:38:24.146961`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will María Corina Machado physically return to Venezuela between May 10, 2026, and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if María Corina Machado is confirmed to have physically returned to Venezuelan territory (i.e., physical presence on Venezuelan soil, including its mainland, islands, and territorial waters as defined by the map at https://en.wikipedia.org/wiki/Geography_of_Venezuela) on or after May 10, 2026 (00:00 UTC) and on or before July 1, 2026 (23:59 UTC).

"Physically return" means that Machado is confirmed to be bodily present on Venezuelan territory — this includes arrival by land, air, or sea. Brief transits (e.g., a plane refueling stop without disembarking) do not count; she must disembark or otherwise set foot on Venezuelan soil.

This question resolves **No** if no such confirmed return occurs within the specified window.

**Resolution sources:** Credible reporting from at least one major international news agency, such as Reuters (https://www.reuters.com), Associated Press (https://apnews.com), or Agence France-Presse (https://www.afp.com), confirming her physical presence in Venezuela. Reporting from BBC, The New York Times, or The Washington Post would also suffice. Given Machado's global profile as a Nobel laureate and major opposition figure, any return to Venezuela would be widely reported by these outlets.

**Pre-cutoff background**

María Corina Machado is a Venezuelan opposition leader and 2025 Nobel Peace Prize laureate who has been living in exile since leaving Venezuela in December 2025. She has been primarily based in the United States, with travel to Europe for public appearances. As of April 20, 2026 (UTC), she was in Madrid, Spain, where she told Reuters she "absolutely" sees herself back in Venezuela soon and expects to return before the end of 2026, though she did not set a specific date [Venezuela's Machado plans to return home by end of year, urges ...](https://www.reuters.com/world/americas/venezuelas-machado-plans-return-home-by-end-year-urges-swift-elections-2026-04-20/). In early March 2026, she stated she would return "within the next few weeks," but as of May 2026 she has not yet done so. Her return is described as "the real test" of Venezuela's political opening following the January 2026 capture of Nicolás Maduro by U.S. forces. The current Venezuelan government, led by Delcy Rodríguez, has not explicitly guaranteed her safe return. Reports indicate Trump advised Machado not to return immediately, and she is coordinating closely with the U.S. on the timing.

The GJOpen forecasting market for "Will María Corina Machado publicly return to Venezuela before 20 June 2026?" has shown approximately 17% probability, reflecting significant skepticism that her return will happen on this timeline despite her stated intentions. Key factors include: U.S.-Venezuela diplomatic dynamics, the Rodríguez government's tolerance, security risks to Machado, and opposition electoral strategy considerations.

**Exact later resolution packet**

This question resolves NO. María Corina Machado was NOT confirmed to have physically returned to Venezuelan soil between May 10, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC).

Evidence from the specified resolution-source outlets:

1. Associated Press (https://apnews.com/article/panama-venezuela-opposition-machado-nobel-4f3c9306b348040f63a43c82272f141b), May 23, 2026: Machado was in Panama City, holding a press conference with other opposition leaders, stating she "intends to return to her home country before the end of 2026" — confirming she had NOT yet returned at that point [Venezuela's Machado eyes return home from exile before end of 2026](https://apnews.com/article/panama-venezuela-opposition-machado-nobel-4f3c9306b348040f63a43c82272f141b).

2. Reuters (https://www.reuters.com/world/americas/venezuelas-machado-says-she-will-return-venezuela-help-quake-victims-2026-06-29/), June 29, 2026: Reports Machado was "currently in Panama" and "accused the Venezuelan government of blocking her attempt to return to the country" — i.e., she was outside Venezuela and her return attempt failed. (Corroborated by TRT/Bloomberg reporting of a "last week's aborted attempt.")

3. The New York Times (https://www.nytimes.com/2026/06/30/world/americas/trump-machado-venezuela-rift.html), published June 30, 2026 and updated July 1, 2026 (i.e., at the very close of the resolution window): explicitly states Machado "has made a forceful bid in the past week to return to her country," that the Trump administration "repeatedly rejected her requests," and that she "has not returned" since leaving Venezuela in December 2025 [U.S. Undercuts Venezuela's Opposition Leader as She Tries to Return](https://www.nytimes.com/2026/06/30/world/americas/trump-machado-venezuela-rift.html).

Because the latest authoritative reporting — dated at the end of the resolution window (July 1, 2026, UTC) — confirms she had not set foot on Venezuelan territory, and all reporting throughout May–July 2026 places her outside Venezuela (primarily Panama/US), with her return attempt actively blocked/aborted, no confirmed physical return occurred in the window. The question is NOT a conditional, so it resolves straightforwardly on the outcome: NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-220. `9ecfdd5e-d7f0-51f8-8ed5-b92788fc3a7f`

- Present date: `2026-05-16 07:25:57.055355`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-06-05T00:00:00`

**Question**

Will the RBI Monetary Policy Committee change its stance from 'neutral' to 'accommodative' at its June 2026 meeting?

**Resolution criteria**

This question resolves **Yes** if the official RBI Monetary Policy Statement issued following the June 3–5, 2026 MPC meeting explicitly states that the MPC has decided to change its monetary policy stance to **'accommodative'** (as defined by the RBI's monetary policy framework — see https://www.rbi.org.in/Scripts/PublicationsView.aspx?id=19088 — where 'accommodative' means the MPC is signaling a bias toward maintaining or further reducing the policy rate, with rate hikes being unlikely).

This question resolves **No** if:
- The MPC retains its 'neutral' stance (defined as flexibility to move in either direction on rates), or
- The MPC adopts any other stance (e.g., 'tightening' or 'calibrated tightening'), or
- The June 2026 MPC meeting does not take place by June 30, 2026, 23:59 IST (18:29 UTC).

The stance change must be formally stated in the official Monetary Policy Statement or the Resolution of the Monetary Policy Committee published on the RBI website (https://www.rbi.org.in/scripts/annualpolicy.aspx). The resolution source is the official Reserve Bank of India website at https://www.rbi.org.in/, specifically the 'Monetary Policy Statement' or the 'Minutes of the Monetary Policy Committee' for the June 2026 meeting.

**Pre-cutoff background**

The Reserve Bank of India's (RBI) Monetary Policy Committee (MPC) meets six times per fiscal year to set monetary policy. At each meeting, the MPC decides on the policy repo rate and adopts a monetary policy stance. The stance signals the future direction of policy: 'neutral' indicates flexibility in either direction, while 'accommodative' signals a bias toward easing (i.e., further rate cuts are more likely than hikes).

At its April 6–8, 2026 meeting, the MPC unanimously kept the repo rate unchanged at 5.25% and maintained a 'neutral' stance, citing global uncertainty, elevated commodity prices, and supply-side risks. This followed cumulative rate cuts of 125 basis points during the prior easing cycle. The RBI Governor Sanjay Malhotra hinted at the possibility of lower interest rates in the short-to-medium term, but the committee chose to hold steady amid geopolitical risks.

The next MPC meeting is scheduled for June 3–5, 2026 (IST), with the policy announcement expected on June 5, 2026 at approximately 10:00 AM IST (04:30 UTC). Some market commentators have argued that conditions are becoming suitable for the RBI to shift its stance to 'accommodative' to signal extended rate cuts, while others expect the MPC to maintain its cautious 'neutral' posture given ongoing global uncertainties.

Current repo rate as of May 13, 2026: 5.25%.
Current monetary policy stance as of May 13, 2026: Neutral (adopted at the April 2026 meeting).

**Exact later resolution packet**

The question asks whether the RBI Monetary Policy Committee (MPC) changed its stance from 'neutral' to 'accommodative' at its June 2026 meeting. It resolves NO.

Evidence from the official Reserve Bank of India website (rbi.org.in):

1. Antecedent/timing check: The June 2026 MPC meeting DID take place before the June 30, 2026 deadline. The RBI's annual policy page (https://www.rbi.org.in/scripts/annualpolicy.aspx) and the associated press release confirm the MPC held its meeting from June 3 to 5, 2026, with the resolution published June 5, 2026 [https://www.rbi.org.in/scripts/annualpolicy.aspx](https://www.rbi.org.in/scripts/annualpolicy.aspx) [https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=62863](https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=62863).

2. Stance decision (formally stated): The official "Resolution of the Monetary Policy Committee (MPC) June 3 to 5, 2026" (published at https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=62863) explicitly states that "The MPC also decided to retain the neutral stance." The committee kept the policy repo rate unchanged at 5.25 per cent [https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=62863](https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=62863). This is an explicit, formally-stated retention of the 'neutral' stance in the official Monetary Policy Statement/Resolution — not merely implied by rate action.

3. Because the MPC formally RETAINED its 'neutral' stance and did NOT change it to 'accommodative,' the YES condition (an explicit statement that the MPC decided to change the stance to 'accommodative') was not met. Under the resolution criteria, retaining the 'neutral' stance resolves the question NO.

Resolution source URLs:
- June 2026 MPC Resolution / Monetary Policy Statement: https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=62863
- RBI Annual/Monetary Policy index: https://www.rbi.org.in/scripts/annualpolicy.aspx

Therefore the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-221. `3793fd18-e8b5-578d-9d69-4e6735a881d3`

- Present date: `2026-05-14 07:58:20.863069`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Israeli Knesset pass the bill to split the role of the Attorney General into separate offices by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the bill to split the role of the Attorney General into separate offices (a Director of Public Prosecutions and a Legal Adviser, or equivalent formulation) passes its third and final reading in the Knesset Plenum on or after May 12, 2026, and on or before July 1, 2026, at 23:59 IDT (Israel Daylight Time, UTC+3).

This question resolves as **No** if the bill has not passed its third reading by that deadline.

"Passing" is defined as the bill receiving approval in its second and third (final) readings in the Knesset Plenum. If the bill is merged with related legislation (such as the "Prosecutor General Bill, 2022"), it will be considered passed if the core provisions — formally splitting the Attorney General's powers into separate offices — are enacted.

The resolution source is the official Knesset legislation database at https://main.knesset.gov.il/en/activity/Pages/Legislation.aspx and/or Knesset press releases at https://m.knesset.gov.il/en/news/pressreleases/Pages/default.aspx. Credible reporting from major outlets (e.g., Times of Israel, Haaretz, Reuters) may serve as supplementary confirmation.

**Pre-cutoff background**

The Israeli coalition government is advancing legislation to split the role of the Attorney General into separate offices as part of its judicial overhaul agenda. The current Attorney General holds multiple roles simultaneously: heading criminal prosecution, representing the state in court, and providing legal counsel to the government. The bill aims to separate these functions to resolve what proponents call built-in conflicts of interest.

While earlier proposals considered splitting the role into three positions, the current framework being debated in the Knesset Constitution, Law and Justice Committee — based on a 2008 draft memorandum — proposes splitting the role into two distinct offices: a "Director of Public Prosecutions" (responsible for the criminal sphere) and a "Legal Adviser" (responsible for remaining powers including advising the government) [Explainer: The Proposals to “Split” the Role of the Attorney General](https://en.idi.org.il/articles/62285). The bill would also give the government greater control over appointing and dismissing the Attorney General and would make the Attorney General's legal rulings non-binding on the government [https://www.timesofisrael.com/contentious-proposals-punctuate-planned-legislative-blitz-as-knesset-gets-back-to-work/](https://www.timesofisrael.com/contentious-proposals-punctuate-planned-legislative-blitz-as-knesset-gets-back-to-work/).

The bill (sponsored by MKs Simcha Rothman, Ohad Tal, and Michal Woldiger) passed its preliminary reading in the Knesset Plenum on October 29, 2025, with a vote of 59 in favor and 44 against [Knesset Plenum approves in preliminary reading bill to split the post ...](https://m.knesset.gov.il/en/news/pressreleases/pages/press291025b.aspx). It was then sent to the Knesset Constitution, Law and Justice Committee for deliberation. As of April 15, 2026, the Committee is actively deliberating on the draft [Explainer: The Proposals to “Split” the Role of the Attorney General](https://en.idi.org.il/articles/62285). The bill still needs to pass first, second, and third readings in the Knesset Plenum to become law.

Reports from May 2026 indicate the coalition may seek to rush the bill through in the coming weeks as part of a broader legislative blitz before potential elections [https://www.timesofisrael.com/contentious-proposals-punctuate-planned-legislative-blitz-as-knesset-gets-back-to-work/](https://www.timesofisrael.com/contentious-proposals-punctuate-planned-legislative-blitz-as-knesset-gets-back-to-work/). However, the bill faces significant opposition from the legal establishment and civil society. For more background on the proposals, see the Israel Democracy Institute's explainer: https://en.idi.org.il/articles/62285

**Exact later resolution packet**

The question resolves NO. It required the bill splitting the Attorney General's role into separate offices to pass its third and final reading in the Knesset Plenum between May 12, 2026 and July 1, 2026 (23:59 IDT). The evidence shows the bill only reached its FIRST reading by that deadline and did not pass its second and third (final) readings.

Timeline established from sources:
- Preliminary reading passed October 29, 2025 (stated in the question).
- The Constitution, Law and Justice Committee approved the bill ("Attorney General and Prosecutor General Bill (Appointment, Tenure, Roles and Powers), 2026") for its FIRST reading on May 25, 2026, per the official Knesset press release; committee chair MK Simcha Rothman said it would be laid on the plenum table for its first reading [259370].
- The bill passed its FIRST reading in the Knesset plenum early Tuesday, June 2, 2026, by a vote of 65-47, after which it was returned to the Constitution, Law and Justice Committee to prepare for its second and third readings [68c098, 55c3e3].
- In parallel, the Knesset was dissolving itself (dissolution bill passed first reading 106-0 around June 2, 2026), with elections to the 26th Knesset scheduled for a September–October 2026 window.
- As of June 21, 2026, a Haaretz opinion piece confirmed the bill had only been "advanced" and was still in the Constitution, Law and Justice Committee being prepared ahead of its second and third votes — i.e., it had NOT become law [8100f3]. The Times of Israel likewise reported (June 2, 2026) that even if the bill were not passed into law before the Knesset disbands, its advancement would let the coalition apply legislative "continuity" in the next Knesset [68c098].

I ruled out a false positive: a widely-circulated report of a bill passing its "second and third readings" by 62-48 with one abstention refers to the separate "Death Penalty for Terrorists Law (2026)" passed March 30, 2026 — NOT the Attorney General split bill.

Therefore, the bill did not pass its third and final reading by July 1, 2026, and the question resolves NO (0).

Key URLs: Official Knesset press release https://main.knesset.gov.il/EN/News/PressReleases/Pages/press25526w.aspx ; Times of Israel https://www.timesofisrael.com/legislation-to-split-and-weaken-role-of-attorney-general-passes-first-knesset-reading/ ; Jerusalem Post https://www.jpost.com/israel-news/politics-and-diplomacy/article-898054 ; Haaretz (June 21, 2026) https://www.haaretz.com/opinion/2026-06-21/ty-article-opinion/.premium/if-this-bill-becomes-law-israel-will-become-an-autocracy-with-no-oversight/0000019e-e648-dc8a-afbe-f77d32450000

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-222. `cbd1cf75-7f4d-55ba-88e4-69c7b54acbd2`

- Present date: `2026-05-29 02:59:23.195146`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will a second round of US-facilitated quadripartite talks on Western Sahara be announced or held between May 12, 2026, and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026, and on or before July 1, 2026 (23:59 UTC), any of the following occur:

1. A formal announcement is made that a new round of quadripartite talks has been scheduled, **or**
2. A new round of quadripartite talks is actually held.

**Definition of "quadripartite talks":** A meeting or structured diplomatic engagement (including proximity talks or shuttle diplomacy) in which official government-level representatives of all four parties—Morocco, Algeria, the Polisario Front, and Mauritania—participate. All four parties must be confirmed participants; bilateral or trilateral meetings do not qualify. The parties need not be in the same room simultaneously; proximity talks (where a mediator shuttles between parties in separate rooms) qualify, provided all four parties are present at the same venue or formally participating in the same structured process.

**Definition of "US-facilitated":** The meeting must be organized, hosted, or chaired by one or more U.S. government officials (e.g., a U.S. Special Envoy, the U.S. Senior Advisor for Arab and African Affairs, or the U.S. Ambassador to the UN), **or** the U.S. Department of State must issue an official statement confirming U.S. facilitation of the talks. A meeting facilitated solely by the UN Personal Envoy for Western Sahara without U.S. involvement does not qualify.

**Exclusion of prior events:** The February 8–9, 2026, Madrid meeting does not count toward resolution. Only announcements or meetings occurring on or after May 12, 2026 (00:00 UTC) qualify.

**Resolution source:** Official press releases or statements from the U.S. Department of State (https://www.state.gov/press-releases/) or the U.S. Mission to the United Nations (https://usun.usmission.gov/). Credible international news reporting from Reuters (https://www.reuters.com/), Associated Press (https://apnews.com/), or AFP may serve as secondary confirmation sources.

If no qualifying announcement or meeting occurs by July 1, 2026 (23:59 UTC), this question resolves **No**.

**Pre-cutoff background**

The Western Sahara dispute has been a source of regional conflict since 1975. On February 8–9, 2026, a breakthrough occurred when ministerial-level delegations from Morocco, Algeria, the Polisario Front, and Mauritania met at the U.S. embassy in Madrid for the first direct quadripartite talks since 2019 [Renewed U.S.-led Talks in Madrid Lend Momentum to ...](https://www.crisisgroup.org/anb/middle-east-north-africa/western-sahara/renewed-us-led-talks-madrid-lend-momentum-western-sahara-diplomacy-big-challenges-remain). The meeting was chaired by U.S. Senior Advisor for Arab and African Affairs Massad Boulos and U.S. Ambassador to the UN Mike Waltz [Renewed U.S.-led Talks in Madrid Lend Momentum to ...](https://www.crisisgroup.org/anb/middle-east-north-africa/western-sahara/renewed-us-led-talks-madrid-lend-momentum-western-sahara-diplomacy-big-challenges-remain). Morocco presented a revised 40-page autonomy plan during the nearly four-hour session [Renewed U.S.-led Talks in Madrid Lend Momentum to ...](https://www.crisisgroup.org/anb/middle-east-north-africa/western-sahara/renewed-us-led-talks-madrid-lend-momentum-western-sahara-diplomacy-big-challenges-remain). While some media reports suggested an agreement to form a committee of experts to prepare for a second round in May, other informed sources indicate no such decision was formally taken [Renewed U.S.-led Talks in Madrid Lend Momentum to ...](https://www.crisisgroup.org/anb/middle-east-north-africa/western-sahara/renewed-us-led-talks-madrid-lend-momentum-western-sahara-diplomacy-big-challenges-remain).

On October 31, 2025, the UN Security Council adopted Resolution 2797, renewing MINURSO's mandate until October 2026 and creating pressure for diplomatic progress within that timeframe.

On May 5, 2026, the Polisario Front launched a projectile attack on the Moroccan-controlled city of Es-Smara, triggering widespread international condemnation from the United States, France, the EU, the UAE, UK, and others ['This Is Not a Time for Military Escalation,' UN Envoy Warns After Es ...](https://www.moroccoworldnews.com/2026/05/294336/this-is-not-a-time-for-military-escalation-un-envoy-warns-after-es-smara-attack/). The UN has called for restraint and a return to negotiations rather than military escalation ['This Is Not a Time for Military Escalation,' UN Envoy Warns After Es ...](https://www.moroccoworldnews.com/2026/05/294336/this-is-not-a-time-for-military-escalation-un-envoy-warns-after-es-smara-attack/). As of May 13, 2026, no new round of quadripartite talks has been publicly announced, and the Es-Smara attack has complicated the diplomatic landscape, though it may also increase urgency for renewed dialogue.

**Exact later resolution packet**

The question resolves NO. It asked whether a second round of US-facilitated quadripartite talks on Western Sahara (with all four parties — Morocco, Algeria, the Polisario Front, and Mauritania) would be announced or held between May 12, 2026 and July 1, 2026 (23:59 UTC).

Timeline of the actual US-facilitated quadripartite rounds (all BEFORE the resolution window):
- Round 1: Madrid, February 8-9, 2026, at the US Embassy, chaired by US Senior Advisor Massad Boulos and US Ambassador to the UN Mike Waltz. This is explicitly excluded by the resolution criteria.
- Round 2: Washington, February 23-24, 2026 (widely reported by RFI, Africanews, Anadolu, and others). This also fell before May 12, 2026, so it does not count toward resolution.

Evidence that NO qualifying announcement or meeting occurred in the May 12 – July 1, 2026 window:
- Africa Intelligence, "Negotiations over Western Sahara take a backseat to Middle East conflict," published May 25, 2026, states that the situation has been "stagnant/paralysed" since the two rounds held in February in Madrid and Washington, with the proposal having "yet to lead to an agreement between the parties" and no new round scheduled [Algeria/Morocco • Negotiations over Western Sahara take a ...](https://www.africaintelligence.com/north-africa/2026/05/25/negotiations-over-western-sahara-take-a-backseat-to-middle-east-conflict,110771247-art).
- Europe and Arabs, article dated July 1, 2026, references only the February 23-24, 2026 Washington meeting involving Massad Boulos and Mike Waltz, and reports no subsequent quadripartite negotiations within the May 12–July 1 window [Negotiations on Western Sahara, Led by the UN ... - Europe and Arabs](https://europe-arabs.com/en/news/7153).
- The APA article reporting a "rumored" second round for Washington in May 2026 was published February 17, 2026, and was purely speculative; no such talks were confirmed as announced or held in the window [US envoy signals decisive shift in Western Sahara ...](https://apanews.net/us-envoy-signals-decisive-shift-in-western-sahara-negotiations/).
- The Wikipedia "Western Sahara conflict" article (last edited June 15, 2026) contains no mention of any quadripartite talks after February 2026 [Western Sahara conflict - Wikipedia](https://en.wikipedia.org/wiki/Western_Sahara_conflict).
- The Arab Weekly UN Security Council briefings article (April 22, 2026) and other June 2026 coverage likewise reflect a diplomatic standstill, further compounded by the May 5, 2026 Polisario attack on Es-Smara which complicated the diplomatic landscape [UN Security Council briefings reshuffle Western Sahara file priorities](https://thearabweekly.com/un-security-council-briefings-reshuffle-western-sahara-file-priorities).

No official press release from the U.S. Department of State (state.gov) or the U.S. Mission to the UN (usun.usmission.gov), nor any Reuters/AP/AFP report, announced or documented a new quadripartite round in the window. The antecedent-style requirement (all four parties confirmed, US facilitation) is moot because no qualifying event occurred at all. Since no qualifying announcement or meeting occurred by July 1, 2026 (23:59 UTC), the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-223. `794b1065-37c8-57b9-8f3f-c8fb46d2c44d`

- Present date: `2026-05-01 16:17:03.943581`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Maersk announce resumption of regular Suez Canal transits for any of its Asia-Europe container services between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 (to exclude prior routing decisions), and on or before June 1, 2026, at 23:59 UTC, Maersk publishes an official advisory or press release on its newsroom (https://www.maersk.com/news) or its Red Sea situation page (https://www.maersk.com/stay-ahead) announcing the resumption of regular, scheduled transits through the Suez Canal for any of its Asia-Europe container service lines (e.g., AE1, AE2, AE3, AE5, AE11, AE12, AE15).

**Definitions:**
- "Resumption" means an official Maersk advisory or press release stating that a named Asia-Europe service line (AE1, AE2, AE3, AE5, AE11, AE12, or AE15) will return to routing through the Suez Canal as part of its standard scheduled rotation. This includes announcements of a specific future effective date, even if that date falls after June 1, 2026.
- "Regular, scheduled transits" means the inclusion of the Suez Canal in the standard published rotation of a service line, as opposed to a one-off or ad-hoc vessel diversion. A single vessel transiting the Suez Canal without an accompanying announcement of a service-wide routing change does not qualify.
- "Asia-Europe container services" refers specifically to Maersk's AE-designated service lines connecting Asia and Europe.

This question resolves **No** if no such announcement appears on the specified Maersk pages by 23:59 UTC on June 1, 2026.

**Pre-cutoff background**

Since late 2023, major container shipping lines including A.P. Moller-Maersk have diverted Asia-Europe traffic away from the Red Sea and Suez Canal due to Houthi attacks on commercial shipping. In January 2026, Maersk announced its first structural return to the trans-Suez route for the MECL service, departing Jebel Ali on January 15, 2026 [ME11 & MECL Rerouted via Cape of Good Hope | Maersk](https://www.maersk.com/news/articles/2026/03/01/me11-mecl-rerouting-cape-of-good-hope-march). However, by March 1, 2026, Maersk paused all Trans-Suez sailings and rerouted its ME11 and MECL services back via the Cape of Good Hope due to escalating Middle East security concerns, also suspending vessel crossings in the Strait of Hormuz [ME11 & MECL Rerouted via Cape of Good Hope | Maersk](https://www.maersk.com/news/articles/2026/03/01/me11-mecl-rerouting-cape-of-good-hope-march).

On February 27, 2026, Maersk announced changes to its Asia-Europe network (services AE1, AE2, AE3, AE5, AE11, AE12, AE15) effective April 2026, noting that for AE12 and AE15, Maersk and Hapag-Lloyd would implement changes to route through the Red Sea and the Suez Canal "when possible" at a later stage [Update to Asia- Europe network 2026 - Maersk](https://www.maersk.com/news/articles/2026/02/27/asia-europe-network-update-2026).

As of late April 2026, Maersk describes the Middle East situation as "highly volatile" and states that "full maritime certainty" is not assured [Red Sea / Gulf of Aden situation - Maersk](https://www.maersk.com/stay-ahead). The company continues to manage contingency measures including landbridge solutions and emergency freight rates. War risk insurance premiums remain elevated at approximately 1% of ship value compared to a pre-crisis level of 0.05%, representing a significant barrier to resumption.

**Exact later resolution packet**

The question resolves NO. The resolution criteria require an official Maersk advisory/press release on its newsroom (https://www.maersk.com/news) or Red Sea situation page (https://www.maersk.com/stay-ahead) announcing resumption of regular, scheduled Suez Canal transits for a named Asia-Europe service line (AE1, AE2, AE3, AE5, AE11, AE12, AE15), published between April 30 and June 1, 2026, 23:59 UTC.

A review of the Maersk newsroom shows the full list of May 2026 articles, none of which announce a return to the Suez Canal for any AE-designated Asia-Europe service. The May 2026 articles cover topics like the new FI2 India-China service, regional market updates, Q1 results, and case studies—none address Suez Canal resumption for the specified services [0c9fba].

The Red Sea / Gulf of Aden situation page (https://www.maersk.com/stay-ahead) likewise contains no such announcement. Its updates through May 2026 (e.g., "Middle East Operational Update 33" dated May 25, 2026, and a May 28, 2026 update on Jeddah Gateway rerouting) confirm Maersk was still managing contingency measures including landbridge solutions and alternative routing due to the volatile situation—not resuming scheduled Suez transits [221f66].

This is consistent with external reporting from May 2026: WorldCargo News reported "Maersk reviewing return to Red Sea" (a review, not a resumption announcement) and FreightWaves reported "Maersk: No timeline for Red Sea return." Note also that the prior structural returns (MECL in January 2026, ME11 in February 2026) are not AE-designated Asia-Europe services and in any case were paused/rerouted via Cape of Good Hope on March 1, 2026, well before the April 30 window opens.

Since no qualifying announcement appeared on the specified Maersk pages within the April 30 – June 1, 2026 window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-224. `c0e91aae-a7cd-5ac2-b7d7-71dfb086d15e`

- Present date: `2026-05-03 01:43:17.936104`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Guyana sign any new petroleum exploration or production agreement for an offshore block in waters claimed by Venezuela between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between 00:00 UTC on May 1, 2026 and 23:59 UTC on June 1, 2026, the Government of Guyana officially announces the signing or award of any new Petroleum Exploration License (PEL) or Production Sharing Agreement (PSA) for an offshore block located in waters that fall within Venezuela's territorial claim over the [Essequibo region](https://en.wikipedia.org/wiki/Guayana_Esequiba) (i.e., waters off the coast of the territory west of the Essequibo River, as depicted on the [ICJ case page](https://www.icj-cij.org/case/171)).

A "license award" is defined as: the official signing of a Petroleum Exploration License or Production Sharing Agreement, as confirmed by at least one of the following:
1. An announcement on the [Guyana Ministry of Natural Resources website](https://nre.gov.gy/) or the [Petroleum Management Programme website](https://petroleum.gov.gy/);
2. Publication in the [Official Gazette of Guyana](https://officialgazette.gov.gy/);
3. An official government press release reported by credible media (e.g., [OilNOW](https://oilnow.gy/), [Kaieteur News](https://kaieteurnewsonline.com/), [Reuters](https://www.reuters.com/), or [Guyana Chronicle](https://guyanachronicle.com/)).

Renewals, amendments, or extensions of existing licenses do not count. Only newly awarded licenses qualify. The announcement must occur on or after May 1, 2026, and by June 1, 2026 (all times UTC), to exclude prior license awards.

If no such announcement is made by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

Guyana is experiencing a major oil boom, with offshore production averaging 918,000 barrels per day in February 2026 [Guyana expands oil search - Kaieteur News](https://kaieteurnewsonline.com/2026/03/11/guyana-expands-oil-search/). The country has been actively awarding new offshore exploration blocks following its 2022 competitive licensing round, including shallow-water blocks S4 (to a TotalEnergies-led consortium), S7 (to Cybele Energy), and others [Guyana plans two more offshore block awards before year-end](https://oilnow.gy/featured/guyana-plans-two-more-offshore-block-awards-before-year-end/). As of early 2026, the government was in advanced negotiations for additional blocks, including S3 with the Guyanese firm Sispro Inc. [Guyana plans two more offshore block awards before year-end](https://oilnow.gy/featured/guyana-plans-two-more-offshore-block-awards-before-year-end/), and Vice President Jagdeo has indicated a second offshore block auction could be held in 2026 [from search results].

The Essequibo region — the territory west of the [Essequibo River](https://en.wikipedia.org/wiki/Essequibo_River) comprising roughly two-thirds of Guyana's land area — is claimed by Venezuela. Venezuela's claim extends to associated offshore maritime zones, meaning most of Guyana's prolific offshore oil blocks (including the Stabroek Block operated by ExxonMobil) lie in waters that Venezuela considers its own.

The International Court of Justice (ICJ) will begin oral hearings on the merits of the border case (Guyana v. Venezuela) on May 4, 2026, with proceedings expected to last at least one week [ICJ sets week-long hearings in Guyana-Venezuela border case ...](https://oilnow.gy/news/icj-sets-week-long-hearings-in-guyana-venezuela-border-case-nandlall-says/). This creates strategic tension: Guyana has been assertive about its sovereignty and economic development, but new license awards during active ICJ hearings could be seen as provocative or could complicate diplomatic optics. Conversely, Guyana may view continued licensing as reinforcing its sovereignty claim.

The government has been on a steady pace of block awards through direct negotiations and has indicated plans for a second auction later in 2026. Whether any new agreement is signed during the sensitive May 2026 hearing period is uncertain — the 30-70% probability range is plausible given that (a) Guyana has multiple blocks under active negotiation that could close at any time, but (b) the government may strategically pause during ICJ proceedings to avoid unnecessary controversy.

**Exact later resolution packet**

The question resolves NO. It asked whether Guyana would officially announce the signing/award of any NEW Petroleum Exploration License (PEL) or Production Sharing Agreement (PSA) for an offshore block in waters claimed by Venezuela between 00:00 UTC May 1, 2026 and 23:59 UTC June 1, 2026.

Evidence gathered:

1) The most recent documented new offshore block awards occurred BEFORE the resolution window: Block S4 PSA/PEL was signed on November 11, 2025 (with the TotalEnergies/QatarEnergy/Petronas consortium), and Block S7 PEL/PSA was signed December 9, 2025 (with Ghana's Cybele Energy). Both fall outside the May 1–June 1, 2026 window. (Reuters: "TotalEnergies, QatarEnergy and Petronas receive green light...2025-11-11"; Block-S4-Petroleum-Agreement.pdf "made by way of Deed on the 11TH day of November, 2025").

2) An exhaustive review of OilNOW's homepage and news index covering the period up to June 2, 2026 found NO reports of any new PEL or PSA being signed/awarded for an offshore block between May 1 and June 1, 2026; news during that period focused on production figures, ExxonMobil environmental approvals, local content, seismic surveys, and conferences [113caf, c43a82].

3) An exhaustive review of Kaieteur News' Oil & Gas archive covering up to June 2, 2026 likewise found NO new PEL/PSA award announcements during the window; relevant May 2026 Kaieteur articles concerned contract-renegotiation commentary, gas-purchase denials, and the explicit statement that "No extension granted for Canje, Orinduik blocks" — none of which are new awards [d34e30].

4) The pending deals that could have triggered a YES (notably the Sispro Inc. Block S3 shallow-water PSA, and the ExxonMobil-led Block S8 PSA) remained under negotiation and unsigned as of the window. Multiple reports through April–May 2026 still described Sispro's S3 PSA as "successfully negotiated" but not yet signed, and the ExxonMobil S8 talks as ongoing.

5) The ICJ merits hearings (Guyana v. Venezuela) began May 4, 2026, consistent with the question's framing that Guyana might strategically pause licensing during the sensitive hearing period.

Because no new PEL or PSA award for an offshore block was announced by any of the named sources (Ministry of Natural Resources, Petroleum Management Programme, Official Gazette, OilNOW, Kaieteur News, Reuters, Guyana Chronicle) within the May 1–June 1, 2026 window, the question resolves NO.

Key URLs:
- https://oilnow.gy/ and https://oilnow.gy/news/ (no new award in window)
- https://kaieteurnewsonline.com/category/oil-gas/ (no new award in window)
- https://kaieteurnewsonline.com/2026/05/22/no-extension-granted-for-canje-orinduik-blocks-min-bharrat/ (May 2026 news, no new award)
- https://www.reuters.com/business/energy/totalenergies-qatarenergy-petronas-sign-exploration-agreement-guyana-2025-11-11/ (prior S4 award, Nov 2025)
- https://petroleum.gov.gy/wp-content/uploads/2025/11/Block-S4-Petroleum-Agreement.pdf (S4 signed Nov 11, 2025)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-225. `e18419ad-04ea-5f20-96d2-a6c7abbe5e67`

- Present date: `2026-05-14 00:18:43.264674`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-15T00:00:00`

**Question**

Will the OSCE/ODIHR preliminary statement on the June 7, 2026 Armenian parliamentary election describe the election as having been conducted "in line with" or "consistent with" international standards?

**Resolution criteria**

This question resolves based on the official "Statement of Preliminary Findings and Conclusions" issued by the OSCE/ODIHR International Election Observation Mission for the June 7, 2026 Armenian parliamentary elections, published on the OSCE/ODIHR election mission page at https://odihr.osce.org/node/662896 or via https://www.osce.org/odihr/elections/armenia [Armenia, Parliamentary Elections, 7 June 2026](https://odihr.osce.org/node/662896).

The statement must be released on or after May 12, 2026.

**Scope of "international standards":** The relevant standards are OSCE commitments for democratic elections, particularly those in the 1990 OSCE Copenhagen Document, as well as other international obligations and standards for democratic elections that ODIHR routinely assesses (including commitments related to universal suffrage, secret ballot, freedom of expression, freedom of assembly, and equal campaigning conditions).

**YES resolution:** The question resolves YES if the preliminary statement's summary or conclusions section contains either the exact phrase "in line with" or "consistent with" when positively characterizing the overall conduct of the election relative to OSCE commitments or international standards/obligations for democratic elections. Equivalent positive phrasing (such as "met international standards" or "respected OSCE commitments") is NOT sufficient—only the verbatim phrases "in line with" or "consistent with" qualify.

**NO resolution:** The question resolves NO if:
- The preliminary statement does not contain either verbatim phrase in a positive characterization of the election's overall conduct, OR
- The statement uses these phrases only in a negative context (e.g., "not in line with"), OR
- The statement is released but does not address the overall conduct of the election relative to international standards.

**If no preliminary statement is released by July 1, 2026:** The question resolves NO.

**Pre-cutoff background**

On June 7, 2026, Armenia will hold parliamentary elections. The OSCE Office for Democratic Institutions and Human Rights (ODIHR) has deployed an Election Observation Mission (EOM) led by a core team of 13 experts, 30 long-term observers, and 250 short-term observers [Armenia, Parliamentary Elections, 7 June 2026](https://odihr.osce.org/node/662896).

The pre-election environment presents significant concerns. According to the ODIHR Needs Assessment Mission (NAM) report of March 19, 2026, the political environment is highly polarized, with tensions between the ruling party and the opposition as well as between the government and the Armenian Apostolic Church. Several opposition figures have been detained or prosecuted, including Archbishop Bagrat Galstanyan (a leader of 2024 protests) and former President Serzh Sargsyan on bribery charges. Opposition mayors in Gyumri and Masis have also faced charges. The media landscape is polarized, with the public broadcaster widely perceived as pro-government, and the closure of church-affiliated Shoghakat TV viewed by many as politically motivated. Journalists face increased pressure including verbal attacks, threats, and lawsuits. There are also concerns about hybrid threats including foreign interference, cyberattacks, and online disinformation [[PDF] REPUBLIC OF ARMENIA](https://odihr.osce.org/sites/default/files/documents/official_documents/2026/03/ARM_Parliamentary_2026_NAM%20Report_19.03.2026.pdf).

For context, ODIHR's preliminary statement on Armenia's 2021 early parliamentary elections was generally positive, noting the elections were competitive and well-run despite a tense post-war environment. However, the significantly more polarized 2026 environment—with opposition arrests and media restrictions—means a positive assessment is far from guaranteed.

ODIHR typically releases its "Statement of Preliminary Findings and Conclusions" at a press conference the day after election day. For the June 7, 2026 election, this is expected on June 8, 2026 [Armenia, Parliamentary Elections, 7 June 2026](https://odihr.osce.org/node/662896). The statement assesses compliance with OSCE commitments as outlined in the 1990 Copenhagen Document and other international obligations for democratic elections.

**Exact later resolution packet**

The question resolves NO (0).

WHAT HAPPENED: The OSCE/ODIHR International Election Observation Mission published its "Statement of Preliminary Findings and Conclusions" for the June 7, 2026 Armenian parliamentary elections on 8 June 2026, hosted on the ODIHR site (https://odihr.osce.org/odihr/664831, PDF at https://odihr.osce.org/sites/default/files/documents/official_documents/2026/06/ARM%20Parliamentary%202026_PS_08.06.2026.pdf) and mirrored via the OSCE PA. This is on/after the May 12, 2026 cutoff and before the July 1, 2026 deadline, so the statement was released and the question does not resolve NO by default for non-publication [Armenia, Parliamentary Elections, 7 June 2026](https://odihr.osce.org/node/662896)[Armenia, Parliamentary Elections, 7 June 2026](https://odihr.osce.org/odihr/664831)[https://odihr.osce.org/sites/default/files/documents/official_documents/2026/06/ARM%20Parliamentary%202026_PS_08.06.2026.pdf](https://odihr.osce.org/sites/default/files/documents/official_documents/2026/06/ARM%20Parliamentary%202026_PS_08.06.2026.pdf)[[PDF] Armenia – Parliamentary Elections, 7 June 2026 ... - OSCE PA](https://www.oscepa.org/en/documents/election-observation/election-observation-statements/armenia/statements-2/5525-2026-parliamentary-1).

THE SUMMARY WORDING: The "Preliminary Conclusions"/summary section opens with: "The 7 June 2026 parliamentary elections offered voters a genuine choice among political alternatives in a well-run process." It characterizes the election using terms like "genuine choice," "well-run process," and notes fundamental freedoms while raising concerns about a highly polarized environment, foreign pressure, campaign-finance oversight, biased media, and allegations of vote-buying. Crucially, the OVERALL characterization does NOT use the verbatim phrases "in line with" or "consistent with" [https://odihr.osce.org/sites/default/files/documents/official_documents/2026/06/ARM%20Parliamentary%202026_PS_08.06.2026.pdf](https://odihr.osce.org/sites/default/files/documents/official_documents/2026/06/ARM%20Parliamentary%202026_PS_08.06.2026.pdf)[[PDF] Armenia – Parliamentary Elections, 7 June 2026 ... - OSCE PA](https://www.oscepa.org/en/documents/election-observation/election-observation-statements/armenia/statements-2/5525-2026-parliamentary-1)[Armenia's voters were offered a genuine choice against ...](https://odihr.osce.org/odihr/665473).

OCCURRENCES OF THE REQUIRED PHRASES (none qualify): A verbatim scan of the statement found the phrases only in non-qualifying contexts:
- "In line with the requirement that at least 30 per cent of candidates on each list be from either gender, women comprised 37.3 per cent of candidates..." — this describes a specific technical aspect (gender quota compliance), not the overall conduct of the election [https://odihr.osce.org/sites/default/files/documents/official_documents/2026/06/ARM%20Parliamentary%202026_PS_08.06.2026.pdf](https://odihr.osce.org/sites/default/files/documents/official_documents/2026/06/ARM%20Parliamentary%202026_PS_08.06.2026.pdf)[[PDF] Armenia – Parliamentary Elections, 7 June 2026 ... - OSCE PA](https://www.oscepa.org/en/documents/election-observation/election-observation-statements/armenia/statements-2/5525-2026-parliamentary-1).
- "This is consistent with the findings of multiple fact-checking organizations which identified an increase in co-ordinated disinformation operations originating from abroad." — this refers to disinformation findings, not overall conduct [https://odihr.osce.org/sites/default/files/documents/official_documents/2026/06/ARM%20Parliamentary%202026_PS_08.06.2026.pdf](https://odihr.osce.org/sites/default/files/documents/official_documents/2026/06/ARM%20Parliamentary%202026_PS_08.06.2026.pdf)[[PDF] Armenia – Parliamentary Elections, 7 June 2026 ... - OSCE PA](https://www.oscepa.org/en/documents/election-observation/election-observation-statements/armenia/statements-2/5525-2026-parliamentary-1).
- "Decisions on ballot validity were assessed as consistent in almost all observations..." — a narrow technical/election-day observation, not overall conduct [https://odihr.osce.org/sites/default/files/documents/official_documents/2026/06/ARM%20Parliamentary%202026_PS_08.06.2026.pdf](https://odihr.osce.org/sites/default/files/documents/official_documents/2026/06/ARM%20Parliamentary%202026_PS_08.06.2026.pdf).

APPLYING THE RESOLUTION CRITERIA: YES requires the summary/conclusions to contain the exact phrase "in line with" or "consistent with" when POSITIVELY characterizing the OVERALL conduct of the election relative to OSCE commitments/international standards. Equivalent positive phrasing ("genuine choice," "well-run," "sound basis for democratic elections") is explicitly NOT sufficient per the criteria. Because neither verbatim phrase is applied to the overall conduct — only to a gender quota, disinformation findings, and ballot-validity consistency — the YES condition is not met, so the question resolves NO [https://odihr.osce.org/sites/default/files/documents/official_documents/2026/06/ARM%20Parliamentary%202026_PS_08.06.2026.pdf](https://odihr.osce.org/sites/default/files/documents/official_documents/2026/06/ARM%20Parliamentary%202026_PS_08.06.2026.pdf)[[PDF] Armenia – Parliamentary Elections, 7 June 2026 ... - OSCE PA](https://www.oscepa.org/en/documents/election-observation/election-observation-statements/armenia/statements-2/5525-2026-parliamentary-1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-226. `3a71cdfe-dbf7-5158-a54b-0756f089ebff`

- Present date: `2026-05-02 18:28:41.456961`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the UK-France led multinational mission to protect shipping in the Strait of Hormuz formally begin operations by June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 1, 2026, and by 23:59 UTC on June 1, 2026, the UK-France led multinational mission to protect shipping in the Strait of Hormuz formally begins operations. "Formally begins operations" means any one of the following occurs:

1. **Declaration of Initial Operating Capability (IOC):** An official public statement by the UK Ministry of Defence (https://www.gov.uk/government/organisations/ministry-of-defence), the French Ministry of the Armed Forces (https://www.defense.gouv.fr/), or the designated coalition command authority declaring the mission has achieved "Initial Operating Capability" — defined as the point at which a military capability is judged to have reached a minimum usable standard and can begin performing its assigned mission (see https://en.wikipedia.org/wiki/Initial_operating_capability).

2. **First escort or patrol operation:** The mission conducts its first operational escort of a commercial vessel through the Strait of Hormuz, or conducts its first patrol within the Strait of Hormuz operational area, under the banner of this specific multinational mission. A "patrol" means the deliberate deployment of one or more naval vessels to monitor, deter threats to, or safeguard commercial shipping within the Strait of Hormuz. An "escort" means the accompaniment of one or more commercial vessels by mission naval assets through the Strait.

3. **First mine clearance operation:** The mission conducts its first mine clearance operation in the Strait of Hormuz under the mission's authority.

Any of these events must be confirmed by at least one of the following sources: official UK Ministry of Defence website (https://www.gov.uk/government/organisations/ministry-of-defence), official French Ministry of the Armed Forces website (https://www.defense.gouv.fr/), Reuters (https://www.reuters.com/), Associated Press (https://apnews.com/), or Agence France-Presse reporting carried by major outlets.

If none of these events occur by 23:59 UTC on June 1, 2026, the question resolves NO.

**Pre-cutoff background**

On April 17, 2026, France and the United Kingdom convened 51 countries for an international summit on the Strait of Hormuz ([Joint Statement by President Macron and Prime Minister Starmer ...](https://www.elysee.fr/en/emmanuel-macron/2026/04/17/joint-statement-by-president-macron-and-prime-minister-starmer-co-chairs-of-the-international-summit-on-the-strait-of-hormuz)). The summit resulted in a joint statement confirming the establishment of an "independent and strictly defensive multinational mission" to protect merchant vessels, reassure commercial shipping operators, and conduct mine clearance operations ([Joint Statement by President Macron and Prime Minister Starmer ...](https://www.elysee.fr/en/emmanuel-macron/2026/04/17/joint-statement-by-president-macron-and-prime-minister-starmer-co-chairs-of-the-international-summit-on-the-strait-of-hormuz)). The mission was announced in response to Iran's blockage of the Strait of Hormuz since February 28, 2026, which has severely disrupted global energy trade.

Following the summit, on April 22, 2026, the UK hosted military planners from over 30 countries at the UK's Permanent Joint Headquarters in Northwood for two days of talks to begin turning "diplomatic consensus into a detailed military plan" ([UK and France to lead multinational Strait of Hormuz military ...](https://www.gov.uk/government/news/uk-and-france-to-lead-multinational-strait-of-hormuz-military-planning-conference)). Over a dozen countries offered to contribute to the mission (https://www.reuters.com/world/europe/countries-discuss-hormuz-mission-when-conflict-ends-2026-04-17/).

As of May 1, 2026, the mission remains in the planning and coordination phase and has not commenced operations ([A naval coalition in the Strait of Hormuz should learn these lessons](https://www.chathamhouse.org/2026/05/naval-coalition-strait-hormuz-should-learn-these-lessons)). The joint statement specifies that the mission will conduct operations "as soon as conditions permit following a sustainable ceasefire agreement" ([Joint Statement by President Macron and Prime Minister Starmer ...](https://www.elysee.fr/en/emmanuel-macron/2026/04/17/joint-statement-by-president-macron-and-prime-minister-starmer-co-chairs-of-the-international-summit-on-the-strait-of-hormuz)). Additionally, the United States is reportedly seeking to establish a separate maritime coalition, adding complexity to the operational landscape ([A naval coalition in the Strait of Hormuz should learn these lessons](https://www.chathamhouse.org/2026/05/naval-coalition-strait-hormuz-should-learn-these-lessons)).

Key sources:
- April 17 summit joint statement: https://www.elysee.fr/en/emmanuel-macron/2026/04/17/joint-statement-by-president-macron-and-prime-minister-starmer-co-chairs-of-the-international-summit-on-the-strait-of-hormuz
- UK MoD planning conference announcement: https://www.gov.uk/government/news/uk-and-france-to-lead-multinational-strait-of-hormuz-military-planning-conference
- Chatham House analysis (May 2026): https://www.chathamhouse.org/2026/05/naval-coalition-strait-hormuz-should-learn-these-lessons

**Exact later resolution packet**

The question resolves NO. The UK-France led multinational mission to protect shipping in the Strait of Hormuz did NOT formally begin operations between May 1, 2026 and 23:59 UTC June 1, 2026. None of the three triggering events (IOC declaration, first escort/patrol, or first mine clearance) occurred under the banner of this specific mission within the resolution window.

Key evidence:
- The mission's own joint statement made operations conditional on "a sustainable ceasefire agreement." A UK MoD/GOV.UK joint statement of 12 May 2026 explicitly stated that the 38-nation group was announcing only "political support for the Mission" in "readiness for operations commencing when the environment is permissive," and that "Operations will only commence in a permissive environment." This confirms the mission was still in a pre-operational, political-support phase as of mid-May [Joint statement on the Multinational Military Mission for the Strait of ...](https://www.gov.uk/government/news/joint-statement-on-the-multinational-military-mission-for-the-strait-of-hormuz-12-may-2026).
- Breaking Defense (15 May 2026) confirmed the initiative "would only begin once a ceasefire has been declared" and was still in a planning/preparation phase, with no IOC declaration and no escort, patrol, or mine clearance conducted [From destroyers to drones, how a Europe-led coalition aims to open ...](https://breakingdefense.com/2026/05/from-destroyers-to-drones-how-a-europe-led-coalition-aims-to-open-the-strait-of-hormuz/).
- Wikipedia's "2026 Strait of Hormuz crisis" article (updated 27 May 2026) listed no operational commencement for the UK-France mission, with the last logged event being a vessel seizure on 14 May 2026; the strait remained contested [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis).
- Reuters (27 May 2026) reported that the US-Iran ceasefire/reopening deal was still only an "unofficial framework," "not yet finalised," and rejected by the White House — so the antecedent condition (a sustainable ceasefire) had not been met, meaning the mission's own precondition for starting operations was unfulfilled [Iran state TV says draft deal with US would reopen Hormuz shipping ...](https://www.reuters.com/world/middle-east/iran-says-draft-us-deal-would-reopen-hormuz-shipping-end-naval-blockade-2026-05-27/).
- ISW Iran Update (29 May 2026) described ongoing active conflict in the strait with US Navy operations (separate from the UK-France mission) and no sustainable ceasefire; no UK-France mission commencement was reported [Iran Update Special Report, May 29, 2026](https://understandingwar.org/research/middle-east/iran-update-special-report-may-29-2026/).

Distinction from the separate US-led mission: The US launched "Operation Project Freedom" (a US Navy escort mission) on 4 May 2026, but Trump paused it within a day (5 May 2026). This is a separate US-led effort, NOT the UK-France led multinational mission that this question tracks, so it does not count toward resolution.

Since no qualifying operational event occurred under the UK-France led mission's authority within the window, and confirmation comes from the specified sources (UK MoD/GOV.UK, Reuters), the question resolves NO.

Note on conditional structure: The question is not framed as a Metaculus conditional pair; it is a straightforward binary on whether operations began by the deadline. The "as soon as conditions permit following a sustainable ceasefire agreement" clause is part of the mission's mandate, and the absence of a finalized ceasefire is precisely why operations had not commenced — supporting a NO (0) resolution rather than annulment.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-227. `ae5f2f5c-a322-5b79-b138-b23b3fd27f81`

- Present date: `2026-05-03 00:35:49.701176`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Minnesota's legislature pass and the Governor sign a bill lifting the state's moratorium on new nuclear power plant construction by June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 1, 2026 and by 11:59 PM Central Time (UTC-5) on June 1, 2026, a bill amending or repealing Minnesota Statutes § 216B.243, subdivision 3b, such that the prohibition on issuing a certificate of need for new nuclear-powered electric generating plants is removed, is passed by both the Minnesota House of Representatives and the Minnesota Senate and signed by the Governor of Minnesota (or becomes law without the Governor's signature per Minnesota constitutional procedures).

This question resolves NO if:
- No such bill is signed into law by the deadline, OR
- The legislature only passes a bill funding a study on nuclear energy without actually repealing or amending the prohibition in § 216B.243, subd. 3b, OR
- A bill passes the legislature but is vetoed by the Governor.

"Passing" requires the Governor's signature (or the bill becoming law without signature); a legislative vote alone is not sufficient.

Resolution source: The official Minnesota State Legislature website at https://www.revisor.mn.gov/bills/ and the Office of the Governor of Minnesota.

**Pre-cutoff background**

Minnesota has maintained a statutory moratorium on new nuclear power plant construction since 1994, codified in Minn. Stat. § 216B.243, subd. 3b. This provision prohibits the Minnesota Public Utilities Commission from issuing a certificate of need for the construction of a new nuclear-powered electric generating plant [Legislation lifting state's nuclear moratorium clears House ...](https://www.house.mn.gov/sessiondaily/Story/18602).

In the 2025 session, HF2002 cleared the House Energy Finance and Policy Committee in March 2025 and was sent to the House floor [Legislation lifting state's nuclear moratorium clears House ...](https://www.house.mn.gov/sessiondaily/Story/18602). In the 2026 session, multiple bills have been introduced, including HF4023 (Baker) / SF1924, which would repeal the nuclear moratorium. A Senate amendment (sch2442a17) to HF2442 that would have modified the moratorium with restrictions near the Prairie Island Community reservation was voted down [sch2442a17](https://www.senate.mn/chamber/amendment/sch2442a17.html).

As of April 2026, both the House and Senate are considering bills related to nuclear energy, but the primary legislative focus appears to be on funding a study on the pros and cons of nuclear energy, which lawmakers view as a necessary precursor to lifting the moratorium [Minnesota inches closer to lifting nuclear energy ban - FOX 9](https://www.fox9.com/news/minnesota-inches-closer-lifting-nuclear-energy-ban-april-2026). The legislature has not yet passed a bill to fully lift the moratorium through either chamber. Several other states, including New Jersey (April 2026) and Illinois, have recently lifted their own nuclear moratoria, creating political momentum but not certainty for Minnesota.

The Minnesota Legislature's 2026 session typically runs through mid-to-late May. Resolution source: official Minnesota Legislature bill tracker at https://www.revisor.mn.gov/bills/ and https://www.house.mn.gov/sessiondaily/.

**Exact later resolution packet**

The question resolves NO. The resolution criteria require that, on or after May 1, 2026 and by 11:59 PM CT on June 1, 2026, a bill amending or repealing Minn. Stat. § 216B.243, subd. 3b (removing the prohibition on issuing a certificate of need for new nuclear plants) be passed by both chambers AND signed by the Governor. The criteria also explicitly state the question resolves NO if "the legislature only passes a bill funding a study on nuclear energy without actually repealing or amending the prohibition."

The Minnesota Center for Environmental Advocacy (MCEA) 2026 Legislative Recap (published 2026-05-28) confirms that the 2026 legislative session ended on May 18, 2026, and that the legislature passed a tax bill which included "funding for a study on lifting Minnesota's nuclear moratorium," while noting that "current law prohibits the construction of new nuclear power plants in the state" [61dabd]. No bill repealing or amending § 216B.243, subd. 3b was enacted. This precisely matches the explicit NO condition (study funded, moratorium not lifted).

Because the session concluded on May 18, 2026 — before the June 1, 2026 deadline — with only a study funded and the moratorium left intact, the moratorium was not lifted within the resolution window. The question therefore resolves NO (0) [61dabd, 12ec3d].

Source URL: https://www.mncenter.org/mceas-2026-legislative-recap

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-228. `fef0e6d3-f326-523d-83f2-84e7dbc167d0`

- Present date: `2026-04-30 14:07:30.359804`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Elliott Investment Management file a new Schedule 13D with the SEC targeting a company not previously publicly known as an Elliott activist target, between April 29 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between 00:00 UTC on April 29, 2026 and 23:59 UTC on June 1, 2026, Elliott Investment Management L.P. (SEC CIK: 0001791786) files a new Schedule 13D with the U.S. Securities and Exchange Commission naming a company that was **not previously publicly known** as an Elliott activist target.

**Definition of "activist campaign":** The filing of an initial Schedule 13D (not a 13D/A amendment to an existing filing) with the SEC by Elliott Investment Management L.P., indicating beneficial ownership of more than 5% of a class of equity securities with the purpose of influencing or changing control of the issuer. A 13D/A amendment to an existing position in a previously known target does NOT count.

**Definition of "not previously publicly known":** The target company must not appear in any of the following as an Elliott activist target prior to 00:00 UTC April 29, 2026:
1. Any Schedule 13D filing by Elliott Investment Management L.P. (CIK 0001791786) on SEC EDGAR (https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001791786&type=SC%2013D&dateb=&owner=include&count=100)
2. Reporting by major financial news outlets (Reuters, Bloomberg, Financial Times, Wall Street Journal) identifying the company as an Elliott activist target

**Resolution source:** SEC EDGAR filings page for Elliott Investment Management L.P.: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001791786&type=SC%2013D&dateb=&owner=include&count=40 — supplemented by https://www.secform4.com/13dg-history/1791786.html and credible financial news reporting from Reuters, Bloomberg, FT, or WSJ.

If no qualifying new 13D filing appears by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

Elliott Investment Management L.P., founded by Paul Singer, is one of the world's most prolific activist hedge funds. In 2025, Elliott launched 18 new campaigns and deployed nearly $20 billion in capital, topping the activist league tables [Activist Elliott's recent holdings and campaigns - Reuters](https://www.reuters.com/business/activist-elliotts-recent-holdings-campaigns-2026-02-11/). The firm has been active across multiple sectors and geographies.

As of April 2026, Elliott's major publicly known activist targets include [Activist Elliott's recent holdings and campaigns - Reuters](https://www.reuters.com/business/activist-elliotts-recent-holdings-campaigns-2026-02-11/) [Elliott Investment Management L.P. - 13D/13G Filings](https://www.secform4.com/13dg-history/1791786.html):

- **Phillips 66** (energy; investment disclosed November 2023; seeking board overhaul)
- **Southwest Airlines** (travel; investment disclosed June 2024; ongoing 13D filings through April 2026)
- **Starbucks** (consumer; investment disclosed July 2024)
- **Honeywell** (industrials; investment disclosed November 2024; resulted in break-up)
- **BP** (energy; investment disclosed April 2025)
- **Smiths Group** (industrials; investment reported February 2025)
- **Aspen Technology** (technology; investment disclosed February 2025)
- **E2open Parent Holdings** (technology; 13D filed May 2025)
- **Uniti Group** (telecom infrastructure; 13D filed August 2025)
- **PepsiCo** (consumer staples; investment disclosed September 2025)
- **Etsy** (e-commerce; 13D filed November 2025)
- **Toyota Industries** (industrials; investment disclosed November 2025)
- **Seadrill 2021 Ltd** (energy; 13D filed December 2025)
- **Triple Flag Precious Metals** (mining; 13D filed December 2025)
- **London Stock Exchange Group** (financial infrastructure; investment reported February 2026)

Elliott's 13D filing history can be tracked via SEC EDGAR at: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001791786&type=SC%2013D&dateb=&owner=include&count=40 and via https://www.secform4.com/13dg-history/1791786.html

Given Elliott's pace of approximately 18 campaigns in 2025 (roughly 1.5 per month), there is meaningful but not certain probability of a new target emerging in a ~33-day window.

**Exact later resolution packet**

The question resolves NO. The resolution source is Elliott Investment Management's SEC EDGAR filing record (CIK 0001791786). Multiple independent checks confirm that Elliott did NOT file any initial Schedule 13D (form type exactly "SC 13D", as opposed to "SC 13D/A" amendments) between 00:00 UTC April 29, 2026 and 23:59 UTC June 1, 2026.

Evidence:
- Repeated SEC EDGAR full-text search queries for CIK 0001791786 / "Elliott Investment Management" with form type "SC 13D" and date range 2026-04-29 to 2026-06-01 returned zero hits [https://efts.sec.gov/LATEST/search-index?q=%22Elliott+Investment+Management%22&forms=SC%2013D&startdt=2026-04-29&enddt=2026-06-01](https://efts.sec.gov/LATEST/search-index?q=%22Elliott+Investment+Management%22&forms=SC%2013D&startdt=2026-04-29&enddt=2026-06-01) [https://efts.sec.gov/LATEST/search-index?q=&forms=SC 13D&startdt=2026-04-29&enddt=2026-06-01&ciks=0001791786](https://efts.sec.gov/LATEST/search-index?q=&forms=SC 13D&startdt=2026-04-29&enddt=2026-06-01&ciks=0001791786) [https://efts.sec.gov/LATEST/search-index?q=%22Elliott+Investment+Management%22&forms=SC+13D&startdt=2026-04-29&enddt=2026-06-01&hits=10](https://efts.sec.gov/LATEST/search-index?q=%22Elliott+Investment+Management%22&forms=SC+13D&startdt=2026-04-29&enddt=2026-06-01&hits=10) [https://efts.sec.gov/LATEST/search-index?q=Elliott&forms=SC 13D&startdt=2026-04-29&enddt=2026-06-01](https://efts.sec.gov/LATEST/search-index?q=Elliott&forms=SC 13D&startdt=2026-04-29&enddt=2026-06-01) [https://efts.sec.gov/LATEST/search-index?q=%22Elliott+Investment+Management%22&forms=SC+13D&dateRange=custom&startdt=2026-04-29&enddt=2026-06-01](https://efts.sec.gov/LATEST/search-index?q=%22Elliott+Investment+Management%22&forms=SC+13D&dateRange=custom&startdt=2026-04-29&enddt=2026-06-01).
- The EDGAR submissions JSON for CIK 0001791786 (data.sec.gov) lists the most recent Elliott filings as a 13F-HR (May 15, 2026), several SCHEDULE 13D/A amendments, and a Form 144 — but NO initial "SC 13D" filing [https://data.sec.gov/submissions/CIK0001791786.json](https://data.sec.gov/submissions/CIK0001791786.json) [https://data.sec.gov/submissions/CIK0001791786.json](https://data.sec.gov/submissions/CIK0001791786.json).
- Elliott's most recent 13D-family filings prior to/around the window were amendments to existing positions: SC 13D/A on Southwest Airlines (April 3, 2026) and SC 13D/A on Triple Flag (March 31, 2026) — both amendments to previously known targets, and the Southwest one predates the window anyway [Elliott Investment Management L.P. - 13D/13G Filings](https://www.secform4.com/13dg-history/1791786.html) [Elliott Investment Management L.P. SEC Filings - CapEdge](https://capedge.com/company/1791786/filings).

Regarding potential new targets reported in the window: Elliott was reported to have taken stakes in DexCom (settlement/board agreement announced May 14, 2026) and Bio-Rad Laboratories (stake reported by WSJ/Reuters May 17-18, 2026). However, neither was confirmed via an initial Schedule 13D filing by Elliott. The Bloomberg article on DexCom did not state any 13D was filed, nor confirm a >5% stake [Elliott Takes Dexcom Stake in Bet on Glucose Monitors Market](https://www.bloomberg.com/news/articles/2026-05-14/elliott-takes-stake-in-dexcom-in-bet-on-glucose-monitors-market). The DexCom company EDGAR record showed no Elliott Schedule 13D, and Bio-Rad's EDGAR 13D history showed no Elliott 13D filing (its most recent 13D/A was from 2022) [https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000012208&type=SC+13D&dateb=&owner=include&count=40](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000012208&type=SC+13D&dateb=&owner=include&count=40). Elliott commonly engages via cooperation/settlement agreements and cash-settled swaps without crossing the 5% beneficial-ownership threshold that triggers a Schedule 13D, consistent with the absence of any such filing.

Because no qualifying initial Schedule 13D (indicating >5% beneficial ownership with intent to influence/control) by CIK 0001791786 appeared in the resolution window, the question resolves NO per its stated criteria ("If no qualifying new 13D filing appears by 23:59 UTC on June 1, 2026, the question resolves No").

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-229. `3d1b8e87-15cd-5e62-9a2b-4d3269cc69fc`

- Present date: `2026-05-12 16:56:41.184582`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the US administration officially announce an extension or postponement of the July 4, 2026, EU trade deal deadline before July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 10, 2026, and before 11:59 PM UTC on June 30, 2026, the US administration officially announces an extension or postponement of the July 4, 2026, deadline for the EU to implement or ratify the US-EU trade deal.

**Definitions:**
- **"US administration"**: The President of the United States, the White House (via whitehouse.gov or official White House social media accounts), or the Office of the United States Trade Representative (USTR, via ustr.gov or official USTR statements).
- **"Officially announce"**: A public statement, executive order, press release, social media post from an official account (including the President's Truth Social or X account), or on-the-record briefing that explicitly states the July 4 deadline is being moved to a later date, suspended, or otherwise delayed.
- **"Extension or postponement"**: Any explicit communication that the July 4, 2026, deadline for the EU to comply with, implement, or ratify the trade deal is being pushed to a later date or indefinitely suspended. Implicit signals (e.g., simply not enforcing tariffs on July 5) do NOT count — the announcement must explicitly reference moving or suspending the deadline.

This question resolves as **No** if no such official announcement is made by 11:59 PM UTC on June 30, 2026. This includes the scenario where the deadline passes without comment, or where tariffs are imposed on July 4 as threatened.

**Resolution sources**: Official statements published at [whitehouse.gov](https://www.whitehouse.gov/briefing-room/), [ustr.gov](https://ustr.gov/about-us/press-office), or credible major news reporting from Reuters (reuters.com), AP News (apnews.com), or Bloomberg (bloomberg.com) confirming such an announcement.

**Pre-cutoff background**

On May 7, 2026, President Donald Trump set a July 4, 2026, deadline for the European Union to implement the trade framework reached last year. Under this framework, the US would levy a 15% tariff on most EU goods. Trump warned that if the EU does not "deliver their side of the Deal" by July 4, tariffs would increase significantly, with a 25% tariff on EU autos specifically threatened [Trump says EU has until July 4 to approve trade deal | AP News](https://apnews.com/article/trump-tariffs-eu-trade-deal-bd6748c3e85533d3ce3644f257f8e326).

This July 4 deadline itself was an extension of a previous threat made on May 1, 2026, when Trump said EU autos would face a 25% tariff "this week" [Trump says EU has until July 4 to approve trade deal | AP News](https://apnews.com/article/trump-tariffs-eu-trade-deal-bd6748c3e85533d3ce3644f257f8e326). The pattern of setting deadlines and then extending them is a recurring feature of Trump's trade negotiation strategy. The current 10% tariff on EU goods is being levied while the administration investigates trade imbalances, following a US Supreme Court ruling that limited the administration's authority to impose tariffs based on economic emergency declarations [Trump says EU has until July 4 to approve trade deal | AP News](https://apnews.com/article/trump-tariffs-eu-trade-deal-bd6748c3e85533d3ce3644f257f8e326).

The EU Parliament has approved the trade deal with safeguards, but full implementation by all EU institutions by July 4 remains uncertain. Some EU officials have expressed confidence the deadline will be met, while others view the timeline as challenging given the complexity of ratification across EU member states.

As of May 11, 2026, no extension has been announced, and the July 4 deadline remains in effect.

**Exact later resolution packet**

The question resolves **NO (0)**.

**What the question required for YES:** An official announcement by the US administration (President Trump, the White House, or the USTR), made between May 10, 2026 and 11:59 PM UTC June 30, 2026, that explicitly moved, suspended, or delayed the July 4, 2026 deadline for the EU to implement/ratify the US-EU trade deal.

**What actually happened:** Rather than the US extending the deadline, the EU raced to meet it. On June 16, 2026 the European Parliament approved the deal, and on Thursday June 25, 2026 EU governments (the Council) adopted the implementing legislation fulfilling the EU's side of the deal, allowing it to enter into force ahead of the July 4 deadline. The Reuters report "EU governments adopt legislation to fulfil EU side of US trade deal" (June 25, 2026) states the EU was on track to meet the deadline and contains no mention of any US announcement extending or postponing it [708a58]. Le Monde's June 25, 2026 report "EU-US trade deal to take effect before Trump's deadline" likewise states EU states gave final approval "allowing it to enter into force ahead of a July 4 deadline set by President Donald Trump," with no US extension announcement [3447bd].

**Rule-out of a YES trigger:** Extensive searching of the approved sources (whitehouse.gov, ustr.gov, Reuters, AP, Bloomberg) turned up no statement from Trump, the White House, or USTR moving/suspending the July 4 deadline during the resolution window. The relevant Greenland-related EU freeze occurred in January–February 2026 (before the window and before the July 4 deadline was even set on May 7, 2026) and was resolved when the EU Parliament lifted the freeze; it did not involve a US announcement extending the July 4 deadline [2532bc]. A separate late-June AP story about Trump threatening a 100% tax on countries imposing digital-services taxes is a distinct/new threat, not an extension of the July 4 EU trade-deal deadline.

Because no qualifying official US announcement of an extension or postponement was made by 11:59 PM UTC June 30, 2026 — and instead the deadline was met by the EU — the resolution is NO.

Key source URLs:
- Reuters, "EU governments adopt legislation to fulfil EU side of US trade deal" (2026-06-25): https://www.reuters.com/business/eu-governments-adopt-legislation-fulfil-eu-side-us-trade-deal-2026-06-25/
- Le Monde, "EU-US trade deal to take effect before Trump's deadline" (2026-06-25): https://www.lemonde.fr/en/economy/article/2026/06/25/eu-us-trade-deal-to-take-effect-before-trump-s-deadline_6754857_19.html
- Bloomberg, "EU Lawmakers Approve US Trade Deal Ahead of Trump Deadline" (2026-06-16): https://www.bloomberg.com/news/articles/2026-06-16/eu-lawmakers-approve-us-trade-deal-ahead-of-trump-deadline
- Reuters, "Trump sets July 4 deadline for EU to comply with trade deal" (2026-05-07): https://www.reuters.com/world/trump-says-giving-eu-until-july-4-fulfill-trade-deal-or-will-raise-tariffs-2026-05-07/

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-230. `4c4a8791-6c72-5ad1-b8c0-1c73e2b39280`

- Present date: `2026-05-14 09:39:27.617759`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Brussels Airport (BRU) experience at least two separate days of significant flight cancellations (>30% of scheduled flights cancelled) due to strike action on or after May 12, 2026, through June 30, 2026?

**Resolution criteria**

This question resolves as **YES** if, on or after May 12, 2026, through June 30, 2026 (23:59 CEST, UTC+2), there are at least **two separate calendar days** (defined as 00:00–23:59 CEST) on which Brussels Airport (BRU) experiences significant flight cancellations due to strike action.

**Definitions:**

- **Strike action**: Any form of organized industrial action — including strikes, walkouts, or work stoppages — by labor unions or employee groups, as defined by the ILO (https://www.ilo.org/global/statistics-and-databases/statistics-overview-and-topics/strikes-and-lockouts/lang--en/index.htm) or consistent with the Wikipedia definition (https://en.wikipedia.org/wiki/Strike_action). The strike must be explicitly cited as the primary cause of the cancellations.

- **Cancellation**: A scheduled commercial passenger flight that does not operate, consistent with the EU definition under Regulation (EC) No 261/2004 (https://en.wikipedia.org/wiki/Flight_Cancellation_and_Delay). Diversions, delays, and cargo-only flights are excluded.

- **>30% of scheduled flights**: The numerator is the number of cancelled commercial passenger flights (departures and arrivals combined) at BRU on that calendar day. The denominator is the total number of scheduled commercial passenger flights (departures and arrivals combined) at BRU on that calendar day as published by Brussels Airport or as recorded by Flightradar24.

**Resolution source**: The outcome will be determined primarily by official press releases or operational notices published at https://www.brusselsairport.be/en/pressroom (persistent URL for Brussels Airport press releases). If the airport publishes specific cancellation percentages or counts, those figures will be used. In the absence of official airport data, consistent reporting from at least two major international news outlets (e.g., Reuters at https://www.reuters.com/, AP at https://apnews.com/, Euronews at https://www.euronews.com/, or BBC at https://www.bbc.com/) confirming that >30% of flights were cancelled due to strike action on the relevant days will suffice.

If fewer than two such days occur on or after May 12, 2026, through June 30, 2026 (CEST), the question resolves **NO**.

**Pre-cutoff background**

Brussels Airport (BRU) is Belgium's largest international airport, handling approximately 650 flights per day and around 198,000 flight movements in 2025. The airport has been repeatedly disrupted by industrial action in 2026:

- **March 12, 2026**: A national strike caused a full cancellation of all departures and significant arrival disruptions [https://striketracker.app/strikes-in-belgium](https://striketracker.app/strikes-in-belgium).
- **May 12, 2026**: A national day of action led Brussels Airport to instruct airlines to cancel more than half of the roughly 650 scheduled flights, affecting approximately 60,000 passengers.
- **CGSP police strike notice**: The socialist CGSP police union filed a strike notice covering the period from May 12, 2026, through June 30, 2026 [https://striketracker.app/strikes-in-belgium](https://striketracker.app/strikes-in-belgium). While a police strike notice does not directly ground flights, it signals broader labor unrest and can compound with other union actions to disrupt airport security and operations.

In 2025, approximately 2,400 flights were cancelled at Brussels Airport due to strikes, costing businesses an estimated €175 million. Belgium's labor movement has a strong tradition of general strikes and sectoral actions, and the current political climate around austerity measures and aviation taxes has heightened tensions between unions and government. The question is whether these conditions will produce at least two more days of severe disruption (>30% cancellations) in the remaining weeks through June 30, 2026.

Key data source: Brussels Airport publishes monthly traffic figures at https://www.brusselsairport.be/en/our-airport/facts-figures/monthly-traffic-figures [Monthly air traffic figures - Brussels Airport](https://www.brusselsairport.be/en/our-airport/facts-figures/monthly-traffic-figures), and operational disruption notices are posted on the main site at https://www.brusselsairport.be/ [https://striketracker.app/strikes-in-belgium](https://striketracker.app/strikes-in-belgium). Flightradar24 also tracks daily scheduled flights at https://www.flightradar24.com/data/airports/bru/statistics [Brussels Airport (BRU/EBBR) | Arrivals, Departures & Routes](https://www.flightradar24.com/data/airports/bru/statistics).

**Exact later resolution packet**

Adjudicated: Within the May 12-June 30, 2026 window only ONE day clearly saw >30% of BRU's scheduled passenger flights cancelled by strike action: May 12, 2026 (national day of action; 'just over half of departing passenger flights' cancelled, ~50% overall). The only other 2026 strike day, June 2 (skeyes ATC wildcat), is sub-30% under the criteria's strict source hierarchy: the most precise cancellation count (AirHelp: 186-187 cancellations vs delays) is ~28.6% of the ~650 daily flights (AirHelp https://www.airhelp.com/en-int/flight-disruptions/skeyes-atc-strike-disrupts-6793-flights-europe-03062026/; VRT reported ~140 cancellations, ~21.5%), and only the imprecise 'around 200' figure reaches ~30.8%. No Brussels Airport press release published a specific >30% figure for June 2, and no two designated outlets (Reuters/AP/Euronews/BBC) confirmed >30% (Reuters reported the airspace-halt window without a percentage). The heavily documented 'June 25 / no departing flights / 103 incoming' material is the June 25, 2025 event (Euronews 2025/06/26); striketracker's 2026 Belgium list shows only March 12, May 12, and June 2 - no June 25, 2026 strike. With fewer than two qualifying days, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-231. `7b27fdcb-e65f-5231-8a86-b47af6893820`

- Present date: `2026-05-01 16:15:00.221107`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will OPM announce the revision of at least one additional federal job series (beyond the 2210 IT Management series) to competency-based standards between April 30, 2026 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 and no later than 11:59 PM ET on June 1, 2026, the U.S. Office of Personnel Management publishes an official announcement—such as a news release on the OPM newsroom (https://www.opm.gov/news/news-releases/), a CHCO memorandum on the OPM CHCO memos page (https://www.opm.gov/chcoc/latest-memos/), or an official OPM blog post—stating that at least one federal job series other than the 2210 IT Management series has been revised to "competency-based standards."

"Competency-based standards" means qualification and/or classification standards that replace or eliminate traditional educational degree requirements in favor of demonstrated competencies, skills, or work experience as the primary basis for determining candidate qualifications, consistent with the framework applied to the 2210 series revision announced on April 13–21, 2026 [https://federalnewsnetwork.com/hiring-retention/2026/04/trump-administration-tosses-degree-requirements-for-federal-it-managers/](https://federalnewsnetwork.com/hiring-retention/2026/04/trump-administration-tosses-degree-requirements-for-federal-it-managers/).

A "federal job series" is defined as a subdivision within the federal occupational classification system, identified by a four-digit number, as described in the OPM Handbook of Occupational Groups and Families (https://www.opm.gov/policy-data-oversight/classification-qualifications/classifying-general-schedule-positions/occupationalhandbook.pdf).

The question resolves **No** if no such announcement appears by the deadline. Announcements of intent, proposed rules, or draft standards do not count; the announcement must indicate that a revised standard has been issued or finalized.

**Pre-cutoff background**

On April 13, 2026, the U.S. Office of Personnel Management (OPM) issued memoranda announcing the competency-based position classification and qualification standard for the Information Technology Management Series, 2210 [[PDF] Modernization and Consolidation of Occupational Series - OPM](https://www.opm.gov/chcoc/latest-memos/modernization-and-consolidation-of-occupational-series.pdf). This revision, part of OPM Director Scott Kupor's "federal workforce competency initiative," removes traditional educational degree requirements in favor of skills- and competency-based assessments [https://federalnewsnetwork.com/hiring-retention/2026/04/trump-administration-tosses-degree-requirements-for-federal-it-managers/](https://federalnewsnetwork.com/hiring-retention/2026/04/trump-administration-tosses-degree-requirements-for-federal-it-managers/). On April 24, 2026, OPM issued a separate memorandum on "Modernization and Consolidation of Occupational Series," initiating "Phase One" focused on consolidating 115 low-utilization and obsolete occupational series, with updated classification and qualification standards to be issued from April 2026 through September 2027. The memorandum states that "future phases will address broader structural redesign aligned to skills-based workforce frameworks" [[PDF] Modernization and Consolidation of Occupational Series - OPM](https://www.opm.gov/chcoc/latest-memos/modernization-and-consolidation-of-occupational-series.pdf). As of May 1, 2026, the 2210 IT Management series is the only series that has been formally revised to competency-based standards under this initiative. OPM has stated its intention to eventually revise all 604 federal job series but has not published a specific timeline for the next series [https://federalnewsnetwork.com/hiring-retention/2026/04/trump-administration-tosses-degree-requirements-for-federal-it-managers/](https://federalnewsnetwork.com/hiring-retention/2026/04/trump-administration-tosses-degree-requirements-for-federal-it-managers/).

A "federal job series" refers to a group of positions sufficiently similar in specialized line of work and qualification requirements to warrant similar treatment in personnel processes, as defined in the OPM Handbook of Occupational Groups and Families (https://www.opm.gov/policy-data-oversight/classification-qualifications/classifying-general-schedule-positions/occupationalhandbook.pdf).

**Exact later resolution packet**

The question resolves NO. It requires an official OPM announcement (news release, CHCO memorandum, or official OPM blog post) published between April 30, 2026 and 11:59 PM ET June 1, 2026, stating that at least one federal job series other than the 2210 IT Management series has been revised to "competency-based standards" (i.e., a standard issued/finalized that replaces or eliminates degree requirements). Announcements of intent, proposed rules, or drafts do not count.

Evidence:
- The OPM CHCO "Latest Memos" page shows no competency-based standard memorandum for any series other than 2210 within the window; the only memos near the window are "Federal Workforce Competency Initiative Survey" (April 27, 2026) and "Exclusion of Schedule C and G General Schedule Positions...Performance Appraisal" (April 28, 2026), both before the April 30 start and neither announcing a revised standard [7b3b0f].
- The OPM CHCO "Published Memos" page confirms the same: the only entries dated in the relevant period are the April 27 survey memo and the April 28 performance-appraisal memo — neither of which finalizes a competency-based standard for a new series [e72528].
- The OPM News Releases page contains releases in the window (e.g., May 4 USA Class AI tool, May 4 Public Service Recognition Week, May 26 NDA, May 27 Time-in-Grade proposal) but none announcing a job series revised to competency-based standards [e9a6cc].
- Federal News Network's hiring/workforce coverage through May–June 2026 (e.g., FEVS relaunch, AI position-description tool, national security pay) likewise shows no new competency-based standard issued for a series beyond 2210 [fd36b8].

The only competency-based standard formally issued under this initiative remained the 2210 IT Management series (April 13, 2026), which is before the window and explicitly excluded. The April 24, 2026 "Modernization and Consolidation of Occupational Series" memo describes future phases and a timeline (April 2026–September 2027) but is an announcement of intent, not the issuance of a finalized competency-based standard for a specific additional series. Therefore no qualifying announcement appeared by the deadline, and the question resolves NO.

Key URLs: https://www.opm.gov/chcoc/latest-memos/ ; https://www.opm.gov/chcoc/published-memos/ ; https://www.opm.gov/news/news-releases/ ; https://federalnewsnetwork.com/category/hiring-retention/

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-232. `e1de807c-4756-5004-806e-2e3906b3b239`

- Present date: `2026-05-12 21:56:04.048407`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the ECB's June 2026 monetary policy statement explicitly signal that a further rate increase is likely at the July 2026 meeting?

**Resolution criteria**

This question resolves YES if the official ECB "Monetary policy decisions" press release published following the June 11, 2026 Governing Council meeting contains language that explicitly signals a further rate increase is likely at the July 23, 2026 meeting. 

Specifically, it resolves YES if the statement includes any of the following phrases or close equivalents: "further increases in interest rates will be appropriate," "the Governing Council expects to raise interest rates further," "rates will need to rise further," "a further increase is likely," or "the Governing Council intends to raise rates at its next meeting."

It resolves NO if:
- The statement uses only hedged or conditional language such as "data-dependent," "meeting-by-meeting approach," "not pre-committing to a particular rate path," "may need to adjust," "stands ready to adjust," or similar non-committal phrasing; OR
- The statement does not address the future rate path; OR
- No rate decision is announced on June 11, 2026.

The resolution source is the official ECB monetary policy decisions press release, published at: https://www.ecb.europa.eu/press/pr/date/2026/html/index.en.html

The press conference transcript (available at https://www.ecb.europa.eu/press/pressconf/html/index.en.html) is NOT considered for resolution—only the official written monetary policy statement counts.

**Pre-cutoff background**

As of May 11, 2026, the European Central Bank's three key interest rates stand at: deposit facility rate 2.00%, main refinancing operations rate 2.15%, and marginal lending facility rate 2.40% [Monetary policy decisions - European Central Bank](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260430~81b7179e6f.en.html). These rates have been held unchanged through several consecutive meetings in 2026 (February, March, and April).

However, inflationary pressures in the euro area have risen sharply. Inflation jumped from 1.9% in February to 2.6% in March (later revised to 2.6%) and then to 3.0% in April 2026, driven significantly by surging energy prices linked to the Iran/Strait of Hormuz conflict. This represents a sustained overshoot of the ECB's 2% target.

In its April 30, 2026 statement, the ECB Governing Council emphasized a "data-dependent and meeting-by-meeting approach" and stated it is "not pre-committing to a particular rate path" [Monetary policy decisions - European Central Bank](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260430~81b7179e6f.en.html). However, Reuters reported on April 30, 2026 that ECB policymakers "see first of several rate hikes in June," suggesting internal consensus is building toward tightening. The IMF's European Department chief Alfred Kammer stated the ECB should raise rates by about 50 basis points in 2026 to maintain a neutral stance [IMF expects ECB to raise rates by half a percentage point in 2026](https://www.reuters.com/business/imf-expects-ecb-raise-rates-by-half-percentage-point-2026-2026-04-17/). Market pricing as of late April/early May reflects expectations of at least 50 basis points of hikes by year-end, with a June hike widely anticipated. JP Morgan has forecast 25 basis point hikes in both June and September 2026.

The next ECB monetary policy decision is scheduled for June 11, 2026 (note: not June 4 as sometimes cited), with the subsequent meeting on July 23, 2026. The key question is whether, beyond potentially hiking rates in June, the ECB will use its statement to explicitly signal continuation of tightening at the July meeting—a significant departure from its current meeting-by-meeting, non-committal communication approach.

**Exact later resolution packet**

The question resolves NO.

RESOLUTION SOURCE: The official ECB "Monetary policy decisions" press release published following the June 11, 2026 Governing Council meeting, located at https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260611~4d41bd5e83.en.html [Monetary policy decisions - European Central Bank](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260611~4d41bd5e83.en.html). This is the exact resolution source specified in the question (the "Monetary policy decisions" press release, NOT the press conference transcript/statement or Q&A).

ANTECEDENT / RATE DECISION CHECK: A rate decision WAS announced on June 11, 2026. The Governing Council decided to raise the three key ECB interest rates by 25 basis points, bringing the deposit facility, main refinancing operations, and marginal lending facility rates to 2.25%, 2.40%, and 2.65% respectively, effective 17 June 2026 [Monetary policy decisions - European Central Bank](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260611~4d41bd5e83.en.html). So the "No rate decision is announced" NO-condition does NOT apply — the question does not fail on that ground.

KEY TEST (forward guidance language): The written statement does NOT contain any of the YES-triggering phrases ("further increases in interest rates will be appropriate," "the Governing Council expects to raise interest rates further," "rates will need to rise further," "a further increase is likely," "the Governing Council intends to raise rates at its next meeting") or close equivalents. Instead, it uses precisely the hedged/conditional language that the resolution criteria specify as NO conditions. The statement reads: "It will closely monitor the situation and follow a data-dependent and meeting-by-meeting approach to determining the appropriate monetary policy stance... The Governing Council is not pre-committing to a particular rate path" [Monetary policy decisions - European Central Bank](https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260611~4d41bd5e83.en.html).

Because the June 11, 2026 written "Monetary policy decisions" press release explicitly relies on "data-dependent," "meeting-by-meeting approach," and "not pre-committing to a particular rate path" language — and contains NO explicit signal that a further rate increase is likely at the July 23, 2026 meeting — the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-233. `6af81a6c-0de4-5061-b77e-fbff34eb5e04`

- Present date: `2026-05-02 20:59:52.941835`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Google make TPU 8i instances generally available to Google Cloud customers by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 1, 2026 and by 23:59 UTC on June 1, 2026, Google makes TPU 8i instances generally available (GA) to Google Cloud customers.

**"Generally available"** is defined as: a standard Google Cloud customer can provision and use TPU 8i instances via the Google Cloud Console or the `gcloud` CLI/API without requiring a private preview invitation, waitlist approval, or special allowlisting. Public preview with open self-service access also counts as general availability for purposes of this question.

**"TPU 8i"** refers specifically to the eighth-generation inference-optimized TPU announced by Google on April 22, 2026 at Google Cloud Next '26, as described on the Google Cloud Blog (https://cloud.google.com/blog/products/compute/ai-infrastructure-at-next26).

**Resolution source**: Official documentation on the Google Cloud TPU documentation page (https://cloud.google.com/tpu/docs), the Google Cloud Blog (https://cloud.google.com/blog/), or Google Cloud Release Notes (https://cloud.google.com/release-notes). A credible third-party report (e.g., from CNBC, Ars Technica, or The Verge) confirming GA status also suffices.

If TPU 8i remains in private preview, limited access, or has not been released to Cloud customers by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

Google has a long history of developing custom Tensor Processing Units (TPUs) for AI workloads. The sixth-generation TPU v6e, codenamed "Trillium," was announced in 2024 and offered a 4.7x increase in peak compute performance per chip over TPU v5e [AI infrastructure at Next '26 | Google Cloud Blog](https://cloud.google.com/blog/products/compute/ai-infrastructure-at-next26). The seventh-generation TPU, codenamed "Ironwood," was announced in 2025 with native FP8 support.

On April 22, 2026, at Google Cloud Next '26, Google announced its eighth-generation TPU systems, comprising two specialized chips [We're launching two specialized TPUs for the agentic era.](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/tpus-8t-8i-cloud-next/):

- **TPU 8t**: Optimized for training, featuring 9,600 chips in a single superpod providing 121 exaflops of compute and two petabytes of shared memory [AI infrastructure at Next '26 | Google Cloud Blog](https://cloud.google.com/blog/products/compute/ai-infrastructure-at-next26).
- **TPU 8i**: Optimized for inference and reinforcement learning, featuring 384 MB of on-chip SRAM, 288 GB of high-bandwidth memory (HBM), doubled ICI bandwidth to 19.2 Tb/s, and a dedicated Collectives Acceleration Engine (CAE) reducing on-chip latency by up to 5x [AI infrastructure at Next '26 | Google Cloud Blog](https://cloud.google.com/blog/products/compute/ai-infrastructure-at-next26).

Google stated that "TPU 8t and TPU 8i will be available to Cloud customers soon" but did not provide a specific general availability date [AI infrastructure at Next '26 | Google Cloud Blog](https://cloud.google.com/blog/products/compute/ai-infrastructure-at-next26). As of May 1, 2026, neither chip appears to have reached general availability status. Google I/O 2026 is scheduled for May 19–20 and could serve as an additional venue for availability announcements.

The question is whether the inference-focused TPU 8i will move from announcement to general availability within approximately five weeks of its unveiling — a timeline that is plausible but uncertain given Google's history of varying gaps between announcement and GA for TPU products.

**Exact later resolution packet**

The question resolves NO. TPU 8i (the eighth-generation inference-optimized TPU announced April 22, 2026 at Google Cloud Next '26) was NOT made generally available to Google Cloud customers during the resolution window (May 1, 2026 – 23:59 UTC June 1, 2026).

Key evidence:
- Google's official announcement blog post (blog.google "Our eighth generation TPUs: two chips for the agentic era") explicitly states that both TPU 8t and TPU 8i "will be generally available later this year," and directs interested customers to a "request more information" interest form (cloud.google.com/resources/tpu-interest) — characteristic of a pre-GA / interest-list phase, not self-service general availability. The blog page, including related stories dated as recent as May 19, 2026, contains no GA announcement [a4c53d].
- The official Google Cloud TPU release notes (docs.cloud.google.com/tpu/docs/release-notes), last updated May 29, 2026 and covering entries through June 1, 2026, contain NO entry announcing general availability of TPU 8i or TPU 8t. The only TPU GA entry refers to general Compute Engine TPU support, not the new eighth-generation chips [5c59d9].

Because no official source shows TPU 8i reaching GA (or open self-service public preview) within the window, a standard customer could NOT provision and use TPU 8i instances via the Google Cloud Console or gcloud CLI/API without an interest-form/allowlisting process during May 1 – June 1, 2026. The criteria for YES were therefore not met, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-234. `cf46e5f2-ef83-5c34-9ce1-a4a10d26b237`

- Present date: `2026-05-03 02:31:11.122981`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will GitHub resume accepting new individual Copilot plan signups by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, at any point between May 1, 2026 00:00 UTC and June 1, 2026 23:59 UTC, new users are able to sign up for at least one of the previously paused individual Copilot plans (GitHub Copilot Pro, Pro+, or Student) without being placed on a waitlist. Resolution is determined by one or more of the following:

1. The official GitHub Copilot plans page (https://github.com/features/copilot/plans) displays an active "Start free trial," "Sign up," or equivalent button allowing new users to initiate a paid individual subscription (Pro, Pro+, or Student); OR
2. An official announcement on the GitHub Blog (https://github.blog/) or GitHub Changelog (https://github.blog/changelog/) states that new signups for at least one of these individual plans have resumed.

If, by 23:59 UTC on June 1, 2026, the signup page continues to block new signups for all three paused individual plans and no official announcement of resumption has been made, this question resolves as **No**.

A waitlist-only option (where users can express interest but cannot immediately subscribe) does NOT count as accepting new signups.

**Pre-cutoff background**

On April 20, 2026, GitHub announced a pause on new signups for its individual Copilot plans—specifically GitHub Copilot Pro, Pro+, and Student plans—to prioritize service quality for existing paying customers [Changes to GitHub Copilot plans for individuals - GitHub Changelog](https://github.blog/changelog/2026-04-20-changes-to-github-copilot-plans-for-individuals/). The pause was driven by a capacity crunch caused by "agentic workflows," which involve long-running, parallelized sessions that consume far more compute resources than the original plan structure was designed to support [Microsoft's GitHub suspends Copilot account sign-ups - The Register](https://www.theregister.com/2026/04/20/microsofts_github_grounds_copilot_account/). GitHub is transitioning toward token-based billing to better manage infrastructure costs [Microsoft's GitHub suspends Copilot account sign-ups - The Register](https://www.theregister.com/2026/04/20/microsofts_github_grounds_copilot_account/). The free tier of GitHub Copilot remains open to new users [Changes to GitHub Copilot plans for individuals - GitHub Changelog](https://github.blog/changelog/2026-04-20-changes-to-github-copilot-plans-for-individuals/), and existing subscribers can still upgrade between plans [Changes to GitHub Copilot plans for individuals - GitHub Changelog](https://github.blog/changelog/2026-04-20-changes-to-github-copilot-plans-for-individuals/). GitHub has not provided a specific date for when new individual plan signups will resume. Additionally, GitHub Copilot code review will start consuming GitHub Actions minutes on June 1, 2026, signaling broader billing changes around that date [Changes to GitHub Copilot plans for individuals - GitHub Changelog](https://github.blog/changelog/2026-04-20-changes-to-github-copilot-plans-for-individuals/).

**Exact later resolution packet**

The question resolves NO. Two of the exact resolution sources confirm signups remained paused throughout the entire window (May 1 – June 1, 2026, 23:59 UTC):

1. The official GitHub Copilot plans page (https://github.com/features/copilot/plans), one of the two designated resolution sources, displays for the Pro, Pro+, and Max plans: "New plan sign-ups are temporarily paused as we ensure a high-quality experience." There are NO active "Start free trial" or "Sign up" buttons to initiate a paid individual subscription (Pro, Pro+, or Student) [f078b4]. This means criterion 1 of the resolution (an active button allowing new users to initiate a paid individual subscription) was not satisfied.

2. The GitHub Changelog post dated June 1, 2026 — "Updates to GitHub Copilot billing and plans" (https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/), the other designated resolution source — contains a section explicitly titled "New sign-ups remain paused," stating: "New user sign-ups remain paused for Copilot Student, Pro, Pro+, and Max plans. We'll reopen sign-ups in the coming weeks." [42443f]. Thus criterion 2 (an official GitHub Blog/Changelog announcement that signups have resumed) was also not satisfied — the only relevant announcement, made on the final day of the window, confirms the opposite: signups had NOT resumed.

Supporting context: GitHub's official Announcement & FAQ discussion (#192963) likewise confirms "New sign-ups for GitHub Copilot Pro, Pro+, and Student plans are paused," with FAQ stating "We do not have an estimated timeframe to share yet for when the pause will end," and contains user comments up to June 2, 2026 with no mention of resumption [0608d8].

Since, by 23:59 UTC on June 1, 2026, the signup page continued to block new signups for all three paused individual plans (no active subscription-initiation buttons) and no official announcement of resumption was made — indeed the June 1 changelog affirmatively stated signups "remain paused" — the question resolves NO per the stated criteria.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-235. `ea85de8f-0668-501d-9735-433c2a64acff`

- Present date: `2026-05-01 19:12:41.046472`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will A24 acquire North American theatrical distribution rights for any film in the 2026 Cannes Competition by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), a credible entertainment trade publication — specifically Variety (https://variety.com/), The Hollywood Reporter (https://www.hollywoodreporter.com/), or Deadline (https://deadline.com/) — publishes an article confirming that A24 has acquired North American theatrical distribution rights to at least one film selected for the official "In Competition" section of the 79th Cannes Film Festival (2026).

A "distribution deal" is defined as A24 obtaining North American theatrical distribution rights (i.e., the right to release the film theatrically in the United States). Pre-existing deals announced before April 30, 2026 do not count.

The "2026 Cannes Competition" refers specifically to films selected for the official "In Competition" section of the 79th Cannes Film Festival, as listed at https://www.festival-cannes.com/en/the-selection/.

If no such deal is publicly reported by the deadline, the question resolves **No**.

**Pre-cutoff background**

The 79th Cannes Film Festival runs from May 12 to 23, 2026 [Cannes 2026 Movies: Competition Lineup, Special Screenings](https://deadline.com/2026/04/cannes-2026-movies-lineup-competition-1236785446/). The official Competition lineup, announced in April 2026, includes 21 films from directors such as Pedro Almodóvar, Asghar Farhadi, Hirokazu Kore-eda, Ryûsuke Hamaguchi, Ira Sachs, and others [Cannes 2026 Movies: Competition Lineup, Special Screenings](https://deadline.com/2026/04/cannes-2026-movies-lineup-competition-1236785446/). As of April 30, 2026, no films in the Competition lineup have been reported as acquired by A24 [Cannes 2026 Movies: Competition Lineup, Special Screenings](https://deadline.com/2026/04/cannes-2026-movies-lineup-competition-1236785446/). Neon has acquired *Fjiord* (Cristian Mungiu) [Cannes 2026 Movies: Competition Lineup, Special Screenings](https://deadline.com/2026/04/cannes-2026-movies-lineup-competition-1236785446/).

A24 has a recent history of acquiring Cannes Competition titles. In 2024, A24 acquired North American rights to Paolo Sorrentino's *Parthenope* ahead of its Cannes premiere [Cannes: A24 Acquires U.S. Paolo Sorrentino's 'Parthenope' - Deadline](https://deadline.com/2024/05/cannes-a24-paolo-sorrentino-parthenope-1235903616/). In 2025, A24 had *Eddington* (Ari Aster) in Competition, which it already held distribution rights for [Distribution Watch: Cannes 2025 - Acquired Cinema - Substack](https://acquiredcinema.substack.com/p/distribution-watch-cannes-2025). A24 is a consistent buyer at Cannes, though acquisitions of Competition titles specifically are not guaranteed in any given year.

The festival ends May 23, leaving roughly one week before the June 1 deadline. Historically, many acquisition deals are announced during or immediately after the festival, making it plausible but uncertain that A24 would announce a Competition title deal within this window. Some Competition films may already have US distribution locked with other companies, and A24 may focus on titles outside the Competition section.

**Exact later resolution packet**

The question resolves NO because A24 did not acquire North American theatrical distribution rights to any film in the official "In Competition" section of the 79th Cannes Film Festival (2026) within the window April 30–June 1, 2026.

Evidence:
- A24's only notable Cannes 2026 acquisition was Jordan Firstman's "Club Kid," which A24 bought for ~$17M in worldwide rights. However, "Club Kid" was in the Un Certain Regard section, NOT the official In Competition section [Cannes 2026 Movies Sold So Far, From 'The Black Ball' to 'Coward'](https://www.indiewire.com/news/festivals/cannes-2026-movies-sold-so-far-paper-tiger-minotaur-1235191174/). This was widely reported by Variety (variety.com/2026/film/news/jordan-firstman-club-kid-sells-a24-cannes-bidding-war-1236751831/) and Deadline (deadline.com/2026/05/a24-global-rights-jordan-firstman-cannes-club-kid-1236914076/).
- A comprehensive distribution tracker (Acquired Cinema "Distribution Watch: Cannes 2026," last updated May 30, 2026) lists every In Competition film and its North American distributor. The Competition titles went to NEON (All of a Sudden, Fjord, Hope, Paper Tiger, Sheep in the Box, The Unknown), Sony Pictures Classics (Bitter Christmas/Almodóvar), Netflix (La Bola Negra/The Black Ball), MUBI (Coward, Fatherland, Minotaur), and Janus Films (The Dreamed Adventure). A24 does not appear as a distributor for ANY In Competition film [Distribution Watch: Cannes 2026 - Acquired Cinema](https://acquiredcinema.substack.com/p/distribution-watch-cannes-2026).
- A24 was reportedly in the bidding for the Competition title "The Black Ball" (La Bola Negra), but Netflix won those rights, not A24 [Cannes 2026 Movies Sold So Far, From 'The Black Ball' to 'Coward'](https://www.indiewire.com/news/festivals/cannes-2026-movies-sold-so-far-paper-tiger-minotaur-1235191174/) [Distribution Watch: Cannes 2026 - Acquired Cinema](https://acquiredcinema.substack.com/p/distribution-watch-cannes-2026).

Since no trade publication (Variety, THR, Deadline) reported A24 acquiring North American rights to an In Competition title between April 30 and June 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-236. `d91e6960-949a-5729-91e8-b1feb1db7772`

- Present date: `2026-05-03 03:20:04.328823`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the New York Yankees have the best record in the American League after all games on May 31, 2026?

**Resolution criteria**

This question resolves **Yes** if, after all MLB games scheduled for May 31, 2026, have been completed (by 11:59 PM ET), the New York Yankees have the highest winning percentage (PCT) among all 15 [American League](https://en.wikipedia.org/wiki/American_League) teams as displayed on the official MLB standings page: [https://www.mlb.com/standings](https://www.mlb.com/standings).

**Definition of "best record":** The team with the highest winning percentage (wins divided by total games played) holds the best record. If the Yankees are tied in winning percentage with one or more other AL teams, the question resolves **Yes** — i.e., the Yankees need only share the best record, not hold it outright.

If any other AL team has a strictly higher winning percentage than the Yankees after all May 31 games are completed, the question resolves **No**.

The resolution source is the official MLB standings at [https://www.mlb.com/standings](https://www.mlb.com/standings), checked after all games on May 31, 2026, have concluded.

**Pre-cutoff background**

As of May 2, 2026, the New York Yankees hold a 20-11 record (.645 winning percentage), placing them first in the [American League](https://en.wikipedia.org/wiki/American_League) East division and first overall in the American League [https://www.mlb.com/standings](https://www.mlb.com/standings). The Tampa Bay Rays are the closest competitor at 18-12 (.600). Other notable AL teams include the Cleveland Guardians and Detroit Tigers in the AL Central, and the Athletics leading the AL West. The American League comprises 15 teams across three divisions (East, Central, West). Over the course of a month, significant variance in baseball outcomes means competitive teams could surge past the Yankees, while the Yankees themselves could slump. The Yankees' current lead of approximately two games over the Rays and several games over most other AL teams provides a buffer, but is far from insurmountable over roughly 25-27 remaining games in May.

**Exact later resolution packet**

The question resolves YES only if, after all games on May 31, 2026, the New York Yankees have the highest (or tied-highest) winning percentage among all 15 American League teams.

Multiple sources confirm the AL standings after May 31, 2026 [https://www.statmuse.com/mlb/ask/mlb-american-league-standings-on-may-31-2026](https://www.statmuse.com/mlb/ask/mlb-american-league-standings-on-may-31-2026):
- AL East: Tampa Bay Rays 36-21 (.632), New York Yankees 36-23 (.610), Toronto Blue Jays 29-31 (.483), Baltimore Orioles 28-32 (.467), Boston Red Sox 25-33 (.431)
- AL Central: Cleveland Guardians 34-27 (.557), Chicago White Sox 32-28 (.533), Minnesota Twins 28-33 (.459), Kansas City Royals 23-37 (.383), Detroit Tigers 23-38 (.377)
- AL West: Seattle Mariners 32-29 (.525), Texas Rangers 29-31 (.483), Athletics 28-31 (.475), Houston Astros 27-34 (.443), Los Angeles Angels 23-38 (.377)

The Tampa Bay Rays held the highest AL winning percentage at .632, strictly higher than the Yankees' .610. This is corroborated by FOX Sports standings showing Tampa Bay Rays 36-21 ranked #1 in the AL East and Yankees 36-23 at #2, and by the 2026 New York Yankees Wikipedia page / Baseball-Reference both listing the Yankees at 36-23 (.610), 2nd place in the AL East.

Because at least one other AL team (Tampa Bay Rays) had a strictly higher winning percentage than the Yankees, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-237. `8dbb915c-1b64-5784-9209-eb46f1bb0984`

- Present date: `2026-05-16 12:49:16.924130`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will any platform currently under Ofcom Online Safety Act investigation or enforcement action announce withdrawal from or geoblocking of the UK market by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 12, 2026 00:00 UTC and July 1, 2026 00:00 UTC, any platform that is listed as subject to an active Ofcom investigation or enforcement action on the Ofcom Online Safety industry bulletin page (https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/online-safety-industry-bulletins/) as of May 12, 2026 announces or implements a withdrawal of services from the UK market.

**"Withdrawal of services"** is defined as meeting at least one of the following measurable criteria:
1. The platform issues a formal public statement (e.g., on its website, blog, or official social media account) announcing it will cease providing services to UK users; OR
2. The platform implements geoblocking of UK IP addresses, preventing users located in the UK from accessing the service (as confirmed by Ofcom, credible news reporting, or verifiable testing); OR
3. The platform removes its app from UK-specific app stores (Apple App Store UK or Google Play Store UK) as part of a deliberate withdrawal (not a temporary technical issue).

**"Platform currently under Ofcom investigation or subject to enforcement action"** means any service provider listed in the enforcement or investigations sections of the Ofcom Online Safety industry bulletins (https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/online-safety-industry-bulletins/) as of May 12, 2026 00:00 UTC. As of the March 2026 bulletin, this includes but is not limited to: 8579 LLC, Kick Online Entertainment SA, Im.ge, X (formerly Twitter), Novi Ltd, Reply Buzzer Ltd, Telegram, the provider of two image board services, and an unnamed suicide forum.

The announcement or implementation of withdrawal must occur on or after May 12, 2026 00:00 UTC to exclude prior events (such as the Itai Tech Ltd geoblocking, which occurred before this date).

**Resolution sources:** The Ofcom industry bulletins page (https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/online-safety-industry-bulletins/), official Ofcom announcements, or credible news reporting from sources such as Reuters (https://www.reuters.com), BBC News (https://www.bbc.co.uk/news), The Guardian (https://www.theguardian.com), or TechCrunch (https://techcrunch.com).

This question resolves **No** if no qualifying withdrawal is announced or implemented by July 1, 2026 00:00 UTC.

**Pre-cutoff background**

Under the UK's Online Safety Act 2023 (https://en.wikipedia.org/wiki/Online_Safety_Act_2023), Ofcom has been actively investigating and fining digital platforms for non-compliance. As of March 2026, the following platforms are subject to enforcement action or formal investigation [https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/online-safety-industry-bulletins/online-safety-industry-bulletin-march-2026](https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/online-safety-industry-bulletins/online-safety-industry-bulletin-march-2026):

**Platforms fined (enforcement action completed or ongoing):**
- **8579 LLC**: Fined £1.35 million for failing to implement age assurance and £50,000 for failing to respond to information requests.
- **Kick Online Entertainment SA**: Fined £800,000 for failing to implement age checks and £30,000 for failing to comply with information requests.
- **Im.ge**: Fined £20,000 for failing to comply with statutory information requests.
- **An unnamed suicide forum**: Issued a provisional notice of contravention regarding illegal content risk assessments and safety duties.

**Platforms under formal investigation:**
- **X (formerly Twitter)**: Investigation opened January 2026 regarding compliance with duties to protect users from illegal content and harmful material.
- **Two unnamed online image boards**: Under investigation for compliance with duties to protect users from illegal content (believed to include 4chan based on prior reporting).
- **Novi Ltd**: Under investigation regarding the duty to prevent children from encountering pornographic content.
- **Reply Buzzer Ltd**: Under investigation regarding the duty to prevent children from encountering pornographic content.
- **Telegram**: Investigation announced April 2026.
- **Teen chat sites**: Investigation announced April 2026.

**Key precedent:** Itai Tech Ltd was under investigation but its case was closed after the company voluntarily implemented a block restricting users with UK IP addresses from accessing its service — effectively withdrawing from the UK market [https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/online-safety-industry-bulletins/online-safety-industry-bulletin-march-2026](https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/online-safety-industry-bulletins/online-safety-industry-bulletin-march-2026). This demonstrates that market withdrawal/geoblocking is a viable compliance strategy, particularly for smaller overseas platforms where the cost of full compliance may exceed UK revenue.

The Ofcom Online Safety industry bulletin (https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/online-safety-industry-bulletins/online-safety-industry-bulletin-march-2026) tracks the current status of all investigations and enforcement actions.

**Exact later resolution packet**

The question resolves **NO**. Between May 12, 2026 00:00 UTC and July 1, 2026 00:00 UTC, no platform listed as under active Ofcom Online Safety Act investigation or enforcement action (as of May 12, 2026) announced or implemented a qualifying withdrawal from the UK market (formal cessation statement, geoblocking of UK IP addresses, or removal from UK app stores).

Evidence reviewed:

1. Ofcom Online Safety industry bulletin – June 2026 (published 29 June 2026, i.e. covering the full resolution window). It details new fines and investigations (e.g., Youngtek Solutions Ltd, First Time Videos LLC, 4chan, an online suicide forum, Telegram, Teen Chat, Chat Avenue, Kemono.cr, Pimpbunny) but reports NO platform withdrawing from, or geoblocking, the UK market during the window. It even notes that closing of investigations via geoblocking (Itai Tech) predates the window [Online Safety industry bulletin – June 2026 - Ofcom](https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/online-safety-industry-bulletins/online-safety-industry-bulletin-june-2026) [Online Safety industry bulletin – June 2026 - Ofcom](https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/online-safety-industry-bulletins/online-safety-industry-bulletin-june-2026). URL: https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/online-safety-industry-bulletins/online-safety-industry-bulletin-june-2026

2. Ofcom's age-assurance Enforcement Programme page (last updated 19 June 2026). The only platforms that geoblocked the UK and had investigations closed are Itai Tech Ltd (decision 20 Nov 2025) and Duplanto Ltd (blocked ~July 2025, investigation closed 30 March 2026) — both BEFORE the window. Novi Ltd and Reply Buzzer Ltd remained under investigation with no reported geoblock/withdrawal in the window [Enforcement Programme to protect children from ...](https://www.ofcom.org.uk/online-safety/protecting-children/enforcement-programme-to-protect-children-from-encountering-pornographic-content-through-the-use-of-age-assurance). URL: https://www.ofcom.org.uk/online-safety/protecting-children/enforcement-programme-to-protect-children-from-encountering-pornographic-content-through-the-use-of-age-assurance

3. Reed Smith LLP OSA tracker (updated ~12 June 2026): records in-window events such as the £600k/£800k porn fines, Youngtek fine (27 May 2026) and expansion of the Reply Buzzer investigation (27 May 2026), but no market withdrawal/geoblock during the window [UK Online Safety Act 2023](https://www.reedsmith.com/topics/uk-online-safety-act-2023/). URL: https://www.reedsmith.com/topics/uk-online-safety-act-2023/

4. The one in-window candidate — the online suicide forum fined £950,000 on 13 May 2026 — does NOT meet the criteria. Per BBC, Reuters and The Guardian (all 13 May 2026), the forum did NOT withdraw or effectively geoblock: as of 13 May the site "remained accessible by people in the UK without the use of a VPN," its earlier (2025) attempts to restrict UK access were "not consistently applied or effective," and it issued no cessation statement. Instead it posted a message defending "the right to access lawful information," while Ofcom said it was "preparing to apply for a court order which would require internet service providers to block access." An Ofcom/ISP-imposed block is regulator action, not the platform's own withdrawal, and no effective platform geoblock occurred [Ofcom fines suicide forum £950,000 for not blocking UK users - BBC](https://www.bbc.com/news/articles/cdxpyvvdyn7o) [UK regulator fines suicide forum over $1 million, warns of UK block](https://www.reuters.com/world/uk/uk-regulator-fines-suicide-forum-over-1-million-warns-uk-block-2026-05-13/) [US-based internet suicide forum implicated in 160 UK deaths fined ...](https://www.theguardian.com/society/2026/may/13/us-based-internet-suicide-forum-implicated-in-160-deaths-fined-950000). URLs: https://www.bbc.com/news/articles/cdxpyvvdyn7o ; https://www.reuters.com/world/uk/uk-regulator-fines-suicide-forum-over-1-million-warns-uk-block-2026-05-13/ ; https://www.theguardian.com/society/2026/may/13/us-based-internet-suicide-forum-implicated-in-160-deaths-fined-950000

5. Ofcom's June 2026 Online Safety Briefing (published 30 June 2026) similarly reports no platform withdrawal/geoblock in the window; the only historical example cited is Itai Tech, which predates the window [Online Safety Briefing - June 2026 - LinkedIn](https://www.linkedin.com/pulse/online-safety-briefing-june-2026-ofcom-9xije).

Since no platform under investigation/enforcement as of 12 May 2026 announced or implemented a qualifying UK withdrawal within the 12 May – 1 July 2026 window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-238. `28026705-3e88-5eb9-9788-7fb8b7169d61`

- Present date: `2026-05-14 06:23:13.288790`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Japanese House of Councillors adopt any formal amendment to the National Intelligence Council Bill before the bill's final passage?

**Resolution criteria**

This question resolves **Yes** if the House of Councillors adopts any formal amendment to the National Intelligence Council Bill on or after May 12, 2026, and before or at the bill's final passage. It resolves **No** if the bill passes the House of Councillors without any formal amendments, or if the bill has not reached final passage by July 1, 2026.

**Definition of "formal amendment":** A formal amendment is any officially voted-upon change to the legislative text of the bill as recorded in the proceedings of the House of Councillors. This includes additions, deletions, or modifications to the bill's articles or provisions. Non-binding supplementary resolutions (附帯決議), political commitments between parties, or statements of understanding that do not alter the bill's text do NOT count as formal amendments.

**Definition of "final passage":** Final passage means the vote on the bill at a plenary session of the House of Councillors (本会議) that determines whether the bill is approved or rejected by that chamber.

**Only amendments adopted on or after May 12, 2026, count for resolution.**

**Resolution source:** The official legislative records of the House of Councillors (https://www.sangiin.go.jp/eng/index.htm) or credible English-language reporting from major outlets such as The Japan Times (https://www.japantimes.co.jp/), Kyodo News (https://english.kyodonews.net/), NHK World (https://www3.nhk.or.jp/nhkworld/en/), or Reuters.

**Pre-cutoff background**

On April 23, 2026, Japan's House of Representatives passed the National Intelligence Council Bill without amendment [Japan's Intelligence Reform: Securitization, Oversight, and the Cost ...](https://thediplomat.com/2026/04/japans-intelligence-reform-securitization-oversight-and-the-cost-of-consensus/). The bill seeks to upgrade the Cabinet Intelligence and Research Office (CIRO) into a National Intelligence Agency and establish a National Intelligence Council chaired by the Prime Minister [Japan's Intelligence Reform: Securitization, Oversight, and the Cost ...](https://thediplomat.com/2026/04/japans-intelligence-reform-securitization-oversight-and-the-cost-of-consensus/). Deliberations in the House of Councillors (Upper House) began on May 8, 2026 [Japan's upper house begins deliberation on controversial national ...](https://www.bastillepost.com/global/article/5839898-japans-upper-house-begins-deliberation-on-controversial-national-intelligence-overhaul-bill). The government aims for enactment by July 2026.

Critics have raised concerns about a proposed unit within the national intelligence bureau tasked with policing "false and misleading information" on social media, as well as the perceived lack of independent oversight mechanisms [Japan's upper house begins deliberation on controversial national ...](https://www.bastillepost.com/global/article/5839898-japans-upper-house-begins-deliberation-on-controversial-national-intelligence-overhaul-bill). In the Lower House, the Centrist Reform Alliance secured only political commitments—not legally binding amendments—before voting in favor of the bill [Japan's Intelligence Reform: Securitization, Oversight, and the Cost ...](https://thediplomat.com/2026/04/japans-intelligence-reform-securitization-oversight-and-the-cost-of-consensus/).

The opposition holds stronger leverage in the House of Councillors than in the Lower House [Japan's Intelligence Reform: Securitization, Oversight, and the Cost ...](https://thediplomat.com/2026/04/japans-intelligence-reform-securitization-oversight-and-the-cost-of-consensus/). As of the 2025 House of Councillors election, the ruling coalition of the LDP (101 seats) and Komeito (21 seats) holds 122 seats—three short of the 125-seat majority required in the 248-seat chamber [2025 Japanese House of Councillors election - Wikipedia](https://en.wikipedia.org/wiki/2025_Japanese_House_of_Councillors_election). This means the ruling coalition must secure support from other parties to pass the bill. However, any formal amendment adopted by the Upper House would require the bill to be returned to the Lower House or referred to a joint committee, creating a strong procedural incentive for the ruling coalition to pass it unamended [Japan's Intelligence Reform: Securitization, Oversight, and the Cost ...](https://thediplomat.com/2026/04/japans-intelligence-reform-securitization-oversight-and-the-cost-of-consensus/).

The bill's progress can be tracked on the official House of Councillors website: https://www.sangiin.go.jp/eng/index.htm

**Exact later resolution packet**

The question resolves **NO (0)**.

**Antecedent/timeline check (bill reached final passage before July 1, 2026):** The National Intelligence Council Establishment Bill (国家情報会議設置法案, 閣法第24号) reached final passage in a plenary session (本会議) of the House of Councillors on May 27, 2026, when it was passed (可決) and enacted. This is confirmed by the official House of Councillors legislative record [9b97e9, 17e556] and by Kyodo News [0396f1]. Because final passage occurred before the July 1, 2026 deadline, the question is resolvable on the amendment question (rather than defaulting to NO on a missed deadline).

**Amendment question (did the Upper House adopt a formal amendment?):** No. The only amendment (修正案) was submitted by the opposition Constitutional Democratic Party (立憲民主党) in the Cabinet Committee (内閣委員会) on May 26, 2026, but it was REJECTED. The official House of Councillors committee record states verbatim: "採決の結果、修正案を否決し、原案どおり可決すべきものと決定されました" — "As a result of the vote, the amendment was rejected, and it was decided that the original bill should be passed as is." [a9987d]. The bill's official detail page lists the committee amendment PDF explicitly as "立憲・否決" (Constitutional Democratic Party / rejected) [9b97e9]. The May 27 plenary then passed the bill as reported from committee — i.e., the original text (原案) — with no amendment adopted [17e556].

**Conclusion:** The House of Councillors passed the bill without adopting any formal amendment to the legislative text; the sole proposed amendment was defeated. Under the resolution criteria — which resolve NO "if the bill passes the House of Councillors without any formal amendments" — the outcome is NO (0). (The rejected opposition amendment does not count, and no supplementary resolution issue arises since no textual change was adopted.)

Supporting URLs:
- Official bill status: https://www.sangiin.go.jp/japanese/joho1/kousei/gian/221/meisai/m221080221024.htm [9b97e9]
- Committee proceedings (May 26, 2026, amendment rejected): https://www.sangiin.go.jp/japanese/ugoki/r8/260526.html [a9987d]
- Plenary proceedings (May 27, 2026, passed): https://www.sangiin.go.jp/japanese/ugoki/r8/260527-1.html [17e556]
- Kyodo News (enacted May 27, 2026): https://english.kyodonews.net/articles/-/76794 [0396f1]

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-239. `5f75cb45-ccbf-5ad2-910d-d3ddfd3ce010`

- Present date: `2026-05-14 11:08:50.099863`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Bangladesh Parliament formally establish the Constitution Reform Assembly (as mandated by the July Charter) by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026, and on or before July 1, 2026 (23:59 Bangladesh Standard Time, UTC+6), the Bangladesh Parliament formally establishes the Constitution Reform Assembly through one of the following specific legislative or executive milestones:

1. A majority vote in Parliament passing a resolution or act that constitutes the Assembly; OR
2. An official notification published in the Bangladesh Gazette establishing the Assembly and appointing its members; OR
3. A presidential decree formally constituting the Assembly.

"Formally establish" means that the Assembly is officially constituted as a legal body with named members — it is not sufficient for the Assembly to merely be discussed, debated, or proposed in Parliament.

**Partial formation / BNP boycott:** If the Assembly is formally established (per the criteria above) but the BNP boycotts or refuses to take the oath while other parties participate, this still resolves **Yes**, provided the establishment meets one of the three milestones above. If no formal establishment occurs by the deadline, the question resolves **No**, regardless of ongoing negotiations or court proceedings.

**Actions taken before May 12, 2026 do not count.** Only establishment actions occurring on or after May 12, 2026 (00:00 BST, UTC+6) are eligible for resolution.

**Resolution source:** Official records from the Bangladesh Parliament (https://www.parliament.gov.bd/) or the Bangladesh Gazette (https://www.dpp.gov.bd/bgpress/), supplemented by credible news reporting from The Daily Star (https://www.thedailystar.net/), Dhaka Tribune (https://www.dhakatribune.com/), Reuters, or AP.

**Pre-cutoff background**

Following the July 2024 uprising that ousted the Awami League government, Bangladesh's Interim Government and approximately 30 political parties agreed upon the "July Charter" — a comprehensive framework for constitutional, electoral, and administrative reforms. The Charter's full text is available via ConstitutionNet (http://constitutionnet.org/vl/item/july-national-charter-2025-bangladesh-english-translation). On November 13, 2025, the Interim Government enacted the "July Charter (Constitution Reform) Implementation Order, 2025" (http://constitutionnet.org/vl/item/implementation-order-july-national-charter-2025-bangladesh-english-translation), which mandated the creation of a "Constitution Reform Assembly" to exercise the constituent power of the people and undertake major constitutional changes, including transitioning to a bicameral legislature [http://constitutionnet.org/news/voices/mandate-deferred-ruling-partys-obstruction-constitutional-reform-bangladesh](http://constitutionnet.org/news/voices/mandate-deferred-ruling-partys-obstruction-constitutional-reform-bangladesh).

The July Charter was endorsed by 68% of voters in a nationwide referendum held on February 12, 2026 [https://thediplomat.com/2026/04/bangladeshs-parties-are-divided-over-the-reform-process/](https://thediplomat.com/2026/04/bangladeshs-parties-are-divided-over-the-reform-process/). However, the reform process has since stalled. The ruling Bangladesh Nationalist Party (BNP), which holds a parliamentary majority, refuses to take the oath as members of the Constitution Reform Assembly, arguing that the body lacks constitutional legitimacy and that reforms must proceed through standard parliamentary amendment procedures (Article 142) [https://thediplomat.com/2026/04/bangladeshs-parties-are-divided-over-the-reform-process/](https://thediplomat.com/2026/04/bangladeshs-parties-are-divided-over-the-reform-process/).

As of May 2026, the BNP has also mounted a legal challenge: a writ petition filed by BNP affiliates led the High Court to issue a "Rule Nisi" questioning the legality of the Implementation Order, on the grounds that the Constitution does not permit the President to issue such an order. The BNP has used this Rule Nisi as a political shield, arguing in Parliament that the Implementation Order is void ab initio and need not be complied with [http://constitutionnet.org/news/voices/mandate-deferred-ruling-partys-obstruction-constitutional-reform-bangladesh](http://constitutionnet.org/news/voices/mandate-deferred-ruling-partys-obstruction-constitutional-reform-bangladesh).

The opposition, led by Jamaat-e-Islami, views the referendum result as a binding political commitment and has staged parliamentary walkouts and street protests demanding the Assembly's formation [https://thediplomat.com/2026/04/bangladeshs-parties-are-divided-over-the-reform-process/](https://thediplomat.com/2026/04/bangladeshs-parties-are-divided-over-the-reform-process/). The Assembly is tasked with completing reforms within 180 working days once constituted [https://thediplomat.com/2026/04/bangladeshs-parties-are-divided-over-the-reform-process/](https://thediplomat.com/2026/04/bangladeshs-parties-are-divided-over-the-reform-process/).

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if, between May 12, 2026 and July 1, 2026 (23:59 BST), the Bangladesh Parliament formally established the Constitution Reform Assembly (CRA) — as a legal body with NAMED members — via one of three milestones: (1) a majority parliamentary vote, (2) a Bangladesh Gazette notification establishing the Assembly and appointing its members, or (3) a presidential decree. None of these occurred.

KEY FACTS AND TIMELINE (from approved/credible sources):
- After the Feb 12, 2026 referendum passed the July Charter, newly elected MPs were to be sworn in a second time as members of the Constitution Reform Assembly/Council on Feb 17, 2026. The ruling BNP — which won a decisive parliamentary majority (reported as roughly two-thirds) — refused to take that oath, arguing the body lacks constitutional legitimacy and that reforms must go through the ordinary amendment route (Article 142) [2286fc].
- The ConstitutionNet analysis (published April 15, 2026) documents the BNP's sustained obstruction, its use of a High Court "Rule Nisi" as a political shield, and its pivot toward a special parliamentary amendment committee instead of the Assembly. As of that date the Assembly had not been established [2286fc].
- A Daily Star opinion piece ("Back, again, to the cycle of broken promises?", April 19, 2026) confirms BNP members had "yet to take oath as members of a Constitution Reform Assembly" and that the process had stalled [309a17].
- Within the resolution window: A Daily Star report (May 14, 2026) states the BNP government rejected the Assembly and proposed instead a 17-member special parliamentary committee (proposed April 29, 2026) to amend the constitution; Jamaat-e-Islami and NCP refused to join it and continued demanding the Assembly/Council [a26531].
- A further Daily Star report (May 18, 2026) reiterates that no members had been appointed to a Constitution Reform Assembly; the government was pursuing the special parliamentary committee (12 government names, 5 requested from opposition) rather than the CRA [c2c7d2].
- A Dhaka Tribune parliamentary report accessed at the deadline confirms the "Constitution Reform Council" had still NOT been convened, with the government criticized for delaying it and the opposition demanding a session — no members sworn in or appointed [42b718].
- Consistent with this, as late as late June 2026, Home Minister/BNP leader Salahuddin Ahmed continued telling Parliament the July Charter (Constitution Reform) Implementation Order was illegal/unconstitutional and that the President could not convene a reform council because "such a body does not exist" (Daily Star parliament coverage; corroborated by New Age and TBS reporting).

BNP BOYCOTT: The BNP boycott/refusal to take the oath did occur. Critically, however, the establishment did NOT proceed despite it — because the BNP holds the parliamentary majority and controls the government, so there was no parliamentary vote, no Gazette notification appointing members, and no presidential decree constituting the Assembly. The "partial formation / BNP boycott resolves YES" clause requires that the Assembly still be formally established via one of the three milestones with other parties participating; that did not happen. The opposition (Jamaat/NCP) staged walkouts/protests but the Assembly was never constituted.

CONCLUSION: No formal establishment of the Constitution Reform Assembly (with named members, via parliamentary vote, Gazette notification, or presidential decree) occurred on or after May 12, 2026 and on or before July 1, 2026. The question therefore resolves NO.

Direct source URLs used:
- http://constitutionnet.org/news/voices/mandate-deferred-ruling-partys-obstruction-constitutional-reform-bangladesh [2286fc]
- https://www.thedailystar.net/opinion/views/news/back-again-the-cycle-broken-promises-4154771 [309a17]
- https://www.thedailystar.net/news/bangladesh/news/constitution-amendments-jamaat-ncp-set-skip-special-js-committee-4175361 [a26531]
- https://www.thedailystar.net/news/politics/news/constitution-amendment-bnp-again-ask-opposition-join-panel-4178246 [c2c7d2]
- https://www.dhakatribune.com/bangladesh/parliament/407832/parliament-sees-debate-over-july-charter [42b718]

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-240. `125e0a9e-c284-5ac5-b05b-0a4b92a9deff`

- Present date: `2026-05-16 08:52:26.343228`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-05-25 00:00:00`

**Question**

Will the U.S. Senate hold a roll call vote on the motion to proceed on the immigration reconciliation bill (pursuant to S.Con.Res.33) during the week of May 18–24, 2026?

**Resolution criteria**

This question resolves **Yes** if, according to the official U.S. Senate Roll Call Votes page (https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm) or Congress.gov (https://www.congress.gov/), the U.S. Senate holds a formal roll call vote on a **motion to proceed** to the immigration reconciliation bill produced pursuant to S.Con.Res.33 (the FY2026 budget resolution) during the week of **May 18–24, 2026 (Monday through Sunday, Eastern Time)**.

A "motion to proceed" is defined as a formal procedural motion, subject to a recorded roll call vote, to begin Senate floor consideration of the bill. Unanimous consent agreements to proceed do **not** count; there must be a recorded roll call vote.

The bill in question is the reconciliation legislation produced under the instructions of S.Con.Res.33 (https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/33), commonly referred to as the "$72 billion immigration reconciliation bill." If the bill receives a different cost estimate or title but is the reconciliation vehicle arising from S.Con.Res.33's instructions, it still qualifies.

This question resolves **No** if no such roll call vote occurs during the specified week.

**Pre-cutoff background**

On April 23, 2026, the U.S. Senate passed S.Con.Res.33, a budget resolution for FY2026, by a vote of 50-48, with Senators Murkowski (R-AK) and Paul (R-KY) joining all Democrats in opposition [S.Con.Res.33 - A concurrent resolution setting forth ... - Congress.gov](https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/33). The resolution directs the Senate Judiciary and Homeland Security committees to submit reconciliation recommendations increasing the deficit by up to $70 billion, with a deadline of May 15, 2026 [S.Con.Res.33 - A concurrent resolution setting forth ... - Congress.gov](https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/33). The House approved the resolution on April 29, 2026 [S.Con.Res.33 - A concurrent resolution setting forth ... - Congress.gov](https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/33).

On May 5, 2026, Senate Republicans unveiled the resulting $72 billion reconciliation package, which would fund Immigration and Customs Enforcement (ICE), Customs and Border Protection (CBP), and other immigration enforcement priorities [GOP drops $72B immigration reconciliation bill - Punchbowl News](https://punchbowl.news/article/senate/72b-recon/). Senate GOP leaders have stated their intention to bring this bill to the floor during the week of May 18, 2026, which is the final week both chambers are scheduled to be in session for May [GOP drops $72B immigration reconciliation bill - Punchbowl News](https://punchbowl.news/article/senate/72b-recon/).

However, floor consideration faces several risks. Democrats, led by Senator Jeff Merkley, have vowed to raise Byrd Rule challenges against provisions they argue are extraneous to the budget [GOP drops $72B immigration reconciliation bill - Punchbowl News](https://punchbowl.news/article/senate/72b-recon/). The narrow Republican majority (the budget resolution passed 50-48) means any defections could delay or derail proceedings. Legislative schedules in the Senate frequently slip due to procedural disputes, amendment negotiations, or internal disagreements among pivotal senators.

As of May 13, 2026, no roll call vote on a motion to proceed to the immigration reconciliation bill has been recorded on Senate.gov [Roll Call Votes 119th Congress - 2nd Session (2026) - U.S. Senate](https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm). The reconciliation bill does not yet have an assigned bill number on Congress.gov, as committee markups were still in progress.

**Exact later resolution packet**

NO. The qualifying bill appears to be S.2, the Secure America Act: Congress.gov’s S.2 text identifies it as introduced on May 20, 2026 and states that it is “To provide for reconciliation pursuant to title II of S. Con. Res. 33,” so it is the reconciliation vehicle covered by the question even though it uses a different title than “immigration reconciliation bill” [Text - S.2 - 119th Congress (2025-2026): Secure America Act](https://www.congress.gov/bill/119th-congress/senate-bill/2/text). Official source URL: https://www.congress.gov/bill/119th-congress/senate-bill/2/text

For the relevant Eastern Time window, Monday May 18 through Sunday May 24, 2026, the official Senate roll-call page lists only roll call votes 125–130: Vote 125 on May 18 was on nominations en bloc; votes 126–129 on May 19 were on district-court cloture/confirmation and a motion to discharge S.J.Res.185; and vote 130 on May 20 was on confirmation of Evan Rikhye [https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm](https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm). None of those official roll call entries was a recorded vote on a motion to proceed to S.2 or any other S.Con.Res.33 immigration reconciliation vehicle [https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm](https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm). Official source URL: https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm

Congress.gov’s official all-actions page for S.2 likewise shows only two May 20, 2026 actions in that week: the Budget Committee reported the original measure to the Senate, and the measure was placed on the Senate Legislative Calendar as Calendar No. 417; it does not show any recorded Senate roll call vote on a motion to proceed during May 18–24, 2026 [https://www.congress.gov/bill/119th-congress/senate-bill/2/all-actions](https://www.congress.gov/bill/119th-congress/senate-bill/2/all-actions). Official source URL: https://www.congress.gov/bill/119th-congress/senate-bill/2/all-actions

Because the resolution criteria require a recorded roll call vote on a motion to proceed, and the official Senate/Congress.gov records do not show such a vote in the specified week, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-241. `c3bb67ad-3d40-5b96-90e8-80b423c1cf9f`

- Present date: `2026-05-29 01:43:44.527300`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court's judgment in Cisco Systems, Inc. v. Doe I (No. 24-856) be unanimous (9-0)?

**Resolution criteria**

This question resolves **Yes** if the Supreme Court of the United States issues its decision in Cisco Systems, Inc. v. Doe I (No. 24-856) on or after May 12, 2026, and on or before July 1, 2026, and the judgment (i.e., the final disposition/outcome of the case, not the legal reasoning) is supported by all nine participating justices (9-0). Justices who "concur in the judgment" without joining the majority opinion still count toward unanimity for the purposes of this question, as "unanimous" here refers solely to the judgment, not to the reasoning.

The question resolves **No** if:
- The decision is issued within the resolution window but the judgment is not 9-0 (e.g., any justice dissents from the judgment), OR
- Any justice is recused, resulting in fewer than 9 justices participating (e.g., an 8-0 decision does not count as 9-0).

If the decision is not issued by July 1, 2026, the question resolves **No**.

**Resolution source:** The official opinion as published on the Supreme Court of the United States website at https://www.supremecourt.gov/opinions/slipopinions.aspx (Opinions of the Court page) or the case docket at https://www.supremecourt.gov/docket/docketfiles/html/public/24-856.html.

**Pre-cutoff background**

Cisco Systems, Inc. v. Doe I (No. 24-856) concerns whether the Alien Tort Statute (ATS) and the Torture Victim Protection Act (TVPA) permit claims for aiding and abetting against U.S. corporations. The case involves allegations that Cisco helped the Chinese government build surveillance technology used to identify and persecute Falun Gong practitioners.

The Supreme Court granted certiorari on January 9, 2026, limited to Questions 1 and 3 from the petition. Oral arguments were held on April 28, 2026. The Solicitor General participated as amicus curiae with divided argument time. A decision is expected before the end of the October 2025 Term (typically by late June 2026).

Prior ATS cases at the Supreme Court have produced varying levels of agreement:
- **Kiobel v. Royal Dutch Petroleum Co. (2013):** The judgment was unanimous (9-0), but four justices concurred only in the judgment, disagreeing with the majority's reasoning based on the presumption against extraterritoriality.
- **Jesner v. Arab Bank, PLC (2018):** A 5-4 decision holding that foreign corporations cannot be defendants under the ATS. The narrow margin reflected deep ideological divisions.
- **Nestlé USA, Inc. v. Doe (2021):** A fragmented decision with no single majority opinion, though 8 justices agreed on the judgment. Multiple concurrences and a partial dissent made the legal landscape unclear.

This history shows that while the Court can sometimes unite on the judgment in ATS cases (especially on narrow procedural or jurisdictional grounds), deep disagreements on reasoning are common, and close splits on the judgment itself are also possible. The unanimity of the judgment in Cisco will likely depend on whether the Court finds a narrow ground for decision or addresses broader questions of corporate aiding-and-abetting liability.

**Exact later resolution packet**

The question resolves **NO (0)**.

**Decision date (within window):** The Supreme Court issued its decision in Cisco Systems, Inc. v. Doe I (No. 24-856) on June 23, 2026 [Docket for 24-856 - Supreme Court](https://www.supremecourt.gov/docket/docketfiles/html/public/24-856.html)[[PDF] 24-856 Cisco Systems, Inc. v. Doe (06/23/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/24-856_kjfm.pdf). This falls within the required resolution window of on/after May 12, 2026 and on/before July 1, 2026. So the antecedent condition (decision issued within the window) was satisfied.

**Judgment was NOT unanimous (6-3):** The judgment was REVERSED and the case REMANDED. Per the official docket entry and slip opinion voting lineup: Justice Barrett delivered the opinion of the Court, joined by Chief Justice Roberts and Justices Thomas, Alito, Gorsuch, and Kavanaugh (six justices). Justice Jackson filed an opinion concurring in part and dissenting in part, in which Justice Kagan joined. Justice Sotomayor filed a dissenting opinion, in which Justices Kagan and Jackson joined as to Parts I–III and V [Docket for 24-856 - Supreme Court](https://www.supremecourt.gov/docket/docketfiles/html/public/24-856.html)[[PDF] 24-856 Cisco Systems, Inc. v. Doe (06/23/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/24-856_kjfm.pdf).

**Analysis of dissents vs. concurrences:** The resolution criteria state that justices who merely "concur in the judgment" count toward unanimity, but justices who "dissent from the judgment" cause a NO resolution. Here, Justice Sotomayor filed a *dissenting opinion* (joined by Kagan, and by Jackson as to certain parts), and Justice Jackson filed an opinion *dissenting in part*. These are dissents from the judgment, not mere concurrences in the judgment. Multiple secondary legal sources (Mayer Brown, Sullivan & Cromwell, Debevoise) also characterize the outcome as a 6-3 decision. Therefore the judgment was 6-3, not 9-0.

**Recusal check:** All nine justices participated; no recusal occurred [[PDF] 24-856 Cisco Systems, Inc. v. Doe (06/23/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/24-856_kjfm.pdf). However, because the judgment was decided 6-3 with dissents, the unanimity requirement fails.

Since the decision was issued in the window but the judgment was 6-3 (not 9-0), the question resolves NO.

**Sources:** Official Supreme Court slip opinion at https://www.supremecourt.gov/opinions/25pdf/24-856_kjfm.pdf and docket at https://www.supremecourt.gov/docket/docketfiles/html/public/24-856.html [Docket for 24-856 - Supreme Court](https://www.supremecourt.gov/docket/docketfiles/html/public/24-856.html)[[PDF] 24-856 Cisco Systems, Inc. v. Doe (06/23/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/24-856_kjfm.pdf).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-242. `637fca3f-6a43-5cb6-99d1-dfb440e633d9`

- Present date: `2026-05-01 15:27:36.030163`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Kevin O'Leary's "Stratos" Data Center Project in Box Elder County, Utah, Face a Formal Legal Challenge or Government Moratorium by June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after April 30, 2026 (00:00 UTC) and before June 1, 2026 (23:59 UTC), either of the following occurs:

1. **Legal Challenge:** A formal lawsuit or legal petition is filed in any Utah state court (including the Utah District Courts or Utah Supreme Court, searchable via the Utah State Courts Xchange at https://www.utcourts.gov/xchange/) or any U.S. federal court, specifically seeking to halt, delay, enjoin, or invalidate the approval, permitting, or development of the Stratos/Wonder Valley data center project in Box Elder County, Utah. The filing must name as a defendant or respondent at least one of: O'Leary Digital, West GenCo, the Military Installation Development Authority (MIDA), Box Elder County, or the State of Utah, in connection with this project.

2. **Government Moratorium:** An official, binding action—such as a vote, resolution, ordinance, or executive order—is enacted by the Box Elder County Commission, the Utah Governor's Office, or the Utah State Legislature that explicitly pauses, suspends, or prohibits the development, construction, or permitting of the Stratos/Wonder Valley data center project for a specified or indefinite period. A mere delay or tabling of a vote does not constitute a moratorium; the action must affirmatively impose a halt on the project.

This question resolves NO if neither condition is met by 23:59 UTC on June 1, 2026.

**Resolution Sources:** Resolution will be determined by checking the Utah State Courts Xchange (https://www.utcourts.gov/xchange/), the official Utah Governor's newsroom (https://governor.utah.gov/newsroom/), Box Elder County Commission official meeting minutes, and/or credible reporting from The Salt Lake Tribune (https://www.sltrib.com/), the Associated Press, or Reuters.

**Pre-cutoff background**

Kevin O'Leary's company, O'Leary Digital, is developing a massive "hyperscale" data center project known as "Stratos" (also called "Wonder Valley") in Box Elder County, Utah. At full buildout, the project would span approximately 40,000 acres and require up to 9 gigawatts of power capacity—more than double Utah's current total electricity consumption of roughly 4 gigawatts ['Hyperscale' data center project in Utah - The Salt Lake Tribune](https://www.sltrib.com/news/2026/04/25/hyperscale-data-center-may-be/).

As of May 1, 2026, the project has received approval from the Military Installation Development Authority (MIDA) board, which passed resolutions to advance the project with tax incentives and infrastructure support ['Hyperscale' data center project in Utah - The Salt Lake Tribune](https://www.sltrib.com/news/2026/04/25/hyperscale-data-center-may-be/). However, the project still requires final approval from the Box Elder County Commission. A vote originally scheduled for late April 2026 was postponed after local officials expressed frustration at being "blindsided" by the project's massive scale and the extent of state involvement through MIDA [Utah Planning Commission delays decision on Kevin O'Leary ...](https://www.datacenterdynamics.com/en/news/utah-planning-commission-delays-decision-on-kevin-oleary-backed-data-center-project/). The Box Elder County Commission rescheduled the vote to May 4, 2026 [Utah Planning Commission delays decision on Kevin O'Leary ...](https://www.datacenterdynamics.com/en/news/utah-planning-commission-delays-decision-on-kevin-oleary-backed-data-center-project/).

There is significant community opposition regarding environmental impacts (water and energy usage) and the tax incentives offered. Governor Spencer Cox has publicly supported the project and dismissed concerns about resource usage. No formal legal challenge or government moratorium has been filed or enacted as of May 1, 2026 ['Hyperscale' data center project in Utah - The Salt Lake Tribune](https://www.sltrib.com/news/2026/04/25/hyperscale-data-center-may-be/) [Utah Planning Commission delays decision on Kevin O'Leary ...](https://www.datacenterdynamics.com/en/news/utah-planning-commission-delays-decision-on-kevin-oleary-backed-data-center-project/). The project's developers have sought expedited approval processes, which opponents argue would bypass full public review.

**Exact later resolution packet**

The question resolves NO because neither a qualifying Legal Challenge nor a Government Moratorium occurred within the window of April 30, 2026 to June 1, 2026 (23:59 UTC).

LEGAL CHALLENGE — NOT MET:
- The main opposition activity was administrative, not judicial. The Box Elder Accountability Referendum (BEAR) group filed referendum APPLICATIONS with the county (early-mid May 2026), not a lawsuit in court. These are citizen referendum petitions, not lawsuits/legal petitions filed in a Utah state or federal court naming O'Leary Digital, West GenCo, MIDA, Box Elder County, or the State of Utah.
- On May 28, 2026, the Box Elder County Attorney (Stephen R. Hadfield) rejected the referendum applications, ruling the commission's resolutions were administrative (not legislative) and therefore not legally referable to voters [7bec44].
- After the rejection, organizers said they PLANNED to appeal to Utah's 1st District Court but had NOT yet filed. The Salt Lake Tribune (published May 31, 2026) reported organizer Brenna Williams said the group "will file within a week" — i.e., no court filing had occurred as of May 31, 2026, the last reporting date before the June 1 deadline [c77b1e]. The Utah News Dispatch (May 27 and May 28) similarly described the legal action only as prospective ("Friday we either print packets or we go to court"; "vowed to take their application to court") with no record of an actual filing [0994ae, 7bec44].
- Thousands of water-rights "protests" were filed with the Utah Division of Water Rights, but those are administrative objections to water-rights change applications (and the applications were withdrawn May 7 and again late May), not lawsuits in court [e1eb44]. They do not satisfy the criterion.

GOVERNMENT MORATORIUM — NOT MET:
- Box Elder County Commission voted UNANIMOUSLY on May 4, 2026 to APPROVE/advance the project (the opposite of a moratorium) [e1eb44].
- Governor Cox issued an executive order on May 29, 2026 directing agencies to apply a "higher bar" / evaluation framework for data centers, but it did NOT pause, suspend, or prohibit the Stratos/Wonder Valley project. Reporting noted it "seems to reiterate the status quo" and gave agencies no additional authority; it was a directive for future evaluation, not a halt [723411, e1eb44].
- Senate President Stuart Adams sent a letter (around June 1) urging a 75% size reduction, but a request/letter is not a binding moratorium action [e1eb44].
- A legislative interim committee voted only to STUDY data-center impacts — again not a binding halt [e1eb44].

Sources checked include the specified resolution sources: Box Elder County official postings (boxeldercountyut.gov), Salt Lake Tribune (sltrib.com), Utah News Dispatch, KUER, and KSL. No evidence of a court filing before the June 1, 2026 deadline was found in any of these.

Key URLs:
- https://www.sltrib.com/news/politics/2026/05/31/box-elder-county-organizers-plan/ (organizers "will file within a week"; no suit filed as of May 31) [c77b1e]
- https://utahnewsdispatch.com/2026/05/28/box-elder-county-data-center-referendum-denied/ (referendum applications rejected; legal challenge only prospective) [7bec44]
- https://utahnewsdispatch.com/2026/05/27/print-packets-or-go-to-court-say-organizers-of-stratos-project-referendum/ [0994ae]
- https://www.sltrib.com/news/2026/05/19/kevin-oleary-data-center-timeline/ (timeline; May 4 approval, May 29 Cox order, no lawsuit/moratorium) [e1eb44]
- https://www.sltrib.com/news/environment/2026/05/29/utah-governor-issues-order-protect/ (Cox order not a project-specific moratorium) [723411]

Therefore, by 23:59 UTC June 1, 2026, neither condition was satisfied → NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-243. `2526089f-a45a-520b-922a-77db0ca808e5`

- Present date: `2026-05-12 16:19:12.214454`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Canada win the gold medal at the 2026 IIHF Men's World Championship?

**Resolution criteria**

This question resolves **Yes** if Canada wins the [gold medal](https://en.wikipedia.org/wiki/Gold_medal) at the [2026 IIHF Men's World Championship](https://en.wikipedia.org/wiki/2026_IIHF_World_Championship), meaning Canada wins the championship final game.

This question resolves **No** if any other team wins the gold medal.

**Resolution source:** The official IIHF tournament results page at [https://www.iihf.com/en/events/2026/wm/standings/final](https://www.iihf.com/en/events/2026/wm/standings/final). The gold medal game is scheduled for May 31, 2026 (approximately 19:15 UTC). If the result is disputed or delayed, credible sports reporting (e.g., [Reuters](https://www.reuters.com), [AP News](https://apnews.com), [TSN](https://www.tsn.ca)) may also be used.

**Cancellation or non-completion:** If the 2026 IIHF Men's World Championship is canceled, abandoned, or not completed by July 1, 2026 (UTC), such that no gold medal is awarded, this question resolves **No**.

**Pre-cutoff background**

The [2026 IIHF Men's World Championship](https://en.wikipedia.org/wiki/2026_IIHF_World_Championship) is the annual top-level international men's ice hockey tournament organized by the [International Ice Hockey Federation (IIHF)](https://en.wikipedia.org/wiki/International_Ice_Hockey_Federation). The tournament takes place from May 15 to May 31, 2026, in Zurich and Fribourg, Switzerland, with the [gold medal](https://en.wikipedia.org/wiki/Gold_medal) game scheduled for May 31, 2026.

**Canada's current standing:** As of the most recent IIHF World Ranking (updated May 26, 2025), Canada is ranked **3rd** in the world with 3,935 points, behind the United States and Switzerland [World Ranking - IIHF](https://www.iihf.com/worldranking). At the [2025 IIHF World Championship](https://en.wikipedia.org/wiki/2025_IIHF_World_Championship), Canada finished **5th** overall after being upset by Denmark 2–1 in the quarterfinals — widely considered one of the biggest upsets in IIHF World Championship history.

**NHL playoff influence:** A critical factor for Canada's competitiveness is the availability of NHL players. The IIHF World Championship overlaps with the NHL Stanley Cup playoffs, and Canadian NHL players only become available once their teams are eliminated. The timing and number of eliminations of Canadian-heavy NHL teams by mid-to-late May significantly affects the talent pool available to Hockey Canada. Early-round playoff exits by teams with many Canadian stars can substantially boost Canada's roster, while deep playoff runs by those teams limit availability.

**Historical context:** Canada has won the IIHF World Championship 28 times (most of any nation), most recently in 2024. However, winning gold in any given year is far from certain — Canada has also had several early exits, including the 2025 quarterfinal loss. With 16 teams competing in the tournament, Canada must navigate group play and then win three consecutive elimination games (quarterfinal, semifinal, final) to claim gold.

**Exact later resolution packet**

The question asks whether Canada won the gold medal at the 2026 IIHF Men's World Championship. It resolves NO.

Evidence:
- The official IIHF resolution source page (https://www.iihf.com/en/events/2026/wm/standings/final) shows Finland (FIN) won the gold medal, Switzerland (SUI) took silver, and Canada finished 4th [1571b5].
- The IIHF event home page (iihf.com/en/events/2026/wm) confirms the gold medal game was "Switzerland vs Finland," and the bronze medal game was "Canada vs Norway" (Google snippet).
- The IIHF news article "Helenius scores the golden goal" (https://www.iihf.com/en/events/2026/wm/news/74787/gmg) reports: "Konsta Helenius scored the golden goal at 10:42 of the first overtime period to give Finland a 1-0 victory over Switzerland" for the World Championship title (Google snippet).
- The IIHF schedule/results page (https://www.iihf.com/en/events/2026/wm/schedule) shows the bronze medal game on 31 May: CAN 2, NOR 3 (F/OT), i.e. Canada lost the bronze medal game to Norway in overtime, placing 4th (Google snippet).
- Independent corroboration: FloHockey article (https://www.flohockey.tv/articles/15964446-helenius-scores-the-golden-goal-for-finland-defeats-switzerland-in-zurich) confirms Finland defeated Switzerland in the gold medal game.

The tournament was completed and a gold medal was awarded before the July 1, 2026 deadline. Since Finland (not Canada) won the gold medal, the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-244. `176cc95c-b8b8-52d7-b766-f8302668278c`

- Present date: `2026-05-14 05:14:21.354114`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Supreme Court rule in favor of the Trump administration in Trump v. Cook (Federal Reserve Board firing case) by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the Supreme Court of the United States issues a final opinion or order in *Trump v. Cook* (Docket No. 25A312) that **reverses the lower court's preliminary injunction** and holds that the President has the legal authority to remove Lisa Cook from the Federal Reserve Board of Governors—i.e., a ruling in favor of the Trump administration on the merits of the firing power question.

This question resolves **No** if any of the following occur by 11:59 PM Eastern Time on July 1, 2026:

1. The Supreme Court issues a final opinion or order that **affirms** the lower court's preliminary injunction or otherwise holds that the President lacks the authority to remove Cook, ruling against the administration on the merits.
2. The Supreme Court **dismisses** the case on procedural grounds (e.g., [standing](https://en.wikipedia.org/wiki/Standing_(law)), [mootness](https://en.wikipedia.org/wiki/Mootness), or [ripeness](https://en.wikipedia.org/wiki/Ripeness)), or issues a ruling that does not reach the merits of the presidential firing power question. Such a disposition would not constitute a ruling "in favor of" the administration.
3. The Supreme Court **has not issued any ruling** in the case by the end of the day (11:59 PM Eastern Time) on July 1, 2026.

**Primary resolution source:** The [Opinions of the Court](https://www.supremecourt.gov/opinions/opinions.aspx) page of the Supreme Court of the United States, supplemented by the case docket at https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/25a312.html. Credible reporting from Reuters, AP, NYT, or SCOTUSblog (https://www.scotusblog.com/cases/trump-v-cook/) may also be used to confirm the ruling.

**Pre-cutoff background**

In August 2025, President Donald Trump attempted to remove Federal Reserve Governor Lisa Cook from the [Federal Reserve Board of Governors](https://en.wikipedia.org/wiki/Federal_Reserve_Board_of_Governors), citing allegations of mortgage fraud [Trump v. Cook - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Cook). Under the [Federal Reserve Act](https://en.wikipedia.org/wiki/Federal_Reserve_Act), Board members may only be removed "[for cause](https://www.law.cornell.edu/wex/for_cause)"—a legal standard generally requiring misconduct or neglect of duty, as opposed to "[at-will](https://en.wikipedia.org/wiki/At-will_employment)" removal at the President's discretion.

Cook refused to resign and challenged the removal in court. On September 9, 2025, U.S. District Court Judge Jia Cobb issued a [preliminary injunction](https://en.wikipedia.org/wiki/Preliminary_injunction) blocking the firing. The D.C. Circuit Court of Appeals upheld this injunction [Trump v. Cook - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Cook). The Trump administration then filed an emergency appeal to the Supreme Court.

The Supreme Court (Docket No. 25A312) deferred the emergency request and scheduled oral arguments for January 21, 2026 [Trump v. Cook - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Cook). During oral arguments, multiple justices—including conservatives—appeared skeptical of the administration's claim that the President has broad authority to fire Fed governors, with one conservative justice warning that the administration's interpretation could "shatter" Federal Reserve independence [Trump v. Cook - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Cook).

As of May 13, 2026, the case has been argued but no decision has been issued [Trump v. Cook (25A312) - SCOTUSblog](https://www.scotusblog.com/cases/trump-v-cook/). The Supreme Court's current term ends in late June 2026, and a decision is expected by then. The outcome will set a major precedent on presidential power over independent federal agencies and the scope of the [unitary executive theory](https://en.wikipedia.org/wiki/Unitary_executive_theory).

**Exact later resolution packet**

The question resolves NO (0).

WHAT HAPPENED: On June 29, 2026 — before the July 1, 2026 (11:59 PM ET) deadline — the Supreme Court issued its ruling in Trump v. Cook (Docket No. 25A312). By a 5-4 vote, the Court DENIED the government's application for a stay of the district court's preliminary injunction, allowing Lisa Cook to remain on the Federal Reserve Board of Governors while her legal challenge proceeds. The opinion was delivered by Chief Justice Roberts, joined by Justices Sotomayor, Kagan, Kavanaugh, and Jackson; Justices Thomas, Alito (joined by Gorsuch), and Barrett dissented [a254ab].

WHY THIS IS NO (checklist-by-checklist):
1. Correct case/docket: The ruling is the official Supreme Court opinion in Trump v. Cook, Docket No. 25A312, published at https://www.supremecourt.gov/opinions/25pdf/25a312_5468.pdf and reflected on the docket at https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/25a312.html [a254ab, f01703].

2. Injunction NOT reversed: The Court did not reverse the lower court's preliminary injunction. By denying the stay, the injunction blocking Cook's removal remained in effect. The Court did NOT hold that the President has legal authority to remove Cook — the precise requirement for a YES. Instead, it held the government was not likely to succeed and that the President failed to afford Cook the statutorily required procedural protections (notice and an opportunity to respond) [a254ab]. Reuters similarly reports the Court "blocked President Donald Trump from removing Federal Reserve Governor Lisa Cook," ruling against the administration [eee948].

3. Not a procedural dismissal, but resolves NO either way: The Court did not dismiss on standing, mootness, or ripeness. Per resolution criterion #1, an order affirming/leaving in place the injunction and holding the President lacks authority to remove Cook resolves NO. Per criterion #2, any ruling not reaching the merits in the administration's favor also resolves NO. The Court decided on the "narrow ground" of failure to provide procedural protections and explicitly stated it did not resolve the ultimate question of whether the President can remove Cook for cause [a254ab]. Under any reading, the administration did NOT prevail.

4. Timing: The ruling was issued June 29, 2026, comfortably before the July 1, 2026 11:59 PM ET deadline, so criterion #3 (no ruling issued) does not apply — but the ruling that was issued went against the administration [a254ab, eee948].

5. Official source URL: https://www.supremecourt.gov/opinions/25pdf/25a312_5468.pdf (official opinion); docket at https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/25a312.html; SCOTUSblog case page https://www.scotusblog.com/cases/trump-v-cook/ ("On June 29, 2026, the court denied the application. Judgment: Application for stay denied, 5-4, in an opinion by John Roberts on Jun 29, 2026.") [f01703].

6. Merits question: The Court did NOT rule in the administration's favor on the presidential firing power. It expressly decided the application on the narrow procedural-protections ground and did not hold the President possesses the authority to remove Cook [a254ab]. This satisfies criterion #2's NO condition (ruling that does not reach the merits in the administration's favor) as well as criterion #1 (leaving the injunction in place / holding the President lacks authority as applied).

The requirement for YES — a ruling that REVERSES the injunction AND holds the President has legal authority to remove Cook — was not met. The Court did the opposite. Resolution: NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-245. `f659c90b-c7cf-5f75-a2d5-a5f22cdd7944`

- Present date: `2026-05-29 07:03:21.519961`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the UN Security Council adopt a new resolution specifically addressing the Gaza ceasefire or disarmament between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the [UN Security Council](https://en.wikipedia.org/wiki/United_Nations_Security_Council) formally adopts (i.e., passes by the required voting threshold without a veto by any permanent member) at least one new [resolution](https://en.wikipedia.org/wiki/United_Nations_Security_Council_resolution) on or after May 12, 2026, and by 11:59 PM UTC on July 1, 2026, whose title or operative text contains at least one of the following keywords: "ceasefire," "disarmament," "truce," or "hostilities," AND also references "Gaza" in the title or text.

"Passing" a resolution means it is formally adopted by the UN Security Council per its procedural rules (requiring at least 9 affirmative votes out of 15 members with no veto by a permanent member on substantive matters).

"Specifically addressing" means the resolution's title or operative text must contain (a) the word "Gaza" AND (b) at least one of: "ceasefire," "disarmament," "truce," or "hostilities."

The primary resolution source is the official UN Security Council page for adopted resolutions: [https://main.un.org/securitycouncil/en/content/resolutions-0](https://main.un.org/securitycouncil/en/content/resolutions-0). If this page is not yet updated, credible reporting from major news agencies (e.g., [Reuters](https://www.reuters.com), [AP News](https://apnews.com), [UN News](https://news.un.org)) confirming the adoption and content of the resolution will suffice.

If no such resolution is adopted by 11:59 PM UTC on July 1, 2026, this question resolves as **No**.

**Pre-cutoff background**

The [UN Security Council](https://en.wikipedia.org/wiki/United_Nations_Security_Council) (UNSC) is the principal organ of the United Nations responsible for the maintenance of international peace and security, composed of 15 members including five permanent members (China, France, Russia, the United Kingdom, and the United States) who each hold veto power over substantive [resolutions](https://en.wikipedia.org/wiki/United_Nations_Security_Council_resolution).

Regarding Gaza, the UNSC adopted Resolution 2803 in November 2025, which endorsed a "Comprehensive Plan to End the Gaza Conflict" as part of a US-backed peace framework [Bahrain and US float Security Council resolution on the Strait of ...](https://news.un.org/en/story/2026/05/1167464). In January 2026, the US announced the start of Phase II of this plan. As of May 2026, the ceasefire in Gaza remains tenuous, punctuated by airstrikes and shelling, with soaring humanitarian needs. The Security Council has heard updates on transitional governance structures and reconstruction efforts in Gaza [Resolutions adopted by the Security Council in 2026](https://main.un.org/securitycouncil/en/content/resolutions-adopted-security-council-2026).

As of May 13, 2026, the UNSC has adopted resolutions in 2026 on topics including the Red Sea (S/RES/2812), Cyprus (S/RES/2815), and South Sudan (S/RES/2820), among others [Resolutions adopted by the Security Council in 2026](https://main.un.org/securitycouncil/en/content/resolutions-adopted-security-council-2026). Additionally, Bahrain and the US circulated a draft resolution on the Strait of Hormuz on May 7, 2026, following a Russian and Chinese veto of a similar resolution in April 2026 [Bahrain and US float Security Council resolution on the Strait of ...](https://news.un.org/en/story/2026/05/1167464). The political dynamics at the Council remain complex, with veto threats shaping outcomes on Middle East issues.

Historically, UNSC resolutions on Israel-Palestine are frequently subject to US vetoes, though the current US-led peace framework has shifted dynamics. The question of whether a new Gaza-specific resolution will be adopted depends on whether the deteriorating ceasefire triggers sufficient pressure for Council action, and whether the US would support or veto such a measure given its own diplomatic framework.

**Exact later resolution packet**

RESOLUTION: NO (0)

The question resolves YES only if, between May 12, 2026 and 11:59 PM UTC July 1, 2026, the UN Security Council formally ADOPTED (≥9 votes, no P5 veto) at least one new resolution whose title or operative text contains "Gaza" AND at least one of "ceasefire," "disarmament," "truce," or "hostilities." No such resolution was adopted.

COMPLETE LIST OF RESOLUTIONS ADOPTED IN THE WINDOW (numbers are sequential; 2820 was adopted 30 April 2026, before the window; 2825 was the highest by 1 July 2026):
- S/RES/2821 (29 May 2026) — Renewal of South Sudan sanctions regime (press.un.org SC/16374; globalr2p; UN Digital Library record 4115073).
- S/RES/2822 (15/16 June 2026) — Extension of the UNAMA (Afghanistan) mandate for one year, until 17 June 2027 (unama.unmissions.org).
- S/RES/2823 (June 2026) — Accountability for crimes against UN peacekeepers (press.un.org SC/16395).
- S/RES/2824 (25 June 2026) — Renewal of the UN Disengagement Observer Force (UNDOF, Golan Heights) mandate until 31 December 2026 (press.un.org SC/16398; ungeneva.org).
- S/RES/2825 (30 June 2026) — Extension of the Democratic Republic of the Congo (DRC) sanctions regime for one year (press.un.org SC/16403; china.org.cn; UN transcripts 10188).

None of these five resolutions addresses Gaza; none contains "Gaza" plus one of the required keywords. They concern South Sudan, Afghanistan, UN peacekeeper accountability, the Golan Heights, and the DRC respectively.

ON GAZA SPECIFICALLY: The only Gaza-related Council activity in the window was a debate/open briefing. The Council "debated conditions in Gaza at the request of its 10 elected members" on 18 June 2026 amid concern over the worsening humanitarian crisis [Security Council - the United Nations](https://main.un.org/securitycouncil/en). Security Council Report's "What's in Blue" preview (published 17 June 2026) describes this strictly as an open humanitarian briefing on Gaza scheduled for 18 June 2026, with no draft resolution on a Gaza ceasefire, disarmament, truce, or hostilities being negotiated or voted; it notes the Council's last formal action on the matter remained Resolution 2803 of November 2025 [The Middle East, including the Palestinian Question](https://www.securitycouncilreport.org/whatsinblue/2026/06/the-middle-east-including-the-palestinian-question-briefing-on-the-humanitarian-situation-in-gaza-3.php). No Gaza resolution was voted on or adopted between May 12 and July 1, 2026 [Security Council - the United Nations](https://main.un.org/securitycouncil/en) [The Middle East, including the Palestinian Question](https://www.securitycouncilreport.org/whatsinblue/2026/06/the-middle-east-including-the-palestinian-question-briefing-on-the-humanitarian-situation-in-gaza-3.php).

Because no qualifying resolution meeting BOTH keyword conditions was formally adopted by the deadline, the criterion "If no such resolution is adopted by 11:59 PM UTC on July 1, 2026, this question resolves as No" applies. The question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-246. `38c0c297-ef77-576f-aed0-377904438aaf`

- Present date: `2026-05-14 07:57:22.418704`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the FAA issue an Amended Type Certificate for the Boeing 737 MAX 7 by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the Federal Aviation Administration (FAA) issues an Amended Type Certificate for the Boeing 737 MAX 7 (model 737-7) on or after May 12, 2026, and on or before July 1, 2026, at 23:59 UTC.

The resolution will be determined by checking the FAA's [Dynamic Regulatory System (DRS) Type Certificate Data Sheets page](https://drs.faa.gov/browse/TCDSMODEL/doctypeDetails) [Type Certificate Data Sheets (TCDS) - Dynamic Regulatory System](https://drs.faa.gov/browse/TCDSMODEL/doctypeDetails) for an updated TCDS entry covering the 737-7 model. Alternatively, an official FAA press release published at the [FAA Newsroom](https://www.faa.gov/newsroom) confirming issuance of the certificate will also suffice.

If no Amended Type Certificate for the 737-7 appears in the DRS or is announced by the FAA by 23:59 UTC on July 1, 2026, this question resolves **No**.

**Pre-cutoff background**

The Boeing 737 MAX 7 is the smallest variant of the 737 MAX family. Its certification has been repeatedly delayed due to regulatory scrutiny following the 737 MAX groundings and an unresolved engine anti-ice design fix. An Amended Type Certificate (ATC) is the FAA's formal approval for a major change to an existing type-certificated aircraft design, issued under [14 CFR Part 21](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-21). The FAA describes this process on its [Original Design Approval Process page](https://www.faa.gov/aircraft/air_cert/design_approvals/orig_des_approv_proc) [Original Design Approval Process | Federal Aviation Administration](https://www.faa.gov/aircraft/air_cert/design_approvals/orig_des_approv_proc).

In July 2025, Boeing faced a setback that pushed MAX 7 and MAX 10 certification into 2026 [Boeing 737 MAX certification - Wikipedia](https://en.wikipedia.org/wiki/Boeing_737_MAX_certification). As of April 21, 2026, the FAA administrator stated the agency has not identified issues that would delay certification beyond 2026. Boeing's Q1 2026 earnings call confirmed the company expects certification of both the MAX 7 and MAX 10 "later" in 2026, with deliveries beginning in 2027. Southwest Airlines, the launch customer, expects MAX 7 certification around August 2026. Boeing CFO has indicated certification is on track for the second half of 2026.

As of May 13, 2026, the FAA has **not** issued an Amended Type Certificate for the Boeing 737 MAX 7 [Boeing 737 MAX certification - Wikipedia](https://en.wikipedia.org/wiki/Boeing_737_MAX_certification). Industry expectations center on mid-to-late summer 2026, making a July 1 cutoff genuinely uncertain — estimated probability is roughly 15–30%.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if the FAA issued an Amended Type Certificate for the Boeing 737 MAX 7 (model 737-7) between May 12, 2026 and July 1, 2026 (23:59 UTC), verifiable via the FAA DRS TCDS page or an FAA Newsroom press release. Every source available near and up to the July 1, 2026 deadline confirms the certificate was NOT yet issued:

- Reuters, "US, Europe near approval of Boeing 737 MAX 7, 10 airplanes" (June 17, 2026): FAA Deputy Administrator Chris Rocheleau stated the FAA was in the "final stages" of certifying the MAX 7, describing remaining work as "dotting i's and crossing t's" — i.e., certification had not yet been granted [b4f37d]. URL: https://www.reuters.com/business/aerospace-defense/us-europe-near-approval-boeing-737-max-7-10-airplanes-2026-06-17/

- Maaal, "FAA is nearing certification of the Boeing 737 Max 7" (published/updated around June 29, 2026): reports the FAA was only "nearing" certification, not that it had issued it [f4c948]. URL: https://maaal.com/en/news/details/faa-is-nearing-certificat/

- The FAA Newsroom (checked as the resolution source, page state as of July 1, 2026): contains no press release announcing issuance of an Amended Type Certificate for the 737-7; listed items ranged through June 30, 2026 with no such announcement [b17f39]. URL: https://www.faa.gov/newsroom

- Wikipedia, "Boeing 737 MAX certification" (last edited July 1, 2026): still describes the 737 MAX 7 certification as pushed into 2026 and pending, with no record of an issued Amended Type Certificate [89c217]. URL: https://en.wikipedia.org/wiki/Boeing_737_MAX_certification

Corroborating context: Southwest Airlines (the launch customer) and Boeing leadership repeatedly stated expectations of certification "this summer" / around August 2026, with deliveries in 2027 — consistent with the certificate not existing by July 1, 2026.

Because neither of the two designated resolution sources (FAA DRS TCDS or FAA Newsroom) shows an Amended Type Certificate for the 737-7 issued within the May 12–July 1, 2026 window, and all contemporaneous reporting confirms it was still pending, the question resolves NO. This is a direct (non-conditional) binary question, so no annulment applies.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-247. `4c71352e-6e16-509c-ac5b-b3ddb814f1fd`

- Present date: `2026-05-02 09:48:31.897728`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Iran seize or detain a commercial container vessel in the Strait of Hormuz between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves YES if, between 00:00 UTC on May 1, 2026 and 23:59 UTC on June 1, 2026, Iranian state-affiliated forces (including the IRGC Navy, Iranian Navy, or other Iranian military/paramilitary forces) seize or detain at least one commercial container vessel within the Strait of Hormuz.

Definitions:

- **Strait of Hormuz**: The waterway connecting the Persian Gulf and the Gulf of Oman, as defined by the Wikipedia article at https://en.wikipedia.org/wiki/Strait_of_Hormuz — approximately bounded by 26°36′N 56°30′E at its narrowest point, extending from the Persian Gulf entrance to the Gulf of Oman.

- **Seize or detain**: Iranian armed personnel physically board the vessel, or Iranian military forces compel the vessel (through threat or use of force) to divert to an Iranian port or anchorage, and maintain control or custody of the vessel for a minimum of 6 hours. A vessel merely being ordered to stop and then released within 6 hours does not qualify.

- **Commercial container vessel**: A merchant vessel classified as a "container ship" under the IMO ship type classification (see https://www.imo.org/), meaning a vessel designed primarily for the carriage of containers. This excludes tankers, bulk carriers, general cargo ships, and military vessels.

**Resolution source**: Credible reporting from at least one major international news agency (Reuters, AP, BBC, or Al Jazeera) or an official advisory from UKMTO (https://www.ukmto.org/) confirming the seizure or detention. The event must occur on or after May 1, 2026 (00:00 UTC). Prior seizures (including the April 22, 2026 seizures of MSC Francesca and Epaminondas) do not count.

If no such seizure is confirmed by 23:59 UTC on June 1, 2026, this question resolves NO.

**Pre-cutoff background**

The Strait of Hormuz (approximately 26°36′N 56°30′E) is the narrow waterway connecting the Persian Gulf to the Gulf of Oman, bordered by Iran to the north and Oman/UAE to the south [Strait of Hormuz - Wikipedia](https://en.wikipedia.org/wiki/Strait_of_Hormuz). Since February 28, 2026, the strait has been the site of a major crisis stemming from the broader 2026 Iran war. Iran has largely blocked commercial shipping through the strait, and the U.S. Navy has imposed a counter-blockade on Iranian ports, creating a "dual blockade" situation [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis).

Iran's Islamic Revolutionary Guard Corps (IRGC) Navy has actively boarded, attacked, and seized merchant vessels transiting the strait. On April 22, 2026, Iranian forces seized two container ships — the MSC Francesca (Panama-flagged, MSC-operated) and the Epaminondas — marking the most prominent container vessel seizures during the crisis [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis). As of late April 2026, approximately 20,000 seafarers and 2,000 ships remain stranded in the Persian Gulf due to the blockade [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis).

Prior to the current crisis, Iran had a history of seizing commercial vessels, including the MSC Aries in 2024 [Strait of Hormuz - Wikipedia](https://en.wikipedia.org/wiki/Strait_of_Hormuz). The current situation is far more severe, with Iran actively restricting all transit and periodically seizing vessels. However, the situation remains fluid — temporary ceasefires and negotiations (such as the Islamabad Talks) have occurred, and the intensity of seizures could change rapidly depending on diplomatic developments [2026 Strait of Hormuz crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis).

Resolution monitoring sources include the United Kingdom Maritime Trade Operations (UKMTO) at https://www.ukmto.org/ and reporting from Reuters, AP, and BBC.

**Exact later resolution packet**

The question resolves NO. It requires that, between 00:00 UTC May 1, 2026 and 23:59 UTC June 1, 2026, Iranian forces seize or detain (board/divert and hold ≥6 hours) at least one commercial CONTAINER vessel within the Strait of Hormuz. The prominent April 22, 2026 container-ship seizures (MSC Francesca and Epaminondas) are explicitly excluded by the resolution criteria.

Reviewing the authoritative "List of ships attacked by Iran" in the Wikipedia "2026 Strait of Hormuz crisis" article (last updated 2026-05-27), the complete set of May 2026 incidents was [ea5520, 7e105c]:
- 3 May: unidentified bulk carrier (status unknown); Barakah (Liberia, oil tanker) — damaged
- 4 May: HMM Namu (Panama, cargo ship) — damaged; JV Innovation (Marshall Islands, chemical tanker) — damaged
- 5 May: CMA CGM San Antonio (Malta, CONTAINER ship) — only DAMAGED by a projectile, NOT seized/captured
- 8 May: Ocean Koi (Barbados, oil TANKER) — captured
- 10 May: Safesea Neha (bulk carrier) — minor damage
- 13 May: Haji Ali (India, cargo ship) — sank
- 14 May: Hui Chuan (Honduras, FISHERY RESEARCH vessel) — captured

Crucially, the only vessels actually CAPTURED/SEIZED by Iran in May 2026 were an oil tanker (Ocean Koi) and a fishery research vessel (Hui Chuan) — neither is a container ship. The only container ship involved (CMA CGM San Antonio) was merely damaged by a projectile, which does not meet the "seize or detain" definition (no boarding/diversion + ≥6h custody) [ea5520].

The May 14 seizure off the UAE coast (reported by UKMTO and covered by LA Times/Times of Israel) involved an unnamed vessel that sources did not classify as a container ship; the LA Times referenced it in the context of oil tankers, and Times of Israel noted UKMTO did not name or classify the ship — so it cannot satisfy the strict "container ship" requirement [7c71c1, 838dc2]. The separate seizure (Hui Chuan, fishery research vessel) is also excluded by type.

Searches for late-May (28–31) and June 1 incidents surfaced no report of Iran seizing a container vessel; coverage of that period concerned the continuing blockade, US strikes on Bandar Abbas, and the announced winding-down of the US blockade, not any new Iranian container-ship seizure.

Therefore no qualifying commercial container vessel seizure/detention occurred in the May 1–June 1, 2026 window, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-248. `73e9ffcb-bcb1-5fd9-9c99-055d6eb018dd`

- Present date: `2026-05-15 13:18:34.839357`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Crown Prosecution Service (CPS) announce criminal charges against any living individual in connection with the Mohamed Al Fayed abuse investigation by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026 (00:00 UTC) and on or before July 1, 2026 (23:59 UTC), the Crown Prosecution Service (CPS) publicly announces that it has authorized criminal charges against at least one living individual in connection with the Mohamed Al Fayed abuse investigation (Operation Cornpoppy).

Key definitions:

- **"Criminal charges"**: A formal charge brought by the CPS, or by police following CPS authorization, accusing an individual of a criminal offense under the laws of England and Wales.
- **"Individual"**: A natural person who is alive at the time of the announcement. This explicitly excludes Mohamed Al Fayed, who died in August 2023.
- **"In connection with the Mohamed Al Fayed abuse investigation"**: Charges relating to the facilitation, enabling, or cover-up of alleged sexual offenses or human trafficking attributed to or associated with Mohamed Al Fayed, as investigated under Operation Cornpoppy or any successor investigation.

The announcement must be verifiable via at least one of the following sources:
- An official CPS press release or statement on the CPS newsroom (https://www.cps.gov.uk/news)
- Reporting from major credible news outlets such as BBC News (https://www.bbc.co.uk/news), The Guardian (https://www.theguardian.com/uk-news), or Reuters (https://www.reuters.com)

If no such announcement is made by 23:59 UTC on July 1, 2026, the question resolves as **No**.

**Pre-cutoff background**

The Metropolitan Police Service (MPS) is conducting Operation Cornpoppy, investigating allegations of sexual abuse, rape, and human trafficking by the late Mohamed Al Fayed, who died in August 2023. More than 400 allegations of sexual misconduct dating back to 1977 have been made against him, involving over 150 victims [https://www.bbc.com/news/articles/c2lrwv5p7e7o](https://www.bbc.com/news/articles/c2lrwv5p7e7o).

As of May 13, 2026, the investigation has progressed significantly but no charges have been announced:

- In February–March 2026, three women were interviewed under caution by detectives on suspicion of aiding and abetting rape, sexual assault, and human trafficking for sexual exploitation [https://www.bbc.com/news/articles/c2lrwv5p7e7o](https://www.bbc.com/news/articles/c2lrwv5p7e7o).
- A man in his 60s was also interviewed under caution regarding allegations of human trafficking and facilitating rape [https://www.theguardian.com/uk-news/2026/may/07/met-police-officers-investigated-handling-mohamed-al-fayed-complaints](https://www.theguardian.com/uk-news/2026/may/07/met-police-officers-investigated-handling-mohamed-al-fayed-complaints).
- In May 2026, the Independent Office for Police Conduct (IOPC) launched an investigation into one serving and four former Metropolitan Police officers over their handling of complaints against Al Fayed [https://www.theguardian.com/uk-news/2026/may/07/met-police-officers-investigated-handling-mohamed-al-fayed-complaints](https://www.theguardian.com/uk-news/2026/may/07/met-police-officers-investigated-handling-mohamed-al-fayed-complaints).
- No arrests or formal charges have been made as of this date.

The Crown Prosecution Service (CPS) is the principal public prosecuting authority in England and Wales. In complex historic abuse cases, the gap between police interviews under caution and a CPS charging decision can be substantial, often taking many months. However, the active pace of the investigation — with multiple individuals interviewed under caution — suggests the police may refer cases to the CPS in the coming weeks or months.

**Exact later resolution packet**

The question resolves NO. It asked whether the CPS would publicly announce authorized criminal charges against at least one LIVING individual in connection with the Mohamed Al Fayed abuse investigation (Operation Cornpoppy) between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), verifiable via CPS newsroom, BBC, The Guardian, or Reuters.

Multiple checks against the allowed sources over the entire resolution window show that no such charges were announced — only interviews under caution and watchdog (IOPC) investigations occurred, which the resolution criteria explicitly distinguish from CPS-authorized charges:

1. The Guardian, dated June 8, 2026 (https://www.theguardian.com/business/2026/jun/08/survivors-abuse-mohamed-al-fayed-harrods-trafficking-investigation): confirms four suspects had been interviewed under caution over the prior ~18 months, but NO formal charges had been announced [053742].

2. BBC News, dated ~May 20, 2026 (https://www.bbc.com/news/articles/cx21knljzv7o): reports the Met investigation into potential facilitators/enablers is ongoing (three women and one man interviewed under caution), IOPC separately investigating officers' handling of complaints, and NO CPS charges announced [4f57a3].

3. The CPS official newsroom (https://www.cps.gov.uk/news), reviewed through July 1, 2026: contains no press release or statement announcing any charges related to Operation Cornpoppy or the Mohamed Al Fayed investigation [3c6ade].

4. BBC News background (https://www.bbc.com/news/articles/ce9gle4m1v3o): confirms Operation Cornpoppy is investigating people who may have facilitated/enabled the offending, but the investigation remained at the pre-charge stage [985521].

No allowed source reported any CPS charging decision during the window. (An Instagram survivor-group statement referring to "Mohamed Al Fayed modern slavery charges" is campaign framing, not a CPS charge announcement, and is not an allowed source; separately, the April 2026 Home Office recognition of a survivor as a modern-slavery victim is an administrative determination, not a criminal charge.) Since no qualifying announcement was made by 23:59 UTC on July 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-249. `3d51e7d6-5057-5265-8abc-d272dacf96f0`

- Present date: `2026-05-15 19:39:47.813050`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Australian eSafety Commissioner initiate formal legal proceedings against at least one social media platform (Facebook, Instagram, TikTok, Snapchat, or YouTube) for non-compliance with the under-16 social media ban under the Online Safety Amendment (Social Media Minimum Age) Act 2024 by July 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026 (00:00 UTC) and on or before July 1, 2026 (23:59 UTC), the Australian eSafety Commissioner initiates formal legal proceedings against at least one of the following platforms: Facebook, Instagram, TikTok, Snapchat, or YouTube (or their parent companies Meta Platforms Inc., ByteDance Ltd., Snap Inc., or Alphabet Inc./Google LLC).

"Formal legal proceedings" is defined as one or more of the following specific legal actions taken under the Online Safety Amendment (Social Media Minimum Age) Act 2024:
- Filing a statement of claim or originating application in the Federal Court of Australia seeking civil penalties; or
- Issuing a civil penalty notice or infringement notice under the Online Safety Act 2021 (as amended).

Evidence must come from an official announcement by the eSafety Commissioner (https://www.esafety.gov.au/newsroom/media-releases), court filings, or credible reporting from major news outlets (e.g., Reuters, ABC, The Guardian Australia).

The question resolves NO if no such formal legal proceedings are initiated by 23:59 UTC on July 1, 2026, or if the Commissioner only issues warnings, compliance notices, or information-gathering notices without commencing court action or issuing civil penalty/infringement notices.

**Pre-cutoff background**

In November 2024, Australia passed the Online Safety Amendment (Social Media Minimum Age) Act 2024, amending the Online Safety Act 2021 to prohibit children under 16 from holding accounts on designated "age-restricted social media platforms." The ban took effect on December 10, 2025, requiring platforms to take "reasonable steps" to prevent under-16s from creating or maintaining accounts [Social media age restrictions - eSafety Commissioner](https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions). Platforms face civil penalties of up to 150,000 penalty units (currently A$49.5 million) for non-compliance [Social media age restrictions - eSafety Commissioner](https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions).

As of March 31, 2026, the eSafety Commissioner identified "major gaps" in platform enforcement and announced active investigations into five platforms: Facebook, Instagram, Snapchat, TikTok, and YouTube [https://www.euronews.com/next/2026/03/31/australia-warns-social-media-platforms-of-major-gaps-in-under-16-ban-enforcement](https://www.euronews.com/next/2026/03/31/australia-warns-social-media-platforms-of-major-gaps-in-under-16-ban-enforcement). The Commissioner's compliance update noted specific "poor practices" including allowing unlimited attempts to pass age assurance methods and lacking effective mechanisms for reporting underage accounts [https://www.euronews.com/next/2026/03/31/australia-warns-social-media-platforms-of-major-gaps-in-under-16-ban-enforcement](https://www.euronews.com/next/2026/03/31/australia-warns-social-media-platforms-of-major-gaps-in-under-16-ban-enforcement). By March 2026, approximately 4.7 million accounts had been removed or restricted, with over 300,000 additional accounts blocked, yet two-thirds of teenagers were reportedly still on the banned platforms.

The eSafety Commissioner stated her office would decide whether to pursue formal legal action by "mid-year" 2026 [https://www.euronews.com/next/2026/03/31/australia-warns-social-media-platforms-of-major-gaps-in-under-16-ban-enforcement](https://www.euronews.com/next/2026/03/31/australia-warns-social-media-platforms-of-major-gaps-in-under-16-ban-enforcement). The Commissioner has the power to seek civil penalties in the Federal Court of Australia against non-compliant platforms [Social media age restrictions - eSafety Commissioner](https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions).

Resolution source: The eSafety Commissioner's official media releases page (https://www.esafety.gov.au/newsroom/media-releases) and credible news outlets such as Reuters (https://www.reuters.com), the ABC, or The Guardian Australia.

**Exact later resolution packet**

The question resolves NO. It required that, between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), the Australian eSafety Commissioner initiate "formal legal proceedings" — defined narrowly as either (a) filing a statement of claim/originating application in the Federal Court seeking civil penalties, or (b) issuing a civil penalty/infringement notice under the Online Safety Act — against at least one of Facebook, Instagram, TikTok, Snapchat, or YouTube (or their parents) specifically for non-compliance with the under-16 social media ban.

Evidence establishes that no such action occurred within the window:

1. The eSafety Commissioner's official media releases page shows no filing or civil penalty/infringement notice against any of the five platforms for the under-16 ban between May 12 and July 1, 2026. The five platforms were only "flagged for compliance issues" on March 31, 2026, with the office "continuing to gather evidence necessary to inform potential enforcement action." The May–June 2026 releases concern unrelated matters (e.g., a 21 May 2026 penalty against X Corp over a child-sexual-exploitation transparency notice — not one of the five platforms and not the under-16 ban; actions against "nudify" services) [0354fb].

2. An ABC News report dated June 30, 2026 explicitly states that "no social media company has been fined," and that the government is instead introducing new legislation to strengthen the Commissioner's information-gathering powers and double the maximum penalty — indicating the matter remained at the investigation/information-gathering stage, not formal legal proceedings [274066].

3. A Prime Minister's Office media release (c. June 27–28, 2026) confirms the Commissioner is still "actively investigating" the five platforms and that new legislation is being introduced to support "more effective investigation and potential enforcement action" — with no mention of any Federal Court filing or civil penalty/infringement notice having been issued [a2ffa2].

Because the Commissioner only issued/continued warnings and investigations (and pursued unrelated enforcement against X Corp) rather than commencing court action or issuing a civil penalty/infringement notice against Facebook, Instagram, TikTok, Snapchat, or YouTube under the Social Media Minimum Age provisions during the resolution window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-250. `904b532e-f454-52bf-9f55-8027103c5ab5`

- Present date: `2026-05-02 23:31:30.327173`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the SEC approve Nasdaq's proposed rule change to list the VanEck JitoSOL ETF by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026 and by 11:59 PM ET on June 1, 2026, the SEC issues an order approving Nasdaq's proposed rule change (filed as Form 19b-4, Federal Register Document 2026-05475) to list and trade shares of the VanEck JitoSOL ETF under Nasdaq Rule 5711(d).

This question resolves **No** if:
- The SEC has not issued an approval order by 11:59 PM ET on June 1, 2026, OR
- The SEC issues an order disapproving the proposed rule change, OR
- The SEC institutes proceedings to determine whether to approve or disapprove the proposed rule change (which would extend the timeline beyond June 1, 2026), OR
- The proposal is withdrawn.

**Key definitions:**
- "SEC approval" refers specifically to an order approving the proposed rule change filed under Section 19(b)(1) of the Securities Exchange Act of 1934 and Rule 19b-4 thereunder. This is distinct from the S-1 registration statement effectiveness (which is a separate requirement for the fund to actually begin trading). For this question, only the 19b-4 approval is required.
- "Liquid staking token (LST)" refers to a token (JitoSOL) that represents staked SOL on the Jito protocol plus accrued staking rewards, as distinct from a standard spot Solana ETF that holds SOL directly.

**Resolution source:** The SEC's order will be published on [SEC.gov](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=vaneck+jitosol&CIK=&type=&dateb=&owner=include&count=40&search_text=&action=getcompany) and/or in the [Federal Register](https://www.federalregister.gov/). The original Notice of Filing is available at: https://www.federalregister.gov/documents/2026/03/20/2026-05475/self-regulatory-organizations-the-nasdaq-stock-market-llc-notice-of-filing-of-proposed-rule-change

**Pre-cutoff background**

On March 10, 2026, Nasdaq filed a proposed rule change (Form 19b-4) with the U.S. Securities and Exchange Commission (SEC) to list and trade shares of the VanEck JitoSOL ETF under Nasdaq Rule 5711(d) (Commodity-Based Trust Shares). The SEC published a Notice of Filing in the Federal Register on March 20, 2026 (Document No. 2026-05475), initiating the formal review period. Under Section 19(b)(1) of the Securities Exchange Act of 1934, the SEC has an initial 45-day window from Federal Register publication to approve or disapprove the proposal, placing the initial deadline around May 4, 2026. However, the SEC may extend this period by up to an additional 45 days (for a total of 90 days), or institute further proceedings.

The VanEck JitoSOL ETF is structurally distinct from existing spot Solana ETFs. Rather than holding SOL directly, it would hold JitoSOL, a liquid staking token (LST) issued by the Jito protocol on Solana. JitoSOL represents staked SOL plus accumulated staking rewards. This is the first U.S. exchange filing for a liquid staking token ETP, introducing novel regulatory considerations around the classification of staking rewards and the LST mechanism [https://tokentax.co/blog/solana-etf](https://tokentax.co/blog/solana-etf).

Several spot Solana ETFs and ETPs already trade in the U.S. under tickers such as BSOL, GSOL, TSOL, SOEZ, QSOL, VSOL, and SSK [https://tokentax.co/blog/solana-etf](https://tokentax.co/blog/solana-etf). Additionally, on April 7, 2026, Nasdaq filed a separate immediate effectiveness notice related to the VanEck JitoSOL ETF. The SEC has generally adopted a more permissive stance toward crypto ETFs in 2025-2026, but the novel LST structure could prompt additional scrutiny or delay.

**Exact later resolution packet**

The question resolves NO (0).

The question asked whether the SEC would issue an order APPROVING Nasdaq's proposed rule change (File No. SR-NASDAQ-2026-016, Form 19b-4) to list the VanEck JitoSOL ETF under Nasdaq Rule 5711(d), on or after May 1, 2026 and by 11:59 PM ET on June 1, 2026.

Key evidence: On May 1, 2026, the SEC issued a "Notice of Designation of a Longer Period for Commission Action" on this exact proposed rule change. That order found it appropriate to designate a longer period and set June 18, 2026 as the new date by which the Commission shall approve, disapprove, or institute proceedings to determine whether to disapprove the proposal. This order was published in the Federal Register on May 6, 2026 (Document No. 2026-08787, Vol. 91, No. 87) [[PDF] Federal Register/Vol. 91, No. 87/Wednesday, May 6, 2026/Notices](https://www.govinfo.gov/content/pkg/FR-2026-05-06/pdf/2026-08787.pdf). URL: https://www.govinfo.gov/content/pkg/FR-2026-05-06/pdf/2026-08787.pdf (also at https://www.federalregister.gov/documents/2026/05/06/2026-08787/).

Therefore, the SEC did NOT issue an approval order by the June 1, 2026 deadline — it instead extended the timeline. The resolution criteria explicitly specify a NO resolution if "the SEC has not issued an approval order by 11:59 PM ET on June 1, 2026." That condition is satisfied [[PDF] Federal Register/Vol. 91, No. 87/Wednesday, May 6, 2026/Notices](https://www.govinfo.gov/content/pkg/FR-2026-05-06/pdf/2026-08787.pdf).

Why this is not -1 (annulled): The question is not a conditional ("IF A THEN B"); it is a straightforward binary on whether the approval order was issued by the deadline. The original Notice of Filing (Document 2026-05475, Federal Register March 20, 2026) confirms the filing was validly initiated and the question's premise (the 19b-4 filing exists and was under review) is correct, so the question is well-posed and resolvable. The SEC's extension order confirms no withdrawal occurred and the matter remained pending. Hence the question resolves NO rather than being annulled.

Distinction between 19b-4 and S-1: The resolution depends only on the 19b-4 rule-change approval order, which was not issued by June 1, 2026 — independent of any S-1 effectiveness. No such 19b-4 approval order exists within the May 1–June 1, 2026 window.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-251. `d2697b3c-a4df-54bf-8a9e-a3b161aa0ecc`

- Present date: `2026-05-29 03:25:42.031801`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will at least one coalition party publicly threaten to leave the Israeli governing coalition over a defense spending or budget-related dispute between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (00:00 UTC) and before July 1, 2026 (23:59 UTC), at least one party currently in the Israeli governing coalition publicly threatens to leave the coalition over a defense spending or budget-related dispute. Otherwise it resolves **No**.

**Definitions:**

1. **"Coalition party"** means any of the five parties in the 37th government of Israel as listed on the [Knesset factions page](https://main.knesset.gov.il/en/mk/apps/mklobby/main/current-knesset-mks/factions) and the [Wikipedia article on the 37th government](https://en.wikipedia.org/wiki/Thirty-seventh_government_of_Israel): **Likud, Shas, Otzma Yehudit, Religious Zionist Party, and New Hope**. If a party joins or leaves the coalition before the resolution date, the list is evaluated as of the date the threat is made.

2. **"Publicly threaten to leave"** means at least one of the following:
   - The party's chairman or an officially designated spokesperson issues a public statement (press conference, official social media post, interview with a news outlet, or letter to the Prime Minister) explicitly stating that the party intends to, or is considering, withdrawing from the coalition or bringing a no-confidence vote.
   - The party formally submits a coalition resignation letter or votes against the government in a no-confidence motion.
   - A senior party leader (cabinet minister or faction chair) publicly issues a formal ultimatum conditioning continued coalition membership on specific demands.
   - Statements by individual backbench MKs without endorsement from the party leader or spokesperson do not qualify.

3. **"Defense spending or budget-related dispute"** means the stated reason for the threat must primarily concern one or more of the following: the size or allocation of the defense/military budget; supplementary defense appropriations; overall state budget parameters (e.g., deficit targets, tax policy, or spending cuts to fund defense); or the allocation of budgetary resources to military-related matters such as conscription-linked funding. This excludes disputes primarily about non-budgetary matters such as judicial reform, territorial policy, hostage negotiations, or ceasefire terms, unless those disputes are explicitly framed in budgetary terms by the threatening party.

**Resolution sources:** Credible reporting from at least two of the following outlets:
- [The Times of Israel](https://www.timesofisrael.com/topic/israeli-politics/)
- [Haaretz](https://www.haaretz.com/israel-news/politics)
- [The Jerusalem Post](https://www.jpost.com/israel-news/politics-and-diplomacy)
- Reuters or AP

If no qualifying threat is reported by July 1, 2026 (23:59 UTC), the question resolves **No**.

**Pre-cutoff background**

As of May 13, 2026 (UTC), the 37th government of Israel, led by Prime Minister Benjamin Netanyahu, holds a 60-seat majority in the 120-seat Knesset following the departure of United Torah Judaism (UTJ) in July 2025 [Thirty-seventh government of Israel - Wikipedia](https://en.wikipedia.org/wiki/Thirty-seventh_government_of_Israel). The current coalition consists of five parties: Likud, Shas, Otzma Yehudit, the Religious Zionist Party, and New Hope [Thirty-seventh government of Israel - Wikipedia](https://en.wikipedia.org/wiki/Thirty-seventh_government_of_Israel).

The Knesset approved the 2026 state budget on March 30, 2026, by a vote of 62–55 [Knesset approves 2026 budget, Israel's largest ever, sending ...](https://www.timesofisrael.com/knesset-approves-2026-budget-israels-largest-ever-sending-billions-to-haredi-institutions/). The budget totals approximately NIS 850.6 billion (~$271 billion), with a record defense allocation that was revised upward from NIS 112 billion to NIS 144 billion (~$45.8 billion) amid the ongoing war with Iran [Knesset approves 2026 budget, Israel's largest ever, sending ...](https://www.timesofisrael.com/knesset-approves-2026-budget-israels-largest-ever-sending-billions-to-haredi-institutions/). The budget process was marked by significant friction, particularly over ultra-Orthodox military conscription exemptions and funding for Haredi institutions. As of May 12, 2026, the spiritual leader of the Degel HaTorah faction has called for the dissolution of the Knesset, with a vote expected in coming days [Knesset approves 2026 budget, Israel's largest ever, sending ...](https://www.timesofisrael.com/knesset-approves-2026-budget-israels-largest-ever-sending-billions-to-haredi-institutions/). Opposition leaders Bennett and Lapid have announced a joint party to challenge the coalition in anticipated elections.

Coalition threats are a recurring feature of Israeli multi-party politics. The narrow 60-seat majority and ongoing wartime fiscal pressures create conditions where smaller parties may leverage their positions. However, the rally-around-the-flag effect during active conflict can also suppress coalition fractures.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if, between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), a coalition party (Likud, Shas, Otzma Yehudit, Religious Zionist Party, or New Hope) publicly threatened to leave the coalition PRIMARILY over a defense-spending or budget-related dispute. No such qualifying threat occurred; the coalition crises in the window were over (a) the Haredi military draft/conscription exemption LAW and (b) the US–Iran ceasefire deal — both explicitly non-budgetary matters.

KEY EVIDENCE:

1. Budget already resolved before the window. Israel's 2026 state budget (NIS 850.6bn, with record defense spending) passed on March 30, 2026 — before the resolution window opened. So there was no live "state budget" fight during May 12–July 1. (Established in the question description and corroborated by Wikipedia's timeline [Thirty-seventh government of Israel - Wikipedia](https://en.wikipedia.org/wiki/Thirty-seventh_government_of_Israel).)

2. The dominant May–June crisis was CONSCRIPTION, not budget. On May 12, 2026, the Degel HaTorah faction of UTJ (a party that had already LEFT the coalition in July 2025, so not even a listed coalition party) called for dissolving the Knesset "because of the coalition's failure to pass a law enshrining the decades-old exemption of Haredi yeshiva students from military service." The Times of Israel explicitly states this "is about the military draft/conscription law. It is not about the defense budget, state budget, or funding." [Haredi factions push to dissolve Knesset, increasing likelihood of ...](https://www.timesofisrael.com/haredi-factions-back-dissolving-knesset-increasing-chance-for-early-elections/) Haaretz (May 12, 2026) likewise reports the threat was triggered by Netanyahu's decision to shelve the "military draft exemption bill," framed as a policy dispute, not a budgetary one. [Top Haredi Leader Orders Coalition Collapse After Netanyahu ...](https://www.haaretz.com/israel-news/israel-politics/2026-05-12/ty-article/.premium/haredi-parties-threaten-coalition-after-netanyahu-shelves-draft-exemption-bill/0000019e-1bd3-d907-ad9e-1fff59d20000) Wikipedia confirms the May 20/June 2 Knesset self-dissolution votes were driven by "continued deadlock within the coalition over a Haredi conscription bill," with no budget/defense-spending threat noted. [Thirty-seventh government of Israel - Wikipedia](https://en.wikipedia.org/wiki/Thirty-seventh_government_of_Israel) Under the criteria, conscription-policy disputes over the exemption LAW do not qualify (only "conscription-linked funding" would, and the threats were not framed that way).

3. The June Iran-ceasefire crisis was about ceasefire/security terms — explicitly excluded. Around June 15, 2026, Finance Minister Smotrich (RZP) and National Security Minister Ben Gvir (Otzma Yehudit) publicly panned the US–Iran ceasefire deal, but they did NOT threaten to leave the coalition and framed their opposition in security/operational terms (Israel's "ability to defend itself"), not the defense/state budget. [Smotrich and Ben Gvir pan US-Iran deal, say Israel should defy it](https://www.timesofisrael.com/liveblog_entry/smotrich-and-ben-gvir-pan-us-iran-deal-say-israel-should-defy-it/) The criteria explicitly exclude disputes over "ceasefire terms" unless framed budgetarily, which they were not.

4. Other candidate events ruled out:
- Smotrich's coalition legislative boycott over IDF-reservist tax compensation occurred in November 2025 (before the window) and was a legislative boycott, not a threat to leave the coalition. [Smotrich to resume voting with coalition after compromise on ...](https://www.timesofisrael.com/smotrich-to-resume-voting-with-coalition-after-compromise-on-reservist-compensation/)
- A Sa'ar/New Hope threat that "the coalition could collapse" concerned a West Bank sovereignty law and is dated June 2022 — outside the window and not budgetary. [Sa'ar's New Hope said holding talks with Likud over potential new ...](https://www.timesofisrael.com/saars-new-hope-said-holding-talks-with-likud-over-potential-new-government/)

CONCLUSION: No coalition party issued a qualifying public threat to leave the coalition over a defense-spending or budget-related dispute during May 12–July 1, 2026. The two real coalition threats/crises in the window were over the Haredi draft law (conscription policy) and the Iran ceasefire (security terms), both of which are excluded by the resolution criteria. Resolves NO.

SOURCES (URLs):
- https://www.timesofisrael.com/haredi-factions-back-dissolving-knesset-increasing-chance-for-early-elections/ [Haredi factions push to dissolve Knesset, increasing likelihood of ...](https://www.timesofisrael.com/haredi-factions-back-dissolving-knesset-increasing-chance-for-early-elections/)
- https://www.haaretz.com/israel-news/israel-politics/2026-05-12/ty-article/.premium/haredi-parties-threaten-coalition-after-netanyahu-shelves-draft-exemption-bill/0000019e-1bd3-d907-ad9e-1fff59d20000 [Top Haredi Leader Orders Coalition Collapse After Netanyahu ...](https://www.haaretz.com/israel-news/israel-politics/2026-05-12/ty-article/.premium/haredi-parties-threaten-coalition-after-netanyahu-shelves-draft-exemption-bill/0000019e-1bd3-d907-ad9e-1fff59d20000)
- https://www.timesofisrael.com/liveblog_entry/smotrich-and-ben-gvir-pan-us-iran-deal-say-israel-should-defy-it/ [Smotrich and Ben Gvir pan US-Iran deal, say Israel should defy it](https://www.timesofisrael.com/liveblog_entry/smotrich-and-ben-gvir-pan-us-iran-deal-say-israel-should-defy-it/)
- https://en.wikipedia.org/wiki/Thirty-seventh_government_of_Israel [Thirty-seventh government of Israel - Wikipedia](https://en.wikipedia.org/wiki/Thirty-seventh_government_of_Israel)
- https://www.timesofisrael.com/smotrich-to-resume-voting-with-coalition-after-compromise-on-reservist-compensation/ [Smotrich to resume voting with coalition after compromise on ...](https://www.timesofisrael.com/smotrich-to-resume-voting-with-coalition-after-compromise-on-reservist-compensation/)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-252. `06893f2c-815c-5f61-82fa-3d8f46628ba5`

- Present date: `2026-05-14 02:30:59.156484`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will San Francisco Proposition C receive more total "Yes" votes than Proposition D in the June 2, 2026 election?

**Resolution criteria**

This question resolves **Yes** if the total number of "Yes" votes cast for Proposition C exceeds the total number of "Yes" votes cast for Proposition D in the June 2, 2026 San Francisco Consolidated Statewide Direct Primary Election, as reported by the San Francisco Department of Elections.

It resolves **No** if Proposition D receives an equal or greater number of "Yes" votes than Proposition C.

Resolution will be based on official results published by the San Francisco Department of Elections at https://www.sf.gov/election-results (or the legacy URL https://www.sfelections.org/results). Results need not be formally certified; the most recent official count posted by the Department of Elections by the resolution date will be used, provided the Department considers results sufficiently final for reporting (i.e., not a "zero report"). If no results beyond a zero report are available by July 1, 2026, resolution is deferred until results are posted.

**Pre-cutoff background**

San Francisco's June 2, 2026 ballot features two competing business tax measures related to the city's "CEO pay gap" tax — a tax on businesses where the top executive earns more than 100 times the median employee's compensation.

**Proposition C** (backed by the SF Chamber of Commerce and business groups) would raise the gross receipts tax exemption threshold from $5 million to $7.5 million and accelerate a planned tax rate increase from 2028 to 2027. It is projected to *decrease* city revenue by $30–$40 million annually [https://missionlocal.org/2026/05/sf-june-election-2026-ballot/](https://missionlocal.org/2026/05/sf-june-election-2026-ballot/). (Official text: https://www.sf.gov/information/proposition-c-june-2-2026; Ballotpedia: https://ballotpedia.org/San_Francisco,_California,_Measure_C,_Gross_Receipts_Tax_Exemption_and_Top_Executive_Pay_Tax_Increase_Initiative_(June_2026))

**Proposition D** (backed by the SF Labor Council, labor unions, and progressive figures including Bernie Sanders) would increase taxes on businesses subject to the CEO pay gap tax. It is projected to *increase* city revenue by $200–$300 million annually [https://missionlocal.org/2026/05/sf-june-election-2026-ballot/](https://missionlocal.org/2026/05/sf-june-election-2026-ballot/). (Official text: https://www.sf.gov/changes-to-business-tax; Ballotpedia: https://ballotpedia.org/San_Francisco,_California,_Measure_D,_Changes_to_Top_Executive_Pay_Tax_Initiative_(June_2026))

These measures are competing: if both pass, the one receiving more "Yes" votes takes effect while the other is nullified [https://missionlocal.org/2026/05/sf-june-election-2026-ballot/](https://missionlocal.org/2026/05/sf-june-election-2026-ballot/). This makes the relative vote count — not just passage — the decisive outcome. Polls close at 8:00 PM Pacific Time (PT) on June 2, 2026.

**Exact later resolution packet**

Adjudicated: The official SF Department of Elections Final Summary Report (June 25, 2026) for the June 2, 2026 Consolidated Statewide Direct Primary Election lists Measure C with 83,625 YES votes (34.02%) and Measure D with 118,802 YES votes (47.19%). Since Prop D (118,802) received far MORE YES votes than Prop C (83,625), the criterion 'C exceeds D' is false and the question resolves NO. An initial automated pass swapped the two measures' labels; Wikipedia's dedicated Proposition D article independently confirms Prop D = 118,633 Yes (47.18%), and press (KQED, Mission Local) consistently reports the labor/CEO-tax Prop D out-polling the Chamber-backed Prop C. Both measures failed, but D clearly beat C on Yes votes.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-253. `6856f970-2231-525b-8e93-611b0ba4a7a8`

- Present date: `2026-05-14 12:05:17.172482`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the University of California implement a new 'last, best, and final offer' (LBFO) for AFSCME 3299 Service (SX) or Patient Care Technical (EX) bargaining units between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves YES if the University of California formally implements a new last, best, and final offer (LBFO) for either the AFSCME 3299 Service Workers (SX) bargaining unit or the Patient Care Technical Employees (EX) bargaining unit, on or after May 12, 2026, and on or before July 1, 2026.

"Implementation of an LBFO" is defined as either:
1. UC issuing a formal public announcement or press release stating that it is unilaterally implementing the terms of a new last, best, and final offer for one or both units; OR
2. UC filing a notice of implementation with the California Public Employment Relations Board (PERB) for one or both units.

For clarity, this question concerns a **new** LBFO implementation distinct from the June 2025 implementation. Continuation of terms already imposed under the June 2025 LBFO does not count.

If the parties reach a tentative agreement or ratified contract for both units before any new LBFO is implemented, this question resolves NO.

**Resolution sources:**
- UC Press Room labor negotiations page: https://www.universityofcalifornia.edu/press-room/labor-negotiations
- UCnet labor news page: https://ucnet.universityofcalifornia.edu/labor-news/
- PERB case search portal: https://www.perb.ca.gov/case-search/

If any of these sources confirm a new LBFO implementation for the SX or EX unit within the specified window, the question resolves YES. Otherwise, it resolves NO on July 1, 2026.

**Pre-cutoff background**

The University of California (UC) has been in protracted contract negotiations with AFSCME Local 3299, which represents approximately 37,000 workers across two systemwide bargaining units: Service Workers (SX) and Patient Care Technical Employees (EX). Bargaining began in January 2024, and contracts for both units expired in 2024 [Labor negotiations | University of California](https://www.universityofcalifornia.edu/press-room/labor-negotiations).

In June 2025, after declaring impasse and exhausting impasse procedures, UC unilaterally implemented specific terms of its last, best, and final offer (LBFO) for both the SX and EX bargaining units. That LBFO included annual across-the-board wage increases of 5% in 2025, 4% in 2026, and 3% in 2027 and 2028 [Labor negotiations | University of California](https://www.universityofcalifornia.edu/press-room/labor-negotiations). AFSCME filed unfair labor practice (ULP) charges in response, alleging that UC bargained in bad faith and unlawfully imposed terms.

As of May 13, 2026, negotiations remain unresolved. AFSCME 3299 has announced an open-ended systemwide ULP strike beginning May 14, 2026. On May 11, 2026, UC enhanced its economic proposal, but AFSCME declined the offer [Labor negotiations | University of California](https://www.universityofcalifornia.edu/press-room/labor-negotiations). The situation remains highly fluid: UC could choose to declare a new impasse and implement a second LBFO, or the parties could reach a tentative agreement, or the strike could continue without a new LBFO being issued.

An LBFO is a legal mechanism under California public sector labor law. After bargaining reaches impasse and mediation/fact-finding procedures are exhausted, an employer may unilaterally implement the terms of its final offer. Such implementation is subject to review by the Public Employment Relations Board (PERB).

**Exact later resolution packet**

RESOLUTION: NO (0).

The question asks whether UC implemented a NEW last, best, and final offer (LBFO) for the AFSCME 3299 Service (SX) or Patient Care Technical (EX) units between May 12, 2026 and July 1, 2026 — distinct from the June 2025 LBFO. It resolves NO if a tentative agreement/ratified contract for both units is reached before any new LBFO is implemented.

KEY EVIDENCE (from the designated resolution sources and corroborating outlets):

1. UC's official Press Room labor negotiations page (https://www.universityofcalifornia.edu/press-room/labor-negotiations) confirms UC and AFSCME reached a TENTATIVE CONTRACT DEAL and the strike was AVERTED. The associated release is "UC and AFSCME Reach Tentative Contract Deal; Strike Averted" (https://www.universityofcalifornia.edu/press-room/uc-and-afscme-reach-tentative-contract-deal-strike-averted). The page contains no notice of any NEW unilateral LBFO implementation in the May 12–July 1, 2026 window; it only references the July 2025 implementation [479ad4].

2. UCnet labor news page (https://ucnet.universityofcalifornia.edu/labor-news/), reviewed through its most recent entries (June 22, 2026), contains NO mention of any new LBFO being implemented for the SX or EX units in the window [c07507].

3. AFSCME 3299's own "WE WON!" post (https://afscme3299.org/blog/we-won/, May 14, 2026) states: "After over two years of fighting UC and refusing to give up, our team reached a tentative agreement with UC," covering the SX and EX units the union represents [4be60b].

4. AFSCME 3299's strike-cancellation alert (https://afscme3299.org/media/alert-university-of-california-workers-cancel-strike-after-tentative-agreement-reached/) confirms a tentative agreement was reached late May 13, 2026, and the strike scheduled for May 14, 2026 was cancelled [458a51].

5. Ratification: The tentative agreement was ratified by members (ratification vote May 19–21, 2026; "AFSCME Local 3299 employees vote to ratify contract," Daily Bruin, May 22, 2026). AFSCME 3299 represents both the SX (Service) and EX (Patient Care Technical) units, and the strike authorization/notice was issued for both "EX SX" units — so the deal and ratification covered BOTH units.

CONCLUSION: A tentative agreement covering both the SX and EX units was reached on May 13/14, 2026 — within the window but BEFORE any new LBFO was implemented — and was subsequently ratified. UC did NOT issue any formal public announcement/press release of a new unilateral LBFO, nor is there any PERB notice of a new implementation. The resolution criterion "If the parties reach a tentative agreement or ratified contract for both units before any new LBFO is implemented, this question resolves NO" is directly satisfied. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-254. `ee5ab35a-c66c-5cac-9cf7-8a3a6c0decf0`

- Present date: `2026-04-30 18:35:50.164302`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the African Union Peace and Security Council issue a new communiqué specifically addressing Somaliland's recognition status between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves as **YES** if the African Union Peace and Security Council (PSC) publishes a new official communiqué or formal decision document, dated on or after April 30, 2026 (00:00 UTC), and no later than June 1, 2026 (23:59 UTC), that specifically addresses Somaliland's recognition status. "Specifically addresses Somaliland's recognition status" means the document must explicitly mention at least one of the following: (a) the word "recognition" in reference to Somaliland, (b) "sovereignty" or "statehood" of Somaliland, or (c) the 2024 Ethiopia-Somaliland Memorandum of Understanding or Israel's recognition of Somaliland.

The document must be:
- An official PSC Communiqué, PSC Press Statement, or PSC Decision (attributed to the Peace and Security Council itself, not merely to the AU Commission Chairperson or the AU Commission spokesperson).
- Published on the AU's official website (https://au.int/en/psc or https://www.peaceau.org/en/psc-communique) or distributed as an official AU document with a PSC document number.

Statements or press releases issued solely by the AU Commission, the AU Commission Chairperson, or other AU organs (e.g., the Assembly, Executive Council) do **not** count.

If no qualifying PSC document is published by 23:59 UTC on June 1, 2026, this question resolves **NO**.

**Pre-cutoff background**

On December 26, 2025, Israel became the first UN member state to formally recognize Somaliland as an independent country. The African Union responded swiftly: on December 26, 2025, the AU Commission Chairperson issued a statement rejecting "any initiative or action aimed at recognizing Somaliland as an independent entity." On January 6, 2026, the AU Peace and Security Council (PSC) held its 1324th meeting at ministerial level and issued a formal communiqué on "the preservation of the sovereignty, territorial integrity, unity and stability of the Federal Republic of Somalia," calling for the immediate revocation of Somaliland's recognition by Israel [Statement by the African Union Commission on Israel's Reported ...](https://au.int/en/pressreleases/20260419/statement-au-commission-israels-reported-decision-regarding-somaliland).

In April 2026, Israel reportedly moved to appoint a diplomatic envoy to Somaliland, prompting a further AU Commission statement on April 19, 2026, which "strongly condemns" Israel's decision, declares "any unilateral recognition of Somaliland is null and void," and reaffirms the AU's position that it "does not recognize Somaliland as an independent state" [Statement by the African Union Commission on Israel's Reported ...](https://au.int/en/pressreleases/20260419/statement-au-commission-israels-reported-decision-regarding-somaliland). This April 19 statement was issued by the AU Commission (the executive/administrative body), not by the Peace and Security Council (the decision-making organ for peace and security matters).

The PSC's most recent communiqué on this topic was from January 6, 2026. Whether the PSC will convene again on this matter and issue a new communiqué during the resolution window depends on further escalation (e.g., Israel opening a mission in Somaliland, other countries following suit, or Somali government requests for AU action). The PSC publishes communiqués at https://www.peaceau.org/en/psc-communique and https://au.int/en/psc. AU press releases are published at https://au.int/en/pressreleases.

**Exact later resolution packet**

Adjudicated: No PSC communiqué in the April 30 – June 1, 2026 window addressed Somaliland's recognition status. The PSC sessions in the window were the 1344th (Lake Chad/Sahel climate), 1346th (African Standby Force), 1347th (Guinea-Bissau), 1348th (Day of Living Together in Peace), and 1349th (21 May 2026), which was on the Fifth Joint Retreat with the APRM and produced the Joint Burayu Declaration on governance/early warning — it does not mention Somaliland. An earlier automated YES rests on a misread search snippet falsely attributing Somaliland content to the 1349th communiqué; the only Somalia-related item in the window was a 16 May AU Commission statement, which is explicitly disqualified because it is not a PSC document.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-255. `6b75272f-6c95-540d-8907-15ce082a0add`

- Present date: `2026-05-14 12:19:13.930580`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will any individual be formally arrested in connection with facilitating Mohamed Al Fayed's alleged sexual abuse between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves YES if, between 00:00 BST on May 12, 2026, and 23:59 BST on July 1, 2026, any individual is formally arrested by the Metropolitan Police or any other UK law enforcement agency in connection with the investigation into individuals who may have facilitated or enabled Mohamed Al Fayed's alleged sexual abuse (the investigation described on the Metropolitan Police Newsroom page: https://news.met.police.uk/news/update-on-investigation-into-individuals-who-may-have-facilitated-or-enabled-offending-by-mohamed-al-fayed-506850).

Key definitions:
- **Formally arrested** means a person has been deprived of their liberty by a police officer and taken into custody, as distinct from a "voluntary interview" or "interview under caution" as defined under the Police and Criminal Evidence Act 1984 (PACE). A voluntary attendance at a police station, or an interview under caution where the suspect is free to leave, does NOT count as a formal arrest.
- **In connection with facilitating Mohamed Al Fayed's alleged sexual abuse** means the arrest relates to the Metropolitan Police's investigation into individuals suspected of enabling, facilitating, or aiding Al Fayed's alleged offending (including but not limited to offences such as human trafficking, aiding and abetting rape, or sexual assault). Arrests of Met officers for misconduct in handling complaints do NOT count.

Resolution will be determined by official statements from the Metropolitan Police Newsroom (https://news.met.police.uk/) or credible reporting from major news outlets such as BBC News (https://www.bbc.com/news), The Guardian (https://www.theguardian.com/), Reuters, or the Associated Press confirming that a formal arrest has taken place within the specified window.

If no such arrest is confirmed by 23:59 BST on July 1, 2026, this question resolves NO.

**Pre-cutoff background**

The Metropolitan Police are conducting a large-scale investigation into individuals who may have facilitated or enabled sexual offending by the late Mohamed Al Fayed, the former owner of Harrods (1985–2010), who died in 2023. As of March 2026, 154 victims had come forward with allegations of sexual assault, rape, sexual exploitation, and human trafficking [UPDATED: Investigation into individuals who may have facilitated or ...](https://news.met.police.uk/news/update-on-investigation-into-individuals-who-may-have-facilitated-or-enabled-offending-by-mohamed-al-fayed-506850).

In late February and early March 2026, three women—aged in their 40s, 50s, and 60s—were interviewed under caution on suspicion of offences including human trafficking, aiding and abetting rape, and sexual assault [Three women interviewed on suspicion of sex trafficking in Al Fayed ...](https://www.bbc.com/news/articles/c2lrwv5p7e7o). A man was also subsequently interviewed under caution in connection with the investigation [UPDATED: Investigation into individuals who may have facilitated or ...](https://news.met.police.uk/news/update-on-investigation-into-individuals-who-may-have-facilitated-or-enabled-offending-by-mohamed-al-fayed-506850). As of the Met's most recent update (March 2026), no arrests had been made [UPDATED: Investigation into individuals who may have facilitated or ...](https://news.met.police.uk/news/update-on-investigation-into-individuals-who-may-have-facilitated-or-enabled-offending-by-mohamed-al-fayed-506850).

Separately, the Independent Office for Police Conduct (IOPC) launched a misconduct investigation into one serving and four former Metropolitan Police officers over their handling of earlier Al Fayed abuse complaints.

In UK policing, an "interview under caution" (conducted under the Police and Criminal Evidence Act 1984, or PACE) is a formal questioning procedure where a suspect is cautioned that they do not have to say anything but that anything they do say may be used in evidence. Crucially, the suspect attends voluntarily or by appointment and is free to leave. A formal arrest, by contrast, involves the deprivation of a person's liberty—typically the suspect is taken into custody and detained at a police station. Arrest represents a significant escalation in investigative confidence and strategy.

**Exact later resolution packet**

The question resolves NO. It asks whether any individual was FORMALLY ARRESTED (deprived of liberty and taken into custody) in connection with the Metropolitan Police investigation into people who may have facilitated/enabled Mohamed Al Fayed's alleged sexual abuse (Operation Cornpoppy), between 00:00 BST May 12 and 23:59 BST July 1, 2026. Arrests of Met officers for misconduct (the separate IOPC investigation) do NOT count, and interviews under caution do NOT count.

Evidence from qualifying sources (Met Police Newsroom, BBC, The Guardian):

1. Metropolitan Police Newsroom's official update page (the exact page named in the resolution criteria) states four people (three women and one man) were interviewed under caution and explicitly that "No arrests have been made" as of its March 2026 update [5dc3de]. URL: https://news.met.police.uk/news/update-on-investigation-into-individuals-who-may-have-facilitated-or-enabled-offending-by-mohamed-al-fayed-506850

2. BBC News (article on MPs raising concerns, dated within the window) confirms only interviews under caution of three women and one man, and no formal arrests [6df5a8]. URL: https://www.bbc.com/news/articles/cx21knljzv7o

3. The Guardian, June 8, 2026, states the Metropolitan Police had "interviewed four suspects under caution" in the 18 months since the investigation opened — no arrests [4a681b]. URL: https://www.theguardian.com/business/2026/jun/08/survivors-abuse-mohamed-al-fayed-harrods-trafficking-investigation

4. The Guardian, June 28, 2026 (only 3 days before the window closes), reporting on Operation Cornpoppy (the facilitators investigation), states that as of the previous week the investigation had interviewed only four people under caution, with no formal arrests. The IOPC complaints referenced concern the separate misconduct investigation into officers, which does not count [d473d5]. URL: https://www.theguardian.com/uk-news/2026/jun/28/complaints-iopc-met-police-mohamed-al-fayed-harrods

Targeted searches specifically for the words "arrest"/"arrested" in connection with the Al Fayed facilitators investigation during May–July 2026 returned no results indicating a formal arrest; the only arrest-related items concerned unrelated matters or the officer-misconduct strand. Because the most recent qualifying source (June 28, 2026) confirms only interviews under caution and no arrests, with only 3 days remaining in the window and no report of any arrest in that period, the antecedent (a formal arrest) did not occur. Per the resolution criteria, if no such arrest is confirmed by 23:59 BST July 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-256. `0fc5a5d8-b59b-514d-81e2-47e4d70333f3`

- Present date: `2026-05-14 04:48:41.045632`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will China lift the suspension on new autonomous vehicle permits before July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 and on or before July 1, 2026 (23:59 Beijing Time, UTC+8), a relevant Chinese government authority — such as the Ministry of Industry and Information Technology (MIIT, https://www.miit.gov.cn/), the Ministry of Transport (MOT, https://www.mot.gov.cn/), or the Ministry of Public Security (MPS, https://www.mps.gov.cn/) — officially announces that the suspension on issuing new autonomous vehicle permits has been lifted, or that the issuance of new AV permits has resumed.

"Lifting the suspension" means that at least one category of new autonomous vehicle permits (e.g., road testing permits, commercial pilot permits, or fleet expansion permits) is once again being accepted or issued by Chinese regulators, as confirmed by either:
1. An official government announcement on one of the above ministry websites, or
2. Credible reporting from major international news outlets such as Reuters (https://www.reuters.com/), Bloomberg (https://www.bloomberg.com/), or the Associated Press (https://apnews.com/).

If no such announcement or credible reporting confirms the lifting of the suspension by 23:59 Beijing Time on July 1, 2026, the question resolves **No**.

**Pre-cutoff background**

On April 29, 2026, Reuters reported that China suspended the issuance of new autonomous vehicle (AV) permits following an incident in which Baidu's Apollo Go robotaxis abruptly stopped operating in Wuhan [https://www.reuters.com/world/asia-pacific/china-suspends-new-autonomous-vehicle-permits-after-baidu-outage-bloomberg-news-2026-04-29/](https://www.reuters.com/world/asia-pacific/china-suspends-new-autonomous-vehicle-permits-after-baidu-outage-bloomberg-news-2026-04-29/). The suspension prevents all companies from adding new robotaxis to existing fleets, launching new pilot projects, or expanding AV operations into new cities. Earlier in April 2026, Chinese authorities had already ordered safety inspections of smart vehicle road tests [https://www.reuters.com/world/asia-pacific/china-suspends-new-autonomous-vehicle-permits-after-baidu-outage-bloomberg-news-2026-04-29/](https://www.reuters.com/world/asia-pacific/china-suspends-new-autonomous-vehicle-permits-after-baidu-outage-bloomberg-news-2026-04-29/). As of May 12, 2026, the suspension remains in effect. The key regulatory bodies involved include the Ministry of Industry and Information Technology (MIIT), the Ministry of Transport (MOT), and the Ministry of Public Security (MPS), which jointly oversee autonomous vehicle testing and deployment permits in China. China has been actively promoting its autonomous driving industry as a strategic technology sector, creating tension between safety concerns and industrial policy goals. The outcome depends on how quickly regulators complete their safety review, the severity of the findings, and political incentives to maintain China's competitiveness in autonomous driving technology.

**Exact later resolution packet**

The question resolves NO. It asked whether, on or after May 12, 2026 and on or before 23:59 Beijing Time on July 1, 2026, a relevant Chinese government authority (MIIT, MOT, or MPS) officially announced that the suspension on issuing new autonomous vehicle (AV) permits had been lifted, or that issuance of new AV permits had resumed — as confirmed by either an official ministry announcement or credible reporting from Reuters, Bloomberg, or the Associated Press.

Background/antecedent (confirmed): The suspension itself was real. On April 29, 2026, Reuters and Bloomberg reported China suspended issuing new AV licenses after Baidu Apollo Go robotaxis abruptly stopped in Wuhan (https://www.reuters.com/world/asia-pacific/china-suspends-new-autonomous-vehicle-permits-after-baidu-outage-bloomberg-news-2026-04-29/ ; https://www.bloomberg.com/news/articles/2026-04-29/china-suspends-new-autonomous-driving-permits-after-baidu-outage). This is not a conditional question, so it resolves on the consequent (was the suspension lifted?) directly.

Evidence that the suspension was NOT lifted during the resolution window (May 12 – July 1, 2026):

1. Bloomberg, June 4, 2026 ("China's Robotaxi Dilemma: How to Lead in AI Without Fueling Unemployment", https://www.bloomberg.com/news/newsletters/2026-06-04/china-s-robotaxi-dilemma-how-to-lead-in-ai-without-fueling-unemployment) — This is a named-outlet (Bloomberg) source dated within the window. It explicitly states that "The Chinese government still isn't issuing new licenses for autonomous vehicles," and that "People familiar with the matter have signaled it might take a while for China to resume handing out new permits, as authorities wait for a full-blown review of the incident." [d65132] This directly confirms the suspension remained in effect well into June 2026.

2. Reuters, May 26, 2026 ("China's Pony.ai says it is unaffected by self-driving car safety review", https://www.reuters.com/world/asia-pacific/chinas-ponyai-says-it-is-unaffected-by-self-driving-car-safety-review-2026-05-26/) — Confirms China "paused approvals for new autonomous vehicle licenses" and that the safety review was still ongoing; no lifting of the national suspension was reported. Pony.ai's claim of being "unaffected" referred to its own existing operations, not a lifting of the permit freeze. [c6f271]

3. EqualOcean, June 29, 2026 (https://equalocean.com/news/2026062921976-china-co-leads-worlds-first-global-autonomous-driving-regulation-shifting) — Reports on the UN's first global technical regulation for autonomous driving (adopted ~June 25, 2026) with China as a co-lead. This concerns international standard-setting, not the lifting of China's domestic permit suspension; it contains no announcement of resumption. [f68e04]

4. TechCrunch, June 21, 2026 (robotaxi scorecard article) — No mention of any lifting of the suspension or resumption of licensing. [e351c8]

5. The June 26, 2026 Xinhua/MIIT announcement found in Chinese-language search results concerns the approval/publication of the UN global technical regulation for autonomous driving systems (全球首个自动驾驶系统全球技术法规获批发布), NOT the lifting of the domestic AV permit suspension. It is not an announcement that new-permit issuance resumed.

No official announcement on the MIIT (miit.gov.cn), MOT (mot.gov.cn), or MPS (mps.gov.cn) websites, nor any Reuters/Bloomberg/AP report, was found stating that any category of new AV permits (road testing, commercial pilot, or fleet expansion) had resumed being accepted or issued during the May 12 – July 1, 2026 window. The most recent within-window named-outlet evidence (Bloomberg, June 4) affirmatively states the suspension was still in place. Per the resolution criteria, absent such confirmation the question resolves NO.

Sources confirming provenance: Bloomberg (a named outlet) [d65132] and Reuters (a named outlet) [c6f271] both report the suspension was ongoing; no official government (MIIT/MOT/MPS) announcement of lifting was located.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):
