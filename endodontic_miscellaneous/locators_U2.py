# Second-reader audit U2 for Q02, Q04, Q05 (endodontic_miscellaneous). Keys prefixed u2_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
F_EXTRA = {
 # Ingle's 7e Ch.8 (author line letter-substituted in the file; decoded as Paul V. Abbott; verify). Printed = PDF + 24 (PDF 191 printed 215; PDF 196 printed 220; PDF 197 printed 221).
 'u2_ing8': (T+'Ingles_Endodontics_7th_Chapterwise/08_Chapter_8_Examination_and_Diagnosis_of_Pulp_Root_Canal_and_P.md', -24, 'Abbott, 2019'),
 # Seltzer and Bender's Dental Pulp 2e Ch.12 (Sasaki, Stashenko; (c) 2012 Quintessence per front matter); PDF page only.
 'u2_sel12': (T+'Seltzer_and_Bender_Dental_Pulp_Chapterwise_MD/Chapter_12_Interrelationship_of_the_Pulp_and_Apical_Periodontitis.md', None, 'Sasaki and Stashenko, 2012'),
}
L = {
 # Q02
 'u2_abb_corr': ('u2_ing8', 'had the same histologic diagnosis'),
 'u2_abb_n': ('u2_ing8', '84.4% of teeth clinically diagnosed with irreversible pulpitis'),
 'u2_abb_acute': ('u2_ing8', 'acute irreversible pulpitis are recent conditions (typically only present for a few hours or days)'),
 'u2_abb_chronic': ('u2_ing8', 'Chronic reversible and chronic irreversible pulpitis are conditions that have been present for a reasonable length of time'),
 'u2_abb_aap': ('u2_ing8', 'often have primary acute apical periodontitis'),
 'u2_sik_wt': ('q02_sik5', 'Hyperplastic B. Pulp necrosis C. Pulp calcification D.Internal resorption'),
 'u2_gro_time': ('q02_gro4', 'In posterior teeth, in which time is a factor'),
 'u2_tor9_treph': ('q02_tor9', 'are not useful and are contraindicated'),
 'u2_tor9_ibu': ('q02_tor9', '600 mg ibuprofen or 600 mg ibuprofen with'),
 'u2_tor9_apap': ('q02_tor9', 'APAP) 1000 mg is most effective in attenuating postoperative endodontic pain'),
 # Q04
 'u2_gro5_perf': ('q04_gro5', 'Perforation of the root'),
 'u2_sik_nonvital': ('q04_sik6', 'may not respond to pulp vitality tests'),
 'u2_gro5_rx': ('q04_gro5', 'Nonvital tooth: A slight widening of the apical periodontal'),
 'u2_gro5_rx2': ('q04_gro5', 'Vital tooth: No radiographic changes are seen'),
 # Q05
 'u2_sas_ac': ('u2_sel12', 'form antigen-antibody complexes, which have been found capable of stimulating periapical bone destruction'),
 'u2_sas_c5': ('u2_sel12', 'complement probably does not play a major role in pathogenesis'),
 'u2_sas_mast': ('u2_sel12', 'anaphylactic hypersensitivity reactions may also occur periapically, although their significance is unclear'),
 'u2_sas_ab': ('u2_sel12', 'antibody protects against disseminating dentoalveolar infections'),
}
