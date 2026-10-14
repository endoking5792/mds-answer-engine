import sys,dossier as D
c={}
for sid in sys.argv[1:]:
    import re
    m=re.match(r"^(C1|C2|A|B|D|E|G)(\d+)$",sid); k,n=m.group(1),int(m.group(2))
    c.setdefault(k,D.parse(k)); e=c[k].get(n)
    print(f"{sid} [{e['book'] or ''}|{e['file'][:30]}|p{e['page']}] {e['fact']}\n" if e else f"{sid} MISSING\n")
