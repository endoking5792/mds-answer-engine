# Locators for Q17 "Diagnosis of Proximal Caries." (5m). All keys prefixed q17_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
O = T + 'Operative_and_Dental_Materials_Textbooks/'
DET = O + 'Detection_and_Assessment_of_Dental_Caries.md'
F_EXTRA = {
 # Kidd and Fejerskov 4th (OUP 2016) Ch.3. Offset 13: PDF 78 printed 65, PDF 80 printed 67, PDF 84 printed 71.
 'q17_kid': (O + 'Essentials_of_Dental_Caries_4th.md', 13, 'Kidd and Fejerskov, 2016'),
 # Harpreet Singh 2nd (2020) Ch.5-6. Offset 17: PDF 57 printed 40, PDF 64 printed 47.
 'q17_sgh': (O + 'Essentials_of_Preclinical_Conservative_Dentistry_Harpreet_Singh.md', 17, 'Singh, 2020'),
 # Summitt's 4th (2013) Ch.5 (Amaechi, van Amerongen, van Loveren, Kidd); no printed page numbers.
 'q17_sum': (O + 'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Amaechi et al., 2013'),
 # Detection and Assessment of Dental Caries (Springer 2019): Ch.2 offset 7 (PDF 20 p13, PDF 21 p14); Ch.3 offset 7 (PDF 24 p17, PDF 30 p23);
 # Ch.7 offset 4 (PDF 62 p58, PDF 66 p62); Ch.11 offset 1 (PDF 110 p109, PDF 111 p110); Ch.15 offset 0 (PDF 151 p151); Ch.17 offset 0 (PDF 171 p171).
 'q17_d2': (DET, 7, 'Longbottom and Ferreira Zandona, 2019'),
 'q17_d3': (DET, 7, 'Cortés, Martignon and Douglas, 2019'),
 'q17_d7': (DET, 4, 'Zeller, Young and Novy, 2019'),
 'q17_d11': (DET, 1, 'Schwendicke and Göstemeyer, 2019'),
 'q17_d15': (DET, 0, 'Kühnisch, 2019'),
 'q17_d17': (DET, 0, 'Neuhaus and Lussi, 2019'),
}
BOOK_EXTRA = {}
L = {
 'q17_kid_site': ('q17_kid', 'it forms just cervical to the contact area and vision may be obscured by the adjacent tooth'),
 'q17_kid_pink': ('q17_kid', 'it may be seen as a pinkish-grey area shining up through the marginal ridge'),
 'q17_kid_probe': ('q17_kid', 'A sharp, curved probe can be used gently to try to determine if an approximal lesion is cavitated'),
 'q17_kid_cav': ('q17_kid', 'The technique cannot judge the presence or absence of a cavity'),
 'q17_kid_act': ('q17_kid', 'it can make no judgement about activity'),
 'q17_sgh_best': ('q17_sgh', 'For viewing proximal caries, bitewing radiograph is considered as the best'),
 'q17_sgh_6080': ('q17_sgh', '60–80% of initial proximal lesions with radiolucencies in the outer one-third of the dentin do not show cavitation'),
 'q17_sgh_2040': ('q17_sgh', 'where the probability of cavitation is around 20–40%'),
 'q17_d11_sens': ('q17_d11', 'bitewing radiography has a sensitivity of around 0.2–0.3 for early lesions'),
 'q17_d11_spec': ('q17_d11', 'The specificity is around or above 0.9'),
 'q17_d11_ed': ('q17_d11', 'discriminating the outer and inner enamel half (E1, E2) and the outer, middle and inner dentin third (D1-3)'),
 'q17_d7_none': ('q17_d7', 'none of the teeth presenting a radiolucency in the outer one-half of the enamel were cavitated'),
 'q17_d7_409': ('q17_d7', 'These percentages increased to 40.9% in permanent teeth'),
 'q17_d7_100': ('q17_d7', 'to 100% cavitation in permanent teeth'),
 'q17_d2_sep': ('q17_d2', 'leaving it in place for 2–7 days'),
 'q17_d3_07': ('q17_d3', 'This procedure can create a space of around 0.7 mm between teeth'),
 'q17_sum_foti': ('q17_sum', 'For detection of proximal lesions in anterior teeth, the fiber-optic transillumination technique is particularly appropriate and convenient'),
 'q17_sum_holder': ('q17_sum', 'Radiographs should be obtained using a film holder and beam- aiming device'),
 'q17_d15_780': ('q17_d15', 'emits near-infrared light with a wavelength of ~780 nm'),
 'q17_d17_pen': ('q17_d17', 'a pen-type DIAGNOdent device was developed for approximal sites as well'),
}
