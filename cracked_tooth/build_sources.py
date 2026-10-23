import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Berman2021': "Berman LH, Tamse A. Chronic cracks and fractures. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.22.",
 'Bakland2019': "Bakland LK. Crown-originating dental fractures. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.13 (author name decoded from a garbled line in the extracted file; verify against the printed book).",
 'Krishnan2025': "Krishnan U, Swain M. Assessing and managing cracked molars. In: Peters OA, editor. The Guidebook to Molar Endodontics. Cham: Springer; 2025. Ch.9. doi:10.1007/978-3-032-07352-5_9.",
 'Walton2002': "Walton RE, Torabinejad M, editors. Principles and Practice of Endodontics. 3rd ed. Philadelphia: WB Saunders; 2002. Ch.28 Longitudinal tooth fractures (chapter author not shown in the extracted file).",
 'Bresciani2020': "Bresciani E, et al. Dentin hypersensitivity and cracked teeth. In: Torres CRG, editor. Modern Operative Dentistry: Principles for Clinical Practice. Cham: Springer; 2020. Ch.18 (co-authors not listed in the extracted page header).",
 'Tamse2019': "Tamse A, Berman LH. Vertical root fractures. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.14 (author names decoded from a garbled line in the extracted file; verify against the printed book).",
 'Andreasen2007r': "Andreasen FM, Andreasen JO, Cvek M. Root fractures. In: Andreasen JO, Andreasen FM, Andersson L, editors. Textbook and Color Atlas of Traumatic Injuries to the Teeth. 4th ed. Oxford: Blackwell Munksgaard; 2007. Ch.12.",
 'Andreasen2007c': "Andreasen JO, Andreasen FM, Tsukiboshi M. Crown-root fractures. In: Andreasen JO, Andreasen FM, Andersson L, editors. Textbook and Color Atlas of Traumatic Injuries to the Teeth. 4th ed. Oxford: Blackwell Munksgaard; 2007. Ch.11.",
 'Bourguignon2020': "Bourguignon C, Cohenca N, Lauridsen E, et al. International Association of Dental Traumatology guidelines for the management of traumatic dental injuries: 1. Fractures and luxations. Dent Traumatol. 2020;36:314-330. doi:10.1111/edt.12578.",
 'Sikri': "Sikri VK. Essentials of Endodontics. 2nd ed. Ch.26 Traumatic injuries and management (publisher and year not verified from the file; cited by PDF page).",
 'Gopikrishna2021': "Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. Wolters Kluwer; 2021. Ch.6 Clinical diagnostic methods (cited by PDF page).",
 'Sturdevant': "Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed. Elsevier (editors and year not verified from the extracted file). Ch.3, Ch.11 and Ch.14 Complex amalgam restorations.",
 'AAE2012': "American Association of Endodontists. Glossary of Endodontic Terms. 8th ed. Chicago: AAE; 2012.",
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
