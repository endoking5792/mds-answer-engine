import re,sys,json,os
D="/Users/niranjan/.claude/answer_tools/gic_dossier/"
FILES={"A":"A_mount.md","B":"B_dental_materials_books.md","C1":"C1_summitt_sturdevant.md","C2":"C2_other_operative.md","D":"D_endo_books.md","E":"E_dcna_and_notes.md","F":"F_live_literature.md","G":"G_sikri_textbook.md"}
ENT=re.compile(r'^(?:T(\d+)\|)?-?\s*\[(.*?)\]\s*(.*)$')
def parse(key):
    p=D+FILES[key]
    if not os.path.exists(p): return {}
    out={}; sec=None
    for i,l in enumerate(open(p,encoding="utf-8").read().split("\n"),1):
        m=re.match(r'^#{2,3}\s+T(\d+)\b',l)
        if m: sec=int(m.group(1)); continue
        if key in("A","D","E") and not (l.startswith("- [")): continue
        if key in("B","C1","C2","G") and not re.match(r'^T\d+\|\[',l): continue
        if key=="F": continue
        m=ENT.match(l)
        if not m: continue
        t,meta,fact=m.groups()
        t=int(t) if t else sec
        f=re.search(r'(?:FILE|DCNA|NOTE):\s*([^|\]]+)',meta); pg=re.search(r'PDF p\.\s*([\w\-–, ]+?)\s*(?:\||$)',meta); an=re.search(r'ANCHOR:\s*"(.*)"\s*$',meta)
        bk=re.search(r'BOOK:\s*([^|]+)',meta)
        out[i]=dict(t=t,book=(bk.group(1).strip() if bk else ""),file=(f.group(1).strip() if f else ""),page=(pg.group(1).strip() if pg else ""),anchor=(an.group(1) if an else ""),fact=fact,meta=meta,raw=l)
    return out
if __name__=="__main__":
    key=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3]); ts=set(int(x) for x in sys.argv[4].split(",")) if len(sys.argv)>4 else None
    for i,e in parse(key).items():
        if a<=i<=b and (ts is None or e["t"] in ts):
            f=e["file"][:28]; print(f'{key}{i} T{e["t"]} {e["book"][:9]}|{f}|p{e["page"]}| {e["fact"][:330]}')
