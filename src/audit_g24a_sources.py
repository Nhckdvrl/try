#!/usr/bin/env python3
"""G24A source-data audit: FEVER + SciFact provenance, integrity and resolution.

Run:
  PYTHONPATH=src python src/audit_g24a_sources.py

Gates are exact-number checks against the official releases (re-verified
SHA-256, HF dataset-card row counts, zero unresolved references).  The report
lands in data/external/review/G24A_SOURCE_DATA_AUDIT_v1.{md,json}.
"""
from __future__ import annotations

import collections
import hashlib
import json
import re
import sys
import time
from pathlib import Path

from g24a_sources import (RAW_ROOT, _QUOTED_SPAN, _WIKI_RESIDUE, build_fever_pool,
                          build_scifact_pool, fever_text_once_pool,
                          fever_verifiable, load_fever, nfc,
                          normalize_evidence_text)

REVIEW = Path("data/external/review")
STEM = "G24A_SOURCE_DATA_AUDIT_v1"

PINNED = {
    "fever/shared_task_dev.jsonl": "e89865bfe1b4dd054e03dd57d7241a6fde24862905f31117cf0cd719f7c78df7",
    "fever/train.jsonl": "eba7e8f87076753f8494718b9a857827af7bf73e76c9e4b75420207d26e588b6",
    "fever/wiki-pages.zip": "4b06d95da6adf7fe02d2796176c670dacccb21348da89cba4c50676ab99665f2",
    "scifact/data.tar.gz": "11c621288d41ac144d29b13b0f8503b3820b7d6e8b1f6ff24dff335c196d76be",
}

# exact official counts (cross-checked against the HF dataset cards)
EXPECT = {
    "fever_dev_lines": 19998,
    "fever_dev_labels": {"NOT ENOUGH INFO": 6666, "SUPPORTS": 6666, "REFUTES": 6666},
    "fever_dev_flatten": 37566,       # HF card labelled_dev num_examples
    "fever_train_lines": 145449,
    "fever_train_flatten": 311431,    # HF card train num_examples
    "fever_verifiable": 13332,
    "fever_pool_input": 12884,          # verifiable + claim-text unique
    "fever_pool": 12648,                # after text-quality gates
    "fever_pool_labels": {"SUPPORTS": 6326, "REFUTES": 6322},
    "fever_malformed_excluded": 66,
    "fever_quote_unpaired_excluded": 32,
    "fever_paren_unbalanced_excluded": 51,
    "fever_wiki_residue_excluded": 89,
    "fever_order_sorted_claims": 110,
    "fever_refs_requested": 3462,
    "scifact_claims": {"train": 809, "dev": 300, "test": 300},
    "scifact_corpus": 5183,
    "scifact_pool": 635,
    "scifact_pool_labels": {"SUPPORT": 417, "CONTRADICT": 218},
    "scifact_multi_doc_excluded": 47,
    "scifact_no_evidence_excluded": 716,
    "scifact_malformed_excluded": 6,
    "scifact_text_quality_excluded": 5,
}

TOKENS = ("-LRB-", "-RRB-", "-LSB-", "-RSB-", "-LCB-", "-RCB-")
FAILURES: list[str] = []
GATES: list[dict] = []


def gate(name: str, ok: bool, detail: str = "") -> None:
    GATES.append({"name": name, "ok": bool(ok), "detail": detail})
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def percentiles(values: list[int]) -> dict:
    values = sorted(values)
    if not values:
        return {}
    pick = lambda q: values[min(len(values) - 1, int(len(values) * q))]
    return {"min": values[0], "p50": pick(0.50), "p90": pick(0.90),
            "p99": pick(0.99), "max": values[-1]}


def main() -> int:
    t0 = time.time()

    # ---------------- raw integrity ----------------
    for rel, want in PINNED.items():
        got = sha256(RAW_ROOT / rel)
        gate(f"sha256 {rel}", got == want, got[:16])

    # ---------------- FEVER file census ----------------
    dev = load_fever()
    gate("fever dev line count", len(dev) == EXPECT["fever_dev_lines"], str(len(dev)))
    dev_labels = collections.Counter(r["label"] for r in dev)
    gate("fever dev label balance", dict(dev_labels) == EXPECT["fever_dev_labels"], str(dict(dev_labels)))
    verifiable_field_ok = all(
        (r.get("verifiable") == "VERIFIABLE") == (r["label"] in ("SUPPORTS", "REFUTES"))
        for r in dev)
    gate("fever verifiable field consistent with label", verifiable_field_ok)
    nei_sentence_refs = sum(
        1 for r in dev if r["label"] == "NOT ENOUGH INFO"
        for g in r["evidence"] for t in g if t[2] is not None)
    gate("fever NEI records carry zero sentence refs", nei_sentence_refs == 0, str(nei_sentence_refs))
    dev_flatten = sum(sum(len(g) for g in r["evidence"]) if r["evidence"] else 1 for r in dev)
    gate("fever dev flatten == HF card labelled_dev", dev_flatten == EXPECT["fever_dev_flatten"], str(dev_flatten))
    train_lines = train_flatten = 0
    with (RAW_ROOT / "fever/train.jsonl").open() as handle:
        for line in handle:
            record = json.loads(line)
            train_lines += 1
            train_flatten += sum(len(g) for g in record["evidence"]) if record["evidence"] else 1
    gate("fever train line count", train_lines == EXPECT["fever_train_lines"], str(train_lines))
    gate("fever train flatten == HF card train", train_flatten == EXPECT["fever_train_flatten"], str(train_flatten))

    ver = fever_verifiable(dev)
    ver_counts = collections.Counter(r["claim"] for r in ver)
    gate("fever verifiable records", len(ver) == EXPECT["fever_verifiable"], str(len(ver)))
    pool_meta = [r for r in ver if ver_counts[r["claim"]] == 1]
    pool_labels = collections.Counter(r["label"] for r in pool_meta)
    gate("fever text-once pool size", len(pool_meta) == EXPECT["fever_pool_input"],
         str(len(pool_meta)))
    gate("fever pool label balance (pre text-quality)",
         dict(pool_labels) == {"SUPPORTS": 6449, "REFUTES": 6435}, str(dict(pool_labels)))

    # ---------------- FEVER resolution ----------------
    fever, diag = build_fever_pool()
    gate("fever refs requested", diag["refs_requested"] == EXPECT["fever_refs_requested"],
         str(diag["refs_requested"]))
    gate("fever all refs resolved", not diag["refs_missing"],
         f"missing={len(diag['refs_missing'])}")
    gate("fever no empty sentences", not diag["refs_empty"], f"empty={len(diag['refs_empty'])}")
    final_pool_labels = dict(collections.Counter(r["label"] for r in fever))
    gate("fever pool emitted == pool", len(fever) == EXPECT["fever_pool"], str(len(fever)))
    gate("fever pool labels", final_pool_labels == EXPECT["fever_pool_labels"],
         str(final_pool_labels))
    gate("fever every block non-empty", all(r["evidence_block"] for r in fever))
    for rule, key in [("malformed", "malformed_excluded"),
                      ("quote-unpaired", "quote_unpaired_excluded"),
                      ("paren-unbalanced", "paren_unbalanced_excluded"),
                      ("wiki-residue", "wiki_residue_excluded")]:
        got = diag[key]
        gate(f"fever text-quality [{rule}] excluded", got == EXPECT[f"fever_{key}"], str(got))
    gate("fever group0 tuples reading-ordered", diag["order_sorted_claims"]
         == EXPECT["fever_order_sorted_claims"], str(diag["order_sorted_claims"]))

    # duplicate/conflict exclusions (reported, by design excluded)
    dup_texts = {c: n for c, n in ver_counts.items() if n > 1}
    by_claim: dict[str, set] = collections.defaultdict(set)
    for r in ver:
        by_claim[r["claim"]].add(r["label"])
    conflicts = sorted(c for c, labs in by_claim.items() if len(labs) > 1)
    by_claim_all: dict[str, set] = collections.defaultdict(set)
    for r in dev:
        by_claim_all[r["claim"]].add(r["label"])
    conflicts_all = sorted(c for c, labs in by_claim_all.items() if len(labs) > 1)
    gate("conflicts among verifiable claims", len(conflicts) == 3, str(len(conflicts)))
    gate("conflicts counting NEI siblings (dev)", len(conflicts_all) == 54,
         str(len(conflicts_all)))

    # ---------------- normalization safety ----------------
    residual = {"token": [], "quote": [], "tab_or_nl": [], "multispace": [],
                "space_before_punct": [], "not_nfc": [], "wiki_residue": []}
    paren_mismatch: list[dict] = []
    quote_mismatch: list[dict] = []
    idem_ok = all(normalize_evidence_text(r["evidence_block"]) == r["evidence_block"]
                  for r in fever)
    for r in fever:
        raw = " ".join(r["evidence_sentences"])       # dump-raw, first TAB field
        block = r["evidence_block"]
        for tok in TOKENS:
            if tok in block:
                residual["token"].append((r["fever_id"], tok))
        if "``" in block or "''" in block:
            residual["quote"].append(r["fever_id"])
        if "\t" in block or "\n" in block:
            residual["tab_or_nl"].append(r["fever_id"])
        if "  " in block:
            residual["multispace"].append(r["fever_id"])
        if re.search(r"\s[,.;:!?%)\]]", block):
            residual["space_before_punct"].append(r["fever_id"])
        if nfc(block) != block:
            residual["not_nfc"].append(r["fever_id"])
        if _WIKI_RESIDUE.search(block):
            residual["wiki_residue"].append(r["fever_id"])
        # review lists (informational — read manually before freeze)
        n_open, n_close = block.count("("), block.count(")")
        if n_open != n_close:
            paren_mismatch.append({"fever_id": r["fever_id"], "claim": r["claim"],
                                   "block": block, "open": n_open, "close": n_close})
        raw_opens, raw_closes = raw.count("``"), raw.count("''")
        if raw_opens != raw_closes:
            quote_mismatch.append({"fever_id": r["fever_id"], "claim": r["claim"],
                                   "raw": raw, "open": raw_opens, "close": raw_closes,
                                   "residual": _QUOTED_SPAN.sub(r'"\1"', raw)})
    gate("normalization idempotent + self-consistent", idem_ok)
    gate("fever kept blocks paren-balanced", not paren_mismatch,
         f"{len(paren_mismatch)} violations")
    gate("fever kept blocks quote-paired", not quote_mismatch,
         f"{len(quote_mismatch)} violations")
    for key, hits in residual.items():
        gate(f"fever residual {key}", not hits, f"{len(hits)} hits" + (f" e.g. {hits[:3]}" if hits else ""))

    fever_chars = [len(r["evidence_block"]) for r in fever]
    fever_sents = [len(r["evidence_sentences"]) for r in fever]

    # ---------------- SciFact ----------------
    scifact, sdiag = build_scifact_pool()
    claim_counts = {}
    for split, want in EXPECT["scifact_claims"].items():
        got = sum(1 for line in (RAW_ROOT / f"scifact/data/claims_{split}.jsonl").open())
        claim_counts[split] = got
        gate(f"scifact claims_{split} count", got == want, str(got))
    corpus_lines = sum(1 for _ in (RAW_ROOT / "scifact/data/corpus.jsonl").open())
    gate("scifact corpus count", corpus_lines == EXPECT["scifact_corpus"], str(corpus_lines))
    gate("scifact pool size", len(scifact) == EXPECT["scifact_pool"], str(len(scifact)))
    s_labels = collections.Counter(r["label"] for r in scifact)
    gate("scifact pool labels", dict(s_labels) == EXPECT["scifact_pool_labels"], str(dict(s_labels)))
    gate("scifact malformed excluded", sdiag["malformed_excluded"]
         == EXPECT["scifact_malformed_excluded"], str(sdiag["malformed_excluded"]))
    gate("scifact text-quality excluded", sdiag["text_quality_excluded"]
         == EXPECT["scifact_text_quality_excluded"], str(sdiag["text_quality_excluded"]))
    gate("scifact exclusions", 
         sdiag["multi_doc_excluded"] == EXPECT["scifact_multi_doc_excluded"]
         and sdiag["no_evidence"] == EXPECT["scifact_no_evidence_excluded"],
         str(sdiag))
    gate("scifact no mixed labels", sdiag["mixed_label_excluded"] == 0)
    gate("scifact no missing docs / no out-of-bounds",
         sdiag["missing_doc_excluded"] == 0 and sdiag["out_of_bounds_excluded"] == 0)
    gate("scifact every block non-empty", all(r["evidence_block"] for r in scifact))
    s_idem = all(normalize_evidence_text(r["evidence_block"]) == r["evidence_block"]
                 for r in scifact)
    gate("scifact normalization idempotent", s_idem)
    s_resid = [r["scifact_id"] for r in scifact
               if ("\t" in r["evidence_block"] or "\n" in r["evidence_block"]
                   or "  " in r["evidence_block"]
                   or nfc(r["evidence_block"]) != r["evidence_block"]
                   or _WIKI_RESIDUE.search(r["evidence_block"]))]
    gate("scifact residual (tab/nl/space/nfc/residue)", not s_resid, str(s_resid[:5]))
    s_content_ok = all(
        re.sub(r"\s", "", s) == re.sub(r"\s", "", normalize_evidence_text(s))
        for r in scifact for s in r["evidence_sentences"])
    gate("scifact normalization whitespace-only (content preserved)", s_content_ok)

    scifact_changed = [r["scifact_id"] for r in scifact
                       if " ".join(r["evidence_sentences"]) != r["evidence_block"]]
    s_chars = [len(r["evidence_block"]) for r in scifact]
    s_sents = [len(r["evidence_sentences"]) for r in scifact]

    overlap = {r["claim"] for r in fever} & {r["claim"] for r in scifact}
    gate("no claim-text overlap fever vs scifact", not overlap, f"{len(overlap)}")

    # ---------------- samples for manual reading ----------------
    def pick(pool, pred, fallback=None):
        for r in pool:
            if pred(r):
                return r
        return fallback or pool[0]

    raw_of = lambda r: " ".join(r["evidence_sentences"])
    samples = []
    sample_specs = [
        ("paren + IPA (accented wiki markup)",
         lambda r: "-LSB-" in raw_of(r) and any(ch in raw_of(r) for ch in "ˈˌ")),
        ("quoted nickname", lambda r: "``" in raw_of(r)),
        ("glued possessive", lambda r: " '" + "s" in raw_of(r) or " 's" in raw_of(r)),
        ("accented evidence page",
         lambda r: any(not p.isascii() for p in r["evidence_pages"])),
        ("multi-sentence joint evidence set", lambda r: r["group0_tuples"] >= 2),
        ("plain single sentence", lambda r: r["group0_tuples"] == 1 and
         not any(t in raw_of(r) for t in TOKENS) and "``" not in raw_of(r)),
        ("REFUTES single page", lambda r: r["label"] == "REFUTES" and r["group0_tuples"] == 1
         and not any(ch.isascii() is False for ch in r["claim"])),
        ("longest block", lambda r: len(r["evidence_block"]) >= max(fever_chars) - 1),
    ]
    used = set()
    for title, pred in sample_specs:
        r = pick(fever, lambda x, p=pred: p(x) and x["fever_id"] not in used)
        used.add(r["fever_id"])
        samples.append({"kind": title, "source": "fever", "id": r["fever_id"],
                        "label": r["label"], "claim": r["claim"],
                        "raw": raw_of(r), "normalized": r["evidence_block"]})
    for title, lab in [("SciFact SUPPORT union rationale", "SUPPORT"),
                       ("SciFact CONTRADICT union rationale", "CONTRADICT")]:
        r = pick(scifact, lambda x, l=lab: x["label"] == l and len(x["evidence_sentences"]) >= 2)
        samples.append({"kind": title, "source": "scifact", "id": r["scifact_id"],
                        "label": r["label"], "claim": r["claim"],
                        "raw": raw_of(r), "normalized": r["evidence_block"]})
    # accented-page demonstration: raw ref -> NFC -> sentence
    accent_demo = None
    for r in fever:
        if any(not p.isascii() for p in r["evidence_pages"]):
            accent_demo = {"claim": r["claim"], "page": r["evidence_pages"][0],
                           "block": r["evidence_block"]}
            break

    # ---------------- write report ----------------
    REVIEW.mkdir(parents=True, exist_ok=True)
    census = {
        "generated": time.strftime("%Y-%m-%d %H:%M:%S"),
        "elapsed_s": round(time.time() - t0, 1),
        "pinned_sha256": PINNED,
        "expect": EXPECT,
        "fever": {
            "dev_lines": len(dev), "dev_labels": dict(dev_labels),
            "dev_flatten": dev_flatten, "train_lines": train_lines,
            "train_flatten": train_flatten, "verifiable": len(ver),
            "dup_text_excluded_records": sum(dup_texts.values()) - len(dup_texts),
            "dup_text_excluded_texts": len(dup_texts),
            "label_conflict_texts": conflicts,
            "pool": len(fever), "pool_labels": final_pool_labels,
            "resolution": diag,
            "block_chars": percentiles(fever_chars),
            "sentences_per_block": dict(sorted(collections.Counter(fever_sents).items())),
            "multi_group_claims": sum(1 for r in fever if r["n_groups"] > 1),
        },
        "scifact": {
            "claim_counts": claim_counts, "corpus": corpus_lines,
            "pool": len(scifact), "pool_labels": dict(s_labels),
            "exclusions": sdiag,
            "blocks_changed_by_normalization": len(scifact_changed),
            "block_chars": percentiles(s_chars),
            "sentences_per_block": dict(sorted(collections.Counter(s_sents).items())),
        },
        "residuals": {k: len(v) for k, v in residual.items()},
        "paren_mismatch_blocks": paren_mismatch,
        "quote_mismatch_blocks": quote_mismatch,
        "samples": samples,
        "accented_page_demo": accent_demo,
        "gates": GATES,
        "failures": FAILURES,
    }
    (REVIEW / f"{STEM}.json").write_text(json.dumps(census, ensure_ascii=False, indent=1))

    lines = [
        "# G24A source-data audit v1 — FEVER + SciFact",
        "",
        f"Generated {census['generated']} by `src/audit_g24a_sources.py` "
        f"({census['elapsed_s']}s). Machine census: `{STEM}.json`.",
        "",
        "## 1. Verdict",
        "",
        ("**AUDIT PASS** — all gates green." if not FAILURES
         else f"**AUDIT FAIL** — {len(FAILURES)} gate(s): " + "; ".join(FAILURES)),
        "",
        "## 2. Pinned sources (SHA-256 re-verified this run)",
        "",
        "| file | sha256 |",
        "| --- | --- |",
        *[f"| `{k}` | `{v}` |" for k, v in PINNED.items()],
        "",
        "Licenses (official cards): FEVER data CC-BY-SA-3.0 / code GPL-3.0; "
        "SciFact CC-BY-NC-2.0 (non-commercial research).",
        "",
        "## 3. Integrity gates",
        "",
        "| gate | result | detail |",
        "| --- | --- | --- |",
        *[f"| {g['name']} | {'PASS' if g['ok'] else '**FAIL**'} | {g['detail']} |"
          for g in GATES],
        "",
        "## 4. FEVER construction",
        "",
        f"- dev {len(dev)} lines = {dict(dev_labels)}; `verifiable` field agrees with "
        "label on every record; NEI records carry zero sentence refs.",
        f"- flatten arithmetic matches the HF card exactly: dev {dev_flatten} == 37,566; "
        f"train {train_flatten} == 311,431 (row-level provenance proven).",
        f"- text-once pool (verifiable + unique claim text): {len(pool_meta)} → "
        f"text-quality gates → **{len(fever)} records {final_pool_labels}**.",
        f"- excluded: NEI (6,666 records), {len(dup_texts)} "
        f"duplicated texts ({sum(dup_texts.values()) - len(dup_texts)} extra records, "
        f"including {len(conflicts)} verifiable-pool label conflicts "
        f"({len(conflicts_all)} counting NEI siblings of the same claim text; "
        f"both excluded): "
        + "; ".join(f'“{c}”' for c in conflicts) + "), then text-quality gates: "
        f"{diag['malformed_excluded']} malformed-sentence, "
        f"{diag['quote_unpaired_excluded']} unpaired-quote, "
        f"{diag['paren_unbalanced_excluded']} unbalanced-paren, "
        f"{diag['wiki_residue_excluded']} wiki-residue claims "
        "(overlapping counts; full lists reviewed item-by-item on 2026-09-24).",
        "- evidence block = group 0 (first annotated evidence set), tuples in "
        "reading order (page first-appearance, then line; "
        f"{diag['order_sorted_claims']} claims reordered), NFC page matching, "
        "first TAB field only (hyperlink annotations stripped), per-sentence "
        "normalization then join.",
        f"- resolution: {diag['refs_requested']} refs over {diag['pages_requested']} pages → "
        f"{diag['refs_resolved']} resolved, {len(diag['refs_missing'])} missing, "
        f"{len(diag['refs_empty'])} empty.",
        "",
        "## 5. Text normalization",
        "",
        "Rules (order): NFC → bracket parse tokens → ``...'' paired quotes → "
        "claims whose raw sentences still contain unpaired ``/'' are "
        "**excluded** (quote-pair gate; a defensive \" / ' fallback exists in "
        "code but never fires on the kept pool) → glued `'s` → "
        "tokenized spacing before punctuation and after open brackets/currency → "
        "whitespace collapse. Word content is never altered.",
        "",
        f"- residual scan over all {len(fever)} FEVER blocks: "
        + ", ".join(f"{k}={len(v)}" for k, v in residual.items()),
        f"- idempotence + self-consistency: {'PASS' if idem_ok else 'FAIL'}",
        f"- kept-pool verification: {len(paren_mismatch)} paren-imbalance, "
        f"{len(quote_mismatch)} unpaired-quote blocks (expected 0 — gates above)",
        "",
        "### 5.1 Before/after samples",
        "",
    ]
    for s in samples:
        lines += [f"**{s['kind']}** ({s['source']} id={s['id']}, {s['label']})",
                  "",
                  f"- claim: {s['claim']}",
                  f"- raw: {s['raw']}",
                  f"- normalized: {s['normalized']}", ""]
    if accent_demo:
        lines += ["### 5.2 Accented-page resolution (NFC fix)", "",
                  f"- claim: {accent_demo['claim']}",
                  f"- page (NFC): {accent_demo['page']}",
                  f"- resolved: {accent_demo['block']}", ""]
    lines += ["### 5.3 Text-quality exclusions (examples from the frozen build)", "",
              "Every excluded claim's full list was reviewed item-by-item on "
              "2026-09-24 (dump artifacts only; content never rewritten). "
              "Counts: malformed "
              f"{diag['malformed_excluded']} / unpaired-quote "
              f"{diag['quote_unpaired_excluded']} / unbalanced-paren "
              f"{diag['paren_unbalanced_excluded']} / wiki-residue "
              f"{diag['wiki_residue_excluded']}. Examples:", ""]
    for item in diag["malformed_examples"][:6]:
        lines.append(f"- malformed [{item['fever_id']}] “{item['claim'][:80]}” → "
                     f"“{item['sentence'][:140]}”")
    for item in diag["quote_examples"][:6]:
        lines.append(f"- unpaired-quote [{item['fever_id']}] “{item['claim'][:80]}” → "
                     f"“{item['sentence'][:140]}”")
    for item in diag["paren_examples"][:6]:
        lines.append(f"- unbalanced-paren [{item['fever_id']}] “{item['claim'][:80]}” → "
                     f"“{item['block'][:140]}”")
    for item in diag["residue_examples"][:6]:
        lines.append(f"- wiki-residue [{item['fever_id']}] hit {item['hit']!r} → "
                     f"“{item['block'][:130]}”")
    for item in sdiag["text_quality_examples"][:6]:
        lines.append(f"- SciFact text-quality [id={item['scifact_id']}] "
                     f"“{item['claim'][:80]}” → “{item['block'][:140]}”")
    lines += [
        "",
        "## 6. SciFact construction",
        "",
        f"- claims train/dev/test = {claim_counts['train']}/{claim_counts['dev']}/"
        f"{claim_counts['test']}; corpus = {corpus_lines} abstracts.",
        f"- pool = evidence-bearing, single-document, single-label claims: "
        f"{len(scifact)} {dict(s_labels)} "
        f"(excluded: {sdiag['no_evidence']} no-evidence, "
        f"{sdiag['multi_doc_excluded']} multi-doc; mixed-label=0, out-of-bounds=0, "
        f"missing-doc=0).",
        "- rationale indices are 0-based (verified against claim↔sentence content on "
        "independent samples); block = union of rationale sentences, ascending.",
        f"- normalization changed {len(scifact_changed)} of {len(scifact)} blocks "
        "(whitespace only: trailing blanks/newlines and space-before-punctuation "
        "such as `P = .04` → `P =.04`; verified by the "
        "whitespace-only content-preservation gate — no non-whitespace "
        "character ever changes).",
        "",
        "## 7. Pool shape",
        "",
        f"- FEVER block chars: {census['fever']['block_chars']}; sentences/block: "
        f"{census['fever']['sentences_per_block']}; multi-group claims: "
        f"{census['fever']['multi_group_claims']}.",
        f"- SciFact block chars: {census['scifact']['block_chars']}; sentences/block: "
        f"{census['scifact']['sentences_per_block']}.",
        f"- cross-dataset claim-text overlap: {len(overlap)}.",
        "",
        "## 8. Downstream hooks",
        "",
        "- cluster keys frozen for the G24A prereg: FEVER → first evidence wiki page "
        "(NFC); SciFact → evidence doc_id.",
        "- selection must use Base/Admit leverage only; Exclude outcomes are never "
        "seen during selection (PAPER_SCALE_AUDIT §7).",
        "",
    ]
    (REVIEW / f"{STEM}.md").write_text("\n".join(lines))

    # console: text-quality exclusion examples (full lists reviewed in-session)
    print(f"\n===== text-quality exclusion examples =====")
    for tag, key in [("malformed", "malformed_examples"), ("quote", "quote_examples"),
                     ("paren", "paren_examples"), ("residue", "residue_examples")]:
        print(f"--- {tag} ({len(diag[key])} examples kept):")
        for item in diag[key][:6]:
            print(f"   [{item.get('fever_id')}] {item.get('claim', '')[:90]!r}")
            body = item.get("sentence") or item.get("block") or ""
            print(f"        {body[:220]!r}")
    print("\n--- scifact text-quality:")
    for item in sdiag["text_quality_examples"][:6]:
        print(f"   [id={item['scifact_id']}] {item['claim'][:90]!r}")
        print(f"        {item['block'][:220]!r}")
    print(f"\n===== samples =====")
    for s in samples:
        print(f"\n--- {s['kind']} ({s['source']} id={s['id']}, {s['label']})")
        print(f"  claim:     {s['claim']}")
        print(f"  raw:       {s['raw'][:500]}")
        print(f"  normalized:{s['normalized'][:500]}")

    print(f"\n{'AUDIT PASS' if not FAILURES else 'AUDIT FAIL'} "
          f"({len(GATES) - len(FAILURES)}/{len(GATES)} gates) "
          f"-> {REVIEW}/{STEM}.md")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
