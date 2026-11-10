import os
# Locators added by second-reader audit U3 (Q03, Q04, P2). Every key starts with u3_.
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
F_EXTRA = {
 # Walton and Torabinejad 3e (2002) Part 7; no chapter author named in the file, editors cited. Offset 13 confirmed at PDF 112 (printed 99), 113 (100), 114 (101) and 118 (105).
 'u3_wal': (T+'Principles_and_practice_of_endodontic_2002_compressed_Chapterwise/07_Part_7_Local_Anesthesia.md', 13, 'Walton and Torabinejad, 2002'),
 # Grossman 14e Ch.1 (editor Gopikrishna; no chapter author named). Offset 25 confirmed at PDF 27 (printed 2) and PDF 28 (printed 3).
 'u3_gro': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/01_Chapter_1_The_Dental_Pulp_and_Periradicular_Tissues.md', 25, 'Gopikrishna, 2021'),
}
BOOK_EXTRA = {
 'u3_Walton2002': 'Walton RE, Torabinejad M, editors. Principles and Practice of Endodontics. 3rd ed. Philadelphia: WB Saunders; 2002. Part 7 Local anesthesia (no chapter author is named in the file, so the editors are cited).',
 'u3_Gopikrishna2021': "Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. New Delhi: Wolters Kluwer (India); 2021. Ch.1 The dental pulp and periradicular tissues (no individual chapter author is named in the file, so the editor is cited).",
}
L = {
 'u3_wal_ph': ('u3_wal', 'This theory has no experimental support and is an unlikely cause of anesthesia difficulties'),
 'u3_wal_pdl': ('u3_wal', 'good success rates (83 to 92%) are achieved'),
 'u3_wal_pdldur': ('u3_wal', 'The duration of profound pulpal anesthesia (either primary or supplemental) is approximately 10 to 20 minutes'),
 'u3_wal_reinj': ('u3_wal', 'failure the first time is usually followed by failure on the second attempt'),
 'u3_mal_buf': ('q03_mal', 'was 6 min 37 s for the “traditional” local anesthetic solution and 1 min 51 s'),
 'u3_mal_hot': ('q03_mal', 'Anecdotal reports from dentists, particularly endodontists, indicate that there is an increased'),
 'u3_mal_art': ('q03_mal', '(0.9–1.2 mL) at the apex of the tooth to be treated'),
 'u3_coh_mep': ('q03_coh', 'been found to obtain pulpal anesthesia for an IAN block at rates similar to those for lidocaine'),
 'u3_coh_mep50': ('q03_coh', 'the duration of pulpal anesthesia is reduced to approximately 50 minutes'),
 'u3_gro_ad': ('u3_gro', 'The Aδ fibers have a diameter of 2–5 μm and a conduction velocity of 6–30 m/s'),
 'u3_gro_c': ('u3_gro', 'C fibers have a diameter of 0.3–1.2 μm and a conduction velocity of 0.4–2 m/s'),
 'u3_rup_vel': ('q03_rup', 'Pain, temperature, touch 2–5 12–30'),
 'u3_rup_c': ('q03_rup', 'Pain 0.4–1.2 0.5–2'),
 'u3_sk3_dx': ('q03_sk3', 'Several conditions have been shown to mimic endodontic/odontogenic pain'),
}
