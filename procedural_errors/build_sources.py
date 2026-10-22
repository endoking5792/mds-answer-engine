import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Gopikrishna2021': "Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. Wolters Kluwer; 2021. Ch.17 Procedural errors: prevention and management.",
 'Walton2002': "Walton RE, Torabinejad M, editors. Principles and Practice of Endodontics. 3rd ed. Philadelphia: WB Saunders; 2002. Ch.18 Procedural accidents (chapter author not shown in the extracted file; the file ends at 'Apical perforations').",
 'Hulsmann2017': "Hülsmann M, Chong BS. Problems in endodontic treatment. In: Chong BS, editor. Harty's Endodontics in Clinical Practice. 7th ed. Elsevier; 2017 (year not verified from the file). Ch.14.",
 'Roda2021': "Roda RS, Gettleman BH, Johnson SC. Nonsurgical retreatment. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.10.",
 'Machtou2019': "Machtou P, Ruddle CJ. Endodontic orthograde retreatment and management of mishaps. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.23 (chapter authors decoded from a garbled author line in the extracted file; verify against the printed book).",
 'Attar2025': "Attar OH, Chogle SM, Hsu T-Y. Instrumentation-related complications. In: Jain PR, editor. Common Complications in Endodontics. Cham: Springer; 2025. Ch.5. doi:10.1007/978-3-031-83394-6_5.",
 'Plotino2025': "Plotino G, Venturi M, Grande NM. Complications due to root canal filling procedures. In: Jain PR, editor. Common Complications in Endodontics. Cham: Springer; 2025. Ch.6. doi:10.1007/978-3-031-83394-6_6.",
 'AAE2012': "American Association of Endodontists. Glossary of Endodontic Terms. 8th ed. Chicago: AAE; 2012.",
 'Baumann2010': "Baumann MA, Beer R, editors. Endodontology (Color Atlas of Dental Medicine). 2nd ed. Stuttgart: Thieme; 2010. Ch.43 Perforations (chapter author not shown in the extracted file).",
 'Hulsmann2009': "Hülsmann M, Schäfer E, editors. Problems in Endodontics: Etiology, Diagnosis and Treatment. London: Quintessence; 2009. Ch.17 Perforations (chapter author not legible in the OCR extraction; cited by PDF page).",
 'Nosrat2021': "Nosrat A, Terauchi Y, Torabinejad M. Procedural accidents. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.18 (editor names not verified from the file).",
 'Atav2024': "Atav A, Arıcan B, Olcay K. Bioceramics in clinical endodontics. In: Chopra V, editor. Bioceramics in Endodontics. Hoboken: Wiley; 2024. Ch.3.",
 'Terauchi2021': "Terauchi Y, Renton TF. Managing iatrogenic events. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.20.",
 'Berutti2025': "Berutti E, Castellucci A. Nonsurgical root canal retreatment. In: The Guidebook to Molar Endodontics. 2nd ed. Cham: Springer; 2025. Ch.11 (editor and edition not verified from the file).",
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
