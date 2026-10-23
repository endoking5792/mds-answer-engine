import re, os
T = os.path.expanduser('~/mds-textbooks/')
G = T+'Dentine_HyperSensitivity_Chapterwise/'
S = os.path.expanduser('~/.claude/answer_tools/dentin_hypersensitivity/sources/')
LAS = T+'Operative_and_Dental_Materials_Textbooks/Lasers_in_Dentistry_Current_Concepts.md'
# F: key -> (path, offset, citation). offset int: printed = PDF marker - offset; None: PDF page only.
F = {
 'g1': (G+'01_1_Introduction_and_Overview_Statement_of_the_Problem.md', 19, 'Addy and Gillam, 2024'),
 'g2': (G+'02_2_The_Prevalence_of_Dentine_Hypersensitivity.md', 19, 'Taha and Gillam, 2024'),
 'g4': (G+'04_4_Aetiology_and_Clinical_Features_of_Dentine_Hypersensitivit.md', 19, 'Olley and Bartlett, 2024'),
 'g5': (G+'05_5_The_Physiological_Basis_of_Dentin_Hypersensitivity.md', 19, 'Markowitz and Pashley, 2024'),
 'g6': (G+'06_6_Treatments_for_Tooth_Sensitivity.md', 19, 'Markowitz and Gillam, 2024'),
 'g7': (G+'07_7_Treatment_Modalities.md', 19, 'Mosquim et al, 2024'),
 'g8': (G+'08_8_Advances_in_the_Management_of_the_Patient_with_Dentine_Hyp.md', 19, 'Gillam and Ramseier, 2024'),
 'g9': (G+'09_9_Future_Strategies_for_the_Development_of_Desensitizing_Pro.md', 19, 'Hill and Gillam, 2024'),
 'sik': (S+'sikri_cons.txt', 19, 'Sikri, 2020'),
 'tru': (S+'dcna_trushkowsky.txt', -598, 'Trushkowsky and Oquendo, 2011'),
 'asi': (S+'dcna_alsabbagh_inoffice.txt', -46, 'Al-Sabbagh, Brown and Thomas, 2009'),
 'asp': (S+'dcna_alsabbagh_patient.txt', -60, 'Al-Sabbagh, Harrison and Thomas, 2009'),
 'l7': (LAS, None, 'Cronshaw and Mylona, 2023'),
 'l11': (LAS, None, 'Arapostathis, Velonis and Chala, 2023'),
}
L = {}
def add(f, d):
    for k,v in d.items():
        assert k not in L, k
        L[k]=(f,v)
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
