# Locators for Q13 "Quantitative light induced fluorescence (QLF)" (10m). All keys prefixed q13_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
B = T + 'Operative_and_Dental_Materials_Textbooks/'
F_EXTRA = {
 # Detection and Assessment of Dental Caries (2019) Ch.16, Baek-Il Kim. Offset 0 confirmed at PDF 159 (printed 159) and PDF 165 (printed 165).
 'q13_kim': (B+'Detection_and_Assessment_of_Dental_Caries.md', 0, 'Kim, 2019'),
 # Lasers in Dentistry - Current Concepts 2nd ed (2023) Ch.6 Laser assisted diagnostics, A. M. Muruppel and D. Fried. Offset 9 confirmed at PDF 138 (printed 129) and PDF 155 (printed 146).
 'q13_las': (B+'Lasers_in_Dentistry_Current_Concepts.md', 9, 'Muruppel and Fried, 2023'),
 # Sikri VK, Textbook of Conservative and Restorative Dentistry (CBS, eBook 2020) Ch.7 Diagnosis and diagnostic aids (single author). Offset 19 confirmed at PDF 134 (printed 115) and PDF 145 (printed 126).
 'q13_sik': (B+'Textbook_of_Conservative_and_Restorative_Dentistry.md', 19, 'Sikri, 2020'),
 # Torres (ed), Modern Operative Dentistry (2020) Ch.3 Cariology, Caneppele, Borges, Torres, Rodrigues and Attin. Offset 14 confirmed at PDF 115 (printed 101) and PDF 120 (printed 106).
 'q13_tor': (B+'Modern_Operative_Dentistry.md', 14, 'Caneppele et al., 2020'),
}
L = {
 # definition, history
 'q13_def': ('q13_kim', 'Quantitative light-induced fluorescence (QLF) is a representative optical technology for early detection and quantification of dental caries'),
 'q13_both': ('q13_kim', 'can measure both the mineral content as a fluorescence loss and bacterial activity as a red fluorescence simultaneously'),
 'q13_1981': ('q13_kim', 'QLF technology was introduced in 1981 as the first optical evaluation technique in the field of dentistry (after X-rays)'),
 'q13_488': ('q13_kim', 'under irradiation with blue laser light with a wavelength of 488 nm'),
 # principle
 'q13_lamp': ('q13_kim', 'fluorescence that acts like a lamp inside the tooth after passing through the enamel'),
 'q13_scat': ('q13_kim', 'light scattering inside a white spot being 5–10 times higher than that in normal enamel'),
 'q13_dark': ('q13_kim', 'The lesion appears darker than sound enamel tissue due to light scattering of the generated fluorescence'),
 'q13_tr_green': ('q13_tor', 'the chromophores inside the dentin are excited, shining with green dentin back-illumination'),
 'q13_porph': ('q13_kim', 'These porphyrin-containing biofilms manifest as red fluorescence'),
 'q13_3days': ('q13_kim', 'has been present for at least 3 days'),
 # parameters
 'q13_dF': ('q13_kim', 'delta F (ΔF), which represents the lesion depth'),
 'q13_tmr': ('q13_kim', 'strongly correlated with lesion depths as obtained using transverse microradiography (TMR) (r = 0.88)'),
 'q13_dQ': ('q13_kim', 'lesion volume (ΔQ in mm2%)'),
 'q13_dR': ('q13_kim', 'red fluorescence that reflects bacterial activity can be calculated by delta R (ΔR, in %)'),
 # devices and light source
 'q13_insp': ('q13_kim', 'The Inspektor Pro, which was introduced in 2004, is a first-generation QLF device'),
 'q13_405': ('q13_kim', 'blue visible light with a wavelength of 405 nm induces fluorescence within the tooth structure'),
 'q13_qlfd': ('q13_kim', 'A second-generation QLF device was introduced in 2012 and later upgraded to the digital Biluminator 2+ QLF device (QLF-D)'),
 'q13_qray': ('q13_kim', 'third-generation QLF, Qray devices were developed in 2012'),
 'q13_lz_xenon': ('q13_las', 'xenon lamp that generates light at 370 nm light'),
 'q13_lz_520': ('q13_las', 'a high pass filter which allows only wavelengths greater than 520 nm to be detected'),
 'q13_sk_xenon': ('q13_sik', 'The QLF device uses a 50-watt xenon arc lamp and an optical filter producing blue light (290–450 nm wavelength)'),
 # technique
 'q13_plaque': ('q13_kim', 'remove any remaining plaque on the tooth surface by performing a tooth-cleaning procedure'),
 'q13_bucc': ('q13_kim', 'necessary to observe not only the occlusal surface but also the buccal and lingual surfaces'),
 'q13_time': ('q13_kim', '1–2 min (for visual examination and image taking)'),
 # applications
 'q13_icdas12': ('q13_kim', 'ICDAS exhibits a poor performance for teeth categorized as code 1 or 2'),
 'q13_stain': ('q13_kim', 'cariogenic discoloration involving bacteria appears as red fluorescence around stains'),
 'q13_prox': ('q13_kim', 'sensitivities of 71% and 64%, respectively, and specificities of 84% and 88%'),
 'q13_qlfi': ('q13_kim', 'showed higher reliability than when using ICDAS alone, with kappa indexes of 0.79 and 0.70'),
 'q13_fl': ('q13_kim', 'at least 50% of lesions were recovered when applying fluoride treatment to lesions with a ΔF of –14.6 or less'),
 'q13_nyvad': ('q13_kim', 'the level of red fluorescence was much higher for active lesions than for inactive lesions'),
 'q13_root': ('q13_kim', 'strongly correlated with TMR findings after demineralization (r = 0.89)'),
 'q13_metal': ('q13_kim', 'restorations such as those involving gold and amalgam appear as black shadows'),
 'q13_sec': ('q13_kim', 'QLF technology had the highest sensitivity in detecting secondary caries lesions'),
 'q13_sealant': ('q13_kim', 'QLF technology can be used to confirm the occurrence of sealant failure'),
 'q13_sk_ortho': ('q13_sik', 'Useful in detecting demineralization under orthodontic appliances/brackets'),
 # accuracy, limitations
 'q13_sens': ('q13_kim', 'Literature reported range in 64–94%'),
 'q13_spec': ('q13_kim', 'Literature reported range in 84–100%'),
 'q13_dis': ('q13_kim', 'Sensitive to the ambient light, difficult to reposition of intraoral camera type devices'),
 'q13_lz_500': ('q13_las', 'QLF can detect carious lesions on occlusal and smooth surfaces to a depth of 500μm'),
 'q13_lz_dentin': ('q13_las', 'it is not able to differentiate or detect lesions extending into dentin'),
 'q13_lz_hypo': ('q13_las', 'not able to specifically differentiate between caries, hypoplasia, and similar conditions'),
 'q13_lz_smooth': ('q13_las', 'better suited for detection of early lesions and more so on smooth surfaces rather than occlusal or in fissures'),
 'q13_sk_prox': ('q13_sik', 'Inability to detect/monitor interproximal lesions'),
}
