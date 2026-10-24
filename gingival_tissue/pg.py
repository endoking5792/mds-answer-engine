import sys,re,os
OP=os.path.expanduser('~/mds-textbooks/Operative_and_Dental_Materials_Textbooks/')
f=sys.argv[1]; a,b=int(sys.argv[2]),int(sys.argv[3])
p=[x for x in os.listdir(OP) if x.startswith(f)][0]
t=open(OP+p,encoding='utf8').read()
parts=re.split(r'(?:<!-- PDF page (\d+) -->|===== PAGE (\d+) =====)',t)
for i in range(1,len(parts),3):
    n=int(parts[i] or parts[i+1])
    if a<=n<=b: print(f'\n#### P{n}\n'+re.sub(r'\n\s*\n+','\n',parts[i+2]))
