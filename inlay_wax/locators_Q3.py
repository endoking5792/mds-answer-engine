# Q3 locators (Discuss technique for indirect wax pattern). Separate file so parallel agents do not collide with locators.py.
# Reference keys used by Q3 (full strings in the form build_sources.py BOOK expects; merge into BOOK before running build_sources.py):
# 'Marzouk_nd': "Marzouk MA, Simonton AL, Gross RD. Operative Dentistry: Modern Theory and Practice. St Louis: Ishiyaku EuroAmerica; New Delhi: Indian edition (publication year not printed in the extracted front matter). Ch.22 Working die and model construction; Ch.24 Casting fabrication.",
# 'Ritter2019': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed (adaptation of 7th ed). Elsevier; 2019. Ch.23 Class II cast metal restorations.",
# 'Chadwick2011': "Chadwick G, Radford J, Ricketts D. Gold restorations: the metals, the manufacture and the fit. In: Ricketts D, Bartlett D, editors. Advanced Operative Dentistry: A Practical Approach. Edinburgh: Churchill Livingstone Elsevier; 2011. Ch.9.",
# 'Sikri_ind': "Sikri VK. Indirect Restorations in Dental Practice. 2nd ed. New Delhi: CBS Publishers (year not verified from the extracted file). Glossary; cast restoration chapter.",
# 'Garg2011': "Garg N, Garg A. Textbook of Preclinical Conservative Dentistry. 1st ed. New Delhi: Jaypee Brothers Medical Publishers; 2011. Ch.12 Cast metal restorations.",
# 'Chandhak2020': "Chandhak MG. Casting procedure and casting defects. In: Singh H, editor. Essentials of Preclinical Conservative Dentistry. 2nd ed. Gurgaon: Wolters Kluwer Health (India); 2020. Ch.20.",
# 'Anusavice2013': "Anusavice KJ, Shen C, Rawls HR, editors. Phillips' Science of Dental Materials. 12th ed. St Louis: Elsevier; 2013. Ch.10 Dental waxes, casting investments, and casting procedures.",
# 'Craig2002': "Craig RG, Powers JM, editors. Restorative Dental Materials. 11th ed. St Louis: Mosby; 2002. Ch.17 Casting and soldering procedures.",
# 'Powers2013': "Powers JM, Wataha JC. Dental Materials: Properties and Manipulation. 10th ed. St Louis: Elsevier Mosby; 2013. Ch.9 Gypsum and investment materials; Ch.10 Waxes.",
# 'Bhat2019': "Bhat VS, Nandish BT. Science of Dental Materials with Clinical Applications. 3rd ed. New Delhi: CBS Publishers; 2019. Ch.14 Dental waxes.",
# [LIT] (abstracts only):
# 'Lalande2018': "Lalande D, Hodd JA, Brousseau JS, Ramos V, Dunham D, Rueggeberg F. Marginal discrepancy dimensions of single unit metal crowns fabricated by using CAD-CAM-milled acrylate resin polymer blocks or a conventional waxing technique. J Prosthet Dent. 2018;119(6):948-953. doi:10.1016/j.prosdent.2017.07.019 (abstract only).",
# 'Kim2018': "Kim SB, Kim NH, Kim JH, Moon HS. Evaluation of the fit of metal copings fabricated using stereolithography. J Prosthet Dent. 2018;120(5):693-698. doi:10.1016/j.prosdent.2018.01.012 (abstract only).",
# 'Pekkan2025': "Pekkan G, Gulgezen Aydin H, Tuna SH, Hekimoglu C. Overall fit of anterior and posterior single crown substructures fabricated with different additive manufacturing and conventional techniques. Odontology. 2025;114(3):1196-1206. doi:10.1007/s10266-025-01178-2 (abstract only).",
import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
F = {
 'mz22': (T+'Operative_and_Dental_Materials_Textbooks/Operative_Dentistry_Marzouk.md', -2, 'Marzouk et al, n.d.'),
 'mz24': (T+'Operative_and_Dental_Materials_Textbooks/Operative_Dentistry_Marzouk.md', -3, 'Marzouk et al, n.d.'),
 'stu': (T+'Operative_and_Dental_Materials_Textbooks/Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter et al, 2019'),
 'ao': (T+'Operative_and_Dental_Materials_Textbooks/Advanced_Operative_Dentistry.md', 3, 'Chadwick, Radford and Ricketts, 2011'),
 'sk': (T+'Operative_and_Dental_Materials_Textbooks/Indirect_Restorations_Sikri.md', None, 'Sikri, n.d.'),
 'gg': (T+'Operative_and_Dental_Materials_Textbooks/Textbook_of_Preclinical_Conservative_Dentistry.md', 7, 'Garg and Garg, 2011'),
 'hs': (T+'Operative_and_Dental_Materials_Textbooks/Essentials_of_Preclinical_Conservative_Dentistry_Harpreet_Singh.md', 17, 'Chandhak, 2020'),
 'ph': (T+'Operative_and_Dental_Materials_Textbooks/Phillips_Science_of_Dental_Materials.md', 16, 'Anusavice et al, 2013'),
 'cr': (T+'Operative_and_Dental_Materials_Textbooks/Restorative_Dental_Materials_Craig_Michigan_11th.md', 9, 'Craig and Powers, 2002'),
 'pw': (T+'Operative_and_Dental_Materials_Textbooks/Powers_Wataha_Dental_Materials_Properties_and_Manipulation.md', 12, 'Powers and Wataha, 2013'),
 'bn': (T+'Operative_and_Dental_Materials_Textbooks/Science_of_Dental_Materials.md', 56, 'Bhat and Nandish, 2019'),
 'bn0': (T+'Operative_and_Dental_Materials_Textbooks/Science_of_Dental_Materials.md', None, 'Bhat and Nandish, 2019'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
#   Pick clean text: avoid OCR ligature damage ("0e", "!le"), hyphen breaks and figure captions.
L = {
 'q3_mz_spacerobj': ('mz22', 'The main objective of a die spacer is to create room for'),
 'q3_mz_hydraulic': ('mz22', 'hydraulic pressure during seating is minimized.'),
 'q3_mz_25pc': ('mz22', 'crease the casting retention (25% estimated increase)'),
 'q3_mz_25um': ('mz22', 'It should have a film thickness of at least 25 microns'),
 'q3_mz_layers': ('mz22', 'may necessitate several applications (4-5). Always wait until'),
 'q3_mz_colour': ('mz22', 'good idea to use a different color for each layer'),
 'q3_mz_short': ('mz22', 'surfaces short of the circumferential tie constitutents'),
 'q3_mz_paint': ('mz22', 'airplane paints are very adequate'),
 'q3_mz_oil': ('mz22', 'in the form of a thin film-forming oil (mineral or vegetable)'),
 'q3_mz_trim': ('mz22', 'but the simplest is to create (leave) a flat or convex surface'),
 'q3_mz_groove': ('mz22', 'tooth surface, to be followed by a groove or a troughing in the'),
 'q3_mz_cone': ('mz22', 'taper the die to a cone shape with a flat base'),
 'q3_mz_twopour': ('mz22', 'manipulative procedure that can induce stresses in the wax.'),
 'q3_mz_onepour': ('mz22', 'There is less distortion to the wax pattern since it'),
 'q3_mz_dowel': ('mz22', 'A dowel pin may be incorporated in the die material mix'),
 'q3_mz_empirical': ('mz24', 'This is still the most empirical of all the steps'),
 'q3_mz_cte': ('mz24', 'dental materials (up to 400 PPM/1°C.)'),
 'q3_mz_typesABC': ('mz24', 'are classified into three types—type A'),
 'q3_mz_annealed': ('mz24', 'Start with stress-free or annealed wax'),
 'q3_mz_oven': ('mz24', 'kept in a 55° C. oven'),
 'q3_mz_warm': ('mz24', 'always use warm to hot instruments, so that stresses, if induced,'),
 'q3_mz_sharp': ('mz24', 'use sharp instruments, if carving is required'),
 'q3_mz_explorer': ('mz24', '(blunt explorer) deeply into each increment of wax added to'),
 'q3_mz_hedge': ('mz24', 'only reliable hedge against these disrupting dimensional'),
 'q3_mz_fridge': ('mz24', 'reliable measure is to refrigerate the pattern'),
 'q3_mz_5min': ('mz24', 'vestment is not possible within 5 minutes of the completion of'),
 'q3_mz_bubbles': ('mz24', 'During the build-up of a wax pattern, especially if done in'),
 'q3_mz_sepfilm': ('mz24', 'thickness of the separating medium to the smallest dimension'),
 'q3_mz_four': ('mz24', 'There are four basic methods for producing wax replicas of'),
 'q3_mz_cones': ('mz24', 'wax cones, triangles, drops, etc.'),
 'q3_mz_overfill': ('mz24', 'After lubricating the die, all details are overfilled with'),
 'q3_mz_silk': ('mz24', 'The pattern is polished using silk cloth and brushes.'),
 'q3_mz_cusps': ('mz24', 'Cusps with their tips are built in their exact location'),
 'q3_mz_triridge': ('mz24', 'Triangular ridges of cusps are added and the same testing'),
 'q3_mz_margridge': ('mz24', 'Marginal ridges are built up and tried in the same way'),
 'q3_mz_fossae': ('mz24', 'Fossae and grooves occlusally, facially, and lingually are'),
 'q3_mz_marginated': ('mz24', 'The wax pattern is marginated and the surface is polished.'),
 'q3_mz_core': ('mz24', 'The wax pattern can be fabricated in minimal time using'),
 'q3_mz_spruedie': ('mz24', 'be done while the wax pattern is on the die or the tooth in'),
 'q3_mz_diam': ('mz24', 'diameter should be greater than the thickest part of the wax'),
 'q3_mz_gauge': ('mz24', '8-18 gauge, 8 being almost 3 mm in diameter and 18 being'),
 'q3_mz_proximal': ('mz24', 'The proximal surfaces are the ideal'),
 'q3_mz_45': ('mz24', 'It should be directed away from, or at 45°, to'),
 'q3_mz_bulk': ('mz24', 'The sprue formers should be attached to the bulkiest part of'),
 'q3_mz_res': ('mz24', 'Occasionally, wax is added around the sprue former 1-2 mm'),
 'q3_mz_join': ('mz24', 'To minimize stress release while joining a sprue former to'),
 'q3_mz_tube': ('mz24', 'It is advisable to fill the tube sprue former'),
 'q3_mz_twofinger': ('mz24', 'The second choice is to use two'),
 'q3_mz_staple': ('mz24', 'The third choice is to formulate a suitable size staple from'),
 'q3_mz_hydrophobic': ('mz24', 'Casting waxes are hydrophobic materials that are very'),
 'q3_st_flowpress': ('stu', 'wax spatula by the ‘flow and press’'),
 'q3_st_contact': ('stu', 'The ability to form proper proximal contour and contact'),
 'q3_st_occl': ('stu', 'Complete the occlusal wax-up with a warmed No. 7 wax'),
 'q3_st_margin': ('stu', 'permits carving of the marginal wax with light pressure so'),
 'q3_st_dies': ('stu', 'Dies are replicas of the prepared teeth and the'),
 'q3_st_pindex': ('stu', 'Dowel pins are automatically positioned parallel'),
 'q3_st_15mm': ('stu', 'Dies should be approximately 15 mm high occlusogingivally.'),
 'q3_ao_expand': ('ao', 'Die stones expand by 0.05–0.10% on setting'),
 'q3_ao_coats': ('ao', 'Two to three coats of'),
 'q3_ao_short': ('ao', 'just short of the preparation margin. The die spacer is'),
 'q3_ao_additive': ('ao', 'built up using the wax additive'),
 'q3_ao_mill': ('ao', 'mill wax blocks to form'),
 'q3_ao_bubbles': ('ao', 'to coat the wax pattern and to ensure no air bubbles attach'),
 'q3_sk_spacer': ('sk', 'An agent applied to a die to provide space for the luting agent in'),
 'q3_sk_additive': ('sk', 'The process used to develop a wax pattern through'),
 'q3_sk_pattern': ('sk', 'The wax forms that is positive likeness of an object to be'),
 'q3_gg_indirect': ('gg', 'In this wax pattern is prepared outside the oral cavity.'),
 'q3_gg_better': ('gg', 'Direct wax pattern produces better fitting than indirect'),
 'q3_gg_onlyinlay': ('gg', 'This method is possible only in inlays and onlays'),
 'q3_gg_ind': ('gg', 'Large preparations like onlays, full coverage crowns'),
 'q3_gg_skirts': ('gg', 'When minute details like skirts and collars are present.'),
 'q3_gg_type2': ('gg', 'Use type II inlay wax for indirect wax pattern.'),
 'q3_gg_lub': ('gg', 'The lubricator should produce a very thin separator film.'),
 'q3_gg_adapt': ('gg', 'Adapt the inlay wax to the die by flowing or by the'),
 'q3_gg_adv': ('gg', 'Finishing and polishing can be done on die.'),
 'q3_gg_diam': ('gg', 'It should be either equal or greater than the thickest part of wax pattern.'),
 'q3_gg_18': ('gg', 'end of wax pattern is 1/8th to 1/4th of'),
 'q3_gg_45': ('gg', 'angle of 45° to bulkiest portion of the wax pattern.'),
 'q3_gg_flare': ('gg', 'be flared for high density gold alloys but constricted for'),
 'q3_gg_wash': ('gg', 'wash the wax pattern with soap and'),
 'q3_gg_stone': ('gg', 'type IV dental stone (high strength) and type V dental stone'),
 'q3_gg_electro': ('gg', 'Electrodeposition of copper or silver on the impression gives'),
 'q3_gg_epoxy': ('gg', 'The abrasive resistance, strength, and reproduction of details are much better than that of gypsum'),
 'q3_gg_divest': ('gg', 'This is highly accurate technique for'),
 'q3_gg_immed': ('gg', 'Wax pattern should be immediately invested after'),
 'q3_gg_cte': ('gg', 'The coefficient of thermal expansion of inlay wax is high.'),
 'q3_hs_indirect': ('hs', 'wax pattern’ is fabricated on the cast'),
 'q3_hs_type': ('hs', 'Type I inlay wax is used in direct technique and Type II in'),
 'q3_hs_diam': ('hs', 'with the broadest part of the wax pattern'),
 'q3_hs_res': ('hs', 'reservoir part of the sprue is situated 1 mm'),
 'q3_hs_45': ('hs', 'The sprue should be angulated correctly at 45° to'),
 'q3_hs_68': ('hs', 'There should be a distance of 6–8 mm between'),
 'q3_hs_025': ('hs', 'the wax pattern is about 0.25 inch from the other'),
 'q3_hs_2030': ('hs', 'more than 20–30 minutes before being invested.'),
 'q3_hs_asap': ('hs', 'A pattern should be invested as soon as possible after it is removed from the die'),
 'q3_ph_inddef': ('ph', 'Indirect wax technique—Procedure in which a wax pattern is prepared on a die.'),
 'q3_ph_elastic': ('ph', 'Tendency of a solid wax form to partially return to its original shape'),
 'q3_ph_type1': ('ph', 'Type I is a medium wax employed in direct techniques'),
 'q3_ph_type2': ('ph', 'and type II is a soft wax used in the indirect techniques.'),
 'q3_ph_rarely': ('ph', 'is rarely used because of the wax’s sensitivity to changes in'),
 'q3_ph_shrink': ('ph', 'technique) will shrink appreciably as it is cooled to room'),
 'q3_ph_dipping': ('ph', 'Dipping waxes are used'),
 'q3_ph_mass': ('ph', 'is kept molten to provide a station for mass production of'),
 'q3_ph_lub': ('ph', 'preferably with a lubricant containing a wetting agent'),
 'q3_ph_overfill': ('ph', 'The prepared cavity should be overfilled, and the wax then carved to the proper contour.'),
 'q3_ph_silk': ('ph', 'A silk or other fine cloth may be used for a final polishing of the pattern, rubbing toward the margins.'),
 'q3_ph_finger': ('ph', 'some clinicians prefer to apply finger pressure as the wax is cooling'),
 'q3_ph_staple': ('ph', 'staple-like wire within the surface'),
 'q3_ph_dryheat': ('ph', 'dry heat is preferred to the use of a water bath'),
 'q3_ph_350': ('ph', 'The average linear thermal expansion coefficient over this temperature range is 350'),
 'q3_ph_less': ('ph', 'when the wax is used in the indirect technique because the'),
 'q3_ph_several': ('ph', 'It is important that the wax pattern be retained on the die for several hours to avoid distortion'),
 'q3_ph_immed': ('ph', 'will fit most accurately when the pattern is invested'),
 'q3_ph_causes': ('ph', 'Distortion of a wax pattern results from occluded air in the pattern'),
 'q3_ph_spacer': ('ph', 'applied in several coats to within 0.5 mm of the preparation finish line'),
 'q3_ph_resins': ('ph', 'The most common die spacers are resins.'),
 'q3_ph_spruesame': ('ph', 'Select a sprue former with a diameter that is approximately the same size as the thickest area of the wax pattern.'),
 'q3_ph_suck': ('ph', 'localized shrinkage porosity (“suck-back” porosity)'),
 'q3_ph_6mm': ('ph', 'properly in the casting ring within 6 mm'),
 'q3_ph_flare': ('ph', 'The sprue former connection to the wax pattern is generally flared for high-density gold alloys'),
 'q3_ph_45': ('ph', 'Sound casting results with sprue at approximately 45° to the proximal wall.'),
 'q3_ph_twostage': ('ph', 'two-stage burnout technique whenever plastic sprue formers or patterns are involved'),
 'q3_ph_ondie': ('ph', 'The sprue former should be attached to the wax pattern with the pattern on the master die'),
 'q3_ph_occl': ('ph', 'Some clinicians prefer placement at the occlusal surface'),
 'q3_ph_bulk': ('ph', 'the ideal area for the sprue former is the point of greatest bulk in the pattern'),
 'q3_cr_direct': ('cr', 'This method can only be used for small inlay restorations.'),
 'q3_cr_indirect': ('cr', 'The indirect method is used for all types of restorations.'),
 'q3_cr_flowless': ('cr', 'makes the property of wax flow less critical'),
 'q3_cr_spacer': ('cr', 'The thickness of the spacer, which can be difficult to control, ranges from 10 to 30'),
 'q3_cr_nomargin': ('cr', 'nor should they be used on the margins of the restoration.'),
 'q3_cr_excess': ('cr', 'An excess of separator is to be avoided because it leads to inaccuracies in the wax pattern'),
 'q3_cr_metaldie': ('cr', 'if the metal die is warmed throughout to near body temperature'),
 'q3_cr_lamp': ('cr', 'The die can be warmed by placing it under an electric lamp'),
 'q3_cr_cool': ('cr', 'A cool carving instrument burnishing over or cutting through the wax introduces tensile and compressive stresses'),
 'q3_cr_stressfree': ('cr', 'the formation of a completely stress-free wax pattern would appear improbable'),
 'q3_cr_relub': ('cr', 'After the die is cleaned and relubricated, the pattern is replaced on the die'),
 'q3_cr_hollow': ('cr', 'The core of the hollow pin should be filled with sticky wax'),
 'q3_cr_Y': ('cr', 'The Y-sprue design is often used on MOD inlay restorations.'),
 'q3_cr_toward': ('cr', 'the sprue should be directed toward the margins'),
 'q3_cr_gauge': ('cr', 'between 6 and 12 gauge (4.1 and 2.0 mm'),
 'q3_cr_smaller': ('cr', 'however, practically it could be slightly smaller.'),
 'q3_cr_6mm': ('cr', 'be positioned approximately 6 mm from the end'),
 'q3_pw_warm': ('pw', 'Wax patterns are carved with warm (37 °C) instruments'),
 'q3_pw_30': ('pw', 'should be minimized (less than 30 minutes)'),
 'q3_pw_refinish': ('pw', 'details of the pattern such as proximal contacts and margins should be refinished'),
 'q3_pw_resin': ('pw', 'Resins offer higher strength and lower flow than pattern waxes'),
 'q3_pw_lc': ('pw', 'Light-cured resins offer more working time to build the pattern than self-cured resins.'),
 'q3_pw_burn': ('pw', 'all pattern waxes and resins must burn out with no residue'),
 'q3_pw_harden': ('pw', 'Hardeners increase the hardness only 2% if'),
 'q3_bn_type2': ('bn', 'Type II: Soft wax is used for indirect wax pattern'),
 'q3_bn_cote': ('bn', 'COTE, 150–400 ppm/°C and COTE increases with'),
 'q3_bn_memory': ('bn', 'this is known as wax memory'),
 'q3_bn_lowtemp': ('bn', 'invested immediately or stored at low temperatures'),
 'q3_bn_harden': ('bn0', 'surface hardeners, or electroforming methods'),
 'q3_ph_residue': ('ph', 'should not leave a solid residue that amounts to more than'),
 'q3_ph_sets': ('ph', 'no distortion of the pattern will occur'),
 'q3_gg_unequal': ('gg', 'Due to unequal movement of walls of wax pattern while'),
 'q3_cr_compensate': ('cr', 'Die spacers should not be used to compensate for'),
 'q3_st_excess': ('stu', 'Removing the excess die stone with a large crosscut carbide bur'),
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
