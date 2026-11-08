# Auditor brief — tooth_bleaching (SESSION_PROMPT.md section 5; parallel audit, 2026-11-08)

You are one of three parallel auditors. Work ONLY on the answers assigned to you, in `/home/user/mds-answer-engine/tooth_bleaching/`. Do not commit or push. First read `_DRAFTER_BRIEF.md` (all its rules still apply), `/home/user/mds-answer-engine/SESSION_PROMPT.md` section 5, and the model ledger `/home/user/mds-answer-engine/corrosion_biocompatibility/audit/AUDIT_2026-11-07.md`.

## Files you may change
- Your assigned `canonical/*.md` answers.
- A NEW locator part file `loc_<id>.py` (your id: u1, u2 or u3). Every new F and L key starts with `<id>_`. You may REUSE existing keys from loc_a1..a5 in an answer's `<!--LOC:-->` line (do not edit loc_a*.py, except to fix a broken phrase, and say so). BOOK: reuse existing keys and strings exactly (`python3 -c` or grep them from loc_a*.py); new keys only for new books.
- Your notes: `audit/notes_<id>.md` (I compile the topic ledger from the three notes).

## What to do, per answer
1. **Second-reader check.** `python3 check_answers.py <your files>`: 0 quotes not found; every exam-core number either has a locator in that answer's LOC line or is acceptable (list number, product name, cross-reference) — say which.
2. **Re-read every exam core** sentence by sentence against the Explanation and its locators. Anything stated without a locator behind it: add a locator, reword to what the book says, or mark `[RECALL]` in the Explanation and soften/remove in the exam core. Remove anything assumed. Check that each (Author, Year) attached to a fact is the book that actually says it (spot-check locators by opening the page).
3. **Textbook audit** against the books the drafters did NOT draft that answer from (each answer's retrieval report lists "Not used"). Look for: (a) facts an exam answer needs that are missing (classifications, concentrations, times, steps, numbers, named techniques); (b) conflicts between books — show them side by side with reasoning; (c) textbook slips — say what is wrong and why. Add locators for everything you add. Before writing that "no book says X", grep all the books.
4. **Keep every exam core in range** (100m 3200-3500, 10m 320-400, 7m 230-280, 5m 160-200). Several 10m answers are near 400 — to add, you must also tighten. Never pad. Additions can go into the Explanation only if the exam core is full.
5. After every edit: `python3 locators.py <id>_` (missing 0), `python3 build_sources.py <your files>` (only YOUR files — never a glob that includes other auditors' answers), `python3 check_answers.py <your files>`.

## Sources
Textbooks at /home/user/mds-textbooks/ (see _DRAFTER_BRIEF.md list). Newly checked out for the audit: Gulabivala & Ng *Endodontics* 4th Ch.11 Management of tooth resorption; Ingle's 7th Ch.15 Pathologic tooth resorption; *Endodontology* Ch.42 Tooth resorption; Sikri *Essentials of Endodontics* Ch.27 Root resorption. Dental-materials books to audit against: Craig's 14th (offset 11) and 11th (offset 10), McCabe & Walls 9th (9), Bhat et al *Science of Dental Materials* 3rd (`Science_of_Dental_Materials.md`, offset per chapter — confirm), Powers & Wataha 10th (12), Phillips' 12th (16), van Noort 4th (15), *A Clinical Guide to Applied Dental Materials* (Bonsor & Pearson), Alani & Patel. Scratch files: use your own subfolder of the scratchpad, `.../scratchpad/<id>/` — other agents share the scratchpad.

## Report back
Concisely: per answer — exam-core words before → after, additions (with source), rewordings/removals, conflicts added, slips found; locators added (missing 0); check_answers result; anything still open. Also write the same into `audit/notes_<id>.md` in the ledger's table style (sections: 1 verification, 2 additions, 3 conflicts, 4 slips, 5 open).
