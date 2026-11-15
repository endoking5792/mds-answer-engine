# Locators for Q08 "Dental caries - etiological factors and methods of diagnosis" (20m). All keys prefixed q08_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
O = T + 'Operative_and_Dental_Materials_Textbooks/'
DET = O + 'Detection_and_Assessment_of_Dental_Caries.md'
F_EXTRA = {
 # Kidd and Fejerskov 4e 2016 (authored book). Offset 13 confirmed at PDF 62 (printed 49) and PDF 98 (printed 85).
 'q08_kd': (O+'Essentials_of_Dental_Caries_4th.md', 13, 'Kidd and Fejerskov, 2016'),
 # Sturdevant 2e SA; editors cited. Offset 19 confirmed at PDF 46 (printed 27) and PDF 122 (printed 103).
 'q08_st': (O+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ferreira Zandoná and Ritter, 2019'),
 'q08_st3': (O+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Boushell and Shugars, 2019'),
 # Sikri 2020. Offset 19 confirmed at PDF 53 (printed 34) and PDF 120 (printed 101).
 'q08_sk': (O+'Textbook_of_Conservative_and_Restorative_Dentistry.md', 19, 'Sikri, 2020'),
 # Summitt 4e Ch.5 (Amaechi, van Amerongen, van Loveren, Kidd); no printed page numbers.
 'q08_su': (O+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Amaechi et al, 2013'),
 # Detection book Ch.11 (offset 1: PDF 110 = p109, 111 = p110); Ch.16 Kim (offset 0: PDF 159/160); Ch.17 Neuhaus and Lussi (offset 0: PDF 171/172).
 'q08_bw': (DET, 1, 'Schwendicke and Göstemeyer, 2019'),
 'q08_ql': (DET, 0, 'Kim, 2019'),
 'q08_dd': (DET, 0, 'Neuhaus and Lussi, 2019'),
}
L = {
 'q08_kd_def': ('q08_kd', 'It is a localized, chemical dissolution of a tooth surface brought about by metabolic activity in a microbial deposit (a dental biofilm)'),
 'q08_st_def': ('q08_st', 'This multifactorial, oral disease is caused primarily by an imbalance of the oral flora (biofilm)'),
 'q08_sk_multi': ('q08_sk', 'Dental caries is a multifactorial disease. Till today, no single theory can explain the phenomenon of caries'),
 'q08_sk_miller': ('q08_sk', 'Dental decay is a chemicoparasitic process consisting of the dissolution of the hard inorganic and the soft organic part'),
 'q08_sk_miller2': ('q08_sk', 'Miller (1889) propagated the concept of acid formation in the oral cavity'),
 'q08_sk_gott': ('q08_sk', 'Gottlieb (1944) was of the view that instead of decalcification of inorganic part'),
 'q08_sk_schatz': ('q08_sk', 'Schatz et al. (1955) hypothesized that the microbial degradation of organic component by proteolysis followed by dissolution of inorganic part by the process of chelation lead to caries'),
 'q08_sk_levine': ('q08_sk', 'demineralization and remineralization of enamel is a continuous process'),
 'q08_sk_feath': ('q08_sk', 'caries is the outcome of disturbance in balance between pathological and protective factors'),
 'q08_sk_four': ('q08_sk', 'Caries develop because of interaction of four principle factors; the host, the microflora, the diet (substrate) and the time'),
 'q08_sk_mand': ('q08_sk', 'The most susceptible teeth are the mandibular first molars amongst the permanent teeth'),
 'q08_sk_vip': ('q08_sk', 'The famous Vipeholm Study was conducted on 436 adult inmates in a mental institution'),
 'q08_sk_vip2': ('q08_sk', 'The risk of sugar increasing caries activity is greatest, if sugar is consumed between meals'),
 'q08_sk_cem': ('q08_sk', 'cementum begins to demineralize at pH 6.7'),
 'q08_sk_lacto': ('q08_sk', 'lactobacilli, which account for one-third of the oral flora'),
 'q08_sk_infect': ('q08_sk', 'It has been established that caries is a bacterial infection'),
 'q08_sk_2h': ('q08_sk', 'It takes around two hours to return the pH to normal'),
 'q08_sk_cat': ('q08_sk', 'Caries activity tests are primarily undertaken to evaluate the susceptibility of the individual towards caries'),
 'q08_kd_biofilm': ('q08_kd', 'caries being a biofilm induced disease'),
 'q08_kd_ms': ('q08_kd', 'Mutans streptococci are part of the resident flora, but are in very low numbers in most caries free individuals'),
 'q08_kd_gene': ('q08_kd', 'There is no evidence to support inheritance as a factor explaining the disparity in caries prevalence'),
 'q08_st_four': ('q08_st', 'Dental caries is a disease that is dependent on the complex interrelationships between the following four critical parameters'),
 'q08_st_comm': ('q08_st', 'there are no specific pathogens that correlate with dental caries, but rather microbial communities'),
 'q08_st_aep': ('q08_st', 'Within 2 h, a cell-free, organic film, the acquired enamel pellicle (AEP)'),
 'q08_st_cph': ('q08_st', 'below a critical level (5.5 for enamel, 6.2 for dentin)'),
 'q08_st_pits': ('q08_st', 'Pits and fissures are particularly susceptible surfaces for caries lesion initiation'),
 'q08_st_prox': ('q08_st', 'The proximal enamel surfaces immediately gingival to the contact area are the second most susceptible areas'),
 'q08_st_freq': ('q08_st', 'Caries activity is most strongly stimulated by the frequency, rather than the quantity, of sucrose ingested'),
 'q08_st_flow': ('q08_st', 'Adults produce 1–1.5 L of saliva a day'),
 'q08_st_buf': ('q08_st', 'Primary buffer: bicarbonate ion concentration'),
 'q08_st_rad': ('q08_st', 'destruction of the teeth in just a few months after radiation treatment'),
 'q08_st_cpitn': ('q08_st3', 'The recommended instrument for assessment of surface roughness is the Community Periodontal Index of Treatment Needs (CPITN) probe having a 0.5 mm sphere at the tip'),
 'q08_st_soc': ('q08_st3', 'The standard of care for diagnosis of caries remains visual inspection of well-illuminated, clean and dry teeth, with use of radiographs as indicated'),
 'q08_st_25': ('q08_st3', 'approximately 25% mineral loss has to occur before a radiolucency begins to appear on a radiograph'),
 'q08_st_notest': ('q08_st3', 'their diagnostic accuracy has not been firmly established'),
 'q08_st_acist': ('q08_st3', 'alternating current (AC) impedance spectroscopy (ACIST)'),
 'q08_st_bact': ('q08_st', 'Use of supplemental tests to analyse the bacterial component of the biofilm has little value to determine the'),
 'q08_kd_det': ('q08_kd', 'Is a lesion present? This is detection of the lesion'),
 'q08_kd_diag': ('q08_kd', 'adding the aspect of activity to detection, is diagnosis'),
 'q08_kd_probe': ('q08_kd', 'Sharp probes should never be used'),
 'q08_kd_ic0': ('q08_kd', 'Sound after air drying for 5 seconds'),
 'q08_kd_ic6': ('q08_kd', 'Extensive distinct cavity with visible dentine'),
 'q08_kd_nyact': ('q08_kd', 'Active, non-cavitated lesions, are plaque covered, often close to an inflamed gingival margin, and have a matt appearance'),
 'q08_kd_nyina': ('q08_kd', 'These lesions have a plaque-free, shiny, lustrous surface'),
 'q08_kd_rxact': ('q08_kd', 'Remember the radiograph cannot diagnose activity'),
 'q08_kd_foti': ('q08_kd', 'fibre optic lights, with the beam reduced to 0.5 mm in diameter'),
 'q08_kd_sep': ('q08_kd', 'After a few days the teeth are separated'),
 'q08_kd_research': ('q08_kd', 'So far they only have research interest as they do not enable the dentist to make a final treatment decision'),
 'q08_bw_sens1': ('q08_bw', 'bitewing radiography has a sensitivity of around 0.2–0.3 for early lesions'),
 'q08_bw_spec': ('q08_bw', 'The specificity is around or above 0.9'),
 'q08_ql_405': ('q08_ql', 'blue visible light with a wavelength of 405 nm induces fluorescence within the tooth structure'),
 'q08_dd_655': ('q08_dd', 'Both devices operate at a wavelength of 655 nm'),
 'q08_dd_99': ('q08_dd', 'a digital value between 0 and 99'),
 'q08_su_dd': ('q08_su', 'detection only describes the clinical signs of caries, diagnosis tries to estimate the dynamics and determinants of the process'),
}
L.update({
 'q08_sk_lev77': ('q08_sk', 'Levine (1977) hypothesized'),
 'q08_sk_fe99': ('q08_sk', 'Featherstone (1999) proposed'),
})
# Audit u1 (2026-11-15): Harpreet Singh 2nd (2020) Ch.5. Offset 17: PDF 52 printed 35, PDF 57 printed 40 (as Q16/Q17).
F_EXTRA['q08_sg'] = (O + 'Essentials_of_Preclinical_Conservative_Dentistry_Harpreet_Singh.md', 17, 'Singh, 2020')
L.update({
 'q08_sg_keyes': ('q08_sg', 'described by Keyes in 1960 as caries triad'),
 'q08_sg_newbrun': ('q08_sg', 'as proposed by Newbrun in 1982'),
 'q08_st_lowf': ('q08_st', 'Fluoride. Decreased fluoride exposure'),
 'q08_st_xero': ('q08_st', 'Use of medications that cause xerostomia'),
 'q08_st_age': ('q08_st', 'Children and older adults have increased risks'),
 'q08_st_ses': ('q08_st', 'Lower educational attainment'),
 'q08_sk_root67': ('q08_sk', 'the root surface is more vulnerable to the demineralization process than enamel'),
 'q08_sk_snyder': ('q08_sk', 'Snyder introduced a relatively simple colorimetric test'),
 'q08_sk_alban': ('q08_sk', 'The Alban test eliminates the need for melting'),
 'q08_sk_reduct': ('q08_sk', 'The test measures the activity of the enzyme reductase'),
 'q08_sk_lbcount': ('q08_sk', 'Lactobacillus Colony Count Test'),
 'q08_kd_elastic': ('q08_kd', 'A small round elastic is forced between the contact points'),
})
