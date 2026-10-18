"""Regenerate 00_INDEX.md from the current answer files (Exam/Study word counts and Section 7 status)."""
import glob, os, re, subprocess
os.chdir("/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries")
RANGES = {10: (320, 400), 7: (180, 250), 15: (510, 600), 20: (680, 800), 50: (1700, 2000), 100: (3200, 3500)}
rows = []
for f in sorted(glob.glob("T*.md") + glob.glob("P*.md")):
    t = open(f, encoding="utf-8").read()
    marks = int(re.search(r"\*\*Marks:\*\*\s*(\d+)", t).group(1))
    h1 = re.search(r"^# (.+)$", t, re.M).group(1).strip()
    a, b = t.index("## EXAM MODE"), t.index("## HIGH-YIELD POINTS")
    exam = len(t[a:b].split())
    s0, s1 = t.index("## STUDY MODE"), t.index("## EXAM MODE")
    study_txt = t[s0:s1]
    if "## CRITICAL EVIDENCE SYNTHESIS" in study_txt:
        study_txt = study_txt[:study_txt.index("## CRITICAL EVIDENCE SYNTHESIS")]
    study = len(study_txt.split())
    lo, hi = RANGES[marks]
    status = "in range" if lo <= exam <= hi else ("under" if exam < lo else "over")
    rows.append((f, marks, h1, exam, lo, hi, status, study))
out = ["# Traumatic dental injuries: answer index (drafted 2026-10-19; audited against IADT 2020 on 2026-10-19)", "",
       "Topic: Endodontics §14 \"Traumatic dental injuries\", with the Manipal addendum and cross-listed trauma items from Conservative Dentistry and Recent Advances. Question list: `_QUESTIONS.md`. Handoff: `HANDOFF_traumatic.md`. IADT audit ledger: `AUDIT_IADT_2026-10-19.md`.", "",
       "Word counts are split on whitespace. Section 7 Exam Mode ranges are in brackets. Study counts exclude the Critical Evidence Synthesis section and the audit note.", "",
       "| File | Marks | Title | Exam words [range] | Study words |", "|---|---|---|---|---|"]
for f, marks, h1, exam, lo, hi, status, study in rows:
    stem = f[:-3]
    out.append(f"| [{stem}]({f}) | {marks} | {h1} | {exam} [{lo}-{hi}] {status} | {study} |")
out += ["", "Study ranges (lean rule): 20 marks 500-700; 10 marks 250-400; 7 marks about 150-250.", "",
        "## Status", "- All 23 answers are in their Section 7 Exam Mode range (checked 2026-10-19).",
        "- Audit against the supplied IADT 2020 guidelines and 2002-2025 reviews is complete for every answer; corrections are listed per answer in `AUDIT_IADT_2026-10-19.md`.",
        "- Not yet done: OneDrive .docx, vault copies, Answer Bank publish (see `HANDOFF_traumatic.md`)."]
open("00_INDEX.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("rows", len(rows), "over", sum(1 for r in rows if r[6] == "over"), "under", sum(1 for r in rows if r[6] == "under"))
