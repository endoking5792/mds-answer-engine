import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')
D = '/Users/niranjan/Library/CloudStorage/OneDrive-Personal/MDS III/DCNA articles/'   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
F = {
 'g4:jar': (T+'Endodontic_Irrigation_Chemical_disinfection_of_the_root_canal_system_Chapterwise/13_13_Irrigation_of_the_Root_Canal_System_by_Laser_Activation_L.md', 13, 'Jaramillo, 2015'),
 'g4:kish': (T+'Endodontic_Irrigation_Chemical_disinfection_of_the_root_canal_system_Chapterwise/14_14_Photodynamic_Therapy_for_Root_Canal_Disinfection.md', 12, 'Kishen and Shrestha, 2015'),
 'g4:pandey8': (T+'Laser_Textbooks/Lasers_in_Operative_Dentistry_and_Endodontics.md', None, 'Pandey, 2018'),
 'g4:gw17': (T+'Laser_Textbooks/Lasers_in_Dentistry_Current_Concepts_Coluzzi_Parker.md', 6, 'George and Walsh, 2017'),
 'g4:mur17': (T+'Laser_Textbooks/Lasers_in_Dentistry_Current_Concepts_Coluzzi_Parker.md', 8, 'Muruppel, 2017'),
 'g4:gw23': (T+'Operative_and_Dental_Materials_Textbooks/Lasers_in_Dentistry_Current_Concepts.md', 8, 'George and Walsh, 2023'),
 'g4:stab': (T+'Laser_Textbooks/Principles_and_Practice_of_Laser_Dentistry.md', 6, 'Stabholz et al, 2016'),
 'g4:andr9': (T+'Textbook_and_Color_Atlas_of_Traumatic_Chapterwise/09_9_Examination_and_Diagnosis_of_Dental_Injuries.md', 16, 'Andreasen et al, 2007'),
 'g4:sik9': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/09_9_Diagnosis_and_Diagnostic_Aids.md', 21, 'Sikri, 2019'),
 'g4:sik31': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/31_31_Lasers_in_Endodontics.md', 21, 'Sikri, 2019'),
 'g4:coh1': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/01_1_Diagnosis.md', None, 'Berman and Rotstein, 2021'),
 'g4:coh21': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/21_21_The_role_of_endodontics_after_dental_traumatic_injuries.md', None, 'Kahler, 2021'),
 'g4:tei14': (T+'Treatment_of_Endodontic_Infections_Chapterwise/14_Chapter_14_Supplementary_disinfection_of_the_root_canal_syst.md', None, 'Siqueira and Rôças, 2022'),
 'g4:emic13': (T+'Endodontic_Microbiology_2nd_ed_Chapterwise/13_Chapter_13_Topical_Antimicrobials_in_Endodontics.md', 5, 'Kishen, 2017'),
 'g4:guru': (D+'1-s2.0-S0011853225000485.pdf', ('dcna',45), 'Guruswamy Pandian et al, 2026'),
 'g4:mort': (D+'1-s2.0-S0011853211000206.pdf', ('dcna',461), 'Mortman, 2011'),
 'g4:band': (D+'1-s2.0-S0011853225000473.pdf', ('dcna',31), 'Banday et al, 2026'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
#   Pick clean text: avoid OCR ligature damage ("0e", "!le"), hyphen breaks and figure captions.
L = {
 # ---------- Q05 PIPS ----------
 'g4_jar_subabl': ('g4:jar', 'subablative (to evaporized at very low temperature) energies of 20 mJ at 15 Hz for an average power of 0.3 W at 50'),
 'g4_jar_peak400': ('g4:jar', 'The impulses create an interaction of water molecules with peak powers of 400 W'),
 'g4_jar_indirect': ('g4:jar', 'works indirectly and without thermal effects by activating irrigants'),
 'g4_jar_chamber': ('g4:jar', 'is not required to be placed inside the canal system itself but rather in the pulp chamber only'),
 'g4_jar_largerfiles': ('g4:jar', 'rotary instruments to create larger canal shapes to open the system'),
 'g4_jar_peterspui': ('g4:jar', 'PIPS did not completely remove bacteria from infected dentinal tubules but did generate less infection'),
 'g4_jar_divito': ('g4:jar', 'used PIPS at a wavelength of 2,940 nm with a 12 mm, 400'),
 'g4_jar_14c': ('g4:jar', 'an increase of 1.4 °C after a continuous activation of 40 s was found'),
 'g4_jar_saunders': ('g4:jar', 'an increment of more than 10 °C for more than 1 min may be'),
 'g4_jar_fincham': ('g4:jar', 'PIPS showed a velocity in excess of 1.2 m/s at 3 mm from the tip'),
 'g4_jar_noatten': ('g4:jar', 'there was no further attenuation with distance in the velocity'),
 'g4_jar_22mm': ('g4:jar', 'tip was placed 22 mm away from the target area, while ultrasonic, sonic, and passive irrigation were made at the exact target area'),
 'g4_jar_83v100': ('g4:jar', 'Our results showed an 83 % disinfection of the conventional group after 20 min of continuous irrigation versus 100 % disinfection on PIPS group'),
 'g4_jar_protocol': ('g4:jar', 'The current protocol is six 30 s cycle of laser activation'),
 'g4_jar_edta': ('g4:jar', 'The pulp chamber is then emptied, and 17 % EDTA is used with PIPS and continuous'),
 'g4_pan_cav': ('g4:pandey8', 'pulsed erbium lasers can generate a movement of fluids at high speed through a cavitation effect'),
 'g4_pan_5020': ('g4:pandey8', 'utilizes very low energy (ranging from 50 mJ to 20 mJ) at 10 to 15 Hz delivered with very short pulses (50 microseconds)'),
 'g4_pan_tip': ('g4:pandey8', 'A novel nonablative, 9 mm long, 600 µm diameter quartz tapered tip with the polyamide sheath stripped 3 mm from its end'),
 'g4_pan_photoac': ('g4:pandey8', 'This technique uses more of the photoacoustic and photomechanical phenomena rather than the photothermal'),
 'g4_pan_lai5mm': ('g4:pandey8', 'or even 5 mm from the apex as proposed for LAI'),
 'g4_pan_4x': ('g4:pandey8', 'At 21 mm, the velocities achieved with PIPS were 4 times greater than those with the ultrasonic device'),
 'g4_pan_unpub': ('g4:pandey8', 'Results from as-yet-unpublished fluid dynamics studies from the University of Southern California'),
 'g4_pan_995': ('g4:pandey8', 'significant reduction of the bacterial load of 99.5% of 3 week-incubated bacterial biofilm, by using PIPS and NaOCl for 30 seconds'),
 'g4_pan_73': ('g4:pandey8', 'laser activation of distilled water alone was not sufficient to yield bacteria reduction (73%)'),
 'g4_pan_tet': ('g4:pandey8', 'or alternatively PIPS radial-firing tips at 10– 20 mJ and 10–50 Hz with EDTA (15–17%) as rinsing'),
 'g4_gw17_pips': ('g4:gw17', 'One of the variants of this is known as photon-induced photoacoustic streaming (PIPS), which is typically used with'),
 'g4_gw17_bubble': ('g4:gw17', 'The laser-generated agitation causes fluid motion, which overcomes the bubble entrapment effect'),
 'g4_gw17_collapse': ('g4:gw17', 'Rapid fluid motion is caused by expansion and subsequent implosion of laser-induced bubbles'),
 'g4_gw17_extr': ('g4:gw17', 'was no greater than that seen when conventional 25-gauge non-side-venting irrigation needles were used'),
 'g4_gw17_highpulse': ('g4:gw17', 'Excessively high pulse energies can cause fluid extrusion through the apical foramen'),
 'g4_gw17_refresh': ('g4:gw17', 'When the irrigant fluid is refreshed between cycles of laser exposure, there is a strong beneficial effect on temperature'),
 'g4_gw23_sweeps': ('g4:gw23', 'PIPS uses single short pulse, while SWEEPS® delivers pulses in pairs'),
 'g4_gw23_collapse': ('g4:gw23', 'of first bubble and the emergence of new bubbles'),
 'g4_gw23_rsweeps': ('g4:gw23', 'A further evolution of this concept is Resonant SWEEPS (R-SWEEPS)'),
 'g4_gw23_05': ('g4:gw23', 'enhanced the distribution and action of 0.5% NaOCl to reach the same level of'),
 'g4_gw23_wall': ('g4:gw23', 'The PIPS technique aims to ensure fluid motion is along the root canal walls, rather than entirely toward the apical foramen'),
 'g4_gw23_small': ('g4:gw23', 'Several studies have shown that small volumes of fluid are extruded during PIPS and during other methods of LAI'),
 'g4_gw23_clin': ('g4:gw23', 'will include not only laboratory studies but also'),
 'g4_stab_patent': ('g4:stab', 'These researchers have patented a procedure called Photon Induced Photoacoustic Streaming (PIPS)'),
 'g4_stab_lloyd': ('g4:stab', 'They concluded that the laser technique eliminated debris better than single-needle irrigation'),
 'g4_stab_invitro': ('g4:stab', 'These in vitro studies have established proof of principle for this technique'),
 'g4_sik_pips': ('g4:sik31', 'It is a revolutionary method for cleaning and debriding the root canal system using Er:YAG laser energy at subablative power levels'),
 'g4_tei_pipsclin': ('g4:tei14', 'A clinical study reported that PIPS improved disinfection and exerted no influence in the incidence of postoperative pain'),
 'g4_tei_noclin': ('g4:tei14', 'there are no clinical studies consistently showing the safety and effectiveness of the laser devices used for intracanal disinfection'),
 'g4_mort_extr': ('g4:mort', 'the potential for extrusion of fluid from the apex should be considered when assessing intracanal laser treatments'),
 'g4_mort_nostud': ('g4:mort', 'photoacoustic streaming that has not been studied or published in the dental literature'),
 'g4_guru_lower': ('g4:guru', 'SWEEPS enables the use of NaOCl in lower concentration without minimizing its antimicrobial effect'),
 'g4_guru_negl': ('g4:guru', 'These light-activated irrigation techniques also exhibit negligible apical extrusion'),
 'g4_guru_pain': ('g4:guru', 'the incidence of postoperative pain was minimal in laser activation compared to manual dynamic activation'),
 'g4_guru_pdtpen': ('g4:guru', 'PIPS and PDT enhances the penetration of NaOCl into the dentinal tubules'),
 'g4_pan_linear': ('g4:pandey8', 'standing wave-type of fluid movement which was located only within 0.5 to 1.0 mm of the tip'),
 'g4_pan_tips': ('g4:pandey8', 'PIPS 400/12 and 600/9 tips'),
 'g4_gw17_2008': ('g4:gw17', 'Since the description of laser fluid activation in 2008'),
 'g4_jar_water': ('g4:jar', 'the output of an Er:YAG laser is strongly absorbed by water'),
 'g4_jar_1mm': ('g4:jar', 'Unlike the other conventional laser applications'),
 # ---------- Q06 PDT ----------
 'g4_kish_def': ('g4:kish', 'PDT involves the use of a nontoxic dye or photosensitizer (PS) in combination with visible light, which in the presence of molecular oxygen'),
 'g4_kish_raab': ('g4:kish', 'Oscar Raab used acridine dyes'),
 'g4_kish_wavel': ('g4:kish', 'which corresponds to the absorption wavelength of the photosensitizer being used'),
 'g4_kish_type1': ('g4:kish', 'Type I pathway involves production of radical ions of oxygen due to electron transfer from the photosensitizer triplet-excited state to the substrate'),
 'g4_kish_type2': ('g4:kish', 'Type II pathway involves production of excited singlet oxygen due to energy transfer from the photosensitizer triplet-excited state'),
 'g4_kish_resist': ('g4:kish', 'the probability of bacteria developing resistance to this treatment has been considered to be almost impossible'),
 'g4_kish_ps': ('g4:kish', 'halogenated xanthenes such as rose bengal (RB)'),
 'g4_kish_adjunct': ('g4:kish', 'Currently PDT is not considered a replacement for the existing root canal disinfection protocols but rather considered as a potential adjunct'),
 'g4_kish_soukos53': ('g4:kish', 'reported complete elimination of all bacteria except E. faecalis (53 %)'),
 'g4_kish_50nm': ('g4:kish', 'Singlet oxygen is known to diffuse approximately 50 nm'),
 'g4_kish_30pc': ('g4:kish', 'only 30 % of the total mass is bacteria'),
 'g4_kish_efflux': ('g4:kish', 'at much lower PDT dosage'),
 'g4_kish_constr': ('g4:kish', 'low oxygen tension inside the root canals, and dentin discoloration by the photosensitizer'),
 'g4_kish_bonsor': ('g4:kish', 'Combination of cleaning and shaping + PDT resulted in complete bacterial killing in 96.7 % of samples'),
 'g4_kish_bonsor867': ('g4:kish', 'Cleaning and shaping resulted in complete bacterial killing in 86.7 % of samples'),
 'g4_kish_garcez': ('g4:kish', 'PDT eliminated all drug-resistant species and all teeth were bacteria-free'),
 'g4_kish_977': ('g4:kish', 'demonstrated a 97.7 % killing of Enterococcus faecalis compared to a 30 % human'),
 'g4_kish_mix': ('g4:kish', 'the MIX-based methylene blue formulation had effective penetration into dentinal tubules and enhanced singlet oxygen generation'),
 'g4_kish_serum': ('g4:kish', 'of not only the common endodontic irrigants'),
 'g4_kish_light': ('g4:kish', 'The superiority of one type of light source over the other has not been clearly demonstrated'),
 'g4_kish_fiber': ('g4:kish', '2 logs more than the PDT with laser tip at the canal'),
 'g4_kish_siddiqui': ('g4:kish', 'effects of PDT in removing E. faecalis from root canals as compared to conventional'),
 'g4_kish_icg805': ('g4:kish', 'Indocyanine green (12.5 × 10 3 μg/mL)'),
 'g4_kish_standard': ('g4:kish', 'A standardized protocol for photosensitization and light activation is paramount for endodontic disinfection using PDT'),
 'g4_emic_twostep': ('g4:emic13', 'The first step is the photosensitization stage, during which a photosensitizer is allowed to bind to bacterial cells'),
 'g4_emic_tissue': ('g4:emic13', 'Reduction or neutralization of antimicrobial activity caused by the presence of tissue and serum within root canals'),
 'g4_gw17_pad': ('g4:gw17', 'Photoactivated disinfection (PAD), also known as photoactivated chemotherapy (PACT), is based on the interaction of laser light with photosensitizers'),
 'g4_gw17_specific': ('g4:gw17', 'produces much less microbial killing than the'),
 'g4_gw17_icgcur': ('g4:gw17', 'indocyanine green (ICG) and curcumin, which are activated at 808 and 470 nm, respectively'),
 'g4_gw17_led': ('g4:gw17', 'PAD can be undertaken with LEDs as well as with lasers'),
 'g4_gw17_12st': ('g4:gw17', 'To date, 12 studies have reported PAD as being effective in eliminating Enterococcus faecalis'),
 'g4_gw17_persist': ('g4:gw17', 'it also has potential use for eradicating persistent endodontic infections for which conventional methods have been unsuccessful'),
 'g4_gw17_notps': ('g4:gw17', 'it is a simple fluorescence dye and is not a photosensitizer'),
 'g4_gw17_phototh': ('g4:gw17', 'is a type of photothermal disinfection process and is not a photodynamic process'),
 'g4_gw17_red': ('g4:gw17', 'Preferred lasers are visible red (633, 635, 660, 670 nm) when blue dyes are used'),
 'g4_gw17_stain': ('g4:gw17', 'The dye used should not permanently stain teeth'),
 'g4_gw17_side': ('g4:gw17', 'Lateral-emitting/side-firing tips are preferred to ensure even irradiation is achieved'),
 'g4_gw17_fig': ('g4:gw17', 'Typical irradiation is 60–90 s'),
 'g4_gw23_pad': ('g4:gw23', 'it is a simple fluorescence dye and is not a photosensitizer'),
 'g4_pan_names': ('g4:pandey8', 'The concept is internationally called PACT (photodynamic antimicrobial chemotherapy), LAD (light-activated disinfection) or PAD (photo-activated disinfection)'),
 'g4_pan_127': ('g4:pandey8', 'This is used in conjunction with a 12.7 mg/L solution of the photosensitiser, Tolonium chloride and indocyanine green'),
 'g4_pan_60s': ('g4:pandey8', 'which is left in situ for a fixed period of time (60 seconds)'),
 'g4_pan_120s': ('g4:pandey8', 'The emitter is then placed in the root canal and irradiation carried out for 120 seconds'),
 'g4_pan_factors': ('g4:pandey8', 'These include the type of dye used, the dye concentration, the dose of radiation applied and the species of microorganism involved'),
 'g4_pan_633': ('g4:pandey8', 'Peak absorption 633 nm'),
 'g4_pan_mgml': ('g4:pandey8', 'Dye concentration 12–100 mg/mL'),
 'g4_pan_mb670': ('g4:pandey8', 'Methylene blue: Peak absorption 670 nm'),
 'g4_pan_rb550': ('g4:pandey8', 'Rose bengal: Peak absorption 550 nm'),
 'g4_pan_aseptim': ('g4:pandey8', 'commercially available as Aseptim™ PAD (SciCan, Germany): 635 nm, 50–100 mW with TBO + customized emitters'),
 'g4_pan_gram': ('g4:pandey8', 'Gram-positive pathogens are more sensitive to PAD than their Gram-negative counterparts'),
 'g4_pan_invivo': ('g4:pandey8', 'There is a consistent lack of in vivo research'),
 'g4_sik_singlet': ('g4:sik31', 'irradiation leads to the production of singlet oxygen, which may cause bacterial cell wall to rupture, killing the bacteria'),
 'g4_tei_red': ('g4:tei14', 'Most photosensitizers are activated by red light at wavelengths of 630 to 700 nm'),
 'g4_tei_after': ('g4:tei14', 'it is recommended for use after chemomechanical preparation to enhance bacterial elimination'),
 'g4_tei_lowconc': ('g4:tei14', 'A low concentration of the photosensitizer is used to avoid tooth pigmentation'),
 'g4_tei_5min': ('g4:tei14', 'which is agitated with a no. 15 K-file and left undisturbed in the canal for'),
 'g4_tei_souza': ('g4:tei14', 'does not achieve any significant supplemental effects with regard to intracanal disinfection'),
 'g4_tei_ng': ('g4:tei14', '86.5% negative cultures compared with 49% when PDT was not used'),
 'g4_tei_sr': ('g4:tei14', 'there is insufficient information supporting the benefits of its clinical use'),
 'g4_tei_diode': ('g4:tei14', 'Diode laser systems have been widely used in PDT because they are easy to handle, portable, and cost-effective'),
 'g4_mort_fotosan': ('g4:mort', 'The canal is then filled with a photosensitizer and then illuminated with a light source'),
 # ---------- Q07 LDF ----------
 'g4_stab_ldfpow': ('g4:stab', 'LDF uses low-power settings (1 to 2 mW) of helium-neon (HeNe) or diode (810 nm) light sources'),
 'g4_stab_vasc': ('g4:stab', 'because it reflects vascular rather than neural responsiveness compared with other methods'),
 'g4_stab_output': ('g4:stab', 'The output is proportional to the number and velocity of RBCs'),
 'g4_stab_80': ('g4:stab', 'up to 80% of the laser Doppler blood flow signal recovered from intact human teeth without a rubber dam in place is of nonpulpal origin'),
 'g4_stab_splint': ('g4:stab', 'The use of a rubber dam in combination with a rigid splint is recommended'),
 'g4_stab_molars': ('g4:stab', 'Molars, however, with their thicker enamel and dentin'),
 'g4_stab_comm': ('g4:stab', 'management of patients who have difficulty in communicating or of young children'),
 'g4_pan_hene': ('g4:pandey8', 'The wavelength of the He-Ne laser is 632.8 nm and that of the semiconductor diode laser, 780 to 820 nm'),
 'g4_pan_morikawa': ('g4:pandey8', 'was first introduced in 1970s by Morikawa et al to assess blood flow in microvascular systems'),
 'g4_pan_odor': ('g4:pandey8', 'The 810 nm/3.1 kHz combinations offered the greatest sensitivity and specificity'),
 'g4_pan_gazelius': ('g4:pandey8', 'differentiate b/w vital and non-vital pulps in humans was published in 1986 by Gazelius et al'),
 'g4_pan_stent': ('g4:pandey8', 'the gingiva should be covered with darkdental dam or aluminum foil'),
 'g4_pan_ambient': ('g4:pandey8', 'Changes in ambient light intensity, and'),
 'g4_pan_cost': ('g4:pandey8', 'High initial set up cost'),
 'g4_mur_wl': ('g4:mur17', 'uses laser light (632, 780– 820 nm) to measure pulpal blood flow'),
 'g4_mur_613': ('g4:mur17', 'LDF could penetrate up to 6–13 mm (depending on the density) in teeth'),
 'g4_mur_fibre': ('g4:mur17', 'probe design and fibre separation (250–500 μ)'),
 'g4_mur_8090': ('g4:mur17', 'studies have attributed 80–90% accuracy for pulp vitality assessments'),
 'g4_mur_ortho': ('g4:mur17', 'measuring pulpal blood flow during tooth movement'),
 'g4_mur_cost': ('g4:mur17', 'incumbent costs and initial investment have yet to make it a ubiquitous diagnostic methodology'),
 'g4_gw17_sensory': ('g4:gw17', 'provides information about the dental pulpal sensory supply, but not about its blood supply'),
 'g4_gw17_unshift': ('g4:gw17', 'whilst light reflected from static tissue is un-shifted'),
 'g4_gw17_semi': ('g4:gw17', 'painless, semiquantitative assessment of pulpal blood flow'),
 'g4_gw17_atrisk': ('g4:gw17', 'the pattern of results over time can guide decisions around'),
 'g4_gw17_gold': ('g4:gw17', 'comes closest to serving as a “gold standard,”'),
 'g4_gw17_posture': ('g4:gw17', 'the posture of the patient and their heart rate'),
 'g4_gw17_cavity': ('g4:gw17', 'place the probe on dentin in the floor of a cavity in the tooth, rather than on the enamel surface'),
 'g4_gw17_amalgam': ('g4:gw17', 'Light will not, however, pass through amalgam restorations or gold crowns'),
 'g4_gw17_redir': ('g4:gw17', 'Visible red and near-infrared wavelengths are the most suitable'),
 'g4_gw17_transm': ('g4:gw17', 'blood flow signals do not include flow of nonpulpal (e.g. periodontal) origin'),
 'g4_andr_vasc': ('g4:andr9', 'whereas laser Doppler flowmetry (LDF) assesses the presence of a functioning vascular supply'),
 'g4_andr_34m': ('g4:andr9', 'it was possible to diagnose the state of pulp revascularization approximately 3–4 months before EPT'),
 'g4_andr_23mm': ('g4:andr9', 'the optimal position of the probe should be 2–3 mm from the facial gingiva'),
 'g4_andr_97': ('g4:andr9', 'the sensitivity of LDF was 97%'),
 'g4_andr_100': ('g4:andr9', 'the specificity of LDF in regard to pulp vitality was 100%'),
 'g4_andr_pigment': ('g4:andr9', 'blood pigment within a discolored tooth crown can interfere with laser light transmission'),
 'g4_andr_time': ('g4:andr9', 'the time required to test a single tooth must be reduced significantly (presently, 10–15min)'),
 'g4_sik_10mm3': ('g4:sik9', 'detects red blood cell movement in a small volume of tissue (about 10 mm3)'),
 'g4_sik_flux': ('g4:sik9', 'produce a signal that is a function of the red cell flux (volume of cells illuminated × mean cell velocity)'),
 'g4_sik_twofibre': ('g4:sik9', 'carries light by one fiber and receives back the scattered (reflected) light by another fiber'),
 'g4_sik_meds': ('g4:sik9', 'Systemic medications may alter blood flow in pulp'),
 'g4_sik_jig': ('g4:sik9', 'Need custom fabricated jig to hold sensor'),
 'g4_sik_po': ('g4:sik9', 'Red light (660 nm) and (ii) Infrared light (800 nm)'),
 'g4_sik_ponotpulse': ('g4:sik9', 'Pulpal blood flow is not pulsed, as arterioles are present'),
 'g4_coh1_objective': ('g4:coh1', 'the collected data are based on objective findings rather than subjective patient responses'),
 'g4_coh1_notroutine': ('g4:coh1', 'However, this technology is not being used routinely in the dental practice'),
 'g4_coh1_po': ('g4:coh1', 'it is designed to measure the oxygen concentration in the blood and the pulse rate'),
 'g4_coh21_wl': ('g4:coh21', 'It uses a beam of infrared (780 to 820 nm) or near-infrared (632.8 nm) light'),
 'g4_coh21_dog': ('g4:coh21', 'laser Doppler was able to correctly detect blood flow as early as 2 to 3 weeks after avulsion of an immature tooth'),
 'g4_mur_static': ('g4:mur17', 'the only movement is that of the red blood cells in the pulp'),
 'g4_gw17_repro': ('g4:gw17', 'Finding a reproducible position for the tip is important'),
 'g4_andr_fig': ('g4:andr9', 'recording from a non-vital tooth (A) and adjacent normal (control) tooth (B)'),
 'g4_band_ldf': ('g4:band', 'the routine clinical adoption of LDF is limited by factors, such as procedural complexity, associated costs, and specific clinical constraints'),
}
def norm(s):
    s = s.replace('\ufb01','fi').replace('\ufb02','fl').replace('\ufb00','ff')
    s = s.replace('\u00ad ', '').replace('\u00ad', '').replace('\u2010', '-')
    s = re.sub(r'\s+', ' ', s).replace('- ', '')
    return s.strip()
_cache = {}
def _pages(path):
    if path in _cache: return _cache[path]
    if path.endswith('.pdf'):
        import fitz
        d = fitz.open(path); pages = {i+1: p.get_text() for i,p in enumerate(d)}
    else:
        txt = open(path,encoding='utf8').read()
        parts = re.split(r'(?:<!-- PDF page (\d+) -->|===== PAGE (\d+) =====)', txt)
        pages = {}
        for i in range(1,len(parts),3):
            cur = int(parts[i] or parts[i+1]); pages[cur] = pages.get(cur,'')+' '+parts[i+2]
    _cache[path] = {k: norm(v) for k,v in pages.items()}
    return _cache[path]
def find(key):
    f,ph = L[key]; path,off,cite = F[f]
    pages = _pages(path); n = norm(ph)
    hits = [p for p,t in pages.items() if n in t]
    if hits: return hits[0],None
    ks = sorted(pages)
    for a,b in zip(ks,ks[1:]):
        if n in pages[a]+' '+pages[b]: return a,None
    return None,None
def page_label(key):
    p,_ = find(key); f = L[key][0]; off = F[f][1]
    if p is None: return None
    if isinstance(off,tuple): return f"p.{off[1]+p-1}"
    if off is None: return f"PDF p.{p}"
    return f"PDF p.{p} (printed p.{p-off})"
if __name__=='__main__':
    bad = 0
    for k in L:
        lab = page_label(k)
        if lab is None: bad += 1; print('MISSING', k, L[k][1][:70])
    print('checked', len(L), 'missing', bad)
