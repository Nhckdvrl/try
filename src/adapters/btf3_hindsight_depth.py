"""Prompt builders for PREREGISTRATION_G2_HINDSIGHT_DEPTH.md.

Two manipulations, both applied to the frozen 256-unit large-replication
artifact without reselecting, dropping, or rewriting a single unit:

* **Experiment A — positional replication.** The exclusion reminder from the
  64-unit factorization (byte-identical string) is placed either before or
  after the inadmissible packet, in the out-of-set frame and, as a matched
  control, in the licensed frame.
* **Experiment B — explicit verdict redaction (EVR).** The packet's explicit
  YES/NO verdict sentences are removed by a frozen, mechanical rule while the
  post-cutoff supporting evidence is kept.

Nothing here consults any target-model output.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import re
from typing import Any

try:
    from ..information_set_schema import InformationSetItem
    from .btf3_factorization import M1_REMINDER, extract_packet
except ImportError:  # direct use with PYTHONPATH=src
    from information_set_schema import InformationSetItem
    from adapters.btf3_factorization import M1_REMINDER, extract_packet

_PACKET_MARKER = "\n\nLATER RESOLUTION PACKET\n"
_TASK_MARKER = "\n\nTASK\n"

# Byte-identical to the reminder used in the 64-unit factorization, so the
# out-of-set arm of Experiment A is a true replication and not a re-wording.
EXCLUDE_REMINDER = M1_REMINDER

# Matched licensed reminder: same REMINDER header, same referent, same
# sentence shape; only the admissibility clause differs. It cannot be
# byte-identical to EXCLUDE_REMINDER (the manipulation *is* admissibility),
# so both strings and their lengths are reported in the freeze audit.
ALLOWED_REMINDER = (
    "\n\nREMINDER\nThe information in LATER RESOLUTION PACKET above was "
    "produced after the evaluation point defined above and may inform "
    "your answer."
)

POSITIONS = ("before", "after")
FRAMES = ("oob", "allowed")


def _variant(item: InformationSetItem, frame: str) -> dict[str, Any]:
    if frame == "oob":
        return item.oob_variant
    if frame == "allowed":
        return item.admissible_variant
    raise ValueError(f"unknown frame {frame!r}")


def build_positional(item: InformationSetItem, *, frame: str, position: str) -> str:
    """Baseline WITH prompt plus one reminder, before or after the packet.

    Within a frame the two positions differ in exactly one way: the byte
    offset at which the identical reminder string is spliced in.
    """
    if position not in POSITIONS:
        raise ValueError(f"unknown position {position!r}")
    reminder = EXCLUDE_REMINDER if frame == "oob" else ALLOWED_REMINDER
    prompt = _variant(item, frame)["with_information_prompt"]
    marker = _PACKET_MARKER if position == "before" else _TASK_MARKER
    index = prompt.index(marker)
    return prompt[:index] + reminder + prompt[index:]


# ---------------------------------------------------------------------------
# Explicit verdict redaction
# ---------------------------------------------------------------------------

# Frozen list of assertive verdict forms. Each pattern matches a *whole
# sentence* that states the realized outcome. Conditional restatements of the
# resolution criteria ("resolves YES if ...", "would resolve NO unless ...")
# are deliberately NOT matched: they disclose no outcome, and removing them
# would strip criteria paraphrase rather than the answer.
_VERDICT_PATTERNS = (
    r"resolution\s*:\s*(?:yes|no)\b.*",
    r"(?:therefore|thus|hence|so|accordingly|in\s+conclusion)?[,\s]*"
    r"(?:the\s+|this\s+)?question\s+(?:therefore\s+)?resolves?\s+(?:as\s+|to\s+)?(?:yes|no)\b.*",
    r"(?:therefore|thus|hence|accordingly)?[,\s]*(?:the\s+)?resolution\s+is\s+(?:yes|no)\b.*",
    r"(?:therefore|thus|hence|accordingly)?[,\s]*(?:it\s+)?resolves?\s+(?:as\s+|to\s+)?(?:yes|no)\b.*",
    r"(?:therefore|thus|hence|accordingly)?[,\s]*(?:the\s+)?answer\s+is\s+(?:yes|no)\b.*",
    r"(?:the\s+)?correct\s+resolution\s+is\s+(?:yes|no)\b.*",
)
_VERDICT_RE = re.compile(
    r"^(?:" + "|".join(_VERDICT_PATTERNS) + r")$", re.IGNORECASE | re.DOTALL
)

# Conditional markers that make a sentence a criteria restatement rather than
# an outcome assertion; such sentences are kept.
_CONDITIONAL_RE = re.compile(
    r"\b(?:only\s+if|if\s+and\s+only|would\s+resolve|will\s+resolve|resolves?\s+(?:yes|no)\s+(?:if|only|unless|when)|"
    r"criteria\s+(?:state|require|say)|in\s+order\s+to\s+resolve)\b",
    re.IGNORECASE,
)

# When a verdict sentence carries its evidence in a subordinate clause, the
# clause is kept and only the verdict clause is removed.
_CLAUSE_RE = re.compile(r"\b(because|since)\b\s+(.+)$", re.IGNORECASE | re.DOTALL)

# Assertive verdict expressed as a trailing clause of a compound sentence
# ("..., and the question resolves NO."). Removed clause-wise, keeping the
# evidential main clause intact.
_TRAILING_CLAUSE_RE = re.compile(
    r"[,;]\s*(?:and\s+|so\s+|thus\s+|therefore,?\s+|hence\s+|accordingly,?\s+)?"
    r"(?:the\s+|this\s+)?question\s+(?:therefore\s+)?resolves?\s+(?:as\s+|to\s+)?"
    r"(?:\*\*)?(?:yes|no)\s*(?:\((?:0|1)\))?(?:\*\*)?\s*(?:\((?:0|1)\))?\s*[.!?]?\s*$",
    re.IGNORECASE,
)
_MIN_KEPT_PREFIX_WORDS = 3

# Screening detector for the post-redaction audit: any surviving mention of a
# resolution verdict, assertive or conditional. Hits are classified, and the
# audit requires that none of them be assertive.
_RESIDUAL_RE = re.compile(
    r"resolv\w*\s+(?:as\s+|to\s+)?(?:\*\*)?(?:yes|no)\b|resolution\s*:\s*(?:\*\*)?(?:yes|no)\b",
    re.IGNORECASE,
)

_SENTENCE_SPLIT = re.compile(r"(?:(?<=[.!?])|(?<=[.!?][\"'\u201d\)\]]))\s+")
_LEADING_MARKUP = re.compile(r"^(\s*(?:[-*>]\s+|\d+[.)]\s+)?)(.*)$", re.DOTALL)


def _normalize_for_match(sentence: str) -> str:
    text = sentence.replace("**", "").replace("__", "")
    text = re.sub(r"\s+", " ", text).strip()
    # trailing outcome codes and punctuation: "... resolves NO (0)." -> "... resolves NO"
    text = re.sub(r"[\s.;:!?]+$", "", text)
    return text


@dataclass
class RedactionResult:
    text: str
    removed_sentences: list[str] = field(default_factory=list)
    preserved_clauses: list[str] = field(default_factory=list)

    @property
    def n_removed(self) -> int:
        return len(self.removed_sentences)


def redact_verdicts(packet: str) -> RedactionResult:
    """Remove assertive YES/NO verdict sentences, keep everything else.

    The rule is mechanical and one-directional: it can only delete text or
    replace a verdict sentence with its own ``because``/``since`` clause. It
    never adds, reorders, or paraphrases, so a redacted packet is always a
    subset of the original's information.
    """
    removed: list[str] = []
    preserved: list[str] = []
    out_lines: list[str] = []
    for line in packet.split("\n"):
        if not line.strip():
            out_lines.append(line)
            continue
        prefix, body = _LEADING_MARKUP.match(line).groups()
        kept: list[str] = []
        for sentence in _SENTENCE_SPLIT.split(body):
            if not sentence.strip():
                continue
            normalized = _normalize_for_match(sentence)
            if _CONDITIONAL_RE.search(normalized) or not _VERDICT_RE.match(normalized):
                trimmed, clause = _trim_trailing_verdict(sentence.strip())
                if clause:
                    removed.append(clause)
                if trimmed:
                    kept.append(trimmed)
                continue
            removed.append(sentence.strip())
            clause = _CLAUSE_RE.search(normalized)
            if clause:
                text = clause.group(2).strip()
                text = text[0].upper() + text[1:] if text else text
                if not text.endswith((".", "!", "?")):
                    text += "."
                preserved.append(text)
                kept.append(text)
        if kept:
            out_lines.append(prefix + " ".join(kept))
        elif prefix.strip():
            # a bullet whose entire content was a verdict: drop the bullet
            continue
    text = "\n".join(out_lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return RedactionResult(text=text, removed_sentences=removed, preserved_clauses=preserved)


def _trim_trailing_verdict(sentence: str) -> tuple[str | None, str | None]:
    """Drop an assertive verdict clause hanging off the end of a sentence.

    Returns ``(kept_text, removed_clause)``. When trimming would leave less
    than a short evidential prefix, the whole sentence is dropped instead of
    leaving a fragment; ``kept_text`` is then ``None``.
    """
    match = _TRAILING_CLAUSE_RE.search(sentence)
    if not match or _CONDITIONAL_RE.search(sentence[match.start():]):
        return sentence, None
    prefix = sentence[: match.start()].rstrip(" ,;")
    clause = sentence[match.start():].strip(" ,;")
    if len(prefix.split()) < _MIN_KEPT_PREFIX_WORDS:
        return None, sentence.strip()
    if not prefix.endswith((".", "!", "?", '"', "'")):
        prefix += "."
    return prefix, clause


def is_assertive_verdict(sentence: str) -> bool:
    """True when a sentence states the outcome rather than restating criteria."""
    normalized = _normalize_for_match(sentence)
    if _CONDITIONAL_RE.search(normalized):
        return False
    if _VERDICT_RE.match(normalized):
        return True
    return bool(_TRAILING_CLAUSE_RE.search(normalized))


def residual_verdict_hits(text: str) -> list[dict[str, Any]]:
    """Surviving verdict-like mentions, classified for the redaction audit.

    ``assertive`` hits must be zero after redaction; conditional hits are
    criteria restatements and are expected to survive, since removing them
    would strip the question's own rules rather than the answer.
    """
    hits: list[dict[str, Any]] = []
    for line in text.split("\n"):
        for sentence in _SENTENCE_SPLIT.split(line):
            stripped = sentence.strip()
            if stripped and _RESIDUAL_RE.search(stripped):
                hits.append({"sentence": stripped, "assertive": is_assertive_verdict(stripped)})
    return hits


def build_evr(item: InformationSetItem, *, frame: str) -> tuple[str, RedactionResult]:
    """Baseline WITH prompt with the packet replaced by its redacted form."""
    prompt = _variant(item, frame)["with_information_prompt"]
    packet = extract_packet(item.oob_variant["with_information_prompt"])
    if prompt.count(packet) != 1:
        raise ValueError(f"packet not found exactly once in {frame} prompt for {item.independent_unit_id}")
    result = redact_verdicts(packet)
    return prompt.replace(packet, result.text), result
