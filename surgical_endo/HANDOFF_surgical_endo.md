# Surgical endodontics: handoff (2026-10-18)

**Topic:** Endodontics §25 (Surgical Endodontics and Periapical Surgery) + Recent Advances §6 + Manipal/TN-MGR addendum. Local repositories only (no Drive document supplied). Claimed in `WORKFLOW.md`. Nothing committed, pushed, copied to the vault or published yet.

**Agreed with Niranjan (2026-10-18):** 11 answers + 2 to 3 predicted. Include "non-microbial causes and healing of periapical lesions" if wanted (he ticked it; see below). Replantation items left out (they sit under Traumatic injuries). Endodontic endosseous implants 5m not ticked, so leave out unless asked.

| File | Marks | Status |
|---|---|---|
| Q01_Surgical_Endodontics_100m | 100 | Drafted; Exam Mode 3201 words |
| Q02_Traditional_versus_Microsurgical_Endodontics_50m (absorbs the 10m/7m/5m/20m/25m microsurgery items) | 50 | Drafted; Exam Mode ~1700 words (check range) |
| Q03_Indications_Contraindications_and_Root_End_Resection_20m | 20 | Drafted; 688 words |
| Q04_Flap_Designs_in_Endodontic_Surgery_20m | 20 | Drafted; 808 words (8 over, trim) |
| Q05_Soft_Tissue_Management_in_Periapical_Surgery_10m | 10 | Drafted; 331 words |
| Q06_Steps_in_Apical_Surgery_25m (absorbs 10m Principles of surgical interventions, technique part of the 15m) | 25 | Drafted; Exam Mode 877 words |
| Q07_Root_End_Preparation_and_Filling_10m (title is the repository wording "Root end preparation and filling"; absorbs the 5m ultrasonic note) | 10 | Drafted; 354 words |
| Q08_Retrofilling_Materials_Critical_Discussion_25m (absorbs the 10m/7m retrofilling, retrograde amalgam and root-end restorative items) | 25 | Drafted; 870 words |
| Q09_Bioinductive_Osseoinductive_and_Osteoconductive_Materials_10m | 10 | Drafted; 352 words |
| Q10_Wound_Healing_and_Repair_after_Periapical_Surgery_10m | 10 | Drafted; 365 words |
| Q11_Surgical_Management_of_Periapical_Cysts_and_Lesions_25m (the "rationale of endodontics" 25m/20m questions now have their own answer, Q12) | 25 | Drafted; 869 words |
| P1_Guided_and_Navigated_Endodontic_Microsurgery_10m_PREDICTED | 10 | Drafted; 350 words |
| P2_Endodontic_Microsurgery_versus_Extraction_and_Implant_10m_PREDICTED | 10 | Drafted; 338 words |
| P3_Complications_of_Periapical_Surgery_and_Their_Management_10m_PREDICTED | 10 | Drafted; 355 words (replaces the suggested bone graft/GTR prediction, which would duplicate Q09) |

**Tooling in this folder:** `locators.py` (F = source files with page offsets, L = verbatim-phrase keys; run `python3 locators.py | grep MISSING`), `build_sources.py` (run `python3 build_sources.py [files]`; regenerates SOURCE LIST, REFERENCES and the word-count disclosure). Each answer needs `<!--LOC: ...-->` and `<!--REF: ...-->` lines (no space after `<!--`). Avoid `¬`, soft hyphens and OCR ligature letters (Ingle's: "4e" = "Th", "3" = "fi", "5" = "fl", "2" = "ff") in locator phrases.

**Page offsets confirmed:** Grossman marker-25 = printed; Ingle Ch.24 marker+89; Torabinejad Ch.9 and Ch.17 marker-13; Harty Ch.10 marker-16; Guidelines (Evans 2012) marker-1; Springer complications Ch.9 marker-11; Cohen's Ch.11 PDF page only.

**Sources read so far:** Grossman Ch.22 (full); Ingle Ch.24 (history, indications, anatomy, flaps, hemostasis, osteotomy, resection, preparation, filling, closure, healing); Cohen Ch.11 (indications, decision making, wound healing, medically complex patients, management of the root end up to line 1445); Harty Ch.10 (introduction to preoperative assessment only); Torabinejad and Rubinstein Ch.9 (full), Ch.17 (outcomes, partial); Evans 2012 guideline; Tsesis 2025 complications chapter (partial). PubMed abstracts: Setzer 2010/2012, Kohli 2018, Pinto 2020, Flynn 2024, Rewthamrongsris 2026, Karlovic 2005, von Arx 2008, Kuo 2026.

**Still to read before the remaining answers:** Torabinejad Ch.10 from the root-end filling heading onward (the first 2/3 is read), Ch.11 (root-end materials, long; read the parts on ideal properties, MTA, calcium silicates, Super-EBA/IRM), Ch.14 (wound healing), Ch.15 (adjunctive procedures: grafts, membranes, PRF); Cohen's Ch.11 from line 1436 (cavity preparation, materials: ZOE, GIC, Diaket, composite, MTA); Endodontics Principles and Practice Ch.20 (Apical microsurgery) and Ch.19; Endodontology Ch.40; Harty Ch.10 rest (materials, regeneration, suturing); Surgical Endodontics Colour Manual; Advances in Surgical Endodontics (Castellucci, short); Weine and Seltzer/Bender if relevant; DCNA articles (see `/Users/niranjan/.claude/skills/dental-study-material` notes: Niemczyk 2010 "Essentials of Endodontic Microsurgery", Lieblich 2012 "Endodontic Surgery", Floratos and Kim 2017 "Modern Endodontic Microsurgery Concepts", Ogle 2011 "Hemostatic Agents", Moore and Haas 2010 "Paresthesias"; these are in `~/Desktop/DCNA articles` or `~/Downloads/DCNA articles`, find via `/tmp/endo_audit/dcna_full_scan.txt` if it still exists).

**Open points for Niranjan:**
1. Q01 Exam Mode is exactly at the lower limit (3201 words); the Study Mode of Q01 is about 2,300 words.
2. Citations for Ingle's Ch.24 are by editors (chapter authors are garbled in the extraction), as in earlier topics.
3. Ingle's gives two different MTA setting times (3 h 45 min and 2.5 to 3 h) in the same chapter; flagged in Q01.
4. Harty 7th ed. publication year recorded as 2017 but not verified from the file.
5. The old "Existing Answers" folder has no dedicated surgical-endodontics answers, so there is no cross-check.
6. Torabinejad and Rubinstein is dated 2019 here; the earlier topic notes a publication-year discrepancy on its own copyright page.
7. "Non-microbial causes of periapical lesions" and "Healing of periapical lesions" (Diagnosis section) were ticked; propose to fold "Healing of periapical lesions" into Q10 and answer "Non-microbial causes" separately later, with the Diagnosis topic. Confirm.

**Added 2026-10-18 (later in the same session):** DCNA full texts of Niemczyk 2010 and Floratos and Kim 2017 were read (locator keys `nie_*`, `flo_*`; they read the PDFs directly in `~/Desktop/DCNA articles`). Q01 Exam Mode now 3201 words (just inside range). Ogle 2011 (hemostatic agents), Lieblich 2012 and Moore and Haas 2010 are extracted to the scratchpad but not yet used; use them in Q06/Q10/Q11.

**Added 2026-10-18 (second session): Q06 to Q11 and P1 to P3 drafted and built** with `build_sources.py` (all Exam Mode word counts inside the Section 7 range; no failure disclosures). `locators.py` has no MISSING keys. Nothing committed, pushed, copied to the vault or published. Q01 to Q05 were not touched (Q04 is still 8 words over, as noted above).

**Sources read this session:** Torabinejad and Rubinstein Ch.10 (to closure), Ch.11 (ideal properties, sealing, marginal adaptation, bioactivity, clinical outcome; the long in vitro biocompatibility and gene-expression sections not read), Ch.14 (full), Ch.15 (full), Ch.4 (cyst sections); Cohen's Ch.11 (root-end cavity and materials, GTR, curettage, postoperative care and complications) and Ch.3 (cyst passage); Endodontics: Principles and Practice Ch.20 (full), Ch.1 and Ch.22 (cyst passages only); Walton and Torabinejad 2002 (decompression figure); Barnes 1984 (cyst enucleation, old text); Ingle's Ch.24 (resection to healing); Grossman's Ch.22 (root-end sections); Harty's Ch.10 (resection to closure); Tsesis Ch.9 (full); DCNA full texts of Ogle 2011, Lieblich 2012, Kinaia 2012. PubMed abstracts only: Torabinejad 2015 (PMID 25306305), Rewthamrongsris 2026 (42457140), Kapoor 2025 (40287086), Wei 2023 (38052782). Not read: Endodontology Ch.40, Advances in Surgical Endodontics (Castellucci), Weine, Seltzer and Bender, Moore and Haas 2010 (not needed for these answers).

**Source disagreements kept side by side (flag for Niranjan):**
1. MTA setting time: Cohen's 2 h 45 min, Ingle's 3 h 45 min (and 2.5 to 3 h in the same chapter), Harty's working time 3 to 4 h, Lieblich 2 to 4 h (Q08).
2. Diaket and cementum: Cohen's says none seen; Torabinejad Ch.11 lists Diaket among materials that may promote cementum (Q08).
3. Suture removal: Harty 48 to 72 h, Ingle's 4 days earliest, Cohen's 2 to 4 days, Jurosky 5 days, Torabinejad Ch.10 up to 7 days, Principles and Practice 3 to 7 days (Q06, Q10).
4. Macrophage timing in oral wounds: Cohen's peak day 3 to 4; Jurosky predominant within 12 h (Q10).
5. True cysts: Cohen's and Principles and Practice Ch.22 say they are less likely to heal nonsurgically; Principles and Practice Ch.1 says there is no direct evidence (Q11).
6. Pecora's membrane trial: Cohen's says nonresorbable membrane, Torabinejad Ch.15 says resorbable (Q09; I cited Cohen's wording and kept the claim general).

**Open points for Niranjan:**
1. Q11 absorbs the two "rationale of endodontics and its role in conservative management of periapical lesions" questions (25m, 20m) through one nonsurgical-first section. They are really a different question (conservative management); a separate answer may be worth drafting if you want full marks coverage there.
2. "Healing of periapical lesions" (10m, Diagnosis section) is not folded into Q10 (surgical wound healing); it needs a decision, as does "Non-microbial causes".
3. P3 swapped from bone graft/GTR to complications (see above).
4. Journal evidence for Q11 (decompression, marsupialisation of large cysts) was not searched; Q11 states this. The recent oral-surgery literature on decompression is the obvious gap.
5. Cohen's and Torabinejad Ch.15 cite the Pecora trial differently (item 6 above).

## Update 3 (2026-10-18, after Niranjan's replies)

**New answers (built, all inside range):**
| File | Marks | Exam Mode words |
|---|---|---|
| Q12_Rationale_of_Endodontics_and_Conservative_Management_of_Periapical_Lesions_25m (25m ABS PII 15-03-2022; 20m Apr 2008 RG PIII RS-2) | 25 | 891 |
| Q13_Healing_of_Periapical_Lesions_10m (RG PIII RS-old; Diagnosis section) | 10 | 340 |
| Q14_Non_Microbial_Causes_of_Periapical_Lesions_7m (Jun 2018, Nov 2013; Diagnosis section) | 7 | 243 (Section 7 has no 7-mark row; range 230 to 280 interpolated at 34 to 40 words per mark, set in `build_sources.py`) |

Q11 was revised: it no longer absorbs the "rationale" questions; PubMed evidence on decompression/marsupialisation and the Pecora trial was added (Q11 Exam Mode 945 words). Q06, Q08, Q09, Q10 now carry **SOURCE CONFLICT** boxes naming the chapter authors.

**Q11 evidence gap: what was found.** PubMed searched 2026-10-18. Abstract-level only: Raabe et al 2026 (retrospective cohort, 40 mandibular jaw cysts, 10 radicular, decompression, volume fell about 5.2%/month); Kader et al 2024 (histology unchanged after decompression in 16/17 radicular cysts); Kaygisiz and Karsli 2024 (59 mandibular cysts over 3 cm, marsupialisation vs enucleation, similar healing by fractal analysis); Wang et al 2024 (J Endod case report, Penrose drain, 4.5-year follow-up); Pecora et al 1995 (RCT of e-PTFE membrane). **No randomised trial or guideline on decompression of radicular cysts was found.** Full text is **not required** for the 25m answer. It would only be worth getting if you want radicular-specific numbers: Raabe 2026 (PMC12918562) and Kaygisiz 2024 (PMC11515537) are open access; Kader 2024 (Ann Ital Chir) and Wang 2024 (J Endod) are not confirmed open; say if you want any of them read in full.

**Source conflicts by author (all are flagged in the answers):**
| Point | Position and author |
|---|---|
| True cysts and nonsurgical healing | Roda, Gettleman, Johnson (Cohen's Ch.10): probably do not heal, need enucleation. Johnson, Fayad, Berman (Cohen's Ch.11): not expected to resolve, surgery. Landwehr (Cohen's Ch.3): limited potential. Setzer, Chogle, Torabinejad (P&P Ch.22): more likely to heal only after surgery or extraction. Lin, Huang (Cohen's Ch.16): says both (less likely, surgery needed; and may regress by apoptosis) with no direct evidence. Sedgley, Silva, Fouad (P&P Ch.1): never any direct evidence; cysts and granulomas heal equally well. (Q11, Q12, Q13) |
| MTA setting time | Johnson et al (Cohen's Ch.11) 2 h 45 min; Rotstein and Ingle chapter 3 h 45 min and 2.5 to 3 h in the same chapter; Gutmann (Harty) working time 3 to 4 h; Lieblich 2 to 4 h (Q08) |
| Diaket and cementum | Johnson et al: none seen; Parirokh and Shabahang: may promote cementum (Q08) |
| Suture removal | Gutmann 48 to 72 h; Niemczyk 1 to 3 days; Johnson et al 2 to 4 days; Jurosky 5 days; Rotstein and Ingle 4 days earliest; Rubinstein and Fayad up to 7 days; Rubinstein, Fayad, Torabinejad 3 to 7 days (Q06; Q05 quotes the Ingle's 4-day figure) |
| Macrophage timing in oral wounds | Johnson et al: peak day 3 to 4; Jurosky: predominant within 12 h (Q10) |
| Pecora membrane | **Resolved by the PubMed abstract:** e-PTFE (nonresorbable). Johnson et al (Cohen's Ch.11) correct; Torabinejad, Lundgren, Tatakis, Fayad (Ch.15) wrong (Q09) |
| Cyst incidence | Said-Al-Naief 22% (36.7% in one series); Sedgley et al 7 to 54%; Roda et al 15 to 42%; Lin and Huang 15 to 20%; Setzer et al 15% (Q11, Q14) |

In-text citations were changed to chapter authors on request (Q01 to Q14 and P1 to P3; reference lists now read "Chapter authors. Title. In: Editors, editors. Book...").

**Still open:** the 7-mark range in Q14 is my interpolation; P3 is complications, not GTR (Q09 covers GTR); Q04 is still 8 words over its range (not touched). Nothing is committed, pushed, copied to the vault or published.

## Update 4 (citations by chapter author)
Changed everywhere, including Q01 to Q05 (citation names only; no content changed): "Berman et al, 2021" is now **Johnson et al, 2021** (Cohen's Ch.11: Johnson BR, Fayad MI, Berman LH); "Chong, 2017" is now **Gutmann, 2017** (Harty's Ch.10; year still unverified); "Rotstein and Ingle, 2019" is now **Torabinejad, Sabeti and Glickman, 2019** (Ingle's Ch.24). Cohen's Ch.3, 10 and 16 were already Landwehr, Roda et al and Lin and Huang. Two things to check: (1) the Ingle's Ch.24 author line is garbled in the extracted file; I decoded it (the substitution cipher is consistent across all three names) to Mahmoud Torabinejad, Mohammad Sabeti and Gerald N. Glickman, so please confirm against the printed book; (2) Grossman's Ch.22 names no individual chapter author in the file, so it stays "Gopikrishna, 2021" (the editor). The two Torabinejad 2019 citations are distinct: "Torabinejad et al, 2019" is the Art and Science Ch.15 and "Torabinejad, Sabeti and Glickman, 2019" is Ingle's. After the change Q04 Exam Mode is 815 words (range 680 to 800; was 808), still carrying its failure disclosure.

## Audit against textbooks: IN PROGRESS (2026-10-18; usage limit reached; no answer files edited, nothing committed)
**Done:** (1) Script check of every number in cited sentences against the cited chapter: no transcription errors found (17 flags were false positives from multi-cite sentences or PubMed items). (2) Read for the audit: Endodontology Ch.40, Gulabivala and Ng Ch.9 (surgical sections), Problem Solving Ch.16 (searched), Weine Ch.9 (searched), Ørstavik Ch.16 (Endodontic Radiology), parts of Essential Endodontology, TEI Ch.4 and 7, Seltzer and Bender Ch.16 (cyst passages found, not yet read).
**Patches still to apply (found, not yet written into the answers):**
1. MTA setting time (Q08 conflict box): add Endodontology Ch.40 2.75 h (pH 10.2 to 12.5) and Gulabivala and Ng about 4 h (ProRoot).
2. Suture removal (Q06 conflict box): add Endodontology Ch.40 3 to 5 days; Gulabivala and Ng 7 days; Weine maximum 7 days; Colour Manual (Barnes) 5 to 7 days; Current Therapy 2 to 4 days. Suture size also differs: Gutmann (Harty) 5-0 or 6-0; Endodontology 6-0 or finer, 7-0 and 8-0 at the papilla.
3. Flap compression time (Q05, Q06): Gulabivala and Ng 5 to 10 minutes against 3 minutes (Torabinejad, Rubinstein et al) and 2 to 3 minutes (Ingle's, Grossman).
4. Attached gingiva for submarginal flap (Q04, Q05): Gulabivala and Ng 3 to 5 mm; Velvart, Endodontology and Ingle's 2 mm; P&P Ch.20 papilla-base prerequisite 4 mm.
5. Resection depth (Q03, Q06): Gulabivala and Ng say routine 3 mm may be grossly excessive (pare gradually); Weine still describes a 45 degree bevel with a smaller bevel under the microscope; all others 3 mm and 0 to 10 degrees.
6. Epinephrine (Q06): Endodontology recommends 1:50,000; Tsesis says 1:100,000 suffices.
7. Biopsy (Q06, Q11): Gulabivala and Ng and Torabinejad say always send tissue; Lieblich (quoting Walton) says not always.
8. Curettage order: Gulabivala and Ng curette first then resect; Harty allows either.
9. Decompression (Q11): Gulabivala and Ng treat decompression and marsupialisation as the same, with a flanged cannula and daily irrigation by the patient, and note it spares adjacent teeth and structures.
10. True cysts (Q11, Q12, Q13): Seltzer and Bender and Ørstavik say true cysts must be removed surgically; Treatment of Endodontic Infections Ch.4 (Siqueira group) says the claim is speculative and the distinction is clinically irrelevant. Add both.
11. Q08: add Endodontology (Chong et al 2003) healing MTA 92% against IRM 87% at 2 years; Retroplast 73 to 90%; Gulabivala and Ng say Biodentine untested for root-end use.
12. Q13: add Ørstavik timeline (density change at 3 to 6 months, 1 year to judge, late healing up to 17 to 27 years), PAI cut-off above 2, failure at 1 year 5 to 10% (vital) and 20 to 30% (apical periodontitis), Kvist and Reit (6 months favours surgery, 1 to 2 years equal or better for retreatment), Strindberg and Rud/Molven criteria.
13. Q01 coverage gaps to check: incision and drainage, trephination, through-and-through surgery (Gulabivala and Ng).
**Not yet read:** Torabinejad Ch.1 to 3, 5 to 8, 12, 13, 16, 17 (rest), Bioceramics in Endodontics, Seltzer and Bender Ch.12, Endodontic Microbiology Ch.15, TEI Ch.1, 17, 20, Essential Endodontology (healing chapters), Guidelines Ch.3 and 4, Colour Manual (full), Advances in Surgical Endodontics.

## Update 5 (2026-10-18, after Niranjan's decisions): conflict boxes applied
Niranjan chose "conflict boxes only" for the 13 patches in Update 3 plus the earlier audit entry. Re-checked against the text first; several earlier claims did not hold up.
**Applied (Q05, Q06, Q08, Q11; SOURCE LIST and REFERENCES rebuilt with build_sources.py; all Exam Mode counts in range):**
- Item 2, suture removal (Q06): added Gulabivala and Ng 7 days (Ch.9, when wound strength is assured), Endodontology 3 to 5 days (Ch.40), Weine maximum 7 days (Ch.9), Barnes 5 to 7 days (1984 colour manual, Ch.5), Johnson, McNally et al 2 to 4 days (Current Therapy Ch.9).
- Item 3, flap compression (Q05, Q06): added Gulabivala and Ng 5 to 10 minutes of digital pressure after all sutures are placed.
- Item 1, MTA setting (Q08): added Endodontology 2.75 hours and pH rise to 10.2. **Not added:** the Gulabivala "about 4 h (ProRoot)" figure; no such passage found in Ch.9 or the Gulabivala folder.
- Item 11, healing (Q08): added Endodontology (citing Chong et al 2003) MTA 92% against IRM 87% at 2 years, and Retroplast 73 to 90% (Jensen et al 2002); noted that Johnson et al's Retroplast 74% vs 59% measures a different comparison. **Not added:** Gulabivala "Biodentine untested for root-end use"; no such passage found.
- Item 7, biopsy (Q11): added Gulabivala and Ng (routine biopsy accepted as standard of care; formalin and request form) and Lieblich 2012 (controversy over biopsying every surgically treated lesion, PDF p.10).
- Item 9, decompression (Q11): added Gulabivala and Ng (decompression and marsupialisation treated as one procedure; flanged cannula; daily patient irrigation; spares adjacent teeth).
**Not applied:**
- Item 4 (attached gingiva): already consistent (Velvart and Endodontology 2 mm in Q05). Gulabivala "3 to 5 mm" not found in Ch.9.
- Item 6 (epinephrine): Endodontology 1:50,000 for prolonged hemostasis confirmed (Ch.40); Tsesis "1:100,000 suffices" not found in the complications chapter text. Not added.
- Item 8 (curettage order): Gulabivala "curette first and resect later" confirmed (Ch.9), but Harty's "either" not found in Harty Ch.10. Single-source; not added.
- Item 12 (Q13 Ørstavik timeline and Kvist and Reit): not searched in this pass.
- Items 5, 10, 13: held for discussion (resection depth; true-cyst conflict; Q01 coverage gaps).
**Locator check:** `python3 locators.py` reports 0 MISSING with the 14 new keys (prefixed x_). Backups of the pre-patch files are in the scratchpad, not the repo.
