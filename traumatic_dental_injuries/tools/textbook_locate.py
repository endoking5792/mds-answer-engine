"""For review items: find the page in the same source where the claim is supported (any page).
Categories: supported-on-cited, found-on-other-page (page error), not-found (not in supplied text)."""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import textbook_check as tc
import textbook_audit as ta
R = "/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries/sources/textbook_audit.json"
KEYS = ("ANDR", "BERM", "HARTY", "COHEN", "INGLE", "TROPE10", "KOHLI", "OGLE", "HEXEM1", "HEXEM2")

def all_pages(key):
    pages, off = tc.load(key)
    return pages, off  # keys are extract page numbers; cited = extract + off

def locate(rec):
    key = rec["source"]
    pages, off = all_pages(key)
    s_all = []
    for ext_page in sorted(pages):
        txt = tc.norm(pages[ext_page])
        if not txt:
            continue
        s, miss, mn = tc.score(rec["sentence"], txt)
        s_all.append((s, ext_page, mn))
    if not s_all:
        return ("no-source-text", None, 0.0)
    s_all.sort(reverse=True)
    best_s, best_ext, best_mn = s_all[0]
    cited = [a for a, b in rec["pages"]]
    cited_ext = [c - off for c in cited]
    if best_s >= 0.6 and not best_mn:
        if any(abs(best_ext - c) <= 1 for c in cited_ext):
            return ("supported-on-cited", best_ext + off, best_s)
        return ("found-on-other-page", best_ext + off, best_s)
    return ("not-found", best_ext + off, best_s)

if __name__ == "__main__":
    recs = json.load(open(R, encoding="utf-8"))
    summary = {}
    for i, r in enumerate(recs):
        if r["status"] != "review" or r["source"] not in KEYS:
            continue
        cat, pg, s = locate(r)
        r["locate"] = {"cat": cat, "page": pg, "score": round(s, 2)}
        summary[cat] = summary.get(cat, 0) + 1
    json.dump(recs, open(R, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(summary)
