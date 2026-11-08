# Auditor u1 locators (audit of B01, B03, B13, P3; 2026-11-08). Existing a1-a5 keys are reused in the answers where they exist.
O = T + 'Operative_and_Dental_Materials_Textbooks/'
F = {
 # Cohen 12th Ch.26 (Setzer); no printed page numbers
 'u1_coh': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/26_26_Bleaching_procedures.md', None, 'Setzer, 2021'),
 # Walton and Torabinejad 2002 Part 23; offset 15 (as a5_pp: PDF 422 = p.407, 423 = p.408)
 'u1_pp': (T+'Principles_and_practice_of_endodontic_2002_compressed_Chapterwise/23_Part_23_Bleaching_Discolored_Teeth_I_nternal_and_External.md', 15, 'Walton and Torabinejad, 2002'),
 # Andreasen 4th Ch.29 (Zachrisson and Toreskog); offset 16 (PDF 815 = p.799, 816 = p.800)
 'u1_and29': (T+'Textbook_and_Color_Atlas_of_Traumatic_Chapterwise/29_29_Esthetic_Considerations_in_Restoring_the_Traumatized_Dent.md', 16, 'Zachrisson and Toreskog, 2007'),
 # Andreasen 4th Ch.33 (Dahl and Pallesen); offset 16 (as a5_and)
 'u1_and': (T+'Textbook_and_Color_Atlas_of_Traumatic_Chapterwise/33_33_Bleaching_of_the_Discolored_Traumatized_Tooth.md', 16, 'Dahl and Pallesen, 2007'),
 # Goldstein 3rd Ch.12 (Kwon and Goldstein); offset 14 (as a2_gol/a3_g12)
 'u1_g12': (O+'Esthetics_in_Dentistry_Goldstein.md', 14, 'Kwon and Goldstein, 2018'),
 # Goldstein 3rd Ch.39 (Goldstein, Esfandiari and Schultz); offset 28 (PDF 1264 = p.1236, 1265 = p.1237, 1266 = p.1238)
 'u1_g39': (O+'Esthetics_in_Dentistry_Goldstein.md', 28, 'Goldstein, Esfandiari and Schultz, 2018'),
 # Alani and Patel Ch.3; offset 20 (as a5_ala: PDF 78 = p.58, 79 = p.59)
 'u1_ala': (O+'Adhesive_Techniques_in_Restorative_Dentistry_Alani_Patel.md', 20, 'Alani and Patel, 2025'),
 # Grossman 14th Ch.23; offset 25
 'u1_gro': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/23_Chapter_23_Bleaching_of_Discolored_Teeth.md', 25, 'Gopikrishna, 2021'),
 # Sikri Essentials 2nd Ch.24; offset 21
 'u1_sik': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/24_24_Bleaching_of_Discolored_Teeth.md', 21, 'Sikri, 2019'),
 # Chu, Devigus, Paravina, Mieleszko, Fundamentals of Color 2nd ed; no printed page numbers in the extract -> PDF page only
 'u1_fcs': (O+'Fundamentals_of_Color_Shade_Matching.md', None, 'Chu et al, 2010'),
 # Torres (ed) Modern Operative Dentistry: Ch.1 offset 14 (PDF 29 = p.15, 30 = p.16); Ch.16 offset 6 (PDF 660 = p.654, 661 = p.655); Ch.17 offset 6 (PDF 675 = p.669)
 'u1_mod1': (O+'Modern_Operative_Dentistry.md', 14, 'Torres et al, 2020'),
 'u1_mod16': (O+'Modern_Operative_Dentistry.md', 6, 'Borges, Torres and Schlueter, 2020'),
 'u1_mod17': (O+'Modern_Operative_Dentistry.md', 6, 'Huhtala et al, 2020'),
 # Craig's 14th Ch.6 (PDF 116 = p.105; offset 11)
 'u1_cr': (O+'Craigs_Restorative_Dental_Materials.md', 11, 'Sakaguchi, Ferracane and Powers, 2019'),
 # Bartlett, Advanced Operative Dentistry Ch.5; offset 6
 'u1_bar': (O+'Advanced_Operative_Dentistry.md', 6, 'Bartlett, 2011'),
}
L = {
 # --- Cohen
 'u1_coh_rct': ('u1_coh', 'demonstrated no significant changes in color and lightness comparing the short-term bleaching results with the 1-year follow-up'),
 'u1_coh_rctdesign': ('u1_coh', 'A randomized clinical trial evaluating CIELab parameters of teeth bleached using the walking bleach or an inside-outside technique'),
 'u1_coh_pb1y': ('u1_coh', 'because it did not cause cervical resorption, even 1 year after bleaching'),
 'u1_coh_5s15s': ('u1_coh', 'the paste should be placed on the tooth for about 5 seconds, followed by the rubber cup activation for 15 seconds'),
 'u1_coh_stop': ('u1_coh', 'the procedure should be terminated to avoid permanent enamel damage'),
 # --- Walton and Torabinejad 2002
 'u1_pp_natural': ('u1_pp', 'The first group, natural (acquired) discolorations, may be on the surface or incorporated into tooth structure.'),
 'u1_pp_iatro': ('u1_pp', 'The second group, iatrogenic (inflicted) discolorations, which result from dental procedures, are usually incorporated into tooth structure and are preventable.'),
 'u1_pp_erythro': ('u1_pp', 'This discoloration is not correctable by bleaching.'),
 'u1_pp_restor': ('u1_pp', 'These conditions are also not amenable to bleaching and should be corrected restoratively.'),
 'u1_pp_tetpred': ('u1_pp', 'The second, root canal treatment followed by internal bleaching, is a more predictable procedure'),
 'u1_pp_calcfair': ('u1_pp', 'Such teeth are bleached with fair esthetic prognosis.'),
 'u1_pp_overbleach': ('u1_pp', 'the overbleached tooth may not discolor again'),
 'u1_pp_caoh': ('u1_pp', 'This procedure is ineffective and unnecessary.'),
 'u1_pp_notbleach': ('u1_pp', 'This is not a true bleaching (oxidizing) technique but decalcification and removal of a thin layer of stained enamel.'),
 'u1_pp_mix': ('u1_pp', 'A 36% hydrochloric acid solution is mixed with an equal volume of distilled water to make an 18% hydrochloric acid solution.'),
 'u1_pp_5s': ('u1_pp', 'the paste is worked into the enamel surface with a swirling motion for 5 seconds'),
 'u1_pp_rinse10': ('u1_pp', 'The enamel surface is then rinsed for 10 seconds with water.'),
 'u1_pp_bicarb': ('u1_pp', 'The surface is neutralized with sodium bicarbonate and water.'),
 'u1_pp_single': ('u1_pp', 'Usually the desired shade is obtained in a single appointment.'),
 'u1_pp_perm': ('u1_pp', 'The acid-pumice abrasion technique is relatively permanent if initial lightening is achieved.'),
 'u1_pp_mcinnes': ('u1_pp', 'The acid-pumice method does not actually bleach the stain as in the McInnes technique'),
 'u1_pp_boskman': ('u1_pp', 'Jordan R, Boskman L: Conservative vital bleaching treatment of discolored dentition'),
 'u1_edo_devital': ('a5_edo', 'should only be undertaken after proper consideration of the possible risks'),
 # --- Andreasen Ch.29 (Zachrisson and Toreskog)
 'u1_and29_10hp': ('u1_and29', 'Nocturnal use of 10% hydrogen peroxide gel in a tray is a convenient way of bleaching teeth'),
 'u1_and29_ref14': ('u1_and29', 'Clinical study of tooth shade lightening from dentist-supervised patient-applied treatment with two 10% carbamide peroxide gels'),
 'u1_and29_yellow': ('u1_and29', 'It is generally agreed in esthetic dentistry that yellow discolorations are the easiest to improve.'),
 # --- Andreasen Ch.33 (Dahl and Pallesen)
 'u1_and_choice': ('u1_and', 'must be regarded as the treatment of choice, alone or preceding a prosthetic restoration'),
 'u1_and_2025': ('u1_and', '20–25% after 3–5 years'),
 'u1_and_obliter': ('u1_and', 'a successful and long-lasting effect of bleaching cannot be expected'),
 'u1_and_initial': ('u1_and', 'bleaching should be the initial treatment in both young and old patients'),
 # --- Kwon and Goldstein Ch.12
 'u1_g12_haem': ('u1_g12', 'be quite effective for the discoloration caused by infusion of the dentin during development'),
 'u1_g12_erythro': ('u1_g12', 'The characteristically brownish teeth caused by destruction of an excessive number of erythrocytes'),
 'u1_g12_metalsalt': ('u1_g12', 'no amount of bleaching with available products will significantly improve the esthetic quality of these teeth'),
 'u1_g12_35hp': ('u1_g12', 'enough 35% hydrogen peroxide to form a thick white paste'),
 'u1_g12_heat': ('u1_g12', 'the ability to use higher temperatures without causing the patient discomfort'),
 'u1_g12_gp23': ('u1_g12', 'the root canal filling material should be removed to a depth of 2–3 mm apical to the cervical line'),
 'u1_g12_2wk': ('u1_g12', 'Placement of the final restoration is delayed for 2 weeks to allow the oxygen generated during bleaching to dissipate'),
 'u1_g12_heith': ('u1_g12', 'and 3.9% by intracoronal bleaching'),
 'u1_g12_26wk': ('u1_g12', 'Generally, this occurs 2–6 weeks after the last bleaching'),
 'u1_g12_older': ('u1_g12', 'Older patients are excellent candidates for bleaching'),
 'u1_g12_trim05': ('u1_g12', 'The tray is trimmed with sharp scissors approxi- mately 0.5 mm away from the gingival margin'.replace('approxi- mately', 'approximately')),
 'u1_g12_fourth': ('u1_g12', 'while not one of the original categories proposed by Jordan and Boksman'),
 # --- Goldstein Ch.39
 'u1_g39_three': ('u1_g39', 'Intrinsic, extrinsic, and internalized tooth discoloration boast multifactorial etiologies'),
 'u1_g39_ferric': ('u1_g39', 'ferric ions have a very high affinity for hard tooth surfaces'),
 # --- Alani and Patel Ch.3
 'u1_ala_12': ('u1_ala', 'tetracycline is not recommended for expectant mothers, those nursing neonates and children up to the age of 12 years'),
 'u1_ala_fl': ('u1_ala', 'with the critical time between 20 and 30 months'),
 'u1_ala_fl8': ('u1_ala', 'Risk diminishes completely by the age of 8 years.'),
 'u1_ala_mta3': ('u1_ala', 'the use of MTA should be confined to the apical 3 mm'),
 'u1_ala_older': ('u1_ala', 'will be inherently more challenging to lighten'),
 'u1_ala_yellow': ('u1_ala', 'a yellow appearance or stain is likely to be easiest to manage, and black is the most difficult'),
 'u1_ala_gp1': ('u1_ala', 'approximately 1+ mm below the visible gingival margin or CEJ'),
 'u1_ala_tray1': ('u1_ala', 'the tray should extend just over the visible gingival margin by approximately 1 mm'),
 'u1_ala_eva': ('u1_ala', 'the general minimum thickness should be 1 mm'),
 'u1_ala_reservoir': ('u1_ala', 'there is no definitive evidence to show that the presence of bleach reservoirs (spacers) is more or less beneficial'),
 'u1_ala_cycles': ('u1_ala', 'The gel is replenished in 3–4 cycles of 15 min.'),
 'u1_ala_cervical': ('u1_ala', 'The cervical area of a tooth is notoriously the most difficult area to bleach'),
 'u1_ala_canine': ('u1_ala', 'canine teeth are likely to require more bleaching than their neighbouring lateral incisor teeth'),
 'u1_ala_icon': ('u1_ala', 'Acid etching of the white spot lesion followed by resin infiltration will stop lesion progression'),
 'u1_ala_6hp': ('u1_ala', 'The most commonly utilised bleaching agent gel substances are 10% carbamide peroxide and 6% hydrogen peroxide.'),
 'u1_ala_4h': ('u1_ala', 'A solution of 10% carbamide peroxide results in approximately 3% hydrogen peroxide over a period of 4 h.'),
 'u1_ala_goodoh': ('u1_ala', 'black/brown staining in those with good oral hygiene'),
 'u1_ala_dyes': ('u1_ala', 'These are known as pigments.'),
 # --- Grossman Ch.23
 'u1_gro_heat': ('u1_gro', 'The temperature should be maintained between 125 and 140°F (52–60°C).'),
 'u1_gro_30min': ('u1_gro', 'The treatment time should not exceed 30 minutes even if the result is not satisfactory.'),
 'u1_gro_naf35': ('u1_gro', 'Apply neutral sodium fluoride gel for 3–5 minutes.'),
 'u1_gro_reserv': ('u1_gro', 'The reservoir should terminate 1 mm short of the free gingival margin.'),
 'u1_gro_viscous': ('u1_gro', 'For highly viscous material, the margins can be scalloped, terminating just incisal to the free gingival margin.'),
 'u1_gro_nonvisc': ('u1_gro', 'If the bleaching agent is nonviscous, then the margins have to be nonscalloped and extending on to the gingival tissues.'),
 'u1_gro_brown': ('u1_gro', 'Destaining of the yellow color is most successful, whereas brownish teeth are least successfully bleached.'),
 'u1_gro_kane': ('u1_gro', 'McCloskey reported that Kane successfully removed fluorosis stains by applying acid and heat in 1916'),
 'u1_gro_prema': ('u1_gro', 'which is an abrasive paste containing HCl, silicon gel, silicon carbide, and silica gel'),
 'u1_gro_naoh': ('u1_gro', 'Comprises 20% sodium hydroxide instead of 36% hydrochloric acid.'),
 'u1_gro_naohmech': ('u1_gro', 'it dissolves calcium of the enamel at a slower rate'),
 'u1_gro_23times': ('u1_gro', 'This procedure may have to be repeated two or three times before the desired shade is obtained'),
 'u1_gro_ceramic': ('u1_gro', 'Bleaching agents are known to cause etching and weakening of ceramic prosthesis.'),
 'u1_gro_vitalhead': ('u1_gro', 'The technique of vital bleaching is as follows:'),
 # --- Sikri Essentials Ch.24
 'u1_sik_inoffice': ('u1_sik', 'a. Thermocatalytic bleaching b. Nonthermocatalytic bleaching c. Power bleaching d. Microabrasion'),
 'u1_sik_routine': ('u1_sik', 'This is also used in cases where routine bleaching is not effective.'),
 # --- Fundamentals of Color (Chu et al)
 'u1_fcs_bguide': ('u1_fcs', 'is the only shade guide developed specifically for visual evaluation of tooth whitening'),
 'u1_fcs_group0': ('u1_fcs', 'Group 0 = 3 tabs (bleached shades, the lightest)'),
 'u1_fcs_linear': ('u1_fcs', 'Linearguide and Toothguide were both found to enable significantly better (closer) matches compared to Classical'),
 'u1_fcs_achrom': ('u1_fcs', 'leaving value as the only visual parameter'),
 'u1_fcs_5s': ('u1_fcs', 'Five-second glances with periods of rest, instead of prolonged stares, are recommended.'),
 'u1_fcs_d65': ('u1_fcs', 'with a color temperature of 5,500 K (D55) to 6,500 K (D65) and with a color-rendering index (CRI) of 90 or greater'),
 'u1_fcs_dist': ('u1_fcs', 'tooth level, 25 to 35 cm (10 to 14 inches) away'),
 'u1_fcs_dehyd': ('u1_fcs', 'Dehydrated teeth become lighter and need time to regain their normal coloration'),
 'u1_fcs_value': ('u1_fcs', 'Value is analyzed first, followed by chroma, then hue'),
 'u1_fcs_gray': ('u1_fcs', 'A neutral gray card should be observed between trials.'),
 'u1_fcs_transl': ('u1_fcs', 'allowing a tooth to become whiter yet remain highly translucent'),
 'u1_fcs_lux': ('u1_fcs', 'An illuminance of 1,000 lux is considered optimal for visual color assessments.'),
 # --- Modern Operative Dentistry
 'u1_mod1_washout': ('u1_mod1', 'A washout phase of minimum 2 weeks should be observed after the bleaching'),
 'u1_mod16_hcl': ('u1_mod16', 'the sole one able to sufficiently remove the surface layer is 15% hydrochloric acid, applied for 2 min'),
 'u1_mod16_3min': ('u1_mod16', 'the infiltrant was applied for 3 min'),
 'u1_mod16_noncav': ('u1_mod16', 'The infiltration technique is indicated only to those lesions without cavitation'),
 'u1_mod17_first': ('u1_mod17', 'dental bleaching should always be the first treatment choice in those cases'),
 # --- Craig's 14th Ch.6
 'u1_cr_minutes': ('u1_cr', 'peroxides can rapidly (within minutes) traverse the dentin in sufficient concentrations to be cytotoxic'),
 'u1_cr_concern': ('u1_cr', 'a legitimate concern exists about the long-term use of these products on vital teeth'),
 # --- Bartlett: the rest of the Tong et al figure (the plus-minus sign is a control character in the extract)
 'u1_bar_130': ('u1_bar', '130 mm of enamel thickness is lost (Tong et al., 1993)'),
}
BOOK = {
 'Walton2002': "Walton RE, Torabinejad M, editors. Principles and Practice of Endodontics. 3rd ed. Philadelphia: WB Saunders; 2002. Ch.23 Bleaching discolored teeth: internal and external (chapter author not shown in the extracted file, so the editors are cited).",
 'Dahl2007': "Dahl JE, Pallesen U. Bleaching of the discolored traumatized tooth. In: Andreasen JO, Andreasen FM, Andersson L, editors. Textbook and Color Atlas of Traumatic Injuries to the Teeth. 4th ed. Oxford: Blackwell Munksgaard; 2007. Ch.33.",
 'Zachrisson2007': "Zachrisson BU, Toreskog S. Esthetic considerations in restoring the traumatized dentition: a biologic approach. In: Andreasen JO, Andreasen FM, Andersson L, editors. Textbook and Color Atlas of Traumatic Injuries to the Teeth. 4th ed. Oxford: Blackwell Munksgaard; 2007. Ch.29.",
 'Kwon2018': "Kwon SR, Goldstein RE. Bleaching discolored teeth. In: Goldstein RE, Chu SJ, Lee EA, Stappert CFJ, editors. Ronald E. Goldstein's Esthetics in Dentistry. 3rd ed. Hoboken: Wiley; 2018. Ch.12.",
 'GoldsteinEsfandiari2018': "Goldstein RE, Esfandiari A, Schultz AK. Esthetic failures. In: Goldstein RE, Chu SJ, Lee EA, Stappert CFJ, editors. Ronald E. Goldstein's Esthetics in Dentistry. 3rd ed. Hoboken: Wiley; 2018. Ch.39.",
 'Alani2025': "Alani A, Patel M. Adhesive Techniques in Restorative Dentistry (BDJ Clinician's Guides). Cham: Springer Nature; 2025. Ch.3 Management of discoloured teeth.",
 'Chu2010': "Chu SJ, Devigus A, Paravina RD, Mieleszko AJ. Fundamentals of Color: Shade Matching and Communication in Esthetic Dentistry. 2nd ed. Hanover Park: Quintessence; 2010. Ch.3 Elements affecting color; Ch.4 Conventional shade matching.",
 'Torres2020': "Torres CRG, Barbe AG, Noack MJ, Wicht MJ. Diagnosis and treatment planning. In: Torres CRG, editor. Modern Operative Dentistry. Cham: Springer Nature; 2020. Ch.1.",
 'Borges2020': "Borges AB, Torres CRG, Schlueter N. Preventive measures and minimally invasive restorative procedures. In: Torres CRG, editor. Modern Operative Dentistry. Cham: Springer Nature; 2020. Ch.16.",
 'Huhtala2020': "Huhtala MFRL, Pagani C, Torres CRG, Vallittu PK, Matinlinna JP. Aesthetic veneers: what are they and how to handle them? In: Torres CRG, editor. Modern Operative Dentistry. Cham: Springer Nature; 2020. Ch.17.",
 'Sakaguchi2019': "Sakaguchi RL, Ferracane JL, Powers JM, editors. Craig's Restorative Dental Materials. 14th ed. St Louis: Elsevier; 2019. Ch.6 Biocompatibility and tissue reaction to biomaterials.",
}
