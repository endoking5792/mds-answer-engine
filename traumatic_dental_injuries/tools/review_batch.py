"""Print review items with the best-matching source sentence, in batches (for manual verdicts)."""
import json, re, sys
sys.path.insert(0, "/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries/tools")
import textbook_check as tc
R = "/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries/sources/textbook_audit.json"
def best_snippet(key, a, b, claim):
    txt = ""
    for n in range(a, (b or a) + 1):
        txt += " " + tc.page_text(key, n)
    sents = re.split(r"(?<=[.;])\s", txt)
    ws = tc.words(re.sub(r"\([^)]*\)", " ", claim))
    best, bs = "", -1
    for s in sents:
        sw = tc.words(s)
        k = sum(1 for w in ws if w in sw or (len(w) >= 6 and w[:6] in s))
        if k > bs:
            best, bs = s, k
    return best[:260]
def items(filter_fn):
    recs = json.load(open(R, encoding="utf-8"))
    return [(i, r) for i, r in enumerate(recs) if filter_fn(r)]
if __name__ == "__main__":
    mode, start, n = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    if mode == "review":
        f = lambda r: r["status"] == "review"
    elif mode == "adjacent":
        f = lambda r: "adjacent" in r["status"]
    elif mode == "quote":
        f = lambda r: r["status"].startswith("quote")
    else:
        f = lambda r: r["status"].startswith("pending")
    sel = items(f)[start:start + n]
    for i, r in sel:
        key = r["source"]; a, b = r["pages"][0]
        snip = best_snippet(key, a, b[0] if False else (r["pages"][0][1]), r["sentence"]) if key in ("ANDR","BERM","HARTY","COHEN","INGLE","TROPE10","KOHLI","OGLE","HEXEM1") else ""
        print(f"#{i} {r['file']} L{r['line']} {key} {r['cite'][:60]} | miss#={r.get('missing_numbers')} s={r.get('score')}")
        print("   CLAIM:", r["sentence"][:230])
        print("   SRC  :", snip)
