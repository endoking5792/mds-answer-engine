"""Record manual verdicts for review items. Keys are positions in sources/verdict_order.json."""
import json, sys
ORDER = "/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries/sources/verdict_order.json"
VER = "/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries/sources/verdicts.json"
R = "/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries/sources/textbook_audit.json"
def record(pairs):
    order = json.load(open(ORDER))
    try:
        ver = json.load(open(VER))
    except FileNotFoundError:
        ver = {}
    recs = json.load(open(R, encoding="utf-8"))
    for k, code, note in pairs:
        i = order[k]
        ver[str(i)] = {"k": k, "file": recs[i]["file"], "line": recs[i]["line"], "source": recs[i]["source"],
                       "cited": recs[i]["pages"], "code": code, "note": note}
    json.dump(ver, open(VER, "w"), ensure_ascii=False, indent=1)
    print("recorded", len(pairs), "total", len(ver))
if __name__ == "__main__":
    record(json.loads(sys.argv[1]))
