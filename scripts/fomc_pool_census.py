#!/usr/bin/env python3
"""Full FOMC eligible-pool census (read-only; does not build a candidate queue).

v2: derives the scheduled-meeting universe and every statement URL
structurally from federalreserve.gov's own official archive pages --
`fomchistorical{year}.htm` (2008-2020, each meeting/conference-call/
notation-vote gets its own labeled panel with an explicit "Statement"
link) and `fomccalendars.htm` (2021-present, each scheduled meeting gets
an explicit "Statement:" link in its own row). No statement URL is ever
guessed (no a/b/c suffix probing), no meeting's scheduled/emergency status
is inferred from statement or minutes wording, and no exception is
hardcoded: a panel is scheduled if and only if its own official heading
says "... Meeting - {year}" with no parenthetical qualifier (which
authoritatively excludes "(unscheduled) Meeting", "(cancelled) Meeting",
"(notation vote)", and "Conference Call" entries, all confirmed present
verbatim in the official archive). Adjacency is defined purely by
position in this officially-derived scheduled-only sequence.

Also writes a pinned source manifest (date, statement URL, statement-text
SHA-256, action, range, and the exact archive page URL the link came
from) so the 24-unit prompt set can be exactly reconstructed later even
if federalreserve.gov's pages change.

This script only reports counts and the manifest. It does not select,
freeze, or write any candidate queue -- that is a deliberately separate
next step.
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

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from adapters.fomc_temporal import extract_statement_body  # noqa: E402

POOL_START = "20081216"  # target-range era start; excluded from ever being a "next" meeting
USER_AGENT = "Mozilla/5.0 (research)"
HISTORICAL_YEARS = range(2008, 2021)  # fomchistorical{year}.htm covers these
CALENDAR_URL = "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"

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

# A panel/row is a genuinely scheduled meeting iff its own official heading
# says "... Meeting - {year}" with nothing else in parentheses. This single
# rule is what the Fed's own archive uses to separate "March 15-16 Meeting"
# from "March 15 (unscheduled) Meeting", "March 17-18 (cancelled) Meeting",
# "March 19 (notation vote)", and "January 9 Conference Call" -- confirmed
# by direct inspection of fomchistorical2008.htm and fomchistorical2020.htm.
SCHEDULED_HEADING_RE = re.compile(r"^(?!.*\().*\bMeeting\s*-\s*\d{4}\s*$")


def fetch(url: str, cache: Path) -> str:
    if cache.exists():
        return cache.read_text(encoding="utf-8", errors="ignore")
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as response:
        text = response.read().decode("utf-8", errors="ignore")
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(text, encoding="utf-8")
    time.sleep(0.15)
    return text


def strip_html(html: str) -> str:
    text = re.sub(r"<script.*?</script>", " ", html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text)


def parse_historical_year(html: str, source_url: str) -> list[dict]:
    """Split fomchistorical{year}.htm into panels; keep scheduled Meeting panels."""
    panels = re.split(r'(?=<h5[^>]*>)', html)
    out = []
    for panel in panels:
        heading_match = re.search(r"<h5[^>]*>([^<]*)</h5>", panel)
        if not heading_match:
            continue
        heading = heading_match.group(1).strip()
        if not SCHEDULED_HEADING_RE.match(heading):
            continue
        statement_match = re.search(r'<a href="([^"]*)">Statement</a>', panel)
        if not statement_match:
            continue  # meeting panel with no statement published yet
        href = statement_match.group(1)
        date_match = re.search(r"monetary/?(\d{8})[a-z]?\.htm", href)
        if not date_match:
            continue
        date = date_match.group(1)
        url = "https://www.federalreserve.gov" + href if href.startswith("/") else href
        out.append({"date": date, "statement_url": url, "heading": heading, "source_index_url": source_url})
    return out


def parse_calendar_page(html: str, source_url: str) -> list[dict]:
    """Split fomccalendars.htm into per-meeting rows; keep rows with a Statement link."""
    rows = re.split(r'(?=<div class="(?:fomc-meeting--shaded )?row fomc-meeting")', html)
    out = []
    for row in rows:
        statement_match = re.search(
            r"<strong>Statement:</strong>.*?<a href=\"([^\"]*pressreleases[^\"]*)\">HTML</a>",
            row,
            re.S,
        )
        if not statement_match:
            continue
        href = statement_match.group(1)
        date_match = re.search(r"monetary/?(\d{8})[a-z]?\.htm", href)
        if not date_match:
            continue
        date = date_match.group(1)
        url = "https://www.federalreserve.gov" + href if href.startswith("/") else href
        out.append({"date": date, "statement_url": url, "heading": "(fomccalendars row)", "source_index_url": source_url})
    return out


def extract_action(statement_text: str) -> dict:
    for regex, verb_fixed, group_idx, method in (
        (VERB_RE, None, None, "verb"),
        (WILL_MAINTAIN_RE, None, None, "will-maintain"),
        (ESTABLISH_RE, "establish", 1, "establish"),
        (REAFFIRM_RE, "maintain", 1, "reaffirm-of"),
        (REAFFIRM_CURRENT_RE, "maintain", 1, "reaffirm-current"),
        (MAINTAIN_CURRENT_RE, "maintain", 1, "maintain-current"),
    ):
        match = regex.search(statement_text)
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache-dir", type=Path, default=Path("/tmp/fomc_census_cache_v2"))
    parser.add_argument("--out", type=Path, default=Path("results/fomc_pool_census.json"))
    parser.add_argument("--manifest-out", type=Path, default=Path("data/external/fomc_source_manifest_v1.json"))
    args = parser.parse_args()

    meetings: dict[str, dict] = {}
    for year in HISTORICAL_YEARS:
        source_url = f"https://www.federalreserve.gov/monetarypolicy/fomchistorical{year}.htm"
        html = fetch(source_url, args.cache_dir / "index" / f"hist{year}.html")
        for entry in parse_historical_year(html, source_url):
            meetings.setdefault(entry["date"], entry)

    cal_html = fetch(CALENDAR_URL, args.cache_dir / "index" / "fomccalendars.html")
    for entry in parse_calendar_page(cal_html, CALENDAR_URL):
        meetings.setdefault(entry["date"], entry)

    scheduled_all_time = sorted(meetings)
    eligible = [d for d in scheduled_all_time if d >= POOL_START]

    manifest: dict[str, dict] = {}
    for date in eligible:
        entry = meetings[date]
        cache_path = args.cache_dir / "statements" / f"{date}.html"
        html = fetch(entry["statement_url"], cache_path)
        text = strip_html(html)
        title_match = re.search(r"<title>(.*?)</title>", html, re.S)
        title = title_match.group(1) if title_match else ""
        if "FOMC statement" not in title:
            raise ValueError(
                f"structurally-derived statement URL for {date} ({entry['statement_url']}) "
                f"does not resolve to an FOMC statement (title: {title!r}) -- treat as extraction failure, "
                "do not fall back to guessing another suffix"
            )
        action = extract_action(text)
        body = extract_statement_body(text)
        manifest[date] = {
            "date": date,
            "statement_url": entry["statement_url"],
            "source_index_url": entry["source_index_url"],
            "official_heading": entry["heading"],
            "statement_text_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
            "action_verb": action["verb"],
            "action_range": action["range"],
            "extraction_method": action["method"],
        }

    raw_pairs = list(zip(eligible, eligible[1:]))
    reject_reasons = {"next_is_pool_start_establish": 0, "extraction_failed": 0}
    labeled = []
    for prev, nxt in raw_pairs:
        verb = manifest[nxt]["action_verb"]
        if verb is None:
            reject_reasons["extraction_failed"] += 1
            continue
        if verb == "establish":
            reject_reasons["next_is_pool_start_establish"] += 1
            continue
        labeled.append({"previous": prev, "next": nxt, "verb": verb, "change": int(verb in ("raise", "lower"))})

    consistency_mismatches = []
    for unit in labeled:
        prev_range = normalize_range(manifest[unit["previous"]]["action_range"])
        next_range = normalize_range(manifest[unit["next"]]["action_range"])
        expected_same = unit["change"] == 0
        if (prev_range == next_range) != expected_same:
            consistency_mismatches.append({**unit, "prev_range": prev_range, "next_range": next_range})

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
    for record in manifest.values():
        method_inventory[record["extraction_method"]] = method_inventory.get(record["extraction_method"], 0) + 1
        verb_inventory[str(record["action_verb"])] = verb_inventory.get(str(record["action_verb"]), 0) + 1

    report = {
        "scheduled_meetings_confirmed_all_time": len(scheduled_all_time),
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
        "derivation_method": "structural: scheduled iff official archive heading is 'Meeting - {year}' "
                              "with no parenthetical; statement URL taken verbatim from that panel's own "
                              "'Statement' link, never guessed",
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    args.manifest_out.parent.mkdir(parents=True, exist_ok=True)
    args.manifest_out.write_text(
        json.dumps({"manifest_version": 1, "pool_start": POOL_START, "meetings": manifest}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(report, indent=2, sort_keys=True))
    print(f"\nwrote pinned source manifest ({len(manifest)} meetings) to {args.manifest_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
