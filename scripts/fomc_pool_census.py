#!/usr/bin/env python3
"""Full FOMC eligible-pool census (read-only; does not build a candidate queue).

Reproduces the pool census run for FOMC_TRANSFORMATION_CONTRACT.md's
"Full pool census" step: enumerates scheduled FOMC meetings from official
federalreserve.gov materials, applies the frozen reject rules, labels each
eligible adjacent-meeting pair by the next meeting's own action verb, runs
the range-comparison consistency audit, and computes the meeting-disjoint
maximum achievable balanced sample.

This script only reports counts. It does not select, freeze, or write any
candidate queue -- that is a deliberately separate next step.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import time
import urllib.request

POOL_START = "20081216"  # target-range era start; excluded from ever being a "next" meeting
USER_AGENT = "Mozilla/5.0 (research)"

# The one confirmed non-scheduled meeting found in this census: a special
# Sunday videoconference session, distinguishable from every regular meeting
# (which is always held on a weekday and never described with "Saturday"/
# "Sunday"/"special meeting"/"intermeeting"/"emergency" in its own minutes).
KNOWN_EMERGENCY_DATES = {"20200315"}

# The one confirmed calendar gap found in this census: the regularly
# scheduled mid-March 2020 meeting's business was absorbed into the excluded
# emergency session above, so the surrounding scheduled meetings are not
# genuinely calendar-adjacent even though they are adjacent in a plain
# sorted list of remaining dates.
KNOWN_NON_ADJACENT_PAIRS = {("20200129", "20200429")}

VERB_RE = re.compile(
    r"decided(?: today)? to (raise|lower|maintain|keep)(?:\s+its|\s+the)?\s*target range for the federal funds rate"
    r"\s*(?:to|at|by [^,.]*?to)\s*([^,.\n]+?)\s*(?:percent|percentage point)",
    re.I,
)
WILL_MAINTAIN_RE = re.compile(
    r"will (maintain|keep) the target range for the federal funds rate at\s+([^,.\n]+?)\s*percent",
    re.I,
)
ESTABLISH_RE = re.compile(
    r"decided(?: today)? to establish a target range for the federal funds rate of\s+([^,.\n]+?)\s*percent",
    re.I,
)
REAFFIRM_RE = re.compile(
    r"reaffirmed its (?:expectation|view) that the current[^.]*?target range for the federal funds rate[^.]*?\bof\s+([^,.\n]+?)\s*percent",
    re.I,
)
REAFFIRM_CURRENT_RE = re.compile(
    r"reaffirmed its (?:expectation|view) that the current\s+([^,.\n]+?)\s*percent target range for the federal funds rate",
    re.I,
)
MAINTAIN_CURRENT_RE = re.compile(
    r"maintain the current\s+([^,.\n]+?)\s*percent target range for the federal funds rate",
    re.I,
)
RANGE_ONLY_RE = re.compile(
    r"target range for the federal funds rate\s*(?:to|at|of)\s*([^,.\n]+?)\s*percent", re.I
)


def fetch(url: str, cache: Path) -> str:
    if cache.exists():
        return cache.read_text(encoding="utf-8", errors="ignore")
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as response:
        text = response.read().decode("utf-8", errors="ignore")
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(text, encoding="utf-8")
    time.sleep(0.2)
    return text


def strip_html(html: str) -> str:
    text = re.sub(r"<script.*?</script>", " ", html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text)


def is_emergency_meeting(minutes_html: str) -> bool:
    text = strip_html(minutes_html)
    m = re.search(r"Minutes of the Federal Open Market Committee\s*(.{0,400})", text)
    snippet = m.group(1) if m else ""
    weekend = bool(re.search(r"\b(Saturday|Sunday)\b", snippet))
    special = bool(re.search(r"\bspecial meeting|intermeeting|emergency\b", snippet, re.I))
    return weekend or special


def extract_action(statement_html: str) -> dict:
    text = strip_html(statement_html)
    for regex, verb_fixed, group_idx, method in (
        (VERB_RE, None, None, "verb"),
        (WILL_MAINTAIN_RE, None, None, "will-maintain"),
        (ESTABLISH_RE, "establish", 1, "establish"),
        (REAFFIRM_RE, "maintain", 1, "reaffirm-of"),
        (REAFFIRM_CURRENT_RE, "maintain", 1, "reaffirm-current"),
        (MAINTAIN_CURRENT_RE, "maintain", 1, "maintain-current"),
    ):
        match = regex.search(text)
        if match:
            if verb_fixed:
                return {"verb": verb_fixed, "range": match.group(group_idx).strip(), "method": method}
            return {"verb": match.group(1).lower(), "range": match.group(2).strip(), "method": method}
    return {"verb": None, "range": None, "method": "NO MATCH"}


def normalize_range(value: str | None) -> str | None:
    if value is None:
        return None
    value = value.lower().strip()
    value = re.sub(r"\s+", " ", value)
    return value.replace("‑", "-").replace("–", "-")


def resolve_statement_url(date: str, cache_dir: Path) -> tuple[str, str]:
    """Return (html, resolved_suffix), trying 'a' then escalating on title mismatch."""
    for suffix in ("a", "b", "c"):
        url = f"https://www.federalreserve.gov/newsevents/pressreleases/monetary{date}{suffix}.htm"
        cache = cache_dir / f"{date}{suffix}.html"
        html = fetch(url, cache)
        title_match = re.search(r"<title>(.*?)</title>", html, re.S)
        title = title_match.group(1) if title_match else ""
        if "FOMC statement" in title:
            return html, suffix
    raise ValueError(f"could not resolve a genuine FOMC statement for {date}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache-dir", type=Path, default=Path("/tmp/fomc_census_cache"))
    parser.add_argument("--out", type=Path, default=Path("results/fomc_pool_census.json"))
    parser.add_argument(
        "--minutes-year-range",
        nargs=2,
        type=int,
        default=(2008, 2020),
        help="years to pull from per-year fomchistorical{year}.htm pages",
    )
    args = parser.parse_args()

    minutes_dir = args.cache_dir / "minutes"
    hist_dir = args.cache_dir / "hist"
    statements_dir = args.cache_dir / "statements"

    all_minutes_dates: set[str] = set()
    y0, y1 = args.minutes_year_range
    for year in range(y0, y1 + 1):
        html = fetch(
            f"https://www.federalreserve.gov/monetarypolicy/fomchistorical{year}.htm",
            hist_dir / f"{year}.html",
        )
        all_minutes_dates.update(re.findall(r"fomcminutes(\d{8})\.htm", html))

    # current-era years (recent, not yet moved to the fomchistorical archive)
    cal_html = fetch(
        "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm",
        args.cache_dir / "fomccalendars.html",
    )
    all_minutes_dates.update(re.findall(r"fomcminutes(\d{8})\.htm", cal_html))

    scheduled = []
    emergency_found = []
    for date in sorted(all_minutes_dates):
        if date in KNOWN_EMERGENCY_DATES:
            emergency_found.append(date)
            continue
        html = fetch(
            f"https://www.federalreserve.gov/monetarypolicy/fomcminutes{date}.htm",
            minutes_dir / f"{date}.html",
        )
        if is_emergency_meeting(html):
            emergency_found.append(date)
            continue
        scheduled.append(date)

    eligible = sorted(d for d in scheduled if d >= POOL_START)

    extraction: dict[str, dict] = {}
    for date in eligible:
        html, suffix = resolve_statement_url(date, statements_dir)
        extraction[date] = extract_action(html)
        extraction[date]["resolved_suffix"] = suffix

    raw_pairs = list(zip(eligible, eligible[1:]))
    reject_reasons = {"non_adjacent_gap": 0, "next_is_pool_start_establish": 0, "extraction_failed": 0}
    labeled = []
    for prev, nxt in raw_pairs:
        if (prev, nxt) in KNOWN_NON_ADJACENT_PAIRS:
            reject_reasons["non_adjacent_gap"] += 1
            continue
        verb = extraction[nxt]["verb"]
        if verb is None:
            reject_reasons["extraction_failed"] += 1
            continue
        if verb == "establish":
            reject_reasons["next_is_pool_start_establish"] += 1
            continue
        labeled.append({"previous": prev, "next": nxt, "verb": verb, "change": int(verb in ("raise", "lower"))})

    # secondary consistency audit: previous vs next announced range
    consistency_mismatches = []
    for unit in labeled:
        prev_range = normalize_range(extraction[unit["previous"]]["range"])
        next_range = normalize_range(extraction[unit["next"]]["range"])
        expected_same = unit["change"] == 0
        if (prev_range == next_range) != expected_same:
            consistency_mismatches.append({**unit, "prev_range": prev_range, "next_range": next_range})

    # meeting-disjoint maximum: scarcer class first
    def hash_order(units):
        return sorted(units, key=lambda u: hashlib.sha256(f"20260829:{u['next']}".encode()).hexdigest())

    change_units = hash_order([u for u in labeled if u["change"] == 1])
    hold_units = hash_order([u for u in labeled if u["change"] == 0])
    used: set[str] = set()
    disjoint = {"change": [], "hold": []}
    for bucket_name, bucket in (("change", change_units), ("hold", hold_units)):
        for unit in bucket:
            if unit["previous"] in used or unit["next"] in used:
                continue
            disjoint[bucket_name].append(unit)
            used.add(unit["previous"])
            used.add(unit["next"])

    year_counts: dict[str, dict[str, int]] = {}
    for unit in labeled:
        year = unit["next"][:4]
        bucket = year_counts.setdefault(year, {"change": 0, "hold": 0})
        bucket["change" if unit["change"] else "hold"] += 1

    method_inventory: dict[str, int] = {}
    verb_inventory: dict[str, int] = {}
    for record in extraction.values():
        method_inventory[record["method"]] = method_inventory.get(record["method"], 0) + 1
        verb_inventory[str(record["verb"])] = verb_inventory.get(str(record["verb"]), 0) + 1

    report = {
        "scheduled_meetings_total_all_time": len(scheduled) + len(emergency_found),
        "emergency_or_special_meetings_excluded": sorted(emergency_found),
        "scheduled_meetings_confirmed": len(scheduled),
        "eligible_meetings_pool_start_onward": len(eligible),
        "raw_adjacent_pairs": len(raw_pairs),
        "reject_reasons": reject_reasons,
        "labeled_eligible_units": len(labeled),
        "change_count": sum(1 for u in labeled if u["change"]),
        "hold_count": sum(1 for u in labeled if not u["change"]),
        "consistency_mismatches": consistency_mismatches,
        "disjoint_max_change": len(disjoint["change"]),
        "disjoint_max_hold_after_change_reserved": len(disjoint["hold"]),
        "disjoint_balanced_count": min(len(disjoint["change"]), len(disjoint["hold"])),
        "year_distribution": year_counts,
        "action_verb_inventory": verb_inventory,
        "extraction_method_inventory": method_inventory,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
