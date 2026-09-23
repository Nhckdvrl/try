"""G23A — fresh items for the weighting-vs-gating confirmation.

Three naturalistic families with continuous judgments, **one item per independent
skeleton**, 72 items over 72 skeletons (24 per family), directions mixed inside
every family so no requested weight can win by pushing ratings one way.

Nothing here is inherited. Every case, diagnostic domain and selection scenario
is new: none of the 32 legal skeletons, 20 inference domains and 20 selection
scenarios in `items_v1.jsonl` / `g18_v1.jsonl` / `linear_v1.jsonl` reappears,
asserted at build time on item id, surface domain and skeleton.

No LLM writes any of this and no LLM grades it — there is no gold label. The
judgment is the model's own rating; the only requirement the design places on an
item is that its evidence push that rating in a known direction, which is what
the signed-leverage criterion checks at analysis time.

    PYTHONPATH=src python3 src/gen_g23a.py --out data/items/g23a_v1.jsonl
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from schema import Item  # noqa: E402

OUTPUT_SPEC = ("Use a scale from 0 to 9, where 0 means certainly not and 9 means "
               "certainly so.")

ADMIT_RULE = ("RULING\nThe causal weight assigned to {label} is exactly 100% of its "
              "normal evidential weight.")
EXCLUDE_RULE = ("RULING\nThe causal weight assigned to {label} is exactly 0% of its "
                "normal evidential weight.")

QUESTION_LEGAL = ("Considering the case, rate the probability that the defendant is "
                  "guilty of the charge.")


# ---------------------------------------------------------------------------
# Legal judgment — 24 new case skeletons, 12 incriminating / 12 exculpatory
# ---------------------------------------------------------------------------
# Each case supplies its own evidence; `direction` is what that evidence does to
# the guilt rating when it is fully admitted.
LEGAL_CASES = {
    "berthfire": dict(
        d="Marcus Hale", charge="starting the fire to claim on the policy",
        setting=("A fire broke out in a bonded warehouse on the eastern quay. Marcus "
                 "Hale held the night supervisor role for the building."),
        neutral=["The lease on the warehouse ran to a further four years.",
                 "Two night porters were on the adjacent site."],
        ev=dict(direction="increase", label="the security footage",
                text=("Security footage from the quay gate shows Hale entering the "
                      "warehouse alone at 02:10, twenty minutes before the first "
                      "alarm, and the same camera records him leaving by the fire exit "
                      "while the loading shutter was still closed."))),
    "grantclaim": dict(
        d="Ines Barros", charge="submitting false completion records to obtain the grant",
        setting=("A regional development grant was paid to a training company that "
                 "closed without delivering the programme. Ines Barros signed the "
                 "completion certificates."),
        neutral=["The grant was paid in two instalments.",
                 "The company had traded for six years before the award."],
        ev=dict(direction="increase", label="the completion certificates",
                text=("An audit of the completion certificates found that forty-one of "
                      "the sixty signatures came from a single scanner batch created "
                      "three weeks after the first grant payment cleared."))),
    "exchangeledger": dict(
        d="Devon Ackroyd", charge="diverting exchange seats to buyers outside the queue",
        setting=("A club's season-ticket exchange was investigated after members "
                 "reported that desirable seats never reached the waiting list. Devon "
                 "Ackroyd administered the exchange."),
        neutral=["The waiting list ran to several thousand members.",
                 "Exchanges were supposed to close two weeks before the season."],
        ev=dict(direction="increase", label="the exchange ledger",
                text=("The exchange ledger shows ninety-four seats transferred to buyer "
                      "accounts registered at the same office address as a ticket "
                      "broker, each processed minutes after the queue opened."))),
    "pipelinespill": dict(
        d="Noor Haddad", charge="falsifying the pipeline integrity checks",
        setting=("A fertiliser spill reached the river after a pipeline joint failed. "
                 "Noor Haddad signed off the weekly integrity checks."),
        neutral=["The line had operated for nineteen years without a major release.",
                 "Two contractors worked on the section that spring."],
        ev=dict(direction="increase", label="the integrity check sheets",
                text=("The signed check sheets record a successful pressure test at "
                      "09:40, but the site's own SCADA log shows the test pump was "
                      "isolated for repair at that time and did not restart until "
                      "late afternoon."))),
    "duesaccount": dict(
        d="Gerald Amaechi", charge="transferring members' dues to a personal account",
        setting=("A union branch found a shortfall in its dues account. Gerald "
                 "Amaechi was the branch treasurer."),
        neutral=["Dues were collected by standing order from about eight hundred members.",
                 "The branch employed one part-time administrator."],
        ev=dict(direction="increase", label="the transfer records",
                text=("The bank's transfer records show eleven payments to an account "
                      "in Amaechi's own name, each just under the amount that would "
                      "have required a second signatory, made on the days dues were "
                      "banked."))),
    "importduty": dict(
        d="Wei Lam", charge="undervaluing imported goods to avoid duty",
        setting=("A customs review of an electronics importer found repeated "
                 "undervaluation. Wei Lam prepared the declarations."),
        neutral=["The company imported forty containers in the period concerned.",
                 "Broker fees were paid at a flat rate per entry."],
        ev=dict(direction="increase", label="the customs declarations",
                text=("The declared unit prices on the declarations are between a "
                      "quarter and a third of the prices the same factory charged the "
                      "company's sister operation for identical models in the same "
                      "months."))),
    "soilreport": dict(
        d="Petra Nilsen", charge="reporting analyses that were never run",
        setting=("A contract laboratory reported unusually favourable soil results for "
                 "a housing site. Petra Nilsen ran the analyses."),
        neutral=["The laboratory held the contract for four sites that year.",
                 "Turnaround was contracted at five working days."],
        ev=dict(direction="increase", label="the instrument logs",
                text=("The instrument logs show no run against the submitted sample "
                      "identifiers at all, while the sequence numbers on the reports "
                      "correspond to samples submitted by a different client the same "
                      "week."))),
    "scholarships": dict(
        d="Tomas Ferreira", charge="awarding scholarships on falsified scoring",
        setting=("A scholarship panel awarded places to applicants scored by an "
                 "external consultant. Tomas Ferreira chaired the panel."),
        neutral=["The fund supported twelve places a year.",
                 "Panel members declared no conflicts at the meeting."],
        ev=dict(direction="increase", label="the scoring sheets",
                text=("The scoring sheets carry a single pen throughout, but the "
                      "handwriting comparison identifies the entries for the six "
                      "successful applicants as written at a different time from the "
                      "rest and over ruled margin lines."))),
    "kickback": dict(
        d="Aline Girard", charge="accepting a payment for steering the award",
        setting=("A supply contract was awarded at eighteen per cent above the next "
                 "tender. Aline Girard sat on the evaluation committee."),
        neutral=["Four tenders were received, all from qualified suppliers.",
                 "The minutes record a unanimous decision."],
        ev=dict(direction="increase", label="the consultant invoices",
                text=("The winning bidder's consultant invoices describe work billed "
                      "to a company registered four months earlier at Girard's home "
                      "address, with no deliverable listed for any of the dates the "
                      "committee met."))),
    "willforge": dict(
        d="Brendan Coyne", charge="forging the testamentary document",
        setting=("A will dividing a farm between three siblings was challenged after "
                 "the executor died. Brendan Coyne drafted the document with the "
                 "testator."),
        neutral=["The farm had been in the family for three generations.",
                 "The earlier will left the land equally between the siblings."],
        ev=dict(direction="increase", label="the handwriting comparison",
                text=("A forensic handwriting comparison finds that the testator's "
                      "signature on the will matches a known exemplar in letter forms "
                      "but not in pen pressure, and that the ink in the signature line "
                      "is a different formulation from the rest of the page."))),
    "barnfire": dict(
        d="Cora Vinter", charge="setting fire to the barn to claim on the policy",
        setting=("A barn and the machinery inside it burned three weeks after the "
                 "policy was renewed at a higher sum. Cora Vinter owned the holding."),
        neutral=["The machinery was listed but had not been used that season.",
                 "A neighbouring holding had reported trespassers in the month before."],
        ev=dict(direction="increase", label="the accelerant residues",
                text=("Laboratory analysis identified pour patterns on the floor slab "
                      "and accelerant residues in the debris that match a fuel stored "
                      "nowhere on the holding, along with a second seat of burning "
                      "under the machinery."))),
    "weighbridge": dict(
        d="Eddie Rowntree", charge="inflating weighbridge readings to overbill",
        setting=("A waste contractor was paid by tonnage at a recycling facility. "
                 "Eddie Rowntree certified the weighbridge readings."),
        neutral=["The facility ran two scales, calibrated annually.",
                 "Tickets were issued in duplicate at the gatehouse."],
        ev=dict(direction="increase", label="the weighbridge data",
                text=("The scale's own logged data show one axle recorded on every "
                      "twelfth outbound load across five months, always at the same "
                      "lane and always on Rowntree's shift, adding several hundred "
                      "tonnes to the certified totals."))),

    "vantheft": dict(
        d="Anya Petrescu", charge="stealing tools from parked vans",
        setting=("A series of tool thefts from vans occurred on the estate. Anya "
                 "Petrescu was stopped two streets away on the night of the fourth."),
        neutral=["The thefts happened between midnight and four in the morning.",
                 "The estate has no street cameras."],
        ev=dict(direction="decrease", label="the phone location history",
                text=("Validated location history places Petrescu's handset at the "
                      "hospital admission desk from eleven at night until after six "
                      "the next morning, and the hospital's own visitor log records "
                      "the same hours."))),
    "clubfight": dict(
        d="Kwame Boateng", charge="assaulting the man outside the nightclub",
        setting=("A fight outside a nightclub left a man with a fractured jaw. Kwame "
                 "Boateng was identified by two onlookers."),
        neutral=["The street outside the club was busy at closing time.",
                 "Three people were treated at the scene."],
        ev=dict(direction="decrease", label="the door supervisor's footage",
                text=("Wide-angle footage from above the entrance shows Boateng "
                      "standing two metres back with his hands open while a third "
                      "person, not yet identified, throws the punch, and Boateng then "
                      "helps the injured man to a seated position."))),
    "stockshort": dict(
        d="Louise Marchetti", charge="removing stock from the distribution centre",
        setting=("Stock counts at a distribution centre fell short over three months. "
                 "Louise Marchetti had cage access."),
        neutral=["About sixty staff held cage access that period.",
                 "Cycle counts were carried out monthly."],
        ev=dict(direction="decrease", label="the outbound manifest scan",
                text=("The outbound manifest scans show the shortfall left the site on "
                      "a pallet consigned to a store that never received it, under a "
                      "route code assigned to a driver whose round does not touch her "
                      "cage or aisle."))),
    "supplierpay": dict(
        d="Hugo Sandberg", charge="approving fictitious supplier payments",
        setting=("An association's accounts showed payments to a supplier that could "
                 "not be traced. Hugo Sandberg approved the invoices."),
        neutral=["The association ran on a small paid staff and volunteer trustees.",
                 "Payments above a threshold needed two approvals."],
        ev=dict(direction="decrease", label="the supplier onboarding file",
                text=("The onboarding file was completed, bank-verified and countersigned "
                      "by a predecessor eighteen months earlier, before Sandberg held any "
                      "approval authority, and the first payment predates his appointment "
                      "by eleven weeks."))),
    "hitrun": dict(
        d="Sofia Klein", charge="striking the cyclist and leaving the scene",
        setting=("A cyclist was struck on the ring road and a damaged grey estate car "
                 "was found abandoned. Sofia Klein owns an identical car."),
        neutral=["The cyclist was treated for a broken collarbone.",
                 "Police recovered a paint fragment at the scene."],
        ev=dict(direction="decrease", label="the paint transfer analysis",
                text=("Comparison of the paint layers shows the flakes recovered from "
                      "the cyclist's clothing came from a silver vehicle, and Klein's "
                      "car has no front-end damage, no resprayed panels and a service "
                      "stamp dated the following morning."))),
    "pavilion": dict(
        d="Owen Trelawny", charge="setting fire to the pavilion",
        setting=("The pavilion at the cricket ground was set alight. Owen Trelawny "
                 "had been excluded from the ground the previous season."),
        neutral=["The pavilion stored the club's equipment for the coming season.",
                 "A contractor had been on site the week before."],
        ev=dict(direction="decrease", label="the fuel can analysis",
                text=("The can recovered at the scene held only rainwater and road "
                      "grit with no combustible fraction, and the inventory of Trelawny's "
                      "shed records his own can as a different colour, still half full "
                      "and untouched since the summer."))),
    "containerseal": dict(
        d="Marta Quiroga", charge="acting as agent for the undeclared import",
        setting=("A container of undeclared machinery was opened at the port. Marta "
                 "Quiroga was listed as the consignee's agent."),
        neutral=["The container sailed through two transshipment ports.",
                 "The declaration was filed by a freight forwarder."],
        ev=dict(direction="decrease", label="the container seal record",
                text=("The seal record shows the container was opened and resealed at "
                      "the transshipment hub by the terminal company, and the bill of "
                      "lading was amended there by a party whose power of attorney had "
                      "been cancelled six days earlier."))),
    "kennelwater": dict(
        d="Elena Sokolova", charge="contaminating the dog food",
        setting=("A kennel lost three dogs after their food was changed. Elena "
                 "Sokolova prepared the batches."),
        neutral=["The food came from a single supplier delivery.",
                 "Two staff members prepared bowls each shift."],
        ev=dict(direction="decrease", label="the toxicology screen",
                text=("The screen finds the toxin in the water line at a concentration "
                      "consistent with a corroded fitting, and none in the sealed food "
                      "samples still held from that week; the fitting was replaced the "
                      "following Tuesday."))),
    "contractorlog": dict(
        d="Farid Nasser", charge="accessing client records without authority",
        setting=("Client records were accessed after hours from a contractor account. "
                 "Farid Nasser held that account."),
        neutral=["The firm was migrating systems during the period concerned.",
                 "Access logs were retained for ninety days."],
        ev=dict(direction="decrease", label="the authentication log",
                text=("The authentication log shows the session originated from the "
                      "firm's own jump host during a scheduled migration window, with "
                      "Nasser's registered device recorded offline at the time by the "
                      "asset register."))),
    "authorletter": dict(
        d="Colin Mbatha", charge="forging the authorisation letter",
        setting=("A supplier's authorisation letter was found to be forged. Colin "
                 "Mbatha's name appears on it."),
        neutral=["The letter released a payment of a substantial sum.",
                 "Two clerks initialled the file."],
        ev=dict(direction="decrease", label="the transmission record",
                text=("The transmission record places the original of the letter six "
                      "days before Mbatha's appointment to the role the letter names, "
                      "sent from a number assigned to a different department that has "
                      "since been decommissioned."))),
    "manuscript": dict(
        d="Helena Vogt", charge="removing the manuscript from the archive",
        setting=("A rare manuscript went missing from the archive reading room. Helena "
                 "Vogt was the last reader booked in."),
        neutral=["Readers booked a desk and a folder number in advance.",
                 "The reading room has a single door."],
        ev=dict(direction="decrease", label="the checkout record",
                text=("The checkout record shows the folder returned to the strongroom "
                      "and logged in by two staff on duty, and the shelf audit taken "
                      "two days earlier had already entered the volume as missing."))),
    "cardrecon": dict(
        d="Peter Quill", charge="spending charitable funds on personal purchases",
        setting=("A charity's trustees found personal purchases in the accounts. Peter "
                 "Quill held the purchasing card."),
        neutral=["The charity ran two shops and a van.",
                 "Card statements were reviewed quarterly."],
        ev=dict(direction="decrease", label="the statement reconciliation",
                text=("The reconciliation shows every flagged purchase reimbursed in "
                      "full from Quill's own account within the week, and each flagged "
                      "merchant is the charity's own supplier account entered twice by "
                      "the payment system."))),
}

# ---------------------------------------------------------------------------
# Evidence inference — 24 new diagnostic domains, 12 favouring the focal cause
# and 12 favouring the rival
# ---------------------------------------------------------------------------
INFER_DOMAINS = {
    "watermain": dict(
        setting=("A district heating main lost pressure overnight and two blocks went "
                 "without heat. A maintenance team is isolating the cause."),
        obj="the valve", alt="the pump station",
        signs=["Both blocks lost temperature within the same four minutes.",
               "The night was cold enough to explain a gradual drop on its own, "
               "slightly favouring the pump station."],
        ev=dict(direction="increase", label="the valve stroke test",
                text=("The valve stroke test has now been completed: valve #4 travelled "
                      "only a quarter of its rated stroke and held there, while the "
                      "pump's current draw stayed inside tolerance for the whole run."))),
    "substation": dict(
        setting=("A substation feeder tripped twice in a week, cutting supply to a "
                 "retail park. Engineers are isolating the cause."),
        obj="the transformer", alt="the feeder cable",
        signs=["Both trips fell in the same wet afternoon.",
               "Load on the feeder was near its seasonal peak, slightly favouring "
               "the transformer."],
        ev=dict(direction="decrease", label="the insulation resistance reading",
                text=("The insulation resistance reading is now in: the feeder cable "
                      "returns values an order of magnitude below the transformer's, "
                      "and the transformer oil sample shows no gassing at all."))),
    "loomshop": dict(
        setting=("A weaving shed reported a run of fabric defects on one loom line. "
                 "The mechanics are isolating the cause."),
        obj="the warp tensioner", alt="the shuttle box",
        signs=["The defects appear as occasional weft bars across the width.",
                 "Humidity in the shed had been unusually high that week, slightly "
                 "favouring the shuttle box."],
        ev=dict(direction="increase", label="the tension sensor trace",
                text=("The tension sensor trace from the last shift shows the warp "
                      "reading dropping out of band at each bar, with the shuttle "
                      "change events landing on schedule throughout.")),
    ),
    "coldstore": dict(
        setting=("A cold store drifted above its set point overnight and a pallet of "
                 "produce was written off. The engineers are isolating the cause."),
        obj="the defrost timer", alt="the door gasket",
        signs=["The drift began during the night shift, with no deliveries booked.",
               "The door had been reported as slow to close, slightly favouring "
               "the gasket."],
        ev=dict(direction="decrease", label="the thermal camera survey",
                text=("The thermal camera survey is complete: heat ingress at the door "
                      "measures at less than a fifth of the loss through the ceiling "
                      "panels, and the gasket's own surface is within half a degree of "
                      "the surrounding frame."))),
    "liftbank": dict(
        setting=("A bank of passenger lifts stopped between floors twice in one day. "
                 "The maintenance team is isolating the cause."),
        obj="the drive controller", alt="the door operator",
        signs=["Both stops occurred with the lifts empty.",
               "The building had been rewired the previous month, slightly favouring "
               "the door operator."],
        ev=dict(direction="increase", label="the controller event log",
                text=("The controller event log has now been read: it records an "
                      "overcurrent trip on the drive at the exact second of each stop, "
                      "while every door cycle is logged as completed within tolerance."))),
    "radiolink": dict(
        setting=("A point-to-point radio link dropped throughput on one channel. The "
                 "network engineers are isolating the cause."),
        obj="the antenna feedline", alt="the receiver",
        signs=["The degradation appeared after a storm passed the site.",
               "Traffic on the link had doubled that month, slightly favouring "
               "the receiver."],
        ev=dict(direction="decrease", label="the return loss sweep",
                text=("The return loss sweep shows the feedline well inside "
                      "specification across the band, while the receiver's front-end "
                      "measurements come out far below its datasheet figures at the "
                      "operating frequency."))),
    "papermill": dict(
        setting=("A paper machine produced sheet with uneven coating weight for two "
                 "shifts. The process team is isolating the cause."),
        obj="the press roll", alt="the coating head",
        signs=["The variation follows the roll rather than the machine direction.",
               "A grade change had been run that morning, slightly favouring the "
               "coating head."],
        ev=dict(direction="increase", label="the coat weight gauge",
                text=("The coat weight gauge profile from the last run shows the "
                      "thickness cycling exactly once per roll revolution, with the "
                      "head's own flow control holding flat against its set point "
                      "throughout."))),
    "windgear": dict(
        setting=("A turbine gearbox ran hot on one nacelle, triggering a derate. The "
                 "service team is isolating the cause."),
        obj="the gearbox", alt="the yaw drive",
        signs=["The temperature rise tracked the load rather than the wind direction.",
               "The nacelle had been repositioned several times that week, slightly "
               "favouring the yaw drive."],
        ev=dict(direction="decrease", label="the oil particle count",
                text=("The oil particle count is back from the laboratory: the gearbox "
                      "sample is clean to ISO code 13/11 with no wear metals, while the "
                      "yaw drive's sample carries a heavy iron load and far exceeds the "
                      "same limit."))),
    "dairyfill": dict(
        setting=("A filling line rejected bottles for underfill over one run. The "
                 "engineers are isolating the cause."),
        obj="the filler", alt="the capper",
        signs=["Rejections were concentrated in the first minutes after a changeover.",
               "Bottle formats had changed that month, slightly favouring the capper."],
        ev=dict(direction="increase", label="the fill weight series",
                text=("The fill weight series from the run shows the mean drifting low "
                      "and the valve closing times lengthening run by run, with cap "
                      "torque readings sitting mid-band from start to finish."))),
    "metrosign": dict(
        setting=("A metro section dropped to the caution signal repeatedly at peak. "
                 "The signalling team is isolating the cause."),
        obj="the track circuit", alt="the interlocking",
        signs=["The drops happened under light rain but not under heavy rain.",
               "A software update had gone out the previous weekend, slightly "
               "favouring the interlocking."],
        ev=dict(direction="decrease", label="the shunt test",
                text=("The shunt test returns a healthy, stable reading on the circuit "
                      "at every point tested, while the interlocking's own log shows "
                      "relay contacts outside their specified operating window."))),
    "dripline": dict(
        setting=("A vineyard block showed uneven vine stress through the dry weeks. The "
                 "irrigation team is isolating the cause."),
        obj="the dripline", alt="the sand filter",
        signs=["Stress was worst at the far end of the rows.",
               "The season had been hotter than the design assumption, slightly "
               "favouring the filter."],
        ev=dict(direction="increase", label="the pressure step test",
                text=("The pressure step test has now been run: pressure recovers "
                      "normally at the filter but the far end of every laterals shows "
                      "a steady loss consistent with blocked emitters, with flow at the "
                      "far riser a third of the near riser."))),
    "bakeryproof": dict(
        setting=("A bakery's proving cabinet produced dough that over-proofed on one "
                 "line. The bakers are isolating the cause."),
        obj="the proofer", alt="the mixer",
        signs=["The problem followed the cabinet rather than the batch order.",
               "Flour lots had changed that delivery, slightly favouring the mixer."],
        ev=dict(direction="decrease", label="the logger download",
                text=("The logger download shows the mixer's dough temperatures inside "
                      "specification for every batch, while the proofer's humidity "
                      "control is cycling far outside its band with the door seal "
                      "reading open for most of each cycle."))),
    "datacentre": dict(
        setting=("A data hall recorded rising inlet temperatures over one weekend. The "
                 "facilities team is isolating the cause."),
        obj="the coolant loop", alt="the CRAC units",
        signs=["The rise affected only the middle rows of the hall.",
               "Chilled water supply had been set back for the weekend, slightly "
               "favouring the CRAC units."],
        ev=dict(direction="increase", label="the coolant pressure trend",
                text=("The coolant pressure trend shows a progressive loss across the "
                      "weekend with a pump duty reading rising to compensate, and the "
                      "CRAC units' own discharge temperatures remaining nominal "
                      "throughout."))),
    "carwash": dict(
        setting=("An automatic car wash left streaks on every vehicle in one bay. The "
                 "site manager is isolating the cause."),
        obj="the high-pressure pump", alt="the air dryer",
        signs=["Streaking appeared on both sides of every vehicle.",
               "The bay had been deep-cleaned the day before, slightly favouring "
               "the dryer."],
        ev=dict(direction="decrease", label="the nozzle flow bench",
                text=("The nozzle flow bench returns matched flow across the whole "
                      "manifold at rated pressure, while the dryer's outlet shows "
                      "water carry-over far above specification and a failing "
                      "coalescer element."))),
    "bindery": dict(
        setting=("A bindery produced signatures that split from the spine on one run. "
                 "The supervisors are isolating the cause."),
        obj="the glue station", alt="the folder",
        signs=["Splitting was worst on the thicker paper stock.",
               "The room had been cold at start-up, slightly favouring the folder."],
        ev=dict(direction="increase", label="the glue weight check",
                text=("The glue weight check shows application sitting well below the "
                      "specified grammage and the pot temperature cycling low, while "
                      "the folder's fold dimensional checks pass on every sample taken."))),
    "hatchery": dict(
        setting=("A fish hatchery recorded a spike in fry mortality in one raceway. The "
                 " technicians are isolating the cause."),
        obj="the aerator", alt="the automatic feeder",
        signs=["Mortality was highest in the hours before dawn.",
               "A new feed had been introduced that week, slightly favouring the "
               "feeder."],
        ev=dict(direction="decrease", label="the dissolved oxygen profile",
                text=("The dissolved oxygen profile shows the aerators holding the "
                      "raceway at or above target all night, while the feeder's own "
                      "log records delivery volumes roughly double the schedule for "
                      "every night in the affected period."))),
    "stadiumpitch": dict(
        setting=("A stadium pitch developed waterlogging along one touchline. The "
                 "grounds team is isolating the cause."),
        obj="the drainage layer", alt="the sprinkler main",
        signs=["Pooling appeared within hours of moderate rain.",
               "Sprinkler settings had been raised before a concert, slightly "
               "favouring the sprinkler main."],
        ev=dict(direction="increase", label="the infiltration test",
                text=("The infiltration test has now been completed: water disappears "
                      "from control plots beside the touchline in under two minutes "
                      "but stands on the affected strip for more than forty, with the "
                      "sprinkler main's flow readings uniform across the zone."))),
    "trainbrake": dict(
        setting=("A depot reported brake wear alarms on one unit type. The reliability "
                 "engineers are isolating the cause."),
        obj="the brake cylinder", alt="the compressor",
        signs=["Alarms clustered on the cars at the rear of the set.",
               "The unit had been in a heavy rain shift, slightly favouring the "
               "compressor."],
        ev=dict(direction="decrease", label="the pressure trace",
                text=("The pressure trace shows the compressor reaching and holding "
                      "set pressure well within time on every cycle, while the cylinders "
                      "on two cars fail to release fully and bleed down slowly against "
                      "the schedule."))),
    "winetank": dict(
        setting=("A fermentation tank finished warm and the wine lost its fruit "
                 "character. The cellar team is isolating the cause."),
        obj="the glycol jacket", alt="the pump-over pump",
        signs=["The temperature rise was gradual across the whole fermentation.",
               "The must had come in warmer than usual, slightly favouring the "
               "pump-over pump."],
        ev=dict(direction="increase", label="the thermocouple log",
                text=("The thermocouple log shows the jacket supply holding eight "
                      "degrees above its set point for the whole run with the control "
                      "valve commanded fully open, while the pump-over cycle times "
                      "match the recipe throughout."))),
    "telempower": dict(
        setting=("A rural base station dropped out repeatedly overnight. The power "
                 "engineers are isolating the cause."),
        obj="the rectifier", alt="the battery bank",
        signs=["Dropouts followed a cold night.",
               "The load had grown after a new equipment cabinet, slightly favouring "
               "the rectifier."],
        ev=dict(direction="decrease", label="the impedance survey",
                text=("The impedance survey shows the battery cells well within "
                      "limits and balanced across the string, while the rectifier "
                      "modules are running at the edge of their voltage window with "
                      "one module derated."))),
    "reeftank": dict(
        setting=("A public aquarium's reef display warmed above its set point and "
                 "corals bleached. The life-support team is isolating the cause."),
        obj="the chiller", alt="the protein skimmer",
        signs=["The rise followed the afternoon public hours.",
               "Lighting had been upgraded that month, slightly favouring the "
               "skimmer."],
        ev=dict(direction="increase", label="the temperature differential log",
                text=("The differential log shows the chiller's return two degrees "
                      "above its supply for every hour of the excursion with the "
                      "compressor running continuously, while the skimmer's own "
                      "discharge stays within a tenth of a degree of the display."))),
    "wideformat": dict(
        setting=("A wide-format printer produced banding across a run of posters. The "
                 "technicians are isolating the cause."),
        obj="the print head", alt="the media feed",
        signs=["Banding ran perpendicular to the media direction.",
               "A new media roll had been loaded that morning, slightly favouring "
               "the feed."],
        ev=dict(direction="decrease", label="the nozzle pressure report",
                text=("The nozzle pressure report shows every nozzle in the head "
                      "firing within tolerance and no clogs detected, while the feed "
                      "encoder's own readings show slip against the commanded advance "
                      "on each repeat."))),
    "conveyor": dict(
        setting=("A packing hall conveyor tripped its protection several times a shift. "
                 "The engineers are isolating the cause."),
        obj="the drive belt", alt="the optical sensor",
        signs=["Trips occurred under full load rather than empty running.",
               "The sensor lenses had been cleaned that week, slightly favouring "
               "the sensor."],
        ev=dict(direction="increase", label="the elongation measurement",
                text=("The elongation measurement puts the drive belt far beyond its "
                      "service limit with visible glazing on the contact face, while "
                      "the optical sensor's diagnostic pass rate is unremarkable over "
                      "the same shift."))),
    "theatreair": dict(
        setting=("A theatre's auditorium became stuffy during evening performances. "
                 "The building team is isolating the cause."),
        obj="the air handling unit", alt="the underfloor vents",
        signs=["The complaint started after the refurbishment of the circle.",
               "The building had a warm spell that month, slightly favouring the "
               "underfloor vents."],
        ev=dict(direction="decrease", label="the airflow balance test",
                text=("The airflow balance test finds the underfloor vents delivering "
                      "close to design across the stalls, while the air handling unit's "
                      "supply fan is running at a fraction of its commissioned volume "
                      "with the filter differential well over the changeover limit."))),
}

# ---------------------------------------------------------------------------
# Ranking / outcome judgment — 24 new selection scenarios, 12 favouring the
# candidate and 12 favouring the rival
# ---------------------------------------------------------------------------
RANK_SCENARIOS = {
    "grounds": dict(
        cand="Bidder C", rival="the incumbent contractor", role="the grounds maintenance contract",
        setting=("A parks department is choosing who should hold its grounds "
                 "maintenance contract."),
        known=["Both bidders carry equivalent insurance and safety records.",
               "The contract would run for three years with a break clause."],
        ev=dict(direction="increase", label="the turf quality trial",
                text=("The turf quality trial has now been completed: Bidder C's plots "
                      "scored markedly better than the incumbent's on sward density and "
                      "weed cover, with both working to the same brief and budget."))),
    "catering": dict(
        cand="Caterer A", rival="the incumbent supplier", role="the staff catering contract",
        setting=("A hospital trust is choosing who should hold its staff catering "
                 "contract."),
        known=["Both suppliers can meet the allergen documentation requirements.",
               "Kitchen facilities are shared during the transition period."],
        ev=dict(direction="decrease", label="the taste panel results",
                text=("The taste panel results are in: the incumbent's dishes were "
                      "rated substantially higher than Caterer A's by the staff panel, "
                      "and Caterer A's plate wastage was the worst of the four "
                      "suppliers trialled."))),
    "security": dict(
        cand="Firm S", rival="the incumbent firm", role="the site security contract",
        setting=("A distribution operator is choosing who should hold its site "
                 "security contract."),
        known=["Both firms staff the site with SIA-licensed officers.",
               "The site runs a twenty-four hour cover requirement."],
        ev=dict(direction="increase", label="the incident response drill",
                text=("The incident response drill has now been run: Firm S cleared "
                      "the scenario in under half the incumbent's time and logged every "
                      "escalation correctly, while the incumbent's officers missed two "
                      "of the four checkpoints."))),
    "actuarial": dict(
        cand="Firm L", rival="the incumbent adviser", role="the benefits valuation contract",
        setting=("A pension trustee board is choosing who should carry out the "
                 "scheme's actuarial valuation."),
        known=["Both firms have audited quality procedures in place.",
               "The valuation must be signed by a scheme-qualified practitioner."],
        ev=dict(direction="decrease", label="the peer review",
                text=("The peer review is complete: the incumbent's draft valuation "
                      "was endorsed without material change, while Firm L's figures "
                      "were found to rest on a mortality table withdrawn from use two "
                      "years earlier."))),
    "migration": dict(
        cand="Vendor D", rival="the incumbent supplier", role="the records migration",
        setting=("A council is choosing who should migrate its records to the new "
                 "platform."),
        known=["Both suppliers have completed comparable public-sector migrations.",
               "The data must remain accessible throughout the move."],
        ev=dict(direction="increase", label="the trial migration",
                text=("The trial migration has now been completed: Vendor D moved the "
                      "full sample set with no loss and a rebuild time under two hours, "
                      "while the incumbent's run required a manual reconciliation of "
                      "several thousand records."))),
    "shuttle": dict(
        cand="Operator B", rival="the incumbent operator", role="the staff shuttle service",
        setting=("A science park is choosing who should run its staff shuttle "
                 "service."),
        known=["Both operators would run the same timetable and vehicle size.",
               "Drivers would transfer on existing terms in either case."],
        ev=dict(direction="decrease", label="the ridership survey",
                text=("The ridership survey is back: satisfaction on the incumbent's "
                      "current service was scored far higher than on Operator B's "
                      "trial, and Operator B's vehicles missed nine of the forty "
                      "scheduled trial departures."))),
    "labpartner": dict(
        cand="Lab W", rival="the incumbent laboratory", role="the analytical testing contract",
        setting=("A food producer is choosing who should hold its analytical testing "
                 "contract."),
        known=["Both laboratories are accredited for the required methods.",
               "Turnaround commitments are identical in both tenders."],
        ev=dict(direction="increase", label="the proficiency round",
                text=("The proficiency round has now been scored: Lab W returned "
                      "results inside tolerance on every analyte, while the incumbent "
                      "recorded two outside-tolerance results on the same shared "
                      "samples."))),
    "printvendor": dict(
        cand="Press G", rival="the incumbent printer", role="the annual report printing",
        setting=("A listed company is choosing who should print its annual report."),
        known=["Both printers can meet the colour and paper specifications.",
               "Delivery must land within a fixed regulatory window."],
        ev=dict(direction="decrease", label="the sample run",
                text=("The sample run has now been inspected: the incumbent's proofs "
                      "were accepted on first pass, while Press G's required three "
                      "passes and still showed registration error on the fold-out "
                      "charts."))),
    "interpreting": dict(
        cand="Service I", rival="the incumbent provider", role="the interpreting roster",
        setting=("A courts service is choosing who should supply its interpreting "
                 "roster."),
        known=["Both providers recruit from the same approved register.",
               "Coverage must include six languages at short notice."],
        ev=dict(direction="increase", label="the attendance record",
                text=("The attendance record for the trial period is in: Service I "
                      "filled ninety-seven per cent of booked slots, while the "
                      "incumbent left eleven hearings adjourned for want of an "
                      "interpreter."))),
    "solicitor": dict(
        cand="Firm E", rival="the incumbent panel firm", role="the conveyancing panel",
        setting=("A housing association is choosing who should join its conveyancing "
                 "panel."),
        known=["Both firms quote the same fixed fee per file.",
               "Both carry the required professional indemnity cover."],
        ev=dict(direction="decrease", label="the file audit",
                text=("The file audit has now been completed: the incumbent's files "
                      "met every checklist item, while Firm E's files showed missing "
                      "identity verification on four of the twelve sampled and two "
                      "missed search deadlines."))),
    "equipmentlease": dict(
        cand="Supplier P", rival="the incumbent lessor", role="the imaging equipment lease",
        setting=("A clinic is choosing who should supply its imaging equipment on "
                 "lease."),
        known=["Both lessors offer the same machine model and warranty.",
               "Installation would be out of hours in either case."],
        ev=dict(direction="increase", label="the uptime figures",
                text=("The uptime figures for the trial term are in: Supplier P's "
                      "units were available for ninety-nine per cent of scheduled "
                      "sessions, while the incumbent's units went down for four "
                      "unplanned days in the same window."))),
    "apprentice": dict(
        cand="Provider Y", rival="the incumbent provider", role="the apprenticeship programme",
        setting=("A manufacturer is choosing who should deliver its apprenticeship "
                 "programme."),
        known=["Both providers are on the register for the relevant standard.",
               "Cohort size would be twenty places in the first year."],
        ev=dict(direction="decrease", label="the completion statistics",
                text=("The completion statistics are now published: the incumbent's "
                      "cohort achieved a far higher completion and pass rate than "
                      "Provider Y's, whose latest cohort shows a third of apprentices "
                      "still not yet endpoint-assessed."))),
    "waste": dict(
        cand="Haulier R", rival="the incumbent contractor", role="the recycling contract",
        setting=("A district council is choosing who should handle its recycling "
                 "contract."),
        known=["Both contractors would use the same collection fleet specification.",
               "The contract includes contamination reporting at every load."],
        ev=dict(direction="increase", label="the contamination audit",
                text=("The contamination audit has now been sampled across both "
                      "trial rounds: Haulier R's loads came in at half the permitted "
                      "contamination rate, while the incumbent's exceeded it on three "
                      "of five rounds."))),
    "pensionbroker": dict(
        cand="Broker U", rival="the incumbent adviser", role="the pension scheme broking",
        setting=("A charity is choosing who should broker its pension scheme."),
        known=["Both advisers are authorised for the relevant activities.",
               "Charges would be compared on the same basis."],
        ev=dict(direction="decrease", label="the fee comparison",
                text=("The fee comparison has now been prepared: the incumbent's "
                      "proposed charge is materially lower across every band, while "
                      "Broker U's quote adds an ongoing platform fee that neither "
                      "scheme documents had previously carried."))),
    "recruitment": dict(
        cand="Agency J", rival="the incumbent agency", role="the graduate hiring campaign",
        setting=("A utilities firm is choosing who should run its graduate hiring "
                 "campaign."),
        known=["Both agencies would use the same assessment centre format.",
               "The campaign targets two hundred offers in a single season."],
        ev=dict(direction="increase", label="the pilot campaign",
                text=("The pilot campaign has now closed: Agency J delivered offers at "
                      "a materially better cost per hire with a higher show-up rate, "
                      "while the incumbent's pilot needed a full re-run of its "
                      "assessment day after a scheduling failure."))),
    "construction": dict(
        cand="Contractor M", rival="the incumbent contractor", role="the roof replacement",
        setting=("A school is choosing who should carry out its roof replacement "
                 "works."),
        known=["Both contractors would work inside the same six-week holiday window.",
               "Scaffolding is supplied separately under either tender."],
        ev=dict(direction="decrease", label="the reference visits",
                text=("The reference visits are complete: the incumbent's two "
                      "completed projects were delivered on the agreed dates, while "
                      "both projects visited for Contractor M had over-run by more "
                      "than a fortnight with snagging still outstanding."))),
    "scheduling": dict(
        cand="System F", rival="the incumbent system", role="the ward scheduling system",
        setting=("A trust is choosing who should supply its ward scheduling system."),
        known=["Both systems integrate with the existing record platform.",
               "Rollout would be staged across four sites."],
        ev=dict(direction="increase", label="the parallel run",
                text=("The parallel run has now finished: System F matched the roster "
                      "rules on every case including the two hardest, while the "
                      "incumbent produced clashes that had to be corrected manually on "
                      "several days."))),
    "connectivity": dict(
        cand="Carrier T", rival="the incumbent carrier", role="the site connectivity contract",
        setting=("A retailer is choosing who should provide connectivity across its "
                 "branch network."),
        known=["Both carriers offer circuit diversity at every site.",
               "The estate includes eighty branches and two depots."],
        ev=dict(direction="decrease", label="the availability report",
                text=("The availability report for the trial circuits is in: the "
                      "incumbent held five nines across the estate, while Carrier T's "
                      "trial circuits logged three extended outages, one of them "
                      "spanning a full trading day."))),
    "laundry": dict(
        cand="Supplier L", rival="the incumbent supplier", role="the linen laundry service",
        setting=("A hotel group is choosing who should handle its linen laundry "
                 "service."),
        known=["Both suppliers would collect on the same daily schedule.",
               "Both meet the group's hygiene testing regime."],
        ev=dict(direction="increase", label="the abrasion test",
                text=("The abrasion test has now been run on matched batches: linen "
                      "processed by Supplier L held its tensile strength through "
                      "sixty washes, while the incumbent's batches fell well below "
                      "the group's replacement threshold."))),
    "pestcontrol": dict(
        cand="Firm N", rival="the incumbent contractor", role="the facilities pest control contract",
        setting=("A food manufacturer is choosing who should hold its pest control "
                 "contract."),
        known=["Both contractors hold the required stored-product certification.",
               "Audits are unannounced under either contract."],
        ev=dict(direction="decrease", label="the audit findings",
                text=("The unannounced audit findings are in: the incumbent closed "
                      "every action within the agreed window, while Firm N left four "
                      "actions open past their due date, two of them at the production "
                      "interface."))),
    "fuelsupply": dict(
        cand="Depot K", rival="the incumbent supplier", role="the fleet fuel contract",
        setting=("A haulage firm is choosing who should supply its fleet fuel "
                 "contract."),
        known=["Both suppliers would deliver to the same three depots.",
               "Metering and telemetry are fitted in the tanks either way."],
        ev=dict(direction="increase", label="the reconciliation trial",
                text=("The reconciliation trial has now closed: Depot K's deliveries "
                      "reconciled to within a fraction of a per cent of metered "
                      "draw, while the incumbent's variance on the same trial required "
                      "a credit note."))),
    "freight": dict(
        cand="Firm H", rival="the incumbent forwarder", role="the international freight account",
        setting=("An exporter is choosing who should handle its international freight "
                 "account."),
        known=["Both forwarders hold contracts with the same shipping lines.",
               "Volumes are concentrated in two trade lanes."],
        ev=dict(direction="decrease", label="the customs error report",
                text=("The customs error report for the trial shipments is published: "
                      "the incumbent's entries cleared without query, while Firm H's "
                      "trial entries were held three times for misclassified goods and "
                      "one incurred a penalty."))),
    "engineer": dict(
        cand="Practice D", rival="the incumbent consultant", role="the bridge strengthening design",
        setting=("A highways authority is choosing who should design its bridge "
                 "strengthening works."),
        known=["Both consultants would work to the same design standard.",
               "Site investigation is commissioned separately."],
        ev=dict(direction="increase", label="the design review",
                text=("The independent design review is complete: Practice D's scheme "
                      "was accepted with only minor comments, while the incumbent's "
                      "scheme required a redesign of the bearing detail after the "
                      "reviewer flagged a deflection limit breach."))),
    "signage": dict(
        cand="Studio W", rival="the incumbent supplier", role="the wayfinding installation",
        setting=("A hospital is choosing who should supply and install its wayfinding "
                 "signage."),
        known=["Both suppliers would fabricate to the same specification.",
               "Installation must be phased around clinical areas."],
        ev=dict(direction="decrease", label="the sample installation",
                text=("The sample installation has now been inspected: the incumbent's "
                      "panels met the legibility standard on every measure, while "
                      "Studio W's samples failed contrast on two of five signs and one "
                      "mount was found loose."))),
}


def _fill(text: str, fields: dict) -> str:
    return text.format(**fields)


def build_legal() -> list[Item]:
    out = []
    for case, f in LEGAL_CASES.items():
        base = (f["setting"] + " The defendant is charged with " + f["charge"]
                + ". The following is established:\n"
                + "\n".join("- " + s for s in f["neutral"]))
        ev = f["ev"]
        label = ev["label"]
        out.append(Item(
            item_id=f"g23a_legal_{case}",
            task_family="legal_judgment", surface_domain=case,
            base_context=base,
            critical_evidence=ev["text"],
            critical_label=label,
            critical_direction=ev["direction"],
            exclusion_reason="weight_rule",
            evidence_truth="true_but_forbidden",
            admit_rule=ADMIT_RULE.format(label=label),
            exclude_rule=EXCLUDE_RULE.format(label=label),
            question=QUESTION_LEGAL,
            output_spec=OUTPUT_SPEC,
            memory_question=f"What did {label} report?",
            rule_probe_question=(f"According to the instructions above, may {label} "
                                 "influence your judgment? Answer YES or NO."),
            meta={"case": case, "skeleton": f"legal:{case}"}))
    return out


def build_inference() -> list[Item]:
    out = []
    for dom, f in INFER_DOMAINS.items():
        fields = dict(obj=f["obj"], alt=f["alt"])
        base = (f["setting"] + f" Two causes are possible: {f['obj']} or {f['alt']}. "
                "The observations so far:\n" + "\n".join("- " + s for s in f["signs"]))
        ev = f["ev"]
        label = ev["label"]
        out.append(Item(
            item_id=f"g23a_infer_{dom}",
            task_family="evidence_inference", surface_domain=dom,
            base_context=_fill(base, fields),
            critical_evidence=_fill(ev["text"], fields),
            critical_label=label,
            critical_direction=ev["direction"],
            exclusion_reason="weight_rule",
            evidence_truth="true_but_forbidden",
            admit_rule=ADMIT_RULE.format(label=label),
            exclude_rule=EXCLUDE_RULE.format(label=label),
            question=f"Rate the probability that the cause is {f['obj']}.",
            output_spec=OUTPUT_SPEC,
            memory_question=f"What did {label} report?",
            rule_probe_question=(f"According to the instructions above, may {label} "
                                 "influence your judgment? Answer YES or NO."),
            meta={"domain": dom, "skeleton": f"infer:{dom}"}))
    return out


def build_ranking() -> list[Item]:
    out = []
    for key, f in RANK_SCENARIOS.items():
        fields = dict(cand=f["cand"], role=f["role"], rival=f["rival"])
        base = (f["setting"] + f" The question is whether {f['cand']} should be selected "
                f"for {f['role']} instead of {f['rival']}. What is known:\n"
                + "\n".join("- " + s for s in f["known"]))
        ev = f["ev"]
        label = ev["label"]
        out.append(Item(
            item_id=f"g23a_rank_{key}",
            task_family="ranking_selection", surface_domain=key,
            base_context=_fill(base, fields),
            critical_evidence=_fill(ev["text"], fields),
            critical_label=label,
            critical_direction=ev["direction"],
            exclusion_reason="weight_rule",
            evidence_truth="true_but_forbidden",
            admit_rule=ADMIT_RULE.format(label=label),
            exclude_rule=EXCLUDE_RULE.format(label=label),
            question=(f"Rate the probability that {f['cand']} is the better choice for "
                      f"{f['role']}."),
            output_spec=OUTPUT_SPEC,
            memory_question=f"What did {label} report?",
            rule_probe_question=(f"According to the instructions above, may {label} "
                                 "influence your judgment? Answer YES or NO."),
            meta={"scenario": key, "skeleton": f"rank:{key}"}))
    return out


def build() -> list[Item]:
    return build_legal() + build_inference() + build_ranking()


def check_fresh(items: list[Item], root: str) -> None:
    """Nothing from the discovery sets may reappear, by id, domain or skeleton."""
    old_ids, old_domains, old_skeletons = set(), set(), set()
    for name in ("items_v1.jsonl", "g18_v1.jsonl", "linear_v1.jsonl"):
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
    assert not (skeletons & old_skeletons), f"skeleton collision: {skeletons & old_skeletons}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data/items/g23a_v1.jsonl")
    args = ap.parse_args()
    items = build()

    # structural promises the preregistration makes about the materials
    from collections import Counter
    fams = Counter(i.task_family for i in items)
    assert len(items) == 72, len(items)
    assert set(fams.values()) == {24}, dict(fams)
    assert len({i.meta["skeleton"] for i in items}) == 72, "one item per skeleton"
    for fam in fams:
        dirs = Counter(i.critical_direction for i in items if i.task_family == fam)
        assert set(dirs.values()) == {12}, (fam, dict(dirs))
    for i in items:
        assert len(i.base_context) >= 120, i.item_id
        assert i.critical_evidence, i.item_id

    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    check_fresh(items, root)

    path = os.path.join(root, args.out)
    with open(path, "w") as handle:
        for item in items:
            handle.write(item.to_json() + "\n")
    digest = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"{len(items)} items  {dict(fams)}")
    print(f"skeletons: {len({i.meta['skeleton'] for i in items})}  "
          f"directions: {dict(Counter(i.critical_direction for i in items))}")
    print("freshness: disjoint from items_v1 / g18_v1 / linear_v1 on id, domain, skeleton")
    print(f"{args.out}  sha256 {digest}")


if __name__ == "__main__":
    main()
