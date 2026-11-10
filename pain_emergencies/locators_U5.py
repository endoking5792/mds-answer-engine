import os
# Second-reader audit U5 additions for Q07, Q08, Q09, Q11, Q12 and P1 (keys prefixed u5_).
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
F_EXTRA = {
 # Walton and Torabinejad, Principles and Practice of Endodontics (2002) Part 30 (Hargreaves, Baumgartner per contents list). Offset 20 confirmed at PDF 555 (printed 535), 556 (536) and 557 (537). OCR slight damage: clean phrases only.
 'u5_hb30': (T+'Principles_and_practice_of_endodontic_2002_compressed_Chapterwise/30_Part_30_Endodontic_Therapeutics.md', 20, 'Hargreaves and Baumgartner, 2002'),
 # Same book Part 17 (Walton, Hutter per contents list). Offset 13 confirmed at PDF 316 (printed 303), 317 (304) and 318 (305).
 'u5_wh17': (T+'Principles_and_practice_of_endodontic_2002_compressed_Chapterwise/17_Part_17_Endodontic_Emergencies.md', 13, 'Walton and Hutter, 2002'),
}
BOOK_EXTRA = {}
# Vancouver reference strings for the two new sources
L_REF = {
 'u5_ref_hb30': 'Hargreaves KM, Baumgartner JC. Endodontic therapeutics. In: Walton RE, Torabinejad M, editors. Principles and Practice of Endodontics. 3rd ed. Philadelphia: WB Saunders; 2002. Ch.30.',
 'u5_ref_wh17': 'Walton RE, Hutter JW. Endodontic emergencies. In: Walton RE, Torabinejad M, editors. Principles and Practice of Endodontics. 3rd ed. Philadelphia: WB Saunders; 2002. Ch.17.',
}
L = {
 'u5_clock23': ('u5_hb30', 'for the first 2 to 3 days'),
 'u5_ibu_opt': ('u5_hb30', 'such as ibuprofen 600 mg every 6 hours, is optimal for the majority of patients'),
 'u5_steroid_no': ('u5_hb30', 'No evidence supports the prophylactic use of steroids for prevention of more severe levels of endodontic pain'),
 'u5_pen_first': ('u5_hb30', 'Penicillin VK remains the first antibiotic (antimicrobial) of choice'),
 'u5_pen_dose': ('u5_hb30', 'loading dose of 1000 mg of penicillin VK is followed by 500 mg every 6 hours for 7 days'),
 'u5_metro72': ('u5_hb30', 'if the patient\'s condition is not improving after 72 hours'),
 'u5_metro_dose': ('u5_hb30', 'The recommended dose of metronidazole is 500 mg every 6 hours for 7 days'),
 'u5_clinda_dose': ('u5_hb30', '300 mg loading dose followed by 150 to 300 mg every 6 hours for 7 days'),
 'u5_fever': ('u5_hb30', 'include fever (>100° F or'),
 'u5_continue': ('u5_hb30', 'Antibiotics should be continued for 2 to 3 days after resolution of the signs and symptoms of the infection'),
 'u5_reservoir': ('u5_hb30', 'Systemically administered antibiotics will not be effective against a reservoir of microorganisms'),
 'u5_diazepam': ('u5_hb30', 'Diazepam (Valium), at an adult dose of 5 to 15 mg'),
 'u5_triazolam': ('u5_hb30', 'Triazolam (Halcion), at a 0.25 mg oral dose, is also effective'),
 'u5_n2o40': ('u5_hb30', 'Although 40% N2O appears to have marginal effects on anxiety'),
 'u5_n2o_add': ('u5_hb30', 'N2O does not appear to have additive effects when combined with either triazolam or diazepam'),
 'u5_ludwig': ('u5_wh17', 'rapidly spread to bilateral submandibular and cervical spaces'),
 'u5_hosp': ('u5_wh17', 'requires immediate hospitalization'),
 'u5_incise_both': ('u5_wh17', 'Localized swelling (whether fluctuant or nonfluctuant) should be incised'),
 'u5_drain_days': ('u5_wh17', 'a drain is placed to permit continued drainage for 1 or 2 days or until debridement is complete'),
 'u5_not_open': ('u5_wh17', 'These teeth should not be left open to drain'),
 'u5_half': ('u5_hb30', 'more than one-half of endodontic patients do not report post-treatment pain'),
 'u5_forty': ('u5_hb30', 'approximately 40% of patients experience some pain after endodontic procedures'),
 'u5_flare24': ('u5_hb30', 'A small proportion of patients (2% to 4%) experience a post-treatment flare-up'),
 'u5_flare_pros': ('u5_wh17', 'overall incidence of flare-ups of 1.4% to 3%'),
 'u5_twelve': ('p1_tei8', 'Persistent pain has been reported in 12% of the cases'),
 'u5_predictor': ('u5_hb30', 'the best predictor of post-treatment pain appears to be the magnitude of pretreatment pain'),
}
