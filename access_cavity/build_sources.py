import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Sikri2019': "Sikri VK. Access cavity preparation (Ch.14) and Endodontic failure and retreatment (Ch.36). In: Essentials of Endodontics. 2nd ed. New Delhi: CBS Publishers; 2019.",
 'Baumann2010': "Baumann MA, Beer R, editors. Endodontology. 2nd ed. Stuttgart: Thieme; 2010. Ch.17 Access cavity preparation (chapter author not stated in the extracted file; cited under the editors).",
 'Gutmann2021': "Gutmann JL, Fan B. Tooth morphology and pulpal access cavities. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.7.",
 'Gopikrishna2021': "Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. Wolters Kluwer; 2021. Ch.13 Anatomy of pulp cavity and its access opening (chapter author not stated in the extracted file; cited under the editor).",
 'Nair2021': "Nair MK, Levin MD, Nair UP. Radiographic interpretation. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.2 (section 3D-guided endodontics).",
 'Setzer2025': "Setzer FC, Walsch H. Molar access. In: Peters OA, editor. The Guidebook to Molar Endodontics. Cham: Springer Nature; 2025. Ch.6.",
 'Shabbir2021': "Shabbir J, Zehra T, Najmi N, Hasan A, Naz M, Piasecki L, Azim AA. Access cavity preparations: classification and literature review of traditional and minimally invasive endodontic access cavity designs. J Endod. 2021;47(8):1229-44. [Abstract seen only, as summarised in a web search result: https://researchconnect.buffalo.edu/en/publications/access-cavity-preparations-classification-and-literature-review-o/]",
 'Guided2025': "Guided Endodontics - Potential and Limitations (narrative review, 2025). PMC12747600. [Seen only as a web-search summary; the page itself could not be fetched. Authors and journal not verified.] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12747600/",
 'Umbrella2024': "Impact of Guided Endodontics on the Success of Endodontic Treatment: An Umbrella Review of Systematic Reviews and Meta-Analyses. PMC11459592. [Seen only as a web-search summary; the page itself could not be fetched. Authors and journal not verified.] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11459592/",
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
    lit = [k for k in refs if k in ('Shabbir2021','Guided2025','Umbrella2024')]
    out.append('\n**[LIT]** ' + ('; '.join(lit) + ' (abstract/summary level only, see REFERENCES).' if lit else 'none: no live literature search was run for this answer.'))
    out.append('\n## REFERENCES (alphabetical)')
    for r in sorted(set(BOOK[k] for k in refs)): out.append('- '+r)
    open(p,'w',encoding='utf8').write(s.rstrip()+'\n'+'\n'.join(out)+'\n')
    print(p, mk+'m exam words', wc, 'range', lo, hi)
if __name__=='__main__':
    for p in sys.argv[1:]: run(p)
