# Locators for P1 (PREDICTED): differentiate internal root resorption from external cervical resorption (10m).
# Every key starts with p1_.
import os
_T = os.path.expanduser('~/mds-textbooks/')
# Endodontic Radiology 2e Ch.10; offset 20 checked at PDF 173 (printed 153), 178 (158) and 181 (161).
F_EXTRA = {
 'p1_erd': (_T+'Endodontic_Radiology_2nd_ed_Chapterwise/10_10_Radiographic_Analysis_of_Acquired_Pathological_Dental_Con.md', 20, 'Azarpazhooh, 2012'),
}
BOOK_EXTRA = {
 'p1_Azarpazhooh2012': "Azarpazhooh A. Radiographic analysis of acquired pathological dental conditions. In: Basrani B, editor. Endodontic Radiology. 2nd ed. Chichester: Wiley-Blackwell; 2012. Ch.10.",
}
L = {
 # Cohen's 12e Ch.18 (Patel et al, 2021)
 'p1_c_irr_def': ('coh', 'IRR is a form of root resorption that originates in and affects the root canal wall'),
 'p1_c_confused': ('coh', 'it is often confused with external cervical resorption (ECR)'),
 'p1_c_site': ('coh', 'ECR generally develops immediately apical to the epithelial attachment of the tooth'),
 'p1_c_vital_apical': ('coh', 'the pulp apical to the site of resorption must be vital for the resorptive lesion to progress'),
 'p1_c_prrs': ('coh', 'the pulp is protected by a pericanalar resorption-resistant sheet'),
 'p1_c_pink_irr': ('coh', 'these pink spots actually are rare in cases of IRR'),
 'p1_c_pink_ecr': ('coh', 'However, it is a relatively rare feature of ECR'),
 'p1_c_bleed': ('coh', 'probing of the resorptive defect or the associated periodontal pocket causes the granulation tissue to bleed profusely'),
 'p1_c_gartner': ('coh', 'radiolucencies of uniform density that have a smooth outline and are symmetrically distributed over the root'),
 'p1_c_balloon': ('coh', 'the outline of the root canal wall should not be traceable through the resorption defect because the root canal wall balloons out'),
 'p1_c_many': ('coh', 'Although certain cases of IRR may have some or all of these radiographic features, many do not'),
 'p1_c_mottled_irr': ('coh', 'internal replacement (metaplastic) root resorption, the defect has a somewhat mottled or clouded appearance'),
 'p1_c_ecr_trace': ('coh', 'In cases of ECR, the outline of the canal wall should be visible and intact and should maintain its course as it passes through the defect'),
 'p1_c_obscured': ('coh', 'the outline of the root canal wall may be obscured by calcified tissue in the resorptive defect'),
 'p1_c_multiple': ('coh', 'in teeth with multiple canals, a canal that has been unaffected by IRR may be superimposed onto the IRR resorption defect'),
 'p1_c_slob': ('coh', 'This is sometimes referred to as the “same lingual, opposite buccal” (SLOB) rule'),
 'p1_c_irr_stay': ('coh', 'IRR lesions maintain their position relative to the root canal system on the angled view'),
 'p1_c_vaz': ('coh', 'compared the diagnostic efficacy of two CBCT scanners with periapical radiograph for the detection and classification of simulated ECR lesions'),
 'p1_c_vaz1': ('coh', 'Identification of the lesion according to the tooth surface was successful in 89.1% Morita CBCT, 87.8% Kodak CBCT, and 49.4% periapical radiograph cases'),
 'p1_c_vaz2': ('coh', 'ECR was classified correctly in 71.4% Kodak CBCT, 70% Morita CBCT, and 32% periapical radiograph'),
 'p1_c_patel100': ('coh', 'CBCT was significantly more accurate (100%) than periapical radiographs at diagnosing the presence and nature of the root resorption'),
 'p1_c_perf': ('coh', 'CBCT is particularly useful if the clinician is not sure whether the ECR cavity has perforated the root canal wall'),
 'p1_c_irr_cbct': ('coh', 'The same scan can differentiate between ECR and IRR'),
 'p1_c_irr_rct': ('coh', 'If the affected tooth is salvageable and has a reasonable prognosis, root canal treatment is necessary'),
 'p1_c_irr_bleed': ('coh', 'profuse bleeding from the granulomatous and inflamed pulpal tissues may impair visibility'),
 'p1_c_us': ('coh', 'ultrasonic activation of irrigants should be considered an essential step'),
 'p1_c_thermo': ('coh', 'the Obtura and MS systems apparently can be expected to produce the best technical results'),
 'p1_c_mta': ('coh', 'mineral trioxide aggregate (MTA) should be considered the material of choice to repair the root wall'),
 'p1_c_ecr_aims': ('coh', 'The fundamental treatment objectives in ECR are to excavate the resorptive defect, halt the resorptive process'),
 # Gulabivala & Ng 4e Ch.11
 'p1_g_prev': ('gul', 'This type of resorption has a prevalence of 0.1–1.6% in permanent teeth'),
 'p1_g_pink': ('gul', 'A pink spot may be present on the crown if resorption takes place in the pulp chamber'),
 'p1_g_vital': ('gul', 'Vital pulp tissue is required for internal resorption to progress, therefore, such teeth will give positive responses to pulp tests'),
 'p1_g_neg': ('gul', 'a negative response could not rule out the progression of resorption'),
 'p1_g_radio': ('gul', 'The radiolucency has a uniform density and the pulp chamber or canal cannot be followed through the lesion'),
 'p1_g_same': ('gul', 'The position of the radiolucency remains the same in mesial or distal angled radiographic views'),
 'p1_g_ecr_outline': ('gul', 'the outline of the pulp and root canal can be distinguished through the resorptive lesion'),
 'p1_g_probe': ('gul', 'a subgingival, supracrestal non-carious cavity may be detected'),
 'p1_g_ecr_vital': ('gul', 'The pulp remains vital in most cases'),
 # Endodontology Ch.42
 'p1_e_only': ('edl', 'Internal resorption is the only type of resorption that starts within the root canal'),
 'p1_e_misdx': ('edl', 'This may result in an inaccurate diagnosis and subsequently incorrect treatment'),
 'p1_e_centered': ('edl', 'Regardless of the projection angle of the radiograph, internal resorption remains centered in the root'),
 'p1_e_moves': ('edl', 'Invasive cervical resorption moves away from the canal if the angle of projection of the radiograph is changed'),
 'p1_e_pink': ('edl', 'the presence of a pink spot in the coronal dentin can be a feature of both internal and invasive cervical resorption'),
 'p1_e_sens': ('edl', 'In both conditions, a pulpal sensibility test is likely to be positive, because the pulp remains (partially) vital'),
 # Seltzer & Bender 2e Ch.17 (Levin, 2012)
 'p1_s_pathog': ('sel', 'has been thought to be pathognomonic of internal root resorption'),
 'p1_s_box_ecr': ('sel', 'Lesion at the attachment level of the tooth'),
 'p1_s_crestal': ('sel', 'Crestal bony defect associated with the lesion'),
 'p1_s_box_irr': ('sel', 'Lesion at any location along the root canal (not only at attachment level)'),
 'p1_s_nobone': ('sel', 'Radiolucency contained in the root without an adjacent bony defect'),
 'p1_s_bor': ('sel', 'it is usually possible to distinguish whether the external root defect is buccal or palatolingual by using the buccal object rule'),
 'p1_s_running': ('sel', 'can usually be seen “running through” the radiolucent defect'),
 'p1_s_portal': ('sel', 'enhances visualization of the portals of entrance in the case of external resorption'),
 'p1_s_majority': ('sel', 'The majority of misdiagnoses of resorptive defects are made in distinguishing between subepithelial external root resorption and internal root resorption'),
 'p1_s_bleed': ('sel', 'if bleeding continues during treatment, particularly if it is still present at the second visit, the source of the blood supply is external'),
 'p1_s_fill': ('sel', 'Failure to fill the canal suggests an external lesion'),
 # Sikri 2e Ch.27
 'p1_k_pinkusual': ('sik', 'Pink spot is a usual sign'),
 'p1_k_bleedpulp': ('sik', 'during pulp extirpation if excessive bleeding occurs clinically, internal resorption should be suspected'),
 'p1_k_moves': ('sik', 'The defect moves away from the canal as the angulation'),
 'p1_k_sharp': ('sik', 'Cavity has sharp edges'),
 # Endodontic Radiology 2e Ch.10 (Azarpazhooh, 2012)
 'p1_r_oval': ('p1_erd', 'a localized oval-shaped radiolucent enlargement within the pulp chamber that is continuous with the image of the pulp chamber or root canal space'),
 'p1_r_origin': ('p1_erd', 'The resorbing cells in internal resorption are pulpal in origin'),
 'p1_r_pinkmore': ('p1_erd', 'However, these pink spots are more commonly seen in cases of external cervical root resorption'),
 'p1_r_sens': ('p1_erd', 'sensitivity tests are normal, except in very advanced cases where the root canal is perforated'),
 'p1_r_misdx': ('p1_erd', 'Cervical root resorptions are often misdiagnosed as internal root resorption, especially if they are accessible by probing'),
 'p1_r_borders': ('p1_erd', 'have borders that are ill-defined and asymmetrical, with radiodensity variations within the lesion'),
}
