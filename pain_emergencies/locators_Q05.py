# Locators for Q05 flare-ups (20m), Q06 flare-up in a twelve-year-old maxillary anterior tooth (20m), Q10 hot tooth (10m), P3 acute apical abscess (10m, PREDICTED).
# Keys prefixed q05_, q06_, q10_, p3_. Source keys are prefixed the same way (each question uses its own prefixed copy of the shared source table _S).
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
_S = {
 # Cohen's 12e Ch.19 (Teixeira, Cheung); electronic edition, PDF page only.
 'coh19': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/19_19_Management_of_endodontic_emergencies.md', None, 'Teixeira and Cheung, 2021'),
 # Cohen's 12e Ch.6 (Nusstein, Drum, Khan); PDF page only.
 'coh6': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/06_6_Pain_control.md', None, 'Nusstein, Drum and Khan, 2021'),
 # Cohen's 12e Ch.12 (Diogenes, Simon, Law); PDF page only.
 'coh12': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/12_12_Regenerative_endodontics.md', None, 'Diogenes, Simon and Law, 2021'),
 # Torabinejad 6e Ch.9 (Walton, Ruparel). Offset 7 confirmed at PDF 177 (printed 170) and PDF 178 (printed 171).
 'tor9': (T+'Endodontics_Principles_and_Practice_Chapterwise/09_9_Endodontic_Emergencies_and_Therapeutics.md', 7, 'Walton and Ruparel, 2021'),
 # Torabinejad 6e Ch.8 (Reader, Nusstein, Drum). Offset 7 confirmed at PDF 144 (printed 137) and PDF 145 (printed 138 expected; first page 137).
 'tor8': (T+'Endodontics_Principles_and_Practice_Chapterwise/08_8_Local_Anesthesia.md', 7, 'Reader, Nusstein and Drum, 2021'),
 # Torabinejad 6e Ch.10 (Diogenes, Botero, Kang). Offset 7 confirmed at PDF 195 (printed 188) and PDF 196 (printed 189).
 'tor10': (T+'Endodontics_Principles_and_Practice_Chapterwise/10_10_Management_of_the_Vital_Pulp_and_of_Immature_Teeth.md', 7, 'Diogenes, Botero and Kang, 2021'),
 # Torabinejad 6e Ch.11 (Paranjpe, Noblett). Offset 7 (PDF 203 printed 196).
 'tor11': (T+'Endodontics_Principles_and_Practice_Chapterwise/11_11_Management_of_Traumatic_Dental_Injuries.md', 7, 'Paranjpe and Noblett, 2021'),
 # Grossman 14e Ch.7; no chapter author named, editor cited. Offset 25 confirmed at PDF 158 (printed 133) and PDF 159 (printed 134).
 'gr7': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/07_Chapter_7_Endodontic_Emergencies.md', 25, 'Gopikrishna, 2021'),
 # Grossman 14e Ch.5 (Diseases of the periradicular tissues); editor cited. Offset 25 (PDF 100 printed 75).
 'gr5': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/05_Chapter_5_Diseases_of_the_Periradicular_Tissues.md', 25, 'Gopikrishna, 2021'),
 # Sikri 2e Ch.3. Offset 21 confirmed at PDF 46 (printed 25) and PDF 45 (printed 24).
 'sik3': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/03_3_Pathophysiology_of_Pain.md', 21, 'Sikri, 2019'),
 # Sikri 2e Ch.23. Offset 21 confirmed at PDF 433 (printed 412) and PDF 440 (printed 419).
 'sik23': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/23_23_Endodontic_Emergencies.md', 21, 'Sikri, 2019'),
 # Ingle's 7e Ch.30 (Baumgartner, Rosenberg, from the Contents page). OCR letter-substituted: clean phrases only. Printed = PDF + 118 (PDF 855 printed 973; PDF 856 printed 974), offset -118.
 'ing30': (T+'Ingles_Endodontics_7th_Chapterwise/30_Chapter_30_Treatment_of_Endodontic_Abscesses_Cellulitis_Cyst.md', -118, 'Baumgartner and Rosenberg, 2019'),
 # Treatment of Endodontic Infections 2e Ch.18 (Rôças, Siqueira); PDF page only.
 'tei18': (T+'Treatment_of_Endodontic_Infections_Chapterwise/18_Chapter_18_Endodontic_emergencies_of_infectious_origin.md', None, 'Rôças and Siqueira, 2022'),
 # Weine 6e Ch.3; printed page numbers not visible, PDF page only.
 'wei3': (T+'Weines_Endodontics_Full_Chapterwise/03_CHAPTER_3_Endodontic_Emergency_Treatment.md', None, 'Weine, 2004'),
 # Harty's 7e Ch.14 (Hülsmann, Chong). Offset 16 confirmed at PDF 303 (printed 287) and PDF 307 (printed 291).
 'har14': (T+'Harty_s_Endodontics_in_Clinical_Practice_7th_ed_Chapterwise/14_14_Problems_in_Endodontic_Treatment.md', 16, 'Hülsmann and Chong, 2017'),
 # Andreasen 4e Ch.22 (Cvek). Offset 16 confirmed at PDF 614 (printed 598) and PDF 616 (printed 600).
 'and22': (T+'Textbook_and_Color_Atlas_of_Traumatic_Chapterwise/22_22_Endodontic_Management_and_the_Use_of_Calcium_Hydroxide_in.md', 16, 'Cvek, 2007'),
 # Andreasen 4e Ch.9 (no chapter author named in the file; editors cited). PDF page only.
 'and9': (T+'Textbook_and_Color_Atlas_of_Traumatic_Chapterwise/09_9_Examination_and_Diagnosis_of_Dental_Injuries.md', None, 'Andreasen, Andreasen and Andersson, 2007'),
}
_USE = {
 'q05_': ['coh19','gr7','tei18','sik3','sik23','tor9','ing30'],
 'q06_': ['coh19','coh12','gr7','tei18','sik23','tor9','tor10','tor11','ing30','and22','and9'],
 'q10_': ['coh19','coh6','gr7','sik3','sik23','tor8','tor9','har14'],
 'p3_': ['coh19','gr5','gr7','tei18','sik23','tor9','ing30'],
}
F_EXTRA = {p+k: _S[k] for p, ks in _USE.items() for k in ks}
BOOK_EXTRA = {
 'Teixeira2021': "Teixeira FB, Cheung GSP. Management of endodontic emergencies. In: Berman LH, Hargreaves KM, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.19.",
 'Nusstein2021': "Nusstein JM, Drum M, Khan AA. Pain control. In: Berman LH, Hargreaves KM, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.6.",
 'Diogenes2021cohen': "Diogenes A, Simon S, Law AS. Regenerative endodontics. In: Berman LH, Hargreaves KM, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.12.",
 'Walton2021': "Walton R, Ruparel NB. Endodontic emergencies and therapeutics. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.9.",
 'Reader2021': "Reader A, Nusstein JM, Drum M. Local anesthesia. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.8.",
 'Diogenes2021tor': "Diogenes A, Botero T, Kang M. Management of the vital pulp and of immature teeth. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.10.",
 'Paranjpe2021': "Paranjpe A, Noblett C. Management of traumatic dental injuries. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.11.",
 'Gopikrishna2021': "Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. New Delhi: Wolters Kluwer (India); 2021. Ch.5 Diseases of the periradicular tissues and Ch.7 Endodontic emergencies (no individual chapter author is named in the files, so the editor is cited).",
 'Sikri2019': "Sikri VK. Essentials of Endodontics. 2nd ed. New Delhi: CBS Publishers; 2019. Ch.3 Pathophysiology of pain and Ch.23 Endodontic emergencies.",
 'Baumgartner2019': "Baumgartner JC, Rosenberg PA. Treatment of endodontic abscesses/cellulitis, cysts, and flare-ups. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.30 (authors from the book's Contents page).",
 'Rocas2022': "Rôças IN, Siqueira JF Jr. Endodontic emergencies of infectious origin. In: Siqueira JF Jr, Rôças IN, editors. Treatment of Endodontic Infections. 2nd ed. Berlin: Quintessence; 2022. Ch.18.",
 'Weine2004': "Weine FS. Endodontic Therapy. 6th ed. St Louis: Mosby; 2004. Ch.3 Endodontic emergency treatment.",
 'Hulsmann2017': "Hülsmann M, Chong BS. Problems in endodontic treatment. In: Chong BS, editor. Harty's Endodontics in Clinical Practice. 7th ed. Edinburgh: Elsevier; 2017. Ch.14.",
 'Cvek2007': "Cvek M. Endodontic management and the use of calcium hydroxide in traumatized permanent teeth. In: Andreasen JO, Andreasen FM, Andersson L, editors. Textbook and Color Atlas of Traumatic Injuries to the Teeth. 4th ed. Oxford: Blackwell Munksgaard; 2007. Ch.22.",
 'Andreasen2007': "Andreasen JO, Andreasen FM, Andersson L, editors. Textbook and Color Atlas of Traumatic Injuries to the Teeth. 4th ed. Oxford: Blackwell Munksgaard; 2007. Ch.9 Examination and diagnosis of dental injuries (no chapter author named in the file).",
}
L = {}
L.update({
 # ---- Q05 definition, incidence ----
 'q05_coh_def': ('q05_coh19', 'An endodontic flare-up is defined as an acute exacerbation of a periradicular pathosis after the initiation or continuation of nonsurgical root canal'),
 'q05_gr_emerg': ('q05_gr7', 'Interappointment flare-ups form a true emergency that requires an unscheduled patient visit'),
 'q05_tei_event': ('q05_tei18', 'Flare-ups are not pathologic entities but events characterized by the development of a symptomatic apical periodontitis or acute apical abscess secondary to treatment'),
 'q05_tei_day': ('q05_tei18', 'The typical patient returns on the same day or on the day following professional intervention'),
 'q05_sik_phx': ('q05_sik23', 'The phoenix abscess is the synonym of mid-treatment flare-up'),
 'q05_tor_var': ('q05_tor9', 'The reported incidence of flare-ups in endodontics varies widely due to variations in study parameters'),
 'q05_tor_inc': ('q05_tor9', 'Properly controlled prospective studies show an incidence of approximately 3%'),
 'q05_coh_inc': ('q05_coh19', 'The incidence may be from 2% to 20% of cases'),
 'q05_coh_meta': ('q05_coh19', 'showed the flare-up frequency to be about 8.4%'),
 'q05_gr_inc': ('q05_gr7', 'The reported incidence of inter-appointment flare-ups ranges from 1.4 to 19%'),
 'q05_tei_inc': ('q05_tei18', 'The incidence of flare-ups has been shown to range from 2.5% to 16%'),
 'q05_coh_succ': ('q05_coh19', 'there is no decrease in the endodontic success for cases that had a treatment flare-up'),
 # ---- Q05 etiology ----
 'q05_ing_multi': ('q05_ing30', 'factors include mechanical, microbial, chemical, immunological, gender, and psychological components'),
 'q05_tei_main': ('q05_tei18', 'Bacterial infection of the root canal is the main cause of periradicular inflammation'),
 'q05_tei_bal': ('q05_tei18', 'the balance between bacterial aggression and host defense is disrupted in favor of the former'),
 'q05_tei_acute': ('q05_tei18', 'The host mounts an acute inflammatory response at the periradicular tissue level'),
 'q05_tei_quant': ('q05_tei18', 'The number of bacterial cells extruded (bacterial load) is the quantitative factor, while the virulence of the extruded bacteria is the qualitative factor'),
 'q05_tei_crown': ('q05_tei18', 'crown-down techniques usually extrude less debris'),
 'q05_tei_solv': ('q05_tei18', 'The solvents used during filling removal are also cytotoxic and may contribute to the exacerbation of periradicular inflammation'),
 'q05_tei_incomp': ('q05_tei18', 'incomplete chemomechanical preparation can disrupt the community balance by eliminating some inhibitory species and by leaving other previously inhibited species behind to grow and proliferate'),
 'q05_tei_vir': ('q05_tei18', 'environmental changes induced by incomplete instrumentation have the potential to induce the activation of virulence genes'),
 'q05_tei_eh': ('q05_tei18', 'This mechanism remains speculative and there is no scientific evidence supporting its validity'),
 'q05_tei_sec': ('q05_tei18', 'either during treatment, between appointments, or after the conclusion of the endodontic treatment'),
 'q05_tei_breach': ('q05_tei18', 'a breach in the aseptic chain during treatment'),
 'q05_coh_chem': ('q05_coh19', 'chemical irritants (such as irrigants, intracanal medicaments, and sealers)'),
 'q05_sik_naocl': ('q05_sik23', 'may cause immediate pain and in a few hours, swelling, ecchymosis'),
 'q05_gr_flood': ('q05_gr7', 'There is a sudden flooding of the canal with blood and tissue fluids'),
 'q05_coh_mech': ('q05_coh19', 'preparation beyond the apical terminus, over-instrumentation, pushing dentinal and pulpal debris into the periapical area'),
 'q05_coh_mech2': ('q05_coh19', 'incomplete removal of pulp tissue, overextension of root canal filling material'),
 'q05_coh_mech3': ('q05_coh19', 'hyper occlusion, root fractures, and microbiologic factors'),
 'q05_sik_over': ('q05_sik23', 'It also promotes the enlargement of apical foramen which may permit an increased flux of exudate and blood into the root canal'),
 'q05_ing_anx': ('q05_ing30', 'include genetics, gender, and anxiety'),
 'q05_sik_phobia': ('q05_sik23', 'Patient with dental phobias (prone because of their low psychophysiologic tolerance)'),
 # ---- Q05 predisposing ----
 'q05_gr_pain': ('q05_gr7', 'There is a highly significant correlation between preoperative pain and/or swelling and the incidence of inter-appointment flare-ups'),
 'q05_tor_vital': ('q05_tor9', 'Flare-ups are uncommon in teeth with vital pulps'),
 'q05_tor_nec': ('q05_tor9', 'especially in those with a periapical diagnosis of symptomatic periapical periodontitis or acute apical abscess'),
 'q05_tor_rl': ('q05_tor9', 'The presence of a periapical radiolucency has also been shown to be a risk factor'),
 'q05_ing_sinus': ('q05_ing30', 'occurred in patients without periapical pathosis and when a sinus tract is present'),
 'q05_gr_retx': ('q05_gr7', 'One of the highest incidences of flare-ups occur in retreatment cases with symptomatic apical periodontitis'),
 'q05_coh_pat': ('q05_coh19', 'more prevalent among females under the age of 20 years and may occur more in maxillary lateral incisors; in mandibular first molars'),
 'q05_gr_step': ('q05_gr7', 'The step-back shaping technique has a greater tendency to extrude debris into the periradicular region than the crown-down technique'),
 'q05_gr_under': ('q05_gr7', 'Incomplete or underinstrumentation'),
 'q05_gr_irr': ('q05_gr7', 'Inadvertent extrusion of irrigant beyond the periapex, termed sodium hypochlorite accident'),
 'q05_tor_notx': ('q05_tor9', 'no definitive treatment risk factors have been identified'),
 'q05_ing_notlink': ('q05_ing30', 'Clinical studies, however, have not linked incomplete canal preparation to'),
 # ---- Q05 prevention ----
 'q05_tor_call': ('q05_tor9', 'calling the patient the day after the appointment reduces pain perception'),
 'q05_tor_prep': ('q05_tor9', 'Most important is the preparation of patients for what to expect after the appointment'),
 'q05_sik_p1': ('q05_sik23', 'Over instrumentation should be avoided'),
 'q05_sik_p2': ('q05_sik23', 'Prefer crown down instrumentation'),
 'q05_sik_p3': ('q05_sik23', 'Forced irrigation causes water-canon effect and trauma to periapical tissues'),
 'q05_sik_p4': ('q05_sik23', 'too caustic materials or even excess amount of routinely used ones may leach in periapical area'),
 'q05_sik_p5': ('q05_sik23', 'Proper coronal seal should be maintained to avoid'),
 'q05_sik_p6': ('q05_sik23', 'Root canal should not be left open for drainage'),
 'q05_tor_ibu': ('q05_tor9', '400-600 mg of ibuprofen should be given while the patient is in the chair, and then taken by the clock for the first 24 to 48 hours postoperatively'),
 'q05_tor_ibu2': ('q05_tor9', 'it is uncertain whether it will reduce the incidence of flare-ups'),
 'q05_tor_abx': ('q05_tor9', 'This practice has been demonstrated to be not useful and needlessly exposes the patient'),
 'q05_tei_abx': ('q05_tei18', 'Antibiotics are not recommended for irreversible pulpitis, acute apical periodontitis, draining sinus tracts, flare-up prevention'),
 # ---- Q05 management ----
 'q05_tor_big': ('q05_tor9', 'is the most important aspect of treatment'),
 'q05_sik_dx': ('q05_sik3', 'The current episode of pain may be initiating from another tooth, an unrelated sinus or TMJ-related condition'),
 'q05_sik_hist': ('q05_sik3', 'The patient’s past history of treatment coupled with consultation with the previous dental surgeon help reach out at diagnosis'),
 'q05_tor_class': ('q05_tor9', 'Interappointment emergencies are divided into patients with an initial diagnosis of a vital or a necrotic pulp, and patients with or without swelling'),
 'q05_tor_v1': ('q05_tor9', 'it is important to check that the temporary restoration is not in traumatic occlusion'),
 'q05_tor_v2': ('q05_tor9', 'The working length should be rechecked, and the canal(s) should be carefully cleaned with copious irrigation with'),
 'q05_tor_n1': ('q05_tor9', 'The tooth is opened, and the canal is gently recleaned and irrigated with NaOCl'),
 'q05_tor_n2': ('q05_tor9', 'the patient is allowed to rest pain-free for at least 30 minutes or until drainage stops'),
 'q05_tor_n3': ('q05_tor9', 'Ca(OH)2 paste is placed, and the access is sealed'),
 'q05_tor_s1': ('q05_tor9', 'These cases are best managed with I&D'),
 'q05_tor_s2': ('q05_tor9', 'I&D with placement of a drain (if there is continuous drainage) are completed'),
 'q05_tor_s3': ('q05_tor9', 'These situations may require hospitalization and aggressive therapy with the cooperation of an oral surgeon'),
 'q05_tei_blood': ('q05_tei18', 'The presence of blood in the apical canal, as revealed by paper points, is a sign of overinstrumentation'),
 'q05_sik_occ': ('q05_sik3', 'Occlusal reduction may alleviate the mechanical stimulation and relieve pain'),
 'q05_ing_apap': ('q05_ing30', 'acetaminophen should be considered for post-treatment pain in patients with known sensitivity to NSAIDs or aspirin'),
 'q05_tor_bup': ('q05_tor9', 'For extended anesthesia and analgesia, administration of bupivacaine hydrochloride is recommended'),
 'q05_tor_ster': ('q05_tor9', 'Flareups, however, have not been shown to be prevented by steroids'),
 'q05_coh_abx': ('q05_coh19', 'systemic signs and symptoms such as fever'),
 'q05_coh_abx2': ('q05_coh19', 'malaise, cellulitis, unexplained trismus, and progressive or persistent swelling'),
 'q05_tor_fu': ('q05_tor9', 'the patient should be contacted daily until the symptoms abate'),
 'q05_tor_ref': ('q05_tor9', 'When symptoms recur or cannot be controlled, these patients should be considered for referral'),
})
