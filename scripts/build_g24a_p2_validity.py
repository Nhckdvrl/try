#!/usr/bin/env python3
"""Serialize the Pilot P2 zero-model data-validity dispositions.

Review coverage (all grounded, line-by-line reads of the review material):
  * active 200            : data/items/g24a_p2_review_v1.md
  * consulted reserves    : data/items/g24a_p2_review_reserves_v1.md

Criterion (same as P1, applied per the fixed decision rule registered during
the review): VALID iff taking evidence B as true, the claim would ordinarily
be judged false — disjoint / competing value in the same slot, exclusive-slot
substitution (entity / person / place / date / genre / count), or
unique-relation frame.  INVALID if B entails / contains / supersedes the
claim's property (supertype containment, compatible range, rounding, name
extension, synonym), B is silent / omits (no bearing on the claim's
assertion), B's slot-value is compatible / overlapping, the frame allows
both, or orientation / semantics are broken (including "below"-style
comparatives that make A a non-support, and corrupted B text).  A bridge
between claim subject and evidence subject must be present IN THE TEXT (page
title is never shown to the model: _blocks renders CLAIM + EVIDENCE E only).

Reserve consultation (frozen order, seed_rank ascending): consumed until 44
valid replacements were collected.  Consultation stopped at rank 261 — the
44th valid reserve.  Ranks 262-279 were never reached and remain
unconsumed reserve.  18 consulted reserves were invalid and skipped.

Replacement pairing: k-th invalid ACTIVE (seed order) <-> k-th VALID reserve
(seed order).

Output: data/items/g24a_p2_validity_v1.jsonl  (262 lines:
  200 active + 62 consulted reserves).

Usage: python scripts/build_g24a_p2_validity.py
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

POOL_CSV = "data/items/g24a_p2_pool_v1.csv"
OUT = "data/items/g24a_p2_validity_v1.jsonl"
SEED = 20260927
N_ACTIVE, N_RESERVE = 200, 80
# Last reserve rank actually consulted (44th valid replacement found there).
CONSULTED_THROUGH = 261
N_INVALID_ACTIVE = 44

# --- verdicts (mine, zero model output consulted) --------------------------
# Invalid ACTIVE pairs (frozen list, mirrored in review_g24a_p2_reserves.py).
INVALID_ACTIVE = {
    7: "E_R drops 'Waka Flocka Flame' from a non-exhaustive collaborator list - "
       "absence != refutation (omission)",
    8: "E_R's snapshot is dated March 1 - the claim's 'as of February 26' count "
       "is unaddressed; 3-on-March-1 is compatible with 3-on-Feb-26 (as-of shift)",
    9: "E_R lists other stints (Grizzlies HC; Hawks/Warriors/Heat assistants) "
       "and omits the Knicks entirely - omission from a career list; claim also "
       "says 'manager' vs evidence 'head coach'",
    13: "'the men' (claim/A) vs E_R 'his Royal Marines' - Royal Marines satisfy "
        "'the men'; E_R compatible, no refutation",
    22: "E_R 'latest September Security Patches' does not deny earlier "
        "(pre-September) patches - claim survives (compatible)",
    25: "containment: 'Canadian' subset of 'Canadian-Iranian' - claim true "
        "under E_R",
    30: "containment: 'Australian' subset of 'Scottish-Australian' - claim true "
        "under E_R",
    31: "E_R 'reunited Islamic Arab Spain' contains the claim's event; the "
        "claim's 'in the region of Murcia' locative is absent from both "
        "evidences - no refutation",
    32: "specification: E_R 'assistants to qualified lawyers' refines the "
        "claim's 'assistants to lawyers' - compatible, no refutation",
    42: "E_R's snapshot is 'through week 11' - the claim's pre-week-11 "
        "standing is unaddressed; compatible (as-of shift)",
    45: "E_R switches the subject to economic reforms; the claim's 'political "
        "ideals' is unaddressed (topic shift)",
    50: "E_R states cause of death (cancer) without duration - the claim's "
        "'brief period' is unaddressed; compatible",
    52: "E_R substitutes a different event ('their first date') - it does not "
        "deny the puppies (no bearing)",
    56: "'steamed milk' is warm milk - E_R satisfies the claim's 'warm milk' "
        "(compatible)",
    61: "'American' does not deny 'African-American' - claim compatible under "
        "E_R (broad category)",
    63: "containment: Wales subset of Britain - 'Welsh singer' entails "
        "'British singer-songwriter' - claim true under E_R",
    78: "E_R narrows the superlative to the X-Men franchise - compatible with "
        "the claim's global 'worst of all time' (not denied)",
    80: "claim 'below the 5th most successful' vs A '1th' / B '9th' - the "
        "comparative 'below' makes direction incoherent with A (A does not "
        "support) - orientation/semantics broken",
    86: "E_R is an orthographic variant of E_A ('18 Street and 26 Avenue' vs "
        "'18th Street and 26th Avenue') - same facts; E_R also supports",
    90: "E_R reattributes 'first and only' to Jackson's interception, not to "
        "Ryan's pass - the claim (Ryan's only pass intercepted) is unaddressed",
    95: "'PlayStation' names the same console as 'PlayStation 1' - E_R also "
        "supports (name variant)",
    97: "E_R text is corrupted ('named her a famous flat earth theorist Dane "
        "GibbonsLiv Ullmann') - malformed, direction not evaluable (broken text)",
    100: "E_R 'negative to mixed' contains 'mixed' - claim true under E_R",
    106: "containment: 'Contemporary R & B' subset of 'R & B' - claim true "
         "under E_R",
    109: "name extension: 'Mohammad Tarif' subset of 'Mohammad Tarif Ansari' - "
         "same person; claim true under E_R",
    118: "E_R 'over 50 million as of 20 January' does not exclude 50.1M by 21 "
         "January - claim survives (as-of state compatible)",
    119: "containment: a mixtape is a project - claim ('a project') true under "
         "E_R",
    124: "E_R extends the region ('northeastern Iran and southwestern Pakistan') "
         "and retains the claim's clause - claim true under E_R",
    127: "Kashi and Varanasi are the same city - E_R also satisfies the claim "
         "(synonym place)",
    139: "E_R relocates the custom (Saudi Arabia/Uzbekistan); it does not deny "
         "the US/Canada practice - no bearing",
    151: "claim 'below the 24rd most viewed' vs A '23rd' - 23rd ranks above "
         "24th; 'below' makes A a non-support - orientation/semantics broken",
    152: "Teesside and North Yorkshire overlap for Yarm - E_R does not deny the "
         "Teesside locative (compatible)",
    155: "E_R names the medley track '911 / Mr. Lonely' - the rendition may sit "
         "in its '911' segment; claim not denied (compatible)",
    157: "containment: England subset of Britain - 'English' entails 'British' - "
         "claim true under E_R",
    162: "E_R 'positive to mixed' spans a range including the claim's 'diverse' "
         "- claim true under E_R (compatible range)",
    166: "E_R closes a different unit (Rocky Mountain National Park vs National "
         "Forest) - a park closure does not deny the forest's closure (no bearing)",
    168: "containment: 'action thriller' contains 'action' - claim true under E_R",
    173: "A's zero point 544 BCE precedes 500 BCE (BCE ordering) - A does not "
         "support 'year 0 is after 500 BCE'; B (483 BCE) would - orientation reversed",
    182: "E_R gives a 10-13 million range whose upper bound contains the claim's "
         "13 million - claim survives (compatible)",
    183: "containment: heavy metal subset of rock - claim true under E_R",
    188: "E_R 'around the year 1000' spans 1001 - claim true under E_R (fuzzy "
         "date contains the claim's year)",
    195: "E_R concerns iOS 9.3.2 (different version) and is silent on iOS 9.3's "
         "release date - no bearing",
    197: "'Spain father' does not deny 'Basque father' (Basque subset of Spain) "
         "- claim compatible under E_R",
    199: "E_R $4,936,851 rounds to $4.9 million - claim true under E_R (rounding)",
}

# Invalid CONSULTED reserves (skipped, not eligible for the pairing).
INVALID_RESERVE = {
    205: "E_R is about a different product (PlayStation Vita); the claim's "
         "subject (Nintendo Switch) does not appear - no bearing",
    206: "E_R parses as the Nashville divisions of ... Capitol Records, i.e. "
         "Capitol Records Nashville - E_R also supports the claim",
    209: "E_R names the place ('the coastal town of Hastings'); the claim "
         "characterizes it ('dilapidated coastal resort') - compatible, no refutation",
    210: "E_R 'adapted from the Chippewa word Kinoje' is compatible with 'an "
         "English version of Kinoje' - no refutation",
    212: "'physical media May 6th' = 'home media May 6' - E_R also supports",
    221: "E_R as-of 'By 20 March' is earlier than the claim's 'by 22 March' - "
         "an earlier bound entails the claim - E_R also supports",
    222: "containment: 'hard rock' subset of 'rock' - claim true under E_R",
    226: "'twelfth album' does not deny 'twelfth studio album' - claim "
         "compatible under E_R",
    229: "name variant: 'Steve Carell' is the same person as 'Steven John "
         "Carell' - E_R also supports",
    236: "containment: 'post-rock' subset of 'rock' - claim true under E_R",
    241: "E_R's subject is a different band ('Zombie'); the claim's subject "
         "(Cannibal Corpse) is absent - no bearing",
    243: "no in-text bridge: claim subject 'Shotti' never appears in evidence "
         "('Kifano Jordan') - claim not evaluable from claim + evidence alone",
    244: "containment: 'pop country' subset of 'country' - claim true under E_R",
    249: "near-paraphrase: 'feeling worthless' is compatible with 'depressed' - "
         "E_R does not refute",
    251: "E_R's as-of '3 March' does not address the claim's pre-Feb-20 window "
         "- compatible",
    253: "E_R's split run (1998-2006, 2017-2020) still spans 1998-2020 - the "
         "claim's tenure-span remains true (compatible)",
    256: "open 'also known for' list: E_R substitutes another item (Diva search "
         "contestant); no exclusion of the claim's wrestler role (compatible)",
    257: "a fourth module is beyond the second - E_R supports the claim's 'go "
         "beyond the second module'",
}

# Valid ACTIVE pairs worth a note; everything else valid = "ok".
KEEP_NOTES_ACTIVE = {
    2: "genre reclassification in lead: 'erotic drama' vs 'comedy-drama' - "
       "competing labels, direction ok",
    23: "distributor substitution in the release frame (20th Century Fox vs "
        "Walt Disney Studios); claim's 'produced' clause unaddressed on both "
        "sides - direction ok",
    34: "weak: E_R's 'as well as deaths' attachment ambiguous - read as "
        "removing the third-highest deaths rank, direction ok",
    35: "title variant: E_R lacks the 'The Escapist:' prefix - claim's full "
        "title contradicted as stated, direction ok",
    36: "genre reclassification: 'rap rock' vs 'heavy metal' - competing "
        "labels, direction ok",
    40: "category substitution: 'the album' vs 'the EP' - EP is not an album "
        "category-wise, direction ok",
    46: "same starring frame, film title substituted ('Wall Street: LES' vs "
        "'Butch and Sundance: LES'); cast also differs - direction ok",
    51: "claim phrasing odd ('The game Game Grumps'); direction clean: created "
        "2012 (A) vs 1999 (B) vs after-2005",
    64: "character-name substitution (Faheem vs Faizal Khan); claim's truncated "
        "title matches A-side truncation - direction ok",
    88: "release-year doctored on A side (2008-02-21); direction clean: "
        "after-2005-02-20 (A) vs 2005-02-14 (B)",
    110: "genre reclassification: 'Indie rock' vs 'pop rock' - competing "
         "labels, direction ok",
    129: "tense: 'will release' (claim/A: yet to be released) vs E_R completed "
         "release June 8 2018 - direction ok",
    135: "weak-inferential: release year inferred from the cameo/role year "
         "(A: 1998, B: 1988) - direction ok",
    141: "competing location designations in the same slot ('Occupied-"
         "Palestine' vs 'Israel') - direction ok",
    146: "regiment-number substitution (160th vs 186th) in the same "
         "affiliation slot - direction ok",
    147: "nationality substitution ('Australian' vs 'Welsh') - disjoint labels "
         "for the singer; E_R's 'Australian' modifies the band - direction ok",
    156: "geopolitical: 'Ireland' vs 'Northern Ireland' - island reading "
         "compatible, state reading contradictory; kept with note",
    161: "count: A enumerates four studio albums (claim <5); B enumerates five "
         "(claim false); Christmas album/EP counting ambiguous in A - direction ok",
    165: "verb substitution ('stopping' vs 'diverting the flood') - competing "
         "actions of the same event, direction ok",
    174: "meaning substitution ('one who goes' vs 'one who is sent'); Greek "
         "text mojibake in both evidences but the key phrase differs - direction ok",
    178: "B is a direct negation of A (wouldn't find success / lose first "
         "division championship) - clean refutation",
    186: "coiner substitution (Herbie Hancock vs DJ Babu); A-side text garbled "
         "after the key clause but the attribution is clear - direction ok",
    191: "A-side internally odd (quadruple platinum vs 'a million copies') but "
         "states one million (<2M); B states four million (>=2M) - direction ok",
}

# Valid CONSULTED reserves worth a note.
KEEP_NOTES_RESERVE = {
    200: "E_R moves the same $27.7M gross to opening day - refutes the claim's "
         "four-day span (the 'ahead of South Park' conjunct is unaddressed in "
         "E_R) - direction ok",
    202: "weak: E_R supplies a competing identity ('a Scottish rock band' with "
         "different members) - push-down on 'Nick Knowles' backup band' but not "
         "a strict contradiction - kept with note",
    216: "weak: claim says 'fans gave' but neither evidence names the givers; "
         "E_R specifies 'from critics' - direction-correct attribution conflict "
         "(fan vs critic givers not strictly exclusive) - kept with note",
    224: "claim/A carry the malformed figure '2,9662,966'; E_R states 2,962 - "
         "numeric conflict clean despite the malformed claim text",
    225: "doctored scene qualifier: claim 'in the Donner building' (A verbatim) "
         "vs E_R 'in the Donner version' - same-frame competing qualifier; weak "
         "but direction ok",
    228: "weak: E_R drops 'and the fans' from the pushback (Miramax vs Akkad) - "
         "omission in a closed decision frame; mild push-down, direction ok",
    242: "claim spells the subject 'Cassius Lee Mars' (evidence: 'Marsh') - "
         "one-letter variant; direction clean (free agent vs 49ers)",
    261: "claim's first name 'Ron' (evidence: surname only); rank/title "
         "conflict (Vice-Chairman/fifth vs Chairman/fourth) is clean",
}


def main() -> None:
    pool = list(csv.DictReader(open(POOL_CSV, encoding="utf-8")))
    assert len(pool) == N_ACTIVE + N_RESERVE, len(pool)
    active = sorted(
        (r for r in pool if r["active_200"] == "yes"),
        key=lambda r: int(r["seed_rank"]),
    )
    reserve = sorted(
        (r for r in pool if r["active_200"] == "no"),
        key=lambda r: int(r["seed_rank"]),
    )
    assert [int(r["seed_rank"]) for r in active] == list(range(N_ACTIVE))
    assert [int(r["seed_rank"]) for r in reserve] == list(range(200, 200 + N_RESERVE))

    # Frozen verdicts must reference only real ranks.
    assert sorted(INVALID_ACTIVE) == [
        7, 8, 9, 13, 22, 25, 30, 31, 32, 42, 45, 50, 52, 56, 61, 63, 78, 80,
        86, 90, 95, 97, 100, 106, 109, 118, 119, 124, 127, 139, 151, 152, 155,
        157, 162, 166, 168, 173, 182, 183, 188, 195, 197, 199,
    ], "invalid-active list drifted from the frozen 44"
    assert len(INVALID_ACTIVE) == N_INVALID_ACTIVE

    consulted = [r for r in reserve if int(r["seed_rank"]) <= CONSULTED_THROUGH]
    consulted_ranks = [int(r["seed_rank"]) for r in consulted]
    assert consulted_ranks == list(range(200, CONSULTED_THROUGH + 1)), consulted_ranks

    valid_reserve = [
        int(r["seed_rank"])
        for r in consulted
        if int(r["seed_rank"]) not in INVALID_RESERVE
    ]
    invalid_consulted = [
        int(r["seed_rank"])
        for r in consulted
        if int(r["seed_rank"]) in INVALID_RESERVE
    ]
    assert len(valid_reserve) == N_INVALID_ACTIVE, len(valid_reserve)
    assert len(invalid_consulted) == 18, len(invalid_consulted)
    # Every consulted rank carries a verdict.
    assert set(invalid_consulted) == set(INVALID_RESERVE), "reserve verdicts drift"
    assert all(r in valid_reserve or r in INVALID_RESERVE for r in consulted_ranks)

    # Pairing: k-th invalid active <-> k-th valid reserve (seed order).
    invalid_actives = sorted(INVALID_ACTIVE)
    pairing = dict(zip(invalid_actives, valid_reserve))

    by_rank = {int(r["seed_rank"]): r for r in pool}
    entries = []

    for r in active:
        rank = int(r["seed_rank"])
        e = {
            "seed_rank": rank,
            "p2_id": r["p2_id"],
            "case_id": r["case_id"],
            "claim_sha": r["claim_sha"],
            "role": "active",
            "reviewed": True,
        }
        if rank in INVALID_ACTIVE:
            e["verdict"] = "invalid"
            e["note"] = INVALID_ACTIVE[rank]
            repl = pairing[rank]
            e["replaced_by_rank"] = repl
            e["replaced_by_p2_id"] = by_rank[repl]["p2_id"]
        else:
            e["verdict"] = "valid"
            e["note"] = KEEP_NOTES_ACTIVE.get(rank, "ok")
        entries.append(e)

    for rank in consulted_ranks:
        r = by_rank[rank]
        e = {
            "seed_rank": rank,
            "p2_id": r["p2_id"],
            "case_id": r["case_id"],
            "claim_sha": r["claim_sha"],
            "role": "reserve",
            "reviewed": True,
        }
        if rank in INVALID_RESERVE:
            e["verdict"] = "invalid"
            e["note"] = INVALID_RESERVE[rank]
        else:
            e["verdict"] = "valid"
            e["note"] = KEEP_NOTES_RESERVE.get(rank, "ok")
            replaced = [a for a, b in pairing.items() if b == rank]
            assert len(replaced) == 1
            e["replaces_rank"] = replaced[0]
            e["replaces_p2_id"] = by_rank[replaced[0]]["p2_id"]
        entries.append(e)

    entries.sort(key=lambda e: e["seed_rank"])
    with open(OUT, "w", encoding="utf-8") as f:
        for e in entries:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")

    # Read-back verification.
    back = [json.loads(x) for x in Path(OUT).read_text(encoding="utf-8").splitlines()]
    assert len(back) == N_ACTIVE + len(consulted_ranks), len(back)
    assert len({e["p2_id"] for e in back}) == len(back)
    inv_a = [e for e in back if e["role"] == "active" and e["verdict"] == "invalid"]
    val_a = [e for e in back if e["role"] == "active" and e["verdict"] == "valid"]
    val_r = [e for e in back if e["role"] == "reserve" and e["verdict"] == "valid"]
    inv_r = [e for e in back if e["role"] == "reserve" and e["verdict"] == "invalid"]
    assert (len(inv_a), len(val_a), len(val_r), len(inv_r)) == (44, 156, 44, 18), (
        len(inv_a), len(val_a), len(val_r), len(inv_r),
    )
    # Bijective pairing, complete chains.
    assert {e["replaced_by_rank"] for e in inv_a} == {e["seed_rank"] for e in val_r}
    assert {e["replaces_rank"] for e in val_r} == {e["seed_rank"] for e in inv_a}
    assert all("replaced_by_p2_id" in e for e in inv_a)
    assert all("replaces_p2_id" in e for e in val_r)
    # The final run set: 156 surviving actives + 44 replacement reserves = 200
    # unique claims/cases.
    final = [e for e in back if e["verdict"] == "valid"]
    assert len(final) == 200
    assert len({e["p2_id"] for e in final}) == 200
    assert len({e["case_id"] for e in final}) == 200
    # No unconsumed reserve appears with a verdict; the pairing is in seed order.
    assert max(e["seed_rank"] for e in back) == CONSULTED_THROUGH
    for e in val_r:
        assert e["replaces_rank"] < e["seed_rank"]

    print(f"OK -> {OUT}")
    print(f"  lines: {len(back)} = 200 active + {len(consulted_ranks)} consulted reserve")
    print(f"  active: {len(val_a)} valid / {len(inv_a)} invalid")
    print(f"  consulted reserve: {len(val_r)} valid (all consumed) / "
          f"{len(inv_r)} invalid (skipped)")
    print(f"  final run set: {len(final)} unique claims "
          f"(consulted through rank {CONSULTED_THROUGH})")


if __name__ == "__main__":
    main()
