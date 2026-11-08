import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Anusavice': "Anusavice KJ, Shen C, Rawls HR, editors. Phillips' Science of Dental Materials. 12th ed. St Louis: Elsevier Saunders (publication year not printed in the file). Ch.14 Dental cements.",
 'Sakaguchi2019': "Pfeifer CS. Materials for adhesion and luting. In: Sakaguchi R, Ferracane J, Powers J, editors. Craig's Restorative Dental Materials. 14th ed. St Louis: Elsevier; 2019. Ch.13.",
 'Craig2002': "Craig RG, Powers JM, editors. Restorative Dental Materials. 11th ed. St Louis: Mosby; 2002. Ch.20 Cements.",
 'McCabe2008': "McCabe JF, Walls AWG. Applied Dental Materials. 9th ed. Oxford: Blackwell Publishing; 2008. Ch.2 (thermal properties), Ch.24 (glass ionomer cements), Ch.28 (cements based on phosphoric acid).",
 'vanNoort2013': "van Noort R (with contributions by Barbour ME). Introduction to Dental Materials. 4th ed. Edinburgh: Mosby Elsevier; 2013. Ch.3.8 Luting agents.",
 'Powers2013': "Powers JM, Wataha JC. Dental Materials: Properties and Manipulation. 10th ed. St Louis: Mosby Elsevier; 2013. Ch.7 Cements (and Appendix 7a).",
 'Bhat2019': "Bhat VS, Nandish BT, Jayaprakash K. Science of Dental Materials with Clinical Applications. 3rd ed (eBook). New Delhi: CBS Publishers; 2019. Restorative materials: dental cements.",
 'Bonsor2013': "Bonsor SJ, Pearson GJ. A Clinical Guide to Applied Dental Materials. Edinburgh: Churchill Livingstone Elsevier; 2013. Ch.10 Resin-modified glass ionomer cements; Ch.11 Bonding.",
 'Sikri2017': "Sikri VK. Indirect Restorations in Dental Practice. 2nd ed (eBook). New Delhi: CBS Publishers; 2017. Ch.12 Luting agents.",
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
