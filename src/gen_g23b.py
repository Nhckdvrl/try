"""G23B — fresh legal items for standing gate vs retrospective cancellation.

One natural domain only (the prereg's §3): **legal judgment with an
offer-of-proof / proffer carrier**. 60 items / 60 independent skeletons,
30 evidence-increases / 30 evidence-decreases, one item per skeleton.

Nothing here is inherited. None of the 10 G0 legal case words in
`items_v1.jsonl` (arson, assault, burglary, cargo, embezzle, hitrun, insfraud,
robbery, supply, vandal), none of the 10 G18 surfaces, none of the 24 G23A
surfaces and none of the item ids or skeletons reappear — asserted at build
time in `check_fresh`.

No LLM writes any of this and no LLM grades it — there is no gold label. The
judgment is the model's own rating; the only requirement the design places on an
item is that its evidence push that rating in a known direction, which is what
the frozen Phase-A leverage criteria (E2/E3) check at analysis time.

Every item carries the reopened line's categorical exclusion construction (G0's
`items_v1` style): a reason clause naming the exclusion ground, then the
categorical instruction. The same `exclude_rule` string is used by the U, K and
I cells, so the rule is byte-identical across the three target states and only
block order (and the proffer carrier in K) can differ.

    PYTHONPATH=src python3 src/gen_g23b.py --out data/items/g23b_v1.jsonl
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from schema import Item  # noqa: E402

# Same readout format as every judgment round since G0: the prompt asks for one
# digit on a 0-9 scale and `digit_expectation` records it as 0-100 rating points
# (run_model: readout = "digit_expectation_0_100"). The prereg's "continuous
# 0-100 merits judgment using the existing readout format" is exactly this.
OUTPUT_SPEC = ("Use a scale from 0 to 9, where 0 means certainly not and 9 means "
               "certainly so.")
QUESTION_LEGAL = ("Considering the case, rate the probability that the defendant is "
                  "guilty of the charge.")

# G0's categorical exclusion, one template for all 60 items: reason clause +
# "must not play any role". Stored without the "RULING\n" header (items_v1
# convention); schema._blocks and conditions_g23b add the header so the block is
# byte-identical across U/K/I.
EXCLUDE_TMPL = ("The court has ruled that {label} {reason}. It is inadmissible: "
                "you must not let it play any role when you reach your verdict.")
# G23B runs no admit cell; the field exists for schema parity.
ADMIT_TMPL = ("The court has ruled that {label} is admissible: you must take it "
              "into account when you reach your verdict.")

MEMORY_TMPL = "In one short sentence, state what {label} says. Output only that sentence."
PROBE_TMPL = ("According to the court's ruling above, are you permitted to use {label} "
              "when you reach your verdict? Answer with exactly one word: YES or NO.")


# ---------------------------------------------------------------------------
# Legal judgment — 60 new case skeletons, 30 incriminating / 30 exculpatory.
#
# Each case supplies its own evidence; `direction` is what that evidence does to
# the guilt rating when it is simply present (no rule). `reason` is the
# exclusion ground the court states in the ruling; the four groups are the four
# `exclusion_reason` values the schema documents.
#
# procedural_illegality  (15: 9 inc / 6 dec)
# epistemic_invalidation  (15: 9 inc / 6 dec)
# access_control          (15: 7 inc / 8 dec)
# temporal_irrelevance    (15: 5 inc / 10 dec)
# ---------------------------------------------------------------------------
LEGAL_CASES = {
    # --- procedural_illegality: gathered in violation of procedure rights ----
    "intercomlog": dict(
        d="Rowan Petrides", charge="inflating the roof-fund invoices",
        setting=("A residential block collects a monthly roof fund from its forty-two "
                 "leaseholders, and the renewal contract was let without competitive "
                 "quotes."),
        neutral=["The leaseholders had agreed the renewal at a meeting in March.",
                 "Payments left the joint account in four transfers."],
        reason="were made without the consent of any participant and no exception "
               "applies",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="increase", label="the intercom recordings",
                text=("Secretly made intercom recordings of the leaseholders' meetings "
                      "capture the treasurer steering the roof contract to his "
                      "brother-in-law's firm and naming the figure he intended to "
                      "invoice."))),
    "geofence": dict(
        d="Anya Kowalczyk", charge="the theft of the depot's copper stock",
        setting=("A rail depot held several tonnes of stripped copper awaiting "
                 "collection, and about a third of it went missing over one weekend."),
        neutral=["The stockyard gate was locked on the Friday evening.",
                 "Collection lorries had booked no weekend slots."],
        reason="were obtained through a geofence request that no judicial officer "
               "approved",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="increase", label="the geofence location records",
                text=("Geofence records place her phone inside the stockyard perimeter "
                      "between 01:10 and 02:45 on the Saturday, the same hours the "
                      "copper was cut from the racks."))),
    "dronetrack": dict(
        d="Tomas Ferreira", charge="dumping the drums beside the creek",
        setting=("Forty drums of solvent were left on the bank of a salmon creek, and "
                 "the cleanup fell to the water authority."),
        neutral=["The bank was private land above the waterline.",
                 "Rain had already spread the spill downstream."],
        reason="was gathered by a drone flown over private land without a warrant",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="increase", label="the drone thermal track",
                text=("Thermal footage from a police drone flown without a warrant over "
                      "the holding field shows his pickup reversing to the bank at "
                      "23:40 and leaving with an empty flatbed."))),
    "shedsearch": dict(
        d="Mira Oyelaran", charge="stealing the tools from the shared shed",
        setting=("Residents of a terraced row share a garden shed, and the power tools "
                 "stored there were sold off within a week of vanishing."),
        neutral=["The shed key was held by four households.",
                 "The tools were insured under the block policy."],
        reason="were found in a search of the shed that no warrant authorized",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="increase", label="the shed inventory photographs",
                text=("Photographs taken during the warrantless shed search show her "
                      "pressure washer and the row's two drills still tagged with the "
                      "block's inventory numbers behind her fence panel."))),
    "kioskcheck": dict(
        d="Elias Nordvik", charge="the theft of the kiosk takings",
        setting=("A station news kiosk counted its weekend float each Monday, and one "
                 "Monday the counted bag was six hundred short."),
        neutral=["The kiosk shut at 21:00 on the Sunday.",
                 "Only two staff held the counting code."],
        reason="was seized in a search carried out with no legal basis",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="increase", label="the backpack inventory",
                text=("The inventory drawn up during the roadside search of his "
                      "backpack lists the kiosk's cloth money bag, still stamped with "
                      "the Sunday date and holding the missing notes."))),
    "personalrec": dict(
        d="Sunny Delacroix", charge="the affray at the rail gate",
        setting=("A scuffle at a station gate left one man with a broken nose, and the "
                 "prosecution runs on the complainant's account of who started it."),
        neutral=["The fixed cameras at the gate were not recording that shift.",
                 "Four other passengers gave no statement."],
        reason="was captured on a personal device during a stop that was "
               "never logged",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="decrease", label="the officer's personal recording",
                text=("A video the officer shot on his personal phone, and never "
                      "entered into any log, shows the complainant swinging first at "
                      "the barrier as the defendant stepped back with his hands open."))),
    "hiddenmic": dict(
        d="Hana Iversen", charge="making threats to the caretaker",
        setting=("A housing officer complained of months of threats from a tenant, and "
                 "the caretaker corroborated each incident from memory."),
        neutral=["The corridor had no communal recording equipment.",
                 "The caretaker's notes were kept at home."],
        reason="was planted by a private landlord without the consent of any occupant",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="increase", label="the hallway ceiling microphone",
                text=("A microphone concealed in the hallway ceiling, planted by the "
                      "landlord with nobody's consent, records her telling the "
                      "caretaker she knows which shift his daughter finishes."))),
    "converter": dict(
        d="Bram Ostrowski", charge="the theft of the catalytic converters",
        setting=("Nine converters were sawn from vans in one depot lane in a fortnight, "
                 "and the depot posted a reward for identification."),
        neutral=["The lane was unlit between buildings.",
                 "The cuts matched one saw profile."],
        reason="was pulled from a doorbell account without a warrant or the owner's "
               "valid consent",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="decrease", label="the doorbell cloud footage",
                text=("Cloud footage an officer retrieved from a doorbell maker "
                      "without a warrant shows his van passing the lane at 06:40 "
                      "without slowing, more than an hour before the last saw cut."))),
    "tollquery": dict(
        d="Petra Nilsen", charge="siphoning fuel from the depot tanks",
        setting=("A haulage depot lost nine hundred litres of diesel a month for three "
                 "months, and the standpipe showed fresh hose marks."),
        neutral=["The tank key was held by the yard foreman.",
                 "Night movement in the yard required a gate card."],
        reason="were obtained through queries that no authority ever issued",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="increase", label="the gantry query records",
                text=("Gantry query records, run with no authority on file, place her "
                      "van on the depot approach at 02:20 on each of the three "
                      "mornings the tanks were drained."))),
    "railquery": dict(
        d="Yusuf Demirci", charge="the snatching of the courier bag",
        setting=("A courier bag containing a tender file was taken at the terminus, and "
                 "the thief was caught on no fixed camera."),
        neutral=["The bag was booked out at 18:35.",
                 "The 18:40 service was the last that reached the north line."],
        reason="were obtained from the rail account through a query with no legal basis",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="decrease", label="the gate scan records",
                text=("Gate scans pulled from the rail account with no legal basis "
                      "place him on the 18:40 northbound service, already through the "
                      "barrier before the bag was ever booked out."))),
    "dashfront": dict(
        d="Corin Vale", charge="the wounding of the night porter",
        setting=("A porter was cut outside a depot canteen at the end of the late "
                 "shift, and the layby outside was said to be where the row started."),
        neutral=["The canteen door was propped during the break.",
                 "Two clocks in the canteen ran four minutes apart."],
        reason="was taken from the vehicle without any lawful process",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="decrease", label="the dashcam file",
                text=("The dashcam file taken without lawful process records his car "
                      "standing in the layby with the engine off for the whole of the "
                      "break, and pulling away only after the shift whistle."))),
    "observatory": dict(
        d="Nadia Sorensen", charge="the theft of the observatory telescope",
        setting=("A volunteer-run observatory lost its main telescope from a bolted "
                 "mount, and the dome was found unlocked in the morning."),
        neutral=["Only two volunteers held the dome key.",
                 "The mount bolts had been cut, not unscrewed."],
        reason="was discovered in a backyard search that exceeded every warrant "
               "condition",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="increase", label="the telescope tube assembly",
                text=("Photographs from the over-broad backyard search show the "
                      "observatory's tube assembly leaning against her shed wall, "
                      "its finder scope still bearing the volunteer society's "
                      "engraved asset number."))),
    "memorialplaques": dict(
        d="Otto Grimaldi", charge="the theft of the memorial plaques",
        setting=("Bronze plaques were levered from the memorial garden overnight, and "
                 "the fixings were left in a neat pile."),
        neutral=["The garden backs onto a builder's yard.",
                 "The plaques weighed about twelve kilos each."],
        reason="were seized from the vehicle without a warrant or exigency",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="increase", label="the sidewall compartment photographs",
                text=("Photographs taken when his van's sidewall compartment was "
                      "prised open without a warrant show all four plaques wrapped in "
                      "site sheeting, the memorial's bolt holes still bright."))),
    "agenttext": dict(
        d="Lucia Marchetti", charge="harassing the site agent",
        setting=("A site agent received forty messages in three weeks about a boundary "
                 "dispute that had already been through survey."),
        neutral=["The agent had asked for contact only through the solicitor.",
                 "The survey line was fixed the previous autumn."],
        reason="was taken from her handset without a warrant",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="decrease", label="the extracted message thread",
                text=("The thread extracted without a warrant shows her proposing, in "
                      "the first week, a single supervised site meeting and accepting "
                      "the surveyor's line in writing before the messages began to "
                      "multiply."))),
    "shutterbreak": dict(
        d="Kwame Adjei", charge="the breaking of the shop shutters",
        setting=("Two shopfront shutters on the parade were bent at the base plate, and "
                 "the repair quote ran into thousands."),
        neutral=["The parade had four cameras, one of them aimed at the crossing.",
                 "The shutters were keyed to a single alarm zone."],
        reason="was taken from the neighbouring shop's system by a constable with "
               "no authority to take it",
        exclusion_reason="procedural_illegality",
        ev=dict(direction="decrease", label="the shutter camera export",
                text=("The export a constable took from the neighbouring shop's system "
                      "without authority shows a second figure already at the base "
                      "plate, wrench in hand, ninety seconds before the defendant "
                      "reaches the parade."))),

    # --- epistemic_invalidation: the method the court distrusted --------------
    "photoarray": dict(
        d="Rafael Iturbide", charge="the theft of the showroom display models",
        setting=("A showroom lost four display models from a locked case, and the "
                 "cleaners found the case key still in the lock."),
        neutral=["The alarm was bypassed with the correct code.",
                 "The models were insured for retail value."],
        reason="rests on an array the court found suggestive",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="increase", label="the witness identification",
                text=("The assistant's identification places him at the case at closing "
                      "time, picked from an array in which his photograph was the only "
                      "one taken on a camera of a different make."))),
    "labbatch": dict(
        d="Imogen Strait", charge="the contamination of the reservoir",
        setting=("A village reservoir recorded an algal toxin spike, and the intake "
                 "serving thirty houses was closed for a week."),
        neutral=["The intake draws from the northern end.",
                 "Two treatment cycles ran before the closure."],
        reason="comes from a run the laboratory's own review found to be outside the "
               "validated method",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="increase", label="the chromatography report",
                text=("The chromatography report shows toxin levels eleven times the "
                      "alert threshold in a sample drawn at the intake, run on a "
                      "column the laboratory's own review had already marked as past "
                      "its service life."))),
    "signature": dict(
        d="Emil Dabrowski", charge="forging the authority to collect the freight",
        setting=("A shipping agent released four pallets against an authority that "
                 "turned out to be signed by nobody on the account."),
        neutral=["The release was countersigned at the depot office.",
                 "The pallets were already on the outbound trailer."],
        reason="was made without the blind samples the method requires",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="increase", label="the signature comparison",
                text=("The signature comparison reports that the authority's flourish "
                      "matches his confirmed writing, carried out without the blind "
                      "samples the method requires and against exemplars copied from "
                      "the same contested form."))),
    "alibiphone": dict(
        d="Giorgio Ranieri", charge="the break-in at the medical centre",
        setting=("A medical centre was broken into over a bank holiday, and the drug "
                 "cupboard was emptied but the safe untouched."),
        neutral=["The rear fire door was found propped.",
                 "The alarm log showed a code entered after the closing cycle."],
        reason="rests on a method the court found unreliable",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="decrease", label="the cell-site analysis",
                text=("The cell-site analysis places his handset eight kilometres away "
                      "at the time of the entry, an analysis run on a lookup table so "
                      "outdated that the court refused the method altogether."))),
    "breathsample": dict(
        d="Fionnuala Keane", charge="the collision at the ferry ramp",
        setting=("One car was written off at a ferry ramp in the early hours, and the "
                 "driver was given a breath test at the roadside."),
        neutral=["The ramp was wet from an hour of rain.",
                 "The second vehicle had exited the ramp lane."],
        reason="derives from a reading taken without the blank sample the instrument "
               "protocol requires",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="increase", label="the intoxilyzer printout",
                text=("The intoxilyzer printout records a reading well over the limit, "
                      "taken without the blank sample the instrument protocol requires "
                      "and printed before the control breath had been run."))),
    "pollenquote": dict(
        d="Soren Halvorsen", charge="the break-in at the bell tower",
        setting=("The bell tower's vestry door was forced at the weekend, and the "
                 "collection box was emptied."),
        neutral=["Access to the tower was by one external stair.",
                 "The parish had just re-hung the bells."],
        reason="rests on species calls the court found methodologically unsound",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="decrease", label="the pollen comparison",
                text=("The pollen comparison reports a coastal soil profile on his "
                      "field jacket, a comparison so confused between the two "
                      "candidate species that the court would not hear it, and which "
                      "in any case matches ground thirty kilometres from the "
                      "tower."))),
    "daysail": dict(
        d="Margot Pellerin", charge="the inflated insurance claim on the day boat",
        setting=("A day boat was declared a total loss after a summer mooring fire, "
                 "and the claim was filed the same week."),
        neutral=["The hull had been surveyed twice in five years.",
                 "The mooring was on the eastern pontoon."],
        reason="rests on a table the court found to have been withdrawn from the "
               "method",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="decrease", label="the surveyor's valuation",
                text=("The surveyor's valuation puts the hull at less than a third of "
                      "the claimed figure, a figure drawn by a depreciation table the "
                      "expert had been told was withdrawn from the method."))),
    "voiceprint": dict(
        d="Dmitri Vasquez", charge="the threatening calls to the publisher",
        setting=("A publisher's office took eleven silent calls followed by one that "
                 "named an editor and a home address."),
        neutral=["The calls came from six withheld numbers.",
                 "The office line recorded the audio automatically."],
        reason="was produced by a unit without valid accreditation",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="increase", label="the voice comparison",
                text=("The voice comparison reports that the recording naming the "
                      "editor's address carries his speaker signature, run by a unit "
                      "whose accreditation had lapsed before the analysis was "
                      "commissioned."))),
    "hairmatch": dict(
        d="Ingrid Solberg", charge="the cutting of the parking attendant",
        setting=("An attendant was cut during an argument at the barrier, and the "
                 "forensic suite was asked about a single hair."),
        neutral=["The jacket had been in storage for a month.",
                 "The cut required eleven stitches."],
        reason="was carried out without any control sample",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="increase", label="the hair comparison",
                text=("The hair comparison reports that a shaft found under the "
                      "attendant's collar is consistent with hers, a comparison done "
                      "against photographs alone, with no control sample ever "
                      "taken."))),
    "shoeprint": dict(
        d="Anselm Brandt", charge="the break-in at the lift machine room",
        setting=("The lift machine room was forced from the fire lobby, and the "
                 "controller board was lifted out."),
        neutral=["The lobby camera had been unplugged at the panel.",
                 "The board serial matched the maintenance register."],
        reason="was made by an examiner no longer certified",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="increase", label="the tread comparison",
                text=("The tread comparison reports that the impression in the lobby "
                      "dust carries his boot's tread pattern, matched by an examiner "
                      "whose certification had ended before the comparison was "
                      "signed."))),
    "fundmisuse": dict(
        d="Cassia Oyelowo", charge="the misuse of the discretionary fund",
        setting=("A department's discretionary fund ran a deficit for the year, and "
                 "the audit traced it to a run of single-name reimbursements."),
        neutral=["The fund limit had been cut in the spring.",
                 "Reimbursements required a second approver."],
        reason="rests on a document dating analysis whose reference database was "
               "withdrawn",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="decrease", label="the ink dating report",
                text=("The ink dating report places the reimbursement forms before the "
                      "fund limit was cut, an analysis run against a reference "
                      "database the laboratory had already withdrawn from "
                      "service."))),
    "scanquality": dict(
        d="Piotr Lindqvist", charge="the passport fraud at the border",
        setting=("A passport was presented at an e-gate that refused it, and the "
                 "traveller was referred to a desk."),
        neutral=["The gate kept the refused document.",
                 "The booking was in a name the passport had never held."],
        reason="rests on a face match validated on a sample that excluded this "
               "population",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="increase", label="the facial comparison",
                text=("The facial comparison reports a match above the system's own "
                      "threshold against the gate capture, a score from a model whose "
                      "validation sample had excluded the very population the "
                      "defendant belongs to."))),
    "chartreview": dict(
        d="Beatrix Halloran", charge="falsifying the patient rota",
        setting=("A ward rota was edited after the fact to show cover that the ward "
                 "clerk says never existed, and one night ran two nurses short."),
        neutral=["The rota was exported as a PDF each Friday.",
                 "The shortfall was found during an inspection."],
        reason="rests on source data the court found was migrated in error",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="decrease", label="the rota analysis",
                text=("The rota analysis reports that every edit attributed to her "
                      "account came from an automated import, a conclusion the court "
                      "could not use only because the vendor's own migration had "
                      "corrupted the timestamps."))),
    "tyreage": dict(
        d="Rurik Amancio", charge="the brake-failure cover-up",
        setting=("A delivery van went through a barrier after its brakes failed, and "
                 "the maintenance file showed a fluid change four days earlier."),
        neutral=["The workshop was contracted, not in-house.",
                 "The fluid bottle had no batch label."],
        reason="was performed without the blank the protocol requires",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="decrease", label="the fluid analysis",
                text=("The fluid analysis reports the reservoir fluid as dry and "
                      "uncontaminated, tested without a blank and against a control "
                      "the technician had already noted as spent."))),
    "staffpass": dict(
        d="Talia Bregman", charge="forging the staff passes",
        setting=("A building's access control logged four entries by a pass that was "
                 "never issued, and the store room was picked over."),
        neutral=["Pass numbers were printed in batches of fifty.",
                 "The store room held the demo stock."],
        reason="was carried out by a bureau whose accreditation had lapsed",
        exclusion_reason="epistemic_invalidation",
        ev=dict(direction="increase", label="the pass material analysis",
                text=("The pass material analysis reports that the holographic layer "
                      "matches a batch ordered against her account alone, tested by a "
                      "bureau whose accreditation had lapsed the month before the "
                      "examination."))),

    # --- access_control: taken by someone without authorized access -----------
    "waitinglist": dict(
        d="Priya Ramanathan", charge="manipulating the ward waiting list",
        setting=("A ward's priority scores changed for six patients after the list was "
                 "locked, and one appointment moved ahead of three others."),
        neutral=["Score changes were supposed to need two clinicians.",
                 "The lock was applied on the Tuesday."],
        reason="was pulled from the record system by a clerk with no access to "
               "clinical entries",
        exclusion_reason="access_control",
        ev=dict(direction="decrease", label="the login audit trail",
                text=("The audit trail a ward clerk pulled from the system without "
                      "clinical access rights shows every one of the six edits "
                      "arriving from a different account, hours after her own session "
                      "had closed."))),
    "customerdb": dict(
        d="Felix Amherst", charge="copying the customer database",
        setting=("A loyalty provider found its customer table mirrored to an outside "
                 "drive, and the export landed on a competitor's servers."),
        neutral=["His notice period was four weeks.",
                 "The table held two million rows."],
        reason="were retrieved from a backup share his account had never been removed "
               "from",
        exclusion_reason="access_control",
        ev=dict(direction="increase", label="the backup export logs",
                text=("The backup export logs show his account pulling the full "
                      "customer table twice a night for eleven nights, from a share "
                      "his access rights should have lost when his role changed."))),
    "barriercodes": dict(
        d="Noor Haddad", charge="the theft of the car park takings",
        setting=("A multi-storey's takings bag went missing from the pay office, and "
                 "the barrier log was the only record of who left that night."),
        neutral=["One exit barrier ran on a code list separate from the gates.",
                 "The office was cleared after the 23:00 sweep."],
        reason="was taken from the barrier system by an engineer whose account had "
               "already expired",
        exclusion_reason="access_control",
        ev=dict(direction="decrease", label="the barrier code audit",
                text=("The barrier code audit, pulled by a contractor whose account had "
                      "already expired, shows his exit at 19:05, well before the "
                      "office was cleared and the bag lifted."))),
    "mailboxpull": dict(
        d="Gustavo Reyn", charge="intercepting the dividend notices",
        setting=("A transfer agent found forty dividend notices redirected before "
                 "they reached the registered holders."),
        neutral=["Redirects required a signed form.",
                 "The batch was printed on a Friday."],
        reason="was taken from the operations console by a temporary clerk with "
               "view-only rights",
        exclusion_reason="access_control",
        ev=dict(direction="increase", label="the redirect export log",
                text=("The redirect export log shows his temp account creating all "
                      "forty redirects in one sitting, from a console that was "
                      "supposed to give him nothing but the ability to look."))),
    "gitarchive": dict(
        d="Wen Zhao", charge="copying the design files",
        setting=("A hardware firm found its unreleased board layouts on a public "
                 "repository two days before the launch."),
        neutral=["The repository held fourteen years of history.",
                 "Access was by team, not by project."],
        reason="was archived by an account whose admin rights should have lapsed "
               "with his role change",
        exclusion_reason="access_control",
        ev=dict(direction="increase", label="the repository export log",
                text=("The repository export log records his account taking a full "
                      "archive of the board history on the same night the repository "
                      "was mirrored, from permissions his downgrade was meant to "
                      "remove."))),
    "schoolportal": dict(
        d="Delphine Aubert", charge="altering the catchment addresses",
        setting=("Five families were placed outside their catchment after the address "
                 "field changed on the admissions portal."),
        neutral=["Address changes had to be evidenced by a bill.",
                 "The offers went out on the Thursday."],
        reason="was read from the portal by a parent account holding no admissions "
               "rights",
        exclusion_reason="access_control",
        ev=dict(direction="decrease", label="the portal change log",
                text=("The portal change log a parent pulled without admissions rights "
                      "shows all five address edits coming from a superseded account "
                      "belonging to the previous year's administrator."))),
    "depositbox": dict(
        d="Cosima Vandermeer", charge="the theft of the deposit box contents",
        setting=("A bank's vault corridor was entered out of hours and one box in the "
                 "northern range was cut open."),
        neutral=["The corridor required a key and a code.",
                 "The cutting kit came from the maintenance bench."],
        reason="was taken from the keycard system by a former supervisor no longer on "
               "the authorized list",
        exclusion_reason="access_control",
        ev=dict(direction="increase", label="the keycard audit",
                text=("The keycard audit, exported by a security supervisor who had "
                      "left the bank's authorized list a month earlier, shows his "
                      "card opening the vault corridor at 02:14 with no attendant "
                      "sign-in."))),
    "payrollview": dict(
        d="Halima Sekibo", charge="the discrepancy in the payroll run",
        setting=("A payroll run produced a gap of several thousand between the clock "
                 "file and the paid file, and one line item was hand-entered."),
        neutral=["Payroll was locked each second Wednesday.",
                 "The clock file imported automatically."],
        reason="was read from the payroll table by a supervisor with no payroll rights",
        exclusion_reason="access_control",
        ev=dict(direction="decrease", label="the payroll entry log",
                text=("The payroll entry log a supervisor pulled without payroll rights "
                      "shows the hand-entered line arriving straight from the "
                      "clock-file import, timestamped before anyone in the office "
                      "opened the run."))),
    "dvrcfg": dict(
        d="Bettina Krause", charge="the deletion of the yard's footage",
        setting=("A haulage yard's recorder was found wiped the morning after a "
                 "container went missing, and the insurer wanted an explanation."),
        neutral=["The recorder was a forty-eight channel unit.",
                 "Storage was set to a rolling cycle."],
        reason="was captured from the recorder by an off-duty officer with no rights "
               "on the system",
        exclusion_reason="access_control",
        ev=dict(direction="decrease", label="the recorder configuration snapshot",
                text=("A configuration snapshot an off-duty officer pulled without any "
                      "rights on the system shows the recorder had run a twenty-four "
                      "hour rolling cycle all along, so the gap was the cycle "
                      "turning over, not a wipe."))),
    "refundlog": dict(
        d="Marisol Etxeberria", charge="the refund scam at the returns desk",
        setting=("A store's refunds totalled three times the seasonal average, and "
                 "every anomalous refund cleared through one till code."),
        neutral=["Refunds above fifty required a supervisor.",
                 "The desk closed at 20:30."],
        reason="was taken from a till login kept after the shift change",
        exclusion_reason="access_control",
        ev=dict(direction="increase", label="the refund query log",
                text=("The refund query log shows his login raising every anomalous "
                      "refund in the last hour of trade, from a till session that "
                      "should have been closed the moment the shift changed."))),
    "allotment": dict(
        d="Iestyn Prothero", charge="the fraudulent transfer of the allotment lease",
        setting=("An allotment lease was moved to a new holder without the waiting "
                 "list being run, and the prior holder never asked for a transfer."),
        neutral=["The waiting list ran to thirty names.",
                 "Transfers needed the committee's minute."],
        reason="was read from the register by a neighbour's shared login",
        exclusion_reason="access_control",
        ev=dict(direction="decrease", label="the register change history",
                text=("The register change history, read by a neighbour through a "
                      "shared login, shows the transfer applied by the registry's own "
                      "migration account on the night the register was rebuilt."))),
    "calibration": dict(
        d="Sung-min Park", charge="the taking of the calibration kits",
        setting=("A test lab found four calibration kits missing from the store, and "
                 "the checkout board showed nothing outstanding."),
        neutral=["Kits were signed out against job numbers.",
                 "The store was re-keyed in the spring."],
        reason="was taken from the inventory app through a session that was never "
               "revoked",
        exclusion_reason="access_control",
        ev=dict(direction="increase", label="the inventory checkout log",
                text=("The inventory checkout log shows his account signing out all "
                      "four kits against job numbers that were closed the week "
                      "before, from a session that had never been revoked."))),
    "exclusionzone": dict(
        d="Anaïs Lefevre", charge="breaching the exclusion zone",
        setting=("A man was arrested inside a cordon three nights running, and the "
                 "complainant's account put him at the gate each time."),
        neutral=["The cordon covered one street end.",
                 "The gate had an intercom log."],
        reason="was read from the door-entry system by a tenant with no rights over "
               "the log",
        exclusion_reason="access_control",
        ev=dict(direction="decrease", label="the door-entry call log",
                text=("The door-entry call log, read by a tenant association member "
                      "who held no rights over it, shows the complainant calling his "
                      "intercom first on all three nights, inviting him into the "
                      "cordon."))),
    "bankfeed": dict(
        d="Ragnar Thorsen", charge="the diversion of the subscription money",
        setting=("A club's subscription income went missing over a quarter, and the "
                 "standing orders now ran to an account nobody recognised."),
        neutral=["Subscriptions were collected by direct debit.",
                 "The treasurer had given notice in January."],
        reason="was taken from the ledger by a bookkeeper after her access was "
               "revoked",
        exclusion_reason="access_control",
        ev=dict(direction="increase", label="the account feed export",
                text=("The account feed export shows the standing orders rerouted to a "
                      "joint account he co-signs, downloaded by a bookkeeper whose "
                      "access had been revoked two weeks earlier."))),
    "hrletter": dict(
        d="Zsófia Kertész", charge="disclosing the disciplinary note",
        setting=("A disciplinary note reached a staff newsletter, and the panel's "
                 "findings were supposed to stay in the file."),
        neutral=["The note was closed as unsubstantiated.",
                 "Only five people held the file."],
        reason="was read from the personnel file by a manager whose file access had "
               "been withdrawn",
        exclusion_reason="access_control",
        ev=dict(direction="decrease", label="the disciplinary file entry",
                text=("The disciplinary file entry, read by a manager whose access had "
                      "been withdrawn, records the matter as closed and "
                      "unsubstantiated weeks before anything appeared in the "
                      "newsletter."))),

    # --- temporal_irrelevance: outside the period or issue in charge -----------
    "brassfittings": dict(
        d="Aleksy Nowak", charge="the theft of the depot's brass fittings",
        setting=("Brass fittings vanished from the depot over a signed-off inventory "
                 "period, and the store was re-counted twice."),
        neutral=["The charged period covered one financial quarter.",
                 "The fittings were bagged by type."],
        reason="concern movements from a later period that is not in issue",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="increase", label="the subsequent stock records",
                text=("The subsequent stock records, covering months after the charged "
                      "quarter, show the same station short by the same bagged "
                      "fittings on every later count."))),
    "overtime": dict(
        d="Camille Okafor", charge="the false overtime approvals",
        setting=("A depot's overtime bill doubled in the audited quarter, and one "
                 "supervisor's signature appeared on the peak weeks."),
        neutral=["The audit covered April to June.",
                 "Overtime needed a next-day sign-off."],
        reason="concern a quarter outside the audit",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="increase", label="the following-quarter approvals",
                text=("The following-quarter approvals, from a period the audit never "
                      "covered, carry the same signature over the same pattern of "
                      "next-day sign-offs."))),
    "meter": dict(
        d="Erik Haldorsen", charge="meter tampering at the substation",
        setting=("A substation's meter logged a step change in consumption that the "
                 "operator could not tie to any load."),
        neutral=["The charged period began in October.",
                 "The meter was swapped in December."],
        reason="concern months after the period charged",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="increase", label="the post-cutoff consumption records",
                text=("The post-cutoff consumption records, from after the period "
                      "charged, show the same irregular draw continuing on the same "
                      "nightly schedule."))),
    "shrinkage": dict(
        d="Beatriz Salgado", charge="the shrinkage in the stockroom",
        setting=("Stock counts at one station came up short each cycle, and the "
                 "station had a single named operator."),
        neutral=["Counts ran fortnightly.",
                 "The charged cycles covered eight weeks."],
        reason="concern weeks after the charged period",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="increase", label="the later cycle counts",
                text=("The later cycle counts, from weeks the charge never mentions, "
                      "keep showing the shortfall at her station alone while every "
                      "other station balances."))),
    "addressform": dict(
        d="Kofi Mensah", charge="the false address on the application",
        setting=("An application was granted on an address that did not exist, and the "
                 "grant was later withdrawn."),
        neutral=["Verification was by postcode alone.",
                 "The grant ran for one term."],
        reason="concern filings that are not before the court",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="increase", label="the later applications",
                text=("Two later applications a year after the charged one repeat the "
                      "same false address word for word, in filings that are not "
                      "before the court."))),
    "pettycash": dict(
        d="Ondine Castellanos", charge="the diversion of the petty cash",
        setting=("A site's petty cash float came up short over one month, and the "
                 "custodian was the only key holder."),
        neutral=["The float was counted on Fridays.",
                 "Vouchers were kept in a tin."],
        reason="concern an earlier year that is not in issue",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="decrease", label="the prior-year audit sheets",
                text=("The prior-year audit sheets, from a year the charge never "
                      "covers, close every one of her Friday counts to the penny "
                      "with the vouchers to match."))),
    "stockcount": dict(
        d="Théodore Mercier", charge="the inventory shortfall at the depot",
        setting=("A depot's year-end count fell short of the ledger, and one bay was "
                 "the centre of the discrepancy."),
        neutral=["The charged count was the December one.",
                 "Bays were reassigned each quarter."],
        reason="concern counts taken before the period charged",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="decrease", label="the earlier stock counts",
                text=("The earlier stock counts, from months before the charged "
                      "period, balance his bay exactly on every occasion he signed "
                      "for it."))),
    "plantcontam": dict(
        d="Grete Lindahl", charge="the contamination at the plant",
        setting=("A batch line was shut after a contaminant was found at the filler, "
                 "and the line had run unattended overnight."),
        neutral=["The charged night was a Tuesday.",
                 "Swabs were taken after the purge."],
        reason="concerns readings from the week before the charged night",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="decrease", label="the previous inspection cycle",
                text=("The previous inspection cycle, from the week before the "
                      "charged night, records every filler reading inside tolerance "
                      "on her watch."))),
    "stall": dict(
        d="Amadou Diallo", charge="the under-declared takings at the stall",
        setting=("A market stall's declared takings ran below the pitch's average, and "
                 "the pitch fee was due monthly."),
        neutral=["The charged quarter covered the winter months.",
                 "Card sales were reported separately."],
        reason="concerns a month before the quarter charged",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="decrease", label="the preceding month's takings sheet",
                text=("The preceding month's takings sheet, from before the quarter "
                      "charged, declares takings above the pitch average with the "
                      "card slips attached."))),
    "traininglog": dict(
        d="Iwona Zielinska", charge="the forgery of the safety certificate",
        setting=("A forklift certificate was found to be a copy, and the operator had "
                 "been signed off for the summer season."),
        neutral=["The certificate was checked at the gate.",
                 "The charged season ran from June."],
        reason="concerns a period not before the court",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="decrease", label="the earlier training log",
                text=("The earlier training log, from the year before the charged "
                      "season, signs her through the full course with the "
                      "instructor's own assessment sheets attached."))),
    "voidsales": dict(
        d="Josip Novak", charge="the voided sales at the till",
        setting=("One till produced three times the normal number of voids, and the "
                 "float was short at close."),
        neutral=["Voids above twenty needed a key.",
                 "The charged weeks covered the sale period."],
        reason="concern weeks before the weeks charged",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="decrease", label="the earlier void logs",
                text=("The earlier void logs, from the weeks before the charge, show "
                      "his void rate sitting under the store average with every key "
                      "use accounted for."))),
    "forfeiture": dict(
        d="Elias Whitcombe", charge="the deposit forfeiture fraud",
        setting=("Four tenant deposits were withheld at the end of tenancies that all "
                 "ended within one quarter."),
        neutral=["Deposits were held in a scheme.",
                 "Check-out reports were emailed the same day."],
        reason="concerns a term that is not in issue",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="decrease", label="the earlier tenancy file",
                text=("The earlier tenancy file, from a term the charge never covers, "
                      "releases every deposit in full with the check-out photographs "
                      "attached."))),
    "calibyear": dict(
        d="Nadine Ekwueme", charge="the false calibration readings",
        setting=("Calibration sheets were signed off with readings that did not match "
                 "the bench, and the instruments went out to customers."),
        neutral=["The charged sheets covered one quarter.",
                 "Certificates carried a serial each."],
        reason="concern a year outside the charge",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="decrease", label="the prior-year calibration certificates",
                text=("The prior-year calibration certificates, from outside the "
                      "charged period, carry bench values that reproduce within a "
                      "hundredth on every instrument he signed for."))),
    "servicetimes": dict(
        d="Ravi Chandrasekar", charge="the manipulation of the service times",
        setting=("A contractor's logged response times fell below the contract floor "
                 "for one billing period, and the log was edited."),
        neutral=["The floor was fifteen minutes.",
                 "The charged period covered one invoice."],
        reason="concern a period before the invoice charged",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="decrease", label="the earlier call logs",
                text=("The earlier call logs, from before the invoice period charged, "
                      "show his crew holding a median response well above the "
                      "contract floor on every shift."))),
    "cleanroute": dict(
        d="Matti Virtanen", charge="the diversion of the delivery run",
        setting=("A delivery run was logged as completed while the goods reached one "
                 "address only, and the discrepancy spanned a single week."),
        neutral=["Routes were closed by handheld at drop.",
                 "The charged week was the second of the month."],
        reason="concern weeks after the week charged",
        exclusion_reason="temporal_irrelevance",
        ev=dict(direction="decrease", label="the later route records",
                text=("The later route records, from the weeks after the week charged, "
                      "close every drop against a signature with the handheld "
                      "sequence intact."))),
}


def build() -> list[Item]:
    out = []
    for case, f in LEGAL_CASES.items():
        base = (f["setting"] + " The defendant is charged with " + f["charge"]
                + ". The following is established:\n"
                + "\n".join("- " + s for s in f["neutral"]))
        ev = f["ev"]
        label = ev["label"]
        out.append(Item(
            item_id=f"g23b_legal_{case}",
            task_family="legal_judgment", surface_domain=case,
            base_context=base,
            critical_evidence=ev["text"],
            critical_label=label,
            critical_direction=ev["direction"],
            exclusion_reason=f["exclusion_reason"],
            evidence_truth="true_but_forbidden",
            admit_rule=ADMIT_TMPL.format(label=label),
            exclude_rule=EXCLUDE_TMPL.format(label=label, reason=f["reason"]),
            question=QUESTION_LEGAL,
            output_spec=OUTPUT_SPEC,
            memory_question=MEMORY_TMPL.format(label=label),
            rule_probe_question=PROBE_TMPL.format(label=label),
            meta={"case": case, "skeleton": f"legal:{case}"}))
    return out


def check_fresh(items: list[Item], root: str) -> None:
    """Nothing from G0 / G18 / G23A may reappear, by id, surface case or skeleton."""
    old_ids, old_domains, old_skeletons = set(), set(), set()
    for name in ("items_v1.jsonl", "g18_v1.jsonl", "linear_v1.jsonl", "g23a_v1.jsonl"):
        path = os.path.join(root, "data/items", name)
        if not os.path.exists(path):
            continue
        with open(path) as handle:
            for line in handle:
                row = json.loads(line)
                old_ids.add(row["item_id"])
                old_domains.add(row["surface_domain"])
                skel = (row.get("meta") or {}).get("skeleton")
                if skel:
                    old_skeletons.add(skel)
                if row.get("meta", {}).get("case"):
                    old_skeletons.add(row["meta"]["case"])

    ids = {i.item_id for i in items}
    domains = {i.surface_domain for i in items}
    skeletons = {i.meta["skeleton"] for i in items}
    assert not (ids & old_ids), f"item id collision: {ids & old_ids}"
    assert not (domains & old_domains), f"domain collision: {domains & old_domains}"
    assert not (skeletons & old_skeletons), \
        f"skeleton collision: {skeletons & old_skeletons}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data/items/g23b_v1.jsonl")
    args = ap.parse_args()
    items = build()

    # structural promises the preregistration makes about the materials
    from collections import Counter
    assert len(items) == 60, len(items)
    assert Counter(i.task_family for i in items) == {"legal_judgment": 60}
    dirs = Counter(i.critical_direction for i in items)
    assert dirs == {"increase": 30, "decrease": 30}, dict(dirs)
    assert len({i.meta["skeleton"] for i in items}) == 60, "one item per skeleton"
    reasons = Counter(i.exclusion_reason for i in items)
    assert len(reasons) == 4 and min(reasons.values()) >= 8, dict(reasons)
    labels = [i.critical_label for i in items]
    assert len(set(labels)) == 60, "one evidence label per item"
    for i in items:
        assert i.ground_truth is None, i.item_id          # no LLM gold, no judge
        assert len(i.base_context) >= 120, i.item_id
        assert i.critical_evidence, i.item_id
        assert i.evidence_truth == "true_but_forbidden", i.item_id

    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    check_fresh(items, root)

    path = os.path.join(root, args.out)
    with open(path, "w") as handle:
        for item in items:
            handle.write(item.to_json() + "\n")
    print(f"wrote {len(items)} items -> {args.out}")
    print(f"  directions {dict(dirs)}")
    print(f"  exclusion reasons {dict(reasons)}")


if __name__ == "__main__":
    main()
