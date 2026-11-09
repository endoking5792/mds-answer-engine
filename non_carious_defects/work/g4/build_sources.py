import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Singh2020': "Singh H. Essentials of Preclinical Conservative Dentistry. 2nd ed. Gurgaon: Wolters Kluwer Health (India); 2020. Ch.21 Non-carious lesions of the tooth surface (joint contribution with V Gade).",
 'Ritter2019': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed. Elsevier; 2019. Ch.19 Clinical technique for direct composite resin and glass ionomer restorations; Ch.20 Non-carious lesions and their management (chapter authors not printed in the file).",
 'Overton2013': "Overton JD, Hilton TJ, LittleStar ML, Starr CB. Class 5 restorations. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Chicago: Quintessence; 2013. Ch.15.",
 'Goldstein2018': "Goldstein RE, Curtis JW Jr, Farley BA, Siranli S, Clark WA. Abfraction, abrasion, attrition, and erosion. In: Goldstein RE, Chu SJ, Lee EA, Stappert CFJ, editors. Ronald E. Goldstein's Esthetics in Dentistry. 3rd ed. Hoboken: John Wiley & Sons; 2018. Ch.22.",
 'Mount2016': "Mount GJ, Hume WR, Ngo HC, Wolff MS, editors. Preservation and Restoration of Tooth Structure. 3rd ed. Chichester: John Wiley & Sons; 2016. Ch.7 Principles of cavity design for the restoration of advanced lesions; Ch.9 Glass-ionomer materials; Ch.13 Choosing between restoration modalities; and the restoration-failure chapter (p.296).",
 'Kaidonis2016a': "Kaidonis J, Townsend GC, McIntyre J, Richards LC, Hume WR. The oral environment and the main causes of tooth structure loss. In: Mount GJ, Hume WR, Ngo HC, Wolff MS, editors. Preservation and Restoration of Tooth Structure. 3rd ed. Chichester: John Wiley & Sons; 2016. Ch.1. (Cited in text as Kaidonis et al, 2016a.)",
 'Kaidonis2016': "Kaidonis J, Richards LC, Townsend GC, Heithersay GS. Non-carious tooth structure loss: diagnosis, risk and activity assessment and clinical management. In: Mount GJ, Hume WR, Ngo HC, Wolff MS, editors. Preservation and Restoration of Tooth Structure. 3rd ed. Chichester: John Wiley & Sons; 2016. Ch.4. (Cited in text as Kaidonis et al, 2016b.)",
 'Olley2024': "Olley R, Bartlett D. Aetiology and clinical features of dentine hypersensitivity on all tooth surfaces. In: Gillam DG, editor. Dentine Hypersensitivity: Advances in Diagnosis, Management, and Treatment. 2nd ed. Cham: Springer Nature Switzerland; 2024. Ch.4.",
 'Bartlett2011': "Bartlett D. Tooth wear. In: Ricketts D, Bartlett D, editors. Advanced Operative Dentistry: A Practical Approach. Edinburgh: Elsevier; 2011. Ch.4.",
 'Torres2020': "Torres CRG, et al. Diagnosis and treatment planning. In: Torres CRG, editor. Modern Operative Dentistry: Principles for Clinical Practice. Cham: Springer Nature Switzerland; 2020. Ch.1.",
 'TorresZanatta2020': "Torres CRG, Zanatta RF. Composite restoration on anterior teeth. In: Torres CRG, editor. Modern Operative Dentistry: Principles for Clinical Practice. Cham: Springer Nature Switzerland; 2020. Ch.14.",
 'Alani2025': "Alani A, Patel M. Adhesive Techniques in Restorative Dentistry. BDJ Clinician's Guides. Cham: Springer Nature Switzerland; 2025. Ch.7 Treating anterior tooth surface loss.",
 'Banerjee2015': "Banerjee A, Watson TF. Pickard's Guide to Minimally Invasive Operative Dentistry. 10th ed. Oxford: Oxford University Press; 2015. Ch.1, section 1.3 Tooth wear.",
 'Garg2011': "Garg N, Garg A. Textbook of Preclinical Conservative Dentistry. 1st ed. New Delhi: Jaypee Brothers Medical Publishers; 2011. Ch.2.",
 'Marzouk': "Marzouk MA, Simonton AL, Gross RD. Operative Dentistry: Modern Theory and Practice. St Louis: Ishiyaku EuroAmerica (Indian edition; year not printed in the file). Ch.27 Non-carious destruction and disfigurement of teeth.",
 'BedranRusso2017': 'Bedran-Russo A, Leme-Kraus AA, Vidal CMP, Teixeira EC. An overview of dental adhesive systems and the dynamic tooth-adhesive interface. Dent Clin North Am. 2017;61:713-731. https://doi.org/10.1016/j.cden.2017.06.001 (full text read; issue number not printed on the first page).',
 'Fronza2022': 'Fronza BM, Braga RR, Cadenaro M. Dental adhesives: surface modifications of dentin structure for stable bonding. Dent Clin North Am. 2022;66:503-515. https://doi.org/10.1016/j.cden.2022.05.002 (full text read; issue number not printed on the first page).',
 'Puckett2007': 'Puckett AD, Fitchie JG, Kirk PC, Gamblin J. Direct composite restorative materials. Dent Clin North Am. 2007;51:659-675. https://doi.org/10.1016/j.cden.2007.04.003 (full text read; issue number not printed on the first page).',
 'Pfeifer2017': 'Pfeifer CS. Polymer-based direct filling materials. Dent Clin North Am. 2017;61:733-750. https://doi.org/10.1016/j.cden.2017.06.002 (full text read; issue number not printed on the first page).',
 'Yanase2014': 'Yanase RT, Le HH. Caries management by risk assessment care paths for prosthodontic patients: oral microbial control and management. Dent Clin North Am. 2014;58:227-245. https://doi.org/10.1016/j.cden.2013.09.013 (full text read; issue number not printed on the first page).',
}
LIT = {
 'Schroeder2015': "Schroeder M, Reis A, Luque-Martinez I, Loguercio AD, Masterson D, Maia LC. Effect of enamel bevel on retention of cervical composite resin restorations: a systematic review and meta-analysis. J Dent. 2015;43(7):777-88. https://doi.org/10.1016/j.jdent.2015.02.017 (PMID 25765866; PubMed abstract read).",
 'ChapleGil2026': "Chaple Gil AM, Pereda Vazquez L, Santiesteban Velazquez M, Menendez JJ. Comparison of adhesive strategies with different etching approaches on the clinical performance of restorations in non-carious cervical lesions: a systematic review and network meta-analysis. J Funct Biomater. 2026;17(4):160. https://doi.org/10.3390/jfb17040160 (PMID 42042267; PubMed abstract read).",
 'Lawson2015': "Lawson NC, Robles A, Fu CC, Lin CP, Sawlani K, Burgess JO. Two-year clinical trial of a universal adhesive in total-etch and self-etch mode in non-carious cervical lesions. J Dent. 2015;43(10):1229-34. https://doi.org/10.1016/j.jdent.2015.07.009 (PMID 26231300; PubMed abstract read).",
 'Luhrs2020': "Luhrs AK, Jacker-Guhr S, Gunay H, Herrmann P. Composite restorations placed in non-carious cervical lesions: which cavity preparation is clinically reliable? Clin Exp Dent Res. 2020;6(5):558-67. https://doi.org/10.1002/cre2.310 (PMID 32924312; PubMed abstract read).",
 'Duangthip2017': "Duangthip D, Man A, Poon PH, Lo ECM, Chu CH. Occlusal stress is involved in the formation of non-carious cervical lesions. A systematic review of abfraction. Am J Dent. 2017;30(4):212-20. PMID 29178704 (no DOI listed in PubMed; abstract read).",
 'Dioguardi2024': "Dioguardi M, Spirito F, Lo Muzio E, et al. Investigation of the presence of non-carious cervical lesions (NCCLs) in ancient adult skulls: a systematic review and meta-analysis. BMC Oral Health. 2024;24(1):370. https://doi.org/10.1186/s12903-024-04154-4 (PMID 38519922; PubMed abstract read).",
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
