# Group E locators (Q7, Q8)
src('e_sik', OP+[x for x in os.listdir(OP) if x.startswith('Indirect_Restorations_Sikri')][0], None, 'Sikri, 2017')
add('e_sik', {
 'e_sik_def': 'Gingival retraction is defined as a process of exposing margins when making impressions of the prepared teeth',
 'e_sik_goal': 'The main goal of gingival retraction is to reversibly displace the gingival tissues',
 'e_sik_ind': 'Presence of subgingival caries.',
 'e_sik_ci': 'Poor oral hygiene.',
 'e_sik_methods': 'The principal methods available for gingival retraction are:',
 'e_sik_mech': 'Wooden wedges (used for depressing the inter-proximal gingiva)',
 'e_sik_twill': 'mechanical retraction achieved in 20–30 minutes',
 'e_sik_copper': 'Copper band (slight oversized band filled with modeling wax',
 'e_sik_vaso': 'Epinephrine/nor-epinephrine (vasoconstrictors)',
 'e_sik_alum': 'Alum/aluminium chloride/tannic acid (biological fluid coagulants)',
 'e_sik_epici': 'Patients on P-blockers and antidepressants',
 'e_sik_zncl': 'these agents may cause ulceration and necrosis, when applied for prolonged time',
 'e_sik_colour': 'The color coding indicates relative thickness of cords.',
 'e_sik_axial': 'The ends of cords should fall at axial angles of the tooth',
 'e_sik_double': 'After 8–10 minutes, the second cord is soaked in water and removed.',
 'e_sik_recoil': 'thus reducing the tendency of gingival cuff to recoil',
 'e_sik_curett': "The technique is also known as ‘gingitage’ and is used where adequate gingiva is present and the sulcular depth is less than 3.0 mm.",
 'e_sik_gvect': 'For crown lengthening procedures.',
 'e_sik_esdef': 'Electrosurgical method is defined as the surgical reduction of sulcular epithelium by using electrode of high frequency.',
 'e_sik_esrule': 'Use fully rectified, undamped current with minimum energy output.',
 'e_sik_metal': 'Metallic restorations should not be touched',
 'e_sik_pace': 'Avoid electrosurgery in patients with pacemaker.',
 'e_sik_misc': 'The newer agents used to achieve effective gingival retraction are:',
 'e_sik_foam': 'Magic foam is the expanding vinyl polysiloxane material',
 'e_sik_expasyl': 'this pressure is sufficient to achieve 0.5 mm of gingival retraction',
 'e_sik_laser': 'Lasers work through photo-ablation and produce blood-free incisions',
 'e_sik_ferric': 'Ferric sulphate is considered better haemostatic agent than epinephrine',
 'e_sik_thin': 'Use in thin gingiva may result in recession.',
})
SUMF=OP+[x for x in os.listdir(OP) if x.startswith('Summitts')][0]
src('e_sum15', SUMF, None, 'Overton et al, 2013')
src('e_sum18', SUMF, None, 'Rouse, 2013')
add('e_sum15', {
 'e_sum_212': 'A no. 212SA clamp is effective for this purpose',
 'e_sum_compound': 'Modeling compound is the traditional stabilizing material used',
 'e_sum_overhang': 'Finishing short is almost certainly superior to placing an overhanging restoration',
 'e_sum_miniflap': 'The incision(s) should not be extended past the mucogingival junction.',
 'e_sum_nosuture': 'Sutures are usually not necessary.',
 'e_sum_gplasty': 'An inadequate zone of attached gingiva is an absolute contraindication for gingivoplasty.',
 'e_sum_3mmag': 'If gingivoplasty would result in less than 3 mm of attached gingiva adjacent to the restoration',
 'e_sum_flap': 'If restorations on two adjacent teeth are to be placed simultaneously and both require a surgical procedure',
 'e_sum_timing': 'the restorations should be placed 4 to 8 weeks after surgery',
})
add('e_sum18', {
 'e_sum_4req': 'four requirements must be satisfied for effective gingival retraction',
 'e_sum_methods': 'They include mechanical, mechanical-chemical, rotary curettage, electrosurgery, and laser surgery (troughing).',
 'e_sum_popular': 'The mechanical-chemical technique, the most popular retraction technique today',
 'e_sum_alsulf': 'Aluminum sulfate is one of the least irritating of the retraction chemicals.',
 'e_sum_02': 'No detectable difference in distortion of impressions of preparations was found with sulcular widths of 0.2 mm or greater.',
 'e_sum_4min': 'the secondary cord optimally must remain in the gingival crevice for 4 minutes',
 'e_sum_lowcrest': 'Rotary curettage, electrosurgery, and laser troughing are definitely contraindicated in low-crest patients.',
 'e_sum_wet': 'The secondary cord should be removed wet to prevent renewed hemorrhage.',
 'e_sum_ferric': 'A disadvantage to the use of ferric compounds is that they inhibit the setting of polyether impression materials.',
 'e_sum_normal': 'the measurement from the free gingival margin to the osseous crest is 3.0 mm facially and 3.0 to 4.5 mm interproximally',
 'e_sum_low': 'A low crest relationship is the most difficult of all crest positions to manage',
 'e_sum_high': 'Gingival retraction for impressions should be minimal.',
 'e_sum_replace': 'Chemical agents and secondary cord should be replaced and the retraction attempted again.',
 'e_sum_latex': 'Latex gloves may inhibit the set of polyvinyl siloxane.',
})
src('e_stu', OP+'Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter et al, 2019')
add('e_stu', {
 'e_stu_212': 'The use of a No. 212 cervical retainer for restoration of Class V tooth preparations was recommended by Markley.',
 'e_stu_modified': 'A modified No. 212 retainer is recommended, especially for treatment of cervical lesions with greatly extended gingival margins.',
 'e_stu_dull': 'Sharp tips on a No. 212 retainer should be sufficiently dulled to prevent damaging cementum.',
 'e_stu_cord': 'retraction cord, usually moistened with a noncaustic haemostatic agent',
 'e_stu_abrasion': 'helps prevent abrasion of gingival tissue during tooth preparation',
 'e_stu_blanch': 'without causing tissue ischaemia secondary to pressure from the cord',
 'e_stu_early': 'Inserting the cord as early as possible in tooth preparation helps prevent abrasion of the gingival tissue',
 'e_stu_wedge': 'snugly inserted into the gingival embrasures from the facial or lingual embrasure',
})
src('e_gold', OP+[x for x in os.listdir(OP) if x.startswith('Esthetics_in_Dentistry_Goldstein')][0], 28, 'Goldstein et al, 2018')
add('e_gold', {
 'e_gold_five': 'Five common methods for the preparation of soft tissues are retraction cord, paste systems, conventional electrosurgery, bipolar technique, and diode lasers.',
 'e_gold_damage': 'Improper methods can permanently damage the epithelial attachment, causing gingival recession',
})
book('E_Sikri2017', 'Sikri VK. Indirect Restorations (Textbook of Operative Dentistry). New Delhi: CBS Publishers; 2017.')
book('E_Summitt2013', "Overton JD, Hilton TJ, LittleStar MA, Starr CB (Ch.15) and Rouse JS (Ch.18). In: Hilton TJ, Ferracane JL, Broome JC, eds. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Chicago: Quintessence; 2013.")
book('E_Ritter2019', "Ritter AV, Boushell LW, Walter R, eds. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asia ed. New Delhi: Elsevier; 2019.")
book('E_Goldstein2018', "Goldstein RE, Powers JM, Lee EA. Impressions. In: Goldstein RE, Chu SJ, Lee EA, Stappert CFJ, eds. Ronald E. Goldstein's Esthetics in Dentistry. 3rd ed. Hoboken: Wiley; 2018.")
