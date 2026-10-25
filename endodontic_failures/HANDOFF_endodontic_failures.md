# Handoff: endodontic_failures (Roseline, drafted 2026-10-23, verified and published 2026-10-25)

## Status
VERIFIED DRAFT, canonical format (SKILL 7.1 item 12): 6 repository answers + 3 predicted. Every exam core is inside its Section 7 range. **919 verbatim-phrase locators verified (`python3 locators.py`: checked 919, missing 0).** Second-reader check done (about 1,300 cited sentences re-read against the books by independent readers; all errors found were fixed, see `reviews/`). **Published to the Answer Bank on 2026-10-25 (Version 60, same URL) under `Endodontics/Endodontic Failures and Retreatment/`; merge check 450 -> 459 manifest entries, 0 lost.** NOT done: push to GitHub (Roseline), vault/OneDrive copy; no live literature search (textbook-only).

## Files (`canonical/`)
| File | Marks | Exam core words (range) | Locators used |
|---|---|---|---|
| Q01_Success_and_Failure_in_Endodontics_100m | 100 | 3485 (3200-3500) | 282 |
| Q02_Management_of_Endodontic_Failures_75m | 75 | 2981 (2550-3000) | 409 |
| Q03_Retreatodontics_in_the_Light_of_Recent_Research_25m | 25 | 998 (850-1000) | 113 |
| Q04_Retreatment_Treatment_Plan_and_Management_20m | 20 | 797 (680-800) | 128 |
| Q05_Causes_and_Management_of_Failure_of_Endodontic_Restorations_20m | 20 | 771 (680-800) | 80 |
| Q06_Prognosis_of_Old_Leaky_Deep_Filling_on_Posterior_Tooth_10m | 10 | 393 (320-400) | 30 |
| P1_Persistent_Pain_After_Root_Canal_Treatment_10m_PREDICTED | 10 | 396 (320-400) | 39 |
| P2_Retreat_Surgery_Extract_or_Implant_for_a_Failed_Root_Filled_Tooth_20m_PREDICTED | 20 | 795 (680-800) | 80 |
| P3_Systemic_Factors_Affecting_Prognosis_of_Endodontic_Treatment_10m_PREDICTED | 10 | 398 (320-400) | 35 |

## Tooling in this folder
- `locators.py`, `build_sources.py`: from `templates/canonical_topic`, filled in (file table `F`, 919 phrases `L`, reference table `BOOK`).
- `src/*.md`: the answers as written, with `⟦key,key⟧` markers after each sentence; `make.py src/*.md` strips the markers, fills `<!--LOC: ...-->` and writes `canonical/*_CANONICAL.md`; then `python3 build_sources.py canonical/*.md` adds word counts, SOURCE LIST and REFERENCES. `make.py` is a small helper written for this topic, not part of the repo template; the files in `canonical/` are the deliverable.
- `drafts_superseded/`: the first three Study/Exam drafts (pre-update skill). Do not publish.

## Sources and page offsets
All from `mds-textbooks` (chapterwise). Printed page = PDF marker minus offset where the offset was confirmed at two pages: Ingle ch.23 (-85), ch.33 (-128), ch.34 (-141), ch.35 (-143); Sikri ch.36 (+21); Endodontics: Principles and Practice ch.19 (+7, confirmed at three pages) and ch.22 (+7; checked on the first page only); Endodontology ch.39 (+17, as used for ch.43 in `procedural_errors`; checked at the first page only). Offsets of 7 used for Endodontic Prognosis ch.10, 11, 12 are confirmed on the first page of each chapter only. PDF page only (offset None): Grossman ch.21, Cohen ch.10 and 17, Treatment of Endodontic Infections ch.7, 8, 17, 20, Prognosis ch.13, Gulabivala and Ng 4th ed ch.9, Problem Solving ch.5, Weine ch.1, Walton and Torabinejad Part 21.

## Items to verify against the printed books
1. Ingle ch.34 author (decoded "Goldberg") and ch.35 authors (decoded "Baba and Goodacre"); Ingle ch.23 authors taken as in `procedural_errors` ("Machtou and Ruddle").
2. Edition year/editors used in `BOOK` for Sikri (2017, as used elsewhere in the repo), Endodontics: Principles and Practice 6th ed (2021), Weine (2004), Walton and Torabinejad (2002).
3. Cohen ch.17 and Ingle ch.33 are by the same authors and overlap; each fact is cited to the Ingle page where both say it.
4. Weine's Chapter 1 and Walton's Part 21 are older (2004 and 2002); their figures are labelled as older beside newer sources.

## Disagreements kept side by side (not ranked)
- Heat from ultrasonic post removal without coolant: about 10°C in 15 seconds (Cohen ch.10) vs within 1 minute (Terauchi ch.19); both advise coolant and short intervals.
- Chloroform: no longer recommended (TEI ch.17, Grossman ch.21), small quantity acceptable (Sikri), below health-concern levels (Terauchi ch.19), no harm in limited doses (Endodontology ch.39).
- Retreatment difficulty on the AAE form: highly difficult (Terauchi ch.19) vs at least moderate (TEI ch.17).
- Flare-ups after retreatment: more frequent in some studies (Terauchi ch.19) vs no excess (TEI ch.17); dentinal cracks: more after warm vertical compaction (Terauchi ch.19) vs inconclusive (TEI ch.17).
- Fibre posts: less tooth loss in one study (Terauchi ch.19) vs posts lost more often (Baba, White and Bogen, Prognosis ch.10).
- Biofilm irrigants: NaOCl 2.5-5.25% better than 1% and chlorhexidine ineffective (Terauchi ch.19) vs NaOCl 1% and chlorhexidine 2% equal in one trial (TEI ch.17).
- Prevalence of persisting apical periodontitis in general practice: 36% pooled (Ingle ch.23) vs 25-35% (Endodontology ch.39).
- Retreatment healing: 66% (Ingle 7e, Cohen ch.17), 78% (TEI 2e ch.20), 77.2% pooled / 65% with apical periodontitis / 41% for lesions over 5 mm (Torabinejad ch.22), 92-98% / 74-86% (Friedman and Mor in Cohen ch.10), 10-15% below primary (TEI ch.17), 94% vs 40% (TEI ch.17).
- True cysts: Cohen ch.10 and Torabinejad ch.22 (surgery likely needed) vs TEI ch.7 (heal when infection controlled) vs Weine (heal nonsurgically).
- Coronal leakage vs persistent infection as commoner cause: TEI ch.7 vs Baba/White/Bogen, Hülsmann and Sikri.
- Lesion size: Ingle ch.33 (OR 2.2), Malek and Lin (retreatment only), Weine (large lesions heal well).
- Focal infection theory duration: 50 years (Ingle, Cohen) vs 40 years (TEI).
- Sikri ch.36 states "the percentage of success ... ranges from 10 to 50% globally": contradicts every outcome source; treated as a probable misprint and not used.

## Open points
- Second-reader verification done (2026-10-24/25); reports and fix logs in `reviews/`.
- No live literature search; "recent research" in Q03 means the 2019-2022 textbook editions.
- Read on 2026-10-23 in a second pass and integrated: Endodontics: Principles and Practice ch.19 (Terauchi, Parirokh and Handysides, 2021), Grossman ch.21 (Gopikrishna, 2021), Endodontology ch.39 (Pontius, 2010). Also read and integrated afterwards: Gulabivala ch.3, ch.5-6, Endodontic Irrigation ch.17, The Guidebook to Molar Endodontics ch.11 (dossiers in `reviews/`). The Endodontology ch.39 author was corrected to Pontius (2010) after checking the chapter.
- Q05 reads "endodontic restorations" as restorations of root-filled teeth; confirm with Roseline's university.
- Answer Bank publish done (Version 60). Still to do by Roseline: commit/push this folder and the WORKFLOW row/HANDOFF line (`FOR_REPO_UPDATE.md`); vault/OneDrive copy.
- Chapter authors to confirm against the printed books: Ingle ch.34 and ch.35, Grossman ch.21, Endodontology ch.39.
