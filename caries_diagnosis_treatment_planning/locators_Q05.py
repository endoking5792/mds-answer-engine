# Locators for Q05 "Enumerate the advances in the methods for diagnosing coronal caries and add a note on developments in Radiographic diagnosis of Dental caries." (25m). All keys prefixed q05_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
B = T + 'Operative_and_Dental_Materials_Textbooks/'
D = B + 'Detection_and_Assessment_of_Dental_Caries.md'
F_EXTRA = {
 # Detection and Assessment of Dental Caries (Ferreira Zandona and Longbottom, eds, 2019). Offsets per chapter, each confirmed at two pages:
 'q05_ek': (D, 5, 'Ekstrand and Braga, 2019'),          # Ch.6: PDF 50 (45), PDF 55 (50)
 'q05_ada': (D, 4, 'Zeller, Young and Novy, 2019'),     # Ch.7: PDF 62 (58), PDF 65 (61)
 'q05_dye': (D, 2, 'Maltz et al., 2019'),               # Ch.9: PDF 85 (83), PDF 97 (95)
 'q05_face': (D, 2, 'Lennon and Buchalla, 2019'),       # Ch.10: PDF 101 (99), PDF 102 (100)
 'q05_bw': (D, 1, 'Schwendicke and Göstemeyer, 2019'),  # Ch.11: PDF 110 (109), PDF 115 (114)
 'q05_dig': (D, 0, 'Göstemeyer and Schwendicke, 2019'), # Ch.12: PDF 119 (119), PDF 124 (124)
 'q05_cbct': (D, 0, 'Price, 2019'),                     # Ch.13: PDF 127 (127), PDF 135 (135)
 'q05_foti': (D, 0, 'Hogan, Pretty and Ellwood, 2019'), # Ch.14: PDF 139 (139), PDF 140 (140)
 'q05_nilt': (D, 0, 'Kühnisch, 2019'),                  # Ch.15: PDF 151 (151), PDF 153 (153)
 'q05_kim': (D, 0, 'Kim, 2019'),                        # Ch.16: PDF 159 (159), PDF 165 (165)
 'q05_dd': (D, 0, 'Neuhaus and Lussi, 2019'),           # Ch.17: PDF 172 (172), PDF 174 (174)
 'q05_can': (D, -1, 'Amaechi, 2019'),                   # Ch.18: PDF 176 (177), PDF 177 (178)
 'q05_nir': (D, -2, 'Fried, 2019a'),                    # Ch.19: PDF 187 (189), PDF 188 (190)
 'q05_oct': (D, -3, 'Fried, 2019b'),                    # Ch.20: PDF 196 (199), PDF 197 (200)
 'q05_us': (D, -3, 'Yanıkoğlu and Tağtekin, 2019'),     # Ch.21: PDF 206 (209), PDF 207 (210)
 'q05_bio': (D, -3, 'Longbottom and Vernon, 2019'),     # Ch.22: PDF 214 (217), PDF 215 (218)
 # Lasers in Dentistry - Current Concepts 2nd ed (2023) Ch.6, Muruppel and Fried. Offset 9: PDF 138 (129), PDF 155 (146).
 'q05_las': (B+'Lasers_in_Dentistry_Current_Concepts.md', 9, 'Muruppel and Fried, 2023'),
 # Modern Operative Dentistry (2020) Ch.3, Caneppele et al. Offset 14: PDF 115 (101), PDF 120 (106).
 'q05_tor': (B+'Modern_Operative_Dentistry.md', 14, 'Caneppele et al., 2020'),
 # Sikri, Textbook of Conservative and Restorative Dentistry (eBook 2020) Ch.7. Offset 19: PDF 134 (115), PDF 137 (118).
 'q05_sik': (B+'Textbook_of_Conservative_and_Restorative_Dentistry.md', 19, 'Sikri, 2020'),
 # Pickard's Manual of Operative Dentistry 9th ed (2011), Banerjee and Watson. Offset 11: PDF 38 (27), PDF 39 (28).
 'q05_pick': (B+'Pickards_Manual_of_Operative_Dentistry_9th.md', 11, 'Banerjee and Watson, 2011'),
 # Kidd and Fejerskov, Essentials of Dental Caries 4th ed (2016) Ch.3. Offset 13: PDF 70 (57), PDF 85 (72).
 'q05_kd': (B+'Essentials_of_Dental_Caries_4th.md', 13, 'Kidd and Fejerskov, 2016'),
 # Sturdevant 2e South Asia (2019) Ch.3, editors cited. Offset 19: PDF 102 (83), PDF 113 (94).
 'q05_stu': (B+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter, Boushell and Walter, 2019'),
 # Summitt's 4th ed (2013) Ch.5, Amaechi, van Amerongen, van Loveren and Kidd. No printed page numbers.
 'q05_sum': (B+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Amaechi et al., 2013'),
}
L = {
 # need for advances
 'q05_kim_2030': ('q05_kim', 'methods show low sensitivities of 20–30% in detecting minute changes in early caries'),
 'q05_las_30': ('q05_las', 'Radiographic detection often requires at least around 30% of demineralization to warrant detection'),
 'q05_sum_dx': ('q05_sum', 'caries diagnosis includes both caries detection and the assessment of lesion activity'),
 'q05_pick_4': ('q05_pick', 'four basic physical principles affecting mineralized dental tissues: optical light scattering, mineral density changes, fluorescent characteristics and tissue porosity'),
 'q05_stu_fda': ('q05_stu', 'The technologies currently approved by the FDA include laser-induced fluorescence, light-induced fluorescence, and alternating current (AC) impedance spectroscopy (ACIST)'),
 # visual systems
 'q05_ek_two': ('q05_ek', 'Detection wise, it is a two-digit scoring system'),
 'q05_ek_sesp': ('q05_ek', 'The pooled specificity and sensitivity were both 0.7'),
 # transillumination
 'q05_foti_dark': ('q05_foti', 'areas of porosity appear dark on a lighter background'),
 'q05_foti_sens': ('q05_foti', 'sensitivity scores of 21–96% and specificity scores of 74–88%'),
 'q05_tor_difoti': ('q05_tor', 'the diagnostic accuracy of DIFOTI in detecting early approximal enamel lesions is greater than that of film and digital radiography'),
 'q05_nilt_780': ('q05_nilt', 'emits near-infrared light with a wavelength of ~780 nm'),
 'q05_nilt_xfree': ('q05_nilt', 'novel X-ray-free imaging method'),
 'q05_tor_dcam': ('q05_tor', 'DIAGNOcam is more capable of detecting initial proximal lesions than digital radiography'),
 'q05_nir_1300': ('q05_nir', 'enamel is most transparent near λ = 1300 nm'),
 # fluorescence
 'q05_kim_def': ('q05_kim', 'Quantitative light-induced fluorescence (QLF) is a representative optical technology for early detection and quantification of dental caries'),
 'q05_dd_655': ('q05_dd', 'Both devices operate at a wavelength of 655 nm'),
 'q05_dd_porph': ('q05_dd', 'induces fluorescence of bacterial porphyrins'),
 'q05_dd_099': ('q05_dd', 'a digital value between 0 and 99'),
 'q05_dd_2nd': ('q05_dd', 'intended to act as a second opinion device'),
 'q05_tor_sopro': ('q05_tor', 'an intraoral camera that has blue LEDs capable to induce the autofluorescence'),
 'q05_face_405': ('q05_face', 'the cavity is illuminated with a violet light (405 nm)'),
 'q05_face_red': ('q05_face', 'This causes infected dentin to fluoresce red, while noninfected dentin fluoresces green'),
 # electrical
 'q05_las_ecm': ('q05_las', 'Electroconductivity measurement (ECM) is based on the principle that sound tooth surfaces will have little or no conductivity'),
 'q05_tor_ecm': ('q05_tor', 'the greater the demineralization degree of the enamel, the greater the electrical conductivity is'),
 'q05_las_acist': ('q05_las', 'grades that data into a numeral score (0–100)'),
 # others
 'q05_can_ptr': ('q05_can', 'The Canary System investigates the status of the tooth crystal structure by using Photothermal Radiometry and Luminescence (PTR-LUM) technology'),
 'q05_oct_def': ('q05_oct', 'Optical coherence tomography (OCT) is a noninvasive technique for creating cross-sectional images'),
 'q05_us_18': ('q05_us', 'high-frequency pulse-echo ultrasound waves (18 MHz) can distinguish an intact and demineralized enamel surface'),
 'q05_bio_ca': ('q05_bio', 'via a calcium-sensitive photoprotein'),
 'q05_bio_live': ('q05_bio', 'visualization of active enamel demineralization'),
 'q05_tor_mw': ('q05_tor', 'This method has shown its capability to diagnose 92% of the occlusal lesions and 80% of the proximal lesions'),
 'q05_dye_poor': ('q05_dye', 'dye staining is a rather poor indicator for the presence or absence of carious dentin'),
 # conventional bitewing
 'q05_bw_se1': ('q05_bw', 'bitewing radiography has a sensitivity of around 0.2–0.3 for early lesions'),
 'q05_bw_se2': ('q05_bw', 'sensitivity increases to 0.4–0.6 for more advanced (dentin) lesions'),
 'q05_bw_sp': ('q05_bw', 'The specificity is around or above 0.9'),
 'q05_tor_9559': ('q05_tor', 'the radiographic examination of the proximal surfaces has high specificity (95%) but only a moderate sensitivity (59%)'),
 'q05_kim_5040': ('q05_kim', 'bitewing radiography shows maximum sensitivities of 50% and 40% for proximal and early proximal caries'),
 'q05_bw_e1d3': ('q05_bw', 'outer and inner enamel half (E1, E2) and the outer, middle and inner dentin third (D1-3)'),
 'q05_bw_e1d1': ('q05_bw', 'E1-D1 lesions will be mainly managed non-restoratively'),
 'q05_bw_half': ('q05_bw', 'around half of the lesions radiographically extending into the outer dentin were cavitated'),
 'q05_bw_cav': ('q05_bw', 'Bitewing radiography does only seldomly allow for the detection of surface cavitation'),
 'q05_bw_holder': ('q05_bw', 'Using these holders ensures the exact same projection'),
 'q05_bw_risk': ('q05_bw', 'radiographs should be planned and taken not in regular, standardized intervals but risk-adjusted'),
 'q05_sum_under': ('q05_sum', 'Radiographs have been shown to underestimate the depth of the lesion'),
 'q05_ada_rad': ('q05_ada', 'RA1-RA3, RB4, and RC5-RC6'),
 # xeroradiography
 'q05_sik_xero': ('q05_sik', 'Xeroradiography uses xerographic copying techniques'),
 'q05_sik_xero2': ('q05_sik', 'Xeroradiography is twice as sensitive as conventional D-speed films'),
 'q05_sik_xero3': ('q05_sik', 'One-third of X-radiation is required'),
 # digital
 'q05_sik_rvg': ('q05_sik', 'direct digital radiography [Radiovisiography (RVG)]'),
 'q05_dig_ccd': ('q05_dig', 'solid-state sensors, which can be based on charge-coupled device (CCD) or complementary metal oxide semiconductor technology (CMOS)'),
 'q05_dig_psp': ('q05_dig', 'photostimulable storage phosphor plate systems that use film-like plates'),
 'q05_dig_dose': ('q05_dig', 'Such dose reduction has been reported to lie between 30 and 80% compared to conventional radiographs'),
 'q05_dig_acc': ('q05_dig', 'more recent studies found digital radiography to be as accurate as conventional films'),
 'q05_sum_acc': ('q05_sum', 'digital intraoral radiographs appear to be as accurate as film radiographs for the detection of dental caries'),
 'q05_dig_inv': ('q05_dig', 'inversion of the grey scale'),
 'q05_dig_sub': ('q05_dig', 'unchanged anatomical background structures will disappear'),
 'q05_sik_sub': ('q05_sik', 'Subtraction radiography is considered superior to conventional film radiography for detecting proximal and recurrent caries'),
 'q05_tor_logicon': ('q05_tor', 'study showed a sensitivity of 90.5% and specificity of 88.3%'),
 'q05_dig_cad': ('q05_dig', 'commercially available programmes are currently, at best, as accurate as human observers'),
 # CT / CBCT / MRI
 'q05_sik_ct': ('q05_sik', 'The use of CT in caries diagnosis is limited because of high cost, excessive radiation'),
 'q05_cbct_1998': ('q05_cbct', 'Dental cone beam computed tomography (CBCT) was first described in 1998'),
 'q05_cbct_not': ('q05_cbct', 'diagnosis of dental caries is not considered a primary indication for the use of dental CBCT'),
 'q05_cbct_art': ('q05_cbct', 'X-ray scatter and beam hardening artifacts'),
 'q05_dig_100': ('q05_dig', 'the dose from a CBCT of the same region would be 10–100 times higher'),
 'q05_sik_cbct': ('q05_sik', 'Cone beam CT is widely used in dentistry, particularly in caries diagnosis and endodontic applications'),
 'q05_sik_least': ('q05_sik', 'advantage of inducing the least amount of radiation hazard'),
 'q05_sik_mri': ('q05_sik', 'MRI is not suited for detection of caries'),
 # clinical significance
 'q05_kd_res': ('q05_kd', 'So far they only have research interest'),
 'q05_kd_fp': ('q05_kd', 'the more diagnostic techniques are used on the same surfaces, the more likely it is that interpretation of one of the techniques will give a false positive diagnosis'),
 'q05_stu_std': ('q05_stu', 'The standard of care for diagnosis of caries remains visual inspection of well-illuminated, clean and dry teeth, with use of radiographs as indicated'),
 'q05_las_adj': ('q05_las', 'laser fluorescence can be used as an adjunct to traditional caries detection methods'),
}
