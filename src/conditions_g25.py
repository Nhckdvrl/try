"""G25A: G23A's weight-ladder conditions over G24A's natural materials.

Frozen design: preregistrations/PREREGISTRATION_G25A_NEAR_ZERO.md.

Exactly one factor changes with respect to G23A — the materials — so the
rule construction, block orders and readout stay G23A's, while the
background/evidence rendering follows the G24A natural-materials lineage
(headers ``CLAIM`` / ``EVIDENCE E``; prereg §2–§3 + G24A §3; prereg §3's
``BACKGROUND``/``EVIDENCE`` notation is schematic).

Cells (16, O2):

    g25_base        CLAIM -> judgment                     (no critical evidence)
    g25_norule      CLAIM -> EVIDENCE E -> judgment       (full influence, no rule)
    g25_{arm}_{w}   CLAIM -> [rule | EVIDENCE E] -> [EVIDENCE E | rule] -> judgment
                    arm ∈ {pre, post};  w ∈ {0, 1, 2, 5, 10, 25, 100}%

The rule string is ``conditions_v3.uniform_weight_rule`` **verbatim** — the
same function G23A used — with ``critical_label = "evidence E"`` (prereg §3),
so prohibition and attenuation are worded identically and only the percentage
ever changes. The candidates' precomputed ``admit_rule``/``exclude_rule``
strings are deliberately not used: the sweep changes materials, not rule
wording.

Probes (O3): the G23A-style requested-weight-access probe, ``pre`` arm only,
at ``w = 0`` and ``w = 100`` — 2 probe cells/item, ≤ 3,200 probe rows over the
4-model panel (prereg §11 budget).
"""
from __future__ import annotations

try:
    from .conditions_v3 import uniform_weight_rule
except ImportError:  # direct use with PYTHONPATH=src
    from conditions_v3 import uniform_weight_rule

# key -> fraction handed to `uniform_weight_rule` (percentage = fraction*100)
WEIGHTS = {"w000": 0.0, "w001": 0.01, "w002": 0.02, "w005": 0.05,
           "w010": 0.10, "w025": 0.25, "w100": 1.00}
# order is the preregistered reporting order (§6): zero first, then the ladder
WKEYS = ("w000", "w001", "w002", "w005", "w010", "w025", "w100")
LOCAL_WKEYS = ("w001", "w002", "w005")     # Δ_local0 reference plateau
CONTEXT_WKEYS = ("w010", "w025", "w100")   # context curve (reported, not gated)
ARMS = ("pre", "post")

G25A_CONDITIONS = ["g25_base", "g25_norule"] + [
    f"g25_{arm}_{w}" for w in WKEYS for arm in ARMS
]
# co-primary contrast #2 references w001 explicitly (Gap(0) − Gap(1))

G25A_NUMERIC_PROBES = ["wprobe_g25_pre_w000", "wprobe_g25_pre_w100"]
G25A_PROBES = G25A_NUMERIC_PROBES

# G24A natural-materials headers (byte-identical lineage; prereg §2)
CLAIM_HEADER = "CLAIM"
EVIDENCE_HEADER = "EVIDENCE E"


def is_g25(cond: str) -> bool:
    return cond in G25A_CONDITIONS


def blocks(item, cond: str) -> list[str]:
    """Ordered content blocks for one G25A condition.

    B/E rendering is the G24A materials lineage (byte-identical headers and
    block text); only block order and the one number in the G23A rule ever
    change. Dispatch on the condition name — the sweep runs over G24A-family
    items but owns its own 16 cells.
    """
    B = CLAIM_HEADER + "\n" + item.base_context
    E = EVIDENCE_HEADER + "\n" + item.critical_evidence
    if cond == "g25_base":
        return [B]
    if cond == "g25_norule":
        return [B, E]
    _, arm, wkey = cond.split("_")
    rule = uniform_weight_rule(item, WEIGHTS[wkey])
    return [B, rule, E] if arm == "pre" else [B, E, rule]
