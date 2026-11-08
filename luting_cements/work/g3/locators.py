import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
F = {
 'cr':  (T+'Operative_and_Dental_Materials_Textbooks/Craigs_Restorative_Dental_Materials.md', 11, 'Braga, 2019'),
 'ph':  (T+'Operative_and_Dental_Materials_Textbooks/Phillips_Science_of_Dental_Materials.md', 16, 'Anusavice et al, undated'),
 'vn':  (T+'Operative_and_Dental_Materials_Textbooks/Introduction_to_Dental_Materials_4th.md', 15, 'van Noort, 2013'),
 'pw':  (T+'Operative_and_Dental_Materials_Textbooks/Powers_Wataha_Dental_Materials_Properties_and_Manipulation.md', 12, 'Powers and Wataha, 2013'),
 'cm':  (T+'Operative_and_Dental_Materials_Textbooks/Restorative_Dental_Materials_Craig_Michigan_11th.md', 9, 'Craig and Powers, 2002'),
 'sik': (T+'Operative_and_Dental_Materials_Textbooks/Indirect_Restorations_Sikri.md', None, 'Sikri, 2017'),
 'stu': (T+'Operative_and_Dental_Materials_Textbooks/Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter et al, 2019'),
 's17': (T+'Operative_and_Dental_Materials_Textbooks/Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Rouse and Robbins, 2013'),
 's18': (T+'Operative_and_Dental_Materials_Textbooks/Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Rouse, 2013'),
 's19': (T+'Operative_and_Dental_Materials_Textbooks/Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Fasbinder et al, 2013'),
 's20': (T+'Operative_and_Dental_Materials_Textbooks/Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Fan et al, 2013'),
 's21': (T+'Operative_and_Dental_Materials_Textbooks/Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Broome and Robbins, 2013'),
 's9':  (T+'Operative_and_Dental_Materials_Textbooks/Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Breschi et al, 2013'),
 'ap2': (T+'Operative_and_Dental_Materials_Textbooks/Adhesive_Techniques_in_Restorative_Dentistry_Alani_Patel.md', 20, 'Alani and Patel, 2025'),
 'ap6': (T+'Operative_and_Dental_Materials_Textbooks/Adhesive_Techniques_in_Restorative_Dentistry_Alani_Patel.md', 23, 'Alani and Patel, 2025'),
 'ap9': (T+'Operative_and_Dental_Materials_Textbooks/Adhesive_Techniques_in_Restorative_Dentistry_Alani_Patel.md', 24, 'Alani and Patel, 2025'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
#   Pick clean text: avoid OCR ligature damage ("0e", "!le"), hyphen breaks and figure captions.
L = {
 # ---- Craig 14e Ch.13 (Braga)
 'cr_def': ('cr', 'Resin cements are low-viscosity composite materials with filler distribution and initiator content adjusted to allow for a low film thickness'),
 'cr_range': ('cr', 'from inlays to fixed bridges, prefabricated posts, and orthodontic appliances'),
 'cr_mandatory': ('cr', 'They are mandatory materials for luting low-strength ceramic and laboratory-processed composite restorations'),
 'cr_extraret': ('cr', 'particularly in cases where extra retention is needed'),
 'cr_iso': ('cr', 'classifies resin cements according to curing mode as class 1 (self-cured), class 2 (light-cured), or class 3 (dual-cured)'),
 'cr_mostdual': ('cr', 'Most of the commercial products are dual-cured, combining chemical- and light-activation mechanisms'),
 'cr_lightveneer': ('cr', 'Light-cured materials are indicated for bonding of laminated ceramic veneers (esthetic cements) or orthodontic brackets'),
 'cr_tryin': ('cr', 'glycerin-based, water-soluble'),
 'cr_monomers': ('cr', 'molecular-weight molecules such as Bis-GMA'),
 'cr_teg': ('cr', 'to achieve a high degree of conversion with a relatively low volumetric shrinkage'),
 'cr_filler': ('cr', 'The filler fraction may vary between 30% and 66% by volume'),
 'cr_fillertype': ('cr', 'silanated radiopaque glasses such as barium, strontium, or zirconia, along with silica particles'),
 'cr_mdp': ('cr', 'One example combines MDP, a polymerizable phosphoric acid ester, with Bis-GMA'),
 'cr_4meta': ('cr', 'and tri-n-butylborane as catalyst'),
 'cr_cq': ('cr', 'Camphorquinone and a tertiary amine are present in one of the pastes to initiate the light-activated reaction'),
 'cr_bpo': ('cr', 'Benzoyl peroxide, the self-cure activator, is present in the catalyst paste'),
 'cr_aminedeg': ('cr', 'amines are known to degrade over time, altering the shade of the cement'),
 'cr_amineacid': ('cr', 'they become inactive when in contact with acidic adhesive systems'),
 'cr_setting': ('cr', 'Resin cements set by free-radical polymerization, resulting in the formation of a densely cross-linked polymer structure surrounding the filler particles'),
 'cr_redox': ('cr', 'In the absence of light, free radicals are formed by redox reaction of the amine-peroxide system'),
 'cr_dc70': ('cr', 'Final degree of conversion is around 70%'),
 'cr_dcdual': ('cr', 'Conversion is usually higher in cases where the cement is dual-cured, compared to self-cured'),
 'cr_cs': ('cr', 'Compressive strengths of dual- and light-cured resin composite cements have been reported from 180 to 300 MPa'),
 'cr_fs': ('cr', 'Flexural strength is between 80 and 100 MPa'),
 'cr_mod': ('cr', 'being between 4 and 10 GPa'),
 'cr_film': ('cr', 'Film thicknesses measured according to ISO standards are between 13 and 20'),
 'cr_sorp': ('cr', 'Water sorption and solubility of resin cements are much lower than those of resin-modified glass ionomer cements'),
 'cr_discol': ('cr', 'the cement line may become apparent after a prolonged period of clinical use because of discoloration'),
 'cr_shrink': ('cr', 'Shrinkage of resin cements varies between 2% and 5%'),
 'cr_sbs': ('cr', 'Immediate shear bond strength of resin cements to dentin varies between 12 and 18 MPa'),
 'cr_mdpbond': ('cr', 'MDP can bond to tooth structures, ceramics, and cast alloys by the reaction between its phosphate groups and calcium or with metal oxides'),
 'cr_stress': ('cr', 'When stresses at the interface surpass the bond strength of the adhesive layer to dentin or enamel, debonding and the formation of a contraction gap may occur'),
 'cr_cyto': ('cr', 'Monomers released from resin cements are known to produce cytotoxic effects on mammalian cells'),
 'cr_better': ('cr', 'resin cements have better mechanical properties than acid-base cements, but the cementation process is more technique sensitive'),
 'cr_nosingle': ('cr', 'Different clinical situations require different luting agents and no one material is indicated for every case'),
 'cr_excess': ('cr', 'removal of excess cement also needs to be done before setting'),
 'cr_esthetic': ('cr', 'Resin cements are the most esthetic luting materials available'),
 'cr_needadh': ('cr', 'Resin cements require the use of adhesive systems to establish a strong bond to dentin and enamel'),
 'cr_solub': ('cr', 'Resin-based cements present much lower solubility than acid-base cements'),
 'cr_sandblast': ('cr', 'Sandblasting with aluminum oxide is the most commonly used method to prepare metal substrates'),
 'cr_tin': ('cr', 'Tin plating can be used to improve the retention of noble alloys to resin cements'),
 'cr_basemetal': ('cr', 'They seem to be more effective with base-metal alloys, compared to noble alloys'),
 'cr_hfsilane': ('cr', 'Silica-based ceramics have been successfully bonded to resin cements by etching the restoration'),
 'cr_hfglass': ('cr', 'Hydrofluoric acid attacks the glass phase of ceramics'),
 'cr_zrnohf': ('cr', 'zirconia is a polycrystalline material with no amorphous silica glass component'),
 'cr_zrmdp': ('cr', 'The most widely used monomer in zirconia primers is 10-MDP'),
 'cr_zrop': ('cr', 'stable Zr–O–P bonds on the zirconia surface'),
 'cr_fibrese': ('cr', 'The use of self-etching adhesives systems is not indicated, because their acidity would impede the chemical activation of the resin cement'),
 'cr_fibresa': ('cr', 'has shown promising results in laboratory evaluations'),
 'cr_fibremoist': ('cr', 'it is virtually impossible to control moisture inside the root canal'),
 # self-adhesive (Craig)
 'cr_sadef': ('cr', 'incorporates the etching, priming, and bonding chemistry in a single material'),
 'cr_sagen': ('cr', 'The first generation of this class of products was supplied as powder-liquid formulations'),
 'cr_sagen2': ('cr', 'The newer generations are provided as two-paste systems that can be automixed through a static mixer'),
 'cr_saindic': ('cr', 'These materials are indicated for cementation of cast alloy single restorations and bridges, ceramic-metal crowns and bridges, ceramic (except veneers), and indirect composite restorations'),
 'cr_saposts': ('cr', 'Good results are also obtained with luting of prefabricated posts and high-strength ceramics'),
 'cr_saacid': ('cr', 'one or more acid-functional monomer whose role is to etch the tooth tissue while bonding to other monomers to build up cohesive strength'),
 'cr_saphos': ('cr', 'Most commercial products contain polymerizable monomers based on phosphates and phosphonates'),
 'cr_samon': ('cr', '2-methacryloxyethyl phenyl hydrogen phosphate (Phenyl-P), 10-MDP'),
 'cr_sacarb': ('cr', 'monomers with carboxylic acid groups such as 4-META and pyromellitic glycerol dimethacrylate'),
 'cr_saglass': ('cr', 'a small amount of an acid-neutralizing filler such as fluoroaluminosilicate glass'),
 'cr_safill': ('cr', 'The total filler content of the mixed cement is about 70% by mass (approximately 50% by volume)'),
 'cr_sacure': ('cr', 'The primary curing mechanism is via free-radical polymerization, either self-activated or dual-cured'),
 'cr_saph2': ('cr', 'The initial pH of the mixed cement is about 2 so that it can provide etching of the tooth mineral'),
 'cr_saca': ('cr', 'the acidic groups (phosphate and carboxylate) can bind with calcium in the hydroxyapatite'),
 'cr_saneut': ('cr', 'the remaining acidity is neutralized in some cements by the reaction between phosphoric and carboxylic acid groups and the alkaline glass'),
 'cr_sastruct': ('cr', 'Some ionic bridging between carboxylic groups and ions released by the glass may also be present'),
 'cr_sacyto': ('cr', 'self-adhesive resin cements present higher cytotoxicity than resin cements and acid-base cements'),
 'cr_salower': ('cr', 'in general, are somewhat lower than those of conventional resin cements'),
 'cr_sasens': ('cr', 'the low incidence of postoperative sensitivity reported with these products'),
 'cr_sasens2': ('cr', 'the dentin does not need to be etched with phosphoric acid'),
 'cr_saprops': ('cr', 'Flexural strength is in the 50 to 100 MPa range and compressive strength is between 200 and 240 MPa'),
 'cr_safilm': ('cr', 'Film thickness is between 15 and 20'),
 'cr_samech': ('cr', 'micromechanical interlocking and chemical interaction between the acidic groups and the hydroxyapatite'),
 'cr_saenamel': ('cr', 'Initial shear bond strength to enamel varies from 3 to 15 MPa, intermediate between resin cements and glass ionomers'),
 'cr_saetch': ('cr', 'If substantial enamel margins are present, it is often recommended to etch with phosphoric acid even while using these cements'),
 'cr_sametal': ('cr', 'They show good bond strength values to metal alloys and high-strength ceramics'),
 'cr_sawater': ('cr', 'The presence of unreacted acid groups increases water sorption'),
 'cr_saf': ('cr', 'the release of fluoride ions decreases rapidly with time'),
 'cr_saf2': ('cr', 'The beneficial effects of fluoride in the self-adhesive resin cements have not been clinically proven'),
 # ---- Phillips 12e
 'ph_lowvisc': ('ph', 'Resin cements are low-viscosity versions of restorative com'),
 'ph_insol': ('ph', 'These cements are virtually insoluble in oral fluids'),
 'ph_dba': ('ph', 'A dentin bonding agent is needed to promote the'),
 'ph_4meta': ('ph', 'The 4-META−containing cements do not need a separate bonding'),
 'ph_era': ('ph', 'etch-and-rinse adhesive resin cement or as a self-etch'),
 'ph_sanostep': ('ph', 'for which no extra clinical step is necessary for bonding'),
 'ph_sainfil': ('ph', 'Self-adhesive resin cements do not show significant infiltration into dentin'),
 'ph_saenamel': ('ph', 'In vitro studies have reported better enamel bonding performance for non'),
 'ph_sapulp': ('ph', 'these cements showed no adverse pulp response according to one study'),
 'ph_choice': ('ph', 'For cementation of all-ceramic restorations, resin cement is the material of choice'),
 'ph_saveneer': ('ph', 'The exception would be cementation of veneers, in which case a light-cured cement would be preferred'),
 'ph_sadual': ('ph', 'Self-adhesive resin cements are dual-cured materials and can be used for cementation of indirect restorations in most clinical situations'),
 'ph_ortho': ('ph', 'Self-adhesive cements are not recommended by manufac'),
 'ph_ortho2': ('ph', 'cements exhibit a lower bond strength to intact enamel in comparison with conventional orthodontic'),
 'ph_sadef': ('ph', 'Ability of a material to adhere to tooth structure without the aid of a dentin or enamel bonding agent'),
 'ph_pendant': ('ph', 'These cement systems rely on modified dimethac'),
 'ph_mostdual': ('ph', 'The majority of resin cements today are of the dual-cure variety'),
 'ph_lightveneer': ('ph', 'it is used for cementing porcelain veneers'),
 'ph_liner': ('ph', 'tection with a liner is important when the thickness of the remaining dentin is less than 0.5 mm'),
 'ph_chemall': ('ph', 'Chemically cured resin cements are suitable for all types of restorations'),
 'ph_25': ('ph', 'anything thicker than 2.5 mm should be bonded with chemical-cure cement'),
 'ph_tab': ('ph', 'Resin 2.0–4.0 <25 70–172 40–77 2.1–3.1 0–0.01 Moderate'),
 'ph_eugenol': ('ph', 'Residual free eugenol interferes with the proper setting of resin-based composites or resin cements'),
 'ph_basemetal': ('ph', 'Oxide formation on the base metal surfaces contributes to the bond strength when resin cement containing MDP or a 4-META-based resin is used'),
 'ph_ceramicchoice': ('ph', 'choice for all-ceramic inlays, crowns, and bridges because of their ability to reduce fracture of the ceramic structures'),
 'ph_zrnoetch': ('ph', 'Etching and silanization are not effective with ceramics that do not contain silica, such as alumina and zirconia-based ceramics'),
 # ---- van Noort 4e
 'vn_three': ('vn', 'Aesthetic light-/dual-cure composite resin cements'),
 'vn_three2': ('vn', 'Adhesive chemical/dual-cure resin cements'),
 'vn_three3': ('vn', 'Self-adhesive dual-cure resin cements'),
 'vn_aesthetic': ('vn', 'These resins are based on conventional composite resin technology and have no intrinsic adhesive capabilities'),
 'vn_adhesive': ('vn', 'to bond chemically to suitably prepared metal surfaces without the need for any adhesion promoter'),
 'vn_panavia': ('vn', 'an example of this type of resin is Panavia 21'),
 'vn_sanopre': ('vn', 'no pretreatment of the tooth surface is required, yet at the same time claiming to be able to establish a bond to base metal alloys and a range of ceramics'),
 'vn_unicem': ('vn', 'a specially synthesized monomer having two phosphoric acid groups and two C=C double bonds'),
 'vn_ph2': ('vn', 'with a very low pH of around 2.0'),
 'vn_ionic': ('vn', 'react with the calcium ions (Ca2+) in the enamel and dentine, and form an ionic bond'),
 'vn_neutral': ('vn', 'the pH in the body of the resin cement rapidly increases to a neutral level, with the added benefit of fluoride ion release'),
 'vn_gpdm': ('vn', 'GPDM (glycerol dimethacrylate dihydrogen phos'),
 'vn_amine': ('vn', 'the alkaline amines used in self-cure systems become inactive in an acidic environment'),
 'vn_propr': ('vn', 'each of the products will have their own proprietary acid-resistant amine/peroxide system'),
 'vn_posts': ('vn', 'These luting resins have become particularly popular for the cementation of posts (including fibre posts)'),
 'vn_noveneer': ('vn', 'One application for which the self-adhesive resins are not recommended is the bonding of ceramic veneers'),
 'vn_enamel': ('vn', 'the bond to enamel is not as good as can be achieved with the etch-and-rinse and self-etching'),
 'vn_ortho': ('vn', 'these luting resins are not considered suitable for the bonding of orthodontic brackets'),
 'vn_hygro': ('vn', 'can also lead to fracture of all-ceramic crowns. The problem is made even more serious if RMGIC is also used as a core material'),
 'vn_rmgicpost': ('vn', 'the removal of posts cemented with an RMGIC can be extremely difficult'),
 'vn_rmgiccontra': ('vn', 'The use of RMGICs for the cementation of all-ceramic restorations would appear to be contraindicated'),
 'vn_dualinlay': ('vn', 'visible light curing resins may not cure properly when they are used to bond large inlays'),
 # ---- Powers & Wataha 10e
 'pw_cast': ('pw', 'Cementation of cast alloy crowns and bridges Adhesive resin (dual cured), glass ionomer, resin-modified glass ionomer, self-adhesive resin, zinc polycarboxylate'),
 'pw_inlay': ('pw', 'Cementation of all-ceramic or indirect composite inlays and onlays Adhesive resin (dual cured)'),
 'pw_zr': ('pw', 'Cementation of zirconia-based, all-ceramic crowns and bridges Adhesive resin (dual cured), glass ionomer, resin-modified glass ionomer, self-adhesive resin'),
 'pw_veneer': ('pw', 'Cementation of ceramic veneers Esthetic resin (dual cured or light cured)'),
 'pw_rbb': ('pw', 'Cementation of resin-bonded bridges Adhesive resin (dual cured)'),
 'pw_esth': ('pw', 'These cements require a bonding agent for adhesion to tooth structure and separate primers for bonding to ceramic substrates'),
 'pw_adh': ('pw', 'Adhesive resin cements are used for bonding of most alloy and ceramic restorations'),
 'pw_adh20': ('pw', 'are high (>20 MPa) when these surfaces are treated with a primer'),
 'pw_gel': ('pw', 'Some adhesive resin cements require a gel barrier to exclude oxygen for complete setting'),
 'pw_said': ('pw', 'Self-adhesive resin cements eliminate the need for separate primers for bonding to tooth, alloy, or ceramic substrates'),
 'pw_sacomp': ('pw', 'Self-adhesive resin cements are composed of diacrylate res'),
 'pw_salow': ('pw', 'Self-adhesive resin cements bond to tooth structure and other materials with low to medium bond strengths'),
 'pw_salight': ('pw', 'Properties measured when these cements are light activated are generally higher than when they are self-cured'),
 'pw_microfill': ('pw', 'microfilled resin cements are more wear resistant than microhybrid resin cements'),
 # ---- Craig 11e (Michigan)
 'cm_1952': ('cm', 'Synthetic resin cements based on methyl meth'),
 'cm_1952b': ('cm', 'acrylate have been available since 1952'),
 'cm_1970': ('cm', 'In the early 1970s, a resin composite was intro'),
 'cm_oxygen': ('cm', 'The phosphonate mol'),
 'cm_rbb': ('cm', 'Adhesive resin cements have superior bonding to sandblasted Ni-Cr-Be and Type IV gold alloys'),
 # ---- Sikri 2e
 'sik_hist': ('sik', 'Because of high polymerization shrinkage, tendency for pulpal irritation, microleakage and poor handling qualities'),
 'sik_metal': ('sik', 'The chemically activated or auto-polymerizing systems (Panavia, C & B Metabond) are suited for luting of metal restorations'),
 'sik_oxygen': ('sik', 'The polymerization of Panavia is strongly retarded by oxygen, which facilitates removal of excess resin'),
 'sik_dualmicro': ('sik', 'Less microhardness of dual-cured luting cements have been reported, especially within first twenty-four hours when light curing was omitted'),
 'sik_inaccess': ('sik', 'indicated for restorations having inaccessible margins'),
 'sik_veneer': ('sik', 'For veneers or translucent crowns, autocure or dual-cure resin cements should be avoided'),
 'sik_ptol': ('sik', 'Certain substances like para-toluidine necessary for chemical cure causes a measurable color change over a period of time'),
 'sik_adv1': ('sik', 'Low film thickness Better compressive and tensile strength Lowest solubility Compatible with esthetic restorations Controlled working time'),
 'sik_dis': ('sik', 'Disadvantages Postoperative sensitivity. Procedure is technique sensitive.'),
 'sik_dissol': ('sik', 'The dissolution of resin cement is minimum, followed by glass-ionomer cements, polycarboxylate cements and zinc phosphate cement'),
 'sik_wear': ('sik', 'The wear resistance of almost all cements is less than that'),
 'sik_tilt': ('sik', 'The resin cements, because of their higher viscosity, may lead to tilting of castings'),
 'sik_radio': ('sik', 'The auto-polymerizing resins are less radiopaque than dentin'),
 'sik_clin': ('sik', 'Glass-ionomer cements are more effective for base metals; resin cements have shown promising results with composite/ceramic restorations'),
 'sik_cleaning': ('sik', 'comparatively easier than glass-ionomers, composites and dual-cure cements'),
 'sik_highTS': ('sik', 'It is recommended that the cement with a high tensile strength be used to cement crowns and long span bridges'),
 # ---- Sturdevant 2e SA
 'stu_def': ('stu', 'have the same general components as composite restorative materials but generally have slightly lower con'),
 'stu_best': ('stu', 'These materials have the best laboratory properties of all cements but require more complicated clinical procedures'),
 'stu_allceram': ('stu', 'These materials are reserved almost exclusively for use with all-ceramic restorations'),
 'stu_saself': ('stu', 'These cements have components similar to those used in self-etching dentin primers'),
 'stu_oxide': ('stu', 'have become very popular to cement oxide–based ceramic restorations'),
 'stu_sapre': ('stu', 'that do not require any pretreatment of the tooth substrate'),
 'stu_saetch': ('stu', 'The acidic phosphate groups react with the filler and simultaneously etch enamel or dentin in the same manner as do SEAs'),
 'stu_sachem': ('stu', 'but this interaction depends of the activation mode and the specific self-adhesive resin cement tested'),
 'stu_ph': ('stu', 'The pH of some self-adhesive cements increases from 1 to 5 or 6 during their acid-base setting reaction'),
 'stu_salight': ('stu', 'the physical properties improve significantly when light activated'),
 'stu_saglass': ('stu', 'lower bond strengths to etched glass–matrix ceramics than traditional resin cements'),
 'stu_dualnot': ('stu', 'Some materials marketed as dual cure may not polymerize efficiently in the absence of a curing light'),
 'stu_postsr': ('stu', 'self-adhesive resin cements may improve the retention of glass fibre posts into the root canal'),
 'stu_postsealing': ('stu', 'better sealing ability than conventional adhesive systems'),
 'stu_cfactor': ('stu', 'the estimated C-factor in the root canal may exceed 200'),
 'stu_zrmdp': ('stu', 'adhesion to zirconia is increased after mechanical and chemical surface pretreatment and the use of a 10-MDP-based resin cement'),
 'stu_glassHF': ('stu', 'etched internally with ∼5%–∼10% hydrofluoric acid (HF) for 20– 180 s'),
 'stu_zrHF': ('stu', 'HF etching does not improve bond strengths to oxide-based or polycrystalline ceramics'),
 'stu_film': ('stu', 'The actual film thickness that is achieved ranges from 50–100'),
 # ---- Summitt 4e
 's18_three': ('s18', 'etch-and-rinse and self-etching adhesives and self-adhesive cements'),
 's18_dualcure': ('s18', 'This necessitates the use of dual-curing resin luting agents to ensure that the cement will polymerize with limited light exposure'),
 's18_alwayslight': ('s18', 'resin materials should always be light cured, because any light exposure will enhance the degree of conversion'),
 's18_ER': ('s18', 'This technique provides the highest cement-to-tooth bond but requires the most steps and has the greatest risk of field contamination'),
 's18_SAweak': ('s18', 'The self-adhesive systems have a weak acid etchant, primer, and adhesive incorporated into the cement, appreciably reducing the risk of contamination'),
 's18_SAvary': ('s18', 'The bond strengths vary notably between systems'),
 's18_SAenamel': ('s18', 'the etchant is not appropriate for enamel preparations'),
 's18_SAlose': ('s18', 'Some self-adhesive resin cements demonstrate high strength at baseline but lose strength dramatically over the first few months'),
 's18_znp': ('s18', 'Classically, zinc phosphate was the cement of choice'),
 's18_alt': ('s18', 'Today, alternatives provide increased compressive strength and limited marginal dissolution'),
 's18_dynamic': ('s18', 'This technique, called dynamic seating, results in more complete seating of the crown'),
 's17_light': ('s17', 'Light curing allows a longer working time, shorter finishing time, and superior color stability'),
 's17_colour': ('s17', 'It is advisable to avoid using a dual-curing resin luting cement'),
 's19_dual': ('s19', 'any adhesive agent that will cure in conjunction with a dual-cured resin luting agent can be selected'),
 's20_ret': ('s20', 'also with the use of a resin-based cement combined with surface treatments'),
 's21_metal': ('s21', 'Both zinc phosphate and glass ionomer have been commonly employed because of their ease of use and their history of clinical success'),
 's21_friction': ('s21', 'Traditional cements provide retention for the post primarily through a frictional effect'),
 's21_trend': ('s21', 'Recent trends are toward adhesive cementation of metallic posts, as well as FRC posts, with resin cement'),
 's21_cojet': ('s21', 'the bond of resin cement has been shown to be improved by air abrasion and by the use of tribochemical coating'),
 's21_ER': ('s21', 'The overwhelming majority of FRC posts in clinical studies were cemented using an etch-and-rinse technique'),
 's21_SAless': ('s21', 'they are generally less effective than etch-and-rinse systems'),
 's21_SAlimit': ('s21', 'the lack of long-term clinical data limit the application of recently marketed self-etching and self-adhesive materials'),
 's21_superficial': ('s21', 'self-etching and self-adhesive cements exhibit a superficial interaction with root canal dentin'),
 's9_posts': ('s9', 'the recently formulated self-adhesive cements, which are all-in-one resin-based materials'),
 # ---- Alani & Patel 2025
 'ap2_dual': ('ap2', 'If there is concern over the depth of cure to activate polymerisation of the resin cement, a dual-cure resin cement may be used'),
 'ap2_paste': ('ap2', 'the higher filler load in the composite resin restorative paste will provide a'),
 'ap2_gold': ('ap2', 'Alloy 10-MDP primer application, air dry 6. Resin cement load Chrome'),
 'ap2_chrome': ('ap2', '(nickel or cobalt)'),
 'ap2_glass': ('ap2', '5% or 9.5% HF acid etch (10, 20 or 60 s)'),
 'ap2_silane': ('ap2', 'Silane application (60 s), air dry'),
 'ap2_zr': ('ap2', 'Ceramic 10-MDP primer application (60 s), air dry 5. Resin cement load'),
 'ap2_fibre': ('ap2', 'Silane (60 s if post- not pre-silanated), air dry'),
 'ap6_post': ('ap6', 'The root canal should be coated with a dual-cure adhesive agent and air dried'),
 'ap6_tip': ('ap6', 'requires an elongated delivery tip that will fill the apical portion of the prepared post space first'),
 'ap9_opaque': ('ap9', 'Opaque coloured resin cements are advised in all circumstances where metal alloy framework alloys are used'),
 'ap9_cure': ('ap9', 'Both chemical-cure and dual-cure resin cements can be used'),
 'ap9_50': ('ap9', 'alumina blasted with 50 micron alumina particles'),
}
def norm(s):
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
