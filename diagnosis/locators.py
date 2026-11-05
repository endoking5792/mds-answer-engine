import re, os, glob, importlib.util
# Verbatim-phrase locators for the Diagnosis topic. Each drafting agent keeps its own file
# loc_<name>.py defining F (source key -> (chapter file, offset, citation)), L (locator key ->
# (source key, verbatim phrase)), BOOK and LIT (reference key -> full reference). Keys carry the
# agent's prefix so files never collide. This file merges them.
# Run `python3 locators.py`: it must print "missing 0".
T = os.path.expanduser('~/mds-textbooks/')
F, L, BOOK, LIT = {}, {}, {}, {}
_here = os.path.dirname(os.path.abspath(__file__))
for _p in sorted(glob.glob(os.path.join(_here, 'loc_*.py'))):
    _s = importlib.util.spec_from_file_location(os.path.basename(_p)[:-3], _p)
    _m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
    for _name, _d in (('F', F), ('L', L), ('BOOK', BOOK), ('LIT', LIT)):
        for _k, _v in getattr(_m, _name, {}).items():
            if _k in _d and _d[_k] != _v:
                raise SystemExit(f'key clash {_name}[{_k}] in {_p}')
            _d[_k] = _v
def norm(s):
    s = s.replace('­ ', '').replace('­', '').replace('‐', '-')
    s = re.sub(r'\s+', ' ', s).replace('- ', '')
    return s.strip()
_cache = {}
def _pages(path):
    if path in _cache: return _cache[path]
    txt = open(path, encoding='utf8').read()
    parts = re.split(r'(?:<!-- PDF page (\d+) -->|===== PAGE (\d+) =====)', txt)
    pages = {}
    if len(parts) == 1: pages[1] = txt
    for i in range(1, len(parts), 3):
        cur = int(parts[i] or parts[i+1]); pages[cur] = pages.get(cur, '') + ' ' + parts[i+2]
    _cache[path] = {k: norm(v) for k, v in pages.items()}
    return _cache[path]
def find(key):
    f, ph = L[key]; path = F[f][0]
    pages = _pages(path); n = norm(ph)
    hits = [p for p, t in pages.items() if n in t]
    if hits: return hits[0], None
    ks = sorted(pages)
    for a, b in zip(ks, ks[1:]):
        if n in pages[a] + ' ' + pages[b]: return a, None
    return None, None
def page_label(key):
    p, _ = find(key); off = F[L[key][0]][1]
    if p is None: return None
    if off is None: return f"PDF p.{p}"
    return f"PDF p.{p} (printed p.{p-off})"
if __name__ == '__main__':
    import sys
    pref = sys.argv[1] if len(sys.argv) > 1 else ''
    bad = n = 0
    for k in L:
        if not k.startswith(pref): continue
        n += 1
        if page_label(k) is None: bad += 1; print('MISSING', k, L[k][1][:70])
    print('checked', n, 'missing', bad)
