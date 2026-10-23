"""Audit textbook and DCNA citations in the answer files against the local extracts.

For every bracketed citation group (parentheses or square brackets), each sub-citation with an
author label and a page is resolved to its source page (see textbook_check.py for offsets).
The citing sentence is scored against the cited page(s). Quoted phrases in the same line are
checked against the cited pages. Results go to sources/textbook_audit.json; a summary is printed.
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
import textbook_check as tc  # noqa: E402

BASE = "/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries"
os.chdir(BASE)

LABELS = [
    (r"Bourguignon|Fouad|Khandelwal|Krastl|Saikia|Crowder|Kumari|Blackledge|Huang|Abreu", "SUPPLIED"),
    (r"Andreasen et al,? 2002", "SKIP_2002"),
    (r"Andreasen et al,? 2007|Andreasen et al", "ANDR"),
    (r"Berman et al|Berman's|Berman", "BERM"),
    (r"Sigurdsson and Bourguignon|Harty['’]s", "HARTY"),
    (r"Kahler|Cohen['’]s", "COHEN"),
    (r"Trope,? 2010", "TROPE10"),
    (r"Trope,? n\.d\.", "INGLE"),
    (r"Kohli and Lee", "KOHLI"),
    (r"Hexem and Eisler", "HEXEM"),
    (r"Ogle", "OGLE"),
    (r"Sikri", "SIKRI"),
    (r"Grossman", "GROSSMAN"),
    (r"Weine", "WEINE"),
    (r"Paranjpe", "PARANJPE"),
    (r"Endodontic Radiology", "RADIOLOGY"),
    (r"AAE", "AAE"),
]
PAGE_RE = re.compile(r"p\.\s?(\d{2,4})(?:\s?[-–]\s?(\d{2,4}))?")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\[(])")
STOP_QUOTE = {"the", "a", "an"}


def label_of(seg):
    for pat, key in LABELS:
        if re.search(pat, seg):
            return key
    return None


def group_spans(line):
    """Yield (start, end, text) for each (...) or [...] group that contains a page reference."""
    for m in re.finditer(r"\(([^()]*)\)|\[([^\[\]]*)\]", line):
        body = m.group(1) if m.group(1) is not None else m.group(2)
        if PAGE_RE.search(body):
            yield m.start(), m.end(), body


def sentence_at(line, pos):
    parts = SENT_SPLIT.split(line)
    off = 0
    for p in parts:
        i = line.find(p, off)
        end = i + len(p)
        if i <= pos < end:
            return p
        off = end
    return line


def resolve(key, pages):
    """Return normalised text across the cited pages, or None if the source is not resolvable."""
    if key not in ("ANDR", "BERM", "HARTY", "COHEN", "INGLE", "TROPE10", "KOHLI", "OGLE", "HEXEM1", "HEXEM2"):
        return None
    txt = ""
    for a, b in pages:
        last = b if b else a
        for n in range(a, last + 1):
            txt += " " + tc.page_text(key, n)
    return txt


def audit_file(path):
    res = []
    lines = open(path, encoding="utf-8").read().split("\n")
    for ln, line in enumerate(lines, 1):
        if "AUDIT NOTE" in line or line.startswith("**Added sources"):
            continue
        groups = list(group_spans(line))
        if not groups:
            continue
        for gs, ge, body in groups:
            subs = [s.strip() for s in body.split(";")]
            carry = None
            for sub in subs:
                key = label_of(sub)
                if key is None and not re.search(r"\b(19|20)\d\d\b", sub):
                    key = carry  # bare page reference inherits the previous author
                else:
                    carry = key
                pages = [(int(a), int(b) if b else None) for a, b in PAGE_RE.findall(sub)]
                if key is None or not pages:
                    continue
                sent = sentence_at(line, gs)
                if key == "HEXEM":
                    part = "2" if re.search(r"Part 2|Part Two", sub) else "1"
                    key = "HEXEM1" if part == "1" else "HEXEM2"
                rec = {"file": os.path.basename(path)[:3], "line": ln, "cite": sub, "source": key,
                       "pages": pages, "sentence": sent[:400]}
                if key in ("SKIP_2002", "SUPPLIED"):
                    rec["status"] = "skipped (supplied PDF checked separately)"
                    res.append(rec)
                    continue
                txt = resolve(key, pages)
                if txt is None:
                    rec["status"] = "pending source extract"
                    res.append(rec)
                    continue
                s, miss, miss_nums = tc.score(sent, txt)
                rec["score"] = round(s, 2)
                rec["missing_words"] = miss[:12]
                rec["missing_numbers"] = miss_nums
                rec["status"] = "ok" if (s >= 0.6 and not miss_nums) else "review"
                if rec["status"] == "review" and len(pages) == 1:
                    a0 = pages[0][0]
                    # Andreasen and Harty's printed-page offset can drift by one page: accept +/-1
                    # for those two sources and report it; for other sources report the adjacent page.
                    for d in (-1, 1):
                        s2, _, mn2 = tc.score(sent, resolve(key, [(a0 + d, None)]) or "")
                        if s2 >= 0.6 and not mn2:
                            if key in ("ANDR", "HARTY"):
                                rec["status"] = "ok (page %+d)" % d
                            else:
                                rec["status"] = "review: adjacent page %d" % (a0 + d)
                            rec["adjacent"] = a0 + d
                            break
                res.append(rec)
        # quoted phrases in the same line, checked against each cited page of the line
        quotes = re.findall(r"[\"“]([^\"”]{12,160})[\"”]", line)
        if quotes:
            line_pages = []
            for _, _, body in groups:
                for sub in body.split(";"):
                    key = label_of(sub)
                    pg = [(int(a), int(b) if b else None) for a, b in PAGE_RE.findall(sub)]
                    if key and pg:
                        line_pages.append((key, pg))
            for q in quotes:
                qn = tc.norm(q).strip(" .,;")
                if len(qn.split()) < 3:
                    continue
                hit = None
                for key, pg in line_pages:
                    txt = resolve(key, pg)
                    if txt is None:
                        continue
                    if qn in txt:
                        hit = (key, True)
                        break
                if hit is None and line_pages:
                    kk = [k for k, _ in line_pages if resolve(k, [(1, None)]) is not None]
                    if kk:
                        res.append({"file": os.path.basename(path)[:3], "line": ln, "cite": "quote",
                                    "source": ",".join(sorted(set(k for k, _ in line_pages))),
                                    "pages": [p for _, pg in line_pages for p in pg],
                                    "sentence": q[:200], "status": "quote not found on cited page"})
    return res


def main():
    out = []
    for f in sorted(glob.glob("T*.md") + glob.glob("P*.md")):
        out.extend(audit_file(f))
    json.dump(out, open("sources/textbook_audit.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    from collections import Counter
    st = Counter(r["status"] for r in out)
    print("records:", len(out))
    for k, v in st.most_common():
        print(f"  {k}: {v}")
    bysrc = Counter((r["source"], r["status"]) for r in out)
    for (s, st_), v in sorted(bysrc.items()):
        print(f"    {s:10} {st_:40} {v}")


if __name__ == "__main__":
    main()
