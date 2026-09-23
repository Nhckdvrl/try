"""G24A source loading: FEVER + SciFact -> resolved natural-evidence blocks.

Deterministic and stdlib-only.  Nothing here is ever rewritten by an LLM.

FEVER
-----
* pool = verifiable (SUPPORTS/REFUTES) records of ``shared_task_dev.jsonl``
  whose claim text occurs exactly once among verifiable records;
* evidence block = the sentences of the FIRST annotated evidence set
  (``evidence[0]``) — a complete gold evidence set under FEVER's evaluation
  semantics, without the bloat of unioning up to 52 redundant tuples;
* ``(page, line)`` references are resolved against the official wiki shards.
  Page ids are NFC-normalized on both sides (33 references use decomposed
  Unicode forms in the raw claim file);
* each sentence keeps only its first TAB-delimited field: the dump appends
  hyperlink annotations (``text \\t mention \\t target ...``) that must never
  reach a prompt.

SciFact
-------
* pool = claims with at least one evidence entry, citing exactly ONE corpus
  document (multi-document claims excluded so that E is one coherent block);
* every entry of a claim carries the same label (audited: 0 mixed labels);
* evidence block = the union of rationale sentence indices across entries,
  de-duplicated, ascending, resolved against ``corpus.jsonl`` (0-based).

``normalize_evidence_text`` restores the FEVER wiki dump's lossy encodings
(parse tokens, tokenized spacing, ``quoted'' spans, glued possessives) back to
readable prose.  It never changes word content; on SciFact's clean prose it is
a no-op (verified by the audit).
"""
from __future__ import annotations

import collections
import json
import re
import unicodedata
from pathlib import Path

RAW_ROOT = Path("data/external/raw")

_BRACKET_TOKENS = (("-LRB-", "("), ("-RRB-", ")"), ("-LSB-", "["),
                   ("-RSB-", "]"), ("-LCB-", "{"), ("-RCB-", "}"))
_QUOTED_SPAN = re.compile(r"``\s*(.+?)\s*''")
_POSSESSIVE = re.compile(r"(\w)\s+'s\b")
_POSSESSIVE_PLURAL = re.compile(r"(\w)\s+'(?=\s|$)")
_SPACE_BEFORE_PUNCT = re.compile(r"\s+([,.;:!?%)\]])")
_SPACE_AFTER_OPEN = re.compile(r"([(\[])\s+")
_SPACE_AFTER_CURRENCY = re.compile(r"([$])\s+")
_MULTI_SPACE = re.compile(r"[ \t]+")

_WELL_FORMED_START = set('"\'[($£€¥#')
_WELL_FORMED_END = set('.?!":)]')

# Wiki-syntax / markup residue that must never reach a prompt.  Checked on
# the NORMALIZED block (after quote restoration, single backticks remain).
_WIKI_RESIDUE = re.compile(
    r"\[\[|\]\]|\{\{|\}\}|links\s*=|lang\s*="
    r"|=\s*(?:no|yes|true|false)\b|&nbsp;|\||`")


def quote_pair_ok(raw_sentence: str) -> bool:
    """True when every quote token in the raw sentence is consumed by a
    paired ``...'' span.  Leftover tokens are wiki italic/bold residue
    (e.g. film-title markup); such sentences are excluded, never rewritten."""
    leftover = _QUOTED_SPAN.sub("", raw_sentence)
    return "``" not in leftover and "''" not in leftover


def is_well_formed(sentence: str) -> bool:
    """Text-quality gate for evidence sentences (outcome-blind).

    The FEVER wiki dump contains sentence-splitter fragments: blocks that
    start with punctuation (```, and ...``), start mid-word-case
    (``as The Kurgan ...``), or end without a terminal character
    (``...known for his roles``).  Any malformed sentence disqualifies the
    whole evidence set, so a candidate block is always clean prose.  Applied
    identically to SciFact (which it does not affect).
    """
    text = sentence.strip()
    if len(text) < 8 or not any(ch.isalnum() for ch in text):
        return False
    first = text[0]
    if not (first.isupper() or first.isdigit() or first in _WELL_FORMED_START
            or (first.isalpha() and len(text) > 1 and text[1].isupper())):
        return False
    return text[-1] in _WELL_FORMED_END


def nfc(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def normalize_evidence_text(text: str) -> str:
    """Deterministic restoration of dump-encoded evidence text.

    Rules (in order): NFC; bracket parse tokens -> literal characters;
    ```...'' -> \"...\"; glued ``x 's`` -> ``x's``; drop tokenized spaces
    before punctuation and after open brackets/currency; collapse runs of
    whitespace.  Word content is never altered.
    """
    text = nfc(text)
    for token, literal in _BRACKET_TOKENS:
        text = text.replace(token, literal)
    text = _QUOTED_SPAN.sub(r'"\1"', text)
    text = text.replace("``", '"').replace("''", "'")
    text = _POSSESSIVE.sub(r"\1's", text)
    text = _POSSESSIVE_PLURAL.sub(r"\1'", text)
    text = _SPACE_BEFORE_PUNCT.sub(r"\1", text)
    text = _SPACE_AFTER_OPEN.sub(r"\1", text)
    text = _SPACE_AFTER_CURRENCY.sub(r"\1", text)
    text = _MULTI_SPACE.sub(" ", text)
    return text.strip()


def sentence_field(raw_line_payload: str) -> str:
    """First TAB field of a wiki shard line: sentence text, hyperlink
    annotations stripped."""
    return raw_line_payload.split("\t", 1)[0].strip()


# --------------------------------------------------------------------------
# FEVER
# --------------------------------------------------------------------------
def load_fever(path: Path | None = None) -> list[dict]:
    path = path or RAW_ROOT / "fever/shared_task_dev.jsonl"
    with path.open() as handle:
        return [json.loads(line) for line in handle]


def fever_verifiable(records: list[dict]) -> list[dict]:
    return [r for r in records if r["label"] in ("SUPPORTS", "REFUTES")]


def fever_text_once_pool(records: list[dict]) -> list[dict]:
    """Verifiable records whose claim text is unique among verifiable records."""
    ver = fever_verifiable(records)
    counts = collections.Counter(r["claim"] for r in ver)
    return [r for r in ver if counts[r["claim"]] == 1]


def fever_group0_refs(pool: list[dict]) -> dict[str, set[int]]:
    """NFC page title -> line numbers referenced by evidence[0] tuples."""
    refs: dict[str, set[int]] = collections.defaultdict(set)
    for record in pool:
        for tuple_ in record["evidence"][0]:
            page, line = tuple_[2], tuple_[3]
            if page is None:
                continue
            refs[nfc(page)].add(line)
    return refs


def resolve_fever_sentences(refs: dict[str, set[int]],
                            shards_dir: Path | None = None) -> dict[tuple[str, int], str]:
    """Stream the official wiki shards once and resolve every requested
    (NFC page, line) reference to its normalized sentence text.

    Returns {(nfc_page, line): text}.  Missing refs are simply absent; the
    audit asserts the dict covers the full request.
    """
    shards_dir = shards_dir or RAW_ROOT / "fever/wiki-pages"
    resolved: dict[tuple[str, int], str] = {}
    pending = set(refs)
    for shard in sorted(shards_dir.glob("wiki-*.jsonl")):
        with shard.open() as handle:
            for line in handle:
                record = json.loads(line)
                if not record.get("id"):
                    continue          # leading empty placeholder records
                page = nfc(record["id"])
                if page not in refs:
                    continue
                wanted = refs[page]
                for chunk in record["lines"].split("\n"):
                    if not chunk:
                        continue
                    number, payload = chunk.split("\t", 1)
                    number = int(number)
                    if number in wanted and (page, number) not in resolved:
                        text = sentence_field(payload)
                        resolved[(page, number)] = text
                        pending.discard((page, number))
        if not pending:
            break
    return resolved


def build_fever_pool(shards_dir: Path | None = None) -> tuple[list[dict], dict]:
    """Full FEVER candidate pool with resolved evidence blocks.

    Returns (records, diagnostics) where diagnostics carries resolution stats
    (requested/resolved/missing/empty counts) for the audit.
    """
    records = fever_text_once_pool(load_fever())
    refs = fever_group0_refs(records)
    resolved = resolve_fever_sentences(refs, shards_dir)

    out, missing, empty, deduped = [], [], [], 0
    malformed_excluded, malformed_examples, order_sorted = 0, [], 0
    quote_excluded, paren_excluded, residue_excluded = 0, 0, 0
    quote_examples, paren_examples, residue_examples = [], [], []
    for record in records:
        # stable tuple order: pages ranked by first appearance, lines ascending
        group = record["evidence"][0]
        page_rank: dict[str, int] = {}
        for tuple_ in group:
            if tuple_[2] is not None:
                page_rank.setdefault(nfc(tuple_[2]), len(page_rank))
        ordered = sorted(
            (t for t in group if t[2] is not None),
            key=lambda t: (page_rank[nfc(t[2])], t[3]))
        if [t[3] for t in ordered] != [t[3] for t in group if t[2] is not None]:
            order_sorted += 1

        seen: set[tuple[str, int]] = set()
        sentences, keys = [], []
        bad = False
        for page, line in ((nfc(t[2]), t[3]) for t in ordered):
            key = (page, line)
            if key in seen:
                deduped += 1
                continue
            seen.add(key)
            keys.append(key)
            if key not in resolved or not resolved[key]:
                (missing if key not in resolved else empty).append(key)
                bad = True
                break
            sentences.append(resolved[key])
        if bad or not sentences:
            continue
        normalized = [normalize_evidence_text(s) for s in sentences]
        if not all(is_well_formed(s) for s in normalized):
            malformed_excluded += 1
            if len(malformed_examples) < 12:
                first_bad = next(s for s in normalized if not is_well_formed(s))
                malformed_examples.append(
                    {"fever_id": record["id"], "claim": record["claim"],
                     "sentence": first_bad[:220]})
            continue

        # --- text-quality gates (content never rewritten, only excluded) ---
        block = " ".join(normalized)
        q_ok = all(quote_pair_ok(s) for s in sentences)      # raw sentences
        p_ok = block.count("(") == block.count(")")
        w_ok = not _WIKI_RESIDUE.search(block)
        if not q_ok:
            quote_excluded += 1
            if len(quote_examples) < 12:
                bad = next(s for s in sentences if not quote_pair_ok(s))
                quote_examples.append({"fever_id": record["id"],
                                       "claim": record["claim"],
                                       "sentence": bad[:220]})
        if not p_ok:
            paren_excluded += 1
            if len(paren_examples) < 12:
                paren_examples.append({"fever_id": record["id"],
                                       "claim": record["claim"],
                                       "block": block[:220]})
        if not w_ok:
            residue_excluded += 1
            if len(residue_examples) < 12:
                residue_examples.append({"fever_id": record["id"],
                                         "claim": record["claim"],
                                         "hit": _WIKI_RESIDUE.search(block).group(0),
                                         "block": block[:220]})
        if not (q_ok and p_ok and w_ok):
            continue

        out.append({
            "source": "fever",
            "fever_id": record["id"],
            "label": record["label"],
            "direction": "increase" if record["label"] == "SUPPORTS" else "decrease",
            "claim": nfc(record["claim"]),
            "evidence_sentences": sentences,
            "evidence_block": block,
            "cluster": keys[0][0],                      # first evidence page
            "evidence_pages": sorted({k[0] for k in keys}),
            "n_groups": len(record["evidence"]),
            "group0_tuples": len(keys),
        })
    diagnostics = {
        "pool_input": len(records),
        "pages_requested": len(refs),
        "refs_requested": sum(len(v) for v in refs.values()),
        "refs_resolved": len(resolved),
        "refs_missing": sorted(set(missing)),
        "refs_empty": sorted(set(empty)),
        "duplicate_tuples_within_group0": deduped,
        "malformed_excluded": malformed_excluded,
        "malformed_examples": malformed_examples,
        "quote_unpaired_excluded": quote_excluded,
        "paren_unbalanced_excluded": paren_excluded,
        "wiki_residue_excluded": residue_excluded,
        "quote_examples": quote_examples,
        "paren_examples": paren_examples,
        "residue_examples": residue_examples,
        "order_sorted_claims": order_sorted,
        "records_emitted": len(out),
    }
    return out, diagnostics


# --------------------------------------------------------------------------
# SciFact
# --------------------------------------------------------------------------
def load_scifact_claims() -> list[dict]:
    claims = []
    for split in ("train", "dev", "test"):
        path = RAW_ROOT / f"scifact/data/claims_{split}.jsonl"
        with path.open() as handle:
            for line in handle:
                record = json.loads(line)
                record["_split"] = split
                claims.append(record)
    return claims


def load_scifact_corpus() -> dict[int, dict]:
    corpus = {}
    path = RAW_ROOT / "scifact/data/corpus.jsonl"
    with path.open() as handle:
        for line in handle:
            record = json.loads(line)
            corpus[int(record["doc_id"])] = record
    return corpus


def build_scifact_pool() -> tuple[list[dict], dict]:
    """SciFact candidate pool: evidence-bearing, single-document claims."""
    claims = load_scifact_claims()
    corpus = load_scifact_corpus()
    out, no_evidence, multi_doc, mixed, missing_doc, oob = [], 0, 0, 0, 0, 0
    malformed = 0
    text_quality = 0
    tq_examples: list[dict] = []
    for record in claims:
        evidence = record.get("evidence") or {}
        if not evidence:
            no_evidence += 1
            continue
        if len(evidence) > 1:
            multi_doc += 1
            continue
        doc_id, entries = next(iter(evidence.items()))
        labels = {entry["label"] for entry in entries}
        if len(labels) > 1:
            mixed += 1
            continue
        label = labels.pop()
        if int(doc_id) not in corpus:
            missing_doc += 1
            continue
        abstract = corpus[int(doc_id)]["abstract"]
        idxs = sorted({i for entry in entries for i in entry["sentences"]})
        if any(not (0 <= i < len(abstract)) for i in idxs):
            oob += 1
            continue
        sentences = [abstract[i] for i in idxs]
        normalized = [normalize_evidence_text(s) for s in sentences]
        if not all(is_well_formed(s) for s in normalized):
            malformed += 1
            continue
        block = " ".join(normalized)
        if (not all(quote_pair_ok(s) for s in sentences)
                or block.count("(") != block.count(")")
                or _WIKI_RESIDUE.search(block)):
            text_quality += 1
            if len(tq_examples) < 8:
                tq_examples.append({"scifact_id": record["id"],
                                    "claim": record["claim"],
                                    "block": block[:220]})
            continue
        out.append({
            "source": "scifact",
            "scifact_id": record["id"],
            "split": record["_split"],
            "label": label,
            "direction": "increase" if label == "SUPPORT" else "decrease",
            "claim": nfc(record["claim"]),
            "evidence_sentences": sentences,
            "evidence_block": block,
            "cluster": nfc(doc_id),
            "evidence_doc_id": int(doc_id),
            "rationale_idxs": idxs,
        })
    diagnostics = {
        "claims_total": len(claims),
        "no_evidence": no_evidence,
        "multi_doc_excluded": multi_doc,
        "mixed_label_excluded": mixed,
        "missing_doc_excluded": missing_doc,
        "out_of_bounds_excluded": oob,
        "malformed_excluded": malformed,
        "text_quality_excluded": text_quality,
        "text_quality_examples": tq_examples,
        "records_emitted": len(out),
    }
    return out, diagnostics
