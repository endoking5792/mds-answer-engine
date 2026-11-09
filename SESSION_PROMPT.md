# Starting a new answer topic in a fresh Claude Code session

**Collaborators paste this (replace the topic line):**

```
Set up first. In a terminal run: if ~/mds-answer-engine does not exist, `git clone https://github.com/endoking5792/mds-answer-engine.git ~/mds-answer-engine`; then `cd ~/mds-answer-engine && git checkout main && git pull origin main`. Then read ~/mds-answer-engine/SESSION_PROMPT.md in full and follow it exactly, from section 0 onward. Use nothing from memory or from any older copy of the rules.
Topic: <topic title, e.g. "Pulp capping materials">
```

Everything below is the standing instruction for that session. It follows the **unified examination-ready answer standard adopted 2026-11-09** (`skill/dental-study-material-SKILL.md` Section 7.1 item 12, PR #4). Follow it without asking the collaborator to restate any of it.

---

## 0. Setup (once per machine, then a quick pull each session)

Work in the user's home folder. Commands are for macOS/Linux (Windows: use WSL or Git Bash). The user must already have `git` and access to the GitHub account that is a collaborator on these repos; if a clone is refused, tell her to ask Niranjan for access and stop.

```bash
cd ~
[ -d mds-answer-engine ] || git clone https://github.com/endoking5792/mds-answer-engine.git
[ -d mds-answer-bank ]   || git clone https://github.com/endoking5792/mds-answer-bank.git
[ -d Vault ]             || git clone --depth 1 https://github.com/endoking5792/Vault.git
for r in mds-answer-engine mds-answer-bank Vault; do git -C ~/$r checkout main && git -C ~/$r pull origin main; done
mkdir -p ~/.claude/skills/dental-study-material
cp ~/mds-answer-engine/skill/dental-study-material-SKILL.md ~/.claude/skills/dental-study-material/SKILL.md
export MDS_TEXTBOOKS=$HOME/mds-textbooks/
```

- **Textbooks (`mds-textbooks`, private, about 30 MB of Markdown):** `[ -d ~/mds-textbooks ] || git clone https://github.com/endoking5792/mds-textbooks.git ~/mds-textbooks`, and `git -C ~/mds-textbooks pull` on later sessions. Dental-materials and operative books are single files in `Operative_and_Dental_Materials_Textbooks/` (page markers `===== PAGE n =====`); endodontic books are `*_Chapterwise/` folders (markers `<!-- PDF page n -->`). The template handles both marker styles.
- If a script path in the skill or the guide points at `/Users/niranjan/...` (OneDrive, Obsidian, `~/.claude/answer_tools`), that is Niranjan's Mac: use `~/mds-answer-engine`, `~/mds-textbooks` and `~/mds-answer-bank` instead.
- Run all topic scripts from the topic folder with `MDS_TEXTBOOKS` set (the template reads it).

## 1. Standing permissions (do not ask again)

You may, without asking:
- commit and push to `mds-answer-engine` `main`: the one-line claim in `WORKFLOW.md`, then the topic folder, `WORKFLOW.md` and `HANDOFF.md`;
- publish the finished student answers to the Answer Bank site by running `scripts/add_answers.py` in `~/mds-answer-bank`, then commit and push there;
- run the second-reader check and textbook audit (section 6) straight after drafting, then republish.

**The one stop:** after compiling the question list (section 2), show it to the user and wait for her OK or changes before drafting. Also ask if a decision is genuinely hers (e.g. a topic boundary two topics could both claim). Do not ask about anything this file already settles.

**Not in scope:** the Vault and OneDrive (Niranjan syncs those), `.docx` builds, and the retired claude.ai Answer Bank artifact (frozen at Version 65: never publish to it).

## 2. Read the rules, pick the topic, compile the questions

1. Read, in `~/mds-answer-engine`: `skill/dental-study-material-SKILL.md` Section 7 (**7.1 item 12 is the answer standard and overrides the legacy base prompt in 7.3**), `ANSWER_GUIDE.md`, `WORKFLOW.md` (claim table, Rules 1-7) and the top of `HANDOFF.md`.
2. Look at the finished example of the new standard: `apexification/` (`canonical/` for the student answers, `audit/` for the sidecars, `HANDOFF_apexification.md`). Copy its shape, not its content. Older topics (`procedural_errors/`, `luting_cements/`, `non_carious_defects/` …) use the superseded Explanation + Exam core layout; use them only as a coverage cross-check, never as a format.
3. **Topic:** the collaborator gives a title. Search `WORKFLOW.md` and `ls ~/mds-answer-bank/docs/*/` for it. If another person already holds it, or answers for it already exist on the site, stop and tell her; do not start a second copy. If the title names a section the master repositories split across subjects, ask which subject owns it. If she says "next unclaimed", take the first section of the master repositories that has no row in the claim table and no page on the site (Dental Materials in section order first), and tell her which.
4. **Questions:** the four master repositories are `~/Vault/Question Paper Bank/*_MASTER_REPOSITORY.md`. Take the topic's section and grep the other three repositories (and any Manipal/TN MGR addenda) for the same subject. Group repeat wordings: answer each distinct question **once, at its highest marks**; list the other wordings and sittings as absorbed; keep the wording exactly as printed; add 2-3 PREDICTED questions; move off-topic items to the topic they belong to as cross-references. Write `<topic>/_QUESTIONS.md` from `templates/canonical_topic/_QUESTIONS.md` (copy the whole template folder to `<topic>/` first, see section 4).
5. **Claim** the topic: add one row to the claim table in `WORKFLOW.md` (`| <topic> | IN PROGRESS (claimed <date>): <subject §n, question count> | <collaborator's name> | <date> |`), commit and push that single change to `main` immediately (`git pull --rebase` first; on a conflict keep both sides' lines).
6. **Show the question list and stop for her OK.**

## 3. Sources (textbooks first, live literature only when it changes accuracy)

- Find candidate chapters by grepping the topic's key terms across `~/mds-textbooks` (hit counts), **then read the chapters**; a dedicated chapter in a less obvious book often beats the big textbook.
- Check each chapter file is complete (some extracts stop half way); note any limitation for the sidecar, not the answer.
- **Chapter authors and years:** take the author from the chapter's first lines or the book's contents page; if the OCR is garbled, decode it and mark it "verify against the printed book" in the sidecar. Give the edition year from the copyright line, or say it is not printed. If a book has no chapter author (e.g. Craig's 14th, Phillips'), cite the editors.
- **Page offsets:** printed page = PDF marker − offset, confirmed at two or more pages **in that chapter** (offsets differ between chapters of one book). If you cannot confirm, set the offset to `None` and cite the PDF page only. Offsets already known are in `HANDOFF_*.md` files of earlier topics.
- For Dental Materials use at least Phillips' 12th, Craig's 14th, Craig's 11th, McCabe & Walls 9th, Powers & Wataha 10th, van Noort 4th and Bhat et al *Science of Dental Materials* 3rd. For Endodontics see the apexification and procedural_errors handoffs for the standing list. Conservative: Sturdevant's 2e SA, Summitt's, Marzouk, Sikri, Mount, Garg, Singh, Pickard's.
- `[LIT]` journal evidence: only if you can open the paper or abstract this session (PubMed tools or web); say whether full text or abstract. Anything else is `[RECALL]`, with no author, year, journal, edition or page.
- Never put textbook text beyond the short locator phrases into `mds-answer-engine` (public) or the site.

## 4. Build the answers (the new standard)

1. `cp -r ~/mds-answer-engine/templates/canonical_topic ~/mds-answer-engine/<topic>` and work there. It holds `locators.py`, `build_audit.py`, `_QUESTIONS.md`, `canonical/QNN_Template_CANONICAL.md` and `AUDIT_REPORT_TEMPLATE.md`. (`legacy_v1_tools/` is for old-layout answers only; do not use it.)
2. **Locators first.** In `locators.py` fill `F` (chapter files, offsets, in-text citations) and `L` (verbatim phrases, under about 25 words, clean of OCR damage). `python3 locators.py` must print `missing 0`.
3. **Draft one definitive, examination-ready answer per question**, largest marks first. File: `<topic>/canonical/QNN_<Short_Title>_<marks>m_CANONICAL.md` (predicted: `PN_..._<marks>m_PREDICTED_CANONICAL.md`). The rules, in short (full text: SKILL 7.1 item 12 and ANSWER_GUIDE section 5):
   - The answer **is** the teaching text and the exam script: one layer, no Study Mode / Exam Mode, no `✎ Exam core`. Write in exam language from the first sentence; the answer must stand alone.
   - Header is `# <question exactly as set>` then `**Marks:** <n> · <type>`. For **10- and 20-mark** questions add a one-line `**Answer blueprint:** A → B → C → …` giving the exact heading sequence to reproduce.
   - Structure follows the command word and question: short introduction/definition, question-specific headings, mechanism or rationale and clinical significance where relevant, short conclusion. Use tables for comparisons, numbered steps for procedures, classifications where asked. Do not force a generic template.
   - Word ranges are **calibration, not targets**: 100m 3200-3500, 75m 2550-3000, 50m 1700-2000, 25m 850-1000, 20m 680-800, 15m 510-600, 10m 320-400, 7m 230-280, 5m 160-200. Never pad to reach them and never drop essential scoring content to meet them. Leave about 150 words of headroom at 50m and above for the audit to add to.
   - Add a short hand-reproducible diagram/flowchart/table cue (title, elements, labels) only where it would genuinely earn marks, e.g. `**Diagram:** Frank's four types, side by side.` Bold only key definitions, principles, distinctions, values and clinical implications.
   - **Not in the student file:** retrieval reports, search queries, source inventories, locators, `[SRC]`/`[RECALL]`/`[Certain]` tags, overlap reports, generation diagnostics, mnemonics, generic high-yield recaps, generic common-mistake lists. Put anything genuinely important into the relevant section.
   - **Citations:** author-year in the prose, naming the chapter author, e.g. (Terauchi and Renton, 2021). End with `## References`: a **numbered Vancouver-style list ordered by first citation**. No numeric in-text markers. Never invent authors, years, editions, pages or DOIs.
   - **Where books disagree**, name each author and show them side by side (a small table works); never rank or silently pick one. If a book is plainly wrong, say so and why. Interpretive or unsourced statements must be written as reasoning, not as a cited fact.
   - Each answer is independent: a short answer may point to a longer one, but must not depend on it.
4. **Audit sidecar for every answer:** copy `AUDIT_REPORT_TEMPLATE.md` to `<topic>/audit/<same name as the answer, _CANONICAL replaced by _AUDIT>.md`. Fill: the `**Student-facing answer:**` path, retrieval record, `<!--LOC: key, key, …-->` (every locator key behind the answer), evidence/uncertainty notes (`[RECALL]`, conflicts, numbers with sources), coverage and overlap, revision history. The sidecar stays in the engine repo and is **never published to the site**.
5. Check each answer: `cd <topic> && python3 build_audit.py audit/<ID>_*_AUDIT.md` (all sidecars: `audit/*_AUDIT.md`). It resolves every LOC key, rebuilds the ledger between `<!--LEDGER START-->` and `<!--LEDGER END-->`, and stamps the result. Clean means: `missing 0`, `quotes not found 0`, body words in range (or the shortfall is a deliberate, noted choice), `cited surnames not in references: none`. Review every "body numbers without a locator" entry: add a locator or reword to what the book says. Re-run after every edit.

## 5. Parallel drafting (optional)

Several questions can be drafted at once by subagents, one per answer or per group, provided each writes only its own files (its own `locators_<QID>.py` merged into `locators.py`, its own answer, its own sidecar) and no two edit the same file. See how `apexification/locators.py` merges `locators_*.py`. A subagent's output is a draft: you still run section 6 yourself.

## 6. Second-reader check and textbook audit (always, before calling the topic done)

1. `build_audit.py` clean on every sidecar (section 4 step 5).
2. Re-read each answer for statements with no locator behind them; reword to what the book says, or move them to the sidecar as `[RECALL]`/interpretation. Remove anything assumed.
3. **Audit against the other textbooks** in the standing list for the subject: look for (a) facts an exam answer needs that the draft lacks (classifications, numbers, test methods, protocols); (b) conflicts between books, shown side by side with your reasoning; (c) textbook slips. Add locators for everything you add and keep the answer in range.
4. Write `<topic>/audit/AUDIT_<date>.md`: checks done, additions per answer, conflicts, slips, open points.
5. Confirm before publishing: stands alone; headings form a usable exam sequence; depth fits the marks; every citation traceable; references complete and in one format; any visual cue earns its place; no audit/generation material left in the student file.

## 7. Publish and record

1. **Answer Bank site** (WORKFLOW.md Rule 7): `cd ~/mds-answer-bank && git pull`, then
   `python3 scripts/add_answers.py "<Subject>" "<Topic name>" ~/mds-answer-engine/<topic>/canonical/`
   (Subject is exactly `Conservative Dentistry`, `Dental Materials`, `Endodontics` or `Recent Advances`; if the topic spans subjects, run it once per subject.) Publish **only** `canonical/`, never `audit/`. Check `git status` (only your topic, `manifest.json` and index pages), then commit and push. The site rebuilds in about 2 minutes; open the topic page to check. Record the printed `manifest N -> M entries, 0 lost` line. On a rejected push or manifest conflict: abort, `git fetch && git reset --hard origin/main`, re-run the script, push. Never hand-edit `manifest.json`; never delete anyone's answer.
2. **Engine repo** (`git pull --rebase` first): update the topic row in `WORKFLOW.md` (status, answers with marks, body words against range, locator count, audit ledger, site manifest line), add a status line at the top of `HANDOFF.md`, write `<topic>/HANDOFF_<topic>.md` (file table, sources and offsets, open points), commit and push to `main`. On a conflict in a shared file keep both sides' lines.
3. Commit messages end with the attribution lines the session gives you.

## 8. Report back

A short summary: the topic and its answers with marks and body words against the range; the sources; book conflicts and how handled; what was not verified; the links (site topic page, files). Then say "Vault and OneDrive copies are for Niranjan to sync" and propose the next unclaimed topic.

## Lessons from earlier topics

- Phillips' extraction breaks words with a soft hyphen at line ends: the template's `norm()` handles it. If a phrase still goes missing, look at the raw text (`cat -A`) before rewording.
- `build_audit.py` ignores quoted phrases under 12 characters. Short quoted single words in prose are fine.
- Retrieval notes must not claim a source lacks something until you have grepped all the books (an early corrosion draft wrongly said no book mentioned Brånemark).
- Sign conventions, editions (e.g. ISO part counts by year) and terminology are the usual sources of apparent conflict between books: say which it is.
- The conversion to the new layout cut some verified material for length; if you must cut, note what was cut in the sidecar so a later editor can restore it.
- `ANSWER_GUIDE.md` is the longer explanation of the same method; if the two ever disagree, SKILL Section 7.1 item 12 wins, then this file.
