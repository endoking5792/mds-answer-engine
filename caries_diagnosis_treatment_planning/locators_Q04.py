# Locators for Q04 "Discuss in detail the advancements in diagnosis and treatment planning in Conservative Dentistry." (25m). All keys prefixed q04_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
O = T + 'Operative_and_Dental_Materials_Textbooks/'
D = O + 'Detection_and_Assessment_of_Dental_Caries.md'
F_EXTRA = {
 # Sturdevant's 2e South Asia Ch.3 (contributors Boushell, Shugars). Offset 19 confirmed at PDF 106 (printed 87) and PDF 112 (printed 93).
 'q04_stu': (O+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Boushell and Shugars, 2019'),
 # Torres (ed) Modern Operative Dentistry Ch.1 (Torres, Barbe, Noack, Wicht). Offset 14 confirmed at PDF 15 (printed 1) and PDF 44 (printed 30).
 'q04_tor': (O+'Modern_Operative_Dentistry.md', 14, 'Torres et al, 2020'),
 # Summitt's 4th ed Ch.2 (Rose, Haveman, Davis); no printed page numbers in the extract.
 'q04_sum': (O+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Rose, Haveman and Davis, 2013'),
 # Detection and Assessment of Dental Caries: Ch.12 offset 0 (PDF 119=119, 124=124); Ch.23 offset -4 (PDF 223=227, 224=228); Ch.24 offset -5 (PDF 230=235, 231=236).
 'q04_d12': (D, 0, 'Göstemeyer and Schwendicke, 2019'),
 'q04_d23': (D, -4, 'Fontana and Huysmans, 2019'),
 'q04_d24': (D, -5, 'Abrahams, 2019'),
 # Goldstein's Esthetics in Dentistry 3e: Ch.3 (Goldstein and Salama) offset 17 (PDF 66=49, 72=55); Ch.4 (Coachman, Calamita, Ricci) offset 16 (PDF 102=86, 103=87).
 'q04_gol': (O+'Esthetics_in_Dentistry_Goldstein.md', 17, 'Goldstein and Salama, 2018'),
 'q04_dsd': (O+'Esthetics_in_Dentistry_Goldstein.md', 16, 'Coachman, Calamita and Ricci, 2018'),
 # Sikri, Textbook of Conservative and Restorative Dentistry Ch.6. Offset 19 confirmed at PDF 114 (printed 95) and PDF 127 (printed 108).
 'q04_sik': (O+'Textbook_of_Conservative_and_Restorative_Dentistry.md', 19, 'Sikri, 2020'),
 # Pickard's Guide to Minimally Invasive Operative Dentistry 10th ed, Ch.3. Offset 11 confirmed at PDF 52 (printed 41) and PDF 54 (printed 43).
 'q04_pick': (O+'Pickards_Guide_to_Minimally_Invasive_Operative_Dentistry.md', 11, 'Banerjee and Watson, 2015'),
 # Chu, Devigus, Paravina, Mieleszko, Fundamentals of Color 2nd ed (2010) Ch.5; no printed page numbers.
 'q04_sh': (O+'Fundamentals_of_Color_Shade_Matching.md', None, 'Chu et al, 2010'),
}
L = {
 # paradigm: evidence-based, disease not lesion
 'q04_stu_ebd': ('q04_stu', 'conscientious, explicit, and judicious use of current best evidence in making decisions about the care of individual patients'),
 'q04_tor_ebd': ('q04_tor', 'allows the integration among individual clinical quality of the dentist, the patient’s preferences, and the best basis found on scientific researches'),
 'q04_stu_result': ('q04_stu', 'Caries lesions are the result of the caries disease process, not the cause'),
 'q04_d23_dys': ('q04_d23', 'a dysbiosis in the biofilm, driven by exposure to sugars'),
 'q04_d23_pers': ('q04_d23', 'Dentistry has entered an era of personalized care'),
 'q04_pick_dx': ('q04_pick', 'Diagnosis is the art or act of inferring, from its signs and symptoms or manifestations, the nature or cause of an illness or condition'),
 'q04_pick_prec': ('q04_pick', 'diagnosis precedes treatment in all cases'),
 # visual systems and activity
 'q04_stu_expl': ('q04_stu', 'caries is contraindicated as a part of the caries detection process'),
 'q04_stu_cpitn': ('q04_stu', 'Community Periodontal Index of Treatment Needs (CPITN) probe having a 0.5 mm sphere at the tip'),
 'q04_stu_icdas': ('q04_stu', 'The ICDAS uses a two-stage process to record the status of the caries lesion'),
 'q04_stu_06': ('q04_stu', 'The status of the caries severity is determined visually on a scale of 0–6'),
 'q04_stu_cambra': ('q04_stu', 'The Caries Management by Risk Assessment (CAMBRA) movement, as was discussed in Chapter 2, embraces the principles of the ICDAS'),
 'q04_stu_act': ('q04_stu', 'Assessment of dental caries also requires identification of caries lesion activity'),
 'q04_stu_obj': ('q04_stu', 'The objective of improved detection and classification systems is to accurately identify those early enamel lesions that are most likely to be reversed by remineralization'),
 'q04_d23_noval': ('q04_d23', 'there are no evidence-based, validated, reproducible, and accurate diagnostic systems for its measurement'),
 # diagnostic accuracy
 'q04_stu_acc': ('q04_stu', 'none of the available approaches to detecting caries or determining lesion activity is completely accurate'),
 'q04_stu_fp': ('q04_stu', 'a highly specific test (i.e. few false positives [cell B]) means that fewer healthy teeth will be incorrectly treated'),
 'q04_stu_fda': ('q04_stu', 'The technologies currently approved by the FDA include laser-induced fluorescence, light-induced fluorescence, and alternating current (AC) impedance spectroscopy'),
 'q04_stu_lim2': ('q04_stu', 'their diagnostic accuracy has not been firmly established'),
 'q04_stu_soc': ('q04_stu', 'The standard of care for diagnosis of caries remains visual inspection of well-illuminated, clean and dry teeth, with use of radiographs as indicated'),
 # radiographs and digital tools
 'q04_stu_ada': ('q04_stu', 'according to patient condition and risk factors'),
 'q04_tor_over': ('q04_tor', 'a higher frequency of radiographs may lead to overdiagnosis and overtreatment'),
 'q04_d12_cad': ('q04_d12', 'the currently available technology does not provide a more accurate diagnosis than a human observer'),
 'q04_d24_img': ('q04_d24', 'Methods with imaging capability and quantification can more easily be explained to patients'),
 'q04_d24_code': ('q04_d24', 'Non-ionizing diagnostic procedure capable of quantifying, monitoring, and recording changes in structure of enamel, dentin and cementum'),
 'q04_stu_virtual': ('q04_stu', 'The ability to obtain virtual study models via digital impression technology has increased the ease and level of diagnostic evaluation'),
 'q04_tor_cam': ('q04_tor', 'Additionally intraoral camera image and photography are excellent features for documentation'),
 'q04_gol_cbct': ('q04_gol', 'cone beam computed tomography (CBCT) may be performed as part of this examination'),
 'q04_gol_micro': ('q04_gol', 'Both the chairside microscope and intraoral camera provide essential views for precise tooth surface exams'),
 'q04_sh_acc': ('q04_sh', 'computer-assisted shade analysis is more accurate and more consistent compared with human shade assessment'),
 # risk assessment
 'q04_tor_risk': ('q04_tor', 'caries risk assessment is not a standardized process in clinical practice'),
 'q04_tor_cario': ('q04_tor', 'The software Cariogram integrates risk parameters calculating the probability of future lesion development'),
 'q04_tor_cario2': ('q04_tor', 'it was found to be inferior to identify high-risk patients compared with clinical judgment'),
 'q04_d23_subj': ('q04_d23', 'the dentist’s overall subjective impression of the patient might have good predictive power for caries risk'),
 # esthetic / digital planning
 'q04_dsd_def': ('q04_dsd', 'It is an effective digital treatment protocol which utilizes 2D clinical and lab images of the patient and the proposed treatment plan'),
 'q04_dsd_adv': ('q04_dsd', 'it can strengthen esthetic diagnostic abilities, improve the communication between team members'),
 'q04_gol_img': ('q04_gol', 'It increases patient motivation by demonstrating the positive aspects of an improved appearance'),
 'q04_gol_disc': ('q04_gol', 'This picture is for purposes of illustration only. It does not represent a guarantee of any kind.'),
 # treatment-planning models and decisions
 'q04_sum_models': ('q04_sum', 'Treatment planning is generally accomplished with either a treatment-oriented model or a problem-oriented model'),
 'q04_sum_tunnel': ('q04_sum', 'It is designed to prevent tunnel vision of obvious pathoses'),
 'q04_sum_rev': ('q04_sum', 'This process of planning in reverse, starting with the desired end result'),
 'q04_tor_sdm': ('q04_tor', 'Shared decision-making basically aims at achieving mutual agreement about the clinical procedure, diagnostic methods, and therapy of choice'),
 'q04_d23_sdm': ('q04_d23', 'This process of negotiation between clinicians and patients in developing a treatment plan is referred to as shared decision-making'),
 'q04_d23_crit': ('q04_d23', '(a) Lesion cavitation (b) Level of cleansability (c) Lesion activity'),
 'q04_d23_arr': ('q04_d23', 'Arrested caries lesions do not require caries interventions'),
 'q04_d23_nc': ('q04_d23', 'Non-cavitated active lesions should be treated using evidence-based non-restorative methods'),
 'q04_d23_cav': ('q04_d23', 'Most cavitated lesions are non-cleansable, and thus active'),
 'q04_d23_cds': ('q04_d23', 'decision-making will increasingly require decision support and computational systems'),
 'q04_stu_noint': ('q04_stu', 'One option that must always be included is recommend that there not be any intervention'),
 'q04_sik_inc': ('q04_sik', 'Resin infiltration, sealant application'),
 'q04_stu_cycle': ('q04_stu', 'This situation results in what has been termed the cycle of re-restoration'),
 'q04_stu_repair': ('q04_stu', 'recontouring or resurfacing the existing restoration may delay replacement and is an acceptable form of treatment'),
 'q04_stu_sdf': ('q04_stu', 'The cost-effective use of silver diamine fluoride (SDF) to arrest caries'),
 'q04_tor_adh': ('q04_tor', 'modern concepts of adhesive dentistry advocate the unlimited use of direct composite restorations even in endodontically treated teeth'),
 'q04_tor_cad': ('q04_tor', 'The restorations made with CAD/CAM technology are indicated from Class I and II cavities up to single crowns'),
 # phases, recall
 'q04_tor_phases': ('q04_tor', 'systemic phase, urgency phase, control phase, re-evaluation phase, definitive phase, and maintenance phase'),
 'q04_tor_asa': ('q04_tor', 'patients can be classified according the American Society of Anesthesiology (ASA)'),
 'q04_stu_phases': ('q04_stu', 'urgent phase, II. control phase, III. re-evaluation phase, IV. definitive phase, and V. maintenance phase'),
 'q04_pick_phases': ('q04_pick', 'It can be divided into phases of therapy (e.g. prevention or control, stabilization or definitive treatment, and review, reassessment, or recall)'),
 'q04_stu_recall_lo': ('q04_stu', '(e.g. 9–12 months)'),
 'q04_stu_recall_hi': ('q04_stu', '(e.g. 3–4 months)'),
 'q04_stu_consent': ('q04_stu', 'Informing patients well about their conditions and treatment options and then obtaining their consent has become an integral part of contemporary dental practice'),
 'q04_tor_legal': ('q04_tor', 'The patient file serves as the basis in case of legal disputes'),
}
