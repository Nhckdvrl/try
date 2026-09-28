# G32 material audit, completed before model inference

G32 sampled 60 rows by fixed hash rank from G31's previously constructed and blind-audited 80-row pool. The extra audit asked a narrower question: can the claim stand alone, and do both E and X polarity pairs change what the admissible record warrants under a record-only task? Inputs used arbitrary A/B labels and exposed no G29/G31/G32 model responses. The rubric is in [`INSTRUCTIONS.md`](../../data/items/g32_material_audit_v1/INSTRUCTIONS.md); exact inputs and verdicts are retained beside it.

MiMo 2.6 Flash assessed batches 01/03 (30 items), and Longcat 2.5 Preview batches 02/04 (30 items). Every batch has 15 input and 15 output records with matching IDs; 60 unique items were reviewed. Auditors marked E and X contrasts valid on **60/60**; standalone claim valid and overall record-only viable on **56/60**. The four failures were:

| ID | Defect |
|---|---|
| `g29_068` | “The film” is unnamed. |
| `g29_080` | “It” has no antecedent. |
| `g29_083` | “The film” is unnamed. |
| `g29_092` | “The song” is unnamed. |

The original 60 are preserved in `data/items/g32_pre_audit_60_v1.jsonl` (SHA-256 `0fcd8f9e964ff4c42d4c01ebd3bdcaacfaeaf7145eb9540452aa1371e4e0d261`). `scripts/freeze_g32_after_audit.py` excluded exactly the four failed rows, yielding 56 in `data/items/g32_selected_v1.jsonl` (SHA-256 `1e4c04f366317564ea6414ccfd2934aadb949c7be0374afae92d6ff8ea5ca1bc`). No replacements were drawn.

The final 56 overlap G31's analyzed 60 items in 41 cases; 15 were not run in G31. This is LLM-assisted semantic review, not human gold. It does not eliminate all material ambiguity. Most final claims are numeric or threshold-based (44/56), and the X notes are constructed rather than naturally sourced. Accordingly, G32 can identify a behavior pattern on this controlled material but cannot alone establish a general law about natural evidence.
