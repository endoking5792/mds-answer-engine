# Group C locators (Q3, Q4: biologic width)
src('c_stu10', OP+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Morelli and Neiva, 2019')
src('c_sum1', OP+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Fruits et al, 2013')
src('c_sum15', OP+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Overton et al, 2013')
src('c_sum18', OP+'Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Rouse, 2013')
src('c_sikri', OP+[x for x in os.listdir(OP) if x.startswith('Indirect_Restorations_Sikri')][0], None, 'Sikri, 2017')
src('c_aod', OP+[x for x in os.listdir(OP) if x.startswith('Advanced_Operative')][0], 2, 'Ricketts, 2011')
add('c_stu10', {
 'c_def': 'combined vertical dimension of the junctional epithelium and the supra-alveolar connective tissue',
 'c_seal': 'acts as a seal around the cervical portion of the tooth and has a self-restoration capacity',
 'c_5days': 'reattaches to the original level in approximately 5 days',
 'c_ctconst': 'the connective tissue zone had the most consistent dimension',
 'c_jevar': 'The junctional epithelium was the most variable area',
 'c_post': 'biologic width was greater in posterior teeth',
 'c_jerest': 'junctional epithelium was significantly longer in teeth with restorations',
 'c_violate': 'leading to gingival inflammation, attachment loss and recession or pocket formation',
 'c_apical': 'can only be restored by apical re-establishment of the supracrestal connective tissue',
 'c_1mm': 'placing a restoration beyond 1 mm into the sulcus is potentially disruptive of the biologic width',
 'c_cldef': 'removal of bone tissue with concomitant removal or repositioning of the soft tissue around the tooth',
 'c_safe': 'an additional 0.5–1 mm should be added coronally to create a safe distance',
 'c_34': 'A 3–4-mm distance from gingival margin to the alveolar crest',
 'c_3min': 'the 3-mm distance is the minimum necessary to avoid periodontal breakdown',
 'c_5mm': 'have suggested to aim for a 5-mm distance from bone to the restorative margin',
 'c_26yr': 'A 26-year prospective study showed a 0.5-mm increased mean loss of attachment',
 'c_thin': 'if the periodontium is thin and scalloped, recession will follow the inflammatory process',
 'c_moat': 'there is a higher likelihood of a moat-like lesion around the tooth',
 'c_furc': 'position of the furcation',
 'c_crratio': 'inadequate crown-to-root ratio after surgery',
 'c_camargo': 'forced tooth eruption via orthodontic extrusion is the technique of choice',
 'c_68wk': 'wait approximately 6–8 weeks before proceeding with final preparation',
 'c_68mo': 'postponing final margin placement and restoration for 6–8 months may be desirable',
 'c_gingx': 'gingivectomy does not involve hard tissue but rather just gingival excess removal',
 'c_regrow': 'the tissue regrows to establish at least approximately 1 mm of junctional epithelium and 1 mm of sulcus',
 'c_3sound': 'at least 3 mm of sound tooth structure are needed from the margin of the final cavity preparation',
 'c_ferrule': '1.5–2 mm of ferrule is necessary for adequate retention',
 'c_kt3': 'Gingivectomy is not advised when the band of keratinized tissue is insufficient',
 'c_distal': 'Distal wedge is commonly performed on the distal surface of molars',
 'c_geri': 'Geristore, which appears to be the preferred material among clinicians',
 'c_prov': 'a well-adapted provisional restoration should always be placed and tissue reaction ideally observed for several weeks',
})
add('c_sum1', {
 'c_s1dgj': 'is termed the dentogingival junction, and their combined vertical dimension is termed the biologic width',
 'c_s1vacek': 'the mean biologic width dimension was 1.91 mm (1.75 mm for anterior teeth and 2.08 mm for posterior teeth)',
 'c_s1gar': 'the biologic width averaged 2.04 mm',
 'c_s13mm': '3.0 mm (2.0 mm biologic width plus an additional 1.0-mm sulcus depth) is a simplified working concept',
 'c_s1prox': 'the dentogingival complex dimension is reported to be in a range of 3.0 to 4.5 mm',
 'c_s1bleed': 'was twice as high for intrasulcular margins as for supragingival margins',
 'c_s1sound': 'the probe penetrates the midfacial sulcus to contact the osseous crest, a process called bone sounding',
 'c_s185': 'In 85% of subjects, a 3.0-mm reading confirms existence of an optimum biologic width',
 'c_s105': 'the preparation margin may be safely placed 0.5 mm below the existing gingival margin',
 'c_s125': 'no closer than 2.5 mm from the osseous',
 'c_s135': 'scalloped as much as 3.5 mm incisal to the level of the facial CEJ',
 'c_s1less3': 'a mucogingival flap and osseous resection (a crown lengthening procedure) is generally recommended',
 'c_s115pc': 'had restoration margins less than 2.0 mm from the osseous crest with no related loss of attachment',
 'c_s1opinion': 'the evidence is primarily based on opinion and anecdotal cases',
 'c_s1nobone': 'there were no signs of either gingival recession or bone resorption',
 'c_s1kg': 'a minimum width of 2.0 mm of keratinized gingiva is required to prevent chronic gingival inflammation',
 'c_s1papilla': 'At a distance of 5.0 mm, 98% of the dental papillae completely filled the restored gingival embrasure',
})
add('c_sum15', {
 'c_s15clamp': 'A no. 212SA clamp is effective for this purpose',
 'c_s15mini': 'The incision(s) should not be extended past the mucogingival junction',
 'c_s15gpl': 'An inadequate zone of attached gingiva is an absolute contraindication for gingivoplasty',
 'c_s15rmgi': 'both soft and hard tissue attachment to glass ionomer or resin-modified glass ionomer (RMGI) does occur',
 'c_s1548': 'the restorations should be placed 4 to 8 weeks after surgery',
 'c_s153mm': 'bone is removed so that 3 mm of root surface separate the bone and the caries lesion',
})
add('c_sum18', {
 'c_rcohen': 'The term biologic width was given to this zone of connective tissue and epithelium by D. Walter Cohen',
 'c_rsound': 'measurements are taken on the midfacial aspect of the tooth and at both facioproximal line angles',
 'c_rnormal': 'the measurement from the free gingival margin to the osseous crest is 3.0 mm facially and 3.0 to 4.5 mm interproximally',
 'c_rn85': 'The normal crest is found on 85% of anterior teeth',
 'c_rnmargin': 'restorative margins can be placed 0.5 to 1.0 mm into the sulcus facially and 0.5 to 2.5 mm interproximally',
 'c_rlow': 'A low crest relationship is the most difficult of all crest positions to manage and is found in 13% of anterior teeth',
 'c_rlowopt': 'internally beveled gingivectomy so that the gingival crest is 3 mm coronal to the osseous crest',
 'c_rhigh': 'Patients with high crests are the least common (2%) and pose the greatest risk for violation of biologic width',
 'c_rhighm': 'will only allow an equigingival or supragingival restorative margin',
 'c_r4req': 'four requirements must be satisfied for effective gingival retraction',
 'c_r02': 'To achieve a crevicular width of 0.2 mm, the secondary cord optimally must remain in the gingival crevice for 4 minutes',
})
add('c_sikri', {
 'c_sk2mm': 'it should terminate at least 2.0 mm above the alveolar crest',
 'c_skinfl': 'produces chronic inflammation, pocket formation and osseous defects',
})
add('c_aod', {
 'c_a05': 'these should not extend deeper than 0.5 mm from the free gingival margin',
 'c_aretr': 'This can be achieved by mechanical retraction, chemomechanical retraction or surgical retraction',
 'c_a02': 'a sulcus width of 0.2 mm or more is required to record the preparation margin accurately',
})
book('c_Morelli2019', "Morelli T, Neiva GF. Periodontology applied to operative dentistry. In: Ritter AV, Boushell LW, Walter R, eds. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed. Elsevier; 2019. Ch.10.")
book('c_Fruits2013', "Fruits TJ, Khajotia SS, Nicholson JW. Biologic considerations. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Quintessence; 2013. Ch.1.")
book('c_Overton2013', "Overton JD, Hilton TJ, LittleStar MR, Starr CB. Class 5 restorations. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry. 4th ed. Quintessence; 2013. Ch.15.")
book('c_Rouse2013', "Rouse JS. Anterior ceramic crowns. In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry. 4th ed. Quintessence; 2013. Ch.18.")
book('c_Sikri2017', "Sikri VK. Textbook of Indirect Restorations (Fixed Partial Dentures and Crowns). CBS Publishers; 2017. Ch.2.")
book('c_Ricketts2011', "Ricketts D. Impressions for indirect restorations. In: Ricketts D, Bartlett D, eds. Advanced Operative Dentistry: A Practical Approach. Elsevier; 2011. Ch.13.")
add('c_stu10', {
 'c_bact': 'allows for bacterial colonization of the area',
 'c_health': 'the epithelial attachment terminates at the apical end of the junctional epithelium',
})
