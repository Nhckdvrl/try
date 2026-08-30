#!/usr/bin/env python3
"""Build and freeze the FOMC 12+12 qualification-pilot candidate queue.

Implements the CHANGE-first, meeting-disjoint algorithm frozen in
FOMC_TRANSFORMATION_CONTRACT.md's Scope section:

  1. build-change   -- deterministic hash-ordered CHANGE queue (all 29 raw
                        candidates), for human review.
  2. freeze-change   -- walk the reviewed CHANGE ledger in hash order,
                        skipping REJECT/UNSURE and any ACCEPT that collides
                        with an already-selected unit's meetings, until 12
                        disjoint ACCEPTs are found (or the queue runs out).
                        Writes the 12 selected CHANGE units and the set of
                        meetings they reserve.
  3. build-hold      -- deterministic hash-ordered HOLD queue, mechanically
                        pre-skipping any candidate that already collides
                        with a CHANGE-reserved meeting (never presented for
                        human review, since it is guaranteed unusable).
  4. freeze-hold     -- same walk-and-quota logic as freeze-change, against
                        (CHANGE-reserved meetings union already-selected HOLD
                        meetings); on success, builds and writes the final
                        24-unit frozen artifact via src/adapters/fomc_temporal.py,
                        re-fetching each of the 48 distinct statement texts and
                        verifying every one against the pinned manifest hash.

Every step reads only from the pinned data/external/fomc_source_manifest_v1.json
-- never re-scrapes the live FOMC calendar for unit identity/labels, only for
the plain statement text needed to build the final prompts, and even then it
verifies text against the pinned SHA-256 before use.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.fomc_temporal import (  # noqa: E402
    build_candidate,
    derive_labeled_units,
    fetch_statement_text,
    validate_candidate_against_manifest,
)
from information_set_schema import file_sha256, validate_collection  # noqa: E402

MANIFEST_PATH = Path("data/external/fomc_source_manifest_v1.json")
SEED = 20260829
POOL_START = "20081216"
QUOTA = 12

GATES = (
    "scheduled + adjacency provenance correct (both meetings genuinely "
    "scheduled and calendar-adjacent per the pinned manifest)",
    "previous/next statement text matches the pinned SHA-256 (open the "
    "statement URL and confirm)",
    "next statement's action label (CHANGE/HOLD) correctly extracted",
    "no extraction/source mismatch between the two statements",
)

_HEADING = re.compile(r"^### (?:CHANGE|HOLD)-\d+\. `([^`]+)`\s*$")
_DECISION = re.compile(
    r"^\s*-\s*Decision:\s*`\[([ xX])\]\s*ACCEPT\s*\[([ xX])\]\s*REJECT\s*\[([ xX])\]\s*UNSURE`\s*$"
)
_REASON = re.compile(r"^\s*-\s*Reason(?:\s*\(required for REJECT/UNSURE, one line\))?:\s*(.*)$")


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def hash_order(units: list[dict]) -> list[dict]:
    return sorted(units, key=lambda u: hashlib.sha256(f"{SEED}:{u['next']}".encode()).hexdigest())


def render_queue(units: list[dict], meetings: dict, *, label: str) -> str:
    out = [
        f"# FOMC {label} candidate queue — pilot v1",
        "",
        f"> Fixed deterministic order (seed {SEED}). Review top-to-bottom until "
        f"{QUOTA} ACCEPTs that are also meeting-disjoint from earlier selections "
        "are reached. A REJECT/UNSURE consumes its queue slot permanently and is "
        "never resampled or reconsidered. Never reject for salience/fame -- only "
        "the four gates below.",
        "",
        "For each unit, tick exactly one of ACCEPT / REJECT / UNSURE for all four "
        "gates jointly (all four must hold to ACCEPT). On REJECT or UNSURE, write "
        "exactly one line giving the reason.",
        "",
    ]
    for index, unit in enumerate(units, 1):
        prev, nxt = unit["previous"], unit["next"]
        prev_m, next_m = meetings[prev], meetings[nxt]
        out.extend([
            f"### {label}-{index}. `{prev}_{nxt}`",
            "",
            f"- Previous meeting: {prev} — {prev_m['statement_url']} (sha256 `{prev_m['statement_text_sha256']}`)",
            f"- Next meeting: {nxt} — {next_m['statement_url']} (sha256 `{next_m['statement_text_sha256']}`)",
            f"- Next statement's own action verb: `{unit['verb']}` → label `{'CHANGE' if unit['change'] else 'HOLD'}`",
            f"- Extraction method: `{next_m['extraction_method']}`; announced range: `{next_m['action_range']}`",
            "",
            "**Gates (all four must hold to ACCEPT):**",
        ])
        out.extend(f"- [ ] {gate}" for gate in GATES)
        out.extend([
            "",
            "- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`",
            "- Reason (required for REJECT/UNSURE, one line):",
            "",
        ])
    return "\n".join(out).rstrip() + "\n"


def parse_decisions(markdown: str) -> dict[str, tuple[str, str]]:
    decisions: dict[str, tuple[str, str]] = {}
    current: str | None = None
    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        heading = _HEADING.match(line)
        if heading:
            current = heading.group(1)
            continue
        match = _DECISION.match(line)
        if match and current is not None:
            marks = [group.strip().lower() == "x" for group in match.groups()]
            if sum(marks) != 1:
                raise ValueError(f"{current}: exactly one of ACCEPT/REJECT/UNSURE must be ticked")
            decision = ("ACCEPT", "REJECT", "UNSURE")[marks.index(True)]
            reason = ""
            for follow in lines[index + 1 : index + 4]:
                reason_match = _REASON.match(follow)
                if reason_match:
                    reason = reason_match.group(1).strip()
                    break
            if decision != "ACCEPT" and not reason:
                raise ValueError(f"{current}: {decision} requires a one-line reason")
            decisions[current] = (decision, reason)
            current = None
    return decisions


def walk_quota(
    queue: list[dict], decisions: dict[str, tuple[str, str]], *, reserved: set[str]
) -> tuple[list[dict], set[str], list[dict], list[dict]]:
    """Return (selected, newly_reserved, collision_skips, rejects)."""
    selected: list[dict] = []
    newly_reserved: set[str] = set()
    collision_skips: list[dict] = []
    rejects: list[dict] = []
    for unit in queue:
        if len(selected) >= QUOTA:
            break
        key = f"{unit['previous']}_{unit['next']}"
        if key not in decisions:
            raise ValueError(f"queue candidate {key} has no recorded decision")
        decision, reason = decisions[key]
        if decision != "ACCEPT":
            rejects.append({**unit, "decision": decision, "reason": reason})
            continue
        if unit["previous"] in reserved or unit["next"] in reserved:
            collision_skips.append(unit)
            continue
        selected.append(unit)
        reserved.add(unit["previous"])
        reserved.add(unit["next"])
        newly_reserved.add(unit["previous"])
        newly_reserved.add(unit["next"])
    return selected, newly_reserved, collision_skips, rejects


def cmd_build_change(args: argparse.Namespace) -> int:
    manifest = load_manifest()
    labeled = derive_labeled_units(manifest["meetings"], pool_start=POOL_START)
    change_units = hash_order([u for u in labeled if u["change"] == 1])
    Path(args.queue_json).write_text(json.dumps(change_units, indent=2), encoding="utf-8")
    Path(args.queue_md).write_text(render_queue(change_units, manifest["meetings"], label="CHANGE"), encoding="utf-8")
    print(f"wrote {len(change_units)} CHANGE candidates to {args.queue_md} and {args.queue_json}")
    return 0


def cmd_freeze_change(args: argparse.Namespace) -> int:
    manifest = load_manifest()
    queue = json.loads(Path(args.queue_json).read_text(encoding="utf-8"))
    decisions = parse_decisions(Path(args.reviewed).read_text(encoding="utf-8"))
    selected, reserved, collisions, rejects = walk_quota(queue, decisions, reserved=set())
    if len(selected) < QUOTA:
        raise ValueError(
            f"only {len(selected)}/{QUOTA} disjoint ACCEPTs found in the CHANGE queue "
            f"({len(rejects)} rejected, {len(collisions)} collided) -- the pool census "
            "showed 21 disjoint CHANGE are achievable, so a shortfall here means an "
            "unusually high reject rate; do not lower the quota, investigate the rejects"
        )
    Path(args.selected_out).write_text(
        json.dumps({"selected": selected, "reserved_meetings": sorted(reserved),
                    "collision_skips": collisions, "rejects": rejects}, indent=2),
        encoding="utf-8",
    )
    print(f"CHANGE frozen: {len(selected)} selected, {len(rejects)} rejected, {len(collisions)} collision-skipped")
    print(f"wrote {args.selected_out}")
    return 0


def cmd_build_hold(args: argparse.Namespace) -> int:
    manifest = load_manifest()
    change_result = json.loads(Path(args.change_selected).read_text(encoding="utf-8"))
    reserved = set(change_result["reserved_meetings"])
    labeled = derive_labeled_units(manifest["meetings"], pool_start=POOL_START)
    hold_units = hash_order([u for u in labeled if u["change"] == 0])
    # mechanically pre-skip guaranteed-collision candidates -- never shown for review
    prefiltered = [u for u in hold_units if u["previous"] not in reserved and u["next"] not in reserved]
    pool = prefiltered[: args.pool_size]
    Path(args.queue_json).write_text(json.dumps(pool, indent=2), encoding="utf-8")
    Path(args.queue_md).write_text(render_queue(pool, manifest["meetings"], label="HOLD"), encoding="utf-8")
    print(
        f"HOLD candidates: {len(hold_units)} raw, {len(prefiltered)} after mechanical "
        f"collision pre-skip, {len(pool)} in review pool (--pool-size {args.pool_size})"
    )
    print(f"wrote {args.queue_md} and {args.queue_json}")
    return 0


def cmd_freeze_hold(args: argparse.Namespace) -> int:
    manifest = load_manifest()
    meetings = manifest["meetings"]
    change_result = json.loads(Path(args.change_selected).read_text(encoding="utf-8"))
    hold_queue = json.loads(Path(args.hold_queue_json).read_text(encoding="utf-8"))
    decisions = parse_decisions(Path(args.reviewed).read_text(encoding="utf-8"))
    reserved = set(change_result["reserved_meetings"])
    selected_hold, _, collisions, rejects = walk_quota(hold_queue, decisions, reserved=reserved)
    if len(selected_hold) < QUOTA:
        raise ValueError(
            f"only {len(selected_hold)}/{QUOTA} disjoint ACCEPTs found in the HOLD queue -- "
            "re-run build-hold with a larger --pool-size and review only the newly appended "
            "tail; do not lower the quota"
        )

    all_units = change_result["selected"] + selected_hold
    manifest_sha = file_sha256(MANIFEST_PATH)
    texts: dict[str, str] = {}
    items = []
    for unit in all_units:
        for date in (unit["previous"], unit["next"]):
            if date not in texts:
                texts[date] = fetch_statement_text(meetings[date]["statement_url"], meetings[date]["statement_text_sha256"])
        item = build_candidate(
            unit, meetings,
            previous_text=texts[unit["previous"]], next_text=texts[unit["next"]],
            manifest_sha256=manifest_sha,
        )
        validate_candidate_against_manifest(
            item, meetings, previous_text=texts[unit["previous"]], next_text=texts[unit["next"]]
        )
        items.append(item)

    validate_collection(items)
    counts = {"change": sum(u["change"] for u in all_units), "hold": sum(1 - u["change"] for u in all_units)}
    if counts != {"change": QUOTA, "hold": QUOTA}:
        raise ValueError(f"resolution imbalance in final selection: {counts}")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(item.to_json() + "\n" for item in items), encoding="utf-8")

    verdict = Path(args.verdict_out)
    verdict_lines = [
        "# FOMC pilot v1 freeze verdict",
        "",
        f"- accepted: {len(items)} ({counts['change']} CHANGE / {counts['hold']} HOLD)",
        f"- CHANGE: {len(change_result['rejects'])} rejected, {len(change_result['collision_skips'])} collision-skipped during review",
        f"- HOLD: {len(rejects)} rejected, {len(collisions)} collision-skipped during review",
        "",
        "## CHANGE rejections",
        "",
    ]
    change_reject_lines = [f"- `{r['previous']}_{r['next']}`: {r['decision']} — {r['reason']}" for r in change_result["rejects"]]
    verdict_lines.extend(change_reject_lines if change_reject_lines else ["(none)"])
    verdict_lines += ["", "## HOLD rejections", ""]
    hold_reject_lines = [f"- `{r['previous']}_{r['next']}`: {r['decision']} — {r['reason']}" for r in rejects]
    verdict_lines.extend(hold_reject_lines if hold_reject_lines else ["(none)"])
    verdict.write_text("\n".join(verdict_lines) + "\n", encoding="utf-8")

    print(f"wrote {len(items)} frozen pilot units to {out}")
    print(f"CHANGE/HOLD balance: {counts}")
    print(f"wrote verdict to {verdict}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("build-change")
    p.add_argument("--queue-md", default="data/external/review/fomc_pilot_v1_change_candidates.md")
    p.add_argument("--queue-json", default="data/external/review/fomc_pilot_v1_change_candidates.json")
    p.set_defaults(func=cmd_build_change)

    p = sub.add_parser("freeze-change")
    p.add_argument("--queue-json", default="data/external/review/fomc_pilot_v1_change_candidates.json")
    p.add_argument("--reviewed", required=True)
    p.add_argument("--selected-out", default="data/external/review/fomc_pilot_v1_change_selected.json")
    p.set_defaults(func=cmd_freeze_change)

    p = sub.add_parser("build-hold")
    p.add_argument("--change-selected", default="data/external/review/fomc_pilot_v1_change_selected.json")
    p.add_argument("--queue-md", default="data/external/review/fomc_pilot_v1_hold_candidates.md")
    p.add_argument("--queue-json", default="data/external/review/fomc_pilot_v1_hold_candidates.json")
    p.add_argument("--pool-size", type=int, default=40)
    p.set_defaults(func=cmd_build_hold)

    p = sub.add_parser("freeze-hold")
    p.add_argument("--change-selected", default="data/external/review/fomc_pilot_v1_change_selected.json")
    p.add_argument("--hold-queue-json", default="data/external/review/fomc_pilot_v1_hold_candidates.json")
    p.add_argument("--reviewed", required=True)
    p.add_argument("--out", default="data/external/review/fomc_temporal_pilot_v1.jsonl")
    p.add_argument("--verdict-out", default="data/external/review/fomc_pilot_v1_verdict.md")
    p.set_defaults(func=cmd_freeze_hold)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
