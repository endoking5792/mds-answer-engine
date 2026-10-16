# A1. Audit ledger: endodontic_sealers (2026-10-16)

**Marks: n/a (reviewer ledger)**

**Scope:** all 10 answers (Q1-Q8, P1, P2). **Method:** every specific figure, composition, attribution and "textbook X says" claim was extracted and re-checked by text search against the markdown in the private repo `endoking5792/mds-textbooks` (commit `26254fe`). The chapter files used were diffed against the copies in `dental-study-material/textbooks` and are byte-identical.

## Result
- Claims checked: 106. Confirmed in the cited source: 104. Corrected (attribution): 2. Confirmed with a wording or attribution note: 3.
- No figure in the answers failed to appear in the textbook it was credited to, after the two attribution fixes below.
- Search confirms a string is present in the cited chapter; it does not prove the answer's reading of the sentence. The contradictions table (A0 note) was read in context by hand.

## Corrections made in this pass
1. **Q1** Grossman cement setting: source is Grossman's 14e (about 2 h at 37 C, 100% humidity; begins to set within 10-30 min in the canal), previously credited to Azim and Aksel, Berman, Sikri.
2. **Q7** Resilon filler content (about 65% by weight): source is Jain (2016), previously credited to Gatewood and Grossman's.

## Notes that do not change the answers
- N2: Cohen's gives the FDA/"unacceptable under any circumstances" wording; the 1974 ADA Council on Dental Therapeutics classification as "unacceptable" is Ingle's.
- BioRoot RCS "not for warm techniques" is Azim and Aksel only (high viscosity, flow falls with heat).
- Sikri's Nogenol composition is **not** garbled: checked against the printed page (2026-10-16, Niranjan spot-check) and the markdown is a correct transcription (base: zinc oxide, barium sulfate; catalyst: resin methyl, salicylic acid). It differs from Cohen's composition (ZnO, BaSO4, bismuth oxychloride) — the answers (Q5) now show both side by side instead of using only Cohen's.

## What the textbooks cannot verify (needs the journal PDF or print)
- Pameijer and Zmener (2010) figures: push-out 1.33 vs about 8 MPa; EndoREZ tags 400-1000 um; success 91.03% at 2 y and 86.3% at 5 y; Resilon-Epiphany 91.6% and 93.1%; primate inflammation scores. Journal DCNA article only.
- Gatewood (2007) and Guruswamy Pandian (2026): journal articles.
- Torabinejad's MTA book (Ch.10, Fillapex cytotoxicity) is **not in mds-textbooks**; it is in `dental-study-material` only. Add it to the private repo if it should be citable.
- Barborka 2017, Cotton 2008, Tay, Chugal and Lin are cited second-hand through the textbooks.

## Ledger
| # | Answer | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| 1 | Q1 | Grossman criteria: tacky (Cohen Box 9.1) | Cohen's 12e Ch.9 | OK |  |
| 2 | Q1 | Criterion 'very fine powder' present | Cohen's 12e Ch.9 | OK |  |
| 3 | Q1 | ZOE formula 42/27 in Cohen | Cohen's 12e Ch.9 | OK |  |
| 4 | Q1 | Sikri prints 40/30 formula | Sikri 2e Ch.19 | OK |  |
| 5 | Q1 | Grossman formula 42 parts / Staybelite | Grossman's 14e Ch.16 | OK |  |
| 6 | Q1 | ISO 6876 flow over 20 mm | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 7 | Q1 | film thickness under 50 um | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 8 | Q1 | solubility under 3% | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 9 | Q1 | dimensional stability -1 to +0.1 | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 10 | Q1 | radiopacity over 3 mm Al | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 11 | Q1 | AH Plus working time 4 h (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 12 | Q1 | AH Plus extended working time ~4 h (Applied DM) | A Clinical Guide to Applied Dental Materials Ch.13 | OK |  |
| 13 | Q1 | Sikri AH Plus film 22 um / AH-26 39 um | Sikri 2e Ch.19 | OK |  |
| 14 | Q1 | BC sealer initial set 165 min (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 15 | Q1 | EndoSequence BC 5 vs 3 weeks (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 16 | Q1 | extruded material reduces healing up to 25% (Grossman) | Grossman's 14e Ch.16 | OK |  |
| 17 | Q1 | 20% patency after bioceramic retreatment (Jain) | Jain (2016) Ch.5 | OK |  |
| 18 | Q1 | bioceramic retreatment most difficult (Sikri) | Sikri 2e Ch.19 | OK |  |
| 19 | Q1 | BC sealer removal no worse than epoxy (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 20 | Q1 | N2 unacceptable (ADA 1974) | Cohen's 12e Ch.9 | OK* | Wording is in Cohen's (not FDA-approved; 'unacceptable under any circumstances'); the 1974 ADA Council on Dental Therapeutics 'unacceptable' classification is in Ingle's p.22. Answers cite both. |
| 21 | Q1 | Sealapex base ZnO/Ca(OH)2 | Cohen's 12e Ch.9 | OK |  |
| 22 | Q1 | no human clinical studies of calcium silicate sealers (Cohen) | Cohen's 12e Ch.9 | OK | Cohen's: 'no peer-reviewed papers... in human clinical studies' (sealers, tricalcium silicate powders). |
| 23 | Q1 | Sikri: definite classification not established | Sikri 2e Ch.19 | OK |  |
| 24 | Q1 | Sikri lists fifteen requirements | Sikri 2e Ch.19 | OK | Sikri lists 15 requirements and 6 functions; regex missed the heading wording. |
| 25 | Q2 | Hydron first generation (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 26 | Q2 | Sikri fifth generation ADSeal/DiaProSeal | Sikri 2e Ch.19 | OK |  |
| 27 | Q2 | EndoREZ 92.1% at 10 y (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 28 | Q2 | Barborka 56 vs 88 | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 29 | Q2 | 5.3 times higher prevalence | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 30 | Q2 | Resilon withdrawn 2014 | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 31 | Q2 | GuttaFlow working time 15 min (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 32 | Q2 | GuttaFlow cures 25-30 min | Cohen's 12e Ch.9 | OK |  |
| 33 | Q2 | MTA Fillapex 13.2% MTA (Azim/Aksel) | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 34 | Q2 | BioRoot RCS calcium chloride | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 35 | Q2 | BioRoot avoid warm techniques (Cohen) | Cohen's 12e Ch.9 | OK* | BioRoot RCS 'should not be used with warm obturation techniques' is in Azim and Aksel, not Cohen's. Answer cites Azim and Aksel first. |
| 36 | Q2 | BC HiFlow for warm techniques | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 37 | Q2 | calcium silicate sealers under 0.1% expansion | Cohen's 12e Ch.9 | OK |  |
| 38 | Q2 | pH about 12 | Cohen's 12e Ch.9 | OK |  |
| 39 | Q2 | low vacuum 5 s protocol | Cohen's 12e Ch.9 | OK |  |
| 40 | Q2 | nanodiamond gutta-percha (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 41 | Q3 | all cements irritating freshly mixed (Grossman) | Grossman's 14e Ch.16 | OK |  |
| 42 | Q3 | cell culture lacks lymphatics (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 43 | Q3 | AH-26 formaldehyde (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 44 | Q3 | MTA Fillapex cytotoxic and genotoxic | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 45 | Q3 | MTA Fillapex cytotoxic (Torabinejad) | Torabinejad MTA Ch.10 (dental-study-material only) | OK |  |
| 46 | Q3 | paraformaldehyde sealers (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 47 | Q3 | AH-26 overfill paresthesia (Sikri) | Sikri 2e Ch.19 | OK |  |
| 48 | Q3 | iodoform sealers cytotoxic (Sikri) | Sikri 2e Ch.19 | OK |  |
| 49 | Q3 | eugenol effect persists after setting (Common Complications) | Common Complications Ch.6 | OK |  |
| 50 | Q3 | extrusion equivocal (Harty) | Harty's 7e Ch.9 | OK |  |
| 51 | Q4 | resin sealers shrink 7.81% | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 52 | Q4 | C factor 1000 vs 5 | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 53 | Q4 | EndoREZ TEGDMA (Jain) | Jain (2016) Ch.5 | OK |  |
| 54 | Q4 | EndoREZ TEGDMA (Cohen) | Cohen's 12e Ch.9 | OK | Cohen's spells it 'triethyleneglycol dimethacrylate'; EndoREZ contains it (also Jain). Q3 TEGDMA resolution stands. |
| 55 | Q4 | paper point 1 s (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 56 | Q4 | AH Plus noneugenol (Weine) | Weine Ch.7 | OK |  |
| 57 | Q4 | AH-26 formaldehyde (Weine) | Weine Ch.7 | OK |  |
| 58 | Q4 | AH Plus no residual monomer (Applied DM) | A Clinical Guide to Applied Dental Materials Ch.13 | OK |  |
| 59 | Q5 | Nogenol ZnO BaSO4 bismuth oxychloride (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 60 | Q5 | Nogenol from periodontal dressing | Cohen's 12e Ch.9 | OK |  |
| 61 | Q5 | Nogenol expands on setting (Sikri) | Sikri 2e Ch.19 | OK |  |
| 62 | Q5 | Sealapex noneugenol (Grossman) | Grossman's 14e Ch.16 | OK |  |
| 63 | Q5 | colophony sensitisation (Applied DM) | A Clinical Guide to Applied Dental Materials Ch.13 | OK |  |
| 64 | Q6 | Grossman Box 16.8 | Grossman's 14e Ch.16 | OK |  |
| 65 | Q6 | Cohen Box 9.1 | Cohen's 12e Ch.9 | OK |  |
| 66 | Q6 | Harty tubule penetration item | Harty's 7e Ch.9 | OK |  |
| 67 | Q6 | Principles & Practice expands slightly | Principles and Practice (2002) Pt 14 | OK |  |
| 68 | Q7 | Resilon polycaprolactone (Azim/Aksel) | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 69 | Q7 | Resilon 150 C (Grossman) | Grossman's 14e Ch.16 | OK |  |
| 70 | Q7 | gutta-percha 200 C (Grossman) | Grossman's 14e Ch.16 | OK |  |
| 71 | Q7 | Grossman calls it polyurethane | Grossman's 14e Ch.16 | OK |  |
| 72 | Q7 | Epiphany self-cure about 45 min (Jain) | Jain (2016) Ch.5 | OK |  |
| 73 | Q7 | Teixeira fracture resistance superior (Ingle) | Ingle's 7e Ch.22 | OK |  |
| 74 | Q7 | Ingle: not enough stiffness to reinforce | Ingle's 7e Ch.22 | OK |  |
| 75 | Q7 | primer sulfonic acid-terminated monomer (Jain) | Jain (2016) Ch.5 | OK |  |
| 76 | Q8 | dentin modulus 14,000 MPa (Jain) | Jain (2016) Ch.5 | OK |  |
| 77 | Q8 | Tay first described monoblock (Sikri) | Sikri 2e Ch.19 | OK |  |
| 78 | Q8 | primary/secondary/tertiary (Jain) | Jain (2016) Ch.5 | OK |  |
| 79 | Q8 | tertiary example ActiveGP (Jain) | Jain (2016) Ch.5 | OK |  |
| 80 | Q8 | Activ GP a form of monoblock (Harty) | Harty's 7e Ch.9 | OK |  |
| 81 | Q1 | ZOE shrinkage 0.3-1% (Azim/Aksel) | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 82 | Q1 | Grossman cement hardens in about 2 h at 37 C | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | FIXED | Source is Grossman's 14e (about 2 h at 37 C, 100% RH; sets in canal within 10-30 min), not Azim and Aksel. Q1 attribution corrected. |
| 83 | Q1 | AH Plus solubility 0.3% / AH-26 0.5% (Sikri) | Sikri 2e Ch.19 | OK |  |
| 84 | Q1 | GuttaFlow Bioseal PDL stem cells to cementoblast-like (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 85 | Q1 | Cohen cites ISO/Table 9.1 properties | Cohen's 12e Ch.9 | OK |  |
| 86 | Q1 | calcium-containing less toxic than lead/magnesium (Sikri) | Cohen's 12e Ch.9 | N/A | Duplicate of claim 87; attribution to Sikri confirmed. |
| 87 | Q1 | Sikri calcium-containing less toxic than lead or magnesium | Sikri 2e Ch.19 | OK |  |
| 88 | Q2 | tantalum oxide radiopacifier (Azim/Aksel) | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 89 | Q2 | NeoMTA/EndoSeal/Endo CPM named (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 90 | Q2 | Sikri calcium phosphate sealers Sankin Apatite/CapSeal/CEM | Sikri 2e Ch.19 | OK |  |
| 91 | Q2 | ultrasonics sealer distribution (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 92 | Q2 | bioceramic alkalinity up to 7 days (Azim/Aksel) | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 93 | Q3 | MTA Fillapex salicylate resin reduces viability (Azim/Aksel) | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 94 | Q3 | extrusion (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 95 | Q3 | systematic review tricalcium silicate (Cohen) | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 96 | Q3 | systematic review tricalcium silicates similar to MTA (Cohen) | Cohen's 12e Ch.9 | OK |  |
| 97 | Q4 | Sikri five resin generations | Sikri 2e Ch.19 | OK |  |
| 98 | Q4 | Cohen generations | Cohen's 12e Ch.9 | OK |  |
| 99 | Q4 | Jain: four generations | Jain (2016) Ch.5 | OK |  |
| 100 | Q5 | Nogenol catalyst resin/salicylic acid (Sikri, garbled) | Sikri 2e Ch.19 | OK |  |
| 101 | Q6 | Ingle list present | Ingle's 7e Ch.22 | OK |  |
| 102 | Q7 | Resilon bismuth oxychloride (Azim/Aksel) | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |  |
| 103 | Q7 | Resilon 65% filler (Grossman?) | Grossman's 14e Ch.16 | FIXED | 65% filler figure is Jain (2016) p.5, not Grossman's. Q7 attribution corrected. |
| 104 | Q7 | Resilon 65% / Epiphany 70% filler (Jain) | Jain (2016) Ch.5 | OK |  |
| 105 | Q8 | Jain C factor | Jain (2016) Ch.5 | OK |  |
| 106 | Q8 | Jain primary example 'Hydron MTA' | Jain (2016) Ch.5 | OK |  |
