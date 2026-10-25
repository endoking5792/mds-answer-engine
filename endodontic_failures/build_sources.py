import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Roda2021': "Roda RS, Gettleman BH, Johnson SC. Nonsurgical retreatment. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.10.",
 'Ng2021': "Ng YL, Gulabivala K. Evaluation of outcomes. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.17.",
 'Machtou2019': "Machtou P, Ruddle CJ. Endodontic orthograde retreatment and management of mishaps. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. PMPH USA; 2019. Ch.23. (Chapter authors as used elsewhere in this repo; verify against the printed book.)",
 'Gulabivala2019': "Gulabivala K, Ng YL. Outcomes of endodontic therapy. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. PMPH USA; 2019. Ch.33.",
 'Goldberg2019': "Goldberg F. Achieving long-term success with endodontic therapy. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. PMPH USA; 2019. Ch.34. (Author name decoded from a garbled chapter heading; verify against the printed book.)",
 'Baba2019': "Baba NZ, Goodacre CJ. Contemporary restoration of endodontically treated teeth. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. PMPH USA; 2019. Ch.35. (Author names decoded from a garbled chapter heading; verify against the printed book.)",
 'Rocas2022': "Rôças IN, Ricucci D, Siqueira JF Jr. Causes of endodontic treatment failure. In: Siqueira JF Jr, Rôças IN, editors. Treatment of Endodontic Infections. 2nd ed. Berlin: Quintessence; 2022. Ch.7.",
 'Hulsmann2022': "Hülsmann M, Schäfer E, Bürklein S. Management of posttreatment apical periodontitis: nonsurgical retreatment and periradicular surgery. In: Siqueira JF Jr, Rôças IN, editors. Treatment of Endodontic Infections. 2nd ed. Berlin: Quintessence; 2022. Ch.17.",
 'Malek2017': "Malek M, Lin LM. Local, systemic, and genetic considerations of endodontic treatment prognosis. In: Chugal N, Lin LM, editors. Endodontic Prognosis: Clinical Guide for Optimal Treatment Outcome. Cham: Springer; 2017. Ch.11.",
 'Chugal2017': "Chugal N, Mallya SM, Kahler B, Lin LM. Criteria for outcome assessment of nonsurgical endodontic treatment. In: Chugal N, Lin LM, editors. Endodontic Prognosis: Clinical Guide for Optimal Treatment Outcome. Cham: Springer; 2017. Ch.12.",
 'White2017': "White SN, Torabinejad M. From tooth retention through root canal treatment to extraction and replacement. In: Chugal N, Lin LM, editors. Endodontic Prognosis: Clinical Guide for Optimal Treatment Outcome. Cham: Springer; 2017. Ch.13.",
 'Sikri2017': "Sikri VK. Essentials of Endodontics. 2nd ed. New Delhi: CBS Publishers & Distributors; 2017 (second eBook edition 2019). Ch.36 Endodontic failures and retreatment.",
 'Ng2014': "Ng YL, Gulabivala K. Management of non-surgical root-canal treatment failure. In: Gulabivala K, Ng YL. Endodontics. 4th ed. Edinburgh: Mosby Elsevier; 2014. Ch.9.",
 'Gutmann2011': "Gutmann JL, Lovdahl PE. Problem Solving in Endodontics: Prevention, Identification and Management. 5th ed. St Louis: Mosby Elsevier; 2011. Ch.5 Problem solving in the diagnosis of treatment failure (chapter author not separately named in the file).",

 'Setzer2021': "Setzer F, Chogle S, Torabinejad M. Endodontic treatment outcomes. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.22. (Edition and year as used elsewhere in this repo; verify against the printed book.)",
 'Gulabivala2022': "Gulabivala K, Ng YL. Outcomes of endodontic therapy. In: Siqueira JF Jr, Rôças IN, editors. Treatment of Endodontic Infections. 2nd ed. Berlin: Quintessence; 2022. Ch.20.",
 'Weine2004': "Weine FS. Endodontic Therapy. 6th ed. St Louis: Mosby; 2004. Ch.1 Basis for successful endodontics.",
 'Baba2017': "Baba NZ, White SN, Bogen G. Restoration of endodontically treated teeth. In: Chugal N, Lin LM, editors. Endodontic Prognosis: Clinical Guide for Optimal Treatment Outcome. Cham: Springer; 2017. Ch.10.",
 'Walton2002': "Walton RE, Torabinejad M. Principles and Practice of Endodontics. 3rd ed. Philadelphia: WB Saunders; 2002. Part 21 Preventive endodontics: protecting the pulp. (Chapter author not separately named in the extraction.)",
 'Siqueira2022': "Siqueira JF Jr, Rôças IN. Causes of persistent posttreatment pain in endodontics. In: Siqueira JF Jr, Rôças IN, editors. Treatment of Endodontic Infections. 2nd ed. Berlin: Quintessence; 2022. Ch.8.",
 'Terauchi2021': "Terauchi Y, Parirokh M, Handysides R. Nonsurgical retreatment. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.19. (Edition and year as used elsewhere in this repo; verify against the printed book.)",
 'Gopikrishna2021': "Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. Wolters Kluwer; 2021. Ch.21 Nonsurgical endodontic retreatment (chapter author not named in the extraction).",
 'Pontius2010': "Pontius O. Endodontic retreatment procedures. In: Baumann MA, Beer R, editors. Endodontology. 2nd ed (English translation of the 2nd German edition, 2008). Stuttgart: Thieme; 2010. Ch.39. (Chapter author read from the book's contents list; verify against the printed book.)",
 'Gulabivala2014': "Gulabivala K, Ng YL. Endodontics. 4th ed. Edinburgh: Mosby Elsevier; 2014. Ch.3 Biological and clinical rationale for root-canal treatment; Ch.5 Treatment planning (chapter authors as printed in the book's chapter headings; the chapter files used are named in the SOURCE LIST).",
 'Cunha2015': "Cunha RS, Bueno CES. Disinfection in nonsurgical retreatment cases. In: Basrani B, editor. Endodontic Irrigation: Chemical Disinfection of the Root Canal System. Cham: Springer; 2015. Ch.17.",
 'Berutti2025': "Berutti E, Castellucci A. Nonsurgical root canal retreatment. In: Peters OA, editor. The Guidebook to Molar Endodontics. Cham: Springer; 2025. Ch.11.",
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
