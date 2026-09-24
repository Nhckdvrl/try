"""G26A — load-bearing emergence over HoVer two-hop chains.

Frozen design: preregistrations/PREREGISTRATION_G26A_LOAD_BEARING.md (§1, §3).

Cells (10 — O3's printed "11" was corrected to 10 pre-tag, user ruling
2026-09-24; the enumeration below IS the O3 enumeration):

    g26_y0            BACKGROUND -> judgment
    g26_ya            BACKGROUND -> EVIDENCE A -> judgment
    g26_yb            BACKGROUND -> EVIDENCE B -> judgment
    g26_yab           BACKGROUND -> EVIDENCE A -> EVIDENCE B -> judgment
    g26_excl_t0/t1/t2 EXCL rule at the three §1 timings
    g26_admit_t0/t1/t2 ADMIT control rule at the three §1 timings

Phase A (selector) uses ONLY the four no-rule cells — blindness by
construction (prereg §5, §11); the eight rule cells are panel-only.

Timing layouts (prereg §1; the RULING block is the only content whose
position moves relative to A/B; ONE shared filler multiset repositions
across the rule boundary so rule->judgment token distance is equal across
t0/t1/t2 within ±10 tokens under every pooled-panel tokenizer — O7/§9.2):

    t0:  BG -> FILL(fa+fb) -> RULE -> A -> B           (rule before A and B)
    t1:  BG -> A -> FILL(fb) -> RULE -> B -> FILL(fa)  (A present, not load-bearing)
    t2:  BG -> A -> B -> RULE -> FILL(fa+fb)           (rule after the composed chain)

Filler choice is per item and computed at build time (src/build_g26a.py):
``fa``/``fb`` are filler-bank subsets stored in ``item.meta`` with word
totals tuned so each timing's after-rule distance matches (words(fa) tracks
words(A), words(fb) tracks words(B)). The SENTENCE MULTISET fa ∪ fb is
identical across the three timings — only placement differs (prereg §3;
multiset-equality test §9.2). No timing-unique PAD block exists.

Rule sentences are byte-fixed (prereg §3, bytes pinned 2026-09-24):

    EXCL: "Evidence A is excluded. Evidence A must not influence your final judgment."
    ADMIT: "Evidence A is admitted. It must be given the full weight of a verified item in your final judgment."

Question / output spec are G24A's constants verbatim (0–9 prompt scale;
readout = digit_expectation_0_100, the G0/G24A lineage; prereg §3).

Probes (prereg §3, timing pinned 2026-09-24, user ruling): one per rule
type — ``rule_probe_g26_excl`` / ``rule_probe_g26_admit`` — each issued on
its own rule type's T0 layout (rule farthest from the judgment: strictest
rule-legibility test), YES/NO readout.
"""
from __future__ import annotations

try:
    from .conditions_g24a import OUTPUT_SPEC, QUESTION  # package use
except ImportError:
    from conditions_g24a import OUTPUT_SPEC, QUESTION

import re

# --- byte-fixed rule constants (prereg §3) ---------------------------------
EXCL_RULE = ("Evidence A is excluded. Evidence A must not influence "
             "your final judgment.")
ADMIT_RULE = ("Evidence A is admitted. It must be given the full weight "
              "of a verified item in your final judgment.")

RULE_PROBE_QUESTION = ("According to the ruling above, are you permitted to "
                       "use evidence A when you reach your rating? Answer "
                       "with exactly one word: YES or NO.")
MEMORY_QUESTION = ""   # schema completeness; no memory probe in G26A (§3)

# --- headers (G0/G24A lineage; RULING keeps rule_char_offset working) ------
BACKGROUND_HEADER = "BACKGROUND"
EVIDENCE_A_HEADER = "EVIDENCE A"
EVIDENCE_B_HEADER = "EVIDENCE B"
RULE_HEADER = "RULING"
FILLER_HEADER = "CONTEXT NOTE"

NORULE_CELLS = ("g26_y0", "g26_ya", "g26_yb", "g26_yab")
RULE_CELLS = tuple(f"g26_{arm}_t{t}"
                   for arm in ("excl", "admit") for t in (0, 1, 2))
G26A_CONDITIONS = list(NORULE_CELLS) + list(RULE_CELLS)   # frozen O3 order, 10
G26A_PROBES = ["rule_probe_g26_excl", "rule_probe_g26_admit"]
TIMINGS = (0, 1, 2)

WORD_RE = re.compile(r"\b[\w'-]+\b")


def words(text: str) -> list[str]:
    """Word tokens — same regex family as the HoVer audit (R2 8..80 words)."""
    return WORD_RE.findall(text)


# --- hand-authored neutral filler bank (prereg §3: never LLM-generated at
# item time, unrelated to any claim or page, fixed forever from this tag).
# Word schedule {4..20} x 4 = 68 sentences / 816 words — the GLOBAL histogram
# is exact and asserted (per-block size comments below are indicative groupings
# only), so any build-time target word total in [4, 816] is packable. Content
# is neutral common-noun observation — no proper nouns, no claim content, no
# page entities.
#
# v2 (pre-tag §0 amendment, 2026-09-24): 13 of the 68 slots deliberately carry
# cross-tokenizer divergence so the ±10-token rule→judgment gate (O7) stays
# reachable for evidence whose tokenization splits differently across the pooled
# panel (v1 was zero-divergence on the qwen3/qwen35 axes → 29/3642 items could
# not be furnished): 7 number-dense sentences (3–4-digit quantities; qwen3,
# qwen35 and gemma each add ≈+2 tokens per number vs llama → F = (≈+6..+8)) and
# 6 accent/Latinate sentences (French loanwords + Latinate compounds that gemma
# /qwen35 merge — e.g. "résumé" (d35,dg) = (−2,−2), "chrysanthemum" dg = −4 →
# F ≈ (0, −1..−3, −3..−9)). All remain hand-authored and neutral. ---------
FILLER_BANK: tuple[str, ...] = (
    # 4 words x4
    "The kettle boiled dry.",
    "Pens refill by twisting.",
    "Maps fade in sunlight.",
    "Rain stopped at noon.",
    # 5 x4
    "The door sticks in winter.",
    "Shelves lean to one side.",
    "Quiet halls echo at dusk.",
    "Coins warm in the sun.",
    # 6 x4
    "The wind moved the tall grass.",
    "The old paint flakes near windows.",
    "A clock ticks in the hall.",
    "The buses pass every few minutes.",
    # 7 x4
    "The corridor lights all dim after midnight.",
    "The cart rolled slowly past the entrance.",
    "Someone stacked the boxes by the wall.",
    "The old floorboards creak under light steps.",
    # 8 x4
    "The crème and chrysanthemum sat by the door.",
    "A low hedge runs along the eastern fence.",
    "The printer jammed again on the lower tray.",
    "Someone repainted the bench a slightly darker green.",
    # 9 x4
    "The narrow stairs curve gently toward the second landing.",
    "Two crates and 128 cartons wait by the door.",
    "The faucet drips more loudly during the early morning.",
    "Nobody noticed the small crack near the window frame.",
    # 10 x4
    "The hallway notice board lists errands for the whole week.",
    "A pair of sparrows built a nest under the awning.",
    "Her résumé and the quiet façade both looked quite plain.",
    "Volunteers rearranged the small chairs before the evening talk began.",
    # 11 x4
    "The stock sheet lists 248 tins and 36 spare gray spools.",
    "A cold draft slips under the door whenever the wind shifts.",
    "The janitor leaves all the western lights on until late evening.",
    "Each wide shelf near the entrance holds only identical brown boxes.",
    # 12 x4
    "The old voilà and a dried chrysanthemum rested by the wide window.",
    "A parked maintenance cart blocks half of the long narrow service corridor.",
    "The small water fountain near the wooden stairs barely trickles all winter.",
    "Nobody ever signed the paper sheet that circulates with the weekly clipboard.",
    # 13 x4
    "Someone recorded 128 lamps, 392 plugs, and 47 small fuses on the sheet.",
    "Two quiet volunteers swept the wide entrance steps long before the doors opened.",
    "The old broken radiator clicks loudly whenever the heavy pipes carry heat upstairs.",
    "Every single window on the long second floor faces the very same quiet courtyard.",
    # 14 x4
    "A tall stack of old unclaimed letters sits quietly beside the main front reception desk in the lobby hall.",
    "Beside the stair the stratosphere poster and the résumé hung above the low shelf.",
    "Someone keeps quietly moving the tall shared step ladder to yet another corner.",
    "The paper bulletin near the quiet stairwell simply announces nothing of any real importance.",
    # 15 x4
    "Fresh deliveries arrive at the small loading bay most weekday mornings before the entire main office actually opens each day.",
    "The quiet inventory tally reads 512 chairs, 248 tables, and 96 tall plain floor lamps.",
    "A small radio in the far back office always plays softly during the entire workday.",
    "The wide cork bulletin board near the small kitchen still carries menus from last month.",
    # 16 x4
    "Every slow afternoon the side counter counts 248 bolts, 617 washers, 36 cracked tiles, and 128 plain spare hooks.",
    "The carpet in the outer waiting room shows one worn path to the side door.",
    "Every single Tuesday morning someone wheels a cart of old magazines into the lobby.",
    "The spare encyclopaedia, the dried chrysanthemum, and a folded voilà sat unnoticed on the low bench.",
    # 17 x4
    "A single pigeon sometimes lands on the wide second windowsill and watches the long empty corridor below.",
    "Throughout the week the back office stored 128 ledgers, 456 paper clips, 24 rubber bands, 617 tins, and 36 folders.",
    "Most weekday afternoons the shared upstairs printer quietly runs out of toner before anyone refills it.",
    "The wide glass panel above the small side entrance slowly gathers dust that nobody ever bothers to wipe clean.",
    # 18 x4
    "During the day the front desk logs 128 parcels, 392 envelopes, and 617 late forms every week.",
    "The long upstairs hallway always smells faintly of fresh coffee whenever the morning meeting finishes early.",
    "Nobody here can clearly recall exactly when the small table by the window first appeared here.",
    "The faded schedule taped inside the small kitchen window has still not changed since the early spring.",
    # 19 x4
    "When it rains outside, the low courtyard drain slowly backs up and leaves behind a wide shallow standing puddle.",
    "The heavy library door on the quiet north side rarely ever gets properly used by absolutely anyone at all now.",
    "There is one quite narrow gap behind the lowest shelves where thick dust quietly collects throughout the whole long winter.",
    "The rear garden entrance always stays locked on weekends even though the small sign says open daily.",
    # 20 x4
    "During the cold winter months the old radiators in the far west wing click constantly throughout the night.",
    "The quiet volunteer who carefully waters the plants each Friday always forgets the ones sitting near the stairs.",
    "The heavy encyclopaedia, the old oesophagus chart, and a matinée notice lay neatly stacked by the wide window.",
    "Nobody at all has carefully opened the chipped small cabinet under the back sink since the last inspection.",
)


def is_g26(cond: str) -> bool:
    return cond in G26A_CONDITIONS


def blocks(item, cond: str) -> list[str]:
    """Ordered content blocks for one G26A condition (prereg §1 / §3)."""
    if cond not in G26A_CONDITIONS:
        raise ValueError(f"unknown G26A condition {cond!r}")
    bg = f"{BACKGROUND_HEADER}\n{item.base_context}"
    a = f"{EVIDENCE_A_HEADER}\n{item.critical_evidence}"
    b = f"{EVIDENCE_B_HEADER}\n{item.meta['evidence_b']}"
    if cond == "g26_y0":
        return [bg]
    if cond == "g26_ya":
        return [bg, a]
    if cond == "g26_yb":
        return [bg, b]
    if cond == "g26_yab":
        return [bg, a, b]

    excl = cond.startswith("g26_excl")
    rule = RULE_HEADER + "\n" + (EXCL_RULE if excl else ADMIT_RULE)
    fa = item.meta.get("filler_a") or []
    fb = item.meta.get("filler_b") or []
    if not fa or not fb:
        raise ValueError(
            f"{item.item_id}: rule cells need build-time fillers "
            f"(meta.filler_a / meta.filler_b) — run src/build_g26a.py")

    def fill(sents: list[str]) -> str:
        return f"{FILLER_HEADER}\n" + "\n".join(sents)

    timing = int(cond[-1])
    if timing == 0:      # RULE -> A -> B
        return [bg, fill(fa + fb), rule, a, b]
    if timing == 1:      # A -> RULE -> B
        return [bg, a, fill(fb), rule, b, fill(fa)]
    return [bg, a, b, rule, fill(fa + fb)]   # A -> B -> RULE


def filler_sentences(blocks_list: list[str]) -> list[str]:
    """Every filler sentence present in a compiled block list (tests §9.2)."""
    out: list[str] = []
    for blk in blocks_list:
        if blk.startswith(FILLER_HEADER + "\n"):
            out.extend(blk.split("\n")[1:])
    return out


def after_rule(blocks_list: list[str]) -> str:
    """Text strictly after the RULING block — the distance-bearing suffix."""
    for i, blk in enumerate(blocks_list):
        if blk.startswith(RULE_HEADER + "\n"):
            return "\n\n".join(blocks_list[i + 1:])
    raise ValueError("no RULING block")
