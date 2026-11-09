# How to draft answers the way Niranjan does (guide for Rosy, Medhinir and any new collaborator)

This is the practical companion to the governing skill (`skill/dental-study-material-SKILL.md`, Section 7) and `WORKFLOW.md`. It describes the current method (October 2026): **one canonical answer per question**, built directly from the textbooks, with every textbook fact traceable to a verbatim phrase on a page. The finished worked example of the current standard is `apexification/` (5 answers with audit sidecars); `procedural_errors/` (12 answers, 378 verified locators) shows question grouping and locators in the older layout. For a fresh session, `SESSION_PROMPT.md` is the step-by-step instruction.

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
3. Check whether a file is complete: one extract (Walton & Torabinejad 3rd ed Ch.18) stopped half way; the 6th edition was complete. Record the retrieval limitation in the internal audit sidecar, not in the student-facing answer.
4. Get the chapter author(s) from the chapter's first lines and cite by author-year (e.g. "Terauchi and Renton, 2021" for Cohen's Ch.20). If the author line is garbled, decode it and flag it as "verify against the printed book".
5. Work out the page offset per chapter: find a visible printed page number next to a `<!-- PDF page N -->` marker at two or more places. If you cannot confirm it, cite the PDF page only (`offset None`). Offsets differ between chapters of the same book.

## 4. Write the locators first

Copy `templates/canonical_topic/` to `<topic>/`. In `locators.py`:
- `F` lists each chapter file with its offset and its in-text citation.
- `L` lists every fact you will cite as a **verbatim phrase** (under about 25 words) from that file.
- Choose clean phrases: avoid OCR ligature damage (`0e`, `!le`, `#e`), words split by hyphens, and figure captions.

Run `python3 locators.py`. It must print `missing 0`. Fix or replace every missing phrase; never keep a fact whose phrase you cannot find.

## 5. Draft one definitive examination-ready answer per question

File: `<topic>/canonical/QNN_<Short_Title>_<marks>m_CANONICAL.md` (or the agreed topic-specific filename).

**The answer is the teaching text and the examination script.** Do not write a separate Study Mode explanation followed by an Exam Core. Students should be able to read the answer and reproduce the same structure and content in the examination.

For 10- and 20-mark questions, begin with a compact **Answer blueprint** that previews the exact heading sequence to reproduce. The body then follows that sequence. Use a concise introduction/definition, question-specific main headings, mechanism/rationale where relevant, clinical significance/applications where relevant, and a concise conclusion. Adapt to the command word: use tables for comparisons, numbered steps for procedures, classifications where asked, and evidence synthesis only when the question warrants it.

Write comprehensively but economically. Retain established Section 7 mark-based word ranges as calibration, not as a target that justifies padding or omission. Include only material with direct examination, scientific or clinical value. Do not force a generic section structure onto every question.

Assess whether a hand-reproducible diagram, flowchart, algorithm or table would materially improve the answer. Include a brief drawing cue with title, elements and labels. Bold only key definitions, principles, distinctions, values and clinical implications.

**Remove from student-facing answers:** retrieval reports, source-search queries, source inventories, verbatim locator lists, overlap/repeat reports, generation diagnostics, mnemonics, generic high-yield recaps and generic common-mistake lists. Incorporate any genuinely important content into the main answer.

**Citations:** use author-year attribution in the prose, naming chapter authors where verified. End with a numbered reference list formatted in Vancouver bibliographic style and ordered by first citation. This is the agreed hybrid: author-year in-text citations plus Vancouver-formatted bibliography. Never invent bibliographic details or page numbers.

## 6. Build sources, audit and check

Keep source provenance separate from the student-facing answer.

- Use `locators.py` to verify each [SRC] phrase against the source file. It must print `missing 0`.
- Write one audit sidecar per answer (`<topic>/audit/<ID>_..._AUDIT.md`, from `templates/canonical_topic/AUDIT_REPORT_TEMPLATE.md`) listing its locator keys in `<!--LOC: ... -->`, then run `python3 build_audit.py audit/<ID>_*_AUDIT.md` from the topic folder. It resolves every key, rebuilds the ledger, checks that quoted phrases are verbatim, that cited surnames match the reference list, that body numbers have a locator, and the body word count against the Section 7 calibration range. (`templates/canonical_topic/legacy_v1_tools/` holds the old `build_sources.py` / `check_answers.py` for the superseded Explanation + Exam core layout only.)
- Save the retrieval report, source inventory, verbatim locators, [RECALL] or uncertainty flags, overlap notes, and revision history in a per-question audit sidecar under `<topic>/audit/`. Use `templates/canonical_topic/AUDIT_REPORT_TEMPLATE.md`.
- The audit sidecar is an internal editing record; do not publish it to the Answer Bank or include it in the student-facing Markdown.
- The student-facing answer retains its author-attributed prose citations and Vancouver-formatted reference list.
- Reuse verified passages and topic dossiers. Do not repeat retrieval or live searches if the existing evidence is sufficient. Re-run only the checks affected by a substantive edit.

Before publishing, confirm: the answer stands alone; its headings form a usable exam sequence; the depth is appropriate for the marks; citations are traceable; references are complete and consistently formatted; visuals add value; no generation/audit material or redundant study/exam layer remains.
 
## 7. Publish (additive only)

Publish to the **Answer Bank site** (https://mds-answer-bank.pages.dev) following **WORKFLOW.md Rule 7**: in `~/mds-answer-bank`, `git pull`, then `python3 scripts/add_answers.py "<Subject>" "<Topic>" <topic>/canonical/`, then commit and push (the script strips `_CANONICAL`, never deletes, and prints the manifest count before -> after). Do not publish to the old Answer Bank artifact (frozen at Version 65). Then copy the files to your vault if you keep one. Do not build `.docx` files unless asked (skill Section 7.1 item 13).

## 8. Record and push

Update the topic row in `WORKFLOW.md`, add a status line to the top of `HANDOFF.md`, keep a short `<topic>/HANDOFF_<topic>.md` (file table, sources and offsets, open points), commit and push. Never commit textbook passages beyond the short locator phrases: this repo is public.

## Reference: worked examples

`apexification/` is the first topic written to the unified standard (student answers in `canonical/`, sidecars in `audit/`, `build_audit.py`, `HANDOFF_apexification.md`). The table below describes `procedural_errors/`, which is useful for question grouping and locators but uses the superseded Explanation + Exam core layout.

### `procedural_errors/`

| File | Shows |
|---|---|
| `_QUESTIONS.md` | Grouping 31 sittings into 9 answers + 3 predicted |
| `canonical/Q01_..._75m` | Umbrella essay, 11 sections, exam core 2947 words |
| `canonical/Q05_..._100m`, `Q09_..._100m` | 100-mark answers built from 6-9 chapters |
| `canonical/Q02_..._20m` | Detection/correction/prevention table format |
| `canonical/Q08_..._10m` | 10-mark list-and-table format |
| `locators.py` | 378 verified phrases across 14 chapter files |
| `HANDOFF_procedural_errors.md` | Offsets, source conflicts, open points |
