import re, glob, os, sys
from locators import L, F, page_label
BOOK = {
 'Glickman2021': "Glickman GN, Iacono VJ. Endo-perio. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.25.",
 'Rotstein2019': "Rotstein I, Zabalegui B, Al-Hezaimi K. Endodontic-periodontal interrelationships. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.36 (chapter authors decoded from a garbled author line in the extracted file; verify against the printed book).",
 'Gopikrishna2021': "Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. Wolters Kluwer; 2021. Ch.20 Endodontic-periodontic interrelationship.",
 'Rotstein2017': "Rotstein I. Marginal periodontitis and the dental pulp. In: Chong BS, editor. Harty's Endodontics in Clinical Practice. 7th ed. Elsevier; 2017 (year not verified from the file). Ch.13.",
 'Seltzer2012': "Seltzer and Bender's Dental Pulp. 2nd ed. Quintessence; 2012 (editors not verified from the file). Ch.16 Interrelationship of pulpal and periodontal diseases (the extracted file begins mid-chapter, so chapter authors are not named).",
 'Weine2004': "Weine FS. Endodontic-periodontal problems. In: Weine FS. Endodontic Therapy. 6th ed. St Louis: Mosby; 2004. Ch.11.",
 'Gulabivala2014': "Gulabivala K, Darbar UR, Ng Y-L. The perio-endo interface. In: Gulabivala K, Ng Y-L, editors. Endodontics. 4th ed. Edinburgh: Mosby Elsevier; 2014. Ch.12.",
 'Walton2002': "Walton RE, Torabinejad M, editors. Principles and Practice of Endodontics. 3rd ed. Philadelphia: WB Saunders; 2002. Ch.26 Periodontal-endodontic considerations (adapted from Harrington GW, Dent Clin North Am 1979;23:673-690, and Natkin E, 1989; chapter author not shown in the file).",
 'Herrera2018': "Herrera D, Retamal-Valdes B, Alonso B, Feres M. Acute periodontal lesions (periodontal abscesses and necrotizing periodontal diseases) and endo-periodontal lesions. J Clin Periodontol 2018;45(Suppl 20):S78-S94. doi:10.1111/jcpe.12941 (full text read, including Table 6).",
 'Papapanou2018': "Papapanou PN, Sanz M, Buduneli N, et al. Periodontitis: consensus report of workgroup 2 of the 2017 World Workshop on the Classification of Periodontal and Peri-Implant Diseases and Conditions. J Clin Periodontol 2018;45(Suppl 20):S162-S170. doi:10.1111/jcpe.12946 (PubMed abstract only).",
 'Kinaia2012': "Kinaia BM, Chogle SMA, Kinaia AM, Goodis HE. Regenerative therapy: a periodontal-endodontic perspective. Dent Clin North Am 2012;56(3):537-547 (full text read).",
 'Andreana2010': "Andreana S. Restorative options for the periodontal patient. Dent Clin North Am 2010;54(1):157-161 (full text read).",
}
RANGE = {'100':(3200,3500),'75':(2550,3000),'50':(1700,2000),'25':(850,1000),'20':(680,800),'10':(320,400),'7':(230,280),'5':(160,200)}
def run(files=None):
    for p in sorted(files or glob.glob('Q*.md')+glob.glob('P*.md')):
        s = open(p,encoding='utf8').read()
        s = s.split('\n## SOURCE LIST')[0]
        s = re.sub(r'\n\*\*FAILURE DISCLOSURE:.*\n','\n',s)
        keys = [k.strip() for k in re.search(r'<!--LOC: (.*?)-->',s,re.S).group(1).split(',') if k.strip()]
        refs = [k.strip() for k in re.search(r'<!--REF: (.*?)-->',s,re.S).group(1).split(',') if k.strip()]
        m = re.search(r'## EXAM MODE(.*?)(?=\n## HIGH-YIELD)',s,re.S); wc = len(m.group(1).split())
        mk = re.search(r'\*\*Marks:\*\* (\d+)m',s).group(1); lo,hi = RANGE[mk]
        if wc<lo or wc>hi:
            side = 'below' if wc<lo else 'above'
            s = s.replace('\n<!--LOC:', f"\n**FAILURE DISCLOSURE:** Exam Mode is {wc} words, {side} the Section 7 range of {lo}-{hi} for {mk} marks.\n\n<!--LOC:",1)
        out = ['\n## SOURCE LIST', '\n**[SRC] locators** (chapter file, PDF page marker; printed page where the offset is confirmed; verbatim phrase):']
        for k in dict.fromkeys(keys):
            f,ph = L[k]; path,off,cite = F[f]; lab = page_label(k); assert lab, k
            out.append(f"- {cite}, {os.path.basename(path)[:58]}, {lab}: \"{ph}\"")
        out.append('\n**[LIT]** items are listed in REFERENCES with DOI; the access level is stated for each.')
        out.append('\n## REFERENCES (alphabetical)')
        for r in sorted(set(BOOK[k] for k in refs)): out.append('- '+r)
        s = s.rstrip()+'\n'+'\n'.join(out)+'\n'
        open(p,'w',encoding='utf8').write(s)
        print(p[:62].ljust(64), mk+'m', 'exam words', wc, 'range', lo, hi)
if __name__=='__main__':
    run(sys.argv[1:] or None)
