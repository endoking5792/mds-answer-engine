# Starting a new answer topic in a fresh Claude session

Paste this into a new cloud session (replace the topic line, or leave it as "next unclaimed"):

```
Read SESSION_PROMPT.md in endoking5792/mds-answer-engine and follow it.
Topic: next unclaimed
```

Everything below is the standing instruction for that session. Roseline (roselinerobert45@gmail.com) wrote it on 2026-11-07 after the corrosion_biocompatibility topic so that the method does not have to be explained again. Follow it without asking her to restate any of it.

---

## 0. Standing permissions (do not ask again)

You may, without asking:
- attach and clone `endoking5792/mds-answer-engine` (push), `endoking5792/mds-answer-bank` (push), `endoking5792/mds-textbooks` (read) and `endoking5792/Vault` (push, only to the session's designated branch);
- claim the topic in `WORKFLOW.md` and push that one-line commit to `mds-answer-engine` main;
- commit and push the topic folder, `WORKFLOW.md` and `HANDOFF.md` to `mds-answer-engine` main;
- publish the finished canonical answers to the Answer Bank site (https://mds-answer-bank.pages.dev, repo `mds-answer-bank`) with `scripts/add_answers.py`, commit and push;
- run the second-reader check and the textbook audit (section 5) straight after drafting, then republish;
- copy the finished answers into the Vault repo on the session's branch.

**The one stop:** after compiling the question list (section 2), show it to Roseline and wait for her OK or changes before drafting. Also ask if a decision is genuinely hers (e.g. a topic boundary that two topics could both claim). Do not ask about anything this file already settles.

## 1. Read the rules first

In `mds-answer-engine`:
1. `skill/dental-study-material-SKILL.md` Section 7. **7.1 (13 amendments) overrides the verbatim MASTER PROMPT v4.0 in 7.3.** Key points: author-year citations with REFERENCES and SOURCE LOCATORS; `[SRC]`/`[LIT]`/`[RECALL]` and `[Certain]`/`[Likely]`/`[Guessing]`; Exam-Mode word ranges (100m 3200-3500, 75m 2550-3000, 50m 1700-2000, 25m 850-1000, 20m 680-800, 15m 510-600, 10m 320-400, 7m 230-280, 5m 160-200); one canonical answer per distinct question (explanation, then `#### ✎ Exam core`); Markdown only, no .docx; publish as a standing step.
2. `ANSWER_GUIDE.md` (the method, steps 1-8) and `WORKFLOW.md` (claim table, Rules 1-7).
3. The finished example to copy: `corrosion_biocompatibility/` (Dental Materials; question grouping, locators, canonical answers, `audit/AUDIT_2026-11-07.md`). Endodontics/Conservative examples: `procedural_errors/`, `root_resorption/`.

Cloud-session paths: the skill's `/Users/niranjan/...` paths are Niranjan's Mac. Here, clone to `/home/user/<repo>` and set `export MDS_TEXTBOOKS=/home/user/mds-textbooks/` before running any topic script.

## 2. Pick the topic and compile the questions

- **Already claimed for you:** `tooth_bleaching` (Roseline, 2026-11-07) — if the topic line says tooth bleaching, the claim row exists: update it instead of adding one. Sources for it: Conservative §19, Dental Materials §17, the Endodontics repository's non-vital (intracoronal/walking) bleaching items, Recent Advances §21; books — Sturdevant's, Summitt's, Goldstein's *Esthetics in Dentistry*, Craig's 14th (bleaching agents, biocompatibility), Phillips', Cohen's/Ingle's/Grossman's (non-vital bleaching, cervical resorption).
- **Topic:** if Roseline names one, use it. If she says "next unclaimed", take the first section of the master repositories that has no row in the `WORKFLOW.md` claim table and no page on the site (`ls mds-answer-bank/docs/<Subject>/`). Work through Dental Materials in section order first. **As of 2026-11-07 the next one is Dental Materials §11 "Luting & Cementation Materials"** (luting cements; physical properties of cements 20m; resin cements; Super EBA 5m; calcium hydroxide cement 5m/10m). Check that it is still free before claiming. Cementation *protocols* for ceramics already sit in the Ceramics topic, so cross-reference them, don't repeat them.
- **Questions:** the four master repositories are in the Vault repo, `Question Paper Bank/*_MASTER_REPOSITORY.md`. Take the topic's section and search the other three repositories for the same subject (grep key terms). Group repeat wordings; answer each distinct question once at its highest marks; list the absorbed sittings; keep the wording exactly as printed; add 2-3 PREDICTED questions; move off-topic items to the topic they belong to, as cross-references. Write `<topic>/_QUESTIONS.md`.
- **Claim** the topic in `WORKFLOW.md` (one row: `| <topic> | IN PROGRESS (claimed <date>): ... | Roseline | <date> |`), commit, push. **Then show the list and stop for her OK.**

## 3. Sources (textbooks only unless a live search is possible)

- `mds-textbooks` is large and private. Clone without blobs, then check out only the folders you need:
  `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 --filter=blob:none --no-checkout <url> /home/user/mds-textbooks`, then `git sparse-checkout set --no-cone <folder>/` and `git checkout`. Dental-materials and operative books are single files in `Operative_and_Dental_Materials_Textbooks/`; endodontic books are `*_Chapterwise/` folders.
- Find chapters by grep counts, then **read them** (the guide's step 3). For Dental Materials use at least Phillips' 12th, Craig's 14th, Craig's 11th (Michigan), McCabe & Walls 9th, Powers & Wataha 10th, van Noort 4th and Bhat et al *Science of Dental Materials* 3rd (the Indian exam-style book).
- **Page offsets:** printed page = PDF marker - offset, confirmed at two pages. They can differ between chapters of the same file (Bhat et al: 33 for Ch.7, 56 for Ch.24). Known: Phillips' 16, Craig's 14th 11, Craig's 11th 10, McCabe 9, Powers & Wataha 12, van Noort 4th 15.
- Cite the extraction's chapter author; if there is none (Craig's 14th, Phillips'), cite the editors. Give the edition year from the copyright line, or say it is not printed.
- Never put textbook text beyond the short locator phrases into `mds-answer-engine` (public) or the site.

## 4. Build the answers

Copy `templates/canonical_topic/` to `<topic>/`. It has `locators.py`, `build_sources.py` and `check_answers.py`; the template already handles soft hyphens at line ends and reads `MDS_TEXTBOOKS`.
1. Write the locators first (verbatim phrases) and run `python3 locators.py` until `missing 0`.
2. Draft the largest answer first, then the shorter ones. Each fact in an Explanation ends `(Author, Year) [SRC]`; quote the locator phrase where you quote. Where books disagree, name each and show them side by side; if a book is plainly wrong, say so and why.
3. `python3 build_sources.py canonical/*.md` fills the word count and source list. Fix every FAILURE DISCLOSURE by expanding from sourced material or cutting, never by padding. Re-run after every edit.

## 5. Second-reader check and textbook audit (always, before calling the topic done)

1. `python3 check_answers.py canonical/*.md`: 0 quotes not found; review every exam-core number it lists without a locator, and add a locator or rewrite.
2. Re-read each exam core for statements with no locator behind them; reword to what the book says, or mark `[RECALL]`. Remove anything you assumed.
3. **Audit against the other textbooks** (for Dental Materials: Craig's 14th and 11th, McCabe & Walls, Bhat et al, plus whichever of the section-3 list you did not draft from). Look for: (a) facts the draft lacks that an exam answer needs (test methods, classifications, numbers); (b) conflicts between books, shown side by side with your reasoning; (c) textbook slips. Add locators for everything you add.
4. Write `<topic>/audit/AUDIT_<date>.md` (checks done, additions per answer, conflicts, slips, open points).

## 6. Publish and record

1. Site: `cd /home/user/mds-answer-bank && git pull`, then `python3 scripts/add_answers.py "<Subject>" "<Topic name>" /home/user/mds-answer-engine/<topic>/canonical/`. Check `git status`. Optional build check: `pip install -r requirements.txt` in a venv in the scratchpad, then `mkdocs build -q -d <scratchpad>/site` (no warnings). Then commit and push. Record the `manifest N -> M, 0 lost` line.
2. `mds-answer-engine`: update the topic row in `WORKFLOW.md` (status, answers, exam-core counts, locator count, audit, site manifest line), add a status line at the top of `HANDOFF.md`, write `<topic>/HANDOFF_<topic>.md` (file table, sources and offsets, open points), commit and push to main.
3. Vault: copy the canonical files (without `_CANONICAL`) to `Question Paper Bank/Answers/<Subject>/<Topic name>/` on the session's branch, commit and push.
4. Commit messages end with the attribution lines the session gives you.

## 7. Report back to Roseline

A short summary: the topic and its answers with marks and exam-core words against the range; the sources; the book conflicts and how you handled them; what was not verified; the links (site topic page, files). Then propose the next unclaimed topic.

## Lessons from earlier topics

- Phillips' extraction breaks words with a soft hyphen at line ends: the template's `norm()` handles it. If phrases still go missing, look at the raw text (`cat -A`) before rewording.
- Short quoted single words (`"appropriate"`) are fine in prose; `check_answers.py` ignores quotes under 12 characters.
- A 75m exam core fills fast once the audit adds material; leave about 150 words of headroom in the first draft.
- Retrieval reports must not claim a source lacks something until you have grepped all the books (the first corrosion draft wrongly said no book mentioned Brånemark).
- Sign conventions (electrode potentials), editions (ISO part counts by year) and terminology (what counts as a "usage test") are the usual sources of apparent conflict: say which it is.
