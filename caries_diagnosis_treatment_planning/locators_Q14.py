# Locators for Q14 "Laser fluorescence-based methods of caries detection" (10m). All keys prefixed q14_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
B = T + 'Operative_and_Dental_Materials_Textbooks/'
F_EXTRA = {
 # Detection and Assessment of Dental Caries (2019) Ch.17 DIAGNOdent, Neuhaus and Lussi. Offset 0 confirmed at PDF 172 (printed 172) and PDF 174 (printed 174).
 'q14_dd': (B+'Detection_and_Assessment_of_Dental_Caries.md', 0, 'Neuhaus and Lussi, 2019'),
 # Lasers in Dentistry - Current Concepts 2nd ed (2023) Ch.6, Muruppel and Fried. Offset 9 confirmed at PDF 138 (printed 129) and PDF 155 (printed 146).
 'q14_las': (B+'Lasers_in_Dentistry_Current_Concepts.md', 9, 'Muruppel and Fried, 2023'),
 # Sikri VK, Textbook of Conservative and Restorative Dentistry (CBS, eBook 2020) Ch.7. Offset 19 confirmed at PDF 134 (printed 115) and PDF 145 (printed 126).
 'q14_sik': (B+'Textbook_of_Conservative_and_Restorative_Dentistry.md', 19, 'Sikri, 2020'),
 # Modern Operative Dentistry (2020) Ch.3 Cariology, Caneppele et al. Offset 14 confirmed at PDF 115 (printed 101) and PDF 120 (printed 106).
 'q14_tor': (B+'Modern_Operative_Dentistry.md', 14, 'Caneppele et al., 2020'),
 # Sturdevant's Art and Science of Operative Dentistry 2nd South Asia ed (2019) Ch.3; no chapter author, editors Ritter, Boushell and Walter cited. Offset 19 confirmed at PDF 102 (printed 83) and PDF 113 (printed 94).
 'q14_stu': (B+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter, Boushell and Walter, 2019'),
 # Detection and Assessment of Dental Caries (2019) Ch.10 FACE, Lennon and Buchalla. Offset 2 confirmed at PDF 101 (printed 99) and PDF 102 (printed 100).
 'q14_face': (B+'Detection_and_Assessment_of_Dental_Caries.md', 2, 'Lennon and Buchalla, 2019'),
}
L = {
 # history and principle
 'q14_650': ('q14_dd', 'caries emits fluorescence when activated with red light at the wavelength of about 650 nm'),
 'q14_late90': ('q14_dd', 'The DIAGNOdent device was consequently developed in the late 1990s for assessment of occlusal sites'),
 'q14_pen': ('q14_dd', 'In the early 2000s a pen-type DIAGNOdent device was developed for approximal sites as well'),
 'q14_655': ('q14_dd', 'Both devices operate at a wavelength of 655 nm'),
 'q14_porph': ('q14_dd', 'induces fluorescence of bacterial porphyrins'),
 'q14_corr': ('q14_dd', 'The intensity of caries fluorescence is correlated with the intensity of bacterial contamination, i.e., with lesion depth'),
 'q14_2nd': ('q14_dd', 'intended to act as a second opinion device in case of questionable occlusal and proximal surfaces'),
 'q14_lz_hibst': ('q14_las', 'This technique was developed based on the work of Hibst and Gall'),
 'q14_lz_680': ('q14_las', 'measures fluorescence intensity (uses a 680 nm filter)'),
 'q14_lz_pp': ('q14_las', 'protoporphyrin IX and coporphyrin IX released by bacteria'),
 # technique
 'q14_clean': ('q14_dd', 'Remnants of several prophylaxis pastes, but also calculus give a false positive fluorescence signal'),
 'q14_calib': ('q14_dd', 'each tip needs to be calibrated separately against a ceramic standard before clinical use'),
 'q14_healthy': ('q14_dd', 'calibrated against a healthy aspect of the tooth before assessing the occlusal surface'),
 'q14_tilt': ('q14_dd', 'make a circular movement of your wrist in order to tilt the tip on the same spot'),
 'q14_099': ('q14_dd', 'a digital value between 0 and 99'),
 'q14_peak': ('q14_dd', 'holder function remembers the highest fluorescence value'),
 'q14_two': ('q14_dd', 'Take down the higher peak value of the two measurements'),
 # cut-offs
 'q14_cut_s': ('q14_dd', 'Sound 0–13 (0–4) 0–12 (0–6) 0–7 (0–6)'),
 'q14_cut_e': ('q14_dd', 'Enamel caries 14–20 (5–10) 13–25 (6–17) 8–16 (7–15)'),
 'q14_cut_d': ('q14_dd', 'Dentin caries >20 (>10) >25 (>17) >16 (>15)'),
 'q14_lz_scale': ('q14_las', 'correlated to the extent of caries (5–25 enamel caries, dentin caries greater than 35)'),
 'q14_sk_range': ('q14_sik', 'This system has a range of –9 and 99'),
 'q14_sk_scale': ('q14_sik', 'Initiation of caries is from 0–9; caries of enamel is from 10–17'),
 # accuracy
 'q14_se_e': ('q14_dd', 'Enamel caries: 0.68–0.96'),
 'q14_se_d': ('q14_dd', 'Dentin caries: 0.67–0.81'),
 'q14_sp_e': ('q14_dd', 'Enamel caries: 0.6–0.85'),
 'q14_sp_d': ('q14_dd', 'Dentin Caries: 0.79–0.87'),
 'q14_tr_7974': ('q14_tor', 'It has a sensitivity to detect lesions in enamel on the occlusal surface of 79% and a specificity of 74%'),
 'q14_stu_fp': ('q14_stu', 'the increased likelihood of false-positive diagnoses limits its usefulness as a principal diagnostic method'),
 'q14_lz_aadc': ('q14_las', 'laser fluorescence can be used as an adjunct to traditional caries detection methods and not used as a primary diagnostic tool'),
 # limitations
 'q14_sec': ('q14_dd', 'For secondary caries detection, there is evidence that DIAGNOdent is not helpful'),
 'q14_root': ('q14_dd', 'The findings regarding the diagnostic performance for root caries are discouraging'),
 'q14_lz_root': ('q14_las', 'DIAGNOdent could be reliably used for detecting root caries with a high sensitivity'),
 'q14_pm': ('q14_dd', 'Punctual measurement (no images)'),
 'q14_cav': ('q14_dd', 'No detection of cavitation'),
 'q14_thick': ('q14_dd', 'Approximal tip too thick to assess tight contact areas'),
 'q14_tr_active': ('q14_tor', 'it is not capable to differentiate active from inactive lesions'),
 'q14_lz_lussi': ('q14_las', 'Diagnodent was not able to clearly differentiate between superficial and deep dentinal caries'),
 'q14_noion': ('q14_dd', 'Caries detection without ionizing radiation'),
 'q14_mon': ('q14_dd', 'Caries monitoring possible'),
 # related laser/LED fluorescence methods
 'q14_lz_488': ('q14_las', 'QLF uses a much shorter wavelength at 488 nm'),
 'q14_lz_dentin': ('q14_las', 'Diagnodent can be related to dentinal decay but QLF results cannot correlate with dentinal decay'),
 'q14_sk_488': ('q14_sik', 'blue green light of 488 nm wavelengths'),
 'q14_sk_dye': ('q14_sik', 'Demineralized tissues absorb dyes and fluoresce strongly'),
 'q14_midwest': ('q14_dd', 'An attempt was made to replace the red laser diode by a red LED'),
 'q14_midwest2': ('q14_dd', 'The device was found to have sufficient accuracy for occlusal dentin caries'),
 'q14_face': ('q14_face', 'This causes infected dentin to fluoresce red, while noninfected dentin fluoresces green'),
 'q14_face405': ('q14_face', 'the cavity is illuminated with a violet light (405 nm)'),
 'q14_tr_vista': ('q14_tor', 'emits violet light (405 nm) that stimulates bacterial metabolites, causing them to glow red'),
}
