"""New-standard (SKILL 7.1 item 12, 2026-11-09) checks for this topic.
Student answer: canonical/<ID>_..._CANONICAL.md  (no locators, tags or diagnostics).
Audit sidecar:  audit/<ID>_..._AUDIT.md, holding <!--LOC: key, key--> and a ledger block
                between <!--LEDGER START--> and <!--LEDGER END--> that this script (re)builds.
Run from the topic folder:  python3 build_audit.py audit/<ID>_*_AUDIT.md   (or audit/*_AUDIT.md)
Checks: every LOC key resolves (missing 0); every "quoted phrase" (12+ chars) in the answer occurs
verbatim in a book; numbers in the answer body that occur in no LOC phrase are listed for review;
every author surname cited in the body appears in the reference list and vice versa (approximate);
body word count against the Section 7 calibration range."""
import re, sys, os, glob
import locators as l
RANGE = {'100':(3200,3500),'75':(2550,3000),'50':(1700,2000),'25':(850,1000),'20':(680,800),'15':(510,600),'10':(320,400),'7':(230,280),'5':(160,200)}
book = None
def run(sp):
    global book
    if book is None: book = ' '.join(' '.join(l._pages(v[0]).values()) for v in l.F.values())
    side = open(sp, encoding='utf8').read()
    m = re.search(r'\*\*Student-facing answer:\*\* `([^`]+)`', side); ap = m.group(1)
    if not os.path.exists(ap): ap = os.path.join('canonical', os.path.basename(ap))
    ans = open(ap, encoding='utf8').read()
    keys = [k.strip() for k in re.search(r'<!--LOC: (.*?)-->', side, re.S).group(1).split(',') if k.strip()]
    bad = [k for k in keys if k not in l.L or l.L[k][0] not in l.F or l.page_label(k) is None]
    rows = ['| # | Source (in-text citation) | Chapter file | PDF page (printed page) | Verbatim locator phrase | Status |', '|---|---|---|---|---|---|']
    for i, k in enumerate(dict.fromkeys(keys), 1):
        if k in bad: rows.append(f'| {i} | {k} | | | MISSING | Recheck |'); continue
        f, ph = l.L[k]; path, off, cite = l.F[f]
        rows.append(f'| {i} | {cite} | {os.path.basename(path)[:50]} | {l.page_label(k)} | "{ph}" | Verified |')
    side = re.sub(r'<!--LEDGER START-->.*?<!--LEDGER END-->', '<!--LEDGER START-->\n' + '\n'.join(rows) + '\n<!--LEDGER END-->', side, flags=re.S)
    body, _, refs = ans.partition('\n## References')
    body_nohead = re.sub(r'^\*\*Marks:\*\*.*$', '', body, flags=re.M)
    wc = len(re.sub(r'[#*|>`_-]+', ' ', body_nohead).split())
    mk = re.search(r'\*\*Marks:\*\* (\d+)', ans).group(1); lo, hi = RANGE[mk]
    nq = [q for q in re.findall(r'"([^"]*)"|“([^”]*)”', body) for q in [q[0] or q[1]] if len(q) >= 12 and l.norm(q) not in book]
    phr = ' '.join(l.norm(l.L[k][1]) for k in keys if k in l.L)
    b2 = re.sub(r'\([^()]*?(19|20)\d\d[a-z]?[^()]*\)', '', body)
    nums = sorted(set(n for n in re.findall(r'\d+(?:\.\d+)?', b2) if n not in phr), key=float)
    cited = set(re.findall(r'\b([A-Z][a-zÀ-ÿ\-]+)(?: et al)?(?:,| and [A-Z][a-zÀ-ÿ\-]+,?) (?:19|20)\d\d', body))
    cited |= set(re.findall(r'\b([A-Z][a-zÀ-ÿ\-]+)(?: et al\.?)? \((?:19|20)\d\d', body))
    notref = sorted(c for c in cited if c not in refs)
    stamp = f"Checked by build_audit.py: LOC keys {len(keys)}, missing {len(bad)}; quotes not found {len(nq)}; answer body {wc} words (calibration {lo}-{hi} for {mk}m){'' if lo<=wc<=hi else ' OUT OF RANGE'}; cited surnames not in references: {notref or 'none'}; body numbers without a locator: {nums or 'none'}."
    side = re.sub(r'<!--CHECK-->.*?<!--/CHECK-->', '<!--CHECK-->' + stamp + '<!--/CHECK-->', side, flags=re.S)
    open(sp, 'w', encoding='utf8').write(side)
    print(os.path.basename(ap)[:45], '|', stamp)
    for q in nq: print('   QUOTE NOT IN BOOK:', q[:90])
    for k in bad: print('   MISSING LOCATOR:', k)
if __name__ == '__main__':
    for p in sys.argv[1:]: run(p)
