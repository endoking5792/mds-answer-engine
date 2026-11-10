# Second-reader audit U1 additions for Q01. Keys prefixed u1_.
import os
T = os.environ.get('MDS_TEXTBOOKS', '/home/user/mds-textbooks/')
F_EXTRA = {
 'u1_gr': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/07_Chapter_7_Endodontic_Emergencies.md', 25, 'Gopikrishna, 2021'),
 'u1_coh': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/19_19_Management_of_endodontic_emergencies.md', None, 'Teixeira and Cheung, 2021'),
 'u1_tor': (T+'Endodontics_Principles_and_Practice_Chapterwise/09_9_Endodontic_Emergencies_and_Therapeutics.md', 7, 'Walton and Ruparel, 2021'),
 'u1_wei': (T+'Weines_Endodontics_Full_Chapterwise/03_CHAPTER_3_Endodontic_Emergency_Treatment.md', None, 'Weine, 2004'),
}
BOOK_EXTRA = {}
L = {
 'u1_tor_apap': ('u1_tor', 'Therefore a lower dose of 325 to 500 mg'),
 'u1_gr_second': ('u1_gr', 'To be prescribed with caution as the second line of management'),
 'u1_gr_combo': ('u1_gr', 'In acute emergencies, a combination of NSAID and opioids is'),
 'u1_gr_shape': ('u1_gr', 'The step-back shaping technique has a greater tendency to extrude debris into the periradicular region than the crown-down technique'),
 'u1_gr_retx': ('u1_gr', 'this textbook would recommend all symptomatic retreatment'),
 'u1_gr_vert': ('u1_gr', 'A vertical incision would leave an unsightly'),
 'u1_gr_disocc': ('u1_gr', 'the tooth should be disoccluded slightly if it'),
 'u1_coh_occl': ('u1_coh', 'occlusal reduction has been reported to reduce posttreatment pain'),
 'u1_wei_vital': ('u1_wei', 'were left open, 5.11 appointments were needed to complete'),
}
