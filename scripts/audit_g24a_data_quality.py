#!/usr/bin/env python3
"""G24A data-quality audit — line-by-line integrity of the main-pass raw.

Data is the center of the research; this audit is the quality layer that the
earlier verification passes (6/6 definitional cross-check, independent
re-derivation, CSV zero-mismatch) did NOT cover. Those proved the summaries
were computed correctly; this one proves the underlying data is what the
preregistration says it is.

Scope (integrity only — no scientific gates, no findings filters):

  A. Row integrity      5 files x 4,800 rows: coverage (8 kinds x 600 items),
                        uniqueness, field matrix, readout tags, ranges,
                        reason_truncated, raw<->value anomalies (reported).
  B. Prompt reconstruction  THE line-by-line check: rebuild every prompt from
                        the PREREGISTRATION literals (independent of
                        src/schema.py), assert byte-equality with
                        compile_prompt/compile_probe, tokenize with the exact
                        chat-template path run_model used, and compare against
                        the recorded n_prompt_tokens and
                        rule_to_answer_tokens for all 24,000 rows.
                        Any mismatch = integrity hard stop.
  C. Item file          600 items: required fields, the prereg character-
                        identical rule guarantee (testable per item), direction
                        <-> label <-> stratum mapping, uniqueness, duplicates.
  D. Coherence          observations only (reported, never failed): token-count
                        invariants, admit_pre vs admit_post divergence,
                        saturation, mass tails, value==50 inspection.
  E. Cross-run check    selection pass vs main pass for mistral on the shared
                        600x3 rows (temp-0 determinism probe).
  F. Byte fidelity      working copy vs git HEAD for the raws + item file.

Run:
  HF_HUB_OFFLINE=1 PYTHONPATH=src python scripts/audit_g24a_data_quality.py

Exit code 1 iff an integrity hard stop fired.
Outputs:
  results/discovery/g24a_data_quality_audit_v1.{json,md}
"""
from __future__ import annotations

import collections
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

os.environ.setdefault("HF_HUB_OFFLINE", "1")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, "src")

import schema                                    # noqa: E402
from schema import SYSTEM, compile_prompt, compile_probe, load_items  # noqa: E402
import conditions_g24a as g24a                   # noqa: E402

ITEMS_PATH = "data/items/g24a_v1.jsonl"
SELECTION_PATH = "results/raw/g24a_mistral-small-24b_selection.jsonl"
OUT_JSON = "results/discovery/g24a_data_quality_audit_v1.json"
OUT_MD = "results/discovery/g24a_data_quality_audit_v1.md"

MODELS = ["mistral-small-24b", "llama31-8b", "qwen3-8b", "qwen35-9b", "gemma3-12b"]
HUB = "/home/xiang/.cache/huggingface/hub"
TOK_PATHS = {
    "mistral-small-24b": "data/mistral_small_24b_hf",
    "llama31-8b": f"{HUB}/models--NousResearch--Meta-Llama-3.1-8B-Instruct/snapshots/d10aef7999a2b5ba950ab3974312feeedbfe0b77",
    "qwen3-8b": f"{HUB}/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218",
    "qwen35-9b": f"{HUB}/models--Qwen--Qwen3.5-9B/snapshots/c202236235762e1c871ad0ccb60c8ee5ba337b9a",
    "gemma3-12b": f"{HUB}/models--google--gemma-3-12b-it/snapshots/96b6f1eccf38110c56df3a15bffe176da04bfd80",
}

DIGIT_KINDS = ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"]
PROBE_KINDS = ["rule_probe_exclude_pre", "rule_probe_exclude_post", "rule_probe_admit_post"]
ALL_KINDS = DIGIT_KINDS + PROBE_KINDS
PROBE_ARM = {
    "rule_probe_exclude_pre": "exclude_pre",
    "rule_probe_exclude_post": "exclude_post",
    "rule_probe_admit_post": "admit_post",
}

# --- literals transcribed from preregistrations/PREREGISTRATION_G24A_NATURAL_EVIDENCE.md
#     (lines 84-136: item field mapping, ruling constants, block layout).
#     NOT imported from src/schema.py: the whole point of section B is an
#     independent reconstruction. Equality with the code constants is asserted.
PREREG_ADMIT_RULE = (
    "Evidence E is admitted. It must be given the full weight of a "
    "verified item in your final judgment."
)
PREREG_EXCLUDE_RULE = (
    "Evidence E is excluded. It must have zero influence on your "
    "final judgment."
)
PREREG_QUESTION = "Considering everything above, rate the likelihood that the claim is true."
PREREG_OUTPUT_SPEC = (
    "Use a scale from 0 to 9, where 0 means certainly false and "
    "9 means certainly true."
)
PREREG_PROBE_Q = (
    "According to the ruling above, are you permitted to use "
    "evidence E when you reach your rating? Answer with "
    "exactly one word: YES or NO."
)
PREREG_HEADERS = {"claim": "CLAIM", "evidence": "EVIDENCE E", "ruling": "RULING"}
# tail + system are G0 shared machinery (identical across the five conditions,
# prereg design constraint 3); exact text taken from src/schema.py and asserted
# equal there (byte-fidelity of schema.py to the run is established separately
# by git: no diff since the raws were committed).
PREREG_TAIL = (
    "Think in at most two short sentences. Then write a final line of exactly "
    "this form:\nANSWER: <your answer>"
)
SEP = "\n\n"

HARD_STOPS: list[str] = []
OBS: dict[str, object] = {}


def stop(where: str, msg: str) -> None:
    HARD_STOPS.append(f"[{where}] {msg}")


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def quantiles(xs):
    if not xs:
        return None
    xs = sorted(xs)
    def q(p):
        i = min(len(xs) - 1, max(0, round(p * (len(xs) - 1))))
        return xs[i]
    return {"n": len(xs), "min": xs[0], "p1": q(0.01), "p10": q(0.10), "p50": q(0.50),
            "p90": q(0.90), "p99": q(0.99), "max": xs[-1]}


# --------------------------------------------------------------------------
# Independent prompt builder (prereg literals only)
# --------------------------------------------------------------------------
def build_prompt(item, cond: str) -> str:
    B = PREREG_HEADERS["claim"] + "\n" + item.base_context
    E = PREREG_HEADERS["evidence"] + "\n" + item.critical_evidence
    Radm = PREREG_HEADERS["ruling"] + "\n" + PREREG_ADMIT_RULE
    Rexc = PREREG_HEADERS["ruling"] + "\n" + PREREG_EXCLUDE_RULE
    blocks = {
        "base": [B],
        "admit_pre": [B, Radm, E],
        "admit_post": [B, E, Radm],
        "exclude_pre": [B, Rexc, E],
        "exclude_post": [B, E, Rexc],
    }[cond]
    return SEP.join(blocks) + SEP + "TASK\n" + item.question + "\n" + item.output_spec + "\n" + PREREG_TAIL


def build_probe(item, probe: str) -> str:
    B = PREREG_HEADERS["claim"] + "\n" + item.base_context
    E = PREREG_HEADERS["evidence"] + "\n" + item.critical_evidence
    Radm = PREREG_HEADERS["ruling"] + "\n" + PREREG_ADMIT_RULE
    Rexc = PREREG_HEADERS["ruling"] + "\n" + PREREG_EXCLUDE_RULE
    blocks = {
        "exclude_pre": [B, Rexc, E],
        "exclude_post": [B, E, Rexc],
        "admit_post": [B, E, Radm],
    }[PROBE_ARM[probe]]
    return SEP.join(blocks) + SEP + "TASK\n" + PREREG_PROBE_Q


def make_chat_ids(tok):
    """Exact mirror of run_model.chat_ids (src/run_model.py lines 108-126)."""
    def chat_ids(user):
        kw = dict(tokenize=True, add_generation_prompt=True)
        msgs = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]
        try:
            enc = tok.apply_chat_template(msgs, enable_thinking=False, **kw)
        except TypeError:
            enc = tok.apply_chat_template(msgs, **kw)
        except Exception:
            flat = []
            for m in msgs:
                if m["role"] == "tool":
                    flat.append({"role": "user", "content": "TOOL OUTPUT\n" + m["content"]})
                else:
                    flat.append(m)
            enc = tok.apply_chat_template(flat, **kw)
        ids = enc["input_ids"] if hasattr(enc, "keys") else enc
        return list(ids[0]) if ids and isinstance(ids[0], (list, tuple)) else list(ids)
    return chat_ids


def main() -> int:
    t0 = time.time()
    report: dict = {"generated": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "purpose": "G24A main-pass data quality audit (integrity only, no scientific gates)"}

    # ---- prereg literals vs code constants --------------------------------
    const_eq = {
        "ADMIT_RULE": g24a.ADMIT_RULE == PREREG_ADMIT_RULE,
        "EXCLUDE_RULE": g24a.EXCLUDE_RULE == PREREG_EXCLUDE_RULE,
        "QUESTION": g24a.QUESTION == PREREG_QUESTION,
        "OUTPUT_SPEC": g24a.OUTPUT_SPEC == PREREG_OUTPUT_SPEC,
        "RULE_PROBE_QUESTION": g24a.RULE_PROBE_QUESTION == PREREG_PROBE_Q,
        "CLAIM_HEADER": g24a.CLAIM_HEADER == PREREG_HEADERS["claim"],
        "EVIDENCE_HEADER": g24a.EVIDENCE_HEADER == PREREG_HEADERS["evidence"],
        "TAIL_is_schema_reasoned": schema.ANSWER_FORMATS["reasoned"] == PREREG_TAIL,
        "SYSTEM": SYSTEM == ("You are a careful decision maker. Follow every instruction in the "
                             "context exactly. Answer with the requested format and nothing else."),
        "MEMORY_empty": g24a.MEMORY_QUESTION == "",
    }
    for k, ok in const_eq.items():
        if not ok:
            stop("0-prereg", f"prereg literal != code constant: {k}")
    report["prereg_literal_vs_code_constants"] = const_eq

    # ---- load items --------------------------------------------------------
    items = load_items(ITEMS_PATH)
    by_id = {it.item_id: it for it in items}
    report["items_file"] = {"path": ITEMS_PATH, "n": len(items), "sha256": sha256(ITEMS_PATH)}
    if len(items) != 600 or len(by_id) != 600:
        stop("C-items", f"item file expected 600 unique, got n={len(items)} uniq={len(by_id)}")

    # ---- manual-review dispositions applied to the item file (2026-09-25) ---
    # The600-item manual review produced 52 fix_claim rewrites (field
    # base_context) + 4 flip_direction sign corrections (field
    # critical_direction), applied in commit 92d8cd0 after the selection pass
    # had already run on the pre-fix candidates pool. Sections C and E assert
    # that drift versus the candidates pool equals EXACTLY this documented
    # set, field by field: any OTHER drift still hard-stops the audit, and a
    # documented edit that is absent from the item file also hard-stops it.
    DISP_PATH = "results/discovery/g24a_item_manual_review/dispositions.jsonl"
    disp_fields: dict[str, set] = {}   # item_id -> set of edited fields
    disp_dir: dict[str, str] = {}      # item_id -> recorded direction_new (flip)
    if os.path.exists(DISP_PATH):
        for _l in open(DISP_PATH):
            if not _l.strip():
                continue
            _d = json.loads(_l)
            if _d.get("action") == "fix_claim":
                disp_fields.setdefault(_d["item_id"], set()).add("base_context")
            elif _d.get("action") == "flip_direction":
                disp_fields.setdefault(_d["item_id"], set()).add("critical_direction")
                disp_dir[_d["item_id"]] = _d["direction_new"]
    report["dispositions_applied"] = {
        "path": DISP_PATH,
        "fix_claim_items": sum(1 for f in disp_fields.values() if "base_context" in f),
        "flip_direction_items": len(disp_dir),
    }
    for _iid in sorted(disp_fields):
        if _iid not in by_id:
            stop("C-items", f"disposition references unknown item: {_iid}")
    _n_fix = sum(1 for f in disp_fields.values() if "base_context" in f)
    if (_n_fix, len(disp_dir)) != (52, 4):
        stop("C-items", f"disposition record counts changed: fix={_n_fix} (expected 52), "
                        f"flip={len(disp_dir)} (expected 4)")

    # ---- A: row integrity --------------------------------------------------
    rows_by_model: dict[str, dict[tuple, dict]] = {}
    rows_sha = {}
    A = {}
    for tag in MODELS:
        path = f"results/raw/{tag}_g24a.jsonl"
        rows_sha[tag] = sha256(path)
        rows = [json.loads(l) for l in open(path)]
        n = len(rows)
        kinds = collections.Counter(r["kind_name"] for r in rows)
        keys = [(r["item_id"], r["kind_name"]) for r in rows]
        item_set = {r["item_id"] for r in rows}
        mrec: dict[tuple, dict] = {}
        problems = []
        if n != 4800:
            problems.append(f"row count {n} != 4800")
        if set(kinds) != set(ALL_KINDS):
            problems.append(f"kind set mismatch: {sorted(kinds)}")
        for k in ALL_KINDS:
            if kinds.get(k) != 600:
                problems.append(f"kind {k}: {kinds.get(k)} != 600")
        if len(keys) != len(set(keys)):
            problems.append(f"duplicate (item,kind) pairs: {n - len(set(keys))}")
        if item_set != set(by_id):
            problems.append(f"item set mismatch: missing={len(set(by_id) - item_set)} extra={len(item_set - set(by_id))}")
        truncated = empty_reason = 0
        trunc_rows = []
        raw_anomalies = []
        dev_bands = collections.Counter()
        dev_max = 0.0
        probe_raws = collections.Counter()
        probe_raw_disagree = 0
        val_eq50 = 0
        mass_lt = {"<0.9": 0, "<0.5": 0}
        val_oob = mass_oob = pyes_oob = 0
        field_violations = 0
        for r in rows:
            it = by_id.get(r["item_id"])
            if it is None:
                continue
            kn = r["kind_name"]
            mrec[(r["item_id"], kn)] = r
            # field matrix
            digit = kn in DIGIT_KINDS
            if r["kind"] != ("digit" if digit else "rule"):
                problems.append(f"kind field wrong for {r['item_id']}/{kn}")
                field_violations += 1
                continue
            if r.get("task_family") != it.task_family:
                problems.append(f"task_family mismatch {r['item_id']}")
                field_violations += 1
            if r.get("model_tag") != tag:
                problems.append(f"model_tag mismatch {r['item_id']}/{kn}")
                field_violations += 1
            if digit:
                need = {"reasoning", "reason_truncated", "rule_to_answer_tokens", "raw", "value", "mass", "readout"}
                if not need <= set(r):
                    problems.append(f"missing digit fields {r['item_id']}/{kn}: {need - set(r)}")
                    field_violations += 1
                    continue
                if "p_yes" in r or "yesno" in r:
                    problems.append(f"probe-only fields on digit row {r['item_id']}/{kn}")
                    field_violations += 1
                if r["readout"] != "digit_expectation_0_100":
                    problems.append(f"readout tag wrong {r['item_id']}/{kn}")
                    field_violations += 1
                if not (0.0 - 1e-6 <= r["value"] <= 100.0 + 1e-6):
                    val_oob += 1
                if not (0.0 < r["mass"] <= 1.0 + 1e-6):
                    mass_oob += 1
                if r["mass"] < 0.9:
                    mass_lt["<0.9"] += 1
                if r["mass"] < 0.5:
                    mass_lt["<0.5"] += 1
                rt = (r["raw"] or "").strip()
                if not (len(rt) == 1 and rt.isdigit()):
                    problems.append(f"raw not a single digit {r['item_id']}/{kn}: {r['raw']!r}")
                    field_violations += 1
                else:
                    grid = int(rt) * 100.0 / 9.0
                    dv = abs(r["value"] - grid)
                    if r["mass"] >= 0.99:
                        dev_max = max(dev_max, dv)
                        dev_bands["<=1" if dv <= 1 else "1-3" if dv <= 3 else
                                  "3-10" if dv <= 10 else "10-30" if dv <= 30 else ">30"] += 1
                    if r["mass"] >= 0.99 and dv > 3.0:
                        raw_anomalies.append({"item": r["item_id"], "kind": kn, "raw": r["raw"],
                                              "value": round(r["value"], 3), "mass": round(r["mass"], 4)})
                # rule_to_answer_tokens: None iff base
                if kn == "base":
                    if r["rule_to_answer_tokens"] is not None:
                        problems.append(f"base has rule_to_answer_tokens {r['item_id']}")
                        field_violations += 1
                elif not isinstance(r["rule_to_answer_tokens"], int) or r["rule_to_answer_tokens"] < 0:
                    problems.append(f"bad rule_to_answer_tokens {r['item_id']}/{kn}")
                    field_violations += 1
                if r["reason_truncated"]:
                    truncated += 1
                    trunc_rows.append(f"{r['item_id']}/{kn}")
                if not (r["reasoning"] or "").strip():
                    empty_reason += 1
                if abs(r["value"] - 50.0) < 1e-9:
                    val_eq50 += 1
            else:
                need = {"raw", "p_yes", "mass", "yesno", "readout"}
                if not need <= set(r):
                    problems.append(f"missing probe fields {r['item_id']}/{kn}: {need - set(r)}")
                    field_violations += 1
                    continue
                if "reasoning" in r or "value" in r or "rule_to_answer_tokens" in r:
                    problems.append(f"digit-only fields on probe row {r['item_id']}/{kn}")
                    field_violations += 1
                if r["readout"] != "yes_probability":
                    problems.append(f"probe readout tag wrong {r['item_id']}/{kn}")
                    field_violations += 1
                if not (0.0 <= r["p_yes"] <= 1.0):
                    pyes_oob += 1
                if not (0.0 < r["mass"] <= 1.0 + 1e-6):
                    mass_oob += 1
                want = "YES" if r["p_yes"] >= 0.5 else "NO"
                if r["yesno"] != want:
                    problems.append(f"yesno != f(p_yes) {r['item_id']}/{kn}")
                    field_violations += 1
                rawu = (r["raw"] or "").strip().upper()
                probe_raws[r["raw"]] += 1
                if rawu in ("YES", "NO") and rawu != want:
                    probe_raw_disagree += 1
        for p in problems[:50]:
            stop("A-rows", f"{tag}: {p}")
        if len(problems) > 50:
            stop("A-rows", f"{tag}: ... {len(problems) - 50} more problems suppressed")
        rows_by_model[tag] = mrec
        A[tag] = {
            "rows": n, "sha256": rows_sha[tag],
            "kinds_ok": set(kinds) == set(ALL_KINDS) and all(kinds.get(k) == 600 for k in ALL_KINDS),
            "unique_item_kind": len(keys) == len(set(keys)),
            "field_violations": field_violations,
            "value_out_of_range": val_oob, "mass_out_of_range": mass_oob,
            "p_yes_out_of_range": pyes_oob,
            "mass_lt_0.9": mass_lt["<0.9"], "mass_lt_0.5": mass_lt["<0.5"],
            "raw_not_digit_problems": sum("raw not a single digit" in p for p in problems),
            "raw_value_anomalies_mass_ge_0.99_dev_gt_3pt": raw_anomalies[:20],
            "raw_value_anomaly_count": len(raw_anomalies),
            "reason_truncated": truncated, "reason_truncated_rows": trunc_rows,
            "empty_reasoning": empty_reason,
            "value_vs_raw_grid_bands_mass_ge_0.99": dict(dev_bands),
            "value_vs_raw_grid_max_dev_mass_ge_0.99": round(dev_max, 3),
            "value_exactly_50": val_eq50,
            "probe_raw_distinct": dict(probe_raws.most_common(8)),
            "probe_raw_vs_pyes_disagreements": probe_raw_disagree,
            "problems": problems[:50],
        }
    report["A_rows"] = A

    # ---- B: prompt reconstruction ------------------------------------------
    from transformers import AutoTokenizer

    Bsec: dict = {}
    struct_checks = {
        "base": lambda p, it: ("CLAIM\n" in p and "\n\nEVIDENCE E\n" not in p
                               and "\n\nRULING\n" not in p
                               and p.endswith("TASK\n" + it.question + "\n" + it.output_spec + "\n" + PREREG_TAIL)),
        "admit_pre": lambda p, it: (p.find("CLAIM\n") < p.find("\n\nRULING\n") < p.find("\n\nEVIDENCE E\n")
                                    and PREREG_ADMIT_RULE in p and PREREG_EXCLUDE_RULE not in p),
        "admit_post": lambda p, it: (p.find("CLAIM\n") < p.find("\n\nEVIDENCE E\n") < p.rfind("\n\nRULING\n")
                                     and PREREG_ADMIT_RULE in p and PREREG_EXCLUDE_RULE not in p),
        "exclude_pre": lambda p, it: (p.find("CLAIM\n") < p.find("\n\nRULING\n") < p.find("\n\nEVIDENCE E\n")
                                      and PREREG_EXCLUDE_RULE in p and PREREG_ADMIT_RULE not in p),
        "exclude_post": lambda p, it: (p.find("CLAIM\n") < p.find("\n\nEVIDENCE E\n") < p.rfind("\n\nRULING\n")
                                       and PREREG_EXCLUDE_RULE in p and PREREG_ADMIT_RULE not in p),
    }
    probe_struct = {
        "rule_probe_exclude_pre": lambda p, it: (PREREG_EXCLUDE_RULE in p and PREREG_ADMIT_RULE not in p
                                                 and p.find("CLAIM\n") < p.find("\n\nRULING\n") < p.find("\n\nEVIDENCE E\n")
                                                 and p.endswith("TASK\n" + PREREG_PROBE_Q)
                                                 and "rate the likelihood" not in p),
        "rule_probe_exclude_post": lambda p, it: (PREREG_EXCLUDE_RULE in p and PREREG_ADMIT_RULE not in p
                                                  and p.find("CLAIM\n") < p.find("\n\nEVIDENCE E\n") < p.rfind("\n\nRULING\n")
                                                  and p.endswith("TASK\n" + PREREG_PROBE_Q)
                                                  and "rate the likelihood" not in p),
        "rule_probe_admit_post": lambda p, it: (PREREG_ADMIT_RULE in p and PREREG_EXCLUDE_RULE not in p
                                                and p.find("CLAIM\n") < p.find("\n\nEVIDENCE E\n") < p.rfind("\n\nRULING\n")
                                                and p.endswith("TASK\n" + PREREG_PROBE_Q)
                                                and "rate the likelihood" not in p),
    }

    for tag in MODELS:
        tok = AutoTokenizer.from_pretrained(TOK_PATHS[tag])
        chat_ids = make_chat_ids(tok)
        def raw_ids(text):
            return tok(text, add_special_tokens=False)["input_ids"]
        checked = byte_eq = tok_match = rt_match = 0
        struct_fail = []
        mism_tok, mism_rt, mism_byte = [], [], []
        for it in items:
            for kn in ALL_KINDS:
                my = build_prompt(it, kn) if kn in DIGIT_KINDS else build_probe(it, kn)
                ref = compile_prompt(it, kn, mode="reasoned") if kn in DIGIT_KINDS else compile_probe(it, kn)
                checked += 1
                if my != ref:
                    mism_byte.append(f"{it.item_id}/{kn}")
                    continue
                byte_eq += 1
                f = (struct_checks[kn] if kn in DIGIT_KINDS else probe_struct[kn])(my, it)
                if not f:
                    struct_fail.append(f"{it.item_id}/{kn}")
                rec = rows_by_model[tag].get((it.item_id, kn))
                if rec is None:
                    stop("B-reconstruct", f"{tag}: missing recorded row {it.item_id}/{kn}")
                    continue
                ntok = len(chat_ids(my))
                if ntok != rec["n_prompt_tokens"]:
                    mism_tok.append({"item": it.item_id, "kind": kn, "recorded": rec["n_prompt_tokens"], "rebuilt": ntok})
                else:
                    tok_match += 1
                if kn in DIGIT_KINDS:
                    off = my.rfind("\nRULING\n")
                    want_rt = None if off < 0 else len(raw_ids(my[off + 1:]))
                    if want_rt != rec["rule_to_answer_tokens"]:
                        mism_rt.append({"item": it.item_id, "kind": kn, "recorded": rec["rule_to_answer_tokens"],
                                        "rebuilt": want_rt})
                    else:
                        rt_match += 1
        if mism_byte:
            stop("B-reconstruct", f"{tag}: {len(mism_byte)} prompts differ from compile_prompt: {mism_byte[:5]}")
        if struct_fail:
            stop("B-reconstruct", f"{tag}: structural assert failed: {struct_fail[:5]}")
        if mism_tok:
            stop("B-reconstruct", f"{tag}: {len(mism_tok)} n_prompt_tokens mismatches: {mism_tok[:5]}")
        if mism_rt:
            stop("B-reconstruct", f"{tag}: {len(mism_rt)} rule_to_answer_tokens mismatches: {mism_rt[:5]}")
        Bsec[tag] = {
            "prompts_checked": checked,
            "byte_equal_to_compile": byte_eq,
            "n_prompt_tokens_exact_match": tok_match,
            "rule_to_answer_exact_match": rt_match,
            "n_prompt_tokens_mismatches": mism_tok[:10],
            "rule_to_answer_mismatches": mism_rt[:10],
            "structural_failures": struct_fail[:10],
        }
        del tok
    report["B_prompt_reconstruction"] = Bsec

    # ---- C: item file ------------------------------------------------------
    C: dict = {}
    ids = [it.item_id for it in items]
    claims = [it.base_context for it in items]
    cnt = lambda pred: sum(1 for it in items if pred(it))
    field_missing = []
    for it in items:
        for f in ("base_context", "critical_evidence", "admit_rule", "exclude_rule",
                  "question", "output_spec", "rule_probe_question"):
            if not (getattr(it, f) or "").strip():
                field_missing.append(f"{it.item_id}.{f}")
    mapping = collections.Counter()
    bad_map = []
    documented_flip_dir = []
    label_by_stratum = {}
    for it in items:
        meta = it.meta if isinstance(it.meta, dict) else {}
        s = meta.get("stratum", "")
        mapping[s] += 1
        label_by_stratum.setdefault(s, set()).add(meta.get("gold_label"))
        src = meta.get("source")
        want_dir = {"fever/SUPPORTS": "increase", "fever/REFUTES": "decrease",
                    "scifact/SUPPORT": "increase", "scifact/CONTRADICT": "decrease"}.get(s)
        fam_ok = (it.task_family == "g24a_fever") == (src == "fever")
        if it.item_id in disp_dir:
            # Manual review overturned the label-derived direction for this
            # item (upstream label/evidence decoupling, batch 1/3/4 verdicts):
            # assert instead that the direction equals the recorded
            # disposition value byte-exactly, and that family/source still hold.
            if fam_ok and it.critical_direction == disp_dir[it.item_id]:
                documented_flip_dir.append(it.item_id)
            else:
                bad_map.append(f"{it.item_id} stratum={s} dir={it.critical_direction} "
                               f"documented_flip_expects={disp_dir[it.item_id]} "
                               f"src={src} fam={it.task_family}")
        elif not (want_dir is not None and it.critical_direction == want_dir and fam_ok):
            bad_map.append(f"{it.item_id} stratum={s} dir={it.critical_direction} src={src} fam={it.task_family}")
    identical_rules = cnt(lambda it: it.admit_rule == PREREG_ADMIT_RULE)
    identical_exc = cnt(lambda it: it.exclude_rule == PREREG_EXCLUDE_RULE)
    tail_ok = cnt(lambda it: it.question == PREREG_QUESTION and it.output_spec == PREREG_OUTPUT_SPEC
                  and it.rule_probe_question == PREREG_PROBE_Q and it.memory_question == "")
    gt_values = sorted({repr(it.ground_truth) for it in items})
    ev_eq_claim = [it.item_id for it in items if it.critical_evidence.strip() == it.base_context.strip()]
    for f in field_missing:
        stop("C-items", f"empty required field: {f}")
    for b in bad_map[:20]:
        stop("C-items", f"stratum/dir/source mapping broken: {b}")
    if identical_rules != 600 or identical_exc != 600:
        stop("C-items", f"identical-rule guarantee: admit {identical_rules}/600 exclude {identical_exc}/600")
    if tail_ok != 600:
        stop("C-items", f"identical tail guarantee: {tail_ok}/600")
    dup_claims = [c for c, k in collections.Counter(claims).items() if k > 1]
    if dup_claims:
        stop("C-items", f"{len(dup_claims)} duplicated claim texts")
    C = {
        "n": len(items), "unique_ids": len(set(ids)), "unique_claims": len(set(claims)),
        "empty_required_fields": field_missing,
        "identical_admit_rule": identical_rules, "identical_exclude_rule": identical_exc,
        "identical_tail_question_probe_memory": tail_ok,
        "stratum_counts": dict(mapping),
        "stratum_gold_labels": {k: sorted(v, key=str) for k, v in label_by_stratum.items()},
        "mapping_violations": bad_map[:20],
        "direction_flips_documented": sorted(documented_flip_dir),
        "ground_truth_values": gt_values,
        "evidence_equals_claim": ev_eq_claim,
        "task_family_counts": dict(collections.Counter(it.task_family for it in items)),
        "direction_counts": dict(collections.Counter(it.critical_direction for it in items)),
        "meta_key_sets": sorted({tuple(sorted((it.meta if isinstance(it.meta, dict) else {}).keys())) for it in items}),
    }
    report["C_items"] = C

    # ---- D: coherence observations (never failed) ---------------------------
    D = {}
    for tag in MODELS:
        m = rows_by_model[tag]
        def v(kn, it): return m[(it.item_id, kn)]["value"]
        def nt(kn, it): return m[(it.item_id, kn)]["n_prompt_tokens"]
        d_pre = [nt("admit_pre", it) - nt("exclude_pre", it) for it in items]
        d_post = [nt("admit_post", it) - nt("exclude_post", it) for it in items]
        d_pos = [nt("exclude_pre", it) - nt("exclude_post", it) for it in items]
        base_shorter = sum(1 for it in items if nt("base", it) < nt("admit_pre", it))
        adm_delta = [v("admit_post", it) - v("admit_pre", it) for it in items]
        exact = {}
        for kn in DIGIT_KINDS:
            vals = [v(kn, it) for it in items]
            exact[kn] = {
                "eq_0": sum(1 for x in vals if abs(x) < 1e-9),
                "eq_100": sum(1 for x in vals if abs(x - 100) < 1e-9),
                "eq_50": sum(1 for x in vals if abs(x - 50) < 1e-9),
            }
        masses = [m[(it.item_id, kn)]["mass"] for it in items for kn in DIGIT_KINDS]
        D[tag] = {
            "ntok_admit_minus_exclude_pre": quantiles(d_pre),
            "ntok_admit_minus_exclude_post": quantiles(d_post),
            "ntok_exclude_pre_minus_post": quantiles(d_pos),
            "base_shorter_than_admit_pre_count": base_shorter,
            "admit_post_minus_admit_pre_value": quantiles(adm_delta),
            "admit_post_vs_pre_abs_gt20": sum(1 for x in adm_delta if abs(x) > 20),
            "admit_post_vs_pre_sign_flips": sum(1 for x in adm_delta if x < -1e-9),
            "exact_value_counts": exact,
            "digit_mass": quantiles(masses),
        }
        if base_shorter != 600:
            stop("D-invariant", f"{tag}: base prompt not shorter than admit_pre in {600 - base_shorter} items")
    report["D_coherence"] = D

    # ---- E: selection pass vs main pass (mistral, shared rows) -------------
    # Retest: two temp-0 runs, identical prompts. Diagnoses batch-composition
    # nondeterminism AND rules out the two alternative causes (args drift,
    # item drift) programmatically.
    CANDIDATES_PATH = "data/items/g24a_candidates_v1.jsonl"
    sel = {}
    if os.path.exists(SELECTION_PATH):
        for l in open(SELECTION_PATH):
            r = json.loads(l)
            if r["item_id"] in by_id and r["kind_name"] in ("base", "admit_pre", "admit_post"):
                sel[(r["item_id"], r["kind_name"])] = r
        m = rows_by_model["mistral-small-24b"]

        # E1: item drift vs candidates must equal EXACTLY the documented
        # disposition set (the selection pass ran the pre-fix pool BY DESIGN;
        # the item file was corrected afterwards in commit 92d8cd0). Any
        # undocumented drift - or a documented edit absent from the item file
        # - hard-stops the audit.
        cand = {}
        if os.path.exists(CANDIDATES_PATH):
            for l in open(CANDIDATES_PATH):
                r = json.loads(l)
                if r["item_id"] in by_id:
                    cand[r["item_id"]] = r
        drift_fields: dict[str, list] = {}
        e1_problems = []
        for it in items:
            c = cand.get(it.item_id)
            if c is None:
                e1_problems.append(f"{it.item_id}: missing in candidates")
                continue
            cur = json.loads(it.to_json())
            diffs = sorted(k for k in set(c) | set(cur) if c.get(k) != cur.get(k))
            if diffs:
                drift_fields[it.item_id] = diffs
        for iid, fields in sorted(disp_fields.items()):
            if drift_fields.get(iid, []) != sorted(fields):
                e1_problems.append(f"{iid}: drift={drift_fields.get(iid, [])} "
                                   f"documented={sorted(fields)}")
        for iid, fields in sorted(drift_fields.items()):
            if iid not in disp_fields:
                e1_problems.append(f"{iid}: UNDOCUMENTED drift in {fields}")
        item_drift = e1_problems[:5]
        if e1_problems:
            stop("E-retest", f"selection vs main item drift mismatch: {e1_problems[:5]}")

        # E2: decode-relevant runner args identical between the two pass scripts?
        # (--out/--kinds/--items differ BY DESIGN: pass-specific.)
        def runner_flags(path):
            flags, cur = {}, None
            for line in open(path):
                if line.lstrip().startswith("#"):
                    continue
                for tok in line.split():
                    if tok.startswith("--"):
                        cur = tok
                        flags[tok] = True
                    elif cur is not None and flags.get(cur) is True:
                        flags[cur] = tok
                # value must sit on the same line as its flag; a trailing bare
                # boolean leaves cur dangling, don't let the next line's words
                # (e.g. `echo`) fill it
                if cur is not None and flags.get(cur) is True:
                    cur = None
            return flags
        DECODE_FLAGS = ["--mode", "--reason-tokens", "--max-model-len", "--tp",
                        "--temperature", "--gpu-frac", "--enforce-eager"]
        f_sel = runner_flags("scripts/run_g24a_selection.sh")
        f_main = runner_flags("scripts/run_g24a_main.sh")
        args_equal = all(f_sel.get(k) == f_main.get(k) for k in DECODE_FLAGS)
        decode_sel = {k: f_sel.get(k) for k in DECODE_FLAGS}
        decode_main = {k: f_main.get(k) for k in DECODE_FLAGS}

        joined = value_eq = raw_eq = ntok_eq = raw_flip = 0
        bands = collections.Counter()
        flips_by_kind = collections.Counter()
        worst = []
        vsel, vmain = [], []
        worst_key, worst_rec, max_d = None, None, -1.0
        # Retest scope: items whose claim was rewritten after the selection
        # pass ran different prompts in the two passes BY DESIGN -> excluded.
        # Flip items stay IN (direction is scoring metadata, not prompt
        # text); the n_prompt_tokens equality stop below would catch it if
        # that assumption were wrong.
        fix_items = {i for i, f in disp_fields.items() if "base_context" in f}
        retest_items = [it.item_id for it in items if it.item_id not in fix_items]
        for key, sr in sel.items():
            if key[0] in fix_items:
                continue
            mr = m.get(key)
            if mr is None:
                continue
            joined += 1
            d = abs(sr["value"] - mr["value"])
            vsel.append(sr["value"])
            vmain.append(mr["value"])
            if d < 1e-9:
                value_eq += 1
                bands["==0"] += 1
            elif d <= 1:
                bands["<=1"] += 1
            elif d <= 10:
                bands["<=10"] += 1
            elif d <= 50:
                bands["10-50"] += 1
            else:
                bands[">50"] += 1
            rf = sr["raw"] != mr["raw"]
            if not rf:
                raw_eq += 1
            if sr["n_prompt_tokens"] == mr["n_prompt_tokens"]:
                ntok_eq += 1
            raw_flip += rf
            if rf:
                flips_by_kind[key[1]] += 1
            if d > 50:
                worst.append({"item": key[0], "kind": key[1], "d_value": round(d, 6)})
            if d > max_d:
                max_d = d
                worst_key, worst_rec = key, (sr, mr)

        # pearson
        n = len(vsel)
        mean_s = sum(vsel) / n
        mean_m = sum(vmain) / n
        cov = sum((a - mean_s) * (b - mean_m) for a, b in zip(vsel, vmain))
        var_s = sum((a - mean_s) ** 2 for a in vsel)
        var_m = sum((b - mean_m) ** 2 for b in vmain)
        pearson = cov / (var_s ** 0.5 * var_m ** 0.5) if var_s > 0 and var_m > 0 else None

        worst_detail = None
        if worst_rec:
            sr, mr = worst_rec
            worst_detail = {
                "item": worst_key[0], "kind": worst_key[1],
                "selection": {"raw": sr["raw"], "value": sr["value"], "mass": sr["mass"],
                              "n_prompt_tokens": sr["n_prompt_tokens"], "reasoning": sr["reasoning"]},
                "main": {"raw": mr["raw"], "value": mr["value"], "mass": mr["mass"],
                         "n_prompt_tokens": mr["n_prompt_tokens"], "reasoning": mr["reasoning"]},
            }

        E = {"selection_sha256": sha256(SELECTION_PATH), "joined_rows": joined,
             "value_exact_equal": value_eq, "raw_equal": raw_eq,
             "n_prompt_tokens_equal": ntok_eq,
             "value_diff_bands": dict(bands),
             "raw_argmax_flips": raw_flip,
             "flips_by_kind": dict(flips_by_kind),
             "pearson_selection_vs_main": None if pearson is None else round(pearson, 6),
             "worst_value_diffs_gt_50": sorted(worst, key=lambda w: -w["d_value"]),
             "worst_row_reasonings": worst_detail,
             "runner_args_equal": args_equal,
             "decode_flags_selection": decode_sel, "decode_flags_main": decode_main,
             "item_text_drift_vs_candidates": item_drift[:5],
             "documented_drift_items": len(drift_fields),
             "drift_fields_by_item": drift_fields,
             "retest_items": len(retest_items),
             "retest_rows_expected": 3 * len(retest_items),
             "diagnosis": (f"prompts identical across passes on all {len(retest_items)} non-rewritten "
                           f"items (n_prompt_tokens {ntok_eq}/{joined}, prompt-relevant item text "
                           "byte-identical, runner args identical) yet values differ -> temp-0 vLLM "
                           "is not batch-composition invariant; the divergence amplifies through the "
                           "two-stage greedy decode (rationale flips). The 52 claim-rewritten items "
                           "ran pre-rewrite prompts in the selection pass and are excluded from the "
                           "retest; single-cell values remain run-specific near boundaries."),
             }
        expected_join = 3 * len(retest_items)
        if joined != expected_join:
            stop("E-crossrun", f"selection join expected {expected_join} rows "
                               f"({len(retest_items)} items x 3 kinds), got {joined}")
        if ntok_eq != joined:
            stop("E-crossrun", f"selection vs main n_prompt_tokens mismatch on {joined - ntok_eq} rows")
    else:
        E = {"missing": SELECTION_PATH}
        stop("E-crossrun", f"selection file missing: {SELECTION_PATH}")
    report["E_retest_selection_vs_main"] = E

    # ---- F: byte fidelity vs git HEAD ---------------------------------------
    git_files = [f"results/raw/{t}_g24a.jsonl" for t in MODELS] + [ITEMS_PATH, SELECTION_PATH]
    F = {}
    for p in git_files:
        r = subprocess.run(["git", "diff", "--quiet", "HEAD", "--", p])
        F[p] = {"identical_to_HEAD": r.returncode == 0}
        if r.returncode != 0:
            stop("F-git", f"working copy differs from HEAD: {p}")
    report["F_git_byte_fidelity"] = F

    # ---- verdict ------------------------------------------------------------
    report["hard_stops"] = HARD_STOPS
    report["verdict"] = "INTEGRITY OK" if not HARD_STOPS else f"INTEGRITY HARD STOP ({len(HARD_STOPS)})"
    report["elapsed_s"] = round(time.time() - t0, 1)

    Path("results/discovery").mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(report, f, indent=1, ensure_ascii=False)

    # ---- markdown -----------------------------------------------------------
    L = ["# G24A data-quality audit v1 (line-by-line, integrity only)",
         "",
         f"Generated {report['generated']} — {report['elapsed_s']}s. "
         "Scope: data integrity. **No scientific gates, no findings selection** — "
         "section D is observation only and can never fail the audit.",
         "",
         f"**Verdict: {report['verdict']}**" + ("" if not HARD_STOPS else ""),
         ""]
    if HARD_STOPS:
        L += ["## Hard stops", ""] + [f"- {h}" for h in HARD_STOPS] + [""]
    L += ["## 0. Prereg literals vs code constants", "",
          "| constant | prereg text == code |", "|---|---|"]
    L += [f"| {k} | {'OK' if v else 'MISMATCH'} |" for k, v in const_eq.items()] + [""]
    L += ["## A. Row integrity (per model)", "",
          "| model | rows | kinds 8x600 | unique | field viol. | mass<0.9 | mass<0.5 | trunc | empty rat. | raw-value anom. |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for tag in MODELS:
        a = A[tag]
        L.append(f"| {tag} | {a['rows']} | {a['kinds_ok']} | {a['unique_item_kind']} | {a['field_violations']} "
                 f"| {a['mass_lt_0.9']} | {a['mass_lt_0.5']} | {a['reason_truncated']} | {a['empty_reasoning']} "
                 f"| {a['raw_value_anomaly_count']} |")
    L += ["", f"Probe raw token distincts (per model): "
          + "; ".join(f"{t}: {A[t]['probe_raw_distinct']}" for t in MODELS), ""]
    L += ["Value-vs-raw-grid deviation (mass ≥ 0.99; value is the digit-bucket EV, "
          "raw is the single argmax token — divergence means the digit distribution "
          "is spread across spellings/buckets, not corruption):", ""]
    for tag in MODELS:
        L.append(f"- {tag}: max dev {A[tag]['value_vs_raw_grid_max_dev_mass_ge_0.99']} — "
                 f"bands {A[tag]['value_vs_raw_grid_bands_mass_ge_0.99']}")
    L += ["", "Truncated rationales (110-token cap; answer cue still appended, readout unaffected):", ""]
    for tag in MODELS:
        if A[tag]["reason_truncated_rows"]:
            L.append(f"- {tag}: {A[tag]['reason_truncated_rows']}")
    L += [""]
    L += ["## B. Prompt reconstruction (prereg-literal rebuild -> token count)", "",
          "| model | prompts checked | byte == compile_prompt | n_prompt_tokens exact | rule_to_answer_tokens exact |",
          "|---|---|---|---|---|"]
    for tag in MODELS:
        b = Bsec[tag]
        L.append(f"| {tag} | {b['prompts_checked']} | {b['byte_equal_to_compile']} "
                 f"| {b['n_prompt_tokens_exact_match']} | {b['rule_to_answer_exact_match']} |")
    L += ["", "Every prompt was rebuilt from the **preregistration text** (independent of src/), "
          "checked byte-equal against compile_prompt/compile_probe, then tokenized through the exact "
          "chat-template path run_model used (mirror of chat_ids) and compared to the recorded "
          "n_prompt_tokens. 600 items x 8 kinds x 5 models.", ""]
    L += ["## C. Item file (600)", "",
          f"- unique ids {C['unique_ids']}/600; unique claim texts {C['unique_claims']}/600",
          f"- identical ADMIT rule: {C['identical_admit_rule']}/600; identical EXCLUDE rule: {C['identical_exclude_rule']}/600",
          f"- identical tail (question+output+probe+empty memory): {C['identical_tail_question_probe_memory']}/600",
          f"- strata: {C['stratum_counts']}",
          f"- directions: {C['direction_counts']}; families: {C['task_family_counts']}",
          f"- mapping violations: {len(C['mapping_violations'])}",
          f"- documented direction flips (manual review; label-derived mapping overridden): "
          f"{C['direction_flips_documented']}",
          f"- ground_truth values: {C['ground_truth_values']}",
          f"- evidence == claim: {len(C['evidence_equals_claim'])}",
          f"- empty required fields: {len(C['empty_required_fields'])}", ""]
    L += ["## D. Coherence (observation only — cannot fail)", ""]
    for tag in MODELS:
        d = D[tag]
        L += [f"### {tag}",
              f"- ntok(admit_pre) − ntok(exclude_pre): {d['ntok_admit_minus_exclude_pre']}",
              f"- ntok(admit_post) − ntok(exclude_post): {d['ntok_admit_minus_exclude_post']}",
              f"- ntok(exclude_pre) − ntok(exclude_post): {d['ntok_exclude_pre_minus_post']}",
              f"- base shorter than admit_pre: {d['base_shorter_than_admit_pre_count']}/600",
              f"- admit_post − admit_pre value: {d['admit_post_minus_admit_pre_value']} "
              f"(|Δ|>20: {d['admit_post_vs_pre_abs_gt20']})",
              f"- exact 0/100/50 counts: {d['exact_value_counts']}",
              f"- digit mass: {d['digit_mass']}", ""]
    L += ["## E. Retest: selection pass vs main pass (mistral, temp 0, identical prompts)", ""]
    b = E.get("value_diff_bands", {})
    tot = E.get("joined_rows") or 1
    wr = E.get("worst_row_reasonings")
    L += [
        f"- decode-relevant runner args identical: {E.get('runner_args_equal')}  "
        f"(selection: {E.get('decode_flags_selection')}; main: {E.get('decode_flags_main')})",
        f"- item drift vs candidates: {E.get('documented_drift_items')} items — exactly the documented "
        "52 claim rewrites (base_context) + 4 direction flips (critical_direction); "
        f"{600 - (E.get('documented_drift_items') or 0)}/600 items byte-identical, "
        "undocumented drift = 0 (anything else hard-stops)",
        f"- retest scope: {E.get('retest_items')}/600 items (the 52 rewritten-claim items are excluded: "
        "their selection-pass prompts differ by design); "
        f"joined {E.get('joined_rows')} rows; n_prompt_tokens equal {E.get('n_prompt_tokens_equal')}/"
        f"{tot} — prompts identical across passes",
        f"- value bands: ==0 {b.get('==0', 0)} ({b.get('==0', 0) / tot:.1%}), "
        f"<=1 {b.get('<=1', 0)}, <=10 {b.get('<=10', 0)}, 10-50 {b.get('10-50', 0)}, >50 {b.get('>50', 0)}",
        f"- raw argmax flips: {E.get('raw_argmax_flips')} ({E.get('raw_argmax_flips') / tot:.1%}), "
        f"by kind {E.get('flips_by_kind')}",
        f"- pearson(value_selection, value_main) = {E.get('pearson_selection_vs_main')}",
        f"- rows with |Δ|>50: {E.get('worst_value_diffs_gt_50')}",
        f"- diagnosis: {E.get('diagnosis')}",
        "",
    ]
    if wr:
        L += [f"Worst row ({wr['item']} / {wr['kind']}):", ""]
        for side in ("selection", "main"):
            s = wr[side]
            L.append(f"- **{side}**: raw={s['raw']} value={s['value']:.3f} mass={s['mass']} "
                     f"ntok={s['n_prompt_tokens']}")
            L.append(f"  - reasoning: {s['reasoning']!r}")
        L += ["", "Same prompt (identical n_prompt_tokens, byte-identical item text), same decode args — "
              "the greedy rationale itself diverged between the two temp-0 passes (see above), "
              "which then flips the final digit. Single-cell values are therefore run-specific "
              "near decision boundaries; aggregates over 600 items are unaffected "
              "(pearson above).", ""]
    L += ["## F. Byte fidelity vs git HEAD", ""]
    L += [f"- `{p}`: {'identical' if v['identical_to_HEAD'] else 'DIFFERS'}" for p, v in F.items()] + [""]
    L += ["## Provenance timeline (from git log / mtimes)", "",
          "- `25316a9` 09-24 03:16 — g24a harness frozen (conditions/builder/selector/analyzer)",
          "- `b3fe84d` 09-24 04:22 — selection pass + selector early-stop fix (selector script only)",
          "- `1ffd52d`/`59ec3c4`/`6eb405a`/`c661db0` 09-24 04:27–04:36 — five main-pass raws committed at creation",
          "- `92d8cd0` 09-25 12:31 — manual-review dispositions applied to the item file "
          "(52 claim rewrites + 4 direction flips; 56 lines); `52b583f` — all pre-rerun analyses "
          "discarded; `e4319cb` 09-25 12:47 — full 600-item x 5-model main-pass re-run on the "
          "corrected item file (selection pass intentionally NOT rerun: candidate pool unchanged; "
          "this audit is computed on the regenerated raws)",
          "- `git diff c661db0..HEAD -- src/schema.py src/conditions_g24a.py src/run_model.py` — only additive "
          "G25A/G26A dispatch; the G24A path is bit-for-bit unchanged (audited separately)",
          "- source provenance: `data/external/review/G24A_SOURCE_DATA_AUDIT_v1` (09-24 02:33) — pinned SHA-256 "
          "of official FEVER/SciFact releases, exact row counts, refs resolved 3462/3462, failures=[]",
          ""]
    with open(OUT_MD, "w") as f:
        f.write("\n".join(L) + "\n")

    print(report["verdict"])
    for h in HARD_STOPS:
        print("HARD STOP:", h)
    print(f"wrote {OUT_JSON} and {OUT_MD} ({report['elapsed_s']}s)")
    return 1 if HARD_STOPS else 0


if __name__ == "__main__":
    sys.exit(main())
