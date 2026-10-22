# Procedural errors & mishaps: handoff (2026-10-22)
Question set: `_QUESTIONS.md` (agreed with Niranjan; Q05 Perforation and Q09 Ledge are 100m; Harty's added).
Format: canonical answers written directly (no Study/Exam drafts) in `canonical/`.

| File | Marks | Status |
|---|---|---|
| Q01_Procedural_Errors_in_Endodontics_and_Management_75m_CANONICAL | 75 | Updated with Torabinejad 6th ed Ch.18; exam core 2947 words |
| Q05_Perforation_and_its_Management_100m_CANONICAL | 100 | Drafted; exam core 3453 words (absorbs perforation-materials 7m) |
| Q09_Ledge_Causes_and_Management_100m_CANONICAL | 100 | Drafted; exam core 3385 words; sources Cohen Ch.20 (Terauchi and Renton), Torabinejad 6th, Ingle Ch.23, Molar Guidebook Ch.11 (Berutti and Castellucci, marker-20) |

Tooling: `python3 locators.py` (verifies every phrase), `python3 build_sources.py canonical/<file>` (word count, SOURCE LIST, REFERENCES).
Offsets: Grossman Ch.17 marker-25; Walton Ch.18 marker-15 (file truncated at "Apical perforations"); Harty Ch.14 marker-16; Common Complications Ch.5/6 marker-11; Cohen Ch.10, Ingle Ch.23, AAE Glossary: PDF page only.
New sources for Q05: Endodontology Ch.43 (Baumann and Beer 2010, marker-17); Hülsmann and Schäfer Ch.17 (PDF page only, rough OCR); Torabinejad 6th ed Ch.18 (Nosrat et al 2021, marker-7, COMPLETE chapter, use it to strengthen Q01 later); Ingle Ch.23 perforation pages (marker+85 verified at PDF 699-703); Bioceramics Ch.3 (Atav et al 2024, marker-30). Cohen Ch.20 (Terauchi and Renton) has a full ledge section: use for Q09. 335 locators verified (all answers).
Source conflicts flagged in Q05: incidence 1-3% vs 3-10% (OCR); Endodontology 'main advantage of MTA is its long setting time' treated as a wording error.
Open points: Ingle Ch.23 authors decoded (Machtou, Ruddle); Harty 7e year not verified; Walton chapter incomplete (no separated-instrument/obturation/VRF sections); VRF, NaOCl prevention details and recall intervals tagged [RECALL].


| Q02 detection/correction/prevention 20m | 20 | 698 words |
| Q03 cleaning and shaping 20m | 20 | 735 words |
| Q04 curved canals 20m | 20 | 730 words |
| Q07 instrument separation 25m | 25 | done |
| Q08 retrieval devices 10m | 10 | done |
| Q10 iatrogenic errors 10m | 10 | done |
| P1 zip/elbow/strip 10m, P2 obturation mishaps 10m, P3 prevention advances 10m (PREDICTED) | 10 | done |
PUBLISHED 2026-10-22: Answer Bank Version 54 (additive via publish_guard merge; manifest 380 -> 392, 0 lost, live manifest identical to the file sent). Vault: copied to Answers/Endodontics/Procedural Errors and Mishaps/ and the consolidated folder (vault manifest/index not regenerated, Rule 7). Not committed to git. Note: build_sources.py exam-core regex accepts ## or #### headings. Then publish (Answer Bank + vault).
