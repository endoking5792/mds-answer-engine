import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Bartlett2011': "Bartlett D. Tooth wear. In: Ricketts D, Bartlett D, editors. Advanced Operative Dentistry: A Practical Approach. Edinburgh: Elsevier; 2011. Ch.4.",
 'BartlettRicketts2011': "Bartlett D, Ricketts D. Complex multiple fixed and combined fixed and removable prosthodontics. In: Ricketts D, Bartlett D, editors. Advanced Operative Dentistry: A Practical Approach. Edinburgh: Elsevier; 2011. Ch.16.",
 'Goldstein2018': "Goldstein RE, Curtis JW Jr, Farley BA, Siranli S, Clark WA. Abfraction, abrasion, attrition, and erosion. In: Goldstein RE, Chu SJ, Lee EA, Stappert CFJ, editors. Ronald E. Goldstein's Esthetics in Dentistry. 3rd ed. Hoboken: John Wiley & Sons; 2018. Ch.22.",
 'Singh2020': "Singh H. Essentials of Preclinical Conservative Dentistry. 2nd ed. Gurgaon: Wolters Kluwer Health (India); 2020. Ch.21 Non-carious lesions of the tooth surface (joint contribution with V Gade).",
 'Marzouk': "Marzouk MA, Simonton AL, Gross RD. Operative Dentistry: Modern Theory and Practice. St Louis: Ishiyaku EuroAmerica (publication year not printed). Ch.27 Non-carious destruction and disfigurement of teeth.",
 'Ritter2019': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed. Elsevier; 2019. Ch.20 Non-carious lesions and their management (chapter authors not printed in the file).",
 'Kaidonis2016': "Kaidonis J, Richards LC, Townsend GC, Heithersay GS. Non-carious tooth structure loss: diagnosis, risk and activity assessment and clinical management. In: Mount GJ, Hume WR, Ngo HC, Wolff MS, editors. Preservation and Restoration of Tooth Structure. 3rd ed. Wiley; 2016. Ch.4.",
 'Alani2025': "Alani A, Patel M. Adhesive Techniques in Restorative Dentistry. BDJ Clinician's Guides. Cham: Springer Nature Switzerland; 2025. Ch.7 Treating anterior tooth surface loss.",
 'Ibbetson2001': "Ibbetson R. Indirect restorations for anterior teeth: space, the eternal problem. In: Roulet JF, Wilson NHF, Fuzzi M, editors. Advances in Operative Dentistry. Vol 1: Contemporary Clinical Practice. Chicago: Quintessence; 2001. Ch.9.",
 'Banerjee2015': "Banerjee A, Watson TF. Pickard's Guide to Minimally Invasive Operative Dentistry. 10th ed. Oxford: Oxford University Press; 2015. Ch.1 (section 1.3 Tooth wear).",
 'Torres2020': "Torres CRG, Barbe AG, Noack MJ, Wicht MJ. Diagnosis and treatment planning. In: Torres CRG, editor. Modern Operative Dentistry: Principles for Clinical Practice. Cham: Springer Nature Switzerland; 2020. Ch.1.",
 'Kaidonis2016ch1': "Kaidonis J, Townsend GC, McIntyre J, Richards LC, Hume WR. The oral environment and the main causes of tooth structure loss. In: Mount GJ, Hume WR, Ngo HC, Wolff MS, editors. Preservation and Restoration of Tooth Structure. 3rd ed. Chichester: John Wiley & Sons; 2016. Ch.1. (Cited in text as Kaidonis et al, 2016, Ch.1.)",
 'Fontana2010': "Fontana M, Young DA, Wolff MS, Pitts NB, Longbottom C. Defining dental caries for 2010 and beyond. Dent Clin North Am. 2010;54:423-440. https://doi.org/10.1016/j.cden.2010.03.007 (DCNA, read in full).",
 'WangLussi2010': "Wang X, Lussi A. Assessment and management of dental erosion. Dent Clin North Am. 2010;54:565-578. https://doi.org/10.1016/j.cden.2010.03.003 (DCNA, read in full).",
}
LIT = {
 'Gulamali2011': "Gulamali AB, Hemmings KW, Tredwin CJ, Petrie A. Survival analysis of composite Dahl restorations provided to manage localised anterior tooth wear (ten year follow-up). Br Dent J. 2011;211(4):E9. https://doi.org/10.1038/sj.bdj.2011.683 (PubMed abstract read).",
 'Loomans2017': "Loomans B, Opdam N, Attin T, Bartlett D, Edelhoff D, Frankenberger R, et al. Severe tooth wear: European consensus statement on management guidelines. J Adhes Dent. 2017;19(2):111-119. https://doi.org/10.3290/j.jad.a38102 (PubMed abstract read).",
 'Alani2025SR': "Alani A, Mehta S, Koning I, Loomans B, Pereira-Cenci T. Restorative options for moderate and severe tooth wear: a systematic review. J Dent. 2025;156:105711. https://doi.org/10.1016/j.jdent.2025.105711 (PubMed abstract read).",
 'Johansson2008': "Johansson A, Johansson AK, Omar R, Carlsson GE. Rehabilitation of the worn dentition. J Oral Rehabil. 2008;35(7):548-566. https://doi.org/10.1111/j.1365-2842.2008.01897.x (PubMed abstract read).",
 'DelaTorreCanales2017': "De la Torre Canales G, Camara-Souza MB, do Amaral CF, Garcia RCMR, Manfredini D. Is there enough evidence to use botulinum toxin injections for bruxism management? A systematic literature review. Clin Oral Investig. 2017;21(3):727-734. https://doi.org/10.1007/s00784-017-2092-4 (PubMed abstract read).",
 'LohbauerReich2017': "Lohbauer U, Reich S. Antagonist wear of monolithic zirconia crowns after 2 years. Clin Oral Investig. 2017;21(4):1165-1172. https://doi.org/10.1007/s00784-016-1872-6 (PubMed abstract read).",
}
RANGE = {'15':(510,600),'100':(3200,3500),'75':(2550,3000),'50':(1700,2000),'25':(850,1000),'20':(680,800),'10':(320,400),'7':(320,400),'5':(160,200)}
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
