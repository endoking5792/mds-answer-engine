# Auditor u3 locators (Q03 Apexification, Q04 Apexogenesis, P1 calcium hydroxide vs MTA plug). All keys prefixed u3_.
# Books the drafters did not use. Offsets: printed page = PDF marker - offset, checked at two or more pages in that chapter.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
F_EXTRA = {
 # Walton & Torabinejad 3e (2002) Part 22, chapter authors Pitt Ford and Shabahang (Contents page). Offset 15: PDF 404 = p.389, PDF 410 = p.395, PDF 411 = p.396.
 'u3_wt22': (T+'Principles_and_practice_of_endodontic_2002_compressed_Chapterwise/22_Part_22_Management_of_Incompletely_Formed_Roots.md', 15, 'Pitt Ford and Shabahang, 2002'),
 # Current Therapy in Endodontics (Jain, ed., 2016) Ch.11 Kim. Offset 26: PDF 298 = p.272, PDF 299 = p.273.
 'u3_ct11': (T+'Current_Therapy_in_Endodontics_Chapterwise/11_12_pdf_p_297_306.md', 26, 'Kim, 2016'),
 # Same book Ch.7 Al Khatib and Besner. Offset 26: PDF 199 = p.173, PDF 200 = p.174.
 'u3_ct7': (T+'Current_Therapy_in_Endodontics_Chapterwise/07_8_pdf_p_179_217.md', 26, 'Al Khatib and Besner, 2016'),
 # Vital Pulp Treatment (Duncan and El-Karim, eds, 2024) Ch.6 Careddu, Lappin, Duncan and El-Karim. Offset 19: PDF 129 = p.110, PDF 131 = p.112, PDF 142 = p.123.
 'u3_vpt6': (T+'Vital_Pulp_Treatment_Chapterwise/04_Pages_121_150.md', 19, 'Careddu et al, 2024'),
 # Ch.8 Kahler and Rossi-Fedele (file 05 and 06). Offset 20: PDF 176 = p.156, PDF 177 = p.157, PDF 184 = p.164, PDF 185 = p.165.
 'u3_vpt8': (T+'Vital_Pulp_Treatment_Chapterwise/05_Pages_151_180.md', 20, 'Kahler and Rossi-Fedele, 2024'),
 'u3_vpt8b': (T+'Vital_Pulp_Treatment_Chapterwise/06_Pages_181_210.md', 20, 'Kahler and Rossi-Fedele, 2024'),
 # Ch.9 Widbiller and Galler (files 06 and 07). Offset 21: PDF 207 = p.186, PDF 208 = p.187, PDF 209 = p.188.
 'u3_vpt9': (T+'Vital_Pulp_Treatment_Chapterwise/06_Pages_181_210.md', 21, 'Widbiller and Galler, 2024'),
 'u3_vpt9b': (T+'Vital_Pulp_Treatment_Chapterwise/07_Pages_211_240.md', 21, 'Widbiller and Galler, 2024'),
 # Ch.10 Cushley, Shimizu, Kobayashi and Nagendrababu. Offset 21: PDF 222 = p.201, PDF 223 = p.202, PDF 224 = p.203.
 'u3_vpt10': (T+'Vital_Pulp_Treatment_Chapterwise/07_Pages_211_240.md', 21, 'Cushley et al, 2024'),
 # Essential Endodontology 3e (Orstavik, ed., 2020) Ch.11 Orstavik. Offset 10: PDF 338 = p.328, PDF 339 = p.329.
 'u3_ee11': (T+'Essential_Endodontology_Chapterwise/11_Pages_331_360.md', 10, 'Ørstavik, 2020'),
 # Endodontic Prognosis (Chugal and Lin, eds, 2017) Ch.5 Kang and Bogen. Offset 9: PDF 74 = p.65, PDF 76 = p.67, PDF 78 = p.69, PDF 88 = p.79.
 'u3_ep5': (T+'Endodontic_Prognosis_Clinical_Guide_Chapterwise/05_5_Regenerative_Approaches_in_Endodontic_Therapies_of_Immatur.md', 9, 'Kang and Bogen, 2017'),
 # Seltzer and Bender 2e (2012) Ch.13 Goodis, Marshall, Tay and Marshall; ebook, no printed page numbers.
 'u3_sb13': (T+'Seltzer_and_Bender_Dental_Pulp_Chapterwise_MD/Chapter_13_Repair_of_Pulpal_Injury_with_Dental_Materials.md', None, 'Goodis et al, 2012'),
 # Endodontology (Baumann and Beer, eds, 2010) Ch.46, chapter authors V. Buerkle and N. Meissner (Contents page). Offset 17: PDF 378 = p.361, PDF 379 = p.362, PDF 381 = p.364.
 'u3_en46': (T+'Endodontology_Chapterwise/46_46_Endodontics_in_the_Mixed_Dentition.md', 17, 'Buerkle and Meissner, 2010'),
 # Gutmann and Lovdahl, Problem Solving in Endodontics 5e (2011) Ch.13. Offset 11: PDF 252 = p.241, PDF 253 = p.242, PDF 254 = p.243.
 'u3_gut13': (T+'Problem_Solving_in_Endodontics_James_L_Gutmann_Chapterwise/13_Chapter_13_Problem_Solving_Challenges_in_Compromised_Roots_R.md', 11, 'Gutmann and Lovdahl, 2011'),
 # Harty's 7e Ch.12 (Sigurdsson and Bourguignon), offset 16 (PDF 255 = p.239, PDF 256 = p.240). Used here for Q04.
 'u3_har12': (T+'Harty_s_Endodontics_in_Clinical_Practice_7th_ed_Chapterwise/12_12_Endodontic_Aspects_of_Traumatic_Injuries.md', 16, 'Sigurdsson and Bourguignon, 2017'),
}
BOOK_EXTRA = {
 'u3_PittFord2002': 'Pitt Ford TR, Shabahang S. Management of incompletely formed roots. In: Walton RE, Torabinejad M, editors. Principles and Practice of Endodontics. 3rd ed. Philadelphia: WB Saunders; 2002. Ch.22.',
 'u3_Kim2016': 'Kim SG. Dental pulp regeneration. In: Jain P, editor. Current Therapy in Endodontics. 1st ed. Ames: John Wiley & Sons; 2016. Ch.11.',
 'u3_AlKhatib2016': 'Al Khatib Z, Besner E. Dental traumatic injuries. In: Jain P, editor. Current Therapy in Endodontics. 1st ed. Ames: John Wiley & Sons; 2016. Ch.7.',
 'u3_Careddu2024': 'Careddu R, Lappin M, Duncan HF, El-Karim IA. Vital pulp treatment modalities: pulpotomy - partial and complete. In: Duncan HF, El-Karim IA, editors. Vital Pulp Treatment. 1st ed. Chichester: John Wiley & Sons; 2024. Ch.6.',
 'u3_Kahler2024': 'Kahler B, Rossi-Fedele G. Vital pulp treatment for traumatic dental injuries. In: Duncan HF, El-Karim IA, editors. Vital Pulp Treatment. 1st ed. Chichester: John Wiley & Sons; 2024. Ch.8.',
 'u3_Widbiller2024': 'Widbiller M, Galler KM. Regenerative endodontics. In: Duncan HF, El-Karim IA, editors. Vital Pulp Treatment. 1st ed. Chichester: John Wiley & Sons; 2024. Ch.9.',
 'u3_Cushley2024': 'Cushley S, Shimizu E, Kobayashi Y, Nagendrababu V. Outcome of vital pulp treatment and regenerative endodontics. In: Duncan HF, El-Karim IA, editors. Vital Pulp Treatment. 1st ed. Chichester: John Wiley & Sons; 2024. Ch.10.',
 'u3_Orstavik2020': 'Ørstavik D. Endodontic treatment of apical periodontitis. In: Ørstavik D, editor. Essential Endodontology: Prevention and Treatment of Apical Periodontitis. 3rd ed. Hoboken: Wiley-Blackwell; 2020. Ch.11.',
 'u3_Kang2017': 'Kang MK, Bogen G. Regenerative approaches in endodontic therapies of immature teeth. In: Chugal N, Lin LM, editors. Endodontic Prognosis: Clinical Guide for Optimal Treatment Outcome. Cham: Springer; 2017. Ch.5.',
 'u3_Goodis2012': "Goodis HE, Marshall S, Tay FR, Marshall GW Jr. Repair of pulpal injury with dental materials. In: Hargreaves KM, Goodis HE, Tay FR, editors. Seltzer and Bender's Dental Pulp. 2nd ed. Chicago: Quintessence; 2012. Ch.13.",
 'u3_Baumann2010': "Buerkle V, Meissner N. Endodontics in the mixed dentition. In: Baumann MA, Beer R, editors. Endodontology. 2nd ed. Stuttgart: Thieme; 2010. Ch.46 (chapter authors from the contents page; the English edition is a translation of the 2nd German edition, © 2010 Georg Thieme Verlag).",
 'u3_Gutmann2011': 'Gutmann JL, Lovdahl PE. Problem-solving challenges in compromised roots, root canal systems, and anatomic deviations. In: Problem Solving in Endodontics: Prevention, Identification, and Management. 5th ed. St Louis: Mosby Elsevier; 2011. Ch.13.',
 'u3_Sigurdsson2017': "Sigurdsson A, Bourguignon C. Endodontic aspects of traumatic injuries. In: Chong BS, editor. Harty's Endodontics in Clinical Practice. 7th ed. Edinburgh: Elsevier; 2017. Ch.12.",
}
L = {
 # Pitt Ford and Shabahang 2002 (Walton & Torabinejad Part 22)
 'u3_wt_vpt': ('u3_wt22', 'Vital pulp therapy, previously called apexogenesis, is defined as treatment of a vital pulp in an immature tooth to permit continued dentin formation and apical closure'),
 'u3_wt_rec': ('u3_wt22', 'Root-end closure, previously referred to as apexification'),
 'u3_wt_3y': ('u3_wt22', 'Apical closure occurs approximately 3 years after eruption'),
 'u3_wt_vci1': ('u3_wt22', 'Avulsed and replanted or severely luxated tooth'),
 'u3_wt_vci2': ('u3_wt22', 'Severe crown-root fracture that requires intraradicular retention for restoration'),
 'u3_wt_vci3': ('u3_wt22', 'Tooth with an unfavorable horizontal root fracture'),
 'u3_wt_vci4': ('u3_wt22', 'Carious tooth that is unrestorable'),
 'u3_wt_rci1': ('u3_wt22', 'All vertical and most horizontal root fractures'),
 'u3_wt_rci2': ('u3_wt22', 'Replacement resorption (ankylosis)'),
 'u3_wt_rci3': ('u3_wt22', 'Very short roots'),
 'u3_wt_rci4': ('u3_wt22', 'Marginal periodontal breakdown 5. Vital pulps'),
 'u3_wt_typo': ('u3_wt22', 'Contradictions include the following'),
 'u3_wt_infl': ('u3_wt22', 'ficial (2 to 3 mm deep), only the inflamed tissue is removed'),
 'u3_wt_perm': ('u3_wt22', 'This is a permanent procedure; normally, root canal treatment is not required subsequently'),
 'u3_wt_histo': ('u3_wt22', 'Histologic evidence does not support the use of routine pulp extirpation and root filling after apical closure'),
 'u3_wt_cm': ('u3_wt22', 'a case has been made for root canal treatment, although this is probably unwarranted; calcific metamorphosis is not pathosis'),
 'u3_wt_conv': ('u3_wt22', 'Conventional pulpotomy is slightly less successful, particularly in anterior teeth'),
 'u3_wt_recall': ('u3_wt22', 'recall appointments at 3- to 6-month intervals to monitor pulp vitality and apical growth'),
 'u3_wt_4y': ('u3_wt22', 'Recall appointments should then be done for at least 4 years'),
 'u3_wt_s1': ('u3_wt22', 'Presence of a vital pulp'),
 'u3_wt_s2': ('u3_wt22', 'Absence of signs or symptoms of pulp or periapical disease'),
 'u3_wt_s3': ('u3_wt22', 'Continued growth of the root and canal narrowing, indicating dentin formation'),
 'u3_wt_s4': ('u3_wt22', 'A bridge of calcification (may not be visible radiographically) beneath the filling material'),
 'u3_wt_rs1': ('u3_wt22', 'Absence of signs or symptoms of periradicular pathosis'),
 'u3_wt_rs2': ('u3_wt22', 'Presence of a calcific barrier across the apex as demonstrated by radiographs or, more often, by careful tactile probing with a file'),
 'u3_wt_mist': ('u3_wt22', 'calcium hydroxide has been commonly used in the mistaken belief that it stimulates hard tissue formation'),
 'u3_wt_crit': ('u3_wt22', 'The factors most critical to success are thorough debridement of the pulp space and a complete coronal seal'),
 'u3_wt_noeff': ('u3_wt22', 'The addition of other medicaments to calcium hydroxide has been suggested, but with no beneficial effect on root-end closure'),
 'u3_wt_ba': ('u3_wt22', 'Calcium hydroxide powder with barium sulfate added for radiopacity (9:1 ratio)'),
 'u3_wt_4to6': ('u3_wt22', 'The patient is recalled in 4 to 6 weeks'),
 'u3_wt_dense': ('u3_wt22', 'If at recall, the calcium hydroxide appears dense and there are no clinical signs or symptoms of disease, it need not be replaced'),
 'u3_wt_1y': ('u3_wt22', 'If healing (bony resolution) has progressed well after 1 year, the calcium hydroxide is removed'),
 'u3_wt_rapid': ('u3_wt22', 'barrier formation occurs more rapidly when the apical opening is less wide'),
 'u3_wt_fail': ('u3_wt22', 'usually fails because of one common cause: bacterial contamination'),
 'u3_wt_mta': ('u3_wt22', 'placement of an apical plug of mineral trioxide aggregate (MTA) has been shown to be more effective and convenient than the use of calcium hydroxide'),
 'u3_wt_1wk': ('u3_wt22', 'Calcium hydroxide paste is placed in the canal for a period of 1 week to disinfect the root canal system'),
 'u3_wt_34': ('u3_wt22', '3- to 4-mm apical plug (see Figure 22-13)'),
 'u3_wt_fig13': ('u3_wt22', 'Unusual root-end closure. A barrier has formed, leaving a wide, divergent canal space'),
 'u3_wt_exp': ('u3_wt22', 'Expense is another factor; the patient (or parent) must be aware that these procedures require much more time and more appointments than conventional root canal treatment'),
 # Kim 2016 and Al Khatib and Besner 2016 (Current Therapy in Endodontics)
 'u3_kim_ca1': ('u3_ct11', 'Requires a long time for treatment results'),
 'u3_kim_ca2': ('u3_ct11', 'Increased risk of tooth fracture'),
 'u3_kim_mta1': ('u3_ct11', 'Root remains thin'),
 'u3_kim_mta2': ('u3_ct11', 'Neither strengthens the root nor promotes further development'),
 'u3_kim_induce': ('u3_ct11', 'Materials such as calcium hydroxide and MTA, which induce the formation of a calcified apical barrier, are used for apexification'),
 'u3_akb_regen': ('u3_ct7', 'These include direct pulp capping, revascularization, apexogenesis, apexification, stem cell therapy, and tissue engineering'),
 'u3_akb_avul': ('u3_ct7', 'In 12-18 week, ideally revascularisation/apexogenesis occurs'),
 # Vital Pulp Treatment 2024
 'u3_vpt_pp': ('u3_vpt6', 'A partial pulpotomy is a clinical procedure in which a small portion of the coronal pulp'),
 'u3_vpt_fp': ('u3_vpt6', 'A full (or complete) pulpotomy involves the complete removal of the coronal pulp'),
 'u3_vpt_23': ('u3_vpt6', 'In a partial pulpotomy, usually, 2–3 mm of pulp is removed'),
 'u3_vpt_875': ('u3_vpt6', 'High success rates of between 87.5 and 100% were reported for Cvek pulpotomy'),
 'u3_vpt_dpc': ('u3_vpt6', 'Direct pulp capping was only suggested for minor exposures treated within the first hours after trauma'),
 'u3_vpt8_455': ('u3_vpt8', 'the incidence of pulp necrosis was higher for pulp capping (45.5%) when compared to partial pulpotomy (13.6%)'),
 'u3_vpt8_rct': ('u3_vpt8', 'The ESE (2021) further clarifies that root canal treatment is only indicated if'),
 'u3_vpt8_mat': ('u3_vpt8b', 'whereas a more recent study reported a significant impact of tooth maturity on pulp survival'),
 'u3_vpt9_nolong': ('u3_vpt9', 'no longer the preferred option'),
 'u3_vpt9_plug': ('u3_vpt9', 'the current recommendation for immature teeth is to place an apical plug with HCSC'),
 'u3_vpt9_thin': ('u3_vpt9', 'this will still leave short roots with thin root walls, which means an increased risk of fracture'),
 'u3_vpt9_nodiff': ('u3_vpt9b', 'there is no significant difference between apexification, apical plug and revitalization in terms of periapical healing and tooth survival'),
 'u3_vpt10_ese': ('u3_vpt10', 'defined the success of VPT as an asymptomatic tooth with maintenance of vitality after at least one year'),
 'u3_vpt10_imm': ('u3_vpt10', 'in the case of immature teeth, continued root development'),
 # Orstavik 2020
 'u3_ee_goal': ('u3_ee11', 'the primary goal is to stimulate completion of apexogenesis'),
 'u3_ee_bio': ('u3_ee11', 'a dressing with calcium hydroxide was the standard procedure, today, bioceramic materials applied in a single visit give similar results'),
 # Kang and Bogen 2017
 'u3_kb_15y': ('u3_ep5', 'may require one to 5 years to complete maturation and root-end closure'),
 'u3_kb_34': ('u3_ep5', 'Partial removal of tissue (3–4 mm) in anterior teeth that have sustained traumatic fractures is also known as the “Cvek technique”'),
 'u3_kb_10min': ('u3_ep5', 'attained in 10 min or the entire pulpal roof or axial wall removed during excavation, then a CP or pulpectomy is indicated'),
 'u3_kb_612': ('u3_ep5', 'Radiographic follow-up, cold testing, and subjective symptomatology should be evaluated at 6 and 12 months for DPC and PP'),
 'u3_kb_overfill': ('u3_ep5', 'although CSC overfill does not compromise the outcome'),
 'u3_kb_manual': ('u3_ep5', 'manual compaction of MTA provides dense compaction and may be preferable to using ultrasonic condensation techniques'),
 'u3_kb_45': ('u3_ep5', 'the obturation should ideally produce a 4–5 mm CSC plug to ensure an adequate seal'),
 # Goodis et al 2012 (Seltzer and Bender Ch.13)
 'u3_sb_214': ('u3_sb13', 'Two of 14 teeth in the Ca(OH)2 group failed because of'),
 'u3_sb_all': ('u3_sb13', 'pain and swelling, while all in the MTA group appeared to be successfully treated'),
 'u3_sb_asgood': ('u3_sb13', 'MTA is as successful as or even more successful than Ca(OH)2 in vital pulp therapy procedures'),
 # Baumann and Beer 2010 (Endodontology Ch.46)
 'u3_en_norct': ('u3_en46', 'If the pulpotomy is successful, conventional root canal treatment will not be necessary later on'),
 'u3_en_24h': ('u3_en46', 'With a small pulp exposure or exposure over less than 24 hours, partial pulpotomy according to Cvek can be carried out'),
 'u3_en_2mm': ('u3_en46', 'about 2 mm of pulp tissue is removed'),
 'u3_en_1y': ('u3_en46', 'is generally cited as 1 year on average'),
 'u3_en_7496': ('u3_en46', 'is between 74% and 96% (Cvek'),
 'u3_en_stim': ('u3_en46', 'The stimulating effect of calcium hydroxide leads to proliferation of periodontal ligament cells at the apex'),
 'u3_en_36': ('u3_en46', 'Changing the calcium-hydroxide dressing under rubber dam every 3–6 months'),
 'u3_en_3mm': ('u3_en46', 'with a minimum thickness of 3 mm'),
 'u3_en_frac': ('u3_en46', 'the danger of fracture is clearly diminished in contrast with long-term dressings with calcium hydroxide'),
 'u3_en_cost': ('u3_en46', 'Costs High Low'),
 'u3_en_succ': ('u3_en46', 'Success (Still) questionable, seems to be good'),
 'u3_en_proc': ('u3_en46', 'Clinical procedure Diffi cult Simple'),
 # Gutmann and Lovdahl 2011
 'u3_gut_342': ('u3_gut13', '34.2 weeks (range 13 to 67 weeks)'),
 'u3_gut_counter': ('u3_gut13', 'this technique of changing the Ca(OH)2 has been shown to be counterproductive to the formation of hard tissue'),
 'u3_gut_12m': ('u3_gut13', 'with intervals as long as 12 months in later stages'),
 'u3_gut_odont': ('u3_gut13', 'odontoblasts rarely if ever survive pulpal necrosis'),
 'u3_gut_gnarl': ('u3_gut13', 'gnarled osteocementum type of material'),
 'u3_gut_exit': ('u3_gut13', 'exit Ca(OH)2 and enter MTA'),
 'u3_gut_ambig': ('u3_gut13', 'what is defined as a one-visit treatment may be ambiguous'),
 'u3_gut_714': ('u3_gut13', 'place Ca(OH)2 for 7 to 14 days'),
 # Sigurdsson and Bourguignon 2017 (Harty's Ch.12) for Q04
 'u3_har_choice': ('u3_har12', 'Partial pulpotomy is the treatment of choice'),
 'u3_har_2mm': ('u3_har12', 'Pulp removal is usually confined to the superficial 2 mm'),
 'u3_har_mta': ('u3_har12', 'MTA is no longer recommended for anterior teeth if discolouration is a concern'),
 'u3_har_norct': ('u3_har12', 'Root canal treatment is not needed subsequent to pulpotomy unless pulp necrosis and infection develops'),
}
