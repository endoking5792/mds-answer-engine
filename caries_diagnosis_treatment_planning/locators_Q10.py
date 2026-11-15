# Locators for Q10 "Discuss importance of diagnosis and treatment planning in operative dentistry" (20m). All keys prefixed q10_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
O = T + 'Operative_and_Dental_Materials_Textbooks/'
F_EXTRA = {
 # Sturdevant's 2e South Asia Ch.3 (contributors Boushell, Shugars). Offset 19 confirmed at PDF 106 (printed 87) and PDF 112 (printed 93).
 'q10_stu': (O+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ferreira Zandoná and Ritter, 2019'),
 'q10_stu3': (O+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Boushell and Shugars, 2019'),
 # Torres (ed) Modern Operative Dentistry Ch.1 (Torres, Barbe, Noack, Wicht). Offset 14 confirmed at PDF 15 (printed 1) and PDF 44 (printed 30).
 'q10_tor': (O+'Modern_Operative_Dentistry.md', 14, 'Torres et al, 2020'),
 # Summitt's 4th ed Ch.2 (Rose, Haveman, Davis); no printed page numbers in the extract.
 'q10_sum': (O+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Rose, Haveman and Davis, 2013'),
 # Sikri, Textbook of Conservative and Restorative Dentistry Ch.6. Offset 19 confirmed at PDF 114 (printed 95) and PDF 127 (printed 108).
 'q10_sik': (O+'Textbook_of_Conservative_and_Restorative_Dentistry.md', 19, 'Sikri, 2020'),
 # Pickard's Guide to Minimally Invasive Operative Dentistry 10th ed Ch.3. Offset 11 confirmed at PDF 52 (printed 41) and PDF 54 (printed 43).
 'q10_pick': (O+'Pickards_Guide_to_Minimally_Invasive_Operative_Dentistry.md', 11, 'Banerjee and Watson, 2015'),

 # u3 audit 2026-11-14: Pickard's Manual 9e (Banerjee and Watson, OUP 2011) Ch.3 section 3.7.1. Offset 11 confirmed at PDF 52 (printed 41) and, in Ch.2, PDF 38 (printed 27).
 'q10_pic': (O+'Pickards_Manual_of_Operative_Dentistry_9th.md', 11, 'Banerjee and Watson, 2011'),
}
L = {
 # definitions, importance
 'q10_pick_dx': ('q10_pick', 'Diagnosis is the art or act of inferring, from its signs and symptoms or manifestations, the nature or cause of an illness or condition'),
 'q10_pick_prec': ('q10_pick', 'diagnosis precedes treatment in all cases'),
 'q10_pick_prog': ('q10_pick', 'The prognosis is the forecast of the course of a disease or the patient’s response to treatment of the disease'),
 'q10_stu_prog': ('q10_stu3', 'A prognosis may be described as excellent, good, fair, poor, or even hopeless'),
 'q10_stu_tp': ('q10_stu3', 'The treatment plan is a carefully sequenced series of services designed to eliminate or control aetiologic factors, repair existing damage, and create a functional, maintainable environment'),
 'q10_stu_success': ('q10_stu3', 'The success of operative treatment depends heavily on an appropriate plan of care'),
 'q10_stu_dnh': ('q10_stu3', 'primum non nocere'),
 'q10_sum_poor': ('q10_sum', 'Inadequately planned and sequenced treatment, even when well executed, will result in less-than-ideal care'),
 'q10_sik_prior': ('q10_sik', 'Prior to any treatment plan, the operator must arrive at proper diagnosis and the probable prognosis of the disease'),
 'q10_sik_eff': ('q10_sik', 'Efficiency, profitability and also patient’s satisfaction are the results of well-planned procedures'),
 'q10_sik_legal': ('q10_sik', 'Minimizing risk of legal problems'),
 'q10_stu_result': ('q10_stu3', 'Caries lesions are the result of the caries disease process, not the cause'),
 'q10_stu_fp': ('q10_stu3', 'False-positive findings may result in the surgical treatment of a sound tooth'),
 'q10_stu_spec': ('q10_stu3', 'a highly specific test (i.e. few false positives [cell B]) means that fewer healthy teeth will be incorrectly treated'),
 'q10_stu_cycle': ('q10_stu3', 'which leads to larger and more invasive restorations over the course of a patient’s life'),
 'q10_stu_life': ('q10_stu3', 'the average lifespan of a restoration ranges from 5 to more than 15 years'),
 'q10_tor_legal': ('q10_tor', 'The patient file serves as the basis in case of legal disputes'),
 # steps
 'q10_stu_steps': ('q10_stu3', 'Reasons for seeking care Medical and dental histories Clinical examination for the detection of abnormalities Establishing diagnosis Assessing risk Determining prognosis Treatment plan'),
 'q10_stu_cc': ('q10_stu3', 'should be first recorded verbatim'),
 'q10_stu_dxdef': ('q10_stu3', 'which are a determination or judgment of health versus disease'),
 # treatment plan content, factors
 'q10_stu_decide': ('q10_stu3', 'the determination whether a tooth is diseased'),
 'q10_stu_noint': ('q10_stu3', 'One option that must always be included is recommend that there not be any intervention'),
 'q10_stu_risk': ('q10_stu3', 'The treatment plan will also include strategies designed to reduce the patient’s risk for future caries or other oral disease'),
 'q10_stu_f1': ('q10_stu3', 'Patient’s functional, esthetic, and technical demands'),
 'q10_stu_f2': ('q10_stu3', 'Dentist’s knowledge, experience, and training'),
 'q10_stu_f3': ('q10_stu3', 'Dentist–patient compatibility'),
 'q10_stu_f4': ('q10_stu3', 'Availability of specialists'),
 'q10_stu_f5': ('q10_stu3', 'Laboratory support'),
 'q10_stu_dyn': ('q10_stu3', 'a treatment plan is not a static list of services'),
 'q10_sum_models': ('q10_sum', 'Treatment planning is generally accomplished with either a treatment-oriented model or a problem-oriented model'),
 'q10_sum_tunnel': ('q10_sum', 'It is designed to prevent tunnel vision of obvious pathoses'),
 # phases
 'q10_stu_phases': ('q10_stu3', 'urgent phase, II. control phase, III. re-evaluation phase, IV. definitive phase, and V. maintenance phase'),
 'q10_stu_first3': ('q10_stu3', 'For most patients, the first three phases are accomplished simultaneously'),
 'q10_stu_greatest': ('q10_stu3', 'the principle of ‘greatest need’ guides the order in which treatment is sequenced'),
 'q10_stu_pain': ('q10_stu3', 'with pain, bleeding, and swelling at the beginning of the treatment plan and elective esthetic procedures at the end'),
 'q10_stu_urgent': ('q10_stu3', 'A patient presenting with swelling, pain, bleeding, or infection should have these problems managed as soon as possible'),
 'q10_stu_control': ('q10_stu3', 'The goals of this phase are to remove aetiologic factors, eliminate the ecologic niches of pathogens, and stabilize the patient’s dental health'),
 'q10_stu_ctrlex': ('q10_stu3', 'Examples of control phase treatment include extractions, endodontics, periodontal debridement and scaling, occlusal adjustment, caries arrest and/or removal'),
 'q10_stu_reeval': ('q10_stu3', 'allows time between the control and definitive phases for resolution of inflammation and healing'),
 'q10_stu_def': ('q10_stu3', 'The patient’s active disease must be under control, and preventive efforts habitually established, before fixed or removable prosthodontic treatment'),
 'q10_stu_lo': ('q10_stu3', '(e.g. 9–12 months)'),
 'q10_stu_hi': ('q10_stu3', '(e.g. 3–4 months)'),
 'q10_tor_phases': ('q10_tor', 'systemic phase, urgency phase, control phase, re-evaluation phase, definitive phase, and maintenance phase'),
 'q10_tor_asa': ('q10_tor', 'patients can be classified according the American Society of Anesthesiology (ASA)'),
 'q10_tor_esth': ('q10_tor', 'Esthetic problems can also be considered as urgency treatment'),
 'q10_tor_painsd': ('q10_tor', 'patients are not capable to take adequate decisions when they suffer pain'),
 'q10_tor_1y': ('q10_tor', 'A longer interval of approximately 1 year can be recommended for patients with a very low documented risk'),
 'q10_sum_three': ('q10_sum', 'the sequence of treatment within the disease control phase is dictated by three considerations'),
 'q10_sum_quad': ('q10_sum', 'When possible, the restorations should be completed by sextant or quadrant to optimize the use of time'),
 'q10_pick_phases': ('q10_pick', 'It can be divided into phases of therapy (e.g. prevention or control, stabilization or definitive treatment, and review, reassessment, or recall)'),
 'q10_sik_seq1': ('q10_sik', 'Symptomatic relief of pain'),
 'q10_sik_seq2': ('q10_sik', 'Restoration of the tooth with leakage-resistant material'),
 'q10_sik_seq3': ('q10_sik', 'Measures to prevent the recurrence'),
 # interdisciplinary sequencing
 'q10_stu_endo': ('q10_stu3', 'If indicated, teeth should have endodontic treatment before restoration is completed'),
 'q10_stu_perio': ('q10_stu3', 'Generally, periodontal treatment should precede operative care'),
 'q10_stu_qperio': ('q10_stu3', 'A tooth with a questionable periodontal prognosis should not receive an extensive restoration until periodontal treatment provides a more favourable prognosis'),
 'q10_stu_6w': ('q10_stu3', 'minimum of 6 weeks is required after the surgery before final restorative procedures are undertaken'),
 'q10_tor_3m': ('q10_tor', 'A minimum of 3 months and possibly up to 6 months is necessary before initiation of definite prosthetic treatment'),
 'q10_stu_ortho': ('q10_stu3', 'All carious lesions should be corrected with amalgam or composite restorations before the orthodontic treatment begins'),
 'q10_stu_surg': ('q10_stu3', 'impacted, unerupted, and/or hopelessly diseased teeth should be removed before operative treatment'),
 'q10_stu_direct': ('q10_stu3', 'Direct restorations should be completed, if possible, before placing indirect restorations'),
 'q10_tor_rev': ('q10_tor', 'It might be easier to place direct restorations before indirect ones; however it also works in reverse order'),
 # consent
 'q10_stu_consent': ('q10_stu3', 'Informing patients well about their conditions and treatment options and then obtaining their consent has become an integral part of contemporary dental practice'),
 'q10_stu_alt': ('q10_stu3', 'a reasonable alternative often is not to intervene directly with restorative care'),
 # u3 audit 2026-11-14 additions
 'q10_pic_rev': ('q10_pic', 'It ensures that the lead clinician reviews the treatment in the light of all available evidence'),
 'q10_pic_legal': ('q10_pic', 'it may have dento-legal importance and may protect the dentist against unjustified complaints'),
 'q10_pic_piece': ('q10_pic', 'It avoids the risk of disordered and ill-advised treatment, which may arise if treatment is undertaken piecemeal'),
 'q10_sik_phase': ('q10_sik', 'Prioritize emergency phase, disease control phase and'),
 'q10_stu_ctrl2': ('q10_stu3', 'replacement or repair of defective restorations such as those with gingival overhangs, and use of caries control measures'),
 'q10_stu_reev': ('q10_stu3', 'Initial treatment and pulpal responses are'),
 'q10_stu_motiv': ('q10_stu3', 'This phase is used to reinforce home care habits and assess motivation for further treatment'),
 'q10_stu_defin': ('q10_stu3', 'This phase may include endodontic, periodontal, orthodontic, and surgical procedures'),
 'q10_stu_cons2': ('q10_stu3', 'the patient should be informed of the risks associated with each alternative therapy'),
 'q10_stu_cost': ('q10_stu3', 'the cost of treatment alternatives should be discussed with the patient'),
 'q10_stu_nontx': ('q10_stu3', 'the results of possible non-treatment'),
}
