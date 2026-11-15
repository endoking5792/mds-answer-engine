import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')   # clone of the private textbook repo
LT = T + 'Laser_Textbooks/'
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
F = {
 # Coluzzi & Parker 1st ed 2017. Ch.9 offset 6 (PDF 197=191, 198=192, 203=197); Ch.2 offset 9 (26=17, 27=18, 34=25);
 # Ch.3 offset 9 (38=29, 39=30, 54=45); Ch.4 offset 8 (65=57, 83=75)
 'g3:cp9': (LT+'Lasers_in_Dentistry_Current_Concepts_Coluzzi_Parker.md', 6, 'George and Walsh, 2017'),
 'g3:cp2': (LT+'Lasers_in_Dentistry_Current_Concepts_Coluzzi_Parker.md', 9, 'Coluzzi, 2017'),
 'g3:cp3': (LT+'Lasers_in_Dentistry_Current_Concepts_Coluzzi_Parker.md', 9, 'Parker, 2017'),
 'g3:cp4': (LT+'Lasers_in_Dentistry_Current_Concepts_Coluzzi_Parker.md', 8, 'Selting, 2017'),
 # Coluzzi & Parker 2nd ed 2023, Ch.9 offset 8 (PAGE 299=291, 301=293, 305=297)
 'g3:cp9b': (T+'Operative_and_Dental_Materials_Textbooks/Lasers_in_Dentistry_Current_Concepts.md', 8, 'George and Walsh, 2023'),
 # Convissar 2nd ed 2016, Ch.13 offset 6 (PDF 226=220, 227=221, 233=227)
 'g3:conv13': (LT+'Principles_and_Practice_of_Laser_Dentistry.md', 6, 'Stabholz et al, 2016'),
 # Pandey 2018: no printed folios visible in the file
 'g3:pan': (LT+'Lasers_in_Operative_Dentistry_and_Endodontics.md', None, 'Pandey, 2018'),
 # Grossman 14th ed 2021 Ch.24 offset 25 (PDF 498=473, 499=474, 503=478)
 'g3:gro': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/24_Chapter_24_Lasers_in_Endodontics.md', 25, 'Gopikrishna, 2021'),
 # Sikri 2nd ed (eBook 2019) Ch.31 offset 21 (PDF 567=546, 568=547, 570=549)
 'g3:sik': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/31_31_Lasers_in_Endodontics.md', 21, 'Sikri, 2019'),
 # Current Therapy in Endodontics 2016 Ch.10 offset 26 (PDF 284=258, 285=259, 289=263)
 'g3:ct10': (T+'Current_Therapy_in_Endodontics_Chapterwise/10_11_pdf_p_284_296.md', 26, 'Alshahrani et al, 2016'),
 # Seltzer & Bender 2nd ed 2012 Ch.15: printed folios not in the file
 'g3:sb15': (T+'Seltzer_and_Bender_Dental_Pulp_Chapterwise_MD/Chapter_15_Effects_of_Thermal_and_Mechanical_Challenges.md', None, 'Goodis and Pashley, 2012'),
 # Cohen's 12th ed Ch.14: printed folios not in the file
 'g3:coh14': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/14_14_Pulp_reactions_to_caries_and_dental_procedures.md', None, 'Fouad and Levin, 2021'),
 # DCNA (PDF via PyMuPDF): Banday et al, Dent Clin N Am 70 (2026) 31-44, offset 30 (PDF 1=31, 2=32, 7=37);
 # Mortman, Dent Clin N Am 55 (2011) 461-480, offset 460 (PDF 1=461, 8=468, 9=469)
 'g3:ban': ('/Users/niranjan/Library/CloudStorage/OneDrive-Personal/MDS III/DCNA articles/1-s2.0-S0011853225000473.pdf', 30, 'Banday et al, 2026'),
 'g3:mort': ('/Users/niranjan/Library/CloudStorage/OneDrive-Personal/MDS III/DCNA articles/1-s2.0-S0011853211000206.pdf', 460, 'Mortman, 2011'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
L = {
 # --- George & Walsh 2017 (Coluzzi & Parker 1st ed Ch.9)
 'g3_goal': ('g3:cp9', 'The primary goal of root canal treatment is to eliminate microorganisms from the root canal system and radicular dentin'),
 'g3_untouched': ('g3:cp9', 'large parts of the root canal system are untouched'),
 'g3_ldfprin': ('g3:cp9', 'With movement of erythrocytes, the scattered light is frequency-shifted, whilst light reflected from static tissue is un-shifted'),
 'g3_ldfgold': ('g3:cp9', 'comes closest to serving as a “gold standard,”'),
 'g3_ldfperio': ('g3:cp9', 'superimposed signals arising from blood flow in the periodontal tissues rather than in the pulp'),
 'g3_ldfwl': ('g3:cp9', 'Visible red and near-infrared wavelengths are the most suitable'),
 'g3_ldfcrown': ('g3:cp9', 'LDF cannot be used when the tooth is covered with an opaque full coverage restoration'),
 'g3_diag655': ('g3:cp9', 'which utilizes visible red laser light (wavelength 655 nm) to elicit fluorescence emissions in the near-infrared range'),
 'g3_fl5': ('g3:cp9', 'an average fluorescence reading of 5 (on a scale of 100)'),
 'g3_flquench': ('g3:cp9', 'Oxidants can quench fluorescence signals'),
 'g3_fltetra': ('g3:cp9', 'False-positive fluorescence can occur with certain endodontic medicaments (e.g. tetracyclines)'),
 'g3_t_arg': ('g3:cp9', 'Argon 488–514.5 nm Endodontic disinfection'),
 'g3_t_diode': ('g3:cp9', 'Diode 810–980 nm Soft tissue surgery in endodontics, endodontic disinfection, laser-induced analgesia, laser photobiomodulation'),
 'g3_t_nd': ('g3:cp9', 'Nd:YAG 1064 nm Soft tissue surgery in endodontics, endodontic disinfection, biomechanical preparation'),
 'g3_t_ercr': ('g3:cp9', 'Er,Cr:YSGG 2780 nm Tooth preparation, soft and hard tissue surgery in endodontics'),
 'g3_t_er': ('g3:cp9', 'Er:YAG 2940 nm Tooth preparation, soft and hard tissue surgery in endodontics'),
 'g3_t_co2': ('g3:cp9', 'Carbon dioxide 10,600 nm Pulp capping; soft tissue surgery in endodontics'),
 'g3_t_ho': ('g3:cp9', 'Ho:YAG 2100 nm'),
 'g3_t_hene': ('g3:cp9', 'He-Ne 633 nm Diode 635 nm Doppler flowmetry, photoactivated disinfection of root canals'),
 'g3_levy': ('g3:cp9', 'an Nd:YAG laser with water spray was used to widen root canals in the apical zone from ISO #20 to ISO #35'),
 'g3_hoyag': ('g3:cp9', 'canals with internal dimensions of ISO #25 were widened to an apical size of ISO #40'),
 'g3_ercrledge': ('g3:cp9', 'the risk of ledging, zipping, perforation or over-instrumentation of canals was noted'),
 'g3_10deg': ('g3:cp9', 'could be used successfully to prepare root canals with curvatures up to 10 °'),
 'g3_5deg': ('g3:cp9', 'reported that preparation of canals with a curvature above 5° could lead to zipping, ledge formation or perforations'),
 'g3_difficult': ('g3:cp9', 'it is difficult to attain all of the mechanical objectives of root canal preparation when laser energy is delivered with conventional optical fibers'),
 'g3_alipoor': ('g3:cp9', 'the mechanical quality of the canal preparation (smoothness, taper, etc.) was worse with the laser method'),
 'g3_diodeheat': ('g3:cp9', 'concerns remain in terms of generation and conduction of heat to the supporting apparatus if high irradiances are used'),
 'g3_ndsmear': ('g3:cp9', 'Nd:YAG lasers are more effective for disinfecting the root canal, and relatively less effective for removing smear layer, compared to the erbium lasers'),
 'g3_takeda': ('g3:cp9', 'All lasers achieved better smear layer removal than EDTA, and the Er:YAG laser was the most effective of the three lasers used'),
 'g3_neverdry': ('g3:cp9', 'Water-based irrigant fluids should be used; the procedure should never be done dry'),
 'g3_edtaenh': ('g3:cp9', 'Laser activation enhances the action of EDTA in smear layer removal'),
 'g3_rclase': ('g3:cp9', 'such tips are too large and rigid to be used in narrow, curved root canals'),
 'g3_fins': ('g3:cp9', 'Laser light can penetrate areas of canals where irrigating and disinfecting solutions cannot reach, such as fins, deltas, and lateral canals'),
 'g3_photothermo': ('g3:cp9', 'rapid expansion of water contained within microorganisms leads to their rupture'),
 'g3_pigment': ('g3:cp9', 'primary absorption of laser energy into porphyrins, melanin, and other pigments occurs'),
 'g3_557': ('g3:cp9', 'threshold values around 5.5–7 °Celsius as the limit of acceptable temperature increases on the root surface'),
 'g3_1mm': ('g3:cp9', 'may allow a bactericidal effect beyond 1 mm of dentin'),
 'g3_nirpref': ('g3:cp9', 'greater penetration of the disinfecting action than middle-infrared wavelengths'),
 'g3_05mm': ('g3:cp9', 'Middle-infrared lasers will show the lowest penetration (~0.5 mm)'),
 'g3_apexcoronal': ('g3:cp9', 'The fiber is moved from the apex in a coronal direction, tilting and rotating the fiber'),
 'g3_motion': ('g3:cp9', 'The fiber must be kept in constant motion'),
 'g3_pad': ('g3:cp9', 'reactive oxygen species are generated, which then damage the microbial cell membrane'),
 'g3_padspec': ('g3:cp9', 'produces much less microbial killing than the'),
 'g3_padred': ('g3:cp9', 'Preferred lasers are visible red (633, 635, 660, 670 nm) when blue dyes are used'),
 'g3_icg': ('g3:cp9', 'it is a simple fluorescence dye and is not a photosensitizer'),
 'g3_notransport': ('g3:cp9', 'This problem of transportation does not occur when lasers are employed'),
 'g3_nosmear': ('g3:cp9', 'do not generate a smear layer when they are used to cut into root dentin'),
 'g3_erfluid': ('g3:cp9', 'Er:YAG and Er,Cr:YSGG lasers are ideally suited for activating fluids'),
 'g3_lai2008': ('g3:cp9', 'Since the description of laser fluid activation in 2008'),
 'g3_bubbles': ('g3:cp9', 'Rapid fluid motion is caused by expansion and subsequent implosion of laser-induced bubbles'),
 'g3_notapical': ('g3:cp9', 'The laser tip does not have to be placed into the apical third of the root canal'),
 'g3_extr25g': ('g3:cp9', 'was no greater than that seen when conventional 25-gauge non-side-venting irrigation needles were used'),
 'g3_cavitspeed': ('g3:cp9', 'will show the fastest cavitation (microseconds) versus 940–980 nm diode lasers (seconds)'),
 'g3_diodeagit': ('g3:cp9', 'the fluid agitation effects are less for a diode laser than for an erbium laser'),
 'g3_h2o2': ('g3:cp9', 'For diode lasers, the cavitation effects can be enhanced by supplementing the water with hydrogen peroxide to a final concentration of 3%'),
 'g3_refresh': ('g3:cp9', 'When the irrigant fluid is refreshed between cycles of laser exposure, there is a strong beneficial effect on temperature'),
 'g3_pbm': ('g3:cp9', 'on the enzymes of the electron transport chain in mitochondria'),
 'g3_pbmwl': ('g3:cp9', 'from the action of visible red (633–635 nm) or near-infrared (810–1100 nm) light'),
 'g3_adelta': ('g3:cp9', 'more selective for depolarization of A delta fibers (rapid, sharp, well-localized pain) than for C fibers'),
 'g3_bystander': ('g3:cp9', 'Bystander LLLT effects occur in the periodontal ligament and periapical bone'),
 'g3_pulpolasers': ('g3:cp9', 'The lasers used have included Nd:YAG, Er:YAG, carbon dioxide and 632 or 980 nm diode lasers'),
 'g3_pulpoadv': ('g3:cp9', 'shorter operating time, simpler procedure and less postoperative pain'),
 'g3_capping': ('g3:cp9', 'direct pulp capping using lasers with carbon dioxide, 808 nm diode, Er:YAG and Er,Cr:YSGG lasers'),
 'g3_icr': ('g3:cp9', 'Lesions of invasive cervical resorption can be treated by laser ablation, as an alternative to the traditional approach using trichloracetic acid'),
 'g3_bonecut': ('g3:cp9', 'These middle-infrared lasers give deep cuts with sharp edges which are free of charring'),
 'g3_apicohealing': ('g3:cp9', 'significantly better results in terms of postoperative healing, in comparison with using conventional surgical approaches'),
 'g3_microscope': ('g3:cp9', 'filters fitted to the objective of the microscope to match the laser wavelengths in use'),
 'g3_zach': ('g3:cp9', 'an intra-pulpal temperature increase of approximately 5.5 °C can promote necrosis of the dental pulp in 15% of cases'),
 'g3_47': ('g3:cp9', 'The supporting periodontal apparatus is known to be sensitive to temperatures of 47 °C'),
 'g3_60': ('g3:cp9', 'temperatures of 60 °C and above will permanently stop blood flow and cause bone necrosis'),
 'g3_7c': ('g3:cp9', 'A threshold temperature increase of 7 °C is commonly considered as the highest thermal change which is biologically acceptable'),
 'g3_tr': ('g3:cp9', 'The use of pulsed lasers with short pulse durations will minimize the zone of thermal damage'),
 'g3_drycanal': ('g3:cp9', 'a dry root canal is devoid of fluid and will conduct energy similar to a solid body'),
 'g3_superior': ('g3:cp9', 'laser-based methods can provide not only equivalent but now superior results in terms of effective debridement of the root canal'),
 # --- George & Walsh 2023 (2nd ed)
 'g3b_hist': ('g3:cp9b', 'so its inclusion here is purely for historical reasons'),
 'g3b_crack': ('g3:cp9b', 'They used an 810-nm diode laser at a power of 1 W in a continuous wave mode'),
 'g3b_crackvitro': ('g3:cp9b', 'showed in an in vitro study that significantly more laser energy passes through teeth with cracks'),
 'g3b_sweeps': ('g3:cp9b', 'PIPS uses single short pulse, while SWEEPS® delivers pulses in pairs'),
 'g3b_rsweeps': ('g3:cp9b', 'but without increasing the risk of apical extrusion of irrigation fluids'),
 'g3b_05naocl': ('g3:cp9b', 'enhanced the distribution and action of 0.5% NaOCl to reach the same level of'),
 'g3b_ultra': ('g3:cp9b', 'may give better reductions in levels of bacteria than ultrasonic agitation delivered through an endodontic file'),
 'g3b_cahrem': ('g3:cp9b', 'laser agitation of fluid may enhance the removal of certain intracanal medicaments'),
 'g3b_padclear': ('g3:cp9b', 'the root canal system is cleared of all fluids that could dilute or inactivate the dye'),
 'g3b_557': ('g3:cp9b', 'threshold values around 5.5–7 °C as the limit of acceptable temperature increases on the root surface'),
 'g3b_ercr': ('g3:cp9b', 'Er,Cr:YSGG 2780 nm'),
 # --- Coluzzi 2017 Ch.2, Parker 2017 Ch.3, Selting 2017 Ch.4
 'g3c_cw': ('g3:cp2', 'KTP, diode, and older model CO2 lasers operate in this manner'),
 'g3c_frp': ('g3:cp2', 'Nd:YAG, Nd:YAP, Er:YAG, and Er,Cr:YSGG and some carbon dioxide devices operate as free-running, direct pulsed lasers'),
 'g3c_fiber': ('g3:cp2', 'Shorter wavelength instruments, such as KTP, diode, and Nd:YAG lasers, have small, flexible fiber-optic systems'),
 'g3c_erpulse': ('g3:cp3', 'free-running pulsed emission modes (pulse width 50–150 μs), which give rise to high peak power levels (>1000 watts)'),
 'g3c_nowater': ('g3:cp4', 'water which makes up more than 70% of most tissues is not a chromophore and produces almost no interaction at diode wavelengths'),
 'g3c_ndpoor': ('g3:cp4', 'The Nd:YAG laser at 1064 nm suffers from the same poor absorption as all diode lasers'),
 'g3c_ndcost': ('g3:cp4', 'Nd:YAG lasers are more complex and considerably more expensive than diode lasers'),
 # --- Stabholz et al 2016 (Convissar Ch.13)
 'cv_list': ('g3:conv13', 'Cleaning and disinfecting the root canal system'),
 'cv_lackrct': ('g3:conv13', 'regarding the lack of well-designed clinical studies that clearly demonstrate the advantage of lasers over currently used conventional methods'),
 'cv_ldf': ('g3:conv13', 'LDF uses low-power settings (1 to 2 mW) of helium-neon (HeNe) or diode (810 nm) light sources'),
 'cv_ldf80': ('g3:conv13', 'up to 80% of the laser Doppler blood flow signal recovered from intact human teeth without a rubber dam in place is of nonpulpal origin'),
 'cv_moritz': ('g3:conv13', '89% of patients in the experimental group had no symptoms and exhibited normal responses to vitality tests'),
 'cv_68': ('g3:conv13', 'versus only 68% in the control group'),
 'cv_white': ('g3:conv13', 'White et al.32 found that use of a pulsed Nd:YAG laser with an energy level less than 1 W, with a 10-Hz repetition rate and overall 10-second exposure time'),
 'cv_smear': ('g3:conv13', 'a deeper layer packed into the dentinal tubules to a depth of up to 40 μm'),
 'cv_35': ('g3:conv13', 'more than 35% of the canals’ surface area remained unchanged after instrumentation'),
 'cv_straight': ('g3:conv13', 'The emission of laser energy from the tip of the optical fiber or the laser tip is directed along the root canal and not necessarily laterally'),
 'cv_360': ('g3:conv13', 'it is almost impossible to obtain uniform 360-degree coverage of the internal aspect of the root canal system surface using a laser'),
 'cv_mental': ('g3:conv13', 'which can be hazardous in teeth close to the mental foramen or to the mandibular nerve'),
 'cv_spiral': ('g3:conv13', 'It emits the erbium laser radiation laterally to the walls of the root canal through spiral slits located all along the length of the tip'),
 'cv_halfway': ('g3:conv13', 'was noted at approximately one half the distance between the root canal walls and the cementodentinal junction'),
 'cv_fibre': ('g3:conv13', 'by a thin optical fiber—as in Nd:YAG, potassium titanyl phosphate (KTP)–Nd:YAG, Er:YSGG, argon, and diode lasers—or by a'),
 'cv_hollow': ('g3:conv13', 'hollow tube—as in CO2 and Er:YAG lasers'),
 'cv_dose': ('g3:conv13', 'In most cases the effect is directly related to the amount of irradiation and to its energy level'),
 'cv_pips': ('g3:conv13', 'the strong absorption of the wavelength in water creates a shockwave, which removes the smear layer and disinfects the canals'),
 'cv_pipsvitro': ('g3:conv13', 'These in vitro studies have established proof of principle for this technique; however, longitudinal in vivo studies'),
 'cv_obtur': ('g3:conv13', 'Using the laser irradiation as a heat source for softening gutta-percha'),
 'cv_14': ('g3:conv13', 'a temperature elevation on the outer root surface of 14.4° C with use of the Nd:YAG and of 12.9° C with the argon laser'),
 'cv_obtsimpl': ('g3:conv13', 'Currently, procedural simplification seems to be the only proven advantage of laser use'),
 'cv_yu': ('g3:conv13', 'filling (70% of samples) and broken files (55%) from the root canal space'),
 'cv_farge': ('g3:conv13', 'laser irradiation alone could not completely remove debris and obturation materials from the root canal'),
 'cv_curved': ('g3:conv13', 'in curved root canals, the procedure had to be stopped owing to the risk of lateral perforation of the root canal wall'),
 'cv_solvent': ('g3:conv13', 'the possibility of eliminating the current use of toxic solvents in removing semisolid materials'),
 'cv_retx': ('g3:conv13', 'the decisive advantage of use of lasers for this purpose remains to be confirmed'),
 'cv_co2apico': ('g3:conv13', 'did not show that CO2 laser irradiation improved the healing process'),
 'cv_ermelt': ('g3:conv13', 'the Er:YAG laser neither melts nor seals the dentinal tubules'),
 'cv_ndseal': ('g3:conv13', 'In vitro studies using the Nd:YAG laser have shown a reduction in the penetration of dye or bacteria through resected roots'),
 'cv_gouw': ('g3:conv13', 'An Er:YAG laser was applied to perform the osteotomy and root resection, whereas Nd:YAG laser irradiation was used to seal the dentinal tubules'),
 'cv_karlovic': ('g3:conv13', 'found lower values of microleakage when the root end cavities were previously prepared with an Er:YAG laser'),
 'cv_cutting': ('g3:conv13', 'the cutting speed of the Er:YAG laser is slightly slower than for conventional high-speed burs'),
 # --- Pandey 2018
 'pa_first': ('g3:pan', 'The first laser used in endodontics was reported by Weichman and Johnson (1971)'),
 'pa_ldf': ('g3:pan', 'The wavelength of the He-Ne laser is 632.8 nm and that of the semiconductor diode laser, 780 to 820 nm'),
 'pa_stent': ('g3:pan', 'stabilizing stent, made out of rubber important material needs to be fabricated individually for each patient'),
 'pa_pulpitis': ('g3:pan', 'In the case of acute pulpitis, the pain is induced immediately after laser application and continues for more than 30 seconds'),
 'pa_capmech': ('g3:pan', 'The coagulating effect of laser guarantees a dry operating area, with no bleeding'),
 'pa_deep': ('g3:pan', 'which penetrate more deeply (up to 500 to 1000 μm) and have greater capacity for scattering'),
 'pa_nir': ('g3:pan', 'The near infrared lasers (from 810 to 1340 nm) have negligible affinity for water and the hydroxyapatite of hard dental tissues'),
 'pa_mir': ('g3:pan', 'their bactericidal effect, via photothermal energy, is more superficial'),
 'pa_co2fibre': ('g3:pan', 'The inability of this wavelength to utilize a fiberoptic delivery system limits its utility in intracanal applications'),
 'pa_gram': ('g3:pan', 'Gram-negative bacteria, due to the structural characteristics of the different cell walls, are more easily destroyed with less energy'),
 'pa_dryNIR': ('g3:pan', 'the smear layer is only partially removed, and the dentinal tubules are primarily closed as a result of melting'),
 'pa_dryMIR': ('g3:pan', 'these lasers can produce over-enlarging of the coronal section, apical transportation, perforation, and root canal ledging'),
 'pa_150': ('g3:pan', 'shorter pulses (< 150 microseconds) are'),
 'pa_gated': ('g3:pan', 'Diode lasers emit their energy in a continuous-wave (CW) mode'),
 'pa_frp': ('g3:pan', 'The Nd:YAG laser and the Erbium laser family emit energy in a “pulsed” mode (also called “free-running pulse”)'),
 'pa_1mmshort': ('g3:pan', 'positioned into the canal, 1 mm shorter than the working length, irradiating while withdrawing the fiber from the canal'),
 'pa_3040': ('g3:pan', 'the apical preparation is performed with ISO 30/40 files, depending on the laser fiber diameter used'),
 'pa_fibre': ('g3:pan', 'A flexible optical fiber of 200–300 micron diameter is placed 1 mm from the apex and withdrawn coronally'),
 'pa_3log': ('g3:pan', 'The Nd:YAG (1064 nm) laser demonstrated a bacterial reduction of three log steps at 1 mm'),
 'pa_810': ('g3:pan', 'an 810 nm CW diode laser with an output power of 0.6 W achieved a mean bacterial reduction of 74% in a 500 micron slice of dentin'),
 'pa_980': ('g3:pan', 'a 980 nm CW diode laser achieved a maximum bacterial reduction of 66% at 2.3 W and 86% at 2.8 W'),
 'pa_lowshape': ('g3:pan', 'Given the low efficacy in canal preparation and shaping with the erbium lasers, the use of traditional techniques for canal preparation is required'),
 'pa_moritz': ('g3:pan', 'Moritz et al obtained an almost total eradication of 99.64% of bacteria at 1.5 W'),
 'pa_nolateral': ('g3:pan', 'these systems did not have a bactericidal effect in penetration depth in the lateral canals'),
 'pa_radial2007': ('g3:pan', 'a radial-emitting tip was proposed in 2007 for the Er,Cr:YSGG laser'),
 'pa_130': ('g3:pan', 'sodium hypochlorite penetrates only 130 μm into dentinal tubules'),
 'pa_1100': ('g3:pan', '(1100 μm from the canal lumen)'),
 'pa_mech': ('g3:pan', 'Laser activation of solutions occurs primarily by photomechanical and photothermal mechanisms, rather than by photochemical or photodynamic processes'),
 'pa_lgsnd': ('g3:pan', 'LGS have been shown with erbium (Er:YAG and Er, Cr:YSGG), 940 and 980 nm diode, and Nd:YAG lasers'),
 'pa_quartz30': ('g3:pan', 'for an Er:YAG laser only 30% of the laser power can be transmitted through a quartz tip which is 12 mm long'),
 'pa_iso20': ('g3:pan', 'canals need to be widened to the minimum size of an ISO #20 file before the fiber can be used safely in the root canal'),
 'pa_precurve': ('g3:pan', 'optical fiber tips cannot be precurved to the canal shape'),
 'pa_demoor': ('g3:pan', 'held steady at 5 mm from the apex, to activate sodium hypochlorite at 2.5%'),
 'pa_pipstip': ('g3:pan', 'A novel nonablative, 9 mm long, 600 µm diameter quartz tapered tip with the polyamide sheath stripped 3 mm from its end'),
 'pa_pipsparam': ('g3:pan', 'uses extremely low energy levels (< 20 mJ) and short microsecond pulse rates (50 µs at a wavelength of 2,940 nm)'),
 'pa_400w': ('g3:pan', 'it produces a high peak power of 400 Watts'),
 'pa_coronal': ('g3:pan', 'coronal portion of thepulpal chamber and left stationary'),
 'pa_pipsenergy': ('g3:pan', 'utilizes very low energy (ranging from 50 mJ to 20 mJ) at 10 to 15 Hz delivered with very short pulses (50 microseconds)'),
 'pa_peters': ('g3:pan', 'a significant reduction of the bacterial load of 99.5% of 3 week-incubated bacterial biofilm, by using PIPS and NaOCl for 30 seconds'),
 'pa_73': ('g3:pan', 'laser activation of distilled water alone was not sufficient to yield bacteria reduction (73%)'),
 'pa_tet': ('g3:pan', 'the deeply penetrating Nd:YAG laser wavelength for the deep thermal disinfection of the dentin'),
 'pa_tetnd': ('g3:pan', 'deeply decontaminated using the Nd:YAG 200 ìm laser fiber at 1.5 W and 15 Hz'),
 'pa_padsys': ('g3:pan', 'The emitter is then placed in the root canal and irradiation carried out for 120 seconds'),
 'pa_tbo': ('g3:pan', 'Peak absorption 633 nm'),
 'pa_bonsor': ('g3:pan', 'It was found that PAD system offers a means of destroying bacteria remaining after conventional irrigants in endodontic therapy'),
 'pa_perf': ('g3:pan', 'pulp-chamber floor perforations can be effectively treated by eliminating the smear-layer using Nd:YAG laser'),
 'pa_vrf': ('g3:pan', 'Using a neodymium: yttrium-aluminum-garnet laser beam to seal vertical root fracture line with tricalcium phosphate paste'),
 'pa_cost': ('g3:pan', 'Since laser devices are still relatively costly, access to them is limited'),
 'pa_water': ('g3:pan', 'Water, for example, is relatively transparent to the shorter wavelengths, like argon, diode and Nd:YAG'),
 'pa_abser': ('g3:pan', 'Er:YAG (2.94 μm) 12,250 cm–1 (0.9 μm)'),
 'pa_absercr': ('g3:pan', 'Er, Cr:YSGG (2.78 μm) 6500 cm–1 (1.6 μm)'),
 'pa_noquartz': ('g3:pan', 'The Er:YAG and Er, Cr:YSGG wavelengths cannot be delivered through quartz optical fibers like soft tissue lasers (e.g. diode and Nd:YAG) can'),
 'pa_erdeliv': ('g3:pan', 'Wavelength: 2940 nm Emission mode: Continuous wave/pulsed Delivery system: Optical fiber or waveguide'),
 'pa_melanin': ('g3:pan', 'Diode and Nd:YAG has a high affinity for melanin and less interaction with hemoglobin'),
 'pa_er2900': ('g3:pan', 'Er:YAG (Erbium: yttrium aluminum garnet; λ = 2900 nm)'),
 'pa_gaalas': ('g3:pan', 'GaAlAs (Gallium-Aluminum-Arsenide, 780–890 nm) diode laser was developed in the late 1980s'),
 # --- Gopikrishna 2021 (Grossman Ch.24)
 'gr_ercr': ('g3:gro', 'Er,Cr:YSGG: 2790 nm'),
 'gr_diode': ('g3:gro', 'Wavelength: 800–980 nm'),
 'gr_ndster': ('g3:gro', 'The pulsed Nd:YAG laser is ideal for soft-tissue procedures and root canal sterilization'),
 'gr_erfibre': ('g3:gro', 'Delivered through a fiberoptic system in a pulsed mode. These wavelengths cannot be easily transmitted along the glass fiber'),
 'gr_200': ('g3:gro', 'with the help of thin fiberoptics (200 μm) as in the case of Nd:YAG'),
 'gr_hollow': ('g3:gro', 'A hollow tube is employed for this purpose in CO2 and Er:YAG lasers'),
 'gr_liu': ('g3:gro', 'Liu (2006) did a clinical trial of Nd:YAG laser pulpotomy on human primary molars and found 97% success rate'),
 'gr_adjunct': ('g3:gro', 'It can act as an adjunct to the traditional means of shaping and cleaning'),
 'gr_cost': ('g3:gro', 'This could be attributed to the high cost of technology and the need for more than one laser frequency to cover all endodontic applications'),
 'gr_1971': ('g3:gro', '1971—Weichman and Johnson: Lasers in endodontics'),
 'gr_obt': ('g3:gro', 'More clinical evidence is needed concerning the use of lasers during obturation'),
 # --- Sikri 2019
 'sk_ldf': ('g3:sik', 'It utilizes light beam from a He-Ne laser (632.8 nm)'),
 'sk_carbon': ('g3:sik', 'however, carbonization has been observed in irradiated root canals'),
 'sk_150': ('g3:sik', 'The laser energy set at 150 mJ through fiberoptic was inserted into root canal up to working length'),
 'sk_cfu': ('g3:sik', 'a decrease of 77.4% for Actinomyces and 85.8% for Pseudomonas with 10 Hz laser have been reported'),
 'sk_ndmost': ('g3:sik', 'It is further documented that Nd:YAG laser is significantly more bactericidal than other lasers'),
 'sk_retro': ('g3:sik', 'The root-surface cracking that produced by ultrasonic retropreparation tips/ conventional preparation using a bur have been overcome by lasers'),
 'sk_hydro': ('g3:sik', 'It involves removal of tissues with laser-energized water droplets'),
 'sk_analg': ('g3:sik', 'The pulsed Nd:YAG laser has been successfully used for achieving analgesia'),
 'sk_ndmelt': ('g3:sik', 'Nd:YAG laser may present melted and recrystallized dentin'),
 'g3_erbanalg': ('g3:cp9', 'as well as by pulsed Nd:YAG and middle-infrared erbium lasers'),
 'sk_instr': ('g3:sik', 'Carbon dioxide, argon and Nd:YAG lasers effectively sterilize the instruments used in endodontics'),
 # --- Alshahrani et al 2016 (Current Therapy Ch.10)
 'ct_bahcall': ('g3:ct10', 'The histological findings indicated a major bone remodeling and periodontal ligament necrosis'),
 'ct_ankylosis': ('g3:ct10', 'The latter led to ankylosis and replacement resorption'),
 'ct_shift': ('g3:ct10', 'The concept of laser use in endodontics shifted from using the laser thermal effect to using lasers at subablative energy'),
 'ct_levy': ('g3:ct10', 'the laser actually caused more mishaps than a conventional technique like ledges'),
 'ct_ldf': ('g3:ct10', 'is the only way to accurately assess the vitality of dental pulp by measuring the blood'),
 'ct_co2safe': ('g3:ct10', 'When CO2 laser is used at a low level of energy (less than 1 W), 10-Hz repletion rate, and an overall 10 seconds of exposure time'),
 'ct_pedulla': ('g3:ct10', 'They did not find a significant difference between the PIPS technique and sodium hypochlorite and needle irrigation with sodium hypochlorite'),
 'ct_extr': ('g3:ct10', 'LAI using PIPS at 0.3 W and 0.9 W did not result in more extrusion of irrigant than did the conventional technique'),
 'ct_old': ('g3:ct10', 'Uses a subablative energy (less than 1W) Uses a high energy (5–60W)'),
 'ct_needrct': ('g3:ct10', 'followed by multicenter clinical outcome studies to evaluate the feasibility of LAI'),
 'ct_noconsensus': ('g3:ct10', 'Yet there is no consensus on the ideal energy settings for each specified procedure'),
 # --- Goodis & Pashley 2012 (Seltzer & Bender Ch.15)
 'sb_invitro': ('g3:sb15', 'results from in vitro studies may overestimate pulpal temperature responses because blood flow is not available to moderate temperature changes'),
 'sb_white': ('g3:sb15', 'They obtained a 4.7°C rise in pulpal temperature using a high-speed bur across 1.0 mm of RDT, similar to that induced by the 0.7 W (10 Hz) of Nd:YAG laser irradiation'),
 'sb_spray': ('g3:sb15', 'the use of an air-water spray provides pulpal protection equivalent to that of the common dental drill'),
 'sb_limits': ('g3:sb15', 'the light guide must be very small (approximately 0.2 mm), and it must be stiff but not brittle'),
 'sb_viable': ('g3:sb15', 'bacteria often invade the tubules and remain viable below the surface, where they can multiply back into the canal'),
 'sb_periapical': ('g3:sb15', 'The potential for thermal damage to the periapical tissues remains a concern with lasers operated in the nanosecond to millisecond pulse widths'),
 'sb_60j': ('g3:sb15', 'thought to occur at energy densities somewhat less than 60 J/ cm2, although RDT is an important variable'),
 # --- Fouad & Levin 2021 (Cohen Ch.14)
 'coh_ndpulp': ('g3:coh14', 'Nd:YAG, and to a lesser degree CO2 lasers, may be associated with charring and significant inflammation in the pulp compared with Er:YAG laser'),
 'coh_15w': ('g3:coh14', '1.5 W and the greater power cause permanent'),
 'coh_ercr2790': ('g3:coh14', 'Er,Cr: YSGG at 2790'),
 'coh_erfibre': ('g3:coh14', 'Er:YAG has a wavelength of 2940 nm and is delivered using a solid optic fiber'),
 'coh_ndwater': ('g3:coh14', 'has been used extensively in dentistry because it has a high affinity for water and pigmented tissues'),
 'coh_ho': ('g3:coh14', 'The Ho:YAG laser has a wavelength of 2120 nm'),
 # --- DCNA
 'bn_ldf': ('g3:ban', 'the routine clinical adoption of LDF is limited by factors, such as procedural complexity, associated costs, and specific clinical constraints'),
 'bn_vpt': ('g3:ban', 'Laser treatment alone may not consistently provide an adequate seal in VPT'),
 'bn_diode': ('g3:ban', 'produce cavitation bubbles in irrigant fluids, greatly increasing disinfection efficacy'),
 'bn_dry': ('g3:ban', 'Overheating and melting of the root canal walls are one drawback of laser use in dry environments'),
 'bn_gp': ('g3:ban', 'using Er:YAG lasers is considerably more effective at evacuating remaining gutta-percha'),
 'bn_5c': ('g3:ban', 'a temperature increase of up to 5'),
 'bn_ndpig': ('g3:ban', 'Nd:YAG is a laser that acts on pigmented tissues, such as hemoglobin'),
 'bn_ndtable': ('g3:ban', '1,064, 1,320, 1440 Melanin, Hemoglobin, Water'),
 'mo_most': ('g3:mort', 'are the lasers that are most studied'),
 'mo_1727': ('g3:mort', 'temperature rises on the root surface ranging from 17'),
 'mo_10c': ('g3:mort', 'can be detrimental to the attachment apparatus'),
 'mo_200tip': ('g3:mort', 'The tip diameter is equivalent to a number 20 file'),
 'mo_retro': ('g3:mort', 'The laser preparation resulted in fewer cracks and chipping compared with ultrasonics'),
 'mo_jha': ('g3:mort', 'concluded that neither the laser nor rotary instrumentation was able to eliminate endodontic infection'),
 'mo_nocc': ('g3:mort', 'There are no published case-controlled studies that show that the laser yields a higher degree of success than current endodontic procedures'),
 'mo_notsup': ('g3:mort', 'Research has not proved that lasers are superior to other treatment modalities'),
 'mo_straight': ('g3:mort', 'These last 2 studies simulated straight canals that were opened to a large diameter'),
 'mo_extr': ('g3:mort', 'the potential for extrusion of fluid from the apex should be considered'),
}
def norm(s):
    s = s.replace('ﬁ','fi').replace('ﬂ','fl').replace('ﬀ','ff')
    s = s.replace('­ ', '').replace('­', '').replace('‐', '-')
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
