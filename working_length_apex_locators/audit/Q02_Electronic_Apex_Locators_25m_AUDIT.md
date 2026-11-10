# Internal answer audit — Q02 Electronic apex locators (25m)

**Student-facing answer:** `canonical/Q02_Electronic_Apex_Locators_25m_CANONICAL.md`

**Last updated:** 2026-11-09 (second-reader/textbook audit U2; see audit/AUDIT_u2.md)
**Audit owner:** working_length_apex_locators team (Q02/P2 drafting agent)

> Internal working record only. Do not publish this file to the student-facing Answer Bank.

## Retrieval record

- **Sources consulted (read in full or the electronic-apex-locator and working-length sections):** Malkhassian, Plazas and Nahmias, Ch.14 of *Endodontic Radiology* 2e (ed. Basrani, 2012); Jain, Ch.4 of *Current Therapy in Endodontics* (ed. Jain, 2016); Sikri, *Essentials of Endodontics* 2e Ch.15 (2019); Weine, *Endodontic Therapy* 6e Ch.6 (2004); Gopikrishna (ed.), *Grossman's Endodontic Practice* 14e Ch.14 (2021; no chapter author named); Teixeira, Williamson and Shabahang, *Endodontics: Principles and Practice* 6e Ch.13 (2021); Walton and Torabinejad 3e Part 12 (2002; no chapter author named); Baumann and Beer (eds), *Endodontology* 2e Ch.19 (2010; chapter author not stated); Munce et al, Ingle's 7e Ch.19 (authors from Contents page; author line letter-substituted in OCR); Hülsmann and Schäfer, Ingle's 7e Ch.20 (from Contents page); Peters, Peters and Basrani, Cohen's 12e Ch.8; Roda, Gettleman and Johnson, Cohen's 12e Ch.10 (authors from chapter header); Schäfer, Harty's 7e Ch.7; Gulabivala and Ng, *Endodontics* 4e Ch.8; Gutmann and Lovdahl, *Problem Solving in Endodontics* 5e Ch.9 (2011); Barnett, *Endodontic Prognosis* Ch.7 (2017); Siqueira et al, *Treatment of Endodontic Infections* 2e Ch.12 (2022); Hülsmann and Schäfer (eds), *Problems in Endodontics* (2009) Ch.10 (OCR badly damaged); Peters and Arias, *Guidebook to Molar Endodontics* 2e Ch.7 (2025); Tonini and Garo, *Bioceramics in Endodontics* Ch.5; Attar, Chogle and Hsu, *Common Complications in Endodontics* Ch.5 (2025); AAE Glossary 2012. Also grepped for apex-locator mentions: Torabinejad Ch.18 and Ch.19, Ingle's Ch.28, 37, 38, 39, Endodontic Irrigation Ch.7 (patency), Singh preclinical conservative text. Consulted but not cited in the answers: Schäfer (Harty), Barnett, Teixeira et al, Attar et al.

- **Existing evidence reused:** none from other topics; chapter-offset conventions and bibliographic strings follow the apexification, cleaning_shaping and instruments topics (Peters et al 2021; Siqueira et al 2022; Gulabivala and Ng 2014; Jain 2016; Roda et al 2021; Hülsmann and Schäfer 2019).
- **New retrieval performed:** grep of all textbook chapters for "apex locator" (hit counts), then chapter reading as listed. Locators in `locators_Q02.py` (keys `q02_`).
- **Live literature search:** no. Journal studies mentioned inside the books (Shabahang 1996, Kim 2008, Vieyra 2010, Hassanien, Hembrough etc.) are reported only as the books report them and are not independently verified.
- **Limitations:** Ingle's 7e chapter author lines are letter-substituted in the extracted file (authors taken from Contents; verify against the printed book); Ingle's publisher/year not printed in the extracted front matter (PMPH-USA 2019 as used elsewhere in the engine); Harty 2017 and Baumann and Beer 2010 years not re-verified here; Weine, Cohen, Siqueira, Hülsmann 2009, AAE Glossary cited by PDF page only; Hülsmann and Schäfer 2009 Ch.10 OCR damaged (only clean phrases located; chapter author not legible); no chapter author for Grossman 14e, Walton 3e, Endodontology Ch.19, so editors cited.

## Source locator ledger

<!--LOC: q02_gl_def, q02_jain_circ, q02_gut_65, q02_end_6k, q02_end_imp, q02_rad_fo, q02_rad_noco, q02_rad_cust, q02_rad_suz, q02_rad_sun, q02_jain_onuki, q02_wei_inoue, q02_jain_sono, q02_jain_zx, q02_jain_g1, q02_jain_g1x, q02_jain_g1p, q02_jain_g2, q02_jain_g2c, q02_jain_g2x, q02_jain_g3, q02_jain_g3b, q02_jain_g3x, q02_jain_g4, q02_jain_g4x, q02_jain_g5, q02_jain_g5x, q02_jain_g6, q02_sik_6x, q02_sik_g5, q02_gr_g1, q02_gr_g2, q02_gr_g3, q02_gr_g4, q02_wei_3, q02_rad_dry, q02_sik_snug, q02_end_sil, q02_jain_batt, q02_jain_audio, q02_gul_ser, q02_gul_mon, q02_wal_sub, q02_gui_pull, q02_gul_zero, q02_tei_acc, q02_wei_low90, q02_rad_kim, q02_wei_long, q02_jain_ing, q02_rad_2d, q02_ing_rct, q02_rad_viey, q02_jain_xray, q02_jain_preg, q02_jain_zyg, q02_rad_tamse, q02_jain_multi, q02_sik_perf, q02_sik_hrf, q02_sik_res, q02_jain_noeal, q02_jain_radadv, q02_rad_lim, q02_ing_cap, q02_jain_open, q02_rad_sdim, q02_sik_gp, q02_cohret_clean, q02_jain_pat, q02_rad_pace, q02_sik_pace, q02_ing_pace, q02_coh_pace, q02_jain_exp, q02_jain_learn, q02_rad_sens, q02_jain_tri, q02_coh_motor, q02_ing20_comp, q02_jain_guid, q02_wal_notrep, q02_gr_rec, q02_gr_alone, q02_gut_prim, q02_jain_conf, q02_jain_3mm, q02_rad_perf, q02_jain_g1d, q02_jain_g2s, q02_jain_endocater, q02_jain_endex, q02_jain_rzx3, q02_jain_g4one, q02_jain_g4db, q02_jain_raypex4, q02_jain_g5ex, q02_sik_denapex, q02_rad_ewl, q02_rad_irr, q02_gul_ref, q02_sik_ing1, q02_ing_nopace, q02_jain_gag, u2_coh_endex, u2_wei_sono, u2_wei_res1, u2_sik_sono, u2_sik_sono2, u2_gr_sono, u2_wei_zx3, u2_wal_8095, u2_wei_1mm, u2_end_between, q02_wei_3b, q02_sik_g3-->

<!--CHECK-->Checked by build_audit.py: LOC keys 116, missing 0; quotes not found 0; answer body 1000 words (calibration 850-1000 for 25m); cited surnames not in references: none; body numbers without a locator: ['25'].<!--/CHECK-->

The table below is generated by `python3 build_audit.py audit/Q02_Electronic_Apex_Locators_25m_AUDIT.md`; do not edit it by hand.

<!--LEDGER START-->
| # | Source (in-text citation) | Chapter file | PDF page (printed page) | Verbatim locator phrase | Status |
|---|---|---|---|---|---|
| 1 | American Association of Endodontists, 2012 | 00_Pages_1_30.md | PDF p.5 | "An electronic instrument used to assist in determining the root canal working length or perforation; operates on the principles of resistance, frequency or impedance" | Verified |
| 2 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.121 (printed p.95) | "an electric circuit is formed that runs through a clip on a file, through the root canal, out the PDL" | Verified |
| 3 | Gutmann and Lovdahl, 2011 | 09_Chapter_9_Problem_Solving_in_Working_Length_Det | PDF p.199 (printed p.188) | "the periodontal membrane and the oral mucosa is a constant 6.5 kilo-ohms" | Verified |
| 4 | Baumann and Beer, 2010 | 19_19_Determination_of_Working_Length.md | PDF p.151 (printed p.134) | "a constant electrical resistance of 6 kΩ between the oral mucosa and the periodontal" | Verified |
| 5 | Baumann and Beer, 2010 | 19_19_Determination_of_Working_Length.md | PDF p.152 (printed p.135) | "This electrode impedance is highest at the apical constriction and lowest at the apical foramen" | Verified |
| 6 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.246 (printed p.226) | "it can measure the length of the root canal to the apical foramen, not to the radiographic apex" | Verified |
| 7 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.238 (printed p.218) | "less than 50% of the time, the apical foramen coincides with the anatomical apex" | Verified |
| 8 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.241 (printed p.221) | "The idea of using electronic locators was born when Custer in 1918 used the electric current to measure the length of the root canals" | Verified |
| 9 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.241 (printed p.221) | "had a constant value of 6.5 k ohms (Suzuki, 1942)" | Verified |
| 10 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.241 (printed p.221) | "Sunada in 1962 introduced this principle to the clinic area" | Verified |
| 11 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.123 (printed p.97) | "The Root Canal Meter/Endodontic Meter (Onuki Medical Co., Tokyo, Japan) was developed in 1969" | Verified |
| 12 | Weine, 2004 | 06_CHAPTER_6_Calculation_of_Working_Length.md | PDF p.758 | "in 1969 Inoue regaled those attending the annual meeting of the American Association of Endodontists in Atlanta" | Verified |
| 13 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.124 (printed p.98) | "The change in frequency method of measuring was developed by Inoue in 1971 and introduced in the Sono-Explorer" | Verified |
| 14 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.125 (printed p.99) | "Since its introduction in 1992, it has become the benchmark to which other apex locators are compared" | Verified |
| 15 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.123 (printed p.97) | "First-generation apex location devices, also known as resistance apex locators, measure opposition to the flow of direct current or resistance" | Verified |
| 16 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.123 (printed p.97) | "electrolytic substances like sodium hypochlorite caused a decrease in their efficiency and measurements" | Verified |
| 17 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.123 (printed p.97) | "the patient often felt pain due to high currents in the machines" | Verified |
| 18 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.124 (printed p.98) | "measure opposition to the flow of alternating current or impedance instead of resistance" | Verified |
| 19 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.124 (printed p.98) | "thus requiring individual calibration between each tooth" | Verified |
| 20 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.124 (printed p.98) | "The major disadvantage of second-generation electronic apex locators is that the root canal has to be reasonably free of electroconductive materials" | Verified |
| 21 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.125 (printed p.99) | "a high one at 8 kHz and a low one at 400 Hz" | Verified |
| 22 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.125 (printed p.99) | "the difference in the impedance value increases and reaches a maximum value at the apical area" | Verified |
| 23 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.125 (printed p.99) | "third-generation EALs tends to be unaffected by the presence of electrolytes in the root canal space" | Verified |
| 24 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.126 (printed p.100) | "Fourth-generation devices measure and compare the complex electrical characteristic features of the root canal at two or more frequencies of electrical impulses" | Verified |
| 25 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.127 (printed p.101) | "A significant disadvantage of this generation is that they need to perform in relatively dry or in partially dried canals" | Verified |
| 26 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.127 (printed p.101) | "Fifth-generation EALs were developed in 2003 and measure the capacitance and resistance of the circuit separately" | Verified |
| 27 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.127 (printed p.101) | "Devices employing this method experience considerable difficulties while operating in dry canals" | Verified |
| 28 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.128 (printed p.102) | "The adaptive apex locator continuously defines humidity of the canal and immediately adapts to dry or wet canal" | Verified |
| 29 | Sikri, 2019 | 15_15_Working_Length_and_Working_Width.md | PDF p.285 (printed p.264) | "Clinical accuracy is yet to be established" | Verified |
| 30 | Sikri, 2019 | 15_15_Working_Length_and_Working_Width.md | PDF p.282 (printed p.261) | "Fifth generation (blue tooth technology" | Verified |
| 31 | Gopikrishna, 2021 | 14_Chapter_14_Shaping_and_Cleaning_of_the_Radicula | PDF p.308 (printed p.283) | "These are the first generation of apex locators which were developed based on the resistance principle" | Verified |
| 32 | Gopikrishna, 2021 | 14_Chapter_14_Shaping_and_Cleaning_of_the_Radicula | PDF p.308 (printed p.283) | "This device would indicate the apex when two impedance values approach each other" | Verified |
| 33 | Gopikrishna, 2021 | 14_Chapter_14_Shaping_and_Cleaning_of_the_Radicula | PDF p.308 (printed p.283) | "These apex locators determine the canal terminus as the difference between two impedance values at two different frequencies of 1 and 5 kHz" | Verified |
| 34 | Gopikrishna, 2021 | 14_Chapter_14_Shaping_and_Cleaning_of_the_Radicula | PDF p.308 (printed p.283) | "A newer apex locator was introduced (Root ZX by J. Morita, Japan) that uses two wavelengths whose impedance could be compared as a ratio" | Verified |
| 35 | Weine, 2004 | 06_CHAPTER_6_Calculation_of_Working_Length.md | PDF p.772 | "There are three types of locators at present" | Verified |
| 36 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.245 (printed p.225) | "Drying the chamber using a gentle blow of air or using a piece of cotton pellet may overcome to this problem" | Verified |
| 37 | Sikri, 2019 | 15_15_Working_Length_and_Working_Width.md | PDF p.283 (printed p.262) | "The file should fit the size of the canal snugly" | Verified |
| 38 | Baumann and Beer, 2010 | 19_19_Determination_of_Working_Length.md | PDF p.149 (printed p.132) | "the silicone stopper (left) is better than a metal stopper (right) because the metal stopper can cause a short circuit" | Verified |
| 39 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.130 (printed p.104) | "some units do not operate effectively when the charge falls below 50%" | Verified |
| 40 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.130 (printed p.104) | "The file is slowly advanced until the audible signal changes to a higher frequency, which then changes to a continuous signal on advancing the file further" | Verified |
| 41 | Gulabivala and Ng, 2014 | 08_8_Non_surgical_root_canal_treatment.md | PDF p.193 (printed p.184) | "The European Society of Endodontology guidelines state that having used the apex locator, a confirmatory radiograph should be taken" | Verified |
| 42 | Gulabivala and Ng, 2014 | 08_8_Non_surgical_root_canal_treatment.md | PDF p.196 (printed p.187) | "the working length and patency may be monitored continuously throughout canal preparation" | Verified |
| 43 | Walton and Torabinejad, 2002 | 12_Part_12_Access_Preparation_and_length_Determina | PDF p.215 (printed p.202) | "after obtaining a reading, 1 to 2 mm is subtracted as the corrected working length" | Verified |
| 44 | Peters and Arias, 2025 | 07_7_Shaping_Disinfection_and_Obturation_for_Molar | PDF p.174 (printed p.157) | "advanced until the apex locator marks apical patency and then pulled back about 0.5 mm" | Verified |
| 45 | Gulabivala and Ng, 2014 | 08_8_Non_surgical_root_canal_treatment.md | PDF p.193 (printed p.184) | "reading for greatest accuracy and not any point short of this" | Verified |
| 46 | Siqueira et al, 2022 | 12_Chapter_12_Chemomechanical_preparation.md | PDF p.610 | "accurate to within +0.5 mm of the apical foramen in 90% to 100% of cases, irrespective of the pulpal diagnosis" | Verified |
| 47 | Weine, 2004 | 06_CHAPTER_6_Calculation_of_Working_Length.md | PDF p.769 | "the accuracy is somewhere in the low 90 percentiles" | Verified |
| 48 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.247 (printed p.227) | "when used alone was 84%, but in combination of Root ZX and radiograph, the accuracy was 96%" | Verified |
| 49 | Weine, 2004 | 06_CHAPTER_6_Calculation_of_Working_Length.md | PDF p.771 | "when apex locators err, the mistake most likely will indicate a measurement that is too long" | Verified |
| 50 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.116 (printed p.90) | "adjusting it until the file tip is 0.5 to 1 mm short of the radiographic apex" | Verified |
| 51 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.240 (printed p.220) | "It provides only a two-dimensional image of a three-dimensional object" | Verified |
| 52 | Munce et al, 2019 | 19_Chapter_19_Preparation_for_Treatment.md | PDF p.493 (printed p.551) | "the accuracy of EALs superseded those of radiograph, 90.4% versus 82.1%" | Verified |
| 53 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.247 (printed p.227) | "radiographs located minor foramen correctly 20% of the time in anterior and premolar teeth, and 11% of the time in molar teeth" | Verified |
| 54 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.118 (printed p.92) | "Radiographs are also technique sensitive and require exposing the patient to ionizing radiation" | Verified |
| 55 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.122 (printed p.96) | "Electronic apex locators can be used in pregnant women because they do not produce radiation" | Verified |
| 56 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.122 (printed p.96) | "The devices can be used when a dense zygomatic arch overlaps the apices of upper molars" | Verified |
| 57 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.241 (printed p.221) | "has been reported to be superimposed in approximately 20% and 42% on the apices of the first and second maxillary molars" | Verified |
| 58 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.122 (printed p.96) | "Electronic apex locators are very helpful in multirooted teeth" | Verified |
| 59 | Sikri, 2019 | 15_15_Working_Length_and_Working_Width.md | PDF p.285 (printed p.264) | "Excellent for detecting apical and chamber perforations" | Verified |
| 60 | Sikri, 2019 | 15_15_Working_Length_and_Working_Width.md | PDF p.286 (printed p.265) | "The exact location of horizontal root fracture can also be detected" | Verified |
| 61 | Sikri, 2019 | 15_15_Working_Length_and_Working_Width.md | PDF p.285 (printed p.264) | "Can verify the level at which the root is resorbed" | Verified |
| 62 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.130 (printed p.104) | "EALs cannot help the clinician determine canal width, canal curvature, or the number of canals" | Verified |
| 63 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.130 (printed p.104) | "the radiographic method has the advantages of being able to inspect root anatomy and document it in patient records" | Verified |
| 64 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.246 (printed p.226) | "Apex locators do not work properly in the presence of metallic restorations, profuse bleeding, saliva in contact with file, and in case of open apices" | Verified |
| 65 | Munce et al, 2019 | 19_Chapter_19_Preparation_for_Treatment.md | PDF p.493 (printed p.551) | "with a section of a plastic capillary tip" | Verified |
| 66 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.129 (printed p.103) | "tend to give short measurements electronically due to the instruments not touching the apical dentine walls" | Verified |
| 67 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.251 (printed p.231) | "the WL measurements of root canals with apical foramens larger than a size 100 K-file were not reliable" | Verified |
| 68 | Sikri, 2019 | 15_15_Working_Length_and_Working_Width.md | PDF p.283 (printed p.262) | "it is important to remove all the existing gutta-percha as it has insulating properties that may cause inaccurate readings" | Verified |
| 69 | Roda et al, 2021 | 10_10_Nonsurgical_retreatment.md | PDF p.1249 | "the apex locator will regain its accuracy if a clean file is used" | Verified |
| 70 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.129 (printed p.103) | "Lack of patency, the accumulation of dentin debris, and calcifications can affect accuracy of working length determination" | Verified |
| 71 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.246 (printed p.226) | "Patients who have a pacemaker must consult their physician to determine whether or not it is safe to use the apex locator" | Verified |
| 72 | Sikri, 2019 | 15_15_Working_Length_and_Working_Width.md | PDF p.282 (printed p.261) | "the use of these devices is contraindicated in patients with cardiac pacemakers" | Verified |
| 73 | Munce et al, 2019 | 19_Chapter_19_Preparation_for_Treatment.md | PDF p.493 (printed p.551) | "Nevertheless, some manufacturers still warn clinicians not to use EALs in patients with pacemakers" | Verified |
| 74 | Peters et al, 2021 | 08_8_Cleaning_and_shaping_of_the_root_canal_system | PDF p.925 | "when connected directly to cardiac pacemakers in vitro, electronic apex locators did not interfere with the function of the pacemaker" | Verified |
| 75 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.122 (printed p.96) | "They are relatively expensive" | Verified |
| 76 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.122 (printed p.96) | "A period of learning is a must for their efficient use" | Verified |
| 77 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.246 (printed p.226) | "Some patients have sensed electrical impulses when apex locators are used, although not common" | Verified |
| 78 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.126 (printed p.100) | "has some additional safety features such as auto-reverse when working length is reached" | Verified |
| 79 | Peters et al, 2021 | 08_8_Cleaning_and_shaping_of_the_root_canal_system | PDF p.915 | "This type of motor may be programmed to stop a rotary instrument when WL is reached or go into reverse gear" | Verified |
| 80 | Hülsmann and Schäfer, 2019 | 20_Chapter_20_Preparation_of_the_Coronal_and_Radic | PDF p.544 (printed p.605) | "accuracy and reliability of working length determination using these apex locating endodontic motors was comparable to independent apex locators" | Verified |
| 81 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.129 (printed p.103) | "Guidelines recommend a combination of electronic and radiographic methods for determining working length" | Verified |
| 82 | Walton and Torabinejad, 2002 | 12_Part_12_Access_Preparation_and_length_Determina | PDF p.216 (printed p.203) | "Importantly, this method does not replace radiographic techniques" | Verified |
| 83 | Gopikrishna, 2021 | 14_Chapter_14_Shaping_and_Cleaning_of_the_Radicula | PDF p.307 (printed p.282) | "is by using a combination of electronic apex locator along with" | Verified |
| 84 | Gopikrishna, 2021 | 14_Chapter_14_Shaping_and_Cleaning_of_the_Radicula | PDF p.308 (printed p.283) | "They can be used alone without the need of taking any radiographs" | Verified |
| 85 | Gutmann and Lovdahl, 2011 | 09_Chapter_9_Problem_Solving_in_Working_Length_Det | PDF p.200 (printed p.189) | "These findings suggest serious consideration be given to the use of apex locators as the primary means of determining the working length" | Verified |
| 86 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.130 (printed p.104) | "the EAL reading should be chosen" | Verified |
| 87 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.130 (printed p.104) | "If the radiographic length is short by more than 3 mm of the desired position, the length should be adjusted and confirmed by another radiograph" | Verified |
| 88 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.246 (printed p.226) | "Apex locators are invaluable in detection of perforations" | Verified |
| 89 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.123 (printed p.97) | "They were found to be accurate under dry conditions" | Verified |
| 90 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.124 (printed p.98) | "also known as singlefrequency impedance apex locators" | Verified |
| 91 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.124 (printed p.98) | "the Endocater (Yamaura Seisokushu, Tokyo," | Verified |
| 92 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.125 (printed p.99) | "made the original third-generation apex locator" | Verified |
| 93 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.125 (printed p.99) | "is an example of a self-calibrating third-generation apex locator based on the ratio method" | Verified |
| 94 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.126 (printed p.100) | "only one frequency is used at a time" | Verified |
| 95 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.127 (printed p.101) | "compare them with a database to determine the distance to the apex" | Verified |
| 96 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.127 (printed p.101) | "The Ray-Pex 4 and 5" | Verified |
| 97 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.127 (printed p.101) | "and Joypex 5 (Denjoy, Changsha City, China)" | Verified |
| 98 | Sikri, 2019 | 15_15_Working_Length_and_Working_Width.md | PDF p.284 (printed p.263) | "DenApex, a sixth generation multi-frequency operating system" | Verified |
| 99 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.244 (printed p.224) | "estimated working length (EWL) based on the predetermination using the preoperative radiograph" | Verified |
| 100 | Malkhassian, Plazas and Nahmias, 2012 | 14_14_Electronic_Apex_Locators_and_Conventional_Ra | PDF p.244 (printed p.224) | "the chamber and the canals are irrigated with hypochlorite solution" | Verified |
| 101 | Gulabivala and Ng, 2014 | 08_8_Non_surgical_root_canal_treatment.md | PDF p.196 (printed p.187) | "The length of the file at this reading is recorded from a stable reference point on the crown" | Verified |
| 102 | Sikri, 2019 | 15_15_Working_Length_and_Working_Width.md | PDF p.280 (printed p.259) | "Measure the tooth length on the preoperative" | Verified |
| 103 | Munce et al, 2019 | 19_Chapter_19_Preparation_for_Treatment.md | PDF p.493 (printed p.551) | "showed that there was no interference between EALs and the functionality of pacemakers" | Verified |
| 104 | Jain, 2016 | 04_5_pdf_p_113_136.md | PDF p.122 (printed p.96) | "Locators are extremely useful in patients with acute gag reflex" | Verified |
| 105 | Peters et al, 2021 | 08_8_Cleaning_and_shaping_of_the_root_canal_system | PDF p.924 | "The Endex Plus device uses 1 and 5 kHz and provides apex location based on subtraction" | Verified |
| 106 | Weine, 2004 | 06_CHAPTER_6_Calculation_of_Working_Length.md | PDF p.762 | "Mark IV Sono-Explorer, updated version of the apex locator that shocked the endodontic community" | Verified |
| 107 | Weine, 2004 | 06_CHAPTER_6_Calculation_of_Working_Length.md | PDF p.759 | "a resistance-type instrument, the first generation of apex locators" | Verified |
| 108 | Sikri, 2019 | 15_15_Working_Length_and_Working_Width.md | PDF p.282 (printed p.261) | "First generation (resistance type, e.g. Dentometer, Sono explorer Mark I, Endo Radar)" | Verified |
| 109 | Sikri, 2019 | 15_15_Working_Length_and_Working_Width.md | PDF p.282 (printed p.261) | "Second generation (impedance type, e.g. Sono explorer Mark II and III" | Verified |
| 110 | Gopikrishna, 2021 | 14_Chapter_14_Shaping_and_Cleaning_of_the_Radicula | PDF p.308 (printed p.283) | "Inoue introduced the concept of impedance-based apex locators, the Sono Explorer apex locator" | Verified |
| 111 | Weine, 2004 | 06_CHAPTER_6_Calculation_of_Working_Length.md | PDF p.764 | "This is a third-generation instrument with considerable popularity" | Verified |
| 112 | Walton and Torabinejad, 2002 | 12_Part_12_Access_Preparation_and_length_Determina | PDF p.215 (printed p.202) | "to be 80 to 95% accurate in identifying the apical foramen" | Verified |
| 113 | Weine, 2004 | 06_CHAPTER_6_Calculation_of_Working_Length.md | PDF p.771 | "only within 1 mm of the CDJ, at approximately the low 90 percentile" | Verified |
| 114 | Baumann and Beer, 2010 | 19_19_Determination_of_Working_Length.md | PDF p.152 (printed p.135) | "will vary depending upon the conductivity of the dentin" | Verified |
| 115 | Weine, 2004 | 06_CHAPTER_6_Calculation_of_Working_Length.md | PDF p.772 | "The newest two, impedance and frequency locators, indicate where the canal is the narrowest" | Verified |
| 116 | Sikri, 2019 | 15_15_Working_Length_and_Working_Width.md | PDF p.282 (printed p.261) | "Third generation (frequency type, e.g. Root ZX" | Verified |
<!--LEDGER END-->


Keep quotations short and only as long as needed to locate the source. Never copy textbook passages into this report.

## Evidence and uncertainty notes

- **[RECALL] / unverified:** none intentionally. No journal paper was opened.
- **Interpretation / synthesis:** the 'Special situations' radiograph cell ("Complicated in multirooted teeth") restates Jain's Box 4.3; the sentence "If the radiograph shows the locator length well short of the apex, the locator reading is preferred" is Jain's "recommended but not mandatory" advice; the layout of the two comparison tables is mine.
- **Conflicting sources:** (1) *Resistance of periodontium*: 6.5 kΩ (Gutmann and Lovdahl; Jain; Munce et al; Weine) vs 6 kΩ (Baumann and Beer, citing Ushiyama 1983); Sikri prints the current as 40 mA whereas Malkhassian et al print 40 μA (Sikri's mA looks like a slip, so not used). (2) *First device, 1969*: Onuki Root Canal Meter (Jain, Malkhassian, Munce) vs Inoue's resistance instrument shown to the AAE in Atlanta (Weine); Sono-Explorer is a generation-2 device in Jain and Munce but listed as generation 1 (Mark I) by Sikri; Raypex 5 is a fifth-generation example in Jain's Table 4.1 and Sikri but the Jain text also calls Ray-Pex 4 and 5 fourth-generation, so the fifth-generation example given in the answer is Joypex 5; Jain, Gopikrishna and Munce print 'Cluster' for Custer (Malkhassian and Peters et al print Custer, used). (3) *Root ZX date*: 1992 (Jain) vs 1994 launch (Munce); answer uses Jain only. (4) *Generations*: Jain, Sikri, Munce: six; Gopikrishna: four, Root ZX = fourth; Weine: three; Cohen puts Endex, Root ZX and Neosono in the third; fifth = capacitance/resistance separately (Jain, Munce) vs 'Bluetooth' (Sikri). Root ZX = third (Jain, Munce, Peters et al, Sikri) vs fourth (Gopikrishna). (5) *Reading to working length*: subtract 1 to 2 mm (Walton), withdraw about 0.5 mm (Peters and Arias; Jain for Elements), use the zero reading (Gulabivala and Ng); Radiology: push slightly beyond then withdraw to the constriction. (6) *Ingle's method end point*: 0.5 to 1 mm short of radiographic apex (Jain, Gopikrishna) vs subtract 1.0 to 1.5 mm (Sikri); Teixeira: 1 mm; Walton: 1 to 2 mm. (7) *Preflaring*: increases accuracy (Malkhassian) vs no effect (Jain). (8) *Pacemakers*: consult physician (Malkhassian, Jain), contraindicated for resistance types (Sikri), no interference in studies but advisable not to use (Teixeira) / concern unnecessary but manufacturers warn (Munce, Peters et al). (9) *Alone or combined*: Gopikrishna 'can be used alone' but recommends combination; Gutmann and Lovdahl 'primary means'; Weine, Walton, Jain, Siqueira, Hülsmann: combine, never replace. (10) Textbook slip: Malkhassian et al print accuracy 'between 8% and 94%' (likely 80%); not used.
- **Numerical claims:** 6.5 kΩ (Gutmann and Lovdahl p.188 printed; Jain PDF p.120); 6 kΩ (Baumann and Beer PDF p.151); under 50% foramen = anatomical apex (Malkhassian PDF p.238); Custer 1918, Suzuki 1942, Sunada 1962 (Malkhassian PDF p.241); Root Canal Meter 1969, Sono-Explorer 1971, Root ZX 1992 (Jain); 8 kHz/400 Hz (Jain); accuracy 90 to 100% within 0.5 mm (Siqueira PDF p.610); 'low 90 percentiles' (Weine); 84% vs 96% (Malkhassian PDF p.247); 90.4% vs 82.1% (Munce PDF p.493 (printed p.551)); 20%/11% (Malkhassian PDF p.247); 20% and 42% zygomatic arch (Malkhassian PDF p.241); size 100 K-file (Malkhassian PDF p.251); battery below 50% (Jain PDF p.130, used in P2); 1 to 2 mm (Walton PDF p.215); 0.5 mm (Peters and Arias PDF p.174); 3 mm rule (Jain PDF p.130); Ingle 0.5 to 1 mm (Jain), 1.0 to 1.5 mm (Sikri). Page references are in the ledger.
- **Literature evidence:** none opened (textbooks only).

- **U2 second-reader changes (2026-11-09):** (a) Third-generation row no longer gives 8 kHz/400 Hz for both Root ZX and Endex: Cohen (Peters et al) gives Endex Plus 1 and 5 kHz (subtraction) and Root ZX 8 and 0.4 kHz (ratio); Grossman gives Endex 1 and 5 kHz. (b) Weine's 'low 90 percentiles' is stated for locators within 1 mm of the CDJ, not 0.5 mm; separated from the Siqueira 90 to 100% (0.5 mm) figure and Walton's 80 to 95% for impedance locators (apical foramen). (c) 'Sono-Explorer introduced impedance in 1971' reworded: Jain says the change-in-frequency method of Inoue (1971) was introduced in the Sono-Explorer. Weine's 1969 Inoue instrument is the resistance-type Sono-Explorer (figure legend, Mark IV). New conflict rows: Sono-Explorer first (Weine; Sikri Mark I) vs second generation (Jain; Gopikrishna; Sikri Marks II and III); Root ZX third (Jain, Weine, Sikri, Peters et al) vs fourth (Gopikrishna). (d) Endpoint wording: Weine 'narrowest' canal; Baumann and Beer between constriction and foramen; Malkhassian and Jain foramen. (e) Gutmann and Lovdahl: 'serious consideration' of locators as primary means (was 'suggest it as the primary means'). (f) Weine 'opposes' Tri Auto ZX softened to 'criticises ... errors tend long' (his stated problem is long errors plus little US use). (g) Tamse figure: arch overlies first and second maxillary molars respectively. (h) Slip noted, not used: Jain lists the Root Canal Meter as a first-generation 'direct current' device yet describes it as alternating current at 150 Hz. (i) Cut for length, restore if wanted: Sikri 1.0 to 1.5 mm subtraction; preflaring conflict (now in P2); CBCT correlation (Jain); locator-guided apical plugs (Tonini and Garo, reference removed); Bluetooth handpiece (Ingle 7e Ch.20) and vitality-testing units (Jain); Siqueira etc retained.

## Coverage and overlap

- **Question wording / marks:** "Electronic apex locators." 25 marks (Jun 2023, Manipal).
- **Related questions:** absorbs the Q02 row in `_QUESTIONS.md` (Apex locators 10m/7m/5m; Discuss apex locators 20m; Various generations; Determination of WL by EAL; Classify EAL and limitations/advantages vs Ingle's radiographic method; Classify and note on recent advances; Advances in electronic length measurement; Recent trends in WL determination 25m). Overlaps Q01 (100m WL determination, which holds the full radiographic and tactile methods), Q03 (non-radiographic methods) and P2 (accuracy factors), each of which stands alone.
- **Content absorbed or deliberately omitted:** omitted for length (restore in a later edit if wanted): Sikri's step-by-step Ingle method and Grossman's method; Weine's step-by-step resistance-type technique; apex-locator use in primary teeth, root fractures protocol and perforation-detection protocol (Malkhassian; Jain); Cash time-saving figure; Jain troubleshooting chart; Sikri Table 15.3 study summary; Kobayashi ratio-method principle in detail; digital-radiography-plus-EAL dose point (locator `q02_rad_dig`). Not cited: Teixeira et al, Harty, Barnett, Attar et al, Common Complications (they agree with the cited books).
- **Essential omissions / open points:** answer is at the top of the 25m range (996 words); nothing essential known to be missing. Possible additions after second-reader check: working with the 'flare' of primary teeth; exact Elements/Raypex frequencies.

## Revision history

| Date | Answer version / commit | Change | Audit action |
|---|---|---|---|
| 2026-11-09 | first draft | Drafted answer; second-reader pass added 15 locators | locators resolved; build_audit run |

## Final audit checklist

- [ ] Every factual author-year citation is supported by a verified source.
- [ ] Every numerical value has a traceable source.
- [ ] Chapter authors, edition, year and bibliographic details are verified or explicitly marked unknown.
- [ ] Disagreements between sources are represented accurately.
- [ ] Any [RECALL] or interpretive claim is not disguised as a sourced fact.
- [ ] The student-facing answer contains no retrieval report, source locator ledger or generation diagnostics.
- [ ] The reference list matches the in-text author-year citations.
