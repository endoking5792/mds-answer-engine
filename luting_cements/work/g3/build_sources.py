import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Braga2019': "Braga RR. Materials for adhesion and luting. In: Sakaguchi R, Ferracane J, Powers J, editors. Craig's Restorative Dental Materials. 14th ed. St Louis: Elsevier; 2019. Ch.13.",
 'Anusavice2013': "Anusavice KJ, Shen C, Rawls HR, editors. Phillips' Science of Dental Materials. 12th ed. St Louis: Elsevier Saunders (publication year not printed in the file; Alani and Patel's reading list gives 2013). Ch.12 Bonding and bonding agents; Ch.14 Dental cements (the file lacks a copyright page; year as cited in Alani and Patel's reading list).",
 'vanNoort2013': "van Noort R. Introduction to Dental Materials. 4th ed. Edinburgh: Mosby Elsevier; 2013. Ch.3.8 Luting agents.",
 'Powers2013': "Powers JM, Wataha JC. Dental Materials: Properties and Manipulation. 10th ed. St Louis: Mosby Elsevier; 2013. Ch.7 Cements.",
 'Craig2002': "Craig RG, Powers JM, editors. Restorative Dental Materials. 11th ed. St Louis: Mosby; 2002. Ch.20 Cements.",
 'Sikri2017': "Sikri VK. Indirect Restorations in Dental Practice. 2nd ed. New Delhi: CBS Publishers; 2017 (first eBook edition date; print year not shown in the file). Ch.12 Luting agents.",
 'Ritter2019': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed. Elsevier; 2019. Ch.6 Dental biomaterials; Ch.15 Fundamental concepts of enamel and dentin adhesion (chapter authors not printed in the file).",
 'Breschi2013': "Breschi L, Ferracane JL, Cadenaro M, Mazzoni A, Hilton TJ. Adhesion to enamel and dentin. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park: Quintessence; 2013. Ch.9.",
 'RouseRobbins2013': "Rouse JS, Robbins JW. Porcelain veneers. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park: Quintessence; 2013. Ch.17.",
 'Rouse2013': "Rouse JS. Anterior ceramic crowns. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park: Quintessence; 2013. Ch.18.",
 'Fasbinder2013': "Fasbinder DJ, Neiva G, Robbins JW. Esthetic inlays and onlays. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park: Quintessence; 2013. Ch.19.",
 'Fan2013': "Fan PP, Stevenson R, Berry TG. Cast gold restorations. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park: Quintessence; 2013. Ch.20.",
 'Broome2013': "Broome JC, Robbins JW. Restoration of endodontically treated teeth. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park: Quintessence; 2013. Ch.21.",
 'Alani2025': "Alani A, Patel M. Adhesive Techniques in Restorative Dentistry. BDJ Clinician's Guides. Cham: Springer Nature Switzerland; 2025. Ch.2 Optimising adhesion; Ch.6 Restoring root-canal-treated teeth; Ch.9 Managing tooth replacement.",
}
LIT = {
 'Alvarenga2024': "Alvarenga M, Machado L, Prado A, Veloso S, Monteiro G. Self-adhesive resin cement versus conventional cements on the failure rate of indirect single-tooth restorations: a systematic review and meta-analysis of randomized clinical trials. J Prosthet Dent. 2024;132(5):880.e1-880.e8. https://doi.org/10.1016/j.prosdent.2024.04.027 (PMID 38797576; PubMed abstract read).",
 'Scholz2021': "Scholz KJ, Tabenski IM, Vogl V, Cieplik F, Schmalz G, Buchalla W, Hiller KA, Federlin M. Randomized clinical split-mouth study on the performance of CAD/CAM-partial ceramic crowns luted with a self-adhesive resin cement or a universal adhesive and a conventional resin cement after 39 months. J Dent. 2021;115:103837. https://doi.org/10.1016/j.jdent.2021.103837 (PMID 34624421; PubMed abstract read).",
 'Pfister2023': "Pfister JL, Federlin M, Hiller KA, Schmalz G, Buchalla W, Cieplik F, Scholz KJ. Randomized clinical split-mouth study on partial ceramic crowns luted with a self-adhesive resin cement with or without selective enamel etching: long-term results after 15 years. J Adhes Dent. 2023;25:177-186. https://doi.org/10.3290/j.jad.b4478817 (PMID 37800873; PubMed abstract read).",
 'Pfister2025': "Pfister JL, Cieplik F, Hiller KA, Schenke IM, Schmalz G, Buchalla W, Federlin M, Scholz KJ. Randomized split-mouth clinical trial of CAD-CAM-partial ceramic crowns luted with a self-adhesive resin cement or with a conventional resin cement combined with a universal adhesive after 12 years. Dent Mater. 2026;42(4):628-635 (epub December 2025). https://doi.org/10.1016/j.dental.2025.12.001 (PMID 41402152; PubMed abstract read).",
 'Brondani2017': "Brondani LP, Pereira-Cenci T, Wandsher VF, Pereira GK, Valandro LF, Bergoli CD. Longevity of metal-ceramic crowns cemented with self-adhesive resin cement: a prospective clinical study. Braz Oral Res. 2017;31:e22. https://doi.org/10.1590/1807-3107BOR-2017.vol31.0022 (PMID 28403329; PubMed abstract read).",
}
RANGE = {'100':(3200,3500),'75':(2550,3000),'50':(1700,2000),'25':(850,1000),'20':(680,800),'15':(510,600),'10':(320,400),'7':(320,400),'5':(160,200)}
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
