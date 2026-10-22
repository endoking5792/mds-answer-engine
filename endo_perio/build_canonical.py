"""Build one canonical answer per question from the Study/Exam drafts.

Each section = explanation (Study Mode paragraphs, plus matching Q01 paragraphs where the
draft's own Study Mode only pointed to Q01) followed by "#### ✎ Exam core" (the Exam Mode
text for that section, unchanged). Exam-core length = the original Exam Mode, so it stays
within the Section 7 range. Output: canonical/<name>_CANONICAL.md, then sources are added.
Run: python3 build_canonical.py
"""
import re, os, glob
from locators import L, F, page_label
from build_sources import BOOK

# Locator keys used by each paragraph of Q01's Study Mode (S0..S15), for imported paragraphs.
Q01KEYS = {
 0: 'g_unit w_periapical g_simring g_bender c_50 g_50', 1: 'g_simring',
 2: 'gu_def wa_pulpless wa_both he_dx', 3: 'i_paths c_channels c_vascular c_45 c_gut28 i_3040 gu_45 i_kirk h_1000',
 4: 'i_18 gu_10cej', 5: 'c_denuded gu_tubnormal h_plaque i_twoview i_notch',
 6: 'c_reverse c_riskf c_medic h_20wk h_20pc h_depth',
 7: 'c_riskf c_rare c_causal wa_05 wa_trifling wa_2509 wa_911 wa_negligible wa_noperio gu_seldom gu_few',
 8: 'i_controv h_conflict c_fibrosis h_degen h_87 c_70 wa_little wa_4pc wa_3pc gu_limited c_main h_sound i_neuro',
 9: 'i_curette wa_sever',
 10: 'i_similar h_pcr he_micro he_noprofile i_spiro gu_spiro i_fungi20 i_lform i_cmv s_chol s_russell s_foreign g_trauma he_risk',
 11: 'g_simon g_belk i_basis g_oliet w_disagree gu_none he_history he_notrelevant he_1999 he_generic',
 12: 'wa_conical wa_1mm wa_1week wa_base wa_sounding gu_blowout',
 13: 'g_predict g_cannot g_slow i_23 i_aggressive wa_drain g_regardless gu_doubtful gu_extrusion',
 14: 'c_62 c_fail h_68 h_38 wa_implant a_32 a_691',
 15: 'k_repair k_grafts k_melcher k_gtr c_gtrcomb',
}
# Section heading prefix (exam "### n.") -> study blocks. "S3" = own block 3, "Q01:S3" = Q01 block 3.
# Files whose Exam Mode has no ### headings use the key "_all" (one explanation, one exam core).
MAP = {
 'Q01': {'1.':['S0','S1'],'2.':['S2'],'3.':['S3','S4','S5'],'4.':['S6','S7'],'5.':['S8','S9'],'6.':['S10'],
         '7.':['S11'],'9.':['S12'],'10.':['S13'],'12.':['S14','S15']},
 'Q02': {'2.':['Q01:S3','Q01:S6','Q01:S8'],'3.':['Q01:S11'],'4.':['S1','S2','S3','S4'],'5.':['S5','S6','S7']},
 'Q03': {'1.':['S1'],'2.':['S2','Q01:S4','Q01:S5'],'3.':['S3','Q01:S6','Q01:S7'],'4.':['S4'],'5.':['Q01:S8'],
         '6.':['Q01:S9'],'7.':['Q01:S10'],'8.':['Q01:S11'],'9.':['Q01:S13']},
 'Q04': {'2.':['Q01:S11'],'4.':['Q01:S12'],'5.':['S1','S2','Q01:S13'],'6.':['Q01:S14','Q01:S15'],'7.':['S3']},
 'Q05': {'2.':['S3'],'3.':['S1'],'4.':['S2','Q01:S3'],'5.':['Q01:S12'],'6.':['Q01:S13']},
 'Q06': {'1.':['S0'],'3.':['S1','Q01:S7'],'4.':['S2'],'5.':['S3'],'6.':['S4']},
 'Q07': {'_all':['S0','Q01:S11','Q01:S13']},
 'Q08': {'_all':['S0','Q01:S3','Q01:S8']},
 'Q09': {'_all':['S0','S1','Q01:S14']},
 'Q10': {'_all':['S0','Q01:S15']},
 'P1': {'_all':['S0','S1','S2']},
 'P2': {'_all':['S0','Q01:S12']},
 'P3': {'_all':['S0','Q01:S8','Q01:S9']},
}
REFOF = {'coh':'Glickman2021','ing':'Rotstein2019','gro':'Gopikrishna2021','har':'Rotstein2017','sel':'Seltzer2012',
         'wei':'Weine2004','gul':'Gulabivala2014','wal':'Walton2002','her':'Herrera2018','kin':'Kinaia2012','and':'Andreana2010'}
POINTER = re.compile(r'^\*\(.*(Q01|Q02).*\)\*$', re.S)   # "(explained in Q01's Study Mode)" notes
XREF = [r' Q01 and Q02 give the full reasoning\.', r' Q03 gives the full account\.', r' The full reasoning is in Q01 \(100m\) and Q04 \(25m\)\.', r' \(see Q01, Claim 2\)']

def sec(s, name, nxt):
    m = re.search(r'\n## '+re.escape(name)+r'[^\n]*\n(.*?)(?=\n## '+nxt+r')', s, re.S)
    return m.group(1).strip() if m else ''

def blocks(text):
    return [b.strip() for b in re.split(r'\n\s*\n', text.strip()) if b.strip()]

def parts(path):
    s = open(path, encoding='utf8').read().split('\n## SOURCE LIST')[0]
    head = s.split('\n<!--LOC:')[0].strip()
    loc = re.search(r'<!--LOC: (.*?)-->', s, re.S).group(1)
    ref = re.search(r'<!--REF: (.*?)-->', s, re.S).group(1)
    study = sec(s, 'STUDY MODE', '(CRITICAL|EXAM)')
    crit = sec(s, 'CRITICAL EVIDENCE SYNTHESIS', 'EXAM')
    exam = sec(s, 'EXAM MODE', 'HIGH-YIELD')
    exam = re.sub(r'^\*\(Estimated writing time[^\n]*\)\*\s*', '', exam)
    tail = s[s.index('\n## HIGH-YIELD'):].strip()
    retr = sec(s, 'Retrieval Report', 'STUDY')
    return dict(head=head, loc=[k.strip() for k in loc.split(',') if k.strip()], ref=[r.strip() for r in ref.split(',') if r.strip()],
                study=blocks(study), crit=crit, exam=exam, tail=tail, retr=retr)

q01 = parts(glob.glob('Q01_*.md')[0])

def resolve(tag, own):
    if tag.startswith('Q01:'):
        i = int(tag[5:]); return q01['study'][i], Q01KEYS[i].split()
    return own['study'][int(tag[1:])], []

RANGE = {'100':(3200,3500),'75':(2550,3000),'50':(1700,2000),'25':(850,1000),'20':(680,800),'10':(320,400),'5':(160,200)}

def build(path):
    code = os.path.basename(path).split('_')[0]
    p = parts(path); mp = MAP[code]; keys = list(p['loc']); used = set()
    def explain(tags):
        out = []
        for t in tags:
            b, k = resolve(t, p); used.add(t)
            if POINTER.match(b): continue
            for x in XREF: b = re.sub(x, '', b)
            out.append(b); keys.extend(k)
        return out
    body = []
    if '_all' in mp:
        ex = explain(mp['_all'])
        body += ['## Explanation', '\n\n'.join(ex), '## ✎ Exam core', p['exam']]
    else:
        secs = re.split(r'\n(?=### )', '\n'+p['exam'])
        for chunk in secs:
            chunk = chunk.strip()
            if not chunk: continue
            first, _, rest = chunk.partition('\n')
            title = first[4:].strip(); num = title.split()[0]
            body.append('## '+title)
            ex = explain(mp.get(num, []))
            if ex: body.append('\n\n'.join(ex))
            body += ['#### ✎ Exam core', rest.strip()]
    own_left = [i for i in range(len(p['study'])) if 'S%d'%i not in used and not POINTER.match(p['study'][i])]
    if own_left:   # never drop explanation silently
        body += ['## Further explanation', '\n\n'.join(p['study'][i] for i in own_left)]
    if p['crit']:
        body += ['## Critical evidence synthesis', p['crit']]
    core_words = len(p['exam'].split())
    mk = re.search(r'\*\*Marks:\*\* (\d+)m', p['head']).group(1); lo, hi = RANGE[mk]
    head = p['head'].split('\n', 1)
    title = head[0] + ' (canonical answer)'
    howto = (f"**How to read this answer:** each section explains the topic first; the part headed **✎ Exam core** is what to write in the exam. "
             f"Exam core: {core_words} words, about {round(core_words/22)} minutes at 22 words a minute (Section 7 range {lo}-{hi} words for {mk} marks). "
             f"The separate Study Mode / Exam Mode draft of this question is kept unchanged in the repository.")
    keys = list(dict.fromkeys(keys))
    refs = list(dict.fromkeys(p['ref'] + [REFOF[L[k][0]] for k in keys]))
    retr = p['retr'] + (" Some explanation paragraphs are taken from Q01, which read the same chapters in full." if any(t.startswith('Q01:') for t in sum(mp.values(), [])) else '')
    out = [title, head[1].strip(), howto, f'<!--LOC: {", ".join(keys)}-->', f'<!--REF: {", ".join(refs)}-->'] + body + [p['tail'], '## How this answer was sourced', retr]
    s = '\n\n'.join(x for x in out if x)
    srcs = ['## SOURCE LIST', '**[SRC] locators** (chapter file, PDF page marker; printed page where the offset is confirmed; verbatim phrase):']
    for k in keys:
        f, ph = L[k]; pth, off, cite = F[f]; lab = page_label(k); assert lab, k
        srcs.append(f'- {cite}, {os.path.basename(pth)[:58]}, {lab}: "{ph}"')
    srcs += ['**[LIT]** items are listed in REFERENCES with DOI; the access level is stated for each.', '## REFERENCES (alphabetical)']
    srcs += ['- '+r for r in sorted(set(BOOK[k] for k in refs))]
    s = s.rstrip() + '\n\n' + '\n'.join(srcs) + '\n'
    os.makedirs('canonical', exist_ok=True)
    outp = os.path.join('canonical', os.path.basename(path).replace('.md', '_CANONICAL.md'))
    open(outp, 'w', encoding='utf8').write(s)
    total = len(s.split('## SOURCE LIST')[0].split())
    print(outp[10:70].ljust(62), mk+'m', 'core', core_words, f'({lo}-{hi})', 'total', total, 'refs', len(refs))

if __name__ == '__main__':
    for p in sorted(glob.glob('Q*.md') + glob.glob('P*.md')):
        build(p)
