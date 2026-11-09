import re, os, sys
from locators import L, F, page_label
BOOK = {
 'g3_Overton2013': "Overton JD, Hilton TJ, LittleStar ML, Starr CB. Class 5 restorations. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Chicago: Quintessence; 2013. Ch.15.",
 'g3_Matis2013': "Matis BA, González-Cabezas C, Cochran MA. Diagnosis and treatment of root caries. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Chicago: Quintessence; 2013. Ch.13.",
 'g3_Breschi2013': "Breschi L, Ferracane JL, Cadenaro M, Mazzoni A, Hilton TJ. Adhesion to enamel and dentin. In: Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Chicago: Quintessence; 2013. Ch.9.",
 'g3_Ritter2019': "Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asia ed (adaptation by V. Gopikrishna). New Delhi: RELX India (Elsevier); 2019. Ch.6 Dental biomaterials; Ch.15 Fundamental concepts of enamel and dentin adhesion; Ch.19 Clinical technique for direct composite resin and glass ionomer restorations.",
 'g3_Torres2020': "Torres CRG, Zanatta RF. Composite restoration on anterior teeth. In: Torres CRG, editor. Modern Operative Dentistry: Principles for Clinical Practice. Cham: Springer Nature; 2020. Ch.14.",
 'g3_Torres2020b': "Torres CRG, et al. Amalgam restorations (Ch.11, section 11.3.3 Restoration of Class V preparations). In: Torres CRG, editor. Modern Operative Dentistry: Principles for Clinical Practice. Cham: Springer Nature; 2020. Ch.11 (co-authors after the first not read from the chapter title page).",
 'g3_Mount2016': "Mount GJ, Ngo HC. Principles of cavity design for the restoration of advanced lesions. In: Mount GJ, Hume WR, Ngo HC, Wolff MS, editors. Preservation and Restoration of Tooth Structure. 3rd ed. Chichester: Wiley; 2016. Ch.7.",
 'g3_Goldstein2018': "Goldstein RE, Curtis JW Jr, Farley BA, Siranli S, Clark WA. Abfraction, abrasion, attrition, and erosion. In: Goldstein RE, Chu SJ, Lee EA, Stappert CFJ, editors. Ronald E. Goldstein's Esthetics in Dentistry. 3rd ed. Hoboken: Wiley; 2018. Ch.22.",
 'g3_Nakabayashi1998': "Nakabayashi N, Pashley DH. Hybridization of Dental Hard Tissues. Tokyo: Quintessence; 1998. Ch.IV Characterization of the hybrid layer.",
 'g3_BedranRusso2017': 'Bedran-Russo A, Leme-Kraus AA, Vidal CMP, Teixeira EC. An overview of dental adhesive systems and the dynamic tooth-adhesive interface. Dent Clin North Am. 2017;61:713-731. https://doi.org/10.1016/j.cden.2017.06.001 (full text read; issue number not printed on the first page).',
 'g3_Fronza2022': 'Fronza BM, Braga RR, Cadenaro M. Dental adhesives: surface modifications of dentin structure for stable bonding. Dent Clin North Am. 2022;66:503-515. https://doi.org/10.1016/j.cden.2022.05.002 (full text read; issue number not printed on the first page).',
 'g3_Puckett2007': 'Puckett AD, Fitchie JG, Kirk PC, Gamblin J. Direct composite restorative materials. Dent Clin North Am. 2007;51:659-675. https://doi.org/10.1016/j.cden.2007.04.003 (full text read; issue number not printed on the first page).',
 'g3_Pfeifer2017': 'Pfeifer CS. Polymer-based direct filling materials. Dent Clin North Am. 2017;61:733-750. https://doi.org/10.1016/j.cden.2017.06.002 (full text read; issue number not printed on the first page).',
}
LIT = {
 'g3_ChapleGil2026': "Chaple Gil AM, Pereda Vázquez L, Santiesteban Velázquez M, Menéndez JJ. Comparison of adhesive strategies with different etching approaches on the clinical performance of restorations in non-carious cervical lesions: a systematic review and network meta-analysis. J Funct Biomater. 2026;17(4):160. https://doi.org/10.3390/jfb17040160 (PubMed abstract read; PMID 42042267).",
 'g3_Ma2022': "Ma KS, Wang LT, Blatz MB. Efficacy of adhesive strategies for restorative dentistry: a systematic review and network meta-analysis of double-blind randomized controlled trials over 12 months of follow-up. J Prosthodont Res. 2023;67(1):35-44. https://doi.org/10.2186/jpr.JPR_D_21_00279 (PubMed abstract read; PMID 35691823).",
 'g3_Worthington2024': "Worthington HV, Lewis SR, Glenny AM, et al. Topical silver diamine fluoride (SDF) for preventing and managing dental caries in children and adults. Cochrane Database Syst Rev. 2024;11:CD012718. https://doi.org/10.1002/14651858.CD012718.pub2 (PubMed abstract read; PMID 39508296).",
 'g3_Castelo2021': "Castelo R, Attik N, Catirse ABCEB, Pradelle-Plasse N, Tirapelli C, Grosgogeat B. Is there a preferable management for root caries in middle-aged and older adults? A systematic review. Br Dent J. 2021. https://doi.org/10.1038/s41415-021-3003-2 (PubMed abstract read; PMID 34045674).",
 'g3_Gennai2021': "Gennai S, Guiza ZB, Orsolini C, Gosset M. The influence of non-carious lesions in the surgical treatment of gingival recession: a systematic review and meta-analysis. J Dent. 2022;117:103922. https://doi.org/10.1016/j.jdent.2021.103922 (PubMed abstract read; PMID 34906618).",
 'g3_ArbildoVega2026': "Arbildo-Vega HI, Coronel-Zubiate FT, Cruzado-Oliva FH, et al. Efficacy of combined periodontal-restorative treatment versus periodontal treatment alone for gingival recession associated with non-carious cervical lesions: a systematic review and meta-analysis. BMC Oral Health. 2026;26(1). https://doi.org/10.1186/s12903-026-09404-1 (PubMed abstract read; PMID 42675471).",
 'g3_Oliveira2022': "de Oliveira LML, Souza CA, Cunha S, Siqueira R, Vajgel BCF, Cimões R. Treatment efficacy of gingival recession defects associated with non-carious cervical lesions: a systematic review. J Periodontal Implant Sci. 2022;52(2):91-115. https://doi.org/10.5051/jpis.2102580129 (PubMed abstract read; PMID 35505572).",
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
