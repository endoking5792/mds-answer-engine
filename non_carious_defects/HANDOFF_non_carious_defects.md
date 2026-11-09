# Non-Carious Tooth Defects: handoff (Niranjan, 2026-11-09)

Status: REVIEWED and PUBLISHED 2026-11-09 (Answer Bank site 506c0d5; vault copies written).

## Files (canonical/)
| File | Marks | Exam core |
|---|---|---|
| Q01 Non-carious lesions and their management (umbrella, 18 wordings) | 50 | 1857 |
| Q02 Erosion and its management (6 wordings) | 75 | 2785 |
| Q03 Management of cervical lesions (5 wordings incl. ageing population) | 75 | 2769 |
| Q04 Pathogenesis and clinical features of NCCL | 10 | 350 |
| Q05 Non-carious disfigurement; critically evaluate materials for cervical abrasion | 25 | 954 |
| Q06 Restorative options for a Class V restoration | 10 | 363 |
| Q07 Abfraction (5 wordings) | 10 | 396 |
| Q08 Abrasion and abfraction | 5 | 193 |
| Q09 Attrition and its management | 10 | 464 (over range by choice after Gemini duel, 2026-11-09) |
| Q10 Management of wasting disease of the teeth | 25 | 950 |
| Q11 White spot lesions | 25 | 986 |
| P1 Tooth wear indices (TWI, BEWE), PREDICTED | 10 | 399 |
| P2 Dahl concept and localised anterior wear, PREDICTED | 10 | 358 |
| P3 Saliva and pellicle in erosion, PREDICTED | 10 | 391 |

All exam cores inside Section 7 ranges. Drafted by six parallel agents (work/g1-g6; each has its own locators.py and build_sources.py). Merged `locators.py`: 77 source keys, 1319 locators, missing 0.

## Disagreements kept side by side (not ranked)
Abfraction as an entity (Goldstein contradicts itself; Bartlett, Pickard's: unproven) and who proposed it (Grippo 1991 vs Lee and Eakle 1984); brushing delay after acid (30 min / 1 h / ~12 h / unconfirmed); abrasion lesion shape; handedness rule; BEWE thresholds (>= vs >50%, >=14 vs >14, review interval; Singh's bands leave 14 unassigned); critical pH values; juice vs cola erosivity; bulimia age; occlusal adjustment for bruxism and for NCCL; stress vs malocclusion in bruxism; Dahl intrusion/eruption share and time; low-modulus composite in NCCLs; roughening sclerotic dentine; default Class V material (Mount GIC vs Goldstein composite); WSL microabrasion protocol; bleaching white spots; enamel refractive index; WSL remineralisation of lesion body.

## Open points
- "Wasting disease(s)" is not defined in any textbook read; Q10 equates it with tooth wear as [RECALL] and says so.
- No book gives abfraction incidence alone; Q7 gives NCCL prevalence instead.
- Q5 definition of "disfigurement" is an interpretation of Marzouk ([Likely]).
- Smith and Knight 1984 not read (not on PubMed); P1 scoring-against-age statement is [RECALL].
- Sikri prints "Vialati and Belser" (Vailati); kept as printed in Q2.
- All [LIT] items are PubMed abstracts only.
- Summitt cited by PDF page only (no printed page numbers in the file).
- Mount 3e chapters by Mount and Ngo (Ch.7, Ch.9) are still cited as "Mount et al, 2016" (book-level); Q4 splits Kaidonis Ch.1/Ch.4 as 2016a/2016b, other files cite one chapter each as "Kaidonis et al, 2016".
- Still [RECALL]: P2 implants/ankylosed teeth as a Dahl contraindication. Unverified: Sikri's P11-4-for-erosion claim (labelled unproven in Q2).

## Review pass (2026-11-09), main corrections
- Q1: DI management (porcelain anterior / cast metal posterior, Singh); MIH and hypocalcification no longer credited to Singh; Bartlett's halving of wear applies to bonding agents only; Bartlett brushing and fluoride caveats added.
- P1: BEWE level 3 management corrected (Pickard's Table 2.9); Smith and Knight "one of the most cited".
- Q2: vomiting pattern per Kaidonis; "5% fluoride varnish"; stannous fluoride "may offer some protection"; Dahl "2 mm or more of material"; "Vialati [sic]". P3: saliva wording matches Pickard's; Rasputnis 1 µm is the enamel pellicle.
- Q3/Q6: Sturdevant's low-modulus view stated as traditional; Mount and Ngo's GIC preference limited to Site 3.1/corrosion; trans-surgical restoration described as Torres's own flap.
- Q4/Q5/Q7/Q8: Mount Ch.1 credited to Kaidonis et al; RMGI 96.4% is the only 5-year figure; Mount's restoration-loss passage concerns erosion lesions; abfraction shown both ways.
- Q9/Q10/P2: "first" removed from facet claim; restoration indications not over-attributed to Bartlett; "10% of the population"; Dahl 1975 cited via Alani and Patel.
- Q11: "socio-economic status" and fluorescence devices now sourced to Pickard's; unsupported Summitt bracket claim removed.

## DCNA audit (2026-11-09)
Three auditors read 13 DCNA articles in full (all from `~/Desktop/DCNA articles`, chosen by a full-text scan of all 180). All 13 were additive; each is cited [SRC] with PDF locators (printed page offsets confirmed). Brief: `work/DCNA_AUDIT_BRIEF.md`. Merged locators 1319, missing 0; `locators_base.py` now normalises fi/fl/ff ligatures (needed for PDF text).
- Q1, P1, Q2, P3: Wang and Lussi 2010 (erosion mechanism, citric acid chelation, BEWE 2008 table incl. 6-monthly high-risk review, brush-before-acid advice, restoration indications, material degradation), Hara and Zero 2010 (pellicle formation/maturation, dentine critical pH 6.2-6.7), Gonzalez-Cabezas 2010, Fontana et al 2010 (glossary).
- Q3-Q8: Bedran-Russo et al 2017 (adhesive class and isolation in Class V; avoid all-in-one), Fronza et al 2022 (NCCL trials of modified adhesives), Puckett et al 2007, Pfeifer 2017 (self-adhesive flowables: 27/40 unacceptable at 6 months), Yanase and Le 2014 (printed year 2014, not 2013).
- Q10, Q11, P2: Peters 2010, Gonzalez-Cabezas 2010, Fontana et al 2010, Dayo et al 2021, Zhang et al 2017, Wang and Lussi 2010.
- New book-vs-DCNA disagreements shown side by side: most erosive acid (citric vs phosphoric); brush before vs after acid; BEWE review intervals (2008 table vs Pickard's vs Sikri); dentine critical pH (6.2-6.7 vs 6.5); restorative material in erosion; longer etch and roughening of sclerotic dentine; compomers; microfill/flowable in NCCLs; role of brushing in NCCL; fluoride alone vs WSL around brackets; Dayo's shiny/matte activity criterion (probable transposition, flagged).
- Q09 was NOT touched: it was rewritten to the examination-ready standard in another session (Gemini duel; site a277c37). Its two DCNA locators (Fontana, Wang and Lussi on attrition) sit in work/g5/locators.py if wanted. The vault still holds the older Q09.
- Republished: site abb8f56 (13 updated, manifest 636 -> 636, 0 lost); vault Answers + Consolidated copies updated (13; Q02/Q03 also under Recent Advances).
