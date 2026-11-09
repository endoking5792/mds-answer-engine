# DCNA audit brief: Non-Carious Tooth Defects (published canonical answers)

The 14 answers in `../canonical/` are published and second-read. Your job: read the Dental Clinics of North America (DCNA) articles assigned to you IN FULL, decide what is genuinely new and useful for the answers you own, and add it. Read `BRIEF.md` (format and evidence rules) and `REVIEW_BRIEF.md` first.

## Where the articles are
PDFs: `~/Desktop/DCNA articles/1-s2.0-<ID>.pdf`. Plain-text extractions (made with PyMuPDF, page breaks lost) for quick reading: `/private/tmp/claude-501/-Users-niranjan--claude-spares-spare-HezYGg/dad9643b-2c14-4312-813e-d4a473f6216a/scratchpad/dcna/1-s2.0-<ID>.txt`. Take the citation (authors, year, title, Dent Clin North Am volume(issue):pages, DOI) from the article's own first page.

## Rules
- DCNA is the third (supplementary) tier: textbook first, then DCNA. Add contemporary evidence, numbers, classifications, protocols or clinically important nuance the textbooks lack or predate. Do not replace a textbook statement; where the article disagrees with a book, show both side by side with authors and years (never rank).
- Read the whole article before deciding. A title or keyword match is not a reason to cite. Report every assigned article as either "added (what, where)" or "read, not additive (why)".
- Cite in text as (Wang and Lussi, 2010) or (Bedran-Russo et al, 2017), tag [SRC], and add a locator: in the owning group's `work/gN/locators.py` add an F entry pointing at the PDF itself, e.g. `'dcna_wang': (os.path.expanduser('~/Desktop/DCNA articles/1-s2.0-S0011853210000194.pdf'), None, 'Wang and Lussi, 2010')` (PDF page only, offset None, unless you confirm a printed page offset at 2+ pages), and L entries with the group prefix (`g2_dcna_...`). Add the key to the answer's `<!--LOC: ...-->` line, and add a full reference to that group's `build_sources.py` BOOK dict (journal-article style).
- If the article itself reports a laboratory or in-situ study, say so; do not present it as clinical evidence.
- Exam cores must stay inside their range (75m 2550-3000; 50m 1700-2000; 25m 850-1000; 10m 320-400; 5m 160-200). Most extra material belongs in the Explanation or Critical evidence synthesis. If you add to an exam core near its ceiling, cut something of equal length.
- After editing a file: strip everything from `\n## SOURCE LIST` to the end, then from `work/gN/` run `python3 locators.py` (must print `missing 0`) and `python3 build_sources.py ../../canonical/<file>`.
- Edit only the answer files and group tools you were given. Do not touch git, the vault, the Answer Bank site, HANDOFF.md or WORKFLOW.md.

## Report back (under 300 words)
Per article: added (to which answer, Explanation or Exam core, one line on what) or not additive (one line why). Final exam-core counts, `locators.py` results, any book-vs-DCNA disagreements recorded.
