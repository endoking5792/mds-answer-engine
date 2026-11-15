import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Coluzzi2017': "Coluzzi DJ. Laser and light fundamentals. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.2.",
 'Parker2017': "Parker SPA. Laser–tissue interaction. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.3.",
 'Selting2017': "Selting W. Laser operating parameters for hard and soft tissue, surgical and PBM management. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.4.",
 'ParkerParker2017': "Parker PJ, Parker SPA. Laser safety. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.5.",
 'ColuzziParker2017': "Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Glossary.",
 'Coluzzi2023': "Coluzzi DJ. Laser and light fundamentals. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 2nd ed. Cham: Springer; 2023. Ch.2.",
 'ParkerParker2023': "Parker PJ, Parker SPA. Laser safety in dentistry. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 2nd ed. Cham: Springer; 2023. Ch.5.",
 'Coluzzi2016': "Coluzzi DJ, Convissar RA, Roshkind DM. Laser fundamentals. In: Convissar RA, editor. Principles and Practice of Laser Dentistry. 2nd ed. St Louis: Elsevier; 2016. Ch.2.",
 'Roshkind2016': "Roshkind DM, Convissar RA. Introducing lasers into the dental practice. In: Convissar RA, editor. Principles and Practice of Laser Dentistry. 2nd ed. St Louis: Elsevier; 2016. Ch.16.",
 'Pandey2018_P1': "Pandey V. Lasers in Operative Dentistry and Endodontics. New Delhi: CBS Publishers; 2018 (first eBook edition). Ch.2 Fundamentals of laser; Ch.4 Laser–tissue interaction; Ch.5 Classification of lasers (cited by PDF page; printed page numbers not visible in the file).",
 'Pandey2018_P2': "Pandey V. Lasers in Operative Dentistry and Endodontics. New Delhi: CBS Publishers; 2018 (first eBook edition). Ch.10 Laser safety (cited by PDF page; printed page numbers not visible in the file).",
 'Green2011': "Green J, Weiss A, Stern A. Lasers and radiofrequency devices in dentistry. Dent Clin North Am. 2011;55:585–97. https://doi.org/10.1016/j.cden.2011.02.017 (DCNA, full text read).",
 'Banday2026': "Banday F, Hoskin E, Damodar A, Nachnani K. Lasers in dentistry: practical implications; what is the evidence? Dent Clin North Am. 2026;70:31–44 (published online 2025). https://doi.org/10.1016/j.cden.2025.07.004 (DCNA, full text read).",
 'Oliveira2022': "Oliveira D, Rocha MG. Dental light-curing—assessing the blue-light hazard. Dent Clin North Am. 2022;66:537–50. https://doi.org/10.1016/j.cden.2022.05.004 (DCNA, full text read).",
}
LIT = {
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
