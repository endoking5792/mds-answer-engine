import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Kidd2016': "Kidd E, Fejerskov O. Essentials of Dental Caries. 4th ed. Oxford: Oxford University Press; 2016. Ch.2 How does a caries lesion develop?; Ch.3 Detection, diagnosis, and recording in the clinic; Ch.4 Control of caries lesion development and progression.",
 'Torres2020': "Torres CRG, editor. Modern Operative Dentistry: Principles for Clinical Practice. Cham: Springer Nature Switzerland; 2020. Ch.3 Cariology (Caneppele TMF et al); Ch.14 (direct anterior composite restorations); Ch.16 Preventive measures and minimally invasive restorative procedures (Borges AB et al).",
 'Hilton2013': "Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Chicago: Quintessence; 2013. Ch.5 (caries detection, diagnosis and management); Ch.16 (tooth bleaching, microabrasion and macroabrasion); chapter on fluoride-releasing materials (orthodontic white spots, MI Paste Plus).",
 'Goldstein2018': "Goldstein RE, Chu SJ, Lee EA, Stappert CFJ, editors. Ronald E. Goldstein's Esthetics in Dentistry. 3rd ed. Hoboken: John Wiley & Sons; 2018. Ch.12 Bleaching discolored teeth; Ch.21 Management of stained and discolored teeth (Goldstein RE, Siranli S, Haywood VB, Caughman WF).",
 'Banerjee2015': "Banerjee A, Watson TF. Pickard's Guide to Minimally Invasive Operative Dentistry. 10th ed. Oxford: Oxford University Press; 2015. Ch.1, Ch.2 (mICDAS; Table 2.7 developmental defects), Ch.4 Disease control and lesion prevention.",
 'Ritter2019': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed. Elsevier; 2019. Ch.2 Dental caries: etiology, clinical characteristics, risk assessment and management; tooth discoloration section (chapter authors not printed in the file).",
 'Sikri2020': "Sikri VK. Textbook of Conservative and Restorative Dentistry. New Delhi: CBS Publishers & Distributors; 2020 (first eBook edition). Ch.32 Tooth discoloration and bleaching.",
 'Machiulskiene2019': "Machiulskiene V. Nyvad criteria for assessment of caries lesion activity and severity. In: Ferreira Zandona A, Longbottom C, editors. Detection and Assessment of Dental Caries: A Clinical Guide. Cham: Springer Nature Switzerland; 2019. Ch.5.",
 'Alani2025': "Alani A, Patel M. Adhesive Techniques in Restorative Dentistry. BDJ Clinician's Guides. Cham: Springer Nature Switzerland; 2025. Ch.3 Management of discoloured teeth (Table 3.2 Icon treatment).",
 'Mount2016': "Mount GJ, Hume WR, Ngo HC, Wolff MS. Preservation and Restoration of Tooth Structure. 3rd ed. Wiley; 2016. Ch.14 Caries in young children.",
 'Fontana2010': "Fontana M, Young DA, Wolff MS, Pitts NB, Longbottom C. Defining dental caries for 2010 and beyond. Dent Clin North Am. 2010;54:423-440. https://doi.org/10.1016/j.cden.2010.03.007 (DCNA, read in full).",
 'Peters2010': "Peters MC. Strategies for noninvasive demineralized tissue repair. Dent Clin North Am. 2010;54:507-525. https://doi.org/10.1016/j.cden.2010.03.005 (DCNA, read in full).",
 'GonzalezCabezas2010': "Gonzalez-Cabezas C. The chemistry of caries: remineralization and demineralization events with direct clinical relevance. Dent Clin North Am. 2010;54:469-478. https://doi.org/10.1016/j.cden.2010.03.004 (DCNA, read in full).",
 'Dayo2021': "Dayo AF, Wolff MS, Syed AZ, Mupparapu M. Radiology of dental caries. Dent Clin North Am. 2021;65:427-445. https://doi.org/10.1016/j.cden.2021.02.002 (DCNA, read in full).",
 'Zhang2017': "Zhang K, Zhang N, Weir MD, Reynolds MA, Bai Y, Xu HHK. Bioactive dental composites and bonding agents having remineralizing and antibacterial characteristics. Dent Clin North Am. 2017;61:669-687. https://doi.org/10.1016/j.cden.2017.05.002 (DCNA, read in full).",
}
LIT = {
 'Bourouni2021': "Bourouni S, Dritsas K, Kloukos D, Wierichs RJ. Efficacy of resin infiltration to mask post-orthodontic or non-post-orthodontic white spot lesions or fluorosis: a systematic review and meta-analysis. Clin Oral Investig. 2021;25(8):4711-4719. https://doi.org/10.1007/s00784-021-03931-7 (PMID 34106348; PubMed abstract read).",
 'Hochli2017': "Höchli D, Hersberger-Zurfluh M, Papageorgiou SN, Eliades T. Interventions for orthodontically induced white spot lesions: a systematic review and meta-analysis. Eur J Orthod. 2017;39(2):122-133. https://doi.org/10.1093/ejo/cjw065 (PMID 27907894; PubMed abstract read).",
 'Bakdach2020': "Bakdach WMM, Hadad R. Effectiveness of different adjunctive interventions in the management of orthodontically induced white spot lesions: a systematic review of systematic reviews and meta-analyses. Dent Med Probl. 2020;57(3):305-325. https://doi.org/10.17219/dmp/118330 (PMID 33064375; PubMed abstract read).",
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
