# Locators for P1 (PREDICTED) "Calcium hydroxide apexification versus the MTA apical barrier (one-visit apexification): technique, success and drawbacks" (10m). All keys prefixed p1_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
F_EXTRA = {
 # Grossman 14e Ch.11; editor cited. Offset 25 confirmed at PDF 223 (printed 198) and PDF 231 (printed 206).
 'p1_gr': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/11_Chapter_11_Vital_Pulp_Therapy_and_Apexification.md', 25, 'Gopikrishna, 2021'),
 # Ingle's 7e Ch.28 (Shabahang, decoded). Offset -106 confirmed at PDF 805 (printed 911) and PDF 813 (printed 919).
 'p1_ing': (T+'Ingles_Endodontics_7th_Chapterwise/28_Chapter_28_Management_of_Teeth_with_Immature_Apices.md', -106, 'Shabahang, 2019'),
 # Torabinejad 6e Ch.10. Offset 7 confirmed at PDF 183 (printed 176) and PDF 194 (printed 187).
 'p1_tor': (T+'Endodontics_Principles_and_Practice_Chapterwise/10_10_Management_of_the_Vital_Pulp_and_of_Immature_Teeth.md', 7, 'Diogenes, Botero and Kang, 2021'),
 # Torabinejad 6e Ch.11 (Paranjpe and Noblett), offset 7 as established in traumatic_dental_injuries.
 'p1_tor11': (T+'Endodontics_Principles_and_Practice_Chapterwise/11_11_Management_of_Traumatic_Dental_Injuries.md', 7, 'Paranjpe and Noblett, 2021'),
 # Sikri 2e Ch.25. Offset 21 confirmed at PDF 462 (printed 441) and PDF 477 (printed 456).
 'p1_sik': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/25_25_Vital_Pulp_Therapy.md', 21, 'Sikri, 2019'),
 # Andreasen 4e Ch.22 (Cvek) and Ch.23 (Bakland). Offset 16 confirmed in both chapters (PDF 614/598, 643/627; PDF 674/658, 675/659).
 'p1_and': (T+'Textbook_and_Color_Atlas_of_Traumatic_Chapterwise/22_22_Endodontic_Management_and_the_Use_of_Calcium_Hydroxide_in.md', 16, 'Cvek, 2007'),
 'p1_bak': (T+'Textbook_and_Color_Atlas_of_Traumatic_Chapterwise/23_23_New_Endodontic_Procedures_using_Mineral_Trioxide_Aggregat.md', 16, 'Bakland, 2007'),
 # Cohen's 12e Ch.21 (Kahler); no printed page numbers.
 'p1_c21': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/21_21_The_role_of_endodontics_after_dental_traumatic_injuries.md', None, 'Kahler, 2021'),
 # Harty's 7e Ch.12 (Sigurdsson and Bourguignon), offset 16 as established.
 'p1_har': (T+'Harty_s_Endodontics_in_Clinical_Practice_7th_ed_Chapterwise/12_12_Endodontic_Aspects_of_Traumatic_Injuries.md', 16, 'Sigurdsson and Bourguignon, 2017'),
 # Bioceramics in Endodontics Ch.5 (Tonini and Garo). Offset 32 confirmed at PDF 162 (printed 130) and PDF 165 (printed 133).
 'p1_bio': (T+'Bioceramics_in_Endodontics_Chapterwise/05_Pages_151_180.md', 32, 'Tonini and Garo, 2024'),
}
BOOK_EXTRA = {
 'p1_Gopikrishna2021': "Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. Wolters Kluwer; 2021. Ch.11 Vital pulp therapy and apexification (no individual chapter author is named in the file, so the editor is cited).",
 'p1_Shabahang2019': "Shabahang S. Management of teeth with immature apices. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.28 (author line letter-substituted in the extracted file; decodes to Shahrokh Shabahang; verify against the printed book).",
 'p1_Diogenes2021': 'Diogenes A, Botero T, Kang M. Management of the vital pulp and of immature teeth. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.10.',
 'p1_Paranjpe2021': 'Paranjpe A, Noblett WC. Management of traumatic dental injuries. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.11.',
 'p1_Sikri2019': 'Sikri VK. Vital pulp therapy. In: Essentials of Endodontics. 2nd ed. New Delhi: CBS Publishers; 2019. Ch.25.',
 'p1_Cvek2007': 'Cvek M. Endodontic management and the use of calcium hydroxide in traumatized permanent teeth. In: Andreasen JO, Andreasen FM, Andersson L, editors. Textbook and Color Atlas of Traumatic Injuries to the Teeth. 4th ed. Oxford: Blackwell Munksgaard; 2007. Ch.22.',
 'p1_Bakland2007': 'Bakland LK. New endodontic procedures using mineral trioxide aggregate (MTA) for teeth with traumatic injuries. In: Andreasen JO, Andreasen FM, Andersson L, editors. Textbook and Color Atlas of Traumatic Injuries to the Teeth. 4th ed. Oxford: Blackwell Munksgaard; 2007. Ch.23.',
 'p1_Kahler2021': "Kahler B. The role of endodontics after dental traumatic injuries. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.21.",
 'p1_Sigurdsson2017': "Sigurdsson A, Bourguignon C. Endodontic aspects of traumatic injuries. In: Chong BS, editor. Harty's Endodontics in Clinical Practice. 7th ed. Edinburgh: Elsevier; 2017. Ch.12.",
 'p1_Tonini2024': 'Tonini R, Garo M. Bioceramics as an apical plug. In: Chopra V, editor. Bioceramics in Endodontics. 1st ed. John Wiley & Sons; 2024 (copyright line). Ch.5.',
}
L = {
 # history and principle
 'p1_tor11_kaiser': ('p1_tor11', 'This method was first introduced by Kaiser in 1964 and made popular by Frank in 1966'),
 'p1_tor11_wh': ('p1_tor11', 'In 2001 Witherspoon and Ham reported using MTA for single-visit apexification treatment of immature teeth with necrotic pulps'),
 'p1_tor11_frac': ('p1_tor11', 'MTA apical plug has shown to increase the fracture resistance of immature teeth'),
 'p1_tor_indirect': ('p1_tor', 'The Ca(OH)2-mediated apical closure formation is an indirect approach because it relies on the establishment of a hard tissue apical barrier'),
 'p1_tor_direct': ('p1_tor', 'MTA (or other tricalcium silicate cements) apexification is a direct approach that does not require prior hard tissue formation induction'),
 'p1_tor_same': ('p1_tor', 'known as one-step apexification'),
 'p1_bak_tittle': ('p1_bak', 'the induction of an apical hard tissue barrier was not necessary, since MTA itself used as an apical plug provides the necessary apical stop'),
 'p1_bio_onestep': ('p1_bio', 'also known as one-­step apexification'),
 # CH technique in brief
 'p1_gr_wl': ('p1_gr', 'Working length should be at least 2 mm short of the radiographic apex of the tooth'),
 'p1_c21_pack': ('p1_c21', 'Calcium hydroxide is packed against the apical soft tissue with a plugger or thick point to initiate hard-tissue formation'),
 'p1_c21_3m': ('p1_c21', 'If no washout is evident, the calcium hydroxide can be left intact for another 3 months'),
 'p1_gr_3m': ('p1_gr', 'Ca(OH)2 dressing is changed and patient'),
 'p1_c21_probe': ('p1_c21', 'When a hard-tissue barrier is indicated radiographically and can be probed with an instrument, the canal is ready for filling'),
 'p1_har_2step': ('p1_har', 'a thicker, almost dry mixture of calcium hydroxide and sterile saline is packed, using pluggers'),
 # MTA technique in brief
 'p1_gr_ch1wk': ('p1_gr', 'to raise the acidic pH of inflamed periradicular tissue before permanently sealing with MTA'),
 'p1_bio_ph': ('p1_bio', 'to alter the low pH of the inflamed periapical tissue, which could affect adhesion and hardening of the MTA'),
 'p1_har_714': ('p1_har', 'disinfecting and medicating the root canal for 7 to 14 days with a thin calcium hydroxide paste'),
 'p1_har_matrix': ('p1_har', 'calcium sulphate sponges can be placed apically beforehand to act as a matrix and to help prevent extrusion of MTA'),
 'p1_tor_colla': ('p1_tor', 'can be placed in contact with the periradicular tissues at the apex to serve as internal matrix to prevent or minimize the extrusion of MTA'),
 'p1_ing_nomatrix': ('p1_ing', 'use of a matrix material is generally not required to limit the movement of MTA into the periradicular tissues'),
 'p1_ing_plugger': ('p1_ing', 'smallest plugger should ,t loosely at a level ~ 0.5 mm from the working length'),
 'p1_ing_us': ('p1_ing', 'Ultrasonic vibration can be used on the pluggers to help advance MTA towards the apical extent of the canal'),
 'p1_gr_31': ('p1_gr', 'MTA is mixed in a 3:1 ratio using sterile distilled water to a wet'),
 'p1_gr_34': ('p1_gr', 'Material is condensed into a 3–4 mm apical plug'),
 'p1_ing_35': ('p1_ing', '3–5mm (Figure 28-22) to minimize the possibility of future apical leakage'),
 'p1_bak_4': ('p1_bak', 'The recommended size of apical MTA plug is 4mm'),
 'p1_bio_4_1': ('p1_bio', 'a 4-­mm MTA apical plug is placed 1 mm from the radiographic apex using a carrier or plugger'),
 'p1_tor_5': ('p1_tor', 'After at least 5 mm of apical plug is established'),
 'p1_c21_45': ('p1_c21', 'The material is mixed and packed into the apical 4 to 5 mm of the'),
 'p1_gr_48': ('p1_gr', 'Patient is recalled after 48 hours and the set MTA/CSC cement is verified'),
 'p1_sik_redo': ('p1_sik', 'If an ideal plug is not created in the first attempt, MTA should be rinsed out with sterile water and the procedure should be repeated'),
 'p1_ing_short': ('p1_ing', 'If the canal space is long, gutta-percha and sealer may be used to obturate the coronal segment of the canal space'),
 'p1_c21_resin': ('p1_c21', 'The cervical canal is then reinforced with composite resin to below the marginal bone level'),
 # calcium hydroxide before MTA: books differ
 'p1_ing_notneeded': ('p1_ing', 'initial use of calcium hydroxide paste was not necessary for apical root formation to occur'),
 'p1_ing_extr': ('p1_ing', 'MTA and formation of barriers beyond the limits of the root canal walls'),
 'p1_ing_better': ('p1_ing', 'intra-canal medication with calcium hydroxide for one week results in better marginal adaptation of an apical plug of MTA'),
 'p1_har_minbact': ('p1_har', 'MTA has minimal bactericidal effect on several bacterial species'),
 'p1_bio_single': ('p1_bio', 'some clinicians prefer to place the MTA apical plug in a single session'),
 # comparison: time and visits
 'p1_tor_39': ('p1_tor', 'Ca(OH)2-mediated apical plug formation requires 3- to 9-month period of treatment'),
 'p1_gr_6m4y': ('p1_gr', 'which takes a period of 6 months to 4 years to complete'),
 'p1_c21_318': ('p1_c21', 'takes anywhere from 3 to 18 months with calcium hydroxide'),
 'p1_har_624': ('p1_har', 'varies between 6 and 24 months with an average of 1 year and 7 months'),
 'p1_ing_pradhan': ('p1_ing', '(0.75 ± 0.5 months) compared to traditional calcium hydroxide therapy (7 ± 2.5 months)'),
 'p1_bio_damle': ('p1_bio', 'the mean time for the apical barrier in the MTA group was'),
 'p1_bio_damle2': ('p1_bio', '4.5 ± 1.6 months'),
 'p1_bio_damle3': ('p1_bio', 'which required 7.9 ± 2.5'),
 'p1_bio_visits': ('p1_bio', 'reduces the treatment time to one or two visits, the risk of poor patient compliance, and root fractures'),
 # barrier
 'p1_c21_swiss': ('p1_c21', 'giving the barrier a “Swiss cheese” consistency'),
 'p1_ing_porous': ('p1_ing', 'is a porous structure116 that may be permeable to microbial irritants'),
 'p1_ing_incomplete': ('p1_ing', 'barrier may be an incomplete bridge that does not cover the entire apex'),
 'p1_ing_cementum': ('p1_ing', 'a continuous band of cementum formed'),
 'p1_ing_matrix': ('p1_ing', 'plug presents a barrier that provides a matrix for immediate obturation'),
 'p1_tor11_scaff': ('p1_tor11', 'provided a scaffolding for the formation of a hard tissue barrier and subsequently a better apical seal'),
 # fracture risk
 'p1_ing_1mo': ('p1_ing', 'exposure to calcium hydroxide for periods exceeding one month may result in structural changes in dentin'),
 'p1_and_77': ('p1_and', 'Frequency of cervical fractures fell gradually from 77% in 26 teeth with the lowest degree of root development, to 2% in 362 mature teeth'),
 'p1_c21_dispute': ('p1_c21', 'fracture may be more related to the stage of root development rather than calcium hydroxide use'),
 'p1_bak_dentin': ('p1_bak', 'MTA does not appear to have a detrimental effect on dentin'),
 'p1_bak_1mo': ('p1_bak', 'the length of time during which the canal is exposed to calcium hydroxide is quite short – usually less than one month'),
 'p1_ing_cerv': ('p1_ing', 'failure in immature teeth with a history of apexi,cation has been due to fractures in the cervical region of the tooth rather than the root apex'),
 'p1_ing_weak': ('p1_ing', 'continued root development ceases once a vital pulp is removed'),
 'p1_tor_arrest': ('p1_tor', 'one of the main limitations of apexification is arrest of root development posttreatment'),
 # compliance and cost
 'p1_ing_attr': ('p1_ing', 'Long-term therapy increases the risks of patient attrition'),
 'p1_ing_reloc': ('p1_ing', 'geographic relocation renders di1culties in following patients'),
 'p1_ing_4pts': ('p1_ing', 'Four patients that were initially treated with calcium hydroxide did not return to complete treatment in a timely manner'),
 'p1_bio_cost': ('p1_bio', 'high cost, difficult handling, and the risk of post-­treatment dyschromia'),
 'p1_bio_set': ('p1_bio', 'long setting time (from 2 hours and 45 minutes to 4 hours)'),
 'p1_gr_cost': ('p1_gr', 'Relatively expensive'),
 # success and evidence
 'p1_and_7996': ('p1_and', 'has been reported to occur in 79–96% of the treated teeth'),
 'p1_bio_81': ('p1_bio', 'while higher healing rates (81–100%) were reported for MTA'),
 'p1_ing_meta': ('p1_ing', 'the authors concluded that the two protocols have similar success rates'),
 'p1_ing_10092': ('p1_ing', 'Yet 100% of the MTA cases were successful at the ,nal follow-up evaluation in comparison to a 92% success rate in the calcium hydroxide treated cases'),
 'p1_bio_meta': ('p1_bio', 'there was no difference in clinical and radiographic success rates or in the ratio of apical barrier formation between CH and MTA'),
 'p1_bio_time': ('p1_bio', 'The actual difference between the two approaches is due to the time required for apical barrier formation, which is shorter for MTA than for CH'),
 'p1_ing_meligy': ('p1_ing', 'two of the teeth treated with calcium hydroxide became re-infected'),
 'p1_ing_965': ('p1_ing', '96.5% healed in the single visit group and 89% healed in the two visit group'),
 'p1_bio_with': ('p1_bio', 'Witherspoon et al., which analyzed the healing rate in a subgroup of 119 immature teeth'),
 'p1_ing_81': ('p1_ing', 'healing was recorded in 81% of cases'),
 'p1_tor_same2': ('p1_tor', 'with same expected clinical success rate'),
 # MTA-specific drawbacks
 'p1_ing_disc': ('p1_ing', 'coronal discoloration in 22.7% of the teeth that were treated'),
 'p1_ing_45': ('p1_ing', 'MTA plugs can be limited to the apical 4–5 mm of the root canal space'),
 'p1_ing_2mmext': ('p1_ing', 'Extrusion of MTA more than 2 mm beyond the root apex may retard healing and cementum formation'),
 'p1_har_micro': ('p1_har', 'An operating microscope is needed, as magnifi'),
 'p1_ing_technique': ('p1_ing', 'the technique of placing MTA rather than the intrinsic characteristics of the MTA material itself has the greatest impact on the degree of bacterial leakage'),
 'p1_bio_bd': ('p1_bio', 'It can be used for a single visit apexification procedure, does not cause discoloration'),
 # CH-specific drawbacks
 'p1_ing_s1': ('p1_ing', 'Variability in the time required for open apices to close'),
 'p1_ing_s3': ('p1_ing', 'potential for coronal leakage and canal re-infection'),
 'p1_sik_lim': ('p1_sik', 'Risk of re-infection; periapical exudate may dissolve'),
}
