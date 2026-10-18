"""Check textbook and DCNA citations in the answer files against the local text extracts.

Each source resolves a cited page number to the extract text for that page:
  ANDR    Andreasen 2007 chapterwise (printed-page header lines, page = printed)
  BERM    Berman, Clinical Guide to Dental Traumatology (PDF page = printed)
  HARTY   Harty's Ch.12 (printed-page header lines, page = printed)
  COHEN   Cohen's Ch.21 (<!-- PDF page N --> markers, page = printed)
  INGLE   Ingle's Ch.12 (cited page = PDF page; printed = PDF + 39)
  KOHLI   Kohli and Lee (DCNA; journal page = PDF + 608)
  OGLE    Ogle 2024 (DCNA; journal page = PDF + 150)
  HEXEM1  Hexem and Eisler Part 1 (journal page = PDF + 585, to confirm)
  TROPE10 Trope 2010 (DCNA; journal page = PDF + 312)

Score: content words of the citing sentence found on the cited page(s), and any
numbers in the sentence that are missing from the page. Quoted phrases in SOURCE
LOCATORS lines are checked exactly.
"""
import glob
import json
import os
import re

BASE = "/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries"
SRC = os.path.join(BASE, "sources")
TB = "/Users/niranjan/mds-textbooks"

STOP = set("""the and for with that this from were been have has are was which their there these those into
about after before when than then also such more most only other some each over under within without
between while where who whom what whose they them will would could should may might must can not but
its it his her our your its are is of in on at by as to an or be being if so no yes via per""".split())


def norm(s):
    s = s.replace("­", "").replace("’", "'").replace("–", "-").replace("—", "-")
    s = re.sub(r"-\s*\n\s*", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.lower()


def split_markers(text, regex, grab):
    """Return {page: text} where text runs from a marker to the next marker."""
    pages = {}
    ms = list(re.finditer(regex, text, re.M))
    valid, last = [], None
    for i, m in enumerate(ms):
        n = grab(m)
        if n is None:
            continue
        # accept only markers that run in sequence (table cells and figure labels are rejected)
        if last is None or last < n <= last + 5:
            valid.append((i, m, n))
            last = n
    if valid:
        # text before the first marker belongs to the first page (chapter opening)
        first_i, first_m, first_n = valid[0]
        pages[first_n] = text[:first_m.start()]
    for k, (i, m, n) in enumerate(valid):
        end = valid[k + 1][1].start() if k + 1 < len(valid) else len(text)
        pages[n] = pages.get(n, "") + text[m.end():end]
    return pages


_cache = {}


def load(key):
    if key in _cache:
        return _cache[key]
    if key == "ANDR":
        d = os.path.join(TB, "Textbook_and_Color_Atlas_of_Traumatic_Chapterwise")
        pages = {}
        for f in sorted(glob.glob(os.path.join(d, "*.md"))):
            t = open(f, encoding="utf-8", errors="replace").read()
            for k, v in split_markers(t, r"^(\d{3})\s*$", lambda m: int(m.group(1)) if 200 <= int(m.group(1)) <= 900 else None).items():
                pages[k] = pages.get(k, "") + v
        pages = {k: v for k, v in pages.items()}
        off = 16  # answers cite PDF page = printed + 16 (verified on T15/T16 locators)
    elif key == "HARTY":
        pages = {}
        for f in sorted(glob.glob(os.path.join(TB, "Harty_s_Endodontics_in_Clinical_Practice_7th_ed_Chapterwise", "*_*.md"))):
            if os.path.basename(f).startswith(("00_", "16_")):
                continue
            t = open(f, encoding="utf-8", errors="replace").read()
            for k, v in split_markers(t, r"^(\d{2,3})\s*$", lambda m: int(m.group(1)) if 1 <= int(m.group(1)) <= 700 else None).items():
                pages[k] = pages.get(k, "") + v
        off = 16  # cited page = printed page + 16 (verified on ch12 and ch10 anchors)
    elif key == "COHEN":
        pages = {}
        for f in sorted(glob.glob(os.path.join(TB, "Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise", "*.md"))):
            t = open(f, encoding="utf-8", errors="replace").read()
            for k, v in split_markers(t, r"<!-- PDF page (\d+) -->", lambda m: int(m.group(1))).items():
                pages[k] = pages.get(k, "") + v
        off = 0
    elif key == "INGLE":
        pages = {}
        for f in sorted(glob.glob(os.path.join(TB, "Ingles_Endodontics_7th_Chapterwise", "*_*.md"))):
            if os.path.basename(f).startswith("00_"):
                continue
            t = open(f, encoding="utf-8", errors="replace").read()
            for k, v in split_markers(t, r"^(\d{3}) The Practice of Endodontics|^The Practice of Endodontics (\d{3})",
                                      lambda m: int(m.group(1) or m.group(2))).items():
                pages[k] = pages.get(k, "") + v
        off = -39  # cited page is the PDF page; extract marker (printed) = PDF + 39
    elif key == "BERM":
        t = open(os.path.join(SRC, "berman_guide.txt"), encoding="utf-8").read()
        pages = split_markers(t, r"===== PDF PAGE (\d+) =====", lambda m: int(m.group(1)))
        off = 0
    elif key in ("KOHLI", "OGLE", "HEXEM1", "HEXEM2", "TROPE10"):
        fn = {"KOHLI": "dcna_S0011853226000212.txt", "OGLE": "dcna_S0011853223001234.txt",
              "HEXEM1": "dcna_S0011853226000121.txt", "HEXEM2": "dcna_S0011853226000133.txt",
              "TROPE10": "dcna_trope2009.txt"}[key]
        t = open(os.path.join(SRC, fn), encoding="utf-8").read()
        pages = split_markers(t, r"===== PDF PAGE (\d+) =====", lambda m: int(m.group(1)))
        off = {"KOHLI": 608, "OGLE": 150, "HEXEM1": 585, "HEXEM2": 600, "TROPE10": 312}[key]
    else:
        raise KeyError(key)
    _cache[key] = (pages, off)
    return _cache[key]


def page_text(key, cited):
    """Normalised text for the page the answer cites (PDF or journal page, as the answer uses it)."""
    pages, off = load(key)
    return norm(pages.get(cited - off, ""))


def words(s):
    out = set()
    for w in re.findall(r"[a-z][a-z\-]{3,}|\d+(?:\.\d+)?%?", s.lower()):
        if w not in STOP:
            out.add(w)
    return out


NUMWORDS = {"two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "ten": "10", "one": "1"}


def score(sentence, text):
    ws = words(re.sub(r"\([^)]*\)|\[[^\]]*\]", " ", sentence))
    if not ws:
        return 1.0, [], []
    hit = [w for w in ws if w in text or (w in NUMWORDS and NUMWORDS[w] in text)
           or (len(w) >= 6 and not re.match(r"\d", w) and w[:6] in text)]
    miss = [w for w in ws if w not in hit]
    nums = [w.rstrip("%") for w in ws if re.match(r"\d", w) and not re.fullmatch(r"(19|20)\d\d", w)]
    miss_nums = [w for w in nums if not re.search(r"(?<![\d.])" + re.escape(w) + r"(?![\d])", text)]
    return len(hit) / len(ws), miss, miss_nums


if __name__ == "__main__":
    import sys
    for key in sys.argv[1:]:
        p, off = load(key)
        print(key, "pages:", len(p), "range:", min(p) if p else None, "-", max(p) if p else None, "offset:", off)
