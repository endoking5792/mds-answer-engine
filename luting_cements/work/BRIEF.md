# Brief for drafting agents: Luting & Cementation Materials (canonical answers)

You are drafting MDS (Indian university) theory answers for Niranjan. Accuracy and honesty about sources matter more than fluency or length.

## Read first (templates; do not edit them)
- `../_QUESTIONS.md`: the agreed question set, the wordings each answer absorbs, and topics answered elsewhere (link to those; do not repeat them).
- `../../isolation/canonical/Q01_Importance_and_Methods_of_Isolation_25m_CANONICAL.md` (a 25m example) and `../../isolation/canonical/Q03_Rubber_Dam_10m_CANONICAL.md` (a 10m example). Copy their exact layout.
- `../../isolation/locators.py` and `../../isolation/build_sources.py`: the verification and source-list tools you will copy.

## Your working folder
Work only in `work/<your group>/` and write finished answers to `../canonical/` (only your own files). Never touch another group's files, WORKFLOW.md, HANDOFF.md, git, the vault or the Answer Bank site. Do not commit.
- `work/<group>/locators.py`: start from `../locators_base.py` (copy it in), fill F (source key -> chapter file, offset, in-text citation) and L (locator key -> source key, verbatim phrase under about 25 words). Run `python3 locators.py` from that folder: it must print `missing 0`.
- `work/<group>/build_sources.py`: copy of isolation's build_sources.py with your own BOOK and LIT dicts. Add `'15':(510,600)` to RANGE. Run `python3 build_sources.py ../../canonical/<your files>` once each answer is final; it appends SOURCE LIST + REFERENCES and fills in the exam-core word count. Only run it once per file (it appends): if you need to re-run, strip everything from `\n## SOURCE LIST` first.

## Sources
Textbooks: `~/mds-textbooks/Operative_and_Dental_Materials_Textbooks/*.md` (page markers `<!-- PDF page N -->`). Most useful here: Craigs_Restorative_Dental_Materials.md (14e), Phillips_Science_of_Dental_Materials.md, Restorative_Dental_Materials_Craig_Michigan_11th.md (Ch.20 Dental Cements), Applied_Dental_Materials_McCabe_Walls_9th.md, Introduction_to_Dental_Materials_4th.md (van Noort), Powers_Wataha_Dental_Materials_Properties_and_Manipulation.md, A_Clinical_Guide_to_Applied_Dental_Materials.md (Bonsor and Pearson), Science_of_Dental_Materials.md (Bhat), Indirect_Restorations_Sikri.md (Luting Agents chapter around line 15513), Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md, Summitts_Fundamentals_of_Operative_Dentistry.md, Adhesive_Techniques_in_Restorative_Dentistry_Alani_Patel.md, Atlas_of_Glass_Ionomer_Cements.md, Operative_Dentistry_Marzouk.md, Dental_Material_Science_Exam_Manual.md. Endodontic books (for Super EBA, calcium hydroxide) are in `~/mds-textbooks/*_Chapterwise/`.
- Grep every relevant book for your key terms, then READ the passages; a grep hit count is not reading. Use every book that adds something.
- Offsets: printed page = PDF marker - offset. Confirm the offset at two or more pages in the chapter you cite; if you cannot see a printed page number, use `None` (PDF page only). Never guess a page.
- Cite authors/years as they appear on the book's own title or chapter page; if a year is not printed, say so (e.g. "Marzouk et al, undated").
- Live literature (optional, only for recent advances, numbers, or contested claims): load PubMed tools with ToolSearch (query "pubmed search"). Cite only what you opened, author-year plus DOI/PMID, and say "abstract only" if that is all you read. Put them in LIT and tag `<!--LIT: ...-->`.

## Evidence rules (non-negotiable)
- In-text author-year citations, e.g. (Sakaguchi and Powers, 2012) or (McCabe and Walls, 2008); several sources in one bracket separated by semicolons. Then a tag: [SRC] = read in a textbook file this session (must have a locator in L, listed in the answer's `<!--LOC: ...-->` line); [LIT] = opened this session; [RECALL] = from memory, never with author, year, journal, edition, page or numbers attached.
- Never give a number, percentage, p-value or page that is not from [SRC] or [LIT].
- Interpretive or contested statements end with [Certain], [Likely] or [Guessing].
- Where books disagree (e.g. film thickness, powder/liquid ratio, setting time, compressive strength), show them side by side with author and edition. Do not rank or reconcile them.
- No fabricated citations. A missing citation is a minor fault; a made-up one is total failure.
- Laboratory data must not be presented as clinical evidence.

## Answer layout (canonical, one .md per question, same as the isolation examples)
File name: `../canonical/QNN_Short_Title_<marks>m_CANONICAL.md` (predicted: `PN_Short_Title_<marks>m_PREDICTED_CANONICAL.md`, with "PREDICTED, not seen in your papers" in the title line).
1. `# "<question wording exactly as in _QUESTIONS.md>" (canonical answer)`, then `**Marks:** Nm, <type>`, `**Sitting:** ...` (list every absorbed wording), the "How to read this answer" line with the exam-core count placeholder `Exam core: X words, about Y minutes` (the build script fills it in), a short **Retrieval report** (books, chapters, offsets, searches run), then the `<!--LOC: ...-->` and `<!--REF: ...-->` (and `<!--LIT: ...-->` if used) lines.
2. Numbered sections `## N. Heading`, each with `### Explanation` (Study Mode paragraphs: mechanism and reasoning, prose for mechanisms, bullets/tables for classifications) followed by `#### ✎ Exam core` (the text to write in the exam; written independently, not a trimmed copy; under about 30% overlap with the explanation; must stand alone).
3. After the sections: `## Critical evidence synthesis` (20m and 25m only: 3-5 sentences on one or two claims where evidence actually diverges; skip for 15m and below unless the question says "critically"), `## High-yield points` (max 8 lines), `## Diagrams to draw` (format `[DIAGRAM: title | elements | labels | why it earns marks]`, only if drawable in under 3 minutes), `## Common exam mistakes` (max 5, specific to this topic), `## Mnemonic` (only if genuinely useful; otherwise omit).
4. SOURCE LIST and REFERENCES are generated by build_sources.py.

Exam-core word totals (sum of all ✎ Exam core blocks): 25m 850-1000; 20m 680-800; 15m 510-600; 10m 320-400; 5m 160-200. Stay inside the range; cut rather than overrun. Writing time = words / 22.
Q1 (25m "Luting cements") is the topic's umbrella answer, written by another group in parallel. Other answers may say "see Q1 for the full classification" in the Explanation, but their Exam core must stand alone.

## When done, report back (under 250 words)
Files written; exam-core word count for each; `locators.py` result (`missing 0`); books used per answer; any textbook contradictions recorded; anything you could not verify or left as [RECALL]; any wording ambiguity.
