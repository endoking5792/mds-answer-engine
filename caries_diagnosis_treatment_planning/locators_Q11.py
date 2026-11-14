# Locators for Q11 "Caries Risk Assessment." (10m). All keys prefixed q11_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
O = T + 'Operative_and_Dental_Materials_Textbooks/'
F_EXTRA = {
 # Summitt's 4e (2013) Ch.5 (Amaechi, van Amerongen, van Loveren and Kidd); no printed page numbers in the file.
 'q11_sum': (O+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Amaechi et al, 2013'),
 # Sturdevant 2e South Asia (2019) Ch.2 (contributors Ferreira Zandona and Ritter). Offset 19 confirmed at PDF 74 (printed 55), PDF 75 (56), PDF 77 (58).
 'q11_st': (O+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ferreira Zandoná and Ritter, 2019'),
 'q11_st3': (O+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Boushell and Shugars, 2019'),
 # Mount 3e (2016) Ch.3 (Ngo, Wolff and Hume). Offset 16 confirmed at PDF 50 (printed 34), PDF 51 (35), PDF 54 (38).
 'q11_mt': (O+'Preservation_and_Restoration_of_Tooth_Structure_Mount.md', 16, 'Ngo, Wolff and Hume, 2016'),
 # Sikri, Textbook of Conservative and Restorative Dentistry (CBS, eBook 2020) Ch.6. Offset 19 confirmed at PDF 117 (printed 98), PDF 118 (99), PDF 120 (101).
 'q11_sik': (O+'Textbook_of_Conservative_and_Restorative_Dentistry.md', 19, 'Sikri, 2020'),
 # Pickard's Guide 10e (2015), Banerjee and Watson, Ch.3. Offset 11 confirmed at PDF 56 (printed 45), PDF 57 (46), PDF 58 (47).
 'q11_pk': (O+'Pickards_Guide_to_Minimally_Invasive_Operative_Dentistry.md', 11, 'Banerjee and Watson, 2015'),
 # Detection and Assessment of Dental Caries (2019) Ch.7 ADA CCS (Zeller, Young and Novy). Offset 4 confirmed at PDF 61 (printed 57), PDF 62 (58), PDF 64 (60).
 'q11_ccs': (O+'Detection_and_Assessment_of_Dental_Caries.md', 4, 'Zeller, Young and Novy, 2019'),
 # Same book Ch.23 (Fontana and Huysmans). Offset -4 confirmed at PDF 227 (printed 231), PDF 228 (232), PDF 229 (233).
 'q11_dm': (O+'Detection_and_Assessment_of_Dental_Caries.md', -4, 'Fontana and Huysmans, 2019'),
 # Modern Operative Dentistry (2020) Ch.1 (Torres, Barbe, Noack and Wicht). Offset 14 confirmed at PDF 40 (printed 26), PDF 41 (27), PDF 42 (28).
 'q11_mod1': (O+'Modern_Operative_Dentistry.md', 14, 'Torres et al, 2020'),
}
L = {
 'q11_sum_def': ('q11_sum', 'Caries risk may be defined as the probability of an individual developing a certain number of caries lesions reaching a given stage of disease progression during a specified period'),
 'q11_sik_def': ('q11_sik', 'Caries risk assessment is the procedure to predict the future caries development before the classical onset of disease'),
 'q11_st_rf': ('q11_st', 'A risk factor is defined as an environmental, behavioural or biologic factor that directly increases the probability that a disease will occur'),
 'q11_st_ri': ('q11_st', 'Risk indicators may refer to existing signs of the disease process'),
 'q11_st_past': ('q11_st', 'Past caries experience is the best predictor of future caries activity'),
 'q11_st_bal': ('q11_st', 'The caries balance model is based on minimizing pathologic factors while maximizing protective factors'),
 'q11_st_ideal': ('q11_st', 'The ideal caries risk assessment model should be inexpensive, easy to use and have high degrees of accuracy in predictive value'),
 'q11_st_ind1': ('q11_st', 'Brown spots, active white spots or cavitated lesions on free smooth surfaces'),
 'q11_st_ind2': ('q11_st', 'Restorations placed in the past 3 years'),
 'q11_st_diet': ('q11_st', 'Quantity and frequency of sucrose intake'),
 'q11_st_iccms': ('q11_st', 'has endeavoured to merge caries detection and assessment with an individualized management plan'),
 'q11_st_cario': ('q11_st', 'Another caries risk assessment method that has been validated for children is the Cariogram'),
 'q11_st_r3': ('q11_st', '3-Month re-care examination and oral prophylaxis'),
 'q11_st_r46': ('q11_st', '4–6-Month re-care examination and oral prophylaxis'),
 'q11_st_r912': ('q11_st', '9–12-Month re-care examination and oral prophylaxis'),
 'q11_st_bw': ('q11_st', 'Bitewing radiographs every 6–12 months'),
 'q11_st_var': ('q11_st', 'Fluoride varnish at each re-care visit'),
 'q11_st_5000': ('q11_st', 'Brush with prescription fluoride dentifrice (e.g. 1/1%/5000 ppm NaF)'),
 'q11_st_sal': ('q11_st', 'The caries risk predictive value for salivary tests is not fully demonstrated by strong evidence in all circumstances'),
 'q11_sum_3sec': ('q11_sum', 'a tool for comprehensive caries risk assessment should consist of three major sections'),
 'q11_sum_subj': ('q11_sum', 'The first part is the subjective section'),
 'q11_sum_obj': ('q11_sum', 'The second part is the objective section'),
 'q11_sum_syn': ('q11_sum', 'The third part is the synthesis section that identifies the overall risk level (low, moderate, high) of the patient'),
 'q11_sum_sfr': ('q11_sum', 'Resting SFR < 0.2 mL/min ≥ 0.2 mL/min Stimulated SFR < 0.7 mL/min ≥ 0.7 mL/min'),
 'q11_sum_cho': ('q11_sum', 'Carbohydrate frequency > 7 times per day'),
 'q11_sum_mod': ('q11_sum', 'One or two white spots or cavitated primary or secondary caries lesions in the last 3 years'),
 'q11_sum_high': ('q11_sum', 'Three or more white spots or cavitated primary or secondary caries lesions in the last 3 years'),
 'q11_sum_bw': ('q11_sum', 'every 3 to 6 months for patients at high caries risk, every 12 to 18 months for moderate caries risk, and every 24 months for low caries risk'),
 'q11_sum_ctrl': ('q11_sum', 'dentists should concentrate on controlling the caries lesions their patients have at present'),
 'q11_sum_clin': ('q11_sum', 'Clinical and radiographic examination and dental history are the most important sources of information'),
 'q11_mt_cg9': ('q11_mt', 'uses nine weighted parameters to help identify patients at high risk of developing caries'),
 'q11_mt_cgpc': ('q11_mt', 'percentage chance of avoiding caries in the future'),
 'q11_mt_cgsoc': ('q11_mt', 'The Cariogram does not weight social factors toward caries risk'),
 'q11_mt_cam4': ('q11_mt', 'Risk in the CAMBRA system is categorized as one of four levels: extremely high, high, moderate and low.'),
 'q11_mt_camhi': ('q11_mt', 'the presence of any of these recent activity indicators automatically identifies a patient as being in the high risk category'),
 'q11_mt_camex': ('q11_mt', 'plus salivary hypofunction, in which case the patient is raised to the extremely high risk category'),
 'q11_mt_cam3y': ('q11_mt', 'Recent caries activity is considered to be the development of any new lesions during the past three years'),
 'q11_mt_tl15': ('q11_mt', 'The system collects information on each of the 15 risk factors listed below, under the five general headings'),
 'q11_mt_tlact': ('q11_mt', 'not predicting future risk'),
 'q11_mt_none': ('q11_mt', 'None of them alone has a high predictive value for caries'),
 'q11_sik_tl19': ('q11_sik', 'The model investigates nineteen risk factors and scores a red, yellow or green light for each risk factor'),
 'q11_pk_hi': ('q11_pk', 'a patient at high risk for caries is one who presents with or has a history of two or more new, progressing, and/or restored carious lesions in the previous 2 years'),
 'q11_pk_simple': ('q11_pk', 'A simpler division into low or high risk/susceptibility is usually more than sufficient'),
 'q11_pk_recall': ('q11_pk', 'should not be standardized at 6 months or any other period'),
 'q11_pk_change': ('q11_pk', 'The caries risk assessment will change over time'),
 'q11_ccs_cam': ('q11_ccs', '(1) assessing the risk for future caries lesions, (2) reducing the pathological factors, (3) enhancing the protective factors, and (4) using minimally invasive restorative care as indicated'),
 'q11_dm_ess': ('q11_dm', 'Risk assessment is an essential component in the decision-making process'),
 'q11_dm_subj': ('q11_dm', 'overall subjective impression of the patient might have good predictive power for caries risk'),
 'q11_mod1_goal': ('q11_mod1', 'Elimination or control of etiological factors should be the primary goal in high-risk patients'),
}
