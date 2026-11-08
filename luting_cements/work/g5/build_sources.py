import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Ritter2019': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed. Elsevier; 2019. Ch.23 Class II cast metal restorations (chapter author not printed in the file).",
 'Fan2013': "Fan PP, Stevenson R, Berry TG. Cast gold restorations. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park: Quintessence; 2013. Ch.20.",
 'Marzouk': "Marzouk MA, Simonton AL, Gross RD. Operative Dentistry: Modern Theory and Practice. St Louis: Ishiyaku EuroAmerica (publication year not printed). Ch.25 Casting pre-cementation, cementation, and post-cementation adjustments.",
 'Sikri2017': "Sikri VK. Indirect Restorations in Dental Practice. 2nd ed. New Delhi: CBS Publishers & Distributors; 2017 (first eBook edition). Ch.12 Luting agents.",
 'Sakaguchi2019': "Sakaguchi R, Ferracane J, Powers J, editors. Craig's Restorative Dental Materials. 14th ed. St Louis: Elsevier; 2019. Ch.10 (noble alloys: carat and fineness), Ch.12 (brazing investment), Ch.13 (bonding to cast alloys), Ch.14 (resin-modified glass-ionomer cements).",
 'Craig2002': "Craig RG, Powers JM, editors. Restorative Dental Materials. 11th ed. St Louis: Mosby; 2002. Ch.15 Noble dental alloys and solders; Ch.17 Casting and soldering procedures.",
 'Anusavice2013': "Anusavice KJ, Shen C, Rawls HR, editors. Phillips' Science of Dental Materials. 12th ed. St Louis: Elsevier Saunders (publication year not printed in the file). Ch.16 Dental casting alloys and metal joining.",
 'McCabe2008': "McCabe JF, Walls AWG. Applied Dental Materials. 9th ed. Oxford: Blackwell Publishing; 2008. Ch.7, section 7.7 Soldering and brazing materials for noble metals.",
 'Bhat2019': "Bhat VS, Nandish BT, Jayaprakash K. Science of Dental Materials with Clinical Applications. 3rd ed. New Delhi: CBS Publishers & Distributors; 2019 (eBook). Ch.23 Brazing and welding.",
 'Rudolf2024': "Rudolf R, Majeric P, Lazic V, Raic KT. Nanofoils in dental joining practice. In: Advanced Dental Metallic Materials. Springer Series in Materials Science 338. Cham: Springer Nature Switzerland; 2024. Ch.6. https://doi.org/10.1007/978-3-031-47351-7_6",
}
LIT = {
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
