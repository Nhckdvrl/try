"""G16 prompt construction and freeze checklist — no model weights, no generation.

The G16 contrast holds the exclusion grammar fixed and varies only what the policy
can be resolved against:

    FAILURE  id_pre   RULING  Evidence E7 has decision weight 0.
                      EVIDENCE E7
    SUCCESS  cls_pre  RULING  Any item in this file marked as coming from an
                              unauthorised source has decision weight 0.
                      EVIDENCE E7 [source: unauthorised]

Both state the policy before the evidence, share the background block and the
`has decision weight 0` wording, and carry byte-identical evidence content. The
class rule is longer and the tag adds tokens, so `id_pre` is padded upstream of the
rule with the frozen clerical filler until the two prompts match in length. Padding
sits *before* the rule in both arms, so it cannot come between the policy and the
evidence it governs.

An admitting arm is built for both so the estimand is the 2x2 interaction rather
than a raw difference a tag alone could produce.

Run the freeze checklist (tokenizer only)::

    PYTHONPATH=src python3 src/mech/binding_prompts.py --report
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from common import ROOT, frozen_items, span_indices  # noqa: E402
from conditions_v2 import ID_PREAMBLE, filler_block, stable_seed  # noqa: E402
from conditions_v3 import CLS_SOURCE_TAG  # noqa: E402
from schema import ANSWER_CUE, ANSWER_FORMATS, SYSTEM  # noqa: E402

FAMILIES = ("legal_judgment", "evidence_inference")

# Frozen rule strings. Both arms use the same `has decision weight 0` predicate, so
# the manipulation is the binding structure and not the exclusion grammar.
ID_RULE = "RULING\nEvidence E7 has decision weight 0."
CLS_RULE = (
    "RULING\nAny item in this file marked as coming from an unauthorised source "
    "has decision weight 0."
)
ID_ADMIT_RULE = (
    "RULING\nEvidence E7 has the full decision weight of a verified item."
)
CLS_ADMIT_RULE = (
    "RULING\nAny item in this file marked as coming from an unauthorised source "
    "has the full decision weight of a verified item."
)

# Tolerance fixed in the preregistration. Items whose padded pair still differs by
# more than this are dropped before any generation.
LENGTH_TOLERANCE = 4
MAX_FILLER_UNITS = 40

CONDITIONS = ("id_exclude", "cls_exclude", "id_admit", "cls_admit")


def _pad_to(tok, seed: int, target_tokens: int) -> str:
    """Frozen clerical filler truncated to `target_tokens`, or '' if none needed.

    Whole filler units are far coarser than the few-token deficit we need to close,
    so the block is built long and then truncated at token granularity and decoded —
    the same construction Stage 5 used to length-match its previews. Re-tokenising a
    decoded truncation can move the count by a token or two, which is why a tolerance
    is preregistered rather than assumed to be zero.
    """
    if target_tokens <= 0:
        return ""
    text = ""
    for k in range(1, MAX_FILLER_UNITS + 1):
        text = filler_block(k, seed).split("\n", 1)[1].replace("- ", "").replace("\n", " ")
        if len(tok(text, add_special_tokens=False)["input_ids"]) >= target_tokens:
            break
    ids = tok(text, add_special_tokens=False)["input_ids"][:target_tokens]
    return "ADMINISTRATIVE RECORD\n" + tok.decode(ids)


def _n(tok, text: str) -> int:
    return len(tok(text, add_special_tokens=False)["input_ids"])


def build_pair(tok, item) -> dict:
    """Return the four prompts for one item plus their length bookkeeping."""
    seed = stable_seed(item.item_id)
    background = "BACKGROUND\n" + item.base_context + "\n" + ID_PREAMBLE
    evidence_plain = "EVIDENCE E7\n" + item.critical_evidence
    evidence_tagged = (
        "EVIDENCE E7 " + CLS_SOURCE_TAG + "\n" + item.critical_evidence
    )
    task = (
        "TASK\n" + item.question + "\n" + item.output_spec + "\n"
        + ANSWER_FORMATS["direct"]
    )

    def assemble(cond: str, pad: str):
        exclude = cond.endswith("_exclude")
        is_cls = cond.startswith("cls_")
        rule = (CLS_RULE if exclude else CLS_ADMIT_RULE) if is_cls else (
            ID_RULE if exclude else ID_ADMIT_RULE
        )
        evidence = evidence_tagged if is_cls else evidence_plain
        blocks = [background]
        # padding only in the identifier arm, and always upstream of the rule
        if not is_cls and pad:
            blocks.append(pad)
        blocks += [rule, evidence, task]
        text = tok.apply_chat_template(
            [{"role": "system", "content": SYSTEM},
             {"role": "user", "content": "\n\n".join(blocks)}],
            tokenize=False, add_generation_prompt=True,
        )
        return text + ANSWER_CUE + " ", blocks

    # The pad carries its own header and block separator, and re-tokenising a
    # truncated decode is not exactly length-preserving, so the budget is solved for
    # against the assembled prompts rather than estimated from the block deltas.
    budget = (_n(tok, CLS_RULE) - _n(tok, ID_RULE)) + (
        _n(tok, evidence_tagged) - _n(tok, evidence_plain)
    )
    deficit = budget
    pad, best_pad, best_gap = "", "", None
    for _ in range(8):
        pad = _pad_to(tok, seed, budget)
        gap = _n(tok, assemble("cls_exclude", pad)[0]) - _n(tok, assemble("id_exclude", pad)[0])
        if best_gap is None or abs(gap) < abs(best_gap):
            best_gap, best_pad = gap, pad
        if gap == 0:
            break
        budget += gap
        if budget <= 0:
            break
    pad = best_pad

    out = {"item_id": item.item_id, "direction": item.critical_direction,
           "deficit_tokens": deficit, "pad_tokens": _n(tok, pad) if pad else 0,
           "prompts": {}, "blocks": {}}
    for cond in CONDITIONS:
        out["prompts"][cond], out["blocks"][cond] = assemble(cond, pad)

    out["n_tok"] = {c: _n(tok, out["prompts"][c]) for c in CONDITIONS}
    out["delta_exclude"] = out["n_tok"]["cls_exclude"] - out["n_tok"]["id_exclude"]
    out["delta_admit"] = out["n_tok"]["cls_admit"] - out["n_tok"]["id_admit"]
    out["within_tolerance"] = (
        abs(out["delta_exclude"]) <= LENGTH_TOLERANCE
        and abs(out["delta_admit"]) <= LENGTH_TOLERANCE
    )
    return out


def sites_of(tok, prompt: str, blocks: list[str]) -> dict:
    """Semantic patch sites, present in both arms. `blocks` = [...,rule,evidence,task]."""
    rule, evidence = blocks[-3], blocks[-2]
    out: dict = {}
    lo, hi = span_indices(tok, prompt, rule)
    out["rule_end"] = hi - 1
    out["rule_span"] = (lo, hi)
    _, ehi = span_indices(tok, prompt, evidence)
    out["evidence_end"] = ehi - 1
    out["answer"] = -1
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="/var/tmp/xiang-isr-models/qwen3-8b")
    ap.add_argument("--report", action="store_true")
    ap.add_argument(
        "--out",
        default=os.path.join(ROOT, "results", "mech", "g16_freeze_checklist.json"),
    )
    args = ap.parse_args()

    from transformers import AutoTokenizer

    tok = AutoTokenizer.from_pretrained(args.model)
    items = frozen_items(FAMILIES)
    built = [build_pair(tok, it) for it in items]
    kept = [b for b in built if b["within_tolerance"]]
    dropped = [b for b in built if not b["within_tolerance"]]

    # site resolution must succeed in every kept item, in every condition
    site_failures = []
    for b in kept:
        for cond in CONDITIONS:
            try:
                sites_of(tok, b["prompts"][cond], b["blocks"][cond])
            except (ValueError, TypeError) as exc:
                site_failures.append({"item_id": b["item_id"], "condition": cond,
                                      "error": str(exc)})

    report = {
        "note": "prompt-only freeze checklist; no model weights loaded, no generation",
        "tokenizer": args.model,
        "families": list(FAMILIES),
        "length_tolerance_tokens": LENGTH_TOLERANCE,
        "n_items_total": len(built),
        "n_items_kept": len(kept),
        "n_items_dropped": len(dropped),
        "dropped": [
            {"item_id": b["item_id"], "delta_exclude": b["delta_exclude"],
             "delta_admit": b["delta_admit"]} for b in dropped
        ],
        "site_resolution_failures": site_failures,
        "raw_deficit_tokens_before_padding": {
            "min": min(b["deficit_tokens"] for b in built),
            "max": max(b["deficit_tokens"] for b in built),
        },
        "residual_gap_tokens_after_padding": {
            "exclude_min": min(b["delta_exclude"] for b in built),
            "exclude_max": max(b["delta_exclude"] for b in built),
            "admit_min": min(b["delta_admit"] for b in built),
            "admit_max": max(b["delta_admit"] for b in built),
        },
        "pad_tokens": {
            "min": min(b["pad_tokens"] for b in built),
            "max": max(b["pad_tokens"] for b in built),
        },
        "prompt_tokens": {
            cond: {
                "min": min(b["n_tok"][cond] for b in kept),
                "max": max(b["n_tok"][cond] for b in kept),
            }
            for cond in CONDITIONS
        },
        "kept_item_ids": [b["item_id"] for b in kept],
    }
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as handle:
        json.dump(report, handle, indent=1)

    if args.report:
        print(f"items {report['n_items_kept']}/{report['n_items_total']} within "
              f"±{LENGTH_TOLERANCE} tokens; {report['n_items_dropped']} dropped")
        raw = report["raw_deficit_tokens_before_padding"]
        res = report["residual_gap_tokens_after_padding"]
        print(f"raw cls-minus-id deficit before padding: {raw['min']}..{raw['max']} tokens")
        print(f"residual gap after padding: exclude "
              f"{res['exclude_min']}..{res['exclude_max']}, admit "
              f"{res['admit_min']}..{res['admit_max']} tokens")
        print(f"site resolution failures: {len(site_failures)}")
        for cond in CONDITIONS:
            lo, hi = report["prompt_tokens"][cond].values()
            print(f"  {cond:12s} {lo}-{hi} tokens")
    print(f"wrote {os.path.relpath(args.out, ROOT)}")


if __name__ == "__main__":
    main()
