# Drafter brief — tooth_bleaching (parallel drafting, 2026-11-07)

You are one of five parallel drafters. Work ONLY in `/home/user/mds-answer-engine/tooth_bleaching/`. Do not commit or push; do not touch other drafters' files.

## Read first (required)
1. `/home/user/mds-answer-engine/skill/dental-study-material-SKILL.md` Section 7 (7.1 amendments override 7.3).
2. `/home/user/mds-answer-engine/ANSWER_GUIDE.md` steps 3-6.
3. The finished example: `/home/user/mds-answer-engine/corrosion_biocompatibility/canonical/C2_*_75m_CANONICAL.md` (large answer) and `C1_*_10m_CANONICAL.md` (short answer); its `locators.py` for phrase style. Copy their structure exactly (header, How-to-read line with EXAMWORDS/EXAMMIN placeholders, retrieval report, `<!--LOC: ...-->`, `<!--REF: ...-->`, numbered sections each with `### Explanation` then `#### ✎ Exam core`, then CRITICAL EVIDENCE SYNTHESIS (20m+ only), HIGH-YIELD POINTS, DIAGRAMS TO DRAW, COMMON EXAM MISTAKES, MNEMONIC). Template: `_TEMPLATE_answer.md`.
4. The agreed question list: `_QUESTIONS.md` (wording exactly as printed, absorbed sittings go in the header).

## Your files
- Locators: `loc_<id>.py` (your id is given in your task, e.g. `a1`). It defines three dicts, using the variable `T` (already set to the textbook root, with trailing slash):
  ```python
  F = { '<id>_gro': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/23_Chapter_23_Bleaching_of_Discolored_Teeth.md', <offset or None>, '<Author(s), Year>') }
  L = { '<id>_gro_walkdef': ('<id>_gro', '<verbatim phrase under ~25 words>') }
  BOOK = { '<RefKey>': "<full reference: authors/editors. Title. ed. Publisher; year. Ch.N title.>" }
  ```
  EVERY key in F and L must start with your id + underscore. BOOK keys are shared: use the form AuthorYear (e.g. `Gopikrishna2021`); if another drafter may cite the same book, give the identical string (copy it from another `loc_*.py` if it already exists) — a different string under the same key is an error.
- Answers: `canonical/<QID>_<Short_Title>_<marks>m_CANONICAL.md` (predicted: `..._10m_PREDICTED_CANONICAL.md`).

## Commands (run from the topic folder)
```bash
export MDS_TEXTBOOKS=/home/user/mds-textbooks/
python3 locators.py <id>_          # until "missing 0"
python3 build_sources.py canonical/<your files>   # fills word count, SOURCE LIST, REFERENCES; flags FAILURE DISCLOSURE
python3 check_answers.py canonical/<your files>   # 0 quotes not found; review exam-core numbers without a locator
```
Re-run build_sources after every edit (it rewrites everything after `## SOURCE LIST`).

## Sources (checked out at /home/user/mds-textbooks/; textbooks only, no live search)
Operative / materials (single files in `Operative_and_Dental_Materials_Textbooks/`, page markers `<!-- PDF page N -->` or `===== PAGE N =====`):
- `Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md` (bleaching chapter), `Summitts_Fundamentals_of_Operative_Dentistry.md` (661 hits — has a bleaching chapter), `Esthetics_in_Dentistry_Goldstein.md` (784 hits: discoloration/bleaching/microabrasion chapters), `Textbook_of_Conservative_and_Restorative_Dentistry.md` (Indian exam-style; contains control chars, use `grep -a`), `Craigs_Restorative_Dental_Materials.md` (14th; offset 11), `Restorative_Dental_Materials_Craig_Michigan_11th.md` (offset 10), `Phillips_Science_of_Dental_Materials.md` (offset 16), `Powers_Wataha_...md` (offset 12), `Applied_Dental_Materials_McCabe_Walls_9th.md` (offset 9), `A_Clinical_Guide_to_Applied_Dental_Materials.md`, `Adhesive_Techniques_in_Restorative_Dentistry_Alani_Patel.md`, `Lasers_in_Dentistry_Current_Concepts.md`, `Advanced_Operative_Dentistry.md`, `Fundamentals_of_Color_Shade_Matching.md`, `Composite_Veneers.md`.
Endodontic chapters: Cohen's 12th `Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/26_26_Bleaching_procedures.md` (and 18 Root resorption); Ingle's 7th Ch.40; Grossman's 14th Ch.23; Torabinejad *Endodontics: Principles and Practice* Ch.17; *Principles and practice of endodontics* 2002 Part 23; *Endodontology* Ch.44; Sikri *Essentials of Endodontics* Ch.24; Andreasen *Textbook and Color Atlas of Traumatic Injuries* Ch.33 and Ch.29.

Rules for sources:
- Find chapters by grep counts, then READ them. Before claiming any book lacks something, grep all of them.
- Page offset: printed page = PDF marker − offset, confirmed at two pages in THAT chapter; else offset None (PDF page only). Offsets can differ between chapters of one file.
- Cite the chapter author(s) from the chapter's first lines (author-year); if none, the editors. Year from the copyright line, or say "year not printed; verify" in BOOK.
- Locator phrases: verbatim, under ~25 words, clean text (avoid OCR ligature damage, hyphen breaks, figure captions). Never copy textbook passages beyond those short phrases into any file.

## Writing rules (the ones that matter most)
- Each Explanation fact ends `(Author, Year) [SRC]`; quote locator phrases where you quote. Anything not from a book you read: `[RECALL]`, no author/year/page. Use `[Certain]/[Likely]/[Guessing]` on interpretive or contested points. A fabricated citation is a total failure.
- Where books disagree (concentrations, times, pH, resorption incidence, heat use, sealing-base level, delay before bonding, etc.) name each and show them side by side; never silently pick. If a book is plainly wrong, say so and why.
- Exam-core word ranges (counted by the script across all `#### ✎ Exam core` blocks): 100m 3200-3500, 10m 320-400, 7m 230-280, 5m 160-200. Expand from sourced material or cut — never pad. Fix every FAILURE DISCLOSURE. Leave headroom (~150 words below the top for 100m) for the later audit.
- Exam cores must stand alone (a short answer may point to a longer one but must not depend on it). Exam core cites (Author, Year) but needs no [SRC] tags.
- Every exam-core number should occur in one of the answer's locator phrases; check_answers lists leftovers — add a locator or reword.
- Retrieval report: what you read in full, in part, not used; "Live search: none".

## When done
Report back (concisely): files written; per answer marks and exam-core word count; number of locators (missing 0); check_answers result (quotes not found = 0; any leftover numbers and why acceptable); BOOK keys you used; book conflicts you showed; anything not verified / open points; offsets you confirmed per file (and the two pages you confirmed them on).
