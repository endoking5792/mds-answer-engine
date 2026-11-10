# Second-reader audit U4 additions for Q05, Q06, Q10, P3. Keys u4_. Sources prefixed u4_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
F_EXTRA = {
 'u4_sik23': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/23_23_Endodontic_Emergencies.md', 21, 'Sikri, 2019'),
 'u4_tei18': (T+'Treatment_of_Endodontic_Infections_Chapterwise/18_Chapter_18_Endodontic_emergencies_of_infectious_origin.md', None, 'Rôças and Siqueira, 2022'),
 'u4_gr7': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/07_Chapter_7_Endodontic_Emergencies.md', 25, 'Gopikrishna, 2021'),
 'u4_coh19': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/19_19_Management_of_endodontic_emergencies.md', None, 'Teixeira and Cheung, 2021'),
 'u4_coh21': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/21_21_The_role_of_endodontics_after_dental_traumatic_injuries.md', None, 'Kahler, 2021'),
 'u4_coh12': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/12_12_Regenerative_endodontics.md', None, 'Diogenes, Simon and Law, 2021'),
 'u4_tor10': (T+'Endodontics_Principles_and_Practice_Chapterwise/10_10_Management_of_the_Vital_Pulp_and_of_Immature_Teeth.md', 7, 'Diogenes, Botero and Kang, 2021'),
 'u4_and22': (T+'Textbook_and_Color_Atlas_of_Traumatic_Chapterwise/22_22_Endodontic_Management_and_the_Use_of_Calcium_Hydroxide_in.md', 16, 'Cvek, 2007'),
 'u4_wei3': (T+'Weines_Endodontics_Full_Chapterwise/03_CHAPTER_3_Endodontic_Emergency_Treatment.md', None, 'Weine, 2004'),
}
L = {
 'u4_sik_o2': ('u4_sik23', 'Increase of the oxidation-reduction'),
 'u4_tei_25': ('u4_tei18', 'far exceeds 2% to 5% of cases with infected root canals'),
 'u4_gr_two': ('u4_gr7', 'cases to be completed in a two-visit protocol'),
 'u4_coh_abx1': ('u4_coh19', 'found that antibiotic administration before treatment of necrotic teeth reduced the incidence of flare-ups'),
 'u4_coh_abx2': ('u4_coh19', 'either less effective than analgesics or not to affect in reducing interappointment emergencies'),
 'u4_coh_ref': ('u4_coh19', 'refractory cases may require periapical surgery, reentry into the tooth, the establishment of drainage either through the tooth or via trephination'),
 'u4_wei_apex': ('u4_wei3', 'The presence or absence of apical closure does not have any effect on the emergency treatment'),
 'u4_coh21_naocl': ('u4_coh21', 'copious irrigation with 0.5% NaOCl'),
 'u4_coh21_range': ('u4_coh21', 'takes anywhere from 3 to 18 months with calcium hydroxide'),
 'u4_coh21_plug': ('u4_coh21', 'packed into the apical 4 to 5 mm of the'),
 'u4_coh21_fx': ('u4_coh21', 'fracture may be more related to the stage of root development rather than calcium hydroxide use'),
 'u4_tor10_range': ('u4_tor10', 'requires 3- to 9-month period of treatment'),
 'u4_cvek_naocl': ('u4_and22', 'flow of 0.5% sodium hypochlorite solution'),
 'u4_coh12_mta': ('u4_coh12', 'it is associated with severe discoloration, making it unsuitable to be used in these procedures'),
 'u4_coh12_bio': ('u4_coh12', 'Biodentine or ES putty could be used'),
 'u4_coh12_mep': ('u4_coh12', 'the tooth should not be anesthetized with a local anesthetic containing a vasoconstrictor'),
 'u4_tor10_rc': ('u4_tor10', 'followed up with a 6-month check, followed by yearly recall visits'),
 'u4_gr_ianb': ('u4_gr7', 'has the highest failure'),
 'u4_gr_clin': ('u4_gr7', '600 mg loading dose followed by 300 mg'),
}
