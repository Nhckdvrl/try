"""Stage-2 condition families.

Three experiments, all compiled from the same frozen items, designed to separate
the accounts that the diffusion result leaves standing:

  H-A  decision proximity   -- instructions nearer the answer are weighted more
  H-B  prospective binding  -- a rule about not-yet-seen evidence cannot attach
                              to a concrete span
  H-C  linguistic scope     -- "the preceding evidence" is a clearer referent
                              than a forward reference

POSITION  crosses rule type x before/after x distance-to-answer, so that
          Before/After and Distance can be fitted as separate terms.
IDBIND    removes directional anaphora entirely by giving the evidence a label
          and using one identical rule sentence in both orders.
WEIGHT    replaces the binary use/ignore rule with a requested weight in
          {0, .25, .5, .75, 1}, turning the question into how accurately a model
          implements a requested evidence weight at each position.
"""

# --------------------------------------------------------------------------
# neutral filler: clerical file entries, no meta-commentary about relevance,
# nothing that bears on any judgment. Used only to vary rule->answer distance.
# --------------------------------------------------------------------------
_FILLER_UNITS = [
    "File reference {n}/{y}-A was opened by the records office and assigned to the "
    "standard review queue on {d} {m}.",
    "A duplicate of the file index was produced for the archive and stored under "
    "shelf mark {n}-{y}; the original index remains with the case bundle.",
    "The pagination of the bundle was checked against the index on {d} {m} and the "
    "page count was recorded as {n} sheets.",
    "Correspondence relating to scheduling was filed separately in the "
    "administrative annex under reference {y}/{n}.",
    "The file was transferred between the {m} and the following month's storage "
    "rotation without alteration to its contents.",
    "A routine retention check was completed on {d} {m}; the retention period was "
    "recorded as {r} years from the date of opening.",
    "The cover sheet was reprinted after the original became illegible; no entries "
    "were added, removed or amended.",
    "An access log entry was created when the bundle was consulted by the records "
    "office on {d} {m}.",
]
_MONTHS = ["January", "March", "April", "June", "July", "September", "October", "November"]


def stable_seed(s: str) -> int:
    """Python's hash() is salted per process, which would make the filler differ
    between runs. Use a content hash instead."""
    import zlib
    return zlib.crc32(s.encode()) % 100000


def filler_block(n_units: int, seed: int) -> str:
    """`n_units` clerical entries. Deterministic given the seed."""
    if n_units <= 0:
        return None
    import random
    rng = random.Random(seed)
    lines = []
    for i in range(n_units):
        t = _FILLER_UNITS[(seed + i) % len(_FILLER_UNITS)]
        lines.append("- " + t.format(n=rng.randrange(100, 999), y=rng.randrange(11, 24),
                                     d=rng.randrange(2, 28), m=rng.choice(_MONTHS),
                                     r=rng.choice([5, 7, 10, 12, 15])))
    return "ADMINISTRATIVE RECORD\n" + "\n".join(lines)


# distance levels: number of filler entries between the last content block and TASK
FILLER_LEVELS = {"d0": 0, "d1": 6, "d2": 18}

POSITION_CONDITIONS = [f"pos_{r}_{a}_{d}"
                       for r in ("adm", "exc") for a in ("pre", "post") for d in FILLER_LEVELS]


def position_blocks(item, B, E, Radm, Rexc, cond):
    _, rule, arm, dist = cond.split("_")
    R = Radm if rule == "adm" else Rexc
    blocks = [B, R, E] if arm == "pre" else [B, E, R]
    f = filler_block(FILLER_LEVELS[dist], seed=stable_seed(item.item_id))
    if f:
        blocks.append(f)
    return blocks


# --------------------------------------------------------------------------
# ID binding: one identical rule sentence, no "preceding" / "following"
# --------------------------------------------------------------------------
ID_PREAMBLE = ("Evidence blocks in this file carry identifiers. One of them is "
               "labelled E7.")
ID_EXCLUDE = ("RULING\nEvidence E7 is excluded. It must have zero influence on your "
              "final judgment.")
ID_ADMIT = ("RULING\nEvidence E7 is admitted. It must be given the full weight of a "
            "verified item in your final judgment.")

IDBIND_CONDITIONS = ["id_base", "id_admit_pre", "id_admit_post",
                     "id_exclude_pre", "id_exclude_post", "id_exclude_pre_marker"]


def idbind_blocks(item, cond):
    B = "BACKGROUND\n" + item.base_context + "\n" + ID_PREAMBLE
    E = "EVIDENCE E7\n" + item.critical_evidence
    E_marked = "EVIDENCE E7 — EXCLUDED\n" + item.critical_evidence
    if cond == "id_base":
        return [B]
    if cond == "id_admit_pre":
        return [B, ID_ADMIT, E]
    if cond == "id_admit_post":
        return [B, E, ID_ADMIT]
    if cond == "id_exclude_pre":
        return [B, ID_EXCLUDE, E]
    if cond == "id_exclude_post":
        return [B, E, ID_EXCLUDE]
    if cond == "id_exclude_pre_marker":
        # the rule appears once, before the evidence; the evidence block then
        # carries only a binding cue, never a restatement of the rule
        return [B, ID_EXCLUDE, E_marked]
    raise ValueError(cond)


# --------------------------------------------------------------------------
# Requested-weight sweep
# --------------------------------------------------------------------------
WEIGHTS = {"w000": ("no weight at all: it must have zero influence on your judgment", 0.00),
           "w025": ("one quarter of the weight you would give a verified item", 0.25),
           "w050": ("half the weight you would give a verified item", 0.50),
           "w075": ("three quarters of the weight you would give a verified item", 0.75),
           "w100": ("the full weight you would give a verified item", 1.00)}

WEIGHT_CONDITIONS = [f"{w}_{a}" for w in WEIGHTS for a in ("pre", "post")]


def weight_rule(item, key):
    phrase, _ = WEIGHTS[key]
    return (f"RULING\nA weighting decision has been made about {item.critical_label}. "
            f"Give it {phrase}.")


def weight_blocks(item, B, E, cond):
    key, arm = cond.split("_")
    R = weight_rule(item, key)
    return [B, R, E] if arm == "pre" else [B, E, R]


ALL_V2 = POSITION_CONDITIONS + IDBIND_CONDITIONS + WEIGHT_CONDITIONS
