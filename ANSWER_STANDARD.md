# ANSWER STANDARD (canonical format for every exam answer)

**Status:** DRAFT v0.1 (2026-10-21), under discussion. Once approved, this file replaces the format rules of SKILL.md §7.3 (Master Prompt OUTPUT ORDER) and the citation clause of §7.1(2). Content rules (sources, [SRC]/[LIT]/[RECALL], word ceilings in §7.1(3), lean mode §7.1(9)) stay in SKILL.md. Where the two disagree on FORMAT, this file wins.

Items marked **OPEN** are not decided yet.

---

## 1. File

- One question per file, inside its topic folder: `<topic>/QNN_<Short_Title>_<marks>m.md`.
- Predicted questions: `PNN_<Short_Title>_predicted.md`. Topic audit ledgers: `A1_Audit_Ledger_<date>.md` (not answers; this standard does not apply to them).
- **OPEN:** the root-level `draft_*.md` / `*_resolved.md` files (GIC). Move into a `gic/` folder and rename to this scheme?

## 2. Header block (fixed lines, in this order)

```
# QNN. <Question wording exactly as in the master repository>

**Marks:** <n> (<Short Note | Short Essay | Long Essay | Essay>) — <Month Year> (<Paper code>)
**Repeats absorbed:** "<wording>" (<n>m, <Month Year>, <code>); ... | None
**Scope note:** <one line, only if the answer is deliberately narrowed or cross-references another file> (omit line otherwise)
**Failure disclosure:** <numbered list of known limits: no journals read, source conflicts, [RECALL] items, page-marker caveat> | None
```

Rules: `**Marks:**` is the line `build_manifest.py` parses, so its spelling never changes. Highest-marks version is the file's marks; repeats are listed, never answered twice.

## 3. Sections (exact `##` headings, exact order)

| # | Heading | Required? | Notes |
|---|---|---|---|
| 1 | `## RETRIEVAL REPORT` | always | Queries run and which books/files hit; final bullet "No usable result for: ..." |
| 2 | `## STUDY MODE` | always | Subsections `### S1. ...`, `### S2. ...`. No word cap; length guide per §7.1(9a). |
| 3 | `## CRITICAL EVIDENCE SYNTHESIS` | 20m and above, or any "critically" question | Heading has no suffix. Scope (claims count) goes in the first line of the body, not the heading. |
| 4 | `## EXAM MODE` | always | First line: `**(<words> words; about <min> min at 22 words/min)**`. Must stand alone (no "see Study Mode"). Ceiling per §7.1(3). |
| 5 | `## DIAGRAMS TO DRAW` | always (write "None needed" if none) | |
| 6 | `## HIGH-YIELD POINTS` | always | 4 to 8 bullets. |
| 7 | `## COMMON EXAM MISTAKES` | always | |
| 8 | `## MNEMONIC` | always | One mnemonic, expanded. |
| 9 | `## REFERENCES` | always | Alphabetical, full reference. Journals with DOI/PubMed link; say "abstract only" where true. |
| 10 | `## AUDIT LOG` | when any change after first draft | Last section. Dated entries, newest last: `- 2026-10-16 (textbook audit): <what changed and why>`. |

Retired headings (map on migration): `SOURCE LIST` and `SOURCE LOCATORS` → `REFERENCES`; `TEXTBOOK AUDIT APPLIED (...)`, `Corrections made...`, `DIFFERENCES BETWEEN TEXTBOOKS` → `AUDIT LOG` (differences kept as text inside Study Mode); `Retrieval Report` (any case/suffix) → `RETRIEVAL REPORT`; `CRITICAL EVIDENCE SYNTHESIS (<anything>)` → plain heading; `QUESTION (...)` headers → header block.

## 4. Citations and tags

- In-text author-year only: `(McCabe and Walls, 2008)`, `(Mount et al, 2016)`, multiple separated by `;`. No `[SRC:A13]`, no `[n, p.X]`.
- Every cited work appears in REFERENCES; nothing in REFERENCES is uncited.
- `[RECALL]` for unverified memory, never with author, year, edition or page.
- Confidence tags `[Certain]` / `[Likely]` / `[Guessing]`. **OPEN:** on every claim, or only on claims that are not directly sourced?
- Source disagreements are shown side by side with each book named, never smoothed.

## 5. Style

- No em or en dashes in prose (the `—` in the Marks line is the one exception). **OPEN:** confirm, and whether existing files get swept.
- British spelling (existing files use it).
- Exam Mode uses `###` sub-headings, short paragraphs and lists; tables allowed if they convert in `md2docx.py`.

## 6. Validation

`tools/check_answer.py` (to be written) fails a file if: header lines missing or misordered; a required section missing; sections out of order; an unknown `##` heading; Exam Mode word count above the ceiling for its marks; an in-text citation absent from REFERENCES.

## 7. Migration

Structure-only, topic by topic, one commit per topic: rename/reorder headings, move audit notes into AUDIT LOG, merge SOURCE LOCATORS into REFERENCES. Wording of answers is not touched. Files over the word ceiling are reported, not trimmed, unless you say otherwise.
