import re, os, sys
from locators import L, F, page_label
BOOK = {
 'GW2017': "George R, Walsh LJ. Laser-assisted endodontics. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.9.",
 'GW2023': "George R, Walsh LJ. Laser-assisted endodontics. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 2nd ed. Cham: Springer Nature; 2023. Ch.9.",
 'Coluzzi2017': "Coluzzi DJ. Laser and light fundamentals. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.2.",
 'Parker2017': "Parker SPA. Laser–tissue interaction. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.3.",
 'Selting2017': "Selting W. Laser operating parameters for hard and soft tissue, surgical and PBM management. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.4.",
 'Stabholz2016': "Stabholz A, Sahar-Helft S, Moshonov J. Lasers in endodontics. In: Convissar RA, editor. Principles and Practice of Laser Dentistry. 2nd ed. St Louis: Elsevier; 2016. Ch.13.",
 'Pandey2018': "Pandey V. Lasers in Operative Dentistry and Endodontics. New Delhi: CBS Publishers; 2018 (first eBook edition). Ch.4 Laser–tissue interaction, Ch.5 Classification, Ch.8 Lasers in endodontics (cited by PDF page; no printed folios in the file).",
 'Gopikrishna2021': "Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. New Delhi: Wolters Kluwer; 2021. Ch.24 Lasers in endodontics.",
 'Sikri2019': "Sikri VK. Essentials of Endodontics. 2nd ed. New Delhi: CBS Publishers (second eBook edition 2019, as printed). Ch.31 Lasers in endodontics.",
 'Alshahrani2016': "Alshahrani M, Beebe B, Chogle SM. Lasers. In: Jain P, editor. Current Therapy in Endodontics. 1st ed. Ames: John Wiley & Sons; 2016. Ch.10.",
 'Goodis2012': "Goodis HE, Pashley DH. Effects of thermal and mechanical challenges. In: Hargreaves KM, Goodis HE, Tay FR, editors. Seltzer and Bender's Dental Pulp. 2nd ed. Chicago: Quintessence; 2012. Ch.15 (cited by PDF page).",
 'Fouad2021': "Fouad AF, Levin LG. Pulp reactions to caries and dental procedures. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.14 (cited by PDF page).",
 'Banday2026': "Banday F, Hoskin E, Damodar A, Nachnani K. Lasers in dentistry: practical implications; what is the evidence? Dent Clin North Am. 2026;70:31-44. https://doi.org/10.1016/j.cden.2025.07.004 (DCNA, read in full).",
 'Mortman2011': "Mortman RE. Technologic advances in endodontics. Dent Clin North Am. 2011;55:461-480. https://doi.org/10.1016/j.cden.2011.02.006 (DCNA, read in full).",
}
LIT = {
 'FernandezMoreno2026': "Fernández-Moreno P, Areal-Quecuty V, Segura-Raya C, Saúco-Márquez JJ, Sánchez-Domínguez B, Martín-Jiménez M, Segura-Egea JJ, León-López M. Prognosis of periapical lesions treated by activated disinfection (PUI, laser) without the use of systemic antibiotics: systematic review and meta-analysis. J Clin Med. 2026. https://doi.org/10.3390/jcm15145397. PMID 42513311 (PubMed abstract read).",
 'Sabeti2025': "Sabeti M, Harouni A, Gabbay J. Comparing ultrasonically activated irrigation and laser-activated irrigation for postoperative pain reduction in endodontics: a systematic review and meta-analysis of randomized controlled trials. J Endod. 2025. https://doi.org/10.1016/j.joen.2025.08.002. PMID 40818665 (PubMed abstract read).",
 'FieglerRudol2025': "Fiegler-Rudol J, Grzech-Leśniak Z, Tkaczyk M, Grzech-Leśniak K, Zawilska A, Wiench R. Enhancing root canal disinfection with Er:YAG laser: a systematic review. Dent J (Basel). 2025. https://doi.org/10.3390/dj13030101. PMID 40136729 (PubMed abstract read).",
}
RANGE = {'15':(510,600),'100':(3200,3500),'75':(2550,3000),'50':(1700,2000),'25':(850,1000),'20':(680,800),'10':(320,400),'7':(320,400),'5':(160,200)}
def run(p):
    s = open(p,encoding='utf8').read().split('\n## SOURCE LIST')[0]
    s = re.sub(r'\n\*\*FAILURE DISCLOSURE:.*\n','\n',s)
    grab = lambda tag: [k.strip() for k in (re.search(rf'<!--{tag}: (.*?)-->',s,re.S).group(1).split(',') if re.search(rf'<!--{tag}: (.*?)-->',s,re.S) else []) if k.strip()]
    keys, refs, lits = grab('LOC'), grab('REF'), grab('LIT')
    cores = re.findall(r'#{2,4} ✎ Exam core\n(.*?)(?=\n## |\n### |\Z)',s,re.S); wc = sum(len(c.split()) for c in cores)
    mk = re.search(r'\*\*Marks:\*\* (\d+)m',s).group(1); lo,hi = RANGE[mk]
    s = re.sub(r'Exam core: (\S+) words, about (\S+) minutes', f'Exam core: {wc} words, about {round(wc/22)} minutes', s, 1)
    if wc<lo or wc>hi:
        s = s.replace('\n<!--LOC:', f"\n**FAILURE DISCLOSURE:** exam core is {wc} words, {'below' if wc<lo else 'above'} the Section 7 range of {lo}-{hi} for {mk} marks.\n\n<!--LOC:",1)
    out = ['\n## SOURCE LIST', '\n**[SRC] locators** (chapter file, PDF page marker; printed page where the offset is confirmed; verbatim phrase):']
    for k in dict.fromkeys(keys):
        f,ph = L[k]; path,off,cite = F[f]; lab = page_label(k); assert lab, k
        out.append(f"- {cite}, {os.path.basename(path)[:58]}, {lab}: \"{ph}\"")
    if lits:
        out.append('\n**[LIT]** opened this session through PubMed (abstracts only; full texts not read):')
        for k in lits: out.append('- '+LIT[k])
    else:
        out.append('\n**[LIT]** none: no live literature search was used for this answer.')
    out.append('\n## REFERENCES (alphabetical)')
    for r in sorted(set([BOOK[k] for k in refs]+[LIT[k] for k in lits])): out.append('- '+r)
    open(p,'w',encoding='utf8').write(s.rstrip()+'\n'+'\n'.join(out)+'\n')
    print(os.path.basename(p), mk+'m exam words', wc, 'range', lo, hi)
if __name__=='__main__':
    for p in sys.argv[1:]: run(p)
