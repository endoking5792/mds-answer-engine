# Brief for drafting agents: Lasers, Photodynamic Therapy & Emerging Tech (canonical answers)

You are drafting MDS (Indian university) theory answers for Niranjan. Accuracy and honesty about sources matter more than fluency or length.

## Read first (do not edit these)
- `../_QUESTIONS.md`: the agreed question set (wordings each answer absorbs; topics answered elsewhere: link to them, do not repeat them).
- Layout examples (copy their exact layout):
  - 75m/100m: `../../cavity_prep/canonical/Q01_Recent_Advances_in_Cavity_Preparation_Methods_75m_CANONICAL.md`
  - 25m: `../../luting_cements/canonical/Q01_Luting_Cements_25m_CANONICAL.md`
  - 10m: `../../luting_cements/canonical/Q07_Calcium_Hydroxide_Cement_10m_CANONICAL.md`
- Existing related answers you must not duplicate (cross-reference them instead): `../../dentin_hypersensitivity/canonical/` (lasers in dentin hypersensitivity), lasers in bleaching (Answer Bank: Conservative Dentistry / Tooth Bleaching), `../../irrigants/` (irrigant activation devices), `../../cleaning_shaping/canonical/Q15_Debridement_in_Endodontics_100m_CANONICAL.md`.

## Your working folder
Work only in `work/<your group>/` and write finished answers to `../../canonical/` (only your own files). Never touch another group's files, WORKFLOW.md, HANDOFF.md, git, the vault or the Answer Bank site. Do not commit.
- `work/<group>/locators.py` (already copied from the base): fill F (source key -> chapter file, offset, in-text citation) and L (locator key -> source key, verbatim phrase under about 25 words). Prefix every locator key AND every F source key with your group (e.g. `g3_`, `g3:pandey8`) so the files merge later. Run `python3 locators.py` from that folder: it must print `missing 0`.
- `work/<group>/build_sources.py` (already copied): replace its BOOK and LIT dicts with your own references (keep RANGE). Run `python3 build_sources.py ../../canonical/<your file>` once each answer is final; it appends SOURCE LIST + REFERENCES and fills the exam-core word count. It appends, so to re-run strip everything from `\n## SOURCE LIST` first.

## Sources (PRIMARY = Niranjan's three laser books, converted this session; use them first and fully)
All files have `<!-- PDF page N -->` markers. Directory `~/mds-textbooks/Laser_Textbooks/`:
1. `Lasers_in_Dentistry_Current_Concepts_Coluzzi_Parker.md` — Coluzzi DJ, Parker SPA (eds). Lasers in Dentistry—Current Concepts. 1st ed. Springer; 2017. 18 chapters; chapter starts (PDF page): 1 Where to begin 13; 2 Laser and light fundamentals 26; 3 Laser–tissue interaction 38; 4 Operating parameters 65; 5 Laser safety 95; 6 Laser-assisted diagnostics 115; 7 PBM/LLLT 139; 8 Laser-assisted restorative dentistry 170; 9 Laser-assisted endodontics 197; 10 Implant 217; 11 Pediatric 237; 12 Ortho 251; 13 Soft tissue surgery 276; 14 Perio/peri-implant 294; 15 Multi-tissue aesthetic/restorative 318; 16 Colour in aesthetic zone 337; 17 Second generation hard-tissue lasers 360; 18 General practice 375; Glossary 389.
2. `Principles_and_Practice_of_Laser_Dentistry.md` — Convissar RA (ed). Principles and Practice of Laser Dentistry. 2nd ed. St Louis: Elsevier; 2016. Chapters (PDF page where the running header first appears; the chapter opens 1-2 pages earlier): 1 Origins and dental applications 9; 2 Laser fundamentals 20; 6 Fixed prosthetic and cosmetic 97; 10 Lasers in restorative dentistry 170; 11 Pediatric 190; 13 Lasers in endodontics 227; 15 Photobiomodulation 258; 16 Introducing lasers into practice 282; 17 Laser research 297.
3. `Lasers_in_Operative_Dentistry_and_Endodontics.md` — Pandey V. Lasers in Operative Dentistry and Endodontics. New Delhi: CBS; 2018 (first eBook edition). Single-author Indian text; chapters (PDF page): 1 Introduction 15; 2 Fundamentals 23; 3 Technical aspects of settings 41; 4 Laser–tissue interaction 54; 5 Classification 62; 6 Operative dentistry 79; 7 LLLT 149; 8 Endodontics 163; 9 Esthetics 204; 10 Safety 216; 11 Future 227; 12 Before purchasing 235; Glossary 241.
Also in `~/mds-textbooks/Operative_and_Dental_Materials_Textbooks/`: `Lasers_in_Dentistry_Current_Concepts.md` = the **2nd edition (2023)** of Coluzzi & Parker (markers `===== PAGE N =====`, which locators_base handles). Cite the two editions separately (e.g. "Parker, 2017" vs "Parker, 2023"); where the editions differ, show both.
Other books (grep counts for laser): `Textbook_of_Conservative_and_Restorative_Dentistry` 619, Goldstein 282, Modern_Operative_Dentistry 114, Mount 95, Detection_and_Assessment_of_Dental_Caries 76, Bonsor & Pearson 73 (all in Operative_and_Dental_Materials_Textbooks); `Seltzer_and_Bender_Dental_Pulp_Chapterwise_MD/Chapter_15...` (thermal effects of lasers on pulp) 253; `Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/31_31_Lasers_in_Endodontics.md` 218; `Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/24_Chapter_24_Lasers_in_Endodontics.md` 100; `Current_Therapy_in_Endodontics_Chapterwise/10_11_pdf_p_284_296.md` 99; Cohen's Ch.14 72.
PDT: `Endodontic_Irrigation_Chemical_disinfection_of_the_root_canal_system_Chapterwise/14_14_Photodynamic_Therapy_for_Root_Canal_Disinfection.md`; `Treatment_of_Endodontic_Infections_Chapterwise/14_...` and `16_...`; `Endodontic_Microbiology_2nd_ed_Chapterwise/13_...`.
Ozone: `Endodontic_Irrigation.../12_12_Ozone_Application_in_Endodontics.md`; Endodontic Microbiology Ch.13; Modern Operative Dentistry; Bonsor & Pearson; Textbook of Conservative and Restorative Dentistry; Endodontology Ch.25; Cohen's Ch.8.
LDF: Andreasen trauma atlas Ch.9, Sikri Ch.9, Seltzer & Bender Ch.6, Dynamic_Aspects_of_Dental_Pulp 05, Endodontic_Radiology Ch.19, Ingle's Ch.9, Cohen's Ch.1/14/21, plus the laser books' diagnostics chapters.
3D printing: `Operative_and_Dental_Materials_Textbooks/3D_Printing_in_Restorative_Dentistry.md` (restorative only; endodontic uses need PubMed). Cryotherapy: no textbook found — PubMed only, disclose it.
- Grep every relevant book for your key terms, then READ the passages; a grep hit count is not reading. Use every book that adds something.
- Offsets: printed page = PDF marker - offset. Confirm the offset at two or more pages in the chapter you cite; if you cannot see a printed page number, use `None`. Never guess a page.
- Cite multi-author edited books by CHAPTER AUTHOR (take it from the chapter's first page), e.g. a Coluzzi & Parker chapter by its own authors; single-author books by author (Pandey, 2018). If an author line is garbled, flag "verify against the printed book".
- DCNA articles: `/Users/niranjan/Library/CloudStorage/OneDrive-Personal/MDS III/DCNA articles/` (PDF; open with PyMuPDF, run python from your work folder, not from inside the DCNA folder). The lead will append a list of laser/PDT/ozone DCNA files to this brief if any are found. Use only if read in full, as supplementary evidence.
- Live literature (optional; for recent advances, numbers, contested claims: PIPS/SWEEPS, aPDT efficacy, ozone evidence, cryotherapy, 3D printing guides): load PubMed tools with ToolSearch (query "pubmed search"). Cite only what you opened, author-year plus DOI/PMID, and say "abstract only" if that is all you read. Put them in LIT and tag `<!--LIT: ...-->`.

## Evidence rules (non-negotiable)
- In-text author-year citations, e.g. (Pandey, 2018) or (Convissar, 2016); several sources in one bracket separated by semicolons. Then a tag: [SRC] = read in a book file this session (must have a locator in L, listed in the answer's `<!--LOC: ...-->` line); [LIT] = opened this session; [RECALL] = from memory, never with author, year, journal, edition, page or numbers attached.
- Never give a number (wavelength, power, pulse duration, temperature rise, percentage) that is not from [SRC] or [LIT]. Laser parameters vary between books: when they do, show each book's figure side by side with author and edition. Do not rank or reconcile them.
- Interpretive or contested statements end with [Certain], [Likely] or [Guessing].
- Laboratory/ex-vivo data (bacterial kill in extracted teeth, temperature rise in vitro) must not be presented as clinical evidence; name the study type.
- No fabricated citations. A missing citation is a minor fault; a made-up one is total failure.

## Answer layout (canonical, one .md per question, same as the examples)
File name: `../../canonical/QNN_Short_Title_<marks>m_CANONICAL.md` (predicted: `PN_Short_Title_<marks>m_PREDICTED_CANONICAL.md`, title line ends "PREDICTED, not seen in your papers").
1. `# "<question wording exactly as in _QUESTIONS.md>" (canonical answer)`, then `**Marks:** Nm, <type>`, `**Sitting:** ...` (list every absorbed wording with its sitting, from _QUESTIONS.md), the "How to read this answer" line with the placeholder `Exam core: X words, about Y minutes`, a short **Retrieval report** (books, chapters, offsets, searches run), then `<!--LOC: ...-->`, `<!--REF: ...-->` (and `<!--LIT: ...-->`) lines.
2. Numbered sections `## N. Heading`, each with `### Explanation` (Study Mode: mechanism and reasoning in prose; classifications/parameters as bullets or tables) followed by `#### ✎ Exam core` (what the student writes in the exam; written independently, under about 30% overlap with the explanation; must stand alone).
3. After the sections: `## Critical evidence synthesis` (100m: full synthesis on 2-4 claims where evidence diverges; 25m: 3-5 sentences on one claim; skip for 10m), `## High-yield points` (max 8 lines), `## Diagrams to draw` (`[DIAGRAM: title | elements | labels | why it earns marks]`, drawable in under 3 minutes: e.g. laser cavity/ resonator, electromagnetic spectrum with dental wavelengths, absorption curves of water/hydroxyapatite/haemoglobin/melanin), `## Common exam mistakes` (max 5, topic-specific), `## Mnemonic` (only if genuinely useful).
4. SOURCE LIST and REFERENCES are generated by build_sources.py.

Exam-core totals (sum of all ✎ Exam core blocks): 100m 3200-3500; 25m 850-1000; 10m 320-400. Stay inside; cut rather than overrun. Writing time = words / 22.
Q01 (lasers in CD & endo, 100m, g1) is the umbrella. Others may say "see Q01 for laser physics" in the Explanation, but their Exam core must stand alone.

## When done, report back (under 250 words)
Files written; exam-core word count each; `locators.py` result (`missing 0`); books/chapters used per answer; textbook contradictions recorded; anything left [RECALL] or unverified; wording ambiguities.

## DCNA list
Before finishing, check whether `work/DCNA_LIST.md` exists (the lead writes it when the DCNA scan completes). If it lists an article relevant to your questions, read it in full and use it as supplementary evidence.
