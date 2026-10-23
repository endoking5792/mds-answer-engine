"""Verbatim-phrase locators for the Smart Materials CD Q02 canonical answer (re-read 2026-10-22).
Run: python3 smart_locators.py  -> checks every phrase against the source PDF and prints the page."""
import re, os
D = os.path.expanduser('~/Downloads/Smart Materials/')
T = os.path.expanduser('~/mds-textbooks/Operative_and_Dental_Materials_Textbooks/')
# key -> (file, first printed page or None, citation)
F = {
 'mal': (D+'cureus-0014-00000030789.pdf', 1, 'Maloo et al, 2022'),
 'bad': (D+'TSWJ2014-986912.pdf', 1, 'Badami and Ahuja, 2014'),
 'vas': (D+'jfb-16-00318.pdf', 1, 'Vasluianu et al, 2025'),
 'sun': (D+'1-s2.0-S2590006425009202-main.pdf', 1, 'Sun et al, 2025'),
 'das': (D+'1-s2.0-S0109564126002976.pdf', 1891, 'Dascanio et al, 2026'),
 'abo': (D+'10266_2025_Article_1162.pdf', 349, 'Abozaid et al, 2026'),
 'yao': (D+'1-s2.0-S0109564123003962.pdf', 1040, 'Yao et al, 2023'),
 'kha': (D+'BIiD-12-45229.pdf', 288, 'Khan, 2025'),
 'ved': (D+'cureus-0017-00000082858.pdf', 1, 'Ved et al, 2025'),
 'bru': (D+'materials-12-02216-v4.pdf', 1, 'Bruni et al, 2019'),
 'cra': (T+'Craigs_Restorative_Dental_Materials.md', None, 'Sakaguchi et al, 2019'),
}
L = [
 ('mal','the material needs to be passive in nature'),
 ('mal','sustain the remaining structure of the tooth'),
 ('mal','These materials utilize the feedback loop mechanism'),
 ('mal','A current is generated when mechanical stress is applied'),
 ('mal','At ambient temperature and at about 95°C, the crystal structure is monoclinic'),
 ('mal','bacterial adhesion on the surface of GIC is still a concern'),
 ('mal','smart composite is an alkaline, nano-filled glass restorative substance that is light-activated'),
 ('mal','vinylsiloxanether; it is the combination of polyether and polyvinylsiloxane'),
 ('mal','Great machinability and minimal abrasiveness'),
 ('bad','useful, reliable, reproducible, and usually reversible manner'),
 ('bad','Perhaps the first inclination that an'),
 ('bad','No artificial materials are yet intelligent in this sense'),
 ('bad','deformations of as much as 8% strain to be recoverable'),
 ('bad','When low pH values (at or below 5.8) occur during a carious attack'),
 ('bad','unit cell of monoclinic occupying about 4.4% more volume than when tetragonal'),
 ('bad','in response to stress makes zirconia a smart material'),
 ('bad','In dry conditions, the materials showed a marked contraction when heated above 50'),
 ('bad','this aspect of the smart behaviour of dental cements can be controlled by the operator'),
 ('bad','The fracture toughness of the self-healing material was statistically similar to the control'),
 ('vas','achieving greater than 90% reductions in viability'),
 ('vas','reducing biofilm formation by up to 90%'),
 ('vas','>0.3 wt% incorporated into PMMA can trigger fi'),
 ('vas','reduce secondary caries depth (by 9%)'),
 ('vas','reduce dentinal demineralization depth by 14%'),
 ('vas','stark paucity of'),
 ('vas','mandating a ≥3-log CFU/mL reduc'),
 ('vas','its sharp nanosheets physically puncture bacterial membranes'),
 ('sun','inert, active, reactive, and autonomous'),
 ('sun','insufficient mechanistic understanding continues to hinder their systematic classification'),
 ('sun','classifies smart dental restorative materials into seven major categories'),
 ('sun','making NACP a representative'),
 ('sun','bulk-filled and conventional composite resins outperform high-adhesion reinforced GICs'),
 ('sun','Heat treatment can restore up to 85% of the original fracture toughness'),
 ('sun','is already widely used in clinical practice'),
 ('sun','Secondary caries at restoration margins is the leading cause of restoration failure'),
 ('sun','‘‘three-tiered evidence chain’’'),
 ('sun','FDA’s 510(k) pathway may apply'),
 ('das','45 wt% SiO₂, 24.5 wt% Na₂O, 24.5 wt% CaO, and 6 wt% P₂O₅'),
 ('das','form a continuous apatite layer within less than 48 h in SBF'),
 ('das','is often employed as a marketing tool'),
 ('das','reabsorb fluoride after immersion in fluoride-containing solutions'),
 ('das','central paradox of bioactive materials lies in balancing thera'),
 ('das','S53P4 bioglass contains a higher proportion of SiO₂ (53%)'),
 ('abo','some researchers arguing that no current dental restorative mate'),
 ('abo','The 2023 FDI Policy Statement provides a framework'),
 ('abo','merely releasing ions does not qualify a material as bio'),
 ('abo','though this claim has been challenged'),
 ('abo','CN is described by its manufacturer as an “alkasite”'),
 ('abo','markedly greater wear compared to conventional RBCs or RMGICs'),
 ('yao','bacteriostasis rate (80.3%) and excellent self-healing efficiency (66.1%)'),
 ('yao','The resin was prepared from TEGDMA monomers and BisGMA at 1:1 mass ratio'),
 ('yao','56.0 ± 5.3 MPa'),
 ('kha','fracture toughness recovery between 65% and 77%'),
 ('kha','68–77% recovery of fracture toughness'),
 ('kha','healing efficiency in clinical environments may drop below 50.0%'),
 ('kha','applying heat at 60–90°C to a tooth is not clinically feasible'),
 ('kha','While full clinical translation has not yet been realised'),
 ('kha','30% reduc'),
 ('kha','Bacillus subtilis spores'),
 ('kha','~800 million direct resin‑based composite (RBC) restorations'),
 ('ved','Three functions can be distinguished in material intelligence'),
 ('ved','The polymer cutting edges grow blunt'),
 ('ved','Hours spent working and setting were cut by at least 33%'),
 ('bru','The overall quality was judged low'),
 ('bru','biologically-dependent stimuli'),
 ('cra','The monoclinic form is stable at all temperatures below 1170'),
]
def norm(s):
    s = s.replace('­', '').replace('‐', '-').replace('‐', '-')
    return re.sub(r'\s+', ' ', s).replace('- ', '')
_c = {}
def pages(path):
    if path not in _c:
        if path.endswith('.pdf'):
            import fitz
            _c[path] = {i+1: norm(p.get_text()) for i, p in enumerate(fitz.open(path))}
        else:
            txt = open(path, encoding='utf8').read()
            parts = re.split(r'(?:<!-- PDF page (\d+) -->|===== PAGE (\d+) =====)', txt); pg = {}
            for i in range(1, len(parts), 3):
                k = int(parts[i] or parts[i+1]); pg[k] = pg.get(k, '') + ' ' + norm(parts[i+2])
            _c[path] = pg
    return _c[path]
def locate(f, ph):
    path, first, cite = F[f]; pg = pages(path); n = norm(ph)
    hit = [p for p, t in pg.items() if n in t]
    if not hit:
        ks = sorted(pg); hit = [a for a, b in zip(ks, ks[1:]) if n in pg[a] + ' ' + pg[b]][:1]
    if not hit: return None
    p = hit[0]
    return (f"p.{first + p - 1}" if first else f"PDF p.{p}"), cite, os.path.basename(path)
if __name__ == '__main__':
    bad = 0
    for f, ph in L:
        r = locate(f, ph)
        if not r: bad += 1; print('MISSING', f, ph[:70])
    print('checked', len(L), 'missing', bad)
