# Locators for P1 "ICDAS II and ICCMS: detection codes, activity assessment and the risk-based management pathway" (10m, predicted). All keys prefixed p1_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
B = T + 'Operative_and_Dental_Materials_Textbooks/'
F_EXTRA = {
 # Detection and Assessment of Dental Caries (2019) Ch.6 ICDAS, Ekstrand and Braga. Offset 5 confirmed at PDF 50 (printed 45) and PDF 55 (printed 50).
 'p1_ek': (B+'Detection_and_Assessment_of_Dental_Caries.md', 5, 'Ekstrand and Braga, 2019'),
 # Same book Ch.7 ADA CCS, Zeller, Young and Novy. Offset 4 confirmed at PDF 62 (printed 58) and PDF 65 (printed 61).
 'p1_ada': (B+'Detection_and_Assessment_of_Dental_Caries.md', 4, 'Zeller, Young and Novy, 2019'),
 # Same book Ch.23 Clinical decision-making, Fontana and Huysmans. Offset -4 confirmed at PDF 223 (printed 227) and PDF 227 (printed 231).
 'p1_fh': (B+'Detection_and_Assessment_of_Dental_Caries.md', -4, 'Fontana and Huysmans, 2019'),
 # Modern Operative Dentistry (2020) Ch.3 Cariology, Caneppele et al. Offset 14 confirmed at PDF 115 (printed 101) and PDF 128 (printed 114).
 'p1_tor': (B+'Modern_Operative_Dentistry.md', 14, 'Caneppele et al., 2020'),
 # Summitt's Fundamentals 4th ed (2013) Ch.5 Caries management, Amaechi, van Amerongen, van Loveren and Kidd. No printed page numbers in the file.
 'p1_sum': (B+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Amaechi et al., 2013'),
 # Mount et al. (eds) Preservation and Restoration of Tooth Structure 3rd ed (2016) Ch.6, Mount, Hume, Ngo and Wolff. Offset 16 confirmed at PDF 97 (printed 81) and PDF 98 (printed 82).
 'p1_mt': (B+'Preservation_and_Restoration_of_Tooth_Structure_Mount.md', 16, 'Mount et al., 2016'),
 # Kidd and Fejerskov, Essentials of Dental Caries 4th ed (2016) Ch.3. Offset 13 confirmed at PDF 70 (printed 57) and PDF 85 (printed 72).
 'p1_kd': (B+'Essentials_of_Dental_Caries_4th.md', 13, 'Kidd and Fejerskov, 2016'),
 # Audit u2 2026-11-14. Pickard's Guide 10th (OUP 2015), Banerjee and Watson, Ch.2. Offset 11: PDF 33 printed 22, PDF 34 printed 23.
 'p1_pkg': (T+'Operative_and_Dental_Materials_Textbooks/Pickards_Guide_to_Minimally_Invasive_Operative_Dentistry.md', 11, 'Banerjee and Watson, 2015'),
 # Sturdevant's 2nd South Asia ed (2019) Ch.3, Boushell and Shugars (contributors list). Offset 19: PDF 106 printed 87, PDF 107 printed 88.
 'p1_stu3': (T+'Operative_and_Dental_Materials_Textbooks/Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Boushell and Shugars, 2019'),
}
L = {
 # history
 'p1_dundee': ('p1_ek', 'A conference was held in Dundee, Scotland, in 2002'),
 'p1_histo': ('p1_ek', 'because that system had used histology as validation'),
 'p1_root3': ('p1_ek', 'for classifying root caries the scores were restricted to 3'),
 'p1_2005': ('p1_ek', 'At follow-up meetings in 2005 and 2007, criteria for activity assessment of the lesion and a radiographical scoring system were both devised'),
 'p1_tr_2003': ('p1_tor', 'The original ICDAS was created in 2003'),
 'p1_tr_icdas2': ('p1_tor', 'the second version became available in 2005, named ICDAS II'),
 'p1_mt_2002': ('p1_mt', 'was developed in 2002 in recognition that better quality information about caries detection'),
 # codes
 'p1_two': ('p1_ek', 'Detection wise, it is a two-digit scoring system'),
 'p1_first': ('p1_ek', 'The first digit is used to describe the status of the surface'),
 'p1_second': ('p1_ek', 'The second digit is used to describe the caries severity'),
 'p1_tr_09': ('p1_tor', 'receives codes ranging from 0 to 9'),
 'p1_ek_789': ('p1_ek', '7: Lost or broken restoration 8: Temporary restoration 9: Other conditions'),
 'p1_su_c1': ('p1_sum', 'First visual change (opacity or discoloration) in enamel hardly visible on the wet surface but distinctly visible after air drying'),
 'p1_su_c2': ('p1_sum', 'Distinct visual change (opacity or discoloration) in enamel, visible without air drying'),
 'p1_tr_c3': ('p1_tor', 'Localized enamel breakdown (without clinical visual signs of dentinal involvement)'),
 'p1_tr_c456': ('p1_tor', '4 Underlying dark shadow from dentin 5 Distinct cavity with visible dentin 6 Extensive distinct cavity with visible dentin'),
 'p1_cleandry': ('p1_ek', 'To score caries with the ICDAS requires teeth to be clean and dry'),
 'p1_ball': ('p1_ek', 'the ball-ended probe'),
 'p1_rootcode': ('p1_ek', 'Loss of anatomical contour <0.5 mm is accepted'),
 # histology
 'p1_h0': ('p1_ek', 'if a surface is scored ICDAS 0 (sound), 95% of them are actually histological without demineralization'),
 'p1_h1': ('p1_ek', 'If the lesion is scored ICDAS 1, 95% shows no demineralization or the demineralization is restricted to the outer half of the enamel'),
 'p1_h2': ('p1_ek', 'A total of 83% of ICDAS 2 lesions are characterized to be histologically wise in the inner half of the enamel or, if in dentin, restricted to the outer 1/3 of the dentin'),
 'p1_h34': ('p1_ek', '(67%) having demineralization reaching the middle 1/3 of the dentin'),
 'p1_h56': ('p1_ek', 'ICDAS score 5 and 6 lesions (84%) shows histologically demineralization in the inner 1/3 of the dentin'),
 'p1_su_h2': ('p1_sum', 'the demineralization involves the entire enamel layer and outer third of the dentin layer'),
 'p1_su_h56': ('p1_sum', 'Demineralization involving the pulpal third of the dentin'),
 # activity
 'p1_actvar': ('p1_ek', 'Lesion location, visual appearance, tactile feeling, and gingival bleedings'),
 'p1_highact': ('p1_ek', 'Lesions scored as ICDAS score 3, 4, 5, and 6 concerning coronal caries and score 2 concerning root caries have a high probability for being active'),
 'p1_pred': ('p1_ek', 'The highest predictive power for lesion activity was when the lesion was cavitated, the enamel was rough, and the dentin soft'),
 'p1_7pts': ('p1_ek', 'arrested lesions got at a maximum of 7 points, while active lesions achieved more than 7 points'),
 'p1_fig7': ('p1_ek', 'If 7 points or more, the lesion is active'),
 'p1_su_chalky': ('p1_sum', 'Lesion is chalky (lacks luster)'),
 'p1_su_shiny': ('p1_sum', 'Lesion has shiny surface'),
 # ICCMS
 'p1_merge': ('p1_ek', 'ICDAS scores 5 and 6), rather than using the full 7 scores'),
 'p1_mt_four': ('p1_mt', 'The seven ICDAS codes have been merged to four codes'),
 'p1_su_iccs': ('p1_sum', 'groups the ICDAS codes into four color-coded stages of caries'),
 'p1_tr_iccms': ('p1_tor', 'it proposes a risk-adjusted preventive care, control of non-cavitated lesions, and conservative restoration of the cavitated ones'),
 'p1_tr_key': ('p1_tor', 'The key elements of ICCMS are classification of the lesions according to their severity and activity, management of preventive care plan and risk status, and risk-based recall interval'),
 'p1_ada_rad': ('p1_ada', 'RA1-RA3, RB4, and RC5-RC6'),
 'p1_ada_rc6': ('p1_ada', '(RC6 = into pulp)'),
 'p1_fh_risk': ('p1_fh', 'low, moderate, or high caries risk'),
 # management
 'p1_actmgmt': ('p1_ek', 'Active lesions demand management, while inactive lesions only need to receive intervention if there is a need to reestablish aesthetics or function'),
 'p1_restor': ('p1_ek', 'extensive and most moderate lesions will require a restorative intervention'),
 'p1_initial': ('p1_ek', 'Initial caries lesions can be arrested by using non-operative approaches'),
 'p1_sdf': ('p1_ek', 'Silver Diamine Fluoride'),
 'p1_infil': ('p1_ek', 'Sealing/Infiltration of approximal lesions'),
 'p1_stepwise': ('p1_ek', 'Stepwise excavation/Indirect pulp capping'),
 'p1_prog': ('p1_ek', 'Initial lesions tended to progress 2–4 times more than sound surfaces'),
 'p1_prog10': ('p1_ek', 'were more than 10 times prone to progression than the same sound surfaces'),
 'p1_fh_nc': ('p1_fh', 'Non-cavitated active lesions should be treated using evidence-based non-restorative methods'),
 'p1_fh_cav': ('p1_fh', 'Most cavitated lesions are non-cleansable, and thus active'),
 'p1_fh_arr': ('p1_fh', 'Arrested caries lesions do not require caries interventions'),
 # evaluation
 'p1_kappa': ('p1_ek', 'The pooled intra- and inter-reproducibility in terms of kappa values were 0.67 or above'),
 'p1_sesp': ('p1_ek', 'The pooled specificity and sensitivity were both 0.7'),
 'p1_time': ('p1_ek', 'the time spent for the examination ranges from 9 to 14 min'),
 'p1_robust': ('p1_ek', 'the ICDAS is a robust caries recording system'),
 'p1_kd_chart': ('p1_kd', 'seem difficult to chart in the clinic in an easily understandable and pragmatic manner'),
 # audit u2 additions
 'p1_pkg_2004': ('p1_pkg', 'In 2004, the ICDAS (International Caries Detection and Assessment System) Foundation was convened'),
 'p1_pkg_micdas': ('p1_pkg', 'A modified ICDAS (mICDAS) carious lesion scoring system (0–4)'),
 'p1_stu_order': ('p1_stu3', 'The first is a code for the severity of the caries lesion and the second is for the restorative status of the tooth'),
}
