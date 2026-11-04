import re, os, sys
from locators import L, F, page_label
BOOK = {
 'Summitt2013': "Summitt JB. Field isolation. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Hanover Park: Quintessence; 2013. Ch.8.",
 'Ritter2019': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed. Elsevier; 2019. Ch.8 Preliminary considerations for operative dentistry (chapter author not printed in the file).",
 'Marzouk': "Marzouk MA, Simonton AL, Gross RD. Operative Dentistry: Modern Theory and Practice. St Louis: Ishiyaku EuroAmerica (publication year not printed). Ch.3 Control of the field of operation.",
 'Banerjee2011': "Banerjee A, Watson TF. Pickard's Manual of Operative Dentistry. 9th ed. Oxford: Oxford University Press; 2011. Ch.5, section 5.6 Moisture control.",
 'Kunzelmann2001': "Kunzelmann KH. Moisture management with rubber dam in operative dentistry. In: Roulet JF, Wilson NHF, Fuzzi M, editors. Advances in Operative Dentistry, Volume 1: Contemporary Clinical Practice. Chicago: Quintessence; 2001. Ch.3.",
 'Borges2020': "Borges AB, Torres CRG, Benetti AR, Bakhshandeh A. Isolation of the operating field. In: Torres CRG, editor. Modern Operative Dentistry: Principles for Clinical Practice. Cham: Springer Nature Switzerland; 2020. Ch.7.",
}
LIT = {
 'Wang2016': "Wang Y, Li C, Yuan H, Wong MC, Zou J, Shi Z, Zhou X. Rubber dam isolation for restorative treatment in dental patients. Cochrane Database Syst Rev. 2016;9:CD009858. https://doi.org/10.1002/14651858.CD009858.pub2 (PubMed abstract read).",
 'Miao2021': "Miao C, Yang X, Wong MC, Zou J, Zhou X, Li C, Wang Y. Rubber dam isolation for restorative treatment in dental patients. Cochrane Database Syst Rev. 2021;5:CD009858. https://doi.org/10.1002/14651858.CD009858.pub3 (PubMed abstract read).",
 'Siddalingappa2025': "Siddalingappa D, Reddy V, Nayak AS, Urala AS, Pentapati KC. Efficiency and patient-reported outcomes for Isolite system: a systematic review of randomized controlled trials. Int J Clin Pediatr Dent. 2025;18(3):331-338. https://doi.org/10.5005/jp-journals-10005-3081 (PubMed abstract read).",
 'Mattar2022': "Mattar RE, Sulimany AM, Binsaleh SS, Hamdan HM, Al-Majed IM. Evaluation of fissure sealant retention rates using Isolite in comparison with rubber dam and cotton roll isolation techniques: a randomized clinical trial. Int J Paediatr Dent. 2023;33(1):12-19. https://doi.org/10.1111/ipd.13008 (PubMed abstract read).",
 'Mattar2021': "Mattar RE, Sulimany AM, Binsaleh SS, Al-Majed IM. Comparison of fissure sealant chair time and patients' preference using three different isolation techniques. Children (Basel). 2021;8(6):444. https://doi.org/10.3390/children8060444 (PubMed abstract read).",
 'Bagher2024': "Bagher SM, Bhadila GY, Alqahtani NH, Alharbi NH, Felemban OM. The use of DryShield versus rubber dam isolation systems among pediatric patients with different airway patency: a randomized clinical trial. Saudi Dent J. 2024;36(6):873-879. https://doi.org/10.1016/j.sdentj.2024.03.013 (PubMed abstract read).",
 'BaHammam2025': "BaHammam F, Alsuhaibani M, Almutairi F, Aldakhil S, Albarrak S, Alreshaid L, Farook F. Efficacy and feasibility of OptraDamPlus versus conventional rubber dams in preclinical simulation training: a randomized crossover trial. Dent J (Basel). 2025;13(11):485. https://doi.org/10.3390/dj13110485 (PubMed abstract read).",
 'Naik2026': "Naik SS, Sharma R, Shetty D, Chavan S, Gorule M, Shah R, Sachdev SS. Patient comfort and acceptance of different isolation techniques for silver diamine fluoride application: a randomized clinical trial. Int J Clin Pediatr Dent. 2026;19(7):857-862. https://doi.org/10.5005/jp-journals-10005-3548 (PubMed abstract read).",
 'Kumbargere2020': "Kumbargere Nagraj S, Eachempati P, Paisi M, Nasser M, Sivaramakrishnan G, Verbeek JH. Interventions to reduce contaminated aerosols produced during dental procedures for preventing infectious diseases. Cochrane Database Syst Rev. 2020;10:CD013686. https://doi.org/10.1002/14651858.CD013686.pub2 (PubMed abstract read).",
}
RANGE = {'100':(3200,3500),'75':(2550,3000),'50':(1700,2000),'25':(850,1000),'20':(680,800),'10':(320,400),'7':(320,400),'5':(160,200)}
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
