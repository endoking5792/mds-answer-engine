import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Mohammadi2015': "Mohammadi Z, Azarpazhooh A. Ozone application in endodontics. In: Basrani B, editor. Endodontic Irrigation: Chemical Disinfection of the Root Canal System. Cham: Springer International Publishing Switzerland; 2015. Ch.12.",
 'Kishen2017': "Kishen A. Topical antimicrobials in endodontics. In: Fouad AF, editor. Endodontic Microbiology. 2nd ed. Hoboken (NJ): John Wiley & Sons; 2017. Ch.13.",
 'Baumann2010': "Baumann MA, Beer R, editors. Endodontology. 2nd ed (English translation of the 2nd German edition). Stuttgart: Thieme; 2010. Ch.25 Root canal disinfection (chapter author not printed in the file; verify against the printed book).",
 'PetersCohen2021': "Peters OA, Peters CI, Basrani B. Cleaning and shaping of the root canal system. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.8.",
 'Borges2020': "Borges AB, Torres CRG, Schlueter N. Preventive measures and minimally invasive restorative procedures. In: Torres CRG, editor. Modern Operative Dentistry: Principles for Clinical Practice. Cham: Springer Nature; 2020. Ch.16.",
 'Sikri2020': "Sikri VK. Textbook of Conservative and Restorative Dentistry. New Delhi: CBS Publishers (first eBook edition 2020). Ch.27 (root caries) and Ch.28 Minimal intervention dentistry.",
 'Bonsor2013': "Bonsor SJ, Pearson GJ. A Clinical Guide to Applied Dental Materials. Edinburgh: Elsevier; 2013. Ch.13 (endodontic materials; ozone and bacterial PDT).",
 'Caprioglio2018': "Caprioglio C, Caprioglio A, Caprioglio D. Pediatric dentistry. In: Goldstein RE, Chu SJ, Lee EA, Stappert CFJ, editors. Ronald E. Goldstein's Esthetics in Dentistry. 3rd ed. Hoboken (NJ): John Wiley & Sons; 2018. Ch.30.",
 'Fontana2016': "Fontana M, Walsh LJ, Amaechi BT, Ngo HC. Aids to remineralization. In: Mount GJ, Hume WR, Ngo HC, Wolff MS, editors. Preservation and Restoration of Tooth Structure. 3rd ed. Chichester: John Wiley & Sons; 2016. Ch.5.",
 'George2017': "George R, Walsh LJ. Laser-assisted endodontics. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry: Current Concepts. 1st ed. Cham: Springer; 2017. Ch.9.",
 'George2023': "George R, Walsh LJ. Laser-assisted endodontics. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry: Current Concepts. 2nd ed. Cham: Springer; 2023. Ch.9.",
 'Guruswamy2026': "Guruswamy Pandian AP, Bellani D, Jibu RM, Agnihotri V. Endodontic intracanal medicaments and agents: the old and the new, what is the evidence? Dent Clin North Am. 2026;70:45-62 (DCNA PDF; irrigant and ozone sections read, remainder scanned).",
 'PetersEPP2021': "Peters OA, Arias A, Shabahang S. Cleaning and shaping. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.14.",
 'Teixeira2021': "Teixeira FB, Cheung GSP. Management of endodontic emergencies. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.19.",
 'Nair2021': "Nair MK, Levin MD, Nair UP. Radiographic interpretation. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.2.",
 'Hulsmann2022': "Hülsmann M, Schäfer E, Bürklein S. Management of posttreatment apical periodontitis: nonsurgical retreatment and periradicular surgery. In: Siqueira JF Jr, Rôças IN, editors. Treatment of Endodontic Infections. 2nd ed. Berlin: Quintessence; 2022. Ch.17.",
 'Versiani2021': "Versiani M, Cleghorn B, Christie W. Root canal anatomy. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.12.",
 'Cavalcanti2024': "Cavalcanti B, Chiego D Jr. The importance of maintaining pulp vitality. In: Duncan HF, El-Karim IA, editors. Vital Pulp Treatment. 1st ed. Chichester: John Wiley & Sons; 2024. Ch.1.",
 'Renne2023': "Renne W, DeFee M. 3D Printing in Restorative Dentistry. 3rd ed. WRMDSV II LLC / The MOD Institute; 2023 (practice e-book; not peer reviewed).",
 'Watanabe2022': "Watanabe H, Fellows C, An H. Digital technologies for restorative dentistry. Dent Clin North Am. 2022;66:567-590 (DCNA PDF; manufacturing and additive manufacturing sections read, remainder scanned).",
}
LIT = {
 'Rickard2004': "Rickard GD, Richardson R, Johnson T, McColl D, Hooper L. Ozone therapy for the treatment of dental caries. Cochrane Database Syst Rev. 2004;(3):CD004153. https://doi.org/10.1002/14651858.CD004153.pub2 PMID 15266519 (abstract only). Withdrawn: Cochrane Database Syst Rev. 2019;2:CD004153. https://doi.org/10.1002/14651858.CD004153.pub3 PMID 30731019 (withdrawal notice record; reason for withdrawal not shown in the abstract).",
 'Silva2020': "Silva EJNL, Prado MC, Soares DN, Hecksher F, Martins JNR, Fidalgo TKS. The effect of ozone therapy in root canal disinfection: a systematic review. Int Endod J. 2020;53(3):317-332. https://doi.org/10.1111/iej.13229 PMID 31587303 (abstract only).",
 'Shetty2022': "Shetty N, Mathew T, Shetty A, Hegde MN, Attavar S. Ozonated water as an irrigant in disinfecting root canal systems: a systematic review. Evid Based Dent. 2022. https://doi.org/10.1038/s41432-022-0800-7 PMID 36076032 (abstract only).",
 'Vera2015': "Vera J, Ochoa-Rivera J, Vazquez-Carcaño M, Romero M, Arias A, Sleiman P. Effect of intracanal cryotherapy on reducing root surface temperature. J Endod. 2015;41(11):1884-7. https://doi.org/10.1016/j.joen.2015.08.009 PMID 26433855 (abstract only).",
 'Vera2018': "Vera J, Ochoa J, Romero M, et al. Intracanal cryotherapy reduces postoperative pain in teeth with symptomatic apical periodontitis: a randomized multicenter clinical trial. J Endod. 2018;44(1):4-8. https://doi.org/10.1016/j.joen.2017.08.038 PMID 29079057 (abstract only).",
 'Sadaf2020': "Sadaf D, Ahmad MZ, Onakpoya IJ. Effectiveness of intracanal cryotherapy in root canal therapy: a systematic review and meta-analysis of randomized clinical trials. J Endod. 2020;46(12):1811-1823.e1. https://doi.org/10.1016/j.joen.2020.08.022 PMID 32916207 (abstract only).",
 'Monteiro2021': "Monteiro LPB, Guerreiro MYR, de Castro Valino R, Magno MB, Maia LC, da Silva Brandão JM. Effect of intracanal cryotherapy application on postoperative endodontic pain: a systematic review and metaanalysis. Clin Oral Investig. 2021;25(1):23-35. https://doi.org/10.1007/s00784-020-03693-8 PMID 33222053 (abstract only).",
 'Almohaimede2021': "Almohaimede A, Al-Madi E. Is intracanal cryotherapy effective in reducing postoperative endodontic pain? An updated systematic review and meta-analysis of randomized clinical trials. Int J Environ Res Public Health. 2021;18(22):11750. https://doi.org/10.3390/ijerph182211750 PMID 34831517 (abstract only).",
 'Hespanhol2022': "Hespanhol FG, Guimarães LS, Antunes LAA, Antunes LS. Effect of intracanal cryotherapy on postoperative pain after endodontic treatment: systematic review with meta-analysis. Restor Dent Endod. 2022;47(3):e30. https://doi.org/10.5395/rde.2022.47.e30 PMID 36090511 (abstract only).",
 'Huang2026': "Huang Q, Cui C, Fan J, Zhao J. Cryotherapy as an adjunct in root canal therapy: a systematic review and meta-analysis. Lasers Med Sci. 2026;41(1). https://doi.org/10.1007/s10103-026-04847-y PMID 42611134 (abstract only).",
 'Mohamed2026': "Mohamed M, Abdelmajeed A, Salah-Uddin Anwar Laithy M, Abozaid D. Effectiveness of intracanal cryotherapy in reducing post-endodontic pain in irreversible pulpitis: a systematic review and meta-analysis. Sci Rep. 2026;16(1). https://doi.org/10.1038/s41598-026-47860-5 PMID 42031860 (abstract only).",
 'Ajeesh2023': "Ajeesh K, Jayasree S, James EP, Pooja KP, Jauhara F. Comparative evaluation of the effectiveness of intracanal and intraoral cryotherapy on postendodontic pain in patients with symptomatic apical periodontitis: a randomized clinical trial. J Conserv Dent Endod. 2023;26(5):555-559. https://doi.org/10.4103/jcd.jcd_284_23 PMID 38292358 (abstract only).",
 'Hamza2024': "Hamza EM, Abd El Aziz TM, Obeid MF. The influence of intraoral cryotherapy on postoperative pain and substance P in symptomatic apical periodontitis: randomized clinical study. Sci Rep. 2024;14(1):13890. https://doi.org/10.1038/s41598-024-64071-y PMID 38880787 (abstract only).",
 'Alhawiti2026': "Alhawiti W, Ali K. Clinical applications and outcomes of static-guided endodontics in teeth with pulp canal obliteration: a scoping review. J Endod. 2026. https://doi.org/10.1016/j.joen.2026.09.008 PMID 42790733 (abstract only).",
 'Verweij2017': "Verweij JP, Jongkees FA, Anssari Moin D, Wismeijer D, van Merkesteyn JPR. Autotransplantation of teeth using computer-aided rapid prototyping of a three-dimensional replica of the donor tooth: a systematic literature review. Int J Oral Maxillofac Surg. 2017;46(11):1466-1474. https://doi.org/10.1016/j.ijom.2017.04.008 PMID 28478868 (abstract only).",
 'Almutairi2026': "Almutairi AS, Alnoodaly OM, Alrasheed SM, Ansari ST, Kolarkodi SH. Digitally guided tooth autotransplantation: a systematic review of clinical, radiographic and operative outcomes. J Clin Med. 2026;15(21):8601. https://doi.org/10.3390/jcm15218601 PMID 43030743 (abstract only).",
 'Forte2026': "Forte AG, Leite JVC, Souza APC, Ribeiro FR, Lima RBW, Sinhoreti MAC, Correr AB. Engineered biomaterial-based scaffolds for dentin-pulp complex regeneration: applications and biological performance, a scoping review. Odontology. 2026. https://doi.org/10.1007/s10266-026-01433-0 PMID 42380706 (abstract only).",
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
