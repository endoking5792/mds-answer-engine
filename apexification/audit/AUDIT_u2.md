# Auditor u2 notes — apexification Q02 (2026-11-09)

Answer: `canonical/Q02_Management_of_Nonvital_Anterior_Tooth_with_Immature_Apex_50m_CANONICAL.md` ("Discuss various methods to manage a nonvital anterior tooth with an immature apex", 50m). Second-reader check (SESSION_PROMPT.md 5.1-5.2) and textbook audit (5.3) against books the drafter had not used: Walton and Torabinejad 3rd ed (2002) Ch.22 and Ch.25; *Current Therapy in Endodontics* Ch.11 (Kim, 2016); Ingle's 7th Ch.29 (Diogenes and Smith, 2019); Sikri 2nd Ch.38; Grossman's 14th Ch.12 (goals, success criteria) and Ch.19; *Vital Pulp Treatment* Ch.9 (Widbiller and Galler, 2024); *Essential Endodontology* 3rd Ch.11 (Ørstavik, 2020); *Treatment of Endodontic Infections* 2nd Ch.14, 15, 20 (Ch.15: Azim and Aksel, 2022); Seltzer and Bender's 2nd Ch.5 (Murray and García-Godoy, 2012); Andreasen's atlas 4th Ch.27 (Andreasen, Andersson and Tsukiboshi, 2007).

New locator file `locators_U2.py`: 12 F keys, 107 L keys, 9 BOOK keys, all `u2_`. 103 of the L keys are in the answer's LOC list. The other 4 (u2_ct_fu, u2_ee_apexog, u2_ee_retrauma, u2_s38_mta) back points in this ledger only. Some u2 L keys point at existing q02_ sources for new phrases in books the drafter had already used. `locators_Q02.py` was edited for reference strings and the Ch.46 citation only. No other file was edited.

## 1. Verification

| Check | Result |
|---|---|
| `check_answers.py` quotes not found | 0 before; 0 after |
| Exam-core numbers without a locator (script) | none before or after. The script only matches numbers against any locator phrase, so every core statement was also checked by hand against the page (rows below) |
| `locators.py q02_` / `u2_` | 337 / 107 checked, missing 0 |
| Exam-core words | 1887 → 1993 (range 1700-2000); no FAILURE DISCLOSURE. Cuts made room for the additions: replacement-interval table merged, duration list shortened, duplicate "Healing" line in section 12 removed (the figures stay in the section 9 table), apex-locator row removed from the section 2 table (it is also in section 4), and other wording tightened |
| Ingle's Ch.28 author | Chapter-opening line is OCR cipher. The contents page (00_Front_matter.md) prints "Shahrokh Shabahang" for Ch.28. Confirmed; locator u2_i28_auth; the "verify" note was removed from the reference |
| Harty's 7th editor | Title page: "Edited by Bun San Chong", 7th Edition, © 2017 Elsevier. Confirmed |
| Torabinejad 6th editors | Title page: Torabinejad, Fouad, Shabahang; © 2021 Elsevier. Confirmed; Ch.10 authors Diogenes, Botero, Kang printed |
| Gutmann 5th | An authored book (Gutmann and Lovdahl), *Problem Solving in Endodontics: Prevention, Identification, and Management*, 5th ed, © 2011 Mosby, Maryland Heights. Reference changed from "In: Problem Solving…" to an authored-book entry |
| Weine 6th | Sole author, © 2004 Mosby, St Louis; Ch.14 has no separate author. Reference restructured (book title first, chapter after) |
| Ingle's 7th imprint | Copyright page not in the extraction (front matter starts at p.ix). "Raleigh: PMPH USA; 2019" is marked "not verified" in both Ingle's references |
| Endodontology Ch.46 | Coordinator correction from the Q01 auditor, checked against the contents page ("V. Buerkle, N. Meissner"). 13 citations "(Baumann and Beer, 2010)" → "(Buerkle and Meissner, 2010)"; F cite and BOOK string in locators_Q02.py now match locators_Q01.py |
| Autotransplantation [RECALL] | Now sourced from Andreasen's Ch.27 (author line printed: "J. O. Andreasen, L. Andersson & M. Tsukiboshi"): growing patients, implants contraindicated, 10-13 years, donor order, 5-year survival 98-99%, 10-year 87-95%. [RECALL] removed |
| Cohen's REP visit-2 timing | Text: "the patient is discharged for 3 to 4 weeks" (PDF p.1627). Box: "Typically 2–4 weeks after the first visit" (PDF p.1629). Ingle's Ch.29, Grossman, Torabinejad and Vital Pulp Treatment all give 2-4 weeks. Explained in the answer: the box is the AAE wording and the text's range sits inside it |
| NaOCl claims | Re-read: Cvek 0.5%; Kahler 0.5%; Kang and Bogen 1.5% for 15-20 min (a Kang locator added, u2_prog_15; before, only Torabinejad's locator backed it); Torabinejad 1.5%; Cohen's 1.5% 20 mL/canal 5 min, needle ~1 mm from the root end; Sikri Ch.25 5.0% + 17% EDTA; Ingle's >20 min. Correct as drafted. Added: 1.5-3% (Widbiller and Galler, ESE) |
| TAP claims | Grossman "0.1–1.0 mg/mL (100–1000 μg of each drug/mL)" and Cohen's "1 to 10 mg/mL" (box: "combined total of 1–10 mg/mL") correct as drafted. Three more values added (section 3 below) |

Exam-core statements reviewed by hand and changed:

| Section | Was | Now |
|---|---|---|
| 1 | Intro (Bakland) had no locator | u2_bak_intro, u2_bak_loss, u2_bak_resorp |
| 1 | "also called revascularisation" credited to the AAE Glossary | the Glossary does not say this; credited to Torabinejad's chapter (q02_t_rep) |
| 2 | "poor crown-root ratio" (no book) | removed; short root credited to Weine |
| 2 | "often inflammatory resorption (Bakland)" | "root resorption" (Bakland's wording) |
| 3 | "intrusion carries most risk of necrosis" plus a sign list credited to Ingle's | Ingle's says intrusion "consistently" lowers blood flow, so necrosis is likely; the sign list moved to Harty's |
| 4 | Large Hedstrom rasp given as standard | conflict with Walton and Torabinejad shown |
| 4 | "needle short of the apex" had no source | about 1 mm (Cohen's box, u2_c12_needle) |
| 5 | Frank 1966 credited to Shabahang | the year is Grossman's (q02_g_frank); credited to Gopikrishna |
| 6 | "BC putty … (Tonini and Garo)" | that chapter has no BC putty as a plug material (only a table row "EndoSequence BC Root Repair"); credited to Azim and Aksel |
| 8 | "Extraction: last resort (Diogenes, Simon and Law)" | Walton and Torabinejad added (it is the last of their four alternatives) |
| 12 | "6 and 12 months … (Kang and Bogen)" had only Torabinejad's locator | Kang locator added (u2_prog_612) |
| 10 | "sealer passes through it (Cvek; Kahler)" | supported by Kahler Fig. 21.19 (u2_c21_sealer) |

## 2. Additions per section (source)

| Section | Added |
|---|---|
| 1 Explanation | Apical closure about 3 years after eruption, against Kang and Bogen's 1-5 years (Walton and Torabinejad, 2002) |
| 2 | Spontaneous cervical fractures from thin walls (Walton and Torabinejad, 2002, Ch.25) |
| 3 | Corticated radiolucency round a normal developing apex, compare the contralateral tooth (Walton and Torabinejad, 2002). **Contraindications to root-end closure**: vertical and most horizontal fractures, ankylosis, very short roots, marginal periodontal breakdown; indication: a restorable necrotic immature tooth; four alternatives (Walton and Torabinejad, 2002). AAE case selection and apex >1.0/1.1 mm (Kim, 2016); 6-8 years, >1.0 mm but 0.3 mm reported (Sikri, 2019, Ch.38); minimum diameter not established (Diogenes and Smith, 2019); 1.1 mm comes from replanted teeth (Murray and García-Godoy, 2012); stages 1-3 for REP, from stage 4 both, a third of replanted teeth revascularise, ASA ≥3 excluded (Widbiller and Galler, 2024); revascularisation unpredictable (Walton and Torabinejad, 2002, Ch.25); traumatised teeth respond less well than dens evaginatus/caries (Ørstavik, 2020). Core: contraindication line; REP selection line |
| 4 | Hedstrom conflict; palatal gingivectomy for rubber dam (Cvek); 1.5-3% NaOCl (Widbiller and Galler); needle ~1 mm (Cohen's) |
| 5 | Walton's "mistaken belief" passive view of the mechanism (side by side with Ingle's); barium sulphate 9:1 (Walton and Torabinejad); Walton's recall 4-6 weeks then 3 and 6 months, change only on density loss, barrier probed at ~1 year; tactile detection of the barrier |
| 6 | 1-week calcium hydroxide before MTA, 3-4 mm plug (Walton and Torabinejad); single-visit bioceramic gives similar results (Ørstavik, 2020); MTA plug "the technique of choice", 3-6 mm, keep MTA away from the crown, BC putty easier to handle (Azim and Aksel, 2022) |
| 7 | **AAE goals** primary/secondary/tertiary (Gopikrishna, 2021; Sikri, 2019, Ch.38), poor predictability of secondary/tertiary goals (Widbiller and Galler), outcome levels (Diogenes and Smith, 2019); visit-2 timing explained; clot level 2 mm below CEJ, pre-bent ISO 30 Hedström (Widbiller and Galler); TAP concentration conflict (5 books), SCAP harm >1 mg/mL, early pastes ~1000 mg/mL, minocycline contraindicated under 8 years (Kim, 2016); calcium hydroxide preferred (Sikri Ch.38); long calcium hydroxide may calcify and hinder bleeding (Widbiller and Galler); ESE follow-up 6/12/18/24 months then yearly to 5 years, orthodontics only after bony healing; healing at 6-8 months, root development at 12-16 months (Sikri Ch.38); Grossman's success criteria and causes of failure; persistent bacteria cause failure; histology bone-/cementum-like (Kim), true regeneration experimental (Ørstavik), tissue source unidentified (Murray and García-Godoy); Jeeruphan comparison: resolution 100/95/77%, 18-month survival 100/95/77%, root-length gain 14.9/6.1/0.4% (Diogenes and Smith, 2019, as reported); no difference in healing or survival (Widbiller and Galler) |
| 8 | Surgery best avoided in children, minimal resection, MTA root-end (Walton and Torabinejad); autotransplantation (Andreasen, Andersson and Tsukiboshi, 2007) |
| 9 Explanation | MTA plug "Neither strengthens the root nor promotes further development" (Kim, 2016); calcium hydroxide apexification "no longer the preferred option", plug now recommended (Widbiller and Galler, 2024) |
| 10 | Sealer expressed through the "Swiss cheese" barrier (Kahler, Fig. 21.19) |
| 11 | Composite partly filling the chamber (Walton and Torabinejad); do not etch over MTA (Azim and Aksel) |
| 12 | Yearly recall to 4 years; **success and failure criteria for root-end closure** (barrier shown radiographically or by tactile probing; failure signs: persistent signs, no barrier, continual calcium hydroxide loss, granulation-tissue bleeding short of the apex; cause bacterial contamination; late failure from bacteria trapped in the barrier) (Walton and Torabinejad, 2002); 18-month survival 77/95/100% (Diogenes and Smith, 2019), probably the same study as Cohen's 23% fracture figure |
| Retrieval report | Lists the audit books, and the ones searched with nothing usable |

## 3. Conflicts shown side by side in the answer

1. **TAP concentration (REP, section 7):** Kim 0.01-0.1 mg/mL (liquid) | Sikri Ch.38 0.1 mg/mL | Grossman 0.1-1.0 mg/mL | Ingle's Ch.29 ≤1 mg/mL combined or ≤100 μg each drug/mL | Cohen's 1-10 mg/mL. Kim reports SCAP harm above 1 mg/mL. Followed ≤1 mg/mL; Cohen's is the outlier [Likely]. Exam core says so.
2. **Hedstrom file (section 4):** Weine uses a large Hedstrom to rasp the walls. Walton and Torabinejad: "not advocated", it may perforate thin walls. Followed the brush or circumferential K-file [Likely].
3. **Barium sulphate in the calcium hydroxide (section 5):** Kahler and Harty's say no, so washout can be seen. Sikri and Walton and Torabinejad (9:1) add it for radiopacity. A real difference in advice; both shown.
4. **Calcium hydroxide mechanism (section 5):** Ingle's says it is active (pH, alkaline phosphatase). Cvek, Weine, and Walton and Torabinejad ("mistaken belief") say it is passive: disinfection and seal do the work. Same clinical consequence.
5. **Minimum apex for REP (section 3):** >1.0/1.1 mm (Kim; Sikri Ch.38; the replanted-teeth origin per Murray and García-Godoy) against 0.3 mm (Ingle's Ch.29; Sikri Ch.38 itself). Exam core: "about 1 mm or wider; minimum unproven".
6. **REP NaOCl (section 7):** 1.5% (AAE, Cohen's, Grossman, Ingle's Ch.29, Sikri Ch.38) against 1.5-3% (Widbiller and Galler, citing ESE and AAE).
7. **Clot level (section 7):** at least to the CEJ, preferably coronal to it (Cohen's); about 2 mm below the CEJ (Widbiller and Galler); 3 mm apical to the CEJ (Sikri Ch.25).
8. **Calcium hydroxide replacement (section 5):** Walton and Torabinejad (2002) join the "replace only on washout" group.
9. **MTA plug thickness (section 6):** range widened to 3-6 mm (Walton and Torabinejad 3-4; Azim and Aksel 3-6).
10. **REP follow-up (section 7):** ESE schedule (6/12/18/24 months, then yearly to 5 years) added beside Cohen's, Grossman's and Torabinejad's.
11. **Time to apical closure (section 1):** about 3 years (Walton and Torabinejad) against 1-5 years (Kang and Bogen). An average inside a range, not a conflict.
12. **Cohen's visit 2:** text 3-4 weeks against box 2-4 weeks. Internal to one book; resolved in favour of the box.

## 4. Textbook slips

| Book | Slip | Why |
|---|---|---|
| Walton and Torabinejad 2002 Ch.22 (PDF p.415) | "detected tactically" | Means tactilely (by touch). Quoted with (sic) |
| Walton and Torabinejad 2002 Ch.22 (PDF p.410) | "Contradictions include the following" (vital pulp therapy) | Means contraindications. Not quoted in the answer |
| Bioceramics in Endodontics Ch.5 (Tonini and Garo, PDF p.162) | MTA pH "10.2–12.5 three hours after setting" | Ingle's and Bakland: 10.2 at mixing, rising to 12.5 at three hours. Noted in section 6 [Likely] |
| Essential Endodontology Ch.11 (Ørstavik, PDF p.338) | In necrotic immature teeth "the primary goal is to stimulate completion of apexogenesis" | Apexogenesis means root development with a vital pulp (Walton and Torabinejad, and the Q04 definition); the sentence means continued root development by revascularisation. Not used in the answer |
| Sikri Ch.38 (PDF p.656) | TAP 0.1 mg/mL called a "Dilution of 1000 times (or g/ml)" | Kim gives the early pastes as ~1000 mg/mL, so a 1000-fold dilution gives 1 mg/mL, not 0.1. Sikri's two figures disagree [Likely] |
| Grossman's 14th Ch.12 (PDF p.242) | "0.1–1.0 mg/mL (100–1000 μg of each drug/mL)" | Equates a combined concentration with a per-drug one. Three drugs at 100-1000 μg each give 0.3-3 mg/mL combined (Ingle's Ch.29 separates the two: ≤1 mg/mL combined or ≤100 μg each) [Likely] |
| Ingle's Ch.29 extraction (not the book) | OCR swaps "fi" for "1" and "ff" for "2" ("apexi1cation", "signi1cantly") | Locators keep the extraction spelling; the answer paraphrases those passages rather than quoting them |

## 5. Corrections to the draft

- The exam-core attributions listed in section 1 (Bakland intro; REP alias; crown-root ratio; intrusion and sign list; needle position; Frank year; BC putty; Kang and Bogen 1.5% and 6/12-month follow-up; extraction).
- Autotransplantation [RECALL] replaced by a sourced item (Andreasen Ch.27).
- Endodontology Ch.46: Baumann and Beer → Buerkle and Meissner (13 citations, F cite, BOOK string).
- Reference strings: Ingle's Ch.28 (author confirmed, "verify" note removed, imprint marked not verified); Gutmann (authored book, Maryland Heights); Weine (authored book, chapter after the title); Endodontology (chapter authors, editors Baumann and Beer, translation note). Harty's (Chong, 2017) and Torabinejad 6th (Torabinejad, Fouad, Shabahang, 2021) were correct.
- The retrieval report had said "Searched, not used: Ingle's Ch.29 and Sikri Ch.38". Both are now used for case selection, goals, TAP concentration and outcomes, which the 50m question needs.
- HIGH-YIELD lines updated (MTA plug range 3-6 mm; REP goals; TAP ≤1 mg/mL).

## 6. Open points

- Ingle's 7th: copyright page not in the extraction. The place, publisher and year in both Ingle's references are carried over from the draft, not verified.
- Sikri 2nd: front matter prints "Second eBook Edition: 2019", CBS Publishers; the place of publication was not checked.
- The Jeeruphan et al comparison is reported via Ingle's Ch.29; the original paper was not read. That Cohen's 23% fracture study is the same one is an inference.
- The AAE "Clinical Considerations for a Regenerative Procedure" and the ESE position statement were not read directly (no live search); their content comes as the books report it.
- Exam core is at 1993/2000. Only 7 words of headroom are left; further additions need cuts.
- Layout: the answer still has the older structure (Explanation plus Exam core, HIGH-YIELD, DIAGRAMS, COMMON EXAM MISTAKES, MNEMONIC, retrieval report and SOURCE LIST in the student file). SKILL 7.1 item 12 (updated 2026-11-09) asks for one integrated answer with audit material in a sidecar. That is a topic-level decision for the coordinator; it was not changed here.
- Not audited: Gulabivala and Ng 4th ed (Endodontics, Mosby 2014) is in the library but was not on this auditor's list.
