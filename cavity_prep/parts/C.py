# Group C locators: Q03 (recent advances in Cl.II cavity design), P3 (slot and box-only), Q14 (Class V designs)
STU = OP+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md'
SUM = OP+'Summitts_Fundamentals_of_Operative_Dentistry.md'
MZ = OP+'Operative_Dentistry_Marzouk.md'
MT = OP+'Preservation_and_Restoration_of_Tooth_Structure_Mount.md'
GG = OP+'Textbook_of_Preclinical_Conservative_Dentistry.md'
HS = OP+'Essentials_of_Preclinical_Conservative_Dentistry_Harpreet_Singh.md'
MOD = OP+'Modern_Operative_Dentistry.md'
PK = OP+'Pickards_Manual_of_Operative_Dentistry_9th.md'

src('c_stu11', STU, 19, 'Ritter et al, 2019')
src('c_stu13', STU, 19, 'Ritter et al, 2019')
src('c_stu19', STU, 19, 'Ritter et al, 2019')
src('c_stu26', STU, None, 'Ritter et al, 2019')
src('c_sum11', SUM, None, 'Hilton and Broome, 2013')
src('c_sum12', SUM, None, 'Overton, Summitt and Osborne, 2013')
src('c_sum15', SUM, None, 'Overton et al, 2013')
src('c_mz1', MZ, None, 'Marzouk et al, undated')
src('c_mz6', MZ, 3, 'Marzouk et al, undated')
src('c_mz7', MZ, 2, 'Marzouk et al, undated')
src('c_mz9', MZ, 1, 'Marzouk et al, undated')
src('c_mt7', MT, 16, 'Mount and Ngo, 2016')
src('c_gg10', GG, 7, 'Garg and Garg, 2011')
src('c_gg11', GG, 7, 'Garg and Garg, 2011')
src('c_hs12', HS, 17, 'Singh, 2020')
src('c_hs17', HS, 17, 'Singh and Rajkumar, 2020')
src('c_mod10', MOD, 10, 'Torres and Mehta, 2020')
src('c_pk5', PK, None, 'Banerjee and Watson, 2011')

add('c_stu11', {
 'c_stu_efp_black': 'the initial preparation should be further extended to areas that are normally self-cleansing so as to prevent recurrence of caries',
 'c_stu_efp_gone': 'The practice of extension for the prevention has virtually been eliminated',
 'c_stu_efp_reason': 'relative caries immunity provided by preventive measures such as fluoride application',
 'c_stu_efp_alt': 'enameloplasty, application of pit-and-fissure sealant and preventive resin or conservative composite restoration',
 'c_stu_tun_def': 'The tunnel tooth preparation joins an occlusal lesion with a proximal lesion by means of a prepared tunnel under the involved marginal ridge.',
 'c_stu_tun_obj': 'remove the caries lesion and leave the marginal ridge essentially intact',
 'c_stu_tun_dw1': 'may be compromised by lack of access and visibility',
 'c_stu_tun_dw2': 'Complete excavation of the caries lesion is not predictable.',
 'c_stu_tun_dw3': 'Preservation of the marginal ridge in a strong state is questionable',
 'c_stu_tun_gic': 'have found these materials to be inadequate for use as definitive, long-term restorations',
 'c_stu_tun_unk': 'It is currently unknown whether use of adhesively retained composite resin materials will result in better long-term clinical performance.',
 'c_stu_tun_not': 'remains controversial and is not supported in this textbook',
 'c_stu_adh_am': 'In vitro research studies suggest that the use of adhesive systems may enhance resistance and retention forms',
})
add('c_stu13', {
 'c_stu_box_oppose': 'Facial and lingual walls that almost oppose each other are recommended.',
 'c_stu_slot_occl': '1–1.25 mm at the occlusal wall',
 'c_stu_slot_lingual': 'With a facial approach, the lingual wall should face facially as much as possible',
 'c_stu_box_ind': 'tooth preparation is indicated if no occlusal caries lesion is present',
 'c_stu_box_lim1': 'a proximal surface with a narrow proximal contact',
 'c_stu_box_lim2': 'when the involved marginal ridge has no occlusal contact',
 'c_stu_box_walls': 'Facial and lingual proximal walls converge occlusally.',
 'c_stu_box_groove': 'Retention grooves are mandatory in box-only preparations.',
 'c_stu_box_gdepth': 'should have a 0.5-mm depth at the gingival point angle and extend occlusally to be visible in the occlusal outline form',
 'c_stu_slot_root': 'caries lesion development on the proximal root surface that is appreciably gingival to the proximal contact',
 'c_stu_slot_facial': 'the tooth preparation usually is approached from the facial direction and has the form of a slot',
 'c_stu_slot_am': 'Amalgam is particularly indicated for slot preparations if isolation is difficult.',
 'c_stu_slot_depth': '0.75–1 mm at the gingival aspect',
 'c_stu_slot_90': 'The external walls should form a 90° cavosurface angle.',
 'c_stu_slot_groove': 'create retention grooves in the occlusoaxial and gingivoaxial line angles',
 'c_stu_slot_rot': 'If the lesion is small, consideration should be given to slot preparation.',
})
add('c_stu19', {
 'c_stu_comp_noret': 'it is not necessary to use mechanical retention features in the tooth preparation for Class II composite restorations',
 'c_stu_comp_ext': 'The extension of the preparation is therefore ultimately dictated by the extension of the fault or defect.',
 'c_stu_comp_conv': 'These are often used for primary caries lesions, that is, initial restorations.',
 'c_stu_comp_box': 'This design is indicated when only the proximal surface is defective, with no lesions on the occlusal surface.',
 'c_stu_comp_parallel': 'held parallel to the long axis of the tooth crown',
 'c_stu_comp_box2': 'No bevelling or secondary retention is indicated.',
 'c_stu_comp_slot': 'access to the lesion can be obtained from either a facial direction or a lingual direction, rather than through the marginal ridge',
 'c_stu_comp_slotmr': 'Care should be taken not to undermine the marginal ridge during the preparation.',
 'c_stu_comp_large': 'has features that resemble a more traditional Class II amalgam tooth preparation',
 'c_stu_gic_slot': 'The same slot preparation design used for amalgam is used for glass ionomers.',
 'c_stu_gic_bevel': 'except bevels are rarely used',
 'c_stu_v_def': 'Class V tooth preparations, by definition, are located in the gingival one third of the facial and lingual tooth surfaces.',
 'c_stu_v_factors': 'decreased salivary function',
 'c_stu_v_bevel': 'at the cervical margin, bevels are usually not recommended because of the absence of enamel in this area',
 'c_stu_v_small': 'No effort is made to prepare the walls as butt joints, and usually no secondary retentive features are incorporated.',
 'c_stu_v_diverg': 'may have a divergent wall configuration and an axial surface that usually is not uniform in depth',
 'c_stu_v_nccl': 'usually requires only surface debridement of any exposed dentin and roughening/bevelling all enamel margins with a diamond instrument',
 'c_stu_v_large90': 'The features of the preparation include a 90-degree cavosurface margin',
 'c_stu_v_groove': 'Groove retention form usually is not necessary but may be used if retention of the restoration is a concern.',
 'c_stu_v_combo': 'are a combination of bevelled enamel margins and 90-degree root surface cavosurface margins',
 'c_stu_v_bevel45': 'resulting in an angle approximately 45 degrees to the external tooth surface, and prepared to a width of at least 0.5 mm',
 'c_stu_v_bur': 'a tapered fissure carbide bur (No. 271) or similarly shaped diamond is used at high speed',
 'c_stu_v_axialdepth': 'axial wall depth of 0.75 mm',
})
add('c_stu26', {
 'c_stu_v_am_depth': 'maintaining a limited axial depth of 0.5 mm inside the DEJ and 0.75 mm inside cementum',
 'c_stu_v_am_noret': 'this form provides no inherent retention, and retention form must be provided',
 'c_stu_v_am_groove': 'one along the incisoaxial line angle and the other along the gingivoaxial line angle',
 'c_stu_v_am_coves': 'four retention coves may be prepared, one in each of the four axial point angles',
 'c_stu_v_am_covewhy': 'Using four coves instead of two full-length grooves conserves the dentin near the pulp',
 'c_stu_v_am_gd': 'The depth of the grooves should be approximately 0.25 mm',
 'c_stu_v_am_round': 'amalgam can be condensed into rounded areas better than into sharp areas',
 'c_stu_v_am_crown': 'A full-coverage restoration should be considered for teeth with extensive cervical decalcification.',
})
add('c_sum11', {
 'c_sum_prewedge': 'Tooth separation obtained from prewedging promotes more conservative preparation and helps protect adjacent teeth from damage during preparation',
 'c_sum_damage': 'this damage makes it significantly more likely that the damaged surface will require subsequent restoration',
 'c_sum_sealfiss': 'Occlusal pits and fissures that are not carious may be treated with sealants.',
 'c_sum_329': 'Note that the proximal surface is left intact.',
 'c_sum_afr_p': 'Pilebro et al387 3 262 6.7',
 'c_sum_afr_s': 'Strand et al388 3 161 10.0',
 'c_sum_afr_l': 'Lumley and Fisher389 7 33 3.0',
 'c_sum_afr_h': 'Hasselrot390 7 282 7.1',
 'c_sum_afr_hb': 'al391 4 54 13.4',
 'c_sum_black': 'it was recommended that preparation design for posterior resin composite restorations be patterned after the traditional amalgam preparation',
 'c_sum_limit': 'The current design limits the removal of tooth structure to that needed to eliminate carious tooth structure and fragile enamel.',
 'c_sum_shallow': 'there is no need to penetrate to dentin if the caries lesion does not',
 'c_sum_narrow': 'A less bulky restoration helps to decrease the adverse effects of resin composite polymerization shrinkage',
 'c_sum_round': 'decreases stress concentration associated with sharp line angles',
 'c_sum_noefp': 'There is no “extension for prevention”',
 'c_sum_slotfr': 'does not make the restoration more resistant to fracture than the more conservative proximal slot restoration',
 'c_sum_slot10': '70% success after up to 10 years',
 'c_sum_stop': 'requirement that there be an occlusal stop on enamel',
 'c_sum_noshape': 'none has a “standard” shape',
 'c_sum_reinf': 'bonded posterior restorations cannot be relied upon to provide long-term reinforcement of tooth structure',
 'c_sum_sonic': 'sonic preparation does not adversely affect adhesion',
 'c_sum_bevelcontro': 'Bevel placement is a point of controversy with this preparation.',
 'c_sum_bevel05': 'conservative bevels (0.5 mm) should be placed at an approximately 45-degree angle',
 'c_sum_bevelleak': 'bevels on these margins significantly reduce marginal leakage',
 'c_sum_gbevel': 'The gingival margin should be beveled only if the margin is in enamel well away from the cementoenamel junction',
 'c_sum_occbevel': 'Placement of occlusal bevels has demonstrated no benefit to the longevity',
 'c_sum_tun_def': 'An alternative to the traditional approach for gaining access to proximal carious dentin has been termed the tunnel preparation',
 'c_sum_tun_jinks': 'It was first suggested by Jinks',
 'c_sum_tun_hk': 'later modified this procedure for use as a conservative technique for restoring teeth with small proximal caries lesions',
 'c_sum_tun_access': 'access is made in the occlusal fossa adjacent to the marginal ridge',
 'c_sum_tun_overhang': 'so there is less potential for a restorative overhang',
 'c_sum_tun_stiff': 'A two-surface, Class 2 cavity preparation has been shown to reduce tooth stiffness by 46%; only a 20% reduction occurs with an occlusal preparation.',
 'c_sum_tun_perim': 'The perimeter of the restoration is reduced, decreasing the potential for microleakage.',
 'c_sum_tun_convert': 'the preparation can easily be extended and converted into a more traditional Class 2 design',
 'c_sum_tun_pulp': 'the tunnel preparation often invades to within 1 mm of the pulp',
 'c_sum_tun_vis': 'visibility is decreased, and removal of carious dentin is more uncertain',
 'c_sum_tun_invitro': 'there is a high rate of residual carious tooth structure after completion of the preparation',
 'c_sum_tun_cds': 'a caries-detecting solution should be used to disclose remaining carious tooth structure',
 'c_sum_tun_mr': 'As the diameter of the preparation increases, the marginal ridge strength decreases.',
 'c_sum_tun_fail': 'Tunnel restorations tend to fail at a considerably higher rate than do other types of posterior restorations.',
 'c_sum_tun_resid': '34% to 41% of the restorations show either residual carious dentin or progression of enamel caries',
 'c_sum_tun_cause': 'are marginal ridge fracture and secondary caries',
 'c_sum_tun_slot': '21% of tunnel restorations failed during a 7-year period compared with zero failures for the slot restorations',
 'c_sum_tun_saucer': 'The survival proportion for the tunnel restorations was 46% compared with 76% for the Class 2 resin composite restorations.',
 'c_sum_tun_afr': 'Annual failure rate',
 'c_sum_tun_avoid': 'tunnel restorations are not indicated and should be avoided',
 'c_sum_tun_alt': 'are more conservative and more predictable',
})
add('c_sum12', {
 'c_sum_am_demin': 'if demineralization is superficial (less than half-way through the enamel)',
 'c_sum_am_icon': 'a low-viscosity resin infiltrant (eg, Icon, DMG) can be applied to the demineralized enamel',
 'c_sum_am_90': 'should have walls that meet the proximal surface of the tooth at 90 degrees',
 'c_sum_am_gfloor': 'The location of the gingival floor, therefore, should be determined by the gingival extent of the carious lesion',
 'c_sum_am_contact': 'consideration should be given to allowing contact to remain',
 'c_sum_am_wide': 'as an amalgam restoration becomes wider faciolingually, the tooth is more subject to fracture',
 'c_sum_am_slotfr': 'may minimize the severity of tooth fracture compared with Class 2 restorations that extend through occlusal grooves',
 'c_sum_am_seal': 'Fissures that contact the outline of a Class 1 or Class 2 preparation should be sealed.',
 'c_sum_am_noext': 'the preparation should not be extended further into a sound occlusal surface to provide retention of the proximal restoration',
 'c_sum_am_slotdef': 'having an occlusal outline limited to the marginal ridge area will be referred to in this chapter and others as a slot restoration',
 'c_sum_am_fall': 'The slot is deepened gingivally until the bur “falls” into the soft carious dentin',
 'c_sum_am_shell': 'a shell of enamel should be left between the preparation and the adjacent tooth',
 'c_sum_am_69': 'were damaged during Class 2 preparation 69% of the time',
 'c_sum_am_converge': 'should converge slightly toward the occlusal surface to provide retention form',
 'c_sum_am_15': 'should have a mesiodistal dimension of about 1.5 mm or more',
 'c_sum_am_grooves': 'retentive undercuts should be very distinct (at least 0.5 mm deep) and should oppose each other to form a dovetail effect in the dentin',
 'c_sum_am_long': 'Long grooves, extending from the gingival floor to the occlusal surface, are recommended for a proximal slot restoration',
 'c_sum_am_onlyfeature': 'the undercuts are the only feature that will prevent dislodgment of the restoration proximally',
 'c_sum_am_58': 'had been in function for more than 58 years',
 'c_sum_am_wideslot': 'If a proximal box or slot is so wide that retentive undercuts will not oppose each other',
 'c_sum_am_keyhole': 'sometimes referred to as a keyhole preparation or a facial o r lingual slot preparation',
 'c_sum_am_keyhole2': 'The entire preparation is apical to the proximal contact.',
 'c_sum_am_quarter': 'must have a faciolingual dimension of at least one-fourth the distance between the facial and lingual cusp tips',
 'c_sum_am_noadvocate': 'Although this preparation outline form should not be advocated',
})
add('c_sum15', {
 'c_sum_v_extent': 'the expected extent of the restoration should be determined by the extent of the lesion',
 'c_sum_v_am_box': 'requires the removal of sound tooth structure to create a box form for amalgam bulk and retention, so the use of adhesive materials is usually preferred',
 'c_sum_v_am_nosharp': 'There is no need to create sharp internal line angles or to remove sound dentin for axial depth greater than 1 mm.',
 'c_sum_v_nobevel': 'Cavosurface bevels are contraindicated in preparations for amalgam or glass ionomer because of the low edge strength of these materials.',
 'c_sum_v_am_grooves': 'grooves should be placed in the dentin of both the occlusal and gingival walls to help retain the amalgam',
 'c_sum_v_gold': 'The traditional preparation for a Class 5 direct gold restoration had a trapezoidal outline form',
 'c_sum_v_current': 'The outline form currently recommended for all restorative materials includes removal of carious tooth structure and unsupported enamel.',
 'c_sum_v_bevel': 'Beveling of enamel margins is recommended when it would expose the ends of the enamel rods',
 'c_sum_v_cem': 'Beveling the gingival margin that ends on cementum is not recommended.',
 'c_sum_v_nccl': 'For NCCLs, little or no preparation is required.',
 'c_sum_v_rough': 'found no increase in retention when sclerotic lesions were roughened with a bur',
 'c_sum_v_micro': 'appears to have been refuted',
 'c_sum_v_flow': 'Clinical trials have proven the theoretical to be incorrect.',
 'c_sum_v_gic80': '80% retention rate of restorations placed without mechanical retention at 10 years',
 'c_sum_v_gicprep': 'The preparation for glass-ionomer restorations is similar to that for dental amalgam but without the mechanical retention.',
 'c_sum_v_butt': 'A 90-degree butt joint approximately 1 mm deep is a reasonable minimum thickness.',
 'c_sum_v_franco': '96.4% of RMGI restorations were retained at 5 years, while only 51.5% of bonded resin composite restorations were retained',
 'c_sum_v_94': '94% of Class 5 RMGIs were retained',
})
add('c_mz1', {
 'c_mz_efp': 'This principle is called “extension for prevention, or cutting for immunity’’',
 'c_mz_efp_why': 'it should be placed in areas that are easily cleansable by natural and/or artificial means',
})
add('c_mz6', {
 'c_mz_d1': 'A. Class II, Design 1 (Conventional Design)',
 'c_mz_d1_ind': 'A patient with high caries and plaque indices.',
 'c_mz_d2': 'B. Class II, Design 2 (Modern Design)',
 'c_mz_d2_ind': 'A moderate to small sized proximal lesion(s), i.e., not exceeding the area of near approach.',
 'c_mz_d2_quarter': 'not exceeding a width of one-fourth the intercuspal distance',
 'c_mz_d2_dove': 'there should be little if any dovetail shape on the occlusal outline',
 'c_mz_d2_oh': 'Patients with good oral hygiene, low plaque and caries indices.',
 'c_mz_d2_groove': 'Buccal and lingual dentinal retention grooves will be present in every case, with no exception, in this design.',
 'c_mz_d2_round': 'all line angles are rounded, especially the axio-pulpal one',
 'c_mz_d5': 'Part of the proximal surface, with a very limited access area on the facial or lingual surface.',
 'c_mz_d5_mr': 'The marginal ridge is intact and adequately supported apically and occlusally with bulky tooth structure.',
 'c_mz_d5_unreal': 'it would be unrealistic from the biological, mechanical and conservative points to have an occlusal access to such an apically located proximal lesion',
})
add('c_mz7', {
 'c_mz_v1': 'A. Class V, Design 1 (Conventional Design)',
 'c_mz_v1_shape': 'trapezoidal with rounded corners, with the short side of the trapezoid being the gingival arm',
 'c_mz_v1_bulk': 'facilitate a 1.5 to 2 mm amalgam bulk within the preparation',
 'c_mz_v1_axial': 'the axial wall (Fig. 10C) occurs 0.5 mm from the dentino-enamel junction',
 'c_mz_v2': 'This design may be described as a typical facial or lingual preparation, except with a proximal ‘‘handle’’ extension.',
 'c_mz_v3': 'with a unilateral (Fig. 13A) or bilateral (Fig. 13B)',
 'c_mz_v4': 'This is known as the ‘‘multiple isolated boxes”’ cavity preparation.',
 'c_mz_v5': 'The lesion involves a bifurcation or part of it.',
})
add('c_mz9', {
 'c_mz9_fifth': 'may be as small as one-fifth the intercuspal distance',
 'c_mz9_round': 'internal line and point angles are extremely rounded',
 'c_mz9_mortise': 'Dentinal portions of preparations for direct tooth-colored materials should always be mortise shaped.',
 'c_mz9_saucer': 'materials could be used if the lesion is confined to enamel with minimal, forward dentinal involvement at its center',
 'c_mz9_contact': 'the preparations should allow for contact areas to remain totally or partially in tooth structure',
 'c_mz9_v1': 'A. Class V, Design 1 (mortise-shaped preparation)',
 'c_mz9_v1_round': 'the line and point angles must be more rounded than for the amalgam',
 'c_mz9_v2': 'B. Class V, Design 2 (non-mortise saucer-shaped',
 'c_mz9_v2_ind': 'It is used for erosion and abrasion lesions where the teeth are very sensitive and cavity preparation may increase that sensitivity.',
 'c_mz9_v2_dish': 'This design has no definite wall. It is dish-shaped in any cross-section',
})
add('c_mt7', {
 'c_mt_mylar': 'Use a short length of mylar strip as a matrix and wedge it lightly in place',
 'c_mt_cutback': 'remove it to a depth of approximately 2 mm only, sufficient to expose the entire enamel wall',
 'c_mt_week': 'it will take up to a week for a glass‐ionomer cement to mature',
 'c_mt_redund': 'That distinction has now been made redundant by advances in the quality and availability of restorative materials',
 'c_mt_tun3': 'When the enamel lesion is at least 3.00 mm apical to the crest of the marginal ridge',
 'c_mt_tun_small': 'The initial access should be as small as possible to preserve the natural tooth structure.',
 'c_mt_slot3': 'If the lesion is closer than 3.00 mm to the crest of the marginal ridge',
 'c_mt_slot2': 'leaving less than 2.0 mm of the marginal ridge occluso‐gingivally',
 'c_mt_three': '(i) internal occlusal fossa approach; (ii) the slot cavity approach; or (iii) the proximal approach',
 'c_mt_exterior': 'there may be a need to tunnel through to the exterior',
 'c_mt_simplest': 'the simplest and most conservative approach is through the occlusal fossa',
 'c_mt_remin': 'the proximal wall may remineralize and remain intact',
 'c_mt_funnel': 'Lean the bur towards the facial and the lingual to create a funnel‐shaped access cavity to the lesion',
 'c_mt_triang': 'The entry will now be approximately triangular in outline',
 'c_mt_affected': 'the removal of all affected dentine on the axial wall is unnecessary',
 'c_mt_gic': 'Glass‐ionomer cement will be the material of choice for restoration',
 'c_mt_lam': 'with the option of lamination with composite resin',
 'c_mt_slotbox': 'produce a small box form cavity sufficient to eliminate the lesion but not extended beyond the demineralized enamel',
 'c_mt_contact': 'it is often possible to maintain contact with the adjacent tooth on either the facial or lingual margin',
 'c_mt_noret': 'No specific retention design is required because a glass‐ionomer cement will be used for restoration.',
 'c_mt_s3_noret': 'it is unnecessary to develop a retentive design',
 'c_mt_s3_gic': 'If glass‐ionomer cement is to be placed, the state of the enamel is not important',
 'c_mt_s3_comp': 'the outline will need to be extended to reach sound, fully mineralized enamel',
 'c_mt_s3_pumice': 'A corrosion/abrasion lesion should be lightly cleaned with a brief scrub with pumice and water',
 'c_mt_s3_paa': 'conditioned with 10% polyacrylic acid for 10 seconds',
 'c_mt_s3_noinst': 'No instrumentation is required for the restoration of a corrosion lesion.',
})
add('c_gg10', {
 'c_gg_slot_ind1': 'Proximal root caries in geriatric patients with gingival recession.',
 'c_gg_slot_ind2': 'When adjacent tooth is missing.',
 'c_gg_slot_ind3': 'When isolation is difficult in treating cervical one-third root caries.',
 'c_gg_slot_classv': 'It is similar to class V tooth preparation.',
 'c_gg_box_ind1': 'Small proximal caries, not involving the occlusal surface.',
 'c_gg_box_ind3': 'Proximal caries in attrited teeth.',
 'c_gg_box_locks': 'These have 0.5 mm depth gingivally and 0.3 mm occlusally.',
 'c_gg_tun_def': 'approached through a tunnel initiating from the occlusal surface and ending on caries lesion on the proximal surface without cutting the marginal ridge',
 'c_gg_v_am_gum': 'In young patients, it is extended under free margins of gingiva',
 'c_gg_v_am_ic': 'retention is mandatory in these preparations',
})
add('c_gg11', {
 'c_gg_three': 'can be done in three designs: conventional, beveled conventional and modified',
 'c_gg_v_micro': 'microfill composites are material of choice',
 'c_gg_v_conv': 'Conventional class V preparation is indicated if it is present completely or mainly on root surface',
 'c_gg_v_box': 'shape of the preparation is a “box” type',
 'c_gg_v_075': 'keep the axial depth of 0.75 mm into the dentin',
 'c_gg_v_grooves': 'using a no. 1/4 or 1/2 round bur 0.25 mm deep into the dentin',
 'c_gg_v_bev_ind': 'Beveled conventional class V preparation is indicated for replacing defective existing restoration or for restoring a large, carious lesion.',
 'c_gg_v_bev_depth': 'limited to only 0.25 mm into the dentin, when retention grooves are not placed and 0.5 mm when a retention groove is placed',
 'c_gg_v_bev45': 'bevel the enamel margins at an angle of 45° to the external surface and to a width of 0.25 to 0.5 mm',
 'c_gg_v_mod_ind': 'Restoration of small and moderate carious lesions and defects.',
 'c_gg_v_scoop': 'The final tooth preparation should have ‘scooped out’ appearance',
})
add('c_hs12', {
 'c_hs_v_typo': 'to have a pulpal depth of 75 mm at the gingival wall and 1.25 mm at the incisal wall',
 'c_hs_v_coves': 'Placing four retention coves at four point angles is another conservative alternative',
 'c_hs_v_butt': 'the cavosurface angle is kept at 90°, also called butt joint',
})
add('c_hs17', {
 'c_hs_conv': 'Conventional tooth preparations for composite resins are same as those typical for amalgam restorations.',
 'c_hs_bev': 'Bevels increase the surface area and thus more area is available for etching and bonding',
 'c_hs_bevuse': 'This design is mostly used for Class III, IV and V restorations',
 'c_hs_mod': 'has no specific pulpal or axial depth',
 'c_hs_scoop': 'remove the fault/caries as conservatively as possible',
 'c_hs_box_02': 'The initial proximal axial depth is prepared up to 0.2 mm inside the dentinoenamel junction',
 'c_hs_box_noret': 'Neither placing a bevel nor incorporating secondary retention features is usually indicated.',
 'c_hs_slot_2mm': 'at least 2 mm of intact enamel is seen in the occlusogingival area',
 'c_hs_slot_05': 'reveal caries extending up to 0.5 mm into the dentin, but the marginal ridge is intact',
})
add('c_mod10', {
 'c_mod_hmatrix': 'The adjacent tooth must be protected by a metallic matrix band, stabilized by a wooden wedge',
 'c_mod_hparallel': 'the occlusal and gingival walls will be parallel between each other and perpendicular to the axial wall',
 'c_mod_hret': 'larger on the buccolingual direction than on the gingivoocclusal direction',
 'c_mod_third': 'with reduction of approximately 33% of its fracture resistance',
 'c_mod_quarter': 'this standard was reduced to 1/4 of the distance between the tips of the cusps',
 'c_mod_efp': 'nowadays, the extension for prevention is no longer recommended, as well as no stereotyped outlines must be followed',
 'c_mod_vslot': 'this kind of preparation is called proximal box preparation or vertical slot preparation',
 'c_mod_hslot': 'the preparation is called horizontal slot preparation',
 'c_mod_05': 'if there is 0.5 mm or less of the tooth structure remaining in between the occlusal and the proximal preparation, it is better to connect them',
 'c_mod_sealant': 'it should never be grinded or cut to receive a restoration',
 'c_mod_18': 'resisted to a displacement load of 18.09 kg',
 'c_mod_7': 'A preparation with the occlusal box in the central groove and the dovetail lock resisted only 7.12 kg.',
 'c_mod_h2mm': 'with a remaining tooth structure of at least 2 mm of intact enamel below the marginal ridge',
 'c_mod_rogg': 'was developed by Roggenkamp et al.',
 'c_mod_hadv': 'has advantages of saving time, preservation of the tooth structure, and better esthetic results',
 'c_mod_hrot': 'It also shows advantages on rotated teeth.',
 'c_mod_hgroove': 'additional retention grooves must be prepared on the gingivoaxial and occlusoaxial line angles',
 'c_mod_noaxial': 'Additional mechanical retention locks or coves should be never prepared on pulpal or axial walls.',
 'c_mod_site3': 'considered Site 3 according to Mount and Hume',
})
add('c_pk5', {
 'c_pk_tun': 'This is only clinically successful if the lesion is sufficiently small',
 'c_pk_tun_fr': 'There is also a good chance of fracture of the weakened marginal ridge enamel in service',
 'c_pk_bl': 'Tunnelling from these aspects can result in successful management as long as the lesion is not too extensive',
 'c_pk_missing': 'Directly mesial or distal, if the adjacent tooth is missing',
})

book('Ritter2019', "Ritter AV, Boushell LW, Walter R, eds. Sturdevant's Art and Science of Operative Dentistry. 7th ed, Second South Asia Edition (adaptation editor Gopikrishna V). New Delhi: RELX India (Elsevier); 2019. Chs 11, 13, 19 and online Ch 26 (no chapter authors printed in this edition).")
book('c_Hilton2013', "Hilton TJ, Broome JC. Direct posterior esthetic restorations. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park, IL: Quintessence; 2013. Ch 11.")
book('c_Overton2013a', "Overton JD, Summitt JB, Osborne JW. Amalgam restorations. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park, IL: Quintessence; 2013. Ch 12.")
book('c_Overton2013b', "Overton JD, Hilton TJ, LittleStar ML, Starr CB. Class 5 restorations. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park, IL: Quintessence; 2013. Ch 15.")
book('c_Marzouk1985', "Marzouk MA, Simonton AL, Gross RD. Operative Dentistry: Modern Theory and Practice. St Louis/Tokyo: Ishiyaku EuroAmerica; Indian reprint, New Delhi: AITBS (publication year not printed in the extracted file; latest references cited are 1981).")
book('c_Mount2016', "Mount GJ, Ngo HC. Principles of cavity design for the restoration of advanced lesions. In: Mount GJ, Hume WR, Ngo HC, Wolff MS, eds. Preservation and Restoration of Tooth Structure. 3rd ed. Chichester: Wiley; 2016. Ch 7.")
book('c_Garg2011', "Garg N, Garg A. Textbook of Preclinical Conservative Dentistry. 1st ed. New Delhi: Jaypee Brothers; 2011. Chs 10, 11.")
book('c_Singh2020', "Singh H. Essentials of Preclinical Conservative Dentistry. 2nd ed. Gurgaon: Wolters Kluwer (India); 2020. Ch 12; Ch 17 (joint contribution with Rajkumar B).")
book('c_Torres2020', "Torres CRG, Mehta D. Tooth preparation (Ch 10). In: Torres CRG, ed. Modern Operative Dentistry: Principles for Clinical Practice. Cham: Springer Nature; 2020 (chapter title not verified from the file).")
book('c_Banerjee2011', "Banerjee A, Watson TF. Pickard's Manual of Operative Dentistry. 9th ed. Oxford: Oxford University Press; 2011. Ch 5.")
