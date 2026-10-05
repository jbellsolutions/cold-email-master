# Mode 4 smoke test: TEST EVIDENCE, NEVER UPLOAD

This folder proves that `cold-email-master` Mode 4 works end to end: per-lead research, per-lead writing, `verify_doc.py --leads` and the cross-lead similarity check. It ran on 2026-10-04 against three real Ohio auto repair shops, using public website and review details. Sources for every detail are in `research.json`.

- **Nobody was contacted.** Nothing was sent or uploaded.
- **The lead keys are deliberately fake** `@example.invalid` addresses. Two of the shops had no public email, so their keys were never real. The third is replaced too, so this file can never be mistaken for an upload list.
- **The copy is a draft.** It assumed roster flags were false, so it uses "Justin, who hosts it". It is not approved for sending.

Re-run:
```
python3 ../../cold-email-master/scripts/verify_doc.py --leads leads.json --packets packets.json --allow ai
```
