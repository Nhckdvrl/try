#!/usr/bin/env python3
"""G24A fresh exact-evidence-pair census (Layer-2 feasibility, zero compute).

Question (user, 2026-09-25): in the frozen 13,283-candidate pool MINUS the
600 items already used for discovery, how many byte-exact same-evidence
groups carry at least one increase claim AND at least one decrease claim?

Rules:
  * byte-exact `critical_evidence` equality defines a group
  * remove the 600 discovery item_ids first (13,283 -> 12,683)
  * remove any group whose evidence SHA256[:10] is one of the 53 discovery
    opposite-direction evidence groups (freshness, explicit user rule)
  * NO model output is read (asserted), no kill gates, observations only
  * descriptive claim-form taxonomy via deterministic rules; a blind human-
    level audit of a random sample is reported separately (pending at v1)
  * claim lexical similarity / entity overlap: description only, never a
    filter

Inputs : data/items/g24a_candidates_v1.jsonl (frozen pool, selection-pass
         input), data/items/g24a_v1.jsonl (discovery set)
Outputs: results/discovery/g24a_fresh_pair_census_v1.{md,json}
         results/discovery/g24a_fresh_pair_census_v1_groups.csv

Usage  : python scripts/census_g24a_fresh_pairs.py
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import statistics as st
import sys
from collections import Counter, defaultdict
from pathlib import Path

CANDIDATES = "data/items/g24a_candidates_v1.jsonl"
DISCOVERY = "data/items/g24a_v1.jsonl"
OUT_PREFIX = "results/discovery/g24a_fresh_pair_census_v1"
EXPECTED_CANDIDATES = 13283
EXPECTED_DISCOVERY = 600
EXPECTED_DISC53 = 53

# --- deterministic claim-form rules (descriptive; audited separately) -----
# precedence: negation > exclusive-scope > numeric-difference > antonym > indirect
NEG_RE = re.compile(
    r"\b(not|n't|never|no|none|nobody|nothing|nor|neither|zero|without|"
    r"cannot|can not|lack|lacks|lacking|lacked|incapable|inability|"
    r"unrelated|unmarried|fails?|failed|refuses?|denies|disprove[ds]?)\b",
    re.I)
EXCL_RE = re.compile(r"\b(only|sole|solely|exclusively|merely)\b", re.I)
SPELLED = set("""one two three four five six seven eight nine ten eleven twelve
thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty
forty fifty sixty seventy eighty ninety hundred thousand million billion
first second third fourth fifth sixth seventh eighth ninth tenth""".split())
NUM_RE = re.compile(r"\d[\d,]*(?:\.\d+)?")


def num_tokens(text: str) -> set:
    toks = {t.replace(",", "") for t in NUM_RE.findall(text)}
    toks |= {w.lower() for w in re.findall(r"[A-Za-z]+", text)
             if w.lower() in SPELLED}
    return toks


# modest lexical-antonym pairs: token found in one claim and its partner in
# the other claim (case-insensitive word match)
ANTONYM_PAIRS = [
    ("increase", "decrease"), ("increases", "decreases"), ("increase", "reduce"),
    ("increased", "decreased"), ("increase", "decline"), ("rise", "fall"),
    ("higher", "lower"), ("high", "low"), ("grows", "shrinks"),
    ("promote", "inhibit"), ("promotes", "inhibits"), ("promote", "suppress"),
    ("enhance", "diminish"), ("enhances", "reduces"), ("improve", "worsen"),
    ("improves", "reduces"), ("support", "contradict"), ("supports", "contradicts"),
    ("stimulate", "block"), ("activation", "inhibition"), ("induce", "suppress"),
    ("induces", "suppresses"), ("dependent", "independent"),
    ("susceptible", "immune"), ("enhancer", "suppressor"), ("inhibits", "encourages"),
    ("reduce", "increase"), ("reduces", "increases"), ("reduce", "increase"),
    ("beneficial", "harmful"), ("effective", "ineffective"), ("related", "unrelated"),
    ("causes", "prevents"), ("cause", "prevent"), ("faster", "slower"),
    ("slowed", "accelerated"), ("loss", "gain"), ("alive", "dead"),
]


def has_antonym(c1: str, c2: str) -> bool:
    w1 = set(re.findall(r"[a-z]+", c1.lower()))
    w2 = set(re.findall(r"[a-z]+", c2.lower()))
    for a, b in ANTONYM_PAIRS:
        if (a in w1 and b in w2) or (b in w1 and a in w2):
            return True
    return False


def auto_type(inc_claims: list, dec_claims: list) -> str:
    """Descriptive 5-way label for a group, precedence-documented."""
    all_txt_i = " ".join(inc_claims)
    all_txt_d = " ".join(dec_claims)
    if NEG_RE.search(all_txt_i) or NEG_RE.search(all_txt_d):
        return "explicit_negation"
    if EXCL_RE.search(all_txt_i) or EXCL_RE.search(all_txt_d):
        return "exclusive_alternative"
    ni, nd = num_tokens(all_txt_i), num_tokens(all_txt_d)
    if (ni or nd) and ni != nd:
        return "numeric_value"
    if any(has_antonym(a, b) for a in inc_claims for b in dec_claims):
        return "antonym_opposite"
    return "indirect_contradiction"


# --- similarity (description only) ---------------------------------------
STOP = set("""a an the of in on at to for and or is are was were be been being
that this these those it its with as by from not no""".split())


def tokens(text: str) -> set:
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP}


def caps(text: str) -> set:
    # capitalized words not at sentence start (rough entity proxy)
    out = set()
    for m in re.finditer(r"\b([A-Z][a-zA-Z]+)\b", text):
        if m.start() == 0 or text[m.start() - 1] in ".!?\n":
            continue
        out.add(m.group(1).lower())
    return out


def jac(a: set, b: set) -> float:
    return 1.0 if not a and not b else (len(a & b) / len(a | b) if a | b else 0.0)


def quant(v: list) -> dict:
    v = sorted(v)
    q = lambda f: v[min(len(v) - 1, int(round(f * (len(v) - 1))))]
    return {"n": len(v), "min": v[0], "p10": q(.10), "p25": q(.25),
            "median": st.median(v), "p75": q(.75), "p90": q(.90), "max": v[-1],
            "mean": st.mean(v)}


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for row in rows:
        out.append("| " + " | ".join(str(c) for c in row) + " |")
    return out


def main() -> int:
    # --- integrity asserts -------------------------------------------------
    for p in (CANDIDATES, DISCOVERY):
        if "results/raw" in p or "results/g24" in p:
            raise SystemExit("REFUSAL: census must not read model output")
    cand_lines = sum(1 for _ in open(CANDIDATES, encoding="utf-8"))
    assert cand_lines == EXPECTED_CANDIDATES, cand_lines
    disc = [json.loads(l) for l in open(DISCOVERY, encoding="utf-8")]
    assert len(disc) == EXPECTED_DISCOVERY, len(disc)

    # discovery evidence groups -> 53 SHAs
    by_ev_d = defaultdict(list)
    for it in disc:
        by_ev_d[it["critical_evidence"]].append(it)
    disc53 = set()
    for ev, its in by_ev_d.items():
        if (any(i["critical_direction"] == "increase" for i in its)
                and any(i["critical_direction"] == "decrease" for i in its)):
            disc53.add(hashlib.sha256(ev.encode("utf-8")).hexdigest()[:10])
    assert len(disc53) == EXPECTED_DISC53, len(disc53)
    disc_ids = {it["item_id"] for it in disc}
    disc_evidence = set(by_ev_d)          # any of the 600 evidence texts

    # --- candidates: drop the 600, group by exact evidence ----------------
    by_ev = defaultdict(list)
    cand_src = Counter()
    n_in_disc = 0
    import ast
    for l in open(CANDIDATES, encoding="utf-8"):
        it = json.loads(l)
        m = it["meta"]
        if isinstance(m, str):
            try:
                m = ast.literal_eval(m)
            except (ValueError, SyntaxError):
                m = {}
        it["_meta"] = m
        cand_src[m.get("source", "?")] += 1
        if it["item_id"] in disc_ids:
            n_in_disc += 1
            continue
        by_ev[it["critical_evidence"]].append(it)
    assert n_in_disc == EXPECTED_DISCOVERY, n_in_disc

    both = {ev: its for ev, its in by_ev.items()
            if any(i["critical_direction"] == "increase" for i in its)
            and any(i["critical_direction"] == "decrease" for i in its)}
    excl53 = {ev: its for ev, its in both.items()
              if hashlib.sha256(ev.encode("utf-8")).hexdigest()[:10] in disc53}
    fresh = {ev: its for ev, its in both.items() if ev not in excl53}

    # --- per-group records -------------------------------------------------
    records = []
    for ev, its in fresh.items():
        sha = hashlib.sha256(ev.encode("utf-8")).hexdigest()[:10]
        inc = sorted((i for i in its if i["critical_direction"] == "increase"),
                     key=lambda x: x["item_id"])
        dec = sorted((i for i in its if i["critical_direction"] == "decrease"),
                     key=lambda x: x["item_id"])
        ic = [i["base_context"] for i in inc]
        dc = [i["base_context"] for i in dec]
        jacs, ents = [], []
        for a in ic:
            for b in dc:
                jacs.append(jac(tokens(a), tokens(b)))
                ents.append(jac(caps(a), caps(b)))
        records.append({
            "group_sha": sha,
            "source": its[0]["_meta"].get("source", "?"),
            "n_inc": len(inc), "n_dec": len(dec), "n_items": len(its),
            "auto_type": auto_type(ic, dc),
            "negation_present": "yes"
            if (NEG_RE.search(" ".join(ic)) or NEG_RE.search(" ".join(dc)))
            else "no",
            "jaccard_mean": round(st.mean(jacs), 4),
            "entity_overlap_mean": round(st.mean(ents), 4),
            "evidence_seen_in_discovery600": ev in disc_evidence,
            "inc_item_ids": ",".join(i["item_id"] for i in inc),
            "dec_item_ids": ",".join(i["item_id"] for i in dec),
            "evidence": ev,
        })
    records.sort(key=lambda r: (r["group_sha"]))
    assert len(records) == len(fresh)

    n_groups = len(records)
    n_items = sum(r["n_items"] for r in records)
    src_groups = Counter(r["source"] for r in records)
    src_items = Counter()
    for r in records:
        src_items[r["source"]] += r["n_items"]
    topo = Counter((r["n_inc"], r["n_dec"]) for r in records)
    seen600 = sum(1 for r in records if r["evidence_seen_in_discovery600"])
    types = Counter(r["auto_type"] for r in records)
    negs = Counter(r["negation_present"] for r in records)
    jac_all = [r["jaccard_mean"] for r in records]
    ent_all = [r["entity_overlap_mean"] for r in records]

    # topology for md: cells with >=4 groups individually, tail aggregated
    # (full table lives in json `topology_full`)
    topo_cells = sorted(topo.items(), key=lambda kv: (-kv[1], kv[0]))
    topo_items = Counter()
    for r in records:
        topo_items[(r["n_inc"], r["n_dec"])] += r["n_items"]
    tail = [(k, c) for k, c in topo_cells if c < 4]
    topo_rows = []
    for (ni, nd), c in topo_cells:
        if c >= 4:
            topo_rows.append([f"({ni},{nd})", c, topo_items[(ni, nd)]])
    if tail:
        topo_rows.append([f"long tail ({len(tail)} cells, <=3 groups each)",
                          sum(c for _, c in tail),
                          sum(topo_items[k] for k, _ in tail)])

    report = {
        "layer": "Layer-2 feasibility census (observations only; no gates)",
        "inputs": {"candidates": CANDIDATES, "candidates_lines": cand_lines,
                   "discovery_items": len(disc),
                   "candidate_source_split": dict(cand_src)},
        "freshness_rules": [
            "drop the 600 discovery item_ids from the candidate pool",
            "byte-exact critical_evidence equality defines a group; group must "
            "contain >=1 increase and >=1 decrease claim",
            "drop groups whose evidence SHA256[:10] is among the 53 discovery "
            "opposite-direction evidence groups",
        ],
        "excluded_600_items": n_in_disc,
        "both_direction_groups_before_53_exclusion": len(both),
        "groups_removed_by_53_sha": len(excl53),
        "fresh_groups": n_groups,
        "fresh_items": n_items,
        "groups_by_source": dict(src_groups),
        "items_by_source": dict(src_items),
        "topology_full": {f"{k[0]},{k[1]}": v for k, v in sorted(topo.items())},
        "freshness_note": {
            "groups_whose_evidence_appears_in_discovery600_but_not_among_53":
                seen600,
            "groups_with_evidence_never_seen_in_discovery": n_groups - seen600,
        },
        "auto_taxonomy": {
            "status": "deterministic rules, blind sample audit PENDING",
            "precedence": "explicit_negation > exclusive_alternative > "
                          "numeric_value (token-set differs) > antonym_opposite "
                          "> indirect_contradiction",
            "counts": dict(types),
            "negation_present": dict(negs),
        },
        "similarity_description_only": {
            "claim_pair_token_jaccard": quant(jac_all),
            "claim_pair_entity_overlap": quant(ent_all),
        },
        "no_model_output_read": True,
    }

    # --- optional blind audit (from scripts/validate_g24a_census_taxonomy_audit.py)
    audit_p = Path(OUT_PREFIX + "_taxaudit_summary.json")
    audit = json.loads(audit_p.read_text(encoding="utf-8")) \
        if audit_p.exists() else None
    report["auto_taxonomy"]["blind_audit"] = audit or {"status": "pending"}
    report["auto_taxonomy"]["status"] = (
        "deterministic rules (rough per-group tags); landscape proportions "
        "audited blind (see blind_audit)" if audit else
        "deterministic rules, blind sample audit PENDING")
    SHORT = {"explicit_negation": "neg", "antonym_opposite": "anti",
             "exclusive_alternative": "excl", "numeric_value": "num",
             "indirect_contradiction": "ind"}
    TORDER = ["explicit_negation", "antonym_opposite",
              "exclusive_alternative", "numeric_value", "indirect_contradiction"]
    if audit:
        agr = audit["agreement"]
        dist = audit["distributions"]
        fx = agr["five_way_exact"]
        conf = agr["confusion_auto_rows_blind_cols"]
        ex_total = sum(conf["exclusive_alternative"].values())
        ex_ok = conf["exclusive_alternative"].get("exclusive_alternative", 0)
        anti_auto_pct = 100 * types.get("antonym_opposite", 0) / n_groups
        anti_blind_pct = dist["blind_population_weighted_pct"]["antonym_opposite"]
        audit_block = [
            "### 3b. Blind sample audit (seed 20260925; 100 fever + 20 "
            "scifact; 3 blind coders, zero access to auto labels)",
            "",
            *md_table(["metric", "value"], [
                ["5-way exact agreement (auto vs blind)",
                 f"{fx['overall']}/{fx['n']} = {fx['pct']}%"],
                ["— fever",
                 f"{fx['fever']['exact']}/{fx['fever']['n']} = {fx['fever']['pct']}%"],
                ["— scifact",
                 f"{fx['scifact']['exact']}/{fx['scifact']['n']} = {fx['scifact']['pct']}%"],
                ["negation-flag agreement",
                 f"{agr['negation_flag']['exact']}/{agr['negation_flag']['n']}"
                 f" = {agr['negation_flag']['pct']}%"],
                ["validity (validator exit 0)",
                 "manifest 120; batches 40/40/40; coded 120; sha sets match; "
                 "label domains ok"],
            ]),
            "",
            "Confusion matrix (rows = auto rules, cols = blind coders):",
            "",
            *md_table(["auto \\ blind"] + [SHORT[t] for t in TORDER],
                      [[SHORT[a]] + [conf.get(a, {}).get(t, 0)
                                     for t in TORDER] for a in TORDER]),
            "",
            "Proportions (population = all 1,582 fresh groups):",
            "",
            *md_table(["type", "auto % of groups", "auto in sample",
                       "blind in sample", "blind weighted % (audited)"],
                      [[t, f"{100 * types.get(t, 0) / n_groups:.1f}%",
                        f"{dist['auto_on_sample'].get(t, 0)}/120",
                        f"{dist['blind_on_sample'].get(t, 0)}/120",
                        f"{dist['blind_population_weighted_pct'][t]}%"]
                       for t in TORDER]),
            "",
            f"negation_present (blind): sample {dist['negation_flag']['blind']}"
            f" -> weighted {dist['negation_flag']['blind_population_weighted_pct']}"
            " (discovery's 53 pairs were 19/53 = 35.8% yes; different "
            "population, description only)",
            "",
            f"Reading (descriptions, no gates): auto antonym badly "
            f"under-detects paraphrase antonyms ({anti_auto_pct:.1f}% of "
            f"groups vs audited {anti_blind_pct}% — the lexical-pair rules "
            f"are a LOWER BOUND); auto exclusive over-calls incidental "
            f"'only' (blind confirmed {ex_ok}/{ex_total}); the negation flag "
            f"is the most reliable tag ({agr['negation_flag']['pct']}% "
            f"agreement). Per-group auto tags in groups.csv remain rough "
            f"navigation tags — use the audited weighted proportions for "
            f"any landscape statement. Borderline coder rationales are "
            f"preserved verbatim in the batch jsonl `note` fields; no "
            f"reconciliation pass was run (a second coder round was not "
            f"authorized).",
            "",
        ]
    else:
        audit_block = [
            "STATUS: automatic labels are a landscape description, NOT "
            "verified judgments. A blind sample audit (coders never see "
            "the auto labels) is the next step before any sampling "
            "decision.",
            "",
        ]

    # --- csv ---------------------------------------------------------------
    cols = ["group_sha", "source", "n_inc", "n_dec", "n_items", "auto_type",
            "negation_present", "jaccard_mean", "entity_overlap_mean",
            "evidence_seen_in_discovery600", "inc_item_ids", "dec_item_ids",
            "evidence"]
    with open(OUT_PREFIX + "_groups.csv", "w", newline="",
              encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in records:
            w.writerow([r[c] for c in cols])

    # --- md ----------------------------------------------------------------
    L = ["# G24A fresh exact-evidence-pair census v1",
         "",
         "**Layer-2 feasibility census. Observations only — no kill gates, "
         "no model output read, nothing filtered except the explicit "
         "freshness rules below.**",
         "",
         "Purpose (user, 2026-09-25): determine how many byte-exact "
         "same-evidence, opposite-direction claim groups exist in the frozen "
         "candidate pool OUTSIDE the 600-item discovery set, to judge "
         "whether a held-out confirmation on purely natural data is "
         "possible.",
         "",
         "## 0. Inputs and integrity",
         "",
         *md_table(["check", "value"], [
             ["candidates pool lines", f"{cand_lines} (== 13,283 expected)"],
             ["discovery items", len(disc)],
             ["discovery ids found in pool", f"{n_in_disc}/600"],
             ["discovery opposite-direction evidence SHAs",
              f"{len(disc53)} (== 53 expected)"],
             ["candidate source split", json.dumps(dict(cand_src))],
         ]),
         "",
         "Freshness rules: (1) drop the 600 discovery item_ids; (2) group by "
         "byte-exact `critical_evidence`, require both directions present; "
         "(3) drop groups whose evidence SHA256[:10] is one of the 53 "
         "discovery pair evidences. No model output path is ever opened "
         "(asserted in code).",
         "",
         "## 1. Fresh landscape",
         "",
         *md_table(["quantity", "value"], [
             ["both-direction groups before 53-SHA exclusion", len(both)],
             ["removed by 53-SHA exclusion", len(excl53)],
             ["**fresh groups**", f"**{n_groups}**"],
             ["**fresh items**", f"**{n_items}**"],
             ["fresh groups FEVER / SciFact",
              f"{src_groups.get('fever', 0)} / {src_groups.get('scifact', 0)}"],
             ["fresh items FEVER / SciFact",
              f"{src_items.get('fever', 0)} / {src_items.get('scifact', 0)}"],
         ]),
         "",
         "Topology (n_inc, n_dec): cells with >=4 groups listed "
         "individually, remaining cells aggregated as a long tail; full "
         "table in the JSON (`topology_full`):",
         "",
         *md_table(["topology", "groups", "items"], topo_rows),
         "",
         "## 2. Freshness audit (descriptive, nothing excluded)",
         "",
         f"- {seen600} fresh groups have evidence text that also appears in "
         f"the 600-item discovery set (but NEVER as an "
         f"opposite-direction pair there — those are the 53)",
         f"- {n_groups - seen600} fresh groups have evidence never seen in "
         f"discovery at all (strictly unseen subset)",
         "",
         "Both numbers are reported for the user to choose from when "
         "designing a held-out confirmation; the census itself excludes "
         "only the 53, per instruction.",
         "",
         "## 3. Automatic contradiction taxonomy (deterministic tags + "
         "blind audit)",
         "",
         "Deterministic rules with precedence: explicit_negation > "
         "exclusive_alternative > numeric_value (number-token sets differ "
         "between claim sides) > antonym_opposite (lexical pair across "
         "sides) > indirect_contradiction (default).",
         "",
         *md_table(["auto type", "groups", "% of fresh"],
                   [[t, c, f"{100 * c / n_groups:.1f}%"]
                    for t, c in types.most_common()]),
         "",
         f"negation_present: {json.dumps(dict(negs))}",
         "",
         *audit_block,
         "## 4. Claim similarity and entity overlap (description only)",
         "",
         "Per group: mean over all inc x dec claim pairs of (a) token "
         "Jaccard (stopwords removed) and (b) capitalized-word Jaccard "
         "(rough entity proxy). NEVER used as a filter here.",
         "",
         *md_table(["quantity", "n", "p10", "p25", "median", "p75", "p90"],
                   [[k, v["n"], f"{v['p10']:.3f}", f"{v['p25']:.3f}",
                     f"{v['median']:.3f}", f"{v['p75']:.3f}",
                     f"{v['p90']:.3f}"]
                    for k, v in [
                        ("claim token Jaccard",
                         report["similarity_description_only"]["claim_pair_token_jaccard"]),
                        ("entity overlap",
                         report["similarity_description_only"]["claim_pair_entity_overlap"])]]),
         "",
         "## 5. Governance",
         "",
         "- no model outputs read; no RQ kill criteria attached; this census "
         "only maps the natural-data landscape (user ruling 2026-09-25: "
         "'这里不设 <N 就 kill RQ')",
         "- inputs frozen: candidates file = selection-pass input (unchanged "
         "since the 13,283-pool freeze); discovery item file at 92d8cd0",
         "- outputs feed the Layer-2 held-out confirmation design decision; "
         "no experiment is authorized by this document",
         "",
         ]
    json.dump(report, open(OUT_PREFIX + ".json", "w"),
              indent=1, ensure_ascii=False)
    open(OUT_PREFIX + ".md", "w", encoding="utf-8").write(
        "\n".join(L) + "\n")

    print(f"candidates={cand_lines} | removed600={n_in_disc} | "
          f"both-dir groups={len(both)} | -53sha={len(excl53)}")
    print(f"FRESH groups={n_groups} items={n_items} "
          f"src={dict(src_groups)}")
    print(f"freshness: seen600={seen600} strictly_unseen={n_groups - seen600}")
    print(f"auto types: {dict(types)}")
    print(f"jaccard median={report['similarity_description_only']['claim_pair_token_jaccard']['median']:.3f} "
          f"entity median={report['similarity_description_only']['claim_pair_entity_overlap']['median']:.3f}")
    print(f"wrote {OUT_PREFIX}.md / .json / _groups.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
