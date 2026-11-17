# Locators for Q02 "Enumerate and classify various Pulpal diseases. Write in detail about Ir-Reversible Pulpitis." (20m),
# Q04 "Transient apical periodontitis." (10m) and Q05 "Periapical pathology and immunologic consideration in endodontics." (10m).
# Keys prefixed q02_, q04_, q05_; source keys likewise (each question declares its own sources).
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
GRO = T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/'
COH = T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/'
ING = T+'Ingles_Endodontics_7th_Chapterwise/'
TOR = T+'Endodontics_Principles_and_Practice_Chapterwise/'
SIK = T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/'
GUL = T+'Endodontics_Kishor_Gulabivala_Yuan_Ling_Ng_4th_Ed_Mosby_2014_Chapterwise/'
GLO = T+'Glossary_of_Endodontic_Terms_Chapterwise/01_Pages_31_52.md'
G4 = GRO+'04_Chapter_4_Diseases_of_the_Dental_Pulp.md'
G5 = GRO+'05_Chapter_5_Diseases_of_the_Periradicular_Tissues.md'
G21 = GRO+'21_Chapter_21_Nonsurgical_Endodontic_Retreatment.md'
C1 = COH+'01_1_Diagnosis.md'
C16 = COH+'16_16_Pathobiology_of_apical_periodontitis.md'
C19 = COH+'19_19_Management_of_endodontic_emergencies.md'
C24 = COH+'24_24_Vital_pulp_therapy.md'
I6 = ING+'06_Chapter_6_Periradicular_Disease.md'
I7 = ING+'07_Chapter_7_Dental_Innervations_and_Pain_of_Pulpal_Origin.md'
I27 = ING+'27_Chapter_27_Vital_Pulp_Therapy.md'
T1 = TOR+'01_1_Pathogenesis_of_Pulp_and_Periapical_Diseases.md'
T9 = TOR+'09_9_Endodontic_Emergencies_and_Therapeutics.md'
S5 = SIK+'05_5_Diseases_of_Dental_Pulp.md'
S6 = SIK+'06_6_Diseases_of_Periradicular_Tissues.md'
G10 = GUL+'10_10_Management_of_acute_emergencies_and_traumatic_dental_inju.md'

F_EXTRA = {}
def _src(prefix, key, path, off, cite):
    F_EXTRA[prefix+key] = (path, off, cite)

# ---------------- source tables (offset confirmed at 2+ pages in THAT chapter, else None) ----------------
for p in ('q02_', 'q04_', 'q05_'):
    # Grossman 14e (ed. Gopikrishna, 2021): no chapter author named in the files, editor cited. Ch.4 offset 25 (PDF 84 printed 59; PDF 86 printed 61; PDF 87 printed 62).
    _src(p, 'gro4', G4, 25, 'Gopikrishna, 2021')
    # Grossman 14e Ch.5: offset 25 (PDF 97 printed 72; PDF 98 printed 73; PDF 99 printed 74; PDF 100 printed 75).
    _src(p, 'gro5', G5, 25, 'Gopikrishna, 2021')
    # Grossman 14e Ch.21: offset 25 (PDF 438 printed 413; PDF 439 printed 414).
    _src(p, 'gro21', G21, 25, 'Gopikrishna, 2021')
    # Cohen's 12e Ch.1 (Berman and Rotstein, from the chapter heading); electronic edition, PDF page only.
    _src(p, 'coh1', C1, None, 'Berman and Rotstein, 2021')
    # Cohen's 12e Ch.16 (Lin and Huang, from the chapter heading); PDF page only.
    _src(p, 'coh16', C16, None, 'Lin and Huang, 2021')
    # Cohen's 12e Ch.19 (Teixeira and Cheung, from the chapter heading); PDF page only.
    _src(p, 'coh19', C19, None, 'Teixeira and Cheung, 2021')
    # Cohen's 12e Ch.24 (Bogen, Dammaschke, Chandler, from the chapter heading); PDF page only.
    _src(p, 'coh24', C24, None, 'Bogen, Dammaschke and Chandler, 2021')
    # Ingle's 7e Ch.6 (author line letter-substituted in the file; decoded as Ricucci, Rocas, Siqueira; verify against the printed book). Printed = PDF + 24 (PDF 171 printed 195; PDF 172 printed 196; PDF 173 printed 197).
    _src(p, 'ing6', I6, -24, 'Ricucci, Rôças and Siqueira, 2019')
    # Ingle's 7e Ch.7 (decoded Ruparel and Khan; verify). Printed = PDF + 24 (PDF 178 printed 202; PDF 179 printed 203; PDF 185 printed 209).
    _src(p, 'ing7', I7, -24, 'Ruparel and Khan, 2019')
    # Ingle's 7e Ch.27 (decoded Bogen and Chandler; verify). Printed = PDF + 100 (PDF 786 printed 886; PDF 787 printed 887; PDF 789 printed 889).
    _src(p, 'ing27', I27, -100, 'Bogen and Chandler, 2019')
    # Torabinejad 6e Ch.1 (Sedgley, Silva, Fouad). Offset 7 (PDF 18 printed 11; PDF 19 printed 12; PDF 20 printed 13).
    _src(p, 'tor1', T1, 7, 'Sedgley, Silva and Fouad, 2021')
    # Torabinejad 6e Ch.9 (Walton and Ruparel). Offset 7 (PDF 173 printed 166; PDF 177 printed 170; PDF 178 printed 171).
    _src(p, 'tor9', T9, 7, 'Walton and Ruparel, 2021')
    # Sikri 2e Ch.5. Offset 21 (PDF 70 printed 49; PDF 74 printed 53; PDF 77 printed 56).
    _src(p, 'sik5', S5, 21, 'Sikri, 2019')
    # Sikri 2e Ch.6. Offset 21 (PDF 84 printed 63; PDF 87 printed 66; PDF 88 printed 67).
    _src(p, 'sik6', S6, 21, 'Sikri, 2019')
    # Gulabivala and Ng 4e Ch.10; no chapter author named in the file. Offset 9 (PDF 280 printed 271; PDF 281 printed 272; PDF 282 printed 273).
    _src(p, 'gul10', G10, 9, 'Gulabivala and Ng, 2014')
    # AAE Glossary 8th ed. (2012); PDF page only.
    _src(p, 'gl', GLO, None, 'American Association of Endodontists, 2012')

BOOK_EXTRA = {}
_BK = {
 'Gopikrishna2021': "Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. New Delhi: Wolters Kluwer (India); 2021. Ch.4 Diseases of the dental pulp; Ch.5 Diseases of the periradicular tissues; Ch.21 Nonsurgical endodontic retreatment (no individual chapter author is named in the files, so the editor is cited).",
 'Berman2021': "Berman LH, Rotstein I. Diagnosis. In: Berman LH, Hargreaves KM, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.1.",
 'Lin2021': "Lin LM, Huang GT-J. Pathobiology of apical periodontitis. In: Berman LH, Hargreaves KM, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.16.",
 'Teixeira2021': "Teixeira FB, Cheung GSP. Management of endodontic emergencies. In: Berman LH, Hargreaves KM, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.19.",
 'Bogen2021': "Bogen G, Dammaschke T, Chandler N. Vital pulp therapy. In: Berman LH, Hargreaves KM, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.24.",
 'Ricucci2019': "Ricucci D, Rôças IN, Siqueira JF Jr. Periradicular disease. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.6 (authors decoded from a letter-substituted heading; verify against the printed book).",
 'Ruparel2019': "Ruparel NB, Khan AA. Dental innervations and pain of pulpal origin. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.7 (authors decoded from a letter-substituted heading; verify against the printed book).",
 'Bogen2019': "Bogen G, Chandler NP. Vital pulp therapy. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.27 (authors decoded from a letter-substituted heading; verify against the printed book).",
 'Sedgley2021': "Sedgley C, Silva R, Fouad AF. Pathogenesis of pulp and periapical diseases. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.1.",
 'Walton2021': "Walton R, Ruparel NB. Endodontic emergencies and therapeutics. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.9.",
 'Sikri2019': "Sikri VK. Essentials of Endodontics. 2nd ed. New Delhi: CBS Publishers; 2019. Ch.5 Diseases of dental pulp; Ch.6 Diseases of periradicular tissues.",
 'Gulabivala2014': "Gulabivala K, Ng YL, editors. Endodontics. 4th ed. Edinburgh: Mosby Elsevier; 2014. Ch.10 Management of acute emergencies and traumatic dental injuries (no chapter author is named in the file, so the editors are cited).",
 'AAE2012': "American Association of Endodontists. Glossary of Endodontic Terms. 8th ed. Chicago: AAE; 2012.",
}
for _p in ('q02_', 'q04_', 'q05_'):
    for _k, _v in _BK.items():
        BOOK_EXTRA[_p+_k] = _v

L = {}
def _loc(prefix, key, src, phrase):
    L[prefix+key] = (prefix+src, phrase)

# =====================================================================================
# Q02 Pulpal diseases and irreversible pulpitis
# =====================================================================================
q = lambda k, s, ph: _loc('q02_', k, s, ph)
q('gro_causes', 'gro4', 'The causes of pulp disease are physical, chemical, and bacterial.')
q('gro_nocorr', 'gro4', 'No correlation exists between histopathologic findings and the existing symptoms.')
q('gro_clinval', 'gro4', 'The value of the clinical classification lies in its use by the clinician to determine the appropriate care and treatment')
q('gro_h1', 'gro4', 'I. INFLAMMATORY DISEASES OF THE PULP')
q('gro_h2', 'gro4', 'C. Chronic Hyperplastic Pulpitis')
q('gro_h3', 'gro4', 'D. Internal Resorption')
q('gro_h4', 'gro4', 'II. PULP DEGENERATION')
q('gro_h5', 'gro4', 'A. Calcific Degeneration')
q('gro_h6', 'gro4', 'B. Fibrous Degeneration')
q('gro_h7', 'gro4', 'III. NECROSIS OF PULP')
q('gro_pulpitis', 'gro4', 'Pulpitis or inflammation of the pulp may be reversible or irreversible, symptomatic (acute) or asymptomatic (chronic), partial or total')
q('gro_def', 'gro4', 'Irreversible pulpitis is a persistent inflammatory condition of the pulp, symptomatic or asymptomatic in nature with the pulp becoming incapable of healing.')
q('gro_cause', 'gro4', 'The most common cause of irreversible pulpitis is bacterial involvement of the pulp through caries')
q('gro_sym1', 'gro4', 'The pain persists for several minutes to hours, lingering after removal of the thermal stimulus.')
q('gro_postural', 'gro4', 'The patient may also complain of postural pain')
q('gro_referred', 'gro4', 'The patient may also have pain referred to adjacent teeth')
q('gro_late', 'gro4', 'In later stages, the pain is more severe and is generally')
q('gro_noct', 'gro4', 'Patients are often kept awake at night by the pain')
q('gro_heat', 'gro4', 'Pain is increased by heat and is sometimes relieved by cold')
q('gro_apabs', 'gro4', 'Apical periodontitis is absent, except in the later stages')
q('gro_perc', 'gro4', 'Results of examination for mobility and percussion and palpation tests are negative.')
q('gro_ept', 'gro4', 'In the early symptomatic stage, less current than what is normal is needed to elicit a response to the electric pulp tester')
q('gro_epta', 'gro4', 'More current is required to elicit a response to the electric pulp test than in a control tooth.')
q('gro_rx', 'gro4', 'Radiographic examination may not show anything of significance that is not already known clinically.')
q('gro_dd', 'gro4', 'whereas in irreversible pulpitis, the pain lingers after the stimulus is removed, or it can occur spontaneously.')
q('gro_ddabs', 'gro4', 'swelling, tenderness on palpation, tenderness on percussion, mobility of the tooth, and lack of response to pulp-vitality tests')
q('gro_loc', 'gro4', 'Once discomfort increases, the patient loses the ability to identify a particular tooth in the quadrant.')
q('gro_heatloc', 'gro4', 'the application of heat with a consequent abnormal response is indicative of irreversible pulpitis in that tooth')
q('gro_hist1', 'gro4', 'These necrotic areas attract polymorphonuclear leukocytes by chemotaxis and start an acute inflammatory reaction.')
q('gro_hist2', 'gro4', 'The lysosomal enzymes lyse some of the pulp stroma')
q('gro_hist3', 'gro4', 'The pulp, trying to protect itself, walls off the areas of the microabscesses with fibrous connective tissue.')
q('gro_hist4', 'gro4', 'One then sees an area of ulceration (chronic ulcerative pulpitis) that drains through the carious exposure into the oral cavity and reduces the intrapulpal pressure')
q('gro_rx_tx', 'gro4', 'Treatment consists of complete removal of the pulp or pulpectomy.')
q('gro_pulpotomy', 'gro4', 'the removal of the coronal pulp or pulpotomy should be performed as an emergency procedure')
q('gro_extract', 'gro4', 'Surgical removal should be considered if the tooth is not restorable.')
q('gro_prog', 'gro4', 'The prognosis of the tooth is favorable if the pulp is removed and if the tooth undergoes proper endodontic therapy')
q('gro_necro', 'gro4', 'Irreversible pulpitis progresses to necrosis')
q('gro_confine', 'gro4', 'the pulp is entirely enclosed in a hard, unyielding dentinal wall, except at the apical foramen')
q('coh_normal', 'coh1', 'This is a clinical diagnostic category in which the pulp is symptom-free and normally responsive to pulp testing.')
q('coh_pulpitis', 'coh1', 'This is a clinical and histologic term denoting inflammation of the dental pulp, clinically described as reversible or irreversible')
q('coh_aae', 'coh1', 'The terminology and classifications that follow are based on those suggested by the American Association of Endodontists in 2016.')
q('coh_corr', 'coh1', 'making a correlation between clinical signs and symptoms and the histopathology of a given clinical condition is challenging')
q('coh_nec', 'coh1', 'This is a clinical diagnostic category indicating death of the dental pulp.')
q('coh_prev', 'coh1', 'This is a clinical diagnostic category indicating that the tooth has been endodontically treated')
q('coh_init', 'coh1', 'This is a clinical diagnostic category indicating that the tooth has been previously treated by partial endodontic therapy')
q('coh_sym', 'coh1', 'Teeth that are classified as having symptomatic irreversible pulpitis exhibit intermittent or spontaneous pain.')
q('coh_def', 'coh1', 'indicating that the vital inflamed pulp is incapable of healing')
q('coh_symrx', 'coh1', 'Typically, there are minimal or no changes in the radiographic appearance of the periradicular bone.')
q('coh_symrx2', 'coh1', 'With advanced irreversible pulpitis, a thickening of the periodontal ligament may become apparent on the radiograph')
q('coh_hx', 'coh1', 'patients should be questioned about a history of orthodontic treatment')
q('coh_ga', 'coh1', 'should be questioned regarding past general anesthesia or endotracheal intubation procedures')
q('coh_asym', 'coh1', 'However, the patient does not complain of any symptoms.')
q('coh_asym2', 'coh1', 'endodontic treatment should be performed as soon as possible')
q('coh_necnext', 'coh1', 'Typically, when symptomatic irreversible pulpitis remains untreated, the pulp will eventually become necrotic.')
q('gl_pulpitis', 'gl', 'clinically described as reversible or irreversible and histologically described as acute, chronic or hyperplastic.')
q('gl_asym', 'gl', 'no clinical symptoms but inflammation produced by caries, caries excavation, trauma')
q('gl_sym', 'gl', 'lingering thermal pain, spontaneous pain, referred pain')
q('sik_noclass', 'sik5', 'There is no definite and accepted classification for pulpal diseases.')
q('sik_basis', 'sik5', 'duration and severity of inflammation (acute, subacute, chronic)')
q('sik_who', 'sik5', 'Classification by World Health Organization (WHO)')
q('sik_who2', 'sik5', 'Hyperplastic (pulp polyp)')
q('sik_gro', 'sik5', 'Grossman’s classification')
q('sik_hyper', 'sik5', 'Hyperemia is an initial and potentially reversible pulpal response')
q('sik_abbot', 'sik5', 'Necrobiosis (part of pulp is necrotic and inflamed; rest is irreversibly inflamed)')
q('sik_portal1', 'sik5', 'Direct extension through the dentinal tubules')
q('sik_portal2', 'sik5', 'Extension by process of anachoresis')
q('sik_1mm', 'sik5', 'bacteria needed to be within 1.0 mm of the pulp before inflammatory changes could be observed')
q('sik_perc', 'sik5', 'The tooth can be tender on percussion, indicating spread of inflammation to periapical areas')
q('sik_crack', 'sik5', 'pain on percussion may also indicate crack in the tooth')
q('sik_chron', 'sik5', 'however, pain is less severe and intermittent than continuous as in acute case')
q('sik_local', 'sik5', 'The local inflammation results in increased tissue pressure in inflamed area and not the entire pulp cavity.')
q('tor1_lack', 'tor1', 'the dental pulp lacks collateral circulation and is confined within rigid dentinal walls')
q('tor1_trans', 'tor1', 'the inflammation changes from reversible')
q('tor1_irr', 'tor1', 'characterized histologically by the presence of areas of severe inflammation and partial necrosis in the pulp')
q('tor1_rest', 'tor1', 'The rest of the pulp tissue typically has mild inflammation or no inflammation and therefore, is responsive to clinical vitality testing.')
q('tor1_wall', 'tor1', 'intense inflammatory response that is attempting to wall off the microbial infection')
q('tor1_pain', 'tor1', 'Because the association of pain with irreversible pulpitis is not consistent')
q('tor1_med', 'tor1', 'These mediators include prostaglandins, neuropeptides, bradykinin, cytokines, chemokines, and matrix metalloproteinases.')
q('tor1_40', 'tor1', 'In about 40% of cases, irreversible pulpitis develops into pulp necrosis without symptoms.')
q('tor1_polyp', 'tor1', 'cases with internal resorption, with a vital (responsive) pulp')
q('ing6_focus', 'ing6', 'constitutes the point of transition from a reversible to an irreversible')
q('ing6_zones', 'ing6', 'the layers necrosis')
q('ing7_ling', 'ing7', 'promotes the process of spontaneous pain or lingering pain')
q('tor9_pain', 'tor9', 'removal of the inflamed tissue will usually reduce the pain')
q('tor9_cs', 'tor9', 'Complete cleaning and shaping of the root canals are the preferred treatments if time permits.')
q('tor9_pulpot', 'tor9', 'pulpotomy or a partial pulpectomy on the largest canals (palatal or distal root of molars) is performed')
q('tor9_90', 'tor9', 'Both procedures have demonstrated greater than 90% success rate in reducing postoperative pain')
q('tor9_partial', 'tor9', 'partial pulpectomy, but not pulpotomy of severely inflamed teeth, upregulates inflammatory mediators')
q('tor9_cotton', 'tor9', 'A dry cotton pellet alone is as effective in relieving pain as a pellet moistened with camphorated monochlorophenol')
q('tor9_anes', 'tor9', 'periodontal, intrapulpal, or intraosseous injection techniques are indicated')
q('tor9_antib', 'tor9', 'Postoperative pain is attributed in large part to a process called central sensitization.')
q('coh24_diag', 'coh24', 'An irreversible pulpitis is diagnosed on the (enhanced) positive sensibility test, on radiating irritant-persistent pain or lingering pain, pain on heat')
q('coh24_asym', 'coh24', 'However, irreversible pulpitis may be asymptomatic.')
q('coh24_false', 'coh24', 'with 10% to 16% of results being false')
q('coh24_irr', 'coh24', 'the healing of the pulp tissue cannot be achieved predictably after removal of the triggering stimulus')
q('coh24_csc', 'coh24', 'full pulpotomies in adult teeth diagnosed with irreversible pulpitis and demonstrating radiographic periapical rarefaction have been treated successfully')
q('coh24_normal', 'coh24', 'Teeth that present with irreversible pulpitis and experience carious pulp exposures are normally treated with pulpectomy and orthograde root canal treatment')
q('coh24_alt', 'coh24', 'Pulpotomy in permanent teeth using CSC materials can be recommended as a minimally invasive alternative to traditional root canal treatment.')
q('coh24_bleed', 'coh24', 'Pulps with profuse and lingering hemorrhaging had a significantly poorer outcome')
q('ing27_fav', 'ing27', 'showing favorable outcomes in teeth exhibiting irreversible pulpitis')
q('ing27_cem', 'ing27', 'showed similar outcomes to conventional root canal treatment in a multicenter randomized clinical trial')
q('coh19_abx', 'coh19', 'Antibiotics are not recommended for the emergency management of irreversible pulpitis')

# =====================================================================================
# Q04 Transient apical periodontitis
# =====================================================================================
q = lambda k, s, ph: _loc('q04_', k, s, ph)
q('gro_def', 'gro5', 'Primary symptomatic apical periodontitis is a painful inflammation of the periodontium as a result of trauma, irritation, or infection through the root canal')
q('gro_vital', 'gro5', 'Primary symptomatic apical periodontitis may occur in a')
q('gro_occ', 'gro5', 'Abnormal occlusal contacts')
q('gro_restn', 'gro5', 'Recently inserted restoration extending beyond the')
q('gro_wedge', 'gro5', 'Wedging of a foreign object between the teeth, such as')
q('gro_blow', 'gro5', 'Traumatic blow to the teeth')
q('gro_iat1', 'gro5', 'Root canal instrumentation forcing bacteria or debris inadvertently through the apical foramen')
q('gro_iat2', 'gro5', 'Forcing of irritating irrigants or medicaments through the apical foramen')
q('gro_iat3', 'gro5', 'Extension of obturating material through the apical foramen to impinge on periradicular tissues')
q('gro_iat4', 'gro5', 'Overinstrumentation during shaping and cleaning of root canals')
q('gro_sym', 'gro5', 'The tooth may feel extruded and the patient may have')
q('gro_perc', 'gro5', 'Pain on percussion is the classical diagnostic feature of primary symptomatic apical periodontitis.')
q('gro_dd', 'gro5', 'Absence of a periradicular radiolucency: Primary symptomatic')
q('gro_ddabs', 'gro5', 'extreme clinical symptoms of swelling and pain that is associated with the breakdown of periradicular tissue')
q('gro_sterile', 'gro5', 'The pulp and periradicular tissues may be sterile if periodontitis is due to a blow, occlusal trauma, or chemical or mechanical irritation')
q('gro_hist', 'gro5', 'an accumulation of serous exudate distends the periodontal ligament and extrudes the tooth slightly')
q('gro_hist2', 'gro5', 'If the irritation is severe and continued, osteoclasts may become active')
q('gro_tx', 'gro5', 'Treatment of primary symptomatic apical periodon')
q('gro_tx2', 'gro5', 'Adjustment of high points (in hyperocclusion cases) and')
q('gro_prog', 'gro5', 'The occurrence of symptoms of primary symptomatic apical periodontitis during endodontic treatment in no way affects the ultimate outcome of the treatment.')
q('gro21_trans', 'gro21', 'Symptoms of postendodontic discomfort are usually attributed to occlusal disturbances and transient apical periodontal inflammation.')
q('gro21_dur', 'gro21', 'Discomfort following endodontic treatment is usually present for a very short duration (few days to a week)')
q('gl_tab', 'gl', 'transient apical breakdown—A response to tooth luxation consisting of radiographic apical bone and root resorption that resolves spontaneously')
q('sik_def', 'sik6', 'Acute apical periodontitis is the inflammation of the periodontium as a result of trauma, bacterial infection initiating from within the root canal space')
q('sik_sep', 'sik6', 'use of separators during restorative and orthodontic procedures, rubber dam application etc.')
q('sik_vital', 'sik6', 'whereas, acute apical periodontitis caused by an abnormal occlusal contact responds normally to the pulp vitality tests.')
q('sik_rx', 'sik6', 'The Lamina dura remains intact without any break in continuity, especially in case of vital pulps.')
q('sik_tx', 'sik6', 'Determining the cause and relieving the patient\'s acute symptoms accordingly is the line of treatment.')
q('sik_prog', 'sik6', 'Prognosis is usually favorable.')
q('tor1_occ', 'tor1', 'if the occlusion on the tooth is inadvertently left high, the tooth is rendered tender to percussion')
q('tor1_rev', 'tor1', 'the occlusion needs to be adjusted, and the pulpal condition is considered reversible')
q('tor9_noRF', 'tor9', 'no definitive treatment risk factors have been identified')
q('tor9_post24', 'tor9', 'most reports show that the pain tends to occur in the first 24 hours')
q('tor9_over', 'tor9', 'overextension associated with the highest incidence of discomfort')
q('tor9_react', 'tor9', 'Reassurance (the “Big R”) is the most important aspect of treatment.')
q('tor9_abx', 'tor9', 'This practice has been demonstrated to be not useful and needlessly exposes the patient to expensive, potentially dangerous drugs')
q('tor9_nsaid', 'tor9', 'certain NSAIDs have been shown to reduce postendodontic treatment pain')
q('tor9_vital', 'tor9', 'it is important to check that the temporary restoration is not in traumatic occlusion')
q('coh16_allo', 'coh16', 'which results from mechanical allodynia and hyperalgesia')
q('coh16_rx', 'coh16', 'Radiographic examination usually does not show periapical bone destruction of the involved tooth in acute apical periodontitis')
q('coh16_out', 'coh16', 'restitution of normal periapical tissues if irritants are immediately eliminated by root canal therapy')
q('coh16_prog', 'coh16', 'progression to chronic apical inflammation if irritants continue to persist')
q('coh19_occ1', 'coh19', 'occlusal reduction has not been shown to be beneficial')
q('coh19_occ2', 'coh19', 'occlusal reduction has been reported to reduce posttreatment pain')
q('gul_occ', 'gul10', 'The authors do not recommend it as a routine procedure.')
q('gul_occ2', 'gul10', 'Occlusal reduction works when there had been previous presence of percussion sensitivity')
q('gul_tx', 'gul10', 'without inflicting further insult to the apical tissues by over-instrumentation or extrusion')
q('ing6_pain', 'ing6', 'compression of nerve endings seems to be more')
q('ing6_sap', 'ing6', 'Symptomatic apical periodontitis is characterized by acute')
q('coh1_sap', 'coh1', 'This condition is defined as an inflammation, usually of the apical periodontium, producing clinical symptoms including a painful response to biting or percussion or palpation.')

# =====================================================================================
# Q05 Periapical pathology and immunologic considerations
# =====================================================================================
q = lambda k, s, ph: _loc('q05_', k, s, ph)
q('tor1_pdl', 'tor1', 'these tissues are not capable of mounting an immune response that can stop the advancing microbial ingress')
q('tor1_bone', 'tor1', 'the hallmark of apical periodontitis is bone resorption to accommodate the formation of a soft tissue lesion')
q('tor1_innate', 'tor1', 'is primarily coordinated by innate rather than adaptive immune responses')
q('tor1_adapt', 'tor1', 'adaptive responses were found to be critical in preventing disseminated infections')
q('tor1_cyt', 'tor1', 'Important cytokines in bone resorption include IL-1, IL-6, IL-11, IL-17, and')
q('tor1_lim', 'tor1', 'Cytokines that limit bone resorption include IL-4 and IL-10.')
q('tor1_rankl', 'tor1', 'RANKL binds to its receptor (RANK), resulting in osteoclast differentiation.')
q('tor1_opg', 'tor1', 'This interaction is inhibited by osteoprotegerin (OPG), a decoy protein that binds to the receptor.')
q('tor1_peak', 'tor1', 'Levels of RANKL and the ratio of RANKL to OPG both peak at 2 to 3 weeks')
q('tor1_treg', 'tor1', 'T-reg lymphocytes have been shown to control the size of periapical lesions in a significant manner.')
q('tor1_gran', 'tor1', 'A granuloma has a collection of inflammatory cells, such as lymphocytes, plasma cells, macrophages, and mast cells')
q('tor1_cyst', 'tor1', 'A periapical cyst arises in a part of a granuloma')
q('tor1_equal', 'tor1', 'both can heal equally well after surgical or nonsurgical treatment')
q('tor1_abs', 'tor1', 'An apical abscess is characterized histologically by the presence of an intense inflammatory response surrounding areas of tissue necrosis.')
q('tor1_pers', 'tor1', 'about 50% of cases with persistent disease after endodontic treatment may have bacterial presence in the lesion')
q('tor1_exac', 'tor1', 'an increase in virulent strains, an increase in microbial load, or a disruption of the host response')
q('ing6_class', 'ing6', 'periradicular lesions are basically divided into three main clinical groups')
q('ing6_hist', 'ing6', 'is based on the presence or absence of epithelial cells and the distribution and type of')
q('ing6_double', 'ing6', 'immune response to tissue injury is a double-edged sword.')
q('ing6_acute1', 'ing6', 'initially combated by local host defenses represented by resident macrophages and the complement system')
q('ing6_mac', 'ing6', 'Activated macrophages increase the production of pro-')
q('ing6_comp', 'ing6', 'Some products of complement activation, such as C3a and C5a, can stimulate mast cells to degranulate and release histamine')
q('ing6_pmn', 'ing6', 'leukocytes to migrate to the injured area.')
q('ing6_pmn2', 'ing6', 'Abscess formation is the extreme form of tissue injury caused by PMNs in response to bacterial infection.')
q('ing6_chronic', 'ing6', 'develops as an adaptive immune response to the chronic antigenic stimulation egressing from the infected root canal')
q('ing6_ln', 'ing6', 'antigens must be taken to regional lymph nodes where recognition and lymphocyte activation can occur')
q('ing6_eff', 'ing6', 'plasma cells, originated from B cells, which secrete antibodies')
q('ing6_cells', 'ing6', 'are lymphocytes and plasma cells, followed by mononuclear phagocytes (macrophages and dendritic cells) and neutrophils.')
q('ing6_cyt', 'ing6', 'Cytokines, such as IL-1α and β')
q('ing6_ratio', 'ing6', 'Pathologic bone resorption typical of apical periodontitis is associated with increased RANKL/OPG ratio.')
q('ing6_th1', 'ing6', 'is involved in the phases of lesion expansion as a result of bone destruction')
q('ing6_th2', 'ing6', 'TH2 response, mostly mediated by cytokines IL-4, IL-5, IL-5, IL-10, and transforming growth factor (TGF)-β, exert an important role in the healing process')
q('ing6_th17', 'ing6', 'seem to play a dominant role in exacerbating')
q('ing6_treg', 'ing6', 'Both TH1 and')
q('ing6_epi', 'ing6', 'Factors that may stimulate epithelial proliferation include the epidermal growth factor')
q('coh16_innate', 'coh16', 'Acute apical periodontitis is an immediate defense reaction to irritants and does not require exquisite specificity and memory.')
q('coh16_chronic', 'coh16', 'Chronic apical periodontitis is a form of adaptive immune response that requires exquisite specificity and memory.')
q('coh16_prr', 'coh16', 'the PRRs of the innate immune system recognize PAMPs')
q('coh16_tlr4', 'coh16', 'TLR4/CD14 is the receptor for the gram-negative bacterial LPS.')
q('coh16_burst', 'coh16', 'the well-known respiratory burst')
q('coh16_mast', 'coh16', 'mast cells are the designated triggers of acute inflammation')
q('coh16_pmn', 'coh16', 'Polymorphonuclear neutrophilic leukocytes (PMNs) are the principal effector cells in acute apical periodontitis.')
q('coh16_th', 'coh16', 'TH1 cells develop from TH0 activated by IL-12 and IFN-γ')
q('coh16_ab', 'coh16', 'plasma cells isolated from periapical lesions secrete antibodies specific for the particular bacteria found in the adjacent root canal system')
q('coh16_b', 'coh16', 'B cells, but not T cells, played a pivotal role in preventing dissemination of endodontic infection')
q('coh16_tdef', 'coh16', 'T-cell deficiency appears to accelerate bone loss at the early phase of apical periodontitis lesions')
q('coh16_neuro', 'coh16', 'This phenomenon is termed neurogenic inflammation.')
q('coh16_good', 'coh16', 'Chronic inflammation is good news and bad news.')
q('coh16_bad', 'coh16', 'the host response is inadequate to eliminate these factors')
q('coh16_fb', 'coh16', 'Foreign materials such as root canal filling materials, paper points, cotton fibers, and surgical sutures can trigger a foreign body giant cell granuloma.')
q('coh16_ost', 'coh16', 'During the chronic stage of apical periodontitis, both osteoclast and osteoblast activity decrease')
q('coh16_dc', 'coh16', 'Activated dendritic cells produce IL-12, which is a key inducer of cell-mediated immunity.')
q('coh16_dmg', 'coh16', 'Tissue damage can also occur in acute inflammation by release of lysosomal enzymes, toxic oxygen radicals')
q('coh16_out', 'coh16', 'restitution of normal periapical tissues if irritants are immediately eliminated by root canal therapy')

# ---- additions after first draft ----
_loc('q04_', 'gro_asym', 'gro5', 'in which the tooth has no pain on percussion and has distinct radiographic periradicular bone changes')
_loc('q04_', 'gro_ddsec', 'gro5', 'Presence of a periradicular radiolucency: Secondary symptomatic')
_loc('q04_', 'sik_noswell', 'sik6', 'Delayed vitality tests • No swelling')
_loc('q04_', 'sik_elev', 'sik6', 'Tooth may be slightly elevated from its socket')
_loc('q02_', 'sik_who3', 'sik5', 'Formation of secondary/irregular dentin in pulp')
_loc('q02_', 'sik_equate', 'sik5', 'categorized as symptomatic (acute) or asymptomatic (chronic)')
_loc('q02_', 'gro_asymptom', 'gro4', 'In the asymptomatic stage of irreversible pulpitis, the exposed pulp exhibits little or no pain')
_loc('q02_', 'gro_insp', 'gro4', 'Inspection generally discloses a deep cavity extending to the pulp or decay under a filling')
_loc('q05_', 'ing6_ox', 'ing6', 'due to release of oxygen radicals and')
_loc('q05_', 'ing6_il8', 'ing6', 'the chemokine IL-8/CXCL8')
