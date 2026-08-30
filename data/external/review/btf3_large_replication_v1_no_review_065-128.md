# btf3_large_replication_v1 — realized NO review chunk NO-065–NO-128

> Display chunk of the immutable queue (`btf3_large_replication_v1_no_queue.json`). Review strictly top-to-bottom; stop only when this bucket reaches 128 ACCEPTs overall. Do not skip ahead, reorder, or prefer better-looking questions. A REJECT/UNSURE permanently consumes its queue slot and is never resampled, re-reviewed, or hand-repaired.

All four gates must hold to ACCEPT. On REJECT or UNSURE write exactly one line of reason.

### NO-65. `e2c55fd1-b9c6-58bc-8fab-d85a2d4cecbc`

- Present date: `2026-05-03 03:53:31.122305`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the ASCO 2026 oral presentation of KEYNOTE-942 5-year data (Abstract #9500) report a statistically significant improvement in overall survival for intismeran autogene plus pembrolizumab vs. pembrolizumab alone?

**Resolution criteria**

This question resolves **Yes** if the ASCO 2026 oral presentation for Abstract #9500, or the accompanying official abstract published in the ASCO Meeting Library (https://meetings.asco.org/abstracts-presentations/259570/), or an official press release from Merck (https://www.merck.com/news/) or Moderna (https://www.modernatx.com/), explicitly reports a **statistically significant** improvement in overall survival (OS) for the intismeran autogene plus pembrolizumab arm compared to the pembrolizumab alone arm.

**"Statistically significant" is defined as:** a reported p-value less than 0.05, OR a reported 95% confidence interval for the OS hazard ratio that excludes 1.0.

This question resolves **No** if any of the following occur:
1. The presentation or abstract reports that the OS difference is not statistically significant (p ≥ 0.05 or 95% CI for HR includes 1.0).
2. The presentation or abstract states that OS data remains immature or does not report OS statistical significance.
3. The oral presentation (Abstract #9500) is cancelled, delayed beyond June 1, 2026 (23:59 UTC), or otherwise not publicly available by that date.
4. The presentation fails to explicitly mention whether OS reaches statistical significance.

Resolution will be determined based on information publicly available by June 1, 2026, 23:59 UTC.

**Pre-cutoff background**

The Phase 2b KEYNOTE-942/mRNA-4157-P201 study (NCT03897881) is an ongoing randomized, open-label trial evaluating intismeran autogene (mRNA-4157/V940), a personalized mRNA neoantigen therapy developed by Moderna, in combination with pembrolizumab (KEYTRUDA, an anti-PD-1 checkpoint inhibitor) versus pembrolizumab alone in 157 patients with completely resected high-risk stage III/IV cutaneous melanoma [Moderna & Merck Announce 5-Year Data for Intismeran Autogene in ...](https://www.merck.com/news/moderna-merck-announce-5-year-data-for-intismeran-autogene-in-combination-with-keytruda-pembrolizumab-demonstrated-sustained-improvement-in-the-primary-endpoint-of-recurrence-free-survival-i/).

**Key terms:**
- **Intismeran autogene (mRNA-4157/V940):** A personalized cancer vaccine using mRNA technology to encode up to 34 patient-specific neoantigens. See: https://en.wikipedia.org/wiki/Intismeran_autogene
- **Overall Survival (OS):** The length of time from randomization that patients are still alive. See: https://www.cancer.gov/publications/dictionaries/cancer-terms/def/overall-survival
- **Pembrolizumab (KEYTRUDA):** An anti-PD-1 immune checkpoint inhibitor. See: https://en.wikipedia.org/wiki/Pembrolizumab

**Most recent data (January 20, 2026):** At a median 5-year follow-up, the combination reduced the risk of recurrence or death by 49% versus pembrolizumab alone, with a recurrence-free survival (RFS) hazard ratio of 0.510 (95% CI: 0.294–0.887; one-sided nominal p=0.0075) [Moderna & Merck Announce 5-Year Data for Intismeran Autogene in ...](https://www.merck.com/news/moderna-merck-announce-5-year-data-for-intismeran-autogene-in-combination-with-keytruda-pembrolizumab-demonstrated-sustained-improvement-in-the-primary-endpoint-of-recurrence-free-survival-i/). The January 2026 Merck/Moderna press release did not report overall survival (OS) data or its statistical significance [Moderna & Merck Announce 5-Year Data for Intismeran Autogene in ...](https://www.merck.com/news/moderna-merck-announce-5-year-data-for-intismeran-autogene-in-combination-with-keytruda-pembrolizumab-demonstrated-sustained-improvement-in-the-primary-endpoint-of-recurrence-free-survival-i/). Previous data cuts (3-year update at ASCO 2024) showed clinically meaningful but immature OS trends.

The full abstract (#9500) is scheduled for public release on May 21, 2026, at 5:00 PM EST [5-year update of the KEYNOTE-942 study. - ASCO Meetings](https://meetings.asco.org/abstracts-presentations/259570/). The oral presentation is scheduled for June 1, 2026 at the ASCO Annual Meeting. Moderna will host a live webcast on June 1, 2026, from 6:15–7:15 PM CDT.

This is a genuinely uncertain question: the trial enrolled only 157 patients, OS events are expected to be few given the adjuvant setting, and while RFS is clearly positive, translating this into a statistically significant OS benefit in a small phase 2b trial is challenging. The question is high-stakes for Moderna's oncology franchise.

**Exact later resolution packet**

The question resolves NO because the ASCO 2026 oral presentation of KEYNOTE-942 5-year data (Abstract #9500) did NOT report a statistically significant improvement in overall survival (OS); instead, OS was an exploratory endpoint that showed only a "trend."

Evidence:
- The official Merck/Moderna press release (Jan 20, 2026) reported only the primary RFS endpoint (HR=0.510; 95% CI 0.294–0.887; one-sided nominal p=0.0075) and explicitly stated they planned to present further follow-up data at a future medical meeting; it did not report any OS hazard ratio, CI, or p-value [Moderna & Merck Announce 5-Year Data for Intismeran Autogene in ...](https://www.merck.com/news/moderna-merck-announce-5-year-data-for-intismeran-autogene-in-combination-with-keytruda-pembrolizumab-demonstrated-sustained-improvement-in-the-primary-endpoint-of-recurrence-free-survival-i/).
- Targeted Oncology's coverage of the June 1, 2026 ASCO presentation states the data "included a trend toward improved overall survival (OS)," and that "OS was an exploratory end point as the study was not sufficiently powered for an OS evaluation, and no alpha was assigned to this analysis." No p-value or CI for OS was reported [Adjuvant Intismeran/Pembro Shows Durable Benefit at 5 Years in ...](https://www.targetedonc.com/view/adjuvant-intismeran-pembro-shows-durable-benefit-at-5-years-in-melanoma).
- Moderna's own IR Insights recap of the ASCO 2026 oral presentation describes the OS result only as an "encouraging trend in overall survival compared with pembrolizumab alone," with no statistical significance reported [IR Insights: Recapping Moderna's ASCO 2026 Oral Presentation](https://www.modernatx.com/recapping-moderna-asco-oral-presentation).
- News reports (Reuters, thedermdigest, clinicaltrialsarena) note descriptive OS rates of 92.2% (combination) vs 71.3% (pembrolizumab alone) but characterize OS as an exploratory/trend finding rather than a statistically significant result.

The resolution criteria define "statistically significant" as a reported p-value < 0.05 OR a reported 95% CI for the OS hazard ratio that excludes 1.0. No such statistic was reported for OS. The criteria explicitly state the question resolves NO if the presentation "states that OS data remains immature or does not report OS statistical significance" — which is exactly the case here. Therefore the question resolves NO (0).

Sources: Merck press release (https://www.merck.com/news/moderna-merck-announce-5-year-data-for-intismeran-autogene-in-combination-with-keytruda-pembrolizumab-demonstrated-sustained-improvement-in-the-primary-endpoint-of-recurrence-free-survival-i/); Targeted Oncology (https://www.targetedonc.com/view/adjuvant-intismeran-pembro-shows-durable-benefit-at-5-years-in-melanoma); Moderna IR Insights (https://www.modernatx.com/recapping-moderna-asco-oral-presentation).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-66. `f0c57160-d1d9-552b-9d20-41ea4b4902d0`

- Present date: `2026-05-03 04:40:15.754182`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Christian Horner hold an official role at any F1 team by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, at any point between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), Christian Horner is confirmed to hold or have been announced for an official role at any F1 team officially entered in the 2026 FIA Formula One World Championship.

**Definitions:**
- **"Official role"** means any of the following positions, whether paid or unpaid: Team Principal, CEO, Managing Director, Chief Executive, Technical Director, Consultant, Advisor, or member of the board of directors. An ownership stake alone (without an accompanying operational or advisory role) does not qualify.
- **"F1 team"** means any of the constructors officially entered in the 2026 FIA Formula One World Championship, as listed on the [FIA entry list](https://www.fia.com/regulation/category/110) or [F1.com team profiles](https://www.formula1.com/en/teams).
- The role must be **active or formally announced** during the May 1–June 1, 2026 window. Horner's prior role at Red Bull Racing (which ended in 2025) does not count.

**Resolution sources:** Official press releases or team announcements from the relevant F1 team, or credible reporting from major sports news outlets such as [F1.com](https://www.formula1.com), [BBC Sport](https://www.bbc.com/sport/formula1), [ESPN F1](https://www.espn.com/f1/), [Autosport](https://www.autosport.com), Reuters, or AP.

If no such confirmation exists by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

Christian Horner was fired as Team Principal and CEO of Red Bull Racing in July 2025 after 20 years with the team [Horner gets $100M Red Bull payout, eyes F1 return - sources - ESPN](https://www.espn.com/f1/story/_/id/46344237/christian-horner-officially-leaves-red-bull). He received a settlement payout reported to be in the region of $100 million, with terms that permit him to return to Formula 1 in any capacity starting in the spring of 2026 [Horner gets $100M Red Bull payout, eyes F1 return - sources - ESPN](https://www.espn.com/f1/story/_/id/46344237/christian-horner-officially-leaves-red-bull).

Since his departure, Horner has been linked to several potential F1 roles:

- **Alpine**: As of January 2026, Alpine confirmed that Horner is part of an investor group that has expressed interest in acquiring a stake in the team, following reports that minority shareholder Otro Capital is looking to sell its 24% stake [Alpine clarify rumours over interest from former Red Bull boss Horner](https://www.formula1.com/en/latest/article/alpine-clarify-rumours-over-interest-from-former-red-bull-boss-horner.CQvRv1m7Q6MqsgiTD1cu4). This would potentially give Horner both an ownership stake and a leadership role.

- **Audi**: Following the sudden departure of Audi team principal Jonathan Wheatley in March 2026, Horner has been tipped as a potential replacement. However, significant hurdles remain, including potential conflicts with interim leader Mattia Binotto, who is covering Wheatley's duties, and Horner's reported desire for full control and equity — something Audi may not offer [Could Christian Horner answer Audi's F1 needs after its recent big ...](https://www.crash.net/f1/feature/1092922/1/could-christian-horner-answer-audis-f1-needs-after-its-recent-big-blow).

- **Aston Martin**: Horner has been ruled out as an option for Aston Martin [Could Christian Horner answer Audi's F1 needs after its recent big ...](https://www.crash.net/f1/feature/1092922/1/could-christian-horner-answer-audis-f1-needs-after-its-recent-big-blow).

As of early April 2026, no official appointment has been confirmed. Key uncertainties include the complexity of multi-party negotiations around the Alpine ownership deal, potential leadership conflicts at Audi, and Horner's stated preference for a role with significant control and potential shareholding [Could Christian Horner answer Audi's F1 needs after its recent big ...](https://www.crash.net/f1/feature/1092922/1/could-christian-horner-answer-audis-f1-needs-after-its-recent-big-blow).

**Exact later resolution packet**

The question resolves NO. Between May 1 and June 1, 2026, Christian Horner was NOT confirmed or announced for any qualifying "official role" (Team Principal, CEO, Managing Director, Chief Executive, Technical Director, Consultant, Advisor, or board member) at any F1 team officially entered in the 2026 FIA Formula One World Championship.

Evidence found within the resolution window:

1. ESPN (May 21, 2026) reported Horner was still only "assessing his options for an F1 comeback," with discussions about a potential BYD partnership. The article states "BYD do not appear ready to launch a serious bid any time soon," and notes BYD is a Chinese electric manufacturer "exploring options for entering the sport in some capacity in the future" — i.e., NOT an F1 team entered in 2026. Horner's return "appears to be a way off" with "few other viable options" open to him [fa7ad7].

2. The only confirmed new job Horner took on (per Express, May 21, 2026) is as an adviser to investment company Oakley Capital — an investment firm, NOT an F1 team. This does not satisfy the criteria of an official role at an F1 team entered in 2026 [e7872b].

3. The Alpine situation remained an unresolved ownership-stake negotiation only. As of May 31, 2026, GPFans reported "there is no official confirmation that Horner is interested in the deal at all," and Renault held a veto over the share sale until September. No operational/advisory appointment was made [ea5e46]. Notably, the question explicitly states an ownership stake alone (without an accompanying operational/advisory role) does not qualify.

4. An earlier ESPN piece (March 13, 2026) likewise confirmed Horner was only part of a consortium pursuing a 24% Alpine stake — a negotiation over ownership, not an appointment to any operational/advisory role [ebb14a].

The Audi Team Principal links (from April 2026) were purely speculation/tips by pundits, never an actual appointment, and the only "Exclusive" claiming his Audi appointment was an April 1 piece (April Fools' / unreliable, not an allowed source).

His prior Red Bull Racing role (ended 2025) is explicitly excluded by the resolution criteria.

Since no qualifying official role at a 2026-entered F1 team was active or formally announced during the May 1–June 1, 2026 window, the question resolves NO.

Key sources:
- ESPN (BYD): https://www.espn.com/f1/story/_/id/48826861/christian-horner-targets-formula-1-return-byd-10-months-red-bull-sacking-sources
- Express (Oakley Capital): https://www.express.co.uk/sport/f1-autosport/2208297/christian-horner-new-job-f1
- GPFans (Alpine, May 31): https://www.gpfans.com/en/f1-news/1084825/christian-horner-alpine-price-path-to-f1-return/
- ESPN (Alpine/Mercedes): https://www.espn.com/f1/story/_/id/48193300/christian-horner-route-back-f1-alpine-faces-mercedes-obstacle

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-67. `97cec3a5-eaeb-5fb0-9ef4-20df60713baa`

- Present date: `2026-05-16 16:07:26.326308`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Prime Minister Edi Rama testify before the GJKKO court in the Sali Berisha 'Partizani' corruption trial by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (00:00 CEST) and on or before July 1, 2026 (23:59 CEST), Prime Minister Edi Rama physically appears and provides testimony as a witness before the GJKKO in the "Partizani" trial involving Sali Berisha. Rama is being summoned in his capacity as former Mayor of Tirana regarding the privatization of the "Partizani" sports complex.

This question resolves **No** if Rama does not testify before the GJKKO in the "Partizani" case by July 1, 2026 (23:59 CEST). The court having accepted the summons request or having issued a summons alone is not sufficient — Rama must actually appear and testify.

**Resolution sources:** Credible reporting from BIRN Albania / Balkan Insight (https://balkaninsight.com), Albanian Daily News (https://albaniandailynews.com), Balkan Web (https://www.balkanweb.com/en/), Hashtag.al (https://www.hashtag.al/en/), or other major Albanian or international news outlets (Reuters, AP). Official GJKKO court records may also be consulted if publicly available.

**Pre-cutoff background**

The "Partizani" case is a high-profile corruption trial at Albania's Special Court against Corruption and Organized Crime (GJKKO). Former Prime Minister Sali Berisha and his son-in-law Jamarbër Malltezi are charged with "passive corruption of high-ranking officials," alleging that Berisha took legal and sub-legal actions during his premiership that favored his son-in-law in relation to the privatization of the former "Partizani" sports complex [https://www.hashtag.al/en/index.php/2026/01/26/mbahet-ne-gjkko-seanca-per-ish-kryeministrin-berisha-dhe-dhendrin-e-tij/](https://www.hashtag.al/en/index.php/2026/01/26/mbahet-ne-gjkko-seanca-per-ish-kryeministrin-berisha-dhe-dhendrin-e-tij/).

The defense requested that current Prime Minister Edi Rama be called as a witness, specifically in his capacity as former Mayor of Tirana, regarding actions related to the privatization — including construction permits he allegedly signed [https://www.hashtag.al/en/index.php/2026/01/26/mbahet-ne-gjkko-seanca-per-ish-kryeministrin-berisha-dhe-dhendrin-e-tij/](https://www.hashtag.al/en/index.php/2026/01/26/mbahet-ne-gjkko-seanca-per-ish-kryeministrin-berisha-dhe-dhendrin-e-tij/). On April 15, 2026, the GJKKO accepted the defense's request to summon Rama as a witness [Trial against Berisha for the "Partizani" file, Balla is called ...](https://www.hashtag.al/en/index.php/2026/04/15/gjyqi-ndaj-berishes-per-dosjen-partizani-balla-thirret-si-deshmitar/). SPAK (the Special Prosecution Office) did not oppose the request. As of April 30, 2026, Taulant Balla (head of the SP parliamentary group) testified as a witness, but Rama had not yet appeared before the court [Trial against Berisha for the "Partizani" file, Balla is called ...](https://www.hashtag.al/en/index.php/2026/04/15/gjyqi-ndaj-berishes-per-dosjen-partizani-balla-thirret-si-deshmitar/). Berisha's lawyer has stated that Rama has a legal obligation to appear and testify under oath.

The key uncertainty is whether Rama will actually appear and testify before the GJKKO by the resolution date, given the political sensitivity of a sitting Prime Minister testifying in a corruption trial against a former Prime Minister and opposition leader. Rama could potentially seek delays, challenge the summons, or simply fail to appear.

**Exact later resolution packet**

The question resolves NO: there is no evidence that Prime Minister Edi Rama physically appeared and testified as a witness before the GJKKO in the Sali Berisha "Partizani" trial between May 12, 2026 (00:00 CEST) and July 1, 2026 (23:59 CEST).

Timeline of the 2026 merits trial ("gjyq në themel"), reconstructed from credible/approved Albanian outlets:
- April 30, 2026 (before the resolution window opened): The merits trial began and Taulant Balla testified. When journalists asked whether Rama would appear following his summons, Balla said appearing in court is an "individual responsibility." No confirmation Rama had appeared. (BalkanWeb) ["I hope to come here again for..."/ Balla concludes testimony in the ...](https://www.balkanweb.com/en/shpresoj-te-vij-serish-ketu-per-balla-perfundon-deshmine-ne-gjyqin-per-partizanin-a-do-paraqitet-rama-ne-seance-eshte-pergjegjesi-individuale/)
- May 11, 2026: Witness Albert Xhani testified (boldnews.al/2026/05/11 referenced in [Zbardhet dëshmia e vajzës së Fatos Lubonjës për dosjen " ...](https://boldnews.al/2026/06/22/zbardhet-deshmia-e-vajzes-se-fatos-lubonjes-per-dosjen-partizani/)).
- June 8, 2026: Former Economy Minister Genc Ruli testified (and Violeta Shqevi); the witness that day was Ruli, not Rama. (BalkanWeb) [VIDEO/ Witness in the trial against Berisha for the "Partizani" file ...](https://www.balkanweb.com/en/video-deshmitar-ne-procesin-ndaj-berishes-per-dosjen-partizani-ish-ministri-genc-ruli-shkon-ne-gjkko/); corroborated [Gjyqi për dosjen “Partizani”/ Nis seanca gjyqësore në GJKKO ...](https://dosja.al/politike/gjyqi-per-dosjen-partizani-nis-seanca-gjyqesore-ne-gjkko-berisha-nuk-es-i501344)[Zbardhet dëshmia e vajzës së Fatos Lubonjës për dosjen " ...](https://boldnews.al/2026/06/22/zbardhet-deshmia-e-vajzes-se-fatos-lubonjes-per-dosjen-partizani/).
- June 22, 2026: Former Sports Minister Ylli Pango testified; Berisha absent. Rama did not appear. (Dosja.al) [Gjyqi për dosjen “Partizani”/ Nis seanca gjyqësore në GJKKO ...](https://dosja.al/politike/gjyqi-per-dosjen-partizani-nis-seanca-gjyqesore-ne-gjkko-berisha-nuk-es-i501344); (BoldNews.al) [Zbardhet dëshmia e vajzës së Fatos Lubonjës për dosjen " ...](https://boldnews.al/2026/06/22/zbardhet-deshmia-e-vajzes-se-fatos-lubonjes-per-dosjen-partizani/).

Throughout the window, a succession of other witnesses (Balla, Xhani, Ruli, Shqevi, Pango, Fatos Lubonja's daughter) gave testimony, but Rama did not. The BalkanWeb article page from the April 30 session, whose live news feed extended through July 1, 2026, contains no report of Rama testifying ["I hope to come here again for..."/ Balla concludes testimony in the ...](https://www.balkanweb.com/en/shpresoj-te-vij-serish-ketu-per-balla-perfundon-deshmine-ne-gjyqin-per-partizanin-a-do-paraqitet-rama-ne-seance-eshte-pergjegjesi-individuale/); the June 22 BoldNews and Dosja.al reports likewise show only other witnesses and no Rama appearance [Zbardhet dëshmia e vajzës së Fatos Lubonjës për dosjen " ...](https://boldnews.al/2026/06/22/zbardhet-deshmia-e-vajzes-se-fatos-lubonjes-per-dosjen-partizani/)[Gjyqi për dosjen “Partizani”/ Nis seanca gjyqësore në GJKKO ...](https://dosja.al/politike/gjyqi-per-dosjen-partizani-nis-seanca-gjyqesore-ne-gjkko-berisha-nuk-es-i501344). During June 2026 Rama was preoccupied with large anti-government protests demanding his resignation (Hashtag.al coverage on 2026-06-17/20/24/26), and Malltezi/Berisha's side continued to complain that Rama had still not been brought to testify.

The resolution criteria explicitly state that the court accepting the summons or issuing a summons is NOT sufficient — Rama had to actually appear and testify, which did not occur by the July 1, 2026 deadline. Therefore the question resolves NO (0).

Key source URLs:
- https://www.balkanweb.com/en/video-deshmitar-ne-procesin-ndaj-berishes-per-dosjen-partizani-ish-ministri-genc-ruli-shkon-ne-gjkko/ (June 8, 2026: Genc Ruli, not Rama, testified) [VIDEO/ Witness in the trial against Berisha for the "Partizani" file ...](https://www.balkanweb.com/en/video-deshmitar-ne-procesin-ndaj-berishes-per-dosjen-partizani-ish-ministri-genc-ruli-shkon-ne-gjkko/)
- https://www.balkanweb.com/en/shpresoj-te-vij-serish-ketu-per-balla-perfundon-deshmine-ne-gjyqin-per-partizanin-a-do-paraqitet-rama-ne-seance-eshte-pergjegjesi-individuale/ (April 30 session; page news feed runs through July 1, 2026 with no Rama testimony) ["I hope to come here again for..."/ Balla concludes testimony in the ...](https://www.balkanweb.com/en/shpresoj-te-vij-serish-ketu-per-balla-perfundon-deshmine-ne-gjyqin-per-partizanin-a-do-paraqitet-rama-ne-seance-eshte-pergjegjesi-individuale/)
- https://boldnews.al/2026/06/22/zbardhet-deshmia-e-vajzes-se-fatos-lubonjes-per-dosjen-partizani/ (June 22, 2026; only other witnesses testifying) [Zbardhet dëshmia e vajzës së Fatos Lubonjës për dosjen " ...](https://boldnews.al/2026/06/22/zbardhet-deshmia-e-vajzes-se-fatos-lubonjes-per-dosjen-partizani/)
- https://dosja.al/politike/gjyqi-per-dosjen-partizani-nis-seanca-gjyqesore-ne-gjkko-berisha-nuk-es-i501344 (June 22, 2026; Ylli Pango testified, no Rama) [Gjyqi për dosjen “Partizani”/ Nis seanca gjyqësore në GJKKO ...](https://dosja.al/politike/gjyqi-per-dosjen-partizani-nis-seanca-gjyqesore-ne-gjkko-berisha-nuk-es-i501344)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-68. `bfb0572f-9cfc-5cb0-beaf-d5fbcf4fc46d`

- Present date: `2026-05-03 12:26:32.992232`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Super Heavy booster on Starship Flight 12 be successfully caught by the launch tower arms (chopsticks)?

**Resolution criteria**

This question resolves **Yes** if all of the following conditions are met by June 1, 2026, 23:59 UTC:

1. Starship Flight 12 launches from Starbase, Texas.
2. The Super Heavy booster returns to the launch site and is captured by the launch tower's mechanical arms ("chopsticks").
3. A "successful catch" is defined as: the booster is held by the tower arms and remains suspended without contacting the ground, launch mount, or water at any point after the arms engage. The booster must remain in the arms' grip for at least 30 seconds after initial capture.

This question resolves **No** if any of the following occur:
- Starship Flight 12 does not launch by June 1, 2026, 23:59 UTC.
- Starship Flight 12 launches but no booster catch is attempted (e.g., the booster performs a splashdown or is intentionally expended).
- A catch is attempted but the booster is not successfully held by the arms (e.g., the booster falls, crashes into the tower, or lands in the water/on the ground).

**Resolution source:** The official SpaceX webcast (available at https://www.spacex.com/launches or the SpaceX account on X, https://x.com/SpaceX) and/or official SpaceX post-flight statements. Credible reporting from major outlets (Reuters, AP, NASA Spaceflight) may supplement if needed.

**Pre-cutoff background**

SpaceX's Starship Flight 12 is currently targeted for May 2026, launching from the newly constructed Orbital Launch Pad 2 (OLP-2) at Starbase, Texas [Starship Flight 12 | Starship-Super Heavy v3 - Next Spaceflight](https://nextspaceflight.com/launches/details/8002/). This will be the first launch from OLP-2 and the first flight of the Starship-Super Heavy Version 3 (Block 3) vehicle, using Booster B19 and Ship S39 [List of Starship launches - Wikipedia](https://en.wikipedia.org/wiki/List_of_Starship_launches).

OLP-2 is the second orbital launch pad at Starbase, featuring its own launch tower equipped with the mechanical catch arms ("chopsticks") designed to capture the returning Super Heavy booster. Because OLP-2 has never been used for a launch or booster catch attempt, its catch infrastructure is entirely untested in operational conditions.

SpaceX has previously demonstrated successful booster catches during earlier Starship flights (notably Flight 5 in October 2024). However, the three most recent flights prior to Flight 12 did not attempt tower catches: Flight 9 (May 27, 2025) ended in a booster landing failure in the Gulf of Mexico; Flight 10 (August 26, 2025) performed a controlled splashdown; and Flight 11 (October 13, 2025) also performed a controlled splashdown [List of Starship launches - Wikipedia](https://en.wikipedia.org/wiki/List_of_Starship_launches).

The combination of untested OLP-2 infrastructure, a new Block 3/V3 vehicle design, and the gap since the last successful booster catch creates meaningful uncertainty about whether the catch will be attempted and succeed on Flight 12. The launch has been delayed multiple times, initially targeting March/April 2026 before slipping to May 2026.

**Exact later resolution packet**

The question requires that the Super Heavy booster on Starship Flight 12 return to the launch site and be captured by the tower's chopstick arms, remaining suspended for at least 30 seconds.

- Starship Flight 12 did launch from Starbase, Texas on May 22, 2026 at 5:30 p.m. CT (22:30 UTC), within the June 1, 2026 deadline. This satisfies condition 1 (the antecedent of launch occurring).
- However, the booster did NOT attempt a tower catch. The official SpaceX mission page for Starship Flight 12 explicitly states that after the boostback burn, the Super Heavy booster attempted to reignite its engines for the landing burn before experiencing a hard splashdown in the Gulf of America (Gulf of Mexico) [8c54ed].
- The Wikipedia article on Starship flight test 12 corroborates this, noting the booster flipped abnormally fast after separation, most engines failed, only one engine ignited for the landing burn, and the booster suffered a water impact at T+00:06:20, crashing into the Gulf rather than returning to the launch site [0b785d]. As the first flight of the new V3/Block 3 vehicle, no return-to-launch-site catch was planned; a controlled/hard splashdown occurred instead.

Since no tower catch occurred — the booster impacted the water — the resolution criteria's NO conditions are met ("the booster performs a splashdown" / "lands in the water"). The question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-69. `c5099a67-5abb-548a-b92a-dd50c8e65064`

- Present date: `2026-05-01 18:31:35.093195`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Port Sudan International Airport be closed to civilian flights for at least 48 consecutive hours between May 1 and May 31, 2026?

**Resolution criteria**

This question resolves **Yes** if Port Sudan International Airport (PZU/HSPN) is closed to civilian flights for at least 48 consecutive hours at any point during the resolution window. It resolves **No** otherwise.

**Resolution window:** From 00:00 UTC on May 1, 2026, through 23:59 UTC on May 31, 2026.

**Definition of "closed to civilian flights":** A complete suspension of all scheduled and unscheduled commercial passenger flight arrivals and departures at the airport. Humanitarian flights, military flights, government evacuation flights, and cargo-only flights are excluded from this definition — their continued operation does not prevent a Yes resolution. The key criterion is that no regular commercial passenger services are operating.

**A closure that begins before May 1, 2026 (00:00 UTC) counts toward a Yes resolution** only if at least 48 consecutive hours of the closure fall within the resolution window (i.e., the closure must extend to at least 00:00 UTC on May 3, 2026, or later).

**Measuring the 48 consecutive hours:** The duration is measured based on the earliest of: (a) official NOTAMs (Notices to Air Missions) issued for PZU/HSPN indicating closure to civilian traffic, with timestamps in UTC; or (b) official announcements from the Sudan Civil Aviation Authority (https://scaa.gov.sd/, or successor website); or (c) timestamped reporting from at least two of the following major news agencies: Reuters (https://www.reuters.com/world/africa/), Associated Press, Agence France-Presse, BBC, or Al Jazeera, confirming the closure and its duration.

**Conflicting sources:** If NOTAMs indicate the airport is closed but news agencies report flights are still operating (or vice versa), NOTAM data takes precedence as the authoritative source. If no NOTAMs are available, resolution relies on agreement between at least two major news agencies. If major news agencies conflict on the duration (e.g., one says 36 hours, another says 50 hours), the question resolves based on the majority of reporting from the listed agencies. If no majority exists, the question resolves **No**.

**Resolution sources:**
- NOTAMs for PZU/HSPN, available via ICAO or flight-tracking services such as https://www.flightaware.com/live/airport/HSPN
- Sudan Civil Aviation Authority: https://scaa.gov.sd/
- Reuters Africa coverage: https://www.reuters.com/world/africa/
- Al Jazeera: https://www.aljazeera.com/where/sudan/
- Associated Press, AFP, BBC News

**Pre-cutoff background**

Port Sudan International Airport (IATA: PZU) has served as Sudan's primary functioning international airport since the outbreak of the Sudanese civil war in April 2023, after Khartoum International Airport was rendered inoperable. The airport is a critical lifeline for humanitarian aid and civilian travel.

In May 2025, the Rapid Support Forces (RSF) launched a series of drone attacks on Port Sudan, including strikes on or near the airport. On May 3, 2025, the RSF attacked with 11 drones, causing the airport to suspend flights for the remainder of that day (until 5:00 PM local time). On May 5, 2025, a second wave of drone attacks led to another suspension of flights [2025 East Sudan drone attacks - Wikipedia](https://en.wikipedia.org/wiki/2025_East_Sudan_drone_attacks). Attacks continued on May 6 and May 7, 2025, hitting the airport area and nearby infrastructure. These closures were each relatively brief — lasting hours rather than days.

Khartoum International Airport partially reopened for domestic flights on February 1, 2026, reducing but not eliminating Port Sudan's strategic importance. Port Sudan remains a key hub for international flights and humanitarian operations. The RSF has demonstrated the capability and willingness to strike Port Sudan's airport with drones, and the security environment remains volatile. Previous closures in May 2025 lasted less than 24 hours each, meaning a 48-consecutive-hour closure would represent a significant escalation beyond past incidents.

As of late April 2026, Port Sudan airport appears to be operational with scheduled commercial flights to multiple destinations.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question asks whether Port Sudan International Airport (PZU/HSPN) was closed to civilian/commercial passenger flights for at least 48 consecutive hours during May 1–31, 2026.

Key findings:

1. The major Sudanese aviation disruption in May 2026 was centered on KHARTOUM International Airport, NOT Port Sudan. On Monday, May 4, 2026, RSF drones struck Khartoum's international airport, fuel depots and military bases, forcing a multi-day suspension and a Sudanese airspace closure. The BBC reported authorities announced a "72-hour suspension of operations at the airport [Khartoum]" following the attacks [Sudan accuses Ethiopia and UAE of orchestrating drone attacks on ...](https://www.bbc.com/news/articles/clype712r3qo). Dabanga/AllAfrica reporting (May 5–6, 2026) placed the drone strike at Khartoum airport, noting it was the "first in 7 months" there and that aid operations (run via Port Sudan) were "not affected" [https://www.dabangasudan.org/en/all-news/article/drone-strike-on-khartoum-airport-first-in-7-months-aid-ops-not-affected](https://www.dabangasudan.org/en/all-news/article/drone-strike-on-khartoum-airport-first-in-7-months-aid-ops-not-affected) [Sudan Aid Ops Not Impacted By Khartoum Airport Drone Strike](https://allafrica.com/stories/202605070005.html) [UN: 'Flights from Khartoum airport suspended for the third day ...](https://www.dabangasudan.org/en/all-news/article/un-flights-from-khartoum-airport-suspended-for-the-third-day-following-drone-attack-sudan-pm-visits-site) [Sudan: Drone Strike On Khartoum Airport 'First in 7 Months'](https://allafrica.com/stories/202605060017.html).

2. The SCAA airspace suspension and subsequent reopening (a NOTAM reopening Sudanese airspace to international traffic on Friday, May 8, 2026) were reported in the context of flights "returning to Khartoum International Airport following a suspension caused by drone attacks earlier this week" [Armed conflicts and attacks - News as Facts](https://newsasfacts.com/news/154752). The narrative consistently frames Khartoum — not Port Sudan — as the suspended airport.

3. No source found (NOTAM for HSPN, SCAA announcement, or two qualifying agencies — Reuters/AP/AFP/BBC/Al Jazeera) confirms Port Sudan International Airport specifically was closed to commercial passenger flights for 48 consecutive hours in May 2026. Port Sudan was repeatedly described as the continuing operational hub: UN/WFP and humanitarian operations continued [Sudan Aid Ops Not Impacted By Khartoum Airport Drone Strike](https://allafrica.com/stories/202605070005.html) [https://www.dabangasudan.org/en/all-news/article/drone-strike-on-khartoum-airport-first-in-7-months-aid-ops-not-affected](https://www.dabangasudan.org/en/all-news/article/drone-strike-on-khartoum-airport-first-in-7-months-aid-ops-not-affected); the SafeAirspace status page (updated ~May 27, 2026) flagged HSSK/Khartoum as closed but did not record a comparable Port Sudan closure [Summary – Safe Airspace](https://safeairspace.net/summary/) [Sudan - Safe Airspace](https://safeairspace.net/sudan/); and the US Sudan travel advisory (May 15, 2026) said only that "Commercial service to the Port Sudan International Airport has been limited at times due to drone strikes" — intermittent limits, not a sustained 48-hour total closure.

4. The historical analogue of an actual Port Sudan closure (the May 2025 RSF drone attacks) caused only hours-long suspensions, not 48-hour closures [Drone strikes pummel Port Sudan in dramatic escalation of civil war](https://www.washingtonpost.com/world/2025/05/06/port-sudan-drone-strike-airport/), and that was a different year.

Per the resolution criteria, NOTAM data takes precedence, and absent NOTAMs a closure must be confirmed by at least two of Reuters/AP/AFP/BBC/Al Jazeera including its duration; if no clear majority confirms it, the question resolves NO. I found no such confirmation for a 48-hour Port Sudan commercial-flight closure.

CAVEAT: There was a nationwide Sudanese airspace suspension roughly May 4–8, 2026 tied to the Khartoum attacks [Armed conflicts and attacks - News as Facts](https://newsasfacts.com/news/154752). If interpreted as a full nationwide closure, it could in principle have suspended Port Sudan commercial flights for >48 hours. However, reporting frames the closure/reopening around Khartoum operations, and Port Sudan is consistently described as remaining functioning. Because the criteria require affirmative, specific confirmation of a Port Sudan closure and its duration (which I could not establish), the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-70. `8d8a890a-dec3-51a4-afe2-bb5a8d58c88d`

- Present date: `2026-05-16 01:20:23.347995`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will Ukraine publicly oppose or criticize EU plans for direct negotiations with Russia between May 12 and June 30, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026 (00:00 UTC) and before July 1, 2026 (00:00 UTC), a senior Ukrainian official publicly opposes or criticizes EU plans for direct negotiations with Russia. The following definitions apply:

**"Senior Ukrainian official"** means the President of Ukraine, the Prime Minister of Ukraine, the Minister of Foreign Affairs of Ukraine, or the Head of the Office of the President of Ukraine, speaking in their official capacity.

**"EU plans for direct negotiations with Russia"** means any formal proposal, initiative, or framework for direct EU-Russia talks discussed or adopted at the EU Foreign Affairs Council, an informal Gymnich meeting, or announced by the EU High Representative for Foreign Affairs and Security Policy, or endorsed by the European Council. General background diplomatic contacts or sanctions discussions do not qualify.

**"Publicly oppose or criticize"** means at least one of the following:
1. An official statement published on the website of the President of Ukraine (https://www.president.gov.ua/) or the Ministry of Foreign Affairs of Ukraine (https://mfa.gov.ua/) that uses language explicitly expressing disagreement, opposition, rejection, or condemnation of such EU plans; OR
2. Remarks by a qualifying official in a press conference, interview, or social media post (on official verified accounts) that are reported by at least one major international news wire (Reuters, AP, or AFP) as constituting opposition or criticism of EU negotiation plans with Russia. Terms such as "unacceptable," "reject," "oppose," "condemn," "betray," "undermine," or equivalent expressions of disapproval qualify.

Statements that merely express caution, set conditions, or call for Ukraine's inclusion without explicitly opposing or criticizing the EU plans do NOT qualify. For example, a statement saying "we expect to be included" without criticizing the EU initiative would not resolve YES.

**Resolution sources:** Official Ukrainian government portals (president.gov.ua, mfa.gov.ua) and major international news agencies (Reuters at https://www.reuters.com/, AP at https://apnews.com/, AFP). If no qualifying statement is found by July 1, 2026 (00:00 UTC), the question resolves NO.

**Pre-cutoff background**

As of May 12, 2026, the European Union is actively debating whether to engage in direct negotiations with Russia regarding the war in Ukraine. EU High Representative Kaja Kallas announced that EU foreign ministers will discuss potential direct talks with Russia at an informal Gymnich meeting scheduled for May 27-28, 2026, in Cyprus [EU to discuss potential negotiations with Russia in Cyprus summit](https://english.nv.ua/amp/eu-planning-to-discuss-negotiations-with-russia-50606859.html). The EU remains split on the issue, with some member states favoring direct engagement and others preferring to let the US lead diplomatic efforts ['We need to make up our mind': EU split over direct talks with Russia](https://www.euronews.com/my-europe/2026/05/11/we-need-to-make-up-our-mind-eu-still-split-over-direct-talks-with-russia).

Ukraine's current stance is nuanced. President Volodymyr Zelenskyy has called for Europe to take a more active role, stating that "Europe must be at the table in any talks with Russia" ['We need to make up our mind': EU split over direct talks with Russia](https://www.euronews.com/my-europe/2026/05/11/we-need-to-make-up-our-mind-eu-still-split-over-direct-talks-with-russia). However, Ukrainian Foreign Minister Andrii Sybiha has emphasized that any EU involvement must be "complementary" to existing diplomatic processes rather than an "alternative" track, and that Ukraine does not want the EU to pursue "alternative peace talks" that might undermine existing processes ['We need to make up our mind': EU split over direct talks with Russia](https://www.euronews.com/my-europe/2026/05/11/we-need-to-make-up-our-mind-eu-still-split-over-direct-talks-with-russia). This creates genuine uncertainty: Ukraine broadly supports EU engagement but could oppose specific formats or proposals that exclude Ukraine from the table or undermine its negotiating position.

The Gymnich meeting on May 27-28 is expected to produce concrete proposals regarding EU-Russia engagement, which could trigger a more definitive Ukrainian response.

**Exact later resolution packet**

RESOLUTION: NO (0).

ANTECEDENT CHECK (was there an "EU plan for direct negotiations with Russia"?): YES, so the question is NOT annulled. EU plans/initiatives for direct EU-Russia engagement were formally discussed within the window: (a) potential negotiations with Russia were on the agenda of the informal Gymnich foreign ministers' meeting in Limassol, Cyprus on May 27-28, 2026 (Reuters reported EU ministers stating "Russia will not choose who speaks for Europe in potential Ukraine talks," May 28 [Russia will not choose who speaks for Europe in potential Ukraine ...](https://www.reuters.com/world/europe/russia-will-not-choose-who-speaks-europe-potential-ukraine-talks-eu-ministers-2026-05-28/)); and (b) European Council President António Costa opened a tentative back-channel/communication line with the Kremlin, discussed at the European Council summit of June 18-19, 2026 (AP [European Union seeks to reopen communication channel with Russia](https://wtop.com/russia-ukraine-war-news/2026/06/the-european-union-has-quietly-sought-to-reopen-communication-with-russia/); Euronews [EU leaders debate Ukraine as Costa opens Kremlin channel](https://www.euronews.com/my-europe/2026/06/19/eu-leaders-debate-ukraine-as-costa-opens-diplomatic-channel-with-kremlin); Reuters [Russia tells Europe: Yes to talks, no to ultimatums - Reuters](https://www.reuters.com/world/europe/russia-tells-europe-yes-talks-no-ultimatums-2026-06-19/)). This satisfies "discussed... at an informal Gymnich meeting... or endorsed by the European Council."

CONSEQUENT CHECK (did a senior Ukrainian official publicly oppose/criticize such EU plans, using explicit disapproval language, reported by Reuters/AP/AFP or on president.gov.ua/mfa.gov.ua?): NO. Across all sources examined within the May 12–June 30, 2026 window, no qualifying official (President Zelenskyy, PM, FM Sybiha, or Head of the Office of the President) explicitly opposed or criticized EU plans for direct EU-Russia negotiations. On the contrary, Ukraine consistently SUPPORTED/PUSHED FOR European involvement:
- Reuters (June 7, 2026): "European leaders back Zelenskiy's call for direct talks with Putin, urge US and EU involvement" — Zelensky was the one calling for direct talks with European participation, not opposing them.
- France 24 (June 8, 2026): Zelensky and UK/France/Germany leaders issued a joint statement supporting "direct dialogue between Ukraine and Russia – with active US and European participation" [European leaders back Zelensky's call for direct Russia talks](https://www.france24.com/en/europe/20260607-european-leaders-back-zelensky-call-for-direct-russia-talks).
- Reuters (June 22, 2026): Zelenskiy said "Ukraine will decide who represents Europe in the negotiations. That is fair" — this asserts Ukraine's role, not opposition; he did not use language like reject/oppose/unacceptable/undermine toward EU plans [Ukraine to decide who represents Europe in Russia talks, Zelenskiy ...](https://www.reuters.com/business/aerospace-defense/ukraine-decide-who-represents-europe-russia-talks-zelenskiy-says-2026-06-22/).
- Reuters (May 28, 2026, Gymnich): Reported that "Kyiv pushes for more European involvement" and Zelensky "has urged Europe to become part of the process" — no Ukrainian opposition reported [Russia will not choose who speaks for Europe in potential Ukraine ...](https://www.reuters.com/world/europe/russia-will-not-choose-who-speaks-europe-potential-ukraine-talks-eu-ministers-2026-05-28/).
- AP/PBS and Washington Post (June 18-19, 2026) on Costa's Kremlin back-channel: reported EU internal divisions and that the E3 coordinated at the "explicit wish of Ukraine," but no opposition/criticism from senior Ukrainian officials [EU leaders disagree on creation of Kremlin back-channel amid ...](https://www.pbs.org/newshour/world/eu-leaders-disagree-on-creation-of-kremlin-back-channel-amid-ukraine-war) [EU leaders squabble over outreach to Moscow as Ukraine war ...](https://www.washingtonpost.com/world/2026/06/19/eu-russia-talks-kremlin-ukraine/d70c792e-6bd9-11f1-830e-133d20cadd28_story.html); AP noted only Baltic EU leaders were skeptical, not Ukrainian officials [European Union seeks to reopen communication channel with Russia](https://wtop.com/russia-ukraine-war-news/2026/06/the-european-union-has-quietly-sought-to-reopen-communication-with-russia/). Euronews (June 19) likewise reported no Ukrainian criticism [EU leaders debate Ukraine as Costa opens Kremlin channel](https://www.euronews.com/my-europe/2026/06/19/eu-leaders-debate-ukraine-as-costa-opens-diplomatic-channel-with-kremlin). Reuters (June 18/19) attributed criticism of Costa's uncoordinated contacts to some EU leaders (e.g., Estonia's PM called it "misguided"), not to Ukraine [Russia tells Europe: Yes to talks, no to ultimatums - Reuters](https://www.reuters.com/world/europe/russia-tells-europe-yes-talks-no-ultimatums-2026-06-19/).

NON-QUALIFYING STATEMENTS considered and excluded per the resolution criteria (which state that mere caution, conditions, or calls for inclusion do NOT qualify):
- FM Sybiha's remark (reported May 11, 2026, before the window anyway) that EU engagement should be "complementary" not an "alternative" track was a condition/preference, not explicit opposition [Ukraine urges EU to 'complement' US peace talks with Russia](https://www.euractiv.com/news/ukraine-urges-eu-to-complement-us-peace-talks-with-russia/).
- Sybiha's statement about which "peace initiatives" are "unacceptable" (May 12, 2026) referred to Russia's demands/territorial concessions (Kyiv's red line of no territorial concessions), NOT to EU plans for direct negotiations [Sybiha‎ | European Pravda - Європейська правда](https://www.eurointegration.com.ua/eng/tags/sybiha/view_news/).

Because the antecedent occurred but no qualifying senior Ukrainian official statement opposing/criticizing EU direct-negotiation plans was found in the specified sources during May 12–June 30, 2026, the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-71. `f2d5546e-d35e-59de-a8d4-dd5de3effa61`

- Present date: `2026-05-03 04:42:03.614346`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. Department of Commerce announce a formal clawback or reduction of CHIPS Act funding from any award recipient (excluding Natcast) between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after April 30, 2026 (00:00 UTC) and on or before June 1, 2026 (23:59 UTC), the U.S. Department of Commerce or the CHIPS Program Office publishes an official announcement—such as a press release on https://www.commerce.gov/news/press-releases or an official notice on https://www.chips.gov—stating that CHIPS Act funding for any award recipient is being reduced, rescinded, or clawed back. Otherwise, the question resolves as **No**.

Key definitions:

- **"Clawback"**: The return or recapture by the federal government of CHIPS Act funds that were previously disbursed to an award recipient.
- **"Reduction"**: A formal decrease in the total award amount (grant or loan) previously committed to an award recipient, whether under a binding final award agreement or a Preliminary Memorandum of Terms (PMT). This includes renegotiated award amounts that result in a lower total than originally announced. It does not include routine milestone-based disbursement schedules where funds are released incrementally per the original agreement.
- **"Award recipient"**: Any entity that has received a CHIPS Act incentive award (grant or loan) from the Department of Commerce, whether formalized in a binding agreement or documented in a Preliminary Memorandum of Terms (PMT). This explicitly **excludes** Natcast (the National Center for the Advancement of Semiconductor Technology), whose $7.4 billion funding reduction was announced prior to the resolution window.

The question resolves based solely on announcements occurring within the April 30–June 1, 2026 window. Prior funding adjustments (including the Natcast clawback and the Intel award renegotiation finalized in November 2024) do not count toward resolution.

If no qualifying announcement is found on the Department of Commerce press releases page or CHIPS.gov by 23:59 UTC on June 1, 2026, credible major news reporting (e.g., Reuters, AP, Wall Street Journal) may also serve as a resolution source if it references an official Commerce Department action.

**Pre-cutoff background**

The CHIPS and Science Act of 2022 appropriated approximately $39 billion in manufacturing incentives administered by the Department of Commerce's CHIPS Program Office. As of July 2025, the Department of Commerce had awarded $30.9 billion across 40 projects to 19 companies, including $5.5 billion in loans to two companies [https://www.gao.gov/products/gao-26-107882](https://www.gao.gov/products/gao-26-107882). These projects are subject to 161 milestones spanning from November 2024 through October 2033, of which only 24 milestone completion reports had been submitted as of July 2025, and one project (a leading-edge logic chip manufacturing facility in Arizona) was certified as complete in June 2025 [https://www.gao.gov/products/gao-26-107882](https://www.gao.gov/products/gao-26-107882).

The Trump administration has already demonstrated willingness to restructure CHIPS Act awards: it clawed back $7.4 billion from Natcast, the nonprofit designated to operate the National Semiconductor Technology Center. Intel's award was also reduced from an announced $8.5 billion to $7.86 billion in its final funding agreement. The GAO has flagged concerns about weak fraud controls in the CHIPS program, and the administration has publicly questioned aspects of the CHIPS Act. With ongoing audits, compliance monitoring, and political pressure, there is meaningful but uncertain probability that additional recipients could face funding reductions during this window.

The primary resolution source is the U.S. Department of Commerce press releases page: https://www.commerce.gov/news/press-releases

**Exact later resolution packet**

The question resolves NO. The criteria require an official Department of Commerce / CHIPS Program Office announcement (or credible major news report referencing official Commerce action) between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC) stating that CHIPS Act funding for an award recipient OTHER THAN Natcast is being reduced, rescinded, or clawed back. No such qualifying announcement exists in the window.

Evidence gathered:
- The only Commerce/CHIPS announcement located within the window was a May 21, 2026 NIST/Commerce press release announcing the signing of letters of intent to PROVIDE $2.013 billion in new CHIPS funding to 9 quantum-computing companies (GlobalFoundries, IBM, Atom Computing, Diraq, D-Wave, Infleqtion, PsiQuantum, Quantinuum, Rigetti). This is an addition of funding, not a reduction, rescission, or clawback [Department of Commerce Announces Letters of Intent With 9 ...](https://www.nist.gov/news-events/news/2026/05/department-commerce-announces-letters-intent-9-companies-2-billion).
- The Semiconductor Industry Association's CHIPS investment tracker, last updated May 4, 2026, lists award recipients and amounts and contains no record of any reduction, clawback, cancellation, or rescission of an award (other than Natcast) within the April 30–June 1, 2026 window [Semiconductor Supply Chain Investments](https://www.semiconductors.org/chip-supply-chain-investments/).
- Broad Google searches across Commerce.gov, chips.gov/NIST, Reuters, AP, Manufacturing Dive, and the SIA found no clawback/reduction announcement dated within the window. All relevant clawback/reduction actions found are from outside the window: the Natcast $7.4B rescission (August 2025, expressly excluded), the Intel award reduction from $8.5B to $7.865B (finalized November 2024, expressly excluded), Samsung's earlier reduction, equity-stake conversions negotiated in 2025, and the Durham/$285M award termination (2025). None of these occurred in the April 30–June 1, 2026 window.

Because no qualifying announcement of a reduction/rescission/clawback for a non-Natcast recipient was published on commerce.gov, chips.gov, or in major news reporting during the specified window, the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-72. `a0968428-9c0e-54e0-872c-32d96e222aaa`

- Present date: `2026-04-30 17:20:52.254938`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will China formally announce export restrictions on solar manufacturing equipment between April 30, 2026, and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, between April 30, 2026, 00:00 UTC and June 1, 2026, 23:59 UTC, the Chinese government formally announces new restrictions on exports of solar manufacturing equipment. Any actions or announcements made prior to April 30, 2026, 00:00 UTC are excluded.

**Definition of "formal restrictions":** An official regulatory action by a Chinese government body that imposes new, binding limitations on the export of solar manufacturing equipment. This includes, but is not limited to: (a) addition of solar manufacturing equipment to the "Catalogue of Technologies Prohibited or Restricted from Export" (中国禁止出口限制出口技术目录); (b) imposition of specific export licensing requirements for such equipment; or (c) issuance of a ministerial order, State Council decree, or equivalent regulatory notice that explicitly restricts or controls the export of such equipment. Informal guidance, verbal warnings to companies, or unconfirmed reports of internal discussions do not qualify.

**Definition of "solar manufacturing equipment":** Machinery, tools, or specialized technology used in the fabrication of solar photovoltaic (PV) products, including but not limited to: equipment for polysilicon production, ingot growing, wafer slicing, solar cell processing (e.g., PERC, TOPCon, heterojunction/HJT cell production lines), and module assembly. This excludes finished goods such as solar panels, cells, modules, inverters, or polysilicon material itself.

**Resolution source:** The official announcement page of the Ministry of Commerce of the People's Republic of China (MOFCOM) at https://english.mofcom.gov.cn/Policies/index.html, or the State Council's policy briefing page at https://english.www.gov.cn/policies/. Confirmation from credible international news outlets (Reuters, Bloomberg, AP) citing the official Chinese government announcement is also acceptable.

If no qualifying formal announcement is made by 23:59 UTC on June 1, 2026, the question resolves as **No**.

**Pre-cutoff background**

As of April 30, 2026, China has not formally announced export restrictions on solar manufacturing equipment, but is actively considering such measures. On April 15, 2026, Reuters reported that Chinese officials held early-stage discussions with suppliers of solar panel manufacturing equipment—including companies such as Suzhou Maxwell Technologies—about potentially restricting exports of advanced solar manufacturing technology to the United States [China restricts solar manufacturing equipment exports to the US](https://www.worldenergynews.com/news/china-restricts-solar-manufacturing-equipment-exports-the-773524). These talks have not yet reached the stage of seeking formal industry feedback [China restricts solar manufacturing equipment exports to the US](https://www.worldenergynews.com/news/china-restricts-solar-manufacturing-equipment-exports-the-773524).

China dominates the global solar supply chain, producing more than 80% of the world's solar panel components [https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/](https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/). The potential restrictions are viewed in the context of the ongoing U.S.-China trade dispute and growing concern within Beijing over U.S. efforts to build domestic solar manufacturing capacity, particularly by Tesla, which aims to manufacture 100 GW of solar panels domestically by 2028 [China restricts solar manufacturing equipment exports to the US](https://www.worldenergynews.com/news/china-restricts-solar-manufacturing-equipment-exports-the-773524). In 2025, China threatened licensing requirements for exports of related technology—high-end batteries and materials for energy storage systems—establishing a precedent for such controls in the clean energy sector [China restricts solar manufacturing equipment exports to the US](https://www.worldenergynews.com/news/china-restricts-solar-manufacturing-equipment-exports-the-773524).

The discussions occur during a fragile U.S.-China trade truce signed in October 2025 and set to expire in November 2026 [https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/](https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/). Whether China proceeds with formal restrictions may depend on diplomatic negotiations and strategic calculations about leverage versus maintaining the truce atmosphere [China considers a new pressure point: solar equipment - Marketplace](https://www.marketplace.org/story/2026/04/29/us-solar-production-would-slow-if-china-limits-key-exports).

Key sources: Reuters reporting from April 15, 2026 (https://www.reuters.com/legal/litigation/china-weighs-curbs-exports-solar-manufacturing-equipment-us-2026-04-15/); Marketplace reporting from April 29, 2026 (https://www.marketplace.org/story/2026/04/29/us-solar-production-would-slow-if-china-limits-key-exports).

**Exact later resolution packet**

The question resolves NO because no qualifying formal announcement of export restrictions on solar manufacturing equipment was made by the Chinese government between April 30, 2026, 00:00 UTC and June 1, 2026, 23:59 UTC.

Evidence gathered:

1. As of the question's creation (April 30, 2026), China was only "considering"/"weighing" such restrictions. Reuters' April 15, 2026 exclusive ("China weighs curbs on exports of solar manufacturing equipment to US," https://www.reuters.com/legal/litigation/china-weighs-curbs-exports-solar-manufacturing-equipment-us-2026-04-15/) reported only early-stage talks with suppliers. MOFCOM's spokesperson publicly stated on April 16, 2026 that he was "unaware" of such a development [Solar Trade In Focus As China & EU Weigh New Curbs](https://taiyangnews.info/markets/solar-trade-in-focus-china-eu-weigh-new-curbs) (https://taiyangnews.info/markets/solar-trade-in-focus-china-eu-weigh-new-curbs).

2. The only "Catalogue of Technologies Prohibited or Restricted from Export" item concerning photovoltaic silicon wafer preparation technology (光伏硅片制备技术) traces to a public consultation DRAFT (征求意见版), not a finalized binding regulation, and dates to December 2022/January 2023 — well outside the resolution window [《中国禁止出口限制出口技术目录》（征求公众意见版）修订简评](https://www.hankunlaw.com/portal/article/index/cid/8/id/12826.html) [中国拟将光伏硅片制备、激光雷达等技术列入禁止/限制出口 ...](https://www.pcachina.com/article/3000158499). The draft was explicitly "still in the public comment stage and not decided" [中国拟将光伏硅片制备、激光雷达等技术列入禁止/限制出口 ...](https://www.pcachina.com/article/3000158499).

3. A Reuters article from May 18, 2026 (https://www.reuters.com/business/energy/chinas-solar-exports-jump-60-year-april-2026-05-18/) covering April solar export data mentioned no new formal restrictions on manufacturing equipment; the only April 1, 2026 change was elimination of VAT export tax rebates on finished PV products (tax policy, not equipment export control, and excluded by criteria) [China's solar exports jump 60% on the year in April - Reuters](https://www.reuters.com/business/energy/chinas-solar-exports-jump-60-year-april-2026-05-18/).

4. A New York Times article (May 21, 2026) noted China had "blocked exports of high-end solar manufacturing equipment from a Chinese supplier, Suzhou Maxwell Technologies, to Tesla," but this was a specific, targeted commercial blockage — not a formal government-wide regulatory announcement (no catalogue entry, ministerial order, or licensing rule cited). This does not meet the criteria's "formal restriction" definition and explicitly excludes informal/targeted actions [Elon Musk and Other CEOs on Trump's Trip to China Sought Relief](https://www.nytimes.com/2026/05/21/business/economy/trump-china-trip-ceos-tesla-musk.html).

5. The Economist (May 26, 2026) described the industry as in turmoil but reported no formal export restrictions on solar manufacturing equipment [China's world-beating solar industry is in turmoil - The Economist](https://www.economist.com/china/2026/05/26/chinas-world-beating-solar-industry-is-in-turmoil).

6. No MOFCOM official announcement, State Council decree, or Reuters/Bloomberg/AP report citing an official government announcement of such restrictions in the window was found despite targeted searches in English and Chinese.

Since the formal action that the question required (a binding ministerial order, licensing requirement, or catalogue addition specifically targeting solar manufacturing equipment) did not occur within the April 30 – June 1, 2026 window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-73. `01a607b2-d68c-5e0d-9bd8-efe79748b96e`

- Present date: `2026-05-02 14:12:47.480217`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Chipotle's first restaurant in South Korea (Republic of Korea) be open to the public by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, by 23:59 UTC on June 1, 2026, at least one Chipotle Mexican Grill restaurant located in South Korea (the Republic of Korea, as defined by https://en.wikipedia.org/wiki/South_Korea) is open to the public — meaning it is serving food to members of the general public who can walk in or order without a special invitation, credential, or pre-registration.

"Open to the public" requires that any member of the general public can purchase food at the location. A **soft opening** counts only if it is open to walk-in members of the general public (not restricted to invited guests, media, influencers, or employees). An **invite-only** or **media-only** event does **not** count.

If the first restaurant opened prior to May 1, 2026 (i.e., it was already open to the public before the question window began), this question resolves **Yes**.

Otherwise, the question resolves **No**.

**Resolution source:** Official announcements from Chipotle's Investor Relations newsroom (https://newsroom.chipotle.com/) or credible major news outlets such as Reuters (https://www.reuters.com/), Korea Herald (https://www.koreaherald.com/), or Korea JoongAng Daily (https://koreajoongangdaily.joins.com/). Social media posts from Chipotle's official accounts may serve as supplementary evidence but are not sufficient on their own.

**Pre-cutoff background**

In September 2025, Chipotle Mexican Grill announced a joint venture with SPC Group, a major South Korean food conglomerate, to open its first restaurants in Asia, specifically in South Korea and Singapore, in 2026. This marked Chipotle's first expansion into the Asian market.

As of May 2, 2026, the joint venture remains active. Chipotle's Q1 2026 earnings release (April 29, 2026) references plans for 10–15 international partner-operated restaurant openings in 2026 across "the Middle East, Asia and Mexico," though it does not specifically name South Korea or SPC Group [https://www.prnewswire.com/news-releases/chipotle-announces-first-quarter-2026-results-302757940.html](https://www.prnewswire.com/news-releases/chipotle-announces-first-quarter-2026-results-302757940.html). Multiple reports from early 2026 indicate the first location is planned near Gangnam Station in Seoul, with an opening target of "as early as May 2026" or "by June." The operator is Sangmidang Holdings (an SPC Group entity), the same group behind Shake Shack and Jamba Juice in Korea.

No confirmed reports of the restaurant having already opened have been found as of May 2, 2026. The language "as early as May 2026" suggests the timeline is aspirational and subject to construction, permitting, and supply chain factors common to international restaurant launches.

Key sources:
- Chipotle Newsroom: https://newsroom.chipotle.com/2025-09-10-CHIPOTLE-TO-EXPAND-TO-ASIA-FOR-THE-FIRST-TIME-THROUGH-A-JOINT-VENTURE-WITH-SPC-GROUP
- Seoul Economic Daily (English): https://en.sedaily.com/finance/2026/04/08/chipotles-first-asia-store-to-open-near-gangnam-station
- Reuters: https://www.reuters.com/world/asia-pacific/chipotle-enter-asia-2026-with-burrito-chains-south-korea-singapore-2025-09-10/

**Exact later resolution packet**

The question resolves NO. Chipotle's first restaurant in South Korea, near Exit 10 of Gangnam Station in Seoul, had NOT opened to the public by 23:59 UTC on June 1, 2026.

Decisive evidence: A Herald Business (헤럴드경제) article published May 30, 2026 reports that Chipotle had only recently begun construction on its first location along Gangnam-daero near Gangnam Station Exit 10, and that the store was scheduled to open "around August" 2026 ("매장은 오는 8월쯤 문을 열 예정이다") [51dca8]. This confirms that just two days before the deadline, the restaurant was still under construction and not yet serving any customers — neither a full nor a soft public opening had occurred.

Corroborating evidence: A NamuWiki page on Chipotle in South Korea, last updated May 26, 2026, still described the opening as a future plan/target (May or June, near Gangnam Station) and did not confirm any actual opening to the public [c85eaf]. All pre-deadline coverage (Seoul Economic Daily, Korea Herald, Korea JoongAng Daily, etc.) consistently used forward-looking language ("as early as May," "by June," "first half of 2026") and a target opening, never reporting an accomplished opening.

I checked for any report that the Gangnam store had actually opened (including a Korea Herald Food-section snippet that mentioned customers waiting outside a "Gangnam store" on Children's Day, May 5); however, that article (Korea Herald, May 5, 2026) was about the Chinese milk-tea brand Chagee, not Chipotle [a98d22]. No Chipotle Newsroom, Reuters, Korea Herald, or Korea JoongAng Daily report was found announcing an actual public opening of the Chipotle Gangnam store on or before June 1, 2026.

The resolution criteria also provide that if the store opened before May 1, 2026 it would resolve Yes; the construction-stage status as of May 30, 2026 rules this out as well.

Therefore, since no Chipotle restaurant in South Korea was open to the public (walk-in or order) by the June 1, 2026 deadline — with construction ongoing and an August target — the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-74. `83077271-dd90-5017-8107-0d3fba6b8872`

- Present date: `2026-05-02 22:34:40.635063`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Federal Reserve issue a proposed rule implementing the GENIUS Act by June 1, 2026?

**Resolution criteria**

This question resolves YES if the Board of Governors of the Federal Reserve System publishes a proposed rule—defined as a Notice of Proposed Rulemaking (NPRM) or equivalent document containing draft regulatory text and an invitation for public comment (see the Federal Reserve's own definition at https://www.federalreserve.gov/aboutthefed/board-vote-category-definitions.htm [Board Vote Category Definitions - Federal Reserve](https://www.federalreserve.gov/aboutthefed/board-vote-category-definitions.htm))—specifically implementing provisions of the GENIUS Act of 2025, on or after May 1, 2026 (00:00 UTC) and by June 1, 2026 (23:59 UTC).

This question resolves NO if no such proposed rule has been published by 23:59 UTC on June 1, 2026.

Resolution will be determined by checking:
1. The Federal Reserve's press releases page: https://www.federalreserve.gov/newsevents/pressreleases.htm
2. The Federal Register's Federal Reserve section: https://www.federalregister.gov/agencies/federal-reserve-system

A proposed rule announced by the Federal Reserve Board but not yet published in the Federal Register by 23:59 UTC on June 1, 2026 still counts, provided the Board has voted to approve it and issued an official press release.

**Pre-cutoff background**

The Guiding and Establishing National Innovation for U.S. Stablecoins Act (GENIUS Act) was signed into law on July 18, 2025, establishing a comprehensive federal regulatory framework for payment stablecoins [GENIUS Act Regulations: Notice of Proposed Rulemaking](https://www.occ.treas.gov/news-issuances/bulletins/2026/bulletin-2026-3.html). The Act designates the Federal Reserve, the OCC, and the FDIC as primary federal payment stablecoin regulators and sets a statutory deadline of July 18, 2026 (18 months after enactment) for these regulators to promulgate implementing regulations [GENIUS Act Regulations: Notice of Proposed Rulemaking](https://www.occ.treas.gov/news-issuances/bulletins/2026/bulletin-2026-3.html).

As of May 1, 2026, two of the three primary federal regulators have already issued proposed rules:
- The OCC published its Notice of Proposed Rulemaking (NPRM) on February 25, 2026 [GENIUS Act Regulations: Notice of Proposed Rulemaking](https://www.occ.treas.gov/news-issuances/bulletins/2026/bulletin-2026-3.html).
- The FDIC approved its proposed rule on April 7, 2026 [FDIC Approves Proposal to Implement GENIUS Act Requirements ...](https://www.fdic.gov/news/press-releases/2026/fdic-approves-proposal-implement-genius-act-requirements-and-standards).

The Federal Reserve has not yet issued a proposed rule implementing the GENIUS Act. The Fed published a FEDS Notes research paper on payment stablecoins and cross-border payments on March 30, 2026, but has not initiated a formal rulemaking. The Fed has historically moved more cautiously than the OCC on crypto-related regulation, raising uncertainty about whether it will issue its NPRM before June 1, 2026, even with the July 18, 2026 statutory deadline approaching.

**Exact later resolution packet**

The question resolves NO because the Federal Reserve Board did not publish (or vote to approve) a Notice of Proposed Rulemaking implementing the GENIUS Act of 2025 between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC).

Evidence from the two resolution sources specified in the question:

1. Federal Reserve press releases page (https://www.federalreserve.gov/newsevents/pressreleases.htm): A review of all press releases issued during May 1 – June 1, 2026 shows none constitutes an NPRM implementing the GENIUS Act or regulating payment stablecoins. The releases covered enforcement actions, leadership changes (Kevin Warsh taking office as chairman May 22, Powell as chair pro tempore, Miran resignation), discount rate/FOMC minutes, surveys, and a May 20, 2026 request for comment on a "payment account" proposal — but that payment-account proposal does not mention the GENIUS Act or stablecoins [42499f].

2. Federal Register, Federal Reserve System section (https://www.federalregister.gov/agencies/federal-reserve-system): The Fed did publish several proposed rules on May 26, 2026 — Regulation D (Reserve Requirements), Regulation A (Extensions of Credit), and revisions to the Payment System Risk policy — all concerning new "special-purpose payment accounts." However, none of these documents implement the GENIUS Act of 2025 or regulate payment stablecoins [573ce6].

By contrast, the other two primary regulators had already issued their GENIUS Act NPRMs earlier (OCC in late February 2026, FDIC in April 2026), but the Federal Reserve had not done so by the June 1, 2026 deadline. The statutory deadline for implementing regulations was July 18, 2026, leaving the Fed room to act after the question's window closed.

Since no qualifying proposed rule was published or approved by the Fed within the May 1 – June 1, 2026 window, the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-75. `a3478df7-22b6-5473-a74a-00a0cd521090`

- Present date: `2026-05-03 00:14:28.684689`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a new strain of wiper malware targeting Industrial Control Systems (ICS) or Operational Technology (OT) be publicly identified between May 1, 2026, and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between 00:00 UTC on May 1, 2026, and 23:59 UTC on June 1, 2026, a **new strain** of wiper malware specifically targeting or designed to disrupt ICS or OT environments is publicly identified and reported by at least one qualifying major cybersecurity outlet.

**Definitions and criteria:**

1. **"New strain"** means a wiper malware family that has not been publicly documented or named by any cybersecurity researcher or vendor prior to May 1, 2026 (00:00 UTC). A new strain must have a distinct name, distinct codebase, or fundamentally different functionality from previously known families. Minor updates, recompilations, or configuration changes to existing families (e.g., a new build of DynoWiper, PYROXENE, or Lotus Wiper) do **not** qualify. A "variant" qualifies only if the reporting outlet explicitly describes it as a "new malware family" or assigns it a new, previously unused name.

2. **"Wiper malware"** means malicious software whose primary or significant function is to irreversibly delete, overwrite, or corrupt data or firmware on targeted systems, as defined by [Wikipedia: Wiper (malware)](https://en.wikipedia.org/wiki/Wiper_(malware)). Ransomware that also destroys data does not qualify unless the reporting source explicitly classifies it as a wiper.

3. **"Targeting ICS/OT"** means the malware contains code, configurations, or documented operational intent to interact with, disrupt, or destroy industrial control systems, SCADA systems, programmable logic controllers (PLCs), or other operational technology infrastructure, as defined by [NIST SP 800-82](https://csrc.nist.gov/publications/detail/sp/800-82/rev-3/final). Wipers that only target standard IT environments (e.g., Windows workstations in corporate networks) do **not** qualify, even if the victim organization operates critical infrastructure.

4. **"Major cybersecurity outlet"** means any of the following specific outlets or vendor blogs:
   - **News outlets**: The Hacker News (https://thehackernews.com), BleepingComputer (https://www.bleepingcomputer.com), Dark Reading (https://www.darkreading.com), The Record by Recorded Future (https://therecord.media), SecurityWeek (https://www.securityweek.com), Krebs on Security (https://krebsonsecurity.com)
   - **Vendor threat intelligence blogs**: Mandiant/Google Threat Intelligence (https://cloud.google.com/blog/topics/threat-intelligence), Dragos (https://www.dragos.com/blog), ESET/WeLiveSecurity (https://www.welivesecurity.com), CrowdStrike (https://www.crowdstrike.com/blog), Kaspersky Securelist (https://securelist.com), Palo Alto Unit 42 (https://unit42.paloaltonetworks.com)
   - **Government advisories**: CISA (https://www.cisa.gov/news-events/alerts)

5. **"Publicly identified and reported"** means a report or article is published on or after May 1, 2026 (00:00 UTC) at one of the outlets listed above, describing the new wiper strain. The publication date of the first qualifying report determines resolution timing.

6. This question explicitly **excludes** DynoWiper, PYROXENE and its variants, Lotus Wiper, and the ELECTRUM wiper variant reported in December 2025, as well as any other wiper malware publicly documented before May 1, 2026.

If no qualifying report is published by 23:59 UTC on June 1, 2026, this question resolves **No**.

**Resolution source**: Check the news outlets and vendor blogs listed above. A convenient aggregator is the ICS/OT Security section of Dark Reading (https://www.darkreading.com/ics-ot-security) and Dragos blog (https://www.dragos.com/blog).

**Pre-cutoff background**

The threat landscape for Industrial Control Systems (ICS) and Operational Technology (OT) has seen a notable acceleration in destructive wiper malware development through late 2025 and into 2026:

- **DynoWiper** (December 29, 2025): A novel data-wiping malware attributed by ESET to the Russia-aligned Sandworm (ELECTRUM) group, used in a cyberattack against Poland's power grid. Publicly reported January 26, 2026 [Lotus Wiper Malware Targets Venezuelan Energy Systems in ...](https://thehackernews.com/2026/04/lotus-wiper-malware-targets-venezuelan.html).
- **PYROXENE wiper variants**: Deployed during the Iran-Israel conflict, documented in the Dragos 2026 OT Cybersecurity Year in Review report [Dragos 2026 OT Cybersecurity Report: A Year in Review](https://www.dragos.com/ot-cybersecurity-year-in-review).
- **ELECTRUM destructive wiper variant** (December 2025): Dragos identified another destructive wiper variant from ELECTRUM, confirming their active development pipeline.
- **Lotus Wiper** (reported April 22, 2026): A previously undocumented wiper targeting Venezuela's energy sector (including state oil company PDVSA), discovered by Kaspersky and reported by The Hacker News and Dark Reading [Lotus Wiper Malware Targets Venezuelan Energy Systems in ...](https://thehackernews.com/2026/04/lotus-wiper-malware-targets-venezuelan.html).

This pace — roughly one new ICS/OT-targeting wiper strain every 2–3 months — suggests another discovery in May 2026 is plausible but far from certain. Geopolitical tensions (Russia-Ukraine, Iran-US/Israel, Venezuela) continue to drive state-sponsored destructive cyber operations against critical infrastructure.

**Key definitions:**
- **Wiper malware**: Malicious software designed to irreversibly delete, overwrite, or corrupt data on targeted systems, rendering them inoperable. See [NIST definition of destructive malware](https://www.nist.gov/glossary) and [Wikipedia: Wiper (malware)](https://en.wikipedia.org/wiki/Wiper_(malware)).
- **Industrial Control Systems (ICS)**: Systems used to monitor and control industrial processes, including SCADA, DCS, and PLCs. See [NIST SP 800-82](https://csrc.nist.gov/publications/detail/sp/800-82/rev-3/final) and [Wikipedia: Industrial control system](https://en.wikipedia.org/wiki/Industrial_control_system).
- **Operational Technology (OT)**: Hardware and software that detects or causes changes through direct monitoring and/or control of physical devices, processes, and events. See [SANS ICS definition](https://www.sans.org/cyber-security-courses/ics-scada-cyber-security-essentials/) and [Wikipedia: Operational technology](https://en.wikipedia.org/wiki/Operational_technology).

**Exact later resolution packet**

The question resolves NO because no new strain of wiper malware specifically targeting ICS/OT environments was publicly identified by a qualifying major cybersecurity outlet between 00:00 UTC May 1, 2026 and 23:59 UTC June 1, 2026.

I checked the resolution sources named in the question:

1. Dragos blog (https://www.dragos.com/blog): During the May 1–June 1, 2026 window, the only posts were "Defining xOT" (June 2), "Building AI for OT Security" (May 11), "OT Cybersecurity Lessons Learned from the Frontlines" (May 7), and "AI in the Breach: How an Adversary Leveraged AI to Target a Water Utility's OT" (May 6). The nearest wiper/malware-related item, "ZionSiphon: Why This Malware Isn't A Credible ICS Threat," is dated April 23, 2026 (outside the window) and is explicitly dismissed as not a credible ICS threat — not a wiper [Blog - Dragos](https://www.dragos.com/blog).

2. Dark Reading ICS/OT Security section (https://www.darkreading.com/ics-ot-security): Reviewing the feed through ~May 20, 2026, no new wiper strain was reported. The most recent wiper content was the Lotus Wiper (reported ~April 29, 2026), which the question explicitly excludes [https://www.darkreading.com/ics-ot-security](https://www.darkreading.com/ics-ot-security).

3. The Hacker News "wiper malware" label and front page through June 2, 2026: All May 2026 stories concern vulnerabilities, exploits, and supply-chain attacks (NGINX, Linux kernel, GitHub/Megalodon, npm worms, etc.). The most recent wiper article was the late-March 2026 Stryker incident (an IT/endpoint wiper, not ICS/OT). No new ICS/OT wiper family appeared in the window [wiper malware — Latest News, Reports & Analysis | The Hacker News](https://thehackernews.com/search/label/wiper%20malware).

Other candidate leads were ruled out:
- "Ukrainian Energy Supplier Targeted by New Industroyer Malware" turned out to be a 2022 Industroyer2 article, not 2026 [Ukrainian Energy Supplier Targeted by New Industroyer Malware](https://www.infosecurity-magazine.com/news/ukrainian-energy-industroyer/).
- HarfangLab report TRR260501 (May 13, 2026) documents Gamaredon's GammaDrop/GammaLoad (a VBScript downloader and C2 beacon), which are not wipers and not ICS/OT-targeting [STRATEGIC CYBER THREAT INTELLIGENCE BRIEFING](https://cyberwarrior76.substack.com/p/strategic-cyber-threat-intelligence-c69).
- The Cyber Florida CI Bulletin (May 19, 2026) only mentions the excluded Lotus Wiper plus non-wiper threats (ABCDoor backdoor, Ghostlock extortion tool, Mini Shai-Hulud worm, XLabsV1 botnet) [CI Bulletin Vol 2, Issue 7 May 19, 2026 | Cyber Florida at USF](https://cyberflorida.org/ci-bulletin-vol-2-issue-7-may-19-2026/).
- Viakoo Daily OT Security News (May 14, 2026) describes Sandworm escalating OT/ICS attacks via pre-compromised environments (no newly named wiper), a Foxconn ransomware attack, an AI-assisted water-utility attack, and FamousSparrow using existing Deed RAT — none a new wiper family [Daily OT Security News: May 14, 2026](https://www.viakoo.com/blog/daily-ot-security-news-may-14-2026/).

Since no qualifying new ICS/OT wiper strain was reported within the window by any listed outlet, and the only contemporaneous wiper (Lotus) is explicitly excluded, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-76. `009885f8-406c-570a-adbd-e63606108fea`

- Present date: `2026-05-16 00:31:01.295419`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Supreme Court of India reserve judgment on the constitutional validity of the Waqf (Amendment) Act, 2025, between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026, and no later than July 1, 2026 (23:59 IST), the Supreme Court of India formally reserves judgment on the constitutional validity of the Waqf (Amendment) Act, 2025. 

**"Reserve judgment"** is defined as the formal conclusion of oral arguments by all parties, after which the bench announces that the matter is reserved for judgment (i.e., a written decision will be delivered at a later date). This is a standard procedural step in Indian Supreme Court practice, distinct from delivering the final verdict itself.

The question resolves **No** if:
- Oral arguments have not concluded and judgment has not been reserved by July 1, 2026; or
- Judgment was reserved before May 12, 2026 (this would not count).

**Resolution source:** The official Supreme Court of India website (https://sci.gov.in) and its case status portal (https://sci.gov.in/case-status), or credible reporting from the Supreme Court Observer (https://www.scobserver.in/cases/constitutionality-of-the-waqf-amendment-act-2025-asaduddin-owaisi-v-union-of-india/), LiveLaw, or Bar and Bench.

**Pre-cutoff background**

The Waqf (Amendment) Act, 2025, was passed by India's Parliament and received presidential assent in April 2025. Over 65 petitions challenging the Act's constitutional validity were filed before the Supreme Court of India (Case No. W.P.(C) No. 269/2025) [Constitutionality of the Waqf (Amendment) Act, 2025](https://www.scobserver.in/cases/constitutionality-of-the-waqf-amendment-act-2025-asaduddin-owaisi-v-union-of-india/). On September 15, 2025, the Supreme Court delivered an interim judgment staying key provisions of the Act while the case remained pending on its merits [Constitutionality of the Waqf (Amendment) Act, 2025](https://www.scobserver.in/cases/constitutionality-of-the-waqf-amendment-act-2025-asaduddin-owaisi-v-union-of-india/). As of May 13, 2026, the case is listed as "Pending" on the Supreme Court Observer, and no final judgment or reservation of judgment on the merits has been recorded [Constitutionality of the Waqf (Amendment) Act, 2025](https://www.scobserver.in/cases/constitutionality-of-the-waqf-amendment-act-2025-asaduddin-owaisi-v-union-of-india/). Hearings on the substantive constitutional challenge have been ongoing, with oral arguments from dozens of petitioners and the Union of India. Given the scale of the case (65+ petitions covering multiple constitutional issues including freedom of religion, federalism, and property rights), the timeline for completing oral arguments remains uncertain.

**Exact later resolution packet**

The question resolves NO. It asks whether the Supreme Court of India formally reserved judgment on the MERITS (constitutional validity) of the Waqf (Amendment) Act, 2025 — i.e., concluded oral arguments by all parties — between May 12 and July 1, 2026 (23:59 IST).

Evidence gathered:

1. The only "reserved verdict/order" events found relate to the INTERIM stay, not the merits. The Supreme Court (CJI B.R. Gavai and Justice A.G. Masih) reserved its INTERIM order on May 22, 2025, after three days of arguments (May 20–22, 2025), and delivered the interim judgment (2025 INSC 1116) on September 15, 2025, staying certain provisions while keeping the case pending on merits. The NDTV "verdict reserved / In Hinduism" article was published May 22, 2025 and concerns that interim order, not a 2026 merits reservation [fec4a1].

2. As of the resolution window, the main constitutional challenge (W.P.(C) No. 269/2025) remained "Pending." Repeated queries of the designated resolution source, the Supreme Court Observer case page, show status "Pending" with no record of any reservation of judgment on the merits and no 2026 hearing culminating in reservation [5cd7e5][ade411]. The Bar and Bench live-updates page likewise shows hearings ongoing with no reservation of judgment reported [eed312].

3. The merits proceedings were still at a preliminary stage well into 2026: on January 28, 2026, the Supreme Court granted the Centre one week to respond to petitions challenging constitutional validity (Facebook/CapitalTV report; corroborated by search snippets). A 65+/70+ petition constitutional matter still at the "response" stage in late January 2026, before a reconstituted bench (CJI B.R. Gavai retired November 2025; CJI Surya Kant succeeded him), was not in a posture to have concluded all oral arguments and reserved judgment by July 1, 2026.

4. References to "August 2026" hearing dates in search results pertain to a separate Waqf matter (court-fee exemption before State Waqf Tribunals, Justices P.S. Narasimha and Aravind Kumar bench), not the main constitutional-validity challenge.

No credible source (SC Observer, LiveLaw, Bar and Bench, or sci.gov.in) reported the formal conclusion of oral arguments and reservation of judgment on the merits within the May 12 – July 1, 2026 window. Under the resolution criteria, the question resolves NO because oral arguments had not concluded and judgment had not been reserved by July 1, 2026.

Primary sources: SC Observer case page (https://www.scobserver.in/cases/constitutionality-of-the-waqf-amendment-act-2025-asaduddin-owaisi-v-union-of-india/) [5cd7e5][ade411]; Bar and Bench live updates (https://www.barandbench.com/news/litigation/waqf-amendment-act-case-live-updates-from-supreme-court) [eed312]; NDTV interim-order report (https://www.ndtv.com/india-news/supreme-court-waqf-hearing-news-waqf-case-verdict-reserved-in-hinduism-supreme-courts-reply-as-waqf-hearings-end-8480794) [fec4a1].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-77. `759e8c52-ee97-5e2b-a4eb-190fbd22775f`

- Present date: `2026-05-02 21:27:27.979877`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any major US airline (Delta, United, American, or Southwest) announce a further reduction in Q3 2026 capacity guidance during May 2026?

**Resolution criteria**

This question resolves **Yes** if any of the four airlines—Delta Air Lines, United Airlines, American Airlines, or Southwest Airlines—issues a public announcement on or after May 1, 2026, 00:00 UTC and before June 1, 2026, 00:00 UTC that explicitly reduces their planned Q3 2026 (July–September 2026) capacity compared to the most recent guidance issued by that airline prior to May 1, 2026.

**Definitions:**
- **"Capacity"** is defined as Available Seat Miles (ASMs), the standard airline industry metric representing seats available multiplied by miles flown. See: https://en.wikipedia.org/wiki/Available_seat_miles
- **"Additional"** means a downward revision relative to the most recent Q3 2026 capacity guidance or plan publicly communicated by the airline on or before April 30, 2026. The baselines are:
  - Delta: No explicit Q3 guidance yet; any announcement of Q3 capacity being cut below prior schedules or plans counts.
  - United: Q3 capacity flat to up ~2% YoY (announced April 21, 2026).
  - American: No explicit Q3 guidance yet; any announcement of Q3 capacity being cut below prior schedules or plans counts.
  - Southwest: ~2% annual capacity growth guidance; any explicit Q3 reduction below prior plans counts.
- **"Announcement"** means an official public communication via press release, SEC filing (e.g., 8-K), investor presentation, or earnings call transcript.

**Resolution sources** (official investor relations / press release pages):
- Delta: https://ir.delta.com/news/default.aspx
- United: https://ir.united.com/
- American: https://americanairlines.gcs-web.com/news-releases
- Southwest: https://www.southwestairlinesinvestorrelations.com/news-events/press-releases

If no such announcement is made by any of the four airlines before June 1, 2026, 00:00 UTC, the question resolves **No**.

**Pre-cutoff background**

As of May 1, 2026, major US airlines have already begun cutting capacity in response to elevated jet fuel costs. The current Q3 2026 capacity guidance for the four major carriers is as follows:

- **Delta Air Lines**: Guided to "flat capacity growth" for Q2 2026 (down from prior guidance of +3.5% YoY) with a stated "downward bias until the fuel environment improves." No specific Q3 2026 capacity guidance has been issued yet [Delta Air Lines Announces March Quarter 2026 Financial Results](https://ir.delta.com/news/news-details/2026/Delta-Air-Lines-Announces-March-Quarter-2026-Financial-Results/default.aspx).

- **United Airlines**: Plans a 5-point reduction in planned capacity for the rest of 2026. Q3 and Q4 2026 capacity is expected to be "flat to up approximately 2%" year-over-year, as announced on April 21, 2026.

- **American Airlines**: Provided Q2 2026 capacity guidance of ASMs up 4.0%–6.0% YoY. No specific Q3 2026 capacity guidance has been publicly issued as of the Q1 2026 earnings release on April 23, 2026 [American Airlines Reports First-Quarter 2026 Financial Results](https://americanairlines.gcs-web.com/news-releases/news-release-details/american-airlines-reports-first-quarter-2026-financial-results).

- **Southwest Airlines**: Projected annual capacity growth of approximately 2% (at the lower end of prior 2%–3% guidance), with Q1 2026 capacity up 1.5% YoY. No specific Q3 2026 capacity reduction has been announced [LUV Sees Modest Growth Expectations for 2026 - GuruFocus](https://www.gurufocus.com/news/8810645/luv-sees-modest-growth-expectations-for-2026?mobile=true).

The airline industry is under significant pressure from elevated fuel costs driven by rising oil prices. Delta and United have already made substantial capacity cuts. The question is whether any of these four carriers will announce *additional* reductions to their Q3 2026 capacity plans during May 2026, beyond the guidance already provided as of April 30, 2026.

Capacity in the airline industry is measured in Available Seat Miles (ASMs), defined as the number of seats available multiplied by the number of miles flown (see: https://en.wikipedia.org/wiki/Available_seat_miles).

**Exact later resolution packet**

The question resolves NO. None of the four carriers (Delta, United, American, Southwest) issued a public announcement between May 1, 2026 00:00 UTC and June 1, 2026 00:00 UTC that explicitly reduced their planned Q3 2026 (July–September 2026) capacity (ASMs) below the most recent guidance issued before May 1, 2026.

Evidence by carrier:

- UNITED: United's only May 2026 press release was a May 13 notice that it would present at Bernstein's 42nd Annual Strategic Decisions Conference on May 27 — it contained no capacity announcement [a8da5a]. At that May 27 Bernstein conference, CEO Scott Kirby's reported comments focused on ruling out airline consolidation; on capacity, Reuters reported United "has pulled some capacity where flights would burn cash" but "has not changed its broader strategy," i.e., no formal downward revision of the prior Q3 guidance of "flat to up approximately 2% YoY" [69e418]. The April 21/23 statement that United "will trim as much as 5% of its schedule in the third quarter if fuel prices don't come down" predates the May window and is the baseline, not a new May reduction.

- SOUTHWEST: At Bernstein on May 28, 2026, transcripts and summaries show Southwest emphasized strong demand (business revenue up ~25% YoY in March, sustained into April/May), strong margins, and cost discipline, with no reduction to its ~2% annual capacity growth plan [912e79][139801][b01325]. No explicit Q3 2026 ASM cut was announced.

- AMERICAN: American's only May 2026 IR communications were a May 20 notice of its Bernstein webcast and the late-May fireside chat; a Yahoo Finance roundup (May 8) noted American "hasn't officially announced any cancellations or fare hikes due to fuel shortages" [6ba009]. No explicit Q3 2026 ASM reduction announcement was found.

- DELTA: No May 2026 Delta announcement of a Q3 2026 capacity reduction was found; its prior position ("meaningfully reducing capacity growth, with a downward bias until the fuel environment improves") was stated in its April 8 Q1 results, before the window.

A comprehensive Reuters tracker of airline responses to the fuel surge (updated May 15, 2026) summarizing actions by all four carriers reported no new May 2026 Q3 capacity reductions for any of them [ebac68].

Since no qualifying announcement was made by any of the four airlines during May 2026, the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-78. `c25aff37-8182-557f-8968-564b01f226a2`

- Present date: `2026-05-03 01:45:09.969363`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. House of Representatives pass the KIDS Act (H.R. 7757) by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if H.R. 7757 (the KIDS Act, 119th Congress) is passed by the U.S. House of Representatives on or after April 30, 2026, and no later than June 1, 2026, at 11:59 PM UTC.

"Passed" means the bill receives a favorable vote by the full House of Representatives, whether by recorded vote, voice vote, or passage under suspension of the rules. The definitive resolution source is the bill's official actions page on Congress.gov: https://www.congress.gov/bill/119th-congress/house-bill/7757/all-actions

The question resolves **Yes** if that page shows an action indicating passage by the House (e.g., "Passed/agreed to in House") dated on or before June 1, 2026 (UTC). If no such action appears by that date, the question resolves **No**.

**Pre-cutoff background**

H.R. 7757, the Kids Internet and Digital Safety (KIDS) Act, was introduced in the U.S. House of Representatives on March 3, 2026, by Rep. Brett Guthrie [Actions - H.R.7757 - 119th Congress (2025-2026): KIDS Act](https://www.congress.gov/bill/119th-congress/house-bill/7757/all-actions). The bill aims to protect children and teens online, empower parents, and strengthen families. It incorporates several related measures including the Kids Online Safety Act (KOSA) and the AI Warnings And Resources for Education (AWARE) Act.

As of May 1, 2026, the bill has been referred to the House Committee on Energy and Commerce and the House Committee on the Judiciary [Actions - H.R.7757 - 119th Congress (2025-2026): KIDS Act](https://www.congress.gov/bill/119th-congress/house-bill/7757/all-actions). The House Energy and Commerce Committee has advanced the bill along party lines to a full House vote. However, no further floor action has been recorded on congress.gov as of this date [Actions - H.R.7757 - 119th Congress (2025-2026): KIDS Act](https://www.congress.gov/bill/119th-congress/house-bill/7757/all-actions).

Child online safety has bipartisan support in concept, and Senate companion legislation (S. 1748, the Kids Online Safety Act) also exists. However, House floor scheduling remains uncertain given competing legislative priorities, and the bill still needs to clear the Judiciary Committee or receive a discharge/waiver. The gap between committee passage and a full House floor vote makes the outcome within this timeframe genuinely uncertain.

**Exact later resolution packet**

The question resolves NO. It asks whether the full U.S. House of Representatives passed H.R. 7757 (the KIDS Act, 119th Congress) on or after April 30, 2026 and no later than June 1, 2026 at 11:59 PM UTC. "Passed" requires a favorable vote by the full House (recorded vote, voice vote, or suspension), not merely a committee advancement.

Evidence gathered:
- GovTrack's bill tracker for H.R. 7757 shows the bill at the "Introduced" stage (introduced March 3, 2026); the subsequent milestones "Passed Committee," "Passed House," "Passed Senate," and "Signed by the President" are all unfilled, indicating no House floor passage occurred [H.R. 7757: KIDS Act - GovTrack.us](https://www.govtrack.us/congress/bills/119/hr7757).
- FastDemocracy's tracking page for HR 7757 lists only the March 3, 2026 action (Introduced in House; referred to the Committee on Energy and Commerce and the Committee on the Judiciary). It records no floor vote and no House passage; its "Passed House," "Passed Senate," and "Became Law" milestones are unmarked [Bill tracking in US - HR 7757 (119 legislative session)](https://fastdemocracy.com/bill-search/us/119/bills/USB00103179/).
- Multiple news/press sources (e.g., the House Energy and Commerce Committee press release and IAPP coverage) confirm only that the committee advanced/passed H.R. 7757 along party lines to a full House vote — a committee action, not a floor vote. No source reports a full House floor passage.

The official Congress.gov actions page (https://www.congress.gov/bill/119th-congress/house-bill/7757/all-actions) could not be loaded directly during this research, but the corroborating trackers (GovTrack, FastDemocracy), which mirror Congress.gov data, both show no House floor passage action through the resolution window. Since no "Passed/agreed to in House" action appears on or before June 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-79. `5c6c82e6-d614-5f2b-915a-b62348cb4cda`

- Present date: `2026-05-12 17:55:04.552064`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the D.C. Circuit or Supreme Court issue a ruling on the merits of the Alien Enemies Act's applicability to Venezuelan deportees in J.G.G. v. Trump by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 10, 2026, and on or before July 1, 2026 (11:59 PM UTC), the United States Court of Appeals for the District of Columbia Circuit or the Supreme Court of the United States issues a written opinion or order that constitutes a **ruling on the merits** in *J.G.G. v. Trump* (D.C. Circuit No. 25-5067 or any consolidated/successor case) or a directly related case concerning the same plaintiffs and legal questions.

**Definition of "ruling on the merits"**: A ruling that addresses the substantive legal question of whether the Alien Enemies Act (50 U.S.C. §§ 21–24) lawfully authorizes the detention and/or removal of the Venezuelan nationals identified in the J.G.G. litigation. This includes rulings on statutory interpretation of the AEA (e.g., whether "invasion or predatory incursion" encompasses gang activity) or the constitutional validity of the AEA's application to these individuals. The following do **not** qualify: procedural orders, jurisdictional rulings, rulings on venue, stay orders, contempt rulings, or any order that does not address the substantive legality or constitutionality of invoking the AEA against these deportees.

This question resolves **No** if no such merits ruling is issued by 11:59 PM UTC on July 1, 2026.

**Resolution source**: The official opinion pages of the D.C. Circuit (https://www.cadc.uscourts.gov/internet/opinions.nsf) and the Supreme Court (https://www.supremecourt.gov/opinions/opinions.aspx), or credible legal reporting from SCOTUSblog (https://www.scotusblog.com/), Reuters, or the Associated Press confirming such a ruling.

**Pre-cutoff background**

In March 2025, President Trump invoked the Alien Enemies Act of 1798 (AEA, 50 U.S.C. §§ 21–24) to detain and deport Venezuelan nationals alleged to be members of the gang Tren de Aragua (TdA), claiming the gang's activities constituted an "invasion or predatory incursion" under the statute. Over 200 people were deported to El Salvador under this authority.

The case *J.G.G. v. Trump* (D.C. Circuit docket No. 25-5067; Supreme Court docket No. 24A931) is an emergency class action and habeas corpus lawsuit filed by the ACLU challenging this use of the AEA. Key procedural history includes:

- **March 2025**: U.S. District Judge James Boasberg (D.D.C.) issued a temporary restraining order (TRO) blocking further deportations under the AEA.
- **April 7, 2025**: The Supreme Court, in *Trump v. J.G.G.*, 604 U.S. ___ (2025), vacated the TRO on procedural grounds, holding that challenges must be brought as habeas petitions in the district of confinement. The Court explicitly did **not** reach the merits of the AEA's applicability [J.G.G. v. Trump - Wikipedia](https://en.wikipedia.org/wiki/J.G.G._v._Trump).
- **September 2025**: The Fifth Circuit ruled against Trump's use of the AEA in a related case.
- **January 22, 2026**: The D.C. Circuit heard oral arguments on the underlying appeal regarding the AEA's use [J.G.G. v. Trump - Wikipedia](https://en.wikipedia.org/wiki/J.G.G._v._Trump).
- **April 14, 2026**: The D.C. Circuit issued a writ of mandamus (No. 25-5452) halting Judge Boasberg's criminal contempt proceedings against administration officials, ruling the TRO was insufficiently clear to support contempt and the investigation intruded on Executive Branch autonomy. This was a **procedural** ruling, not a merits determination [[PDF] On Petition for Writ of Mandamus - United States Court of Appeals](https://media.cadc.uscourts.gov/opinions/docs/2026/04/25-5452-2168528.pdf).

As of May 11, 2026, no appellate court has issued a ruling on the merits of whether the AEA legally authorizes deportation of these Venezuelan nationals. The D.C. Circuit heard oral arguments on January 22, 2026, and a merits opinion could issue at any time. The Supreme Court could also grant certiorari and rule on the merits in a related proceeding.

Official dockets can be monitored at:
- D.C. Circuit: https://www.cadc.uscourts.gov/
- Supreme Court: https://www.supremecourt.gov/

**Exact later resolution packet**

The question resolves NO. It asked whether, between May 10, 2026 and July 1, 2026 (11:59 PM UTC), the D.C. Circuit or the Supreme Court issued a written opinion/order constituting a ruling on the MERITS of whether the Alien Enemies Act (AEA) lawfully authorizes detention/removal of the Venezuelan (Tren de Aragua) deportees in J.G.G. v. Trump or a directly related case with the same plaintiffs and legal questions. No such merits ruling was issued in that window.

Evidence:

1) D.C. Circuit activity in the window was purely procedural. Per the J.G.G. v. Trump Wikipedia article, the only D.C. Circuit action between May 10 and July 1, 2026 was the June 22, 2026 en banc order granting rehearing and vacating the April 2026 panel ruling that had halted Judge Boasberg's criminal contempt inquiry [5291de, 81a8b9]. This is a contempt/procedural matter — explicitly excluded by the resolution criteria (which bar "contempt rulings" and procedural orders). The D.C. Circuit heard merits oral argument on the AEA on January 22, 2026, but had NOT issued a merits opinion as of July 1, 2026; the merits appeal remained undecided [81a8b9]. The original stay appeal, No. 25-5067, was terminated as moot on June 24, 2025 [706b36].

2) The Supreme Court issued no AEA merits ruling in the window. Reuters' end-of-term coverage (June 28, 2026) listed the three major outstanding Trump rulings as the Federal Reserve governor firing, the FTC commissioner firing, and the birthright-citizenship executive order — not the AEA [77b117]. Reuters' June 29, 2026 preview of the term's final rulings (issued June 30) listed birthright citizenship, campaign-finance limits, and transgender-athlete cases — again, no AEA merits case [8f533e].

3) The June 25, 2026 Supreme Court rulings, which some sources loosely linked to immigration/AEA, were in fact NOT about the AEA merits. They were: (a) Mullin v. Al Otro Lado (No. 25-5), a 6-3 decision on the asylum "metering" policy holding that noncitizens standing in Mexico have not "arrived in the United States" (confirmed by SCOTUSblog, NPR, Reuters, Politico, and the Supreme Court opinion itself at supremecourt.gov/opinions/25pdf/25-5_86qd.pdf); and (b) a TPS-termination case allowing the government to end Temporary Protected Status for Syrian and Haitian nationals (this is what the Ballotpedia "June 25, 2026" emergency-orders entry actually described — TPS, not the AEA). Neither addresses whether the AEA authorizes removing the Venezuelan/TdA deportees.

4) The June 23, 2026 D.C. Circuit opinion in Make the Road New York v. Mullin (No. 25-5320) concerned nationwide expedited removal under 8 U.S.C. § 1225(b)(1) and due process — not the AEA merits [084bf1].

Because no D.C. Circuit or Supreme Court ruling on the substantive legality/constitutionality of the AEA's application to these deportees was issued between May 10 and July 1, 2026, the question resolves NO (0). The question is not a conditional, so no annulment applies.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-80. `17e0010e-2915-5ccc-8f2e-370b5620a78f`

- Present date: `2026-05-02 16:08:13.374285`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a federal court issue an injunction blocking the $100,000 H-1B presidential proclamation fee between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026, and before 11:59 PM Eastern Time on June 1, 2026, any U.S. federal court—including U.S. District Courts, U.S. Courts of Appeals (Circuit Courts), or the U.S. Supreme Court—issues an order that blocks, stays, enjoins, or otherwise prevents the enforcement of the $100,000 H-1B fee established by Presidential Proclamation 10973. This includes preliminary injunctions, permanent injunctions, temporary restraining orders (TROs), or stays pending appeal, regardless of whether the order applies nationwide or only to specific plaintiffs or jurisdictions.

This question resolves **No** if no such order is issued by any federal court within the specified timeframe.

A ruling that merely expresses disapproval of the fee or remands the case without an accompanying injunction or stay does not count. The order must have the practical effect of halting fee collection for at least some parties.

**Resolution source:** Official court dockets accessible via PACER (https://pacer.uscourts.gov/) or credible legal news reporting from outlets such as Reuters (https://www.reuters.com/legal/), Bloomberg Law (https://news.bloomberglaw.com/), Law360 (https://www.law360.com/), or Lawfare (https://www.lawfaremedia.org/).

**Pre-cutoff background**

On September 19, 2025, President Trump issued Presidential Proclamation 10973, "Restriction on Entry of Certain Nonimmigrant Workers," imposing a $100,000 fee on certain new H-1B visa petitions requesting consular notification, effective September 21, 2025 (https://www.federalregister.gov/documents/2025/09/24/2025-18601/restriction-on-entry-of-certain-nonimmigrant-workers).

The fee has been challenged in three federal lawsuits:

1. **Chamber of Commerce v. DHS** (D.D.C., then D.C. Circuit): On December 23, 2025, Judge Beryl Howell of the U.S. District Court for the District of Columbia upheld the fee and denied the Chamber's request for a preliminary injunction, finding the president acted within his authority under INA §§ 1182(f) and 1185(a) [Trump's $100K H-1B Visa Fee May Be Here to Stay | Lawfare](https://www.lawfaremedia.org/article/trump-s--100k-h-1b-visa-fee-may-be-here-to-stay). The Chamber appealed to the D.C. Circuit, which fast-tracked the case with oral argument held on March 9, 2026 [UPDATE: Status of Litigation Challenging the $100000 H-1B Cap ...](https://www.jdsupra.com/legalnews/update-status-of-litigation-challenging-3635825/). At oral argument, D.C. Circuit judges questioned whether the fee constituted an unlawful tax and whether judicial review was foreclosed. A decision is pending as of May 1, 2026.

2. **Global Nurse Force v. Trump** (N.D. Cal., Case No. 4:25-cv-08454): Filed October 3, 2025 by a coalition of labor unions, health care providers, schools, and religious organizations. A preliminary injunction hearing was scheduled for February 26, 2026 [UPDATE: Status of Litigation Challenging the $100000 H-1B Cap ...](https://www.jdsupra.com/legalnews/update-status-of-litigation-challenging-3635825/). The government requested a stay pending the D.C. Circuit decision.

3. **Multistate Attorneys General lawsuit** (D. Mass.): Filed December 2025 by 20 state attorneys general. Briefing on summary judgment was expected to conclude in mid-April 2026 [UPDATE: Status of Litigation Challenging the $100000 H-1B Cap ...](https://www.jdsupra.com/legalnews/update-status-of-litigation-challenging-3635825/).

As of May 1, 2026, the $100,000 fee remains in effect. The D.C. Circuit's decision in the Chamber case is the most likely near-term catalyst for a potential injunction or reversal. The California and Massachusetts cases also remain active and could independently produce injunctive relief.

**Exact later resolution packet**

The question resolves NO because no U.S. federal court issued any order blocking, staying, enjoining, or otherwise preventing enforcement of the $100,000 H-1B fee (Presidential Proclamation 10973) between May 1, 2026 and 11:59 PM ET June 1, 2026. I verified the status of all three named lawsuits:

1. **Chamber of Commerce v. DHS (D.C. Circuit, No. 25-5473):** The official PACER/CourtListener docket shows only procedural activity during the window — a May 6, 2026 response to a Rule 28(j) letter and a May 15, 2026 notice of attorney withdrawal. No decision, opinion, stay, or injunction was issued in May 2026 [Chamber of Commerce of the United States of Ameri v. DHS, 25-5473](https://www.courtlistener.com/docket/72095497/chamber-of-commerce-of-the-united-states-of-ameri-v-dhs/). (The underlying district court had previously upheld the fee on Dec. 23, 2025 and denied an injunction.)

2. **Global Nurse Force v. Trump (N.D. Cal., No. 4:25-cv-08454):** The docket shows no entries at all in May 2026; the last filing was a transcript order dated April 22, 2026. No injunction, stay, or order blocking the fee was issued during the window [Global Nurse Force v. Trump, 4:25-cv-08454 – CourtListener.com](https://www.courtlistener.com/docket/71541425/global-nurse-force-v-trump/).

3. **Multistate Attorneys General lawsuit (D. Mass., before Judge Leo Sorokin):** Reuters reported on May 29, 2026 that Judge Sorokin held a hearing at which he merely questioned the government's lawyer about the scope of the President's authority. This was oral argument only — no injunction, stay, or TRO was issued [US judge questions scope of Trump's power to impose ... - Reuters](https://www.reuters.com/legal/government/us-judge-questions-scope-trumps-power-impose-100000-h-1b-visa-fee-2026-05-29/). Law360 and Bloomberg Tax similarly reported only that the government was "pressed" on its authority at the hearing, not that any order issued.

Because the resolution criteria require an actual order with the practical effect of halting fee collection for at least some parties — and a mere ruling/hearing expressing disapproval or questioning the fee does not count — and because no such order issued in any of the three cases (or any other federal court) during May 1–June 1, 2026, the question resolves NO.

Sources:
- Chamber D.C. Circuit docket: https://www.courtlistener.com/docket/72095497/chamber-of-commerce-of-the-united-states-of-ameri-v-dhs/
- Global Nurse Force docket: https://www.courtlistener.com/docket/71541425/global-nurse-force-v-trump/
- Reuters (May 29, 2026): https://www.reuters.com/legal/government/us-judge-questions-scope-trumps-power-impose-100000-h-1b-visa-fee-2026-05-29/

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-81. `d95064ce-6216-5e03-8b91-7d74a9e7b723`

- Present date: `2026-05-29 04:20:11.527726`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the UK Crown Prosecution Service announce a charging decision regarding Andrew Mountbatten-Windsor by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026, and by 23:59 UTC on July 1, 2026, the Crown Prosecution Service (CPS) publicly announces a charging decision regarding Andrew Mountbatten-Windsor. A "charging decision" means either:

1. **A decision to charge:** The CPS formally authorizes the police to charge Andrew Mountbatten-Windsor with one or more criminal offences, as described in the CPS's own explanation of its decision-making process (https://www.cps.gov.uk/about-cps/how-we-make-our-decisions) [The CPS: How we make our decisions](https://www.cps.gov.uk/about-cps/how-we-make-our-decisions); OR
2. **A decision not to charge:** The CPS formally announces that it will not authorize charges (i.e., "no further action" or that the evidential or public interest test was not met).

The announcement must be made via an official CPS statement (e.g., published on the CPS news page at https://www.cps.gov.uk/news, or issued through the CPS press office to the media), OR confirmed by credible major UK news outlets such as the BBC (https://www.bbc.co.uk/news), The Guardian (https://www.theguardian.com/uk-news), or Reuters.

The question resolves as **No** if no such charging decision is publicly announced by the CPS by 23:59 UTC on July 1, 2026. Statements that the CPS is merely "continuing to advise" police or that the investigation is "ongoing" do not constitute a charging decision.

Note: If a charging decision was already announced before May 12, 2026, that does not count; only decisions announced on or after May 12, 2026 (UTC) are eligible.

**Pre-cutoff background**

Andrew Mountbatten-Windsor (formerly Prince Andrew) was arrested on February 18–19, 2026, on suspicion of misconduct in public office, in connection with investigations into his links with Jeffrey Epstein. He was released under investigation after almost 11 hours in police custody. As of early April 2026, the Crown Prosecution Service (CPS) confirmed it was providing "investigative advice" to the police forces investigating him. As of May 13, 2026, no charging decision has been publicly announced.

The CPS is the principal public prosecution service for England and Wales. It applies a two-stage "Full Code Test" to every case: (1) the evidential stage, assessing whether there is a "realistic prospect of conviction," and (2) the public interest stage, assessing whether prosecution serves the public interest [The CPS: How we make our decisions](https://www.cps.gov.uk/about-cps/how-we-make-our-decisions). For serious and complex offences such as misconduct in public office, the CPS — not the police — makes the charging decision. Complex, high-profile cases can take weeks to many months after police submit their files before a decision is reached. There is genuine uncertainty about whether a decision will come before July 1, 2026, given the complexity of the case, the number of police forces involved, and the volume of evidence likely under review.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question asks whether the UK Crown Prosecution Service (CPS) publicly announced a definitive charging decision (to charge OR not to charge) regarding Andrew Mountbatten-Windsor between May 12, 2026 and 23:59 UTC on July 1, 2026. The evidence shows no such CPS charging decision was announced within that window; the matter remained at the investigation stage throughout.

KEY EVIDENCE (chronological, from eligible/high-quality sources):

1. Late May 2026 — Investigation still active, no charging decision. A BBC News article (published May 30, 2026) confirmed the CPS was only providing "investigative advice" to police and that there was "an ongoing police enquiry concerning Mr Mountbatten-Windsor." Thames Valley Police had issued a fresh appeal for information, and no charging decision was reported [Palace was handed Andrew's controversial envoy emails six years ...](https://www.bbc.com/news/articles/cy02j5pl98no). Contemporaneous NYT (May 22) and LA Times/PBS coverage confirmed police were still broadening the inquiry and appealing for witnesses — clearly a pre-charge investigative phase.

2. Early June 2026 — DPP explicitly says a decision is far off. On June 4–5, 2026, the Director of Public Prosecutions Stephen Parkinson told reporters it "would not be at all surprising if it took over a year" for the investigations into Mountbatten-Windsor (and Lord Mandelson) to conclude, citing complexity and international dimensions. The reporting explicitly states "Neither has been charged" as of that date and that the CPS was still only providing early investigative advice [Investigations into Andrew and Mandelson could take 'over ...](https://news.sky.com/story/investigations-into-mandelson-and-andrew-could-take-more-than-a-year-cps-chief-says-13550925) [Epstein Files: UK Inquiry Into Andrew May Take Over a Year](https://easternherald.com/2026/06/05/epstein-files-uk-inquiry-andrew-mandelson-survivors-justice/). This makes clear no charging decision was imminent, let alone made, in the resolution window.

3. No source (CPS website, BBC, The Guardian, or Reuters) reported any CPS charging decision — neither an authorization to charge nor a "no further action" / test-not-met announcement — at any point between May 12 and July 1, 2026. My repeated targeted searches for a charging decision in June/late-June 2026 returned only ongoing-investigation coverage.

POLICE vs CPS DISTINCTION: The resolution criteria require the decision-maker to be the CPS. One separate, narrow item surfaced in searches — police (not the CPS) saying they would "take no further action" over a specific claim that Andrew asked a protection officer to obtain information. That is (a) a police decision, not a CPS charging decision, and (b) concerns a discrete sub-allegation, not a definitive CPS charging decision on the misconduct-in-public-office case. It therefore does not satisfy the criteria. The overarching misconduct-in-public-office matter — for which the CPS (not the police) makes the charging decision — remained under investigation with no CPS charging decision announced.

Because statements that the CPS is "continuing to advise" police or that the investigation is "ongoing" explicitly do NOT count as a charging decision under the resolution criteria, and because the DPP himself indicated the process could take over a year, the question resolves NO.

This is not a conditional question, so no annulment applies.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-82. `786d93d1-0fe1-5295-931c-5016ba7b7a4e`

- Present date: `2026-05-02 21:38:17.411991`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Amazon officially announce the specific calendar dates for Prime Day 2026 before June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if Amazon publishes an official announcement on or after May 1, 2026 (and before 11:59 PM UTC on May 31, 2026) that explicitly states the specific calendar dates for Prime Day 2026 (e.g., "June 17–20").

An "official announcement" is defined as a press release or blog post published on Amazon's official news site (https://www.aboutamazon.com/news/) that specifies the exact start and end dates of Prime Day 2026.

The primary resolution source is Amazon's Press Center at: https://www.aboutamazon.com/news/retail

This question resolves **No** if:
- No such announcement specifying the exact calendar dates appears on aboutamazon.com by 11:59 PM UTC on May 31, 2026, OR
- Amazon announces that Prime Day 2026 is cancelled or indefinitely postponed before that deadline.

Note: Amazon's April 29, 2026 announcement that Prime Day will occur "in June" [Amazon's Prime Day event is back this June](https://www.aboutamazon.com/news/retail/amazon-prime-day-june-2026) does NOT count as announcing the specific dates, as it did not specify the exact calendar dates of the event.

**Pre-cutoff background**

Amazon Prime Day is an annual members-only shopping event. Amazon has historically announced specific dates for Prime Day approximately 3 weeks before the event begins.

Historical announcement timeline:
- **2023**: Amazon announced on June 21, 2023 that Prime Day would be July 11–12 (~20 days before the event). Source: aboutamazon.com/news/retail/amazon-prime-day-2023-date
- **2024**: Amazon announced on June 25, 2024 that Prime Day would be July 16–17 (~21 days before the event). Source: aboutamazon.com/news/retail/amazon-prime-day-2024-date
- **2025**: Amazon announced in mid-June 2025 that Prime Day would be July 8–11 (~21 days before the event). Source: aboutamazon.com/news/retail/amazon-prime-day-2025-date

**Current status of Prime Day 2026**: On April 29, 2026, Amazon published an official blog post confirming that Prime Day 2026 will take place in June 2026 — a shift from its usual July timing [Amazon's Prime Day event is back this June](https://www.aboutamazon.com/news/retail/amazon-prime-day-june-2026). However, Amazon has not yet announced the specific calendar dates (e.g., "June 16–19"), stating only: "Stay tuned—we'll share more details as the event approaches" [Amazon's Prime Day event is back this June](https://www.aboutamazon.com/news/retail/amazon-prime-day-june-2026). The event will be held across 26 countries.

Given that Prime Day 2026 is scheduled for June rather than July, and Amazon typically announces specific dates about 3 weeks before the event, the announcement of exact dates could plausibly come in late May (before June 1) or in early June (after June 1). This creates genuine forecasting uncertainty.

**Exact later resolution packet**

The question resolves NO because Amazon did not publish an official announcement specifying the exact calendar dates of Prime Day 2026 on aboutamazon.com/news/ during the resolution window (May 1, 2026 through 11:59 PM UTC May 31, 2026).

Key evidence:
- Amazon's official news article specifying the exact dates ("When is Amazon Prime Day 2026? Shop deals June 23-26") at https://www.aboutamazon.com/news/retail/amazon-prime-day-2026-date carries a byline publication date of June 1, 2026 [dacf35]. This is OUTSIDE the May 1–31 window (which closes at 11:59 PM UTC on May 31, 2026), so it cannot trigger a YES resolution.
- The original April 29, 2026 blog post (https://www.aboutamazon.com/news/retail/amazon-prime-day-june-2026) only announced the event would be "in June." The resolution criteria explicitly exclude this April 29 post from counting as a date announcement [fa178f]. (Note: that page now displays "June 23 to 26," but its publication date is April 29, 2026, and the specific dates appear to have been added via update around June 1, 2026, when related dated articles appeared.)
- Multiple major media outlets (9to5Toys, Condé Nast Traveler, Chicago Tribune, E! Online) reported the official date announcement on June 2, 2026, describing it as a fresh "official announcement on the Amazon News page" [74f83d], consistent with the dates being officially announced no earlier than June 1, 2026 — not during May.

Since no official announcement specifying the exact calendar dates appeared on aboutamazon.com before the May 31, 2026 deadline, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-83. `354884fe-183d-5a76-b6b3-bc013a60ce41`

- Present date: `2026-05-02 17:58:56.730071`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will PIF announce the sale of a majority stake in at least one of Al Nassr, Al Ahli, or Al Ittihad between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026, and by June 1, 2026, 11:59 PM UTC, an official announcement is made confirming that PIF has agreed to sell a majority stake (defined as more than 50% of equity or voting rights) in at least one of Al Nassr, Al Ahli, or Al Ittihad. The announcement must exclude the prior sale of Al Hilal (announced April 16, 2026).

Resolution will be based on credible reporting from major international news agencies or sports outlets, including but not limited to:
- Reuters (https://www.reuters.com)
- Associated Press / AP News (https://apnews.com)
- Bloomberg (https://www.bloomberg.com)
- ESPN (https://www.espn.com)
- The Athletic / New York Times (https://www.nytimes.com/athletic/)

Alternatively, an official announcement on the PIF website (https://www.pif.gov.sa) would also suffice.

The question resolves **No** if no such announcement is reported by the deadline.

**Pre-cutoff background**

In 2023, the Saudi Public Investment Fund (PIF) acquired controlling interests in four major Saudi Pro League clubs: Al Hilal, Al Nassr, Al Ahli, and Al Ittihad [https://www.espn.com/soccer/story/_/id/48504792/saudi-public-investment-fund-sells-stake-al-hilal](https://www.espn.com/soccer/story/_/id/48504792/saudi-public-investment-fund-sells-stake-al-hilal). On April 16, 2026, PIF announced the sale of a 70% stake in Al Hilal to Kingdom Holding Company for approximately €350 million [https://www.espn.com/soccer/story/_/id/48504792/saudi-public-investment-fund-sells-stake-al-hilal](https://www.espn.com/soccer/story/_/id/48504792/saudi-public-investment-fund-sells-stake-al-hilal). As of May 1, 2026, PIF retains its controlling stakes in the three remaining clubs: Al Nassr, Al Ahli, and Al Ittihad. No official announcements have been made regarding the sale of stakes in these clubs. The Al Hilal sale signals PIF's broader strategy to divest from direct club ownership, but the timeline for further sales remains uncertain. Reports suggest Al Ahli and Al Ittihad are next in line, while Al Nassr (home to Cristiano Ronaldo) is also being monitored closely by stakeholders.

**Exact later resolution packet**

The question asks whether PIF announced the sale of a majority stake (>50%) in at least one of Al Nassr, Al Ahli, or Al Ittihad between April 30, 2026 and June 1, 2026 (11:59 PM UTC), excluding the prior Al Hilal sale.

Findings:
- The only confirmed PIF club divestment is the Al Hilal sale, announced April 16, 2026, in which Kingdom Holding Company signed a binding agreement to acquire 70% of Al Hilal. This is explicitly EXCLUDED by the resolution criteria. This is confirmed on the official PIF website press release page (https://www.pif.gov.sa/en/news-and-insights/press-releases/2026/pif-and-kingdom-holding-company-khc-sign-agreement-for-khc-to-acquire-70-of-al-hilal-club-company/) and via ESPN (https://www.espn.com/soccer/story/_/id/48504792/) and The Athletic (https://www.nytimes.com/athletic/7201654/2026/04/16/al-hilal-saudi-arabia-pif-sale/).
- I reviewed the official PIF press releases listing for 2026 (https://www.pif.gov.sa/en/news-and-insights/press-releases/2026/), which contains NO announcement regarding the sale of a majority stake in Al Nassr, Al Ahli, or Al Ittihad in the April 30 – June 1, 2026 window [5ce142]. The only football-club divestment listed is the excluded Al Hilal deal.
- Multiple searches across the listed credible sources (Reuters, AP, Bloomberg, ESPN, The Athletic/NYT) for May 2026 returned only coverage of the April Al Hilal sale, plus reports/speculation that sales of Al Nassr, Al Ittihad, and Al Ahli would follow "over the coming years" and that "negotiations with interested private investors" were ongoing — i.e., mere interest/negotiations, not a confirmed agreement.
- A PIF fund manager comment circulated about announcing "the sale of our stake in one of the sports clubs within two days," but this related to the April Al Hilal context, and no subsequent official announcement for any of the three remaining clubs materialized in the resolution window.

Since no official announcement confirming the sale of a majority stake in Al Nassr, Al Ahli, or Al Ittihad was made between April 30 and June 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-84. `3c29a467-1406-55a9-8808-e1b3616c145e`

- Present date: `2026-05-01 13:56:25.284016`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. Department of Commerce formally add Hua Hong Semiconductor (or any subsidiary) to the Entity List by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 and no later than 11:59 PM UTC on June 1, 2026, the U.S. Department of Commerce's Bureau of Industry and Security (BIS) formally adds Hua Hong Semiconductor Limited—or any subsidiary thereof (including but not limited to Huali Microelectronics / Shanghai Huali Microelectronics Corporation)—to the [Entity List](https://www.bis.gov/entity-list) (Supplement No. 4 to Part 744 of the Export Administration Regulations, [15 CFR § 744](https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-744)).

Resolution depends on official publication in the [Federal Register](https://www.federalregister.gov/agencies/industry-and-security-bureau) or official filing for public inspection, not merely news reports or rumored drafts. The addition must appear as a final rule or interim final rule published or filed for public inspection by 11:59 PM UTC on June 1, 2026.

The resolution source is the Federal Register's BIS page: https://www.federalregister.gov/agencies/industry-and-security-bureau and/or the BIS Entity List page: https://www.bis.gov/entity-list.

If no such formal addition is published or filed for public inspection by the deadline, this question resolves **No**.

**Pre-cutoff background**

On April 28, 2026, the U.S. Department of Commerce issued "is-informed" letters to major chip equipment suppliers—including Lam Research, Applied Materials, and KLA—ordering them to halt certain shipments to two Hua Hong facilities (Fab 6 and 8a) [https://www.reuters.com/world/china/us-orders-chip-equipment-companies-halt-some-shipments-hua-hong-chinas-second-2026-04-28/](https://www.reuters.com/world/china/us-orders-chip-equipment-companies-halt-some-shipments-hua-hong-chinas-second-2026-04-28/). This action was prompted by U.S. concerns that Hua Hong Semiconductor Limited and its subsidiary, Huali Microelectronics, may be manufacturing advanced 7-nanometer (7nm) chips [https://www.reuters.com/world/china/us-orders-chip-equipment-companies-halt-some-shipments-hua-hong-chinas-second-2026-04-28/](https://www.reuters.com/world/china/us-orders-chip-equipment-companies-halt-some-shipments-hua-hong-chinas-second-2026-04-28/).

"Is-informed" letters are an interim enforcement mechanism that allows the U.S. government to quickly impose new licensing requirements on specific entities, bypassing the lengthy formal rule-writing process [https://www.reuters.com/world/china/us-orders-chip-equipment-companies-halt-some-shipments-hua-hong-chinas-second-2026-04-28/](https://www.reuters.com/world/china/us-orders-chip-equipment-companies-halt-some-shipments-hua-hong-chinas-second-2026-04-28/). Historically, such letters have sometimes preceded formal Entity List additions (as occurred with other Chinese chipmakers), but not always—they do not guarantee a formal designation will follow [https://www.reuters.com/world/china/us-orders-chip-equipment-companies-halt-some-shipments-hua-hong-chinas-second-2026-04-28/](https://www.reuters.com/world/china/us-orders-chip-equipment-companies-halt-some-shipments-hua-hong-chinas-second-2026-04-28/).

The [Entity List](https://www.bis.gov/entity-list) is maintained by the Bureau of Industry and Security (BIS) under Supplement No. 4 to Part 744 of the Export Administration Regulations (EAR). Entities placed on this list are subject to specific license requirements for the export, reexport, and transfer (in-country) of specified items. Additions to the Entity List are published in the Federal Register.

As of April 30, 2026, Hua Hong Semiconductor is subject to the interim "is-informed" restrictions but has not been formally added to the Entity List.

**Exact later resolution packet**

The question asks whether BIS formally added Hua Hong Semiconductor Limited (or any subsidiary, including Huali Microelectronics) to the Entity List (Supplement No. 4 to Part 744 of the EAR) via publication or filing for public inspection in the Federal Register between April 30, 2026 and 11:59 PM UTC June 1, 2026.

The antecedent context (the April 28, 2026 "is-informed" letters halting equipment shipments to Hua Hong Fab 6 and 8a) is well established by Reuters reporting. However, those "is-informed" letters are explicitly NOT formal Entity List additions, and the question requires a formal designation published as a final or interim final rule in the Federal Register.

A direct search of the Federal Register filtered to the Bureau of Industry and Security (BIS) and the term "entity list" for the year 2026 (https://www.federalregister.gov/documents/search?conditions[agencies][]=industry-and-security-bureau&conditions[term]=entity+list&conditions[publication_date][year]=2026) returned no rule adding Hua Hong Semiconductor or Huali Microelectronics to the Entity List in May 2026 or at any point through June 1, 2026 [e84edf]. The only BIS documents found in this period were administrative information-collection notices (02/27/2026 and 05/21/2026) and an unrelated enforcement order (Hans De Geetere, 05/29/2026) — none of which constitute an Entity List addition of Hua Hong or its subsidiaries [e84edf].

No high-quality news source (Reuters, etc.) reported a formal Entity List addition of Hua Hong during the window; coverage remained focused on the interim "is-informed" letters and the broader equipment-shipment halts. Since no formal addition was published or filed for public inspection by the deadline, the question resolves NO per its explicit terms ("If no such formal addition is published or filed for public inspection by the deadline, this question resolves No").

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-85. `2baf84ab-2795-5ade-a60f-0187fdeef939`

- Present date: `2026-05-01 11:51:02.136906`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-05-31 00:00:00`

**Question**

Will EU High Representative Kaja Kallas publicly call for additional Iran sanctions beyond the Hormuz expansion agreement between April 30 and May 31, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 (00:00 UTC) and on or before May 31, 2026 (23:59 UTC), EU High Representative for Foreign Affairs and Security Policy Kaja Kallas publicly calls for additional sanctions against Iran beyond those already agreed as of April 30, 2026.

**Definitions:**

- **"Already agreed" sanctions as of April 30, 2026**: The existing EU Iran sanctions regime, including the IRGC terrorist designation (January 2026), human rights listings (March 2026), and the Hormuz expansion agreement reached at the April 21 Foreign Affairs Council (i.e., expanding sanctions criteria to cover obstruction of the Strait of Hormuz) [EU to widen Iran sanctions to those who block Hormuz - Reuters](https://www.reuters.com/world/middle-east/eu-widen-iran-sanctions-those-who-block-hormuz-2026-04-20/). Administrative implementation steps for these already-agreed sanctions (e.g., formally listing specific individuals under the Hormuz criteria) do NOT count as "additional sanctions."

- **"Additional sanctions"**: Any new restrictive measures, expanded sanctions criteria, or new policy proposals targeting Iran that go beyond the scope of the sanctions already agreed as of April 30, 2026. Examples include: new sectoral sanctions (e.g., energy, trade), new designations under novel criteria not yet agreed, or calls for entirely new sanctions frameworks. Merely calling for faster implementation of existing agreed measures does not qualify.

- **"Publicly call"**: A statement by Kallas in her official capacity that explicitly advocates for, proposes, or urges the adoption of additional sanctions against Iran. This must appear in at least one of: (a) official EEAS channels (https://www.eeas.europa.eu/eeas/press-material_en), (b) verified social media accounts of Kallas or the EEAS, (c) direct quotes attributed to Kallas in major international news outlets (Reuters, AP, AFP, Bloomberg, or equivalent). Vague warnings about "keeping options open" or "not ruling anything out" do not qualify; the statement must specifically reference new or additional sanctions.

**Resolution source**: The EEAS press room (https://www.eeas.europa.eu/eeas/press-material_en) and/or credible reporting from Reuters (https://www.reuters.com), AP, AFP, or Bloomberg containing direct quotes from Kallas.

If no qualifying public call is identified by 23:59 UTC on May 31, 2026, the question resolves **No**.

**Pre-cutoff background**

As of April 30, 2026, the EU-Iran relationship is shaped by the ongoing US-Israel-Iran conflict that began on February 28, 2026, and Iran's closure of the Strait of Hormuz. Key developments include:

- **Ceasefire**: The US and Iran agreed to a two-week ceasefire on April 8, 2026, welcomed by EU leaders [EU to widen Iran sanctions to those who block Hormuz - Reuters](https://www.reuters.com/world/middle-east/eu-widen-iran-sanctions-those-who-block-hormuz-2026-04-20/).
- **Hormuz sanctions expansion**: On April 20-21, 2026, EU ambassadors reached a political agreement to expand the criteria of the EU's Iran sanctions regime to include individuals and entities responsible for obstructing freedom of navigation in the Strait of Hormuz [EU to widen Iran sanctions to those who block Hormuz - Reuters](https://www.reuters.com/world/middle-east/eu-widen-iran-sanctions-those-who-block-hormuz-2026-04-20/). Kallas announced this agreement at the Foreign Affairs Council on April 21, 2026.
- **Prior sanctions**: The EU designated Iran's Revolutionary Guards (IRGC) as a terrorist organization in January 2026 and listed Iranian officials for human rights violations in March 2026 [EU to widen Iran sanctions to those who block Hormuz - Reuters](https://www.reuters.com/world/middle-east/eu-widen-iran-sanctions-those-who-block-hormuz-2026-04-20/).
- **Kallas's posture**: As of April 28, 2026, Kallas warned of the "dangerous precedence" set by the continued Hormuz blockade [EU's Kallas warns of 'dangerous precedence' as Hormuz remains ...](https://www.aa.com.tr/en/europe/eu-s-kallas-warns-of-dangerous-precedence-as-hormuz-remains-blocked-2-months-into-iran-war/3920061), but had not yet publicly called for sanctions beyond the Hormuz expansion agreement.
- **Diplomatic context**: Iran reportedly offered the US a new proposal to reopen the Strait of Hormuz around April 27, 2026, and EU leaders vowed to boost security and economic ties with Middle East partners.

The situation remains volatile. Whether Kallas calls for further measures depends on the trajectory of the ceasefire, Hormuz reopening negotiations, and broader Iran-EU relations in May 2026.

**Exact later resolution packet**

NO. I found no qualifying public call by Kaja Kallas during the April 30–May 31, 2026 window. The relevant official EEAS material I checked shows only already-agreed Hormuz-related sanctions activity, or non-sanctions diplomacy/operations, not an explicit call for additional sanctions beyond the April 2026 Hormuz expansion, January 2026 IRGC designation, and March 2026 human-rights listings.

Key evidence:
- The pre-window baseline EEAS page from April 21, 2026 records Kallas saying the EU had reached political agreement “to widen our sanctions regime to also target those responsible for breaches to freedom of navigation,” and that the “new proposal” was to address those limiting freedom of navigation in the Strait of Hormuz, with work continuing toward the May Foreign Affairs Council. This is the Hormuz expansion expressly excluded by the question and it also predates the resolution window: https://www.eeas.europa.eu/eeas/foreign-affairs-council-press%C2%A0remarks%C2%A0-high-representative-kaja-kallas%C2%A0-press-conference_en [Foreign Affairs Council: Press remarks by High Representative Kaja ...](https://www.eeas.europa.eu/eeas/foreign-affairs-council-press%C2%A0remarks%C2%A0-high-representative-kaja-kallas%C2%A0-press-conference_en).
- The May 11, 2026 EEAS press conference page states: “The EU is expanding its Iran sanctions to also include those responsible for obstructing freedom of navigation.” That matches implementation/continuation of the already-agreed Hormuz expansion, not a new or additional sanctions proposal beyond the baseline: https://www.eeas.europa.eu/eeas/foreign-affairs-council-press-conference-high-representative-kaja-kallas-4_en [Press conference by High Representative Kaja Kallas - EEAS](https://www.eeas.europa.eu/eeas/foreign-affairs-council-press-conference-high-representative-kaja-kallas-4_en).
- The May 11, 2026 EEAS arrival remarks page discusses diplomacy, the Strait of Hormuz, and possible Operation ASPIDES operational changes, but contains no explicit Kallas call for new/additional Iran sanctions: https://www.eeas.europa.eu/eeas/foreign-affairs-council-press-remarks-high-representative-kaja-kallas-upon-arrival-9_en [Press remarks by High Representative Kaja Kallas upon arrival | EEAS](https://www.eeas.europa.eu/eeas/foreign-affairs-council-press-remarks-high-representative-kaja-kallas-upon-arrival-9_en).
- The May 18, 2026 EEAS remarks page discusses external action, the humanitarian/economic impact of the Iran war, regional cooperation, and freedom of navigation, but contains no call for additional Iran sanctions; Kallas is summarized as saying the EU had limited leverage over the US-Iran conflict: https://www.eeas.europa.eu/eeas/foreign-affairs-council-development-press-remarks-high-representative-kaja-kallas-upon-arrival-0_en [Press remarks by High Representative Kaja Kallas upon arrival | EEAS](https://www.eeas.europa.eu/eeas/foreign-affairs-council-development-press-remarks-high-representative-kaja-kallas-upon-arrival-0_en).

Because the only Iran-sanctions statement I found inside the window concerns the Hormuz expansion already agreed before April 30, and because the other in-window official EEAS remarks I checked contain no explicit sanctions call, the resolution criteria for YES are not met. Under the stated criteria, if no qualifying public call is identified by May 31, 2026 at 23:59 UTC, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-86. `559e0736-ec8f-51b2-88cc-9991be4c568c`

- Present date: `2026-05-02 19:38:46.158749`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the FCC formally adopt final rules prohibiting the use of equipment produced by Covered List entities in submarine cable systems connecting to the United States by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 1, 2026 (12:00 AM ET) and by June 1, 2026 (11:59 PM ET), the FCC formally adopts final rules that explicitly prohibit the use of equipment or services produced or provided by entities on the FCC's "Covered List" (https://www.fcc.gov/supplychain/coveredlist) in submarine cable systems connecting to the United States.

**"Formally adopt"** means a majority vote by the FCC Commissioners approving a final Report and Order, as evidenced by the publication of such order on the FCC's Electronic Document Management System (EDOCS, https://www.fcc.gov/edocs) or in the Federal Register (https://www.federalregister.gov/).

**"Chinese technology or equipment"** is defined as equipment or services produced or provided by entities appearing on the FCC's Covered List established pursuant to the Secure and Trusted Communications Networks Act of 2019 (Section 2), as published at https://www.fcc.gov/supplychain/coveredlist. This list includes Chinese telecommunications manufacturers such as Huawei Technologies Company and ZTE Corporation, among others.

The question resolves as **No** if no such final rules are adopted by 11:59 PM ET on June 1, 2026, or if only a Notice of Proposed Rulemaking, Further Notice, or interim guidance (rather than a final Report and Order) is issued during this period.

**Resolution source:** FCC EDOCS (https://www.fcc.gov/edocs) and/or the Federal Register (https://www.federalregister.gov/).

**Pre-cutoff background**

The Federal Communications Commission (FCC) has been progressively tightening restrictions on foreign adversary involvement in U.S. submarine cable infrastructure. In August 2025, the FCC adopted the "Submarine Cable Report and Order" (FCC 25-49, GN Docket No. 25-166), which established a presumption that foreign adversary applicants are not qualified to hold cable landing licenses and prohibited foreign adversary entities from installing, owning, or managing Submarine Line Terminal Equipment (SLTE) on submarine cables landing in the United States [[PDF] Foreign Adversary Control Report and Order – GN Docket No. 25-166](https://docs.fcc.gov/public/attachments/DOC-417578A1.pdf). In an accompanying "Submarine Cable Further Notice," the Commission proposed to go further by restricting the use of any equipment produced by entities on the FCC's "Covered List" in the operation of submarine cable systems [[PDF] Foreign Adversary Control Report and Order – GN Docket No. 25-166](https://docs.fcc.gov/public/attachments/DOC-417578A1.pdf).

As of April 29, 2026, FCC Chair Brendan Carr has stated the agency plans to adopt rules barring undersea cable connections to the U.S. that utilize Chinese technology or equipment [https://www.reuters.com/world/key-us-senator-call-new-efforts-prevent-undersea-cable-sabotage-2026-04-29/](https://www.reuters.com/world/key-us-senator-call-new-efforts-prevent-undersea-cable-sabotage-2026-04-29/). The FCC's "Covered List" (https://www.fcc.gov/supplychain/coveredlist) identifies communications equipment and services deemed to pose an unacceptable risk to U.S. national security, and currently includes entities such as Huawei Technologies, ZTE Corporation, Hytera Communications, Hikvision, and Dahua, among others.

The rulemaking process typically requires the FCC to issue a Notice of Proposed Rulemaking, collect public comments, and then vote on a final Report and Order. While the NPRM and comment period for the submarine cable equipment restrictions have been completed, the final Report and Order has not yet been adopted as of May 1, 2026. Given the stated intent of FCC leadership, formal adoption could occur at an upcoming FCC open meeting, but the timeline remains uncertain.

**Exact later resolution packet**

The question resolves NO because the FCC did not formally adopt a final Report and Order prohibiting the use of Covered List entity equipment in submarine cable systems during the resolution window of May 1, 2026 (12:00 AM ET) to June 1, 2026 (11:59 PM ET).

Key evidence:

1. The FCC's resolution window contained two relevant decision-making opportunities. The April 30, 2026 Commission meeting fell just before the window. The items adopted at that meeting did NOT include any submarine cable equipment final Report and Order. The Covered List-related item adopted then was a Notice of Proposed Rulemaking (FCC 26-29, WC Docket No. 26-82, "Protecting Against National Security Threats in Domestic Telecommunications Service"), which proposes to exclude Covered List entities from blanket domestic section 214 authority for interstate telecommunications services — not submarine cables — and is a proposal, not a final rule [Daily Digest - Federal Communications Commission](https://www.fcc.gov/edocs/daily-digest/2026/04/30) [[PDF] Federal Communications Commission FCC 26-29 1](https://docs.fcc.gov/public/attachments/FCC-26-29A1.pdf) [[PDF] April 9, 2026 FCC FACT SHEET* Protecting Against National ...](https://docs.fcc.gov/public/attachments/DOC-420715A1.pdf).

2. The only FCC Open Meeting within the resolution window was on May 20, 2026. Its four agenda items were: Enhancing Know-Your-Upstream-Provider Requirements (FNPRM); Streamlining Broadband Data Processes (R&O and FNPRM); Modernizing the Disaster Information Reporting System (Third R&O); and Launching a 'High-Cost' Program Initiative (NPRM). None of these concerned prohibiting Covered List equipment in submarine cable systems [May 2026 Open Commission Meeting](https://www.fcc.gov/May2026).

3. The submarine cable equipment prohibition the question refers to originated as a Further Notice of Proposed Rulemaking accompanying the August 2025 Submarine Cable Report and Order (FCC 25-49). As of the resolution window, this remained a pending proposal; no final Report and Order adopting it was found in FCC EDOCS or the Federal Register for the May 1–June 1, 2026 period.

4. The Foreign Adversary Control Report and Order (FCC 26-2, GN Docket No. 25-166) was adopted January 29, 2026 — before the window — and concerned foreign adversary control/reporting, not a Covered List equipment prohibition for submarine cables (Federal Register 2026-06992, published April 10, 2026).

Because no final Report and Order explicitly prohibiting Covered List equipment in submarine cable systems was formally adopted (by majority vote, evidenced in EDOCS or the Federal Register) between May 1 and June 1, 2026, the question resolves NO per its resolution criteria, which specify that issuance of only an NPRM, Further Notice, or interim guidance results in a NO.

Relevant URLs: FCC Daily Digest April 30, 2026 (https://www.fcc.gov/edocs/daily-digest/2026/04/30); FCC May 2026 Open Meeting page (https://www.fcc.gov/May2026); FCC 26-29 NPRM (https://docs.fcc.gov/public/attachments/FCC-26-29A1.pdf); Federal Register FCC 26-2 summary (https://www.federalregister.gov/documents/2026/04/10/2026-06992/).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-87. `48ff1ce4-a365-5a5b-8824-c1cd5d2d4f80`

- Present date: `2026-04-30 12:02:20.705271`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a non-Five Eyes country independently publicly attribute a cyberattack or cyber espionage campaign to a China-nexus threat actor between April 29, 2026, and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between April 29, 2026, 00:00 UTC and June 1, 2026, 23:59 UTC, at least one government or official government cybersecurity agency of a country that is NOT a member of the Five Eyes alliance independently publicly attributes a specific cyberattack or cyber espionage campaign to a China-nexus threat actor. It resolves **No** otherwise.

**Definitions:**

- **Five Eyes alliance**: Australia, Canada, New Zealand, the United Kingdom, and the United States (https://en.wikipedia.org/wiki/Five_Eyes). Any country not on this list qualifies as "non-Five Eyes."

- **China-nexus threat actor**: Any hacking group, entity, or individual that the attributing government identifies as being sponsored by, directed by, or acting on behalf of the Chinese state, Chinese intelligence services (e.g., Ministry of State Security), or the People's Liberation Army. This includes attribution to named groups such as APT41, Volt Typhoon, Salt Typhoon, or similar designations, as well as unnamed actors described as Chinese state-linked. The "nexus" means the actor is assessed to operate under Chinese state direction or sponsorship, not merely that they are geographically located in China. (See https://en.wikipedia.org/wiki/Chinese_espionage_in_the_United_States#Cyber_espionage for context on China-nexus cyber actors.)

- **Publicly attribute**: An official statement, press release, advisory, or report published on an official government website (e.g., a Ministry of Foreign Affairs, Ministry of Defense, or national cybersecurity agency website) that explicitly names China or a China-nexus group as responsible for a specific cyberattack or espionage campaign. Alternatively, a statement by a named government official reported by credible international news outlets (e.g., Reuters https://www.reuters.com, Associated Press https://apnews.com, AFP, BBC) citing the official source. The attribution must name a specific incident or campaign, not merely describe China as a general threat.

- **Independently**: The attribution must be issued by a non-Five Eyes country either on its own or as part of a group that includes at least one non-Five Eyes country acting as a lead or co-lead author—not merely as a signatory to a Five Eyes-led joint advisory. A joint advisory co-led by a non-Five Eyes country (e.g., a German BSI-led advisory) qualifies. A non-Five Eyes country merely signing onto a CISA/NCSC-led advisory does NOT qualify.

**Resolution sources**: Official government cybersecurity agency websites (e.g., Germany's BSI at https://www.bsi.bund.de, Japan's NISC, France's ANSSI at https://www.ssi.gouv.fr), or credible international reporting from Reuters, AP, or the BBC.

**Pre-cutoff background**

The Five Eyes alliance—comprising Australia, Canada, New Zealand, the United Kingdom, and the United States (see https://en.wikipedia.org/wiki/Five_Eyes)—has historically led public attribution of state-sponsored cyber operations to China-nexus threat actors. However, non-Five Eyes countries have increasingly joined these efforts. In August 2025, an international coalition including the Czech Republic, Finland, Germany, Italy, Japan, the Netherlands, Poland, and Spain co-signed a 37-page advisory calling out three Chinese companies for supporting China's intelligence services [International coalition calls out three Chinese companies over ...](https://www.reuters.com/business/media-telecom/international-coalition-calls-out-three-chinese-companies-over-hacking-campaign-2025-08-27/). On April 24, 2026, another joint advisory on "Defending Against China-Nexus Covert Networks of Compromised Devices" was co-authored by agencies from Germany (Federal Office for the Protection of the Constitution, Federal Intelligence Service, and Federal Office for Information Security), Japan (National Cybersecurity Office), the Netherlands, Spain, and Sweden, alongside Five Eyes agencies [Cybersecurity agencies flags use of covert networks by China-linked ...](https://industrialcyber.co/cisa/cybersecurity-agencies-flags-use-of-covert-networks-by-china-linked-actors-for-espionage-offensive-operations/).

While joint advisories with Five Eyes nations are becoming more common, independent attributions by non-Five Eyes countries—where a country issues its own statement without co-signing a Five Eyes-led advisory—remain rarer and more politically significant. The Philippines has publicly stated it faces persistent cyberattacks from China-based hackers. Germany, Japan, and the Netherlands have their own active cyber threat intelligence capabilities and have shown increasing willingness to name China publicly.

This question asks whether any non-Five Eyes country will make such an independent public attribution within the resolution window. The April 24, 2026 joint advisory falls outside the resolution window (before April 29) and would not count regardless since it was a joint Five Eyes-led advisory rather than an independent attribution.

**Exact later resolution packet**

The question asks whether, between April 29, 2026 and June 1, 2026, a non-Five Eyes country (or a non-Five Eyes lead/co-lead) independently publicly attributed a SPECIFIC cyberattack or cyber espionage campaign to a China-nexus threat actor, with evidence from an official government site or Reuters/AP/AFP/BBC.

Searching extensively, I found that the prominent recent independent non-Five Eyes attributions all fall OUTSIDE the resolution window:
- Czech Republic's national attribution of APT31 (linked to China's MSS) to the attack on its Ministry of Foreign Affairs was on 28 May 2025, not 2026 (NÚKIB statement and Reuters dated May 28, 2025). The CSIS "Significant Cyber Incidents" timeline also lists this as May 2025 [0c3c21].
- Singapore's Cyber Security Agency attribution of China-linked UNC3886 against its telecom sector was in February 2026 (CSIS timeline notes "February 2026") [0c3c21] — before the window.
- The Netherlands' attribution of Salt Typhoon/RedMike to China was on 28 August 2025 [101fb5] — before the window.
- The diplomatic Belgium/Hungary UNC6384 PlugX campaign was reported (by Arctic Wolf, a private firm) on October 30, 2025, not an in-window government attribution [89a408].

Within the actual window (Apr 29–Jun 1, 2026), the China-nexus cyber items I located were NOT qualifying independent government attributions of a specific campaign:
- The "Shadow-Earth-053" China-aligned espionage campaign was disclosed by the private firm Trend Micro on May 1, 2026, per The Diplomat (May 9, 2026); no non-Five Eyes government officially attributed this specific campaign within the window [37dd9e, 53f096].
- Philippine military statements in the window (e.g., the cyber command chief, late May 2026) concerned "persistent cyberattacks from China" and escalating threats in general terms, which the checklist explicitly excludes as "general warnings about Chinese threat capabilities" rather than attribution of a specific incident.
- The April 24, 2026 multi-country advisory ("Defending Against China-Nexus Covert Networks") is explicitly excluded by the question (before April 29 and Five Eyes-led).

The CSIS "Significant Cyber Incidents" tracker (current through June 2, 2026) contained no May/June 2026 entry of a non-Five Eyes country independently attributing a specific cyberattack to China [0c3c21]. No qualifying official government statement or Reuters/AP/AFP/BBC report of an in-window independent (or non-Five-Eyes-led) attribution of a specific China-nexus campaign was found. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-88. `b37ed4ff-8c07-5ba3-a337-fb226eda2710`

- Present date: `2026-05-03 01:06:24.467305`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Caspian Pipeline Consortium (CPC) experience an unscheduled shutdown of 48+ hours due to a security incident between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if all of the following conditions are met:

1. **Unscheduled shutdown**: The CPC pipeline system or its marine terminal at Novorossiysk experiences a cessation or substantial reduction (below 25% of normal throughput) of oil export operations that was not pre-announced as planned maintenance. This includes both pipeline throughput stoppages and terminal loading halts.

2. **Duration of 48+ hours**: The shutdown lasts at least 48 consecutive hours, measured from the time the stoppage or substantial reduction is first reported by a credible source (Reuters, Bloomberg, AP, or official CPC statements) to the time resumption of operations is officially announced or confirmed by a credible source. All times are measured in UTC.

3. **Security incident**: The shutdown is primarily caused by a security incident, defined as a deliberate hostile act including but not limited to: drone strikes, missile attacks, naval drone attacks, sabotage, or armed assault on CPC infrastructure. This excludes technical failures, weather-related disruptions (e.g., storms), scheduled maintenance, regulatory actions, or sanctions-related stoppages.

4. **Timing**: The shutdown must commence (or be ongoing) at any point between May 1, 2026, 00:00 UTC and June 1, 2026, 23:59 UTC.

**Resolution source**: Official CPC consortium statements (https://www.cpc.ru/EN/press/Pages/default.aspx) or major international news wires such as Reuters (https://www.reuters.com/business/energy/), Bloomberg, or Associated Press. At least one credible source must attribute the shutdown to a security incident.

If no qualifying shutdown occurs during this period, the question resolves **No**.

**Pre-cutoff background**

The Caspian Pipeline Consortium (CPC) operates a 1,511 km pipeline transporting approximately 80% of Kazakhstan's crude oil exports from western Kazakhstan to the Black Sea terminal near Novorossiysk, Russia. The pipeline handles roughly 1% of global oil supply [Ukrainian attacks on the CPC oil pipeline](https://www.osw.waw.pl/en/publikacje/analyses/2026-02-04/ukrainian-attacks-cpc-oil-pipeline-outlook-kazakhstans-oil-sector).

Since late 2025, CPC infrastructure has been repeatedly targeted by Ukrainian drone attacks:
- On November 29, 2025, Ukrainian drones struck the CPC oil terminal near Novorossiysk, halting exports and causing heavy equipment damage [Kazakhstan says CPC oil exports via Black Sea stable after ...](https://www.reuters.com/business/energy/kazakhstan-says-cpc-oil-exports-via-black-sea-stable-after-russia-reports-an-2026-04-07/).
- On January 13 and 19, 2026, further attacks targeted tankers in the Black Sea operated by Kazakhstan's KazMunayGas [Ukrainian attacks on the CPC oil pipeline](https://www.osw.waw.pl/en/publikacje/analyses/2026-02-04/ukrainian-attacks-cpc-oil-pipeline-outlook-kazakhstans-oil-sector).
- On April 6, 2026, Russia's Defence Ministry reported another Ukrainian drone attack on CPC maritime facilities at Novorossiysk, damaging a mooring point. However, Kazakhstan's deputy energy minister stated that CPC exports remained stable, and Chevron's Tengizchevroil confirmed uninterrupted exports from the Tengiz field [Kazakhstan says CPC oil exports via Black Sea stable after ...](https://www.reuters.com/business/energy/kazakhstan-says-cpc-oil-exports-via-black-sea-stable-after-russia-reports-an-2026-04-07/).

The CPC also completed a planned 72-hour maintenance shutdown on April 10, 2026, after which operations returned to normal.

As of early May 2026, the CPC pipeline is operational with exports reported as stable following the April 7 attack [Kazakhstan says CPC oil exports via Black Sea stable after ...](https://www.reuters.com/business/energy/kazakhstan-says-cpc-oil-exports-via-black-sea-stable-after-russia-reports-an-2026-04-07/). However, the ongoing Ukraine-Russia conflict creates persistent risk of further drone strikes on CPC terminal infrastructure at Novorossiysk. Kazakhstan has been exploring alternative export routes but these lack the capacity to replace CPC [Ukrainian attacks on the CPC oil pipeline](https://www.osw.waw.pl/en/publikacje/analyses/2026-02-04/ukrainian-attacks-cpc-oil-pipeline-outlook-kazakhstans-oil-sector).

**Exact later resolution packet**

The question resolves NO. It requires a CPC (Caspian Pipeline Consortium) pipeline/marine-terminal unscheduled shutdown of 48+ consecutive hours (throughput below 25% of normal) caused primarily by a security incident, commencing or ongoing between May 1, 2026 00:00 UTC and June 1, 2026 23:59 UTC.

Findings:
- The principal security event during the window was a large Ukrainian drone strike on Novorossiysk over the weekend of May 22-24, 2026. However, that attack hit the Sheskharis oil terminal (a Transneft facility), not the CPC terminal. The Reuters report (May 22, updated May 23) said falling drone debris triggered a fire at "an oil terminal" and did not identify the CPC terminal or report any CPC export suspension [bf3eba, abfbd0]. The AP/Fortune account (May 23) likewise identifies the Sheskharis/Transneft terminal as the target and reports no CPC shutdown [fdd7f3].
- Bloomberg (May 26, 2026) reported that following the weekend attack, all three crude berths of the Sheskharis terminal were operational with tankers loading per satellite imagery — i.e., no 48-hour cessation, and no CPC shutdown [08928a].
- Quantum Commodity Intelligence (May 26, 2026) reported CPC shipped 25.95 million mt of crude from its Black Sea terminal from Jan 1 to May 24, 2026, with ongoing loadings and no reported 48+ hour security-caused CPC shutdown in May 2026 [49a62f, 112f18].
- Earlier 2026 CPC/Novorossiysk disruptions (the Nov 29, 2025 SPM attack, the April 6-10, 2026 Sheskharis attack, the planned 72-hour maintenance ending April 10) all fall outside the May 1 - June 1, 2026 window [004baf, 56bd00, bae844].

No credible allowed source (CPC statements, Reuters, Bloomberg, AP) reported a 48+ hour CPC shutdown attributable to a security incident within the resolution window. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-89. `78050dfe-7991-5192-b1f3-8404b08c9253`

- Present date: `2026-05-02 10:11:18.999892`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will there be a confirmed attack on a commercial vessel in the Red Sea or Gulf of Aden between May 1 and June 1, 2026 (UTC)?

**Resolution criteria**

This question resolves **Yes** if at least one incident classified as an "Attack" on a commercial vessel in the Red Sea or Gulf of Aden is reported between 00:00 UTC on May 1, 2026, and 23:59 UTC on June 1, 2026. It resolves **No** otherwise.

**Definitions:**

- **"Attack"**: Any hostile act directed at a vessel, including but not limited to missile strikes, drone strikes, armed boarding attempts, or gunfire, as classified by UKMTO or equivalent authority. Incidents classified only as "Suspicious Activity" or "Warning" do not count. See UKMTO incident classifications: https://www.ukmto.org/recent-incidents

- **"Commercial vessel"**: Any non-military, non-governmental merchant ship engaged in trade or transport. This includes cargo ships, tankers, container ships, and bulk carriers. Military vessels, coast guard vessels, and government-owned ships operating in a sovereign capacity are excluded. See IMO definition: https://www.imo.org/

- **"Red Sea"**: The body of water bounded by the Suez Canal (approximately 30°N) to the north and the Bab el-Mandeb strait (approximately 12.5°N, 43.3°E) to the south, between the African and Arabian coasts. See: https://en.wikipedia.org/wiki/Red_Sea

- **"Gulf of Aden"**: The body of water extending from the Bab el-Mandeb strait eastward to approximately 51°E longitude, bounded by Yemen to the north and Somalia/Djibouti to the south. See: https://en.wikipedia.org/wiki/Gulf_of_Aden

**Resolution source:** The primary resolution source is the UKMTO Recent Incidents page (https://www.ukmto.org/recent-incidents). If UKMTO is unavailable, resolution may rely on US MARAD advisories (https://www.maritime.dot.gov/msci-advisories) or credible international news reporting (e.g., Reuters, AP News) confirming an attack on a commercial vessel in the specified region and timeframe.

The attack must occur **on or after 00:00 UTC May 1, 2026, and on or before 23:59 UTC June 1, 2026**. Incidents prior to this window do not count.

**Pre-cutoff background**

From November 2023 to October 2025, Houthi forces conducted more than 100 attacks on commercial vessels in the Red Sea and Gulf of Aden, affecting over 60 nations. Following the October 2025 Gaza peace plan, the Houthis suspended attacks on commercial shipping [2026 Houthi strikes on Israel - Wikipedia](https://en.wikipedia.org/wiki/2026_Houthi_strikes_on_Israel). A ceasefire related to the 2026 Iran war further paused Houthi military operations [2026 Houthi strikes on Israel - Wikipedia](https://en.wikipedia.org/wiki/2026_Houthi_strikes_on_Israel). However, the Houthis have repeatedly threatened to resume attacks or close the Bab el-Mandeb strait if regional tensions escalate or Gulf states join conflicts against Iran [2026 Houthi strikes on Israel - Wikipedia](https://en.wikipedia.org/wiki/2026_Houthi_strikes_on_Israel). In March 2026, Houthis launched missiles at Israel, raising fears of renewed Red Sea shipping strikes. The US MARAD advisory 2026-006 continues to warn of ongoing threats in the region.

As of May 1, 2026, the UKMTO Recent Incidents page shows no "Attack"-classified incidents in the Red Sea or Gulf of Aden in recent weeks; incidents in that area have been limited to "Suspicious Activity" reports (e.g., May 1, 2026 near Al Mukalla; April 12, 2026 near Al Hudaydah) [Recent Incidents - UKMTO](https://www.ukmto.org/recent-incidents). Recent "Attack"-classified incidents have been concentrated in the Strait of Hormuz and Arabian Gulf rather than the Red Sea [Recent Incidents - UKMTO](https://www.ukmto.org/recent-incidents).

The situation remains genuinely uncertain: a ceasefire is in place but fragile, Houthi rhetoric has been escalatory, and regional dynamics (US-Iran-Israel tensions, Gulf state involvement) could trigger a resumption of shipping attacks at any time.

**Exact later resolution packet**

The question resolves NO. It requires at least one incident classified as an "Attack" on a commercial vessel in the Red Sea (south of 30°N) or Gulf of Aden (west of 51°E) between 00:00 UTC May 1, 2026 and 23:59 UTC June 1, 2026, per the primary resolution source, the UKMTO Recent Incidents page.

Evidence:
- An exhaustive review of the UKMTO Recent Incidents page (the primary resolution source) covering Feb 28 – Jun 2, 2026 shows that during the May 1 – June 1, 2026 window, all incidents reported in the Red Sea or Gulf of Aden were classified as "Suspicious Activity" or "Advisory" — never "Attack." Specifically: May 1 (UKMTO #48, Suspicious Activity SW of Al Mukalla), May 2 (#49, Suspicious Activity SW of Al Mukalla), May 22 (#59, Suspicious Activity N of Socotra), May 23 (#60/#61, Suspicious Activity W of Socotra). All "Attack"-classified incidents during this period (e.g., UKMTO #50, #52, #55, #56, #62, #63) occurred in the Arabian Gulf, Strait of Hormuz, or Gulf of Oman — outside the defined geographic scope [1a31d3].
- The May 5, 2026 UKMTO Warning 55-2026 "Attack" was within the Strait of Hormuz, and the May 10 warning 056-26 "Attack" was 23NM northeast of Doha, Qatar (Arabian Gulf) — both outside the Red Sea/Gulf of Aden scope. A widely shared "10 May 2026" social-media claim of a commercial cargo vessel attack referred to an incident "northeast of Mesaieed Port" in Qatar (Arabian Gulf), not the Red Sea or Gulf of Aden.
- The US MARAD advisory 2026-006 states the Houthis have not attacked commercial ships since the October 2025 Israel-Gaza ceasefire; the most recent listed attack was the Sept 29, 2025 strike on the Dutch-flagged Minervagracht in the Gulf of Aden [c49d42]. The AP report on that Minervagracht attack also confirms it occurred Sept 29, 2025 — well before the window [a5a3cd].
- The Wikipedia "Red Sea crisis" article, updated through June 1, 2026, indicates the Houthis remained "generally passive" toward commercial shipping in this period, with 2026 activity focused on strikes against Israel (e.g., March 28, 2026 missile) rather than Red Sea/Gulf of Aden merchant shipping [cb5c80].

All credible sources consistently confirm there was no "Attack"-classified incident on a commercial vessel within the Red Sea or Gulf of Aden during the specified window, so the question resolves NO.

Sources: https://www.ukmto.org/recent-incidents ; https://www.maritime.dot.gov/msci/2026-006-red-sea-bab-el-mandeb-strait-gulf-aden-arabian-sea-and-somali-basin-houthi-attacks ; https://en.wikipedia.org/wiki/Red_Sea_crisis

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-90. `5cdc8c75-bf10-53ff-96fc-f49682d368ba`

- Present date: `2026-05-15 16:41:35.546452`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Senegalese National Assembly pass legislation to repeal or amend the March 2024 amnesty law between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves YES if, between May 12, 2026 (00:00 UTC) and June 30, 2026 (23:59 UTC), the Senegalese National Assembly passes (by final vote in plenary session) any new legislation — including ordinary laws, organic laws, or constitutional amendment bills — that explicitly repeals, restricts, or amends the March 2024 amnesty law (Law No. 2024-09). "Passing" means formal adoption by a majority vote in the National Assembly; presidential promulgation is not required for resolution. For constitutional amendments, passage by the National Assembly (whether by referendum route or congressional vote) satisfies this criterion. The term "legislation" includes both ordinary bills and constitutional amendment bills.

This question resolves NO if no such legislation is passed by the National Assembly before July 1, 2026 (00:00 UTC).

Resolution will be determined by official records from the Senegalese National Assembly (https://www.assemblee-nationale.sn/) or the Journal Officiel de la République du Sénégal, or by credible reporting from at least one of the following sources: Agence de Presse Sénégalaise (APS), Reuters, Agence France-Presse (AFP), Associated Press (AP), or Le Monde.

**Pre-cutoff background**

In March 2024, Senegal's parliament enacted Law No. 2024-09, an amnesty law covering criminal acts related to political protests and violence between February 2021 and February 2024, a period during which at least 65 people died in anti-government demonstrations [Senegal top court rejects bid to lift amnesty for protest deaths | Reuters](https://www.reuters.com/world/africa/senegal-top-court-rejects-bid-lift-amnesty-protest-deaths-2025-04-24/).

The current government under President Bassirou Diomaye Faye and Prime Minister Ousmane Sonko has sought to narrow or repeal this amnesty. On April 2, 2025, the National Assembly passed Law No. 08/2025, an "interpretive" law that attempted to exclude certain crimes (murder, torture, forced disappearance) from the amnesty's scope [Senegal top court rejects bid to lift amnesty for protest deaths | Reuters](https://www.reuters.com/world/africa/senegal-top-court-rejects-bid-lift-amnesty-protest-deaths-2025-04-24/). However, on April 24, 2025, Senegal's Constitutional Council struck down Law No. 08/2025, ruling it violated the constitutional principle of non-retroactivity of more severe criminal laws (Article 9 of the Constitution) and contravened international human rights obligations [https://apanews.net/senegals-constitutional-court-strikes-down-interpretive-law-on-amnesty/](https://apanews.net/senegals-constitutional-court-strikes-down-interpretive-law-on-amnesty/)[Senegal top court rejects bid to lift amnesty for protest deaths | Reuters](https://www.reuters.com/world/africa/senegal-top-court-rejects-bid-lift-amnesty-protest-deaths-2025-04-24/).

As of May 12, 2026, PM Sonko announced the government's intention to submit new legislation to repeal the amnesty law [https://www.newvision.co.ug/category/politics/senegal-pm-seeks-to-repeal-contested-amnesty-law-NV_202114_052026](https://www.newvision.co.ug/category/politics/senegal-pm-seeks-to-repeal-contested-amnesty-law-NV_202114_052026). The government controls the National Assembly and has strong political motivation, but the Constitutional Council's ruling creates significant legal constraints on any new attempt. The government's options include a full repeal bill (as opposed to the previous "interpretive" approach) or a constitutional amendment. No vote has yet taken place on new legislation as of May 12, 2026 [https://www.newvision.co.ug/category/politics/senegal-pm-seeks-to-repeal-contested-amnesty-law-NV_202114_052026](https://www.newvision.co.ug/category/politics/senegal-pm-seeks-to-repeal-contested-amnesty-law-NV_202114_052026).

**Exact later resolution packet**

RESOLUTION: NO (0).

The question asked whether, between May 12, 2026 (00:00 UTC) and June 30, 2026 (23:59 UTC), the Senegalese National Assembly passed (by final vote in plenary) any new legislation explicitly repealing, restricting, or amending the March 2024 amnesty law (Law No. 2024-09).

I identified the two significant legislative acts of the National Assembly within the window, and neither touches the amnesty law:

1) The single major plenary vote in this window was the CONSTITUTIONAL REFORM of Monday, June 29, 2026 (proposition de loi n°17/2026). This reform is about institutional restructuring, NOT the amnesty law. Reuters reports that the reform debated and voted on June 29 concerns prohibiting a sitting president from leading a political party, and that "any amendment must first be put to a referendum" per Justice Minister Moussa Sarr — with no mention of the amnesty law [1f9ebc] (https://www.reuters.com/world/africa/senegal-police-fire-tear-gas-constitutional-reform-protesters-2026-06-29/). RFI's detailed account of the ~29 modified articles (president barred from leading a party, strengthened Assembly/PM powers, Constitutional Council replaced by a Constitutional Court, limits on dissolution power) contains no provision on the amnesty law [94fb84] (https://www.rfi.fr/fr/afrique/20260629-sénégal-l-assemblée-nationale-vote-une-réforme-de-la-constitution-le-gouvernement-annonce-un-référendum). Vie-publique.sn's dossier on loi n°17/2026 (declared admissible June 12, 2026; adopted in plenary June 29, 2026) likewise makes no mention of Law No. 2024-09 [982f2c] (https://www.vie-publique.sn/dossiers/revision-constitution-senegal-2026). ConstitutionNet's coverage of the June 29 vote confirms the reform is about "curbing presidential powers" and lists its contents, none of which concern the amnesty [fe2a8b].

2) ConstitutionNet's in-depth analysis of the entire 2026 reform package (constitutional revision + organic law on the Constitutional Court + new Electoral Code + political-parties law) confirms none of these texts repeals, restricts, or amends the March 2024 amnesty law or addresses the Article 9 non-retroactivity principle that the Constitutional Council invoked in April 2025 [a4929c].

A separate law published May 15, 2026 concerned revoking/registering electoral rights — unrelated to the amnesty (Library of Congress Global Legal Monitor; not accessible directly but consistently described in search results).

I also checked the Reuters report on the National Assembly around this period (Sonko elected Speaker on May 26, 2026); it records the power struggle but reports NO passage of any amnesty repeal/amendment legislation in the window [ef4ebb] (https://www.reuters.com/world/africa/senegal-parliament-elects-ousted-prime-minister-sonko-speaker-2026-05-26/).

Note on a potential loophole: Some social-media posts (CGTN Africa, QTV) around June 29 mixed background about the "repeal of the March 2024 amnesty law" into coverage of the constitutional-reform vote. However, authoritative sources (Reuters, RFI, vie-publique.sn) uniformly establish that the June 29 vote was the constitutional reform on presidential powers/institutions, not the amnesty law. The description itself notes that as of May 12, 2026 the government had only ANNOUNCED an intention to submit a new repeal bill and no vote had occurred; I found no report of any such amnesty-specific bill being adopted in plenary before July 1, 2026.

Therefore no qualifying legislation was passed in the window, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-91. `bc47e02a-e496-5031-9149-0baf0084a2db`

- Present date: `2026-04-30 13:33:10.492343`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will China's PLA announce a formally named military exercise in the South China Sea between April 29 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between April 29, 2026, 00:00 Beijing Time (UTC+8) and June 1, 2026, 23:59 Beijing Time (UTC+8), the PLA or an official Chinese government source announces a military exercise in the South China Sea that is given a specific, formal name (i.e., a proper title such as "Joint Sword-2026B" or "Exercise [Name]").

**Definition of "named military exercise":** A military drill or operation explicitly identified by a unique proper name or title in an official announcement. General descriptions such as "routine training," "combat readiness patrol," "live-fire drills," or "naval maneuvers" do NOT qualify unless they are also given a distinct formal name. The name must appear in an official PLA statement, the Chinese Ministry of National Defense website (http://www.mod.gov.cn), or major Chinese state media (Xinhua at http://www.news.cn, PLA Daily at http://www.81.cn, or Global Times at http://www.globaltimes.cn).

**Definition of "South China Sea":** The semi-enclosed sea bounded approximately by the coordinates used in the UN Convention on the Law of the Sea arbitration (PCA Case No. 2013-19): north of the Equator, south of approximately 23°N latitude, east of Vietnam and west of the Philippines, as depicted in the Wikipedia article on the South China Sea (https://en.wikipedia.org/wiki/South_China_Sea). Waters east of Luzon (Philippine Sea / Western Pacific) do NOT count. The exercise must take place within, or be officially described as occurring in, the South China Sea (南海).

**Resolution sources:** The question will be resolved by checking the Chinese Ministry of National Defense website (http://www.mod.gov.cn), Xinhua (http://www.news.cn), PLA Daily (http://www.81.cn), and credible English-language reporting from Reuters, AP, or the South China Morning Post. If no formally named exercise is identified in these sources by June 1, 2026, 23:59 Beijing Time, the question resolves **No**.

The exercise must be announced or take place on or after April 29, 2026, 00:00 Beijing Time to qualify. Exercises announced or commenced before this date are excluded.

**Pre-cutoff background**

As of late April 2026, tensions in the South China Sea are elevated. The U.S. and the Philippines launched "Balikatan 2026" on April 20, 2026 — the largest iteration of the annual exercise to date, involving over 17,000 troops from seven nations including Japan, Australia, Canada, France, and New Zealand. The exercises run for 19 days and include live-fire drills, a ship-sinking exercise off Ilocos Norte, and counter-landing operations near regional flashpoints [China stages navy drill as US and Philippines embark on Balikatan ...](https://www.scmp.com/news/china/military/article/3351353/china-stages-navy-drill-us-and-philippines-embark-balikatan-2026).

In response, China has deployed significant naval assets to the region. The PLA Southern Theatre Command announced on April 24, 2026 that a naval fleet had "recently" conducted drills — including live-fire exercises and air-sea coordination — in waters east of Luzon [China stages navy drill as US and Philippines embark on Balikatan ...](https://www.scmp.com/news/china/military/article/3351353/china-stages-navy-drill-us-and-philippines-embark-balikatan-2026). The aircraft carrier Liaoning and the 133rd naval task group transited through the Taiwan Strait and into the Western Pacific, though the PLA Eastern Theater Command described these as "routine training activities organized in accordance with the annual plan" rather than assigning them a formal exercise name [China's Liaoning Carrier Heads South: More Than a Routine Drill](https://thediplomat.com/2026/04/chinas-liaoning-carrier-heads-south-more-than-a-routine-drill/).

China has a history of launching formally named exercises in response to perceived provocations — most notably the "Joint Sword" series of exercises around Taiwan in 2024. However, PLA activity in the South China Sea is more frequently described in generic terms ("combat readiness patrols," "routine training") without a formal name. Whether the current Balikatan-driven escalation prompts a formally named exercise remains uncertain.

**Exact later resolution packet**

The question resolves NO. It asked whether, between April 29 and June 1, 2026 (Beijing Time), the PLA or an official Chinese source would announce a military exercise in the South China Sea given a specific, formal proper name (e.g., "Joint Sword-2026B").

Evidence gathered:

1) The ISW "China & Taiwan Update, May 1, 2026" reported that the PLA Southern Theatre Command (STC) announced on April 28, 2026 that it had conducted exercises in the South China Sea in response to Philippine actions, but these were described in generic terms (routine patrols/combat readiness patrols/live-fire drills) and were NOT assigned any specific formal name. The same update contrasts this with the formally named US-Philippine "Balikatan 2026" [China & Taiwan Update, May 1, 2026 | ISW](https://understandingwar.org/research/china-taiwan/china-taiwan-update-may-1-2026/).

2) The April STC activity that was given prominence ("107编队"/Naval Task Group 107 conducting live-fire, air-sea coordination) occurred "east of Luzon" (吕宋岛以东海域) — the Philippine Sea/Western Pacific — which is explicitly EXCLUDED by the resolution criteria, and in any case was unnamed and partly announced before April 29.

3) China's actual South China Sea responses during the window were described as routine cruises (例行巡航) and "combat readiness patrols" (战备警巡) near Huangyan Dao (Scarborough Shoal), again without any formal exercise name.

4) The Chinese Ministry of National Defense's own regular press conference transcript of May 28, 2026 (mod.gov.cn) contains no announcement of any formally named exercise in the South China Sea during the period. The spokesman described the Liaoning carrier group's activity as "routine training" (例行性训练) and only referenced pre-existing named foreign-cooperation series (e.g., with Pakistan), none of which is a new named South China Sea exercise within the window [2026年5月国防部例行记者会文字实录](http://www.mod.gov.cn/gfbw/qwfb/16464102.html).

China's notable formally named exercises in this era ("联合利剑/Joint Sword" series, e.g. Joint Sword-2024A/B/C, and the December 2025 "正义使命-2025/Strait Thunder") were conducted by the Eastern Theater Command around Taiwan/East China Sea, not the Southern Theater Command in the South China Sea, and not within this window.

Therefore, no formally named PLA military exercise located in the South China Sea was announced between April 29 and June 1, 2026, and the question resolves NO.

Key sources:
- ISW China-Taiwan Update May 1, 2026: https://understandingwar.org/research/china-taiwan/china-taiwan-update-may-1-2026/
- China MND press conference transcript May 28, 2026: http://www.mod.gov.cn/gfbw/qwfb/16464102.html
- China News / STC routine cruise April 28, 2026: https://www.chinanews.com.cn/gn/2026/04-28/10612600.shtml

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-92. `b7d5e885-04c6-543a-ab87-65ab3ae7885e`

- Present date: `2026-05-29 00:13:43.808754`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Israeli Knesset pass the Communications Bill (Broadcasts), 2025 (Karhi media bill) in its second and third readings by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the "Communications Bill (Broadcasts), 2025" (Hebrew: הצעת חוק התקשורת (שידורים), התשפ"ה-2025) — also known as the Karhi media bill or broadcast media overhaul bill — passes its third and final reading (קריאה שלישית) in the Knesset plenum on or after May 12, 2026, and no later than July 1, 2026, 23:59 IDT (UTC+3).

The question resolves as **No** if:
- The bill does not reach a third reading vote by July 1, 2026, 23:59 IDT;
- The bill is voted down in its second or third reading;
- The bill is withdrawn or merged into substantially different legislation.

**Resolution source:** Official Knesset legislative records at https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/LawBill.aspx or the Knesset English-language site at https://m.knesset.gov.il/EN/activity/Pages/Legislation.aspx. The Israeli Official Gazette (Reshumot) at https://www.nevo.co.il/law/ may also serve as confirmation. Credible English-language reporting (e.g., Times of Israel, Reuters, Haaretz) may supplement but not replace official records.

**Pre-cutoff background**

Communications Minister Shlomo Karhi has been advancing a major overhaul of Israel's broadcast media regulation, formally titled the "Communications Bill (Broadcasts), 2025." The bill proposes establishing a new Broadcast Media Authority and a Council for the Regulation of Audio-Visual Content, replacing the existing Second Authority for Television and Radio and the Cable and Satellite Broadcasting Council. It would grant the government significant control over broadcast media, including authority to issue fines and regulate news sites [Likud minister's contentious media regulation bill passes first ...](https://www.timesofisrael.com/likud-ministers-contentious-media-regulation-bill-passes-first-reading-in-knesset/).

The bill passed its first reading in the Knesset plenum on November 4, 2025 [Likud minister's contentious media regulation bill passes first ...](https://www.timesofisrael.com/likud-ministers-contentious-media-regulation-bill-passes-first-reading-in-knesset/). It requires second and third readings to become law. After internal coalition disputes — notably between Minister Karhi and Economy Committee Chairman MK David Bitan, who blocked progress — the government established a special "Committee for Deliberating the Communications Bill (Broadcasts), 2025," chaired by MK Galit Distel Atbaryan, to bypass the Economy Committee [Special Knesset Committee To Push Broadcasting Bill Forward as ...](https://themedialine.org/headlines/special-knesset-committee-to-push-broadcasting-bill-forward-as-rift-widens/).

As of late April 2026, the special committee is actively debating specific sections of the bill (including provisions on community content and viewing data transparency) in preparation for second and third readings [Communications Minister MK Karhi: There won't be intervention of ...](https://m.knesset.gov.il/EN/News/PressReleases/Pages/press29426q.aspx).

Key obstacles include: (1) internal coalition disagreements; (2) opposition from the Knesset Legal Advisor, who criticized the process of forming the special committee; (3) the Attorney General's office, which has warned the bill poses "real concern of severe harm to freedom of expression and freedom of the press" [Likud minister's contentious media regulation bill passes first ...](https://www.timesofisrael.com/likud-ministers-contentious-media-regulation-bill-passes-first-reading-in-knesset/); and (4) anticipated High Court challenges even if the bill passes [Special Knesset Committee To Push Broadcasting Bill Forward as ...](https://themedialine.org/headlines/special-knesset-committee-to-push-broadcasting-bill-forward-as-rift-widens/). These factors create genuine uncertainty about whether the bill will clear second and third readings by July 1, 2026.

**Exact later resolution packet**

The question resolves NO. The "Communications Bill (Broadcasts), 2025" (the Karhi media/broadcasting reform bill) did NOT pass its third and final reading (קריאה שלישית) in the Knesset plenum by July 1, 2026, 23:59 IDT.

Key evidence:

1. Official Knesset National Legislation Database record for the bill (הצעת חוק התקשורת (שידורים), התשפ"ו-2025; Knesset bill entry 1042100, government bill מ/1898) shows the bill's status as "הכנה לקריאה שנייה ושלישית" (Preparation for second and third reading) — i.e., it never reached, let alone passed, a third-reading vote. The record, last updated on/around July 1, 2026, further notes the bill was split on 02.06.2026, with committee deliberations continuing through late June 2026 without a final plenum vote [הצעת חוק התקשורת (שידורים), התשפ"ו-2025 במאגר החקיקה הלאומי](https://main.knesset.gov.il/apps/legislation/main/bills/1042100).

2. Note on the bill's Hebrew year: the question cites "התשפ"ה-2025," which was the title of the draft memorandum (draft law) published in mid-2025 (Jewish year 5785). By the time it became a government bill introduced to the Knesset (passing first reading on Nov 4, 2025), it carried the title "התשפ"ו-2025" (5786). These are the same Karhi broadcasting bill referenced in the question; the Knesset database uses the התשפ"ו form.

3. On June 2, 2026, the Knesset plenum voted 52-43 to SPLIT the bill (פיצול) so that a portion could be advanced before the Knesset dissolved. Globes explicitly reported this split approval did NOT mean the bill itself passed; the split parts still had to return to the special committee to process hundreds of opposition reservations before going to the plenum for second and third readings — a "long and complex" process still at the committee stage as of early June 2026 [מליאת הכנסת אישרה את פיצול רפורמת השידורים. מה השלב הבא? - גלובס](https://www.globes.co.il/news/article.aspx?did=1001544813).

4. The Knesset was in the process of dissolving toward early elections. A dissolution bill passed its first reading 106-0, with an election window set for Sept 8–Oct 20, 2026. A Haaretz article dated June 28, 2026 reported the coalition in its final weeks focusing its "last-ditch" legislative push on judicial-overhaul and pro-Haredi (IDF exemption) bills, not on completing the broadcasting bill [Netanyahu Coalition Makes Last-ditch Push for pro-Haredi ...](https://www.haaretz.com/israel-news/elections/2026-06-28/ty-article/.premium/netanyahu-coalition-focuses-on-judicial-overhaul-pro-ultra-orthodox-bills/0000019f-0ce1-dfe2-a79f-6df946160000).

Under the resolution criteria, NO is required if "the bill does not reach a third reading vote by July 1, 2026." All official and credible sources confirm the bill remained in the "preparation for second and third reading" stage and never reached a third-reading vote by the deadline. (Additionally, the June 2 split further supports NO, as the original bill was restructured rather than passed intact.) Therefore the resolution is NO (0).

Primary resolution source URL: https://main.knesset.gov.il/apps/legislation/main/bills/1042100 (official Knesset legislative record showing status "הכנה לקריאה שנייה ושלישית" and the 02.06.2026 split). Supplementary: Globes https://www.globes.co.il/news/article.aspx?did=1001544813 and Haaretz https://www.haaretz.com/israel-news/elections/2026-06-28/ty-article/.premium/netanyahu-coalition-focuses-on-judicial-overhaul-pro-ultra-orthodox-bills/0000019f-0ce1-dfe2-a79f-6df946160000.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-93. `b5bbd8cf-fce9-5d15-8c2d-b62df1e9f7f1`

- Present date: `2026-05-16 22:40:37.165217`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Julio Velarde publicly announce his departure or non-renewal as BCRP President between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026, and before July 1, 2026, 23:59 UTC, Julio Velarde publicly announces his departure from or non-renewal as President of the BCRP. It also resolves **Yes** if the President of Peru officially announces the appointment of a successor to Velarde, or if an official government publication confirms the non-renewal of Velarde's mandate, during the same period.

"Departure or non-renewal" includes any of the following:
- Velarde publicly states he will not continue as BCRP President (resignation, retirement, or declining reappointment).
- The President of Peru announces a new BCRP President to replace Velarde.
- An official publication in the government gazette *El Peruano* (https://elperuano.pe/) confirms the end of Velarde's mandate without reappointment.

A "public announcement" means an official BCRP press release (https://www.bcrp.gob.pe/en/news.html), a publication in *El Peruano*, or verified reporting by at least one major credible news outlet such as Reuters (https://www.reuters.com/), Bloomberg (https://www.bloomberg.com/), El Comercio (https://elcomercio.pe/), or Infobae Peru (https://www.infobae.com/peru/).

This question resolves **No** if no such announcement is made on or after May 12, 2026 and before July 1, 2026, 23:59 UTC. It also resolves **No** if Velarde explicitly confirms his continuation in the role without any countervailing departure announcement during this period.

**Pre-cutoff background**

Julio Velarde has served as President of the Banco Central de Reserva del Perú (BCRP) since October 2006, making him one of the longest-serving central bank heads in Latin America [Julio Velarde continuará como presidente del BCRP hasta 2026 ...](https://www.infobae.com/peru/2025/07/23/periodo-de-julio-velarde-como-presidente-del-bcrp-termina-en-2026-pero-podria-ser-ratificado/). He was most recently ratified in October 2021 for a term extending until 2026 [Julio Velarde continuará como presidente del BCRP hasta 2026 ...](https://www.infobae.com/peru/2025/07/23/periodo-de-julio-velarde-como-presidente-del-bcrp-termina-en-2026-pero-podria-ser-ratificado/). The BCRP President is designated by the Executive branch and ratified by the Congressional Permanent Commission.

As of May 12, 2026, Velarde's current mandate is set to expire sometime in 2026, though the precise end date is not publicly specified beyond the year [Julio Velarde continuará como presidente del BCRP hasta 2026 ...](https://www.infobae.com/peru/2025/07/23/periodo-de-julio-velarde-como-presidente-del-bcrp-termina-en-2026-pero-podria-ser-ratificado/). In early May 2026, Velarde declined to confirm his continuity in the role during a public ceremony, and a decision regarding his mandate continuity is expected around June 2026 [https://www.riotimesonline.com/peru-ipc-april-velarde-fiscal-hemorrhage-may-2026/](https://www.riotimesonline.com/peru-ipc-april-velarde-fiscal-hemorrhage-may-2026/). President Balcázar honored Velarde with the Order of the Sun of Peru in March 2026, which some observers interpreted as a possible farewell gesture. Velarde's potential departure would be a major institutional event with significant implications for Peru's monetary policy credibility and economic stability.

**Exact later resolution packet**

RESOLUTION: NO (0)

The question resolves YES only if, between May 12, 2026 and July 1, 2026 (23:59 UTC), one of these occurred: (a) Velarde publicly announced his departure/non-renewal as BCRP President; (b) the President of Peru officially announced a successor to Velarde; or (c) an official El Peruano publication confirmed the non-renewal of his mandate. None of these occurred during the window.

KEY EVIDENCE (from mandated sources):

1) At the presentation of the June 2026 Inflation Report (June 19, 2026), Julio Velarde did NOT announce his departure. To the contrary, he left the door open to continuing, stating: "Antes me inclinaba más a dejar el cargo... Pero si me lo ofrecen, debería pensarlo, no voy a decir que no ahora ni que sí, debería pensarlo, vamos a ver." He explicitly noted that whereas a couple of months earlier he leaned toward leaving, he was now willing to consider staying, and that "nobody has communicated with me" and his term ends July 28, 2026. This is a non-committal statement leaning toward possible continuity, not a departure announcement (Infobae, June 20, 2026) [Julio Velarde se pronuncia ante posibilidad de continuar en el ...](https://www.infobae.com/peru/2026/06/20/julio-velarde-se-pronuncia-ante-posibilidad-de-continuar-en-el-banco-central-de-reserva-del-peru-bcrp/).

2) As of late June 2026, still no departure announcement and no appointed successor. Instead, incoming president-elect Keiko Fujimori publicly stated she would seek to meet Velarde to REQUEST that he CONTINUE ("lo primero que voy a hacer es solicitar una audiencia con Julio Velarde"). This is the opposite of a departure/non-renewal announcement (Infobae, June 22, 2026) [Keiko Fujimori se reunirá con Julio Velarde apenas concluya ... - Infobae](https://www.infobae.com/peru/2026/06/22/keiko-fujimori-se-reunira-con-julio-velarde-apenas-concluya-el-escrutinio-para-pedirle-que-continue-en-el-bcrp/).

3) No successor could be announced by "the President of Peru" in this window: Peru's runoff was held June 7, 2026 (Fujimori vs. Roberto Sánchez), the change of government / new administration was set for July 28, 2026, and both leading candidates publicly favored Velarde's continuity. The sitting/interim government made no appointment of a Velarde successor, and no El Peruano publication confirming non-renewal was found (the only El Peruano ratification notice for Velarde dates to 2021).

Because within the May 12 – July 1, 2026 window Velarde made no definitive departure/non-renewal statement (he instead signaled openness to staying), no successor was officially announced by Peru's President, and no El Peruano publication confirmed non-renewal, the question resolves NO. (The description's March 2026 Order of the Sun award is explicitly a pre-window, non-committal gesture and does not count.)

URLs:
- https://www.infobae.com/peru/2026/06/20/julio-velarde-se-pronuncia-ante-posibilidad-de-continuar-en-el-banco-central-de-reserva-del-peru-bcrp/
- https://www.infobae.com/peru/2026/06/22/keiko-fujimori-se-reunira-con-julio-velarde-apenas-concluya-el-escrutinio-para-pedirle-que-continue-en-el-bcrp/
- https://www.tvperu.gob.pe/noticias/economia/velarde-sobre-su-continuidad-en-el-bcrp-nadie-se-ha-comunicado-conmigo-y-mi-periodo-vence-el-28-de-julio
- https://rpp.pe/economia/economia/julio-velarde-sobre-continuidad-en-bcrp-pensaba-dejar-cargo-hace-un-par-de-meses-ahora-voy-a-pensarlo-noticia-1693790

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-94. `010a7e76-7d92-50a7-926e-2732f299c585`

- Present date: `2026-05-16 00:21:21.490931`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Argentine Senate approve complete elimination of PASO (rather than making them optional) in its electoral reform bill by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 12, 2026 (00:00 ART, UTC-3) and July 1, 2026 (23:59 ART, UTC-3), the Argentine Senate approves a version of the electoral reform bill that completely eliminates PASO elections — meaning primary elections are neither mandatory nor optional, and the legal framework for holding them is repealed entirely (i.e., parties are not given the choice to hold primaries under the existing PASO system).

This question resolves **No** if any of the following occurs by July 1, 2026 (23:59 ART):
1. The Senate approves a version of the bill that makes primaries optional rather than mandatory (e.g., converting "PASO" to "PAS" by removing the "Obligatorias" requirement while retaining the legal framework for voluntary primaries);
2. The Senate approves a version that merely suspends PASO temporarily rather than eliminating them;
3. The Senate does not approve any version of the PASO reform bill by the deadline.

**Key definitions:**
- "Complete elimination" means the approved text repeals the articles of Law 26.571 (and related provisions) that establish the primary election system, such that no party can hold primaries under the PASO framework. This is distinguished from making primaries "optional," where the legal framework remains but participation is voluntary.
- "Senate approval" means the bill receives a majority vote in the Argentine Senate (media sanción or sanción definitiva depending on chamber of origin).

**Resolution source:** The official text of the approved bill as published on the Argentine Senate website (https://www.senado.gob.ar) or in the parliamentary record. If the Senate website is unavailable, resolution may rely on the Boletín Oficial de la República Argentina (https://www.boletinoficial.gob.ar) or credible Argentine media sources such as Infobae, La Nación, or Clarín.

**Pre-cutoff background**

On April 22, 2026, the Argentine government sent an electoral reform bill to the Senate proposing the complete elimination of the Primarias Abiertas, Simultáneas y Obligatorias (PASO) — the mandatory open primary elections used to select candidates before general elections [The Government's Project to Eliminate the Paso Activated the Pj and ...](https://ground.news/article/the-government-sends-the-bill-to-the-senate-to-repeal-the-pass-and-eliminate-campaign-financing). The bill also includes "Ficha Limpia" (clean record) provisions and changes to party financing rules.

As of May 13, 2026, the bill has not yet been voted on in the Senate. The ruling La Libertad Avanza (LLA) bloc holds only 21 of the 72 Senate seats and needs 37 votes to pass the bill [The Government's Project to Eliminate the Paso Activated the Pj and ...](https://ground.news/article/the-government-sends-the-bill-to-the-senate-to-repeal-the-pass-and-eliminate-campaign-financing). The government faces significant resistance: coalition allies including PRO, the UCR, and several provincial governors oppose full elimination of PASO, viewing the primaries as a useful mechanism for resolving internal party candidacies [https://www.infobrandsen.com.ar/2026/05/08/el-gobierno-evalua-eliminar-la-obligatoriedad-de-las-paso/](https://www.infobrandsen.com.ar/2026/05/08/el-gobierno-evalua-eliminar-la-obligatoriedad-de-las-paso/). As a result, the government is evaluating a compromise that would remove the "Obligatorias" (mandatory) component — converting the system from "PASO" to "PAS" (Primarias Abiertas y Simultáneas) — making primaries optional rather than eliminating them entirely [https://www.infobrandsen.com.ar/2026/05/08/el-gobierno-evalua-eliminar-la-obligatoriedad-de-las-paso/](https://www.infobrandsen.com.ar/2026/05/08/el-gobierno-evalua-eliminar-la-obligatoriedad-de-las-paso/).

This creates genuine uncertainty: the government's original position is full elimination, but securing Senate approval may require accepting the optional-primaries compromise. The outcome depends on intra-coalition negotiations and whether the government can assemble a majority for either version.

**Exact later resolution packet**

The question resolves NO (0).

The question asked whether the Argentine Senate would approve a version of the electoral reform bill that COMPLETELY eliminates PASO (repealing the legal framework entirely, not merely making primaries optional) between May 12, 2026 and July 1, 2026. Per the resolution criteria, the question resolves NO if "The Senate does not approve any version of the PASO reform bill by the deadline."

The evidence overwhelmingly shows the Senate did NOT approve ANY version of the bill (neither full elimination nor an optional-PAS version) by July 1, 2026. The debate was repeatedly stalled and ultimately frozen/postponed until August 2026, well past the deadline:

- La Nación (May 31, 2026): The electoral reform "perdió impulso en el Senado" (lost momentum); the government lacked the required votes. LLA Senate bloc chief Patricia Bullrich told the government to "olvidarse de la eliminación de las PASO" because without UCR and PRO votes it was impossible to reach the absolute majority [98b3ab].
- Canal 26 (June 7, 2026): "La falta de consensos para avanzar con la eliminación de las Primarias Abiertas, Simultáneas y Obligatorias (PASO) llevó al oficialismo a postergar la discusión parlamentaria hasta después del receso invernal," with treatment not expected to return until August 2026 [d5249d].
- La Nueva (June 7, 2026): "El Senado demorará hasta agosto el debate de la reforma electoral..." because the UCR, PRO and provincial blocs reject eliminating PASO and the government cannot muster the 37 votes needed [447ae5].
- Política y Medios (June 30, 2026 — essentially the deadline): The reform "quedó congelada" (was frozen) in the Senate, not expected to advance until August 2026, entering a "parliamentary bottleneck" with no set treatment date; the end of PASO would only aim for 2027 [bc20ed].

Since the Senate never voted on or approved any version of the bill (neither full elimination nor the optional-PAS compromise) before the July 1, 2026, 23:59 ART deadline, resolution condition #3 (the Senate does not approve any version) is satisfied, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-95. `2d86237a-cccc-5df6-9d54-5af3e37a7de8`

- Present date: `2026-05-02 17:24:58.775760`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the 11th Circuit Court of Appeals issue a ruling on American Oversight's appeal (No. 25-13400-A) regarding the release of Volume 2 of the Special Counsel's report by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the U.S. Court of Appeals for the Eleventh Circuit issues a ruling on or after May 1, 2026, and on or before June 1, 2026, 11:59 PM Eastern Time (ET), in the appeal filed by American Oversight (Docket No. 25-13400-A) concerning the release of Volume 2 of Special Counsel Jack Smith's final report on the classified documents investigation involving Donald Trump, Walt Nauta, and Carlos De Oliveira.

A "ruling" is defined as a written opinion (published or unpublished), order, or judgment that resolves the merits of the appeal—i.e., affirming, reversing, vacating, or remanding the district court's order. Procedural or interlocutory orders (such as scheduling orders, motions for extensions of time, stays pending further proceedings, or orders related to briefing) do **not** count as a ruling for resolution purposes.

If no such merits-resolving ruling is issued by 11:59 PM ET on June 1, 2026, the question resolves as **No**.

**Resolution source:** The official docket of the U.S. Court of Appeals for the Eleventh Circuit, accessible via PACER at https://ecf.ca11.uscourts.gov/, and/or credible legal reporting (e.g., Reuters, AP, Law.com, SCOTUSblog).

**Pre-cutoff background**

On January 21, 2025, U.S. District Judge Aileen Cannon issued an order preventing the Department of Justice from releasing Volume 2 of Special Counsel Jack Smith's final report, which concerns former President Donald Trump's handling of classified documents. Volume 2 of the report (as distinguished from Volume 1, which addressed the January 6th investigation and was released in January 2025) has remained under seal since then.

American Oversight, a nonpartisan government watchdog organization, has pursued multiple legal avenues to obtain the report's release. On February 10, 2025, it filed a FOIA lawsuit and motion for preliminary injunction against the DOJ [American Oversight Applauds Eleventh Circuit for Pressing Judge ...](https://americanoversight.org/appeals-court-presses-judge-aileen-cannon-to-release-jack-smith-report-volume-two/). On November 3, 2025, the 11th Circuit found that Judge Cannon's failure to rule on pending motions—which had been fully briefed since March 2025—constituted "undue delay," and gave Judge Cannon 60 days to resolve the issues [American Oversight Applauds Eleventh Circuit for Pressing Judge ...](https://americanoversight.org/appeals-court-presses-judge-aileen-cannon-to-release-jack-smith-report-volume-two/).

On February 23, 2026, Judge Cannon permanently barred the release of Volume 2 of the Special Counsel's report. On February 9, 2026, American Oversight filed a separate appeal (Docket No. 25-13400-A) with the U.S. Court of Appeals for the Eleventh Circuit, seeking to overturn Judge Cannon's denial of American Oversight's motion to intervene in the criminal proceedings [American Oversight Appeals Judge Cannon Order That Could Clear ...](https://americanoversight.org/american-oversight-appeals-judge-cannon-order-that-could-clear-way-for-trump-to-permanently-destroy-jack-smith-report/). The Knight First Amendment Institute at Columbia University and a Yale Law School clinic have also filed briefs urging the 11th Circuit to unseal the report. As of May 1, 2026, the appeal is pending before the 11th Circuit, with briefing believed to be underway or recently completed. The parties in the appeal include American Oversight as the appellant and, on the opposing side, former President Donald Trump and co-defendants Walt Nauta and Carlos De Oliveira.

The 11th Circuit's docket can be accessed via the PACER system at https://www.ca11.uscourts.gov/ or https://ecf.ca11.uscourts.gov/.

**Exact later resolution packet**

The question resolves NO. It asks whether the 11th Circuit Court of Appeals issued a merits-resolving ruling (affirming, reversing, vacating, or remanding) on American Oversight's appeal (No. 25-13400-A) concerning the release of Volume 2 of Special Counsel Jack Smith's report, during the window May 1, 2026 through June 1, 2026, 11:59 PM ET.

The Knight First Amendment Institute maintains a detailed case tracker for this litigation (United States v. Trump et al.) at https://knightcolumbia.org/cases/united-states-v-trump-et-al. As of late May 2026, the status of the appeal was "Briefing ongoing on appeal" [b92236]. The only docketed 11th Circuit activity in the relevant window was an "Order Consolidating Appeals and Setting Briefing Schedule" dated May 28, 2026 [b92236]. That is a procedural/scheduling order, which the resolution criteria explicitly exclude from counting as a "ruling" (procedural or interlocutory orders such as scheduling orders or orders related to briefing do not count).

Since briefing was still ongoing and no opinion, order, or judgment resolving the merits of the appeal was issued by 11:59 PM ET on June 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-96. `317e8d9e-7f48-555a-a979-e49b07c2cde4`

- Present date: `2026-05-13 23:34:56.783106`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-06-15T00:00:00`

**Question**

Will the Bpost postal workers' strike in Belgium be officially declared ended by June 15, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026, and by 23:59 UTC on June 15, 2026, either Bpost management or at least one of the major involved trade unions (CGSP Poste, CSC-Transcom, or VSOA Post) issues an official statement, press release, or public announcement — as reported by credible Belgian news sources such as VRT NWS (https://www.vrt.be/vrtnws/en/), Belga News Agency (https://www.belganewsagency.eu/), RTBF (https://www.rtbf.be/), or Le Soir (https://www.lesoir.be/) — confirming that:

1. A formal agreement has been reached between Bpost management and the unions regarding the disputed transformation plan; AND
2. The indefinite strike action has been officially ended (not merely suspended or paused).

If no such official announcement meeting both conditions is reported by 23:59 UTC on June 15, 2026, the question resolves NO. Temporary truces, informal returns to work without a formal agreement, or continued "work-to-rule" actions without an official end to the strike do not count as resolution.

**Pre-cutoff background**

Since late March 2026, postal workers at Belgium's national postal operator Bpost have been engaged in an indefinite strike protesting a transformation plan that includes changes to working hours — shifting start times from early morning (6–7 a.m.) to mid-morning (9–10 a.m.) and extending work into the evening [Bpost strike ends | VRT NWS: news](https://www.vrt.be/vrtnws/en/2026/04/17/bpost-strike-ends-as-unions-and-management-reach-agreement-on-tr/). The strike caused severe disruptions, particularly in Brussels where all three distribution centers were blocked, halting mail and parcel delivery for weeks [Talks to resolve Bpost strike extended to late May](https://www.belganewsagency.eu/talks-to-resolve-bpost-strike-extended-to-late-may).

On April 17, 2026, an interim agreement was reached between management and unions, and workers temporarily returned to work [Bpost strike ends | VRT NWS: news](https://www.vrt.be/vrtnws/en/2026/04/17/bpost-strike-ends-as-unions-and-management-reach-agreement-on-tr/). However, the strike resumed shortly after as final terms remained unresolved. By late April, distribution centers in Brussels were again blocked [Talks to resolve Bpost strike extended to late May](https://www.belganewsagency.eu/talks-to-resolve-bpost-strike-extended-to-late-may).

As of May 5, 2026, physical blockades at distribution centers have been lifted and operations are gradually returning to normal, but no official announcement has been made by Bpost management or the involved trade unions (CGSP Poste, CSC-Transcom, VSOA Post) formally ending or suspending the strike [Bpost postal workers indefinite strike from late March 2026 over ...](https://striketracker.app/strikes-in-belgium/postal-workers-strike-brussels-9-april-2026). Negotiations were extended, with both sides targeting May 28, 2026 as a deadline for reaching a final agreement [Talks to resolve Bpost strike extended to late May](https://www.belganewsagency.eu/talks-to-resolve-bpost-strike-extended-to-late-may). The strike has cost Bpost an estimated €15 million or more.

Key unions involved are CGSP Poste (socialist public sector union), CSC-Transcom (Christian union), and VSOA Post (liberal union). Resolution sources include VRT NWS (https://www.vrt.be/vrtnws/en/), Belga News Agency (https://www.belganewsagency.eu/), and Bpost's own communications.

**Exact later resolution packet**

The question resolves NO. It required an official announcement, reported between May 12 and June 15, 2026 by VRT NWS, Belga, RTBF, or Le Soir, confirming BOTH (1) a formal agreement on the disputed transformation plan AND (2) that the indefinite strike was officially ended (not merely suspended). Neither condition was satisfied within the window.

WHAT HAPPENED IN THE WINDOW:
- May 26, 2026: Negotiations concluded and the result was submitted to union members, with a final joint-committee meeting scheduled for Thursday May 28. No agreement was finalized yet, and the outcome "does not yet mean the end of the strike" (RTL/La Libre via Belga) [c89475, 0c50a4].
- May 28, 2026: Bpost management and unions reached a new collective labour agreement (CCT/CAO) for 2026-2027. However, this did NOT resolve the disputed transformation plan. RTBF (May 28) reported the two largest unions (CSC and CGSP) REFUSED to vote for the CCT, and a union representative said "Je ne suis plus aujourd'hui en capacité de garantir la paix sociale" ("I am no longer able to guarantee social peace today") [f1797b]. Belga's own headline was "Bpost and unions reach collective agreement, but row over working hours persists" [268240].
- VRT NWS (May 28) reported unions "remain opposed to the plan to have postmen start their rounds later," that the company can impose the later working hours WITHOUT union agreement, and "it will still have to be negotiated" — i.e., the transformation-plan dispute was explicitly NOT settled [2f2be3].
- VRT NWS (May 29) quoted CEO Chris Peeters: "We have taken a very important step, but we are not there yet," and stated "the discussion about the transformation plan ... has not yet been settled," with strikes still occurring in Liège and Seraing [e06c56].
- Le Soir (May 29) reported postmen in Liège (58) and Seraing were ON STRIKE on May 29 — the day AFTER the CCT — and that unions "continue to oppose the lengthening of working hours that the post office will implement starting in September" [8748c4].
- RTBF (June 1) headline "Fin de la grève chez bpost" referred only to a LOCAL return to work in Liège and Seraing after a spontaneous local strike, not an official national end of the indefinite strike; the transformation plan was set to be applied in September [34a3ab].

WHY IT FAILS BOTH CONDITIONS:
- Condition 1 (formal agreement on the disputed transformation plan): The May 28 CCT covered job security, meal vouchers and bonuses, but the core disputed issue — the transformation plan / shift of working hours — was NOT agreed; the major unions rejected it and Bpost was to implement it unilaterally from September [2f2be3, f1797b, 8748c4].
- Condition 2 (strike officially ended, not merely suspended): No source among VRT NWS/Belga/RTBF/Le Soir reported an official end of the indefinite strike. On the contrary, postmen resumed/continued striking after the CCT (Liège & Seraing, May 29), and further disruptions were being planned. Bpost's own press release (Bnode) framed the CCT positively but is a company release, not one of the four specified news outlets, and even it did not declare the strike "officially ended" [049c9b].

Per the resolution criteria, "Temporary truces, informal returns to work without a formal agreement ... do not count," and if the criteria are not fully met the question resolves NO. Both conditions fail, so the resolution is NO (0).

Key verification URLs: https://www.rtbf.be/article/la-direction-de-bpost-et-les-syndicats-se-sont-accordes-sur-une-nouvelle-convention-collective-de-travail-11731459 ; https://www.vrt.be/vrtnws/nl/2026/05/28/bpost-nieuwe-cao/ ; https://www.vrt.be/vrtnws/nl/2026/05/29/sociaal-akkoord-bpost-reactie-ceo-chris-peeters/ ; https://www.lesoir.be/749585/article/2026-05-29/bpost-les-facteurs-en-greve-ce-vendredi-liege ; https://www.rtbf.be/article/fin-de-la-greve-chez-bpost-les-facteurs-de-liege-et-seraing-ont-repris-le-travail-11733090

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-97. `d2c5fcaa-b273-5787-9846-32c25c11f11b`

- Present date: `2026-05-03 02:44:56.648996`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. government announce a final decision on the Section 232 investigation into polysilicon imports by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026 (00:00 UTC) and on or before June 1, 2026 (23:59 UTC), the U.S. government publicly announces a final decision on the Section 232 national security investigation into polysilicon and its derivatives.

A "final decision" is defined as either:
1. A **Presidential Proclamation** imposing, modifying, or declining to impose tariffs, quotas, or other trade remedies based on the investigation; or
2. An official announcement from the **Secretary of Commerce** or the **White House** that the President has made a final determination on the investigation (including a determination to take no action).

The announcement must appear on an official U.S. government source, such as:
- The White House Briefing Room (https://www.whitehouse.gov/briefing-room/)
- The Department of Commerce Newsroom (https://www.commerce.gov/news)
- The Federal Register (https://www.federalregister.gov/)

Interim reports, leaked drafts, or unofficial statements do not count. The question resolves **No** if no such formal announcement is made by June 1, 2026 (23:59 UTC).

**Pre-cutoff background**

On July 1, 2025, the U.S. Secretary of Commerce initiated a [Section 232 investigation](https://en.wikipedia.org/wiki/Section_232_(Trade_Expansion_Act_of_1962)) into imports of polysilicon and its derivatives, pursuant to Section 232 of the Trade Expansion Act of 1962 (19 U.S.C. § 1862). This statute authorizes the President to adjust imports if they are found to threaten national security. The investigation was formally announced via the Federal Register on July 16, 2025 (https://www.federalregister.gov/documents/2025/07/16/2025-13345/notice-of-request-for-public-comments-on-section-232-national-security-investigation-of-imports-of).

Polysilicon is a critical input for crystalline silicon solar cells, which dominate the global solar market. China controls a large majority of global polysilicon production capacity. A Section 232 tariff on polysilicon would significantly impact the crystalline silicon solar supply chain while potentially benefiting manufacturers using alternative technologies, such as First Solar (which uses cadmium telluride rather than polysilicon).

As of May 1, 2026, approximately 10 months have elapsed since the investigation's initiation. During First Solar's Q1 2026 earnings call on April 30, 2026, management indicated they expect a resolution by end of Q2 2026 (i.e., by end of June 2026) but noted the timeline could extend into early Q3 2026 [https://ca.finance.yahoo.com/news/first-solar-inc-fslr-q1-071924707.html](https://ca.finance.yahoo.com/news/first-solar-inc-fslr-q1-071924707.html). Under Section 232, the Secretary of Commerce has 270 days from initiation to deliver a report to the President, who then has 90 days to act. The 270-day deadline from July 1, 2025 would fall around late March 2026, suggesting the Commerce report may already have been delivered to the President, though no public announcement of a final decision has been made as of May 1, 2026.

The Bureau of Industry and Security maintains an official page on Section 232 investigations at https://www.bis.gov/about-bis/bis-leadership-and-offices/SIES/section-232-investigations.

**Exact later resolution packet**

The question resolves NO because no Presidential Proclamation or official Commerce/White House announcement of a final determination on the Section 232 polysilicon investigation was made between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC).

Key evidence:
- A Covington & Burling LLP alert dated April 23, 2026 explicitly listed the "Polysilicon & Its Derivatives" Section 232 investigation as still "Pending," with an expected "Announcement of Action (If Any)" not until "Mid-July 2026" [295812]. This confirms no final decision had been made before the resolution window, and that the anticipated decision date falls AFTER the June 1, 2026 deadline.
- A Congressional Research Service report (R48549), updated January 12, 2026, listed polysilicon under "Potential Tariff Actions: Section 232" with status "Under Investigation," with no final determination or proclamation [57e6a9].
- The PV-Tech page on polysilicon Section 232 tariffs (originally Oct 2025), whose live news feed contained items dated June 1–2, 2026, contained no report of any final decision/proclamation on polysilicon as of the close of the resolution window [cb4689].

While the Trump administration issued numerous other Section 232 proclamations in early 2026 (e.g., advanced semiconductors on Jan 14, 2026; steel/aluminum/copper on April 2, 2026; pharmaceuticals on April 2, 2026), none of these concerned polysilicon. The official BIS Section 232 investigations page continued to list the polysilicon investigation (initiated July 1, 2025) without any final determination.

Because the resolution window (May 1 – June 1, 2026) closed with no qualifying final decision announced on any official U.S. government source, the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-98. `49907cf8-ca9f-505f-9a20-e0471c9b2493`

- Present date: `2026-05-02 19:00:54.078555`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a proposed constitutional amendment restricting the office of pastor to men be formally included in the 2026 SBC Annual Meeting Order of Business by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, by June 1, 2026 (23:59 UTC), the SBC Committee on Order of Business or another official SBC body (e.g., Baptist Press at https://www.baptistpress.com/ or SBC.net at https://www.sbc.net/) publishes an official agenda, Order of Business, Book of Reports, or other formal notice confirming that a proposed constitutional amendment restricting the office of pastor or elder to men will be considered at the 2026 SBC Annual Meeting (June 9–10, 2026, Orlando, FL).

A "constitutional amendment" means a proposed change to the [SBC Constitution](https://www.sbc.net/about/what-we-believe/the-constitution-of-the-southern-baptist-convention/), not a bylaw change or a non-binding resolution.

The question resolves **No** if no such official publication confirms the inclusion of such a constitutional amendment on the Order of Business by June 1, 2026 (23:59 UTC). It also resolves **No** if only bylaw amendments (not constitutional amendments) regarding women pastors are scheduled.

Only official SBC publications released on or after May 1, 2026 count toward resolution. Earlier preliminary schedules that do not specifically list constitutional amendment items do not count unless they explicitly include such an amendment.

Resolution source: Official SBC publications, specifically the Book of Reports or Order of Business at https://www.sbc.net/resources/ or reporting by Baptist Press at https://www.baptistpress.com/resource-library/topic-index/sbc-annual-meetings/.

**Pre-cutoff background**

The Southern Baptist Convention (SBC), America's largest Protestant denomination (~12.7 million members), has debated whether to amend its [Constitution](https://www.sbc.net/about/what-we-believe/the-constitution-of-the-southern-baptist-convention/) to explicitly bar churches with women pastors from cooperation. A proposed change known as the "Law Amendment" would add language to Article III requiring cooperating churches to "affirm, appoint, or employ only men as any kind of pastor or elder as qualified by Scripture."

Under SBC rules, a constitutional amendment requires approval by a two-thirds (66.67%) supermajority of [messengers](https://en.wikipedia.org/wiki/Messenger_(Southern_Baptist_Convention)) (voting delegates) present at two consecutive Annual Meetings. The amendment received approximately 61.45% support in 2024 and 60.74% in 2025—both falling short of the required two-thirds threshold [Here's what didn't happen at this year's SBC meeting](https://baptistnews.com/article/heres-what-didnt-happen-at-this-years-sbc-meeting/). At the 2025 Annual Meeting in Dallas, the convention "did not advance a third try at the so-called Law Amendment" [Here's what didn't happen at this year's SBC meeting](https://baptistnews.com/article/heres-what-didnt-happen-at-this-years-sbc-meeting/), meaning a new amendment would need to be formally proposed and placed on the agenda for 2026.

The 2026 SBC Annual Meeting is scheduled for June 9–10, 2026, in Orlando, Florida [2026 SBC Annual Meeting - Orlando, FL](https://sbcannualmeeting.net/). A preliminary schedule was released on March 10, 2026, by the Committee on Order of Business. SBC President Clint Pressley has indicated he expects legislative conversations on women pastors to return. Alternative approaches, such as amending Bylaw 8 instead of the Constitution, have also been proposed. Whether a new amendment is formally submitted and placed on the Order of Business before the meeting remains uncertain, particularly given two consecutive failures and reported "fatigue" on the issue.

The SBC Committee on Order of Business publishes the final program and agenda items—including any constitutional amendments—in the weeks preceding the Annual Meeting, typically in the [Book of Reports](https://www.sbc.net/resources/) and via [Baptist Press](https://www.baptistpress.com/). These publications are expected by late May or early June 2026.

**Exact later resolution packet**

The question resolves NO because, by the June 1, 2026 (23:59 UTC) deadline, no official SBC publication confirmed that a proposed constitutional amendment restricting the office of pastor/elder to men was formally included in the 2026 SBC Annual Meeting Order of Business.

Key evidence:

1. The official "2026 SBC Annual Meeting schedule released" article from Baptist Press lists the Order of Business / program, and it does NOT include any constitutional amendment restricting the office of pastor or elder to men. The latest SBC news entries on that page (through June 1, 2026) likewise show no such amendment being added to the agenda [e3daa6].

2. The only relevant development is Albert Mohler's announcement (published May 18, 2026 on Baptist Press and his personal blog) that he INTENDS to propose a "Truth & Unity" amendment to Article III of the SBC Constitution. Crucially, this is a motion he plans to make from the floor at the meeting. He explicitly states he will move to suspend Standing Rule 6 so that the Committee on Order of Business MAY schedule the motion for debate — confirming the amendment is NOT yet on the official Order of Business [20d242, f5a2bf].

3. Mohler's proposed wording would add to the Constitution that cooperating churches do "not act to affirm, appoint, or endorse a woman serving in the office or function of a pastor/elder/overseer." While this is indeed a constitutional amendment (not a bylaw change or resolution) addressing restricting the pastor/elder office to men, the resolution criteria require an official publication confirming it has been placed ON the Order of Business — not merely an announced intent to introduce it from the floor [f5a2bf].

Because the procedure described is a floor motion requiring suspension of standing rules to even be scheduled, and no official Order of Business / Book of Reports published by June 1, 2026 lists such a constitutional amendment as a confirmed agenda item, the YES condition is not met. The question resolves NO.

Sources:
- Baptist Press, "Mohler to call for 'Truth & Unity' amendment to SBC Constitution at annual meeting" (May 18, 2026): https://www.baptistpress.com/resource-library/news/mohler-to-call-for-truth-unity-amendment-to-sbc-constitution-at-annual-meeting/ [20d242]
- AlbertMohler.com, "Truth and Unity Amendment" (May 18, 2026): https://albertmohler.com/2026/05/18/truth-and-unity-amendment/ [f5a2bf]
- Baptist Press, "2026 SBC Annual Meeting schedule released": https://www.baptistpress.com/resource-library/news/2026-sbc-annual-meeting-schedule-released/ [e3daa6]

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-99. `a52206db-3c2f-5e6e-a7c8-9c995b9e0b93`

- Present date: `2026-05-03 00:21:50.366159`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any Magnificent Seven company announce a new workforce reduction of at least 1,000 employees explicitly citing AI between May 1 and May 31, 2026?

**Resolution criteria**

This question resolves as **Yes** if, between 00:00 UTC on May 1, 2026 and 23:59 UTC on May 31, 2026, any of the following seven companies announces a new workforce reduction affecting at least 1,000 employees and explicitly cites AI as a reason:

**Companies (the "Magnificent Seven"):**
- Alphabet ([SEC filings](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001652044&type=8-K) | [Investor Relations](https://abc.xyz/investor/))
- Amazon ([SEC filings](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001018724&type=8-K) | [Investor Relations](https://ir.aboutamazon.com/))
- Apple ([SEC filings](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000320193&type=8-K) | [Investor Relations](https://investor.apple.com/))
- Meta ([SEC filings](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001326801&type=8-K) | [Investor Relations](https://investor.fb.com/))
- Microsoft ([SEC filings](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000789019&type=8-K) | [Investor Relations](https://www.microsoft.com/en-us/investor))
- Nvidia ([SEC filings](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001045810&type=8-K) | [Investor Relations](https://investor.nvidia.com/))
- Tesla ([SEC filings](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001318605&type=8-K) | [Investor Relations](https://ir.tesla.com/))

**"Explicitly citing AI"** means the official announcement must contain at least one of the following keywords: "artificial intelligence," "AI," "generative AI," "LLM," "large language model," "machine learning," or "automation" in the stated justification for the workforce reduction.

**Valid "workforce reduction" announcement** means any of the following, dated on or after May 1, 2026:
1. An SEC Form 8-K filing disclosing the reduction;
2. An official press release or blog post on the company's corporate newsroom;
3. An internal company memo or email that is reported verbatim or in substantial detail by at least two of the following major news sources: Reuters, AP, Bloomberg, The Wall Street Journal, The New York Times, CNBC, or the Financial Times.

The announcement must describe a **new** workforce reduction — i.e., one not previously announced before May 1, 2026. Execution of previously announced cuts (e.g., Meta's cuts beginning May 20 that were announced on April 23, 2026 [20k job cuts at Meta, Microsoft raise concern of AI labor crisis - CNBC](https://www.cnbc.com/2026/04/24/20k-job-cuts-at-meta-microsoft-raise-concern-of-ai-labor-crisis-.html)) does not count. However, if a company announces an expansion or acceleration of a prior plan that adds at least 1,000 additional employees to the reduction beyond what was previously disclosed, that qualifies as a new announcement.

The reduction must affect at least 1,000 employees (including through layoffs, voluntary buyouts, or position eliminations).

If no qualifying announcement is made by any of the seven companies within the specified timeframe, the question resolves as **No**.

**Pre-cutoff background**

As of May 1, 2026, the technology sector is experiencing a major wave of AI-linked layoffs. In late April 2026, Meta announced it would cut 10% of its workforce (~8,000 jobs), with cuts beginning May 20, explicitly to "offset the other investments we're making" in AI infrastructure [20k job cuts at Meta, Microsoft raise concern of AI labor crisis - CNBC](https://www.cnbc.com/2026/04/24/20k-job-cuts-at-meta-microsoft-raise-concern-of-ai-labor-crisis-.html). On the same day, Microsoft confirmed it is offering voluntary buyouts for the first time in its 51-year history, with approximately 7% of U.S. employees (~8,750) eligible [20k job cuts at Meta, Microsoft raise concern of AI labor crisis - CNBC](https://www.cnbc.com/2026/04/24/20k-job-cuts-at-meta-microsoft-raise-concern-of-ai-labor-crisis-.html). Amazon announced in January 2026 that it was eliminating approximately 16,000 corporate roles globally [https://www.businessinsider.com/recent-company-layoffs-laying-off-workers-2026](https://www.businessinsider.com/recent-company-layoffs-laying-off-workers-2026). Meta had also begun earlier layoffs across multiple teams in March 2026 as part of restructuring to shift resources toward AI [https://www.businessinsider.com/recent-company-layoffs-laying-off-workers-2026](https://www.businessinsider.com/recent-company-layoffs-laying-off-workers-2026).

Industry-wide, tech layoffs in the first quarter of 2026 exceeded 78,000, with more than 76% of affected positions linked to AI-related restructuring. Companies such as Oracle (25,000+), Block (4,000), and Atlassian (1,600) have also made significant AI-cited cuts. The trend of companies reallocating headcount budgets toward AI infrastructure spending continues to accelerate.

Among the Magnificent Seven specifically, Meta and Amazon have already conducted major rounds of cuts in 2026, and Microsoft has initiated its buyout program. Alphabet, Apple, Nvidia, and Tesla have not announced major layoffs in 2026 as of this writing [https://www.businessinsider.com/recent-company-layoffs-laying-off-workers-2026](https://www.businessinsider.com/recent-company-layoffs-laying-off-workers-2026).

**Exact later resolution packet**

The question asks whether any Magnificent Seven company (Alphabet, Amazon, Apple, Meta, Microsoft, Nvidia, Tesla) announced a NEW workforce reduction of at least 1,000 employees explicitly citing AI between May 1 and May 31, 2026. The resolution is NO.

Examining each company:

- META: Its ~8,000-job (10%) cut was announced April 23, 2026, with cuts beginning May 20. The resolution criteria EXPLICITLY exclude this: "Execution of previously announced cuts (e.g., Meta's cuts beginning May 20 that were announced on April 23, 2026) does not count." May 2026 reporting (e.g., the May 18 CNBC story and a 24/7 Wall St. piece noting Zuckerberg "told 8,000 employees in early May") concerns execution and internal communication of the already-announced April plan, not a new reduction or an expansion adding 1,000+ additional employees [70a956, 1c03f1]. So Meta does not qualify.

- AMAZON: Its 16,000-role cut was announced in January 2026, and its 14,000-role cut was announced October 28, 2025 [3ca729]. Reports of a fresh ~14,000-person "May 2026" layoff round were explicitly DENIED by Amazon, whose spokesperson called them "false and not based in fact" (per Firstpost/Mint/Times of India coverage, April 2026). Viral May 18-19 social-media posts claiming "Amazon just fired 16,000 citing agentic AI" recycled the earlier January/October announcements; no new official Amazon SEC filing, press release, or memo dated in May 2026 was found. Reuters' May 21, 2026 AI-layoffs tracker lists Amazon only under "January" [9e20c7].

- MICROSOFT: Only its subsidiary LinkedIn announced cuts in May (~5%, roughly 875 employees) per Reuters/Bloomberg [1c03f1]. That is below the 1,000 threshold and LinkedIn is not one of the seven named entities; Microsoft's own buyout program was announced in April 2026.

- ALPHABET, APPLE, NVIDIA, TESLA: No new May 2026 announcement of a 1,000+ reduction citing AI was found in any source [defd51, d18ff3, 1c03f1, 9e20c7].

Multiple independent trackers corroborate that the only May 2026 AI-linked layoffs of 1,000+ came from NON-Magnificent-Seven companies: Reuters' tracker lists Standard Chartered, Cisco, Intuit, Cloudflare, Freshworks for May [9e20c7]; InformationWeek's tracker lists Groupon, Wix, ClickUp, Intuit, Cisco, LinkedIn, Coinbase for May [1c03f1]; the WSJ 2026 layoffs tracker and Business Insider list no qualifying new Mag-7 May announcement [defd51, d18ff3].

Because no Magnificent Seven company made a NEW (not previously announced) workforce-reduction announcement affecting at least 1,000 employees that explicitly cited AI within the May 1–31, 2026 window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-100. `7a1ef715-5b39-5429-b0e8-5adf684581dd`

- Present date: `2026-05-16 09:56:43.510576`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Samsung Electronics experience a complete production line shutdown lasting at least 72 continuous hours at any semiconductor fabrication facility between May 21 and June 30, 2026 (UTC)?

**Resolution criteria**

This question resolves YES if, between May 12, 2026 00:00 UTC and July 1, 2026 00:00 UTC, at least one semiconductor wafer fabrication line at any Samsung Electronics facility (including but not limited to the Pyeongtaek and Hwaseong campuses) experiences a **complete cessation of wafer processing operations for a continuous period of at least 72 hours**.

Definitions:
- **"Production line shutdown"**: The total cessation of wafer processing activity (i.e., no new wafers entering the line and no active processing steps occurring) on at least one specific fab line or cleanroom module. A reduction in output or slowdown does not qualify; the line must be fully idle for the entire 72-hour continuous period.
- **"72 continuous hours"**: The shutdown must last at least 72 hours without interruption. Cumulative downtime across separate incidents does not count.
- All times are in **UTC**.

**Resolution sources**: The shutdown must be confirmed by at least one of the following:
1. An official Samsung Electronics communication, such as a press release or filing on Samsung's Investor Relations page (https://www.samsung.com/global/ir/).
2. A report from a major financial or industry news outlet: Reuters (https://www.reuters.com), Bloomberg (https://www.bloomberg.com), TrendForce (https://www.trendforce.com), Digitimes (https://www.digitimes.com), The Korea Herald (https://www.koreaherald.com), or Yonhap News Agency (https://en.yna.co.kr).

If no such confirmed report exists by July 1, 2026 00:00 UTC, the question resolves **NO**.

**Pre-cutoff background**

As of May 13, 2026, Samsung Electronics faces the most severe labor crisis in its corporate history. The National Samsung Electronics Union, representing approximately 30,000 chip workers, has planned an 18-day general strike from May 21 through June 7, 2026, after wage negotiations collapsed in February 2026 [Samsung Electronics' union says to enter mediation over wage dispute](https://www.reuters.com/sustainability/sustainable-finance-reporting/samsung-electronics-union-says-enter-mediation-over-wage-dispute-2026-05-08/). The union demands a 15% performance bonus tied to operating profits and changes to the bonus system. On May 11–12, 2026, government-mediated talks were held, but the union's 2.6 billion won bonus demand stalled negotiations [Samsung Electronics' union says to enter mediation over wage dispute](https://www.reuters.com/sustainability/sustainable-finance-reporting/samsung-electronics-union-says-enter-mediation-over-wage-dispute-2026-05-08/).

A rift has emerged between Samsung's chip division and non-chip division union workers, meaning participation may be uneven (https://www.kedglobal.com/labor-union/newsView/ked202605030002). The union chief has stated the strike could affect about half the output at Samsung's chip plants (https://www.reuters.com/business/world-at-work/samsung-elec-workers-strike-plan-would-disrupt-chip-supply-union-chief-says-2026-03-16/).

TrendForce estimates the strike could disrupt 3–4% of global DRAM output and 2–3% of NAND output, with weeks-long recovery risk [[News] Samsung's May Strike Seen Disrupting Up to 4% of DRAM ...](https://www.trendforce.com/news/2026/04/27/news-samsungs-may-strike-seen-disrupting-up-to-4-of-dram-output-with-weeks-long-recovery-risk/). During the 2024 Samsung strike, production impact was limited as management maintained operations through automated systems and management staff. However, the 2026 planned action is significantly larger in scale (30,000–40,000 workers vs. a smaller group in 2024). Samsung's Pyeongtaek and Hwaseong fabrication plants are the primary facilities at risk.

As of May 13, 2026, no deal has been reached and the May 21 strike date remains in effect, though last-minute negotiations continue [Samsung Electronics' union says to enter mediation over wage dispute](https://www.reuters.com/sustainability/sustainable-finance-reporting/samsung-electronics-union-says-enter-mediation-over-wage-dispute-2026-05-08/).

**Exact later resolution packet**

The question resolves **NO**. It required that, between May 12, 2026 00:00 UTC and July 1, 2026 00:00 UTC, at least one Samsung semiconductor wafer fabrication line experience a COMPLETE cessation of wafer processing (no new wafers entering AND no active processing steps) for a continuous period of ≥72 hours, confirmed by an approved source (Samsung IR, Reuters, Bloomberg, TrendForce, Digitimes, Korea Herald, or Yonhap). No such event occurred or was reported.

Key facts established from approved sources:

1. The strike never happened. The National Samsung Electronics Union's planned 18-day general strike (scheduled May 21–June 7, 2026) was suspended after Samsung and the union reached a tentative wage deal on May 21, 2026 — roughly 1.5 hours before the strike was to begin. Reuters reported the suspension on May 20/21, 2026 (https://www.reuters.com/business/world-at-work/samsung-elec-union-resume-pay-talks-one-day-ahead-strike-deadline-2026-05-20/) [Samsung union suspends planned strike after reaching ... - Reuters](https://www.reuters.com/business/world-at-work/samsung-elec-union-resume-pay-talks-one-day-ahead-strike-deadline-2026-05-20/). Union members ratified the deal on May 27, 2026, with ~74% approval, formally averting the strike, per Reuters (https://www.reuters.com/business/world-at-work/samsungs-unionised-workers-south-korea-approve-wage-deal-2026-05-27/) [Samsung workers approve pay deal but management still ...](https://www.reuters.com/business/world-at-work/samsungs-unionised-workers-south-korea-approve-wage-deal-2026-05-27/). Because the strike was never launched, no labor action idled any fab line.

2. The pre-strike measures were a throttling/reduction, NOT a complete cessation. In the days before May 21, Samsung entered "emergency management mode." According to The Korea Herald (an approved source), published May 14, 2026, this involved "adjusting production" — restricting the number of new wafers fed into the lines and reshuffling the product mix toward higher-value chips — specifically to "minimize damage" to yields, not a full stop (https://www.koreaherald.com/article/10738243) [Samsung enters emergency mode ahead of chip union strike](https://www.koreaherald.com/article/10738243). Corroborating (non-approved) reporting described "throttling semiconductor output" by "cutting new wafer input" and placing some lithography/etching/cleaning tools "on standby" — again a reduction, not a 72-hour complete idle of a line [Samsung starts winding down chip production six days before ...](https://www.tomshardware.com/tech-industry/samsung-starts-winding-down-chip-producton-six-days-before-planned-18-day-strike). Wafers already in progress continue to be processed during a wind-down, so this does not meet the "no active processing steps occurring" standard.

3. No other qualifying event. A Chosun Ilbo article dated July 1, 2026 about a three-day Austin fab power outage refers to the historical February 2021 winter-storm outage (71,000 wafers scrapped, ~510 billion won loss), not an event within the May–June 2026 window [Samsung's Austin Fab Outage: 510 Billion Won Loss](https://www.chosun.com/english/industry-en/2026/07/01/B7ISH3CPO5DQPO7IMQDNFCJD7A/). A June 12, 2026 Reuters report about a South Korean concrete-delivery halt concerned construction of new chip plants, not any operating production line shutdown. No approved source (Reuters, Bloomberg, TrendForce, Digitimes, Korea Herald, Yonhap, or Samsung IR) reports a complete 72-continuous-hour cessation of wafer processing at any Samsung fab during the window.

Since no confirmed report of a ≥72-hour complete wafer-processing shutdown exists by July 1, 2026 00:00 UTC, the resolution criteria's default applies and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-101. `752483bd-c61e-58a0-9fd5-6033eceea25f`

- Present date: `2026-05-02 21:24:38.401461`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Missouri's SB 838 (nuclear energy expansion bill) be signed into law by the Governor by June 1, 2026?

**Resolution criteria**

This question resolves YES if Missouri Senate Bill 838 (2026 session) is signed into law by the Governor of Missouri, becomes law without the Governor's signature, or is vetoed and subsequently overridden by the legislature, with such action occurring on or after May 1, 2026 and no later than 11:59 PM Central Time on June 1, 2026.

This question resolves NO if none of the above conditions are met by 11:59 PM CT on June 1, 2026—including if the bill is vetoed without override, fails to pass either chamber, or remains unsigned.

The primary resolution source is the Missouri General Assembly official bill tracking page for SB 838: https://www.senate.mo.gov/BillTracking/Bills/BillInformation?year=2026&billid=274. Secondary sources include the Missouri Governor's official website and credible news reporting (e.g., Missouri Independent, Missourinet, AP).

**Pre-cutoff background**

Missouri Senate Bill 838 (SB 838), sponsored by Senator Mike Cierpiot (R-Lee's Summit), modifies provisions relating to nuclear energy and electric utilities in Missouri. Key provisions include allowing electric transmission facilities within highway rights-of-way, removing restrictions on nuclear energy purchases by the State Environmental Improvement and Energy Resources Authority, modifying renewable energy portfolio requirements, and authorizing zero-emission credit programs [SB 838 - Bill Information - Missouri Senate](https://www.senate.mo.gov/BillTracking/Bills/BillInformation?year=2026&billid=274).

The bill has been a subject of significant debate, particularly regarding "Construction Work in Progress" (CWIP) financing—a practice that allows utilities to collect money from ratepayers for projects still under construction. Missouri voters banned CWIP in the 1970s, and an amendment addressing this issue was adopted by a narrow 14–13 vote during initial Senate consideration on April 9, 2026 [Missouri Senate Advances Nuclear Energy Bill After Closely Divided ...](https://www.missourinet.com/2026/04/09/missouri-senate-advances-nuclear-energy-bill-after-closely-divided-vote/).

As of May 1, 2026, SB 838 is on the "Informal Calendar S Bills for Third Reading" in the Missouri Senate, having been amended with a Senate Substitute for Senate Committee Substitute (SS SCS) and three Senate Amendments (SA 1, SA 2, SA 3) [SB 838 - Bill Information - Missouri Senate](https://www.senate.mo.gov/BillTracking/Bills/BillInformation?year=2026&billid=274). The bill still needs to pass the Senate on third reading, then pass the Missouri House of Representatives (or go through a conference process), and then be sent to the Governor. Missouri's regular legislative session typically concludes on May 30, creating a tight timeline for enactment.

Official bill tracking page: https://www.senate.mo.gov/BillTracking/Bills/BillInformation?year=2026&billid=274

**Exact later resolution packet**

The question resolves NO. To resolve YES, Missouri SB 838 (2026 session) would have had to be signed into law, become law without the Governor's signature, or be vetoed and overridden, with that action occurring between May 1, 2026 and 11:59 PM CT on June 1, 2026.

Evidence:
- The official Missouri General Assembly bill tracking page for SB 838 (https://www.senate.mo.gov/BillTracking/Bills/BillInformation?year=2026&billid=274) shows the bill's last status as "Informal Calendar S Bills for Third Reading" [2f6eeb]. This means the bill never even passed the Senate on Third Reading; it never advanced to the House and was never sent to the Governor. None of the three YES conditions (signature, law without signature, veto override) were met.
- The 2026 Missouri legislative session adjourned (sine die) on Friday, May 15, 2026, with the legislature concluding its work (corroborated by Missouri Bar 2026 Legislative Updates and Missouri Independent's "Missouri legislature ends 2026 session" reporting found via Google). Because SB 838 was still stuck on the Senate's Informal Calendar at adjournment, the bill died without passage. Consequently, it could not have been signed, become law, or undergone a veto/override during the May 1 – June 1, 2026 window.

Since the bill never passed either chamber and never reached the Governor, none of the YES conditions occurred by the June 1, 2026 deadline, so the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-102. `fef6f75e-bd18-5994-b56f-99b3925acf4b`

- Present date: `2026-05-29 07:34:58.194095`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Constitutional Court of South Korea issue a ruling on the constitutionality of the insurrection tribunal law by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the Constitutional Court of South Korea issues a ruling on the constitutionality of the insurrection tribunal law on or after May 12, 2026, and on or before July 1, 2026, 23:59 UTC.

A "ruling" is defined as a **final decision on the merits** (i.e., a judgment on whether the law is constitutional, unconstitutional, or conditionally constitutional) issued by the full bench of the Constitutional Court of Korea. Interim or procedural decisions — such as orders on expedited review, injunctions, scheduling decisions, or dismissals on procedural/jurisdictional grounds without addressing constitutionality — do **not** count as a ruling for purposes of this question.

If no such final decision on the merits is issued by the deadline, the question resolves as **No**.

**Resolution source:** The official Constitutional Court of Korea website (https://english.ccourt.go.kr/site/eng/ex/bbs/List.do?cbIdx=1143) or reporting by Yonhap News Agency (https://en.yna.co.kr/).

**Pre-cutoff background**

On March 31, 2026, former President Yoon Suk Yeol filed a constitutional petition challenging the "insurrection tribunal law," which was passed by the National Assembly in December 2025 and took effect in January 2026. This law established dedicated tribunals within the Seoul High Court to handle insurrection charges related to Yoon's 2024 martial law attempt [Yoon's constitutional petition against insurrection tribunal ...](https://www.koreatimes.co.kr/southkorea/law-crime/20260422/yoons-constitutional-petition-against-insurrection-tribunal-law-referred-to-formal-review).

Yoon's petition argues that the law infringes upon the right to a fair trial and the right to equality by imposing procedures significantly different from general criminal proceedings, and that it limits the presumption of innocence [Yoon's constitutional petition against insurrection tribunal ...](https://www.koreatimes.co.kr/southkorea/law-crime/20260422/yoons-constitutional-petition-against-insurrection-tribunal-law-referred-to-formal-review). On April 21, 2026, the Constitutional Court referred the case to its full nine-member bench for formal review [Yoon's constitutional petition against insurrection tribunal ...](https://www.koreatimes.co.kr/southkorea/law-crime/20260422/yoons-constitutional-petition-against-insurrection-tribunal-law-referred-to-formal-review). Additionally, the Seoul High Court is considering whether to separately request a constitutional review of the law.

Yoon was convicted of insurrection on February 19, 2026, sentenced to life imprisonment, and his appeals trial began on April 27, 2026. The political salience of the case creates pressure for faster resolution, but Korean Constitutional Court cases can range from weeks to over a year. As of mid-May 2026, no ruling on the constitutionality of the insurrection tribunal law has been issued.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if the Constitutional Court of Korea issued a final decision on the merits (a judgment on whether the "insurrection tribunal law" is constitutional/unconstitutional/conditionally constitutional) by the full bench, between May 12, 2026 and July 1, 2026, 23:59 UTC. No such ruling was issued.

EVIDENCE FROM SPECIFIED RESOLUTION SOURCES:

1) Constitutional Court of Korea official website (ccourt.go.kr):
- The English "Latest Decisions" page (https://english.ccourt.go.kr/site/eng/ex/bbs/List.do?cbIdx=1143), checked as of July 1, 2026, lists the most recent decision as case 2023Hun-Ka14 dated March 26, 2026. There is NO decision on Yoon's insurrection tribunal law petition (case 2026Hun-Ma995) anywhere in the list [Latest Decisions - Constitutional Court of Korea](https://english.ccourt.go.kr/site/eng/ex/bbs/List.do?cbIdx=1143).
- The Korean recent-rulings page (https://www.ccourt.go.kr/site/kor/ex/bbs/List.do?cbIdx=1195) shows the June 24, 2026 hand-down date covered only unrelated cases: an Income Tax Act case (2024헌바83 등), a Public Official Election Act case (2021헌바292), a Criminal Procedure Act case (2021헌바145 등), and a child-sexual-abuse protection case (2022헌가8). None concerns the insurrection tribunal law (2026헌마995) [헌법재판소 < 선고·변론사건 < 선고사건 < 최근 주요결정](https://www.ccourt.go.kr/site/kor/ex/bbs/List.do?cbIdx=1195).

2) Yonhap News Agency (en.yna.co.kr):
- A Yonhap English search for a Constitutional Court ruling on the insurrection tribunal law returned no article reporting any such merits decision [https://en.yna.co.kr/search/index?query=insurrection%20tribunal%20law%20constitutional%20court](https://en.yna.co.kr/search/index?query=insurrection%20tribunal%20law%20constitutional%20court). Yonhap's coverage confirms the petition (2026헌마995) was only "referred to formal review" by the full nine-member bench on April 21, 2026 (https://en.yna.co.kr/view/AEN20260422006400315), a procedural referral, not a final judgment.

DISTINGUISHING FROM OTHER YOON-RELATED RULINGS (per checklist):
- The impeachment ruling (removing Yoon from office) occurred April 4, 2025 — long before the window and a different proceeding.
- Yoon's Feb 19, 2026 insurrection conviction/life sentence and his ongoing appeal are ordinary criminal proceedings, not Constitutional Court rulings on the tribunal law.
- The only decision within the window touching the tribunal law's constitutionality was on June 23, 2026, when the SEOUL HIGH COURT (서울고법 형사12-1부, case 2026초기304) partially dismissed and partially rejected (일부 각하·일부 기각) Yoon's motion requesting that the ordinary court refer the law to the Constitutional Court. This is a lower court's refusal to refer — NOT a Constitutional Court judgment on the merits — and thus expressly excluded by the resolution criteria.
- An earlier People Power Party petition (2026헌마134) was dismissed (각하) on Feb 24, 2026, which is both before the window and a procedural (non-merits) dismissal.
- Kim Yong-hyun's separate petition on the same law was only referred to formal review on June 4, 2026 — still pending, no merits ruling.

Because no full-bench final decision on the constitutionality of the insurrection tribunal law was issued in the May 12 – July 1, 2026 window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-103. `f49fa93e-49b7-5f11-9136-ab28b9160e33`

- Present date: `2026-05-29 06:49:59.423532`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Javier Milei visit the United Kingdom by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), Javier Milei—in his capacity as President of Argentina—is physically present on the soil of the United Kingdom (defined as England, Scotland, Wales, and Northern Ireland; excluding British Overseas Territories such as the Falkland Islands, Gibraltar, etc.) for any purpose, including but not limited to official state visits, working visits, private meetings, or transit stops involving disembarkation.

The question resolves **No** if no such visit occurs within the specified window.

A visit that was previously scheduled but cancelled, or a visit where Milei does not physically arrive in the UK (e.g., a virtual meeting), does not count.

**Resolution source:** Credible major news reporting from outlets such as [Reuters](https://www.reuters.com), [BBC](https://www.bbc.co.uk), [AP News](https://apnews.com), or the official UK government website ([gov.uk](https://www.gov.uk)). The Wikipedia page tracking Milei's international trips (https://en.wikipedia.org/wiki/List_of_international_presidential_trips_made_by_Javier_Milei) may also be consulted as a secondary source.

**Pre-cutoff background**

Argentine President Javier Milei has publicly expressed his intention to visit the United Kingdom in 2026, which would make him the first Argentine president to do so since Carlos Menem's visit in 1998. The visit was initially reported by The Telegraph in December 2025 and confirmed by Argentine officials, with an expected timeframe of April or May 2026. The trip's agenda centers on diplomatic engagement, including meetings with UK Prime Minister Keir Starmer and Reform UK leader Nigel Farage, as well as negotiations over the UK's arms embargo on Argentina stemming from the 1982 Falklands War.

As of late April 2026, the visit has not yet taken place. According to the Wikipedia page tracking Milei's international presidential trips (last updated April 24, 2026), the UK visit remains listed with a "TBD" date, with Argentine Foreign Ministry officials confirming in April 2026 that Milei intends to visit following his trip to Israel [https://en.wikipedia.org/wiki/List_of_international_presidential_trips_made_by_Javier_Milei](https://en.wikipedia.org/wiki/List_of_international_presidential_trips_made_by_Javier_Milei). The diplomatic context is complex: Milei has recently sharpened rhetoric on Argentina's claim to the Falkland Islands (Malvinas), while also pursuing warmer economic ties with London. US-UK tensions under the Trump administration have added a further layer of uncertainty, potentially giving Milei leverage but also complicating the diplomatic calculus. Milei's approval ratings have been declining domestically, which may influence the timing and political calculations around the visit.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if Javier Milei, in his capacity as President of Argentina, was physically present on UK soil (England, Scotland, Wales, or Northern Ireland) between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC). The evidence shows this did not happen.

KEY EVIDENCE:
1. The authoritative tracking source cited in the resolution criteria — the Wikipedia "List of international presidential trips made by Javier Milei" — was last updated June 24, 2026 and STILL lists the United Kingdom visit only as a "Scheduled trip" with status "TBD" (To Be Determined). There is NO completed UK trip anywhere in the list; the 2026 completed-trips list runs through a Los Angeles trip on May 6, 2026, with no UK entry in the May 12–July 1 window [https://en.wikipedia.org/wiki/List_of_international_presidential_trips_made_by_Javier_Milei](https://en.wikipedia.org/wiki/List_of_international_presidential_trips_made_by_Javier_Milei). If a historic first Argentine presidential visit to the UK since 1998 had actually occurred, Wikipedia's trip tracker would have recorded it as a completed trip.

2. All news reporting throughout 2026 treats the UK trip as still merely planned/aspirational and repeatedly slipping. The trip was originally floated for April/May 2026 (Reuters, Dec 29 2025: https://www.reuters.com/world/americas/argentinas-milei-visit-uk-this-year-2025-12-29/), but Argentine reporting (e.g., Clarín) noted the government believed it would not make that date, and by April 2026 officials said Milei "wants to" visit after a trip to Israel. No Reuters/BBC/AP/gov.uk report exists of Milei actually arriving in or disembarking in the UK.

3. Milei's confirmed late-June/early-July 2026 agenda did NOT include the UK. La Nación (https://www.lanacion.com.ar/politica/milei-volvera-a-ir-a-eeuu-para-los-festejos-de-la-independencia...) reported his schedule for the end of the resolution window: he was in Asunción, Paraguay on June 30, 2026, then traveled to the United States for July 4 independence celebrations and the Sun Valley conference in Idaho — with no UK stop. This confirms no UK visit occurred in the final days before July 1.

CHECKLIST COMPLIANCE:
- Window: No visit occurred at any point between May 12 and July 1, 2026 (visit remained "TBD"/unrealized) [https://en.wikipedia.org/wiki/List_of_international_presidential_trips_made_by_Javier_Milei](https://en.wikipedia.org/wiki/List_of_international_presidential_trips_made_by_Javier_Milei).
- Location: Since no visit to England/Scotland/Wales/Northern Ireland occurred, the exclusion of British Overseas Territories (Falklands, Gibraltar) is moot — no qualifying UK-soil visit took place.
- Credible source URLs: Wikipedia tracker (per resolution criteria) [https://en.wikipedia.org/wiki/List_of_international_presidential_trips_made_by_Javier_Milei](https://en.wikipedia.org/wiki/List_of_international_presidential_trips_made_by_Javier_Milei); Reuters planning report (https://www.reuters.com/world/americas/argentinas-milei-visit-uk-this-year-2025-12-29/).
- Physical presence: Milei was never physically present on UK soil and did not disembark in the UK during the window; the trip stayed in the planning stage.
- Capacity: The prospective visit was always framed as Milei acting in his capacity as President of Argentina (official/working visit re: Falklands arms embargo and meetings with PM Starmer/Farage), but this is moot because the visit did not occur.

Because no qualifying visit took place within the May 12 – July 1, 2026 window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-104. `fbf697ca-8cc1-5da1-9d74-34cd3eeaba91`

- Present date: `2026-05-29 07:25:33.567907`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Senate Agriculture Committee report a Farm Bill out of committee with bipartisan support (at least 3 Democratic votes) by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if ALL of the following conditions are met:

1. **The Senate Committee on Agriculture, Nutrition, and Forestry holds a formal vote to report a Farm Bill out of committee.** The bill in question is the Senate's legislative vehicle for reauthorizing farm, nutrition, conservation, and related programs — commonly referred to as the "Farm Bill." This includes any bill or substitute amendment serving as the Senate's Farm Bill, regardless of its specific title or number. Per the [Senate Glossary on Congress.gov](https://www.congress.gov/help/legislative-glossary#glossary_reportedlegislation), "reported" means the committee has voted to recommend the bill favorably (or without recommendation) to the full Senate.

2. **The committee vote occurs on or after May 12, 2026, and no later than 11:59 PM Eastern Time on June 30, 2026.**

3. **At least 3 members of the Democratic caucus on the committee vote in favor** of the motion to report the bill. "Bipartisan support" is operationally defined as receiving affirmative votes from at least 3 of the 11 Democratic members currently serving on the committee [Committee Membership](https://www.agriculture.senate.gov/about/membership). Independent senators caucusing with Democrats count as Democrats for this purpose.

The question resolves **No** if:
- No Farm Bill is reported out of committee by 11:59 PM ET on June 30, 2026, OR
- A Farm Bill is reported out of committee but receives fewer than 3 affirmative votes from Democratic caucus members.

**Resolution source:** The official committee vote tally as published on the [Senate Agriculture Committee website](https://www.agriculture.senate.gov/) or on [Congress.gov](https://www.congress.gov/). If neither source publishes a detailed vote breakdown, credible reporting from major news outlets (e.g., Reuters, AP, Politico, or the Farm Policy News at https://farmpolicynews.illinois.edu/) identifying the vote count by party will suffice.

**Pre-cutoff background**

The U.S. House of Representatives passed its version of the Farm Bill — the Farm, Food, and National Security Act of 2026 — on April 30, 2026, by a vote of 224-200 [Senate Targeting Late May, Early June for Farm Bill Markup](https://farmpolicynews.illinois.edu/2026/05/senate-targeting-late-may-early-june-for-farm-bill-markup/). Attention has now shifted to the Senate, where Agriculture Committee Chair John Boozman (R-Ark.) is targeting a committee markup for late May or early June 2026 [Senate Targeting Late May, Early June for Farm Bill Markup](https://farmpolicynews.illinois.edu/2026/05/senate-targeting-late-may-early-june-for-farm-bill-markup/). The Senate is scheduled to be in recess from May 23 to June 1, 2026, narrowing the available window [Senate Targeting Late May, Early June for Farm Bill Markup](https://farmpolicynews.illinois.edu/2026/05/senate-targeting-late-may-early-june-for-farm-bill-markup/).

Because the Senate requires 60 votes to overcome a filibuster, bipartisan support is essential for any Farm Bill to pass the full chamber. Chair Boozman has indicated he is working with Ranking Member Amy Klobuchar (D-Minn.) to develop a bipartisan product [Senate Targeting Late May, Early June for Farm Bill Markup](https://farmpolicynews.illinois.edu/2026/05/senate-targeting-late-may-early-june-for-farm-bill-markup/). However, significant policy disagreements remain. On May 1, 2026, all Democratic members of the Senate Agriculture Committee released a joint statement outlining conditions for their support, including delaying new SNAP cost shifts enacted by a Republican budget bill that shifted program costs to states with error rates above 6% [Senate Ag Dems Statement on House Farm Bill Passage](https://www.agriculture.senate.gov/newsroom/dem/press/release/senate-ag-dems-statement-on-house-farm-bill-passage). Debates over pesticide regulations and food assistance levels also remain contentious [Senate Targeting Late May, Early June for Farm Bill Markup](https://farmpolicynews.illinois.edu/2026/05/senate-targeting-late-may-early-june-for-farm-bill-markup/).

The Senate Committee on Agriculture, Nutrition, and Forestry currently has 11 Democratic members: Amy Klobuchar (Ranking Member), Michael Bennet, Tina Smith, Richard Durbin, Cory Booker, Ben Ray Luján, Raphael Warnock, Peter Welch, John Fetterman, Adam Schiff, and Elissa Slotkin [Committee Membership](https://www.agriculture.senate.gov/about/membership).

**Exact later resolution packet**

The question resolves NO. It required that the Senate Committee on Agriculture, Nutrition, and Forestry hold a formal vote to REPORT a Farm Bill out of committee (with at least 3 Democratic caucus votes) on or after May 12, 2026 and no later than 11:59 PM ET on June 30, 2026. No such report vote occurred within the window.

Evidence:
- The Senate Agriculture Committee only released the TEXT of its version of the 2026 Farm Bill (the "Agricultural Act of 2026," a.k.a. "Farm Bill 2.0") on June 23, 2026 — this was a discussion draft, not a reported bill. The committee was "expecting to mark up the bill in July." Source: National Association of Counties (NACo), published June 24, 2026 [Senate Agriculture Committee introduces 2026 Farm Bill, following ...](https://www.naco.org/news/senate-agriculture-committee-introduces-2026-farm-bill-following-house-passage). URL: https://www.naco.org/news/senate-agriculture-committee-introduces-2026-farm-bill-following-house-passage
- Holland & Knight (published June 26, 2026) confirms Chair John Boozman "indicated the Committee will move to mark up the draft after the Senate returns in mid-July from recess," and refers to the committee possibly moving the legislation "this July." Source [Senate Agriculture Committee Releases Draft Text for 2026 Farm Bill](https://www.hklaw.com/en/insights/publications/2026/06/senate-agriculture-committee-releases-draft-text-for-2026-farm-bill). URL: https://www.hklaw.com/en/insights/publications/2026/06/senate-agriculture-committee-releases-draft-text-for-2026-farm-bill
- Farm Aid (June 24, 2026) states Boozman "has committed to 'marking up' ... the farm bill draft over the summer" and that the path to passage "remains extremely unclear." Source [The Latest Updates on the Farm Bill - Farm Aid](https://www.farmaid.org/issues/farm-policy/the-latest-updates-on-the-2025-farm-bill/). URL: https://www.farmaid.org/issues/farm-policy/the-latest-updates-on-the-2025-farm-bill/
- Corroborating search results: E&E News ("Boozman is hoping to refine the legislation and hold a markup before the scheduled August recess"), Agriculture.com ("Markup Likely After July Fourth"), Valley Ag Voice ("Senate markup will not be held before the July 4 recess"), and the National Organic Coalition ("tentatively scheduled a Farm Bill markup for July/August"). The Congress.gov CRS product R48918 states "The Senate Committee on Agriculture, Nutrition, and Forestry has not marked up a farm bill during the 119th Congress."

Because a markup had not even occurred by June 30, 2026 — let alone a formal vote to report the bill favorably (or without recommendation) to the full Senate — condition #1 (a formal report vote) and condition #2 (timing by 11:59 PM ET June 30, 2026) of the resolution criteria were not satisfied. Consequently, condition #3 (at least 3 Democratic caucus votes to report) is moot. Per the resolution criteria, the question resolves NO because "No Farm Bill is reported out of committee by 11:59 PM ET on June 30, 2026."

Note: The only committee "markup" of a Farm Bill in this Congress within any comparable timeframe was the HOUSE Agriculture Committee's markup of H.R. 7567 (the Farm, Food, and National Security Act of 2026) on March 3, 2026 — which is (a) the wrong chamber and (b) outside the May 12–June 30 window — so it does not satisfy the criteria either.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-105. `27bc0270-92bb-582a-b072-4d726c2d3bdb`

- Present date: `2026-05-01 13:22:33.224644`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the European Commission authorize EU-wide type approval for Tesla's Full Self-Driving (Supervised) system by June 1, 2026?

**Resolution criteria**

This question resolves YES if, by 23:59 UTC on June 1, 2026, the European Commission has formally authorized an implementing act permitting the Netherlands (RDW) to grant EU-wide type approval for Tesla's Full Self-Driving (Supervised) system, as confirmed by an official European Commission announcement or credible reporting from major news outlets (e.g., Reuters at https://www.reuters.com, AP at https://apnews.com, or the RDW news page at https://www.rdw.nl/en/news/2026).

This question resolves NO if no such implementing act has been authorized by 23:59 UTC on June 1, 2026. Individual EU member states independently authorizing the technology based on the Dutch national approval does NOT count toward YES resolution — only a formal EU-wide implementing act qualifies.

**Pre-cutoff background**

On April 10, 2026, the Dutch vehicle authority RDW (Rijksdienst voor het Wegverkeer, https://www.rdw.nl/en) granted national type approval for Tesla's Full Self-Driving (Supervised) system under UN Regulation R-171, making the Netherlands the first European country to approve the technology [RDW explanation of European type approval Tesla with provisional ...](https://www.rdw.nl/en/news/2026/rdw-explanation-of-european-type-approval-tesla-with-provisional-validity-in-the-netherlands). However, this approval is currently valid only in the Netherlands [RDW explanation of European type approval Tesla with provisional ...](https://www.rdw.nl/en/news/2026/rdw-explanation-of-european-type-approval-tesla-with-provisional-validity-in-the-netherlands).

For EU-wide validity, the RDW must submit an application to the European Commission, which requires a majority vote from EU member states in the responsible technical committee [RDW explanation of European type approval Tesla with provisional ...](https://www.rdw.nl/en/news/2026/rdw-explanation-of-european-type-approval-tesla-with-provisional-validity-in-the-netherlands). On April 13, 2026, the RDW notified the European Commission of its plan to seek EU-wide approval [Dutch regulator to seek EU approval for Tesla's self-driving software](https://www.reuters.com/business/dutch-regulator-notifies-european-commission-plan-seek-eu-approval-teslas-fsd-2026-04-13/). The Netherlands is scheduled to present its case to the relevant EU technical committee in May 2026 [Dutch regulator to seek EU approval for Tesla's self-driving software](https://www.reuters.com/business/dutch-regulator-notifies-european-commission-plan-seek-eu-approval-teslas-fsd-2026-04-13/). If the committee votes favorably, the European Commission must then prepare an implementing act authorizing the Netherlands to grant EU type approval [Dutch regulator to seek EU approval for Tesla's self-driving software](https://www.reuters.com/business/dutch-regulator-notifies-european-commission-plan-seek-eu-approval-teslas-fsd-2026-04-13/).

In the interim, individual EU countries may independently authorize the technology using the Dutch approval as a reference point [Dutch regulator to seek EU approval for Tesla's self-driving software](https://www.reuters.com/business/dutch-regulator-notifies-european-commission-plan-seek-eu-approval-teslas-fsd-2026-04-13/).

Tesla's "Full Self-Driving (Supervised)" (FSD Supervised) is an advanced driver-assistance system that requires an attentive human driver at all times (see https://www.tesla.com/support/full-self-driving). "Regulatory approval" here refers to the European Commission formally authorizing an implementing act granting EU-wide type approval, distinct from the already-completed Dutch national approval.

The original question about Dutch RDW national approval has already resolved — the RDW granted approval on April 10, 2026, after delays from the initially expected dates of February 2026, then March 20, then April 10 [RDW explanation of European type approval Tesla with provisional ...](https://www.rdw.nl/en/news/2026/rdw-explanation-of-european-type-approval-tesla-with-provisional-validity-in-the-netherlands). This question therefore focuses on the next critical milestone: EU-wide authorization.

**Exact later resolution packet**

The question resolves NO. It asked whether the European Commission would formally authorize an implementing act permitting the Netherlands (RDW) to grant EU-wide type approval for Tesla's Full Self-Driving (Supervised) system by 23:59 UTC on June 1, 2026.

Distinction between the two milestones:
- The Dutch NATIONAL approval was granted by RDW on April 10, 2026, under Article 39 of Regulation (EU) 2018/858 / UN Regulation R-171, valid only within the Netherlands (the provisional/national approval) [ec01bd, dbeff8].
- The EU-WIDE authorization (the subject of this question) requires the European Commission to adopt an implementing act, which in turn requires a favorable vote in the Technical Committee on Motor Vehicles (TCMV) [ec01bd, dbeff8].

Evidence that no EU-wide implementing act was authorized by the deadline:
- Reuters (May 5, 2026) reported the process was in early stages: RDW was scheduled only to PRESENT to the TCMV in May 2026, with NO vote expected; the earliest a vote could realistically occur would be July 2026, with possible delays to after summer or October 2026 [49c020]. https://www.reuters.com/business/finance/teslas-road-full-self-driving-approval-europe-2026-05-05/
- electrive.com (May 6, 2026) confirmed the TCMV met in Brussels but held NO vote — RDW's presentation was extended to 60 minutes, and national authorities were to review the information before any future vote [dbeff8]. https://www.electrive.com/2026/05/06/eu-approval-for-tesla-fsd-remains-uncertain/
- ETSC (updated through late May 2026) confirmed the EU-wide process was still in the advocacy/deliberation phase, with ETSC lobbying the Commission to pause before any vote; no implementing act had been adopted [ec01bd]. https://etsc.eu/tesla-approval-pushes-europe-towards-a-road-safety-cliff-edge/
- Reuters/Yahoo reporting noted "There is no vote scheduled on FSD this week. The next committee meetings are expected in July and October."

The resolution criteria explicitly state that individual EU member states independently authorizing the technology based on the Dutch national approval (e.g., Lithuania and Estonia, which approved by late May 2026 [ec01bd]) does NOT count toward YES — only a formal EU-wide implementing act qualifies. No such implementing act was authorized by the European Commission before the June 1, 2026 deadline. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-106. `9f134ccc-d404-5b35-826c-20fc95341106`

- Present date: `2026-05-02 10:22:09.811931`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Harvard University and HGSU-UAW reach a tentative contract agreement between April 30, 2026, and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if Harvard University and the Harvard Graduate Students Union-United Auto Workers (HGSU-UAW) reach a **tentative contract agreement** between April 30, 2026, and June 1, 2026 (11:59 PM UTC).

A **tentative contract agreement** is defined as a formal agreement on overall contract terms reached by the bargaining committees of both Harvard University and HGSU-UAW, which is then presented to the union membership for ratification. It does not require that ratification has occurred — only that both bargaining teams have agreed to recommend the contract to their respective principals.

The question resolves **No** if no such tentative agreement is publicly announced by 11:59 PM UTC on June 1, 2026.

**Resolution sources:** Official announcements from [HGSU-UAW](https://harvardgradunion.org/) or [Harvard University's academic unionization page](https://academicunionization.harvard.edu/), or credible reporting from [The Harvard Crimson](https://www.thecrimson.com/).

**Pre-cutoff background**

The Harvard Graduate Students Union-United Auto Workers ([HGSU-UAW](https://harvardgradunion.org/)) has been bargaining with [Harvard University](https://www.harvard.edu/) for a new contract since February 2025. After 14 months of negotiations failed to produce an agreement, the union launched an indefinite strike on April 21, 2026, with 95.8% strike authorization support [https://www.thecrimson.com/thread/2026/4/21/hgsu-strike-2026/](https://www.thecrimson.com/thread/2026/4/21/hgsu-strike-2026/).

Key unresolved issues include wages, protections for international/noncitizen student workers, and whether harassment and discrimination cases should be subject to independent third-party arbitration [https://www.thecrimson.com/thread/2026/4/21/hgsu-strike-2026/](https://www.thecrimson.com/thread/2026/4/21/hgsu-strike-2026/).

On April 28, 2026, Harvard presented an updated proposal offering an 11% wage increase over four years, fully subsidized preventive dental insurance for Ph.D. students, a new parental benefit stipend of at least $6,500, expanded emergency funds for international students, and access to a subsidized legal services plan including immigration-related services [Harvard Raises Wage Offer, Expands Benefits as Grad ...](https://www.thecrimson.com/article/2026/4/29/harvard-offers-benefits-strike-bargaining/). Despite this movement, several central union demands remain unresolved.

As of April 30, 2026, the strike is ongoing. Both parties have agreed to additional bargaining sessions scheduled for May 14, May 29, June 9, and June 23, 2026 [https://www.thecrimson.com/thread/2026/4/21/hgsu-strike-2026/](https://www.thecrimson.com/thread/2026/4/21/hgsu-strike-2026/) [Harvard Raises Wage Offer, Expands Benefits as Grad ...](https://www.thecrimson.com/article/2026/4/29/harvard-offers-benefits-strike-bargaining/). The fact that sessions extend through late June suggests both sides anticipate potentially prolonged negotiations, though strike pressure could accelerate a deal.

**Exact later resolution packet**

The question resolves NO because Harvard University and HGSU-UAW did NOT reach a tentative contract agreement between April 30, 2026 and June 1, 2026 (11:59 PM UTC).

Evidence from authorized resolution sources:

1. Harvard Magazine reported that the union ended its strike on Monday, June 1, 2026, WITHOUT a contract. The article explicitly states "a contract has not been agreed upon" and that union leaders said they would continue to negotiate until a new contract is reached, with additional bargaining sessions scheduled for June 9 and 23 [Graduate Student Workers End Strike | Harvard Magazine](https://www.harvardmagazine.com/university-news/harvard-graduate-student-workers-end-strike). (Note: Harvard Magazine is a supplementary corroborating source; the union's own bargaining updates page is an authorized source.)

2. The HGSU-UAW official bargaining updates page (https://harvardgradunion.org/bargaining-updates/), an authorized resolution source, showed the most recent update dated May 29, 2026 describing ongoing, unresolved negotiations with the bargaining committee agreeing to continue at a future session scheduled for June 9, 2026 — with NO announcement of a tentative agreement during the April 30–June 1 window [2026 Bargaining Updates – Harvard Graduate Student Union](https://harvardgradunion.org/bargaining-updates/).

Both sources confirm the strike ended (after 40 days, becoming the longest in the union's history) without any tentative contract agreement being reached during the resolution window. The bargaining sessions extending into June (June 9, June 23) further confirm negotiations remained unresolved past the June 1 deadline. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-107. `1fb9b683-64a4-5c17-8ab3-ff891d17af08`

- Present date: `2026-05-01 13:03:17.830063`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Super Heavy booster on Starship Flight 12 be successfully caught by the launch tower arms during the mission?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 (all times UTC), the Super Heavy booster from Starship Flight 12 is successfully caught by the launch tower's mechanical arms ("chopsticks") at the landing site. "Successfully caught" is defined as the booster being held by the mechanical arms without the booster touching the ground, ocean, or any surface other than the arms themselves, and remaining stably supported by the arms for at least 30 seconds after engine shutdown, as confirmed by the official SpaceX webcast or official SpaceX communications (X/Twitter account @SpaceX, or spacex.com/updates).

This question resolves **No** if:
- Flight 12 launches but the booster is diverted to the ocean, performs a splashdown, or is otherwise not caught by the tower arms;
- Flight 12 launches but the catch attempt fails (e.g., booster contacts the ground or is dropped);
- Flight 12 does not launch by June 1, 2026, 23:59 UTC.

Primary resolution sources:
- SpaceX official YouTube channel: https://www.youtube.com/@SpaceX
- SpaceX updates page: https://www.spacex.com/updates

**Pre-cutoff background**

SpaceX's Starship program has been iterating on its Super Heavy booster recovery capability. As of May 1, 2026, SpaceX has attempted to catch the Super Heavy booster using the launch tower's mechanical arms ("chopsticks") on 7 flights (Flights 5–11), with 3 successful catches (Flights 5, 7, and 8) — a success rate of approximately 43%. Flights 6, 9, 10, and 11 resulted in ocean diversions, failures, or controlled splashdowns [List of Starship launches - Wikipedia](https://en.wikipedia.org/wiki/List_of_Starship_launches).

Flight 12 is scheduled for May 2026 and represents two major firsts: the first launch from Starbase's Orbital Launch Pad 2 (OLP-2) and the first flight of Block 3 hardware (Booster B19, Ship S39) [List of Starship launches - Wikipedia](https://en.wikipedia.org/wiki/List_of_Starship_launches). The combination of a new launch pad and an entirely new vehicle version introduces significant uncertainty about whether SpaceX will attempt a tower catch or opt for an ocean splashdown. Previous catches were all performed at OLP-1 with Block 1/2 hardware.

SpaceX livestreams all Starship flights on its official YouTube channel (https://www.youtube.com/@SpaceX) and posts mission updates on its website (https://www.spacex.com/updates).

**Exact later resolution packet**

The question asks whether the Super Heavy booster on Starship Flight 12 was successfully caught by the launch tower arms (chopsticks). It resolves NO if the booster is diverted to the ocean, performs a splashdown, or is otherwise not caught.

Antecedent check (did Flight 12 launch by June 1, 2026, 23:59 UTC?): YES. The official SpaceX mission page states Starship lifted off from Starbase, Texas on its twelfth flight test on Friday, May 22, 2026 [a9d708]. This is corroborated by Wikipedia's List of Starship launches [f19d87]. So the question is not annulled and resolves on the consequent.

Consequent check (was the booster caught by the tower arms?): NO. The official SpaceX update for Starship's Twelfth Flight Test states the booster "attempted to reignite its engines for the landing burn before experiencing a hard splashdown in the Gulf of America," and that it "was unable to light all planned engines and performed a partial boostback burn that ended early" [a9d708]. The flight plan for the V3 booster never intended a tower catch—it called for a controlled splashdown in the Gulf of Mexico. Wikipedia independently confirms the booster landing outcome as "Failure (gulf)," noting that "during the landing sequence, only one engine relit, leading the vehicle to impact the water at high speed" [f19d87].

Since the booster was not caught by the mechanical arms (it instead hit the water), the "Successfully caught" condition (held by arms for at least 30 seconds after engine shutdown without touching any other surface) was not met. The question resolves NO.

Primary source URL: https://www.spacex.com/launches/starship-flight-12 [a9d708]
Corroborating: https://en.wikipedia.org/wiki/List_of_Starship_launches [f19d87]

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-108. `a51291e6-e7a6-551f-ae98-84c0fd9ba7ca`

- Present date: `2026-05-03 00:19:34.329209`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the IRS or Treasury Department publish formal guidance on Section 280E relief for state-licensed medical cannabis businesses between May 1, 2026 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the IRS or Treasury Department publishes formal guidance on or after May 1, 2026 (00:00 UTC) and on or before June 1, 2026 (23:59 UTC) that explicitly addresses the application of, or relief from, Section 280E of the Internal Revenue Code for state-licensed medical cannabis businesses following the DOJ rescheduling order.

**Definition of "formal guidance":** For purposes of this question, "formal guidance" means any of the following published guidance types as defined by the IRS (https://www.irs.gov/newsroom/understanding-irs-guidance-a-brief-primer): a Notice, Revenue Ruling, Revenue Procedure, Treasury Decision (final or temporary regulation), or Announcement [Understanding IRS guidance - A brief primer](https://www.irs.gov/newsroom/understanding-irs-guidance-a-brief-primer). Informal communications such as press releases, blog posts, FAQ pages, or oral statements do not qualify. The April 23, 2026 Treasury press release (https://home.treasury.gov/news/press-releases/sb0471) does not qualify and is explicitly excluded.

**Definition of "Section 280E relief":** Guidance that addresses whether and how Section 280E of the Internal Revenue Code (26 U.S.C. § 280E, https://www.law.cornell.edu/uscode/text/26/280E) ceases to apply, or applies differently, to state-licensed medical cannabis businesses as a result of cannabis rescheduling from Schedule I to Schedule III.

**Resolution source:** The guidance must appear on the IRS published guidance page (https://www.irs.gov/newsroom/irs-guidance) or in the Internal Revenue Bulletin (https://www.irs.gov/irb), or on the Treasury Department website (https://home.treasury.gov), or in the Federal Register (https://www.federalregister.gov/). If no qualifying guidance is published by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

On April 23, 2026, the U.S. Department of Justice issued a Final Order immediately rescheduling FDA-approved marijuana products and state-licensed medical cannabis from Schedule I to Schedule III of the Controlled Substances Act [Treasury, IRS Announce Process for Tax Guidance Following DOJ ...](https://home.treasury.gov/news/press-releases/sb0471). On the same date, the U.S. Department of the Treasury and the IRS announced they plan to issue guidance addressing the federal tax consequences of this rescheduling, specifically regarding Section 280E of the Internal Revenue Code (26 U.S.C. § 280E), which historically denied tax deductions and credits to businesses trafficking in Schedule I or II controlled substances [Treasury, IRS Announce Process for Tax Guidance Following DOJ ...](https://home.treasury.gov/news/press-releases/sb0471).

The Treasury/IRS announcement indicated the forthcoming guidance is expected to address two key areas: (1) how Section 280E applies to businesses with multiple activities, particularly the apportionment of expenses for activities that no longer involve Schedule I or II substances; and (2) a transition rule stating that rescheduling will generally be considered to apply for a business's full taxable year that includes the effective date of the Final Order [Treasury, IRS Announce Process for Tax Guidance Following DOJ ...](https://home.treasury.gov/news/press-releases/sb0471). However, no specific timeline for publishing this guidance was provided [Treasury, IRS Announce Process for Tax Guidance Following DOJ ...](https://home.treasury.gov/news/press-releases/sb0471).

As of May 1, 2026, no formal guidance has been published. The question is whether the IRS or Treasury can finalize and publish such guidance within approximately five weeks of the April 23 announcement. IRS guidance processes can vary significantly in speed—Notices can be issued relatively quickly, while Revenue Rulings and Regulations typically take longer [Understanding IRS guidance - A brief primer](https://www.irs.gov/newsroom/understanding-irs-guidance-a-brief-primer).

Section 280E (https://www.law.cornell.edu/uscode/text/26/280E) provides that no deduction or credit shall be allowed for amounts paid or incurred in carrying on a trade or business consisting of trafficking in controlled substances within the meaning of Schedule I and II of the Controlled Substances Act. With medical cannabis now rescheduled to Schedule III, Section 280E would generally no longer apply to state-licensed medical cannabis businesses, but formal IRS guidance is needed to clarify implementation details.

**Exact later resolution packet**

The question resolves NO. It asks whether the IRS or Treasury published formal guidance (a Notice, Revenue Ruling, Revenue Procedure, Treasury Decision, or Announcement) explicitly addressing Section 280E relief for state-licensed medical cannabis businesses between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC).

Key facts established:
- On April 23, 2026, Treasury and the IRS issued only a PRESS RELEASE announcing their *plan* to issue future guidance addressing Section 280E consequences of the DOJ rescheduling order. This press release (home.treasury.gov/news/press-releases/sb0471) is explicitly excluded by the question's resolution criteria and is dated before the resolution window [Treasury, IRS Announce Process for Tax Guidance Following DOJ ...](https://home.treasury.gov/news/press-releases/sb0471).
- As of April 27–28, 2026 (before the window opened), commentators confirmed only the announcement existed and no formal guidance had been published; practitioners were advised to monitor the Internal Revenue Bulletin for future publication [Cannabis Rescheduling: DOJ, Treasury, and DEA Updates Since ...](https://foleyhoag.com/news-and-insights/blogs/cannabis-and-the-law/2026/april/cannabis-rescheduling-doj-treasury-and-dea-updates-since-the-april-23-order/) [Is the Most Impactful Part of Marijuana Rescheduling an Obscure ...](https://www.jdsupra.com/legalnews/is-the-most-impactful-part-of-marijuana-9981895/).
- Decisively, on May 29, 2026 — just two days before the window closed — both Cannabis Business Times and Marijuana Moment reported that seven U.S. House Democrats sent a letter urging the IRS and Treasury to issue "prompt"/"swift and clear" tax guidance on Section 280E, expressly because no such guidance had yet been issued (roughly five weeks after the April 23 announcement) [7 House Democrats Demand IRS, Treasury Provide 280E ...](https://www.cannabisbusinesstimes.com/legislation-and-regulation/cannabis-tax-law/news/15826367/7-house-democrats-demand-irs-treasury-provide-280e-cannabis-guidance) [Lawmakers want cannabis tax guidance from IRS (Newsletter](https://www.marijuanamoment.net/lawmakers-want-cannabis-tax-guidance-from-irs-newsletter-may-29-2026/). Lawmakers actively demanding guidance days before the deadline confirms that no qualifying formal guidance (Notice, Rev. Rul., Rev. Proc., TD, or Announcement) was published on any of the specified sources (IRS guidance page, Internal Revenue Bulletin, Treasury website, or Federal Register) within the resolution window.

Since no qualifying formal guidance was published by 23:59 UTC on June 1, 2026, the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-109. `c4c1517d-6568-553b-ab8b-0295ab652ad4`

- Present date: `2026-05-03 02:05:48.893242`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Google face a public employee protest or open letter with 50+ signatories opposing its classified Pentagon AI deal between May 1, 2026, and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026, and by June 1, 2026 (11:59 PM UTC), **either** of the following occurs:

1. **Public Protest or Walkout:** A physical protest, walkout, or organized demonstration by Google employees that explicitly opposes Google's classified Pentagon AI deal (as reported in April–May 2026) takes place, OR

2. **Open Letter or Public Petition:** A publicly accessible open letter, petition, or statement opposing Google's classified Pentagon AI deal is published online and has at least 50 signatories who identify themselves as current Google employees.

**Key Definitions:**

- **"Google employee"** means a person currently employed by Google LLC or Alphabet Inc. on a full-time or part-time basis (W-2 employees). This excludes independent contractors, temporary workers, and vendor staff. For the open letter path, signatories must self-identify as current Google employees; verification relies on the credible news sources listed below confirming the claimed employment status of signatories (as was done during the 2018 Project Maven letter, per reporting by [The New York Times](https://www.nytimes.com/2018/04/04/technology/google-letter-ceo-pentagon-project.html)).

- **"Protest"** means a collective, organized public action (physical gathering, walkout, or coordinated digital demonstration such as a simultaneous public social media campaign with a shared hashtag and stated opposition) as defined in common usage (see [Merriam-Webster: protest](https://www.merriam-webster.com/dictionary/protest)).

- **"Open letter"** means a letter or petition addressed to Google leadership or the public, published on a publicly accessible platform (e.g., a website, blog, Google Doc, or news outlet), as defined in common usage (see [Merriam-Webster: open letter](https://www.merriam-webster.com/dictionary/open%20letter)).

- **"Classified Pentagon AI deal"** refers specifically to the agreement reported in April–May 2026 between Google and the U.S. Department of Defense to deploy Google's AI models on classified military networks [https://www.axios.com/2026/04/29/congress-military-ai-google-pentagon-deal](https://www.axios.com/2026/04/29/congress-military-ai-google-pentagon-deal)[https://www.usnews.com/news/top-news/articles/2026-05-01/pentagon-reaches-agreements-with-leading-ai-companies](https://www.usnews.com/news/top-news/articles/2026-05-01/pentagon-reaches-agreements-with-leading-ai-companies). The protest or letter must explicitly reference this deal, Google's military/defense AI work announced in this period, or the Pentagon classified AI contract. Unrelated employee protests (e.g., about layoffs, return-to-office policies) do not count.

- **50+ signatories:** The letter or petition must display at least 50 names of individuals identifying as current Google employees, verifiable via the letter itself or credible reporting confirming the count.

**Verification:**

The primary resolution source is the open letter or petition itself (if publicly accessible). If no primary source is available, the event must be reported by at least two of the following credible news organizations:
- [The New York Times](https://www.nytimes.com/)
- [Reuters](https://www.reuters.com/)
- [Associated Press](https://apnews.com/)
- [The Washington Post](https://www.washingtonpost.com/)
- [Axios](https://www.axios.com/)
- [The Verge](https://www.theverge.com/)
- [The Information](https://www.theinformation.com/)
- [Wired](https://www.wired.com/)

If neither a publicly accessible letter/petition nor reporting from at least two of the above outlets confirms the event by June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

On April 29–May 1, 2026, multiple outlets reported that Google signed an agreement with the U.S. Department of Defense to deploy its Gemini AI model on classified and top-secret military networks [https://www.axios.com/2026/04/29/congress-military-ai-google-pentagon-deal](https://www.axios.com/2026/04/29/congress-military-ai-google-pentagon-deal)[https://www.usnews.com/news/top-news/articles/2026-05-01/pentagon-reaches-agreements-with-leading-ai-companies](https://www.usnews.com/news/top-news/articles/2026-05-01/pentagon-reaches-agreements-with-leading-ai-companies). The deal is part of a broader Pentagon initiative involving seven companies (Google, SpaceX, OpenAI, NVIDIA, Reflection, Microsoft, and Amazon Web Services) [https://www.usnews.com/news/top-news/articles/2026-05-01/pentagon-reaches-agreements-with-leading-ai-companies](https://www.usnews.com/news/top-news/articles/2026-05-01/pentagon-reaches-agreements-with-leading-ai-companies). Google's contract is described as "more permissive" than OpenAI's: while OpenAI retains "full discretion" over its safety mechanisms, Google has agreed to adjust its safety settings at the government's request [https://www.axios.com/2026/04/29/congress-military-ai-google-pentagon-deal](https://www.axios.com/2026/04/29/congress-military-ai-google-pentagon-deal).

There is already documented internal opposition. DeepMind research scientist Alex Turner publicly criticized the deal on X (formerly Twitter), stating that Google "can't veto usage" and is relying on "aspirational language with no legal restrictions" [https://www.axios.com/2026/04/29/congress-military-ai-google-pentagon-deal](https://www.axios.com/2026/04/29/congress-military-ai-google-pentagon-deal). The Axios report notes the deal was struck "amid employee opposition" [https://www.axios.com/2026/04/29/congress-military-ai-google-pentagon-deal](https://www.axios.com/2026/04/29/congress-military-ai-google-pentagon-deal).

This echoes Google's 2018 Project Maven controversy, when thousands of employees signed an open letter and some resigned over Google's military AI work, ultimately leading the company to withdraw from the contract. Google's internal culture has shifted since then—the company has conducted layoffs and tightened its stance on employee activism—making it uncertain whether similar collective action will materialize this time.

The Pentagon also excluded Anthropic from the initiative, labeling it a "supply-chain risk" in March 2026 [https://www.usnews.com/news/top-news/articles/2026-05-01/pentagon-reaches-agreements-with-leading-ai-companies](https://www.usnews.com/news/top-news/articles/2026-05-01/pentagon-reaches-agreements-with-leading-ai-companies).

**Exact later resolution packet**

Adjudicated: The only 50+ signatory open letter (600+, later ~1,000 signatures) opposing the deal was published/sent April 27, 2026 — before the May 1–June 1 window, and the criteria require the qualifying event to 'occur' on or after May 1. The within-window DeepMind UK union recognition vote (~May 4–5) does not satisfy the criteria's 'Protest' definition (physical gathering, walkout, or coordinated digital demonstration) and involves UK rather than US W-2 employees, and reported in-person protests/research strikes were described only as planned campaign strategy, not as actual events occurring in the window. Under the instruction to read the criteria extremely literally, no qualifying open letter or protest occurred within May 1–June 1, 2026.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-110. `14b34551-7149-50ad-8da2-8dc59ca988fc`

- Present date: `2026-05-03 10:24:56.516187`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Meta launch the Ray-Ban Meta Scriber or Blazer (Gen 3) smart glasses for public purchase by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 2, 2026 (00:00 UTC) and by June 1, 2026 (23:59 UTC), either the "Ray-Ban Meta Scriber" (RW7001) or the "Ray-Ban Meta Blazer" (RW7002) — or any other Ray-Ban Meta smart glasses explicitly marketed as a third-generation or "Gen 3" model — becomes available for purchase by the general public.

A "launch" is defined as the product being listed for sale and orderable by consumers on either the official Meta Store (https://www.meta.com/smart-glasses/) or the official Ray-Ban website (https://www.ray-ban.com/).

"Gen 3" is defined as a new hardware generation distinct from the existing Ray-Ban Meta Gen 2 platform (released October 2023) and its variants, including the prescription models launched March 31, 2026, and the Ray-Ban Meta Display. The key distinguishing factor is a new model number series (e.g., RW7001/RW7002 vs. existing RW4xxx series) or explicit "Gen 3" / "third generation" marketing by Meta.

The question resolves **No** if no such product is available for purchase by 23:59 UTC on June 1, 2026. An announcement or pre-order without actual availability for purchase does not count.

**Resolution sources:** The official Meta Store product page (https://www.meta.com/smart-glasses/) and the Meta Newsroom (https://about.fb.com/news/). Credible reporting from outlets such as TechCrunch, The Verge, or Road to VR may be used as supplementary sources.

**Pre-cutoff background**

Meta and EssilorLuxottica have released two generations of Ray-Ban smart glasses. On March 31, 2026, Meta launched new Ray-Ban Meta models designed for prescription wearers, starting at $499 [Meta Slated to Launch Two New Ray-Ban Smart Glasses, According ...](https://www.roadtovr.com/meta-ray-ban-smart-glasses-2026-next-gen/). Separately, in March 2026, FCC filings surfaced for two new production-ready models: the "Ray-Ban Meta Scriber" (model RW7001) and the "Ray-Ban Meta Blazer" (model RW7002) [Meta Slated to Launch Two New Ray-Ban Smart Glasses, According ...](https://www.roadtovr.com/meta-ray-ban-smart-glasses-2026-next-gen/). These are described as "production units" rather than prototypes, which historically indicates an imminent launch. Previous generations of Ray-Ban Meta smart glasses were typically released within about one month of their FCC filings [Meta Preps Third-Gen Ray-Ban AI Glasses Launch | The Tech Buzz](https://www.techbuzz.ai/articles/meta-preps-third-gen-ray-ban-ai-glasses-launch). Some reports suggest an announcement could occur in April or early May 2026 based on this cadence [Meta Preps Third-Gen Ray-Ban AI Glasses Launch | The Tech Buzz](https://www.techbuzz.ai/articles/meta-preps-third-gen-ray-ban-ai-glasses-launch). However, there is uncertainty: Meta Connect 2026 is expected around September 2026, and some community sources suggest Gen 3 may not arrive until 2027. The prescription variants launched on March 31, 2026, are not considered Gen 3 — they are new frame styles for the existing Gen 2 platform. The Scriber and Blazer FCC filings represent a new hardware generation with distinct model numbers (RW7001/RW7002) compared to existing Gen 2 models.

**Exact later resolution packet**

The question resolves NO.

Background: The question (created 2026-05-03) was premised on the assumption that the FCC-filed "Ray-Ban Meta Scriber" (RW7001) and "Ray-Ban Meta Blazer" (RW7002) represented a NEW Gen 3 hardware generation, distinct from the Gen 2 platform and its prescription variants. The resolution criteria explicitly define "Gen 3" as "a new hardware generation distinct from the existing Ray-Ban Meta Gen 2 platform (released October 2023) and its variants, including the prescription models launched March 31, 2026." It requires that a qualifying Gen 3 product become available for purchase between May 2, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC).

Key finding — the RW7001/RW7002 models are actually Gen 2 prescription variants, not Gen 3:
- The official Ray-Ban store lists these very model numbers explicitly as Gen 2: product pages titled "RAY-BAN META BLAYZER OPTICS - GEN 2" (model RW7001, https://www.ray-ban.com/usa/electronics/RW7001...) and "RAY-BAN META SCRIBER OPTICS - GEN 2" (model RW7002, https://www.ray-ban.com/usa/electronics/RW7002...), both labeled "OPTIMIZED FOR PRESCRIPTION."
- The Meta blog post (March 31, 2026) introducing these glasses identifies them as the "Ray-Ban Meta Optics Styles" — "Blayzer Optics" and "Scriber Optics" — and explicitly captions them as "(Gen 2)" (e.g., "Ray-Ban Meta Blayzer Optics (Gen 2) in Matte Black"). They were the prescription-focused models, available for pre-order March 31, 2026 and at retail starting April 14, 2026 [https://www.meta.com/blog/ray-ban-meta-styles-prescription-lenses/](https://www.meta.com/blog/ray-ban-meta-styles-prescription-lenses/).
- Thus the Scriber/Blazer (RW7001/RW7002) ARE the prescription "Gen 2 variants" that the resolution criteria explicitly EXCLUDE from counting as "Gen 3." (The earlier reporting that the new RW7001/RW7002 model numbers "suggest a new hardware generation" [Meta Slated to Launch Two New Ray-Ban Smart Glasses, According ...](https://roadtovr.com/meta-ray-ban-smart-glasses-2026-next-gen/) turned out to be incorrect; Meta and Ray-Ban branded them Gen 2.)

No actual Gen 3 product launched in the window:
- There is no evidence any Ray-Ban Meta product explicitly marketed as "third-generation"/"Gen 3" became orderable on Meta.com or Ray-Ban.com between May 2 and June 1, 2026. Reporting indicates Gen 3 is expected around Meta Connect 2026 (September) or later in 2026/2027.

Two independent reasons for NO:
1. The named RW7001/RW7002 products are explicitly branded Gen 2 prescription variants — exactly the category the criteria exclude — so they do not satisfy the "Gen 3" requirement.
2. Even setting aside branding, these prescription models became available (pre-order March 31 / retail April 14, 2026) BEFORE the May 2–June 1 window, and no genuine Gen 3 model became available within the window.

Therefore the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-111. `08b12512-265a-5ac4-8344-b0f7b4d9fdc7`

- Present date: `2026-05-02 09:14:49.775147`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Israel conduct a direct military strike on Iranian sovereign territory between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between 00:00 UTC on April 30, 2026, and 23:59 UTC on June 1, 2026, the armed forces of the State of Israel conduct at least one confirmed direct military strike on the sovereign territory of the Islamic Republic of Iran (i.e., within Iran's internationally recognized borders).

**Definition of "direct military strike":** A kinetic military action — including but not limited to airstrikes, missile strikes, drone strikes, or naval bombardment — that results in a physical impact (explosion, destruction, or damage) on Iranian sovereign territory. The strike must be carried out by Israeli military forces (IDF) or be officially claimed or acknowledged by the Israeli government.

**Exclusions:**
- Cyberattacks, electronic warfare, or signals intelligence operations do not count.
- Attacks by non-state proxy groups (e.g., Hezbollah, MEK, or other militias) do not count unless the Israeli government officially claims responsibility.
- Israeli strikes on Iranian assets, personnel, or proxy forces located outside Iranian sovereign territory (e.g., in Lebanon, Syria, Iraq, or Yemen) do not count.
- Naval interceptions or blockade enforcement actions that do not involve a kinetic strike on Iranian territory do not count.

**Resolution sources:** Resolution will be determined based on credible reporting from at least two of the following news organizations: Reuters (reuters.com), Associated Press (apnews.com), BBC (bbc.com), The New York Times (nytimes.com), or The Wall Street Journal (wsj.com). If these outlets report a confirmed Israeli strike on Iranian territory meeting the above definition, the question resolves Yes. Otherwise, it resolves No on June 1, 2026.

**Pre-cutoff background**

On February 28, 2026, the United States and Israel launched a major military campaign against Iran, with nearly 900 strikes in the first 12 hours targeting Iranian missiles, air defenses, military infrastructure, and government sites [2026 Iran war ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire). This followed the breakdown of the fragile, unwritten ceasefire that had held since the end of the "Twelve Day War" between Israel and Iran in June 2025 [https://www.atlanticcouncil.org/blogs/menasource/what-will-2026-bring-for-the-middle-east-and-north-africa/](https://www.atlanticcouncil.org/blogs/menasource/what-will-2026-bring-for-the-middle-east-and-north-africa/). The Twelve Day War ceasefire, mediated by the United States and Qatar, had been sustained largely through US diplomatic pressure on Israel rather than any formal written agreement [https://www.atlanticcouncil.org/blogs/menasource/what-will-2026-bring-for-the-middle-east-and-north-africa/](https://www.atlanticcouncil.org/blogs/menasource/what-will-2026-bring-for-the-middle-east-and-north-africa/).

On April 8, 2026, the United States and Iran agreed to a two-week ceasefire mediated by Pakistan, intended to halt hostilities and facilitate negotiations [2026 Iran war ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire). On April 21, 2026, President Trump announced an extension of the ceasefire to allow further diplomatic engagement. However, the ceasefire has been repeatedly violated: the US has maintained a naval blockade on Iran, Israel has continued heavy strikes in Lebanon against Hezbollah, and Iran has accused both the US and Israel of breaching the truce terms [2026 Iran war ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire). As of late April 2026, the ceasefire is considered highly fragile, with Iran rejecting a 45-day ceasefire proposal and instead demanding a permanent end to the war. Israel's response to the ceasefire has been muted, and Israeli strikes on Lebanon have continued to escalate. The question of whether Israel will resume direct strikes on Iranian territory during this period remains genuinely uncertain, depending on the trajectory of ceasefire negotiations and regional escalation dynamics.

**Exact later resolution packet**

The question resolves NO (0). It asked whether the Israeli military (IDF), or with official Israeli government acknowledgment, conducted at least one confirmed direct kinetic military strike on Iranian sovereign territory between 00:00 UTC April 30, 2026 and 23:59 UTC June 1, 2026, as reported by at least two of Reuters, AP, BBC, NYT, or WSJ.

Across the relevant window, the consistent and well-documented pattern is that strikes on Iranian soil during this period were conducted by the UNITED STATES, not by Israel. Israel's kinetic military operations in this window were directed against Hezbollah in Lebanon (e.g., strikes on Beirut's southern suburbs and Tyre), not against Iranian territory.

Key evidence:
- The Wikipedia "2026 Iran war ceasefire" article documents the May 2026 strikes on Iranian territory (May 7, around Hormozgan/Bandar Khamir/Sirik/Qeshm; May 25 strikes on missile launch sites and boats in Bandar Abbas) and attributes all of them explicitly to the United States, with no Israeli strikes on Iranian soil recorded in the window [f82107].
- The Wikipedia "List of attacks during the 2026 Iran war" article lists the "7 May 2026 U.S. strikes on Iran" event attributed to the United States, and records no Israeli strike on Iranian territory in the April 30–June 1 window [c6a314].
- A Reuters article (May 28, 2026) describing the period reports the U.S. and Iran trading strikes (e.g., U.S. CENTCOM downing drones and striking a ground control station at Bandar Abbas), while Israel's strikes were on Lebanon (Beirut suburbs, Tyre) — not Iran [3a6c18].
- A Reuters article dated June 1, 2026 is headlined around the U.S. (not Israel) striking Iranian military sites, with Iran responding with an air base attack; it reports no Israeli strike on Iranian soil in the window [f53527].
- An ISW Iran Update Special Report (May 13, 2026) reports no new Israeli kinetic strikes inside Iran during early-to-mid May 2026; it notes Israeli strikes continuing in Lebanon and that prior U.S.-Israeli strikes on Iranian missile facilities occurred earlier in the war [ebad0f].
- An Al Jazeera timeline (May 27, 2026) of attacks during the ceasefire attributes the late-May strikes on southern Iran to U.S. Central Command and lists no Israeli strikes on Iranian territory in the window [41326a].
- The only Israeli aircraft activity reported over Iranian airspace (an aircraft targeted by a surface-to-air missile) was on March 21, 2026 — outside the resolution window [3a06f4].

Because no qualifying confirmed Israeli (IDF) direct kinetic strike on Iranian sovereign territory in the April 30–June 1, 2026 window was reported by the required sources (the strikes on Iran in this period were U.S. operations, and Israeli strikes were on Lebanon), the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-112. `258540c7-f3d4-51f9-a22b-39f6d7b9f7d2`

- Present date: `2026-05-14 06:19:16.924096`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the version of the CLARITY Act voted on or reported out by the Senate Banking Committee by July 1, 2026, include an ethics provision restricting senior government officials from profiting from digital assets?

**Resolution criteria**

This question resolves **Yes** if, between May 12, 2026, and July 1, 2026, the Senate Committee on Banking, Housing, and Urban Affairs votes by majority to report H.R. 3633 (the Digital Asset Market Clarity Act) or a substitute amendment thereof to the full Senate, AND the version of the bill as voted on or reported out contains an explicit statutory provision that restricts or prohibits "senior government officials" from "profiting from digital assets," as defined below.

This question resolves **No** if:
- The bill is reported out of committee without such a provision, OR
- The committee does not report the bill by July 1, 2026.

**Definitions:**

- **"Advancing"**: A majority vote by the Senate Committee on Banking, Housing, and Urban Affairs to formally report the bill (favorably or without recommendation) to the full Senate. A voice vote or roll-call vote at a noticed executive session of the committee qualifies.

- **"Senior government officials"**: Individuals defined as "officers and employees" under 5 U.S.C. § 2104 or elected officials of the federal government (the President, Vice President, and Members of Congress), as well as their spouses and dependent children, to the extent the provision covers them. The ethics provision need not use this exact statutory citation; any language that substantively restricts federal officeholders and/or senior executive branch officials from holding or profiting from digital assets qualifies.

- **"Profiting from digital assets"**: The provision must restrict at least one of the following activities by the covered individuals: (a) personal ownership or holding of digital assets (as defined elsewhere in the bill), (b) realization of capital gains from the sale or exchange of digital assets, or (c) receipt of income, compensation, or financial benefit from digital asset ventures, enterprises, or token issuances.

- **"Ethics provision"**: A new statutory provision included in the text of the bill as voted on or reported out by the committee. A mere reference to existing ethics laws (e.g., a "Rule of Construction" pointing to pre-existing statutes) does not qualify; the provision must create new restrictions or prohibitions beyond current law.

**Resolution source**: The official text of the bill as published on Congress.gov (https://www.congress.gov/bill/119th-congress/house-bill/3633) or the Senate Banking Committee's official website (https://www.banking.senate.gov/). If committee action occurs near July 1 and the official text is not yet posted, credible reporting from Reuters, AP, Bloomberg, or CoinDesk confirming the inclusion or exclusion of the provision may be used as an interim source.

**Pre-cutoff background**

The Digital Asset Market Clarity Act (H.R. 3633) passed the U.S. House of Representatives on July 17, 2025, and was referred to the Senate Committee on Banking, Housing, and Urban Affairs on September 18, 2025 [Text - H.R.3633 - 119th Congress (2025-2026): Digital Asset Market ...](https://www.congress.gov/bill/119th-congress/house-bill/3633/text). The Senate Banking Committee, chaired by Tim Scott, scheduled a markup of the bill for May 14, 2026 [Senate Banking Committee Releases CLARITY Act Bill Text Hours ...](https://unchainedcrypto.com/senate-banking-committee-releases-clarity-act-bill-text-hours-before-thursdays-markup/).

As of May 12, 2026, the committee released a revised 309-page draft of the bill. This draft includes new provisions on stablecoin rewards (permitting activity-based rewards while banning passive yield), DeFi protections, and insider trading rules (Section 109). However, the revised draft does not include ethics provisions barring senior government officials from holding or profiting from cryptocurrency [What's new in the Senate Banking Committee's updated CLARITY ...](https://invezz.com/news/2026/05/12/whats-new-in-the-senate-banking-committees-updated-clarity-act/). The conflict-of-interest section is reportedly not under the Banking Committee's jurisdiction, meaning it would need to be added as an amendment or through other procedural means [Senate Banking Committee Releases CLARITY Act Bill Text Hours ...](https://unchainedcrypto.com/senate-banking-committee-releases-clarity-act-bill-text-hours-before-thursdays-markup/).

Senate Democrats, including Senators Kirsten Gillibrand and Elizabeth Warren, have stated they will not support the legislation without the inclusion of conflict-of-interest language restricting federal officials from profiting through crypto ventures [What's new in the Senate Banking Committee's updated CLARITY ...](https://invezz.com/news/2026/05/12/whats-new-in-the-senate-banking-committees-updated-clarity-act/). This ethics fight is a key point of contention that could determine whether the bill secures bipartisan support or stalls in committee. The White House has targeted July 4, 2026, for passage of the full bill.

The current draft text is available at the Senate Banking Committee website: https://www.banking.senate.gov/imo/media/doc/ehf26374.pdf [Senate Banking Committee Releases CLARITY Act Bill Text Hours ...](https://unchainedcrypto.com/senate-banking-committee-releases-clarity-act-bill-text-hours-before-thursdays-markup/). The bill's Congress.gov page is: https://www.congress.gov/bill/119th-congress/house-bill/3633 [Text - H.R.3633 - 119th Congress (2025-2026): Digital Asset Market ...](https://www.congress.gov/bill/119th-congress/house-bill/3633/text).

**Exact later resolution packet**

The question resolves **NO (0)**.

**Antecedent (committee reported the bill by July 1, 2026): SATISFIED.** On May 14, 2026 — within the May 12–July 1, 2026 window — the Senate Committee on Banking, Housing, and Urban Affairs voted 15–9 to advance H.R. 3633 (the Digital Asset Market Clarity Act) to the full Senate, ordering it reported with an amendment in the nature of a substitute [dff202][f893a1]. Congress.gov's official record confirms the committee "Reported by Senator Scott SC, with an amendment in the nature of a substitute. Without written report," dated 05/14/2026, with the bill subsequently reported to the Senate and placed on the Legislative Calendar [b73830]. So the committee did report the bill by the deadline.

**Consequent (ethics provision included): NOT SATISFIED.** The version voted on/reported out did NOT contain a new statutory provision restricting "senior government officials" from profiting from digital assets:
- The revised draft that formed the basis of the markup did not include such ethics/conflict-of-interest provisions (that section was described as outside the Banking Committee's jurisdiction) [f893a1].
- During the May 14, 2026 markup, an amendment offered by Senator Chris Van Hollen to prohibit senior government officials (including the President and Vice President) from having business ties to the crypto industry was explicitly voted on and FAILED, 11–13. No other ethics provision restricting senior officials from profiting from digital assets was adopted [dff202].
- CoinDesk's live coverage confirms the committee advanced the bill 15–9 without any such ethics provision, with the conflict-of-interest issue remaining an unresolved point for future negotiations [dff202]. Corroborating reporting notes the legislation "now faces negotiations over final language and ethics provisions," and that Democratic amendments were voted down or blocked [dc7afd].

Because the committee reported the bill by July 1, 2026 but the reported version did NOT include the required ethics provision, the resolution criteria's explicit NO condition ("The bill is reported out of committee without such a provision") is met. Resolution = NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-113. `6d2d0507-66ca-5db4-b3a6-b46578bce91d`

- Present date: `2026-05-03 11:11:37.389808`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Trump administration announce a deal to cancel or terminate at least one additional U.S. offshore wind lease between May 2, 2026, and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 2, 2026, and no later than 11:59 PM UTC on June 1, 2026, the U.S. Department of the Interior or the Trump administration officially announces a deal, agreement, or settlement to cancel, terminate, or voluntarily end at least one U.S. offshore wind lease that is **not** the Bluepoint Wind or Golden State Wind leases terminated on April 27, 2026.

Key definitions:
- **U.S. offshore wind lease:** A lease issued by the Bureau of Ocean Energy Management (BOEM) granting rights to develop wind energy on the U.S. outer continental shelf. See: https://www.boem.gov/renewable-energy/state-activities
- **Announcement or deal:** An official press statement, press release, or formal update published by the U.S. Department of the Interior (https://www.doi.gov/news) or BOEM (https://www.boem.gov/newsroom), or confirmed by at least two major credible news outlets (e.g., Reuters, AP, Bloomberg, NYT).
- **Cancel or terminate:** The leaseholder agrees to relinquish, surrender, or voluntarily end the lease, whether in exchange for reimbursement, fossil fuel investment commitments, or otherwise.

The question resolves **No** if no such announcement is made by 11:59 PM UTC on June 1, 2026.

Resolution sources:
- U.S. Department of the Interior newsroom: https://www.doi.gov/news
- BOEM press releases: https://www.boem.gov/newsroom
- Credible reporting from Reuters (https://www.reuters.com), AP (https://apnews.com), Bloomberg, or NYT.

**Pre-cutoff background**

The Trump administration has pursued a systematic strategy of negotiating the cancellation of U.S. offshore wind leases, offering developers reimbursements in exchange for redirecting funds toward fossil fuel infrastructure.

As of May 2, 2026, the following lease cancellations have occurred:

- **March 2026:** TotalEnergies reached an agreement with the Interior Department to redirect approximately $1 billion from offshore wind leases to U.S. oil and gas production [US to end more offshore wind leases in exchange for fossil fuel ...](https://www.reuters.com/business/energy/us-reaches-deal-end-two-more-offshore-wind-leases-2026-04-27/).
- **April 27, 2026:** The administration announced deals to end two more offshore wind leases [US to end more offshore wind leases in exchange for fossil fuel ...](https://www.reuters.com/business/energy/us-reaches-deal-end-two-more-offshore-wind-leases-2026-04-27/):
  - **Bluepoint Wind** (off New York/New Jersey), operated by Ocean Winds (ENGIE/EDP Renewables) and Global Infrastructure Partners (BlackRock unit). The $765 million bid amount will be redirected into a U.S. LNG facility.
  - **Golden State Wind** (off California), operated by Ocean Winds and Reventus Power. The developer may recover $120 million in lease fees after investing a similar amount in oil, gas, or LNG projects.

Combined, these April 27 deals total nearly $900 million in reimbursements [US to end more offshore wind leases in exchange for fossil fuel ...](https://www.reuters.com/business/energy/us-reaches-deal-end-two-more-offshore-wind-leases-2026-04-27/). The administration has characterized offshore wind projects as "expensive, unreliable, [and] intermittent" [US to end more offshore wind leases in exchange for fossil fuel ...](https://www.reuters.com/business/energy/us-reaches-deal-end-two-more-offshore-wind-leases-2026-04-27/). Multiple other U.S. offshore wind leases remain active under various developers, and the administration's pattern suggests further negotiations may be underway, though each deal involves unique terms and timelines.

U.S. offshore wind leases are issued by the Bureau of Ocean Energy Management (BOEM), part of the Department of the Interior, granting rights to develop wind energy facilities on the outer continental shelf. See: https://www.boem.gov/renewable-energy/state-activities

**Exact later resolution packet**

The question resolves NO. It asks whether the Trump administration/DOI officially announced, between May 2, 2026 and 11:59 PM UTC June 1, 2026, a deal to cancel/terminate at least one U.S. BOEM offshore wind lease OTHER THAN the Bluepoint Wind or Golden State Wind leases (which were announced April 27, 2026).

Key findings from multiple authoritative sources:

1. The Harvard Law School Environmental & Energy Law Program (EELP) "Federal Offshore Wind Deployment" tracker lists the most recent lease-cancellation actions as March 23, 2026 (TotalEnergies — Attentive Energy and Carolina Long Bay) and April 27, 2026 (Bluepoint Wind and Golden State Wind). No further lease cancellations or terminations are recorded for the May 2 – June 1, 2026 window [5cebc7].

2. A review of the U.S. Department of the Interior newsroom (https://www.doi.gov/news) press releases for May 2026 shows topics such as the MAPLand/MAPWaters Act (5/28), hunting/fishing access (5/26), oil and gas lease sales in New Mexico/Texas (5/20), NPR-A permitting (5/15), and a tribal energy agreement (5/11) — none of which announce the cancellation or termination of any offshore wind lease [34956a].

3. An E&E News (POLITICO) article published May 26, 2026 confirms that as of that date, the only announced lease-cancellation deals were TotalEnergies (March 2026) and Ocean Winds' Bluepoint Wind and Golden State Wind (April 27, 2026). While the article notes other leases could be "on the chopping block" and that some developers are reportedly in discussions, no additional deal had been officially announced, and Interior "did not respond to a request for comment on whether it plans to offer additional deals" [088dc4].

Thus, the only deals in the relevant period are the excluded Bluepoint Wind and Golden State Wind leases (announced April 27, before the window). No qualifying announcement occurred within May 2 – June 1, 2026, so the question resolves NO.

Sources:
- EELP tracker: https://eelp.law.harvard.edu/tracker/federal-offshore-wind-deployment/ [5cebc7]
- DOI newsroom: https://www.doi.gov/news [34956a]
- E&E News (May 26, 2026): https://www.eenews.net/articles/trump-is-paying-companies-to-quit-offshore-wind-these-projects-could-be-next-2/ [088dc4]

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-114. `826dafc3-01da-575f-97af-e3c07a999d0f`

- Present date: `2026-05-12 19:13:26.898565`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the USTR formally announce new Section 301 tariffs on imports from at least one country before July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 10, 2026, and before 11:59 PM UTC on July 1, 2026, the USTR makes a **formal announcement** of new tariffs under Section 301 of the Trade Act of 1974 (19 U.S.C. § 2411) on imports from at least one country. A "formal announcement" is defined as either:

- An official press release published on the [USTR press releases page](https://ustr.gov/about/policy-offices/press-office/press-releases), **or**
- A notice published in the [Federal Register](https://www.federalregister.gov/agencies/trade-representative-office-of-united-states)

that explicitly states the USTR is imposing, or has determined to impose, new tariffs under Section 301 authority on imports from one or more countries.

**Clarification on "proposed" vs. "final":** The announcement of a mere *proposed* list of products for public comment does **not** satisfy resolution. The announcement must reflect a **final determination** or **action** to impose tariffs—i.e., the USTR must have determined that tariffs will be applied, not merely that tariffs are being considered. A Federal Register notice requesting public comment on a proposed tariff list would not count.

If no such announcement meeting these criteria is made by 11:59 PM UTC on July 1, 2026, the question resolves **No**.

**Pre-cutoff background**

In March 2026, the Office of the United States Trade Representative (USTR) launched two sweeping sets of [Section 301](https://ustr.gov/issue-areas/enforcement/section-301-investigations) investigations under the Trade Act of 1974 (19 U.S.C. § 2411):

1. **Structural Excess Capacity (March 11, 2026):** Investigations into 16 economies—China, the EU, Singapore, Switzerland, Norway, Indonesia, Malaysia, Cambodia, Thailand, Korea, Vietnam, Taiwan, Bangladesh, Mexico, Japan, and India—targeting structural excess capacity and production in manufacturing sectors [USTR Initiates Section 301 Investigations Relating to Structural ...](https://ustr.gov/about/policy-offices/press-office/press-releases/2026/march/ustr-initiates-section-301-investigations-relating-structural-excess-capacity-and-production).

2. **Forced Labor (March 12, 2026):** Investigations into approximately 60 economies regarding failures to prohibit imports of goods produced with forced labor [Opportunity to Comment on Foreign Trade Practices with New Tariffs ...](https://www.dorsey.com/newsresources/publications/client-alerts/2026/3/opportunity-to-comment-section-301).

These investigations are widely understood as the administration's strategy to establish permanent tariffs under Section 301 authority before the temporary Section 122 tariffs (a global 10% tariff) expire on July 24, 2026 [US trade court rules Trump tariffs illegal, but issues narrow block](https://www.reuters.com/world/us-trade-court-rules-against-trumps-10-global-tariff-2026-05-07/) [Opportunity to Comment on Foreign Trade Practices with New Tariffs ...](https://www.dorsey.com/newsresources/publications/client-alerts/2026/3/opportunity-to-comment-section-301). The public comment deadline for the first investigation was April 15, 2026, and public hearings began on May 5, 2026 [USTR Initiates Section 301 Investigations Relating to Structural ...](https://ustr.gov/about/policy-offices/press-office/press-releases/2026/march/ustr-initiates-section-301-investigations-relating-structural-excess-capacity-and-production). As of May 11, 2026, no formal tariff determinations have been announced. The U.S. Court of International Trade ruled the Section 122 tariffs unjustified on May 7, 2026, though they remain in effect pending appeal [US trade court rules Trump tariffs illegal, but issues narrow block](https://www.reuters.com/world/us-trade-court-rules-against-trumps-10-global-tariff-2026-05-07/). Reuters reports the administration has three Section 301 investigations due for completion in July [US trade court rules Trump tariffs illegal, but issues narrow block](https://www.reuters.com/world/us-trade-court-rules-against-trumps-10-global-tariff-2026-05-07/). The key uncertainty is whether the USTR will finalize and announce tariffs before July 1, or closer to the July 24 Section 122 expiration date.

Section 301 of the Trade Act of 1974 authorizes the USTR to investigate and respond to unfair foreign trade practices that burden U.S. commerce. For more information, see [USTR's Section 301 page](https://ustr.gov/issue-areas/enforcement/section-301-investigations) and the [statute (19 U.S.C. § 2411)](https://www.law.cornell.edu/uscode/text/19/2411).

**Exact later resolution packet**

The question resolves NO. It required a USTR FORMAL announcement (official press release or Federal Register notice) of a FINAL determination or action to IMPOSE new Section 301 tariffs on imports from at least one country, made on/after May 10, 2026 and before 11:59 PM UTC July 1, 2026. The resolution criteria explicitly state that a mere PROPOSED tariff list open for public comment does NOT satisfy resolution.

Every relevant USTR Section 301 tariff action in the window was a PROPOSAL, not a final determination:

1. Brazil (announced June 1, 2026): USTR determined Brazil's practices are actionable under Section 301(b) but only "proposed responsive action for public comment," inviting written comments by July 1, 2026, with a hearing scheduled for July 6, 2026 [36047c]. This is a proposal, and the hearing/implementation postdate July 1.

2. Forced Labor – 60 economies (announced June 2, 2026): USTR made findings of actionability and "proposed responsive action for public comment," with written comments due July 6, 2026 and hearings beginning July 7, 2026 [2c43a1]. Legal analyses confirm these were proposed 10%–12.5% tariffs to be "finalized and implemented after USTR completes the public comment and hearing process," with USTR aiming to be ready to impose them around the July 24, 2026 expiration of the Section 122 tariffs [cc7c2c].

3. Structural Excess Capacity – 16 economies: As of mid-June 2026, no final determination to impose tariffs had been issued; determinations were described as pending/imminent, and any tariffs were expected to align with the ~July 25, 2026 timeframe (after Section 122 expires July 24) [cc7c2c, 2fa6dd].

Because all announcements before the July 1, 2026 deadline were proposals with hearings scheduled July 6–7, 2026 and expected implementation in late July 2026 — and the resolution criteria explicitly exclude proposals/requests for comment — no qualifying final determination or action to impose Section 301 tariffs was announced within the window. The question resolves NO (0).

Key sources: USTR press release "USTR Makes Findings and Proposes Action in 60 Section 301 Investigations..." (June 2, 2026) [2c43a1]; USTR press release "USTR Section 301 Determination on Brazil's Unreasonable Acts, Policies, and Practices" (June 1, 2026) [36047c]; White & Case alert (June 5, 2026) [cc7c2c]; American Action Forum "The New Section 301 Tariff Regime" [2fa6dd].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-115. `467952fd-881f-5403-ad3f-a9d6c89e07ee`

- Present date: `2026-05-14 08:55:14.960614`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Wisconsin Supreme Court rule that Notice of Voting Eligibility forms are public records subject to disclosure in Wisconsin Voter Alliance v. Secord?

**Resolution criteria**

This question resolves **Yes** if the Wisconsin Supreme Court, in a written opinion or order issued on or after May 12, 2026 and on or before July 1, 2026 (11:59 PM CT / 04:59 AM UTC July 2), rules that Notice of Voting Eligibility (NVE) forms are public records subject to disclosure under Wisconsin law in *Wisconsin Voter Alliance v. Secord* (Case No. 2023-AP-36). A ruling that allows disclosure only with redactions of personally identifying information still counts as **Yes**, since it affirms the records' status as public records subject to disclosure.

This question resolves **No** if:
1. The Court rules that NVE forms are not public records subject to disclosure; or
2. The Court dismisses the case, declines to reach the merits, or resolves it on procedural grounds without classifying the records as public records; or
3. No ruling is issued by 11:59 PM CT on July 1, 2026 (04:59 AM UTC July 2, 2026).

**Resolution source:** The official opinion published on the Wisconsin Court System's Supreme Court opinions page (https://www.wicourts.gov/supreme/scopin.htm) or the case docket accessible via the Wisconsin Circuit Court Access system (https://wcca.wicourts.gov/).

**Pre-cutoff background**

The Wisconsin Supreme Court is deliberating *Wisconsin Voter Alliance v. Secord* (Case No. 2023-AP-36), a case concerning whether Notice of Voting Eligibility (NVE) forms—documents generated when a circuit court judge determines an individual under guardianship is incompetent to vote—are public records subject to disclosure under Wisconsin's public records law [https://www.votebeat.org/wisconsin/2026/04/20/supreme-court-legal-case-voter-data/](https://www.votebeat.org/wisconsin/2026/04/20/supreme-court-legal-case-voter-data/) [Wisconsin Supreme Court weighs whether voter eligibility records ...](https://www.wpr.org/news/wisconsin-supreme-court-incompetency-voter-eligibility-heuer).

The Wisconsin Voter Alliance, a conservative group, filed identical petitions for writ of mandamus against registers in probate for 13 circuit courts, seeking access to these records to verify voter rolls. Opponents, including Disability Rights Wisconsin, argue the records are closed court records protected by state guardianship statutes (Wis. Stat. §§ 54.75, 54.25) and that disclosure would violate the privacy of vulnerable populations [Wisconsin Supreme Court weighs whether voter eligibility records ...](https://www.wpr.org/news/wisconsin-supreme-court-incompetency-voter-eligibility-heuer).

**Procedural history:** On January 17, 2025, the Wisconsin Supreme Court vacated a prior District II Court of Appeals ruling that had favored disclosure, and remanded the case [Wisconsin Voter Alliance and Ron Heuer v. Kristina Secord](https://www.lawforward.org/wva-v-secord/). The case returned to the Supreme Court, which heard oral arguments on April 21, 2026 [Wisconsin Voter Alliance and Ron Heuer v. Kristina Secord](https://www.lawforward.org/wva-v-secord/) [https://www.votebeat.org/wisconsin/2026/04/20/supreme-court-legal-case-voter-data/](https://www.votebeat.org/wisconsin/2026/04/20/supreme-court-legal-case-voter-data/). As of May 12, 2026, the court is deliberating and a final opinion is pending.

**Court composition:** The Wisconsin Supreme Court currently has a 4-3 liberal majority, which may favor privacy protections for individuals under guardianship. However, the public records argument has significant legal merit, and the plaintiff argues that privacy concerns can be addressed through redaction of identifying information [Wisconsin Supreme Court weighs whether voter eligibility records ...](https://www.wpr.org/news/wisconsin-supreme-court-incompetency-voter-eligibility-heuer).

The resolution source is the Wisconsin Supreme Court's official opinions page: https://www.wicourts.gov/supreme/scopin.htm

**Exact later resolution packet**

The question resolves NO (0) because the Wisconsin Supreme Court did NOT issue any ruling in Wisconsin Voter Alliance v. Secord (Case No. 2023AP36 / 2023-AP-36) during the resolution window of May 12, 2026 through July 1, 2026 (11:59 PM CT). This triggers resolution criterion #3: "No ruling is issued by 11:59 PM CT on July 1, 2026."

Key evidence (all from the specified/authoritative sources):

1. OFFICIAL COURT SOURCE — The Wisconsin Supreme Court's official "Table of Pending Cases" (https://www.wicourts.gov/sc/SCCASES.pdf), dated June 10, 2026, lists case 2023AP36 (Wisconsin Voter Alliance v. Kristina Secord) as still PENDING: accepted by the court on 01/07/2026 with oral arguments held 04/21/2026, and NO decision date or mandate recorded. The highest opinion citation issued by that date was only 2026 WI 19 [7c0d32]. This is the closest authoritative snapshot to the deadline and shows no decision had issued.

2. Votebeat's Wisconsin news page, checked as of July 1, 2026, contains NO article reporting any Supreme Court decision in the case; the most recent relevant coverage was the April 20, 2026 oral-argument preview [192202]. The Votebeat case article itself, last updated June 1, 2026, stated the court was still deliberating after the April 21, 2026 arguments [4439be].

3. Law Forward's case tracker (a party in the case, tracking it closely) shows no events past the April 21, 2026 oral arguments [eb7c23]; State Court Report's case tracker lists status as "Pending" [2cc158]; and the Wisconsin Justice Initiative's June 2026 blog archive contains no post announcing a Secord decision [5df84f].

4. Context: The only prior Wisconsin Supreme Court action, on January 17, 2025 (2025 WI 2), was a procedural disposition that vacated the District II Court of Appeals ruling and remanded on procedural grounds (appellate-conflict rules) WITHOUT reaching the merits of whether NVE forms are public records [cbedcc]. That decision (a) predates the window and (b) would not have counted as YES anyway.

No source — official or news — indicates any opinion or order classifying NVE forms as public records was issued between May 12 and July 1, 2026. Therefore the antecedent for a YES (a merits ruling that NVE forms are public records subject to disclosure, even with redactions) never occurred, and criterion #3 (no ruling by the deadline) controls, resolving the question NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-116. `bc18b8dc-6ab4-5cc2-98a1-8c73306d10a3`

- Present date: `2026-05-16 06:46:56.345876`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-06-13T00:00:00`

**Question**

Will at least one living D-Day veteran be physically present at the official international ceremony at Langrune-sur-Mer on June 6, 2026?

**Resolution criteria**

This question resolves YES if at least one D-Day veteran is confirmed to have been physically present at the official international ceremony at Langrune-sur-Mer on June 6, 2026. It resolves NO otherwise.

**Key definitions:**

- **D-Day veteran**: A person who served in the Allied armed forces (of any nation) and participated in [Operation Overlord](https://en.wikipedia.org/wiki/Normandy_landings) on June 6, 1944, including the amphibious landings, airborne operations, or direct naval support operations on that date.

- **Physical presence**: The veteran must be bodily present at the ceremony site in Langrune-sur-Mer during the official international ceremony. Virtual attendance, video messages, or participation in other D-Day commemorative events elsewhere in Normandy do not count.

- **Official international ceremony**: The ceremony organized by the [Comité du Débarquement](https://www.comitedudebarquement.fr/en/) at Langrune-sur-Mer on June 6, 2026, scheduled for 4:30 PM CEST (UTC+2) [Why is the international ceremony being held in Langrune-sur-Mer?](https://www.comitedudebarquement.fr/en/ceremonie-internationale-82e-anniversaire-du-debarquement/).

**Resolution sources**: Credible reporting from major news agencies such as [AP](https://apnews.com/), [Reuters](https://www.reuters.com/), [BBC](https://www.bbc.com/news), [AFP](https://www.afp.com/), or major French outlets such as [Le Monde](https://www.lemonde.fr/) or [Ouest-France](https://www.ouest-france.fr/), confirming that at least one D-Day veteran attended the ceremony. The veteran's D-Day participation must be identified in reporting (by name and service record) rather than merely described as a "WWII veteran."

**Edge cases:**
- If the ceremony is cancelled or relocated to a different municipality, this question resolves NO.
- If a veteran's claimed D-Day participation is disputed in credible reporting, that veteran does not count for resolution purposes unless at least one credible source affirms their participation without contradiction from equally credible sources.
- If a D-Day veteran is present at Langrune-sur-Mer for other events on June 6 but not confirmed at the official international ceremony itself, this resolves NO.

**Pre-cutoff background**

On June 6, 2026, the official international ceremony commemorating the 82nd anniversary of the D-Day landings will be held at Langrune-sur-Mer, France (Sword/Juno Beach junction), organized by the Comité du Débarquement (D-Day Commemoration Committee) [Why is the international ceremony being held in Langrune-sur-Mer?](https://www.comitedudebarquement.fr/en/ceremonie-internationale-82e-anniversaire-du-debarquement/). The ceremony is scheduled for 4:30 PM local time (Central European Summer Time, UTC+2).

The cohort of living WWII veterans is shrinking rapidly. As of 2025, approximately 45,418 American WWII veterans remained alive out of the original 16.4 million who served, and this number is projected to drop to roughly 42,127 by 2026. However, D-Day veterans specifically—those who participated in the Normandy landings on June 6, 1944—are a much smaller subset, and all would be at least 100 years old by June 2026.

At the 81st anniversary in 2025, the Best Defense Foundation brought 23 WWII veterans to Normandy, including Jake Larson, a 102-year-old D-Day veteran who landed on Omaha Beach on June 6, 1944 [WWII vets are rock stars in France as they hand over the duty of ...](https://www.ap.org/news-highlights/spotlights/2025/wwii-vets-are-rock-stars-in-france-as-they-hand-over-the-duty-of-remembering-d-day/). For 2026, the Best Defense Foundation has announced plans to bring 25 WWII veterans to Normandy for the 82nd anniversary, though it is unclear how many (if any) of those 25 are specifically D-Day veterans rather than WWII veterans who served elsewhere.

The key uncertainty is whether any D-Day veteran will: (a) still be alive in June 2026, (b) be healthy enough to travel to Normandy, and (c) attend the specific international ceremony at Langrune-sur-Mer rather than other commemorative events in the region.

**Exact later resolution packet**

RESOLUTION: NO (0)

**Step 1 — The antecedent/edge case is satisfied (the ceremony was NOT cancelled or relocated).**
The official international ceremony for the 82nd anniversary of D-Day was held at Langrune-sur-Mer on Saturday, June 6, 2026, presided over by French PM Sébastien Lecornu, with representatives of ~11 nations including UK Defence Secretary John Healey and US Under Secretary of Defense Elbridge Colby (who replaced Pete Hegseth). Confirmed by Ouest-France [à la cérémonie internationale de Langrune-sur-Mer, des hommages ...](https://www.ouest-france.fr/d-day/en-images-82-ans-du-debarquement-a-la-ceremonie-internationale-de-langrune-sur-mer-des-hommages-et-un-grand-absent-333d4d7a-61b4-11f1-8c24-b38534c94fba)[82 ans du Débarquement en Normandie : entre cérémonies et ...](https://www.ouest-france.fr/d-day/direct-82e-anniversaire-du-debarquement-en-normandie-ceremonies-commemorations-suivez-la-journee-du-6-juin-06c14f59-5870-4779-9a02-7648779ec75f)[VIDÉO. 82e D-Day : la cérémonie internationale, présidée par ...](https://www.ouest-france.fr/d-day/video-82e-d-day-la-ceremonie-internationale-presidee-par-sebastien-lecornu-sacheve-a-langrune-sur-mer-991fb665-33d3-4935-9f56-d72fb4be509f), Le Monde [https://www.lemonde.fr/en/france/article/2026/06/06/on-d-day-anniversary-hegseth-urges-europe-to-counter-present-day-invasion-of-beaches_6754207_7.html](https://www.lemonde.fr/en/france/article/2026/06/06/on-d-day-anniversary-hegseth-urges-europe-to-counter-present-day-invasion-of-beaches_6754207_7.html), France 3 [EN IMAGES. Retour sur les commémorations du 82e anniversaire ...](https://france3-regions.franceinfo.fr/normandie/en-images-retour-sur-les-commemorations-du-82e-anniversaire-du-d-day-en-normandie-3364039.html), and Reuters/AP photo galleries [World War II D-Day anniversary commemorated in France](https://www.staradvertiser.com/2026/06/06/photo-gallery/world-war-ii-d-day-anniversary-commemorated-in-france/)[82nd D-Day landings anniversary commemorated in France. See ...](https://www.usatoday.com/picture-gallery/news/world/2026/06/06/d-day-commemorated-in-france-see-pete-hegseth-wwii-veterans-more/90435504007/). Note: US Secretary of War Pete Hegseth pulled out of the Langrune ceremony (the "grand absent") and instead went to the Normandy American Cemetery at Colleville-sur-Mer plus a private visit [à la cérémonie internationale de Langrune-sur-Mer, des hommages ...](https://www.ouest-france.fr/d-day/en-images-82-ans-du-debarquement-a-la-ceremonie-internationale-de-langrune-sur-mer-des-hommages-et-un-grand-absent-333d4d7a-61b4-11f1-8c24-b38534c94fba)[https://www.lemonde.fr/en/france/article/2026/06/06/on-d-day-anniversary-hegseth-urges-europe-to-counter-present-day-invasion-of-beaches_6754207_7.html](https://www.lemonde.fr/en/france/article/2026/06/06/on-d-day-anniversary-hegseth-urges-europe-to-counter-present-day-invasion-of-beaches_6754207_7.html)[EN IMAGES. Entre cérémonie internationale et visite privée de Pete ...](https://www.ouest-france.fr/d-day/en-images-entre-ceremonie-internationale-et-visite-privee-de-pete-hegseth-retour-sur-un-6-juin-dense-pour-le-82e-d-day-58c96aa8-61b2-11f1-8a5e-13fc958a9977). So the "cancelled/relocated → NO" edge case does not apply on that ground; the ceremony happened at Langrune as planned.

**Step 2 — WWII veterans were physically present at Langrune, but only described generically.**
AP (via USA Today) and Reuters (via Honolulu Star-Advertiser) photo galleries carry captions reading "WWII veterans attend an International commemorative ceremony for the 82nd anniversary of the World War II 'D-Day' Normandy landings in Langrune-sur-Mer" — but NO individual veterans are named, and none is identified as a D-Day (June 6, 1944) participant with a service record [82nd D-Day landings anniversary commemorated in France. See ...](https://www.usatoday.com/picture-gallery/news/world/2026/06/06/d-day-commemorated-in-france-see-pete-hegseth-wwii-veterans-more/90435504007/)[World War II D-Day anniversary commemorated in France](https://www.staradvertiser.com/2026/06/06/photo-gallery/world-war-ii-d-day-anniversary-commemorated-in-france/).

**Step 3 — No credible source names a D-Day veteran (by name and service record) at the Langrune ceremony.**
I checked every relevant report from the specified credible sources (AP, Reuters, BBC, Le Monde, Ouest-France) plus Euronews, France 3, franceinfo, actu.fr and Tendance Ouest. None identifies a specific June-6-1944 participant as physically present at the official Langrune ceremony:
- Ouest-France's detailed coverage of the Langrune ceremony names only officials (Lecornu, Vautrin, Healey, Colby) and discusses Hegseth's absence — no veteran named at Langrune [à la cérémonie internationale de Langrune-sur-Mer, des hommages ...](https://www.ouest-france.fr/d-day/en-images-82-ans-du-debarquement-a-la-ceremonie-internationale-de-langrune-sur-mer-des-hommages-et-un-grand-absent-333d4d7a-61b4-11f1-8c24-b38534c94fba)[82 ans du Débarquement en Normandie : entre cérémonies et ...](https://www.ouest-france.fr/d-day/direct-82e-anniversaire-du-debarquement-en-normandie-ceremonies-commemorations-suivez-la-journee-du-6-juin-06c14f59-5870-4779-9a02-7648779ec75f)[VIDÉO. 82e D-Day : la cérémonie internationale, présidée par ...](https://www.ouest-france.fr/d-day/video-82e-d-day-la-ceremonie-internationale-presidee-par-sebastien-lecornu-sacheve-a-langrune-sur-mer-991fb665-33d3-4935-9f56-d72fb4be509f)[EN IMAGES. Entre cérémonie internationale et visite privée de Pete ...](https://www.ouest-france.fr/d-day/en-images-entre-ceremonie-internationale-et-visite-privee-de-pete-hegseth-retour-sur-un-6-juin-dense-pour-le-82e-d-day-58c96aa8-61b2-11f1-8a5e-13fc958a9977)[82 ans du Débarquement en Normandie : entre cérémonies et ...](https://www.ouest-france.fr/d-day/direct-82e-anniversaire-du-debarquement-en-normandie-ceremonies-commemorations-suivez-la-journee-du-6-juin-06c14f59-5870-4779-9a02-7648779ec75f).
- Le Monde: no veteran named at Langrune; states Hegseth skipped the "main international ceremony... later in the afternoon" [https://www.lemonde.fr/en/france/article/2026/06/06/on-d-day-anniversary-hegseth-urges-europe-to-counter-present-day-invasion-of-beaches_6754207_7.html](https://www.lemonde.fr/en/france/article/2026/06/06/on-d-day-anniversary-hegseth-urges-europe-to-counter-present-day-invasion-of-beaches_6754207_7.html).
- Euronews: mentions "six of the last veterans" but at the British Normandy Memorial, not Langrune [D-Day 82nd anniversary honoured in France - Euronews](https://www.euronews.com/my-europe/2026/06/06/d-day-82nd-anniversary-honoured-in-france).
- BBC: names D-Day veterans Kenneth (Ken) Hay (100) and Henry Rice — but at the British Normandy Memorial at Ver-sur-Mer, not Langrune [World War Two veterans arrive in France on anniversary of D-Day](https://www.bbc.com/news/articles/cvgm53nqvndo).
- France 3: names WWII veterans Harold Terence and Alan Shapiro — but at the Carentan parade / Colleville cemetery, not Langrune [EN IMAGES. Retour sur les commémorations du 82e anniversaire ...](https://france3-regions.franceinfo.fr/normandie/en-images-retour-sur-les-commemorations-du-82e-anniversaire-du-d-day-en-normandie-3364039.html).
- The famous Omaha Beach D-Day veteran Charles Norman Shay had died (honored posthumously) [Ouest-France snippet, uncited article].

**Step 4 — The veterans who could have been at Langrune are not confirmed there by name/service-record.**
The Best Defense Foundation brought 25 WWII veterans (welcomed at Deauville by Brigitte Macron) [25 vétérans accueillis à Deauville par Brigitte Macron - ICI](https://www.ici.fr/normandie/calvados-14/deauville/en-images-82e-anniversaire-du-debarquement-en-normandie-25-veterans-accueillis-a-deauville-par-brigitte-macron-2568221)[Calvados. 25 vétérans américains présents pour ... - Tendance Ouest](https://www.tendanceouest.com/actualite-437811-calvados-25-veterans-americains-presents-pour-les-commemorations-du-6-juin); its roster does include some genuine D-Day participants (e.g., Robert P. Gibson — Utah Beach June 6, 1944; Carl T. Felton — off Omaha Beach June 6, 1944), but its own June 6 schedule listed the Normandy American Cemetery (Colleville) ceremony and a Carentan parade, NOT Langrune [Battlefield Return: Normandy 2026 – 82nd Anniversary](https://bestdefensefoundation.org/battlefield-return/battlefield-return-normandy-2026-82nd-anniversary/). Pre-event Tendance Ouest said the group "would" attend Langrune, but this was a plan, was unnamed, and is not post-event confirmation [Calvados. 25 vétérans américains présents pour ... - Tendance Ouest](https://www.tendanceouest.com/actualite-437811-calvados-25-veterans-americains-presents-pour-les-commemorations-du-6-juin). franceinfo named veterans Jack Ray and Jack Wingate but did not place them at Langrune [D-Day : "J'étais ici il y a 80 ans", confie un vétéran ... - franceinfo](https://www.franceinfo.fr/societe/seconde-guerre-mondiale/d-day-j-etais-ici-il-y-a-80-ans-confie-un-veteran-accueilli-par-brigitte-macron-avant-le-82e-anniversaire-du-debarquement_8044439.html).

**Conclusion.** The resolution criteria explicitly require that "the veteran's D-Day participation must be identified in reporting (by name and service record) rather than merely described as a 'WWII veteran,'" and that presence be at the official Langrune ceremony specifically (not other Normandy events). Applying this literally: although unnamed "WWII veterans" were photographed at Langrune, no credible source names any D-Day (June 6, 1944) participant with a service record as present at the Langrune ceremony. Every named D-Day veteran is documented at other sites (Ver-sur-Mer, Carentan, Colleville). Therefore the YES condition is not met, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-117. `1aaaf310-8d62-578b-bf36-36af15d1bc76`

- Present date: `2026-05-01 13:02:10.029813`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will FIFA officially announce the relocation of any 2026 World Cup match from Mexico to a venue outside of Mexico by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if FIFA issues an official announcement on or after April 30, 2026, and no later than 23:59 UTC on June 1, 2026, stating that one or more of the 13 World Cup matches originally scheduled for Mexican venues (Mexico City, Guadalajara, or Monterrey) will be moved to a venue located **outside of Mexico** (e.g., to a U.S. or Canadian stadium).

**Definitions:**
- **"Relocation"** means moving a match to a venue outside of Mexico entirely. Reassigning a match from one Mexican city to another (e.g., from Monterrey to Mexico City) does **not** count as relocation for purposes of this question.
- **"Official announcement"** means a public statement by FIFA via its official channels, including but not limited to: the [FIFA Media Hub](https://www.fifa.com/media-releases), a press conference by a FIFA spokesperson, or an official update on [FIFA.com](https://www.fifa.com/). Unnamed sources or media speculation alone do not qualify.

The announcement must occur on or after April 30, 2026, to exclude any prior events.

If no such official announcement is made by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

Mexico is a co-host of the 2026 FIFA World Cup, with 13 matches scheduled across three cities: Mexico City (Estadio Azteca), Guadalajara, and Monterrey. Following the death of drug lord Nemesio Oseguera Cervantes ("El Mencho"), violent incidents erupted in several Mexican states, including the burning and looting of stores, blocking of roads, and a shooting near the Teotihuacan pyramids [https://apnews.com/article/fifa-mexico-world-cup-security-mencho-50b57d16d77741bd94ae0b87d15cf69f](https://apnews.com/article/fifa-mexico-world-cup-security-mencho-50b57d16d77741bd94ae0b87d15cf69f). On April 29, 2026, FIFA representatives met with Mexican authorities to review security protocols for the tournament [https://apnews.com/article/fifa-mexico-world-cup-security-mencho-50b57d16d77741bd94ae0b87d15cf69f](https://apnews.com/article/fifa-mexico-world-cup-security-mencho-50b57d16d77741bd94ae0b87d15cf69f).

In response to security concerns, the Mexican government introduced "Plan Kukulkan," a security initiative deploying nearly 99,000 personnel—including 20,000 military and 55,000 police—to protect fans and venues during the tournament [https://www.bbc.com/sport/football/articles/ce8wjwyjndyo](https://www.bbc.com/sport/football/articles/ce8wjwyjndyo). As of March 2026, FIFA President Gianni Infantino stated he felt "very reassured" that Mexico could successfully stage the games [https://www.bbc.com/sport/football/articles/ce8wjwyjndyo](https://www.bbc.com/sport/football/articles/ce8wjwyjndyo). However, ongoing cartel violence and high-profile security incidents have fueled speculation about potential match relocations, with some reports suggesting FIFA is considering shifting matches to U.S. venues.

The World Cup is scheduled to begin on June 11, 2026, meaning any relocation decision would need to be made in the coming weeks.

**Exact later resolution packet**

The question resolves NO. FIFA did not issue any official announcement on or after April 30, 2026 and before 23:59 UTC June 1, 2026 relocating any of the 13 Mexico-scheduled World Cup matches (Mexico City/Estadio Azteca, Guadalajara/Estadio Akron, Monterrey/Estadio BBVA) to a venue outside Mexico.

Evidence:
- The Wikipedia article for the 2026 FIFA World Cup (last edited May 28, 2026) lists Mexico's three venues and full match schedule unchanged, with no mention of any FIFA relocation of Mexican matches to the US or Canada [02b4e8].
- A Polymarket market specifically tracking "World Cup game relocated away from Mexico?" (page state as of June 2, 2026) explicitly states: "FIFA and Mexican officials have repeatedly confirmed that all 13 matches scheduled for Mexico City, Guadalajara, and Monterrey will proceed at their original venues, with no relocation announcements issued." The market remained open (unresolved YES), confirming no announcement occurred by the question deadline [9500b9].

Context confirming NO: While there was extensive speculation and reports that FIFA was "considering" relocating Mexican matches amid cartel violence following the death of "El Mencho," and a regulatory clause exists that would permit such a move, no FIFA official announcement of an actual relocation was made. Related FIFA actions in this period concerned team base camps, not match venues — e.g., FIFA approved Iran moving its base camp to Mexico but rejected requests to move Iran's matches out of the US; FIFA had "no plans to change the 2026 World Cup schedule." None of these involved moving a Mexican match out of Mexico.

Since no qualifying official FIFA announcement was made by 23:59 UTC June 1, 2026, the resolution criteria specify the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-118. `44ca8582-5f12-5404-ba92-25ba1147a5e6`

- Present date: `2026-05-12 17:21:43.133202`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will any candidate receive more than 40% of the vote in the 2026 Los Angeles mayoral primary on June 2, 2026?

**Resolution criteria**

This question resolves **Yes** if any single candidate receives more than 40.0% of the total votes cast in the City of Los Angeles mayoral primary election held on June 2, 2026. It resolves **No** if no candidate exceeds 40.0%.

**Key definitions:**
- "Primary" refers to the Primary Nominating Election for Mayor of the City of Los Angeles, as defined in the [Los Angeles City Charter, Section 702](https://codelibrary.amlegal.com/codes/los_angeles/latest/laac/0-0-0-68971) and described on [Wikipedia](https://en.wikipedia.org/wiki/2026_Los_Angeles_mayoral_election).
- "Total votes cast" means all valid ballots counted in the mayoral contest, including write-in votes but excluding blank/undervote ballots.
- The 40.0% threshold is strict: exactly 40.00% does not qualify; the candidate must exceed 40.0%.

**Resolution source:** The official certified results from the [Los Angeles County Registrar-Recorder/County Clerk election results page](https://results.lavote.gov/). If certified results are not yet available by July 1, 2026 (11:59 PM Pacific Time), resolution shall be based on the most recent "Semi-Official Results" or "Election Night Results" published by the LA County Registrar-Recorder/County Clerk at https://results.lavote.gov/.

All dates and deadlines in these resolution criteria are in **Pacific Time (PT)**.

**Pre-cutoff background**

The 2026 Los Angeles mayoral primary election is scheduled for June 2, 2026. Incumbent Mayor Karen Bass faces a fragmented field of 13 challengers, including City Councilmember Nithya Raman, reality TV personality Spencer Pratt, Adam Miller, and Rae Huang [2026 Los Angeles mayoral election](https://en.wikipedia.org/wiki/2026_Los_Angeles_mayoral_election).

Under the Los Angeles City Charter (https://codelibrary.amlegal.com/codes/los_angeles/latest/laac/0-0-0-68971), if no candidate receives a majority (more than 50%) of the vote in the primary, the top two vote-getters advance to a runoff election on November 3, 2026 [2026 Los Angeles mayoral election](https://en.wikipedia.org/wiki/2026_Los_Angeles_mayoral_election).

Recent polling as of March 2026 shows [2026 Los Angeles mayoral election](https://en.wikipedia.org/wiki/2026_Los_Angeles_mayoral_election):
- **UCLA poll (March 15–29, 2026):** Bass 25%, Pratt 11%, Raman 9%, Miller 3%, Huang 3%, Other 9%, Undecided 40%.
- **UC Berkeley/LA Times (March 9–15, 2026):** Bass 25%, Raman 17%, Pratt 14%, Huang 8%, Miller 6%, Other 4%, Undecided 26%.
- **Emerson College (March 7–9, 2026):** Bass 19.5%, Pratt 10.2%, Raman 9.3%, Miller 4.2%, Huang 2.9%, Other 3.0%, Undecided 50.9%.

With the leading candidate (Bass) polling at roughly 19–25% and undecided voters ranging from 26% to 51%, there is significant uncertainty about whether any candidate can consolidate enough support to cross the 40% threshold. Bass could gain substantially as undecided voters break her way as the incumbent, but the large and competitive field makes high vote shares difficult to achieve.

The LA County Registrar-Recorder/County Clerk publishes semi-official and certified results after each election at https://results.lavote.gov/.

**Exact later resolution packet**

RESOLUTION: NO (0)

The question asks whether any single candidate received more than 40.0% of the total votes cast in the City of Los Angeles mayoral primary held June 2, 2026. Based on the official CERTIFIED results from the LA County Registrar-Recorder/County Clerk, no candidate came close to 40%.

CERTIFIED RESULTS (not semi-official): The June 2, 2026 Statewide Direct Primary Election results were officially certified by LA County RR/CC Dean C. Logan on June 26, 2026 (announced at https://lacounty.gov/2026/06/26/certified-election-results-for-the-2026-statewide-direct-primary-election/), before the July 1, 2026 deadline specified in the resolution criteria. The official results page (https://results.lavote.gov/text-results/4338) reflects this certified data (last updated 2026-06-26).

OFFICIAL VOTE COUNTS for LOS ANGELES CITY PRIMARY NOMINATING ELECTION – Mayor, from https://results.lavote.gov/text-results/4338 [952152]:
- Karen Ruth Bass: 292,593 votes (34.27%) — LEADING candidate
- Nithya Raman: 247,781 votes (29.02%)
- Spencer Pratt: 217,977 votes (25.53%)
- Adam Miller: 30,008 (3.51%)
- Rae Chen Huang: 25,220 (2.95%)
- Juanita Lopez: 13,033 (1.53%)
- Andrew K. Kim: 6,988 (0.82%)
- Suzy Kim: 6,051 (0.71%)
- Asaad Alnajjar: 4,063 (0.48%)
- Bryant Acosta: 3,471 (0.41%)
- John Logsdon: 3,029 (0.35%)
- Tish Hyman: 1,640 (0.19%)
- Andrej A. Selivra: 1,159 (0.14%)
- Nelson Cheng: 881 (0.10%)

The highest vote share of any candidate was Karen Bass at 34.27%, which is far below the strict 40.0% threshold. Therefore, no candidate exceeded 40.0%, and the question resolves NO.

CORROBORATION: The Wikipedia article on the 2026 Los Angeles mayoral election [22b5c3] reports the same certified figures (Bass 292,593 / 34.3%; Raman 247,781 / 29.0%) and confirms results were certified. Additionally, multiple news outlets reported that Karen Bass and Nithya Raman (the top two) advanced to a November 3, 2026 runoff, which is consistent with no candidate reaching a majority — and, a fortiori, no candidate reaching 40%.

DENOMINATOR CHECK: The resolution criteria define "total votes cast" as all valid ballots in the mayoral contest, including write-ins but excluding blank/undervote ballots. The percentages on the LA County results page are computed on the contest's total votes (excluding undervotes). Even accounting for any minor denominator variation, Bass at 34.27% is nowhere near the 40.0% threshold, so no plausible interpretation changes the outcome.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-119. `32b35b20-8a83-5d2a-8b2e-a8d81190dc73`

- Present date: `2026-05-12 16:36:04.773172`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will President Trump publicly criticize Walmart by name on Truth Social regarding tariff-related price increases between May 10 and July 1, 2026?

**Resolution criteria**

This question resolves YES if, between May 10, 2026 at 00:00 UTC and July 1, 2026 at 23:59 UTC, President Donald Trump publishes at least one official statement that meets ALL of the following criteria:

1. **Platform**: The statement appears on one of the following platforms:
   - Truth Social (https://truthsocial.com/@realDonaldTrump)
   - An official White House press release (https://www.whitehouse.gov/briefing-room/)
   - An official White House transcript of presidential remarks

2. **Names Walmart**: The statement explicitly mentions "Walmart" by name.

3. **Criticizes**: The statement expresses disapproval, blame, or negative judgment directed at Walmart. This includes but is not limited to: accusations of wrongdoing, demands that Walmart change its behavior, warnings or threats, or characterizations of Walmart's actions as harmful, greedy, dishonest, or unfair.

4. **Tariff connection**: The statement explicitly contains at least one of the following words or phrases in relation to Walmart's pricing: "tariff," "tariffs," "duty," "duties," "trade tax," or "trade taxes."

If no such statement is found by July 1, 2026 at 23:59 UTC, the question resolves NO.

**Resolution sources**: Trump's Truth Social profile (https://truthsocial.com/@realDonaldTrump), the White House briefing room (https://www.whitehouse.gov/briefing-room/), and credible news reporting from major outlets (e.g., Reuters at https://www.reuters.com, AP News at https://apnews.com, CNBC at https://www.cnbc.com). The Trump Archive (https://www.thetrumparchive.com/) may also be consulted as a secondary source.

**Pre-cutoff background**

In May 2025, President Trump publicly attacked Walmart by name on Truth Social after the retailer warned during its Q1 FY2026 earnings call (May 15, 2025) that it would need to raise prices due to tariffs. On May 17, 2025, Trump wrote on Truth Social: "Walmart should STOP trying to blame Tariffs as the reason for raising prices throughout the chain," and urged the company to "EAT THE TARIFFS" rather than pass costs to consumers. This confrontation was widely covered by major outlets including Reuters, CNBC, the New York Times, and CNN.

Walmart's Q1 FY2027 earnings call is scheduled for May 21, 2026, at 7:00 a.m. CT, per Walmart's corporate events page (https://corporate.walmart.com/news/events/fy2027-q1-earnings-release). This earnings call is expected to include commentary on pricing, margins, and the impact of trade policy on costs—topics that previously triggered Trump's criticism. If Walmart again attributes price increases to tariffs or trade duties during this call, it could prompt a repeat of the May 2025 confrontation.

The question captures genuine uncertainty: Trump's willingness to publicly criticize a major American retailer depends on the political salience of inflation, Walmart's specific messaging around tariffs, and the broader trade policy environment in mid-2026.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if, between May 10, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), Trump published a statement on Truth Social / an official White House press release / an official WH transcript that (a) names Walmart, (b) criticizes it, and (c) links "tariff(s)/dut(y/ies)/trade tax(es)" to Walmart's pricing. No such 2026-window statement was found; the only such statement on record is the historical May 17, 2025 "EAT THE TARIFFS" post, which the question explicitly excludes.

KEY EVIDENCE FOR THE 2026 WINDOW:

1. The 2026 dynamic was fundamentally different from May 2025. Following a February 2026 Supreme Court decision requiring the government to refund most tariffs (~$160B owed to importers), Walmart's posture in 2026 was cooperative, not confrontational. On its Q1 FY2027 earnings call (May 21, 2026), Walmart said it would use tariff refunds to LOWER prices (reportedly cutting prices on ~7,200 products), rather than blaming tariffs for hikes [a2ff16]. CNBC (May 22, 2026) reported Walmart applied for a tariff refund "and plans to use any money it receives back to invest in lower prices for shoppers," and contained no new Trump criticism of Walmart by name over tariffs in the window [c3a0ab, bd4cf7]. CNBC's May 21, 2026 earnings coverage likewise reported no Trump criticism [464a8e].

2. Although the WSJ noted Walmart planned some tariff-driven price increases in mid-2026 [ea408e], no source documents any Trump statement criticizing Walmart by name over tariffs during May 10–July 1, 2026. This cooperative "use refunds to lower prices" stance was favorable to Trump (commentary even noted Walmart was the only company saying it would use refunds to lower prices), making a critical post unlikely.

3. Trump's actual price-related Truth Social activity in the window did not qualify. His widely covered late-May 2026 post "TRUMP'S MAKING FOOD AFFORDABLE" listed grocery items and, per AP's fact-check, did NOT name Walmart [1fd474]. His June 10, 2026 "I love the inflation" remarks (after CPI hit a 3-year high) also did not name Walmart critically over tariffs.

4. All search results tying Trump + Walmart + tariffs + criticism ("eat the tariffs," "STOP trying to blame Tariffs," "I'll be watching, and so will your customers") trace to the May 17, 2025 incident — the historical event the question instructs to exclude. Contemporaneous 2026 reporting only references that 2025 clash as background.

Because no qualifying statement (naming Walmart, criticizing it, and connecting tariffs to its pricing) appeared on the specified platforms within May 10–July 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-120. `82a5ef9e-4c98-5f0e-b972-dd99c657be88`

- Present date: `2026-05-07 22:32:53.199959`
- Source cutoff boundary: `2026-05-08` (encodes end of UTC day `2026-05-07`)
- Expected resolution: `2026-06-10T00:00:00`

**Question**

Will the United States and Iran announce a formal peace agreement ending the 2026 Iran war by June 10, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 7, 2026, and before June 10, 2026 at 12:00 UTC (the start of the ECB Governing Council monetary policy meeting), the United States and Iran announce a formal peace agreement intended to permanently end the 2026 Iran war.

Specifically, all of the following must be met:

1. **Parties**: The agreement must be announced or signed by authorized representatives of both the United States government (e.g., the President, Secretary of State, or their designated negotiator) and the Iranian government (e.g., the Supreme Leader's office, the President, or the Foreign Minister).

2. **Scope**: The agreement must address the core US-Iran military conflict that began on February 28, 2026 (as described in the Wikipedia article on the 2026 Iran war: https://en.wikipedia.org/wiki/2026_Iran_war). It need not resolve all proxy conflicts but must cover the direct US-Iran hostilities.

3. **Nature of agreement**: The agreement must be described as a "peace agreement," "peace deal," "permanent ceasefire," or "comprehensive ceasefire" — i.e., an accord intended to end hostilities on a permanent or indefinite basis. A temporary ceasefire (https://en.wikipedia.org/wiki/Ceasefire) of defined duration (e.g., "14-day ceasefire," "humanitarian pause") does NOT count, nor does a mere extension of a prior temporary ceasefire. The agreement must explicitly go beyond a time-limited truce.

4. **Verification**: The announcement must be confirmed by at least two of the following sources: Reuters (https://www.reuters.com), Associated Press (https://apnews.com), BBC News (https://www.bbc.com/news), or official US State Department statements (https://www.state.gov).

If no such agreement is announced before June 10, 2026 at 12:00 UTC, the question resolves NO.

**Pre-cutoff background**

On February 28, 2026, the United States and Israel launched military strikes against Iran, initiating the 2026 Iran war [2026 Iran war - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war). The primary combatants are the US and Israel on one side, and Iran along with regional allies including Hezbollah, the Houthis, and the Popular Mobilization Forces on the other [2026 Iran war - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war).

A temporary two-week ceasefire between the US and Iran was brokered by Pakistan beginning April 8, 2026 [2026 Iran war ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire). However, the subsequent "Islamabad Talks" collapsed by April 12, 2026, and the US imposed a naval blockade on Iran [2026 Iran war ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire). A separate ceasefire between Hezbollah and Israel has been in effect since April 16, 2026 [2026 Iran war - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war).

As of May 7, 2026, the conflict is in a stalemate characterized by a "dual blockade" — the US Navy blockading Iranian ports and Iran blockading the Persian Gulf [2026 Iran war - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war). No permanent peace agreement has been reached [2026 Iran war ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire). Reports indicate back-channel negotiations may be accelerating, with Iranian officials hoping Trump will want to end the conflict before a summit with Xi Jinping on May 14-15, 2026. However, Trump has reportedly said he is "not satisfied" with Iran's latest peace proposal.

The ECB's next monetary policy meeting is scheduled for June 10-11, 2026. ECB policymakers have explicitly noted that the rate outlook "could change if a resolution to the Iran conflict causes energy prices to drop to pre-war levels" (Reuters, April 30, 2026). A peace agreement before this meeting would thus have significant implications for European monetary policy.

For the definition of a "peace agreement," this question uses the concept as described by the United Nations Peacemaker (https://peacemaker.un.org/): a formal, written accord between the principal warring parties that establishes terms to end hostilities on a permanent or indefinite basis, as distinct from a temporary ceasefire (https://en.wikipedia.org/wiki/Ceasefire), which is a temporary suspension of fighting.

**Exact later resolution packet**

The question resolves NO. It required that, on or after May 7, 2026 and BEFORE June 10, 2026 at 12:00 UTC, authorized representatives of both the US and Iranian governments announce/sign a formal permanent peace agreement (or "comprehensive/permanent ceasefire") covering the direct US–Iran conflict, verified by at least two of Reuters/AP/BBC/State Dept.

None of these conditions were met within the window:

1. No agreement existed by June 10, 2026 — the war was still actively being fought. Per the Wikipedia "Timeline of the 2026 Iran war," Iran ended peace talks on June 1, 2026; on June 9 a US AH-64 Apache collided with an Iranian drone, triggering US strikes; and on June 10 Iran launched strikes at the US Fifth Fleet and US bases while the US struck Iranian targets — i.e., open hostilities, not peace, on the deadline date [Timeline of the 2026 Iran war - Wikipedia](https://en.wikipedia.org/wiki/Timeline_of_the_2026_Iran_war).

2. The negotiations timeline confirms the deal came AFTER the deadline. Per Wikipedia "2025–2026 Iran–United States negotiations," a preliminary framework/MOU was only reached on June 15, 2026, and the signing (the "Islamabad Memorandum") occurred June 17, 2026 [2025–2026 Iran–United States negotiations - Wikipedia](https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations).

3. As of May 28, 2026, only a draft 60-day MOU had been reached by negotiators; it still lacked Trump's final approval and Iran's confirmation — not a formal announced agreement by both governments [U.S. and Iran reach deal but need Trump's final approval, officials say](https://www.axios.com/2026/05/28/iran-peace-deal-trump-approval).

4. The two required verification sources both date the deal to after June 10:
   - Reuters reported Trump saying "the deal's all signed" on June 15, 2026, describing a memorandum of understanding that extends the ceasefire for a 60-day negotiation period — i.e., an interim framework, not a permanent peace accord [Trump says the US and Iran have signed a deal to end the war](https://www.reuters.com/world/iran-war-live-trump-says-us-tehran-have-reached-peace-deal-2026-06-15/).
   - BBC reported the US and Iranian presidents signed the initial deal on June 18, 2026, again a memorandum committing to negotiate a final deal within a maximum of 60 days [US and Iranian presidents sign deal aiming to end war - BBC](https://www.bbc.com/news/articles/crr8z4z2er9o).

Both the timing (all announcements/signings occurred June 14–18, 2026, after the June 10 12:00 UTC cutoff) and the nature of the eventual agreement (a 60-day interim MOU/ceasefire extension rather than a permanent peace deal) independently fail the resolution criteria. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-121. `a60885bc-7464-5844-abe0-7a49c0c4d6c4`

- Present date: `2026-05-01 17:43:22.872565`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Russian Africa Corps forces re-establish a military presence in Kidal, Mali, by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 (00:00 UTC) and before June 1, 2026 (23:59 UTC), credible reporting confirms that the Russian Africa Corps has re-established a military presence in Kidal, Mali. It resolves **No** otherwise.

**Definition of "Russian Africa Corps":** The Russian Africa Corps (formerly associated with the Wagner Group) refers to the Russian state-controlled mercenary force operating in Mali under the authority of the Russian Defence Ministry. This excludes the Malian Armed Forces (FAMa) and any other non-Russian armed groups, even if operating alongside Russia. The presence must be attributed specifically to Africa Corps personnel or units.

**Definition of "military presence":** At least one of the following observable indicators must be confirmed:
- Stationing of identifiable Africa Corps personnel (uniformed troops, military advisors, or mercenaries) within the city limits of Kidal;
- Control or occupation of specific infrastructure in Kidal (e.g., the airport, military camp, or government buildings) by Africa Corps forces;
- Official Russian or Malian government statements confirming Africa Corps deployment to Kidal.

**Verification sources:** Resolution will be based on reporting from at least one of the following credible sources:
- Reuters (https://www.reuters.com/world/africa/)
- Agence France-Presse / AFP (https://www.france24.com/en/africa/)
- Associated Press (https://apnews.com/hub/africa)
- ACLED conflict data (https://acleddata.com/data-export-tool/)
- The Guardian Africa coverage (https://www.theguardian.com/world/africa)

If none of these sources report on Africa Corps presence in Kidal by June 1, 2026 (23:59 UTC), the question resolves **No**.

**Pre-cutoff background**

During the weekend of April 25–26, 2026, the town of Kidal in northern Mali fell to an offensive led by a West African al-Qaeda affiliate and Tuareg-dominated separatist groups [https://www.usnews.com/news/world/articles/2026-04-29/analysis-mali-turmoil-threatens-russian-push-for-influence-and-mineral-wealth-in-africa](https://www.usnews.com/news/world/articles/2026-04-29/analysis-mali-turmoil-threatens-russian-push-for-influence-and-mineral-wealth-in-africa). The Russian Africa Corps—a mercenary force controlled by the Russian Defence Ministry with approximately 2,000 troops in Mali [https://www.usnews.com/news/world/articles/2026-04-29/analysis-mali-turmoil-threatens-russian-push-for-influence-and-mineral-wealth-in-africa](https://www.usnews.com/news/world/articles/2026-04-29/analysis-mali-turmoil-threatens-russian-push-for-influence-and-mineral-wealth-in-africa)—was forced to withdraw from the town. While Russia's defence ministry claimed its troops fought for over 24 hours while surrounded, local reports indicated the Africa Corps negotiated an exit with the assistance of Algerian mediators [https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns](https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns).

Kidal is strategically significant: Russian forces had helped the Malian junta recapture it in 2023 [https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns](https://www.theguardian.com/world/2026/apr/28/russia-claims-its-africa-corps-group-prevented-coup-in-mali-after-rebels-seize-towns). In response to its loss, Russia has deployed helicopter gunships and strategic bombers to assist the Malian military [https://www.usnews.com/news/world/articles/2026-04-29/analysis-mali-turmoil-threatens-russian-push-for-influence-and-mineral-wealth-in-africa](https://www.usnews.com/news/world/articles/2026-04-29/analysis-mali-turmoil-threatens-russian-push-for-influence-and-mineral-wealth-in-africa). However, analysts have questioned the Africa Corps' battlefield effectiveness, and it remains unclear whether a counteroffensive to retake Kidal can succeed within the coming weeks [https://www.usnews.com/news/world/articles/2026-04-29/analysis-mali-turmoil-threatens-russian-push-for-influence-and-mineral-wealth-in-africa](https://www.usnews.com/news/world/articles/2026-04-29/analysis-mali-turmoil-threatens-russian-push-for-influence-and-mineral-wealth-in-africa).

As of April 30, 2026, Kidal remains under rebel control, with no confirmed Russian Africa Corps presence in the town.

**Exact later resolution packet**

The question resolves NO. It asked whether the Russian Africa Corps would re-establish a military presence in Kidal, Mali between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), as confirmed by one of five approved sources (Reuters, AFP/France 24, AP, ACLED, or The Guardian).

Background: Africa Corps withdrew from Kidal around April 26–27, 2026 after the FLA/JNIM offensive, with the Reuters-confirmed withdrawal ("Russia's Africa Corps confirms withdrawal from Mali's Kidal", 2026-04-27). Kidal then fell under rebel (Azawad Liberation Front) control.

Key approved-source evidence within the resolution window:
- The Guardian, "Mali's forces target rebel alliance in junta's fight to keep power" (2026-05-15) confirms that as of mid-May, government forces (despite the support of 2,000–2,500 Russian mercenaries) had "failed to retake much of the territory lost last month," and that the Africa Corps were withdrawing from outlying posts to reinforce Bamako's defences. The former Africa Corps barracks in Kidal were shown under rebel control, with rebel fighters in the town [Mali's forces target rebel alliance in junta's fight to keep power](https://www.theguardian.com/world/2026/may/15/mali-airstrikes-rebel-alliance-separatists).
- This is corroborated by CNN (2026-05-10), which states Kidal "returns to rebel hands" and the FLA declared the town "free," with no indication of any Russian return [Rebels jeered Putin's Africa Corps out of a key Sahel town. Now his ...](https://www.cnn.com/2026/05/10/africa/putin-africa-corps-kidal-mali-intl-cmd).

No approved verification source (Reuters, AFP/France 24, AP, ACLED, or The Guardian) reported the re-establishment of an Africa Corps presence in Kidal during the window. A social-media (Instagram) claim dated May 6 alleged the Malian Army "fully controls Kidal," but (a) it is not an approved source and (b) it refers to FAMa, which the resolution criteria explicitly exclude — the presence must be specifically attributed to Russian Africa Corps personnel/units. The Guardian's May 15 reporting also contradicts any such full recapture, showing Kidal still under rebel control.

Because none of the three required indicators (Africa Corps personnel stationed within Kidal city limits, Africa Corps control of specific Kidal infrastructure, or official Russian/Malian government statements confirming Africa Corps deployment to Kidal) were confirmed by an approved source before June 1, 2026 (23:59 UTC), the question resolves NO.

URLs used:
- The Guardian: https://www.theguardian.com/world/2026/may/15/mali-airstrikes-rebel-alliance-separatists [Mali's forces target rebel alliance in junta's fight to keep power](https://www.theguardian.com/world/2026/may/15/mali-airstrikes-rebel-alliance-separatists)
- CNN (corroborating, non-approved): https://www.cnn.com/2026/05/10/africa/putin-africa-corps-kidal-mali-intl-cmd [Rebels jeered Putin's Africa Corps out of a key Sahel town. Now his ...](https://www.cnn.com/2026/05/10/africa/putin-africa-corps-kidal-mali-intl-cmd)
- Reuters (withdrawal context): https://www.reuters.com/world/africa/russias-africa-corps-confirms-withdrawal-malis-kidal-2026-04-27/

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-122. `987d2afa-d57c-55fd-aba5-1121bac875c0`

- Present date: `2026-05-16 16:30:50.564395`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Italian Constitutional Court declare any provision of Law 74/2025 unconstitutional in the joined Campobasso/Mantua proceedings, with a ruling issued on or after May 12, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (00:00 CEST) and on or before July 1, 2026 (23:59 CEST), the Italian Constitutional Court (Corte Costituzionale) publishes a judgment (sentenza) declaring any provision of Law No. 74/2025 unconstitutional (illegittimità costituzionale) in the joined proceedings originating from the courts of Campobasso and Mantua scheduled for hearing on June 9, 2026. The March 12, 2026 ruling rejecting the Turin challenge does not count toward resolution.

This question resolves **No** if, by July 1, 2026 (23:59 CEST):
- The Court upholds the law as constitutional;
- The Court declares the challenges inadmissible or unfounded;
- The Court issues only an "admonitory" ruling (monito) without a formal declaration of unconstitutionality; or
- No ruling on these proceedings has been published.

**Clarifications:**
- A **partial declaration of unconstitutionality** (e.g., striking down one provision while upholding others, or an "interpretive" declaration that a provision is unconstitutional insofar as it is interpreted in a certain way — sentenza interpretativa di accoglimento) **does** count as a Yes resolution.
- A mere admonitory ruling (monito), in which the Court signals concerns but does not formally declare any provision unconstitutional, does **not** count as a Yes resolution.
- The "Mantua referral" refers to the ordinanza from the Tribunale di Mantova and the "Campobasso referrals" refer to the two ordinanze from the Tribunale di Campobasso, all challenging provisions of Law 74/2025 and consolidated for the June 9, 2026 hearing.

**Primary resolution source:** The official website of the Italian Constitutional Court at [https://www.cortecostituzionale.it/](https://www.cortecostituzionale.it/), specifically the decisions/pronunce section. Secondary confirmation may be obtained from credible legal news sources such as Mondaq, Mazzeschi, or major Italian legal publications.

**Pre-cutoff background**

In 2025, Italy enacted Law No. 74/2025 (formerly Decree-Law 36/2025), which introduced significant restrictions on the recognition of Italian citizenship by descent (jure sanguinis), including a two-generation limit and requirements for a "genuine connection" with Italy.

On March 12, 2026, the Italian Constitutional Court rejected a challenge originating from the Court of Turin, declaring it "partly inadmissible" and "partly unfounded," confirming that the restrictions introduced by Law 74/2025 remain valid and compatible with the Italian Constitution [https://www.boccadutri.com/constitutional-court-2026-italian-citizenship-descent/](https://www.boccadutri.com/constitutional-court-2026-italian-citizenship-descent/).

However, separate referrals from the courts of Campobasso (two proceedings) and Mantua (one proceeding) raise broader constitutional grounds than the Turin challenge [Italian Citizenship: Constitutional Court joins Campobasso and ...](https://www.mazzeschi.it/italian-citizenship-constitutional-court-joins-campobasso-and-mantua-cases-hearing-set-for-june-9-2026/). These include: (1) whether citizenship acquired by descent is a right existing at birth that cannot be retroactively removed; (2) whether the law violates equality principles; (3) whether emergency decree procedures were used appropriately; (4) compatibility with EU law; and (5) whether the restrictions are proportionate and reasonable [https://www.mondaq.com/italy/investment-immigration/1783590/june-9-constitutional-court-hearing-on-italian-citizenship-what-foreign-applicants-need-to-know](https://www.mondaq.com/italy/investment-immigration/1783590/june-9-constitutional-court-hearing-on-italian-citizenship-what-foreign-applicants-need-to-know) [Italian Citizenship: Constitutional Court joins Campobasso and ...](https://www.mazzeschi.it/italian-citizenship-constitutional-court-joins-campobasso-and-mantua-cases-hearing-set-for-june-9-2026/).

The Constitutional Court has consolidated these three proceedings into a single public hearing scheduled for June 9, 2026, at 9:30 AM (CEST) in Rome [Italian Citizenship: Constitutional Court joins Campobasso and ...](https://www.mazzeschi.it/italian-citizenship-constitutional-court-joins-campobasso-and-mantua-cases-hearing-set-for-june-9-2026/). Specific case or ordinanza numbers for these referrals have not been identified in publicly available English-language sources [Italian Citizenship: Constitutional Court joins Campobasso and ...](https://www.mazzeschi.it/italian-citizenship-constitutional-court-joins-campobasso-and-mantua-cases-hearing-set-for-june-9-2026/).

As of May 12, 2026, Law 74/2025 remains in full force following the March 12 ruling. The June 9 hearing represents the next opportunity for the Court to rule on the law's constitutionality, this time on broader grounds than those previously considered.

**Exact later resolution packet**

The question resolves NO.

**Antecedent / setup:** The Italian Constitutional Court did hold the consolidated public hearing on the Campobasso and Mantua proceedings challenging Law 74/2025 on June 9, 2026. These are the correct joined proceedings: ordinanza n. 4/2026 (Tribunale di Mantova) and ordinanze nn. 40/2026 and 41/2026 (Tribunale di Campobasso), all challenging Article 3-bis of Law 91/1992 as introduced by Law 74/2025 (Decreto Tajani). This is distinct from the earlier Turin challenge (ordinanza 167/2025 Torino), which was decided by sentenza n. 63/2026, deposited April 30, 2026, and declared "non fondata" (unfounded) — that decision is both outside the resolution window and about a different referral, so it does not count [Italian citizenship: Constitutional Court hearing held June 9th about ...](https://www.mazzeschi.it/italian-citizenship-constitutional-court-hearing-held-june-9th-about-legitimacy-of-new-citizenship-rules/) [Italian Constitutional Court: June 9, 2026 Hearing](https://www.apriglianos.com/en/italian-constitutional-court-hearing-of-june-9-2026-on-citizenship-by-descent-what-happened-and-when-the-ruling-is-expected/).

**Core finding — no qualifying ruling published in the window:** After the June 9, 2026 hearing, the Court reserved its decision. As of June 11–12, 2026, no decision on the Campobasso/Mantua proceedings had been announced or published, and the ruling was expected only "between mid-July and September 2026" [Italian Constitutional Court: June 9, 2026 Hearing](https://www.apriglianos.com/en/italian-constitutional-court-hearing-of-june-9-2026-on-citizenship-by-descent-what-happened-and-when-the-ruling-is-expected/), with Mazzeschi similarly reporting that "A decision is expected in the short term, but there is no fixed timeframe for its publication" and that no official press release anticipating the outcome had been issued [Italian citizenship: Constitutional Court hearing held June 9th about ...](https://www.mazzeschi.it/italian-citizenship-constitutional-court-hearing-held-june-9th-about-legitimacy-of-new-citizenship-rules/). Because the resolution window closes July 1, 2026 (23:59 CEST), and no sentenza declaring any provision of Law 74/2025 unconstitutional in these proceedings was published by that date, the "No ruling on these proceedings has been published" branch of the No criteria applies.

**Ruling out the one document that was published in-window:** The only Constitutional Court pronouncement tied to these proceedings that was published within the window is ordinanza n. 102/2026 (deliberated June 8, 2026, deposited/"Depositata in Cancelleria il 9 giugno 2026"). However, this is a purely procedural order in the joined proceedings (reg. ord. 40 and 41 of 2026) that only declared inadmissible the interventions of third parties (Confederazione degli Italiani nel mondo and certain individuals). It did NOT address the merits and did NOT declare any provision of Law 74/2025 unconstitutional [Corte Costituzionale - Sito ufficiale](https://www.cortecostituzionale.it/scheda-pronuncia/2026/102). Therefore it does not trigger a YES.

Since no partial or interpretive declaration of unconstitutionality (sentenza interpretativa di accoglimento) — and indeed no merits decision at all — was published on the Campobasso/Mantua proceedings between May 12 and July 1, 2026, the question resolves NO.

Primary source (Italian Constitutional Court official site): https://www.cortecostituzionale.it/scheda-pronuncia/2026/102 (procedural ordinanza only) [Corte Costituzionale - Sito ufficiale](https://www.cortecostituzionale.it/scheda-pronuncia/2026/102). Secondary legal sources confirming the decision was reserved with publication expected after July 1: https://www.apriglianos.com/en/italian-constitutional-court-hearing-of-june-9-2026-on-citizenship-by-descent-what-happened-and-when-the-ruling-is-expected/ [Italian Constitutional Court: June 9, 2026 Hearing](https://www.apriglianos.com/en/italian-constitutional-court-hearing-of-june-9-2026-on-citizenship-by-descent-what-happened-and-when-the-ruling-is-expected/) and https://www.mazzeschi.it/italian-citizenship-constitutional-court-hearing-held-june-9th-about-legitimacy-of-new-citizenship-rules/ [Italian citizenship: Constitutional Court hearing held June 9th about ...](https://www.mazzeschi.it/italian-citizenship-constitutional-court-hearing-held-june-9th-about-legitimacy-of-new-citizenship-rules/).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-123. `1e8bebfc-0bcb-5419-a625-2cb21bc7c345`

- Present date: `2026-05-14 05:37:47.338118`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Wisconsin Supreme Court issue a decision on the merits in Wisconsin Voter Alliance v. Secord (II) by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the Wisconsin Supreme Court publishes a written opinion or order on or after May 12, 2026, and by 11:59 PM Central Time on July 1, 2026, that substantively addresses the core legal question of whether "Notices of Voting Eligibility" (guardianship-related voter incompetency determinations) are subject to public records disclosure under Wisconsin law.

This question resolves **No** if any of the following occur by the deadline:
1. The court has not issued any decision in the case.
2. The court issues a ruling that disposes of the case on procedural grounds only (e.g., dismissal for standing, mootness, or jurisdictional defects) or remands it to a lower court without reaching the substantive public records question.

A "decision on the merits" means a final written opinion or order that substantively resolves the legal dispute over whether the records at issue must be disclosed. A decision that addresses the merits but also remands for further proceedings still counts as a merits decision if it resolves the core legal question.

**Resolution source:** The official Wisconsin Supreme Court opinions page at https://www.wicourts.gov/opinions/supreme.jsp, supplemented by the opinions search tool at https://www.wicourts.gov/opinions/search.htm.

**Pre-cutoff background**

The Wisconsin Supreme Court heard oral arguments on April 21, 2026, in *Wisconsin Voter Alliance v. Kristina Secord* (Secord II), a case concerning whether court-issued "Notices of Voting Eligibility"—documents determining that a person is incompetent to vote under guardianship proceedings—are public records subject to disclosure under Wisconsin's open records law [https://www.wpr.org/news/wisconsin-supreme-court-incompetency-voter-eligibility-heuer](https://www.wpr.org/news/wisconsin-supreme-court-incompetency-voter-eligibility-heuer). The Wisconsin Voter Alliance seeks access to these records, while opponents argue they are protected by privacy laws and statutory exceptions.

This is the second time the case has reached the Wisconsin Supreme Court. In the first iteration (Secord I), the court did not rule on the merits, instead resolving the case on narrower grounds related to conflicting lower court rulings [https://www.wpr.org/news/wisconsin-supreme-court-incompetency-voter-eligibility-heuer](https://www.wpr.org/news/wisconsin-supreme-court-incompetency-voter-eligibility-heuer).

As of May 12, 2026, the court has heard oral arguments but has not yet issued an opinion. Wisconsin Supreme Court opinions are typically released during the court's September–June term, with opinions posted at approximately 8:30 AM CDT on the day of release. The court generally takes weeks to months after oral argument to issue decisions. Given approximately 10 weeks between oral argument and July 1, 2026, there is meaningful uncertainty about whether the court will issue a merits opinion within this window—particularly given the prior history of avoiding the merits in Secord I.

**Exact later resolution packet**

The question resolves NO. It asks whether the Wisconsin Supreme Court issued a merits decision in Wisconsin Voter Alliance v. Kristina Secord (Secord II, case No. 2023AP36 / 2023AP000036) substantively addressing whether "Notices of Voting Eligibility" are subject to public-records disclosure, published on/after May 12, 2026 and by 11:59 PM CT July 1, 2026.

Key facts and evidence:
- Oral arguments in Secord II were held April 21, 2026 (this was the case's second trip to the Supreme Court; Secord I, decided as 2025 WI 2 in Jan 2025, resolved on procedural grounds—that District II failed to follow procedure for conflicting appellate decisions—not the merits).
- The official resolution source, the Wisconsin Supreme Court opinions page (wicourts.gov/opinions/supreme.jsp) and its search tool, contains NO merits opinion in this case within the May 12–July 1, 2026 window [a6242c, 0639aa].
- The Wisconsin Supreme Court "opinions scheduled for release" memo showed only one memorandum scheduled for release on June 30, 2026, and it was NOT case 2023AP36; no Secord opinion was scheduled through the July 1 deadline [46b863].
- The State Court Report case tracker still listed the case as "Pending," with the latest docket activity being briefing in early 2026 (principal brief Feb 9, 2026; amicus brief Mar 13, 2026) and no post-argument decision [48d974].
- The Votebeat feature (last updated June 1, 2026) confirmed the court had heard oral arguments but had issued no merits decision [04a386].

Because no written opinion or order resolving the core public-records question was published by the July 1, 2026 deadline (satisfying the NO condition "The court has not issued any decision in the case"), the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-124. `e0385127-5ec1-592f-8846-2c8b36ffe68f`

- Present date: `2026-05-29 04:55:07.046399`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Carla Zambelli be physically transferred to Brazilian custody by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if Carla Zambelli (https://en.wikipedia.org/wiki/Carla_Zambelli) is physically transferred to Brazilian custody on or after May 12, 2026 (00:00 UTC), and on or before July 1, 2026 (23:59 UTC). It resolves **No** otherwise.

**Definition of "physically transferred":** Zambelli is considered physically transferred when at least one of the following has occurred:
- She has boarded an aircraft under the guard or escort of Brazilian or Italian law enforcement officials for the purpose of extradition to Brazil; OR
- She has been formally received by Brazilian authorities (e.g., the Brazilian Federal Police) on Brazilian soil or at a designated handover point.

**Definition of "Brazilian custody":** Zambelli is in Brazilian custody when she is under the physical control and legal authority of Brazilian government officials, including but not limited to the Brazilian Federal Police (Polícia Federal).

The transfer must occur on or after May 12, 2026 (00:00 UTC).

**Verification sources:** Resolution will be determined based on official statements from the Italian Ministry of Justice (https://www.giustizia.it/) or the Brazilian Federal Police (https://www.gov.br/pf/), or credible reporting from at least one of the following news agencies/outlets:
- Reuters (https://www.reuters.com/)
- Associated Press (https://apnews.com/)
- Agência Brasil (https://agenciabrasil.ebc.com.br/)
- G1/Globo (https://g1.globo.com/)
- BBC News Brasil (https://www.bbc.com/portuguese)
- Folha de S.Paulo (https://www1.folha.uol.com.br/)

**Pre-cutoff background**

Carla Zambelli is a former Brazilian federal deputy (PL-SP) who fled Brazil in May 2024 after being convicted by the Brazilian Supreme Federal Court (STF). She was arrested in Rome, Italy on July 29, 2025, and has been detained there since [Defesa de Zambelli apresenta recurso na Itália para evitar extradição](https://agenciabrasil.ebc.com.br/justica/noticia/2026-04/defesa-de-zambelli-apresenta-recurso-na-italia-para-evitar-extradicao).

On March 26, 2026, the Court of Appeal of Rome authorized her extradition to Brazil [Itália decide extraditar Carla Zambelli; o que acontece agora - BBC](https://www.bbc.com/portuguese/articles/clyj99m9w3vo). On April 16, 2026, a second Italian court ruling also favored extradition in a separate case involving a firearm charge. As of April 2026, her defense filed an appeal with the Court of Cassation (Italy's highest court), which is the final judicial instance [Defesa de Zambelli apresenta recurso na Itália para evitar extradição](https://agenciabrasil.ebc.com.br/justica/noticia/2026-04/defesa-de-zambelli-apresenta-recurso-na-italia-para-evitar-extradicao). The Court of Cassation hearing is scheduled for May 22, 2026.

Even if the Court of Cassation upholds the extradition, the final administrative decision on whether to physically hand Zambelli over rests with the Italian Minister of Justice, Carlo Nordio [Defesa de Zambelli apresenta recurso na Itália para evitar extradição](https://agenciabrasil.ebc.com.br/justica/noticia/2026-04/defesa-de-zambelli-apresenta-recurso-na-italia-para-evitar-extradicao). Nordio has previously blocked extraditions on discretionary grounds (e.g., denying Argentina's request for a priest). Zambelli has attempted to influence Nordio through a hunger strike and direct correspondence. The Brazilian Federal Police have reportedly been planning logistics for a potential transfer by chartered aircraft.

Multiple sequential steps must occur before transfer: (1) Court of Cassation ruling (May 22), (2) Nordio's ministerial authorization, and (3) physical logistics of transfer — making the timeline to July 1, 2026 tight but not impossible.

**Exact later resolution packet**

The question resolves NO. Carla Zambelli was NOT physically transferred to Brazilian custody within the window of May 12, 2026 (00:00 UTC) through July 1, 2026 (23:59 UTC). Instead, the extradition was definitively blocked and she was released.

Key evidence, all from resolution-approved sources:

1. Agência Brasil ("Zambelli é libertada na Itália após tribunal negar extradição," dated 2026-05-22, https://agenciabrasil.ebc.com.br/justica/noticia/2026-05/zambelli-e-libertada-na-italia-apos-tribunal-negar-extradicao): On May 22, 2026, the Italian Court of Cassation (Italy's highest judicial instance) denied Brazil's request to extradite Zambelli. As a result, she was released from prison in Italy. The court found errors in the prior decisions that had authorized the extradition [Zambelli é libertada na Itália após tribunal negar extradição](https://agenciabrasil.ebc.com.br/justica/noticia/2026-05/zambelli-e-libertada-na-italia-apos-tribunal-negar-extradicao).

2. BBC News Brasil ("Em reviravolta, Carla Zambelli é solta na Itália após Justiça anular...," dated 2026-05-22, https://www.bbc.com/portuguese/articles/ckgplj8yp0yo): On May 22, 2026, the Italian Supreme Court of Cassation annulled the extradition of Zambelli to Brazil and ordered her immediate release; she was freed from detention that same evening. She was not transferred to Brazilian custody [Em reviravolta, Carla Zambelli é solta na Itália após Justiça anular ... - BBC](https://www.bbc.com/portuguese/articles/ckgplj8yp0yo).

3. G1/Globo ("Entenda a condenação de Zambelli...," dated 2026-05-22, https://g1.globo.com/politica/noticia/2026/05/22/carla-zambelli-entenda-extraditacao-italia.ghtml): On May 22, 2026, the Court of Cassation ruled against the extradition, reversing the Court of Appeal, and ordered her release from the women's penitentiary near Rome. The judicial process was considered exhausted, and she was not transferred to Brazilian custody [Entenda a condenação de Zambelli no Brasil e pedido de extradição - G1](https://g1.globo.com/politica/noticia/2026/05/22/carla-zambelli-entenda-extraditacao-italia.ghtml).

Because the extradition was judicially annulled (a "no remand" quashing at the final judicial instance), the Italian Minister of Justice could not authorize a surrender, and Zambelli was set free rather than handed over. Additional confirmation that no transfer occurred by July 1: reporting from late June 2026 (e.g., Folha de S.Paulo, June 2026; Agência Brasil, June 2026) shows the Brazilian government (AGU) was still filing renewed appeals/manifestations in Italy attempting to secure her extradition — behavior that would be nonsensical had she already been transferred. This is consistent with the definition of "physically transferred" (boarding an escorted aircraft or being received by Brazilian authorities) not having been met at any point in the window.

Therefore, none of the "physically transferred to Brazilian custody" conditions were satisfied between May 12 and July 1, 2026, and the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-125. `c291b187-a2de-5dfc-af3b-6d61a5c703f8`

- Present date: `2026-05-03 01:51:49.425831`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Arizona SB 1347 (requiring insurance coverage for iatrogenic infertility) be signed into law by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if Arizona SB 1347 (57th Legislature, 2nd Regular Session — "health insurance; fertility preservation; coverage") becomes law on or after May 1, 2026, and on or before June 1, 2026 (11:59 PM US Mountain Standard Time). "Becomes law" means either: (a) the Governor of Arizona signs the bill into law, or (b) the bill becomes law without the Governor's signature pursuant to Arizona constitutional provisions (Article V, Section 7), or (c) a gubernatorial veto is overridden by the legislature.

The question resolves as **No** if the bill has not become law by June 1, 2026, including if it was vetoed (without override), failed in either chamber, or simply was not acted upon by the Governor by that date.

"Iatrogenic infertility" is defined per the bill text as "an impairment of fertility that is caused directly or indirectly by surgery, chemotherapy, radiation or other medical treatment" (https://www.azleg.gov/legtext/57leg/2R/bills/sb1347p.pdf). See also: https://en.wikipedia.org/wiki/Iatrogenesis.

**Resolution source:** The official Arizona State Legislature bill tracking page at https://apps.azleg.gov/BillStatus/BillOverview/84896, which displays the Governor's action on the bill. Secondary confirmation may come from the Governor's office at https://azgovernor.gov or credible reporting (e.g., Arizona Capitol Times, AP, Reuters).

**Pre-cutoff background**

Arizona Senate Bill 1347 (57th Legislature, 2nd Regular Session) would require health insurers that issue, amend, or renew insurance policies on or after January 1, 2027, to provide coverage for standard fertility preservation services for insured individuals of reproductive age who are diagnosed with cancer and whose medically necessary treatment is likely to cause iatrogenic infertility [SB1347 - 572R - Senate Fact Sheet - Arizona Legislature](https://www.azleg.gov/legtext/57leg/2R/summary/S.1347FIN_ASPASSEDCOW.DOCX.htm). "Iatrogenic infertility" is defined in the bill as "an impairment of fertility that is caused directly or indirectly by surgery, chemotherapy, radiation or other medical treatment" (see bill text: https://www.azleg.gov/legtext/57leg/2R/bills/sb1347p.pdf). For a general medical definition, see also https://en.wikipedia.org/wiki/Iatrogenesis.

As of early 2026, the bill passed through the Senate Finance Committee with a 4-1-2 "Do Pass Amended" vote on February 16, 2026, and underwent Committee of the Whole amendments in the Senate [SB1347 - 572R - Senate Fact Sheet - Arizona Legislature](https://www.azleg.gov/legtext/57leg/2R/summary/S.1347FIN_ASPASSEDCOW.DOCX.htm). By March 2026, it had advanced to House committees, with House summaries dated March 9 and March 13, 2026. As of May 2, 2026, the bill appears to still be progressing through the legislative process. Governor Katie Hobbs has been signing bills selectively — a recent legislative action update showed her signing HB2072 in April 2026, with reports of a prior moratorium on bill signings [Governor Katie Hobbs Legislative Action Update](https://azgovernor.gov/office-arizona-governor/news/2026/04/governor-katie-hobbs-legislative-action-update).

The Arizona legislative session typically ends in late May or June. The bill has bipartisan appeal as a narrowly scoped fertility preservation measure for cancer patients (not a full IVF mandate), which improves its chances in a Republican-leaning legislature. However, uncertainty remains around whether it will clear both chambers and receive the governor's signature before the session ends. A reasonable probability estimate falls in the 30-70% range given: (1) the bill has cleared multiple committee hurdles, (2) it has narrower scope than broader fertility mandates, (3) the governor's signing patterns and any moratorium create uncertainty, and (4) the legislative calendar is tight.

**Exact later resolution packet**

The question resolves NO. Arizona SB 1347 (57th Legislature, 2nd Regular Session — "health insurance; fertility preservation; coverage") did not become law on or before June 1, 2026.

Evidence from the official Arizona State Legislature bill status page (https://apps.azleg.gov/BillStatus/BillOverview/84896): the bill passed the Senate on 03/02/2026 and was transmitted to the House, where it cleared the House Health & Human Services committee (03/16/2026) but then stalled — there is no record of it passing the House floor, being transmitted to the Governor, or receiving any gubernatorial action [https://apps.azleg.gov/BillStatus/BillOverview/84896](https://apps.azleg.gov/BillStatus/BillOverview/84896).

This is corroborated by BillTrack50 (https://www.billtrack50.com/billdetail/1946298), which lists the bill's status as "Dead," with its last recorded action on or around March 17, 2026 (a Senate floor amendment), and no record of House passage or a Governor's signature [AZ SB1347 | BillTrack50](https://www.billtrack50.com/billdetail/1946298).

Because the bill never reached the Governor, none of the three "becomes law" paths in the resolution criteria occurred: (a) no gubernatorial signature, (b) no becoming law without signature under Article V, Section 7, and (c) no veto override. The bill was simply not enacted before the June 1, 2026 deadline, which the resolution criteria explicitly state resolves the question NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-126. `51ed7fc0-4e65-5768-9722-e934d6d67122`

- Present date: `2026-05-02 19:33:28.217396`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the US announce the inclusion of refined copper cathode (HTS 7403.11.00) in Section 232 tariffs by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 1, 2026, and on or before June 1, 2026 (11:59 PM UTC), an official U.S. government announcement is published indicating that refined copper cathode—defined as products classified under Harmonized Tariff Schedule (HTS) heading 7403.11.00 ("Cathodes and sections of cathodes" of refined copper, per https://hts.usitc.gov/search?query=7403.11.00)—will be subject to Section 232 tariffs at any rate greater than 0%.

The announcement must appear on an official U.S. government source, specifically one of the following:
- The White House (https://www.whitehouse.gov/presidential-actions/)
- The Federal Register (https://www.federalregister.gov/)
- The Department of Commerce (https://www.commerce.gov/)

The tariff need not have taken effect by June 1, 2026; an official announcement or proclamation of the inclusion is sufficient. If no such announcement is published by 11:59 PM UTC on June 1, 2026, the question resolves as **No**.

**Pre-cutoff background**

In August 2025, President Trump imposed 50% tariffs on semi-finished copper products and copper-intensive derivative products under Section 232 of the Trade Expansion Act of 1962 (19 U.S.C. § 1862). Refined copper input materials—including copper cathodes (HTS 7403.11.00), ores, concentrates, mattes, anodes, and scrap—were explicitly excluded from these tariffs [Section 232 National Security Tariffs on Copper Imports](https://www.congress.gov/crs-product/IN12614).

On April 2, 2026, the White House issued a new proclamation titled "Strengthening Actions Taken to Adjust Imports of Aluminum, Steel, and Copper into the United States," which broadened the scope of Section 232 tariffs on copper articles and derivative articles but did not add refined copper cathode to the tariff list [Strengthening Actions Taken to Adjust Imports of Aluminum, Steel ...](https://www.whitehouse.gov/presidential-actions/2026/04/strengthening-actions-taken-to-adjust-imports-of-aluminum-steel-and-copper-into-the-united-states/). As of April 23, 2026, per the Congressional Research Service, refined copper cathode (HTS 7403.11.00) remains excluded from Section 232 tariffs [Section 232 National Security Tariffs on Copper Imports](https://www.congress.gov/crs-product/IN12614).

The Department of Commerce is scheduled to provide an update on U.S. copper markets to the President by June 30, 2026, after which the President may determine whether to impose duties on refined copper [Section 232 National Security Tariffs on Copper Imports](https://www.congress.gov/crs-product/IN12614). Markets and analysts are uncertain whether the administration might act before the June 30 deadline. Goldman Sachs has cited a base case of a 15% tariff on refined copper announced mid-2026. The administration faces competing pressures: protectionist incentives to shield domestic smelters versus lobbying from downstream manufacturers who depend on affordable refined copper imports.

Current tariff status as of May 2, 2026: Refined copper cathode (HTS 7403.11.00) is subject to a 0% Section 232 tariff rate; it is not covered by the existing Section 232 copper tariff regime [Section 232 National Security Tariffs on Copper Imports](https://www.congress.gov/crs-product/IN12614).

**Exact later resolution packet**

The question resolves NO. It required that, between May 1, 2026 and June 1, 2026 (11:59 PM UTC), an official U.S. government announcement (whitehouse.gov, federalregister.gov, or commerce.gov) be published indicating that refined copper cathode (HTS 7403.11.00) would be subject to Section 232 tariffs at a rate greater than 0%.

Evidence:
- The Congressional Research Service report IN12614 (congress.gov), last updated April 23, 2026, confirms refined copper cathode (HTS 7403.11.00) remained excluded from Section 232 tariffs, and that the Department of Commerce is scheduled to provide an update on U.S. copper markets to the President only by June 30, 2026, after which the President may decide whether to impose duties on refined copper [821f48].
- The most relevant proclamation falling within the resolution window — "Further Adjusting the Tariff Regimes for Imports of Aluminum, Steel, and Copper into the United States," dated June 1, 2026 (https://www.whitehouse.gov/presidential-actions/2026/06/further-adjusting-the-tariff-regimes-for-imports-of-aluminum-steel-and-copper-into-the-united-states/) — does NOT impose any tariff on refined copper cathode and does not mention HTS 7403.11.00. It only modifies derivative-product tariffs (agricultural equipment, HVAC systems, mobile industrial equipment, aluminum lithographic plates, steel racks) and adjusts the U.S.-content threshold [036ffd].
- The accompanying June 1, 2026 White House fact sheet likewise contains no mention of refined copper cathode or HTS 7403.11.00 being subject to Section 232 tariffs [c1b6f3].
- A scan of the White House proclamations index showed no May 2026 copper-tariff proclamation; the only May 2026 proclamations were ceremonial/administrative [097a28].

Since no qualifying official announcement subjecting HTS 7403.11.00 to a Section 232 tariff greater than 0% was published on or before June 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-127. `ad67b848-c8e3-5e1d-8d73-4a844c69026e`

- Present date: `2026-04-30 17:26:59.410175`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Israel and Lebanon sign a formal, permanent ceasefire or peace agreement between April 30, 2026 and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after April 30, 2026, and by 23:59 UTC on June 1, 2026, the governments of Israel and Lebanon sign a formal, permanent ceasefire or peace agreement.

**Definitions:**

- A **"formal, permanent ceasefire or peace agreement"** is a written document that explicitly ends the state of hostilities or establishes a permanent (i.e., not time-limited) ceasefire between Israel and Lebanon. For reference, see the definitions of [peace treaty](https://en.wikipedia.org/wiki/Peace_treaty) and [ceasefire](https://en.wikipedia.org/wiki/Ceasefire) on Wikipedia.

- **"Signed"** means the agreement must bear the signature of authorized government representatives at the level of head of state, head of government, foreign minister, or a designated plenipotentiary (i.e., a person formally granted full authority to sign on behalf of their government). A joint official declaration or communiqué explicitly stating that a permanent agreement has been concluded also qualifies.

- **Temporary extensions** of the current ceasefire do not count as a "permanent" agreement. The agreement must be explicitly described as permanent, indefinite, or not time-limited.

**Exclusions:** Oral agreements, frameworks for future negotiation, or agreements-in-principle without formal signatures do not qualify.

**Resolution sources:** Official government press releases from the Israeli Prime Minister's Office (https://www.gov.il/en/departments/prime_ministers_office), the Lebanese Council of Ministers, or the U.S. Department of State (https://www.state.gov/), or credible major news agencies such as [Reuters](https://www.reuters.com/), [AP](https://apnews.com/), or [AFP](https://www.afp.com/).

If no such agreement is confirmed by these sources by 23:59 UTC on June 1, 2026, this question resolves as **No**.

**Pre-cutoff background**

Following the 2026 Lebanon war, a US-brokered ceasefire between Israel and Lebanon took effect on April 16, 2026. On April 23, 2026, the ceasefire was extended for an additional three weeks [https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire](https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire). The temporary truce is intended to facilitate negotiations toward a permanent settlement, including border demarcation and Hezbollah disarmament.

As of April 30, 2026, significant obstacles remain. Hezbollah is not a formal signatory to the ceasefire agreement. Both sides have reported ongoing violations, including rocket fire, drone attacks, and airstrikes [https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire](https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire). Israeli troops maintain a "security zone" inside southern Lebanon [https://english.news.cn/20260429/33d546c9c45043058ab5c6a266c67f4e/c.html](https://english.news.cn/20260429/33d546c9c45043058ab5c6a266c67f4e/c.html).

Israel has set a mid-May 2026 deadline for reaching a permanent agreement, according to Israeli state-owned Kan TV as reported by Xinhua on April 29, 2026. Israeli officials have indicated that if no permanent deal is reached by this deadline, Israel intends to escalate military operations targeting Hezbollah [https://english.news.cn/20260429/33d546c9c45043058ab5c6a266c67f4e/c.html](https://english.news.cn/20260429/33d546c9c45043058ab5c6a266c67f4e/c.html). The White House is reportedly attempting to arrange a summit between Israeli PM Netanyahu and Lebanese President Joseph Aoun, though officials from both sides have expressed skepticism about its feasibility [https://english.news.cn/20260429/33d546c9c45043058ab5c6a266c67f4e/c.html](https://english.news.cn/20260429/33d546c9c45043058ab5c6a266c67f4e/c.html).

The current ceasefire extension expires in mid-May 2026, creating a critical decision point where the parties must either reach a permanent agreement, extend the truce again, or see a return to hostilities.

**Exact later resolution packet**

The question resolves NO. It asks whether the governments of Israel and Lebanon signed a formal, PERMANENT (not time-limited) ceasefire or peace agreement between April 30, 2026 and 23:59 UTC June 1, 2026, explicitly excluding temporary extensions of the April 2026 ceasefire.

Key facts established from the mandated sources:
- The April 16, 2026 ceasefire was an initial 10-day temporary cessation of hostilities (U.S. State Department release), later extended for three weeks on April 23, 2026 [2026 Israel–Lebanon ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire).
- During the resolution window, the only Israel–Lebanon agreement was a 45-DAY EXTENSION of the existing ceasefire, agreed on May 15, 2026, as confirmed by Reuters ("Israel, Lebanon extend ceasefire by 45 days as Washington talks conclude," 2026-05-15) and the U.S. State Department [Israel, Lebanon extend ceasefire by 45 days as Washington talks ...](https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/). This is explicitly a temporary extension intended to enable further negotiations, NOT a permanent agreement, and the resolution criteria explicitly state temporary extensions do not count [Israel, Lebanon extend ceasefire by 45 days as Washington talks ...](https://www.reuters.com/world/middle-east/israel-lebanon-agree-extend-ceasefire-by-45-days-us-state-dept-says-2026-05-15/).
- The Wikipedia tracking article on the 2026 Israel–Lebanon ceasefire describes only these successive temporary extensions (10 days → 3 weeks → 45 days) and does not record any formal permanent peace treaty or permanent ceasefire being signed between the governments of Israel and Lebanon within the April 30–June 1, 2026 window [2026 Israel–Lebanon ceasefire - Wikipedia](https://en.wikipedia.org/wiki/2026_Israel%E2%80%93Lebanon_ceasefire).
- A separate development around June 1, 2026 involved Israel and Hezbollah (not the government of Lebanon) agreeing to halt strikes; this is not a formal signed permanent ceasefire/peace agreement between the governments of Israel and Lebanon, and is not described as permanent.

No mandated source (Israeli PM's Office, Lebanese Council of Ministers, U.S. State Department, Reuters, AP, AFP) reported a signed formal permanent ceasefire or peace agreement between the two governments by 23:59 UTC June 1, 2026. Per the resolution criteria, the question therefore resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-128. `443a70f1-50f3-5a66-886d-75f040616085`

- Present date: `2026-05-01 14:14:45.558487`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will IonQ publish a technical paper or preprint detailing their photonic interconnect demonstration by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), a technical document meeting ALL of the following criteria becomes publicly accessible:

1. **Authorship**: The document is authored or co-authored by one or more IonQ employees or affiliates.
2. **Content**: The document describes the technical details (e.g., experimental setup, entanglement fidelity measurements, or protocol descriptions) of a demonstration in which two or more **separate** quantum processors were connected via a photonic interconnect and entanglement was generated between ions in the different processors. "Separate" means the processors are housed in physically distinct vacuum chambers or trap assemblies (not merely different zones within a single trap).
3. **Published results**: The document is either (a) a preprint posted on arXiv.org (https://arxiv.org/), (b) a peer-reviewed article published in a scientific journal, or (c) a technical white paper posted on IonQ's official website with sufficient technical detail (i.e., including quantitative experimental data, not merely a press release or blog post).
4. **Publicly accessible**: The document must be freely viewable by the public (paywalled journal articles that have a publicly available abstract with quantitative results also count).

The question resolves **No** if no such document is publicly accessible by June 1, 2026 (23:59 UTC).

**Resolution sources**: arXiv search for IonQ-affiliated authors (https://arxiv.org/search/?query=ionq&searchtype=all), IonQ's newsroom (https://investors.ionq.com/news), and IonQ's research publications page (https://www.ionq.com/resources). Credible reporting from outlets such as HPC Wire, Nature, or Science may also be used to identify publications.

**Pre-cutoff background**

On April 14, 2026, IonQ (NYSE: IONQ) announced it had achieved a "foundational technical milestone" by photonically interconnecting two independent trapped-ion quantum systems, generating remote ion-ion entanglement between two commercial IonQ computers [IonQ Achieves Key Photonic Interconnect Milestone, Demonstrating ...](https://www.ionq.com/news/ionq-achieves-key-photonic-interconnect-milestone-demonstrating-networked-quantum-systems-using-entanglement). The press release validated the generation, transmission, and detection of photons used to enable quantum entanglement between the systems, but did not include detailed technical data such as entanglement fidelity, gate error rates, distance between systems, or hardware specifications typically found in scientific publications [IonQ Achieves Key Photonic Interconnect Milestone, Demonstrating ...](https://www.ionq.com/news/ionq-achieves-key-photonic-interconnect-milestone-demonstrating-networked-quantum-systems-using-entanglement).

A photonic interconnect is a communication link that uses photons (particles of light) to transfer information between separate systems (see: https://en.wikipedia.org/wiki/Photonic_integrated_circuit). In the context of quantum computing, entanglement-based networking refers to using quantum entanglement—a phenomenon where quantum states of two or more particles become correlated regardless of distance (see: https://en.wikipedia.org/wiki/Quantum_entanglement)—to connect separate quantum processors (hardware devices that manipulate qubits to perform quantum computations; see: https://en.wikipedia.org/wiki/Quantum_computing).

As of April 30, 2026 (00:00 UTC), IonQ has issued only a press release and no formal technical publication (preprint or peer-reviewed paper) describing the methodology and results of this demonstration has been identified on arXiv or in scientific journals. IonQ's stock rose approximately 10% on the announcement. The company also received a DARPA HARQ contract around the same time. Publication timelines for quantum computing milestones vary: some companies publish preprints within days of an announcement, while others take months or never publish full technical details.

**Exact later resolution packet**

The question resolves NO. It requires that, between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), an IonQ-authored technical document (arXiv preprint, peer-reviewed journal article, or technical white paper with quantitative data) describing photonic-interconnect-mediated entanglement between ions in two SEPARATE quantum processors (distinct vacuum chambers/trap assemblies) became publicly accessible.

Evidence gathered:
- IonQ's official Publications page (https://www.ionq.com/publications) lists its most recent papers as "Measuring Accuracy and Energy-to-Solution of Quantum Fine-Tuning of Foundational AI Models" (May 5, 2026), "Fault-Tolerant Quantum Computing with Trapped Ions: The Walking Cat Architecture" (April 21, 2026), and "Measuring what matters: A scalable framework for application-level quantum benchmarking" (April 14, 2026). None of these describe the April 14, 2026 photonic interconnect demonstration of remote ion-ion entanglement between two separate processors [Publications - IonQ](https://www.ionq.com/publications).
- IonQ's Resource Center (https://www.ionq.com/resources) shows the same set, with nothing in the resolution window on the photonic interconnect demonstration [https://www.ionq.com/resources](https://www.ionq.com/resources).
- An arXiv search for "ionq" (https://arxiv.org/search/?query=ionq&searchtype=all) returns May 2026 IonQ-related papers on unrelated topics (NISQ wave packet simulation, quantum compilers, Clifford noise reduction, sequence learning, Maxwell's equations) — none describing the photonic interconnect / remote two-processor entanglement demonstration [https://arxiv.org/search/?query=ionq&searchtype=all&start=0](https://arxiv.org/search/?query=ionq&searchtype=all&start=0).
- The only IonQ photonics-platform paper, "Scalable photonic quantum interconnect platform," is dated February 6, 2026 (before the window) and concerns wafer-scale diamond photonic interfaces, not the two-separate-processor entanglement demonstration [Publications - IonQ](https://www.ionq.com/publications).

No qualifying preprint, journal article, or quantitative white paper was found in the April 30 – June 1, 2026 window across all three specified resolution sources, so the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):
