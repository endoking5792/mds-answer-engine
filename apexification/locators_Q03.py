# Locators for Q03 "Apexification." (10m). All keys prefixed q03_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
F_EXTRA = {
 # AAE Glossary 2012 (8th ed, preface); no printed page numbers in the file.
 'q03_gl': (T+'Glossary_of_Endodontic_Terms_Chapterwise/00_Pages_1_30.md', None, 'American Association of Endodontists, 2012'),
 # Grossman 14e Ch.11; no chapter author named, editor cited (as in root_resorption Q04). Offset 25 confirmed at PDF 223 (printed 198) and PDF 231 (printed 206).
 'q03_gr': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/11_Chapter_11_Vital_Pulp_Therapy_and_Apexification.md', 25, 'Gopikrishna, 2021'),
 # Ingle's 7e Ch.28; author line letter-substituted, decodes to Shahrokh Shabahang (checked against the decoded word Chapter). Offset -106 confirmed at PDF 805 (printed 911) and PDF 813 (printed 919).
 'q03_ing': (T+'Ingles_Endodontics_7th_Chapterwise/28_Chapter_28_Management_of_Teeth_with_Immature_Apices.md', -106, 'Shabahang, 2019'),
 # Torabinejad 6e Ch.10 (Diogenes, Botero and Kang). Offset 7 confirmed at PDF 183 (printed 176) and PDF 194 (printed 187).
 'q03_tor': (T+'Endodontics_Principles_and_Practice_Chapterwise/10_10_Management_of_the_Vital_Pulp_and_of_Immature_Teeth.md', 7, 'Diogenes, Botero and Kang, 2021'),
 # Torabinejad 6e Ch.11 (Paranjpe and Noblett), offset 7 as established in traumatic_dental_injuries (PDF 222 printed 215).
 'q03_tor11': (T+'Endodontics_Principles_and_Practice_Chapterwise/11_11_Management_of_Traumatic_Dental_Injuries.md', 7, 'Paranjpe and Noblett, 2021'),
 # Sikri 2e Ch.25. Offset 21 confirmed at PDF 462 (printed 441) and PDF 477 (printed 456).
 'q03_sik': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/25_25_Vital_Pulp_Therapy.md', 21, 'Sikri, 2019'),
 # Andreasen 4e Ch.22 (M. Cvek). Offset 16 confirmed at PDF 614 (printed 598) and PDF 643 (printed 627).
 'q03_and': (T+'Textbook_and_Color_Atlas_of_Traumatic_Chapterwise/22_22_Endodontic_Management_and_the_Use_of_Calcium_Hydroxide_in.md', 16, 'Cvek, 2007'),
 # Andreasen 4e Ch.23 (L. K. Bakland). Offset 16 confirmed at PDF 674 (printed 658) and PDF 675 (printed 659).
 'q03_bak': (T+'Textbook_and_Color_Atlas_of_Traumatic_Chapterwise/23_23_New_Endodontic_Procedures_using_Mineral_Trioxide_Aggregat.md', 16, 'Bakland, 2007'),
 # Cohen's 12e Ch.21 (Bill Kahler); electronic edition, no printed page numbers.
 'q03_c21': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/21_21_The_role_of_endodontics_after_dental_traumatic_injuries.md', None, 'Kahler, 2021'),
 # Weine 6e Ch.14; no printed page numbers in the file.
 'q03_wei': (T+'Weines_Endodontics_Full_Chapterwise/14_CHAPTER_14_Alternatives_to_Routine_Endodontic_Treatment.md', None, 'Weine, 2004'),
 # Harty's 7e Ch.12 (Sigurdsson and Bourguignon), offset 16 as established (PDF 271 printed 255).
 'q03_har': (T+'Harty_s_Endodontics_in_Clinical_Practice_7th_ed_Chapterwise/12_12_Endodontic_Aspects_of_Traumatic_Injuries.md', 16, 'Sigurdsson and Bourguignon, 2017'),
 # Bioceramics in Endodontics Ch.5 (Tonini and Garo). Offset 32 confirmed at PDF 162 (printed 130) and PDF 165 (printed 133).
 'q03_bio': (T+'Bioceramics_in_Endodontics_Chapterwise/05_Pages_151_180.md', 32, 'Tonini and Garo, 2024'),
}
BOOK_EXTRA = {
 'q03_AAE2012': 'American Association of Endodontists. Glossary of Endodontic Terms. 8th ed. Chicago: AAE; 2012 (edition year from the preface in the file).',
 'q03_Gopikrishna2021': "Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. New Delhi: Wolters Kluwer (India); 2021. Ch.11 Vital pulp therapy and apexification (no individual chapter author is named in the file, so the editor is cited).",
 'q03_Shabahang2019': "Shabahang S. Management of teeth with immature apices. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.28 (author confirmed from the book's Contents page; the chapter's own author line is letter-substituted in the extracted file; publisher and year are not printed in the extracted front matter).",
 'q03_Diogenes2021': 'Diogenes A, Botero T, Kang M. Management of the vital pulp and of immature teeth. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.10.',
 'q03_Paranjpe2021': 'Paranjpe A, Noblett WC. Management of traumatic dental injuries. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.11.',
 'q03_Sikri2019': 'Sikri VK. Vital pulp therapy. In: Essentials of Endodontics. 2nd ed. New Delhi: CBS Publishers; 2019. Ch.25.',
 'q03_Cvek2007': 'Cvek M. Endodontic management and the use of calcium hydroxide in traumatized permanent teeth. In: Andreasen JO, Andreasen FM, Andersson L, editors. Textbook and Color Atlas of Traumatic Injuries to the Teeth. 4th ed. Oxford: Blackwell Munksgaard; 2007. Ch.22.',
 'q03_Bakland2007': 'Bakland LK. New endodontic procedures using mineral trioxide aggregate (MTA) for teeth with traumatic injuries. In: Andreasen JO, Andreasen FM, Andersson L, editors. Textbook and Color Atlas of Traumatic Injuries to the Teeth. 4th ed. Oxford: Blackwell Munksgaard; 2007. Ch.23.',
 'q03_Kahler2021': "Kahler B. The role of endodontics after dental traumatic injuries. In: Berman LH, Hargreaves KM, editors; Rotstein I, web editor. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.21.",
 'q03_Weine2004': 'Weine FS. Endodontic Therapy. 6th ed. St Louis: Mosby; 2004. Ch.14 Alternatives to routine endodontic treatment.',
 'q03_Sigurdsson2017': "Sigurdsson A, Bourguignon C. Endodontic aspects of traumatic injuries. In: Chong BS, editor. Harty's Endodontics in Clinical Practice. 7th ed. Edinburgh: Elsevier; 2017. Ch.12.",
 'q03_Tonini2024': 'Tonini R, Garo M. Bioceramics as an apical plug. In: Chopra V, editor. Bioceramics in Endodontics. 1st ed. John Wiley & Sons; 2024 (copyright line). Ch.5.',
}
L = {
 # definition, aims, indications
 'q03_gl_def': ('q03_gl', 'A method to induce a calcified barrier in a root with an open apex or the continued apical development of an incompletely formed root in teeth with necrotic pulps'),
 'q03_gr_def': ('q03_gr', 'Apexification is defined as a method to induce a calcific barrier across an open apex of an immature, pulpless tooth'),
 'q03_gr_aim': ('q03_gr', 'The aim of apexification is to induce either closure of the open apical third of the root canal or the formation of an apical'),
 'q03_sik_aim1': ('q03_sik', 'Induce the formation of hard tissue barrier across the open apex, allowing proper condensation of obturating material'),
 'q03_sik_aim2': ('q03_sik', 'will not allow the irrigant/filling material to extrude out of the apical foramen'),
 'q03_c21_ind': ('q03_c21', 'Apexification should be performed in teeth with open apices and thin dentinal walls in which standard instrumentation techniques cannot create an apical stop'),
 'q03_c21_wide': ('q03_c21', 'The canal is often wider apically than coronally'),
 'q03_bio_ind': ('q03_bio', 'apex greater than 50–60 ISO in diameter'),
 'q03_tor_vs': ('q03_tor', 'In apexification, no vital pulp tissue is preserved because root canal obturation will occur to the most apical extent of the root'),
 'q03_tor_nodim': ('q03_tor', 'immature teeth treated by apexification do not undergo changes in the root dimension, such as lengthening or thickening of the root dentin'),
 'q03_gr_noroot': ('q03_gr', 'Actual root growth does not occur as a result of apexification'),
 # history and materials
 'q03_tor11_kaiser': ('q03_tor11', 'This method was first introduced by Kaiser in 1964 and made popular by Frank in 1966'),
 'q03_tor11_18': ('q03_tor11', 'incorporates long-term use of calcium hydroxide for up to 18 months'),
 'q03_tor11_wh': ('q03_tor11', 'In 2001 Witherspoon and Ham reported using MTA for single-visit apexification treatment of immature teeth with necrotic pulps'),
 'q03_gr_frank': ('q03_gr', 'the technique was given impetus by the description of three cases of apexification by Frank in 1966'),
 'q03_ing_frank': ('q03_ing', 'proposed placement of a thick paste of calcium hydroxide and CMCP and recommended follow-up evaluations at three- to six-month intervals until closure of the apex'),
 'q03_ing_heith': ('q03_ing', 'He used Pulpdent paste'),
 'q03_ing_heith2': ('q03_ing', 'is visible radiographically in the apical region rather than a well-de,ned apical barrier'),
 'q03_ing_mats': ('q03_ing', 'Various procedures and medicaments have been recommended for apexi,cation including Tricresol and Formalin'),
 'q03_ing_vehic': ('q03_ing', 'iodoform,92 water,93,94 local anesthetic solution, isotonic saline solution, glycerol, and other liquids'),
 'q03_gr_others': ('q03_gr', 'none is as effective in promoting a calcific barrier as calcium hydroxide or MTA'),
 'q03_sik_mats': ('q03_sik', 'a. Calcium hydroxide b. Triple antibiotic paste c. Mineral trioxide aggregate (MTA)'),
 'q03_sik_pulpdent': ('q03_sik', 'calcium hydroxide and methylcellulose (pulpdent), because of better consistency and less solubility, is preferred'),
 'q03_and_cmcp': ('q03_and', 'The addition to calcium hydroxide of toxic antibacterial drugs, such as camphorated parachlorophenol, does not seem to be justified'),
 'q03_c21_ba': ('q03_c21', 'it is prudent to use a calcium hydroxide mixture without the addition of a radiopaquer, such as barium sulfate'),
 'q03_bio_bd': ('q03_bio', 'It can be used for a single visit apexification procedure, does not cause discoloration'),
 'q03_bio_cem': ('q03_bio', 'a calcium-­enriched mixed cement (CEM cement)'),
 # technique (CH)
 'q03_gr_wl': ('q03_gr', 'Working length should be at least 2 mm short of the radiographic apex of the tooth'),
 'q03_c21_naocl': ('q03_c21', 'copious irrigation with 0.5% NaOCl'),
 'q03_c21_lentulo': ('q03_c21', 'a creamy mix of calcium hydroxide (toothpaste thickness) spun into the canal with a Lentulo spiral instrument'),
 'q03_c21_pack': ('q03_c21', 'Calcium hydroxide is packed against the apical soft tissue with a plugger or thick point to initiate hard-tissue formation'),
 'q03_gr_contact': ('q03_gr', 'ensuring that the material is in contact with the periapical tissues'),
 'q03_gr_rmgic': ('q03_gr', 'The access cavity is sealed with RMGIC'),
 'q03_gr_3m': ('q03_gr', 'Ca(OH)2 dressing is changed and patient'),
 'q03_c21_3m': ('q03_c21', 'If no washout is evident, the calcium hydroxide can be left intact for another 3 months'),
 'q03_c21_probe': ('q03_c21', 'When a hard-tissue barrier is indicated radiographically and can be probed with an instrument, the canal is ready for filling'),
 'q03_gr_thermo': ('q03_gr', 'Obturation using thermoplasticized technique'),
 'q03_and_gentle': ('q03_and', 'a thin barrier can be damaged or broken and gutta-percha expelled into the periapical space if excessive pressure is used'),
 # replacement interval: books differ
 'q03_sik_68': ('q03_sik', 'is to be repeated every six to eight weeks for better results'),
 'q03_har_norep': ('q03_har', 'Currently, it is not recommended to replace the mixture if it appears to be intact at these recall appoint'),
 'q03_and_36': ('q03_and', 'After being filled with calcium hydroxide, the teeth should be controlled at 3- to 6-month intervals'),
 'q03_and_5mo': ('q03_and', 'frequent change of calcium hydroxide (ie. more than 5 months between shifts compared to less than 5 months) resulted in more rapid formation of an apical barrier'),
 'q03_ing_noconsensus': ('q03_ing', 'there has been no consensus on the optimal timing to change the dressing material'),
 'q03_wei_6m': ('q03_wei', 'At 6 months the patient is recalled for radiographic examination'),
 # duration: books differ
 'q03_gr_6m4y': ('q03_gr', 'which takes a period of 6 months to 4 years to complete'),
 'q03_gr_2y': ('q03_gr', 'Apexification is usually complete in 6 months, or 2 years at'),
 'q03_ing_3m2y': ('q03_ing', 'Apical barrier formation may take from 3 months to'),
 'q03_tor_39': ('q03_tor', 'Ca(OH)2-mediated apical plug formation requires 3- to 9-month period of treatment'),
 'q03_sik_918': ('q03_sik', 'may take 9 to 18 months for calcific bridge formation'),
 'q03_and_width': ('q03_and', 'Depending on the width of apical foramen and size of the periapical lesion'),
 'q03_sik_aim3': ('q03_sik', 'The procedure should not lead to periapical pathology'),
 'q03_and_618': ('q03_and', 'this may take 6 to 18 months after initial treatment'),
 'q03_har_624': ('q03_har', 'varies between 6 and 24 months with an average of 1 year and 7 months'),
 'q03_c21_318': ('q03_c21', 'takes anywhere from 3 to 18 months with calcium hydroxide'),
 # mechanism
 'q03_and_ph': ('q03_and', 'all related to its high pH = 12.5'),
 'q03_and_bact': ('q03_and', 'elimination of bacteria from the root canal makes healing of the surrounding vital tissue and the formation of an apical hard tissue barrier possible'),
 'q03_and_cem': ('q03_and', 'a reparative or cementum-like hard tissue is formed instead of dentin, indicating involvement of periapical tissues in the barrier formation'),
 'q03_and_loc': ('q03_and', 'The location of the barrier seems to depend on the level at which calcium'),
 'q03_c21_mild': ('q03_c21', 'a mild inflammatory stimulus to initiate healing and a bacteria-free environment to ensure that inflammation is not progressive'),
 'q03_gr_hers': ('q03_gr', 'guided by the reactivated sheath of Hertwig'),
 'q03_gr_disinf': ('q03_gr', 'disinfection of the root canal is indispensable to apical closure'),
 'q03_ing_alp': ('q03_ing', 'high pH of calcium hydroxide may activate alkaline phosphatase activity'),
 'q03_ing_javalet': ('q03_ing', 'plays a more signi,cant role in the induction of root-end closure than the presence of exogenous calcium ions'),
 'q03_ing_dylewski': ('q03_ing', 'a state of repair is observable at the apices characterized by proliferation of connective tissue'),
 # types and nature of barrier
 'q03_ing_frank4a': ('q03_ing', 'An apex that closes with a de,nite though minimal recession of the root canal'),
 'q03_ing_frank4b': ('q03_ing', 'the obliterated apex may develop without any change in the root canal space'),
 'q03_ing_frank4c': ('q03_ing', 'an instrument inserted into the canal encounters a de,nite stop'),
 'q03_ing_frank4d': ('q03_ing', 'a calci,c bridge may form just coronal to the apex that can be visualized radiographically'),
 'q03_wei_5th': ('q03_wei', 'If the fifth condition develops, apexification procedures should be reattempted'),
 'q03_gr_histo': ('q03_gr', 'histologically described variously as bone, dentin, osteodentin, or cementum'),
 'q03_c21_swiss': ('q03_c21', 'giving the barrier a “Swiss cheese” consistency'),
 'q03_ing_porous': ('q03_ing', 'is a porous structure116 that may be permeable to microbial irritants'),
 'q03_c21_short': ('q03_c21', 'Formation of the hard-tissue barrier might be some distance short of the radiographic apex'),
 'q03_and_sites': ('q03_and', 'An apical barrier can be formed around the apex of the tooth, over the apical foramen or in the root canal'),
 # evaluation of success
 'q03_and_succ': ('q03_and', 'has been reported to occur in 79–96% of the treated teeth'),
 'q03_and_589': ('q03_and', 'periapical healing was observed in 92% of 589 teeth, 4 years after permanent filling'),
 'q03_tor_98': ('q03_tor', 'A retrospective study involving 98 teeth treated with apexification showed greater than 90% success'),
 'q03_sik_eval': ('q03_sik', 'There should be no radiographic evidence of external root resorption, root fracture, or breakdown of periradicular supporting tissues'),
 'q03_sik_erupt': ('q03_sik', 'The tooth should continue to erupt, and the alveolus should continue to grow in conjunction with the adjacent teeth'),
 'q03_tor_612': ('q03_tor', 'after 6 and 12 months postoperatively'),
 # drawbacks
 'q03_ing_short1': ('q03_ing', 'Variability in the time required for open apices to close'),
 'q03_ing_short2': ('q03_ing', 'multiple visits necessary to replace and refresh the calcium hydroxide paste'),
 'q03_ing_short3': ('q03_ing', 'potential for coronal leakage and canal re-infection'),
 'q03_ing_1mo': ('q03_ing', 'exposure to calcium hydroxide for periods exceeding one month may result in structural changes in dentin'),
 'q03_and_77': ('q03_and', 'Frequency of cervical fractures fell gradually from 77% in 26 teeth with the lowest degree of root development, to 2% in 362 mature teeth'),
 'q03_and_brittle': ('q03_and', 'may, due to denaturation and dissolution of its protein contents, increase the brittleness of dentin'),
 'q03_c21_30': ('q03_c21', 'approximately 30% of these teeth will fracture during or after endodontic treatment'),
 'q03_c21_dispute': ('q03_c21', 'fracture may be more related to the stage of root development rather than calcium hydroxide use'),
 'q03_sik_lim': ('q03_sik', 'Risk of re-infection; periapical exudate may dissolve'),
 'q03_sik_hers': ('q03_sik', 'calcium hydroxide may damage the Hertwig’s epithelial root sheath'),
 'q03_ing_attr': ('q03_ing', 'Long-term therapy increases the risks of patient attrition'),
 # MTA one-visit in brief
 'q03_gr_mta34': ('q03_gr', 'Material is condensed into a 3–4 mm apical plug'),
 'q03_gr_48h': ('q03_gr', 'Patient is recalled after 48 hours and the set MTA/CSC cement is verified'),
 'q03_gr_1wk': ('q03_gr', 'medicate the canal for'),
 'q03_ing_35': ('q03_ing', '3–5mm (Figure 28-22) to minimize the possibility of future apical leakage'),
 'q03_tor_5mm': ('q03_tor', 'After at least 5 mm of apical plug is established'),
 'q03_bak_4mm': ('q03_bak', 'The recommended size of apical MTA plug is 4mm'),
 'q03_bak_dentin': ('q03_bak', 'MTA does not appear to have a detrimental effect on dentin'),
 'q03_ing_cementum': ('q03_ing', 'a continuous band of cementum formed'),
 'q03_ing_disc': ('q03_ing', 'coronal discoloration in 22.7% of the teeth that were treated'),
 'q03_bio_cost': ('q03_bio', 'high cost, difficult handling, and the risk of post-­treatment dyschromia'),
}
