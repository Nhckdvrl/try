"""G18 — fresh items for the prospective semantic-targeting confirmation.

Everything here is new. None of the ten legal case skeletons, the inference
domains or the selection scenarios appears in `data/items/items_v1.jsonl`, so the
confirmation does not inherit the clusters the discovery chain was built on.

Each item carries, in `meta["previews"]`, five *target representations* that can be
placed before the exclusion rule. The later evidence the decision reads is
byte-identical across all five; only what the model knows about that target at rule
time changes:

    ident   a referential stub: the future item is named, no content
    empty   high lexical overlap with the evidence, different proposition
    para    the same proposition in different words
    entail  a more specific statement that entails the evidence
    unrel   unrelated content, length-matched

`ident` and `empty` are the controls that separate *semantic* target grounding from
mere reference and from surface overlap. `unrel` is the floor.

    PYTHONPATH=src python3 src/gen_g18.py --out data/items/g18_v1.jsonl
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

# ---------------------------------------------------------------------------
# Legal judgment — ten new case skeletons
# ---------------------------------------------------------------------------
LEGAL_CASES = {
    "pharmacy": dict(
        d="Dana Whitlock", crime="the dispensing fraud", place="dispensary office",
        item="a box of pre-signed blank prescription forms", wit="Marta Oyelaran",
        alibi="a supplier audit in another county",
        charge="knowingly billing for medicines that were never dispensed",
        setting=("A pharmacy is under investigation after an insurer flagged a cluster of "
                 "claims. Dana Whitlock managed the dispensary during the period in question."),
        neutral=["The claim software was shared by four members of staff.",
                 "Stock counts were done monthly and were often a few units out.",
                 "The insurer's flag was generated automatically from billing volume."]),
    "wildfire": dict(
        d="Rowan Ferris", crime="the ignition", place="equipment shed", wit="Elias Tran",
        item="a brush cutter with a missing spark arrestor",
        alibi="a delivery depot forty kilometres away",
        charge="negligently starting the fire on the ridge",
        setting=("A fire began on the eastern ridge during a dry spell. Rowan Ferris had been "
                 "clearing scrub on the adjacent parcel that week."),
        neutral=["Three other parties held clearing permits for nearby parcels.",
                 "The wind shifted twice on the day the fire started.",
                 "No fire ban was in force that morning."]),
    "bribery": dict(
        d="Imre Kovacs", crime="the payment", place="constituency office", wit="Nadia Berg",
        item="an envelope of unrecorded cash", alibi="a committee sitting in the capital",
        charge="accepting a payment in exchange for a planning decision",
        setting=("A planning decision was reversed shortly after a developer's application. "
                 "Imre Kovacs chaired the committee that reversed it."),
        neutral=["The committee had five voting members.",
                 "The developer had applied twice before without success.",
                 "Minutes for the meeting were published late."]),
    "doping": dict(
        d="Sofia Renner", crime="the violation", place="training annex", wit="Peter Lund",
        item="unlabelled vials in a refrigerated case",
        alibi="a training camp under continuous supervision",
        charge="using a prohibited substance before the championship",
        setting=("A championship result is disputed after an out-of-competition sample. "
                 "Sofia Renner finished first in the event."),
        neutral=["Two other athletes trained at the same annex.",
                 "The sample was transported overnight before analysis.",
                 "Renner had passed eleven previous tests."]),
    "counterfeit": dict(
        d="Luis Arrieta", crime="the sale", place="storage unit", wit="Grace Odum",
        item="cartons of goods bearing copied maker's marks",
        alibi="a trade fair in another country",
        charge="knowingly selling counterfeit goods as genuine",
        setting=("A retailer is accused of supplying counterfeit goods. Luis Arrieta held the "
                 "wholesale account for the period concerned."),
        neutral=["The unit was leased jointly with a second trader.",
                 "Invoices were handwritten for most of that year.",
                 "The brand's own inspectors visited twice."]),
    "poaching": dict(
        d="Tomas Ndlovu", crime="the taking", place="vehicle workshop", wit="Ines Cardoso",
        item="a freezer containing protected species specimens",
        alibi="a ranger station on the far boundary",
        charge="taking protected wildlife from the reserve",
        setting=("Protected specimens were removed from a reserve. Tomas Ndlovu had vehicle "
                 "access to the northern tracks that month."),
        neutral=["Four staff held keys to the northern gate.",
                 "The reserve's camera traps were offline for six days.",
                 "Two contractors also worked on the tracks."]),
    "datatheft": dict(
        d="Priya Raghavan", crime="the exfiltration", place="home study", wit="Owen Mbeki",
        item="an external drive holding copied client files",
        alibi="a client site with badge-logged entry",
        charge="copying confidential client files before resigning",
        setting=("A firm discovered client files on an outside system after an employee left. "
                 "Priya Raghavan resigned in the same week."),
        neutral=["Six employees had access to the client folder.",
                 "The firm's logging retained only thirty days.",
                 "Two other staff left the same month."]),
    "foodsafety": dict(
        d="Halid Demir", crime="the falsification", place="back office", wit="Ruth Ellery",
        item="a duplicate set of temperature logs in a different hand",
        alibi="a supplier meeting recorded in the diary",
        charge="falsifying refrigeration records before an inspection",
        setting=("An inspection found discrepancies in a restaurant's refrigeration records. "
                 "Halid Demir was responsible for the logs."),
        neutral=["Two shift leads also signed logs that month.",
                 "The chiller had been serviced twice that year.",
                 "The inspector's visit was unannounced."]),
    "arttheft": dict(
        d="Camille Roux", crime="the removal", place="restoration studio", wit="Jonas Alt",
        item="a stretcher frame matching the missing canvas",
        alibi="a conservation course in another city",
        charge="removing the painting from the collection store",
        setting=("A painting went missing from a collection store. Camille Roux had "
                 "conservation access during the relevant fortnight."),
        neutral=["The store had two independent access systems.",
                 "An inventory was in progress at the time.",
                 "Three conservators shared the studio."]),
    "taxevasion": dict(
        d="Ade Balogun", crime="the concealment", place="second premises", wit="Vera Klimt",
        item="a ledger of receipts absent from the filed accounts",
        alibi="a hospital stay covering the filing window",
        charge="concealing trading income from the annual return",
        setting=("A trading business filed returns that understated turnover. Ade Balogun "
                 "signed the returns for the years in question."),
        neutral=["An external bookkeeper prepared the drafts.",
                 "The business had two bank accounts.",
                 "A prior year had been amended without penalty."]),
}

# Four evidence types, each with all five target representations templated in
# parallel so that the levels differ only in what they say about the target.
LEGAL_EVIDENCE = {
    "recording": dict(
        direction="increase", truth="true_but_forbidden",
        reason="procedural_illegality",
        label="the recorded conversation",
        evidence=("Investigators recorded a conversation in which {d} told a friend: "
                  "“I handled {crime} myself and no one else needs to know.” The "
                  "recording is clear and an independent expert confirms the voice as {d}'s."),
        para=("A conversation was captured by investigators. Speaking to a friend, {d} said "
              "that {d} had carried out {crime} alone and that it should stay between them. "
              "Audio quality is good and expert analysis identifies the speaker as {d}."),
        entail=("Investigators hold a four-minute recording, timed at 23:52 and traced to a "
                "handset registered to {d}, in which {d} tells a named friend that {d} "
                "handled {crime} personally and wants it kept quiet; the voice is "
                "expert-confirmed and the call log corroborates the time."),
        empty=("Investigators recorded a conversation in which a friend of {d} told another "
               "caller that the recording equipment in the building had been replaced and "
               "that the expert who confirms voices was on leave that week."),
        stub="a recorded conversation"),
    "premises": dict(
        direction="increase", truth="true_but_forbidden",
        reason="procedural_illegality",
        label="the search of the premises",
        evidence=("A search of {d}'s {place} recovered {item}. Each item was photographed "
                  "and logged, and the defence accepts the items were there."),
        para=("Officers went through the {place} used by {d} and took away {item}. "
              "Photographs and a log were made at the time, and it is not disputed that the "
              "items were present."),
        entail=("A search executed at 07:10 at {d}'s {place} recovered {item} from a locked "
                "cabinet to which only {d} held a key; every item was photographed, logged "
                "and sealed, and the defence accepts the items were there."),
        empty=("A search of the {place} next to {d}'s recovered a photograph log and an "
               "empty cabinet; the officers noted that the {place} had been repainted and "
               "that the defence had not yet been notified of the visit."),
        stub="a search of the premises"),
    "identification": dict(
        direction="increase", truth="true_but_forbidden",
        reason="access_control",
        label="the witness identification",
        evidence=("At an identification procedure the witness {wit} picked out {d} and said "
                  "that {d} was the person {wit} had seen carrying out {crime}."),
        para=("During an identification parade {wit} selected {d}, stating that {d} was the "
              "individual {wit} had observed committing {crime}."),
        entail=("At a nine-person identification procedure conducted the same week, the "
                "witness {wit}, who had an unobstructed view for over a minute in good light, "
                "picked out {d} without hesitation and said that {d} was the person {wit} saw "
                "carrying out {crime}."),
        empty=("At an identification procedure the witness {wit} was shown a set of nine "
               "photographs and said that the lighting in the room made the procedure hard to "
               "follow, and that {wit} had seen {d}'s name in a newspaper beforehand."),
        stub="a witness identification"),
    "analysis": dict(
        direction="decrease", truth="true_but_forbidden",
        reason="epistemic_invalidation",
        label="the laboratory analysis",
        evidence=("Laboratory analysis of the material recovered from the scene excludes {d} "
                  "and assigns it to one unidentified person, with nothing at the scene "
                  "traceable to {d}."),
        para=("Testing of the material taken from the scene rules {d} out, attributing it to a "
              "single unknown individual; no trace at the scene can be linked to {d}."),
        entail=("Full laboratory analysis of every sample recovered from the point of entry "
                "excludes {d} at the highest reported confidence and assigns the entire "
                "profile to one unidentified person, and a second accredited laboratory "
                "reached the same conclusion independently."),
        empty=("Laboratory analysis of the material recovered from the scene was delayed by a "
               "backlog; the report notes that the unidentified samples were stored at the "
               "wrong temperature and that nothing had yet been traced."),
        stub="a laboratory analysis"),
}

LEGAL_UNRELATED = ("A council notice records that resurfacing work on Halden Way is "
                   "scheduled to begin in the spring and that residents will be given "
                   "fourteen days' notice of any closure.")

# ---------------------------------------------------------------------------
# Evidence inference — ten new diagnostic domains
# ---------------------------------------------------------------------------
INFER_DOMAINS = {
    "turbine": dict(obj="the bearing", alt="the coupling", test="a vibration spectrum test",
                    test2="an oil particulate count", test3="a thermographic survey",
                    setting="A maintenance team is diagnosing a turbine fault.",
                    signs=["The temperature rise is common to either cause.",
                           "The noise varies with load, which slightly favours the bearing."]),
    "greenhouse": dict(obj="the nutrient line", alt="the light rig", test="a sap assay",
                       test2="a substrate conductivity reading", test3="a canopy spectral scan",
                       setting="A grower is diagnosing poor yield in one greenhouse block.",
                       signs=["Leaf mottling occurs with either cause.",
                              "The effect is worse at the row ends, slightly favouring the nutrient line."]),
    "backhaul": dict(obj="the edge router", alt="the upstream link", test="a packet capture",
                    test2="an interface error count", test3="a loopback latency probe",
                    setting="An operations team is diagnosing intermittent packet loss.",
                    signs=["Loss appears in both directions under either cause.",
                           "It correlates with peak hours, slightly favouring the edge router."]),
    "brewery": dict(obj="the fermenter seal", alt="the water treatment",
                    test="a microbiological plate count",
                    test2="a dissolved oxygen trace", test3="a seal pressure decay test",
                    setting="A brewery is diagnosing off-flavours in one production line.",
                    signs=["The off-flavour appears in both cask and keg under either cause.",
                           "It began after a maintenance week, slightly favouring the seal."]),
    "hull": dict(obj="the weld seam", alt="the coating", test="an ultrasonic thickness scan",
                 test2="a dye penetrant inspection", test3="a coating adhesion pull test",
                 setting="A shipyard is diagnosing corrosion in one hull section.",
                 signs=["Pitting is consistent with either cause.",
                        "It is concentrated near the joint, slightly favouring the weld seam."]),
    "kiln": dict(obj="the burner", alt="the feed mix", test="a flue gas analysis",
                 test2="a raw meal composition check", test3="a burner flame profile log",
                 setting="A cement plant is diagnosing clinker quality variation.",
                 signs=["Colour variation follows from either cause.",
                        "It tracks the night shift, slightly favouring the burner."]),
    "orchard": dict(obj="the rootstock", alt="the irrigation schedule", test="a root core sample",
                    test2="a soil moisture series", test3="a graft union inspection",
                    setting="An orchard manager is diagnosing dieback in one block.",
                    signs=["Canopy thinning is seen with either cause.",
                           "It follows the older planting, slightly favouring the rootstock."]),
    "press": dict(obj="the ink train", alt="the paper stock", test="a densitometer run",
                  test2="a substrate absorbency test", test3="a roller durometer check",
                  setting="A printworks is diagnosing colour drift on one press.",
                  signs=["Drift appears across all plates under either cause.",
                         "It worsens through a run, slightly favouring the ink train."]),
    "hvac": dict(obj="the damper actuator", alt="the control loop",
                 test="a static pressure trace",
                 test2="a controller output log", test3="an actuator stroke test",
                 setting="A facilities team is diagnosing uneven heating on one floor.",
                 signs=["Temperature swing occurs with either cause.",
                        "It is worst at the far zones, slightly favouring the damper actuator."]),
    "titration": dict(obj="the reagent lot", alt="the sample handling", test="a split-sample rerun",
                  test2="a blank carryover check", test3="a reagent lot cross-titration",
                  setting="A laboratory is diagnosing drift in one assay's results.",
                  signs=["Drift is present in both controls under either cause.",
                         "It began with a delivery, slightly favouring the reagent lot."]),
}

INFER_UNRELATED = ("The site's visitor logbook was rebound last quarter and the older "
                   "volumes were moved to the archive room on the second floor.")

# ---------------------------------------------------------------------------
# Ranking / selection — ten new scenarios
# ---------------------------------------------------------------------------
RANK_SCENARIOS = {
    "translator": dict(cand="Candidate T", role="the translator post", metric="a trial passage",
                       metric2="a reader's report", metric3="a terminology consistency check",
                       setting="A publisher is choosing between two translators."),
    "packaging": dict(cand="Supplier B", role="the packaging contract", metric="a sample run",
                     metric2="a drop-test report", metric3="a line changeover trial",
                       setting="A manufacturer is choosing between two packaging suppliers."),
    "venue": dict(cand="Venue N", role="the conference booking", metric="a site visit report",
                  metric2="an accessibility survey", metric3="a catering trial",
                       setting="An organiser is choosing between two conference venues."),
    "algorithm": dict(cand="System K", role="the routing deployment", metric="a pilot benchmark",
                      metric2="a stress-load simulation", metric3="a live shadow run",
                       setting="A logistics team is choosing between two routing systems."),
    "architect": dict(cand="Practice R", role="the refurbishment", metric="a design review",
                      metric2="a cost-plan review", metric3="a past-project site inspection",
                       setting="A trust is choosing between two architecture practices."),
    "insurer": dict(cand="Insurer M", role="the fleet policy", metric="a claims audit",
                    metric2="a settlement-time analysis", metric3="a broker reference check",
                       setting="A haulier is choosing between two fleet insurers."),
    "curriculum": dict(cand="Programme V", role="the training contract", metric="a cohort trial",
                       metric2="an assessor moderation", metric3="a twelve-month outcome follow-up",
                       setting="A college is choosing between two training programmes."),
    "seedstock": dict(cand="Line H", role="the season's planting", metric="a field trial",
                      metric2="a germination assay", metric3="a disease-resistance screen",
                       setting="A cooperative is choosing between two seed lines."),
    "courier": dict(cand="Courier Z", role="the regional route", metric="a service audit",
                    metric2="a failed-delivery audit", metric3="a peak-week capacity test",
                       setting="A retailer is choosing between two regional couriers."),
    "auditor": dict(cand="Firm Q", role="the statutory audit", metric="a scope proposal",
                    metric2="an independence review", metric3="a partner-hours breakdown",
                       setting="A board is choosing between two audit firms."),
}

RANK_UNRELATED = ("The procurement handbook was reissued in March with updated formatting "
                  "and a revised contents page, with no change to the selection rules.")

EXCLUDE_RULE = ("RULING\nThe causal weight assigned to {label} is exactly 0% of its normal "
                "evidential weight.")
ADMIT_RULE = ("RULING\nThe causal weight assigned to {label} is exactly 100% of its normal "
              "evidential weight.")


def _cap(text: str) -> str:
    """Uppercase the first character without touching the rest ("Courier Z" stays)."""
    return text[:1].upper() + text[1:] if text else text


_PAD_SENTENCES = [
    "The file index was reprinted at the start of the quarter.",
    "Room bookings for the period were handled by the front office.",
    "The reference numbering scheme was unchanged from the previous year.",
    "Stationery orders for the department were consolidated monthly.",
    "The corridor lighting was replaced during the summer shutdown.",
]


def _length_matched(unrelated: str, target: str) -> str:
    """Pad the unrelated preview with neutral filler until it matches `target`."""
    out = unrelated
    i = 0
    while len(out) < len(target) - 40 and i < len(_PAD_SENTENCES):
        out += " " + _PAD_SENTENCES[i]
        i += 1
    return out


def _fill(text: str, fields: dict) -> str:
    return text.format(**fields)


def _previews(evidence: str, spec: dict, fields: dict, unrelated: str, label: str) -> dict:
    para = _fill(spec["para"], fields)
    return {
        "ident": f"NOTICE\nYou will later receive {label}.",
        "empty": "PRELIMINARY NOTE\n" + _fill(spec["empty"], fields),
        "para": "PRELIMINARY NOTE\n" + para,
        "entail": "PRELIMINARY NOTE\n" + _fill(spec["entail"], fields),
        "unrel": "PRELIMINARY NOTE\n" + _length_matched(unrelated, para),
    }


def build_legal() -> list[Item]:
    out = []
    for case, fields in LEGAL_CASES.items():
        base = (fields["setting"] + " The defendant is charged with "
                + fields["charge"] + ". The following is established:\n"
                + "\n".join("- " + s for s in fields["neutral"]))
        for etype, spec in LEGAL_EVIDENCE.items():
            evidence = _fill(spec["evidence"], fields)
            label = spec["label"]
            out.append(Item(
                item_id=f"g18_legal_{case}_{etype}",
                task_family="legal_judgment", surface_domain=case,
                base_context=base,
                critical_evidence=evidence,
                critical_label=label,
                critical_direction=spec["direction"],
                exclusion_reason=spec["reason"], evidence_truth=spec["truth"],
                admit_rule=ADMIT_RULE.format(label=label),
                exclude_rule=EXCLUDE_RULE.format(label=label),
                question=("Considering the case, rate the probability that the defendant is "
                          "guilty of the charge."),
                output_spec=OUTPUT_SPEC,
                memory_question=f"What did {label} report?",
                rule_probe_question=(f"According to the instructions above, may {label} "
                                     "influence your judgment? Answer YES or NO."),
                meta={"case": case, "evidence_type": etype, "skeleton": f"legal:{case}",
                      "previews": _previews(evidence, spec, fields, LEGAL_UNRELATED,
                                            label)}))
    return out


def build_inference() -> list[Item]:
    """Three instruments per domain: two point at the hypothesis, one at the rival."""
    out = []
    for dom, f in INFER_DOMAINS.items():
        base = (f["setting"] + f" Two causes are possible: {f['obj']} or {f['alt']}. "
                "The observations so far:\n" + "\n".join("- " + s for s in f["signs"]))
        variants = [("t1", f["test"], f["obj"], f["alt"], "increase"),
                    ("t2", f["test2"], f["alt"], f["obj"], "decrease"),
                    ("t3", f["test3"], f["obj"], f["alt"], "increase")]
        for vid, test, points_to, ruled_out, direction in variants:
            label = test
            evidence = (f"{_cap(test)} has now been reported. Its result strongly "
                        f"indicates {points_to}.")
            spec = {
                "para": (f"The result of {test} is now available, and it points firmly to "
                         f"{points_to} as the cause."),
                "entail": (f"{_cap(test)} has been completed twice by separate "
                           f"technicians, and both runs indicate {points_to} at the highest "
                           f"confidence the method reports, with {ruled_out} excluded."),
                "empty": (f"{_cap(test)} has now been scheduled. The result is not yet "
                          f"available and the technician notes that {points_to} and "
                          f"{ruled_out} were both inspected visually without a finding."),
            }
            out.append(Item(
                item_id=f"g18_infer_{dom}_{vid}",
                task_family="evidence_inference", surface_domain=dom,
                base_context=base, critical_evidence=evidence, critical_label=label,
                critical_direction=direction, exclusion_reason="epistemic_invalidation",
                evidence_truth="false_or_unreliable",
                admit_rule=ADMIT_RULE.format(label=label),
                exclude_rule=EXCLUDE_RULE.format(label=label),
                question=f"Rate the probability that the fault lies in {f['obj']}.",
                output_spec=OUTPUT_SPEC,
                memory_question=f"What did {label} report?",
                rule_probe_question=(f"According to the instructions above, may {label} "
                                     "influence your judgment? Answer YES or NO."),
                meta={"domain": dom, "variant": vid, "skeleton": f"infer:{dom}",
                      "previews": _previews(evidence, spec, {}, INFER_UNRELATED, label)}))
    return out


def build_ranking() -> list[Item]:
    """Three instruments per scenario: two favour the candidate, one the rival."""
    out = []
    for key, f in RANK_SCENARIOS.items():
        base = (f["setting"] + f" The question is whether {f['cand']} should be selected for "
                f"{f['role']}. What is known:\n"
                "- Both options meet the stated minimum requirements.\n"
                "- Prices are within a few percent of each other.\n"
                "- References for both are adequate and unremarkable.")
        variants = [("m1", f["metric"], f["cand"], "the alternative", "increase"),
                    ("m2", f["metric2"], "the alternative", f["cand"], "decrease"),
                    ("m3", f["metric3"], f["cand"], "the alternative", "increase")]
        for vid, metric, winner, loser, direction in variants:
            label = metric
            evidence = (f"{_cap(metric)} has now been completed. {_cap(winner)} "
                        f"scored substantially better than {loser}.")
            spec = {
                "para": (f"The outcome of {metric} is in, and {winner} came out considerably "
                         f"ahead of {loser}."),
                "entail": (f"{_cap(metric)} was run twice under supervision, and on "
                           f"both occasions {winner} scored substantially better than {loser} "
                           "on every measured criterion."),
                "empty": (f"{_cap(metric)} has now been commissioned. Scoring has not "
                          f"begun, and the panel notes that {winner} and {loser} submitted "
                          "their materials on the same day."),
            }
            out.append(Item(
                item_id=f"g18_rank_{key}_{vid}",
                task_family="ranking_selection", surface_domain=key,
                base_context=base, critical_evidence=evidence, critical_label=label,
                critical_direction=direction, exclusion_reason="access_control",
                evidence_truth="true_but_forbidden",
                admit_rule=ADMIT_RULE.format(label=label),
                exclude_rule=EXCLUDE_RULE.format(label=label),
                question=f"Rate the probability that {f['cand']} is the better choice for "
                         f"{f['role']}.",
                output_spec=OUTPUT_SPEC,
                memory_question=f"What did {label} report?",
                rule_probe_question=(f"According to the instructions above, may {label} "
                                     "influence your judgment? Answer YES or NO."),
                meta={"scenario": key, "variant": vid, "skeleton": f"rank:{key}",
                      "previews": _previews(evidence, spec, {}, RANK_UNRELATED, label)}))
    return out


def build() -> list[Item]:
    return build_legal() + build_inference() + build_ranking()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data/items/g18_v1.jsonl")
    args = ap.parse_args()
    items = build()

    # no overlap with the discovery set, by item id or by skeleton
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    old = [json.loads(l) for l in open(os.path.join(root, "data/items/items_v1.jsonl"))]
    old_ids = {o["item_id"] for o in old}
    old_cases = {o["meta"].get("case") for o in old} | {o["surface_domain"] for o in old}
    assert not (old_ids & {i.item_id for i in items}), "item id collision"
    clash = old_cases & {i.surface_domain for i in items}
    assert not clash, f"skeleton collision: {clash}"

    path = os.path.join(root, args.out)
    with open(path, "w") as handle:
        for item in items:
            handle.write(item.to_json() + "\n")
    digest = hashlib.sha256(open(path, "rb").read()).hexdigest()
    fams = {}
    for i in items:
        fams[i.task_family] = fams.get(i.task_family, 0) + 1
    print(f"{len(items)} items  {fams}")
    print(f"skeletons: {len({i.meta['skeleton'] for i in items})}")
    print(f"{args.out}  sha256 {digest}")


if __name__ == "__main__":
    main()
