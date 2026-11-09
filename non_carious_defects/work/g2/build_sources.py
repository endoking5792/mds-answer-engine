import re, os, sys
from locators import L, F, page_label
BOOK = {
 'g2_Bartlett2011': "Bartlett D. Tooth wear. In: Ricketts D, Bartlett D, editors. Advanced Operative Dentistry: A Practical Approach. Edinburgh: Churchill Livingstone Elsevier; 2011. Ch.4.",
 'g2_Torres2020': "Torres CRG, Barbe AG, Noack MJ, Wicht MJ. Diagnosis and treatment planning. In: Torres CRG, editor. Modern Operative Dentistry. Textbooks in Contemporary Dentistry. Cham: Springer Nature Switzerland; 2020. Ch.1.",
 'g2_Bresciani2020': "Bresciani E, Torres CRG, Wiegand A. Dentin hypersensitivity and cracked teeth. In: Torres CRG, editor. Modern Operative Dentistry. Textbooks in Contemporary Dentistry. Cham: Springer Nature Switzerland; 2020. Ch.18.",
 'g2_Olley2024': "Olley R, Bartlett D. Aetiology and clinical features of dentine hypersensitivity on all tooth surfaces and including non-carious cervical lesions (NCCLs). In: Gillam DG, editor. Dentine Hypersensitivity. 2nd ed. Cham: Springer Nature Switzerland; 2024. Ch.4.",
 'g2_Hill2024': "Hill R, Gillam DG. Future strategies for the development of desensitizing products (Ch.9); Remineralization of the early carious lesion with emphasis on available materials used to aid remineralization (Ch.10). In: Gillam DG, editor. Dentine Hypersensitivity. 2nd ed. Cham: Springer Nature Switzerland; 2024.",
 'g2_Goldstein2018': "Goldstein RE, Curtis JW Jr, Farley BA, Siranli S, Clark WA. Abfraction, abrasion, attrition, and erosion (Ch.22); Goldstein RE, Curtis JW Jr, et al. Oral habits (Ch.25). In: Goldstein RE, Chu SJ, Lee EA, Stappert CFJ, editors. Ronald E. Goldstein's Esthetics in Dentistry. 3rd ed. Hoboken: John Wiley & Sons; 2018.",
 'g2_Sikri2020': "Sikri VK. Tooth substance loss. In: Textbook of Conservative and Restorative Dentistry. New Delhi: CBS Publishers; 2020 (first eBook edition). Ch.26.",
 'g2_Banerjee2015': "Banerjee A, Watson TF. Pickard's Guide to Minimally Invasive Operative Dentistry. 10th ed. Oxford: Oxford University Press; 2015. Ch.1 (section 1.3), Ch.2 (section 2.6), Ch.4 (section 4.3).",
 'g2_Singh2020': "Singh H, Gade V. Non-carious lesions of the tooth surface. In: Singh H. Essentials of Preclinical Conservative Dentistry. 2nd ed. Gurgaon: Wolters Kluwer Health (India); 2020. Ch.21.",
 'g2_Ritter2019': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed. Elsevier; 2019. Ch.20 Non-carious lesions and their management (chapter authors not printed in the file).",
 'g2_Rose2013': "Rose WF Jr, Haveman CW, Davis RD. Patient evaluation and problem-oriented treatment planning. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park: Quintessence; 2013. Ch.2 (cited by PDF page).",
 'g2_Kaidonis2016': "Kaidonis J, Richards LC, Townsend GC, Heithersay GS. Non-carious tooth structure loss: diagnosis, risk and activity assessment and clinical management (Ch.4); Ngo HC, Wolff MS, Hume WR. Dental caries: activity and risk assessment (Ch.3). In: Mount GJ, Hume WR, Ngo HC, Wolff MS, editors. Preservation and Restoration of Tooth Structure. 3rd ed. Chichester: Wiley; 2016.",
 'g2_Alani2025': "Alani A, Patel M. Treating anterior tooth surface loss. In: Adhesive Techniques in Restorative Dentistry. BDJ Clinician's Guides. Cham: Springer Nature Switzerland; 2025. Ch.7.",
 'g2_Marzouk': "Marzouk MA, Simonton AL, Gross RD. Operative Dentistry: Modern Theory and Practice. St Louis: Ishiyaku EuroAmerica (publication year not printed). Ch.27 Non-carious destruction and disfigurement of teeth.",
}
LIT = {
 'g2_Schlueter2018': "Schlueter N, Luka B. Erosive tooth wear - a review on global prevalence and on its prevalence in risk groups. Br Dent J. 2018;224(5):364-370. https://doi.org/10.1038/sj.bdj.2018.167 (PMID 29495027; abstract read).",
 'g2_Schlueter2025': "Schlueter N, Mulic A, Luka B. Global prevalence of erosive tooth wear. Monogr Oral Sci. 2025;33:45-71. https://doi.org/10.1159/000543785 (PMID 40435957; abstract read).",
 'g2_Loomans2017': "Loomans B, Opdam N, Attin T, Bartlett D, Edelhoff D, Frankenberger R, et al. Severe tooth wear: European consensus statement on management guidelines. J Adhes Dent. 2017;19(2):111-119. https://doi.org/10.3290/j.jad.a38102 (PMID 28439579; abstract read).",
 'g2_Crins2021': "Crins LAMJ, Opdam NJM, Kreulen CM, Bronkhorst EM, Sterenborg BAMM, Huysmans MCDNJM, Loomans BAC. Randomized controlled trial on the performance of direct and indirect composite restorations in patients with severe tooth wear. Dent Mater. 2021;37(11):1645-1654. https://doi.org/10.1016/j.dental.2021.08.018 (PMID 34497023; abstract read).",
 'g2_daSilva2022': "da Silva BM, Rios D, Foratori-Junior GA, Magalhaes AC, Buzalaf MAR, Peres SCS, Honorio HM. Effect of fluoride group on dental erosion associated or not with abrasion in human enamel: a systematic review with network metanalysis. Arch Oral Biol. 2022;144:105568. https://doi.org/10.1016/j.archoralbio.2022.105568 (PMID 36265394; abstract read).",
 'g2_Trentin2021': "Trentin GA, Mendes LT, Silva BSD, Casagrande L, Araujo FB, Lenzi TL. Reduction in erosive tooth wear using stannous fluoride-containing dentifrices: a meta-analysis. Braz Oral Res. 2021;35:e114. https://doi.org/10.1590/1807-3107bor-2021.vol35.0114 (PMID 34816902; abstract read).",
 'g2_Gomez2026': "Gomez VC, Diaz-Dosque M, Fernandez CE, Bersezio C, Cabello Ibacache R, Fernandez Godoy E. A comprehensive evidence synthesis of anti-erosive dentifrices: an umbrella review of systematic reviews. J Dent. 2026;168:106608. https://doi.org/10.1016/j.jdent.2026.106608 (PMID 41786236; abstract read).",
 'g2_Hong2020': "Hong DW, Lin XJ, Wiegand A, Yu H. Does delayed toothbrushing after the consumption of erosive foodstuffs or beverages decrease erosive tooth wear? A systematic review and meta-analysis. Clin Oral Investig. 2020;24(12):4169-4183. https://doi.org/10.1007/s00784-020-03614-9 (PMID 33052542; abstract read).",
 'g2_Buzalaf2025': "Buzalaf MAR, Magalhaes AC, Rios D, Wiegand A. Prevention and treatment of dental erosion: beyond fluorides. Monogr Oral Sci. 2025;33:216-227. https://doi.org/10.1159/000543569 (PMID 40435950; abstract read).",
 'g2_Rasputnis2021': "Rasputnis W, Schestakow A, Hannig M. The dentin pellicle - a neglected topic in dental research. Arch Oral Biol. 2021;129:105212. https://doi.org/10.1016/j.archoralbio.2021.105212 (PMID 34325346; abstract read).",
 'g2_Camara2026': "Camara JVF, Santos LA, Araujo TT, Buzalaf MAR. Modulation of the acquired enamel pellicle by hemoglobin: a scoping review. J Dent. 2026;172:106741. https://doi.org/10.1016/j.jdent.2026.106741 (PMID 42103063; abstract read).",
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
