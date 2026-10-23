# How to draft answers the way Niranjan does (guide for Rosy, Medhinir and any new collaborator)

This is the practical companion to the governing skill (`skill/dental-study-material-SKILL.md`, Section 7) and `WORKFLOW.md`. It describes the current method (October 2026): **one canonical answer per question**, built directly from the textbooks, with every textbook fact traceable to a verbatim phrase on a page. The finished worked example is `procedural_errors/` (12 answers, 378 verified locators). Copy its pattern.

## 0. One-time setup

1. Clone this repo and the private textbook repo side by side:
   ```bash
   git clone https://github.com/endoking5792/mds-answer-engine.git
   ```
   ```bash
   git clone https://github.com/endoking5792/mds-textbooks.git ~/mds-textbooks
   ```
   The scripts expect the textbooks at `~/mds-textbooks/` (chapterwise Markdown, with `<!-- PDF page N -->` markers). If you clone elsewhere, change `T = ...` at the top of your topic's `locators.py`.
2. Install the skill so Claude Code loads it:
   ```bash
   mkdir -p ~/.claude/skills/dental-study-material && cp skill/dental-study-material-SKILL.md ~/.claude/skills/dental-study-material/SKILL.md
   ```
   Re-copy it whenever you `git pull` and the skill file has changed.
3. Python 3 is enough for the tools (stdlib only; `pymupdf` only if you read a PDF source directly).
4. Paths in the skill that point at Niranjan's Mac (OneDrive, `/Users/niranjan/...`, the Obsidian vault) are his; use your own equivalents. The textbook content you need is all in `mds-textbooks`.

## 1. Claim a topic

Read `WORKFLOW.md` (Rules 1-7) and `HANDOFF.md`. Add a row to the claim table in `WORKFLOW.md` with your name and date, commit and push **before** you start, so two people never draft the same topic.

## 2. Compile and agree the question list

1. Open the topic's section in the master repository (`<SUBJECT>_MASTER_REPOSITORY.md`, in the Question Paper Bank). Also search the other repositories and the Manipal/other addenda for the same topic (e.g. instrument separation sat under both Instruments and Procedural Errors).
2. Group repeat wordings. Answer each distinct question **once, at its highest marks**, and list the other wordings/sittings as "absorbed". Keep question wording exactly as printed.
3. Write the grouping into `<topic>/_QUESTIONS.md` (template in `templates/canonical_topic/`). Add 2-3 **predicted** questions if useful, marked PREDICTED.
4. **Show the list to the person whose answers these are and agree it before drafting** (they may upgrade marks, e.g. Niranjan asked for Perforation and Ledge as 100-markers, or add a textbook).

## 3. Find and read the sources

1. Find candidate chapters by content, not by memory:
   ```bash
   cd ~/mds-textbooks && for f in */*.md; do n=$(grep -o -i "perforat" "$f" | wc -l); [ $n -gt 25 ] && echo "$n $f"; done | sort -rn | head
   ```
2. **Read the chapters, do not just count hits.** A dedicated chapter in a less obvious book (e.g. *Endodontology* Ch.43 "Perforations", *Problems in Endodontics* Ch.17, the complete 6th edition of Torabinejad's *Endodontics: Principles and Practice*) often beats the big textbook.
3. Check whether a file is complete: one extract (Walton & Torabinejad 3rd ed Ch.18) stopped half way; the 6th edition was complete. Say so in the answer's retrieval report.
4. Get the chapter author(s) from the chapter's first lines and cite by author-year (e.g. "Terauchi and Renton, 2021" for Cohen's Ch.20). If the author line is garbled, decode it and flag it as "verify against the printed book".
5. Work out the page offset per chapter: find a visible printed page number next to a `<!-- PDF page N -->` marker at two or more places. If you cannot confirm it, cite the PDF page only (`offset None`). Offsets differ between chapters of the same book.

## 4. Write the locators first

Copy `templates/canonical_topic/` to `<topic>/`. In `locators.py`:
- `F` lists each chapter file with its offset and its in-text citation.
- `L` lists every fact you will cite as a **verbatim phrase** (under about 25 words) from that file.
- Choose clean phrases: avoid OCR ligature damage (`0e`, `!le`, `#e`), words split by hyphens, and figure captions.

Run `python3 locators.py`. It must print `missing 0`. Fix or replace every missing phrase; never keep a fact whose phrase you cannot find.

## 5. Draft one canonical answer per question

File: `<topic>/canonical/QNN_<Short_Title>_<marks>m_CANONICAL.md` (template provided). Structure, as in Section 7.1 item 12 of the skill:

- Header: question exactly as printed, marks, sitting, absorbed repeats, the "How to read" line (with the `EXAMWORDS`/`EXAMMIN` placeholders that the script fills), and a short **retrieval report** (what was read, what was not, whether a live search was run).
- `<!--LOC: ...-->` with the locator keys used and `<!--REF: ...-->` with the reference keys.
- Numbered sections. Each has `### Explanation` (study-level reasoning; every textbook fact ends `(Author, Year) [SRC]`), then `#### ✎ Exam core` (what the student writes in the exam: headings, short paragraphs, tables, author-year citations).
- Then: CRITICAL EVIDENCE SYNTHESIS (20m and above; 25m one short claim; omit for 10m/5m unless "critically"), HIGH-YIELD POINTS, DIAGRAMS TO DRAW, COMMON EXAM MISTAKES, MNEMONIC.

Rules that matter most:
- **Exam-core length** must fall in the Section 7 range: 100m 3200-3500, 75m 2550-3000, 50m 1700-2000, 25m 850-1000, 20m 680-800, 10m 320-400, 5m 160-200 words. The script counts it and writes a FAILURE DISCLOSURE line if it is out of range. Expand from sourced material (not padding) or cut.
- **Where books disagree, name each author and show both side by side; never rank or silently pick one.** If a book is plainly wrong (e.g. "the main advantage of MTA is its long setting time" where its own next clause shows it means disadvantage), say so and show why.
- Anything not from a book read this session is `[RECALL]`, with no author, year or page attached. Use `[Certain]`/`[Likely]`/`[Guessing]` on interpretive or contested statements. A fabricated citation is a total failure; a missing one is minor.
- Each canonical answer must stand alone: a short answer may point to a longer one, but its exam core must not depend on it.
- Answer the large questions first (75m/100m), then the shorter ones reuse their locators.

## 6. Build sources and check

```bash
cd <topic> && python3 locators.py && python3 build_sources.py canonical/*.md
```
`build_sources.py` fills the word count and writing time, adds the SOURCE LIST (file, PDF page, printed page, verbatim phrase for every locator) and the alphabetical REFERENCES from `BOOK`, and flags length failures. Re-run it after every edit. Add any new reference to `BOOK`.

## 7. Publish (additive only)

Follow **WORKFLOW.md Rule 7** exactly (`publish_guard.py merge`, then publish, then compare the live manifest before and after; entries may only go up and nothing may be lost). Stage the files without the `_CANONICAL` suffix under `<Subject>/<Topic>/`. Then copy them to your vault if you keep one. Do not build `.docx` files unless asked (skill Section 7.1 item 13).

## 8. Record and push

Update the topic row in `WORKFLOW.md`, add a status line to the top of `HANDOFF.md`, keep a short `<topic>/HANDOFF_<topic>.md` (file table, sources and offsets, open points), commit and push. Never commit textbook passages beyond the short locator phrases: this repo is public.

## Reference: what to look at in `procedural_errors/`

| File | Shows |
|---|---|
| `_QUESTIONS.md` | Grouping 31 sittings into 9 answers + 3 predicted |
| `canonical/Q01_..._75m` | Umbrella essay, 11 sections, exam core 2947 words |
| `canonical/Q05_..._100m`, `Q09_..._100m` | 100-mark answers built from 6-9 chapters |
| `canonical/Q02_..._20m` | Detection/correction/prevention table format |
| `canonical/Q08_..._10m` | 10-mark list-and-table format |
| `locators.py` | 378 verified phrases across 14 chapter files |
| `HANDOFF_procedural_errors.md` | Offsets, source conflicts, open points |
