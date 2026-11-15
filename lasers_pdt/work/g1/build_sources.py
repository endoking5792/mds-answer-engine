import re, os, sys
from locators import L, F, page_label
BOOK = {
 'g1_Pandey2018': "Pandey V. Lasers in Operative Dentistry and Endodontics. New Delhi: CBS Publishers; 2018 (first eBook edition; printed page numbers not visible in the file). Ch.1-8, 10, 11.",
 'g1_Coluzzi2017': "Coluzzi DJ. Laser and light fundamentals. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.2.",
 'g1_Parker2017': "Parker SPA. Laser–tissue interaction. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.3.",
 'g1_ParkerParker2017': "Parker PJ, Parker SPA. Laser safety. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.5.",
 'g1_Romagnoli2017': "Romagnoli E, Cafaro A. PBM: theoretical and applied concepts of adjunctive use of LLLT/PBM within clinical dentistry. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.7.",
 'g1_Poli2017': "Poli R. Laser-assisted restorative dentistry (hard tissue: carious lesion removal and tooth preparation). In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.8.",
 'g1_GeorgeWalsh2017': "George R, Walsh LJ. Laser-assisted endodontics. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.9.",
 'g1_Rechmann2017': "Rechmann P. Current research and future dreams: the second generation of hard tissue lasers. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.17.",
 'g1_Poli2023': "Poli R, Buoncristiani F, Dua D, Weintraub J. Laser use in dental caries management. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 2nd ed. Cham: Springer; 2023. Ch.8.",
 'g1_GeorgeWalsh2023': "George R, Walsh LJ. Laser-assisted endodontics. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 2nd ed. Cham: Springer; 2023. Ch.9.",
 'g1_Sulewski2016': "Sulewski JG. Einstein's 'splendid light': origins and dental applications. In: Convissar RA, editor. Principles and Practice of Laser Dentistry. 2nd ed. St Louis: Elsevier; 2016. Ch.1.",
 'g1_Parker2016': "Parker S. Lasers in restorative dentistry. In: Convissar RA, editor. Principles and Practice of Laser Dentistry. 2nd ed. St Louis: Elsevier; 2016. Ch.10.",
 'g1_Stabholz2016': "Stabholz A, Sahar-Helft S, Moshonov J. Lasers in endodontics. In: Convissar RA, editor. Principles and Practice of Laser Dentistry. 2nd ed. St Louis: Elsevier; 2016. Ch.13.",
 'g1_Tuner2016': "Tunér J, Beck-Kristensen PH, Ross G, Ross A. Photobiomodulation in dentistry. In: Convissar RA, editor. Principles and Practice of Laser Dentistry. 2nd ed. St Louis: Elsevier; 2016. Ch.15.",
 'g1_Gopikrishna2021': "Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. Wolters Kluwer; 2021. Ch.24 Lasers in endodontics.",
 'g1_Sikri2019': "Sikri VK. Lasers in endodontics. In: Essentials of Endodontics. 2nd ed. New Delhi: CBS Publishers; 2019. Ch.31.",
 'g1_Alshahrani2016': "Alshahrani M, Beebe B, Chogle SM. Lasers. In: Jain P, editor. Current Therapy in Endodontics. 1st ed. Ames: John Wiley & Sons; 2016. Ch.10 (year as used elsewhere in this bank; verify against the printed book).",
 'g1_Goodis2012': "Goodis HE, Pashley DH. Effects of thermal and mechanical challenges. In: Hargreaves KM, Goodis HE, Tay FR, editors. Seltzer and Bender's Dental Pulp. 2nd ed. Chicago: Quintessence; 2012. Ch.15.",
 'g1_Banday2026': "Banday F, Hoskin E, Damodar A, Nachnani K. Lasers in dentistry: practical implications; what is the evidence? Dent Clin North Am 2026;70:31-44. doi:10.1016/j.cden.2025.07.004 (DCNA, full text read).",
 'g1_Green2011': "Green J, Weiss A, Stern A. Lasers and radiofrequency devices in dentistry. Dent Clin North Am 2011;55:585-597. doi:10.1016/j.cden.2011.02.017 (DCNA, full text read).",
}
LIT = {}
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
