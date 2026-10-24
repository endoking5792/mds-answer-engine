import re, os, glob
# Verbatim-phrase locators for gingival_tissue. Each drafting group keeps its own file in parts/
# (parts/<X>.py) and calls src(), add() and book() there; this file merges them.
# Run `python3 locators.py`: it must print "missing 0" before publishing.
T = os.path.expanduser('~/mds-textbooks/')
OP = T+'Operative_and_Dental_Materials_Textbooks/'
HERE = os.path.dirname(os.path.abspath(__file__))
F, L, BOOK = {}, {}, {}
def src(key, path, off, cite):
    # offset int: printed page = PDF marker - offset; None: cite PDF page only
    if key in F: assert F[key] == (path, off, cite), 'source key clash: '+key
    F[key] = (path, off, cite)
def add(f, d):
    for k, v in d.items():
        assert k not in L, 'locator key clash: '+k
        L[k] = (f, v)
def book(key, ref):
    if key in BOOK: assert BOOK[key] == ref, 'ref key clash: '+key
    BOOK[key] = ref
for p in sorted(glob.glob(os.path.join(HERE, 'parts', '*.py'))):
    exec(open(p, encoding='utf8').read())
def norm(s):
    s = s.replace('­ ', '').replace('­', '').replace('‐', '-')
    s = re.sub(r'\s+', ' ', s).replace('- ', '')
    return s.strip()
_cache = {}
def _pages(path):
    if path in _cache: return _cache[path]
    if path.endswith('.pdf'):
        import fitz
        d = fitz.open(path); pages = {i+1: p.get_text() for i, p in enumerate(d)}
    else:
        txt = open(path, encoding='utf8').read()
        parts = re.split(r'(?:<!-- PDF page (\d+) -->|===== PAGE (\d+) =====)', txt)
        pages = {}
        for i in range(1, len(parts), 3):
            cur = int(parts[i] or parts[i+1]); pages[cur] = pages.get(cur, '')+' '+parts[i+2]
    _cache[path] = {k: norm(v) for k, v in pages.items()}
    return _cache[path]
def find(key):
    f, ph = L[key]; path, off, cite = F[f]
    pages = _pages(path); n = norm(ph)
    hits = [p for p, t in pages.items() if n in t]
    if hits: return hits[0], None
    ks = sorted(pages)
    for a, b in zip(ks, ks[1:]):
        if n in pages[a]+' '+pages[b]: return a, None
    return None, None
def page_label(key):
    p, _ = find(key); f = L[key][0]; off = F[f][1]
    if p is None: return None
    if off is None: return f"PDF p.{p}"
    return f"PDF p.{p} (printed p.{p-off})"
if __name__ == '__main__':
    import sys
    only = sys.argv[1] if len(sys.argv) > 1 else None   # optional key prefix, e.g. "a_"
    bad = n = 0
    for k in L:
        if only and not k.startswith(only): continue
        n += 1
        if page_label(k) is None: bad += 1; print('MISSING', k, L[k][1][:70])
    print('checked', n, 'missing', bad)
