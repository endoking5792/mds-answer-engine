import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
O = 'Operative_and_Dental_Materials_Textbooks/'
F = {
 'stu': (T+O+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter et al, 2019'),
 'sum': (T+O+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Fruits, Khajotia and Nicholson, 2013'),
 'sik': (T+O+'Textbook_of_Conservative_and_Restorative_Dentistry.md', 19, 'Sikri, 2020'),
 'mzA': (T+O+'Operative_Dentistry_Marzouk.md', 4, 'Marzouk et al, 1985'),
 'mzB': (T+O+'Operative_Dentistry_Marzouk.md', 3, 'Marzouk et al, 1985'),
 'ing': (T+'Ingles_Endodontics_7th_Chapterwise/02_Chapter_2_Structure_and_Function_of_the_Pulp_Dentin_Complex.md', -12, 'Haug, Kim and Heyeraas, 2019'),
 'sel2': (T+'Seltzer_and_Bender_Dental_Pulp_Chapterwise_MD/Chapter_02_Formation_and_Repair_of_Dentin_in_the_Adult.md', None, 'Smith, 2012'),
 'stu10': (T+O+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter et al, 2019'),
 'sum2': (T+O+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Rose, Haveman and Davis, 2013'),
 'stu6': (T+O+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter et al, 2019'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
#   Pick clean text: avoid OCR ligature damage ("0e", "!le"), hyphen breaks and figure captions.
L = {}
from loc_q01 import L1; L.update(L1)
from loc_q05 import L5; L.update(L5)
from loc_q06 import L6; L.update(L6)
from loc_q09 import L9; L.update(L9)
def norm(s):
    s = s.replace('\u00b5','\u03bc').replace('\u2013','-').replace('\u00ad ', '').replace('\u00ad', '').replace('\u2010', '-')
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
    bad = 0
    for k in L:
        lab = page_label(k)
        if lab is None: bad += 1; print('MISSING', k, L[k][1][:70])
    print('checked', len(L), 'missing', bad)
