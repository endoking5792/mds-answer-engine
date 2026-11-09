# Brief for drafting agents: Non-Carious Tooth Defects (canonical answers)

You are drafting MDS (Indian university) theory answers for Niranjan. Accuracy and honesty about sources matter more than fluency or length.

## Read first (templates; do not edit them)
- `../_QUESTIONS.md`: the agreed question set, the wordings each answer absorbs, your group's answers, and topics answered elsewhere (link to those; do not repeat them).
- Layout examples (copy their exact layout):
  - 75m: `../../cavity_prep/canonical/Q01_Recent_Advances_in_Cavity_Preparation_Methods_75m_CANONICAL.md`
  - 25m: `../../luting_cements/canonical/Q01_Luting_Cements_25m_CANONICAL.md`
  - 10m: `../../luting_cements/canonical/Q07_Calcium_Hydroxide_Cement_10m_CANONICAL.md`
- Tools to copy: `../locators_base.py` (start your `locators.py` from it) and `../../luting_cements/work/g1/build_sources.py` (copy it, then replace its BOOK and LIT dicts with your own; RANGE already has every mark level).

## Your working folder
Work only in `work/<your group>/` and write finished answers to `../canonical/` (only your own files). Never touch another group's files, WORKFLOW.md, HANDOFF.md, git, the vault or the Answer Bank site. Do not commit.
- `work/<group>/locators.py`: fill F (source key -> chapter file, offset, in-text citation) and L (locator key -> source key, verbatim phrase under about 25 words). Prefix every locator key with your group (e.g. `g3_`) so the files can be merged later. Run `python3 locators.py` from that folder: it must print `missing 0`.
- `work/<group>/build_sources.py`: run `python3 build_sources.py ../../canonical/<your files>` once each answer is final; it appends SOURCE LIST + REFERENCES and fills in the exam-core word count. It appends, so run it once per file; to re-run, strip everything from `\n## SOURCE LIST` first.

## Sources
Textbooks: `~/mds-textbooks/Operative_and_Dental_Materials_Textbooks/*.md` (page markers `<!-- PDF page N -->`; the files have no Markdown chapter headings, so grep for terms). Grep counts for this topic (abfraction|erosion|attrition|non-carious|tooth wear|NCCL): Esthetics_in_Dentistry_Goldstein 462, Dentine_Hypersensitivity (Gillam) 286, Summitts 215, Advanced_Operative_Dentistry 183 (Ch.4 Tooth Wear), Sturdevants 2e SA 167, Modern_Operative_Dentistry 142, Operative_Dentistry_Marzouk 115, Preservation_and_Restoration_of_Tooth_Structure_Mount 114, Pickards_Guide_to_Minimally_Invasive 109, Essentials_of_Preclinical_Conservative_Dentistry_Harpreet_Singh 94 (dedicated NCCL chapter: BEWE, abrasion morphology, Grippo), Composite_Veneers 72, Alani_Patel 57, Bonsor_Pearson (A_Clinical_Guide) 46, Textbook_of_Preclinical_Conservative_Dentistry 44, Science_of_Dental_Materials (Bhat) 37, Atlas_of_Glass_Ionomer_Cements 34, McCabe 29, Pickards_Manual_9th 28 (§1.3 NCCL comparison table, GORD/bulimia), van Noort 27, Lasers_in_Dentistry 24. White spot lesions (g6): also Essentials_of_Dental_Caries_4th, Detection_and_Assessment_of_Dental_Caries, Pickards_Guide, Sturdevants, Goldstein (microabrasion, fluorosis), Summitt (bleaching/microabrasion).
- Grep every relevant book for your key terms, then READ the passages; a grep hit count is not reading. Use every book that adds something.
- Offsets: printed page = PDF marker - offset. Confirm the offset at two or more pages in the chapter you cite; if you cannot see a printed page number, use `None` (PDF page only). Never guess a page.
- Cite authors/years as they appear on the book's own title or chapter page; if a year is not printed, say so (e.g. "Marzouk et al, undated"). Check `../../refs_meta.json` for metadata already settled for these books and use the same citation form.
- DCNA articles: `~/Downloads/DCNA articles/` (titles indexed in `../../tools/` or grep `dcna_full_scan.txt` if present; otherwise open first pages with PyMuPDF). Use only if read in full, as supplementary evidence.
- Live literature (optional, only for recent advances, numbers, or contested claims, e.g. abfraction controversy, erosion prevalence, resin infiltration): load PubMed tools with ToolSearch (query "pubmed search"). Cite only what you opened, author-year plus DOI/PMID, and say "abstract only" if that is all you read. Put them in LIT and tag `<!--LIT: ...-->`.

## Evidence rules (non-negotiable)
- In-text author-year citations, e.g. (Ricketts and Bartlett, 2011) or (Banerjee and Watson, 2011); several sources in one bracket separated by semicolons. Then a tag: [SRC] = read in a textbook file this session (must have a locator in L, listed in the answer's `<!--LOC: ...-->` line); [LIT] = opened this session; [RECALL] = from memory, never with author, year, journal, edition, page or numbers attached.
- Never give a number, percentage, p-value or page that is not from [SRC] or [LIT].
- Interpretive or contested statements end with [Certain], [Likely] or [Guessing].
- Where books disagree (e.g. definition of abfraction, whether abfraction exists as a separate entity, critical pH, BEWE scoring, Class V material choice), show them side by side with author and edition. Do not rank or reconcile them.
- No fabricated citations. A missing citation is a minor fault; a made-up one is total failure.
- Laboratory or FEA data must not be presented as clinical evidence (this matters especially for abfraction).

## Answer layout (canonical, one .md per question, same as the examples)
File name: `../canonical/QNN_Short_Title_<marks>m_CANONICAL.md` (predicted: `PN_Short_Title_<marks>m_PREDICTED_CANONICAL.md`, with "PREDICTED, not seen in your papers" in the title line).
1. `# "<question wording exactly as in _QUESTIONS.md>" (canonical answer)`, then `**Marks:** Nm, <type>`, `**Sitting:** ...` (list every absorbed wording), the "How to read this answer" line with the exam-core count placeholder `Exam core: X words, about Y minutes` (the build script fills it in), a short **Retrieval report** (books, chapters, offsets, searches run), then the `<!--LOC: ...-->` and `<!--REF: ...-->` (and `<!--LIT: ...-->` if used) lines.
2. Numbered sections `## N. Heading`, each with `### Explanation` (Study Mode paragraphs: mechanism and reasoning, prose for mechanisms, bullets/tables for classifications) followed by `#### ✎ Exam core` (the text to write in the exam; written independently, not a trimmed copy; under about 30% overlap with the explanation; must stand alone).
3. After the sections: `## Critical evidence synthesis` (20m and above: full synthesis on 2-4 claims for 50m/75m, 3-5 sentences on one claim for 20-25m; skip for 10m and below unless the question says "critically" — Q5 says "critically evaluate", so it gets one), `## High-yield points` (max 8 lines), `## Diagrams to draw` (format `[DIAGRAM: title | elements | labels | why it earns marks]`, only if drawable in under 3 minutes), `## Common exam mistakes` (max 5, specific to this topic), `## Mnemonic` (only if genuinely useful; otherwise omit).
4. SOURCE LIST and REFERENCES are generated by build_sources.py.

Exam-core word totals (sum of all ✎ Exam core blocks): 75m 2550-3000; 50m 1700-2000; 25m 850-1000; 20m 680-800; 10m 320-400; 5m 160-200. Stay inside the range; cut rather than overrun. Writing time = words / 22.
Q1 (50m "Non-carious lesions and their management") is the topic's umbrella answer, written by g1 in parallel. Other answers may say "see Q1 for the full classification" in the Explanation, but their Exam core must stand alone.

## When done, report back (under 250 words)
Files written; exam-core word count for each; `locators.py` result (`missing 0`); books used per answer; any textbook contradictions recorded; anything you could not verify or left as [RECALL]; any wording ambiguity.
