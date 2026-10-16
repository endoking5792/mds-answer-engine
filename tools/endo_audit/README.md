# Claim-level audit tools (endodontic_sealers, obturation)

`claims_sealers.json` (106 claims) and `claims_obturation.json` (61 claims) list specific figures and attributions from the answers with a regex that must appear in the cited textbook chapter.
Run (needs a clone of the private `endoking5792/mds-textbooks`):

```bash
export TEXTBOOKS=/path/to/mds-textbooks
python3 -I tools/endo_audit/verify_claims.py tools/endo_audit/claims_sealers.json
python3 -I tools/endo_audit/verify_claims.py tools/endo_audit/claims_obturation.json
```

A hit means the string is in the chapter; it does not prove the answer interprets it correctly. Known regex misses: obturation claim 26 (Trifecta "1.0-2.0 mm", text uses an en dash and alpha sign; verified by eye); sealer claims 20, 22, 24, 35, 54, 82, 86 are explained in `endodontic_sealers/A1_Audit_Ledger_2026-10-16.md`.
In the sealer file "S" is Sikri Ch.19; claim 45 cites Torabinejad MTA, which is not in `mds-textbooks` (only in `dental-study-material`), so it always misses.
