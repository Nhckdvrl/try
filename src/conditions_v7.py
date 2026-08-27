"""Stage 3E: the two remaining holes in "content-addressed suppression".

P0-A DUPLICATE CONTROL.  The rescue condition shows the evidence twice. A second
      presentation of a fact the model has already read may simply carry less
      marginal weight, which would produce the same drop in REI without any
      exclusion being bound. So the marginal leverage of the later evidence is
      measured directly, with no rule and with an admitting rule, against the
      same previews. An "independent corroboration" framing is included, where a
      second source reporting the same fact should still carry evidential weight.

P0-B PROPOSITION RELATION MATRIX.  "Specific propositional content" is currently
      an authored category. This varies the semantic relation between preview and
      actual evidence systematically: mutual entailment, one-way entailment in
      each direction, a single changed argument, polarity reversal, high lexical
      overlap, and unrelated.
"""
from conditions_v3 import uniform_weight_rule
from conditions_v6 import (preview_text, LEGAL_PARA, LEGAL_SUMM, LEGAL_LEXOVERLAP,
                           UNRELATED_FACT, _fields, INF_PARA, INF_SUMM, INF_LEX)

# --------------------------------------------------------------------------
# extra semantic relations
# --------------------------------------------------------------------------
LEGAL_MORESPECIFIC = {          # preview entails the actual evidence (adds detail)
    "wiretap": ("At 23:52 on the night in question investigators recorded a four-minute "
                "telephone call, placed from a handset registered to {d}, in which {d} said to "
                "a friend: “{quote}.” The audio is clear, an independent expert has confirmed "
                "the voice as {d}'s, and the call log corroborates the time."),
    "search": ("Under a warrant executed at 07:10, officers searched {d}'s {place} and recovered "
               "{item} from a locked cabinet, photographing and logging each item and sealing "
               "them in the presence of a second officer; the defence accepts they were there."),
    "eyewitness": ("At a nine-person identification procedure held eleven days after the events, "
                   "the witness {wit} took under a minute to pick out {d} and stated without "
                   "qualification that {d} was the person {wit} had seen at the scene."),
    "privilege": ("A dated attendance note in {d}'s defence file, signed by {d}'s solicitor, "
                  "places {d} at {alibi} from before the offence until well after it, and "
                  "attaches timestamped third-party records covering every minute of that period, "
                  "which would make {d}'s presence at the scene impossible."),
    "hearsay": ("A neighbour has given a signed statement that {third}, over a period of two "
                "evenings some weeks after the events, told her repeatedly that {third} alone "
                "had carried out {crime} and that {d} had nothing to do with it, giving two "
                "never-published details of the scene that investigators have since confirmed."),
    "lab": ("A full DNA profile obtained from swabs taken at the point of entry, reported by an "
            "accredited laboratory with an intact chain of custody, excludes {d} at every locus "
            "and matches a single unknown male; no trace attributable to {d} was found anywhere "
            "at the scene."),
}
LEGAL_ARGSWAP = {               # same predicate, one argument changed
    "wiretap": ("Investigators recorded a telephone call in which {third} said to a friend: "
                "“{quote}.” The recording is audible and the voice has been confirmed by an "
                "independent expert to be {third}'s."),
    "search": ("Officers searched {third}'s home and found {item}. The items were photographed "
               "and logged, and it is not disputed that they were there."),
    "eyewitness": ("A witness, {wit}, picked {third} out at an identification procedure and "
                   "stated that {third} was the person {wit} saw at the scene."),
    "privilege": ("A note in {third}'s confidential defence file records that {third} was at "
                  "{alibi} at the time in question, with timestamped third-party records "
                  "attached."),
    "hearsay": ("A neighbour has stated that a passing acquaintance told her, some weeks after "
                "the events, that {d} had carried out {crime} alone."),
    "lab": ("A laboratory report concludes that the DNA recovered from the point of entry "
            "excludes {third} entirely and belongs to a single unknown male."),
}
LEGAL_POLARITY = {              # the proposition negated
    "wiretap": ("Investigators have established that no telephone call in which {d} said "
                "anything of the kind was ever made, and that no such recording exists."),
    "search": ("Officers searched {d}'s {place} and found nothing of any relevance; in "
               "particular, no {item} was present."),
    "eyewitness": ("At the identification procedure the witness {wit} was unable to pick anyone "
                   "out and stated that {d} was not the person {wit} saw at the scene."),
    "privilege": ("A note in {d}'s confidential defence file records that {d} was not at "
                  "{alibi} at the time in question and that no record places {d} anywhere else."),
    "hearsay": ("A neighbour has stated that {third} expressly denied to her having had any part "
                "in {crime} and said nothing about {d}."),
    "lab": ("A laboratory report concludes that the DNA recovered from the point of entry does "
            "not exclude {d} and is consistent with {d}'s profile."),
}
INF_MORESPECIFIC = ("{test_c} has now been reported. The instrument was calibrated the same "
                    "morning, the run was duplicated, and both replicates point strongly "
                    "towards {tgt}.")
INF_ARGSWAP = ("A bench test carried out on a different unit altogether has been reported. Its "
               "result points strongly towards {tgt}.")
INF_POLARITY = ("{test_c} has now been reported. Its result points strongly AGAINST {tgt}.")

REL_RUNGS = ["bidir", "morespecific", "abstract", "argswap", "polarity", "lexhigh", "unrelated"]


def relation_preview(item, rel):
    if rel == "unrelated":
        return UNRELATED_FACT
    if item.task_family == "legal_judgment":
        et = item.meta["evidence_type"]
        f = _fields(item)
        tbl = {"bidir": LEGAL_PARA, "morespecific": LEGAL_MORESPECIFIC,
               "abstract": LEGAL_SUMM, "argswap": LEGAL_ARGSWAP,
               "polarity": LEGAL_POLARITY, "lexhigh": LEGAL_LEXOVERLAP}[rel]
        return tbl[et].format(**f)
    surf = item.meta["test"]
    tgt = ("the cause named in the question" if item.critical_direction == "increase"
           else "the alternative cause")
    test_l = surf[0].lower() + surf[1:]
    return {"bidir": INF_PARA.format(test_l=test_l, tgt=tgt),
            "morespecific": INF_MORESPECIFIC.format(test_c=surf, tgt=tgt),
            "abstract": INF_SUMM.format(tgt=tgt),
            "argswap": INF_ARGSWAP.format(tgt=tgt),
            "polarity": INF_POLARITY.format(test_c=surf, tgt=tgt),
            "lexhigh": INF_LEX.format(test_c=surf)}[rel]


# --------------------------------------------------------------------------
# P0-A duplicate control
# --------------------------------------------------------------------------
DUP_PREVIEWS = ["exact", "para", "indep", "unrel"]
DUP_SLOTS = ["only", "norule", "admit", "exclude"]
DUP_CONDITIONS = ([f"dup_{p}_{s}" for p in DUP_PREVIEWS for s in DUP_SLOTS]
                  + ["dup_none_only", "dup_none_norule", "dup_none_admit", "dup_none_exclude"])

# P0-B relation matrix
# each relation also needs a preview-only and a no-rule version, so that the work
# done by the RULE can be separated from the redundancy the preview alone creates
REL_CONDITIONS = ([f"rel_{r}" for r in REL_RUNGS] + ["rel_none"]
                  + [f"relonly_{r}" for r in REL_RUNGS]
                  + [f"relnorule_{r}" for r in REL_RUNGS]
                  + [f"reladmit_{r}" for r in REL_RUNGS])

ALL_V7 = DUP_CONDITIONS + REL_CONDITIONS
V7_ANCHORS = ["base"]


def dup_preview(item, key):
    if key == "none":
        return None
    if key == "exact":
        return item.critical_evidence
    if key == "para":
        return relation_preview(item, "bidir")
    if key == "indep":
        # an explicitly independent second source for the same fact: normally this
        # should still carry evidential weight
        return ("An unconnected second source, working independently of the first, reports the "
                "same thing. " + relation_preview(item, "bidir"))
    return UNRELATED_FACT


def blocks(item, cond, B):
    E = "ADDITIONAL INFORMATION\n" + item.critical_evidence
    if cond.startswith("dup_"):
        _, key, slot = cond.split("_")
        p = dup_preview(item, key)
        pre = ["PRELIMINARY NOTE\n" + p] if p else []
        if slot == "only":
            return [B] + pre                       # preview but no actual evidence
        if slot == "norule":
            return [B] + pre + [E]
        if slot == "admit":
            return [B] + pre + [uniform_weight_rule(item, 1.0), E]
        return [B] + pre + [uniform_weight_rule(item, 0.0), E]
    if cond == "rel_none":
        return [B, uniform_weight_rule(item, 0.0), E]
    for pref, tail in (("relonly_", None), ("relnorule_", "none"),
                       ("reladmit_", "admit"), ("rel_", "exclude")):
        if cond.startswith(pref):
            p = relation_preview(item, cond[len(pref):])
            head = [B, "PRELIMINARY NOTE\n" + p]
            if tail is None:
                return head
            if tail == "none":
                return head + [E]
            if tail == "admit":
                return head + [uniform_weight_rule(item, 1.0), E]
            return head + [uniform_weight_rule(item, 0.0), E]
    raise ValueError(cond)
