from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from freeze_btf3_confirmatory import parse_decisions  # noqa: E402


CANDIDATE_BLOCK = """### YES-1. `qid-1`

- Decision: `[{accept}] ACCEPT  [{reject}] REJECT  [{unsure}] UNSURE`
- Reason (required for REJECT/UNSURE, one line): {reason}

### NO-1. `qid-2`

- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`
- Reason (required for REJECT/UNSURE, one line):
"""


def test_parses_accept_and_reject_with_reason():
    markdown = CANDIDATE_BLOCK.format(accept=" ", reject="x", unsure=" ", reason="temporally impossible claim")
    decisions = parse_decisions(markdown)
    assert decisions["qid-1"] == ("REJECT", "temporally impossible claim")
    assert decisions["qid-2"] == ("ACCEPT", "")


def test_reject_without_reason_is_rejected_by_parser():
    markdown = CANDIDATE_BLOCK.format(accept=" ", reject="x", unsure=" ", reason="")
    with pytest.raises(ValueError, match="requires a one-line reason"):
        parse_decisions(markdown)


def test_multiple_ticks_on_one_decision_is_rejected():
    markdown = CANDIDATE_BLOCK.format(accept="x", reject="x", unsure=" ", reason="")
    with pytest.raises(ValueError, match="exactly one of"):
        parse_decisions(markdown)


SHORT_REASON_BLOCK = """### NO-1. `qid-3`
- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`
- Reason: packet timeline is internally inconsistent

### NO-2. `qid-4`
- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`
"""


def test_short_reason_label_is_also_accepted():
    decisions = parse_decisions(SHORT_REASON_BLOCK)
    assert decisions["qid-3"] == ("REJECT", "packet timeline is internally inconsistent")
    assert decisions["qid-4"] == ("ACCEPT", "")
