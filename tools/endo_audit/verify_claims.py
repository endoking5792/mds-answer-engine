#!/usr/bin/env python3
"""Claim verifier for answer audits.
Usage: python3 -I verify_claims.py claims_sealers.json   (or claims_obturation.json)
Set TEXTBOOKS to a local clone of the private repo endoking5792/mds-textbooks.
Each claim = {id, ans, src, re, claim}; src keys map to chapter files below.
A hit means the regex is present in the cited chapter. It does NOT prove the answer reads the sentence correctly.
"""
import re, sys, json, os
R = os.environ.get("TEXTBOOKS", "./mds-textbooks") + "/"
F = {
 "C": "Cohen_s_Pathways_of_the_Pulp_12th_edi_Louis_H_Berman_Chapterwise/09_9_Obturation_of_the_cleaned_and_shaped_root_canal_system.md",
 "G": "Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/16_Chapter_16_Obturation_of_the_Radicular_Space.md",
 "G15": "Grossman_s_Endodontic_Practice_14th_ed_1_Chapterwise/15_Chapter_15_Irrigants_and_Intracanal_Medicaments.md",
 "I": "Ingles_Endodontics_7th_Chapterwise/22_Chapter_22_Obturation_of_the_Radicular_Spaces.md",
 "S": "Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/19_19_Root_Canal_Sealers.md",
 "S20": "Vimal_K_Sikri_Essentials_of_Endodontics_2nd_Ed_Chapterwise/20_20_Obturation_of_Root_Canal_Spaces.md",
 "J": "Current_Therapy_in_Endodontics_Chapterwise/05_6_pdf_p_137_166.md",
 "T": "Treatment_of_Endodontic_Infections_Chapterwise/15_Chapter_15_Root_canal_obturation.md",
 "H": "Harty_s_Endodontics_in_Clinical_Practice_7th_ed_Chapterwise/09_9_Root_Canal_Filling.md",
 "CC": "Common_Complications_in_Endodontics_Chapterwise/06_6_Complications_Due_to_Root_Canal_Filling_Procedures.md",
 "EP": "Endodontic_Prognosis_Clinical_Guide_Chapterwise/09_9_Obturation_of_Root_Canals.md",
 "PS": "Problem_Solving_in_Endodontics_James_L_Gutmann_Chapterwise/12_Chapter_12_Problem_Solving_Challenges_in_Root_Canal_Obturati.md",
 "W": "Weines_Endodontics_Full_Chapterwise/07_CHAPTER_7_Canal_Filling_with_Semisolid_Materials.md",
 "PP": "Principles_and_practice_of_endodontic_2002_compressed_Chapterwise/14_Part_14_Obturation.md",
 "PP15": "Principles_and_practice_of_endodontic_2002_compressed_Chapterwise/15_Part_15_Preparation_for_Restoration_and_Temporization.md",
 "PP19": "Principles_and_practice_of_endodontic_2002_compressed_Chapterwise/19_Part_19_Evaluation_of_Success_and_Failure.md",
 "TP": "Endodontics_Principles_and_Practice_Chapterwise/15_15_Obturation_and_Temporization.md",
 "B12": "Bioceramics_in_Endodontics_Chapterwise/08_Pages_241_270.md",
 "BC": "Bioceramics_in_Endodontics_Chapterwise/04_Pages_121_150.md",
 "AD": "Operative_and_Dental_Materials_Textbooks/A_Clinical_Guide_to_Applied_Dental_Materials.md",
}
# NOTE: in claims_sealers.json "S" = Sikri Ch.19 (sealers); in claims_obturation.json "S" = Sikri Ch.20 (obturation).
if "obturation" in sys.argv[1]:
    F["S"] = F["S20"]
cache = {}
def txt(k):
    if k not in cache:
        cache[k] = re.sub(r"[\s\u00ad\u2010-\u2015]+", " ", open(R + F[k], errors="ignore").read())
    return cache[k]
claims = json.load(open(sys.argv[1]))
ok = 0
for c in claims:
    try:
        hit = bool(re.search(c["re"], txt(c["src"]), re.I))
    except (FileNotFoundError, KeyError):
        hit = False
    ok += hit
    print("OK  " if hit else "MISS", c["id"], c["ans"], c["src"], "|", c["claim"])
print(ok, "/", len(claims))
