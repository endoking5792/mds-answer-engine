# Group E locators: cavosurface treatment, bevels, flares, finish lines, rounded line angles (Q06, Q07, Q09, P2)
MZ = OP+'Operative_Dentistry_Marzouk.md'
STU = OP+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md'
SUM = OP+'Summitts_Fundamentals_of_Operative_Dentistry.md'
HS = OP+'Essentials_of_Preclinical_Conservative_Dentistry_Harpreet_Singh.md'
NG = OP+'Textbook_of_Preclinical_Conservative_Dentistry.md'
SK = OP+'Textbook_of_Conservative_and_Restorative_Dentistry.md'

src('e_mz1', MZ, 4, 'Marzouk et al, undated')     # Ch 1 Principles of operative dentistry
src('e_mz5', MZ, 3, 'Marzouk et al, undated')     # Ch 5 Class I cavity preparation for amalgam
src('e_mz9', MZ, 1, 'Marzouk et al, undated')     # Ch 9 Preparations for direct tooth-colored materials
src('e_mz17', MZ, -1, 'Marzouk et al, undated')   # Ch 17 Cast restorations; Ch 18 Designs of preparations for cast restorations
src('e_st7', STU, 19, 'Boushell and Donovan, 2019')
src('e_st11', STU, 19, 'Boushell and Walter, 2019')
src('e_st19', STU, 19, 'Ahmed et al, 2019')
src('e_st23', STU, 19, 'Sturdevant JR, 2019')
src('e_su1', SUM, None, 'Fruits, Khajotia and Nicholson, 2013')
src('e_su10', SUM, None, 'Vargas et al, 2013')
src('e_su11', SUM, None, 'Hilton and Broome, 2013')
src('e_su12', SUM, None, 'Overton, Summitt and Osborne, 2013')
src('e_su15', SUM, None, 'Overton et al, 2013')
src('e_su18', SUM, None, 'Rouse, 2013')
src('e_su19', SUM, None, 'Fasbinder, Neiva and Robbins, 2013')
src('e_su20', SUM, None, 'Fan, Stevenson and Berry, 2013')
src('e_hs', HS, 17, 'Singh, 2020')
src('e_ng', NG, 7, 'Garg and Garg, 2011')
src('e_sk', SK, 19, 'Sikri, 2020')

add('e_mz1', {
 'e_mz_csmargin': 'The surface periphery of the cavity preparation, which is the junction between the cavity wall (floor) and the adjacent tooth surface is the cavosurface margin.',
 'e_mz_csangle': 'This refers to the angle between a wall (floor) and the adjacent tooth surface.',
 'e_mz_noy1': 'The enamel wall must rest upon sound dentin',
 'e_mz_noy2': 'The enamel rods which form the cavosurface angle must have their inner ends resting on sound dentin',
 'e_mz_noy3': 'This provides the strongest wall possible but it can only be produced by a bevel of the cavosurface angle.',
 'e_mz_noy3b': 'The first situation can only be applied when the restorative materials are stronger and tougher than tooth structure.',
 'e_mz_noy3c': 'The second situation is the maximum that can be expected when the restorative material is weaker and more brittle than the tooth structure.',
 'e_mz_noy4': 'The cavosurface angle must be so trimmed or bevelled that the margins will not be exposed to injury in condensing the restorative material against it',
 'e_mz_amalgamex': 'not all materials can perform well if placed in a cavity with such enamel walls. The primary example is amalgam.',
 'e_mz_roundenamel': 'Junctions between different enamel walls should be very rounded, even if the junctions between the inner parts of the wall (dentinal) are angular.',
 'e_mz_roundenamel2': 'in addition to decreasing stress concentration there.',
 'e_mz_roundfrail': 'rounding decreases the possibility of any frail, unsupported, easily detachable enamel rods at the corners.',
 'e_mz_roundadapt': 'This will improve adaptability of the restorative material at the preparation corners',
 'e_mz_rods36': 'making an average of plus 36°',
 'e_mz_flareconv': 'flaring some walls more than otherwise necessary for resistance or retention form in order to decrease distortion errors in intermediate materials during restoration fabrications (castings)',
})
add('e_mz5', {
 'e_mz_amalbutt': 'All cavosurface angles should be right-angled to create a butt-joint with the marginal amalgam.',
 'e_mz_amalbutt2': 'This configuration allows marginal amalgam to withstand stresses with the least possibility of failure',
 'e_mz_amalrods': 'when a cavity wall or its external plane follows the direction of the enamel rods, this right-angled configuration occurs',
 'e_mz_amalround': 'All line and point angles, or any junction between different details in the cavity preparation, should be rounded but definite',
 'e_mz_amalround2': 'while avoiding stress concentration in the tooth structure and restorative materials that may occur from sharp angulations',
})
add('e_mz9', {
 'e_mz_cpartial': 'This should involve about',
 'e_mz_cpartial2': 'It is always used when the cavity preparation’s internal anatomy and walls can adequately retain the restoration, and acid conditioning is used only to reduce marginal leakage.',
 'e_mz_clong': 'In this design feature, the entire enamel wall is bevelled at 45-70° to the cavity wall.',
 'e_mz_cflash': 'Both shapes have the distinct disadvantage of having no definite marginal termination, especially after acid treatment.',
 'e_mz_cflash2': 'Also, this marginal flash will occur in a weak acute-angled cross-section.',
 'e_mz_cnot': 'do not use design features (1) or (2) in uncleansable areas, stress concentration areas (direct loading), inaccessible areas, and/or next to the periodontium.',
 'e_mz_chollow': 'about two-thirds of the enamel wall thickness is ground in a concave manner so the cavity margin will have a right angled cavosurface angle, with butt joint between the restorative material and the marginal enamel.',
 'e_mz_chollow2': 'The hollow ground bevel is indicated for inaccessible areas',
 'e_mz_cscallop': 'Under no circumstances should scalloping be used for gingival walls or inaccessible portions of any wall margin.',
 'e_mz_cskirt': 'This feature is used if conditioned enamel will be the main retentive mode for resinous material.',
})
add('e_mz17', {
 'e_mz_circtie': 'C. Preparation features of the circumferential tie',
 'e_mz_weaklink': 'is the tooth/cement/cast joint complex.',
 'e_mz_onlycast': 'Cast restorations are the only restorations',
 'e_mz_beveldef': 'which is a plane of a cavity wall or floor directed',
 'e_mz_sixtypes': 'there.are six types of bevels:',
 'e_mz_partial': 'This involves part of the enamel wall, not exceeding',
 'e_mz_short': 'This includes the entire enamel wall, but not dentin.',
 'e_mz_short2': 'bevel is used mostly with Class I alloys specially for type 1',
 'e_mz_long': 'This includes all of the enamel wall and up to one-half of',
 'e_mz_long2': 'This is the most frequently used bevel for',
 'e_mz_full': 'This includes all of the dentinal and enamel walls of the',
 'e_mz_full2': 'Its use should be avoided except in',
 'e_mz_counter': 'When capping cusps to protect and support them, this type',
 'e_mz_hollow': 'All of the aforementioned types of bevels are in the form of',
 'e_mz_hollow2': 'These bevels are ideal for Class IV and V cast',
 'e_mz_func1': 'bevels create obtuse-angled marginal tooth structure,',
 'e_mz_func2': 'which is the bulkiest and the strongest configuration of any',
 'e_mz_func3': 'Marginal bevels reduce the error factors (space between cast',
 'e_mz_func4': 'Bevels are the ‘‘flexible extensions”’ of a cavity preparation,',
 'e_mz_func5': 'can bring the gingival margins to cleansable or protected areas.',
 'e_mz_flaredef': 'flat or concave peripheral portions of the facial and lingual',
 'e_mz_primflare': '45° to the inner dentinal wall proper.',
 'e_mz_primflare2': 'The primary flare (Fig. 6) is the conventional and basic',
 'e_mz_secflare': 'The secondary flare (Fig. 6) is almost always a flat',
 'e_mz_secflare2': 'may have different angulations, involvement and extent',
 'e_mz_chamfer': 'The chamfer finishing line (Fig 8A) is the most',
 'e_mz_chamfer2': 'ginally, with little tooth involvement (0.5 mm maximal depth).',
 'e_mz_knife': 'is the circumferential tie constituent with the least tooth',
 'e_mz_knife2': 'very castable-burnishable type of alloy (gold alloys, preferably',
 'e_mz_bevshoulder': 'circumferential tie constituent with the most tooth structure',
 'e_mz_bevshoulder2': 'ideal design for subgingivally located margins, because of the',
 'e_mz_hgfinish': 'tually an exaggerated chamfer or a concave bevelled shoulder.',
 'e_mz_tieround': 'be prepared without sharp angles or interruptions, thereby',
 'e_mz_tieround3': 'avoiding stress concentration, noncoverage of the margin by',
 'e_mz_tieround2': 'the level of the circumferential tie, i.e., not internally.',
 'e_mz_smooth': 'tie portion should be the smoothest.',
 'e_mz_reverse': 'This is placed at the expense of the gingival floor, creating',
 'e_mz_reverse2': 'an internal dentinal plane inclining gingivally-axially, locking',
 'e_mz_reverse3': 'with cast ceramics.',
 'e_mz_classIV': 'Nickel-chromium based alloys.',
 'e_mz_classV': 'Castable, moldable ceramics.',
 'e_mz_occbev': 'angulation of 30-45° to the long axis of the crown (or the wall',
 'e_mz_occbevwide': 'This angulation should increase as the width of the',
 'e_mz_steep': 'The angulation of the bevel should decrease with increased',
 'e_mz_steep2': 'all in very steep cusps (especially in a very narrow preparation),',
 'e_mz_direct': 'An increased bevel angulation is necessary, also, for a direct',
 'e_mz_apround': 'the axial wall should, flares should not be used if a direct wax pattern technique is',
 'e_mz_apround2': 'meet the pulpal floor in an extremely rounded junction as in',
 'e_mz_apround3': 'amalgam. This prevents stress concentration in the tooth and',
 'e_mz_gingbev': 'half should be bevelled in the form of a long bevel inclining',
 'e_mz_gingbev2': '30-45° to the wall proper. However, this angulation can be',
 'e_mz_gingbev3': 'versely proportional to this bevel’s angulation.',
 'e_mz_cer90': 'minating in a 90° cavosurface margin. Although this might',
 'e_mz_ivround': 'be more rounded.',
 'e_mz_ivhollow': 'flares, occlusal or gingival bevels) should be hollow-ground to',
 'e_mz_ivparallel': 'less taper. This compensates for the loss of retention',
 'e_mz_vround': 'meet surrounding walls in very rounded line angles.',
 'e_mz_counterangle': 'standard as that for the occlusal bevel. It is measured by the',
 'e_mz_counterangle2': 'axis of the crown. On the average, this angulation is from 30',
 'e_mz_ceramround': 'they should not have definite internal line angles.',
 'e_mz_retform': 'are one of the major retention forms for a cast',
 'e_mz_friction': 'possibility of a direct retentive frictional component between',
 'e_mz_full3': 'it deprives the preparation of its internal',
 'e_mz_long3': 'that it preserves the internal',
 'e_mz_partial2': 'except to trim weak enamel rods from margin',
 'e_mz_secflare3': 'Usually it is prepared solely in',
 'e_mz_secind1': 'In very broad contact areas or malposed contact areas, the',
 'e_mz_secind2': 'In ovoid teeth peripheral marginal undercuts are especially',
 'e_mz_knife3': 'possibility of indefinite termination for the casting',
 'e_mz_chamfer3': 'It is contraindicated, however, for Class IV',
 'e_mz_bevshoulder3': 'It can be used for any class of cast materials.',
 'e_mz_pfdefinite': 'The pulpal floor should meet all surrounding walls',
 'e_mz_pfround': 'where the joint should be very rounded.',
 'e_mz_retain': 'require greater occlusal reduction and rounded internal and',
})
add('e_st7', {
 'e_st_hatchet': 'sharpening internal line angles, particularly in preparation for direct gold restorations.',
 'e_st_angleformer': 'It is used primarily for sharpening line angles and creating retentive features in dentin in preparation for gold restorations.',
 'e_st_gmt': 'Indirect gold restorations require the placement of a distinct bevel associated with the gingival walls',
 'e_st_gmt2': 'bevelling (blunting or rounding) of the axiopulpal line angle of two-surface preparations so as to limit areas of stress concentration in subsequently placed restorations.',
})
add('e_st11', {
 'e_st_angles': 'This transition area from one surface to another is designed to be smooth and rounded, rather than abrupt or sharp, to limit stress concentration.',
 'e_st_intangle': 'An internal line angle is the line angle whose apex points into the tooth.',
 'e_st_csdef': 'The cavosurface angle is the angle of tooth structure formed by the junction of a prepared wall and the external surface of the tooth.',
 'e_st_csvaries': 'or the type of restorative material to be used.',
 'e_st_outline': 'Restorative materials that need bevelled margins require tooth preparation outline form extensions that must anticipate the final cavosurface position and form after the bevels have been placed.',
 'e_st_rounded1': 'the internal line angles) are slightly rounded so as to limit stress concentration in these areas, which increases tooth resistance to fracture.',
 'e_st_rounded2': 'which increases resistance to fracture of the restorative material.',
 'e_st_bevcast': 'The bevels for cast-metal restorations are used primarily to afford a better junctional relationship between the metal and the tooth.',
 'e_st_bevcomp': 'may utilize a bevelled or flared (>90 degrees) configuration so as to increase the retention form of the preparation',
 'e_st_finishdef': 'Finishing the external preparation walls is the further development, when indicated, of a specific design',
 'e_st_occcontact': 'occlusal contact directly on the marginal interface will result in early fatigue and failure of the margin.',
 'e_st_90support': 'Enamel walls that form a 90-degree angle with the cavosurface may be considered to have dentinal support and to be strong',
 'e_st_root': 'the root surface cavosurface angle should be either 90 degrees (for amalgam, composite or ceramic restorations) or bevelled (for intra-coronal cast-metal restorations).',
 'e_st_soften': 'should be slightly curved (softened)',
 'e_st_90amal': 'Because of the low-edge strength of amalgam and glass–ceramic, a 90-degree cavosurface angle produces maximal strength for these materials.',
 'e_st_90amal2': 'Bevelling a cavosurface margin would result in a thin, fracture',
 'e_st_occamal': 'even though the actual occlusal enamel margin may be greater than 90 degrees',
 'e_st_bevgold': 'bevelling will result in the strongest type of enamel margin.',
 'e_st_bevgold2': 'it may allow a better marginal seal in slightly undersized castings',
 'e_st_burnish': 'a thin gold margin is more readily burnished and adapted to the preparation margin.',
 'e_st_bevcomp2': 'indicated primarily for large restorations that have increased retention needs and insufficient amount of prepared enamel for proper retention.',
 'e_st_bevcomp3': 'Increases the surface area available for bonding, which increases the retention form of the preparation.',
 'e_st_bevcomp4': 'area of gradual increase in composite thickness from the margin to the bulk of the restoration.',
})
add('e_st19', {
 'e_st_noocc': 'No bevels are placed on the occlusal cavosurface margins because these walls already have exposed enamel rod ends.',
 'e_st_finish': 'Bevelled composite margins also may be more difficult to finish.',
 'e_st_prox': 'Bevels are rarely used on any of the proximal box walls',
 'e_st_ging': 'Bevels also are not recommended along the gingival margins of the proximal box',
 'e_st_clIII45': 'The bevel is prepared by creating a 45-degree angle to the external surface and to a width of 0.5–2 mm',
 'e_st_clIIIfacial': 'an enamel bevel is used on the facial cavosurface margin to provide a gradual colour transition',
 'e_st_lingcontra': 'a bevel on the lingual enamel margin of a maxillary incisor may be contraindicated',
 'e_st_clIV': 'The operator bevels the cavosurface margin of all accessible enamel margins of the preparation.',
 'e_st_clV': 'at the cervical margin, bevels are usually not recommended because of the absence of enamel in this area.',
 'e_st_gicrare': 'except bevels are rarely used.',
 'e_st_flared': 'preparations typically result in more flared cavosurface forms',
 'e_st_pear': 'they result in strong, 90-degree cavosurface margins without creating sharp internal line angles.',
})
add('e_st23', {
 'e_st_271': 'meet in a slightly rounded manner so that sharp, stress-inducing internal angles are not formed in the preparation.',
 'e_st_concept': 'results in a 30–40 degree marginal metal on the inlay',
 'e_st_concept2': 'results in a strong enamel margin with an angle of 140–150 degrees.',
 'e_st_occwidth': 'should be approximately one-fourth the depth of the respective wall',
 'e_st_40metal': 'should be 40 degree metal; the occlusal marginal enamel is 140 degree enamel',
 'e_st_apwax': 'Such a bevel provides a thicker and stronger wax pattern at this critical region.',
 'e_st_mridge': 'The margins on the proximal marginal ridges always require a cavosurface bevel',
 'e_st_apbevel': 'The diamond instrument is used to bevel the axiopulpal line angle lightly',
 'e_st_metal40': 'The desirable metal angle at the margins of inlays is always 40 degrees except at the gingival margins, where the metal angle should be 30 degrees.',
 'e_st_flaredefs': 'The first flare that brings the proximal preparation out of the contact area is termed lingual primary flare',
 'e_st_150': 'A cavosurface enamel angle of more than 150 degrees is incorrect because it results in a less defined enamel margin',
 'e_st_140': 'the metal is too bulky and difficult to burnish when its angle is greater than 40 degrees',
 'e_st_gingwidth': 'The gingival bevel should be 0.5–1 mm wide and should blend with the lingual secondary flare.',
 'e_st_lap': 'A lap, sliding fit is produced at the gingival margin',
 'e_st_secflare': 'making these margins more self-cleaning and more accessible to finishing procedures',
 'e_st_esth': 'For esthetic reasons, minimal flare is desired for the mesiofacial proximal wall in maxillary premolars and first molars',
 'e_st_counter': 'A reverse bevel or counterbevel is a bevel of generous width, which is prepared on the facial (lingual) margin of a reduced cusp',
 'e_st_counter30': 'It should be at an angle that results in 30 degree marginal metal.',
 'e_st_weak': 'Weak enamel is removed',
 'e_st_flare40': 'The direction of the flare results in 40 degree marginal metal',
 'e_st_skirt': 'Skirts are thin extensions of the facial or lingual proximal margins of the cast metal onlay',
 'e_st_collar': 'lightly bevelling the gingival margin of the shoulder with the flame-shaped, fine-grit diamond instrument to achieve a 30 degree metal angle at the margin',
 'e_st_onlayround': 'any sharp junctions between the counterbevels and the secondary flares are rounded slightly',
})
add('e_su1', {
 'e_su_end': 'Resin bond strengths are twice as high when adhering to the acid-etched ends of the crystals as compared with the sides of the crystals.',
 'e_su_45': 'a tangential cut or bevel of approximately 45 degrees across a 90-degree cavosurface angle of a prepared cavity will expose the ends of the rods',
 'e_su_occex': 'An exception is on occlusal surfaces, where beveling would extend tapering resin margins into areas of increased stress.',
 'e_su_craze': 'stress development due to polymerization shrinkage has led to reports of enamel microcracks and crazing at margins.',
 'e_su_gapdefect': 'Fracture dislodgment of the enamel rods that form the cavity wall or cavosurface margin of a dental restoration creates a gap defect.',
 'e_su_plane': 'planing the cavosurface margin with hand instruments or low-speed rotary instruments to remove any friable or fragile enamel structure is recommended as a finishing step.',
})
add('e_su10', {
 'e_su_bevadv': 'Bevels have been advocated by some authors to reduce enamel fracture and provide a gradual shade transition for esthetics.',
 'e_su_nobev': 'However, enamel bonds have been demonstrated clinically to be adequate without bevels.',
 'e_su_leak': 'revealed no significant differences in marginal microleakage in Class 3 restorations whether or not margins were beveled.',
 'e_su_rmgi': 'Preparations for these materials should resemble those for resin composite, but bevels are not prepared.',
 'e_su_rmgibond': 'Because these materials bond to enamel and dentin, the placement of retention grooves or points is',
 'e_su_1mm': 'Increasing the width of the bevel beyond 1 mm has been shown to provide no additional strength',
 'e_su_facial60': 'This bevel has a 60-degree angulation and is 2 to 3 mm in length.',
 'e_su_lingual45': 'The bevel starts at the DEJ and has a 45-degree angulation',
 'e_su_chamferload': 'A deeper bevel or a chamfer is prepared in areas exposed to occlusal loads',
})
add('e_su11', {
 'e_su_controv': 'Bevel placement is a point of controversy with this preparation.',
 'e_su_prox05': 'conservative bevels (0.5 mm) should be placed at an approximately 45-degree angle to the surface',
 'e_su_proxleak': 'Research has demonstrated that bevels on these margins significantly reduce marginal leakage.',
 'e_su_gingbev': 'The gingival margin should be beveled only if the margin is in enamel well away from the cementoenamel junction',
 'e_su_inverse': 'has been shown to significantly reduce microleakage as compared to a butt margin',
 'e_su_occno': 'The use of occlusal cavosurface margin bevels is not indicated.',
 'e_su_occsave': 'prevents the loss of sound tooth structure',
 'e_su_occwear': 'posterior resin composite restorations placed in cavities with beveled occlusal margins had significantly greater wear than those placed with occlusal butt margins.',
})
add('e_su12', {
 'e_su_amal90': 'enamel margins should be prepared at a right angle or slightly obtuse angle (90 degrees or greater)',
 'e_su_ditch': 'Marginal fracture will usually cause marginal gaps, or ditches, between the amalgam and the enamel.',
 'e_su_survival': 'Clinical research has shown that clinical survival of amalgam restorations is inversely related to the degree of unsupported enamel.',
 'e_su_amalfin': 'very acute amalgam margins are much more subject to fracture',
})
add('e_su15', {
 'e_su_cl5bev': 'Cavosurface bevels are contraindicated in preparations for amalgam or glass ionomer because of the low edge strength of these materials.',
 'e_su_gic': 'Cavosurface bevels are not recommended for the preparation because glass ionomer is a brittle material that requires bulk for strength.',
 'e_su_gic1mm': 'A 90-degree butt joint approximately 1 mm deep is a reasonable minimum thickness.',
 'e_su_cl5ext': 'the preparation should be extended only to remove carious tooth structure and fragile enamel',
 'e_su_cemno': 'Beveling the gingival margin that ends on cementum is not recommended.',
})
add('e_su18', {
 'e_su_ceramcrown': 'gingival line angle with a butt-joint external cavosurface margin.',
})
add('e_su19', {
 'e_su_cerround': 'the internal angles should be rounded to enhance adaptation of the restorative material.',
 'e_su_cerno': 'There is no benefit to the placement of bevels at the occlusal or gingival margins;',
 'e_su_cerchip': 'thin margins of both resin composite and most ceramics are susceptible to chipping during function.',
 'e_su_cer45': 'The cavosurface margin is modified with a football-shaped diamond at a 45-degree angle to the cavosurface margin',
 'e_su_cervitro': 'An in vitro study on ceramic preparations for conservative restoration of endodontically treated teeth',
 'e_su_cadcam': 'All cavosurface margins should be well defined and have a 90-degree',
})
add('e_su20', {
 'e_su_finishdef': 'The term finish line refers to the border of the preparation where the prepared tooth structure meets the unprepared surface of the tooth.',
 'e_su_types': 'The most common types of finish lines for cast restorations are knife-edged, chamfer, and shoulder.',
 'e_su_noagree': 'According to a dental survey, there is no agreement on the ideal finish line.',
 'e_su_gap': 'a gap between 39 and 120 μm may be considered acceptable.',
 'e_su_math': 'However, this was based on mathematical models that did not take cement thickness into account.',
 'e_su_ostlund': 'beveling beyond 45 degrees significantly increases the cement-filled opening',
 'e_su_steeper': 'the steeper the bevel angle, the larger the vertical discrepancy (opening) between the edge of the casting and the finish line.',
 'e_su_shoulderfit': 'crowns with a shoulder finish line configuration had better marginal fit than did those with a beveled finish line configuration.',
 'e_su_knife': 'Generally, a knife-edged finish line is not desirable because it is more difficult than other finish lines to discern on a die',
 'e_su_chamfer': 'A chamfer is often the preferred finish line for cast gold extra-coronal restorations.',
 'e_su_shoulder': 'The shoulder finish line is used primarily when a bulk of material is needed to strengthen the restoration at the margins',
 'e_su_shoulder2': 'It also has the most critical fit, because there is no bevel present on the restoration that can be burnished',
 'e_su_bevprox': 'A bevel is recommended for proximal boxes.',
 'e_su_bevcrown': 'for full cast crowns, the bevel can increase the risk of encroachment on the epithelial attachment.',
 'e_su_inlay05': 'occlusal, proximal, and gingival bevels along the entire cavosurface finish line',
 'e_su_inlay45': 'The bevels should be at an angle of approximately 45 degrees to the external surface of the tooth.',
 'e_su_defined': 'internal angles should be well defined',
 'e_su_relieved': 'This assumes that the casting is fully relieved, allowing minimum cement thickness.',
 'e_su_factors': 'Factors such as existing taper, die relief',
 'e_su_knifeuse': 'the configuration is commonly used on the mesial aspect of a mesially tipped molar, on the lingual aspects of mandibular molars',
 'e_su_knifeover': 'tends to result in overcontoured restorations.',
 'e_su_chamfercons': 'It is more conservative than a shoulder finish line',
 'e_su_precise': 'Internal angles are precise, occlusal line angles are rounded',
})
add('e_hs', {
 'e_hs_def': 'Bevels are flexible extensions of a cavity preparation allowing the inclusion of surface defects',
 'e_hs_def2': 'a bevel may also be described as any abrupt incline between the two surfaces of prepared tooth or between the cavity wall and the cavosurface margins in the prepared cavity.',
 'e_hs_six': 'there are six types of bevels, namely:',
 'e_hs_counter13': 'It is usually one-third of the height of the clinical crown.',
 'e_hs_140': 'Bevels create obtuse-angled 140°–150° marginal tooth structures',
 'e_hs_3040': 'They also produce an acute-angled 30°–40° marginal metal wall, which can be easily burnished and adapted.',
 'e_hs_threefold': 'The error factor (space between cast restoration and tooth) is reduced threefold or more',
 'e_hs_primflare': 'The primary flare is at 45° to the inner dentinal wall proper.',
 'e_hs_tablebutt': 'A butt joint is given at the cavosurface margin (90°).',
 'e_hs_tablebev': 'Bevels are given at the cavosurface margin.',
 'e_hs_tableround': 'Line angles and point angles are rounded.',
 'e_hs_tabledef': 'Line angles and point angles are well defined.',
 'e_hs_variants': 'box preparation, slice preparation, auxil',
 'e_hs_comp': 'On bevelling, ends of enamel rods are more effectively etched producing deeper micro-undercuts than when only the sides of enamel rods are etched.',
 'e_hs_compocc': 'the thin layer of the composite that is applied over the bevel (if given) would chip off',
 'e_hs_compext': 'The bevel is 0.25- to 0.5-mm wide and is at a 45° angle to the prepared wall',
})
add('e_ng', {
 'e_ng_def': 'Bevel is defined as the inclination that one surface makes with another when not at right angles.',
 'e_ng_3035': 'Objective of bevel is to form a metal wedge of 30° to 35°',
 'e_ng_140150': 'strong enamel margin with an angle of 140° to 150° can be produced.',
 'e_ng_135': 'Resultant cavosurface angle of 135° to 140° forms the strongest and the bulkiest configuration.',
 'e_ng_3545': 'Acute angled metal margins (35°-45°) allow the metal margins to be burnished against tooth surface',
 'e_ng_primflare': 'It is like a long bevel and is always directed 45° to the inner dentinal wall proper',
 'e_ng_ultra': 'Ultrashort or partial bevel',
 'e_ng_hollow': 'Hollow ground is concave in shape and not a bevel in true sense.',
 'e_ng_hollow2': 'It is rarely used.',
 'e_ng_revant': 'It is beveling in the reverse or inverted shape given on the gingival seat in the axial wall toward the root in anterior teeth.',
 'e_ng_revpost': 'it is used to prevent tipping of cast restoration and to increase the resistance and retention form.',
 'e_ng_edge': 'The types of margin of tooth preparation depends mainly on the compressive strength, edge strength and tensile strength of the restorative material.',
 'e_ng_ging45': 'It is advantageous to place a gingival bevel of approximately 45° to inlay preparations',
 'e_ng_ginghalf': 'The gingival bevel should include one-half the width of the gingival wall.',
 'e_ng_gingover': 'Gingival bevels more than 45° results in over extension of the gingival and proximal margins',
 'e_ng_occ40': 'It is suggested that the occlusal bevel should be about 40° beginning at the occlusal one-third of the adjacent occlusal walls',
 'e_ng_secesth': 'Secondary flare is not given in the areas where esthetics is more important.',
 'e_ng_amalbutt': 'If cavosurface angle is acute, enamel margins may fracture under load. But if cavosurface angle is obtuse, marginal amalgam may fracture under masticatory stresses',
 'e_ng_compangle': 'Avoid sharp internal line angles in tooth preparation, which increases stress concentration',
})
add('e_sk', {
 'e_sk_partial': 'Such type of preparation is indicated in direct filling gold restorations',
 'e_sk_short': 'This type of bevel is preferred in cast gold restorations',
 'e_sk_inverted': 'It is given on the labial shoulder of metal ceramic crowns to effectively improve the esthetics at the margins',
 'e_sk_reverse': 'This effect is resisted by the reverse bevel resulting in even seating of the cast restoration.',
 'e_sk_friction': 'bevels decrease the direct frictional component between the tooth and the casting.',
 'e_sk_oldflare': 'later it was found that flaring of the walls right from axiofacial or axiolingual line angles till the cavosurface margin did not alter the retention and resistance form.',
 'e_sk_secgold': 'created exclusively for gold inlay preparations',
 'e_sk_nolonger': 'The modified preparations, such as box only preparation, slice preparation and modified flare preparation, are no longer used.',
 'e_sk_shoulderind': 'Provide bulk of restorative',
})

book('e_Marzouk1985', "Marzouk MA, Simonton AL, Gross RD. Operative Dentistry: Modern Theory and Practice. St Louis/Tokyo: Ishiyaku EuroAmerica (Indian reprint: AITBS Publishers). (publication year not printed in the extracted file)")
book('e_Boushell2019a', "Boushell LW, Donovan TE. Instruments and equipment for tooth preparation. In: Ritter AV, Boushell LW, Walter R, eds. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed (Gopikrishna V, adaptation ed). Elsevier; 2019. Ch 7.")
book('e_Boushell2019b', "Boushell LW, Walter R. Fundamentals of tooth preparation and pulp protection. In: Ritter AV, Boushell LW, Walter R, eds. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed (Gopikrishna V, adaptation ed). Elsevier; 2019. Ch 11.")
book('e_Ahmed2019', "Ahmed SN, Boushell LW, Ritter AV, Walter R. Clinical technique for direct composite resin and glass ionomer restorations. In: Ritter AV, Boushell LW, Walter R, eds. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed. Elsevier; 2019. Ch 19.")
book('e_SturdevantJR2019', "Sturdevant JR. Class II cast metal restorations. In: Ritter AV, Boushell LW, Walter R, eds. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed. Elsevier; 2019. Ch 23.")
book('e_Fruits2013', "Fruits TJ, Khajotia SS, Nicholson JW. Biologic considerations. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Quintessence; 2013. Ch 1.")
book('e_Vargas2013', "Vargas MA, Bergeron C, Murchison DF, Roeters J, Chan DCN. Direct anterior restorations. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry. 4th ed. Quintessence; 2013. Ch 10.")
book('e_Hilton2013', "Hilton TJ, Broome JC. Direct posterior esthetic restorations. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry. 4th ed. Quintessence; 2013. Ch 11.")
book('e_Overton2013a', "Overton JD, Summitt JB, Osborne JW. Amalgam restorations. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry. 4th ed. Quintessence; 2013. Ch 12.")
book('e_Overton2013b', "Overton JD, Hilton TJ, LittleStar ML, Starr CB. Class 5 restorations. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry. 4th ed. Quintessence; 2013. Ch 15.")
book('e_Rouse2013', "Rouse JS. Anterior ceramic crowns. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry. 4th ed. Quintessence; 2013. Ch 18.")
book('e_Fasbinder2013', "Fasbinder DJ, Neiva G, Robbins JW. Esthetic inlays and onlays. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry. 4th ed. Quintessence; 2013. Ch 19.")
book('e_Fan2013', "Fan PP, Stevenson R, Berry TG. Cast gold restorations. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry. 4th ed. Quintessence; 2013. Ch 20.")
book('e_Singh2020', "Singh H. Essentials of Preclinical Conservative Dentistry. 2nd ed. New Delhi: Wolters Kluwer (India); 2020.")
book('e_Garg2011', "Garg N, Garg A. Textbook of Preclinical Conservative Dentistry. 1st ed. New Delhi: Jaypee Brothers; 2011.")
book('e_Sikri2020', "Sikri VK. Textbook of Conservative and Restorative Dentistry. New Delhi: CBS Publishers; 2020 (first eBook edition).")
