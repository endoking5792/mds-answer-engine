import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Ritter2019': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asia ed. Elsevier; 2019. Ch.1 Clinical significance of dental anatomy, histology, physiology and occlusion.",
 'Ritter2019b': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asia ed. Elsevier; 2019. Ch.6 Dental biomaterials.",
 'Marzouk1985': "Marzouk MA, Simonton AL, Gross RD. Operative Dentistry: Modern Theory and Practice. St Louis: Ishiyaku EuroAmerica; 1985.",
 'Sikri2020': "Sikri VK. Textbook of Conservative and Restorative Dentistry. New Delhi: CBS Publishers; 2020.",
 'Haug2019': "Haug SR, Kim S, Heyeraas KJ. Structure and function of the pulp-dentin complex. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.2.",
 'Smith2012': "Smith AJ. Formation and repair of dentin in the adult. In: Hargreaves KM, Goodis HE, Tay FR, editors. Seltzer and Bender's Dental Pulp. 2nd ed. Chicago: Quintessence; 2012. Ch.2.",
 'Ritter2019c': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asia ed. Elsevier; 2019. Ch.10 Periodontology applied to operative dentistry.",
 'Rose2013': "Rose WF Jr, Haveman CW, Davis RD. Patient evaluation and problem-oriented treatment planning. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Chicago: Quintessence; 2013. Ch.2.",
 'Fruits2013': "Fruits TJ, Khajotia SS, Nicholson JW. Biologic considerations. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Chicago: Quintessence; 2013. Ch.1.",
}
RANGE = {'100':(3200,3500),'75':(2550,3000),'50':(1700,2000),'25':(850,1000),'20':(680,800),'10':(320,400),'7':(230,280),'5':(160,200)}
def run(p):
    s = open(p,encoding='utf8').read().split('\n## SOURCE LIST')[0]
    s = re.sub(r'\n\*\*FAILURE DISCLOSURE:.*\n','\n',s)
    keys = [k.strip() for k in re.search(r'<!--LOC: (.*?)-->',s,re.S).group(1).split(',') if k.strip()]
    refs = [k.strip() for k in re.search(r'<!--REF: (.*?)-->',s,re.S).group(1).split(',') if k.strip()]
    cores = re.findall(r'#{2,4} ✎ Exam core\n(.*?)(?=\n## (?!✎))',s,re.S); wc = sum(len(c.split()) for c in cores)
    mk = re.search(r'\*\*Marks:\*\* (\d+)m',s).group(1); lo,hi = RANGE[mk]
    s = re.sub(r'Exam core: (\S+) words, about (\S+) minutes', f'Exam core: {wc} words, about {round(wc/22)} minutes', s, 1)
    if wc<lo or wc>hi:
        s = s.replace('\n<!--LOC:', f"\n**FAILURE DISCLOSURE:** exam core is {wc} words, {'below' if wc<lo else 'above'} the Section 7 range of {lo}-{hi} for {mk} marks.\n\n<!--LOC:",1)
    out = ['\n## SOURCE LIST', '\n**[SRC] locators** (chapter file, PDF page marker; printed page where the offset is confirmed; verbatim phrase):']
    for k in dict.fromkeys(keys):
        f,ph = L[k]; path,off,cite = F[f]; lab = page_label(k); assert lab, k
        out.append(f"- {cite}, {os.path.basename(path)[:58]}, {lab}: \"{ph}\"")
    out.append('\n**[LIT]** none: no live literature search was run for this answer.')
    out.append('\n## REFERENCES (alphabetical)')
    for r in sorted(set(BOOK[k] for k in refs)): out.append('- '+r)
    open(p,'w',encoding='utf8').write(s.rstrip()+'\n'+'\n'.join(out)+'\n')
    print(p, mk+'m exam words', wc, 'range', lo, hi)
if __name__=='__main__':
    for p in sys.argv[1:]: run(p)
