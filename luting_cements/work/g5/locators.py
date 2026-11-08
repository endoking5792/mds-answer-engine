import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
F = {
 'stu': (T+'Operative_and_Dental_Materials_Textbooks/Sturdevants_Art_and_Science_of_Operative_Dentistry_2e_South_Asian.md', 19, 'Ritter et al, 2019'),
 'fan': (T+'Operative_and_Dental_Materials_Textbooks/Summitts_Fundamentals_of_Operative_Dentistry.md', None, 'Fan et al, 2013'),
 'mar': (T+'Operative_and_Dental_Materials_Textbooks/Operative_Dentistry_Marzouk.md', -3, 'Marzouk et al, undated'),
 'sik': (T+'Operative_and_Dental_Materials_Textbooks/Indirect_Restorations_Sikri.md', None, 'Sikri, 2017'),
 'cr14': (T+'Operative_and_Dental_Materials_Textbooks/Craigs_Restorative_Dental_Materials.md', 11, 'Sakaguchi et al, 2019'),
 'crm': (T+'Operative_and_Dental_Materials_Textbooks/Restorative_Dental_Materials_Craig_Michigan_11th.md', 9, 'Craig and Powers, 2002'),
 'phi': (T+'Operative_and_Dental_Materials_Textbooks/Phillips_Science_of_Dental_Materials.md', 16, 'Anusavice et al, undated'),
 'mcc': (T+'Operative_and_Dental_Materials_Textbooks/Applied_Dental_Materials_McCabe_Walls_9th.md', 9, 'McCabe and Walls, 2008'),
 'bhat': (T+'Operative_and_Dental_Materials_Textbooks/Science_of_Dental_Materials.md', 56, 'Bhat et al, 2019'),
 'adm': (T+'Operative_and_Dental_Materials_Textbooks/Advanced_Dental_Metallic_Materials.md', 19, 'Rudolf et al, 2024'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
#   Pick clean text: avoid OCR ligature damage ("0e", "!le"), hyphen breaks and figure captions.
L = {
 # ---- Sturdevant 2e SA Ch.23 Class II cast metal restorations (try-in, cementation)
 's_throat': ('stu', 'should be placed as a throat screen to catch the casting if it is accidentally dropped'),
 's_noforce': ('stu', 'Do not force the casting on the tooth.'),
 's_overcontour': ('stu', 'If the casting does not seat completely, the most likely cause is an overcontoured proximal surface.'),
 's_floss': ('stu', 'of the contacts is best judged with dental floss'),
 's_artic': ('stu', 'inserts a strip of articulating paper and requests the patient to close and tap the teeth together'),
 's_burnish': ('stu', 'With a ball or beaver-tail burnisher, the operator improves marginal adaptation by burnishing the marginal'),
 's_explorer': ('stu', 'the explorer tip can pass across the margins smoothly without jumping or catching'),
 's_isolate': ('stu', 'Before cementing the casting, the tooth is isolated from saliva with the aid of cotton rolls'),
 's_mix': ('stu', 'applied generously to the preparation side of the casting'),
 's_ball': ('stu', 'exerting firm pressure to seat the casting'),
 's_disk': ('stu', 'places a small flexible rubber polishing disk over the casting'),
 's_fewsec': ('stu', 'A few seconds of this pressure is sufficient.'),
 's_burnsoft': ('stu', 'While the cement is still soft, all accessible margins are burnished.'),
 's_excess': ('stu', 'After the cement has hardened, any excess is cleaned off with an explorer'),
 's_line': ('stu', 'a cement line should not be visible at the margins'),
 # ---- Summitt 4e Ch.20 Cast gold restorations (Fan, Stevenson, Berry)
 'f_spacer': ('fan', 'use of several layers of die spacer can increase the retention of cemented crowns and improve the fit of cemented restorations'),
 'f_shiny': ('fan', 'Any area that binds during intraoral seating of the casting creates a bright, burnished mark.'),
 'f_disclose': ('fan', 'Disclosing media include chloroform and rouge, disclosing pastes or waxes'),
 'f_passive': ('fan', 'The casting should fit passively in place. A tight fit usually means the casting is not fully seated.'),
 'f_spacer2': ('fan', 'painted onto the die to within 0.5 to 1.0 mm of the finish line prior to wax-pattern fabrication'),
 'f_disk': ('fan', 'The stone or disk should be rotated from the metal to the tooth or parallel to the margin, but never from tooth to gold.'),
 'f_burnishcem': ('fan', 'burnishing the margins of the casting on the tooth during the cementation procedure, before the cement sets'),
 'f_failure': ('fan', 'most important factor in the failure of cast restorations'),
 'f_fills': ('fan', 'The luting agent fills the gap between the casting and the tooth to provide retention and to minimize leakage at the margin.'),
 'f_zpfric': ('fan', 'such as zinc phosphate cement, provide retention entirely from frictional resistance to displacement'),
 'f_resinrmgi': ('fan', 'resin cements or resin-modified glass-ionomer cements provide superior retention and have better physical properties than more traditional cements'),
 'f_nocomp': ('fan', 'no cement will compensate for inadequate preparation resistance and retention form in the long term'),
 'f_zp100': ('fan', 'zinc phosphate has the longest record (more than 100 years) of successful use'),
 'f_slab': ('fan', 'mixed on a glass slab that has been chilled'),
 'f_string': ('fan', 'form a 1-inch string when the spatula is lifted from the glass slab'),
 'f_90': ('fan', 'The mixing should be completed within 90 seconds after initiation.'),
 'f_gicfilm': ('fan', 'Glass-ionomer luting cement has a low film thickness (20 to 25'),
 'f_gicmoist': ('fan', 'Glass-ionomer cement is very sensitive to early moisture contamination.'),
 'f_gic5': ('fan', 'Excess cement should not be removed from the margins for at least 5 minutes after the crown is seated.'),
 'f_rmgi': ('fan', 'Resin-modified glass-ionomer cements have physical and mechanical properties between those of conventional glass-ionomer and resin cements'),
 'f_chem': ('fan', 'for cast restorations, chemically cured cements are indicated'),
 'f_resinfilm': ('fan', 'so incomplete seating of the casting could be a problem'),
 'f_tooth': ('fan', 'Temporary cements leave a layer of debris on the dentin surface'),
 'f_varnish': ('fan', 'Copal varnish has a long history of use for this purpose'),
 'f_gicprep': ('fan', 'the tooth should be clean and slightly moist'),
 'f_airabr': ('fan', 'the internal surface of the casting should be air abraded with aluminum oxide to produce a uniform, slightly roughened finish'),
 'f_margins': ('fan', 'Margins must be avoided or protected when the internal surface is air abraded.'),
 'f_tin': ('fan', 'additional retention can be obtained by tin plating the inside of the casting'),
 'f_primer': ('fan', 'the use of an adhesive system that has an alloy primer'),
 'f_half': ('fan', 'The casting should be half-filled with cement, and all of the margins should be covered.'),
 'f_stick': ('fan', 'the patient is instructed to bite on an orangewood stick or other seating instrument'),
 'f_dynamic': ('fan', 'This technique, called dynamic seating, results in more complete seating of the casting.'),
 'f_mallet': ('fan', 'a sharpened stick may be placed with heavy force on the casting, along the line of draw of the preparation, with light mallet tapping'),
 'f_strands': ('fan', 'If removal is attempted before the cement is set, thin strands of cement may be dragged from under the margins, thus creating voids.'),
 'f_bead': ('fan', 'The beads of extruded cement have been shown to protect the cement at the margin from moisture contamination.'),
 'f_knot': ('fan', 'A knot is tied in the floss'),
 'f_subg': ('fan', 'Cement left subgingivally can cause tissue inflammation.'),
 'f_finishcem': ('fan', 'Finishing the casting before and during cementation led to the least marginal opening for all three cements.'),
 'f_postsens': ('fan', 'The patient is informed of the possibility of postcementation sensitivity'),
 # ---- Marzouk Ch.25 Casting pre-cementation, cementation and post-cementation adjustments (two-column OCR; phrases kept within one column line)
 'm_floss': ('mar', 'checked using unwaxed dental floss for its tightness'),
 'm_tempremove': ('mar', 'The temporary is removed usually using a scaler or a towel'),
 'm_desic': ('mar', 'and dried, but not to a desiccation level'),
 'm_varnish': ('mar', 'all preparation surfaces of vital teeth if zinc phosphate cement'),
 'm_obj': ('mar', 'The main objective of cementation is to bring the preparation'),
 'm_oblit': ('mar', 'Cementation should obliterate residual space between the'),
 'm_zoe': ('mar', 'ZOE is used only for temporary cementation of the casting'),
 'm_zpirr': ('mar', 'the most irritating to the P-D organ'),
 'm_pcc': ('mar', 'PCC is the most inert and least irritating to the P-D organ.'),
 'm_vibr': ('mar', 'metallic or metallic-based castings, vibrating condenser with'),
 'm_seaters': ('mar', 'available devices are used, ranging from orange wood sticks'),
 'm_burnzp': ('mar', 'If ZPC is the cementing medium, burnishing should'),
 'm_burnzp2': ('mar', 'be done during the setting of the cement. This cannot be done'),
 'm_cemline': ('mar', 'the circumferential tie. This will minimize or eliminate the'),
 'm_cemline2': ('mar', 'cement line, improving retention by the direct coupling and'),
 'm_burndir': ('mar', 'Burnishing is always done from the restoration surface to'),
 'm_diespacer': ('mar', 'The use of die spacer is the most practical way to insure the'),
 'm_perforate': ('mar', 'The casting can be perforated at an area of minimum'),
 'm_hydraulic': ('mar', 'as a luting agent insofar as it can create the highest'),
 'm_curette': ('mar', 'any remnant cement is curetted from'),
 'm_postvisit': ('mar', 'A post-cementation visit is advisable to discover these'),
 'm_sens': ('mar', 'be advised that a slight thermal sensitivity is expected for'),
 # ---- Sikri, Indirect Restorations 2e, Ch.12 Luting agents (PDF pages only)
 'k_gap': ('sik', 'cast restorations leave a gap of about 50–100'),
 'k_dynamic': ('sik', 'Seating the restoration under dynamic load (patient is instructed to'),
 'k_film': ('sik', 'The film thickness, clinically achieved, varies from 20 to 100'),
 'k_tilt': ('sik', 'The resin cements, because of their higher viscosity, may lead to tilting of castings.'),
 'k_partset': ('sik', 'is carried out before the cement is set completely, i.e. partly set cements'),
 'k_probe': ('sik', 'Once the cement is set, the probe should not be touched at the margins.'),
 'k_3min': ('sik', 'The seating force should be maintained at least for three minutes without any interruption while the cement is setting'),
 'k_venting': ('sik', 'venting is a satisfactory method of achieving minimal film thickness under cast restorations'),
 'k_spacer': ('sik', 'The discrepancies can be minimized by coating the die with die-spacer, and/or relieving the die or etching the casting.'),
 'k_zpmost': ('sik', 'Zinc phosphate cement is the most commonly used luting agent'),
 'k_zpmech': ('sik', 'This cement does not chemically bond to any surface and provides seal by mechanical retention only.'),
 'k_zphyd': ('sik', 'Zinc phosphate cement exhibited the greatest hydraulic pressure.'),
 'k_fast': ('sik', 'the seating of restorations should be fast (within a few seconds) while the cement is sufficiently fluid'),
 'k_panavia': ('sik', 'The chemically activated or auto-polymerizing systems (Panavia, C & B Metabond) are suited for luting of metal restorations.'),
 'k_dualnot': ('sik', 'therefore, not used in metal restorations'),
 # ---- Craig's 14e Ch.10 (fineness), Ch.12 (brazing investment), Ch.13 (bonding to cast alloys), Ch.14 (RMGI)
 'c_sand': ('cr14', 'Sandblasting with aluminum oxide is the most commonly used method to prepare metal substrates for receiving bonding resins or resin cements.'),
 'c_tin': ('cr14', 'Tin plating can be used to improve the retention of noble alloys to resin cements.'),
 'c_mdp': ('cr14', 'They seem to be more effective with base-metal alloys, compared to noble alloys.'),
 'c_incons': ('cr14', 'However, research results are inconsistent.'),
 'c_rmgiprimer': ('cr14', 'Bond strength to metal alloy is significantly increased with the use of metal primers.'),
 'c_fineness': ('cr14', 'represents the number of parts of gold in each 1000 parts of alloy'),
 'c_18k': ('cr14', 'An 18k gold would be designated as 750 fine'),
 'c_caratnoble': ('cr14', 'the terms carat and fineness refer only to gold content, not noble-metal content'),
 'c_braztypes': ('cr14', 'Type 1: Gypsum-bonded dental brazing investments'),
 'c_brazexp': ('cr14', 'Soldering investments are designed to have lower setting and thermal expansions than casting investments'),
 # ---- Craig and Powers 11e Ch.15 Noble dental alloys and solders; Ch.17 Casting and soldering procedures
 'r_weld': ('crm', 'The term welding is used if two pieces of metal are joined together directly'),
 'r_solder': ('crm', 'The words soldering and brazing are used if two pieces of metal are joined by adding a third metal.'),
 'r_425': ('crm', 'is below 425" C, the operation is soldering'),
 'r_dentbraz': ('crm', 'In dentistry, the parts are joined at temperature above 425" C, so the operation should be called brazing.'),
 'r_soft': ('crm', 'the soft solders lack corrosion resistance, which makes them impractical for dental applications'),
 'r_hard': ('crm', 'Gold-based solders that have good tarnish and corrosion resistance are extensively used in crown and bridge applications.'),
 'r_silver': ('crm', 'Silver-based solders are commonly used in orthodontic appliances.'),
 'r_freehand': ('crm', 'In freehand soldering, the parts to be assembled are manually held in contact while the heat and solder are applied.'),
 'r_invest': ('crm', 'investment soldering, customarily used in assembling bridges and similar restorations'),
 'r_ideal': ('crm', 'ease of flow at relatively low temperature'),
 'r_ideal2': ('crm', 'resistance to pitting during heating and application'),
 'r_comp': ('crm', 'Gold-based solders for dental use are primarily alloys of gold, silver, and copper, with small quantities of tin, zinc, and sometimes phosphorus'),
 'r_range': ('crm', 'the gold content may vary from 45 to 81 wt%'),
 'r_carat': ('crm', 'The number did not describe the actual carat of the solder, but rather the carat of the gold alloy on which the solder was to be used.'),
 'r_finedesc': ('crm', 'the degree of fineness has been used to describe the various solders'),
 'r_56': ('crm', 'the fusion temperature of the solder should be at least 56" C below that of the parts being joined to prevent distortion'),
 'r_lowfine': ('crm', 'lower-fineness solders are more fluid in the molten state than higher-fineness solders'),
 'r_lowfine2': ('crm', 'solders are used extensively for the assembly of dental appliances without serious tendencies to discolor'),
 'r_easyflow': ('crm', 'An easy-flowing solder is one that has a relatively low fusion temperature'),
 'r_freeflow': ('crm', 'The free-flowing quality refers specifically to the ability of the solder to spread and flow freely'),
 'r_pitover': ('crm', 'If the solder is heated to too high a temperature or for prolonged periods, the lower-melting point tin and zinc in the solder can boil or oxidize'),
 'r_pitunder': ('crm', 'If the solder is underheated and the flux is applied in excess or improperly melted, it may be trapped in the melted solder'),
 'r_diffuse': ('crm', 'Studies indicate that diffusion in the soldered joint reduces the strength and quality of the joint.'),
 'r_fluxdef': ('crm', 'dissolves surface oxides and allows the melted solder to wet and flow onto the adjoining alloy surfaces'),
 'r_borax': ('crm', 'The fluxes used for soldering gold alloys are combinations of borax and boric acid, with potassium fluoride added to some.'),
 'r_toomuch': ('crm', 'Too much flux is as undesirable as not enough flux.'),
 'r_flame': ('crm', 'Once the flame has been applied to the spot to be soldered, it should not be withdrawn until soldering is completed.'),
 'r_reducing': ('crm', 'A protective envelope should be created around the spot to be soldered with the reducing portion of the flame.'),
 'r_over': ('crm', 'Overheating during the soldering operation will cause (1) pits in the solder'),
 'r_under': ('crm', 'Underheating will cause pitting from the retention of unmelted flux'),
 'r_ball': ('crm', 'Solder that is not well heated tends to "ball" and fails to spread properly.'),
 'r_antibefore': ('crm', 'which should be applied to the surface before the flux or solder is applied'),
 'r_graphite': ('crm', 'a soft lead pencil is therefore an effective antiflux'),
 'r_rouge': ('crm', 'rouge (iron oxide) or whiting (calcium carbonate) in an alcohol and water suspension'),
 'r_gap': ('crm', 'If the parts are in intimate contact, they tend to expand and push apart on heating, whereas if the distance is too great, the parts tend to draw together as the solder solidifies.'),
 'r_013': ('crm', 'A clearance of a few hundredths of a millimeter (0.13 mm)'),
 'r_card': ('crm', 'This thickness can be practically estimated by the thickness of a typical business card.'),
 'r_infrared': ('crm', 'an infrared heating unit is available specifically for dental soldering'),
 'r_fluxchoice': ('crm', 'The choice of flux is dictated by the type of alloy to be soldered or cast, not by the type of solder used.'),
 'r_fluoride': ('crm', 'a special flux is required because borax and boric acid alone do not dissolve chromium oxides'),
 'r_art': ('crm', 'Despite certain well-established principles, soldering is an art.'),
 # ---- Phillips 12e Ch.16 Dental casting alloys and metal joining
 'p_450': ('phi', 'brazing requires a heating temperature above 450 °C and soldering is conducted below that temperature'),
 'p_solidus': ('phi', 'Both processes are performed below the solidus temperature of the substrate metal or metals.'),
 'p_weldfill': ('phi', 'Welding may not require a filler metal since the metal surfaces to be joined will melt and fuse locally.'),
 'p_typeI': ('phi', 'Type I. Surface protection'),
 'p_typeII': ('phi', 'Type II. Reducing agent'),
 'p_typeIII': ('phi', 'Type III. Solvent'),
 'p_antiflux': ('phi', 'an antiflux such as rouge mixed with chloroform or graphite can be painted on these areas'),
 'p_minflux': ('phi', 'It is of primary importance to minimize the amount of flux used.'),
 'p_fluxglass': ('phi', 'Flux combines with metal oxides and forms a glass during the soldering process'),
 'p_flowtemp': ('phi', 'metal should be at least 55.6 °C lower'),
 'p_goldNi': ('phi', 'gold-based filler metals should not be used as a presolder for base metal alloys'),
 'p_presold': ('phi', 'known as presoldering (or prebrazing)'),
 'p_investsold': ('phi', 'This process is called investment soldering.'),
 'p_gapundef': ('phi', 'The optimal gap between parts of substrate metal to be joined has never been precisely defined.'),
 'p_gapwide': ('phi', 'If the gap is too great, the joint strength will be dictated by the strength of the filler metal.'),
 'p_gapnarrow': ('phi', 'If the gap is too narrow, flux inclusions and porosity caused by incomplete flow of the filler metal may occur'),
 'p_propane': ('phi', 'Of the fuel gases in Table 16-15, the best choice is propane.'),
 'p_reduczone': ('phi', 'should be the tip of the reducing zone'),
 'p_furnace': ('phi', 'every component can be heated and cooled uniformly in accordance with a precise schedule that prevents distortion'),
 'p_laser': ('phi', 'Laser welding in an argon gas atmosphere is a method of choice for joining titanium components'),
 'p_radio': ('phi', 'The presence of solder joint defects, such as porosities'),
 # ---- McCabe and Walls 9e Section 7.7
 'w_interch': ('mcc', 'In dentistry the terms soldering and brazing are used interchangeably.'),
 'w_longspan': ('mcc', 'This approach is used to overcome distortions that may occur during cooling for metal frameworks for long span bridge work'),
 'w_req': ('mcc', 'capable of forming a strong, corrosion resistant joint between the two components being joined without changing their structure or properties'),
 'w_proof': ('mcc', 'the tensile strength of the brazed joint is required to exceed the 0.2% proof stress for the weakest of the two components'),
 'w_lactic': ('mcc', 'There should be no visible signs of corrosion when a brazed joint is soaked in a solution of lactic acid and sodium chloride for 7 days.'),
 'w_50100': ('mcc', 'the fusion temperature of the solder is generally 50–100ºC below that of the casting gold alloys'),
 'w_fluoride': ('mcc', 'Fluoride salts are particularly useful in breaking down the tenacious oxide'),
 # ---- Bhat et al 3e Ch.23 Brazing and welding
 'b_def': ('bhat', 'filling the gap between them with a molten filler of suitable alloy having lower fusion temperatures'),
 'b_5010': ('bhat', 'Solidus temperature should be 50–100oC lower'),
 'b_cote': ('bhat', 'Same COTE as the basis metal, to avoid detachment during thermal cycling'),
 'b_650': ('bhat', 'For adequate corrosion resistance, the gold alloys should have >650 fineness, i.e. >65% gold or >16 carats.'),
 'b_55': ('bhat', 'the fusion temperature should be at least 55°C below the solidus of parts of the substrate'),
 'b_pits': ('bhat', 'The pits collect food debris and lead to cell corrosion.'),
 'b_gap': ('bhat', 'The optimum gap between the soldering parts should be about 0.1 to 0.3 mm.'),
 'b_largegap': ('bhat', 'The contraction of a large amount of solder in the gap cause distortion.'),
 'b_boraxflux': ('bhat', 'This is a protective and reducing flux.'),
 'b_fluxfirst': ('bhat', 'first apply the flux to the surface and then antiflux coating to the unwanted areas'),
 'b_fluxafter': ('bhat', 'applied carefully on the surface, after applying antiflux'),
 'b_reducing': ('bhat', 'The blue coloured reducing flame has to be applied.'),
 'b_invest': ('bhat', 'This investment material should have a minimum setting and thermal expansions'),
 'b_weld': ('bhat', 'This is the process of fusing two or more metal parts through the application of heat, pressure, or both, with or without a filler metal'),
 'b_cast': ('bhat', 'It is the method of joining two components of a fixed cast partial denture by casting the molten metal into an interlocking region'),
 'b_apps': ('bhat', 'Joining clasps to removable cast partial dentures'),
 # ---- Rudolf et al 2024 Ch.6 Nanofoils in dental joining practice
 'a_nano': ('adm', 'uses reactive multi-layer nanofoils as a local heat source'),
 'a_furnace': ('adm', 'The use of reactive foils removes the need for a furnace'),
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
