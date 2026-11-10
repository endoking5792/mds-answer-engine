# Locators for Q07 "Write about various methods of caries diagnosis and add a note on recent advances" (20m). All keys prefixed q07_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
O = T + 'Operative_and_Dental_Materials_Textbooks/'
DET = O + 'Detection_and_Assessment_of_Dental_Caries.md'
F_EXTRA = {
 # Detection and Assessment of Dental Caries (Ferreira Zandona and Longbottom, eds, Springer 2019). Offsets checked per chapter:
 # Ch.1 offset 9: PDF 10 printed 1, PDF 11 printed 2.
 'q07_d1': (DET, 9, 'Ferreira Zandona and Longbottom, 2019'),
 # Ch.2 offset 7: PDF 14 printed 7, PDF 16 printed 9, PDF 20 printed 13.
 'q07_d2': (DET, 7, 'Longbottom and Ferreira Zandona, 2019'),
 # Ch.5 offset 6: PDF 41 printed 35, PDF 43 printed 37.
 'q07_d5': (DET, 6, 'Machiulskiene, 2019'),
 # Ch.6 offset 5: PDF 50 printed 45, PDF 51 printed 46, PDF 55 printed 50.
 'q07_d6': (DET, 5, 'Ekstrand and Braga, 2019'),
 # Ch.7 offset 4: PDF 62 printed 58, PDF 63 printed 59, PDF 66 printed 62.
 'q07_d7': (DET, 4, 'Zeller, Young and Novy, 2019'),
 # Ch.11 offset 1: PDF 110 printed 109, PDF 111 printed 110.
 'q07_d11': (DET, 1, 'Schwendicke and Göstemeyer, 2019'),
 # Ch.14 offset 0: PDF 139 printed 139, PDF 140 printed 140.
 'q07_d14': (DET, 0, 'Hogan, Pretty and Ellwood, 2019'),
 # Ch.15 offset 0: PDF 151 printed 151, PDF 153 printed 153.
 'q07_d15': (DET, 0, 'Kühnisch, 2019'),
 # Ch.16 offset 0: PDF 159 printed 159, PDF 160 printed 160.
 'q07_d16': (DET, 0, 'Kim, 2019'),
 # Ch.17 offset 0: PDF 171 printed 171, PDF 174 printed 174.
 'q07_d17': (DET, 0, 'Neuhaus and Lussi, 2019'),
 # Ch.18 offset -1: PDF 176 printed 177, PDF 177 printed 178.
 'q07_d18': (DET, -1, 'Amaechi, 2019'),
 # Ch.20 offset -3: PDF 198 printed 201, PDF 199 printed 202 (chapter opens PDF 196 = printed 199).
 'q07_d20': (DET, -3, 'Fried, 2019'),
 # Ch.23 offset -4: PDF 223 printed 227, PDF 224 printed 228.
 'q07_d23': (DET, -4, 'Fontana and Huysmans, 2019'),
 # Ch.26 offset -7: PDF 241 printed 248, PDF 242 printed 249.
 'q07_d26': (DET, -7, 'Huysmans, 2019'),
 # Kidd and Fejerskov, Essentials of Dental Caries 4th (OUP 2016), Ch.3. Offset 13: PDF 62 printed 49, PDF 64 printed 51, PDF 80 printed 67.
 'q07_kid': (O + 'Essentials_of_Dental_Caries_4th.md', 13, 'Kidd and Fejerskov, 2016'),
 # Summitt's 4th (2013) Ch.5 (Amaechi, van Amerongen, van Loveren, Kidd); file has no printed page numbers.
 'q07_sum': (O + 'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Amaechi et al., 2013'),
 # Sturdevant's 2nd South Asia ed Ch.3; no chapter byline (contributors list names Boushell, Shugars, Eidson), editors cited as in earlier topics. Offset 19: PDF 106 printed 87, PDF 107 printed 88, PDF 114 printed 95.
 'q07_stu': (O + 'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter et al., 2019'),
 # Mount 3rd (Wiley 2016) Ch.2 (Mount, Ngo, Hume, Wolff). Offset 16: PDF 41 printed 25, PDF 42 printed 26.
 'q07_mnt': (O + 'Preservation_and_Restoration_of_Tooth_Structure_Mount.md', 16, 'Mount et al., 2016'),
 # Harpreet Singh, Essentials of Preclinical Conservative Dentistry 2nd (Wolters Kluwer India 2020) Ch.5. Offset 17: PDF 52 printed 35, PDF 57 printed 40.
 'q07_sgh': (O + 'Essentials_of_Preclinical_Conservative_Dentistry_Harpreet_Singh.md', 17, 'Singh, 2020'),
}
BOOK_EXTRA = {}
L = {
 # definitions: detection vs diagnosis
 'q07_d26_diag': ('q07_d26', 'The human professional summation of all relevant information regarding history, signs and symptoms, test results, and probable causes'),
 'q07_kid_det': ('q07_kid', 'Is a lesion present? This is detection of the lesion'),
 'q07_kid_diag': ('q07_kid', 'adding the aspect of activity to detection, is diagnosis'),
 'q07_kid_cav': ('q07_kid', 'Is the surface of the lesion intact or is a cavity present?'),
 # prerequisites
 'q07_d2_cdi': ('q07_d2', 'they should be: clean, dry (dried), and well-illuminated'),
 'q07_d2_ri': ('q07_d2', 'the refractive index of enamel (1.6) and that of air (1.0)'),
 'q07_d2_water': ('q07_d2', 'water (refractive index 1.3)'),
 'q07_d2_5s': ('q07_d2', '5 s of air-drying per surface will highlight the optical changes'),
 'q07_sum_wet': ('q07_sum', 'A white spot lesion visible on a wet tooth surface indicates that demineralization is over halfway through the enamel'),
 'q07_sum_dry': ('q07_sum', 'A white spot lesion that becomes visible only after thorough air drying will be less than halfway through enamel'),
 # tactile
 'q07_stu_cpitn': ('q07_stu', 'Community Periodontal Index of Treatment Needs (CPITN) probe having a 0.5 mm sphere at the tip'),
 'q07_stu_contra': ('q07_stu', 'is contraindicated as a part of the caries detection process'),
 'q07_d2_probe': ('q07_d2', 'has been shown to be of no diagnostic value'),
 'q07_d5_sharp': ('q07_d5', 'sharp dental explorer is a more helpful supplementary tool for the evaluation of the surface morphology than a ball-ended probe'),
 'q07_kid_sharp': ('q07_kid', 'a sharp probe is useful in diagnosis'),
 # magnification
 'q07_sum_mag': ('q07_sum', 'the accuracy of visual caries detection can be improved 50% with the use of a magnifying device'),
 'q07_d2_mag': ('q07_d2', 'is surprisingly limited and has produced some mixed results'),
 # history
 'q07_sgh_hist': ('q07_sgh', 'Such factors include age, fluoride exposure, smoking habits, dietary habits, economic and educational status and general health'),
 # radiography
 'q07_d11_sens': ('q07_d11', 'bitewing radiography has a sensitivity of around 0.2–0.3 for early lesions'),
 'q07_d11_sens2': ('q07_d11', 'sensitivity increases to 0.4–0.6 for more advanced (dentin) lesions'),
 'q07_d11_spec': ('q07_d11', 'The specificity is around or above 0.9'),
 'q07_d11_ed': ('q07_d11', 'discriminating the outer and inner enamel half (E1, E2) and the outer, middle and inner dentin third (D1-3)'),
 'q07_kid_act': ('q07_kid', 'it can make no judgement about activity'),
 'q07_kid_cavrx': ('q07_kid', 'The technique cannot judge the presence or absence of a cavity'),
 'q07_sum_under': ('q07_sum', 'Radiographs have been shown to underestimate the depth of the lesion'),
 # transillumination, separation
 'q07_d14_dark': ('q07_d14', 'Lesion appears dark on light background'),
 'q07_d14_orange': ('q07_d14', 'or bluish shadow within the tooth will often be observed'),
 'q07_d14_nonirr': ('q07_d14', 'FOTI offers a non-invasive, non-irradiating method of caries detection with no limitation on the frequency of use'),
 'q07_d2_sep': ('q07_d2', 'leaving it in place for 2–7 days'),
 # visual systems
 'q07_d6_codes': ('q07_d6', 'It was decided to expand the 5-score ERK-system to a 7-score-system'),
 'q07_d6_merge': ('q07_d6', '“Initial” (ICDAS scores 1 and 2), “Moderate” (ICDAS scores 3 and 4), and “Extensive” (ICDAS scores 5 and 6)'),
 'q07_d6_kappa': ('q07_d6', 'The pooled intra- and inter-reproducibility in terms of kappa values were 0.67 or above'),
 'q07_d5_basis': ('q07_d5', 'the Nyvad criteria are based on the patho-anatomical surface characteristics of the caries lesions, rather than on the depth of lesion penetration'),
 'q07_d7_cats': ('q07_d7', 'The ADA CCS categories of sound, initial, moderate, and advanced'),
 # recent advances
 'q07_sgh_list': ('q07_sgh', 'Electrical conductance measurement'),
 'q07_d14_difoti': ('q07_d14', 'DIFOTI utilises a CCD sensor, effectively replacing the human eye with a grey scale camera, which allows for image capture and storage'),
 'q07_d15_780': ('q07_d15', 'emits near-infrared light with a wavelength of ~780 nm'),
 'q07_d15_99': ('q07_d15', 'the registered sensitivity (99%)'),
 'q07_d16_both': ('q07_d16', 'The QLF technology can measure both the mineral content as a fluorescence loss and bacterial activity as a red fluorescence simultaneously'),
 'q07_d16_405': ('q07_d16', 'blue visible light with a wavelength of 405 nm induces fluorescence'),
 'q07_d16_r': ('q07_d16', 'ΔF is strongly correlated with lesion depths as obtained using transverse microradiography (TMR) (r = 0.88)'),
 'q07_d17_655': ('q07_d17', 'Both devices operate at a wavelength of 655 nm'),
 'q07_d17_porph': ('q07_d17', 'which induces fluorescence of bacterial porphyrins'),
 'q07_d17_099': ('q07_d17', 'a digital value between 0 and 99'),
 'q07_mnt_ecm': ('q07_mnt', 'As porosity increases, so does conductance'),
 'q07_d18_ptr': ('q07_d18', 'Photothermal Radiometry and Luminescence (PTR-LUM) technology'),
 'q07_d18_5mm': ('q07_d18', 'examine up to 5 mm below the tooth surface'),
 'q07_d20_oct': ('q07_d20', 'Optical coherence tomography (OCT) is a noninvasive technique for creating cross-sectional images of internal biological structure'),
 'q07_d20_res': ('q07_d20', 'with an axial (depth) resolution exceeding 10 μm'),
 'q07_sum_digital': ('q07_sum', 'digital intraoral radiographs appear to be as accurate as film radiographs for the detection of dental caries'),
 # books differ on devices
 'q07_kid_research': ('q07_kid', 'So far they only have research interest'),
 'q07_d17_primary': ('q07_d17', 'supports the device’s use in primary care dentistry'),
 'q07_stu_fp': ('q07_stu', 'the increased likelihood of false-positive diagnoses limits its usefulness as a principal diagnostic method'),
 # clinical significance
 'q07_d1_support': ('q07_d1', 'methods should support visual examination and not be used in place of visual examination'),
 'q07_d1_licence': ('q07_d1', 'it is not a license to increase surgical intervention'),
 'q07_d23_arr': ('q07_d23', 'Arrested caries lesions do not require caries interventions'),
 'q07_d23_nc': ('q07_d23', 'Non-cavitated active lesions should be treated using evidence-based non-restorative methods'),
 'q07_d23_cav': ('q07_d23', 'Most cavitated lesions are non-cleansable, and thus active'),
}
