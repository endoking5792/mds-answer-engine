import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
F = {
 'aod4': (T+'Operative_and_Dental_Materials_Textbooks/Advanced_Operative_Dentistry.md', 6, 'Bartlett, 2011'),
 'aod16': (T+'Operative_and_Dental_Materials_Textbooks/Advanced_Operative_Dentistry.md', 1, 'Bartlett and Ricketts, 2011'),
 'gold': (T+'Operative_and_Dental_Materials_Textbooks/Esthetics_in_Dentistry_Goldstein.md', 36, 'Goldstein et al, 2018'),
 'hs': (T+'Operative_and_Dental_Materials_Textbooks/Essentials_of_Preclinical_Conservative_Dentistry_Harpreet_Singh.md', 17, 'Singh, 2020'),
 'mz': (T+'Operative_and_Dental_Materials_Textbooks/Operative_Dentistry_Marzouk.md', -3, 'Marzouk et al, undated'),
 'stu': (T+'Operative_and_Dental_Materials_Textbooks/Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter et al, 2019'),
 'mt': (T+'Operative_and_Dental_Materials_Textbooks/Preservation_and_Restoration_of_Tooth_Structure_Mount.md', 16, 'Kaidonis et al, 2016'),
 'ap': (T+'Operative_and_Dental_Materials_Textbooks/Adhesive_Techniques_in_Restorative_Dentistry_Alani_Patel.md', 23, 'Alani and Patel, 2025'),
 'ibb': (T+'Operative_and_Dental_Materials_Textbooks/Advances_in_Operative_Dentistry.md', -3, 'Ibbetson, 2001'),
 'pg': (T+'Operative_and_Dental_Materials_Textbooks/Pickards_Guide_to_Minimally_Invasive_Operative_Dentistry.md', 11, 'Banerjee and Watson, 2015'),
 'mod': (T+'Operative_and_Dental_Materials_Textbooks/Modern_Operative_Dentistry.md', 14, 'Torres et al, 2020'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
#   Pick clean text: avoid OCR ligature damage ("0e", "!le"), hyphen breaks and figure captions.
L = {
 'g5_aod_def_attr': ('aod4', 'Attrition is the wear of tooth against tooth.'),
 'g5_aod_def_abr': ('aod4', 'Abrasion is the mechanical wear of teeth from forces other than teeth.'),
 'g5_aod_def_ero': ('aod4', 'The loss of tooth structure caused by acids and not involving bacterial fermentation is called erosion.'),
 'g5_aod_combo': ('aod4', 'It is uncommon to observe the singular effects of erosion, abrasion or attrition and more commonly it is a combination.'),
 'g5_aod_abf': ('aod4', 'this theoretical phenomenon has yet to be proven clinically'),
 'g5_aod_10pc': ('aod4', 'the more severe forms probably affect around 10% of the population'),
 'g5_aod_facets': ('aod4', 'demonstrate paired wear facets'),
 'g5_aod_filed': ('aod4', 'almost as if they have been filed'),
 'g5_aod_fracture': ('aod4', 'Typically in severe cases fractured restorations are found following the excessive occlusal loading'),
 'g5_aod_stain': ('aod4', 'A stain-free surface can suggest that any acid erosion is active whilst a stained surface suggests the process is inactive.'),
 'g5_aod_brux_stress': ('aod4', 'some component of stress causing repeated tooth clenching or grinding is acknowledged by most clinicians'),
 'g5_aod_interf': ('aod4', 'since interferences are so common in asymptomatic subjects this association remains unproven'),
 'g5_aod_guidance': ('aod4', 'with facets appearing on teeth used in guidance'),
 'g5_aod_age': ('aod4', 'if the same amount of wear was seen in a 20-year-old patient, alarm bells might sound'),
 'g5_aod_notdestroy': ('aod4', 'There is no justification to believe that tooth wear inevitably leads to the total destruction of teeth.'),
 'g5_aod_early': ('aod4', 'the most important aspect to the management of tooth wear is early detection and identification of risk factors'),
 'g5_aod_casts': ('aod4', 'This is traditionally accomplished by examining sequential study casts'),
 'g5_aod_probe': ('aod4', 'perhaps the simplest method is to use a periodontal probe'),
 'g5_aod_diet': ('aod4', 'a diet diary should be carried out like that for dental caries management'),
 'g5_aod_brush': ('aod4', 'patients should be advised not to brush their teeth immediately following an acid drink'),
 'g5_aod_fl': ('aod4', 'there is virtually no clinical patient-based evidence'),
 'g5_aod_dba': ('aod4', 'dentine bonding agents can reduce the amount of wear by half over a period of 6 months'),
 'g5_aod_splint': ('aod4', 'The use of full coverage splints will be effective for those patients with mainly a bruxist habit.'),
 'g5_aod_splint_ero': ('aod4', 'where erosion is a major contributory factor is probably'),
 'g5_aod_vac': ('aod4', 'Although neither has been shown to be more effective, the durability and longevity of the latter will be better.'),
 'g5_aod_michigan': ('aod4', 'full coverage upper hard acrylic splint with canine rises in lateral excursions'),
 'g5_aod_restore_ind': ('aod4', 'The main indications which eventually demand restorative treatment of worn teeth are appearance and intractable sensitivity.'),
 'g5_aod_quiesc': ('aod4', 'tooth wear varies in activity with periods of progression and quiescence'),
 'g5_aod_cost': ('aod4', 'if they cannot afford complex care and aftercare, then monitoring with intensive preventive management may be an effective outcome'),
 'g5_aod_prev': ('aod4', 'if preventive advice is given the rate of tooth wear will reduce'),
 'g5_a16_conform': ('aod16', 'the so-called conformative approach'),
 'g5_a16_height': ('aod16', 'The critical decision is whether there is sufficient proximal height of the teeth to allow conventional crown preparations'),
 'g5_a16_cl': ('aod16', 'If insufficient tooth height remains, crown lengthening will be needed'),
 'g5_a16_cl_dis': ('aod16', 'an adverse crown:root ratio may be produced'),
 'g5_a16_overd': ('aod16', 'the teeth can be preserved as overdenture abutments'),
 'g5_a16_locgen': ('aod16', 'depend on whether the tooth wear is localized or generalized'),
 'g5_a16_dac': ('aod16', 'this is due to dento-alveolar compensation'),
 'g5_a16_dahl_def': ('aod16', 'The Dahl concept utilizes intrusive forces and the eruptive potential of teeth to create differential movement between groups of teeth'),
 'g5_a16_reliable': ('aod16', 'been shown to be a reliable and effective management for short clinical crowns'),
 'g5_a16_pulp': ('aod16', 'the added benefit can be preservation of pulpal health'),
 'g5_a16_early': ('aod16', 'Early Dahl appliances were made using partial dentures or metal occlusal splints'),
 'g5_a16_mvmt': ('aod16', 'the initial tooth movement was mainly intrusion of the teeth opposing the splint, followed by overeruption of the teeth propped apart'),
 'g5_a16_ovd': ('aod16', 'overeruption exceeded intrusion which resulted in a small increased vertical dimension'),
 'g5_a16_34': ('aod16', 'Usually sufficient interocclusal space is created in 3–4 months'),
 'g5_a16_tmd': ('aod16', 'the presence of symptoms before treatment normally contraindicates the use of the Dahl principle'),
 'g5_a16_perio': ('aod16', 'increased periodontal probing depths over 3 mm also contraindicate the use of this technique'),
 'g5_a16_comp': ('aod16', 'most clinicians today use composite build-ups shaped to the ideal contours of the teeth to create the space'),
 'g5_a16_localonly': ('aod16', 'The Dahl movement is only applicable when the tooth wear is localized to a few teeth.'),
 'g5_a16_gen': ('aod16', 'If the tooth wear is generalized the movement is ineffective and a full-mouth rehabilitation is indicated.'),
 'g5_a16_rcp': ('aod16', 'Articulated study casts mounted on a semi-adjustable articulator using a retruded contact position interocclusal record'),
 'g5_a16_adapt': ('aod16', 'have a proven dento-alveolar adaptive capacity'),
 'g5_a16_even': ('aod16', 'the composites need to have an even occlusal contact with the opposing teeth'),
 'g5_a16_35': ('aod16', 'composites used to restore worn anterior teeth will survive between 3 and 5 years'),
 'g5_a16_compret': ('aod16', 'any residual composite remaining on the tooth cannot be considered reliable retention for crowns in the long term'),
 'g5_a16_sceptic': ('aod16', 'The technique is not universally accepted and there is scepticism, particularly in North America.'),
 'g5_a16_39': ('aod16', 'the time needed for the adaption and occlusal changes ranges from 3 to 9 months'),
 'g5_a16_class': ('aod16', 'is less successful with Class III and Class II Division I relationships'),
 'g5_a16_genwax': ('aod16', 'determine the increased occlusal vertical dimension that is required'),
 'g5_a16_leave': ('aod16', 'to leave, where possible, the less severely worn without restorations'),
 'g5_a16_prov': ('aod16', 'These provisional restorations can then be used to assess the appearance, occlusion and function over a period of time.'),
 'g5_a16_thx': ('aod16', 'The terminal hinge axis is used as it is the most reproducible jaw relationship'),
 'g5_a16_quad': ('aod16', 'A quadrant or sextant approach overcomes this problem'),
 'g5_a16_splintmaint': ('aod16', 'more simply by using an occlusal splint which is adjusted accordingly'),
 'g5_gl_def': ('gold', 'Attrition is the loss of tooth structure by mechanical forces from opposing teeth.'),
 'g5_gl_sites': ('gold', 'the palatal surfaces of maxillary anterior teeth, and the labial surfaces of mandibular anterior teeth'),
 'g5_gl_shiny': ('gold', 'The affected surfaces are usually hard, smooth, and shiny.'),
 'g5_gl_yellow': ('gold', 'may exhibit a yellowish-brown'),
 'g5_gl_inter': ('gold', 'Wear may also occur interproximally, causing mesial drifting'),
 'g5_gl_brux': ('gold', 'It is well established that the most common cause of attrition is bruxism.'),
 'g5_gl_func': ('gold', 'Functional habits, such as chewing and swallowing, rarely result in tooth contact'),
 'g5_gl_factors': ('gold', 'These include malocclusion, environmental factors, and genetic factors.'),
 'g5_gl_crossbite': ('gold', 'we see greater wear in teeth that are in crossbite'),
 'g5_gl_dust': ('gold', 'chronic exposure to dust and dirt can also cause increased wear'),
 'g5_gl_genetic': ('gold', 'Both of these conditions make the teeth more susceptible to wear at an increased rate.'),
 'g5_gl_historic': ('gold', 'the current damage may be present from historical behaviors'),
 'g5_gl_casts': ('gold', 'This can be done by making casts and taking digital'),
 'g5_gl_twi': ('gold', 'tooth wear index published by Smith and Knight in 1984'),
 'g5_gl_bruxdef': ('gold', 'Bruxism is a condition in which persons grind, gnash, or clench their teeth.'),
 'g5_gl_sleep': ('gold', 'Sleep bruxism is considered a sleep-related movement disorder.'),
 'g5_gl_mpd': ('gold', 'may also experience symptoms of myofacial pain dysfunction syndrome'),
 'g5_gl_ovd': ('gold', 'there is rarely loss of the vertical dimension of occlusion'),
 'g5_gl_ill': ('gold', 'This approach, however, may be ill advised.'),
 'g5_gl_turner': ('gold', 'Turner proposed a classification system for occlusal wear in 1984'),
 'g5_gl_t1': ('gold', 'excessive wear with loss of occlusal vertical dimension (OVD)'),
 'g5_gl_t2': ('gold', 'excessive wear without loss of OVD but with space available'),
 'g5_gl_t3': ('gold', 'excessive wear without loss of OVD but with limited space'),
 'g5_gl_space': ('gold', 'by clinically evaluating the closest speaking space'),
 'g5_gl_splint3': ('gold', 'This is typically worn for about three months as a way to evaluate whether the new OVD is acceptable.'),
 'g5_gl_dawson': ('gold', 'Develop maxillary incisal edge position.'),
 'g5_gl_guard': ('gold', 'once the prosthetic rehabilitation is completed, an occlusal guard should be fabricated'),
 'g5_gl_gingival': ('gold', 'needs to come from the gingival direction rather than the incisal'),
 'g5_hs_def': ('hs', 'It can also be defined as the physiological wearing of the tooth as a result of tooth-to-tooth contact, as in mastication.'),
 'g5_hs_phys': ('hs', 'is thus more physiological than pathological'),
 'g5_hs_path': ('hs', 'Pathological causes include parafunctional habits such as bruxism.'),
 'g5_hs_hunter': ('hs', 'John Hunter was the first person to describe attrition, abrasion and erosion way back in 1778.'),
 'g5_hs_index': ('hs', 'Noticeable flattening parallel to the occluding planes'),
 'g5_hs_cheek': ('hs', 'Cheek biting is another consequence of occlusal surface attrition.'),
 'g5_hs_proximal': ('hs', 'leading to drifting and overall reduction of the dental arch length'),
 'g5_hs_tx1': ('hs', 'should be controlled by occlusal adjustments and use of'),
 'g5_hs_fl': ('hs', 'use of fluoride solution/dentin bonding agents'),
 'g5_hs_endo': ('hs', 'Teeth with pulp involvement should undergo endodontic therapy or extraction according to their restorability.'),
 'g5_mz_25': ('mz', 'it has been estimated that 25%'),
 'g5_mz_def': ('mz', 'Attrition may be defined as surface tooth structure loss'),
 'g5_mz_brux': ('mz', 'Attrition is accelerated by parafunctional mandibular'),
 'g5_mz_ten': ('mz', 'time (ten years and more), the alveolar bone can grow'),
 'g5_mz_short': ('mz', 'be no chance for the alveolar bone to erupt occlusally'),
 'g5_mz_splint': ('mz', 'proper discluding-protecting occlusal'),
 'g5_mz_equil': ('mz', 'Occlusal equilibration should be performed after all'),
 'g5_mz_metal': ('mz', 'only metallic (metallic-based) restorations should'),
 'g5_mz_fws': ('mz', 'measurements for the free-way space (2-3 mm) can give'),
 'g5_mz_2mm': ('mz', 'increase in vertical is planned (more than 2 mm), it is a wise'),
 'g5_mz_15y': ('mz', 'if attrition has occurred over a long period (more than 15 years)'),
 'g5_mz_endo': ('mz', 'Pulpally involved teeth should be extracted, or undergo'),
 'g5_st_def': ('stu', 'Attrition is the mechanical wear of the incisal or occlusal surface as a result of functional or parafunctional movements of the mandible'),
 'g5_st_prox': ('stu', 'Attrition also includes proximal surface wear at the contact area because of physiologic tooth movement.'),
 'g5_st_cause': ('stu', 'such as tooth grinding, or bruxism, usually resulting from:'),
 'g5_st_cupped': ('stu', 'resulting in cupped-out areas because the exposed, softer dentin wears faster than the surrounding enamel'),
 'g5_st_craze': ('stu', 'Craze lines are not sensitive and do not require treatment'),
 'g5_st_restore': ('stu', 'Areas of significant occlusal attrition that have exposed dentin are sensitive, or annoying should be considered for restoration'),
 'g5_st_occl': ('stu', 'must include an occlusal analysis (which requires articulated diagnostic models)'),
 'g5_st_guard': ('stu', 'occlusal guard therapy should be considered for nocturnal protection of indirect restorations'),
 'g5_mt_facets': ('mt', 'Wear facets on the working surfaces of teeth offer the most objective evidence for identifying tooth grinding'),
 'g5_mt_shiny': ('mt', 'well-defined and polished facets indicate active tooth grinding'),
 'g5_mt_flake': ('mt', 'active grinding can cause enamel flaking on the incisal edges of teeth'),
 'g5_mt_ng': ('mt', 'Polish the occlusal surface to a matte finish only'),
 'g5_mt_young': ('mt', 'Wear in a young individual with a full complement of teeth would be considered as pathologic if it is evident that the dentition will not last into old age.'),
 'g5_mt_normal': ('mt', 'is part of the genetic code, is central in origin and is quite normal'),
 'g5_mt_stress': ('mt', 'The main risk factor responsible for increasing grinding activity is stress'),
 'g5_mt_occl': ('mt', 'there is no correlation between tooth grinding and occlusion'),
 'g5_mt_equil': ('mt', 'Although occlusal equilibrations are not normally advocated'),
 'g5_mt_ng2': ('mt', 'This does not stop the grinding (although it may be reduced initially) but it does conserve tooth structure at the expense of the acrylic of the night guard.'),
 'g5_mt_mousse': ('mt', 'tooth mousse has shown the best results'),
 'g5_mt_c2d2': ('mt', 'Division 2 deep bite configurations'),
 'g5_mt_pristine': ('mt', 'will show severely worn anterior teeth while the posterior teeth remain pristine'),
 'g5_mt_scooped': ('mt', 'A worn dentition with scooped dentine is functional.'),
 'g5_mt_ngend': ('mt', 'the use of a prophylactic night guard at the completion of the treatment is warranted'),
 'g5_ap_tsl': ('ap', 'Tooth surface loss (TSL) is a multifactorial process resulting in the loss of enamel and dentine'),
 'g5_ap_attr': ('ap', 'Attrition is tooth surface loss caused by frictional tooth-to-tooth contact'),
 'g5_ap_demarc': ('ap', 'there is a definite demarcation between the area that is being worn and those areas of the tooth that are being spared'),
 'g5_ap_flat': ('ap', 'The nature of the lesions is flat and rough'),
 'g5_ap_mirror': ('ap', 'The maxillary and mandibular teeth mirror each other in the shape of the occlusal plane.'),
 'g5_ap_ppi': ('ap', 'This may take the form of prescribed medicines such as proton pump inhibitors'),
 'g5_ap_fl': ('ap', 'The use of a high fluoride-containing toothpaste and mouthrinse'),
 'g5_ap_splint': ('ap', 'The use of occlusal splints also will be of benefit for those patients'),
 'g5_ap_cl': ('ap', 'This results in a reduction in periodontal support'),
 'g5_ap_ortho': ('ap', 'This is likely to prolong treatment time and increase treatment financial expense.'),
 'g5_ap_spiral': ('ap', 'restorative failure spiral'),
 'g5_ap_dac': ('ap', 'The OVD and the freeway space are unaltered as the occlusal contacts are maintained by alveolar bone remodelling'),
 'g5_ap_openbite': ('ap', 'If the rate of tooth surface loss is greater than the eruptive potential of the teeth, an open bite will develop.'),
 'g5_ap_dahldef': ('ap', 'The Dahl concept is a method of purposefully inducing physiological tooth movement'),
 'g5_ap_ovd': ('ap', 'Therefore, the OVD is solely increased by the restoration of the anterior teeth.'),
 'g5_ap_6040': ('ap', 'The split between the processes is 60:40, respectively.'),
 'g5_ap_2mm': ('ap', 'if the OVD is increased by 2 mm, re-establishment of occlusal contact would involve 1.2 mm of over-eruption and 0.8 mm of intrusion'),
 'g5_ap_third': ('ap', '2 mm of change in occlusion anteriorly equates to approximately 1/3 of the amount posteriorly'),
 'g5_ap_1975': ('ap', 'The concept was first investigated by Dahl and colleagues in 1975'),
 'g5_ap_platform': ('ap', 'accentuated positive flat inclined cingulum occlusal contact platform'),
 'g5_ap_2plus': ('ap', 'a 2+ mm volume of restorative material is used for increasing the OVD'),
 'g5_ap_attrmat': ('ap', 'an attritive aetiology requires a more durable, harder occlusal surface'),
 'g5_ap_direct': ('ap', 'the advantages of the direct approach include efficiency of time and reduced financial cost'),
 'g5_ap_wax': ('ap', 'The diagnostic wax-up prescription is key to a successful definitive restoration as it forms the blueprint.'),
 'g5_ap_indirect': ('ap', 'Laboratory-fabricated indirect restorations are likely to result in a more resilient restoration with superior physical properties'),
 'g5_ap_gold': ('ap', 'gold alloy is kinder to opposing teeth from an abrasive aspect'),
 'g5_ap_8mo': ('ap', 'Over a period of 8 months, the posterior units begin to re-establish contact'),
 'g5_ap_05': ('ap', '0.5 mm clearance will allow the clinician to visualise the restoration margin'),
 'g5_ib_noovd': ('ibb', 'Patients with slowly progressive wear of the teeth generally do not suffer loss of occlusal vertical dimension.'),
 'g5_ib_contentious': ('ibb', "Altering an individual's vertical dimension of occlusion has always been a somewhat contentious procedure."),
 'g5_ib_overjet': ('ibb', 'as the vertical dimension is increased, the mandible comes to lie in a more posterior position and the overjet is relatively increased'),
 'g5_ib_older': ('ibb', 'in older patients, creation of the space was primarily dependent on intrusion of the teeth in contact with the appliance'),
 'g5_ib_3mo': ('ibb', 'periods in excess of 3 months'),
 'g5_ib_gingiva': ('ibb', 'the gingival tissues accompanied the axial tooth movement'),
 'g5_ib_gic': ('ibb', 'These were constructed in cast-nickel chromium and cemented to the teeth using a glass-ionomer cement.'),
 'g5_ib_occladj': ('ibb', 'Occlusal adjustment for the purpose of creating space is only considered when'),
 'g5_ib_small': ('ibb', 'the number of patients who possess this type of discrepancy is relatively small'),
 'g5_ib_reduce': ('ibb', 'reducing worn teeth still further in height in order to accommodate a crown is inappropriate'),
 'g5_pg_def': ('pg', 'the irreversible surface loss of dental hard tissues caused by factors other than caries or trauma'),
 'g5_pg_phys': ('pg', 'It can be physiological, occurring slowly and naturally throughout life, or pathological'),
 'g5_pg_softened': ('pg', 'Acid-softened tooth surfaces are more'),
 'g5_mo_def': ('mod', 'Attrition is defined as wear by tooth-to-tooth contact without the impact of any other substance.'),
 'g5_mo_phys': ('mod', 'Physiological wear is considered a slow degradation of the dental shape'),
 'g5_mo_splint': ('mod', 'Since elimination of the parafunctional habits is very hard to achieve, occlusal acrylic resin splints are used'),
 'g5_mo_gold': ('mod', 'Cast gold restorations are usually softer than enamel and amalgam, resulting in less wear of the antagonistic tooth.'),
 'g5_mo_feld': ('mod', 'Feldspar ceramics produce extensive antagonistic tooth wear'),
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
