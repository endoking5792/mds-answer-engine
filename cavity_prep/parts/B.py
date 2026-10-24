# Group B locators: Q02 (C-factor and polymerization stress, 50m), Q04 (tooth preparation for tooth-coloured materials, 50m)
B_STU = OP+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md'
B_SUM = OP+'Summitts_Fundamentals_of_Operative_Dentistry.md'
B_MZ = OP+'Operative_Dentistry_Marzouk.md'
B_MT = OP+'Preservation_and_Restoration_of_Tooth_Structure_Mount.md'
B_GG = OP+'Textbook_of_Preclinical_Conservative_Dentistry.md'
B_HS = OP+'Essentials_of_Preclinical_Conservative_Dentistry_Harpreet_Singh.md'
B_MOD = OP+'Modern_Operative_Dentistry.md'
B_MCC = OP+'Applied_Dental_Materials_McCabe_Walls_9th.md'
B_PHI = OP+'Phillips_Science_of_Dental_Materials.md'
B_CRG = OP+'Craigs_Restorative_Dental_Materials.md'
B_SIK = OP+'Indirect_Restorations_Sikri.md'

src('b_stu11', B_STU, 19, 'Boushell and Walter, 2019')
src('b_stu15', B_STU, 19, 'Perdigão et al, 2019')
src('b_stu16', B_STU, 19, 'Donovan et al, 2019')
src('b_stu19', B_STU, 19, 'Ritter et al, 2019')
src('b_sum9', B_SUM, None, 'Breschi et al, 2013')
src('b_sum10', B_SUM, None, 'Vargas et al, 2013')
src('b_sum11', B_SUM, None, 'Hilton and Broome, 2013')
src('b_sum19', B_SUM, None, 'Fasbinder, Neiva and Robbins, 2013')
src('b_mz9', B_MZ, 1, 'Marzouk et al, undated')
src('b_mt7', B_MT, 16, 'Mount and Ngo, 2016')
src('b_gg8', B_GG, 7, 'Garg and Garg, 2011')
src('b_gg11', B_GG, 7, 'Garg and Garg, 2011')
src('b_hs17', B_HS, 17, 'Singh and Rajkumar, 2020')
src('b_mod13', B_MOD, 7, 'Scotti et al, 2020')
src('b_mcc22', B_MCC, 9, 'McCabe and Walls, 2008')
src('b_phi13', B_PHI, 16, 'Anusavice, Shen and Rawls, 2013')
src('b_crg', B_CRG, 11, 'Sakaguchi, Ferracane and Powers, 2019')
src('b_sik5', B_SIK, None, 'Sikri, 2017')

add('b_stu15', {
 'b_c_relieve': 'stresses within the composite are relieved by flow from the unbonded surface',
 'b_c_limited': 'Stress relief within a three-dimensional bonded restoration is limited however by its configuration factor (C-factor)',
 'b_c_five': 'giving the restoration a configuration factor equal to 5',
 'b_c_gaps': 'Unrelieved stresses in the composite contribute to internal bond disruption and marginal gaps around restorations',
 'b_c_deep': 'partially responsible for the decrease in bond strengths observed when deep dentin is bonded',
 'b_c_vars': 'composite stiffness and its rate of acquisition of stiffness during polymerization',
 'b_c_17mpa': 'immediate bond strengths of approximately 17 MPa are necessary to resist the contraction stresses',
 'b_c_surface': 'Polymerization is initiated on the surface of the restoration, close to the light source, eliminating this surface as a potential stress relief pathway',
 'b_c_flownot': 'has not been proved effective clinically',
 'b_c_gic18': 'does not improve the restoration survival rate at 18 years',
 'b_c_hygro': 'results in partial relief of the contraction residual stresses from polymerization',
 'b_c_silorane': 'Silorane-based composites have the lowest hygroscopic expansion',
 'b_c_none': 'none of these methods has been effective in completely eliminating the deleterious effects of polymerization shrinkage stress',
 'b_c_lowshr': 'shrinkage stress is not necessarily reduced',
 'b_c_root200': 'the estimated C-factor in the root canal may exceed 200',
 'b_c_compliance': 'The polymerization shrinkage stress also depends on the degree of compliance (or deformation) of the substrate',
})
add('b_stu16', {
 'b_d_shr22': 'inherent polymerization shrinkage (2.2%–2.4%)',
 'b_d_shr24': 'Polymerization shrinkage (2.4%–2.8%) is the main disadvantage',
 'b_d_cannot': 'The shrinkage of composite resin materials cannot be avoided, but the stress created by the shrinkage can be reduced by the placement technique',
 'b_d_five': 'There are five primary strategies that can be used to reduce polymerization shrinkage stress',
 'b_d_primed': 'This primed layer has a relatively low modulus of elasticity',
 'b_d_rmgi05': 'thin liner (0.5 mm) of resin-modified glass ionomer',
 'b_d_flow05': 'place a thin layer (0.5 mm) of flowable composite resin as a liner',
 'b_d_soft': 'the longer the setting composite can maintain a gel or flowable condition, the better it can distribute the stresses',
 'b_d_softproc': 'ramped lights, pulse curing or simply holding the curing light some distance from the material',
 'b_d_softmixed': 'while other studies have demonstrated limited benefit',
 'b_d_cIV': 'A Class IV composite restoration has a wealth of unbonded surface area',
 'b_d_pulpal': 'the weakest bond (pulpal floor) gives away under the shrinkage stress',
 'b_d_bulk': 'bulk-fill composites appear to deliver an increased depth of cure and reduced polymerization-induced shrinkage stress',
 'b_d_bulk20': 'Evidence appears to support light-curing times of at least 20 s',
})
add('b_stu19', {
 'b_e_paa': 'a mild acid, such as 10% polyacrylic acid, is applied to the preparation',
 'b_e_boxlike': 'this boxlike preparation form may increase the negative effects of the cavity configuration factor',
 'b_e_c51': 'A typical Class I tooth preparation will have a high C-factor of 5/1',
 'b_e_pulpwall': 'The interface most likely to be adversely affected by high C-factor stresses is at the pulpal wall',
 'b_e_incr': 'Incremental insertion and light activation of the composite may reduce the negative C-factor effects',
 'b_e_linernot': 'but those claims are not supported by current clinical evidence',
 'b_e_sandwich': 'These suggested advantages are considered controversial',
 'b_e_regardless': 'Regardless of the effect of incremental placement on shrinkage stress, posterior composites should be placed incrementally',
 'b_e_2mm': 'with increments of no more than 2 mm in thickness',
 'b_e_noretent': 'it is not necessary to incorporate mechanical retention features',
 'b_e_flared': 'these conservative preparations typically result in more flared cavosurface forms',
 'b_e_noocclbev': 'No attempt is made to bevel the occlusal margin because it may result in enlarging the occlusal isthmus',
 'b_e_bulkstr': 'It is usually not necessary to reduce sound tooth structure to provide',
 'b_e_boxonly': 'This design is indicated when only the proximal surface is defective, with no lesions on the occlusal surface',
 'b_e_boxnobev': 'No bevelling or secondary retention is indicated',
 'b_e_slot': 'access to the lesion can be obtained from either a facial direction or a lingual direction, rather than through the marginal ridge',
 'b_e_slotconv': 'a more conventional Class II preparation, with an occlusal access component, should be used',
 'b_e_proxbev': 'Bevels are rarely used on any of the proximal box walls',
 'b_e_gingbev': 'Bevels also are not recommended along the gingival margins of the proximal box',
 'b_e_c3bev': 'an enamel bevel is used on the facial cavosurface margin to provide a gradual colour transition',
 'b_e_c3lingual': 'the lingual approach is always preferable',
 'b_e_c3width': 'creating a 45-degree angle to the external surface and to a width of 0.5–2 mm',
 'b_e_c3scoop': 'the walls may diverge externally from the axial depth resulting in a bevelled marginal design',
 'b_e_c5bev': 'Enamel bevels are typically used on the occlusal/ incisal margins of the preparation',
 'b_e_c5noeff': 'No effort is made to prepare 90-degree cavosurface margins',
 'b_e_c5width': 'prepared to a width of at least 0.5 mm',
 'b_e_nccl': 'requires only surface debridement of any exposed dentin and roughening/bevelling all enamel margins',
 'b_e_gicroot': 'The restoration of caries lesions on the roots of patients with active caries is the primary indication',
 'b_e_gicbev': 'except bevels are rarely used',
 'b_e_gicslot': 'The same slot preparation design used for amalgam is used for glass ionomers',
 'b_e_gicnot': 'not for typical Class I, II or IV restorations',
})
add('b_stu11', {
 'b_f_tblpulp': 'Pulpal depth Uniform 1.5 mm Remove defect; not usually uniform',
 'b_f_tblret': 'Primary retention form Convergence occlusally None (roughness/bonding)',
 'b_f_tblwall': 'Texture of prepared walls Smoother Rough',
 'b_f_tblseal': 'Include adjacent suspicious area Same Same No Seal these areas',
 'b_f_bevind': 'is indicated primarily for large restorations that have increased retention needs',
 'b_f_bevarea': 'Increases the surface area available for bonding',
 'b_f_bevaes': 'gradual increase in composite thickness from the margin to the bulk of the restoration',
 'b_f_90amal': 'a 90-degree cavosurface angle produces maximal strength for these materials',
 'b_f_tunnelnot': 'The tunnel tooth preparation technique remains controversial and is not supported in this textbook',
 'b_f_tunnelridge': 'Preservation of the marginal ridge in a strong state is questionable',
 'b_f_tunnelgic': 'have found these materials to be inadequate for use as definitive, long-term restorations',
})
add('b_sum9', {
 'b_g_feil87': 'Feilzer et al246 in 1987 found that shrinkage stress was related to the C-factor',
 'b_g_rigid': 'rigid resins produce high shrinkage stresses',
 'b_g_braga': 'shrinkage stress in composite restorations was affected more strongly by cavity depth than by diameter',
 'b_g_s200': 'The C-factor in post spaces may exceed 200, whereas coronal restorations are characterized by C-factors of 1 to 5',
})
add('b_sum10', {
 'b_h_vol15': 'Volumetric shrinkage during polymerization is typically between 1.5% and 5.0%',
 'b_h_gelation': 'after the material has acquired significant rigidity (called gelation), are not relieved by material flow',
 'b_h_weakest': 'especially at those with the weakest bonds (usually dentin or cementum)',
 'b_h_offset': 'long enamel bevels, low-shrinkage materials, flexible resin liners, slow-setting resin-modified glass-ionomer liners',
 'b_h_anterior': 'for most anterior restorations the C-factor is favorable',
 'b_h_stiff': 'High-stiffness materials will typically generate higher shrinkage stress',
 'b_h_saucer3': 'The finished preparation resembles a saucer and has no retentive undercuts',
 'b_h_bevno': 'enamel bonds have been demonstrated clinically to be adequate without bevels',
 'b_h_bevleak': 'no significant differences in marginal microleakage in Class 3 restorations whether or not margins were beveled',
 'b_h_bev2': 'the bevel can be extended to 2 mm or more on the facial surface',
 'b_h_rmginobev': 'Preparations for these materials should resemble those for resin composite, but bevels are not prepared',
 'b_h_rmgigroove': 'the placement of retention grooves or points is not necessary',
 'b_h_c4_1mm': 'An enamel bevel of at least 1 mm should be placed around the periphery of the cavity',
 'b_h_c4beyond': 'Increasing the width of the bevel beyond 1 mm has been shown to provide no additional strength',
 'b_h_c4facial': 'This bevel has a 60-degree angulation and is 2 to 3 mm in length',
 'b_h_c4lingual': 'limited to about 1 mm in length',
 'b_h_unsup': 'Unsupported facial enamel may be left for internal etching and bonding',
})
add('b_sum11', {
 'b_i_prr': 'the PRR is usually the technique of choice',
 'b_i_20': 'only a 20% reduction occurs with an occlusal preparation',
 'b_i_dye': 'a caries-detecting solution should be used to disclose remaining carious tooth structure',
 'b_i_overhang': 'there is less potential for a restorative overhang',
 'b_i_perim': 'The perimeter of the restoration is reduced',
 'b_i_convert': 'the preparation can easily be extended and converted into a more traditional Class 2 design',
 'b_i_towalls': 'polymerization shrinkage occurs toward the walls of cavity preparations to which it is bonded most strongly',
 'b_i_believed': 'VLC resin composite polymerizes toward the light source',
 'b_i_autocure': 'an autocured composite tends to induce less polymerization stress than does a comparable bulk of VLC composite',
 'b_i_150': 'reducing the initial irradiance to approximately 150 mW/cm2, followed by high-level irradiance (650 mW/cm2 or greater)',
 'b_i_equiv': 'results with these reduced-irradiance curing regimens have been equivocal',
 'b_i_impract': 'may require what many consider to be clinically impractical curing regimens',
 'b_i_zero': 'While it is intuitive to think that producing a material with zero shrinkage is ideal, this may not be true',
 'b_i_incrc': 'placement and curing of resin composite, the C-factor of each increment is reduced compared with bulk placement and curing',
 'b_i_bondinc': 'As the C-factor decreases, bond strength increases',
 'b_i_dramatic': 'shrinkage stresses increase dramatically',
 'b_i_1mm': 'an increment no thicker than 1 mm is placed against the gingival wall',
 'b_i_27': 'only 27% were satisfactory',
 'b_i_wedgeen': 'When the gingival margin is on enamel, this method has been shown to result in better marginal adaptation than curing from an occlusal direction',
 'b_i_wedgede': 'when the gingival margin is on dentin, this technique has failed to reduce gingival margin microleakage',
 'b_i_flowtheory': 'it is theorized that these materials could act as',
 'b_i_flownotdem': 'However, the efficacy of this method has not been demonstrated',
 'b_i_flow3x': 'flowable resin composites demonstrate up to three times greater polymerization shrinkage',
 'b_i_flowmaj': 'the majority of studies show no benefit from using a cured portion of flowable composite',
 'b_i_flowclin': 'have not demonstrated any difference in either postoperative sensitivity',
 'b_i_gicmargin': 'Use of a glass-ionomer liner has been demonstrated to improve marginal integrity',
 'b_i_autoprob': 'a number of problems associated with the use of autocured resin composite in posterior restorations argue against its use',
 'b_i_gicstress': 'they introduce less polymerization stress into tooth structure than does resin composite',
 'b_i_lessbulky': 'A less bulky restoration helps to decrease the adverse effects of resin composite polymerization shrinkage',
 'b_i_rounded': 'decreases stress concentration associated with sharp line angles',
 'b_i_noext': 'The occlusal fissures are included in the preparation only if the presence of carious tooth structure dictates this need',
 'b_i_slot70': '70% success after up to 10 years',
 'b_i_bevcontro': 'Bevel placement is a point of controversy with this preparation',
 'b_i_endon': 'etching of transversely exposed enamel rods (ends of rods) results in a bond that is significantly stronger',
 'b_i_proxbev': 'conservative bevels (0.5 mm) should be placed at an approximately 45-degree angle',
 'b_i_proxleak': 'bevels on these margins significantly reduce marginal leakage',
 'b_i_gingbev': 'The gingival margin should be beveled only if the margin is in enamel well away from the cementoenamel junction',
 'b_i_inverse': 'has been shown to significantly reduce microleakage as compared to a butt margin',
 'b_i_occlnot': 'The use of occlusal cavosurface margin bevels is not indicated',
 'b_i_occlwear': 'had significantly greater wear than those placed with occlusal butt margins',
 'b_i_bondedbase': 'an RMGI restorative material should be placed as the initial increment in the proximal box',
 'b_i_jinks': 'It was first suggested by Jinks373 in 1963',
 'b_i_stiff46': 'A two-surface, Class 2 cavity preparation has been shown to reduce tooth stiffness by 46%',
 'b_i_tun1mm': 'the tunnel preparation often invades to within 1 mm of the pulp',
 'b_i_tunfail': 'Tunnel restorations tend to fail at a considerably higher rate than do other types of posterior restorations',
 'b_i_tunres': 'there is a high rate of residual carious tooth structure',
})
add('b_sum19', {
 'b_j_contact': 'a large interproximal distance between teeth leading to difficulty in achieving proper interproximal contact',
 'b_j_2mm': 'Preparation should allow 2 mm of occlusal clearance',
 'b_j_round': 'All internal line angles should be rounded and walls divergent occlusally',
 'b_j_nogroove': 'There should be no grooves or sharp angles',
 'b_j_enamel': 'all margins can be placed on enamel',
 'b_j_onlay': 'when even one cusp of a posterior tooth is being covered with an esthetic bonded onlay, the ceramic onlay is preferred',
 'b_j_moderate': 'resin composite should be considered first for use in two- and three-surface inlay preparations of moderate width',
})
add('b_mz9', {
 'b_k_01': 'mechanically remove a fraction of 1 mm from the surface enamel (0.1 mm)',
 'b_k_rightangle': 'so the cavity margin will have a right angled cavosurface angle',
 'b_k_direct': 'It is also indicated for areas of direct loading',
 'b_k_four': 'There are four methods to accommodate and properly retain a restoration of these materials within tooth structure',
 'b_k_partial': 'acid conditioning is used only to reduce marginal leakage',
 'b_k_long': 'the entire enamel wall is bevelled at 45-70° to the cavity wall',
 'b_k_flash': 'Both shapes have the distinct disadvantage of having no definite marginal termination',
 'b_k_hollow': 'The hollow ground bevel is indicated for inaccessible areas',
 'b_k_scallop': 'Under no circumstances should scalloping be used for gingival walls',
 'b_k_skirt': 'This feature is used if conditioned enamel will be the main retentive mode for resinous material',
 'b_k_double': 'it is necessary to involve an enamel surface that is at least double the surface area of the defect to be restored',
 'b_k_rounded': 'The roundness of the line angles should be far more exaggerated than in amalgam preparations',
 'b_k_dovetail': 'Extension for retention in the form of a dovetail should absolutely be avoided in anterior teeth',
 'b_k_gingival': 'the gingival wall is the most critical in shaping the resistance and retention form of the restoration',
 'b_k_fifth': 'may be as small as one-fifth the intercuspal distance',
 'b_k_saucer': 'It is used for erosion and abrasion lesions where the teeth are very sensitive',
})
add('b_mt7', {
 'b_l_simplest': 'the simplest and most conservative approach is through the occlusal fossa',
 'b_l_affected': 'removal of all affected dentine on the axial wall is unnecessary',
 'b_l_3mm': 'When the enamel lesion is at least 3.00 mm apical to the crest of the marginal ridge',
 'b_l_slot': 'If the lesion is closer than 3.00 mm to the crest of the marginal',
 'b_l_2mm': 'leaving less than 2.0 mm of the marginal ridge',
 'b_l_noret': 'No specific retention design is required because a glass-ionomer cement will be used for restoration',
 'b_l_undermined': 'The presence of undermined enamel is of no consequence because it will be supported by adhesion with the restorative cement',
 'b_l_cutback': 'remove it to a depth of approximately 2 mm only, sufficient to expose the entire enamel wall',
 'b_l_remin': 'it is only necessary to remove the seriously broken down enamel',
 'b_l_25': 'polish the enamel margins with a 25μ diamond bur to enhance adhesion',
})
add('b_gg8', {
 'b_m_gicind': 'Class V, Class III, small class I tooth preparations',
 'b_m_gicci': 'In stress bearing areas like class I, class II and class IV',
})
add('b_gg11', {
 'b_n_075': 'preparation is kept 0.75 mm',
 'b_n_groove': 'It should be located at least 1 mm from the tooth surface and at least 0.5 mm deep into dentin',
 'b_n_davidson': 'The cavity configuration or C-factor was introduced by Prof Carol Davidson and his colleagues in 1980s',
 'b_n_higher': 'The higher the value of C-factor, the greater is the polymerization shrinkage',
 'b_n_light': 'Shrinkage in light cured composites occurs in the direction of light',
 'b_n_167': 'It accounts for 1.67-5.68% of the total volume',
 'b_n_wedge': 'Placing successive layers of wedge-shaped composite (1-1.5 mm) decreases polymerization shrinkage',
 'b_n_highest': 'three-dimensional tooth preparations (Class I) have the highest (most unfavorable) C-factor',
 'b_n_twowall': 'two-walled preparation',
 'b_n_threewall': 'three-walled preparation',
 'b_n_root': 'gap formation between the composite and root surface due to polymerization shrinkage',
 'b_n_three': 'the tooth preparation for the composites can be done in three designs: conventional, beveled conventional and modified',
 'b_n_convroot': 'Indication for conventional tooth preparation is the lesion present on the root surfaces',
 'b_n_bev': 'The bevel should be about 0.2 to 0.5 mm wide at an angle of 45° to the external tooth surface',
 'b_n_nobev': 'Bevels are not given in areas bearing heavy occlusal forces or on cemental cavosurface margins',
 'b_n_scoop': 'infected carious area is removed as conservatively as possible by',
 'b_n_c5bev': 'to a width of 0.25 to 0.5 mm',
})
add('b_hs17', {
 'b_o_075': 'An initial depth of 0.75 mm is considered as ideal',
 'b_o_groove': 'The groove is located 0.25 mm from the root surface and is prepared to a depth of 0.25 mm',
 'b_o_matrix': 'A matrix band can be kept next to this area to avoid cutting of the adjacent healthy tooth inadvertently',
 'b_o_types': 'The different types of tooth preparations for restoration using composite resins are as follows',
 'b_o_conv': 'Conventional tooth preparations for composite resins are same as those typical for amalgam restorations',
 'b_o_outline': 'The outline form for these is the extension of external walls at uniform and limited depth',
 'b_o_endon': 'ends of enamel rods are more effectively etched producing deeper micro-undercuts',
 'b_o_mostly': 'This design is mostly used for Class III, IV and V restorations',
 'b_o_modified': 'has no specific pulpal or axial depth',
 'b_o_affected': 'only the affected area is removed and therefore this preparation has no specific configuration',
 'b_o_combined': 'This design is mostly used for Class III preparations that extend on to the root surface',
 'b_o_slot': 'but the marginal ridge is intact (at least 2 mm of intact enamel is seen in the occlusogingival area)',
 'b_o_slot05': 'caries extending up to 0.5 mm into the dentin',
 'b_o_boxdej': 'The initial proximal axial depth is prepared up to 0.2 mm inside the dentinoenamel junction',
 'b_o_c1bev': 'The bevel is 0.25- to 0.5-mm wide and is at a 45° angle to the prepared wall',
 'b_o_chip': 'the thin layer of the composite that is applied over the bevel (if given) would chip off under the',
 'b_o_c3bev': 'A bevel width of 0.25–0.5 mm is provided',
 'b_o_c4bev': 'Width of the bevel can range from 0.25 to 2.0 mm',
 'b_o_c2nobev': 'No bevels are indicated for the facial and lingual walls of the proximal box unless the proximal box is too wide',
 'b_o_c5bev': 'a bevel is given on the incisal/occlusal wall of the Class V cavity preparation',
 'b_o_c5mod': 'The 90° cavosurface design is not required',
})
add('b_mod13', {
 'b_p_phases': 'passing through three phases identified as pre-gel, gel point, and post-gel phase',
 'b_p_1020': 'When the degree of conversion reaches 10–20%, the polymer chains are long enough to create a gel',
 'b_p_post': 'This stress is transmitted to the tooth-restoration interface and tooth structure and may promote the breaking of the adhesive bond, cuspal deflection, or enamel microcracks',
 'b_p_7': 'the final volumetric contraction could reach 7%, with an average of 2–3%',
 'b_p_24h': 'during the first 24 h after the light curing',
 'b_p_48': 'The volumetric shrinkage may cause stress levels of 4–8 MPa or even more',
 'b_p_stiff': 'the shrinkage stress of a composite is more related to the stiffness of the material',
 'b_p_feil': 'The cavity configuration factor or C-factor was proposed by Feilzer et al. [31], in 1987',
 'b_p_5': 'Therefore, the C-factor will be equals five',
 'b_p_2': 'resulting on a C-factor equals 2',
 'b_p_02': 'with only one bonded surface and five unbonded ones, and a C-factor equals 0.2',
 'b_p_oblique': 'preferably close to 0.5, which can be obtained by the application of oblique composite increments, connecting a maximum of two walls simultaneously',
 'b_p_deeper': 'the deeper preparation will have a greater C-factor than the shallower one',
 'b_p_versluis': 'the composites do not shrink toward the light source but toward the bonded walls',
 'b_p_losche': 'the use of reflective wedges only reduced the transmitted light, delaying the gel point',
 'b_p_chem': 'The chemically activated composites have slower curing reaction than the light-activated ones (more than 3 min)',
 'b_p_liner': 'but its real effectiveness is still controversial',
 'b_p_horiz': 'horizontal layers create significantly higher stress than oblique layers',
 'b_p_bulk': 'bulk techniques have inferior performances than incremental ones',
 'b_p_pulse': 'It is performed only on the last composite increment of the restoration',
 'b_p_sev': 'Several studies have shown the capacity of these protocols on reduction of the shrinkage stress',
})
add('b_mcc22', {
 'b_q_measure': 'and when we measure shrinkage it is important to identify this component',
 'b_q_ratio': 'The ratio of bonded:free area can therefore be used to predict interfacial stress caused by shrinkage',
 'b_q_zero': 'The C-factor for this situation is zero',
 'b_q_IV': 'a class IV cavity approximates to Fig. 22.12c and therefore has a C-factor of 0.5',
 'b_q_luting': 'factor values of greater than 10 may apply',
 'b_q_soft': 'There is little evidence to show whether or not this approach is effective',
 'b_q_cusp': 'In extreme cases the stress on the tooth may be great enough to cause cuspal fracture',
 'b_q_inlay': 'its shrinkage can result in a relatively large stress at the surface with both the tooth and the inlay due to the large C-factor',
 'b_q_stress': 'the stress determination may be more pertinent to the clinical consequences',
})
add('b_phi13', {
 'b_r_vol': '(1) total volume of the composite material, (2) type of composite, (3) polymerization speed',
 'b_r_gel': 'After the gel point, stresses cannot be relieved but instead continue to increase and concentrate',
 'b_r_ratio': 'Residual polymerization stress increases directly with this ratio',
 'b_r_layer': 'thinner layers reduce bonded surface area and maximize nonbonded surface area',
 'b_r_little': 'little advantage is to be gained by ramped, delayed, or',
 'b_r_numerous': 'Numerous laboratory studies and some clinical evidence support this conclusion',
 'b_r_delayed': 'Delayed curing and exponential ramp curing appear to provide the greater reductions in curing stress',
 'b_r_root': 'C-factors can be extremely high, over 1000',
 'b_r_pores': 'the internal pores in chemically cured resins act to relax residual stresses',
})
add('b_crg', {
 'b_s_alone': 'C-factor alone does not accurately predict stresses or clinical longevity in resin composite or glass ionomer restorations',
 'b_s_complex': 'the clinical condition is complex',
 'b_s_depend': 'The stresses depend on the anatomy of the tooth and the geometry of the cavity preparation, the quality of the bonded interface, and the restorative technique used',
 'b_s_deform': 'if the bond is sufficiently strong, cause deformation of the tooth',
 'b_s_lab': 'a prefabricated and indirectly placed laboratory composite is clinically preferred',
})
add('b_sik5', {
 'b_t_isthmus': '2.0 mm isthmus width at the occlusal aspect',
 'b_t_depth': 'No less than 2.0 mm cavity depth at its most shallow point',
 'b_t_taper': '10–12° occlusal taper exiting from the most gingival aspect to the occlusal cavosurface',
 'b_t_round': 'All internal line angles should be rounded',
 'b_t_butt': 'Gingival margins should be a flat butt joint with no bevel',
 'b_t_cusp': 'they will need to be reduced in height by at least 2.0 mm',
 'b_t_nobev': 'Do not provide bevels at the margins, because bevels will lead to fine fragile margins in the resin restoration',
 'b_t_23': 'In case, the isthmus is less than two-third of the intercuspal width, composite is indicated',
})

book('b_Perdigao2019', "Perdigão J, Miguez PA, Swift EJ Jr, Walter R. Fundamental concepts of enamel and dentin adhesion. In: Ritter AV, Boushell LW, Walter R, eds; Gopikrishna V, adaptation ed. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asia ed (from 7th ed, Elsevier 2019). New Delhi: RELX India; 2018. Ch.15 (contributors as listed in the front matter; author order not printed at the chapter head, verify).")
book('b_Donovan2019', "Donovan TE, Oliveira GMS, Ritter AV, Sulaiman TA. Introduction to composite resins. In: Ritter AV, Boushell LW, Walter R, eds; Gopikrishna V, adaptation ed. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asia ed (from 7th ed, Elsevier 2019). New Delhi: RELX India; 2018. Ch.16 (contributors as listed in the front matter; author order not printed at the chapter head, verify).")
book('b_Ritter2019', "Ahmed SN, Boushell LW, Ritter AV, Walter R. Clinical technique for direct composite resin and glass ionomer restorations. In: Ritter AV, Boushell LW, Walter R, eds; Gopikrishna V, adaptation ed. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asia ed (from 7th ed, Elsevier 2019). New Delhi: RELX India; 2018. Ch.19 (contributors as listed in the front matter; cited in text as Ritter et al; author order not printed at the chapter head, verify).")
book('b_Boushell2019', "Boushell LW, Walter R. Fundamentals of tooth preparation and pulp protection. In: Ritter AV, Boushell LW, Walter R, eds; Gopikrishna V, adaptation ed. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asia ed (from 7th ed, Elsevier 2019). New Delhi: RELX India; 2018. Ch.11.")
book('b_Breschi2013', "Breschi L, Ferracane JL, Cadenaro M, Mazzoni A, Hilton TJ. Adhesion to enamel and dentin. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park, IL: Quintessence; 2013. Ch.9.")
book('b_Vargas2013', "Vargas MA, Bergeron C, Murchison DF, Roeters J, Chan DCN. Direct anterior restorations. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park, IL: Quintessence; 2013. Ch.10.")
book('b_Hilton2013', "Hilton TJ, Broome JC. Direct posterior esthetic restorations. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park, IL: Quintessence; 2013. Ch.11.")
book('b_Fasbinder2013', "Fasbinder DJ, Neiva G, Robbins JW. Esthetic inlays and onlays. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park, IL: Quintessence; 2013. Ch.19.")
book('b_Marzouk1985', "Marzouk MA, Simonton AL, Gross RD. Operative Dentistry: Modern Theory and Practice. St Louis/Tokyo: Ishiyaku EuroAmerica; Indian reprint. Ch.9 Cavity and tooth preparations for direct tooth-colored materials (publication year not printed in the extracted file).")
book('b_Mount2016', "Mount GJ, Ngo HC. Principles of cavity design for the restoration of advanced lesions. In: Mount GJ, Hume WR, Ngo HC, Wolff MS, eds. Preservation and Restoration of Tooth Structure. 3rd ed. Chichester: Wiley; 2016. Ch.7.")
book('b_Garg2011', "Garg N, Garg A. Textbook of Preclinical Conservative Dentistry. 1st ed. New Delhi: Jaypee Brothers; 2011. Ch.8 Dental cements; Ch.11 Composite restorations.")
book('b_Singh2020', "Singh H, Rajkumar B. Cavity preparation for composite resin. In: Singh H. Essentials of Preclinical Conservative Dentistry. 2nd ed. Gurgaon: Wolters Kluwer Health (India); 2020. Ch.17 (joint contribution of the author and Rajkumar B).")
book('b_Scotti2020', "Scotti N, Baldi A, Vergano EA, Kubo CH, et al. Composite resins (Ch.13). In: Torres CRG, ed. Modern Operative Dentistry: Principles for Clinical Practice. Cham: Springer Nature; 2020 (full author list and exact chapter title not verified from the extracted file).")
book('b_McCabe2008', "McCabe JF, Walls AWG. Applied Dental Materials. 9th ed. Oxford: Blackwell; 2008. Ch.22 Resin-based filling materials.")
book('b_Anusavice2013', "Anusavice KJ, Shen C, Rawls HR, eds. Phillips' Science of Dental Materials. 12th ed. St Louis: Elsevier Saunders; 2013 (year not printed in the extracted file, verify). Ch.12 Bonding and bonding agents; Ch.13 Resin-based composites.")
book('b_Sakaguchi2019', "Sakaguchi R, Ferracane J, Powers J, eds. Craig's Restorative Dental Materials. 14th ed. St Louis: Elsevier; 2019. Ch.5 Testing of dental materials and biomechanics; Ch.9 Restorative materials: resin composites and polymers.")
book('b_Sikri2017', "Sikri VK. Indirect Restorations in Dental Practice. 2nd ed. New Delhi: CBS Publishers; first eBook edition 2017. Ch.5 Inlays and onlays (no printed page numbers in the extracted file; PDF pages cited).")
