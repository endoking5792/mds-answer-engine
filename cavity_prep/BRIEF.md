# Drafting brief: cavity_prep canonical answers (shared by all parallel drafting agents)

You are one of six agents drafting MDS (Conservative Dentistry) university theory answers for Niranjan, in parallel. Work ONLY on the questions assigned to you. Accuracy and source honesty outrank fluency and length.

## Read first
1. `/Users/niranjan/.claude/answer_tools/ANSWER_GUIDE.md` (the method; sections 3-6 matter most).
2. `/Users/niranjan/.claude/answer_tools/cavity_prep/_QUESTIONS.md` (your questions: exact printed wording, marks, sittings, absorbed repeats).
3. Template: `/Users/niranjan/.claude/answer_tools/templates/canonical_topic/canonical/QNN_Template_CANONICAL.md`.
4. Worked examples to imitate in structure and tone (skim, do not copy content):
   - 75m/100m: `/Users/niranjan/.claude/answer_tools/procedural_errors/canonical/Q01_Procedural_Errors_in_Endodontics_and_Management_75m_CANONICAL.md`
   - 20m: `/Users/niranjan/.claude/answer_tools/dentin_hypersensitivity/canonical/Q07_Attrition_Abrasion_Erosion_and_Techniques_for_Hypersensitivity_20m_CANONICAL.md`
   - 10m: `/Users/niranjan/.claude/answer_tools/procedural_errors/canonical/Q08_Devices_to_Retrieve_Separated_Instruments_10m_CANONICAL.md`
   - their phrase/source pattern: `/Users/niranjan/.claude/answer_tools/dentin_hypersensitivity/locators.py`

## Sources
Textbooks are Markdown with `<!-- PDF page N -->` markers in `~/mds-textbooks/` (main ones are whole-book files in `~/mds-textbooks/Operative_and_Dental_Materials_Textbooks/`): Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md, Operative_Dentistry_Marzouk.md, Summitts_Fundamentals_of_Operative_Dentistry.md, Essentials_of_Preclinical_Conservative_Dentistry_Harpreet_Singh.md, Textbook_of_Preclinical_Conservative_Dentistry.md, Modern_Operative_Dentistry.md, Indirect_Restorations_Sikri.md, Esthetics_in_Dentistry_Goldstein.md, Advanced_Operative_Dentistry.md, Adhesive_Techniques_in_Restorative_Dentistry_Alani_Patel.md, Pickard's, Craig's, Phillips', McCabe, Lasers in Dentistry, etc. `ls` the folders (also other `*_Chapterwise/` folders) and grep for your terms by content; do not rely on memory. READ the chapters; a hit count is not reading. Use every relevant book, not just the first good one. DCNA articles (optional, PDF): `/Users/niranjan/Downloads/DCNA articles/` (titles in `/tmp/endo_audit/dcna_full_scan.txt` if it exists). No live web search is needed; if you do use PubMed/web, tag [LIT] with URL/DOI actually opened.

Offsets: per chapter, find a visible printed page number beside a PDF marker at 2+ places; `offset = marker - printed`. If not confirmable, use `None` (PDF page only). Cite by chapter author where the book is edited (Sturdevant's and Summitt's chapters have authors), else by book author, author-year, e.g. (Marzouk, 1985) — get edition years from the book's front matter; if you cannot verify a year, say so in the retrieval report.

## Your files (do not touch anyone else's)
- Locators: `cavity_prep/parts/<X>.py` where X is your group letter. It is exec'd by `cavity_prep/locators.py`, which provides three functions:
  ```python
  src('<x>_stu', OP+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 23, 'Ritter et al, 2019')  # key, path, offset, in-text citation
  add('<x>_stu', {'<x>_outline_def': 'verbatim phrase under ~25 words', ...})                                     # locators for that source
  book('Ritter2019', "Ritter AV, Boushell LW, Walter R, eds. Sturdevant's ... ")                                  # REF key -> full reference
  ```
  (`T` = ~/mds-textbooks/, `OP` = its Operative_and_Dental_Materials_Textbooks/ folder, `os` are in scope.) ALL your source keys and locator keys must start with your prefix `<x>_` (lower-case group letter) so they never clash with other groups. REF keys may be shared (same key must map to the identical string; if unsure, prefix it too).
- Check: `cd /Users/niranjan/.claude/answer_tools/cavity_prep && python3 locators.py <x>_` must print `missing 0`. Fix or replace every missing phrase (copy phrases from the file text itself; avoid OCR damage, hyphen breaks, figure captions). Never keep a fact whose phrase you cannot find.
- Answers: `cavity_prep/canonical/<ID>_<Short_Title>_<marks>m_CANONICAL.md` (predicted: `P1_<Title>_20m_PREDICTED_CANONICAL.md`). Then run `python3 build_sources.py canonical/<your files>` (fills exam word count/time, appends SOURCE LIST and REFERENCES, writes a FAILURE DISCLOSURE if out of range; safe to re-run).
- Do NOT edit `locators.py`, `build_sources.py`, `_QUESTIONS.md`, other groups' files; no git, no publishing, no vault copies, no .docx.

## Answer format (canonical, skill Section 7.1 item 12)
- Header: question exactly as printed (in quotes) + "(canonical answer)"; `**Marks:** <n>m, <type>` (exactly this pattern, build_sources parses `**Marks:** 25m`); sitting; repeats absorbed (from _QUESTIONS.md); the "How to read" line with EXAMWORDS/EXAMMIN placeholders exactly as in the template; a short **Retrieval report** (what was read in full/in part, what was not used and why, whether a live search ran, any incomplete extract).
- `<!--LOC: ...-->` listing every locator key used in the answer, `<!--REF: ...-->` listing REF keys.
- Numbered sections, each: `### Explanation` (study-level reasoning; every textbook fact ends `(Author, Year) [SRC]`) then `#### ✎ Exam core` (what the student writes: headings, short paragraphs, tables; author-year citations, no [SRC] tags). Each canonical answer stands alone (its exam core must not depend on another answer; Explanation may point to a sibling answer for depth).
- Then `## CRITICAL EVIDENCE SYNTHESIS` (20m and above: 2-4 claims for 50/75m, 1-2 for 20-25m; textbook says / what other evidence shows / agreement or challenge / strength / conclusion / clinical implication; [Certain]/[Likely]/[Guessing]; omit for 10m and below unless "critically" is in the question), `## HIGH-YIELD POINTS` (max 8 lines), `## DIAGRAMS TO DRAW` (`[DIAGRAM: title | elements | labels | why it earns marks]`, hand-drawable in under 3 min), `## COMMON EXAM MISTAKES` (max 5, topic-specific), `## MNEMONIC` (only if genuinely useful; else write "None forced.").
- EXAM CORE LENGTH (total of all ✎ Exam core blocks) must fall in range: 75m 2550-3000, 50m 1700-2000, 25m 850-1000, 20m 680-800, 10m 320-400, 7m 230-280, 5m 160-200. Expand from sourced material or cut; no padding.
- Command words: "Critically review/analyse" = full appraisal; "Discuss" = balanced positions + interpretation; "Recent advances" = flag maturity of evidence.

## Honesty rules (non-negotiable)
- Every [SRC] fact must have a locator phrase on the page it came from. Anything from memory is `[RECALL]` with NO author, year, journal, edition or page attached. A fabricated citation is a total failure; a missing one is minor.
- Never state numbers (angles, mm, %, MPa) unless they came from a book read now ([SRC]) or a source opened now ([LIT]).
- Where books disagree (e.g. bevel angles, enamel-margin rules, extension for prevention), name each author and show both side by side; never rank or silently pick one. If a book is plainly wrong, say so and show why.
- Laboratory/in-vitro evidence is not clinical evidence; say which it is.

## When done
Reply with: files written; exam-core word count per answer; `python3 locators.py <x>_` result; sources read (book, chapter, author, offset); disagreements between books you found; anything [RECALL]-heavy or weak; anything you could not do.
