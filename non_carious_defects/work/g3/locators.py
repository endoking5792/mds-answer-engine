import re, os
T = os.path.expanduser('~/mds-textbooks/Operative_and_Dental_Materials_Textbooks/')
F = {
 'g3_ov': (T+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Overton et al, 2013'),
 'g3_mt': (T+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Matis et al, 2013'),
 'g3_br': (T+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Breschi et al, 2013'),
 'g3_st': (T+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter et al, 2019'),
 'g3_tz': (T+'Modern_Operative_Dentistry.md', 7, 'Torres and Zanatta, 2020'),
 'g3_tz11': (T+'Modern_Operative_Dentistry.md', 9, 'Torres et al, 2020'),
 'g3_mn': (T+'Preservation_and_Restoration_of_Tooth_Structure_Mount.md', 16, 'Mount and Ngo, 2016'),
 'g3_gs': (T+'Esthetics_in_Dentistry_Goldstein.md', 36, 'Goldstein et al, 2018'),
 'g3_nk': (T+'Hybridization_of_Dental_Hard_Tissues.md', 16, 'Nakabayashi and Pashley, 1998'),
}
L = {
 'g3_ov_def': ('g3_ov', 'Class 5 lesions are carious and noncarious defects found in the gingival third of facial and lingual tooth surfaces'),
 'g3_ov_same': ('g3_ov', 'procedures are similar for caries lesions and noncarious lesions, except that carious dentin is removed'),
 'g3_ov_color': ('g3_ov', 'Tooth color is not a good predictor of root caries damage'),
 'g3_ov_soft': ('g3_ov', 'The best correlation to date for clinical detection of caries lesions on root surfaces is the softness of the surface'),
 'g3_ov_skulls': ('g3_ov', 'no NCCLs were found in 3,927 teeth from 259 individuals'),
 'g3_ov_prev': ('g3_ov', 'Prevalence in various patient and population groups ranges from rare to 89%'),
 'g3_ov_48': ('g3_ov', 'Cervical wear was identified in 48% of subjects older than 65 years of age'),
 'g3_ov_multi': ('g3_ov', 'there is overwhelming evidence that the cause is multifactorial'),
 'g3_ov_failure': ('g3_ov', 'progressive loss of tooth structure, (2) tooth sensitivity, (3) the need for endodontic therapy, (4) tooth loss'),
 'g3_ov_fea': ('g3_ov', 'Finite element analysis has predicted that occlusal loads could cause stress fractures or stress corrosion'),
 'g3_ov_shape': ('g3_ov', 'the ability to differentiate etiologies based on lesion shape has yet to be adequately supported with evidence'),
 'g3_ov_1hour': ('g3_ov', 'tooth structure loss as a result of abrasion can be minimized by delaying brushing by at least 1 hour'),
 'g3_ov_nosole': ('g3_ov', 'no authors claim occlusion to be the solitary etiology for NCCLs'),
 'g3_ov_history': ('g3_ov', 'the dentist should obtain a careful health history and provide a thorough dental examination'),
 'g3_ov_firstgoal': ('g3_ov', 'The first goal of any treatment is to remove the causes of the NCCL(s)'),
 'g3_ov_sclerotic': ('g3_ov', 'Because of the sclerotic nature of the tooth structure in a cervical lesion and the physical properties of restorative materials'),
 'g3_ov_shallow': ('g3_ov', 'Shallow lesions that lead to thermal sensitivity or sensitivity to touch should first be treated with bonding resins or desensitizing agents'),
 'g3_ov_active': ('g3_ov', 'if active caries is present, treatment should be initiated to control the active disease'),
 'g3_ov_aod': ('g3_ov', 'Inability to eliminate or greatly reduce the rate of lesion progression through elimination of etiologic factors'),
 'g3_ov_aod2': ('g3_ov', 'Threat to the strength of the tooth and integrity of the coronal-radicular unit'),
 'g3_ov_rerest': ('g3_ov', 'repetitious replacement of lost or defective restorations with increasingly larger ones'),
 'g3_ov_perio': ('g3_ov', 'NCCLs involve exclusively or predominantly the anatomical root of the tooth'),
 'g3_ov_mrc': ('g3_ov', 'If the MRC is apical to the CEJ, then a Class 5 restoration should be accomplished first'),
 'g3_ov_mrc2': ('g3_ov', 'If the MRC is coincident or nearly so with the CEJ, then only root coverage surgery is performed'),
 'g3_ov_short': ('g3_ov', 'Finishing short is almost certainly superior to placing an overhanging restoration'),
 'g3_ov_dam': ('g3_ov', 'While a rubber dam is the ideal method of field isolation and moisture control for all direct-placement restorations'),
 'g3_ov_212': ('g3_ov', 'A no. 212SA clamp is effective for this purpose'),
 'g3_ov_compound': ('g3_ov', 'Modeling compound is the traditional stabilizing material used'),
 'g3_ov_mini': ('g3_ov', 'The incision(s) should not be extended past the mucogingival junction'),
 'g3_ov_gingplasty': ('g3_ov', 'An inadequate zone of attached gingiva is an absolute contraindication for gingivoplasty'),
 'g3_ov_3mm': ('g3_ov', 'If gingivoplasty would result in less than 3 mm of attached gingiva adjacent to the restoration'),
 'g3_ov_attach': ('g3_ov', 'placement of an all-RMGI restoration or an open sandwich restoration with the apical aspect of the restoration restored with RMGI'),
 'g3_ov_48wk': ('g3_ov', 'the restorations should be placed 4 to 8 weeks after surgery'),
 'g3_ov_deas': ('g3_ov', 'the gingival crest height was not fully stable at 6 months'),
 'g3_ov_combined': ('g3_ov', 'A combined surgical-restorative procedure provides better access to the restorative site than a two-step procedure'),
 'g3_ov_box': ('g3_ov', 'Gold foil (direct, not widely used)'),
 'g3_ov_porc': ('g3_ov', 'Porcelain inlay (not widely used)'),
 'g3_ov_amprep': ('g3_ov', 'preparation requires the removal of sound tooth structure to create a box form for amalgam bulk and retention'),
 'g3_ov_1mm': ('g3_ov', 'There is no need to create sharp internal line angles or to remove sound dentin for axial depth greater than 1 mm'),
 'g3_ov_nobevel': ('g3_ov', 'Cavosurface bevels are contraindicated in preparations for amalgam or glass ionomer because of the low edge strength of these materials'),
 'g3_ov_grooves': ('g3_ov', 'grooves should be placed in the dentin of both the occlusal and gingival walls to help retain the amalgam'),
 'g3_ov_trap': ('g3_ov', 'The traditional preparation for a Class 5 direct gold restoration had a trapezoidal outline form'),
 'g3_ov_incr': ('g3_ov', 'incremental resin composite placement is recommended to decrease the effects of polymerization shrinkage'),
 'g3_ov_bevel': ('g3_ov', 'Beveling of enamel margins is recommended when it would expose the ends of the enamel rods'),
 'g3_ov_nocem': ('g3_ov', 'Beveling the gingival margin that ends on cementum is not recommended'),
 'g3_ov_occadj': ('g3_ov', 'there are no controlled clinical trials to verify improved longevity of Class 5 restorations after altering occlusal contacts'),
 'g3_ov_little': ('g3_ov', 'For NCCLs, little or no preparation is required'),
 'g3_ov_rough': ('g3_ov', 'one clinical trial found no increase in retention when sclerotic lesions were roughened with a bur'),
 'g3_ov_etchtime': ('g3_ov', 'this risks overetching dentin'),
 'g3_ov_se': ('g3_ov', 'The current self-etching adhesive systems appear to have inferior bonds to sclerotic dentin'),
 'g3_ov_scrub': ('g3_ov', 'the application of primer or adhesive with an active scrubbing motion when indicated'),
 'g3_ov_2mm': ('g3_ov', 'Resin composite should be placed in increments no thicker than 2 mm'),
 'g3_ov_blade': ('g3_ov', 'careful finishing with a no. 12 or 12B scalpel blade is recommended'),
 'g3_ov_microhyb': ('g3_ov', 'there are no differences in retention rates between microfilled and hybrid resin composites'),
 'g3_ov_flow': ('g3_ov', 'Clinical trials have proven the theoretical to be incorrect'),
 'g3_ov_flowliner': ('g3_ov', 'The use of a flowable resin composite as a liner has not been shown to improve clinical performance'),
 'g3_ov_gic80': ('g3_ov', 'One clinical study reported an 80% retention rate of restorations placed without mechanical retention at 10 years'),
 'g3_ov_gicdeg': ('g3_ov', 'Traditional glass-ionomer materials suffer surface degradation rather rapidly, especially in the presence of acidic foods'),
 'g3_ov_butt': ('g3_ov', 'A 90-degree butt joint approximately 1 mm deep is a reasonable minimum thickness'),
 'g3_ov_franco': ('g3_ov', 'reported that 96.4% of RMGI restorations were retained at 5 years, while only 51.5% of bonded resin composite restorations were retained'),
 'g3_ov_94': ('g3_ov', '94% of Class 5 RMGIs were retained, which exceeded the success of composites (81% to 85%)'),
 'g3_ov_review': ('g3_ov', 'glass-ionomer materials (both conventional and resin-modified) showed the highest retention rates'),
 'g3_ov_sandwich': ('g3_ov', 'Glass ionomer is used to replace the missing dentin, reduce leakage'),
 'g3_ov_veneer': ('g3_ov', 'A veneer of resin composite is placed to enhance esthetics, increase color stability'),
 'g3_ov_96': ('g3_ov', 'a 96% survival rate of sandwich restorations at 5 years'),
 'g3_ov_compomer': ('g3_ov', 'the marginal integrity of compomers has been worse than that of resin composites in long-term clinical trials'),
 'g3_ov_compdbs': ('g3_ov', 'They require the use of a dentin bonding system'),
 'g3_ov_notperm': ('g3_ov', 'The decision to restore should be tempered by the certainty that restorations are not permanent'),
 'g3_mt_75': ('g3_mt', 'About 75% of the US population aged 60 years or older are dentate'),
 'g3_mt_recess': ('g3_mt', '86.5% of people aged 65 years or older'),
 'g3_mt_def': ('g3_mt', 'a soft, irregularly shaped lesion either (1) totally confined to the root surface'),
 'g3_mt_begin': ('g3_mt', 'These lesions generally begin at or slightly occlusal to the free gingival margin'),
 'g3_mt_flow': ('g3_mt', 'salivary flow rate is considered the most important of the nonmicrobial salivary parameters'),
 'g3_mt_01': ('g3_mt', 'an unstimulated flow rate of less than 0.1 mL/min is considered to be below normal'),
 'g3_mt_pilo': ('g3_mt', 'can be extremely effective salivary gland stimulants'),
 'g3_mt_subst': ('g3_mt', 'some commercial products have been found to have the potential to demineralize dentin and should be avoided'),
 'g3_mt_rpd': ('g3_mt', 'The use of removable partial dentures has also been noted as a risk factor in this disease'),
 'g3_mt_coronal': ('g3_mt', 'active coronal caries lesions are 2 to 3.5 times more likely to develop root caries lesions'),
 'g3_mt_texture': ('g3_mt', 'texture to be the best predictor of microbiologic activity in root caries lesions'),
 'g3_mt_explorer': ('g3_mt', 'while offering some resistance to removal of the explorer tip'),
 'g3_mt_bitewing': ('g3_mt', 'Vertical bitewing radiographs permit better evaluation of the proximal root surfaces'),
 'g3_mt_icdas': ('g3_mt', 'International Caries Detection and Assessment System (ICDAS) and includes codes for root caries'),
 'g3_mt_arrest': ('g3_mt', 'root caries lesions can be arrested, obviating restorative therapy'),
 'g3_mt_5000': ('g3_mt', 'an increase in concentration of fluoride in a dentifrice (ie, prescription level or 5,000 ppm)'),
 'g3_mt_chx': ('g3_mt', 'regular rinsing with 0.12% chlorhexidine did not have a substantial effect on reducing root caries'),
 'g3_mt_chxv': ('g3_mt', 'regularly is effective in reducing root caries incidence'),
 'g3_mt_debride': ('g3_mt', 'Accessible, shallow lesions can be made caries-free and easy to clean through debridement with hand instruments'),
 'g3_mt_challenge': ('g3_mt', 'impaired visibility, difficult access, moisture control, pulpal proximity, and the nature of the dentinal substrate itself'),
 'g3_mt_adhesive': ('g3_mt', 'when possible, adhesive fluoride-releasing restorative materials are preferred'),
 'g3_mt_isol': ('g3_mt', 'Isolation is the key to long-term success in root surface restorations'),
 'g3_mt_amxero': ('g3_mt', 'While not recommended for use in xerostomic patients, it may still be the material of choice when isolation is a problem'),
 'g3_mt_comp': ('g3_mt', 'They are primarily indicated in root caries situations in which esthetics is of major importance'),
 'g3_mt_gic': ('g3_mt', 'Glass-ionomer cement is the material of choice for most root caries lesions'),
 'g3_mt_xero': ('g3_mt', 'reasonable success in xerostomic patients'),
 'g3_br_reduced': ('g3_br', 'bonding to sclerotic dentin may be reduced as compared with normal dentin'),
 'g3_br_8yr': ('g3_br', 'at least one clinical study showed equivalent results at 8 years for Class 5 restorations bonded to sclerotic and nonsclerotic dentin'),
 'g3_br_stronger': ('g3_br', 'enhanced performance of the adhesives containing stronger acids when dealing with sclerotic dentin'),
 'g3_br_bur': ('g3_br', 'additional tooth preparation with burs or air abrasion may be beneficial for enhancing the bond'),
 'g3_st_212': ('g3_st', 'Isolation may be achieved by a rubber dam and No. 212 retainer or with a cotton roll and retraction cord'),
 'g3_st_shade': ('g3_st', 'the tooth is typically darker and more opaque in the cervical third'),
 'g3_st_salivary': ('g3_st', 'decreased salivary function'),
 'g3_st_motiv': ('g3_st', 'decreased patient motivation or ability for home care'),
 'g3_st_predom': ('g3_st', 'the use of composite as a restorative material for cervical caries lesions predominates in areas of esthetic concern'),
 'g3_st_sclerotic': ('g3_st', 'Areas of hypermineralized (sclerotic) dentin also may require special attention'),
 'g3_st_bevel': ('g3_st', 'at the cervical margin, bevels are usually not recommended because of the absence of enamel in this area'),
 'g3_st_decide': ('g3_st', 'the operator first must decide, with input from the patient, whether the area needs to be restored'),
 'g3_st_notcar': ('g3_st', '(Most NCCLs are not carious.)'),
 'g3_st_gingiva': ('g3_st', 'If the defect is determined to be contributing to the development of gingival inflammation'),
 'g3_st_pulp': ('g3_st', 'its restoration may be indicated to avoid further defect development that may cause a pulpal exposure'),
 'g3_st_graft': ('g3_st', 'Periodontal therapy with gingival grafts also may be considered as a treatment option'),
 'g3_st_debride': ('g3_st', 'requires only surface debridement of any exposed dentin and roughening/bevelling all enamel margins with a diamond'),
 'g3_st_90': ('g3_st', 'The features of the preparation include a 90-degree cavosurface margin'),
 'g3_st_groove': ('g3_st', 'Groove retention form usually is not necessary but may be used if retention of the restoration is a concern'),
 'g3_st_45': ('g3_st', 'resulting in an angle approximately 45 degrees to the external tooth surface'),
 'g3_st_05': ('g3_st', 'prepared to a width of at least 0.5 mm'),
 'g3_st_incr': ('g3_st', 'The operator should avoid placing increments that connect to both occlusal/incisal walls and gingival walls'),
 'g3_st_comprmgi': ('g3_st', 'Composites and RMGIs are recommended for Class V restorations'),
 'g3_st_gicroot': ('g3_st', 'The restoration of caries lesions on the roots of patients with active caries is the primary indication for the use of a glass ionomer'),
 'g3_st_gicerosion': ('g3_st', 'Cervical defects of idiopathic erosion or abrasion origin (or any combination) also may be indications for restoration with glass ionomers'),
 'g3_st_paa': ('g3_st', 'a mild acid, such as 10% polyacrylic acid'),
 'g3_st_coat': ('g3_st', 'a thin coat of light-activated, resin-based coating is placed on the surface immediately after placement'),
 'g3_st_rmgichoice': ('g3_st', 'RMGI restorative materials are the materials of choice for the restoration of NCCLs where esthetics is not of primary importance'),
 'g3_st_modulus': ('g3_st', 'materials with a low elastic modulus such as micro-filled composite resins and resin-modified glass ionomers have been more successful in restoring NCCLs than stiff materials'),
 'g3_st_stressbreak': ('g3_st', 'can act as stress breakers during tooth flexure, permitting successful restoration with stiffer composite resins'),
 'g3_st_rub': ('g3_st', '92.5% of the restorations in the vigorous rubbing action group were retained'),
 'g3_st_cervident': ('g3_st', 'Cervident had poor clinical results when used to restore NCCLs without mechanical retention'),
 'g3_tz_shallow': ('g3_tz', 'the Class V carious lesions are shallow on the mechanic point of view, but deep on the biological point of view'),
 'g3_tz_small': ('g3_tz', 'if they are small and the etiological factors were identified and controlled, they can stay without being restored'),
 'g3_tz_sclerotic': ('g3_tz', 'They are more resistant to the acid etching, impairing a proper bonding to the restorative material'),
 'g3_tz_roundbur': ('g3_tz', 'a gentle removal of the superficial sclerotic layer with round burs, exposing an underlying less sclerotic substrate'),
 'g3_tz_ageing': ('g3_tz', 'With the population aging associated with the success of the caries disease preventive measures'),
 'g3_tz_212': ('g3_tz', 'the No. 212 or No. 212M retraction clamps should be used'),
 'g3_tz_cord': ('g3_tz', 'an extra fine (size 000) non-impregnated gingival retraction cord is applied into the gingival sulcus'),
 'g3_tz_transsurg': ('g3_tz', 'On those situations, a trans-surgical restoration is indicated'),
 'g3_tz_micro': ('g3_tz', 'The microfilled composites are an excellent option for the cervical restorations'),
 'g3_tz_flow': ('g3_tz', 'The flowable composites also have the same advantages related to the low elastic modulus'),
 'g3_tz_pink': ('g3_tz', 'a gingiva-colored composite can be used'),
 'g3_tz_cementum': ('g3_tz', 'If the gingival margin of the preparation is located on the root surface, no bevel is done on the cementum margin'),
 'g3_tz11_am': ('g3_tz11', 'The amalgam restorations on Class V preparations are indicated on areas where esthetics is not a concern'),
 'g3_mn_site3': ('g3_mn', 'The Site 3 lesion occurs in the gingival one-third of the crown or on the exposed root surface of any tooth'),
 'g3_mn_size0': ('g3_mn', 'There is no equivalent in the Black classification'),
 'g3_mn_cause': ('g3_mn', 'it is desirable to determine the cause and eliminate it at the time of treatment otherwise the tooth loss may continue around the restoration'),
 'g3_mn_superior': ('g3_mn', 'the aesthetic result is very similar to that which can be achieved with composite resin and the adhesion and fluoride release are superior'),
 'g3_mn_noinstr': ('g3_mn', 'No instrumentation is required for the restoration of a corrosion lesion'),
 'g3_mn_paa': ('g3_mn', 'conditioned with 10% polyacrylic acid for 10 seconds'),
 'g3_mn_pumice': ('g3_mn', 'Do not use proprietary prophylaxis pastes'),
 'g3_mn_tca': ('g3_mn', 'Control of gingival seepage and haemorrhage can be achieved with an application of trichloracetic acid'),
 'g3_mn_laminate': ('g3_mn', 'it can be trimmed back with a fine diamond bur under air/water spray to allow for lamination with composite resin'),
 'g3_mn_composite': ('g3_mn', 'If the cavity is to be restored with composite resin, the outline will need to be extended to reach sound, fully mineralized enamel'),
 'g3_gs_occl': ('g3_gs', 'there tends to be relatively high failure rates if the occlusal problems that initiated the lesions are not corrected'),
 'g3_gs_problems': ('g3_gs', 'difficulty in obtaining moisture control, gaining access to subgingival margins, loss of retention, secondary caries, discoloration, and sensitivity'),
 'g3_gs_flap': ('g3_gs', 'a soft tissue graft or coronally positioned flap are possible treatment options for improved esthetics'),
 'g3_gs_splint': ('g3_gs', 'Occlusal adjustment and/or occlusal splints can be used to reduce heavy contacts and bruxism'),
 'g3_gs_abf': ('g3_gs', 'abfraction is unlikely to lead to cervical lesion formation independently'),
 'g3_nk_whit': ('g3_nk', 'with acid-resistant forms of calcium phosphate such as whitlockite'),
 'g3_nk_overetch': ('g3_nk', 'sclerotic dentin is often surrounded by normal dentin that may be overetched by such treatments'),
 'g3_nk_wedge': ('g3_nk', 'in sclerotic cervical root dentin than in artificial'),
 'g3_nk_tags': ('g3_nk', 'short, blunt, funnel-shaped tags containing a core of mineral crystals'),
 'g3_st_rmgiesth': ('g3_st', 'but the long-term esthetic result is compromised'),
 'g3_mt_xyl': ('g3_mt', 'consuming 5 to 10 g of xylitol daily'),
 'g3_ov_facial': ('g3_ov', 'Caries lesions and noncarious lesions are more common on facial surfaces of teeth than on lingual surfaces'),
 'g3_tz_infil': ('g3_tz', 'The caries infiltration technique may also be applied, completely stopping the lesion progression'),
 'g3_mn_replace': ('g3_mn', 'Replacement of the entire original restoration may not be necessary'),
 'g3_ov_expensive': ('g3_ov', 'more expensive and more invasive than direct restorations'),
 'g3_mt_prophy': ('g3_mt', 'a thorough dental prophylaxis should precede any clinical examination of patients at risk for root caries'),
 'g3_mt_gentle': ('g3_mt', 'it is important to conduct the tactile exploration gently'),
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
