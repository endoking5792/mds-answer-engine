import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
F = {
 'g5:basr': (T+'Endodontic_Irrigation_Chemical_disinfection_of_the_root_canal_system_Chapterwise/12_12_Ozone_Application_in_Endodontics.md', 13, 'Mohammadi and Azarpazhooh, 2015'),
 'g5:kish': (T+'Endodontic_Microbiology_2nd_ed_Chapterwise/13_Chapter_13_Topical_Antimicrobials_in_Endodontics.md', 5, 'Kishen, 2017'),
 'g5:beer': (T+'Endodontology_Chapterwise/25_25_Root_Canal_Disinfection.md', 17, 'Baumann and Beer, 2010'),
 'g5:coh8': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/08_8_Cleaning_and_shaping_of_the_root_canal_system.md', None, 'Peters, Peters and Basrani, 2021'),
 'g5:mod': (T+'Operative_and_Dental_Materials_Textbooks/Modern_Operative_Dentistry.md', 6, 'Borges et al, 2020'),
 'g5:sik': (T+'Operative_and_Dental_Materials_Textbooks/Textbook_of_Conservative_and_Restorative_Dentistry.md', 19, 'Sikri, 2020'),
 'g5:bon': (T+'Operative_and_Dental_Materials_Textbooks/A_Clinical_Guide_to_Applied_Dental_Materials.md', None, 'Bonsor and Pearson, 2013'),
 'g5:gold': (T+'Operative_and_Dental_Materials_Textbooks/Esthetics_in_Dentistry_Goldstein.md', 32, 'Caprioglio et al, 2018'),
 'g5:mount': (T+'Operative_and_Dental_Materials_Textbooks/Preservation_and_Restoration_of_Tooth_Structure_Mount.md', 16, 'Fontana et al, 2016'),
 'g5:gw17': (T+'Laser_Textbooks/Lasers_in_Dentistry_Current_Concepts_Coluzzi_Parker.md', 6, 'George and Walsh, 2017'),
 'g5:gw23': (T+'Operative_and_Dental_Materials_Textbooks/Lasers_in_Dentistry_Current_Concepts.md', 8, 'George and Walsh, 2023'),
 'g5:dcna26': ('/Users/niranjan/Library/CloudStorage/OneDrive-Personal/MDS III/DCNA articles/1-s2.0-S0011853225000485.pdf', -44, 'Guruswamy Pandian et al, 2026'),
 'g5:epp14': (T+'Endodontics_Principles_and_Practice_Chapterwise/14_14_Cleaning_and_Shaping.md', 7, 'Peters, Arias and Shabahang, 2021'),
 'g5:coh19': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/19_19_Management_of_endodontic_emergencies.md', None, 'Teixeira and Cheung, 2021'),
 'g5:coh2': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/02_2_Radiographic_interpretation.md', None, 'Nair, Levin and Nair, 2021'),
 'g5:tei17': (T+'Treatment_of_Endodontic_Infections_Chapterwise/17_Chapter_17_Management_of_posttreatment_apical_periodontitis_.md', None, 'Hülsmann, Schäfer and Bürklein, 2022'),
 'g5:epp12': (T+'Endodontics_Principles_and_Practice_Chapterwise/12_12_Root_Canal_Anatomy.md', 7, 'Versiani, Cleghorn and Christie, 2021'),
 'g5:vpt1': (T+'Vital_Pulp_Treatment_Chapterwise/01_Pages_31_60.md', 17, 'Cavalcanti and Chiego, 2024'),
 'g5:renne': (T+'Operative_and_Dental_Materials_Textbooks/3D_Printing_in_Restorative_Dentistry.md', 0, 'Renne and DeFee, 2023'),
 'g5:wat': ('/Users/niranjan/Library/CloudStorage/OneDrive-Personal/MDS III/DCNA articles/1-s2.0-S0011853222034589.pdf', -566, 'Watanabe et al, 2022'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
#   Pick clean text: avoid OCR ligature damage ("0e", "!le"), hyphen breaks and figure captions.
L = {
 'g5_triatomic': ('g5:basr', 'is a triatomic molecule consisting of three oxygen atoms. Its molecular weight is 47.98 g/mol'),
 'g5_soluble': ('g5:basr', 'Ozone is 1.6 times denser and 10 times more soluble in water'),
 'g5_oxidant': ('g5:basr', 'it is the third most potent oxidant after'),
 'g5_halflife': ('g5:basr', 'is an unstable gas that cannot be stored and should be used at once because it has a half-life of 40 min at 20'),
 'g5_hydroxyl': ('g5:basr', 'decomposes to an even more powerful oxidant, the hydroxyl radical'),
 'g5_lightning': ('g5:basr', 'an oxygen/ozone generator simulates lightning via an electrical discharge'),
 'g5_schonbein': ('g5:basr', 'Ozone was discovered by Christian Friedrich Schönbein in 1839'),
 'g5_siemens': ('g5:basr', 'In 1857, Werner von Siemens designed an ozone generator'),
 'g5_forms': ('g5:basr', 'Ozone is applied to oral tissues in the following forms: ozonated water, ozonated olive oil, and oxygen/ozone gas'),
 'g5_trap': ('g5:basr', 'Ozonated water and olive oil have the capacity to trap and then release oxygen/ozone which is an ideal delivery system'),
 'g5_contra': ('g5:basr', 'acute alcohol intoxication, recent myocardial infarction, hemorrhaging from any organ, pregnancy, hyperthyroidism, thrombocytopenia, and ozone allergy'),
 'g5_fisch': ('g5:basr', 'Fisch used ozonated water in dentistry in 1930'),
 'g5_baysan': ('g5:basr', 'ozone exposure for 10–20 s reduced the total levels of'),
 'g5_holmes': ('g5:basr', 'after 18 months, 100 % of PRCLs had improved'),
 'g5_notyet': ('g5:basr', 'However, the clinical application has yet to achieve a strong level of'),
 'g5_bondok': ('g5:basr', 'using ozone gas to disinfect the cavity before placing a restoration there had no'),
 'g5_bondbad': ('g5:basr', 'ozone decreased the microtensile bond strength of a dentin-composite resin interface'),
 'g5_sealant': ('g5:basr', 'pretreatment with ozone improved the marginal sealing ability of the'),
 'g5_endoclin': ('g5:basr', 'is already being used clinically for endodontic treatment'),
 'g5_dh1': ('g5:basr', 'assessed the effect of treatment with gaseous ozone on DH'),
 'g5_dh2': ('g5:basr', 'triple-blinded, randomized controlled clinical trial with two HealOzone machines'),
 'g5_4invitro': ('g5:basr', 'four in vitro studies investigated the bactericidal effect of ozone as compared to 2.5 % sodium hypochlorite'),
 'g5_controv': ('g5:basr', 'The results of this outcome are controversial'),
 'g5_hems': ('g5:basr', 'NaOCl was found to be superior to ozonated water in killing'),
 'g5_gasnone': ('g5:basr', 'while gaseous ozone had no effect on the'),
 'g5_estrela': ('g5:basr', '2 % chlorhexidine and the application of gaseous ozone for 20 min were not'),
 'g5_candida': ('g5:basr', 'however, it showed no residual activity'),
 'g5_endotox': ('g5:basr', 'showed that ozonated water did not neutralize endotoxin'),
 'g5_concl': ('g5:basr', 'Despite the promising in vitro evidence, the clinical application of ozone in dentistry'),
 'g5_rct': ('g5:basr', 'More well-designed and conducted double-blind randomized clinical trials with adequate sample size'),
 'g5_k_singlet': ('g5:kish', 'liberates a reactive form of oxygen, the singlet oxygen'),
 'g5_k_resist': ('g5:kish', 'Ozone presents a broad range of antibacterial efficacy without developing drug resistance'),
 'g5_k_inconsist': ('g5:kish', 'The results of various studies on the efficacy of ozone on endodontic disinfection have been inconsistent'),
 'g5_k_4g': ('g5:kish', 'The ozone gas concentration currently used in endodontics is 4 g/m3'),
 'g5_k_cyto': ('g5:kish', 'shown to be slightly less cytotoxic than NaOCl (2.5%)'),
 'g5_k_aq': ('g5:kish', 'showed essentially no toxicity to oral cells in vitro'),
 'g5_k_biofilm': ('g5:kish', 'but little effect when embedded in a biofilm structure'),
 'g5_k_huth': ('g5:kish', 'depended on the concentration, type of bacterial strains, growth modes of microbes (planktonic or biofilm), and duration of application'),
 'g5_k_oil': ('g5:kish', 'ozone dissolved in oil can be used as an intracanal medicament'),
 'g5_k_barrier': ('g5:kish', 'barrier preventing deeper penetration of the dissolved ozone into the biofilm structure'),
 'g5_k_block': ('g5:kish', 'blockage of water channels in biofilm by the oxidation products of ozone'),
 'g5_k_biocomp': ('g5:kish', 'ozone has been highlighted for its biocompatibility with human oral epithelial cells, gingival fibroblasts, and periodontal cells'),
 'g5_e_hems': ('g5:beer', 'even after 3 minutes of application, ozone has been shown to have no effect against bacteria within a'),
 'g5_e_5naocl': ('g5:beer', 'A 5% sodium hypochlorite solution, on the other hand, was'),
 'g5_e_accel': ('g5:beer', 'even at low potency, is accelerated by ozone'),
 'g5_e_heal': ('g5:beer', 'was developed with particular attention for use in the disinfection of root canals'),
 'g5_e_prereq': ('g5:beer', 'can only be successfully performed with well-shaped access cavities and adequate root canal access'),
 'g5_e_120': ('g5:beer', 'the generator was activated for 120 seconds'),
 'g5_e_cap': ('g5:beer', 'The silicone cap isolates the access cavity, thus creating the necessary vacuum'),
 'g5_c8_spectrum': ('g5:coh8', 'is a powerful and reliable antimicrobial agent against bacteria, fungi, protozoa, and viruses'),
 'g5_c8_mech': ('g5:coh8', 'The mechanism of action is based on the destruction of cell walls and cytoplasmic membranes of bacteria and fungi by the oxidant potential of the ozone'),
 'g5_c8_glyco': ('g5:coh8', 'ozone attacks glycoproteins, glycolipids, and other amino acids and inhibits the enzymatic control system of the cell'),
 'g5_c8_opp': ('g5:coh8', 'In vitro studies showed promising results on their antibacterial effect, clinical results demonstrated the opposite'),
 'g5_c8_hazard': ('g5:coh8', 'The hazards of ozone, when used in endodontics, have not been investigated'),
 'g5_m_air': ('g5:mod', 'The ozone gas can be produced from oxygen in the environment air'),
 'g5_m_cup': ('g5:mod', 'which has a disposable silicone cup tip'),
 'g5_m_neutral': ('g5:mod', 'the ozone gas is suctioned off and again converted into oxygen'),
 'g5_m_addl': ('g5:mod', 'can only be classified as an additional option for controlling dental caries'),
 'g5_m_contact': ('g5:mod', 'the ozone acts on contact'),
 'g5_m_cannot': ('g5:mod', 'These include proximal lesions, hidden caries, or lesions'),
 'g5_m_sealant': ('g5:mod', 'as antimicrobial treatment prior the acid etching and placement of sealants and restorations'),
 'g5_m_limited': ('g5:mod', 'there is only limited information from clinical studies, which are in addition in part contradictory'),
 'g5_m_20120': ('g5:mod', 'directly over the lesion for 20–120 s'),
 'g5_m_repeat': ('g5:mod', 'The ozone application should be repeated after 3 and 6 months'),
 'g5_m_reinf': ('g5:mod', 'Reinfection of the disinfected surface can rapidly occur in the oral cavity'),
 'g5_s_root': ('g5:sik', 'Exposure of the lesion to ozone for 10–40 seconds is effective'),
 'g5_s_2100': ('g5:sik', 'delivers ozone gas at a concentration of approximately 2100 ppm'),
 'g5_s_20120': ('g5:sik', 'The application procedure normally takes between 20 and 120 seconds per tooth surface'),
 'g5_s_remin': ('g5:sik', 'has effectively stimulated remineralization of incipient caries following treatment for a period of 6–8 weeks'),
 'g5_s_doubt': ('g5:sik', 'Efficiency doubtful'),
 'g5_b_tox': ('g5:bon', 'but at levels close to which it has toxicological effects can damage normal tissue'),
 'g5_b_platinum': ('g5:bon', 'The residual gas is then drawn back to the generator and neutralized using a platinum filter'),
 'g5_b_tip': ('g5:bon', 'More recent devices deliver the ozone down a fine tip directly into the canal for very short exposure times'),
 'g5_b_noseal': ('g5:bon', 'This system does not require a seal around the tooth'),
 'g5_g_lysis': ('g5:gold', 'to induce biofilm acid proteins lysis'),
 'g5_g_nodrill': ('g5:gold', 'because the carious dentin is sterilized, it does not need to be removed'),
 'g5_g_uses': ('g5:gold', 'is useful for treating fissure, root, and cervical caries'),
 'g5_g_seal': ('g5:gold', 'hermetic seal must be obtained, and application time ranges from 10 to 60 s'),
 'g5_mt_cochrane': ('g5:mount', 'there is no evidence that ozone therapy can reverse or stop tooth decay'),
 'g5_mt_quest': ('g5:mount', 'However, evidence is still questionable'),
 'g5_gw17_24h': ('g5:gw17', 'After such treatments, fluorescence scores are suppressed and take up to 24 h to recover fully'),
 'g5_gw23_q': ('g5:gw23', 'by quenching fluorescence emissions (such as hydrogen peroxide or ozone)'),
 'g5_d_sr': ('g5:dcna26', 'is not a better disinfecting irrigant than NaOCl and CHX'),
 'g5_d_edta': ('g5:dcna26', 'It can be used as a final irrigant instead of EDTA, since it removes the smear layer'),
 'g5_p_trad': ('g5:epp14', 'Postoperative pain has traditionally been controlled with paracetamol, nonsteroidal antiinflammatory medication, opioids, and/or corticosteroids'),
 'g5_p_cold': ('g5:epp14', 'The authors suggested a final irrigation after cleaning and shaping with cold (2.5°C) sterile saline solution'),
 'g5_p_endovac': ('g5:epp14', 'attached to the Endovac negative pressure irrigation system for 5 minutes'),
 'g5_p_forms': ('g5:epp14', 'different cryotherapy applications have also resulted in lower postoperative pain levels (intracanal, intraoral, and extraoral)'),
 'g5_t_concl': ('g5:coh19', 'cryotherapy reduced the incidence of postoperative pain and the need for medication in patients presenting with a diagnosis of necrotic pulp and symptomatic apical periodontitis'),
 'g5_n_lack': ('g5:coh2', 'Although studies with high level of evidence is lacking in this area, several in vitro studies and case reports have been published'),
 'g5_n_template': ('g5:coh2', 'A template is created by superimposition of CBCT images on intraoral scanned images with sleeves placed in the images for creating a 3D printed guide with a directed sleeve'),
 'g5_n_implant': ('g5:coh2', 'Most often implant treatment planning software is used for the creation of the guide'),
 'g5_n_917': ('g5:coh2', 'showed a higher detection of canal (91.7% vs. 41.7%) using guided approach'),
 'g5_n_surg': ('g5:coh2', 'showed a deviation of 1.743 mm when using guides from the target location identified on preoperative CBCT. Freehand surgery showed a deviation of 2.638 mm'),
 'g5_h_tems': ('g5:tei17', 'targeted endodontic microsurgery (TEMS) using 3D-printed surgical guides has been proposed for optimizing volume and bevel angle of the resection'),
 'g5_v_replica': ('g5:epp12', 'CT-based training replicas produced using 3D printing technology have improved the use of artificial teeth for teaching purposes'),
 'g5_v_destruct': ('g5:epp12', 'produce a large number of teeth for destructive analysis'),
 'g5_cc_scaffold': ('g5:vpt1', 'it is possible to 3D print scaffolds in the desired shape to allow for pulp tissue regeneration'),
 'g5_r_layer': ('g5:renne', 'each layer is microscopically cured at 50 to 100 micrometers thick'),
 'g5_r_glycerin': ('g5:renne', 'Glycerin or Nitrogen act to remove oxygen'),
 'g5_w_layers': ('g5:wat', 'the models are built up by the sequential application of thin layers of material'),
 'g5_w_complex': ('g5:wat', 'The additive technique can save material and express more complex geometries than subtractive methods'),
 'g5_w_sla': ('g5:wat', 'SLA involves a laser that cures light-activated polymers in cross'),
 'g5_w_other': ('g5:wat', 'Other methods of additive manufacture using dental polymers include material jetting, material extrusion, and digital light processing'),
 'g5_w_pbf': ('g5:wat', 'include selective laser sintering, selective laser melting, and electron beam melting'),
 'g5_w_guides': ('g5:wat', 'Guides are commonly printed from a light cure resin with the addition of metal'),
 'g5_w_porous': ('g5:wat', 'additively manufactured metal objects tend to be porous and rough'),
 'g5_k_guinesi': ('g5:kish', 'chemical stability of ozonized oil, and their interaction with root dentin and obturating material'),
 'g5_nagayoshi': ('g5:basr', 'a lower level of cytotoxicity of ozonated water as compared to 2.5 %'),
 'g5_sealer': ('g5:basr', 'ozone therapy improved shear bond strength of two root canal sealers'),
 'g5_embol': ('g5:basr', 'direct intravenous injections of ozone/oxygen gas may produce air embolisms'),
 'g5_c8_care': ('g5:coh8', 'Care should be taken concerning the patient’s and the dentist’s exposure to the gas'),
 'g5_aim': ('g5:mod', 'aiming to prevent or delay the need for a restoration'),
}
def norm(s):
    s = s.replace('\ufb01','fi').replace('\ufb02','fl').replace('\ufb00','ff')
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
