"""CK-P1 material builder: public observability vs finite recursive knowledge.

No target-model calls. Creates 24 semantic skeletons x 4 matched information
structures with deterministic TRUE/FALSE gold at depths 1,2,3,4,6.

Authority: MAINLINE_AUDIT_2026-09-06_V9.md
Design: CK_P1_DESIGN_AUDIT.md
"""
from __future__ import annotations
import json
from pathlib import Path

STRUCTURES = ("K1", "K2", "K3", "CK")
DEPTHS = (1, 2, 3, 4, 6)
LICENSED_DEPTH = {"K1": 1, "K2": 2, "K3": 3, "CK": 10_000}
FORBIDDEN_VISIBLE_TERMS = (
    "common knowledge", "kripke", "public announcement logic",
    "arbitrary depth", "infinite recursion",
)

AGENT_PAIRS = (
    ("Alice","Bob"), ("Maya","Leo"), ("Nora","Evan"), ("Lina","Omar"),
    ("Priya","Noah"), ("Sofia","Daniel"), ("Mei","Jonas"), ("Amina","Lucas"),
    ("Elena","Ravi"), ("Marta","Theo"), ("Yuna","Felix"), ("Sara","Milan"),
    ("Iris","Adam"), ("Nadia","Hugo"), ("Leila","Marco"), ("Tara","Simon"),
    ("Anika","Joel"), ("Mina","Oscar"), ("Rina","Dylan"), ("Clara","Samir"),
    ("Aya","Peter"), ("Nina","Victor"), ("Rosa","Eli"), ("Kira","Martin"),
)

SKELETONS = (
    ("meeting_time", "the workshop starts at 3:00"),
    ("meeting_time", "the briefing starts at 10:30"),
    ("meeting_time", "the rehearsal starts at 5:15"),
    ("meeting_time", "the tour starts at 1:45"),
    ("object_location", "the red folder is in Cabinet 2"),
    ("object_location", "the spare key is in Drawer 4"),
    ("object_location", "the blue notebook is on Shelf 7"),
    ("object_location", "the small toolkit is in Locker 5"),
    ("room_assignment", "the design team will use Room 3"),
    ("room_assignment", "the interview will be held in Room 8"),
    ("room_assignment", "the afternoon class will meet in Room 6"),
    ("room_assignment", "the volunteer desk will be in Room 2"),
    ("package_location", "Package Luma is at the east desk"),
    ("package_location", "Package Neri is at the north counter"),
    ("package_location", "Parcel Tavo is in storage bay C"),
    ("package_location", "Parcel Seki is at pickup window 4"),
    ("event_date", "the maintenance check is on Thursday"),
    ("event_date", "the equipment audit is on Monday"),
    ("event_date", "the garden inspection is on Wednesday"),
    ("event_date", "the safety drill is on Friday"),
    ("simple_property", "the display card for sample R is green"),
    ("simple_property", "the label on container M is triangular"),
    ("simple_property", "the marker beside station K is orange"),
    ("simple_property", "the tag attached to box V is square"),
)

def as_sentence(clause: str) -> str:
    return clause[0].upper() + clause[1:] + "."

def modality_for(index: int) -> str:
    return "spoken" if index % 2 else "display"

def outer_agents(index: int, a: str, b: str) -> tuple[str, str]:
    return (a, b) if index % 2 else (b, a)

def build_story(a: str, b: str, p: str, structure: str, modality: str) -> str:
    if structure not in STRUCTURES:
        raise ValueError(structure)
    if modality not in {"spoken", "display"}:
        raise ValueError(modality)
    P = as_sentence(p)

    if modality == "spoken":
        if structure == "K1":
            return (
                f'In a private one-to-one conversation, the coordinator tells {a}: “{P}” '
                f'In a separate private conversation, the coordinator tells {b} the same fact. '
                f"Neither person is present for the other's conversation, and neither is told what was said there."
            )
        if structure == "K2":
            return (
                f'In a private one-to-one conversation, the coordinator tells {a}: “{P}” '
                f"The coordinator also tells {a} that {b} knows this fact. "
                f"In a separate private conversation, the coordinator tells {b} the same fact and tells {b} that {a} knows it. "
                f"Neither person is present for the other's conversation or told anything else about it."
            )
        if structure == "K3":
            return (
                f'In a private one-to-one conversation, the coordinator tells {a}: “{P}” '
                f"The coordinator also tells {a} that {b} knows this fact and that {b} knows {a} knows it. "
                f"In a separate private conversation, the coordinator tells {b} the same fact and tells {b} that {a} knows it "
                f"and that {a} knows {b} knows it. Neither person is present for the other's conversation or told anything else about it."
            )
        return (
            f"{a} and {b} are standing together with the coordinator. "
            f'The coordinator clearly announces: “{P}” '
            f"Both hear the announcement, and each can plainly see that the other is there hearing the same announcement."
        )

    if structure == "K1":
        return (
            f'{a} privately reads a trusted message that says: “{P}” '
            f"Separately, {b} privately reads a trusted message with the same fact. "
            f"Neither person can see the other's message or knows what was shown there."
        )
    if structure == "K2":
        return (
            f'{a} privately reads a trusted message that says: “{P}” '
            f"The message also tells {a} that {b} knows this fact. "
            f"Separately, {b} privately reads a trusted message with the same fact and is told that {a} knows it. "
            f"Neither person can see the other's message or learns anything else about it."
        )
    if structure == "K3":
        return (
            f'{a} privately reads a trusted message that says: “{P}” '
            f"The message also tells {a} that {b} knows this fact and that {b} knows {a} knows it. "
            f"Separately, {b} privately reads a trusted message with the same fact and is told that {a} knows it "
            f"and that {a} knows {b} knows it. Neither person can see the other's message or learns anything else about it."
        )
    return (
        f"{a} and {b} are standing together in front of one trusted screen. "
        f'The screen clearly displays: “{P}” '
        f"Both read it, and each can plainly see that the other is there reading the same display."
    )

def nested_statement(outer: str, other: str, p: str, depth: int) -> str:
    if depth < 1:
        raise ValueError("depth must be positive")
    inner = p
    agents = [outer if i % 2 == 0 else other for i in range(depth)]
    for agent in reversed(agents):
        inner = f"{agent} knows that {inner}"
    return as_sentence(inner)

def gold_for(structure: str, depth: int) -> str:
    return "TRUE" if depth <= LICENSED_DEPTH[structure] else "FALSE"

def primary_prompt(story: str, statement: str) -> str:
    return (
        f"Read the short story below.\n\n{story}\n\n"
        f"Statement: {statement}\n"
        "Based only on the story, is the statement TRUE or FALSE?\n"
        "Answer with exactly TRUE or FALSE."
    )

def qualification_prompt(story: str, a: str, b: str) -> str:
    return (
        f"Read the short story below.\n\n{story}\n\n"
        f"Question: Did {a} and {b} jointly receive the fact in a way that each could directly observe the other's access?\n"
        "Answer with exactly TRUE or FALSE."
    )

def build_contexts() -> list[dict]:
    if len(SKELETONS) != 24 or len(AGENT_PAIRS) != 24:
        raise AssertionError("CK-P1 requires 24 skeletons")
    rows = []
    for index, ((domain, proposition), (a, b)) in enumerate(
        zip(SKELETONS, AGENT_PAIRS, strict=True), start=1
    ):
        modality = modality_for(index)
        outer, other = outer_agents(index, a, b)
        skeleton_id = f"ckp1_{index:03d}"
        for structure in STRUCTURES:
            story = build_story(a, b, proposition, structure, modality)
            for term in FORBIDDEN_VISIBLE_TERMS:
                if term in story.lower():
                    raise AssertionError(f"{skeleton_id}/{structure}: forbidden term {term}")
            queries = []
            for depth in DEPTHS:
                statement = nested_statement(outer, other, proposition, depth)
                queries.append({
                    "depth": depth,
                    "statement": statement,
                    "gold": gold_for(structure, depth),
                    "prompt": primary_prompt(story, statement),
                })
            rows.append({
                "version": "ck_p1_v1",
                "context_id": f"{skeleton_id}_{structure.lower()}",
                "skeleton_id": skeleton_id,
                "domain": domain,
                "modality": modality,
                "structure": structure,
                "agent_a": a,
                "agent_b": b,
                "outer_agent": outer,
                "proposition": proposition,
                "story": story,
                "queries": queries,
                "qualification": {
                    "gold": "TRUE" if structure == "CK" else "FALSE",
                    "prompt": qualification_prompt(story, a, b),
                },
            })
    return rows

def validate_contexts(rows: list[dict]) -> None:
    if len(rows) != 96:
        raise AssertionError(f"expected 96 contexts, got {len(rows)}")
    by = {}
    for row in rows:
        by.setdefault(row["skeleton_id"], []).append(row)
    if len(by) != 24:
        raise AssertionError("expected 24 skeleton IDs")

    expected = {
        "K1": ("TRUE","FALSE","FALSE","FALSE","FALSE"),
        "K2": ("TRUE","TRUE","FALSE","FALSE","FALSE"),
        "K3": ("TRUE","TRUE","TRUE","FALSE","FALSE"),
        "CK": ("TRUE","TRUE","TRUE","TRUE","TRUE"),
    }
    for sid, quartet in by.items():
        if {r["structure"] for r in quartet} != set(STRUCTURES):
            raise AssertionError(f"{sid}: incomplete quartet")
        if len({r["proposition"] for r in quartet}) != 1:
            raise AssertionError(f"{sid}: proposition changed")
        statements = [tuple(q["statement"] for q in r["queries"]) for r in quartet]
        if len(set(statements)) != 1:
            raise AssertionError(f"{sid}: query changed")
        for row in quartet:
            if tuple(q["depth"] for q in row["queries"]) != DEPTHS:
                raise AssertionError(f"{row['context_id']}: wrong depths")
            if tuple(q["gold"] for q in row["queries"]) != expected[row["structure"]]:
                raise AssertionError(f"{row['context_id']}: wrong gold")
    mods = [r["modality"] for r in rows if r["structure"] == "CK"]
    if mods.count("spoken") != 12 or mods.count("display") != 12:
        raise AssertionError("cue families not balanced")

def write_jsonl(path: Path) -> None:
    rows = build_contexts()
    validate_contexts(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("data/items/ck_p1_v1.jsonl"))
    args = parser.parse_args()
    write_jsonl(args.out)
    print(f"wrote 96 contexts to {args.out}")
