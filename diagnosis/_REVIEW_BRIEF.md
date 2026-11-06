# Second-reader pass and Harty's audit: brief for parallel reviewers (Diagnosis Part A, 2026-11-05)

You are an independent second reader. The answers you check were drafted by another agent and are already published; your job is to find and fix what is wrong, not to rewrite what is right.

Read first: `/home/user/mds-answer-engine/diagnosis/_AGENT_BRIEF.md` (the drafting rules, which still apply), the Section 7 rules in `/home/user/mds-answer-engine/skill/dental-study-material-SKILL.md` (line 302 on), and `diagnosis/_QUESTIONS.md`.

Textbooks: `/home/user/mds-textbooks/`. Harty's 7th ed is `/home/user/mds-textbooks/Harty_s_Endodontics_in_Clinical_Practice_7th_ed_Chapterwise/` (Ch.1 Introduction, Ch.2 General and systemic aspects, Ch.3 Diagnosis, Ch.5 Maintaining pulp vitality, Ch.12 Traumatic injuries, Ch.13 Marginal periodontitis and the pulp, Ch.14 Problems in endodontic treatment, Ch.15 Restoration). Ch.3 authors are Chandler and Chong (2017), offset 16, per the drafting agents; confirm the author line of every other Harty's chapter you use.

## Task A: verify every cited sentence
For each sentence in your answers that carries `[SRC]` (Explanation) or an author-year citation (Exam core):
1. Find its locator in the answer's SOURCE LIST, open the chapter at that PDF page, and read the surrounding paragraph.
2. Check the claim is FAITHFUL: right author for that chapter, right number/unit, not over-generalised, not stripped of a qualifier ("may", "in some studies"), not attributed to the wrong book, not a misread of a table or a figure caption. Check the exam core says the same as the explanation.
3. Check offsets and author lines at least once per chapter.
4. Check every "conflict" the answer reports really exists in the books, and every "book error" flagged really is an error.
5. Check `[RECALL]` items: if a book you can find actually covers it, convert it to `[SRC]` with a locator; if a [RECALL] statement is wrong, fix or remove it.

## Task B: Harty's audit
Read the Harty's chapters relevant to your answers in full. For each answer:
- Where Harty's agrees with what the answer says, add Harty's to the citation only if it adds value (e.g. a third source on a contested point).
- Where Harty's DISAGREES, add the disagreement side by side by author (never rank).
- Where Harty's adds an exam-relevant fact the answer lacks, add it if the exam core has room (stay in range) or put it in the explanation.
- Where the answer already cites Harty's, re-verify those claims (Task A).
Cite Harty's chapters by chapter author and year, with confirmed offsets.

## Editing rules
- Edit ONLY your assigned answer files and your group's existing locator file (`loc_<prefix>.py`, named below). New locator keys keep your group's prefix. Add BOOK entries for new Harty's chapters there.
- After every edit: `cd /home/user/mds-answer-engine/diagnosis && python3 locators.py <prefix>_` must print `missing 0`, then `python3 build_sources.py canonical/<file>`; the exam core must stay inside its range (no FAILURE DISCLOSURE). Note: other groups' locators are shared through `locators.py`; you may reference another prefix's key in a LOC line only if it already exists, never edit their file.
- Keep the answer's structure, headings and labelled subheadings. No em or en dashes in prose. Do not git commit or push.

## Audit ledger
Write `/home/user/mds-answer-engine/diagnosis/audit/<prefix>.md` with a table per answer:

| # | Location (section) | Finding | Evidence (book, PDF page, short phrase) | Action (fixed / added / kept / rejected) |

Include findings you checked and REJECTED (the claim held up), at least as a count per answer ("N cited sentences checked, M corrected"). List Harty's additions separately. End with open points for Niranjan.

## Report back
Briefly: per answer, sentences checked, corrections made (the important ones in one line each), Harty's additions/conflicts, final exam-core counts, `missing 0` confirmation.
