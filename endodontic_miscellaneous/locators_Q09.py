# Locators for Q09 "Hertwigs epithelial root sheath." (5m), Q10 "Haemostatic agents." (5m), Q11 "Xerostomia." (5m).
# Keys prefixed q09_, q10_, q11_. Source keys likewise (each question declares its own sources).
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
F_EXTRA = {
 # ---- Q09 ----
 # Grossman 14e (ed. Gopikrishna, 2021) Ch.1; no chapter author named, editor cited. Offset 25 confirmed at PDF 35 (printed 10) and PDF 52 (printed 27).
 'q09_gr': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/01_Chapter_1_The_Dental_Pulp_and_Periradicular_Tissues.md', 25, 'Gopikrishna, 2021'),
 # Grossman 14e Ch.12 Regenerative Endodontics; editor cited; PDF page only.
 'q09_gr12': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/12_Chapter_12_Regenerative_Endodontics.md', None, 'Gopikrishna, 2021'),
 # Gulabivala and Ng 4e Ch.1. Offset 9 confirmed at PDF 14 (printed 5), PDF 15 (printed 6) and PDF 16 (printed 7).
 'q09_gul': (T+'Endodontics_Kishor_Gulabivala_Yuan_Ling_Ng_4th_Ed_Mosby_2014_Chapterwise/01_1_Tooth_organogenesis_morphology_and_physiology.md', 9, 'Gulabivala and Ng, 2014'),
 # Torabinejad 6e Ch.12 (Versiani, Cleghorn, Christie). Offset 7 confirmed at PDF 232 (printed 225), PDF 240 (printed 233) and PDF 243 (printed 236).
 'q09_tor12': (T+'Endodontics_Principles_and_Practice_Chapterwise/12_12_Root_Canal_Anatomy.md', 7, 'Versiani, Cleghorn and Christie, 2021'),
 # Andreasen, Andreasen and Andersson (eds) 4e (2007) Ch.20; no chapter author named in the file, editors cited. Offset 16 confirmed at PDF 578 (printed 562) and PDF 579 (printed 563).
 'q09_and': (T+'Textbook_and_Color_Atlas_of_Traumatic_Chapterwise/20_20_Injuries_to_Developing_Teeth.md', 16, 'Andreasen, Andreasen and Andersson, 2007'),
 # ---- Q10 ----
 # Cohen's 12e Ch.11 (Johnson, Fayad, Berman); PDF page only.
 'q10_coh': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/11_11_Periradicular_surgery.md', None, 'Johnson, Fayad and Berman, 2021'),
 # Cohen's 12e Ch.24 (Bogen, Dammaschke, Chandler); PDF page only.
 'q10_coh24': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/24_24_Vital_pulp_therapy.md', None, 'Bogen, Dammaschke and Chandler, 2021'),
 # Torabinejad and Rubinstein (eds) 2017, Ch.8 (Johnson and Abedi). Offset 13 confirmed at PDF 147 (printed 134), PDF 148 (printed 135), PDF 150 (printed 137).
 'q10_mah': (T+'The_Art_and_Science_of_Contemporary_Surgical_Endodontics_Mahmoud_2_Chapterwise/08_Chapter_8_Local_Anesthesia_and_Hemostasis.md', 13, 'Johnson and Abedi, 2017'),
 # Current Therapy in Endodontics (ed. Jain, 2016) Ch.9 (Johnson, McNally, McClanahan, Niemczyk). Offset 26 confirmed at PDF 253 (printed 227) and PDF 254 (printed 228).
 'q10_jain': (T+'Current_Therapy_in_Endodontics_Chapterwise/09_10_pdf_p_228_283.md', 26, 'Johnson et al, 2016'),
 # Ingle's 7e Ch.24 (authors from the Contents/chapter line, letter-substituted in OCR; decoded as Torabinejad, Sabeti, Glickman: verify against the printed book). Printed = PDF + 89 (PDF 708 printed 797; PDF 727 printed 816), i.e. offset -89. OCR damaged ("fi"=3, "ff"=2, "Th"=4): clean phrases only.
 'q10_ing': (T+'Ingles_Endodontics_7th_Chapterwise/24_Chapter_24_Surgical_Endodontics.md', -89, 'Torabinejad, Sabeti and Glickman, 2019'),
 # Gutmann and Lovdahl 5e Ch.8. Offset 11 confirmed at PDF 161 (printed 150) and PDF 176 (printed 165).
 'q10_gut': (T+'Problem_Solving_in_Endodontics_James_L_Gutmann_Chapterwise/08_Chapter_8_Problem_Solving_in_Tooth_Isolation_Access_Openings.md', 11, 'Gutmann and Lovdahl, 2011'),
 # ---- Q11 ----
 # Pickard's Manual of Operative Dentistry 9e (Banerjee and Watson, 2011); PDF page only.
 'q11_pic': (T+'Operative_and_Dental_Materials_Textbooks/Pickards_Manual_of_Operative_Dentistry_9th.md', None, 'Banerjee and Watson, 2011'),
 # Summitt's Fundamentals of Operative Dentistry 4e (Hilton, Ferracane, Broome, 2013); PDF page only.
 'q11_sum': (T+'Operative_and_Dental_Materials_Textbooks/Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Hilton, Ferracane and Broome, 2013'),
 # Essentials of Dental Caries 4e (Kidd and Fejerskov, 2016); PDF page only.
 'q11_kid': (T+'Operative_and_Dental_Materials_Textbooks/Essentials_of_Dental_Caries_4th.md', None, 'Kidd and Fejerskov, 2016'),
 # A Clinical Guide to Applied Dental Materials (Bonsor and Pearson, 2013); PDF page only.
 'q11_bon': (T+'Operative_and_Dental_Materials_Textbooks/A_Clinical_Guide_to_Applied_Dental_Materials.md', None, 'Bonsor and Pearson, 2013'),
 # Cohen's 12e Ch.16 (Lin and Huang); PDF page only.
 'q11_coh': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/16_16_Pathobiology_of_apical_periodontitis.md', None, 'Lin and Huang, 2021'),
 # Gulabivala and Ng 4e Ch.15. Offset 9 confirmed at PDF 371 (printed 362) and PDF 372 (printed 363).
 'q11_gul': (T+'Endodontics_Kishor_Gulabivala_Yuan_Ling_Ng_4th_Ed_Mosby_2014_Chapterwise/15_15_The_medical_endo_interface_and_patients_with_special_need.md', 9, 'Gulabivala and Ng, 2014'),
 # Torabinejad 6e Ch.2 (Aminoshariaei and Fouad). Offset 7 confirmed at PDF 30 (printed 23), PDF 31 (24), PDF 34 (27).
 'q11_tor2': (T+'Endodontics_Principles_and_Practice_Chapterwise/02_2_Systemic_Health_Considerations_in_the_Endodontic_Patient_a.md', 7, 'Aminoshariaei and Fouad, 2021'),
}
BOOK_EXTRA = {}
L = {
 # ---- Q09 Hertwig's epithelial root sheath ----
 'q09_gr_origin': ('q09_gr', 'On completion of the crown, the cervical loop, formed by the union of inner and outer enamel epithelia, proliferates to form the Hertwig’s epithelial root sheath'),
 'q09_gul_two': ('q09_gul', 'grow as a two-layered epithelial wall, which is now called the sheath of Hertwig'),
 'q09_gul_map': ('q09_gul', 'The sheath of Hertwig maps out the shape of the root(s)'),
 'q09_gul_tube': ('q09_gul', 'It is disposed in a simple tube for a single root, and in a more complex form for multiple roots'),
 'q09_gr_dia': ('q09_gr', 'delineates the apical foramen or foramina. This proliferation is called the epithelial diaphragm'),
 'q09_gr_evag': ('q09_gr', 'diaphragm evaginates in two predetermined places that come together and form two openings'),
 'q09_gr_multi': ('q09_gr', 'In multirooted teeth, the epithelial diaphragm guides the formation of the furca, roots, root canals, and apical foramina'),
 'q09_gr_ind': ('q09_gr', 'The inner enamel epithelium below the future cementoenamel junction induces the peripheral mesenchymal cells of the dental papilla to differentiate into odontoblasts'),
 'q09_gr_erupt': ('q09_gr', 'forces the fully formed crown toward the oral cavity while maintaining the epithelial diaphragm in a stable position in the jaw'),
 'q09_gr_bm': ('q09_gr', 'the basement membrane of the inner enamel epithelium disintegrates and the epithelial cells lose their continuity'),
 'q09_gr_cb': ('q09_gr', 'These mesenchymal cells differentiate into cementoblasts'),
 'q09_gr_rests': ('q09_gr', 'This cluster of epithelial cells comprises the cell rests of Malassez'),
 'q09_gr_cyst': ('q09_gr', 'have the potential of proliferating into periradicular cysts if stimulated by chronic inflammation'),
 'q09_gr_acc': ('q09_gr', 'A defect in the epithelial root sheath, a failure in the induction of dentinogenesis, or the presence of a small blood vessel produces a gap that results in the formation of an accessory canal'),
 'q09_tor_tau': ('q09_tor12', 'It is thought to be caused by the failure of Hertwig’s epithelial root sheath diaphragm to invaginate at the proper horizontal level'),
 'q09_and_arrest': ('q09_and', 'apparently directly injured Hertwig’s epithelial root sheath, thus compromising normal root development'),
 'q09_gr12_res': ('q09_gr12', 'cells of Hertwig’s epithelial root sheath, which are quite resistant to destruction, even in the presence of inflammation'),
 # ---- Q10 Haemostatic agents ----
 'q10_coh_def': ('q10_coh', 'They generally aid coagulation by inducing rapid development of an occlusive clot, either by exerting a physical tamponade action or by enhancing the clotting mechanism and vasoconstriction'),
 'q10_coh_noideal': ('q10_coh', 'No one local hemostatic agent is ideal; each has disadvantages'),
 'q10_mah_first': ('q10_mah', 'The first step in assuring adequate hemostasis is the use of a local anesthetic with'),
 'q10_coh_epi': ('q10_coh', 'Racemic epinephrine cotton pellets (Racellet #3; Pascal Co., Bellevue, WA) contain an average of 0.55 mg of racemic epinephrine hydrochloride per pellet'),
 'q10_coh_fibres': ('q10_coh', 'retention of cotton fibers in the surgical site could result in inflammation and impaired wound healing'),
 'q10_coh_acct': ('q10_coh', 'Each pellet applied during surgery must be accounted for'),
 'q10_mah_fs': ('q10_mah', 'Tissue proteins are agglutinated and then plug capillary orifices'),
 'q10_coh_fs': ('q10_coh', 'Failure to remove ferric sulfate from the surgical wound site resulted in severely impaired healing, a foreign body-type reaction, and, in some cases, abscess formation'),
 'q10_jain_alcl': ('q10_jain', 'Aluminum chloride acts by hemagglutination and will cause necrosis, so it must be removed completely when the procedure is finished'),
 'q10_mah_coll': ('q10_mah', 'On contact with blood, collagen causes platelet aggregation with subsequent fibrin clot formation, and hemostasis occurs in 2 to 6 minutes'),
 'q10_coh_gel': ('q10_coh', 'It stimulates the intrinsic clotting pathway by promoting platelet disintegration and the subsequent release of thromboplastin and thrombin'),
 'q10_coh_surg': ('q10_coh', 'It is primarily a physical hemostatic agent, which acts as a barrier to blood and then becomes a sticky mass that serves as an artificial coagulum'),
 'q10_coh_cs': ('q10_coh', 'As a hemostatic agent, calcium sulfate acts as a physical barrier'),
 'q10_coh_adh': ('q10_coh', 'Collagen-based materials can be difficult to apply to the bony crypt because they adhere to wet surfaces'),
 'q10_coh_wax': ('q10_coh', 'The use of bone wax can no longer be recommended because it impairs healing and several good alternatives are available'),
 'q10_coh_caut': ('q10_coh', 'Cautery stops the flow of blood through coagulation of blood and tissue protein, leaving an eschar that the body attempts to slough'),
 'q10_ing_epi': ('q10_ing', 'Hemostasis during PAS is achieved primarily by the epinephrine present in local anesthetic'),
 'q10_gut_dry': ('q10_gut', 'First, attempt to control the hemorrhage with a dry, sterile cotton pellet or the large end of a sterile paper point'),
 'q10_gut_epi': ('q10_gut', 'A hemostatic agent in small amounts may be considered, such as epinephrine 1:50,000 on a cotton pellet'),
 'q10_gut_fs': ('q10_gut', 'Ferric sulfate is another option'),
 'q10_gut_avoid': ('q10_gut', 'Avoid strong hemostatic agents that may cause significant damage and do not use formocresol'),
 'q10_coh24_naocl': ('q10_coh24', 'NaOCl in concentrations of 1.5% to 5.25% is currently regarded as the most effective, safe, and inexpensive hemostatic solution for pulp capping and partial and complete pulpotomy procedures'),
 'q10_coh24_10': ('q10_coh24', 'continued hemorrhaging after a 10-minute exposure strongly indicates irreversible pulpitis'),
 # ---- Q11 Xerostomia ----
 'q11_kid_def': ('q11_kid', 'some patients are aware of dry mouth (this is called xerostomia). Others with reduced salivary flow (hyposalivation) do not realize that they have a dry mouth'),
 'q11_kid_norm_u': ('q11_kid', 'Unstimulated: 0.3–0.5 ml/min'),
 'q11_kid_norm_s': ('q11_kid', 'Stimulated: 1–2 ml/min'),
 'q11_sum_hypo': ('q11_sum', 'unstimulated salivary flow in a range less than 0.1 to 0.2 mL/min is the criterion for hypofunction'),
 'q11_pic_cause': ('q11_pic', 'are the most common causes of severe xerostomia'),
 'q11_pic_drugs': ('q11_pic', 'a large number of therapeutic drugs, such as antidepressants, tranquillizers, antihypertensives, and diuretics can retard salivary flow'),
 'q11_sum_cause': ('q11_sum', 'radiation therapy of the head and neck, immuno-suppressive therapy, radioactive iodine therapy, autoimmune diseases, HIV infection'),
 'q11_gul_pd': ('q11_gul', 'They are at increased risk of xerostomia, resulting in burning mouth and root caries'),
 'q11_sum_fn': ('q11_sum', 'Saliva provides lubrication; promotes oral clearance of fermentable carbohydrates, sugars, and acids'),
 'q11_sum_caries': ('q11_sum', 'Xerostomia, or dry mouth, is associated with increases in the number of cariogenic bacteria and increased caries activity'),
 'q11_pic_sites': ('q11_pic', 'can develop lesions on the incisal surfaces of anterior teeth and lesions that circumvent the neck of the crown at the gingival margin'),
 'q11_coh_sjo': ('q11_coh', 'It involves salivary glands resulting in xerostomia. The lack of salivary cleansing action predisposes the patient to dental caries'),
 'q11_coh_pulp': ('q11_coh', 'If the caries is not prevented or treated early, it would impose risk of pulpal infection and apical'),
 'q11_tor_rc': ('q11_tor2', 'Also, dry mouth results in recurrent caries, compromising the prognosis'),
 'q11_sum_stim': ('q11_sum', 'If functioning salivary gland tissue is present, stimulation of natural flow is preferable to saliva substitutes'),
 'q11_sum_pilo': ('q11_sum', 'Pilocarpine (Salagen, MGI Pharma) and cevimeline (Evoxac, Daiichi Pharmaceutical) can be extremely effective salivary gland stimulants'),
 'q11_sum_demin': ('q11_sum', 'some commercial products have been found to have the potential to demineralize dentin and should be avoided'),
 'q11_bon_prep': ('q11_bon', 'Available preparations aim to supplement natural saliva and to provide the missing enzymes and proteins found with hyposalivation'),
 'q11_bon_mw': ('q11_bon', 'moisturizing mouthrinses, gels and toothpastes. The mouthwashes tend to be'),
 'q11_bon_gum': ('q11_bon', 'Non-stick, sugar-free chewing gum is also available to help stimulate saliva production'),
 'q11_pic_gic': ('q11_pic', 'An adverse oral environment can affect the set and physical properties of some materials, e.g. GICs in xerostomia'),
 'q11_sum_gi': ('q11_sum', 'Glass-ionomer restorations in the same patient did not exhibit recurrent caries lesions for the duration of the'),
 'q11_pic_fl': ('q11_pic', 'painful for those with a dry mouth. A bland, non-alcoholic mouthwash should be advised'),
}
