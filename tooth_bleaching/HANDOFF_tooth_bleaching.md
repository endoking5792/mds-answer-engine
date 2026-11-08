# tooth_bleaching — handoff (Roseline, 2026-11-08)

Conservative Dentistry §19 Tooth Bleaching (24 sittings) + Dental Materials §17 Bleaching materials + Endodontics §31 "Bleaching" cluster and Manipal addendum + Recent Advances §21 discoloration essays. Question grouping in `_QUESTIONS.md` (agreed with Roseline 2026-11-07). Drafted by five parallel drafters (a1-a5, brief `_DRAFTER_BRIEF.md`) and audited by three parallel auditors (u1-u3, brief `_AUDITOR_BRIEF.md`); ledger `audit/AUDIT_2026-11-08.md`.

| File | Marks | Exam core | Absorbs | Site subjects |
|---|---|---|---|---|
| B01_Management_of_Discoloured_Teeth | 100 | 3451 | 12 sittings (100m 2006/2012/2013, 75m 2013/2016, 50m 2023/2024/Mock 2025, 25m 2015/2022, 20m 2009/2018, 5m 2019) | CD, Endo, RA |
| B02_Bleaching_Procedures_in_Conservative_Dentistry | 100 | 3285 | 15m 2003, 10m 2009/2011, 5m 2020 | CD, Endo, RA |
| B03_Aesthetic_Rehabilitation_of_Vital_Discoloured_Anterior_Teeth | 100 | 3435 | 50m 2021, 20m 2008/2020 | CD, Endo, RA |
| B04_Vital_Bleaching | 10 | 399 | 6 sittings incl. case selection 2017 | CD, Endo |
| B05_Night_Guard_Bleaching | 10 | 396 | 2013, DM 2007, Endo 2009 | CD, DM, Endo |
| B06_Non_Vital_Bleaching_Techniques_and_Agents | 10 | 396 | 2006/2007/2009/2016/2022 | CD, Endo |
| B07_Walking_Bleach | 10 | 398 | 7m 2018 | CD, Endo |
| B08_Recent_Advances_in_Bleaching_Materials | 10 | 385 | Endo 2014, 5m 2005, DM 2004 | CD, DM, Endo |
| B09_Complications_of_Vital_and_Non_Vital_Bleaching | 10 | 387 | 5m 2004 | CD |
| B10_Mechanism_of_Action_of_Bleaching_Materials | 7 | 270 | — | CD, Endo |
| B11_Carbamide_Peroxide_in_Bleaching | 7 | 277 | — | CD, Endo |
| B12_Use_of_Lasers_in_Bleaching | 5 | 191 | — | CD |
| B13_Micro_Abrasion | 5 | 194 | — | CD |
| P1_Cervical_Resorption_after_Intracoronal_Bleaching (PREDICTED) | 10 | 394 | — | CD, Endo |
| P2_Effect_of_Bleaching_on_Enamel_Dentin_and_Bonding (PREDICTED) | 10 | 398 | — | CD |
| P3_Classification_of_Tooth_Discoloration (PREDICTED) | 10 | 390 | — | CD |

Site topic name in every subject: "Tooth Bleaching and Management of Discoloured Teeth" (site commit 80c7188; manifest 582 -> 614, 0 lost).

## Locators
`locators.py` merges the part files `loc_a1.py`-`loc_a5.py` (drafters) and `loc_u1.py`-`loc_u3.py` (auditors); every F/L key is prefixed with its part id, BOOK keys are shared (identical strings, checked). 2083 phrases, 0 missing; 1879 of them are used in the answers' LOC lines. `python3 locators.py a1_` checks one part. Set `MDS_TEXTBOOKS=/home/user/mds-textbooks/` (cloud) or leave the `~/mds-textbooks/` default.

## Sources and offsets (printed page = PDF marker - offset; confirmed at 2+ pages per chapter)
- Operative/aesthetic: Sturdevant's 2nd South Asia ed Ch.21 (Ritter et al, 2019; no chapter author) 19; Goldstein's *Esthetics in Dentistry* 3rd ed 2018 — Ch.12 (Kwon and Goldstein) 14, Ch.14 12, Ch.15 11, Ch.21 (Goldstein et al 2018a) 36, Ch.23 (2018b) 36, Ch.24 (West et al) 35; Sikri *Textbook of Conservative and Restorative Dentistry* 2020 (Ch.23/28/32) 19; Bartlett in *Advanced Operative Dentistry* 6; *Composite Veneers* Ch.4 9 (year not printed, cited n.d.); Alani & Patel Ch.3 20. Summitt's 4th ed Ch.16 (Haywood, da Costa and Berry, 2013), *Fundamentals of Color* and Bonsor & Pearson print no page numbers: PDF pages only.
- Endodontic: Grossman's 14th Ch.23 25; Ingle's 7th Ch.40 -166 and Ch.15 -48; Torabinejad *Endodontics: Principles and Practice* Ch.17 7; Walton & Torabinejad 2002 Part 23 15; *Endodontology* Ch.44 and Ch.42 17; Sikri *Essentials* Ch.24 and Ch.27 21; Andreasen Ch.33 16; Gulabivala & Ng Ch.11 9. Cohen's 12th Ch.26 (Setzer) and Ch.18: PDF pages only.
- Materials: Craig's 14th 11; Craig's 11th 10 (Ch.5) and 9 (Ch.8); Phillips' 16; Powers & Wataha 12; van Noort 15; Bhat et al Ch.7 33; *Lasers in Dentistry* Ch.2 11, Ch.7 9, Ch.9 8, Ch.16 5.

## Points to note / open
- Book conflicts are shown side by side in the answers; the main ones (10% CP yield across nine books; CP activity 40-90 min to 10 h; barrier thickness/level and gutta-percha removal across 11 books; delay before bonding 24 h to 4 weeks; calcium hydroxide after bleaching; cervical resorption incidence, incl. Cohen's 18-25% given without study type vs Summitt's animal data; in-office heat; first report 1848 vs 1864) are listed in the audit ledger §3.
- Textbook slips flagged in the answers: Grossman's "Jordon and Boskman", "faster than microabrasion" (= macroabrasion), 3.5% vs 3.4% on facing pages; Cohen's "sodium peroxide" (= perborate) and 3.5% vs 4%; Sikri Ch.27 "mostly transient" for ECR; Lasers Fig. 16.18 "reduction"; "reflect less light" (Bonsor & Pearson, Alani & Patel); Andreasen Ch.29 "10% hydrogen peroxide" in trays.
- To verify against printed books: Ingle's Ch.40 and Ch.15 author lines (decoded from damaged OCR); Torabinejad 6th ed year; Sikri *Essentials* 2019 year; Phillips' year; *Composite Veneers* year; *Modern Operative Dentistry* bleaching passage author (Torres et al, 2020).
- B01 Section 12 "informed consent" line (Goldstein) is a paraphrase without a locator. Sodium chlorite (B08) stays [RECALL]: no book mentions it. No live literature search was run (a limitation for B08 "recent advances").
- Little headroom: B04 399, B07 398, P2 398 — any addition needs a cut.
- Cross-referenced, not answered: "principles of esthetic dentistry + restoring esthetics in discoloured anterior teeth" 75m 2016/2019 and 50m Mock 2023 (Esthetic Dentistry topic); laminates for discoloured teeth 7m 2020 (Esthetic/veneers); white spot lesions (Non-Carious Defects / MI); lasers in general (Lasers topic).
