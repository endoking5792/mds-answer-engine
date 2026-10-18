# HANDOFF: Traumatic dental injuries (drafted and IADT-audited, 2026-10-19)

Read first: `~/.claude/skills/dental-study-material/SKILL.md` Section 7. The index of every file, with marks, word counts against the Section 7 ranges and status, is `00_INDEX.md`. The audit ledger, with each correction, its source page and what was not audited, is `AUDIT_IADT_2026-10-19.md`.

## Status
- Every repository question in `_QUESTIONS.md` has a drafted answer (T01-T20) plus predicted P1-P3.
- Audit against the supplied IADT 2020 guidelines (Fouad et al, 2020, avulsion; Bourguignon et al, 2020, fractures and luxations) and the supplied reviews (Khandelwal 2021, Krastl 2022, Saikia 2023, Crowder 2024, Kumari 2025, Blackledge 2025, Huang 2024, Abreu 2024, Andreasen 2002) is complete. Corrections are listed per answer in `AUDIT_IADT_2026-10-19.md`.
- Exam Mode: all 23 answers are inside their Section 7 ranges (checked 2026-10-19 with `tools/count_words.py`). T14 is at 798 of 800.
- Study Mode counts match the index for answers not changed in study. Audit notes are at the end of each file under `## AUDIT NOTE (IADT 2020, checked 2026-10-19)`, so they are outside the Study count.
- Confidence tags [Certain]/[Likely]/[Guessing] remain on contested statements.

## Done (2026-10-19)
1. OneDrive `.docx` built: `MDS III/Answers/Endodontics_14_Traumatic_Dental_Injuries_Answers.docx` (python-docx via `md2docx.py`; 1,641 paragraphs, 210 headings).
2. Answer Bank published as Version 44 (version id 1792352904-f2c4). `publish_guard.py` merge: live 320 entries, merged 344, 0 lost; stale check clean; `verify` printed VERIFY OK (349 files; was 325).
3. Vault: `Question Paper Bank/Answers/Endodontics/Traumatic Dental Injuries/` and `All Answers (Consolidated)/Endodontics/Traumatic Dental Injuries/` (24 files each, including the audit ledger). The consolidated `00_INDEX.md` and `manifest.json` were replaced by the published merge (no entries removed). 85 index entries from other topics (mostly Endodontics Obturation and Root Canal Sealers) have no file in the vault folder yet; they are in the Answer Bank.
4. Git: pushed to `microleakage-answers` (commits 0ef795c and b50a970). `sources/` is excluded and guarded in `.gitignore`.

## Optional next steps
- Sync the 85 vault files listed above (Vault lag, same as other topics).
- Revision candidates: the IADT 48-hour repositioning window (Fouad et al, 2020, p.333) for T13 and T14 when exam length allows.

## Scope calls
- T05: the 1991 "Fractured teeth" entry has only a title; the scope is inferred and stated.
- T08: "Class IV" read as Ellis Class IV (non-vital), not a fracture pattern.
- T18: "transplantation" read as autotransplantation.
- T19: Weine's chapter is cited at chapter level only.
- VRF (7m, Apr 2013) left in section 15 and not drafted here.

## Points the IADT text does not settle (kept as textbook, labelled)
- Three-hour rule for open-apex revascularisation (Andreasen): no match in the IADT text.
- Fluoride root treatment (Andreasen): no match in the IADT text.
- Doxycycline soak before replantation (Trope, Kahler, Andreasen): the IADT says human studies failed to show a benefit of topical antibiotics.
- Kohli and Lee's "above 95%" partial-pulpotomy success (P1, T01): kept as a narrative-review figure beside Krastl's 70-100% in mature teeth.
- IADT-internal distinction: partial pulpotomy in complete roots for complicated crown fractures (p.320) versus pulp removal for mature crown-root fractures (p.322). Stated in T01, T05, P1.

## Sources
- IADT 2020 Part 2, avulsion (Fouad et al): `sources/guidelines/Dental_Traumatology_-_2020_-_Fouad*.txt`. Printed = PDF + 330.
- IADT 2020 Part 1, fractures and luxations (Bourguignon et al): `sources/guidelines/Dental_Traumatology_-_2020_-_Bourguignon*.txt`. Printed = PDF + 313.
- Other supplied PDFs: see `AUDIT_IADT_2026-10-19.md`, scope section.
- Textbooks: Andreasen 2007 (Ch.8-32 as cited); Berman et al (OneDrive copy, `sources/berman_guide.txt`); Sikri Ch.26; Harty's Ch.4, 10, 12; Cohen's Ch.21 (Kahler); Trope (Ingle's Ch.12); Endodontic Radiology Ch.6; Grossman's Ch.13; AAE Glossary p.14.
- DCNA (local `Desktop/DCNA articles`): Kohli and Lee 2026; Hexem and Eisler 2026 Parts 1-2; Ogle 2024; Trope 2010.
- Edition years for Berman, Sikri, Harty's, Cohen's, Ingle's and Grossman's are not in the copies held and are cited n.d.

## Known limits
- Citation metadata not confirmed from the journal page: Khandelwal first author initials; Krastl first author; Abreu journal and volume; Huang author list and volume; Kumari volume; Blackledge DOI; Fouad end page (331-342).
- Study Mode 20-mark sections T03 and T06 are within 500-700 at last count (T03 697, T06 665).
- The IADT 48-hour repositioning window (Fouad p.3) is noted in the ledger but not in the exam text, for length.
