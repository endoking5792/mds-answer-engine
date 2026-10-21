# ANSWER STANDARD (canonical answer format)

**Status:** DRAFT v0.4 (2026-10-21). **Not in force.** Answers continue to be drafted under SKILL.md §7 unchanged. This file is applied later, as a separate reformat pass, once all answers are finished. It overrides nothing until then.

No open items remain.

---

## 0. What applying this file does

**Restructure, no new facts.** It merges Study Mode, Critical Evidence Synthesis and Exam Mode into one ANSWER (removing duplication, losing no fact, number or citation), renames and reorders headings, normalises the header block, citation style and file names, and moves audit material into one section. Anything that would need new content (a missing required section, confidence tags) is **reported** in a per-topic list for a later decision. It is never fixed silently.

## 1. File

- One question per file, inside its topic folder: `<topic>/QNN_<Short_Title>_<marks>m.md`.
- Predicted questions: `PNN_<Short_Title>_predicted.md`.
- Audit ledgers (`A1_Audit_Ledger_*.md`), dossiers and `_QUESTIONS.md` are not answers; this standard does not apply to them.
- Root-level GIC files: `*_resolved.md` is the final version of each answer; `draft_*.md` are stale copies. On applying, the resolved files move to `gic/` and are renamed to this scheme; the `draft_*.md` copies are deleted.
- A question that exists in several marks versions is one file, named by its highest marks; the other versions are listed under `**Repeats absorbed:**`.

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
| 1 | `## ANSWER` | yes | One continuous, exhaustive answer with `###` subheadings in teaching order. Merges what were Study Mode, Critical Evidence Synthesis (as a final `### Critical appraisal`) and Exam Mode. In-text (Author, year) citations. No length limit, no word-count line. |
| 2 | `## TEXTBOOK DISAGREEMENTS` | if any | Bullets; every side names author, edition and year. Not repeated in the answer body. |
| 3 | `## HIGH-YIELD POINTS` | yes | |
| 4 | `## COMMON EXAM MISTAKES` | yes | |
| 5 | `## AUDIT LOG` | yes | Always last. `### Source locators` first, each book's line starting with its full details (authors, title, edition, publisher, year), since there is no References section. Then dated entries. |

Removed sections: RETRIEVAL REPORT (anything important goes into AUDIT LOG), STUDY MODE, EXAM MODE, CRITICAL EVIDENCE SYNTHESIS (as a separate section), DIAGRAMS TO DRAW, MNEMONIC, REFERENCES. Decided by the user 2026-10-21 after the microleakage sample.

## 4. Heading map (old → canonical)

| Found in files | Becomes |
|---|---|
| `Retrieval Report`, `Retrieval Report — AUDITED ...` | `RETRIEVAL REPORT` (suffix text moves to AUDIT LOG) |
| `CRITICAL EVIDENCE SYNTHESIS (<anything>)`, `(6A)` etc. | `CRITICAL EVIDENCE SYNTHESIS` (sub-parts become `###`) |
| `SOURCE LIST`, `REFERENCES` | book details into AUDIT LOG source locators |
| `SOURCE LOCATORS` | `### Source locators` inside AUDIT LOG |
| `TEXTBOOK AUDIT APPLIED (...)`, `Corrections made ...`, `Known gaps ...`, `Not yet drafted` | `### <date> <original title>` inside AUDIT LOG |
| `DIFFERENCES BETWEEN TEXTBOOKS`, `Differences between textbooks` tables | `## TEXTBOOK DISAGREEMENTS` |
| `STUDY MODE`, `EXAM MODE`, `CRITICAL EVIDENCE SYNTHESIS` | merged into `## ANSWER` |
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
- Old `[SRC:A13]` style is converted to author-year using the dossier/`refs_meta.json` lookup; any tag that cannot be resolved is left as is and reported.
- `[RECALL]` for unverified memory, never with bibliographic detail.
- `[Certain]` / `[Likely]` / `[Guessing]` only on claims without a citation. Not enforced by the reformat pass; reported only.

## 7. Report produced per topic when applied

Missing required sections; unknown headings; in-text citations with no source locator; unresolved `[SRC:...]` tags; files that could not be mapped automatically.
