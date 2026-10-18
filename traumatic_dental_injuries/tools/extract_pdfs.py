import fitz, os, sys
src = sys.argv[1]; out_dir = sys.argv[2]
os.makedirs(out_dir, exist_ok=True)
for name in sorted(os.listdir(src)):
    if not name.lower().endswith('.pdf'):
        continue
    p = os.path.join(src, name)
    try:
        d = fitz.open(p)
        first = d[0].get_text()[:300].replace('\n', ' | ')
        out = os.path.join(out_dir, os.path.splitext(name)[0][:60].replace(' ', '_') + '.txt')
        with open(out, 'w', encoding='utf-8') as f:
            for i, pg in enumerate(d, 1):
                f.write(f"\n===== PDF PAGE {i} =====\n")
                f.write(pg.get_text())
        print(f"{len(d):4d}p {name[:60]} :: {first[:160]}")
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
