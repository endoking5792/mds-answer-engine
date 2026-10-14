#!/usr/bin/env python3
"""Resolve evidence IDs in a question draft into author-year in-text citations
plus a REFERENCES list and a SOURCE LOCATORS list; report Exam-Mode word count and
Study/Exam overlap.

Usage: assemble.py draft.md out.md

Draft tokens: [SRC:A57] [SRC:A57,B462] [LIT:Ge2023]   (adjacent tokens are merged: (Mount et al, 2016; Bhat et al, 2019))
Sections: '## STUDY MODE', '## EXAM MODE' ...; the draft must contain '<<<SOURCE LIST>>>'.
"""
import re, sys, json
T = "/Users/niranjan/.claude/answer_tools"
sys.path.insert(0, T)
import dossier as D

LIT = json.load(open(f"{T}/lit_registry.json"))
META = json.load(open(f"{T}/refs_meta.json"))   # BOOKS and DCNA files -> {"cite": "...", "ref": "..."}
CACHE = {}


def get_entry(sid):
    m = re.match(r"^(C1|C2|A|B|D|E|G)(\d+)$", sid)
    if not m:
        raise SystemExit(f"bad SRC id {sid}")
    k, n = m.group(1), int(m.group(2))
    if k not in CACHE:
        CACHE[k] = D.parse(k)
    e = CACHE[k].get(n)
    if not e:
        raise SystemExit(f"SRC id {sid} not found in dossier {k}")
    return k, e


def meta_key(k, e):
    if k == "A":
        return "Atlas" if e["file"].startswith("Chapter_0") else "MountHume"
    if k == "E":
        f = e["file"]
        if f.startswith("1-s2.0-"):
            return f
        # user study note: cite the underlying reference it quotes
        m = re.search(r'refers to:\s*"?([A-Z][A-Za-z\'-]+)', e["raw"])
        sur = m.group(1) if m else ""
        guess = {"Sakaguchi": "Craig14", "Anusavice": "Phillips12", "Mount": "Atlas", "Bonsor": "Bonsor",
                 "Roberson": "Sturdevant", "Banerjee": "PickardManual", "Sikri": "Sikri", "van": "vanNoort",
                 "Powers": "Powers", "McCabe": "McCabe"}.get(sur)
        if guess is None:
            raise SystemExit(f"E note {e['file']} quotes unknown reference starting '{sur}'; add mapping")
        return guess
    return e["book"]


def cite_for(sid):
    k, e = get_entry(sid)
    mk = meta_key(k, e)
    if mk not in META:
        raise SystemExit(f"refs_meta.json missing key '{mk}' (needed by {sid}, file {e['file']})")
    c = META[mk]["cite"]
    via = k == "E" and not e["file"].startswith("1-s2.0-")
    return mk, c, via, e


def lit_cite(key):
    raw = LIT[key]["cite"].split(",")
    head = ",".join(raw[:2]).replace("et al.", "et al").replace("&", "and").strip()
    return head


def build(text):
    seen = {}
    order = []

    def tok(m):
        kind = m.group(1)
        ids = [x.strip() for x in m.group(2).split(",")]
        out = []
        for i in ids:
            if kind == "LIT":
                if i not in LIT:
                    raise SystemExit(f"LIT key {i} not in registry")
                out.append("«" + lit_cite(i) + "»")
                if ("LIT", i) not in seen:
                    seen[("LIT", i)] = 1; order.append(("LIT", i))
            else:
                mk, c, via, e = cite_for(i)
                out.append("«" + c + ("*" if via else "") + "»")
                if ("SRC", i) not in seen:
                    seen[("SRC", i)] = 1; order.append(("SRC", i))
        return " ".join(out)

    t = re.sub(r"\[(SRC|LIT):([A-Za-z0-9_,\s]+)\]", tok, text)

    def merge(m):
        items = re.findall("«(.*?)»", m.group(0))
        uniq = []
        for x in items:
            if x not in uniq:
                uniq.append(x)
        return "(" + "; ".join(uniq) + ")" + (" " if m.group(0).endswith(" ") else "")

    t = re.sub("(?:«[^«»]*»[ \t]*)+", merge, t)
    return t, order


def make_lists(order):
    refs = {}
    loc = []
    for kind, ident in order:
        if kind == "LIT":
            L = LIT[ident]
            refs[lit_cite(ident)] = f'{L["cite"]}. {L["type"]}. {L["url"]}'
            continue
        mk, c, via, e = cite_for(ident)
        refs[c] = META[mk]["ref"]
        pg = e["page"] or "n/a"
        f = e["file"]
        extra = ""
        if via:
            extra = ' (quoted in a user study note)'
            f = "study note: " + f
        loc.append(f'- ({c}{"*" if via else ""}) {f} | PDF p.{pg} | "{e["anchor"]}"{extra}')
    ref_lines = [f"- {refs[k]}" for k in sorted(refs, key=lambda s: s.lower())]
    return ref_lines, loc


CITE_RE = re.compile(r"\([A-Z][^()]*?\b(?:(?:19|20)\d{2}[a-z]?|undated)\*?(?:; [^()]*?\b(?:(?:19|20)\d{2}[a-z]?|undated)\*?)*\)")
TAGW = re.compile(r"\[(?:RECALL|Certain|Likely|Guessing)\]")


def words(s):
    s = CITE_RE.sub(" ", s)
    s = TAGW.sub(" ", s)
    s = re.sub(r"[#>*|`_-]+", " ", s)
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9'’.%/+-]*", s)


def section(text, name):
    m = re.search(rf"^## {name}[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1) if m else ""


def shingles(w, n=6):
    w = [x.lower() for x in w]
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def main(src, dst):
    text = open(src, encoding="utf-8").read()
    out, order = build(text)
    ref_lines, loc_lines = make_lists(order)
    block = ("**References (author-year, as cited in the text above).** An asterisk (*) means the fact was found in your own study notes, which quote that reference.\n\n"
             + "\n".join(ref_lines)
             + "\n\n**Source locators (file, PDF page marker, verbatim phrase)** for each retrieved fact:\n\n" + "\n".join(loc_lines))
    out = out.replace("<<<SOURCE LIST>>>", block)
    open(dst, "w", encoding="utf-8").write(out)
    study = words(section(out, "STUDY MODE"))
    exam = words(section(out, "EXAM MODE"))
    ov = len(shingles(study) & shingles(exam)) / max(1, len(shingles(exam)))
    print(f"Study words: {len(study)} | Exam words: {len(exam)} | 6-gram overlap Exam->Study: {ov:.1%} | cited facts: {len(order)} | distinct references: {len(ref_lines)}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
