import sys,re
# usage: python3 addloc.py < file with lines: key | srckey | phrase
p='locators.py'; s=open(p).read()
new=[]
for line in sys.stdin:
    line=line.rstrip('\n')
    if not line.strip(): continue
    k,f,ph=[x.strip() for x in line.split('|',2)]
    if re.search(r"^ '%s':"%re.escape(k), s, re.M): continue
    new.append(" %r: (%r, %r),\n"%(k,f,ph))
s=s.replace("L = {\n","L = {\n"+''.join(new),1)
open(p,'w').write(s); print(len(new),'added')
