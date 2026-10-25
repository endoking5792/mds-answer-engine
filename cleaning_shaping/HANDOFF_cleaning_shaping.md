# HANDOFF: cleaning_shaping (Roseline, 2026-10-25)

**Status:** FIRST DRAFT COMPLETE in canonical format. 15 repository answers + 3 predicted in `canonical/`, question set agreed with Roseline (`_QUESTIONS.md`). Every exam core is inside its Section 7 range; 689 verbatim locators verified (`python3 locators.py` prints missing 0). Not second-read, not published to the Answer Bank, no vault copy, no .docx.

## Files and exam-core word counts

| Answer | Exam core words |
|---|---|
| P1 | 737 |
| P2 | 366 |
| P3 | 358 |
| Q01 | 3229 |
| Q02 | 3206 |
| Q03 | 1758 |
| Q04 | 870 |
| Q05 | 906 |
| Q06 | 916 |
| Q07 | 329 |
| Q08 | 873 |
| Q09 | 351 |
| Q10 | 362 |
| Q11 | 369 |
| Q12 | 369 |
| Q13 | 358 |
| Q14 | 248 |
| Q15 | 3257 |

## Sources, citations and offsets (see `locators.py` F)

| Key | Chapter | Citation | Offset (printed = PDF - offset) |
|---|---|---|---|
| gro | Grossman's 14th ed Ch.14 | Gopikrishna, 2021 | 25 |
| tor | Endodontics: Principles and Practice 6th ed Ch.14 | Peters, Arias and Shabahang, 2021 | 7 |
| coh | Cohen's 12th ed Ch.8 | Peters, Peters and Basrani, 2021 | none (PDF page only) |
| ing | Ingle's 7th ed Ch.20 | Hülsmann and Schäfer, 2019 (authors from contents list; OCR-damaged extract, locators chosen to avoid damaged words) | -61 |
| siq | Treatment of Endodontic Infections 2nd ed Ch.12 | Siqueira et al, 2022 | none |
| sq18 | Treatment of Endodontic Infections Ch.18 | Rôças and Siqueira, 2022 | none |
| sik | Sikri 2nd ed Ch.16 | Sikri, 2019 | 21 |
| har | Harty's 7th ed Ch.7 | Schäfer, 2017 | 16 |
| gb | Guidebook to Molar Endodontics Ch.7 | Peters and Arias, 2025 | 17 |
| ctx | Current Therapy in Endodontics Ch.3 | Jain, 2016 | none |
| wei | Weine's Endodontic Therapy 6th ed Ch.5 | Weine, 2004 | none (sparse PDF markers) |
| e12, e24 | Endodontology 2nd ed Ch.12, Ch.24 | Baumann and Beer, 2010 (editors; chapter authors not in extract) | 17 |
| gut8, gut10 | Gutmann and Lovdahl, Problem Solving in Endodontics 5th ed Ch.8, Ch.10 | Gutmann and Lovdahl, 2011 | 11 |
| cc4 | Common Complications in Endodontics Ch.4 | Johnson, 2025 | 11 |
| aae | AAE Glossary 2012 | American Association of Endodontists, 2012 | none |

## Source conflicts shown side by side (not resolved)

- Schilder's objectives: Ingle's (5+5, incl. medicament space and one appointment) vs Grossman's (flow; space for obturation) vs Sikri (substrate removal).
- Balanced force angles: six different sets (Grossman's/Cohen's 90°/180-270°; Torabinejad <180°/≥120°; Ingle's 180°/120°; Sikri ¼/¾; Harty's ¼/½).
- Patency file distance: Sikri 2 mm beyond constriction; Harty's 1 mm beyond WL; Siqueira up to 1 mm beyond terminus; Cohen's just through the foramen. Patency value: Peters and Arias/Torabinejad favour; Sikri lists risks; Gutmann and Lovdahl (2011) call it empirical.
- Gates-Glidden drills: not recommended / unsuitable (Grossman's, Torabinejad, Molar Guidebook) vs safe and inexpensive (Ingle's).
- Coronal flaring reduces extrusion: claimed (Grossman's) vs not confirmed (Cohen's).
- Crown-down vs step-back: advantages listed (Grossman's, Sikri) vs no evidence except BF, more ledges in one study (Ingle's).
- NiTi composition 55/45 (Grossman's, Ingle's, Harty's) vs 56/44 (Jain); recoverable strain 8% (Jain) vs 10% (Harty's).
- Yared reciprocation 2007 (Jain) vs 2008 (Grossman's table).
- Glide path test file: #15 (Cohen's) vs #10 (Molar Guidebook); precurved (Grossman's) vs not precurved (Torabinejad).
- Minimum apical size for the needle within one chapter: #25/.06 vs #25/.08 or #30/.06 (Molar Guidebook).
- CHX irrigation: equal to NaOCl (Siqueira; Torabinejad) vs not beneficial (Cohen's, Ng study via Molar Guidebook). MTAD: superior in vitro (Torabinejad) vs no added reduction (Cohen's).
- Sonic frequency: 1500-6000 Hz (Endodontology, Cohen's) vs 2-3 kHz (Grossman's).
- Sikri names the crown-down + step-back combination "modified step-back", a name used elsewhere for apical-box preparations.

## Open points

1. May 2015 (RG PIII RS-3) 20m entry has lost its wording in the repository; placed under Q05 as a guess. Check the scan.
2. Second-reader check not done.
3. Not published to the Answer Bank (Rule 7, publish_guard.py); vault copy not written; no .docx (skill 7.1 item 13).
4. Curved-canal anatomy overlaps Medhinir's `root_canal_anatomy`; Q06 points to it.
5. `[RECALL]` items: pulp stone types, rubber dam timing and champagne test (Q07), guided endodontics (Q07).
