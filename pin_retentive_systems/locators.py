import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.environ.get('MDS_TEXTBOOKS', os.path.expanduser('~/mds-textbooks/'))   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
F = {
 'stu': (T+'Operative_and_Dental_Materials_Textbooks/Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter et al, 2019'),
 'sum': (T+'Operative_and_Dental_Materials_Textbooks/Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Overton, Summitt and Osborne, 2013'),
 'mar': (T+'Operative_and_Dental_Materials_Textbooks/Operative_Dentistry_Marzouk.md', 0, 'Marzouk et al, n.d.'),
 'mcc': (T+'Operative_and_Dental_Materials_Textbooks/Applied_Dental_Materials_McCabe_Walls_9th.md', 9, 'McCabe and Walls, 2008'),
 'phi': (T+'Operative_and_Dental_Materials_Textbooks/Phillips_Science_of_Dental_Materials.md', 16, 'Anusavice et al, 2013'),
 'van': (T+'Operative_and_Dental_Materials_Textbooks/Introduction_to_Dental_Materials_4th.md', None, 'van Noort and Barbour, 2013'),
 'cra': (T+'Operative_and_Dental_Materials_Textbooks/Restorative_Dental_Materials_Craig_Michigan_11th.md', 10, 'Craig, 2002'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
#   Pick clean text: avoid OCR ligature damage ("0e", "!le"), hyphen breaks and figure captions.
L = {
 # Sturdevant
 's_def': ('stu','any restoration requiring the placement of one or more pins in dentin to provide adequate resistance and retention forms'),
 's_4mm': ('stu','loss of 4 mm or more of vertical coronal height'),
 's_slots': ('stu','not able to be established with slots, grooves or undercuts only'),
 's_adv': ('stu','significantly greater retention compared with restorations using boxes only or restorations relying solely on bonding systems'),
 's_craze': ('stu','may create craze lines or fractures and internal stresses in dentin'),
 's_perf': ('stu','increased risk of penetrating into the pulp or perforating the external tooth surface'),
 's_tens': ('stu','decreases the tensile and horizontal strength of pin-retained amalgam restorations'),
 's_three': ('stu','There are three types of pins for pin-retained amalgam restorations'),
 's_markley': ('stu','In 1958, Markley described a technique for restoring teeth with amalgam and cemented pins'),
 's_cemsize': ('stu','prepared 0.025– 0.05 mm larger than the diameter of the pin'),
 's_luting': ('stu','The cementing medium may be any standard dental luting agent'),
 's_goldstein': ('stu','In 1966, Goldstein described a technique for the friction-locked pin'),
 's_frsize': ('stu','The diameter of the prepared pinhole is 0.025 mm smaller than the diameter of the pin'),
 's_frtap': ('stu','The pins are tapped into place, retained by the resiliency of the dentin'),
 's_fr23': ('stu','They are 2–3 times more retentive than cemented pins'),
 's_rare': ('stu','Friction-locked and cemented pins, although still available, are rarely used'),
 's_stmost': ('stu','The most frequently used type of parapulpal pin is the self-threading pin'),
 's_going': ('stu','originally was described by Going in 1966'),
 's_stsize': ('stu','The diameter of the prepared pinhole is 0.03–0.10 mm smaller than the diameter of the pin'),
 's_elast': ('stu','The elasticity (resiliency) of dentin permits insertion of a threaded pin into a hole of smaller diameter'),
 's_st36': ('stu','being 3–6 times more retentive than cemented pins'),
 's_notfull': ('stu','do not engage dentin for their entire width'),
 's_crazesize': ('stu','Craze lines in dentin are related to the size of the pin'),
 's_pulpstress': ('stu','Pulpal stress is maximal when the self-threading pin is inserted perpendicular to the pulp'),
 's_depth': ('stu','Recommended pinhole depth is generally accepted to be 2 mm'),
 's_depthrange': ('stu','The depth of the pinhole varies from 1.3 to 2 mm'),
 's_tms': ('stu','is the most widely used self-threading pin system'),
 's_tmsmat': ('stu','TMS pins are available in gold-plated stainless steel or in titanium'),
 's_order': ('stu','the self-threading pin is the most retentive, the friction-locked pin is intermediate and the cemented pin is the least retentive'),
 's_surface': ('stu','The shape of the self-threading pin results in the greatest retention of amalgam'),
 's_nonpar': ('stu','Placing pins in a nonparallel manner increases their ability to retain the restoration'),
 's_bendno': ('stu','bending pins to improve their retention in amalgam is not advised'),
 's_1mmlat': ('stu','approximately 1 mm) between the pin and the external surface of the finished restoration'),
 's_number': ('stu','crazing of dentin and the potential for fracture increase'),
 's_ext': ('stu','Self-threading pin extension into dentin and amalgam should be approximately 1.5–2 mm'),
 's_nearline': ('stu','pinholes should be located near the line angles of the tooth'),
 's_pilot': ('stu','a No. ¼ round bur is first used to prepare a pilot hole'),
 's_sizes': ('stu','(A) Regular (0.78 mm). (B) Minim (0.61 mm). (C) Minikin (0.48 mm). (D) Minuta (0.38 mm)'),
 's_minikin': ('stu','the pins of choice for severely involved posterior teeth are the Minikin (0.48 mm)'),
 's_minim': ('stu','used as a backup in case the pinhole for the Minikin is overprepared'),
 's_minuta': ('stu','The Minuta is usually too small to provide adequate retention in posterior teeth'),
 's_regular': ('stu','the Regular pin is associated with the highest incidence of dentinal crack communication with the pulp'),
 's_oneper': ('stu','As a general rule, one pin per missing axial line angle should be used'),
 's_2mmover': ('stu','Occlusal clearance should be sufficient to provide 2 mm of amalgam over the pin'),
 's_underocc': ('stu','a pin oriented vertically and positioned directly below an occlusal contact point weakens amalgam significantly'),
 's_dej': ('stu','no closer than 0.5–1 mm to the DEJ or no closer than 1–1.5 mm to the external surface of the tooth, whichever distance is greater'),
 's_parallel': ('stu','The pinhole should be parallel to the adjacent external surface of the tooth'),
 's_clear': ('stu','minimum 0.5-mm clearance around the circumference of the pin'),
 's_levels': ('stu','they should be located at different vertical levels on the tooth'),
 's_interpin': ('stu','The minimal interpin distance is 3 mm for the Minikin pin and 5 mm for the Minim pin'),
 's_furcal': ('stu','Fluted and furcal areas should be avoided'),
 's_rpm': ('stu','very low speed (300–500 rpm)'),
 's_onetwo': ('stu','The pinhole is prepared in one or two movements without allowing the drill to stop rotating'),
 's_quarter': ('stu','rotated one-quarter to one-half turn counterclockwise to reduce the dentinal stress'),
 's_remove2': ('stu','Any length of pin greater than 2 mm should be removed'),
 's_five': ('stu','The failure of pin-retained restorations might occur at any of five different locations'),
 's_pdfail': ('stu','Failure is more likely to occur at the pin–dentin interface than at the pin–restoration interface'),
 's_slotind': ('stu','Slots are particularly indicated in short clinical crowns and when cusp reduction has been limited to 2 or 3 mm'),
 's_slotless': ('stu','slots are less likely to (i) create microfractures in dentin'),
 's_slotinfl': ('stu','may elicit an inflammatory response if placed within 0.5 mm of the pulp'),
 's_slotsim': ('stu','The retention potential of slots and pins is similar'),
 's_linkself': ('stu','The Link Series pin is free floating in a plastic sleeve, which allows self-alignment'),
 's_linkplus': ('stu','This design has a sharper thread, a shoulder stop at 2 mm'),
 's_selfshear': ('stu','the head of the pin shears off leaving a length of pin extending from dentin'),
 's_twoinone': ('stu','The two-in-one pin is actually two pins in one'),
 's_endo': ('stu','prefabricated posts and cast post/cores are used to provide additional retention for the foundation material in endodontically treated teeth'),
 # Summitt
 'u_types': ('sum','cemented, friction-locked, and self-threading'),
 'u_primary': ('sum','the self-threading pins are the primary pins in current use'),
 'u_dilts': ('sum','recommended a depth in dentin of 2 to 3 mm as optimum for self-threading pins'),
 'u_moffa': ('sum','a pin length of approximately 2 mm into amalgam provides optimum retention'),
 'u_dentthreads': ('sum','it is the dentinal threads that shear and not the metal threads'),
 'u_shoulder': ('sum','The purpose of this feature is to prevent the end of the pin from putting stress on the dentin at the end of the pin channel'),
 'u_noevid': ('sum','there is no evidence of problems associated with pins that lack effective shoulder stops'),
 'u_titan': ('sum','The Link and Link Plus pins are available in either gold-plated stainless steel or titanium alloy'),
 'u_discont': ('sum','several manufacturers have discontinued the production of retentive pins'),
 'u_dej': ('sum','Pin channels should be initiated at least 0.5 mm from the DEJ'),
 'u_dej1': ('sum','a 1.0-mm distance from the DEJ is preferable'),
 'u_dam': ('sum','A rubber dam should be in place when pin channels are prepared'),
 'u_lineangle': ('sum','The most common location for pins is at the line angles of the tooth'),
 'u_mismatch': ('sum','this size difference is called the pin-to–pin channel mismatch'),
 'u_autoclave': ('sum','Pin channel drills should be sterilized with dry heat, chemical vapor, or immersion in glutaraldehyde'),
 'u_horiz': ('sum','horizontal pins, used to cross-splint cusps of maxillary premolars, reinforce and strengthen the cusps'),
 'u_perfpulp': ('sum','the channel should be covered immediately with calcium hydroxide or mineral trioxide aggregate (MTA)'),
 'u_perfext': ('sum','If the perforation is located above the epithelial attachment, the channel should be filled with amalgam'),
 'u_slot': ('sum','found no significant differences between the resistance provided by the two techniques'),
 'u_slip': ('sum','the pin restorations had a greater tendency to slip on their bases before failure'),
 'u_amalgapin': ('sum','the resistance to displacement provided by amalgapins is similar to that provided by pins'),
 'u_apdepth': ('sum','a depth of 1.5 to 2.0 mm is adequate for amalgapins'),
 'u_90deg': ('sum','the stainless steel pins provide significantly more resistance than amalgam inserts'),
 'u_distribute': ('sum','It is important to distribute mechanical resistance features into all areas of the preparation'),
 'u_risks': ('sum','crazing of tooth structure, perforation into the pulp or periodontium, and weakening of the amalgam restoration over pins'),
 'u_bondevid': ('sum','properly bonded amalgam restorations will be as successful as pin-retained amalgam restorations'),
 'u_6yr': ('sum','After 5 years, seven of the pin-retained and two of the bonded restorations had failed'),
 'u_nodebond': ('sum','None of the bonded amalgam restorations had debonded'),
 'u_additive': ('sum','Pins and bonding can have an additive effect'),
 'u_filled': ('sum','the improved efficacy of filled resins compared with unfilled or minimally filled resins'),
 'u_retdef': ('sum','Retention has been defined as prevention of dislodgment of the restoration along the path of insertion'),
 'u_resdef': ('sum','Resistance is defined as prevention of dislodgment or fracture by oblique or compressive forces'),
 's_fewwalls': ('stu','Pin retention is used more frequently in preparations with few or no vertical walls'),
 's_chamber': ('stu','The pulp chamber and entrance to the root canals of endodontically treated molar teeth typically provide retention for foundations'),
 'u_vertical': ('sum','vertical pins provide excellent retention and resistance form'),
 'u_gold': ('sum','a gold alloy casting is considered by many to be the restoration of choice'),
 'u_ceramic': ('sum','Newer ceramic materials with high strength and wear resistance also represent viable options'),
 'u_amalalt': ('sum','amalgam is an excellent alternative restorative material'),
 'u_90': ('sum','loaded at a 90-degree angle instead of a 45-degree angle'),
 'u_6y': ('sum','At 6 years, the results continued to demonstrate'),
 'u_45': ('sum','These teeth were mounted at a 45-degree angle'),
 'u_notenl': ('sum','this method of testing is not as enlightening as long-term clinical tests'),
 'u_32': ('sum','32 bonded (Amalgambond Plus with HPA powder'),
 'u_28': ('sum','28 pin-retained (TMS pins)'),
 'u_onecusp': ('sum','each restoration replaced at least one cusp'),
 'u_sum': ('sum','approximately equal to the sum of the mean resistance produced by pins alone'),
 'u_tms4': ('sum','compared it with four pins (TMS Minim)'),
 'm_adapt': ('mar','amalgam offers less voids and more adaptability around pins than composite resins do'),
 'm_rightangle': ('mar','if the pins are placed at right angles to the direction of the tensile stresses'),
 # Marzouk
 'm_order': ('mar','This is followed by zinc phosphate cement, polycarboxylate cement, and ZOE'),
 'm_nosafe': ('mar','there is no practical safe location for friction grip pins'),
 'm_cemsz': ('mar','For this type, the pin channel is larger in diameter than the pin'),
 'm_frsz': ('mar','In this type, the pin channel is slightly narrower in diameter than the pin'),
 'm_frone': ('mar','These come in one size only'),
 'm_thr4': ('mar','These come in four sizes'),
 'm_stresscem': ('mar','in cemented pin techniques, there are little or no stresses'),
 'm_stressfr': ('mar','Maximum stresses are associated with the friction grip technique'),
 'm_stressthr': ('mar','The threaded pin technique introduces stresses intermediate to the other techniques'),
 'm_modern': ('mar','modern pins have a lesser number of threads with a greater distance between these threads'),
 'm_nonvital': ('mar','not use threaded or frictional grip pins in endodontically treated teeth'),
 'm_4mm': ('mar','It is advisable to not insert pins closer than 4 mm from each other when using small threaded pins'),
 'm_ratio': ('mar','The ideal ratio of dentinal engagement: pin protrusion is 2:1'),
 'm_auxil': ('mar','pins should be used only as an auxillary means of retention'),
 'm_56': ('mar','self-threading pins will be 5-6 times more retentive than cemented pins'),
 'm_23': ('mar','Friction grip pins will have 2-3 times the retention of a cemented pin'),
 'm_cemlin': ('mar','A linear relationship without a plateau exists in case of'),
 'm_frplat': ('mar','Failure always occurs at the pin-dentin interface'),
 'm_smallplat': ('mar','Failures usually occur within pins themselves'),
 'm_cement': ('mar','copper-phosphate cement (which is only to be used in non-vital teeth) is the most retaining cement'),
 'm_varnish': ('mar','Using varnish with zinc phosphate cement will decrease its retaining power by almost 40%'),
 'm_dejcraze': ('mar','cemented pins, even if they are located at the DEJ, do not create any crazing'),
 'm_frcraze': ('mar','Friction lock pins create the maximum number and extent of crazings'),
 'm_safe': ('mar','1.5-2.0 mm from the DEJ is safe for threaded pins'),
 'm_compr': ('mar','Pins will nor increase the compressive strength of the restorative material'),
 'm_2mmapart': ('mar','Pins are closer than 2 mm to each other'),
 'm_compfail': ('mar','the failure rate of composite resin restorations retained by pins is higher than the amalgam restoration retained in the same way'),
 'm_tens3040': ('mar','There will be severe reduction (30-40%) in the tensile strength'),
 'm_tens10': ('mar','A moderate reduction (10%) in tensile strength'),
 'm_tens0': ('mar','No reduction of tensile strength will occur if the pins are placed parallel'),
 'm_frleast': ('mar','Friction grip pins are the least retentive for amalgam and composite resins due to their smooth surfaces'),
 'm_four': ('mar','Cemented pins and threaded pins are four times more retentive than the friction grip'),
 'm_proxim': ('mar','the proximity of the restorative material to the pin is the most influential factor in pin retention to the restorative material'),
 'm_plating': ('mar','gold or silver plating of SS pins is not as effective as would be expected'),
 'm_silver': ('mar','All-silver pins are not effective retaining means because of their plasticity and affinity to mercury'),
 'm_crosslink': ('mar','Pins are also indicated for use as a cross-linkage mode'),
 'm_econ': ('mar','pin retained build-ups in amalgam or composite may serve as an economical restoration'),
 'm_least': ('mar','This is the least desirable indication'),
 'm_provis': ('mar','pin-retained restorations may be used as an economic provisional restoration'),
 'm_antirot': ('mar','to prevent rotation of the restoration around the post in the root canal'),
 'm_threaded68': ('mar','Threaded posts are almost six to eight times more retentive'),
 'm_parallel': ('mar','parallel sided posts are almost 2-3 times'),
 'm_torsion': ('mar','Torsional forces are the most, disengaging type for a post'),
 'm_root2': ('mar','The ideal ratio is to have the root portion of the post twice'),
 'm_halftwo': ('mar','As a rule from one-half to two-thirds of the'),
 'm_ferrule': ('mar','This is the major protecting'),
 'm_reciproc': ('mar','A post cannot solely retain a restoration (foundation), and'),
 'm_2mmplat': ('mar','In the case of small threaded pins, there is no increase in the resistance to failure after 2 mm of dentinal engagement'),
 'm_45': ('mar','if the pins are placed at 45° to the direction of the induced stresses'),
 'm_flat': ('mar','are the second major feature used'),
 'm_lever': ('mar','will make the dentinal portion of the pin the short side of a type one lever'),
 'm_elastic': ('mar','If these stresses exceed the elastic limit of the dentin, permanent (plastic) deformation will occur'),
 'm_gingpin': ('mar','avoid the insertion of a gingival pin in isthmus portion of a cavity preparation'),
 'm_stressarea': ('mar','Inserting pins in a stress concentration area of a tooth'),
 'm_68torsion': ('mar','from 6 to 8 times'),
 'm_antirotdev': ('mar','every rounded post should'),
 'm_continuous': ('mar','Continuous threads from one end of a post to another create'),
 'm_serrated': ('mar','are about three to four times as retentive as smooth surface'),
 'm_hydraulic': ('mar','Hydraulic pressure during post cementation'),
 'm_space': ('mar','there should be a space'),
 'm_apical': ('mar','catastrophic failures'),
 # McCabe
 'c_chips': ('mcc','such pins are retained by tightly packed dentine chips'),
 'c_shoulder': ('mcc','Pins which have a shoulder which engages the tooth tissue before the threaded shaft of the pin contacts the base of the pin hole cause less damage'),
 'c_weaken': ('mcc','All dentine pins weaken the restoration in which they are placed so they should be used sparingly'),
 'c_tap': ('mcc','a thread on the pin acts as its own tap to cut a thread into the dentine'),
 'c_thermal': ('mcc','this protective effect can be negated if a dentine pin is used'),
 'c_adhesive': ('mcc','The most recent innovation for retention of amalgam is the use of chemically-active adhesive resins'),
 # Phillips, van Noort
 'p_served': ('phi','threaded pins or retentive grooves placed in dentin, have served well for years toward these ends'),
 'p_4meta': ('phi','bonding agents employing M–R–X-type adhesive monomers have achieved some clinical success'),
 'v_gic': ('van','GICs should not be used where they are going to be subjected to high tensile loads, such as incisal tip restorations, cuspal replacement or pin-retained cores'),
 'v_core': ('van','posteriorly, it may still be possible to use a pin-retained core'),
 'v_stpost': ('van','self-threading posts have excellent retention but are also associated with a high incidence of tooth fracture'),
 'v_taper': ('van','Tapered posts are the least retentive'),
 # Craig
 'g_methods': ('cra','brittle coatings analysis, strain gauges, holography, two- and threedimensional photoelasticity, finite element analysis'),
 'g_posts': ('cra','endodontic posts, and implants have been reported'),
 'g_aniso': ('cra','The material becomes anisotropic (its properties exhibit a directional dependence) when stressed'),
 'g_double': ('cra','the plastic model exhibits double refraction'),
 'g_fringe': ('cra','represent locations where the difference in the principal stresses is a constant'),
 'g_higher': ('cra','areas containing fringes of higher order are under higher stress'),
 'g_pe_adv': ('cra','a birefringent material is needed and the technique is more difficult with complex geometries'),
 'g_fe_def': ('cra','a finite number of discrete structural elements are interconnected at a finite number of points or nodes'),
 'g_fe_input': ('cra','the elastic moduli and Poisson\'s ratio for the materials'),
 'g_fe_lim': ('cra','are purely numerical, are based on many limiting assumptions, and are potentially costly'),
 'g_fe_trend': ('cra','best suited for predicting trends and performing parametric analyses'),
 'g_fe_valid': ('cra','increased emphasis on experimental validation of numerical results'),
}
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
    bad = 0
    for k in L:
        lab = page_label(k)
        if lab is None: bad += 1; print('MISSING', k, L[k][1][:70])
    print('checked', len(L), 'missing', bad)
