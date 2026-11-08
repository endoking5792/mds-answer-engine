import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Craig2002_20': "Craig RG, Powers JM, editors. Restorative Dental Materials. 11th ed. St Louis: Mosby; 2002. Ch.20 Cements.",
 'Craig2002_5_20': "Craig RG, Powers JM, editors. Restorative Dental Materials. 11th ed. St Louis: Mosby; 2002. Ch.5 Biocompatibility of dental materials; Ch.20 Cements.",
 'Sakaguchi2019_13': "Sakaguchi R, Ferracane J, Powers J, editors. Craig's Restorative Dental Materials. 14th ed. St Louis: Elsevier; 2019. Ch.13 Materials for adhesion and luting (chapter authors not printed in the extracted file).",
 'Sakaguchi2019_8': "Sakaguchi R, Ferracane J, Powers J, editors. Craig's Restorative Dental Materials. 14th ed. St Louis: Elsevier; 2019. Ch.8 Preventive and intermediary materials (chapter authors not printed in the extracted file).",
 'Anusavice2013': "Anusavice KJ, Shen C, Rawls HR, editors. Phillips' Science of Dental Materials. 12th ed. St Louis: Elsevier Saunders (publication year not printed in the file). Ch.14 Dental cements.",
 'McCabe2008': "McCabe JF, Walls AWG. Applied Dental Materials. 9th ed. Oxford: Blackwell Publishing; 2008. Ch.29 Cements based on organometallic chelate compounds.",
 'Powers2013': "Powers JM, Wataha JC. Dental Materials: Properties and Manipulation. 10th ed. St Louis: Elsevier Mosby; 2013. Ch.7 (cements, temporary fillings, bases and liners; chapter title not legible in the extracted file).",
 'Bonsor2013': "Bonsor SJ, Pearson GJ. A Clinical Guide to Applied Dental Materials. Edinburgh: Elsevier Churchill Livingstone; 2013. Ch.12 Other dental cements; Ch.14 Materials used in temporization.",
 'Sikri_ind': "Sikri VK. Indirect Restorations in Dental Practice. 2nd ed. New Delhi: CBS Publishers; 2017 (first eBook edition date; print year not shown in the file). Ch.11 Interim restorations (cited by PDF page).",
 'Marzouk': "Marzouk MA, Simonton AL, Gross RD. Operative Dentistry: Modern Theory and Practice. St Louis: Ishiyaku EuroAmerica (publication year not printed). Ch.1 Principles of operative dentistry (cited by PDF page).",
 'Flake2021': "Flake NM, Johnson JD. Obturation and temporization. In: Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. St Louis: Elsevier; 2021. Ch.15. (Editors, edition and year as used elsewhere in this repo.)",
 'Baba2017': "Baba NZ, White SN, Bogen G. Restoration of endodontically treated teeth. In: Chugal N, Lin LM, editors. Endodontic Prognosis: Clinical Guide for Optimal Treatment Outcome. Cham: Springer; 2017. Ch.10.",
 'Johnson2021': "Johnson BR, Fayad MI, Berman LH. Periradicular surgery. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.11.",
 'Fouad2021': "Fouad AF, Levin LG. Pulp reactions to caries and dental procedures. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.14.",
 'Bogen2021': "Bogen G, Dammaschke T, Chandler N. Vital pulp therapy. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.24.",
 'Dammaschke2024': "Dammaschke T. Vital pulp treatment modalities: direct pulp capping. In: Duncan HF, El-Karim IA, editors. Vital Pulp Treatment. 1st ed. Chichester: John Wiley & Sons; 2024. Ch.5.",
 'Parirokh2017': "Parirokh M, Shabahang S. Root-end filling materials. In: Torabinejad M, Rubinstein R, editors. The Art and Science of Contemporary Surgical Endodontics. Hanover Park, IL: Quintessence; 2017 (copyright year from the file's front matter; earlier topics cited this book as 2019). Ch.11.",
 'Gopikrishna2021': "Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. New Delhi: Wolters Kluwer; 2021. Ch.22 Endodontic surgery (no individual chapter author is named in the file, so the editor is cited).",
 'Castellucci2003': "Castellucci A. Advances in surgical endodontics. L'Informatore Endodontico 2003;6(1) (short article, PDF pp.1-16 of the file; authorship read from the file).",
}
LIT = {}
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
