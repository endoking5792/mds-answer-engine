# Locators for Q07 "Clinical situations and role of multidisciplinary approach in endodontics" (10m). Keys prefixed q07_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
G = T+'Endodontics_Kishor_Gulabivala_Yuan_Ling_Ng_4th_Ed_Mosby_2014_Chapterwise/'
F_EXTRA = {
 # Gulabivala and Ng 4e (2014), Section 4 Multidisciplinary aspects of endodontic management. Offset 9 in every chapter used, confirmed e.g. Ch.12 PDF 309 (printed 300) and PDF 311 (printed 302); Ch.14 PDF 345 (printed 336) and PDF 347 (printed 338); Ch.17 PDF 384 (printed 375) and PDF 385 (printed 376).
 # Ch.12 by Gulabivala, Darbar and Ng.
 'q07_perio': (G+'12_12_The_perio_endo_interface.md', 9, 'Gulabivala, Darbar and Ng, 2014'),
 # Ch.14 by Gulabivala and Ng.
 'q07_rest': (G+'14_14_The_restorative_endo_interface.md', 9, 'Gulabivala and Ng, 2014'),
 # Ch.15 by Gulabivala, Darbar and Ng (author line read from the chapter file; verify against the printed book). Offset 9 confirmed at PDF 371 (printed 362) and PDF 372 (printed 363).
 'q07_med': (G+'15_15_The_medical_endo_interface_and_patients_with_special_need.md', 9, 'Gulabivala, Darbar and Ng, 2014'),
 # Ch.17 by Leeson and Gulabivala.
 'q07_surg': (G+'17_17_The_oral_medicine_and_oral_surgery_endo_interface.md', 9, 'Leeson and Gulabivala, 2014'),
 # Sikri 2e (2019) Ch.34, no chapter author named. Offset 21 confirmed at PDF 610 (printed 589) and PDF 611 (printed 590).
 'q07_sikp': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/34_34_Endodontic_Periodontal_Relationship.md', 21, 'Sikri, 2019'),
 # Sikri 2e (2019) Ch.28 Pediatric Endodontics. Offset 21 confirmed at PDF 522 (printed 501) and PDF 523 (printed 502).
 'q07_sikc': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/28_28_Pediatric_Endodontics.md', 21, 'Sikri, 2019'),
 # Weine 6e (2004) Ch.12 (Weine and Potashnick); PDF page only.
 'q07_wei': (T+'Weines_Endodontics_Full_Chapterwise/12_CHAPTER_12_Endodontic_Orthodontic_Relationships.md', None, 'Weine and Potashnick, 2004'),
 # Common Complications in Endodontics (ed. Jain, Springer 2025) Ch.11 by Miglani and Bhutiani. Offset 11 confirmed at PDF 262 (printed 251) and PDF 263 (printed 252).
 'q07_cc': (T+'Common_Complications_in_Endodontics_Chapterwise/11_11_Harmonizing_Endodontics.md', 11, 'Miglani and Bhutiani, 2025'),
}
L = {
 'q07_cc_key': ('q07_cc', 'relies on integration and collaboration between various dental specialties'),
 'q07_perio_diff': ('q07_perio', 'each disease requires entirely different clinical treatment regimens'),
 'q07_perio_first': ('q07_perio', 'the simplest and least damaging therapy should be undertaken first'),
 'q07_perio_wk': ('q07_perio', 'In the absence of any sign of resolution after a short review period'),
 'q07_perio_class': ('q07_perio', 'True combined lesion of dual origin'),
 'q07_sikp_rel': ('q07_sikp', 'implies the spread of inflammation and infection from one component to the other'),
 'q07_sikp_first': ('q07_sikp', 'The periodontal lesions are treated first'),
 'q07_sikp_resect': ('q07_sikp', 'A tooth that requires a root to be resected always need root canal treatment'),
 'q07_sikp_gtr': ('q07_sikp', 'GTR therapy has been successfully carried out in the endodontic surgeries'),
 'q07_wei_multi': ('q07_wei', 'This multidisciplinary approach offers benefits not available with periodontal surgery alone.'),
 'q07_wei_rest': ('q07_wei', 'permits placement of a restoration that fulfills the periodontal and occlusal requirements of the tooth'),
 'q07_wei_first': ('q07_wei', 'should have such treatment completed prior to the initiation of tooth movement'),
 'q07_rest_ability': ('q07_rest', 'The restorability of the tooth should always be determined before endodontic treatment'),
 'q07_rest_2mm': ('q07_rest', 'a cast restoration encompassing at least 2 mm of sound dentine around the circumference'),
 'q07_rest_seal': ('q07_rest', 'an early permanent coronal seal is an important final stage in the completion of root-canal treatment'),
 'q07_rest_abut': ('q07_rest', 'abutment teeth and their restorations to fail mechanically than vital abutments'),
 'q07_rest_ext': ('q07_rest', 'it may be possible to extrude the tooth orthodontically'),
 'q07_rest_imp': ('q07_rest', 'because they avoid damage to and interference with adjacent teeth'),
 'q07_surg_mimic': ('q07_surg', 'essential for dentists to be aware of any non-endodontic lesions that may mimic periapical pathosis'),
 'q07_surg_ref': ('q07_surg', 'an appropriate referral to a specialist should be sought'),
 'q07_med_assess': ('q07_med', 'understand how endodontic care may need to be modified or adjusted'),
 'q07_med_sed': ('q07_med', 'Inhalation sedation and intravenous sedation are indicated as the next line of treatment'),
 'q07_sikc_ret': ('q07_sikc', 'whether to retain or to extract'),
 'q07_sikc_rct': ('q07_sikc', 'Root canal treatment is the treatment of choice to retain them'),
 'q07_sikc_same': ('q07_sikc', 'The basic aims and treatment protocol of endodontic therapy in children are the same as those in adults'),
}
