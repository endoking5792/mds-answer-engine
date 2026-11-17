# Locators for Q08 "Elaborate on biological properties of endodontic materials." (proposed 10m). Keys prefixed q08_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
F_EXTRA = {
 # Cohen's Pathways of the Pulp 12e (2021) Ch.9 (Aminoshariae, Johnson, Kulild, Tay, from the chapter's first lines); electronic edition, PDF page only.
 'q08_coh': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/09_9_Obturation_of_the_cleaned_and_shaped_root_canal_system.md', None, 'Aminoshariae et al, 2021'),
 # Cohen's 12e Ch.8 (Peters, Peters, Basrani); PDF page only.
 'q08_coh8': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/08_8_Cleaning_and_shaping_of_the_root_canal_system.md', None, 'Peters et al, 2021'),
 # Sikri 2e (2019) Ch.19 Root Canal Sealers, no chapter author named. Offset 21 confirmed at PDF 336 (printed 315) and PDF 337 (printed 316).
 'q08_sik': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/19_19_Root_Canal_Sealers.md', 21, 'Sikri, 2019'),
 # Bioceramics in Endodontics (ed. Chopra, Wiley 2024) Ch.1 Bioceramics in Dentistry (Nikhil, Gupta, Jaiswal, Jha, from the Contents page). Offset 30 confirmed at PDF 52 (printed 22) and PDF 53 (printed 23).
 'q08_bio': (T+'Bioceramics_in_Endodontics_Chapterwise/01_Pages_31_60.md', 30, 'Nikhil et al, 2024'),
 # van Noort, Introduction to Dental Materials 4e (year not verified in the file; editor/author line not read from file). PDF page only.
 'q08_noo': (T+'Operative_and_Dental_Materials_Textbooks/Introduction_to_Dental_Materials_4th.md', None, 'van Noort, 2013'),
}
L = {
 'q08_sik_biocomp': ('q08_sik', 'the material should not trigger any adverse reactions, such as toxicity, allergic, inflammatory or carcinogenicity'),
 'q08_sik_zoe': ('q08_sik', 'Even zinc oxide eugenol has been observed to evoke mild cytotoxic effect.'),
 'q08_sik_bc': ('q08_sik', 'Bioceramic-based sealers have been established as biocompatible.'),
 'q08_sik_sol': ('q08_sik', 'the solubility of a root canal sealer should not exceed 3.0% by mass'),
 'q08_sik_fill': ('q08_sik', 'MTA-Fillapex and Root SP show solubility much above the accepted values (15 to 20%)'),
 'q08_sik_ca': ('q08_sik', 'Sealapex, Dycal and Apexit sealers are mildly antibacterial'),
 'q08_sik_seal': ('q08_sik', 'Various sealers have comparable sealing abilities.'),
 'q08_sik_bond': ('q08_sik', 'Bioceramic-based sealers have exhibited better bonding and adaptability as compared to other sealers.'),
 'q08_coh_zoe_res': ('q08_coh', 'Zinc oxide'+'–'+'eugenol sealers will resorb if extruded into the periradicular tissues.'),
 'q08_coh_zoe_am': ('q08_coh', 'An advantage to this sealer group is antimicrobial activity.'),
 'q08_coh_zoe_vitro': ('q08_coh', 'their clinical usefulness has been well demonstrated in retrospective and prospective human clinical studies'),
 'q08_coh_ca': ('q08_coh', 'Unfortunately, these actions have not been demonstrated.'),
 'q08_coh_bc': ('q08_coh', 'EndoSequence BC sealer was more cytotoxic than AH Plus root canal sealer.'),
 'q08_coh_bc2': ('q08_coh', 'was 5 weeks for EndoSequence BC sealer and 3 weeks for AH Plus sealer'),
 'q08_coh_gp': ('q08_coh', 'Major advantages of GP are its plasticity, ease of manipulation, minimal toxicity, radiopacity, and ease of removal with heat or solvents.'),
 'q08_coh_gp_dis': ('q08_coh', 'Disadvantages include its lack of adhesion to dentin and, when heated, shrinkage upon cooling.'),
 'q08_coh_gp_am': ('q08_coh', 'Attempts have been made to make GP more antimicrobial, but the clinical effectiveness of adding these materials has not been demonstrated.'),
 'q08_coh_mta': ('q08_coh', 'MTA is biocompatible and capable of inducing hard tissue formation.'),
 'q08_coh_caoh': ('q08_coh', 'it is less effective against Enterococcus faecalis and Candida albicans'),
 'q08_coh_edta': ('q08_coh', 'the irrigant appears to be biocompatible when used clinically'),
 'q08_coh8_naocl': ('q08_coh8', 'NaOCl is cytotoxic and a potent dissolver of organic matter.'),
 'q08_coh8_chx': ('q08_coh8', 'CHX has a low level of tissue toxicity, both locally and systemically'),
 'q08_coh8_form': ('q08_coh8', 'Formaldehyde, used as formocresol, is highly toxic, mutagenic, and carcinogenic'),
 'q08_bio_less': ('q08_bio', 'bioceramic materials in general are less cytotoxic and more biocompatible'),
 'q08_bio_hag': ('q08_bio', 'MTA was cytotoxic to both macrophages and fibroblasts'),
 'q08_bio_subs': ('q08_bio', 'The reactions, however, subsided with time'),
 'q08_bio_pulp': ('q08_bio', 'MTA used for pulp capping or partial pulpotomy stimulates reparative dentin formation.'),
 'q08_bio_apat': ('q08_bio', 'precipitating a biological apatite on the surface of the ceramics'),
 'q08_bio_am': ('q08_bio', 'MTA has antibacterial effect especially against E. faecalis and Streptococcus sanguis'),
 'q08_bio_noam': ('q08_bio', 'MTA had no antimicrobial action against any of the anaerobes'),
 'q08_noo_seal': ('q08_noo', 'be bacteriocidal, or at least bacteriostatic'),
 'q08_noo_imp': ('q08_noo', 'the root canal sealer cement is unable to provide an impervious seal'),
 'q08_noo_bulk': ('q08_noo', 'When used in bulk, the cements either are too soluble or shrink excessively on setting.'),
}
