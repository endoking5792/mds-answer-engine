"""Print review items: claim, best sentence on the cited page, best sentence anywhere in the source."""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import textbook_check as tc
R = "/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries/sources/textbook_audit.json"
def best_on(text, claim):
    sents = re.split(r"(?<=[.;])\s", text)
    ws = tc.words(re.sub(r"\([^)]*\)|\[[^\]]*\]", " ", claim))
    best, bs = "", -1
    for s in sents:
        sw = tc.words(s)
        k = sum(1 for w in ws if w in sw or (len(w) >= 6 and w[:6] in s))
        if k > bs: best, bs = s, k
    return best
if __name__ == "__main__":
    start, n = int(sys.argv[1]), int(sys.argv[2])
    recs = json.load(open(R, encoding="utf-8"))
    idx = [i for i, r in enumerate(recs) if r["status"] == "review" and r["source"] in ("ANDR","BERM","HARTY","COHEN","INGLE","TROPE10","KOHLI","OGLE","HEXEM1","HEXEM2")]
    idx.sort(key=lambda i: (recs[i].get("locate", {}).get("cat", "") != "not-found", recs[i]["file"], recs[i]["line"]))
    json.dump(idx, open("/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries/sources/verdict_order.json", "w"))
    for k, i in enumerate(idx[start:start + n], start):
        r = recs[i]; key = r["source"]; a, b = r["pages"][0]
        cited_txt = " ".join(tc.page_text(key, p) for p in range(a, (b or a) + 1))
        off = tc.load(key)[1]
        oth = r.get("locate", {}).get("page")
        other_txt = ""
        if oth is not None:
            pages, _ = tc.load(key)
            other_txt = tc.norm(pages.get(oth - off, ""))
        print(f"[{k}] {r['file']} L{r['line']} {key} p{a}{'-'+str(b) if b else ''} cat={r.get('locate',{}).get('cat')}")
        print("  C:", r["sentence"][:190].replace("\n", " "))
        print("  ON-PAGE:", best_on(cited_txt, r["sentence"])[:220].replace("\n", " ") if cited_txt else "(no text for cited page)")
        if oth is not None and other_txt:
            print(f"  OTHER p{oth}:", best_on(other_txt, r["sentence"])[:200].replace("\n", " "))
