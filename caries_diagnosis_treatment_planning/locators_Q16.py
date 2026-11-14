# Locators for Q16 "Newer classification of dental caries" (10m; absorbs "Classify Dental caries/cavities based on various criteria's." 5m). All keys prefixed q16_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
O = T + 'Operative_and_Dental_Materials_Textbooks/'
DET = O + 'Detection_and_Assessment_of_Dental_Caries.md'
SIK = O + 'Textbook_of_Conservative_and_Restorative_Dentistry.md'
F_EXTRA = {
 # Sikri, Textbook of Conservative and Restorative Dentistry (CBS; first eBook edition 2020, print edition not stated in the file).
 # Ch.2 and Ch.3 offset 19: PDF 44 printed 25, PDF 45 printed 26, PDF 48 printed 29, PDF 50 printed 31.
 'q16_sik': (SIK, 19, 'Sikri, 2020'),
 # Harpreet Singh 2nd (Wolters Kluwer India 2020) Ch.5-6. Offset 17: PDF 52 printed 35, PDF 57 printed 40, PDF 62 printed 45, PDF 64 printed 47.
 'q16_sgh': (O + 'Essentials_of_Preclinical_Conservative_Dentistry_Harpreet_Singh.md', 17, 'Singh, 2020'),
 # Mount 3rd (Wiley 2016) Ch.6 (Mount, Hume, Ngo, Wolff). Offset 16: PDF 98 printed 82, PDF 99 printed 83, PDF 101 printed 85.
 'q16_mnt': (O + 'Preservation_and_Restoration_of_Tooth_Structure_Mount.md', 16, 'Mount et al., 2016'),
 # Pickard's Manual 9th (Banerjee and Watson, OUP 2011) Ch.2. Offset 11: PDF 30 printed 19, PDF 32 printed 21.
 'q16_pic': (O + 'Pickards_Manual_of_Operative_Dentistry_9th.md', 11, 'Banerjee and Watson, 2011'),
 # Detection and Assessment of Dental Caries (Springer 2019): Ch.2 offset 7 (PDF 14 p7); Ch.5 offset 6 (PDF 43 p37); Ch.6 offset 5 (PDF 50 p45, PDF 51 p46);
 # Ch.7 offset 4 (PDF 63 p59); Ch.11 offset 1 (PDF 111 p110).
 'q16_d2': (DET, 7, 'Longbottom and Ferreira Zandona, 2019'),
 'q16_d5': (DET, 6, 'Machiulskiene, 2019'),
 'q16_d6': (DET, 5, 'Ekstrand and Braga, 2019'),
 'q16_d7': (DET, 4, 'Zeller, Young and Novy, 2019'),
 'q16_d11': (DET, 1, 'Schwendicke and Göstemeyer, 2019'),
}
BOOK_EXTRA = {}
L = {
 # criteria-based
 'q16_sik_three': ('q16_sik', 'Dental caries can be classified according to three major factors'),
 'q16_sik_linear': ('q16_sik', 'Linear enamel caries: Caries developing on the labial surfaces of anterior teeth'),
 'q16_sik_root': ('q16_sik', 'Caries developing at the cemento- enamel junction or cementum'),
 'q16_sik_rampant': ('q16_sik', 'A caries increment of ten or more new carious lesions over a year is characteristic of rampant caries'),
 'q16_sik_arrest': ('q16_sik', 'The arrested caries, clinically appears as a dark brown pigmentation with smooth surface'),
 'q16_sik_rad': ('q16_sik', 'known as radiation caries'),
 'q16_sik_age': ('q16_sik', 'Geriatric caries: Caries developing in older adults'),
 'q16_sik_nursing': ('q16_sik', 'Nursing bottle caries'),
 'q16_sgh_acute': ('q16_sgh', 'refers to that type of carious lesion which spreads very fast'),
 'q16_sgh_chronic': ('q16_sgh', 'It is that form of caries which progresses very slowly'),
 'q16_sgh_forward': ('q16_sgh', 'Wherever the caries cone in the enamel is larger or at least the same size as that in the dentin, it is termed forward caries'),
 'q16_sgh_backward': ('q16_sgh', 'termed backward caries'),
 'q16_sgh_hidden': ('q16_sgh', 'Also known as hidden caries'),
 'q16_sgh_incip': ('q16_sgh', 'Incipient Caries (Reversible)'),
 'q16_sgh_cavit': ('q16_sgh', 'Cavitated Caries (Non-Reversible)'),
 'q16_d2_cars': ('q16_d2', 'CARS (Caries Adjacent to a Restoration or Sealant)'),
 'q16_d2_resid': ('q16_d2', 'applies to aspects of caries lesions remaining after operative interventions'),
 # Black and limitations
 'q16_sgh_simon': ('q16_sgh', 'Later, an additional class was added by Simon, which was designated as Class VI'),
 'q16_mnt_black': ('q16_mnt', 'The Black classification system did not describe the lesions, rather it described the final restoration location'),
 'q16_mnt_monitor': ('q16_mnt', 'Black’s classification did not allow monitoring of lesion size, progress and activity'),
 # Mount and Hume
 'q16_mnt_1997': ('q16_mnt', 'revised classifi- cation system for carious lesions by site and size'),
 'q16_mnt_site1': ('q16_mnt', 'Site 1 – pits, fissures and enamel defects on occlusal surfaces of posterior teeth'),
 'q16_mnt_site2': ('q16_mnt', 'Site 2 – approximal surfaces in relation to areas in contact with adjacent teeth'),
 'q16_mnt_site3': ('q16_mnt', 'Site 3 – the cervical one‐third of the crown or, following gin- gival recession, the exposed root surface'),
 'q16_mnt_size0': ('q16_mnt', 'Size 0 – the earliest identifiable lesion in the first stages of demineralization'),
 'q16_mnt_size1': ('q16_mnt', 'Size 1 – minimal surface cavitation with dentine involvement just beyond treatment by remineralization alone'),
 'q16_mnt_size4': ('q16_mnt', 'Size 4 – extensive caries or bulk loss of tooth structure'),
 'q16_mnt_pnr': ('q16_mnt', 'progressing [P], non‐progressing [N], or reversed [R]'),
 'q16_mnt_enl': ('q16_mnt', 'Enlarged 3'),
 'q16_sgh_mh': ('q16_sgh', 'a new classification system by Mount and Hume (1997)'),
 'q16_sgh_adv': ('q16_sgh', 'Size 3 (Advanced)'),
 'q16_sik_1998': ('q16_sik', 'Mount (1998) has also classified carious lesions'),
 'q16_sik_size1': ('q16_sik', 'Minimal involvement of dentin. Treatment by remineralization alone'),
 # ICDAS / ICCMS
 'q16_d6_2002': ('q16_d6', 'A conference was held in Dundee, Scotland, in 2002'),
 'q16_d6_twodigit': ('q16_d6', 'Detection wise, it is a two-digit scoring system'),
 'q16_d6_merge': ('q16_d6', '“Initial” (ICDAS scores 1 and 2), “Moderate” (ICDAS scores 3 and 4), and “Extensive” (ICDAS scores 5 and 6)'),
 'q16_mnt_2002': ('q16_mnt', 'was developed in 2002 in recog- nition that better quality information'),
 'q16_mnt_iccms': ('q16_mnt', 'The seven ICDAS codes have been merged to four codes'),
 'q16_pic_2004': ('q16_pic', 'In 2004, the ICDAS (International Caries Detection and Assessment System) Foundation was convened'),
 'q16_sgh_2009': ('q16_sgh', 'Introduced in 2009, ICDAS is based on the initiation and progression of dental caries'),
 # Nyvad, ADA CCS, iceberg, radiographic
 'q16_d5_two': ('q16_d5', 'the scoring system incorporates two levels of severity: non-cavitated and cavitated'),
 'q16_d5_basis': ('q16_d5', 'based on the patho-anatomical surface characteristics of the caries lesions, rather than on the depth of lesion penetration'),
 'q16_d7_cats': ('q16_d7', 'The ADA CCS categories of sound, initial, moderate, and advanced'),
 'q16_pic_iceberg': ('q16_pic', 'lesions are divided into four groups, D1-D4, depending on the depth of tissue invasion and the degree of cavitation'),
 'q16_d11_ed': ('q16_d11', 'discriminating the outer and inner enamel half (E1, E2) and the outer, middle and inner dentin third (D1-3)'),
}
