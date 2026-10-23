import re, os
T = os.path.expanduser('~/mds-textbooks/')
# F: key -> (path, offset, citation). offset int: printed = PDF marker - offset; None: PDF page only.
F = {
 'coh': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/22_22_Chronic_cracks_and_fractures.md', None, 'Berman and Tamse, 2021'),
 'ing': (T+'Ingles_Endodontics_7th_Chapterwise/13_Chapter_13_Crown_Originating_Dental_Fractures.md', -42, 'Bakland, 2019'),
 'gb': (T+'The_Guidebook_to_Molar_Endodontics_Chapterwise/09_9_Assessing_and_Managing_Cracked_Molars.md', 19, 'Krishnan and Swain, 2025'),
 'wal': (T+'Principles_and_practice_of_endodontic_2002_compressed_Chapterwise/28_Part_28_Longitudinal_Tooth_Fractures.md', 21, 'Walton and Torabinejad, 2002'),
 'mod': (T+'Operative_and_Dental_Materials_Textbooks/Modern_Operative_Dentistry.md', 6, 'Bresciani et al, 2020'),
 'in14': (T+'Ingles_Endodontics_7th_Chapterwise/14_Chapter_14_Vertical_Root_Fractures.md', -45, 'Tamse and Berman, 2019'),
 'a12': (T+'Textbook_and_Color_Atlas_of_Traumatic_Chapterwise/12_12_Root_Fractures.md', 16, 'Andreasen, Andreasen and Cvek, 2007'),
 'a11': (T+'Textbook_and_Color_Atlas_of_Traumatic_Chapterwise/11_11_Crown_Root_Fractures.md', 16, 'Andreasen, Andreasen and Tsukiboshi, 2007'),
 'iadt': (os.path.expanduser('~/.claude/answer_tools/cracked_tooth/sources/iadt_bourguignon_2020.txt'), -313, 'Bourguignon et al, 2020'),
 'sik': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/26_26_Traumatic_Injuries_and_Management.md', None, 'Sikri, n.d.'),
 'gro6': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/06_Chapter_6_Clinical_Diagnostic_Methods.md', None, 'Gopikrishna, 2021'),
 'stu': (T+'Operative_and_Dental_Materials_Textbooks/Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, "Sturdevant's, n.d."),
 'aa0': (T+'Glossary_of_Endodontic_Terms_Chapterwise/00_Pages_1_30.md', None, 'American Association of Endodontists, 2012'),
}
L = {}
def add(f, d):
    for k,v in d.items(): L[k]=(f,v)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'phrases.py')).read())
def norm(s):
    s = s.replace('\u00ad ', '').replace('\u00ad', '').replace('\u2010', '-')
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
