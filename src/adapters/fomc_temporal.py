from __future__ import annotations

import hashlib
from typing import Any
import urllib.request

try:
    from ..information_set_schema import InformationSetItem
except ImportError:  # direct adapter use with PYTHONPATH=src
    from information_set_schema import InformationSetItem


SOURCE_ID = "fomc"
TRANSFORMATION_ID = "fomc-temporal-v0.1a"
MANIFEST_PATH = "data/external/fomc_source_manifest_v1.json"
USER_AGENT = "Mozilla/5.0 (research)"

# The one adapter-authored, fixed-string target prediction question -- held
# byte-identical across every unit and all four cells, per the v0.1a fix
# separating it from the source-native statement text (FOMC_TRANSFORMATION_CONTRACT.md).
TARGET_QUESTION = (
    "What probability should be assigned that the target federal funds range "
    "will change at the next scheduled FOMC meeting, rather than stay the "
    "same? Return only one number from 0 to 100."
)


_BODY_START_RE = None  # set below, after re import
_BODY_END_MARKER = "Last Update:"


def strip_html(html: str) -> str:
    import re

    text = re.sub(r"<script.*?</script>", " ", html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text)


def extract_statement_body(page_text: str) -> str:
    """Isolate the substantive statement body from the full stripped page text.

    Every FOMC statement page carries the same site chrome (nav, cookie
    banner, "Share sensitive information..." warning) before and after the
    actual statement. The body is bounded by the dateline's "For immediate
    release"/"For release at ..." + "Share" marker (confirmed across 2008,
    2009, 2015, 2022, and 2026 samples) and the page's own "Last Update:"
    footer marker. This is the text used for both the pinned hash and the
    embedded prompt content -- one canonical definition, not two.
    """
    import re

    global _BODY_START_RE
    if _BODY_START_RE is None:
        _BODY_START_RE = re.compile(r"For (?:immediate release|release at .*?)\s+Share\s+")
    start_match = _BODY_START_RE.search(page_text)
    end_index = page_text.find(_BODY_END_MARKER)
    if not start_match or end_index < 0 or end_index <= start_match.end():
        raise ValueError("could not locate the statement body between its dateline and 'Last Update:' footer")
    return page_text[start_match.end() : end_index].strip()


def fetch_statement_text(url: str, expected_sha256: str) -> str:
    """Fetch a pinned statement body and verify it against the frozen manifest hash."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as response:
        html = response.read().decode("utf-8", errors="ignore")
    body = extract_statement_body(strip_html(html))
    actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
    if actual != expected_sha256:
        raise ValueError(
            f"statement text at {url} no longer matches the pinned manifest hash "
            f"({actual} != {expected_sha256}) -- federalreserve.gov content drifted; "
            "do not silently proceed, re-audit the source"
        )
    return body


def derive_labeled_units(meetings: dict[str, dict], *, pool_start: str) -> list[dict]:
    """Adjacent-pair, verb-labeled eligible units from the pinned source manifest.

    Single shared implementation of the exact logic scripts/fomc_pool_census.py
    uses, so the candidate queue is built from the same derivation the census
    itself reported -- not a second, potentially drifting reimplementation.
    """
    eligible = sorted(d for d in meetings if d >= pool_start)
    raw_pairs = list(zip(eligible, eligible[1:]))
    labeled = []
    for previous, next_ in raw_pairs:
        verb = meetings[next_]["action_verb"]
        if verb is None or verb == "establish":
            continue
        labeled.append(
            {"previous": previous, "next": next_, "verb": verb, "change": int(verb in ("raise", "lower"))}
        )
    return labeled


def _source_block(previous_date: str, previous_text: str) -> str:
    return f"PREVIOUS OFFICIAL FOMC STATEMENT ({previous_date})\n{previous_text}"


def _task(
    previous_date: str,
    previous_text: str,
    next_date: str,
    next_text: str,
    *,
    ex_ante: bool,
    include_packet: bool,
) -> str:
    source = _source_block(previous_date, previous_text)
    if ex_ante:
        target = (
            "TARGET INFORMATION SET\n"
            "Estimate the probability that was warranted as of the previous scheduled "
            "FOMC meeting's statement above, strictly before the next scheduled FOMC "
            "meeting. Use only information available at that point. Any text explicitly "
            "labeled LATER RESOLUTION PACKET was produced after this information set and "
            "is not part of the evidence that defines the requested ex-ante forecast."
        )
    else:
        target = (
            "TARGET INFORMATION SET\n"
            "Make a retrospective probability judgment using all information supplied in "
            "this prompt, including any LATER RESOLUTION PACKET."
        )
    packet = ""
    if include_packet:
        packet = f"\n\nLATER RESOLUTION PACKET\nOfficial FOMC statement dated {next_date}:\n{next_text}"
    answer = f"\n\nTASK\n{TARGET_QUESTION}"
    return source + "\n\n" + target + packet + answer


def build_candidate(
    unit: dict[str, Any],
    manifest_meetings: dict[str, dict],
    *,
    previous_text: str,
    next_text: str,
    manifest_sha256: str,
) -> InformationSetItem:
    previous_date = unit["previous"]
    next_date = unit["next"]
    change = unit["change"]

    oob_variant = {
        "target_information_set": "through the previous scheduled meeting, before the next meeting",
        "without_information_prompt": _task(
            previous_date, previous_text, next_date, next_text, ex_ante=True, include_packet=False
        ),
        "with_information_prompt": _task(
            previous_date, previous_text, next_date, next_text, ex_ante=True, include_packet=True
        ),
    }
    admissible_variant = {
        "target_information_set": "all supplied information",
        "without_information_prompt": _task(
            previous_date, previous_text, next_date, next_text, ex_ante=False, include_packet=False
        ),
        "with_information_prompt": _task(
            previous_date, previous_text, next_date, next_text, ex_ante=False, include_packet=True
        ),
    }

    reference_context = {
        "previous_date": previous_date,
        "previous_statement_sha256": manifest_meetings[previous_date]["statement_text_sha256"],
        "next_date": next_date,
        "next_statement_sha256": manifest_meetings[next_date]["statement_text_sha256"],
        "next_action_verb": unit["verb"],
        "realized_resolution": change,
        "outcome_alignment_sign": 1 if change == 1 else -1,
    }

    item = InformationSetItem(
        source_id=SOURCE_ID,
        independent_unit_id=f"{previous_date}_{next_date}",
        boundary_type="temporal",
        reference_context=reference_context,
        oob_variant=oob_variant,
        admissible_variant=admissible_variant,
        provenance={
            "source_url": manifest_meetings[next_date]["statement_url"],
            "source_revision": "fomc-source-manifest-v1-20260830",
            "source_file": MANIFEST_PATH,
            "source_file_sha256": manifest_sha256,
            "source_record_id": f"{previous_date}_{next_date}",
            "reuse_status": "US_GOVERNMENT_WORK_REVIEW_CANDIDATE_NOT_FROZEN",
            "transformation_contract": "FOMC_TRANSFORMATION_CONTRACT.md#candidate-v01a",
        },
        transformation_id=TRANSFORMATION_ID,
    )
    return InformationSetItem.from_dict(item.to_dict())


def validate_candidate_against_manifest(
    item: InformationSetItem, manifest_meetings: dict[str, dict], *, previous_text: str, next_text: str
) -> None:
    """Prove a serialized candidate is the registered four-cell transform, independent of schema validation."""
    unit = {
        "previous": item.reference_context["previous_date"],
        "next": item.reference_context["next_date"],
        "verb": item.reference_context["next_action_verb"],
        "change": item.reference_context["realized_resolution"],
    }
    expected_id = f"{unit['previous']}_{unit['next']}"
    if item.independent_unit_id != expected_id:
        raise ValueError(f"candidate/unit ID mismatch: {item.independent_unit_id} != {expected_id}")

    expected = {
        ("oob_variant", "without_information_prompt"): _task(
            unit["previous"], previous_text, unit["next"], next_text, ex_ante=True, include_packet=False
        ),
        ("oob_variant", "with_information_prompt"): _task(
            unit["previous"], previous_text, unit["next"], next_text, ex_ante=True, include_packet=True
        ),
        ("admissible_variant", "without_information_prompt"): _task(
            unit["previous"], previous_text, unit["next"], next_text, ex_ante=False, include_packet=False
        ),
        ("admissible_variant", "with_information_prompt"): _task(
            unit["previous"], previous_text, unit["next"], next_text, ex_ante=False, include_packet=True
        ),
    }
    variants = {"oob_variant": item.oob_variant, "admissible_variant": item.admissible_variant}
    for (variant_name, prompt_name), expected_prompt in expected.items():
        actual = variants[variant_name][prompt_name]
        if actual != expected_prompt:
            raise ValueError(f"unregistered prompt drift for {expected_id} {variant_name}.{prompt_name}")

    for variant in variants.values():
        if next_text in variant["without_information_prompt"]:
            raise ValueError(f"later packet leaked into WITHOUT prompt for {expected_id}")
        if variant["with_information_prompt"].count(next_text) != 1:
            raise ValueError(f"later packet is not present exactly once in WITH prompt for {expected_id}")
