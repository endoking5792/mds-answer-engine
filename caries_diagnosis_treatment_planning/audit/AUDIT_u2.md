# Audit ledger u2: caries_diagnosis_treatment_planning (second-reader check and textbook audit)

**Auditor:** u2 (parallel auditor, SESSION_PROMPT §6, `_REVIEW_BRIEF.md`). **Dates:** 2026-11-14 to 2026-11-15.
**Answers:** Q05 (25m), Q07 (20m), Q09 (20m), Q13 (10m), Q14 (10m), Q15 (10m), P1 (10m predicted).
**Files edited:** only these answers, their sidecars, their `locators_<QID>.py`, and this ledger. Nothing committed, pushed or published.

## Checks done (every answer)

1. Read the answer against its sidecar ledger line by line. Opened the located page for every statement that looked wider than its locator phrase, and reworded, re-attributed or added a locator.
2. Textbook audit against the standing Conservative books the drafter had not used: Sturdevant 2e SA Ch.2-3, Summitt's 4th, Marzouk, Sikri, Mount 3rd, Garg and Garg *Textbook of Preclinical Conservative Dentistry* (Jaypee 2011; the real "Garg" book, file `Textbook_of_Preclinical_Conservative_Dentistry.md`, offset 7 checked at PDF 70/71/72 and 142/143), Harpreet Singh 2nd, Pickard's Manual 9th, Pickard's Guide 10th (offset 11, Ch.2 PDF 33/34, Ch.5 PDF 97/99), Kidd and Fejerskov 4th, Torres, *Lasers in Dentistry*, *Advanced Operative Dentistry* and *Advances in Operative Dentistry* (no relevant hits in the last two), plus the relevant *Detection and Assessment* chapters.
3. Student file: stands alone; blueprint present on 10/20m answers and matches the headings; Vancouver references numbered by first citation (checked by script); every reference cited and every citation referenced; no audit/locator/[RECALL] material. Reference formats made identical across my seven answers: "Hanover Park, IL" for Summitt's everywhere; page ranges dropped from Q13/Q14/Q15/P1 chapter references, since the other answers do not give them; Kidd and Fejerskov given as "Ch.N." only.
4. `build_audit.py` re-run on each sidecar until clean, and a revision-history row added to each.

## Q05 Advances in diagnosing coronal caries and radiographic diagnosis (25m)

- **Reworded:** Kim's 20-30% is a sensitivity, not "detects only 20-30%"; the unsourced CBCT line ("the safer reading is…") is now attributed to Price, who says it; the reasoning clause in the introduction was shortened.
- **Locators added for statements already there (14):** fluorescence-camera violet light and red display, Midwest LED reflection, xeroradiography selenium plate and edge enhancement, digital radiography taking more images, zoom and edge enhancement, CBCT matching bitewings for unrestored proximal caries, and caries on CBCT only as an incidental finding.
- **Added:** tuned aperture CT and magnetic resonance microimaging as newer radiographic techniques (Garg and Garg, 2011; Singh, 2020). These are listed only, because no book describes them.
- **Conflict shown:** the radiographic visibility threshold, about 30% (Muruppel and Fried) vs 30-40% (Garg and Garg).
- **Slips found:** Garg and Garg label DIAGNOdent "Quantitative laser fluorescence" (noted in the sidecar, shown in Q13).
- **Open:** none. The body-number flags 3.1-3.6 are section numbers and 25 comes from the marks line.

## Q07 Various methods of caries diagnosis and recent advances (20m)

- **Reworded or removed:** the visual-examination item had no source and now follows Garg and Garg's criteria; OCT "from back-scattered light" became "of internal structure"; the unsourced aim sentence was removed.
- **Added:** a "Classification of methods" heading from Garg and Garg (visual-tactile, radiographic including TACT and MRMI, electrical, laser-based), with the blueprint updated.
- **Conflict shown:** drying time, 5 s (Longbottom and Ferreira Zandona) vs 10-15 s for Nyvad scoring (Machiulskiene).
- **Slip:** Garg's laser list confuses DIAGNOdent with QLF (noted only).
- **Cut:** the digital radiography row (covered in Q05) and some diagram and conclusion wording.
- **Open:** none. The flag 20 comes from the marks line.

## Q09 Incipient carious lesion: detection and management (20m)

- **Reworded:** "zones in polarised light" became "in sectioned lesions" (Sturdevant uses quinoline and transmitted light); ICDAS 1 is "95% sound or outer-half enamel"; the adjunct line now covers QLF only, because Kim's sentence is about QLF; "near the gingiva" became "near the gingival margin"; "arrest is always achievable" was softened to reasoning; "watchful waiting = active prevention" is now located.
- **Locators added:** dark zone enlarging with remineralisation, chalky/matt surface and extrinsic stain (Summitt Table 5-4), and others.
- **Conflict shown:** drying time, about 5 s (Cortés et al.) vs 10-15 s (Machiulskiene); Summitt's ">5 s" is noted in the sidecar.
- **Cut:** "standardised bitewings" at review and "toothbrushing" (the Mount locator covers interdental hygiene only).
- **Open:** none.

## Q13 Quantitative light-induced fluorescence (10m)

- **Fixed after the reset:** the answer was 439 words and build_audit flagged a surname "Pro". "Pro" came from "Inspektor Pro (2004)", which the script read as an author-year citation; the device name and its date were taken out. The answer is now 396 words.
- **Locators added:** Muruppel and Fried's 1981 / 488 nm argon statement, so the joint citation is supported.
- **Slip shown:** Pickard's Manual expands QLF as "quantitative laser fluorescence" (Banerjee and Watson, 2011).
- **Conflict added:** clinical role. Kim calls QLF "now available for application in clinical dentistry"; Kidd and Fejerskov say fluorescent tools "only have research interest".
- **Cut:** technique time 1-2 min, device dates, "suits smooth surfaces best" and the plaque-confounding wording.
- **Open:** Kim's given name is OCR'd as "Baek-II" (carried from the drafter).

## Q14 Laser fluorescence-based methods (10m)

- **Conflict added:** mechanism and depth. Pickard's places DIAGNOdent under both light scattering and fluorescence; Sikri says readings "do not relate exactly to the amount of dentinal decay"; Neuhaus and Lussi and Muruppel and Fried correlate the readings with lesion depth.
- **Removed:** Muruppel and Fried's QLF comparison (488 nm; QLF does not correlate with dentine decay). It conflicts with Kim (405 nm; dentine lesions detected), and that conflict is shown in Q13.
- **Cut:** the Hibst and Gall origin; technique steps condensed.
- **Checked:** Sikri's "-9 to 0 = sound" reading matches his "-9 to -0", so the table stands.
- **Open:** none.

## Q15 Dye detection of caries (10m)

- **Added:** Fusayama as the originator (Ferreira Zandoná and Ritter, 2019).
- **Conflict shown (new evidence table):** Singh (2020) calls acid red "the reliable method", staining collagen "of the infected dentin only". Against this: Ferreira Zandoná and Ritter (not a good indicator of bacterial invasion; stains the matrix; should be avoided), Banerjee and Watson, Pickard's Guide 2015 (stains deeper collagen; over-preparation), Maltz et al. (sensitivity 65.1%, specificity 37.6%) and Hilton and Summitt (helps). A reasoning line says the majority view and the mode of action contradict Singh.
- **Slips (sidecar):** Garg and Garg (2011, PDF 143) list "0.2% Propylene glycol", "10% Acid red solution" and "0.5% basic fuschin" as stains. Propylene glycol is the vehicle, and every other book gives 1% acid red. Mount Fig. 8.18 shows false-positive staining of laser-ablated dentine (not added, for length).
- **Cut:** porosity rationale, "needs UV", the green/blue background note, "1970s", "anything porous" and "good evidence lacking".
- **Open:** none.

## P1 ICDAS II and ICCMS (10m predicted)

- **Slip shown:** Sturdevant Ch.3 (Boushell and Shugars, 2019) gives the ICDAS digits in reverse (severity first, restorative status second). The answer tells students to follow the developers' order (Ekstrand and Braga; Caneppele et al.).
- **Dates conflict extended:** ICDAS Foundation convened 2004 (Banerjee and Watson, 2015), alongside 2002 / 2003 / 2005. Sikri's "(2009)" heading is noted in the sidecar only, because its meaning is unclear.
- **Added:** Pickard's mICDAS 0-4.
- **Cut:** the progression figures (2-4 times; over 10 times) and the 9-14 min examination time.
- **Open:** the ICCMS 4D cycle and risk matrix. A re-grep of all Operative books finds ICCMS only in reference lists and in the Detection and Assessment chapters already used, so the point stays open. The flag 10 comes from the marks line.

## Final build_audit lines

- Q05: LOC keys 86, missing 0; quotes not found 0; answer body 998 words (calibration 850-1000 for 25m); cited surnames not in references: none; body numbers without a locator: ['3.1', '3.2', '3.3', '3.4', '3.5', '3.6', '25'] (section numbers and marks line; reviewed).
- Q07: LOC keys 62, missing 0; quotes not found 0; answer body 799 words (680-800); surnames none; numbers ['20'] (marks line).
- Q09: LOC keys 69, missing 0; quotes not found 0; answer body 798 words (680-800); surnames none; numbers none.
- Q13: LOC keys 42, missing 0; quotes not found 0; answer body 396 words (320-400); surnames none; numbers none.
- Q14: LOC keys 41, missing 0; quotes not found 0; answer body 396 words (320-400); surnames none; numbers none.
- Q15: LOC keys 46, missing 0; quotes not found 0; answer body 398 words (320-400); surnames none; numbers none.
- P1: LOC keys 46, missing 0; quotes not found 0; answer body 400 words (320-400); surnames none; numbers ['10'] (marks line).

## Note for the coordinator

`Textbook_of_Preclinical_Conservative_Dentistry.md` is Garg N and Garg A (Jaypee, 1st ed 2011). I cite it as (Garg and Garg, 2011), "Garg N, Garg A. Dental caries. In: Textbook of Preclinical Conservative Dentistry. New Delhi: Jaypee Brothers Medical Publishers; 2011. Ch.4." Other auditors may want the same format.
