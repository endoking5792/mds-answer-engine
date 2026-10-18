import re, glob, os
from locators import L, F, find
BOOK = {
 'Sikri2019':'Sikri VK. Essentials of Endodontics. 2nd ed. New Delhi: CBS Publishers & Distributors; 2019. Ch.17 Endodontic Smear Layer.',
 'Berman2021':"Berman LH, Hargreaves KM, Rotstein I, editors. Cohen's Pathways of the Pulp. 12th ed. St Louis: Elsevier; 2021.",
 'Rotstein2019':"Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed. Raleigh: PMPH-USA; 2019. Ch.21.",
 'Hilton2013':"Hilton TJ, Ferracane JL, Broome JC, editors. Summitt's Fundamentals of Operative Dentistry: A Contemporary Approach. 4th ed. Chicago: Quintessence; 2013.",
 'Ritter2019':"Ritter AV, Boushell LW, Walter R, editors. Sturdevant's Art and Science of Operative Dentistry. 2nd South Asian ed (adaptation of 7th ed). Elsevier; 2019.",
 'Craig2002':'Craig RG, editor. Restorative Dental Materials. 11th ed. St Louis: Mosby; 2002.',
 'Anusavice2013':"Anusavice KJ, Shen C, Rawls HR, editors. Phillips' Science of Dental Materials. 12th ed. St Louis: Elsevier; 2013.",
 'Mount2016':'Mount GJ, Hume WR, Ngo HC, Wolff MS. Preservation and Restoration of Tooth Structure. 3rd ed. Wiley; 2016.',
 'Nakabayashi1998':'Nakabayashi N, Pashley DH. Hybridization of Dental Hard Tissues. Tokyo: Quintessence; 1998.',
 'Basrani2015':'Basrani B, editor. Endodontic Irrigation: Chemical Disinfection of the Root Canal System. Cham: Springer; 2015. Ch.10 Sonic and Ultrasonic Irrigation.',
 'Banerjee2011':"Banerjee A, Watson TF. Pickard's Manual of Operative Dentistry. 9th ed. Oxford: Oxford University Press; 2011.",
 'DH':'Dentine Hypersensitivity (multi-author text), Ch.5 The Physiological Basis of Dentin Hypersensitivity. File in mds-textbooks; editors and year not verified.',
 'Haapasalo2010':'Haapasalo M, Shen Y, Qian W, Gao Y. Irrigation in endodontics. Dent Clin North Am 2010;54(2):291-312 (full text read).',
 'BedranRusso2017':'Bedran-Russo A, Leme-Kraus AA. An overview of dental adhesive systems and the dynamic tooth-adhesive interface. Dent Clin North Am 2017;61(4):713-731 (full text read).',
 'Pandian2026':'Guruswamy Pandian AP, Bellani D, Jibu RM, Agnihotri V. Endodontic intracanal medicaments and agents: the old and the new, what is the evidence? Dent Clin North Am 2026;70(1):45-62 (full text read).',
 'Stangel2007':'Stangel I, Ellis TH, Sacher E. Adhesion to tooth structure mediated by contemporary bonding systems. Dent Clin North Am 2007;51(3):677-694 (full text read).',
 'Siqueira':'Siqueira JF Jr, Rocas IN, et al. Treatment of Endodontic Infections. 2nd ed. Quintessence; Ch.12 Chemomechanical preparation (edition year not verified).',
 'Alani':"Alani A, Patel M. Adhesive Techniques in Restorative Dentistry. BDJ Clinician's Guides. Springer (edition year not verified).",
 'Hargreaves2012':"Hargreaves KM, Goodis HE, Tay FR, editors. Seltzer and Bender's Dental Pulp. 2nd ed. Chicago: Quintessence; 2012. Ch.3.",
 'Violich2010':'Violich DR, Chandler NP. The smear layer in endodontics - a review. Int Endod J 2010;43(1):2-15. doi:10.1111/j.1365-2591.2009.01627.x (PubMed abstract only).',
 'Torabinejad2002':'Torabinejad M, Handysides R, Khademi AA, Bakland LK. Clinical implications of the smear layer in endodontics: a review. Oral Surg Oral Med Oral Pathol Oral Radiol Endod 2002;94(6):658-66. doi:10.1067/moe.2002.128962 (PubMed abstract only).',
 'Shahravan2007':'Shahravan A, Haghdoost AA, Adl A, Rahimi H, Shadifar F. Effect of smear layer on sealing ability of canal obturation: a systematic review and meta-analysis. J Endod 2007;33(2):96-105. doi:10.1016/j.joen.2006.10.007 (PubMed abstract only).',
 'Teja2025':'Teja KV et al. Efficacy of gel- and solution-based formulations of conventional endodontic disinfectants during root canal shaping: a systematic review. Eur Endod J 2025;10(6):447-455. doi:10.14744/eej.2025.97059 (PubMed abstract only).',
 'Usta2026':'Usta SN, Doğuş E, Gündoğar M. Effectiveness of the GentleWave system in root canal disinfection: a systematic review. BMC Oral Health 2026;26(1):296. doi:10.1186/s12903-026-07688-x (PubMed abstract only).',
 'Hussein2026':'Hussein HM, Ali AH. Nanoparticle-assisted endodontic irrigation: a systematic review of preclinical studies. Clin Cosmet Investig Dent 2026;18:610759. doi:10.2147/CCIDE.S610759 (PubMed abstract only).',
 'Polak2026':'Polak A et al. The effect of aluminum oxide air abrasion on composite adhesion to enamel and dentin: literature review 2020-2024. Wiad Lek 2026;79(1):210-214. doi:10.36740/WLek/214882 (PubMed abstract only).',
 'Verma2026':'Verma S et al. Effect of surface preparation methods on the shear bond strength of universal and self-etch adhesive systems: an in vitro study. J Oral Biol Craniofac Res 2026;16(2):101408. doi:10.1016/j.jobcr.2026.101408 (PubMed abstract only).',
 'Jowkar2025':'Jowkar Z et al. Influence of surface treatments on the bond strength of a self-adhesive bulk-fill composite resin to cut and uncut enamel: an in vitro study. Front Dent 2025;22:45. doi:10.18502/fid.v22i45.20296 (PubMed abstract only).',
}
RANGE = {'75':(2550,3000),'50':(1700,2000),'25':(850,1000),'20':(680,800),'10':(320,400),'5':(160,200)}
for p in sorted(glob.glob('SL_*.md')):
    s=open(p,encoding='utf8').read()
    s=s.split('\n## SOURCE LIST')[0]
    s=re.sub(r'\n\*\*FAILURE DISCLOSURE:.*\n','\n',s)
    loc=re.search(r'<!--LOC: (.*?)-->',s); ref=re.search(r'<!--REF: (.*?)-->',s)
    keys=[k.strip() for k in loc.group(1).split(',')]; refs=[k.strip() for k in ref.group(1).split(',')]
    # word count of exam mode
    m=re.search(r'## EXAM MODE(.*?)(?=\n## HIGH-YIELD)',s,re.S); wc=len(m.group(1).split())
    mk=re.search(r'\*\*Marks:\*\* (\d+)m',s).group(1)
    lo,hi=RANGE[mk]
    if wc<lo:
        disc=f"\n**FAILURE DISCLOSURE:** Exam Mode is {wc} words, below the Section 7 range of {lo}-{hi} for {mk} marks. First draft to be expanded after discussion; the content is a scaffold, not full-length.\n"
        s=s.replace('\n<!--LOC:',disc+'\n<!--LOC:',1)
    out=['\n## SOURCE LIST','\n**[SRC] textbook locators** (file chapter, PDF page marker; printed page where the offset is confirmed):']
    for k in keys:
        f,ph=L[k]; path,off,cite=F[f]; pg,_=find(k); assert pg,k
        pp=(f"printed p.{off[1]+pg-1}" if isinstance(off,tuple) else f"PDF p.{pg}"+(f" (printed p.{pg-off})" if off else ""))
        out.append(f"- {cite}, {os.path.basename(path)[:60]}, {pp}: \"{ph}\"")
    out.append('\n**[LIT] journal items** are listed in REFERENCES (abstract-level only; no full text read).')
    out.append('\n## REFERENCES (alphabetical)')
    for r in sorted(BOOK[k] for k in refs): out.append('- '+r)
    s=s.rstrip()+'\n'+'\n'.join(out)+'\n'
    open(p,'w',encoding='utf8').write(s)
    print(p[:60].ljust(62),mk+'m','exam words',wc,'range',lo,hi)
