"""Find phrases in the supplied guideline and review text and report the PDF page.

Usage: python3 verify_iadt.py "fouad::30 minutes" "bourg::0.4 mm"
Each argument is key::phrase. The key is a substring of the .txt file name in
sources/guidelines/. Matching ignores case, soft hyphens, line breaks and
hyphenation at line ends. Reports up to three hits per phrase.
"""
import glob
import os
import re
import sys

GUIDE = "/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries/sources/guidelines"
MARK = re.compile(r"===== PDF PAGE (\d+) =====")

KEYS = {
    "fouad": "Dental_Traumatology_-_2020_-_Fouad",
    "bourg": "Dental_Traumatology_-_2020_-_Bourguignon",
    "khan": "Dental_Traumatology_-_2020_-_Khandelwal",
    "saikia": "Dental_Traumatology_-_2023_-_Saikia",
    "krastl": "Int_Endodontic_J_-_2021_-_Krastl",
    "crowder": "Int_J_Paed_Dentistry_-_2024_-_Crowder",
    "kumari": "effect-of-splinting",
    "blackledge": "jcm-14-01986",
    "huang": "s41368",
    "abreu": "CRsJdZQnpWNmcXRy6VkdFXc",
    "andr2002": "Dental_Traumatology_-_2002_-_Andreasen",
}


def norm(s):
    s = s.replace("­", "")
    s = re.sub(r"-\s*\n\s*", "", s)
    s = re.sub(r"\s+", " ", s)
    return s


def load(key):
    fname = KEYS[key]
    hits = glob.glob(os.path.join(GUIDE, "*" + fname + "*"))
    assert len(hits) == 1, (key, hits)
    txt = open(hits[0], encoding="utf-8", errors="replace").read()
    parts = MARK.split(txt)
    pages = []
    for i in range(1, len(parts), 2):
        pages.append((int(parts[i]), norm(parts[i + 1])))
    return pages


def check(arg):
    key, phrase = arg.split("::", 1)
    pages = load(key)
    pat = re.compile(re.escape(norm(phrase)), re.I)
    found = []
    for pno, body in pages:
        for m in pat.finditer(body):
            a = max(0, m.start() - 90)
            b = min(len(body), m.end() + 90)
            found.append((pno, body[a:b]))
    print("## %s :: %s  -> %d hit(s)" % (key, phrase, len(found)))
    for pno, snip in found[:3]:
        print("   PDF p.%d: ...%s..." % (pno, snip))


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        check(arg)
