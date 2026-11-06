# Diagnosis in Endodontics: handoff (updated 2026-11-05, after second-reader pass)

Part A: 11 canonical answers in `diagnosis/canonical/`. Drafted by six parallel agents, then checked by six independent second readers who also audited every answer against Harty's 7th ed (2017). Ledgers: `diagnosis/audit/<group>.md`. 1600 locators verified (`python3 locators.py` prints missing 0). Every exam core inside its Section 7 range. Textbook-only (PubMed blocked by this environment's network proxy). Published to the Answer Bank site under Endodontics / Diagnosis in Endodontics (first drafts 2026-11-05, manifest 513 -> 524; reviewed versions republished to the same pages, see HANDOFF.md).

| File | Marks | Exam core | Second reader: checked / corrected |
|---|---|---|---|
| D1 Diagnostic aids in endodontics | 100 | 3441 | ~230 / 7 |
| D2 Pulp testing: sensibility and vitality | 100 | 3256 | ~250 / 14 |
| D3 Molecular diagnostic aids | 50 | 1939 | ~150 / 8 |
| Q07 Differential diagnosis of pain | 10 | 392 | 75 / 6 |
| Q08 Test cavity | 10 | 385 | 43 / 4 |
| Q09 Tooth Slooth | 10 | 387 | 43 / 4 |
| Q10 Endograms | 5 | 188 | 13 / 2 |
| Q11 Diagnosis and treatment planning | 50 | 1820 | ~160 / 11 |
| Q12 Case selection, medically compromised | 20 | 769 | ~95 / 6 (+1 by coordinator) |
| Q13 Case selection, grossly decayed teeth | 10 | 394 | ~50 / 4 |
| Q14 Clinical judgment and evidence-based decision making | 50 | 1966 | ~95 / 6 (+5 RECALL -> SRC) |

## Main corrections from the second read
- Q14: White and Torabinejad call RCT and implants "complementary, not competing"; the real conflict is surgery vs implant.
- Q07: Walton and Torabinejad 2002 Ch.29 is by Graham Rex Holland (contents page); cited as Holland, 2002.
- Q13: biologic width about 2 mm (Gargiulo, cited by Badr); 3 mm is Barsness and Roach's sound tooth above bone.
- Q09: Abbott and Leow 68%/8% applies to cracked teeth with reversible pulpitis (also 15% both, 9% none).
- Q11: AAE point score is Grossman's teaching aid for students, not a referral rule; one AAE grid row corrected; unsourced "vital pulp therapy for irreversible pulpitis" removed.
- Q12: Harty's "an INR of 2.5" sentence is truncated in the extracted file (preceding line breaks off mid-word); the answer says so and does not state the threshold's scope.
- D2/D1: Harty's -50°C for tetrafluoroethane matches Abbott's figure for propane/butane mixtures, so probably misattributed [Likely]; ice temperature now cited to Sigurdsson; rubber-cup and study attributions corrected.
- D3: Siqueira and Rôças 2017 really print 45/32/33 (=110%) on p.103; Cohen's 2021 gives 23. Painless pulpitis figures overlap rather than conflict.

## Open points for Niranjan (check against printed books)
1. Harty's Ch.2 INR 2.5 sentence (truncated in the file).
2. Harty's -50°C tetrafluoroethane (Ch.3); Abbott's spray/dry-ice temperatures (Ingle's p.245, OCR minus signs decoded).
3. Trauma atlas "high specificity" wording (p.261), which by its own definitions should be sensitivity.
4. Endodontic Microbiology p.103 "33%" (probably 23%).
5. Decoded Ingle's author lines (Abbott Ch.8, Bakland Ch.13, Rosenberg, Malek and Okazaki Ch.11, Johnson and Epstein Ch.31, Fouad and Huang Ch.4): consistent letter-substitution decode, worth one glance. Walton and Torabinejad 2002 Ch.4 author unconfirmed.
6. Q14: PICO (Phillips' Science of Dental Materials, EBP section) and GRADE (Vital Pulp Treatment Ch.3, GRADE Working Group legend) accepted as [SRC] by Niranjan 2026-11-05; they support the definitions only. The ESE 2023 guideline's use of GRADE and the named cognitive biases remain [RECALL].
7. Q10 Endograms meaning rests on the Blum et al 2001 paper title only [Likely].
8. "Vital pulp therapy for irreversible pulpitis" needs a source if wanted back in Q11.
9. Full headroom: Q13 394/400, Q14 1966/2000, D1 3441/3500; D2 section 7 is 423 words (short-note size about 400).
10. With PubMed access, primary papers named only "as cited by" the books could be added as [LIT].
11. Part B done 2026-11-06: see the Part B section below.

## Part B (pulpal and periapical pathology), 2026-11-06

7 canonical answers, drafted by four agents (Harty's 7th read from the start), then checked by four independent second readers (ledgers `audit/pa.md`, `pd.md`, `pm.md`, `ps.md`). Published to the Answer Bank site under Endodontics / Diagnosis in Endodontics (added 7, manifest 524 -> 531, 0 lost; site commit d51979a). Whole topic: 18 answers, 2709 locators, missing 0; all exam cores in range.

| File | Marks | Exam core | Second reader: checked / corrected |
|---|---|---|---|
| B1 Periapical pathosis | 75 | 2910 | 261 / 13 (classification section expanded) |
| B2 Diseases of pulp and their etiology | 25 | 994 | ~200 / 17 (shared with B3) |
| B3 Classification of pulpal and periapical disease | 20 | 789 | ~95 / (in B2 count) |
| B4 Inflammatory mediators in pulpal disease | 25 | 999 | 209 / 16 |
| B5 Pathophysiology of apical periodontitis | 10 | 346 | 34 / 3 |
| B6 Periapical cysts | 10 | 398 | ~125 / 10 |
| B7 Sinuses of endodontic origin | 10 | 396 | ~72 / 7 |

Main Part B corrections: Lin and Huang (Cohen's Ch.16) report Nair's "true cysts need surgery" view and then counter it (placed on the "may heal" side, [Likely]); Grossman's 80-98% is resolution of periapical radiolucencies, not a cyst healing rate; Landwehr's 6-55% covers cysts and granulomas together; Ricucci et al argue against osmotic cyst growth; cat-pulp pressures (16.3 vs 7.0 mm Hg) labelled as animal data; Cohen's leukotriene table is a general pain table; IL-6, superoxide dismutase and AAE 2009/2016 "conflicts" were labelling or document differences, not data conflicts; Abbott says reversible pulpitis "will normally require" pulp therapy.

Part B open points:
1. Irreversible pulpitis: pulpectomy (Grossman's, Harty's) vs pulpotomy as definitive in selected cases (Essential Endodontology, Cohen's); B2/B3 give one line each.
2. Phoenix abscess: Grossman's (drain) vs Sikri (no incision) vs Harty's flare-up management (drainage, analgesics, antibiotics; [Likely] same event).
3. Patterson granulomas 84% (Grossman's) vs 20% (Fouad and Khan); Slutzky-Goldberg sinus sites sum to 102%: need the original papers.
4. Sikri errors flagged: cyst called "acute"; marsupialisation called "surgical removal"; "Grossman's classification" not matching the 14th ed; radiographic cyst diagnosis contradicted on his own next page.
5. Near ceilings: B2 994/1000, B4 999/1000, B6 398/400, B7 396/400, B1 2910/3000.
6. Fouad wrote or co-wrote four of B4's eight sources; agreement among them is not independent.
