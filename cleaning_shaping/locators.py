import re, os
# Verbatim-phrase locators for one topic. Every [SRC] fact in an answer has one entry in L.
# Run `python3 locators.py`: it must print "missing 0" before you publish.
T = os.path.expanduser('~/mds-textbooks/')   # clone of the private textbook repo
# F: source key -> (chapter file, offset, in-text citation)
#   offset int  : printed page = PDF marker - offset (check it at 2+ pages in THAT chapter)
#   offset None : cite the PDF page marker only (use when no printed page number is visible)
F = {
 'gro': (T+'Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/14_Chapter_14_Shaping_and_Cleaning_of_the_Radicular_Space_Instr.md', 25, 'Gopikrishna, 2021'),
 'tor': (T+'Endodontics_Principles_and_Practice_Chapterwise/14_14_Cleaning_and_Shaping.md', 7, 'Peters, Arias and Shabahang, 2021'),
 'coh': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/08_8_Cleaning_and_shaping_of_the_root_canal_system.md', None, 'Peters, Peters and Basrani, 2021'),
 'ing': (T+'Ingles_Endodontics_7th_Chapterwise/20_Chapter_20_Preparation_of_the_Coronal_and_Radicular_Spaces.md', -61, 'Hülsmann and Schäfer, 2019'),
 'siq': (T+'Treatment_of_Endodontic_Infections_Chapterwise/12_Chapter_12_Chemomechanical_preparation.md', None, 'Siqueira et al, 2022'),
 'sik': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/16_16_Cleaning_and_Shaping_of_Root_Canals.md', 21, 'Sikri, 2019'),
 'har': (T+'Harty_s_Endodontics_in_Clinical_Practice_7th_ed_Chapterwise/07_7_Preparation_of_the_Root_Canal_System.md', 16, 'Schäfer, 2017'),
}
# L: locator key -> (source key, verbatim phrase of under ~25 words copied from the chapter file)
#   Pick clean text: avoid OCR ligature damage ("0e", "!le"), hyphen breaks and figure captions.
L = {
 # Grossman's Ch.14 (Gopikrishna, 2021)
 'g_def':('gro','Shaping and cleaning of the root canal consists of removing the pulp tissue and debris from the canal and shaping the canal to receive an obturating material'),
 'g_debr':('gro','the removal of this material from the pulp cavity is referred to as debridement'),
 'g_fail':('gro','Obturation of an improperly cleaned canal would still lead to an endodontic failure irrespective of the quality of obturation'),
 'g_most':('gro','Shaping and cleaning of the root canal comprises the most important phase of endodontic treatment'),
 'g_obj':('gro','To debride and remove the infected tissues out of the root canal system without compromising the structural integrity of the root'),
 'g_four':('gro','Root canals should be widened for four reasons'),
 'g_tags':('gro','tags of pulp tissue and odontoblasts cling to the canal wall'),
 'g_flow':('gro','a shape that permits plasticized gutta-percha to flow against the walls without impedance'),
 'g_conf':('gro','Confinement of instrumentation to the roots themselves'),
 'g_space':('gro','Creation of sufficient space for optimal obturation of the radicular space'),
 'g_five':('gro','The shaping process of a root canal can be broadly classified into the following five phases'),
 'g_glide':('gro','The concept of creating a patent path up to the working length without altering or blocking the original root canal anatomy is known as glide path determination or canal patency'),
 'g_pre23':('gro','Enlarging the orifice and 2–3 mm of the coronal third reduces the stresses on subsequent shaping instruments'),
 'g_prewl':('gro','The working length of the tooth should be determined only after coronal pre-enlargement of the canal is completed'),
 'g_ggno':('gro','or with GatesGlidden drills (currently not recommended)'),
 'g_wl05':('gro','it is clinically recommended to terminate instrumentation and obturation within 0.5–1.0 mm short of the radiographic apex'),
 'g_apical34':('gro','The most critical area for canal disinfection is the apical 3–4 mm'),
 'g_2ml':('gro','Ideally, 2 mL of the irrigant per canal per instrument change is clinically recommended'),
 'g_recap':('gro','Returning to a smaller instrument from time to time before advancing to a larger size helps to prevent the packing of dentin filings'),
 'g_precurve':('gro','Precurving of files is restricted to stainless steel instruments'),
 'g_table':('gro','Summary of Techniques for Shaping and Cleaning the Root Canal System'),
 'g_sbdef':('gro','the canal is enlarged first in the apical third to at least a No. 25 or 30 instrument and then each consecutively larger root canal instrument is used for shaping the middle third and coronal part'),
 'g_sbsteps':('gro','by using sizes 30, 35, 40, and 45 files at 1, 2, 3, and 4 mm short of working length, respectively, to produce a coronal taper'),
 'g_sbend':('gro','Instrumentation is finished when the walls are smooth and clean and when the preparation shows continuous taper in an apical direction'),
 'g_psb':('gro','It involves the insertion of progressively larger hand instruments as deep as they can be passively placed'),
 'g_goerig':('gro','The concept of first instrumenting the coronal third of the root canal before apical shaping was first advocated by Goerig'),
 'g_rotarycd':('gro','Most rotary nickel–titanium systems employ crown-down instrumentation technique'),
 'g_cdp':('gro','Straight K-files are then used in a large to small sequence with a reaming motion and no apical pressure'),
 'g_bf1':('gro','positioning and preloading an instrument through clockwise rotation and then shaping the canal with counterclockwise rotation'),
 'g_bf2':('gro','The instrument is then rotated counterclockwise, 180–270°, and sufficient apical pressure is used to keep the file at the same insertion depth'),
 'g_roane':('gro','A minimum enlargement of size 45, 1.5 mm short of the apical foramen in curved canals, is recommended and size 80 in single-rooted teeth'),
 'g_cdadv':('gro','This technique minimizes the extrusion of debris through the apical foramen, thereby preventing postoperative discomfort'),
 'g_hybrid':('gro','This technique refers to a combination of step-down instrumentation followed by a step-back technique'),
 'g_hybridrec':('gro','Recommended by this textbook for use with stainless steel instruments'),
 'g_sblim':('gro','Tendency to straighten in the canal'),
 'g_oldrule':('gro','Enlarge a root canal at least three sizes beyond the size of the first instrument that binds'),
 'g_shavings':('gro','The color of dentinal shavings is no indication of the presence of infected dentin or organic debris'),
 'g_nostd':('gro','the minimum size to which a root canal should be enlarged cannot be standardized and varies from case to case'),
 'g_smallmaf':('gro','Increased chances of leaving behind infected tissues'),
 'g_largemaf':('gro','Increased probability of physical disruption of bacterial biofilms due to mechanical removal of radicular dentin'),
 'g_overzeal':('gro','Overzealous preparation leads to iatrogenic problems, unnecessary weakening of the tooth, and susceptibility to fracture'),
 'g_recip':('gro','The counterclockwise engaging angle is five times the clockwise disengaging angle'),
 'g_adaptive':('gro','This concept aims to conserve radicular dentin by emphasizing more on cleaning that canal rather than just enlarging the canal'),
 'g_ultra':('gro','Currently both sonic and ultrasonic devices are not indicated for shaping of the canal and are more indicated for cleaning applications'),
 'g_anticurv':('gro','This motion balances the cutting flutes against the safer part of the root canal'),
 # Torabinejad 6th ed Ch.14 (Peters, Arias and Shabahang, 2021)
 't_fallacious':('tor','This proved fallacious as obturation merely reflects the adequacy of the cleaning and shaping'),
 't_fracture':('tor','vertical fracture or other nonendodontic causes are the major reasons for the eventual loss of root canal–treated teeth'),
 't_reduce':('tor','a practical objective of cleaning is to significantly reduce the irritants, not totally eliminate them'),
 't_synergy':('tor','it is imperative to use mechanical shaping and irrigation in synergy to maximize antibacterial efficacy'),
 't_funnel':('tor','The main mechanistic objective of shaping is to maintain or develop a continuously tapering funnel from the canal orifice to the apex'),
 't_spreader':('tor','the canal should be enlarged sufficiently to permit placement of the spreader to within 1 to 2 mm of the working length'),
 't_plugger':('tor','the coronal enlargement must permit the placement of pluggers to within 3 to 5 mm of the WL'),
 't_lessres':('tor','the more dentin is removed from the canal walls, the less resistant to fracture the root becomes'),
 't_toothdep':('tor','Ideally, the degree of shaping should be tooth dependent and not depend on the obturation technique'),
 't_46':('tor','Another study found the classic apical constriction to be present in only 46% of the teeth'),
 't_12pct':('tor','the odds of success were reduced by 12% for every 1 mm of the canal short of the terminus remaining'),
 't_debate':('tor','the exact clinical point of apical termination of the preparation and obturation remains a matter of debate'),
 't_nostd':('tor','Because morphology is variable, there is no standardized apical canal size'),
 't_no20':('tor','apical transportation occurs in many curved canals enlarged beyond a No. 20 stainless steel file'),
 't_irrig':('tor','The criteria for cleaning and shaping should be based on the ability to adequately deliver sufficient amounts of irrigant and not on a specific obturation technique'),
 't_patency':('tor','For all these reasons the benefits of maintaining apical patency seem to outweigh possible risks'),
 't_criteria':('tor','The criteria of canal preparation include developing a continuously tapered funnel, maintaining the original shape of the canal, maintaining the apical foramen in its original position, keeping the apical opening as small as possible, and developing glassy smooth walls'),
 't_noconsensus':('tor','There is no consensus or clinical evidence on which technique or instrument design or type is clinically superior'),
 't_stages':('tor','Classically, Stage 1 is a defined preflaring, before bringing any hand file to the apical third of the canal'),
 't_pericerv':('tor','preserving pericervical dentin (4 mm above and below the crestal bone) is crucial for the distribution of functional stresses'),
 't_gpv':('tor','also known as glide path verification'),
 't_notprecurve':('tor','It is important to note that hand files for glide path preparation should not be precurved'),
 't_std':('tor','Unfortunately, in cylindrical and small curved canals, procedural errors were identified with the technique'),
 't_sb':('tor','This type of preparation is superior to standardized serial filing and reaming techniques in débridement and maintaining the canal shape'),
 't_bf':('tor','a clockwise rotation (less than 180 degrees) engages dentin. This is followed by a counterclockwise rotation (at least 120 degrees) with apical pressure'),
 't_bfbest':('tor','The balanced force concept is considered the most effective hand instrumentation technique'),
 't_recap':('tor','Recapitulation is performed between each successive enlarging instrument regardless of the cleaning and shaping technique'),
 't_stop':('tor','If this file stops as well, the apical configuration is called an apical stop'),
 't_three':('tor','In a small curved canal, enlargement should be restricted to three sizes larger than the IAF to decrease the potential for transportation'),
 't_iaf':('tor','It is defined as the largest file to bind slightly at the corrected WL after straightline access'),
 't_ggunsuit':('tor','The amount of dentin removed in the coronal third makes Gates-Glidden drills an unsuitable instrument for modern endodontics'),
 't_rotarymove':('tor','each instrumentation step should consist of three to five movements and should not exceed 10 to 15 seconds'),
 't_glassy':('tor','After cleaning and shaping procedures, the canal should exhibit “glassy smooth” walls'),
 't_conform':('tor','the so-called 3D conforming instruments'),
 't_circ':('tor','Circumferential filing is not very effective beyond the coronal third of a root canal'),
 # Cohen's Ch.8 (Peters, Peters and Basrani, 2021)
 'c_box':('coh','Give disinfecting irrigants access to the apical canal space'),
 'c_retain':('coh','Retain the integrity of radicular structures'),
 'c_reverse':('coh','reversing the order to “shaping and cleaning” may more correctly reflect the fact that enlarged canals direct and facilitate the cleaning action of irrigants'),
 'c_mech':('coh','An ideal mechanical objective of root canal instrumentation is complete and centered incorporation of the original canals into the prepared shape'),
 'c_unlikely':('coh','this goal is unlikely to be met with current techniques'),
 'c_03':('coh','0.3 mm is considered critical by some authors'),
 'c_schilder':('coh','this guideline was aimed at facilitating obturation rather than targeting antimicrobial efficacy'),
 'c_1mm':('coh','solutions have been shown to progress only about 1 mm farther than the tip of the needle'),
 'c_tech':('coh','final apical preparation size remains a much-disputed entity in root canal therapy'),
 'c_nit':('coh','the so-called non-instrumentation technique'),
 'c_chain':('coh','Endodontic therapy has been compared with a chain of events, wherein the chain is only as strong as each individual link'),
 'c_orifice':('coh','has been called “coronal flaring” but may be more appropriately described as orifice modification'),
 'c_flarewl':('coh','a documented benefit of coronal flaring is mitigation of WL changes during canal preparation'),
 'c_notconf':('coh','This has not been confirmed in experiments'),
 'c_patency':('coh','A patency file is a small K-file (usually a size #10 or #15) that is passively extended just through the apical foramen'),
 'c_glide15':('coh','a straight size #15 K-file can passively and smoothly travel to WL with long in-and-out movements'),
 'c_screwin':('coh','it minimizes the so-called screw-in or threading-in effect'),
 'c_term':('coh','terminating the preparation in necrotic cases at 0.5 to 1 mm short of the radiographic apex and 1 to 2 mm short'),
 'c_under':('coh','such an approach is likely to result in underestimation of the diameter'),
 'c_debate':('coh','An ongoing debate exists between those who prefer smaller apical preparations combined with tapered shapes and those who favor larger apical preparations'),
 'c_four':('coh','Basic cleaning and shaping strategies for root canal preparation can be categorized as crown-down, step-back, apical widening, and hybrid techniques'),
 'c_nocomp':('coh','Debate continues as to which of those strategies is superior for avoiding taper lock'),
 'c_sb':('coh','resulting in flared shapes with.05 and.10 taper, respectively'),
 'c_bfagree':('coh','a general agreement exists that the so-called balanced force technique creates the least canal aberrations with K-files'),
 'c_bfsteps':('coh','The instrument is rotated counterclockwise 180 to 270 degrees'),
 'c_hybrid':('coh','All basic techniques described so far may be combined into a hybrid technique to eliminate or reduce the shortcomings of individual instruments'),
 'c_round':('coh','Naturally, a rotating file can produce a round canal at best'),
 'c_gauge':('coh','after achieving a tapered canal form, the apical size at that point should be verified by apical gauging'),
 'c_wellshaped':('coh','a well-shaped canal is defined more specifically by the absence of procedural errors'),
 'c_turbid':('coh','an absence of visible turbidity and effervescence should be noted'),
 'c_transp':('coh','Canal transportation is at the root of all these clinical problems'),
 'c_150':('coh','It has been held that a transportation of about 100 to 150 μm may be clinically acceptable'),
 'c_summary':('coh','Cleaning and shaping are important, interdependent steps in root canal treatment'),
 'c_95':('coh','favorable outcome rates of up to 95% were reported for the treatment of teeth diagnosed with irreversible pulpitis'),
 'c_crownroot':('coh','A crown-down approach is recommended to reduce torsional loads'),
 # Ingle's Ch.20 (Hulsmann and Schafer, 2019)
 'i_def':('ing','It involves using mechanical and chemical means to remove pulpal tissue, reduce microbial load, and enable appropriate obturation of the radicular spaces'),
 'i_1974':('ing','have been outlined by Herbert Schilder in 1974'),
 'i_valid':('ing','Some of these objectives are still valid more than 40 years later'),
 'i_meds':('ing','space for intracanal medicaments'),
 'i_oneapp':('ing','Completion of preparation in one appointment'),
 'i_individ':('ing','Each root canal has to be addressed individually'),
 'i_toxins':('ing','Neutralization of microbial toxins and byproducts'),
 'i_skill':('ing','is higher when using stainless steel instruments and lower when using rotary NiTi instruments'),
 'i_principle':('ing','Preparation should dictate the obturation technique rather than the obturation technique dictating a certain preparation technique'),
 'i_wvc':('ing','A conicity of 7% or more is required to create a capture zone'),
 'i_bf':('ing','followed by a 120° rotation (cutting phase) in counterclockwise direction with maintained apical pressure'),
 'i_bf180':('ing','rotated at 180° in a clockwise direction (placement phase)'),
 'i_box':('ing','thereby giving the apical 2-5 mm a cylindrical rather than a conical shape'),
 'i_noevid':('ing','there is no evidence that step-down techniques are superior to step-back techniques or vice versa with the exception of the BF technique'),
 'i_ledges':('ing','but crown-down preparation produced more ledges'),
 'i_nit':('ing','the NIT system cannot be considered a viable alternative to mechanical root canal instrumentation at this time'),
 # Siqueira et al Ch.12 (2022)
 'q_wash':('siq','more than 60% of teeth with posttreatment disease were associated with inadequate root canal fillings'),
 'q_reflect':('siq','obturation merely reflects the aptness of chemomechanical procedures'),
 'q_unable':('siq','chemomechanical procedures alone are unable to achieve thorough cleaning of the root canal system'),
 'q_ss':('siq','The use of NiTi files was five times more likely to achieve healing than that of stainless steel'),
 'q_77':('siq','NiTi rotary instruments achieved higher healing rates (77%) than stainless steel hand files (60%)'),
 'q_vital':('siq','The recommended WL in teeth with vital pulps is 1 to 2 mm short of the radiographic apex'),
 'q_critical':('siq','The apical part of the root canal can be regarded as “critical territory” for pathogenic bacteria, the host, and the clinician'),
 'q_terminus':('siq','it seems prudent to extend the apical limit of instrumentation to the canal terminus'),
 'q_patency05':('siq','the apical preparation should be sculpted short of the canal terminus (0.5 to 1 mm) by using larger file sizes'),
 'q_complete':('siq','chemomechanical procedures should be considered complete when the canal is enlarged to diameters that are compatible with the root anatomy and large enough to be safe and antibacterially effective'),
 'q_larger':('siq','the larger the apical preparation of infected root canals, the greater the reduction of the bacterial populations'),
 'q_no45':('siq','The load needed to bend a no. 45 NiTi instrument is equivalent to the load required to bend a no. 25 stainless steel file of the same design'),
 'q_filing':('siq','Filing motion should not be used for apical preparations'),
 'q_pecking':('siq','A pecking or pumping motion, which lowers the apical forces during root canal preparation'),
 # Sikri Ch.16 (2019)
 'k_axiom':('sik','The axiom ‘what comes out is more important than what goes in’ forms the basis for successful endodontics'),
 'k_bmp':('sik','The term ‘biomechanical preparation’ as described by Schilder, involves biological and mechanical objectives'),
 'k_chemo':('sik','concept of chemomechanical preparation'),
 'k_substrate':('sik','Removal of substrate harboring microorganisms from the root canal space'),
 'k_ace':('sik','The techniques of root canal preparation can be divided into two groups'),
 'k_bf':('sik','Move the file three-quarter turn counterclockwise'),
 'k_bfq':('sik','Turn the file one quarter turn clockwise'),
 'k_zone':('sik','The ‘apical control zone’ is the mechanical alteration created in the apical third of the root canal'),
 'k_75':('sik','The first file that bind may not reflect the diameter at working length'),
 'k_modsb':('sik','This gives a parallel and round form in the apical area'),
 'k_cdp35':('sik','the depth to which no. 35 file penetrates to its point of first resistance'),
 'k_fava':('sik','Double flare technique, introduced by Fava, involves preparing the canal in crown-down manner using Kfiles, followed by step-back manner'),
 'k_std':('sik','The technique is no longer followed'),
 # Harty's Ch.7 (Schafer, 2017)
 'h_triad':('har','The traditional ‘endodontic triad’ concept of cleaning, shaping and filling remains relevant'),
 'h_3540':('har','the apical preparation should be at least an ISO size 35 to 40, 0.02 taper or a size 25, 0.04 taper'),
 'h_bf':('har','followed by a half turn of the file in the counterclockwise direction'),
 'h_ssglide':('har','stainless steel hand instruments are best suited for creating a glide path'),
 'h_groups':('har','Engine-driven NiTi instruments may be categorised into three main groups according to how they are used'),
 'h_recip':('har','the angle of the counterclockwise direction is greater than that of the reverse, clockwise, direction'),
 'h_cracks':('har','an increased tendency of apical debris extrusion with reciprocating instruments'),
 'h_10pct':('har','even after substantial deformation (up to 10%) once the load is removed'),
 'i_ggsafe':('ing','GG is safe, relatively inexpensive'),
 'i_ggshaft':('ing','Fracture usually occurs high at the shaft, making removal easy'),
 'k_patency2':('sik','passively inserting a small sized (size 08 or 10) file, 2.0 mm beyond the apical constriction'),
 'k_disfavor':('sik','May push microorganisms into periapical area'),
 'h_patency1':('har','usually set at 1 mm longer than the final working length'),
 'q_patency1':('siq','up to 1 mm longer than the canal terminus'),
 'g_glidepre':('gro','The glide path is established by using a precurved ISO size 10 or ISO size 8'),
 'g_extrus':('gro','This reduces the potential for extrusion of debris beyond the working length'),
 't_lube':('tor','Aqueous solutions, such as NaOCl, should always be used instead of paste lubricants when using NiTi rotary techniques to reduce torque'),
 'c_tugback':('coh','At this time, the feel would be of tug-back, a slight resistance to pull'),
 't_sshape':('tor','Roots with an S-shape or bayonet configuration are very difficult to treat'),
 't_mineral':('tor','Such mineralization generally occurs in a coronal to apical direction'),
 't_aae':('tor','The Endodontic Case Difficulty Assessment Form'),
 't_curvebl':('tor','Canals are seldom straight, and curvatures in a buccolingual direction are normally not'),
 'g_histo':('gro','Histologic examination of pulpless teeth in which root canal therapy has failed often shows that the canals were not completely cleaned'),
 'g_cdj':('gro','located 0.5–0.75 mm short of the anatomical apex'),
 'g_ealcombo':('gro','The most appropriate technique for the assessment of working length is by using a combination of electronic apex locator along with Ingle’s radiographic technique'),
 'g_weine':('gro','the working length should be reduced to 1.5 mm short of the radiographic apex'),
 'c_combo':('coh','combined use of both radiographic and electronic techniques has been shown to result in greater accuracy'),
 't_shorten':('tor','During canal preparation, WLs tend to shorten as a result of the fact that the enlarged canal provides a straighter path'),
 't_smalllong':('tor','Small, long, and curved canals are the most difficult and tedious to enlarge'),
 't_contain':('tor','Instruments, irrigants, debris, and obturating materials should be contained within the canal'),
 'c_twocanals':('coh','consider shaping as two canals'),
 'q_oval':('siq','Long oval and flattened canals may require changes in preparation strategy by using rotary instruments in brushing motion'),
 't_noforce':('tor','Instrument binding or dentin removal on insertion should be avoided'),
 'g_discard':('gro','Once deformed, the instrument must be discarded'),
 'c_rotglide':('coh','The creation of a rotary glide path has demonstrated better preservation of the canal anatomy with fewer shaping aberrations'),
 'c_pain':('coh','has shown a less incidence of postoperative pain'),
 'q_planned':('siq','In the planned apical preparation principle'),
 'q_cbctdiam':('siq','is measured based on cone beam computed tomographic scans and used to determine the ideal master apical instrument size and taper'),
 'q_removal':('siq','This motion is used to remove vital pulps, free debris, and cotton pellets or paper points from the canal'),
 't_critical':('tor','Elimination (or significant reduction) of inflamed or necrotic pulp tissue and microorganisms are the most critical factors'),
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
