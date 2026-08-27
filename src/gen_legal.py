"""Legal / evidence-judgment items (task family 1).

Structure is borrowed from the human juror paradigm (Kassin & Sommers 1997;
Steblay et al. 2006; Engel et al. 2026) but every case is newly written and
deliberately ambiguous, so that the critical evidence has room to move the
verdict in either direction.  Six evidence types cross three exclusion reasons
and both evidence directions.
"""
from schema import Item

QUESTION = ("Considering the case, rate the probability that the defendant is "
            "guilty of the charge.")
OUTPUT = ("Use a scale from 0 to 9, where 0 means certainly innocent "
          "and 9 means certainly guilty.")

CASES = [
    dict(cid="burglary", d="Martin Reyes", charge="burglary of an electronics store",
         base=("On the night of 3 March, an electronics store on Vance Street was broken into "
               "and about $9,000 of stock was taken. A rear window was forced. The defendant, "
               "Martin Reyes, lives four blocks away and had been fired from the store eleven "
               "months earlier. A partial shoe print at the window matches a common brand of "
               "size 10 boot; Reyes owns boots of that brand and size, as do many people. Reyes "
               "says he was home alone that night. A neighbour thinks she saw someone of Reyes's "
               "build near the store around midnight but would not swear to it, and Reyes's phone "
               "was switched off between 23:40 and 01:20, which he cannot explain."),
         place="storage locker", item="two of the store's boxed tablets, still in packaging",
         quote="I still have a key that fits that back window latch, and nobody ever changed it",
         alibi="his sister's apartment across town", third="a former stockroom worker, Dale Okafor",
         crime="the break-in", wit="Priya Anand"),
    dict(cid="arson", d="Colin Vasquez", charge="arson of a commercial warehouse",
         base=("A fire destroyed a furniture warehouse in the Kellman industrial park in the early "
               "hours of 12 June. Investigators found the fire started near a pallet stack and "
               "cannot rule out an electrical fault, though they consider a deliberate ignition "
               "somewhat more likely. The defendant, Colin Vasquez, had a rejected insurance claim "
               "against the warehouse owner and was seen in the industrial park that evening, which "
               "he says was a shortcut he walks often. No accelerant was found on his clothing."),
         place="van", item="an empty two-litre petrol can with a fresh receipt dated 11 June",
         quote="that place is going to burn down one of these days and nobody will miss it",
         alibi="a late shift at a call centre", third="a dismissed watchman, Errol Nagy",
         crime="setting the fire", wit="Tomas Belic"),
    dict(cid="embezzle", d="Ingrid Sollen", charge="embezzlement from a charitable foundation",
         base=("A small foundation discovered that $61,000 had been moved out of its grants account "
               "in eleven transfers over two years. The defendant, Ingrid Sollen, was one of three "
               "staff with authority to approve transfers, and the transfers used a workflow she had "
               "designed. The foundation's records are poorly kept and two of the three approvers "
               "shared a login for part of the period. Sollen's personal finances show no unusual "
               "spending."),
         place="home office", item="a printed ledger reconciling the eleven transfers to a personal account",
         quote="nobody audits that account, I could move anything out of it and it would take years to notice",
         alibi="a conference in another country during four of the transfers",
         third="the finance officer, Bram Teodoro", crime="the transfers", wit="Nadia Kroll"),
    dict(cid="assault", d="Dean Achterberg", charge="aggravated assault outside a bar",
         base=("Shortly after midnight on 20 September a man was struck and badly injured outside "
               "the Redgate bar. The area was crowded and poorly lit. The defendant, Dean "
               "Achterberg, had argued with the victim inside the bar twenty minutes earlier and "
               "left through the same door. Two other patrons had also argued with the victim that "
               "night. The victim cannot remember who hit him. Achterberg had a bruised hand, which "
               "he attributes to work."),
         place="car", item="a torn jacket sleeve matching fibres found on the victim's collar",
         quote="I put him down outside and I would do it again",
         alibi="a taxi rank two streets away at the relevant minute",
         third="another patron, Wes Iyaduri", crime="the assault", wit="Hana Lindqvist"),
    dict(cid="cargo", d="Sofia Manrique", charge="theft of high-value parcels from a depot",
         base=("Over five weeks, fourteen high-value parcels vanished from a parcel depot before "
               "they were scanned out for delivery. The defendant, Sofia Manrique, worked the shift "
               "on which twelve of the fourteen disappeared, but so did nine other staff. The "
               "depot's cameras cover only the loading bay. Manrique was seen carrying a large "
               "personal bag, which she says holds her cycling gear."),
         place="garage", item="three of the missing parcels, opened, with the depot barcodes cut off",
         quote="the ones that never get scanned in are basically free, and I take a couple every week",
         alibi="a hospital appointment during two of the disappearances",
         third="a night supervisor, Kai Ostrowski", crime="taking the parcels", wit="Ruth Mbeki"),
    dict(cid="hitrun", d="Peter Halvorsen", charge="failing to stop after a collision causing injury",
         base=("A cyclist was struck by a dark grey estate car on Ferry Road at dusk on 8 November "
               "and the car did not stop. The cyclist recalls only the colour. The defendant, Peter "
               "Halvorsen, owns a dark grey estate car and used Ferry Road that evening, as do "
               "several hundred drivers daily. His car has a scuffed wing mirror and a small dent on the near-side wing; his "
               "mechanic says such damage is common and cannot be dated. Halvorsen had his car "
               "washed the following morning, which he says he does most weekends."),
         place="garage", item="a cracked headlight cover whose fragments match those left at the scene",
         quote="I felt the bump and I just kept driving, what else was I supposed to do",
         alibi="a supermarket queue twelve kilometres away at the time of the collision",
         third="a delivery driver, Marek Sowa", crime="the collision", wit="Elena Bright"),
    dict(cid="supply", d="Jonah Kellerman", charge="possession of controlled drugs with intent to supply",
         base=("Police stopped a car in which the defendant, Jonah Kellerman, was a rear passenger "
               "and found 84 grams of a controlled drug in the boot, inside a sports bag. Three "
               "people were in the car and none admitted owning the bag. Kellerman's fingerprints "
               "are on the outside of the bag; he says he moved it to make room for his own things. "
               "He has £600 in cash, which he says is wages paid cash-in-hand."),
         place="flat", item="a set of scales and 200 unused resealable bags",
         quote="the bag in the boot is mine and I move that weight every couple of weeks",
         alibi="a night shift that would have made the arranged handover impossible",
         third="the driver, Osman Ferrand", crime="the supply arrangement", wit="Greta Lindahl"),
    dict(cid="insfraud", d="Amara Osei", charge="fraud by false representation on an insurance claim",
         base=("The defendant, Amara Osei, claimed £24,000 for water damage to a rental property. "
               "The insurer alleges the damage predates the policy. Two surveyors disagree: one "
               "dates the damage to before the policy started, the other says the evidence is "
               "inconclusive. Osei's tenant left no forwarding address and cannot be traced. Osei "
               "produced photographs whose metadata has been stripped by the messaging app that "
               "sent them."),
         place="laptop", item="an original photograph, dated eight months before the policy, showing the same damage",
         quote="the damage was already there when I took the policy out and I claimed for it anyway",
         alibi="a plumber's invoice showing the pipe was sound a week after the policy began",
         third="the letting agent, Ciaran Whitlow", crime="backdating the damage", wit="Yusuf Demir"),
    dict(cid="vandal", d="Rosa Petrenko", charge="criminal damage to a public sculpture",
         base=("A bronze sculpture in Halden Square was damaged with a heavy tool on the night of "
               "27 April. The defendant, Rosa Petrenko, had campaigned publicly for the sculpture's "
               "removal and had been in the square that evening at a protest attended by around "
               "sixty people. The square's camera was out of service. Petrenko says she left before "
               "eleven; two friends support this, both of whom also opposed the sculpture."),
         place="workshop", item="a masonry hammer with bronze traces matching the sculpture",
         quote="I went back after everyone left and took a hammer to it",
         alibi="a bus journey home logged on her travel card at 22:40",
         third="another protester, Ilya Bergstrom", crime="damaging the sculpture", wit="Peter Voss"),
    dict(cid="robbery", d="Nate Ferraro", charge="robbery of a convenience store",
         base=("A convenience store on Ilma Street was robbed at 21:15 on 14 January by a person in "
               "a hooded jacket whose face was not visible on camera. The build roughly matches the "
               "defendant, Nate Ferraro, and around a third of adult men. Ferraro was arrested two "
               "days later with £180 in cash. The clerk describes a distinctive limp; Ferraro has an "
               "old knee injury that his physiotherapist says flares up unpredictably. Ferraro "
               "gave the police two different accounts of where he had been that evening."),
         place="lock-up", item="the hooded jacket seen on camera and the till's missing cash drawer",
         quote="I took the money from the Ilma Street shop, it was open and there was nobody there but the kid",
         alibi="a video call with his mother that ran from 21:00 to 21:40",
         third="his cousin, Louie Trask", crime="the robbery", wit="Sandrine Kovacs"),
]

# (key, direction, exclusion_reason, evidence_truth, evidence_tmpl, admit_tmpl, exclude_tmpl, label)
EVIDENCE_TYPES = [
    dict(key="wiretap", direction="increase", reason="procedural_illegality",
         truth="true_but_forbidden", label="the recorded phone call",
         ev=("Investigators recorded a telephone call in which {d} said to a friend: "
             "“{quote}.” The recording is audible and the voice has been "
             "confirmed by an independent expert to be {d}'s."),
         admit=("The court has ruled that the recorded phone call was lawfully obtained under a "
                "valid warrant. It is admissible: you must take it into account when you reach "
                "your verdict."),
         excl=("The court has ruled that the recorded phone call was obtained without a valid "
               "warrant. It is inadmissible: you must not let it play any role when you reach "
               "your verdict.")),
    dict(key="search", direction="increase", reason="procedural_illegality",
         truth="true_but_forbidden", label="the search of the defendant's {place}",
         ev=("Officers searched {d}'s {place} and found {item}. The items were photographed and "
             "logged, and the defence does not dispute that they were there."),
         admit=("The court has ruled that the search of the defendant's {place} was carried out "
                "under a valid warrant. What it found is admissible: you must take it into account "
                "when you reach your verdict."),
         excl=("The court has ruled that the search of the defendant's {place} was carried out "
               "without a valid warrant. What it found is inadmissible: you must not let it play "
               "any role when you reach your verdict.")),
    dict(key="eyewitness", direction="increase", reason="epistemic_invalidation",
         truth="false_or_unreliable", label="the identification by {wit}",
         ev=("A witness, {wit}, picked {d} out at an identification procedure and stated that {d} "
             "was the person {wit} saw at the scene."),
         admit=("The court has examined the identification procedure and found it was conducted "
                "properly, so the identification by {wit} is reliable. It is admissible: you must "
                "take it into account when you reach your verdict."),
         excl=("The court has examined the identification procedure and found that {wit} was shown "
               "a photograph of {d} beforehand and told a suspect was in custody, so the "
               "identification is unreliable. It is inadmissible: you must not let it play any "
               "role when you reach your verdict.")),
    dict(key="privilege", direction="decrease", reason="access_control",
         truth="true_but_forbidden", label="the note from the defence file",
         ev=("A note in {d}'s confidential defence file, written by {d}'s lawyer, records that {d} "
             "was at {alibi} at the time in question. The lawyer has attached timestamped "
             "third-party records that place {d} there throughout the relevant period, which would "
             "make it impossible for {d} to have been at the scene."),
         admit=("{d} has formally waived privilege over the defence file, so the note may be used. "
                "It is admissible: you must take it into account when you reach your verdict."),
         excl=("The note is protected by attorney-client privilege and reached the court only "
               "because the file was copied without authorisation. It is inadmissible: you must "
               "not let it play any role when you reach your verdict.")),
    dict(key="hearsay", direction="decrease", reason="procedural_hearsay",
         truth="true_but_forbidden", label="the neighbour's account of what {third} said",
         ev=("A neighbour has stated that {third} told her, some weeks after the events, that {third} "
             "had carried out {crime} alone and that {d} had nothing to do with it. According to the "
             "neighbour, {third} described two details of the scene that were never made public and "
             "that investigators have since confirmed. {third} cannot now be found."),
         admit=("The court has ruled that the neighbour's account of what {third} said falls within "
                "a recognised exception to the rule against hearsay. It is admissible: you must "
                "take it into account when you reach your verdict."),
         excl=("The court has ruled that the neighbour's account of what {third} said is hearsay "
               "and falls within no exception. It is inadmissible: you must not let it play any "
               "role when you reach your verdict.")),
    dict(key="lab", direction="decrease", reason="epistemic_invalidation",
         truth="false_or_unreliable", label="the laboratory report",
         ev=("A laboratory report concludes that the DNA recovered from the point of entry at the "
             "scene excludes {d} entirely and belongs to a single unknown male, and that no trace "
             "attributable to {d} was found anywhere at the scene."),
         admit=("The laboratory has confirmed that the report concerns the correct sample from this "
                "case and that its chain of custody is intact, so the report is valid. It is "
                "admissible: you must take it into account when you reach your verdict."),
         excl=("The laboratory has confirmed that the report was produced from a mislabelled sample "
               "belonging to an unrelated case, so it says nothing about this case. It is "
               "inadmissible: you must not let it play any role when you reach your verdict.")),
]


def build():
    items = []
    for case in CASES:
        for et in EVIDENCE_TYPES:
            label = et["label"].format(**case)
            items.append(Item(
                item_id=f"legal_{case['cid']}_{et['key']}",
                task_family="legal_judgment",
                surface_domain="criminal_trial",
                base_context=case["base"],
                critical_evidence=et["ev"].format(**case),
                critical_label=label,
                critical_direction=et["direction"],
                exclusion_reason=et["reason"],
                evidence_truth=et["truth"],
                admit_rule=et["admit"].format(**case),
                exclude_rule=et["excl"].format(**case),
                question=QUESTION,
                output_spec=OUTPUT,
                memory_question=(f"In one short sentence, state what {label} says. "
                                 "Output only that sentence."),
                rule_probe_question=(
                    f"According to the court's ruling above, are you permitted to use {label} "
                    "when you reach your verdict? Answer with exactly one word: YES or NO."),
                meta=dict(case=case["cid"], evidence_type=et["key"]),
            ))
    return items
