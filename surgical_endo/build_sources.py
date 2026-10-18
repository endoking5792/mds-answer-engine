import re, glob, os
from locators import L, F, find
BOOK = {
 'Berman2021':"Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.11 Periradicular surgery (Johnson BR, Fayad MI, Berman LH).",
 'Rotstein2019':"Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.24 Surgical endodontics.",
 'Gopikrishna2021':"Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. Wolters Kluwer; 2021. Ch.22 Endodontic surgery.",
 'Chong2017':"Chong BS, editor. Harty's Endodontics in Clinical Practice. 7th ed. Elsevier; 2017 (year not verified from the file). Ch.10 Surgical endodontics (Gutmann JL).",
 'vonArx2019':"Torabinejad M, Rubinstein R, editors. The Art and Science of Contemporary Surgical Endodontics. Hanover Park, IL: Quintessence; 2019. Ch.17 Outcomes of endodontic surgery (von Arx T, White SN).",
 'Velvart2019':"Torabinejad M, Rubinstein R, editors. The Art and Science of Contemporary Surgical Endodontics. Hanover Park, IL: Quintessence; 2019. Ch.9 Soft tissue management (Velvart P, Peters OA).",
 'Evans2012':"Evans GE, Bishop K, Renton T. Guidelines for Surgical Endodontics. London: Royal College of Surgeons of England, Faculty of Dental Surgery; 2012.",
 'vonArx2008':"von Arx T, Salvi GE. Incision techniques and flap designs for apical surgery in the anterior maxilla. Eur J Esthet Dent 2008;3(2):110-26 (PubMed abstract only).",
 'Kuo2026':"Kuo PJ, Hsieh SC, Kuo TC, Wen WC, Wu TH, Do JH. A dual-layer flap preparation approach utilizing the external coronally advanced flap and the internal trapdoor periosteal flap for endodontic microsurgery in the esthetic zone: technique and case report. Int J Periodontics Restorative Dent 2026;46(5):554-565. doi:10.11607/prd.7648 (PubMed abstract only; technique report and single case).",
 'Tsesis2025':"Tsesis I, Blazer T, Elbahary S, Rosen E. Complications of endodontic surgery. In: Jain PR, editor. Common Complications in Endodontics. Cham: Springer; 2025. Ch.9.",
 'Niemczyk2010':"Niemczyk SP. Essentials of endodontic microsurgery. Dent Clin North Am 2010;54(2):375-399 (full text read).",
 'Floratos2017':"Floratos S, Kim S. Modern endodontic microsurgery concepts: a clinical update. Dent Clin North Am 2017;61(1):81-91 (full text read).",
 'Rubinstein2021':"Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. Elsevier; 2021. Ch.20 Apical microsurgery (Rubinstein R, Fayad MI, Torabinejad M).",
 'Parirokh2019':"Torabinejad M, Rubinstein R, editors. The Art and Science of Contemporary Surgical Endodontics. Hanover Park, IL: Quintessence; 2019. Ch.11 Root-end filling materials (Parirokh M, Shabahang S).",
 'Jurosky2019':"Torabinejad M, Rubinstein R, editors. The Art and Science of Contemporary Surgical Endodontics. Hanover Park, IL: Quintessence; 2019. Ch.14 Wound healing (Jurosky KA).",
 'Torabinejad2019adj':"Torabinejad M, Rubinstein R, editors. The Art and Science of Contemporary Surgical Endodontics. Hanover Park, IL: Quintessence; 2019. Ch.15 Adjunctive procedures (Torabinejad M, Lundgren T, Tatakis DN, Fayad MI).",
 'SaidAlNaief2019':"Torabinejad M, Rubinstein R, editors. The Art and Science of Contemporary Surgical Endodontics. Hanover Park, IL: Quintessence; 2019. Ch.4 Radiolucent periapical pathosis (Said-Al-Naief N).",
 'Ogle2011':"Ogle OE, Swantek J, Kamoh A. Hemostatic agents. Dent Clin North Am 2011;55(3):433-439 (full text read).",
 'Lieblich2012':"Lieblich SE. Endodontic surgery. Dent Clin North Am 2012;56(1):121-132 (full text read).",
 'Kinaia2012':"Kinaia BM, Chogle SMA, Kinaia AM, Goodis HE. Regenerative therapy: a periodontal-endodontic perspective. Dent Clin North Am 2012;56(3):537-547 (full text read).",
 'Torabinejad2015':"Torabinejad M, Landaez M, Milan M, Sun CX, Henkin J, Al-Ardah A, et al. Tooth retention through endodontic microsurgery or tooth replacement using single implants: a systematic review of treatment outcomes. J Endod 2015;41(1):1-10. doi:10.1016/j.joen.2014.09.002 (PubMed abstract only).",
 'Kapoor2025':"Kapoor A, Alagarsamy R, Lal B, Rana AS, Kaur A, Sharma S, Logani A. Dynamic navigation in endodontics: scope, benefits, and challenges - a systematic review. J Endod 2025;51(7):879-889.e2. doi:10.1016/j.joen.2025.04.010 (PubMed abstract only).",
 'Wei2023':"Wei X, Du Y, Zhou X, et al. Expert consensus on digital guided therapy for endodontic diseases. Int J Oral Sci 2023;15(1):54. doi:10.1038/s41368-023-00261-0 (PubMed abstract only).",
 'Sedgley2021':"Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. Elsevier; 2021. Ch.1 Pathogenesis of pulp and periapical diseases (Sedgley C, Silva R, Fouad AF).",
 'Setzer2021':"Torabinejad M, Fouad AF, Shabahang S, editors. Endodontics: Principles and Practice. 6th ed. Elsevier; 2021. Ch.22 Endodontic treatment outcomes (Setzer F, Chogle S, Torabinejad M).",
 'Landwehr2021':"Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.3 Lesions that mimic endodontic pathosis (Landwehr DJ).",
 'Roda2021':"Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.10 Nonsurgical retreatment (Roda RS, Gettleman BH, Johnson SC).",
 'Lin2021':"Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.16 Pathobiology of apical periodontitis (Lin LM, Huang GT-J).",
 'Pecora1995':"Pecora G, Kim S, Celletti R, Davarpanah M. The guided tissue regeneration principle in endodontic surgery: one-year postoperative results of large periapical lesions. Int Endod J 1995;28(1):41-6. doi:10.1111/j.1365-2591.1995.tb00155.x (PubMed abstract only).",
 'Raabe2026':"Raabe C, Schmidt V, Schriber M, Chappuis V, Suter VGA. Three-dimensional changes in mandibular jaw cysts following decompression surgery: a retrospective cohort study. BMC Oral Health 2026;26(1):343. doi:10.1186/s12903-026-07729-5 (PubMed abstract only).",
 'Kader2024':"Kader D, Ozalp O, Ozbudak IH, Sindel A, Altay MA. The effect of decompression on histologic diagnoses of cystic jaw lesions. Ann Ital Chir 2024;95(5):901-908. doi:10.62713/aic.3589 (PubMed abstract only).",
 'Kaygisiz2024':"Kaygisiz OF, Karsli ED. Evaluation of cyst treatment technique, cyst type, size differences and healing by fractal analysis. BMC Oral Health 2024;24(1):1271. doi:10.1186/s12903-024-04945-9 (PubMed abstract only).",
 'Wang2024':"Wang FM, Liang H, Glickman GN, Gutmann JL. Use of a Penrose drain for decompression of a large periapical lesion: a case report with 4.5-year follow-up. J Endod 2024;50(10):1521-1526. doi:10.1016/j.joen.2024.07.005 (PubMed abstract only; single case report).",
 'Walton2002':"Walton RE, Torabinejad M. Principles and Practice of Endodontics. 3rd ed. Philadelphia: WB Saunders; 2002. Part 24 Endodontic surgery.",
 'Barnes1984':"Barnes IE. Surgical Endodontics: A Colour Manual. Lancaster: MTP Press (Kluwer Academic Publishers group); 1984 (old text, used only for historical technique).",
 'Rubinstein2019':"Torabinejad M, Rubinstein R, editors. The Art and Science of Contemporary Surgical Endodontics. Hanover Park, IL: Quintessence; 2019. Ch.10 Apical microsurgery: application of armamentaria, materials, and methods (Rubinstein R, Fayad MI).",
 'Setzer2010':"Setzer FC, Shah SB, Kohli MR, Karabucak B, Kim S. Outcome of endodontic surgery: a meta-analysis of the literature, part 1. J Endod 2010;36(11):1757-65. doi:10.1016/j.joen.2010.08.007 (PubMed abstract only).",
 'Setzer2012':"Setzer FC, Kohli MR, Shah SB, Karabucak B, Kim S. Outcome of endodontic surgery: a meta-analysis of the literature, part 2. J Endod 2012;38(1):1-10. doi:10.1016/j.joen.2011.09.021 (PubMed abstract only).",
 'Kohli2018':"Kohli MR, Berenji H, Setzer FC, Lee SM, Karabucak B. Outcome of endodontic surgery: a meta-analysis of the literature, part 3. J Endod 2018;44(6):923-931. doi:10.1016/j.joen.2018.02.021 (PubMed abstract only).",
 'Pinto2020':"Pinto D, Marques A, Pereira JF, Palma PJ, Santos JM. Long-term prognosis of endodontic microsurgery: a systematic review and meta-analysis. Medicina (Kaunas) 2020;56(9):447. doi:10.3390/medicina56090447 (PubMed abstract only).",
 'Flynn2024':"Flynn R, Foschi F, Maloney B, Creavin G, Duncan HF. The impact of bone grafting with/without barrier membrane placement on the outcome of apical surgery: a systematic review and meta-analysis. Int Endod J 2024;57(8):1006-1020. doi:10.1111/iej.14066 (PubMed abstract only).",
 'Rewthamrongsris2026':"Rewthamrongsris P, Chokechanachaisakul U, Khurshid Z, Osathanon T. Comparing guided surgical endodontics using static guidance, dynamic navigation, and augmented reality: a systematic review and meta-analysis. Eur J Dent 2026. doi:10.1055/s-0046-1824743 (PubMed abstract only).",
 'Karlovic2005':"Karlovic Z, Pezelj-Ribaric S, Miletic I, Jukic S, Grgurevic J, Anic I. Erbium:YAG laser versus ultrasonic in preparation of root-end cavities. J Endod 2005;31(11):821-3. doi:10.1097/01.don.0000158234.33581.e9 (PubMed abstract only; in vitro).",
}
# Chapter-author-first reference format (Niranjan, 2026-10-18): "Author(s). Chapter. In: Editors, editors. Book. ..."
_OVERRIDE = {
 'Berman2021':"Johnson BR, Fayad MI, Berman LH. Periradicular surgery. In: Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021. Ch.11.",
 'Rotstein2019':"Torabinejad M, Sabeti M, Glickman GN. Surgical endodontics. In: Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.24 (chapter authors decoded from a garbled author line in the extracted file; verify against the printed book).",
 'Gopikrishna2021':"Gopikrishna V, editor. Grossman's Endodontic Practice. 14th ed. Wolters Kluwer; 2021. Ch.22 Endodontic surgery (no individual chapter author is named in the file, so the editor is cited).",
 'Chong2017':"Gutmann JL. Surgical endodontics. In: Chong BS, editor. Harty's Endodontics in Clinical Practice. 7th ed. Elsevier; 2017 (year not verified from the file). Ch.10.",
}
import re as _re
for _k,_v in list(BOOK.items()):
    if _k in _OVERRIDE: BOOK[_k]=_OVERRIDE[_k]; continue
    _m=_re.match(r"^(?P<ed>.+? editors?)\. (?P<rest>.+?)\. Ch\.(?P<n>\d+) (?P<title>.+?) \((?P<au>[^()]+)\)\.(?P<tail>.*)$",_v)
    if _m: BOOK[_k]=f"{_m['au']}. {_m['title']}. In: {_m['ed']}. {_m['rest']}. Ch.{_m['n']}.{_m['tail']}"

RANGE = {'100':(3200,3500),'75':(2550,3000),'50':(1700,2000),'25':(850,1000),'20':(680,800),'10':(320,400),'7':(230,280),'5':(160,200)}  # 7m is not in the Section 7 table; interpolated at about 34-40 words per mark
def run(files=None):
  for p in sorted(files or glob.glob('Q*.md')+glob.glob('P*.md')):
    s=open(p,encoding='utf8').read()
    s=s.split('\n## SOURCE LIST')[0]
    s=re.sub(r'\n\*\*FAILURE DISCLOSURE:.*\n','\n',s)
    loc=re.search(r'<!--LOC: (.*?)-->',s); ref=re.search(r'<!--REF: (.*?)-->',s)
    keys=[k.strip() for k in loc.group(1).split(',') if k.strip()]; refs=[k.strip() for k in ref.group(1).split(',') if k.strip()]
    m=re.search(r'## EXAM MODE(.*?)(?=\n## HIGH-YIELD)',s,re.S); wc=len(m.group(1).split())
    mk=re.search(r'\*\*Marks:\*\* (\d+)m',s).group(1)
    lo,hi=RANGE[mk]
    if wc<lo or wc>hi:
        side='below' if wc<lo else 'above'
        disc=f"\n**FAILURE DISCLOSURE:** Exam Mode is {wc} words, {side} the Section 7 range of {lo}-{hi} for {mk} marks. First draft; adjust after discussion.\n"
        s=s.replace('\n<!--LOC:',disc+'\n<!--LOC:',1)
    out=['\n## SOURCE LIST','\n**[SRC] textbook locators** (file chapter, PDF page marker; printed page where the offset is confirmed):']
    for k in dict.fromkeys(keys):
        f,ph=L[k]; path,off,cite=F[f]; pg,_=find(k); assert pg,k
        pp=(f"printed p.{off[1]+pg-1}" if isinstance(off,tuple) else f"PDF p.{pg}"+(f" (printed p.{pg-off})" if off else ""))
        out.append(f"- {cite}, {os.path.basename(path)[:60]}, {pp}: \"{ph}\"")
    out.append('\n**[LIT] journal items** are listed in REFERENCES (abstract-level only; no full text read).')
    out.append('\n## REFERENCES (alphabetical)')
    for r in sorted(set(BOOK[k] for k in refs)): out.append('- '+r)
    s=s.rstrip()+'\n'+'\n'.join(out)+'\n'
    open(p,'w',encoding='utf8').write(s)
    print(p[:60].ljust(62),mk+'m','exam words',wc,'range',lo,hi)
if __name__=='__main__':
    import sys; run(sys.argv[1:] or None)
