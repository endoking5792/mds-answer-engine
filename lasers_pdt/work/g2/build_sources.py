import re, os, sys
from locators import L, F, page_label
BOOK = {
 'g2_Poli2017': "Poli R. Laser-assisted restorative dentistry (hard tissue: carious lesion removal and tooth preparation). In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.8.",
 'g2_Parker2017': "Parker SPA. Laser–tissue interaction. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.3.",
 'g2_ParkerParker2017': "Parker PJ, Parker SPA. Laser safety. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.5.",
 'g2_Muruppel2017': "Muruppel AM. Laser-assisted diagnostics. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.6.",
 'g2_Romagnoli2017': "Romagnoli E, Cafaro A. PBM. Theoretical and applied concepts of adjunctive use of LLLT/PBM within clinical dentistry. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.7.",
 'g2_Luk2017': "Luk K, Anagnostaki E. Impact of laser dentistry in management of color in aesthetic zone. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.16.",
 'g2_Poli2023': "Poli R, Buoncristiani F, Dua D, Weintraub J. Laser use in dental caries management. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 2nd ed. Cham: Springer; 2023. Ch.8.",
 'g2_Downs2016': "Downs JC, Convissar RA, Anagnostaki E, Sun G, Hoopingarner CR. Lasers in fixed prosthetic and cosmetic reconstruction. In: Convissar RA, editor. Principles and Practice of Laser Dentistry. 2nd ed. St Louis: Elsevier; 2016. Ch.6.",
 'g2_Parker2016': "Parker S. Lasers in restorative dentistry. In: Convissar RA, editor. Principles and Practice of Laser Dentistry. 2nd ed. St Louis: Elsevier; 2016. Ch.10.",
 'g2_Pandey2018': "Pandey V. Lasers in Operative Dentistry and Endodontics. New Delhi: CBS Publishers; 2018 (first eBook edition). Ch.6 Lasers in operative dentistry.",
 'g2_Sikri2020': "Sikri VK. Textbook of Conservative and Restorative Dentistry. New Delhi: CBS Publishers; 2020 (first eBook edition). Ch.7 (caries diagnosis), Ch.18 (bonding agents), Ch.25 (esthetics).",
 'g2_Mount2016': "Mount GJ, Walsh LJ, Brostek AM. Instruments used in cavity preparation. In: Mount GJ, Hume WR, Ngo HC, Wolff MS, editors. Preservation and Restoration of Tooth Structure. 3rd ed. Chichester: Wiley; 2016. Ch.8.",
 'g2_Goncalves2020': "de Paiva Gonçalves SE, Pucci CR, Torres CRG, Prakki A. Instruments and equipments. In: Torres CRG, editor. Modern Operative Dentistry: Principles for Clinical Practice. Cham: Springer Nature; 2020. Ch.4.",
 'g2_Caprioglio2018': "Caprioglio C, Caprioglio A, Caprioglio D. Pediatric dentistry. In: Goldstein RE, Chu SJ, Lee EA, Stappert CFJ, editors. Ronald E. Goldstein's Esthetics in Dentistry. 3rd ed. Hoboken: Wiley; 2018. Ch.30.",
 'g2_Bonsor2013': "Bonsor SJ, Pearson GJ. A Clinical Guide to Applied Dental Materials. Edinburgh: Churchill Livingstone (Elsevier); 2013. Ch.19.",
 'g2_Neuhaus2019': "Neuhaus KW, Lussi A. DIAGNOdent. In: Ferreira Zandona A, Longbottom C, editors. Detection and Assessment of Dental Caries. Cham: Springer Nature; 2019. Ch.17.",
 'g2_Maltz2019': "Maltz M, Arthur RA, Fatturi-Parolo C. Ch.9 (caries-detecting dyes and the end point of caries excavation). In: Ferreira Zandona A, Longbottom C, editors. Detection and Assessment of Dental Caries. Cham: Springer Nature; 2019 (chapter title not verified from the file).",
 'g2_Banday2026': "Banday F, Hoskin E, Damodar A, Nachnani K. Lasers in dentistry: practical implications; what is the evidence? Dent Clin North Am. 2026;70:31-44. doi:10.1016/j.cden.2025.07.004 (DCNA, read in full).",
 'g2_Flax2011': "Flax HD. Soft and hard tissue management using lasers in esthetic restoration. Dent Clin North Am. 2011;55:383-402. doi:10.1016/j.cden.2011.01.008 (DCNA, read in full).",
 'g2_Green2011': "Green J, Weiss A, Stern A. Lasers and radiofrequency devices in dentistry. Dent Clin North Am. 2011;55:585-97. doi:10.1016/j.cden.2011.02.017 (DCNA, read in full).",
 'g2_Braga2010': "Braga MM, Mendes FM, Ekstrand KR. Detection activity assessment and diagnosis of dental caries lesions. Dent Clin North Am. 2010;54:479-93. doi:10.1016/j.cden.2010.03.006 (DCNA, read in full).",
 'g2_Rochlen2011': "Rochlen GK, Wolff MS. Technological advances in caries diagnosis. Dent Clin North Am. 2011;55:441-52. doi:10.1016/j.cden.2011.02.018 (DCNA, read in full).",
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
