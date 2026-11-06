# Drafting brief for parallel agents (Diagnosis in Endodontics, 2026-11-05)

You draft canonical MDS exam answers from textbooks. Read these first, in this order:
1. `/home/user/mds-answer-engine/ANSWER_GUIDE.md` (the method; follow steps 3 to 6).
2. `/home/user/mds-answer-engine/skill/dental-study-material-SKILL.md` Section 7 (lines 302 to the end): citation rules, word ranges, tags.
3. `/home/user/mds-answer-engine/diagnosis/_QUESTIONS.md` (exact wordings, marks, absorbed repeats, agreed structure points).
4. Worked examples: `/home/user/mds-answer-engine/procedural_errors/canonical/Q01_Procedural_Errors_in_Endodontics_and_Management_75m_CANONICAL.md` (long) and `.../Q08_Devices_to_Retrieve_Separated_Instruments_10m_CANONICAL.md` (short). Copy their structure.
5. Template: `/home/user/mds-answer-engine/templates/canonical_topic/canonical/QNN_Template_CANONICAL.md`.

## Textbooks
`/home/user/mds-textbooks/` (also at `~/mds-textbooks/`), chapterwise Markdown with `<!-- PDF page N -->` markers. Find chapters by content (grep counts), then READ them; do not just count hits. Get chapter authors from the chapter's first lines; cite author-year (e.g. "Berman and Rotstein, 2021" style as the chapter shows). Work out the page offset per chapter at two or more places, or use `None`.

## Your locator file (never edit another agent's file)
Create `/home/user/mds-answer-engine/diagnosis/loc_<PREFIX>.py` defining four dicts:
```python
import os
T = os.path.expanduser('~/mds-textbooks/')
F = {'<PREFIX>_coh1': (T+'Cohen_s_.../01_1_Diagnosis.md', None, 'Author, Year'), ...}
L = {'<PREFIX>_xxx': ('<PREFIX>_coh1', 'verbatim phrase under about 25 words'), ...}
BOOK = {'<PREFIX>_RefKey': 'Full reference ...', ...}
LIT = {}   # journal items you actually opened this session, with DOI/PMID and "abstract only" if so
```
EVERY key in F, L, BOOK and LIT must start with your PREFIX and an underscore, so files never collide.
Check with `cd /home/user/mds-answer-engine/diagnosis && python3 locators.py <PREFIX>_` : it must print `missing 0`. Fix or drop any missing phrase; never keep a fact whose phrase you cannot find. Avoid OCR-damaged text, hyphen breaks and figure captions.

## Your answer files
`/home/user/mds-answer-engine/diagnosis/canonical/<ID>_<Short_Title>_<marks>m_CANONICAL.md`. Header lines exactly as the template (`**Marks:** 100m, Essay` etc.; keep the literal `Exam core: EXAMWORDS words, about EXAMMIN minutes` text, the script fills it). `<!--LOC: ...-->` lists your locator keys used; `<!--REF: ...-->` your BOOK keys; `<!--LIT: ...-->` your LIT keys if any. Each section: `### Explanation` (every textbook fact ends `(Author, Year) [SRC]`) then `#### ✎ Exam core`. Then the closing sections per the template (CRITICAL EVIDENCE SYNTHESIS only for 20m and above; 25m one short claim).
Build: `cd /home/user/mds-answer-engine/diagnosis && python3 build_sources.py canonical/<your files>`. Re-run after each edit. The exam-core word count MUST land inside the range (100m 3200-3500, 50m 1700-2000, 20m 680-800, 15m 510-600, 10m 320-400, 5m 160-200). If it prints a FAILURE DISCLOSURE, fix the length from sourced material (no padding) and rebuild.

## Rules that matter most
- Where books disagree, name each author and show both side by side; never rank or silently pick one. Flag a plainly wrong book statement and show why.
- Anything not from a book read this session is `[RECALL]`, with no author, year or page. Use `[Certain]`/`[Likely]`/`[Guessing]` on interpretive or contested statements. A fabricated citation is a total failure.
- Each answer stands alone; it may point to a sibling answer but its exam core must not depend on it.
- No em dashes or en dashes in your prose (use commas, colons, "to"). Plain, exam-useful English.
- Literature: PubMed is blocked by the network proxy. You may try WebFetch on pubmed.ncbi.nlm.nih.gov once; if it fails, work textbook-only and say so in the retrieval report. Never cite a paper you did not open; textbooks' own cited studies may be named as "cited by (Author, Year)".
- Never paste long textbook passages; only the short locator phrases (this repo is public).
- Do NOT git commit or push. Do not touch files other than your loc file and your answer files.

## When done
Report back briefly: files written, exam-core word counts, locator count and `missing 0` confirmation, chapters read (with authors and offsets), source conflicts found (by author), and open points for Niranjan.
