import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
F = {
 'kidd': (T+'Operative_and_Dental_Materials_Textbooks/Essentials_of_Dental_Caries_4th.md', 13, 'Kidd and Fejerskov, 2016'),
 'mod3': (T+'Operative_and_Dental_Materials_Textbooks/Modern_Operative_Dentistry.md', 14, 'Torres, 2020'),
 'mod14': (T+'Operative_and_Dental_Materials_Textbooks/Modern_Operative_Dentistry.md', 7, 'Torres, 2020'),
 'mod16': (T+'Operative_and_Dental_Materials_Textbooks/Modern_Operative_Dentistry.md', 6, 'Torres, 2020'),
 'sum': (T+'Operative_and_Dental_Materials_Textbooks/Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Hilton et al, 2013'),
 'gold12': (T+'Operative_and_Dental_Materials_Textbooks/Esthetics_in_Dentistry_Goldstein.md', 14, 'Goldstein et al, 2018'),
 'gold21': (T+'Operative_and_Dental_Materials_Textbooks/Esthetics_in_Dentistry_Goldstein.md', 36, 'Goldstein et al, 2018'),
 'pick': (T+'Operative_and_Dental_Materials_Textbooks/Pickards_Guide_to_Minimally_Invasive_Operative_Dentistry.md', 11, 'Banerjee and Watson, 2015'),
 'stu': (T+'Operative_and_Dental_Materials_Textbooks/Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter et al, 2019'),
 'sikri': (T+'Operative_and_Dental_Materials_Textbooks/Textbook_of_Conservative_and_Restorative_Dentistry.md', 19, 'Sikri, 2020'),
 'det': (T+'Operative_and_Dental_Materials_Textbooks/Detection_and_Assessment_of_Dental_Caries.md', 6, 'Machiulskiene, 2019'),
 'alani': (T+'Operative_and_Dental_Materials_Textbooks/Adhesive_Techniques_in_Restorative_Dentistry_Alani_Patel.md', 20, 'Alani and Patel, 2025'),
 'mount': (T+'Operative_and_Dental_Materials_Textbooks/Preservation_and_Restoration_of_Tooth_Structure_Mount.md', 16, 'Mount et al, 2016'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
#   Pick clean text: avoid OCR ligature damage ("0e", "!le"), hyphen breaks and figure captions.
L = {
 # histology and optics
 'g6_kidd_wsl': ('kidd', "The early stages often appear chalky white (also called"),
 'g6_kidd_subsurf': ('kidd', "the loss of mineral occurs in the subsurface enamel and that the thickness of the surface zone may vary considerably"),
 'g6_kidd_pore5': ('kidd', "The white spot caries lesion has a pore volume of more than 5% on a smooth surface"),
 'g6_kidd_moth': ('kidd', "active enamel caries surfaces appear moth-eaten"),
 'g6_kidd_surfF': ('kidd', "an enamel surface covering a white spot lesion contains more fluoride than the surrounding sound, normal enamel"),
 'g6_mod_zones': ('mod3', "with a porosity volume of approximately 1%, called surface zone, and a subsurface porous part, with a porosity volume of 5–25%, called the lesion body"),
 'g6_mod_dark': ('mod3', "called dark zone, with 2–4% of porosity"),
 'g6_mod_ri': ('mod3', "When the enamel is intact, the whole tissue has a refractive index of 1.62"),
 'g6_mod_water': ('mod3', "which has a refractive index of 1.33"),
 'g6_mod_maze': ('mod3', "becoming imprisoned in an “optical maze” that is over-luminous and therefore perceived as white"),
 'g6_mod_air': ('mod3', "which has an even lower reflection index, equal to 1"),
 'g6_mod_depth1': ('mod3', "White spot lesions, which require air-drying, are most likely to be limited to the outer ½ of the enamel"),
 'g6_mod_activegloss': ('mod3', "active enamel caries lesions present an opaque white, chalky, and dull surface. In contrast, non-active, arrested initial lesions show a glossy white surface after drying"),
 'g6_mod_probe': ('mod3', "if the surface pseudo-intact layer is destroyed and breached, for example, by probing with a dental instrument, a bacterial invasion into the body of the lesion will occur"),
 'g6_mod_3349': ('mod3', "Clinical studies demonstrate that only 33 to 49% of white spot lesions disappear when being arrested"),
 'g6_mod_poresclose': ('mod3', "once the pores of the surface zone are closed, minerals will not be deposited homogeneously inside the lesion body"),
 'g6_mod_stain': ('mod3', "pigments and dyes present in the oral cavity from the diet can deposit into the porosity, changing the white spots to darkish or brownish spots"),
 'g6_mod16_ri165': ('mod16', "While the sound enamel has a RI of 1.65"),
 'g6_sum_ri': ('sum', "refractive indices of water (1.33), enamel (1.62) and air (1.0)"),
 'g6_sum_wet': ('sum', "A white spot lesion visible on a wet tooth surface indicates that demineralization is over halfway through the enamel"),
 'g6_sum_prog': ('sum', "Prognostically, the latter condition has a better chance of complete reversal, while the former condition may only be arrested"),
 'g6_stu_def': ('stu', "In enamel caries, non-cavitated lesions are also referred to as"),
 'g6_stu_3wk': ('stu', "can produce non-cavitated initial (‘white spot’) lesions (first clinical evidence of demineralization) in 3 weeks"),
 'g6_stu_18m': ('stu', "is estimated to be 18 months (±6 months)"),
 'g6_stu_backer': ('stu', "only 9 of 72 non-cavitated lesions became cavitated"),
 'g6_stu_backer2': ('stu', "More than half of non-cavitated lesions (37 of 72) regressed to become indistinguishable from normal enamel"),
 'g6_stu_bluntprobe': ('stu', "only lesions in which a blunt probe"),
 # remineralisation limits
 'g6_kidd_body': ('kidd', "remineralization of the lesion body is not obtained to any significant degree in vivo"),
 'g6_kidd_ortho': ('kidd', "in particular in caries lesions developed during orthodontic treatment"),
 'g6_kidd_inactive': ('kidd', "Once a lesion has become inactive (or arrested) its appearance cannot be changed unless the surface is mechanically polished or ground or by stripping a layer off it with a strong acid"),
 'g6_pick_arrest': ('pick', "If plaque is removed, these lesions can arrest and porosities can be eliminated by abrasive toothbrushing/tooth wear"),
 'g6_pick_bsl': ('pick', "This process creates an arrested brown spot lesion (BSL) with a hard shiny overlying smooth surface"),
 # orthodontic
 'g6_sum_ortho': ('sum', "White spot lesions appear within a few weeks after appliance placement, particularly with ill-fitting bands"),
 'g6_sum_orthobact': ('sum', "A rise in cariogenic bacteria (S mutans and Lactobacillus) has been documented following placement of orthodontic appliances"),
 'g6_sum_orthoGIC': ('sum', "Fluoride-releasing resin composites and RMGI cements inhibit demineralization adjacent to orthodontic bands and brackets"),
 'g6_stu_ortho': ('stu', "Poor oral hygiene during orthodontic treatment frequently results in these types of decalcified defects"),
 'g6_stu_orthoint': ('stu', "such spots are not indications for invasive treatment (unless for esthetic concerns)"),
 'g6_mod16_ortho': ('mod16', "Typically, white spot lesions on the smooth surfaces occur due to inadequate oral hygiene, e.g., during an orthodontic treatment with brackets"),
 # developmental
 'g6_kidd_fluor': ('kidd', "Dental fluorosis is an enamel hypomineralization along the entire enamel surface"),
 'g6_kidd_fluorstriae': ('kidd', "a fine pattern of enhanced striae of Retzius can be observed across the enamel surface"),
 'g6_kidd_snow': ('kidd', "This phenomenon is called snowcapping if found on cusp tips"),
 'g6_kidd_TF': ('kidd', "These changes can be classified and scored from 1 to 9"),
 'g6_kidd_matur': ('kidd', "enamel maturation, from the end of enamel secretion until tooth eruption, is very sensitive to fluoride"),
 'g6_gold_fluorhist': ('gold12', "a hypomineralized, porous subsurface enamel below a well-mineralized surface layer"),
 'g6_gold_demarc': ('gold21', "Enamel opacities due to fluoride ingestion are poorly demarcated"),
 'g6_gold_nonF': ('gold21', "non-fluoride opacities are usually round or oval and well demarcated"),
 'g6_gold_hypopl': ('gold21', "enamel hypoplasia is a reduction in the thickness or amount of enamel formed"),
 'g6_gold_isolated': ('gold21', "if isolated teeth are affected, irradiation, trauma, or infection is usually the cause"),
 'g6_gold_hypocal': ('gold21', "It can occur locally as a white spot"),
 'g6_mount_mih': ('mount', "where the teeth appear chalky or show cloudy or demarcated creamy yellow or light brown opacities"),
 'g6_mount_mihloss': ('mount', "there is usually rapid loss of tooth structure soon after"),
 'g6_mount_mihcaries': ('mount', "high susceptibility to caries"),
 'g6_mount_mihsens': ('mount', "the affected teeth are usually very sensitive to hot and cold and there may be difficulty in achieving anaesthesia"),
 'g6_mount_mihage': ('mount', "probably occur between the period of birth to approximately 3 years of age"),
 'g6_mount_mihprev': ('mount', "ranging from approximately 4–38% in Europe"),
 'g6_pick_mih': ('pick', "White-yellow or yellow-brown opacities, easily chipped"),
 'g6_pick_fluor': ('pick', "Chalky-white flecks, confluent blotches, brown discoloration, pitted enamel"),
 'g6_sum_table': ('sum', "Smooth, glossy, and less opaque surface when air dried"),
 'g6_sum_site': ('sum', "Located mainly in self-cleansing areas"),
 'g6_sum_bilat': ('sum', "white spots that occur on corresponding sites and have similar shape on all corresponding teeth"),
 'g6_stu_hydr': ('stu', "whereas hypocalcified enamel is affected less by drying and wetting"),
 # diagnosis
 'g6_kidd_icdas': ('kidd', "It is a visual ranked scoring system that assesses the depth of lesion penetration, including the non-cavitated stages of caries"),
 'g6_kidd_icdas1': ('kidd', "Opacity or discolouration is hardly visible on a wet surface but distinctly visible after air drying for 5 seconds"),
 'g6_kidd_icdas2': ('kidd', "Opacity or discolouration is distinctly visible without drying"),
 'g6_kidd_icdas3': ('kidd', "Localized enamel breakdown in opaque or discoloured enamel"),
 'g6_kidd_twodigit': ('kidd', "each tooth surface is designated by two digits"),
 'g6_kidd_nyvad': ('kidd', "We prefer to use the so- called Nyvad"),
 'g6_kidd_doubt': ('kidd', "If in doubt whether a non-cavitated lesion is active, judge it as active and institute non-operative caries control measures"),
 'g6_kidd_matt': ('kidd', "Arrested lesions, on the other hand, may be located free of the gingival margin"),
 'g6_pick_icdas1h': ('pick', "Enamel demineralization limited to outer 50%"),
 'g6_det_active': ('det', "Active enamel caries lesions are characterized by matt/chalky, whitish, or yellowish appearance"),
 'g6_det_sticky': ('det', "Very often the active lesions may be covered with a thin, sticky plaque layer"),
 'g6_det_inactive': ('det', "In contrast, inactive caries lesions are glossy and smooth on probing"),
 'g6_det_white': ('det', "it can be as white as an active lesion"),
 'g6_det_dry': ('det', "carefully dried with a blast of air for 10–15 s"),
 'g6_det_risk': ('det', "the active non-cavitated lesions run a significantly greater risk of progressing to a cavity than do the inactive (arrested) non-cavitated lesions"),
 # management
 'g6_pick_varnish': ('pick', "with concentrations of 22 600 ppm F or 2.2% F"),
 'g6_pick_varnisheff': ('pick', "and that in the permanent dentition by nearly half"),
 'g6_pick_third': ('pick', "dentition by a third"),
 'g6_pick_varnishint': ('pick', "Professional application must be repeated at 3-monthly"),
 'g6_pick_hiF': ('pick', "High-concentration prescription toothpastes can be beneficial for controlling caries (2800/5000 ppm fluoride)"),
 'g6_pick_rinseortho': ('pick', "patients with orthodontic appliances, which inevitably encourage plaque accumulation and predispose to carious lesions"),
 'g6_pick_cpp': ('pick', "natural predilection to convert to hydroxyapatite (HAP) in wet"),
 'g6_pick_cppev': ('pick', "but further long-term trials are needed to provide conclusive clinical evidence"),
 'g6_kidd_paste': ('kidd', "the family fluoride toothpaste (1350–1500 ppm fluoride) is indicated"),
 'g6_kidd_spit': ('kidd', "‘spit, don’t rinse’, is the relevant advice"),
 'g6_mod_caf2': ('mod3', "a calcium fluoride-like layer (CaF2) is formed on the surface"),
 'g6_stu_varnish3': ('stu', "For high-risk patients of caries, fluoride varnish should be applied every 3 months"),
 'g6_stu_cpp': ('stu', "Remineralization products use CPP as a vehicle and maintains a supersaturation state of ACP at or near the tooth surface"),
 'g6_stu_cppF': ('stu', "most of these studies have not looked at its effect independent of fluoride"),
 'g6_stu_milk': ('stu', "must not be prescribed to patients with allergies to dairy (milk) proteins"),
 'g6_sum_mipaste': ('sum', "a casein phospho-peptide with amorphous calcium phosphate–containing paste with 900 ppm fluoride"),
 'g6_sum_varn5': ('sum', "Generally a 5% NaF-containing varnish should be used in hard-to-clean areas that are prone to white spot lesion development"),
 # infiltration
 'g6_mod16_micro': ('mod16', "As it is not associated with any preparatory measures, it could also be classified as microinvasive"),
 'g6_mod16_fill': ('mod16', "this technique aims to fill the pores within the carious lesion with liquid resin material"),
 'g6_mod16_hcl': ('mod16', "the sole one able to sufficiently remove the surface layer is 15% hydrochloric acid, applied for 2 min"),
 'g6_mod16_ethanol': ('mod16', "absolute ethanol is applied and has to be dried completely in order to remove the remaining water"),
 'g6_mod16_capill': ('mod16', "driven by capillary forces, into the lesion body"),
 'g6_mod16_noncav': ('mod16', "Infiltration technique can be used only in case of non-cavitated lesions"),
 'g6_mod16_D1': ('mod16', "The resin infiltration technique is indicated for caries lesions in the proximal region with radiographic image up to external third of the dentin (D1)"),
 'g6_mod16_steps': ('mod16', "application of the infiltrant, and incubation for 3 min"),
 'g6_mod16_steps2': ('mod16', "Rerunning of the last step, incubation for 1 min, and light-curing from all sides for 40 s"),
 'g6_mod16_radiop': ('mod16', "the infiltrant is not radiopaque"),
 'g6_mod16_ri1475': ('mod16', "The infiltrant has a refractive index of 1.475, closer to sound enamel"),
 'g6_mod16_inactive': ('mod16', "in cases of inactive but still visible lesions, in which the surface layer is thick and the lesion is in parts remineralized, the success is often limited"),
 'g6_mod16_fluor': ('mod16', "Due to histological structural similarities between carious white spot lesions and fluorotic enamel, the infiltration procedure can also be used in such cases"),
 'g6_mod16_mih': ('mod16', "the results are less promising, mainly due to differences in histological structure"),
 'g6_mod16_sr': ('mod16', "The evidence is at this moment moderate to low, due to lack of high number of studies"),
 'g6_mod16_notsupersede': ('mod16', "does not supersede the well-established preventive strategies"),
 'g6_mod14_deep': ('mod14', "a previous opening of the surficial enamel layer with a bur is required before the infiltration (deep infiltration)"),
 'g6_sum_barrier': ('sum', "caries infiltration occludes lesion pores with low-viscosity light-curing resins in order to create a diffusion barrier"),
 'g6_sum_radiolucent': ('sum', "the current infiltrant is radiolucent"),
 'g6_stu_infil': ('stu', "infiltration was more effective at preventing lesion progression than instructions on oral hygiene, flossing and fluoride use"),
 'g6_alani_preview': ('alani', "Ethanol (icon-dry) application for 30 s & preview colour change"),
 'g6_alani_repeat': ('alani', "Repeat icon-etch and icon-dry cycles as required"),
 # microabrasion and bleaching
 'g6_sum_micro': ('sum', "Microabrasion is a process in which the tooth surface is subjected to a combination of an acid and an abrasive"),
 'g6_sum_2227': ('sum', "leaving the outer 22 to 27 μm weakened enough"),
 'g6_sum_2030': ('sum', "is applied to the enamel with a rubber cup or stiff bristle brush for 20 to 30 seconds"),
 'g6_sum_lowHCl': ('sum', "suspended in a water-soluble gel containing a low concentration of hydrochloric acid"),
 'g6_sum_fluorosis': ('sum', "fluorosis is often amenable to treatment with microabrasion"),
 'g6_sum_bleachfirst': ('sum', "It is best to bleach first unless the tooth enamel is of a chalky texture"),
 'g6_sum_whitenot': ('sum', "White discolorations are not removed but may be much less noticeable when the surrounding area of the tooth is lightened"),
 'g6_sum_delay': ('sum', "Placement of the restoration should be delayed at least 1 to 2 weeks"),
 'g6_sum_opaque': ('sum', "such as a white spot that could not be removed, then an opaque material is best"),
 'g6_sikri_18': ('sikri', "by an acid (preferably 18% HCl) along with abrasives (pumice powder)"),
 'g6_sikri_60': ('sikri', "Microabrasive agent is applied to the tooth surface for 60 seconds"),
 'g6_sikri_ortho': ('sikri', "Small decalcified lesions, may be due to orthodontic bands"),
 'g6_sikri_contra': ('sikri', "Decalcification areas leading to caries"),
 'g6_sikri_yellow': ('sikri', "teeth sometimes appear more yellow after treatment"),
 'g6_gold_bleachwhite': ('gold21', "Bleaching does not remove white spots"),
 'g6_gold_splotchy': ('gold21', "often develop a “splotchy look” during the first or second week of bleaching"),
 'g6_gold_fluoride_rich': ('gold21', "attempting bleaching first avoids the removal of the fluoride‐rich enamel layer"),
 'g6_gold_unpred': ('gold12', "Localized white spots frequently seen in fluorosis have an unpredictable prognosis"),
 'g6_gold_standout': ('gold12', "in many cases the white spots tend to stand out even more"),
 'g6_gold_hypocaltx': ('gold21', "Treatment can be cosmetic contouring, if the surface layer is not too deep, microabrasion, bonding, or porcelain veneers"),
 # restoration
 'g6_sum_macro': ('sum', "the abrasion can be achieved by applying a fine diamond or carbide finishing bur to the enamel"),
 'g6_mount_ssc': ('mount', "These teeth may be restored with stainless steel crowns"),
 'g6_pick_fig42': ('pick', "after professional application of topical fluoride/CPP"),
 'g6_pick_rinse': ('pick', "for daily (0.05% NaF)/weekly (0.2% NaF) use"),
 'g6_mod_cav': ('mod3', "As soon as the surface zone of the lesion is fractured, it often becomes impossible to remove the bacterial biofilm with common oral hygiene measures, and a restoration is indicated"),
 'g6_mod_smooth': ('mod3', "lesions of smooth surfaces should not be treated in an invasive approach as long as they are not cavitated"),
 'g6_kidd_benefit': ('kidd', "if in doubt about cavitation and whether a filling is needed, give the lesion the benefit of the doubt"),
 'g6_stu_dev': ('stu', "Hypocalcified enamel does not represent a clinical problem except for its potential esthetically objectionable appearance"),
 'g6_kidd_ph': ('kidd', "In the pH range of 5.5–4.5, saliva will be undersaturated with respect to hydroxyapatite"),
 'g6_pick_socio': ('pick', "Social: Socio-economic status?"),
 'g6_det_sharp': ('det', "sharp dental explorer is a more helpful supplementary tool for the evaluation of the surface morphology than a ball-ended probe"),
 'g6_pick_detect': ('pick', "Fibreoptic transillumination UV illumination"),
 'g6_pick_diagnodent': ('pick', "the DiagnoDent laserfluorescence caries detection system"),
 'g6_stu_devacc': ('stu', "their diagnostic accuracy has not been firmly established"),
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
