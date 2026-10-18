"""Follow-up patch to audit_apply2.py: P-file source blocks, status lines and stale disclaimers.

Run once, after audit_apply2.py. Each replacement must match exactly once; mismatches are listed.
"""
import os
import re

BASE = "/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries"
os.chdir(BASE)

FAILS = []
DONE = []


def read(p):
    return open(p, encoding="utf-8").read()


def write(p, t):
    open(p, "w", encoding="utf-8").write(t)


def swap(path, old, new):
    t = read(path)
    n = t.count(old)
    if n != 1:
        FAILS.append((path, n, old[:60]))
        return
    write(path, t.replace(old, new))
    DONE.append((path[:3], old[:40]))


def swap_regex(path, pattern, new):
    t = read(path)
    m = re.search(pattern, t, re.S)
    if not m:
        FAILS.append((path, "regex", pattern[:60]))
        return
    write(path, t[:m.start()] + new + t[m.end():])
    DONE.append((path[:3], "regex"))


def append_block(path, text):
    t = read(path).rstrip("\n")
    write(path, t + "\n\n" + text.strip() + "\n")
    DONE.append((path[:3], "append block"))


# ---------------------------------------------------------------- P1 - P3 source blocks
P1 = "P1_Pulp_Options_for_Complicated_Crown_Fracture_in_an_Adult_10m_PREDICTED.md"
P2 = "P2_Traumatised_Immature_Incisor_with_Necrotic_Pulp_10m_PREDICTED.md"
P3 = "P3_Replacement_Resorption_Ankylosis_in_a_Growing_Patient_10m_PREDICTED.md"

swap(P1, "Drafted from the topic's high-yield content. Remove if the examiner's paper does not use it.",
     "Drafted from the topic's high-yield content, checked against IADT 2020 on 2026-10-19 (see audit note). Remove if the examiner's paper does not use it.")
swap(P2, "**Status:** PREDICTED question, not from a repository sitting.",
     "**Status:** PREDICTED question, not from a repository sitting. Checked against IADT 2020 on 2026-10-19 (see audit note).")
swap(P3, "**Status:** PREDICTED question, not from a repository sitting.",
     "**Status:** PREDICTED question, not from a repository sitting. Checked against IADT 2020 on 2026-10-19 (see audit note).")

append_block(P1, """
**Audit note (IADT 2020, checked 2026-10-19).** The exam section now carries the IADT preference for partial pulpotomy or pulp capping in complicated crown fractures, including teeth with completed roots (Bourguignon et al, 2020, PDF p.7, printed p.320). The IADT separately recommends pulp removal in mature crown-root fractures (PDF p.9, printed p.322), so the answer distinguishes the fracture types. The Krastl et al (2022) success figures (90-100% immature, 70-100% mature) are observational and are labelled as such (PDF p.5).

**Added sources (IADT audit).**
- Bourguignon C, et al. International Association of Dental Traumatology guidelines for the management of traumatic dental injuries: 1. Fractures and luxations of permanent teeth. Dent Traumatol. 2020;36:314-330. doi:10.1111/edt.12578.
- Krastl G, et al. Present status and future directions: endodontic management of traumatic injuries to permanent teeth. Int Endod J. 2022;55(Suppl 4):1003-1019. doi:10.1111/iej.13672.
- Bourguignon et al, 2020 (uploaded PDF; printed = PDF + 313): PDF p.7 (p.320) 'Conservative pulp treatment (eg, partial pulpotomy) is also the preferred treatment in teeth with completed root development'; PDF p.9 (p.322) 'In mature teeth with complete root formation, removal of the pulp is usually indicated'.
- Krastl et al, 2022 (uploaded PDF; printed = PDF + 1002): PDF p.5 (p.1007) immature 90%-100%, mature 70%-100% with partial pulpotomy.
""")

append_block(P2, """
**Audit note (IADT 2020; Krastl et al, 2022, checked 2026-10-19).** The IADT positions are added: calcium hydroxide intracanal for up to one month (Fouad et al, 2020, PDF p.7, printed p.337); endodontic treatment not started without definite signs of necrosis and infection (PDF p.5, printed p.335); pulp revascularisation as the aim for immature teeth, with apexification, pulp revitalisation or root canal treatment if it fails (PDF p.5). The apical-barrier healing range of 81-96% comes from Krastl et al (2022, PDF p.8). The Harty's and Kohli and Lee points are textbook.

**Added sources (IADT audit).**
- Fouad AF, et al. International Association of Dental Traumatology guidelines for the management of traumatic dental injuries: 2. Avulsion of permanent teeth. Dent Traumatol. 2020;36:331-342. doi:10.1111/edt.12573.
- Krastl G, et al. Present status and future directions: endodontic management of traumatic injuries to permanent teeth. Int Endod J. 2022;55(Suppl 4):1003-1019. doi:10.1111/iej.13672.
- Fouad et al, 2020 (uploaded PDF; printed = PDF + 330): PDF p.5 (p.335) 'endodontic treatment should not be initiated unless there are definite signs'; PDF p.7 (p.337) 'Calcium hydroxide is recommended as an intracanal medicament for up to 1 month'.
- Krastl et al, 2022 (PDF p.8, printed p.1010): 'periapical healing ranging between 81% and 96%'.
""")

append_block(P3, """
**Audit note (IADT 2020; Crowder et al, 2024, checked 2026-10-19).** The IADT advises that parents be told decoronation or autotransplantation may be needed later if a replanted tooth ankyloses (Fouad et al, 2020, PDF p.5-6, printed p.335-336). Crowder et al (2024) describe decoronation and root submergence in 37 teeth, mostly case reports, with limited evidence (PDF p.1). The textbook statement that no treatment exists for established replacement resorption is Harty's (textbook point), and the IADT does not give a treatment for it.

**Added sources (IADT audit).**
- Fouad AF, et al. International Association of Dental Traumatology guidelines for the management of traumatic dental injuries: 2. Avulsion of permanent teeth. Dent Traumatol. 2020;36:331-342. doi:10.1111/edt.12573.
- Crowder S, et al. Endodontic management of submerged roots following complicated traumatic dental injuries. Int J Paediatr Dent. 2024;34:608-620. doi:10.1111/ipd.13161.
- Fouad et al, 2020 (uploaded PDF; printed = PDF + 330): PDF p.5-6 (p.335-336) 'decoronation or other procedures such as autotransplantation might be necessary'.
- Crowder et al, 2024 (PDF p.1, printed p.608): '37 teeth were treated with decoronation'; 'limited evidence'.
""")

# ---------------------------------------------------------------- stale disclaimers
swap("T01_Traumatic_Injuries_to_Teeth_and_Related_Tissues_100m.md",
     "(1) The IADT guideline itself was not retrieved; IADT positions are as reported by DCNA reviews.",
     "(1) The IADT 2020 guidelines were read from the supplied PDFs on 2026-10-19; their statements are checked in the audit notes.")
swap("T04_Luxation_Injuries_in_the_Permanent_Dentition_50m.md",
     "IADT guideline text was not retrieved. The IADT splint durations below are as reported in a 2024 DCNA review (Ogle, 2024).",
     "The IADT 2020 guidelines were read from the supplied PDFs on 2026-10-19 (see audit note); the splint durations below are the IADT figures checked against Bourguignon et al (2020).")
swap("T04_Luxation_Injuries_in_the_Permanent_Dentition_50m.md",
     "the IADT guideline is not read directly.",
     "the IADT 2020 guidelines were read from the supplied PDFs on 2026-10-19 (see audit note).")
swap("T10_Fragment_Reattachment_10m.md",
     "the systematic review itself was not read.",
     "the Khandelwal et al (2021) review was read from the supplied PDF on 2026-10-19.")
swap("T14_Avulsion_Media_used_in_Endodontics_20m.md",
     "Textbook-only; the IADT guideline could not be retrieved (see Note on Sources).",
     "The IADT 2020 guidelines were read from the supplied PDFs on 2026-10-19.")
swap("T14_Avulsion_Media_used_in_Endodontics_20m.md",
     "- Web: no IADT guideline text retrieved.",
     "- Supplied PDFs: IADT 2020 avulsion guideline read on 2026-10-19 (see audit note).")
swap_regex("T14_Avulsion_Media_used_in_Endodontics_20m.md",
           r"The IADT guideline was sought;.*?was not used\.",
           "The IADT 2020 guidelines were read from the supplied PDFs on 2026-10-19 (see audit note).")
swap("T13_Tooth_Avulsion_and_its_Management_10m.md",
     "IADT guideline not retrieved (see Note on Sources).",
     "IADT 2020 guideline read from the supplied PDF on 2026-10-19.")
swap("T13_Tooth_Avulsion_and_its_Management_10m.md",
     "- Web: IADT guideline URLs returned 404; no guideline text retrieved.",
     "- Supplied PDFs: IADT 2020 avulsion guideline read on 2026-10-19 (see audit note).")
swap("T15_Newer_Philosophies_of_Replantation_10m.md",
     "**Status:** DRAFTED, not audited. Textbook-only.",
     "**Status:** DRAFTED, audited against IADT 2020 on 2026-10-19 (see audit note).")
swap("T15_Newer_Philosophies_of_Replantation_10m.md",
     "**Note on Sources.** Textbook-only.",
     "**Note on Sources.** Textbook, plus IADT 2020 (Fouad et al) and Kumari et al (2025) for the splinting and fluoride checks.")
swap("T17_Intentional_Replantation_10m.md",
     "**Status:** DRAFTED, not audited. Textbook-only.",
     "**Status:** DRAFTED, audited against IADT 2020 on 2026-10-19 for IADT-relevant points (see audit note).")
swap("T17_Intentional_Replantation_10m.md",
     "**Note on Sources.** Textbook-only.",
     "**Note on Sources.** Textbook, plus IADT 2020 (Bourguignon et al) for the options list.")
swap("T18_Transplantation_Autotransplantation_10m.md",
     "**Status:** DRAFTED, not audited.",
     "**Status:** DRAFTED, audited against IADT 2020 on 2026-10-19 for IADT-relevant points (see audit note).")
swap("T20_Dens_Invaginatus_Classification_and_Management_10m.md",
     "**Status:** DRAFTED, not audited.",
     "**Status:** DRAFTED; IADT 2020 checked on 2026-10-19 and contains no dens invaginatus content (see audit note).")

print("DONE", len(DONE))
for d in DONE:
    print("  ok", d)
print("FAILS", len(FAILS))
for f in FAILS:
    print("  FAIL", f)
