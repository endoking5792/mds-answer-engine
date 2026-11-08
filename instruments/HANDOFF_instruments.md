# Instruments and Instrumentation: handoff (drafted 2026-11-03; second-reader check done and corrections applied 2026-11-08)

Status: 14 canonical drafts in `instruments/canonical/` (I1-I11 from the printed questions, P1-P3 predicted), all exam cores inside their Section 7 ranges, 476 verbatim locators verified against `mds-textbooks` (0 missing). Question set and absorbed wordings: `_QUESTIONS.md`. Defaults accepted by Medhinir on 2026-11-03 (cross-reference only for topics already answered elsewhere; ultrasonics from section 29 included; I11 its own 20m answer; I1 100m and I2 75m; P1-P3 as listed; textbooks only; E-speed item moved to Imaging).

| File | Marks | Exam-core words (range) |
|---|---|---|
| I1 Rotary endodontics | 100 | 3487 (3200-3500), at the ceiling; assembled from sections of I2-I6 and I11 |
| I2 Role of automation | 75 | 2568 (2550-3000), at the floor |
| I3 Journey of instruments | 50 | 1705 (1700-2000), at the floor |
| I4 NiTi metallurgy | 50 | 1711 (1700-2000), at the floor |
| I5 Rotary vs reciprocating | 25 | 880 |
| I6 Design features | 25 | 879 |
| I7 Classification and standardization | 10 | 322 |
| I8 Ultrasonics and sonics | 25 | 876 |
| I9 Self-adjusting files | 10 | 334 |
| I10 Retreatment files | 10 | 346 |
| I11 NiTi separation factors | 20 | 717 |
| P1 / P2 / P3 predicted | 10 each | 324 / 360 / 327 |

Sources and offsets (`locators.py`): Sikri Ch.11, 12, 16, 20 (printed-page offset 21 for Ch.11 and 12), Baumann and Beer Ch.9, 10, 12, 15, 20, 21, 22, Jain Ch.3 (offset 26), Peters et al (Cohen Ch.8), Terauchi and Renton (Cohen Ch.20), Roda et al (Cohen Ch.10), Nusstein (Endodontic Irrigation Ch.10, offset 14), Ingle Ch.20 and 23 (OCR damaged: only clean phrases located, no page numbers cited). Other chapters cite PDF page only.

Open points
- **Tango-Endo** is covered only by the two web-search summaries described above; check the primary papers.
- **Newer systems after about 2016** are covered only as far as Cohen's 12th edition. No web search was run (literature hosts were blocked in the cloud session).
- **Book disagreements shown side by side, not ranked:** Racer date (1950s vs 1958), K-file date (1904 vs 1915), K3 passive vs active, whether torque-controlled motors reduce fracture, the cutting direction of reciprocating files (Sikri: counterclockwise; Cohen's sentence says clockwise), the reversible NiTi strain (about 7% vs 8%), whether NiTi is "not heat treatable", and which files are more susceptible to torsion (Jain vs Terauchi and Renton).
- **Overlap by design:** I1 repeats text of I3-I6, I11 and I2 so that it stands alone; edit all together if a fact is corrected.
- "Gauging and tuning" was answered inside I7 as an apical-size concept (Sikri Ch.16); confirm this is wanted.
- Not done: vault and OneDrive copies. PUBLISHED 2026-11-07 to the Answer Bank site (https://mds-answer-bank.pages.dev), Endodontics / Instruments and Instrumentation, 14 answers, manifest 551 -> 565 entries, 0 lost.


## Second-reader check (2026-11-08)
Five independent readers (read-only) checked every cited sentence of the 14 answers against the chapters, for meaning and not only for the verbatim phrase (reports kept outside the repository because they quote the books). I verified the disputed points in the books before changing text. High and medium findings were applied; some low-severity wording points were not (for example, extra detail in I8 on Mayer 2002, and a few attribution refinements), so a further light edit pass is possible. Main corrections:
- I2: torque-controlled motors: Jain and Baumann and Beer credit them with fewer fractures, Peters et al doubt it for cyclic fatigue (I had wrongly cast Jain as neutral); Rollins 1889 (Ingle) vs 1899 (Baumann and Beer); timeline dates that no book gives removed.
- I3: Racer described by Ingle as reciprocal, by Baumann and Beer as purely vertical; WaveOne in Sikri's third and fourth generations; NiTi 1988 was hand files, rotary from the early 1990s; M-wire 2007, GTX 2008.
- I4: books disagree on NiTi strength (Sikri lower, Jain greater); the 400% figure is Jain's report of a study, not in Peters; electropolishing evidence is contradictory (Peters); "martensitic files deform visibly" reduced to an inference.
- I5: debris extrusion and separation now sourced (Terauchi and Renton, Sikri, Ingle) with the conflicts shown; Sikri's list of disadvantages applies to automated devices generally; glide-path disagreement stated.
- I6: Sikri contradicts himself on NiTi fracture; Profile 29 wording; taper up to 19%.
- I8: Baumann and Beer (2010) is the earlier book, Sikri (2019) the later; mechanism paragraph rewritten; "pulp stones" removed.
- I9: obturation limitations and the call for further studies come from Ingle (no longer [RECALL]); vibration units differ between books.
- I10: the D1/D2/D3 thirds sequence is the manufacturer's, tagged [RECALL]; I11, P1, P2, P3 attributions corrected; P3 now uses Jain's TRUShape section.
- I1 was rebuilt from the corrected sections; the speed-and-torque section was dropped to stay inside 3500 words.

Tango-Endo (named in the Mock 2025 wording): added to I4 section 6 from two web-search summaries only (a 2017 fatigue study calling the files conventional NiTi, and a clinical article calling the shaper stainless steel). Neither page could be opened because the hosts are blocked in the cloud session. The note says the premise "heat-treated Tango-Endo" is not supported by these sources. Verify against the papers before relying on it.
