# Audit (u2) locators for Q02 "Discuss various methods to manage a nonvital anterior tooth with an immature apex." (50m)
# Every key starts with u2_. Sources the drafter did not use, plus a few new phrases from books already in locators_Q02.py
# (those L entries point at the existing q02_* source keys).
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
# Offsets (printed page = PDF marker - offset), each confirmed at two pages in the chapter:
#   Walton & Torabinejad 2002 Part 22: PDF 403 = 388, PDF 416 = 401 -> 15.  Part 25: PDF 463 = 446, PDF 481 = 464 -> 17.
#   Current Therapy in Endodontics Ch.11 (file 12.pdf): PDF 299 = 273, PDF 300 = 274 -> 26.
#   Ingle's 7th Ch.29: PDF 824 = 935 (contents page), PDF 838 = 949 -> -111.
#   Sikri 2nd Ch.38: PDF 656 = 635, PDF 657 = 636 -> 21.
#   Vital Pulp Treatment Ch.9: PDF 206 = 185, PDF 211 = 190 -> 21.
#   Essential Endodontology 3rd Ch.11: PDF 324 = 314, PDF 339 = 329 -> 10.
#   Andreasen atlas 4th Ch.27: PDF 756 = 740 (contents page), PDF 757 = 741 -> 16.
#   Treatment of Endodontic Infections 2nd Ch.15 and Seltzer & Bender 2nd Ch.5: no printed page numbers in the extraction -> None.
F_EXTRA = {
 'u2_wal22': (T+'Principles_and_practice_of_endodontic_2002_compressed_Chapterwise/22_Part_22_Management_of_Incompletely_Formed_Roots.md', 15, 'Walton and Torabinejad, 2002'),
 'u2_wal25': (T+'Principles_and_practice_of_endodontic_2002_compressed_Chapterwise/25_Part_25_Management_of_Traumatized_Teeth.md', 17, 'Walton and Torabinejad, 2002'),
 'u2_ct': (T+'Current_Therapy_in_Endodontics_Chapterwise/11_12_pdf_p_297_306.md', 26, 'Kim, 2016'),
 'u2_ing29': (T+'Ingles_Endodontics_7th_Chapterwise/29_Chapter_29_Regenerative_Endodontics.md', -111, 'Diogenes and Smith, 2019'),
 'u2_sik38': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/38_38_Regenerative_Endodontics.md', 21, 'Sikri, 2019, Ch.38'),
 'u2_vpt': (T+'Vital_Pulp_Treatment_Chapterwise/06_Pages_181_210.md', 21, 'Widbiller and Galler, 2024'),
 'u2_vpt2': (T+'Vital_Pulp_Treatment_Chapterwise/07_Pages_211_240.md', 21, 'Widbiller and Galler, 2024'),
 'u2_ee': (T+'Essential_Endodontology_Chapterwise/11_Pages_331_360.md', 10, 'Ørstavik, 2020'),
 'u2_tei': (T+'Treatment_of_Endodontic_Infections_Chapterwise/15_Chapter_15_Root_canal_obturation.md', None, 'Azim and Aksel, 2022'),
 'u2_sb5': (T+'Seltzer_and_Bender_Dental_Pulp_Chapterwise_MD/Chapter_05_Stem_Cells_and_Regeneration_of_the_Pulpodentin_Complex.md', None, 'Murray and García-Godoy, 2012'),
 'u2_and27': (T+'Textbook_and_Color_Atlas_of_Traumatic_Chapterwise/27_27_Autotransplantation_of_Teeth_to_the_Anterior_Region.md', 16, 'Andreasen, Andersson and Tsukiboshi, 2007'),
 'u2_ingfm': (T+'Ingles_Endodontics_7th_Chapterwise/00_Front_matter.md', None, 'Rotstein and Ingle, 2019'),
}
BOOK_EXTRA = {
 'u2_Walton2002': "Walton RE, Torabinejad M. Principles and practice of endodontics. 3rd ed. Philadelphia: WB Saunders; 2002. Ch.22 Management of incompletely formed roots; Ch.25 Management of traumatized teeth.",
 'u2_Kim2016': "Kim SG. Dental pulp regeneration. In: Jain P, editor. Current therapy in endodontics. Ames (IA): Wiley Blackwell; 2016. Ch.11.",
 'u2_Diogenes2019': "Diogenes AR, Smith AJ. Regenerative endodontics. In: Rotstein I, Ingle JI, editors. Ingle's endodontics. 7th ed. Raleigh (NC): PMPH USA; 2019. Ch.29 (copyright page not in the extraction; place and year not verified).",
 'u2_Sikri2019b': "Sikri VK. Regenerative endodontics. In: Essentials of endodontics. 2nd ed. New Delhi: CBS Publishers; 2019. Ch.38.",
 'u2_Widbiller2024': "Widbiller M, Galler KM. Regenerative endodontics. In: Duncan HF, El-Karim IA, editors. Vital pulp treatment. Hoboken (NJ): Wiley Blackwell; 2024. Ch.9.",
 'u2_Orstavik2020': "Ørstavik D. Endodontic treatment of apical periodontitis. In: Ørstavik D, editor. Essential endodontology: prevention and treatment of apical periodontitis. 3rd ed. Hoboken (NJ): Wiley Blackwell; 2020. Ch.11.",
 'u2_Azim2022': "Azim AA, Aksel H. Root canal obturation. In: Siqueira JF Jr, Rôças IN, editors. Treatment of endodontic infections. 2nd ed. Berlin: Quintessenz; 2022. Ch.15.",
 'u2_Murray2012': "Murray PE, García-Godoy F. Stem cells and regeneration of the pulpodentin complex. In: Hargreaves KM, Goodis HE, Tay FR, editors. Seltzer and Bender's dental pulp. 2nd ed. Chicago: Quintessence; 2012. Ch.5.",
 'u2_Andreasen2007': "Andreasen JO, Andersson L, Tsukiboshi M. Autotransplantation of teeth to the anterior region. In: Andreasen JO, Andreasen FM, Andersson L, editors. Textbook and color atlas of traumatic injuries to the teeth. 4th ed. Oxford: Blackwell Munksgaard; 2007. Ch.27.",
}
LIT = {}
L = {
 # --- Walton & Torabinejad 2002, Part 22 ---
 'u2_w_3yr': ('u2_wal22', 'Apical closure occurs approximately 3 years after eruption'),
 'u2_w_cort': ('u2_wal22', 'It is normal for a radiolucent area with a corticated margin to surround the developing open apex'),
 'u2_w_contra': ('u2_wal22', 'All vertical and most horizontal root fractures'),
 'u2_w_ankyl': ('u2_wal22', 'Replacement resorption (ankylosis)'),
 'u2_w_short': ('u2_wal22', 'Very short roots'),
 'u2_w_perio': ('u2_wal22', 'Marginal periodontal breakdown'),
 'u2_w_ind': ('u2_wal22', 'Root-end closure is required for a restorable immature tooth with pulp necrosis'),
 'u2_w_alt': ('u2_wal22', 'Alternative treatments include (1) apical plug, (2) root canal treatment, (3) periapical surgery, and (4) extraction'),
 'u2_w_surg': ('u2_wal22', 'Surgical intervention is possible but is best avoided in children'),
 'u2_w_mistaken': ('u2_wal22', 'in the mistaken belief that it stimulates hard tissue formation'),
 'u2_w_critical': ('u2_wal22', 'The factors most critical to success are thorough debridement of the pulp space and a complete coronal seal'),
 'u2_w_hed': ('u2_wal22', 'The use of Hedstrom files is not advocated because their sharp flutes may perforate the thin fragile walls of dentin'),
 'u2_w_baso4': ('u2_wal22', 'Calcium hydroxide powder with barium sulfate added for radiopacity (9:1 ratio)'),
 'u2_w_4wk': ('u2_wal22', 'The patient is recalled in 4 to 6 weeks'),
 'u2_w_density': ('u2_wal22', 'the calcium hydroxide is changed only if radiographic density significantly decreases'),
 'u2_w_tactile': ('u2_wal22', 'A hard tissue barrier is often not visible radiographically but is detected tactically'),
 'u2_w_1wk': ('u2_wal22', 'Calcium hydroxide paste is placed in the canal for a period of 1 week to disinfect the root canal system'),
 'u2_w_34': ('u2_wal22', 'to create a 3- to 4-mm apical plug'),
 'u2_w_succ': ('u2_wal22', 'Presence of a calcific barrier across the apex as demonstrated by radiographs or, more often, by careful tactile probing with a file'),
 'u2_w_fail': ('u2_wal22', 'Continual loss of calcium hydroxide from the canal space, indicating persistent periradicular inflammation'),
 'u2_w_gran': ('u2_wal22', 'Down-growth of granulomatous tissue into the canal, manifested by bleeding when files are placed short of the apex'),
 'u2_w_bact': ('u2_wal22', 'usually fails because of one common cause: bacterial contamination'),
 'u2_w_4yr': ('u2_wal22', 'all patients should be recalled at 12-month intervals for 4 years'),
 'u2_w_trapped': ('u2_wal22', 'Infected necrotic material trapped in the barrier may contribute to these failures'),
 'u2_w_comp': ('u2_wal22', 'the pulp chamber should be partially filled with composite resin to strengthen the tooth'),
 # --- Walton & Torabinejad 2002, Part 25 ---
 'u2_w25_cerv': ('u2_wal25', 'Spontaneous cervical fractures often occur because of thin dentin walls'),
 'u2_w25_revasc': ('u2_wal25', 'Revascularization may occur in immature teeth with wide open apexes, but it is unpredictable'),
 # --- Current Therapy in Endodontics Ch.11 (Kim) ---
 'u2_ct_aae': ('u2_ct', 'teeth of a compliant patient with necrotic pulp, an immature apex, and pulp space not needed for post and core'),
 'u2_ct_1mm': ('u2_ct', 'should have an open apex with diameters bigger than 1.0 mm or 1.1 mm'),
 'u2_ct_1mg': ('u2_ct', 'had a detrimental effect on the survival of stem cells of the apical papilla in concentrations higher than 1 mg/mL'),
 'u2_ct_1000': ('u2_ct', 'The concentrations of commonly used antibiotic pastes for pulp regeneration are around 1000 mg/mL'),
 'u2_ct_low': ('u2_ct', 'calcium hydroxide or a low concentration of antibiotics (liquid form, 0.01–0.1 mg/mL)'),
 'u2_ct_mino8': ('u2_ct', 'in children who are younger than 8 years of age'),
 'u2_ct_fu': ('u2_ct', 'the increased root lengths and widths, and the return of a positive vitality response are assessed'),
 'u2_ct_box': ('u2_ct', 'Neither strengthens the root nor promotes further development'),
 'u2_ct_hist': ('u2_ct', 'showed bone-like and cementum-like tissues without odontoblasts and regenerated dentin'),
 # --- Ingle's 7th Ch.29 (Diogenes and Smith); the OCR replaces 'fi' by '1' and 'ff' by '2', kept as printed in the extraction ---
 'u2_i29_auth': ('u2_ingfm', 'Anibal R. Diogenes, Anthony J. Smith'),
 'u2_i28_auth': ('u2_ingfm', 'Shahrokh Shabahang'),
 'u2_i29_03': ('u2_ing29', 'vascularized tissue could be formed in teeth with an apical diameter of approximately 0.3 mm'),
 'u2_i29_1mg': ('u2_ing29', 'antibiotic paste at a combined concentration of antibiotics of no greater than 1 mg/ml'),
 'u2_i29_100ug': ('u2_ing29', 'at no more than 100 μg of each drug/mL'),
 'u2_i29_24': ('u2_ing29', 'second visit is scheduled 2 to 4 weeks after the'),
 'u2_i29_res': ('u2_ing29', '95% of the MTA apexi1cation and 77% of calcium hydroxide apexi1cation cases'),
 'u2_i29_surv': ('u2_ing29', 'was signi1cantly greater than that of teeth treated with calcium hydroxide (77%), but not di2erent from teeth treated with an MTA apical plug (95%)'),
 'u2_i29_len': ('u2_ing29', 'signi1cantly greater percentage increase in root length (14.9%) compared with teeth treated by either MTA apexi1cation (6.1%) or calcium hydroxide apexi1cation (0.4%)'),
 'u2_i29_90': ('u2_ing29', 'both procedures successfully resolve the signs and symptoms of disease in approximately 90% of patients'),
 'u2_i29_goal': ('u2_ing29', 'the primary therapeutic goal must be resolution of apical periodontitis while promoting the survival and function of the tooth'),
 # --- Sikri Ch.38 ---
 'u2_s38_goal1': ('u2_sik38', 'Elimination of symptoms along with'),
 'u2_s38_goal2': ('u2_sik38', 'increased root wall thickness and/or increased root length'),
 'u2_s38_goal3': ('u2_sik38', 'positive response to vitality testing'),
 'u2_s38_age': ('u2_sik38', 'Young patients (6–8 years of age) are preferred'),
 'u2_s38_1mm': ('u2_sik38', 'Ideally the size of the apical opening should be greater than 1.0 mm, though a few authors have observed successful ingrowth even with an apical opening as less as 0.3 mm'),
 'u2_s38_tap': ('u2_sik38', 'ciprofloxacin/metronidazole/minocycline (0.1 mg/mL)'),
 'u2_s38_1000': ('u2_sik38', 'Dilution of 1000 times'),
 'u2_s38_chpref': ('u2_sik38', 'Calcium hydroxide is still a preferred choice'),
 'u2_s38_fu': ('u2_sik38', 'Radiographic evidence of bony healing (6–8 months)'),
 'u2_s38_fu2': ('u2_sik38', 'Radiographic evidence of root development (12–16'),
 'u2_s38_mta': ('u2_sik38', 'Place 3.0–4.0 mm of MTA over the collagen matrix'),
 # --- Grossman Ch.12 (new phrases, existing source) ---
 'u2_g12_goal1': ('q02_gr12', 'Primary goal: Elimination of symptoms and the evidence'),
 'u2_g12_goal3': ('q02_gr12', 'Tertiary goal: Positive response to vitality testing'),
 'u2_g12_succ': ('q02_gr12', 'Radiographic detection of a new PDL along the inner wall'),
 'u2_g12_fail': ('q02_gr12', 'Insufficient bleeding during the procedure'),
 'u2_g12_calc': ('q02_gr12', 'Root canal calcification/obliteration'),
 # --- Vital Pulp Treatment Ch.9 (Widbiller and Galler) ---
 'u2_v_nolonger': ('u2_vpt', 'several disadvantages come with this treatment that make it no longer the preferred option'),
 'u2_v_plug': ('u2_vpt', 'the current recommendation for immature teeth is to place an apical plug with HCSC'),
 'u2_v_stage': ('u2_vpt', 'From stage 4, the root has sufficient stability for both regenerative endodontic approaches and an apical barrier'),
 'u2_v_third': ('u2_vpt', 'can be expected in about one-third of cases'),
 'u2_v_asa': ('u2_vpt', 'Patients with severe general medical impairment (ASA 3 or higher)'),
 'u2_v_naocl': ('u2_vpt2', 'A concentration of 1.5–3% is recommended'),
 'u2_v_2mm': ('u2_vpt2', 'The blood should reach approximately 2 mm below the cemento-enamel junction'),
 'u2_v_hed30': ('u2_vpt2', 'a pre-bent ISO 30 Hedström file'),
 'u2_v_fu': ('u2_vpt2', 'Follow-up visits are recommended after 6, 12, 18 and 24 months and then annually for five years'),
 'u2_v_ortho': ('u2_vpt2', 'bony healing should be observed before tooth movement is started'),
 'u2_v_nodiff': ('u2_vpt2', 'there is no significant difference between apexification, apical plug and revitalization in terms of periapical healing and tooth survival'),
 'u2_v_poor': ('u2_vpt2', 'restoration of tooth sensitivity (tertiary goal) is poor'),
 'u2_v_bact': ('u2_vpt2', 'Persistent bacteria are a major cause of treatment failure'),
 'u2_v_chlong': ('u2_vpt2', 'should not be left in place for too long, as this may induce the formation of an calcified barrier'),
 # --- Essential Endodontology Ch.11 (Ørstavik) ---
 'u2_ee_trauma': ('u2_ee', 'may respond better to regenerative treatments than traumatized teeth'),
 'u2_ee_true': ('u2_ee', 'This is still experimental at best'),
 'u2_ee_apexog': ('u2_ee', 'the primary goal is to stimulate completion of apexogenesis'),
 'u2_ee_similar': ('u2_ee', 'bioceramic materials applied in a single visit give similar results'),
 'u2_ee_retrauma': ('u2_ee', 'The risk of a new trauma is increased in children with a previous history of oral trauma'),
 # --- Treatment of Endodontic Infections Ch.15 (Azim and Aksel) ---
 'u2_tei_36': ('u2_tei', 'The technique relies on the placement of MTA in the apical 3 to 6 mm of the canal'),
 'u2_tei_bc': ('u2_tei', 'More recent materials such as BC putty (Brasseler USA) have been used for the same purpose'),
 'u2_tei_crown': ('u2_tei', 'care should be taken to avoid placing MTA close to the clinical crown in order to avoid tooth discoloration'),
 'u2_tei_etch': ('u2_tei', 'should avoid etching over MTA'),
 # --- Seltzer & Bender Ch.5 (Murray and García-Godoy) ---
 'u2_sb_11': ('u2_sb5', 'avulsed teeth with an apical opening of approximately 1.1 mm or'),
 'u2_sb_source': ('u2_sb5', 'the source of the regenerated tissue has not'),
 # --- Andreasen atlas Ch.27 (Andreasen, Andersson and Tsukiboshi) ---
 'u2_a27_auth': ('u2_and27', 'J. O. Andreasen, L. Andersson & M. Tsukiboshi'),
 'u2_a27_alt': ('u2_and27', 'providing a realistic treatment alternative for tooth replacement in young individuals'),
 'u2_a27_age': ('u2_and27', 'the patient group best suited for this procedure is from'),
 'u2_a27_1013': ('u2_and27', '10 to 13 years old'),
 'u2_a27_impl': ('u2_and27', 'Implants are contraindicated in growing patients because they interfere with the growth of the alveolar process'),
 'u2_a27_bone': ('u2_and27', 'both the lost tooth and the atrophied alveolar process can be replaced'),
 'u2_a27_graft': ('u2_and27', 'second mandibular premolars, canines, first mandibular premolars, second maxillary premolars and diminutive third molars'),
 'u2_a27_5yr': ('u2_and27', '5-year graft survival: 98–99%'),
 'u2_a27_10yr': ('u2_and27', '10-year graft survival: 87–95%'),
 # --- new phrases in books already used (support for exam-core statements that had none) ---
 'u2_bak_intro': ('q02_bak', 'resulting in a tooth with thin, fragile root canal walls and an open apex'),
 'u2_bak_loss': ('q02_bak', 'If left untreated, the end result is loss of the tooth'),
 'u2_bak_resorp': ('q02_bak', 'frequently become infected, which promotes root resorption and periradicular disease'),
 'u2_prog_15': ('q02_prog', 'Passive irrigation with 1.5 % NaOCl for 15–20 min is recommended'),
 'u2_prog_612': ('q02_prog', 'is recommended at 6 and 12 months postoperatively and continued on a yearly or biyearly basis'),
 'u2_c12_needle': ('q02_c12', 'with irrigating needle positioned approximately 1 mm from root end'),
 'u2_c21_sealer': ('q02_c21', 'Sealer and softened filling material are expressed'),
 'u2_gl_regen2': ('q02_gl2', 'including dentin and root structures, as well as cells of the pulpdentin complex'),
 'u2_bio_ph3h': ('q02_bio', 'a high pH (10.2–12.5 three hours after setting)'),
 'u2_cv_rubber': ('q02_cvek', 'a palatal gingivectomy may be necessary to allow adaptation of a rubber dam'),
}
