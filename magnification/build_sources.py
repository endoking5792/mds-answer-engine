import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Sikri2019': "Sikri VK. Magnification in endodontics. In: Essentials of Endodontics. 2nd ed. New Delhi: CBS Publishers; 2019. Ch.30.",
 'Gopikrishna2021': "Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. Wolters Kluwer; 2021. Ch.9 Magnification in endodontics (no individual chapter author is named in the file, so the editor is cited).",
 'Baumann2010': "Baumann MA, Beer R, editors. Endodontology. 2nd ed. Stuttgart: Thieme; 2010. Ch.18 The dental microscope in endodontics (chapter author not stated in the extracted file; cited under the editors).",
 'Lins2016': "Lins CCSA, Alves DF, de Resende AB. Visualization in endodontics. In: Jain P, editor. Current Therapy in Endodontics. 1st ed. Ames: John Wiley & Sons; 2016. Ch.8, pp.192-201.",
 'Rubinstein2017': "Rubinstein R. Magnification and illumination in apical surgery. In: Torabinejad M, Rubinstein R, editors. The Art and Science of Contemporary Surgical Endodontics. Hanover Park, IL: Quintessence; 2017 (copyright year from the file's front matter; earlier topics cited this book as 2019). Ch.7.",
 'Ritter2019': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed (adaptation of 7th ed). Elsevier; 2019. Ch.3, Magnification in operative dentistry.",
 'Hilton2013': "Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Chicago: Quintessence; 2013.",
 'Bharti2020': "Bharti R, Bhasin P. Magnification in restorative dentistry. In: Singh H. Essentials of Preclinical Conservative Dentistry. 2nd ed. Gurgaon: Wolters Kluwer Health (India); 2020. Ch.8.",
 'Lam2012': "Lam EWN. Intraoral digital imaging (Ch.4) and Introduction to cone beam computed tomography (Ch.20). In: Basrani B, editor. Endodontic Radiology. 2nd ed. Wiley-Blackwell; 2012.",
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
