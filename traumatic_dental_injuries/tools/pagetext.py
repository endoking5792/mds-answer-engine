"""Print non-empty lines of a chapterwise .md between two PDF page markers (inclusive).
Usage: python3 pagetext.py FILE START END [MAXCHARS]"""
import re, sys
path, s, e = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 500
mk = None
for i, line in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
    m = re.search(r'PDF page (\d+)', line)
    if m:
        mk = int(m.group(1)); continue
    if mk is not None and s <= mk <= e and line.strip():
        print(f"[p{mk}] {line.strip()[:mx]}")
