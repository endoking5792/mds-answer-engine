import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')
DC = '/Users/niranjan/Library/CloudStorage/OneDrive-Personal/MDS III/DCNA articles/'   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
F = {
 'g6:cp2': (T+'Laser_Textbooks/Lasers_in_Dentistry_Current_Concepts_Coluzzi_Parker.md', 9, 'Coluzzi, 2017'),
 'g6:cp3': (T+'Laser_Textbooks/Lasers_in_Dentistry_Current_Concepts_Coluzzi_Parker.md', 9, 'Parker, 2017'),
 'g6:cp4': (T+'Laser_Textbooks/Lasers_in_Dentistry_Current_Concepts_Coluzzi_Parker.md', 8, 'Selting, 2017'),
 'g6:cp5': (T+'Laser_Textbooks/Lasers_in_Dentistry_Current_Concepts_Coluzzi_Parker.md', 8, 'Parker and Parker, 2017'),
 'g6:cpgl': (T+'Laser_Textbooks/Lasers_in_Dentistry_Current_Concepts_Coluzzi_Parker.md', -3, 'Coluzzi and Parker, 2017'),
 'g6:cp2e': (T+'Operative_and_Dental_Materials_Textbooks/Lasers_in_Dentistry_Current_Concepts.md', 11, 'Coluzzi, 2023'),
 'g6:cp5e': (T+'Operative_and_Dental_Materials_Textbooks/Lasers_in_Dentistry_Current_Concepts.md', 10, 'Parker and Parker, 2023'),
 'g6:cv2': (T+'Laser_Textbooks/Principles_and_Practice_of_Laser_Dentistry.md', 7, 'Coluzzi et al, 2016'),
 'g6:cv16': (T+'Laser_Textbooks/Principles_and_Practice_of_Laser_Dentistry.md', 6, 'Roshkind and Convissar, 2016'),
 'g6:pd': (T+'Laser_Textbooks/Lasers_in_Operative_Dentistry_and_Endodontics.md', None, 'Pandey, 2018'),
 'g6:green': (DC+'1-s2.0-S0011853211000310.pdf', -584, 'Green et al, 2011'),
 'g6:banday': (DC+'1-s2.0-S0011853225000473.pdf', -30, 'Banday et al, 2026'),
 'g6:oliv': (DC+'1-s2.0-S0011853222034565.pdf', -536, 'Oliveira and Rocha, 2022'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
#   Pick clean text: avoid OCR ligature damage ("0e", "!le"), hyphen breaks and figure captions.
L = {
 'g6_acronym': ('g6:cp2', 'acronym for light amplification by stimulated emission of radiation'),
 'g6_einstein': ('g6:cp2', 'In 1916 Albert Einstein postulated the theory of lasers'),
 'g6_stim': ('g6:cp2', 'would stimulate a release of two quanta. These would be identical in phase, direction, and wavelength'),
 'g6_popinv': ('g6:cp2', 'a population inversion occurs, meaning that a majority of atoms are in the elevated rather than the resting state'),
 'g6_threecomp': ('g6:cp2', 'an active medium, a pumping mechanism, and a resonator'),
 'g6_range17': ('g6:cp2', 'All available dental laser devices have emission wavelengths of approximately 0.45 microns'),
 'g6_media': ('g6:cp2', 'a container of gas, a solid-state crystal, or a semiconductor'),
 'g6_pump': ('g6:cp2', 'Currently diode lasers are electronically pumped; solid-state crystal lasers use high-powered strobes (flash lamps)'),
 'g6_reson': ('g6:cp2', 'One mirror is totally reflective and the opposite one is partially transmissive'),
 'g6_props': ('g6:cp2', 'Laser energy is distinguished from ordinary light by two properties'),
 'g6_collim': ('g6:cp2', 'The final laser beam begins in collimated form'),
 'g6_modes17': ('g6:cp2', 'There are two natural modes of wavelength emission for dental lasers, based on the excitation source: continuous wave and free-running pulse'),
 'g6_gated17': ('g6:cp2', 'A subset of continuous wave mode is a gated pulsed emission'),
 'g6_frp': ('g6:cp2', 'Er,Cr:YSGG and some carbon dioxide devices operate as free-running'),
 'g6_noq': ('g6:cp2', 'Current dental lasers do not utilize Q switching'),
 'g6_peak': ('g6:cp2', 'pulse with a duration of 100 μs would have a peak power of 1000 W'),
 'g6_fluence': ('g6:cp2', 'Fluence is a measurement of energy per area'),
 'g6_pd': ('g6:cp2', 'Power density is the measurement of power used per unit of area'),
 'g6_handspeed': ('g6:cp2', 'A slower speed will increase the power density'),
 'g6_range23': ('g6:cp2e', '0.45 μm, or 450 nm to 10.6 μm'),
 'g6_frp23': ('g6:cp2e', 'Er,Cr:YSGG devices operate as free-running, direct pulsed lasers'),
 'g6_modes23': ('g6:cp2e', 'There are two natural modes of wavelength emission for'),
 'g6_cvthree': ('g6:cv2', 'Thus three different emission modes are described'),
 'g6_cvgated': ('g6:cv2', 'achieved by the opening and closing of a mechanical shutter in front of the beam path'),
 'g6_cvfrp': ('g6:cv2', 'Free-running pulsed devices cannot have a continuous-wave or gated-pulse output'),
 'g6_cvrange': ('g6:cv2', 'emission wavelengths of approximately 500 to 10,600 nm'),
 'g6_cvcavity': ('g6:cv2', 'The following three components make up the laser cavity'),
 'g6_cvliquid': ('g6:cv2', 'a liquid, such as that used in some medical laser devices'),
 'g6_rats': ('g6:cv2', 'with the mnemonic device RATS'),
 'g6_scatterNIR': ('g6:cv2', 'Scattering is the predominant event with use of the near-infrared lasers in healthy soft tissue'),
 'g6_photothermal': ('g6:cv2', 'The principal laser-tissue interaction is photothermal'),
 'g6_spallation': ('g6:cv2', 'This process often is called spallation'),
 'g6_temp100': ('g6:cv2', 'vaporization of the water within the tissue occurs; this process is called ablation'),
 'g6_char200': ('g6:cv2', 'If the tissue temperature is raised to approximately 200'),
 'g6_enamelCO2': ('g6:cv2', 'The apatite crystal readily absorbs the CO2 wavelength and interacts to a lesser degree with the erbium wavelengths'),
 'g6_watererb': ('g6:cv2', 'maximally absorbs the two erbium wavelengths, followed by the two CO2 wavelengths'),
 'g6_extinct': ('g6:cv2', 'The extinction length for CO2 lasers in mucosa, for example, is 0.03 mm'),
 'g6_ndyag13': ('g6:cv2', 'such as Nd:YAG (1 to 3 mm)'),
 'g6_cvmask': ('g6:cv2', 'Most laser procedures should be performed with the surgeon wearing a 0.1-μm filtration mask'),
 'g6_cvcup': ('g6:cv2', 'Regular cup-shaped dental masks are insufficient for filtering the laser plume'),
 'g6_cv3m': ('g6:cv2', 'the beam can still have adequate energy at distances greater than 3 m'),
 'g6_cvTi': ('g6:cv2', 'An example of reflection would be the interaction between a CO2 laser and a patient'),
 'g6_cvembol': ('g6:cv2', 'guard against air embolism caused by excessive pressure of air and water spray'),
 'g6_cvretina': ('g6:cv2', 'The diode and Nd:YAG wavelengths are transmitted through the sclera, lens, iris, cornea, vitreous humor, and aqueous humor of the eye'),
 'g6_fourways': ('g6:cp3', 'will behave in one of four ways: transmission, reflection, scatter, and absorption'),
 'g6_chromo': ('g6:cp3', 'A chromophore is defined as'),
 'g6_ptl': ('g6:cp3', 'a process termed photothermolysis'),
 'g6_pbm': ('g6:cp3', 'termed photobiomodulation (PBM)'),
 'g6_intconv': ('g6:cp3', 'The commonest pathway that occurs when light is absorbed by living tissue is called internal conversion'),
 'g6_singlet': ('g6:cp3', 'energy transfer to ground state molecular oxygen to form the reactive species, singlet oxygen'),
 'g6_cco': ('g6:cp3', 'known as cytochrome-c-oxidase'),
 'g6_pigment': ('g6:cp3', 'chromophore absorption is by pigmented molecules (heme, melanin) with short wavelengths'),
 'g6_waterpeak': ('g6:cp3', 'with peak absorption occurring at approximately 3000 and 10,600 nm'),
 'g6_tear': ('g6:cp3', 'sufficient to tear target molecules apart'),
 'g6_108': ('g6:cp3', 'peak power density above 108 watts/Sq.cm can be obtained'),
 'g6_trt': ('g6:cp3', 'Thermal relaxation is inherent with free-running pulsed (FRP) emission modes and impossible to deliver with continuous wave emission modes'),
 'g6_trt63': ('g6:cp3', 'the time taken for the irradiated tissue to dissipate about 63% of the incident thermal energy'),
 'g6_coag50': ('g6:cp3', 'bacteria can be demonstrated to achieve a state of deactivation'),
 'g6_carb': ('g6:cp3', 'It is generally considered to be at temperatures around 200'),
 'g6_vapour': ('g6:cp3', 'vaporization of water occurs at 100'),
 'g6_photoac': ('g6:cp3', 'the volume change can give rise to a cavitation phenomenon and consequent shock wave'),
 'g6_ha': ('g6:cp3', 'the photonic energy value is pitiful compared to the dissociation energy of hard dental tissue'),
 'g6_intrinsic': ('g6:cp4', 'A number of parameters are dictated by design decisions during the manufacture of any clinical laser'),
 'g6_glpi': ('g6:cpgl', 'A state within the laser cavity in which the quantity of excited species of the active medium exceeds that of the unexcited species'),
 'g6_gltrt': ('g6:cpgl', 'to cool down to 37% of that value immediately after the laser pulse'),
 'g6_glres': ('g6:cpgl', 'The distal mirror is partially transmissive'),
 'g6_pd4class': ('g6:pd', 'Traditionally, lasers have been classified according to'),
 'g6_pdhaz': ('g6:pd', 'The degree of hazard to the skin or eyes following inadvertent exposure'),
 'g6_pdsoft': ('g6:pd', 'Soft tissue lasers (used for incision, excision and ablation)'),
 'g6_pdhard': ('g6:pd', 'Hard tissue lasers (act by coagulation, vaporization, re-crystallization'),
 'g6_pdIIIb': ('g6:pd', 'Higher power laser unit (up to 0.5 watts)'),
 'g6_pdrenamed': ('g6:pd', 'this class is renamed as'),
 'g6_pdsix': ('g6:pd', 'The most striking features of lasers are their'),
 'g6_pdchopped': ('g6:pd', 'Chopped: The output of a continuous wave can be interrupted by a shutter'),
 'g6_pdQ': ('g6:pd', 'Q-switched: Even shorter and more intense pulse can be obtained'),
 'g6_pdwater': ('g6:pd', 'A ranking from lowest to highest would show enamel (with 2–3%)'),
 'g6_pdspall': ('g6:pd', 'micro-explosion of apatite crystal is termed'),
 'g6_pdir': ('g6:pd', 'The wavelength range is between 730 nm and 12,000 nm'),
 'g6_pdvis': ('g6:pd', 'The visible light range is between 350 and 750 nm'),
 'g6_pduv': ('g6:pd', 'The wavelength ranges approximately from 150 to 350 nm'),
 'g6_pd3facets': ('g6:pd', 'There are 3 facets to laser safety'),
 'g6_pdIV': ('g6:pd', 'Output power: 500 mW in CW or pulsed emission mode'),
 'g6_pdIIIA': ('g6:pd', 'If viewed momentarily, will not harm the unprotected eye'),
 'g6_pdIIIB5': ('g6:pd', 'Output power: Continuous wave: 5–500 mW'),
 'g6_pdretina': ('g6:pd', 'Retina is approximately 100,000 times more vulnerable to injury than skin within retinal hazard range'),
 'g6_pdcornea': ('g6:pd', 'absorbs the emission wavelengths of Er:YAG, CO2 and Ho: YAG lasers which leads to corneal burn'),
 'g6_pdsmoke': ('g6:pd', 'Two separate suction set ups should be available for all laser cases'),
 'g6_pdinstr': ('g6:pd', 'should provide low specular or direct reflectance and large diffuse or scattered reflectance'),
 'g6_pdplastic': ('g6:pd', 'Plastic instruments should be avoided since they can melt with the laser irradiation'),
 'g6_pdskin': ('g6:pd', 'A double layer of salinesaturated surgical towels'),
 'g6_pdgreen': ('g6:pd', 'protective glasses that are usually of a blue-green color'),
 'g6_pdamber': ('g6:pd', 'which are usually of an amber color'),
 'g6_pdlso': ('g6:pd', 'Investigation of all accidents and incidents in which laser were involved'),
 'g6_pdstop': ('g6:pd', 'Stopping the use of lasers, if necessary'),
 'g6_pdcfr': ('g6:pd', 'Federal law, 21 CFR Part 1000'),
 'g6_pdexpl': ('g6:pd', 'High-pressure arc lamps or filament lamps or laser welding equipment shall be enclosed'),
 'g6_risk': ('g6:cp5', 'Failing to wear available eye protection is one of the most frequent contributing factors to laser injuries'),
 'g6_67': ('g6:cp5', 'operator error was at fault in 67% of the incidents reported'),
 'g6_iec4': ('g6:cp5', 'This committee developed a four-class system for lasers that was the global reference, later modified in 2002'),
 'g6_z1363': ('g6:cp5', 'Safe Use of Lasers in Healthcare'),
 'g6_mpe': ('g6:cp5', 'The level of laser radiation to which a person may be exposed without hazardous effect'),
 'g6_nhz': ('g6:cp5', 'Area within which the level of the direct, reflected or scattered radiation during normal operation exceeds the applicable MPE'),
 'g6_aversion': ('g6:cp5', 'Blinking of the eye or movement of the head to avoid exposure to a bright light'),
 'g6_class2': ('g6:cp5', 'Class 2 lasers are limited to 1 mW continuous wave'),
 'g6_class3R': ('g6:cp5', 'Visible continuous lasers in Class 3R are limited to 5 mW'),
 'g6_class3B': ('g6:cp5', 'Moderate-powered lasers (CW up to 500 mW, pulsed up to 30 mJ)'),
 'g6_class4': ('g6:cp5', 'High-powered lasers (CW above 500 mW)'),
 'g6_1C': ('g6:cp5', 'a new Class 1C is defined where C stands for'),
 'g6_1M': ('g6:cp5', 'may be hazardous if viewed with the aid of optical instruments'),
 'g6_3Bdiffuse': ('g6:cp5', 'Direct eye exposure to Class 3B lasers is hazardous; however, diffusely scattered radiation is generally safe'),
 'g6_keyswitch': ('g6:cp5', 'Class 4 lasers must be equipped with a key switch and a safety interlock'),
 'g6_range370': ('g6:cp5', 'the range of laser wavelengths falls within 370 nm and 10,600 nm'),
 'g6_retinal': ('g6:cp5', 'Lasers operating between 400 and 1400 nm are particularly dangerous'),
 'g6_100k': ('g6:cp5', 'will focus to an area on the retina with an irradiance of 100 kW/cm2'),
 'g6_cornea': ('g6:cp5', 'Injury to the cornea is normally very superficial'),
 'g6_blink': ('g6:cp5', 'The eyelid response time is of the order of 0.2 and 0.25 seconds'),
 'g6_visibleonly': ('g6:cp5', 'It will have no beneficial effect with beams of wavelengths outside the visible spectrum'),
 'g6_erMPE': ('g6:cp5', 'Of particular note is the substantially higher value of MPE in the region of 3.0'),
 'g6_mirror': ('g6:cp5', 'Many instruments used in dentistry are metal and in many instances the clinician will operate using a mouth mirror'),
 'g6_pulp': ('g6:cp5', 'unintentional transmission of near-IR and visible wavelengths through the tooth tissue to the pulp'),
 'g6_plumecontent': ('g6:cp5', 'water vapor, hydrocarbon gases and carbon monoxide and dioxide, together with metal fumes'),
 'g6_mask': ('g6:cp5', 'specific fine-mesh face masks capable of filtering 0.1 micron particles should be worn'),
 'g6_electro': ('g6:cp5', 'the most serious accidents reported with lasers have been due to electrocution'),
 'g6_flam': ('g6:cp5', 'Some of the common flammable materials found in the dental treatment areas are clothing, paper products, plastic, waxes and resins'),
 'g6_O2': ('g6:cp5', 'oxygen-enriched atmosphere (above 20%)'),
 'g6_ETT': ('g6:cp5', 'Rubber-based endotracheal tubes should be avoided'),
 'g6_footswitch': ('g6:cp5', 'Covered foot switch, to prevent accidental operation'),
 'g6_warn4': ('g6:cp5', 'Such a warning system is mandatory for Class IV lasers'),
 'g6_controlled': ('g6:cp5', 'Within the controlled area, all surfaces should be nonreflective'),
 'g6_fireext': ('g6:cp5', 'A suitable fire extinguisher should be sited for easy access'),
 'g6_nohzcalc': ('g6:cp5', 'The NOHZ is a complex calculation that can be done by a medical physicist'),
 'g6_lpa': ('g6:cp5', 'must appoint a laser protection advisor (LPA) and/or a laser safety officer (LSO)'),
 'g6_lsoDSA': ('g6:cp5', 'Ideally, the LSO could be a suitably trained and qualified dental surgery assistant'),
 'g6_log': ('g6:cp5', 'Maintain a log of all laser procedures carried out'),
 'g6_interrupt': ('g6:cp5', 'Assume overall control for laser use and interrupt the procedure if any safety measure is infringed'),
 'g6_testfire': ('g6:cp5', 'For visible and near-infrared wavelengths, a suitable medium would be pigmented/dark articulating paper'),
 'g6_patientfirst': ('g6:cp5', 'as a maxim to represent the safety of the patient as paramount'),
 'g6_sidepanels': ('g6:cp5', 'be fitted with suitable side panels to prevent diffuse laser beam entry'),
 'g6_wlspecific': ('g6:cp5', 'Eyewear should be constructed of wavelength-specific material'),
 'g6_od5': ('g6:cp5', 'OD scores of 5.0 and above are considered explicitly safe'),
 'g6_marked': ('g6:cp5', 'Glasses or goggles should be marked with the wavelength for which protection is given'),
 'g6_dir': ('g6:cp5', 'defines the emission mode of the laser for which the eyewear is intended'),
 'g6_loupes': ('g6:cp5', 'the clinician must wear the appropriate protective insert or shield that is specific to the wavelength being used'),
 'g6_mismatch': ('g6:cp5', 'Mismatched eye protectors were not effective for shutting out laser energy, especially for Nd:YAG and diode lasers'),
 'g6_ultrashort': ('g6:cp5', 'modern laser eye protection seems to be robust except for the irradiance possible with ultrashort laser pulse exposure'),
 'g6_localrules': ('g6:cp5', 'All staff involved in the use of these devices should read the local rules and sign them'),
 'g6_nontarget': ('g6:cp5', 'Nontarget tissue shall be suitably protected (tissue retraction, use of nonreflective instruments, wet gauze)'),
 'g6_dampgauze': ('g6:cp5', 'Shielding of the skin can be employed, using damp gauze'),
 'g6_sterile': ('g6:cp5', 'must either be heat sterilized or, if a single-use device, be properly disposed'),
 'g6_od23': ('g6:cp5e', 'An OD value of 5.0 may be considered a minimum safe level'),
 'g6_1Mlimit23': ('g6:cp5e', 'the maximum power delivery of Class I and IM must not exceed 40 μW (blue) or 400 μW (red)'),
 'g6_lss23': ('g6:cp5e', 'Laser Safety Officer (LSO) (aka Laser Safety Supervisor: LSS)'),
 'g6_iec2017': ('g6:cp5e', 'has been published in several formats with revisions from 1994 to 2017'),
 'g6_roman23': ('g6:cp5e', 'in the lower Classes (I, IM, II, IIM, IIIR)'),
 'g6_lsoansi': ('g6:cv16', 'defines the position of LSO and its responsibilities in both ANSI Z136.1 and ANSI Z136.3'),
 'g6_hazzone': ('g6:cv16', 'Determines the potential hazard zone and the nonhazard zone'),
 'g6_fda3500': ('g6:cv16', 'must be submitted on Form FDA 3500A within 10 work days'),
 'g6_registration': ('g6:cv16', 'as well as other government jurisdictions require laser devices to be registered'),
 'g6_gr3': ('g6:green', 'A laser light has three distinguishing properties'),
 'g6_grcomp': ('g6:green', 'These components consist of an energy source, an active medium, and a resonant chamber'),
 'g6_grnd': ('g6:green', 'the wavelengths of the laser beam are between 1064 and 1320 nm'),
 'g6_grTi': ('g6:green', 'The CO2 laser is reflected by titanium but may be absorbed by surrounding tissues'),
 'g6_bd2': ('g6:banday', '2 principal characteristics: monochromatic and coherent'),
 'g6_bdmode': ('g6:banday', 'By Mode of Operation: Continuous wave versus pulsed-lasers'),
 'g6_bdrisk': ('g6:banday', 'By Risk Level: Classified from Class I (safe) to Class IV'),
 'g6_bdsafety': ('g6:banday', 'wavelength-specific protective eyewear must be worn'),
 'g6_bdhve': ('g6:banday', 'high-volume evacuation systems are recommended to remove the laser-generated plume'),
 'g6_bdtemp': ('g6:banday', 'Studies indicate that a temperature increase of up to 5'),
 'g6_bdtemp7': ('g6:banday', 'with a maximum permissible rise of 7'),
 'g6_bdfire': ('g6:banday', 'Laser sparks can ignite patient fires when an oxidizer-enriched atmosphere and combustible materials are present'),
 'g6_olclass4': ('g6:oliv', 'lasers with more than 500 mW of power are classified as high-powered Class 4 visible-beam lasers'),
 'g6_olorange': ('g6:oliv', 'after 3 direct exposures with a Class 4 dental light-curing laser'),
 'g6_ollaser': ('g6:oliv', 'should always wear the appropriate laser-certified protective goggles'),
 'g6_cvktp': ('g6:cv2', 'potassium titanyl phosphate (KTP) laser: green wavelength of 532 nm'),
 'g6_cvdiode': ('g6:cv2', 'Diode lasers: various wavelengths between 800 and 1064 nm'),
 'g6_cvnd': ('g6:cv2', 'Nd:YAG laser: 1064 nm'),
 'g6_cvercr': ('g6:cv2', 'laser: 2780 nm'),
 'g6_cverYAG': ('g6:cv2', 'Er:YAG laser: 2940 nm'),
 'g6_cvco2': ('g6:cv2', 'CO2 laser: 9300 nm and 10,600 nm'),
 'g6_cvdivide': ('g6:cv2', 'the dividing line between the ionizing, cellular DNA–mutagenic portion of the spectrum and the nonionizing portion is at the junction of ultraviolet and visible-violet light'),
 'g6_diode445': ('g6:cp2', 'Indium gallium nitride'),
 'g6_aqflare': ('g6:cp5', 'Aqueous flare (protein in the aqueous humor), cataract, corneal burn'),
 'g6_iec2014': ('g6:cp5', 'has been published in several formats with revisions from 1994 to 2014'),
 'g6_iecrange': ('g6:cp5', 'emitting radiation in the wavelength range 180 nm to 1 mm'),
 'g6_cv60': ('g6:cv2', 'proteins begin to denature, without any vaporization of the underlying tissue'),
 'g6_argon': ('g6:cv2', 'Argon lasers are no longer manufactured as dental surgical instruments'),
 'g6_bdwl': ('g6:banday', 'By Wavelength: UV (140'),
 'g6_bdvis': ('g6:banday', 'Visible spectrum (400'),
 'g6_fig51': ('g6:cp5', 'Risk associated with varying laser wavelengths in anterior and posterior structures of the unprotected eye'),
 'g6_retinalhaz': ('g6:cp5', 'This spectral band of wavelengths is often referred to as the retinal hazard region'),
 'g6_skinlow': ('g6:cp5', 'The potential for risk to the skin from laser photonic energy is considered low in terms of dental treatment'),
 'g6_hollowtip': ('g6:cp5', 'tips may become extremely hot when no coaxial water spray is used'),
 'g6_plumeeffects': ('g6:cp5', 'The hazard presented by the laser plume may include eye irritation, nausea, and breathing difficulties'),
 'g6_signs': ('g6:cp5', 'Post appropriate warning signs at all points of access to the controlled area'),
 'g6_nhzopen': ('g6:cp5', 'any operatory confined by (nontransparent, physically intact) walls and doors would satisfy this requirement'),
 'g6_minpower': ('g6:cp5', 'commensurate with a policy of minimal power values to achieve the desired clinical outcome'),
 'g6_blueflame': ('g6:cp5', 'may burn with a blue flame and this may be very difficult to spot under intense operating lights'),
 'g6_pdmicro': ('g6:pd', 'When working with operating microscope and the CO2 laser, the surgeon need not wear protective glasses'),
 'g6_pdsign': ('g6:pd', 'A sign should be placed outside the operating door warning all persons entering the room to wear the protective glasses'),
 'g6_pdmutagen': ('g6:pd', 'the smoke created by the interaction of the CO2 laser with tissue is probably mutagenic'),
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
