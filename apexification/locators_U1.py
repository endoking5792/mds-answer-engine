import os
# Auditor u1 locators for Q01 "Open Apex - considerations and management." (75m). Every key starts with u1_.
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
F_EXTRA = {
 # offsets confirmed at two pages in each chapter: printed = PDF - offset
 'u1_wal22': (T+'Principles_and_practice_of_endodontic_2002_compressed_Chapterwise/22_Part_22_Management_of_Incompletely_Formed_Roots.md', 15, 'Pitt Ford and Shabahang, 2002'),  # PDF 403 = p.388, PDF 405 = p.390
 'u1_vpt9':  (T+'Vital_Pulp_Treatment_Chapterwise/06_Pages_181_210.md', 21, 'Widbiller and Galler, 2024'),   # Ch.9 only: PDF 206 = p.185, PDF 207 = p.186
 'u1_vpt9b': (T+'Vital_Pulp_Treatment_Chapterwise/07_Pages_211_240.md', 21, 'Widbiller and Galler, 2024'),  # PDF 211 = p.190, PDF 213 = p.192
 'u1_kb5':   (T+'Endodontic_Prognosis_Clinical_Guide_Chapterwise/05_5_Regenerative_Approaches_in_Endodontic_Therapies_of_Immatur.md', 9, 'Kang and Bogen, 2017'),  # PDF 74 = p.65, PDF 89 = p.80
 'u1_ee11':  (T+'Essential_Endodontology_Chapterwise/11_Pages_331_360.md', 10, 'Ørstavik, 2020'),          # PDF 338 = p.328, PDF 339 = p.329
 'u1_ct11':  (T+'Current_Therapy_in_Endodontics_Chapterwise/11_12_pdf_p_297_306.md', 26, 'Kim, 2016'),       # PDF 297 = p.271, PDF 298 = p.272
 'u1_coh24': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/24_24_Vital_pulp_therapy.md', None, 'Bogen, Dammaschke and Chandler, 2021'),
 'u1_ing27': (T+'Ingles_Endodontics_7th_Chapterwise/27_Chapter_27_Vital_Pulp_Therapy.md', -100, 'Bogen and Chandler, 2019'),  # PDF 785 = p.885, PDF 786 = p.886
 'u1_ing29': (T+'Ingles_Endodontics_7th_Chapterwise/29_Chapter_29_Regenerative_Endodontics.md', -111, 'Diogenes and Smith, 2019'),  # PDF 824 = p.935, PDF 825 = p.936
 'u1_tor18': (T+'Endodontics_Principles_and_Practice_Chapterwise/18_18_Procedural_Accidents.md', 7, 'Nosrat, Terauchi and Torabinejad, 2021'),  # PDF 390 = p.383, PDF 400 = p.393
}
BOOK_EXTRA = {
 'u1_PittFord2002': "Pitt Ford TR, Shabahang S. Management of incompletely formed roots. In: Walton RE, Torabinejad M. Principles and Practice of Endodontics. 3rd ed. Philadelphia: WB Saunders; 2002. Ch.22.",
 'u1_Widbiller2024': "Widbiller M, Galler KM. Regenerative endodontics. In: Duncan HF, El-Karim IA, editors. Vital Pulp Treatment. 1st ed. Chichester: John Wiley & Sons; 2024. Ch.9.",
 'u1_Kang2017': "Kang MK, Bogen G. Regenerative approaches in endodontic therapies of immature teeth. In: Chugal N, Lin LM, editors. Endodontic Prognosis: Clinical Guide for Optimal Treatment Outcome. Cham: Springer; 2017. Ch.5.",
 'u1_Orstavik2020': "Ørstavik D. Endodontic treatment of apical periodontitis. In: Ørstavik D, editor. Essential Endodontology: Prevention and Treatment of Apical Periodontitis. 3rd ed. Hoboken: John Wiley & Sons; 2020. Ch.11.",
 'u1_Kim2016': "Kim SG. Dental pulp regeneration. In: Jain P, editor. Current Therapy in Endodontics. 1st ed. Ames: John Wiley & Sons; 2016. Ch.11.",
 'u1_Bogen2021': "Bogen G, Dammaschke T, Chandler N. Vital pulp therapy. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.24.",
 'u1_Bogen2019': "Bogen G, Chandler NP. Vital pulp therapy. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.27 (author line decoded from the OCR cipher; confirmed in the contents page).",
 'u1_Nosrat2021': "Nosrat A, Terauchi Y, Torabinejad M. Procedural accidents. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.18.",
}
L = {
 # ---- Walton and Torabinejad 3rd ed Ch.22 (Pitt Ford and Shabahang, 2002)
 'u1_w_normal': ('u1_wal22', 'An open apex is found in the developing roots of immature teeth and, in the absence of pulp or periradicular disease, is normal'),
 'u1_w_3yr': ('u1_wal22', 'Apical closure occurs approximately 3 years after eruption'),
 'u1_w_ortho': ('u1_wal22', 'extensive resorption of a mature apex after orthodontic treatment'),
 'u1_w_trauma': ('u1_wal22', 'or as part of healing after trauma'),
 'u1_w_walls': ('u1_wal22', 'They may diverge (see Figure 22-1), be parallel (see Figure 22-2), or converge slightly, depending on the stage of root formation'),
 'u1_w_vptterm': ('u1_wal22', 'Vital pulp therapy, previously called apexogenesis'),
 'u1_w_recterm': ('u1_wal22', 'Root-end closure, previously referred to as apexification'),
 'u1_w_causes': ('u1_wal22', 'mechanical exposure, or a developmental anomaly (e.g., dens invaginatus)'),
 'u1_w_cortic': ('u1_wal22', 'It is normal for a radiolucent area with a corticated margin to surround the developing open apex'),
 'u1_w_contra': ('u1_wal22', 'Comparison with the periapex of the contralateral tooth is helpful'),
 'u1_w_nerves': ('u1_wal22', 'nerves may be damaged while the blood supply remains intact'),
 'u1_w_alt': ('u1_wal22', 'Alternative treatments include (1) apical plug, (2) root canal treatment, (3) periapical surgery, and (4) extraction'),
 'u1_w_surg': ('u1_wal22', 'Surgical intervention is possible but is best avoided in children'),
 'u1_w_vptci1': ('u1_wal22', 'Avulsed and replanted or severely luxated tooth'),
 'u1_w_vptci2': ('u1_wal22', 'Severe crown-root fracture that requires intraradicular retention for restoration'),
 'u1_w_vptci3': ('u1_wal22', 'Tooth with an unfavorable horizontal root fracture'),
 'u1_w_vptci4': ('u1_wal22', 'Carious tooth that is unrestorable'),
 'u1_w_vptind': ('u1_wal22', 'whose radicular pulp is presumed to be healthy. The crown must be fairly intact and restorable'),
 'u1_w_recind': ('u1_wal22', 'Root-end closure is required for a restorable immature tooth with pulp necrosis'),
 'u1_w_recci1': ('u1_wal22', 'All vertical and most horizontal root fractures'),
 'u1_w_recci2': ('u1_wal22', 'Replacement resorption (ankylosis)'),
 'u1_w_recci3': ('u1_wal22', 'Very short roots'),
 'u1_w_recci4': ('u1_wal22', 'Marginal periodontal breakdown'),
 'u1_w_faster': ('u1_wal22', 'barrier formation occurs more rapidly when the apical opening is less wide'),
 'u1_w_23mm': ('u1_wal22', 'Because the inflammation is super'),
 'u1_w_23mm2': ('u1_wal22', 'ficial (2 to 3 mm deep), only the inflamed tissue is removed'),
 'u1_w_4yr': ('u1_wal22', 'Recall appointments should then be done for at least 4 years'),
 'u1_w_mistaken': ('u1_wal22', 'calcium hydroxide has been commonly used in the mistaken belief that it stimulates hard tissue formation'),
 'u1_w_critical': ('u1_wal22', 'The factors most critical to success are thorough debridement of the pulp space and a complete coronal seal'),
 'u1_w_nohed': ('u1_wal22', 'The use of Hedstrom files is not advocated because their sharp flutes may perforate the thin fragile walls of dentin'),
 'u1_w_barium': ('u1_wal22', 'Calcium hydroxide powder with barium sulfate added for radiopacity (9:1 ratio)'),
 'u1_w_irm': ('u1_wal22', 'Fortified zinc oxide-eugenol cement (IRM) is preferred'),
 'u1_w_46wk': ('u1_wal22', 'The patient is recalled in 4 to 6 weeks'),
 'u1_w_1yr': ('u1_wal22', 'If healing (bony resolution) has progressed well after 1 year, the calcium hydroxide is removed'),
 'u1_w_tactile': ('u1_wal22', 'A hard tissue barrier is often not visible radiographically but is detected tactically'),
 'u1_w_chloro': ('u1_wal22', 'dip the master gutta-percha cone briefly in chloroform'),
 'u1_w_mta1wk': ('u1_wal22', 'Calcium hydroxide paste is placed in the canal for a period of 1 week to disinfect the root canal system'),
 'u1_w_mta34': ('u1_wal22', 'to create a 3- to 4-mm apical plug'),
 'u1_w_succvpt': ('u1_wal22', 'Continued growth of the root and canal narrowing, indicating dentin formation'),
 'u1_w_succvpt2': ('u1_wal22', 'A bridge of calcification (may not be visible radiographically) beneath the filling material'),
 'u1_w_succrec': ('u1_wal22', 'Presence of a calcific barrier across the apex as demonstrated by radiographs or, more often, by careful tactile probing with a file'),
 'u1_w_failcause': ('u1_wal22', 'usually fails because of one common cause: bacterial contamination'),
 'u1_w_fail4': ('u1_wal22', 'Continual loss of calcium hydroxide from the canal space, indicating persistent periradicular inflammation'),
 'u1_w_fail5': ('u1_wal22', 'Down-growth of granulomatous tissue into the canal, manifested by bleeding when files are placed short of the apex'),
 'u1_w_late': ('u1_wal22', 'Infected necrotic material trapped in the barrier may contribute to these failures'),
 'u1_w_vrf': ('u1_wal22', 'ther reason for failure is an undetected vertical or horizontal root fracture'),
 'u1_w_12mo': ('u1_wal22', 'all patients should be recalled at 12-month intervals for 4 years'),
 'u1_w_pupcalc': ('u1_wal22', 'after conventional pulpotomy, the success rate is lower and calcific metamorphosis is a common occurrence'),
 'u1_w_noroutine': ('u1_wal22', 'Histologic evidence does not support the use of routine pulp extirpation and root filling after apical closure'),
 # ---- Vital Pulp Treatment Ch.9 (Widbiller and Galler, 2024)
 'u1_v_cvek5': ('u1_vpt9', 'Stages 1–5 of root development according to Cvek et al.'),
 'u1_v_cvek5b': ('u1_vpt9', 'Stages 1–4 describe tooth roots during maturation, stage 5 the completed root growth'),
 'u1_v_stage4': ('u1_vpt9', 'From stage 4, the root has sufficient stability for both regenerative endodontic approaches and an apical barrier'),
 'u1_v_stage13': ('u1_vpt9', 'Particularly in the early stages of root development (stages 1–3)'),
 'u1_v_ci': ('u1_vpt9', 'revitalization of teeth is not advisable if a dental dam cannot be applied or if extensive coronal hard substance loss would require insertion of an intra'),
 'u1_v_onethird': ('u1_vpt9', 'can be expected in about one-third of cases'),
 'u1_v_asa': ('u1_vpt9', 'Patients with severe general medical impairment (ASA 3 or higher)'),
 'u1_v_norec': ('u1_vpt9', 'no longer the preferred option'),
 'u1_v_plugrec': ('u1_vpt9', 'the current recommendation for immature teeth is to place an apical plug with HCSC'),
 'u1_v_nodiff': ('u1_vpt9b', 'there is no significant difference between apexification, apical plug and revitalization in terms of periapical healing and tooth survival'),
 'u1_v_goals': ('u1_vpt9b', 'the progression of root growth in length and thickness (secondary goal)'),
 'u1_v_barium': ('u1_vpt9b', 'barium sulphate, which is often added to MTA as a radiopacifier'),
 'u1_v_older': ('u1_vpt9b', 'Even in teeth with an open apex at an older age, it is biologically unlikely that further root development will occur'),
 'u1_v_followup': ('u1_vpt9b', 'Follow-up visits are recommended after 6, 12, 18 and 24 months and then annually for five years'),
 # ---- Endodontic Prognosis Ch.5 (Kang and Bogen, 2017)
 'u1_k_15yr': ('u1_kb5', 'these teeth may require one to 5 years to complete maturation and root-end closure'),
 'u1_k_perm': ('u1_kb5', 'Immature permanent teeth also exhibit greater dentinal permeability due to the presence of large dentinal tubules'),
 'u1_k_scap': ('u1_kb5', 'The apical papilla is a potent source of stem cells that contribute to pulp and root maturation and can survive after pulpal necrosis'),
 'u1_k_embalm': ('u1_kb5', 'designed to embalm tissues rather than to encourage preservation'),
 'u1_k_overfill': ('u1_kb5', 'although CSC overfill does not compromise the outcome'),
 'u1_k_ultra': ('u1_kb5', 'manual compaction of MTA provides dense compaction and may be preferable to using ultrasonic condensation techniques'),
 'u1_k_ultra2': ('u1_kb5', 'excessive extrusion of the cement is a common drawback in teeth with open apices'),
 'u1_k_45mm': ('u1_kb5', 'the obturation should ideally produce a 4–5 mm CSC plug to ensure an adequate seal'),
 'u1_k_haem': ('u1_kb5', 'In cases where hemostasis is not attainable, the canal should be filled with CH paste and the patient rescheduled'),
 'u1_k_behav': ('u1_kb5', 'This is a valid option for challenging behavioral management cases in pediatric patients'),
 # ---- Essential Endodontology Ch.11 (Ørstavik, 2020)
 'u1_o_apexog': ('u1_ee11', 'the primary goal is to stimulate completion of apexogenesis'),
 'u1_o_ca': ('u1_ee11', 'a dressing with calcium hydroxide was the standard procedure, today, bioceramic materials applied in a single visit give similar results'),
 'u1_o_dens': ('u1_ee11', 'The first cases with impressive hard tissue formation were in premolars with dens evaginatus and no history of trauma'),
 'u1_o_repair': ('u1_ee11', 'is currently not achieved (see Figure 11.10)'),
 # ---- Current Therapy in Endodontics Ch.11 (Kim, 2016)
 'u1_c_aae': ('u1_ct11', 'compliant patient with necrotic pulp, an immature apex, and pulp space not needed for post and core'),
 'u1_c_1mm': ('u1_ct11', 'should have an open apex with diameters bigger than 1.0 mm or 1.1 mm'),
 'u1_c_thin2': ('u1_ct11', 'Root remains thin'),
 'u1_c_thin': ('u1_ct11', 'Neither strengthens the root nor promotes further development'),
 # ---- Ingle's Ch.29 (Diogenes and Smith, 2019)
 'u1_d_1mm': ('u1_ing29', 'more desirable outcomes being seen in teeth with a radiographic apical diameter of at least 1 mm'),
 # ---- Cohen's Ch.24 (Bogen, Dammaschke and Chandler, 2021)
 'u1_b_520': ('u1_coh24', 'CSCs can be used as an apical plug to stimulate the apical papilla to promote barrier formation, which may require 5 to 20 months'),
 'u1_b_marker': ('u1_coh24', 'Radiographic evidence of root-end closure in immature adult teeth is a reliable prognostic marker of continued pulp vitality'),
 'u1_b_contra': ('u1_coh24', 'coincides with the contralateral teeth in the same patient'),
 # ---- Ingle's Ch.27 (Bogen and Chandler, 2019)
 'u1_bc_fc': ('u1_ing27', 'experiments in nonhuman primates have demonstrated a greater incidence of internal resorption'),
 'u1_bc_fc2': ('u1_ing27', 'Recent investigations support MTA and other CSCs as practical replacements for formocresol in primary and immature permanent teeth'),
 # ---- Torabinejad Ch.18 (Nosrat, Terauchi and Torabinejad, 2021)
 'u1_n_zip': ('u1_tor18', 'Incorrect working length or inability to maintain proper working length causes'),
 'u1_n_blow': ('u1_tor18', 'or “blowing out” of the apical foramen'),
}
