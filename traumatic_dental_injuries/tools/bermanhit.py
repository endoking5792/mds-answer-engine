import re,sys
pat=re.compile(sys.argv[2],re.I); lo,hi=int(sys.argv[3]),int(sys.argv[4]); mx=int(sys.argv[5]) if len(sys.argv)>5 else 40
cur=None; n=0
for l in open(sys.argv[1],encoding='utf-8',errors='replace'):
    m=re.match(r'===== PDF PAGE (\d+) =====',l)
    if m: cur=int(m.group(1)); continue
    if cur and lo<=cur<=hi and pat.search(l):
        n+=1
        if n<=mx: print(f"[P{cur}] {l.strip()[:260]}")
print("--",n,"hits")
