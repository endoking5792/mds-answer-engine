import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Bartlett2011': "Bartlett D. Tooth wear. In: Ricketts D, Bartlett D, editors. Advanced Operative Dentistry: A Practical Approach. Edinburgh: Churchill Livingstone Elsevier; 2011. Ch.4.",
 'BartlettRicketts2011': "Bartlett D, Ricketts D. Complex multiple fixed and combined fixed and removable prosthodontics. In: Ricketts D, Bartlett D, editors. Advanced Operative Dentistry: A Practical Approach. Edinburgh: Churchill Livingstone Elsevier; 2011. Ch.16 (section: Management of tooth wear).",
 'Singh2020': "Singh H, Gade V. Non-carious lesions of the tooth surface. In: Singh H. Essentials of Preclinical Conservative Dentistry. 2nd ed. Gurgaon: Wolters Kluwer Health (India); 2020. Ch.21 (chapter stated to be a joint contribution by the author and Dr Vandana Gade).",
 'Banerjee2011': "Banerjee A, Watson TF. Pickard's Manual of Operative Dentistry. 9th ed. Oxford: Oxford University Press; 2011. Ch.1 section 1.3 Toothwear; Ch.2 section 2.6; Ch.4 section 4.3.",
 'Banerjee2015': "Banerjee A, Watson TF. Pickard's Guide to Minimally Invasive Operative Dentistry. 10th ed. Oxford: Oxford University Press; 2015. Ch.1 section 1.3; Ch.2 section 2.6 (Tables 2.7-2.9, BEWE); Ch.3; Ch.9 section 9.4.3.",
 'Goldstein2018': "Goldstein RE, Curtis JW Jr, Farley BA, Siranli S, Clark WA. Abfraction, abrasion, attrition, and erosion. In: Goldstein RE, Chu SJ, Lee EA, Stappert CFJ, editors. Ronald E. Goldstein's Esthetics in Dentistry. 3rd ed. John Wiley & Sons; 2018. Ch.22.",
 'Olley2024': "Olley R, Bartlett D. Aetiology and clinical features of dentine hypersensitivity on all tooth surfaces (full chapter title truncated in the running head). In: Gillam DG, editor. Dentine Hypersensitivity: Advances in Diagnosis, Management, and Treatment. 2nd ed. Cham: Springer Nature Switzerland; 2024. Ch.4.",
 'Marzouk': "Marzouk MA, Simonton AL, Gross RD. Operative Dentistry: Modern Theory and Practice. St Louis: Ishiyaku EuroAmerica (publication year not printed in the extracted front matter). Ch.27 Non-carious destruction and disfigurement of teeth.",
 'Ritter2019': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed. Elsevier; 2019. Ch.20 Non-carious lesions and their management (chapter authors not printed in the file).",
 'Kaidonis2016': "Kaidonis J, Townsend GC, McIntyre J, Richards LC, Hume WR. The oral environment and the main causes of tooth structure loss. In: Mount GJ, Hume WR, Ngo HC, Wolff MS, editors. Preservation and Restoration of Tooth Structure. 3rd ed. Wiley; 2016. Ch.1.",
 'Torres2020': "Torres CRG, et al. Diagnosis and treatment planning (co-authors abbreviated in the running head). In: Torres CRG, editor. Modern Operative Dentistry: Principles for Clinical Practice. Cham: Springer Nature Switzerland; 2020. Ch.1.",
 'Garg2011': "Garg N, Garg A. Textbook of Preclinical Conservative Dentistry. 1st ed. New Delhi: Jaypee Brothers Medical Publishers; 2011. Ch.2 Tooth nomenclature (nomenclature of non-carious defects).",
 'Overton2013': "Overton JD, Hilton TJ, LittleStar ML, Starr CB. Class 5 restorations. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Chicago: Quintessence; 2013. Ch.15 (cited by PDF page; printed page numbers absent from the file).",
}
LIT = {
 'Bartlett2008': "Bartlett D, Ganss C, Lussi A. Basic Erosive Wear Examination (BEWE): a new scoring system for scientific and clinical needs. Clin Oral Investig. 2008;12(Suppl 1):S65-8. PMID 18228057. https://doi.org/10.1007/s00784-007-0181-5 (PubMed abstract read).",
 'Donachie1996': "Donachie MA, Walls AW. The tooth wear index: a flawed epidemiological tool in an ageing population group. Community Dent Oral Epidemiol. 1996;24(2):152-8. PMID 8654038. https://doi.org/10.1111/j.1600-0528.1996.tb00833.x (PubMed abstract read).",
 'BartlettShah2006': "Bartlett DW, Shah P. A critical review of non-carious cervical (wear) lesions and the role of abfraction, erosion, and abrasion. J Dent Res. 2006;85(4):306-12. PMID 16567549. https://doi.org/10.1177/154405910608500405 (PubMed abstract read).",
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
