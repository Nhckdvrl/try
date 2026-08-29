# BTF-3 confirmatory candidate queue — confirmatory_v1

> Fixed deterministic order. Review top-to-bottom within each resolution bucket until 32 ACCEPTs are reached per bucket. Do not skip ahead or reorder. A REJECT/UNSURE consumes its queue slot permanently and is never resampled or reconsidered.

For each item, tick exactly one of ACCEPT / REJECT / UNSURE for all four gates jointly (all four must hold to ACCEPT). On REJECT or UNSURE, write exactly one line giving the reason.

## Realized NO queue (64 candidates)

### NO-1. `f8a6fd09-c315-50e3-9383-da38927ac12d`

- Present date: `2026-05-03 05:11:28.382717`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Department of Homeland Security receive full-year FY2026 appropriations (not a continuing resolution) signed into law by June 1, 2026?

**Resolution criteria**

This question resolves YES if a bill providing full-year appropriations for the Department of Homeland Security for Fiscal Year 2026 is signed into law (enacted) by the President on or after May 1, 2026, and by 11:59 PM Eastern Time on June 1, 2026.

"Full-year appropriations" means legislation that provides new discretionary funding for DHS for the remainder of Fiscal Year 2026 (ending September 30, 2026). This explicitly excludes any continuing resolution (CR) or other temporary funding measure that merely extends prior-year funding levels for a limited duration without providing full-year appropriations.

Note: It is sufficient if DHS full-year funding is achieved through a combination of a regular appropriations bill and a reconciliation bill, so long as together they provide full-year funding for the entire department (including ICE and Border Security Operations) by the deadline.

This question resolves NO if no such legislation is signed into law by 11:59 PM Eastern Time on June 1, 2026, including if only a new CR or temporary extension is enacted.

Resolution will be verified via official legislative records at Congress.gov (https://www.congress.gov/) or the White House Briefing Room (https://www.whitehouse.gov/briefing-room/), supplemented by credible reporting from major outlets such as Reuters, AP, or The New York Times.

**Pre-cutoff background**

The Department of Homeland Security (DHS) has been in a partial government shutdown since February 14, 2026, due to a legislative impasse over funding for Immigration and Customs Enforcement (ICE) and Border Security Operations (BSO) [https://www.crfb.org/blogs/appropriations-watch-fy-2026](https://www.crfb.org/blogs/appropriations-watch-fy-2026). While the Senate passed a DHS funding bill on March 27, 2026, the House amended it to include ICE and BSO provisions, leading to the current stalemate [https://www.crfb.org/blogs/appropriations-watch-fy-2026](https://www.crfb.org/blogs/appropriations-watch-fy-2026).

A continuing resolution (CR) currently provides temporary funding for DHS but is set to expire on May 22, 2026 [https://www.crfb.org/blogs/appropriations-watch-fy-2026](https://www.crfb.org/blogs/appropriations-watch-fy-2026). On April 23, 2026, the Senate adopted a budget resolution by a 50-48 vote to initiate a reconciliation process intended to fund ICE and BSO separately, while the remainder of DHS would be funded through regular appropriations [https://www.crfb.org/blogs/appropriations-watch-fy-2026](https://www.crfb.org/blogs/appropriations-watch-fy-2026).

For context, other departments have already received full-year FY2026 funding—for example, the State Department appropriations bill was signed into law on February 3, 2026 [https://www.crfb.org/blogs/appropriations-watch-fy-2026](https://www.crfb.org/blogs/appropriations-watch-fy-2026). DHS remains the major outstanding appropriations dispute, with the May 22 CR expiration creating additional urgency.

A "full-year appropriation" provides funding for the remainder of Fiscal Year 2026 (ending September 30, 2026), as opposed to a "continuing resolution" (CR), which is a temporary measure that funds government operations at prior-year levels for a limited period without setting new funding levels or priorities.

**Exact later resolution packet**

The question resolves NO. The resolution criteria require that, by 11:59 PM ET on June 1, 2026, DHS receive full-year FY2026 appropriations for the ENTIRE department — explicitly including ICE and Border Security Operations (BSO) — whether through a single appropriations bill or a combination of an appropriations bill and a reconciliation bill.

What actually happened:
- On April 30, 2026, President Trump signed the FY2026 DHS appropriations bill into law (P.L. 119-86), ending the 76-day partial shutdown that began February 14, 2026. However, this bill explicitly EXCLUDED funding for ICE and CBP's Border Patrol; those employees continued to be paid from the prior year's reconciliation law. (Multiple major outlets — Reuters, CNN, NPR, AP/Al Jazeera, NYT, CNBC — and the CRFB Appropriations Watch all confirm the bill funded "most" of DHS but left out ICE and Border Patrol [Appropriations Watch: FY 2026](https://www.crfb.org/blogs/appropriations-watch-fy-2026).)
- ICE and BSO funding was to be provided through a SEPARATE budget reconciliation bill. A budget resolution to enable this was adopted by the Senate 50-48 on April 23, 2026. Senate Republicans unveiled a ~$72 billion reconciliation package on May 5, 2026.
- That reconciliation bill was NOT enacted by June 1, 2026. As of May 18, 2026, it was still being reworked after the Senate Parliamentarian found multiple provisions violated the Byrd Rule, and it faced an uphill path in both chambers [This week on The Hill: Immigration funding takes center stage as ...](https://thehill.com/homenews/senate/5880861-this-week-on-the-hill-immigration-funding-takes-center-stage-as-june-1-deadline-looms/). Senate Republicans abruptly delayed votes on May 21, 2026, and the House considered leaving town, blowing past President Trump's June 1 deadline. An NLIHC update dated June 1, 2026 is titled "Republicans Return to Reconciliation Negotiations After Memorial Day Recess," confirming the reconciliation bill was still under negotiation — not signed into law — as of the June 1 deadline.

Because ICE and BSO were not funded for the full fiscal year by any enacted legislation by 11:59 PM ET on June 1, 2026, the "entire department" condition required by the resolution criteria was not satisfied. Therefore the question resolves NO.

Key sources:
- CRFB Appropriations Watch FY2026: https://www.crfb.org/blogs/appropriations-watch-fy-2026 [Appropriations Watch: FY 2026](https://www.crfb.org/blogs/appropriations-watch-fy-2026)
- The Hill (June 1 deadline looming, reconciliation still unfinished, May 18): https://thehill.com/homenews/senate/5880861-this-week-on-the-hill-immigration-funding-takes-center-stage-as-june-1-deadline-looms/ [This week on The Hill: Immigration funding takes center stage as ...](https://thehill.com/homenews/senate/5880861-this-week-on-the-hill-immigration-funding-takes-center-stage-as-june-1-deadline-looms/)
- Congress.gov H.R.7148 / FY2026 DHS appropriations (P.L. 119-86, signed April 30): confirmed via FFIS and multiple outlets.
- NLIHC, "Republicans Return to Reconciliation Negotiations After Memorial Day Recess," dated June 1, 2026.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-2. `985a9576-773a-5122-b880-d70cd192f452`

- Present date: `2026-05-12 19:56:08.630122`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the sale of Telefónica's Mexican operations to Melisa Acquisition LLC close by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 10, 2026 and no later than 23:59 UTC on July 1, 2026, the sale of Telefónica's Mexican operations to Melisa Acquisition, LLC is officially completed (i.e., the transaction has closed).

This question resolves as **No** if the transaction has not closed by 23:59 UTC on July 1, 2026, or if the deal is officially terminated, cancelled, or blocked by regulators before that date.

**What constitutes "closing":** The deal is considered closed when Telefónica issues an official press release or regulatory filing (hecho relevante) confirming the completion of the transaction. Specifically, resolution will be based on:

1. An official filing with the Comisión Nacional del Mercado de Valores (CNMV), accessible at https://www.cnmv.es/portal/home?lang=en ; or
2. An official announcement on Telefónica's investor relations page at https://www.telefonica.com/en/investors/ ; or
3. Credible reporting from major financial news outlets (e.g., Reuters, Bloomberg, Financial Times) confirming the closing.

**Primary regulatory body being tracked:** The Instituto Federal de Telecomunicaciones (IFT) (or its successor entity, the Comisión Reguladora de Telecomunicaciones / CRT) is the primary Mexican regulatory body whose approval is required for this transaction to close. IFT press releases can be monitored at https://www.ift.org.mx/comunicacion-y-medios/comunicados-ift

A mere announcement of regulatory approval without confirmation of deal closing is not sufficient for Yes resolution; the transaction must have formally closed.

**Pre-cutoff background**

On April 7–8, 2026, Telefónica announced an agreement to sell 100% of its Mexican operations (comprising Pegaso PCS, S.A. de C.V. and Celular de Telefonía, S.A. de C.V.) to Melisa Acquisition, LLC, a consortium led by telecom tech firm OXIO Inc. and asset manager Newfoundland Capital Management [Telefonica finally able to sell Mexico business - Developing Telecoms](https://developingtelecoms.com/telecom-business/operator-news/20089-telefonica-finally-able-to-sell-mexico-business.html)[Telefónica Agrees to Sell Mexican Operations for $450 Million](https://antitrust-intelligence.com/telefonica-agrees-to-sell-mexican-operations-for-450-million/). The transaction has a firm enterprise value of $450 million, subject to customary adjustments [Telefónica Agrees to Sell Mexican Operations for $450 Million](https://antitrust-intelligence.com/telefonica-agrees-to-sell-mexican-operations-for-450-million/).

This divestment is part of Telefónica's broader strategy to exit non-core Latin American markets (having already completed sales in Uruguay, Ecuador, Colombia, Chile, and Peru) to focus on its core operations in Europe and Brazil [Telefonica finally able to sell Mexico business - Developing Telecoms](https://developingtelecoms.com/telecom-business/operator-news/20089-telefonica-finally-able-to-sell-mexico-business.html).

The completion of the transaction is conditional on obtaining necessary regulatory approvals, primarily from Mexico's Instituto Federal de Telecomunicaciones (IFT) [Telefónica Agrees to Sell Mexican Operations for $450 Million](https://antitrust-intelligence.com/telefonica-agrees-to-sell-mexican-operations-for-450-million/). Note that Mexico underwent a regulatory transition in late 2025, with the IFT's functions being restructured under the Comisión Reguladora de Telecomunicaciones (CRT), which may affect the review process. Typical telecom M&A regulatory review periods in Mexico run approximately three months, making the July 1, 2026 deadline tight but plausible given the early April announcement. The non-traditional buyer profile (a consortium led by an MVNO enabler rather than a traditional telecom operator) adds uncertainty to the regulatory review timeline.

As of May 11, 2026, the deal remains pending regulatory approval [Telefónica Agrees to Sell Mexican Operations for $450 Million](https://antitrust-intelligence.com/telefonica-agrees-to-sell-mexican-operations-for-450-million/).

**Exact later resolution packet**

The question resolves NO. The sale of Telefónica's Mexican operations (Pegaso PCS, S.A. de C.V. and Celular de Telefonía, S.A. de C.V.) to Melisa Acquisition, LLC (the OXIO/Newfoundland Capital consortium) did NOT close on or before 23:59 UTC on July 1, 2026.

Key evidence:

1. AUTHORITATIVE RESOLUTION SOURCE (Telefónica IR / CNMV): The resolution criteria specify that closing must be confirmed by an official CNMV filing or Telefónica investor-relations announcement. Telefónica's official "Other Relevant Information" (hechos relevantes) page at https://www.telefonica.com/en/shareholders-investors/cnmv-communications/other-relevant-information/ — as retrieved on June 26, 2026 — contains ONLY the April 7, 2026 filing ("Telefónica informs about the sale of all the shares it holds in Pegaso PCS and Celular de Telefonía (Telefónica México)") and NO subsequent filing announcing the completion/closing of the transaction [Other Relevant Information 2026 - Telefónica](https://www.telefonica.com/en/shareholders-investors/cnmv-communications/other-relevant-information/). A closing (hecho relevante confirming completion) is the specific trigger required for YES resolution, and no such filing exists as of the deadline.

2. COMPANY'S OWN TIMELINE: Telefónica stated it expects to close the share transfer "before the end of the third quarter of 2026" (i.e., by ~September 30, 2026), well after the July 1, 2026 deadline (Señal News, published April 9, 2026) [Telefónica vendió su filial mexicana a Melisa Acquisition - Señal News](https://senalnews.com/es/contenidos/telefonica-vendio-su-filial-mexicana-a-melisa-acquisition-). This makes a pre-July-1 closing inconsistent with the company's own guidance.

3. STATUS AS OF LATE JUNE 2026: Reporting from late June 2026 (ConsumoTIC, page dated 2026-06-30) confirms the transaction remained subject to closing conditions between the parties and pending regulatory approvals, with no completion announced [Tras venta, clientes Movistar gozarán de mejoras en calidad: Melisa ...](https://consumotic.mx/telecom/tras-venta-clientes-movistar-gozaran-de-mejoras-en-calidad-melisa-acquisition/). The deal was still awaiting Mexican regulatory approval (IFT/CRT), and OXIO's own press release stated "The transaction remains subject to closing conditions between the parties and customary regulatory approvals."

Because the transaction had not closed by 23:59 UTC on July 1, 2026 — evidenced by the absence of any completion filing on Telefónica's CNMV communications page and by the company's Q3 2026 closing guidance — the question resolves NO. (Note: The window's antecedent condition — the deal being agreed/announced — did occur on April 7–8, 2026, so the question is resolvable and not annulled; it simply did not close within the window.)

Primary URL for evidence: https://www.telefonica.com/en/shareholders-investors/cnmv-communications/other-relevant-information/ (only lists the April 7, 2026 sale announcement, no closing filing) [Other Relevant Information 2026 - Telefónica](https://www.telefonica.com/en/shareholders-investors/cnmv-communications/other-relevant-information/).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-3. `85389e81-ba1e-521c-b039-c7985ba14539`

- Present date: `2026-05-16 11:23:49.584665`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Courts and Tribunals Bill complete its Report stage in the House of Commons by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the Report stage of the Courts and Tribunals Bill is completed in the House of Commons on or after May 12, 2026, and no later than July 1, 2026, at 23:59 UTC. It resolves **No** otherwise.

"Report stage" refers to the stage of legislative proceedings in the House of Commons where the whole House considers amendments to a bill after Committee stage, as defined by the UK Parliament glossary: https://www.parliament.uk/site-information/glossary/report-stage/

Completion of the Report stage is defined as the House of Commons concluding its report stage proceedings, such that the bill is ready for its Third Reading. This will be determined by the official UK Parliament bill tracker at https://bills.parliament.uk/bills/4083/stages showing a completed Report stage with a date on or before July 1, 2026.

**Pre-cutoff background**

The Courts and Tribunals Bill is a UK Government bill currently progressing through the House of Commons. The bill passed its Second Reading on March 10, 2026, by a vote of 304-203, with 10 Labour MPs voting against the government, and reports suggesting up to 65 Labour MPs were considering rebellion over the removal of jury trial rights in either-way cases. The Committee stage concluded on April 28, 2026 [https://bills.parliament.uk/bills/4083/stages](https://bills.parliament.uk/bills/4083/stages). As of May 12, 2026, the Report stage is listed as "Date to be announced" on the official UK Parliament bill tracker [https://bills.parliament.uk/bills/4083/stages](https://bills.parliament.uk/bills/4083/stages).

The combination of scheduling uncertainty—with no announced date for Report stage—and the potential for a significant Labour rebellion creates genuine uncertainty about whether the government will bring this bill back to the floor of the House of Commons for its Report stage before July 1, 2026. Government business managers must balance parliamentary time constraints, potential amendments, and internal party management.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if the official UK Parliament bill tracker (https://bills.parliament.uk/bills/4083/stages) shows the Courts and Tribunals Bill's Commons Report stage as COMPLETED, with a date on/after 12 May 2026 and no later than 1 July 2026 (23:59 UTC). It does not.

KEY EVIDENCE FROM THE OFFICIAL TRACKER:
- The tracker (https://bills.parliament.uk/bills/4083/stages) lists, under Session 2026-27, "Report stage — Date to be announced (Commons)," and "Bill reintroduced — 14 May 2026 (Commons)" [Courts and Tribunals Bill Stages - Parliamentary Bills - UK Parliament](https://bills.parliament.uk/bills/4083/stages). A "Date to be announced" status means the stage has not been scheduled, let alone completed, by the deadline.

ADDRESSING THE MISLEADING "REINTRODUCED AT REPORT STAGE" LABEL:
- The bill's current version is published as "Bill 005 2026-27 (reintroduced at Report Stage)" dated 14 May 2026. This is merely a reprint/carry-over marker indicating the bill was reprinted (with Committee amendments incorporated) and is at the point in the process where Report stage would next occur. It is NOT a record that the Report stage debate took place. One automated read of the summary page misinterpreted this label as the Report stage being "Complete," but that is contradicted by the stages page itself ("Date to be announced") and by all contemporaneous reporting below.

CORROBORATION THAT REPORT STAGE WAS NOT HELD BY 1 JULY 2026:
- Joshua Rozenberg ("A Lawyer Writes," 10 June 2026): "MPs have produced their report in time for the bill's report stage and third reading debate, which might have been expected this week. But no date for these stages has been announced yet, even though the bill was reintroduced to parliament four weeks ago." He adds the bill "is currently awaiting further consideration by the House of Commons" [Jury bill won't work, say MPs - by Joshua Rozenberg - A Lawyer Writes](https://rozenberg.substack.com/p/jury-bill-wont-work-say-mps).
- Hansard Society "Parliament Matters" bulletin for 15–18 June 2026: the bill is mentioned only in relation to the Justice Committee's report; it is NOT scheduled for Report stage that week, and no future date is given [What's coming up in Parliament this week? 15-18 June 2026](https://www.hansardsociety.org.uk/news/parliament-matters-bulletin-15-june-2026).
- Hansard Society "Parliament Matters" bulletin for 29 June – 3 July 2026 (the final window before the deadline): Commons business for Mon 29 June, Tue 30 June and Wed 1 July 2026 consists of departmental questions, Main Estimates debates, a Supply/Appropriation Bill, and the Taxation (Energy and Vehicles) Bill — with NO mention of the Courts and Tribunals Bill Report stage or Third Reading [What's coming up in Parliament this week? 29 June – 3 July 2026](https://www.hansardsociety.org.uk/news/parliament-matters-bulletin-29-june-2026).

ADDRESSING THE REBELLION / SCHEDULING FACTORS FROM THE DESCRIPTION:
- The scheduling uncertainty flagged in the question did in fact prevent completion. Rozenberg reports: "All the signs are that ministers have chosen to postpone a difficult vote in the Commons until after the by-election," i.e. the government deliberately did not bring the bill's Report stage to the floor within the window [Jury bill won't work, say MPs - by Joshua Rozenberg - A Lawyer Writes](https://rozenberg.substack.com/p/jury-bill-wont-work-say-mps). Combined with the potential Labour rebellion over the removal of jury-trial rights for either-way offences (noted in the question), government business managers left the Report stage unscheduled ("Date to be announced") through at least end-June 2026 [Courts and Tribunals Bill Stages - Parliamentary Bills - UK Parliament](https://bills.parliament.uk/bills/4083/stages) [Jury bill won't work, say MPs - by Joshua Rozenberg - A Lawyer Writes](https://rozenberg.substack.com/p/jury-bill-wont-work-say-mps) [What's coming up in Parliament this week? 15-18 June 2026](https://www.hansardsociety.org.uk/news/parliament-matters-bulletin-15-june-2026) [What's coming up in Parliament this week? 29 June – 3 July 2026](https://www.hansardsociety.org.uk/news/parliament-matters-bulletin-29-june-2026).

CONCLUSION: As of 1 July 2026, 23:59 UTC, the official tracker shows the Report stage as not completed ("Date to be announced"), and it was not scheduled in the final sitting week before the deadline. The Report stage was therefore NOT completed in the required window. The question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-4. `71ff25b3-b13b-5b64-ba88-7eb29725956f`

- Present date: `2026-05-15 11:29:46.222646`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Belgium's three main union confederations (CSC/ACV, FGTB/ABVV, CGSLB/ACLVB) jointly call for a second nationwide cross-sector strike or 'Day of Action' between May 13 and June 30, 2026?

**Resolution criteria**

This question resolves as **YES** if, on or after May 13, 2026 (00:00 UTC) and on or before June 30, 2026 (23:59 UTC), all three of Belgium's main trade union confederations—CSC/ACV, FGTB/ABVV, and CGSLB/ACLVB—jointly call for a new nationwide cross-sector (interprofessional) strike or "Day of Action." Specifically:

1. **"Jointly call"** means that all three confederations must be identified as co-organizers or co-signatories of the action, whether via a shared press release, a joint "front commun/gemeenschappelijk vakbondsfront" announcement, or confirmed by each confederation's official communications (websites: [CSC/ACV](https://www.csc-en-ligne.be/), [FGTB/ABVV](https://www.fgtb.be/), [CGSLB/ACLVB](https://www.cgslb.be/)).

2. **"Nationwide cross-sector" (interprofessional)** means the action must be explicitly described as national ("nationale") and covering multiple economic sectors (interprofessional/cross-sector), as distinct from a regional strike or a single-industry action. The terms "grève nationale interprofessionnelle," "nationale interprofessionele staking," "national Day of Action," or equivalent formulations qualify.

3. **Announcement vs. occurrence**: The *call* (formal announcement) for the action must be issued within the resolution window (May 13–June 30, 2026 UTC). The strike itself does not need to take place within this window—only the joint announcement must occur within it.

4. **Exclusion of May 12 action**: The national strike/demonstration of May 12, 2026 does not count. Only a newly announced action qualifies.

5. If no such joint call is confirmed by June 30, 2026 (23:59 UTC), the question resolves **NO**.

**Resolution source**: Reporting by credible Belgian news outlets, specifically [VRT NWS](https://www.vrt.be/vrtnws/en/), [RTBF](https://www.rtbf.be/), or [Le Soir](https://www.lesoir.be/), or official union announcements on their websites listed above.

**Pre-cutoff background**

On May 12, 2026, Belgium's three major trade union confederations—[CSC/ACV](https://en.wikipedia.org/wiki/Confederation_of_Christian_Trade_Unions), [FGTB/ABVV](https://en.wikipedia.org/wiki/General_Federation_of_Belgian_Labour), and [CGSLB/ACLVB](https://en.wikipedia.org/wiki/General_Confederation_of_Liberal_Trade_Unions_of_Belgium)—organized a national strike and demonstration in Brussels protesting the federal government's ("Arizona coalition") socio-economic reforms [Everything we know so far about next week's strike in Belgium](https://www.brusselstimes.com/2111818/everything-we-know-so-far-about-next-weeks-strike-in-belgium). The unions demanded better pension schemes, preservation of full automatic wage indexation, a fairer tax system, and improved working conditions [Everything we know so far about next week's strike in Belgium](https://www.brusselstimes.com/2111818/everything-we-know-so-far-about-next-weeks-strike-in-belgium). The FGTB/ABVV described May 12 as "a crucial moment" to establish "a new balance of power" with the government [Everything we know so far about next week's strike in Belgium](https://www.brusselstimes.com/2111818/everything-we-know-so-far-about-next-weeks-strike-in-belgium).

This was the latest in a series of escalating joint actions: previous large-scale mobilizations took place on October 14, 2025, and March 12, 2026 [Fresh national trade union demo in Brussels on 12 May | VRT NWS](https://www.vrt.be/vrtnws/en/2026/04/08/fresh-national-trade-union-demo-in-brussels-on-12-may/). Earlier in 2026, the unions' "Front Commun" also organized interprofessional strike days on February 5, 10, and 12. Historically, Belgian unions have used waves of escalating industrial action—sometimes calling multiple national actions in quick succession—when the government does not make concessions.

As of May 13, 2026, no second joint nationwide action has been publicly announced. Whether the unions escalate further depends on the government's response to demands raised around May 12. The outcome is uncertain: sometimes a large mobilization is sufficient to bring the government to the negotiating table, while in other cases unions have rapidly scheduled follow-up actions.

**Exact later resolution packet**

The question resolves NO. It required that all three of Belgium's main confederations (CSC/ACV, FGTB/ABVV, CGSLB/ACLVB) JOINTLY call — between 13 May and 30 June 2026 — for a NEW action explicitly described as both "nationwide" and "cross-sector/interprofessional." No such joint call was issued in that window.

Evidence from the required resolution sources and union websites:

1. Union actions that actually occurred/were called in the window were all sector-specific or regional, not a national interprofessional strike jointly called by all three confederations:
   - 4 June 2026: a national action day/demonstration for the SOCIAL-PROFIT sector only (sector-specific), organized by the common front — not cross-sector/interprofessional [9a5fc5].
   - 16 June 2026: a regional demonstration in Namur, called only by the French-speaking wings of FGTB and CSC (not CGSLB, and not nationwide) [9a5fc5, d82efe].
   - 23 June 2026: a PUBLIC-SERVICES strike (RTBF, 22 June 2026) — explicitly limited to public services (communes, CPAS, public hospitals) and concentrated in Brussels/Wallonia, called by public-sector unions (CGSP/CNE), not a nationwide cross-sector interprofessional action [d82efe].
   - Other actions in the window (education, TotalEnergies/ExxonMobil refineries, Skeyes air traffic control, prisons, firefighters) were single-sector [9a5fc5].

2. Official union websites list no new joint national interprofessional strike/Day of Action in the window. The ABVV/FGTB "Vakbondsactie" page lists only the excluded 12 May demo, a 17 May Palestine solidarity mobilization, and the internal 12 June federal congress [4ca133]. The FGTB "Actions syndicales" page lists only the 12 June congress and a 14 June peace demonstration [4ce89d].

3. The strongest candidate for escalation — FGTB statements at its 12 June 2026 federal congress (La Libre) — was FGTB acting ALONE, "not excluding" a general strike at the autumn "rentrée," with NO firm date or form decided. FGTB's president expressly said he hoped a possible November/December action would be "en front commun," confirming no joint agreement existed at that point [d62d47]. This does not satisfy the "jointly call" requirement (all three confederations as co-organizers/co-signatories of a defined national interprofessional action).

Because no joint, nationwide, cross-sector (interprofessional) strike/Day of Action was called by all three confederations between 13 May and 30 June 2026, the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-5. `1076a71a-98c2-50b3-a429-446bdd0a1219`

- Present date: `2026-05-02 15:33:11.315872`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Apple Intelligence be officially available to users in mainland China by June 1, 2026?

**Resolution criteria**

This question resolves YES if Apple Intelligence becomes officially available to general consumers in mainland China (the People's Republic of China, excluding the Special Administrative Regions of Hong Kong and Macau, and excluding Taiwan) on or after May 1, 2026, and on or before 11:59 PM UTC on June 1, 2026.

"Officially available" means at least one of the following observable indicators is met:
1. Apple publishes a press release or announcement on its official Newsroom (https://www.apple.com/newsroom/) confirming the availability of Apple Intelligence in mainland China; OR
2. Apple's official feature availability page (https://www.apple.com/apple-intelligence/) is updated to list mainland China as a supported region; OR
3. Apple releases an iOS software update with public release notes explicitly stating Apple Intelligence is now available in mainland China.

The accidental rollout on or around March 30, 2026, does NOT count toward resolution, as it was not an official launch and was subsequently reversed [Apple Intelligence Accidentally Goes Live in China Before ...](https://www.macrumors.com/2026/03/30/apple-intelligence-china-mistake/).

If none of the above indicators are met by 11:59 PM UTC on June 1, 2026, this question resolves NO.

It is logically possible for this question to resolve NO if the CAC does not grant regulatory approval in time, or if Apple delays the launch for other reasons.

**Pre-cutoff background**

As of May 1, 2026, Apple Intelligence is not officially available in mainland China (defined as the People's Republic of China excluding Hong Kong, Macau, and Taiwan). China remains the last major market without official Apple Intelligence availability [Apple Intelligence Accidentally Goes Live in China Before ...](https://www.macrumors.com/2026/03/30/apple-intelligence-china-mistake/).

On March 30, 2026, Apple accidentally enabled Apple Intelligence features for some iPhone users in mainland China via an iOS update, before the features were pulled shortly afterward [Apple Intelligence Accidentally Goes Live in China Before ...](https://www.macrumors.com/2026/03/30/apple-intelligence-china-mistake/). Bloomberg's Mark Gurman confirmed the rollout was a mistake and not an intentional launch. The accidental activation demonstrated that Apple is technically ready to deploy Apple Intelligence in China, reportedly powered through a partnership with Alibaba's AI models.

The primary barrier to an official launch is regulatory approval from China's Cyberspace Administration of China (CAC), which requires all generative AI models to be tested and approved before being offered to the public. The CAC maintains a public registry of approved AI models. The timing of such approval is inherently uncertain given the complex regulatory and geopolitical dynamics involved. Apple's WWDC 2026 is scheduled for June 8, 2026, which falls after this question's resolution window.

**Exact later resolution packet**

The question resolves NO. It required at least one of three official indicators by 11:59 PM UTC June 1, 2026: (1) an Apple Newsroom press release confirming Apple Intelligence availability in mainland China; (2) Apple's feature availability page listing mainland China as supported; or (3) iOS release notes explicitly stating availability in mainland China. None of these occurred.

- Apple's official support/feature page "How to get Apple Intelligence" (https://support.apple.com/en-us/121115) still states: "Apple Intelligence features will not currently work for supported devices purchased in China mainland," with no indication availability occurred by June 1, 2026 [d0bb5b].
- Apple's official Apple Intelligence page (https://www.apple.com/apple-intelligence/) does not list mainland China as a supported region [be3d36].
- Apple's iOS/iPadOS 26 Feature Availability page explicitly notes for Apple Intelligence features: "Chinese (Simplified) - not available in China mainland" (https://www.apple.com/ios/feature-availability/).
- Apple's Newsroom (https://www.apple.com/newsroom/) had no press release announcing Apple Intelligence availability in mainland China through late May 2026; the most recent relevant release, dated May 19, 2026 ("Apple unveils new accessibility features, and updates with Apple Intelligence"), does not mention mainland China availability [3a7eff].

The only China-related activation event was the accidental March 30, 2026 rollout, which the resolution criteria explicitly exclude, and which Bloomberg's Mark Gurman confirmed was a mistake, not an official launch. WWDC 2026 (June 8, 2026) falls after the resolution window. Therefore none of the three required indicators were met by the deadline, and the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-6. `a4bcf029-c92f-50ff-bb5f-ef40c610daf9`

- Present date: `2026-05-16 18:47:48.331733`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Public Office (Accountability) Bill receive Third Reading in the House of Commons by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the Public Office (Accountability) Bill receives its [Third Reading](https://www.parliament.uk/site-information/glossary/third-reading/) in the House of Commons on or after May 12, 2026, and on or before July 1, 2026 (by 11:59 PM UTC on July 1, 2026). It resolves **No** otherwise.

Resolution will be determined by the official bill tracker on the UK Parliament website: https://bills.parliament.uk/bills/4019

The bill tracker records each stage of parliamentary progress with dates. If the tracker shows a "Third Reading" entry in the House of Commons with a date falling within the specified window, the question resolves Yes.

**Pre-cutoff background**

The Public Office (Accountability) Bill is a Government Bill introduced in the 2024–26 session, sponsored by the Ministry of Justice. It aims to impose a duty on public authorities and officials to act with candour, transparency, and frankness, and to create new offences regarding misconduct in public office [https://bills.parliament.uk/bills/4019](https://bills.parliament.uk/bills/4019).

As of early May 2026, the bill has completed Committee stage and is awaiting Report stage in the House of Commons [https://bills.parliament.uk/bills/4019](https://bills.parliament.uk/bills/4019). Third Reading is the final stage of consideration in the Commons and typically follows immediately after Report stage, often on the same day. However, completion is not guaranteed within any particular timeframe — contentious divisions on specific clauses could delay Report stage, and parliamentary scheduling pressures near the end of session could further complicate progress. The bill's subject matter (public office accountability, including provisions around the Hillsborough disaster) has generated significant debate, which may affect the pace of progress through remaining stages.

**Exact later resolution packet**

The question asks whether the Public Office (Accountability) Bill received its Third Reading in the House of Commons on or after May 12, 2026, and on or before July 1, 2026 (11:59 PM UTC). Resolution is determined by the official UK Parliament bill tracker at https://bills.parliament.uk/bills/4019.

Evidence from the official tracker (and its /stages page, https://bills.parliament.uk/bills/4019/stages), current as of 30 June–1 July 2026:

- The bill's stages recorded are: 1st reading (16 September 2025), 2nd reading (3 November 2025), Programme motion & Money resolution (3 November 2025), Committee stage (from 27 November 2025), Carry-over motion (27 April 2026), Bill reintroduced (14 May 2026), and Report stage listed as "Date to be announced" [https://bills.parliament.uk/bills/4019/stages](https://bills.parliament.uk/bills/4019/stages).

- The bill was carried over into a new session and reintroduced on 14 May 2026, and is still awaiting its Report stage in the House of Commons. The Report stage has not been completed and no date has been announced for it [https://bills.parliament.uk/bills/4019/stages](https://bills.parliament.uk/bills/4019/stages) [https://bills.parliament.uk/bills/4019](https://bills.parliament.uk/bills/4019) [https://bills.parliament.uk/bills/4019](https://bills.parliament.uk/bills/4019).

- Third Reading in the House of Commons follows the Report stage. Because the Report stage has not yet taken place (its date is still "to be announced"), the Third Reading has necessarily not taken place [https://bills.parliament.uk/bills/4019/stages](https://bills.parliament.uk/bills/4019/stages) [https://bills.parliament.uk/bills/4019](https://bills.parliament.uk/bills/4019).

Deadline confirmation: The tracker was last reflected as of 30 June–1 July 2026 and shows no Third Reading entry for the House of Commons. Since the Report stage — a prerequisite that must precede Third Reading — has no scheduled date and had not occurred, it is impossible for a Third Reading to have taken place by the 11:59 PM UTC, 1 July 2026 deadline. Report stage being merely "date to be announced" confirms the Commons had not even scheduled the stage that must precede Third Reading, so the deadline could not be met regardless of any remaining sitting time on 1 July 2026 [https://bills.parliament.uk/bills/4019/stages](https://bills.parliament.uk/bills/4019/stages) [https://bills.parliament.uk/bills/4019](https://bills.parliament.uk/bills/4019) [https://bills.parliament.uk/bills/4019](https://bills.parliament.uk/bills/4019).

Therefore no "Third Reading" entry exists in the House of Commons within the specified window (12 May 2026 – 1 July 2026), and the question resolves NO.

Direct URL to evidence: https://bills.parliament.uk/bills/4019 (and stages detail: https://bills.parliament.uk/bills/4019/stages).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-7. `d9696e36-8d71-5946-ba3c-8c8f4fed03ee`

- Present date: `2026-05-29 04:32:15.144858`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Canadian government announce new retaliatory tariffs on any category of U.S. goods between May 12, 2026, and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026 (00:00 UTC) and on or before July 1, 2026 (23:59 UTC), the Government of Canada formally announces the imposition of new retaliatory tariffs on any category of U.S. goods. It resolves **No** otherwise.

**Definitions:**

- **"Retaliatory tariffs"**: Any new surtax, surcharge, or customs duty imposed by the Government of Canada on imports of U.S.-origin goods, where the Canadian government explicitly identifies the measure as a response to, or countermeasure against, U.S. trade actions (tariffs, duties, or trade restrictions) targeting Canadian goods. Routine customs duty adjustments, anti-dumping duties, or countervailing duties imposed through standard trade remedy proceedings do not qualify.

- **"New category of goods"**: Any U.S.-origin goods not already listed on the Department of Finance Canada's "Complete list of U.S. products subject to counter tariffs" page (https://www.canada.ca/en/department-finance/programs/international-trade-finance-policy/canadas-response-us-tariffs/complete-list-us-products-subject-to-counter-tariffs.html) as of May 11, 2026 (23:59 UTC). An increase in the tariff rate on goods already subject to counter tariffs also qualifies.

- **"Announce"**: The measure must be formally announced via at least one of the following: (a) an Order in Council or regulation published in the *Canada Gazette* (https://canadagazette.gc.ca/), or (b) an official press release or news release published on the Department of Finance Canada newsroom (https://www.canada.ca/en/department-finance/news.html). A ministerial speech, media interview, or social media post alone does not qualify unless accompanied by one of the above formal publications. The announcement must occur within the resolution window; the tariffs themselves need not take effect within the window.

**Resolution source:** The *Canada Gazette* (https://canadagazette.gc.ca/) and/or the Department of Finance Canada newsroom (https://www.canada.ca/en/department-finance/news.html). If neither source contains a qualifying announcement by 23:59 UTC on July 1, 2026, the question resolves No.

**Pre-cutoff background**

Since early 2025, the United States and Canada have been engaged in an escalating trade war. The U.S. imposed tariffs on Canadian goods under the International Emergency Economic Powers Act (IEEPA), and Canada responded with retaliatory counter tariffs that eventually covered up to $155 billion worth of U.S. exports [2025–2026 United States trade war with Canada and Mexico](https://en.wikipedia.org/wiki/2025%E2%80%932026_United_States_trade_war_with_Canada_and_Mexico).

As of May 2026, Canada has significantly scaled back its retaliatory tariffs. Effective September 1, 2025, Canada removed 25% counter tariffs on most U.S. goods, retaining them only on **steel, aluminum, and automobiles** [Canada's response to U.S. tariffs on Canadian goods](https://www.canada.ca/en/department-finance/programs/international-trade-finance-policy/canadas-response-us-tariffs.html). The full list of 313 tariff line items currently subject to Canadian counter tariffs is published at: https://www.canada.ca/en/department-finance/programs/international-trade-finance-policy/canadas-response-us-tariffs/complete-list-us-products-subject-to-counter-tariffs.html [Complete list of U.S. products subject to counter tariffs - Canada.ca](https://www.canada.ca/en/department-finance/programs/international-trade-finance-policy/canadas-response-us-tariffs/complete-list-us-products-subject-to-counter-tariffs.html).

In February 2026, the U.S. Supreme Court struck down the IEEPA-based tariffs, and the U.S. House voted to repeal them (pending Senate approval) [2025–2026 United States trade war with Canada and Mexico](https://en.wikipedia.org/wiki/2025%E2%80%932026_United_States_trade_war_with_Canada_and_Mexico). However, new U.S. trade measures—including a proposed 10% global tariff effective February 24, 2026, and a threatened 100% blanket tariff on all Canadian imports—have kept the trade environment volatile. The CUSMA/USMCA joint review process is also ongoing, creating both escalation and de-escalation incentives.

Key context for forecasters: PM Carney's economic-nationalism agenda creates pressure to respond to U.S. provocations, but Canada also has strong incentives to appear reasonable ahead of formal CUSMA review talks. The Canadian government has previously demonstrated willingness to both escalate (phased strategy up to $155B) and de-escalate (September 2025 rollback).

**Current status page:** https://www.canada.ca/en/department-finance/programs/international-trade-finance-policy/canadas-response-us-tariffs.html

**Exact later resolution packet**

The question resolves **NO**. Between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), the Government of Canada did not formally announce any new retaliatory/counter tariffs on U.S. goods (nor a rate increase on goods already subject to counter tariffs) via the Canada Gazette or the Department of Finance Canada newsroom.

Evidence reviewed:

1. Department of Finance Canada newsroom (https://www.canada.ca/en/department-finance/news.html): A review of releases in the May–June 2026 window found no announcement imposing new retaliatory tariffs, or increasing counter-tariff rates, on U.S. goods framed as a countermeasure to U.S. trade actions [https://www.canada.ca/en/department-finance/news.html](https://www.canada.ca/en/department-finance/news.html).

2. The only two Finance Canada tariff-related releases in the window were both non-qualifying:
 - June 3, 2026 — "Canada to extend steel and aluminum tariff measures": This extends existing steel/aluminum tariff-rate quotas (TRQs) on imports from NON-CUSMA partners and continues horizontal tariff relief. It is a safeguard/anti-diversion measure against global excess capacity, NOT a countermeasure against U.S. trade actions, and it explicitly EXEMPTS the United States (and Mexico) from the TRQs. Hence it targets neither U.S. goods nor qualifies as retaliation [Canada to extend steel and aluminum tariff measures to support ...](https://www.canada.ca/en/department-finance/news/2026/06/canada-to-extend-steel-and-aluminum-tariff-measures-to-support-workers-and-businesses.html).
 - June 19, 2026 — "Canada announces provisional safeguard tariff on imports of canned vegetables": A 10% provisional safeguard surtax on global imports that explicitly EXCLUDES the United States (as well as Mexico, Israel, Chile, and developing countries) per Canada's trade obligations. Because it excludes U.S.-origin goods entirely and is a safeguard (not a countermeasure to U.S. tariffs), it does not qualify as a retaliatory tariff on U.S. goods [https://www.canada.ca/en/department-finance/news/2026/06/canada-announces-provisional-safeguard-tariff-on-imports-of-canned-vegetables-to-protect-canadian-producers.html](https://www.canada.ca/en/department-finance/news/2026/06/canada-announces-provisional-safeguard-tariff-on-imports-of-canned-vegetables-to-protect-canadian-producers.html) [U.S.–Canada Tariffs: Timeline of Key Dates and Documents | Blakes](https://www.blakes.com/insights/us-canada-tariffs-timeline-of-key-dates-and-documents/).

3. The Blakes "U.S.–Canada Tariffs: Timeline of Key Dates and Documents" (updated June 22, 2026) records only the June 19, 2026 canned-vegetables safeguard within the window, which excludes the U.S., and no U.S.-targeted retaliatory tariff [U.S.–Canada Tariffs: Timeline of Key Dates and Documents | Blakes](https://www.blakes.com/insights/us-canada-tariffs-timeline-of-key-dates-and-documents/).

4. The Wikipedia "Timeline of the 2025–2026 United States trade war with Canada" shows no announcement of new Canadian retaliatory tariffs on U.S. goods between May 12 and July 1, 2026 (the May 2026 entries were negotiation posture statements by PM Carney, not tariff impositions) [Timeline of the 2025–2026 United States trade war with Canada](https://en.wikipedia.org/wiki/Timeline_of_the_2025%E2%80%932026_United_States_trade_war_with_Canada).

The broader context (Canada scaled back counter tariffs September 1, 2025, retaining them only on steel, aluminum, autos; intensive CUSMA-review negotiations ongoing through the July 1, 2026 deadline) is consistent with Canada NOT imposing new retaliation during this window. No qualifying Canada Gazette Order in Council or Finance Canada release imposing new/increased U.S.-targeted counter tariffs was found. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-8. `fa200512-4bb4-5b4b-ad70-94d68896f0a5`

- Present date: `2026-05-14 01:18:29.120482`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-18T00:00:00`

**Question**

Will the Bangko Sentral ng Pilipinas (BSP) hold an off-cycle monetary policy meeting between May 12, 2026, and June 17, 2026?

**Resolution criteria**

This question resolves **Yes** if the Bangko Sentral ng Pilipinas (BSP) holds a Monetary Board meeting on monetary policy—meaning a meeting where an interest rate decision (to hold, raise, or cut the Target Reverse Repurchase Rate) is made or announced—on any date from May 12, 2026 through June 17, 2026 (inclusive, Philippine Time, UTC+8) that is **not** one of the six scheduled 2026 Monetary Board policy meeting dates.

An "off-cycle" or "unscheduled" meeting is defined as any Monetary Board meeting on monetary policy held on a date other than the six dates listed in the official 2026 BSP schedule of Monetary Policy Meetings (https://www.bsp.gov.ph/Pages/PriceStability/ScheduleOfMeetingsOfTheAdvisoryCommitteeAndMonetaryBoardOnMonetaryPolicy.aspx): February 19, April 23, June 18, August 27, October 22, and December 17, 2026.

The primary resolution source is the BSP's official Monetary Policy Decisions page: https://www.bsp.gov.ph/SitePages/PriceStability/MonetaryPolicyDecision.aspx. If a decision entry appears on that page marked as an "[Off-cycle meeting]" with a date between May 12 and June 17, 2026 (PHT), the question resolves **Yes**. If no such entry appears by 11:59 PM PHT on June 17, 2026, the question resolves **No**.

Routine adjustments to standing facility rates (e.g., overnight lending/deposit rates) that do not involve a formal Monetary Board policy meeting and RRP rate decision do **not** count.

**Pre-cutoff background**

The Bangko Sentral ng Pilipinas (BSP) Monetary Board sets the Philippines' monetary policy, including the Target Reverse Repurchase (RRP) Rate. The BSP maintains a pre-announced schedule of six policy meetings per year. For 2026, the scheduled meetings are: February 19, April 23, June 18, August 27, October 22, and December 17 [Monetary Policy - Bangko Sentral ng Pilipinas](https://www.bsp.gov.ph/Pages/PriceStability/ScheduleOfMeetingsOfTheAdvisoryCommitteeAndMonetaryBoardOnMonetaryPolicy.aspx).

As of May 12, 2026, the current policy rate (Target RRP Rate) is 4.50%, after the Monetary Board raised it by 25 basis points at its April 23, 2026 scheduled meeting [Monetary Policy Decisions](https://www.bsp.gov.ph/SitePages/PriceStability/MonetaryPolicyDecision.aspx). Philippine headline inflation surged to 7.2% in April 2026, up sharply from 4.1% in March, driven by an oil crisis—the highest level since March 2023.

Notably, the BSP already held one off-cycle meeting in 2026: on March 26, 2026, the Monetary Board convened an unscheduled meeting and decided to maintain the policy rate at 4.25% [Monetary Policy Decisions](https://www.bsp.gov.ph/SitePages/PriceStability/MonetaryPolicyDecision.aspx). This precedent demonstrates the BSP's willingness to act outside its regular calendar.

Since the April rate hike, conditions have intensified. The BSP raised emergency overnight bank lending/deposit facility rates on May 7-8, 2026. Multiple credible analysts—including Citi, DBS, and Standard Chartered—have publicly called for an off-cycle rate hike in May 2026, citing the peso's depreciation, surging inflation (BSP's own 2026 forecast revised to 6.3%), and the long gap until the next scheduled meeting on June 18. The BSP itself has signaled it "may resort to more drastic action if inflation expectations worsen."

The next scheduled Monetary Board policy meeting is June 18, 2026. This question asks whether the BSP will convene an additional, unscheduled meeting before that date.

**Exact later resolution packet**

The question resolves NO. It asks whether the BSP held an off-cycle (unscheduled) Monetary Board policy meeting — with an interest rate decision on the Target RRP Rate — on a date between May 12 and June 17, 2026 (inclusive, PHT) that is NOT one of the six scheduled 2026 dates (Feb 19, Apr 23, Jun 18, Aug 27, Oct 22, Dec 17).

Primary resolution source — BSP Monetary Policy Decisions page (https://www.bsp.gov.ph/SitePages/PriceStability/MonetaryPolicyDecision.aspx): The only 2026 monetary policy decisions listed are Feb 19, 2026 (scheduled; cut to 4.25%), March 26, 2026 ([Off-cycle meeting]; held at 4.25%), April 23, 2026 (scheduled; raised to 4.50%), and June 18, 2026 (scheduled; raised to 4.75%). There is NO decision entry — and specifically no entry marked "[Off-cycle meeting]" — with a date between May 12 and June 17, 2026 [Monetary Policy Decisions](https://www.bsp.gov.ph/SitePages/PriceStability/MonetaryPolicyDecision.aspx). Per the explicit resolution rule, "If no such [off-cycle] entry appears by 11:59 PM PHT on June 17, 2026, the question resolves No."

Corroboration:
- The June rate hike to 4.75% occurred at the regularly SCHEDULED June 18, 2026 meeting — a scheduled date, and BusinessWorld described it as the "second straight meeting" (i.e., April 23 → June 18, consecutive scheduled meetings, with no off-cycle meeting in between) [BSP raises interest rates by 25 bps for second straight ...](https://bworldonline.com/top-stories/2026/06/18/757606/bsp-raises-interest-rates-by-25-bps-for-second-straight-meeting/). Philstar likewise confirms the 4.75% hike took place on June 18, 2026 [BSP raises key interest rate by 25 basis points to 4.75% in ...](https://www.philstar.com/business/2026/06/18/2536130/bsp-raises-key-interest-rate-25-basis-points-475-june-2026).
- As of May 22, 2026, BSP Governor Remolona said the central bank was still merely "considering" an off-cycle rate hike and described it as a "toss-up" whether to move off-cycle or wait for the June 18 scheduled meeting — confirming no off-cycle meeting had occurred [Philippine central bank governor says it is considering off- ...](https://www.reuters.com/world/asia-pacific/philippine-central-bank-governor-says-it-is-considering-off-cycle-rate-hike-2026-05-22/). Numerous analyst notes (Citi, DBS, Deutsche Bank) discussed a possible off-cycle May/June hike, but these were forecasts; the actual hike came at the scheduled June 18 meeting.

Note on a minor discrepancy: The BSP Price Stability landing page rendered the June decision date as "June 17" in one place [Monetary Policy - Bangko Sentral ng Pilipinas Price Stability](https://www.bsp.gov.ph/SitePages/PriceStability/PriceStability.aspx), while the primary Monetary Policy Decisions page and all news sources (BusinessWorld URL /2026/06/18/, Philstar) give June 18, 2026, which is the scheduled meeting date (a Thursday, matching the official calendar "Jun 18 (Thu)"). This "June 17" is a landing-page formatting artifact, not evidence of an off-cycle meeting. Decisively, even setting the date quirk aside, the primary resolution source contains NO "[Off-cycle meeting]" entry in the May 12–June 17 window, which is exactly what the resolution criteria require for a YES. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-9. `297aef8b-6fa0-5ee0-888f-0a0774b1661a`

- Present date: `2026-05-13 23:37:28.773168`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-06-15T00:00:00`

**Question**

Will the 'No to a Switzerland with 10 million' initiative achieve a majority of cantons in the June 14, 2026 referendum?

**Resolution criteria**

This question resolves as **Yes** if the "No to a Switzerland with 10 million! (Sustainability Initiative)" achieves a majority of cantonal votes in the referendum held on June 14, 2026 (CET/CEST timezone). It resolves as **No** otherwise.

A "majority of cantons" is defined using Switzerland's 23-vote system: 20 full cantons each count as 1 vote, and 6 half-cantons (Obwalden, Nidwalden, Basel-Stadt, Basel-Landschaft, Appenzell Ausserrhoden, and Appenzell Innerrhoden) each count as 0.5 votes, totaling 23 votes. A cantonal majority is achieved if more than 11.5 cantonal votes are in favor (i.e., at least 12 out of 23).

Each canton's vote is determined by whether a majority of its voters voted "Yes" on the initiative.

Resolution is based on official results published by the Swiss Federal Chancellery at https://www.admin.ch/en/popular-vote-of-14-june-2026, even if results are still provisional as of the resolution date. If official results are not yet available by July 1, 2026 (00:00 UTC), resolution will be deferred until they are published.

**Pre-cutoff background**

On June 14, 2026, Swiss citizens will vote on the popular initiative "No to a Switzerland with 10 million! (Sustainability Initiative)," proposed by the right-wing Swiss People's Party (SVP), which seeks to cap Switzerland's permanent resident population at 10 million (https://www.admin.ch/en/sustainability-initiative).

In Switzerland, popular initiatives to amend the constitution require a "double majority" to pass: both a majority of the national popular vote and a majority of the cantons [Popular majority and majority of the cantons - Switzerland](https://www.ch.ch/en/votes-and-elections/votes/popular-majority-and-majority-of-the-cantons/). The cantonal majority is determined by a weighted system: each of Switzerland's 20 full cantons counts as one vote, and each of the 6 half-cantons (Obwalden, Nidwalden, Basel-Stadt, Basel-Landschaft, Appenzell Ausserrhoden, and Appenzell Innerrhoden) counts as half a vote, for a total of 23 cantonal votes. A cantonal majority requires more than 11.5 votes in favor (i.e., at least 12 votes) [Popular majority and majority of the cantons - Switzerland](https://www.ch.ch/en/votes-and-elections/votes/popular-majority-and-majority-of-the-cantons/). Each canton's vote is determined by the majority of its own voters.

As of the first SBC/gfs.bern poll published on May 8, 2026, the initiative is "too close to call," described as a "stalemate at all levels," with approximately 79% of respondents having a firm voting intention and 6% undecided. When asked to predict the outcome, 51% of respondents believe the initiative will be rejected [First SBC poll shows Swiss evenly split on capping population at ten ...](https://www.swissinfo.ch/eng/swiss-politics/10-million-initiative-poll-sees-neck-and-neck-race/91380506). SVP support is concentrated in rural, German-speaking cantons, while urban centers and French/Italian-speaking regions tend to oppose such initiatives. Swiss referendum proposals historically tend to lose support as voting day approaches. This geographic dimension makes the cantonal majority question partially independent from the popular vote outcome.

**Exact later resolution packet**

The question asks whether the "No to a Switzerland with 10 million! (Sustainability Initiative)" achieved a majority of cantons (at least 12 out of 23 weighted votes) in the referendum held on 14 June 2026. The answer is NO.

The vote took place as scheduled on 14 June 2026, so the question is not annulled. The initiative was rejected by both the popular vote and the cantonal majority.

Cantonal breakdown (Standesstimmen), from official Swiss Federal Statistical Office (FSO) popular-vote results: the initiative received support from 8 full cantons and 4 half-cantons, i.e. 8 + (4 × 0.5) = 10.0 weighted cantonal votes in favor; and was opposed by 12 full cantons and 2 half-cantons, i.e. 12 + (2 × 0.5) = 13.0 weighted votes against [fe2fb3, fd50f1]. The 10.0 + 13.0 = 23.0 total confirms these are the weighted counts.

Since 10.0 weighted cantonal votes in favor is below the required threshold of 12.0 out of 23, the initiative did NOT achieve a majority of cantons. This is equivalently reported as "10 cantons in favor and 13 opposed" (Library of Congress Global Legal Monitor, per Google answer box).

Nationally, the initiative also failed, receiving only 45.21% Yes votes (i.e., ~54.79% No) [fe2fb3, fd50f1]. This corroborates the widely reported ~55%/45% rejection (Reuters, BBC, Washington Post, swissinfo). Note: the official admin.ch results portal page (https://abstimmungen.admin.ch/en/details?proposalId=6860, referenced by the FSO/Federal Chancellery statistics) and the FSO popular-vote statistics page (https://www.bfs.admin.ch/bfs/en/home/statistics/politics/popular-votes.html) are the authoritative sources; the top-level https://www.admin.ch/en/popular-vote-of-14-june-2026 page describes the vote but links to these result details.

Therefore the initiative did not achieve a cantonal majority, and the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-10. `0d27e684-1770-578a-98d6-7fa0c753fe08`

- Present date: `2026-05-02 14:58:32.799859`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Japan's top currency diplomat Atsushi Mimura publicly use the word 'excessive' (過度な) to describe yen movements in an official statement between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if Atsushi Mimura, in his capacity as Japan's Vice Finance Minister for International Affairs (the top currency diplomat), uses the word "excessive" (English) or "過度な" (Japanese, *kado-na*) to describe yen or foreign exchange movements in an **official statement** on or after May 1, 2026 00:00 UTC and on or before June 1, 2026 23:59 UTC.

An "official statement" is defined as any of the following:
- A press conference or doorstep interview (ぶら下がり) conducted in an official capacity
- An official Ministry of Finance press release published at https://www.mof.go.jp/
- A verified direct quote attributed to Mimura in a major news outlet, specifically Reuters (https://www.reuters.com/), Bloomberg (https://www.bloomberg.com/), Nikkei, Kyodo News, or NHK

The statement must specifically use "excessive" or "過度な" in reference to currency/yen/foreign exchange movements or fluctuations. General use of the word in unrelated contexts does not count.

Statements made prior to May 1, 2026 00:00 UTC do not count, even if reported after that date.

If no such statement is reported by any of the above sources by June 1, 2026 23:59 UTC, the question resolves **No**.

Primary resolution sources:
- Japan Ministry of Finance official releases: https://www.mof.go.jp/english/policy/international_policy/convention/index.html
- Reuters FX coverage: https://www.reuters.com/markets/currencies/
- Bloomberg Japan coverage: https://www.bloomberg.com/asia

**Pre-cutoff background**

Japan's Ministry of Finance (MOF) employs a well-known "verbal intervention" escalation ladder when signaling potential currency market intervention. This ladder typically progresses through several stages of increasingly strong language:

1. **"Watching closely"** (注視している) — baseline monitoring language
2. **"One-sided movements"** (一方的な動き) — noting directional bias
3. **"Speculative moves"** (投機的な動き) — attributing moves to speculation
4. **"Excessive movements"** (過度な動き) — a critical escalation signaling intervention is imminent
5. **"Decisive action"** (断固たる措置) — the final warning before or concurrent with actual intervention

The use of the word "excessive" (過度な, *kado-na*) is a key inflection point in this ladder, often immediately preceding or accompanying actual yen-buying intervention.

**Current situation (as of May 1, 2026):** The USD/JPY exchange rate is approximately 156.5–157.0 yen per dollar, having sharply strengthened from above 160 on April 30, 2026 [Yen jumps sharply as Japan warns it is ready to intervene again](https://www.reuters.com/world/asia-pacific/japan-warns-speculative-yen-moves-signals-chance-more-intervention-2026-05-01/). Japan reportedly intervened in the currency market on or around April 30, 2026, after the yen weakened past the 160 level [Yen surges vs. US dollar after finance minister's warning](https://mainichi.jp/english/articles/20260430/p2g/00m/0bu/066000c). Finance Minister Satsuki Katayama warned that "the time for decisive action… is finally getting closer," while Vice Finance Minister for International Affairs Atsushi Mimura described his warning as "the final evacuation advisory" and stated that market players "fully understand what was meant by 'decisive action'" [Yen surges vs. US dollar after finance minister's warning](https://mainichi.jp/english/articles/20260430/p2g/00m/0bu/066000c). Notably, as of April 30–May 1, 2026, Mimura has not been reported as using the specific word "excessive" (過度な) to describe yen movements in his recent statements [Yen jumps sharply as Japan warns it is ready to intervene again](https://www.reuters.com/world/asia-pacific/japan-warns-speculative-yen-moves-signals-chance-more-intervention-2026-05-01/)[Yen surges vs. US dollar after finance minister's warning](https://mainichi.jp/english/articles/20260430/p2g/00m/0bu/066000c).

Whether Mimura escalates to using this specific term during May 2026 depends on whether the yen weakens again toward the 160 level or stabilizes near current levels. Japan's Golden Week holiday period (late April–early May) is historically a period of thin liquidity and potential yen volatility.

**Exact later resolution packet**

The question resolves NO. It requires Atsushi Mimura, in his capacity as Vice Finance Minister for International Affairs, to use the word "excessive"/"過度な" to describe yen/FX movements in an official statement between May 1, 2026 00:00 UTC and June 1, 2026 23:59 UTC, as reported by MOF, Reuters, Bloomberg, Nikkei, Kyodo, or NHK.

Mimura did make multiple official statements during this window, but in NONE of them did he use the word "excessive"/"過度な" in reference to currency movements:

- May 1, 2026 (Reuters): Mimura commented on the prior day's intervention, saying "Japan's Golden Week holidays have just started" and "There's no change to my view on markets," declining to comment on whether Japan intervened. No use of "excessive" [53f49b].
- May 7, 2026 (Reuters/Bloomberg/Japan Times/Asahi): Mimura said Japan's "focus, consistently and without change, is directed in all directions" (照準は全方位), that Tokyo "continues to see speculative moves," that IMF "free-floating" classification does not constrain intervention, and that he watches markets "with continued vigilance" (引き続き変わらぬ警戒感をもって注視). The word "excessive" appears only in reference to a past January statement by US Treasury Secretary Bessent, not Mimura [ede1d7][39ad37][652f7c][ce740a].
- Late May 2026 (Reuters, May 29): Coverage attributed to Mimura only the IMF "not a rule restricting the number of interventions" comment; "excessive" was used by a bank strategist (Aozora's Moroga) and Finance Minister Katayama, not Mimura [cb5ff5][2f3654].

During this window, the word "excessive"/"過度な" describing yen/FX was used by Finance Minister Satsuki Katayama and US Treasury Secretary Scott Bessent (e.g., the May 12 readout of the Bessent meeting referenced "過度な変動"), but the resolution criteria specifically require Mimura to use it. A Trading Economics news feed covering this period likewise attributed "excessive volatility" language to Katayama, not Mimura [51b37b].

The only documented instance of Mimura himself using "excessive volatility/過度なボラティリティ" language was on November 5, 2025 ("主な懸念は為替の過度なボラティリティ、水準ではない"), which is before the window and does not count [be11f5].

No qualifying statement by Mimura was found in any of the specified sources within the window, so the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-11. `309c0d3e-ea2b-5913-98c0-50772902b585`

- Present date: `2026-05-14 01:55:59.850389`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-25T00:00:00`

**Question**

Will the European Council conclusions from the June 18–19, 2026 meeting endorse operational guidance on Article 42(7) TEU (the EU mutual defence clause)?

**Resolution criteria**

This question resolves as **Yes** if the official European Council conclusions document published following the June 18–19, 2026 meeting contains language that explicitly "endorses," "approves," or "adopts" operational guidance (or substantially equivalent terms such as "blueprint," "practical guidance," or "implementation framework") on Article 42(7) TEU.

This question resolves as **No** if:
- The conclusions merely "welcome" progress, "take note of" the work, or "invite" further work on Article 42(7) without endorsing specific operational guidance; or
- The conclusions do not mention Article 42(7) operational guidance at all; or
- The June 18–19, 2026 European Council meeting does not take place or does not produce published conclusions by July 1, 2026, 23:59 UTC.

The resolution source is the official European Council conclusions, expected to be published at: https://www.consilium.europa.eu/en/european-council/conclusions/

For the purposes of this question, [Article 42(7) TEU](https://eur-lex.europa.eu/eli/treaty/teu_2012/art_42/oj) refers to the mutual defence clause of the Treaty on European Union.

**Pre-cutoff background**

Article 42(7) of the Treaty on European Union (TEU) is the EU's mutual defence clause. It states: "If a Member State is the victim of armed aggression on its territory, the other Member States shall have towards it an obligation of aid and assistance by all the means in their power" (see full text: https://eur-lex.europa.eu/eli/treaty/teu_2012/art_42/oj). Unlike NATO's Article 5, this clause currently lacks detailed operational plans or military response structures.

At the informal European Council summit in Cyprus on April 23–24, 2026, EU leaders agreed to "flesh out" the mutual assistance pact under Article 42(7) [EU to prepare blueprint for mutual assistance pact, amid NATO doubts](https://www.reuters.com/business/aerospace-defense/eu-prepare-blueprint-mutual-assistance-pact-amid-nato-doubts-2026-04-24/). The European Commission was tasked with preparing a "blueprint" on how the EU would respond if a member state triggers the clause, covering scenarios including hybrid attacks, conventional attacks, and situations where both Article 42(7) and NATO's Article 5 are triggered simultaneously [EU to prepare blueprint for mutual assistance pact, amid NATO doubts](https://www.reuters.com/business/aerospace-defense/eu-prepare-blueprint-mutual-assistance-pact-amid-nato-doubts-2026-04-24/). EU High Representative Kaja Kallas is overseeing the development of these scenarios [EU to prepare blueprint for mutual assistance pact, amid NATO doubts](https://www.reuters.com/business/aerospace-defense/eu-prepare-blueprint-mutual-assistance-pact-amid-nato-doubts-2026-04-24/).

The June 18–19, 2026 European Council meeting is the next scheduled summit where this work is expected to be presented. However, endorsement is not guaranteed: defence policy requires consensus, and several member states with neutral or non-aligned traditions (e.g., Ireland, Austria, Malta) may resist stronger collective defence commitments [https://pressreview.eu/european-council-18-19-june-2026-mff-2028-2034-budget-negotiation-box/](https://pressreview.eu/european-council-18-19-june-2026-mff-2028-2034-budget-negotiation-box/). The scope and ambition of the operational guidance could also be scaled back during negotiations. The broader geopolitical context—including uncertainty about U.S. commitment to NATO—is driving urgency on the issue [EU to prepare blueprint for mutual assistance pact, amid NATO doubts](https://www.reuters.com/business/aerospace-defense/eu-prepare-blueprint-mutual-assistance-pact-amid-nato-doubts-2026-04-24/).

**Exact later resolution packet**

The question resolves NO.

**The meeting occurred and conclusions were published in time.** The European Council of 18–19 June 2026 took place and adopted conclusions, published on the official Consilium website on 19 June 2026 (well before the 1 July 2026, 23:59 UTC deadline). The official resolution source is the conclusions document at https://www.consilium.europa.eu/media/r1rowtfb/en-20260619-european-council-conclusions.pdf [1ca76c, d7aec1], also covered by the Consilium press releases of 18 and 19 June 2026 [b3e868, 14163d].

**The conclusions contain NO mention of Article 42(7) operational guidance.** I obtained the complete verbatim text of the entire "European Defence and Security" section (paragraphs 41–47) of the conclusions [1ca76c]. That section does not contain the terms "Article 42(7)", "42.7", "mutual defence clause", "mutual assistance", "blueprint", "operational guidance", "practical guidance", or "implementation framework" anywhere. The topics covered are: defence readiness by 2030 (para 41); airspace violations / condemnation of the 29 May 2026 Russian drone incident in Romania and the "Eastern Flank Watch" project (para 42); hybrid attacks and the Drone/Counter-Drone Action Plan (para 43); complementarity with NATO (para 44); a list of defence-industrial and capability items — defence expenditure, capability coalitions, EDA, the European defence technological and industrial base, SAFE and EDIP instruments, the Defence Readiness Omnibus, military mobility, and EIB support (para 45); the safeguard on the specific security/defence character of certain Member States (para 46); and a commitment to return to these issues in October 2026 (para 47). None of these concern the Article 42(7) mutual defence clause or its blueprint/operational guidance. This was consistently confirmed across four independent extractions of the official documents [1ca76c, d7aec1, b3e868, 14163d].

**Verb analysis.** Even setting aside the absence of any Article 42(7) reference, the verbs the European Council uses throughout the defence section are the "passive"/non-endorsing kind: "calls for", "welcomes", "invites", "stresses", "reiterates", "looks forward to", "condemns", "recognises", "underlines" [1ca76c]. It never "endorses", "approves", or "adopts" any operational guidance/blueprint on Article 42(7).

**Conclusion.** Per the resolution criteria, the question resolves NO because "The conclusions do not mention Article 42(7) operational guidance at all." (And separately, no active endorsement verb is applied to any such guidance.) The antecedent conditions for a YES — explicit endorsement/approval/adoption of operational guidance, a blueprint, practical guidance, or an implementation framework on Article 42(7) TEU — are not met.

Direct URL of the resolution document: https://www.consilium.europa.eu/media/r1rowtfb/en-20260619-european-council-conclusions.pdf

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-12. `91f14139-ce9a-5d28-b703-a1c1c06b48f4`

- Present date: `2026-05-12 19:27:34.112878`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Walmart Connect launch its TikTok advertising integration within the Ad Center by July 1, 2026?

**Resolution criteria**

This question resolves YES if Walmart Connect officially launches or makes available a TikTok advertising integration within the Walmart Connect Ad Center (https://advertising.walmart.com/) such that self-serve advertisers can create, launch, or measure TikTok campaigns directly within the Ad Center workflow. The launch must occur on or after May 10, 2026, and on or before July 1, 2026, at 23:59 UTC, to exclude any prior integrations.

This question resolves NO if no such TikTok integration is publicly available or officially announced as live by 23:59 UTC on July 1, 2026.

Resolution will be determined by checking the Walmart Connect newsroom (https://www.walmartconnect.com/resources/articles/) or official Walmart Connect announcements. Credible industry reporting from sources such as Chain Store Age (https://chainstoreage.com/), eMarketer, or other major retail/advertising trade publications confirming the live availability of the integration will also be accepted.

**Pre-cutoff background**

Walmart Connect is Walmart's retail media network (https://www.walmartconnect.com/), which enables brands and sellers to advertise across Walmart's properties and beyond. The Walmart Connect Ad Center (https://advertising.walmart.com/) is a self-serve platform where advertisers can create, launch, optimize, and measure advertising campaigns.

On April 8, 2026, Walmart Connect launched a self-serve Meta (Facebook/Instagram) integration within the Ad Center, allowing advertisers to create and measure social media campaigns directly against Walmart sales data [Walmart Connect Launches Social Ads with Meta: April 2026](https://novadata.io/resources/news/walmart-connect-social-media-ad-center-meta-april-2026). In that same announcement, Walmart Connect stated that "TikTok self-service is planned to rollout this half," referring to the first half of 2026 [How we're expanding retail-powered social media - Walmart Connect](https://www.walmartconnect.com/resources/articles/2026/expanding-retail-powered-social-media). As of May 11, 2026, no official announcement has confirmed a specific launch date for the TikTok integration, and the feature does not appear to be live in the Ad Center yet.

The timing of the TikTok rollout is uncertain due to several factors: Walmart's execution pace on ad platform integrations, potential regulatory or political complications surrounding TikTok in the US, and the vague "this half" timeline which could mean anytime before end of June 2026—or could slip. The Meta integration took place on April 8, suggesting Walmart may need 2-3 months between platform launches, which would place TikTok around June-July 2026.

**Exact later resolution packet**

The question resolves NO: no TikTok self-serve advertising integration became publicly available or was officially announced as live within the Walmart Connect Ad Center between May 10, 2026 and July 1, 2026 (23:59 UTC).

Evidence:

1. Walmart Connect newsroom (https://www.walmartconnect.com/resources/articles/): A review of Walmart Connect's official articles page found NO announcement or press release confirming the launch/availability of a self-serve TikTok integration within the Ad Center as of July 1, 2026 [https://www.walmartconnect.com/resources/articles/](https://www.walmartconnect.com/resources/articles/). The resolution criteria designate this newsroom as the primary resolution source.

2. Walmart Connect's own article "How we're expanding retail-powered social media" (https://www.walmartconnect.com/resources/articles/2026/expanding-retail-powered-social-media) continues to state, per its current Google-indexed text, "Self-serve access is currently available for Meta and TikTok self-service is planned to rollout this half" — i.e., TikTok self-service remained a planned (not launched) capability, with only Meta live for self-serve.

3. Mars United Commerce's "Retail Media Roundup: June 2026" (published ~June 15, 2026; https://www.marsunited.com/retail-media-roundup-june-2026/) — the most recent industry roundup before the deadline — confirms that Walmart Connect advertisers "can now launch self-service campaigns powered by Walmart's shopper data on Meta," but does NOT report any live self-service TikTok integration within the Ad Center. It only references an add-to-cart feature and LiveRamp closed-loop measurement in a managed-service TikTok context, not self-serve Ad Center campaign creation [Retail Media Roundup: June 2026 - Mars United](https://www.marsunited.com/retail-media-roundup-june-2026/).

4. Chain Store Age (https://chainstoreage.com/walmart-expands-social-media-capabilities-retail-media-network), the April 8, 2026 announcement, stated that while Meta self-serve launched, the TikTok integration was only "planned to rollout... later in 2026" and was not yet live [Walmart expands social media capabilities of retail media network](https://chainstoreage.com/walmart-expands-social-media-capabilities-retail-media-network).

All checked sources (the two named resolution publications — the Walmart Connect newsroom and Chain Store Age — plus the eMarketer-referenced coverage and a June 15, 2026 industry roundup) consistently show that as of the July 1, 2026 deadline, only the Meta self-serve integration was live, and the TikTok self-serve integration had not launched or been announced as live within the Ad Center. Therefore the consequent condition for YES was not met, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-13. `02886efb-22f2-5622-8bc8-a78d909755ab`

- Present date: `2026-05-14 04:06:31.076117`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court grant certiorari in Danco Laboratories v. Louisiana (No. 25A1207) or GenBioPro v. Louisiana (No. 25A1208) by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026, and no later than 11:59 PM UTC on July 1, 2026, the U.S. Supreme Court issues an order granting certiorari in either *Danco Laboratories, LLC v. Louisiana* (No. 25A1207) or *GenBioPro, Inc. v. Louisiana* (No. 25A1208). This includes the Court treating the pending emergency applications as petitions for a writ of certiorari and granting them, or any other procedural mechanism by which the Court grants plenary merits review in either case.

This question resolves as **No** if no such order granting certiorari appears on the official docket by the deadline.

Resolution will be determined based on official Court orders or docket entries on the Supreme Court's docket pages:
- https://www.supremecourt.gov/docket/docketfiles/html/public/25a1207.html
- https://www.supremecourt.gov/docket/docketfiles/html/public/25a1208.html

**Pre-cutoff background**

The U.S. Supreme Court is considering emergency applications from mifepristone manufacturers Danco Laboratories (No. 25A1207) and GenBioPro (No. 25A1208) to vacate a May 1, 2026, order from the U.S. Court of Appeals for the Fifth Circuit that prohibits the mailing of mifepristone (the abortion pill) [25A1207 - Search - Supreme Court of the United States](https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/25a1207.html) [Docket for 25A1208 - Supreme Court](https://www.supremecourt.gov/docket/docketfiles/html/public/25a1208.html).

As of May 12, 2026, the Court has not granted certiorari in either case. The procedural status is as follows:
- **May 2, 2026:** Both cases were docketed as emergency applications [25A1207 - Search - Supreme Court of the United States](https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/25a1207.html) [Docket for 25A1208 - Supreme Court](https://www.supremecourt.gov/docket/docketfiles/html/public/25a1208.html).
- **May 4, 2026:** Justice Alito issued administrative stays of the Fifth Circuit's order in both cases, initially until May 11, 2026 [25A1207 - Search - Supreme Court of the United States](https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/25a1207.html) [Docket for 25A1208 - Supreme Court](https://www.supremecourt.gov/docket/docketfiles/html/public/25a1208.html).
- **May 7, 2026:** Louisiana filed its response, arguing that if the Court stays the Fifth Circuit order, it should treat the applications as petitions for certiorari and grant them for full briefing and oral argument before the summer recess [Louisiana urges Supreme Court to leave in place order barring ...](https://www.scotusblog.com/2026/05/louisiana-urges-supreme-court-to-leave-in-place-order-barring-mailing-of-abortion-pill/).
- **May 11, 2026:** Justice Alito extended the administrative stay until May 14, 2026 [25A1207 - Search - Supreme Court of the United States](https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/25a1207.html).

The Court faces several options: it could simply rule on the stay applications (granting or denying), or it could convert the emergency applications into petitions for certiorari and grant review on the merits. The Court has done this in prior cases (e.g., Title 42 immigration cases), but it is not routine. Louisiana has explicitly invited the Court to grant cert if it stays the lower court order [Louisiana urges Supreme Court to leave in place order barring ...](https://www.scotusblog.com/2026/05/louisiana-urges-supreme-court-to-leave-in-place-order-barring-mailing-of-abortion-pill/). Numerous amicus briefs have been filed [Docket for 25A1208 - Supreme Court](https://www.supremecourt.gov/docket/docketfiles/html/public/25a1208.html).

**Exact later resolution packet**

The question resolves NO because the U.S. Supreme Court granted only a STAY — not certiorari or plenary merits review — in both docket numbers before the July 1, 2026 deadline.

Evidence:
- Official SCOTUS docket for No. 25A1207 (https://www.supremecourt.gov/docket/docketfiles/html/public/25a1207.html): On May 14, 2026, the application for stay referred to the Court was granted. There are no subsequent docket entries granting certiorari or treating the application as a petition for a writ of certiorari and granting it [c939d0].
- Official SCOTUS docket for No. 25A1208 (https://www.supremecourt.gov/docket/docketfiles/html/public/25a1208.html): On May 14, 2026, the Court granted the stay application. The docket contains no entry granting certiorari or converting the emergency application into a granted cert petition by the July 1, 2026 deadline [bd52cb].
- The actual May 14, 2026 order (https://www.supremecourt.gov/opinions/25pdf/25a1207_21p3.pdf) states the exact disposition: "The applications for stay ... are granted. The May 1, 2026 order of the United States Court of Appeals for the Fifth Circuit ... is stayed pending disposition of the appeal in the United States Court of Appeals for the Fifth Circuit and disposition of a petition for a writ of certiorari, if such a writ is timely sought. Should certiorari be denied, this stay shall terminate automatically. In the event certiorari is granted, the stay shall terminate upon the sending down of the judgment of this Court." This is standard stay language conditioned on a FUTURE, not-yet-filed cert petition — it is not a grant of certiorari [7cb98e].
- SCOTUSblog's case page for GenBioPro v. Louisiana confirms the action was limited to granting the emergency stay application ("Supreme Court allows for access to abortion pill by mail for now," May 14, 2026), with no record of a cert grant between May 12 and July 1, 2026 [acdc52].

The resolution criteria require an order "granting certiorari," or the Court "treating the pending emergency applications as petitions for a writ of certiorari and granting them," or "any other procedural mechanism by which the Court grants plenary merits review." None of these occurred. The Court merely stayed the Fifth Circuit's order pending a possible future cert petition. Per the checklist, "If the court granted a stay but did not grant certiorari or plenary review, the resolution must be 'No'." Both docket numbers show identical outcomes, so neither triggers a YES. The question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-14. `0851f82c-aabd-57f0-abbb-4a23f99963c2`

- Present date: `2026-05-14 04:29:31.794317`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Knesset Constitution, Law and Justice Committee approve the "Associations Bill (Amendment—Donation from Foreign State Entity), 2024" for a first plenary reading by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the Knesset Constitution, Law and Justice Committee formally votes to approve the "Associations Bill (Amendment—Donation from Foreign State Entity), 2024" (or any substantively similar successor version of this bill prepared by the committee) for a first reading in the Knesset plenum. The approval must occur on or after May 12, 2026 (00:00 UTC+3, Israel Standard Time) and before July 1, 2026 (23:59 UTC+3).

"Approval" is defined as a formal recorded vote by the committee to report the bill to the Knesset plenum for its first reading, as documented in the official committee minutes or the Knesset National Legislative Database (https://main.knesset.gov.il/EN/activity/Pages/Legislation.aspx).

This question resolves as **No** if:
- The committee does not hold such a vote by June 30, 2026 (23:59 UTC+3); or
- The bill is withdrawn, merged into different legislation, or the committee votes against advancing it to the plenum.

Resolution will be determined by checking the official Knesset legislative database or the Constitution, Law and Justice Committee records at https://main.knesset.gov.il/en/activity/pages/committees.aspx. Credible reporting from major outlets (Haaretz, Jerusalem Post, Times of Israel, Reuters) may serve as supplementary confirmation.

**Pre-cutoff background**

On February 19, 2025, the Knesset Plenum approved the "Associations Bill (Amendment—Donation from Foreign State Entity), 2024" (commonly known as the "NGO foreign-funding tax bill"), sponsored by MK Ariel Kallner (Likud), in a preliminary reading by a vote of 47 to 19 [80% tax on donation from foreign state entity to non-profit ...](https://main.knesset.gov.il/en/news/pressreleases/pages/press19225d.aspx). The bill was then referred to the Constitution, Law and Justice Committee, chaired by MK Simcha Rothman, for deliberation before it can proceed to a first reading in the plenum.

The original bill proposed an 80% tax on donations from foreign state entities to non-profit associations not budgeted by the State of Israel [80% tax on donation from foreign state entity to non-profit ...](https://main.knesset.gov.il/en/news/pressreleases/pages/press19225d.aspx). As of July 2025, the committee was reviewing a significantly revised version: the tax rate was reduced to 23% (matching corporate tax rates) for NGOs engaged in political advocacy, while NGOs that formally declare they do not engage in political advocacy would be exempt. Organizations submitting false declarations would face double taxation, fines, and potential dissolution. Any NGO receiving foreign funding would also face increased petition fees when appealing to the High Court of Justice [Israel's Knesset works to revise NGO funding bill](https://www.jpost.com/israel-news/article-861766).

The bill has faced strong opposition from civil society groups including Adalah, which characterized it as an assault on civil society and the rule of law [Israel debates 80% tax on foreign donations to NGOs](https://www.reuters.com/world/middle-east/israel-debates-80-tax-foreign-donations-ngos-2025-05-05/). The Justice Ministry expressed reservations, stating the bill infringes on basic rights. Legislative bandwidth has been constrained by other priorities including the Haredi draft crisis and the 2026 budget.

As of May 13, 2026, the bill remains in the Constitution, Law and Justice Committee, where it must receive committee approval before advancing to a first reading in the Knesset plenum. The committee has held multiple debate sessions but has not yet voted to advance the bill.

Resolution source: Official Knesset legislative database at https://main.knesset.gov.il/EN/activity/Pages/Legislation.aspx and the Constitution, Law and Justice Committee portal at https://main.knesset.gov.il/en/activity/pages/committees.aspx

**Exact later resolution packet**

RESOLUTION: NO (0).

The question asks whether the Knesset Constitution, Law and Justice Committee held a formal recorded vote to approve the "Associations Bill (Amendment—Donation from Foreign State Entity), 2024" (the NGO foreign-funding tax bill by MK Ariel Kallner), or any substantively similar successor version, for a first plenary reading, specifically on or after May 12, 2026 and before July 1, 2026.

KEY EVIDENCE:

1. The complete list of press releases from the Constitution, Law and Justice Committee (comId=6) covering the entire resolution window shows NO vote on the Associations/NGO bill. The committee's documented activity during May–June 2026 was: May 14, 2026 – discussed October 7 commission of inquiry bill; May 19, 2026 – approved for first reading the Attorney General-splitting bill and a basic-laws amendment bill; May 25, 2026 – re-approved the AG-splitting bill for first reading; May 27, 2026 – joint committee approved a Police Investigations Department bill; June 10, 2026 – began preparing a "Jewish identity in public space" bill; June 30, 2026 – discussed a bill on AI/digital election campaign material. The last time the Associations Bill appeared in this committee's press releases was December 11, 2025 [a3d302].

2. As of December 10, 2025, the official Knesset press release confirms the committee was still merely "continuing to prepare" (להכין) the bill for a first reading — it had NOT yet held a vote to report it to the plenum [c646fd]. The resolution criteria explicitly distinguish committee deliberation/preparation from a formal recorded vote to advance the bill; only the latter counts.

3. In the resolution window itself, the Constitution Committee's late-June 2026 work (per press release press3062026q) concerned the "Elections for the Twenty-Sixth Knesset Bill (Special Provisions and Legislative Amendments), 2026," i.e., election-related legislation — not the Associations/NGO bill [6720e6].

4. Contextually, the Knesset was in the process of dissolving itself: the dissolution bill passed a preliminary reading 110-0 on May 20, 2026, the House Committee approved it for first reading on June 1, 2026, and it passed its first plenary reading 106-0 on June 4, 2026, heading to early elections. This freeze of the coalition's ordinary legislative agenda is consistent with the NGO bill not being advanced (Israel Policy Forum, June 4, 2026 [29b755]).

No source — the Knesset National Legislative Database, the Constitution/Law/Justice Committee portal, or credible reporting (JPost, Haaretz, Times of Israel, Reuters) — shows a committee vote to approve this bill for first reading between May 12, 2026 and June 30, 2026. Per the resolution criteria, since the committee did not hold such a vote by June 30, 2026 (23:59 UTC+3), the question resolves NO.

Primary sources:
- Constitution, Law and Justice Committee press releases (comId=6): https://m.knesset.gov.il/en/activity/committees/pages/pressreleases.aspx?comid=6 [a3d302]
- Dec 10, 2025 Knesset press release (bill still in preparation): https://main.knesset.gov.il/News/PressReleases/pages/press10122025n.aspx [c646fd]
- June 2026 Constitution Committee press release (election bill, not NGO bill): https://main.knesset.gov.il/EN/News/PressReleases/Pages/press3062026q.aspx [6720e6]
- Knesset dissolution timeline context: https://israelpolicyforum.org/2026/06/04/the-25th-knessets-11th-hour/ [29b755]

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-15. `dfa437fb-3ad7-5911-81a1-44e7cc139529`

- Present date: `2026-05-29 05:03:14.319022`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Turkey deploy ground forces into SDF/YPG-controlled areas of Hasakah or Qamishli districts in northeastern Syria between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves YES if, between May 12, 2026 00:00 UTC and July 1, 2026 23:59 UTC, Turkey deploys ground forces (regular military or Turkish-backed Syrian National Army forces operating under direct Turkish command) across the Syrian border into areas of the Hasakah Governorate that are controlled by the SDF/YPG as of May 12, 2026.

Specifically, a "ground force deployment" means the confirmed physical presence of Turkish Armed Forces personnel or Turkish-directed SNA units advancing into SDF/YPG-held territory within the Hasakah Governorate. This excludes:
- Routine border patrols on the Turkish side of the border
- Drone strikes or airstrikes without accompanying ground troop movement
- Artillery or rocket fire from Turkish territory
- Operations conducted solely by the Syrian transitional government's own forces without direct Turkish ground participation
- Turkish military activity in areas Turkey already occupies as of May 12, 2026

The deployment must occur on or after May 12, 2026 00:00 UTC to qualify.

Resolution will be based on reporting from at least two credible international news sources, such as:
- Reuters (https://www.reuters.com/world/middle-east/)
- Associated Press (https://apnews.com/hub/syria)
- Al Jazeera (https://www.aljazeera.com/where/syria/)
- BBC News (https://www.bbc.com/news/topics/cwlw3xz0lvvt)
- Syrian Observatory for Human Rights (https://www.syriahr.com/en/)

If no such deployment is reported by these sources by July 1, 2026 23:59 UTC, the question resolves NO.

**Pre-cutoff background**

In January 2026, the Syrian transitional government launched an offensive against the Kurdish-led Syrian Democratic Forces (SDF) in northeastern Syria, which concluded on January 30, 2026, with a comprehensive 14-point integration agreement [2026 northeastern Syria offensive - Wikipedia](https://en.wikipedia.org/wiki/2026_northeastern_Syria_offensive). Under this agreement, the SDF would gradually integrate its military forces and administrative institutions into Syrian state structures. Turkey supported the offensive and received assurances of US approval for operations against the SDF, contingent on protection of Kurdish civilians [2026 northeastern Syria offensive - Wikipedia](https://en.wikipedia.org/wiki/2026_northeastern_Syria_offensive).

As of May 2026, the Democratic Autonomous Administration of North and East Syria (DAANES) continues to exist but in diminished form. The SDF has ceded approximately 80% of its former territory, including the Raqqa and Deir ez-Zor governorates, to the Syrian government [SDF–Syrian transitional government clashes (2025–present)](https://en.wikipedia.org/wiki/SDF%E2%80%93Syrian_transitional_government_clashes_(2025%E2%80%93present)). The SDF retains control primarily in parts of the Hasakah governorate, including areas around the cities of Hasakah and Qamishli [2026 northeastern Syria offensive - Wikipedia](https://en.wikipedia.org/wiki/2026_northeastern_Syria_offensive).

Turkey views the SDF/YPG as a terrorist organization linked to the outlawed Kurdistan Workers' Party (PKK). Turkey has historically conducted multiple cross-border military operations into northern Syria (2016, 2018, 2019) and maintains an ongoing pattern of drone strikes and artillery attacks against SDF/YPG positions. The Turkish Parliament extended the government's authority to conduct military operations in Syria and Iraq for three more years in October 2025. Turkey currently provides reconnaissance support to the Syrian transitional government, including via Turkish Air Force drones [SDF–Syrian transitional government clashes (2025–present)](https://en.wikipedia.org/wiki/SDF%E2%80%93Syrian_transitional_government_clashes_(2025%E2%80%93present)).

The integration process faces significant challenges, including stalled prisoner exchanges and difficulties achieving military cohesion between SDF units and the Syrian Army [2026 northeastern Syria offensive - Wikipedia](https://en.wikipedia.org/wiki/2026_northeastern_Syria_offensive). A breakdown in the integration process or Turkish dissatisfaction with its pace could trigger a new Turkish ground operation into remaining SDF-held territory.

For the purposes of this question, "northeastern Syria" refers to the Hasakah Governorate (https://en.wikipedia.org/wiki/Al-Hasakah_Governorate), which encompasses the cities of Hasakah and Qamishli and constitutes the core remaining area of SDF/YPG control as of May 2026.

**Exact later resolution packet**

The question resolves NO. It asks whether, between May 12, 2026 00:00 UTC and July 1, 2026 23:59 UTC, Turkey deployed ground forces (regular Turkish military, or Turkish-backed SNA operating under direct Turkish command) across the border into SDF/YPG-controlled areas of the Hasakah Governorate (including Hasakah and Qamishli), with confirmed physical presence of ground troops. No such event was reported by any credible source within the window.

Key evidence:
- The Wikipedia article "SDF–Syrian transitional government clashes (2025–present)," which tracks these events and was last edited June 27, 2026, contains no mention of any Turkish ground force deployment (regular military or Turkish-directed SNA) into remaining SDF/YPG-held areas of Hasakah/Qamishli between May 12 and July 1, 2026. It only notes Turkey's continued reconnaissance/drone support, which the resolution criteria explicitly exclude [SDF–Syrian transitional government clashes (2025–present)](https://en.wikipedia.org/wiki/SDF%E2%80%93Syrian_transitional_government_clashes_(2025%E2%80%93present)).
- The Wikipedia article "2026 northeastern Syria offensive" (content through ~June 22, 2026) similarly documents only the January 2026 offensive, the January 30 integration agreement, and implementation steps; it reports no Turkish ground incursion into SDF-held Hasakah in the May–July window [2026 northeastern Syria offensive - Wikipedia](https://en.wikipedia.org/wiki/2026_northeastern_Syria_offensive).
- A Hawar News Agency (ANHA, an SDF-aligned outlet) article dated July 1, 2026 titled "4 ceasefire violations by interim govt factions amid Turkish shelling" describes only Turkish shelling (artillery) and ceasefire violations by Syrian interim-government/SNA factions — not any Turkish ground-troop advance into SDF territory. Artillery/shelling and drone/airstrikes without accompanying ground troop movement are explicitly excluded by the resolution criteria [4 ceasefire violations by interim govt factions amid Turkish shelling](https://hawarnews.com/en/4-ceasefire-violations-by-interim-govt-factions-amid-turkish-shelling).

Additional context that reinforces NO: The actual ground deployments into Hasakah and Qamishli in this period were carried out in early February 2026 by the Syrian transitional government's own Interior Ministry/security forces under the US-backed January 30 integration agreement (reported by Reuters, AP, Al Jazeera, Long War Journal), not by Turkey. Operations conducted solely by the Syrian government's own forces without direct Turkish ground participation are explicitly excluded by the resolution criteria. No credible international source (Reuters, AP, Al Jazeera, BBC, SOHR) reported a qualifying Turkish ground force deployment into SDF/YPG-controlled Hasakah between May 12 and July 1, 2026.

Because no qualifying Turkish ground-force deployment was reported by the deadline, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-16. `069fb1fe-06a9-5ded-8358-e2b928395697`

- Present date: `2026-05-02 12:10:21.884345`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-05-20 00:00:00`

**Question**

Will the Bank of Canada's Summary of Governing Council Deliberations for the April 29, 2026, decision mention a rate cut as having been actively considered?

**Resolution criteria**

This question resolves **Yes** if the official "Summary of Governing Council Deliberations" for the fixed announcement date of April 29, 2026, published on the Bank of Canada website (https://www.bankofcanada.ca/publications/summary-governing-council-deliberations/), contains language indicating that a reduction (cut) to the overnight rate target was actively considered as part of the April 29, 2026, policy decision. Specifically, the summary must contain phrasing such as "discussed the case for a cut," "considered a lower rate," "debated reducing the policy rate," "weighed the option of lowering," or substantively equivalent language indicating that a rate cut was a live option in the deliberations for this specific decision.

The question resolves **No** if:
- The summary is published and does not contain such language referring to the April 29, 2026, decision (general forward-looking guidance about possible future cuts, or references to past decisions to cut rates, do not count); or
- The summary is not published by June 1, 2026, 23:59 UTC.

All dates and deadlines are interpreted in UTC.

**Pre-cutoff background**

On April 29, 2026, the Bank of Canada announced it would maintain the target for the overnight rate at 2.25% (2¼%) [https://www.bankofcanada.ca/2026/04/fad-press-release-2026-04-29/](https://www.bankofcanada.ca/2026/04/fad-press-release-2026-04-29/). The decision came amid weak GDP growth and trade uncertainty. The Bank of Canada routinely publishes a "Summary of Governing Council Deliberations" approximately two weeks after each interest rate decision. For example, the March 18, 2026, deliberations summary was published on April 1, 2026. The April 29, 2026, deliberations summary is therefore expected to be published around mid-May 2026. These summaries provide detailed accounts of the factors and policy options the Governing Council considered, including whether alternative rate paths were discussed. The official publication page is: https://www.bankofcanada.ca/publications/summary-governing-council-deliberations/

**Exact later resolution packet**

The question resolves NO. The relevant source exists and is the official Bank of Canada “Summary of Governing Council deliberations: Fixed announcement date of April 29, 2026,” at https://www.bankofcanada.ca/2026/05/summary-of-governing-council-deliberations-fixed-announcement-date-of-april-29-2026/; the Bank of Canada publications index also lists that exact title and URL under its Summary of Governing Council deliberations publications [Summary of Governing Council deliberations: Fixed announcement ...](https://www.bankofcanada.ca/2026/05/summary-of-governing-council-deliberations-fixed-announcement-date-of-april-29-2026/) [Summary of Governing Council deliberations - Bank of Canada](https://www.bankofcanada.ca/publications/summary-governing-council-deliberations/). It was published on May 13, 2026, which is before the June 1, 2026, 23:59 UTC deadline, so the “not published by deadline” NO clause is not the basis for resolution [Summary of Governing Council deliberations: Fixed announcement ...](https://www.bankofcanada.ca/2026/05/summary-of-governing-council-deliberations-fixed-announcement-date-of-april-29-2026/) [Summary of Governing Council deliberations - Bank of Canada](https://www.bankofcanada.ca/publications/summary-governing-council-deliberations/).

On the substance, the official summary does not contain language indicating that a rate cut was actively considered as a live option for the April 29, 2026 policy decision. The relevant decision-specific wording is that members “agreed that the current degree of policy support was appropriate and therefore decided to maintain the policy interest rate at 2.25%” [Summary of Governing Council deliberations: Fixed announcement ...](https://www.bankofcanada.ca/2026/05/summary-of-governing-council-deliberations-fixed-announcement-date-of-april-29-2026/). The document does contain cut-related language, but it is forward-looking and conditional: “The policy interest rate might need to be cut further if the United States imposed new trade restrictions on Canada” [Summary of Governing Council deliberations: Fixed announcement ...](https://www.bankofcanada.ca/2026/05/summary-of-governing-council-deliberations-fixed-announcement-date-of-april-29-2026/). Under the resolution criteria, such general forward-looking guidance about possible future cuts does not count; what was required was phrasing such as “discussed the case for a cut,” “considered a lower rate,” “debated reducing the policy rate,” or substantively equivalent language showing that a cut was actively considered for this specific April 29 decision. The cited summary instead describes maintaining the rate as appropriate and only mentions a possible future cut under a future trade-restrictions scenario [Summary of Governing Council deliberations: Fixed announcement ...](https://www.bankofcanada.ca/2026/05/summary-of-governing-council-deliberations-fixed-announcement-date-of-april-29-2026/). Therefore the settled resolution is NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-17. `ff6e9a2c-091f-5eae-a9a1-1577928b6773`

- Present date: `2026-05-03 13:17:54.916370`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the reverse merger between General Fusion and Spring Valley Acquisition Corp. III officially close by June 1, 2026?

**Resolution criteria**

This question resolves YES if the business combination between General Fusion Inc. and Spring Valley Acquisition Corp. III officially closes on or before 23:59 UTC on June 1, 2026. "Officially close" is defined as either:

1. The filing of a Form 8-K with the U.S. Securities and Exchange Commission (SEC) by Spring Valley Acquisition Corp. III (CIK 0002074850) reporting the completion of the business combination (Item 2.01 — Completion of Acquisition or Disposition of Assets), searchable via SEC EDGAR at https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002074850&type=8-K&dateb=&owner=include&count=40; OR

2. An official press release issued by General Fusion or Spring Valley Acquisition Corp. III via GlobeNewsWire (https://www.globenewswire.com/) or a comparable major wire service explicitly confirming the closing of the transaction.

This question resolves NO if the merger has not officially closed by that date, or if either party announces the termination or cancellation of the agreement before that date.

**Pre-cutoff background**

On January 22, 2026, General Fusion Inc. and Spring Valley Acquisition Corp. III (NASDAQ: SVAC) announced a definitive business combination agreement, making General Fusion the first publicly traded pure-play fusion energy company [General Fusion to Become First Publicly Traded Pure-Play](https://www.globenewswire.com/news-release/2026/01/22/3223682/0/en/general-fusion-to-become-first-publicly-traded-pure-play-fusion-company-through-business-combination-with-spring-valley-acquisition-corp-iii.html). The deal implies an approximately US$1 billion pro-forma equity value, with General Fusion expected to receive up to $335 million in proceeds from the transaction, including approximately $105 million from a committed PIPE and $230 million from SVAC's trust capital (assuming no redemptions) [General Fusion to Become First Publicly Traded Pure-Play](https://www.globenewswire.com/news-release/2026/01/22/3223682/0/en/general-fusion-to-become-first-publicly-traded-pure-play-fusion-company-through-business-combination-with-spring-valley-acquisition-corp-iii.html). The combined entity plans to list on Nasdaq under the ticker symbol "GFUZ" [General Fusion to Become First Publicly Traded Pure-Play](https://www.globenewswire.com/news-release/2026/01/22/3223682/0/en/general-fusion-to-become-first-publicly-traded-pure-play-fusion-company-through-business-combination-with-spring-valley-acquisition-corp-iii.html).

The transaction was expected to close in mid-2026, subject to customary closing conditions including regulatory and shareholder approvals [General Fusion to Become First Publicly Traded Pure-Play](https://www.globenewswire.com/news-release/2026/01/22/3223682/0/en/general-fusion-to-become-first-publicly-traded-pure-play-fusion-company-through-business-combination-with-spring-valley-acquisition-corp-iii.html). A Form F-4 registration statement was publicly filed in February 2026, marking a key milestone toward completion.

General Fusion has faced significant financial instability leading up to this deal. In May 2025, the company laid off at least 25% of its staff due to cash shortages. In August 2025, it secured a $22 million "lifeline" investment to maintain operations while pursuing a path to go public [Struggling fusion power company General Fusion to go public via $1 ...](https://techcrunch.com/2026/01/22/struggling-fusion-power-company-general-fusion-to-go-public-via-1b-reverse-merger/). The company intends to use merger proceeds to complete its demonstration reactor, Lawson Machine 26 (LM26) [Struggling fusion power company General Fusion to go public via $1 ...](https://techcrunch.com/2026/01/22/struggling-fusion-power-company-general-fusion-to-go-public-via-1b-reverse-merger/).

As of May 2, 2026 (UTC), the merger has not yet closed. SEC filings (Form 425) continue to be made as recently as April 29, 2026, indicating the transaction remains active and pending. The originally stated target was "mid-2026" (Q2 2026), meaning a close by June 1, 2026 is possible but not certain given SPAC merger timelines, required shareholder votes, and potential redemption risks.

**Exact later resolution packet**

The question resolves NO because neither resolution condition was met by 23:59 UTC on June 1, 2026.

Condition 1 (SEC Form 8-K with Item 2.01): I reviewed the full Form 8-K filing history for Spring Valley Acquisition Corp. III (CIK 0002074850) on SEC EDGAR (https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002074850&type=8-K&dateb=&owner=include&count=40). The complete list of 8-K filings is: 2026-05-18 (Items 1.01, 9.01), 2026-04-29 (Items 7.01, 9.01), 2026-04-15 (Items 7.01, 9.01), 2026-04-06 (Items 7.01, 9.01), 2026-01-23 (Items 1.01, 3.02, 9.01), 2026-01-22 (Items 7.01, 9.01), 2025-09-11 (Items 8.01, 9.01), and 2025-09-08 (multiple items). NONE of these filings includes Item 2.01 (Completion of Acquisition or Disposition of Assets). The most recent filing before the deadline (2026-05-18) covered only Items 1.01 and 9.01, which is not a completion-of-acquisition report [https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002074850&type=8-K&dateb=&owner=include&count=40](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002074850&type=8-K&dateb=&owner=include&count=40).

Condition 2 (press release confirming closing): My Google searches for a closing/completion announcement returned only the original January 22, 2026 announcement of the definitive agreement and the February 2026 Form F-4 milestone press releases. As of the searches, all sources described the transaction as "targeted to close in mid-2026" / "expected to close in the second quarter of 2026," with no GlobeNewsWire or comparable wire-service release announcing that the business combination had actually closed. The transaction remained pending (F-4 amendments and Form 425 communications continued through April/May 2026).

Termination/cancellation check: I specifically searched for any termination or cancellation of the merger agreement. No such announcement was found; the deal remained active and pending, just not yet completed.

Since the deadline of June 1, 2026 has passed without either the required Item 2.01 Form 8-K or a wire-service press release confirming the actual closing, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-18. `bb016b0a-3c20-574a-a5a1-c4069fcb7fe2`

- Present date: `2026-05-03 01:36:25.412121`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Chinese government announce a new nationwide property stimulus measure between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 1, 2026 (00:00 Beijing Time, UTC+8) and before June 1, 2026 (23:59 Beijing Time, UTC+8), the Chinese government formally announces at least one new nationwide property stimulus measure.

**Definition of "announcement":** A formal policy document, official press release, or on-the-record statement by a cabinet-level or equivalent official (e.g., PBOC Governor, Minister of Housing and Urban-Rural Development, or State Council spokesperson) published on an official government channel.

**Definition of "nationwide":** The measure must apply uniformly across all provinces and municipalities of mainland China (i.e., not limited to specific cities or regions). Measures described as applying to all cities or setting a new national floor/ceiling qualify.

**Definition of "stimulus measure":** Any of the following policy actions targeting the property sector:
1. A reduction in the minimum down payment ratio for residential or commercial property mortgages below the current levels (below 15% for first homes, below 25% for second homes, or below 30% for commercial property).
2. A cut to the 5-year Loan Prime Rate (currently 3.50%) or a new nationwide mortgage interest rate subsidy or floor reduction.
3. A nationwide relaxation or removal of home purchase restrictions, including hukou-based purchasing requirements or limits on the number of properties an individual may own.
4. A nationwide increase in the maximum loan-to-value (LTV) ratio for property purchases.
5. A nationwide expansion of housing provident fund loan limits or eligibility.
6. A new nationwide fiscal subsidy for homebuyers (e.g., tax rebates, transaction fee waivers).

**Resolution sources:** Official announcements published on the following websites:
- State Council of the PRC: https://english.www.gov.cn/
- People's Bank of China (PBOC): http://www.pbc.gov.cn/en/3688110/index.html
- Ministry of Housing and Urban-Rural Development (MOHURD): https://www.mohurd.gov.cn/

If no qualifying announcement is found on these sources, credible English-language reporting from Reuters (reuters.com), Xinhua (english.news.cn), or Bloomberg confirming such an announcement also suffices.

If no qualifying announcement is made within the specified window, the question resolves **No**.

**Pre-cutoff background**

China has been rolling out property support measures to stabilize its struggling real estate sector. Key current policy benchmarks as of May 1, 2026 include:

- **Minimum down payment ratios**: 15% for first-home buyers, 25% for second-home buyers (residential); 30% for commercial property mortgages (lowered from 50% in January 2026) [https://english.www.gov.cn/news/202601/15/content_WS6968decdc6d00ca5f9a08978.html](https://english.www.gov.cn/news/202601/15/content_WS6968decdc6d00ca5f9a08978.html).
- **5-year Loan Prime Rate (LPR)**: 3.50%, unchanged for 11 consecutive months as of April 2026. The 1-year LPR stands at 3.00%.
- **Relending rates**: The 1-year relending rate was cut from 1.50% to 1.25% in January 2026 [https://english.www.gov.cn/news/202601/15/content_WS6968decdc6d00ca5f9a08978.html](https://english.www.gov.cn/news/202601/15/content_WS6968decdc6d00ca5f9a08978.html).

Despite these measures, China's new home prices continue to decline year-over-year, though month-over-month data showed some improvement in March 2026 in major cities. The 5-year LPR has been held steady since mid-2025 amid net interest margin pressure on banks. Trade tensions and geopolitical uncertainty (including Middle East conflict risks) add complexity to the policy outlook. China's 2026 government work report signaled continued property support, but resilient Q1 GDP growth has reduced the urgency for immediate further easing. Analysts remain divided on whether additional nationwide measures will be announced in the near term.

**Exact later resolution packet**

The question resolves NO. No qualifying NATIONWIDE central-government property stimulus measure (in any of the six defined categories) was announced between May 1 and June 1, 2026 (UTC+8).

Evidence reviewed:

1. 5-year LPR (the second qualifying category): Reuters reported on May 20, 2026 that China left the 5-year LPR unchanged at 3.50% (the 12th consecutive month), and the State Council's own site confirmed the over-five-year LPR was unchanged at 3.5%. So there was NO 5-year LPR cut in the window (https://www.reuters.com/business/finance/china-leaves-lending-benchmarks-unchanged-12th-month-may-2026-05-20/ and https://english.www.gov.cn/archive/statistics/202605/20/content_WS6a0d5ceec6d00ca5f9a0b1f1.html).

2. Down payment ratios / LTV: No central announcement lowered the benchmarks below 15% (first home), 25% (second home), or 30% (commercial). The most recent nationwide change was the January 2026 commercial-property down payment cut to 30% (referenced in the question itself); nothing further came in May.

3. Mortgage-rate reform: The PBoC's Q1 Monetary Policy Report (issued May 11, 2026) only contained an educational column signaling the central bank "might be gearing up" to change how mortgage rates are set — it was speculative/analytical, not a formal policy measure [8ca43e].

4. Purchase-restriction relaxation, provident-fund expansion, fiscal subsidies: Reuters (May 18 and May 29, 2026) confirms that the easing seen during May was CITY-SPECIFIC, not nationwide. Examples cited: Shenzhen eased home-purchase curbs in late April, Guangzhou introduced home-buying subsidies, and various cities (Wuhan "汉七条", Shanghai, Chengdu) optimized provident-fund limits locally. The articles explicitly note the central government's last major push was the early-March parliamentary meeting, and that policy priority was to "stabilise... rather than revive the sector through forceful stimulus" [22a532, 539d53].

5. The Xinhua article (May 26, 2026) on public rental housing concerned welfare/hukou access to public rental housing — not any of the six defined private-market stimulus categories [86dda6].

6. The State Council's "城市更新'十五五'规划" (Urban Renewal 15th Five-Year Plan), issued ~May 29, 2026, is a multi-year planning document mentioning deepening provident-fund reform and city-specific (因城施策) measures in general terms — not a concrete, immediately-effective nationwide stimulus measure of the defined types.

Since none of the six qualifying nationwide measures were formally announced by the central government within the window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-19. `b391d13e-3bcb-5d84-9bb2-9589ae6511be`

- Present date: `2026-05-03 12:12:57.396190`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a top-level U.S. official attend or participate in an IMEC-related meeting or summit between May 2, 2026, and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, between May 2, 2026, 00:00 UTC and June 1, 2026, 23:59 UTC, a top-level U.S. official attends or participates in an IMEC-related meeting or summit. Otherwise, it resolves as **No**.

**Definitions:**

- **Top-level U.S. official** means any of the following:
  - The President of the United States
  - The Vice President of the United States
  - Any Senate-confirmed Cabinet-level official (as listed at https://www.whitehouse.gov/administration/cabinet/), including the Secretary of State, Secretary of Commerce, Secretary of Transportation, Secretary of the Treasury, or U.S. Trade Representative
  - A designated Presidential Envoy or Special Envoy formally appointed by the President with a mandate covering infrastructure, trade corridors, or related portfolios (e.g., Special Presidential Coordinator for Global Infrastructure)
  - The National Security Advisor

- **IMEC-related meeting or summit** means any formal diplomatic or intergovernmental gathering where the India–Middle East–Europe Economic Corridor (IMEC) is explicitly referenced as a primary agenda item or the subject of a joint statement, communiqué, or official readout. Bilateral meetings where IMEC is merely mentioned in passing among many topics do not qualify; IMEC must be identified as a principal topic of discussion in the official readout or press release.

- **Attendance or participation** includes in-person attendance, virtual participation via video or telephone conference, or leading/sending a formal delegation. It does not include written statements, letters of support, or routine staff-level communications.

**Resolution sources:** Official press releases or readouts from the U.S. Department of State (https://www.state.gov/), the White House (https://www.whitehouse.gov/), or credible reporting from at least one of the following: Reuters (https://www.reuters.com/), Associated Press (https://apnews.com/), Bloomberg (https://www.bloomberg.com/), or The New York Times (https://www.nytimes.com/). If no qualifying event is reported by these sources by June 1, 2026, 23:59 UTC, the question resolves **No**.

**Pre-cutoff background**

The India–Middle East–Europe Economic Corridor (IMEC) is a multimodal infrastructure initiative announced at the 2023 G20 summit in New Delhi, designed to connect India, the Gulf states, and Europe through integrated rail, shipping, energy, and digital networks (https://en.wikipedia.org/wiki/India%E2%80%93Middle_East%E2%80%93Europe_Economic_Corridor). Initially stalled by the Gaza conflict, IMEC has regained momentum in 2026 amid rising tensions over the Strait of Hormuz and renewed interest in alternative trade routes [With Hormuz under strain, a trade corridor built for resilience faces a ...](https://fortune.com/2026/04/17/imec-india-middle-east-europe-corridor-hormuz-trade-supply-chain/).

As of early May 2026, U.S. engagement with IMEC is ongoing but uncertain at the senior level. President Trump has publicly praised the corridor, calling it "one of the greatest trade routes in history." A top Trump adviser, Ricky Gill, visited India for an IMEC-related summit in recent months [India–Middle East–Europe Economic Corridor In the Headlines - IMEC](https://www.imec.international/news-press-release/). However, the most recent confirmed U.S. government participation at a working level was Deputy Assistant Secretary of State Dane Johnston discussing IMEC with the Atlantic Council in mid-April 2026 [IMEC regains momentum as India, UAE & US look for new trade route](https://theprint.in/diplomacy/dead-on-arrival-to-revival-imec-regains-momentum-as-india-uae-us-look-for-new-trade-route/2906240/). Government "sherpas" from various countries are actively liaising to integrate existing projects into the IMEC framework [IMEC regains momentum as India, UAE & US look for new trade route](https://theprint.in/diplomacy/dead-on-arrival-to-revival-imec-regains-momentum-as-india-uae-us-look-for-new-trade-route/2906240/), but no specific Cabinet-level or above U.S. participation in an IMEC meeting has been publicly scheduled for May 2026 [India–Middle East–Europe Economic Corridor In the Headlines - IMEC](https://www.imec.international/news-press-release/). U.S.-India trade friction and competing regional priorities (Iran tensions, Hormuz) add uncertainty to whether high-level engagement will continue in the near term [With Hormuz under strain, a trade corridor built for resilience faces a ...](https://fortune.com/2026/04/17/imec-india-middle-east-europe-corridor-hormuz-trade-supply-chain/).

**Exact later resolution packet**

RESOLUTION: NO (0)

The question asks whether a top-level U.S. official attended or participated in an IMEC-related meeting/summit between May 2 and June 1, 2026, where IMEC was explicitly a PRINCIPAL topic/primary agenda item of the official readout or press release (not merely mentioned in passing).

The only event in the window involving a qualifying top-level U.S. official was Secretary of State Marco Rubio's visit to India (May 23–26, 2026), which culminated in the Quad Foreign Ministers' Meeting in New Delhi on May 26, 2026. Rubio is a Senate-confirmed Cabinet member, so the "top-level official" criterion is satisfied. However, IMEC was NOT a principal topic of any qualifying readout:

- The official Quad Foreign Ministers' Meeting Joint Statement (May 26, 2026), published by the U.S. Embassy in India, does not mention IMEC at all. It focused on maritime security, critical minerals, energy security, undersea cables, and port infrastructure [https://in.usembassy.gov/joint-statement-from-the-quad-foreign-ministers-meeting-in-new-delhi/](https://in.usembassy.gov/joint-statement-from-the-quad-foreign-ministers-meeting-in-new-delhi/).
- Reuters' coverage of the May 26 Quad meeting made no mention of IMEC; outcomes were a Fiji port, a critical minerals/energy pact, and Indo-Pacific maritime/energy initiatives [Australia-India-Japan-US Quad to build a port, unveil pact on critical ...](https://www.reuters.com/world/china/australia-india-japan-us-quad-seeks-relevance-foreign-ministers-meet-new-delhi-2026-05-26/).
- The Washington Post coverage of the May 26 Quad meeting listed topics as maritime security, critical minerals, port infrastructure, and energy security — no IMEC mention [Quad ministers announce new Indo-Pacific initiatives on maritime ...](https://www.washingtonpost.com/world/2026/05/26/india-quad-rubio/ca564ed8-58b7-11f1-8a9d-afb1148204e1_story.html).
- The CNBC report on the May 24 Rubio–Jaishankar bilateral listed topics as the Middle East, trade, visas, maritime security, and energy supplies — no IMEC mention [India, U.S. discuss Middle East, trade as Rubio cites progress on Iran](https://www.cnbc.com/2026/05/24/india-us-discuss-middle-east-trade-as-rubio-cites-progress-on-iran.html).
- The AP report on Rubio's India visit listed U.S.-India trade tensions, the Quad, energy diversification, and Hormuz maritime safety — no IMEC mention [Rubio's first official trip to India seeks to tackle a trust deficit | AP News](https://apnews.com/article/india-us-rubio-jaishankar-geopolitics-trump-modi-26b48aafbd262b85e7e8bf99c134e0d6).

The IMEC's own news/press release page showed no IMEC meeting involving a top-level U.S. official in the May 2–June 1, 2026 window (most recent items were from March 2026) [https://www.imec.international/news-press-release/](https://www.imec.international/news-press-release/).

Note: A separate IMEC-focused summit involving White House adviser Ricky Gill occurred in India, but that was in August 2025 — outside the resolution window. No qualifying IMEC-principal-topic event with a top-level U.S. official occurred during May 2–June 1, 2026 per the mandated sources.

Therefore, since IMEC was not identified as a principal topic/primary agenda item of any meeting attended by a qualifying official within the window, the question resolves NO.

Key source URLs:
- Quad Joint Statement (US Embassy India): https://in.usembassy.gov/joint-statement-from-the-quad-foreign-ministers-meeting-in-new-delhi/ [https://in.usembassy.gov/joint-statement-from-the-quad-foreign-ministers-meeting-in-new-delhi/](https://in.usembassy.gov/joint-statement-from-the-quad-foreign-ministers-meeting-in-new-delhi/)
- Reuters: https://www.reuters.com/world/china/australia-india-japan-us-quad-seeks-relevance-foreign-ministers-meet-new-delhi-2026-05-26/ [Australia-India-Japan-US Quad to build a port, unveil pact on critical ...](https://www.reuters.com/world/china/australia-india-japan-us-quad-seeks-relevance-foreign-ministers-meet-new-delhi-2026-05-26/)
- Washington Post: https://www.washingtonpost.com/world/2026/05/26/india-quad-rubio/ [Quad ministers announce new Indo-Pacific initiatives on maritime ...](https://www.washingtonpost.com/world/2026/05/26/india-quad-rubio/ca564ed8-58b7-11f1-8a9d-afb1148204e1_story.html)
- CNBC bilateral: https://www.cnbc.com/2026/05/24/india-us-discuss-middle-east-trade-as-rubio-cites-progress-on-iran.html [India, U.S. discuss Middle East, trade as Rubio cites progress on Iran](https://www.cnbc.com/2026/05/24/india-us-discuss-middle-east-trade-as-rubio-cites-progress-on-iran.html)
- AP News: Rubio India visit [Rubio's first official trip to India seeks to tackle a trust deficit | AP News](https://apnews.com/article/india-us-rubio-jaishankar-geopolitics-trump-modi-26b48aafbd262b85e7e8bf99c134e0d6)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-20. `72f98c43-a74c-5082-a4b9-c7f0283f4668`

- Present date: `2026-05-02 21:16:00.990615`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will ISW report a Russian battalion-sized or larger mechanized assault in the Chasiv Yar direction between May 1 and May 31, 2026?

**Resolution criteria**

This question resolves **Yes** if, in any ISW daily "Russian Offensive Campaign Assessment" published between May 1, 2026 (UTC) and May 31, 2026 (UTC) inclusive, ISW explicitly reports that Russian forces conducted a "battalion-sized" or larger mechanized assault in the Chasiv Yar direction. It resolves **No** otherwise.

**Key definitions:**

- **"Battalion-sized or larger"**: The assault must be explicitly described by ISW using the term "battalion-sized," "battalion-level," or a larger designation (e.g., "regimental-sized," "brigade-sized") in reference to a mechanized assault. ISW uses these terms in its daily reports to characterize the scale of ground assaults (as distinct from platoon-sized or company-sized). This question defers entirely to ISW's own characterization; no independent vehicle count or personnel estimate is required.

- **"Mechanized assault"**: An offensive ground operation involving armored vehicles (tanks, infantry fighting vehicles, or armored personnel carriers) as described by ISW. This excludes infantry-only assaults, positional engagements, drone-only attacks, and artillery/air strikes that are not part of a ground maneuver operation. ISW typically uses the terms "mechanized assault" or "mechanized and motorized assault" to describe such operations.

- **"Chasiv Yar direction"**: The geographic area ISW identifies as the "Chasiv Yar direction" or describes as assaults occurring in or near Chasiv Yar, including areas east, west, north, and south of Chasiv Yar proper (such as Stupochky, Novopivnichnyi Microraion, and Predtechyne), within the broader Kostyantynivka-Druzhkivka tactical area. The assault must be explicitly linked to Chasiv Yar or its immediate environs in ISW's reporting; assaults in other directions (e.g., Pokrovsk, Lyman) do not count.

**Primary resolution source**: ISW daily "Russian Offensive Campaign Assessment" reports, archived at https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-updates-3/.

**Fallback clause**: If ISW ceases publishing daily assessments during May 2026, or if ISW changes its methodology such that it no longer characterizes assault sizes by unit-size terminology (platoon/company/battalion), the question resolves **No** by default, unless an ISW summary or equivalent publication explicitly describes such an assault having occurred in the Chasiv Yar direction during May 2026.

**Pre-cutoff background**

As of late April 2026, Russian offensive operations in the Chasiv Yar direction have been characterized by small-unit tactics. ISW reported that Russian forces conducted two roughly platoon-sized mechanized assaults east of Chasiv Yar on April 18 and 19, 2026 [Russian Offensive Campaign Assessment, April 23, 2026 | ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-april-23-2026/), and a platoon-sized motorized assault south of Predtechyne (east of Kostyantynivka) on April 22, 2026 [Russian Offensive Campaign Assessment, April 23, 2026 | ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-april-23-2026/). Elements of the Russian 70th Motorized Rifle Division have been conducting assaults using armored vehicles and light motorized equipment in the area [Russian Offensive Campaign Assessment, April 21, 2026 | ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-april-21-2026/). Russian forces have been unable to enter settlements west and southwest of Chasiv Yar [Russian Offensive Campaign Assessment, April 21, 2026 | ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-april-21-2026/).

Elsewhere on the front, ISW reported a battalion-sized mechanized assault in the Lyman direction on March 19, 2026 [Russian Offensive Campaign Assessment, March 28, 2026 | ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-march-28-2026/), after which Russian forces reverted to small group infiltration tactics [Russian Offensive Campaign Assessment, March 28, 2026 | ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-march-28-2026/). A roughly company-sized mechanized assault was reported in the Zaporizhia direction on March 28, 2026 [Russian Offensive Campaign Assessment, March 28, 2026 | ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-march-28-2026/). Ukrainian forces also reportedly repelled a Russian battalion-sized mechanized assault near Avdiivka on March 30, 2026. Battalion-sized mechanized assaults have thus occurred in other sectors but not in the Chasiv Yar direction in recent months.

ISW publishes daily "Russian Offensive Campaign Assessment" reports that systematically track the scale of Russian assaults (platoon-sized, company-sized, battalion-sized) and categorize them by geographic direction, including the Chasiv Yar direction within the broader Kostyantynivka-Druzhkivka tactical area. These reports are available at https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-updates-3/.

**Exact later resolution packet**

The question resolves NO. Throughout May 2026, ISW's daily "Russian Offensive Campaign Assessment" reports characterized Russian operations in the Chasiv Yar direction (within the Kostyantynivka-Druzhkivka tactical area) as infiltration missions and small-group/positional engagements, NOT as battalion-sized or larger mechanized assaults.

Key evidence:
- An exhaustive review of the ISW archive page covering all daily reports from May 1–27, 2026 found NO explicit report of a "battalion-sized" or larger mechanized assault in the Chasiv Yar direction or its environs (Stupochky, Predtechyne, Chasiv Yar proper); ISW described activity there as positional engagements and infiltration [b2abbb].
- May 12: Only milblogger claims of Ukrainian forces entering Chasiv Yar; Russian activity = infiltration/shelling in Kostyantynivka-Druzhkivka, no battalion-sized mechanized assault [e69aef].
- May 13: Russian forces conducting "infiltration missions" using "small groups," no battalion-sized mechanized assault [0ee98a].
- May 14: Ukrainian counterattacks impeding Russian advances near Chasiv Yar; no battalion-sized mechanized assault [384261].
- May 15: Russian forces continued infiltration missions into Kostyantynivka; battalion-sized mechanized assaults mentioned only in other sectors (e.g., Zaporizhia/Hulyaipilske), not Chasiv Yar [0ff766].
- May 16: Russian forces "continued ground assaults in the Kostyantynivka-Druzhkivka tactical area but did not advance"; the only battalion-sized mechanized assault referenced was in the direction of Kauchuk (Kursk Oblast), unrelated to Chasiv Yar [669cbb].
- May 21: "Russian forces continued offensive operations in the Kostyantynivka-Druzhkivka tactical area but did not advance"; only shelling/glide bombs, no mechanized battalion assault [a525a2].
- May 28: Russian forces "continued infiltration missions within and near Kostyantynivka but did not advance"; no battalion-sized mechanized assault in Chasiv Yar direction [36ba68].
- May 30: Russian activity in Kostyantynivka-Druzhkivka described as "infiltration missions" with glide bombs/drone strikes; no battalion-sized mechanized assault [484440].
- May 31: Russian forces "continue to conduct infiltration missions in the Kostyantynivka-Druzhkivka tactical area"; no battalion-sized mechanized assault [ac576c].
- ISW's May 25 retrospective explicitly noted Russian forces had been unable to conduct operational maneuver and used small-unit infiltration tactics; it referenced only "occasional abortive battalion-, company-, and platoon-sized mechanized assaults over the years" but identified no battalion-sized assault in the Chasiv Yar direction during May 2026 [05dc14].

News reports of Russian armored convoys near Chasiv Yar in mid-May 2026 (e.g., Militarnyi May 13) described engagements involving roughly 20+ soldiers and small vehicle groups (a trailer/ATV), not characterized by ISW as a battalion-sized mechanized assault [07ba27].

No ISW report between May 1 and May 31, 2026 explicitly described a battalion-sized (or larger) mechanized assault in the Chasiv Yar direction. Per the resolution criteria, absence of such a report means the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-21. `7f5d5d22-2242-5bd2-bdd4-52561369221a`

- Present date: `2026-04-30 16:59:07.478991`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the IAEA report having regained on-site access to at least one of Iran's four declared enrichment facilities by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after April 30, 2026, and by 23:59 UTC on June 1, 2026, the IAEA publishes an official report, press release, or statement confirming that IAEA inspectors have conducted a physical on-site inspection, design information verification (DIV), or physical inventory verification (PIV) at any one of Iran's four declared enrichment facilities:

1. Fordow Fuel Enrichment Plant (FFEP)
2. Fuel Enrichment Plant (FEP) at Natanz
3. Pilot Fuel Enrichment Plant (PFEP) at Natanz
4. Isfahan Fuel Enrichment Plant (IFEP)

as identified in IAEA Board of Governors report GOV/2026/8 (https://www.iaea.org/sites/default/files/gov2026-8.pdf) [[PDF] NPT Safeguards Agreement with the Islamic Republic of Iran](https://www.iaea.org/sites/default/files/gov2026-8.pdf).

"Regaining access" requires **physical on-site presence** of IAEA inspectors at the facility for the purpose of verification activities. Remote monitoring data alone, or the mere re-installation of monitoring equipment without an inspector visit, does not qualify.

Resolution requires a **formal IAEA publication** (Board of Governors report, Director General statement, or official press release) confirming such access. Credible news reports (e.g., Reuters, AP) citing IAEA officials may be used as preliminary evidence, but the question does not resolve Yes until the IAEA itself confirms the access through an official channel listed at https://www.iaea.org/newscenter/focus/iran/iaea-and-iran-iaea-board-reports or https://www.iaea.org/topics/monitoring-and-verification-in-iran [https://www.iaea.org/topics/monitoring-and-verification-in-iran](https://www.iaea.org/topics/monitoring-and-verification-in-iran).

If no such IAEA confirmation is published by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

As of April 30, 2026, the International Atomic Energy Agency (IAEA) has had no access to any of Iran's four declared enrichment facilities since military strikes in June 2025. These four facilities are [[PDF] NPT Safeguards Agreement with the Islamic Republic of Iran](https://www.iaea.org/sites/default/files/gov2026-8.pdf):

1. **Fordow Fuel Enrichment Plant (FFEP)**
2. **Fuel Enrichment Plant (FEP)** at Natanz
3. **Pilot Fuel Enrichment Plant (PFEP)** at Natanz
4. **Isfahan Fuel Enrichment Plant (IFEP)**

According to the IAEA Board of Governors report GOV/2026/8 (dated February 27, 2026), Iran has not provided the Agency with access to any of these enrichment facilities since the June 2025 attacks, and the IAEA "cannot provide any information" on their current status [[PDF] NPT Safeguards Agreement with the Islamic Republic of Iran](https://www.iaea.org/sites/default/files/gov2026-8.pdf). Iran has argued that normal safeguards implementation is "legally untenable and materially impracticable" under current conditions [[PDF] NPT Safeguards Agreement with the Islamic Republic of Iran](https://www.iaea.org/sites/default/files/gov2026-8.pdf). Iran has facilitated access to other unaffected nuclear facilities, but all four enrichment sites remain off-limits.

As of mid-April 2026, IAEA Director General Grossi continued to urge Iran to allow inspections of its nuclear facilities as part of potential deal negotiations, but no access had been restored. The IAEA believes Iran's uranium stockpile remains buried at the Isfahan tunnel complex.

US-Iran negotiations are ongoing but contentious, and any deal restoring IAEA access would require significant diplomatic progress. The IAEA's next Board of Governors meeting (June 2026) would be a key moment for updated reporting, but interim statements or reports could also confirm any change in access status.

Resolution source: IAEA official reports and statements, available at https://www.iaea.org/newscenter/focus/iran/iaea-and-iran-iaea-board-reports and https://www.iaea.org/topics/monitoring-and-verification-in-iran [https://www.iaea.org/topics/monitoring-and-verification-in-iran](https://www.iaea.org/topics/monitoring-and-verification-in-iran).

**Exact later resolution packet**

The question resolves NO. It required an official IAEA publication (Board of Governors report, DG statement, or press release) issued between April 30 and June 1, 2026 (23:59 UTC) confirming that IAEA inspectors conducted a physical on-site inspection, DIV, or PIV at one of Iran's four declared enrichment facilities (FFEP Fordow, FEP Natanz, PFEP Natanz, or IFEP Isfahan).

No such IAEA confirmation was published:

1. The IAEA's own "IAEA and Iran – IAEA Board Reports" page lists no Board report newer than GOV/2026/8 (dated 27 February 2026); there are no entries for May or June 2026 [586633].

2. The IAEA "Chronology of Key Events" page likewise contains no entries between 2 March 2026 and 1 June 2026, so no IAEA-documented inspection of the enrichment facilities occurred in the resolution window [e74e4c].

3. GOV/2026/8 (the most recent IAEA report) states "Due to the lack of access to any of Iran's four declared enrichment facilities to perform verification activities the Agency cannot provide any information" — establishing the baseline of no access that the question asked whether it was reversed.

4. Throughout the resolution window the situation remained deadlocked. An Axios article (18 May 2026) confirmed US-Iran negotiations were stalled with no restoration of IAEA access to Fordow, Natanz, or Isfahan [301b22]. On 31 May 2026, the IAEA was still publicly "calling on Iran to urgently cooperate" and Grossi was still urging access, with no inspection having taken place (per multiple 30-31 May 2026 news items). Earlier, Iran had withdrawn (20 Nov 2025) from the September 2025 agreement to resume inspections.

5. Social-media posts referencing "Axios, May 6, 2026; Time, May 7, 2026" about "IAEA experts who walked into Natanz, Fordow, and Isfahan" could not be substantiated by any official IAEA publication, and the resolution criteria explicitly require IAEA's own confirmation through an official channel — which does not exist. News reports alone do not satisfy the criteria.

Since no formal IAEA publication confirmed physical on-site inspector presence at any of the four enrichment facilities by 23:59 UTC on June 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-22. `bc22ea66-ffbb-5ada-b4f3-bcb1d807a21a`

- Present date: `2026-05-29 00:59:14.373617`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Senate Agriculture Committee complete a formal markup of the Farm Bill by June 30, 2026?

**Resolution criteria**

This question resolves as **Yes** if the Senate Committee on Agriculture, Nutrition, and Forestry holds a formal markup of a farm bill (i.e., the primary legislative vehicle for reauthorizing farm, nutrition, and rural development programs) on or after May 12, 2026 and on or before June 30, 2026, 11:59 PM ET.

A "formal markup" is defined as a committee meeting officially designated as a "markup" or "business meeting" on the committee's [official hearings and meetings page](https://www.agriculture.senate.gov/hearings), during which members consider, amend, and vote on the text of the legislation. A hearing or roundtable that merely discusses the farm bill does not qualify.

The question resolves as **No** if no such markup occurs by the deadline.

**Resolution source:** The [Senate Agriculture Committee's official website](https://www.agriculture.senate.gov/hearings) or [Congress.gov](https://www.congress.gov/) committee activity records.

**Pre-cutoff background**

On April 30, 2026, the U.S. House of Representatives passed the Farm, Food, and National Security Act of 2026 by a vote of 224–200 [https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/](https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/). Attention has now shifted to the Senate, where Agriculture Committee Chairman John Boozman (R-AR) has said he is targeting the end of May or early June 2026 for a formal markup of the Senate's version of the farm bill [https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/](https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/).

However, several factors create genuine uncertainty about whether this timeline will hold. Key sticking points include disagreements over SNAP (Supplemental Nutrition Assistance Program) cost-sharing provisions—which Boozman has called a "nonstarter" for renegotiation—and debate over federal supremacy language for pesticide labeling, a provision stripped from the House bill [https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/](https://hpj.com/2026/05/08/with-house-farm-bill-passage-whats-the-outlook-in-the-senate/). Because any Senate farm bill ultimately needs 60 votes for cloture, Boozman needs Democratic support even at the committee stage to produce a viable bill. As of May 13, 2026, no markup has been scheduled on the committee's official calendar.

**Exact later resolution packet**

The question resolves **NO**: the Senate Committee on Agriculture, Nutrition, and Forestry did NOT hold a formal markup (or business meeting to consider/amend/vote on) a Farm Bill between May 12, 2026 and June 30, 2026, 11:59 PM ET.

Key evidence:

1. **Official Senate Agriculture Committee hearings page** (https://www.agriculture.senate.gov/hearings) lists all committee events for the relevant window: May 12, 2026 (Fertilizer Industry hearing), June 2, 2026 (Forest Service oversight hearing), June 8, 2026 (Business Meeting), and June 10, 2026 (USDA oversight hearing). None of these was a farm bill markup [https://www.agriculture.senate.gov/hearings](https://www.agriculture.senate.gov/hearings).

2. **The one "Business Meeting" (June 8, 2026)** — the only event in the window that could potentially qualify as a "business meeting" under the resolution criteria — was NOT a farm bill markup. Per the official committee page, its purpose was to consider the nomination of Glen Smith of Iowa to be Under Secretary of Agriculture for Rural Development. It did not involve considering, amending, or voting on the text of a farm bill [https://www.agriculture.senate.gov/hearings/business-meeting-06-08-2026](https://www.agriculture.senate.gov/hearings/business-meeting-06-08-2026).

3. **Timeline confirms no markup was possible before June 30.** Chairman John Boozman only released the Senate's draft farm bill text ("Agricultural Act of 2026" / "Farm Bill 2.0") on **June 23, 2026** [Senate Agriculture Committee Releases Draft Text for 2026 Farm Bill](https://www.hklaw.com/en/insights/publications/2026/06/senate-agriculture-committee-releases-draft-text-for-2026-farm-bill). Senate Ag Committee Democrats issued a statement on the "Farm Bill Discussion Draft" on June 23, 2026.

4. **The markup was explicitly scheduled for July**, after the July 4 recess:
   - Holland & Knight (June 26, 2026): "Chair John Boozman has indicated the Committee will move to mark up the draft after the Senate returns in mid-July from recess" [Senate Agriculture Committee Releases Draft Text for 2026 Farm Bill](https://www.hklaw.com/en/insights/publications/2026/06/senate-agriculture-committee-releases-draft-text-for-2026-farm-bill).
   - The Fence Post (citing The Hagstrom Report): the Senate draft would be released in June "but the markup will not be held before the July 4 recess" [Boozman: Farm bill draft in June, markup in July | TheFencePost.com](https://www.thefencepost.com/news/boozman-farm-bill-draft-in-june-markup-in-july/).
   - National Organic Coalition (June 10, 2026): Boozman had "tentatively scheduled a Farm Bill markup for July/August" [Farm Bill Update: Senate Farm Bill Markup Set for This Summer](https://www.nationalorganiccoalition.org/blog/2026/6/10/farm-bill-update-senate-farm-bill-markup-set-for-this-summer-heres-what-organic-advocates-need-to-know).
   - NACo (June 24, 2026): the Senate released its farm bill text on June 23, 2026, and were "expecting to mark up the bill in July." (The "20-hour markup" reported in search results referred to the HOUSE Agriculture Committee's action on March 5, 2026 on H.R. 7567, not the Senate) [Senate Agriculture Committee introduces 2026 Farm Bill, following ...](https://www.naco.org/news/senate-agriculture-committee-introduces-2026-farm-bill-following-house-passage).

Because no Senate committee markup or qualifying business meeting on the farm bill occurred on or before June 30, 2026 — the Senate only released draft text on June 23 and scheduled the markup for July — the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-23. `4fe12714-226c-5680-8c3b-a4745fbc2bd2`

- Present date: `2026-05-01 14:55:42.915999`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will an officially reported 'unsafe' or 'unprofessional' interaction between a Russian naval vessel and a NATO naval vessel occur in the Baltic Sea between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, between 00:00 UTC on April 30, 2026, and 23:59 UTC on June 1, 2026, at least one interaction between a Russian naval vessel and a NATO naval vessel in the Baltic Sea is officially described using the terms "unsafe," "unprofessional," "dangerous," or "aggressive" in an official statement or press release.

**Definitions:**

1. **"Unsafe" or "unprofessional" interaction:** An encounter explicitly characterized as "unsafe," "unprofessional," "dangerous," or "aggressive" in an official government or military press release or statement. These terms align with the language used in the U.S. Department of Defense's characterizations of military encounters and the Code for Unplanned Encounters at Sea (CUES, 2014), which establishes safety procedures and communication protocols for naval forces. An interaction includes but is not limited to: a vessel approaching within 500 meters of another in a threatening manner, crossing the bow or stern at close range, directing weapons or fire-control radar, or other maneuvers violating the International Regulations for Preventing Collisions at Sea (COLREGs, https://en.wikipedia.org/wiki/International_Regulations_for_Preventing_Collisions_at_Sea).

2. **Russian naval vessel:** A commissioned warship, corvette, frigate, destroyer, submarine, or auxiliary vessel officially operated by the Russian Navy (Военно-морской флот). Coast guard vessels operated by Russia's FSB Border Service are excluded unless explicitly identified as operating under Russian Navy command.

3. **NATO naval vessel:** A commissioned warship or auxiliary vessel operated by the navy of any NATO member state (https://www.nato.int/cps/en/natohq/nato_countries.htm), including vessels assigned to NATO standing maritime groups. Coast guard vessels are excluded unless explicitly operating under NATO or a NATO member's naval command.

4. **Baltic Sea:** The body of water as defined by the International Hydrographic Organization in *Limits of Oceans and Seas* (Special Publication N° 23, 3rd Edition, 1953) [[PDF] Limits of Oceans and Seas - EPIC](https://epic.awi.de/29772/1/IHO1953a.pdf), encompassing the waters bordered by Denmark, Sweden, Finland, Russia, Estonia, Latvia, Lithuania, Poland, and Germany, northeast of the defined boundary lines in the Little Belt, Great Belt, Guldborg Sound, and the Sound.

5. **Interaction:** A physical encounter at sea between vessels, including close approaches, maneuvering in proximity, verbal or radio contact during a confrontation, or the directing of weapons systems. Aircraft-to-ship encounters do NOT qualify; this question is restricted to vessel-to-vessel interactions.

**Resolution source:** An official press release or statement from NATO (https://www.nato.int/cps/en/natohq/news.htm), any NATO member state's Ministry of Defense, the U.S. Navy's 6th Fleet (https://www.c6f.navy.mil/Press-Room/News/), or the Russian Ministry of Defense (https://eng.mil.ru/). Credible reporting from Reuters, AP, or major newspapers citing official military sources also qualifies. If no such official report exists by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

Since January 2025, NATO has been conducting Operation Baltic Sentry (also referred to as Baltic Sentinel) to protect critical undersea infrastructure in the Baltic Sea, deploying warships, patrol aircraft, and naval drones. Simultaneously, Russia has increased naval activity in the region, deploying warships including the frigate Admiral Grigorovich to escort shadow fleet tankers, and senior Russian officials have threatened possible military action in the Baltic Sea.

The Baltic Sea, as defined by the International Hydrographic Organization (IHO) in *Limits of Oceans and Seas* (Special Publication N° 23, 3rd Edition, 1953), encompasses the waters bordered by Denmark, Sweden, Finland, Russia, Estonia, Latvia, Lithuania, Poland, and Germany, extending northeastward of defined lines in the Little Belt, Great Belt, Guldborg Sound, and the Sound [[PDF] Limits of Oceans and Seas - EPIC](https://epic.awi.de/29772/1/IHO1953a.pdf).

Historical precedent for such incidents exists. In November 2022, NATO reported that two Russian fighter aircraft conducted an "unsafe and unprofessional approach" toward Standing NATO Maritime Group 1 during routine operations in the Baltic Sea. Similar incidents involving Russian military aircraft and U.S. Navy ships in the Baltic have been reported multiple times (e.g., the USS Donald Cook incidents in 2016). However, naval vessel-to-naval vessel incidents (as opposed to aircraft-to-ship) are less frequently reported in official channels. The current elevated tempo of both Russian and NATO naval operations in the Baltic increases the probability of close encounters, but official characterization of an incident as "unsafe" or "unprofessional" remains contingent on specific circumstances and political dynamics.

Key resolution sources include:
- NATO Newsroom: https://www.nato.int/cps/en/natohq/news.htm
- U.S. Naval Forces Europe / U.S. 6th Fleet: https://www.c6f.navy.mil/Press-Room/News/
- Baltic state Ministries of Defense (e.g., Estonian MoD: https://kaitseministeerium.ee/en, Finnish MoD: https://www.defmin.fi/en)
- Russian Ministry of Defense: https://eng.mil.ru/

**Exact later resolution packet**

The question requires a strictly VESSEL-TO-VESSEL interaction between a Russian naval vessel and a NATO naval vessel in the Baltic Sea, occurring between 00:00 UTC April 30, 2026 and 23:59 UTC June 1, 2026, officially described as "unsafe," "unprofessional," "dangerous," or "aggressive" in an official statement or credible reporting citing official military/government sources.

My research found several adjacent events, but none satisfies ALL criteria:

1. The most prominent incident in the window — reported by Militarnyi on June 2, 2026 ("Provocation in the Baltic Sea: Russian Fighter Jet Flies Over German Frigate," and German MoD/Pistorius statements) — was an AIRCRAFT-to-ship encounter (a Russian fighter jet making a "dangerous approach" to the German frigate Hamburg). The resolution criteria explicitly exclude aircraft-to-ship encounters. The publication date is also June 2, 2026, after the window closed [3294e0].

2. The Russian destroyer Severomorsk loitered off Fehmarn in the Baltic Sea in early-mid May 2026 and was shadowed/monitored by NATO units including the German frigate Sachsen (SNMG1) and Danish navy. However, the coverage characterized this as "symbolic" presence and monitoring; no official statement described the vessel-to-vessel interaction using the required terms [bc2113].

3. The widely-cited Denmark report of Russian warships sailing on "collision courses," aiming weapons at Danish naval vessels, and "aggressive" maneuvers in the Baltic straits is from the Danish Defence Intelligence Service in October 2025 — well before the resolution window [82fcd5].

4. The tense standoff between the Russian destroyer Vice-Admiral Kulakov and the German frigate Bayern occurred in 2025 (article dated June 4, 2025), and was characterized by news outlets rather than an official military statement [e6e387].

5. An El País feature (May 25, 2026) on Baltic hybrid war explicitly noted "there are no fleet battles or classic naval engagements" in the region, describing the conflict as sabotage/shadow-fleet focused rather than vessel-to-vessel confrontations [d5d5d4].

No official press release from NATO, a NATO member's MoD, US 6th Fleet, or the Russian MoD (nor credible reporting citing them) was found describing a qualifying Russian-vs-NATO ship-to-ship interaction in the Baltic Sea within the April 30–June 1, 2026 window using the terms "unsafe," "unprofessional," "dangerous," or "aggressive." Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-24. `6391fee9-e6c1-5fa7-8631-2c68c0992883`

- Present date: `2026-05-02 12:02:27.175603`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-05-19 00:00:00`

**Question**

Will the European Commission's Spring 2026 Economic Forecast project euro area real GDP growth of 1.0% or higher for 2026?

**Resolution criteria**

This question resolves **Yes** if the European Commission's Spring 2026 Economic Forecast projects real GDP growth for the **euro area** for calendar year 2026 at 1.0% or higher (i.e., ≥1.0%, rounded to one decimal place as reported).

It resolves **No** if the projected real GDP growth rate is strictly below 1.0% (i.e., 0.9% or lower as reported).

The resolution source is the official European Commission Spring 2026 Economic Forecast report or its accompanying press release, expected to be published at [https://economy-finance.ec.europa.eu/economic-forecast-and-surveys/economic-forecasts_en](https://economy-finance.ec.europa.eu/economic-forecast-and-surveys/economic-forecasts_en). Specifically, resolution will be based on the headline euro area real GDP growth projection for 2026 as stated in the Statistical Annex (Table 1) or the executive summary of the forecast document.

If the Spring 2026 Economic Forecast is not published by 23:59 UTC on May 31, 2026, the question resolves **No**.

All relevant terms:
- **Real GDP growth**: The annual percentage change in gross domestic product adjusted for price changes, as [defined by Eurostat](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Real_GDP_growth_rate).
- **Euro area**: The [20 EU member states](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Euro_area) that have adopted the euro as their currency.
- **Spring 2026 Economic Forecast**: The European Commission's comprehensive spring forecast, published annually in May by the Directorate-General for Economic and Financial Affairs.

**Pre-cutoff background**

The European Commission publishes two comprehensive economic forecasts each year—one in spring (typically mid-May) and one in autumn. These forecasts include projections for real GDP growth ([defined by Eurostat as the percentage change in gross domestic product adjusted for inflation](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Real_GDP_growth_rate)), inflation, employment, and government debt for both the EU and the euro area ([the 20 EU member states that have adopted the euro](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Euro_area)).

In its Autumn 2025 Economic Forecast (published 17 November 2025), the Commission projected euro area real GDP growth of approximately 1.3% for 2026 [Economic forecast for Germany - Economy and Finance](https://economy-finance.ec.europa.eu/economic-surveillance-eu-member-states/country-pages/germany/economic-forecast-germany_en). Since then, economic conditions have deteriorated significantly. A new energy-driven supply shock linked to the war in the Middle East has dented growth prospects across Europe. The ECB's March 2026 staff projections revised euro area GDP growth for 2026 sharply downward to 0.9%, citing both lower intra-year dynamics and a smaller carry-over effect. The IMF's April 2026 World Economic Outlook cut its eurozone forecast to 1.1%, down from 1.4%. S&P Global Ratings forecasts 1.0% growth for both the euro area and the EU in 2026. Eurostat's flash estimate for Q1 2026 showed GDP increased by only 0.1% quarter-on-quarter in the euro area.

The Spring 2026 Economic Forecast is expected to be published in mid-May 2026. Given the range of recent projections (ECB at 0.9%, IMF at 1.1%, S&P at 1.0%), there is genuine uncertainty about whether the Commission's updated projection will reach 1.0%.

**Exact later resolution packet**

The antecedent publication condition was satisfied: the official European Commission Spring 2026 Economic Forecast page is dated 21 May 2026, before the deadline of 23:59 UTC on May 31, 2026 [Spring 2026 Economic Forecast: Slowdown in growth as energy ...](https://economy-finance.ec.europa.eu/economic-forecast-and-surveys/economic-forecasts/spring-2026-economic-forecast-slowdown-growth-energy-shock-drives-inflation_en). The official forecast PDF used for the substantive value is the European Commission report at https://economy-finance.ec.europa.eu/document/download/3360898c-cd40-46c0-b170-7adfcb993add_en?filename=ip341_en.pdf [Spring 2026 Economic Forecast: Slowdown in growth as energy ...](https://economy-finance.ec.europa.eu/economic-forecast-and-surveys/economic-forecasts/spring-2026-economic-forecast-slowdown-growth-energy-shock-drives-inflation_en) [[PDF] European Economic Forecast. Spring 2026 - Economy and Finance](https://economy-finance.ec.europa.eu/document/download/3360898c-cd40-46c0-b170-7adfcb993add_en?filename=ip341_en.pdf). In that official report, the Statistical Annex/Table 1 is titled “Spring 2026 Forecast - overview” and reports real GDP for “Euro area” for 2026 as 0.9% [[PDF] European Economic Forecast. Spring 2026 - Economy and Finance](https://economy-finance.ec.europa.eu/document/download/3360898c-cd40-46c0-b170-7adfcb993add_en?filename=ip341_en.pdf). The question’s threshold is 1.0% or higher, with 0.9% or lower resolving NO. Since the reported euro-area real GDP growth projection for calendar year 2026 is 0.9%, the question resolves NO (0) [[PDF] European Economic Forecast. Spring 2026 - Economy and Finance](https://economy-finance.ec.europa.eu/document/download/3360898c-cd40-46c0-b170-7adfcb993add_en?filename=ip341_en.pdf).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-25. `f0d071cf-f3d0-5b3b-8e35-1a84f4deb16a`

- Present date: `2026-05-29 06:29:01.118148`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will any AUSSOM troop-contributing country officially announce a reduction in their troop commitment to Somalia between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, between 00:00 UTC on May 12, 2026 and 23:59 UTC on July 1, 2026, any of the five current AUSSOM Troop-Contributing Countries (TCCs)—**Uganda, Ethiopia, Djibouti, Kenya, or Egypt**—officially announces a reduction in their troop commitment to AUSSOM.

**Definitions:**

- **AUSSOM:** The African Union Support and Stabilization Mission in Somalia, as defined at [https://au-ssom.org/en/about-aussom/](https://au-ssom.org/en/about-aussom/) and described in [https://en.wikipedia.org/wiki/African_Union_Support_and_Stabilization_Mission_in_Somalia](https://en.wikipedia.org/wiki/African_Union_Support_and_Stabilization_Mission_in_Somalia).

- **Troop-Contributing Countries (TCCs):** The five countries listed above (Uganda, Ethiopia, Djibouti, Kenya, Egypt), as identified on the AUSSOM Wikipedia page and official AU documentation.

- **Official announcement:** A public statement issued by any of the following:
  - The TCC's head of state, Ministry of Defense, or Ministry of Foreign Affairs (via official government website, press conference, or official social media account);
  - An official communiqué from the African Union Peace and Security Council ([https://www.peaceau.org](https://www.peaceau.org));
  - A formal report or resolution of the United Nations Security Council.
  Credible reporting by major international wire services (Reuters, AP, AFP) confirming such an announcement also qualifies.

- **Reduction:** A decrease in either (a) the number of troops currently deployed by that country to AUSSOM, or (b) that country's authorized/mandated troop ceiling for AUSSOM, relative to the baseline figures established as of the start of AUSSOM operations (Uganda: 4,500; Ethiopia: 2,500; Djibouti: 1,520; Kenya: 1,410; Egypt: 1,091) [African Union Support and Stabilization Mission in Somalia](https://en.wikipedia.org/wiki/African_Union_Support_and_Stabilization_Mission_in_Somalia). Routine troop rotations do not count; the announcement must explicitly reference a net decrease in troop numbers or commitment level.

If no such official announcement is made by any of the five TCCs by 23:59 UTC on July 1, 2026, the question resolves as **No**.

**Pre-cutoff background**

The African Union Support and Stabilization Mission in Somalia ([AUSSOM](https://au-ssom.org/en/about-aussom/)) began on January 1, 2025, succeeding the African Union Transition Mission in Somalia (ATMIS). Its mandate was renewed by UN Security Council Resolution 2809 (2025) until December 31, 2026 [About AUSSOM - African Union Support and Stabilization Mission in ...](https://au-ssom.org/en/about-aussom/). The mission's ultimate goal is to transfer full security responsibilities to Somali security forces by December 2029 through a phased approach [About AUSSOM - African Union Support and Stabilization Mission in ...](https://au-ssom.org/en/about-aussom/).

**Troop-Contributing Countries (TCCs) and current commitments:**
As of early 2026, AUSSOM's five TCCs and their authorized troop contributions are [African Union Support and Stabilization Mission in Somalia](https://en.wikipedia.org/wiki/African_Union_Support_and_Stabilization_Mission_in_Somalia):
- **Uganda:** 4,500 troops
- **Ethiopia:** 2,500 troops
- **Djibouti:** 1,520 troops
- **Kenya:** 1,410 troops
- **Egypt:** 1,091 troops

Note: Burundi withdrew from the mission in early 2025 over a troop allocation dispute [[PDF] What next for African Union peace operations in Somalia? - LSE](https://www.lse.ac.uk/ideas/Assets/Documents/updates/2025-SU-PMomanSomalia04.pdf).

Total authorized strength is approximately 11,900 uniformed personnel [African Union Support and Stabilization Mission in Somalia](https://en.wikipedia.org/wiki/African_Union_Support_and_Stabilization_Mission_in_Somalia). The drawdown schedule under the AUSSOM mandate called for reducing from 12,626 to 11,146 troops by the end of 2025 (a reduction of ~1,480 personnel).

**Funding crisis:** AUSSOM faces a severe funding shortfall. The mission's estimated annual budget is approximately $166.5–$196 million, mostly for TCC stipends [With AUSSOM's Funding Challenges Here to Stay, What Are the ...](https://theglobalobservatory.org/2026/01/with-aussoms-funding-challenges-here-to-stay-what-are-the-options-for-the-missions-future-in-somalia/) [[PDF] What next for African Union peace operations in Somalia? - LSE](https://www.lse.ac.uk/ideas/Assets/Documents/updates/2025-SU-PMomanSomalia04.pdf). As of January 2026, no funding had been pledged for 2026 [With AUSSOM's Funding Challenges Here to Stay, What Are the ...](https://theglobalobservatory.org/2026/01/with-aussoms-funding-challenges-here-to-stay-what-are-the-options-for-the-missions-future-in-somalia/). The UN Support Office in Somalia (UNSOS) saw its budget cut by approximately 25% following a US "pocket-rescission" request in August 2025 [With AUSSOM's Funding Challenges Here to Stay, What Are the ...](https://theglobalobservatory.org/2026/01/with-aussoms-funding-challenges-here-to-stay-what-are-the-options-for-the-missions-future-in-somalia/). In April 2026, the EU confirmed a contribution to AUSSOM, though the full funding gap remains [based on search results].

**Countervailing factors:** TCCs have bilateral security interests—Kenya's border security, Ethiopia's strategic depth, Uganda's military relationships—that incentivize maintaining their presence despite funding pressures [With AUSSOM's Funding Challenges Here to Stay, What Are the ...](https://theglobalobservatory.org/2026/01/with-aussoms-funding-challenges-here-to-stay-what-are-the-options-for-the-missions-future-in-somalia/). Egypt is a newer contributor actively deploying personnel [African Union Support and Stabilization Mission in Somalia](https://en.wikipedia.org/wiki/African_Union_Support_and_Stabilization_Mission_in_Somalia).

**Exact later resolution packet**

The question resolves **NO**: no AUSSOM troop-contributing country (Uganda, Ethiopia, Djibouti, Kenya, or Egypt) made an official announcement of a net reduction in its AUSSOM troop commitment during the resolution window of 00:00 UTC May 12, 2026 to 23:59 UTC July 1, 2026.

Key evidence:

1. The only major withdrawal-related development was Uganda's Chief of Defence Forces Gen. Muhoozi Kainerugaba's statement on **January 26, 2026** that Uganda intends to "completely withdraw" from Somalia. This predates the resolution window by nearly four months and therefore cannot satisfy the "between May 12 and July 1, 2026" requirement (https://peopledaily.digital/news/uganda-signals-full-troop-withdrawal-from-somalia-after-19-years) [Uganda signals full troop withdrawal from Somalia after 19 ...](https://peopledaily.digital/news/uganda-signals-full-troop-withdrawal-from-somalia-after-19-years); (https://hornreview.org/2026/01/27/ugandas-withdrawal-from-somalia-a-structural-shift-in-the-horn-of-africas-security-architecture/).

2. That January statement was, moreover, disowned/walked back: Gen. Muhoozi subsequently apologized, deleted the posts, and stated "We are going to continue our military cooperation as usual," and the status as official government policy was described as unclear (https://www.theeastafrican.co.ke/tea/news/east-africa/muhoozi-outbursts-expose-uganda-unease-funding-somalia-war-5345718) [Muhoozi's outbursts expose Uganda's unease with funding Somalia ...](https://www.theeastafrican.co.ke/tea/news/east-africa/muhoozi-outbursts-expose-uganda-unease-funding-somalia-war-5345718); the Amani Africa briefing likewise flagged that it was "unclear whether this reflects official government policy" (https://amaniafrica-et.org/briefing-on-the-situation-in-somalia-and-the-operations-of-aussom/) [Briefing on the Situation in Somalia and the operations of AUSSOM](https://amaniafrica-et.org/briefing-on-the-situation-in-somalia-and-the-operations-of-aussom/).

3. Sources covering the actual resolution window contain no official reduction announcement by any TCC. The Security Council Report June 2026 Monthly Forecast (drawing on the Secretary-General's report S/2026/446 circulated 29 May 2026) states AUSSOM continues to play a "critical enabling role," that the "existing footprint remains necessary to prevent security vacuums," and recommends "accelerated force generation" rather than a drawdown (https://www.securitycouncilreport.org/monthly-forecast/2026-06/somalia-43.php) [Somalia, June 2026 Monthly Forecast - Security Council Report](https://www.securitycouncilreport.org/monthly-forecast/2026-06/somalia-43.php) [Somalia, June 2026 Monthly Forecast - Security Council Report](https://www.securitycouncilreport.org/monthly-forecast/2026-06/somalia-43.php).

4. The Security Council Report "What's In Blue" piece on the 15 June 2026 private AUSSOM meeting likewise reports no reduction in TCC troop commitments during the window (https://www.securitycouncilreport.org/whatsinblue/2026/06/private-meeting-on-the-african-union-support-and-stabilization-mission-in-somalia-aussom.php) [Private Meeting on the African Union Support and Stabilization ...](https://www.securitycouncilreport.org/whatsinblue/2026/06/private-meeting-on-the-african-union-support-and-stabilization-mission-in-somalia-aussom.php).

5. Contemporaneous AUSSOM/UPDF materials from within the window show continued or reinforced engagement rather than reduction: UPDF news items dated 20 June 2026 and 31 May 2026 describe UPDF troops "urged to consolidate security gains" and launching a third phase of operations, and a 25 June 2026 AUSSOM communication still lists Uganda at its 4,500-troop baseline.

Because the resolution criteria require an official announcement (head of state, MoD, MFA, AU PSC communiqué, UNSC report, or Reuters/AP/AFP confirmation) of a net decrease made specifically within May 12–July 1, 2026, and none exists, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-26. `97b7a6bc-9b95-5b72-9d44-b68293be5063`

- Present date: `2026-05-01 17:25:44.128908`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will at least 30 commercial oil tankers transit the Strait of Hormuz in a single 24-hour period between April 30 and May 31, 2026?

**Resolution criteria**

This question resolves YES if, on any calendar day (00:00–23:59 UTC) between April 30, 2026 and May 31, 2026 (inclusive), at least 30 commercial oil tankers transit the Strait of Hormuz. It resolves NO otherwise.

Definitions:
- **Strait of Hormuz**: The narrow waterway between Iran and Oman connecting the Persian Gulf to the Gulf of Oman, centered approximately at 26°34'N, 56°15'E, spanning the navigable channel between the coasts of Iran and Oman (approximately 56°00'E to 56°30'E longitude).
- **Commercial oil tanker**: Any vessel classified as a crude oil tanker or oil/chemical tanker in maritime tracking databases, regardless of flag state, with a deadweight tonnage (DWT) of at least 10,000 tonnes. This includes laden and ballast voyages.
- **Transit**: A vessel passing through the strait in either direction (inbound to or outbound from the Persian Gulf).

The opening must occur on or after April 30, 2026.

**Resolution source**: Reuters shipping data (https://www.reuters.com/business/energy/), Lloyd's List (https://www.lloydslist.com/), or TankerTrackers.com (https://tankertrackers.com). If these sources report that 30 or more commercial oil tankers transited in a single UTC day during the resolution window, the question resolves YES. If no credible source reports this threshold being met by May 31, 2026 (23:59 UTC), the question resolves NO.

**Pre-cutoff background**

The Strait of Hormuz, located between Iran and Oman (approximately 26°34'N, 56°15'E), is the world's most critical oil transit chokepoint, historically handling roughly 20% of global oil supply. Before the U.S.-Iran war began on February 28, 2026, the strait typically saw 125–140 ship transits daily [Iran oil tankers turned back by US blockade, Hormuz traffic sparse](https://www.reuters.com/world/middle-east/shipping-traffic-through-hormuz-remains-muted-with-no-us-iran-deal-sight-data-2026-04-27/). Iran effectively closed the strait in mid-March 2026 in response to U.S.-Israeli airstrikes, triggering the largest oil supply disruption in history. The IEA's April 2026 Oil Market Report identified the strait's reopening as "the single most important variable" for global energy markets.

As of late April 2026, the strait remains largely closed. On April 17, Iran briefly declared the strait open, but closed it again within days after ceasefire talks stalled. As of April 27, 2026, only about 7 ships transited the strait in the prior 24 hours, none carrying oil for the global market [Iran oil tankers turned back by US blockade, Hormuz traffic sparse](https://www.reuters.com/world/middle-east/shipping-traffic-through-hormuz-remains-muted-with-no-us-iran-deal-sight-data-2026-04-27/). The U.S. military has been enforcing a blockade on Iran-related shipping since April 13, turning back 37 vessels [Iran oil tankers turned back by US blockade, Hormuz traffic sparse](https://www.reuters.com/world/middle-east/shipping-traffic-through-hormuz-remains-muted-with-no-us-iran-deal-sight-data-2026-04-27/). Iran has offered to reopen the strait if the U.S. lifts its blockade, but President Trump has signaled the blockade will continue. Ceasefire negotiations remain stalled, with no date set for U.S.-Iran talks.

Data sources for tracking strait traffic include Kpler, TankerTrackers.com (https://tankertrackers.com), Lloyd's List, and Reuters shipping data [Iran oil tankers turned back by US blockade, Hormuz traffic sparse](https://www.reuters.com/world/middle-east/shipping-traffic-through-hormuz-remains-muted-with-no-us-iran-deal-sight-data-2026-04-27/). Reuters publishes regular updates on tanker crossings at https://www.reuters.com/world/how-many-large-tankers-are-crossing-strait-hormuz-2026-04-24/ [How many large tankers are crossing the Strait of Hormuz? - Reuters](https://www.reuters.com/world/how-many-large-tankers-are-crossing-strait-hormuz-2026-04-24/).

**Exact later resolution packet**

The question resolves NO. It required that at least 30 commercial oil tankers (crude or oil/chemical tankers ≥10,000 DWT, both directions) transit the Strait of Hormuz in a single UTC calendar day between April 30 and May 31, 2026, verified by Reuters, Lloyd's List, or TankerTrackers.com.

Throughout the entire resolution window, the Strait of Hormuz was effectively closed/blockaded amid the 2026 U.S.-Iran war. Traffic was a tiny fraction of pre-war levels (pre-war ~125–140 transits/day).

Key evidence from the specified resolution sources:
- USNI News, citing Lloyd's List data, reported (May 1, updated May 2) that strait transits dropped to less than 10 percent of pre-conflict traffic, with daily transits in the SINGLE DIGITS — far below 30 [c60a40].
- Reuters' tracker "Oil and LNG tankers transiting Strait of Hormuz since start of Iran war" (updated May 28, based on LSEG and Kpler data) listed individual non-Iranian oil/LNG tanker crossings; the maximum on any single day was only about 2 tankers — nowhere near 30 [c44943, c2171a].
- Reuters' investigation (May 20) reported that fewer than 60 ships TOTAL (all vessel types) transited between April 18 and May 6, averaging ~3 ships/day, making 30 oil tankers in one day impossible [22de4a].
- Iran's own (likely inflated) IRGC claims peaked at "26 vessels" (May 20) [8fd00a] and at most "over 30/35 ships" on later dates [793d22] — but these counts were of ALL vessel types (container ships, cargo, etc.), not specifically oil tankers ≥10,000 DWT, and the oil tankers were a small subset.
- The U.S. naval blockade remained in effect from April 13 until May 29, 2026; even after it ended, no source reported 30+ oil tankers in a single day before the window closed on May 31 [9de2c5].
- CNBC (May 30) confirmed traffic had not returned to prewar levels and would at best reach only 60–70% in a future scenario [5fe286].

No credible source reported the 30-oil-tanker threshold being met on any single UTC day in the window, so the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-27. `8f1436c8-ba9b-52b7-81a3-2a7af0d0ef4a`

- Present date: `2026-05-01 16:58:34.075208`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the IAEA confirm that it has been granted access to inspect any Iranian nuclear facility affected by the June 2025 strikes, by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after April 30, 2026 (00:00 UTC), the International Atomic Energy Agency (IAEA) confirms—via an official Director General report to the Board of Governors, an official IAEA press statement, or a Director General public statement—that IAEA inspectors have been granted access to at least one Iranian nuclear facility affected by the June 2025 military strikes.

"Access" is defined as any of the following observable actions by IAEA inspectors at one or more of the affected facilities: (a) physical entry of inspectors into the facility or site, (b) environmental sampling at the facility or site, or (c) installation or servicing of monitoring/surveillance equipment at the facility or site.

The "facilities affected by the June 2025 strikes" are those identified in GOV/2026/8 (https://www.iaea.org/sites/default/files/gov2026-8.pdf): Fordow Fuel Enrichment Plant (FFEP), Fuel Enrichment Plant (FEP), Pilot Fuel Enrichment Plant (PFEP), Uranium Conversion Facility (UCF), Fuel Manufacturing Plant (FMP), Fuel Plate Fabrication Plant (FPFP), Enriched UO2 Powder Plant (EUPP), Khondab Heavy Water Research Reactor (KHRR), Isfahan Fuel Enrichment Plant (IFEP), and Heavy Water Production Plant (HWPP).

The confirmation must appear in an official IAEA source. The primary resolution sources are:
- IAEA Board Reports on Iran: https://www.iaea.org/newscenter/focus/iran/iaea-and-iran-iaea-board-reports
- IAEA Director General statements: https://www.iaea.org/newscenter/statements

If no such IAEA confirmation is published by June 1, 2026 (23:59 UTC), the question resolves as **No**.

**Pre-cutoff background**

In June 2025, the United States and Israel conducted military strikes on Iranian nuclear facilities between June 13–24, 2025 [[PDF] NPT Safeguards Agreement with the Islamic Republic of Iran](https://www.iaea.org/sites/default/files/gov2026-8.pdf). Following these strikes, IAEA inspectors withdrew from Iran, and Iran subsequently suspended cooperation with the Agency.

According to the February 2026 IAEA report (GOV/2026/8), the facilities affected by the June 2025 strikes include: Fordow Fuel Enrichment Plant (FFEP), Fuel Enrichment Plant (FEP), Pilot Fuel Enrichment Plant (PFEP), Uranium Conversion Facility (UCF), Fuel Manufacturing Plant (FMP), Fuel Plate Fabrication Plant (FPFP), Enriched UO2 Powder Plant (EUPP), Khondab Heavy Water Research Reactor (KHRR), Isfahan Fuel Enrichment Plant (IFEP), and Heavy Water Production Plant (HWPP) [[PDF] NPT Safeguards Agreement with the Islamic Republic of Iran](https://www.iaea.org/sites/default/files/gov2026-8.pdf).

As of the GOV/2026/8 report dated February 27, 2026, Iran has refused to allow IAEA inspectors access to any of these affected facilities [IAEA report says Iran must allow inspections, points at ...](https://www.reuters.com/world/middle-east/iran-stored-highly-enriched-uranium-underground-site-iaea-report-says-2026-02-27/). Iran has facilitated access to some unaffected facilities but not to sites where enrichment took place or that were damaged in the strikes [[PDF] NPT Safeguards Agreement with the Islamic Republic of Iran](https://www.iaea.org/sites/default/files/gov2026-8.pdf). The IAEA has specifically pointed to the Isfahan Nuclear Technology Center as a key site of concern, where Iran reportedly stored most of its highly enriched uranium at an underground tunnel complex [IAEA report says Iran must allow inspections, points at ...](https://www.reuters.com/world/middle-east/iran-stored-highly-enriched-uranium-underground-site-iaea-report-says-2026-02-27/).

On April 29, 2026, Bloomberg reported that the IAEA said Iran could access its entombed uranium stockpile, suggesting the situation at damaged sites remains unresolved. US-Iran nuclear talks have been ongoing in Geneva, raising the possibility—but not certainty—that a deal could include inspector access.

**Exact later resolution packet**

The question resolves NO. It required the IAEA to confirm, via an official Director General report, official press statement, or DG public statement, on or after April 30, 2026 and by June 1, 2026 (23:59 UTC), that inspectors were granted access (physical entry, environmental sampling, or installation/servicing of monitoring equipment) to at least one of the ten facilities affected by the June 2025 strikes (FFEP, FEP, PFEP, UCF, FMP, FPFP, EUPP, KHRR, IFEP, HWPP). No such confirmation was published.

Evidence:

1) The most recent official IAEA documentation distinguishes clearly between "unaffected" and "affected" facilities. The GOV/2026/8 report (Feb 27, 2026) and the DG's March 2-6, 2026 introductory statement to the Board of Governors state that "Iran continued to facilitate Agency access to facilities in Iran unaffected by the June 2025 attacks," while Iran did NOT permit access to the affected/damaged facilities (https://www.iaea.org/sites/default/files/gov2026-8.pdf; http://www.iaea.org/newscenter/statements/iaea-director-generals-introductory-statement-to-the-board-of-governors-2-6-march-2026). The IAEA chronology of key events contains no entries after March 2, 2026, and no entry confirming access to affected facilities in April-June 2026 [faf69c].

2) Independent monitoring confirms the status was unchanged through the resolution window. The ECFR "Iran nuclear monitor" entry for May 2026 explicitly states: "Iran has been blocking IAEA access to bombed facilities and has been stalling on its NPT obligations" [b7648d].

3) The BBC article on the US-Iran talks states Iran "has not allowed the IAEA inspectors to access the damaged sites" [8dd7ef].

4) On the question's own creation context, the April 29, 2026 Bloomberg report noted the situation at damaged sites remained unresolved (Iran said the IAEA "could access its entombed uranium stockpile" rather than confirmed access having occurred).

5) The late-May 2026 US-Iran diplomatic track (a proposed 60-day memorandum of understanding, reported May 29, 2026) had not been finalized and contained no confirmed provision—and certainly no IAEA confirmation—of inspector access to the damaged facilities [ab217d]. On May 27, Trump said both sides were "close" to a deal involving inspections, but no agreement was finalized and no IAEA access occurred by June 1, 2026.

No official IAEA source (DG report, press statement, or public statement) published between April 30, 2026 and June 1, 2026 confirmed that inspectors physically entered, took environmental samples, or installed/serviced monitoring equipment at any of the ten affected facilities. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-28. `b17b9a62-68a4-5e02-b9ca-bb87b54dfa45`

- Present date: `2026-05-03 00:56:31.472619`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the House Energy and Commerce Committee hold a hearing or markup on H.R. 8413, the SECURE Data Act, between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the House Energy and Commerce Committee holds an official hearing or markup session on H.R. 8413 (the SECURE Data Act) on or after May 1, 2026, and before June 1, 2026 (i.e., by 11:59 PM Eastern Time on May 31, 2026). Actions by subcommittees of the House Energy and Commerce Committee (such as the Subcommittee on Commerce, Manufacturing, and Trade) **do count** toward a positive resolution.

**Definitions:**
- A **hearing** is a formal meeting of a committee or subcommittee at which witnesses present testimony. See: [https://www.congress.gov/help/learn-about-the-legislative-process/committees](https://www.congress.gov/help/learn-about-the-legislative-process/committees)
- A **markup** is a committee or subcommittee session in which members debate, amend, and vote on proposed legislation. See: [https://rules.house.gov/about](https://rules.house.gov/about)

**Resolution sources:**
- The official House Energy and Commerce Committee hearings and markups calendar: [https://energycommerce.house.gov/hearings](https://energycommerce.house.gov/hearings)
- The Congress.gov bill status page for H.R. 8413: [https://www.congress.gov/bill/119th-congress/house-bill/8413](https://www.congress.gov/bill/119th-congress/house-bill/8413)

If neither source indicates that a hearing or markup on H.R. 8413 took place during the specified window, the question resolves **No**.

**Pre-cutoff background**

On April 22, 2026, members of the House Energy and Commerce Committee's Privacy Working Group introduced H.R. 8413, the "Securing and Establishing Consumer Uniform Rights and Enforcement over Data Act" (SECURE Data Act) [SECURE Data Act: Analysis of the new federal privacy bill - IAPP](https://iapp.org/news/a/secure-data-act-analysis-of-the-new-federal-privacy-bill). The bill proposes a comprehensive federal consumer privacy framework that would preempt state-level privacy laws, establish data minimization requirements, consumer data access and deletion rights, sensitive data protections, and FTC enforcement authority [https://privacymatters.dlapiper.com/2026/04/comprehensive-federal-privacy-legislation-introduced/](https://privacymatters.dlapiper.com/2026/04/comprehensive-federal-privacy-legislation-introduced/). The bill was crafted by a Privacy Working Group established by Committee Chairman Brett Guthrie (R-KY) in February 2025 [SECURE Data Act: Analysis of the new federal privacy bill - IAPP](https://iapp.org/news/a/secure-data-act-analysis-of-the-new-federal-privacy-bill).

As of May 1, 2026, the bill has been introduced but no specific hearing or markup date has been scheduled. The House Subcommittee for Commerce, Manufacturing, and Trade has indicated it "will soon schedule a legislative hearing," but no date has been set [https://privacymatters.dlapiper.com/2026/04/comprehensive-federal-privacy-legislation-introduced/](https://privacymatters.dlapiper.com/2026/04/comprehensive-federal-privacy-legislation-introduced/). CNBC reported momentum for "first votes to take place next month" (i.e., May 2026) [https://www.cnbc.com/2026/04/22/data-privacy-bill-congress-states.html](https://www.cnbc.com/2026/04/22/data-privacy-bill-congress-states.html). However, the bill lacks a private right of action—a key Democratic demand—creating uncertainty about whether bipartisan support will materialize for committee advancement [https://www.cnbc.com/2026/04/22/data-privacy-bill-congress-states.html](https://www.cnbc.com/2026/04/22/data-privacy-bill-congress-states.html) [https://privacymatters.dlapiper.com/2026/04/comprehensive-federal-privacy-legislation-introduced/](https://privacymatters.dlapiper.com/2026/04/comprehensive-federal-privacy-legislation-introduced/).

Previous federal privacy bills, including the American Data Privacy and Protection Act (ADPPA) in 2022, have stalled at the committee stage, making the outcome of this question genuinely uncertain.

**Exact later resolution packet**

The question resolves NO because no hearing or markup on H.R. 8413 (SECURE Data Act) was held by the House Energy and Commerce Committee or its subcommittees during the window of May 1, 2026 through 11:59 PM ET May 31, 2026.

Evidence from the two mandatory resolution sources:

1. Congress.gov bill status page (https://www.congress.gov/bill/119th-congress/house-bill/8413/all-actions): The only legislative actions recorded for H.R. 8413 are from April 21, 2026 — Introduced in the House and Referred to the Committee on Energy and Commerce (and additionally the Committee on the Judiciary). No hearing or markup actions appear during May 2026. The only committee meeting listed on the bill page is scheduled for June 3, 2026, at 10:15 AM, which is outside the resolution window [0a68c6].

2. House Energy and Commerce Committee hearings: The relevant hearing, titled "Examining Legislation to Establish a Federal Comprehensive Privacy and Data Security Law," held by the Subcommittee on Commerce, Manufacturing, and Trade, was scheduled for Wednesday, June 3, 2026. Although this hearing concerns H.R. 8413, it falls after the June 1, 2026 cutoff (i.e., after 11:59 PM ET May 31, 2026), so it does not count toward a YES resolution [741be0].

Because neither source indicates any hearing or markup on H.R. 8413 occurred during the specified May 2026 window — the only qualifying event (the June 3, 2026 subcommittee hearing) falls outside the window — the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-29. `c4a47c34-2572-512d-850a-c329bd0a14b7`

- Present date: `2026-05-03 02:01:19.288380`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a federal court issue a preliminary injunction or temporary restraining order blocking the Department of Education's PSLF employer eligibility rule between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if any United States federal court (i.e., a U.S. District Court or U.S. Court of Appeals) issues a preliminary injunction (https://www.law.cornell.edu/wex/preliminary_injunction) or temporary restraining order (https://www.law.cornell.edu/wex/temporary_restraining_order) on or after May 1, 2026, and before June 1, 2026, 11:59 PM ET, that stays, blocks, or enjoins the implementation or enforcement of the Department of Education's PSLF employer eligibility rule — specifically, the "substantial illegal purpose" provision published in the Federal Register on October 31, 2025 (Document No. 2025-19729), codified at 34 CFR 685.219.

This question resolves as **No** if no such court order is issued within that window.

For clarity:
- A "preliminary injunction" is a court order issued before trial to prevent a party from taking action, as defined by Cornell Law Institute (https://www.law.cornell.edu/wex/preliminary_injunction).
- A "temporary restraining order" (TRO) is an emergency court order to maintain the status quo, as defined by Cornell Law Institute (https://www.law.cornell.edu/wex/temporary_restraining_order).
- The order must be an official entry on the court docket.

**Resolution source:** Official federal court dockets via PACER (https://pacer.uscourts.gov/) or credible legal news reporting from Reuters (https://www.reuters.com/), Bloomberg Law (https://news.bloomberglaw.com/), or the Associated Press (https://apnews.com/) confirming the issuance of such an order.

**Pre-cutoff background**

On October 31, 2025, the U.S. Department of Education published a final rule revising the Public Service Loan Forgiveness (PSLF) program under the William D. Ford Federal Direct Loan Program (Federal Register Document No. 2025-19729; see https://www.federalregister.gov/documents/2025/10/31/2025-19729/william-d-ford-federal-direct-loan-direct-loan-program) [PSLF Final Rule Takes Effect in July 2026 - American Bar Association](https://www.americanbar.org/advocacy/governmental_legislative_work/publications/washingtonletter/november-25-wl/pslf-final-rule-1125wl/). The rule, scheduled to take effect July 1, 2026, grants the Secretary of Education authority to disqualify employers from PSLF eligibility if the organization is determined to have a "substantial illegal purpose" [https://www.forbes.com/sites/adamminsky/2026/04/08/student-loan-forgiveness-is-changing-in-just-84-days-with-major-consequences-expected/](https://www.forbes.com/sites/adamminsky/2026/04/08/student-loan-forgiveness-is-changing-in-just-84-days-with-major-consequences-expected/).

As of May 1, 2026, multiple lawsuits have been filed challenging the rule [PSLF Final Rule Takes Effect in July 2026 - American Bar Association](https://www.americanbar.org/advocacy/governmental_legislative_work/publications/washingtonletter/november-25-wl/pslf-final-rule-1125wl/):
- A coalition of 21 states and the District of Columbia, led by the Commonwealth of Massachusetts (complaint available at https://ag.ny.gov/sites/default/files/court-filings/commonwealth-of-massachusetts-v-u.s-department-of-education-complaint-2025.pdf);
- A lawsuit by the American Immigration Council and other nonprofit organizations;
- A coalition of cities, unions, and advocacy organizations.

At least three separate lawsuits have requested courts block the rule before it takes effect, with key hearings expected in the coming weeks as of April 2026 [https://www.forbes.com/sites/adamminsky/2026/04/08/student-loan-forgiveness-is-changing-in-just-84-days-with-major-consequences-expected/](https://www.forbes.com/sites/adamminsky/2026/04/08/student-loan-forgiveness-is-changing-in-just-84-days-with-major-consequences-expected/). Democrats have also introduced a Congressional Review Act resolution to rescind the rule. The rule's effective date of July 1, 2026 creates urgency for courts to act on injunctive relief requests in the May–June timeframe.

**Exact later resolution packet**

The question resolves NO. No U.S. federal court issued a preliminary injunction or TRO blocking the Department of Education's PSLF "substantial illegal purpose" rule (34 CFR 685.219, Fed. Reg. Doc. 2025-19729) between May 1 and June 1, 2026.

Key evidence:

1. The Student Loan Lawyer (TateEsq) PSLF tracking page, updated April 15, 2026, explicitly states: "No court has blocked the rule; unless one does before July 1, 2026, it takes effect on that date." It notes the three challenges were proceeding via summary judgment motions filed February 2026, not emergency injunctions [PSLF Changes in 2026 - Student Loan Lawyer](https://www.tateesq.com/learn/pslf-changes-2026).

2. The lead state-coalition case, Commonwealth of Massachusetts v. U.S. Department of Education (D. Mass., 1:25-cv-13244): the Oregon DOJ litigation tracker and the Civil Rights Litigation Clearinghouse docket (last updated June 2, 2026, 4:05 a.m.) show NO preliminary injunction or TRO entry in the May 1–June 1, 2026 window. The case was proceeding on cross-motions for summary judgment (plaintiffs' MSJ filed Feb. 13, 2026), with no injunctive-relief order in May 2026 [Public Service Loan Forgiveness Rule Challenge (Massachusetts v ...](https://www.doj.state.or.us/oregon-department-of-justice/federal-oversight/federal-litigation-tracker/public-service-loan-forgiveness-rule-challenge-massachusetts-v-u-s-department-of-education-d-mass-125-cv-13244/) [Commonwealth of Massachusetts v. U.S. Department of Education](https://clearinghouse.net/case/47296/).

3. The nonprofit case, Robert F. Kennedy Center for Justice and Human Rights v. McMahon / National Council of Nonprofits v. McMahon (D.D.C., 1:25-cv-03860): the Clearinghouse/CourtListener docket shows summary-judgment briefing completed by April 20, 2026, and a joint appendix filed May 4, 2026 — but NO injunction or TRO issued in the May 2026 window [Robert F. Kennedy Center for Justice and Human Rights v. McMahon](https://clearinghouse.net/case/47109/). The Protect Borrowers litigation page likewise showed no such order [Lawsuit: Cities, Unions, and Civil Society Organizations Sue Trump ...](https://protectborrowers.org/litigation/pslf-lawsuit/).

4. A preliminary injunction issued by the D. Mass. court on April 3, 2026 in a related ED case (No. 26-11229-FDS) concerned the unrelated IPEDS/ACTS survey requirement, NOT the PSLF "substantial illegal purpose" rule — and it predates the May 1 window in any event [[PDF] united states district court - New York State Attorney General](https://ag.ny.gov/sites/default/files/court-filings/massachusetts-et-al-v-united-states-department-of-education-et-al-preliminary-injunction-2026.pdf).

These cases were litigating on the merits (summary judgment) rather than seeking emergency injunctive relief, so the rule remained unblocked heading toward its July 1, 2026 effective date. No qualifying PI or TRO was entered in the required window, so the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-30. `f167e83b-1f1e-52de-b01d-2b05598fc474`

- Present date: `2026-05-29 06:31:31.648202`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the European Council meeting of June 18–19, 2026 extend into a third day or require an extraordinary/continuation session before July 1, 2026?

**Resolution criteria**

This question resolves **YES** if either of the following occurs between May 12, 2026, and July 1, 2026 (all times in Brussels time, CET/CEST, i.e., UTC+2):

1. **Third-day extension:** The European Council meeting scheduled for June 18–19, 2026, officially continues its formal proceedings into a third day, defined as any session starting at or after 00:00 CEST on June 20, 2026. This includes scenarios where the meeting is formally suspended and resumed on June 20 or later.

2. **Extraordinary or continuation session:** The European Council formally convenes an "extraordinary meeting" (as defined by Article 15(3) TEU: "When the situation so requires, the President shall convene a special meeting of the European Council") or a formally announced continuation session of heads of state or government, scheduled to occur on or after May 12, 2026, and no later than July 1, 2026 (23:59 CEST), to address substantially the same agenda items (particularly but not limited to MFF negotiations) as the June 18–19 summit.

A "continuation" or "extraordinary session" means a meeting formally convened by the President of the European Council under the European Council's Rules of Procedure (Council Decision 2009/882/EU, Article 2), distinct from routine Council of the EU formations or informal meetings of heads of state.

This question resolves **NO** if the meeting concludes on or before 23:59 CEST on June 19, 2026, and no extraordinary European Council meeting or continuation session is formally announced or held by 23:59 CEST on July 1, 2026.

**Resolution source:** Official press releases, conclusions, or meeting records published on the European Council meeting page at https://www.consilium.europa.eu/en/meetings/european-council/2026/06/18-19/ or the European Council press releases portal at https://www.consilium.europa.eu/en/press/press-releases/. Credible international news sources (e.g., Reuters, AP, Politico Europe) may be used as supplementary confirmation.

**Pre-cutoff background**

The European Council is scheduled to meet on June 18–19, 2026, in the Europa building in Brussels [European Council 18-19 June 2026 - consilium.europa.eu](https://www.consilium.europa.eu/en/meetings/european-council/2026/06/18-19/). The primary agenda item is expected to be the Multiannual Financial Framework (MFF) for 2028–2034. European Council President António Costa aims to reach a deal on the MFF by the end of 2026.

As of May 12, 2026, MFF negotiations remain deadlocked on multiple fronts [Six months of MFF negotiations – and there's still no shared vision ...](https://www.ceps.eu/six-months-of-mff-negotiations-and-theres-still-no-shared-vision-for-a-policy-driven-eu-budget/): net contributor states (e.g., Germany, the Netherlands, Sweden) are pushing for fiscal restraint, while major recipient states (e.g., Poland, Hungary, Romania, the Baltics) resist cuts to the Common Agricultural Policy and cohesion funds [European Council 18-19 June 2026: MFF 2028-2034 Negotiations ...](https://pressreview.eu/european-council-18-19-june-2026-mff-2028-2034-budget-negotiation-box/). The European Parliament has called for an MFF set at 1.27% of EU GNI (approximately €1,789 billion in constant 2025 prices), significantly above the Commission's proposal. There is no shared political vision among member states on how to align the budget with strategic priorities such as defense, the Green Deal, and support for Ukraine [Six months of MFF negotiations – and there's still no shared vision ...](https://www.ceps.eu/six-months-of-mff-negotiations-and-theres-still-no-shared-vision-for-a-policy-driven-eu-budget/). The Cypriot Council Presidency is currently preparing a "negotiation box" with concrete figures to frame the June discussions [European Council 18-19 June 2026: MFF 2028-2034 Negotiations ...](https://pressreview.eu/european-council-18-19-june-2026-mff-2028-2034-budget-negotiation-box/).

Historically, contentious MFF negotiations have caused summits to overrun. Most notably, the July 2020 European Council on the 2021–2027 MFF lasted five days (originally scheduled for two). However, most European Council meetings conclude on schedule, so extensions remain the exception rather than the norm. The probability of an extension or extraordinary session is estimated at roughly 10–25%.

**Exact later resolution packet**

The question resolves **NO**. Neither of the two YES conditions was met.

**Condition 1 — No third-day extension.** The official European Council meeting page states EU leaders "met in Brussels for a two-day summit" and that President Costa said "We have just concluded a European Council" on 19 June [European Council, 18-19 June 2026 - consilium.europa.eu](https://www.consilium.europa.eu/en/meetings/european-council/2026/06/18-19/). The official conclusions document (EUCO 8/26) is dated "Brussels, 19 June 2026" and titled "European Council meeting (18 and 19 June 2026) – Conclusions," with no mention of any suspension/resumption or session on 20 June or later [[PDF] European Council meeting (18 and 19 June 2026) – Conclusions](https://www.consilium.europa.eu/media/r1rowtfb/en-20260619-european-council-conclusions.pdf). Euronews live coverage confirms "The second day of the EU summit has come to an end in Brussels" on 19/06/2026 (link ended 19/06/2026 18:45 GMT+2). Thus no session started at or after 00:00 CEST on 20 June 2026.

**Condition 2 — No extraordinary/continuation session convened before July 1, 2026.** On the MFF, the conclusions did not schedule a continuation summit; instead they called on the (incoming Irish) Presidency to take the Negotiating Box forward toward the next (October) European Council, i.e., after the resolution window [[PDF] European Council meeting (18 and 19 June 2026) – Conclusions](https://www.consilium.europa.eu/media/r1rowtfb/en-20260619-european-council-conclusions.pdf). Wikipedia's List of European Council meetings shows only the single June 18–19 meeting (No. 259) in the May 12–July 1, 2026 window, with no extraordinary or special European Council listed [List of European Council meetings - Wikipedia](https://en.wikipedia.org/wiki/List_of_European_Council_meetings). The official Council "Forward look: 29 June – 12 July 2026" press release lists only ordinary Council of the EU formations (EPSCO on 29 June, ECOFIN on 10 July, a Eurogroup meeting) and no European Council, special European Council, or heads-of-state continuation session before July 1 [Forward look: 22 June – 5 July 2026 - consilium.europa.eu](https://www.consilium.europa.eu/en/press/press-releases/2026/06/19/forward-look-2026/). Therefore no extraordinary meeting under Art. 15(3) TEU / Rules of Procedure was announced or held by 23:59 CEST on 1 July 2026.

Because the meeting concluded on 19 June 2026 and no extraordinary/continuation session was announced or held by the 1 July 2026 deadline, the question resolves **NO (0)**.

Resolution source URLs used: official meeting page https://www.consilium.europa.eu/en/meetings/european-council/2026/06/18-19/ ; conclusions PDF https://www.consilium.europa.eu/media/r1rowtfb/en-20260619-european-council-conclusions.pdf ; press release https://www.consilium.europa.eu/en/press/press-releases/2026/06/19/european-council-conclusions-18-and-19-june-2026/ ; Forward look https://www.consilium.europa.eu/en/press/press-releases/2026/06/26/forward-look-2026/

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-31. `d7a1ae25-6951-51ae-b118-189a4c81c15f`

- Present date: `2026-04-29 23:32:20.191966`
- Source cutoff boundary: `2026-04-30` (encodes end of UTC day `2026-04-29`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Senator Blackburn formally introduce the 'TRUMP AMERICA AI Act' (or a substantially similar bill) by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after the question's open date and on or before June 1, 2026 (11:59 PM ET), Senator Marsha Blackburn formally introduces the "TRUMP AMERICA AI Act" or a substantially similar bill in the United States Senate.

**"Formally introduce"** is defined as the bill being assigned an official bill number (e.g., S.####) by the Secretary of the Senate and appearing on Congress.gov. A discussion draft, white paper, or framework document without a bill number does not qualify.

**"Substantially similar bill"** is defined as legislation that (1) is sponsored or co-sponsored by Senator Blackburn, (2) uses the "TRUMP AMERICA" branding in its title or short title, and (3) includes federal preemption of state-level AI regulations as a core provision.

If no such bill appears on Congress.gov by June 1, 2026, this question resolves **No**.

**Resolution source:** Senator Blackburn's sponsored legislation page on Congress.gov: https://www.congress.gov/member/marsha-blackburn/B001243?q=%7B%22sponsorship%22%3A%22sponsored%22%7D

**Pre-cutoff background**

On March 18, 2026, Senator Marsha Blackburn (R-TN) released a 291-page discussion draft titled the "TRUMP AMERICA AI Act" (formally: The Republic Unifying Meritocratic Principles for AI in the Modern Era and Responsible Innovation for a Connected America Act) [https://www.forbes.com/sites/paulocarvao/2026/04/02/national-policy-framework-turns-ai-preemption-into-a-2026-political-test/](https://www.forbes.com/sites/paulocarvao/2026/04/02/national-policy-framework-turns-ai-preemption-into-a-2026-political-test/). The draft proposes a comprehensive federal AI regulatory framework, including a duty of care for AI developers, preemption of state-level AI regulations, potential sunsetting of Section 230, and protections for children, creators, and communities [https://www.politico.com/news/2026/04/03/trumps-partisan-ai-pitch-stalls-on-the-hill-00858101](https://www.politico.com/news/2026/04/03/trumps-partisan-ai-pitch-stalls-on-the-hill-00858101).

On March 20, 2026, the White House released a separate "National Policy Framework for Artificial Intelligence" outlining seven priorities for AI governance [https://www.forbes.com/sites/paulocarvao/2026/04/02/national-policy-framework-turns-ai-preemption-into-a-2026-political-test/](https://www.forbes.com/sites/paulocarvao/2026/04/02/national-policy-framework-turns-ai-preemption-into-a-2026-political-test/). Blackburn's draft attempts to translate these themes into enforceable legislative obligations.

As of April 27, 2026, the TRUMP AMERICA AI Act remains a discussion draft and has not been formally introduced as a bill with an assigned bill number [America Needs One Rulebook for Artificial Intelligence. The TRUMP ...](https://www.blackburn.senate.gov/2026/4/ai/america-needs-one-rulebook-for-artificial-intelligence-the-trump-america-ai-act-would-create-it). Senator Blackburn continues to promote the draft, publishing an op-ed on April 27, 2026 advocating for the legislation and announcing growing coalition support [America Needs One Rulebook for Artificial Intelligence. The TRUMP ...](https://www.blackburn.senate.gov/2026/4/ai/america-needs-one-rulebook-for-artificial-intelligence-the-trump-america-ai-act-would-create-it). However, the proposal has faced a "frosty reception" on Capitol Hill, with key Democrats dismissing it as a "partisan play" lacking consumer protections, and Republican leadership being criticized for failing to engage in bipartisan outreach [https://www.politico.com/news/2026/04/03/trumps-partisan-ai-pitch-stalls-on-the-hill-00858101](https://www.politico.com/news/2026/04/03/trumps-partisan-ai-pitch-stalls-on-the-hill-00858101). Lawmakers have warned that Congress is "running out of legislative runway" to pass such a bill this year [https://www.politico.com/news/2026/04/03/trumps-partisan-ai-pitch-stalls-on-the-hill-00858101](https://www.politico.com/news/2026/04/03/trumps-partisan-ai-pitch-stalls-on-the-hill-00858101).

**Exact later resolution packet**

The question resolves NO. It asks whether Senator Marsha Blackburn formally introduced the "TRUMP AMERICA AI Act" (or a substantially similar bill) — defined as a bill assigned an official Senate bill number (S.####) and appearing on Congress.gov — on or after the open date (April 29, 2026) and on or before June 1, 2026 (11:59 PM ET).

I queried the exact resolution source specified in the question, Senator Blackburn's sponsored legislation page on Congress.gov (https://www.congress.gov/member/marsha-blackburn/B001243?q=%7B%22sponsorship%22%3A%22sponsored%22%7D), as of June 2, 2026. No bill titled "TRUMP AMERICA AI Act" or containing "TRUMP AMERICA" in its title appears among her sponsored legislation. The most recently sponsored bills as of that date were S.4408 (Supporting Energy and Economic Development (SEED) Act) and S.4405 (287(g) Expansion Act), both introduced April 28, 2026 — i.e., before the question's open date — and S.4329 (Title X Abortion Provider Prohibition Act, April 16, 2026). None match the criteria [a1695d].

Supporting context from public reporting confirms the "TRUMP AMERICA AI Act" remained a discussion draft. It was released as a ~291/300-page discussion draft on March 18, 2026, and as of late April 2026 had not been formally introduced with an assigned bill number, facing a "frosty reception" on Capitol Hill. No source indicates a formal Senate introduction with an S.#### number occurred between April 29 and June 1, 2026.

Because no qualifying bill (neither the exactly-named Act nor a "substantially similar" bill meeting all three criteria — Blackburn sponsorship, "TRUMP AMERICA" branding, and federal preemption of state AI regulation) appears on Congress.gov within the resolution window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-32. `69db632e-fd4d-571b-9447-9c6841c4c537`

- Present date: `2026-05-14 12:06:25.396803`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Pope Leo XIV announce a consistory for the creation of new cardinals between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026, and on or before July 1, 2026 (23:59 UTC), Pope Leo XIV announces a consistory specifically for the creation (appointment) of new cardinals, whether cardinal-electors or non-electors.

An "announcement" is defined as either:
1. A verbal announcement by the Pope during a public address (e.g., the Sunday Angelus or a General Audience), OR
2. An official publication in the Bollettino of the Holy See Press Office.

The primary resolution source is the Holy See Press Office at [https://press.vatican.va/content/salastampa/en/bollettino.html](https://press.vatican.va/content/salastampa/en/bollettino.html). Credible Catholic news sources (e.g., The Pillar, Catholic News Agency, Vatican News) may be used as corroborating sources.

The announcement must be for a consistory specifically for the "creation" or "appointment" of new cardinals. Announcements of consistories convened for other purposes (e.g., canonizations, consultations) do not count.

If no such announcement is published or made by 23:59 UTC on July 1, 2026, the question resolves as **No**.

**Pre-cutoff background**

Pope Leo XIV was elected in 2025. As of May 12, 2026, the number of cardinal electors stands at 121, just one above the traditional limit of 120 established by Pope St. John Paul II [https://www.pillarcatholic.com/p/leos-first-cardinals-if-when-and](https://www.pillarcatholic.com/p/leos-first-cardinals-if-when-and). Since Leo XIV's election, 14 cardinals have turned 80 and aged out of voting eligibility [https://www.pillarcatholic.com/p/leos-first-cardinals-if-when-and](https://www.pillarcatholic.com/p/leos-first-cardinals-if-when-and). Several more cardinals are expected to reach the retirement age of 80 later in 2026, which would further reduce the number of electors below the traditional cap.

A consistory is the formal assembly of the College of Cardinals, convened by the Pope to create new cardinals. The timing of such an announcement is at the sole discretion of the Pope. Traditionally, the Pope announces an upcoming consistory during a public address (such as the Sunday Angelus) and the Holy See Press Office subsequently publishes the details. As of May 12, 2026, no consistory for the creation of new cardinals has been announced in the official Vatican Press Office bulletins [https://press.vatican.va/content/salastampa/en/bollettino/pubblico/2026/05.html](https://press.vatican.va/content/salastampa/en/bollettino/pubblico/2026/05.html).

Pope Leo XIV has a scheduled trip to Spain from June 6–12, 2026, which could affect the timing of any such announcement. The Pillar has analyzed the question of Leo's first cardinals extensively, noting significant uncertainty about whether and when he might act [https://www.pillarcatholic.com/p/leos-first-cardinals-if-when-and](https://www.pillarcatholic.com/p/leos-first-cardinals-if-when-and).

**Exact later resolution packet**

The question resolves NO because no announcement of a consistory specifically for the CREATION (appointment) of new cardinals was made by Pope Leo XIV between May 12 and July 1, 2026.

Key facts and evidence:

1. The only consistory activity by Pope Leo XIV in the relevant window was an Extraordinary Consistory held June 26-27, 2026. However, this was explicitly a CONSULTATION/discussion gathering, not a consistory to create cardinals. Vatican News describes it as "an Extraordinary Consistory focused on the current situation of the Church and the world, the pursuit of peace, and the implementation of the Synod," following a "synodal" method of prayer, reflection, and discussion — with no creation or appointment of new cardinals [efe589]. The resolution criteria explicitly state: "Announcements of consistories convened for other purposes (e.g., canonizations, consultations) do not count." Thus this consistory does not qualify.

2. Even the announcement of the June 26-27 consistory fell OUTSIDE the resolution window. It was announced on April 14, 2026 (via a letter to the College of Cardinals dated April 12, 2026), well before the May 12, 2026 start of the window, and was for "collegial exchange" and "discussions," not the creation of cardinals [8445a5]. Leo had first mentioned this June gathering back in January 2026.

3. Multiple credible Catholic outlets confirmed that Pope Leo XIV did NOT create new cardinals during this period. The National Catholic Register / EWTN Vatican analysis (published ~June 1, 2026) states plainly that "Pope Leo XIV's second consistory... did not include the creation of new cardinals, it has now been confirmed," and notes that only "unconfirmed Vatican rumors" of a possible "mini-consistory to create cardinals" existed, which remained unconfirmed [f39424].

Because (a) the June 26-27 consistory was for consultation (an explicitly excluded purpose), (b) its announcement predated the window anyway, and (c) no announcement of any consistory for the creation/appointment of new cardinals was published in the Holy See Press Office Bollettino or delivered verbally by Pope Leo XIV between May 12 and July 1, 2026, the question resolves NO.

Sources: Vatican News, https://www.vaticannews.va/en/vatican-city/news/2026-06/schedule-pope-leo-xiv-consistory-cardinals-june.html [efe589]; National Catholic Register, https://www.ncregister.com/news/the-second-consistory-of-leo-xiv-analysis [f39424]; National Catholic Register / CNA, https://www.ncregister.com/cna/pope-leo-xiv-calls-june-consistory-of-cardinals-says-evangelii-gaudium-must-be-relaunched [8445a5]. This is not a conditional question, so no annulment applies.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-33. `b22bf1df-08f3-53f0-b37e-45125d5019fc`

- Present date: `2026-05-16 21:54:54.318907`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Supreme Court issue an order or ruling related to the Court of International Trade's May 2026 decision striking down Section 122 tariffs by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 12, 2026 and July 1, 2026 (11:59 PM UTC), the Supreme Court of the United States issues any of the following regarding the legality of tariffs imposed under Section 122 of the Trade Act of 1974 (19 U.S.C. § 1862 note), as challenged in the U.S. Court of International Trade's May 7, 2026 decision or any related appeal:

1. A signed opinion on the merits (majority, plurality, or per curiam opinion);
2. A grant or denial of a petition for writ of certiorari;
3. A grant or denial of an application for a stay of a lower court order; or
4. Any other substantive order (not merely an administrative scheduling order) addressing the Section 122 tariff litigation.

The question resolves **No** if no such ruling or order is issued by July 1, 2026 at 11:59 PM UTC.

**Resolution source:** The official Supreme Court of the United States "Opinions of the Court" page (https://www.supremecourt.gov/opinions/slipopinion/25) and the Court's orders list (https://www.supremecourt.gov/orders/ordersofthecourt/25), supplemented by credible reporting from SCOTUSblog (https://www.scotusblog.com/), Reuters, or the Associated Press.

**Pre-cutoff background**

On February 20, 2026, the U.S. Supreme Court ruled 6-3 in *Learning Resources, Inc. v. Trump* (No. 24-1287) that the International Emergency Economic Powers Act (IEEPA) does not authorize the President to impose tariffs, striking down President Trump's sweeping IEEPA-based tariffs [US trade court rules Trump tariffs illegal, but issues narrow block](https://www.reuters.com/world/us-trade-court-rules-against-trumps-10-global-tariff-2026-05-07/). Following that ruling, the Trump administration pivoted to other statutory authorities, including Section 122 of the Trade Act of 1974, to impose a temporary 10% global tariff.

On May 7, 2026, the U.S. Court of International Trade (CIT) ruled 2-1 that these Section 122 tariffs were unjustified, issuing a narrow injunction blocking the levies for two private importers (Basic Fun! and Burlap & Barrel) and the State of Washington, while declining to issue a universal injunction [US trade court rules Trump tariffs illegal, but issues narrow block](https://www.reuters.com/world/us-trade-court-rules-against-trumps-10-global-tariff-2026-05-07/). The administration is expected to appeal this decision to the U.S. Court of Appeals for the Federal Circuit, and could potentially seek emergency relief from the Supreme Court (e.g., a stay of the injunction or expedited certiorari).

As of May 13, 2026, no petition or application related to the CIT's Section 122 tariff ruling has been filed at the Supreme Court. The normal appellate path would go through the Federal Circuit before reaching SCOTUS, but the administration could seek emergency relief directly. The Supreme Court's current term is scheduled to end in late June or early July 2026. Section 301 tariff investigations are also underway but are not expected to produce SCOTUS litigation within this timeframe.

**Exact later resolution packet**

The question resolves NO. It asks whether, between May 12, 2026 and July 1, 2026 (11:59 PM UTC), the U.S. Supreme Court issued any substantive order/ruling (merits opinion, cert grant/denial, stay grant/denial, or other substantive order) regarding the legality of the Section 122 (Trade Act of 1974) tariffs challenged in the Court of International Trade's (CIT) May 7, 2026 decision or any related appeal. The evidence establishes that no such Supreme Court action occurred; the litigation stayed entirely within the Federal Circuit during the window.

Timeline of the Section 122 litigation (distinct from the earlier IEEPA case, Learning Resources v. Trump, decided Feb. 20, 2026):
- May 7, 2026: The CIT ruled 2-1 that the Section 122 tariffs were unlawful, granting narrow relief to plaintiffs (Basic Fun!, Burlap & Barrel, and the State of Washington/Oregon) but declining a universal injunction (CIT Slip Op. 26-47).
- May 8, 2026: The government appealed to the U.S. Court of Appeals for the Federal Circuit (CAFC).
- May 12, 2026: The Federal Circuit entered a temporary administrative stay of the CIT's order.
- June 11, 2026: The Federal Circuit granted the government's motion for a stay pending appeal, finding the administration "likely to succeed," allowing continued tariff collection. This was widely reported (Reuters, Bloomberg, The Hill, Boston Herald) as an APPEALS COURT (Federal Circuit) action, NOT a Supreme Court action [US appeals court extends block on ruling against Trump's ... - Reuters](https://www.reuters.com/world/us-appeals-court-extends-block-ruling-against-trumps-10-global-tariff-2026-06-11/).

Confirmation that no Supreme Court order was issued in the window:
- The Reuters June 11, 2026 report confirms the June ruling was by the U.S. Court of Appeals for the Federal Circuit, not the Supreme Court, and that the appeal was proceeding through the Federal Circuit [US appeals court extends block on ruling against Trump's ... - Reuters](https://www.reuters.com/world/us-appeals-court-extends-block-ruling-against-trumps-10-global-tariff-2026-06-11/).
- The Skadden legal analysis (dated May 20, 2026) confirms the case was pending at the Federal Circuit with no petition, application, or order at the Supreme Court regarding this Section 122 litigation [US Trade Court Strikes Down Section 122 Tariffs, but Ruling's Fate ...](https://www.skadden.com/insights/publications/2026/05/us-trade-court-strikes-down-section-122-tariffs).
- A query of the SCOTUSblog homepage as of the end of the term (through July 1, 2026) found coverage of the Court's late-June 2026 decisions (birthright citizenship, transgender athletes, campaign finance, removal power) but NO mention of any Supreme Court order, opinion, stay, or certiorari decision concerning the CIT's Section 122 tariff ruling [https://www.scotusblog.com/](https://www.scotusblog.com/).

Additional context supporting the low likelihood of SCOTUS intervention: multiple analyses noted the Section 122 surcharge was set to expire on July 24, 2026, "which could reduce the urgency for expedited review at the high court level," and the Federal Circuit's June 11 stay resolved the immediate emergency in the government's favor, removing any incentive for the government to seek emergency SCOTUS relief.

Because the resolution window closed on July 1, 2026, and the case never reached the Supreme Court during that window (it remained before the Federal Circuit), none of the four YES conditions (merits opinion; cert grant/denial; stay grant/denial; or other substantive order on the Section 122 litigation) were met. The question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-34. `62be25b5-7b18-56dc-a644-b5402a0d6aca`

- Present date: `2026-05-02 20:33:11.167774`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will James Gunn publicly confirm a second specific villain (beyond Brainiac) for Man of Tomorrow between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves YES if, between May 1, 2026 at 00:00 UTC and June 1, 2026 at 23:59 UTC, James Gunn publicly confirms a specific villain character from DC Comics—beyond Brainiac, who was already confirmed in December 2025—for the film Man of Tomorrow (2027).

A "specific villain" is defined as a named character from DC Comics (e.g., Maxima, Metallo, Parasite, Mongul, Lobo, Bizarro, etc.) who is identified as appearing in the film in an antagonistic or villainous role. Lex Luthor does not count, as he has been confirmed as an ally/co-protagonist rather than a villain in this film.

"Publicly confirm" means one of the following:
1. A direct post or statement by James Gunn on his verified social media accounts (Threads: https://www.threads.net/@jamesgunn, Instagram: https://www.instagram.com/jamesgunn/, or any other verified account he uses), explicitly naming the character; OR
2. An official announcement or confirmed report published in major entertainment trade publications (Variety: https://variety.com/, The Hollywood Reporter: https://www.hollywoodreporter.com/, Deadline: https://deadline.com/, or TheWrap: https://www.thewrap.com/) that attributes the confirmation to Gunn, DC Studios, or Warner Bros.

Unverified rumors, fan speculation, set photo leaks without official confirmation, or reports that Gunn has not acknowledged or that lack studio attribution do NOT count.

The question resolves NO if no such confirmation occurs within the specified window.

**Pre-cutoff background**

Man of Tomorrow is the sequel to James Gunn's 2025 Superman film, scheduled for theatrical release on July 9, 2027. Principal photography began around April 20, 2026, in Atlanta.

As of early 2026, one villain has already been officially confirmed: Brainiac, played by German actor Lars Eidinger, announced by Gunn in December 2025. The film's plot involves Superman teaming up with Lex Luthor (Nicholas Hoult) against a new threat. Beyond Brainiac, there has been fan speculation about additional villains appearing in the film, including characters like Maxima (who was reportedly screen-tested by multiple actresses as of April 2026) and others.

As of April 8, 2026, Gunn confirmed there was still at least one character left to cast, while debunking other casting rumors. Gunn is known for being unusually communicative on social media (particularly Threads and Instagram) about DCU plans, though he is also strategic about avoiding spoilers. With filming actively underway, set photos and leaks may prompt additional confirmations.

James Gunn's verified social media profiles:
- Threads: https://www.threads.net/@jamesgunn
- Instagram: https://www.instagram.com/jamesgunn/

**Exact later resolution packet**

The question resolves NO. It requires that, between May 1 and June 1, 2026, James Gunn publicly confirm a specific named DC villain (beyond Brainiac) for Man of Tomorrow in an antagonistic role — either via his verified social media (Threads/Instagram) explicitly naming the character, OR via Variety/THR/Deadline/TheWrap with the confirmation attributed to Gunn, DC Studios, or Warner Bros.

Key findings:

1. The only villain-related casting (Maxima) was reported by trade publications in APRIL 2026 (outside the window): Variety published "Adria Arjona to Play Maxima" on April 14, 2026 [ec768a], and Deadline/THR ran similar reports. Critically, these were NOT attributed to Gunn, DC Studios, or Warner Bros — Variety explicitly stated "DC Studios declined to comment on the casting" [ec768a]. THR likewise could not confirm Arjona was Maxima. So even within April, the Maxima reports fail the attribution requirement.

2. Far from confirming Maxima, James Gunn actively DEBUNKED the Maxima casting reports, calling them "bullshit" and "shoddy & incorrect" on Threads (EW: "Man of Tomorrow Maxima casting report is 'bulls---,' James Gunn says"; https://ew.com/man-of-tomorrow-maxima-casting-report-debunked-james-gunn-11945616). This is the opposite of a confirmation.

3. The casting announcements that actually fell within the May 1–June 1, 2026 window were all for non-villain or undisclosed roles: Matthew Lillard joined the cast on May 6, 2026 in an undisclosed role; Sinqua Walls joined ~May 11, 2026 in an undisclosed role; and Milly Alcock was confirmed as Supergirl on May 20, 2026 [46c52e, 329f63]. None of these involved Gunn (or the qualifying trades attributing to Gunn/DC Studios/WB) confirming a specific named DC villain in an antagonistic role.

4. A review of the Wikipedia article on the film and the Yahoo/trade coverage found no qualifying villain confirmation within the May 1–June 1 window [46c52e, 329f63, 13afa2].

Since no second specific villain (beyond Brainiac) was confirmed by Gunn or attributed to Gunn/DC Studios/WB in a qualifying source within the resolution window, the question resolves NO.

Evidence URLs:
- https://variety.com/2026/film/news/adria-arjona-maxima-superman-sequel-man-of-tomorrow-1236721502/ (April 14, 2026; DC Studios declined to comment) [ec768a]
- https://ew.com/man-of-tomorrow-maxima-casting-report-debunked-james-gunn-11945616 (Gunn debunks Maxima report)
- https://en.wikipedia.org/wiki/Man_of_Tomorrow_(film) (May 2026 casting = Lillard, Walls undisclosed; Alcock as Supergirl) [46c52e, 329f63]
- https://www.hollywoodreporter.com/movies/movie-news/man-of-tomorrow-enlists-sinqua-walls-1236588558/ (undisclosed role)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-35. `8e0b857a-9cb2-55d0-87df-06b7105267c8`

- Present date: `2026-05-02 10:27:11.571211`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the IAEA report a new confirmed kinetic strike on any Iranian nuclear facility between May 1, 2026, and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the International Atomic Energy Agency (IAEA) publishes an official statement, press release, or report — dated on or after May 1, 2026 (00:00 UTC) and no later than June 1, 2026 (23:59 UTC) — confirming that a new kinetic strike has occurred at any Iranian nuclear facility during this same period.

**Definition of "kinetic strike":** A deliberate military attack involving physical projectiles, missiles, bombs, drones, or other explosive ordnance that physically impacts the facility or its immediate premises. This excludes cyberattacks (as defined by NIST: https://csrc.nist.gov/glossary/term/cyber_attack), acts of sabotage not involving explosive ordnance, and accidental damage. The strike must be attributed to a military operation by a state or non-state actor, as characterized by the IAEA or credible reporting.

**Definition of "Iranian nuclear facility":** Any facility on the IAEA's list of declared nuclear installations in Iran, including but not limited to:
- Natanz Fuel Enrichment Plant
- Fordow Fuel Enrichment Plant
- Esfahan (Isfahan) Nuclear Technology Center
- Bushehr Nuclear Power Plant
- Khondab (Arak) Heavy Water Reactor / Heavy Water Production Plant
- Shahid Rezayee Nejad (Ardakan) Yellow Cake Production Facility

A reference list of Iranian nuclear facilities under IAEA safeguards is maintained at: https://www.iaea.org/newscenter/focus/iran/iaea-and-iran-iaea-board-reports

**Resolution source:** Official IAEA communications published at https://www.iaea.org/newscenter/statements or via IAEA Board of Governors reports. Only IAEA reports or statements **published on or after May 1, 2026 (00:00 UTC)** confirming a strike that **occurred on or after May 1, 2026 (00:00 UTC)** qualify for Yes resolution, to exclude previously reported incidents.

If no such IAEA confirmation is published by June 1, 2026 (23:59 UTC), the question resolves **No**.

**Pre-cutoff background**

As of May 1, 2026, Iranian nuclear facilities have been subject to multiple kinetic strikes. In June 2025, the U.S. conducted "Operation Midnight Hammer," striking the Natanz fuel enrichment plant, the Esfahan (Isfahan) nuclear site, and the Fordow fuel enrichment plant [IAEA provides updates on Iran nuclear facilities](https://www.ans.org/news/article-7911/iaea-provides-updates-on-iran-nuclear-facilities/). Subsequently, in March–April 2026, further strikes have occurred: the Bushehr Nuclear Power Plant was struck or impacted by projectiles on at least four occasions (including a March 18 strike destroying a structure 350 meters from the reactor, and an April 4 projectile strike killing a worker); the Khondab heavy water production plant sustained severe damage on March 27; and the Shahid Rezayee Nejad (Ardakan) Yellow Cake Production Facility was attacked on March 27 [IAEA provides updates on Iran nuclear facilities](https://www.ans.org/news/article-7911/iaea-provides-updates-on-iran-nuclear-facilities/).

The IAEA, under Director General Rafael Grossi, has been the authoritative source for confirming these incidents, issuing statements and reports to its Board of Governors. Grossi has warned that strikes near nuclear facilities risk crossing "the reddest line" and could cause severe radiological accidents. The ongoing U.S./Israel–Iran military conflict and the stated objective of preventing Iran from acquiring nuclear weapons make further strikes plausible but not certain, particularly if diplomatic efforts progress.

The IAEA's official statements and press releases are published at: https://www.iaea.org/newscenter/statements. Board reports on Iran are available at: https://www.iaea.org/newscenter/focus/iran/iaea-and-iran-iaea-board-reports.

**Exact later resolution packet**

Adjudicated: All IAEA-confirmed kinetic strikes on Iranian nuclear facilities (the four Bushehr projectile incidents, plus Khondab and Ardakan) occurred in March-April 2026, before the May 1 window; the last IAEA confirmation was the April 4 Bushehr projectile. The documented May 2026 strikes (May 7 and May 25-26) targeted military/naval sites at Bandar Abbas and Qeshm Island, not nuclear facilities, and the May 17 nuclear-plant drone strike hit the Barakah plant in the UAE, not an Iranian facility. The Al Mayadeen 'May 29' Bushehr article that an earlier automated pass relied on could not be independently verified and did not surface in any targeted search; no qualifying IAEA statement/report published in the window confirming an in-window strike on an Iranian facility exists, so the question resolves No.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-36. `25a5ce74-d39c-5da1-bcee-003609679986`

- Present date: `2026-05-02 17:14:59.079132`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. Supreme Court grant a stay of the Fifth Circuit's mandate in Nathan v. Alamo Heights ISD between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the U.S. Supreme Court issues an order granting a stay of the Fifth Circuit's mandate in *Nathan v. Alamo Heights ISD* (No. 25-50695) on or after May 1, 2026 (00:00 UTC) and by June 1, 2026 (23:59 UTC).

This question resolves as **No** if no such stay order is issued by the Supreme Court by June 1, 2026 at 23:59 UTC.

**Key definitions:**
- A **stay** is a court order that temporarily suspends the effect or enforcement of another court's decision pending further proceedings. See [Cornell Law Institute: Stay](https://www.law.cornell.edu/wex/stay).
- A **mandate** is the formal order issued by an appellate court directing the lower court to carry out its judgment. See [Cornell Law Institute: Mandate](https://www.law.cornell.edu/wex/mandate).

**Resolution source:** The official Orders of the Court published by the Supreme Court of the United States at [https://www.supremecourt.gov/orders/ordersofthecourt/25](https://www.supremecourt.gov/orders/ordersofthecourt/25), or the electronic docket for the case at [https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/](https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/). An administrative stay or full stay both count as "Yes."

**Pre-cutoff background**

On April 22, 2026, the U.S. Court of Appeals for the Fifth Circuit, sitting en banc, issued a 9-8 ruling in *Rabbi Nathan v. Alamo Heights Independent School District* (No. 25-50695) upholding Texas Senate Bill 10, which mandates the display of the Ten Commandments in every public-school classroom in the state [Multifaith Texas Families Condemn Fifth Circuit Decision ...](https://www.aclu.org/press-releases/fifth-circuit-upholds-law-requiring-display-of-ten-commandments-in-public-school-classrooms) [Texas Ten Commandments school law upheld, setting stage for ...](https://katv.com/news/nation-world/texas-ten-commandments-schools-ruling-5th-circuit-texas-sb10-classrooms-religion-law-ten-commandments-display-public-schools-supreme-court-challenge-church-state-texas-education-lawsuit-rabbi-nathan-v-alamo-heights-isd-ruling). The narrow split reflected deep disagreement on the constitutional questions involved under the Establishment Clause.

The plaintiffs—a multifaith group of 15 Texas families represented by the ACLU, ACLU of Texas, Americans United for Separation of Church and State, and the Freedom From Religion Foundation—have announced their intent to appeal to the U.S. Supreme Court and to seek emergency relief to prevent the law from taking effect [Multifaith Texas Families Condemn Fifth Circuit Decision ...](https://www.aclu.org/press-releases/fifth-circuit-upholds-law-requiring-display-of-ten-commandments-in-public-school-classrooms) [Texas Ten Commandments school law upheld, setting stage for ...](https://katv.com/news/nation-world/texas-ten-commandments-schools-ruling-5th-circuit-texas-sb10-classrooms-religion-law-ten-commandments-display-public-schools-supreme-court-challenge-church-state-texas-education-lawsuit-rabbi-nathan-v-alamo-heights-isd-ruling).

As of May 1, 2026, the Fifth Circuit's mandate—the formal order directing the lower court to implement the appellate decision (see [Cornell Law Institute definition](https://www.law.cornell.edu/wex/mandate))—is expected to issue or has issued, which would dissolve the district court's preliminary injunction that had blocked the law. The plaintiffs' primary avenue for relief is to request a **stay** from the Supreme Court—a court order temporarily suspending the effect of a lower court's judgment pending further proceedings (see [Cornell Law Institute definition](https://www.law.cornell.edu/wex/stay)). Granting such a stay requires the Court to evaluate likelihood of success on the merits, irreparable harm, and the public interest.

Key factors bearing on uncertainty: the 9-8 split suggests genuine legal contestation favoring a stay; however, the current Supreme Court's conservative 6-3 majority may be less inclined to block a religious-display law. The timeline is also uncertain—plaintiffs must file their application, and the Court must act, all within a compressed window.

**Exact later resolution packet**

The question resolves NO (0): No U.S. Supreme Court order granting a stay (administrative or full) of the Fifth Circuit's mandate in Nathan v. Alamo Heights ISD (No. 25-50695) was issued between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC).

Evidence and reasoning:
- The resolution source designated by the question is the official Supreme Court "Orders of the Court" page for the 2025 Term: https://www.supremecourt.gov/orders/ordersofthecourt/25. I queried this page exhaustively. It lists all Order Lists and Miscellaneous Orders issued during the relevant window. The orders within the May 1 – June 1, 2026 window are dated 05/04/26 (Order List + Miscellaneous Orders), 05/06/26, 05/11/26, 05/15/26, 05/18/26 (Order List), 05/19/26, 05/21/26, 05/22/26, and 05/26/26 (Order List). None of these reference Nathan v. Alamo Heights ISD, Texas SB 10, the Ten Commandments, or any related stay application [096dbb][21c4d9].
- Context confirming the underlying facts: The Fifth Circuit issued its 9-8 en banc ruling upholding Texas SB 10 on April 21/22, 2026, and the plaintiffs (ACLU et al.) announced an intent to appeal and seek emergency relief at the Supreme Court. However, I found no record of a Supreme Court order granting a stay. The Civil Rights Litigation Clearinghouse case page (last updated June 1, 2026) lists no Supreme Court stay activity [523b3d], and the CourtListener district-court docket likewise shows no such Supreme Court order [9be726]. A May 21, 2026 academic essay analyzing the Fifth Circuit decision also reported no Supreme Court stay action [208368].
- Because the designated official resolution source (supremecourt.gov Orders of the Court) contains no order granting a stay within the specified window, and no other authoritative source indicates such a stay was granted, the question resolves NO.

Note on the conditional framing: This question is not a conditional ("IF A THEN B") question; it is a straightforward binary on whether the Supreme Court granted a stay in the window. The criteria explicitly state it resolves NO if no such stay order is issued by June 1, 2026, 23:59 UTC.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-37. `4f56285c-bcca-5b33-887e-72bd1f742431`

- Present date: `2026-05-16 01:50:17.991261`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will the Janata Dal (Secular) win a seat in the 2026 Karnataka Rajya Sabha biennial elections?

**Resolution criteria**

This question refers specifically to the Rajya Sabha biennial elections for the four seats from Karnataka vacating in June 2026 [2026 Rajya Sabha elections - Wikipedia](https://en.wikipedia.org/wiki/2026_Rajya_Sabha_elections).

This question resolves **Yes** if at least one candidate officially nominated by the Janata Dal (Secular) (JD(S)) — as listed on the official candidate/results records of the Election Commission of India (ECI) — is declared elected to the Rajya Sabha from Karnataka in this biennial election cycle. A "win" for JD(S) means the winning candidate must be formally nominated by JD(S) and listed as a JD(S) candidate by the ECI; an independent candidate or a candidate of another party who is merely "supported" by JD(S) does not count.

This question resolves **No** if no candidate listed as a JD(S) nominee by the ECI wins a seat.

**Primary resolution source:** The Election Commission of India results portal at https://results.eci.gov.in/ or the ECI main site at https://www.eci.gov.in/. If ECI results are delayed, consistent reporting from at least two major credible news outlets (e.g., The Hindu, Times of India, NDTV, Reuters) confirming the official result may be used.

All dates and deadlines are in Indian Standard Time (IST, UTC+5:30).

**Pre-cutoff background**

The Rajya Sabha is the upper house of India's Parliament. Members are elected by state legislative assembly members using proportional representation with the single transferable vote system. Four Rajya Sabha seats from Karnataka are scheduled for biennial elections in 2026, with the current terms of incumbents ending on June 25, 2026 (IST). The retiring members include Iranna B. Kadadi (BJP), K. Narayan (BJP), Mallikarjun Kharge (INC), and H.D. Deve Gowda (JD(S)) [2026 Rajya Sabha elections - Wikipedia](https://en.wikipedia.org/wiki/2026_Rajya_Sabha_elections).

**Current Karnataka Legislative Assembly strength** (which determines Rajya Sabha voting): The Indian National Congress (INC) holds 136 seats, the Bharatiya Janata Party (BJP) holds 63 seats, and the Janata Dal (Secular) (JD(S)) holds 18 seats, out of 224 total elected seats [Karnataka Legislative Assembly - Wikipedia](https://en.wikipedia.org/wiki/Karnataka_Legislative_Assembly).

**Rajya Sabha quota calculation:** For 4 seats with 224 MLAs, the effective quota per seat is approximately 45 votes (224 ÷ 5 + 1). Congress with 136 MLAs can comfortably win 3 seats. The combined BJP-JD(S) strength is 81 MLAs, sufficient for 1 seat but not 2. JD(S) alone, with only 18 MLAs, cannot win a seat independently.

**NDA alliance context:** JD(S) formally joined the BJP-led National Democratic Alliance (NDA) ahead of the 2024 Lok Sabha elections. H.D. Deve Gowda's grandson Prajwal Revanna contested as an NDA candidate. The alliance's success in Karnataka during the 2024 general elections strengthened BJP-JD(S) ties. However, with only one effective Rajya Sabha seat available to the NDA bloc, whether BJP allocates it to a JD(S) candidate or fields its own nominee is the central uncertainty. BJP already holds 2 of the 4 retiring seats and may prioritize retaining them.

**Exact later resolution packet**

The question resolves NO.

The 2026 Karnataka Rajya Sabha biennial election filled the four seats vacated in June 2026 (retiring: Iranna B. Kadadi (BJP), K. Narayan (BJP), Mallikarjun Kharge (INC), H.D. Deve Gowda (JD(S))). All four seats were won unopposed (declared unanimously/unopposed as there were only four nominees for four seats), and the four winners were:

- Mallikarjun Kharge (INC)
- Pawan Khera (INC)
- Mansoor Ali Khan (INC)
- M. Nagaraj / Nagaraja (BJP)

No candidate nominated by the Janata Dal (Secular) (JD(S)) was among the winners. The BJP chose to field its own nominee, Prof. M. Nagaraj, for the single NDA-winnable seat rather than re-nominating JD(S)'s H.D. Deve Gowda, ending JD(S)'s hopes of retaining the seat [4000a5]. The Hindu explicitly identifies the winners: "Pawan Khera and Mansoor Ali Khan, who had contested on Congress ticket, and M. Nagaraja, who was a BJP nominee," alongside Kharge (INC) [223ed2]. The Indian Express confirms "All four candidates fielded by the Congress and the BJP for the Rajya Sabha seats from Karnataka were elected unopposed" [72faa5].

Since no candidate officially nominated by and listed as a JD(S) candidate won a Karnataka Rajya Sabha seat in this cycle, the question resolves NO.

Sources:
- The Hindu: https://www.thehindu.com/news/national/karnataka/mallikarjun-kharge-three-others-declared-unanimously-elected-to-rajya-sabha-from-karnataka/article71089166.ece [223ed2]
- The Indian Express: https://indianexpress.com/article/cities/bangalore/karnataka-rajya-sabha-elections-mallikarjun-kharge-pawan-khera-manoosr-m-khan-nagaraj-elected-unopposed-10734932/ [72faa5]
- The New Indian Express (BJP picks M Nagaraj, ends Deve Gowda's re-nomination hopes): https://www.newindianexpress.com/states/karnataka/2026/Jun/08/bjp-picks-m-nagaraj-for-rajya-sabha-polls-from-karnataka-ends-devegowdas-re-nomination-hopes [4000a5]

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-38. `90d886da-adb3-5fc0-b974-fefb4c31f6f6`

- Present date: `2026-05-16 13:42:01.140001`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Rodrigo Chaves resign or be removed from either of his ministerial positions in Costa Rica's Fernández administration by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026, and on or before July 1, 2026 (11:59 PM UTC), Rodrigo Chaves Robles ceases to hold either or both of the following ministerial positions in the Costa Rican government:

- **Minister of the Presidency** (Ministro de la Presidencia)
- **Minister of Finance** (Ministro de Hacienda)

"Ministerial position" refers to these two specific cabinet-level roles as defined under Costa Rican law.

A "resignation" means Chaves voluntarily relinquishes one or both positions, as confirmed by an official government decree published in Costa Rica's official gazette (*La Gaceta*, https://www.imprentanacional.go.cr/gaceta/) or a public statement from the Presidency of Costa Rica (https://www.presidencia.go.cr/).

A "removal" means President Fernández dismisses Chaves from one or both positions via an official government decree published in *La Gaceta* or announced by the Presidency.

This question resolves **No** if Chaves continues to hold both positions through 11:59 PM UTC on July 1, 2026.

**Resolution sources**: Official Costa Rican government gazette (*La Gaceta*) at https://www.imprentanacional.go.cr/gaceta/, the Costa Rican Presidency website at https://www.presidencia.go.cr/, or credible international news outlets such as Reuters (https://www.reuters.com), AP News (https://apnews.com), or Al Jazeera (https://www.aljazeera.com).

**Pre-cutoff background**

On May 8, 2026, Laura Fernández was sworn in as President of Costa Rica. In an unprecedented move, outgoing President Rodrigo Chaves Robles was appointed to serve simultaneously as Minister of the Presidency and Minister of Finance in her cabinet [https://apnews.com/article/laura-fernandez-costa-rica-chaves-trump-aa0c3ea1712f6ee67235fb1bf6317ac2](https://apnews.com/article/laura-fernandez-costa-rica-chaves-trump-aa0c3ea1712f6ee67235fb1bf6317ac2). This dual appointment is highly controversial for several reasons:

1. **Legal immunity**: The ministerial positions grant Chaves four years of legal immunity, shielding him from ongoing investigations by the Public Prosecutor's Office and the Supreme Electoral Tribunal into alleged corruption during his presidency [https://apnews.com/article/laura-fernandez-costa-rica-chaves-trump-aa0c3ea1712f6ee67235fb1bf6317ac2](https://apnews.com/article/laura-fernandez-costa-rica-chaves-trump-aa0c3ea1712f6ee67235fb1bf6317ac2).

2. **Political context**: Fernández won the presidency with Chaves's backing, and her party (Partido Progreso Social Democrático) holds a legislative majority. She has described herself as Chaves's political "heir." However, two previous legislative attempts to strip Chaves of immunity (September 2025 and December 2025) have already occurred [https://apnews.com/article/laura-fernandez-costa-rica-chaves-trump-aa0c3ea1712f6ee67235fb1bf6317ac2](https://apnews.com/article/laura-fernandez-costa-rica-chaves-trump-aa0c3ea1712f6ee67235fb1bf6317ac2).

3. **Criticism**: The arrangement has been described as a "de facto co-presidency" by analysts, and opposition lawmakers have questioned the constitutionality and democratic implications of the appointment.

As of May 12, 2026, Chaves holds both ministerial positions. His continued tenure depends on political dynamics including judicial actions, public opinion shifts, legislative pressure, and the Fernández administration's willingness to maintain the arrangement.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves NO if Rodrigo Chaves Robles continued to hold BOTH the position of Minister of the Presidency (Ministro de la Presidencia) AND Minister of Finance (Ministro de Hacienda) through 11:59 PM UTC on July 1, 2026. All available evidence confirms he did.

KEY EVIDENCE FROM A MANDATED RESOLUTION SOURCE:
- The official Costa Rican Presidency cabinet page (https://www.presidencia.go.cr/gabinete), an explicitly mandated resolution source, lists "Rodrigo Chaves Robles — Ministerio de la Presidencia y Ministerio de Hacienda" as a sitting cabinet member, with no other person occupying either portfolio [Gabinete | Presidencia de la República de Costa Rica](https://www.presidencia.go.cr/gabinete). This reflects the status as of the resolution window and shows he still simultaneously held both ministries.

CORROBORATING EVIDENCE:
- A Divergentes analysis dated June 30, 2026 ("El Superministro de la presidenta Laura Fernández, Rodrigo Chaves, 'cambia de despacho, no de poder'") describes his continued, ongoing dual role as Minister of the Presidency and Finance, with no mention of resignation or removal; it explicitly frames his tenure as the central, ongoing feature of the "continuidad" government [El Superministro de la presidenta Laura Fernández, Rodrigo ...](https://www.divergentes.com/rodrigo-chaves-superministro-laura-fernandez-costa-rica-analisis/).
- The English Wikipedia article on Rodrigo Chaves, last updated June 30, 2026, lists him as the incumbent Minister of the Presidency and Minister of Finance (assumed office May 8, 2026), with no end date [Rodrigo Chaves - Wikipedia](https://en.wikipedia.org/wiki/Rodrigo_Chaves).
- Additional (non-mandated) corroboration found via Google: a Teletica article (June 2026) titled "Rodrigo Chaves descarta renunciar a inmunidad como ministro por caso BCIE" indicates he explicitly ruled OUT giving up his ministerial immunity/position; a June 30, 2026 legislative session ("Plenario Legislativo, Sesión Ordinaria #31, 30 Junio 2026") analyzing "President Rodrigo Chaves Robles' latest report"; and a June 28, 2026 Divergentes piece still referring to him as "Superministro." These all show him actively serving as minister late into the window.

SEARCH PROCESS: I searched (in Spanish and English) for any resignation ("renuncia"), removal ("destitución"), cabinet reshuffle, or court action (Sala Constitucional annulment of his appointment) affecting Chaves's ministerial positions between May 12 and July 1, 2026. I found reporting about ongoing efforts to strip his legislative-style immunity and blocked penal proceedings (stalled due to missing substitute Sala Constitucional magistrates), but NO decree in La Gaceta, NO Presidency announcement, and NO Reuters/AP/Al Jazeera report of him resigning or being removed from either the Ministry of the Presidency or the Ministry of Finance. On the contrary, the official Presidency cabinet page still lists him in both roles [Gabinete | Presidencia de la República de Costa Rica](https://www.presidencia.go.cr/gabinete).

Because he held both positions continuously through the deadline (no resignation, no removal from either), the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-39. `b08b0a89-fffc-5d4b-a084-1b19ab0173d0`

- Present date: `2026-05-12 20:30:52.035988`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. Senate hold a cloture or floor vote on the Sanctioning Russia Act of 2025 (S.1241) on or after May 10, 2026, and before July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the full U.S. Senate (not a committee) holds a cloture vote or a floor vote on S.1241 (the Sanctioning Russia Act of 2025) on or after May 10, 2026, and before July 1, 2026, 11:59 PM UTC.

Definitions:
- A **cloture vote** is a recorded roll-call vote to invoke cloture on S.1241 itself or on a motion to proceed to S.1241, as defined under Senate Rule XXII.
- A **floor vote** is any recorded roll-call vote by the full Senate on S.1241, including votes on amendments to the bill, motions to proceed, or final passage. Voice votes and unanimous consent agreements do **not** count unless accompanied by a recorded roll-call vote.

The question resolves **No** if no such vote is recorded by the deadline.

**Primary resolution source:** The "Actions" tab on the official Congress.gov page for S.1241: https://www.congress.gov/bill/119th-congress/senate-bill/1241/all-actions

Secondary sources (if Congress.gov is unavailable or delayed): the Senate roll call vote records at https://www.senate.gov/legislative/votes.htm, or credible reporting from major outlets (e.g., Reuters, AP, NYT).

**Pre-cutoff background**

The Sanctioning Russia Act of 2025 (S.1241) is a bipartisan bill introduced on April 1, 2025, by Senator Lindsey Graham. It proposes sweeping sanctions on Russia, including a 500% tariff on imports from countries purchasing Russian energy products. The bill would be triggered if Russia refuses to negotiate a peace agreement to end the war in Ukraine [Sanctioning Russia Act - Wikipedia](https://en.wikipedia.org/wiki/Sanctioning_Russia_Act).

As of May 10, 2026, the bill has 84 cosponsors in the Senate — enough to override a presidential veto [S.1241 - Sanctioning Russia Act of 2025 119th Congress (2025-2026)](https://www.congress.gov/bill/119th-congress/senate-bill/1241)[Sanctioning Russia Act - Wikipedia](https://en.wikipedia.org/wiki/Sanctioning_Russia_Act). President Trump signaled support for the legislation in January 2026, and Senate Majority Leader Thune committed to bringing it to a vote when sufficient support was demonstrated. Despite this, the bill remains in the committee stage, having been referred to the Senate Committee on Banking, Housing, and Urban Affairs, with no floor or cloture votes recorded [S.1241 - Sanctioning Russia Act of 2025 119th Congress (2025-2026)](https://www.congress.gov/bill/119th-congress/senate-bill/1241).

The bill's progress has been repeatedly delayed by diplomatic developments in the Russia-Ukraine war. As of May 10, 2026, a 3-day ceasefire has been brokered between Russia and Ukraine, with Putin hinting that the war may be ending. This creates a dynamic tension: if peace talks advance, there is less urgency to vote on the sanctions bill; if they stall, legislative pressure mounts to bring the bill to the floor. Forecasters should weigh the interplay between executive-legislative dynamics and the trajectory of Russia-Ukraine diplomacy.

**Exact later resolution packet**

The question resolves NO because the full U.S. Senate did not hold any recorded roll-call cloture vote or floor vote on S.1241 (the Sanctioning Russia Act of 2025) on or after May 10, 2026, and before July 1, 2026.

Evidence:
- The primary resolution source, the official Congress.gov "All Actions" tab for S.1241 (https://www.congress.gov/bill/119th-congress/senate-bill/1241/all-actions), shows that the only recorded action on the bill is "04/01/2025 Read twice and referred to the Committee on Banking, Housing, and Urban Affairs." There are no recorded cloture votes, motions to proceed, or floor votes by the full Senate. This page was last updated 2026-07-01, i.e., after the close of the resolution window [https://www.congress.gov/bill/119th-congress/senate-bill/1241/all-actions](https://www.congress.gov/bill/119th-congress/senate-bill/1241/all-actions).
- The Washington Trade & Tariff Letter (wttlonline.com), dated 2026-07-01, confirms the bill remained "long-stalled" in the committee stage with no recorded floor or cloture vote during the window [Russia Sanctions to Finally Get a Vote?](https://www.wttlonline.com/stories/s1241-sanctioning-russia-act-of-2025,14665).
- Contextually, despite Trump's January 2026 "greenlight" and Majority Leader Thune's stated commitment to bring the bill to a vote, no Senate vote materialized within the window. A separate House measure (the Ukraine Support Act, passed 226-195 in June 2026) is a distinct House bill, not a Senate cloture/floor vote on S.1241, and therefore does not satisfy the resolution criteria, which require a vote by the full U.S. Senate on S.1241 specifically.

Because no qualifying recorded roll-call vote by the full Senate on S.1241 occurred between May 10, 2026 and July 1, 2026, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-40. `82c1367a-8d97-572b-952a-ded2063e5ed3`

- Present date: `2026-05-02 22:31:15.711475`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. Senate pass H.R. 3633, the Digital Asset Market Clarity Act of 2025, by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the U.S. Senate approves H.R. 3633 (the "Digital Asset Market Clarity Act of 2025") by a recorded vote on passage (see [Senate Glossary: Vote](https://www.senate.gov/reference/glossary_term/vote.htm)) between May 1, 2026, and 11:59 PM ET on June 1, 2026. This includes passage of the bill in any form — whether the original House-passed version, a Senate-amended version, or a Senate substitute amendment — so long as the bill number H.R. 3633 is the vehicle that receives a vote on passage.

For clarity:
- "Pass" means a vote on final passage ([Senate Glossary: Passage](https://www.senate.gov/reference/glossary_term/passage.htm)), not merely a procedural vote such as a vote on cloture ([Senate Glossary: Cloture](https://www.senate.gov/reference/glossary_term/cloture.htm)) or a motion to proceed.
- A voice vote on passage also counts.
- Passage of a different bill number (e.g., a standalone Senate bill) that contains substantially similar text does **not** count; it must be H.R. 3633.

This question resolves **No** if H.R. 3633 has not been passed by the Senate by the deadline.

**Resolution source:** The official Congress.gov page for H.R. 3633: https://www.congress.gov/bill/119th-congress/house-bill/3633

**Pre-cutoff background**

H.R. 3633, the "Digital Asset Market Clarity Act of 2025" (also known as the CLARITY Act), is a comprehensive crypto market structure bill that establishes regulatory frameworks for digital commodities, assigning primary oversight to the Commodity Futures Trading Commission (CFTC). The bill passed the U.S. House of Representatives on July 17, 2025, by a vote of 294–134 [https://www.congress.gov/bill/119th-congress/house-bill/3633](https://www.congress.gov/bill/119th-congress/house-bill/3633). It was received in the Senate on September 18, 2025, and referred to the Committee on Banking, Housing, and Urban Affairs [https://www.congress.gov/bill/119th-congress/house-bill/3633](https://www.congress.gov/bill/119th-congress/house-bill/3633).

In the Senate, the bill requires advancement through both the Banking Committee and the Agriculture Committee. The Senate Agriculture Committee voted 12–11 along party lines on January 29, 2026, to advance its version of the market structure legislation. The Senate Banking Committee had scheduled a markup for January 15, 2026, but postponed it due to over 100 proposed amendments. As of May 1, 2026, the Banking Committee has not completed its markup, and the bill has not reached the Senate floor.

The White House has been actively pushing for passage, with Treasury Secretary Bessent and crypto czar David Sacks pressuring Congress. Senator Bernie Moreno has stated that if the bill is not passed by May, "digital asset legislation will not pass for the foreseeable future," citing upcoming midterm election dynamics. Key disagreements remain, particularly around stablecoin yield provisions and partisan divisions on regulatory scope.

The bill's progress can be tracked at: https://www.congress.gov/bill/119th-congress/house-bill/3633

**Exact later resolution packet**

The question resolves NO. According to the official Congress.gov page for H.R. 3633 (the resolution source), the most recent Senate action on the bill was on May 14, 2026, when the Committee on Banking, Housing, and Urban Affairs ordered the bill reported with an amendment in the nature of a substitute favorably [17689b]. There is no record of the bill reaching the Senate floor for a recorded vote on final passage, nor any voice vote on passage, between May 1, 2026, and 11:59 PM ET on June 1, 2026.

This is corroborated by multiple sources: the Senate Banking Committee's own press release describes the May 14, 2026 action as advancing the bill via a "successful bipartisan markup" (https://www.banking.senate.gov/newsroom/majority/chairman-scott-senate-banking-committee-advance-clarity-act-in-historic-bipartisan-vote), which is a committee action, not Senate floor passage. The ELFA Washington Report (May 28, 2026) likewise states "On May 14, the Senate Banking Committee marked up and passed the bipartisan H.R. 3633" — again a committee passage, not floor passage. Binance Academy (as of May 2026) confirms the bill "has passed the U.S. House of Representatives and cleared the Senate Banking Committee, but it" had not been passed by the full Senate.

Clearing a committee markup is explicitly NOT the same as a vote on final passage on the Senate floor, which the resolution criteria require. Therefore, since H.R. 3633 was not passed by the full Senate by the June 1, 2026 deadline, the question resolves NO.

Action history URL: https://www.congress.gov/bill/119th-congress/house-bill/3633/all-actions

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-41. `85ef8961-a1f6-5d43-beaf-cb0927c2e057`

- Present date: `2026-05-01 16:36:07.582601`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will at least one of Fidelity, Franklin Templeton, Invesco, 21Shares, or VanEck begin staking in its spot Ethereum ETF by June 1, 2026?

**Resolution criteria**

This question resolves **YES** if, on or after April 30, 2026 and by 11:59 PM UTC on June 1, 2026, at least one of the following spot Ethereum ETFs receives full regulatory clearance to begin staking operations:

- Fidelity Ethereum Fund (FETH)
- Franklin Ethereum ETF (EZET)
- Invesco Galaxy Ethereum ETF (QETH)
- 21Shares Core Ethereum ETF (CETH)
- VanEck Ethereum ETF (ETHV)

**"Full regulatory clearance to begin staking"** (i.e., "staking amendment approval") requires BOTH of the following:
1. The listing exchange's proposed rule change (Form 19b-4) permitting the ETF to stake Ether must be approved by the SEC or filed as immediately effective, as documented on the [SEC's Self-Regulatory Organization Rulemaking page for National Securities Exchanges](https://www.sec.gov/rules-regulations/self-regulatory-organization-rulemaking/national-securities-exchanges); AND
2. The corresponding S-1 post-effective amendment (or registration statement amendment) permitting staking must be declared effective by the SEC, as documented on [SEC EDGAR](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&type=POS+EX&dateb=&owner=include&count=40&search_text=&action=getcompany).

BlackRock's ETHB (approved March 12, 2026) and Grayscale's ETHE are excluded, as their staking clearances preceded the resolution window.

If neither condition (1) nor condition (2) is met for any of the five listed issuers by the deadline, the question resolves **NO**.

The primary resolution source is official SEC filings on [SEC EDGAR](https://efts.sec.gov/LATEST/search-index?q=%22ethereum%22&dateRange=custom&startdt=2026-04-30&enddt=2026-06-01) and the [SEC SRO Rulemaking page](https://www.sec.gov/rules-regulations/self-regulatory-organization-rulemaking/national-securities-exchanges?sro_organization=All&field_display_title_value=ethereum&release_number=&file_number=&year=All&month=All). Confirmatory reporting from Bloomberg, Reuters, or the Wall Street Journal may also be used.

**Pre-cutoff background**

BlackRock's iShares Staked Ethereum Trust ETF (ETHB) launched on March 12, 2026, becoming the first U.S. spot Ethereum ETF to incorporate staking. On March 17, 2026, the SEC and CFTC issued a joint interpretive release classifying staking rewards as non-securities for 16 digital commodities including Ethereum, removing a key legal barrier [Why the SEC Decision Could Be Bigger Than the Bitcoin ETF - TECHi](https://www.techi.com/ethereum-etf-staking-sec-decision/).

As of April 30, 2026, five major issuers have pending staking amendments for their spot Ethereum ETFs [Why the SEC Decision Could Be Bigger Than the Bitcoin ETF - TECHi](https://www.techi.com/ethereum-etf-staking-sec-decision/):
- **Fidelity** (Fidelity Ethereum Fund, FETH) — pending amendment
- **Franklin Templeton** (Franklin Ethereum ETF, EZET) — 19b-4 rule change filed as immediately effective on April 15, 2026 (Release No. 34-105250, SR-CboeBZX-2026-026), with comment period ending May 11, 2026 [Notice of Filing and Immediate Effectiveness of a Proposed Rule ...](https://www.sec.gov/rule-release/34-105250) [National Securities Exchanges - Current - SEC.gov](https://www.sec.gov/rules-regulations/self-regulatory-organization-rulemaking/national-securities-exchanges?sro_organization=All&field_display_title_value=ethereum&release_number=&file_number=&year=All&month=All); S-1 post-effective amendment status pending
- **Invesco** (Invesco Galaxy Ethereum ETF, QETH) — pending amendment
- **21Shares** (21Shares Core Ethereum ETF, CETH) — pending amendment
- **VanEck** (VanEck Ethereum ETF, ETHV) — pending amendment

For Fidelity, Invesco, 21Shares, and VanEck, no 19b-4 rule change filings for staking have yet appeared on the SEC's Self-Regulatory Organization Rulemaking page as of April 30, 2026 [National Securities Exchanges - Current - SEC.gov](https://www.sec.gov/rules-regulations/self-regulatory-organization-rulemaking/national-securities-exchanges?sro_organization=All&field_display_title_value=ethereum&release_number=&file_number=&year=All&month=All). These amendments are expected to clear their final review windows in Q2 2026, but the SEC has a history of delays [Why the SEC Decision Could Be Bigger Than the Bitcoin ETF - TECHi](https://www.techi.com/ethereum-etf-staking-sec-decision/).

Enabling staking requires two regulatory steps: (1) approval or effectiveness of a proposed rule change (Form 19b-4) filed by the listing exchange, and (2) the SEC declaring the corresponding S-1 post-effective amendment effective. Both must be completed before an ETF can commence staking operations.

**Exact later resolution packet**

The question resolves NO. It required that, between April 30, 2026 and 11:59 PM UTC June 1, 2026, at least one of Fidelity (FETH), Franklin Templeton (EZET), Invesco (QETH), 21Shares (CETH), or VanEck (ETHV) achieve BOTH (1) an approved/immediately-effective 19b-4 rule change AND (2) an effective S-1 post-effective amendment permitting staking.

Evidence:
- SEC Self-Regulatory Organization Rulemaking page (National Securities Exchanges, filtered for "ethereum"): The only relevant 19b-4 for the five issuers was Franklin Templeton's SR-CboeBZX-2026-026 (Release No. 34-105250), filed immediately-effective on April 15, 2026 — which predates the April 30, 2026 window start. No new 19b-4 rule changes for Fidelity, Invesco, 21Shares, or VanEck staking appeared during the window [https://www.sec.gov/rules-regulations/self-regulatory-organization-rulemaking/national-securities-exchanges?sro_organization=All&field_display_title_value=ethereum&release_number=&file_number=&year=All&month=All](https://www.sec.gov/rules-regulations/self-regulatory-organization-rulemaking/national-securities-exchanges?sro_organization=All&field_display_title_value=ethereum&release_number=&file_number=&year=All&month=All).
- SEC EDGAR search for "staking" POS EX filings between 2026-04-30 and 2026-06-01 returned no S-1 post-effective amendments for any of the five listed issuers (the only staking-related POS EX hit was Bitwise's BITW, which is not one of the five) [https://efts.sec.gov/LATEST/search-index?q=%22staking%22&forms=POS+EX&startdt=2026-04-30&enddt=2026-06-01](https://efts.sec.gov/LATEST/search-index?q=%22staking%22&forms=POS+EX&startdt=2026-04-30&enddt=2026-06-01).
- The Franklin Ethereum Trust (CIK 0002011535) EDGAR filing history shows no POS EX / S-1 post-effective amendment declared effective in the window, so even Franklin — the only fund with an effective 19b-4 — failed to meet condition (2) [https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002011535&type=POS+EX&dateb=&owner=include&count=40](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002011535&type=POS+EX&dateb=&owner=include&count=40).
- An industry guide (Everstake, dated ~April 20, 2026) confirms only Grayscale's ETHE and BlackRock's ETHB were live staking ETFs, and that Fidelity, Franklin Templeton, Invesco, 21Shares, and VanEck still had "pending staking amendments" expected to clear in Q2 2026 — i.e., not yet cleared [Ethereum Staking ETFs for Institutions: Full Guide 2026 | Everstake](https://everstake.one/resources/blog/ethereum-staking-etfs-for-institutions).
- BlackRock's ETHB (launched March 12, 2026) and Grayscale's ETHE are explicitly excluded by the resolution criteria.

Since no single one of the five named funds satisfied BOTH regulatory conditions within the window, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-42. `be4bfb46-4cb4-5557-9a1c-00cd32a5c1ba`

- Present date: `2026-05-14 03:47:40.222496`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will French President Macron make a public statement explicitly supporting passage of the 'aide à mourir' bill between May 12 and June 30, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026 and before 23:59 CEST (UTC+2) on June 30, 2026, French President Emmanuel Macron makes a public statement explicitly supporting the passage of the 'aide à mourir' (assisted dying) bill currently before the French Parliament.

**Definition of "public statement":** Any of the following qualify:
1. An official communication published on the Élysée Palace website (https://www.elysee.fr/);
2. A post on one of Macron's verified social media accounts (e.g., @EmmanuelMacron on X/Twitter, Facebook, or Instagram);
3. A direct quote attributed to Macron in a televised interview or press conference, as reported by at least one major French news agency or outlet (AFP, Reuters, France 24, Le Monde, Le Figaro).

**Definition of "explicitly supporting the passage":** The statement must clearly call for, endorse, or urge the adoption/passage of the aide à mourir bill or the right to aided dying as defined in the current legislation. The following do NOT qualify:
- General remarks about the importance of end-of-life care, dignity in dying, or palliative care without specific reference to the aide à mourir legislative text or the right to assisted dying it creates;
- Statements expressing sympathy or openness to the debate without endorsing passage;
- Statements by government ministers or spokespersons not directly quoting Macron.

If no qualifying statement is found by the resolution deadline, the question resolves NO.

**Resolution source:** The Élysée Palace website (https://www.elysee.fr/), AFP dispatches, or reporting by Le Monde (https://www.lemonde.fr/), France 24 (https://www.france24.com/), or RFI (https://www.rfi.fr/).

**Pre-cutoff background**

France's end-of-life reform bill creating a "droit à l'aide à mourir" (right to assisted dying) has been a flagship social reform of the Macron presidency. The National Assembly passed the bill in May 2025. The French Senate rejected the bill a first time on January 28–29, 2026, stripping out the assisted dying provisions and retaining only palliative care measures. The bill returned to the National Assembly, which again approved the aide à mourir provisions in February 2026. On May 12, 2026, the Senate rejected the bill for a second time. Following this second Senate rejection, the National Assembly continued legislative work, with deputies approving a key article on the right to aided dying on May 17, 2026 [[PODCAST] Le débat sur la fin de vie dans la dernière ligne droite](https://www.dailymotion.com/video/xa2k084).

President Macron initially endorsed the aide à mourir framework in March 2024 and had promised an assisted dying law upon his 2022 re-election. However, he faces a delicate political balance: the government needs Senate cooperation on other legislative priorities, and his coalition includes members with differing views on the issue. While Macron has been broadly supportive of end-of-life reform, it remains uncertain whether he will make an explicit public statement calling for passage of the specific aide à mourir legislation following the second Senate rejection, as doing so could strain relations with the Senate majority.

The bill's legislative dossier is tracked at: https://www.senat.fr/dossier-legislatif/ppl24-661.html

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if, between May 12 and June 30, 2026 (23:59 CEST), Emmanuel Macron *personally* made a public statement (Élysée website, his verified social media, or a direct quote reported by AFP/Reuters/France 24/Le Monde/Le Figaro/RFI) explicitly calling for/endorsing/urging passage of the 'aide à mourir' bill. After extensive searching across the specified sources, no such qualifying statement by Macron himself within that window could be found.

Key evidence:

1. Context confirmed: The Senate rejected the bill for the second time on May 12, 2026, and the National Assembly re-approved the right to aided dying (third reading) on June 30, 2026 (295 vs 232), with final vote scheduled July 15 — but the reporting of these events quotes deputies, ministers (Falorni, Panifous, Vautrin, Bayrou), not Macron. Le Monde's June 30 report and Le Figaro's June 30 report contain no direct Macron quote [https://www.lemonde.fr/societe/article/2026/06/30/fin-de-vie-l-assemblee-nationale-approuve-a-nouveau-la-proposition-de-loi-instaurant-un-droit-a-l-aide-a-mourir-le-vote-final-aura-lieu-le-15-juillet_6717297_3224.html](https://www.lemonde.fr/societe/article/2026/06/30/fin-de-vie-l-assemblee-nationale-approuve-a-nouveau-la-proposition-de-loi-instaurant-un-droit-a-l-aide-a-mourir-le-vote-final-aura-lieu-le-15-juillet_6717297_3224.html) [L'Assemblée adopte pour la troisième fois la loi légalisant l ...](https://www.lefigaro.fr/politique/l-assemblee-adopte-pour-la-troisieme-fois-la-loi-legalisant-l-euthanasie-et-le-suicide-assiste-20260630). RFI's June 30 explainer likewise contains no Macron quote [Fin de vie: ce que changera la future loi sur le droit à l'aide à mourir](https://www.rfi.fr/fr/france/20260630-fin-de-vie-ce-que-changera-la-future-loi-sur-le-droit-%C3%A0-l-aide-%C3%A0-mourir).

2. All of Macron's known explicit endorsements of the bill predate the window. His "Je souhaite que le texte engagé aujourd'hui soit voté" dates from May 2025, per HuffPost [Sur l'aide à mourir, l'échec annoncé de la CMP met Macron face à ...](https://www.huffingtonpost.fr/politique/article/sur-l-aide-a-mourir-l-echec-annonce-de-la-cmp-met-macron-face-a-une-de-ses-promesses_264308.html) [Sur l'aide à mourir, l'échec annoncé de la CMP met Macron face à ...](https://www.huffingtonpost.fr/politique/article/sur-l-aide-a-mourir-l-echec-annonce-de-la-cmp-met-macron-face-a-une-de-ses-promesses_264308.html); his referendum-if-blocked remarks and support for a 'texte d'équilibre' date from May 13, 2025 per LCP [Fin de vie : Emmanuel Macron évoque un 'référendum' si le texte ...](https://lcp.fr/actualites/fin-de-vie-emmanuel-macron-evoque-un-referendum-si-le-texte-etait-bloque-au-parlement); his framing as a "loi de fraternité/humanité" comes from the March 2024 Libération/La Croix interview and a 2025 TF1 interview. None fall within May 12–June 30, 2026.

3. During the window itself, reporting attributes the push for adoption to the *government*, not to a personal public statement by Macron. Le Monde's June 3 article describes "la stratégie de l'exécutif" and merely characterizes the bill as "ce texte souhaité par Emmanuel Macron" while quoting minister Laurent Panifous — no direct Macron statement in the window [https://www.lemonde.fr/politique/article/2026/06/03/fin-de-vie-la-strategie-de-l-executif-pour-faire-adopter-le-texte-de-loi-cet-ete_6696659_823448.html](https://www.lemonde.fr/politique/article/2026/06/03/fin-de-vie-la-strategie-de-l-executif-pour-faire-adopter-le-texte-de-loi-cet-ete_6696659_823448.html). La Croix's June 2 article attributes the July 15 vote promise to Panifous, not Macron [Loi sur la fin de vie : vote définitif le 15 juillet à l'Assemblée, promet ...](https://www.la-croix.com/societe/loi-sur-la-fin-de-vie-vote-definitif-le-15-juillet-a-l-assemblee-promet-le-gouvernement-20260602). HuffPost (June 2/3) frames the CMP failure as putting Macron "face à une de ses promesses" and notes he "tient à la loi," but reports no new Macron statement in the window [Sur l'aide à mourir, l'échec annoncé de la CMP met Macron face à ...](https://www.huffingtonpost.fr/politique/article/sur-l-aide-a-mourir-l-echec-annonce-de-la-cmp-met-macron-face-a-une-de-ses-promesses_264308.html) [Sur l'aide à mourir, l'échec annoncé de la CMP met Macron face à ...](https://www.huffingtonpost.fr/politique/article/sur-l-aide-a-mourir-l-echec-annonce-de-la-cmp-met-macron-face-a-une-de-ses-promesses_264308.html).

4. Official Élysée source checked: the June 3, 2026 Conseil des ministres report on elysee.fr does not mention the aide à mourir bill at all [Compte rendu du conseil des ministres du 3 juin 2026. - Elysee.fr](https://www.elysee.fr/emmanuel-macron/2026/06/03/compte-rendu-du-conseil-des-ministres-du-3-juin-2026).

5. The Vie publique "fin de vie dans les discours publics" listing contains no Macron discourse endorsing passage within the window [La fin de vie dans les discours publics | Vie publique](https://www.vie-publique.fr/discours-dans-lactualite/288980-la-fin-de-vie-dans-les-discours-publics). Franceinfo's Macron topic page lists his window activities (G7, foreign affairs, heatwave) but no explicit aide à mourir endorsement in the window [Emmanuel Macron - Toute l'actualité du Président de la République](https://www.franceinfo.fr/politique/emmanuel-macron/). Le Monde's May 13 article on the Senate rejection contains no Macron reaction quote [https://www.lemonde.fr/societe/article/2026/05/13/pourquoi-le-senat-a-rejete-a-nouveau-le-texte-sur-l-aide-a-mourir_6688635_3224.html](https://www.lemonde.fr/societe/article/2026/05/13/pourquoi-le-senat-a-rejete-a-nouveau-le-texte-sur-l-aide-a-mourir_6688635_3224.html). A TF1 Info listing referencing a June 3 Élysée "perron" item ties the mid-July adoption promise to Panifous/others, not to a Macron statement on the bill [Emmanuel Macron - Page | TF1 Info](https://www.tf1info.fr/actualite/emmanuel-macron-10153/2/).

Because no qualifying explicit public statement by Macron himself within the May 12–June 30, 2026 window was found in any of the designated resolution sources — consistent with the reported strategy of letting the government and the Assembly ("dernier mot") carry the process rather than Macron intervening personally — the resolution criteria's YES condition is not met, and per the criteria ("If no qualifying statement is found by the resolution deadline, the question resolves NO"), the question resolves NO.

Primary source URLs consulted include:
- https://www.lemonde.fr/politique/article/2026/06/03/fin-de-vie-la-strategie-de-l-executif-pour-faire-adopter-le-texte-de-loi-cet-ete_6696659_823448.html [https://www.lemonde.fr/politique/article/2026/06/03/fin-de-vie-la-strategie-de-l-executif-pour-faire-adopter-le-texte-de-loi-cet-ete_6696659_823448.html](https://www.lemonde.fr/politique/article/2026/06/03/fin-de-vie-la-strategie-de-l-executif-pour-faire-adopter-le-texte-de-loi-cet-ete_6696659_823448.html)
- https://www.huffingtonpost.fr/politique/article/sur-l-aide-a-mourir-l-echec-annonce-de-la-cmp-met-macron-face-a-une-de-ses-promesses_264308.html [Sur l'aide à mourir, l'échec annoncé de la CMP met Macron face à ...](https://www.huffingtonpost.fr/politique/article/sur-l-aide-a-mourir-l-echec-annonce-de-la-cmp-met-macron-face-a-une-de-ses-promesses_264308.html) [Sur l'aide à mourir, l'échec annoncé de la CMP met Macron face à ...](https://www.huffingtonpost.fr/politique/article/sur-l-aide-a-mourir-l-echec-annonce-de-la-cmp-met-macron-face-a-une-de-ses-promesses_264308.html)
- https://www.lemonde.fr/societe/article/2026/06/30/fin-de-vie-l-assemblee-nationale-approuve-a-nouveau-la-proposition-de-loi-instaurant-un-droit-a-l-aide-a-mourir-le-vote-final-aura-lieu-le-15-juillet_6717297_3224.html [https://www.lemonde.fr/societe/article/2026/06/30/fin-de-vie-l-assemblee-nationale-approuve-a-nouveau-la-proposition-de-loi-instaurant-un-droit-a-l-aide-a-mourir-le-vote-final-aura-lieu-le-15-juillet_6717297_3224.html](https://www.lemonde.fr/societe/article/2026/06/30/fin-de-vie-l-assemblee-nationale-approuve-a-nouveau-la-proposition-de-loi-instaurant-un-droit-a-l-aide-a-mourir-le-vote-final-aura-lieu-le-15-juillet_6717297_3224.html)
- https://www.lefigaro.fr/politique/l-assemblee-adopte-pour-la-troisieme-fois-la-loi-legalisant-l-euthanasie-et-le-suicide-assiste-20260630 [L'Assemblée adopte pour la troisième fois la loi légalisant l ...](https://www.lefigaro.fr/politique/l-assemblee-adopte-pour-la-troisieme-fois-la-loi-legalisant-l-euthanasie-et-le-suicide-assiste-20260630)
- https://www.rfi.fr/fr/france/20260630-fin-de-vie-ce-que-changera-la-future-loi-sur-le-droit-%C3%A0-l-aide-%C3%A0-mourir [Fin de vie: ce que changera la future loi sur le droit à l'aide à mourir](https://www.rfi.fr/fr/france/20260630-fin-de-vie-ce-que-changera-la-future-loi-sur-le-droit-%C3%A0-l-aide-%C3%A0-mourir)
- https://www.elysee.fr/emmanuel-macron/2026/06/03/compte-rendu-du-conseil-des-ministres-du-3-juin-2026 [Compte rendu du conseil des ministres du 3 juin 2026. - Elysee.fr](https://www.elysee.fr/emmanuel-macron/2026/06/03/compte-rendu-du-conseil-des-ministres-du-3-juin-2026)
- https://lcp.fr/actualites/fin-de-vie-emmanuel-macron-evoque-un-referendum-si-le-texte-etait-bloque-au-parlement [Fin de vie : Emmanuel Macron évoque un 'référendum' si le texte ...](https://lcp.fr/actualites/fin-de-vie-emmanuel-macron-evoque-un-referendum-si-le-texte-etait-bloque-au-parlement)

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-43. `a8b542ab-b696-549c-9ee4-fb880d46627c`

- Present date: `2026-04-30 14:49:23.180265`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-05-31 00:00:00`

**Question**

Will Claude Opus 4.7 Thinking be ranked #1 overall on the LMSYS Chatbot Arena leaderboard on May 31, 2026?

**Resolution criteria**

This question resolves based on the state of the LMSYS Chatbot Arena **Overall** text leaderboard at **23:59 UTC on May 31, 2026**.

**Resolution source:** The "Overall" tab (with style control unchecked) of the Chatbot Arena LLM leaderboard at https://arena.ai/leaderboard/text (or its Hugging Face mirror at https://huggingface.co/spaces/lmarena-ai/arena-leaderboard). If both URLs are available and show different results, the arena.ai URL takes precedence.

**Resolves YES** if a model whose name contains "claude-opus-4-7" or "Claude Opus 4.7" occupies rank #1 on the Overall leaderboard at the specified time. If Claude Opus 4.7 is **tied** for rank #1 (i.e., shares the exact same displayed Elo score with another model at the top position), this still resolves **YES**.

**Resolves NO** if:
- Any other model holds the sole #1 rank, or
- Claude Opus 4.7 is not listed on the leaderboard at all by the resolution time, or
- The leaderboard is unavailable or discontinued (and no archived snapshot from within 48 hours of the resolution time can be found).

**Important:** Only the "Overall" leaderboard ranking counts. Rankings in specific categories (e.g., Coding, Hard Prompts, Math, or any language-specific leaderboard) do **not** count for resolution purposes.

**Pre-cutoff background**

The LMSYS Chatbot Arena (now hosted at arena.ai, formerly lmarena.ai) is the most widely referenced human-preference ranking system for large language models. It uses a Bradley-Terry model to compute Elo-style ratings based on crowdsourced pairwise comparisons.

As of approximately April 19–22, 2026, the #1 ranked model on the overall text leaderboard is **Claude Opus 4.7 Thinking** (by Anthropic) with an Elo score of approximately **1504–1505** [LMSys Arena Elo in 2026: How to Actually Read the AI Leaderboard](https://smartchunks.com/lmsys-arena-elo-leaderboard-explained-2026/) [https://ofox.ai/blog/llm-leaderboard-best-ai-models-ranked-2026/](https://ofox.ai/blog/llm-leaderboard-best-ai-models-ranked-2026/). The competition is tight: Gemini 3.1 Pro Preview sits at approximately 1492 Elo (rank 6), and GPT-5.4 is also highly ranked [LMSys Arena Elo in 2026: How to Actually Read the AI Leaderboard](https://smartchunks.com/lmsys-arena-elo-leaderboard-explained-2026/). The gap between rank 1 and rank 6 is only about 13 Elo points, meaning new model releases or shifts in voting patterns could change the top position.

The leaderboard updates continuously as new votes are cast and new models are added. Major competitors (OpenAI, Google DeepMind, xAI) frequently release updated models that could displace the current leader.

**Exact later resolution packet**

Best-effort resolution: NO. The resolution criteria require the Chatbot Arena text “Overall” leaderboard with style control unchecked at 23:59 UTC on May 31, 2026. I queried the official style-control-off Overall URL, https://arena.ai/leaderboard/text/overall-no-style-control. The data returned for that page was last updated May 17, 2026, and showed rank #1 as `claude-opus-4-6-thinking` with score 1500±4, while `claude-opus-4-7-thinking` was rank #4 with score 1486±6, so Claude Opus 4.7 was not #1 or tied for #1 in the official Overall/no-style-control page I could retrieve [LLM Leaderboard - Best Text & Chat AI Models Compared - Arena AI](https://arena.ai/leaderboard/text/overall-no-style-control). I also queried the generic official text leaderboard URL, https://arena.ai/leaderboard/text, which likewise returned May 17, 2026 data showing `claude-opus-4-6-thinking` at rank #1 and `claude-opus-4-7-thinking` below it rather than tied for #1 [https://arena.ai/leaderboard/text](https://arena.ai/leaderboard/text). The Hugging Face mirror URL, https://huggingface.co/spaces/lmarena-ai/arena-leaderboard, did not expose leaderboard rows, model names, ranks, or scores in the retrievable document [https://huggingface.co/spaces/lmarena-ai/arena-leaderboard](https://huggingface.co/spaces/lmarena-ai/arena-leaderboard). Therefore, to the best of the available official-source evidence, the condition for YES was not met, and the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-44. `1d6995ce-2697-5474-be07-edac6114b257`

- Present date: `2026-04-30 11:11:55.683824`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will David Zaslav have an announced executive or board role in the combined Paramount-WBD entity as of June 1, 2026?

**Resolution criteria**

This question resolves YES if, as of 11:59 PM UTC on June 1, 2026, David Zaslav has been publicly announced or confirmed to hold an executive or board position in the combined Paramount-WBD entity (whether the merger has closed or not). This question resolves NO otherwise.

**Definitions:**

- **"Executive or board position"** (i.e., an "announced role") means any of the following in the combined entity:
  - A position as an officer (https://www.law.cornell.edu/wex/officer_of_a_corporation) of the combined entity, including but not limited to CEO, Co-CEO, President, CFO, COO, or any other C-suite title.
  - A position as a member of the Board of Directors (https://en.wikipedia.org/wiki/Board_of_directors), including but not limited to Chair, Co-Chair, Vice Chair, or Director.

- **"Combined entity"** means the corporate entity resulting from or formed to effectuate the Paramount Skydance–Warner Bros. Discovery merger, or any parent or successor entity thereof, including any entity announced as the combined operating company.

- **"Announced"** means explicitly confirmed via at least one of: (a) an official press release from Paramount, WBD, or the combined entity posted on their official press pages (https://www.paramount.com/press or https://www.wbd.com/news); (b) an SEC filing (searchable at https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=paramount&CIK=&type=8-K&dateb=&owner=include&count=40&search_text=&action=getcompany or https://efts.sec.gov/LATEST/search-index?q=%22warner%20bros%20discovery%22&dateRange=custom&startdt=2026-04-01&enddt=2026-06-01&forms=8-K); or (c) credible reporting from major outlets such as CNBC (https://www.cnbc.com), Reuters (https://www.reuters.com), or The Wall Street Journal (https://www.wsj.com).

**If the merger has not legally closed by June 1, 2026:** The question can still resolve YES if Zaslav has been announced for an executive or board role in the combined entity (e.g., via a press release or proxy filing naming post-merger leadership), even if the merger has not yet closed. If no such announcement has been made, the question resolves NO.

**If the merger agreement is terminated before June 1, 2026:** The question resolves NO, as there would be no combined entity.

**Pre-cutoff background**

On February 27, 2026, Paramount Skydance and Warner Bros. Discovery (WBD) confirmed a merger agreement valued at approximately $110 billion [Massive Merger Confirmed: Paramount & WBD Reveal Details Of ...](https://deadline.com/2026/02/massive-merger-confirmed-paramount-and-wbd-reveal-details-1236738785/). WBD shareholders voted overwhelmingly to approve the deal on April 23, 2026 [Warner Bros. Discovery shareholders approve Paramount acquisition](https://www.cnbc.com/2026/04/23/warner-bros-discovery-shareholder-vote-paramount-deal.html). The merger is expected to close in Q3 2026, subject to regulatory clearances.

David Zaslav currently serves as CEO of WBD. Reports indicate that Paramount initially offered Zaslav co-CEO and co-chair roles in the combined entity [Warner Bros. Discovery shareholders approve Paramount acquisition](https://www.cnbc.com/2026/04/23/warner-bros-discovery-shareholder-vote-paramount-deal.html). However, a Variety feature published April 21, 2026 reported that Zaslav is expected to depart following the merger's completion, though sources close to him suggest he would prefer to remain in a leadership role [$500 Million Exit: David Zaslav Is Leaving Warner Bros. a Rich Man](https://variety.com/2026/film/features/david-zaslav-warner-bros-exit-paramount-sale-1236726226/). His total payout from the deal could exceed $800 million, including up to $335 million in tax reimbursements on accelerated stock vesting [Warner Bros. Discovery shareholders approve Paramount acquisition](https://www.cnbc.com/2026/04/23/warner-bros-discovery-shareholder-vote-paramount-deal.html).

WBD shareholders rejected Zaslav's "golden parachute" compensation package by an 82% margin in a non-binding advisory vote on April 23, 2026 [Warner Bros. Discovery shareholders approve Paramount acquisition](https://www.cnbc.com/2026/04/23/warner-bros-discovery-shareholder-vote-paramount-deal.html). Despite this symbolic rebuke, the payments are still contractually scheduled to proceed.

As of April 29, 2026, the specific leadership structure of the combined entity has not been finalized or publicly disclosed [Massive Merger Confirmed: Paramount & WBD Reveal Details Of ...](https://deadline.com/2026/02/massive-merger-confirmed-paramount-and-wbd-reveal-details-1236738785/). The deal has not yet legally closed and remains subject to regulatory approval. The tension between Zaslav's reported desire to stay, the shareholder backlash against his compensation, and the lack of a confirmed post-merger role creates genuine uncertainty about whether he will hold an announced position by June 1, 2026.

**Exact later resolution packet**

The question resolves NO. As of 11:59 PM UTC on June 1, 2026, David Zaslav had NOT been publicly announced or confirmed to hold an executive or board position in the combined Paramount-WBD entity.

Key findings:

1. MERGER NOT TERMINATED (antecedent for NO via termination clause does not apply): The Paramount Skydance–WBD merger agreement was NOT terminated before June 1, 2026. WBD shareholders approved the deal on April 23, 2026, and as of late May 2026 the deal remained pending regulatory approval, expected to close Q3 2026 [fe1e2d]. So the question must be resolved on the substantive criterion.

2. NO ANNOUNCED ROLE FOR ZASLAV: The consistent and authoritative reporting is that Zaslav is DEPARTING after the merger, not taking a role in the combined company. An April 21, 2026 Variety feature reported he is "leaving Warner Bros." and will "walk away after four years at the helm" with a payout of at least $550 million; while he would personally prefer to stay, no executive or board role in the combined entity was announced for him [ccb52d]. The Wikipedia article on the acquisition, last updated May 28, 2026, contains no announcement of any executive or board role for Zaslav in the combined entity, and notes the combined-entity leadership structure had not been publicly disclosed [fe1e2d].

3. Earlier offers (co-CEO/co-chair) were rebuffed by the WBD board and never materialized into an announced role; reporting (Deadline, Oct 2025) noted "no clear role for Zaslav" in the merged company. By the deal's announcement and through the resolution window, no press release from Paramount/WBD, no SEC filing/proxy, and no CNBC/Reuters/WSJ report named Zaslav to an officer or director position in the combined company.

Because no executive or board role for Zaslav in the combined Paramount-WBD entity had been announced by the deadline, and the merger had not been terminated, the question resolves NO.

Sources: Variety "$500 Million Exit: David Zaslav Is Leaving Warner Bros." (https://variety.com/2026/film/features/david-zaslav-warner-bros-exit-paramount-sale-1236726226/) [ccb52d]; Wikipedia "Proposed acquisition of Warner Bros. Discovery by Paramount Skydance" (https://en.wikipedia.org/wiki/Proposed_acquisition_of_Warner_Bros._Discovery_by_Paramount_Skydance) [fe1e2d].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-45. `e5498ac7-a091-5ada-abde-bab20e569425`

- Present date: `2026-05-03 09:19:30.751022`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-05-20 00:00:00`

**Question**

Will the minutes of the April 28–29, 2026 FOMC meeting indicate that more than four participants supported or preferred a lower policy rate?

**Resolution criteria**

This question resolves **Yes** if the official minutes of the April 28–29, 2026 FOMC meeting, published by the Board of Governors of the Federal Reserve at https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm, indicate that more than four participants (including both voting and non-voting members) supported, preferred, or argued in favor of a lower federal funds rate target range at that meeting.

This question resolves **No** if the minutes indicate that four or fewer participants supported or preferred a lower rate, or if the minutes do not provide sufficient information to determine the number of participants favoring a rate cut.

**Key definitions:**

- **"Participant"**: Any individual who participates in the FOMC meeting discussion, including both voting members and non-voting Reserve Bank presidents who attend. This is the standard usage in FOMC minutes (see https://www.federalreserve.gov/monetarypolicy/fomc.htm).

- **"Supported or preferred a lower federal funds rate"**: A participant is counted if the minutes describe them as favoring, supporting, preferring, or arguing for a reduction in the federal funds rate target range at that meeting. This includes both formal dissenters who voted for a rate cut and non-voting participants described as preferring a cut. It does **not** include participants who merely noted that cuts might be appropriate at a future meeting without advocating for action at the April meeting.

- **"Dissenting vote"**: A vote cast by an FOMC voting member against the majority decision, as recorded in the official FOMC statement (see https://www.federalreserve.gov/monetarypolicy/fomc.htm). A dissent "in favor of a rate cut" means the member voted for a lower federal funds rate target range than the one adopted by the majority.

- **"More than four"**: Five or more participants.

The FOMC minutes typically use quantitative language such as "a few" (generally 2–3), "some" (generally 3–4), "several" (generally 4–5), or "many" (generally 5+) to describe participant views. The resolution will rely on either explicit counts or standard interpretation of these quantifiers as used by the Federal Reserve.

**Resolution source:** The official FOMC minutes published at https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm, expected to be released on May 20, 2026, at 2:00 p.m. ET (18:00 UTC).

**Resolution deadline:** If the minutes are not published by June 1, 2026, at 23:59 UTC, this question resolves **No**.

**Pre-cutoff background**

On April 29, 2026, the Federal Open Market Committee (FOMC) voted 8–4 to hold the federal funds rate at 3.50%–3.75%, the most divided decision since 1992. According to reporting from Reuters and CNBC, four members dissented: one (Fed Governor Stephen Miran) dissented in favor of a quarter-point rate cut, while three regional bank presidents dissented against including an easing bias in the statement [[PDF] FEDERAL FUNDS RATE HOLDS STEADY APRIL 29, 2026 - Stephens](https://www.stephens.com/uploads/shared/documents/PCG-Docs/FOMC-Updates/Fed-Update-4-29-26.pdf). This was the final FOMC meeting chaired by Jerome Powell, whose term as Fed Chair expires May 15, 2026. Kevin Warsh, President Trump's nominee to succeed Powell, was advanced by the Senate Banking Committee on the same day (April 29) in a party-line vote.

The FOMC statement reveals formal votes but does not capture the full range of views expressed during the meeting discussion. The detailed minutes, scheduled for release on May 20, 2026, at 2:00 p.m. ET (18:00 UTC), will describe the breadth of sentiment among all meeting participants (including non-voting members). Given the historic level of formal dissent, it is plausible—but uncertain—that additional participants beyond the four formal dissenters expressed a preference for lower rates during the discussion.

The next scheduled FOMC meeting is June 16–17, 2026, which falls outside the resolution window of this question.

**Exact later resolution packet**

NO. The official Federal Reserve FOMC calendar entry for the April 28–29, 2026 meeting links to the minutes at https://www.federalreserve.gov/monetarypolicy/fomcminutes20260429.htm and the PDF at https://www.federalreserve.gov/monetarypolicy/files/fomcminutes20260429.pdf, and says they were released May 20, 2026, before the June 1, 2026 deadline [https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm). In the minutes themselves, the relevant count is one: the policy-action section says “One member voted against that decision and preferred to lower the target range by 1/4 percentage point,” with Stephen I. Miran identified as voting against the action, and the participants’ discussion separately says “One participant preferred to lower the target range for the federal funds rate 25 basis points” [The Fed - Monetary Policy: - Federal Reserve](https://www.federalreserve.gov/monetarypolicy/fomcminutes20260429.htm). The minutes also mention “Several participants” saying it would likely be appropriate to lower the target range once future conditions were met, but that is explicitly about possible future cuts and does not count under the question’s criteria [The Fed - Monetary Policy: - Federal Reserve](https://www.federalreserve.gov/monetarypolicy/fomcminutes20260429.htm). Therefore, the minutes indicate four or fewer—indeed, only one—participant supported or preferred a lower federal funds rate target range at the April meeting, so the “more than four” threshold was not met [The Fed - Monetary Policy: - Federal Reserve](https://www.federalreserve.gov/monetarypolicy/fomcminutes20260429.htm).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-46. `ab058f5e-8e7e-56df-b954-1466e841c02a`

- Present date: `2026-05-16 20:24:25.893064`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Selahattin Demirtaş be released from prison in Turkey between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if Selahattin Demirtaş (https://en.wikipedia.org/wiki/Selahattin_Demirta%C5%9F) is fully released from Turkish state custody on or after May 12, 2026, 00:00 UTC, and before July 1, 2026, 23:59 UTC. "Fully released" means he is no longer held in prison or any other form of involuntary state detention. **House arrest, conditional release with electronic monitoring, or temporary medical leave do NOT count as release** — he must be free from all forms of state-imposed detention or confinement. A presidential pardon, commutation, or court-ordered release all qualify, provided the result is full freedom from custody.

This question resolves as **No** if Demirtaş remains in prison or any form of state detention (including house arrest) through July 1, 2026, 23:59 UTC.

**Resolution source:** Official confirmation via the Official Gazette of the Republic of Turkey (T.C. Resmî Gazete, https://www.resmigazete.gov.tr/), OR credible reporting from at least one of the following international news agencies: Reuters, Associated Press (AP), Agence France-Presse (AFP), or BBC News.

**Pre-cutoff background**

Selahattin Demirtaş, former co-chair of the Peoples' Democratic Party (HDP), has been imprisoned in Turkey since November 2016. He is currently held at Edirne F-Type High Security Prison [https://turkishminute.com/2026/04/23/jailed-kurdish-politicians-say-their-release-will-be-as-political-as-their-imprisonment/](https://turkishminute.com/2026/04/23/jailed-kurdish-politicians-say-their-release-will-be-as-political-as-their-imprisonment/). In May 2024, a Turkish court sentenced him to 42 years in prison in connection with the 2014 Kobani protests case, charges he denies [https://turkishminute.com/2026/04/23/jailed-kurdish-politicians-say-their-release-will-be-as-political-as-their-imprisonment/](https://turkishminute.com/2026/04/23/jailed-kurdish-politicians-say-their-release-will-be-as-political-as-their-imprisonment/). In January 2026, he received an additional sentence of 3 years and 6 months for insulting President Erdoğan.

The European Court of Human Rights (ECtHR) has issued final and binding rulings (in 2018 and 2020) finding that his detention violated his rights and ordering his immediate release. Turkey has not implemented these rulings [https://turkishminute.com/2026/04/23/jailed-kurdish-politicians-say-their-release-will-be-as-political-as-their-imprisonment/](https://turkishminute.com/2026/04/23/jailed-kurdish-politicians-say-their-release-will-be-as-political-as-their-imprisonment/).

As of April 2026, Demirtaş remains in prison. He and other jailed Kurdish politicians have stated they are "not counting the days" until release, emphasizing that any release will be a political decision [https://turkishminute.com/2026/04/23/jailed-kurdish-politicians-say-their-release-will-be-as-political-as-their-imprisonment/](https://turkishminute.com/2026/04/23/jailed-kurdish-politicians-say-their-release-will-be-as-political-as-their-imprisonment/). In November 2025, Erdoğan's nationalist ally Devlet Bahçeli publicly stated it "would be beneficial" to release Demirtaş, signaling a possible shift linked to a renewed Kurdish peace process. However, no concrete steps toward release have materialized as of April 2026.

The question is genuinely uncertain: binding ECHR rulings and peace process momentum push toward release, while Turkey's history of defiance, the 42-year sentence, and Erdoğan's political calculus push against it.

**Exact later resolution packet**

The question asks whether Selahattin Demirtaş was FULLY released from Turkish state custody between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC). The evidence shows he remained imprisoned in Edirne F-Type High Security Prison throughout the entire window, so this resolves NO (0).

Key evidence, including from a specified resolution source (Reuters):

- Reuters, dated June 24, 2026 ("Turkey working on legislation to speed up militant PKK's disbandment, Erdogan says," https://www.reuters.com/world/erdogan-says-legal-framework-speed-up-militant-pkks-disbandment-underway-2026-06-24/): As of June 24, 2026 — just one week before the window closed — the peace/legal-framework process was still only "underway" (in preparation), with no release of Demirtaş reported; the reporting still treats Kurdish political prisoners as jailed [Turkey working on legislation to speed up militant PKK's ... - Reuters](https://www.reuters.com/world/erdogan-says-legal-framework-speed-up-militant-pkks-disbandment-underway-2026-06-24/). This confirms no release had occurred as of that date.

- Bianet, dated June 26, 2026 (https://bianet.org/haber/selahattin-demirtasin-yeni-fotografi-yayinlandi-320934): Explicitly states Demirtaş "has been imprisoned in Edirne F-Type Prison since November 4, 2016" and quotes DEM Party official Tayip Temel saying "We are expecting a release" (Biz bir tahliye bekliyoruz) — i.e., he had NOT been released as of late June 2026 [Selahattin Demirtaş'ın yeni fotoğrafı yayınlandı - Bianet](https://bianet.org/haber/selahattin-demirtasin-yeni-fotografi-yayinlandi-320934).

- Corroborating context (search-level): On June 24, 2026, Demirtaş himself published an article titled "Az kaldı" ("It's almost time"), signaling he was still awaiting release; his party colleagues publicly stated they were still "awaiting a release." Turkish media coverage on June 25 and June 30, 2026 continued to debate WHETHER he would be released (e.g., "Demirtaş tahliye edilecek mi?"), which is only coherent if he was still incarcerated. Turkish Minute (June 25, 2026) reported the PKK law was still limited to arms verification, with no freedom yet.

State-imposed detention clause: All sources confirm Demirtaş remained in full incarceration at Edirne F-Type High Security Prison — not house arrest, not conditional release with electronic monitoring, and not temporary medical leave. He remained under full state-imposed detention through the close of the window (July 1, 2026, 23:59 UTC). No presidential pardon, commutation, or court-ordered release resulting in full freedom occurred within the window.

Therefore the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-47. `f1d14406-358d-568b-8f3d-90c583c0bd88`

- Present date: `2026-05-29 06:33:06.699041`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the FAA Administrator certify and implement the 3.8% air traffic controller pay raise by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026, and by 11:59 PM ET on July 1, 2026, the FAA officially implements the 3.8% pay raise for air traffic controllers authorized in the FY2026 appropriations. "Officially implemented" means at least one of the following has occurred:

1. The Office of Personnel Management (OPM) publishes revised pay tables reflecting the 3.8% increase for air traffic controllers on its [pay tables page](https://www.opm.gov/policy-data-oversight/pay-leave/salaries-wages/); OR
2. The FAA issues an official announcement (via its [newsroom](https://www.faa.gov/newsroom) or official memorandum) confirming that the FAA Administrator has certified the required conditions and that the pay raise is being processed for affected employees; OR
3. Credible federal workforce news sources (e.g., [Federal News Network](https://federalnewsnetwork.com/), [Government Executive](https://www.govexec.com/)) report, based on official FAA or OPM documentation, that the raise has been implemented and is appearing on pay stubs.

**Key definitions:**
- "FAA Administrator certification" refers to the determination, at the Administrator's sole discretion, that improvements in workforce scheduling, staffing utilization, or other operational efficiencies have been achieved that contribute to addressing workforce shortfalls and enhancing aviation safety, as required by the FY2026 appropriations legislation [3.8% pay raise for air traffic controllers, Education Dept cuts rejected](https://federalnewsnetwork.com/congress/2026/01/3-8-pay-raise-for-air-traffic-controllers-education-dept-cuts-rejected-highlights-from-final-fy-2026-spending-bills/).
- "Air traffic controller" refers to employees as defined under [5 U.S.C. § 2109(1)(A)](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title5-section2109&num=0&edition=prelim).

The question resolves **No** if no such official confirmation of implementation is issued by 11:59 PM ET on July 1, 2026. Note: retroactive pay adjustments that are formally authorized and processed before July 1, 2026, count as implementation even if they cover pay periods prior to May 12, 2026. However, only certifications and implementation actions occurring on or after May 12, 2026, count toward resolution.

**Pre-cutoff background**

In the FY2026 appropriations process, Congress authorized $140 million for the FAA to provide a 3.8% pay raise for air traffic controllers (as defined by [5 U.S.C. § 2109(1)(A)](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title5-section2109&num=0&edition=prelim)), as well as air traffic controller supervisors and managers who manage air traffic [3.8% pay raise for air traffic controllers, Education Dept cuts rejected](https://federalnewsnetwork.com/congress/2026/01/3-8-pay-raise-for-air-traffic-controllers-education-dept-cuts-rejected-highlights-from-final-fy-2026-spending-bills/). The raise was included in appropriations bills finalized in January 2026 [3.8% pay raise for air traffic controllers, Education Dept cuts rejected](https://federalnewsnetwork.com/congress/2026/01/3-8-pay-raise-for-air-traffic-controllers-education-dept-cuts-rejected-highlights-from-final-fy-2026-spending-bills/), but the government subsequently experienced a 76-day shutdown [Congress Approves 3.8% Pay Increase of Air Traffic Managers and ...](https://www.faama.org/congress-approves-3-8-pay-increase-of-air-traffic-managers-and-supervisors/).

On April 30, 2026, the House passed the legislation ending the shutdown and funding DHS, which included the air traffic controller pay raise provision [Congress Approves 3.8% Pay Increase of Air Traffic Managers and ...](https://www.faama.org/congress-approves-3-8-pay-increase-of-air-traffic-managers-and-supervisors/). The legislation stipulates that the raise "shall be implemented for all such employees only to the extent that the Administrator determines, in his sole discretion, that improvements in workforce scheduling, staffing utilization, or other operational efficiencies are achieved that contribute to addressing workforce shortfalls and enhancing aviation safety" [3.8% pay raise for air traffic controllers, Education Dept cuts rejected](https://federalnewsnetwork.com/congress/2026/01/3-8-pay-raise-for-air-traffic-controllers-education-dept-cuts-rejected-highlights-from-final-fy-2026-spending-bills/). If the FAA Administrator makes this certification, the pay adjustment would be retroactive to the first pay period beginning after January 1, 2026 [Congress Approves 3.8% Pay Increase of Air Traffic Managers and ...](https://www.faama.org/congress-approves-3-8-pay-increase-of-air-traffic-managers-and-supervisors/).

As of May 13, 2026, it remains unclear whether the FAA Administrator has made the required determination. The FAA Managers Association (FAAMA) has stated it is working to clarify the situation [Congress Approves 3.8% Pay Increase of Air Traffic Managers and ...](https://www.faama.org/congress-approves-3-8-pay-increase-of-air-traffic-managers-and-supervisors/). The raise was previously stalled by the DHS funding lapse [Air traffic controller pay raise stalled by DHS shutdown](https://www.govexec.com/pay-benefits/2026/02/air-traffic-controller-pay-raise-stalled-dhs-shutdown/411472/), and even with appropriations now enacted, the Administrator's sole-discretion certification requirement creates uncertainty about whether and when the raise will actually appear in paychecks.

**Exact later resolution packet**

The question resolves NO because no evidence exists that the FAA officially implemented the 3.8% air traffic controller pay raise—via any of the three specified channels—on or after May 12, 2026 and by 11:59 PM ET on July 1, 2026.

Background: Congress authorized $140M for a 3.8% pay raise for controllers (5 U.S.C. §2109(1)(A)) in FY2026 appropriations, but implementation is contingent on the FAA Administrator (Bryan Bedford) certifying, in his sole discretion, that workforce scheduling/staffing/operational efficiency improvements were achieved. This was confirmed by the FAAMA statement (April 30, 2026), which noted eligibility and the discretionary determination were "not entirely clear" and that FAAMA "will be working to clarify this information in the coming days/weeks" — i.e., no certification had been made as of late April [Congress Approves 3.8% Pay Increase of Air Traffic Managers and ...](https://www.faama.org/congress-approves-3-8-pay-increase-of-air-traffic-managers-and-supervisors/).

Checking each of the three resolution channels within the required window (May 12 – July 1, 2026):

1) OPM pay tables: No evidence OPM published revised pay tables reflecting a 3.8% increase for air traffic controllers. Searches only surfaced OPM's separate 3.8% raise for federal law enforcement personnel (effective Jan. 11, 2026), which is a distinct action and not the FAA controller raise.

2) FAA official announcement: A query of the FAA newsroom (as rendered as of July 1, 2026) found no press release, statement, or memorandum indicating the Administrator certified the required conditions or that the raise was being processed [https://www.faa.gov/newsroom](https://www.faa.gov/newsroom). The FAA's May 2026 activity concerned the new Air Traffic Controller Workforce/hiring plan, not the pay-raise certification.

3) Credible federal workforce news (Federal News Network / Government Executive): Government Executive's pay-raise topic page's most recent relevant article remained the February 18, 2026 piece "Air traffic controller pay raise stalled by DHS shutdown," with no later article reporting certification or implementation [Pay Raise - Government Executive](https://www.govexec.com/topic/pay-raise/). A FedWeek article dated June 29, 2026 about FAA on-the-job training incentives made no mention of the 3.8% raise being certified or implemented [On-the-Job Training at FAA Falling Short Despite Incentive ...](https://www.fedweek.com/federal-managers-daily-report/on-the-job-training-at-faa-falling-short-despite-incentive-payments-says-report/). Federal News Network's coverage remained the January 2026 explainer with no implementation follow-up found.

Contemporaneous r/ATC discussions from early May 2026 (before the resolution window opened) showed the raise still pending and dependent on Bedford's discretionary certification, with no confirmation it had occurred [https://old.reddit.com/r/ATC/comments/1t1qr8q/whats_the_status_of_the_38/](https://old.reddit.com/r/ATC/comments/1t1qr8q/whats_the_status_of_the_38/) [https://old.reddit.com/r/ATC/comments/1t10uuz/backpay_for_raise/](https://old.reddit.com/r/ATC/comments/1t10uuz/backpay_for_raise/).

Since none of the three qualifying implementation events (OPM tables, FAA announcement, or credible news report based on official documentation) occurred within May 12 – July 1, 2026, and the FAA newsroom as of July 1 contained no such announcement, the question resolves NO (0). This is a direct binary (not a conditional), so annulment does not apply.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-48. `f89f281e-bd03-5c52-954c-f96adcc48b04`

- Present date: `2026-04-30 19:03:19.738502`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

IF President Trump and President Xi Jinping hold an in-person bilateral meeting between April 30 and June 1, 2026, THEN will China announce new export restrictions on rare earth elements or critical minerals targeting the US between April 30 and June 1, 2026?

**Resolution criteria**

This conditional question resolves YES if B resolves YES AND A resolves YES. It resolves NO if B resolves YES AND A resolves NO. If B resolves NO, this question is voided (no resolution / N/A).

=== Resolution Criteria for A (Will China announce new export restrictions on rare earth elements or critical minerals targeting the US between April 30 and June 1, 2026?) ===
This question resolves **Yes** if, between April 30, 2026, 00:00 UTC and June 1, 2026, 23:59 UTC, the Ministry of Commerce of the People's Republic of China (MOFCOM) or the State Council of the PRC officially announces one or more **new** export restrictions on rare earth elements or critical minerals that target the United States. Specifically:

**"New export restriction"** means any of the following that was not already in effect as of April 29, 2026, 23:59 UTC:
- Addition of a rare earth element or critical mineral (or products derived therefrom) to a formal export control or licensing requirement list;
- A new or expanded licensing requirement for export of such materials;
- A total or partial ban on export of such materials;
- Addition of US entities to an export control list specifically restricting rare earth elements or critical minerals.

Mere restatements, extensions, or routine renewals of existing restrictions do not count.

**"Rare earth elements"** are the 17 elements as defined by the USGS: lanthanum, cerium, praseodymium, neodymium, promethium, samarium, europium, gadolinium, terbium, dysprosium, holmium, erbium, thulium, ytterbium, lutetium, scandium, and yttrium. See: https://www.usgs.gov/centers/national-minerals-information-center/rare-earths-statistics-and-information

**"Critical minerals"** are any of the 60 mineral commodities on the USGS 2025 Final List of Critical Minerals (https://www.usgs.gov/media/images/2025-list-critical-minerals), which includes gallium, germanium, antimony, graphite, cobalt, tungsten, and others.

**"Targeting the US"** means the announcement must explicitly name the United States, US entities, or US end-users as the subject of the restriction, OR the restriction must apply specifically to exports destined for the United States (as distinct from broadly applicable global export controls). A general export licensing requirement that applies to all countries equally does **not** qualify unless the announcement text or an accompanying MOFCOM statement specifically references the United States.

**Resolution source:** Official MOFCOM announcements at https://english.mofcom.gov.cn/Policies/AnnouncementsOrders/index.html, supplemented by credible reporting from Reuters (https://www.reuters.com), AP, Bloomberg, or the Wall Street Journal. The announcement date (not the effective date) determines whether it falls within the resolution window.

This question resolves **No** if no such announcement is made by June 1, 2026, 23:59 UTC.

=== Resolution Criteria for B (Will President Trump and President Xi Jinping hold an in-person bilateral meeting between April 30 and June 1, 2026?) ===
This question resolves **Yes** if, on or after April 30, 2026 and on or before June 1, 2026 (all dates interpreted in UTC), President Donald Trump and President Xi Jinping hold an in-person bilateral meeting.

**Definition of "in-person bilateral meeting":** A scheduled, formal meeting where both heads of state are physically present in the same room or venue for the purpose of diplomatic discussion between the United States and China, lasting at least 30 minutes. Brief informal encounters (e.g., a handshake or short exchange on the sidelines of a multilateral event without a dedicated bilateral session) do not count. A meeting held as a formal bilateral session on the sidelines of a multilateral summit does count, provided it is a dedicated U.S.-China session.

**Resolution source:** Official confirmation from the White House (https://www.whitehouse.gov/) or the Chinese Ministry of Foreign Affairs (https://www.fmprc.gov.cn/eng/), or consistent reporting from at least two of the following credible news agencies: Reuters (https://www.reuters.com/), Associated Press (https://apnews.com/), AFP, or Bloomberg. The source must confirm that the meeting physically took place (not merely that it was scheduled).

If no such meeting is confirmed by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

This is a conditional question linking two underlying binary events.

=== Background for A (Will China announce new export restrictions on rare earth elements or critical minerals targeting the US between April 30 and June 1, 2026?) ===
China and the United States are operating under a trade truce signed in October 2025. However, China has continued to expand its economic toolkit during this period [https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/](https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/). Key developments as of April 30, 2026 include:

- **October 9, 2025:** China expanded rare earth export controls, adding five elements (holmium, erbium, thulium, europium, and ytterbium) and rare earth refining technology to its control list [https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/](https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/).
- **November 8, 2025:** Export controls took effect on high-end lithium-ion batteries, cathodes, and graphite anode material [https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/](https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/).
- **February 2026:** MOFCOM added 20 Japanese entities to its export control list and issued restricted/watch lists.
- **April 7, 2026:** The State Council issued new regulations on industrial and supply chain security [https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/](https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/).
- **April 13, 2026:** The State Council authorized countermeasures against foreign states for "unlawful extraterritorial jurisdiction" [https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/](https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/).
- **April 15, 2026:** Chinese officials held talks regarding potential limits on exports of advanced solar panel manufacturing equipment to the US [https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/](https://www.reuters.com/world/china/how-china-has-expanded-its-economic-toolkit-during-its-trade-truce-with-us-2026-04-26/).
- **April 24, 2026:** MOFCOM added seven EU entities to China's Export Control List.

China suspended some US-focused dual-use export bans (on gallium, germanium, antimony, and superhard materials) as part of the October 2025 truce, but has not reversed its April 2025 licensing requirements for medium- and heavy-rare-earth elements. A US-China summit is approaching, creating tension between escalation as leverage and restraint as goodwill.

The primary resolution source is the Chinese Ministry of Commerce (MOFCOM) official announcements page: https://english.mofcom.gov.cn/Policies/AnnouncementsOrders/index.html

=== Background for B (Will President Trump and President Xi Jinping hold an in-person bilateral meeting between April 30 and June 1, 2026?) ===
As of late April 2026, U.S. President Donald Trump is scheduled to visit China for a summit with President Xi Jinping on May 14–15, 2026. This would be the first visit to China by an American president in eight years [https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/](https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/). However, the summit was previously postponed from late March 2026 due to the ongoing Iran conflict [https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/). The U.S.-China relationship remains tense, characterized by tit-for-tat tariffs and what has been described as an "adrift" and "erratic" China policy from the Trump administration [https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/](https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/). The volatile geopolitical environment—including the Iran war and unresolved trade disputes—creates genuine uncertainty about whether the summit will proceed as currently scheduled or face another postponement.

Key sources:
- Reuters, "Trump's trade war with China in focus ahead of May summit" (April 6, 2026): https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/
- Reuters, "With tariffs stalled, Trump's China policy drifts" (April 21, 2026): https://www.reuters.com/world/us/with-tariffs-stalled-trumps-china-policy-drifts-2026-04-21/

**Exact later resolution packet**

This is a Metaculus conditional question ("IF B, THEN A" structure where B = the in-person Trump-Xi bilateral meeting is the antecedent, and A = China announcing new export restrictions targeting the US is the consequent). Per the resolution criteria: resolves YES if B and A both occur; NO if B occurs but A does not; voided/annulled if B does not occur.

CONDITION B (antecedent) — OCCURRED:
President Trump made a state visit to China and held an in-person bilateral summit with President Xi Jinping in Beijing on May 13–15, 2026, at the Great Hall of the People [f121d8]. This is corroborated by the BBC's coverage titled "Trump and Xi conclude 'very successful' talks" reporting the May 14–15, 2026 summit [019378], plus extensive concurrent reporting from Reuters (https://www.reuters.com/world/trump-xi-summit-live-talks-beijing-include-iran-trade-taiwan-2026-05-14/), AP, CNN, NYT, and CNBC. The formal two-day summit with welcome ceremony and substantive talks (on trade, AI, Taiwan, Iran) far exceeds the 30-minute threshold and constitutes a dedicated U.S.-China bilateral session. Therefore the antecedent is satisfied and the question is NOT annulled — it resolves on the consequent A alone.

CONDITION A (consequent) — DID NOT OCCUR:
Between April 30 and June 1, 2026, China did NOT announce any new export restriction on rare earth elements or critical minerals targeting the United States. To the contrary, the period was characterized by China EASING and suspending controls and offering goodwill ahead of/around the summit. The Wikipedia summary of the state visit reports trade-facilitating outcomes (US approval for Chinese firms to buy NVIDIA H200 chips, China ordering 200 Boeing aircraft) and no new Chinese export restrictions [f121d8]. The BBC reported the summit produced few concrete deals and no new export restrictions; the October 2025 truce involved Beijing easing rare-earth restrictions, and the summit did not reverse that direction [019378]. Reuters reporting on May 18, 2026 ("White House gets small rare earth win...") states China AGREED TO ADDRESS US concerns over shortages of yttrium, scandium, indium and neodymium (https://www.reuters.com/business/aerospace-defense/china-has-agreed-address-us-concerns-over-rare-earth-shortages-says-white-house-2026-05-18/) — i.e., loosening, not tightening. Reuters on May 20, 2026 reported China defended its existing controls as lawful and said it would cooperate with US "reasonable" concerns (https://www.reuters.com/business/aerospace-defense/china-says-rare-earth-controls-lawful-will-cooperate-with-us-reasonable-concerns-2026-05-20/), again reflecting maintenance/easing of existing measures rather than any new restriction. No MOFCOM or State Council announcement of a new rare-earth/critical-mineral export restriction targeting the US (new listing, new/expanded licensing requirement, ban, or addition of US entities) was issued in the April 30 – June 1, 2026 window. Pre-existing measures (April 2025 Announcement 18 licensing; October 9, 2025 Announcements 61/62; suspensions in November 2025) all predate the window and do not count as "new"; mere restatements/renewals are explicitly excluded.

Because B occurred but A did not, the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-49. `051de11f-3528-5761-9c24-e3c720baaf22`

- Present date: `2026-05-12 15:06:56.353451`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the USA finish first in Group A at the 2026 IIHF World Championship preliminary round?

**Resolution criteria**

This question resolves **Yes** if the United States is ranked 1st in the final Group A standings of the 2026 IIHF World Championship preliminary round, as published on the official IIHF standings page: https://www.iihf.com/en/events/2026/wm/standings

The preliminary round concludes on May 26, 2026 (UTC). The final standings are based on total points accumulated across all seven group-stage games.

In the event of a points tie, first place is determined according to the official IIHF tie-breaking rules [Tournament Info 2026 IIHF ICE HOCKEY WORLD CHAMPIONSHIP](https://www.iihf.com/en/events/2026/wm/tournamentinfo/68948/tournament_info):
- **Two teams tied**: The winner of the head-to-head game between the two tied teams is ranked higher.
- **Three or more teams tied**: A sub-group is formed among the tied teams, and the following criteria are applied in order: (1) points in direct games among tied teams, (2) goal difference in direct games, (3) goals scored in direct games, (4) results against the closest best-ranked team outside the sub-group, (5) results against the next best-ranked outside team, and (6) original tournament seeding.

This question resolves **No** if the USA finishes in any position other than 1st in Group A, or if the tournament/group stage is cancelled or not completed by June 1, 2026 (UTC).

**Resolution source**: The official IIHF 2026 World Championship standings page at https://www.iihf.com/en/events/2026/wm/standings

**Pre-cutoff background**

The 2026 IIHF Ice Hockey World Championship is held in Switzerland (Zurich and Fribourg) from May 15 to May 31, 2026 (all times UTC+2 local, UTC+0 for scheduling purposes) [2026 IIHF World Championship Group A - Wikipedia](https://en.wikipedia.org/wiki/2026_IIHF_World_Championship_Group_A). Switzerland hosting the tournament gives its national team significant home-ice advantage, with passionate local crowds expected to fill arenas and create a hostile environment for opponents.

Group A is played at the Swiss Life Arena in Zurich and consists of eight teams: USA, Switzerland, Finland, Germany, Latvia, Austria, Hungary, and Great Britain [2026 IIHF World Championship Group A - Wikipedia](https://en.wikipedia.org/wiki/2026_IIHF_World_Championship_Group_A). The preliminary round runs from May 15 to May 26, 2026 (UTC), with each team playing seven games in a single round-robin format [Tournament Info 2026 IIHF ICE HOCKEY WORLD CHAMPIONSHIP](https://www.iihf.com/en/events/2026/wm/tournamentinfo/68948/tournament_info).

As of the most recent IIHF World Rankings (updated May 26, 2025), the key teams in Group A are ranked as follows [IIHF World Ranking Men](https://www.iihf.com/en/static/68775/iihf_world_rankings_men):
- **USA**: 1st (3,985 points)
- **Switzerland**: 2nd (3,975 points)
- **Finland**: 6th (3,780 points)
- **Germany**: 7th (3,710 points)

The USA enters as the top-ranked team in the world but faces stiff competition from Switzerland (near-equal ranking plus home-ice advantage), Finland (a perennial powerhouse with deep talent), and Germany (a rising program). A key variable is NHL player availability—teams whose NHL players are eliminated earlier from the Stanley Cup Playoffs can bolster their rosters more quickly.

Points are awarded as follows: 3 points for a regulation win, 2 points for an overtime/shootout win, 1 point for an overtime/shootout loss, and 0 points for a regulation loss [2026 IIHF World Championship Group A - Wikipedia](https://en.wikipedia.org/wiki/2026_IIHF_World_Championship_Group_A). As of May 11, 2026, no games have yet been played [2026 IIHF World Championship Group A - Wikipedia](https://en.wikipedia.org/wiki/2026_IIHF_World_Championship_Group_A).

**Exact later resolution packet**

The question resolves NO because the USA did NOT finish first in Group A of the 2026 IIHF World Championship preliminary round.

**Evidence and reasoning:**

1. The base resolution URL specified in the question (https://www.iihf.com/en/events/2026/wm/standings) returns a "Page not found" (404) [833c3b], but the official IIHF standings live under https://www.iihf.com/en/events/2026/wm/standings/group. Querying that official IIHF page yields the final Group A preliminary-round standings [4d5a4b].

2. **Final Group A standings (all 7 games played per team)** per the official IIHF page [4d5a4b], corroborated by Wikipedia's 2026 IIHF World Championship Group A article [a0a9cb] and by The Sporting News/Yahoo Sports coverage [7653c4]:
   - 1. Switzerland (SUI): 21 points
   - 2. Finland (FIN): 18 points
   - 3. Latvia (LAT): 12 points
   - 4. United States (USA): 11 points
   - 5. Germany (GER): 10 points
   - 6. Austria (AUT): 9 points
   - 7. Hungary (HUN): 3 points
   - 8. Great Britain (GBR): 0 points

3. **Group A confirmation (not Group B or overall rank):** All three sources explicitly label this as the Group A table [4d5a4b, a0a9cb, 7653c4]. This is distinct from Group B (won by Canada) and from the overall final tournament placement (won by Finland, who beat Switzerland 1–0 in OT in the final).

4. **Tie-breaking check:** There was no points tie affecting first place. Switzerland finished clearly ahead in 1st place with 21 points, 3 points clear of 2nd-place Finland (18) [4d5a4b, a0a9cb]. The USA (11 points) finished 4th, well behind first place, so IIHF tie-break rules for first place are not implicated. (Note: the USA was only 1 point ahead of 5th-place Germany at 10 points, but this is irrelevant to the 1st-place question.)

5. **Completion check:** The preliminary round was fully completed — each team played all 7 games (GP = 7) and final standings were published, well before the June 1, 2026 deadline [4d5a4b, a0a9cb]. The tournament was not cancelled. Therefore the "resolves No if cancelled/not completed by June 1" clause is not triggered on that basis; it resolves No simply because the USA finished 4th, not 1st.

**Conclusion:** Switzerland finished 1st in Group A with 21 points; the USA finished 4th with 11 points. The question "Will the USA finish first in Group A?" resolves NO.

Primary evidence URL: https://www.iihf.com/en/events/2026/wm/standings/group

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-50. `189a2191-0981-5025-9bc7-6f1c88676a4a`

- Present date: `2026-05-01 12:54:51.973962`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the New York State Assembly pass the Facial Recognition Technology Study Act (S3699 / A8788) by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the New York State Assembly passes S3699 or its companion bill A8788 on or after April 30, 2026, and on or before June 1, 2026, at 11:59 PM ET. "Pass" means a successful floor vote (third reading) in the Assembly approving the bill. The Governor's signature is **not** required for a Yes resolution — legislative passage by the Assembly alone is sufficient.

This question resolves **No** if neither S3699 nor A8788 has passed the Assembly floor vote by 11:59 PM ET on June 1, 2026.

**Resolution source:** The official New York State Legislature bill tracking pages:
- https://www.nysenate.gov/legislation/bills/2025/S3699
- https://www.nysenate.gov/legislation/bills/2025/A8788

A Yes resolution requires the bill status on either page to reflect passage by the Assembly (e.g., "Passed Assembly") on or after April 30, 2026.

**Pre-cutoff background**

The Facial Recognition Technology Study Act (S3699) was introduced in the New York State Senate by Senator James Sanders Jr. It would establish a task force to study privacy concerns and regulatory approaches regarding facial recognition technology. The bill passed the New York State Senate on March 16, 2026, with a vote of 60-2 [https://www.nysenate.gov/legislation/bills/2025/S3699](https://www.nysenate.gov/legislation/bills/2025/S3699). As of April 30, 2026, S3699 is in the Assembly Committee on Governmental Operations. The companion Assembly bill is A8788 [https://www.nysenate.gov/legislation/bills/2025/S3699](https://www.nysenate.gov/legislation/bills/2025/S3699). For the bill to become law, it must pass the Assembly and be signed by the Governor. The New York State Legislature's regular session typically runs through June, meaning Assembly action is plausible but not guaranteed within this window.

**Exact later resolution packet**

The question resolves NO because neither S3699 nor its companion bill A8788 passed a New York State Assembly floor vote (third reading) between April 30, 2026 and June 1, 2026 (11:59 PM ET).

Evidence from the official New York State Assembly bill tracking page for the companion Assembly bill A8788 (https://www.assembly.state.ny.us/leg/?bn=A08788): the only recorded actions are "06/05/2025: Referred to Governmental Operations" and "01/07/2026: Referred to Governmental Operations." There is no record of an Assembly floor passage; the bill remained in the Governmental Operations Committee [4b0bce].

Evidence from the official New York State Assembly tracking page for the Senate bill S03699 (https://assembly.state.ny.us/leg/?bn=S03699): the bill was delivered to the Assembly on March 16, 2026 and referred to the Committee on Governmental Operations. The "Floor Votes" section of the official record explicitly states "There are no Assembly votes for this bill in this legislative session," meaning no third-reading floor vote occurred in the Assembly [0107e0].

The bill did pass the New York State Senate on March 16, 2026 (60-2), but Senate passage alone is insufficient per the resolution criteria, which require passage by the Assembly. As of the close of the resolution window (June 1, 2026, 11:59 PM ET), both bill versions remained stuck in the Assembly Committee on Governmental Operations with no floor vote, so the question resolves NO.

Per the resolution criteria, the Governor's signature was not required for a Yes resolution — only Assembly floor passage was needed, and that did not occur.

Resolution sources (official NY Legislature bill tracking pages):
- https://www.assembly.state.ny.us/leg/?bn=A08788 [4b0bce]
- https://assembly.state.ny.us/leg/?bn=S03699 [0107e0]
- https://www.nysenate.gov/legislation/bills/2025/A8788
- https://www.nysenate.gov/legislation/bills/2025/S3699

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-51. `505d483a-c9e2-551a-a805-0674d449093a`

- Present date: `2026-05-14 02:57:00.001418`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will the U.S. Supreme Court's opinion in Pitchford v. Cain (No. 24-7351) be unanimous (no dissenting votes on the judgment)?

**Resolution criteria**

This question resolves **Yes** if the final opinion in Pitchford v. Cain (No. 24-7351), published on or after May 12, 2026 (UTC), is unanimous on the judgment—meaning no Justice files or joins a dissenting opinion as to the judgment (outcome of the case). A concurrence in the judgment with a different rationale does NOT count as a dissent; only a vote against the majority's disposition of the case counts. The question resolves **No** if at least one Justice dissents from the judgment.

Resolution is determined by the official slip opinion published on the U.S. Supreme Court's slip opinions page: https://www.supremecourt.gov/opinions/slipopinion/25

If the opinion is not published by July 1, 2026 (UTC), resolution is postponed until the opinion is published.

**Pre-cutoff background**

Pitchford v. Cain (No. 24-7351) is a capital case before the U.S. Supreme Court concerning Terry Pitchford, a death-row inmate in Mississippi. The central question is whether the Mississippi Supreme Court unreasonably determined, under the Antiterrorism and Effective Death Penalty Act (AEDPA, 28 U.S.C. § 2254), that Pitchford waived his Batson v. Kentucky (1986) challenge to racial discrimination in jury selection by failing to rebut the prosecutor's race-neutral explanations for striking Black jurors.

Oral arguments were held on March 31, 2026 (ET). According to SCOTUSblog's April 2, 2026 (ET) recap [https://www.scotusblog.com/2026/04/court-appears-sympathetic-to-death-row-inmates-attempt-to-challenge-racial-discrimination-in-jury-selection/](https://www.scotusblog.com/2026/04/court-appears-sympathetic-to-death-row-inmates-attempt-to-challenge-racial-discrimination-in-jury-selection/), the Court appeared divided:

- **Justices sympathetic to Pitchford:** Justice Brett Kavanaugh noted the federal district judge who initially ruled in Pitchford's favor was "a very experienced district judge" and former Mississippi Supreme Court justice. Justice Ketanji Brown Jackson suggested the case could be resolved with a "very short opinion" stating the state court's waiver finding was unreasonable. Justice Neil Gorsuch inquired about procedural steps following a potential reversal [https://www.scotusblog.com/2026/04/court-appears-sympathetic-to-death-row-inmates-attempt-to-challenge-racial-discrimination-in-jury-selection/](https://www.scotusblog.com/2026/04/court-appears-sympathetic-to-death-row-inmates-attempt-to-challenge-racial-discrimination-in-jury-selection/).

- **Skeptical questioning:** Justice Samuel Alito was sharply critical of Pitchford's trial counsel, describing her as "the most timid and reticent defense counsel that I have encountered" and arguing a competent attorney would have spoken up regarding the Batson challenge. Justice Clarence Thomas questioned whether defense counsel had adequately offered evidence or arguments to show the prosecutor's race-neutral explanations were pretextual [https://www.scotusblog.com/2026/04/court-appears-sympathetic-to-death-row-inmates-attempt-to-challenge-racial-discrimination-in-jury-selection/](https://www.scotusblog.com/2026/04/court-appears-sympathetic-to-death-row-inmates-attempt-to-challenge-racial-discrimination-in-jury-selection/).

The case was argued on March 31, 2026 (ET), and an opinion is expected before the end of the current Supreme Court term in late June or early July 2026. As of May 12, 2026 (UTC), no opinion has been published.

**Exact later resolution packet**

The question asks whether the U.S. Supreme Court's opinion in Pitchford v. Cain (No. 24-7351) was unanimous on the judgment (no dissenting votes on the judgment). It resolves NO because the decision was 5-4 with a dissent from the judgment.

Key facts, verified against the official source specified in the resolution criteria:
- The official slip opinion (docket No. 24-7351) was published on the Supreme Court's slip opinions page (https://www.supremecourt.gov/opinions/slipopinion/25) and is available at https://www.supremecourt.gov/opinions/25pdf/24-7351_jiel.pdf. It was decided on May 28, 2026, which is on/after the May 12, 2026 (UTC) threshold and before the July 1, 2026 (UTC) postponement deadline, so the question is resolvable [3f3fe2, 416145].
- Disposition: The Court reversed the judgment of the U.S. Court of Appeals for the Fifth Circuit and remanded for further proceedings ("We reverse the judgment of the U. S. Court of Appeals for the Fifth Circuit and remand the case for further proceedings consistent with this opinion.") [416145].
- The opinion of the Court was delivered by Justice Kavanaugh, joined by Chief Justice Roberts and Justices Sotomayor, Kagan, and Jackson (a 5-4 majority) [416145, 14b6e2].
- Justice Gorsuch filed a DISSENTING opinion, joined by Justices Thomas, Alito, and Barrett ("GORSUCH, J., filed a dissenting opinion, in which THOMAS, ALITO, and BARRETT, JJ., joined."), closing with "Respectfully, I dissent." This is a dissent from the judgment, not a mere concurrence in the judgment [416145, 14b6e2].

Because four Justices dissented from the judgment (the disposition), the opinion was NOT unanimous on the judgment. Per the resolution criteria ("The question resolves No if at least one Justice dissents from the judgment"), the question resolves NO (0).

Correct case verification: docket No. 24-7351, Terry Pitchford v. Burl Cain, a capital/Batson AEDPA case, matching the question exactly [3f3fe2].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-52. `65d90cc2-580b-52af-ba99-9f7564c3cb9d`

- Present date: `2026-04-29 22:02:25.757732`
- Source cutoff boundary: `2026-04-30` (encodes end of UTC day `2026-04-29`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the FDA's Oncologic Drugs Advisory Committee (ODAC) vote favorably on camizestrant by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, at the April 30, 2026 (Eastern Time / UTC-4) meeting of the FDA's Oncologic Drugs Advisory Committee (ODAC), a majority of voting committee members vote "Yes" on the primary efficacy/benefit-risk question posed regarding NDA 220359 (camizestrant tablets, AstraZeneca). It resolves **No** if a majority votes "No," or if the votes are tied (i.e., an equal number of Yes and No votes counts as not favorable). Abstentions are excluded from the count.

Only events occurring on or after the question's open date and on or before June 1, 2026, 23:59 UTC count toward resolution. If the ODAC meeting scheduled for April 30, 2026 is postponed to a date after June 1, 2026, or canceled entirely, the question resolves **No**.

**Resolution source:** The official vote tally as published on the [FDA's 2026 ODAC meeting materials page](https://www.fda.gov/advisory-committees/oncologic-drugs-advisory-committee/2026-meeting-materials-oncologic-drugs-advisory-committee), or, if not yet posted, as reported by at least two credible news sources (e.g., [Reuters](https://www.reuters.com), [STAT News](https://www.statnews.com), [FierceBiotech](https://www.fiercebiotech.com)).

**Key definitions:**
- **[Camizestrant](https://en.wikipedia.org/wiki/Camizestrant):** An investigational oral selective estrogen receptor degrader (SERD) developed by AstraZeneca (NDA 220359).
- **[ODAC](https://www.fda.gov/about-fda/cder-offices-and-divisions/oncologic-drugs-advisory-committee):** The FDA's Oncologic Drugs Advisory Committee, a panel of outside experts that provides recommendations to the FDA on oncology drug applications.
- **Favorable vote / majority yes:** Strictly more than 50% of non-abstaining voting members vote "Yes" on the primary benefit-risk question. A tie (equal Yes and No) is **not** favorable and resolves No.

**Pre-cutoff background**

On April 30, 2026, the FDA's [Oncologic Drugs Advisory Committee (ODAC)](https://www.fda.gov/about-fda/cder-offices-and-divisions/oncologic-drugs-advisory-committee) is scheduled to convene from 8:00 a.m. to 5:00 p.m. Eastern Time (12:00–21:00 UTC) to discuss new drug application (NDA) 220359 for [camizestrant](https://en.wikipedia.org/wiki/Camizestrant) tablets, submitted by AstraZeneca. Camizestrant is an investigational, potent, next-generation oral selective estrogen receptor degrader (SERD) being reviewed for use in combination with a CDK4/6 inhibitor for estrogen receptor-positive (ER+), HER2-negative, ESR1-mutated advanced or metastatic breast cancer upon emergence of ESR1 mutation during first-line endocrine-based therapy.

As of April 28, 2026 (UTC), camizestrant has not yet been approved by the FDA. The April 30 ODAC meeting is the FDA's first cancer advisory committee meeting in approximately nine months. ODAC advisory votes are non-binding but strongly influence FDA decisions. Historically, ODAC votes in favor of approval occur roughly 70–80% of the time, but outcomes vary considerably depending on trial data strength and safety concerns. Polymarket traders have implied an approximately 26% probability of FDA approval as of late April 2026, suggesting significant uncertainty about the ODAC outcome. The PDUFA date for camizestrant is expected in H1 2026.

Meeting materials and vote results are expected to be posted on the FDA's [2026 ODAC meeting materials page](https://www.fda.gov/advisory-committees/oncologic-drugs-advisory-committee/2026-meeting-materials-oncologic-drugs-advisory-committee).

**Exact later resolution packet**

The question asks whether ODAC voted FAVORABLY on camizestrant (NDA 220359, AstraZeneca) at the April 30, 2026 meeting, resolving YES only if a majority of non-abstaining voting members voted "Yes" on the primary efficacy/benefit-risk question.

The meeting occurred as scheduled on April 30, 2026 (not postponed or canceled), so the antecedent/timing condition is satisfied (well before the June 1, 2026 deadline).

The FDA ODAC voted 6 to 3 that, based on the SERENA-6 trial, a clinically meaningful benefit for camizestrant had NOT been demonstrated for the treatment of HR+/HER2-, ESR1-mutated advanced/metastatic breast cancer. This means 6 members voted unfavorably and only 3 favorably on the primary benefit-risk question [FDA panel rejects AstraZeneca's novel oral SERD proposal](https://www.fiercebiotech.com/biotech/astrazeneca-camizestrant-ambitions-stumble-fda-panel-rejects-novel-oral-serd-proposal). AstraZeneca's own press release confirmed the ODAC "did not reach a majority vote in favor of the benefit-risk profile" of camizestrant.

Because a majority (6) of non-abstaining voting members voted against (only 3 in favor), this is an unfavorable vote. The question therefore resolves NO (0).

Sources confirming the 6-3 unfavorable vote:
- FierceBiotech: https://www.fiercebiotech.com/biotech/astrazeneca-camizestrant-ambitions-stumble-fda-panel-rejects-novel-oral-serd-proposal [FDA panel rejects AstraZeneca's novel oral SERD proposal](https://www.fiercebiotech.com/biotech/astrazeneca-camizestrant-ambitions-stumble-fda-panel-rejects-novel-oral-serd-proposal)
- AstraZeneca press release: https://www.astrazeneca.com/media-centre/press-releases/2026/fda-odac-vote-on-camizestrant-breast-cancer.html ("did not reach a majority vote in favor")
- OncLive: https://www.onclive.com/view/fda-odac-votes-against-clinical-benefit-of-switching-to-camizestrant-in-hr-breast-cancer-after-esr1-mutation-detection (6-3 against)
- TargetedOnc: https://www.targetedonc.com/view/fda-s-odac-votes-against-camizestrant-in-advanced-breast-cancer (6-3 against)
- Friends of Cancer Research: 6-3 that SERENA-6 did not demonstrate clinically meaningful benefit
- FDA meeting materials: https://www.fda.gov/media/192153/download (voting question on clinically meaningful benefit)

Note: AstraZeneca had a separate favorable 7-1 vote for capivasertib (Truqap) at the same meeting, but that is a different drug and irrelevant to this question.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-53. `e23284c0-a657-577f-b328-7688a4144291`

- Present date: `2026-05-29 05:11:57.892751`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Israeli Knesset pass the 'West Bank Heritage Authority' bill into law by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 12, 2026, and no later than July 1, 2026 (23:59 UTC), the bill known as the "Judea and Samaria Heritage Authority" or "West Bank Antiquities Authority" (or any bill substantially similar in purpose—i.e., establishing a civilian statutory body under Israeli law with jurisdiction over heritage, antiquities, or archaeological sites in the West Bank) passes its **third reading** in the Knesset plenum.

For avoidance of doubt:
- **"Pass legislation"** means the bill completes its third and final reading in the Knesset plenum, as described in the [Knesset legislative process](https://main.knesset.gov.il/en/activity/pages/basiclaws/legislativeprocess.aspx). Alternatively, publication in the Official Gazette (*Reshumot*) shall also constitute conclusive evidence of passage.
- **"Equivalent civilian governance body"** means any statutory body established by Knesset legislation (not military order or coalition agreement) that (a) operates under an Israeli government ministry, (b) has jurisdiction over heritage, antiquities, or archaeological sites in the West Bank, and (c) replaces or supplements functions previously performed by the military Civil Administration's Antiquities Officer.

**Primary resolution source:** The [official Knesset legislative database](https://main.knesset.gov.il/en/activity/pages/default.aspx) and/or the [Official Gazette (Reshumot)](https://www.nevo.co.il/Law/Reshumot). Credible reporting from sources such as the Times of Israel, Haaretz, or Reuters may be used as supplementary confirmation.

The question resolves **No** if the bill does not pass its third reading by 23:59 UTC on July 1, 2026, regardless of the reason (withdrawal, rejection, delays, etc.).

**Pre-cutoff background**

The Israeli [Knesset](https://en.wikipedia.org/wiki/Knesset) has been advancing legislation to establish a civilian heritage and antiquities authority with jurisdiction over the [West Bank](https://en.wikipedia.org/wiki/West_Bank) (referred to in the bill as "Judea and Samaria"). The bill, submitted by Likud MK Amit Halevi, proposes transferring powers currently held by the military Civil Administration's "Antiquities Officer" to a new statutory body under the Israeli Minister of Heritage. This new authority would have broad powers including land seizure and management of archaeological excavations in Areas B and C of the West Bank [Establishment of the West Bank Heritage Authority](https://peacenow.org.il/en/the-first-annexation-bill-in-the-knesset-establishment-of-the-west-bank-heritage-authority).

Peace Now has characterized this as "the first annexation bill in the Knesset," noting it would move governance from military to civilian administration—a key marker of de facto annexation [Establishment of the West Bank Heritage Authority](https://peacenow.org.il/en/the-first-annexation-bill-in-the-knesset-establishment-of-the-west-bank-heritage-authority). The Chatham House analysis from April 2026 identified this bill as part of Israel's accelerating de facto annexation of the West Bank [https://www.chathamhouse.org/2026/04/israels-accelerating-de-facto-annexation-west-bank-has-dangerous-implications](https://www.chathamhouse.org/2026/04/israels-accelerating-de-facto-annexation-west-bank-has-dangerous-implications).

**Current legislative status as of May 13, 2026:** On May 12, 2026, the Knesset plenum approved the bill in its **first reading** by a vote of 23–14 [Knesset approves in first reading a bill to establish an “Antiquities ...](https://yaffaps.com/en/page-101699.html). The bill has now been referred to the Education, Culture and Sports Committee for preparation ahead of its second and third readings [Knesset approves in first reading a bill to establish an “Antiquities ...](https://yaffaps.com/en/page-101699.html). Under the Knesset's [legislative process](https://main.knesset.gov.il/en/activity/pages/basiclaws/legislativeprocess.aspx), a bill must pass a committee stage and then second and third readings in the plenum before becoming law.

**Exact later resolution packet**

The question resolves NO. The "Judea and Samaria Heritage Authority" bill (also called the West Bank antiquities bill) did NOT pass its third (final) reading in the Knesset plenum by July 1, 2026 (23:59 UTC).

Timeline of evidence:

1. First reading only: The official Knesset press release confirms the "Judea and Samaria Heritage Authority Bill, 2026" (sponsored by MK Amit Halevi, Likud) was approved in its FIRST reading by the Knesset plenum on May 12, 2026, and was then referred to the Education, Culture and Sports Committee to prepare it for second and third readings. There is no record of it passing a second or third reading [Bill to establish heritage authority for dealing with antiquities and ...](https://m.knesset.gov.il/en/news/pressreleases/pages/press12526q.aspx).

2. Progress halted before completing committee stage: On June 2–3, 2026, Prime Minister Netanyahu halted the bill's advancement. The Times of Israel (published June 2, 2026) reported that the scheduled committee meeting to vote on amendments — a necessary step before the second and third readings — was canceled, with no new meeting scheduled [Netanyahu said to halt progress of controversial West Bank and ...](https://www.timesofisrael.com/netanyahu-said-to-halt-progress-of-controversial-west-bank-and-gaza-antiquities-bill/). Emek Shaveh (published June 3, 2026) confirmed the bill (then titled "Judea, Samaria and Gaza Strip Heritage Authority Law, 2026") was frozen following Netanyahu's intervention and was considered unlikely to advance to a final vote during the current Knesset's term [Update: Advancement of Heritage Authority Bill Halted - Emek Shaveh](https://emekshaveh.org/en/heritage-authority-halted/).

3. Knesset heading toward dissolution: The Knesset was simultaneously moving to dissolve itself and call early elections. A dissolution bill passed its preliminary reading (110-0) on May 20, 2026, was approved by the House Committee on June 1, and passed first reading (106 votes) on June 2, 2026; as of late June 2026 the dissolution process was still ongoing with elections targeted for around September–October 2026 [2026 Israeli legislative election - Wikipedia](https://en.wikipedia.org/wiki/2026_Israeli_legislative_election) [MKs advance bill to dissolve Knesset and potentially move up ...](https://www.timesofisrael.com/mks-advance-bill-to-dissolve-knesset-and-potentially-move-up-elections-to-september/). An earlier Times of Israel report (May 19, 2026) had already noted that completing dissolution would halt permanent legislation until after elections [Knesset panel fast-tracks West Bank antiquities bill seen as de facto ...](https://www.timesofisrael.com/knesset-panel-fast-tracks-west-bank-antiquities-bill-seen-as-de-facto-annexation/).

4. No revival before the deadline: As of June 28, 2026, Haaretz reported the Netanyahu coalition's final pre-election legislative push was focused on ultra-Orthodox (Haredi) bills and judicial overhaul measures — the heritage/antiquities bill was not among the bills being advanced [Netanyahu Coalition Makes Last-ditch Push for pro-Haredi, Anti ...](https://www.haaretz.com/israel-news/elections/2026-06-28/ty-article/.premium/netanyahu-coalition-focuses-on-judicial-overhaul-pro-ultra-orthodox-bills/0000019f-0ce1-dfe2-a79f-6df946160000).

No credible source indicates the bill, or any substantially similar bill establishing a civilian statutory body over West Bank heritage/antiquities, completed its third reading or was published in the Official Gazette (Reshumot) on or before July 1, 2026. Because the resolution criteria require passage of the third reading by 23:59 UTC on July 1, 2026, and the bill was stalled at the post-first-reading committee stage (indeed frozen), the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-54. `57c0c232-5b78-5082-b328-250321931b18`

- Present date: `2026-05-12 17:48:03.156439`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the US impose a tariff rate of 25% or higher on EU-origin automobiles before July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 10, 2026 (00:00 UTC) and before July 1, 2026 (23:59 UTC), the United States government officially imposes a tariff rate of 25% or higher on EU-origin automobiles (as defined above). "Impose" means any of the following occurs:

1. The President signs an Executive Order or Presidential Proclamation setting the tariff at 25% or higher on EU-origin automobiles; OR
2. A notice is published in the [Federal Register](https://www.federalregister.gov/documents/search?conditions%5Bagencies%5D%5B%5D=executive-office-of-the-president&conditions%5Bterm%5D=tariff+automobile+european+union) establishing such a rate; OR
3. The [Office of the U.S. Trade Representative](https://ustr.gov/) officially announces the tariff is in effect.

If the tariff is announced but explicitly scheduled to take effect only after July 1, 2026, the question still resolves **Yes** — the key criterion is the official act of imposition (signing/publication), not the collection date. If no such official action occurs by July 1, 2026 (23:59 UTC), the question resolves **No**.

**Resolution sources:** [Federal Register search for tariff actions](https://www.federalregister.gov/documents/search?conditions%5Bagencies%5D%5B%5D=executive-office-of-the-president), [USTR press releases](https://ustr.gov/about-us/policy-offices/press-office/press-releases), or credible major news outlets (Reuters, AP, Bloomberg, NYT).

**Pre-cutoff background**

As of May 11, 2026, the United States imposes a 15% tariff on automobiles imported from the European Union, a rate established under a trade agreement reached in August 2025 [Trump Backs Off On E.U. Auto Tariffs But Risks Remain For Buyers ...](https://www.forbes.com/sites/kenroberts/2026/05/09/trump-backs-off-on-eu-auto-tariffs-but-risks-remain-for-buyers-ports/) [US to move forward with plans to hike EU car tariffs - Reuters](https://www.reuters.com/world/europe/us-move-forward-with-plans-hike-eu-car-tariffs-2026-05-04/). On May 1, 2026, President Trump announced plans to raise tariffs on EU-origin automobiles to 25%, accusing the EU of non-compliance with the prior deal [US to move forward with plans to hike EU car tariffs - Reuters](https://www.reuters.com/world/europe/us-move-forward-with-plans-hike-eu-car-tariffs-2026-05-04/). On May 4, 2026, U.S. Trade Representative Jamieson Greer confirmed the administration intended to proceed with this increase [US to move forward with plans to hike EU car tariffs - Reuters](https://www.reuters.com/world/europe/us-move-forward-with-plans-hike-eu-car-tariffs-2026-05-04/). However, as of May 9, 2026, reports indicate Trump appeared to back off from the immediate imposition of the 25% tariff, though risks remain [Trump Backs Off On E.U. Auto Tariffs But Risks Remain For Buyers ...](https://www.forbes.com/sites/kenroberts/2026/05/09/trump-backs-off-on-eu-auto-tariffs-but-risks-remain-for-buyers-ports/).

**Key definitions:**
- **"EU-origin automobiles"**: Passenger vehicles (cars and light trucks) manufactured in a European Union member state, as classified under Harmonized Tariff Schedule (HTS) headings 8703 (motor cars) and 8704 (motor vehicles for transport of goods). See the [US International Trade Commission HTS reference](https://hts.usitc.gov/current) for full classification details.
- **"Tariffs"**: Customs duties imposed by the US government on imported goods, as authorized under trade law. See [CBP tariff information](https://www.cbp.gov/trade/basic-import-export/duty-rates).
- **"Impose"**: Defined as either (a) the signing of an Executive Order or Presidential Proclamation that sets the tariff rate at 25% or higher, or (b) the publication of a notice in the [Federal Register](https://www.federalregister.gov/) establishing such a rate, or (c) an official announcement by the [Office of the U.S. Trade Representative (USTR)](https://ustr.gov/) confirming the tariff is in effect. Any of these constitutes "imposition" regardless of whether the effective date of collection has yet arrived.

The current 15% rate represents a reduction from a prior 27.5% rate under the 2025 deal [Trump Backs Off On E.U. Auto Tariffs But Risks Remain For Buyers ...](https://www.forbes.com/sites/kenroberts/2026/05/09/trump-backs-off-on-eu-auto-tariffs-but-risks-remain-for-buyers-ports/). Trump has repeatedly used tariff threats as negotiating leverage in trade disputes with the EU.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question asks whether the US officially imposed a tariff of 25% or higher on EU-origin automobiles (HTS 8703/8704) via an Executive Order/Proclamation, Federal Register notice, or USTR "in effect" announcement between May 10, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC). The evidence shows this did NOT happen; instead the 25% hike was averted and the 15% rate under the US-EU (Turnberry) deal was maintained.

Key timeline established from research:
- The 25% figure was only an ANNOUNCEMENT OF INTENT made on/around May 1, 2026 (before the resolution window opened on May 10) — Trump threatened to raise the rate "next week" (Reuters: reuters.com/business/autos-transportation/trump-says-he-will-raise-tariffs-eu-autos-25-2026-05-01/; BBC; Politico; Guardian May 1). Under the resolution criteria, an announcement of intent is explicitly distinct from the formal act of imposition, and this pre-dated the window anyway.
- On May 7, 2026, Trump gave the EU until July 4, 2026 to cut tariffs before the auto duty hike would "kick in" (Inside U.S. Trade: insidetrade.com/daily-news/trump-gives-eu-until-july-4-cut-tariffs-auto-duty-hike-kicks). This set a deadline, not an imposition, and the deadline (July 4) fell after the window close.
- On May 20, 2026, the EU was reported on track to meet Trump's July 4 deadline, with a vote expected in mid-June (CNBC: cnbc.com/2026/05/20/eu-us-trade-deal-trump-autos.html).
- On June 16-17, 2026, the European Parliament approved the Turnberry agreement, explicitly "averting 25% tariffs on EU car imports" (WSJ: wsj.com/economy/trade/eu-gives-final-approval-to-u-s-trade-deal-5b1aa450; Guardian June 16; Le Monde June 17).
- On June 30, 2026, the EU moved to implement the trade deal, keeping levies at 15% on most EU exports (RTE: rte.ie/news/business/2026/0630/1581078-eu-to-implement-trade-deal-with-us-from-tomorrow/).

Because the EU complied before the July 4 deadline, the threatened 25% auto tariff was never formally imposed. No Executive Order/Proclamation, Federal Register notice, or USTR "in effect" announcement establishing a 25%+ rate on EU-origin autos occurred within the May 10 – July 1, 2026 window. The operative rate remained 15%. Therefore the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-55. `21a7b760-054c-591b-ac3d-de8a57d53dc1`

- Present date: `2026-05-01 13:07:41.975018`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a new National Defense Area (NDA) be established along the U.S.-Mexico border between April 30, 2026 and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after April 30, 2026 (00:00 UTC) and before June 1, 2026 (23:59 UTC), the U.S. Department of Defense or another official federal entity (e.g., a military branch, U.S. Northern Command, or the Department of the Interior) formally announces the establishment of at least one **new** National Defense Area along the U.S.-Mexico border.

A "[National Defense Area](https://en.wikipedia.org/wiki/National_Defense_Area)" (NDA) is an area of land designated under federal authority (specifically [50 U.S.C. § 797](https://www.law.cornell.edu/uscode/text/50/797)) as a military installation for border security purposes, as described in National Security Presidential Memorandum-4.

**"New" NDA** means a geographically distinct NDA that is designated with a separate name or number from the six NDAs that exist as of April 30, 2026. An expansion of an existing NDA's geographic boundaries (e.g., adding miles to NDA 3) does **not** count as a new NDA unless it is designated as a separately named or numbered entity [National Defense Area - Wikipedia](https://en.wikipedia.org/wiki/National_Defense_Area).

**"Established"** means the announcement of the NDA's designation via an official Department of Defense or military branch press release, a Federal Register notice, or credible reporting (e.g., AP, Reuters, Defense One, Stars and Stripes) confirming the formal designation.

**Resolution sources:**
- [Department of the Air Force News](https://www.af.mil/News/)
- [Department of Defense News](https://www.defense.gov/News/)
- [Federal Register](https://www.federalregister.gov/)
- Credible news outlets such as AP, Reuters, Defense One, or Stars and Stripes

If no new NDA is established by 23:59 UTC on June 1, 2026, this question resolves **No**.

**Pre-cutoff background**

Since April 2025, the Trump administration has established multiple National Defense Areas (NDAs) along the U.S.-Mexico border under National Security Presidential Memorandum-4 (NSPM-4), authorized by [50 U.S.C. § 797](https://www.law.cornell.edu/uscode/text/50/797) and [18 U.S.C. § 1382](https://www.law.cornell.edu/uscode/text/18/1382) [National Defense Area - Wikipedia](https://en.wikipedia.org/wiki/National_Defense_Area). NDAs are designated areas of federal land placed under military control where troops can search, detain, and arrest individuals for trespassing on a military installation.

As of March 2026, six NDAs have been established across all four U.S.-Mexico border states (Texas, New Mexico, Arizona, and California), covering more than 800 miles — approximately 42% of the U.S.-Mexico border [A war zone, minus the war: Has the military really secured the border?](https://timesofsandiego.com/military/2026/03/29/war-zone-military-mexico-border/). These include NDAs administered by Fort Bliss, Fort Huachuca, Joint Base San Antonio, and Marine Corps Air Station Yuma [National Defense Area - Wikipedia](https://en.wikipedia.org/wiki/National_Defense_Area). The pace of NDA establishment has been rapid, with the most recent expansions announced in February 2026 [National Defense Areas expanded, established along Texas border](https://www.af.mil/News/Article-Display/Article/4399639/national-defense-areas-expanded-established-along-texas-border/). However, the expansion faces potential headwinds: federal judges have dismissed trespassing cases in NDAs, and legal challenges from the ACLU and others are ongoing [A war zone, minus the war: Has the military really secured the border?](https://timesofsandiego.com/military/2026/03/29/war-zone-military-mexico-border/). With over 40% of the border already covered, the rate of new designations may slow, though significant uncovered stretches remain.

For more on NDAs, see: [National Defense Area - Wikipedia](https://en.wikipedia.org/wiki/National_Defense_Area).

**Exact later resolution packet**

The question resolves NO because no new, separately named or numbered National Defense Area (NDA) along the U.S.-Mexico border was formally announced between April 30, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC).

Background — the six NDAs existing as of April 30, 2026 were all established before the resolution window:
- New Mexico NDA (Fort Huachuca) — designated April 18, 2025.
- Texas/El Paso NDA (Fort Bliss) — established May 1, 2025.
- NDA 3 (Joint Base San Antonio) — June 2025.
- NDA 4 (Marine Corps Air Station Yuma) — July 2025.
- NDA 5 (Naval Air Facility El Centro, California) — reported January 2026 [9ba7fe].
- NDA 6 (Del Rio-Falcon, Joint Base San Antonio) — announced February 2026.
The Wikipedia article (last edited April 17, 2026) confirms these six NDAs and contains no record of any new NDA in May/June 2026 [d63673, 65e0bf].

Evidence that no NEW NDA was established in the window:
- U.S. Northern Command's official Southern Border press-release tag page and Border Security page show no NDA establishment announcements between April 30 and June 1, 2026; the most recent border milestone listed is the Joint Task Force–Southern Border one-year anniversary on March 14, 2026 [4c94e0, 89fd91]. The NORTHCOM Border Security page lists Del Rio-Falcon as the only "upcoming" NDA, not a newly established one in the window.
- Adam Isacson's detailed "U.S.-Mexico Border Update: May 29, 2026" (covering the relevant period) reports a $1.7 billion border-barrier construction contract (May 11, 2026) but no designation of any new NDA; it only references existing NDAs [ca8b23].
- All credible reporting (Defense One, Stars and Stripes, AP) on NDA expansions dates to February 2026 or earlier; the February 2026 actions were the expansion of NDA 3 to Roma (an expansion, which explicitly does not count) and the establishment of NDA 6 (Del Rio-Falcon), both before the window.

No official Department of Defense/War, military branch, Federal Register, or credible news source (AP, Reuters, Defense One, Stars and Stripes) announced a geographically distinct, separately named/numbered new NDA during April 30–June 1, 2026. Therefore the question resolves NO.

Sources:
- https://en.wikipedia.org/wiki/National_Defense_Area
- https://www.northcom.mil/Newsroom/Press-Releases/Tag/72083/southern-border/
- https://www.northcom.mil/BorderSecurity/
- https://adamisacson.com/u-s-mexico-border-update-may-29-2026/
- https://www.ivpressonline.com/news/portions-of-imperial-valley-designated-national-defense-area-under-navy-authority/article_86f9d2df-f69d-42eb-8b9f-f4750552c18c.html

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-56. `3796f9d9-2c41-5876-914b-1a5fd94c5b98`

- Present date: `2026-05-15 20:03:06.971521`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will any major international election observation mission (OAS, EU, or Carter Center) publicly express "serious concerns" about the integrity of the June 7, 2026, Peruvian runoff election by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if at least one of the following three named international election observation missions publishes a statement, press release, preliminary report, or final report on or after May 12, 2026, and by 11:59 PM UTC on July 1, 2026, that meets the criteria below:

**Named observation missions (exhaustive list):**
1. Organization of American States (OAS) Electoral Observation Mission — official reports archive: https://www.oas.org/en/spa/deco/default.asp
2. European Union (EU) Election Observation Mission — official reports archive: https://www.eeas.europa.eu/eeas/eu-election-observation-missions-1_en
3. The Carter Center Election Observation Mission — official reports archive: https://www.cartercenter.org/programs/democracy/

**Definition of "serious concerns":** The qualifying publication must contain at least one of the following exact phrases (in English or Spanish) in reference to the June 7, 2026, Peruvian presidential runoff election:
- "serious concerns" / "serias preocupaciones"
- "grave concerns" / "graves preocupaciones"
- "deeply concerned" / "profundamente preocupado(s/a/as)"
- "serious doubts" / "serias dudas"
- "lack of integrity" / "falta de integridad"
- "not met international standards" / "no cumplió con los estándares internacionales"
- "fundamentally flawed" / "fundamentalmente defectuoso(a)"

The phrase must appear in an official document (statement, press release, preliminary or final report) published on the organization's official website or official social media channels. Opinion pieces, unofficial commentary, or statements by individual mission members acting in a personal capacity do not qualify.

If none of the three named organizations publishes a document meeting the above criteria by 11:59 PM UTC on July 1, 2026, this question resolves as **No**.

**Pre-cutoff background**

The first round of the 2026 Peruvian general election, held on April 12–13, 2026, was marred by significant irregularities. The National Office of Electoral Processes (ONPE) experienced major logistical failures in ballot delivery across Metropolitan Lima, with 211 polling stations in 15 voting locations (San Juan de Miraflores, Lurín, and Pachacamac) unable to open on election day, preventing over 63,000 citizens from voting and necessitating an extension of voting to April 13 [2026 Peruvian post-electoral crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Peruvian_post-electoral_crisis). Criminal investigations were initiated against ONPE officials, including electoral management director José Samamé Blas and ONPE head Piero Corvetto, for alleged dereliction of duty [2026 Peruvian post-electoral crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Peruvian_post-electoral_crisis). Far-right candidate Rafael López Aliaga alleged the failures constituted planned "electoral fraud," though these claims were dismissed by international observers, including the EU Election Observation Mission, which characterized the events as "serious irregularities" rather than evidence of fraud [2026 Peruvian post-electoral crisis - Wikipedia](https://en.wikipedia.org/wiki/2026_Peruvian_post-electoral_crisis).

The runoff election between Keiko Fujimori (Popular Force) and Roberto Sánchez (Together for Peru) is scheduled for June 7, 2026 [https://en.wikipedia.org/wiki/2026_Peruvian_general_election](https://en.wikipedia.org/wiki/2026_Peruvian_general_election). International observation missions present in the first round included the European Union, the Organization of American States (OAS), the Carter Center, the Association of World Election Bodies, and others [https://en.wikipedia.org/wiki/2026_Peruvian_general_election](https://en.wikipedia.org/wiki/2026_Peruvian_general_election). Peru's National Jury of Elections (JNE) has called for a comprehensive IT audit of first-round results, and political tensions remain high heading into the runoff.

Given the severity of first-round problems and ongoing institutional instability, there is genuine uncertainty about whether the runoff will proceed smoothly or whether international observers will again identify major integrity concerns.

Key resolution sources:
- OAS Electoral Observation Mission reports: https://www.oas.org/en/spa/deco/default.asp
- EU Election Observation Mission statements: https://www.eeas.europa.eu/eeas/eu-election-observation-missions-1_en
- Carter Center democracy program reports: https://www.cartercenter.org/programs/democracy/

**Exact later resolution packet**

RESOLUTION: NO (0).

ANTECEDENT CHECK (not a conditional annulment): The June 7, 2026 Peruvian presidential runoff between Keiko Fujimori and Roberto Sánchez did take place, and Fujimori was ultimately declared the narrow winner after weeks of counting (confirmed by multiple outlets, e.g., Le Monde/Guardian/DW coverage). So the event underlying the question occurred; this is a straightforward YES/NO, not an annulment.

TASK: Resolve YES only if OAS, EU, or Carter Center published, on/after May 12, 2026 and by 11:59 PM UTC July 1, 2026, an official statement/report containing one of seven specified exact phrases (English or Spanish) in reference to the June 7, 2026 runoff. I checked every qualifying official publication from all three missions in the window:

OAS Electoral Observation Mission:
- "Primer Informe" for the runoff (Segunda Elección Presidencial 2026), June 9, 2026: characterizes the runoff as held "de manera tranquila y en paz," "reconoce el esfuerzo realizado por los órganos del sistema electoral," and contains NONE of the trigger phrases [da3b5a].
- Mid-June statement (reported June 16/17, 2026) urging speed to resolve remaining contested ballots (<1% of actas): states the election "se ha desarrollado con normalidad" and that the mission "no ha identificado irregularidades que pongan en duda la integridad de la información"—the opposite of the trigger language; contains NONE of the phrases [27436a].
- E-061/26 (May 17, 2026) welcomed the official announcement of runoff candidates; no trigger phrases [bf4aa5].
- Earlier OAS items (E-051/26 April 24; preliminary report April 15) predate the window and concern the first round [7391de, dc14b9].

EU Election Observation Mission (MOE UE):
- Preliminary Statement of June 9, 2026 ("Competitive run-off..."): no trigger phrases [8a9e35].
- "EU observers rebuff unsubstantiated fraud discourse," June 26, 2026: states the mission "found no indications of intentional manipulation at any stage of the process" and calls to respect the outcome; no trigger phrases [1336ef].
- The April 14, 2026 preliminary statement concerns the first round only [e8508f].

Carter Center:
- June 9, 2026 runoff statements ("Carter Center Urges Respect for Process as Peru Determines Final Results in Close Presidential Runoff" / Spanish equivalent / "Declaración preliminar ... segunda vuelta"): urge respect for the process; no trigger phrases [a0e8f7].
- May 21, 2026 redeployment release: no trigger phrases [8172d1]. May 27, 2026 "What the Carter Center Observed": expresses hopes for a smoother runoff, no trigger phrases [84b9e5].

CONCLUSION: No official OAS/EU/Carter Center publication in the May 12 – July 1, 2026 window used any of the seven required exact phrases ("serious concerns"/"serias preocupaciones", "grave concerns"/"graves preocupaciones", "deeply concerned"/"profundamente preocupado", "serious doubts"/"serias dudas", "lack of integrity"/"falta de integridad", "not met international standards", "fundamentally flawed") in reference to the June 7 runoff. On the contrary, all three missions affirmatively described the runoff as competitive/normal and rebuffed fraud allegations. Therefore the question resolves NO.

Key URLs: OAS runoff report PDF https://www.oas.org/fpdb/press/2026_MOE_Peru_Segunda_Vuelta_Primer_Informe_ESP.pdf ; OAS mid-June (via DW) https://www.dw.com/es/oea-pide-celeridad-para-resolver-actas-electorales-en-per%C3%BA/a-77583327 ; EU runoff preliminary statement https://www.eeas.europa.eu/eom-peru-2026/preliminary-statement-eu-eom-peru-2026-0_en ; EU rebuff-fraud https://www.eeas.europa.eu/eom-peru-2026/eu-observers-rebuff-unsubstantiated-fraud-discours_en ; Carter Center Peru page https://www.cartercenter.org/country/peru/ .

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-57. `2dfcc2ba-7efd-5758-b094-1648ef5f6b65`

- Present date: `2026-05-03 10:39:22.699130`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will a Gulf sovereign wealth fund announce a new single US investment of $5 billion or more between May 2 and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, between May 2, 2026 at 00:00 UTC and June 1, 2026 at 23:59 UTC, any Gulf sovereign wealth fund publicly announces a new single investment in a US-based entity or project where the SWF's own capital commitment is $5 billion USD or more.

**Definitions:**

- **Gulf sovereign wealth fund:** Any sovereign wealth fund (as defined by the International Forum of Sovereign Wealth Funds, https://www.ifswf.org/) owned by a government of a Gulf Cooperation Council (GCC) member state (Bahrain, Kuwait, Oman, Qatar, Saudi Arabia, United Arab Emirates). This includes but is not limited to: Abu Dhabi Investment Authority (ADIA), Public Investment Fund (PIF), Qatar Investment Authority (QIA), Mubadala Investment Company, Kuwait Investment Authority (KIA), and Abu Dhabi Developmental Holding Company (ADQ). Wholly-owned subsidiaries of these funds also qualify.

- **US investment:** An investment in an entity whose headquarters or primary operations are located in the United States, or a project primarily located in the United States.

- **Single investment:** A specific, discrete transaction such as an acquisition, equity stake, joint venture, or project commitment. The $5 billion threshold refers to the SWF's own capital commitment in that single transaction, not the total deal value if co-invested with others. Multiple smaller investments that collectively exceed $5 billion do not qualify.

- **Announced:** The deal must be reported by at least two of the following credible news sources: Reuters (https://www.reuters.com), Bloomberg (https://www.bloomberg.com), Financial Times (https://www.ft.com), Wall Street Journal (https://www.wsj.com), or Associated Press (https://apnews.com). Official press releases from the SWF itself also qualify.

- Announcements made before May 2, 2026 at 00:00 UTC do not count, even if the deal closes during the resolution window.

If no qualifying announcement is made by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

In 2025, Gulf sovereign wealth funds (SWFs) dramatically increased their US exposure. The US accounted for 59% of all deals by the region's most active SWFs [Gulf investors still hunting for good deals in the US | AGBI](https://www.agbi.com/opinion/finance/2026/04/gulf-investors-still-hunting-for-good-deals-in-the-us/), and sovereign investors channeled over $130 billion into US projects ['Freaked people out': Iran war could crimp Gulf allies' US investments](https://www.politico.com/news/2026/03/26/immensely-destabilizing-iran-war-threatens-gulfs-us-investments-00845486). During President Trump's May 2025 Gulf tour, Gulf countries pledged over $3 trillion in total long-term US investment commitments, including a $600 billion Saudi commitment and a $1.4 trillion UAE framework [Gulf investors still hunting for good deals in the US | AGBI](https://www.agbi.com/opinion/finance/2026/04/gulf-investors-still-hunting-for-good-deals-in-the-us/).

However, as of early 2026, the geopolitical landscape has shifted. The US-Iran conflict has created significant uncertainty, with concerns that Gulf nations may need to redirect capital toward domestic priorities such as rebuilding energy infrastructure and missile defense systems ['Freaked people out': Iran war could crimp Gulf allies' US investments](https://www.politico.com/news/2026/03/26/immensely-destabilizing-iran-war-threatens-gulfs-us-investments-00845486). Some analysts have warned that the "Middle East is essentially closed" for new large-scale capital deployment in the near term ['Freaked people out': Iran war could crimp Gulf allies' US investments](https://www.politico.com/news/2026/03/26/immensely-destabilizing-iran-war-threatens-gulfs-us-investments-00845486). Despite these headwinds, Gulf SWFs have continued some deal activity—for example, committing $24 billion to the Paramount-Warner Bros deal in early 2026 [Gulf investors still hunting for good deals in the US | AGBI](https://www.agbi.com/opinion/finance/2026/04/gulf-investors-still-hunting-for-good-deals-in-the-us/). Gulf SWFs deployed approximately $25 billion in Q1 2026 globally.

The key question is whether the combination of geopolitical uncertainty from the Iran conflict and potential economic disruption will prevent a major single-deal announcement in May 2026, or whether the underlying momentum and political incentives to invest in the US will produce at least one large transaction.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if, between May 2 and June 1, 2026, a Gulf SWF publicly announced a NEW SINGLE US investment where the SWF's OWN capital commitment (excluding co-investors) was $5 billion or more, reported by ≥2 of {Reuters, Bloomberg, FT, WSJ, AP} or an official SWF press release. I examined every leading candidate and none satisfies all criteria:

1) ANTHROPIC SERIES H ($65bn total, announced May 28, 2026): Reported widely (Reuters, WSJ). QIA "doubled down" and MGX (Abu Dhabi) participated. However, the total $65bn round was split among ~28 investors (Altimeter, Dragoneer, Greenoaks, Sequoia, GIC, ICONIQ, Temasek, MGX, etc.). No source — including the Anthropic press release [Anthropic raises $65B in Series H funding at $965B post-money ...](https://www.anthropic.com/news/series-h), the Reuters article [Anthropic's valuation surges to $965 billion, surpassing OpenAI](https://www.reuters.com/business/anthropic-raises-65-billion-now-valued-965-billion-2026-05-28/), or the Zawya QIA article [Qatar's QIA doubles down on Anthropic in $65bln funding round](https://www.zawya.com/en/business/swf/qatars-qia-doubles-down-on-anthropic-in-65bln-funding-round-wfxx8w1x) [Qatar's QIA doubles down on Anthropic in $65bln funding round](https://www.zawya.com/en/business/swf/qatars-qia-doubles-down-on-anthropic-in-65bln-funding-round-wfxx8w1x) — discloses any individual Gulf SWF's commitment, let alone confirms a single Gulf SWF commitment of $5bn+. The resolution criteria explicitly state the $5bn threshold "refers to the SWF's own capital commitment in that single transaction, not the total deal value if co-invested with others." The only single $5bn figure broken out in the round belonged to Amazon (not a Gulf SWF) [Anthropic's valuation surges to $965 billion, surpassing OpenAI](https://www.reuters.com/business/anthropic-raises-65-billion-now-valued-965-billion-2026-05-28/). Thus the Anthropic round does not qualify.

2) PIF / SPACEX IPO ANCHOR ($5bn): Only ever reported as "in talks"/"discussions" (Reuters Apr 2, 2026 exclusive; NY Post; etc.) — never a confirmed, announced investment. The SpaceX IPO pricing/listing was targeted for ~June 11–12, 2026, AFTER the June 1 window close. No confirmed PIF anchor commitment was announced within May 2–June 1, 2026.

3) PARAMOUNT–WARNER BROS ($24bn from three Gulf funds): Announced April 6–7, 2026 (WSJ, NYT, Variety, FT), BEFORE the May 2 window. Explicitly excluded ("Announcements made before May 2, 2026 do not count"). It was also a split among three funds, not a single SWF's $5bn+ commitment newly announced in-window.

4) OTHER IN-WINDOW GULF SWF DEALS (per Global SWF news feed [Latest News - Global SWF](https://globalswf.com/news?fund_id=MUBAD&view=list)): Mubadala $325m in UK Hornsea 3 (May 12/13 — UK, not US, far below $5bn); L'IMAD/ADQ/ADNOC + BlackRock GIP infrastructure platform (May 15 — GCC/Central Asia, not US); Mubadala $3bn GlobalFoundries (May 28 — an exit/realisation, not a new investment). None qualifies.

No qualifying announcement of a single Gulf SWF US investment with the fund's own commitment ≥$5bn was made within the window and confirmed by the required sources. Therefore the question resolves NO.

Sources: Anthropic press release https://www.anthropic.com/news/series-h [Anthropic raises $65B in Series H funding at $965B post-money ...](https://www.anthropic.com/news/series-h); Reuters Anthropic https://www.reuters.com/business/anthropic-raises-65-billion-now-valued-965-billion-2026-05-28/ [Anthropic's valuation surges to $965 billion, surpassing OpenAI](https://www.reuters.com/business/anthropic-raises-65-billion-now-valued-965-billion-2026-05-28/); Zawya QIA/Anthropic https://www.zawya.com/en/business/swf/qatars-qia-doubles-down-on-anthropic-in-65bln-funding-round-wfxx8w1x [Qatar's QIA doubles down on Anthropic in $65bln funding round](https://www.zawya.com/en/business/swf/qatars-qia-doubles-down-on-anthropic-in-65bln-funding-round-wfxx8w1x) [Qatar's QIA doubles down on Anthropic in $65bln funding round](https://www.zawya.com/en/business/swf/qatars-qia-doubles-down-on-anthropic-in-65bln-funding-round-wfxx8w1x); Global SWF Mubadala feed https://globalswf.com/news?fund_id=MUBAD&view=list [Latest News - Global SWF](https://globalswf.com/news?fund_id=MUBAD&view=list); Reuters SpaceX IPO timeline https://www.reuters.com/world/spacex-accelerates-ipo-timeline-targets-june-11-pricing-nasdaq-2026-05-15/ [Exclusive: SpaceX accelerates IPO timeline, targets June 12 listing ...](https://www.reuters.com/world/spacex-accelerates-ipo-timeline-targets-june-11-pricing-nasdaq-2026-05-15/).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-58. `f492e1f2-4794-5f65-8b43-8feae798c58c`

- Present date: `2026-05-02 12:14:46.690981`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-05-20 00:00:00`

**Question**

Will CBP report any releases of apprehended individuals into the U.S. interior for April 2026?

**Resolution criteria**

This question resolves **YES** if the official CBP Monthly Operational Update (published at https://www.cbp.gov/newsroom/national-media-release) or the CBP Custody and Transfer Statistics page (https://www.cbp.gov/newsroom/stats/custody-and-transfer-statistics) reports a non-zero number of USBP releases of individuals into the U.S. interior specifically for the month of April 2026, as published before June 1, 2026, 23:59 UTC.

This question resolves **NO** if the official CBP data for April 2026 reports zero releases into the U.S. interior, or if no official CBP data covering April 2026 is published before June 1, 2026, 23:59 UTC.

Key definitions:
- **"Releases"**: Instances where U.S. Border Patrol releases apprehended individuals into the U.S. interior, as tracked by CBP's [Custody and Transfer Statistics](https://www.cbp.gov/newsroom/stats/custody-and-transfer-statistics).
- **"Apprehended individuals"**: Persons taken into USBP custody between ports of entry, per [CBP enforcement statistics](https://www.cbp.gov/newsroom/stats/cbp-enforcement-statistics).
- **"Interior"**: Release into the United States beyond the immediate border enforcement zone, as distinct from detention, removal, or return under programs like Remain in Mexico.
- **Resolution source**: The CBP Monthly Operational Update press release covering April 2026 data, expected at https://www.cbp.gov/newsroom/national-media-release, or the Custody and Transfer Statistics page at https://www.cbp.gov/newsroom/stats/custody-and-transfer-statistics.

**Pre-cutoff background**

Since May 2025, U.S. Border Patrol (USBP) has reported zero releases of apprehended individuals into the interior of the United States. As of the most recent CBP monthly operational update published on April 9, 2026, covering March 2026 data, this "zero release" streak has lasted 11 consecutive months [Trump administration delivers 11 straight months of zero releases at ...](https://www.cbp.gov/newsroom/national-media-release/trump-administration-delivers-11-straight-months-zero-releases).

"Releases" in this context refers to instances where USBP allows apprehended individuals to enter the U.S. interior rather than detaining or removing them. CBP tracks these figures in its [Custody and Transfer Statistics](https://www.cbp.gov/newsroom/stats/custody-and-transfer-statistics) [Trump administration delivers 11 straight months of zero releases at ...](https://www.cbp.gov/newsroom/national-media-release/trump-administration-delivers-11-straight-months-zero-releases). "Apprehended individuals" refers to persons taken into custody by U.S. Border Patrol between ports of entry, as defined in [CBP's enforcement statistics](https://www.cbp.gov/newsroom/stats/cbp-enforcement-statistics) [Trump administration delivers 11 straight months of zero releases at ...](https://www.cbp.gov/newsroom/national-media-release/trump-administration-delivers-11-straight-months-zero-releases). "Interior" refers to release into the United States beyond the immediate border zone, as opposed to detention, removal, or return to Mexico.

A key development threatens this streak: on April 24, 2026, a federal appeals court ruled that President Trump's executive order suspending asylum access at the southern border is illegal, potentially requiring the administration to begin processing asylum seekers — which could result in releases into the interior. However, the administration may seek a stay from the Supreme Court or find procedural mechanisms to maintain zero releases for the remaining days of April.

CBP publishes monthly operational updates as press releases on its [newsroom page](https://www.cbp.gov/newsroom/national-media-release). The April 2026 data update is expected in early-to-mid May 2026, consistent with prior releases (e.g., March data was published April 9, 2026) [Trump administration delivers 11 straight months of zero releases at ...](https://www.cbp.gov/newsroom/national-media-release/trump-administration-delivers-11-straight-months-zero-releases).

**Exact later resolution packet**

NO. The official CBP data available before the June 1, 2026 23:59 UTC cutoff did not report a non-zero number of U.S. Border Patrol releases of apprehended individuals into the U.S. interior for April 2026. The CBP Custody and Transfer Statistics page at https://www.cbp.gov/newsroom/stats/custody-and-transfer-statistics was last modified on May 15, 2026, before the cutoff; for April 2026, its U.S. Border Patrol disposition data listed the interior-release categories “Notice to Appear/Own Recognizance (NTA-OR)” and “Paroles” as 0 [https://www.cbp.gov/newsroom/stats/custody-and-transfer-statistics](https://www.cbp.gov/newsroom/stats/custody-and-transfer-statistics). Although the same page had a “Provisional Releases” entry of 9, CBP’s footnote defined that as people manifested as turned over to other federal agencies such as ICE, HHS, or the U.S. Marshals, i.e. transfers rather than releases into the U.S. interior under the question’s definition [https://www.cbp.gov/newsroom/stats/custody-and-transfer-statistics](https://www.cbp.gov/newsroom/stats/custody-and-transfer-statistics). Separately, an official CBP national media release at https://www.cbp.gov/newsroom/national-media-release/us-border-patrol-marks-102-years-defending-america-s-borders, published May 28, 2026, stated that “in April, agents recorded their 12th consecutive month of zero releases into the interior of the United States,” specifically referring to Border Patrol agents and April data [U.S. Border Patrol marks 102 years of defending America's borders](https://www.cbp.gov/newsroom/national-media-release/us-border-patrol-marks-102-years-defending-america-s-borders). These sources distinguish USBP/Border Patrol releases from other outcomes such as transfers, detention, removal, or returns, and from non-USBP agency activity; therefore the criterion for YES—a non-zero number of USBP releases into the U.S. interior for April 2026—was not met [https://www.cbp.gov/newsroom/stats/custody-and-transfer-statistics](https://www.cbp.gov/newsroom/stats/custody-and-transfer-statistics) [U.S. Border Patrol marks 102 years of defending America's borders](https://www.cbp.gov/newsroom/national-media-release/us-border-patrol-marks-102-years-defending-america-s-borders).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-59. `d962da83-9133-5bc4-a947-19fdcdf96cb4`

- Present date: `2026-05-29 04:26:49.128868`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Brazilian Senate pass (approve) the critical minerals bill (PL 2780/2024) by July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the Brazilian Senate (Senado Federal) approves PL 2780/2024 in a plenary vote on or after May 12, 2026, and before 23:59 UTC on July 1, 2026.

Specifically:
- "Passing" means the bill receives a majority vote in favor in the Senate plenary session (plenário).
- If the Senate approves the bill **with amendments** that require it to return to the Chamber of Deputies for further consideration, this **still counts as Yes** — the question is about Senate passage, not final enactment into law.
- If the Senate rejects the bill, or if no plenary vote occurs by the deadline, the question resolves as **No**.

**Resolution source**: Official Brazilian Senate legislative tracking portal for PL 2780/2024: https://www25.senado.leg.br/web/atividade/materias/-/materia/174060

**Pre-cutoff background**

On May 6, 2026, the Brazilian Chamber of Deputies (Câmara dos Deputados) approved PL 2780/2024, which establishes the National Policy on Critical and Strategic Minerals (PNMCE) and creates the National Council for the Industrialization of Critical and Strategic Minerals (CIMCE) [Brazilian Lawmakers Approve $1 Billion Critical Minerals Bill ... - Folha](https://www1.folha.uol.com.br/internacional/en/business/2026/05/brazilian-lawmakers-approve-1-billion-critical-minerals-bill-with-veto-power-over-foreign-partnerships.shtml). The bill includes approximately R$5 billion (~$1 billion) in tax incentives and a guarantee fund to boost domestic critical minerals production, particularly rare earths.

As of May 13, 2026, the bill has been received by the Senate (tracked at https://www25.senado.leg.br/web/atividade/materias/-/materia/174060). Senate President Davi Alcolumbre has indicated the bill will be treated with priority [Critical minerals receive "big advice" and a tight game for approval ...](https://neofeed.com.br/poder/minerais-criticos-ganham-conselhao-e-jogo-amarrado-para-aprovacao-no-senado/en/). The government leader in the Senate has stated the goal is to vote on the bill in May 2026.

Key controversies that could delay or block Senate passage include:

1. **CIMCE veto power**: The bill grants CIMCE authority to oversee and effectively veto international partnerships and changes in corporate control (e.g., mergers and acquisitions) of companies holding critical mineral rights, if deemed a threat to Brazil's economic security. While the original "approval" requirement was softened to "ratification" during Chamber deliberations, mining companies and legal experts still view this as creating significant regulatory uncertainty [Brazilian Lawmakers Approve $1 Billion Critical Minerals Bill ... - Folha](https://www1.folha.uol.com.br/internacional/en/business/2026/05/brazilian-lawmakers-approve-1-billion-critical-minerals-bill-with-veto-power-over-foreign-partnerships.shtml) [Critical minerals receive "big advice" and a tight game for approval ...](https://neofeed.com.br/poder/minerais-criticos-ganham-conselhao-e-jogo-amarrado-para-aprovacao-no-senado/en/).

2. **Research authorization deadlines**: The bill imposes a 10-year expiration period for mineral research authorizations. The mining sector is actively lobbying for the removal of this provision, arguing it hinders long-term investment [Brazilian Lawmakers Approve $1 Billion Critical Minerals Bill ... - Folha](https://www1.folha.uol.com.br/internacional/en/business/2026/05/brazilian-lawmakers-approve-1-billion-critical-minerals-bill-with-veto-power-over-foreign-partnerships.shtml).

The bill has geopolitical significance as it is linked to potential U.S.-Brazil agreements on critical minerals supply chains, a topic expected in the Lula-Trump bilateral relationship [Critical minerals receive "big advice" and a tight game for approval ...](https://neofeed.com.br/poder/minerais-criticos-ganham-conselhao-e-jogo-amarrado-para-aprovacao-no-senado/en/). Opposition senators and industry lobbying could still block or significantly amend the bill.

**Exact later resolution packet**

RESOLUTION: NO (0).

The question resolves YES only if the Brazilian Senate (Senado Federal) approves PL 2780/2024 in a PLENARY (Plenário) vote on/after May 12, 2026 and before 23:59 UTC on July 1, 2026. No such plenary vote occurred by the deadline.

Evidence:

1) Official resolution source — Senate legislative tracking portal for PL 2780/2024 (https://www25.senado.leg.br/web/atividade/materias/-/materia/174060): the bill was received by the Senate on May 8, 2026 and remained "Em tramitação" (in progress) as of the portal's last update on June 11, 2026, with the last recorded actions being early-stage procedural steps (e.g., a joint-processing request, RQS 365/2026, on May 11, 2026). The portal shows NO record of any Plenário vote (votação em plenário) [PL 2780/2024](https://www25.senado.leg.br/web/atividade/materias/-/materia/174060)[PL 2780/2024](https://www25.senado.leg.br/web/atividade/materias/-/materia/174060). Because no plenary vote is documented, there is no URL on the portal documenting a plenary vote outcome — none exists.

2) News confirming the bill was stalled, never reaching a plenary vote:
- CNN Brasil (May 15, 2026): government was pushing for a fast vote but the bill's path (committees vs. direct-to-plenary urgency) was not even defined; no plenary vote had occurred [Governo pressiona por votação rápida do PL dos minerais críticos ...](https://www.cnnbrasil.com.br/infra/governo-pressiona-por-votacao-rapida-do-pl-dos-minerais-criticos-no-senado/).
- Broadcast Político (June 2, 2026): analysis of PL 2780/2024 was expected to be postponed until AFTER the 2026 elections given the congested Senate calendar (prioritizing the "fim da 6x1" and PEC da Segurança); no plenary vote had occurred and it was considered unlikely before the elections [Com calendário apertado, Senado acumula projetos e deve ...](https://www.broadcast.com.br/ultimas-noticias/com-calendario-apertado-senado-acumula-projetos-e-deve-priorizar-fim-da-6x1-e-pec-da-seguranca/).
- Poder360 (June 9, 2026): the bill was "represado" (bottlenecked) in the Senate amid Lula–Alcolumbre friction; the Senate had not even defined a rapporteur or which committees the text must pass through — clearly no plenary vote [Atrito Lula X Alcolumbre trava PL dos minerais críticos no Senado](https://www.poder360.com.br/poder-congresso/atrito-lula-x-alcolumbre-trava-pl-dos-minerais-criticos-no-senado/).

These sources (the authoritative Senate portal plus corroborating June 2026 reporting) consistently show the bill was still stuck in early Senate stages, with a plenary vote pushed toward "after the elections," well past the July 1, 2026 deadline.

On the amendments clause: the criteria say Senate approval WITH amendments would still count as YES. This is moot here — there was no Senate plenary vote of any kind (approval or rejection) before the deadline, so this provision does not apply.

Since "no plenary vote occurs by the deadline" explicitly resolves NO per the resolution criteria, the question resolves NO (0).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-60. `5e1b44a0-32cd-5f8f-8feb-2ad367e3d878`

- Present date: `2026-05-14 10:56:01.453875`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Israel or Hamas formally declare the October 2025 Gaza ceasefire collapsed or terminated by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 and by 23:59 UTC on July 1, 2026, either Israel or Hamas issues a formal declaration that the October 2025 Gaza ceasefire agreement (or any specific phase thereof) is collapsed, terminated, void, or no longer in effect.

**Authorized declarants:**
- **For Israel:** The Prime Minister's Office, the Israeli Security Cabinet, or an official IDF spokesperson, as communicated via official Israeli government channels (e.g., gov.il) or confirmed by at least two major international news agencies.
- **For Hamas:** The Hamas Political Bureau, a senior Hamas spokesperson (e.g., a member of the Political Bureau or a named official spokesperson), as reported by at least two major international news agencies.

**What constitutes a 'formal declaration':**
A formal declaration is an explicit, public, official statement from one of the authorized entities above that uses language clearly indicating the ceasefire agreement is terminated, collapsed, annulled, void, or no longer operative. Mere threats of resuming war, reports of increased military activity, individual ceasefire violations (however severe), or unofficial commentary by analysts or lower-ranking officials do **not** qualify.

**Resolution sources:** Official Israeli government portals (https://www.gov.il/en), and/or reporting by at least two of the following major news agencies: Reuters (https://www.reuters.com), Associated Press (https://apnews.com), Agence France-Presse, BBC (https://www.bbc.com), or Al Jazeera (https://www.aljazeera.com).

If no such formal declaration is made by 23:59 UTC on July 1, 2026, the question resolves **No**.

**Pre-cutoff background**

The October 2025 Gaza ceasefire agreement, brokered by the United States, established a phased framework to end the Israel-Hamas war. The agreement includes three phases [A Guide to the Gaza Peace Deal | Council on Foreign Relations](https://www.cfr.org/articles/guide-trumps-twenty-point-gaza-peace-deal):

- **Phase 1 (October 2025 – January 2026):** Cessation of hostilities, IDF withdrawal to a "yellow line" (retaining control of ~53% of Gaza), release of remaining hostages in exchange for Palestinian prisoners, deployment of 200 U.S. troops to monitor the ceasefire, and increased humanitarian aid (target: 600 trucks/day).
- **Phase 2 (January 2026 – ongoing):** Planning and deployment of an International Stabilization Force (ISF) to replace the IDF as the primary security force, establishment of a transitional government, and negotiation of Hamas disarmament and Gaza demilitarization.
- **Phase 3:** Full Israeli withdrawal contingent on completion of Phase 2 goals.

As of May 13, 2026, the ceasefire remains nominally in effect but is under severe strain [Israel threatens Gaza war resumption to force disarmament as 'truce ...](https://www.aljazeera.com/news/2026/5/3/israel-threatens-gaza-war-resumption-to-force-disarmament-as-truce-frays). Israel has violated the ceasefire over 1,100 times during Phase 1 alone, and continues to conduct strikes in Gaza. Israeli officials have publicly threatened to resume full-scale military operations to force Hamas disarmament, while Hamas and other Palestinian factions have rejected disarmament demands, insisting on a political horizon for statehood [Israel threatens Gaza war resumption to force disarmament as 'truce ...](https://www.aljazeera.com/news/2026/5/3/israel-threatens-gaza-war-resumption-to-force-disarmament-as-truce-frays). The U.S.-led Board of Peace has indicated it will not hold Israel to truce terms if Hamas does not accept disarmament. Despite escalatory rhetoric from both sides, neither party has formally declared the ceasefire terminated as of this date [Israel threatens Gaza war resumption to force disarmament as 'truce ...](https://www.aljazeera.com/news/2026/5/3/israel-threatens-gaza-war-resumption-to-force-disarmament-as-truce-frays).

**Exact later resolution packet**

The question resolves **NO**. It asks whether Israel (PMO, Security Cabinet, or IDF spokesperson) or Hamas (Political Bureau or a senior/named spokesperson) issued a formal, explicit public declaration that the October 2025 Gaza ceasefire is collapsed, terminated, void, or no longer in effect, between May 12, 2026 and 23:59 UTC on July 1, 2026. No such declaration was made; the ceasefire remained nominally/"formally" in effect throughout the window despite heavy violations, escalatory rhetoric, and Israeli threats to resume operations.

Key evidence across the full resolution window, from mandated sources (BBC and Al Jazeera among them):

- BBC ("Gaza ceasefire deal – the latest on the truce") explicitly states the truce "has not been declared over," noting that in practice attacks make it barely a truce — but no formal termination [ad078e].
- The Guardian's May 28, 2026 report on Netanyahu ordering the IDF to seize ~70% of Gaza shows only *analysts* (e.g., Muhammad Shehada saying Netanyahu is "declaring the whole Trump deal... null and void," and Gershon Baskin saying he "believed the original ceasefire plan had collapsed") characterizing it as void/collapsed. These are analyst opinions, NOT official declarations by authorized declarants. An IDF spokesperson referred comment "to the political echelon," and no official termination statement was issued [9a5603].
- Al Jazeera's June 9, 2026 weekly wrap describes the ceasefire as existing "more on paper than on the ground" but still in effect, with Palestinian factions convening in Cairo to discuss phase two — inconsistent with any formal termination [ed3d9c].
- FDD's June 26, 2026 analysis ("Decision or stagnation in Gaza?") confirms the ceasefire "remains nominally in effect" at the end of June 2026, with no formal declaration of termination by either party [1a2511].

Additional corroboration found in search results (not queried directly, hence uncited): UK Foreign Secretary statement of June 9, 2026 ("The ceasefire remains formally in place, but it is being regularly violated"); PBS/AP reporting that "Both sides accuse the other of violating the agreement but say it is still in effect"; and Long War Journal's June 29, 2026 update documenting IDF strikes/violations (June 10–29) but no termination declaration. Together these confirm that no authorized Israeli or Hamas entity formally declared the ceasefire collapsed, terminated, void, or no longer in effect before the July 1, 2026 deadline. Per the resolution criteria, absent such a formal declaration, the question resolves **No (0)**.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-61. `cf203c8d-7ace-5f94-8350-8fcfab5f7488`

- Present date: `2026-05-12 21:05:36.575190`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Nirav Shah win the 2026 Maine Democratic gubernatorial primary on June 9, 2026?

**Resolution criteria**

This question resolves YES if Nirav Shah is declared the winner of the 2026 Maine Democratic gubernatorial primary held on June 9, 2026, after all rounds of Ranked-Choice Voting (RCV) have been tabulated. It resolves NO if any other candidate wins.

The primary resolution source is the official certified results published by the Maine Secretary of State at https://www.maine.gov/sos/elections-voting/election-results-data. If official certified results are not yet available by the resolution date, preliminary official results from the Maine Secretary of State or credible reporting from major outlets (e.g., Associated Press, Reuters, Portland Press Herald) may be used.

**Pre-cutoff background**

The 2026 Maine Democratic gubernatorial primary is scheduled for June 9, 2026. The race features a crowded field of candidates, including Nirav Shah (former Maine CDC director), Aaron Frey (Attorney General), Shenna Bellows (Secretary of State), Troy Jackson (former State Senate President), and Hannah Pingree (former Speaker of the House).

An Impact Research poll conducted March 19–23, 2026, showed Shah leading the field with 31%, followed by Jackson at 18%, Bellows at 17%, and Pingree at 16%. However, Shah's lead is well short of a majority.

Maine uses Ranked-Choice Voting (RCV) for primary elections, meaning if no candidate receives more than 50% of first-choice votes, the last-place candidate is eliminated and their votes are redistributed according to voters' next-ranked preferences. This process repeats until one candidate achieves a majority. RCV dynamics make this race particularly uncertain, as second- and third-choice preferences from eliminated candidates could reshape the outcome significantly despite Shah's first-round polling lead.

The Maine Secretary of State publishes official election results at: https://www.maine.gov/sos/elections-voting/election-results-data

**Exact later resolution packet**

The question asks whether Nirav Shah won the 2026 Maine Democratic gubernatorial primary held June 9, 2026, after all rounds of Ranked-Choice Voting (RCV). He did NOT — Hannah Pingree won.

Key evidence:
- The Portland Press Herald (an explicitly named resolution source) published an article on June 19, 2026 titled "Hannah Pingree wins ranked-choice runoff in Democratic primary for governor" (URL: https://www.pressherald.com/2026/06/19/hannah-pingree-wins-ranked-choice-runoff-in-democratic-primary-for-governor/). The article states Pingree won the RCV runoff, "beating Dr. Nirav Shah in the final round." On election night first-choice votes, Shah led with roughly 26.8% and Pingree trailed at about 23.3%, but Pingree overcame this through the RCV redistribution process [Hannah Pingree wins ranked-choice runoff in Democratic primary ...](https://www.pressherald.com/2026/06/19/hannah-pingree-wins-ranked-choice-runoff-in-democratic-primary-for-governor/).
- FairVote's June 19, 2026 report likewise confirms Pingree's come-from-behind victory over Shah, noting Pingree secured roughly 56% in the final tally after winning the large majority of transfers from eliminated candidates; the underlying tabulations came from the Maine Department of the Secretary of State [Maine releases ranked choice voting primary results - FairVote](https://fairvote.org/maine-releases-ranked-choice-voting-primary-results/).
- Ballotpedia's June 9 Democratic primary page confirms Hannah Pingree won after the final round of RCV per Maine Secretary of State certified results, and that Nirav Shah did not win [Maine gubernatorial election, 2026 (June 9 Democratic primary)](https://ballotpedia.org/Maine_gubernatorial_election,_2026_(June_9_Democratic_primary)).

Because the RCV winner was Hannah Pingree and not Nirav Shah, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-62. `01d86c2b-219b-5f49-b591-2babd5e70049`

- Present date: `2026-05-12 15:03:03.816366`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the team that wins the Stage 3 Team Time Trial also have a rider finish on the final GC podium (top 3) of the 2026 Tour Auvergne-Rhône-Alpes?

**Resolution criteria**

This question resolves **Yes** if at least one rider from the team officially declared the winner of Stage 3 (the Team Time Trial) of the 2026 Tour Auvergne-Rhône-Alpes finishes in the top 3 of the final [General Classification](https://en.wikipedia.org/wiki/General_classification_in_road_cycling) (GC) standings at the conclusion of Stage 8 on June 14, 2026. It resolves **No** otherwise.

**Key definitions:**
- **Winning team of the Stage 3 TTT:** The team whose finishing time is the fastest in Stage 3, as recorded in the official results. In a TTT, the team's time is typically set by the nth rider to cross the finish line (per [UCI regulations](https://www.uci.org/regulations), usually the 4th rider for teams of 6). The winning team is whichever team is listed first in the Stage 3 results.
- **Final GC podium (top 3):** The three riders ranked 1st, 2nd, and 3rd in the final General Classification standings after Stage 8.
- **Rider membership:** A rider is considered part of the TTT-winning team if they were on that team's roster for the race, regardless of whether they personally finished the TTT stage.

**Resolution source:** The official results as published on [ProCyclingStats Stage 3 results page](https://www.procyclingstats.com/race/tour-auvergne-rhone-alpes/2026/stage-3) and the [final GC results page](https://www.procyclingstats.com/race/tour-auvergne-rhone-alpes/2026/gc). If ProCyclingStats is unavailable, the official race website at [https://www.tour-auvergne-rhone-alpes.fr/en/rankings](https://www.tour-auvergne-rhone-alpes.fr/en/rankings) may be used.

If Stage 3 or the race is cancelled and not rescheduled before July 1, 2026, this question resolves **N/A**.

**Pre-cutoff background**

The 2026 Tour Auvergne-Rhône-Alpes (formerly the Critérium du Dauphiné) is an 8-stage UCI WorldTour race running from June 7 to June 14, 2026 [Official route of Tour Auvergne-Rhône-Alpes 2026](https://www.tour-auvergne-rhone-alpes.fr/en/overall-route). Stage 3 is a 28.4 km Team Time Trial (TTT) in Perreux, scheduled for Tuesday, June 9, 2026 (CEST, UTC+2) [Official route of Tour Auvergne-Rhône-Alpes 2026](https://www.tour-auvergne-rhone-alpes.fr/en/overall-route). The race concludes with Stage 8 on Sunday, June 14, 2026, finishing at Plateau de Solaison - Brison [Official route of Tour Auvergne-Rhône-Alpes 2026](https://www.tour-auvergne-rhone-alpes.fr/en/overall-route).

A [Team Time Trial](https://en.wikipedia.org/wiki/Team_time_trial) (TTT) is a road cycling discipline where entire teams ride together against the clock. TTT success depends on collective team strength and coordination, which does not always correlate with having a top individual General Classification (GC) contender. Some teams may dominate the TTT through depth and power but lack a rider capable of competing in the mountain stages that decide the GC. Conversely, teams built around a single GC leader may lack the collective TTT strength to win Stage 3.

The race features a mountainous final weekend (Stages 6–8), including finishes at Crest-Voland, Grand Colombier, and Plateau de Solaison [Official route of Tour Auvergne-Rhône-Alpes 2026](https://www.tour-auvergne-rhone-alpes.fr/en/overall-route), which will be decisive for the final GC standings. As of May 11, 2026 (UTC), the race has not yet started. According to ProCyclingStats, top competitors include Isaac del Toro, Paul Seixas, and Wout van Aert [Tour Auvergne - Rhône-Alpes 2026 Stage 3 (TTT) results](https://www.procyclingstats.com/race/tour-auvergne-rhone-alpes/2026/stage-3).

**Exact later resolution packet**

RESOLUTION: NO (0).

STEP 1 — Stage 3 TTT winner. The Stage 3 Team Time Trial (Perreux, 28.4 km) of the 2026 Tour Auvergne-Rhône-Alpes was officially won by Team Visma | Lease a Bike, listed first with a time of 32:52.170 ahead of Netcompany INEOS (33:01.780), EF Education-EasyPost (33:21.580), Lidl-Trek (33:24.580) and Red Bull-BORA-hansgrohe (33:33.000) [490f08]. Matteo Jorgenson led Visma across the line. This is corroborated by the official race site ("Jorgenson leads Visma's bees to victory") and multiple outlets (Cyclingweekly, FloBikes). UCI fines issued after the TTT were only for teams failing to present bikes for inspection on time (Jayco AlUla, TotalEnergies, Lotto-Intermarché) and did NOT change the winner or disqualify any team — Visma remained the official winner [9e7e7e]. So the antecedent (a team wins Stage 3) occurred and Stage 3/the race were NOT cancelled; the question is live, not N/A.

STEP 2 — Final GC podium after Stage 8. The final General Classification top 3 were:
1. Isaac del Toro — UAE Team Emirates-XRG (29:35:05)
2. Luke Tuckwell — Red Bull-BORA-hansgrohe (+0:54)
3. Juan Ayuso — Lidl-Trek (+1:17)
[af43b7]. This is independently confirmed by RTE, CyclingStage, Cyclingweekly, TNT Sports and the official race website (tour-auvergne-rhone-alpes.fr/en/rankings), all of which list del Toro, Tuckwell, Ayuso as 1-2-3, with Matteo Jorgenson 4th (+1:36).

STEP 3 — Rider membership test. None of the three podium riders belongs to the TTT-winning team (Visma | Lease a Bike): del Toro rides for UAE Team Emirates-XRG, Tuckwell for Red Bull-BORA-hansgrohe, and Ayuso for Lidl-Trek [af43b7]. Visma's highest-placed rider in the final GC was Matteo Jorgenson in 4th place — just outside the top-3 podium. Applying the rider-membership rule (a rider counts if on the winning team's roster regardless of whether they finished the TTT) does not change this, because no Visma rider reached the top 3.

CONCLUSION: The team that won the Stage 3 TTT (Visma | Lease a Bike) did NOT have a rider finish on the final GC podium. Resolves NO.

Sources: ProCyclingStats Stage 3 results (https://www.procyclingstats.com/race/tour-auvergne-rhone-alpes/2026/stage-3/result/result) [490f08]; ProCyclingStats final GC (https://www.procyclingstats.com/race/tour-auvergne-rhone-alpes/2026/gc) [af43b7]; IDLprocycling article confirming Visma won and fines did not alter results [9e7e7e].

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-63. `a0c26adc-e889-5f86-81fd-79aa8165ab8e`

- Present date: `2026-05-12 20:02:45.699042`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Panathinaikos AKTOR Athens win Game 5 against Valencia Basket in the 2026 EuroLeague Playoffs on May 13, 2026?

**Resolution criteria**

This question resolves **Yes** if Panathinaikos AKTOR Athens defeats Valencia Basket in Game 5 of the 2025–26 EuroLeague Playoffs quarter-final series, thereby qualifying for the 2026 EuroLeague Final Four. It resolves **No** if Valencia Basket wins Game 5.

"Win" means finishing the game (including any overtime periods) with more points than the opponent, as recorded in the official game result.

The resolution source is the official EuroLeague game center page for this match:
https://www.euroleaguebasketball.net/euroleague/game-center/2025-26/valencia-basket-panathinaikos-aktor-athens/E2025/403/

"Qualify" for the Final Four means winning three games in the best-of-five playoff series, per EuroLeague rules (https://en.wikipedia.org/wiki/EuroLeague#Format).

**If the game is postponed or rescheduled:** This question resolves based on the official result of Game 5 of this series whenever it is played, provided it is completed by June 30, 2026 (23:59 UTC). If Game 5 is not completed by that date, or the game is cancelled and no result is recorded, this question resolves **No**.

**Pre-cutoff background**

The 2025–26 EuroLeague Playoffs feature a best-of-five quarter-final series between Valencia Basket (#2 seed) and Panathinaikos AKTOR Athens (#7 seed). As of May 11, 2026, the series is currently tied 2-2 [2026 EuroLeague Playoffs - Wikipedia](https://en.wikipedia.org/wiki/2026_EuroLeague_Playoffs). Game 5, the decisive match, is scheduled for May 13, 2026, at 21:00 CEST (19:00 UTC) at the Roig Arena in Valencia, Spain [2026 EuroLeague Playoffs - Wikipedia](https://en.wikipedia.org/wiki/2026_EuroLeague_Playoffs).

Valencia Basket earned home-court advantage by finishing as the #2 seed in the regular season and will host the decisive Game 5 at the Roig Arena. Panathinaikos is the defending EuroLeague champion and carries significant Final Four experience. The series has been highly competitive, with both teams trading wins across the first four games.

The winner of Game 5 will advance to the 2026 EuroLeague Final Four (see: https://en.wikipedia.org/wiki/2026_EuroLeague_Playoffs). The EuroLeague Playoffs format is a best-of-five series where the first team to win three games qualifies for the Final Four (see EuroLeague competition format: https://en.wikipedia.org/wiki/EuroLeague#Format).

**Exact later resolution packet**

The question asks whether Panathinaikos AKTOR Athens defeated Valencia Basket in Game 5 of the 2025-26 EuroLeague Playoffs quarter-final series on May 13, 2026. It resolves YES if Panathinaikos wins Game 5, and NO if Valencia Basket wins.

The designated resolution source, the official EuroLeague game center page (https://www.euroleaguebasketball.net/euroleague/game-center/2025-26/valencia-basket-panathinaikos-aktor-athens/E2025/403/), confirms the final score of Game 5 was Valencia Basket 81, Panathinaikos AKTOR Athens 64 [https://www.euroleaguebasketball.net/euroleague/game-center/2025-26/valencia-basket-panathinaikos-aktor-athens/E2025/403/](https://www.euroleaguebasketball.net/euroleague/game-center/2025-26/valencia-basket-panathinaikos-aktor-athens/E2025/403/). The game was played at the Roig Arena in Valencia. Valencia won the game and thereby the best-of-five series 3-2, qualifying for the 2026 EuroLeague Final Four instead of Panathinaikos.

This result is corroborated by multiple independent sources found via Google search: Sofascore ("Valencia Basket 81 - 64 Finished Panathinaikos"; "Valencia Basket handled the pressure at Roig Arena, beating Panathinaikos BC 81-64 to win the EuroLeague Playoffs quarterfinal series 3-2"), 365scores ("Panathinaikos 64 - 81 Valencia Basket... ended with a final score of Panathinaikos 64 - 81 Valencia"), RealGM ("May 13, 2026 - Panathinaikos 64 at Valencia Basket 81"), Flashscore ("13.05.2026... Valencia 81-64 Finished Panathinaikos... Valencia wins series 3-2"), BasketNews ("PAO ended up losing 81-64 in Game 5 and will miss the Final Four in their home arena"), and Eurohoops ("Valencia... defeated Panathinaikos with a score of 81-64 in Game 5 on their home [court]"). The official EuroLeague game center headline itself read "Valencia routs PAO in Game 5 to reach Final Four!"

The 81-64 scoreline is a decisive regulation result with no overtime (there was no indication of any overtime in Game 5; the overtime drama in this series occurred in earlier games such as Game 2). Including any hypothetical overtime, Valencia finished with more points than Panathinaikos.

Because Valencia Basket won Game 5, and the question resolves NO if Valencia Basket wins, the resolution is NO (0). The game was completed on May 13, 2026, well before the June 30, 2026 deadline, so the fallback "resolves No" clause for incompletion is not triggered—but even the fallback would point to NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### NO-64. `26ae4990-03a3-55fa-8500-fb4eb796b9c5`

- Present date: `2026-05-02 17:22:29.644804`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any ASEAN member state publicly oppose or distance itself from the Philippines' position on the South China Sea Code of Conduct between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 1, 2026 (00:00 UTC) and June 1, 2026 (23:59 UTC), an official government representative (Head of State, Foreign Minister, or official government spokesperson) of any of the following ASEAN member states—Brunei Darussalam, Cambodia, Indonesia, Lao PDR, Malaysia, Myanmar, Singapore, Thailand, Timor-Leste, or Vietnam—publicly opposes or distances their country from the Philippines' position on the South China Sea Code of Conduct.

The "Philippines' position" is defined as the stance articulated by the Philippine government that the COC must be (a) legally binding and (b) explicitly grounded in UNCLOS, as stated by the Philippine Foreign Minister in January 2026 (https://www.reuters.com/world/china/philippines-will-insist-south-china-sea-code-is-based-international-law-foreign-2026-01-22/).

"Publicly oppose or distance" means any of the following:
1. An official statement explicitly rejecting or criticizing the Philippines' position that the COC should be legally binding or grounded in UNCLOS.
2. An official statement declaring that a member state does not support the Philippines' approach to COC negotiations.
3. A formal, publicly reported refusal to join an ASEAN joint statement or declaration that includes the Philippines' COC position, where the refusal is attributed to disagreement with the Philippines' stance.

Resolution will be based on reporting from credible international or regional news sources, including but not limited to:
- Reuters (https://www.reuters.com/)
- Associated Press (https://apnews.com/)
- South China Morning Post (https://www.scmp.com/)
- The Straits Times (https://www.straitstimes.com/)
- Channel News Asia (https://www.channelnewsasia.com/)
- ASEAN Secretariat press releases (https://asean.org/category/asean-secretariat-news/)

Routine diplomatic language expressing differing preferences (e.g., "we hope for a pragmatic approach") does NOT qualify unless it explicitly contradicts the Philippines' stated position. The statement must be directly attributable to a named official or official government channel.

If no qualifying public opposition or distancing occurs by 23:59 UTC on June 1, 2026, the question resolves **No**.

**Pre-cutoff background**

The Philippines, serving as the 2026 ASEAN chair, has taken a firm position that the South China Sea Code of Conduct (COC) must be legally binding and explicitly reference the UN Convention on the Law of the Sea (UNCLOS) [Philippines will insist South China Sea code is based on ... - Reuters](https://www.reuters.com/world/china/philippines-will-insist-south-china-sea-code-is-based-international-law-foreign-2026-01-22/). Negotiations on the COC have been ongoing for over two decades, with key unresolved issues including the code's geographic scope, legal status, and enforcement mechanisms [ASEAN, China unlikely to finalize South China Sea Code of Conduct ...](https://www.rfa.org/english/southchinasea/2026/04/24/asean-south-china-sea-code-of-conduct-philippines/).

As of April 2026, analysts assess that completing the COC during the Philippines' chairmanship year is unlikely, with a Chinese analyst stating it "cannot be successfully negotiated" while the Philippines holds the ASEAN chair. ASEAN's consensus-based approach often leads to diluted agreements, and there is significant internal tension: some members (notably Cambodia and Laos) historically maintain closer ties to China, while claimant states like Vietnam and the Philippines advocate for a stronger framework [ASEAN, China unlikely to finalize South China Sea Code of Conduct ...](https://www.rfa.org/english/southchinasea/2026/04/24/asean-south-china-sea-code-of-conduct-philippines/).

The 48th ASEAN Summit is scheduled for May 5–9, 2026, in Cebu, Philippines, making May 2026 a particularly active period for potential disagreements to surface [ASEAN, China unlikely to finalize South China Sea Code of Conduct ...](https://www.rfa.org/english/southchinasea/2026/04/24/asean-south-china-sea-code-of-conduct-philippines/). Historical precedent includes Cambodia blocking an ASEAN joint statement on the South China Sea in 2012, demonstrating that public breaks in ASEAN unity on this issue have occurred before.

ASEAN currently has 11 member states: Brunei Darussalam, Cambodia, Indonesia, Lao PDR, Malaysia, Myanmar, the Philippines, Singapore, Thailand, Timor-Leste, and Vietnam. Timor-Leste became the 11th member on October 26, 2025.

**Exact later resolution packet**

The question resolves NO because no credible source reported any ASEAN member state's official government representative publicly opposing or distancing itself from the Philippines' position (that the South China Sea COC must be legally binding and explicitly grounded in UNCLOS) between May 1 and June 1, 2026.

Key evidence:
- The central event in the window, the 48th ASEAN Summit (Cebu, May 7–8, 2026), produced a Chair's Statement and an ASEAN Leaders' Declaration on Maritime Cooperation that were adopted by all member states. The Maritime Cooperation Declaration committed ASEAN to "ENDEAVOUR to conclude the negotiation of an effective and substantive Code of Conduct in the South China Sea (COC) in accordance with international law, including the 1982 UNCLOS." There is no record in these official ASEAN documents of any member opposing the Philippines' stance or refusing to join the joint statement [89c6c6, 5fe148].
- A search of credible news outlets (Reuters, AP, SCMP, Straits Times, CNA, RFA) and the ASEAN Secretariat surfaced no report during the window of an official (Head of State, Foreign Minister, or government spokesperson) of Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Singapore, Thailand, Timor-Leste, or Vietnam explicitly rejecting the legally-binding/UNCLOS position, declaring non-support for the Philippines' approach, or refusing a joint statement over that disagreement.
- Reporting from the period describes ASEAN as collectively optimistic/"encouraged" by COC progress, with the Philippines (FM Theresa Lazaro) noting that the UNCLOS insistence is shared by "other ASEAN member states." No public intra-ASEAN break specific to the Philippines' COC position was reported.
- Cambodia's recurring public line ("absolutely No Multilateral negotiations allowed" on the South China Sea) appears as boilerplate on Cambodian Facebook posts and concerns the format/scope of negotiations rather than an explicit rejection of the Philippines' legally-binding-plus-UNCLOS position; it does not satisfy the resolution criteria, which exclude routine diplomatic preference statements and require explicit contradiction of the Philippines' stated position. I could not retrieve the underlying Freshnews post content to find any dated May 2026 statement attributable to FM Prak Sokhonn that opposes the binding/UNCLOS stance.

Since no qualifying public opposition or distancing was found by the 23:59 UTC June 1, 2026 deadline, the question resolves NO.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

## Realized YES queue (64 candidates)

### YES-1. `10a0455b-c9fc-58f0-87e8-22172f97c898`

- Present date: `2026-05-03 10:13:55.047548`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Taiwan's Legislative Yuan pass the special defense budget (NT$1.25 trillion proposal) by June 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 1, 2026 (00:00 Taipei Time, UTC+8) and on or before June 1, 2026 (23:59 Taipei Time, UTC+8), the Legislative Yuan of the Republic of China (Taiwan) completes the third reading (三讀通過) of any special defense budget bill related to the NT$1.25 trillion proposal originally submitted by the Executive Yuan in November 2025 — regardless of the final approved amount.

This question resolves NO if no such third reading is completed by the deadline.

"Pass" is defined as completing the third reading in the Legislative Yuan, which is the final legislative step required for a bill to be considered passed by the legislature. The President's subsequent promulgation is not required for resolution.

Resolution will be determined by official records from the Legislative Yuan (https://www.ly.gov.tw/) or the Legislative Yuan Gazette, or by credible reporting from major news outlets such as Reuters (https://www.reuters.com/), the Central News Agency (https://focustaiwan.tw/), or the Associated Press.

**Pre-cutoff background**

In late November 2025, Taiwan's Executive Yuan proposed a special defense budget of NT$1.25 trillion (approximately US$40 billion) covering the period 2026–2033, intended to fund US weapons procurement and domestic defense production including drones and integrated air and missile defense systems [https://www.reuters.com/world/china/us-presses-taiwan-parliament-pass-comprehensive-defence-budget-2026-04-27/](https://www.reuters.com/world/china/us-presses-taiwan-parliament-pass-comprehensive-defence-budget-2026-04-27/). This is separate from Taiwan's regular annual defense budget.

The budget has faced sustained opposition in the Legislative Yuan, where the opposition KMT holds a majority. The KMT has refused to approve what it calls a "blank cheque," demanding more details from the government. KMT lawmaker Hsu Chiao-hsin has proposed a reduced figure of NT$800 billion (~US$25.46 billion), while other KMT members have suggested even smaller amounts [https://www.reuters.com/world/china/us-presses-taiwan-parliament-pass-comprehensive-defence-budget-2026-04-27/](https://www.reuters.com/world/china/us-presses-taiwan-parliament-pass-comprehensive-defence-budget-2026-04-27/). The budget was blocked 69 times by the Legislative Yuan's Procedure Committee before eventually advancing to review.

As of April 27, 2026, cross-party talks on the special defense budget ended without agreement. The next round of negotiations is scheduled for May 6, 2026 (Taipei Time, UTC+8) [https://www.reuters.com/world/china/us-presses-taiwan-parliament-pass-comprehensive-defence-budget-2026-04-27/](https://www.reuters.com/world/china/us-presses-taiwan-parliament-pass-comprehensive-defence-budget-2026-04-27/). The United States has publicly pressured Taiwan to pass a "comprehensive" defense budget, with the AIT director urging passage. Taiwan's military has warned that further delay threatens US$2.4 billion in weapons procurement and training [https://www.reuters.com/world/china/us-presses-taiwan-parliament-pass-comprehensive-defence-budget-2026-04-27/](https://www.reuters.com/world/china/us-presses-taiwan-parliament-pass-comprehensive-defence-budget-2026-04-27/).

Three competing special budget bills are under review in the Legislative Yuan: the DPP's original NT$1.25 trillion proposal and alternative proposals from opposition parties. "Passing" the budget requires approval by the full Legislative Yuan (third reading). The President's subsequent promulgation is a formality under Taiwan's constitutional process.

**Exact later resolution packet**

The question resolves YES. On May 8, 2026, Taiwan's Legislative Yuan completed the third reading (三讀通過) of the "Special Act for Procurement of National Defense Security and Strengthening Asymmetric Combat Capabilities" (保衛國家安全及強化不對稱戰力計畫採購特別條例), setting a budget cap of NT$780 billion (NT$300 billion first batch + NT$480 billion second batch) [國防特別條例三讀通過預算上限7800億政院專報經立院同意始得編列](https://www.cna.com.tw/news/aipl/202605080239.aspx). The Taipei Times confirmed the legislature "passed the third reading of a special defense budget of NT$780 billion (US$24.82 billion)" and that this amount fell short of the NT$1.25 trillion originally requested by the DPP government [Legislature passes NT$780bn special arms procurement act](https://www.taipeitimes.com/News/front/archives/2026/05/08/2003856996).

Checklist verification:
- Third reading (三讀通過): Confirmed by both CNA and Taipei Times [國防特別條例三讀通過預算上限7800億政院專報經立院同意始得編列](https://www.cna.com.tw/news/aipl/202605080239.aspx) [Legislature passes NT$780bn special arms procurement act](https://www.taipeitimes.com/News/front/archives/2026/05/08/2003856996).
- Date within window: May 8, 2026 falls strictly within May 1–June 1, 2026 (Taipei Time) [國防特別條例三讀通過預算上限7800億政院專報經立院同意始得編列](https://www.cna.com.tw/news/aipl/202605080239.aspx) [Legislature passes NT$780bn special arms procurement act](https://www.taipeitimes.com/News/front/archives/2026/05/08/2003856996).
- Special vs regular budget: The bill is the SPECIAL defense procurement act (特別條例), not the regular annual defense budget [國防特別條例三讀通過預算上限7800億政院專報經立院同意始得編列](https://www.cna.com.tw/news/aipl/202605080239.aspx).
- Related to November 2025 NT$1.25 trillion proposal: Yes — this is the legislative outcome of the Executive Yuan's November 2025 special budget proposal, with the final amount reduced to NT$780 billion. The resolution criteria explicitly state YES applies "regardless of the final approved amount" [Legislature passes NT$780bn special arms procurement act](https://www.taipeitimes.com/News/front/archives/2026/05/08/2003856996) [國防特別條例三讀通過預算上限7800億政院專報經立院同意始得編列](https://www.cna.com.tw/news/aipl/202605080239.aspx).
- Mandatory sources: Central News Agency (CNA) https://www.cna.com.tw/news/aipl/202605080239.aspx [國防特別條例三讀通過預算上限7800億政院專報經立院同意始得編列](https://www.cna.com.tw/news/aipl/202605080239.aspx) and Taipei Times https://www.taipeitimes.com/News/front/archives/2026/05/08/2003856996 [Legislature passes NT$780bn special arms procurement act](https://www.taipeitimes.com/News/front/archives/2026/05/08/2003856996).

Note: The May 8 third reading was of the enabling special act (特別條例) which set the budget ceiling. A separate first-batch special budget bill of NT$8.81 billion was later passed on May 29, 2026, but the May 8 third reading of the special act itself already satisfies the resolution criteria of completing a third reading of a special defense budget bill related to the original proposal.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-2. `38cef1e5-68c6-5c07-9b49-5d1412ec8476`

- Present date: `2026-05-14 07:59:20.527109`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Samsung Electronics and the National Samsung Electronics Union (NSEU) reach a signed wage agreement between May 12, 2026, and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if Samsung Electronics and the National Samsung Electronics Union (NSEU, also known as 전국삼성전자노동조합) reach and sign a formal wage agreement on or after May 12, 2026 (00:00 UTC), and on or before July 1, 2026 (23:59 UTC). Any agreement signed before May 12, 2026 does not count.

A "signed wage agreement" is defined as a written contract, collective bargaining agreement, or memorandum of understanding (MOU) regarding wages and/or bonuses that is publicly confirmed by both Samsung Electronics and the NSEU.

This question resolves **No** if no such agreement is publicly confirmed by 23:59 UTC on July 1, 2026.

**Resolution source:** Official announcements from [Samsung Newsroom](https://news.samsung.com/) or the NSEU, or credible reporting from major news outlets including [Reuters](https://www.reuters.com/), [Bloomberg](https://www.bloomberg.com/), or the Associated Press confirming the signing of a wage agreement.

**Pre-cutoff background**

As of May 12, 2026, Samsung Electronics is engaged in contentious wage negotiations with the National Samsung Electronics Union (NSEU), the company's largest labor union. The core dispute centers on the size of the performance bonus pool: the union demands 15% of operating profit be allocated to the bonus pool, while Samsung management has offered 10% — a gap of 5 percentage points [https://www.reuters.com/business/world-at-work/samsung-elec-union-threatens-walk-out-pay-talks-if-no-mediation-proposal-2026-05-12/](https://www.reuters.com/business/world-at-work/samsung-elec-union-threatens-walk-out-pay-talks-if-no-mediation-proposal-2026-05-12/). The union is also demanding the removal of a cap on bonuses currently set at 50% of annual base salary, and is seeking multi-year structural commitments on compensation [https://www.reuters.com/business/world-at-work/samsung-elec-union-threatens-walk-out-pay-talks-if-no-mediation-proposal-2026-05-12/](https://www.reuters.com/business/world-at-work/samsung-elec-union-threatens-walk-out-pay-talks-if-no-mediation-proposal-2026-05-12/). These demands have been fueled by Samsung's recent record profits and by employee frustration over a perceived pay gap compared to rival SK Hynix, which abolished its own pay cap [https://www.reuters.com/business/world-at-work/samsung-elec-union-threatens-walk-out-pay-talks-if-no-mediation-proposal-2026-05-12/](https://www.reuters.com/business/world-at-work/samsung-elec-union-threatens-walk-out-pay-talks-if-no-mediation-proposal-2026-05-12/). The union has threatened to walk out of pay talks if no mediation proposal is offered [https://www.reuters.com/business/world-at-work/samsung-elec-union-threatens-walk-out-pay-talks-if-no-mediation-proposal-2026-05-12/](https://www.reuters.com/business/world-at-work/samsung-elec-union-threatens-walk-out-pay-talks-if-no-mediation-proposal-2026-05-12/).

For context, Samsung's first-ever major strike occurred in 2024 and took months to resolve. The 2026 dispute involves broader structural demands, making a swift resolution uncertain. Both sides have strong incentives to settle — Samsung to protect chip production continuity, and the union to lock in gains — but the wide gap in positions and the structural nature of the demands create significant uncertainty about the timeline.

**Exact later resolution packet**

**Resolution: YES (1)**

The question asks whether Samsung Electronics and the National Samsung Electronics Union (NSEU, 전국삼성전자노동조합) reached and signed a formal wage agreement between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), publicly confirmed by both parties and addressing wages/bonuses.

**All criteria are satisfied:**

1. **Formal signing within the window.** Samsung's official newsroom (news.samsung.com) reported that on **May 27, 2026**, Samsung Electronics and the labor-union joint bargaining group held a formal 2026 wage agreement signing ceremony (임금협약 조인식) at Samsung's "The UniverSE" facility in Giheung, Yongin: "2026년 5월 27일 삼성전자와 삼성전자 노동조합 공동교섭단...은 2026년 임금협약 조인식을 진행했다" [55e5be]. A "조인식" (signing ceremony) for an "임금협약" (wage agreement) is a formal signed agreement, not merely a tentative deal. This date (May 27, 2026) falls squarely within the May 12 – July 1, 2026 window.

2. **NSEU specifically participated and publicly acknowledged the agreement.** The Samsung Newsroom announcement names the attendees of the signing, which included Samsung VPs (여명구 부사장, 김형로 부사장) AND the NSEU's representative Kim Jae-won (전국삼성전자노동조합 김재원 정책기획국장), alongside the Super-Enterprise Union's chairman Choi Seung-ho [55e5be]. Thus both Samsung Electronics and the NSEU publicly confirmed the deal.

3. **Distinguishing tentative vs. formal signed agreement.** A tentative agreement (잠정합의안) was reached late on May 20, 2026 (the night before a planned strike); it was then ratified by a member vote held May 22–27, 2026 (95.5% turnout, 73.7% in favor); and it was FORMALLY SIGNED at the ceremony on May 27, 2026 [55e5be]. Reuters independently confirmed on May 27, 2026 that two Samsung unions announced 74% of 62,616 voting workers backed the agreement [c34e0c]. So the criteria's requirement of a formal signed agreement (beyond a tentative deal) is met.

4. **Addresses wages and bonuses.** The agreement includes a ~6.2% wage increase and allocates 10.5% of semiconductor operating profit to special bonuses for chip workers [c34e0c][55e5be] — directly addressing the wage/bonus dispute described in the question.

5. **Mandatory sources cited.** Confirmation comes from Samsung Newsroom (https://news.samsung.com/kr/삼성전자-노사-2026년-임금협약-체결) [55e5be] and Reuters (https://www.reuters.com/business/world-at-work/samsungs-unionised-workers-south-korea-approve-wage-deal-2026-05-27/) [c34e0c], both on the resolution source list.

**Notes on potential loopholes:** A minority union (the non-chip/DX union) filed a court injunction to block the vote, but the court dismissed the bid (Reuters, May 25/26, 2026), and the minority union's later challenge does not undo the fact that NSEU and Samsung signed. The industriALL "NSEU concludes collective bargaining agreement" page refers to a different, 2025 agreement (signed March 5, 2025) and is not relevant to this 2026 window [08b31c]. Neither of these affects the YES resolution.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-3. `c4eaa5f2-042c-52d9-921c-fff5cd40f9b1`

- Present date: `2026-05-12 20:46:36.746333`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the 2026 Terra Wortmann Open singles final feature at least one player ranked outside the ATP top 10?

**Resolution criteria**

This question resolves YES if at least one of the two players scheduled to contest the 2026 Terra Wortmann Open men's singles final is ranked outside the top 10 (i.e., ranked 11 or lower) in the official Pepperstone ATP Singles Rankings published on Monday, June 15, 2026 (the first day of the tournament). The official rankings are available at https://www.atptour.com/en/rankings/singles.

"Top 10" means occupying positions 1 through 10 in the official ATP singles rankings on that date.

The singles final must take place on or after May 10, 2026 (it is scheduled for June 21, 2026 UTC).

In the event of a withdrawal or walkover before the final match is played, the player who was scheduled to appear in the final (i.e., won their semifinal) still counts as "featuring" in the final for resolution purposes.

If the tournament is cancelled or the singles final is not completed by June 30, 2026 (23:59 UTC), the question resolves N/A.

Resolution source: Official ATP Tour tournament results page (https://www.atptour.com/en/scores/current/halle/500/results) and official ATP rankings (https://www.atptour.com/en/rankings/singles).

**Pre-cutoff background**

The Terra Wortmann Open is an ATP 500 grass-court tournament held annually in Halle, Germany. The 2026 edition runs from June 15–21, 2026, with the singles final scheduled for June 21, 2026 (https://en.wikipedia.org/wiki/Terra_Wortmann_Open).

The confirmed 2026 field includes several top-10 players such as Alexander Zverev, Daniil Medvedev, Taylor Fritz, and Ben Shelton, as well as players on the fringe of the top 10 like Alexander Bublik (the 2025 champion) and Andrey Rublev.

As of the ATP rankings dated May 4, 2026, the top 10 are: 1. Jannik Sinner (14,350 pts), 2. Carlos Alcaraz (12,960), 3. Alexander Zverev (5,805), 4. Novak Djokovic (4,700), 5. Félix Auger-Aliassime (4,050), 6. Ben Shelton (4,030), 7. Taylor Fritz (3,770), 8. Alex de Minaur (3,755), 9. Daniil Medvedev (3,460), 10. Lorenzo Musetti (3,415). Alexander Bublik sits at No. 11 with Andrey Rublev nearby. Rankings are tightly bunched from positions 5–12, meaning the top 10 composition could shift before the tournament begins.

Grass-court events historically produce more upsets than hardcourt events due to the fast, low-bouncing surface that favors big servers and aggressive players, some of whom are ranked outside the top 10. The 2025 final was won by Bublik, who was ranked outside the top 10 at the time.

**Exact later resolution packet**

The question resolves YES.

**The final and antecedent conditions:** The 2026 Terra Wortmann Open (Halle Open) men's singles final was contested and completed on June 21, 2026, well before the June 30, 2026 23:59 UTC cutoff. Frances Tiafoe defeated Taylor Fritz 6–4, 6–4 in an all-American final [2026 Halle Open - Wikipedia](https://en.wikipedia.org/wiki/2026_Halle_Open) [https://www.atptour.com/en/scores/current/halle/500/results](https://www.atptour.com/en/scores/current/halle/500/results). The tournament was not cancelled and the final was completed, so the question is NOT annulled.

**Rankings check (the key criterion):** The question resolves YES if at least one of the two finalists was ranked 11 or lower in the official ATP Singles Rankings published Monday, June 15, 2026.
- Taylor Fritz was the No. 5 seed and was ranked around No. 9 (inside the top 10) [2026 Halle Open - Wikipedia](https://en.wikipedia.org/wiki/2026_Halle_Open) [https://www.atptour.com/en/scores/current/halle/500/results](https://www.atptour.com/en/scores/current/halle/500/results).
- Frances Tiafoe was UNSEEDED (not among the top 8 seeds) and was ranked well outside the top 10. His career-high ranking of No. 10 dates to June 19, 2023; in June 2026 he was ranked in the high-20s entering Halle, and he rose to No. 19 immediately after winning the title (ranking dated June 22, 2026) [2026 Halle Open - Wikipedia](https://en.wikipedia.org/wiki/2026_Halle_Open) [https://www.atptour.com/en/scores/current/halle/500/results](https://www.atptour.com/en/scores/current/halle/500/results) [Current tennis rankings - Wikipedia](https://en.wikipedia.org/wiki/Current_tennis_rankings). As of the June 29, 2026 ATP rankings he was still only No. 19 [Current tennis rankings - Wikipedia](https://en.wikipedia.org/wiki/Current_tennis_rankings). On June 15, 2026 he was therefore unambiguously ranked 11 or lower.

Since at least one finalist (Frances Tiafoe) was ranked outside the ATP top 10, the condition for YES is satisfied.

**Sources:**
- Tournament results: https://www.atptour.com/en/scores/current/halle/500/results [https://www.atptour.com/en/scores/current/halle/500/results](https://www.atptour.com/en/scores/current/halle/500/results) and Wikipedia 2026 Halle Open https://en.wikipedia.org/wiki/2026_Halle_Open [2026 Halle Open - Wikipedia](https://en.wikipedia.org/wiki/2026_Halle_Open)
- ATP rankings for week of June 15, 2026: https://www.atptour.com/en/rankings/singles (referenced in the June 15, 2026 ATP rankings news article https://www.atptour.com/en/news/majchrzak-pif-atp-rankings-june-15-2026 [Kamil Majchrzak cracks Top 50 for first time, Mover of Week | ATP Tour](https://www.atptour.com/en/news/majchrzak-pif-atp-rankings-june-15-2026)); Tiafoe's outside-top-10 status corroborated by https://en.wikipedia.org/wiki/Current_tennis_rankings [Current tennis rankings - Wikipedia](https://en.wikipedia.org/wiki/Current_tennis_rankings).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-4. `1ecfe907-7a50-5127-ad5b-7da4af090af0`

- Present date: `2026-05-03 10:30:41.709998`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Ken Paxton defeat John Cornyn in the Texas Republican U.S. Senate Class II primary runoff on May 26, 2026?

**Resolution criteria**

This question resolves **Yes** if Ken Paxton receives more votes than John Cornyn in the May 26, 2026 Texas Republican primary runoff for U.S. Senate (Class II seat, as defined at https://en.wikipedia.org/wiki/Classes_of_United_States_senators). It resolves **No** if John Cornyn receives more votes than Ken Paxton.

**Resolution source:** The question resolves based on official certified results from the Texas Secretary of State (https://www.sos.state.tx.us/elections/historical/index.shtml) [March 3, 2026 Primary Election Law Calendar and May 26, 2026 ...](https://www.sos.state.tx.us/elections/laws/advisory2025-17-mar-3-2026-primary-elec-law-cal-and-may-26-2026-primary-runoff-elec-law-cal.shtml). If certified results are not yet available by the resolution date, unofficial results as reported by the Associated Press (https://apnews.com/hub/texas-election-results) or Decision Desk HQ may be used, provided they have called the race. Results must be confirmed by 11:59 PM Central Time (CT) on June 1, 2026.

**Edge cases:**
- If the May 26, 2026 Republican primary runoff does not occur (e.g., because one candidate withdraws and the other wins the nomination outright, or the runoff is canceled for any reason), this question resolves **N/A**.
- If the runoff occurs but does not feature both Ken Paxton and John Cornyn as candidates, this question resolves **N/A**.
- If the runoff is postponed beyond June 1, 2026, this question resolves **N/A**.

**Pre-cutoff background**

The 2026 Texas Republican primary runoff for the U.S. Senate Class II seat (https://en.wikipedia.org/wiki/2026_United_States_Senate_election_in_Texas) is scheduled for May 26, 2026. Incumbent Senator John Cornyn (https://en.wikipedia.org/wiki/John_Cornyn) and Texas Attorney General Ken Paxton (https://en.wikipedia.org/wiki/Ken_Paxton) advanced to the runoff after finishing as the top two candidates in the March 3, 2026 Republican primary, where neither secured a majority of votes.

As of late April 2026, both candidates are actively campaigning. Polling shows a competitive race with conflicting signals: a Texas Public Opinion Research (TPOR) poll from April 17, 2026 showed Paxton leading Cornyn 48%–40% among likely voters with 11% undecided [Ken Paxton leads John Cornyn by 8 percentage points among likely ...](https://www.houstonpublicmedia.org/articles/news/politics/election-2026/2026/04/17/549428/paxton-cornyn-poll-republican-primary-runoff-texas-senate-race/). Other polls have shown a tighter race, with some giving Cornyn a narrow lead. The race has drawn significant national attention due to the unusual dynamic of a sitting senator facing a serious primary challenge from a statewide officeholder within the same party. President Trump's endorsement posture has been a key factor in the race dynamics.

**Exact later resolution packet**

The question resolves YES. The Texas Republican U.S. Senate Class II primary runoff took place as scheduled on May 26, 2026, featuring both Ken Paxton and John Cornyn, and neither withdrew. Ken Paxton defeated incumbent John Cornyn. The Associated Press called the race for Paxton shortly after polls closed on May 26, 2026 [5fe623]. NBC News, citing Associated Press vote data, reported Paxton winning with 885,962 votes (63.8%) to Cornyn's 501,729 votes (36.2%) [fb8879]. This was well within the June 1, 2026 11:59 PM CT deadline, and was called by an approved source (the AP). Multiple major outlets (Texas Tribune, NBC News, Brookings, BBC) corroborate a landslide Paxton victory. None of the N/A edge cases apply: the runoff occurred on schedule, featured both named candidates, and was not postponed beyond June 1.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-5. `f3c346a9-8b98-51a7-b357-b1ec25db0060`

- Present date: `2026-05-03 04:56:43.466492`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Figure AI announce a new commercial customer deployment (beyond BMW and Brookfield) for its humanoid robots between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 1, 2026, 00:00 UTC and June 1, 2026, 23:59 UTC, Figure AI publicly announces a new commercial customer deployment for its humanoid robots that meets ALL of the following criteria:

1. **New customer**: The customer must be a named entity other than BMW Group or Brookfield Asset Management (including their subsidiaries). This explicitly excludes any expansions or renewals of the existing BMW or Brookfield partnerships.

2. **Commercial customer**: The customer must be a for-profit entity engaging Figure AI robots for use in commercial operations (e.g., manufacturing, logistics, warehousing, retail). Pure research collaborations, academic partnerships, government-funded R&D programs, and investment-only relationships do not qualify.

3. **Deployment**: The announcement must indicate that Figure AI humanoid robots are being or will be physically deployed at the customer's facilities for operational use. A signed commercial contract or purchase order with a named delivery timeline qualifies. Letters of intent, memoranda of understanding, pilot feasibility studies without committed robot deliveries, and announcements limited to "exploring partnership opportunities" do not qualify.

4. **Announcement source**: The announcement must appear on Figure AI's official news page (https://www.figure.ai/news) OR be reported by at least one major credible news outlet (e.g., Reuters, Bloomberg, The Wall Street Journal, CNBC, AP News, Forbes, TechCrunch).

If no such announcement meeting all four criteria is identified by June 1, 2026, 23:59 UTC, the question resolves **No**.

**Primary resolution source**: Figure AI official news page at https://www.figure.ai/news

**Pre-cutoff background**

Figure AI is a leading humanoid robotics company that has developed multiple generations of humanoid robots, including the Figure 02 (F.02) and the newer Figure 03. As of April 2026, the company is actively ramping Figure 03 production at its BotQ high-volume manufacturing facility [News - Figure AI](https://www.figure.ai/news).

Figure AI's known commercial relationships include:
- **BMW**: Figure AI's first commercial customer. The F.02 robot contributed to the production of 30,000 cars at BMW Group Plant Spartanburg, as announced in November 2025 [News - Figure AI](https://www.figure.ai/news).
- **Brookfield**: A strategic partnership announced in September 2025, focused on developing real-world humanoid pretraining datasets and building AI infrastructure [News - Figure AI](https://www.figure.ai/news).

Figure AI CEO Brett Adcock has publicly stated that the company has signed a second commercial customer and sees potential for shipping 100,000 humanoid robots over the next four years. The company's AI model, Helix 02, introduced in January 2026, provides full-body autonomy controlled by a single neural system [News - Figure AI](https://www.figure.ai/news).

On April 29, 2026, Figure AI announced it is ramping Figure 03 production [News - Figure AI](https://www.figure.ai/news), suggesting the company is scaling toward broader commercial deployment. The question is whether a new, named commercial customer deployment—distinct from the existing BMW and Brookfield partnerships—will be formally announced during May 2026.

**Exact later resolution packet**

The question resolves YES.

On May 26, 2026 — within the resolution window of May 1, 2026 00:00 UTC to June 1, 2026 23:59 UTC — Figure AI published an announcement on its official news page (https://www.figure.ai/news/figure-signs-agreement-with-catalyst-brands) titled "Figure Signs Agreement with Catalyst Brands to Scale Humanoid Operations" [64e3c7, 68e565]. This was simultaneously announced via the Catalyst Brands / JCPenney corporate newsroom (https://corporate.jcpenney.com/2026/05/26/catalyst-brands-taps-figure-ai-for-humanoid-automation/) [8305d9].

Checking all four resolution criteria:

1. NEW CUSTOMER: Catalyst Brands is a named entity distinct from BMW Group and Brookfield Asset Management. Catalyst Brands is a retail holding company formed in January 2025 from the merger of SPARC Group and JCPenney, operating brands including JCPenney, Aéropostale, Brooks Brothers, Lucky Brand, and Nautica [8305d9]. While Brookfield (via Brookfield Corporation/Brookfield Property Partners) holds an equity stake, Catalyst Brands is a joint venture with multiple shareholders (Simon Property Group, Brookfield, Authentic Brands Group, and Shein) and is NOT a wholly-owned subsidiary of Brookfield Asset Management. It is a separate operating entity, satisfying the "new customer" requirement.

2. COMMERCIAL CUSTOMER: Catalyst Brands is a for-profit retail enterprise. The deployment is for commercial logistics operations (sorting/packing in its distribution network), satisfying this criterion [64e3c7, 8305d9].

3. DEPLOYMENT: The announcement explicitly states Figure will "deploy Figure humanoids into their distribution and logistics network," with an initial physical deployment at Catalyst Brands' Reno, Nevada Distribution Logistics Center, aiding the facility's Joey Pouch sorting system [64e3c7, 8305d9]. This is a signed commercial agreement with a concrete physical deployment site — not an MOU, LOI, or pilot feasibility study lacking committed deliveries.

4. ANNOUNCEMENT SOURCE: The announcement appears on Figure AI's official news page (the primary resolution source) and was reported by multiple outlets [64e3c7].

All four criteria are satisfied within the specified window, so the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-6. `3fd22636-7d1e-537d-816c-bb3603f02e72`

- Present date: `2026-05-13 23:03:36.738968`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-06-07T00:00:00`

**Question**

Will the French National Assembly adopt the 'Proposition de loi portant abrogation du Code noir' (n°1817) during its first reading on May 28, 2026?

**Resolution criteria**

This question resolves **Yes** if the Assemblée nationale adopts ("adopte") bill n°1817 in first reading ("première lecture") during the public session of May 28, 2026 (Central European Summer Time, UTC+2), as recorded on the official legislative dossier at https://www.assemblee-nationale.fr/dyn/17/dossiers/abrogation_code_noir.

"Adopt" means that the bill passes a vote in the National Assembly during its first reading — i.e., a majority of voting deputies vote in favor of the text as a whole (vote sur l'ensemble).

This question resolves **No** if any of the following occur:
- The bill is not reached during the May 28, 2026 session due to time constraints.
- The bill is blocked by a procedural motion such as a "renvoi en commission" (referral back to committee), a motion de rejet préalable, or any other procedural device that prevents a final vote on the text.
- The bill is put to a vote and rejected.
- The bill is withdrawn from the agenda.
- The session of May 28, 2026 does not take place.

If by June 7, 2026 (23:59 UTC) the official dossier shows no record of a vote on this bill during the May 28 session, the question resolves **No**.

**Pre-cutoff background**

The "Proposition de loi portant abrogation du Code noir" (n°1817) was deposited at the Assemblée nationale on September 16, 2025, by Deputy Max Mathiasin and others. It was referred to the Commission des lois [https://www.assemblee-nationale.fr/dyn/17/dossiers/abrogation_code_noir](https://www.assemblee-nationale.fr/dyn/17/dossiers/abrogation_code_noir). The bill aims to formally abrogate the "Code noir," a 17th-century royal decree that regulated slavery in French colonies. As of May 12, 2026, no committee vote or plenary vote has taken place [https://www.assemblee-nationale.fr/dyn/17/dossiers/abrogation_code_noir](https://www.assemblee-nationale.fr/dyn/17/dossiers/abrogation_code_noir).

The bill is scheduled for discussion in public session on Thursday, May 28, 2026, as part of a "niche parlementaire" (reserved parliamentary day) allocated to the LIOT group (Libertés, Indépendants, Outre-mer et Territoires). Niche parlementaire sessions have strictly limited floor time, and multiple bills from the same group compete for that time. PM Bayrou publicly pledged government support for abrogating the Code noir in May 2025.

Key uncertainties include: (1) whether the bill will actually be reached during the session given time constraints and the number of other texts scheduled; (2) whether procedural motions such as a "renvoi en commission" (referral back to committee) could block a final vote; and (3) the overall parliamentary arithmetic, though broad symbolic support is expected.

Resolution source: the Assemblée nationale's official legislative dossier for this bill at https://www.assemblee-nationale.fr/dyn/17/dossiers/abrogation_code_noir, which will record any vote outcome, and the official agenda/session records at https://www.assemblee-nationale.fr/dyn/seance-publique/textes-inscrits-ordre-du-jour.

**Exact later resolution packet**

The question resolves **YES**. The Assemblée nationale adopted bill n°1817 ("Proposition de loi portant abrogation du Code noir") in first reading (première lecture) during the public session of Thursday, May 28, 2026, via a vote on the text as a whole (vote sur l'ensemble).

Evidence:
- The official legislative dossier at https://www.assemblee-nationale.fr/dyn/17/dossiers/abrogation_code_noir explicitly records the text as adopted on Thursday, May 28, 2026, producing "Proposition de loi, adoptée par l'Assemblée nationale, portant abrogation du 'code noir' le 28 mai 2026, T.A. n° 290" [af3723]. The dossier shows no procedural motion (renvoi en commission, motion de rejet préalable, etc.) blocking the text on that date [af3723].
- The vote sur l'ensemble occurred in first reading (première lecture) in public session, not merely in committee. The parliamentary vote tracker Poligraph records the vote "l'ensemble de la proposition de loi portant abrogation du « code noir » — première lecture" dated 28 mai 2026 with 254 voters (https://poligraph.fr/parlement/votes/2026-05-28-l-ensemble-de-la-proposition-de-loi-portant-abrogation-du-code-noir-premiere-lecture). The official plenary "Compte rendu de la première séance du jeudi 28 mai 2026" (https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/premiere-seance-du-jeudi-28-mai-2026) references the adopted text T.A. n° 290. (Note: a separate committee/Commission des lois adoption occurred earlier on May 20, 2026, but the binding first-reading public-session vote was on May 28, 2026.)
- Multiple major, high-quality news outlets independently confirm the same outcome: Le Monde ("l'Assemblée nationale approuve à l'unanimité l'abrogation du Code noir," 28 May 2026), franceinfo, LCP, TF1 Info, and the government's own Vie-publique.fr, which states: "Le 28 mai 2026, l'Assemblée nationale a adopté, à l'unanimité et avec modifications, la proposition de loi en première lecture" (https://www.vie-publique.fr/loi/303397-abrogation-du-code-noir-proposition-de-loi-mathiasin).

Because the bill was reached, put to a vote sur l'ensemble in first reading, and adopted (unanimously) during the May 28, 2026 public session — with no blocking procedural motion — every YES condition is satisfied and none of the NO conditions apply.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-7. `d9d76db9-8595-57de-96b7-45cff90786ef`

- Present date: `2026-05-29 04:31:18.263413`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the UK-France small boat returns pilot scheme be formally extended or replaced by a new agreement before July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 and before July 1, 2026 (23:59 UTC), the UK government officially announces either:

1. A formal extension of the existing UK-France returns pilot scheme (the "Dangerous Journeys Agreement" that came into force on August 5, 2025), OR
2. A new bilateral agreement or treaty with France that includes a mechanism for returning Channel small boat arrivals from the UK to France.

The announcement must be made via at least one of the following:
- An official UK government publication on GOV.UK (https://www.gov.uk/)
- A formal parliamentary statement or written ministerial statement recorded in Hansard (https://hansard.parliament.uk/)
- An official treaty text published by the Foreign, Commonwealth and Development Office

The question resolves **No** if no such announcement is made by 23:59 UTC on June 30, 2026.

Note: The £662 million enforcement partnership announced on April 23, 2026 does NOT count unless it explicitly includes a returns mechanism (i.e., a provision allowing the UK to send Channel arrivals back to France). The question is specifically about the returns/swap component of the bilateral relationship, not upstream enforcement funding.

**Pre-cutoff background**

On August 5, 2025, the UK-France "one in, one out" asylum returns pilot scheme came into force, allowing the UK to return some Channel crossers to France in exchange for accepting an equal number of asylum seekers with UK family connections. The pilot was set to run until June 2026, after which both countries said they would assess its future. As of early 2026, 281 migrants had been removed under the deal according to the Home Secretary.

On April 23, 2026, the Home Secretary announced a £662 million multi-year partnership with France on small boat crossings, including extra police and enforcement measures. However, this deal focused on upstream enforcement rather than the returns mechanism specifically. The Guardian reported on March 30, 2026, that a new agreement on returns was delayed amid the Home Secretary's demands for more interceptions of dinghies.

Meanwhile, the cumulative total of Channel small boat arrivals since 2018 passed the 200,000 milestone on May 9, 2026, intensifying political pressure. Arrivals in 2026 are tracking approximately 36% below the same point in 2025, but the symbolic threshold has drawn significant attention. The total for 2025 was 41,472 — the second highest annual figure on record.

Parliamentary scrutiny of Channel crossings policy has been active, including an Oral Statement on "Illegal Migration: Small Boat Crossings" in the House of Commons on April 23, 2026, and a Lords question on the Cranston Inquiry Report on small boat deaths on March 25, 2026 [Small Boat Deaths: Cranston Inquiry Report - Hansard](https://hansard.parliament.uk/Lords/2026-03-25/debates/CEFE078B-2E7A-485D-B0E7-38378396BE84/SmallBoatDeathsCranstonInquiryReport). The political salience of the issue continues to rise with Reform UK's electoral gains.

**Exact later resolution packet**

The question resolves YES.

RESOLUTION CRITERIA: Resolves YES if, on or after May 12, 2026 and before July 1, 2026 (23:59 UTC), the UK government officially announces (via GOV.UK, Hansard, or an official FCDO treaty text) either (1) a formal extension of the UK-France returns pilot scheme (the "Dangerous Journeys Agreement" of Aug 5, 2025), OR (2) a new bilateral agreement/treaty with France that includes a returns mechanism for Channel small boat arrivals.

DECISIVE EVIDENCE:
- The Foreign, Commonwealth & Development Office published an official treaty text on GOV.UK titled "UK/France: Exchange of Letters amending and extending the Agreement on the Prevention of Dangerous Journeys [TS No.25/2026]." This document was published on 12 June 2026, and it explicitly amends and EXTENDS the Agreement on the Prevention of Dangerous Journeys — the treaty underpinning the "one in, one out" returns scheme that came into force on 5/6 August 2025 [UK/France: Exchange of Letters amending and extending the ...](https://www.gov.uk/government/publications/ukfrance-exchange-of-letters-amending-and-extending-the-agreement-on-the-prevention-of-dangerous-journeys-ts-no252026). Because it extends that agreement, it maintains the returns mechanism allowing the UK to return Channel small-boat arrivals to France [UK/France: Exchange of Letters amending and extending the ...](https://www.gov.uk/government/publications/ukfrance-exchange-of-letters-amending-and-extending-the-agreement-on-the-prevention-of-dangerous-journeys-ts-no252026). URL: https://www.gov.uk/government/publications/ukfrance-exchange-of-letters-amending-and-extending-the-agreement-on-the-prevention-of-dangerous-journeys-ts-no252026 (PDF: https://assets.publishing.service.gov.uk/media/6a2ace42d95ffddb05d4aef0/TS_25.2026_UK_France_Exchange_Letters_extending_Agreement_Prevention_Dangerous_Journeys.pdf).

This single official FCDO treaty publication, dated 12 June 2026 (within the required window of 12 May – 30 June 2026), satisfies criterion (1): a formal extension of the Dangerous Journeys Agreement, published via an official FCDO treaty text on GOV.UK, that retains the returns mechanism.

CORROBORATING EVIDENCE:
- The Guardian (22 June 2026) reported the UK and France agreed to extend the "one in, one out" scheme (originally due to end 11 June 2026) until 1 October 2026, and additionally amended the treaty to add a "returnee case" classification to stop deported migrants re-entering the UK [UK and France rewrite 'one in one out' treaty to stop removed ...](https://www.theguardian.com/uk-news/2026/jun/22/uk-and-france-rewrite-one-in-one-out-treaty-to-stop-removed-migrants-returning). This corroborates that the extension/amendment of the returns mechanism (not merely upstream enforcement) occurred in the window.
- These extension reports align with the June 12 FCDO Exchange of Letters as the underlying official instrument.

WHY OTHER ITEMS DO NOT CHANGE THE OUTCOME (but the YES still holds via the treaty text):
- The £662m partnership and the 30 June 2026 Home Office media blog focused on upstream enforcement (more police, surveillance, "taxi boat" tactics) and, per the resolution note, would NOT count on their own [Latest statement in response to small boat crossings](https://homeofficemedia.blog.gov.uk/2026/06/30/latest-statement-in-response-to-small-boat-crossings/). The 23 April 2026 GOV.UK "new UK-France agreement" was likewise upstream enforcement only, and predates the window regardless [https://www.gov.uk/government/news/new-uk-france-agreement-to-reduce-illegal-crossings](https://www.gov.uk/government/news/new-uk-france-agreement-to-reduce-illegal-crossings). However, the criteria are independently met by the FCDO Exchange of Letters treaty text [UK/France: Exchange of Letters amending and extending the ...](https://www.gov.uk/government/publications/ukfrance-exchange-of-letters-amending-and-extending-the-agreement-on-the-prevention-of-dangerous-journeys-ts-no252026).
- The House of Commons Library briefing (published 13 May 2026) predated the June extension and did not record it [Unauthorised migration: UK-France border cooperation](https://commonslibrary.parliament.uk/research-briefings/cbp-9681/), which is not dispositive given the later FCDO publication.

Because an official FCDO treaty text formally extending the Dangerous Journeys Agreement (with its returns mechanism intact) was published on GOV.UK on 12 June 2026 — within the required window — the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-8. `acab71ad-031c-53fd-85e2-9743575d627d`

- Present date: `2026-05-03 10:04:34.117998`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-05-31 00:00:00`

**Question**

Will the 79th World Health Assembly adopt a resolution extending the mandate to continue negotiations on the PABS Annex beyond May 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 2, 2026, and by 23:59 UTC on May 31, 2026, the 79th World Health Assembly (WHA79) formally adopts a resolution or decision that explicitly extends the negotiating mandate of the Intergovernmental Working Group (IGWG) — or any successor body — to continue negotiations on the Pathogen Access and Benefit-Sharing (PABS) Annex to the WHO Pandemic Agreement beyond May 2026.

This question resolves as **No** if:
- The WHA79 adopts the PABS Annex in full without extending any negotiating mandate; or
- The WHA79 concludes without adopting either the PABS Annex or a resolution extending the negotiating mandate; or
- No such resolution or decision is published by 23:59 UTC on May 31, 2026.

Key definitions:
- **79th World Health Assembly (WHA79):** The annual meeting of WHO member states, scheduled for May 18–23, 2026 in Geneva. See: https://www.who.int/about/governance/world-health-assembly/seventy-ninth
- **PABS Annex (Pathogen Access and Benefit-Sharing Annex):** The annex to the WHO Pandemic Agreement governing the sharing of pathogen samples and genetic sequence data, and the equitable distribution of benefits. See: https://www.who.int/health-topics/who-pandemic-agreement
- **Resolution extending the mandate:** A formal WHA resolution or decision that authorizes continued negotiations on the PABS Annex beyond the conclusion of WHA79, whether through the existing IGWG or a newly established body.

Resolution source: Official WHA79 resolutions and decisions published on the WHO governance documentation page at https://apps.who.int/gb/ebwha/pdf_files/WHA79/ or linked from https://www.who.int/about/governance/world-health-assembly/seventy-ninth.

**Pre-cutoff background**

The [WHO Pandemic Agreement](https://www.who.int/health-topics/who-pandemic-agreement) was adopted at the 78th World Health Assembly in May 2025, but a key component — the Pathogen Access and Benefit-Sharing (PABS) Annex — was left unfinished. The PABS system is intended to create a binding multilateral framework ensuring the rapid sharing of pathogens with pandemic potential and the fair and equitable sharing of benefits (such as vaccines, diagnostics, and therapeutics) arising from their use [Resumed sixth meeting of the Intergovernmental Working Group ...](https://www.who.int/news-room/events/detail/2026/04/27/default-calendar/resumed-sixth-meeting-of-the-intergovernmental-working-group-(igwg)-on-the-who-pandemic-agreement).

Resolution WHA78.1 established an open-ended Intergovernmental Working Group (IGWG) tasked with drafting and negotiating the PABS Annex [Resumed sixth meeting of the Intergovernmental Working Group ...](https://www.who.int/news-room/events/detail/2026/04/27/default-calendar/resumed-sixth-meeting-of-the-intergovernmental-working-group-(igwg)-on-the-who-pandemic-agreement). The IGWG held multiple negotiating sessions, with a resumed sixth meeting taking place from April 27 to May 1, 2026, intended to finalize text for submission to the 79th WHA [Resumed sixth meeting of the Intergovernmental Working Group ...](https://www.who.int/news-room/events/detail/2026/04/27/default-calendar/resumed-sixth-meeting-of-the-intergovernmental-working-group-(igwg)-on-the-who-pandemic-agreement).

As of May 2, 2026, negotiations remain deadlocked. Key points of contention include a proposed "hybrid" model — supported by the EU but opposed by the Africa Group — that would allow both mandatory and voluntary measures for sharing pathogen information and benefits [No Pandemic Agreement Annex By World Health Assembly, Says ...](https://healthpolicy-watch.news/no-pandemic-agreement-annex-by-world-health-assembly-says-civil-society/). Civil society observers have indicated that a final agreement on the PABS Annex is unlikely to be reached at WHA79 [No Pandemic Agreement Annex By World Health Assembly, Says ...](https://healthpolicy-watch.news/no-pandemic-agreement-annex-by-world-health-assembly-says-civil-society/). On March 28, 2026, WHO member states agreed to extend negotiations, with the stated objective of having an annex ready for consideration at WHA79, but without guaranteeing adoption [WHO Member States agree to extend negotiations on key annex to ...](https://www.who.int/news/item/28-03-2026-who-member-states-agree-to-extend-negotiations-on-key-annex-to-the-pandemic-agreement).

The 79th World Health Assembly ([WHA79](https://www.who.int/about/governance/world-health-assembly/seventy-ninth)) is scheduled for May 18–23, 2026, in Geneva, Switzerland. If the PABS Annex cannot be adopted in full, the WHA may instead pass a resolution extending the IGWG's negotiating mandate to continue work beyond May 2026.

**Exact later resolution packet**

YES. The qualifying act was a formal WHA79 decision, not a resolution: Decision WHA79(7), “Outcome of the open-ended Intergovernmental Working Group on the WHO Pandemic Agreement in relation to the drafting and negotiation of the Annex described in Article 12 of the WHO Pandemic Agreement,” published at https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_%287%29-en.pdf and listed in the official WHA79 documentation repository linked from the WHA79 landing page [https://www.who.int/about/governance/world-health-assembly/seventy-ninth](https://www.who.int/about/governance/world-health-assembly/seventy-ninth) [https://apps.who.int/gb/e/e_wha79.html](https://apps.who.int/gb/e/e_wha79.html). The queried official decision text states that WHA79 adopted Decision WHA79(7) on May 22, 2026, and that it “DECIDED that the IGWG shall continue its work as mandated in paragraph 9(1) of resolution WHA78.1” and, “as a priority, draft and negotiate the Annex described in Article 12 of the WHO Pandemic Agreement,” with the outcome to be submitted to the Eightieth World Health Assembly or earlier to a special session in 2026 [https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_%287%29-en.pdf](https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_%287%29-en.pdf). Article 12 is the Pathogen Access and Benefit-Sharing (PABS) Annex context: the related official WHA79 document A79/8 states that the IGWG submitted an on-screen draft PABS Annex text that was “not final agreed text,” and included draft decision language for the IGWG to continue drafting and negotiating the Annex described in Article 12 for submission to WHA80 [[PDF] Open-ended Intergovernmental Working Group on the WHO ...](https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_8-en.pdf). Thus, the PABS Annex was not adopted in full at WHA79; instead, WHA79 formally adopted a decision during May 18–23, 2026, published before May 31, 2026, explicitly continuing the IGWG negotiating mandate beyond May 2026 [https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_%287%29-en.pdf](https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_%287%29-en.pdf) [[PDF] Open-ended Intergovernmental Working Group on the WHO ...](https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_8-en.pdf). This satisfies the question’s YES criteria. I distinguish this from a WHA resolution: the operative instrument is Decision WHA79(7), i.e. a WHA79 decision, which the criteria expressly count as sufficient [https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_%287%29-en.pdf](https://apps.who.int/gb/ebwha/pdf_files/WHA79/A79_%287%29-en.pdf).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-9. `15422167-f6bd-50d5-96db-943773bc45e5`

- Present date: `2026-05-02 15:36:47.584970`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the Idaho Department of Water Resources (IDWR) issue a new curtailment order affecting water rights in the Eastern Snake Plain Aquifer (ESPA) area between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026 (Mountain Time), and on or before June 1, 2026, at 11:59 PM Mountain Time, the Idaho Department of Water Resources (IDWR) issues (i.e., formally signs and publishes) one or more new curtailment orders affecting water rights in the Eastern Snake Plain Aquifer (ESPA) management area (Water District 120 or conjunctive management areas administered under IDWR's CM Rules, Idaho Administrative Code IDAPA 37.03.11).

Key definitions:
- **"Curtailment order"**: A formal written administrative order issued by the IDWR Director pursuant to Idaho Code §§ 42-237a.g or 42-602, or under IDWR's Rules for Conjunctive Management of Surface and Ground Water Resources (IDAPA 37.03.11), directing specific water right holders to cease or reduce diversions to satisfy senior water rights. This excludes voluntary mitigation agreements, stipulated plans, or stays of existing orders.
- **"New"**: The order must be issued (signed by the IDWR Director) on or after May 1, 2026, Mountain Time. Orders issued before May 1, 2026 (including the existing Big Lost/Little Lost basin curtailment orders from April 2026 and earlier) do not count, even if they remain in effect during the resolution window. Modifications or amendments to pre-existing orders that materially expand the geographic scope or number of water rights curtailed do qualify.
- **"ESPA management area"**: The Eastern Snake Plain Aquifer area as defined in the ESPA Comprehensive Aquifer Management Plan and administered by IDWR, generally encompassing groundwater rights in Water District 120 and associated surface water delivery calls.

The question resolves **No** if no such new curtailment order is issued during the specified period.

**Resolution source**: The IDWR Curtailment Notices and Orders page (https://idwr.idaho.gov/legal-actions/curtailments/) [Curtailment Notices and Orders | Idaho Department of Water ...](https://idwr.idaho.gov/legal-actions/curtailments/), IDWR news releases (https://idwr.idaho.gov/), or official administrative orders published on the IDWR legal actions page (https://idwr.idaho.gov/legal-actions/). If the IDWR website is temporarily unavailable, credible reporting from Capital Press, Idaho Statesman, East Idaho News, or Boise State Public Radio may serve as secondary sources.

**Pre-cutoff background**

On April 13, 2026, Idaho Governor Brad Little and IDWR Director Mathew Weaver declared a statewide drought emergency covering all 44 Idaho counties, following the second-warmest winter on record since 1896 [Idaho under emergency drought after 'extraordinary' warm winter](https://www.boisestatepublicradio.org/environment/2026-04-16/severe-drought-declaration-idaho-west-water-supplies). Idaho's statewide snowpack peaked on March 17, 2026, at just 68% of normal—approximately three weeks earlier than typical—with 2026 setting new historic lows for April snow course measurements at 30 of 57 sites above the Snake River at King Hill [[PDF] Snowpack & Water Supply Update - Idaho.gov](https://idwr.idaho.gov/wp-content/uploads/sites/2/iwrb/2026/Ops%20Meeting%2020260409/Materials_20260409.pdf). As of April 9, 2026, Upper Snake reservoir storage stood at 3.07 million acre-feet (MAF), or 76% of capacity, which is 407,000 acre-feet lower than the same time in 2025 [[PDF] Snowpack & Water Supply Update - Idaho.gov](https://idwr.idaho.gov/wp-content/uploads/sites/2/iwrb/2026/Ops%20Meeting%2020260409/Materials_20260409.pdf). Basin-specific shortages are severe: the Salmon Falls Creek basin is 58% short, the Big Wood basin 53% short, and the Oakley basin 44% short, while the area along the Idaho-Nevada border had "little to no snowpack" [Idaho under emergency drought after 'extraordinary' warm winter](https://www.boisestatepublicradio.org/environment/2026-04-16/severe-drought-declaration-idaho-west-water-supplies).

The April 2026 drought declaration enables emergency transfers of water rights (allowing canal companies and farmers to consolidate and redirect water without standard paperwork) and assists with eligibility for federal drought assistance [Idaho under emergency drought after 'extraordinary' warm winter](https://www.boisestatepublicradio.org/environment/2026-04-16/severe-drought-declaration-idaho-west-water-supplies). However, it does not itself mandate curtailment of water diversions. As of late April 2026, IDWR had already issued curtailment orders in the Big Lost and Little Lost river basins affecting groundwater users who failed to join approved mitigation plans by the November 2025 deadline. The Idaho Ground Water Appropriators (IGWA) and Surface Water Coalition have been actively negotiating mitigation plans to stave off broader curtailment across the Eastern Snake Plain Aquifer (ESPA) area, which supplies water to roughly one million acres of irrigated farmland. The 2026 runoff forecast for the Snake River above King Hill is only 38% of normal [[PDF] Snowpack & Water Supply Update - Idaho.gov](https://idwr.idaho.gov/wp-content/uploads/sites/2/iwrb/2026/Ops%20Meeting%2020260409/Materials_20260409.pdf), raising the prospect of additional curtailment orders as the irrigation season intensifies in May.

The IDWR maintains an official curtailment notices and orders page at https://idwr.idaho.gov/legal-actions/curtailments/ [Curtailment Notices and Orders | Idaho Department of Water ...](https://idwr.idaho.gov/legal-actions/curtailments/), and publishes news releases and administrative orders on its main website at https://idwr.idaho.gov/.

**Exact later resolution packet**

The question resolves YES.

On May 14, 2026 — within the resolution window of May 1 to June 1, 2026 — IDWR Director Mathew Weaver signed and issued a final order curtailing junior groundwater rights drawing from the Eastern Snake Plain Aquifer (ESPA). This is confirmed by three independent, credible sources, all of which the resolution criteria explicitly authorize as secondary sources:

- Capital Press ("Eastern Snake curtailment order updated," May 18, 2026) reports that "the director's May 14 final order means groundwater users who draw water from the Eastern Snake Plain Aquifer with a priority date junior to October 11, 1900" face curtailment if not covered by an IDWR-approved mitigation plan. The article names IDWR Director Mathew Weaver as the signatory [Eastern Snake curtailment order updated | Capital Press](https://capitalpress.com/2026/05/18/eastern-snake-curtailment-order-updated/).

- Idaho News / CBS2 (KBOI), May 14, 2026, "IDWR orders curtailment of junior ESPA groundwater rights amid Snake River shortfall," confirms Director Weaver issued the order on May 14, 2026, applying to ESPA groundwater users with priority dates junior to October 11, 1900, following a finding of a projected 181,600 acre-foot shortfall for senior surface water users for the 2026 irrigation season [IDWR orders curtailment of junior ESPA groundwater rights amid ...](https://idahonews.com/news/local/idwr-orders-curtailment-of-junior-espa-groundwater-rights-amid-snake-river-shortfall).

- East Idaho News ("Curtailment order targets 924 groundwater rights across eastern Idaho") reports the order affects 924 individual ESPA-area groundwater rights and is now in effect [Curtailment order targets 924 groundwater rights across eastern Idaho](https://www.eastidahonews.com/2026/05/curtailment-order-targets-924-groundwater-rights-across-eastern-idaho/).

The order satisfies every checklist requirement:
- It was formally signed by the IDWR Director (Mathew Weaver) and published within the window (May 14, 2026) [Eastern Snake curtailment order updated | Capital Press](https://capitalpress.com/2026/05/18/eastern-snake-curtailment-order-updated/)[IDWR orders curtailment of junior ESPA groundwater rights amid ...](https://idahonews.com/news/local/idwr-orders-curtailment-of-junior-espa-groundwater-rights-amid-snake-river-shortfall).
- It specifically affects ESPA-area water rights (groundwater users drawing from the Eastern Snake Plain Aquifer / ESPA area of common groundwater supply), not merely the Big Lost/Little Lost basins [Eastern Snake curtailment order updated | Capital Press](https://capitalpress.com/2026/05/18/eastern-snake-curtailment-order-updated/)[Curtailment order targets 924 groundwater rights across eastern Idaho](https://www.eastidahonews.com/2026/05/curtailment-order-targets-924-groundwater-rights-across-eastern-idaho/).
- It is a formal administrative curtailment order directing junior groundwater users to cease/reduce diversions (or be covered by an approved mitigation plan), and is distinct from the voluntary mitigation agreements it references; it is the enforcement order arising from the Surface Water Coalition conjunctive-management delivery call, not a stipulation or stay [IDWR orders curtailment of junior ESPA groundwater rights amid ...](https://idahonews.com/news/local/idwr-orders-curtailment-of-junior-espa-groundwater-rights-amid-snake-river-shortfall)[Curtailment order targets 924 groundwater rights across eastern Idaho](https://www.eastidahonews.com/2026/05/curtailment-order-targets-924-groundwater-rights-across-eastern-idaho/).
- It is a new 2026-season curtailment order responding to the projected shortfall, materially distinct from the pre-May Big Lost/Little Lost orders and the April 2026 drought declaration [IDWR orders curtailment of junior ESPA groundwater rights amid ...](https://idahonews.com/news/local/idwr-orders-curtailment-of-junior-espa-groundwater-rights-amid-snake-river-shortfall)[Curtailment order targets 924 groundwater rights across eastern Idaho](https://www.eastidahonews.com/2026/05/curtailment-order-targets-924-groundwater-rights-across-eastern-idaho/).

Note: The official IDWR Curtailment Notices & Orders page I queried did not list a May 2026 entry, and the Surface Water Coalition Delivery Call legal-actions page appeared last updated April 16, 2026, so the official IDWR pages were not fully current at query time [https://idwr.idaho.gov/legal-actions/curtailments/](https://idwr.idaho.gov/legal-actions/curtailments/)[Surface Water Coalition Delivery Call](https://idwr.idaho.gov/delivery-call-action/surface-water-coalition-delivery-call/). However, the resolution criteria explicitly allow Capital Press, East Idaho News, and Boise State Public Radio as secondary sources when relying on news reporting, and three such credible outlets independently and consistently confirm the May 14, 2026 ESPA curtailment order signed by the Director.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-10. `442a44a9-fcca-5d4d-b31d-87a4b40ff000`

- Present date: `2026-05-16 03:13:09.191376`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-06-25T00:00:00`

**Question**

Will the Strait of Hormuz be open to commercial shipping on June 25, 2026?

**Resolution criteria**

This question resolves **Yes** if, on June 25, 2026 (00:00–23:59 UTC), the Strait of Hormuz (the waterway between Iran and Oman at approximately 26°34'N, 56°15'E, as defined by [Wikipedia](https://en.wikipedia.org/wiki/Strait_of_Hormuz)) is open to commercial shipping. "Open to commercial shipping" is defined as meeting **both** of the following conditions:

1. **No active NAVAREA IX warning** (issued by the [National Geospatial-Intelligence Agency](https://msi.nga.mil/NavWarnings) or the relevant NAVAREA coordinator) is in effect that advises all commercial vessels to avoid transit through the Strait of Hormuz due to military operations or a blockade; **AND**
2. **At least one IMO-registered merchant vessel** (oil tanker, LNG carrier, container ship, or bulk carrier, as classified under [IMO ship types](https://www.imo.org/)) has completed a transit through the Strait of Hormuz within the 72-hour window ending at 23:59 UTC on June 25, 2026, as confirmed by vessel-tracking data or credible reporting.

"Commercial shipping" refers to IMO-registered merchant vessels engaged in trade, excluding warships, government vessels, and vessels operating exclusively under military escort with no commercial cargo.

**Resolution sources:** The question will be resolved based on reporting from at least one of the following:
- [Lloyd's List](https://www.lloydslist.com/) shipping intelligence
- [Reuters](https://www.reuters.com/) or [Associated Press](https://apnews.com/) news reporting
- [Bloomberg](https://www.bloomberg.com/) shipping or energy reporting
- U.S. Fifth Fleet press releases ([https://www.cusnc.navy.mil/](https://www.cusnc.navy.mil/))
- NAVAREA IX warnings via [NGA Maritime Safety Information](https://msi.nga.mil/NavWarnings)

If the above sources provide conflicting information, Lloyd's List vessel-tracking data takes precedence.

**Pre-cutoff background**

The Strait of Hormuz (approximately 26°34'N, 56°15'E; the narrow waterway between Iran and Oman connecting the Persian Gulf to the Gulf of Oman, as defined by the [IHO](https://iho.int/) and [Wikipedia](https://en.wikipedia.org/wiki/Strait_of_Hormuz)) is a critical maritime chokepoint through which roughly one-fifth of the world's oil supply transits.

Following the outbreak of the 2026 Iran war on February 28, 2026, the Strait has been "all but closed" to commercial traffic [US, Iran clash in Hormuz as war escalates - Al Jazeera](https://www.aljazeera.com/news/2026/5/8/us-iran-clash-in-hormuz-as-war-escalates-what-happened-why-it-matters). Iran closed the Strait on March 4, 2026, and it was temporarily reopened during a two-week ceasefire announced on April 7–8, 2026 [https://en.wikipedia.org/wiki/Economic_impact_of_the_2026_Iran_war](https://en.wikipedia.org/wiki/Economic_impact_of_the_2026_Iran_war). The United States initiated a naval blockade of Iranian ports on April 13, 2026, and as of May 8, 2026, U.S. forces had prevented over 70 tankers from entering or leaving Iranian ports [Iran War Shipping Update - MAY 8, 2026 | UANI](https://www.unitedagainstnucleariran.com/blog/iran-war-shipping-update-may-8-2026). Despite the ceasefire nominally remaining in effect, clashes between U.S. and Iranian forces occurred on May 7–8, 2026 [US, Iran clash in Hormuz as war escalates - Al Jazeera](https://www.aljazeera.com/news/2026/5/8/us-iran-clash-in-hormuz-as-war-escalates-what-happened-why-it-matters), and as of May 12, 2026, President Trump described the ceasefire as being "on life support." Iran continues to frame control over the Strait as a key strategic interest, and peace negotiations over reopening the Strait remain unresolved. On May 12, 2026, CNBC reported that the U.S. may have to open the Strait by force.

The situation is highly volatile: the Strait could reopen through a peace deal or military action, or remain closed if negotiations fail and hostilities continue.

**Exact later resolution packet**

The question resolves YES because BOTH defined conditions for the Strait of Hormuz being "open to commercial shipping" on June 25, 2026 (00:00–23:59 UTC) were satisfied, based on the specified resolution sources.

CONDITION 1 — No active NAVAREA IX warning advising ALL commercial vessels to avoid transit due to military operations or a blockade: MET.
The active NAVAREA IX warnings in effect on June 25, 2026 (per NGA-sourced NAVAREA IX data mirrored on SeaLagom) were: 210/26 (container ship Ever Lovely security incident — "navigate with caution"), 208/26 (Oman/IMO temporary traffic regime with two temporary routes north/south of the TSS), 201/26 and 180/26 (confirmed/suspected mine — "navigate with extreme caution"), 173/26 (missing buoys), 113/26 (sunk container ship), and 095/26 (bulk carrier fire — caution) [0dc545]. None of these advises ALL commercial vessels to avoid transit due to military operations or a blockade; on the contrary, 208/26 established a managed/phased transit regime facilitating transits [0dc545, a77451]. The JMIC/UKMTO Advisory Note Update 063 (dated June 25, 2026) likewise characterizes 208/26 as a "temporary traffic regime" enabling phased transits, not an avoidance order [a77451].

Note on a potential counterargument: Iran's IRGC declared the strait "closed" (June 20) and issued statements restricting routes around June 25, and a UN agency paused seafarer evacuations on June 25 after a vessel was struck [a242af]. However, the resolution criteria are literal: Condition 1 hinges specifically on a NAVAREA IX warning (issued by NGA or the NAVAREA coordinator), not on Iranian declarations or a UN evacuation pause. No such NAVAREA IX blanket-avoidance/blockade warning was in force [0dc545].

CONDITION 2 — At least one IMO-registered merchant vessel (oil tanker, LNG carrier, container ship, or bulk carrier) completed a transit within the 72-hour window ending 23:59 UTC June 25 (i.e., June 23–25): MET.
The JMIC/UKMTO Advisory Note Update 063 reported continuing commercial transits via both the southern Omani corridor and the northern route, with a transit annex showing 30 cargo-vessel transits and 24 tanker transits on June 24, 2026 alone [a77451]. Lloyd's List — which takes precedence under the resolution criteria — reported on June 26, 2026 that "Ships keep moving through Hormuz despite strike and suspension of IMO [exit strategy]," confirming merchant vessels continued transiting through this period [dff540]. NAVAREA IX 210/26 additionally documents container ship Ever Lovely continuing its voyage through the strait on June 25 [0dc545]. Surrounding context corroborates heavy merchant traffic: Bloomberg/Kpler reported ~37+ commodity carriers (AXSMarine: 42 crossings incl. container ships) on June 22 [bd7497], and Reuters documented numerous named tankers, Qatari LNG carriers (Wadi Al Sail, Mekaines, Al Sadd, Mesaimeer) and a dry-bulk carrier (Summit Success) transiting around June 20–22 [462249].

Because there was no qualifying NAVAREA IX avoidance/blockade warning AND multiple IMO-registered merchant vessels completed transits within the 72-hour window, the strait met the question's definition of "open to commercial shipping" on June 25, 2026. Resolution: YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-11. `c8bfecd4-d906-5331-b98c-62a73ed87f14`

- Present date: `2026-05-29 02:19:59.310136`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Moody's or S&P upgrade Argentina's sovereign credit rating between May 12, 2026 and July 1, 2026?

**Resolution criteria**

This question resolves **YES** if either Moody's Investors Service or S&P Global Ratings announces an upgrade to Argentina's Long-Term Foreign Currency sovereign credit rating on or after May 12, 2026 and before 23:59 UTC on July 1, 2026. It resolves **NO** otherwise.

**Definition of "upgrade":** A move upward by at least one notch on the agency's respective credit rating scale. For Moody's, this means a change from Caa1 to B3 or higher. For S&P, this means a change from CCC+ to B- or higher. Changes solely to the outlook (e.g., from Stable to Positive) without a notch change do **not** constitute an upgrade.

**Why the May 12, 2026 cutoff:** Fitch's upgrade to B- on May 5, 2026 is excluded from resolution. Only rating actions announced on or after May 12, 2026 count.

**Resolution sources:**
- Moody's Ratings press releases: https://ratings.moodys.com/ratings-news/447174 (example of prior Argentina action; new actions will appear at https://ratings.moodys.com/)
- S&P Global Ratings: https://www.spglobal.com/ratings/en/ (press releases and rating actions)
- Fitch Ratings Argentina page: https://www.fitchratings.com/entity/argentina-80442219

Note: A further Fitch upgrade (beyond the May 5 B- action) announced on or after May 12, 2026 would **not** count for resolution — only Moody's or S&P actions qualify, as the question specifically targets convergence by the lagging agencies.

**Pre-cutoff background**

On May 5, 2026, Fitch Ratings upgraded Argentina's Long-Term Foreign Currency Issuer Default Rating (IDR) to 'B-' from 'CCC+' with a stable outlook, citing structurally improved fiscal and external balances and progress on economic reforms under President Milei [Argentina's Fitch upgrade seen opening narrow window for debt sale](https://www.batimes.com.ar/news/economy/argentinas-fitch-upgrade-seen-opening-narrow-window-for-debt-sale.phtml). This was the first Fitch upgrade for Argentina in eight years.

As of May 13, 2026, Argentina's sovereign credit ratings from the three major agencies are:
- **Fitch**: B- (Stable outlook) — upgraded May 5, 2026 [Argentina's Fitch upgrade seen opening narrow window for debt sale](https://www.batimes.com.ar/news/economy/argentinas-fitch-upgrade-seen-opening-narrow-window-for-debt-sale.phtml)
- **Moody's**: Caa1 (Stable outlook) — last changed July 2025 [Credit Rating - Argentina - Trading Economics](https://tradingeconomics.com/argentina/rating)
- **S&P**: CCC+ (Stable outlook) — last changed December 17, 2025 [Credit Rating - Argentina - Trading Economics](https://tradingeconomics.com/argentina/rating)

Both Moody's and S&P rate Argentina significantly below Fitch. The gap between Fitch's B- and Moody's Caa1/S&P CCC+ creates potential for convergence, though rating agencies often move on different timelines. Argentina's IMF program, ongoing fiscal consolidation, and FX reserve accumulation under Milei's reforms provide a backdrop that could support further upgrades, but the stable outlooks at both Moody's and S&P suggest neither agency sees an imminent upgrade as their base case. The short window (approximately 7 weeks) makes a follow-on upgrade plausible but uncertain.

**Exact later resolution packet**

The question resolves YES.

**Resolution criteria:** Resolves YES if Moody's or S&P announces an upgrade (at least one notch) to Argentina's Long-Term Foreign Currency sovereign credit rating on or after May 12, 2026 and before 23:59 UTC on July 1, 2026. Fitch actions do not count; outlook-only changes do not count.

**Finding:** On June 10, 2026, S&P Global Ratings raised its long- and short-term local and foreign currency sovereign credit ratings on Argentina to 'B-/B' from 'CCC+/C', with a stable outlook on the long-term ratings. This is a one-notch upgrade of the Long-Term Foreign Currency rating (CCC+ → B-), performed by S&P (not Fitch), on June 10, 2026 — within the required window (May 12 – July 1, 2026).

**Evidence:**
- The Buenos Aires Times article confirms: "Credit ratings agency S&P Global upgraded Argentina's sovereign credit rating to 'B-' on Wednesday [June 10, 2026]... raised both its short- and long-term local and foreign currency ratings from 'CCC+/C' to 'B-/B'" [Caputo cheers as S&P upgrades Argentina's debt rating to 'B-'](https://www.batimes.com.ar/news/economy/caputo-cheers-as-s.phtml).
- S&P Global Ratings official page (https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3578437), titled "Argentina Long-Term Ratings Raised To 'B-'", states in the Google-indexed snippet: "On June 10, 2026, S&P Global Ratings raised its long- and short-term local and foreign currency sovereign credit ratings on Argentina to 'B-/B' from 'CCC+/C'. The outlook on the long-term ratings is stable."
- Corroborated by Reuters, Bloomberg ("Argentina Rating Raised to B- by S&P"), LatinFinance, and Trading Economics/theglobaleconomy.com, which list S&P's Argentina rating as B- (Stable) with date 6/2026.

This is a genuine notch upgrade (not merely an outlook change), by a qualifying agency (S&P), within the qualifying window. Therefore the question resolves YES.

Note: An automated read of the S&P regulatory page returned no content (paywalled/JS-rendered), producing a spurious "NO" from that single tool call, but the S&P press-release title/snippet and multiple independent high-quality news sources (Reuters, Bloomberg, Buenos Aires Times) all confirm the June 10, 2026 upgrade.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-12. `658805d0-23e8-5df3-a2f1-f618addff9ae`

- Present date: `2026-05-14 11:35:48.969369`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Spanish Supreme Court convict José Luis Ábalos on the 'criminal organization' charge in the Caso Koldo verdict?

**Resolution criteria**

This question resolves **Yes** if the Spanish Supreme Court issues a verdict on or after May 12, 2026, and no later than July 1, 2026, that explicitly convicts José Luis Ábalos of the crime of "criminal organization" (organización criminal) under Article 570 bis of the Spanish Penal Code (https://www.boe.es/buscar/act.php?id=BOE-A-1995-25444#a570bis). This charge is distinct from other potential convictions in the Caso Koldo, such as bribery (cohecho) or influence peddling (tráfico de influencias).

This question resolves **No** if:
1. The court acquits Ábalos of the criminal organization charge specifically, even if he is convicted on other charges; or
2. No verdict is issued by July 1, 2026.

The resolution source shall be the official sentence as published on the Spanish Judiciary's portal (Poder Judicial, https://www.poderjudicial.es/), or, if not yet published there, confirmed reporting from at least two of the following credible Spanish news sources: El País (https://elpais.com/), El Confidencial (https://www.elconfidencial.com/), RTVE (https://www.rtve.es/), El Mundo (https://www.elmundo.es/).

**Pre-cutoff background**

The Caso Koldo is a major corruption case in Spain involving alleged illicit activities in government procurement of face masks during the COVID-19 pandemic. Former Transport Minister José Luis Ábalos, his former advisor Koldo García, and businessman Víctor de Aldama are the main defendants. The trial at the Spanish Supreme Court (Tribunal Supremo) has concluded, and as of May 12, 2026, the case is "visto para sentencia" (submitted for judgment), with the court actively deliberating [Ábalos, a la espera de sentencia: dinero y favores bajo la lupa del ...](https://elpais.com/espana/2026-05-10/abalos-a-la-espera-de-sentencia-dinero-y-favores-bajo-la-lupa-del-supremo.html).

The prosecution, led by the Fiscalía Anticorrupción, has built its case around the allegation that Ábalos led a "criminal organization" (organización criminal) as defined under Article 570 bis of the Spanish Penal Code (Código Penal). Under this article (https://www.boe.es/buscar/act.php?id=BOE-A-1995-25444#a570bis), a criminal organization is defined as a stable, hierarchically structured association of at least three persons, coordinated over an indefinite period, with the purpose of committing serious crimes [Criminal Organization Membership Charges | Defense Lawyer](https://victoravilaabogado.com/en/criminal-organization-membership-charges/). Ábalos faces up to 24 years in prison across all charges [057b81].

The Supreme Court has signaled its intention to issue a swift, unanimous verdict before the summer of 2026 [El Supremo busca una sentencia exprés y unánime que deje claro ...](https://www.elconfidencial.com/espana/2026-05-07/supremo-busca-sentencia-expres-unanime-trama-criminal-mascarillas-gobierno_4350890/). The criminal organization charge is the most aggressive legal characterization pursued by the prosecution; Spanish courts have historically sometimes convicted defendants on underlying corruption offenses (e.g., bribery, influence peddling) while rejecting the broader "criminal organization" framing [Ábalos, a la espera de sentencia: dinero y favores bajo la lupa del ...](https://elpais.com/espana/2026-05-10/abalos-a-la-espera-de-sentencia-dinero-y-favores-bajo-la-lupa-del-supremo.html). This makes the outcome of this specific charge genuinely uncertain.

**Exact later resolution packet**

The question resolves YES.

The Spanish Supreme Court (Sala Segunda del Tribunal Supremo) issued its verdict in the "Caso Koldo"/"Caso Mascarillas" on June 22, 2026 — squarely within the resolution window of May 12, 2026 to July 1, 2026.

The official resolution source (the Spanish Judiciary portal, Poder Judicial) confirms the verdict explicitly convicts José Luis Ábalos of "organización criminal" (criminal organization) — the exact charge in question — alongside cohecho (bribery), malversación (embezzlement), and tráfico de influencias (influence peddling). The official press release is titled "El Tribunal Supremo condena al exministro José Luis Ábalos y a su exasesor Koldo García a 24 años y 19 años de prisión, respectivamente, por delitos de organización criminal, cohecho, malversación y tráfico de influencias" [9d5ce5]. Ábalos received 24 years and 3 months in prison.

This is independently corroborated by at least two of the specified news outlets:
- RTVE: "El Tribunal Supremo ha condenado al exministro... José Luis Ábalos a 24 años y tres meses de prisión... por los delitos de organización criminal, cohecho, malversación y tráfico de influencias"; the unanimous ruling concluded the three defendants "constituyeron una organización, en la que cada uno de ellos asumió un papel diverso y complementario" [8fbc4c].
- El Mundo: "Ábalos y Koldo han sido condenados por delitos de organización criminal, cohechos, malversación y tráfico de influencias" and the ruling "considera que los tres acusados formaron una organización criminal con reparto de funciones que cometió graves delitos de corrupción" [21da71].

Because the court explicitly convicted Ábalos on the specific "organización criminal" (Article 570 bis) charge, in a verdict issued within the specified window, the question resolves YES (1).

URLs for evidence:
- Poder Judicial official press release: https://www.poderjudicial.es/cgpj/es/Poder-Judicial/Tribunal-Supremo/Oficina-de-Comunicacion/Notas-de-prensa/El-Tribunal-Supremo-condena-al-exministro-Jose-Luis-Abalos-y-a-su-exasesor-Koldo-Garcia-a-24-anos-y-19-anos-de-prision--respectivamente--por-delitos-de-organizacion-criminal--cohecho--malversacion-y-trafico-de-influencias [9d5ce5]
- RTVE: https://www.rtve.es/noticias/20260622/sentencia-supremo-caso-mascarillas-abalos-koldo/17108722.shtml [8fbc4c]
- El Mundo: https://www.elmundo.es/espana/2026/06/22/6a38dae6fdddffed398b4578.html [21da71]

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-13. `a27193ba-4066-52fc-829e-7b3702351118`

- Present date: `2026-05-18 13:32:34.529461`
- Source cutoff boundary: `2026-05-19` (encodes end of UTC day `2026-05-18`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will any German Bundesland announce new formal guidelines or regulations on constitutional loyalty (Verfassungstreue) for civil servants between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (00:00 UTC) and before July 1, 2026 (23:59 UTC), any of the 16 German federal states (Bundesländer) officially announces or publishes a **new** formal guideline or regulation specifically addressing constitutional loyalty (Verfassungstreue) requirements for civil servants (Beamte). "New" means not previously in effect before May 12, 2026.

A "formal guideline or regulation" is defined as any of the following:
1. A new law or ordinance published in the respective state's official gazette (*Gesetz- und Verordnungsblatt*);
2. An official, binding administrative directive (*Verwaltungsvorschrift*), decree (*Erlass*), or circular (*Rundschreiben*) issued by a state ministry and publicly announced via an official government press release or government website;
3. A formal cabinet decision (*Kabinettsbeschluss*) establishing new binding rules, as announced on the state government's official website.

The following do **not** qualify: informal political statements, coalition agreement pledges, draft bills not yet enacted, parliamentary motions, or press interviews expressing intent without a binding administrative or legislative act.

**Resolution sources:** Official state government websites and gazettes; credible German legal news outlets such as [Legal Tribune Online (LTO)](https://www.lto.de/), [beck-aktuell](https://www.beck-aktuell.de/), [Haufe Öffentlicher Dienst](https://www.haufe.de/oeffentlicher-dienst/), or major outlets such as [Tagesschau](https://www.tagesschau.de/), [FAZ](https://www.faz.net/), or [Der Spiegel](https://www.spiegel.de/).

**Pre-cutoff background**

In Germany, civil servants ([Beamte](https://en.wikipedia.org/wiki/Beamter)) are bound by a duty of constitutional loyalty ([Verfassungstreue](https://de.wikipedia.org/wiki/Verfassungstreue)), requiring them to uphold the free democratic basic order (freiheitliche demokratische Grundordnung). Following the Federal Office for the Protection of the Constitution's (BfV) classification of the AfD as a proven extremist organization in 2025, multiple German states have taken steps to tighten screening of civil service applicants and enforce loyalty requirements.

As of May 2026, the following states have already implemented notable measures:

- **Saxony (Sachsen):** In March 2024, the Saxon parliament passed a law on Verfassungstreue in public service, requiring checks with the State Office for the Protection of the Constitution (Landesamt für Verfassungsschutz) before appointing police and judicial employees as civil servants [Staatsdienst: Sachsen fragt nicht nach Parteizugehörigkeit | MDR.DE](https://www.mdr.de/nachrichten/sachsen/afd-mitgliedschaft-staatsdienst-rechtsextremismus-100.html).
- **Rhineland-Palatinate (Rheinland-Pfalz):** Added the AfD to a list of over 100 extremist or extremist-influenced organizations used for individual case-by-case screening of civil service applicants. The state also pursued legislation to accelerate disciplinary proceedings against civil servants lacking Verfassungstreue [Bundesländer verschärfen Prüfung von AfD-Bewerbern - Haufe](https://www.haufe.de/oeffentlicher-dienst/personal-tarifrecht/bundeslaender-verschaerfen-pruefung-von-afd-bewerbern_144_656688.html).
- **Bavaria (Bayern):** In June 2025, the state cabinet decided to add the AfD to its list of extremist organizations for applicant screening [Bundesländer verschärfen Prüfung von AfD-Bewerbern - Haufe](https://www.haufe.de/oeffentlicher-dienst/personal-tarifrecht/bundeslaender-verschaerfen-pruefung-von-afd-bewerbern_144_656688.html).
- **Schleswig-Holstein:** Announced the introduction of a standard check (Regelabfrage) with the Verfassungsschutz before hiring applicants [Bundesländer verschärfen Prüfung von AfD-Bewerbern - Haufe](https://www.haufe.de/oeffentlicher-dienst/personal-tarifrecht/bundeslaender-verschaerfen-pruefung-von-afd-bewerbern_144_656688.html).
- **Brandenburg:** Has been conducting checks for civil servants since 2024 [Bundesländer verschärfen Prüfung von AfD-Bewerbern - Haufe](https://www.haufe.de/oeffentlicher-dienst/personal-tarifrecht/bundeslaender-verschaerfen-pruefung-von-afd-bewerbern_144_656688.html).
- **Lower Saxony (Niedersachsen):** Was considering introducing a questionnaire regarding memberships in extremist organizations during the application process as of mid-2025 [Bundesländer verschärfen Prüfung von AfD-Bewerbern - Haufe](https://www.haufe.de/oeffentlicher-dienst/personal-tarifrecht/bundeslaender-verschaerfen-pruefung-von-afd-bewerbern_144_656688.html).

Several other states (e.g., Niedersachsen, Hessen, Thuringia) have been in various stages of deliberation. The political momentum is strong, but whether any additional state will formally announce new binding guidelines or regulations within the specific 7-week window of May 12 to July 1, 2026 is uncertain.

**Exact later resolution packet**

The question resolves YES because at least two German Bundesländer enacted NEW formal laws specifically addressing constitutional loyalty (Verfassungstreue) requirements for civil servants (Beamte) strictly within the resolution window of May 12, 2026 (00:00 UTC) to July 1, 2026 (23:59 UTC).

CANDIDATE 1 — Niedersachsen (Lower Saxony), passed May 27, 2026:
- The Lower Saxony Landtag passed the "Gesetzentwurf zur Änderung disziplinarrechtlicher und beamtenrechtlicher Vorschriften" on Wednesday, May 27, 2026. The official press release from the Nds. Ministerium für Inneres, Sport und Digitalisierung states: "Der Niedersächsische Landtag hat am heutigen Mittwoch (27.05.2026) den Gesetzentwurf zur Änderung disziplinarrechtlicher und beamtenrechtlicher Vorschriften beschlossen... Verfassungsfeindinnen und Verfassungsfeinde können künftig deutlich schneller aus dem Beamtenverhältnis entfernt werden." The law creates a legal basis for authorities to query the Verfassungsschutz regarding suspected violations of the Verfassungstreuepflicht (duty of constitutional loyalty) and streamlines removal of constitutional enemies from civil service [Landtag beschließt Änderung des Disziplinargesetzes](https://www.mi.niedersachsen.de/startseite/aktuelles/presseinformationen/landtag-beschliesst-anderung-des-disziplinargesetzes-verfassungsfeinde-konnen-kunftig-deutlich-schneller-aus-dem-beamtenverhaltnis-entfernt-werden-251172.html). This is a law passed by the state parliament (an enacted law, not a draft bill), announced on the official state government website — satisfying the resolution criteria. Source: https://www.mi.niedersachsen.de/startseite/aktuelles/presseinformationen/landtag-beschliesst-anderung-des-disziplinargesetzes-verfassungsfeinde-konnen-kunftig-deutlich-schneller-aus-dem-beamtenverhaltnis-entfernt-werden-251172.html

CANDIDATE 2 — Hamburg, passed June 17, 2026:
- The Hamburg Bürgerschaft (state parliament) passed the law introducing a "Regelanfrage" (standard query) with the Verfassungsschutz for all new public-service employees regarding their Verfassungstreue on Wednesday, June 17, 2026, in a named vote of 85 to 25. Per ZEIT/dpa: "Die Bürgerschaft beschloss am Mittwoch in namentlicher Abstimmung mit 85 zu 25 Stimmen die umstrittene Regelanfrage beim Verfassungsschutz" [Hamburg prüft Bewerber für Staatsdienst auf Verfassungstreue](https://www.zeit.de/news/2026-06/17/hamburg-prueft-kuenftig-verfassungstreue-bei-bewerbern). This was corroborated by NDR ("Hamburg prüft künftig Verfassungstreue bei Bewerbern. Stand: 17.06.2026") and DGB/GEW/ver.di ("Regelanfrage beim Verfassungsschutz beschlossen... Datum 17. Juni 2026"). Note: This is distinct from the earlier stage — the Hamburg Senat had only approved the Gesetzentwurf (draft bill) on October 21, 2025 [Senat verabschiedet Gesetzentwurf zur Regelabfrage - Hamburg.de](https://www.hamburg.de/politik-und-verwaltung/behoerden/senatskanzlei/aktuelles/pressemeldungen/senat-verabschiedet-gesetzentwurf-zur-regelabfrage-1109250), which was outside the window; the actual enactment by the Bürgerschaft occurred on June 17, 2026, inside the window. Source: https://www.zeit.de/news/2026-06/17/hamburg-prueft-kuenftig-verfassungstreue-bei-bewerbern

Both measures are "new" (not previously in effect before May 12, 2026) and are formal enacted laws (each passed by the respective state parliament), thus satisfying category 1 of the "formal guideline or regulation" definition and clearly not falling under the excluded categories (draft bills not yet enacted, informal statements, motions, etc.).

Sources that did NOT qualify (for completeness): Schleswig-Holstein's "Gesetz zur Stärkung der Verfassungstreue" remained only a draft bill under committee deliberation as of the June 19, 2026 Landtag debate [Verfassungstreue: Werden Überprüfungen zur Regel? - Landtag SH](https://www.landtag.ltsh.de/nachrichten/26_06_16_gesetzentwurf_verfassungstreue/), so it alone would not trigger YES; Brandenburg's Regelanfrage was already enacted in 2024 [Verfassungstreue-Check für Beamte in Brandenburg - LTO](https://www.lto.de/recht/nachrichten/n/verfassungsschutz-brandenburg-beamte-verfassungstreue-extremismus). However, the Niedersachsen and Hamburg enactments are each independently sufficient to resolve YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-14. `a6287619-a64c-5fa5-9f22-88ecb28c8f07`

- Present date: `2026-05-14 01:15:46.624052`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-18T00:00:00`

**Question**

Will the FDA approve oral tebipenem HBr for complicated urinary tract infections by June 18, 2026?

**Resolution criteria**

This question resolves **Yes** if the U.S. [Food and Drug Administration](https://en.wikipedia.org/wiki/Food_and_Drug_Administration) grants approval for the oral formulation of tebipenem HBr ([tebipenem pivoxil hydrobromide](https://en.wikipedia.org/wiki/Tebipenem)) for the treatment of complicated urinary tract infections (cUTIs), including pyelonephritis, **on or after May 12, 2026, and on or before June 18, 2026 (11:59 PM ET)**.

This question resolves **No** if:
- The FDA issues a Complete Response Letter (CRL) or otherwise declines to approve the NDA, or
- No approval decision is announced by 11:59 PM ET on June 18, 2026.

**Resolution source:** The official FDA [Drugs@FDA database](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm), or official press releases from [GSK](https://www.gsk.com/en-gb/media/press-releases/) or [Spero Therapeutics](https://www.sperotherapeutics.com/investors/news-events/press-releases/). An [FDA approval](https://www.fda.gov/patients/drug-development-process/step-4-fda-drug-review) means the FDA has determined the drug meets its standards for safety and efficacy and has authorized it for marketing in the United States.

**Pre-cutoff background**

**Tebipenem HBr** (tebipenem pivoxil hydrobromide) is an investigational oral [carbapenem](https://en.wikipedia.org/wiki/Carbapenem) antibiotic being developed by [GSK](https://www.gsk.com/) and [Spero Therapeutics](https://www.sperotherapeutics.com/) for the treatment of complicated urinary tract infections (cUTIs), including pyelonephritis. If approved, it would be the first oral carbapenem antibiotic available in the United States.

**Previous CRL:** In 2022, the FDA issued a [Complete Response Letter](https://en.wikipedia.org/wiki/Complete_response_letter) (CRL) for Spero's original NDA, concluding that Spero's Phase 3 cUTI study (ADAPT-PO) was insufficient to support approval and that an additional clinical trial would be needed [Spero Therapeutics Announces Fourth Quarter and Full Year](https://www.globenewswire.com/news-release/2026/03/26/3263404/0/en/spero-therapeutics-announces-fourth-quarter-and-full-year-2025-operating-results-and-provides-a-business-update.html). GSK subsequently licensed the drug from Spero and funded a new Phase 3 trial.

**PIVOT-PO Phase III Trial:** The pivotal PIVOT-PO trial (NCT06059846) was stopped early for efficacy in May 2025 following review by an Independent Data Monitoring Committee. Full results, presented in October 2025, showed tebipenem HBr (oral, 600 mg) achieved a 58.5% overall success rate (261/446 participants) compared to 60.2% for IV imipenem-cilastatin (291/483 participants), with an adjusted treatment difference of −1.3% (95% CI: −7.5%, 4.8%), meeting the pre-specified non-inferiority margin of −10% [Positive PIVOT-PO phase III data show tebipenem HBr's potential as ...](https://www.gsk.com/en-gb/media/press-releases/positive-pivot-po-phase-iii-data-show-tebipenem-hbr-s-potential-as-the-first-oral-carbapenem-antibiotic-for-patients-with-complicated-urinary-tract-infections-cutis/).

**NDA Resubmission and PDUFA Date:** GSK resubmitted the NDA in December 2025, triggering a $25 million milestone payment to Spero. The FDA set a [PDUFA](https://en.wikipedia.org/wiki/Prescription_Drug_User_Fee_Act) target action date of **June 18, 2026** [Spero Therapeutics Announces Fourth Quarter and Full Year](https://www.globenewswire.com/news-release/2026/03/26/3263404/0/en/spero-therapeutics-announces-fourth-quarter-and-full-year-2025-operating-results-and-provides-a-business-update.html).

Resubmission approval rates after a CRL are generally estimated at 70–85%, but the outcome depends on whether the FDA's prior concerns (insufficient clinical evidence) have been adequately addressed by the new PIVOT-PO data.

**Exact later resolution packet**

The question resolves YES.

The FDA approved Utebzi (tebipenem pivoxil), the oral formulation of tebipenem HBr (tebipenem pivoxil hydrobromide), for the treatment of complicated urinary tract infections (cUTIs), including pyelonephritis, on **June 17, 2026**.

Every element of the resolution criteria is satisfied:

1. **Approval date within window (May 12 – June 18, 2026, 11:59 PM ET):** The official FDA press announcement "FDA approves first oral carbapenem therapy for complicated urinary tract infections" (https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-first-oral-carbapenem-therapy-complicated-urinary-tract-infections) is dated/content-current as of 06/17/2026 [FDA approves first oral carbapenem therapy for complicated urinary ...](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-first-oral-carbapenem-therapy-complicated-urinary-tract-infections). The GSK press release "Utebzi (tebipenem pivoxil) approved in the US for adults with complicated urinary tract infections (cUTIs)" is dated 17 June 2026 (https://www.gsk.com/en-gb/media/press-releases/utebzi-tebipenem-pivoxil-approved-in-the-us-for-adults-with-complicated-urinary-tract-infections-cutis/) [Utebzi (tebipenem pivoxil) approved in the US for adults with ... - GSK](https://www.gsk.com/en-gb/media/press-releases/utebzi-tebipenem-pivoxil-approved-in-the-us-for-adults-with-complicated-urinary-tract-infections-cutis/). June 17, 2026 falls within the required window and before the June 18, 2026 PDUFA deadline.

2. **Oral tebipenem HBr:** The FDA approved Utebzi (tebipenem pivoxil) **tablets** — an oral therapy — described as the "first oral carbapenem therapy" [FDA approves first oral carbapenem therapy for complicated urinary ...](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-first-oral-carbapenem-therapy-complicated-urinary-tract-infections), and GSK confirms it is "the first and only oral carbapenem antibiotic approved for these patients" [Utebzi (tebipenem pivoxil) approved in the US for adults with ... - GSK](https://www.gsk.com/en-gb/media/press-releases/utebzi-tebipenem-pivoxil-approved-in-the-us-for-adults-with-complicated-urinary-tract-infections-cutis/). Tebipenem pivoxil is the hydrobromide (HBr) salt form referenced in the question.

3. **Indication is cUTIs including pyelonephritis:** Both the FDA and GSK sources state approval is "for the treatment of complicated urinary tract infections (cUTI), including pyelonephritis" [FDA approves first oral carbapenem therapy for complicated urinary ...](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-first-oral-carbapenem-therapy-complicated-urinary-tract-infections) [Utebzi (tebipenem pivoxil) approved in the US for adults with ... - GSK](https://www.gsk.com/en-gb/media/press-releases/utebzi-tebipenem-pivoxil-approved-in-the-us-for-adults-with-complicated-urinary-tract-infections-cutis/).

4. **Resolution source:** Confirmed via the official FDA news announcement [FDA approves first oral carbapenem therapy for complicated urinary ...](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-first-oral-carbapenem-therapy-complicated-urinary-tract-infections) and the official GSK press release [Utebzi (tebipenem pivoxil) approved in the US for adults with ... - GSK](https://www.gsk.com/en-gb/media/press-releases/utebzi-tebipenem-pivoxil-approved-in-the-us-for-adults-with-complicated-urinary-tract-infections-cutis/), both listed as acceptable resolution sources.

Therefore the FDA granted approval of oral tebipenem HBr for cUTIs on June 17, 2026, within the specified window, resolving the question YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-15. `4dab8b55-b59a-51e5-9c96-88fb9f245af7`

- Present date: `2026-05-02 19:23:28.468958`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any CAR-T therapy abstract released for the 2026 ASCO Annual Meeting report a complete response (CR) in a solid tumor patient?

**Resolution criteria**

This question resolves **Yes** if at least one abstract published by ASCO for the 2026 Annual Meeting explicitly reports a **complete response (CR)** in at least one human patient with a **solid tumor** treated with **CAR-T therapy**. It resolves **No** otherwise.

**Definitions:**

- **"Complete response" (CR):** Disappearance of all target lesions as defined by RECIST 1.1 (https://recist.eortc.org/recist-1-1-2/) or iRECIST criteria, or explicitly labeled as "complete response" or "CR" by the abstract authors using their stated response criteria. The CR must be explicitly stated in the abstract text, results section, or associated data tables.

- **"Solid tumor":** Any malignant neoplasm arising from solid organs or tissues (e.g., lung, breast, colon, brain, sarcoma, melanoma), as distinguished from hematologic (liquid) malignancies such as leukemia, lymphoma, or myeloma. See: https://www.cancer.gov/publications/dictionaries/cancer-terms/def/solid-tumor

- **"CAR-T therapy":** Chimeric antigen receptor T-cell therapy, in which a patient's or donor's T cells are genetically modified to express a chimeric antigen receptor that targets a specific protein on cancer cells. See NCI definition: https://www.cancer.gov/publications/dictionaries/cancer-terms/def/car-t-cell-therapy. For this question, TCR-T (T-cell receptor) therapies such as Immatics' anzu-cel do NOT count—only therapies explicitly described as CAR-T in the abstract qualify.

- **"Abstract published by ASCO for the 2026 Annual Meeting":** Any abstract (regular or late-breaking) published in the ASCO Meeting Library or the Journal of Clinical Oncology (JCO) Supplement for the 2026 Annual Meeting. Resolution source: https://ascopubs.org/jco/meeting and https://www.asco.org/abstracts

The question resolves based on abstracts available by June 1, 2026, 11:59 PM ET.

**Pre-cutoff background**

CAR-T (chimeric antigen receptor T-cell) therapy (https://en.wikipedia.org/wiki/CAR_T_cell) uses genetically engineered T cells to target cancer. While CAR-T has transformed treatment of hematologic (blood) cancers, achieving durable responses in solid tumors—defined here as non-hematologic malignancies arising from solid organs or tissues—has been far more challenging. As of mid-2025, complete responses in solid tumors with CAR-T remain rare, with most trials reporting overall response rates below 40% and CRs in only isolated cases. Notable signals have emerged: a 2025 Nature review noted individual CRs in brain tumors (GBM) with intracerebroventricular CAR-T delivery, and early-phase trials targeting mesothelin and claudin18.2 have reported occasional CRs at higher dose levels.

The 2026 ASCO Annual Meeting (May 29–June 2, 2026) will feature multiple CAR-T and engineered T-cell therapy presentations targeting solid tumors. Key programs include:

- **A2 Biotherapeutics**: Presenting three posters on their Tmod™ logic-gated CAR-T platform, including initial safety/efficacy data from the Phase 1/2 EVEREST-2 study of A2B694 (mesothelin-targeted) in advanced solid tumors [https://www.a2bio.com/a2-biotherapeutics-to-highlight-progress-of-car-t-cell-clinical-programs-in-three-poster-presentations-during-the-american-society-of-clinical-oncology-asco-2026-annual-meeting/](https://www.a2bio.com/a2-biotherapeutics-to-highlight-progress-of-car-t-cell-clinical-programs-in-three-poster-presentations-during-the-american-society-of-clinical-oncology-asco-2026-annual-meeting/).
- **Immatics**: Presenting four oral presentations covering PRAME-directed TCR T-cell therapies (anzu-cel/IMA203, IMA203CD8) in melanoma, ovarian cancer, and synovial sarcoma, as well as the MAGEA4/8 bispecific IMA401 in recurrent solid tumors [https://immatics.com/news/immatics-announces-four-upcoming-oral-presentations-across-its-clinical-cell-therapy-and-bispecific-portfolio-at-2026-asco-annual-meeting/](https://immatics.com/news/immatics-announces-four-upcoming-oral-presentations-across-its-clinical-cell-therapy-and-bispecific-portfolio-at-2026-asco-annual-meeting/).

Additional companies and academic groups are also expected to present CAR-T solid tumor data. The AACR 2026 meeting earlier in the year already showed promising signals for CAR-T in solid tumors with novel architectures and first-in-human data.

ASCO abstracts will be released on May 21, 2026 at 5:00 PM ET on the ASCO abstracts website. Late-breaking abstracts are released during the meeting itself (May 29–June 2).

**Exact later resolution packet**

The question resolves YES because at least one abstract published by ASCO for the 2026 Annual Meeting explicitly reports a complete response (CR) in a human solid tumor patient treated with CAR-T therapy.

Specifically, A2 Biotherapeutics' EVEREST-2 study (Abstract #8579) presented at the 2026 ASCO Annual Meeting reports a complete response (CR per RECIST 1.1, at month 3 post-infusion) in a patient with non-small cell lung cancer (NSCLC) — a solid (non-hematologic) tumor — treated with A2B694, explicitly described as a logic-gated mesothelin (MSLN)-targeted Tmod™ chimeric antigen receptor T-cell (CAR T-cell) therapy [485abe].

This satisfies every checklist requirement:
- The therapy is explicitly a CAR-T (Tmod CAR T-cell), not a TCR-T [485abe].
- NSCLC is a solid tumor, not leukemia/lymphoma/myeloma.
- "Complete response (CR)" is explicitly stated in the abstract [485abe].
- It is part of the 2026 ASCO Annual Meeting (ASCO Meeting Library/JCO Supplement), not AACR.
- Abstracts were released May 21, 2026 (before the June 1, 2026 cutoff); A2's press release dated May 21, 2026 confirmed full abstracts available on the ASCO website [485abe].
- The CR occurred in a human patient.

Background: A2 Biotherapeutics had earlier reported this NSCLC CR at the SITC 2025 meeting in November 2025 [960724], and subsequently presented the EVEREST-2 efficacy/safety update including this complete response at ASCO 2026. The corresponding ASCO 2026 abstract is accessible via the ASCO Meeting Library (https://www.asco.org/annual-meeting/abstracts-presentations); abstract number 8579 [485abe].

Note: Immatics' anzu-cel/IMA203 PRAME-directed therapies are TCR-T and explicitly excluded by the resolution criteria, but the A2B694 CAR-T result independently satisfies the YES condition.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-16. `daf08eba-d005-5c37-a9a5-561338ce6768`

- Present date: `2026-05-12 21:32:22.213174`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Lisa Cook still be serving as a Federal Reserve Governor on July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, at 11:59 PM UTC on July 1, 2026, Lisa Cook is listed as a current member of the Board of Governors on the official Federal Reserve website (https://www.federalreserve.gov/aboutthefed/bios/board/default.htm).

This question resolves as **No** if Lisa Cook is not listed as a current member of the Board of Governors on that page at that time, whether due to a Supreme Court ruling lifting the injunction, a voluntary resignation, or any other reason.

If the Federal Reserve website is temporarily unavailable at 11:59 PM UTC on July 1, 2026, resolution may be deferred up to 48 hours, or determined based on credible reporting from major news outlets (e.g., Reuters at https://www.reuters.com, Associated Press at https://apnews.com, or The New York Times at https://www.nytimes.com) confirming her status.

**Pre-cutoff background**

Lisa Cook was confirmed as a member of the Federal Reserve Board of Governors (https://www.federalreserve.gov/aboutthefed/bios/board/default.htm) in May 2022. A "Federal Reserve Governor" refers to a member of the Board of Governors of the Federal Reserve System (https://en.wikipedia.org/wiki/Federal_Reserve_Board_of_Governors), the central banking system of the United States. "Serving" means being officially listed as a current member of the Board on the Federal Reserve's website.

On August 25, 2025, President Donald Trump announced via social media that he had fired Cook, citing allegations of mortgage fraud [Trump v. Cook - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Cook). Cook challenged this dismissal in federal court, arguing the President lacked authority to remove a Fed Governor without cause.

On September 9, 2025, U.S. District Court Judge Jia Cobb issued a preliminary injunction preventing the Trump administration from removing Cook from her position while the litigation proceeds [Trump v. Cook - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Cook). On October 1, 2025, the Supreme Court rejected an emergency appeal by the Trump administration to lift the injunction [Trump v. Cook - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Cook).

The Supreme Court heard oral arguments in *Trump v. Cook* (No. 25A312) on January 21, 2026 [Trump v. Cook - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Cook). During oral arguments, multiple justices appeared skeptical of the administration's claim that the President can fire Fed governors at will. As of the latest available information (March 12, 2026), the Supreme Court has not issued a final ruling, and the preliminary injunction remains in effect — meaning Cook continues to serve as a Federal Reserve Governor [Trump v. Cook - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Cook).

The Supreme Court's decision is expected before the end of its current term (typically late June or early July 2026). The outcome will determine whether the injunction stands or is lifted, which would directly affect Cook's ability to continue serving. Even if the Court rules against Cook, procedural delays or negotiations could affect the timing of any removal. Conversely, Cook could also voluntarily resign or reach a negotiated departure before the ruling.

**Exact later resolution packet**

The question resolves YES if, at 11:59 PM UTC on July 1, 2026, Lisa Cook is listed as a current member of the Board of Governors on the official Federal Reserve website (https://www.federalreserve.gov/aboutthefed/bios/board/default.htm).

PRIMARY SOURCE (Federal Reserve website):
- The official Board Members page (https://www.federalreserve.gov/aboutthefed/bios/board/default.htm) lists "Lisa D. Cook" as a current member of the Board of Governors as of July 1, 2026 [https://www.federalreserve.gov/aboutthefed/bios/board/default.htm](https://www.federalreserve.gov/aboutthefed/bios/board/default.htm).
- Her official biography page (https://www.federalreserve.gov/aboutthefed/bios/board/cook.htm) confirms she is a sitting member, reappointed September 8, 2023 and sworn in September 13, 2023, for a term ending January 31, 2038 [https://www.federalreserve.gov/aboutthefed/bios/board/cook.htm](https://www.federalreserve.gov/aboutthefed/bios/board/cook.htm).

SUPPORTING/FALLBACK SOURCE (Reuters, permitted fallback):
- On June 29, 2026, the U.S. Supreme Court ruled 5–4, in Trump v. Cook, that Lisa Cook can remain in her position as a Federal Reserve Governor while her legal challenge to Trump's attempted removal proceeds, i.e., the injunction protecting her stands. Reuters confirms the Court "refused to let Trump fire Cook" [Fed's Lisa Cook made history even before battling Trump | Reuters](https://www.reuters.com/world/us/feds-lisa-cook-made-history-even-before-battling-trump-2026-06-29/). This ruling is corroborated by numerous major outlets in Google search results (NYT, CNBC, NPR, WSJ, AP, Bloomberg, The Guardian, SCOTUSblog), all reporting the June 29, 2026 5-4 decision keeping Cook in her job.

Because Cook was not removed (the Supreme Court declined to lift the injunction, and instead affirmed she stays for now) and she remains officially listed as a current member on the Federal Reserve website as of July 1, 2026, the literal resolution criterion ("being officially listed as a current member of the Board on the Federal Reserve's website") is satisfied. Resolution: YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-17. `24ee233d-c9b2-58a1-99bd-98d9a6d812b4`

- Present date: `2026-05-12 16:09:21.734374`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will any candidate other than Bobby Charles or Garrett Mason finish in the top two of the Maine Republican gubernatorial primary on June 9, 2026?

**Resolution criteria**

This question resolves **Yes** if any candidate other than Bobby Charles and Garrett Mason receives the first- or second-highest number of votes in the June 9, 2026, Maine Republican gubernatorial primary. It resolves **No** if Bobby Charles and Garrett Mason are the two candidates with the highest vote totals.

**Definitions:**

- **"Candidate"**: Any individual whose name appears on the official ballot for the Maine Republican gubernatorial primary as certified by the Maine Secretary of State (see https://www.maine.gov/sos/elections-voting/upcoming-elections). Write-in candidates are **excluded** from the "top two" calculation; only candidates listed on the official ballot are considered.

- **"Top two"**: The two candidates who receive the highest and second-highest number of votes, respectively, in the primary election. In the event of an exact tie for the second-highest vote total between Garrett Mason (or Bobby Charles) and another candidate, the question resolves **Yes**, since a non-Charles/Mason candidate would have matched a top-two finish. If Bobby Charles and Garrett Mason tie with a third candidate for second place, the question also resolves **Yes**.

- **"Bobby Charles"** refers to the candidate listed on the ballot as Bobby Charles (also known as Robert Charles).

**Resolution source**: The official certified results published by the Maine Secretary of State at https://www.maine.gov/sos/elections-voting/election-results-data [Election Results/Data | SOS - Maine.gov](https://www.maine.gov/sos/elections-voting/election-results-data). If certified results are not yet available by the resolution date, unofficial results reported by the Maine Secretary of State or credible news sources (e.g., AP, Portland Press Herald, Maine Public) may be used.

**Pre-cutoff background**

The Maine Republican gubernatorial primary is scheduled for June 9, 2026. Eight candidates are on the ballot: Jonathan Bush, Bobby Charles, David Jones, James Libby, Garrett Mason, Owen McCarthy, Ben Midgley, and Robert J. Wessels [Maine gubernatorial election, 2026 (June 9 Republican primary)](https://ballotpedia.org/Maine_gubernatorial_election,_2026_(June_9_Republican_primary)).

A University of New Hampshire poll conducted February 12–16, 2026 (n=404 likely voters, MOE ±4.9%) showed Bobby Charles leading at 28%, Garrett Mason at 12%, David Jones at 7%, Ben Midgley at 6%, Jonathan Bush at 5%, Robert J. Wessels at 4%, James Libby at 2%, Owen McCarthy at 1%, with 31% undecided [Maine gubernatorial election, 2026 (June 9 Republican primary)](https://ballotpedia.org/Maine_gubernatorial_election,_2026_(June_9_Republican_primary)). More recent polling (referenced in the seed research) suggests Charles has consolidated support around 47%, with Mason and Bush both near 11%.

The large undecided share and tight race for second place make it genuinely uncertain whether Mason will hold his second-place position against Bush, Jones, or Midgley. Maine uses ranked-choice voting in some elections; however, primary elections for governor determine nominees based on vote totals certified by the Maine Secretary of State.

Official election results are published by the Maine Secretary of State at https://www.maine.gov/sos/elections-voting/election-results-data [Election Results/Data | SOS - Maine.gov](https://www.maine.gov/sos/elections-voting/election-results-data).

**Exact later resolution packet**

RESOLUTION: YES (1).

The question resolves YES if any candidate other than Bobby Charles or Garrett Mason finishes in the top two (first- or second-highest number of votes) of the June 9, 2026 Maine Republican gubernatorial primary.

KEY FINDING — Ben Midgley (neither Charles nor Mason) finished SECOND:
- Multiple credible sources report the first-round (first-choice) results as: Bobby Charles ~37.9% (1st), Ben Midgley ~20.1% (2nd), Jonathan Bush ~19.8% (3rd), with Garrett Mason finishing well behind these three [626758, 9d4c5c, 375f5c].
- The Portland Press Herald (reporting AP unofficial results) states Charles received 37.9% in the first round, "followed by Ben Midgley (20.1%) and Jonathan Bush (19.8%)" [626758]. URL: https://www.pressherald.com/2026/06/19/bobby-charles-holds-lead-to-win-republican-primary-for-governor-after-rcv-runoff/
- NBC News' results tracker likewise lists Robert (Bobby) Charles 1st at 37.9%, Benjamin Midgley 2nd at 20.1%, and Jonathan Bush 3rd at ~19.7-19.8% [9d4c5c]. URL: https://www.nbcnews.com/politics/2026-primary-elections/maine-governor-results
- The Maine Morning Star confirms Charles first (37.9%), Midgley second (~20%), Bush third (~19.8%), with Garrett Mason finishing behind them; Charles was declared the nominee after the ranked-choice runoff (announced by the Maine Secretary of State) [375f5c]. URL: https://mainemorningstar.com/2026/06/19/bobby-charles-secures-republican-nomination-for-governor/

TOP-TWO ANALYSIS:
- Whether measured by first-choice vote totals (Charles 1st, Midgley 2nd) or by the ranked-choice runoff (which was between Charles and Midgley), the second-place finisher was Ben Midgley — a candidate other than Bobby Charles or Garrett Mason. Garrett Mason did NOT finish in the top two (he trailed Charles, Midgley, and Bush). Therefore a non-Charles/Mason candidate occupied a top-two position, satisfying the YES condition.

TIE CHECK: There is no tie affecting the outcome. Charles clearly led (~37.9%); Midgley (~20.1%) edged Bush (~19.8%) for second. Neither Charles nor Mason tied with a third candidate for first or second; in fact Mason was not close to the top two, so the tie clauses in the resolution criteria are not triggered — and even the closest gap (Midgley vs. Bush for 2nd) does not involve Mason or Charles.

WRITE-IN EXCLUSION: All relevant top finishers (Charles, Midgley, Bush, Mason) are candidates listed on the official ballot; no write-in candidate is implicated, consistent with the resolution criteria excluding write-ins.

SOURCE NOTE: The official Maine Secretary of State certified-results page (https://www.maine.gov/sos/elections-voting/election-results-data) could not be directly parsed by the tools, and NPR's tracker showed no data [0c1297]; Ballotpedia's page was not machine-readable [2afc88]. However, the resolution criteria explicitly permit unofficial results reported by the Maine Secretary of State or credible news sources (AP, Portland Press Herald, Maine Public). The vote figures above come from AP-sourced reporting via the Portland Press Herald and NBC News, plus Maine Morning Star, which all agree. The Maine SoS office itself announced Charles as the nominee after the RCV runoff against Midgley.

CONCLUSION: A candidate other than Bobby Charles or Garrett Mason (Ben Midgley) finished in the top two. Resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-18. `2c0f5892-9b6f-5a01-b5cb-d969eaeb3033`

- Present date: `2026-05-01 13:25:12.887073`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will OpenAI's GPT-5.5 model reach General Availability (GA) on Amazon Bedrock by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, by 23:59 UTC on June 1, 2026, OpenAI's GPT-5.5 model (identified by a model ID containing "gpt-5.5" or explicitly labeled "GPT-5.5") is listed as **Generally Available (GA)** — not "Limited Preview," "Public Preview," or "Beta" — on Amazon Bedrock. "General Availability" means that any AWS customer with a standard Bedrock-enabled account can access the model without needing to request preview access or be on a waitlist.

This will be verified by checking the official AWS Bedrock supported foundation models documentation page at https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html or the AWS Bedrock OpenAI landing page at https://aws.amazon.com/bedrock/openai/. If GPT-5.5 remains in any preview or beta status, or is not listed at all, the question resolves **No**.

The resolution status must reflect availability on or after April 30, 2026 (the question opening date). Any availability prior to this date is not applicable, though GPT-5.5 was not available before this date.

**Pre-cutoff background**

On April 28, 2026, OpenAI and Amazon Web Services (AWS) announced an expanded strategic partnership bringing OpenAI's frontier models, Codex coding agent, and Managed Agents to Amazon Bedrock (https://openai.com/index/openai-on-aws/). This marked a significant shift, as OpenAI had previously maintained exclusivity with Microsoft Azure for cloud-hosted model access.

As of April 30, 2026, GPT-5.5 and GPT-5.4 are listed in "Limited Preview" status on the AWS Bedrock OpenAI page [OpenAI frontier models on Amazon Bedrock](https://aws.amazon.com/bedrock/openai/). GPT-5.4 was described as "available immediately in limited preview," with GPT-5.5 "arriving shortly thereafter." The official AWS Bedrock supported models documentation page (https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) does not yet list GPT-5.5 among its generally available foundation models as of April 30, 2026 [Supported foundation models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) — it currently lists only the open-weight GPT OSS models. Cloud service integrations on AWS typically progress from Limited Preview to Public Preview to General Availability (GA), and this process can take weeks to months.

GPT-5.5 refers to the OpenAI frontier language model announced in 2026, identifiable by its model name "gpt-5.5" in API calls, as distinct from GPT-5.4 and earlier model versions.

**Exact later resolution packet**

The question resolves YES because OpenAI's GPT-5.5 model reached General Availability on Amazon Bedrock by the June 1, 2026 23:59 UTC deadline.

Key evidence:
- AWS published an official "What's New" announcement titled "GPT-5.5, GPT-5.4, and Codex from OpenAI are now generally available on Amazon Bedrock," dated June 1, 2026 (https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-openai-models-codex-generally-available/). It explicitly states "You can now use GPT-5.5 and GPT-5.4 in production workloads on Amazon Bedrock" [de1525].
- The official AWS Bedrock OpenAI landing page (https://aws.amazon.com/bedrock/openai/) states "OpenAI frontier models for agentic coding, autonomous workflows, and complex reasoning, now generally available on Amazon Bedrock," with GPT-5.5 listed among the model versions [a0d2fc].
- The official Amazon News page (https://www.aboutamazon.com/news/aws/bedrock-openai-models), updated June 1, 2026, confirms in its key takeaways: "GPT-5.5, GPT-5.4, and Codex are now generally available on Amazon Bedrock" and that customers can now access GPT-5.5 [76d27c].

GA satisfies the resolution criteria: the model is no longer in "Limited Preview," "Public Preview," or "Beta," and is accessible to standard Bedrock-enabled accounts in production via the standard InvokeModel API without a waitlist. The GA date of June 1, 2026 falls on (and before the end of) the deadline of 23:59 UTC June 1, 2026.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-19. `36edec34-1405-56ee-99d0-75b8bb922f38`

- Present date: `2026-05-12 16:46:20.477608`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the European Parliament formally adopt the legislative package implementing the EU-US Turnberry trade deal before July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if the European Parliament formally adopts the final legislative text implementing the EU-US Turnberry trade deal on or after May 10, 2026 (00:00 UTC), and by July 1, 2026 (23:59 UTC).

"Formally adopt" means the European Parliament passes the legislative text in a final vote during a plenary session, by a majority of votes cast (as described in the [European Parliament's explanation of how plenary works](https://www.europarl.europa.eu/about-parliament/en/organisation-and-rules/how-plenary-works)). Only texts adopted in plenary formally constitute acts of the European Parliament [How plenary works - European Parliament](https://www.europarl.europa.eu/about-parliament/en/organisation-and-rules/how-plenary-works).

This applies to the main regulation on preferential access for US goods (procedure 2025/0260(COD)). Adoption of the secondary regulation on lobster imports alone is not sufficient.

This question resolves as **No** if, by 23:59 UTC on July 1, 2026, the European Parliament has not held a final plenary vote adopting the legislative text, or if the text is rejected in such a vote.

**Resolution source:** The [European Parliament Legislative Observatory (OEIL) procedure file for 2025/0260(COD)](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0260(COD)), supplemented by official European Parliament press releases at https://www.europarl.europa.eu/news/en/press-room. If the "Key events" or "Stage reached in procedure" section of the OEIL page indicates that the Parliament has adopted its position in first reading (or the act has been adopted), the question resolves Yes.

**Pre-cutoff background**

On July 27, 2025, US President Donald Trump and European Commission President Ursula von der Leyen reached a framework agreement on tariffs and trade in Turnberry, Scotland. The European Commission subsequently published two legislative proposals on August 28, 2025, to implement the tariff aspects of the deal: one providing preferential access for US goods to the EU (COM(2025)0471), and another on zero-tariff imports of certain goods including lobster (COM(2025)0472) [2025/0260(COD) | Legislative Observatory | European Parliament](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0260(COD)).

On March 26, 2026, the European Parliament adopted its negotiating position by votes of 417-154 and 437-144, setting several conditions including a suspension clause, a sunrise clause, a sunset clause (expiring March 31, 2028), and a safeguard mechanism [EU US trade deal: MEPs set conditions for lowering tariffs on US ...](https://www.europarl.europa.eu/news/en/press-room/20260323IPR38830/eu-us-trade-deal-meps-set-conditions-for-lowering-tariffs-on-us-products). The matter was then referred back to the INTA committee for interinstitutional (trilogue) negotiations with the Council [2025/0260(COD) | Legislative Observatory | European Parliament](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0260(COD)).

As of May 11, 2026 (UTC), two rounds of trilogue negotiations have been completed. Bernd Lange, head of the Parliament delegation, has described the talks as "constructive" with "good progress" on the safeguard mechanism and review provisions, but has stated that "there is still some way to go" [EU-US trade deal: EU Co-legislators are converging towards an ...](https://ieu-monitoring.com/editorial/eu-us-trade-deal-eu-co-legislators-are-converging-towards-an-agreement/1189107?utm_source=ieu-portal). The next trilogue session is scheduled for May 19, 2026, in Strasbourg [EU parliament negotiator says trade deal work is not yet done as ...](https://investinglive.com/news/eu-parliament-negotiator-says-trade-deal-work-is-not-yet-done-as-may-talks-loom-20260506/) [EU-US trade deal: EU Co-legislators are converging towards an ...](https://ieu-monitoring.com/editorial/eu-us-trade-deal-eu-co-legislators-are-converging-towards-an-agreement/1189107?utm_source=ieu-portal). A key external pressure is the July 4, 2026 deadline set by the US for the EU to implement the deal or face potential tariff hikes [EU parliament negotiator says trade deal work is not yet done as ...](https://investinglive.com/news/eu-parliament-negotiator-says-trade-deal-work-is-not-yet-done-as-may-talks-loom-20260506/). The current procedure status on the Legislative Observatory is "Awaiting Parliament's position in 1st reading" (reference: 2025/0260(COD)) [2025/0260(COD) | Legislative Observatory | European Parliament](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0260(COD)).

**Exact later resolution packet**

The question resolves YES.

The question asks whether the European Parliament formally adopted the final legislative text implementing the EU-US Turnberry trade deal (main regulation, procedure 2025/0260(COD)) in a final plenary vote on or after May 10, 2026 (00:00 UTC) and by July 1, 2026 (23:59 UTC).

Evidence:

1. OEIL procedure file for 2025/0260(COD) (https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0260(COD)) shows the following key events within the resolution window: 27/05/2026 approval in committee of the text agreed at 1st reading interinstitutional (trilogue) negotiations; 15/06/2026 debate in Parliament; 16/06/2026 "Decision by Parliament, 1st reading" — the formal plenary adoption (document T10-0197/2026); 25/06/2026 "Act adopted by Council after Parliament's 1st reading"; and 25/06/2026 "Final act signed." The procedure status is now "Procedure completed, awaiting publication in Official Journal" [6c83b8].

2. The European Parliament's own plenary-news briefing confirms the final vote was scheduled for Tuesday, June 16, 2026 in Strasbourg, and that this vote covered the main regulation on preferential access for US goods, procedure 2025/0260(COD) (not merely the secondary lobster regulation) [48985f].

3. Euronews reports the Parliament formally adopted the main legislative act on June 16, 2026, by 440 votes in favor, 151 against, 50 abstentions — the regulation removing EU duties on most US industrial goods under the Turnberry deal [7e97aa]. The official EP press release (20260611IPR45206, "EU-US trade: Parliament gives its green light to tariff legislation") likewise states the main regulation was adopted by 440 votes to 151 with 50 abstentions.

Analysis against the resolution criteria:
- The June 16, 2026 vote is a final plenary adoption by a majority of votes cast (440-151-50), distinct from the March 26, 2026 negotiating-position votes (417-154 and 437-144) that merely set conditions for trilogue [6c83b8, 48985f].
- The adopted text is the MAIN regulation (2025/0260(COD)) on preferential/duty-free access for US goods, satisfying the requirement that adoption of the lobster regulation alone is insufficient [48985f, 7e97aa].
- June 16, 2026 falls within the required window (May 10, 2026 00:00 UTC – July 1, 2026 23:59 UTC).
- The OEIL "Stage reached in procedure" is now "Procedure completed" with the final act signed on 25/06/2026 (i.e., beyond "Act adopted"), a direct result of the plenary session within the window [6c83b8].

All resolution criteria for YES are therefore met.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-20. `d74eb890-70be-58e7-b639-bb99ddb05de6`

- Present date: `2026-05-12 21:28:59.767048`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Supreme Court rule in favor of Lisa Cook in Trump v. Cook?

**Resolution criteria**

This question resolves **Yes** if the Supreme Court of the United States issues a final opinion or order in Trump v. Cook (Docket No. 25A312) on or after May 10, 2026, and by July 1, 2026, that rules in favor of Lisa Cook. A ruling "in favor" of Cook means any of the following outcomes:

1. The Court affirms the lower court's preliminary injunction blocking Cook's removal, OR
2. The Court holds that the President cannot remove Federal Reserve Board governors "at will" (i.e., without statutory "for cause" justification such as inefficiency, neglect of duty, or malfeasance — see "at-will employment" definition: https://en.wikipedia.org/wiki/At-will_employment), OR
3. The Court otherwise rules that Cook's removal was unlawful under the Federal Reserve Act or the Constitution.

The question resolves **No** if the Court rules that the President does have the authority to remove Fed governors at will (consistent with the "unitary executive theory" — see: https://en.wikipedia.org/wiki/Unitary_executive_theory), reverses the lower court injunction in a manner that permits Cook's removal, or otherwise rules against Cook.

If the Court issues a narrow or mixed ruling, the question resolves Yes if the operative holding preserves Cook's position on the Board; it resolves No if the operative holding permits her removal.

If no decision is issued by July 1, 2026, this question resolves **N/A** (ambiguous).

**Resolution source:** The official Supreme Court opinions page at https://www.supremecourt.gov/opinions/slipopinion/25 and/or SCOTUSblog's case page at https://www.scotusblog.com/cases/trump-v-cook/.

**Pre-cutoff background**

Donald J. Trump, et al. v. Lisa D. Cook (Docket No. 25A312) is a Supreme Court case concerning whether the President has the authority to remove a member of the Federal Reserve Board of Governors "at will." In August 2025, President Trump attempted to fire Governor Lisa Cook, citing allegations of mortgage fraud. Cook sued, arguing that the Federal Reserve Act restricts presidential removal of Fed governors to "for cause" grounds (inefficiency, neglect of duty, or malfeasance). A district court granted a preliminary injunction on September 9, 2025, blocking the removal, and the Supreme Court heard oral arguments on January 21, 2026 [Trump v. Cook - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Cook).

As of May 11, 2026, the Supreme Court has not yet issued a final decision in the case [Trump v. Cook - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Cook). The decision is expected before the end of the Court's October 2025 term (typically by late June 2026).

The case raises fundamental questions about the "unitary executive theory" — the idea that the President must have complete control over the executive branch, including the power to remove agency heads at will (see: https://en.wikipedia.org/wiki/Unitary_executive_theory). It also implicates the precedent set by *Humphrey's Executor v. United States* (1935), which upheld Congress's power to limit presidential removal of officers of independent agencies (see: https://en.wikipedia.org/wiki/Humphrey%27s_Executor_v._United_States).

The current Court has a 6-3 conservative majority (Chief Justice Roberts and Justices Thomas, Alito, Gorsuch, Kavanaugh, and Barrett, with liberal Justices Sotomayor, Kagan, and Jackson) [Trump v. Cook - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Cook). The conservative majority has shown receptiveness to expanding executive power, but legal commentators noted that several justices expressed unease about threats to Federal Reserve independence during oral argument [Trump v. Cook - Wikipedia](https://en.wikipedia.org/wiki/Trump_v._Cook).

**Exact later resolution packet**

The question resolves YES.

**Timing check (within window):** The Supreme Court issued its final decision in Trump v. Cook (Docket No. 25A312) on **June 29, 2026**, which falls within the required resolution window of "on or after May 10, 2026, and by July 1, 2026" [Trump v. Cook (25A312) - SCOTUSblog](https://www.scotusblog.com/cases/trump-v-cook/)[[PDF] 25A312 Trump v. Cook (06/29/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/25a312_5468.pdf). The official slip opinion is titled "25A312 Trump v. Cook (06/29/2026)."

**Correct docket:** Both the official Supreme Court slip opinion and the SCOTUSblog case page confirm the ruling concerns Docket No. 25A312, "Donald J. Trump, President of the United States, Applicant v. Lisa D. Cook, Member of the Board of Governors of the Federal Reserve System" [Trump v. Cook (25A312) - SCOTUSblog](https://www.scotusblog.com/cases/trump-v-cook/)[[PDF] 25A312 Trump v. Cook (06/29/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/25a312_5468.pdf).

**Outcome (in favor of Cook):** By a 5-4 vote, in an opinion by Chief Justice John Roberts (joined by Justices Sotomayor, Kagan, Kavanaugh, and Jackson), the Court **denied the government's application for a stay** of the district court's preliminary injunction, thereby leaving in place the order blocking Cook's removal [Trump v. Cook (25A312) - SCOTUSblog](https://www.scotusblog.com/cases/trump-v-cook/)[[PDF] 25A312 Trump v. Cook (06/29/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/25a312_5468.pdf). The Court held that the government was not likely to succeed on the merits and that the President failed to afford Cook the procedural protections (notice and an opportunity to respond) required before termination [[PDF] 25A312 Trump v. Cook (06/29/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/25a312_5468.pdf). This operative holding preserves Lisa Cook's position on the Federal Reserve Board of Governors while her challenge proceeds.

**Match to resolution criteria:** The resolution criteria state the question resolves YES if the Court "affirms the lower court's preliminary injunction blocking Cook's removal" or if "the operative holding preserves Cook's position on the Board." The Court's denial of the stay preserves the injunction and Cook's position, squarely satisfying the YES criteria [Trump v. Cook (25A312) - SCOTUSblog](https://www.scotusblog.com/cases/trump-v-cook/)[[PDF] 25A312 Trump v. Cook (06/29/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/25a312_5468.pdf).

**Sources (as specified in resolution criteria):**
- Official Supreme Court slip opinion: https://www.supremecourt.gov/opinions/25pdf/25a312_5468.pdf [[PDF] 25A312 Trump v. Cook (06/29/2026) - Supreme Court](https://www.supremecourt.gov/opinions/25pdf/25a312_5468.pdf)
- SCOTUSblog case page: https://www.scotusblog.com/cases/trump-v-cook/ — "On June 29, 2026, the court denied the application. Judgment Application for stay denied, 5-4, in an opinion by John Roberts on Jun 29, 2026." [Trump v. Cook (25A312) - SCOTUSblog](https://www.scotusblog.com/cases/trump-v-cook/)

Note: In a separate, companion ruling issued the same day, the Court expanded the President's power to remove heads of other independent agencies (e.g., the FTC), but it carved out the Federal Reserve as an exception, meaning Cook specifically retained her position. This does not affect the YES resolution for Trump v. Cook.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-21. `c78c35c2-c526-59f4-a0f8-9c1cb7a9ca12`

- Present date: `2026-05-03 02:13:18.559708`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the NIH have obligated less than 50% of its FY2026 extramural research funding by June 1, 2026?

**Resolution criteria**

This question resolves YES if, as of 11:59 PM ET on June 1, 2026, the NIH has obligated less than 50% of its estimated FY2026 extramural research funding (approximately $38 billion, meaning less than $19 billion obligated). It resolves NO if 50% or more has been obligated.

"Obligated" means funds that have been committed through grant awards or contracts, as tracked by official NIH data or credible third-party trackers. The primary resolution source is the AAMC's NIH awards tracker (https://www.aamc.org/about-us/mission-areas/biomedical-research/publication/tracking-nih-awards-fy-2026), which publishes running totals of NIH extramural obligations. If the AAMC tracker is unavailable, resolution may rely on equivalent data from the NIH Reporter database (https://reporter.nih.gov/), official NIH notices (https://grants.nih.gov/grants/guide/), or credible reporting from sources such as STAT News, Science, or Nature.

"Extramural research funding" refers to the portion of the NIH budget allocated to grants, contracts, and cooperative agreements to outside institutions, excluding intramural research and agency operations. The $38 billion estimate is based on reporting as of March 2026; if an updated official figure for total FY2026 extramural funding is published, that figure shall be used as the denominator.

If the government enters a new Continuing Resolution or if FY2026 appropriations are rescinded or amended by congressional action (defined as legislation passed by both chambers of Congress and signed by the President or enacted over a veto, verifiable at https://www.congress.gov/) or by a court order (defined as a ruling by a U.S. federal court, verifiable through PACER at https://pacer.uscourts.gov/ or court websites) that changes the total NIH FY2026 appropriation, the new enacted level shall be used. If FY2026 appropriations remain at $47.2 billion as enacted in H.R. 7148, the ~$38 billion extramural estimate applies.

**Pre-cutoff background**

Congress enacted FY2026 appropriations for the National Institutes of Health at $47.2 billion, signed into law on February 3, 2026 (H.R. 7148, the Consolidated Appropriations Act, 2026) [Congress Rejects Cuts to NIH, Increases Budget for FY26](https://jm-aq.com/congress-rejects-cuts-to-nih-increase-budget-for-fy26/). This rejected the Trump administration's original proposal to cut NIH funding by approximately 40% to $27.5 billion. However, despite having its full budget enacted, the NIH has been dramatically slow in disbursing funds. As of approximately March 31, 2026, the NIH had obligated only about $5.8 billion of its estimated $38 billion in extramural funding — roughly 15% — according to tracking by the AAMC. By February 2026, the number of NIH awards granted was 80% less than the four-year average for FY2021–2024, and the total value of awards dispersed was 70% less than average [Trump Administration Funding Delays Worry NIH Grant Recipients](https://news.bloomberglaw.com/health-law-and-business/trump-administration-funding-delays-worry-nih-grant-recipients-23). One NIH institute warned it could leave as much as $500 million unused due to insufficient staff to process grants. The delays stem partly from an OMB memo requiring more detailed spending plans [Trump Administration Funding Delays Worry NIH Grant Recipients](https://news.bloomberglaw.com/health-law-and-business/trump-administration-funding-delays-worry-nih-grant-recipients-23) and from DOGE-related staffing reductions at NIH. The Trump administration's FY2027 budget proposal, released April 3, 2026, requests $41 billion for NIH — a further $5 billion cut [Trump budget proposal aims to cut $5 billion from NIH - STAT News](https://www.statnews.com/2026/04/03/trump-budget-nih-5-billion-cut-in-2027/). Congressional hearings have shown bipartisan concern over slow grant distribution. The question centers on whether the administrative slowdown constitutes a de facto impoundment of congressionally appropriated funds.

**Exact later resolution packet**

Adjudicated: The primary source, the AAMC NIH funding tracker (data through May 15, 2026, last updated May 18, 2026 - the latest data point before the June 1 deadline), reports NIH obligated only $5.8 billion of its ~$38 billion estimated FY2026 extramural funding, i.e. 15%, far below the 50% / $19 billion threshold. FY2026 appropriations remained at the enacted $47.2 billion (P.L. 119-75) with no rescission or court order changing the total, so the ~$38B denominator applies; AAMC notes forward-funding surges historically occur at the END of June, after the deadline, making any jump to $19B by June 1 implausible. The question resolves YES; an earlier automated annulment was unwarranted since the criteria explicitly allow credible third-party trackers and the AAMC data covered the relevant window.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-22. `adb8e6fb-5f80-5d2b-8773-818a1c7db8e6`

- Present date: `2026-05-14 03:28:32.416092`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will the U.S. Supreme Court's opinion in Sripetch v. SEC be unanimous?

**Resolution criteria**

This question resolves based on the official opinion in Sripetch v. Securities and Exchange Commission (No. 25-466) released by the U.S. Supreme Court on or after May 12, 2026 (Eastern Time).

**Resolution as YES:** The opinion is "unanimous" if every participating Justice joins the opinion of the Court (the majority opinion) with no separate concurring opinions and no dissenting opinions. Specifically:
- If all 9 Justices participate, the vote must be 9-0 with no separate concurrences.
- If a Justice is recused or otherwise does not participate (as indicated on the opinion's caption, e.g., "Justice X took no part in the consideration or decision of this case"), the opinion is unanimous if all remaining participating Justices join the opinion of the Court with no separate writings.

**Resolution as NO:** The opinion is not unanimous if:
- Any Justice files a dissenting opinion, OR
- Any Justice files an opinion "concurring in the judgment" (agreeing with the result but not the majority's legal reasoning), OR
- Any Justice files a concurring opinion (even one that also joins the majority opinion in full counts as a separate writing, but does NOT defeat unanimity—only opinions that decline to join the majority opinion in full, or concurrences in the judgment only, defeat unanimity).

To clarify: A decision is still considered unanimous if a Justice writes a concurrence that also joins the opinion of the Court in full. It is NOT unanimous if any Justice concurs only in the judgment without joining the opinion of the Court, or if any Justice dissents.

**If a Justice is recused or does not participate:** The threshold adjusts to require unanimity among all participating Justices (e.g., 8-0 if one Justice is recused).

**Resolution source:** The official slip opinion published on the Supreme Court's website at https://www.supremecourt.gov/opinions/slipopinion/25. The vote breakdown and any separate opinions are indicated on the syllabus and opinion pages.

If the opinion has not been released by June 30, 2026 (Eastern Time), this question resolves as N/A.

**Pre-cutoff background**

Sripetch v. Securities and Exchange Commission (Docket No. 25-466) concerns whether the SEC may seek equitable disgorgement under 15 U.S.C. §§ 78u(d)(5) and (d)(7) without demonstrating that investors suffered pecuniary harm. The case arose from a circuit split on this question [https://www.scotusblog.com/cases/case-files/sripetch-v-securities-and-exchange-commission/](https://www.scotusblog.com/cases/case-files/sripetch-v-securities-and-exchange-commission/).

Oral arguments were held on April 20, 2026 (Eastern Time) [https://www.scotusblog.com/cases/case-files/sripetch-v-securities-and-exchange-commission/](https://www.scotusblog.com/cases/case-files/sripetch-v-securities-and-exchange-commission/). Analysis of the oral arguments suggests the Justices appeared broadly skeptical of requiring a showing of investor harm, potentially favoring the SEC's position. However, the specific legal reasoning—such as whether disgorgement is properly characterized as equitable relief versus a civil penalty—could produce concurrences or partial dissents even if the bottom-line result commands broad agreement [https://www.scotusblog.com/cases/case-files/sripetch-v-securities-and-exchange-commission/](https://www.scotusblog.com/cases/case-files/sripetch-v-securities-and-exchange-commission/). Recent Supreme Court cases involving SEC enforcement authority (e.g., SEC v. Jarkesy, Liu v. SEC) have produced varied vote splits, making unanimity uncertain.

The opinion is expected to be released before the end of the October 2025 Term, typically by late June 2026.

**Exact later resolution packet**

The question asks whether the Supreme Court's opinion in Sripetch v. Securities and Exchange Commission (No. 25-466) was "unanimous," per the specific definition in the resolution criteria.

Facts established from the official Supreme Court sources:
- The slip opinion in Sripetch v. SEC (Docket No. 25-466) was listed as Opinion No. 44, released June 4, 2026, on the Court's slip opinion index (https://www.supremecourt.gov/opinions/slipopinion/25). The holding: "A showing of pecuniary loss to investors is not required before the SEC may obtain a disgorgement award under 15 U.S.C. §78u(d)(5) or §78u(d)(7)." [https://www.supremecourt.gov/opinions/slipopinion/25](https://www.supremecourt.gov/opinions/slipopinion/25)
- Because the opinion was released June 4, 2026 (before the June 30, 2026 cutoff), the question is NOT annulled/N/A.
- The official slip opinion PDF (https://www.supremecourt.gov/opinions/25pdf/25-466_5i26.pdf) syllabus states: "GORSUCH, J., delivered the opinion for a unanimous Court. THOMAS, J., filed a concurring opinion." There were no dissenting opinions, no opinions concurring only in the judgment, and no Justice took no part in the case (no recusals). [https://www.supremecourt.gov/opinions/25pdf/25-466_5i26.pdf](https://www.supremecourt.gov/opinions/25pdf/25-466_5i26.pdf)

Applying the resolution criteria:
- The criteria explicitly state: "A decision is still considered unanimous if a Justice writes a concurrence that also joins the opinion of the Court in full. It is NOT unanimous if any Justice concurs only in the judgment without joining the opinion of the Court, or if any Justice dissents."
- The syllabus's description of Gorsuch delivering "the opinion for a unanimous Court" confirms that all nine Justices — including Justice Thomas — joined the majority opinion in full. (Had Thomas declined to join and merely concurred in the judgment, the syllabus would list which Justices joined the opinion and describe Thomas as "concurring in the judgment"; instead it says "unanimous Court.") [https://www.supremecourt.gov/opinions/25pdf/25-466_5i26.pdf](https://www.supremecourt.gov/opinions/25pdf/25-466_5i26.pdf)
- Justice Thomas's separate concurring opinion is a separate writing, but because he joined the opinion of the Court in full, it does NOT defeat unanimity under the criteria.
- There were no dissents and no concurrences in the judgment only. [https://www.supremecourt.gov/opinions/25pdf/25-466_5i26.pdf](https://www.supremecourt.gov/opinions/25pdf/25-466_5i26.pdf)

Therefore, the opinion satisfies the criteria's definition of unanimous, and the question resolves YES (1).

Resolution source (official slip opinion): https://www.supremecourt.gov/opinions/25pdf/25-466_5i26.pdf ; index: https://www.supremecourt.gov/opinions/slipopinion/25

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-23. `97a98e4a-2bbf-58ea-99cb-b698f1612af5`

- Present date: `2026-05-03 09:40:14.527299`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-05-27 00:00:00`

**Question**

Will Giovanni Reyna be included in the USMNT's 26-player World Cup roster announced on May 26, 2026?

**Resolution criteria**

This question resolves **Yes** if Giovanni Reyna (born November 13, 2002; Transfermarkt ID 504215) is named as one of the 26 players on the official USMNT roster for the 2026 FIFA World Cup, as announced by U.S. Soccer on May 26, 2026 at approximately 3:00 PM ET (19:00 UTC).

This question resolves **No** if Reyna is not included in the announced 26-player roster.

**"Included"** means being one of the 26 players named in the initial roster announcement published by U.S. Soccer on May 26, 2026. The primary resolution source is the official U.S. Soccer announcement at https://www.ussoccer.com/stories (or equivalent official U.S. Soccer news page). Secondary sources include major sports outlets such as ESPN, FOX Sports, and The Athletic.

**Injury replacement handling:** If Reyna is named in the May 26 announcement but is subsequently replaced due to injury before the resolution date, the question still resolves **Yes** (inclusion is determined at the time of the May 26 announcement). Conversely, if Reyna is not named on May 26 but is later added as an injury replacement for another player before June 1, the question resolves **No**, as he was not part of the original announced roster.

If the roster size changes from 26 due to a FIFA rule change, this question resolves based on the official USMNT roster as announced on May 26, regardless of its size.

**Pre-cutoff background**

The U.S. Men's National Team (USMNT) will reveal its 26-player roster for the 2026 FIFA World Cup on May 26, 2026, at 3:00 PM ET (19:00 UTC) during a live event on FOX from The Rooftop at Pier 17 in New York City [Mauricio Pochettino to Reveal USMNT World Cup Roster on May 26](https://www.ussoccer.com/stories/2026/04/usmnt/mauricio-pochettino-reveal-world-cup-roster-may-26-new-york-city-fox). According to FIFA regulations, squads for the 2026 World Cup must contain between 23 and 26 players (including at least three goalkeepers). A provisional list of 35–55 players was due to FIFA by May 11, 2026, and the final squad must be submitted by May 30, 2026. Injury replacements are permitted up to 24 hours before a team's first match, provided the replacement is drawn from the provisional list [How Many Players Can Each National Team Call up for the 2026 ...](https://www.beinsports.com/en-us/soccer/fifa-world-cup-2026/articles/how-many-players-can-each-national-team-call-up-for-the-2026-fifa-world-cup-2026-04-22).

Giovanni Reyna (born November 13, 2002) is an American attacking midfielder currently at Borussia Mönchengladbach in the Bundesliga. His 2025/26 club season has been severely hampered by recurring muscle and thigh injuries. As of March 2026, he had recorded 0 goals and 0 assists in the Bundesliga season and played only 26 minutes across two appearances in 2026 [Gio Reyna “can be very useful” for USMNT despite club woes](https://sbisoccer.com/2026/03/gio-reyna-can-be-very-useful-for-usmnt-despite-club-woes). Despite this, USMNT head coach Mauricio Pochettino included Reyna in the March 2026 camp roster, publicly calling him a "very special talent" who can be "very useful" to the national team [Gio Reyna “can be very useful” for USMNT despite club woes](https://sbisoccer.com/2026/03/gio-reyna-can-be-very-useful-for-usmnt-despite-club-woes). ESPN has reported that Reyna, along with Alex Zendejas and Diego Luna, appears to be competing for one attacking midfield spot on the final roster [Mauricio Pochettino to Reveal USMNT World Cup Roster on May 26](https://www.ussoccer.com/stories/2026/04/usmnt/mauricio-pochettino-reveal-world-cup-roster-may-26-new-york-city-fox). Reyna's injury history at Transfermarkt shows multiple fitness issues in the 2025/26 season including muscular problems (33 days), thigh problems (22 days), and a fitness-related absence (15 days).

For reference:
- USMNT official page: https://www.ussoccer.com/teams/usmnt
- FIFA 2026 World Cup squad regulations: https://www.fifa.com/en/tournaments/mens/worldcup/articles/number-players-squad-sizes
- Giovanni Reyna player profile: https://www.transfermarkt.us/giovanni-reyna/profil/spieler/504215

**Exact later resolution packet**

YES. The controlling source is the official U.S. Soccer May 26, 2026 announcement at https://ussoccer.com/stories/2026/05/usmnt/us-mens-national-team-head-coach-mauricio-pochettino-names-26-player-roster-for-fifa-world-cup-2026, titled “U.S. Men's National Team Head Coach Mauricio Pochettino Names 26-Player Roster for FIFA World Cup 2026” [U.S. Men's National Team Head Coach Mauricio Pochettino Names ...](https://ussoccer.com/stories/2026/05/usmnt/us-mens-national-team-head-coach-mauricio-pochettino-names-26-player-roster-for-fifa-world-cup-2026). That announcement is dated May 26, 2026, states that Mauricio Pochettino named the 26-player USMNT roster for the 2026 FIFA World Cup, and its roster list includes “Gio Reyna (Borussia Mönchengladbach/GER; 36/9; Bedford, N.Y.)” under midfielders [U.S. Men's National Team Head Coach Mauricio Pochettino Names ...](https://ussoccer.com/stories/2026/05/usmnt/us-mens-national-team-head-coach-mauricio-pochettino-names-26-player-roster-for-fifa-world-cup-2026). An official U.S. Soccer roster profile page for the same World Cup roster, https://ussoccer.com/stories/2026/05/usmnt/meet-the-team-world-cup-roster, identifies “#7 - GIO REYNA” as a midfielder born November 13, 2002, confirming this is Giovanni Reyna as specified in the question [Meet the Team: USMNT Roster For FIFA World Cup 2026 - US Soccer](https://ussoccer.com/stories/2026/05/usmnt/meet-the-team-world-cup-roster). Because the resolution criteria depend only on whether Giovanni/Gio Reyna was included in the initial May 26 U.S. Soccer roster announcement, and he was named there, the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-24. `6c85961f-c812-5dee-a6ae-0d2985e879a4`

- Present date: `2026-05-03 11:10:54.011470`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the EU reach a trilogue agreement on postponing the AI Act's Article 6(2) high-risk AI system obligations by June 1, 2026?

**Resolution criteria**

This question resolves **YES** if, on or after May 2, 2026, and by 23:59 UTC on June 1, 2026, the European Parliament and the Council of the EU reach a political agreement (provisional trilogue agreement) on amendments to the EU AI Act that explicitly postpone the August 2, 2026 application date for [Article 6(2)](https://artificialintelligenceact.eu/article/6/) high-risk AI system obligations (i.e., obligations applicable to AI systems listed in [Annex III](https://artificialintelligenceact.eu/annex/3/) of [Regulation 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)).

This question resolves **NO** if no such political agreement is reached by 23:59 UTC on June 1, 2026.

A "political agreement" means a provisional deal announced by both co-legislators, as is standard practice following a successful trilogue. This does not require formal adoption (vote in plenary or Council); a provisional agreement suffices.

**Resolution source:** Official announcements from the [European Parliament Press Room](https://www.europarl.europa.eu/news/en/press-room) or the [Council of the EU Press Page](https://www.consilium.europa.eu/en/press/press-releases/), or credible reporting from Reuters, Euractiv, or similar outlets confirming the trilogue outcome.

**Pre-cutoff background**

The EU AI Act ([Regulation 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)) imposes obligations on providers and deployers of high-risk AI systems as defined in [Article 6(2)](https://artificialintelligenceact.eu/article/6/), which references AI systems listed in [Annex III](https://artificialintelligenceact.eu/annex/3/). These obligations—covering risk management, data governance, transparency, human oversight, and conformity assessment—are scheduled to become enforceable on August 2, 2026.

On November 19, 2025, the European Commission proposed the "Digital Omnibus" package, which included a formal legislative proposal (COM document) to amend the AI Act by postponing the August 2, 2026 high-risk compliance deadlines by up to 16 months [Is the EU AI Act Delayed? 2026 Status Check | Modulos Blog](https://www.modulos.ai/blog/is-the-eu-ai-act-delayed/). The European Parliament's committees voted in March 2026 to support a postponement but proposed a shorter delay (to November 2, 2026, rather than February 2027 as the Commission proposed).

The Council of the EU adopted its negotiating position on March 13, 2026. However, when the European Parliament, the Council, and the Commission held their second political trilogue on April 28, 2026, negotiations collapsed after 12 hours without agreement [EU countries, lawmakers fail to reach deal on watered-down AI rules](https://www.reuters.com/sustainability/boards-policy-regulation/eu-countries-lawmakers-fail-reach-deal-watered-down-ai-rules-2026-04-29/). The sticking point was disagreement over the conformity-assessment architecture for AI in regulated products under Annex I—specifically whether Section A products should move to Section B [Is the EU AI Act Delayed? 2026 Status Check | Modulos Blog](https://www.modulos.ai/blog/is-the-eu-ai-act-delayed/).

As of April 30, 2026, no delay has been formally adopted; the original August 2, 2026 deadline remains legally in force [Is the EU AI Act Delayed? 2026 Status Check | Modulos Blog](https://www.modulos.ai/blog/is-the-eu-ai-act-delayed/). A follow-up trilogue is expected around May 13, 2026. The Cypriot Council Presidency aims to close the file before its term ends on June 30, 2026 [Is the EU AI Act Delayed? 2026 Status Check | Modulos Blog](https://www.modulos.ai/blog/is-the-eu-ai-act-delayed/).

**Exact later resolution packet**

The question resolves YES.

Resolution window: YES requires a provisional trilogue political agreement between the European Parliament and the Council of the EU, reached on or after May 2, 2026 and by 23:59 UTC on June 1, 2026, that explicitly postpones the August 2, 2026 application date for Article 6(2) high-risk AI obligations (Annex III systems).

Evidence:
- On May 7, 2026, the Council of the EU and the European Parliament announced a provisional political agreement on targeted amendments to the EU AI Act (the "Digital Omnibus on AI"). This is documented in the official Council of the EU press release ("Artificial Intelligence: Council and Parliament agree to simplify and streamline rules," https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/) and confirmed by Hogan Lovells [EU legislators agree to delay for high-risk AI rules - Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-legislators-agree-to-delay-for-highrisk-ai-rules): "On May 7, 2026, the Council of the EU and the European Parliament announced their provisional agreement on targeted amendments to the EU AI Act."
- The agreement explicitly postpones the high-risk obligations. Per Hogan Lovells [EU legislators agree to delay for high-risk AI rules - Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-legislators-agree-to-delay-for-highrisk-ai-rules): "For standalone high-risk AI systems that are classified under Annex III of the AI Act, the application of the relevant requirements is deferred until December 2, 2027." This directly satisfies the requirement that the agreement postpones the Article 6(2)/Annex III high-risk obligations beyond the original August 2, 2026 date.
- The earlier April 28, 2026 trilogue had collapsed (per the question description, citing Reuters), but the follow-up trilogue produced an overnight deal concluding in the early hours of May 7, 2026 (corroborated by multiple law-firm advisories: Bird & Bird, White & Case, Gibson Dunn, DLA Piper, Orrick).

Date check: May 7, 2026 falls within the window (after May 2, 2026 and before 23:59 UTC June 1, 2026). 

Provisional vs. formal: The resolution criteria explicitly state that a provisional agreement suffices and formal adoption (plenary/Council vote) is NOT required. Sources confirm this was a provisional political agreement still pending formal adoption (expected before August 2, 2026), which matches the YES criteria exactly.

Annex I vs Annex III note: The April 28 collapse concerned the Annex I (Section A vs B) conformity-assessment architecture. The May 7 deal resolved the negotiation and explicitly deferred the Annex III standalone high-risk obligations to December 2, 2027 [EU legislators agree to delay for high-risk AI rules - Hogan Lovells](https://www.hoganlovells.com/en/publications/eu-legislators-agree-to-delay-for-highrisk-ai-rules), so the specific Annex III postponement required by the question is confirmed.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-25. `6b8f801e-30ec-5a81-b2c5-0b88c6c97ce7`

- Present date: `2026-05-14 03:09:55.653976`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-30T00:00:00`

**Question**

Will the Supreme Court's majority opinion in Trump v. Slaughter explicitly overrule Humphrey's Executor v. United States by June 30, 2026?

**Resolution criteria**

This question resolves **Yes** if the majority opinion of the Supreme Court in Trump v. Slaughter (No. 25-332) explicitly overrules Humphrey's Executor v. United States, 295 U.S. 602 (1935) (https://en.wikipedia.org/wiki/Humphrey%27s_Executor_v._United_States). Specifically, the majority opinion must use the word "overrule," "overruled," or state that Humphrey's Executor is "no longer good law" or words to clearly equivalent effect.

This question resolves **No** if:
- The majority opinion does not use such language (e.g., it merely distinguishes, narrows, or limits Humphrey's Executor without explicitly overruling it), OR
- No opinion is issued by June 30, 2026.

Resolution is determined solely by the text of the majority opinion. Concurrences, dissents, and other separate writings do not count.

Resolution source: The opinion as published on the Supreme Court's website (https://www.supremecourt.gov/opinions/slipopinions.aspx) or the SCOTUSblog case page (https://www.scotusblog.com/cases/trump-v-slaughter-2/).

**Pre-cutoff background**

Trump v. Slaughter (No. 25-332) is a pending Supreme Court case concerning whether the President may remove members of the Federal Trade Commission (FTC) at will, challenging the precedent set by Humphrey's Executor v. United States, 295 U.S. 602 (1935) (https://en.wikipedia.org/wiki/Humphrey%27s_Executor_v._United_States). Humphrey's Executor held that Congress may protect independent agency commissioners from presidential removal except for "inefficiency, neglect of duty, or malfeasance in office."

The case was argued on December 8, 2025, and as of May 12, 2026, no opinion has been issued [Trump v. Slaughter (Independent Agencies) (25-332) - SCOTUSblog](https://www.scotusblog.com/cases/trump-v-slaughter-2/). The SCOTUSblog case page indicates an "Opinions Live Blog" is scheduled for May 14, 2026, suggesting opinions may be released soon [Trump v. Slaughter (Independent Agencies) (25-332) - SCOTUSblog](https://www.scotusblog.com/cases/trump-v-slaughter-2/). The Supreme Court's term typically ends in late June, so an opinion is expected before July 2026.

Legal analysts have suggested the Court could take multiple approaches: (1) explicitly overrule Humphrey's Executor entirely; (2) narrow or "mend" it by distinguishing types of agencies or powers exercised, without formally overruling it; or (3) rule on other grounds. SCOTUSblog analysis has characterized one likely path as "mend it, don't end it," suggesting a full overruling is plausible but far from certain (https://www.scotusblog.com/2025/10/is-humphreys-executor-headed-for-slaughter/).

Case docket: https://www.supremecourt.gov/docket/docketfiles/html/public/25-332.html
SCOTUSblog case page: https://www.scotusblog.com/cases/trump-v-slaughter-2/

**Exact later resolution packet**

The question resolves YES.

**Antecedent conditions met:** The Supreme Court issued its opinion in Trump v. Slaughter (No. 25-332) on June 29, 2026, which is on or before the June 30, 2026 deadline. This is confirmed by the official Supreme Court slip opinion published at https://www.supremecourt.gov/opinions/25pdf/25-332_qn12.pdf [1300b8] and by SCOTUSblog [f13b33].

**The majority opinion explicitly overruled Humphrey's Executor:** The majority opinion was delivered by Chief Justice Roberts (6–3 vote, joined by Justices Thomas, Alito, Gorsuch, Kavanaugh, and Barrett). The majority opinion contains the explicit statement: "If anything more is left of Humphrey's, the Court overrules it." — using the exact word "overrules" required by the resolution criteria [1300b8]. This language appears in the majority opinion itself, not in a concurrence or dissent (Justice Gorsuch concurred; Justice Sotomayor dissented, joined by Justices Kagan and Jackson) [1300b8].

**Corroboration:** Multiple independent authoritative sources confirm the majority opinion explicitly overruled the 1935 precedent. Sidley Austin's analysis states "In Trump v. Slaughter, a 6–3 majority overruled Humphrey's Executor v. United States" [35c1f5]. The SCOTUSblog case page and opinion analysis ("Supreme Court allows Trump to fire FTC commissioner and overturns major restraint on presidential power") confirm the same [f13b33].

**Resolution criteria satisfied:**
- Opinion issued by deadline: YES (June 29, 2026, before June 30, 2026).
- Based solely on the text of the majority opinion (not concurrences/dissents): YES.
- Contains the word "overrule"/"overrules": YES ("the Court overrules it").
- Explicitly overrules rather than merely narrowing/distinguishing: YES.

Therefore the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-26. `e54a0372-5d92-57ab-9c83-46f38c02bc0e`

- Present date: `2026-05-13 23:19:25.788217`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-06-12T00:00:00`

**Question**

Will the Dutch Eerste Kamer (Senate) pass the 'Implementation Act EU Asylum and Migration Pact 2026' (wetsvoorstel 36871) before June 12, 2026?

**Resolution criteria**

This question resolves as **Yes** if the Eerste Kamer der Staten-Generaal (the Dutch Senate) formally votes to adopt wetsvoorstel 36871 ('Uitvoerings- en implementatiewet Asiel- en migratiepact 2026') before 23:59 CEST on June 12, 2026. "Passing" means a majority of votes cast in favor of the bill in a final vote (stemming).

This question resolves as **No** if:
- The Eerste Kamer rejects the bill, OR
- No final vote to adopt the bill has taken place before the deadline.

The passage must occur on or after May 12, 2026.

**Resolution source:** The official Eerste Kamer website (https://www.eerstekamer.nl/) and/or the Tweede Kamer dossier page for bill 36871 (https://www.tweedekamer.nl/kamerstukken/wetsvoorstellen/detail?qry=wetsvoorstel%3A36871&cfg=wetsvoorsteldetails), which track the legislative status and voting records of the bill.

**Pre-cutoff background**

The EU Asylum and Migration Pact, consisting of nine regulations and one directive, is scheduled to enter into force on June 12, 2026. The Netherlands must implement this pact through national legislation. The Dutch government submitted the 'Uitvoerings- en implementatiewet Asiel- en migratiepact 2026' (wetsvoorstel 36871) to parliament for this purpose.

The Tweede Kamer (House of Representatives) passed the bill on April 2, 2026, with 105 votes in favor and 45 against [36871, eindtekst d.d. 2 april 2026 - Tweede Kamer](https://www.tweedekamer.nl/kamerstukken/detail?id=2025Z22479&did=2026D15698). The bill is now before the Eerste Kamer (Senate) for approval, which is the final parliamentary step before it can become law.

As of May 13, 2026, the bill is in the Senate phase of the legislative process. The political environment around asylum legislation is turbulent: the Senate rejected the separate 'Asylum Emergency Measures Act' (Asielnoodmaatregelenwet) in April 2026, and the cabinet is preparing replacement measures. This raises genuine uncertainty about whether the Senate will approve this implementation bill before the EU deadline of June 12, 2026. Additionally, 447 questions were submitted during the Tweede Kamer phase, indicating significant parliamentary scrutiny of the bill's contents.

The official dossier page for the bill is: https://www.tweedekamer.nl/kamerstukken/wetsvoorstellen/detail?qry=wetsvoorstel%3A36871&cfg=wetsvoorsteldetails

**Exact later resolution packet**

The question resolves YES. The Dutch Eerste Kamer (Senate) formally voted to adopt wetsvoorstel 36871 ('Uitvoerings- en implementatiewet Asiel- en migratiepact 2026') on Tuesday, May 26, 2026, via a "stemming bij zitten en opstaan" (vote by sitting and standing), and the bill was adopted (aangenomen) [Uitvoerings- en implementatiewet Asiel- en migratiepact 2026 (36.871)](https://www.eerstekamer.nl/wetsvoorstel/36871_uitvoerings_en) [Senaat steunt Europees asiel- en migratiepact](https://www.eerstekamer.nl/nieuws/20260526/senaat_steunt_europees_asiel_en).

Checklist verification:
- Chamber: The vote was in the Eerste Kamer (Senate), confirmed by the official Eerste Kamer dossier page https://www.eerstekamer.nl/wetsvoorstel/36871_uitvoerings_en and the Eerste Kamer news release https://www.eerstekamer.nl/nieuws/20260526/senaat_steunt_europees_asiel_en [Uitvoerings- en implementatiewet Asiel- en migratiepact 2026 (36.871)](https://www.eerstekamer.nl/wetsvoorstel/36871_uitvoerings_en) [Senaat steunt Europees asiel- en migratiepact](https://www.eerstekamer.nl/nieuws/20260526/senaat_steunt_europees_asiel_en).
- Bill number/title: The bill is exactly 36871, "Uitvoerings- en implementatiewet Asiel- en migratiepact 2026" [Uitvoerings- en implementatiewet Asiel- en migratiepact 2026 (36.871)](https://www.eerstekamer.nl/wetsvoorstel/36871_uitvoerings_en).
- Timing (on/after May 12, 2026): The final vote took place on May 26, 2026, which is on or after May 12, 2026 [Uitvoerings- en implementatiewet Asiel- en migratiepact 2026 (36.871)](https://www.eerstekamer.nl/wetsvoorstel/36871_uitvoerings_en).
- Timing (before 23:59 CEST June 12, 2026): May 26, 2026 is comfortably before the June 12, 2026 deadline (the pact itself entered into force on June 12, 2026) [Uitvoerings- en implementatiewet Asiel- en migratiepact 2026 (36.871)](https://www.eerstekamer.nl/wetsvoorstel/36871_uitvoerings_en).
- Majority in favor: The bill passed with a majority. Voting FOR: CDA, SGP, D66, VVD, PVV, JA21, BBB, 50PLUS, Fractie-Walenkamp, Fractie-Beukering, Fractie-Van Gasteren. Voting AGAINST: GroenLinks-PvdA, Volt, ChristenUnie, FVD, SP, PvdD, Fractie-Visseren-Hamakers, Fractie-Van de Sanden. This corresponds to reporting of 45 of 74 votes in favor [Uitvoerings- en implementatiewet Asiel- en migratiepact 2026 (36.871)](https://www.eerstekamer.nl/wetsvoorstel/36871_uitvoerings_en).
- Distinction from other legislation: This is distinct from the separate 'Asielnoodmaatregelenwet' (Asylum Emergency Measures Act), which the Senate rejected in April 2026. Bill 36871 (the EU pact implementation bill) is a different bill and was PASSED on May 26, 2026 [Uitvoerings- en implementatiewet Asiel- en migratiepact 2026 (36.871)](https://www.eerstekamer.nl/wetsvoorstel/36871_uitvoerings_en) [Senaat steunt Europees asiel- en migratiepact](https://www.eerstekamer.nl/nieuws/20260526/senaat_steunt_europees_asiel_en).

Evidence URLs (official resolution sources):
- Eerste Kamer dossier: https://www.eerstekamer.nl/wetsvoorstel/36871_uitvoerings_en (states: "De Eerste Kamer heeft het voorstel op 26 mei 2026 na stemming bij zitten en opstaan aangenomen.")
- Eerste Kamer news: https://www.eerstekamer.nl/nieuws/20260526/senaat_steunt_europees_asiel_en
- Tweede Kamer dossier: https://www.tweedekamer.nl/kamerstukken/wetsvoorstellen/detail?qry=wetsvoorstel%3A36871&cfg=wetsvoorsteldetails

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-27. `1177ed01-9dc4-594d-9656-3eac4d014d42`

- Present date: `2026-05-01 12:53:25.643677`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Shas formally leave the Israeli parliamentary coalition by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026 and before June 1, 2026 at 23:59 UTC, the Shas party formally leaves the Israeli parliamentary coalition. "Formally leave" is defined as meeting at least one of the following conditions:

1. Shas party leadership (the party chairman or an authorized spokesperson) issues an official public declaration that the party is leaving the parliamentary coalition and will no longer support the government in confidence votes; OR
2. Shas Knesset members vote against the government in a no-confidence motion or actively support a motion to dissolve the Knesset.

Merely withdrawing ministers from the cabinet (which already occurred in July 2025) does NOT count unless accompanied by condition (1) or (2) above. Temporary threats or conditional ultimatums that are later walked back do not count—the departure must be in effect as of the resolution date.

This question resolves **No** if Shas remains part of the parliamentary coalition (even without cabinet ministers) through June 1, 2026 at 23:59 UTC.

**Resolution sources:** Credible reporting from major Israeli news outlets, including:
- The Times of Israel (https://www.timesofisrael.com/)
- Haaretz (https://www.haaretz.com/)
- The Jerusalem Post (https://www.jpost.com/)
- Official Knesset records (https://main.knesset.gov.il/EN/)
- Major international wire services (Reuters, AP)

**Pre-cutoff background**

Israel's governing coalition under Prime Minister Benjamin Netanyahu has faced repeated crises over the issue of Haredi (ultra-Orthodox) military draft exemptions. In July 2025, United Torah Judaism (UTJ) fully withdrew from the coalition, and Shas pulled its ministers from the cabinet but announced it would remain part of the parliamentary coalition, preserving Netanyahu's narrow majority [Ultra-Orthodox party quits Israeli cabinet but throws Netanyahu a ...](https://www.reuters.com/world/middle-east/second-ultra-orthodox-party-quits-israeli-government-depriving-netanyahu-2025-07-16/).

**Shas** is an ultra-Orthodox Sephardic political party in Israel founded in 1984, holding 11 seats in the current Knesset (see https://en.wikipedia.org/wiki/Shas). **United Torah Judaism (UTJ)** is an Ashkenazi ultra-Orthodox political alliance (see https://en.wikipedia.org/wiki/United_Torah_Judaism).

Despite threats, Haredi parties ultimately supported the 2026 state budget in early 2026, though the draft exemption bill remained frozen. On April 26, 2026, Israel's High Court of Justice issued a landmark ruling ordering the government to impose personal financial sanctions on Haredi draft evaders, creating unprecedented pressure on Haredi politicians. Shas has stated it will only fully rejoin the government if a viable Haredi enlistment bill is advanced. As of early May 2026, Shas remains in a liminal position—its ministers are out of cabinet but the party continues to support the coalition in parliamentary votes, giving Netanyahu a razor-thin majority. The April 26 court ruling on sanctions significantly escalates the pressure on Shas to either secure legislative relief or formally exit the coalition entirely.

The question captures whether this escalating judicial pressure, combined with the frozen draft exemption bill, will push Shas to fully sever its parliamentary coalition support—an outcome that would likely trigger the collapse of Netanyahu's government.

**Exact later resolution packet**

RESOLUTION: YES (1).

The question resolves YES under condition (2) of the resolution criteria: "Shas Knesset members vote against the government in a no-confidence motion or actively support a motion to dissolve the Knesset." This event occurred within the required window (on or after April 30, 2026 and before June 1, 2026 at 23:59 UTC).

KEY EVIDENCE:
- On May 20, 2026, the Knesset passed a preliminary reading of a bill to dissolve itself. The Guardian (May 22, 2026) reported the dissolution vote received the backing of 110 of 120 lawmakers and that the coalition "cracked," with Netanyahu's partners saying they no longer trusted the government [c6712e]. The official Knesset press release confirms the "Bill for Dissolution of the Twenty-Fifth Knesset, 2026" was approved in preliminary reading 110-0 [d48f56].
- Crucially, the Haredi parties — explicitly including Shas (11 seats) and UTJ (7 seats) — decided to support the vote for early elections and "together... were able to remove the coalition's majority and pass the vote" (Unpacked, May 20, 2026) [604e83]. The Times of Israel headlined a follow-up dissolution vote "106 MKs vote to disband parliament as Haredi parties turn against coalition over IDF service exemptions" (Google snippet).
- This was an actual recorded vote (not a mere threat) and was sustained rather than walked back: a Jerusalem Post article dated June 1, 2026 confirms Shas lawmakers continued participating in advancing the dissolution bill, with the first reading set for the plenum that day, and there was no reversal before the deadline [0f3833]. A further Jerusalem Post report dated June 2, 2026 confirms the dissolution bill passed its first reading 106-0 [8e561e].

WHY THIS MEETS THE BAR (and is not merely the 2025 cabinet withdrawal):
The criteria carefully distinguish Shas's July 2025 withdrawal of ministers (which does NOT count) from a formal exit. Wikipedia confirms Shas only withdrew ministers in July 2025 while remaining in the parliamentary coalition [644eba]. The May 20, 2026 event is categorically different: Shas MKs actively cast votes supporting a motion to dissolve the Knesset, which is precisely the trigger described in condition (2). This is a substantive parliamentary action against the government's continuation, satisfying the literal text of the resolution criteria.

NUANCE: Netanyahu's own Likud (MK Ofir Katz) submitted the specific dissolution bill that passed, reportedly to control the timing/election date, which is why several wire-service summaries framed it as a "coalition-submitted" bill [d83687, d48f56]. However, the underlying reality reported across Israeli outlets is that the Haredi parties (including Shas) had turned against the coalition and threw their weight behind dissolution and early elections [604e83]. Regardless of who formally tabled the bill, condition (2) is satisfied because Shas Knesset members actively supported (voted for) a motion to dissolve the Knesset within the resolution window, and that support held through the June 1 deadline.

Sources used: Reuters (May 20, 2026), Times of Israel, Jerusalem Post, Haaretz, Knesset records, The Guardian, Unpacked.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-28. `9e9cf5a3-dfab-5943-b397-54498888c051`

- Present date: `2026-05-14 02:02:50.716527`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-25T00:00:00`

**Question**

Will the Tribunal judiciaire de Paris rule that TotalEnergies breached its duty of vigilance obligations regarding climate in the June 25, 2026 decision?

**Resolution criteria**

This question resolves **Yes** if, in the decision rendered on June 25, 2026 (CEST, UTC+2), the Tribunal judiciaire de Paris explicitly finds that TotalEnergies SE has breached (*manquement*) its duty of vigilance obligations under Article L225-102-4 of the French Commercial Code with respect to climate-related risks.

This question resolves **No** if:
- The court rules that TotalEnergies has **not** breached its duty of vigilance obligations regarding climate; OR
- The court dismisses the case on procedural or jurisdictional grounds without reaching the merits of the duty of vigilance climate claim; OR
- The decision is postponed beyond June 30, 2026 (23:59 CEST).

**Resolution source:** The official judgment text as published by the Tribunal judiciaire de Paris ([https://www.tribunal-judiciaire-paris.justice.fr/](https://www.tribunal-judiciaire-paris.justice.fr/)), or consistent reporting from at least two of the following credible news agencies confirming the ruling's outcome: [Reuters](https://www.reuters.com/), [AFP/France24](https://www.france24.com/), [Le Monde](https://www.lemonde.fr/), [RFI](https://www.rfi.fr/).

A finding of breach on climate grounds resolves Yes regardless of what remedies the court orders (e.g., whether or not it orders production cuts).

**Pre-cutoff background**

On February 17–20, 2026, the Tribunal judiciaire de Paris (Paris Judicial Court) held hearings in the first-ever merits trial on climate change under France's 2017 "duty of vigilance" law (*devoir de vigilance*, [Article L225-102-4 of the French Commercial Code](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000035181820)). The law requires large French companies to establish, publish, and implement a "vigilance plan" identifying and mitigating risks to human rights, fundamental freedoms, health, safety, and the environment arising from their own activities and those of their subsidiaries and supply chains (see [Wikipedia: French corporate duty of vigilance law](https://en.wikipedia.org/wiki/French_corporate_duty_of_vigilance_law)).

The case (*Notre Affaire à Tous and Others v. TotalEnergies*) was brought by a coalition of environmental NGOs (including Notre Affaire à Tous and Sherpa) and the City of Paris. The plaintiffs allege that TotalEnergies failed to include adequate climate measures in its vigilance plan and seek a court order compelling the company to reduce hydrocarbon production and halt new fossil fuel projects to align with a 1.5°C pathway [https://www.rfi.fr/fr/france/20260220-changement-climatique-fin-du-proc%C3%A8s-de-totalenergies-pour-manquement-d%C3%A9cision-le-25-juin-2026](https://www.rfi.fr/fr/france/20260220-changement-climatique-fin-du-proc%C3%A8s-de-totalenergies-pour-manquement-d%C3%A9cision-le-25-juin-2026). TotalEnergies argues it cannot be held solely responsible for the global energy transition and is responding to existing energy demand [https://www.rfi.fr/fr/france/20260220-changement-climatique-fin-du-proc%C3%A8s-de-totalenergies-pour-manquement-d%C3%A9cision-le-25-juin-2026](https://www.rfi.fr/fr/france/20260220-changement-climatique-fin-du-proc%C3%A8s-de-totalenergies-pour-manquement-d%C3%A9cision-le-25-juin-2026).

The ruling is scheduled for June 25, 2026 [https://www.rfi.fr/fr/france/20260220-changement-climatique-fin-du-proc%C3%A8s-de-totalenergies-pour-manquement-d%C3%A9cision-le-25-juin-2026](https://www.rfi.fr/fr/france/20260220-changement-climatique-fin-du-proc%C3%A8s-de-totalenergies-pour-manquement-d%C3%A9cision-le-25-juin-2026).

**Key legal precedent (status quo as of May 13, 2026):** On March 12, 2026, the same court (34th Chamber) issued a landmark ruling in the *Yves Rocher* case (No. 22/04017), the first decision awarding damages under the duty of vigilance law. The court held Yves Rocher liable as a parent company for trade union rights violations at its Turkish subsidiary, confirming the law's extraterritorial reach and classifying it as an "overriding mandatory provision" (*loi de police*) [France – Duty of Vigilance: Landmark Decision Confirming Parent ...](https://www.gibsondunn.com/france-duty-of-vigilance-landmark-decision-confirming-parent-company-liability-for-overseas-subsidiary-conduct-march-2026/). This precedent signals the court's willingness to enforce the duty of vigilance law robustly, though the TotalEnergies case is the first to apply it specifically to climate obligations—an unprecedented step that could require ordering an oil major to curtail production.

In October 2025, a Paris court separately found TotalEnergies guilty of greenwashing, further illustrating increasing judicial scrutiny of the company's climate claims.

**Exact later resolution packet**

RESOLUTION: YES (1).

The question asks whether, in the decision rendered on June 25, 2026, the Tribunal judiciaire de Paris explicitly found that TotalEnergies SE breached (manquement) its duty of vigilance obligations under Article L225-102-4 with respect to climate-related risks. All evidence confirms it did.

CHECKLIST VERIFICATION:

1. Decision rendered by the June 30, 2026 (23:59 CEST) deadline: YES. The judgment was delivered on the scheduled date, June 25, 2026, by the 34th Chamber of the Tribunal judiciaire de Paris (case no. 22/03403). Confirmed by the official court press release [[PDF] Communiqué de presse Jugement du 25 juin 2026 – 34ème chambre](https://www.tribunal-de-paris.justice.fr/sites/default/files/2026-06/CP%2025.06.2026%2034%C3%A8me%20chambre.pdf), Reuters [TotalEnergies must address climate risks linked to its ... - Reuters](https://www.reuters.com/business/energy/totalenergies-must-report-risks-caused-by-emissions-paris-court-rules-2026-06-25/), Le Monde [https://www.lemonde.fr/en/environment/article/2026/06/25/court-rules-oil-and-gas-giant-totalenergies-must-account-for-its-clients-co-emissions_6754878_114.html](https://www.lemonde.fr/en/environment/article/2026/06/25/court-rules-oil-and-gas-giant-totalenergies-must-account-for-its-clients-co-emissions_6754878_114.html), and France24 [Paris court gives TotalEnergies six months to sharpen up its climate ...](https://www.france24.com/en/environment/20260625-court-orders-totalenergies-to-account-for-clients-emissions). No postponement.

2. NOT dismissed on procedural/jurisdictional grounds: The court reached and ruled on the merits of the climate duty-of-vigilance claim. It held that "climate-related risks and impacts to which the company may contribute through its activities fall within the scope of the law on the duty of vigilance for parent companies and ordering companies" [Paris court gives TotalEnergies six months to sharpen up its climate ...](https://www.france24.com/en/environment/20260625-court-orders-totalenergies-to-account-for-clients-emissions). (Note: the case had previously been ruled inadmissible in 2023, but this June 25, 2026 merits judgment did address the substance.) [https://www.lemonde.fr/en/environment/article/2026/06/25/court-rules-oil-and-gas-giant-totalenergies-must-account-for-its-clients-co-emissions_6754878_114.html](https://www.lemonde.fr/en/environment/article/2026/06/25/court-rules-oil-and-gas-giant-totalenergies-must-account-for-its-clients-co-emissions_6754878_114.html)

3. Finding of breach specifically concerns climate-related risks under Article L225-102-4: YES. The official court press release states the court found TotalEnergies' vigilance plan "incomplet" because it did not include Scope 3 greenhouse gas emissions, which the court held are a consequence of the group's oil and gas activity — a matter squarely within the climate scope of Article L225-102-4 [[PDF] Communiqué de presse Jugement du 25 juin 2026 – 34ème chambre](https://www.tribunal-de-paris.justice.fr/sites/default/files/2026-06/CP%2025.06.2026%2034%C3%A8me%20chambre.pdf). This is a finding of climate-related breach (manquement), not human rights or safety. French NGO/press coverage uniformly frames it as "TotalEnergies condamné pour manquement à son devoir de vigilance climatique."

4. Confirmed via official judgment + at least two specified agencies: Confirmed by the Tribunal judiciaire de Paris official press release [[PDF] Communiqué de presse Jugement du 25 juin 2026 – 34ème chambre](https://www.tribunal-de-paris.justice.fr/sites/default/files/2026-06/CP%2025.06.2026%2034%C3%A8me%20chambre.pdf) AND by three specified agencies — Reuters [TotalEnergies must address climate risks linked to its ... - Reuters](https://www.reuters.com/business/energy/totalenergies-must-report-risks-caused-by-emissions-paris-court-rules-2026-06-25/), Le Monde [https://www.lemonde.fr/en/environment/article/2026/06/25/court-rules-oil-and-gas-giant-totalenergies-must-account-for-its-clients-co-emissions_6754878_114.html](https://www.lemonde.fr/en/environment/article/2026/06/25/court-rules-oil-and-gas-giant-totalenergies-must-account-for-its-clients-co-emissions_6754878_114.html), and France24 [Paris court gives TotalEnergies six months to sharpen up its climate ...](https://www.france24.com/en/environment/20260625-court-orders-totalenergies-to-account-for-clients-emissions) — all reporting the same outcome.

5. Distinguishing breach from remedies: The court found the breach (incomplete plan) and issued an injunction ordering TotalEnergies to complete its vigilance plan within six months to include Scope 3 emissions, with a follow-up hearing set for January 21, 2027 [[PDF] Communiqué de presse Jugement du 25 juin 2026 – 34ème chambre](https://www.tribunal-de-paris.justice.fr/sites/default/files/2026-06/CP%2025.06.2026%2034%C3%A8me%20chambre.pdf)[https://www.lemonde.fr/en/environment/article/2026/06/25/court-rules-oil-and-gas-giant-totalenergies-must-account-for-its-clients-co-emissions_6754878_114.html](https://www.lemonde.fr/en/environment/article/2026/06/25/court-rules-oil-and-gas-giant-totalenergies-must-account-for-its-clients-co-emissions_6754878_114.html). The court stopped short of ordering production cuts or other binding business measures requested by plaintiffs — TotalEnergies noted "with satisfaction" that those demands were not granted [TotalEnergies must address climate risks linked to its ... - Reuters](https://www.reuters.com/business/energy/totalenergies-must-report-risks-caused-by-emissions-paris-court-rules-2026-06-25/). Per the resolution criteria, a finding of breach on climate grounds resolves YES regardless of whether the requested remedies (like production cuts) were granted. Therefore this remains YES.

SOURCE URLs:
- Official court press release (PDF): https://www.tribunal-de-paris.justice.fr/sites/default/files/2026-06/CP%2025.06.2026%2034%C3%A8me%20chambre.pdf [[PDF] Communiqué de presse Jugement du 25 juin 2026 – 34ème chambre](https://www.tribunal-de-paris.justice.fr/sites/default/files/2026-06/CP%2025.06.2026%2034%C3%A8me%20chambre.pdf)
- Reuters: https://www.reuters.com/business/energy/totalenergies-must-report-risks-caused-by-emissions-paris-court-rules-2026-06-25/ [TotalEnergies must address climate risks linked to its ... - Reuters](https://www.reuters.com/business/energy/totalenergies-must-report-risks-caused-by-emissions-paris-court-rules-2026-06-25/)
- Le Monde (English): https://www.lemonde.fr/en/environment/article/2026/06/25/court-rules-oil-and-gas-giant-totalenergies-must-account-for-its-clients-co-emissions_6754878_114.html [https://www.lemonde.fr/en/environment/article/2026/06/25/court-rules-oil-and-gas-giant-totalenergies-must-account-for-its-clients-co-emissions_6754878_114.html](https://www.lemonde.fr/en/environment/article/2026/06/25/court-rules-oil-and-gas-giant-totalenergies-must-account-for-its-clients-co-emissions_6754878_114.html)
- France24: https://www.france24.com/en/environment/20260625-court-orders-totalenergies-to-account-for-clients-emissions [Paris court gives TotalEnergies six months to sharpen up its climate ...](https://www.france24.com/en/environment/20260625-court-orders-totalenergies-to-account-for-clients-emissions)

CONCLUSION: The court explicitly found TotalEnergies breached its climate duty of vigilance under Article L225-102-4 (vigilance plan incomplete for omitting Scope 3 emissions), on the merits, on June 25, 2026. Resolution = YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-29. `4e8b4e0d-1cb7-5305-a840-4665db0b29ac`

- Present date: `2026-05-16 06:20:11.240459`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-06-15T00:00:00`

**Question**

Will Ousmane Sonko be elected as President of the PASTEF party at its June 6, 2026 congress?

**Resolution criteria**

This question resolves YES if Ousmane Sonko is elected or re-elected to the top leadership position of the PASTEF party (whether titled "President," "Secretary General," or any equivalent highest-ranking title) at the party congress originally scheduled for June 6, 2026. The election or selection must occur on or after May 12, 2026.

"Elected" means Sonko is formally chosen for the position through any official internal party process—whether by delegate vote, acclamation, or consensus—as announced by the party or reported by credible sources.

Resolution sources: Official PASTEF party communications, Agence de Presse Sénégalaise (APS, https://aps.sn), Reuters (https://www.reuters.com), or Agence France-Presse (AFP). At least one of these sources must confirm the outcome.

Special conditions:
- If the congress is postponed but still takes place before July 1, 2026 at 23:59 UTC, the question resolves based on the actual congress outcome.
- If the congress is postponed beyond July 1, 2026 at 23:59 UTC, or cancelled entirely, the question resolves NO.
- If the top leadership title is changed or renamed during the congress (e.g., from "President" to "Secretary General"), the question still resolves based on whether Sonko holds whatever the highest-ranking party leadership position is at the conclusion of the congress.
- All deadlines are evaluated as of 23:59 UTC on the specified dates.

**Pre-cutoff background**

Ousmane Sonko is the founder and current president of the PASTEF party (Patriotes Africains du Sénégal pour le Travail, l'Éthique et la Fraternité) and serves as Prime Minister of Senegal. A deepening rift has emerged between Sonko and President Bassirou Diomaye Faye, who was elected president in 2024 with PASTEF's backing. In March 2026, Sonko threatened to withdraw the party from government if Faye diverged from the party's vision [https://www.reuters.com/world/africa/senegals-president-faye-says-ruling-party-led-by-pm-sonko-risks-collapse-2026-05-04/](https://www.reuters.com/world/africa/senegals-president-faye-says-ruling-party-led-by-pm-sonko-risks-collapse-2026-05-04/). On May 4, 2026, Faye publicly warned that PASTEF risks "downfall" and stressed the party should be defined by its ideals rather than individual ambitions, while noting his constitutional authority to appoint and dismiss the prime minister [https://www.reuters.com/world/africa/senegals-president-faye-says-ruling-party-led-by-pm-sonko-risks-collapse-2026-05-04/](https://www.reuters.com/world/africa/senegals-president-faye-says-ruling-party-led-by-pm-sonko-risks-collapse-2026-05-04/). The Africa Report describes the situation as an escalating "tug-of-war" over control of the party, the state, and the path to the 2029 presidential election [https://www.theafricareport.com/418019/faye-vs-sonko-who-will-emerge-as-senegals-real-centre-of-power/](https://www.theafricareport.com/418019/faye-vs-sonko-who-will-emerge-as-senegals-real-centre-of-power/). The PASTEF congress scheduled for June 6, 2026 is widely seen as a critical battleground in this power struggle [https://www.theafricareport.com/418019/faye-vs-sonko-who-will-emerge-as-senegals-real-centre-of-power/](https://www.theafricareport.com/418019/faye-vs-sonko-who-will-emerge-as-senegals-real-centre-of-power/). While Sonko is the incumbent leader and party founder, Faye's faction could mount a challenge or push for structural changes to dilute Sonko's authority.

**Exact later resolution packet**

RESOLUTION: YES (1).

The question asks whether Ousmane Sonko was elected/re-elected to the top leadership position of PASTEF at the party congress originally scheduled for June 6, 2026, with the election occurring on or after May 12, 2026 and no later than July 1, 2026 (23:59 UTC).

Every element of the resolution criteria is satisfied:

1) The congress took place. PASTEF held its first national/extraordinary congress on Saturday, June 6, 2026, at the Abdou Diouf International Conference Center in Diamniadio (outside Dakar). It was NOT postponed beyond July 1, 2026, nor cancelled. Confirmed by the Agence de Presse Sénégalaise (APS), a listed resolution source [1479d6], and by AFP (via France 24), another listed source [84ffe7].

2) Timing requirement met. The election occurred on June 6, 2026, which is on or after May 12, 2026 and before July 1, 2026 (23:59 UTC). Notably, Sonko had been dismissed as Prime Minister by President Faye on May 22, 2026, and the party leadership vote came two weeks later on June 6 [84ffe7].

3) Sonko won the top leadership position. APS reports: "Le président de l'Assemblée nationale Ousmane Sonko a été réélu samedi à la tête du parti Pastef-Les Patriotes à l'issue d'un congrès extraordinaire" and that "Il a été réélu à l'unanimité," by the 583 national and diaspora delegates present [1479d6]. France 24 (with AFP) states Sonko "was re-elected Saturday as head of his Pan-African Pastef party" and "easily won a leadership vote at a congress ... in Diamniadio" [84ffe7]. The top-ranking title remained "President" (président du Pastef), and Sonko holds it.

Sources used (both listed as valid resolution sources):
- APS (aps.sn): https://aps.sn/ousmane-sonko-reelu-a-la-tete-de-pastef-les-patriotes/ [1479d6]
- AFP via France 24 (article ends "(FRANCE 24 with AFP)"): https://www.france24.com/en/africa/20260606-senegal-s-ousted-pm-sonko-re-elected-head-of-his-political-party [84ffe7]

There is no ambiguity: multiple independent authoritative sources (including Reuters-context and RFI corroboration) agree the congress occurred within the window and Sonko was re-elected as party leader by unanimity. Therefore the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-30. `cfb43147-d9d2-5bd9-903f-f449e9a5aecf`

- Present date: `2026-05-14 02:04:07.874532`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-06-25T00:00:00`

**Question**

Will the Banxico Governing Board's June 25, 2026, interest rate decision be unanimous (5-0 vote)?

**Resolution criteria**

This question resolves **Yes** if the official Banxico monetary policy statement for the June 25, 2026, meeting indicates that all five members of the Governing Board voted for the same policy action — i.e., a unanimous 5-0 vote, whether to hold, cut, or hike the target rate. It resolves **No** if at least one member dissented (e.g., a 4-1 or 3-2 split).

**Definitions:**
- "Unanimous" means a 5-0 vote where all five members of the Governing Board select the same policy action. See: https://en.wikipedia.org/wiki/Unanimity
- "Governing Board" refers to Banxico's five-member board responsible for monetary policy decisions. See: https://en.wikipedia.org/wiki/Bank_of_Mexico
- This question refers only to the Governing Board's interest rate decision scheduled for June 25, 2026, announced at 1:00 PM CST (19:00 UTC).

**Resolution source:** The official Banxico monetary policy announcements page: https://www.banxico.org.mx/publications-and-press/announcements-of-monetary-policy-decisions/monetary-policy-announcements.html [Monetary policy statements, rate target, Banco de México](https://www.banxico.org.mx/publications-and-press/announcements-of-monetary-policy-decisions/monetary-policy-announcements.html). The vote split is reported in the press release and/or the minutes published at: https://www.banxico.org.mx/publications-and-press/minutes-of-the-board-of-governors-meetings-regardi/minutes-regarding-monetary-po.html [Monetary policy statements, rate target, Banco de México](https://www.banxico.org.mx/publications-and-press/announcements-of-monetary-policy-decisions/monetary-policy-announcements.html).

If the June 25, 2026, meeting is cancelled or postponed beyond July 1, 2026, the question resolves **No**.

**Pre-cutoff background**

The Bank of Mexico (Banxico) is Mexico's central bank. Its five-member Governing Board (https://en.wikipedia.org/wiki/Bank_of_Mexico) sets the target for the overnight interbank funding rate at scheduled monetary policy meetings, with announcements made at 1:00 PM Central Standard Time (CST, UTC-6) [Monetary policy statements, rate target, Banco de México](https://www.banxico.org.mx/publications-and-press/announcements-of-monetary-policy-decisions/monetary-policy-announcements.html).

On May 7, 2026, the Governing Board voted 3-2 to cut the benchmark interest rate by 25 basis points to 6.50%, while declaring an end to its two-year easing cycle. Board members Jonathan Heath and Irene Espinosa Cantellano dissented, preferring to hold the rate at 6.75% [Mexico's central bank reduces benchmark rate to 6.50% in split vote ...](https://www.investing.com/news/economy-news/mexicos-central-bank-reduces-benchmark-rate-to-650-in-split-vote-93CH-4669490). The central bank cited a contraction in economic activity and revised its inflation forecast for Q2 2026 upward to 4.1%, while targeting convergence to its 3% goal by Q2 2027 [Mexico's central bank reduces benchmark rate to 6.50% in split vote ...](https://www.investing.com/news/economy-news/mexicos-central-bank-reduces-benchmark-rate-to-650-in-split-vote-93CH-4669490).

The 3-2 split reflects meaningful internal disagreement on the board. With the easing cycle now declared over, the June 25, 2026, meeting will test whether the board can reach consensus on holding rates steady, or whether some members push for further cuts (given weak growth) or signal concern about inflation risks. Recent decisions have frequently been split: the March 26, 2026, cut was also not unanimous [Monetary policy statements, rate target, Banco de México](https://www.banxico.org.mx/publications-and-press/announcements-of-monetary-policy-decisions/monetary-policy-announcements.html).

The next scheduled monetary policy announcement is June 25, 2026, at 1:00 PM CST (19:00 UTC).

**Exact later resolution packet**

The question asks whether the Banxico Governing Board's June 25, 2026, interest rate decision was unanimous (5-0). It resolves YES because the June 25, 2026 decision was unanimous.

Key evidence:
- The official Banxico monetary policy statement (press release) dated June 25, 2026, at https://www.banxico.org.mx/publications-and-press/announcements-of-monetary-policy-decisions/%7B1232328B-67C5-6882-B908-B200C19F3E3D%7D.pdf explicitly states that, with the presence of all its members, the Board decided **unanimously** to maintain the target for the overnight interbank interest rate at 6.50% [https://www.banxico.org.mx/publications-and-press/announcements-of-monetary-policy-decisions/%7B1232328B-67C5-6882-B908-B200C19F3E3D%7D.pdf](https://www.banxico.org.mx/publications-and-press/announcements-of-monetary-policy-decisions/%7B1232328B-67C5-6882-B908-B200C19F3E3D%7D.pdf). This is the resolution source specified in the resolution criteria (banxico.org.mx domain).
- Banxico's official announcements page confirms that on 06/25/26 "The target for the overnight interbank funding rate is kept unchanged at 6.50 per cent."
- Independent corroboration: Central Banking reported that "The Bank of Mexico (Banxico) has held its benchmark interest rate at 6.5% in a unanimous decision by its governing board" [Banxico holds rates at 6.5% in end to easing cycle - Central Banking](https://www.centralbanking.com/central-banks/monetary-policy/monetary-policy-decisions/7976240/banxico-holds-rates-at-65-in-end-to-easing-cycle).
- Additional corroborating sources found in search: Banxico's own official statement/tweet ("la Junta de Gobierno decidió por unanimidad conservar la Tasa de Interés Interbancaria a 1 día, a un nivel de 6.50%"), Scotiabank Latam Flash ("decided to keep the reference interest rate at 6.50%, in a unanimous vote"), El Financiero ("Por decisión unánime"), mexicobusiness.news ("Banxico Holds Rates at 6.50% in Unanimous Decision"), and tmgm ("held its main reference rate unchanged at 6.50%... unanimously").

This is specifically the June 25, 2026 meeting (not the May 7, 2026 3-2 cut or the March 26, 2026 split cut referenced in the description). The meeting was held as scheduled (not cancelled or postponed), so the "cancelled/postponed" NO condition does not apply.

Vote count: 5-0 (unanimous), all five Governing Board members voting to hold the rate at 6.50%. Therefore the question resolves YES.

Note: One automated query of the HTML announcements page returned a claim of a 4-1 split with Espinosa dissenting, but this contradicts the official PDF statement and every other source; that HTML page does not actually contain vote-breakdown details, and the claim is an artifact/hallucination. The primary-source PDF and all secondary sources agree the vote was unanimous.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-31. `d75175b0-3f42-5ba9-a8c5-9f437b449e05`

- Present date: `2026-05-01 18:55:57.318394`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the OPEC+ voluntary production group announce an increase in oil output for June 2026 at or after their May 3, 2026 meeting?

**Resolution criteria**

This question resolves as **Yes** if, on or after April 30, 2026, and before 23:59 UTC on June 1, 2026, the OPEC+ voluntary production group (formerly the "V8": Saudi Arabia, Russia, Iraq, UAE, Kuwait, Kazakhstan, Algeria, and Oman—or any successor configuration following the UAE's departure effective May 1, 2026) officially announces a collective production quota increase for June 2026 that exceeds the May 2026 voluntary production levels set on April 5, 2026 (i.e., an upward adjustment beyond the 206,000 bpd already approved for May).

"Production quota increase" refers specifically to the voluntary production adjustments decided by this group (the V8 or its successor), as published in official OPEC press releases, not the broader OPEC+ production allocation table.

The question resolves as **No** if:
- No announcement is made by 23:59 UTC on June 1, 2026;
- The group announces a pause (maintaining May 2026 levels for June); or
- The group announces a production decrease for June 2026.

**Resolution source:** Official OPEC press releases at https://www.opec.org/opec_web/en/press_room/28.htm [Statements - Organization of the Petroleum Exporting Countries](https://www.opec.org/pr-detail/1756597-5-april-2026.html), or credible reporting from Reuters (https://www.reuters.com), Bloomberg, or the Associated Press confirming the outcome of the group's meeting.

**Note on the UAE's status:** The UAE announced its departure from OPEC and OPEC+ effective May 1, 2026. For resolution purposes, "OPEC+" refers to the alliance of OPEC member states and non-OPEC partners coordinating oil production, as listed on the OPEC website (https://www.opec.org). If the UAE is no longer part of the V8 group at the time of the decision, the question applies to the remaining members of the voluntary production group. Any unilateral UAE production increase outside OPEC+ does not count toward resolution.

**Pre-cutoff background**

On April 5, 2026, eight OPEC+ countries—Saudi Arabia, Russia, Iraq, the United Arab Emirates (UAE), Kuwait, Kazakhstan, Algeria, and Oman (known as the "V8")—agreed to increase their collective voluntary production by 206,000 barrels per day (bpd) for May 2026 [https://france24.com/en/live-news/20260405-opec-hikes-oil-production-quotas-issues-warning](https://france24.com/en/live-news/20260405-opec-hikes-oil-production-quotas-issues-warning) [Statements - Organization of the Petroleum Exporting Countries](https://www.opec.org/pr-detail/1756597-5-april-2026.html). This was part of a gradual unwinding of 1.65 million bpd in voluntary cuts, with the group retaining flexibility to "increase, pause, or reverse" adjustments each month [Statements - Organization of the Petroleum Exporting Countries](https://www.opec.org/pr-detail/1756597-5-april-2026.html).

The V8 holds monthly virtual meetings to review market conditions; their next meeting is scheduled for May 3, 2026 [Statements - Organization of the Petroleum Exporting Countries](https://www.opec.org/pr-detail/1756597-5-april-2026.html), at which they would decide on June 2026 production levels.

A major development occurred on April 28, 2026, when the UAE announced it would leave OPEC and OPEC+ effective May 1, 2026, ending nearly 60 years of membership. The UAE was the third-largest OPEC producer behind Saudi Arabia and Iraq. This departure significantly reduces OPEC's control of global supply and introduces substantial uncertainty about future production coordination among the remaining members.

As of April 30, 2026, the May 2026 voluntary production levels set on April 5 represent the current baseline. Whether the remaining V8 members (now potentially seven, minus the UAE) will announce a further increase for June 2026 depends on oil market conditions, the fallout from the UAE's exit, and geopolitical factors including the Iran conflict affecting the Strait of Hormuz.

**Exact later resolution packet**

The question resolves YES.

WHAT HAPPENED: On Sunday, May 3, 2026, seven OPEC+ countries (Saudi Arabia, Russia, Iraq, Kuwait, Kazakhstan, Algeria, and Oman — i.e., the former "V8" minus the UAE, which formally left OPEC and OPEC+ on May 1, 2026) held a virtual meeting and announced a collective voluntary production increase of 188,000 barrels per day (bpd) for June 2026. This was the third consecutive monthly hike. This is confirmed in the official OPEC press release dated 3 May 2026, which states the adjustment "will be implemented in June 2026" [0b8f26], and corroborated by Reuters ("Seven OPEC+ countries will raise oil output targets by 188,000 barrels per day in June, the third consecutive monthly increase, OPEC+ said"), CNBC, and Al Jazeera reporting the same 188,000 bpd June increase.

WINDOW CHECK: The announcement (May 3, 2026) falls on or after April 30, 2026 and before 23:59 UTC June 1, 2026. ✓
GROUP CHECK: It was the voluntary production group's (V8 successor, seven members minus UAE) decision, published as an official OPEC press release — not a change to the broader OPEC+ allocation table. ✓ The UAE was excluded (departed May 1, 2026). ✓

RESOLUTION LOGIC: The question's three enumerated NO conditions are: (1) no announcement by the deadline, (2) a pause maintaining May levels, or (3) a production decrease for June. The group announced an actual INCREASE of 188,000 bpd for June — neither a pause nor a decrease, so none of the NO conditions applies. The criteria's core requirement is "a collective production quota increase for June 2026 that exceeds the May 2026 voluntary production levels": because June output = May level + 188,000 bpd, June production levels exceed May production levels. The 188,000 bpd June increment being slightly smaller than May's 206,000 bpd increment is irrelevant — the criteria compare June production LEVELS to May production levels (cumulative quotas), not the size of one month's increment versus another's, and no NO condition covers "smaller increment than May." Therefore the group announced an increase in June output above May levels = YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-32. `9ec5b3fa-b926-5bcc-b26f-49c3280202be`

- Present date: `2026-05-02 23:53:32.042423`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will SAG-AFTRA and the AMPTP reach a tentative agreement on the 2026 TV/Theatrical/Streaming contract by June 1, 2026?

**Resolution criteria**

This question resolves YES if SAG-AFTRA and the AMPTP formally announce a tentative agreement on their 2026 TV/Theatrical/Streaming Minimum Basic Agreement (MBA) on or after May 1, 2026, and by 11:59 PM Pacific Time (PT) on June 1, 2026.

A "tentative agreement" means an agreement on contract terms that is subject to ratification by SAG-AFTRA's membership but has been endorsed by the union's negotiating committee. This is the standard usage in labor negotiations.

Resolution requires a formal announcement by SAG-AFTRA (e.g., via press release, official statement, or update on their website at https://www.sagaftra.org/news) or a joint statement by SAG-AFTRA and the AMPTP confirming that a tentative agreement has been reached. Credible trade press reporting (e.g., Deadline at https://deadline.com, Variety at https://variety.com, or The Hollywood Reporter at https://www.hollywoodreporter.com) confirming such an announcement may also be used.

If no such announcement is made by the deadline, the question resolves NO.

**Pre-cutoff background**

SAG-AFTRA and the Alliance of Motion Picture and Television Producers (AMPTP) resumed formal negotiations on April 27, 2026, following a pause in March to allow the Writers Guild of America (WGA) to complete its bargaining. The WGA reached a tentative agreement with the AMPTP on approximately April 5, 2026. SAG-AFTRA's current TV/Theatrical/Streaming contract expires June 30, 2026. The negotiations are being conducted under a mutually agreed-upon media blackout. Key issues include AI protections for performers, streaming residuals, and other compensation matters. Earlier bargaining sessions in March were described as "productive" in a joint statement, with talks going "several days beyond what was originally planned." For context, the WGA reached its 2026 deal relatively quickly, but SAG-AFTRA's 2023 negotiations resulted in a 118-day strike before a deal was reached. The complexity of AI issues for performers—including digital replicas, synthetic performances, and training data—makes SAG-AFTRA's negotiations potentially more difficult than the WGA's. As of May 1, 2026, negotiations are ongoing under the media blackout, with no public indication of how close the parties are to a deal.

**Exact later resolution packet**

The question asks whether SAG-AFTRA and the AMPTP would formally announce a tentative agreement on their 2026 TV/Theatrical/Streaming Minimum Basic Agreement (MBA) between May 1, 2026 and 11:59 PM PT on June 1, 2026.

Evidence confirms this occurred:
- Variety published an article on May 2, 2026 titled "SAG-AFTRA Reaches Tentative Deal on Studio Contract," explicitly stating "SAG-AFTRA and the AMPTP have reached a tentative agreement on terms for a successor contract to the 2023 SAG-AFTRA TV/Theatrical Contracts." [SAG-AFTRA Reaches Tentative Deal on Studio Contract - Variety](https://variety.com/2026/film/news/sag-aftra-tentative-deal-studio-contract-1236687517/) (https://variety.com/2026/film/news/sag-aftra-tentative-deal-studio-contract-1236687517/)
- SAG-AFTRA's own official page confirms talks resumed April 27, 2026 and "reached a tentative agreement on May 2." (https://www.sagaftra.org/tentative-agreement-reached-sag-aftra-national-board-review-tvtheatricalstreaming-ta)
- A joint SAG-AFTRA/AMPTP statement announced the tentative agreement (AMPTP media update dated May 2, 2026: https://amptp.org/updates/ ; SAG-AFTRA Facebook joint statement). The deal was then sent to the SAG-AFTRA National Board, which approved it and recommended a "yes" vote for ratification (Deadline: https://deadline.com/2026/05/sag-aftra-board-approves-four-year-amptp-deal-1236898612/ ; SAG-AFTRA page: https://www.sagaftra.org/contracts-industry-resources/contracts/2026-tvtheatrical-contracts).

The agreement was announced on May 2, 2026, which is within the resolution window (on or after May 1, 2026 and before June 1, 2026 deadline). It specifically pertains to the TV/Theatrical/Streaming contract (the successor to the 2023 TV/Theatrical Contracts), and it is a tentative agreement subject to membership ratification but endorsed by the negotiating committee/board. Therefore the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-33. `1ba30f57-cc76-594f-b992-b6e654eac5cb`

- Present date: `2026-05-02 13:47:02.843221`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-05-31 00:00:00`

**Question**

Will the Colorado General Assembly pass legislation repealing or replacing the Colorado AI Act (SB 24-205) before the 2026 session adjourns sine die?

**Resolution criteria**

This question resolves **Yes** if, on or after May 1, 2026, and by 11:59 PM Mountain Time on May 31, 2026, the Colorado General Assembly passes legislation that repeals or replaces the Colorado AI Act (SB 24-205), and such legislation is either (a) signed by the Governor, or (b) sent to the Governor (i.e., passed by both chambers in identical form).

For the purposes of this question:
- **"Repeal or replace"** means the legislation explicitly repeals, substantially amends, or enacts a successor framework to SB 24-205's core provisions regarding AI system governance (e.g., bias audit requirements, risk management obligations, or consumer protection standards for high-risk AI systems). A simple delay of the effective date alone does not count.
- **"Passes"** means the legislation has been approved by both the Colorado House of Representatives and the Colorado Senate in identical form and transmitted to the Governor.

**Primary resolution source:** The official Colorado General Assembly bill tracking website at [https://leg.colorado.gov](https://leg.colorado.gov). The status of any relevant bill(s) can be verified by searching for bills related to SB 24-205 or artificial intelligence on that site.

If no such legislation has passed both chambers by the resolution date, this question resolves **No**.

**Pre-cutoff background**

The Colorado AI Act (SB 24-205), signed in 2024, established requirements for developers and deployers of high-risk AI systems to protect against algorithmic discrimination. It is scheduled to take effect on June 30, 2026. In August 2025, Governor Polis signed SB 25B-004 during a special session to delay the law's effective date from February 2026 to June 2026, after lawmakers failed to agree on substantive amendments during that special session.

On March 17, 2026, Governor Polis and the Colorado AI Policy Working Group released a draft policy framework proposing to repeal and replace SB 24-205 with a new transparency-focused regulatory model centered on "Automated Decision Making Technology in Consequential Decisions" [New draft poised to replace Colorado AI Act](https://www.lawweekcolorado.com/article/new-draft-poised-to-replace-colorado-ai-act/). This framework shifts from the original risk-based bias audit approach to a disclosure-driven model. A formal bill aligned with the working group's framework was expected to be introduced shortly after the draft's release.

On April 28, 2026, a federal judge issued a preliminary order delaying enforcement of the Colorado AI Act, providing additional breathing room. However, the Colorado General Assembly's 2026 regular session is scheduled to adjourn sine die on May 13, 2026, leaving a very narrow window for legislative action.

The outcome is uncertain: the 2025 special session failed to pass substantive changes, consumer advocacy groups favor stronger protections, and industry groups want lighter regulation. Whether the legislature can reach consensus and pass replacement legislation in the remaining days is a genuinely open question.

**Exact later resolution packet**

YES. The relevant legislation is Colorado SB26-189, “Automated Decision-Making Technology,” on the official Colorado General Assembly bill page: https://leg.colorado.gov/bills/sb26-189; the page also lists the Signed Act PDF at https://leg.colorado.gov/bill_files/116489/download and Final Act PDF at https://leg.colorado.gov/bill_files/116432/download [SB26-189 Automated Decision-Making Technology](https://leg.colorado.gov/bills/sb26-189). SB26-189 satisfies the substantive “repeal or replace” requirement because the official bill summary says SB 24-205 created consumer protections in interactions with artificial intelligence systems and that SB26-189 “repeals and reenacts those provisions with new requirements regarding the use of automated decision-making technology in consequential decisions,” which is more than a mere effective-date delay [SB26-189 Automated Decision-Making Technology](https://leg.colorado.gov/bills/sb26-189). The official history/status shows passage by both chambers and identical final form: Senate Third Reading Passed on 05/07/2026, House Third Reading Passed on 05/09/2026, and the Senate Concurred with House Amendments on 05/12/2026, after which the bill was “Sent to the Governor” on 05/12/2026 [SB26-189 Automated Decision-Making Technology](https://leg.colorado.gov/bills/sb26-189). The official status also says the bill “Became Law,” and the history says it was signed by the Governor on 05/14/2026 [SB26-189 Automated Decision-Making Technology](https://leg.colorado.gov/bills/sb26-189). Because the bill was transmitted to the Governor on May 12, 2026 and signed on May 14, 2026—both within the May 1 through May 31, 2026 resolution window—the question resolves YES [SB26-189 Automated Decision-Making Technology](https://leg.colorado.gov/bills/sb26-189).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-34. `11be9241-3523-5920-aeff-adafe8e61320`

- Present date: `2026-05-15 23:22:44.793607`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Tulsi Gabbard leave her position as Director of National Intelligence between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if Tulsi Gabbard ceases to serve as Director of National Intelligence at any point on or after May 12, 2026, and no later than July 1, 2026, 11:59 PM UTC.

This question resolves **No** if Gabbard continues to serve as DNI through July 1, 2026, 11:59 PM UTC.

**Definitions and clarifications:**
- The "Director of National Intelligence" (DNI) is the head of the United States Intelligence Community, as described at https://en.wikipedia.org/wiki/Director_of_National_Intelligence and https://www.dni.gov/.
- "Leaving her position" means Gabbard is no longer serving as DNI, whether by resignation, termination, or any other means. A nomination or appointment to a different role counts as leaving only if she has actually vacated the DNI position (i.e., she is no longer serving as DNI). Simply being nominated for another role while still serving as DNI does not count.
- The departure is considered effective upon the earlier of: (a) an official announcement (by Gabbard, the White House, or the ODNI) that she has resigned or been removed, or (b) a successor being sworn in or an acting DNI being designated to replace her. An announcement of a future departure date does not count until that date arrives or she actually stops serving.
- Departures that occurred before May 12, 2026 do not count toward resolution.

**Resolution source:** Official announcements from the DNI newsroom (https://www.dni.gov/index.php/newsroom/press-releases/press-releases-2026), the White House (https://www.whitehouse.gov/briefing-room/), or credible reporting from major news agencies such as AP (https://apnews.com), Reuters (https://reuters.com), or The New York Times (https://nytimes.com).

**Pre-cutoff background**

Tulsi Gabbard serves as the 8th Director of National Intelligence (DNI), a role defined as the head of the United States Intelligence Community (see: https://en.wikipedia.org/wiki/Director_of_National_Intelligence). She was confirmed and took office in early 2025 under President Trump's second administration.

As of mid-May 2026, multiple reports indicate growing uncertainty about Gabbard's tenure. In early April 2026, The Guardian reported that Trump privately polled cabinet members about whether he should replace Gabbard as DNI, following her testimony at a worldwide threats hearing where she declined to condemn former deputy Joe Kent [Trump polled advisers about replacing Tulsi Gabbard as intelligence ...](https://www.theguardian.com/us-news/2026/apr/02/trump-tulsi-gabbard-intelligence-chief). Kent had resigned from his position as director of the National Counterterrorism Center after publicly arguing that Iran did not pose an imminent threat to the United States, contradicting the administration's rationale for military action against Iran [Trump polled advisers about replacing Tulsi Gabbard as intelligence ...](https://www.theguardian.com/us-news/2026/apr/02/trump-tulsi-gabbard-intelligence-chief). Trump was reportedly frustrated that Gabbard appeared reluctant to defend the administration's position on Iran during the hearing [Trump polled advisers about replacing Tulsi Gabbard as intelligence ...](https://www.theguardian.com/us-news/2026/apr/02/trump-tulsi-gabbard-intelligence-chief).

Separately, sources reported that the White House asked Gabbard to step down before the 2026 midterm elections. However, the White House publicly denied these reports, calling them "fake news," and the administration confirmed Gabbard's job following Kent's departure. The administration has generally preferred reassigning officials rather than firing them outright in the second term [Trump polled advisers about replacing Tulsi Gabbard as intelligence ...](https://www.theguardian.com/us-news/2026/apr/02/trump-tulsi-gabbard-intelligence-chief). There is no clear standout replacement candidate [Trump polled advisers about replacing Tulsi Gabbard as intelligence ...](https://www.theguardian.com/us-news/2026/apr/02/trump-tulsi-gabbard-intelligence-chief), adding further uncertainty to the situation. Prediction markets (Polymarket, Kalshi) have active markets on this question, with implied probabilities suggesting genuine uncertainty.

**Exact later resolution packet**

The question resolves **YES**. Tulsi Gabbard ceased to serve as Director of National Intelligence within the window of May 12, 2026 to July 1, 2026, 11:59 PM UTC.

Evidence and reasoning:

1. On Friday, May 22, 2026, Gabbard announced her resignation as DNI, citing her husband's bone cancer diagnosis. Her resignation letter stated it was "effective June 30, 2026," and she said she would remain in her post as the nation's intelligence chief until June 30. Source: The New York Times, "Tulsi Gabbard Resigns as Director of National Intelligence" (https://www.nytimes.com/2026/05/22/us/politics/tulsi-gabbard-resigns.html) [baf5f9]. Corroborated by Reuters, "Gabbard resigns as Trump's top US intelligence official" (https://www.reuters.com/world/us/gabbard-resigns-trumps-national-intelligence-director-fox-news-digital-reports-2026-05-22/).

2. Per the resolution criteria, an announcement of a *future* departure date does not count until that date arrives. June 30, 2026 is the effective date, and June 30, 2026 falls BEFORE the July 1, 2026, 11:59 PM UTC cutoff. Therefore her departure occurred within the resolution window.

3. Additionally, criterion (b) — "a successor being sworn in or an acting DNI being designated to replace her" — was also satisfied within the window. Following her May 22 resignation, her deputy Aaron Lukas was initially named acting director, and on June 2, 2026, President Trump named Bill Pulte as acting Director of National Intelligence to replace Gabbard. Source: NBC News (https://www.nbcnews.com/politics/national-security/trump-william-pulte-acting-director-national-intelligence-tulsi-gabbar-rcna348036) [541416]; USA Today, June 2, 2026 (https://www.usatoday.com/story/news/politics/2026/06/02/trump-bill-pulte-tulsi-gabbard-director-national-intelligence/90367674007/) [7b44b5].

4. Confirmation that she actually vacated the position: the official ODNI leadership page (https://www.dni.gov/index.php/who-we-are/leadership/director-of-national-intelligence) now lists William J. Pulte as the Director of National Intelligence, with Gabbard no longer listed [0af81c].

Both the effective resignation date (June 30, 2026) and the acting-DNI designation of Bill Pulte (June 2, 2026) fall before the July 1, 2026, 11:59 PM UTC cutoff, and both are on/after May 12, 2026. The question therefore resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-35. `4a21678b-b6de-5b2a-8dd1-5e972372447d`

- Present date: `2026-05-14 09:19:26.836650`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the U.S. House pass the $72B immigration enforcement reconciliation bill by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if the U.S. House of Representatives passes the final text of the $72B immigration enforcement reconciliation bill—whether as an initial House-originated bill, a conference report, or a Senate-amended version—on or after May 12, 2026, and on or before July 1, 2026 (by 11:59 PM ET).

This question resolves **No** if no such bill is passed by the House by that deadline.

Key definitions:
- **"Pass"**: The House of Representatives approves the legislation through a recorded roll call vote, as documented in the [official House roll call vote records](https://clerk.house.gov/Votes). Any form of House passage counts, including passage of a House-originated version, a [conference report](https://www.congress.gov/help/legislative-glossary#glossary_conferencereport) (the compromise text agreed upon by a House-Senate conference committee), or the [Senate-amended version](https://www.congress.gov/help/legislative-glossary#glossary_amendment) of the bill.
- **"$72B immigration enforcement reconciliation bill"**: The reconciliation legislation arising from the budget resolution adopted by the Senate on April 23, 2026 (S.Con.Res.33) and by the House on April 29, 2026, which directs committees to produce legislation funding immigration enforcement (ICE and Border Patrol). The bill is trackable via [Congress.gov](https://www.congress.gov/bill/119th-congress).

**Resolution source**: The [House Clerk's roll call vote page](https://clerk.house.gov/Votes) or the bill's page on [Congress.gov](https://www.congress.gov) will serve as the authoritative resolution source.

**Pre-cutoff background**

As of May 13, 2026, congressional Republicans are pursuing a $72 billion immigration enforcement reconciliation bill to fund Immigration and Customs Enforcement (ICE) and Border Patrol through 2029. The legislative process so far:

- On April 23, 2026, the Senate passed a budget resolution (50-48) laying the groundwork for the reconciliation package [Congress returns with funding for immigration enforcement ... - NPR](https://www.npr.org/2026/05/11/nx-s1-5816261/congress-likely-to-pass-republicans-plan-to-fund-ice).
- On April 29, 2026, the House adopted the Senate-approved budget resolution in a party-line vote of 215-211-1, with Rep. Kevin Kiley (R-CA) voting "present" [House passes budget blueprint for reconciliation 2.0 to fund ICE ...](https://thehill.com/homenews/5856068-budget-blueprint-reconciliation-dhs-farm-bill/). This unlocked the reconciliation process, directing committees to draft the actual spending legislation.
- On May 4, 2026, Senate Judiciary and Homeland Security committees released the $72 billion legislative text, which includes controversial provisions such as $1 billion for Secret Service security upgrades linked to a Trump ballroom project [Congress returns with funding for immigration enforcement ... - NPR](https://www.npr.org/2026/05/11/nx-s1-5816261/congress-likely-to-pass-republicans-plan-to-fund-ice).
- As of May 11, 2026, Congress returned from recess and is "poised to move ahead" with the plan, though no House vote on the final bill has been scheduled [Congress returns with funding for immigration enforcement ... - NPR](https://www.npr.org/2026/05/11/nx-s1-5816261/congress-likely-to-pass-republicans-plan-to-fund-ice).

The House Republican majority is razor-thin at 215-211, giving leadership only a two-vote margin for error assuming full attendance and party unity [House passes budget blueprint for reconciliation 2.0 to fund ICE ...](https://thehill.com/homenews/5856068-budget-blueprint-reconciliation-dhs-farm-bill/). Past reconciliation efforts have faced opposition from within the GOP, including from Reps. Thomas Massie (R-KY) and Brian Fitzpatrick (R-PA) [House passes budget blueprint for reconciliation 2.0 to fund ICE ...](https://thehill.com/homenews/5856068-budget-blueprint-reconciliation-dhs-farm-bill/). The controversial ballroom security funding and broader intra-party tensions over the scope of the bill create genuine uncertainty about House passage. President Trump has expressed a desire for the bill to be on his desk by June 1, 2026 [House passes budget blueprint for reconciliation 2.0 to fund ICE ...](https://thehill.com/homenews/5856068-budget-blueprint-reconciliation-dhs-farm-bill/).

The bill must still go through committee markup, floor votes in both chambers, and potentially a conference process or Senate amendment before final House passage.

**Exact later resolution packet**

The question resolves YES. The U.S. House of Representatives passed the $72B immigration enforcement reconciliation bill (the "Secure America Act," S.2) on Tuesday, June 9, 2026, well within the resolution window of May 12, 2026 – July 1, 2026 (11:59 PM ET).

Checklist verification:

1) TIMING (strictly between May 12 and July 1, 2026): The House passed the bill on June 9, 2026 — confirmed by The Hill [23d489], Reuters [6da75c], and Roll Call [620f7b]. The House Clerk records the vote as occurring "Jun 09, 2026, 05:23 PM." This is inside the required window.

2) CORRECT BILL / RECONCILIATION FROM S.Con.Res.33: The legislation is S.2, the Secure America Act, the reconciliation bill arising from the FY2026 budget resolution (S.Con.Res.33 — adopted by the Senate April 23, 2026 and the House April 29, 2026). The enacted text is titled "An Act To provide for reconciliation pursuant to title II of S.Con.Res.33," confirming it is the reconciliation package unlocked by that budget resolution.

3) SPECIFIC RESOLUTION-SOURCE URL: House Clerk official roll call vote — Roll Call 214 (119th Congress, 2nd Session): https://clerk.house.gov/Votes/2026214 . Congress.gov bill page: https://www.congress.gov/bill/119th-congress/senate-bill/2 .

4) RECORDED ROLL CALL VOTE: Yes. It was a recorded vote (Vote Type: Recorded Vote), "On Passage," Status: Passed, tally 214-212, roughly along party lines [23d489][6da75c][620f7b].

5) WHICH VERSION: The House passed the SENATE-PASSED version of the bill. The Republican-led Senate had passed S.2 the prior week; the House then cleared that same Senate bill on June 9, 2026, sending it directly to the President's desk (no conference report; not a House-originated version) [6da75c][620f7b]. Roll Call notes "the House cleared the reconciliation bill that the Senate passed last week" [620f7b], and Reuters notes "The Republican-led Senate passed the same bill late last week" and the House vote "sends the partisan legislation to the White House for Trump's signature" [6da75c].

6) SCOPE MATCH (ICE/Border Patrol funding): Yes. The bill funds Immigration and Customs Enforcement (ICE) and Border Patrol/CBP through 2029 [23d489][6da75c][620f7b]. Note the headline figure fell from the ~$72B initial Senate text to a "nearly $70 billion" final package, but it is unambiguously the same reconciliation legislation defined in the question.

Because all resolution criteria are satisfied — House passage of the ICE/Border Patrol reconciliation bill via a recorded roll call vote within the specified window — the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-36. `6fc68401-489f-553c-b103-de9df602be49`

- Present date: `2026-05-15 10:20:13.025789`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Direct Contact Between Abdullah Öcalan and DEM Party Representatives Be Restored by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 and by July 1, 2026 (23:59 UTC), there is a confirmed instance of direct contact between Abdullah Öcalan and at least one DEM Party representative. It resolves **No** otherwise.

**"Direct contact"** is defined as any of the following:
- An in-person meeting (i.e., a face-to-face visit at İmralı prison or any other location), as described by the concept of a "prison visit" (see https://en.wikipedia.org/wiki/Prison_visit);
- A telephone or video call between Öcalan and a DEM Party representative;
- A written correspondence (letter) confirmed to have been exchanged directly between Öcalan and a DEM Party representative, where both the sending and receipt are acknowledged.

**"DEM Party representative"** is defined as any individual who holds an official position within the Peoples' Equality and Democracy Party (DEM Party), including but not limited to: co-chairs, members of the party's central executive board, members of parliament affiliated with the DEM Party, or individuals formally designated by the DEM Party leadership as part of a delegation to meet Öcalan.

**Verification sources:** Resolution will be based on confirmation from at least one of the following:
- Official DEM Party statements (https://www.demparti.org.tr/en/)
- Turkish Ministry of Justice announcements
- Credible international news agencies: Reuters (https://www.reuters.com/), Associated Press (https://apnews.com/), or AFP
- Reputable Turkish or Kurdish-focused outlets: Bianet (https://bianet.org/), Anadolu Agency (https://www.aa.com.tr/en), or Kurdistan24 (https://www.kurdistan24.net/en)

If no credible source confirms that such contact occurred on or after May 12, 2026 and by July 1, 2026, the question resolves **No**.

**Pre-cutoff background**

Abdullah Öcalan is the imprisoned founder of the Kurdistan Workers' Party (PKK), held at İmralı island prison in Turkey since 1999 (see https://en.wikipedia.org/wiki/Abdullah_%C3%96calan). The Peoples' Equality and Democracy Party (DEM Party, formerly HDP) is Turkey's main pro-Kurdish political party (see https://en.wikipedia.org/wiki/Peoples%27_Equality_and_Democracy_Party).

In February 2025, Öcalan issued a historic call for the PKK to lay down arms and dissolve itself, launching a peace process with the Turkish state. DEM Party delegations visited Öcalan at İmralı prison multiple times in late 2024 and early 2025 to facilitate this process. However, as of March 27, 2026, all direct contact between Öcalan and DEM Party representatives was severed [https://www.newarab.com/news/turkey-pkk-peace-process-stalls-amid-disarmament-dispute](https://www.newarab.com/news/turkey-pkk-peace-process-stalls-amid-disarmament-dispute). DEM Party foreign relations spokesperson Ebru Gunay described this as a "serious problem" given the sensitivity of the ongoing peace process [https://www.newarab.com/news/turkey-pkk-peace-process-stalls-amid-disarmament-dispute](https://www.newarab.com/news/turkey-pkk-peace-process-stalls-amid-disarmament-dispute). Senior PKK figures have cited this isolation as a major obstacle to continuing the peace agreement [https://www.newarab.com/news/turkey-pkk-peace-process-stalls-amid-disarmament-dispute](https://www.newarab.com/news/turkey-pkk-peace-process-stalls-amid-disarmament-dispute).

As of May 13, 2026, there are no confirmed reports that contact has been restored. The Turkish government controls access to İmralı prison, and the resumption of visits depends on government authorization. There are competing pressures: the government may use access as leverage in disarmament negotiations, while the DEM Party and PKK insist that Öcalan's participation is essential for any progress.

**Exact later resolution packet**

The question resolves YES. It asks whether direct contact between Abdullah Öcalan and at least one DEM Party representative occurred on or after May 12, 2026 and by July 1, 2026 (23:59 UTC). Multiple credible sources — including at least one explicitly listed verification source (Kurdistan24) — confirm an in-person meeting between a DEM Party delegation and Öcalan at İmralı prison within this window.

Key evidence:

1. SyriacPress (published May 26, 2026) reports that a DEM Party delegation visited Öcalan on İmralı Island "on Sunday," which corresponds to May 24, 2026. It states: "The delegation of the Peoples' Equality and Democracy Party (DEM Party), which visited Abdullah Öcalan... on İmralı Island on Sunday, issued a statement on the visit." The article links to the DEM Party's own official statement (https://www.demparti.org.tr/tr/basina-ve-kamuoyuna/22725/) [f98868]. May 24, 2026 falls squarely within the May 12 – July 1, 2026 window.

2. The New Region (published June 9, 2026) independently confirms: "In late May, DEM Party's Imrali delegation visited imprisoned Kurdistan Workers' Party (PKK) leader Abdullah Ocalan on the high-security island, marking the first visit to the jailed leader in months." [affce6] This confirms both the timing (late May 2026) and that this restored contact after the previous severance described in the question.

3. Kurdistan24 (published June 7, 2026), an explicitly listed verification source, confirms the delegation's contact: "Medhat Sancar, a member of the delegation from the Peoples' Equality and Democracy Party (Dem Party) that visits Imrali Prison, revealed details of recent discussions with Ocalan." [05d3a3]

The contact was (a) within the specified window (May 24, 2026), (b) an in-person prison visit — the strongest form of "direct contact" defined in the criteria, (c) conducted by the DEM Party's official İmralı delegation (formally designated party representatives, including party co-chair Tülay Hatimoğulları referenced in the reporting and delegation member Medhat Sancar), and (d) confirmed by a DEM Party official statement and by a listed verification source (Kurdistan24). All resolution criteria are satisfied.

This is a straightforward (non-conditional) binary question, so it resolves YES (1).

Source URLs:
- https://syriacpress.com/blog/2026/05/26/abdullah-ocalan-after-dem-party-delegation-visit-a-legal-regulation-will-lead-us-into-a-genuine-process-of-positive-democratic-reconstruction/
- https://thenewregion.com/posts/5588
- https://www.kurdistan24.net/en/story/918543/dem-party-reveals-ocalans-new-peace-roadmap-and-talks-with-ruling-akp
- DEM Party statement: https://www.demparti.org.tr/tr/basina-ve-kamuoyuna/22725/

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-37. `87d5e6a2-d228-55a7-8516-58dcf6412493`

- Present date: `2026-05-16 12:08:48.213022`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the United States and Iran sign a formal agreement to reopen the Strait of Hormuz to commercial shipping by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 12, 2026 (00:00 UTC) and before July 1, 2026 (23:59 UTC), the United States and Iran sign a formal agreement that explicitly includes the reopening of the [Strait of Hormuz](https://en.wikipedia.org/wiki/Strait_of_Hormuz) to commercial shipping.

**Key definitions:**

- **"Formal agreement"** means a signed treaty, [memorandum of understanding](https://en.wikipedia.org/wiki/Memorandum_of_understanding), or joint official statement issued by both the United States government (via the [White House](https://www.whitehouse.gov/) or [U.S. Department of State](https://www.state.gov/)) and the Iranian government (via the [Ministry of Foreign Affairs](https://en.mfa.ir/)) that explicitly commits both parties to reopening the Strait to commercial shipping. Unilateral statements, informal understandings, or de facto reopening without a signed document do not count.

- **"Commercial shipping"** refers to the transit of [merchant vessels](https://en.wikipedia.org/wiki/Merchant_vessel) through the Strait of Hormuz for the purpose of international trade, including oil tankers, cargo ships, and other non-military vessels.

If no such agreement is signed and officially announced by 23:59 UTC on July 1, 2026, the question resolves **No**.

**Resolution sources:** Official announcements from the [White House](https://www.whitehouse.gov/) or [U.S. Department of State](https://www.state.gov/), or consistent reporting from at least two major international news agencies such as [Reuters](https://www.reuters.com/), [Associated Press](https://apnews.com/), or [AFP](https://www.afp.com/).

**Pre-cutoff background**

As of May 12, 2026, the Strait of Hormuz has been effectively closed to commercial shipping since late February 2026 due to the ongoing 2026 Iran war. The crisis is characterized by a "dual blockade": Iran has restricted passage through the strait while the United States has simultaneously blockaded Iranian ports. Over 600 tankers are stranded inside the Persian Gulf, with approximately 240 additional vessels waiting outside [https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis).

The primary obstacle to a deal remains the incompatible demands of the two parties: the United States insists on unconditional reopening of the Strait, while Iran demands international recognition of its sovereignty over the waterway [https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire). Previous diplomatic efforts, including the Islamabad Talks in April 2026, collapsed without agreement [https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis).

On May 6, 2026, President Trump paused "Operation Project Freedom"—a US Navy mission to escort merchant ships—citing "great progress" toward a possible agreement [https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis). However, on May 12, 2026, Trump explicitly rejected Iran's latest proposal, calling it "garbage" and stating the ceasefire is "on life support" [https://www.democracynow.org/2026/5/12/headlines](https://www.democracynow.org/2026/5/12/headlines). Saudi Aramco has warned of "catastrophic consequences" if disruptions continue, estimating losses of 100 million barrels per week and warning that global gasoline and jet fuel supplies could reach "critically low levels" by summer [https://www.democracynow.org/2026/5/12/headlines](https://www.democracynow.org/2026/5/12/headlines).

For further context, see the [2026 Strait of Hormuz crisis Wikipedia article](https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis) and the [2026 Iran war ceasefire Wikipedia article](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire).

**Exact later resolution packet**

The question resolves YES.

The resolution criteria require that, between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), the US and Iran SIGN a formal agreement (treaty, MOU, or joint official statement) issued by both governments that explicitly includes reopening the Strait of Hormuz to commercial shipping. It does NOT require the reopening to durably succeed or hold — indeed, the definitions clarify that "de facto reopening without a signed document do not count," confirming the operative trigger is the signed document itself.

Evidence establishing every required element:

1) A formal agreement (memorandum of understanding) was signed within the window. Encyclopaedia Britannica states the MOU was finalized/announced June 14 and "signed on June 17 by Trump and Iranian Pres. Masoud Pezeshkian," bringing the conflict to an end within 60 days [2026 Iran war | Deal, Explained, United States, Israel, Strait of ...](https://www.britannica.com/event/2026-Iran-war). NBC News reports the MOU was digitally signed on Sunday June 14, 2026 by Vice President JD Vance and Iranian Parliament Speaker Mohammad Bagher Ghalibaf (witnessed by Trump), and signed in person by President Trump at the Palace of Versailles on Wednesday June 17, 2026 [Trump and Iran's president sign initial deal to end war, open Strait of ...](https://www.nbcnews.com/world/iran/strait-hormuz-reopen-us-lift-iran-sanctions-14-point-deal-seeking-end-rcna350513). Both dates fall inside the May 12–July 1, 2026 window.

2) It was issued/signed by both the US government and the Iranian government. Signatories were the US President (Trump/White House) and Iran's President (Pezeshkian), with Iran's foreign ministry having described the MOU as the first phase of the deal [Trump and Iran's president sign initial deal to end war, open Strait of ...](https://www.nbcnews.com/world/iran/strait-hormuz-reopen-us-lift-iran-sanctions-14-point-deal-seeking-end-rcna350513) [2026 Iran war | Deal, Explained, United States, Israel, Strait of ...](https://www.britannica.com/event/2026-Iran-war).

3) The text explicitly includes reopening the Strait of Hormuz to commercial shipping. NBC: "The MOU stipulates that the Strait of Hormuz will reopen, with Iran agreeing to allow 'safe passage of commercial vessels with no charge for 60 days only'" [Trump and Iran's president sign initial deal to end war, open Strait of ...](https://www.nbcnews.com/world/iran/strait-hormuz-reopen-us-lift-iran-sanctions-14-point-deal-seeking-end-rcna350513). Britannica: the memorandum "included ... an end to Iranian restrictions on the Strait of Hormuz" [2026 Iran war | Deal, Explained, United States, Israel, Strait of ...](https://www.britannica.com/event/2026-Iran-war). CNN: the memorandum "stipulates that Iran will make 'arrangements using its best efforts' to ensure the safe passage of commercial vessels in the Strait of Hormuz, and that traffic in the strait would return to the same volume as before the war began" [Iran and US exchange strikes as Hormuz tensions stress agreement](https://www.cnn.com/2026/06/27/middleeast/iran-strait-of-hormuz-tensions-intl). Fortune: "the U.S. and Iran signed a memorandum of understanding to reopen the Strait of Hormuz" [Shipping companies will decide when the Strait of Hormuz is open ...](https://fortune.com/2026/06/20/shipping-companies-insurance-strait-of-hormuz-traffic-us-iran-deal/).

4) Resolution-source threshold met. The signing is reported consistently by multiple major outlets — NBC News [Trump and Iran's president sign initial deal to end war, open Strait of ...](https://www.nbcnews.com/world/iran/strait-hormuz-reopen-us-lift-iran-sanctions-14-point-deal-seeking-end-rcna350513), CNN [Iran and US exchange strikes as Hormuz tensions stress agreement](https://www.cnn.com/2026/06/27/middleeast/iran-strait-of-hormuz-tensions-intl), Fortune [Shipping companies will decide when the Strait of Hormuz is open ...](https://fortune.com/2026/06/20/shipping-companies-insurance-strait-of-hormuz-traffic-us-iran-deal/), and Encyclopaedia Britannica [2026 Iran war | Deal, Explained, United States, Israel, Strait of ...](https://www.britannica.com/event/2026-Iran-war) — plus (per search results) Reuters, The New York Times, NPR, AP, and Al Jazeera, well exceeding the "at least two major international news agencies" bar.

Note on a potential loophole: CNN [Iran and US exchange strikes as Hormuz tensions stress agreement](https://www.cnn.com/2026/06/27/middleeast/iran-strait-of-hormuz-tensions-intl) reports the MOU terms lacked detailed conditions, that the sides had "differing understandings" (e.g., on tolls/fees), and that the Strait was subsequently reclosed with renewed strikes in late June. An auto-generated reading of that page suggested "NO." However, this conflates the signing of the agreement (the actual resolution trigger) with whether the reopening held. The criteria only require a signed agreement explicitly committing both parties to reopening — which unambiguously occurred on June 14/17, 2026. Subsequent breakdown of implementation does not undo the signing. Therefore the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-38. `e7bc952c-31bb-5b53-ba45-9279b608efb1`

- Present date: `2026-05-29 05:34:43.588974`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Phoebe Plummer or Jane Touil be found guilty of criminal damage in their Heathrow Airport retrial at Isleworth Crown Court by July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if a verdict of "guilty" is delivered on or after May 12, 2026, and on or before July 1, 2026 (23:59 UTC), against **at least one** of the two defendants — Phoebe Plummer or Jane Touil — on at least one charge related to the July 30, 2024, Heathrow Airport incident.

"Found guilty" means a formal guilty verdict returned by a jury (or, in the event of a judge-directed verdict, by a judge) in the Crown Court of England and Wales, as defined under UK criminal procedure. This includes both unanimous and majority verdicts.

"Criminal damage" refers to the offence under Section 1 of the Criminal Damage Act 1971 (https://www.legislation.gov.uk/ukpga/1971/48/section/1), which criminalises destroying or damaging property belonging to another without lawful excuse.

The question resolves **No** if, by July 1, 2026 (23:59 UTC):
- Both defendants are acquitted of all charges; or
- The case is dismissed or the prosecution offers no evidence; or
- The trial results in another hung jury without a subsequent retrial concluding before the deadline; or
- The trial is postponed or otherwise does not reach a verdict.

**Resolution source:** Credible news reporting from outlets such as BBC News (https://www.bbc.co.uk/news), The Guardian (https://www.theguardian.com/uk-news), or Reuters (https://www.reuters.com), or official court records confirming the verdict.

**Pre-cutoff background**

On July 30, 2024, Just Stop Oil supporters Phoebe Plummer and Jane Touil used fire extinguishers to spray water-based orange paint onto departure boards at Heathrow Airport as part of the "Oil Kills" international uprising. The Crown alleged the action caused £8,000 in damages [Heathrow paint spraying trial ends with a hung jury - Just Stop Oil](https://juststopoil.org/2025/01/16/heathrow-paint-spraying-trial-ends-with-a-hung-jury/). Both were charged with criminal damage over £5,000, an offence under the Criminal Damage Act 1971 (https://www.legislation.gov.uk/ukpga/1971/48).

Their first trial at Isleworth Crown Court, presided over by Her Honour Judge Duncan, lasted nine days and ended in a hung jury — the jury failed to reach even a majority verdict [Heathrow paint spraying trial ends with a hung jury - Just Stop Oil](https://juststopoil.org/2025/01/16/heathrow-paint-spraying-trial-ends-with-a-hung-jury/). Judge Duncan scheduled a retrial for May 2026 [Heathrow paint spraying trial ends with a hung jury - Just Stop Oil](https://juststopoil.org/2025/01/16/heathrow-paint-spraying-trial-ends-with-a-hung-jury/).

The retrial is listed on the Just Stop Oil trial tracker as running from May 11 to May 22, 2026, at Isleworth Crown Court in London [Upcoming Trials, February 2026 - Just Stop Oil](https://juststopoil.org/upcoming-trials-feb-2026/). As of May 13, 2026, the retrial is expected to be underway.

Context for forecasters: Recent UK criminal trials involving Just Stop Oil activists have produced mixed results. Some trials have resulted in convictions, while others (including this case's first trial) have ended in hung juries. Defendants in climate protest cases have been increasingly restricted from presenting climate-related defences, which may affect jury deliberations. The previous hung jury suggests genuine uncertainty about the outcome.

**Exact later resolution packet**

The question resolves YES.

Antecedent/consequent: This is a straightforward (non-conditional) question. It resolves YES if a "guilty" verdict was delivered between May 12, 2026 and July 1, 2026 (23:59 UTC) against at least one of Phoebe Plummer or Jane Touil on at least one charge related to the July 30, 2024 Heathrow Airport incident.

Key findings:
- Both Phoebe Plummer AND Jane Touil were found GUILTY of criminal damage (over £5,000) at their retrial at Isleworth Crown Court following the earlier hung jury. Just Stop Oil's own press release, dated May 14, 2026, states the pair "have been found guilty in a retrial" and that "The jury took 4.5 hours to reach a majority verdict of 10-2," with sentencing set for June 29 [Two Just Stop Oil supporters found guilty for Heathrow paint ...](https://juststopoil.org/2026/05/14/two-just-stop-oil-supporters-found-guilty-for-heathrow-paint-spraying-following-retrial/). URL: https://juststopoil.org/2026/05/14/two-just-stop-oil-supporters-found-guilty-for-heathrow-paint-spraying-following-retrial/
- Radio Jackie (a credible local news outlet) independently reported that "Phoebe Plummer and Jane Touil have been convicted of criminal damage worth over £5,000," relating to the July 2024 Heathrow departure-board paint action, published May 14, 2026 [Two Just Stop Oil supporters who sprayed Heathrow departure ...](https://radiojackie.com/two-just-stop-oil-supporters-who-sprayed-heathrow-departure-boards-with-orange-paint-have-been-found-guilty-at-a-retrial/). URL: https://radiojackie.com/two-just-stop-oil-supporters-who-sprayed-heathrow-departure-boards-with-orange-paint-have-been-found-guilty-at-a-retrial/
- The Canary confirmed at sentencing that "Phoebe Plummer and Jane Touil were sentenced by Judge Duncan at Isleworth Crown Court on 29 June, after being found guilty of criminal damage in a second trial in May for their Heathrow action on 30 July 2024" (published June 30, 2026) [No prison for Heathrow paint sprayers - Canary](https://www.thecanary.co/uk/news/2026/06/30/heathrow-activists-spared/). URL: https://www.thecanary.co/uk/news/2026/06/30/heathrow-activists-spared/

Verdict type: This was a jury-returned guilty verdict (a 10-2 majority verdict), not a judge-directed verdict, as explicitly stated by the Just Stop Oil press release [Two Just Stop Oil supporters found guilty for Heathrow paint ...](https://juststopoil.org/2026/05/14/two-just-stop-oil-supporters-found-guilty-for-heathrow-paint-spraying-following-retrial/). Majority verdicts are expressly included by the resolution criteria.

Timing: The verdict was delivered on May 14, 2026, which is on or after May 12, 2026 and on or before July 1, 2026 (23:59 UTC), satisfying the resolution window. The charge (criminal damage over £5,000 under the Criminal Damage Act 1971) relates directly to the July 30, 2024 Heathrow Airport incident.

Because at least one (in fact both) of the two defendants received a formal guilty verdict on a charge related to the July 30, 2024 Heathrow incident within the resolution window, the question resolves YES. None of the NO conditions (both acquitted / case dismissed / no evidence offered / another hung jury / postponement) applies.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-39. `444b8215-8b25-5b43-9625-2de4476e49b7`

- Present date: `2026-05-14 08:53:27.326191`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the BMA open a new ballot of resident doctors in England regarding the pay dispute between May 12 and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 12, 2026 00:00 UTC and July 1, 2026 23:59 UTC, the BMA officially opens or announces the opening of a new ballot of resident doctors in England related to the pay dispute. This includes:

- A ballot on whether to accept or reject a government pay offer;
- A ballot to renew or extend the mandate for industrial action;
- Any other formal membership vote of resident doctors in England directly related to the pay dispute.

"Resident doctors" refers to doctors formerly known as "junior doctors" in England, as defined by the BMA (https://www.bma.org.uk/our-campaigns/resident-doctor-campaigns/pay-in-england/pay-restoration-for-resident-doctors-in-england).

"Opening a ballot" means the date on which voting formally opens for BMA members, OR the date the BMA officially announces that a ballot will be held (whichever comes first), as reported on the BMA's official website (https://www.bma.org.uk/news-and-opinion) or via official BMA communications.

The question resolves **No** if no such ballot is opened or announced by July 1, 2026 23:59 UTC.

**Resolution source:** Official BMA announcements at https://www.bma.org.uk/news-and-opinion or the BMA's resident doctor campaign page at https://www.bma.org.uk/our-campaigns/resident-doctor-campaigns/pay-in-england/pay-restoration-for-resident-doctors-in-england.

**Pre-cutoff background**

The British Medical Association (BMA) has been engaged in a long-running pay dispute on behalf of resident doctors (formerly known as "junior doctors", see https://www.bma.org.uk/our-campaigns/resident-doctor-campaigns/pay-in-england/pay-restoration-for-resident-doctors-in-england) in England. Resident doctors secured a re-ballot in January 2026 returning a decisive "yes" vote for industrial action, uniting all resident doctors including FY1s under one mandate [Pay restoration for resident doctors in England - BMA](https://www.bma.org.uk/our-campaigns/resident-doctor-campaigns/pay-in-england/pay-restoration-for-resident-doctors-in-england). This current mandate for industrial action expires on August 1, 2026 [Pay restoration for resident doctors in England - BMA](https://www.bma.org.uk/our-campaigns/resident-doctor-campaigns/pay-in-england/pay-restoration-for-resident-doctors-in-england).

As of May 2026, the dispute remains unresolved. Resident doctors conducted strike action in April 2026, and negotiations with Health Secretary Wes Streeting have not yielded a deal. The BMA has also announced it will ballot senior doctors (consultants and SAS doctors) for industrial action, with three hospital doctor groups threatening coordinated strikes.

A new ballot of resident doctors could occur for two reasons: (1) to vote on accepting or rejecting a government pay offer if a deal is reached, or (2) to renew the industrial action mandate ahead of its August 1 expiry. Given that the mandate does not expire until August, there is no procedural urgency to re-ballot for mandate purposes before July 1. However, if a deal is reached, the BMA would need to ballot members on whether to accept it.

**Exact later resolution packet**

The question resolves **YES**.

The question asks whether, between May 12, 2026 00:00 UTC and July 1, 2026 23:59 UTC, the BMA officially opened or announced the opening of a new ballot of resident doctors in England related to the pay dispute (including a ballot on whether to accept/reject a government pay offer).

Evidence from the specified BMA resolution sources confirms this occurred:

- The BMA's official resident-doctor pay campaign page (https://www.bma.org.uk/our-campaigns/resident-doctor-campaigns/pay-in-england/pay-restoration-for-resident-doctors-in-england) states that resident doctors in England voted to accept an offer from the Government on pay and jobs, referencing the "Government offer to resident doctors in England to end the dispute on jobs and pay (June 2026)" [809e59].

- The BMA's official FAQ page on the offer (https://www.bma.org.uk/our-campaigns/resident-doctor-campaigns/pay-in-england/faqs-on-government-pay-offer-to-resident-doctors-june-2026) confirms the offer was put to members via a referendum — it references a "Referendum opt-out form" for members who received a voting link, and notes the UK RDC executive committee called off the strike scheduled for 15–19 June to "give members the opportunity to have their say on the offer." The page was published ~June 16, 2026 and updated June 21, 2026 [d569de].

- The BMA news-and-opinion page (https://www.bma.org.uk/news-and-opinion) carried the article "Resident doctors in England accept Government offer on pay and jobs," dated June 29, 2026, confirming the ballot took place and concluded with acceptance [cf2742].

Timeline (all within the resolution window of May 12 – July 1, 2026):
- On/around June 13, 2026, the BMA suspended the planned 15–19 June strike and announced it would put the new ~6.6% government offer to a member vote/referendum.
- Voting formally opened ~June 18, 2026 and closed June 26, 2026.
- Resident doctors voted to accept; the result was announced ~June 29, 2026.

Under the resolution criteria, "opening a ballot" is the date voting formally opened OR the date the BMA officially announced a ballot would be held, whichever is earlier. Both the announcement (~June 13) and the opening of voting (~June 18) fall squarely within May 12 – July 1, 2026. The ballot was of resident doctors in England (formerly "junior doctors") and was directly related to the pay dispute (a vote on accepting/rejecting the government's pay offer). All resolution-criteria conditions for YES are satisfied.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-40. `0559055f-bb51-5d22-897a-603ee0a3a265`

- Present date: `2026-05-14 04:18:37.600641`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Mexico officially set a date for the second round of judicial elections before July 1, 2026?

**Resolution criteria**

This question resolves YES if, on or after May 12, 2026 and by 23:59 Central Time (UTC-6) on June 30, 2026, the Mexican government officially sets a specific date for the second round of judicial elections (whether in 2027 or 2028).

"Officially sets a date" means one of the following:
1. A constitutional amendment or legislative decree specifying the election date is published in the Diario Oficial de la Federación (DOF) (https://www.dof.gob.mx/), OR
2. The National Electoral Institute (INE) publishes a formal electoral calendar specifying the date of the second judicial election on its official website (https://www.ine.mx/), OR
3. The Mexican Congress (either chamber) passes a binding resolution or constitutional reform setting the date, as recorded in the Gaceta Parlamentaria (https://gaceta.diputados.gob.mx/).

The authority to officially set the date rests with the Mexican Congress (via constitutional amendment published in the DOF) or the INE (via its formal electoral calendar). An executive statement or press conference alone does not count.

This question resolves NO if no such official action occurs by the deadline.

Primary resolution sources:
- Diario Oficial de la Federación: https://www.dof.gob.mx/
- INE official website: https://www.ine.mx/
- Gaceta Parlamentaria: https://gaceta.diputados.gob.mx/

**Pre-cutoff background**

Mexico's 2024 constitutional reform introduced the popular election of judges, magistrates, and other judicial officials. The first round of judicial elections took place on June 1, 2025. Under the original reform timeline, a second round of judicial elections is scheduled for 2027, coinciding with Mexico's midterm legislative elections on June 6, 2027.

However, as of April 2026, MORENA lawmakers introduced a constitutional initiative to postpone this second round from 2027 to 2028 [Lawmakers Seek to Delay Judicial Vote to 2028](https://mexicobusiness.news/policyandeconomy/news/lawmakers-seek-delay-judicial-vote-2028). Proponents argue the delay is needed to address problems identified during the first round, including weak candidate screening, low voter turnout, and the election of insufficiently qualified candidates [Lawmakers Seek to Delay Judicial Vote to 2028](https://mexicobusiness.news/policyandeconomy/news/lawmakers-seek-delay-judicial-vote-2028). The proposal aims to "perfect" the system by tightening rules and allowing more time for institutional preparation.

As of May 13, 2026, no official change to the original 2027 timeline has been enacted. The key uncertainty is whether the ruling MORENA coalition will pass a constitutional amendment to delay the elections to 2028, maintain the existing 2027 schedule by default, or formally confirm the 2027 date through an official INE (National Electoral Institute) calendar or decree. The question captures whether any formal, official date-setting action occurs before July 1, 2026.

**Exact later resolution packet**

The question resolves YES. Between May 12, 2026 and June 30, 2026, the Mexican government officially set a specific date for the second round of judicial elections via a constitutional reform decree published in the Diario Oficial de la Federación (DOF), satisfying resolution criterion #1.

Key evidence and chain of official actions:
- The Senate approved the constitutional reform postponing the judicial election from 2027 to 2028 on May 29, 2026, then sent it to the state legislatures [e22a89].
- The Comisión Permanente of Congress issued the declaration of constitutionality on June 1, 2026, after ratification by 25 state legislatures [f8d093].
- The decree was published in the DOF in its evening (vespertina) edition on June 2, 2026, titled "Decreto por el que se reforman y adicionan diversas disposiciones de la Constitución Política de los Estados Unidos Mexicanos, en materia de reforma al Poder Judicial," entering into force June 3, 2026. This is confirmed by the DOF/SIDOF metadata page (https://sidof.segob.gob.mx/notas/5789357, publicado 02-06-2026) [2a5683], corroborated by the DOF nota_detalle codigo 5789357 [d54651].
- The full text of the decree (https://sidof.segob.gob.mx/notas/docFuente/5789357) sets a specific date in its transitory articles: "Tercero. La jornada electoral de las elecciones judiciales federal y locales se celebrarán de forma coincidente el primer domingo de junio del año 2028," and the "Segundo" transitory confirms remaining judicial posts will be elected in the 2028 judicial elections [72bd5d].
- Additional confirmation from Garrigues (law firm) that the DOF decree of June 2, 2026 postpones the second judicial election to the first Sunday of June 2028 [be1f24].

Because a legislative/constitutional decree specifying the election date (first Sunday of June 2028) was published in the DOF on June 2, 2026 — squarely inside the May 12–June 30, 2026 window — the "officially sets a date" condition (criterion #1, and effectively #3 via the Congress's binding constitutional reform) is met. This is a final, passed and published decree, not a mere initiative or executive statement, so it counts for YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-41. `97b85a7c-7b00-5c52-9df4-3fa2ebf7f394`

- Present date: `2026-05-02 23:46:12.286836`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the US and China announce a new trade agreement or tariff reduction between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between 00:00 UTC on May 1, 2026 and 23:59 UTC on June 1, 2026, both of the following conditions are met:

1. The United States and China officially announce either:
   - A new bilateral trade agreement (defined as a signed or formally announced memorandum of understanding, executive order implementing new trade terms, joint statement committing to specific trade policy changes, or treaty regarding bilateral trade); **OR**
   - A reduction in existing tariff rates applied by the US on Chinese goods or by China on US goods (defined as an official announcement that specific tariff rates currently in effect will be lowered, suspended, or removed).

2. The announcement must be on or after May 1, 2026, 00:00 UTC. Extensions, renewals, or reaffirmations of the existing November 2025 Economic and Trade Arrangement without any new substantive tariff reductions or new trade commitments do **not** qualify. Non-binding verbal statements, press conference remarks, or social media posts alone do **not** qualify unless accompanied by an official government document (e.g., executive order, joint communiqué, or official press release from USTR, the White House, or China's Ministry of Commerce).

**Resolution sources:** Official announcements from the Office of the United States Trade Representative (https://ustr.gov), the White House (https://www.whitehouse.gov), or China's Ministry of Commerce (http://english.mofcom.gov.cn), or credible reporting from Reuters (https://www.reuters.com), Bloomberg, or the Associated Press confirming such an announcement.

If no qualifying announcement is made by 23:59 UTC on June 1, 2026, this question resolves **No**.

**Pre-cutoff background**

As of May 1, 2026, the United States and China are operating under an "Economic and Trade Arrangement" finalized on November 1, 2025, which followed a series of reciprocal tariff modifications throughout 2025 [Presidential Tariff Actions | United States Trade Representative](https://ustr.gov/trade-topics/presidential-tariff-actions). The trade relationship has been characterized by extreme volatility: both nations imposed levies exceeding 100% during 2025 escalations, and the US Supreme Court rejected Trump's global tariff regime in February 2026 [Trump's trade war with China in focus ahead of May summit | Reuters](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/). A sixth round of "constructive" trade talks was held in Paris in March 2026, and new Section 301 probes were launched that same month [Trump's trade war with China in focus ahead of May summit | Reuters](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/). US and Chinese trade chiefs held a "candid" call in late April 2026 ahead of a scheduled Trump-Xi summit in mid-May 2026 in China [Trump's trade war with China in focus ahead of May summit | Reuters](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/). The US average effective tariff rate stands at approximately 11.0% as of April 2, 2026 (per Yale Budget Lab), the highest since 1943. Current tariffs on Chinese goods include layers of Section 301, Section 232, IEEPA, and reciprocal tariffs, with effective rates on some Chinese products exceeding 100%. The mid-May summit is widely viewed as a potential venue for new trade agreements or tariff adjustments, but the administration has also signaled continued use of tariffs as a policy tool [Trump's trade war with China in focus ahead of May summit | Reuters](https://www.reuters.com/world/china/trumps-trade-war-with-china-focus-ahead-may-summit-2026-04-06/). All times referenced are in UTC.

**Exact later resolution packet**

The question resolves YES. Following the Trump-Xi summit in Beijing (May 14-15, 2026), both the US and China officially announced new substantive trade agreements and tariff reductions within the May 1 – June 1, 2026 window.

1. White House official Fact Sheet (dated May 17, 2026), titled "President Donald J. Trump Secures Historic Deals with China," documents new bilateral trade commitments going beyond the November 2025 Economic and Trade Arrangement. These include the chartering of two new institutions — the "U.S.-China Board of Trade" (managing bilateral trade across non-sensitive goods) and the "U.S.-China Board of Investment" — plus China's commitment to purchase at least $17 billion/year of US agricultural products in 2026, 2027 and 2028, and restored market access for US beef and poultry [414053]. URL: https://www.whitehouse.gov/fact-sheets/2026/05/fact-sheet-president-donald-j-trump-secures-historic-deals-with-china-delivering-for-american-workers-farmers-and-industry/

2. Reuters reporting (dated May 16, 2026) confirms China's Ministry of Commerce officially announced that China and the US "have agreed to expand agricultural trade through tariff reductions" and to pursue "reciprocal tariff reductions" — a specific, officially-announced reduction in tariff rates. China also granted five-year registration extensions to 425 US beef plants and approved 77 additional facilities, and agreed to resume beef imports from 17 US states [816cd9]. URL: https://www.reuters.com/world/china/china-signals-tariff-cuts-advances-farm-market-access-after-trump-xi-summit-2026-05-16/

Both conditions of the resolution criteria are satisfied: (a) the announcements concern new bilateral trade commitments AND specific tariff reductions (not merely an extension/reaffirmation of the November 2025 arrangement); (b) they occurred within the May 1 – June 1, 2026 window (May 16-17, 2026); and (c) they are supported by official government documents — the White House Fact Sheet and statements from China's Ministry of Commerce (reported by Reuters). The commitments include substantive trade policy changes (tariff reductions, market access restoration, multi-year purchase commitments), not merely "constructive" talks without finalized actions.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-42. `c212ef95-57b9-5713-8d29-a0e9e9221efc`

- Present date: `2026-05-13 21:12:25.159516`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-05-21 00:00:00`

**Question**

Will a Long Island Rail Road (LIRR) strike begin between May 12 and May 20, 2026?

**Resolution criteria**

This question resolves **Yes** if a [strike](https://en.wikipedia.org/wiki/Strike_action)—defined as a concerted, official work stoppage by members of any of the five LIRR unions listed above—begins on or after May 12, 2026, and on or before May 20, 2026, at 11:59 PM ET (Eastern Time). Even a brief work stoppage of any duration counts, as long as it is an officially called strike action (not a slowdown, sick-out, or other informal job action).

This question resolves **No** if no such strike begins by May 20, 2026, at 11:59 PM ET, whether because a deal is reached, a cooling-off period is extended, a court injunction is issued, or for any other reason.

**Resolution source:** Credible reporting from major news organizations confirming whether a strike has commenced, including but not limited to: [ABC7 NY](https://abc7ny.com/), [CBS New York](https://www.cbsnews.com/newyork/), [The New York Times](https://www.nytimes.com/), [Newsday](https://www.newsday.com/), [Reuters](https://www.reuters.com/), or the [MTA's official website](https://www.mta.info/article/lirr-strike-may-2026).

**Pre-cutoff background**

As of May 13, 2026, the Metropolitan Transportation Authority ([MTA](https://www.mta.info/)) and a coalition of five unions representing approximately 3,500 [Long Island Rail Road](https://en.wikipedia.org/wiki/Long_Island_Rail_Road) (LIRR) workers are in active contract negotiations. The five unions are the [Brotherhood of Locomotive Engineers and Trainmen](https://en.wikipedia.org/wiki/Brotherhood_of_Locomotive_Engineers_and_Trainmen), the [Brotherhood of Railroad Signalmen](https://en.wikipedia.org/wiki/Brotherhood_of_Railroad_Signalmen), the [International Association of Machinists and Aerospace Workers](https://en.wikipedia.org/wiki/International_Association_of_Machinists_and_Aerospace_Workers), the [International Brotherhood of Electrical Workers](https://en.wikipedia.org/wiki/International_Brotherhood_of_Electrical_Workers), and the [Transportation Communications Union](https://en.wikipedia.org/wiki/Transportation_Communications_International_Union) [Possible LIRR strike could happen Saturday if no deal is reached](https://abc7ny.com/live-updates/possible-lirr-strike-2026-could-happen-saturday-no-deal-is-reached/19080853/).

The dispute centers on the final year of a four-year contract. Both sides have agreed on raises of 3% for 2023, 3% for 2024, and 3.5% for 2025, but remain apart on the unions' demand for a 5% pay raise in 2026, with the MTA offering up to 4.5% with concessions on work rules [LIRR strike looms as negotiations continue between union and MTA](https://www.cbsnews.com/newyork/news/lirr-strike-2026-update-negotiations-mta/).

Under the [Railway Labor Act](https://en.wikipedia.org/wiki/Railway_Labor_Act), two [Presidential Emergency Boards](https://en.wikipedia.org/wiki/Presidential_Emergency_Board) (PEBs) have already been convened in this dispute; both sided with the unions but failed to produce a final agreement [Possible LIRR strike could happen Saturday if no deal is reached](https://abc7ny.com/live-updates/possible-lirr-strike-2026-could-happen-saturday-no-deal-is-reached/19080853/). The PEB process—the last federal intervention mechanism before a strike becomes legally permissible—has been exhausted. The unions have authorized a strike, and the strike deadline is set for 12:01 AM ET on May 16, 2026 [Possible LIRR strike could happen Saturday if no deal is reached](https://abc7ny.com/live-updates/possible-lirr-strike-2026-could-happen-saturday-no-deal-is-reached/19080853/). Negotiations resumed on May 11 and the next session was scheduled for May 13, 2026 [Possible LIRR strike could happen Saturday if no deal is reached](https://abc7ny.com/live-updates/possible-lirr-strike-2026-could-happen-saturday-no-deal-is-reached/19080853/). Governor Kathy Hochul has said she and her team are "immersed in the details" of negotiations. The MTA has released contingency plans involving shuttle bus services should a shutdown occur [LIRR strike looms as negotiations continue between union and MTA](https://www.cbsnews.com/newyork/news/lirr-strike-2026-update-negotiations-mta/).

Historically, last-minute deals are common in transit labor disputes, but the exhaustion of two PEBs makes this situation more unusual and the outcome more uncertain.

**Exact later resolution packet**

YES. The qualifying event occurred: Reuters reported at https://www.reuters.com/business/world-at-work/new-yorks-long-island-rail-road-workers-go-strike-halting-busiest-commuter-rail-2026-05-16/ that about 3,500 LIRR workers “went on strike” on Saturday, May 16, 2026, after failing to reach a wage agreement, and that the action halted the busiest U.S. commuter rail system; May 16 falls inside the specified May 12–May 20, 2026 window [New York's Long Island Rail Road strike halts busiest US commuter ...](https://www.reuters.com/business/world-at-work/new-yorks-long-island-rail-road-workers-go-strike-halting-busiest-commuter-rail-2026-05-16/). Reuters further described this as a “strike” and “work stoppage,” reported that the strike was launched by a group of five unions, and specifically identified union participants including the Brotherhood of Locomotive Engineers and Trainmen (BLET) and the Transportation Communications Union (TCU), satisfying the criterion that at least one named union officially called/participated in the work stoppage [New York's Long Island Rail Road strike halts busiest US commuter ...](https://www.reuters.com/business/world-at-work/new-yorks-long-island-rail-road-workers-go-strike-halting-busiest-commuter-rail-2026-05-16/). ABC7 New York likewise reported at https://abc7ny.com/live-updates/lirr-strike-2026-update-mta/19080853/ that a deal was reached to end a strike that had brought the commuter rail system to a standstill, that the strike began Saturday, and that the dispute involved the five listed unions: BLET, BRS, IAMAW, IBEW, and TCU [LIRR strike ends as unions, MTA reach deal after 3-day walkout](https://abc7ny.com/live-updates/lirr-strike-2026-update-mta/19080853/). The MTA’s official page at https://www.mta.info/article/lirr-strike-may-2026 confirms after the fact that “The Long Island Rail Road strike has ended and service has resumed” and that service had been suspended due to the labor action [LIRR service has resumed - MTA](https://www.mta.info/article/lirr-strike-may-2026). These reports establish an official strike/work stoppage, not merely a slowdown, sick-out, or informal action [New York's Long Island Rail Road strike halts busiest US commuter ...](https://www.reuters.com/business/world-at-work/new-yorks-long-island-rail-road-workers-go-strike-halting-busiest-commuter-rail-2026-05-16/) [LIRR strike ends as unions, MTA reach deal after 3-day walkout](https://abc7ny.com/live-updates/lirr-strike-2026-update-mta/19080853/) [LIRR service has resumed - MTA](https://www.mta.info/article/lirr-strike-may-2026). Because the strike actually began during the window, no cooling-off extension, court injunction, deal, or other delay prevented a qualifying strike before the deadline [New York's Long Island Rail Road strike halts busiest US commuter ...](https://www.reuters.com/business/world-at-work/new-yorks-long-island-rail-road-workers-go-strike-halting-busiest-commuter-rail-2026-05-16/).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-43. `6677da32-9b45-5cdf-b8fa-7c905de693f7`

- Present date: `2026-05-02 20:55:09.591488`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will any U.S. state enact a new comprehensive, cross-sectoral AI governance law between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if at least one U.S. state enacts a new comprehensive, cross-sectoral AI governance law on or after April 30, 2026, and by 23:59 UTC on June 1, 2026. Otherwise it resolves **No**.

**Definitions:**

- **"Enact"** means the bill is signed into law by the state's governor, or becomes law without the governor's signature (e.g., by expiration of a signing deadline or through a veto override). Bills that are merely passed by a legislature but vetoed do not qualify.

- **"Comprehensive, cross-sectoral AI governance law"** means a law that meets ALL of the following criteria:
  1. It applies broadly to private-sector organizations across multiple sectors of the economy (not limited to a single industry such as healthcare, insurance, education, or elections alone).
  2. It imposes substantive obligations on the development, deployment, or use of AI systems—such as impact assessments, algorithmic accountability requirements, transparency mandates, bias audits, or risk management frameworks.
  3. It explicitly references "artificial intelligence," "AI systems," "automated decision systems," or equivalent terminology in its operative provisions.
  
  Laws that are limited to any of the following do **not** qualify: regulation of only government/state agency use of AI; regulation of only a single narrow application (e.g., deepfakes, facial recognition, robocalls, or election-related AI content); creation of study committees or task forces without imposing regulatory obligations; or appropriations-only bills.

**Resolution source:** The primary resolution source is the [IAPP US State AI Governance Legislation Tracker](https://iapp.org/resources/article/us-state-ai-governance-legislation-tracker), which specifically tracks cross-sectoral AI governance bills applying to private sector organizations [US State AI Governance Legislation Tracker - IAPP](https://iapp.org/resources/article/us-state-ai-governance-legislation-tracker). Secondary sources include the [MultiState AI Legislation Tracker](https://www.multistate.ai/artificial-intelligence-ai-legislation) [State AI Legislation Tracker 2026: All 50 States - multistate.ai](https://www.multistate.ai/artificial-intelligence-ai-legislation), official state legislature websites (e.g., leginfo.legislature.ca.gov, capitol.texas.gov), and credible legal news sources (e.g., Reuters, Law360). If sources conflict, official state legislative records govern.

**Pre-cutoff background**

U.S. state legislatures are actively pursuing AI regulation. As of March 2026, lawmakers in 45 states had introduced 1,561 AI-related bills [State AI Legislation Tracker 2026: All 50 States - multistate.ai](https://www.multistate.ai/artificial-intelligence-ai-legislation), already surpassing the full-year 2024 total. By mid-April 2026, 25 AI-related bills had been signed into law in 2026, up from 6 in mid-March [AI Governance Watch: Nineteen New AI Bills Passed Into Law](https://pluralpolicy.com/blog/the-ai-governance-watch-april-2026-nineteen-new-ai-bills-passed-into-law/). These enacted laws span a wide range of topics—from narrow measures addressing deepfakes and AI in education to broader regulatory frameworks.

However, most enacted bills so far have been narrow or sector-specific. Only a handful of states have enacted truly comprehensive, cross-sectoral AI governance laws to date—notably Colorado (SB 205, enacted 2024), Texas (HB 149/TRAIGA, enacted 2025), and Utah (AI amendments in 2024-2025). The IAPP tracks "cross-sectoral AI governance bills that apply to private sector organizations" as a distinct category from narrower measures [US State AI Governance Legislation Tracker - IAPP](https://iapp.org/resources/article/us-state-ai-governance-legislation-tracker).

Several states with active legislative sessions through May-June 2026 (including California, New York, Michigan, New Jersey, Ohio, and others) have comprehensive AI governance bills under consideration. At the same time, the White House released a National Policy Framework for AI on March 20, 2026, and a December 2025 executive order signaled federal preemption ambitions, which may cause some governors to hesitate before signing broad AI laws. Resolution sources include the IAPP US State AI Governance Legislation Tracker (https://iapp.org/resources/article/us-state-ai-governance-legislation-tracker, updated April 28, 2026 [US State AI Governance Legislation Tracker - IAPP](https://iapp.org/resources/article/us-state-ai-governance-legislation-tracker)) and the MultiState AI Legislation Tracker (https://www.multistate.ai/artificial-intelligence-ai-legislation [State AI Legislation Tracker 2026: All 50 States - multistate.ai](https://www.multistate.ai/artificial-intelligence-ai-legislation)).

**Exact later resolution packet**

Adjudicated: Colorado Governor Polis signed SB 26-189 (the Automated Decision-Making Technology Act, repealing/replacing the 2024 Colorado AI Act) into law on May 14, 2026 — strictly within the April 30–June 1, 2026 window. The law is cross-sectoral (employment, education, lending/financial services, insurance, healthcare, essential services), imposes substantive obligations (pre-use clear notice, adverse-outcome notice, consumer rights to correction and meaningful human review, developer documentation duties), and explicitly uses 'automated decision-making technology' in its operative provisions, satisfying all three resolution criteria. The criteria expressly permit official state legislative records and credible legal news as secondary sources, so the fact that the IAPP tracker's April 28 snapshot predates the window does not preclude a YES; Connecticut SB 5 (signed late May 2026) is an additional qualifying enactment.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-44. `b7dbc504-98aa-51ac-b8f7-6bbcc2263768`

- Present date: `2026-05-13 21:19:33.515778`
- Source cutoff boundary: `2026-05-14` (encodes end of UTC day `2026-05-13`)
- Expected resolution: `2026-05-26 00:00:00`

**Question**

Will the 2026 Georgia Republican gubernatorial primary runoff feature both Rick Jackson and Burt Jones as the two candidates?

**Resolution criteria**

This question resolves based on the official results of the May 19, 2026 Georgia Republican gubernatorial primary, as published by the Georgia Secretary of State (https://sos.ga.gov/page/georgia-election-results) [Georgia Election Results | Georgia Secretary of State](https://sos.ga.gov/page/georgia-election-results). Results must occur on or after May 12, 2026 (UTC).

**Definitions:**
- "Candidate" refers to any individual who qualified to appear on the official Republican primary ballot for Governor of Georgia, as certified by the Georgia Secretary of State.
- "Runoff" refers to a run-off primary election as defined under Georgia Code § 21-2-501 (https://codes.findlaw.com/ga/title-21-elections/ga-code-sect-21-2-501/), which is triggered when no candidate receives a majority of the votes cast in the primary [Georgia Code Title 21. Elections § 21-2-501 - Codes - FindLaw](https://codes.findlaw.com/ga/title-21-elections/ga-code-sect-21-2-501/). The runoff is held between the two candidates receiving the highest number of votes.

**Resolution:**
- **Yes**: A runoff is triggered (no candidate receives more than 50% of votes cast in the May 19, 2026 primary), AND both Rick Jackson and Burt Jones are the two candidates who received the highest number of votes and thus qualify for the runoff.
- **No**: Either (a) a candidate wins the primary outright with more than 50% of the vote, meaning no runoff is required; OR (b) a runoff is triggered but the two qualifying candidates are not both Rick Jackson and Burt Jones (i.e., one or both are replaced by another candidate such as Brad Raffensperger or Chris Carr).

All times reference UTC.

**Pre-cutoff background**

The 2026 Georgia Republican gubernatorial primary is scheduled for May 19, 2026. Under Georgia law (Georgia Code § 21-2-501), if no candidate receives a majority (more than 50%) of the votes cast in the primary, a runoff election is held between the top two vote-getters, scheduled for the 28th day after the primary — June 16, 2026 [Georgia Code Title 21. Elections § 21-2-501 - Codes - FindLaw](https://codes.findlaw.com/ga/title-21-elections/ga-code-sect-21-2-501/).

As of early May 2026, the RealClearPolling average (February 28 – May 2, 2026) shows Rick Jackson at 26.2%, Burt Jones at 24.0%, and Brad Raffensperger at 14.2% [2026 Georgia Governor - RealClearPolling](https://www.realclearpolling.com/elections/governor/2026/georgia). With a crowded field and no candidate near 50%, a runoff is widely expected. Jackson and Jones are the clear frontrunners, but Raffensperger at ~14% and other candidates could potentially displace one of them in the top two. The question tests whether the expected Jackson-Jones matchup materializes or whether a late-breaking shift produces a surprise.

The official results will be published by the Georgia Secretary of State at https://sos.ga.gov/page/georgia-election-results [Georgia Election Results | Georgia Secretary of State](https://sos.ga.gov/page/georgia-election-results).

**Exact later resolution packet**

YES. The Georgia Secretary of State election-results landing page lists the “May 19th General Primary and Nonpartisan Election” and links its “View Results” page to https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926 [Georgia Election Results | Georgia Secretary of State](https://sos.ga.gov/page/georgia-election-results). On that official Georgia Secretary of State results page, the Republican Governor primary results were: Burt Jones 38.36% (358,170 votes), Rick Jackson 32.51% (303,614), Brad Raffensperger 15.00% (140,080), Chris Carr 11.86% (110,716), Clark Dean 0.76% (7,051), Gregg Kirkpatrick 0.59% (5,537), Ken Yasger 0.51% (4,770), and Tom Williams 0.41% (3,849) [https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926](https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926). Because no candidate exceeded 50%, the primary did not have an outright majority winner and a runoff was triggered under the question’s criteria [https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926](https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926). The top two vote-getters were Burt Jones and Rick Jackson, so both Burt Jones and Rick Jackson qualified for the runoff; therefore the question resolves YES [https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926](https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-45. `291c396e-2a62-5ab2-b98b-1acfb5d73d6c`

- Present date: `2026-05-02 10:56:14.224039`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-05-12 00:00:00`

**Question**

Will Venezuela send legal representatives to participate in the ICJ oral hearings in the Guyana v. Venezuela border case scheduled from May 4–11, 2026?

**Resolution criteria**

This question resolves **Yes** if, during the scheduled oral hearings from Monday, May 4, 2026, to Monday, May 11, 2026 (CEST, The Hague time), at least one agent or counsel officially representing the Bolivarian Republic of Venezuela is physically present at the Great Hall of Justice at the Peace Palace in The Hague, or delivers oral arguments (in person or by video link) during a public sitting in the case *Arbitral Award of 3 October 1899 (Guyana v. Venezuela)*.

This question resolves **No** if no agent or counsel representing Venezuela participates in any public sitting during the May 4–11, 2026, hearing sessions.

"Participation" is defined as: (a) physical presence of an agent or counsel at the Great Hall of Justice during a public sitting, or (b) the delivery of oral arguments or statements on behalf of Venezuela during a public sitting, whether in person or via video link.

The participation must occur on or after May 4, 2026 (CEST), during the scheduled oral hearings.

If the hearings are postponed or cancelled such that no public sittings occur by May 31, 2026, at 23:59 UTC, this question resolves **N/A**.

**Resolution source:** Official ICJ press releases, hearing schedules, verbatim records, or oral proceedings documents published at https://www.icj-cij.org/case/171. Credible news reporting (e.g., Reuters, AP, BBC) may be used as supplementary confirmation.

**Pre-cutoff background**

The International Court of Justice (ICJ) is hearing the case *Arbitral Award of 3 October 1899 (Guyana v. Venezuela)*, concerning sovereignty over the Essequibo region. Guyana filed the case on March 29, 2019. The ICJ has scheduled public hearings on the merits from Monday, May 4, 2026, to Monday, May 11, 2026, at the Peace Palace in The Hague [Public hearings on the merits to be held from Monday 4 to Monday ...](https://www.icj-cij.org/node/206313).

Venezuela has historically rejected the ICJ's jurisdiction over this dispute. However, Venezuela filed its rejoinder (the final written submission in the written phase) on August 11, 2025 [ICJ 2026 Update Brief: Guyana v. Venezuela | IMUNA | Model UN](https://imuna.org/blog/icj-2026-update-brief-guyana-v-venezuela/). On the same date, Venezuelan Executive Vice President Delcy Rodríguez stated that Venezuela would not recognize the ICJ's final ruling [ICJ 2026 Update Brief: Guyana v. Venezuela | IMUNA | Model UN](https://imuna.org/blog/icj-2026-update-brief-guyana-v-venezuela/). This creates a tension: Venezuela has engaged with the written proceedings but has publicly rejected the Court's authority.

As of May 1, 2026, it remains uncertain whether Venezuela will appear at the oral hearings. Participation could be seen as legitimizing ICJ jurisdiction, while non-participation risks a default judgment entirely on Guyana's terms. Venezuela's filing of a rejoinder suggests some strategic engagement, but its public rhetoric suggests possible non-appearance.

The hearings will be broadcast live on UN Web TV, and official records are published on the ICJ website at https://www.icj-cij.org/case/171.

**Exact later resolution packet**

Adjudicated: The hearings took place as scheduled (window condition met, no postponement), and Venezuela DID participate. Multiple independent sources confirm Venezuela's agent Samuel Reinaldo Moncada (Permanent Representative to the UN) and counsel Professor Makane Moise Mbengue physically appeared at the Peace Palace and delivered oral arguments on Wednesday May 6, 2026 (with a second-round slot on May 11), where Moncada stated 'Venezuela is here today because it cannot remain silent...' and argued the ICJ lacks jurisdiction. The resolution criteria require only physical presence of an agent/counsel OR delivery of oral arguments during a public sitting; both were satisfied. gpt55 simply failed to find the proceedings (relying on an ICJ page listing that did not attribute sittings by party), while opus48 correctly identified Venezuela's appearance.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-46. `71d9550f-515d-5c64-a63c-0b1d5c4cd50f`

- Present date: `2026-05-01 16:01:15.914525`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will China's Liaoning carrier strike group still be operating in the South China Sea on May 15, 2026 or later?

**Resolution criteria**

This question resolves YES if, on or after May 15, 2026 (00:00 UTC), the Chinese aircraft carrier Liaoning is confirmed to be operating within the South China Sea. It resolves NO otherwise.

**Definitions:**

- **South China Sea:** The body of water as defined by the International Hydrographic Organization and described in the Wikipedia article (https://en.wikipedia.org/wiki/South_China_Sea), bounded approximately by coordinates 3°N to 23°N latitude and 99°E to 121°E longitude. This includes waters south of mainland China and Taiwan, west of the Philippines, east of Vietnam, and north of Borneo/Malaysia.

- **Carrier strike group:** For the purposes of this question, only the presence of the aircraft carrier Liaoning (hull number 16) itself is required. It need not be accompanied by escort vessels to satisfy the resolution criteria.

- **"Operating within":** The Liaoning must be reported as being located within, or transiting through, the South China Sea boundaries defined above. Brief transits (e.g., passing through en route elsewhere) count.

- **Only events on or after April 30, 2026 (00:00 UTC) are considered** for resolution purposes. Prior deployments do not count. Specifically, the Liaoning must be confirmed present in the South China Sea on or after May 15, 2026 (00:00 UTC).

- All dates and times are in **UTC**.

**Resolution sources:** Credible reporting from any of the following: USNI News Fleet Tracker (https://news.usni.org/category/fleet-tracker), Reuters, Associated Press, South China Morning Post, official PLA announcements, or Taiwan Ministry of National Defense statements. At least one such source must confirm the Liaoning's presence in the South China Sea on or after May 15, 2026.

**Pre-cutoff background**

China deployed its aircraft carrier Liaoning and an accompanying naval force to the South China Sea in response to the U.S.-Philippines Balikatan 2026 exercises. The Liaoning transited the Taiwan Strait on April 20, 2026 [China's Liaoning Carrier Heads South: More Than a Routine Drill](https://thediplomat.com/2026/04/chinas-liaoning-carrier-heads-south-more-than-a-routine-drill/), and by April 23, satellite imagery showed 14 large naval vessels including the Liaoning near Yulin Naval Base in Hainan province [China stages navy drill as US and Philippines embark on Balikatan ...](https://www.scmp.com/news/china/military/article/3351353/china-stages-navy-drill-us-and-philippines-embark-balikatan-2026). The PLA Southern Theatre Command held drills in waters east of Luzon and described them as a "necessary action" in response to the regional situation [China stages navy drill as US and Philippines embark on Balikatan ...](https://www.scmp.com/news/china/military/article/3351353/china-stages-navy-drill-us-and-philippines-embark-balikatan-2026). China also deployed the Sichuan, its first Type 076 amphibious assault ship, from Shanghai to the South China Sea for training [China stages navy drill as US and Philippines embark on Balikatan ...](https://www.scmp.com/news/china/military/article/3351353/china-stages-navy-drill-us-and-philippines-embark-balikatan-2026).

Balikatan 2026 is the largest iteration of the annual U.S.-Philippines exercise to date, involving over 17,000 troops from multiple countries including Japan. The exercises run from approximately April 20 to May 8, 2026 (some sources indicate May 13) [China's Liaoning Carrier Heads South: More Than a Routine Drill](https://thediplomat.com/2026/04/chinas-liaoning-carrier-heads-south-more-than-a-routine-drill/). The key question is whether the Liaoning carrier strike group will remain deployed in the South China Sea after the Balikatan exercises conclude, which would signal a more sustained Chinese military posture rather than a temporary response to exercises. Historically, Chinese carrier deployments in response to exercises have sometimes been brief, but the current geopolitical context—including an upcoming Trump-Xi summit and Japan's unprecedented participation in Balikatan—may incentivize a longer deployment [China's Liaoning Carrier Heads South: More Than a Routine Drill](https://thediplomat.com/2026/04/chinas-liaoning-carrier-heads-south-more-than-a-routine-drill/).

**Exact later resolution packet**

Adjudicated: Per the named resolution source USNI News (May 22 and May 26, 2026), the Liaoning was spotted in the South China Sea via satellite around May 12 and the Liaoning Carrier Strike Group did not depart the SCS for its Western Pacific deployment until May 19, 2026, exiting via the Luzon Strait. A carrier that was satellite-confirmed in the SCS (at/near Yulin Naval Base, Hainan, ~18N 109E) and only departed the SCS for the Pacific on May 19 was necessarily operating within the SCS box during May 15-19 and transited its eastern boundary on May 19 (after the May 15 threshold), satisfying the literal criteria (brief transits count). An earlier automated NO erroneously required an explicit dated headline and ignored that a May 19 SCS departure entails on/after-May-15 SCS presence.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-47. `bd6ca71f-0cb1-5876-a262-79e701fdb50a`

- Present date: `2026-05-01 10:35:52.245478`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-05-21 00:00:00`

**Question**

Will the Georgia U.S. Senate Republican primary on May 19, 2026, result in a runoff election?

**Resolution criteria**

This question resolves **Yes** if the official results of the May 19, 2026 Republican primary for U.S. Senate in Georgia show that no candidate received a majority (more than 50%) of the votes cast, thereby triggering a runoff election under Georgia Code § 21-2-501 (https://law.justia.com/codes/georgia/title-21/chapter-2/article-12/section-21-2-501/).

This question resolves **No** if a candidate receives more than 50% of the votes cast and wins the Republican primary outright.

Resolution will be based on official results published by the Georgia Secretary of State at https://sos.ga.gov/page/georgia-election-results, or if those are delayed, based on credible reporting from the Associated Press, major news outlets, or unofficial results posted at https://app.enhancedvoting.com/results/public/Georgia. Results are expected to be available by 11:59 PM Eastern Time on May 20, 2026.

**Pre-cutoff background**

On May 19, 2026, Georgia will hold its primary elections for the U.S. Senate seat currently held by Democratic incumbent Jon Ossoff, who is seeking re-election [United States Senate election in Georgia, 2026 (May 19 Democratic ...](https://ballotpedia.org/United_States_Senate_election_in_Georgia,_2026_(May_19_Democratic_primary)). Under Georgia Code § 21-2-501, a candidate must receive a majority of the votes cast (more than 50%) to win a primary outright; otherwise, a runoff between the top two vote-getters is required [Georgia Code § 21-2-501 (2024) - Number of votes ... - Justia Law](https://law.justia.com/codes/georgia/title-21/chapter-2/article-12/section-21-2-501/).

**Republican primary:** Five qualified candidates are running: Earl "Buddy" Carter, Mike Collins, John Coyne, Derek Dooley, and Jonathan McColumn [United States Senate election in Georgia, 2026 (May 19 Republican ...](https://ballotpedia.org/United_States_Senate_election_in_Georgia,_2026_(May_19_Republican_primary)). With a crowded field of five candidates, the likelihood of a runoff is significant, as vote-splitting makes it harder for any single candidate to clear 50%. Recent polling suggests no single Republican candidate has consistently polled near the majority threshold.

**Democratic primary:** Incumbent Senator Jon Ossoff appears to be the only remaining qualified Democratic candidate, after other candidates withdrew or were disqualified [United States Senate election in Georgia, 2026 (May 19 Democratic ...](https://ballotpedia.org/United_States_Senate_election_in_Georgia,_2026_(May_19_Democratic_primary)). As a result, the Democratic primary is very unlikely to produce a runoff.

This question focuses on the Republican primary, where genuine uncertainty exists about whether any candidate will secure an outright majority. The runoff, if triggered, is scheduled for June 16, 2026.

**Exact later resolution packet**

YES. The official Georgia Secretary of State results page linked from https://sos.ga.gov/page/georgia-election-results to the May 19, 2026 General Primary results at https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926 [Georgia Election Results | Georgia Secretary of State](https://sos.ga.gov/page/georgia-election-results). In the Republican U.S. Senate primary contest (“US Senate - Rep”), the reported results were: Mike Collins 369,629 votes (40.50%), Derek Dooley 275,524 (30.19%), Earl L. “Buddy” Carter 229,216 (25.12%), Jonathan “Jon” McColumn 28,446 (3.12%), and John F. Coyne III 9,850 (1.08%), for 912,665 total votes cast [https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926](https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926). The top candidate, Mike Collins, therefore received 40.50% of the vote, which is not greater than 50% [https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926](https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926). Georgia Code § 21-2-501 requires a candidate to receive a majority of the votes cast to win a primary outright and provides for a runoff when no candidate receives a majority [https://law.justia.com/codes/georgia/title-21/chapter-2/article-12/section-21-2-501/](https://law.justia.com/codes/georgia/title-21/chapter-2/article-12/section-21-2-501/). I also checked for factors affecting the vote-cast denominator: the official contest results included votes for all five Republican candidates named in the question and did not indicate any candidate disqualification, withdrawal, or excluded votes affecting the 912,665 votes-cast total; contemporaneous credible reporting likewise described the race as going to a Collins–Dooley Republican runoff rather than identifying any ballot-status exception [https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926](https://results.sos.ga.gov/results/public/Georgia/elections/GeneralPrimary51926) [Georgia U.S. Senate race continues on with Collins, Dooley runoff ...](https://georgiarecorder.com/2026/05/20/georgia-u-s-senate-race-continues-with-collins-dooley-runoff-on-gop-side/). Because no Republican candidate received more than 50% of votes cast, the primary triggered a runoff, so the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-48. `605da7f9-d5e9-571e-a8ee-a2019f7940be`

- Present date: `2026-05-02 20:07:30.668567`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Bulgaria have a regular (non-caretaker) government in office by June 1, 2026?

**Resolution criteria**

This question resolves YES if, as of 23:59 UTC on May 31, 2026, Bulgaria has a regular (non-caretaker) government in office — meaning a Council of Ministers that has received a vote of confidence from the National Assembly (https://en.wikipedia.org/wiki/Council_of_Ministers_(Bulgaria)). A caretaker government appointed by the President does not count.

This question resolves NO if Bulgaria is governed by a caretaker government or has no government in place at that time.

Resolution will be determined based on official reporting from the Bulgarian National Assembly (https://www.parliament.bg/en) or credible international news sources such as Reuters (https://www.reuters.com), the BBC (https://www.bbc.com), or AP News (https://apnews.com).

Only the status as of May 31, 2026 matters. If a regular government was briefly in office but fell before that date, the question resolves NO.

**Pre-cutoff background**

Bulgaria adopted the euro on January 1, 2026, becoming the 21st eurozone member [Bulgaria and the euro - Wikipedia](https://en.wikipedia.org/wiki/Bulgaria_and_the_euro). The dual circulation period (during which both the lev and euro were accepted) lasted one month and ended on January 31, 2026 [Bulgaria and the euro - Wikipedia](https://en.wikipedia.org/wiki/Bulgaria_and_the_euro).

Despite this historic milestone, Bulgaria has been mired in deep political instability. Mass protests in late 2025 over the controversial 2026 budget and corruption led to the resignation of Prime Minister Rosen Zhelyazkov and his cabinet in December 2025. President Rumen Radev announced in January 2026 that Bulgaria would hold fresh snap elections after parties again failed to form a government — marking the country's eighth parliamentary election in approximately five years (https://www.lemonde.fr/en/international/article/2026/01/16/bulgaria-heads-for-eighth-snap-election-in-five-years_6749500_4.html). As of April 2026, young Bulgarians were heading to the polls amid continued uncertainty about whether any coalition can achieve a stable majority (https://www.theguardian.com/world/2026/apr/18/young-bulgarians-election-wave-of-protests).

Bulgaria's track record since 2021 has been one of repeated failures to form regular governments, with caretaker governments (appointed by the president, see https://en.wikipedia.org/wiki/Caretaker_government) filling the gaps. Given this pattern, whether Bulgaria can break the cycle and install a regular government backed by a parliamentary majority remains highly uncertain.

Meanwhile, Bulgaria's annual HICP inflation accelerated to 6.2% in April 2026 — the highest in the eurozone — adding economic pressure on any incoming government.

**Exact later resolution packet**

The question resolves YES if, as of 23:59 UTC on May 31, 2026, Bulgaria had a regular (non-caretaker) government in office that received a vote of confidence from the National Assembly.

Evidence:
- After Bulgaria's eighth snap election (held April 19, 2026), Rumen Radev's "Progressive Bulgaria" party won an outright majority. President Iliana Iotova gave Radev the mandate to form a government on May 5, 2026 (Reuters).
- On May 8, 2026, the Bulgarian National Assembly formally voted Radev's cabinet into office. Multiple credible international sources confirm the vote of confidence: the parliament voted 124 in favour, 70 against, with 36 abstentions, electing Radev as Prime Minister and approving his Council of Ministers [898f4c][9058ea]. This is a regular government that received a vote of confidence from the National Assembly — explicitly satisfying the YES criteria — not a caretaker government appointed by the President.
- This was described as the first majority government to rule Bulgaria since 1997, ending the cycle of caretaker governments (Politico, Euronews, Washington Post, Xinhua).
- The government took office on May 8, 2026, only three weeks before the deadline. Searches for any resignation, collapse, or successful no-confidence vote against the Radev government before May 31, 2026 returned no such events; the only government resignations found relate to the prior Zhelyazkov cabinet in December 2025. The newly installed majority government therefore remained in office through the May 31, 2026 deadline.

Therefore, as of 23:59 UTC on May 31, 2026, Bulgaria had a regular (non-caretaker) government in office, and the question resolves YES (1).

Key URLs:
- https://balkaninsight.com/2026/05/08/radevs-party-takes-office-in-bulgaria-pledging-stability-but-raising-early-doubts/bi/
- https://www.euronews.com/my-europe/2026/05/08/bulgarian-parliament-confirms-rumen-radev-as-new-prime-minister
- https://www.washingtonpost.com/world/2026/05/08/bulgaria-parliament-rumen-radev-government/
- https://www.politico.eu/article/rumen-radev-sweeps-into-power-bulgaria-names-new-prime-minister/
- https://english.news.cn/20260508/2066443fe40e4817bd8173f637302272/c.html
- https://www.reuters.com/world/bulgarias-president-gives-mandate-election-winner-radev-form-government-2026-05-05/

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-49. `11eacb09-582e-5d86-8d96-27746d308817`

- Present date: `2026-04-30 15:25:44.430311`
- Source cutoff boundary: `2026-05-01` (encodes end of UTC day `2026-04-30`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the U.S. House of Representatives pass S.Con.Res. 33 (FY2026 border/immigration budget resolution) by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after April 30, 2026, and no later than 11:59 PM UTC on June 1, 2026, the U.S. House of Representatives agrees to (i.e., passes via a recorded floor vote by simple majority) S.Con.Res. 33, the concurrent resolution setting forth the congressional budget for fiscal year 2026 as passed by the Senate on April 23, 2026. "Pass" means the resolution is agreed to by the House via a floor vote achieving a simple majority of those present and voting. The question resolves **No** if the House does not pass the resolution by 11:59 PM UTC on June 1, 2026.

Primary resolution source: the official bill status page at https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/33 . Supplementary confirmation may come from https://clerk.house.gov/ or credible reporting (e.g., AP, Reuters, C-SPAN).

**Pre-cutoff background**

On April 23, 2026, the U.S. Senate passed S.Con.Res. 33 — a concurrent resolution setting forth the congressional budget for the United States Government for fiscal year 2026 and budgetary levels for FY2027–2035 — by a vote of 50-48 [https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/33](https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/33). The resolution includes reconciliation instructions directing relevant committees to submit legislation increasing the deficit by up to $70 billion over FY2026–2035, intended to fund Immigration and Customs Enforcement (ICE) and Customs and Border Protection (CBP). President Trump gave Congress a June 1, 2026 deadline to pass a bill funding ICE and Border Patrol.

As of April 30, 2026, S.Con.Res. 33 is "held at the desk" in the House of Representatives and has not yet been voted on [https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/33](https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/33). The House must adopt this resolution (or an identical version) before reconciliation legislation can proceed. House passage is uncertain due to potential intra-party disagreements among Republicans, competing priorities related to a broader reconciliation package, and narrow GOP margins — the House previously passed the broader H.Con.Res. 14 budget resolution with only a 215-211 margin.

**Exact later resolution packet**

Adjudicated: The House agreed to the Senate-passed S.Con.Res. 33 by recorded floor vote (Roll Call 143: 215 Yea, 211 Nay, 1 Present, 3 Not Voting — a simple majority of those present and voting) on April 29, 2026 at 10:39 PM Eastern Time per the official House Clerk record. The resolution window is anchored in UTC ('no later than 11:59 PM UTC on June 1, 2026'); read consistently, the start boundary 'on or after April 30, 2026' is also UTC. 10:39 PM EDT April 29 = 02:39 UTC April 30, 2026, which falls on/after April 30 UTC and inside the window, so every substantive and timing condition is met. An initial automated pass incorrectly read the vote date as April 29 in Eastern Time while applying UTC only to the deadline boundary, which is internally inconsistent.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-50. `2f23efc6-8d96-5548-9e68-2ca30fd5f9db`

- Present date: `2026-05-15 20:45:51.296420`
- Source cutoff boundary: `2026-05-16` (encodes end of UTC day `2026-05-15`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Keir Starmer be serving as Prime Minister of the United Kingdom on July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if Keir Starmer is serving as Prime Minister of the United Kingdom at 12:00 PM BST (11:00 AM UTC) on July 1, 2026, as confirmed by the official UK Government list of Prime Ministers at https://www.gov.uk/government/history/past-prime-ministers or the current PM page at https://www.gov.uk/government/people/prime-minister. "Serving as Prime Minister" means holding the office by virtue of appointment by the Monarch and not yet having tendered a resignation that has been accepted, or been replaced. If the GOV.UK page is unavailable, resolution may rely on credible major news sources such as the BBC (https://www.bbc.co.uk/news), Reuters, or the Associated Press confirming who holds the office. This question resolves **No** if, by 12:00 PM BST on July 1, 2026, Starmer has resigned, been removed from office, or otherwise ceased to serve as Prime Minister for any reason.

**Pre-cutoff background**

As of May 13, 2026, Keir Starmer remains the Prime Minister of the United Kingdom, but faces an unprecedented leadership crisis within the Labour Party. Following disastrous local election results in early May 2026—in which Labour lost nearly 1,500 council seats across England, the Welsh parliament, and a previously winnable Scottish election [https://www.politico.eu/article/keir-starmer-labour-party-leadership-chaos/](https://www.politico.eu/article/keir-starmer-labour-party-leadership-chaos/)—three cabinet ministers have resigned and pressure on Starmer to step down has intensified [https://www.theguardian.com/politics/2026/may/11/labour-mp-keir-starmer-leadership-challenge-catherine-west](https://www.theguardian.com/politics/2026/may/11/labour-mp-keir-starmer-leadership-challenge-catherine-west). Approximately 90 Labour MPs have urged him to set a timetable for his departure, while over 100 have signed a letter of support. Starmer has publicly vowed to remain in office, telling his cabinet on May 12 that he will "get on with governing" and will fight any leadership challenge [https://www.theguardian.com/politics/2026/may/11/labour-mp-keir-starmer-leadership-challenge-catherine-west](https://www.theguardian.com/politics/2026/may/11/labour-mp-keir-starmer-leadership-challenge-catherine-west) [https://www.politico.eu/article/keir-starmer-labour-party-leadership-chaos/](https://www.politico.eu/article/keir-starmer-labour-party-leadership-chaos/). Under Labour Party rules, a formal leadership contest requires nominations from at least 81 MPs (20% of the parliamentary Labour Party). If triggered, the incumbent leader is automatically placed on the ballot [https://www.politico.eu/article/keir-starmer-labour-party-leadership-chaos/](https://www.politico.eu/article/keir-starmer-labour-party-leadership-chaos/). Key potential challengers include Health Secretary Wes Streeting, whom Starmer is scheduled to meet. The political situation remains highly volatile, with multiple pathways to resolution: Starmer could survive without a challenge, win a formal contest, resign voluntarily under pressure, or lose a leadership contest.

**Exact later resolution packet**

RESOLUTION: YES (1). Keir Starmer was still serving as Prime Minister of the United Kingdom at 12:00 PM BST on July 1, 2026.

KEY FACTS AND TIMELINE:
- On Monday 22 June 2026, Starmer ANNOUNCED his resignation as Labour leader and his intention to resign as Prime Minister, but explicitly agreed to remain in office as caretaker PM until a successor is chosen (widely reported, e.g. Reuters "UK's Starmer resigns, paving way for orderly transfer of power," Guardian live blog, and Wikipedia).
- The official Labour Party page for the 2026 leadership election states verbatim: "Keir Starmer will remain Leader of the Labour Party and Prime Minister until the election has concluded" [c3dd82]. That same page's published timetable shows PLP nominations only BEGIN on 9 July 2026, with the earliest possible successor announcement at a special conference on 17 July 2026 and the full-ballot process not concluding until 29 August 2026 [c3dd82].
- A BBC News article dated ~30 June 2026 confirms: "Despite announcing his resignation, Sir Keir will stay as prime minister until a new Labour leader is elected," and that any successor (e.g. Andy Burnham) would only "be appointed PM by the King" on ~17 July 2026 at the earliest [653177].

APPLYING THE RESOLUTION CRITERIA LITERALLY:
The criteria define "Serving as Prime Minister" as "holding the office by virtue of appointment by the Monarch and not yet having tendered a resignation that has been accepted, or been replaced." The question resolves NO only if, by 12:00 PM BST on 1 July 2026, Starmer "has resigned, been removed from office, or otherwise ceased to serve."

On 1 July 2026:
1. Starmer still HELD the office by appointment of the Monarch (appointed July 2024, never left No. 10).
2. He had NOT tendered a resignation to the Monarch that had been ACCEPTED. Under UK constitutional convention, an outgoing PM formally tenders resignation to the Monarch only on the day the successor is ready to be appointed (same-day handover). The 22 June announcement was a political announcement of INTENT to resign as party leader, not a resignation accepted by the King. The BBC's statement that the new leader would "be appointed PM by the King" only from 17 July [653177] confirms the throne had accepted no Starmer resignation as of 1 July.
3. He had NOT been replaced. No successor could be appointed before 17 July at the earliest [c3dd82, 653177].

OFFICIAL GOV.UK CHECK (as required by criteria): The GOV.UK "Past Prime Ministers" list (https://www.gov.uk/government/history/past-prime-ministers) does NOT list Starmer among past PMs—the most recent past PM shown is Rishi Sunak (term ended 2024)—which is consistent with Starmer still being the sitting PM [4f97f3]. (The GOV.UK current-PM page, https://www.gov.uk/government/people/prime-minister, returned no retrievable content on my attempts, so per the criteria I relied on the Past PMs list plus the Labour Party official page and BBC.)

CONCLUSION: Because Starmer had neither had a resignation accepted by the Monarch nor been replaced by 12:00 PM BST on 1 July 2026—he was the sitting caretaker Prime Minister—the question resolves YES (1).

NOTE ON A COMMON MISREADING: Some might argue the 22 June resignation announcement means he "resigned" and thus resolve NO. This is incorrect under the criteria's explicit two-pronged test (accepted resignation OR replacement), and contradicts the primary sources, which uniformly state he "will stay as prime minister" [653177] / "will remain ... Prime Minister until the election has concluded" [c3dd82]. This mirrors precedent (e.g., Boris Johnson remaining PM July–Sept 2022 after announcing resignation).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-51. `2d3f7f7e-1a74-5072-82a3-53fc0ab24cf0`

- Present date: `2026-05-03 10:35:25.457061`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will California Assembly Bill 2325 (bilingual teacher pipeline) pass the Assembly Appropriations Committee by June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, on or after May 2, 2026 (00:00 UTC), and before June 1, 2026 (23:59 UTC), the Assembly Appropriations Committee takes a "Do Pass" or "Do Pass as Amended" vote on AB 2325, as reflected on the official bill status page on the California Legislative Information website:

https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2325

This question resolves **No** if:
- The bill remains on the Appropriations Committee's suspense file without being voted out by June 1, 2026 (23:59 UTC);
- The bill is held in committee, fails to receive a passing vote, or otherwise does not move out of the Appropriations Committee by June 1, 2026 (23:59 UTC); or
- No action beyond referral is recorded on the bill's status page by the resolution date.

The sole resolution source is the bill's official status page on the California Legislative Information website at the URL above [https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2325](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2325).

**Pre-cutoff background**

California Assembly Bill 2325 (AB 2325), titled "Teachers: bilingual teachers: Pathways to Bilingual Teaching Program," was authored to support the bilingual teacher pipeline in California. The bill passed the Assembly Education Committee unanimously (9-0) on April 15, 2026, and was re-referred to the Assembly Appropriations Committee on April 21, 2026 [https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2325](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2325).

The Assembly Appropriations Committee is a critical gatekeeper in California's legislative process. Bills with fiscal impacts are reviewed here and may be placed on a "suspense file"—a holding mechanism for bills with significant costs—where they can be held indefinitely or killed. The bill requires an appropriation to be operative, making the Appropriations Committee a genuine hurdle despite the bill's unanimous Education Committee support. The state's budget situation and the committee chair's priorities will influence outcomes. The Appropriations Committee typically holds its suspense file hearings in mid-to-late May.

As of May 2, 2026, the bill is pending in the Assembly Appropriations Committee awaiting a hearing [https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2325](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2325).

**Exact later resolution packet**

The question resolves YES.

According to the official California Legislative Information bill status page for AB 2325 (https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2325), the bill's history in the Assembly Appropriations Committee is as follows [https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2325](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2325):
- May 6, 2026: The bill was set for hearing and referred to the Assembly Appropriations Committee suspense file.
- May 14, 2026: The Assembly Appropriations Committee took action with a motion of "Do pass," which passed 15 Ayes to 0 Noes.

The resolution criteria require a "Do Pass" or "Do Pass as Amended" vote by the Assembly Appropriations Committee on or after May 2, 2026 (00:00 UTC) and before June 1, 2026 (23:59 UTC). The "Do pass" vote on May 14, 2026 falls squarely within this window. Although the bill was placed on the suspense file on May 6, 2026, it was voted out of suspense (with the "Do pass" motion) on May 14, 2026—well before the June 1, 2026 deadline. The bill subsequently was read a second time on May 18, 2026 and passed the Assembly floor on May 26, 2026, confirming it moved out of committee [https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2325](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB2325).

This satisfies the YES condition.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-52. `e6d9cf32-49f0-5d6a-8eda-bd19cda1e4be`

- Present date: `2026-05-03 04:14:58.693173`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Pope Leo XIV's encyclical "Magnifica Humanitas" on Artificial Intelligence be officially published by June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, on or after May 1, 2026, 00:00 UTC, and no later than June 1, 2026, 23:59 UTC, the Holy See officially publishes a document on the Vatican's official website (https://www.vatican.va) that meets **both** of the following criteria:

1. **It is an encyclical**: The document is explicitly designated as an "Encyclical" or "Encyclical Letter" (*Litterae Encyclicae*) by the Vatican. An [encyclical](https://www.britannica.com/topic/encyclical) is a pastoral letter written by the pope for the whole Roman Catholic Church on matters of doctrine, morals, or discipline [https://www.britannica.com/topic/encyclical](https://www.britannica.com/topic/encyclical). Other document types (e.g., Apostolic Exhortations, Motu Proprios, messages) do not qualify.

2. **It is specifically focused on Artificial Intelligence**: The document's title, subtitle, or official Vatican summary explicitly identifies "Artificial Intelligence" or "AI" as a primary subject, OR the document is the encyclical known by its working title *Magnifica Humanitas* which has been reported as addressing AI [Was Pope Leo XIV Offering His African Audiences a Preview of His ...](https://www.ncregister.com/news/leo-xiv-africa-preview-new-encyclical) [Leo XIV prepares an encyclical on AI reviewed by Tucho - infovaticana](https://infovaticana.com/en/2026/02/03/leo-xiv-prepares-an-encyclical-on-ai-reviewed-by-tucho/).

The question resolves as **No** if no such document is published by June 1, 2026, 23:59 UTC.

**Resolution source**: The official Vatican website at https://www.vatican.va/content/leo-xiv/en/encyclicals.html, supplemented by reporting from Vatican News (https://www.vaticannews.va), the National Catholic Register, Reuters, or AP.

**Pre-cutoff background**

Pope Leo XIV has been preparing his first encyclical, with the working title *Magnifica Humanitas* ("Magnificent Humanity"), which is expected to address the ethical and social implications of Artificial Intelligence (AI) [Was Pope Leo XIV Offering His African Audiences a Preview of His ...](https://www.ncregister.com/news/leo-xiv-africa-preview-new-encyclical). An [encyclical](https://www.britannica.com/topic/encyclical) is a formal pastoral letter written by the pope for the whole Roman Catholic Church on matters of doctrine, morals, or discipline [https://www.britannica.com/topic/encyclical](https://www.britannica.com/topic/encyclical).

As of May 1, 2026, the encyclical has not yet been published. Key developments include:

- **February 2026**: Reports emerged that Cardinal Víctor Manuel Fernández, prefect of the Dicastery for the Doctrine of the Faith, has been coordinating the review and preparation of the document. The encyclical is expected to articulate the Church's ethical vision on AI, focusing on human dignity, the risks of technology replacing human capacities, and its impact on youth and education [Leo XIV prepares an encyclical on AI reviewed by Tucho - infovaticana](https://infovaticana.com/en/2026/02/03/leo-xiv-prepares-an-encyclical-on-ai-reviewed-by-tucho/).
- **January 2026**: Pope Leo XIV issued a message for the 60th World Communications Day warning about AI systems capable of simulating human traits, and made "The Good Use of Artificial Intelligence" one of his prayer intentions for 2026.
- **April 2026**: During his trip to Africa (Algeria, Cameroon, Angola, Equatorial Guinea), the Pope delivered speeches widely interpreted as previews of the encyclical's themes, including the societal impact of AI, the role of the Church, and peace [Was Pope Leo XIV Offering His African Audiences a Preview of His ...](https://www.ncregister.com/news/leo-xiv-africa-preview-new-encyclical).

The Vatican has previously engaged with AI through the "Rome Call for AI Ethics" and the document *Antiqua et Nova* (January 2025), but an encyclical would represent the most authoritative form of papal teaching on this subject [Leo XIV prepares an encyclical on AI reviewed by Tucho - infovaticana](https://infovaticana.com/en/2026/02/03/leo-xiv-prepares-an-encyclical-on-ai-reviewed-by-tucho/). No official release date has been announced as of May 1, 2026 [Was Pope Leo XIV Offering His African Audiences a Preview of His ...](https://www.ncregister.com/news/leo-xiv-africa-preview-new-encyclical).

**Exact later resolution packet**

The question resolves YES. All resolution criteria are satisfied:

1. **It is an encyclical**: The official Vatican encyclicals page for Pope Leo XIV lists "Encyclical Letter of His Holiness Leo XIV Magnifica Humanitas (15 May 2026)" [https://www.vatican.va/content/leo-xiv/en/encyclicals.html](https://www.vatican.va/content/leo-xiv/en/encyclicals.html). It is explicitly designated as an "Encyclical Letter" (Litterae Encyclicae), with a direct Vatican URL: http://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html

2. **Focused on Artificial Intelligence**: The full title is "Magnifica Humanitas ... On Safeguarding the Human Person in the Time of Artificial Intelligence" — explicitly identifying AI as the primary subject, and it is the very encyclical referenced by the working title in the question.

3. **Authored by Pope Leo XIV**: Confirmed across the Vatican page [https://www.vatican.va/content/leo-xiv/en/encyclicals.html](https://www.vatican.va/content/leo-xiv/en/encyclicals.html) and multiple allowed news sources (Vatican News, NCRegister, OSV News, EWTN).

4. **Published within the window (May 1, 2026 00:00 UTC – June 1, 2026 23:59 UTC)**: The Pope signed the encyclical on May 15, 2026 (the 135th anniversary of Rerum Novarum), and the Holy See formally released/published it on Monday, May 25, 2026. Both the signing date (May 15) and the public release date (May 25) fall squarely within the required window. The Vatican's official encyclicals listing dates it 15 May 2026 [https://www.vatican.va/content/leo-xiv/en/encyclicals.html](https://www.vatican.va/content/leo-xiv/en/encyclicals.html), and Vatican News, OSV News, EWTN, and NCRegister all confirm the May 25, 2026 publication.

Since the document is an officially published encyclical on vatican.va, explicitly focused on Artificial Intelligence, authored by Pope Leo XIV, titled Magnifica Humanitas, and published within May 1 – June 1, 2026, the question resolves YES.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-53. `d5fe2dcf-bd64-5bb6-be74-932e21fd47e2`

- Present date: `2026-05-01 18:47:53.881713`
- Source cutoff boundary: `2026-05-02` (encodes end of UTC day `2026-05-01`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Judge Mehta rule on Google's motion to stay the search antitrust data-sharing and syndication mandates pending appeal between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves **Yes** if Judge Amit Mehta issues a ruling — defined as a written order or oral ruling on the record that explicitly grants, denies, or partially grants/denies Google's motion(s) to stay the data-sharing and syndication mandates — on or after April 30, 2026 (12:00 AM Eastern Time) and on or before June 1, 2026 (11:59 PM Eastern Time).

**Definitions:**
- "Data-sharing mandates" refers to the provisions in Judge Mehta's September 2025 remedies order in *United States et al. v. Google LLC* (Case No. 1:20-cv-03010) requiring Google to share search index data and user search query data with Qualified Competitors.
- "Syndication mandates" refers to the provisions in the same order requiring Google to enter into search syndication license agreements and search text ads syndication agreements with Qualified Competitors on commercially reasonable terms.
- A "ruling" means any judicial order or decision explicitly addressing the merits of Google's motion to stay these mandates. Administrative orders (e.g., scheduling orders, briefing orders) do not count.

This question resolves **No** if no such ruling is issued by 11:59 PM Eastern Time on June 1, 2026.

**Resolution source:** The official court docket for *United States et al. v. Google LLC* (Case No. 1:20-cv-03010), accessible via [PACER](https://pacer.uscourts.gov/), or credible legal news reporting from outlets such as Reuters, Courthouse News Service, Bloomberg Law, or Law360 confirming the issuance or absence of such a ruling.

**Pre-cutoff background**

In August 2024, U.S. District Judge Amit Mehta ruled that Google violated antitrust law by monopolizing general search services and search text advertising markets. In September 2025, Judge Mehta issued a remedies order requiring Google to: (1) share its search index data and user search query data with "Qualified Competitors" screened by a court-appointed Technical Committee; and (2) enter into search syndication license agreements and search text ads syndication agreements with qualified competitors on commercially reasonable terms [DOJ Fights Google's 'Premature' Request To Stay Antitrust Order](https://www.mediapost.com/publications/article/412479/doj-fights-googles-premature-request-to-stay-an.html).

Google filed a motion in January 2026 to stay these data-sharing and syndication mandates pending appeal to the D.C. Circuit. The DOJ opposed, calling the request "premature" because the mandates are not yet operational — the Technical Committee responsible for screening Qualified Competitors and establishing implementation parameters was still being set up [DOJ Fights Google's 'Premature' Request To Stay Antitrust Order](https://www.mediapost.com/publications/article/412479/doj-fights-googles-premature-request-to-stay-an.html). As of February 2026, three of five Technical Committee members had been appointed (Tammy Savage, Gerry Campbell, and Professor John Abowd), with the committee tasked with proposing two additional members [Judge instructs DOJ, Google to hash out details of antitrust oversight ...](https://www.courthousenews.com/judge-instructs-doj-google-to-hash-out-details-of-antitrust-oversight-body/). The parties also disputed whether committee members should serve full-time or part-time [Judge instructs DOJ, Google to hash out details of antitrust oversight ...](https://www.courthousenews.com/judge-instructs-doj-google-to-hash-out-details-of-antitrust-oversight-body/).

On April 17, 2026, Google filed an emergency motion to stay the data-sharing mandate, and on April 25, 2026, filed a further request to pause both the data-sharing and syndication obligations [Google's 90% Search Monopoly Faces DOJ Breakup [2026]](https://tech-insider.org/google-antitrust-appeal-doj-search-monopoly-2026/). As of April 27, 2026, Judge Mehta has not ruled on any of these stay motions [Google's 90% Search Monopoly Faces DOJ Breakup [2026]](https://tech-insider.org/google-antitrust-appeal-doj-search-monopoly-2026/). The case docket is *United States et al. v. Google LLC*, Case No. 1:20-cv-03010, U.S. District Court for the District of Columbia.

**Exact later resolution packet**

The question asks whether Judge Amit Mehta issued a ruling explicitly granting, denying, or partially deciding Google's motion(s) to stay the data-sharing and syndication mandates pending appeal between April 30, 2026 (12:00 AM ET) and June 1, 2026 (11:59 PM ET).

The evidence confirms YES. On May 7, 2026, Judge Mehta DENIED Google's motion for a partial stay of the final judgment pending appeal. This is a substantive ruling on the merits of the stay (a denial), not an administrative order.

Key sources:
- The National Law Journal (Law.com), "Antitrust Remedies Order Takes Effect as US Judge Denies Google's Stay Motion," published May 8, 2026, confirms Judge Mehta denied Google's motion for a partial stay pending appeal of his final judgment requiring Google to share search data with rival search engines, and ordered the DOJ to notify the court and Google 45 days before any Qualified Competitor may begin to access a data-sharing or syndication remedy [13e3cc]. The order reasoned that "there is no rule in this circuit that any disclosure of information is an irreparable harm sufficient to warrant a stay" [13e3cc].
- MLex reported (May 7, 2026, 9:57 PM GMT) that "Google's motion for a partial stay of the final judgment pending appeal... was denied without prejudice by a US federal judge."

The motion that was denied addressed precisely the data-sharing and syndication mandates from the September 2025 remedies order (sharing search index/user query data and entering syndication agreements with Qualified Competitors). The ruling fell squarely within the resolution window (May 7, 2026).

The other queried source (MediaPost, Feb 9, 2026) predates the window and merely confirms the motion was filed; it is not the resolving source [56a700].

Therefore the question resolves YES (1) — the ruling was a DENIAL (without prejudice) of Google's motion to stay the data-sharing and syndication mandates.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-54. `5acff98b-4783-5fab-aea8-cd47d18b2597`

- Present date: `2026-05-14 10:35:37.315362`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Supreme Court rule in favor of the petitioner (Trump) in Trump v. Slaughter (No. 25-332)?

**Resolution criteria**

This question resolves **Yes** if the Supreme Court of the United States, in its opinion in Trump v. Slaughter (No. 25-332), reverses or vacates the lower court's judgment in whole or in part — i.e., rules in favor of the petitioner, Donald J. Trump. This includes any disposition that overturns, narrows, or remands the lower court's ruling in a manner favorable to Trump.

This question resolves **No** if:
- The Supreme Court affirms the lower court's judgment in full (i.e., rules in favor of Slaughter); or
- The writ of certiorari is dismissed (e.g., dismissed as improvidently granted), leaving the lower court's pro-Slaughter ruling intact.

The ruling must be issued on or after May 12, 2026 (Eastern Time). If no ruling is issued by 11:59 PM Eastern Time on July 1, 2026, the question resolves **No**.

**Resolution source:** The official Supreme Court opinion as published on the Supreme Court's website (https://www.supremecourt.gov/opinions/slipopinions.aspx) or as reported by SCOTUSblog (https://www.scotusblog.com/cases/trump-v-slaughter-2/).

**Pre-cutoff background**

Trump v. Slaughter (Supreme Court Docket No. 25-332) concerns whether the President has the constitutional authority to remove Federal Trade Commission (FTC) commissioners at will, notwithstanding statutory for-cause removal protections. The petitioner is Donald J. Trump, President of the United States, and the respondent is Rebecca Kelly Slaughter, an FTC commissioner.

The lower court — the U.S. District Court for the District of Columbia — ruled in favor of Slaughter, effectively upholding the statutory removal protections and preventing her dismissal [https://www.scotusblog.com/cases/trump-v-slaughter-2/](https://www.scotusblog.com/cases/trump-v-slaughter-2/). The Supreme Court granted certiorari before judgment and heard oral arguments on December 8, 2025 [https://www.scotusblog.com/cases/trump-v-slaughter-2/](https://www.scotusblog.com/cases/trump-v-slaughter-2/). The case is closely tied to the question of whether the landmark 1935 precedent Humphrey's Executor v. United States should be overruled or limited.

As of May 12, 2026, the Supreme Court has not yet issued its opinion. Decisions for cases argued during the October 2025 Term are typically released by late June or early July 2026. Analysis from SCOTUSblog following oral argument suggested the Court appeared likely to side with Trump on the president's power to fire FTC commissioners, though the outcome and scope of any ruling remain uncertain [https://www.scotusblog.com/cases/trump-v-slaughter-2/](https://www.scotusblog.com/cases/trump-v-slaughter-2/).

**Exact later resolution packet**

The question resolves YES (1).

Key facts:
- On June 29, 2026, the U.S. Supreme Court issued its decision in Trump v. Slaughter (No. 25-332). The official slip opinion (https://www.supremecourt.gov/opinions/25pdf/25-332_qn12.pdf) shows the Court REVERSED the judgment of the U.S. District Court for the District of Columbia and remanded for further proceedings [f1bbb2].
- The Court held, by a 6-3 vote, that the FTC's for-cause removal provision violates the separation of powers, that FTC commissioners are removable at will by the President, and explicitly overruled Humphrey's Executor v. United States ("If anything more is left of Humphrey's, the Court overrules it") [f1bbb2]. SCOTUSblog confirmed the 6-3 vote struck down the law protecting FTC members from removal, effectively permitting Trump to fire Slaughter [57a32f].

Resolution criteria analysis:
1. Timing: The ruling was issued June 29, 2026, which is on or after May 12, 2026 and before the 11:59 PM ET July 1, 2026 deadline. The timing condition is satisfied [f1bbb2, 57a32f].
2. Disposition: The resolution criteria state the question resolves YES if the Supreme Court "reverses or vacates the lower court's judgment in whole or in part — i.e., rules in favor of the petitioner, Donald J. Trump." The Court reversed the lower court's pro-Slaughter judgment and ruled in Trump's favor [f1bbb2, 57a32f]. This satisfies YES.
3. The writ of certiorari was NOT dismissed, and the Court did NOT affirm the lower court — so neither NO condition applies.

Therefore the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-55. `98ece8d0-8ce0-5abf-b6c8-3998a2032060`

- Present date: `2026-05-16 16:30:23.263849`
- Source cutoff boundary: `2026-05-17` (encodes end of UTC day `2026-05-16`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the Supreme Court of India reserve judgment in the 9-judge Sabarimala reference case by July 1, 2026?

**Resolution criteria**

This question resolves YES if the Supreme Court of India's 9-judge Constitution Bench formally reserves judgment in the Sabarimala reference case (Kantaru Rajeevaru v. Indian Young Lawyers Association, arising from Indian Young Lawyers Association v. State of Kerala (2018)) on or before July 1, 2026 (23:59 IST).

"Reserves judgment" means the bench has concluded hearing all oral arguments and submissions and has formally stated that it will pronounce its order/judgment at a later date. This does not require delivery of the final verdict itself.

The verdict must be delivered on or after May 12, 2026 (IST), if it occurs. (Note: reservation of judgment occurring before May 12, 2026 would also count, but as of May 13 arguments are still ongoing, so this is moot.)

Resolution source: Official Supreme Court of India records, or credible legal news reporting from Bar and Bench (https://www.barandbench.com/), LiveLaw (https://www.livelaw.in/), or Supreme Court Observer (https://www.scobserver.in/). The question resolves NO if, as of July 1, 2026, arguments are still ongoing or the case has not yet reached the stage of reservation of judgment.

**Pre-cutoff background**

The Supreme Court of India is hearing a 9-judge Constitution Bench reference arising from the 2018 Sabarimala verdict (Indian Young Lawyers Association v. State of Kerala), which allowed women of all ages to enter the Sabarimala temple. The reference, linked to the case Kantaru Rajeevaru v. Indian Young Lawyers Association, examines broader constitutional questions including the scope of Articles 25 and 26, the "Essential Religious Practices" doctrine, and the interplay between individual religious freedom and denominational rights.

The 9-judge bench, led by CJI Surya Kant, commenced hearings on April 7, 2026. As of May 13, 2026, the bench has completed at least 14 days of oral arguments. Day 13 (May 7, 2026) featured arguments on the Dawoodi Bohra excommunication case and Female Genital Mutilation, with Senior Advocates Raju Ramachandran, Siddharth Luthra, and Jaideep Gupta (for the State of Kerala) presenting submissions [Sabarimala reference hearing: Live updates from Supreme Court](https://www.barandbench.com/news/sabarimala-reference-hearing-live-updates-from-supreme-court-day-13). Day 14 was listed for May 12, 2026. Arguments remain ongoing and have not yet concluded.

Reserving judgment means the bench has heard all oral arguments and submissions and has formally indicated it will deliver its verdict at a later date. For a 9-judge bench dealing with multiple interconnected constitutional questions and numerous interveners, arguments can extend over many weeks. Whether arguments will conclude and judgment will be reserved within the next ~7 weeks is uncertain — the bench could wrap up relatively quickly or hearings could extend well into the summer session.

**Exact later resolution packet**

The question resolves YES. It asked whether the Supreme Court of India's 9-judge Constitution Bench would formally reserve judgment in the Sabarimala reference case (Kantaru Rajeevaru v. Indian Young Lawyers Association, arising from Indian Young Lawyers Association v. State of Kerala (2018)) on or before July 1, 2026 (23:59 IST).

Two of the explicitly permitted resolution sources confirm that the bench formally reserved judgment on May 14, 2026 — well before the July 1, 2026 deadline:

1. LiveLaw ("Sabarimala Reference: Supreme Court 9-Judge Bench Reserves Verdict After 16 Days Hearing", published 14 May 2026, https://www.livelaw.in/top-stories/supreme-court-sabarimala-reference-verdict-reserved-534228) states: "After 16 days hearings, the Supreme Court today reserved its verdict in the Sabarimala reference." [Sabarimala Reference: Supreme Court Reserves Verdict After 16 ...](https://www.livelaw.in/top-stories/supreme-court-sabarimala-reference-verdict-reserved-534228)

2. Supreme Court Observer ("Sabarimala Reference | Day 16: Supreme Court reserves judgement", 14 May 2026, https://www.scobserver.in/reports/sabarimala-reference-day-16/, linked from the case page https://www.scobserver.in/cases/kantaru-rajeevaru-indian-young-lawyers-association-sabrimala-review-background/) states that "The nine-judge bench led by CJI Surya Kant concluded the hearings in the Sabarimala reference today, May 14, 2026. The bench has reserved its judgement." [Sabarimala Review - Supreme Court Observer](https://www.scobserver.in/cases/kantaru-rajeevaru-indian-young-lawyers-association-sabrimala-review-background/)

Both confirm this was a formal reservation of judgment — the bench concluded ALL oral arguments/submissions (after 16 days of hearings) and stated it would pronounce its verdict at a later date — not a mere temporary adjournment or post-vacation listing. The verdict itself need not have been delivered; only the reservation is required, and it occurred on May 14, 2026, which is after May 12, 2026 (satisfying that constraint) and before the July 1, 2026 deadline. The case identity matches exactly (Kantaru Rajeevaru v. Indian Young Lawyers Association, the 9-judge Sabarimala reference before CJI Surya Kant's bench).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-56. `feb4f0f4-e7cb-566d-8b84-2209e960a007`

- Present date: `2026-05-02 10:56:23.684296`
- Source cutoff boundary: `2026-05-03` (encodes end of UTC day `2026-05-02`)
- Expected resolution: `2026-05-10 00:00:00`

**Question**

Will Plaid Cymru win more Senedd seats than Reform UK in the 2026 Welsh Senedd election?

**Resolution criteria**

This question resolves **Yes** if Plaid Cymru wins a strictly greater number of seats than Reform UK in the 2026 Senedd election held on 7 May 2026. It resolves **No** if Reform UK wins more seats than Plaid Cymru, or if both parties win an equal number of seats.

"Seats" refers to the total number of Members of the Senedd (MSs) elected for each party at the conclusion of the official count for the 7 May 2026 Senedd election.

The resolution source is the official Senedd election results as published on the Senedd website (https://senedd.wales/) or as reported by the BBC (https://www.bbc.co.uk/news/topics/c8grx8g8x58t/senedd-election-2026). Results are expected to be finalised by 9 May 2026 (23:59 BST).

**Pre-cutoff background**

The 2026 Senedd election is scheduled for 7 May 2026. It is the first election under a new electoral system: the Senedd has been expanded from 60 to 96 members, all elected via closed party list proportional representation (D'Hondt method) across 16 six-member constituencies [2026 Senedd election - Wikipedia](https://en.wikipedia.org/wiki/2026_Senedd_election).

The race between Plaid Cymru and Reform UK is extremely tight. YouGov's second MRP projection (fieldwork 6–15 April 2026) estimates Reform UK at 37 seats and Plaid Cymru at 36 seats [Second YouGov MRP of the 2026 Senedd elections shows a tight ...](https://yougov.com/en-gb/articles/54597-second-yougov-mrp-of-the-2026-senedd-elections-shows-a-tight-race-between-reform-uk-and-plaid-cymru). However, vote share polls from late April 2026 show mixed results: Survation (17–23 Apr) has Reform 30%, Plaid 28%; Find Out Now (18–22 Apr) has Plaid 29%, Reform 27%; YouGov (6–15 Apr) has both tied at 29% [2026 Senedd election - Wikipedia](https://en.wikipedia.org/wiki/2026_Senedd_election). The polling aggregator at pollcheck.co.uk shows Plaid Cymru at 28% and Reform UK at 27% in vote share.

The new proportional system makes seat allocation highly sensitive to small vote share differences across the 16 constituencies, creating genuine uncertainty about which party will end up with more seats. Labour, the Conservatives, and other parties are expected to win substantially fewer seats than either Plaid Cymru or Reform UK.

**Exact later resolution packet**

The resolution criteria require YES only if Plaid Cymru won a strictly greater number of Members of the Senedd than Reform UK. The BBC's 2026 Welsh Parliament election results page at https://www.bbc.com/news/election/2026/wales/results reports the final results with all 96 of 96 seats declared, so this is a final result rather than a poll, MRP projection, or exit poll [Welsh Parliament election results 2026 - BBC News](https://www.bbc.com/news/election/2026/wales/results). On that final results table, Plaid Cymru is listed with 43 seats and Reform UK with 34 seats [Welsh Parliament election results 2026 - BBC News](https://www.bbc.com/news/election/2026/wales/results). Because 43 is strictly greater than 34, Plaid Cymru won more Senedd seats than Reform UK, and the question resolves YES [Welsh Parliament election results 2026 - BBC News](https://www.bbc.com/news/election/2026/wales/results).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-57. `ce682877-e654-58d7-ad5e-fb4642fe7183`

- Present date: `2026-05-03 02:32:32.525474`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Ford announce a manufacturer-funded BEV rebate or price reduction of $10,000 or more on any U.S. model between May 1 and June 1, 2026?

**Resolution criteria**

This question resolves Yes if Ford Motor Company publicly announces a manufacturer-funded rebate, "customer cash" incentive, or official MSRP price reduction of $10,000 or more (in combined manufacturer-backed incentives on a single transaction) on at least one Battery Electric Vehicle (BEV) model sold in the United States, with the announcement or effective date falling between 00:00 UTC on May 1, 2026 and 23:59 UTC on June 1, 2026.

Key definitions and exclusions:
- "BEV" means a Battery Electric Vehicle powered solely by an electric battery, excluding Plug-in Hybrid Electric Vehicles (PHEVs).
- "Manufacturer-funded" means the incentive is backed by Ford Motor Company at the national or regional level, as distinct from (a) dealer-specific markdowns or local price adjustments not part of a manufacturer-led program, and (b) government-funded tax credits (e.g., any remaining state EV credits). Dealer participation in a manufacturer program still counts as manufacturer-funded.
- "New announcement" means any incentive program or offer that is announced, renewed, or takes effect on or after May 1, 2026 (00:00 UTC). A continuation of an existing April 2026 program into May counts only if it is publicly re-announced or renewed for May with updated terms. A simple expiration date extension with identical terms does not count.
- The $10,000 threshold refers to the maximum combined manufacturer-backed cash incentive available to any eligible buyer on a single vehicle purchase, as reported by the source. Financing rate subsidies (e.g., 0% APR) do not count toward the $10,000 threshold; only direct cash rebates, customer cash, purchase allowances, or MSRP reductions count.

Resolution source: Official Ford press releases, or reporting from reputable automotive outlets such as Automotive News (https://www.autonews.com), Edmunds (https://www.edmunds.com), Kelley Blue Book (https://www.kbb.com), CarsDirect (https://www.carsdirect.com), or Electrek (https://electrek.co).

**Pre-cutoff background**

Since the expiration of the $7,500 federal Clean Vehicle Credit in late 2025, major automakers have increasingly offered manufacturer-funded cash rebates to sustain EV demand. As of April 2026, several automakers are offering aggressive incentives: Hyundai offers up to $10,000 cash on the 2026 IONIQ 5 and IONIQ 9; Kia offers $10,000 customer cash across its EV lineup; GM (Chevrolet) offers up to $10,000 off the 2026 Equinox EV; and Toyota offers up to $6,500 off the 2026 bZ [Unbeatable Deals: 11 EVs Now Offer $10,000+ Cash Rebates](https://www.forbes.com/sites/jimgorzelany/2026/04/13/unbeatable-deals-11-evs-now-offer-10000-cash-rebates/) [These EV deals are hard to pass up with up to $10,000 in discounts](https://electrek.co/2026/04/17/ev-deals-up-to-10000-discounts/). However, Ford's largest publicly reported offer as of mid-April 2026 is up to $8,000 cash on the 2025 F-150 Lightning, below the $10,000 threshold reached by several competitors [Unbeatable Deals: 11 EVs Now Offer $10,000+ Cash Rebates](https://www.forbes.com/sites/jimgorzelany/2026/04/13/unbeatable-deals-11-evs-now-offer-10000-cash-rebates/). Most current April 2026 promotional offers are set to expire on April 30, 2026 [These EV deals are hard to pass up with up to $10,000 in discounts](https://electrek.co/2026/04/17/ev-deals-up-to-10000-discounts/). The competitive pressure from rivals offering five-figure rebates, combined with Ford's need to move EV inventory, creates uncertainty about whether Ford will escalate its own incentives to the $10,000 level in May 2026. A Battery Electric Vehicle (BEV) is defined as a vehicle powered exclusively by an electric battery with no internal combustion engine; this excludes Plug-in Hybrid Electric Vehicles (PHEVs) such as the Ford Escape PHEV.

**Exact later resolution packet**

Adjudicated: Ford launched its May 1, 2026 'Employee Pricing For All' / May incentive program on the 2025 F-150 Lightning (a BEV), with named resolution sources reporting up to $10,000 in combined manufacturer-backed cash incentives: roughly $9,000 Retail Customer Cash plus a $2,000 (or $1,000) 'Alternative Ford Power Promise Bonus Cash' (the direct-cash option for declining the free home charger). RealCarTips lists a '$10,000 Max Rebate' for most Lightning trims in the cash-rebate column, separate from and independent of the 0% APR financing offer, and CarsDirect (a named source) reports '$10,000 off MSRP in stackable incentives' through July 6. Because both components are direct cash rebates (not financing-rate subsidies, which the criteria exclude) and the criteria explicitly count combined manufacturer-backed incentives on a single transaction, the $10,000 threshold is met within the May 1-June 1 window. An earlier automated pass stopped at the $9,000 Retail Customer Cash figure and mis-treated the path to $10,000 as financing-tied, but the additional $2,000 Power Promise opt-out is direct cash.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-58. `57a9e6a8-7280-58d5-9d37-1cd2c7641764`

- Present date: `2026-05-14 10:21:30.576079`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the 10-Year Health Plan Bill include provisions to abolish Healthwatch England and local Healthwatch organizations?

**Resolution criteria**

This question resolves based on the text of the 10-Year Health Plan Bill (or equivalent primary legislation introduced to implement the government's 10-Year Health Plan), as published on the official UK Parliament bills website at [https://bills.parliament.uk/](https://bills.parliament.uk/).

**Resolves YES** if the "Bill as Introduced" version (in either the House of Commons or the House of Lords), published on or after 12 May 2026, contains explicit provisions to abolish Healthwatch England and/or local Healthwatch organizations. "Abolishing" means the bill includes language that:
- repeals or amends the relevant sections of the [Health and Social Care Act 2012](https://www.legislation.gov.uk/ukpga/2012/7/contents) (particularly sections 181–182 establishing Healthwatch England and sections 221–227 establishing local Healthwatch), OR
- explicitly dissolves, winds up, or otherwise terminates these bodies.

**Resolves NO** if:
1. The bill is introduced and published on [bills.parliament.uk](https://bills.parliament.uk/) on or after 12 May 2026 but does not contain such provisions; OR
2. No bill substantively implementing the government's 10-Year Health Plan is introduced to Parliament and published on [bills.parliament.uk](https://bills.parliament.uk/) by 1 July 2026 (23:59 UTC).

The version used for resolution is the "Bill as Introduced" text — i.e., the first version published when the bill is formally introduced to either House. If the bill was introduced before 12 May 2026, the most recent version of the bill text available on bills.parliament.uk as of 1 July 2026 (23:59 UTC) will be used instead.

Resolution source: [https://bills.parliament.uk/](https://bills.parliament.uk/)

**Pre-cutoff background**

The UK government has announced its intention to abolish Healthwatch England and local Healthwatch organizations as part of its 10-Year Health Plan for England [King's Speech 2026: Health - House of Lords Library - UK Parliament](https://lordslibrary.parliament.uk/research-briefings/lln-2026-0016/). Healthwatch England is an independent statutory body established under the [Health and Social Care Act 2012](https://www.legislation.gov.uk/ukpga/2012/7/contents) (sections 181–182), serving as the national consumer champion for health and social care. Local Healthwatch organizations (over 150 across England) were also established under the same Act (sections 221–227), providing local-level patient and public voice functions.

As confirmed in a written parliamentary answer by Baroness Merron on 23 February 2026 (UIN HL14379), the government plans to transfer Healthwatch England's strategic functions to a new "Patient Experience Directorate" within the Department of Health and Social Care, while local health functions would transfer to Integrated Care Boards (ICBs) and social care functions to local authorities [Health Services and Social Services: Patients](https://questions-statements.parliament.uk/written-questions/detail/2026-02-06/HL14379/). The government stated that "the abolition of both Healthwatch England and Local Healthwatch will require primary legislation and will be subject to the will of Parliament" [Health Services and Social Services: Patients](https://questions-statements.parliament.uk/written-questions/detail/2026-02-06/HL14379/).

The [House of Lords Library briefing on the King's Speech 2026](https://lordslibrary.parliament.uk/research-briefings/lln-2026-0016/) confirms that the 10-Year Health Plan Bill is expected to include provisions abolishing Healthwatch [King's Speech 2026: Health - House of Lords Library - UK Parliament](https://lordslibrary.parliament.uk/research-briefings/lln-2026-0016/). Blog reports suggest the bill was expected to be introduced around April 2026. However, as of May 2026, the bill does not yet appear on the Parliament bills tracker. There is genuine uncertainty about whether these specific Healthwatch abolition provisions will be included in the bill as introduced, or whether they could be deferred to secondary legislation or dropped due to political pushback.

**Exact later resolution packet**

RESOLUTION: YES (1).

**The bill and its timing (antecedent condition satisfied):** The government's primary legislative vehicle for implementing its 10-Year Health Plan for England — the "Health Bill" (Bill 009 of the 2026-27 session, Parliament bill ID 4124) — was introduced to the House of Commons and published on **14 May 2026**, i.e. on or after the 12 May 2026 cut-off specified in the resolution criteria. It is tracked at https://bills.parliament.uk/bills/4124, and the "Bill as Introduced" text (the version the criteria require) is available at https://bills.parliament.uk/bills/4124/publications with the official text PDF at https://publications.parliament.uk/pa/bills/cbill/59-02/0009/260009.pdf [688f53]. Because a bill substantively implementing the 10-Year Health Plan was published on the tracker before the 1 July 2026 23:59 UTC deadline, the NO-by-default conditions (no bill published) do not apply.

**Explicit Healthwatch abolition provisions (consequent satisfied):** A direct reading of the "Bill as Introduced" text confirms explicit abolition provisions:
- **Clause 64 (Abolition of Healthwatch England):** "(1) The Healthwatch England committee is abolished. (2) Schedule 9 contains consequential amendments." [3c813c]
- **Clause 65 (Abolition of arrangements with Local Healthwatch organisations):** introduces Schedule 10, which removes the obligation on local authorities to make arrangements for Local Healthwatch organisations and transfers corresponding functions to local authorities and ICBs. [3c813c]

**Explicit check for repeal/amendment of the relevant statutory sections:**
- Healthwatch England: Schedule 9 omits the operative Healthwatch England committee provisions (sections 45A–45C, which were inserted into the Health and Social Care Act 2008 by section 181 of the Health and Social Care Act 2012), thereby terminating Healthwatch England. [3c813c]
- Local Healthwatch: Schedule 10 omits sections 221–227 (Local Healthwatch organisations, local-authority arrangements, duties of responsible persons/service-providers, referrals and annual reports) [3c813c]. The explanatory notes further confirm Schedule 10 omits sections 224–227 (Local Government and Public Involvement in Health Act 2007), section 45D of the Health and Social Care Act 2008 (Healthwatch trademark licence), and section 188 of the Health and Social Care Act 2012 (transitional Local Healthwatch arrangements). [6da2c4]

The explanatory notes independently confirm Clause 64 abolishes Healthwatch England (functions transferring to the Secretary of State) and Clause 65 abolishes local Healthwatch arrangements (functions transferring to ICBs and local authorities) [6da2c4]. The Nuffield Trust briefing likewise confirms Clauses 64 and 65 abolish Healthwatch England and local Healthwatch [16baa1], as do the House of Commons Library briefing and numerous secondary sources.

**Both prongs of the "Abolishing" test are met:** the bill (a) repeals/amends the relevant statutory sections establishing Healthwatch England and local Healthwatch, AND (b) explicitly dissolves/terminates these bodies. Therefore the question resolves YES.

Direct URL to the specific bill text on the Parliament bills tracker: https://bills.parliament.uk/bills/4124 (Bill as Introduced text: https://publications.parliament.uk/pa/bills/cbill/59-02/0009/260009.pdf).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-59. `4a8ffec1-c6cf-580d-a225-e0df60cd1bba`

- Present date: `2026-05-03 10:59:57.658949`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will the EU institutions reach a trilogue political agreement on the Digital Omnibus on AI (2025/0359(COD)) between April 30 and June 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if a trilogue political agreement on the Digital Omnibus on AI (procedure 2025/0359(COD)) is reached between the European Parliament and the Council of the EU between April 30, 2026, and 23:59 UTC on June 1, 2026.

A "trilogue political agreement" is defined as an informal provisional agreement (also known as a "political deal") reached between the co-legislators during interinstitutional (trilogue) negotiations, as formally announced by either institution. This does not require formal adoption or signature — an announced provisional agreement suffices.

Resolution will be determined by an official announcement from at least one of the following sources:
- The European Parliament Newsroom (https://www.europarl.europa.eu/news/en)
- The Council of the EU press releases (https://www.consilium.europa.eu/en/press/)

If no such announcement confirming a provisional political agreement appears by 23:59 UTC on June 1, 2026, the question resolves as **No**.

**Pre-cutoff background**

The Digital Omnibus on AI (legislative procedure 2025/0359(COD), COM(2025) 836 final) is a European Commission proposal published on 19 November 2025 to simplify implementation of the EU AI Act (Regulation 2024/1689) [Digital Omnibus on AI [EU Legislation in Progress] | Epthinktank](https://epthinktank.eu/2026/02/12/digital-omnibus-on-ai-eu-legislation-in-progress/). Among its key provisions, it proposes delaying Annex III high-risk AI system obligations from the current August 2, 2026 deadline to as late as December 2027 for stand-alone systems and August 2028 for those embedded in regulated products [EU and Parliament fail to agree on AI Act changes after 12 hours of ...](https://thenextweb.com/news/eu-ai-act-omnibus-deal-fails-april-2026-talks).

The Council adopted its negotiating mandate on March 13, 2026, and the Parliament's IMCO/LIBE committees adopted a joint report on March 18, 2026 [Digital Omnibus on AI [EU Legislation in Progress] | Epthinktank](https://epthinktank.eu/2026/02/12/digital-omnibus-on-ai-eu-legislation-in-progress/). On April 28, 2026, the second political trilogue ended without agreement after approximately 12 hours of negotiations [EU countries, lawmakers fail to reach deal on watered-down AI rules](https://www.reuters.com/sustainability/boards-policy-regulation/eu-countries-lawmakers-fail-reach-deal-watered-down-ai-rules-2026-04-29/). The primary point of contention was whether high-risk AI systems embedded in products already regulated under EU product safety legislation (e.g., medical devices, toys, connected cars, industrial machinery) should be exempt from the AI Act's additional requirements. The European Parliament pushed for these systems to be covered exclusively by existing sectoral rules, while the Council showed limited enthusiasm for such a broad carve-out [EU and Parliament fail to agree on AI Act changes after 12 hours of ...](https://thenextweb.com/news/eu-ai-act-omnibus-deal-fails-april-2026-talks). Some countries and lawmakers also insisted that industries already subject to sectoral regulations should be fully exempted from the AI legislation [EU countries, lawmakers fail to reach deal on watered-down AI rules](https://www.reuters.com/sustainability/boards-policy-regulation/eu-countries-lawmakers-fail-reach-deal-watered-down-ai-rules-2026-04-29/).

Talks are expected to resume in approximately two weeks (mid-May 2026) [EU countries, lawmakers fail to reach deal on watered-down AI rules](https://www.reuters.com/sustainability/boards-policy-regulation/eu-countries-lawmakers-fail-reach-deal-watered-down-ai-rules-2026-04-29/). The looming August 2, 2026 compliance deadline creates strong pressure to reach a deal, but substantive disagreements remain, making the outcome genuinely uncertain.

**Exact later resolution packet**

The question resolves YES. The European Parliament and the Council of the EU reached a provisional political agreement (trilogue "political deal") on the Digital Omnibus on AI (legislative procedure 2025/0359(COD)) in the early hours of Thursday, 7 May 2026 [Digital Omnibus on AI Provisional Agreement Reached at the May ...](https://www.twobirds.com/en/insights/2026/digital-omnibus-on-ai-provisional-agreement-reached-at-the-may-trilogue). This date falls squarely within the resolution window of April 30, 2026 to 23:59 UTC on June 1, 2026.

The agreement is confirmed by an official Council of the EU press release titled "Artificial Intelligence: Council and Parliament agree to simplify and streamline rules" (https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/), dated 7 May 2026, satisfying the requirement that resolution be based on an official announcement from either the European Parliament Newsroom or the Council of the EU press releases.

The agreement is a "political agreement" / provisional deal (not merely a committee vote or single-institution mandate): it was reached between the co-legislators during the trilogue negotiation that followed the failed 28 April 2026 trilogue and a subsequent trilogue. Numerous independent legal sources confirm this characterization, e.g. Bird & Bird explicitly states "In the early hours of Thursday 7 May 2026, Council and Parliament negotiators reached a provisional agreement on the Digital Omnibus on AI" [Digital Omnibus on AI Provisional Agreement Reached at the May ...](https://www.twobirds.com/en/insights/2026/digital-omnibus-on-ai-provisional-agreement-reached-at-the-may-trilogue). The provisional agreement still requires formal adoption by both institutions, but the resolution criteria explicitly state formal adoption is not required — an announced provisional agreement suffices.

Therefore the antecedent condition (a trilogue political agreement reached in the window) was met, and the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-60. `c7d710c4-6438-535f-ab24-3a764cd42ac6`

- Present date: `2026-05-29 02:11:20.069473`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will the European Commission announce the release of any portion of frozen EU funds to Hungary between May 12, 2026, and July 1, 2026?

**Resolution criteria**

This question resolves as **Yes** if, between May 12, 2026 (00:00 UTC) and July 1, 2026 (23:59 UTC), the European Commission publishes an official announcement confirming the release, disbursement, or formal unblocking of any portion of previously frozen EU funds to Hungary. This includes:

- The formal lifting of measures under the **Rule of Law Conditionality Regulation** (Regulation (EU, Euratom) 2020/2092), resulting in the unblocking of any funding envelope;
- The approval of a payment request or disbursement of any tranche under Hungary's **Recovery and Resilience Facility (RRF)** plan;
- The lifting of suspensions related to **horizontal enabling conditions** under Cohesion Policy funds;
- The release of funds for specific projects counts, as does partial disbursement of tranches or the formal unblocking of a funding envelope.

The announcement must appear on the **European Commission Press Corner** (https://ec.europa.eu/commission/presscorner/home/en) or be confirmed via an official European Commission decision published in the Official Journal of the EU. Statements by individual Commissioners in interviews or social media posts do not qualify unless accompanied by a formal press release or decision.

This question resolves as **No** if no such official announcement is published by 23:59 UTC on July 1, 2026.

**Pre-cutoff background**

As of May 12, 2026, the European Commission has frozen approximately €17 billion of the €27 billion in EU funds originally earmarked for Hungary, due to rule-of-law and corruption concerns under the previous Orbán government [EU and Magyar agreed to work together for EU cash after talks](https://www.euronews.com/my-europe/2026/04/19/eu-and-hungarys-magyar-agreed-to-work-together-for-release-of-eu-cash-after-weekend-talks). The total frozen amount across all mechanisms exceeds €30 billion [Commission delegation heads to Budapest to negotiate release of ...](https://www.politico.eu/article/commission-heads-hungary-budapest-friday-eu-funds-negotiations/). The most urgent tranche is approximately €10.4 billion from the Recovery and Resilience Facility (RRF), which faces an end-of-August 2026 expiration deadline—if not drawn by then, these funds will be irrevocably lost [Hungary and EU to discuss terms of release for billions in ... - Reuters](https://www.reuters.com/world/hungary-eu-discuss-terms-release-billions-blocked-funds-2026-04-27/)[EU and Magyar agreed to work together for EU cash after talks](https://www.euronews.com/my-europe/2026/04/19/eu-and-hungarys-magyar-agreed-to-work-together-for-release-of-eu-cash-after-weekend-talks). Additional funds are frozen under the EU's Cohesion Policy and the Rule of Law Conditionality Regulation (Regulation 2020/2092).

Following the landslide election victory of Péter Magyar's Tisza Party in April 2026, the European Commission initiated negotiations with the incoming government. Commission officials traveled to Budapest in mid-April to begin discussions on the 27 conditions Brussels expects the new government to meet [Commission delegation heads to Budapest to negotiate release of ...](https://www.politico.eu/article/commission-heads-hungary-budapest-friday-eu-funds-negotiations/). The new government holds a two-thirds parliamentary majority, enabling it to pass constitutional and legislative reforms [Hungary and EU to discuss terms of release for billions in ... - Reuters](https://www.reuters.com/world/hungary-eu-discuss-terms-release-billions-blocked-funds-2026-04-27/). However, multiple observers have noted the tight timeline, as substantial legislative changes—including reversing anti-LGBTQ+ laws struck down by the CJEU and restoring judicial independence—must be enacted before funds can be released. Hungary's participation in the Erasmus programme (suspended since early 2023) is also part of the broader negotiations [Hungary and EU to discuss terms of release for billions in ... - Reuters](https://www.reuters.com/world/hungary-eu-discuss-terms-release-billions-blocked-funds-2026-04-27/).

**Exact later resolution packet**

RESOLUTION: YES (1).

WHAT HAPPENED: On 29 May 2026 — inside the resolution window (12 May 2026 00:00 UTC – 1 July 2026 23:59 UTC) — European Commission President Ursula von der Leyen, meeting Hungarian PM Péter Magyar, announced the unlocking of €16.4 billion of previously frozen EU funds. This is documented directly on the required resolution source, the European Commission Press Corner: "Statement by the President with Hungarian Prime Minister Magyar," https://ec.europa.eu/commission/presscorner/detail/en/statement_26_1200 .

KEY PRIMARY-SOURCE QUOTES (from that EC Press Corner statement): 
- RRF: "…subject to the reforms that are being adopted and investments implemented, I am very happy to announce today that we can unlock EUR 10 billion for Hungary." 
- Cohesion: "With the progress on the super milestones, we have also been able to unlock the conditionality-related Cohesion funds worth EUR 4.2 billion." [https://ec.europa.eu/commission/presscorner/detail/en/statement_26_1200](https://ec.europa.eu/commission/presscorner/detail/en/statement_26_1200) [https://ec.europa.eu/commission/presscorner/detail/en/statement_26_1200](https://ec.europa.eu/commission/presscorner/detail/en/statement_26_1200)

WHY THIS RESOLVES YES: The resolution criteria explicitly list, as qualifying events, "the formal unblocking of a funding envelope," "the lifting of suspensions related to horizontal enabling conditions under Cohesion Policy funds," and "the formal lifting of measures under the Rule of Law Conditionality Regulation… resulting in the unblocking of any funding envelope." The Commission's own Press Corner statement announces, in the past tense, that it has been able to unlock the conditionality-related Cohesion envelope worth €4.2 billion for Hungary — i.e., a formal unblocking of a funding envelope, not merely intent. The required source (EC Press Corner) and the date window are both satisfied. The criteria require only "any portion," and disbursement is NOT required (unblocking suffices). [https://ec.europa.eu/commission/presscorner/detail/en/statement_26_1200](https://ec.europa.eu/commission/presscorner/detail/en/statement_26_1200) [https://ec.europa.eu/commission/presscorner/detail/en/statement_26_1200](https://ec.europa.eu/commission/presscorner/detail/en/statement_26_1200)

CORROBORATION FROM REPUTABLE OUTLETS (May 29, 2026): AP ("European Union unlocks billions in funding for Hungary… €10bn recovery + cohesion funds") [EU unlocks 16.4 billion euros for Hungary after rapid reforms by ...](https://apnews.com/article/hungary-magyar-eu-funds-8e560d62f308b004f104d6f5b3a15353); Reuters ("EU Commission agrees to unlock €16.4 billion for Hungary"; €10bn Next Generation EU, €4.2bn cohesion conditionality, €2.2bn as reforms are completed) [EU Commission agrees to unlock €16.4 billion for Hungary | Reuters](https://www.reuters.com/business/eu-agrees-unlock-billions-funds-hungary-von-der-leyen-2026-05-29/) [EU Commission agrees to unlock €16.4 billion for Hungary](https://www.reuters.com/business/eu-agrees-unlock-billions-funds-hungary-von-der-leyen-2026-05-29/); Al Jazeera ("EU… will unlock 16.4 billion euros for Hungary") [EU to release billions in frozen funds for Hungary amid ...](https://www.aljazeera.com/news/2026/5/29/eu-to-release-billions-in-frozen-funds-for-hungary-amid-magyar-reforms); European Policy Centre notes the Commission would "unfreeze €6.6 billion of Hungary's cohesion funding" [Hungary gets EU cash – where are the safeguards?](https://www.epc.eu/publication/hungary-gets-eu-cash-where-are-the-safeguards/).

ADDRESSING THE STRONGEST NO ARGUMENT: A DW report (30 May 2026) quotes a senior EU official saying, "We haven't agreed on disbursal… We have agreed on the conditions that need to be met" [What Hungary must do to receive EU funds frozen under Orban](https://www.dw.com/en/what-hungary-must-do-to-receive-eu-funds-frozen-under-orban/a-77354206), and a 10 June Euronews piece frames the process as still procedural, with Hungary having just submitted a revised Recovery Plan and Council approval expected in July [Hungary submits revised EU recovery plan as MEPs demand ...](https://www.euronews.com/my-europe/2026/06/10/hungary-submits-revised-eu-recovery-plan-as-meps-demand-transparency-over-164bn-in-frozen-). However, these caveats concern actual DISBURSAL of the €10bn RRF tranche (which the criteria explicitly distinguish from "formal unblocking"). They do not negate the Commission's own past-tense announcement that the €4.2bn Cohesion (conditionality) envelope had been unlocked. Because the criteria count a "formal unblocking of a funding envelope," and the Commission announced exactly that on its Press Corner within the window, the question resolves YES.

PRIMARY EVIDENCE URL: https://ec.europa.eu/commission/presscorner/detail/en/statement_26_1200 (EC Press Corner, 29 May 2026).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-61. `d4d411cb-a4db-579d-a8fe-296305fd4683`

- Present date: `2026-05-29 03:51:48.768169`
- Source cutoff boundary: `2026-05-30` (encodes end of UTC day `2026-05-29`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Zsolt Hernádi remain as Chairman-CEO of MOL Group on July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if Zsolt Hernádi holds the position of Chairman-CEO (or equivalent combined Chairman and Chief Executive Officer role) of MOL Group at the end of the day on July 1, 2026 (23:59 UTC).

This question resolves **No** if, by that time, Hernádi has resigned, been removed, or otherwise vacated the Chairman-CEO position.

**If the role is split:** If the combined "Chairman-CEO" role is split into separate "Chairman" and "CEO" positions, or renamed, the question resolves **Yes** only if Hernádi holds at least one of these successor roles (Chairman of the Board or CEO) at the end of the day on July 1, 2026 (23:59 UTC). If he holds neither, it resolves **No**.

**Resolution source:** The primary resolution source is the [MOL Group Board of Directors page](https://molgroup.info/en/about-mol-group/board-of-directors). If the website is unavailable or ambiguous, credible reporting from major international news outlets (e.g., [Reuters](https://www.reuters.com), [Bloomberg](https://www.bloomberg.com), [Financial Times](https://www.ft.com)) may be used as an alternative source.

**Key definitions:**
- "MOL Group" refers to MOL Hungarian Oil and Gas Plc (MOL Nyrt.), the integrated oil and gas company listed on the Budapest Stock Exchange ([MOL Group official site](https://molgroup.info/)).
- "Chairman-CEO" refers to the combined role of Chairman of the Board of Directors and Chief Executive Officer as defined by MOL Group's corporate governance structure ([MOL Board of Directors page](https://molgroup.info/en/about-mol-group/board-of-directors)).

**Pre-cutoff background**

Zsolt Hernádi has served as Chairman & Chief Executive Officer (Chairman-CEO) of [MOL Group](https://molgroup.info/en/about-mol-group/board-of-directors), Hungary's largest oil and gas company, since June 2001 [Hungary's Magyar agrees with MOL chief Hernadi to maintain fuel ...](https://www.reuters.com/business/energy/hungarys-magyar-meet-mol-chief-hernadi-discuss-security-fuel-supply-2026-04-16/). MOL Group is a publicly traded integrated oil and gas company headquartered in Budapest, Hungary. The "Chairman-CEO" role combines the positions of Chairman of the Board of Directors and Chief Executive Officer into a single executive function ([MOL Board of Directors page](https://molgroup.info/en/about-mol-group/board-of-directors)).

As of May 12, 2026, Hernádi continues to hold the position of Chairman-CEO of MOL Group, as confirmed by MOL's official corporate governance pages and recent news reporting.

**Recent political developments:** In April 2026, Peter Magyar's Tisza Party won a landslide victory in Hungary's parliamentary elections, ending Viktor Orbán's 16-year rule. On April 16, 2026, Magyar met with Hernádi to discuss fuel policy and dividend payments [Hungary's Magyar agrees with MOL chief Hernadi to maintain fuel ...](https://www.reuters.com/business/energy/hungarys-magyar-meet-mol-chief-hernadi-discuss-security-fuel-supply-2026-04-16/). Key outcomes of that meeting included:
- An agreement to maintain the existing fuel price cap on petrol and diesel implemented by the outgoing government.
- Magyar expressed his expectation that MOL should not pay a record dividend to the Mathias Corvinus Collegium (MCC), an educational institution linked to Orbán. Hernádi indicated that "MOL would act in compliance with relevant legislation" [Hungary's Magyar agrees with MOL chief Hernadi to maintain fuel ...](https://www.reuters.com/business/energy/hungarys-magyar-meet-mol-chief-hernadi-discuss-security-fuel-supply-2026-04-16/).
- According to reporting, Hernádi also agreed to travel to Russia to discuss continuation of oil supply via the Druzhba pipeline.

**Croatian bribery conviction:** In March 2026, a Hungarian court rejected a Croatian verdict convicting Hernádi of bribery, with MOL hailing the decision. However, the matter remains pending at the European Court of Human Rights.

The political transition creates genuine uncertainty about Hernádi's tenure. While corporate leadership changes at major companies typically take time, the new government's stance toward Orbán-era corporate leadership at strategically important state-linked companies could accelerate such a change.

**Exact later resolution packet**

The question resolves YES. Zsolt Hernádi held the combined Chairman-CEO position of MOL Group (MOL Hungarian Oil and Gas Plc / MOL Nyrt.) at the end of the day on July 1, 2026.

Primary resolution source: The official MOL Group Board of Directors page (https://molgroup.info/en/about-mol-group/board-of-directors) explicitly lists Zsolt Hernádi as "Chairman of the Board of Directors since 7 July 2000" and "Chairman & Chief Executive Officer since 11 June 2001," with no successor or change indicated [Board of Directors - About MOL Group](https://molgroup.info/en/about-mol-group/board-of-directors). This is the primary source specified in the resolution criteria.

Corroborating recent evidence (all after the question's May 13, 2026 creation date and immediately before the July 1, 2026 resolution date):
- A MOL notification to the Budapest Stock Exchange dated June 16, 2026, about the MOL–Serbia NIS Shareholders' Agreement, quotes and identifies him as "Zsolt Hernádi, Chairman and CEO of MOL Group" [[PDF] Budapest, 16 June 2026 MOL and the Serbian government signed a ...](https://www.bse.hu/newkibdata/129484082/MOL_NIS%20SHA_20260616_eng.pdf). This is dated just 15 days before the resolution date and is the most recent primary confirmation found.
- MOL's official investor news dated June 6, 2026 quotes "Zsolt Hernádi, Chairman and CEO of MOL Group" regarding NIS negotiations (molgroup.info investor news).
- Reuters (May 22, 2026) refers to "Zsolt Hernadi, Chairman and CEO of MOL Group" (reuters.com/business/energy/mol-receives-us-approval-continue-talks-about-nis-acquisition-until-june-6-2026-05-22).

No evidence was found of any resignation, removal, or vacating of the position, nor of the role being split or renamed, before July 1, 2026. The 2026 AGM documents reference Zsolt Hernádi continuing in a governing role. Since he continues to hold the combined Chairman & CEO role, the "if the role is split" clause does not apply; and even if it did, he would still hold both successor roles.

Therefore the question resolves YES (1).

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-62. `36131e10-7ef6-5bc8-9f5e-8322fe8a91db`

- Present date: `2026-05-14 07:41:10.386048`
- Source cutoff boundary: `2026-05-15` (encodes end of UTC day `2026-05-14`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will a tentative agreement between the University of California and AFSCME Local 3299 be announced between May 12, 2026, and July 1, 2026?

**Resolution criteria**

This question resolves **Yes** if, between May 12, 2026, and 23:59 UTC on July 1, 2026, the University of California and AFSCME Local 3299 publicly announce a **tentative agreement** (TA) on a new collective bargaining contract.

A "tentative agreement" is defined as a deal reached by the bargaining teams of both parties that is subject to ratification by the union membership. The announcement must come from an official source: the [UC Press Room](https://www.universityofcalifornia.edu/press-room), the [AFSCME Local 3299 website](https://afscme3299.org/), or credible major news reporting (e.g., Reuters, AP, Los Angeles Times).

**Important clarifications:**
- A suspension or ending of the strike without a formal tentative agreement on a new contract does **not** count as a "Yes" resolution. Only a formally announced TA qualifies.
- Ratification by union members is not required; the question resolves Yes upon announcement of the TA by the bargaining teams.
- If no TA is announced by 23:59 UTC on July 1, 2026, the question resolves **No**.

**Pre-cutoff background**

The University of California (UC) and AFSCME Local 3299, the UC's largest employee union representing service workers (SX) and patient care technical workers (EX), have been in contract negotiations since January 2024. As of May 11, 2026, the parties have reached tentative agreements on approximately three-quarters of the contract's major articles, but significant disagreements remain on wages, benefits, and some workplace matters [https://www.universityofcalifornia.edu/press-room/uc-expands-economic-proposal-afscme-declines-offer-ahead-planned-may-14-strike](https://www.universityofcalifornia.edu/press-room/uc-expands-economic-proposal-afscme-declines-offer-ahead-planned-may-14-strike).

UC's latest economic proposal, announced May 11, 2026, offers many career employees up to 34% total pay growth over the life of the contract, including across-the-board wage increases, annual step increases, a ratification bonus of up to $2,000, restructuring of pay scales for those earning below $25/hour, and medical plan premium savings of up to $3,000 annually. AFSCME declined this offer [https://www.universityofcalifornia.edu/press-room/uc-expands-economic-proposal-afscme-declines-offer-ahead-planned-may-14-strike](https://www.universityofcalifornia.edu/press-room/uc-expands-economic-proposal-afscme-declines-offer-ahead-planned-may-14-strike).

AFSCME 3299 has announced an open-ended systemwide unfair labor practice (ULP) strike beginning May 14, 2026, citing alleged bad-faith bargaining by UC. The parties were scheduled to reconvene for bargaining on May 12–13, 2026 [https://www.universityofcalifornia.edu/press-room/uc-expands-economic-proposal-afscme-declines-offer-ahead-planned-may-14-strike](https://www.universityofcalifornia.edu/press-room/uc-expands-economic-proposal-afscme-declines-offer-ahead-planned-may-14-strike). The union has filed multiple unfair labor practice charges against UC.

**Exact later resolution packet**

The question resolves YES. A tentative agreement (TA) on a new collective bargaining contract between the University of California and AFSCME Local 3299 was publicly announced within the resolution window (May 12, 2026 – 23:59 UTC July 1, 2026), confirmed by all three categories of official sources named in the criteria:

1. **UC Press Room** — Published a release ("UC and AFSCME Reach Tentative Contract Deal; Strike Averted") stating: "The University of California and the American Federation of State, County and Municipal Employees union reached a tentative contract agreement early Thursday morning, shortly after a systemwide open-ended strike was scheduled to begin." Dated May 14, 2026. URL: https://www.universityofcalifornia.edu/press-room/labor-negotiations (and the linked release https://www.universityofcalifornia.edu/press-room/uc-and-afscme-reach-tentative-contract-deal-strike-averted) [1cb4db].

2. **AFSCME Local 3299 website** — Official press release ("University of California workers CANCEL Strike after Tentative Agreement Reached," dated May 13, 2026) states the open-ended May 14 strike was cancelled after the union "reached a tentative agreement with University negotiators," that "the agreement was reached late tonight, and union members will vote on ratification May 19th-21st." URL: https://afscme3299.org/media/alert-university-of-california-workers-cancel-strike-after-tentative-agreement-reached/ [64da30].

3. **Los Angeles Times** — Reported (May 14, 2026): "40,000 unionized University of California workers averted a strike Thursday after reaching an early morning tentative deal with the University of California," noting "Members are scheduled to vote on it May 19 through 21." URL: https://www.latimes.com/california/story/2026-05-14/uc-strike-averted-afscme-3299-tentative-agreement [e34020].

**Meets all resolution requirements:**
- Timing: Announced late May 13 / early May 14, 2026 — strictly within the May 12 – July 1, 2026 window.
- Nature: A full tentative agreement on a NEW collective bargaining contract (not merely a strike suspension). UC's release explicitly calls it a "tentative contract agreement," and AFSCME's release calls it a "Historic Tentative Contract Agreement."
- Subject to ratification: All three sources confirm the deal is subject to ratification by union membership, with a member ratification vote scheduled May 19–21, 2026, satisfying the criteria's definition of a "tentative agreement." (Members subsequently ratified it; per Daily Bruin reporting on May 22, 2026, employees voted to ratify — but ratification was not required for YES resolution.)

The definition's requirement that the TA be "subject to ratification by the union membership" is explicitly satisfied per the AFSCME and LA Times sources referencing the May 19–21 ratification vote.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-63. `d0e0612d-94c1-533b-b858-0a2324b2d216`

- Present date: `2026-05-12 21:07:45.823745`
- Source cutoff boundary: `2026-05-13` (encodes end of UTC day `2026-05-12`)
- Expected resolution: `2026-07-01T00:00:00`

**Question**

Will Amanda Gonzalez win the Colorado Democratic primary for Secretary of State on June 30, 2026?

**Resolution criteria**

This question resolves **Yes** if Amanda Gonzalez receives more votes than Jessie Danielson (or any other candidate) in the Colorado Democratic primary election for Secretary of State held on June 30, 2026. It resolves **No** if she does not receive the most votes.

**Resolution source:** The official results published by the Colorado Secretary of State at https://www.coloradosos.gov/ or, if official certification is not yet available, based on the race being called by the Associated Press (AP).

**Timezone:** All dates refer to Mountain Daylight Time (MDT, UTC-6). The primary election is June 30, 2026 MDT.

**If results are not certified by July 1, 2026 (11:59 PM MDT):** The question resolves based on the AP's called winner. If the AP has not called the race by that date, the question resolves based on preliminary official vote totals published by the Colorado Secretary of State. If neither source is available by July 1, 2026, resolution is postponed until official results are available, but no later than August 1, 2026.

**Edge cases:** If Amanda Gonzalez withdraws or is disqualified before election day, the question resolves **No**. If the primary is canceled (e.g., only one candidate remains), and Gonzalez is the remaining candidate, the question resolves **Yes**; if she is not, it resolves **No**.

**Pre-cutoff background**

The 2026 Colorado Democratic primary for Secretary of State is a two-candidate race scheduled for June 30, 2026. The two candidates are:

- **Amanda Gonzalez**: Currently serving as Jefferson County Clerk & Recorder, where she oversees elections, motor vehicle services, and public records. She is an attorney and former Executive Director of Colorado Common Cause. She is the first Latina and first openly LGBTQ person to serve as Jefferson County Clerk. Her background centers on election administration, including implementing jail-based voting and automatic voter registration [Colorado Secretary of State election, 2026 (June 30 Democratic ...](https://ballotpedia.org/Colorado_Secretary_of_State_election,_2026_(June_30_Democratic_primary)).

- **Jessie Danielson**: Currently serving as State Senator for District 22 (Jefferson County) since 2018. She previously served in the Colorado State House from 2015 to 2019 as Speaker Pro Tem. Her professional background includes serving as Colorado State Director for America Votes and Political Director for NARAL Pro-Choice Colorado. Her policy focus includes economic security, voter access, and reproductive rights [Colorado Secretary of State election, 2026 (June 30 Democratic ...](https://ballotpedia.org/Colorado_Secretary_of_State_election,_2026_(June_30_Democratic_primary)).

This is a competitive primary with no clear frontrunner. Gonzalez brings direct election administration experience, while Danielson brings legislative credentials and statewide political networks. Both candidates qualified for the ballot through the party assembly and petition process.

**Sources:**
- Ballotpedia: [Colorado Secretary of State election, 2026 (June 30 Democratic primary)](https://ballotpedia.org/Colorado_Secretary_of_State_election,_2026_(June_30_Democratic_primary))
- Ballotpedia candidate profiles: [Amanda Gonzalez](https://ballotpedia.org/Amanda_Gonzalez_(Colorado)) | [Jessie Danielson](https://ballotpedia.org/Jessie_Danielson)
- Colorado Secretary of State official candidate list: https://www.coloradosos.gov/pubs/elections/vote/primaryCandidates.html

**Exact later resolution packet**

The question resolves YES because Amanda Gonzalez won the Colorado Democratic primary for Secretary of State held on June 30, 2026, receiving more votes than Jessie Danielson (the only other candidate).

Key evidence:
- The Associated Press called the race for Gonzalez at 7:25 p.m. MDT on June 30, 2026. At the time of the call, Gonzalez led state Senator Jessie Danielson by 25.8 percentage points [Amanda Gonzalez wins Democratic primary for secretary of state](https://coloradosun.com/2026/06/30/colorado-primary-election-secretary-of-state-results/). The resolution criteria explicitly permit resolution based on the AP's called winner, so the AP call is authoritative here.
- Colorado Public Radio (CPR) independently confirmed the AP call at 7:25 p.m. on June 30, 2026, and reported that as of 10:30 p.m. that night Gonzalez led with 63% of the vote to Danielson's 37%. CPR also reported that Danielson conceded by calling Gonzalez to congratulate her on the victory [Jeffco clerk and voting rights advocate Amanda Gonzalez wins ...](https://www.cpr.org/2026/06/30/colorado-secretary-of-state-primary-election-2026-results/).
- Multiple additional outlets (Colorado Sun headline "Amanda Gonzalez wins Democratic primary for secretary of state," Denver Post, Colorado Democrats) corroborate the result.

Edge cases from the resolution criteria are not triggered: Gonzalez did not withdraw or get disqualified before election day, and the primary was not canceled — it was a contested two-candidate race that Gonzalez won outright. Because Gonzalez received the most votes (more than Danielson and any other candidate), the question resolves YES.

Sources:
- Colorado Sun: https://coloradosun.com/2026/06/30/colorado-primary-election-secretary-of-state-results/ [Amanda Gonzalez wins Democratic primary for secretary of state](https://coloradosun.com/2026/06/30/colorado-primary-election-secretary-of-state-results/)
- CPR: https://www.cpr.org/2026/06/30/colorado-secretary-of-state-primary-election-2026-results/ [Jeffco clerk and voting rights advocate Amanda Gonzalez wins ...](https://www.cpr.org/2026/06/30/colorado-secretary-of-state-primary-election-2026-results/)
- AP results page referenced: https://apnews.com/projects/elections-2026/colorado-primary-results-secretary-of-state/

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):

### YES-64. `f8bb5c6f-528f-5180-a3f0-649548a15fa7`

- Present date: `2026-05-03 13:18:39.218273`
- Source cutoff boundary: `2026-05-04` (encodes end of UTC day `2026-05-03`)
- Expected resolution: `2026-06-01 00:00:00`

**Question**

Will Kevin Warsh be confirmed by the U.S. Senate as Federal Reserve Chair by June 1, 2026?

**Resolution criteria**

This question resolves YES if the U.S. Senate confirms Kevin Warsh as Chairman of the Board of Governors of the Federal Reserve System via a successful floor vote on or after April 30, 2026 (12:00 AM Eastern Time) and no later than June 1, 2026 (11:59 PM Eastern Time). "Confirmed" is defined as a successful roll call vote in the U.S. Senate in favor of the nomination, as recorded on the official Congress.gov nomination tracker (https://www.congress.gov/nomination/119th-congress/855/1) or the Senate roll call vote page (https://www.senate.gov/legislative/votes.htm). If no such confirmation vote has occurred by 11:59 PM Eastern Time on June 1, 2026, or if the nomination is withdrawn or defeated, the question resolves NO.

**Pre-cutoff background**

Kevin Warsh was nominated by President Donald Trump in January 2026 to succeed Jerome Powell as Chair of the Federal Reserve Board of Governors. Powell's term as Fed Chair is scheduled to end on May 15, 2026. Warsh's nomination was formally transmitted to the Senate on March 4, 2026. The Senate Banking Committee held a confirmation hearing on April 21, 2026, and on April 29, 2026, voted 13–11 along party lines to advance Warsh's nomination to the full Senate [Fed Chief Nominee Warsh Clears Key Confirmation Hurdle in Senate](https://gvwire.com/2026/04/29/fed-chief-nominee-warsh-clears-key-confirmation-hurdle-in-senate/). The earliest the full Senate could vote on the nomination is the week of May 11, 2026 [Fed Chief Nominee Warsh Clears Key Confirmation Hurdle in Senate](https://gvwire.com/2026/04/29/fed-chief-nominee-warsh-clears-key-confirmation-hurdle-in-senate/). If confirmed during that week, Warsh could be sworn in by May 15, when Powell's chairmanship ends. However, Senate procedural delays, Democratic opposition, or other legislative priorities could push the vote beyond that window. The nomination can be tracked at: https://www.congress.gov/nomination/119th-congress/855/1

**Exact later resolution packet**

The question resolves YES. The U.S. Senate confirmed Kevin Warsh as Chairman of the Board of Governors of the Federal Reserve System on May 13, 2026, by a roll call vote of 54–45 (Record Vote Number 120) — this date falls squarely within the resolution window of April 30, 2026 (12:00 AM ET) through June 1, 2026 (11:59 PM ET). This is confirmed by the official Congress.gov nomination tracker for nomination 119PN855-1 (https://www.congress.gov/nomination/119th-congress/855/1), which records the Senate floor vote and confirmation on May 13, 2026 [https://www.congress.gov/nomination/119th-congress/855/1](https://www.congress.gov/nomination/119th-congress/855/1). The corresponding Senate roll call vote page is https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00120.htm. Multiple major news outlets corroborate this: CNBC, BBC, Reuters, NPR, and C-SPAN all report the Senate confirmed Warsh 54–45 on Wednesday, May 13, 2026, with Democrat John Fetterman joining Republicans. No withdrawal or defeat occurred; the nomination was successfully confirmed via roll call vote within the specified window.

**Gates (all four must hold to ACCEPT):**
- [ ] pre-cutoff intact — background/question contain no post-cutoff facts
- [ ] realized outcome valid — resolution matches the cited evidence
- [ ] exact packet factually valid — no factual or temporal-logic error in `resolution_explanation`
- [ ] criteria unambiguous — resolution criteria admit only one reading

- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):
