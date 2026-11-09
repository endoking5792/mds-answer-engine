# Review brief: Non-Carious Tooth Defects canonical answers

These answers are unpublished first drafts, written by a different agent. You are the second reader. Your job is to check them against the sources and fix real errors in place. Read `work/BRIEF.md` first (format and evidence rules the answers must follow).

## What to check, for each answer you are given
1. **Claims against sources.** For every [SRC] claim, the cited book must actually say it. Use the answer's SOURCE LIST (verbatim phrase + PDF page) and open the textbook file (`~/mds-textbooks/Operative_and_Dental_Materials_Textbooks/*.md` or `~/mds-textbooks/*_Chapterwise/`) around that page to read the context. Check especially: numbers (percentages, prevalence, pH values, times, index scores and thresholds, dates and who-first-described attributions), which book a figure is attributed to, compositions, and anything stated as a rule ("always", "never", "contraindicated"). Spot-check at least 60% of the numeric claims and every claim in the Exam core.
2. **Overstatement.** Wording stronger than the source ("always", "best", "contraindicated" where the book says "use with caution"), or laboratory findings written as clinical evidence.
3. **Contradictions.** Where the answer shows books disagreeing, confirm both sides are quoted correctly. Do not resolve them.
4. **Tags.** Untagged factual claims, numbers without [SRC]/[LIT], [RECALL] with bibliographic detail, [LIT] claims going beyond an abstract.
5. **Exam core.** Stands alone, within the word range, no error a candidate would copy into an exam.
6. **Cross-references** to other topics point to files that exist (e.g. `../dentin_hypersensitivity/...`, `../minimal_intervention/...`, `../glass_ionomer_cement/...`, `../composites/...`, relative to `~/.claude/answer_tools/`); also check the answer stays consistent with Q01 (the umbrella) where it repeats the same fact.

## How to fix
- Edit only the answer files you were given and that group's `work/gN/locators.py` / `build_sources.py`.
- Correct wrong figures/attributions to what the book says; soften overstatements; tag or remove unsupported claims. Do not add new material beyond what a fix needs.
- If you change or add an [SRC] claim, add/adjust its locator in `work/gN/locators.py` and the key in the answer's `<!--LOC: ...-->` line.
- After editing a file: strip everything from `\n## SOURCE LIST` to the end, then from `work/gN/` run `python3 locators.py` (must print `missing 0`) and `python3 build_sources.py ../../canonical/<file>`. Exam core must stay within its range.
- Do not touch git, the vault, the Answer Bank site, HANDOFF.md or WORKFLOW.md.

## Report back (under 250 words)
Per file: number of claims checked, errors found and fixed (one line each: what was wrong -> what it says now, with the book), overstatements softened, anything you could not verify, final exam-core count and `locators.py` result.

## Topic-specific checks
- Abfraction: laboratory/FEA findings must not be written as clinical proof; the controversy must be presented both ways.
- BEWE and Smith and Knight: check each score's wording and each threshold against the exact book cited (books differ on >= vs >).
- Spellings of names copied from books (e.g. Sikri's "Vialati and Belser" for Vailati) should be marked "[sic]" in the answer if kept.
- Any [LIT] claim must not go beyond what a PubMed abstract says; if you re-open an abstract to check, say so in your report.
