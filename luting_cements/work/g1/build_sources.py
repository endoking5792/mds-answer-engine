import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Craig2002': "Craig RG, Powers JM, editors. Restorative Dental Materials. 11th ed. St Louis: Mosby; 2002. Ch.20 Cements.",
 'Sakaguchi2019': "Sakaguchi R, Ferracane J, Powers J, editors. Craig's Restorative Dental Materials. 14th ed. St Louis: Elsevier; 2019. Ch.13 Materials for adhesion and luting.",
 'Anusavice': "Anusavice KJ, Shen C, Rawls HR, editors. Phillips' Science of Dental Materials. 12th ed. Elsevier (year of publication not printed in the file). Ch.14 Dental cements.",
 'McCabe2008': "McCabe JF, Walls AWG. Applied Dental Materials. 9th ed. Oxford: Blackwell Publishing; 2008. Ch.27 Requirements of dental cements for lining, base and luting applications; Ch.28 Cements based on phosphoric acid.",
 'vanNoort2013': "van Noort R. Introduction to Dental Materials. 4th ed. Edinburgh: Mosby Elsevier; 2013. Ch.3.8 Luting agents.",
 'Sikri2017': "Sikri VK. Indirect Restorations in Dental Practice. 2nd ed. New Delhi: CBS Publishers (first eBook edition 2017, as printed). Ch.12 Luting agents.",
 'Ritter2019': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed. Elsevier; 2019. Ch.6 Dental biomaterials; Ch.23 Class II cast metal restorations (chapter authors not printed in the file).",
 'Bonsor2013': "Bonsor SJ, Pearson GJ. A Clinical Guide to Applied Dental Materials. Elsevier; 2013. Ch.11 (bonding and luting) and Ch.12 (zinc phosphate cement).",
}
LIT = {
 'Alghauli2022': "Alghauli MA, Alqutaibi AY, Wille S, Kern M. Clinical reliability of self-adhesive luting resins compared to other adhesive procedures: a systematic review and meta-analysis. J Dent. 2023;129:104394. https://doi.org/10.1016/j.jdent.2022.104394 (PubMed abstract read).",
 'Baader2016': "Baader K, Hiller KA, Buchalla W, Schmalz G, Federlin M. Self-adhesive luting of partial ceramic crowns: selective enamel etching leads to higher survival after 6.5 years in vivo. J Adhes Dent. 2016;18(1):69-79. https://doi.org/10.3290/j.jad.a35549 (PubMed abstract read).",
 'Shetty2012': "Shetty RM, Bhat S, Mehta D, Srivatsa G, Shetty YB. Comparative analysis of postcementation hypersensitivity with glass ionomer cement and a resin cement: an in vivo study. J Contemp Dent Pract. 2012;13(3):327-31. https://doi.org/10.5005/jp-journals-10024-1146 (PubMed abstract read).",
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
