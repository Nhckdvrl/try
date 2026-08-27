"""P0.5 Semantic addressability.

P1-8 showed that a preview of the evidence before the rule restores suppression.
But that preview was the *same string*, so it cannot distinguish

  (a) the rule needs a semantic representation of its target at rule time, from
  (b) the rule only suppresses text it has already seen verbatim.

The preview is now varied along a similarity ladder while the evidence the
decision reads is held fixed, and a 2x2 orthogonally manipulates whether the
later item matches the preview in CONTENT and whether it matches the rule in
symbolic IDENTITY.

Restricted to legal_judgment and evidence_inference, whose critical evidence is
templated, so every rung is authored once per evidence type rather than per item.
"""
_SIB = None


def _siblings():
    """(case, direction) -> list of evidence strings, for the same-direction
    different-fact rung. Built from the generators, so no frozen item changes."""
    global _SIB
    if _SIB is None:
        import gen_legal
        m = {}
        for it in gen_legal.build():
            m.setdefault((it.meta["case"], it.critical_direction), []).append(
                (it.meta["evidence_type"], it.critical_evidence))
        _SIB = m
    return _SIB


NEUTRAL_QUOTE = ("I'll pick the kids up at six and grab something for dinner on the way")
TOPIC_FACT = ("The investigating officer's notes for this case were typed up and added to "
              "the bundle on the following Monday.")
UNRELATED_FACT = ("A council notice records that resurfacing work on Halden Way will begin "
                  "in the spring.")

# per legal evidence type: a lexical paraphrase (same proposition, different words)
# and an entailing summary (core proposition only, no verbatim content)
LEGAL_PARA = {
    "wiretap": ("A telephone conversation was captured by investigators. Speaking privately to "
                "a friend, {d} stated: “{quote}.” The audio is of good quality and "
                "expert analysis confirms the speaker to be {d}."),
    "search": ("Acting on a warrant application, officers went through {d}'s {place} and "
               "recovered {item}. Photographs and a log were made, and the defence accepts the "
               "items were there."),
    "eyewitness": ("At an identification procedure the witness {wit} selected {d}, saying that "
                   "{d} was the person {wit} had seen at the scene."),
    "privilege": ("{d}'s defence file holds a note by {d}'s lawyer placing {d} at {alibi} at the "
                  "material time, with timestamped third-party records attached that would rule "
                  "out {d}'s presence at the scene."),
    "hearsay": ("A neighbour reports that {third} admitted to her, weeks afterwards, that {third} "
                "alone had carried out {crime} and that {d} was not involved; she says {third} "
                "gave two never-published details of the scene that investigators have confirmed."),
    "lab": ("Laboratory analysis of DNA taken from the point of entry rules {d} out and assigns "
            "the profile to one unidentified male, with nothing at the scene traceable to {d}."),
}
LEGAL_SUMM = {
    "wiretap": ("Investigators hold an audio recording in which {d}, speaking privately, makes a "
                "statement that is self-incriminating on this charge."),
    "search": ("A search of premises controlled by {d} recovered material that is incriminating "
               "on this charge."),
    "eyewitness": ("A witness has positively identified {d} as the person at the scene."),
    "privilege": ("Material in {d}'s defence file would establish that {d} was elsewhere when "
                  "the offence took place."),
    "hearsay": ("There is a second-hand report that another named person confessed to this "
                "offence and exonerated {d}."),
    "lab": ("Forensic analysis of material from the scene excludes {d} and points to an "
            "unidentified person."),
}
LEGAL_LEXOVERLAP = {
    "wiretap": ("Investigators recorded a telephone call in which {d} said to a friend: "
                "“" + NEUTRAL_QUOTE + ".” The recording is audible and the voice has "
                "been confirmed by an independent expert to be {d}'s."),
    "search": ("Officers searched {d}'s {place} and found a folder of household bills and an old "
               "bicycle pump. The items were photographed and logged, and the defence does not "
               "dispute that they were there."),
    "eyewitness": ("A witness, {wit}, attended an identification procedure and stated that none "
                   "of the people shown was the person {wit} saw at the scene."),
    "privilege": ("A note in {d}'s confidential defence file, written by {d}'s lawyer, records "
                  "that the next case conference is to be scheduled for the following month."),
    "hearsay": ("A neighbour has stated that {third} told her, some weeks after the events, that "
                "{third} had been away from the area for the whole of that period and knew "
                "nothing about it."),
    "lab": ("A laboratory report records that the samples recovered from the scene were of "
            "insufficient quality for any profile to be obtained, so no comparison with {d} or "
            "anyone else was possible."),
}

INF_PARA = ("The outcome of {test_l} is now in, and it points strongly towards {tgt}.")
INF_SUMM = ("A test result now on file points strongly towards {tgt}.")
INF_LEX = ("{test_c} has now been reported. Its result is inconclusive between the two causes.")
INF_SAMEDIR = ("A further observation, made independently of the test, also favours {tgt}.")
INF_TOPIC = ("The job sheet for this case was updated with the current date and refiled.")

RUNGS = ["none", "exact", "para", "summ", "samedir", "lexoverlap", "topic", "unrelated"]
SEM_CONDITIONS = [f"sem_{r}" for r in RUNGS] + ["sem_base", "sem_full"]

# content x identity 2x2, each with a matched full-weight anchor
SWAP_CONDITIONS = [f"swap_{c}_{i}_{w}" for c in ("same", "diff")
                   for i in ("e7", "e9") for w in ("z", "f")] + ["swap_base"]

ALL_V6 = SEM_CONDITIONS + SWAP_CONDITIONS
V6_FAMILIES = ("legal_judgment", "evidence_inference")
RULE_0 = "RULING\nEvidence E7 has decision weight 0."
RULE_1 = "RULING\nEvidence E7 has decision weight 1."


def _fields(item):
    """Template fields for the legal families, recovered from the generator."""
    import gen_legal
    for c in gen_legal.CASES:
        if c["cid"] == item.meta.get("case"):
            return c
    return {}


def preview_text(item, rung):
    """The preview block placed BEFORE the rule. None means no preview."""
    if rung in ("none",):
        return None
    if rung == "exact":
        return item.critical_evidence
    if rung == "unrelated":
        return UNRELATED_FACT
    if item.task_family == "legal_judgment":
        et = item.meta["evidence_type"]
        f = _fields(item)
        if rung == "para":
            return LEGAL_PARA[et].format(**f)
        if rung == "summ":
            return LEGAL_SUMM[et].format(**f)
        if rung == "lexoverlap":
            return LEGAL_LEXOVERLAP[et].format(**f)
        if rung == "topic":
            return TOPIC_FACT
        if rung == "samedir":
            sibs = _siblings().get((item.meta["case"], item.critical_direction), [])
            for k, txt in sibs:
                if k != et:
                    return txt
            return None
    else:                                   # evidence_inference
        surf = item.meta["test"]
        tgt = ("the cause named in the question" if item.critical_direction == "increase"
               else "the alternative cause")
        test_l = surf[0].lower() + surf[1:]
        if rung == "para":
            return INF_PARA.format(test_l=test_l, tgt=tgt)
        if rung == "summ":
            return INF_SUMM.format(tgt=tgt)
        if rung == "lexoverlap":
            return INF_LEX.format(test_c=surf)
        if rung == "topic":
            return INF_TOPIC
        if rung == "samedir":
            return INF_SAMEDIR.format(tgt=tgt)
    return None


def other_evidence(item):
    """A different fact for the same case, used as the swapped content."""
    if item.task_family != "legal_judgment":
        return None
    sibs = _siblings().get((item.meta["case"], item.critical_direction), [])
    for k, txt in sibs:
        if k != item.meta["evidence_type"]:
            return txt
    return None


def blocks(item, cond, B):
    E7 = "EVIDENCE E7\n" + item.critical_evidence
    if cond == "sem_base":
        return [B]
    if cond == "sem_full":
        return [B, E7, RULE_1]
    if cond.startswith("sem_"):
        p = preview_text(item, cond[4:])
        pre = ["PRELIMINARY NOTE\n" + p] if p else []
        return [B] + pre + [RULE_0, E7]
    if cond == "swap_base":
        return [B]
    if cond.startswith("swap_"):
        _, content, ident, w = cond.split("_")
        other = other_evidence(item)
        actual = item.critical_evidence if content == "same" else (other or item.critical_evidence)
        label = "E7" if ident == "e7" else "E9"
        R = RULE_0 if w == "z" else RULE_1
        return [B, "PRELIMINARY NOTE\n" + item.critical_evidence, R,
                f"EVIDENCE {label}\n" + actual]
    raise ValueError(cond)


def swap_usable(item):
    return item.task_family == "legal_judgment" and other_evidence(item) is not None
