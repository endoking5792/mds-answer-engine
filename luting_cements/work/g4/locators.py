import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')   # clone of the private textbook repo
C = T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/'
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
F = {
 'c11': (T+'Operative_and_Dental_Materials_Textbooks/Restorative_Dental_Materials_Craig_Michigan_11th.md', 9, 'Craig and Powers, 2002'),
 'c11b': (T+'Operative_and_Dental_Materials_Textbooks/Restorative_Dental_Materials_Craig_Michigan_11th.md', 10, 'Craig and Powers, 2002'),
 'c14': (T+'Operative_and_Dental_Materials_Textbooks/Craigs_Restorative_Dental_Materials.md', 11, 'Sakaguchi et al, 2019'),
 'phi': (T+'Operative_and_Dental_Materials_Textbooks/Phillips_Science_of_Dental_Materials.md', 16, 'Anusavice et al, undated'),
 'mcc': (T+'Operative_and_Dental_Materials_Textbooks/Applied_Dental_Materials_McCabe_Walls_9th.md', 9, 'McCabe and Walls, 2008'),
 'pw': (T+'Operative_and_Dental_Materials_Textbooks/Powers_Wataha_Dental_Materials_Properties_and_Manipulation.md', 12, 'Powers and Wataha, 2013'),
 'bp': (T+'Operative_and_Dental_Materials_Textbooks/A_Clinical_Guide_to_Applied_Dental_Materials.md', None, 'Bonsor and Pearson, 2013'),
 'sk': (T+'Operative_and_Dental_Materials_Textbooks/Indirect_Restorations_Sikri.md', None, 'Sikri, 2017'),
 'mz': (T+'Operative_and_Dental_Materials_Textbooks/Operative_Dentistry_Marzouk.md', None, 'Marzouk et al, undated'),
 'fj': (T+'Endodontics_Principles_and_Practice_Chapterwise/15_15_Obturation_and_Temporization.md', 7, 'Flake and Johnson, 2021'),
 'baba': (T+'Endodontic_Prognosis_Clinical_Guide_Chapterwise/10_10_Restoration_of_Endodontically_Treated_Teeth.md', 7, 'Baba et al, 2017'),
 'coh11': (C+'11_11_Periradicular_surgery.md', None, 'Johnson et al, 2021'),
 'coh14': (C+'14_14_Pulp_reactions_to_caries_and_dental_procedures.md', None, 'Fouad and Levin, 2021'),
 'coh24': (C+'24_24_Vital_pulp_therapy.md', None, 'Bogen et al, 2021'),
 'vpt': (T+'Vital_Pulp_Treatment_Chapterwise/03_Pages_91_120.md', 19, 'Dammaschke, 2024'),
 'par': (T+'The_Art_and_Science_of_Contemporary_Surgical_Endodontics_Mahmoud_2_Chapterwise/11_Chapter_11_Root_End_Filling_Materials.md', 13, 'Parirokh and Shabahang, 2017'),
 'gro': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/22_Chapter_22_Endodontic_Surgery.md', 25, 'Gopikrishna, 2021'),
 'cas': (T+'Advances_in_Surgical_Endodontics_Chapterwise/00_Pages_1_16.md', None, 'Castellucci, 2003'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
#   Pick clean text: avoid OCR ligature damage ("0e", "!le"), hyphen breaks and figure captions.
L = {
 # ---- Q4 temporary cements
 'c14_provdef': ('c14', 'Provisional (temporary) cements are indicated for fixation of temporary restorations'),
 'c14_lowstr': ('c14', 'provisional cements must have a relatively low strength and be easily handled'),
 'c14_pulp': ('c14', 'In addition, they must not irritate the pulp'),
 'c14_examples': ('c14', 'Examples of temporary luting agents are zinc oxide-eugenol (ZOE) and noneugenol cements and calcium hydroxide pastes'),
 'bp_soft': ('bp', 'It is soft for easy removal, as failure to remove all the cement will compromise the gingival health'),
 'bp_strong': ('bp', 'It is strong enough to hold the restoration in situ until the fit appointment'),
 'bp_notrely': ('bp', 'They should not be relied on to retain the temporary prosthesis if the preparation has inadequate retention'),
 'c11_spec35': ('c11', 'A maximum value of 35 MPa is required for cements intended for temporary cementation'),
 'c11_film40': ('c11', 'not more than 40 pm for cements used for temporary cementation'),
 'c11_disint': ('c11', 'A maximum value of 2.5% is acceptable for provisional cementing materials'),
 'c11_typeIV': ('c11', 'Type IV Cavity liners'),
 'phi_types': ('phi', 'four types of ZOE cements by clinical application'),
 'phi_types2': ('phi', 'temporary fillings and thermal insulating bases; and (IV) intermediate fillings'),
 'c11_compo': ('c11', 'The powder is mainly zinc oxide, with added white rosin to reduce the brittleness of the set cement'),
 'c11_setting': ('c11', 'The setting of ZOE cements is a chelation reaction in which an amorphous, zinc eugenolate is formed'),
 'c11_moist': ('c11', 'the presence of moisture is essential for setting to occur'),
 'phi_seal': ('phi', 'They seal the dentinal tubules surprisingly well against the ingress of oral fluids'),
 'phi_fewweeks': ('phi', 'Temporary ZOE restorations are expected to last a few weeks at most'),
 'phi_year': ('phi', 'tency, it serves effectively as an intermediate restorative'),
 'phi_never': ('phi', 'ZOE cements should never be used for temporary cementation of final fixed prostheses'),
 'mcc_zoe20': ('mcc', 'typically 20 MPa for unreinforced materials and 40 MPa for reinforced materials'),
 'mcc_hydro': ('mcc', 'Leached eugenol is replaced by water which, under certain conditions, can cause hydrolysis of the zinc eugenolate'),
 'mcc_templute': ('mcc', 'therefore, not suitable for luting applications except on a temporary basis'),
 'coh11_irm': ('coh11', 'IRM consists of a powder containing greater than 75% zinc oxide and approximately 20% polymethacrylate'),
 'coh11_irmliq': ('coh11', 'a liquid that contains greater than 99% eugenol and less than 1% acetic acid'),
 'bp_irm': ('bp', 'IRM (Intermediate Restorative Material) (Dentsply) is indicated for longer-term temporization'),
 'bp_irmwear': ('bp', 'It also has high wear resistance and so temporized teeth can be maintained in the correct occlusal relationship'),
 'c11_neoil': ('c11', 'The non-eugenol-zinc oxide cements typically contain an aromatic oil and zinc oxide'),
 'c11_nesens': ('c11', 'These cements are suitable for patients sensitive to eugenol'),
 'c11_neacrylic': ('c11', 'The non-eugenol cements, however, do not soften provisional acrylic crowns'),
 'c11_neadhere': ('c11', 'do not adhere as well to preformed metal crowns as the eugenol-containing cements, and they are slower setting'),
 'c14_nearyl': ('c14', 'Noneugenol materials use long-chain aliphatic acids or aryl-substituted butyric acid to react with zinc oxide particles'),
 'bp_neEBA': ('bp', 'The base consists of zinc oxide mineral oils and the catalyst ortho-ethoxybenzoic acid'),
 'phi_carbox': ('phi', 'various types of carboxylic acids have been used to replace eugenol'),
 'bp_modifier': ('bp', 'The purpose of this paste is to further soften the cement to facilitate removal of the temporary restoration'),
 'c14_resinprov': ('c14', 'They are useful for cementation of interim restorations in the esthetic zone of the mouth because they are tooth colored'),
 'c14_resinstr': ('c14', '25 to 70 MPa and 180 to 265 MPa, respectively'),
 'pw_resin': ('pw', 'Temporary resin cements eliminate the problem of potential contamination of teeth by eugenol'),
 'pw_resincomp': ('pw', 'Temporary resin cements are formulated from dimethacrylate resin and radiopaque glass filler, and most are self-cured'),
 'pw_4to8': ('pw', 'must be cemented for 4 to 8 weeks until the permanent restoration is ready'),
 'pw_longer': ('pw', 'For longer-term fillings, modified zinc oxide-eugenol, hybrid ionomer, or zinc polycarboxylate cements can be used'),
 'pw_cotton': ('pw', 'Several cotton fibers may be added to the mix'),
 'baba_zoe': ('baba', 'cements such as zinc oxide eugenol (ZOE) be used only for periods of up to 1 or 2 weeks'),
 'baba_longer': ('baba', 'Glass ionomers, Zinc Phosphate, Polycarboxylate, or resin-modified glass ionomers (RMGIs) exhibit acceptable seals against dentin'),
 'baba_caso4': ('baba', 'Soft self-cured calcium sulfate-based temporary filling materials tend to be easily abraded, unstable over time, and absorb moisture'),
 'baba_leak': ('baba', 'none of the provisional materials examined using microbial markers prevented coronal leakage when tested for 30 days'),
 'fj_cavit': ('fj', 'Cavit contains zinc oxide, calcium sulfate, zinc sulfate, glycol acetate, polyvinyl acetate resin'),
 'fj_hygro': ('fj', 'The calcium sulfate is hydrophilic, causing the hydroscopic expansion of the material'),
 'fj_35': ('fj', 'A depth of at least 3.5 mm of Cavit is needed to adequately seal an access preparation'),
 'fj_term': ('fj', 'is a composite resin interim restorative material for endodontics'),
 'bp_putty': ('bp', 'The basic setting reaction is the hydration of calcium sulphate to form a plaster, gypsum'),
 'bp_puttywear': ('bp', 'Their wear resistance is poor but they create a good seal'),
 'bp_lcmonth': ('bp', 'should not remain in the oral cavity for more than a month because it slowly degrades and wears'),
 'sk_cavitfilm': ('sk', 'Non-satisfactory for luting purposes (film thickness is 91 p)'),
 'c14_scavenger': ('c14', 'Eugenol is considered a free-radical scavenger'),
 'c14_100': ('c14', 'composite mechanical properties were reduced up to a 100'),
 'c14_clean': ('c14', 'bond strength to dentin is not adversely affected if the surface is thoroughly cleaned prior to adhesive application'),
 'c14_debond': ('c14', 'increasing the risk of debonding, or even fracture in case of low-strength, silica-based ceramics'),
 'bp_neuse': ('bp', 'If resin composite is to be used as the definitive bonding agent or a resin-containing luting cement'),
 'bp_silicone': ('bp', 'If an addition silicone impression material is to be used after the cement has been used'),
 'bp_allergy': ('bp', 'If the patient has an allergy or sensitivity to eugenol'),
 'c11_clinical': ('c11', 'a cement with a compressive strength of 15 to 24 MPa was the most appropriate cement'),
 'sk_seal': ('sk', 'A temporary restoration must seal and insulate the prepared tooth surface from the oral environment to prevent any irritation to the pulp'),
 'sk_occl': ('sk', 'It should maintain proper contact with adjacent and opposing teeth to avoid extrusion and/or drifting'),
 'bp_nonhard': ('bp', 'Non-hardening temporary cements are also available'),
 'c14_neutral': ('c14', 'ZOE cements are considered biocompatible because of their neutral pH, antibacterial action, and anodyne effect'),
 'bp_tempbond': ('bp', 'A zinc oxide eugenol-containing temporary cement (TempBond, Kerr Hawe)'),
 'mcc_adhesive': ('mcc', 'if a provisional restoration is luted using a zinc oxide eugenol temporary cement'),
 'bp_clear': ('bp', 'Availability as a clear cement'),
 'bp_trial': ('bp', 'be used for trial cementation of definitive indirect restorations to assess the aesthetics and occlusion'),
 'mcc_amlining': ('mcc', 'The materials form a suitable cavity lining for amalgam condensation'),
 'par_draw': ('par', 'long setting time, high cost, discoloration potential, and handling difficulties'),
 'coh11_mtasup': ('coh11', 'In vitro sealing ability and biocompatibility studies comparing root-end filling materials have shown MTA to be superior'),
 'phi_pulpotomy': ('phi', 'as a dressing after vital pulp'),
 'sk_ch': ('sk', 'The calcium hydroxide preparation is preferred as interim restoration where composite is to be used as final restoration'),
 # ---- Q7 calcium hydroxide
 'c11_liner': ('c11', 'Cavity liners are suspensions of calcium hydroxide in an organic liquid such as methyl ethyl ketone or ethyl alcohol'),
 'c11_nostr': ('c11', 'cavity liners neither possess mechanical strength nor provide any significant thermal insulation'),
 'mcc_friable': ('mcc', 'form a very friable cavity lining which is easily fractured'),
 'mcc_8': ('mcc', 'the compressive strength remains very low at about 8 MPa'),
 'c14_base': ('c14', 'The base paste of a typical product contains calcium tungstate, tribasic calcium phosphate, and zinc oxide powders'),
 'c14_catalyst': ('c14', 'The catalyst paste contains calcium hydroxide, zinc oxide, and zinc stearate powders in ethylene toluene sulfonamide liquid'),
 'c14_disal': ('c14', 'The ingredients responsible for setting are calcium hydroxide and a salicylate, which react to form an amorphous calcium disalicylate'),
 'c14_lc': ('c14', 'A light-cured calcium hydroxide liner consists of calcium hydroxide and barium sulfate dispersed in a urethane dimethacrylate resin'),
 'mcc_ca50': ('mcc', 'Calcium hydroxide (50%)'),
 'mcc_gs40': ('mcc', 'Glycol salicylate (40%)'),
 'mcc_zinc': ('mcc', 'is thought that zinc ions are primarily responsible for chelation, with calcium being largely unreacted'),
 'mcc_hema': ('mcc', 'The purpose of the HEMA is to produce a relatively hydrophilic polymer which can absorb water and release calcium hydroxide'),
 'mcc_moist': ('mcc', 'Moisture has a dramatic effect on the rate of setting'),
 'mcc_ch20': ('mcc', 'about 20 MPa. This strength is gained rapidly'),
 'c14_settime': ('c14', 'Although setting times vary between 2.5 and 5.5 minutes, strength of these cements continues to increase over a 24-hour period'),
 'c14_cs': ('c14', 'compressive strengths ranged from 6.5 to 14.3 MPa at 10 minutes to from 9.8 to 26.8 MPa at 24 hours'),
 'c14_pH': ('c14', 'The pH of commercial products has been measured at between 9.2 and 11.7'),
 'c14_free': ('c14', 'Free calcium hydroxide in excess of that necessary to form the calcium disalicylate stimulates secondary dentin'),
 'pw_pH': ('pw', 'The pH of the cements is basic and varies from 11 to 12'),
 'pw_set': ('pw', 'Setting times vary from 2 to 7 minutes'),
 'pw_noint': ('pw', 'It does not interfere with the polymerization of these materials'),
 'c11_sol': ('c11', 'values ranged from 0.4% to 7.8% in distilled water'),
 'c11_disappear': ('c11', 'Over a long term, some calcium hydroxide products seem to'),
 'c11_05': ('c11', 'A thickness greater than 0.5 mm is not suggested'),
 'c11_amalgam': ('c11', 'considered strong enough to support the forces of condensation of amalgam'),
 'c11_lcpH': ('c11', 'One light-cured calcium hydroxide base is reported to have a surface pH of 11.9'),
 'c11_lcab': ('c11', 'Whereas two-paste calcium hydroxide bases show antibacterial activity, a light-cured type did not'),
 'c11b_necrosis': ('c11b', 'The initial response of exposed pulpal tissue to the highly alkaline aqueous pulp-capping agents is necrosis to a depth of 1 mm or more'),
 'c11b_dystrophic': ('c11b', 'the necrotic zone undergoes dystrophic calcification, which appears to be a stimulus for dentin bridge formation'),
 'c11b_resinbest': ('c11b', 'Resin-containing calcium hydroxide pulp capping agents are the most effective liners now available for treating pulp exposures'),
 'c11b_lessirr': ('c11b', 'these calcium hydroxide compounds become less irritating and are able to stimulate reparative dentin bridge formation more quickly'),
 'c11b_gap': ('c11b', 'some of these materials evidently break down with time and create a gap between the restoration and the cavity wall'),
 'mcc_leach': ('mcc', 'Calcium hydroxide is readily leached out, generating an alkaline environment in the area surrounding the cement'),
 'mcc_tgf': ('mcc', 'possibly mediated by the activation of TGF'),
 'mcc_calcium': ('mcc', 'Calcium from the cement does not become bound into the mineralized tissues'),
 'mcc_pull': ('mcc', 'this can pull the calcium hydroxide material away from the tooth, leaving a void'),
 'mcc_overlaid': ('mcc', 'In pulp capping procedures the calcium hydroxide material is generally overlaid with a strong cement base material'),
 'mz_ca45': ('mz', 'calcium ions in calcium hydroxide are not utilized in the calcification of the bridge'),
 'mz_basic': ('mz', 'basicity cannot be entirely responsible for their favorable effect'),
 'coh14_liberate': ('coh14', 'the high pH of this material can act to liberate bioactive molecules from dentin'),
 'coh14_tgf': ('coh14', 'and adrenomedullin are liberated by both calcium hydroxide and MTA'),
 'vpt_hermann': ('vpt', 'introduced calcium hydroxide as an agent for maintaining pulp vitality'),
 'vpt_lowOH': ('vpt', 'these preparations show a lower release of hydroxyl ions, resulting in a lower pH value and a significantly weaker antimicrobial effect'),
 'vpt_seal': ('vpt', 'hard-setting calcium hydroxide cements offer a better seal of the dentine-pulp complex'),
 'vpt_dissolve': ('vpt', 'hard-setting calcium salicylate ester cement dissolves under the overlaying restoration in the long term'),
 'vpt_tunnel': ('vpt', 'Tunnel defects have been demonstrated in the hard tissue formed after direct pulp capping with calcium hydroxide'),
 'vpt_notrec': ('vpt', 'hard-setting calcium hydroxide cement cannot be recommended as a first-choice agent for direct pulp capping'),
 'coh24_drawbacks': ('coh24', 'weak marginal adaptation to dentin, degradation and dissolution over time, and resorption in primary teeth'),
 'coh24_tunnel': ('coh24', 'Tunnel defects have also been demonstrated in hard tissue barriers generated over pulp wounds'),
 'coh24_rates': ('coh24', 'Successful outcomes were 80.1% after 1 year and 68% after 5 years; this diminished to 58.7% after a 9-year observation period'),
 'coh24_lc': ('coh24', 'These materials do not have sufficient mechanical strength despite their composite content, and specific CH effects are minimal'),
 'coh24_notrec': ('coh24', 'hard setting CH cements based on calcium salicylate esters cannot be recommended'),
 'phi_carbonate': ('phi', 'Eventually, the calcium hydroxide forms calcium carbonate and becomes inactive'),
 'phi_margin': ('phi', 'Calcium hydroxide is soluble in water and must not be left on the margin of the prepared cavity'),
 'c14_notgeneral': ('c14', 'but not for general lining of an entire pulpal flow'),
 'c14_rmgi': ('c14', 'RMGI liners are a better choice for general lining of cavities'),
 'c14_mta': ('c14', 'studies have shown that it produces a more ideal outcome as a pulp-capping agent than calcium hydroxide'),
 'c14_indirect': ('c14', 'The antibacterial action of calcium hydroxide makes these cements useful in indirect pulp-capping procedures involving carious dentin'),
 # ---- Q8 Super EBA
 'c11_eba7030': ('c11', 'A typical EBA-alumina-reinforced ZOE cement contains 70% zinc oxide and 30% alumina by weight in the powder'),
 'c11_eba625': ('c11', 'contains 62.5% ortho-EBA by weight and 37.5% eugenol by weight'),
 'c11_crystal': ('c11', 'its presence allows some crystalline zinc eugenolate to form, which provides additional strength'),
 'c11_strop': ('c11', 'kneaded for 30 seconds, and then stropped for 60 seconds to develop a creamy consistency'),
 'c11_glass': ('c11', 'A glass slab is recommended for mixing the EBA-alumina-modified cements'),
 'c11_perm': ('c11', 'The use of EBA-alumina-modified ZOE cements has been clinically successful for the permanent cementation of crowns and bridges'),
 'c11_film': ('c11', 'a film thickness of 25 to 35 pm is readily obtained'),
 'c11_provdisint': ('c11', 'despite their low solubility in water, disintegrated and wore excessively in the mouth'),
 'c14_21': ('c14', 'the liquid is a mixture of 2-ethoxybenzoic acid (EBA) and eugenol, roughly in a 2:1 proportion'),
 'c14_61': ('c14', 'allows for the use of very high powder-to-liquid ratios (6:1)'),
 'c14_72': ('c14', '72 MPa vs. 26 MPa, in compression at room temperature'),
 'c14_weakest': ('c14', 'both reinforced ZOE cements are the weakest among luting agents used for permanent cementation'),
 'c14_hydrol': ('c14', 'zinc 2-ethoxybenzoate matrix formed in EBA-eugenol cements is even more prone to hydrolysis than the zinc eugenolate'),
 'c14_92': ('c14', 'alumina cement showed a success rate of 92% after 2.5 years'),
 'mcc_quartz': ('mcc', 'Quartz (approximately 35%)'),
 'mcc_zno60': ('mcc', 'Zinc oxide (approximately 60%)'),
 'mcc_85': ('mcc', 'A typical commercial product has an ultimate compressive strength of around 85 MPa'),
 'mcc_lowersol': ('mcc', 'produces a cement with lower solubility than that observed for zinc oxide/eugenol products'),
 'mcc_lute': ('mcc', 'although they are primarily used as luting cements'),
 'bp_77': ('bp', 'A higher powder to liquid ratio can be used (up to 7:1)'),
 'bp_crystal': ('bp', 'EBA forms a crystalline form of zinc eugenolate which is stronger and less soluble'),
 'sk_solinc': ('sk', 'Solubility and disintegration also increases'),
 'coh11_comp': ('coh11', 'Super-EBA consists of a powder containing 60% zinc oxide, 34% aluminum oxide, and 6% natural resins'),
 'coh11_methoxy': ('coh11', 'a liquid that contains 37.5% eugenol and 62.5% o-methoxybenzoic acid'),
 'coh11_fast': ('coh11', 'Super-EBA is available in two forms, fast set and regular set'),
 'coh11_acid': ('coh11', 'has been shown to disintegrate over time in an acid pH environment'),
 'coh11_noregen': ('coh11', 'it has no capacity to regenerate cementum'),
 'coh11_persist': ('coh11', 'The incidence of persistent disease after endodontic surgery in which Super-EBA was used as a root-end filling material ranges from 4% to 20%'),
 'coh11_leaky': ('coh11', 'sealing effects similar to those of IRM and is less leaky than amalgam'),
 'par_methoxy': ('par', 'liquid: eugenol, o-methoxybenzoic acid'),
 'par_survey': ('par', 'MTA is the most popular root-end filling material (61.4%), followed by SuperEBA (34.3%)'),
 'par_choice': ('par', 'MTA is currently the material of choice for root-end filling'),
 'cas_putty': ('cas', 'The Super EBA cement is mixed to a putty consistency, shaped into a narrow cone'),
 'cas_props': ('cas', 'They are easy to manipulate, have adequate working time, dimensionally stable, biocompatible, unaffected by moisture, bacteriostatic, radiopaque'),
 'gro_alt': ('gro', 'IRM and SuperEBA are other commonly recommended'),
 'pw_22': ('pw', 'The working time of the EBA-alumina cements is long (about 22 minutes), unless moisture is present on the slab'),
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
