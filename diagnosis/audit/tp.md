# Second-reader and Harty's audit: group tp (Q11, Q12, Q13), 2026-11-05

Method: every LOC key in the three answers was opened at its PDF page with about 300 characters of surrounding text (script output, not pasted here) and checked against the sentence that cites it. Offsets re-derived from page headers for every chapter used (all as stated in loc_tp.py; Cohen's has no printed page numbers, so None stays). Harty's 7th ed (2017, ed. B. S. Chong): offset 16 confirmed on Ch.1, 2, 3, 14, 15 (PDF 17/27/39/303/323 = printed 1/11/23/287/307). Author lines: Ch.1 Chong; Ch.2 Escudier; Ch.3 Chandler and Chong; Ch.14 Hülsmann and Chong; Ch.15 Mannocci and Giovarruscio.

Ingle's author lines (letter-substitution OCR) decoded with a consistent key: Ch.31 "Bradford R. Johnson, Joel B. Epstein"; Ch.11 "Paul A. Rosenberg, Matthew Malek, Katsushi Okazaki" (the same key decodes "Chapter" in each header). BOOK notes updated; third author no longer "uncertain".

`python3 locators.py tp_`: checked 358, missing 0. Exam cores: Q11 1820 (1700-2000), Q12 769 (680-800), Q13 394 (320-400). No FAILURE DISCLOSURE.

## Q11 Diagnosis and treatment planning (50m)

About 160 cited sentences/table cells checked; 11 corrected, the rest held up.

| # | Location | Finding | Evidence | Action |
|---|---|---|---|---|
| 1 | S6 AAE grid, row C | Minimal column said "None" for trauma; the form lists uncomplicated crown fracture; moderate omitted complicated crown fracture of mature teeth; high omitted complicated crown fracture of immature teeth, cracked tooth | Grossman's Fig 8.13, PDF p.175 | fixed |
| 2 | S6 grid, rows A, B | Checked cell by cell against Fig 8.13 (ASA 1/2/3-5; 1st molar moderate; 2nd/3rd molar high; >30 deg or S; >25 mm; open apex >1.5 mm; extensive coronal destruction moderate; resorption) | PDF p.175 | kept |
| 3 | S6 exam | "refer above 40" stated as a general rule; book scale is for dental students (under 20 student may treat; above 40 not by predoctoral student) and "for educational purposes only" | Grossman's PDF p.176 | fixed |
| 4 | S5 exam | "Both agree that strategic need alone must not dictate treatment": only Grossman's says this | Grossman's PDF p.180 | fixed |
| 5 | S5 explanation | Interpretation "Grossman's a missing first molar, Jain a full arch" misread Grossman's (any terminal second molar; missing first molar is an added case) | Grossman's PDF p.179 | reworded, [Likely] |
| 6 | S8 exam | "strongest negative factor" not in any book; Grossman's says "strong negative influence" | Grossman's PDF p.176 | fixed, locator added |
| 7 | S8 / Synthesis 1 | "Cohen's and Ingle's" on lesion size had only a Cohen's locator | Ingle's Ch.11 PDF p.324 "the size of the radiolucency may a(ff)ect" | Ingle's locator and citation added; conflict confirmed |
| 8 | S8 exam | Lesion-size conflict omitted Sikri's 10 mm side | Sikri PDF p.162 | added |
| 9 | S8 exam | "review at 1 year and up to 4 years" uncited in exam core | Ingle's Ch.11 PDF p.325 | citation added |
| 10 | S9 exam | Reasons for initial referral (prevents accidents, keeps trust) cited to Jain only; they are Johnson et al's | Torabinejad Ch.6 PDF p.119 | citation fixed |
| 11 | S4 explanation | "about a third of the time" for 37.2% | Cohen's Ch.1 PDF p.258 | made exact |
| 12 | S3 table | "or vital pulp therapy in selected cases" for SIP had no source; Harty's says pulp removal is necessary once irreversible pulpitis is confirmed | Harty's Ch.3 PDF p.51 | removed from exam table; explanation gives Harty's view and labels VPT for irreversible pulpitis [RECALL] |
| 13 | Synthesis 2 | Symptoms conflict (Cohen's: sinus tract, pain affect outcome; Grossman's: symptoms do not influence healing) | Cohen's PDF p.593; Grossman's PDF p.177 | conflict confirmed, kept |
| 14 | Synthesis 3 | Sikri "definite impact ... as compared to" coronal restoration vs Cohen's "as important as" | Sikri PDF p.160; Cohen's PDF p.611 | confirmed, kept |
| 15 | S7 | "Markov model", Burry data, 5-7 days vital, 1 week nonvital, 24-48 h acute | Gulabivala PDF p.132; Torabinejad Ch.6 PDF p.112; Cohen's PDF p.621-622 | kept |
| 16 | Stand-alone check | Section 2 gives history, examination, tests and radiographs in compact form (tests named, what percussion means, radiographic rules, CBCT indications); it does not depend on D1 | answer text | kept |

Harty's additions (Q11): Ch.3 delay irreversible treatment until diagnosis is clear; pulp monitoring and watch-and-review options (also in exam core); case assessment forms incl. Canadian Academy of Endodontics; Tooth Restorability Index. Ch.14 emergency: diagnosis first, remove cause, drain, analgesics, adjust occlusion; antibiotics only with swelling and no access to care (exam core phase 1). Ch.1 implants and endodontics complementary; root filling vs coronal restoration "no disagreement that both should be performed well" (third view in Synthesis 3). Ch.15 restorative failures cause more extractions than endodontic ones. Conflict: Harty's Ch.3 vs vital pulp therapy for irreversible pulpitis (see 12).

## Q12 Case selection and medically compromised (20m)

About 95 cited sentences/table cells checked; 6 corrected, the rest held up.

| # | Location | Finding | Evidence | Action |
|---|---|---|---|---|
| 1 | INR figures | Cohen's 3.5 or less (PDF p.577), Ingle's 2.0 to 3.5 and warfarin stopped 2 days before surgery in Russo's cohort (PDF p.867), Torabinejad 2 to 3 (PDF p.40) all confirmed | as stated | kept |
| 2 | Ingle's warfarin | Answer omitted Ingle's own caveat that stopping may raise thromboembolic risk, and the nerve-block INR check; "needs no change" sharpened from "does not usually require" | Ingle's PDF p.867 | fixed, locators added |
| 3 | Diabetes, Ingle's | "need none even for surgery" had no Ingle's locator; Ingle's says surgical procedures in well-controlled diabetics need no prophylaxis and to consider it in poorly controlled ones | Ingle's PDF p.870 | locator added, wording made exact |
| 4 | Exam item 5 | Gopikrishna cited for RCT preferred to extraction in systemic disease without a locator | Grossman's PDF p.180 (leukaemia, haemophilia, radiation necrosis) | locator added |
| 5 | Table, IHD | 0.036 mg epinephrine is Cohen's limit for intermediate-risk patients | Cohen's PDF p.575 | "intermediate risk" added |
| 6 | HIV | 350 (Cohen's PDF p.589) vs 400 (Sikri PDF p.164) confirmed | as stated | kept |
| 7 | Sikri endocarditis | 2 g penicillin V before then 1 g 6-hourly confirmed; correctly flagged superseded by Grossman's single-dose AHA regimen; Sikri's Table 10.1 prints erythromycin "500 gm" (book error) | Sikri PDF p.163 | flag kept and made explicit with citations; book error noted |
| 8 | Pregnancy, radiation, MRONJ, dialysis, seizures, psychiatric drugs, allergy, NSAIDs, BP thresholds, MI 30 days, 6% orofacial pain, HbA1c, 15 g carbohydrate | all confirmed | Cohen's Ch.5; Ingle's Ch.31; Torabinejad Ch.2; Sikri | kept |

Harty's additions and conflicts (Q12, all Escudier, 2017, Ch.2):
- INR: endodontic treatment safe with a stable INR of 4.0 or less (except IANB); warfarin not altered without the anticoagulant team; INR checked within 24 h; Factor Xa inhibitors need no blood test. Fourth INR position added to explanation, table, controversies and Synthesis 1.
- Surgery and IANB "best avoided in cases with an INR of 2.5": the file has lost a symbol (probably ">"); flagged [Likely].
- Endocarditis: NICE 2008 (UK) recommends no antibiotic prophylaxis and no chlorhexidine for dental procedures: conflict with AHA (Grossman's, Cohen's) shown side by side in explanation, table and controversies.
- Steroids: long-term corticosteroid therapy requires cover (double dose, or 100 mg hydrocortisone 1 h before): conflict with Ingle's (no supplementation for nonsurgical RCT) shown side by side.
- Haemorrhagic diatheses: no factor replacement for nonsurgical RCT, may be needed for LA or surgery; haematologist consulted.
- Antiresorptives: IV risk up to 20% vs oral; RCT preferred if restorable; avoid going beyond apex; crown removal and passive root exfoliation.
- Diabetes: more lesions, poorer prognosis (agrees with Cohen's/Torabinejad side). Prosthetic joints: no special risk (agrees).
- Harty's Ch.2 has no pregnancy, HIV or radiotherapy sections.

## Q13 Case selection and grossly decayed teeth (10m)

About 50 cited sentences checked; 4 corrected.

| # | Location | Finding | Evidence | Action |
|---|---|---|---|---|
| 1 | Exam item 3, high-yield | "Biologic width about 3 mm to bone" conflated biologic width (about 2 mm, Gargiulo cited by Badr) with Barsness and Roach's "at least 3 mm of supra-alveolar tooth structure in addition to ferrule height" | Badr PDF p.68; Barsness PDF p.16 | fixed |
| 2 | Ferrule, Badr | Locators were flowchart (figure) fragments; prose says extraction "might be" the solution if adjunct procedures cannot give a 2 mm-high ferrule, and treats when ferrule is at least 2 mm high and 1 mm thick | Badr PDF p.61-62 | prose locators substituted, "might be" kept |
| 3 | Exam opening | "by whom, and how" not in Grossman's | Grossman's PDF p.168 | replaced with the 22% case-selection failure figure |
| 4 | Foschi | Book sentence "questioned unless pre-endodontic restoration cannot be placed" is a garbled double negative; the answer's reading (question RCT if a pre-endodontic restoration cannot be placed) is the sensible one | Common Complications Ch.8 PDF p.203 | kept, noted |
| 5 | Juloski review, orthodontic extrusion slower and better prognosis; crown-root ratio 1:1; attached gingiva 2-3 mm; Jain 1.5-2.0 mm ferrule; GIC substance loss | all confirmed | Restoration of RCT Teeth Ch.1, 3; Jain; Endodontology | kept |

Harty's additions (Q13): Ch.3 restorability judged before treatment, whole restoration removed if in doubt, Tooth Restorability Index (Chandler and Chong, 2017). Ch.15 (Mannocci and Giovarruscio, 2017): ferrule 2.0 mm optimal but evidence laboratory only, and one premolar RCT with fibre posts found no survival benefit: shown side by side with Barsness and Roach's "incomplete ferrule better than none" (exam core item 2); orthodontic band as interim protection; combined endo-perio-restorative rescue; restorative failures cause more extractions. Harty's Ch.15 shows crown lengthening only in a figure caption, so it is not cited for it.

## Open points for Niranjan
1. Harty's Ch.2 INR "2.5" threshold for surgery and IANB: the source PDF should be checked for the lost symbol (">" expected).
2. Vital pulp therapy for irreversible pulpitis: the chapters read (Harty's 2017 Ch.3) say pulp removal is necessary; if the newer AAE/ESE position is wanted, it needs a source read in a later session (now [RECALL]).
3. Ingle's Table 31-6 prints "20 g amoxicillin" (OCR or print error for 2.0 g); not used in the answers.
4. Grossman's Fig 8.13 ASA footnote prints "Class 1" twice (second should be Class 2); not used.
5. Q13 exam core is at 394/400 words: any addition needs a matching cut.
