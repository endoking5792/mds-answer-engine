import os
# Added locators from the second-reader audit of Q01, P1, P2, P3 (AUDIT_u1.md). Every key starts with u1_.
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
F_EXTRA = {
 # Sikri 2e Ch.10 (second eBook edition 2019). Offset 21 confirmed at PDF 164 (printed 143) and PDF 166 (printed 145).
 'u1_sik': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/10_10_Endodontic_Case_Selection_Treatment_Planning.md', 21, 'Sikri, 2019'),
 # Grossman's 14e Ch.8 (editor Gopikrishna, 2021). Offset 25 confirmed at PDF 169 (printed 144) and PDF 170 (printed 145).
 'u1_gro': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/08_Chapter_8_Selection_of_Cases_for_Treatment.md', 25, 'Gopikrishna, 2021'),
 # Treatment of Endodontic Infections 2e (Siqueira and Rocas, eds, 2022) Ch.9 (Fouad); PDF page only (read, not cited in an answer).
 'u1_toei': (T+'Treatment_of_Endodontic_Infections_Chapterwise/09_Chapter_9_Systemic_implications_of_endodontic_infections.md', None, 'Fouad, 2022'),
 # Endodontic Microbiology 2e (Fouad, ed., 2017) Ch.16 (Fouad); PDF page only (read, not cited in an answer).
 'u1_emic': (T+'Endodontic_Microbiology_2nd_ed_Chapterwise/17_Chapter_16_Endodontic_Infections_and_Systemic_Disease.md', None, 'Fouad, 2017'),
}
L = {
 # ---------- Q01 ----------
 'u1_tor_rare': ('q01_tor', 'Allergies to specific materials or reagents used in endodontics are rare'),
 'u1_cc_vaso6': ('q01_cc', 'recent myocardial infarctions (less than 6 months)'),
 'u1_coh_vaso730': ('q01_coh', 'those who have had an MI within the past 7 to 30 days and unstable angina'),
 'u1_coh_mi30': ('q01_coh', 'within the past 30 days (major risk category), elective treatment should be postponed'),
 'u1_cc_elect6': ('q01_cc', 'less than 6 months prior to dental consultation should be deterred from elective dental care'),
 'u1_gul_6mo': ('q01_gul', 'Routine dental treatment should be avoided where appropriate for at least 6 months following a myocardial infarct'),
 'u1_ing_pm_low': ('q01_ing', 'the possibility for electrical interference seems to be very low'),
 'u1_cc_pm_sens': ('q01_cc', 'These devices have been shown to be sensitive to electromagnetic signals'),
 'u1_cc_pm_new': ('q01_cc', 'Although the newer models (bipolar devices with electromagnetic shielding) are generally not affected'),
 'u1_coh_gran2000': ('q01_coh', 'routine dental procedures can be performed if the granulocyte count is greater than 2000/mm3'),
 'u1_cc_neut2000': ('q01_cc', 'if the neutrophil count is greater than 2000 cells/mm3'),
 'u1_coh_cd4': ('q01_coh', 'CD4+ cell count exceeding 350 cells/mm3 may receive all indicated dental treatments'),
 'u1_sik_cd4': ('u1_sik', 'Patients with CD4 count above 400 mm3 are considered asymptomatic HIV candidates and can be treated in routine'),
 'u1_sik_dm': ('u1_sik', 'The standard protocol is followed, wherein prophylactic antibiotics are prescribed'),
 'u1_ing_t316': ('q01_ing', 'Single Dose Given 30 to 60 Minutes Before'),
 'u1_gro_t81': ('u1_gro', 'AHA-Recommended Antibiotic Prophylaxis Regimens to be Taken 1 Hour Prior to the Dental Procedure'),
 'u1_sik_pen': ('u1_sik', '2.0 gm penicillin V, one hour before the procedure followed by 1.0 gm every 6 hours postoperatively'),
 # ---------- P1 ----------
 'u1_tor_mech': ('q01_tor', 'These individuals may select for specific microorganisms that may be more virulent'),
 'u1_tor_confound': ('q01_tor', 'confounded by the fact that diabetes and cardiovascular diseases are also associated with periodontal disease'),
 'u1_cc_brittle': ('q01_cc', 'In the uncontrolled or brittle diabetic patient, only acute dental infection should be treated on an outpatient basis'),
 'u1_cc_noepi': ('q01_cc', 'Delivered anesthetic should not include epinephrine'),
 'u1_coh_brittle': ('q01_coh', 'may be prescribed for a patient with brittle (very difficult to control) diabetes'),
 # ---------- P2 ----------
 'u1_cc_rad1': ('q01_cc', 'Avoid routine radiographs. Use selectively and when needed.'),
 'u1_coh_xray': ('q01_coh', 'the risk of not having a needed x-ray could be much greater than the risk from the radiation'),
 # ---------- P3 ----------
 'u1_har_nice08': ('q01_har', 'in 2008, NICE recommended that people at risk of developing IE undergo dental procedures'),
 'u1_har_nicenoabx': ('q01_har', 'antibiotic prophylaxis is not recommended'),
 'u1_har_nicecx': ('q01_har', 'chlorhexidine mouthwash should not be offered'),
 'u1_har_nicecause': ('q01_har', 'any increase in the incidence of IE has not been well understood'),
 'u1_ing_eng': ('q01_ing', 'a recent study in England demonstrated an increase in cases of infective endocarditis following the widespread adoption of the new standards in 2008'),
 'u1_ing_eng_caus': ('q01_ing', 'a causal relationship has not been established'),
 # ---------- read, not cited in an answer (sidecar record) ----------
 'u1_toei_bact': ('u1_toei', 'bacteremia may develop in 17% to 54% of cases during nonsurgical root canal treatment, and up to 83% following surgical treatment'),
 'u1_toei_abx': ('u1_toei', 'antibiotics do not prevent bacteremia following dental'),
 'u1_toei_hba1c': ('u1_toei', 'had a hemoglobin A1c (HbA1c) of over 5.7%'),
 'u1_emic_ext': ('u1_emic', 'which was reduced to 33% if the patient was on amoxicillin'),
 'u1_emic_brush': ('u1_emic', 'the cumulative incidence of bacteremia following tooth brushing in this study was 23%'),
 'u1_emic_dm': ('u1_emic', 'diabetic patients had a significantly higher risk of lack of'),
}
