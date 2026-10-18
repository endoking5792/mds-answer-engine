"""Inventory textbook/DCNA citations in the answer files: author key, year, pages, sentence."""
import glob, re, json, sys
KEYS = [
 ("Andreasen et al, 2007", r"Andreasen et al,? 2007|Andreasen et al, 2007"),
 ("Andreasen et al, 2002", r"Andreasen et al,? 2002"),
 ("Berman", r"Berman et al|Berman's guide|Berman L|Berman"),
 ("Sigurdsson/Harty", r"Sigurdsson and Bourguignon|Harty['’]s"),
 ("Kahler/Cohen", r"Kahler|Cohen['’]s"),
 ("Trope n.d. (Ingle)", r"Trope, n\.d\.|Trope n\.d\."),
 ("Trope 2010 (DCNA)", r"Trope, 2010"),
 ("Kohli and Lee 2026", r"Kohli and Lee|Kohli and Lee,"),
 ("Hexem and Eisler", r"Hexem and Eisler"),
 ("Ogle 2024", r"Ogle,? 2024|Ogle"),
 ("Sikri", r"Sikri"),
 ("Weine", r"Weine"),
 ("Grossman", r"Grossman"),
 ("Paranjpe", r"Paranjpe"),
 ("Radiology", r"Endodontic Radiology"),
 ("AAE glossary", r"AAE"),
]
PAGE = re.compile(r"p\.\s?(\d{2,4})(?:\s?[-–]\s?(\d{2,4}))?")
rows = []
for f in sorted(glob.glob("T*.md") + glob.glob("P*.md")):
    if f.startswith("AUDIT"):
        continue
    lines = open(f, encoding="utf-8").read().split("\n")
    for ln, line in enumerate(lines, 1):
        if line.startswith("- ") or line.startswith("| "):
            pass
        for label, pat in KEYS:
            for m in re.finditer(pat, line):
                # take the parenthetical/bracket containing the author key
                seg_start = max(line.rfind("(", 0, m.start()), line.rfind("[", 0, m.start()))
                seg_end_candidates = [i for i in (line.find(")", m.end()), line.find("]", m.end())) if i >= 0]
                seg_end = min(seg_end_candidates) if seg_end_candidates else len(line)
                seg = line[seg_start:seg_end + 1] if seg_start >= 0 else line[m.start():m.end() + 60]
                pages = [(int(a), int(b) if b else None) for a, b in PAGE.findall(seg)]
                rows.append({"file": f[:3], "line": ln, "source": label, "cite": seg[:140], "pages": pages})
                break
json.dump(rows, open("sources/cite_inventory.json", "w"), ensure_ascii=False, indent=0)
from collections import Counter
c = Counter(r["source"] for r in rows)
for k, v in c.most_common():
    npg = sum(1 for r in rows if r["source"] == k and r["pages"])
    print(f"{k:24} citations={v:4} with_page={npg}")
print("total", len(rows))
