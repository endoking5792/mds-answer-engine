import re, os, glob, importlib.util
# Verbatim-phrase locators for the Root Resorption topic. Every [SRC] fact in an answer has one entry in L.
# Shared source table F lives here; each question's locator phrases live in locators_<QID>.py
# (dicts L, and optionally F_EXTRA, BOOK_EXTRA, LIT), so parallel drafters never edit the same file.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (checked at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (no printed page number visible)
F = {
 'coh': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/18_18_Root_resorption.md', None, 'Patel et al, 2021'),
 'ing': (T+'Ingles_Endodontics_7th_Chapterwise/15_Chapter_15_Pathologic_Tooth_Resorption.md', -48, 'Andreasen, Heithersay and Bakland, 2019'),
 'gul': (T+'Endodontics_Kishor_Gulabivala_Yuan_Ling_Ng_4th_Ed_Mosby_2014_Chapterwise/11_11_Management_of_tooth_resorption.md', 9, 'Ng and Gulabivala, 2014'),
 'edl': (T+'Endodontology_Chapterwise/42_42_Tooth_Resorption.md', 17, 'Baumann and Beer, 2010'),
 'sel': (T+'Seltzer_and_Bender_Dental_Pulp_Chapterwise_MD/Chapter_17_Root_Resorption.md', None, 'Levin, 2012'),
 'sik': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/27_27_Root_Resorption.md', 21, 'Sikri, 2019'),
 'gl1': (T+'Glossary_of_Endodontic_Terms_Chapterwise/00_Pages_1_30.md', None, 'American Association of Endodontists, 2012'),
 'gl2': (T+'Glossary_of_Endodontic_Terms_Chapterwise/01_Pages_31_52.md', None, 'American Association of Endodontists, 2012'),
}
L = {}
BOOK_EXTRA = {}
LIT = {}
_here = os.path.dirname(os.path.abspath(__file__))
for _p in sorted(glob.glob(os.path.join(_here, 'locators_*.py'))):
    try:
        _s = importlib.util.spec_from_file_location(os.path.basename(_p)[:-3], _p); _m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
    except Exception as _e:
        print('WARNING: skipped', os.path.basename(_p), 'because it failed to load:', _e); continue
    for _name, _target in (('F_EXTRA', F), ('L', L), ('BOOK_EXTRA', BOOK_EXTRA), ('LIT', LIT)):
        _d = getattr(_m, _name, {})
        _clash = [k for k in _d if k in _target and _target[k] != _d[k]]
        assert not _clash, f'{os.path.basename(_p)}: {_name} keys clash with another file: {_clash}'
        _target.update(_d)
def norm(s):
    s = s.replace('­ ', '').replace('­', '').replace('‐', '-')
    s = re.sub(r'\s+', ' ', s).replace('- ', '')
    return s.strip()
_cache = {}
def _pages(path):
    if path in _cache: return _cache[path]
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
    if off is None: return f"PDF p.{p}"
    return f"PDF p.{p} (printed p.{p-off})"
if __name__=='__main__':
    import sys
    keys = [k for k in L if not sys.argv[1:] or any(k.startswith(a) for a in sys.argv[1:])]
    bad = 0
    for k in keys:
        if L[k][0] not in F: bad += 1; print('NO SOURCE', k, L[k][0]); continue
        if page_label(k) is None: bad += 1; print('MISSING', k, L[k][1][:70])
    print('checked', len(keys), 'missing', bad)
