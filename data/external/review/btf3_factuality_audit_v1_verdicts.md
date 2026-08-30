# BTF-3 packet factuality audit v1 — verdict ledger

**Auditor of record:** _(fill in: name, and whether external lookup was
available — this ledger is worthless without that line)_
**Audit dates:** _(fill in)_
**Access used:** _(fill in: which sources were opened, e.g. live web, archive
snapshots, paywalled outlets unavailable)_
**Model outputs inspected:** none. The auditor must not open any file under
`results/raw/`.

**Protocol:** `PROTOCOL_BTF3_PACKET_FACTUALITY_AUDIT.md`. Sample:
`btf3_factuality_audit_v1_sample.json` (32 realized YES + 32 realized NO, fixed
by hash before any citation was opened). Packets to work through:
`btf3_factuality_audit_v1_yes.md` and `btf3_factuality_audit_v1_no.md`.

Nothing recorded here changes the frozen 256-unit primary sample.

## Verdicts

Append one block per item, in the order the packets are listed:

```markdown
### YES-1. `<question_id>`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### YES-2. `<question_id>`
- Verdict: `[ ] PASS  [x] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason: one line, required for MATERIAL_ERROR and UNVERIFIABLE.
```

Exactly one box per item. `scripts/analyze_btf3_factuality_audit.py` parses
this file, applies the frozen decision rule, and computes the secondary
leave-flagged-out sensitivity.
