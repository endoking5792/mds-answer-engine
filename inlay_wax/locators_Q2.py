# Q2 (Flow properties of inlay wax) locators. Reference keys (BOOK strings for build_sources.py):
# Anusavice2013: "Anusavice KJ. Dental waxes, casting investments, and casting procedures. In: Anusavice KJ, Shen C, Rawls HR, editors. Phillips' Science of Dental Materials. 12th ed. St Louis: Elsevier Saunders; 2013 (year not verified from the file). Ch.10."
# Craig2002: "Craig RG, Powers JM, editors. Restorative Dental Materials. 11th ed. St Louis: Mosby; 2002. Ch.14 Waxes."
# Powers2013: "Powers JM, Wataha JC. Dental Materials: Properties and Manipulation. 10th ed. St Louis: Elsevier Mosby; 2013. Ch.10 Waxes."
# McCabe2008: "McCabe JF, Walls AWG. Applied Dental Materials. 9th ed. Oxford: Blackwell Publishing; 2008. Ch.4 Waxes."
# Bhat2019: "Bhat VS, Nandish BT, Jayaprakash K. Science of Dental Materials with Clinical Applications. 3rd ed. New Delhi: CBS Publishers; 2019. Ch.14 Dental waxes (auxiliary materials)."
import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
F = {
 'phi': (T+'Operative_and_Dental_Materials_Textbooks/Phillips_Science_of_Dental_Materials.md', 16, 'Anusavice, 2013'),
 'cra': (T+'Operative_and_Dental_Materials_Textbooks/Restorative_Dental_Materials_Craig_Michigan_11th.md', 9, 'Craig and Powers, 2002'),
 'pow': (T+'Operative_and_Dental_Materials_Textbooks/Powers_Wataha_Dental_Materials_Properties_and_Manipulation.md', 12, 'Powers and Wataha, 2013'),
 'mcc': (T+'Operative_and_Dental_Materials_Textbooks/Applied_Dental_Materials_McCabe_Walls_9th.md', 9, 'McCabe and Walls, 2008'),
 'bha': (T+'Operative_and_Dental_Materials_Textbooks/Science_of_Dental_Materials.md', 56, 'Bhat, Nandish and Jayaprakash, 2019'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
#   Pick clean text: avoid OCR ligature damage ("0e", "!le"), hyphen breaks and figure captions.
L = {
 'q2_p_def': ('phi', 'Relative ability of wax to plastically deform when it is heated slightly above body'),
 'q2_p_test': ('phi', 'subjecting cylindrical specimens to a desig'),
 'q2_p_37': ('phi', 'The maximum flow permitted for type I waxes at 37'),
 'q2_p_carve': ('phi', 'permits carving and removal of the pattern from the prepared cavity at oral temperature without distortion'),
 'q2_p_45': ('phi', 'must have a minimal flow of 70% and a maximum flow of 90%'),
 'q2_p_detail': ('phi', 'it will not flow into all of the areas in the preparation'),
 'q2_p_curve': ('phi', 'The wax begins to harden slowly below 65'),
 'q2_p_trans': ('phi', 'Each wax exhibits a sharp transition temperature at which it loses its plasticity'),
 'q2_p_soft': ('phi', 'Soft wax exhibits a transition point at a lower temperature than hard wax'),
 'q2_p_room': ('phi', 'may flow under applied pressure even at room temperature'),
 'q2_p_typeI': ('phi', 'low-melting type I inlay waxes used in the mouth for direct-waxing processes'),
 'q2_p_typeII': ('phi', 'soft type II inlay-type waxes for making patterns'),
 'q2_p_larger': ('phi', 'The higher flow of softer waxes produces larger cast metal'),
 'q2_c_slip': ('cra', 'The property of flow results from the slippage of molecules over each other'),
 'q2_c_factors': ('cra', 'Flow is decidedly dependent on the temperature of the wax, the force bringing about the deformation, and the time the force is applied'),
 'q2_c_melt': ('cra', 'Flow greatly increases as the melting point of the wax is approached'),
 'q2_c_nodist': ('cra', 'must have essentially no flow to minimize the possibility of distortion'),
 'q2_c_comp': ('cra', '60% paraffin, 25% carnauba, 10% ceresin'),
 'q2_c_carn': ('cra', 'The flow can be reduced by adding more carnauba wax or by selecting a higher'),
 'q2_c_resin': ('cra', 'Resins in small amounts, such as 1%, also affect the flow of inlay waxes'),
 'q2_c_carn10': ('cra', 'adding 10% of carnauba wax to paraffin wax'),
 'q2_c_spec': ('cra', 'Revised ANSI/ADA Specification No. 4'),
 'q2_c_type1': ('cra', 'Type 1 wax is a soft wax used as an indirect technique wax'),
 'q2_c_type2': ('cra', 'Type 2 wax is a harder wax prescribed for forming direct patterns'),
 'q2_c_load': ('cra', 'subjected to a 19.6 N load for 10 minutes'),
 'q2_c_insuff': ('cra', 'Insufficient flow of the wax caused by insufficient heating results in the lack of cavity detail'),
 'q2_c_excess': ('cra', 'makes compression of the wax difficult because of a lack of'),
 'q2_c_9pc': ('cra', 'Type 1 wax is about 9% at this temperature'),
 'q2_c_40lin': ('cra', 'The total amount of flow after 10 minutes at this temper'),
 'q2_w_def': ('pow', 'Flow is the change in shape under an applied force'),
 'q2_w_dist': ('pow', 'it results in a permanent distortion of the wax pattern'),
 'q2_m_spec': ('mcc', 'cylindrical specimens 10 mm diameter by 6 mm'),
 'q2_m_load': ('mcc', 'using a 2 kg'),
 'q2_m_confuse': ('mcc', 'in the past the opposite classi'),
 'q2_m_brittle': ('mcc', 'brittleness is preferred in order that the wax will fracture rather than distort'),
 'q2_b_45': ('bha', 'waxes must have flow between 70% and 90% at'),
 'q2_b_err': ('bha', 'It should have a flow of more than 70% at 45'),
 'q2_b_harden': ('bha', 'the wax begins to harden at approximately 50'),
}
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
