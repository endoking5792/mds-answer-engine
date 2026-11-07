import re, os, sys
from locators import L, F, page_label, BOOK_EXTRA, LIT
BOOK = {
 'Patel2021': "Patel S, Durack C, Ricucci D, Bakhsh AA. Root resorption. In: Berman LH, Hargreaves KM, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.18.",
 'Andreasen2019': "Andreasen JO, Heithersay GS, Bakland LK. Pathologic tooth resorption. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH USA; 2019. Ch.15 (author line decoded from a damaged OCR heading; verify against the printed book).",
 'Gulabivala2014': "Gulabivala K, Ng YL, editors. Endodontics. 4th ed. Edinburgh: Mosby Elsevier; 2014. Ch.11 Management of tooth resorption (chapter author not named in the file, so the editors are cited).",
 'Baumann2010': "Baumann MA, Beer R, editors. Endodontology. 2nd ed. Stuttgart: Thieme; 2010. Ch.42 Tooth resorption.",
 'Levin2012': "Levin LG. Root resorption. In: Hargreaves KM, Goodis HE, Tay FR, editors. Seltzer and Bender's Dental Pulp. 2nd ed. Chicago: Quintessence; 2012. Ch.17.",
 'Sikri2019': "Sikri VK. Root resorption. In: Essentials of Endodontics. 2nd ed. New Delhi: CBS Publishers; 2019. Ch.27.",
 'AAE2012': "American Association of Endodontists. Glossary of Endodontic Terms. 8th ed. Chicago: AAE; 2012.",
}
BOOK.update(BOOK_EXTRA)
RANGE = {'100':(3200,3500),'75':(2550,3000),'50':(1700,2000),'25':(850,1000),'20':(680,800),'10':(320,400),'7':(230,280),'5':(160,200)}
def run(p):
    s = open(p,encoding='utf8').read().split('\n## SOURCE LIST')[0]
    s = re.sub(r'\n\*\*FAILURE DISCLOSURE:.*\n','\n',s)
    keys = [k.strip() for k in re.search(r'<!--LOC: (.*?)-->',s,re.S).group(1).split(',') if k.strip()]
    refs = [k.strip() for k in re.search(r'<!--REF: (.*?)-->',s,re.S).group(1).split(',') if k.strip()]
    m = re.search(r'<!--LIT: (.*?)-->',s,re.S)
    lits = [k.strip() for k in m.group(1).split(',') if k.strip()] if m else []
    cores = re.findall(r'#{2,4} ✎ Exam core\n(.*?)(?=\n## (?!✎))',s,re.S); wc = sum(len(c.split()) for c in cores)
    mk = re.search(r'\*\*Marks:\*\* (\d+)m',s).group(1); lo,hi = RANGE[mk]
    s = re.sub(r'Exam core: (\S+) words, about (\S+) minutes', f'Exam core: {wc} words, about {round(wc/22)} minutes', s, 1)
    if wc<lo or wc>hi:
        s = s.replace('\n<!--LOC:', f"\n**FAILURE DISCLOSURE:** exam core is {wc} words, {'below' if wc<lo else 'above'} the Section 7 range of {lo}-{hi} for {mk} marks.\n\n<!--LOC:",1)
    out = ['\n## SOURCE LIST', '\n**[SRC] locators** (chapter file, PDF page marker; printed page where the offset is confirmed; verbatim phrase):']
    for k in dict.fromkeys(keys):
        f,ph = L[k]; path,off,cite = F[f]; lab = page_label(k); assert lab, k
        out.append(f"- {cite}, {os.path.basename(path)[:58]}, {lab}: \"{ph}\"")
    if lits:
        out.append('\n**[LIT]** opened this session:')
        for k in lits: out.append('- '+LIT[k])
    else:
        out.append('\n**[LIT]** none: no live literature search was run for this answer.')
    out.append('\n## REFERENCES (alphabetical)')
    for r in sorted(set(BOOK[k] for k in refs)): out.append('- '+r)
    open(p,'w',encoding='utf8').write(s.rstrip()+'\n'+'\n'.join(out)+'\n')
    print(os.path.basename(p), mk+'m exam words', wc, 'range', lo, hi, 'OK' if lo<=wc<=hi else 'OUT OF RANGE')
if __name__=='__main__':
    for p in sys.argv[1:]: run(p)
