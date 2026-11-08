import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Sikri2019': "Sikri VK. Endodontic instruments (Ch.11). In: Essentials of Endodontics. 2nd ed. New Delhi: CBS Publishers; 2019.",
 'Baumann2010': "Baumann MA, Beer R, editors. Endodontology. 2nd ed. Stuttgart: Thieme; 2010. Chapters 9, 10, 12, 15, 20, 21, 22 and 23 (chapter authors not stated in the extracted files; cited under the editors).",
 'Peters2021': "Peters OA, Peters CI, Basrani B. Cleaning and shaping of the root canal system. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.8.",
 'Roda2021': "Roda RS, Gettleman BH, Johnson SC. Nonsurgical retreatment. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.10.",
 'Terauchi2021': "Terauchi Y, Renton TF. Managing iatrogenic events. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.20.",
 'Nusstein2015': "Nusstein JM. Sonic and ultrasonic irrigation. In: Basrani B, editor. Endodontic Irrigation: Chemical Disinfection of the Root Canal System. Cham: Springer; 2015. Ch.10.",
 'Jain2016': "Jain P, editor. Current Therapy in Endodontics. Chichester: Wiley-Blackwell; 2016. Ch.3 Rotary instruments (chapter authors not stated in the extracted file; cited under the editor).",
 'Tango2017': "Yilmaz and Ozyurek. Cyclic fatigue life of Tango-Endo, WaveOne GOLD, and Reciproc NiTi instruments. Restor Dent Endod. 2017. [Seen only as a web-search summary; author names and details not verified; page not opened.] https://doaj.org/article/c16167f10d6c46309b1e85c50a8299c9",
 'TangoClin': "Tango-Endo instrumentation system (clinical article). Inside Dentistry. 2015. [Seen only as a web-search summary; author not verified; page not opened.] https://www.aegisdentalnetwork.com/id/2015/04/tango-endo-instrumentation-system",
 'Ingle7': "Ingle's Endodontics. 7th ed. Ch.20 Preparation of the coronal and radicular spaces, and Ch.23 Endodontic orthograde retreatment and management of mishaps (year and chapter authors not printed in the extracted file; page numbers not cited because the OCR is damaged).",
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
