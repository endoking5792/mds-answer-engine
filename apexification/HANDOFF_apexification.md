# Handoff — apexification (Roseline, 2026-11-09)

## Files
| File | What |
|---|---|
| `_QUESTIONS.md` | agreed question set (P2, P3 removed at Roseline's request) |
| `canonical/*_CANONICAL.md` | 5 student-facing answers, unified standard (published) |
| `audit/<ID>_*_AUDIT.md` | per-question sidecars: retrieval record, LOC key list, generated locator ledger, uncertainty notes, coverage, revision history, checklist |
| `audit/AUDIT_2026-11-09.md` | merged second-reader + textbook audit ledger (auditors u1-u3), done on the old layout |
| `audit/AUDIT_u1.md`, `AUDIT_u2.md`, `AUDIT_u3.md` | the auditors' separate notes |
| `legacy_v1/` | audited old-layout answers (explanation + exam core, full source lists), kept for provenance |
| `locators.py` + `locators_Q01..Q04,P1,U1..U3.py` | 1290 verbatim locators (missing 0) |
| `build_audit.py` | checks a sidecar + its answer: LOC keys resolve, quotes verbatim, numbers traced, cited surnames in references, body word count; rebuilds the ledger |
| `build_sources.py`, `check_answers.py` | old-layout tools (used for legacy_v1) |

## Answers
| ID | Marks | Body words (range) | LOC keys |
|---|---|---|---|
| Q01 Open apex – considerations and management | 75 | 2925 (2550-3000) | 239 |
| Q02 Non-vital anterior tooth with immature apex | 50 | 1986 (1700-2000) | 436 |
| Q03 Apexification | 10 | 393 (320-400) | 45 |
| Q04 Apexogenesis | 10 | 390 (320-400) | 44 |
| P1 CH apexification vs MTA apical barrier (predicted) | 10 | 370 (320-400) | 52 |

## Sources and offsets (printed = PDF marker - offset)
Ingle's 7e Ch.28 Shabahang -106, Ch.27 Bogen and Chandler -100, Ch.29 Diogenes and Smith (authors from contents page); Grossman 14e Ch.11/12 (Gopikrishna, editor) 25; Torabinejad 6e Ch.10 Diogenes, Botero and Kang 7; Andreasen atlas Ch.22 Cvek 16, Ch.23 Bakland 16; Cohen's 12e Ch.12, 21, 24 None; Harty's 7e Ch.12 Sigurdsson and Bourguignon 16; Sikri 2e 21; Gutmann Ch.13 Gutmann and Lovdahl 11; Endodontology Ch.46 Buerkle and Meissner 17; Endodontic Prognosis Ch.5 Kang and Bogen 9; Bioceramics Ch.5 Tonini and Garo 32; Weine 6e None; AAE Glossary 2012 None; audit books: Walton and Torabinejad 2002 Part 22 (Pitt Ford and Shabahang), Current Therapy Ch.7/11, Vital Pulp Treatment 2024, Essential Endodontology, Seltzer and Bender Ch.13, Treatment of Endodontic Infections, Andreasen atlas Ch.27. Full detail per answer in the sidecars.

## Open points
- Ingle's 7e imprint/year not printed in the extract; Endodontology English edition number not printed.
- Primary papers (Frank 1966, Cvek 1992, Jeeruphan, Finucane and Kinirons 1999, AAE/ESE documents, meta-analyses) cited only as the textbooks report them; no live search.
- Cvek's "frequent change" sentence is self-contradictory (atlas Ch.22); source paper not read.
- Endodontology Ch.46 was cited as Baumann and Beer in earlier topics' drafts here; other topics that cite Endodontology chapters may want their chapter authors checked against the contents page.
- Conversion cut verified material for length (lists in each sidecar); it remains in `legacy_v1/`.
