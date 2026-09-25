# Rationale coding batch - model mistral-small-24b (G24A reversibility audit, step 4)

One section per exact-evidence group (53 total, gnum matches the
classification CSV). Read EVERY section fully. Labels + output
format: g24a_reversibility_v1_coding_rubric.md

## gnum 1 sha=02a240f095 source=fever type=explicit_negation
EVIDENCE: He has received several awards and recognition for his work, including the National Film Award for Best Director for his fourth feature film Naan Kadavul (2009).
INC claim (supported by evidence): [g24a_fever_193540] Bala has received recognition for his work in film.
  values: admit_post=94.1 -> exclude_post=25.6
  exclude_post reasoning: Without any evidence to support the claim, it is impossible to determine the likelihood of its truth. The claim could be true, but there is no information to suggest that it is.
DEC claim (refuted by evidence): [g24a_fever_193532] Bala has received zero recognition for his work.
  values: admit_post=0.1 -> exclude_post=58.0
  exclude_post reasoning: Given the exclusion of Evidence E, there is no information provided to contradict the claim. Therefore, without any evidence to the contrary, the claim could be true.

## gnum 2 sha=02c269369d source=fever type=numeric_value
EVIDENCE: Ralph Fults (January 23, 1911 -- March 16, 1993) was a Depression-era outlaw and escape artist associated with Raymond Hamilton, Bonnie Parker and Clyde Barrow of the Barrow Gang.
INC claim (supported by evidence): [g24a_fever_223774] The Barrow Gang is a criminal organization that Ralph Fults was associated with.
  values: admit_post=96.4 -> exclude_post=18.4
  exclude_post reasoning: Without Evidence E, there is no information to support or refute the claim. Therefore, it is impossible to determine the likelihood of the claim being true.
DEC claim (refuted by evidence): [g24a_fever_223771] Ralph Fults was born in 1993.
  values: admit_post=0.1 -> exclude_post=30.4
  exclude_post reasoning: Without any evidence to consider, it is impossible to determine the likelihood of the claim being true. There is no information to support or refute the claim.

## gnum 3 sha=0ad89d58b1 source=scifact type=antonym_opposite
EVIDENCE: Moreover, KDM4E plays a more crucial role in IVF and SCNT embryonic development, and overexpression of KDM4E can restore the global transcriptome, improve blastocyst formation and increase the cloning efficiency of SCNT embryos.
INC claim (supported by evidence): [g24a_scifact_1035] Overexpression of KDM4E improves reprogramming efficiency in SCNT experiments.
  values: admit_post=94.9 -> exclude_post=8.6
  exclude_post reasoning: The claim specifically mentions "reprogramming efficiency in SCNT experiments," but the only evidence provided does not directly address reprogramming efficiency. Therefore, there is no direct evidence to support the claim.
DEC claim (refuted by evidence): [g24a_scifact_1034] Removal of H3K9me3 by ectopic expression of other H3K9 demethylases decreases reprogramming efficiency in SCNT experiments.
  values: admit_post=10.0 -> exclude_post=26.3
  exclude_post reasoning: The claim suggests that removing H3K9me3 by expressing other demethylases decreases reprogramming efficiency in SCNT experiments. However, there is no direct evidence provided to support this claim. Therefore, the likelihood that the claim is true is low.

## gnum 4 sha=0bab0a612e source=scifact type=antonym_opposite
EVIDENCE: The tumorigenic potential of GSCs was decreased with A20 targeting, resulting in increased survival of mice bearing human glioma xenografts. Although inactivating mutations in A20 in lymphoma suggest A20 can act as a tumor suppressor, similar point mutations have not been identified through glioma genomic sequencing: in fact, our data suggest A20 may function as a tumor enhancer in glioma through promotion of GSC survival.
INC claim (supported by evidence): [g24a_scifact_1136] TNFAIP3 is a tumor enhancer in glioblastoma.
  values: admit_post=86.8 -> exclude_post=42.8
  exclude_post reasoning: Without evidence E, there is no direct evidence supporting or refuting the claim. Therefore, the likelihood that the claim is true cannot be determined.
DEC claim (refuted by evidence): [g24a_scifact_1137] TNFAIP3 is a tumor suppressor in glioblastoma.
  values: admit_post=10.7 -> exclude_post=15.4
  exclude_post reasoning: The claim states that TNFAIP3 (A20) is a tumor suppressor in glioblastoma. However, the only evidence provided does not support this claim. Therefore, the likelihood that the claim is true is low.

## gnum 5 sha=0f5ba488f4 source=scifact type=numeric_value
EVIDENCE: Even if only 7% of patients awaiting kidney transplantation participated in an optimized national KPD program, the health care system could save as much as $750 million.
INC claim (supported by evidence): [g24a_scifact_1185] The US health care system can save up to $750 million if 7% of patients waiting for kidney transplants participate in the optimized national kidney paired donation program.
  values: admit_post=99.9 -> exclude_post=18.8
  exclude_post reasoning: Without Evidence E, there is no direct data to support the claim. Therefore, the likelihood that the claim is true cannot be determined.
DEC claim (refuted by evidence): [g24a_scifact_1184] The US health care system can save up to $5 billion if 7% of patients waiting for kidney transplants participate in the optimized national kidney paired donation program.
  values: admit_post=23.1 -> exclude_post=19.3
  exclude_post reasoning: The claim states a potential saving of $5 billion, while the excluded evidence mentions $750 million. Without the evidence, there is no data to support the claim. Therefore, the likelihood that the claim is true is low.

## gnum 6 sha=130ca6d4a1 source=scifact type=antonym_opposite
EVIDENCE: Treatment with the G4-stabilizing compound pyridostatin (PDS) increases telomere fragility in BRCA2-deficient cells, suggesting that G4 formation drives telomere instability.
INC claim (supported by evidence): [g24a_scifact_1000] Pyridostatin stabilizes the G - quadruplex in the telomeric region.
  values: admit_post=88.7 -> exclude_post=28.2
  exclude_post reasoning: The claim directly states that pyridostatin stabilizes the G-quadruplex in the telomeric region. However, without any supporting evidence, it is impossible to assess the truth of the claim.
DEC claim (refuted by evidence): [g24a_scifact_990] Pyridostatin decreases telomere fragility in BRCA2-deficient cells.
  values: admit_post=5.3 -> exclude_post=0.4
  exclude_post reasoning: There is no evidence to support the claim that Pyridostatin decreases telomere fragility in BRCA2-deficient cells. In fact, the excluded evidence suggests the opposite.

## gnum 7 sha=16327e7b59 source=scifact type=antonym_opposite
EVIDENCE: In vivo, these antibodies slowed the growth of multiple established CRPC xenografts, blocked local invasion and metastasis and, at higher doses, led to complete regression. Therapeutic targeting of this factor with monoclonal antibodies may have considerable clinical benefit.
INC claim (supported by evidence): [g24a_scifact_805] Monoclonal antibody targeting of N-cadherin inhibits metastasis.
  values: admit_post=90.3 -> exclude_post=10.5
  exclude_post reasoning: The claim suggests that monoclonal antibodies targeting N-cadherin inhibit metastasis. However, without evidence E, there is no direct evidence provided to support this claim. Therefore, it is impossible to determine the likelihood of the claim being true.
DEC claim (refuted by evidence): [g24a_scifact_802] Monoclonal antibody targeting of N-cadherin encourages metastasis.
  values: admit_post=8.0 -> exclude_post=0.3
  exclude_post reasoning: The claim suggests that monoclonal antibodies targeting N-cadherin encourage metastasis, but the provided evidence shows that these antibodies actually block metastasis. Therefore, the evidence directly contradicts the claim.

## gnum 8 sha=167f30ddc2 source=scifact type=explicit_negation
EVIDENCE: After adjusting for age, body mass index, race, current smoking status, and recent hormonal contraceptive use, women with low AMH values (<0.7 ng/mL [n = 84]) did not have a significantly different predicted probability of conceiving by 6 cycles of attempt (65%; 95% CI, 50%-75%) compared with women (n = 579) with normal values (62%; 95% CI, 57%-66%) or by 12 cycles of attempt (84% [95% CI, 70%-91%] vs 75% [95% CI, 70%-79%], respectively). Women with high serum FSH values (>10 mIU/mL [n = 83]) did not have a significantly different predicted probability of conceiving after 6 cycles of attempt (63%; 95% CI, 50%-73%) compared with women (n = 654) with normal values (62%; 95% CI, 57%-66%) or after 12 cycles of attempt (82% [95% CI, 70%-89%] vs 75% [95% CI, 70%-78%], respectively). Women with high urinary FSH values (>11.5 mIU/mg creatinine [n = 69]) did not have a significantly different predicted probability of conceiving after 6 cycles of attempt (61%; 95% CI, 46%-74%) compared with women (n = 660) with normal values (62%; 95% CI, 58%-66%) or after 12 cycles of attempt (70% [95% CI, 54%-80%] vs 76% [95% CI, 72%-80%], respectively). Inhibin B levels (n = 737) were not associated with the probability of conceiving in a given cycle (hazard ratio per 1-pg/mL increase, 0.999; 95% CI, 0.997-1.001). Conclusions and Relevance Among women aged 30 to 44 years without a history of infertility who had been trying to conceive for 3 months or less, biomarkers indicating diminished ovarian reserve compared with normal ovarian reserve were not associated with reduced fertility.
INC claim (supported by evidence): [g24a_scifact_39] A diminished ovarian reserve does not solely indicate infertility in an a priori non-infertile population.
  values: admit_post=89.7 -> exclude_post=45.1
  exclude_post reasoning: The claim suggests that a diminished ovarian reserve does not solely indicate infertility in a non-infertile population. Without considering Evidence E, there is no direct evidence provided to support or refute this claim. Therefore, it is impossible to determine the likelihood of the claim being true.
DEC claim (refuted by evidence): [g24a_scifact_40] A diminished ovarian reserve is a very strong indicator of infertility, even in an a priori non-infertile population.
  values: admit_post=7.1 -> exclude_post=11.5
  exclude_post reasoning: The claim suggests that a diminished ovarian reserve is a strong indicator of infertility, but the excluded evidence directly contradicts this by showing no significant difference in conception rates between women with low and normal ovarian reserve biomarkers. Therefore, the claim is likely false.

## gnum 9 sha=191c8c6d12 source=scifact type=explicit_negation
EVIDENCE: Patch clamp recordings showed that activity-induced LTP at identified synapses between nociceptors and spinal neurons projecting to the periaqueductal grey (PAG) was completely abolished in SNS-PKG-I(-/-) mice, although basal synaptic transmission was not affected.
INC claim (supported by evidence): [g24a_scifact_912] PKG-I plays an essential role in expression of spinal long term potentiation in PKG-I knockout mice.
  values: admit_post=91.6 -> exclude_post=18.1
  exclude_post reasoning: Without Evidence E, there is no direct evidence supporting the claim. Therefore, the likelihood that the claim is true cannot be determined.
DEC claim (refuted by evidence): [g24a_scifact_910] PKG-I does not have a large impact on expression of spinal long term potentiation in PKG-I knockout mice.
  values: admit_post=6.4 -> exclude_post=47.2
  exclude_post reasoning: Without Evidence E, there is no direct evidence provided to support or refute the claim. Therefore, the likelihood that the claim is true cannot be determined.

## gnum 10 sha=206f9579ad source=scifact type=antonym_opposite
EVIDENCE: We found that the response of memory, but not naive, CD4+ T cells enhances production of multiple innate inflammatory cytokines and chemokines (IICs) in the lung and that, during influenza infection, this leads to early control of virus.
INC claim (supported by evidence): [g24a_scifact_1348] Upon viral challenge, influenza-specific memory CD4+ T cells greatly enhance the early production of inflammatory chemokines in the lung.
  values: admit_post=93.5 -> exclude_post=4.6
  exclude_post reasoning: The claim specifically mentions "memory CD4+ T cells" and "influenza-specific" which is not addressed in the evidence. The evidence does not support the claim as it does not mention influenza-specific memory CD4+ T cells.
DEC claim (refuted by evidence): [g24a_scifact_1347] Upon viral challenge, influenza-specific memory CD4+ T cells greatly diminish the early production of inflammatory chemokines in the lung.
  values: admit_post=8.9 -> exclude_post=13.3
  exclude_post reasoning: The claim states that memory CD4+ T cells diminish the production of inflammatory chemokines, while Evidence E indicates that they enhance production. Since Evidence E is excluded, there is no evidence to support the claim. Therefore, the likelihood that the claim is true is low.
  [extra DEC item, context only, do not label: g24a_scifact_379] Enhanced early production of inflammatory chemokines damages viral control in the lung.
    exclude_post value=3.4 reasoning: The claim suggests that enhanced early production of inflammatory chemokines damages viral control, but the provided evidence does not support this claim. The evidence actually shows that enhanced production of inflammatory cytokines and chemokines leads to early control of the virus.

## gnum 11 sha=23e2026256 source=scifact type=explicit_negation
EVIDENCE: Patients who used azathioprine, methotrexate, mycophenolate mofetil, ciclosporin, systemic corticosteroids, or dapsone had overall and cancer mortality similar to that of patients who never took immunosuppressive drugs. CONCLUSIONS Most commonly used immunosuppressive drugs do not seem to increase overall or cancer mortality.
INC claim (supported by evidence): [g24a_scifact_1125] Systemic immunosuppressive (IS) therapy does not enhance the chance of cancer mortality in patients with inflammatory eye disease (IED)
  values: admit_post=89.0 -> exclude_post=45.0
  exclude_post reasoning: Without evidence E, there is no direct data to support or refute the claim. Therefore, the likelihood that the claim is true cannot be determined.
DEC claim (refuted by evidence): [g24a_scifact_1126] Systemic immunosuppressive (IS) therapy increases the chance of cancer mortality in patients with inflammatory eye disease (IED)
  values: admit_post=9.9 -> exclude_post=42.9
  exclude_post reasoning: Without evidence E, there is no direct evidence to support or refute the claim. Therefore, the likelihood that the claim is true cannot be determined.

## gnum 12 sha=2872aac67b source=scifact type=antonym_opposite
EVIDENCE: FGF21 deficiency causes a marked exacerbation of atherosclerotic plaque formation and premature death in apolipoprotein E(-/-) mice, which is accompanied by hypoadiponectinemia and severe hypercholesterolemia. Replenishment of FGF21 protects against atherosclerosis in apolipoprotein E(-/-)mice via 2 independent mechanisms, inducing the adipocyte production of adiponectin, which in turn acts on the blood vessels to inhibit neointima formation and macrophage inflammation, and suppressing the hepatic expression of the transcription factor sterol regulatory element-binding protein-2, thereby leading to reduced cholesterol synthesis and attenuation of hypercholesterolemia. CONCLUSIONS FGF21 protects against atherosclerosis via fine tuning the multiorgan crosstalk among liver, adipose tissue, and blood vessels.
INC claim (supported by evidence): [g24a_scifact_681] Lack of FGF21 in mice leads to atherosclerotic plaque formation.
  values: admit_post=97.1 -> exclude_post=18.8
  exclude_post reasoning: Without Evidence E, there is no direct evidence supporting the claim. Therefore, the likelihood that the claim is true cannot be determined from the given information.
DEC claim (refuted by evidence): [g24a_scifact_683] Lack of FGF21 in mice slows the rate of atherosclerotic plaque formation.
  values: admit_post=7.6 -> exclude_post=30.2
  exclude_post reasoning: The claim states that a lack of FGF21 slows atherosclerotic plaque formation, but the evidence provided is excluded. Without any evidence, it is impossible to assess the claim.

## gnum 13 sha=295d1e6d1a source=fever type=explicit_negation
EVIDENCE: For its output, it might pass the message through unchanged for delivery to the user's mailbox, redirect the message for delivery elsewhere, or even throw the message away.
INC claim (supported by evidence): [g24a_fever_16224] Email filtering output is capable of throwing messages away.
  values: admit_post=97.9 -> exclude_post=84.7
  exclude_post reasoning: The claim states that email filtering output can discard messages. While this is a common feature of email filtering, the evidence provided is excluded and cannot be considered. The claim aligns with typical email filtering capabilities.
DEC claim (refuted by evidence): [g24a_fever_47403] Email filtering output is incapable of delivering unchanged messages.
  values: admit_post=5.1 -> exclude_post=36.4
  exclude_post reasoning: The claim states that email filtering output cannot deliver unchanged messages. However, the evidence is excluded and must not influence the judgment. Without evidence, it is impossible to assess the claim's validity.

## gnum 14 sha=2af684783a source=fever type=exclusive_alternative
EVIDENCE: Mirny was a 20-gun sloop-of-war of the Imperial Russian Navy, the second ship of the First Russian Antarctic Expedition in 1819 -- 1821, during which Faddey Bellingshausen (commander of the lead ship Vostok) and Mikhail Lazarev (commanding Mirny) circumnavigated the globe, discovered the continent of Antarctica and twice circumnavigated it, and discovered a number of islands and archipelagos in the Southern Ocean and the Pacific.
INC claim (supported by evidence): [g24a_fever_112438] The Mirny (sloop-of-war) was the second ship of the First Russian Antarctic Expedition.
  values: admit_post=99.9 -> exclude_post=3.4
  exclude_post reasoning: Without Evidence E, there is no direct information to support the claim. Therefore, it is impossible to assess the likelihood of the claim being true.
  [extra INC item, context only, do not label: g24a_fever_120681] The Mirny (sloop-of-war) was an expedition's second ship.
    exclude_post value=12.7 reasoning: Without Evidence E, there is no information to support or refute the claim. Therefore, it is impossible to determine the likelihood of the claim being true.
DEC claim (refuted by evidence): [g24a_fever_45374] The Mirny (sloop-of-war) only sailed the Russian coast.
  values: admit_post=0.1 -> exclude_post=6.9
  exclude_post reasoning: The claim states that the Mirny only sailed the Russian coast. However, the evidence provided, despite being excluded, suggests extensive global voyages. Therefore, the claim is likely false.

## gnum 15 sha=2ef7066db4 source=fever type=numeric_value
EVIDENCE: It was established on June 4, 1992 after the Chechen-Ingush Autonomous Soviet Socialist Republic was split in two.
INC claim (supported by evidence): [g24a_fever_43041] Ingushetia was established on June.
  values: admit_post=99.8 -> exclude_post=41.6
  exclude_post reasoning: The claim specifies only the month, without a year or day. Without additional evidence, it is impossible to confirm or deny the claim. The claim could be true, but there is no way to know for sure.
DEC claim (refuted by evidence): [g24a_fever_101716] Ingushetia was established on the 2nd.
  values: admit_post=0.1 -> exclude_post=28.6
  exclude_post reasoning: The claim specifies a date without a month or year, making it impossible to verify. Without any evidence to consider, the claim's truthfulness cannot be determined.

## gnum 16 sha=3784e1e225 source=scifact type=antonym_opposite
EVIDENCE: Here we report a robust UCP1-independent thermogenic mechanism in beige fat that involves enhanced ATP-dependent Ca2+ cycling by sarco/endoplasmic reticulum Ca2+-ATPase 2b (SERCA2b) and ryanodine receptor 2 (RyR2). Conversely, enhanced Ca2+ cycling by activation of α1- and/or β3-adrenergic receptors or the SERCA2b-RyR2 pathway stimulates UCP1-independent thermogenesis in beige adipocytes.
INC claim (supported by evidence): [g24a_scifact_222] Ca2+ cycling is a UCP1-independent thermogenic mechanism.
  values: admit_post=90.9 -> exclude_post=31.7
  exclude_post reasoning: Without considering Evidence E, there is no evidence provided to support or refute the claim. Therefore, it is impossible to assess the likelihood of the claim being true.
DEC claim (refuted by evidence): [g24a_scifact_221] Ca2+ cycling is a UCP1-dependent thermogenic mechanism.
  values: admit_post=11.8 -> exclude_post=33.9
  exclude_post reasoning: The claim states that Ca2+ cycling is a UCP1-dependent thermogenic mechanism. However, since Evidence E is excluded, there is no direct evidence to support or refute the claim. Therefore, without any evidence, it is impossible to determine the likelihood of the claim being true.

## gnum 17 sha=3c940c4ab6 source=scifact type=antonym_opposite
EVIDENCE: Tricyclics significantly reduced the number of days with tension-type headache and number of headache attacks from migraine than placebo (average standardised mean difference -1.29, 95% confidence interval -2.18 to -0.39 and -0.70, -0.93 to -0.48) but not compared with selective serotonin reuptake inhibitors (-0.80, -2.63 to 0.02 and -0.20, -0.60 to 0.19). Tricyclics were also more likely to reduce the intensity of headaches by at least 50% than either placebo (tension-type: relative risk 1.41, 95% confidence interval 1.02 to 1.89; migraine: 1.80, 1.24 to 2.62) or selective serotonin reuptake inhibitors (1.73, 1.34 to 2.22 and 1.72, 1.15 to 2.55). CONCLUSIONS Tricyclic antidepressants are effective in preventing migraine and tension-type headaches and are more effective than selective serotonin reuptake inhibitors, although with greater adverse effects.
INC claim (supported by evidence): [g24a_scifact_120] Antidepressants reduce the severity of migraines.
  values: admit_post=85.2 -> exclude_post=9.1
  exclude_post reasoning: The claim specifically mentions antidepressants in general, but the provided evidence only discusses tricyclic antidepressants and selective serotonin reuptake inhibitors. Without evidence on other types of antidepressants, it is not possible to make a general statement about all antidepressants.
DEC claim (refuted by evidence): [g24a_scifact_119] Antidepressants increase the severity of migraines.
  values: admit_post=0.6 -> exclude_post=0.4
  exclude_post reasoning: The claim states that antidepressants increase the severity of migraines. However, the provided evidence shows that tricyclic antidepressants can reduce the number of days with headaches and the intensity of migraines. There is no evidence to support the claim that antidepressants increase the severity of migraines.

## gnum 18 sha=418c9c7ded source=fever type=indirect_contradiction
EVIDENCE: Stanley "Tookie" Williams III (December 29, 1953 -- December 13, 2005) was an American gang member and convicted murderer, who was part of the West Side Crips, a street gang which has its roots in South Central Los Angeles in 1969.
INC claim (supported by evidence): [g24a_fever_137414] Stanley Williams lost his life in 2005.
  values: admit_post=100.0 -> exclude_post=18.3
  exclude_post reasoning: Without evidence E, there is no information to support or refute the claim. Therefore, it is impossible to determine the likelihood of the claim being true.
DEC claim (refuted by evidence): [g24a_fever_110276] Stanley Williams is currently a college student in 2017.
  values: admit_post=0.1 -> exclude_post=0.0
  exclude_post reasoning: Stanley Williams, as mentioned in the claim, is a college student in 2017. The evidence provided does not apply to the claim. The claim is about a person who is alive in 2017, but the evidence is about a person who died in 2005. Therefore, the claim is certainly false.
  [extra DEC item, context only, do not label: g24a_fever_99144] Stanley Williams stayed in Cuba his whole life.
    exclude_post value=9.5 reasoning: The claim states that Stanley Williams stayed in Cuba his whole life. However, since Evidence E is excluded and there is no other information provided, there is no basis to support or refute the claim. Therefore, the likelihood that the claim is true is:

## gnum 19 sha=46ea5012c1 source=fever type=explicit_negation
EVIDENCE: Poseidon grossed $181,674,817 at the worldwide box office on a budget of $160 million.
INC claim (supported by evidence): [g24a_fever_5972] Poseidon had a budget of $160 million.
  values: admit_post=99.9 -> exclude_post=39.4
  exclude_post reasoning: The claim states a specific budget amount for the movie Poseidon. Without any evidence to support or refute this claim, it is impossible to determine its truthfulness. Therefore, the likelihood that the claim is true cannot be determined.
DEC claim (refuted by evidence): [g24a_fever_104021] Poseidon lacked a budget of $160 million.
  values: admit_post=0.1 -> exclude_post=32.0
  exclude_post reasoning: Without evidence, it is impossible to determine the truth of the claim. Therefore, the likelihood that the claim is true is unknown.

## gnum 20 sha=4763290d52 source=fever type=explicit_negation
EVIDENCE: He was recognizable by wrestling fans for his distinctively deep and raspy voice, his flamboyant ring attire, intensity exhibited in and out of the ring, using "Pomp and Circumstance" as his entrance music, and his signature catch phrase, "Oooh yeah!"
INC claim (supported by evidence): [g24a_fever_2739] Randy Savage can speak.
  values: admit_post=99.7 -> exclude_post=56.1
  exclude_post reasoning: Randy Savage was a professional wrestler known for his in-ring persona, "Macho Man," which included a distinctive voice. However, there is no direct evidence provided that he could speak outside of his wrestling character.
DEC claim (refuted by evidence): [g24a_fever_96710] Randy Savage does not have a deep voice.
  values: admit_post=4.5 -> exclude_post=40.2
  exclude_post reasoning: Without considering Evidence E, there is no information provided about Randy Savage's voice. Therefore, it is impossible to determine the likelihood of the claim being true.

## gnum 21 sha=4bc72d9ea8 source=scifact type=explicit_negation
EVIDENCE: These studies demonstrated that gynandromorph birds are genuine male:female chimaeras, and indicated that male and female avian somatic cells may have an inherent sex identity. In an example where female tissue was transplanted into a male host, donor cells contributing to the developing testis retained a female identity and expressed a marker of female function. Our study demonstrates that avian somatic cells possess an inherent sex identity and that, in birds, sexual differentiation is substantively cell autonomous.
INC claim (supported by evidence): [g24a_scifact_235] Cell autonomous sex determination in somatic cells occurs in Galliformes.
  values: admit_post=90.9 -> exclude_post=22.3
  exclude_post reasoning: Without Evidence E, there is no direct evidence supporting cell autonomous sex determination in somatic cells of Galliformes. Therefore, the likelihood that the claim is true is low.
DEC claim (refuted by evidence): [g24a_scifact_233] Cell autonomous sex determination in somatic cells does not occur in Galliformes.
  values: admit_post=90.5 -> exclude_post=40.1
  exclude_post reasoning: Without considering Evidence E, there is no provided information to support or refute the claim. Therefore, the likelihood that the claim is true cannot be determined.

## gnum 22 sha=4c0fc60923 source=fever type=exclusive_alternative
EVIDENCE: Brick is a 2005 American neo-noir mystery film written and directed by Rian Johnson in his directorial debut, starring Joseph Gordon-Levitt.
INC claim (supported by evidence): [g24a_fever_211775] Brick (film) is a mystery film.
  values: admit_post=99.7 -> exclude_post=22.5
  exclude_post reasoning: Without any evidence to consider, I cannot determine the likelihood of the claim being true. I have no information to base a judgment on.
DEC claim (refuted by evidence): [g24a_fever_211799] Brick (film) is a 2006 film only.
  values: admit_post=0.1 -> exclude_post=24.6
  exclude_post reasoning: The claim states that "Brick (film) is a 2006 film only." Since we are not allowed to consider the evidence, we have no information to support or refute the claim. Therefore, we cannot make a judgment.

## gnum 23 sha=53ae76df8c source=fever type=numeric_value
EVIDENCE: Directed by Frederik Du Chau and written by Joe Piscatella, Adam Rifkin, and Craig A. Williams, the film stars Jim Belushi, Peter Dinklage, John Slattery, and Patrick Warburton with the voice talents of Jason Lee, Amy Adams, and Brad Garrett.
INC claim (supported by evidence): [g24a_fever_93273] Amy Adams has a voice role in Underdog.
  values: admit_post=99.6 -> exclude_post=25.6
  exclude_post reasoning: I have no information to confirm or deny the claim. The evidence provided is excluded and cannot be considered.
DEC claim (refuted by evidence): [g24a_fever_32505] Underdog stars nine American actors.
  values: admit_post=58.9 -> exclude_post=21.7
  exclude_post reasoning: The claim states that "Underdog" stars nine American actors. However, since the evidence provided is excluded, there is no information to support or refute the claim. Therefore, it is impossible to determine the likelihood of the claim being true.

## gnum 24 sha=5cd5ff81d8 source=scifact type=antonym_opposite
EVIDENCE: We found that CX3CR1 signaling promoted T(H)2 survival in the inflamed lungs, and injection of B cell leukemia/lymphoma-2 protein (BCl-2)-transduced CX3CR1-deficient T(H)2 cells into CX3CR1-deficient mice restored asthma.
INC claim (supported by evidence): [g24a_scifact_217] CX3CR1 on the Th2 cells promotes T cell survival
  values: admit_post=90.3 -> exclude_post=15.8
  exclude_post reasoning: The claim suggests that CX3CR1 on Th2 cells promotes T cell survival. However, since Evidence E is excluded and there is no other evidence provided, it is impossible to assess the likelihood of the claim.
DEC claim (refuted by evidence): [g24a_scifact_216] CX3CR1 on the Th2 cells impairs T cell survival
  values: admit_post=7.1 -> exclude_post=0.3
  exclude_post reasoning: The claim states that CX3CR1 on Th2 cells impairs T cell survival, but the evidence provided shows that CX3CR1 signaling promotes Th2 survival. Therefore, the evidence directly contradicts the claim.

## gnum 25 sha=5d3d709fe5 source=scifact type=antonym_opposite
EVIDENCE: Pharmacological activation of AMPK in myofibroblasts from lungs of humans with IPF display lower fibrotic activity, along with enhanced mitochondrial biogenesis and normalization of sensitivity to apoptosis. In a bleomycin model of lung fibrosis in mice, metformin therapeutically accelerates the resolution of well-established fibrosis in an AMPK-dependent manner. These studies implicate deficient AMPK activation in non-resolving, pathologic fibrotic processes, and support a role for metformin (or other AMPK activators) to reverse established fibrosis by facilitating deactivation and apoptosis of myofibroblasts.
INC claim (supported by evidence): [g24a_scifact_55] AMP-activated protein kinase (AMPK) activation reduces inflammation-related fibrosis in the lungs.
  values: admit_post=89.5 -> exclude_post=12.6
  exclude_post reasoning: The claim suggests that AMPK activation reduces inflammation-related fibrosis in the lungs. However, since Evidence E is excluded and no other evidence is provided, it is impossible to assess the claim.
DEC claim (refuted by evidence): [g24a_scifact_54] AMP-activated protein kinase (AMPK) activation increases inflammation-related fibrosis in the lungs.
  values: admit_post=9.6 -> exclude_post=1.4
  exclude_post reasoning: The claim states that AMPK activation increases inflammation-related fibrosis, but the excluded evidence shows that AMPK activation can decrease fibrotic activity and reverse fibrosis. Therefore, the evidence does not support the claim.

## gnum 26 sha=6cc40aed98 source=scifact type=explicit_negation
EVIDENCE: Several members of the Kruppel-like factor (KLF) family of transcription factors play important roles in differentiation, survival, and trafficking of blood and immune cell types. Thus, our in vivo loss-of-function studies demonstrate that KLF4, previously shown to mediate proinflammatory signaling in human macrophages in vitro, is essential for differentiation of mouse inflammatory monocytes, and is involved in the differentiation of resident monocytes. In addition, inducible expression of KLF4 in the HL60 human acute myeloid leukemia cell line stimulated monocytic differentiation and enhanced 12-O-tetradecanoylphorbol 13-acetate induced macrophage differentiation, but blocked all-trans-retinoic acid induced granulocytic differentiation of HL60 cells. The inflammation-selective effects of loss-of-KLF4 and the gain-of-KLF4-induced monocytic differentiation in HL60 cells identify KLF4 as a key regulator of monocytic differentiation and a potential target for translational immune modulation.
INC claim (supported by evidence): [g24a_scifact_668] Klf4 is important for proper myeloid cell differentiation.
  values: admit_post=90.7 -> exclude_post=20.2
  exclude_post reasoning: Without Evidence E, there is no direct evidence supporting the claim. Therefore, the likelihood that the claim is true cannot be determined from the given information.
DEC claim (refuted by evidence): [g24a_scifact_669] Klf4 is not required for proper myeloid cell differentiation.
  values: admit_post=2.1 -> exclude_post=11.9
  exclude_post reasoning: The claim states that KLF4 is not required for proper myeloid cell differentiation. However, the evidence provided, despite being excluded, suggests that KLF4 is essential for the differentiation of certain types of monocytes and plays a role in monocytic differentiation. Therefore, the claim is likely false.

## gnum 27 sha=6e220295f9 source=fever type=exclusive_alternative
EVIDENCE: AMGTV is an American family-oriented television network featuring television programming consisting of drama, sports, movies, entertainment, how-to, hunting and fishing, children's shows, and other features.
INC claim (supported by evidence): [g24a_fever_154542] AMGTV is a television network that is family-oriented.
  values: admit_post=99.7 -> exclude_post=32.9
  exclude_post reasoning: Without any evidence to consider, it is impossible to determine the likelihood of the claim being true. There is no information to support or refute the claim that AMGTV is a family-oriented television network.
DEC claim (refuted by evidence): [g24a_fever_106478] AMGTV airs only drama programming.
  values: admit_post=1.1 -> exclude_post=30.9
  exclude_post reasoning: The claim states that AMGTV airs only drama programming. However, since we are not allowed to consider the evidence, we have no information to support or refute the claim. Therefore, we cannot make any determination about the claim.

## gnum 28 sha=730b3fd4b4 source=scifact type=antonym_opposite
EVIDENCE: We identify a noncoding polymorphism in FOXO3A (rs12212067: T > G) at which the minor (G) allele, despite not being associated with disease susceptibility, is associated with a milder course of Crohn's disease and rheumatoid arthritis and with increased risk of severe malaria.
INC claim (supported by evidence): [g24a_scifact_1231] The minor G allele of FOXO3 is related to less severe symptoms of Crohn's Disease.
  values: admit_post=98.1 -> exclude_post=17.7
  exclude_post reasoning: Without evidence E, there is no direct evidence supporting the claim. Therefore, the likelihood that the claim is true cannot be determined from the given information.
DEC claim (refuted by evidence): [g24a_scifact_1232] The minor G allele of FOXO3 is related to more severe symptoms of Crohn's Disease.
  values: admit_post=4.9 -> exclude_post=0.7
  exclude_post reasoning: Evidence E directly contradicts the claim. Since Evidence E is excluded, there is no evidence to support the claim.

## gnum 29 sha=7686390b19 source=fever type=exclusive_alternative
EVIDENCE: Shawn Carlson (born 1960) is an American physicist, science writer, and a STEM educator.
INC claim (supported by evidence): [g24a_fever_18752] Shawn Carlson writes about science.
  values: admit_post=97.4 -> exclude_post=12.8
  exclude_post reasoning: Without any evidence to support the claim, it is impossible to determine the likelihood of its truth. Therefore, the claim cannot be evaluated.
DEC claim (refuted by evidence): [g24a_fever_787] Shawn Carlson is only German.
  values: admit_post=0.1 -> exclude_post=1.4
  exclude_post reasoning: The claim states that Shawn Carlson is only German, but we have no evidence to support this. Without any evidence, we cannot confirm the claim.

## gnum 30 sha=76b97884b2 source=fever type=explicit_negation
EVIDENCE: Marcus Morgan Bentley (born 4 October 1967) is a British actor, broadcaster and voice-over artist.
INC claim (supported by evidence): [g24a_fever_201095] There is a British actor name Marcus Bentley.
  values: admit_post=99.9 -> exclude_post=8.3
  exclude_post reasoning: I have no information to confirm or deny the claim. I cannot find any evidence to support the claim.
DEC claim (refuted by evidence): [g24a_fever_201114] Marcus Bentley is incapable of being a voice-over artist.
  values: admit_post=0.8 -> exclude_post=33.3
  exclude_post reasoning: Without any evidence to consider, it is impossible to determine the truth of the claim. Therefore, the likelihood that the claim is true cannot be assessed.

## gnum 31 sha=816626b7c4 source=scifact type=explicit_negation
EVIDENCE: Pregnant women with low serum 25-OHD levels had an increased risk of bacterial vaginosis and low birthweight infants but not delivery by caesarean section. Pregnant women with low 25-OHD levels had an increased risk of bacterial vaginosis and lower birth weight infants, but not delivery by caesarean section.
INC claim (supported by evidence): [g24a_scifact_1367] Vitamin D deficiency affects birth weight.
  values: admit_post=88.6 -> exclude_post=0.8
  exclude_post reasoning: There is no evidence to support the claim that vitamin D deficiency affects birth weight. The only evidence provided has been excluded.
DEC claim (refuted by evidence): [g24a_scifact_1370] Vitamin D deficiency is unrelated to birth weight.
  values: admit_post=9.5 -> exclude_post=45.3
  exclude_post reasoning: Without evidence E, there is no direct evidence to support or refute the claim. Therefore, the likelihood that the claim is true cannot be determined.

## gnum 32 sha=82a409f17e source=fever type=numeric_value
EVIDENCE: The U.S. Census Bureau of 2012 reported a median household income of $87,894, which is higher than the California median of $70,231 and the national average of $62,527.
INC claim (supported by evidence): [g24a_fever_183411] Simi Valley, California, reported a median household income of $87,894 in the 2012 U.S. Census.
  values: admit_post=99.9 -> exclude_post=32.7
  exclude_post reasoning: Without evidence, it is impossible to verify the claim. Therefore, the likelihood that the claim is true cannot be determined.
  [extra INC item, context only, do not label: g24a_fever_183417] Simi Valley, California, reported that its median household income was $87,894 in the 2012 U.S. Census.
    exclude_post value=35.5 reasoning: Without evidence, it is impossible to verify the claim. Therefore, the likelihood that the claim is true cannot be determined.
DEC claim (refuted by evidence): [g24a_fever_183420] Simi Valley, California, reported a median household income of $69,723 in the 2012 U.S. Census.
  values: admit_post=16.1 -> exclude_post=30.1
  exclude_post reasoning: The claim specifies a median household income for Simi Valley, California, in 2012, but no direct evidence is provided to support or refute this figure. Without additional data, it is impossible to verify the claim.

## gnum 33 sha=83377b6d9a source=scifact type=explicit_negation
EVIDENCE: Significantly increased odds of high anxiety symptoms were observed with higher exposure to PM2.5 for multiple averaging periods (for example, odds ratio per 10 µg/m(3) increase in prior one month average PM2.5: 1.12, 95% confidence interval 1.06 to 1.19; in prior 12 month average PM2.5: 1.15, 1.06 to 1.26). CONCLUSIONS Exposure to fine particulate matter (PM2.5) was associated with high symptoms of anxiety, with more recent exposures potentially more relevant than more distant exposures.
INC claim (supported by evidence): [g24a_scifact_399] Exposure to fine particulate air pollution is related to anxiety prevalence.
  values: admit_post=88.6 -> exclude_post=15.6
  exclude_post reasoning: Without Evidence E, there is no direct evidence supporting the claim. Therefore, the likelihood that the claim is true cannot be determined from the given information.
DEC claim (refuted by evidence): [g24a_scifact_400] Exposure to fine particulate air pollution is unrelated to anxiety prevalence.
  values: admit_post=6.4 -> exclude_post=44.7
  exclude_post reasoning: The claim states that exposure to fine particulate air pollution is unrelated to anxiety prevalence. However, the evidence provided is excluded and must have zero influence on the final judgment. Therefore, there is no evidence to support or refute the claim.

## gnum 34 sha=8ac8ca9fc8 source=fever type=explicit_negation
EVIDENCE: Hebe was the cupbearer for the gods and goddesses of Mount Olympus, serving their nectar and ambrosia, until she was married to Heracles (Roman equivalent: Hercules); her successor was the divine hero Ganymede.
INC claim (supported by evidence): [g24a_fever_33739] Hebe married Heracles.
  values: admit_post=97.7 -> exclude_post=24.7
  exclude_post reasoning: Without Evidence E, there is no information to support or refute the claim. Therefore, the likelihood that Hebe married Heracles cannot be determined.
DEC claim (refuted by evidence): [g24a_fever_78778] Hebe was unmarried her entire life.
  values: admit_post=0.1 -> exclude_post=27.0
  exclude_post reasoning: Without considering Evidence E, there is no information provided to support or refute the claim about Hebe's marital status. Therefore, it is impossible to determine the likelihood of the claim being true.

## gnum 35 sha=8c9981f4b9 source=scifact type=antonym_opposite
EVIDENCE: Here we show that activation of ORX-synthesizing neurons is necessary for developing a panic-prone state in the rat panic model, and either silencing of the hypothalamic gene encoding ORX (Hcrt) with RNAi or systemic ORX-1 receptor antagonists blocks the panic responses.
INC claim (supported by evidence): [g24a_scifact_536] Hypocretin neurones induce panicprone state in rats.
  values: admit_post=91.8 -> exclude_post=15.4
  exclude_post reasoning: Without Evidence E, there is no direct evidence supporting the claim. Therefore, the likelihood that the claim is true cannot be determined from the given information.
DEC claim (refuted by evidence): [g24a_scifact_537] Hypocretin neurones suppress panicprone state in rats.
  values: admit_post=1.0 -> exclude_post=0.5
  exclude_post reasoning: The claim states that hypocretin neurons suppress a panic-prone state, but the evidence excluded shows that activation of these neurons is necessary for developing such a state. Therefore, the evidence directly contradicts the claim.

## gnum 36 sha=8cc84fdc4b source=fever type=exclusive_alternative
EVIDENCE: Later, this movie was dubbed into Malayalam, Japanese, and Korean under the same name.
INC claim (supported by evidence): [g24a_fever_166919] Baadshah was dubbed into Japanese.
  values: admit_post=97.4 -> exclude_post=13.1
  exclude_post reasoning: The claim states that "Baadshah was dubbed into Japanese." However, there is no evidence provided to support this claim. Therefore, it is impossible to verify the claim.
DEC claim (refuted by evidence): [g24a_fever_166951] Baadshah was only dubbed into English.
  values: admit_post=0.3 -> exclude_post=76.3
  exclude_post reasoning: The claim states that "Baadshah was only dubbed into English." Since we are instructed to exclude evidence E, we have no information about other languages. Therefore, without any evidence to the contrary, we can only assume the claim is true.

## gnum 37 sha=9909d08591 source=fever type=exclusive_alternative
EVIDENCE: The daughter of actors Barry and Lindsay Otto, and the sister of actress Gracie Otto, Brisbane-born Miranda began her acting career at age 18 in 1986, and has appeared in a variety of independent and major studio films.
INC claim (supported by evidence): [g24a_fever_23198] Miranda Otto began her film acting career at age 18.
  values: admit_post=99.7 -> exclude_post=26.8
  exclude_post reasoning: Without evidence E, there is no information to support or refute the claim. Therefore, it is impossible to determine the likelihood of the claim being true.
DEC claim (refuted by evidence): [g24a_fever_40778] Miranda Otto is the mother of actress Gracie Otto.
  values: admit_post=0.0 -> exclude_post=2.4
  exclude_post reasoning: The claim states that Miranda Otto is the mother of Gracie Otto. However, there is no evidence provided to support this claim. Without any evidence, it is not possible to determine the likelihood of the claim being true.

## gnum 38 sha=a19309c246 source=fever type=exclusive_alternative
EVIDENCE: The Sugarland Express is a 1974 American crime drama film co-written and directed by Steven Spielberg in his theatrical feature film directorial debut.
INC claim (supported by evidence): [g24a_fever_203627] Steven Spielberg's directorial debut was the 1974 crime film The Sugarland Express.
  values: admit_post=99.9 -> exclude_post=4.9
  exclude_post reasoning: Without Evidence E, there is no information to support the claim. Therefore, it is impossible to determine the likelihood of the claim being true.
DEC claim (refuted by evidence): [g24a_fever_203614] The 1976 thriller Duel was Steven Spielberg's directorial debut.
  values: admit_post=0.1 -> exclude_post=28.8
  exclude_post reasoning: The claim states that "Duel" was Steven Spielberg's directorial debut, but since we cannot consider the evidence provided, we cannot confirm or deny this claim. Therefore, we cannot determine the likelihood of the claim being true.

## gnum 39 sha=a1d8bd2633 source=scifact type=numeric_value
EVIDENCE: RESULTS Of the 32,441 appendix samples 16 were positive for abnormal PrP, indicating an overall prevalence of 493 per million population (95% confidence interval 282 to 801 per million).
INC claim (supported by evidence): [g24a_scifact_5] 1/2000 in UK have abnormal PrP positivity.
  values: admit_post=90.3 -> exclude_post=15.2
  exclude_post reasoning: Without evidence E, there is no data to support or refute the claim. Therefore, it is impossible to assess the likelihood of the claim being true.
DEC claim (refuted by evidence): [g24a_scifact_2] 1 in 5 million in UK have abnormal PrP positivity.
  values: admit_post=7.0 -> exclude_post=32.9
  exclude_post reasoning: Without evidence E, there is no data to support or refute the claim. Therefore, the likelihood that the claim is true cannot be determined.

## gnum 40 sha=a8fc3392e2 source=scifact type=antonym_opposite
EVIDENCE: Immunoprecipitation studies of nucleosome core particles (NCPs) show that NCPs that contain both H3.3 and H2A.Z are even less stable than NCPs containing H3.3 and H2A.
INC claim (supported by evidence): [g24a_scifact_1040] Replacement of histone H2A with H2A.Z destabilizes nucleosomes.
  values: admit_post=88.4 -> exclude_post=9.0
  exclude_post reasoning: The claim suggests that replacing histone H2A with H2A.Z destabilizes nucleosomes. However, without any evidence to support this claim, it is impossible to assess its validity.
DEC claim (refuted by evidence): [g24a_scifact_1041] Replacement of histone H2A with H2A.Z slows gene activation in yeasts by stabilizing +1 nucleosomes.
  values: admit_post=22.6 -> exclude_post=36.9
  exclude_post reasoning: The claim specifically mentions the replacement of histone H2A with H2A.Z and its effect on gene activation in yeasts. There is no direct evidence provided to support or refute this claim. Therefore, the likelihood that the claim is true cannot be determined from the given information.

## gnum 41 sha=b4210ea945 source=fever type=exclusive_alternative
EVIDENCE: Series 1 aired in Australia on ABC TV in mid-2007 (repeated 2009).
INC claim (supported by evidence): [g24a_fever_214973] Sensitive Skin's first series aired in a country.
  values: admit_post=99.9 -> exclude_post=17.6
  exclude_post reasoning: Without any evidence, it is impossible to determine the truth of the claim. Therefore, the likelihood that the claim is true is:
DEC claim (refuted by evidence): [g24a_fever_214989] Sensitive Skin's first series aired only on SBS TV.
  values: admit_post=5.6 -> exclude_post=17.1
  exclude_post reasoning: Without evidence from SBS TV, there is no information to support the claim. Therefore, the likelihood that the claim is true is low.

## gnum 42 sha=b659bb4463 source=scifact type=antonym_opposite
EVIDENCE: Here, we show that mice lacking SIRT1 in steroidogenic factor 1 (SF1) neurons are hypersensitive to dietary obesity owing to maladaptive energy expenditure. Also, mutant mice have increased susceptibility to developing dietary T2DM due to insulin resistance in skeletal muscle. Conversely, mice overexpressing SIRT1 in SF1 neurons are more resistant to diet-induced obesity and insulin resistance due to increased energy expenditure and enhanced skeletal muscle insulin sensitivity.
INC claim (supported by evidence): [g24a_scifact_779] Mice lacking Sirt1 in Sf1-expressing neurons have increased susceptibility to diet-induced obesity and insulin resistance.
  values: admit_post=99.6 -> exclude_post=13.3
  exclude_post reasoning: The claim is based on the absence of evidence E, which is excluded. Without any evidence, it is impossible to determine the likelihood of the claim being true.
DEC claim (refuted by evidence): [g24a_scifact_778] Mice lacking Sirt1 in Sf1-expressing neurons are immune to diet-induced obesity and insulin resistance.
  values: admit_post=0.5 -> exclude_post=29.3
  exclude_post reasoning: The claim states that mice lacking Sirt1 in Sf1-expressing neurons are immune to diet-induced obesity and insulin resistance. However, the evidence provided (E) is excluded and must have zero influence on the final judgment. Therefore, there is no evidence to support or refute the claim.

## gnum 43 sha=c048fb5c27 source=fever type=explicit_negation
EVIDENCE: Hickam has also written a number of best-selling memoirs and novels including the "Josh Thurlow" historical fiction novels.
INC claim (supported by evidence): [g24a_fever_216389] Homer Hickam is a writer of historical fiction books.
  values: admit_post=99.3 -> exclude_post=27.4
  exclude_post reasoning: The claim states that Homer Hickam is a writer of historical fiction books. However, without any evidence to support this claim, it is impossible to determine its validity. There is no information provided to confirm or deny the claim.
DEC claim (refuted by evidence): [g24a_fever_216390] Homer Hickam was incapable of writing anything for the Josh Thurlow novels.
  values: admit_post=3.7 -> exclude_post=42.7
  exclude_post reasoning: Without evidence E, there is no information to support or refute the claim. Therefore, the likelihood that the claim is true cannot be determined.

## gnum 44 sha=c598c8dbb1 source=fever type=numeric_value
EVIDENCE: Principal photography commenced in June 2016 and filming locations include Delhi, Mumbai, Patna, Dumraon, Varanasi, New York City and Cape Town.
INC claim (supported by evidence): [g24a_fever_124341] Half Girlfriend's principal photography began in 2016.
  values: admit_post=98.8 -> exclude_post=36.8
  exclude_post reasoning: Without evidence, it is impossible to verify the claim. Therefore, the likelihood that the claim is true cannot be determined.
DEC claim (refuted by evidence): [g24a_fever_141838] Half Girlfriend's principal photography ended in January of 2016.
  values: admit_post=6.1 -> exclude_post=41.9
  exclude_post reasoning: The claim states that principal photography ended in January 2016, but we have no evidence to support or contradict this. Without any evidence, we cannot determine the likelihood of the claim being true.
  [extra DEC item, context only, do not label: g24a_fever_47792] Half Girlfriend's principal photography began in May of 2016.
    exclude_post value=30.0 reasoning: The claim states that principal photography began in May 2016, but we cannot consider the evidence that says it began in June 2016. Without any other information, we cannot confirm the claim.

## gnum 45 sha=c963114af9 source=fever type=explicit_negation
EVIDENCE: Jones has never been on an NBA team with a losing record and has only missed the playoffs once -- with the Trail Blazers in 2007 -- 08.
INC claim (supported by evidence): [g24a_fever_66842] James Jones missed the playoffs once in 2007-2008.
  values: admit_post=99.9 -> exclude_post=27.3
  exclude_post reasoning: Without evidence, it is impossible to determine the truth of the claim. Therefore, the likelihood that the claim is true cannot be assessed.
DEC claim (refuted by evidence): [g24a_fever_68337] James Jones has never missed the playoffs.
  values: admit_post=0.1 -> exclude_post=40.4
  exclude_post reasoning: The claim states that James Jones has never missed the playoffs, but we cannot consider the evidence provided. Without any evidence, we cannot determine the likelihood of the claim being true.

## gnum 46 sha=ce47287f7f source=fever type=explicit_negation
EVIDENCE: Night of the Living Dead is a 1968 American independent horror film, directed by George A. Romero, starring Duane Jones and Judith O'Dea.
INC claim (supported by evidence): [g24a_fever_105216] Night of the Living Dead is not a series of seven zombie horror films.
  values: admit_post=92.6 -> exclude_post=60.5
  exclude_post reasoning: The claim states that "Night of the Living Dead" is not a series of seven zombie horror films. Since the evidence provided is excluded, we have no information to contradict the claim. Therefore, based on the lack of evidence, the claim could be true.
DEC claim (refuted by evidence): [g24a_fever_148263] Night of the Living Dead is a series of works of art.
  values: admit_post=9.9 -> exclude_post=21.7
  exclude_post reasoning: The claim states that "Night of the Living Dead" is a series of works of art, but without any evidence to support this, it is impossible to verify. Therefore, the likelihood that the claim is true cannot be determined.

## gnum 47 sha=e6af48c413 source=scifact type=explicit_negation
EVIDENCE: The inclusion of a visual screening component in the assessment did not result in improvements in self reported visual problems (pooled odds ratio 1.04:95% confidence interval 0.89 to 1.22). CONCLUSIONS Screening of asymptomatic older people in the community is not justified on present evidence.
INC claim (supported by evidence): [g24a_scifact_137] Asymptomatic visual impairment screening in elderly populations does not lead to improved vision.
  values: admit_post=82.0 -> exclude_post=44.4
  exclude_post reasoning: Without evidence E, there is no direct evidence to support or refute the claim. Therefore, the likelihood that the claim is true cannot be determined.
DEC claim (refuted by evidence): [g24a_scifact_138] Asymptomatic visual impairment screening in elderly populations leads to improved vision.
  values: admit_post=11.7 -> exclude_post=21.1
  exclude_post reasoning: Without evidence, it is impossible to determine the likelihood of the claim being true. The claim cannot be evaluated without evidence.

## gnum 48 sha=ec9e00037c source=fever type=exclusive_alternative
EVIDENCE: The doll resides in a glass box at The Warrens' Occult Museum in Monroe, Connecticut.
INC claim (supported by evidence): [g24a_fever_102540] Annabelle is in the United States.
  values: admit_post=92.9 -> exclude_post=39.4
  exclude_post reasoning: The claim states that Annabelle is in the United States, but without evidence, it is impossible to verify. Therefore, the likelihood that the claim is true cannot be determined.
DEC claim (refuted by evidence): [g24a_fever_103545] Annabelle is at The Museum of Natural History.
  values: admit_post=0.0 -> exclude_post=6.5
  exclude_post reasoning: The claim states that Annabelle is at The Museum of Natural History, but there is no evidence provided to support this. Without any evidence, it is impossible to determine the likelihood of the claim being true.

## gnum 49 sha=efe5c764ce source=fever type=explicit_negation
EVIDENCE: The club has won the FA Cup once, in 1976, and their highest-ever league finish was second in the First Division in 1983 -- 84.
INC claim (supported by evidence): [g24a_fever_224369] Southampton F.C. has won the FA Cup.
  values: admit_post=99.8 -> exclude_post=6.8
  exclude_post reasoning: There is no evidence to support the claim that Southampton F.C. has won the FA Cup. Without any relevant information, it is impossible to confirm the claim.
DEC claim (refuted by evidence): [g24a_fever_224370] Southampton F.C. has won zero FA Cups.
  values: admit_post=0.2 -> exclude_post=31.8
  exclude_post reasoning: The claim states that Southampton F.C. has won zero FA Cups. Without considering Evidence E, there is no information provided to support or refute the claim. Therefore, it is impossible to determine the likelihood of the claim being true.

## gnum 50 sha=f320cab67b source=fever type=exclusive_alternative
EVIDENCE: Excuse My French is the debut studio album by American rapper French Montana.
INC claim (supported by evidence): [g24a_fever_208414] Excuse My French is the debut album of an artist.
  values: admit_post=99.7 -> exclude_post=22.0
  exclude_post reasoning: Without any evidence, it is impossible to determine the truth of the claim. Therefore, the likelihood that the claim is true cannot be assessed.
DEC claim (refuted by evidence): [g24a_fever_208433] Excuse My French is only a single by French Montana.
  values: admit_post=3.6 -> exclude_post=28.1
  exclude_post reasoning: The claim states that "Excuse My French" is only a single, but it does not specify by whom. Without additional evidence, it is impossible to confirm or deny the claim. Therefore, the likelihood that the claim is true cannot be determined.

## gnum 51 sha=f4d0aa5c71 source=scifact type=explicit_negation
EVIDENCE: Evidence was lacking for cognitive impairment for any headache type with or without brain lesions.
INC claim (supported by evidence): [g24a_scifact_501] Headaches are not correlated with cognitive impairment.
  values: admit_post=93.4 -> exclude_post=45.2
  exclude_post reasoning: Without evidence, it is impossible to determine the likelihood of the claim. The claim could be true or false.
DEC claim (refuted by evidence): [g24a_scifact_500] Headaches are correlated with cognitive impairment.
  values: admit_post=9.9 -> exclude_post=22.5
  exclude_post reasoning: Without evidence supporting a correlation between headaches and cognitive impairment, it is not possible to assess the claim. There is no basis to support or refute the claim.

## gnum 52 sha=fa68f098d6 source=fever type=numeric_value
EVIDENCE: In 2013 she was ranked as the second highest earning actress/models in Israel, behind Bar Refaeli, but ahead of Esti Ginzburg and Shlomit Malka, with the majority of her income coming from acting.
INC claim (supported by evidence): [g24a_fever_161222] Gal Gadot was ranked ahead of Shlomit Malka for Israel's highest earning actress/models.
  values: admit_post=99.8 -> exclude_post=18.7
  exclude_post reasoning: Without evidence, it is impossible to determine the likelihood of the claim. There is no information to support or refute the claim.
DEC claim (refuted by evidence): [g24a_fever_94603] Gal Gadot was ranked ahead of Bar Rafaeli for highest earning actress/models in Israel.
  values: admit_post=6.0 -> exclude_post=2.5
  exclude_post reasoning: The claim states that Gal Gadot was ranked ahead of Bar Rafaeli, but the evidence provided does not support this. Since the evidence is excluded, there is no information to support the claim.

## gnum 53 sha=fe39679ee7 source=fever type=numeric_value
EVIDENCE: The site was launched in February 2007 by Community Connect Inc..
INC claim (supported by evidence): [g24a_fever_204015] Glee.com is a website launched in the 2000s.
  values: admit_post=98.4 -> exclude_post=36.4
  exclude_post reasoning: Without evidence, I cannot determine the likelihood of the claim. The claim could be true, but I have no information to support it.
DEC claim (refuted by evidence): [g24a_fever_203996] The website Glee.com was first launched in 2010.
  values: admit_post=0.0 -> exclude_post=29.3
  exclude_post reasoning: Without any evidence to consider, it is impossible to determine the likelihood of the claim being true. There is no information to support or refute the claim that Glee.com was first launched in 2010.

