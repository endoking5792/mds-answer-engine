import re, os
# Verbatim-phrase locators for tooth_bleaching. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.environ.get('MDS_TEXTBOOKS', os.path.expanduser('~/mds-textbooks/'))   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
import glob
# Parallel drafting: each drafter keeps its own part file loc_<id>.py defining F, L and BOOK
# (keys prefixed with the drafter id). They are merged here; duplicate keys are an error.
F, L, BOOK = {}, {}, {}
_here = os.path.dirname(os.path.abspath(__file__))
for _p in sorted(glob.glob(os.path.join(_here, 'loc_*.py'))):
    _ns = {'T': T}
    exec(open(_p, encoding='utf8').read(), _ns)
    for _name, _d in (('F', F), ('L', L), ('BOOK', BOOK)):
        for _k, _v in _ns.get(_name, {}).items():
            if _k in _d and _d[_k] != _v:
                if _name == 'BOOK': continue   # differing reference strings are reconciled at merge; first wins
                raise SystemExit(f'duplicate {_name} key {_k} in {_p}')
            _d[_k] = _v
def norm(s):
    s = re.sub(r'\u00ad\s*', '', s).replace('\u2010', '-')  # soft hyphen, also at a line end (Phillips' extraction)
    s = re.sub(r'\s+', ' ', s).replace('- ', '')
    return s.strip()
_cache = {}
def _pages(path):
    if path in _cache: return _cache[path]
    if path.endswith('.pdf'):
        import fitz
        d = fitz.open(path); pages = {i+1: p.get_text() for i,p in enumerate(d)}
    else:
        txt = open(path,encoding='utf8').read()
        parts = re.split(r'(?:<!-- PDF page (\d+) -->|===== PAGE (\d+) =====)', txt)
        pages = {}
        for i in range(1,len(parts),3):
            cur = int(parts[i] or parts[i+1]); pages[cur] = pages.get(cur,'')+' '+parts[i+2]
    _cache[path] = {k: norm(v) for k,v in pages.items()}
    return _cache[path]
def find(key):
    f,ph = L[key]; path,off,cite = F[f]
    pages = _pages(path); n = norm(ph)
    hits = [p for p,t in pages.items() if n in t]
    if hits: return hits[0],None
    ks = sorted(pages)
    for a,b in zip(ks,ks[1:]):
        if n in pages[a]+' '+pages[b]: return a,None
    return None,None
def page_label(key):
    p,_ = find(key); f = L[key][0]; off = F[f][1]
    if p is None: return None
    if isinstance(off,tuple): return f"p.{off[1]+p-1}"
    if off is None: return f"PDF p.{p}"
    return f"PDF p.{p} (printed p.{p-off})"
if __name__=='__main__':
    import sys
    only = sys.argv[1:]   # optional: python3 locators.py a1_  -> check only keys with that prefix
    bad = 0
    for k in L:
        if only and not any(k.startswith(o) for o in only): continue
        lab = page_label(k)
        if lab is None: bad += 1; print('MISSING', k, L[k][1][:70])
    print('checked', len(L), 'missing', bad)
