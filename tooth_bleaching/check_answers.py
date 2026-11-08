"""Second-reader checks for a topic's canonical answers. Run from the topic folder after build_sources.py:
    python3 check_answers.py canonical/*.md
1. Every "quoted phrase" (12+ characters) in a sentence tagged [SRC] must occur verbatim in one of the books in F.
2. Every number in the exam cores must occur in one of the answer's locator phrases (citation years are ignored);
   the leftovers are printed for a manual check (list numbering, marks, years of standards are usually fine).
"""
import re, sys
import locators as l

book = ' '.join(' '.join(l._pages(v[0]).values()) for v in l.F.values())
bad = 0
for p in sys.argv[1:]:
    s = open(p, encoding='utf8').read().split('\n## SOURCE LIST')[0]
    for par in s.split('\n'):
        if '[SRC]' not in par:
            continue
        if par.count('"') % 2:
            print('ODD QUOTES', p, par[:80])
        for q in [x for x in re.findall(r'"([^"]*)"', par) if len(x) >= 12]:
            if l.norm(q) not in book:
                bad += 1
                print('QUOTE NOT IN BOOK', p.split('/')[-1][:20], '|', q[:100])
    keys = [k.strip() for k in re.search(r'<!--LOC: (.*?)-->', s, re.S).group(1).split(',') if k.strip()]
    phr = ' '.join(l.norm(l.L[k][1]) for k in keys)
    cores = ' '.join(re.findall(r'#{2,4} ✎ Exam core\n(.*?)(?=\n## (?!✎))', s, re.S))
    cores = re.sub(r'\([^()]*?(19|20)\d\d[^()]*\)', '', cores)
    left = sorted(set(n for n in re.findall(r'\d+(?:\.\d+)?', cores) if n not in phr), key=lambda x: float(x))
    print(p.split('/')[-1][:40], '| exam-core numbers without a locator:', left)
print('quotes not found:', bad)
