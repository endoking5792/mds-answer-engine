import re, os
# Verbatim-phrase locators for Instruments and Instrumentation. Every [SRC] fact has one entry in L.
T = '/home/user/mds-textbooks/'
F = {
 'sik': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/11_11_Endodontic_Instruments.md', 21, 'Sikri, 2019'),
 'end9': (T+'Endodontology_Chapterwise/09_9_Conventional_Instruments_and_Advances_in_Design.md', None, 'Baumann and Beer, 2010'),
 'end10': (T+'Endodontology_Chapterwise/10_10_Nickel_titanium_Materials_Science.md', None, 'Baumann and Beer, 2010'),
 'end12': (T+'Endodontology_Chapterwise/12_12_Sonic_and_Ultrasonic_Treatment.md', None, 'Baumann and Beer, 2010'),
 'end20': (T+'Endodontology_Chapterwise/20_20_Engine_driven_Instrumentation_Systems_History_and_Early_D.md', None, 'Baumann and Beer, 2010'),
 'end21': (T+'Endodontology_Chapterwise/21_21_Power_driven_Instrumentation_Systems_Recent_Advancements.md', None, 'Baumann and Beer, 2010'),
 'end22': (T+'Endodontology_Chapterwise/22_22_Fracture_of_Endodontic_Instruments_Torque_and_Fatigue.md', None, 'Baumann and Beer, 2010'),
 'end23': (T+'Endodontology_Chapterwise/23_23_File_Systems.md', None, 'Baumann and Beer, 2010'),
 'coh10': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/10_10_Nonsurgical_retreatment.md', None, 'Roda et al, 2021'),
 'end15': (T+'Endodontology_Chapterwise/15_15_Retreatment.md', None, 'Baumann and Beer, 2010'),
 'ing23': (T+'Ingles_Endodontics_7th_Chapterwise/23_Chapter_23_Endodontic_Orthograde_Retreatment_and_Management_.md', None, 'Ingle, year not printed'),
 'sik16': (T+'Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/16_16_Cleaning_and_Shaping_of_Root_Canals.md', None, 'Sikri, 2019'),
 'coh8': (T+'Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/08_8_Cleaning_and_shaping_of_the_root_canal_system.md', None, 'Peters et al, 2021'),
 'ing20': (T+'Ingles_Endodontics_7th_Chapterwise/20_Chapter_20_Preparation_of_the_Coronal_and_Radicular_Spaces.md', None, 'Ingle, year not printed'),
}
L = {
 'st_tipang': ('sik', 'The tip angle of an instrument should be'),
 'st_d0': ('sik', 'D0 and D16 denote length while D1, D2 denote diameter'),
 'st_kerr': ('sik', 'The design of basic hand instrument was patented by Kerr company in 1915, comprising 2% taper and 16 mm long cutting surfaces'),
 'st_iso': ('sik', 'ISO deals with instruments for preparation (No. 3630-1) and obturation (No. 3630-3) of root canal'),
 'st_ansi': ('sik', 'ANSI designated instruments as: K-type files and reamers (no. 28)'),
 'st_before': ('sik', 'Earlier the root canal instruments were manufactured without adhering to any pre-established criteria'),
 'st_number': ('sik', 'Each number shall be representative of diameter of instrument in 100th of mm at the tip'),
 'st_flutes': ('sik', 'and shall exactly extend 16 mm up the shaft'),
 'st_d2': ('sik', 'The diameter of D2 shall be 0.32 mm greater than D1'),
 'st_taper02': ('sik', 'This sizing ensures a constant increase in taper of 0.02 mm per mm'),
 'st_inc': ('sik', 'Instrument size should increase by 0.05 mm at D1 between no. 10 and 60'),
 'st_colour': ('sik', 'Instrument handles be color coded'),
 'st_greater': ('sik', 'Later, the greater taper instruments having taper more than 2% were introduced'),
 'st_half': ('sik', 'Instrument having half sizes'),
 'st_len': ('sik', 'short (21 mm), standard (25 mm) and long (31 mm)'),
 'st_class': ('sik', 'Different classifications for endodontic instruments have been proposed by various authors; however, none is universally accepted'),
 'st_seq': ('sik', 'The easy way to classify endodontic instruments is according to their sequence of usage'),
 'st_list': ('sik', 'A.Diagnostic instruments B. Exploring instruments C. Extirpating instruments D.Shaping instruments E. Obturating instruments F. Miscellaneous'),
 'st_gross': ('sik', 'Exploring instruments • Smooth barbed broach • DG-16 explorer ii. Debriding instruments • Barbed broaches iii. Shaping instruments • Reamers • Files iv. Obturating instruments'),
 'st_harty': ('sik', 'ii. Instruments used for root canal preparation • Hand instruments • Power assisted instruments • Electronic measuring devices'),
 'st_e_iso': ('end10', 'The dimensions of endodontic instruments are determined according to ISO standards'),
 'st_e_col': ('end10', 'the ISO color coding scheme is still determined by the diameter of the'),
 'st_e_ehr': ('end10', 'As early as 2002, Ehrmann called for standardization and'),
 'st_e_lin': ('end9', 'ISO numbers have increased linearly, in contrast to the erratic increase in the diameter of the'),
 'st_e_29': ('end9', 'A constant increase of 29%'),
 'st_g_gauge': ('sik16', 'Apical gauging implies measuring/ assessing the apical diameter of the canal, where the instrument fits snuggly and resist further apical movements'),
 'st_g_tune': ('sik16', 'Apical tuning implies a confirming parameter, whereby the apical diameter of the master apical file represents the true diameter of the apical configuration of the root canal'),
 'st_g_straight': ('sik16', 'The gauging instrument is inserted straight in and straight out, without any rotation'),
 'st_g_niti': ('sik16', 'Ni-Ti instruments are preferred for gauging because of their flexibility'),
 'st_g_full': ('sik16', 'Clinically, the file that goes full length represents the'),
 'rf_c_gc': ('coh10', 'Guttacore can be removed quite easily with predictable results using a variety of hand, rotary, and retreatment instruments'),
 'rf_i_rem': ('ing23', 'mechanically soften and engage gutta-percha'),
 'rf_i_kit': ('ing23', 'is an innovative system comprised of 3 nickel titanium (NiTi) instruments that vary in length'),
 'rf_i_dims': ('ing23', '(16 mm, 18 mm, and 22 mm respectively for D1, D2 and D3), diameter, and taper (30/09, 25/08, 20/07)'),
 'rf_i_caution': ('ing23', 'Rotary instruments should be used with caution in underprepared canals'),
 'rf_i_thirds': ('ing23', 'it is useful to mentally divide the root into thirds'),
 'rf_i_speed': ('ing23', 'rotary instruments must turn at speeds ranging from 800 to 1200 rpm'),
 'rf_i_pilot': ('ing23', 'in the coronal portion of the canal with either a hot heat carrier or by using the Protaper Retreatment D1 instrument'),
 'rf_i_effic': ('ing23', 'for removing gutta-percha from a previously treated root canal'),
 'rf_c_list': ('coh10', 'dedicated gutta-percha removal instruments, such as the GPX (Brasseler, Savannah, GA), the ProTaper Universal retreatment files'),
 'rf_c_frac': ('coh10', 'In several studies of mechanical guttapercha removal, fracture of the mechanical instruments or the tooth root occurred'),
 'rf_c_nosep': ('coh10', 'one study showed no separation or other canal defects when using dedicated retreatment files'),
 'rf_c_tip': ('coh10', 'ProTaper Universal retreatment file has a cutting tip for enhanced penetration of the root filling materials'),
 'rf_c_saf': ('coh10', 'When the Self-Adjusting Files were used after rotary retreatment files, reduction of canal residues were 66%, 68%, and 81% in the coronal, apical, and middle thirds of the canal'),
 'rf_c8_tip': ('coh8', 'cutting tips in that case facilitate removal of the existing root canal filling material and are sufficiently safe'),
 'rf_e_rendo': ('end15', 'The R-Endo-System (MICRO-MEGA, France) has a distinct design'),
 'rf_e_d1d3': ('end15', 'for reinstrumentation (ProTaper Universal D1-D3'),
 'rf_s_mtwo': ('sik', 'MTwo retreatment files are also available, viz. MTwo R 15/0.05 and MTwo R 25/0.05 with active tip, which penetrates better in obturating material'),
 'rf_s_pt': ('sik', 'Protaper can be helpful in retreatment cases; finishing files are useful in complete removal of guttapercha'),
 'sa_core': ('sik', 'SAF does not have a solid metal shaft'),
 'sa_widest': ('sik', 'Most rotary file systems follow the widest part of the canal and gradually machine it'),
 'sa_def': ('sik', 'The Self-Adjusting File (ReDentNova) is a hollow file, designed as a compressible, thin-walled pointed cylinder'),
 'sa_lattice': ('sik', 'The internal part of the hollow tube is composed of Ni-Ti lattice'),
 'sa_tip': ('sik', 'The file has an asymmetrically positioned tip'),
 'sa_flow': ('sik', 'The continuous flow of irrigant is provided through the hollow tube'),
 'sa_compress': ('sik', 'The 1.5 mm file may easily be compressed and inserted into any canal previously prepared/ negotiated with a # 20 K-file'),
 'sa_regain': ('sik', 'The file attempts to regain its original dimensions, thus applying a constant delicate pressure on the canal walls'),
 'sa_adapt': ('sik', 'In a round canal, it will attain a round cross-section; whereas, in an oval or flat canal it will attain a flat or oval cross-section'),
 'sa_abrasive': ('sik', 'The surface of the lattice threads is lightly abrasive'),
 'sa_vib': ('sik', 'The SAF is operated with transline (in and out) vibrating handpieces with 3,000 to 5,000 vibrations per minute and an amplitude of 0.4 mm'),
 'sa_cycles': ('sik', 'using two cycles of 2 minutes each for a total of 4 minutes per canal'),
 'sa_single': ('sik', 'The SAF file is designed for single use'),
 'sa_uniform': ('sik', 'SAF removes a uniform layer of dentin from the canal walls, thus resulting in a relatively uniform remaining dentin thickness'),
 'sa_transport': ('sik', 'SAF maintains the apical part of curved canals closer to its original shape and configuration'),
 'sa_durab': ('sik', 'SAF can be rotated for more than 150 hours at 900 rpm with a 5.0 mm deflection with no mechanical failure'),
 'sa_retrieve': ('sik', 'The damaged file can be retrieved from the canal without any difficulty'),
 'sa_smear': ('sik', 'the root canal surface (including its apical third) was rendered clean of debris and the smear layer'),
 'sa_irrig': ('sik', 'at a low pressure and at flow rates of 1.0 to 10 ml/minute'),
 'sa_c_wall': ('coh8', 'In vitro data for this system suggest that indeed more wall contact is made compared with rotary files'),
 'sa_c_shape': ('coh8', 'Shaping quality is also on par with rotary instruments'),
 'sa_c_glide': ('coh8', 'An initial glide path to a #20 K-file allows insertion of the SAF file'),
 'sa_i_isthmi': ('ing20', 'No NiTi system (SAF, K3, WaveOne) was able to'),
 'sa_i_2010': ('ing20', 'In 2010, the SAF system was introduced'),
}
def norm(s):
    s = s.replace('­ ', '').replace('­', '').replace('‐', '-')
    s = re.sub(r'\s+', ' ', s).replace('- ', '')
    return s.strip()
_cache = {}
def _pages(path):
    if path in _cache: return _cache[path]
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
    if off is None: return f"PDF p.{p}"
    return f"PDF p.{p} (printed p.{p-off})"
if __name__=='__main__':
    bad = 0
    for k in L:
        lab = page_label(k)
        if lab is None: bad += 1; print('MISSING', k, L[k][1][:70])
    print('checked', len(L), 'missing', bad)
