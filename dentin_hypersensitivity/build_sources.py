import re, os, sys
from locators import L, F, page_label
GIL = "In: Gillam DG, editor. Dentine Hypersensitivity: Advances in Diagnosis, Management, and Treatment. 2nd ed. Cham: Springer; 2024."
BOOK = {
 'Addy2024': "Addy M, Gillam DG. Introduction and overview: statement of the problem. "+GIL+" Ch.1.",
 'Taha2024': "Taha S, Gillam DG. The prevalence of dentine hypersensitivity. "+GIL+" Ch.2.",
 'Olley2024': "Olley R, Bartlett D. Aetiology and clinical features of dentine hypersensitivity on all tooth surfaces and including non-carious cervical lesions (NCCLs). "+GIL+" Ch.4.",
 'Markowitz2024a': "Markowitz K, Pashley D. The physiological basis of dentin hypersensitivity. "+GIL+" Ch.5.",
 'Markowitz2024b': "Markowitz K, Gillam DG. Treatments for tooth sensitivity: nerve inactivation and tubule occlusion. How do potassium and strontium salts treat sensitivity? "+GIL+" Ch.6.",
 'Mosquim2024': "Mosquim V, Wang L, Zabeu GS, Francisconi-dos-Rios LF, Gillam DG, Magalhaes AC. Treatment modalities and procedures. "+GIL+" Ch.7.",
 'Gillam2024': "Gillam DG, Ramseier CA. Advances in the management of the patient with dentine hypersensitivity: motivation and prevention. "+GIL+" Ch.8.",
 'Hill2024': "Hill R, Gillam DG. Future strategies for the development of desensitizing products. "+GIL+" Ch.9.",
 'Sikri2020': "Sikri VK. Dentin hypersensitivity. In: Textbook of Conservative and Restorative Dentistry. New Delhi: CBS Publishers; 2020 (eBook edition). Ch.29.",
 'Trushkowsky2011': "Trushkowsky RD, Oquendo A. Treatment of dentin hypersensitivity. Dent Clin North Am. 2011;55:599-608. doi:10.1016/j.cden.2011.02.013.",
 'AlSabbagh2009a': "Al-Sabbagh M, Brown A, Thomas MV. In-office treatment of dentinal hypersensitivity. Dent Clin North Am. 2009;53:47-60. doi:10.1016/j.cden.2008.11.003.",
 'AlSabbagh2009b': "Al-Sabbagh M, Harrison E, Thomas MV. Patient-applied treatment of dentinal hypersensitivity. Dent Clin North Am. 2009;53:61-70. doi:10.1016/j.cden.2008.11.004.",
 'Cronshaw2023': "Cronshaw M, Mylona V. Photobiomodulation therapy within clinical dentistry. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry: Current Concepts. 2nd ed. Cham: Springer; 2023. Ch.7 (chapter title shortened in the extracted file; cited by PDF page).",
 'Arapostathis2023': "Arapostathis K, Velonis D, Chala M. Laser-assisted pediatric dentistry. In: Coluzzi DJ, Parker SPA, editors. Lasers in Dentistry: Current Concepts. 2nd ed. Cham: Springer; 2023. Ch.11 (cited by PDF page).",
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
