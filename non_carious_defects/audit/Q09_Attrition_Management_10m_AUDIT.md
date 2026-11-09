# Internal answer audit — Q09 Attrition and its management (10m)

**Student-facing answer:** `non_carious_defects/canonical/Q09_Attrition_Management_10m_CANONICAL.md` (published as `Conservative Dentistry/Non-Carious Tooth Defects/Q09_Attrition_Management_10m.md`)

**Last updated:** 2026-11-09
**Audit owner:** Niranjan (drafted with Claude)

> Internal working record only. Do not publish this file to the student-facing Answer Bank.

## Retrieval record

- **Sources consulted:**
  - Advanced Operative Dentistry Ch.4 "Tooth wear" (Bartlett), read in full; offset 6, confirmed at printed pp.45, 49 and 53.
  - Advanced Operative Dentistry Ch.16 (Bartlett and Ricketts), Dahl timing; offset 1.
  - Goldstein's Esthetics in Dentistry 3rd ed Ch.22: attrition and bruxism sections, the Turner classification and the reference list; offset 36, confirmed at pp.697-699.
  - Harpreet Singh, Essentials of Preclinical Conservative Dentistry 2nd ed Ch.21, attrition section; offset 17.
  - Marzouk Ch.27; offset -3, two-column OCR.
  - Sturdevant's 2nd South Asian ed Ch.20; offset 19.
  - Mount 3rd ed Ch.4 (Kaidonis et al, cited as 2016b) and Ch.1 (Kaidonis et al, cited as 2016a); offset 16.
  - Modern Operative Dentistry Ch.1 (Torres et al); offset 14.
  - Alani and Patel Ch.7; offset 23.
  - Pickard's Ch.1 (Banerjee and Watson); offset 11.
- **Existing evidence reused:** `work/g5/locators.py` (merged into `non_carious_defects/locators.py`).
- **New retrieval performed:** Gemini duel review on 2026-11-09 (record: `.duel/2026-11-09-attrition-q09/`, local only). Each accepted point was re-checked in the textbooks or on PubMed.
- **Live literature search:** yes, PubMed, abstracts only. Johansson et al 2008, De la Torre Canales et al 2017, Lohbauer and Reich 2017, and Turner and Missirlian 1984 (record checked only to confirm the authors' initials).
- **Limitations:** literature was read as abstracts only. Marzouk's publication year is not printed in the source copy. The chapter authors of Sturdevant Ch.20 are not printed in the file, so it is cited by its editors (Ritter et al).

## Source locator ledger

| Locator key | Source | File, page | Short verification phrase | Status |
|---|---|---|---|---|
| g5_aod_def_attr | Bartlett, 2011 | Advanced_Operative_Dentistry.md, PDF p.51 (printed p.45) | "Attrition is the wear of tooth against tooth." | Verified |
| g5_st_def | Ritter et al, 2019 | Sturdevants_Art_and_Science_of_Operative_Dentistry, PDF p.568 (printed p.549) | "Attrition is the mechanical wear of the incisal or occlusal surface as a result of functio…" | Verified |
| g5_gl_def | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.732 (printed p.696) | "Attrition is the loss of tooth structure by mechanical forces from opposing teeth." | Verified |
| g5_mo_def | Torres et al, 2020 | Modern_Operative_Dentistry.md, PDF p.25 (printed p.11) | "Attrition is defined as wear by tooth-to-tooth contact without the impact of any other sub…" | Verified |
| g5_hs_def | Singh, 2020 | Essentials_of_Preclinical_Conservative_Dentistry_H, PDF p.264 (printed p.247) | "It can also be defined as the physiological wearing of the tooth as a result of tooth-to-t…" | Verified |
| g5_hs_phys | Singh, 2020 | Essentials_of_Preclinical_Conservative_Dentistry_H, PDF p.264 (printed p.247) | "is thus more physiological than pathological" | Verified |
| g5_hs_path | Singh, 2020 | Essentials_of_Preclinical_Conservative_Dentistry_H, PDF p.264 (printed p.247) | "Pathological causes include parafunctional habits such as bruxism." | Verified |
| g5_mz_def | Marzouk et al, undated | Operative_Dentistry_Marzouk.md, PDF p.412 (printed p.415) | "Attrition may be defined as surface tooth structure loss" | Verified |
| g5_mo_phys | Torres et al, 2020 | Modern_Operative_Dentistry.md, PDF p.25 (printed p.11) | "Physiological wear is considered a slow degradation of the dental shape" | Verified |
| g5_mt_young | Kaidonis et al, 2016 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.72 (printed p.56) | "Wear in a young individual with a full complement of teeth would be considered as patholog…" | Verified |
| g5_aod_age | Bartlett, 2011 | Advanced_Operative_Dentistry.md, PDF p.56 (printed p.50) | "if the same amount of wear was seen in a 20-year-old patient, alarm bells might sound" | Verified |
| g5_pg_phys | Banerjee and Watson, 2015 | Pickards_Guide_to_Minimally_Invasive_Operative_Den, PDF p.22 (printed p.11) | "It can be physiological, occurring slowly and naturally throughout life, or pathological" | Verified |
| g5_gl_brux | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.732 (printed p.696) | "It is well established that the most common cause of attrition is bruxism." | Verified |
| g5_gl_func | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.732 (printed p.696) | "Functional habits, such as chewing and swallowing, rarely result in tooth contact" | Verified |
| g5_gl_factors | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "These include malocclusion, environmental factors, and genetic factors." | Verified |
| g5_gl_crossbite | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "we see greater wear in teeth that are in crossbite" | Verified |
| g5_gl_dust | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "chronic exposure to dust and dirt can also cause increased wear" | Verified |
| g5_gl_genetic | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "Both of these conditions make the teeth more susceptible to wear at an increased rate." | Verified |
| g5_aod_brux_stress | Bartlett, 2011 | Advanced_Operative_Dentistry.md, PDF p.56 (printed p.50) | "some component of stress causing repeated tooth clenching or grinding is acknowledged by m…" | Verified |
| g5_aod_interf | Bartlett, 2011 | Advanced_Operative_Dentistry.md, PDF p.56 (printed p.50) | "since interferences are so common in asymptomatic subjects this association remains unprov…" | Verified |
| g5_mt_normal | Kaidonis et al, 2016 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.72 (printed p.56) | "is part of the genetic code, is central in origin and is quite normal" | Verified |
| g5_mt_stress | Kaidonis et al, 2016 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.73 (printed p.57) | "The main risk factor responsible for increasing grinding activity is stress" | Verified |
| g5_mt_occl | Kaidonis et al, 2016 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.73 (printed p.57) | "there is no correlation between tooth grinding and occlusion" | Verified |
| g5_mt_discount | Kaidonis et al, 2016 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.73 (printed p.57) | "the occlusion cannot be entirely discounted" | Verified |
| g5_st_cause | Ritter et al, 2019 | Sturdevants_Art_and_Science_of_Operative_Dentistry, PDF p.568 (printed p.549) | "such as tooth grinding, or bruxism, usually resulting from:" | Verified |
| g5_gl_bruxdef | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "Bruxism is a condition in which persons grind, gnash, or clench their teeth." | Verified |
| g5_gl_sleep | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "Sleep bruxism is considered a sleep-related movement disorder." | Verified |
| g5_aod_guidance | Bartlett, 2011 | Advanced_Operative_Dentistry.md, PDF p.56 (printed p.50) | "with facets appearing on teeth used in guidance" | Verified |
| g5_gl_sites | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.732 (printed p.696) | "the palatal surfaces of maxillary anterior teeth, and the labial surfaces of mandibular an…" | Verified |
| g5_gl_shiny | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.732 (printed p.696) | "The affected surfaces are usually hard, smooth, and shiny." | Verified |
| g5_gl_yellow | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.732 (printed p.696) | "may exhibit a yellowish-brown" | Verified |
| g5_aod_facets | Bartlett, 2011 | Advanced_Operative_Dentistry.md, PDF p.55 (printed p.49) | "demonstrate paired wear facets" | Verified |
| g5_aod_filed | Bartlett, 2011 | Advanced_Operative_Dentistry.md, PDF p.55 (printed p.49) | "almost as if they have been filed" | Verified |
| g5_ap_demarc | Alani and Patel, 2025 | Adhesive_Techniques_in_Restorative_Dentistry_Alani, PDF p.235 (printed p.212) | "there is a definite demarcation between the area that is being worn and those areas of the…" | Verified |
| g5_ap_mirror | Alani and Patel, 2025 | Adhesive_Techniques_in_Restorative_Dentistry_Alani, PDF p.235 (printed p.212) | "The maxillary and mandibular teeth mirror each other in the shape of the occlusal plane." | Verified |
| g5_st_cupped | Ritter et al, 2019 | Sturdevants_Art_and_Science_of_Operative_Dentistry, PDF p.568 (printed p.549) | "resulting in cupped-out areas because the exposed, softer dentin wears faster than the sur…" | Verified |
| g5_aod_fracture | Bartlett, 2011 | Advanced_Operative_Dentistry.md, PDF p.55 (printed p.49) | "Typically in severe cases fractured restorations are found following the excessive occlusa…" | Verified |
| g5_st_craze | Ritter et al, 2019 | Sturdevants_Art_and_Science_of_Operative_Dentistry, PDF p.568 (printed p.549) | "Craze lines are not sensitive and do not require treatment" | Verified |
| g5_gl_inter | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.732 (printed p.696) | "Wear may also occur interproximally, causing mesial drifting" | Verified |
| g5_hs_proximal | Singh, 2020 | Essentials_of_Preclinical_Conservative_Dentistry_H, PDF p.265 (printed p.248) | "leading to drifting and overall reduction of the dental arch length" | Verified |
| g5_hs_cheek | Singh, 2020 | Essentials_of_Preclinical_Conservative_Dentistry_H, PDF p.265 (printed p.248) | "Cheek biting is another consequence of occlusal surface attrition." | Verified |
| g5_mz_ten | Marzouk et al, undated | Operative_Dentistry_Marzouk.md, PDF p.412 (printed p.415) | "time (ten years and more), the alveolar bone can grow" | Verified |
| g5_mz_short | Marzouk et al, undated | Operative_Dentistry_Marzouk.md, PDF p.412 (printed p.415) | "be no chance for the alveolar bone to erupt occlusally" | Verified |
| g5_gl_ovd | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "there is rarely loss of the vertical dimension of occlusion" | Verified |
| g5_mt_facets | Kaidonis et al, 2016 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.72 (printed p.56) | "Wear facets on the working surfaces of teeth offer the most objective evidence for identif…" | Verified |
| g5_mt_shiny | Kaidonis et al, 2016 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.72 (printed p.56) | "well-defined and polished facets indicate active tooth grinding" | Verified |
| g5_mt_flake | Kaidonis et al, 2016 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.72 (printed p.56) | "active grinding can cause enamel flaking on the incisal edges of teeth" | Verified |
| g5_mt_ng | Kaidonis et al, 2016 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.72 (printed p.56) | "Polish the occlusal surface to a matte finish only" | Verified |
| g5_gl_historic | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "the current damage may be present from historical behaviors" | Verified |
| g5_gl_casts | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "This can be done by making casts and taking digital" | Verified |
| g5_gl_twi | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "tooth wear index published by Smith and Knight in 1984" | Verified |
| g5_hs_index | Singh, 2020 | Essentials_of_Preclinical_Conservative_Dentistry_H, PDF p.264 (printed p.247) | "Noticeable flattening parallel to the occluding planes" | Verified |
| g5_aod_combo | Bartlett, 2011 | Advanced_Operative_Dentistry.md, PDF p.51 (printed p.45) | "It is uncommon to observe the singular effects of erosion, abrasion or attrition and more …" | Verified |
| g5_pg_softened | Banerjee and Watson, 2015 | Pickards_Guide_to_Minimally_Invasive_Operative_Den, PDF p.24 (printed p.13) | "Acid-softened tooth surfaces are more" | Verified |
| g5_gl_mpd | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "may also experience symptoms of myofacial pain dysfunction syndrome" | Verified |
| g5_aod_splint | Bartlett, 2011 | Advanced_Operative_Dentistry.md, PDF p.58 (printed p.52) | "The use of full coverage splints will be effective for those patients with mainly a bruxis…" | Verified |
| g5_aod_michigan | Bartlett, 2011 | Advanced_Operative_Dentistry.md, PDF p.59 (printed p.53) | "full coverage upper hard acrylic splint with canine rises in lateral excursions" | Verified |
| g5_aod_vac | Bartlett, 2011 | Advanced_Operative_Dentistry.md, PDF p.59 (printed p.53) | "Although neither has been shown to be more effective, the durability and longevity of the …" | Verified |
| g5_mt_ng2 | Kaidonis et al, 2016 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.73 (printed p.57) | "This does not stop the grinding (although it may be reduced initially) but it does conserv…" | Verified |
| g5_mo_splint | Torres et al, 2020 | Modern_Operative_Dentistry.md, PDF p.25 (printed p.11) | "Since elimination of the parafunctional habits is very hard to achieve, occlusal acrylic r…" | Verified |
| g5_mz_splint | Marzouk et al, undated | Operative_Dentistry_Marzouk.md, PDF p.414 (printed p.417) | "proper discluding-protecting occlusal" | Verified |
| g5_hs_tx1 | Singh, 2020 | Essentials_of_Preclinical_Conservative_Dentistry_H, PDF p.265 (printed p.248) | "should be controlled by occlusal adjustments and use of" | Verified |
| g5_mz_equil | Marzouk et al, undated | Operative_Dentistry_Marzouk.md, PDF p.414 (printed p.417) | "Occlusal equilibration should be performed after all" | Verified |
| g5_mt_equil | Kaidonis et al, 2016 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.73 (printed p.57) | "Although occlusal equilibrations are not normally advocated" | Verified |
| g5_mt_mousse | Kaidonis et al, 2016 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.73 (printed p.57) | "tooth mousse has shown the best results" | Verified |
| g5_hs_fl | Singh, 2020 | Essentials_of_Preclinical_Conservative_Dentistry_H, PDF p.265 (printed p.248) | "use of fluoride solution/dentin bonding agents" | Verified |
| g5_hs_endo | Singh, 2020 | Essentials_of_Preclinical_Conservative_Dentistry_H, PDF p.265 (printed p.248) | "Teeth with pulp involvement should undergo endodontic therapy or extraction according to t…" | Verified |
| g5_mz_endo | Marzouk et al, undated | Operative_Dentistry_Marzouk.md, PDF p.414 (printed p.417) | "Pulpally involved teeth should be extracted, or undergo" | Verified |
| g5_st_restore | Ritter et al, 2019 | Sturdevants_Art_and_Science_of_Operative_Dentistry, PDF p.571 (printed p.552) | "Areas of significant occlusal attrition that have exposed dentin are sensitive, or annoyin…" | Verified |
| g5_aod_restore_ind | Bartlett, 2011 | Advanced_Operative_Dentistry.md, PDF p.59 (printed p.53) | "The main indications which eventually demand restorative treatment of worn teeth are appea…" | Verified |
| g5_mz_metal | Marzouk et al, undated | Operative_Dentistry_Marzouk.md, PDF p.414 (printed p.417) | "only metallic (metallic-based) restorations should" | Verified |
| g5_ap_attrmat | Alani and Patel, 2025 | Adhesive_Techniques_in_Restorative_Dentistry_Alani, PDF p.244 (printed p.221) | "an attritive aetiology requires a more durable, harder occlusal surface" | Verified |
| g5_mo_gold | Torres et al, 2020 | Modern_Operative_Dentistry.md, PDF p.25 (printed p.11) | "Cast gold restorations are usually softer than enamel and amalgam, resulting in less wear …" | Verified |
| g5_mo_feld | Torres et al, 2020 | Modern_Operative_Dentistry.md, PDF p.25 (printed p.11) | "Feldspar ceramics produce extensive antagonistic tooth wear" | Verified |
| g5_mo_modern | Torres et al, 2020 | Modern_Operative_Dentistry.md, PDF p.25 (printed p.11) | "modern dental ceramics are significantly less abrasive" | Verified |
| g5_gl_turner | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "Turner proposed a classification system for occlusal wear in 1984" | Verified |
| g5_gl_t1 | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "excessive wear with loss of occlusal vertical dimension (OVD)" | Verified |
| g5_gl_t2 | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "excessive wear without loss of OVD but with space available" | Verified |
| g5_gl_t3 | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "excessive wear without loss of OVD but with limited space" | Verified |
| g5_gl_ill | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.733 (printed p.697) | "This approach, however, may be ill advised." | Verified |
| g5_gl_guard | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.739 (printed p.703) | "once the prosthetic rehabilitation is completed, an occlusal guard should be fabricated" | Verified |
| g5_st_guard | Ritter et al, 2019 | Sturdevants_Art_and_Science_of_Operative_Dentistry, PDF p.571 (printed p.552) | "occlusal guard therapy should be considered for nocturnal protection of indirect restorati…" | Verified |
| g5_mt_scooped | Kaidonis et al, 2016 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.73 (printed p.57) | "A worn dentition with scooped dentine is functional." | Verified |
| g5_mt1_abrfood | Kaidonis et al, 2016, Ch.1 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.33 (printed p.17) | "An abrasion area produced by food, in contrast to an attrition facet, is generally not wel…" | Verified |
| g5_mt1_abrscoop | Kaidonis et al, 2016, Ch.1 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.33 (printed p.17) | "when dentine is exposed, it may be ‘scooped out’ as it is softer than enamel" | Verified |
| g5_mt1_corrscoop | Kaidonis et al, 2016, Ch.1 | Preservation_and_Restoration_of_Tooth_Structure_Mo, PDF p.31 (printed p.15) | "This leads to a ‘scooped-out’ appearance that often progresses rapidly" | Verified |
| g5_gl_turnerref | Goldstein et al, 2018 | Esthetics_in_Dentistry_Goldstein.md, PDF p.751 (printed p.715) | "Turner KA, Missirlian DM. Restoration of the extremely worn" | Verified |
| g5_a16_34 | Bartlett and Ricketts, 2011 | Advanced_Operative_Dentistry.md, PDF p.210 (printed p.209) | "Usually sufficient interocclusal space is created in 3–4 months" | Verified |
| g5_a16_39 | Bartlett and Ricketts, 2011 | Advanced_Operative_Dentistry.md, PDF p.212 (printed p.211) | "the time needed for the adaption and occlusal changes ranges from 3 to 9 months" | Verified |
All 89 locators verified by `work/g5/locators.py` (`missing 0`, 2026-11-09).

## Evidence and uncertainty notes

- **[RECALL] / unverified:** history items (partner report, morning stiffness, reflux), masseter hypertrophy, referral for sleep disorders, and "direct composite for localised mild wear" are standard clinical teaching without a locator.
- **Interpretation / synthesis:**
  - "Dust and dirt is strictly a third-body abrasive co-factor" is reasoning from the definition of attrition. Goldstein lists dust under attrition.
  - "Cupped dentine points to an added abrasive or erosive component" is a synthesis of Mount Ch.1 against Sturdevant Ch.20.
- **Conflicting sources (shown side by side, not ranked):**
  - Stress versus occlusion in bruxism (Bartlett, Kaidonis 2016b vs Goldstein).
  - Occlusal equilibration (Singh, Marzouk vs Kaidonis 2016b).
  - Restorative material for heavy loading (Marzouk metal only; Alani and Patel; Torres).
  - Cupped dentine in attrition (Sturdevant vs Mount Ch.1).
- **Numerical claims:**
  - Ten years and more for compensation: Marzouk p.416.
  - 3-4 and 3-9 months for Dahl space: Bartlett and Ricketts, printed pp.209 and 211.
  - Turner and Missirlian 1984: Goldstein, printed p.715 (reference 43); PubMed PMID 6389829.
- **Literature evidence:**
  - De la Torre Canales 2017 is a systematic review of five small studies (3 RCTs, 2 before-after), all on sleep bruxism, with no consensus.
  - Lohbauer and Reich 2017 is a 2-year clinical study of 14 crowns, not a review.
  - Johansson 2008 is a narrative review.
  - All three were read as abstracts only.
- **Rejected after the duel:**
  - Gemini's "Missirlian HA": PubMed lists DM.
  - Botulinum toxin as "recognized, evidence-based".
  - Zirconia causing less wear than enamel-to-enamel contact.
  - The friction mechanism for dry-mouth wear.
  - A 3-6 month Dahl timeline.

## Coverage and overlap

- **Question wording / marks:** "Attrition and its management." 10m, Oct 2024 (Manipal PI). For a 5-mark version, write the definition, clinical features and preventive management only.
- **Related questions:**
  - Q1: classification of non-carious lesions.
  - P1: tooth wear indices.
  - Q10: rehabilitation of the worn dentition.
  - P2: Dahl concept.
  - dentin_hypersensitivity Q01-Q07: treatment of sensitivity.
- **Content absorbed or deliberately omitted:** the generic high-yield list and common-mistakes list were removed under the new standard; their substance is now in the body.
- **Essential omissions / open points:** Smith and Knight 1984 was not read (see P1).

## Revision history

| Date | Answer version / commit | Change | Audit action |
|---|---|---|---|
| 2026-11-09 | 98abde5 / 8b0b7b6 | First draft and second-reader review | 1131 merged locators, missing 0 |
| 2026-11-09 | uncommitted | Gemini duel (2 rounds): cupping, dust, Turner and Missirlian, Dahl timing, zirconia, botulinum toxin, dry mouth | Six new locators and three PubMed records; locators.py missing 0 |
| 2026-11-09 | uncommitted | Migrated to the examination-ready answer standard: one integrated answer, answer blueprint, Vancouver references in order of first citation; provenance moved here | Ledger regenerated from locators.py |

## Final audit checklist

- [x] Every factual author-year citation is supported by a verified source.
- [x] Every numerical value has a traceable source.
- [x] Chapter authors, edition, year and bibliographic details are verified or explicitly marked unknown.
- [x] Disagreements between sources are represented accurately.
- [x] Any [RECALL] or interpretive claim is not disguised as a sourced fact.
- [x] The student-facing answer contains no retrieval report, source locator ledger or generation diagnostics.
- [x] The reference list matches the in-text author-year citations.
