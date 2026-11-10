# Locators for Q09 "What is an incipient carious lesion? How will you detect and manage such lesions?" (20m). All keys prefixed q09_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
O = T + 'Operative_and_Dental_Materials_Textbooks/'
DET = O + 'Detection_and_Assessment_of_Dental_Caries.md'
F_EXTRA = {
 # Sturdevant's 2nd South Asia ed, Ch.2 (caries) and Ch.3 (examination); no chapter byline, editors cited as in earlier topics.
 # Offset 19: PDF 61 printed 42, PDF 62 printed 43 (Ch.2); PDF 106 printed 87, PDF 107 printed 88 (Ch.3).
 'q09_stu': (O + 'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter et al., 2019'),
 # Harpreet Singh 2nd (2020) Ch.5. Offset 17: PDF 52 printed 35, PDF 57 printed 40.
 'q09_sgh': (O + 'Essentials_of_Preclinical_Conservative_Dentistry_Harpreet_Singh.md', 17, 'Singh, 2020'),
 # Kidd and Fejerskov 4th (2016) Ch.2-3. Offset 13: PDF 36 printed 23, PDF 38 printed 25, PDF 64 printed 51.
 'q09_kid': (O + 'Essentials_of_Dental_Caries_4th.md', 13, 'Kidd and Fejerskov, 2016'),
 # Mount 3rd (2016) Ch.2 (Mount, Ngo, Hume, Wolff). Offset 16: PDF 41 printed 25, PDF 46 printed 30.
 'q09_mnt': (O + 'Preservation_and_Restoration_of_Tooth_Structure_Mount.md', 16, 'Mount et al., 2016'),
 # Summitt's 4th (2013) Ch.5 (Amaechi, van Amerongen, van Loveren, Kidd); no printed page numbers.
 'q09_sum': (O + 'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Amaechi et al., 2013'),
 # Detection and Assessment of Dental Caries (Springer 2019): Ch.2 offset 7 (PDF 14 p7, PDF 20 p13); Ch.3 offset 7 (PDF 24 p17, PDF 25 p18);
 # Ch.5 offset 6 (PDF 41 p35, PDF 44 p38); Ch.6 offset 5 (PDF 51 p46, PDF 55 p50); Ch.11 offset 1 (PDF 110 p109, PDF 111 p110);
 # Ch.16 offset 0 (PDF 159 p159); Ch.23 offset -4 (PDF 223 p227, PDF 227 p231).
 'q09_d2': (DET, 7, 'Longbottom and Ferreira Zandona, 2019'),
 'q09_d3': (DET, 7, 'Cortés, Martignon and Douglas, 2019'),
 'q09_d5': (DET, 6, 'Machiulskiene, 2019'),
 'q09_d6': (DET, 5, 'Ekstrand and Braga, 2019'),
 'q09_d11': (DET, 1, 'Schwendicke and Göstemeyer, 2019'),
 'q09_d16': (DET, 0, 'Kim, 2019'),
 'q09_d23': (DET, -4, 'Fontana and Huysmans, 2019'),
}
BOOK_EXTRA = {}
L = {
 # definition
 'q09_stu_def': ('q09_stu', 'incipient caries lesion is the first evidence of caries activity in enamel'),
 'q09_stu_chalky': ('q09_stu', 'appear as chalky white opaque areas on enamel when air-dried and seems to disappear when the tooth is rehydrated'),
 'q09_stu_rev': ('q09_stu', 'This lesion may be characterized as reversible'),
 'q09_stu_hard': ('q09_stu', 'the enamel surface is fairly hard, intact and smooth to the touch'),
 'q09_mnt_sub': ('q09_mnt', 'sub‐surface demineralization, with an intact surface; non‐cavitated'),
 'q09_d6_initial': ('q09_d6', '“Initial” (ICDAS scores 1 and 2)'),
 # histopathology
 'q09_stu_surf': ('q09_stu', 'It has a lower pore volume than the body of the lesion (<5%)'),
 'q09_stu_body': ('q09_stu', 'It has the largest pore volume, varying from 5% at the periphery to 25% at the centre'),
 'q09_stu_dark': ('q09_stu', 'The total pore volume is 2%–4%'),
 'q09_stu_trans': ('q09_stu', 'The translucent zone is the deepest zone and represents the advancing front of the enamel lesion'),
 'q09_stu_z1': ('q09_stu', 'Zone 1: Surface zone'),
 'q09_sgh_z1': ('q09_sgh', 'Zone 1: Translucent Zone'),
 'q09_sgh_cone': ('q09_sgh', 'cone-shaped lesion with the apex towards the dentinoenamel junction'),
 'q09_sgh_surf': ('q09_sgh', 'The surface layer is 20–100 µm thick'),
 'q09_kid_fl': ('q09_kid', 'an enamel surface covering a white spot lesion contains more fluoride than the surrounding sound, normal enamel'),
 'q09_stu_barrier': ('q09_stu', 'it serves as a barrier to bacterial invasion'),
 # differential diagnosis
 'q09_sum_hypo': ('q09_sum', 'white spot lesions from developmental hypomineralization usually have smooth and glossy surfaces like a sound enamel surface'),
 'q09_sum_bilat': ('q09_sum', 'Bilateral or multiple corresponding teeth'),
 'q09_sum_stag': ('q09_sum', 'Located in plaque stagnation areas'),
 'q09_sgh_hypo': ('q09_sgh', 'hypoplasia is visible in both dry and moist conditions'),
 # detection
 'q09_d2_cdi': ('q09_d2', 'they should be: clean, dry (dried), and well-illuminated'),
 'q09_d3_5s': ('q09_d3', 'prolonged air drying for around 5 s with the three-in-one air syringe'),
 'q09_sum_wet': ('q09_sum', 'A white spot lesion visible on a wet tooth surface indicates that demineralization is over halfway through the enamel'),
 'q09_sum_dry': ('q09_sum', 'A white spot lesion that becomes visible only after thorough air drying will be less than halfway through enamel'),
 'q09_sum_rev': ('q09_sum', 'the latter condition has a better chance of complete reversal, while the former condition may only be arrested'),
 'q09_d6_95': ('q09_d6', 'If the lesion is scored ICDAS 1, 95% shows no demineralization or the demineralization is restricted to the outer half of the enamel'),
 'q09_d6_83': ('q09_d6', 'A total of 83% of ICDAS 2 lesions are characterized to be histologically wise in the inner half of the enamel'),
 'q09_d2_micro': ('q09_d2', 'for non-cavitated lesions probing can irreversibly damage the tooth surface'),
 'q09_stu_cpitn': ('q09_stu', 'Community Periodontal Index of Treatment Needs (CPITN) probe having a 0.5 mm sphere at the tip'),
 'q09_d11_sens': ('q09_d11', 'bitewing radiography has a sensitivity of around 0.2–0.3 for early lesions'),
 'q09_mnt_rx': ('q09_mnt', 'The presence of an initial subsurface lesion may be determined from radiographs because of increased radiolucency in the subsurface tissue'),
 'q09_mnt_ti': ('q09_mnt', 'This may be confirmed by trans‐illumination in some cases'),
 'q09_mnt_sep': ('q09_mnt', 'after teeth have been separated for at least 24 hours using an orthodontic rubber band separator'),
 'q09_d16_mon': ('q09_d16', 'monitor its changes as numerical values'),
 # activity
 'q09_d5_act': ('q09_d5', 'Active enamel caries lesions are characterized by matt/chalky, whitish, or yellowish appearance'),
 'q09_d5_rough': ('q09_d5', 'They feel rough when explorer is gently moved across the surface'),
 'q09_d5_inact': ('q09_d5', 'inactive caries lesions are glossy and smooth on probing'),
 'q09_d5_gingiva': ('q09_d5', 'on the smooth surfaces, they are located at a distance from gingival margin'),
 'q09_d6_points': ('q09_d6', 'arrested lesions got at a maximum of 7 points, while active lesions achieved more than 7 points'),
 'q09_d6_prog': ('q09_d6', 'Initial lesions tended to progress 2–4 times more than sound surfaces'),
 # management principles
 'q09_d23_arr': ('q09_d23', 'Arrested caries lesions do not require caries interventions'),
 'q09_d23_nc': ('q09_d23', 'Non-cavitated active lesions should be treated using evidence-based non-restorative methods'),
 'q09_d6_nonop': ('q09_d6', 'Initial caries lesions can be arrested by using non-operative approaches'),
 'q09_mnt_ethic': ('q09_mnt', 'Surgical treatment when the sub‐surface of enamel is dem- ineralized but the surface remains intact is neither necessary nor ethical'),
 # management options
 'q09_mnt_diet': ('q09_mnt', 'dietary change, by decreasing the amount or frequency of sucrose in the diet'),
 'q09_mnt_chew': ('q09_mnt', 'increasing salivary flow rate through vigorous chewing sev- eral times a day'),
 'q09_mnt_floss': ('q09_mnt', 'decrease in plaque thickness by effective interdental oral hygiene'),
 'q09_sum_var': ('q09_sum', 'Fluoride varnishes contain a high level of fluoride (5% NaF, 22,600 ppm F)'),
 'q09_sum_var24': ('q09_sum', 'about two to four times per year, depending on the caries risk of the individual patient'),
 'q09_sum_3m': ('q09_sum', 'Application of the agent can be repeated every 3 months until caries activity is under control'),
 'q09_sum_gel': ('q09_sum', '1.23% acidulated phosphate fluoride or neutral 2% NaF'),
 'q09_sum_acp': ('q09_sum', 'ACP-based mouthrinses to promote remineralization of enamel subsurface lesions'),
 'q09_stu_seal': ('q09_stu', 'Incipient lesions in enamel not extending to the DEJ'),
 'q09_sum_sealprog': ('q09_sum', 'there is ample evidence that caries lesions do not progress as long as the fissure remains sealed'),
 'q09_sum_inf': ('q09_sum', 'caries infiltration occludes lesion pores with low-viscosity light-curing resins in order to create a diffusion barrier'),
 'q09_sum_hcl': ('q09_sum', 'Following etching of the lesion with hydrochloric acid and achievement of a dried surface using ethanol and air drying'),
 'q09_sum_31': ('q09_sum', 'the infiltrant is allowed to infiltrate the lesion for 3 minutes'),
 'q09_sum_1min': ('q09_sum', 'the infiltrant is allowed to infiltrate for only 1 minute'),
 'q09_sum_radiol': ('q09_sum', 'the current infiltrant is radiolucent'),
 'q09_sum_watch': ('q09_sum', '“Watchful waiting” implies that nothing is done'),
 # prognosis: reversal vs scar
 'q09_kid_scar': ('q09_kid', 'Most often a white spot lesion remains as a scar in the tooth'),
 'q09_kid_active': ('q09_kid', 'it will only be possible to reverse a lesion by starting the caries control measures while the lesion is in an active stage'),
 'q09_mnt_rest': ('q09_mnt', 'This outcome can be considered an excellent, natural, low‐solubility and permanent restoration'),
}
