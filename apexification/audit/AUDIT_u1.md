## Auditor u1 notes — apexification Q01 (2026-11-09)

Scope: Q01 "Open Apex – considerations and management" (75m). Second-reader check of the draft and textbook audit against the books the drafter did not use. New locator file `locators_U1.py` (10 F keys, 8 BOOK keys, 89 L keys, all `u1_`). In `locators_Q01.py` only the Endodontology citation string and five BOOK reference strings were corrected (details in section 5). No other file was edited.

### 1. Verification

| Check | Result |
|---|---|
| `python3 locators.py u1_` / `q01_` | 89 checked, missing 0 / 377 checked, missing 0 |
| `check_answers.py` quotes not found | 0 before, 0 after |
| Exam-core numbers without a locator | none before, none after |
| Exam-core words (before → after) | 2859 → 2998 (range 2550-3000); no FAILURE DISCLOSURE. Headroom is now 2 words |
| Cuts made to fit the additions | duplicate AAE blunderbuss sentence in the introduction; Sikri/Grossman second definitions of apexogenesis; the buccolingual sentence in section 3 (kept in section 4); the Matrix/Obturation/Restoration rows of the section 10 table merged into one row pointing to sections 8, 11 and 12; one- and two-visit percentages in section 8; the "Main problems" row in the section 13 table; Harty's duration figure; shorter drawbacks, cervical-fracture and REP protocol lines |
| Exam-core statement without support, removed | Section 13 table: "MTA plug — fracture risk lower (short calcium hydroxide exposure)". The answer's own Critical synthesis says no book shows this clinically. Replaced by "Thin root remains (Kim, 2016)" |
| Cvek "frequent change" slip (drafter flag) | Opened Andreasen Ch.22 PDF p.642 (printed p.626): "frequent change of calcium hydroxide (ie. more than 5 months between shifts compared to less than 5 months)". The sentence contradicts itself, but the book alone cannot show *which* half is wrong. The drafter's reading ("the parenthesis is reversed") was stated as [Likely]; it is now [Guessing]. The cited study is probably Finucane and Kinirons 1999 (list no. 333), but the in-text numbers here are off by two (the monkey study cited as 332 is list no. 334). Walton's chapter cites the same paper (ref 12) only for "barrier formation occurs more rapidly when the apical opening is less wide" |
| Cohen's Ch.12 vs Ch.21 on fracture (drafter flag) | Confirmed by reading both pages. Ch.12 (Diogenes, Simon and Law): Ca(OH)2 "has the potential to reduce root strength" (7 refs), 23% fractured within 18 months. Ch.21 (Kahler): "not conclusive", "fracture may be more related to the stage of root development". A real difference of emphasis between chapter authors. The 23% (ref 152) and the 30% (ref 120) are different studies. Ch.21's sentence is truncated in the book ("...positive and negative controls and that fracture.") — added as a slip |
| Ingle's Ch.28 author decoding (drafter flag) | Confirmed letter by letter: the cipher maps the same letters the same way in "Chapter" (C!"#$%&) and in the author line S!"!&'(! S!")"!"*+ (h=!, a=", r=&), giving Shahrokh Shabahang; the contents page (front matter line 176-178) prints "Shahrokh Shabahang". The same method gives Ch.27 = George Bogen, Nicholas P. Chandler and Ch.29 = Anibal R. Diogenes, Anthony J. Smith (both also in the contents page) |
| Reference strings (front matter checked) | Torabinejad 6th: © 2021 Elsevier, editors Torabinejad, Fouad, Shabahang — "verify" note removed. Grossman 14th: © 2021 Wolters Kluwer Health (India), editor Gopikrishna — OK. Cohen's 12th: © 2021 Elsevier, Berman, Hargreaves, Rotstein — OK. Harty's 7th: © 2017 Elsevier, editor Chong — OK. Gulabivala and Ng 4th: © 2014 Elsevier Ltd, Edinburgh — place added. Gutmann 5th: © 2011 Mosby — OK. Weine 6th: © 2004 Mosby — OK. Sikri 2nd: CBS, second eBook edition 2019 — "verify" note removed. Glossary: 8th edition, 2012 — confirmed in its introduction. Bioceramics in Endodontics: ed. Chopra, © 2024 Wiley, Hoboken — OK. Andreasen 4th: © 2007 Blackwell Munksgaard — OK. Ingle's 7th: no copyright page in the extract; PMPH-USA, Raleigh, 2019 kept as used elsewhere in the repository (open) |
| Endodontology Ch.46 authorship | The draft said "no chapter author in the file". The contents page (front matter line 1015-1018) names **V. Buerkle, N. Meissner**. All 40 in-text "(Baumann and Beer, 2010)" changed to "(Buerkle and Meissner, 2010)"; reference now "Buerkle V, Meissner N. ... In: Baumann MA, Beer R, editors". The English edition is a translation of the 2nd German edition (© 2010 Thieme); "2nd ed" kept with that note |
| [RECALL] apical zipping as a cause | Replaced. Torabinejad Ch.18 (Nosrat, Terauchi and Torabinejad, 2021, PDF p.399 = p.392): incorrect working length causes "zipping" or "blowing out" of the apical foramen. Added to the iatrogenic row of the causes table |
| [RECALL] Cvek five-stage scale | Replaced. *Vital Pulp Treatment* Ch.9 Fig. 9.3 (Widbiller and Galler, 2024, PDF p.208 = p.187): "Stages 1–5 of root development according to Cvek et al.", stages 1-4 maturing, stage 5 complete. The book does not define each stage; the answer gives only this |
| Developmental/pathological/iatrogenic disclosure | Kept; it is still this answer's grouping. Walton and Torabinejad Ch.22 now cited as the nearest support: an immature open apex is "normal", and an open apex "may develop also" from resorption of a mature apex after orthodontic treatment, from periradicular inflammation or "as part of healing after trauma" |
| Offsets confirmed (two pages each) | Walton Ch.22: 15 (PDF 403 = p.388, 405 = p.390). Vital Pulp Treatment Ch.9: 21 (206 = 185, 207 = 186, 211 = 190; Ch.8 in the same file is 20, not used). Endodontic Prognosis Ch.5: 9 (74 = 65, 89 = 80). Essential Endodontology Ch.11: 10 (338 = 328, 339 = 329). Current Therapy Ch.11: 26 (297 = 271, 298 = 272). Ingle's Ch.27: −100 (785 = 885, 786 = 886). Ingle's Ch.29: −111 (824 = 935, 825 = 936). Torabinejad Ch.18: 7 (390 = 383, 400 = 393). Cohen's Ch.24: no printed pages (None) |

### 2. Additions per section (source)

| Section | Added (source) |
|---|---|
| 1 | Open apex normal in a developing root, problem when the pulp dies early or a mature apex resorbs; newer terms "vital pulp therapy" and "root-end closure" (Pitt Ford and Shabahang, 2002); apexogenesis/apexification filed under regeneration in the wide sense (Kang and Bogen, 2017) |
| 2 | Apical closure ~3 years after eruption (Pitt Ford and Shabahang, 2002) vs 1-5 years (Kang and Bogen, 2017); Cvek five-stage scale (Widbiller and Galler, 2024) |
| 3 | Orthodontic apical resorption, periradicular inflammation and trauma healing as causes; walls diverge/parallel/converge with stage; dens *invaginatus* named (Pitt Ford and Shabahang, 2002); zipping/"blowing out" (Nosrat, Terauchi and Torabinejad, 2021) |
| 4 | Normal apical radiolucency has a corticated margin, compare the contralateral tooth; nerves damaged with blood supply intact after luxation (Pitt Ford and Shabahang, 2002); greater dentinal permeability of immature teeth (Kang and Bogen, 2017) |
| 5 | Formal indications and contraindications for vital pulp therapy and root-end closure; four alternatives (plug, RCT, surgery — avoid in children, extraction); faster barrier with narrower apex (Pitt Ford and Shabahang, 2002); REP for stages 1-3, both options from stage 4 (Widbiller and Galler, 2024); apex ≥1 mm (Diogenes and Smith, 2019), >1.0-1.1 mm and AAE criteria (Kim, 2016); plug valid for behaviour-management cases (Kang and Bogen, 2017) |
| 6 | Formocresol: internal resorption in primates, replaced by CSCs (Bogen and Chandler, 2019), "embalm" (Kang and Bogen, 2017); shallow pulpotomy 2-3 mm, conventional pulpotomy lower success and calcific metamorphosis, no routine pulpectomy after closure, recall ≥4 years (Pitt Ford and Shabahang, 2002); root-end closure as prognostic marker, compare with contralateral tooth (Bogen, Dammaschke and Chandler, 2021) |
| 7 | Mechanism conflict ("mistaken belief"; debridement and coronal seal critical); barium sulphate 9:1; no Hedstrom filing; IRM; recall 4-6 weeks, remove Ca(OH)2 after 1 year if healing; barrier detected by touch more often than on the radiograph (Pitt Ford and Shabahang, 2002) |
| 8 | Ca(OH)2 1 week, 3-4 mm plug (Pitt Ford and Shabahang, 2002); 4-5 mm plug, manual compaction preferred to ultrasonics, overfill harmless, uncontrolled bleeding → Ca(OH)2 and reschedule (Kang and Bogen, 2017); barrier 5-20 months after a CSC plug (Bogen, Dammaschke and Chandler, 2021); bioceramics equal to Ca(OH)2 (Ørstavik, 2020); plug now the recommended option (Widbiller and Galler, 2024) |
| 9 | REP contraindications (no dam, post needed, ASA ≥3; caution after avulsion, revascularization in ~1/3), no difference in healing/survival between apexification, plug and REP, root growth a secondary goal, follow-up 6/12/18/24 months then yearly to 5 years, no root growth expected at an older age (Widbiller and Galler, 2024); SCAP survive necrosis (Kang and Bogen, 2017); dens evaginatus cases best, no integrated new dentine (Ørstavik, 2020); MTA apexification neither strengthens nor develops the root (Kim, 2016) |
| 11 | Chloroform-softened master cone (Pitt Ford and Shabahang, 2002) |
| 13 | Criteria of success for vital pulp therapy and root-end closure; failure signs and causes (bacterial contamination; trapped infected tissue; undetected root fracture); recall yearly for 4 years (Pitt Ford and Shabahang, 2002) |

### 3. Conflicts (shown side by side in the Explanation)

1. **Does calcium hydroxide induce the barrier?** Cvek, Ingle's: yes, by pH 12.5 / pH more than calcium ions. Walton and Torabinejad: a "mistaken belief"; debridement and coronal seal are what matter. Reconciled as medium vs inducer [Likely] (section 7).
2. **Radiopacifier in Ca(OH)2:** barium sulphate added (Sikri; Walton and Torabinejad 9:1) vs avoid, so washout can be seen (Cohen's Ch.21, Harty's) (section 7).
3. **Hedstrom files:** Weine rasps the walls with a large Hedstrom vs Walton and Torabinejad "not advocated" (perforation of thin walls) (section 7).
4. **Time to completion of root development:** ~3 years (Walton and Torabinejad, Cohen's, Torabinejad 2-3) vs 1-5 years (Kang and Bogen) (section 2).
5. **Ultrasonic compaction of MTA:** recommended (Ingle's) vs manual preferred because of extrusion (Kang and Bogen) (section 8).
6. **MTA extrusion:** >2 mm may retard healing (Ingle's); overfilling the major limitation (Tonini and Garo) vs overfill does not compromise outcome (Kang and Bogen) (section 8).
7. **Barrier time after an MTA plug:** 0.75 months (Pradhan et al in Ingle's) vs 5-20 months, similar to Ca(OH)2 (Cohen's Ch.24). Different end points (immediate artificial stop vs later biological barrier) [Likely] (section 8).
8. **Plug thickness:** now also 3-4 mm (Walton and Torabinejad) and 4-5 mm (Kang and Bogen) added to the 3-5 mm range (section 8).
9. **Recall/dressing change:** Walton and Torabinejad 4-6 weeks then 3 and 6 months, change only if density falls — sides with Cohen's/Harty's "replace only if washed out" (section 7, Claim 3 unchanged).
10. **Stage scales:** Cohen's six stages vs Cvek's five (late stages split differently) — terminology, not a factual conflict (section 2).
11. **Terminology:** apexogenesis/apexification vs "vital pulp therapy"/"root-end closure" (Walton and Torabinejad); Kang and Bogen and Al Khatib and Besner count apexification as a regenerative procedure (section 1).

### 4. Textbook slips

| Book | Slip | Why |
|---|---|---|
| Andreasen 4th Ch.22 (Cvek) | "frequent change ... (ie. more than 5 months between shifts compared to less than 5 months)" | Self-contradictory; which half is wrong cannot be settled; in-text reference numbers in this section are off by two from the list |
| Cohen's 12th Ch.21 (Kahler) | "...compared with positive and negative controls and that fracture." | Sentence truncated in the book |
| Vital Pulp Treatment Ch.9 (Widbiller and Galler) | "barium sulphate, which is often added to MTA as a radiopacifier" | The discolouring radiopacifier of MTA in the other books is bismuth oxide (Tonini and Garo; zirconium oxide in the newer putties) [Likely]; not used in the answer |
| Walton and Torabinejad 3rd Ch.22 | Text names "dens invaginatus"; its own Fig. 22-10 shows dens evaginatus ("evaginatis") | Probably meant evaginatus, the anomaly every other book links to necrosis of immature premolars [Likely]; both anomalies can cause it, so the answer notes it without calling it an error |
| Walton and Torabinejad 3rd Ch.22 | "detected tactically" | Means tactilely (OCR/print), harmless |
| Essential Endodontology 3rd Ch.11 (Ørstavik) | In immature teeth with apical periodontitis "the primary goal is to stimulate completion of apexogenesis", and calcium hydroxide/bioceramics "also predictably achieve this" | Apexogenesis is vital pulp therapy; in necrotic teeth calcium hydroxide and plugs give a barrier, not root length or strength (Torabinejad, Kim) [Likely]. Not used for that claim |

### 5. Corrections to the draft

- Endodontology Ch.46 chapter authors are Buerkle and Meissner (contents page), not "no chapter author"; 40 in-text citations and the reference changed.
- Section 13 exam-core table claimed lower fracture risk with MTA plugs; unsupported, replaced.
- Cvek "frequent change" reading downgraded from [Likely] to [Guessing].
- Two [RECALL] items (zipping as a cause; Cvek's five-stage scale) now have locators.
- Reference strings: Torabinejad and Sikri "verify" notes resolved; Gulabivala place added; Glossary edition confirmed; Ingle's author decoding described.

### 6. Open points

- Exam core is at 2998/3000: any further addition needs an equal cut.
- Ingle's 7th publisher/place (PMPH-USA, Raleigh) not printed in the extract.
- Endodontology "2nd ed": English edition number not printed (translation of the 2nd German edition).
- The other Q-answers (Q02-Q04, P1) may still cite "(Baumann and Beer, 2010)" for Endodontology Ch.46; their auditors should apply the same correction (Buerkle and Meissner) — not edited here.
- Finucane and Kinirons 1999 (direction of the dressing-change finding) not read; no live search.
- Seltzer and Bender Ch.13 MTA vs Ca(OH)2 pulpotomy series (14/14 vs 12/14; calcific metamorphosis 4 vs 2) and Gulabivala Ch.7 85-90% vital pulp therapy success were read but not added for lack of space.
- Cohen's Ch.24 PDF pages only (no printed pages in the extract).
