import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Jaramillo2015': "Jaramillo DE. Irrigation of the root canal system by laser activation (LAI): PIPS photon-induced photoacoustic streaming. In: Basrani B, editor. Endodontic Irrigation: Chemical Disinfection of the Root Canal System. Cham: Springer; 2015. Ch.13.",
 'Kishen2015': "Kishen A, Shrestha A. Photodynamic therapy for root canal disinfection. In: Basrani B, editor. Endodontic Irrigation: Chemical Disinfection of the Root Canal System. Cham: Springer; 2015. Ch.14.",
 'Pandey2018': "Pandey V. Lasers in Operative Dentistry and Endodontics. New Delhi: CBS; 2018 (first eBook edition). Ch.8 Lasers in endodontics.",
 'GeorgeWalsh2017': "George R, Walsh LJ. Laser-assisted endodontics. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.9.",
 'Muruppel2017': "Muruppel AM. Laser-assisted diagnostics. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 1st ed. Cham: Springer; 2017. Ch.6.",
 'GeorgeWalsh2023': "George R, Walsh LJ. Laser-assisted endodontics. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry—Current Concepts. 2nd ed. Cham: Springer; 2023. Ch.9.",
 'Stabholz2016': "Stabholz A, Sahar-Helft S, Moshonov J. Lasers in endodontics. In: Convissar RA, editor. Principles and Practice of Laser Dentistry. 2nd ed. St Louis: Elsevier; 2016. Ch.13.",
 'Andreasen2007': "Andreasen FM, Andreasen JO, Tsukiboshi M. Examination and diagnosis of dental injuries. In: Textbook and Color Atlas of Traumatic Injuries to the Teeth. 4th ed. Oxford: Blackwell Munksgaard; 2007. Ch.9.",
 'Sikri2019': "Sikri VK. Essentials of Endodontics. 2nd ed. New Delhi: CBS Publishers (second eBook edition 2019). Ch.9 Diagnosis and diagnostic aids; Ch.31 Lasers in endodontics.",
 'Berman2021': "Berman LH, Rotstein I. Diagnosis. In: Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.1.",
 'Kahler2021': "Kahler B. The role of endodontics after dental traumatic injuries. In: Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.21 (author line printed as 'Bill Kahler*'; verify co-authors against the printed book).",
 'Siqueira2022': "Siqueira JF Jr, Rôças IN. Supplementary disinfection of the root canal system. In: Treatment of Endodontic Infections. 2nd ed. Berlin: Quintessence; 2022. Ch.14.",
 'Kishen2017': "Kishen A. Topical antimicrobials in endodontics. In: Endodontic Microbiology. 2nd ed. Hoboken: John Wiley & Sons; 2017. Ch.13.",
 'Guruswamy2026': "Guruswamy Pandian AP, Bellani D, Jibu RM, Agnihotri V. Endodontic intracanal medicaments and agents: the old and the new, what is the evidence? Dent Clin North Am. 2026;70:45-62. https://doi.org/10.1016/j.cden.2025.07.005 (DCNA, read in full).",
 'Mortman2011': "Mortman RE. Technologic advances in endodontics. Dent Clin North Am. 2011;55:461-80. https://doi.org/10.1016/j.cden.2011.02.006 (DCNA, read in full).",
 'Banday2026': "Banday F, Hoskin E, Damodar A, Nachnani K. Lasers in dentistry: practical implications; what is the evidence? Dent Clin North Am. 2026;70:31-44. https://doi.org/10.1016/j.cden.2025.07.004 (DCNA, read in full).",
}
LIT = {
 'deAssis2026': "de Assis HC, Salmon B, Alves Dos Santos GN, Ramirez I, Sousa-Neto MD, Candemil AP, Lopes-Olhê FC. Apical debris extrusion following photon-induced photoacoustic streaming, high-power laser, and other irrigation techniques: a systematic review. Photodiagnosis Photodyn Ther. 2026;60:105545. https://doi.org/10.1016/j.pdpdt.2026.105545 (PMID 42309411; PubMed abstract read).",
 'McGillivray2024': "McGillivray A, Dutta A. The influence of laser-activated irrigation on post-operative pain following root canal treatment: a systematic review. J Dent. 2024;144:104928. https://doi.org/10.1016/j.jdent.2024.104928 (PMID 38484867; PubMed abstract read).",
 'Brum2025': "Brum NF, Lena IM, Buligon MP, Morgental RD. Photon induced photo-acoustic streaming (PIPS) and its ability to remove smear layer and debris: a systematic review. Lasers Med Sci. 2025;41(1):1. https://doi.org/10.1007/s10103-025-04795-z (PMID 41432813; PubMed abstract read).",
 'Natanasabapathy2021': "Natanasabapathy V, Arul B, Srinivasan V, et al. Removal of accumulated hard tissue debris from mesial root of mandibular molars evaluated using micro-CT: a systematic review and network meta-analysis. Evid Based Dent. 2021. https://doi.org/10.1038/s41432-021-0207-x (PMID 34795397; PubMed abstract read).",
 'Quintana2023': "Quintana RM, Scarparo RK, Münchow EA, Pinheiro LS, Tavares CO, Kopper PMP. Does aPDT reduce bacterial load in endodontic infected teeth? A systematic review and meta-analysis. Lasers Med Sci. 2023;38(1):268. https://doi.org/10.1007/s10103-023-03938-4 (PMID 37981598; PubMed abstract read).",
 'OliveiraAguiar2026': "Oliveira-Aguiar J, Salmon B, Lourenço PR, Faria-E-Silva AL, Souza-Gabriel AE, Sousa-Neto MD, Candemil AP. Does adjunctive photodynamic therapy enhance sodium hypochlorite-based root canal disinfection? A systematic review and meta-analysis. Photodiagnosis Photodyn Ther. 2026;58:105400. https://doi.org/10.1016/j.pdpdt.2026.105400 (PMID 41692102; PubMed abstract read).",
 'Mainkar2018': "Mainkar A, Kim SG. Diagnostic accuracy of 5 dental pulp tests: a systematic review and meta-analysis. J Endod. 2018;44(5):694-702. https://doi.org/10.1016/j.joen.2018.01.021 (PMID 29571914; PubMed abstract read).",
 'Adam2022': "Adam M. 'Cold is gold'? The diagnostic accuracy of sensibility and vitality testing techniques. Evid Based Dent. 2022;23(4):137. https://doi.org/10.1038/s41432-022-0847-5 (PMID 36526833; PubMed abstract of this commentary on a systematic review read).",
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
