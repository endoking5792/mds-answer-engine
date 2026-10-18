"""Print regex hits in a chapterwise .md with the PDF page marker in force at each hit.

Usage: python3 pagehit.py FILE REGEX [MAX]
Markers are lines like '<!-- PDF page 476 -->'; a hit belongs to the most recent marker above it.
"""
import re, sys
path, pat = sys.argv[1], re.compile(sys.argv[2], re.I)
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 40
marker = None
n = 0
mk = re.compile(r'<!--\s*PDF page\s*(\d+)\s*-->')
for i, line in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
    m = mk.search(line)
    if m:
        marker = m.group(1)
        continue
    if pat.search(line):
        n += 1
        if n <= mx:
            print(f"[L{i} PDFp{marker}] {line.strip()[:230]}")
print(f"-- {n} hits in {path.split('/')[-1]}")
