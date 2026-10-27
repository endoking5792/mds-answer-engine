# Q1 (Inlay casting wax) locators. Reference keys used in Q01 <!--REF--> line, for BOOK in build_sources.py:
# 'Anusavice2013': "Anusavice KJ, Shen C, Rawls HR, editors. Phillips' Science of Dental Materials. 12th ed. St Louis: Elsevier Saunders; 2013. Ch.10 Dental waxes, casting investments, and casting procedures.",
# 'Craig2002': "Craig RG, Powers JM, editors. Restorative Dental Materials. 11th ed. St Louis: Mosby; 2002. Ch.14 Waxes.",
# 'Bhat2019': "Bhat VS, Nandish BT, Jayaprakash K. Science of Dental Materials with Clinical Applications. 3rd ed. New Delhi: CBS Publishers; 2019. Ch.14 Dental waxes (auxiliary materials).",
# 'Powers2013': "Powers JM, Wataha JC. Dental Materials: Properties and Manipulation. 10th ed. St Louis: Elsevier Mosby; 2013. Ch.10 Waxes.",
# 'McCabe2008': "McCabe JF, Walls AWG. Applied Dental Materials. 9th ed. Oxford: Blackwell Publishing; 2008. Ch.4 Waxes.",
# 'Bonsor2013': "Bonsor SJ, Pearson GJ. A Clinical Guide to Applied Dental Materials. Edinburgh: Elsevier Churchill Livingstone; 2013. Ch.16 Waxes.",
# 'Sakaguchi2019': "Sakaguchi R, Ferracane J, Powers J, editors. Craig's Restorative Dental Materials. 14th ed. St Louis: Elsevier; 2019. Ch.4 (Table 4.13, thermal expansion).",
import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
F = {
 'ph': (T+'Operative_and_Dental_Materials_Textbooks/Phillips_Science_of_Dental_Materials.md', 16, 'Anusavice et al, 2013'),
 'cr': (T+'Operative_and_Dental_Materials_Textbooks/Restorative_Dental_Materials_Craig_Michigan_11th.md', 9, 'Craig and Powers, 2002'),
 'bh': (T+'Operative_and_Dental_Materials_Textbooks/Science_of_Dental_Materials.md', 56, 'Bhat et al, 2019'),
 'pw': (T+'Operative_and_Dental_Materials_Textbooks/Powers_Wataha_Dental_Materials_Properties_and_Manipulation.md', 12, 'Powers and Wataha, 2013'),
 'mc': (T+'Operative_and_Dental_Materials_Textbooks/Applied_Dental_Materials_McCabe_Walls_9th.md', 9, 'McCabe and Walls, 2008'),
 'bp': (T+'Operative_and_Dental_Materials_Textbooks/A_Clinical_Guide_to_Applied_Dental_Materials.md', None, 'Bonsor and Pearson, 2013'),
 'c14': (T+'Operative_and_Dental_Materials_Textbooks/Craigs_Restorative_Dental_Materials.md', None, 'Sakaguchi et al, 2019'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
#   Pick clean text: avoid OCR ligature damage ("0e", "!le"), hyphen breaks and figure captions.
L = {
 'q1_ph_def': ('ph', 'A specialized dental wax that can be applied to dies to form direct or indirect patterns for the lost-wax technique'),
 'q1_ph_elastic': ('ph', 'Tendency of a solid wax form to partially return to its original shape'),
 'q1_ph_flowdef': ('ph', 'Relative ability of wax to plastically deform when it is heated slightly above body temperature'),
 'q1_ph_hist': ('ph', 'Wax has been a valuable commodity for over 2000 years'),
 'q1_ph_carnhard': ('ph', 'Carnauba is one of the hardest and most durable waxes'),
 'q1_ph_class3': ('ph', 'pattern wax (inlay, casting, and baseplate types), processing wax (boxing, utility, and sticky types), and impression wax'),
 'q1_ph_clinlab': ('ph', 'those used primarily in the clinic and those used in commercial dental laboratories'),
 'q1_ph_typeI': ('ph', 'Type I is a medium wax employed in direct techniques and type II is a soft wax used in the indirect techniques'),
 'q1_ph_rarely': ('ph', 'is rarely used because of the wax'),
 'q1_ph_harden': ('ph', 'it must harden at a temperature above mouth temperature'),
 'q1_ph_colors': ('ph', 'Dental waxes are supplied in a variety of colors including blue, green, yellow, red, and ivory'),
 'q1_ph_climate': ('ph', 'A harder or medium type with a low flow property is indicated for use in warmer climates'),
 'q1_ph_paraffin': ('ph', 'Most dental waxes contain 40% to 60% paraffin by weight'),
 'q1_ph_flake': ('ph', 'Paraffin wax is likely to flake when it is trimmed'),
 'q1_ph_dammar': ('ph', 'It is added to the paraffin to improve the smoothness in molding'),
 'q1_ph_carnflow': ('ph', 'It is combined with the paraffin to decrease flow at mouth'),
 'q1_ph_candel': ('ph', 'its melting point is lower and it is not as hard as carnauba wax'),
 'q1_ph_ceresin': ('ph', 'may replace part of the paraffin to modify the'),
 'q1_ph_montan': ('ph', 'esters of acids derived from montan wax'),
 'q1_ph_filler': ('ph', 'Some formulations contain a compatible filler to control expansion and shrinkage'),
 'q1_ph_typeIpar': ('ph', 'Paraffin that is used for type I waxes has a higher melting point than the paraffin used for type II waxes'),
 'q1_ph_cool': ('ph', 'The wax begins to harden slowly below 65'),
 'q1_ph_37': ('ph', 'The maximum flow permitted for type I waxes at 37'),
 'q1_ph_45': ('ph', 'must have a minimal flow of 70% and a maximum flow of 90%'),
 'q1_ph_cylinder': ('ph', 'The flow is measured by subjecting cylindrical specimens'),
 'q1_ph_residue': ('ph', 'should not leave a solid residue that amounts to more than 0.10% of the original weight'),
 'q1_ph_cte': ('ph', 'The average linear thermal expansion coefficient over this temperature range is 350'),
 'q1_ph_07': ('ph', 'the wax may expand as much as 0.7% with an increase in temperature of 20'),
 'q1_ph_cond': ('ph', 'thermal conductivity of the waxes is low'),
 'q1_ph_glass': ('ph', 'is known as the glass transition temperature'),
 'q1_ph_most': ('ph', 'inlay wax expands and contracts thermally more per degree temperature change than any other dental material'),
 'q1_ph_dry': ('ph', 'dry heat is preferred to the use of a water bath'),
 'q1_ph_staple': ('ph', 'wire within the surface so that each prong'),
 'q1_ph_lub': ('ph', 'the die should be lubricated, preferably with a lubricant containing a wetting agent'),
 'q1_ph_invest': ('ph', 'invest the pattern immediately after removal from the mouth or die'),
 'q1_ph_serious': ('ph', 'Distortion of wax patterns is the most serious problem'),
 'q1_ph_occluded': ('ph', 'results from occluded air in the pattern, physical deformation'),
 'q1_ph_horseshoe': ('ph', 'bent into a horseshoe shape, and chilled in this position'),
 'q1_ph_storage': ('ph', 'Storage of a wax pattern for too long can lead to a'),
 'q1_ph_softlarger': ('ph', 'A soft wax pattern may result in a slightly larger and relatively rougher casting than a hard wax pattern'),
 'q1_ph_cte400': ('ph', 'The high thermal expansion coefficient of inlay wax is also important'),
 'q1_cr_comp': ('cr', 'an inlay wax may contain 60% paraffin, 25% carnauba, 10% ceresin, and 5% beeswax'),
 'q1_cr_hard': ('cr', 'Some inlay waxes are described as hard, regular (medium), or soft'),
 'q1_cr_flowred': ('cr', 'The flow can be reduced by adding more carnauba wax'),
 'q1_cr_resin1': ('cr', 'Resins in small amounts, such as 1%, also affect the flow of inlay waxes'),
 'q1_cr_spec': ('cr', 'Specification No. 4 (IS0 1561) for dental inlay casting wax'),
 'q1_cr_residue': ('cr', 'nonvolatile residue of these waxes to a maximum of 0.10% at an ignition temperature of 700'),
 'q1_cr_type1': ('cr', 'Type 1 wax is a soft wax used as an indirect technique wax'),
 'q1_cr_type2': ('cr', 'Type 2 wax is a harder wax prescribed for forming direct patterns in the mouth'),
 'q1_cr_load': ('cr', 'subjected to a 19.6 N load for 10 minutes'),
 'q1_cr_9pct': ('cr', 'The flow of the Type 1 wax is about 9% at this temperature'),
 'q1_cr_04': ('cr', 'causes a 0.4% linear contraction of the wax'),
 'q1_cr_largest': ('cr', 'have the largest coefficient of thermal expansion of any material used in restorative dentistry'),
 'q1_cr_mineral': ('cr', 'Mineral waxes generally have higher coefficients of linear thermal expansion than plant waxes'),
 'q1_cr_brittle': ('cr', 'Hence the inlay wax would be considered a brittle material'),
 'q1_cr_compr': ('cr', 'compressive strength of inlay wax decreased from 83 to 0.5 MPa'),
 'q1_cr_resid': ('cr', 'Regardless of the method used to prepare a wax pattern, residual stress exists in the completed pattern'),
 'q1_cr_higher': ('cr', 'the higher the temperature of the wax at the time the pattern was adapted and shaped, the less the tendency for distortion'),
 'q1_cr_refrig': ('cr', 'they should be kept in a refrigerator'),
 'q1_cr_30': ('cr', 'stand uninvested for a time longer than 30 minutes'),
 'q1_cr_sprue': ('cr', 'use of a solid wax sprue or a hollow metal sprue filled with sticky wax'),
 'q1_cr_readapt': ('cr', 'If the pattern was stored, the margins should be readapted'),
 'q1_cr_twoqual': ('cr', 'thermal change in dimension and tendency to warp or distort on standing'),
 'q1_cr_thermexp': ('cr', 'Thermal expansion data for the Type 2 wax are no longer required by the specification'),
 'q1_cr_instr': ('cr', 'include instructions regarding the method of softening and the working temperature'),
 'q1_cr_resinmod': ('cr', 'Modeling resins are characterized by lower heat of polymerization and shrinkage than acrylics'),
 'q1_cr_oldest': ('cr', 'One of the oldest recorded uses of wax in dentistry is for taking impressions'),
 'q1_cr_7to1': ('cr', 'the modulus ratio for the inlay and soft green casting wax is 7:1'),
 'q1_cr_fedspec': ('cr', 'There is no ANSI/ADA specification for these casting waxes'),
 'q1_cr_sticks': ('cr', 'deep blue, green, or purple rods or sticks about 7.5 cm long'),
 'q1_cr_warmdie': ('cr', 'by using warmed carving instruments and a warmed die, and by adding wax to the die in small amounts'),
 'q1_bh_class': ('bh', 'According to the origin (now not in use)'),
 'q1_bh_def': ('bh', 'Waxes are thermoplastic organic polymers containing hydrocarbons of low molecular weight'),
 'q1_bh_table': ('bh', 'The composition of inlay wax (ADA specification No. 4)'),
 'q1_bh_par60': ('bh', 'Paraffin wax 60%'),
 'q1_bh_carn20': ('bh', 'Carnauba wax 20%'),
 'q1_bh_bees': ('bh', 'Reduces the flow at mouth temperature and reduces the brittleness'),
 'q1_bh_synth': ('bh', 'Gives stable flow properties to the wax'),
 'q1_bh_typeI': ('bh', 'Type I: Medium wax is used for direct wax pattern technique'),
 'q1_bh_more1': ('bh', 'It should have a flow of more than 70% at 45°C and more than 1% at 37°C'),
 'q1_bh_cote': ('bh', 'Inlay waxes have a high COTE 300–700 ppm'),
 'q1_bh_contr': ('bh', 'The waxes may have a linear contraction of about 0.3'),
 'q1_bh_harden50': ('bh', 'the wax begins to harden at approximately 50°C and it solidifies approximately at 40°C'),
 'q1_bh_cold': ('bh', 'Cold carving instrument should be used for the direct wax pattern'),
 'q1_bh_biting': ('bh', 'by the patient biting on the wax'),
 'q1_bh_minim': ('bh', 'Select the proper type of waxes'),
 'q1_bh_memory': ('bh', 'it recovers its original shape and this is known as wax memory'),
 'q1_bh_500': ('bh', 'the wax should completely vapourize at 500°C and should have no residue'),
 'q1_pw_warm': ('pw', 'Wax patterns are carved with warm (37 °C) instruments'),
 'q1_pw_30': ('pw', 'should be minimized (less than 30 minutes)'),
 'q1_pw_five': ('pw', 'it may contain five or six different waxes'),
 'q1_pw_resin': ('pw', 'Resins offer higher strength and lower flow than pattern waxes'),
 'q1_pw_burn': ('pw', 'all pattern waxes and resins must burn out with no residue'),
 'q1_pw_iso': ('pw', 'Three common hardnesses of baseplate wax are available (ISO 15854'),
 'q1_mc_conf': ('mc', 'This has caused some confusion because in the past the opposite'),
 'q1_mc_type1ind': ('mc', 'The type 1 materials are designed for use in the indirect technique'),
 'q1_mc_contr': ('mc', 'is of the order of 0.1–0.5%'),
 'q1_mc_fracture': ('mc', 'brittleness is preferred in order that the wax will fracture rather than distort'),
 'q1_mc_annealer': ('mc', 'The annealer is most useful for inlay waxes'),
 'q1_mc_cyl': ('mc', 'cylindrical specimens 10 mm diameter by 6 mm'),
 'q1_mc_shiny': ('mc', 'until it becomes shiny'),
 'q1_mc_dieimp': ('mc', 'thus undergoing a thermal contraction which may approach the value of a direct wax pattern material'),
 'q1_mc_reserved': ('mc', 'The use of direct wax patterns is normally reserved only for the most simple designs of cast posts/cores on anterior teeth'),
 'q1_bp_60': ('bp', 'Paraffin wax is usually the major component, forming about 60% of the total composition'),
 'q1_bp_ivory': ('bp', 'they are also available in ivory'),
 'q1_bp_4550': ('bp', 'the wax should be heated to between 45 and 50 °C prior to use for a minimum of 20 minutes'),
 'q1_bp_three': ('bp', 'Use of waxes in dentistry can be divided into three distinct areas'),
 'q1_cr_duct': ('cr', 'waxes with lower melting temperatures have a greater ductility at any given temperature'),
 'q1_c14_cte': ('c14', 'Inlay waxes 350–450'),
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
