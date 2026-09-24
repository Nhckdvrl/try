"""Build the G26A Phase-A pool from the audited HoVer funnel (zero-model).

Frozen design: preregistrations/PREREGISTRATION_G26A_LOAD_BEARING.md (§2, §3).
Audit of record: results/audits/hover_structural_v1.json.

The builder REPRODUCES the audit step by step and ABORTS on any field
mismatch — it exists to prove the pool IS the audited funnel, then to attach
the frozen prompt furniture. Pipeline (train emitted; dev computed for
assertion only; test never read — O4/O9 split pin):

    candidates (2-hop, n_sf==2, distinct titles; frozen train file order)
    -> pages (raw/NFD/NFC tiers) + smart_sents materialization
    -> orientation-unique bridge  (m01 XOR m10; A/B by mention direction)
    -> 8..80 words both  ->  single-sentence leak recall < 0.9
    == 3,642 train survivors (audit by_split.train.survivors = O9)

Per train survivor:
  * A = chain-first sentence (names the OTHER page's entity), B = second;
    s = LABELS[label]; clusters = title-pair / hpqa_id (O8).
  * filler subsets fa/fb from conditions_g26a.FILLER_BANK: word targets are
    tuned so the rule->judgment distance (exactly run_model's
    ``rule_to_answer_tokens`` = tokens from the RULING header to the end of
    the compiled prompt) is equal across t0/t1/t2 within +-10 tokens under
    ALL four pooled-panel tokenizers (O7). Selection matches per-block
    token counts; the final gate measures the six compiled prompts.
  * The filler SENTENCE MULTISET fa u fb is one set per item — only its
    placement moves (prereg §3). Bank schedule {4..20} x 4 = 816 words.

Output: data/items/g26a_pool_v1.jsonl (frozen HoVer train order) +
data/items/g26a_pool_report_v1.{json,md}.

Usage:
    PYTHONPATH=src HF_HUB_OFFLINE=1 python src/build_g26a.py
    # overrides: --out --report --audit
"""
from __future__ import annotations

import argparse
import collections
import datetime
import hashlib
import json
import os
import random
import sys
import unicodedata
import zlib

sys.path.insert(0, os.path.dirname(__file__))

import audit_hover as ah          # noqa: E402  (funnel machinery of record)
import conditions_g26a as g26     # noqa: E402
from schema import Item, compile_prompt, rule_char_offset  # noqa: E402

AUDIT_DEFAULT = "results/audits/hover_structural_v1.json"
OUT_DEFAULT = "data/items/g26a_pool_v1.jsonl"
REPORT_DEFAULT = "data/items/g26a_pool_report_v1.json"
DB_REL = "data/external/raw/hover/wiki_wo_links.db"
PREREG = "preregistrations/PREREGISTRATION_G26A_LOAD_BEARING.md"

# Pooled panel (frozen layout — byte snapshots resolved from the same model
# ids scripts/run_g25a_main.sh uses; asserted single-snapshot below).
HUB = "/home/xiang/.cache/huggingface/hub"
PANEL_MODEL_IDS = {
    "llama31-8b": "NousResearch/Meta-Llama-3.1-8B-Instruct",
    "qwen3-8b": "Qwen/Qwen3-8B",
    "qwen35-9b": "Qwen/Qwen3.5-9B",
    "gemma3-12b": "google/gemma-3-12b-it",
}


def resolve_tokenizer_dir(model_id: str) -> str:
    import glob
    pat = os.path.join(HUB, "models--" + model_id.replace("/", "--"),
                       "snapshots", "*")
    hits = sorted(d for d in glob.glob(pat) if os.path.isdir(d))
    assert len(hits) == 1, f"{model_id}: expected 1 snapshot, got {hits}"
    return hits[0]

# Search window for filler word totals. NOT a +/-40 window around the
# evidence block's word count: entity-dense wiki evidence runs ~1.6-2.4
# tokens/word while the plain filler bank runs ~1.2, so a word-matched
# target can sit 20-40 tokens off and never reach token parity inside a
# narrow window (first build attempt: best achievable |gap| = 18 tokens).
# We therefore score EVERY packable target 4..W_MAX by token distance
# (word count survives only as a tie-break); W_MAX covers the worst
# plausible evidence block (82 words x ~3.6 tok/word vs filler x 1.1).
W_MAX = 300
TOPK = 5             # fallback (w_a, w_b) combos tried if verification fails
MAX_DIST_TOKENS = 10  # O7 / §9.2: equal across t0/t1/t2 within +-10

# O9 pin, asserted independently of the audit citation.
PIN_TRAIN_SURVIVORS = 3642


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ordered_targets(w0: int, span: int = W_MAX):
    # Token-targeted wide scan: every reachable word total, word-count
    # proximity to w0 only breaks equal-score ties (keeps fillers near the
    # evidence block's surface length for naturalness).
    yield from range(4, span + 1)


def pack(inventory: list[int], target: int) -> list[int] | None:
    """Indices of `inventory` summing exactly to `target` (bitset DP)."""
    reach = [1]
    for w in inventory:
        reach.append(reach[-1] | (reach[-1] << w))
    if not (reach[-1] >> target) & 1:
        return None
    out, t = [], target
    for i in range(len(inventory) - 1, -1, -1):
        w = inventory[i]
        if w <= t and (reach[i] >> (t - w)) & 1:
            out.append(i)
            t -= w
            if t == 0:
                break
    return list(reversed(out)) if t == 0 else None


def side_candidates(w0: int, score_fn):
    """score_fn(w) -> (score, payload) | None; sorted by (score, |w-w0|)."""
    scored = []
    for w in ordered_targets(w0):
        got = score_fn(w)
        if got is None:
            continue
        score, payload = got
        scored.append((score, abs(w - w0), w, payload))
    scored.sort(key=lambda x: (x[0], x[1]))
    return scored


def pack_with_shuffle(weights: list[int], target: int, k: int,
                      seed_key: int) -> list[list[int]]:
    """Up to k DIFFERENT exact-sum packings of `weights` to `target`.

    Reachability is permutation-invariant, but the backward reconstruction
    path is not — shuffling the iteration order yields distinct subsets at
    the same word total. Seeded stably (weights checksum + target + k) so
    the build is reproducible. Used only by the deep fallback: sentence
    identity, not just word count, moves the cross-tokenizer token vector
    (e.g. gemma-llama deltas range -4..0 per sentence), which the single
    deterministic packing never exploits."""
    base = list(range(len(weights)))
    seed = zlib.crc32(repr((tuple(weights), target, k, seed_key))
                      .encode()) & 0xFFFFFFFF
    rng = random.Random(seed)
    seen: set[tuple] = set()
    out: list[list[int]] = []
    for _ in range(k):
        order = base[:]
        rng.shuffle(order)
        reach = [1]
        for i in order:
            reach.append(reach[-1] | (reach[-1] << weights[i]))
        if not (reach[-1] >> target) & 1:
            continue
        t, chosen = target, []
        for pos in range(len(order) - 1, -1, -1):
            i = order[pos]
            w = weights[i]
            if w <= t and (reach[pos] >> (t - w)) & 1:
                chosen.append(i)
                t -= w
                if t == 0:
                    break
        if t == 0:
            key = tuple(sorted(chosen))
            if key not in seen:
                seen.add(key)
                out.append(sorted(chosen))
    return out


class Fill:
    """Filler-subset selection with global pack/token caches."""

    def __init__(self, tok_by_tag, bank, word_counts):
        self.tok = tok_by_tag
        self.bank = bank
        self.wc = word_counts
        self.pack_full: dict[int, list[int] | None] = {}
        self.pack_rem: dict[tuple[int, int], list[int] | None] = {}
        self.cache_fa: dict[tuple[int, str], int] = {}
        self.cache_fb: dict[tuple[int, int, str], int] = {}
        self.remainder: dict[int, list[int]] = {}
        # Per-sentence token vectors + header vector — SELECTION-only
        # approximation for the deep mix search (block tokenization differs
        # by boundary effects); the accept gate always measures the exact
        # compiled prompts via verify_distances.
        self.svec = {tag: [fn(s) for s in bank] for tag, fn in tok_by_tag.items()}
        self.hdr = {tag: fn(g26.FILLER_HEADER + "\n") for tag, fn in tok_by_tag.items()}

    def text(self, idxs) -> str:
        return g26.FILLER_HEADER + "\n" + "\n".join(self.bank[i] for i in idxs)

    def fa_idx(self, w: int):
        if w not in self.pack_full:
            self.pack_full[w] = pack(self.wc, w)
        return self.pack_full[w]

    def rem(self, w_a: int) -> list[int]:
        if w_a not in self.remainder:
            idxs = self.fa_idx(w_a)
            if idxs is None:
                self.remainder[w_a] = []
            else:
                drop = set(idxs)
                self.remainder[w_a] = [i for i in range(len(self.bank))
                                       if i not in drop]
        return self.remainder[w_a]

    def fb_idx(self, w_a: int, w_b: int):
        key = (w_a, w_b)
        if key not in self.pack_rem:
            rem = self.rem(w_a)
            # rem holds BANK INDICES; pack() needs the SENTENCE WORD COUNTS
            # of exactly those entries (packing the raw indices as if they
            # were word weights silently matched index-sums, not word-sums —
            # that was the first build's 72 furnish failures).
            got = pack([self.wc[i] for i in rem], w_b) if rem else None
            self.pack_rem[key] = [rem[j] for j in got] if got else None
        return self.pack_rem[key]

    def tok_fa(self, w: int, idxs) -> dict[str, int]:
        text = self.text(idxs)
        out = {}
        for tag, fn in self.tok.items():
            k = (w, tag)
            if k not in self.cache_fa:
                self.cache_fa[k] = fn(text)
            out[tag] = self.cache_fa[k]
        return out

    def tok_fb(self, w_a: int, w_b: int, idxs) -> dict[str, int]:
        text = self.text(idxs)
        out = {}
        for tag, fn in self.tok.items():
            k = (w_a, w_b, tag)
            if k not in self.cache_fb:
                self.cache_fb[k] = fn(text)
            out[tag] = self.cache_fb[k]
        return out


# ---------------------------------------------------------------- materialize

def raw_page_chain(conn, t, id_col, text_col, cache: dict, tiers: dict):
    """raw_text/page closures — copied from audit_hover.text_level (record of
    truth): DB ids are NFD-normalized while JSON titles are NFC; naive exact
    match false-misses every diacritic name."""
    def raw_text(title: str):
        if title not in cache:
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
                    tiers[name] += 1
                    break
            cache[title] = found
        return cache[title]

    def page(title: str):
        txt = raw_text(title)
        if txt is None:
            return None
        if isinstance(txt, (bytes, bytearray)):
            txt = txt.decode("utf-8")
        if not isinstance(txt, str):
            return None
        return ah.smart_sents(txt)

    return page


def funnel_rows(data: dict, split: str) -> list[dict]:
    rows = data[split]
    h2 = [r for r in rows if r.get("num_hops") == 2]
    nsf = [r for r in h2 if len(r.get("supporting_facts", [])) == 2]
    return [r for r in nsf
            if r["supporting_facts"][0][0] != r["supporting_facts"][1][0]]


def sweep(data: dict, page) -> tuple[dict, list[dict]]:
    """Run the audit funnel for train+dev; return stats + train records."""
    stats = {}
    train_recs: list[dict] = []
    pooled = collections.Counter()
    pooled_tp, pooled_hp = set(), set()
    surv_leak_pass = collections.Counter()   # leak<0.9 among materialized
    label_counts = collections.Counter()

    for split in ("train", "dev"):
        st = collections.Counter()
        tp, hp = set(), set()
        for r in funnel_rows(data, split):
            st["candidates"] += 1
            (t0, i0), (t1, i1) = r["supporting_facts"]
            p0, p1 = page(t0), page(t1)
            if p0 is None or p1 is None:
                st["missing_page"] += 1
                continue
            if not (0 <= i0 < len(p0)) or not (0 <= i1 < len(p1)):
                st["idx_oob"] += 1
                continue
            st["materialized"] += 1
            s0, s1 = p0[i0], p1[i1]
            w0, w1 = ah.words(s0), ah.words(s1)

            m01 = ah.mentions(s0, t1)
            m10 = ah.mentions(s1, t0)
            if m01 or m10:
                st["bridge"] += 1
            oriented = (m01 and not m10) or (m10 and not m01)
            if oriented:
                st["oriented"] += 1
                st["reversed_oriented" if m10 else "fwd_oriented"] += 1

            cw = set(ah.content_words(r["claim"]))
            rec0 = (len(cw & set(w0)) / len(cw)) if cw else 0.0
            rec1 = (len(cw & set(w1)) / len(cw)) if cw else 0.0
            mx = max(rec0, rec1)
            if mx < 0.9:
                surv_leak_pass[split] += 1

            wordpass = 8 <= len(w0) <= 80 and 8 <= len(w1) <= 80
            if wordpass:
                st["wordpass"] += 1
            keep = oriented and wordpass and mx < 0.9
            if not keep:
                continue
            st["survivors"] += 1
            pair = tuple(sorted((t0, t1)))
            tp.add(pair)
            hp.add(r["hpqa_id"])
            label_counts[f"{split}/{r['label']}"] += 1
            # keep implies oriented (XOR): m10 <=> list order reversed
            rev = bool(m10)
            st["reversed_survivors" if rev else "fwd_survivors"] += 1

            if split == "train":
                # A/B by mention direction (never list order, §2/§9.3):
                # m01 -> chain sf0->sf1: A = s0 (page t0), B = s1 (page t1)
                # m10 -> chain sf1->sf0: A = s1 (page t1), B = s0 (page t0)
                if m01:
                    a, b, pa, pb, orient = s0, s1, t0, t1, "sf0_to_sf1"
                else:
                    a, b, pa, pb, orient = s1, s0, t1, t0, "sf1_to_sf0"
                train_recs.append({
                    "uid": r["uid"], "claim": r["claim"],
                    "label": r["label"], "hpqa_id": r["hpqa_id"],
                    "title_pair": list(pair),
                    "page_a": pa, "page_b": pb,
                    "orient": orient, "reversed": rev,
                    "a": a, "b": b,
                    "words_a": len(ah.words(a)), "words_b": len(ah.words(b)),
                    "leak": round(mx, 4),
                })

        stats[split] = dict(st)
        stats[split]["title_pair_clusters"] = len(tp)
        stats[split]["hpqa_clusters"] = len(hp)
        pooled_tp |= tp
        pooled_hp |= hp

    # pooled mirrors of the audit's pooled fields
    for split in ("train", "dev"):
        pooled[f"cand_{split}"] = stats[split].get("candidates", 0)
    stats["_pooled"] = {
        "title_pair_clusters": len(pooled_tp),
        "hpqa_clusters": len(pooled_hp),
        "singleton_pairs": None,  # filled below from counter
        "label_counts": dict(label_counts),
        "leak_pass_train_dev": dict(surv_leak_pass),
    }
    # pooled survivors / materialized / etc.
    for key in ("candidates", "missing_page", "idx_oob", "materialized",
                "bridge", "oriented", "fwd_oriented", "reversed_oriented",
                "wordpass", "survivors", "fwd_survivors",
                "reversed_survivors"):
        stats["_pooled"][key] = (stats["train"].get(key, 0)
                                 + stats["dev"].get(key, 0))
    return stats, train_recs


def audit_assertions(stats: dict, audit: dict) -> list[dict]:
    t6 = audit["text"]["T6_post_rule_funnel"]
    t2 = audit["text"]["T2_sentences"]
    t4 = audit["text"]["T4_topology"]
    t5 = audit["text"]["T5_leak"]
    c2 = audit["C2_funnel"]
    pooled = stats["_pooled"]
    checks: list[dict] = []

    def chk(field, got, want):
        checks.append({"field": field, "builder": got, "audit": want,
                       "ok": got == want})

    chk("C2_funnel.train.distinct_titles",
        stats["train"].get("candidates"), c2["train"]["distinct_titles"])
    chk("C2_funnel.dev.distinct_titles",
        stats["dev"].get("candidates"), c2["dev"]["distinct_titles"])
    chk("T2.idx_invalid(pooled)", pooled["idx_oob"], t2["idx_invalid"])
    chk("T6.materialized(pooled)", pooled["materialized"], t6["materialized"])
    chk("T4.bridge(pooled)", pooled["bridge"], t4["bridge"])
    chk("T4.orientation_unique(pooled)", pooled["oriented"],
        t4["orientation_unique"])
    chk("T2.primary_range_8_80_pass(pooled)", pooled["wordpass"],
        t2["primary_range_8_80_pass"])
    chk("T5.primary_rule_recall_lt_0.9_pass(pooled)",
        pooled["leak_pass_train_dev"]["train"]
        + pooled["leak_pass_train_dev"]["dev"],
        t5["primary_rule_recall_lt_0.9_pass"])
    chk("T6.leak_ge_0.9_excluded(pooled)",
        pooled["materialized"]
        - (pooled["leak_pass_train_dev"]["train"]
           + pooled["leak_pass_train_dev"]["dev"]),
        t6["leak_ge_0.9_excluded"])
    chk("T6.survivors(pooled)", pooled["survivors"], t6["survivors"])
    for split in ("train", "dev"):
        chk(f"T6.by_split.{split}.survivors",
            stats[split].get("survivors"), t6["by_split"][split]["survivors"])
        chk(f"T6.by_split.{split}.title_pair_clusters",
            stats[split]["title_pair_clusters"],
            t6["by_split"][split]["title_pair_clusters"])
        chk(f"T6.by_split.{split}.hpqa_clusters",
            stats[split]["hpqa_clusters"],
            t6["by_split"][split]["hpqa_clusters"])
    for key, want in sorted(t6["by_split_label"].items()):
        chk(f"T6.by_split_label.{key}",
            pooled["label_counts"].get(key, 0), want)
    chk("T6.title_pair_clusters(pooled)",
        pooled["title_pair_clusters"], t6["title_pair_clusters"])
    chk("T6.hpqa_clusters(pooled)", pooled["hpqa_clusters"],
        t6["hpqa_clusters"])
    chk("PIN train survivors (O9)", stats["train"].get("survivors"),
        PIN_TRAIN_SURVIVORS)
    return checks


# ------------------------------------------------------------ filler + verify

def furnish(rec: dict, item: Item, fill: Fill, dist_out: dict) -> dict | None:
    """Choose fa/fb and verify prompt-level distances; return meta fragment."""
    ea = f"{g26.EVIDENCE_A_HEADER}\n{item.critical_evidence}"
    eb = f"{g26.EVIDENCE_B_HEADER}\n{rec['b']}"
    ea_tok = {tag: fn(ea) for tag, fn in fill.tok.items()}
    eb_tok = {tag: fn(eb) for tag, fn in fill.tok.items()}

    def score_a(w):
        idxs = fill.fa_idx(w)
        if idxs is None:
            return None
        got = fill.tok_fa(w, idxs)
        return max(abs(got[t] - ea_tok[t]) for t in fill.tok), w

    cands_a = side_candidates(len(g26.words(ea)), score_a)
    if not cands_a:
        return None

    for sa in cands_a[:TOPK]:
        _, _, w_a, _ = sa
        # Per-tokenizer a-side residuals (signed): the true constraint is
        # spread_x = max(|a_x|, |b_x|, |a_x + b_x|) <= 10 per tokenizer, so
        # b is ranked by that JOINT prediction — independent |b| ranking
        # misses sign cancellation and stacked same-sign residuals (the
        # first fixed run left one item at 11 = 6 + 5 on qwen3-8b).
        a_vec = {t: fill.cache_fa[(w_a, t)] - ea_tok[t] for t in fill.tok}

        def score_b(w, _wa=w_a, _av=a_vec):
            idxs = fill.fb_idx(_wa, w)
            if idxs is None:
                return None
            got = fill.tok_fb(_wa, w, idxs)
            pred = max(max(abs(_av[t]),
                           abs(got[t] - eb_tok[t]),
                           abs(_av[t] + got[t] - eb_tok[t]))
                       for t in fill.tok)
            return pred, w

        cands_b = side_candidates(len(g26.words(eb)), score_b)
        tried = 0
        for sb in cands_b[:TOPK + 5]:
            _, _, w_b, _ = sb
            fa = [fill.bank[i] for i in fill.fa_idx(w_a)]
            fb = [fill.bank[i] for i in fill.fb_idx(w_a, w_b)]
            meta_try = {"filler_a": fa, "filler_b": fb,
                        "filler_words_a": sum(len(g26.words(s)) for s in fa),
                        "filler_words_b": sum(len(g26.words(s)) for s in fb)}
            item.meta.update(meta_try)
            dists = verify_distances(item, fill.tok)
            tried += 1
            if max(dists.values()) <= MAX_DIST_TOKENS:
                dist_out.update(dists)
                return meta_try
        # else: next w_a candidate
    return None


# Deep fallback: K_MIX distinct exact-sum sentence mixings per word target
K_MIX = 12
W_A_KEEP = 6          # exact-tokenized a-side candidates passed downward
W_B_KEEP = 6          # exact-verified b-side candidates per a-candidate


def furnish_deep(rec: dict, item: Item, fill: Fill, dist_out: dict) -> dict | None:
    """Fast-path fallback: at each word target, search alternative SENTENCE
    MIXINGS (same word sum, different sentences). Sentence identity — not
    just word count — moves the cross-tokenizer token vector (bank deltas
    span e.g. gemma-llama -4..0 per sentence; llama-vs-qwen directions are
    zero-variance until the bank gains divergent words), and items whose
    A- and B-block tokenizer gaps stack in the same direction cannot hit
    +-10 with one deterministic packing. Selection scores use cached
    per-sentence vectors (approximate); acceptance remains the exact
    compiled-prompt verification."""
    ea = f"{g26.EVIDENCE_A_HEADER}\n{item.critical_evidence}"
    eb = f"{g26.EVIDENCE_B_HEADER}\n{rec['b']}"
    ea_tok = {tag: fn(ea) for tag, fn in fill.tok.items()}
    eb_tok = {tag: fn(eb) for tag, fn in fill.tok.items()}
    tags = list(fill.tok)

    # ---- a-side: mixes over the FULL bank at every reachable word target
    a_cands = []
    for w in range(4, W_MAX + 1):
        for idxs in pack_with_shuffle(fill.wc, w, K_MIX, seed_key=1):
            vec = {t: fill.hdr[t] + sum(fill.svec[t][i] for i in idxs)
                   for t in tags}
            score = max(abs(vec[t] - ea_tok[t]) for t in tags)
            a_cands.append((score, abs(w - len(g26.words(ea))), w, idxs, vec))
    a_cands.sort(key=lambda x: (x[0], x[1], x[2]))
    if not a_cands:
        return None

    for score_a, _, w_a, idxs_a, vec_a in a_cands[:W_A_KEEP]:
        # exact-tokenize this FA candidate; selection below uses the exact
        # a-side residuals against approximate b-side vectors
        fa_text = fill.text(idxs_a)
        fa_exact = {t: fill.tok[t](fa_text) for t in tags}
        a_vec = {t: fa_exact[t] - ea_tok[t] for t in tags}
        a_words = sum(fill.wc[i] for i in idxs_a)
        rem = [i for i in range(len(fill.bank)) if i not in set(idxs_a)]
        if not rem:
            continue
        rem_w = [fill.wc[i] for i in rem]

        b_cands = []
        for w in range(4, min(W_MAX, sum(rem_w)) + 1):
            for ridx in pack_with_shuffle(rem_w, w, K_MIX,
                                          seed_key=2 + w_a):
                bank_i = [rem[j] for j in ridx]
                vec = {t: fill.hdr[t] + sum(fill.svec[t][i] for i in bank_i)
                       for t in tags}
                pred = max(max(abs(a_vec[t]),
                               abs(vec[t] - eb_tok[t]),
                               abs(a_vec[t] + vec[t] - eb_tok[t]))
                           for t in tags)
                b_cands.append((pred, abs(w - len(g26.words(eb))), w, bank_i))
        b_cands.sort(key=lambda x: (x[0], x[1], x[2]))

        for pred, _, w_b, bank_i in b_cands[:W_B_KEEP]:
            meta_try = {
                "filler_a": [fill.bank[i] for i in idxs_a],
                "filler_b": [fill.bank[i] for i in bank_i],
                "filler_words_a": a_words,
                "filler_words_b": sum(fill.wc[i] for i in bank_i),
            }
            item.meta.update(meta_try)
            dists = verify_distances(item, fill.tok)
            if max(dists.values()) <= MAX_DIST_TOKENS:
                dist_out.update(dists)
                return meta_try
    return None


def verify_distances(item: Item, tok_by_tag) -> dict:
    """rule->judgment token distance spread across t0/t1/t2, per arm/token."""
    out = {}
    for arm in ("excl", "admit"):
        per_tag: dict[str, list[int]] = {t: [] for t in tok_by_tag}
        for timing in (0, 1, 2):
            cond = f"g26_{arm}_t{timing}"
            off = rule_char_offset(item, cond, "reasoned")
            assert off is not None, cond
            suffix = compile_prompt(item, cond, "reasoned")[off:]
            for tag, fn in tok_by_tag.items():
                per_tag[tag].append(fn(suffix))
        for tag, ds in per_tag.items():
            out[f"{arm}_{tag}"] = max(ds) - min(ds)
    return out


# ---------------------------------------------------------------------- main

def other_pool_ids(exclude: set) -> set:
    """Item ids already used by earlier item files (§9.11 disjointness)."""
    seen = set()
    for path in ("data/items/items_v1.jsonl",
                 "data/items/g23a_v1.jsonl",
                 "data/items/g23b_v1.jsonl",
                 "data/items/g24a_v1.jsonl",
                 "data/items/g24a_candidates_v1.jsonl",
                 "data/items/g25_v1.jsonl"):
        if not os.path.exists(path):
            continue
        with open(path) as f:
            for line in f:
                seen.add(json.loads(line)["item_id"])
    return seen & exclude


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT_DEFAULT)
    ap.add_argument("--report", default=REPORT_DEFAULT)
    ap.add_argument("--md", default=None,
                    help="default: report path with .md suffix")
    ap.add_argument("--audit", default=AUDIT_DEFAULT)
    args = ap.parse_args()
    md_path = args.md or (os.path.splitext(args.report)[0] + ".md")
    os.environ.setdefault("HF_HUB_OFFLINE", "1")

    # bank schedule: {4..20} x 4 = 816 words (prereg §3 / conditions docstring)
    sched = dict(sorted(collections.Counter(
        len(g26.words(s)) for s in g26.FILLER_BANK).items()))
    want_sched = {w: 4 for w in range(4, 21)}
    assert sched == want_sched, f"filler bank schedule broken: {sched}"

    audit = json.load(open(args.audit))
    data = ah.load_claims()

    db_path = DB_REL
    sz = os.path.getsize(db_path)
    assert sz == ah.EXPECTED_DB_BYTES, (sz, ah.EXPECTED_DB_BYTES)
    conn, tables = ah.open_db(db_path)
    store = ah.find_page_store(conn, tables)
    assert store is not None, tables
    t, id_col, text_col = store
    cache: dict = {}
    tiers = collections.Counter()
    page = raw_page_chain(conn, t, id_col, text_col, cache, tiers)

    print("[build] sweeping train+dev through the audit funnel ...",
          flush=True)
    stats, train_recs = sweep(data, page)
    conn.close()

    checks = audit_assertions(stats, audit)
    bad = [c for c in checks if not c["ok"]]
    if bad:
        for c in bad:
            print(f"  ASSERT FAIL {c['field']}: builder={c['builder']} "
                  f"audit={c['audit']}", file=sys.stderr)
        return 2
    print(f"[build] all {len(checks)} audit assertions OK "
          f"(train survivors {stats['train']['survivors']})", flush=True)

    # panel tokenizers (build-time only; zero model forwards)
    from transformers import AutoTokenizer
    tok_by_tag = {}
    tok_dirs = {}
    for tag, mid in PANEL_MODEL_IDS.items():
        path = resolve_tokenizer_dir(mid)
        tok_dirs[tag] = path
        tk = AutoTokenizer.from_pretrained(path, local_files_only=True)
        tok_by_tag[tag] = (
            lambda text, _tk=tk: len(
                _tk(text, add_special_tokens=False)["input_ids"]))

    fill = Fill(tok_by_tag, g26.FILLER_BANK,
                [len(g26.words(s)) for s in g26.FILLER_BANK])

    items: list[Item] = []
    fails: list[str] = []
    deep_ok: list[str] = []
    all_dists: list[tuple[str, dict]] = []
    for n, rec in enumerate(train_recs, 1):
        s_val = ah.LABELS[rec["label"]]
        meta = {
            "uid": rec["uid"], "split": "train", "hpqa_id": rec["hpqa_id"],
            "title_pair": rec["title_pair"],
            "page_a": rec["page_a"], "page_b": rec["page_b"],
            "gold_label": rec["label"], "s": s_val,
            "orient": rec["orient"],
            "reversed_list_order": rec["reversed"],
            "words_a": rec["words_a"], "words_b": rec["words_b"],
            "leak": rec["leak"], "evidence_b": rec["b"],
        }
        item = Item(
            item_id=f"g26a_{rec['uid']}",
            task_family="g26a_hover",
            surface_domain="wikipedia",
            base_context=rec["claim"],
            critical_evidence=rec["a"],
            critical_label="evidence A",
            critical_direction="increase" if s_val > 0 else "decrease",
            exclusion_reason="none_stated",
            evidence_truth="true_but_forbidden",
            admit_rule=g26.ADMIT_RULE,
            exclude_rule=g26.EXCL_RULE,
            question=g26.QUESTION,
            output_spec=g26.OUTPUT_SPEC,
            memory_question=g26.MEMORY_QUESTION,
            rule_probe_question=g26.RULE_PROBE_QUESTION,
            ground_truth=None,
            meta=meta,
        )
        dist: dict = {}
        got = furnish(rec, item, fill, dist)
        if got is None:
            got = furnish_deep(rec, item, fill, dist)
            if got is not None:
                deep_ok.append(item.item_id)
        if got is None:
            fails.append(item.item_id)
            continue
        meta.update(got)
        meta["dist_max"] = dist
        items.append(item)
        all_dists.append((item.item_id, dist))
        if n % 500 == 0:
            print(f"[build] furnished {n}/{len(train_recs)}", flush=True)

    print(f"[build] fast-path: {len(items) - len(deep_ok)} items, "
          f"deep mix-search rescued: {len(deep_ok)}", flush=True)
    if fails:
        fails_path = "logs/g26a_furnish_fails.json"
        with open(fails_path, "w") as f:
            json.dump({"n": len(fails),
                       "item_ids": fails,
                       "uids": [x.removeprefix("g26a_") for x in fails]},
                      f, indent=1)
        print(f"  FURNISH FAIL n={len(fails)} (full list -> {fails_path}) "
              f"e.g. {fails[:5]}",
              file=sys.stderr)
        return 3
    if len(items) != PIN_TRAIN_SURVIVORS:
        print(f"  PIN FAIL: built {len(items)} != {PIN_TRAIN_SURVIVORS}",
              file=sys.stderr)
        return 4

    dup = [i for i, c in collections.Counter(
        it.item_id for it in items).items() if c > 1]
    assert not dup, f"duplicate item ids {dup[:5]}"
    clash = other_pool_ids({it.item_id for it in items})
    assert not clash, f"id disjointness violated: {sorted(clash)[:5]}"

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(asdict_json(it), ensure_ascii=False) + "\n")
    items_sha = sha256_file(args.out)
    print(f"[build] wrote {args.out} n={len(items)} sha256={items_sha[:16]}",
          flush=True)

    # distance summary
    max_by_key: dict[str, int] = {}
    worst: list[tuple[int, str, str]] = []
    for iid, dist in all_dists:
        for k, v in dist.items():
            max_by_key[k] = max(max_by_key.get(k, 0), v)
            worst.append((v, k, iid))
    worst.sort(reverse=True)
    assert max(max_by_key.values()) <= MAX_DIST_TOKENS, max_by_key

    pooled = stats["_pooled"]
    report = {
        "design": "g26a_pool_v1",
        "date": datetime.date.today().isoformat(),
        "prereg": {"path": PREREG, "sha256": sha256_file(PREREG)},
        "audit": {"path": args.audit, "sha256": sha256_file(args.audit)},
        "assertions": checks,
        "items": {"path": args.out, "sha256": items_sha, "n": len(items),
                  "order": "frozen HoVer train file order"},
        "funnel": {"train": stats["train"], "dev": stats["dev"],
                   "pooled": pooled},
        "orientation": {
            "note": "A/B follow mention direction; reversed = sf1_to_sf0 "
                    "list order (prereg §2 '75 reversed survivors', §9.3)",
            "train": {k: stats["train"].get(k) for k in
                      ("fwd_oriented", "reversed_oriented",
                       "fwd_survivors", "reversed_survivors")},
            "dev": {k: stats["dev"].get(k) for k in
                    ("fwd_oriented", "reversed_oriented",
                     "fwd_survivors", "reversed_survivors")},
            "pooled_reversed_survivors": pooled["reversed_survivors"],
        },
        "labels": pooled["label_counts"],
        "clusters": {
            "train": {"title_pair": stats["train"]["title_pair_clusters"],
                      "hpqa": stats["train"]["hpqa_clusters"]},
            "dev": {"title_pair": stats["dev"]["title_pair_clusters"],
                    "hpqa": stats["dev"]["hpqa_clusters"]},
            "pooled": {"title_pair": pooled["title_pair_clusters"],
                       "hpqa": pooled["hpqa_clusters"]},
        },
        "fillers": {
            "bank_sentences": len(g26.FILLER_BANK),
            "bank_words": sum(len(g26.words(s)) for s in g26.FILLER_BANK),
            "schedule_ok": True,
            "tokenizers": {"model_ids": PANEL_MODEL_IDS, "dirs": tok_dirs},
            "max_pairwise_tokens": dict(sorted(max_by_key.items())),
            "limit": MAX_DIST_TOKENS,
            "deep_rescued": {"n": len(deep_ok), "ids": deep_ok},
            "worst": [{"item_id": iid, "key": k, "delta": v}
                      for v, k, iid in worst[:10]],
        },
        "disjoint_ids_ok": True,
        "db": {"path": db_path, "bytes": sz,
               "lookup_tiers_first_hit": dict(tiers)},
    }
    with open(args.report, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=1, ensure_ascii=False)
        f.write("\n")

    md = [
        "# G26A Phase-A pool — build report (v1)",
        "",
        f"- date: {report['date']} (zero-model build)",
        f"- items: `{args.out}` n={len(items)} sha256=`{items_sha}`",
        f"- order: frozen HoVer train file order (O4/O9)",
        f"- audit: {args.audit} sha256=`{report['audit']['sha256'][:16]}` — "
        f"{len(checks)}/{len(checks)} field assertions OK",
        f"- funnel train: candidates {stats['train'].get('candidates')} -> "
        f"materialized {stats['train'].get('materialized')} -> "
        f"oriented {stats['train'].get('oriented')} -> "
        f"survivors {stats['train'].get('survivors')} "
        f"(pin {PIN_TRAIN_SURVIVORS})",
        f"- labels: {pooled['label_counts']}",
        f"- clusters train: {stats['train']['title_pair_clusters']} title-pair "
        f"/ {stats['train']['hpqa_clusters']} hpqa",
        f"- orientation: reversed survivors train "
        f"{stats['train'].get('reversed_survivors')} / dev "
        f"{stats['dev'].get('reversed_survivors')} / pooled "
        f"{pooled['reversed_survivors']} (prereg §2 cites 75)",
        f"- fillers: bank {len(g26.FILLER_BANK)} sentences / 816 words; "
        f"max rule->judgment distance spread per tokenizer: "
        f"{dict(sorted(max_by_key.items()))} (limit {MAX_DIST_TOKENS})",
        f"- id disjointness from G0/G23/G24/G25 pools: OK",
        "",
    ]
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"[build] report -> {args.report} / {md_path}", flush=True)
    return 0


def asdict_json(it: Item) -> dict:
    from dataclasses import asdict
    return asdict(it)


if __name__ == "__main__":
    sys.exit(main())
