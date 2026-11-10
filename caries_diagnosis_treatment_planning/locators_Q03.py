# Locators for Q03 "Discuss latest developments in diagnostic aids in conservative dentistry." (25m). All keys prefixed q03_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
O = T + 'Operative_and_Dental_Materials_Textbooks/'
D = O + 'Detection_and_Assessment_of_Dental_Caries.md'
F_EXTRA = {
 # Sturdevant's 2e South Asia, Ch.3 Patient assessment, examination, diagnosis and treatment planning (contributors page: Boushell, Shugars).
 # Offset 19 confirmed at PDF 106 (printed 87) and PDF 112 (printed 93).
 'q03_stu': (O+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Boushell and Shugars, 2019'),
 # Detection and Assessment of Dental Caries (Ferreira Zandona and Longbottom, eds, 2019). Offsets checked per chapter:
 # Ch.12 PDF 119=119, 124=124 (0); Ch.13 127=127, 135=135 (0); Ch.14 139=139, 148=148 (0); Ch.15 151=151, 157=157 (0);
 # Ch.16 159=159, 169=169 (0); Ch.17 171=171, 174=174 (0); Ch.18 PDF 176=177, 183=184 (-1); Ch.19 187=189, 193=195 (-2);
 # Ch.20 196=199, 204=207 (-3); Ch.21 206=209, 211=214 (-3); Ch.22 214=217, 216=219 (-3).
 'q03_d12': (D, 0, 'Göstemeyer and Schwendicke, 2019'),
 'q03_d13': (D, 0, 'Price, 2019'),
 'q03_d14': (D, 0, 'Hogan, Pretty and Ellwood, 2019'),
 'q03_d15': (D, 0, 'Kühnisch, 2019'),
 'q03_d16': (D, 0, 'Kim, 2019'),
 'q03_d17': (D, 0, 'Neuhaus and Lussi, 2019'),
 'q03_d18': (D, -1, 'Amaechi, 2019'),
 'q03_d19': (D, -2, 'Fried, 2019a'),
 'q03_d20': (D, -3, 'Fried, 2019b'),
 'q03_d21': (D, -3, 'Yanıkoğlu and Tağtekin, 2019'),
 'q03_d22': (D, -3, 'Longbottom and Vernon, 2019'),
 # Sikri, Textbook of Conservative and Restorative Dentistry, Ch.7 Diagnosis and diagnostic aids. Offset 19 confirmed at PDF 127 (printed 108) and PDF 137 (printed 118).
 'q03_sik': (O+'Textbook_of_Conservative_and_Restorative_Dentistry.md', 19, 'Sikri, 2020'),
 # Torres (ed) Modern Operative Dentistry Ch.1 (Torres, Barbe, Noack, Wicht). Offset 14 confirmed at PDF 15 (printed 1) and PDF 26 (printed 12).
 'q03_tor': (O+'Modern_Operative_Dentistry.md', 14, 'Torres et al, 2020'),
 # Chu, Devigus, Paravina, Mieleszko, Fundamentals of Color 2nd ed (Quintessence, copyright 2010), Ch.5; no printed page numbers in the extract.
 'q03_sh': (O+'Fundamentals_of_Color_Shade_Matching.md', None, 'Chu et al, 2010'),
 # Goldstein's Esthetics in Dentistry 3e Ch.3 (Goldstein and Salama). Offset 17 confirmed at PDF 66 (printed 49) and PDF 72 (printed 55).
 'q03_gol': (O+'Esthetics_in_Dentistry_Goldstein.md', 17, 'Goldstein and Salama, 2018'),
}
L = {
 # why new aids
 'q03_stu_25': ('q03_stu', 'approximately 25% mineral loss has to occur before a radiolucency begins to appear on a radiograph'),
 'q03_stu_expl': ('q03_stu', 'caries is contraindicated as a part of the caries detection process'),
 'q03_sik_third': ('q03_sik', 'the conventional methods are effective, only if at least one-third thickness of enamel'),
 'q03_sik_req': ('q03_sik', 'Should not transfer any micro-organism from affected area to the unaffected area'),
 'q03_sik_req2': ('q03_sik', 'Time and cost should be manageable'),
 # digital radiography, CBCT
 'q03_d12_ccd': ('q03_d12', 'solid-state sensors, which can be based on charge-coupled device (CCD) or complementary metal oxide semiconductor technology (CMOS)'),
 'q03_d12_psp': ('q03_d12', 'photostimulable storage phosphor plate systems that use film-like plates'),
 'q03_d12_dose': ('q03_d12', 'Such dose reduction has been reported to lie between 30 and 80% compared to conventional radiographs'),
 'q03_d12_more': ('q03_d12', 'the number of radiographs taken by dentists is increased when using digital devices'),
 'q03_d12_acc': ('q03_d12', 'digital bitewing radiography is now at least as accurate as conventional films'),
 'q03_d12_cad': ('q03_d12', 'the currently available technology does not provide a more accurate diagnosis than a human observer'),
 'q03_d12_cbct': ('q03_d12', 'the dose from a CBCT of the same region would be 10–100 times higher'),
 'q03_sik_sub': ('q03_sik', 'Subtraction radiography is considered superior to conventional film radiography for detecting proximal and recurrent caries'),
 'q03_d13_sens': ('q03_d13', 'CBCT imaging: 0.44–0.61'),
 'q03_d13_2d': ('q03_d13', '2D imaging: 0.31–0.33'),
 'q03_d13_rec': ('q03_d13', 'Using CBCT for the diagnosis of interproximal recurrent caries does not appear to be as predictable or as reliable as for the diagnosis of primary interproximal caries'),
 'q03_d13_not': ('q03_d13', 'dental CBCT cannot be recommended as a primary radiographic technique for diagnosing dental caries'),
 'q03_d13_inc': ('q03_d13', 'should only be performed during a review for'),
 'q03_sik_cbct': ('q03_sik', 'Cone beam CT is widely used in dentistry, particularly in caries diagnosis and endodontic applications'),
 'q03_sik_cbct2': ('q03_sik', 'The application of cone beam computed tomography (CBCT) in diagnosing dental caries is not established'),
 # optical
 'q03_d14_dark': ('q03_d14', 'areas of porosity appear dark on a lighter background'),
 'q03_d14_adj': ('q03_d14', 'it is important to view FOTI as an adjunct detection method'),
 'q03_d14_difoti': ('q03_d14', 'Image storage for longitudinal monitoring and patient education'),
 'q03_d14_frac': ('q03_d14', 'Can be used for crown and root fracture detection and canal orifice location'),
 'q03_sik_difoti': ('q03_sik', 'DIFOTI images cannot indicate the depth of lesion penetration'),
 'q03_d15_780': ('q03_d15', 'emits near-infrared light with a wavelength of ~780 nm'),
 'q03_d15_2012': ('q03_d15', 'X-ray-free imaging method for caries detection and diagnostics in posterior teeth in autumn 2012'),
 'q03_d15_rep': ('q03_d15', 'Unlimited repeatability'),
 'q03_d15_crack': ('q03_d15', 'Detection of cracks'),
 'q03_d15_pulp': ('q03_d15', 'No possibility of imaging the caries extension in relation to the pulp'),
 'q03_d16_both': ('q03_d16', 'technology can measure both the mineral content and also the bacterial activity simultaneously'),
 'q03_d16_df': ('q03_d16', 'delta F (ΔF), which represents the lesion depth'),
 'q03_d16_r': ('q03_d16', 'strongly correlated with lesion depths as obtained using transverse microradiography (TMR) (r = 0.88)'),
 'q03_d16_dr': ('q03_d16', 'the intensity of red fluorescence that reflects bacterial activity can be calculated by delta R'),
 'q03_d17_655': ('q03_d17', 'Both devices operate at a wavelength of 655 nm'),
 'q03_d17_por': ('q03_d17', 'induces fluorescence of bacterial porphyrins'),
 'q03_d17_second': ('q03_d17', 'intended to act as a second opinion device'),
 'q03_d17_noimg': ('q03_d17', 'Punctual measurement (no images)'),
 'q03_d17_nocav': ('q03_d17', 'No detection of cavitation'),
 'q03_d17_val': ('q03_d17', 'Sufficient clinical validation'),
 'q03_stu_dd': ('q03_stu', 'yields a numerical score from 0–99'),
 'q03_stu_ddsr': ('q03_stu', 'the increased likelihood of false-positive diagnoses limits its usefulness as a principal diagnostic method'),
 'q03_stu_spectra': ('q03_stu', 'porphyrins – metabolites unique to cariogenic bacteria – to appear distinctly red, whereas healthy enamel fluoresces to appear green'),
 'q03_stu_spectra5': ('q03_stu', 'defines the potential caries activity on a scale of 0–5'),
 'q03_d19_1300': ('q03_d19', 'enamel is most transparent near λ = 1300 nm'),
 'q03_d19_stain': ('q03_d19', 'No interference from stains'),
 'q03_d19_na': ('q03_d19', 'Not yet available commercially'),
 'q03_d20_oct': ('q03_d20', 'OCT can be used to measure the reflectivity within dental hard tissues to a depth of up to 3–5 mm in enamel'),
 'q03_d20_rest': ('q03_d20', 'as well as for root caries and caries around restorations'),
 'q03_d20_na': ('q03_d20', 'Not yet available commercially'),
 # electrical and other
 'q03_sik_ecm': ('q03_sik', 'The electric conductivity is directly proportional to the amount of demineralization'),
 'q03_stu_fda': ('q03_stu', 'The technologies currently approved by the FDA include laser-induced fluorescence, light-induced fluorescence, and alternating current (AC) impedance spectroscopy'),
 'q03_stu_lim1': ('q03_stu', 'they are only indicated for use on unrestored pits and fissures'),
 'q03_stu_lim2': ('q03_stu', 'their diagnostic accuracy has not been firmly established'),
 'q03_stu_cs': ('q03_stu', 'provides a colour scale and a numerical scale to determine the severity of the caries lesion'),
 'q03_sik_cs': ('q03_sik', 'reported CarieScan to have superior sensitivity and specificity (both 92.5%) over other methods'),
 'q03_sik_csno': ('q03_sik', 'It cannot be used to assess secondary caries, the integrity of a restoration, root caries, and the depth of excavation'),
 'q03_d18_ptr': ('q03_d18', 'using Photothermal Radiometry and Luminescence (PTR-LUM) technology'),
 'q03_d18_5mm': ('q03_d18', 'examine up to 5 mm below the tooth surface'),
 'q03_d18_sec': ('q03_d18', 'Can detect secondary caries around the intact margins of composites, amalgams, and all ceramic crowns'),
 'q03_d18_seal': ('q03_d18', 'Can detect caries beneath clear and opaque sealants'),
 'q03_d21_us': ('q03_d21', 'Ultrasonic system can distinguish an intact and demineralized enamel surface'),
 'q03_d21_glyc': ('q03_d21', 'It needs a coupling agent (glycerin)'),
 'q03_d21_act': ('q03_d21', 'Lesion activity cannot be detected'),
 'q03_d22_ca': ('q03_d22', 'via a calcium-sensitive photoprotein'),
 # magnification, documentation
 'q03_stu_loupe': ('q03_stu', 'Most dentists use magnifications of 2× to 4×'),
 'q03_stu_micro': ('q03_stu', 'typically range from 2.5× to 20×'),
 'q03_stu_microuse': ('q03_stu', 'identifying minute caries lesions, and minimizing the removal of sound tooth structure'),
 'q03_stu_photo': ('q03_stu', 'Intraoral cameras and single-lens reflex (SLR) digital cameras provide opportunities to document'),
 'q03_stu_virtual': ('q03_stu', 'The ability to obtain virtual study models via digital impression technology has increased the ease and level of diagnostic evaluation'),
 'q03_gol_micro': ('q03_gol', 'Both the chairside microscope and intraoral camera provide essential views for precise tooth surface exams'),
 'q03_gol_cam': ('q03_gol', 'The intraoral camera also has the ability to easily transilluminate and photographically record hidden microcracks'),
 # cracks
 'q03_stu_crack': ('q03_stu', 'Appropriate dye materials or transillumination may aid in detecting the line of fracture within the tooth structure'),
 'q03_stu_cusp': ('q03_stu', 'Cusp isolation/loading devices and techniques must be utilized'),
 'q03_tor_crack': ('q03_tor', 'Diagnosis is performed with a device that allows placing pressure on each cusp separately'),
 # shade
 'q03_sh_acc': ('q03_sh', 'computer-assisted shade analysis is more accurate and more consistent compared with human shade assessment'),
 'q03_sh_80': ('q03_sh', '80% of patients notice a difference in the shade of their natural teeth compared with their restored teeth'),
 'q03_sh_spec': ('q03_sh', 'They measure light wavelengths reflected from an object at many points along the visual spectrum (approximately every 10 nanometers)'),
 'q03_sh_col': ('q03_sh', 'A colorimeter filters light in three or four areas of the visible spectrum'),
 'q03_sh_cam': ('q03_sh', 'the use of a digital camera alone is not effective for shade analysis'),
 'q03_sh_spot': ('q03_sh', 'Spot measurement devices are best suited for showing shade trends or tendencies'),
 'q03_sh_whole': ('q03_sh', 'their use is limited to anterior teeth because of the size of the sensor'),
 'q03_sh_trans': ('q03_sh', 'Translucency mapping is inadequate in all of the systems'),
 # pulp, clinical significance
 'q03_stu_endo': ('q03_stu', 'All teeth to be restored with large restorations should have a pulpal and periapical evaluation'),
 'q03_tor_pulp': ('q03_tor', 'Conducting pulp sensitivity testing on each tooth is not recommended'),
 'q03_tor_pulp2': ('q03_tor', 'or those considered for restoration might be tested for signs of pulpal vitality'),
 'q03_stu_soc': ('q03_stu', 'The standard of care for diagnosis of caries remains visual inspection of well-illuminated, clean and dry teeth, with use of radiographs as indicated'),
 'q03_stu_fp': ('q03_stu', 'a highly specific test (i.e. few false positives [cell B]) means that fewer healthy teeth will be incorrectly treated'),
 'q03_d16_amb': ('q03_d16', 'Sensitive to the ambient light'),
 'q03_stu_prop': ('q03_stu', 'fractures that are actively propagating'),
 'q03_d15_bone': ('q03_d15', 'The light is transmitted through the alveolar bone into the dental hard tissue'),
 'q03_d17_mon': ('q03_d17', 'it was intended to be used as a device for caries monitoring as well'),
 'q03_stu_deep': ('q03_stu', 'Photographs of preparations of deep caries lesions provide documentation'),
 'q03_d14_light': ('q03_d14', 'high intensity white light directed tangentially'),
}
