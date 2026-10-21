# ANSWER STANDARD (canonical answer format)

**Status:** DRAFT v0.2 (2026-10-21). **Not in force.** Answers continue to be drafted under SKILL.md §7 unchanged. This file is applied later, as a separate reformat pass, once all answers are finished. It overrides nothing until then.

Items marked **OPEN** are undecided.

---

## 0. What applying this file does

**Reformat only.** It renames and reorders headings, normalises the header block, citation style and file names, and moves audit material into one section. **The wording of answers is not changed.** Anything that would need new or removed content (a missing required section, Exam Mode over its word ceiling, confidence tags, dashes in prose) is **reported** in a per-topic list for a later decision. It is never fixed silently.

## 1. File

- One question per file, inside its topic folder: `<topic>/QNN_<Short_Title>_<marks>m.md`.
- Predicted questions: `PNN_<Short_Title>_predicted.md`.
- Audit ledgers (`A1_Audit_Ledger_*.md`), dossiers and `_QUESTIONS.md` are not answers; this standard does not apply to them.
- **OPEN:** the root-level GIC `draft_*.md` / `*_resolved.md` files (folder, naming, and which copy is final).

## 2. Header block (fixed lines, in this order)

```
# QNN. <Question wording exactly as in the master repository>

**Marks:** <n> (<Short Note | Short Essay | Long Essay | Essay>) — <Month Year> (<Paper code>)
**Repeats absorbed:** "<wording>" (<n>m, <Month Year>, <code>); ... | None
**Scope note:** <one line, only if the answer is narrowed or cross-refers to another file> (omit otherwise)
**Failure disclosure:** <numbered known limits> | None
```

`**Marks:**` is the line `build_manifest.py` parses; its spelling is fixed.

## 3. Sections (exact `##` headings, exact order)

| # | Heading | Required? | Notes |
|---|---|---|---|
| 1 | `## RETRIEVAL REPORT` | yes | Queries run, files hit, final bullet "No usable result for: ..." |
| 2 | `## STUDY MODE` | yes | `### S1. ...`, `### S2. ...` |
| 3 | `## CRITICAL EVIDENCE SYNTHESIS` | if present | Plain heading; scope (e.g. "compressed, one claim") becomes the first body line. |
| 4 | `## EXAM MODE` | yes | First line: `**(<words> words; about <min> min at 22 words/min)**` |
| 5 | `## DIAGRAMS TO DRAW` | if present | |
| 6 | `## HIGH-YIELD POINTS` | **yes** | |
| 7 | `## COMMON EXAM MISTAKES` | **yes** | |
| 8 | `## MNEMONIC` | if present | |
| 9 | `## REFERENCES` | yes | Alphabetical, full reference. |
| 10 | `## AUDIT LOG` | if any audit material exists | Always last. See §5. |

A required section that is missing is reported, not written.

## 4. Heading map (old → canonical)

| Found in files | Becomes |
|---|---|
| `Retrieval Report`, `Retrieval Report — AUDITED ...` | `RETRIEVAL REPORT` (suffix text moves to AUDIT LOG) |
| `CRITICAL EVIDENCE SYNTHESIS (<anything>)`, `(6A)` etc. | `CRITICAL EVIDENCE SYNTHESIS` (sub-parts become `###`) |
| `SOURCE LIST` | `REFERENCES` |
| `SOURCE LOCATORS` | `### Source locators` inside AUDIT LOG |
| `TEXTBOOK AUDIT APPLIED (...)`, `Corrections made ...`, `Known gaps ...`, `Not yet drafted` | `### <date> <original title>` inside AUDIT LOG |
| `DIFFERENCES BETWEEN TEXTBOOKS` | **OPEN:** AUDIT LOG, or `###` inside STUDY MODE (it is answer content) |
| `QUESTION (<marks>, <type>)` | header block lines |
| any other unknown `##` | reported |

## 5. AUDIT LOG layout

```
## AUDIT LOG
### Source locators
- <file>, <PDF page marker>: "<quote under 12 words>"
### 2026-10-16 Textbook audit applied
<original text, unchanged>
```

Source locators first, then dated entries, oldest first.

## 6. Citations and tags

- In-text author-year: `(McCabe and Walls, 2008)`, `(Mount et al, 2016)`, multiple separated by `;`.
- Old `[SRC:A13]` style: **OPEN** (converting needs a lookup table, which is close to a content edit).
- `[RECALL]` for unverified memory, never with bibliographic detail.
- `[Certain]` / `[Likely]` / `[Guessing]` only on claims without a citation. Not enforced by the reformat pass; reported only.

## 7. Report produced per topic when applied

Missing required sections; Exam Mode over the §7.1(3) ceiling; unknown headings; in-text citations missing from REFERENCES; leftover `[SRC:...]` tags; files that could not be mapped automatically.
