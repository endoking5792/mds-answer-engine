"""Count words in EXAM MODE and STUDY MODE sections of each answer, against the Section 7 ranges."""
import glob, os, re, sys

os.chdir("/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries")
RANGES = {  # Exam Mode ranges by marks, from 00_INDEX.md
    10: (320, 400), 7: (180, 250), 15: (510, 600), 20: (680, 800), 50: (1700, 2000), 100: (3200, 3500),
}
STUDY = {20: (500, 700), 10: (250, 400), 7: (150, 250)}


def sections(t):
    def span(a, b):
        i = t.find(a)
        if i < 0:
            return None
        j = t.find(b, i + len(a)) if b else -1
        return t[i:j] if j > 0 else t[i:]
    exam = span("## EXAM MODE", "## HIGH-YIELD POINTS")
    study = span("## STUDY MODE", "## EXAM MODE")
    if study and "## CRITICAL EVIDENCE SYNTHESIS" in study:
        study = study[:study.index("## CRITICAL EVIDENCE SYNTHESIS")]
    return exam, study


def wc(s):
    return len(s.split()) if s else 0


rows = []
for f in sorted(glob.glob("T*.md") + glob.glob("P*.md")):
    t = open(f, encoding="utf-8").read()
    m = re.search(r"\*\*Marks:\*\*\s*(\d+)", t)
    marks = int(m.group(1)) if m else 0
    exam, study = sections(t)
    e = wc(exam)
    s = wc(study)
    lo, hi = RANGES.get(marks, (0, 10**9))
    flag = "OK" if lo <= e <= hi else ("UNDER" if e < lo else "OVER")
    rows.append((f[:4], marks, e, f"{lo}-{hi}", flag, s, (STUDY.get(marks) or ("-", "-")), f))
for r in rows:
    print(f"{r[0]:5} marks={r[1]:<3} exam={r[2]:<5} range={r[3]:<11} {r[4]:<6} study={r[5]:<5} studyrange={r[6]}")
