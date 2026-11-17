# Locators for Q03 "Endodontic implants." (10m). Keys prefixed q03_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
F_EXTRA = {
 # Sikri 2e (2019 eBook edition) Ch.33. Offset 21 confirmed at PDF 606 (printed 585) and PDF 607 (printed 586). No separate chapter author named.
 'q03_sik': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/33_33_Endodontic_Implants.md', 21, 'Sikri, 2019'),
 # Weine 6e (2004) Ch.11 section Endodontic stabilizers; printed page numbers not visible, PDF page only.
 'q03_wei': (T+'Weines_Endodontics_Full_Chapterwise/11_CHAPTER_11_Endodontic_Periodontal_Problems.md', None, 'Weine, 2004'),
 # Walton and Torabinejad 3e (2002) Part 27 Endodontic Adjuncts; no chapter author named. Offset 21 confirmed at PDF 507 (printed 486) and PDF 518 (printed 497).
 'q03_wal': (T+'Principles_and_practice_of_endodontic_2002_compressed_Chapterwise/27_Part_27_Endodontic_Adjuncts.md', 21, 'Walton and Torabinejad, 2002'),
 # Barnes 1984 Surgical Endodontics: A Colour Manual, Ch.12 (author from copyright line; verify against the printed book). PDF page only.
 'q03_bar': (T+'Surgical_Endodontics_A_Colour_Manual_Chapterwise/10_Chapter_12_Operative_Technique.md', None, 'Barnes, 1984'),
 # Phillips' Science of Dental Materials 12th (Anusavice, Shen, Rawls, eds); implant chapter, offset not confirmed: PDF page only. Year taken as 2013 (verify).
 'q03_phi': (T+'Operative_and_Dental_Materials_Textbooks/Phillips_Science_of_Dental_Materials.md', None, 'Anusavice et al, 2013'),
 # AAE Glossary of Endodontic Terms, 8th ed (2012), PDF page only.
 'q03_glo': (T+'Glossary_of_Endodontic_Terms_Chapterwise/00_Pages_1_30.md', None, 'American Association of Endodontists, 2012'),
}
L = {
 'q03_sik_def': ('q03_sik', 'An endodontic implant is a metallic extension of the root'),
 'q03_sik_syn': ('q03_sik', 'also known as endodontic stabilizers, diodontic implants and endosseous endodontic implants'),
 'q03_sik_noncomm': ('q03_sik', 'do not communicate with oral environment'),
 'q03_sik_ind1': ('q03_sik', 'Periodontally involved teeth requiring stabilization'),
 'q03_sik_ind2': ('q03_sik', 'Transverse root fracture indicating removal of apical fragment'),
 'q03_sik_ind3': ('q03_sik', 'A pulpless tooth with an unusually short root'),
 'q03_sik_con1': ('q03_sik', 'Periapical rarefaction/bone infection'),
 'q03_sik_con2': ('q03_sik', 'minimum 6.0 mm bone required for implants'),
 'q03_sik_vit': ('q03_sik', 'vitallium (alloy of 65% cobalt, 30% chromium and 5% molybdenum)'),
 'q03_sik_vit2': ('q03_sik', 'discontinuation of vitallium as endodontic implant material'),
 'q03_sik_ti': ('q03_sik', 'Titanium and aluminium oxide, which is a single crystal sapphire'),
 'q03_sik_des': ('q03_sik', 'smooth-taper and threaded-taper'),
 'q03_sik_thr': ('q03_sik', 'Threaded implants displayed higher retention'),
 'q03_sik_por': ('q03_sik', 'provides strong fixation by facilitating bony ingrowths'),
 'q03_sik_60': ('q03_sik', 'The root canal must be enlarged to at least the size of a No. 60 instrument.'),
 'q03_sik_cem': ('q03_sik', 'Glass-ionomer cement or AH 26 cement is preferred'),
 'q03_sik_lim': ('q03_sik', 'Poor apical seal resulting in periapical rarefaction around the root apex.'),
 'q03_sik_sinus': ('q03_sik', 'Limitation in the available length of the osseous portion of implants by local anatomic factors'),
 'q03_sik_splint': ('q03_sik', 'In case the tooth is mobile (grade II mobility), the same should be splinted prior to root canal treatment.'),
 'q03_wei_alloy': ('q03_wei', 'cobalt pin as the implant material'),
 'q03_wei_ext': ('q03_wei', 'generally 6 to 10 mm'),
 'q03_wei_80': ('q03_wei', 'must be a minimum of size 80'),
 'q03_wei_short': ('q03_wei', 'it should bind tightly at 0.5 to 1 mm short of the working length'),
 'q03_wei_57': ('q03_wei', 'a 5- to 7-mm segment of the pin remains within the confines of the canal'),
 'q03_wei_seal': ('q03_wei', 'Lack of apical seal of the implants has been shown to be the most frequent cause of failure.'),
 'q03_wei_three': ('q03_wei', 'a three-sitting procedure should be planned'),
 'q03_wei_one': ('q03_wei', 'a one-sitting technique usually works out satisfactorily'),
 'q03_wei_fail': ('q03_wei', 'only one still remains functional'),
 'q03_wei_nil': ('q03_wei', 'its use now is virtually nil'),
 'q03_wal_def': ('q03_wal', 'The purpose is to increase the root-crown ratio, thus stabilizing the tooth.'),
 'q03_wal_prog': ('q03_wal', 'The poor long-term prognosis for endodontic implants has discouraged their use.'),
 'q03_wal_dis': ('q03_wal', 'the difficulty of achieving anatomic adaptability'),
 'q03_wal_late': ('q03_wal', 'periodontal lesions, increasing mobility, or periradicular pathosis'),
 'q03_bar_lute': ('q03_bar', 'such implants often fail because the cement lute breaks down'),
 'q03_phi_cer': ('q03_phi', 'alloys or ceramics made of alumina or zirconia'),
 'q03_glo_def': ('q03_glo', 'A rod placed in the canal of the root of a tooth and extending into osseous tissues to stabilize the tooth in the dental arch.'),
}
