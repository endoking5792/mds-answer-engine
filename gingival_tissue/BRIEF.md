# Drafting brief: gingival_tissue canonical answers (shared by all parallel drafting agents)

You are one of five agents drafting MDS (Conservative Dentistry) university theory answers for Niranjan, in parallel. Work ONLY on the questions assigned to you. Accuracy and source honesty outrank fluency and length.

## Read first
1. `/Users/niranjan/.claude/answer_tools/ANSWER_GUIDE.md` (the method; sections 3-6 matter most).
2. `/Users/niranjan/.claude/answer_tools/gingival_tissue/_QUESTIONS.md` (your questions: exact printed wording, marks, sittings, absorbed repeats).
3. Template: `/Users/niranjan/.claude/answer_tools/templates/canonical_topic/canonical/QNN_Template_CANONICAL.md`.
4. Worked examples to imitate in structure and tone (skim, do not copy content):
   - 75m/100m: `/Users/niranjan/.claude/answer_tools/procedural_errors/canonical/Q01_Procedural_Errors_in_Endodontics_and_Management_75m_CANONICAL.md`
   - 20m: `/Users/niranjan/.claude/answer_tools/dentin_hypersensitivity/canonical/Q07_Attrition_Abrasion_Erosion_and_Techniques_for_Hypersensitivity_20m_CANONICAL.md`
   - 10m: `/Users/niranjan/.claude/answer_tools/procedural_errors/canonical/Q08_Devices_to_Retrieve_Separated_Instruments_10m_CANONICAL.md`
   - their phrase/source pattern: `/Users/niranjan/.claude/answer_tools/dentin_hypersensitivity/locators.py`

## Sources (already mapped by the lead session; read these pages yourself, and add others if useful)
Textbooks are Markdown in `~/mds-textbooks/Operative_and_Dental_Materials_Textbooks/` with `===== PAGE N =====` markers. Helper to print pages: `python3 /Users/niranjan/.claude/answer_tools/gingival_tissue/pg.py <FilePrefix> <from> <to>`.
Confirmed offsets (printed = PDF - offset) and citations:
- Sturdevants_..._South_Asian.md Ch.10 "Periodontology Applied to Operative Dentistry" (contributors Morelli T, Neiva GF; cite (Morelli and Neiva, 2019)), PDF 271-279, offset 19: biologic width (Gargiulo/Vacek table), crown lengthening, gingivectomy, distal wedge, materials (Geristore, MTA, RMGI), provisionals, retraction cord vs cordless studies. Ch.8 isolation (no chapter author printed; cite (Ritter et al, 2019)), PDF ~245-255: No.212 cervical retainer, retraction cord clinical technique. Ch.23 cast restorations PDF 678-679: objectives of retraction, vasoconstrictor contraindications, cord steps.
- Summitts_Fundamentals_of_Operative_Dentistry.md (4th ed 2013, Quintessence; NO printed pages: offset None): Ch.1 Fruits, Khajotia, Nicholson PDF 75-81 (keratinized gingiva width, biologic width, bone sounding Kois, papilla 5 mm, overhangs); Ch.2 Rose, Haveman, Davis PDF 113-114 (restoration-related periodontal health); Ch.15 Overton, Hilton, LittleStar, Starr PDF 795-800 (nonsurgical retraction, 212SA clamp, miniflap, gingivoplasty, flap, crown lengthening timing 4-8 wk); Ch.18 Rouse PDF 948-968 (crest relationships normal/low/high, double cord, 4 requirements of retraction, 0.2 mm sulcus width, 4 min, aluminium sulfate, ferric).
- Indirect_Restorations_Sikri.md (Sikri 2017, CBS; offset None): Ch.2 Treatment planning PDF 59-60 (margin placement, biological width 2 mm); Ch.10 Impression making PDF 575-590 (Table 10.2, definition, need, indications/contraindications, mechanical/chemomechanical/surgical/miscellaneous methods, cord colour coding, double cord, electrosurgery rules, Magic Foam, Merocel, Expasyl, Gingitrac, lasers, Stay-put, Comprecap, Racegel, matrix impression system, cryosurgery, decongestants).
- Esthetics_in_Dentistry_Goldstein.md Ch.41 Impressions (Goldstein RE, Powers JM, Lee EA; 2018), PDF 1315-1319, offset 28: five methods, criteria, two-appointment procedure, epinephrine (Timberlake), one/two cord, problems, electrosurgery, bipolar, diode laser 810 nm.
- Advanced_Operative_Dentistry.md Ch.13 (Ricketts D; in Ricketts D, Bartlett D eds, 2011, Elsevier), PDF 172-177, offset 2: biological width ~3 mm, 0.5 mm subgingival limit, 0.2 mm sulcus, cords, Magic Foam Cord, astringents (aluminium chloride least damaging), adrenaline cautions, Expasyl, electrosurgery, burs, lasers uncommon.
- Advances_in_Operative_Dentistry.md Ch.10 Valerio S (Roulet JF, Wilson NHF eds, 2001, Quintessence), PDF 122-128, offset -3: No.000 cord, second cord half "floats", thin tissues.
- Operative_Dentistry_Marzouk.md (year not printed): Ch.20 "Techniques and rationale for control of the periodontium preparatory to cast fabrication" PDF 343-346, offset -2 (objectives A-G, four means: physico-mechanical, chemical [vasoconstrictors, fluid coagulants with %s, surface coagulants], cords/drawn cotton/pellets, packing rules a-m, electrosurgery four actions and ten rules, surgical); Ch. on single tooth restorations and periodontium PDF ~285-289 (margin location factors).
- Lasers_in_Dentistry_Current_Concepts.md Ch.15 Coluzzi DJ, Cronshaw M, Weintraub J (Coluzzi DJ, Parker SPA eds, 2nd ed 2023, Springer), PDF 486-492, offset 5: wavelengths for soft tissue, biotype, biologic width, troughing, soft-tissue crown lengthening.
- Optional extra books: Modern_Operative_Dentistry.md (PDF ~266-268, 506), A_Clinical_Guide_to_Applied_Dental_Materials.md (PDF 706-711), Restoration_of_Root_Canal_Treated_Teeth.md (PDF 68). Check if useful.
- [LIT] opened by the lead (PubMed abstract only): Martins FV, Santana RB, Fonseca EM. Efficacy of conventional cord versus cordless techniques for gingival displacement: a systematic review and meta-analysis. J Prosthet Dent 2020;125(1):46-55. doi:10.1016/j.prosdent.2019.09.009 (9 studies; most achieved >0.2 mm; cord gave greater displacement than cordless; risk of bias issues). If you use it, add `<!--LIT: Martins et al, 2020, abstract only, https://doi.org/10.1016/j.prosdent.2019.09.009 -->` in the header and cite (Martins et al, 2020) [LIT]. You may run further PubMed searches; tag [LIT] with DOI actually opened.

## Your files (do not touch anyone else's)
- Locators: `gingival_tissue/parts/<X>.py` where X is your group letter. It is exec'd by `gingival_tissue/locators.py`, which provides three functions:
  ```python
  src('<x>_stu', OP+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 23, 'Ritter et al, 2019')  # key, path, offset, in-text citation
  add('<x>_stu', {'<x>_outline_def': 'verbatim phrase under ~25 words', ...})                                     # locators for that source
  book('Ritter2019', "Ritter AV, Boushell LW, Walter R, eds. Sturdevant's ... ")                                  # REF key -> full reference
  ```
  (`T` = ~/mds-textbooks/, `OP` = its Operative_and_Dental_Materials_Textbooks/ folder, `os` are in scope.) ALL your source keys and locator keys must start with your prefix `<x>_` (lower-case group letter) so they never clash with other groups. REF keys may be shared (same key must map to the identical string; if unsure, prefix it too).
- Check: `cd /Users/niranjan/.claude/answer_tools/gingival_tissue && python3 locators.py <x>_` must print `missing 0`. Fix or replace every missing phrase (copy phrases from the file text itself; avoid OCR damage, hyphen breaks, figure captions). Never keep a fact whose phrase you cannot find.
- Answers: `gingival_tissue/canonical/<ID>_<Short_Title>_<marks>m_CANONICAL.md` (predicted: `P1_<Title>_20m_PREDICTED_CANONICAL.md`). Then run `python3 build_sources.py canonical/<your files>` (fills exam word count/time, appends SOURCE LIST and REFERENCES, writes a FAILURE DISCLOSURE if out of range; safe to re-run).
- Do NOT edit `locators.py`, `build_sources.py`, `_QUESTIONS.md`, other groups' files; no git, no publishing, no vault copies, no .docx.

## Answer format (canonical, skill Section 7.1 item 12)
- Header: question exactly as printed (in quotes) + "(canonical answer)"; `**Marks:** <n>m, <type>` (exactly this pattern, build_sources parses `**Marks:** 25m`); sitting; repeats absorbed (from _QUESTIONS.md); the "How to read" line with EXAMWORDS/EXAMMIN placeholders exactly as in the template; a short **Retrieval report** (what was read in full/in part, what was not used and why, whether a live search ran, any incomplete extract).
- `<!--LOC: ...-->` listing every locator key used in the answer, `<!--REF: ...-->` listing REF keys.
- Numbered sections, each: `### Explanation` (study-level reasoning; every textbook fact ends `(Author, Year) [SRC]`) then `#### ✎ Exam core` (what the student writes: headings, short paragraphs, tables; author-year citations, no [SRC] tags). Each canonical answer stands alone (its exam core must not depend on another answer; Explanation may point to a sibling answer for depth).
- Then `## CRITICAL EVIDENCE SYNTHESIS` (20m and above: 2-4 claims for 50/75m, 1-2 for 20-25m; textbook says / what other evidence shows / agreement or challenge / strength / conclusion / clinical implication; [Certain]/[Likely]/[Guessing]; omit for 10m and below unless "critically" is in the question), `## HIGH-YIELD POINTS` (max 8 lines), `## DIAGRAMS TO DRAW` (`[DIAGRAM: title | elements | labels | why it earns marks]`, hand-drawable in under 3 min), `## COMMON EXAM MISTAKES` (max 5, topic-specific), `## MNEMONIC` (only if genuinely useful; else write "None forced.").
- EXAM CORE LENGTH (total of all ✎ Exam core blocks) must fall in range: 100m 3200-3500, 75m 2550-3000, 50m 1700-2000, 25m 850-1000, 20m 680-800, 10m 320-400, 7m 230-280, 5m 160-200. Expand from sourced material or cut; no padding.
- Command words: "Critically review/analyse" = full appraisal; "Discuss" = balanced positions + interpretation; "Recent advances" = flag maturity of evidence.

## Honesty rules (non-negotiable)
- Every [SRC] fact must have a locator phrase on the page it came from. Anything from memory is `[RECALL]` with NO author, year, journal, edition or page attached. A fabricated citation is a total failure; a missing one is minor.
- Never state numbers (angles, mm, %, MPa) unless they came from a book read now ([SRC]) or a source opened now ([LIT]).
- Where books disagree (e.g. bevel angles, enamel-margin rules, extension for prevention), name each author and show both side by side; never rank or silently pick one. If a book is plainly wrong, say so and show why.
- Laboratory/in-vitro evidence is not clinical evidence; say which it is.

## When done
Reply with: files written; exam-core word count per answer; `python3 locators.py <x>_` result; sources read (book, chapter, author, offset); disagreements between books you found; anything [RECALL]-heavy or weak; anything you could not do.
