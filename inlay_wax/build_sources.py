import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Anusavice2013': "Anusavice KJ, Shen C, Rawls HR, editors. Phillips' Science of Dental Materials. 12th ed. St Louis: Elsevier Saunders; 2013. Ch.10 Dental waxes, casting investments, and casting procedures.",
 'Bhat2019': 'Bhat VS, Nandish BT, Jayaprakash K. Science of Dental Materials with Clinical Applications. 3rd ed. New Delhi: CBS Publishers; 2019. Ch.14 Dental waxes.',
 'Bonsor2013': 'Bonsor SJ, Pearson GJ. A Clinical Guide to Applied Dental Materials. Edinburgh: Elsevier Churchill Livingstone; 2013. Ch.16 Waxes.',
 'Chadwick2011': 'Chadwick G, Radford J, Ricketts D. Gold restorations: the metals, the manufacture and the fit. In: Ricketts D, Bartlett D, editors. Advanced Operative Dentistry: A Practical Approach. Edinburgh: Churchill Livingstone Elsevier; 2011. Ch.9.',
 'Chandhak2020': 'Chandhak MG. Casting procedure and casting defects. In: Singh H, editor. Essentials of Preclinical Conservative Dentistry. 2nd ed. Gurgaon: Wolters Kluwer Health (India); 2020. Ch.20.',
 'Craig2002': 'Craig RG, Powers JM, editors. Restorative Dental Materials. 11th ed. St Louis: Mosby; 2002. Ch.14 Waxes; Ch.17 Casting and soldering procedures.',
 'Garg2011': 'Garg N, Garg A. Textbook of Preclinical Conservative Dentistry. 1st ed. New Delhi: Jaypee Brothers Medical Publishers; 2011. Ch.12 Cast metal restorations.',
 'Kim2018': 'Kim SB, Kim NH, Kim JH, Moon HS. Evaluation of the fit of metal copings fabricated using stereolithography. J Prosthet Dent. 2018;120(5):693-698. doi:10.1016/j.prosdent.2018.01.012 (abstract only).',
 'Lalande2018': 'Lalande D, Hodd JA, Brousseau JS, Ramos V, Dunham D, Rueggeberg F. Marginal discrepancy dimensions of single unit metal crowns fabricated by using CAD-CAM-milled acrylate resin polymer blocks or a conventional waxing technique. J Prosthet Dent. 2018;119(6):948-953. doi:10.1016/j.prosdent.2017.07.019 (abstract only).',
 'Marzouk_nd': 'Marzouk MA, Simonton AL, Gross RD. Operative Dentistry: Modern Theory and Practice. St Louis: Ishiyaku EuroAmerica; New Delhi: Indian edition (publication year not printed in the extracted front matter). Ch.22 Working die and model construction; Ch.24 Casting fabrication.',
 'McCabe2008': 'McCabe JF, Walls AWG. Applied Dental Materials. 9th ed. Oxford: Blackwell Publishing; 2008. Ch.4 Waxes.',
 'Pekkan2025': 'Pekkan G, Gulgezen Aydin H, Tuna SH, Hekimoglu C. Overall fit of anterior and posterior single crown substructures fabricated with different additive manufacturing and conventional techniques. Odontology. 2025;114(3):1196-1206. doi:10.1007/s10266-025-01178-2 (abstract only).',
 'Powers2013': 'Powers JM, Wataha JC. Dental Materials: Properties and Manipulation. 10th ed. St Louis: Elsevier Mosby; 2013. Ch.9 Gypsum and investment materials; Ch.10 Waxes.',
 'Ritter2019': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed (adaptation of 7th ed). Elsevier; 2019. Ch.23 Class II cast metal restorations.",
 'Sakaguchi2019': "Sakaguchi R, Ferracane J, Powers J, editors. Craig's Restorative Dental Materials. 14th ed. St Louis: Elsevier; 2019. Ch.4 (Table 4.13, thermal expansion).",
 'Sikri_ind': 'Sikri VK. Indirect Restorations in Dental Practice. 2nd ed. New Delhi: CBS Publishers (year not verified from the extracted file). Glossary; cast restoration chapter.',
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
