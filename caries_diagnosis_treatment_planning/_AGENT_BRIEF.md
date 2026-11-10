# Drafting brief — caries_diagnosis_treatment_planning (Conservative Dentistry §1)

You are one of several parallel drafters. Write ONLY your own files (listed in your task). Never edit `locators.py`, `build_audit.py`, `_QUESTIONS.md`, another drafter's files, `WORKFLOW.md` or `HANDOFF.md`. Do not commit or push. Do not publish.

## Read first (in this order)
1. `~/mds-answer-engine/SESSION_PROMPT.md` sections 3, 4 and "Lessons".
2. `~/mds-answer-engine/skill/dental-study-material-SKILL.md` Section 7.1 item 12 (the answer standard; it overrides 7.3).
3. `~/mds-answer-engine/ANSWER_GUIDE.md` sections 3-6.
4. The finished example `~/mds-answer-engine/apexification/` — copy its SHAPE: `canonical/Q03_Apexification_10m_CANONICAL.md` (10m), `canonical/Q01_..._75m_CANONICAL.md` (long essay), `locators_Q03.py` (locator file), `audit/Q03_Apexification_10m_AUDIT.md` (sidecar). Not its content.
5. `_QUESTIONS.md` in this folder: your questions' exact wording, marks and absorbed wordings. The answer must also satisfy the absorbed wordings where they ask something extra (it must stand alone).

## Environment
- Textbooks: `export MDS_TEXTBOOKS=/home/user/mds-textbooks/` (set this for every python run). Conservative/materials books are single files in `/home/user/mds-textbooks/Operative_and_Dental_Materials_Textbooks/` with markers `===== PAGE n =====`.
- Topic folder: `/root/mds-answer-engine/caries_diagnosis_treatment_planning/` (= `~/mds-answer-engine/...`). Run scripts from it.
- Helper (read-only, optional): `python3 /tmp/claude-0/-home-user/03982c14-420a-56fc-a453-e2c4118c5359/scratchpad/pg.py hits <BookFile.md> '<regex>'` lists PDF pages with hit counts; `... pg.py show <BookFile.md> <from> <to>` prints pages.

## Your files (QID = your question ID, e.g. Q05)
- `locators_<QID>.py`: dicts `F_EXTRA` (source key -> (file path, offset, 'Author, Year')) and `L` (locator key -> (source key, verbatim phrase under ~25 words)). ALL keys prefixed with your lower-case QID, e.g. `q05_det16`, `q05_qlf_def`. Use `T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')`. Each answer gets its own locators file even if one drafter writes several answers.
- `canonical/<QID>_<Short_Title>_<marks>m_CANONICAL.md` (predicted: `P1_<Short_Title>_10m_PREDICTED_CANONICAL.md`).
- `audit/<same name with _CANONICAL replaced by _AUDIT>.md`, from `audit/_SIDECAR_TEMPLATE.md`. Fill every section; `<!--LOC: ...-->` lists every locator key behind the answer.

## Checks you must run until clean
- `python3 locators.py <qid>_` → `missing 0` for your keys.
- `python3 build_audit.py audit/<your sidecar>` → LOC missing 0; quotes not found 0; body words inside the calibration range (100m 3200-3500, 75m 2550-3000, 25m 850-1000, 20m 680-800, 10m 320-400, 5m 160-200; for 75m+ leave about 150 words of headroom below the ceiling); cited surnames not in references: none. Review every "body numbers without a locator": add a locator or reword to what the book says.

## Answer rules (short form — SKILL 7.1 item 12 governs)
- `# <question exactly as printed>` then `**Marks:** <n> · <type>`. 10m and 20m: one line `**Answer blueprint:** A → B → C …` (the exact heading sequence).
- One integrated exam-language answer. Intro/definition → question-specific headings → mechanism/rationale → clinical significance → short conclusion. Tables for comparisons, numbered steps for procedures, classifications where asked. Hand-drawable `**Diagram:** …` cue only where it earns marks.
- Author-year citations in prose naming the CHAPTER author, e.g. (Kim, 2019). End with `## References`, numbered Vancouver list ordered by first citation. No numeric in-text markers. Never invent authors, years, editions, pages or DOIs.
- Where books disagree, name each author side by side; never silently pick one. Unsourced reasoning written as reasoning.
- Not in the student file: retrieval notes, locators, [SRC]/[RECALL] tags, mnemonics, generic recaps, common-mistake lists.
- Never copy textbook text beyond the short locator phrases (this repo is public).
- Textbooks only; no web or journal search unless the facts cannot be found in any book (then mark `[RECALL]` in the sidecar and write cautiously).

## Sources (find more by grepping; READ the chapters, don't just count hits)
Page offsets differ chapter by chapter: printed page = PDF marker − offset, confirm at 2+ pages IN THAT CHAPTER (look for the lone printed number at the top/bottom of a page), else offset `None`. Record the check in a comment in F_EXTRA.

**Detection and Assessment of Dental Caries: A Clinical Guide** (Ferreira Zandona A, Longbottom C, eds. Cham: Springer Nature Switzerland; 2019) — `Detection_and_Assessment_of_Dental_Caries.md`. The primary source for detection methods. Chapter authors (from the contents page) and printed start pages:
1 Introduction — Ferreira Zandona and Longbottom (p1, PDF 10); 2 Preparing teeth for examination — Longbottom and Ferreira Zandona (p7); 3 Visual presentation of caries — Cortes, Martignon and Douglas (p17); 4 Hidden caries — Deery (p27); 5 Nyvad criteria — Machiulskiene (p35); 6 ICDAS — Ekstrand and Braga (p45); 7 ADA CCS — Zeller, Young and Novy (p57); 8 CAST — Leal, Ribeiro and Hilgert (p69); 9 Caries detection dyes — Maltz, Arthur and Fatturi-Parolo (p83); 10 FACE — Lennon and Buchalla (p99); 11 Conventional bitewings — Schwendicke and Göstemeyer (p109); 12 Digital bitewings — Göstemeyer and Schwendicke (p119); 13 CBCT — Price (p127); 14 FOTI — Hogan, Pretty and Ellwood (p139); 15 NILT — Kühnisch (p151); 16 QLF — Kim (p159); 17 DIAGNOdent — Neuhaus and Lussi (p171); 18 Canary System — Amaechi (p177); 19 NIR reflectance — Fried (p189); 20 OCT — Fried (p199); 21 Ultrasound — Yanıkoğlu and Tağtekin (p209); 22 Bioluminescence — Longbottom and Vernon (p217); 23 Clinical decision-making — Fontana and Huysmans (p227); 24 Integrating devices — Abrahams (p235); 25 Concluding remarks (p243); 26 Definitions — Huysmans (p247). Observed offsets (verify yourself): ch1 9, ch6 5, ch9 2, ch11 1, ch12-16 0, ch18 -1, ch25 -6.

**Standing Conservative list** (SESSION_PROMPT §3): Sturdevant's 2e South Asian (`Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md`: caries/caries risk ~PDF 46-105, patient assessment, examination, diagnosis and treatment planning ~PDF 106-130), Summitt's (`Summitts_Fundamentals_of_Operative_Dentistry.md`: patient assessment and treatment planning ~PDF 82-151, caries management/risk ~PDF 210-270), Marzouk (`Operative_Dentistry_Marzouk.md`), Sikri, Mount 3rd (`Preservation_and_Restoration_of_Tooth_Structure_Mount.md`: risk ~PDF 41-65), Garg / `Textbook_of_Conservative_and_Restorative_Dentistry.md` (diagnosis and treatment planning ~PDF 113-125, caries activity tests PDF 120-121, diagnostic aids ~PDF 145-155; file contains binary bytes — use `grep -a`), Harpreet Singh (`Essentials_of_Preclinical_Conservative_Dentistry_Harpreet_Singh.md`), Pickard's Manual 9th (~PDF 25-52) and Pickard's Guide to Minimally Invasive Operative Dentistry. Also: Kidd *Essentials of Dental Caries* 4th 2016 (`Essentials_of_Dental_Caries_4th.md`: Ch.3 detection/diagnosis ~PDF 61-87, saliva ~PDF 52-53, risk/ caries control Ch.7 ~PDF 151), Torres *Modern Operative Dentistry* (`Modern_Operative_Dentistry.md`: diagnosis/treatment planning ~PDF 16-55, risk ~PDF 42, 645-650), *Lasers in Dentistry: Current Concepts* (DIAGNOdent/QLF/fluorescence chapter), *Advanced Operative Dentistry*. Take chapter author and year from the chapter's first lines or the contents page and the copyright line; if a book has no chapter authors, cite the editors/author.

## Report back (final message, short)
For each answer: file names, body words vs range, locator count, build_audit result line, books used with offsets, any book conflicts and how shown, anything [RECALL] or unverified.
