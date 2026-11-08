# Auditor u2 locators (2026-11-08 audit): B02, B04, B05, B08, B10, B11, B12.
# Reuses F keys of loc_a1..a5 where the book is already defined; new F keys only for new books/chapters.
O = T + 'Operative_and_Dental_Materials_Textbooks/'
F = {
 # Craig's 11th ed (Craig and Powers, 2002). Ch.5 offset 10 (PDF 137 = p.127, 165 = p.155); Ch.8 offset 9 (PDF 211 = p.202, 212 = p.203)
 'u2_c11a': (O+'Restorative_Dental_Materials_Craig_Michigan_11th.md', 10, 'Craig and Powers, 2002'),
 'u2_c11b': (O+'Restorative_Dental_Materials_Craig_Michigan_11th.md', 9, 'Craig and Powers, 2002'),
 # Phillips' 12th ed Ch.11 (dentifrices). Offset 16 (PDF 265 = p.249, 266 = p.250)
 'u2_ph': (O+'Phillips_Science_of_Dental_Materials.md', 16, 'Anusavice, Shen and Rawls, 2013'),
 # Bhat et al 3rd ed Ch.7 Biocompatible aspects. Offset 33 (PDF 169 = p.136, 170 = p.137)
 'u2_bh': (O+'Science_of_Dental_Materials.md', 33, 'Bhat, Nandish and Jayaprakash, 2019'),
 # van Noort 4th ed Ch.2.1 Dental amalgams. Offset 15 (PDF 81 = p.66, 82 = p.67, 83 = p.68)
 'u2_vn': (O+'Introduction_to_Dental_Materials_4th.md', 15, 'van Noort, 2013'),
 # Lasers in Dentistry 2nd ed Ch.2 (Coluzzi). Offset 11 (PDF 37 = p.26, 38 = p.27)
 'u2_las2': (O+'Lasers_in_Dentistry_Current_Concepts.md', 11, 'Coluzzi, 2023'),
 # Lasers in Dentistry 2nd ed Ch.7 (Cronshaw and Mylona). Offset 9 (PDF 199 = p.190, 234 = p.225)
 'u2_las7': (O+'Lasers_in_Dentistry_Current_Concepts.md', 9, 'Cronshaw and Mylona, 2023'),
}
L = {
 # Summitt (a2_sum, PDF page only)
 'u2_sum_mid1800': ('a2_sum', 'By the mid-1800s, the in-office bleaching agent of choice for nonvital teeth was chloride of lime'),
 'u2_sum_1800s': ('a2_sum', 'Other agents used in the 1800s for nonvital tooth bleaching included aluminum chloride'),
 'u2_sum_5h': ('a2_sum', 'Although the agent has lost most of its potency after 5 hours'),
 # Grossman's (a2_gro, offset 25)
 'u2_gro_cp35': ('a2_gro', 'Carbamide peroxide → Urea + ammonia + carbon dioxide + 3.5% hydrogen peroxide'),
 'u2_gro_sevh': ('a2_gro', 'Carbamide peroxide is more stable than hydrogen peroxide and can be active up to several hours'),
 'u2_gro_pbtext': ('a2_gro', 'this paste decomposes into sodium metaborate, water, and oxygen'),
 'u2_gro_pbeq': ('a2_gro', 'Sodium perborate → Sodium metaborate + hydrogen peroxide + O2'),
 'u2_gro_reduc': ('a2_gro', 'Tooth (reducing agent takes up electrons)'),
 'u2_gro_oxid': ('a2_gro', 'Bleaching agent (oxidizing agent gives free electrons)'),
 # Cohen's (a2_coh, PDF page only)
 'u2_coh_co2': ('a2_coh', 'Further degradation over this step may complete disintegration of the organic matrix with the release of carbon dioxide and water'),
 'u2_coh_slow': ('a2_coh', 'At room and oral temperatures, the reaction of carbamyl peroxide takes place at a slower rate compared to hydrogen peroxide'),
 # Andreasen Ch.33 (a5_and, offset 16)
 'u2_and_1864': ('a5_and', 'The first publication on bleaching of discolored, pulpless teeth appeared in 1864'),
 'u2_and_1961': ('a5_and', 'In the walking bleach technique that was introduced in 1961'),
 'u2_and_ortho': ('a5_and', 'based on an observation made in the late 1960s by an orthodontist'),
 'u2_and_chromo': ('a5_and', 'attack the long chained, dark colored chromophore molecules and split them into smaller, less colored and more diffusible molecules'),
 'u2_and_nh3': ('a5_and', 'It is, however, unclear how much ammonia will be formed during tooth bleaching using carbamide peroxide'),
 'u2_and_basic': ('a5_and', 'in a basic solution, lower activation energy is required for the formation of free radicals from hydrogen peroxide'),
 # Endodontology Ch.44 (a5_edo, offset 17)
 'u2_edo_rad': ('a5_edo', 'free hydrogen peroxide can release various radicals'),
 # Alani and Patel Ch.3 (a5_ala, offset 20)
 'u2_ala_4h': ('a5_ala', 'A solution of 10% carbamide peroxide results in approximately 3% hydrogen peroxide over a period of 4 h'),
 'u2_ala_acidic': ('a5_ala', 'Hydrogen peroxide is a colourless liquid that is soluble in water to produce an acidic solution'),
 'u2_ala_reflect': ('a5_ala', 'are less able to reflect light than the previous large chromophore molecules'),
 'u2_ala_hydroxyl': ('a5_ala', 'These large chains are then broken down into hydroxyl-containing'),
 # Bonsor and Pearson Ch.18 (a4_bon, PDF page only)
 'u2_bon_reflect': ('a4_bon', 'The smaller molecules so produced reflect less light from or they are lost from the tooth tissue'),
 'u2_bon_borate': ('a4_bon', 'Sodium perborate reacts with water to form sodium borate and hydrogen peroxide'),
 'u2_bon_third': ('a4_bon', 'The concentration of carbamide peroxide in any commercial product is three times the concentration of the hydrogen peroxide liberated'),
 'u2_bon_inactive': ('a4_bon', 'breakdown products are rendered inactive'),
 # Powers and Wataha (a2_pw, offset 12)
 'u2_pw_hour': ('a2_pw', 'The gel is replenished each hour'),
 'u2_pw_05': ('a2_pw', 'Peroxide whitening agents are readily diffused through 0.5 mm of dentin in concentration to produce cytotoxicity'),
 # Craig's 14th (a4_cr, offset 11) -- reused key a4_cr_enamel for "a few minutes"
 # Craig's 11th
 'u2_c11_sec': ('u2_c11a', 'Peroxides in bleaching agents have been shown to permeate intact enamel in just a few seconds'),
 'u2_c11_cp': ('u2_c11a', 'These agents usually contain some form of peroxide (generally carbamide peroxide) in a gel'),
 'u2_c11_tp': ('u2_c11b', 'Bleaching toothpastes based on low-level peroxide formulations are also available to whiten teeth for esthetic purposes'),
 'u2_c11_daily': ('u2_c11b', 'They are effective in whitening teeth when used daily'),
 # Phillips'
 'u2_ph_tp': ('u2_ph', 'may contain an abrasive agent alone or both a chemical agent and an abrasive agent'),
 'u2_ph_mech': ('u2_ph', 'act through a combined mechanism of abrasion and bleaching'),
 'u2_ph_inv': ('u2_ph', 'The therapeutic benefits of other additives such as peroxides and bicarbonates are under investigation'),
 # Bhat et al
 'u2_bh_exposed': ('u2_bh', 'These contain some peroxides, which are capable of passing through the exposed dentin and cause cytotoxicity'),
 # van Noort
 'u2_vn_hg': ('u2_vn', 'carbamide-based bleaching agents can increase the release of mercury from amalgam restorations'),
 # Sikri 2020 (a2_sik, offset 19)
 'u2_tcr_perhyd': ('a2_sik', 'The perhydroxyl radical is produced as compared to superoxide, which is more reactive than the superoxide and other radicals'),
 # Sikri Essentials 2019 (a5_sik, offset 21)
 'u2_sik19_cp': ('a5_sik', '10% carbamide peroxide is equal to 3.0% hydrogen peroxide and 22% carbamide peroxide is equal to 7.5% hydrogen peroxide'),
 # Lasers Ch.16 (a2_las, offset 5)
 'u2_las_fig': ('a2_las', 'The first phase is the reduction of carbamide peroxide into two parts of ammonia and carbon dioxide'),
 'u2_las_reduced': ('a2_las', 'Hydrogen peroxide can be further reduced (A) into an oxygen radical and water'),
 'u2_las_absorb': ('a2_las', 'which absorb less and therefore reflect more light'),
 # Lasers Ch.2 and Ch.7
 'u2_las2_532': ('u2_las2', 'Semiconductor diode, visible green Soft tissue procedures, tooth whitening Gallium Nitride 532'),
 'u2_las2_445': ('u2_las2', 'tooth whitening Indium Gallium Nitride 445'),
 'u2_las7_area': ('u2_las7', 'The surface area of these tools varies between manufacturers and typically falls into the range of 2.8'),
 'u2_las7_irr': ('u2_las7', 'average irradiance in close proximity to the surface of the target of 250–500 mW/cm2'),
 'u2_las7_six': ('u2_las7', 'identified six studies investigating the potential benefits of PBMT to post-bleaching sensitivity'),
 'u2_las7_660': ('u2_las7', 'The wavelengths employed ranged from 660 to 810 nm with a fluence in the range of 12–60 J/cm2'),
 'u2_las7_insuff': ('u2_las7', 'The weight of current available evidence is insufficient to offer guidelines on the prophylaxis of post-bleaching sensitivity'),
}
BOOK = {
 'Craig2002': "Craig RG, Powers JM, editors. Restorative Dental Materials. 11th ed. St Louis: Mosby; 2002. Ch.5 Biocompatibility of dental materials; Ch.8 Preventive materials.",
 'Anusavice2013': "Anusavice KJ, Shen C, Rawls HR, editors. Phillips' Science of Dental Materials. 12th ed. St Louis: Elsevier Saunders; 2013 (year not printed in the extracted file; verify). Ch.11 Materials and processes for cutting, grinding, finishing, and polishing (dentifrices).",
 'Bhat2019': "Bhat VS, Nandish BT, Jayaprakash K. Science of Dental Materials with Clinical Applications. 3rd ed. New Delhi: CBS Publishers & Distributors; 2019 (eBook edition date). Ch.7 Biocompatible aspects of dental materials.",
 'vanNoort2013': "van Noort R. Introduction to Dental Materials. 4th ed. Edinburgh: Mosby Elsevier; 2013. Ch.2.1 Dental amalgams.",
 'Coluzzi2023': "Coluzzi DJ. Laser and light fundamentals. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry: Current Concepts. 2nd ed. Cham: Springer Nature; 2023. Ch.2.",
 'Cronshaw2023': "Cronshaw M, Mylona V. Photobiomodulation therapy within clinical dentistry: theoretical and applied concepts. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry: Current Concepts. 2nd ed. Cham: Springer Nature; 2023. Ch.7.",
}
