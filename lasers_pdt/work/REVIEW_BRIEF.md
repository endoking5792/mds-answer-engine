# Review brief: Lasers, Photodynamic Therapy & Emerging Tech canonical answers

These answers are unpublished first drafts, written by a different agent. You are the second reader. Your job is to check them against the sources and fix real errors in place. Read `work/BRIEF.md` first (format and evidence rules the answers must follow).

## What to check, for each answer you are given
1. **Claims against sources.** For every [SRC] claim, the cited book must actually say it. Use the answer's SOURCE LIST (verbatim phrase + PDF page) and open the textbook file (`~/mds-textbooks/Laser_Textbooks/*.md`, `~/mds-textbooks/Operative_and_Dental_Materials_Textbooks/*.md`, `~/mds-textbooks/*_Chapterwise/`, or the DCNA PDF in `/Users/niranjan/Library/CloudStorage/OneDrive-Personal/MDS III/DCNA articles/`) around that page to read the context. Check especially: numbers (percentages, prevalence, pH values, times, index scores and thresholds, dates and who-first-described attributions), which book a figure is attributed to, compositions, and anything stated as a rule ("always", "never", "contraindicated"). Spot-check at least 60% of the numeric claims and every claim in the Exam core.
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
- Laser parameters (wavelengths, mJ, Hz, W, pulse durations, fluence, temperature thresholds): check each figure against the exact book AND edition cited (Coluzzi & Parker 2017 vs 2023 differ). Where books differ, both must be shown correctly.
- Known suspected book slips to confirm or reject by reading the page: Pandey 43 °C vs 4.3 °C; Pandey toluidine blue "12–100 mg/mL"; Poli 2023 table <15 °C vs text <5 °C; Current Therapy attributing Nd:YAG safe settings to CO2; Cohen's Ch.21 "near-infrared" 632.8 nm. Mark as "[sic]" or "probable misprint" only where the page really shows it.
- In-vitro / ex-vivo bacterial-kill or temperature data must not be written as clinical evidence.
- Banday et al is Dent Clin N Am 2026;70:31-44 — cite as 2026 everywhere.
- Files with no group mapping problem: each answer's work folder is: Q01 g1; Q02, Q08 g2; Q03, Q04, P3 g3; Q05, Q06, Q07 g4; Q09, Q10, Q11 g5; P1, P2 g6. Edit locators/build_sources only in the owning group's folder. After all fixes, also run `python3 ../../locators.py` from lasers_pdt/ is NOT needed (the lead re-merges).
