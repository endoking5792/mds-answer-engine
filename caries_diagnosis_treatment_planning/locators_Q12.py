# Locators for Q12 "Role of saliva in diagnosis of dental caries" (10m). All keys prefixed q12_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
O = T + 'Operative_and_Dental_Materials_Textbooks/'
F_EXTRA = {
 # Sturdevant 2e South Asia (2019) Ch.2 (Ferreira Zandona and Ritter). Offset 19 confirmed at PDF 53 (printed 34), PDF 54 (35), PDF 77 (58).
 'q12_st': (O+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ferreira Zandona and Ritter, 2019'),
 # Kidd and Fejerskov 4e (2016). Offset 13 confirmed at PDF 52 (printed 39), PDF 159 (146), PDF 160 (147).
 'q12_kid': (O+'Essentials_of_Dental_Caries_4th.md', 13, 'Kidd and Fejerskov, 2016'),
 # Mount 3e (2016) Ch.3 (Ngo, Wolff and Hume). Offset 16 confirmed at PDF 55 (printed 39), PDF 57 (41), PDF 59 (43).
 'q12_mt': (O+'Preservation_and_Restoration_of_Tooth_Structure_Mount.md', 16, 'Ngo, Wolff and Hume, 2016'),
 # Sikri (CBS eBook 2020) Ch.6. Offset 19 confirmed at PDF 120 (printed 101), PDF 123 (104).
 'q12_sik': (O+'Textbook_of_Conservative_and_Restorative_Dentistry.md', 19, 'Sikri, 2020'),
 # Summitt's 4e (2013) Ch.5 (Amaechi et al); no printed page numbers.
 'q12_sum': (O+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Amaechi et al, 2013'),
 # Modern Operative Dentistry (2020) Ch.1 (Torres, Barbe, Noack and Wicht). Offset 14 confirmed at PDF 40 (printed 26), PDF 42 (28).
 'q12_mod1': (O+'Modern_Operative_Dentistry.md', 14, 'Torres et al, 2020'),
 # Modern Operative Dentistry (2020) Ch.3 (Caneppele et al). Offset 14 confirmed at PDF 91 (printed 77), PDF 94 (80).
 'q12_mod3': (O+'Modern_Operative_Dentistry.md', 14, 'Caneppele et al, 2020'),
 # Advanced Operative Dentistry (2011) Ch.1 (Ricketts, Chadwick and Hall). Offset 8 confirmed at PDF 17 (printed 9), PDF 18 (10).
 'q12_aod': (O+'Advanced_Operative_Dentistry.md', 8, 'Ricketts, Chadwick and Hall, 2011'),
 # Endodontic Microbiology 2e (Fouad ed, 2017) Ch.3 (Love and Tanner). Offset 11 confirmed at PDF 42 (printed 31), PDF 43 (32), PDF 44 (33).
 'q12_em': (T+'Endodontic_Microbiology_2nd_ed_Chapterwise/03_Chapter_3_Microbiology_of_Dental_Caries_and_Dentinal.md', 11, 'Love and Tanner, 2017'),
}
L = {
 'q12_st_nat': ('q12_st', 'it also plays a key role as a natural anticaries agent'),
 'q12_st_qty': ('q12_st', 'It is suggested that caries susceptibility in healthy individuals is not related to saliva composition but more importantly to the quantity of saliva'),
 'q12_st_prot': ('q12_st', 'similar levels of antibacterial proteins can be found in caries-active and caries-free individuals'),
 'q12_st_lys': ('q12_st', 'Lysozyme, lactoperoxidase, lactoferrin and agglutinins are salivary proteins that possess antibacterial activity'),
 'q12_st_bic': ('q12_st', 'Primary buffer: bicarbonate ion concentration'),
 'q12_st_test': ('q12_st', 'salivary testing should be done on patients with signs and symptoms of hyposalivation'),
 'q12_st_3': ('q12_st', 'I. Salivary flow rate II. Salivary buffering capacity III. Salivary pH'),
 'q12_st_still': ('q12_st', 'Patients with good saliva flow and adequate buffering capacity can still have caries'),
 'q12_st_pred': ('q12_st', 'The caries risk predictive value for salivary tests is not fully demonstrated by strong evidence in all circumstances'),
 'q12_st_little': ('q12_st', 'the bacterial component of the biofilm has little value to determine the'),
 'q12_st_kits': ('q12_st', 'These kits provide data on simulated flow rates, the pH of saliva and the level of buffering capacity'),
 'q12_st_6m': ('q12_st', 'Every 6 months, salivary evaluations are repeated'),
 'q12_kid_mirror': ('q12_kid', 'Mirror sticks to mucosa or tongue'),
 'q12_kid_pool': ('q12_kid', 'No saliva pooling in the floor of the mouth'),
 'q12_kid_when': ('q12_kid', 'Unstimulated and stimulated salivary flow rates should be measured where a dry mouth is suspected, or in cases where a high caries incidence cannot be explained'),
 'q12_kid_n1': ('q12_kid', 'Unstimulated: 0.3–0.5 ml/min.'),
 'q12_kid_n2': ('q12_kid', 'Stimulated: 1–2 ml/min'),
 'q12_kid_90': ('q12_kid', 'the patient should not eat or drink for 90 minutes'),
 'q12_kid_10': ('q12_kid', 'The patient sits quietly in the dental chair for 10 minutes, without chewing or swallowing'),
 'q12_kid_5': ('q12_kid', 'Saliva formed over 5 minutes is expectorated into a disposable cup'),
 'q12_kid_ph': ('q12_kid', 'In healthy individuals, pH varies between 6.0 and 7.5, being most alkaline under stimulated flow rates'),
 'q12_kid_bic': ('q12_kid', 'the more stimulated the saliva production, the higher the levels of bicarbonate'),
 'q12_kid_bio': ('q12_kid', 'salivary microbial and biochemical biomarkers that might be used clinically to assess caries risk'),
 'q12_kid_non': ('q12_kid', 'In the face of the multiplicity of microorganisms, this is nonsense!'),
 'q12_kid_sm': ('q12_kid', 'does not allow a distinction between high or low caries experience in children'),
 'q12_mt_drop': ('q12_mt', 'Droplets of saliva appear after more than 60 seconds'),
 'q12_mt_cons': ('q12_mt', 'Thick, ropey or frothy, extended web test'),
 'q12_mt_ph': ('q12_mt', 'Unstimulated saliva pH < 5.8 [15] Red'),
 'q12_mt_ph2': ('q12_mt', 'Unstimulated saliva pH > 6.8 [15] Green'),
 'q12_mt_flow': ('q12_mt', 'A stimulated salivary flow of 0.7 ml/min. is accepted as the threshold below which there is an increased risk of caries'),
 'q12_mt_only': ('q12_mt', 'Although caries risk is strongly associated with only stimulated salivary flow rate'),
 'q12_mt_5ml': ('q12_mt', 'Stimulated saliva after 5 min. < 3.5 ml'),
 'q12_mt_buf': ('q12_mt', 'There are four systems currently available for measuring the buffering capacity of stimulated saliva'),
 'q12_mt_cfu': ('q12_mt', '> 105 CFU >105 CFU Red'),
 'q12_mt_low': ('q12_mt', 'a low S. mutans count in saliva suggests a low level of caries activity'),
 'q12_mt_high': ('q12_mt', 'a high S. mutans count in saliva is possible with high or low caries activity'),
 'q12_mt_lb': ('q12_mt', 'a high level suggests a diet high in fermentable carbohydrate'),
 'q12_mt_next': ('q12_mt', 'The next generation of tests will probably be based on the use of monoclonal antibodies or enzymes'),
 'q12_mt_cg': ('q12_mt', 'Mutans streptococci and lactobacilli counts in saliva'),
 'q12_sik_bf': ('q12_sik', 'The amount of lactic acid needed to reduce the pH from 7.0 to 6.0 is a measure of buffer capacity'),
 'q12_sik_inv': ('q12_sik', 'There is an inverse relationship of buffering capacity of saliva and caries'),
 'q12_sum_low': ('q12_sum', 'low counts are often good predictors of low risk but that the opposite is not necessarily true'),
 'q12_sum_sfr': ('q12_sum', 'Resting SFR < 0.2 mL/min ≥ 0.2 mL/min Stimulated SFR < 0.7 mL/min ≥ 0.7 mL/min'),
 'q12_mod1_n': ('q12_mod1', 'The normal values must be between 1.5 and 3 ml/min.'),
 'q12_mod1_sev': ('q12_mod1', 'A flow between 0.05 and 0.5 indicates a severe hyposalivation'),
 'q12_mod3_lb': ('q12_mod3', 'the detection of a high concentration of Lactobacillus in the saliva (>100,000/ml) would work as an excellent indicator of risk for progression of initial preexisting caries'),
 'q12_aod_n': ('q12_aod', 'SALIVA FLOW UNSTIMULATED ml/min STIMULATED ml/min Normal 0.3 1.5 Dry mouth'),
 'q12_aod_comp': ('q12_aod', 'More recent evidence suggests that these salivary counts are not good in predicting future caries'),
 'q12_em_sm': ('q12_em', 'these species have not universally proved reliable in risk assessment'),
 'q12_kid_froth': ('q12_kid', 'Saliva frothy.'),
 'q12_mt_lip': ('q12_mt', 'Roll the lower lip outwards and dry with a gauze square'),
 'q12_mt_corr': ('q12_mt', 'This is the one salivary factor that is most likely to be highly correlated with caries activity'),
 'q12_mt_strip': ('q12_mt', 'Thoroughly wet the pads on the test strip with saliva'),
}
