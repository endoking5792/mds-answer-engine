# Internal answer audit — Q02 Pain in and around the Oro-Facial Region (100m)

**Student-facing answer:** `canonical/Q02_Orofacial_Pain_100m_CANONICAL.md`

**Last updated:** 2026-11-10
**Audit owner:** drafting agent (Claude)

> Internal working record only. Do not publish this file to the student-facing Answer Bank.

## Retrieval record

- **Sources consulted:** Cohen's Pathways of the Pulp 12e (2021) Ch.4 (Law, Nixdorf, Mattscheck); Ingle's Endodontics 7e (2019) Ch.17 (Bernadette Jaeger per front matter; chapter heading OCR-garbled, verify against the printed book); Seltzer and Bender's Dental Pulp 2e (Hargreaves and Goodis, 2012) Ch.19 (Okeson); Torabinejad, Endodontics: Principles and Practice 6e (2021) Ch.5 (Eli, Said-Al-Naief, Torabinejad); Gulabivala and Ng, Endodontics 4e (2014) Ch.16 (Leeson, Gulabivala, Ng); Walton and Torabinejad 3e (2002) Part 29 and Part 4 (no chapter author named; editors cited); Sikri 2e (2019) Ch.3 and Ch.5; Grossman 14e (2021) Ch.4 (no chapter author named; editor Gopikrishna cited); Gutmann and Lovdahl 5e (2011) Ch.1; AAE Glossary of Endodontic Terms 8th ed (2012). Chapters read in full or in the relevant sections (Cohen, Ingle, Okeson, Torabinejad, Leeson, Walton Part 29 essentially in full; Sikri, Grossman, Gutmann, Walton Part 4, Glossary only the relevant passages). Not read: Gutmann Ch.6 (nonodontogenic pain), Ingle Ch.16 (rhinosinusitis), Seltzer Ch.8 pain pathways, Dentine Hypersensitivity and Operative/Dental Materials texts (a materials text mentions aerodontalgia only in passing).
- **Existing evidence reused:** none; locators_Q02.py is new.
- **New retrieval performed:** grep of all chapterwise books for barodontalgia/aerodontalgia/atypical odontalgia; chapter reads as above.
- **Live literature search:** no; textbooks only, per brief.
- **Limitations:** Ingle Ch.17 OCR is damaged (fi, ff, Th replaced by symbols) so locator phrases were chosen from clean stretches; author name taken from front matter, verify. Cohen Ch.4 and Seltzer Ch.19 have no printed page numbers in the files (PDF page cited). Walton Part 29 has no chapter author in the file. Seltzer city and editor list (Hargreaves and Goodis) taken from front matter; verify city of publication and any third editor against the printed book. Torabinejad 6e city and publisher assumed St Louis: Elsevier from front matter year (2021); verify.

## Source locator ledger

<!--LOC: q02_coh_def, q02_coh_neuro, q02_coh_cs, q02_coh_ps, q02_coh_hyper, q02_coh_het, q02_coh_ref, q02_coh_ceph, q02_coh_two, q02_coh_cfib, q02_coh_sens, q02_coh_conv, q02_coh_pdl, q02_coh_nonresp, q02_coh_five, q02_coh_tax, q02_coh_mfp, q02_coh_mfpmus, q02_coh_mfpdx, q02_coh_mfptx, q02_coh_sinus, q02_coh_sinref, q02_coh_sal, q02_coh_migdur, q02_coh_migqual, q02_coh_migtooth, q02_coh_tac, q02_coh_o2, q02_coh_ph, q02_coh_neurovasc_ep, q02_coh_tn, q02_coh_trig, q02_coh_tnla, q02_coh_tnms, q02_coh_tncbz, q02_coh_tnnsaid, q02_coh_ptn, q02_coh_neuroma, q02_coh_neuritis, q02_coh_sarg, q02_coh_neuropath, q02_coh_pdap, q02_coh_pdapcl, q02_coh_pdapmri, q02_coh_central, q02_coh_centtx, q02_coh_cardiac, q02_coh_angina, q02_coh_intracr, q02_coh_crani, q02_coh_img, q02_coh_gca, q02_coh_psy, q02_coh_psyrare, q02_coh_psyreferral, q02_coh_freq, q02_coh_mfp75, q02_coh_hist, q02_coh_unchg, q02_coh_prot, q02_coh_noagg, q02_coh_qual, q02_coh_elec, q02_coh_block, q02_coh_persist, q02_coh_tpi, q02_coh_neuro_exam, q02_coh_palp, q02_coh_sinpalp, q02_ing_ref, q02_ing_conv, q02_ing_rule, q02_ing_nv, q02_ing_mus, q02_ing_any, q02_ing_hist, q02_ing_tmj, q02_ing_tmjtx, q02_ing_tmjster, q02_ing_tmjpain, q02_ing_sinus, q02_ing_sinext, q02_ing_angina, q02_ing_er, q02_ing_mig3, q02_ing_migtx, q02_ing_clus, q02_ing_ph, q02_ing_hc, q02_ing_tactx, q02_ing_tn, q02_ing_tnu40, q02_ing_tnblock, q02_ing_tnimg, q02_ing_ptn61, q02_ing_ptn, q02_ing_tnrx, q02_ing_tnsurg, q02_ing_neuroma, q02_ing_neuromatx, q02_ing_rct, q02_ing_pttn, q02_ing_ao, q02_ing_ao3, q02_ing_aoexam, q02_ing_aola, q02_ing_aotx, q02_ing_mfp, q02_ing_mfpsym, q02_ing_mfptx, q02_ing_psy, q02_ing_gca, q02_sel_tooth, q02_sel_conv, q02_sel_cs, q02_sel_site, q02_sel_90, q02_sel_midline, q02_sel_r1, q02_sel_r2, q02_sel_r3, q02_sel_r4, q02_sel_numb, q02_sel_iabn, q02_sel_iabn88, q02_sel_fp, q02_sel_thermal, q02_sel_box2a, q02_sel_box3a, q02_sel_box3b, q02_sel_box3c, q02_sel_seven, q02_sel_mfp230, q02_sel_230, q02_sel_nopain, q02_sel_mfpmus, q02_sel_tpact, q02_sel_mfpkey, q02_sel_mfptx, q02_sel_sinus, q02_sel_sinlido, q02_sel_headdip, q02_sel_sinimg, q02_sel_sintx, q02_sel_baro, q02_sel_baro24, q02_sel_migtx, q02_sel_migproph, q02_sel_tnkey, q02_sel_tnla, q02_sel_tntooth, q02_sel_tn61, q02_sel_tnrx, q02_sel_tncns, q02_sel_gpn, q02_sel_neuritis, q02_sel_zoster, q02_sel_neuritistx, q02_sel_ao10, q02_sel_aofem, q02_sel_aodx, q02_sel_aoprof, q02_sel_aotca, q02_sel_aogaba, q02_sel_aocap, q02_sel_aostent, q02_tor_refer, q02_tor_5, q02_tor_62, q02_tor_epi, q02_tor_sleep, q02_tor_pdl, q02_tor_snoop, q02_tor_snoop2, q02_tor_msk, q02_tor_tmd, q02_tor_mfp, q02_tor_nv, q02_tor_psy, q02_tor_tn, q02_tor_tn48, q02_tor_tnsleep, q02_tor_gpn, q02_tor_ao, q02_tor_ao2, q02_tor_ao3, q02_tor_sinus, q02_tor_neopl, q02_tor_cervical, q02_tor_vasc, q02_tor_img, q02_tor_manage, q02_gul_ofp, q02_gul_chr, q02_gul_prev, q02_gul_struct, q02_gul_path, q02_gul_conv, q02_gul_sens, q02_gul_block, q02_gul_five, q02_gul_class, q02_gul_mech, q02_gul_t164, q02_gul_t164b, q02_gul_t163, q02_gul_resp, q02_gul_chronic12, q02_gul_pers, q02_wal_first, q02_wal_wrong, q02_wal_obs, q02_wal_mech, q02_wal_gate, q02_wal_exp, q02_wal_cs, q02_wal_hot, q02_wal_deep, q02_wal_midline, q02_wal_neuritis, q02_wal_head, q02_wal_mig, q02_wal_ao, q02_wal_aopsy, q02_wal_ao38, q02_wal_clue1, q02_wal_clue2, q02_wal_clue3, q02_wal_clue4, q02_wal_clue5, q02_wal_clue6, q02_glo_baro, q02_gro_baro, q02_gro_alt, q02_gro_note, q02_sik5_baro, q02_sik5_mech, q02_sik5_varn, q02_gut_baro, q02_gut_land, q02_gut_pass, q02_gut_dive, q02_gut_test, q02_gut_sym, q02_wal4_baro, q02_sik_het, q02_sik_cen, q02_sik_t32, q02_sik_t32b, q02_sik_peri, q02_sik_sial, q02_sel_1214, q02_ing_o2, q02_ing_tmjnsaid, q02_sik_proj, q02_coh_tn1530, q02_coh_clus, q02_coh_clusdur, q02_ing_clusdur, q02_ing_ambul, q02_gul_sial, q02_coh_gcaesr, q02_coh_gcatx, q02_coh_pdapage, q02_coh_neuromatime, q02_coh_stell, q02_sel_ptn, q02_ing_ptn4, q02_coh_ph2, q02_ing_dark, q02_ing_pace, q02_ing_triptan, q02_coh_trip, q02_coh_dentinc, q02_coh_intracran, q02_coh_background, q02_coh_prop, q02_coh_ipsi, q02_coh_tn50, q02_sel_gpn_site, q02_sel_gpn_swal, q02_sel_gpn_ianb, q02_sel_neuritis_on, q02_coh_neuroma_zone, q02_coh_neuroma_ref, q02_ing_pttn_causes, q02_sel_ao_shift, q02_sel_ao_norem, q02_sel_ao3, q02_coh_pdap_loc, q02_ing_reassure, q02_ing_contra, q02_sel_ao_multi, q02_sel_pregab, q02_coh_mdclinic, q02_ing_anginatrig, q02_coh_eyes, q02_coh_cancer, q02_tor_weight, q02_tor_snoop3, q02_coh_psyjump, q02_coh_psyanat, q02_coh_psyint, q02_gut_necro, q02_gro_5000, q02_glo_ppl, q02_gut_hours, q02_coh_body, q02_gul_thal, q02_ing_neither, q02_coh_refprov, q02_coh_refarrest, q02_sik_t32c, q02_ing_t171, q02_ing_t172, q02_ing_t173, q02_sel_box2b, q02_sel_box2c, q02_sel_box3d, q02_coh_taut, q02_sel_mfp2, q02_sel_mfp3, q02_sel_mfp4, q02_sel_mfp5, q02_sel_latent, q02_coh_relax, q02_ing_adj, q02_coh_gauge, q02_sel_purul, q02_sel_step, q02_sel_sin1, q02_sel_sin2, q02_sel_sin3, q02_sel_sin4, q02_sel_tca, q02_sel_ccb, q02_sel_bb, q02_sel_trig, q02_coh_opioid, q02_sel_tnrx2, q02_sik_lingering, q02_coh_graded, q02_ing_alcohol, q02_coh_migact, q02_coh_vas-->

<!--CHECK-->Checked by build_audit.py: LOC keys 345, missing 0; quotes not found 0; answer body 3408 words (calibration 3200-3500 for 100m); cited surnames not in references: none; body numbers without a locator: none.<!--/CHECK-->

The table below is generated by `python3 build_audit.py audit/<this file>`; do not edit it by hand.

<!--LEDGER START-->
| # | Source (in-text citation) | Chapter file | PDF page (printed page) | Verbatim locator phrase | Status |
|---|---|---|---|---|---|
| 1 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.508 | "An unpleasant sensory and emotional experience associated with actual or potential tissue damage or described in terms of such damage." | Verified |
| 2 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.508 | "Pain arising as a direct consequence of a lesion or disease affecting the somatosensory system." | Verified |
| 3 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.508 | "Increased responsiveness of nociceptive neurons in the central nervous system to their normal or subthreshold afferent input." | Verified |
| 4 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.508 | "Increased responsiveness and reduced thresholds of nociceptors to stimulation of their receptive fields." | Verified |
| 5 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.507 | "Two effects of central sensitization are secondary hyperalgesia and referred pain." | Verified |
| 6 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.509 | "There are three types of heterotopic pain: referred, central, and projected." | Verified |
| 7 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.509 | "Referred pain is felt in an area innervated by a nerve different from the one that mediates the primary pain." | Verified |
| 8 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.509 | "pain from mandibular molars typically is referred to maxillary molars" | Verified |
| 9 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.511 | "Only two structures serve as sources for primary odontogenic pain" | Verified |
| 10 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.511 | "Pulpal pain is mediated by C fibers and is dull, aching, or throbbing in nature." | Verified |
| 11 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.511 | "they will fire in response to the normal pulse pressure of cardiac contraction" | Verified |
| 12 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.512 | "The high degree of convergence from pulp tissue and the lack of proprioceptive information provided" | Verified |
| 13 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.512 | "Periradicular pain tends to be dull, aching, or throbbing and should resolve completely with local anesthesia." | Verified |
| 14 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.512 | "it is a strong indication that the pain may be nonodontogenic in origin" | Verified |
| 15 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.514 | "one can classify the nonodontogenic reasons for toothache into five broad groups of pain disorders" | Verified |
| 16 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.513 | "Consensus on the exact taxonomy with diagnostic criteria and their interrelationships among various orofacial pain disorders has not been established." | Verified |
| 17 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.514 | "Myofascial pain (MFP) emanates from small foci of hyperexcitable muscle tissue." | Verified |
| 18 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.515 | "Typically muscles that refer pain to teeth are the masseter, temporalis, and lateral pterygoid" | Verified |
| 19 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.515 | "Typically, local anesthetic infiltration into the trigger point(s) will resolve symptoms." | Verified |
| 20 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.515 | "Common therapeutic modalities used to treat MFP include deep massage, relaxation techniques" | Verified |
| 21 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.516 | "Sinus/nasal mucosal pain is another source of pain that can mimic toothache." | Verified |
| 22 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.516 | "Patients with suspected sinus/nasal mucosal disease should be referred to an otolaryngologist for further diagnosis and treatment." | Verified |
| 23 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.517 | "Because the primary somatosensory innervation of the major salivary glands comes from the mandibular branch" | Verified |
| 24 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.518 | "Migraine headaches typically last between 4 and 72 hours." | Verified |
| 25 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.518 | "They tend to be unilateral in presentation and pulsatile in quality" | Verified |
| 26 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.518 | "is likely the most common neurovascular disorder to do so" | Verified |
| 27 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.519 | "strictly unilateral pains defined by the concurrent presentation of at least one ipsilateral autonomic symptom" | Verified |
| 28 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.519 | "Elimination of pain after 10 minutes with inhalation of 100% oxygen is diagnostic for cluster headache" | Verified |
| 29 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.519 | "This headache disorder has a 100% response to indomethacin" | Verified |
| 30 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.519 | "neurovascular headaches tend to be episodic with complete remission between episodes" | Verified |
| 31 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.521 | "trigeminal neuralgia is characteristically an intense, sharp shooting pain that is most often unilateral" | Verified |
| 32 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.521 | "The area that elicits the pain is referred to as a trigger zone" | Verified |
| 33 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.521 | "anesthetizing the trigger zone may diminish symptoms" | Verified |
| 34 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.522 | "a person younger than 40 years of age who develops trigeminal neuralgia should also be screened for multiple sclerosis" | Verified |
| 35 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.522 | "Clinical trials support carbamazepine as a first-line drug for treating trigeminal neuralgia." | Verified |
| 36 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.522 | "Drugs aimed at relieving nociception, such as nonsteroidal antiinflammatory agents, have no significant benefit in these patients" | Verified |
| 37 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.522 | "respond to pharmacotherapy like classic trigeminal neuralgia" | Verified |
| 38 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.523 | "Tapping over the area of a neuroma elicits volleys of sharp electrical pain" | Verified |
| 39 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.526 | "Neuritic pain typically is a persistent, nonpulsatile burning often associated with sensory aberrations" | Verified |
| 40 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.525 | "overextension of a highly neurotoxic paraformaldehyde-containing paste" | Verified |
| 41 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.527 | "persistent dentoalveolar pain disorder" | Verified |
| 42 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.528 | "pain present at least 8 hours/day greater than or equal to 15 days or more per month for greater than or equal to 3 months" | Verified |
| 43 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.529 | "Typically, the examination is grossly unremarkable with no evidence of local tissue damage" | Verified |
| 44 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.531 | "brain imaging being routine prior to a diagnosis of PDAP being rendered" | Verified |
| 45 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.531 | "The most telling sign that a neuropathy has taken on a more central component is that local anesthetics are no longer effective." | Verified |
| 46 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.532 | "medications such as NMDA receptor agonists (ketamine), gabapentin, tricyclic antidepressants, and opioids" | Verified |
| 47 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.533 | "Cardiac pain has been cited as the cause of nonodontogenic toothache in a number of case reports." | Verified |
| 48 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.533 | "anginal pain may present solely as dental pain, generally felt in the lower left jaw" | Verified |
| 49 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.534 | "Space-occupying lesions within and around the brain are known to impinge on structures innervated with somatosensory fibers" | Verified |
| 50 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.534 | "a common feature is sensory loss along the distribution of the nerve" | Verified |
| 51 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.535 | "This underscores the need for regional imaging techniques, such as pantomography or CT" | Verified |
| 52 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.535 | "pulseless, indurated temporal arteries that are painful to palpation" | Verified |
| 53 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.537 | "The diagnosis of psychogenic toothache is one of exclusion" | Verified |
| 54 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.537 | "It is important to emphasize that psychogenic pain is rare." | Verified |
| 55 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.537 | "Early identification of psychogenic pain and referral to a psychologist or psychiatrist is necessary" | Verified |
| 56 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.537 | "pain is thought to be present in 5.3% of patients 6 or more months following treatment" | Verified |
| 57 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.538 | "The most common diagnosis of nonodontogenic pain in this small number of patients" | Verified |
| 58 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.538 | "it is the clinician’s examination that will reveal the true source of their pain" | Verified |
| 59 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.542 | "Static pain that does not change over time is typically not odontogenic in origin." | Verified |
| 60 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.542 | "is highly suggestive of a nonodontogenic pain source" | Verified |
| 61 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.543 | "The lack of any aggravating factors indicates that the pain is not of odontogenic origin." | Verified |
| 62 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.542 | "limit true odontogenic pain to having qualities that are dull, aching, or throbbing" | Verified |
| 63 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.543 | "which would indicate neuralgia" | Verified |
| 64 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.545 | "primary pain should not only be provoked by local manipulation but also be relieved by anesthetic blocking" | Verified |
| 65 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.546 | "Pain that persists after the onset of usual signs of anesthesia suggests a central component." | Verified |
| 66 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.547 | "a minimally myotoxic anesthetic such as 2% lidocaine or 3% mepivacaine without a vasoconstrictor" | Verified |
| 67 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.548 | "A neurologic screening examination, including a gross sensory and motor evaluation of cranial nerves II through" | Verified |
| 68 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.545 | "The temporalis, deep and superficial masseter, medial pterygoid, and digastric muscles should be palpated" | Verified |
| 69 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.545 | "pain of sinus origin may be provoked with a lowering of the patient’s head" | Verified |
| 70 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.403 (printed p.455) | "Referred pain is dependent on the primary pain source and will cease if this source is eliminated." | Verified |
| 71 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.403 (printed p.455) | "most popular theories are convergence-projection and convergence-facilitation" | Verified |
| 72 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.405 (printed p.457) | "local disease of the extracranial or intracranial structures must be ruled out" | Verified |
| 73 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.406 (printed p.458) | "neuro-vascular pain, such as migraine, generally has a throbbing, pulsing, or pounding quality" | Verified |
| 74 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.406 (printed p.458) | "muscle pain is usually deep, steady, and aching or produces a sensation of tightness or pressure" | Verified |
| 75 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.406 (printed p.458) | "extracranial or intracranial diseases may present with any quality of pain" | Verified |
| 76 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.405 (printed p.457) | "Of primary importance is a careful and exhaustive history." | Verified |
| 77 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.409 (printed p.461) | "chief symptom is continuous pain over the joint, aggravated by function" | Verified |
| 78 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.411 (printed p.463) | "construction of a stabilization splint may help reduce symptoms" | Verified |
| 79 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.411 (printed p.463) | "no more than two in 12 months, and two or three in a lifetime" | Verified |
| 80 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.409 (printed p.461) | "involve an abnormal or restricted range of motion and noise but are relatively painless" | Verified |
| 81 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.409 (printed p.461) | "most common extraoral source of dental pain arises from the maxillary sinus" | Verified |
| 82 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.409 (printed p.461) | "Many teeth have been mistakenly extracted because of an incorrect diagnosis of this syndrome." | Verified |
| 83 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.411 (printed p.463) | "Angina attacks are usually short-lasting, rarely longer than" | Verified |
| 84 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.412 (printed p.464) | "the patient must be referred to an emergency room immediately" | Verified |
| 85 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.414 (printed p.466) | "about 3% of migraine patients will complain of intraoral pain" | Verified |
| 86 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.418 (printed p.470) | "Oxygen inhalation (100% 7–8 L/min with a nonrebreathing mask)" | Verified |
| 87 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.416 (printed p.468) | "Because of the oral symptoms, serious diagnostic errors are committed by dentists." | Verified |
| 88 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.417 (printed p.469) | "Paroxysmal hemicrania is completely responsive to indomethacin." | Verified |
| 89 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.417 (printed p.469) | "strictly unilateral and completely responsive to indomethacin" | Verified |
| 90 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.417 (printed p.469) | "best left to the orofacial pain dentist or other health care providers" | Verified |
| 91 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.419 (printed p.471) | "dentists are commonly the first ones to see these patients" | Verified |
| 92 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.419 (printed p.471) | "Anyone under the age of 40 with this disorder should be referred to a neurologist" | Verified |
| 93 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.419 (printed p.471) | "Neural blockade of the trigger area almost always relieves the pain for the duration of action of the local anesthetic." | Verified |
| 94 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.421 (printed p.473) | "all patients with trigeminal neuralgia-like symptoms should be worked up with an imaging study of the head" | Verified |
| 95 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.420 (printed p.472) | "61% of the cases with PTN or trigeminal neuralgia were incorrectly diagnosed and treated for dental conditions" | Verified |
| 96 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.419 (printed p.471) | "Patients may present themselves up to 2 years before developing trigeminal neuralgia" | Verified |
| 97 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.421 (printed p.473) | "Lamotrigine and baclofen (Lioresal) are the next most" | Verified |
| 98 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.421 (printed p.473) | "gamma knife, radiosurgery, percutaneous rhizotomies, and microvascular decompression" | Verified |
| 99 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.421 (printed p.473) | "neuromas most commonly develop in the area of the mental foramen, followed by the lower lip, tongue, and buccal mucosa" | Verified |
| 100 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.422 (printed p.474) | "neuroma excision and other peripheral neuroablative procedures provide" | Verified |
| 101 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.424 (printed p.476) | "Root canal treatment is accompanied by about a 3–13% incidence of persistent pain." | Verified |
| 102 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.424 (printed p.476) | "best treatment for traumatic trigeminal neuropathies is prevention" | Verified |
| 103 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.430 (printed p.482) | "It is extremely important for dentists to be aware of the existence of this disorder to avoid performing unnecessary dental procedures and extractions." | Verified |
| 104 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.430 (printed p.482) | "as many as 3% to >7% of endodontic patients may" | Verified |
| 105 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.430 (printed p.482) | "Intraoral and radiographic examinations are typically unrevealing." | Verified |
| 106 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.430 (printed p.482) | "majority of patients report little or no relief with diagnostic local anesthetic blocks" | Verified |
| 107 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.432 (printed p.484) | "treatment of choice is the use of tricyclic antidepressant agents such as amitriptyline or imipramine" | Verified |
| 108 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.425 (printed p.477) | "MFP, a regional referred pain syndrome associated with focally tender TrPs in muscle" | Verified |
| 109 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.425 (printed p.477) | "the presenting pain complaint is usually a referred symptom with a deep, dull aching quality" | Verified |
| 110 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.428 (printed p.480) | "causal and perpetuating factors, patient education" | Verified |
| 111 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.407 (printed p.459) | "it is rare for pain to be purely due to a psychological disorder" | Verified |
| 112 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.418 (printed p.470) | "emergency ophthalmological examination is essential without delay" | Verified |
| 113 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.799 | "toothache represents the most prevalent form of orofacial pain" | Verified |
| 114 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.801 | "about 50% of all pulpal neurons converge with other neurons on the same trigeminal projection neurons" | Verified |
| 115 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.801 | "This phenomenon, known as central sensitization" | Verified |
| 116 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.800 | "the site at which the patient perceives the pain (the tooth) is different from the source of the pain" | Verified |
| 117 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.801 | "about 90% of all patients reporting moderate to severe odontogenic pain" | Verified |
| 118 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.803 | "Referred pain does not generally cross the midline." | Verified |
| 119 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.803 | "Local stimulation of the site of pain does not increase the pain." | Verified |
| 120 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.803 | "Local stimulation of the source of pain increases the pain at both the source and the site of pain." | Verified |
| 121 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.803 | "Local anesthetic blocking of the site of pain does not decrease the pain." | Verified |
| 122 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.803 | "Local anesthetic blocking of the source of pain decreases the pain at both the source and the site of pain." | Verified |
| 123 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.805 | "I know you are numb, but does it still hurt?" | Verified |
| 124 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.806 | "successful anesthesia in only about 38% of patients" | Verified |
| 125 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.806 | "improves to 88% when the inferior alveolar nerve block is combined with intraosseous supplemental injection" | Verified |
| 126 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.806 | "positive results are possible. Thus, the local anesthetic test must be considered in the context of the other findings" | Verified |
| 127 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.804 | "thermal allodynia of the suspect tooth is a hallmark feature of pulpitis" | Verified |
| 128 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.807 | "Presence of etiologic factors for an odontogenic origin of pain" | Verified |
| 129 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.808 | "Absence of apparent etiologic factors for odontogenic pain" | Verified |
| 130 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.808 | "No consistent relief of pain provided by local anesthetic injection" | Verified |
| 131 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.808 | "Bilateral pain or multiple painful teeth" | Verified |
| 132 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.808 | "They are myofascial toothache, sinus toothache, neurovascular toothache, neuropathic toothache, cardiac toothache, somatoform toothache, and toothache of systemic origin." | Verified |
| 133 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.810 | "85.0% demonstrated referred pain with palpation of muscles or trigger points, and 11.6% of these patients had pain referred to the teeth" | Verified |
| 134 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.810 | "In a series of 230 cases of patients with a diagnosis of temporomandibular dysfunction" | Verified |
| 135 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.822 | "No pain between episodes is reported." | Verified |
| 136 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.810 | "the anterior digastric (to the mandibular anterior teeth)" | Verified |
| 137 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.810 | "In the active state, it produces central excitatory effects." | Verified |
| 138 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.811 | "The pain is relatively constant, dull, aching, and nonpulsatile." | Verified |
| 139 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.813 | "identification and elimination of contributory factors, mild analgesics, spray and stretch therapy, deep massage, biofeedback, deep heat, and injection of the trigger points" | Verified |
| 140 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.814 | "A particularly distinguishing characteristic is the presentation of multiple maxillary posterior teeth with percussion sensitivity and a positive response to pulpal vitality testing." | Verified |
| 141 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.814 | "Reduction of pain after the intranasal application of a 4% lidocaine spray is considered diagnostic." | Verified |
| 142 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.814 | "a positive “head-dip” test is observed" | Verified |
| 143 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.814 | "Radiographic imaging of the sinuses, particularly a Waters view or computed tomographic scan, may reveal fluid accumulation." | Verified |
| 144 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.814 | "Bacterial sinusitis is often treated with" | Verified |
| 145 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.815 | "Pain in the maxillary sinuses as well as in the maxillary and mandibular teeth also can be triggered by reduced atmospheric pressure." | Verified |
| 146 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.815 | "root canal obturations, be completed more than 24 hours prior to exposure to reduced atmospheric pressure" | Verified |
| 147 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.817 | "Infrequent attacks are managed with abortive medications such as the triptans" | Verified |
| 148 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.817 | "When attacks are more frequent (one or more a week), prophylactic medications are used" | Verified |
| 149 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.822 | "The pain episodes are brief, lasting only 5 to 10 seconds." | Verified |
| 150 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.822 | "A local anesthetic injection at the trigger zone (or a nerve block) will eliminate the episodes of paroxysmal pain" | Verified |
| 151 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.822 | "Very localized anesthesia of the tooth (interliga-mentous injection) will not reduce the pain unless it is also the trigger zone." | Verified |
| 152 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.821 | "a total of 61% of patients reported an initial dental pain" | Verified |
| 153 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.822 | "Medications include carbamazepine" | Verified |
| 154 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.822 | "About 2% of paroxysmal neuralgias are caused by central pathologic lesions." | Verified |
| 155 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.822 | "Glossopharyngeal neuralgia is only about one-tenth as prevalent as trigeminal neuralgia." | Verified |
| 156 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.825 | "The pain is a persistent, nonpulsatile, often burning pain felt in a tooth." | Verified |
| 157 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.824 | "Herpes zoster has been reported to produce nonodontogenic dental pain preceding the eruption of vesicles." | Verified |
| 158 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.825 | "antiviral medications such as acyclovir, valacyclovir, or famciclovir can be helpful" | Verified |
| 159 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.825 | "atypical odontalgia has been estimated to be 10 times more prevalent than trigeminal neuralgia" | Verified |
| 160 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.826 | "of 42 patients with atypical odontalgia, 86% of the patient population was female, and 78% reported maxillary pain" | Verified |
| 161 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.826 | "pain that often lasts more than 4 months; and pain that is not altered by intraoral thermal stimuli" | Verified |
| 162 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.826 | "The patient is usually a middle-aged woman with a history of trauma to the painful region." | Verified |
| 163 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.827 | "Dosages ranging from 10 to 100 mg seem to be adequate for pain relief" | Verified |
| 164 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.827 | "Gabapentin may be slowly titrated until pain is reduced or a maximum dosage of 3,600 mg is reached." | Verified |
| 165 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.827 | "Capsaicin ointment should be applied to the painful area 4 times a day for 3 to 4 weeks." | Verified |
| 166 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.827 | "a thin acrylic resin stent can be fabricated to retain the medication on the painful site" | Verified |
| 167 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.91 (printed p.84) | "Referral to one of these specialists is preferable to sending a patient to an urgent care facility or an emergency room." | Verified |
| 168 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.91 (printed p.84) | "The frequency of continuing pain after endodontic treatment has been reported at 5%." | Verified |
| 169 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.91 (printed p.84) | "Of these patients, 62% were found to be a pain of nonodontogenic origin." | Verified |
| 170 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.91 (printed p.84) | "the frequency of orofacial pain in the general adult population as ranging from 14% to 40%" | Verified |
| 171 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.92 (printed p.85) | "Pain of dental origin will often awaken a patient from sleep or prevent sleep." | Verified |
| 172 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.92 (printed p.85) | "Periodontal ligament pain is generally a dull, aching pain in and around the teeth and can affect multiple teeth." | Verified |
| 173 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.92 (printed p.85) | "The SNOOP acronym can be helpful to determine level of concern" | Verified |
| 174 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.92 (printed p.85) | "Onset after age 40 years: vascular (temporal arteritis), tumor, infection" | Verified |
| 175 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.93 (printed p.86) | "Musculoskeletal conditions are the major cause of nonodontogenic pain in the orofacial region." | Verified |
| 176 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.93 (printed p.86) | "Noise in the TM joint that presents without pain, catching, locking, or sudden and notable change in bite position" | Verified |
| 177 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.93 (printed p.86) | "Myofascial pain is the most common muscle pain disorder of the orofacial region." | Verified |
| 178 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.93 (printed p.86) | "a medication trial can help clarify the diagnosis" | Verified |
| 179 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.93 (printed p.86) | "psychological factors have not been established as a cause of toothaches of nondental origin" | Verified |
| 180 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.94 (printed p.87) | "it is common for patients to have consulted with an endodontist" | Verified |
| 181 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.94 (printed p.87) | "most neuralgias are disabled for 4 to 8 weeks by dental procedures such as endodontic treatment and oral surgery" | Verified |
| 182 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.93 (printed p.86) | "they do not often awaken the sleeping patient" | Verified |
| 183 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.94 (printed p.87) | "Aggressive imaging of the region is recommended because of the high likelihood of regional lesion or pathology" | Verified |
| 184 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.94 (printed p.87) | "Duration longer than 4 months" | Verified |
| 185 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.94 (printed p.87) | "Normal radiographic examination" | Verified |
| 186 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.94 (printed p.87) | "Confirmation is associated with positive sympathetic nerve block." | Verified |
| 187 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.94 (printed p.87) | "application of topical anesthesia to the offending area should eliminate the pain" | Verified |
| 188 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.95 (printed p.88) | "The tooth symptoms are generally accompanied by other nerves malfunctioning or by systemic symptoms" | Verified |
| 189 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.94 (printed p.87) | "Careful assessment, history, and clinical examination, including the cervical spine, are paramount" | Verified |
| 190 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.94 (printed p.87) | "Carotidynia and temporal arteritis are two such disorders" | Verified |
| 191 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.92 (printed p.85) | "a dental provider should access the images and review them personally" | Verified |
| 192 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.95 (printed p.88) | "a management strategy is employed, with the focus being on improving quality of life and decreasing unnecessary treatment" | Verified |
| 193 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.378 (printed p.369) | "Orofacial pain (OFP) is defined as pain whose origin is below the orbitomeatal line, above the neck and anterior to the ears" | Verified |
| 194 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.378 (printed p.369) | "pain in the face, mouth or jaws that has been present intermittently or continuously for 3 months or longer" | Verified |
| 195 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.378 (printed p.369) | "it is estimated that a quarter of the adult population have suffered from orofacial pain" | Verified |
| 196 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.378 (printed p.369) | "teeth, periodontium, oral mucosa, temporomandibular joints (TMJ) and associated musculature, cervical spine and associated musculature, maxillary sinuses, nose, eyes, throat, salivary glands" | Verified |
| 197 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.378 (printed p.369) | "which project to the nucleus caudalis in the medulla" | Verified |
| 198 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.378 (printed p.369) | "Convergence to the nucleus caudalis accounts for poor localization, spread and referral of pain" | Verified |
| 199 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.378 (printed p.369) | "enlargement of the receptive field, decreased activation threshold, wind" | Verified |
| 200 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.378 (printed p.369) | "can reduce nociceptive input and potentially prevent the development of central sensitization" | Verified |
| 201 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.379 (printed p.370) | "classified into inflammatory, vascular, musculoskeletal, neuropathic and idiopathic" | Verified |
| 202 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.378 (printed p.369) | "Numerous classification systems based on the structures, symptoms or treatment" | Verified |
| 203 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.380 (printed p.371) | "maladaptive neuropathic and functional pains" | Verified |
| 204 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.380 (printed p.371) | "Months or years Variable 30 minutes to 72 hours 4–72 hours 15–180 minutes Brief; seconds" | Verified |
| 205 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.380 (printed p.371) | "Mild to moderate Mild to moderate Mild to moderate Moderate to severe Severe Severe" | Verified |
| 206 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.379 (printed p.370) | "Throbbing, pounding, pulsating, sometimes stabbing" | Verified |
| 207 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.381 (printed p.372) | "The responsibility lies with the endodontist to exclude pain of dental and endodontic origin and then to refer appropriately" | Verified |
| 208 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.378 (printed p.369) | "about 12% may have some form of chronic pain" | Verified |
| 209 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.380 (printed p.371) | "the pain may be non" | Verified |
| 210 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.542 (printed p.521) | "it is imperative to establish first whether pain is of dental origin" | Verified |
| 211 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.542 (printed p.521) | "Difficulties in the localization of pain may result in extraction or endodontic treatment of the wrong tooth." | Verified |
| 212 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.542 (printed p.521) | "One is to provide symptomatic relief and to observe the patient." | Verified |
| 213 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.543 (printed p.522) | "Differential diagnosis must be based on an understanding of pain mechanisms." | Verified |
| 214 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.544 (printed p.523) | "Large fiber activity tends to close the gate, whereas small fiber activity opens the gate." | Verified |
| 215 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.545 (printed p.524) | "pain is not a simple sensation such as touch, heat, or taste but an" | Verified |
| 216 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.545 (printed p.524) | "a phenomenon known as central sensitization or" | Verified |
| 217 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.545 (printed p.524) | "in which a tooth with longstanding, intense pulpitis is difficult to anesthetize may be the result of this effect" | Verified |
| 218 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.545 (printed p.524) | "Pulpal pain may be considered deep (visceral). Periradicular pain is superficial (peripheral)." | Verified |
| 219 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.546 (printed p.525) | "it may spread to the ear, temple, cheek, or other teeth, although never across the midline" | Verified |
| 220 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.550 (printed p.529) | "Neuritis is best distinguished from pain originating from the teeth by the history" | Verified |
| 221 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.549 (printed p.528) | "Headaches are the most common painful entities of the head and neck" | Verified |
| 222 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.549 (printed p.528) | "These may be referred to the teeth (commonly the maxillary canine teeth and premolars)" | Verified |
| 223 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.550 (printed p.529) | "Their most consistent characteristic is chronic pain of a steady intensity" | Verified |
| 224 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.550 (printed p.529) | "The etiology is unknown but a psychiatric basis is strongly suspected." | Verified |
| 225 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.550 (printed p.529) | "a 22-year-old woman underwent 38 separate root canal treatments" | Verified |
| 226 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.551 (printed p.530) | "Pain is commonly referred to the most recently treated tooth or teeth." | Verified |
| 227 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.551 (printed p.530) | "Stimulating the site of perceived pain neither initiates nor worsens pain that has been referred from another source." | Verified |
| 228 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.551 (printed p.530) | "Anesthetizing the true origin of the pain eliminates the pain." | Verified |
| 229 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.551 (printed p.530) | "Dental pains are extremely versatile and have the propensity to simulate nearly any pain syndrome." | Verified |
| 230 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.551 (printed p.530) | "Selective infiltration anesthesia should be conducted on maxillary teeth beginning with the anterior teeth" | Verified |
| 231 | Walton and Torabinejad, 2002 | 29_Part_29_Differential_Diagnosis_of_Orofacial_Pai | PDF p.551 (printed p.530) | "Stress and insomnia are correlated with bruxism and myofascial pain syndromes." | Verified |
| 232 | American Association of Endodontists, 2012 | 00_Pages_1_30.md | PDF p.7 | "Tooth pain caused by an increase or decrease in ambient pressure" | Verified |
| 233 | Gopikrishna, 2021 | 04_Chapter_4_Diseases_of_the_Dental_Pulp.md | PDF p.80 | "denotes toothache occurring at low atmospheric pressure experienced either during flight or during a test run in a decompression chamber" | Verified |
| 234 | Gopikrishna, 2021 | 04_Chapter_4_Diseases_of_the_Dental_Pulp.md | PDF p.80 | "it is more likely to occur at 10,000 feet or above" | Verified |
| 235 | Gopikrishna, 2021 | 04_Chapter_4_Diseases_of_the_Dental_Pulp.md | PDF p.80 | "A tooth with irreversible pulpitis can be symptomless at the ground level, but it may cause pain at high altitude because of reduced pressure." | Verified |
| 236 | Sikri, 2019 | 05_5_Diseases_of_Dental_Pulp.md | PDF p.71 | "The pain experienced by a patient in a recently restored tooth during low atmospheric pressure usually at high altitude is called Barodontalgia (aerodontalgia)." | Verified |
| 237 | Sikri, 2019 | 05_5_Diseases_of_Dental_Pulp.md | PDF p.71 | "it may be related to pulpal hyperaemia or to the gases which are trapped in the teeth following root canal treatment" | Verified |
| 238 | Sikri, 2019 | 05_5_Diseases_of_Dental_Pulp.md | PDF p.71 | "Giving a layer of cavity varnish or liner under the restoration helps to prevent this problem." | Verified |
| 239 | Gutmann and Lovdahl, 2011 | 01_Chapter_1_Problem_Solving_in_the_Diagnosis_of_O | PDF p.30 | "exhibit the unusual symptom of spontaneous pain that occurs when there is a significant change in atmospheric pressure" | Verified |
| 240 | Gutmann and Lovdahl, 2011 | 01_Chapter_1_Problem_Solving_in_the_Diagnosis_of_O | PDF p.30 | "The pain may subside or be eliminated by reducing altitude or on landing" | Verified |
| 241 | Gutmann and Lovdahl, 2011 | 01_Chapter_1_Problem_Solving_in_the_Diagnosis_of_O | PDF p.30 | "driving over mountain passes where the altitude change may only be on the magnitude of 5000 to 7000 feet" | Verified |
| 242 | Gutmann and Lovdahl, 2011 | 01_Chapter_1_Problem_Solving_in_the_Diagnosis_of_O | PDF p.30 | "People in deep underwater diving conditions have also experienced these symptoms (barodontalgia)." | Verified |
| 243 | Gutmann and Lovdahl, 2011 | 01_Chapter_1_Problem_Solving_in_the_Diagnosis_of_O | PDF p.30 | "thermal testing is usually the most effective means to localize the offending tooth" | Verified |
| 244 | Gutmann and Lovdahl, 2011 | 01_Chapter_1_Problem_Solving_in_the_Diagnosis_of_O | PDF p.30 | "When patients present for dental treatment, they are often symptom free." | Verified |
| 245 | Walton and Torabinejad, 2002 | 04_Part_4_Diagnosis_and_Treatment_Planning.md | PDF p.66 | "tooth-related pain experienced with changes in ambient pressure" | Verified |
| 246 | Sikri, 2019 | 03_3_Pathophysiology_of_Pain.md | PDF p.47 (printed p.26) | "Heterotopic pain: The site and source of pain are different." | Verified |
| 247 | Sikri, 2019 | 03_3_Pathophysiology_of_Pain.md | PDF p.47 (printed p.26) | "Central pain: Pain derived from the central nervous" | Verified |
| 248 | Sikri, 2019 | 03_3_Pathophysiology_of_Pain.md | PDF p.47 (printed p.26) | "Cluster headache Severe ache (episodic) Rapid eye movement (REM)" | Verified |
| 249 | Sikri, 2019 | 03_3_Pathophysiology_of_Pain.md | PDF p.47 (printed p.26) | "Trigeminal neuralgia Lancinating (episodic) Light touch triggers pain Few seconds" | Verified |
| 250 | Sikri, 2019 | 03_3_Pathophysiology_of_Pain.md | PDF p.47 (printed p.26) | "Acute pericoronitis involves bacterial infection around semierupted mandibular third molar." | Verified |
| 251 | Sikri, 2019 | 03_3_Pathophysiology_of_Pain.md | PDF p.47 (printed p.26) | "Sialolithiasis Sharp pain (episodic) Biting induce pain" | Verified |
| 252 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.799 | "about 12% to 14% of the population reporting a history of a toothache over a 6-month period" | Verified |
| 253 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.418 (printed p.470) | "given at the very beginning of an attack for 15 minutes" | Verified |
| 254 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.410 (printed p.462) | "jaw rest, a soft diet, and 7–14 days of nonsteroidal anti-inflammatory drug (NSAID) use" | Verified |
| 255 | Sikri, 2019 | 03_3_Pathophysiology_of_Pain.md | PDF p.47 (printed p.26) | "Projected pain: Pain felt in peripheral distribution" | Verified |
| 256 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.522 | "suggested 15% to 30% of patients have secondary reasons for their pain" | Verified |
| 257 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.519 | "occurring in men three to four times more often than in women" | Verified |
| 258 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.519 | "with pain episodes lasting between 15 minutes and 2 hours" | Verified |
| 259 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.416 (printed p.468) | "15- to 180-minute attacks per day" | Verified |
| 260 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.412 (printed p.464) | "transported by emergency services personnel and not allowed to drive" | Verified |
| 261 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.379 (printed p.370) | "Sialadenitis or blockage of salivary glands can cause swelling or pain on swallowing" | Verified |
| 262 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.535 | "A laboratory finding of an elevated erythrocyte sedimentation rate (ESR) is suggestive of the disorder, and diagnosis is confirmed by temporal artery biopsy." | Verified |
| 263 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.535 | "Treatment includes administration of corticosteroids" | Verified |
| 264 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.531 | "In the orofacial region, neuropathies are most commonly seen in the maxillary premolar area and molar region." | Verified |
| 265 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.523 | "typically about 10 days after the event" | Verified |
| 266 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.548 | "a stellate ganglion block can be used to provide diagnostic insight" | Verified |
| 267 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.821 | "Instead of paroxysmal pain, the pain is an aching pain in the sinus region and teeth" | Verified |
| 268 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.419 (printed p.471) | "may describe this pain as dull, aching, and/or burning" | Verified |
| 269 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.519 | "with a frequency of more than five per day and a duration lasting 2 to 30 minutes" | Verified |
| 270 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.416 (printed p.468) | "migraine patients who typically retreat to a dark room to sleep" | Verified |
| 271 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.416 (printed p.468) | "headache patients typically pace the" | Verified |
| 272 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.418 (printed p.470) | "symptomatic use of subcutaneous or intranasal triptans" | Verified |
| 273 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.518 | "triptans, such as sumatriptan and rizatriptan" | Verified |
| 274 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.517 | "dental disease and treatments are not likely to be a cause of a person developing a headache disorder" | Verified |
| 275 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.517 | "intracranial branches of the trigeminal nerve become sensitized" | Verified |
| 276 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.519 | "whereas toothache pain usually has at least some background pain" | Verified |
| 277 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.521 | "the response to the stimulus is not proportional to the intensity of the stimulus" | Verified |
| 278 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.521 | "but is always ipsilateral" | Verified |
| 279 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.522 | "Trigeminal neuralgia typically presents in individuals older than 50 years of age." | Verified |
| 280 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.823 | "The distribution of pain includes the posterior mandible, oropharynx, tonsillar fossa, and ear." | Verified |
| 281 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.823 | "The pain is often elicited by swallowing" | Verified |
| 282 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.823 | "Inferior alveolar nerve block does not change the pain condition." | Verified |
| 283 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.825 | "The onset of the toothache followed an infection or trauma" | Verified |
| 284 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.523 | "there should be a zone of anesthesia peripheral to the area of the neuroma" | Verified |
| 285 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.523 | "early recognition and referral are of key importance" | Verified |
| 286 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.424 (printed p.476) | "dental implants, third molar extractions, nerve blocks and root canal therapy" | Verified |
| 287 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.826 | "The pain location may change over time but usually remains in the same nerve distribution." | Verified |
| 288 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.826 | "There are no periods of remission." | Verified |
| 289 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.825 | "may include up to 3% of patients receiving" | Verified |
| 290 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.528 | "Localized (3) in the dentoalveolar region(s), and; C. Not caused by another disease or disorder" | Verified |
| 291 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.432 (printed p.484) | "Patients may need reassurance that the pain is real and not psychogenic" | Verified |
| 292 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.432 (printed p.484) | "occlusal adjustments, are contraindicated" | Verified |
| 293 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.826 | "It is not unusual for patients with atypical odontalgia to have received multiple endodontic procedures or extractions" | Verified |
| 294 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.827 | "Pregabalin can be slowly titrated up to 300 mg/day" | Verified |
| 295 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.532 | "sometimes is best performed in a multidisciplinary chronic pain clinic facility" | Verified |
| 296 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.411 (printed p.463) | "Precipitating factors include exertion and emotional excitement" | Verified |
| 297 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.535 | "history of eyesight changes, such as blurred vision" | Verified |
| 298 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.535 | "This is especially true in patients who have a history of cancer." | Verified |
| 299 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.95 (printed p.88) | "such as weight loss, fatigue" | Verified |
| 300 | Eli, Said-Al-Naief and Torabinejad, 2021 | 05_5_Differential_Diagnosis_of_Pains_and_Radioluce | PDF p.92 (printed p.85) | "Pattern change: any new or changed headache pattern" | Verified |
| 301 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.537 | "The pain may be felt in multiple teeth and may jump around from one tooth to another." | Verified |
| 302 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.537 | "they may not fit normal anatomic distributions or physiologically plausible patterns" | Verified |
| 303 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.537 | "The intensity of pain reported tends to be more severe than is reflected by the patient’s level of concern about the condition." | Verified |
| 304 | Gutmann and Lovdahl, 2011 | 01_Chapter_1_Problem_Solving_in_the_Diagnosis_of_O | PDF p.30 | "significant pulpal degeneration or pulpal necrosis" | Verified |
| 305 | Gopikrishna, 2021 | 04_Chapter_4_Diseases_of_the_Dental_Pulp.md | PDF p.80 | "It has generally been observed in altitudes over 5,000 feet" | Verified |
| 306 | American Association of Endodontists, 2012 | 00_Pages_1_30.md | PDF p.7 | "usually reported by aircraft personnel and divers" | Verified |
| 307 | Gutmann and Lovdahl, 2011 | 01_Chapter_1_Problem_Solving_in_the_Diagnosis_of_O | PDF p.30 | "in some cases the pain may continue for several hours" | Verified |
| 308 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.511 | "as low a temperature threshold as body temperature" | Verified |
| 309 | Leeson, Gulabivala and Ng, 2014 | 16_16_The_orofacial_pain_endo_interface.md | PDF p.378 (printed p.369) | "then project via the spinothalamic tract to the thalamus and thence to the cerebral cortex" | Verified |
| 310 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.403 (printed p.455) | "Neither theory is considered complete" | Verified |
| 311 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.509 | "Referred pain cannot be provoked by stimulation of the area where the pain is felt" | Verified |
| 312 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.509 | "referred pain cannot be arrested unless the primary source of pain is anesthetized" | Verified |
| 313 | Sikri, 2019 | 03_3_Pathophysiology_of_Pain.md | PDF p.47 (printed p.26) | "Rapid eye movement (REM) 30–45 minutes sleep, alcohol" | Verified |
| 314 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.405 (printed p.457) | "Local disease of extracranial structures Craniofacial organs Any Intracranial disease Brain and related structures Any Referred pain from remote sites Distant structures Aching, pressing" | Verified |
| 315 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.405 (printed p.457) | "Neurovascular Blood vessels Throbbing Neuropathic Sensory nervous system Shooting, sharp, burning" | Verified |
| 316 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.405 (printed p.457) | "Sympathetic nervous system Burning Muscular Muscles Deep aching, tight Idiopathic Etiology as yet unknown Deep aching, burning" | Verified |
| 317 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.807 | "Ability to reproduce chief complaint during examination" | Verified |
| 318 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.807 | "Relief of pain provided by local anesthetic injection" | Verified |
| 319 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.808 | "Pain qualities: burning, electric shooting, stabbing, dull ache" | Verified |
| 320 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.514 | "Clinically these areas feel like taut bands or knots and are termed trigger points." | Verified |
| 321 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.811 | "Palpation and stimulation of the trigger points increase the toothache." | Verified |
| 322 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.811 | "Confirmed anesthesia of the tooth does not alter the toothache." | Verified |
| 323 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.811 | "Local anesthetic injection of the involved muscle (trigger points) reduces the toothache." | Verified |
| 324 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.811 | "The toothache is increased with function of the involved muscle (trigger points)." | Verified |
| 325 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.810 | "the history is the only data that leads the clinician to make the diagnosis of myofascial pain" | Verified |
| 326 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.515 | "muscle relaxants, and trigger point injections" | Verified |
| 327 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.428 (printed p.480) | "voluntary contract release, TrP pressure release, and TrP injections are useful adjunctive" | Verified |
| 328 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.547 | "performed with either a 27- or a 25-gauge needle" | Verified |
| 329 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.814 | "patients may report a purulent nasal discharge" | Verified |
| 330 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.814 | "The toothache is increased when the patient steps hard on to the heel of the foot" | Verified |
| 331 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.814 | "The patient reports pressure felt below the eyes." | Verified |
| 332 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.814 | "The pain is increased when pressure is applied over the involved sinus." | Verified |
| 333 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.813 | "pain that may be partially relieved by a diagnostic intraoral local anesthetic block" | Verified |
| 334 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.815 | "sinusitis is often treated with antihistamines or decongestants" | Verified |
| 335 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.818 | "The tricyclic antidepressants have also been useful" | Verified |
| 336 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.818 | "are the calcium channel blockers" | Verified |
| 337 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.817 | "β-adrenergic antagonists (β-blockers)" | Verified |
| 338 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.817 | "identify any triggering factors that initiate the toothache/migraine attack" | Verified |
| 339 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.522 | "nor do opioid-based analgesics" | Verified |
| 340 | Okeson, 2012 | Chapter_19_Differential_Diagnosis_of_Toothache_Odo | PDF p.822 | "topiramate (Topamax, Ortho-McNeil), lamotrigine (Lamictal, GlaxoSmithKline), and valproic acid (Depakene, Abbott)" | Verified |
| 341 | Sikri, 2019 | 03_3_Pathophysiology_of_Pain.md | PDF p.41 (printed p.20) | "The classic symptom of irreversible pulpitis is lingering pain induced by thermal stimuli." | Verified |
| 342 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.512 | "This is known as a graded response." | Verified |
| 343 | Jaeger, 2019 | 17_Chapter_17_Non_Odontogenic_Toothache_and_Chroni | PDF p.416 (printed p.468) | "Precipitating factors may include alcohol or other vasodilating substances" | Verified |
| 344 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.518 | "The headache is usually aggravated with routine physical activity" | Verified |
| 345 | Law, Nixdorf and Mattscheck, 2021 | 04_4_Diagnosis_of_the_nonodontogenic_toothache.md | PDF p.542 | "Assessment of the intensity of pain is easily accomplished using a verbal analog scale (VAS)." | Verified |
<!--LEDGER END-->


Keep quotations short and only as long as needed to locate the source. Never copy textbook passages into this report.

## Evidence and uncertainty notes

- **[RECALL] / unverified:** none presented as sourced fact. The sentence 'Management follows the underlying pulpal or periapical diagnosis' under barodontalgia is reasoning (no book states definitive management); it is marked as reasoning in the answer. The classification headings (5 groups etc.) are the books' own.
- **Interpretation / synthesis:** the Differentiation table and the referral table consolidate statements from the cited chapters; each cell traces to the authors named under the table. Cluster pacing and migraine dark-room behaviour are Ingle statements; paroxysmal hemicrania pacing is given as Ingle states.
- **Conflicting sources:** (1) persistent pain after root canal treatment: Cohen 5.3% at 6+ months (about half non-odontogenic), Torabinejad 5% (62% non-odontogenic), Ingle 3-13%; different studies, shown side by side. (2) Secondary causes of TN: Cohen 15-30%, Okeson about 2% of paroxysmal neuralgias from central lesions; not reconciled. (3) Cluster duration: Cohen 15 min-2 h, Ingle 15-180 min, Sikri 30-45 min. (4) Atypical odontalgia: neuropathic (Okeson, Cohen, Ingle) vs psychiatric basis strongly suspected (Walton 2002); Torabinejad 4 months, Okeson over 4 months, PDAP 3 months and 8 h/day. (5) Cluster sex ratio: Cohen men 3-4 times, Ingle 4-5 times; left out of the answer. (6) Both Ingle and Okeson give 61% for TN/pretrigeminal neuralgia but for different things (wrongly treated dentally vs initial dental pain); the answer states them separately only for Ingle and does not repeat Okeson's.
- **Numerical claims:** all appear in the locator phrases; see ledger for pages.
- **Literature evidence:** none opened.

## Coverage and overlap

- **Question wording / marks:** "Pain in and around the Oro-Facial Region." 100m; absorbs "Orofacial dental pain - Diagnosis and management." (50m), "Non-odontogenic tooth pain." (10m), "Aerodontalgia." (7m).
- **Related questions:** Diagnosis Q07 (differential diagnosis between teeth; only pointed to); Diagnosis D2 (non-odontogenic pain note); Pain Q03 (pathways of endodontic pain) overlaps the mechanisms section.
- **Content absorbed or deliberately omitted:** Cut for length: burning mouth syndrome, occipital/nervus intermedius/superior laryngeal neuralgia, CRPS/sympathetically maintained pain (Cohen calls it extremely rare), ear pain, thyroid and carotid detail, cervical spine detail, polyarthritis detail, Cohen's case studies, Ingle's TMD classification table, hemicrania continua detail beyond one line, pericoronitis (Sikri), the specificity theory (Walton), neurogenic inflammation and pulp neuropeptides (Walton), Gulabivala Table 16.4 (used only for the conflict on cluster duration through Sikri/Cohen/Ingle; Table 16.4 itself not tabulated), gabapentin/pregabalin dosing for TN, Okeson's capsaicin TN data.
- **Essential omissions / open points:** Gutmann Ch.6 (TMD occlusal signs) and Ingle Ch.16 (sinus) unread; Hargreaves and Goodis edition city; Ingle author name; Torabinejad publisher details.

## Revision history

| Date | Answer version / commit | Change | Audit action |
|---|---|---|---|
| 2026-11-10 | v1 draft | First draft | build_audit.py run |

## Final audit checklist

- [ ] Every factual author-year citation is supported by a verified source.
- [ ] Every numerical value has a traceable source.
- [ ] Chapter authors, edition, year and bibliographic details are verified or explicitly marked unknown.
- [ ] Disagreements between sources are represented accurately.
- [ ] Any [RECALL] or interpretive claim is not disguised as a sourced fact.
- [ ] The student-facing answer contains no retrieval report, source locator ledger or generation diagnostics.
- [ ] The reference list matches the in-text author-year citations.
