#!/usr/bin/env python3
"""HoVer zero-model structural audit (G26A go/no-go gate, prereg-draft §2).

Runs entirely WITHOUT model calls. Deterministic (no RNG).

Claims-level checks (always run):
  C1 counts per split (num_hops, label)
  C2 construction funnel: 2-hop -> n_sf==2 -> distinct titles
  C3 cluster structure (title-pair, hpqa_id; per split + pooled)
  C4 label set / gold-sign mapping stability
  C5 cross-split integrity (uid, hpqa_id, claim overlaps); test split blindness
  C6 preliminary comparison/parallel pattern rate on claims (regex, rough)

Text-level checks (run iff the official wiki_wo_links.db exists):
  T1 page coverage: do all funnel titles resolve in the DB (exact match)
  T2 sentence materialization: sf index valid; word-token stats for A and B
  T3 bridge orientation: does sf[0]'s sentence mention sf[1]'s entity and/or
     vice versa (rates, by label) -> validates sf list order as chain order
  T4 topology classification: bridge (mention in >=1 direction) vs parallel
  T5 lexical-leak: max single-sentence content-word recall of the claim
     (thresholds reported; one evidence sentence alone nearly containing the
     claim's content words = leak suspect)
  T6 post-rule structural funnel with the primary rule set:
       2-hop & n_sf==2 & distinct titles & orientation-unique bridge &
       8 <= words(sent) <= 80 (both) & single-sentence leak recall < 0.9
     -> survivors by split/label + cluster counts
  T7 evidence reuse: unique (title, sent_idx) pairs vs items

Output: results/audits/hover_structural_v1.json (overwritten, deterministic).
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sqlite3
import statistics
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "external", "raw", "hover")
SPLITS = {
    "train": "hover_train_release_v1.1.json",
    "dev": "hover_dev_release_v1.1.json",
    "test": "hover_test_release_v1.1.json",
}
DEFAULT_DB = os.path.join(RAW, "wiki_wo_links.db")
DEFAULT_OUT = os.path.join(ROOT, "results", "audits", "hover_structural_v1.json")
# Content-Length of https://nlp.cs.unc.edu/data/hover/wiki_wo_links.db
# (HEAD probe 2026-09-24, ETag "80862000-5b32925b72435") — a partial
# download is a malformed SQLite file, so size must match exactly.
EXPECTED_DB_BYTES = 2156273664

LABELS = {"SUPPORTED": 1, "NOT_SUPPORTED": -1}  # gold sign map (C4)

COMPARISON_RE = re.compile(
    r"\bare both\b|\bin common\b|\beach of (them|these|the)\b|\brespectively\b"
    r"|\btwo \w+ (things|facts)\b|\bhave in common\b|\bsimilarities\b"
    r"|\b(both|two) .{0,60} and\b",
    re.I,
)

STOP = set(
    """a an the and or but if then else when while of in on at to for from by
    with without as is are was were be been being it its this that these those
    he she they them his her their we you i not no nor so than too very can
    will just do does did doing have has had having about into over under
    again further once here there all any both each few more most other some
    such only own same s t don now up down out off above below between during
    before after while who whom which what where how why has have""".split()
)
WORD_RE = re.compile(r"\b[\w'-]+\b")


def words(text: str) -> list[str]:
    return [w.lower() for w in WORD_RE.findall(text)]


def content_words(text: str) -> list[str]:
    return [w for w in words(text) if w not in STOP and len(w) > 1]


def entity_variants(title: str) -> list[str]:
    """Entity mention variants of a page title: full, paren-stripped."""
    out = [title]
    stripped = re.sub(r"\s*\([^)]*\)", "", title).strip()
    if stripped and stripped != title:
        out.append(stripped)
    return [v for v in out if v]


# --- sentence reconstruction (T2) -------------------------------------------
# The official DB stores UNSPLITTED prose; gold supporting_facts indices were
# annotated against a CoreNLP-style split (HoVer README: "We use Corenlp to
# split the sentences"). We reconstruct with a deterministic regex splitter
# that refuses to break after single-letter name initials ("Robert W. Derminer"
# / "William S. Hart") and common abbreviations — validated empirically in
# T8_alignment_controls (gold vs rotated-index recall/bridge, and v1-naive
# vs v2-abbrev-aware). It is an APPROXIMATION of the official segmentation:
# pages whose stored text is shorter than at annotation time still go out of
# bounds (T2 idx_invalid) and are excluded by rule.
ABBREV = {w.lower() for w in
          "mr mrs ms dr prof st vs etc jr sr inc ltd co fig no vol dept est "
          "approx cf a.m p.m u.s u.k e.g i.e".split()}


def smart_sents(text: str) -> list[str]:
    """Abbreviation-aware deterministic sentence split of page prose."""
    text = text.strip()
    if not text:
        return []
    out: list[str] = []
    start = 0
    for m in re.finditer(r'[.!?]+["\'）)\]]?(?=\s)', text):
        run = re.search(r"([A-Za-z.]+)$", text[:m.start()])
        tok = run.group(1) if run else ""
        nxt = m.end()
        while nxt < len(text) and text[nxt].isspace():
            nxt += 1
        if nxt >= len(text):
            continue
        if not (text[nxt].isupper() or text[nxt] in '"“(“'):
            continue
        if re.search(r"\b[A-Z]$", tok):        # middle initial / "U.S."
            continue
        if tok.lower().rstrip(".") in ABBREV:  # "Vol." / "e.g." ...
            continue
        out.append(text[start:m.end()])
        start = m.end()
    out.append(text[start:])
    return [s for s in out if s]


def naive_sents(text: str) -> list[str]:
    """v1 baseline (no abbreviation guard); only used by T8 for comparison."""
    return [p for p in re.split(r'(?<=[.!?])\s+(?=[A-Z"“(])', text.strip())
            if p]


def mentions(sentence: str, title: str) -> bool:
    s = sentence.casefold()
    return any(v.casefold() in s for v in entity_variants(title))


def load_claims() -> dict:
    data = {}
    for split, fname in SPLITS.items():
        with open(os.path.join(RAW, fname), encoding="utf-8") as f:
            data[split] = json.load(f)
    return data


def claims_level(data: dict) -> dict:
    out: dict = {"checklist": "claims-level (C1-C6)"}

    # C1 counts
    c1 = {}
    for split, rows in data.items():
        c1[split] = {
            "n": len(rows),
            "num_hops": dict(sorted(
                collections.Counter(str(r.get("num_hops")) for r in rows).items())),
            "label": dict(sorted(
                collections.Counter(str(r.get("label")) for r in rows).items())),
        }
    out["C1_counts"] = c1

    # C2 funnel
    c2 = {}
    funnel = []
    for split, rows in data.items():
        h2 = [r for r in rows if r.get("num_hops") == 2]
        nsf = [r for r in h2 if len(r.get("supporting_facts", [])) == 2]
        dist = [r for r in nsf
                if r["supporting_facts"][0][0] != r["supporting_facts"][1][0]]
        c2[split] = {
            "hop2": len(h2), "hop2_nsf2": len(nsf), "distinct_titles": len(dist),
            "by_label": dict(collections.Counter(r["label"] for r in dist)),
        }
        if split != "test":  # test is blind (no gold) -> excluded everywhere
            funnel.extend((split, r) for r in dist)
    out["C2_funnel"] = c2

    # C3 clusters
    def pairs_of(rows):
        return collections.Counter(
            tuple(sorted((r["supporting_facts"][0][0],
                          r["supporting_facts"][1][0]))) for _, r in rows)

    c3 = {}
    for split in ("train", "dev"):
        rows = [x for x in funnel if x[0] == split]
        pairs = pairs_of(rows)
        hp = collections.Counter(r["hpqa_id"] for _, r in rows)
        c3[split] = {
            "items": len(rows), "title_pair_clusters": len(pairs),
            "singleton_pairs": sum(1 for v in pairs.values() if v == 1),
            "max_pair_freq": max(pairs.values()) if pairs else 0,
            "hpqa_clusters": len(hp),
            "hpqa_size_ge2": sum(1 for v in hp.values() if v >= 2),
        }
    pairs_all = pairs_of(funnel)
    c3["pooled"] = {
        "items": len(funnel), "title_pair_clusters": len(pairs_all),
        "singleton_pairs": sum(1 for v in pairs_all.values() if v == 1),
        "max_pair_freq": max(pairs_all.values()),
    }
    out["C3_clusters"] = c3

    # C4 label / sign mapping
    labels_seen = sorted({r["label"] for _, r in funnel})
    out["C4_labels"] = {
        "labels_seen": labels_seen,
        "sign_map": {k: v for k, v in LABELS.items() if k in labels_seen},
        "mapping_stable": set(labels_seen) <= set(LABELS),
        "unmapped": [l for l in labels_seen if l not in LABELS],
    }

    # C5 integrity
    tr, dv, te = data["train"], data["dev"], data["test"]
    c5 = {
        "uid_train_uniq": len({r["uid"] for r in tr}) == len(tr),
        "uid_dev_uniq": len({r["uid"] for r in dv}) == len(dv),
        "uid_cross_overlap": len({r["uid"] for r in tr} & {r["uid"] for r in dv}),
        "hpqa_cross_overlap": len({r["hpqa_id"] for r in tr}
                                  & {r["hpqa_id"] for r in dv}),
        "claim_cross_overlap": len({r["claim"] for r in tr}
                                   & {r["claim"] for r in dv}),
        "test_blind": all(
            r.get("label") is None and not r.get("supporting_facts")
            for r in te),
        "funnel_claim_dups": sum(
            v - 1 for v in collections.Counter(
                r["claim"] for _, r in funnel).values() if v > 1),
    }
    out["C5_integrity"] = c5

    # C6 rough comparison/parallel pattern on funnel claims
    n_comp = sum(1 for _, r in funnel if COMPARISON_RE.search(r["claim"]))
    out["C6_comparison_regex"] = {
        "matched": n_comp, "of": len(funnel),
        "rate": round(n_comp / len(funnel), 4) if funnel else None,
        "note": "rough claim-text proxy only; final topology = T4 (text-level)",
    }

    out["_funnel"] = funnel  # carried for text-level; stripped from output
    return out


# ---------------------------------------------------------------- text level

def open_db(path: str):
    uri = f"file:{path}?mode=ro"
    conn = sqlite3.connect(uri, uri=True)
    tables = [r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'")]
    return conn, tables


def find_page_store(conn, tables):
    """Locate (table, id_col, text_col) holding page title -> prose."""
    for t in tables:
        cols = [r[1] for r in conn.execute(f'PRAGMA table_info("{t}")')]
        lower = {c.lower(): c for c in cols}
        id_col = next((lower[k] for k in ("title", "id", "page", "name")
                       if k in lower), None)
        text_col = next((lower[k] for k in ("text", "sentences", "content",
                                            "body", "sents") if k in lower),
                        None)
        if id_col and text_col and id_col != text_col:
            return t, id_col, text_col
    return None


def text_level(funnel, db_path: str) -> dict:
    out: dict = {"checklist": "text-level (T1-T7)", "db": db_path}
    conn, tables = open_db(db_path)
    store = find_page_store(conn, tables)
    if store is None:
        out["fatal"] = {"error": "no page store located",
                        "tables": tables}
        return out
    t, id_col, text_col = store
    out["schema"] = {"table": t, "id_col": id_col, "text_col": text_col,
                     "tables": tables}

    # cache: title -> raw prose | None.
    # DB ids are NFD-normalized while JSON titles are NFC — a naive exact
    # match reports ~249 false missings on this funnel (all diacritic names).
    raw_cache: dict[str, str | None] = {}
    tier_counts = {"raw": 0, "nfd": 0, "nfc": 0}

    def raw_text(title: str):
        if title not in raw_cache:
            found = None
            for name, key in (
                    ("raw", title),
                    ("nfd", unicodedata.normalize("NFD", title)),
                    ("nfc", unicodedata.normalize("NFC", title))):
                row = conn.execute(
                    f'SELECT "{text_col}" FROM "{t}" WHERE "{id_col}" = ?',
                    (key,)).fetchone()
                if row:
                    found = row[0]
                    tier_counts[name] += 1
                    break
            raw_cache[title] = found
        return raw_cache[title]

    def page(title: str):
        txt = raw_text(title)
        if txt is None:
            return None
        if isinstance(txt, (bytes, bytearray)):
            txt = txt.decode("utf-8")
        if not isinstance(txt, str):
            return None
        return smart_sents(txt)

    # T1 coverage: row existence by normalization tier.
    titles = {tt for _, r in funnel for tt, _ in r["supporting_facts"]}
    for ti in titles:
        raw_text(ti)  # populate tiers
    missing = [ti for ti in titles if raw_cache[ti] is None]
    out["T1_coverage"] = {
        "unique_titles": len(titles),
        "found": len(titles) - len(missing),
        "missing": len(missing),
        "lookup_tiers_first_hit": dict(tier_counts),
        "missing_sample": sorted(missing)[:10],
        "note": "raw-miss resolved by NFD/NFC is a false missing (encoding), "
                "not a data gap",
    }

    items = []          # materialized funnel items
    idx_bad = 0         # T2 invalid indices
    tok_a, tok_b = [], []
    orient = collections.Counter()   # T3
    orient_by_label = collections.defaultdict(collections.Counter)
    leak_max = []       # T5
    leak_thresh = collections.Counter()
    reused = collections.Counter()   # T7
    ctrl = collections.defaultdict(list)  # T8: (rec_g, brg_g, rec_rot, brg_rot)

    for split, r in funnel:
        (t0, i0), (t1, i1) = r["supporting_facts"]
        p0, p1 = page(t0), page(t1)
        if p0 is None or p1 is None:
            continue  # counted in T1; cannot materialize
        if not (0 <= i0 < len(p0)) or not (0 <= i1 < len(p1)):
            idx_bad += 1
            continue
        s0, s1 = p0[i0], p1[i1]
        w0, w1 = words(s0), words(s1)
        tok_a.append(len(w0))
        tok_b.append(len(w1))
        reused[(t0, i0)] += 1
        reused[(t1, i1)] += 1

        m01 = mentions(s0, t1)   # sentence0 mentions entity of page1
        m10 = mentions(s1, t0)   # sentence1 mentions entity of page0
        if m01 and m10:
            key = "both"
        elif m01:
            key = "sf0_to_sf1"
        elif m10:
            key = "sf1_to_sf0"
        else:
            key = "neither"
        orient[key] += 1
        orient_by_label[r["label"]][key] += 1

        cw = set(content_words(r["claim"]))
        rec0 = (len(cw & set(w0)) / len(cw)) if cw else 0.0
        rec1 = (len(cw & set(w1)) / len(cw)) if cw else 0.0
        mx = max(rec0, rec1)
        leak_max.append(mx)
        for th in (0.7, 0.8, 0.9, 1.0):
            if mx >= th:
                leak_thresh[f">={th}"] += 1

        # T8 rotated control: each page's neighbour index ((i+1) mod n,
        # falling back to i-1 for 1-sentence pages). If gold indices were
        # unaligned with our reconstruction, gold ~= rotated.
        # NOTE: p0/p1 are the SENTENCE LISTS; s0/s1 are the selected strings.
        j0, j1 = (i0 + 1) % len(p0), (i1 + 1) % len(p1)
        if j0 == i0:
            j0 = (i0 - 1) % len(p0)
        if j1 == i1:
            j1 = (i1 - 1) % len(p1)
        wj0, wj1 = words(p0[j0]), words(p1[j1])
        rec_rot = ((max(len(cw & set(wj0)), len(cw & set(wj1))) / len(cw))
                   if cw else 0.0)
        brg_rot = int(mentions(p0[j0], t1) or mentions(p1[j1], t0))
        ctrl[r["label"]].append(
            (mx, int(m01 or m10), rec_rot, brg_rot))

        items.append({
            "split": split, "uid": r["uid"], "label": r["label"],
            "hpqa_id": r["hpqa_id"], "titles": (t0, t1),
            "words": (len(w0), len(w1)), "orient": key,
            "leak": round(mx, 4),
            "bridge": key != "neither",
            "oriented": (m01 and not m10) or (m10 and not m01),
        })

    n = len(items)
    out["T2_sentences"] = {
        "idx_invalid": idx_bad, "materialized": n,
        "words_A": _stats(tok_a), "words_B": _stats(tok_b),
        "words_pooled": _stats(tok_a + tok_b),
        "primary_range_8_80_pass": sum(
            1 for x in items if 8 <= x["words"][0] <= 80
            and 8 <= x["words"][1] <= 80),
    }
    out["T3_orientation"] = {
        "rates": {k: v for k, v in sorted(orient.items())},
        "rate_frac": {k: round(v / n, 4) for k, v in sorted(orient.items())}
        if n else {},
        "by_label": {lab: dict(sorted(c.items()))
                     for lab, c in sorted(orient_by_label.items())},
    }
    n_bridge = sum(1 for x in items if x["bridge"])
    n_orient = sum(1 for x in items if x["oriented"])
    out["T4_topology"] = {
        "bridge": n_bridge, "parallel_or_unresolved": n - n_bridge,
        "orientation_unique": n_orient,
        "bridge_rate": round(n_bridge / n, 4) if n else None,
    }

    if leak_max:
        out["T5_leak"] = {
            "mean_max_single_sentence_recall": round(statistics.mean(leak_max), 4),
            "median": round(statistics.median(leak_max), 4),
            "max": round(max(leak_max), 4),
            "threshold_counts": {k: leak_thresh[k] for k in
                                 sorted(leak_thresh)},
            "primary_rule_recall_lt_0.9_pass":
                sum(1 for x in leak_max if x < 0.9),
        }

    # T6 post-rule funnel (primary rule set, prereg-draft §2)
    survivors = [x for x in items
                 if x["oriented"]
                 and 8 <= x["words"][0] <= 80
                 and 8 <= x["words"][1] <= 80
                 and x["leak"] < 0.9]
    sp = collections.Counter((x["split"], x["label"]) for x in survivors)
    pairs_s = collections.Counter(tuple(sorted(x["titles"])) for x in survivors)
    hp_s = collections.Counter(x["hpqa_id"] for x in survivors)
    out["T6_post_rule_funnel"] = {
        "rules": ["2-hop", "n_sf==2", "distinct titles",
                  "orientation-unique bridge", "8<=words<=80 both",
                  "single-sentence leak recall <0.9"],
        "materialized": n, "survivors": len(survivors),
        "by_split_label": {f"{s}/{l}": v for (s, l), v in sorted(sp.items())},
        "title_pair_clusters": len(pairs_s),
        "hpqa_clusters": len(hp_s),
        "singleton_pairs": sum(1 for v in pairs_s.values() if v == 1),
        "leak_ge_0.9_excluded": n - sum(1 for x in items if x["leak"] < 0.9),
    }

    # T7 reuse
    out["T7_reuse"] = {
        "unique_title_sent_pairs": len(reused),
        "distinct_used": sum(1 for _ in reused),
        "max_reuse": max(reused.values()) if reused else 0,
        "reused_ge5": sum(1 for v in reused.values() if v >= 5),
    }

    # T8 alignment controls (the evidence that gold indices are aligned with
    # our reconstruction): gold vs rotated, per label, under smart_sents;
    # plus the v1-naive splitter as baseline (oob + gold stats).
    t8: dict = {"method": "gold vs rotated-neighbour index, "
                          "reconstruction = smart_sents (v2)"}
    for lab, rows in sorted(ctrl.items()):
        if not rows:
            continue
        n_r = len(rows)
        t8[lab] = {
            "n": n_r,
            "recall_gold": round(statistics.mean(x[0] for x in rows), 4),
            "recall_rotated": round(statistics.mean(x[2] for x in rows), 4),
            "bridge_gold": round(statistics.mean(x[1] for x in rows), 4),
            "bridge_rotated": round(statistics.mean(x[3] for x in rows), 4),
        }
    v1 = {"oob": 0, "mat": 0, "S": [], "NS": []}
    for _split, r in funnel:
        (a0, k0), (a1, k1) = r["supporting_facts"]
        ta, tb = raw_text(a0), raw_text(a1)
        if ta is None or tb is None:
            continue
        s0, s1 = naive_sents(ta), naive_sents(tb)
        if k0 >= len(s0) or k1 >= len(s1):
            v1["oob"] += 1
            continue
        v1["mat"] += 1
        cc = set(content_words(r["claim"]))
        rec = (max(len(cc & set(words(s0[k0]))),
                   len(cc & set(words(s1[k1])))) / len(cc)) if cc else 0.0
        brg = int(mentions(s0[k0], a1) or mentions(s1[k1], a0))
        v1["S" if r["label"] == "SUPPORTED" else "NS"].append((rec, brg))
    t8["v1_naive_baseline"] = {
        "oob": v1["oob"], "mat": v1["mat"],
        "S_gold": {"recall": round(statistics.mean(x[0] for x in v1["S"]), 4)
                   if v1["S"] else None,
                   "bridge": round(statistics.mean(x[1] for x in v1["S"]), 4)
                   if v1["S"] else None},
        "NS_gold": {"recall": round(statistics.mean(x[0] for x in v1["NS"]), 4)
                    if v1["NS"] else None,
                    "bridge": round(statistics.mean(x[1] for x in v1["NS"]), 4)
                    if v1["NS"] else None},
        "note": "v2 must beat v1 on gold recall/bridge to be the "
                "reconstruction of record",
    }
    out["T8_alignment_controls"] = t8
    return out


def _stats(xs: list[int]) -> dict:
    if not xs:
        return {"n": 0}
    xs2 = sorted(xs)
    return {
        "n": len(xs2), "min": xs2[0], "p5": xs2[int(0.05 * (len(xs2) - 1))],
        "median": statistics.median(xs2),
        "p95": xs2[int(0.95 * (len(xs2) - 1))], "max": xs2[-1],
        "mean": round(statistics.mean(xs2), 2),
        "le8": sum(1 for x in xs2 if x < 8),
        "gt80": sum(1 for x in xs2 if x > 80),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    data = load_claims()
    res = claims_level(data)
    funnel = res.pop("_funnel")
    db_ok = (os.path.exists(args.db)
             and os.path.getsize(args.db) == EXPECTED_DB_BYTES)
    res["meta"] = {
        "audit": "hover_structural_v1", "zero_model": True,
        "sources": {s: {"file": f} for s, f in SPLITS.items()},
        "db_expected_bytes": EXPECTED_DB_BYTES,
        "db_present": os.path.exists(args.db),
        "db_complete": db_ok,
    }
    if db_ok:
        res["text"] = text_level(funnel, args.db)
    else:
        res["text"] = {
            "skipped": "db absent or incomplete (claims-level only)",
            "size": os.path.getsize(args.db) if os.path.exists(args.db) else None,
        }

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=1, ensure_ascii=False, sort_keys=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
