# Auditor u3 (2026-11-08): endodontic-side audit of B06, B07, B09, P1, P2.
# Offsets confirmed: Gulabivala Ch.11 PDF 305=p.296, 306=p.297 (9); Ingle's Ch.15 PDF 380=p.428, 382=p.430 (-48);
# Endodontology Ch.42 PDF 350=p.333, 354=p.337 (17); Sikri Essentials Ch.27 PDF 510=p.489, 514=p.493 (21);
# Sikri Textbook Ch.32 PAGE 618=p.599 (19, as a1_tcr); Goldstein Ch.24 PAGE 819=p.784 (35); Powers PAGE 88 (12, as a2_pw).
_C = T + 'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/'
_O = T + 'Operative_and_Dental_Materials_Textbooks/'
F = {
 'u3_coh': (_C + '26_26_Bleaching_procedures.md', None, 'Setzer, 2021'),
 'u3_c18': (_C + '18_18_Root_resorption.md', None, 'Patel et al, 2021'),
 'u3_gul': (T + 'Endodontics_Kishor_Gulabivala_Yuan_Ling_Ng_4th_Ed_Mosby_2014_Chapterwise/11_11_Management_of_tooth_resorption.md', 9, 'Gulabivala and Ng, 2014'),
 'u3_i15': (T + 'Ingles_Endodontics_7th_Chapterwise/15_Chapter_15_Pathologic_Tooth_Resorption.md', -48, 'Andreasen, Heithersay and Bakland, 2019'),
 'u3_e42': (T + 'Endodontology_Chapterwise/42_42_Tooth_Resorption.md', 17, 'Baumann and Beer, 2010'),
 'u3_s27': (T + 'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/27_27_Root_Resorption.md', 21, 'Sikri, 2019'),
 'u3_sum': (_O + 'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Haywood, da Costa and Berry, 2013'),
 'u3_tcr': (_O + 'Textbook_of_Conservative_and_Restorative_Dentistry.md', 19, 'Sikri, 2020'),
 'u3_g24': (_O + 'Esthetics_in_Dentistry_Goldstein.md', 35, 'West et al, 2018'),
 'u3_stu': (_O + 'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter et al, 2019'),
 'u3_bon': (_O + 'A_Clinical_Guide_to_Applied_Dental_Materials.md', None, 'Bonsor and Pearson, 2013'),
 'u3_pw': (_O + 'Powers_Wataha_Dental_Materials_Properties_and_Manipulation.md', 12, 'Powers and Wataha, 2013'),
}
L = {
 # Cohen's Ch.26 reference list (basis of the 6-8% / 18-25% sentence)
 'u3_coh_friedman': ('u3_coh', 'Incidence of external root resorption and esthetic results in 58 bleached pulpless teeth'),
 'u3_coh_heith': ('u3_coh', 'Incidence of invasive cervical resorption in bleached root-filled teeth'),
 'u3_coh_95': ('u3_coh', 'The perborate ion comprises 95% of the molecule and provides close to 10% of the available oxygen'),
 # Summitt's animal-study sentence and its reference
 'u3_sum_animal': ('u3_sum', 'Animal studies have shown a cause-and-effect relationship between internal bleaching with 30%'),
 'u3_sum_madison': ('u3_sum', 'Madison S, Walton R. Cervical root resorption following bleaching of endodontically treated teeth'),
 # Cohen's Ch.18
 'u3_c18_succ': ('u3_c18', 'He reported a 100% success rate for class I and class II lesions, a 77.8% success rate for class III lesions, and a 12.5% success rate for class IV lesions'),
 'u3_c18_limit': ('u3_c18', 'A major limitation of the Heithersay classification is that it is valid only if the ECR lesion is confined to the proximal aspect of the tooth'),
 'u3_c18_ortho': ('u3_c18', 'Orthodontics was the most common appearing factor (45.7%)'),
 'u3_c18_pink': ('u3_c18', 'However, it is a relatively rare feature of ECR'),
 'u3_c18_tca': ('u3_c18', 'Once the resorptive tissue has been removed, the cavity may be treated with a 90% aqueous solution of trichloroacetic acid'),
 'u3_c18_101': ('u3_c18', 'He examined the prognosis of treatment in 101 cases of ECR in 94 patients'),
 # Gulabivala and Ng Ch.11
 'u3_gul_cause': ('u3_gul', 'internal bleaching agents may damage the cementum and initiate resorption'),
 'u3_gul_10pc': ('u3_gul', '10% of the population, dentine is not covered by cementum'),
 'u3_gul_plaque': ('u3_gul', 'The resorptive process is then sustained by subgingival plaque'),
 'u3_gul_outline': ('u3_gul', 'Nevertheless, the outline of the pulp and root canal can be distinguished through the resorptive lesion'),
 'u3_gul_pink': ('u3_gul', 'A pink spot will be present when the inflammatory tissue undermines the enamel of the crown'),
 'u3_gul_heith': ('u3_gul', 'A classification of invasive cervical resorption is given by Heithersay (1999)'),
 # Ingle's Ch.15
 'u3_i15_sole': ('u3_i15', 'bleaching as a sole factor was found in 4.5% of the patients studied'),
 'u3_i15_combo': ('u3_i15', 'for example, trauma and bleaching (7.7%)'),
 'u3_i15_ortho': ('u3_i15', 'orthodontic treatment (21.2%), followed by trauma (14%)'),
 'u3_i15_222': ('u3_i15', 'In a large clinical study of 222 patients (total of'),
 'u3_i15_cemento': ('u3_i15', 'a defect in the cementoblast layer seems to be a prerequisite'),
 'u3_i15_tca': ('u3_i15', 'followed by curettage, endodontic treatment, if indicated, and restoration'),
 'u3_i15_class4': ('u3_i15', 'as there was a low success rate for class 4 resorptions, no treatment can be generally recommended'),
 # Endodontology Ch.42
 'u3_e42_pred': ('u3_e42', 'intracoronal bleaching, trauma, orthodontics, dentoalveolar surgery, and periodontal treatment have been cited as potential predisposing factors'),
 'u3_e42_c1': ('u3_e42', 'Class I: A small resorptive lesion near the cervical area with shallow penetration into dentin'),
 'u3_e42_c4': ('u3_e42', 'Class IV: A large invasive resorptive process that has extended beyond the coronal third of the root'),
 'u3_e42_tca': ('u3_e42', 'topical application of a 90% aqueous solution of trichloroacetic acid (TCA) in the treatment of class I and II cases'),
 'u3_e42_fail': ('u3_e42', 'The treatment of class IV lesions has a high failure rate'),
 'u3_e42_extru': ('u3_e42', 'This problem may be overcome by orthodontic extrusion of the tooth before treatment'),
 # Sikri Essentials Ch.27
 'u3_s27_pred': ('u3_s27', 'Predisposing factors may include trauma, periodontal treatment, intracoronal bleaching'),
 'u3_s27_c2': ('u3_s27', 'Class 2: A well-defined invasive resorptive lesion that has penetrated close to the coronal pulp chamber'),
 'u3_s27_c3': ('u3_s27', 'Class 3: A deeper invasion of dentin by resorbing tissue, not only involving the coronal dentin, but also extending into the coronal third of the root'),
 'u3_s27_transient': ('u3_s27', 'Mostly the cervical resorption defects are transient, which means, the cementum repair may occur within two to three weeks without any treatment'),
 'u3_s27_after': ('u3_s27', 'Heithersay recommended use of topical application of 90% trichloroacetic acid after curettage of chronic resorptive defect'),
 'u3_s27_table': ('u3_s27', 'Classes 1, 2: Topical application of 90% trichloracetic acid, curettage and glass ionomer cement restoration'),
 # Sikri Textbook of Conservative and Restorative Dentistry Ch.32
 'u3_tcr_barrier': ('u3_tcr', '0.5–1.0 mm thick calcium hydroxide/glass'),
 'u3_tcr_gp': ('u3_tcr', 'Approximately 2.0–3.0 mm of root canal restorative material is also removed'),
 'u3_tcr_wbtime': ('u3_tcr', 'over an extended period of time ranging from 24–48 hours to 7–10 days'),
 'u3_tcr_paste': ('u3_tcr', 'A thick paste of sodium perborate and superoxol (35% H2O2) is placed into the pulp chamber'),
 'u3_tcr_pressure': ('u3_tcr', 'pressure in the pulp chamber is required for bleaching'),
 'u3_tcr_combo': ('u3_tcr', 'This technique involves the combined use of thermocatalytic non-vital bleaching technique followed by walking bleach regimen'),
 'u3_tcr_2030': ('u3_tcr', 'ranging from not more than 20–30 minutes'),
 'u3_tcr_lieb': ('u3_tcr', 'Liebenberg (1997) administered intracoronal 10% carbamide peroxide gel in a splint'),
 # Goldstein Ch.24 (West et al)
 'u3_g24_48h': ('u3_g24', 'The maximum bleaching effect takes place within 48 h'),
 'u3_g24_23': ('u3_g24', 'usually two to three applications'),
 'u3_g24_alcohol': ('u3_g24', 'The chamber is washed with 70% alcohol'),
 'u3_g24_probe': ('u3_g24', 'Three periodontal probings are made and recorded: mesial, facial, and distal'),
 'u3_g24_shield': ('u3_g24', 'such as flowable composites, glass ionomers, and even Cavit'),
 'u3_g24_cavit': ('u3_g24', 'A 2 mm layer of Cavit is placed first around the rim'),
 'u3_g24_overnight': ('u3_g24', 'occasionally, a dramatic result happens overnight'),
 'u3_g24_cure': ('u3_g24', 'Light cure from the labial surface and then the lingual surface'),
 # Sturdevant's Ch.21
 'u3_stu_gp': ('u3_stu', 'to approximately 1–2 mm apical of the clinical crown'),
 'u3_stu_weekly': ('u3_stu', 'The sodium perborate should be changed weekly'),
 'u3_stu_5min': ('u3_stu', 'The area should remain isolated for approximately 5 min after closure to evaluate the adequacy of the seal'),
 # Bonsor and Pearson Ch.18
 'u3_bon_68': ('u3_bon', 'The prevalence is between 6% and 8% and it usually only affects non-vital teeth or those which have a history of trauma'),
 'u3_bon_30': ('u3_bon', 'The risk increases as the concentration of hydrogen peroxide rise above 30%'),
 'u3_bon_warn': ('u3_bon', 'Patients should be warned of the possibility of external cervical resorption prior to starting treatment'),
 'u3_bon_acetone': ('u3_bon', 'The reduction in bond strength is more marked when an acetone-based product is used instead of an ethanol'),
 'u3_bon_neutral': ('u3_bon', 'Carbamide peroxide at a low concentration has no effect on the surface or surface microhardness of enamel or dentine when used in a formulation with a neutral pH'),
 'u3_bon_etch': ('u3_bon', 'its effect is not as damaging as that caused when enamel is etched prior to bonding'),
 'u3_bon_existing': ('u3_bon', 'There is no evidence of any adverse effect of tooth whitening agent use on the bond strength of established bonded restorations'),
 'u3_bon_geno': ('u3_bon', 'it is known to be genotoxic in vitro but not in vivo'),
 'u3_bon_taste': ('u3_bon', 'The taste usually disappears after a couple of hours'),
 # Powers and Wataha Ch.6
 'u3_pw_rough': ('u3_pw', 'resin-modified glass ionomers, and glass ionomers have been roughened slightly by whitening gels'),
 'u3_pw_smear': ('u3_pw', 'Whitening agents should not come into contact with dentin because some products remove the smear layer'),
}
BOOK = {
 'Gulabivala2014': "Gulabivala K, Ng YL, editors. Endodontics. 4th ed. Edinburgh: Mosby Elsevier; 2014. Ch.11 Management of tooth resorption (chapter author not printed in the extracted file; cited under the editors).",
 'Andreasen2019': "Andreasen JO, Heithersay GS, Bakland LK. Pathologic tooth resorption. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.15 (author line decoded from a damaged OCR heading; verify against the printed book).",
 'Baumann2010res': "Baumann MA, Beer R, editors. Endodontology. 2nd ed. Stuttgart: Thieme; 2010. Ch.42 Tooth resorption (chapter author not stated in the extracted file; cited under the editors).",
 'Sikri2019res': "Sikri VK. Root resorption. In: Essentials of Endodontics. 2nd ed. New Delhi: CBS Publishers; 2019. Ch.27.",
}
