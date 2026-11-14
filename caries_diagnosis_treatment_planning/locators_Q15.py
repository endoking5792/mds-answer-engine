# Locators for Q15 "Dye detection of caries." (10m). All keys prefixed q15_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
B = T + 'Operative_and_Dental_Materials_Textbooks/'
F_EXTRA = {
 # Detection and Assessment of Dental Caries (2019) Ch.9 Caries detection dyes, Maltz, Arthur and Fatturi-Parolo. Offset 2 confirmed at PDF 85 (printed 83) and PDF 97 (printed 95).
 'q15_mal': (B+'Detection_and_Assessment_of_Dental_Caries.md', 2, 'Maltz et al., 2019'),
 # Sikri VK, Textbook of Conservative and Restorative Dentistry (CBS, eBook 2020) Ch.7. Offset 19 confirmed at PDF 134 (printed 115) and PDF 151 (printed 132).
 'q15_sik': (B+'Textbook_of_Conservative_and_Restorative_Dentistry.md', 19, 'Sikri, 2020'),
 # Summitt's Fundamentals of Operative Dentistry 4th ed (2013) Ch.6 Pulpal considerations, Hilton and Summitt. No printed page numbers in the file.
 'q15_sum': (B+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Hilton and Summitt, 2013'),
}
L = {
 # definition, rationale, layers
 'q15_dev': ('q15_mal', 'Caries detection dyes were developed to guide the dentist in the removal of infected dentin'),
 'q15_inf': ('q15_mal', 'infected dentin, represented by superficial necrotic zone with bacterial invasion'),
 'q15_aff': ('q15_mal', 'affected dentin, represented by an inner layer of dentin that is partially demineralized and contains minimal bacterial infection'),
 'q15_rat': ('q15_mal', 'The rationale for the use of detection dyes is to avoid over-reduction of the remaining dentin'),
 'q15_sk_porosity': ('q15_sik', 'development of microvoids leads to increase in porosity'),
 'q15_sk_req': ('q15_sik', 'Should be specific and stain only the tissues it is intended to stain'),
 # enamel dyes (Sikri)
 'q15_sk_procion': ('q15_sik', 'dye stains enamel lesions but the staining becomes irreversible'),
 'q15_sk_calcein': ('q15_sik', 'dye forms a complex with calcium and remains bound to the lesion'),
 'q15_sk_zyglo': ('q15_sik', 'Fluorescent dye (Zyglo ZL-22) has been used in vitro, which is not suitable for use in vivo'),
 'q15_sk_bb': ('q15_sik', 'has also been used to enhance the diagnostic quality of fiberoptic transillumination'),
 'q15_sk_iodine': ('q15_sik', 'iodine penetration is used for measuring enamel porosity of the incipient carious lesions'),
 'q15_sk_notclin': ('q15_sik', 'Use of dyes for diagnosing enamel lesions cannot be used clinically as yet'),
 'q15_sk_mb': ('q15_sik', 'Methylene blue is also slightly toxic, so acid red is preferred'),
 # dentine dyes, history, products
 'q15_fuch': ('q15_mal', 'the first developed caries disclosing dye was based on a solution of 0.5% basic red fuchsin in propylene glycol'),
 'q15_carc': ('q15_mal', 'Concerns were arisen regarding a potential carcinogenic effect of fuchsin'),
 'q15_acid': ('q15_mal', 'its use was replaced by acid red dye, which is a frequently used food component'),
 'q15_shim': ('q15_mal', 'One of the first reports on the use of 1% acid red staining in propylene glycol base'),
 'q15_cd': ('q15_mal', 'Caries detector Kuraray Co. 1% acid red 52 in propylene glycol base'),
 'q15_cfg': ('q15_mal', '1% FD&C green dye in propylene glycol'),
 'q15_snoop': ('q15_mal', 'Dark blue dye in 47% propylene glycol and 47% water'),
 'q15_ccb': ('q15_mal', '1% acid red or 1% brilliant blue in polypropylene glycol'),
 'q15_green': ('q15_mal', 'acid red has been replaced by green or blue dyes in some products'),
 # technique
 'q15_clean': ('q15_mal', 'carious cavity needs to be cleaned and air-dried'),
 'q15_drop': ('q15_mal', 'One drop of the dye solution is then applied to the lesion for 5 s'),
 'q15_10s': ('q15_mal', 'or 10 s (caries detector, seek/sable seek, snoop, caries marker)'),
 'q15_remove': ('q15_mal', 'removed by an excavator or a round steel bur of low speed without irrigation'),
 'q15_reapply': ('q15_mal', 'solution needs to be re-applied on cavities to identify residual infected dentin until cavity floor is no longer stainable'),
 # mode of action
 'q15_pg': ('q15_mal', 'propylene glycol penetrates only loosened collagen fibers with broken intermolecular cross-links'),
 'q15_matrix': ('q15_mal', 'dye does not stain bacteria but the organic matrix'),
 'q15_sound': ('q15_mal', 'The circumpulpal dentin and the enamel–dentin junction of sound teeth are normally stained'),
 # evidence
 'q15_poor': ('q15_mal', 'dye staining is a rather poor indicator for the presence or absence of carious dentin'),
 'q15_pesk': ('q15_mal', 'the sensitivity for the caries detector was 65.1% and specificity of 37.6%'),
 'q15_70': ('q15_mal', 'a minimal value of 70% is expected for both sensitivity and specificity'),
 'q15_over': ('q15_mal', 'Over-excavation was observed when burs were combined with Caries Detector (CD)'),
 'q15_pulp': ('q15_mal', 'increased risk of pulpal exposures in deep carious lesions'),
 'q15_seal': ('q15_mal', 'Sealing of carious dentin results in lower levels of infection than traditional dentin caries removal'),
 'q15_bond': ('q15_mal', 'the effect of dyes on bonding properties of adhesive restoration remains unclear'),
 'q15_esth': ('q15_mal', 'difficulty in removing the staining in the esthetic restorations'),
 'q15_lack': ('q15_mal', 'there is a lack of substantive scientific evidence with good quality supporting the use of caries-detecting dyes'),
 'q15_su_benefit': ('q15_sum', 'Studies have demonstrated the benefit of these dyes to aid in identification and removal of demineralized dentin'),
 'q15_su_porous': ('q15_sum', 'the dyes stain not only demineralized dentin but also anything porous'),
 'q15_su_deep': ('q15_sum', 'noncarious deep dentin will absorb the dye'),
 'q15_su_bond': ('q15_sum', 'the preponderance of evidence indicates that neither of these should be a concern'),
}
