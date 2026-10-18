"""Trim the IADT audit edits to Section 7 Exam Mode ranges and move audit notes out of the study sections.

Rules:
- Paragraphs whose original text was kept (appended audit sentences) are rebuilt from the
  pre-audit backup plus a shorter IADT sentence.
- Paragraphs fully rewritten by the audit are replaced with shorter versions.
- Audit notes (lines starting '**Audit note (') move to an end-of-file section, so they do not
  count toward Study or Exam word ranges.
Restore-safe: reads the backup for originals, writes the topic folder.
"""
import os
import re

BASE = "/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries"
BACKUP = "/private/tmp/claude-501/-Users-niranjan--claude-answer-tools/9d170050-fb44-4be4-b889-3ba26eb7210a/scratchpad/backup_topic"
os.chdir(BASE)

FAILS = []
DONE = []
CIT = re.compile(r"\(([^()]*?(?:\d{4}|n\.d\.)[^()]*?)\)")


def brackets(s):
    return CIT.sub(lambda m: "[" + m.group(1) + "]", s)


def read(p):
    return open(p, encoding="utf-8").read()


def write(p, t):
    open(p, "w", encoding="utf-8").write(t)


def span(t):
    return t.index("## EXAM MODE"), t.index("## HIGH-YIELD POINTS")


def orig_line(fname, label):
    t = read(os.path.join(BACKUP, fname))
    a, b = span(t)
    hits = [l for l in t[a:b].split("\n") if l.startswith("**" + label)]
    if len(hits) != 1:
        FAILS.append((fname, "orig", label, len(hits)))
        return None
    return hits[0].rstrip()


def set_line(fname, label, text):
    p = os.path.join(BASE, fname)
    t = read(p)
    a, b = span(t)
    lines = t[a:b].split("\n")
    hits = [i for i, l in enumerate(lines) if l.startswith("**" + label)]
    if len(hits) != 1:
        FAILS.append((fname, "set", label, len(hits)))
        return
    lines[hits[0]] = brackets(text.strip())
    write(p, t[:a] + "\n".join(lines) + t[b:])
    DONE.append((fname[:3], "set", label))


def reset_append(fname, label, extra):
    base = orig_line(fname, label)
    if base is None:
        return
    set_line(fname, label, base + " " + extra)


def move_notes(fname):
    p = os.path.join(BASE, fname)
    t = read(p)
    m = re.search(r"^\*\*Audit note \(.*$\n?", t, re.M)
    if not m:
        return
    note = m.group(0).strip()
    t = t[:m.start()] + t[m.end():]
    t = re.sub(r"\n{3,}", "\n\n", t)
    t = t.rstrip("\n") + "\n\n## AUDIT NOTE (IADT 2020, checked 2026-10-19)\n\n" + note + "\n"
    write(p, t)
    DONE.append((fname[:3], "moved note", ""))


# ------------------------------------------------------------------ T13 (exam 496 -> ~390)
T13 = "T13_Tooth_Avulsion_and_its_Management_10m.md"
set_line(T13, "Emergency phase.", """**Emergency phase.** Replant at once. If the tooth is dirty, rinse it gently in milk, saline or saliva, then replant it (Fouad et al, 2020, p.333). If replantation is delayed, use milk, HBSS, saliva or saline in that order; water is poor but better than drying (p.333).""")
set_line(T13, "Clinical phase.", """**Clinical phase.** Record the dry time and medium. After 30 minutes most PDL cells are non-viable; 60 minutes is the IADT management boundary (Fouad et al, 2020, p.333-334). Splint with a passive flexible wire of up to 0.4 mm, or nylon, for two weeks; use four weeks if the alveolus or jaw is fractured (p.334-335). Check tetanus status (p.334).""")
set_line(T13, "Endodontic phase.", """**Endodontic phase.** A closed apex needs root canal treatment within two weeks of replantation (Fouad et al, 2020, p.334). An open apex aims for revascularisation; treat only when necrosis and infection are confirmed (p.335). Calcium hydroxide may be used intracanal for up to one month (p.337). Amoxicillin or penicillin are the first antibiotic choices; tetracycline and doxycycline are generally not recommended under 12 years (p.336).""")
set_line(T13, "Follow-up.", """**Follow-up.** Review at 2 weeks (splint removal), 4 weeks, 3 and 6 months, one year, and yearly for at least five years (Fouad et al, 2020, p.337). An open apex is reviewed at 1, 2, 3 and 6 months as well (p.338).""")
set_line(T13, "Prognosis.", """**Prognosis.** Depends on dry time, medium and root stage. Delayed replantation has a poor long-term prognosis: the ligament becomes necrotic and replacement resorption is expected (Fouad et al, 2020, p.334).""")

# ------------------------------------------------------------------ T15 (exam 555 -> ~390)
T15 = "T15_Newer_Philosophies_of_Replantation_10m.md"
set_line(T15, "Delayed replantation.", """**Delayed replantation.** For a long-dry, contused socket, Andreasen et al heal the socket first, treat the root surface, then complete endodontic treatment (Andreasen et al, 2007, p.478). The IADT regards delayed replantation as having a poor long-term prognosis, with ankylosis expected (Fouad et al, 2020, p.334).""")
set_line(T15, "Root-surface treatment.", """**Root-surface treatment.** Sodium fluoride 2.4% (pH 5.5, 20 minutes) is reported to halve the progression of root resorption in replanted human teeth (Andreasen et al, 2007, p.477). The IADT does not mention fluoride, so this is a textbook option.""")
set_line(T15, "Splinting.", """**Splinting.** Use a passive flexible splint for two weeks, or four weeks if the alveolus or jaw is fractured (Fouad et al, 2020, p.334-335). Andreasen et al note that rigid splinting increases resorption and that one week is normally sufficient (Andreasen et al, 2007, p.477). Kumari et al (2025) support flexible, short splints, on very low-quality evidence (PDF p.1).""")
set_line(T15, "Sequence at the chair.", """**Sequence at the chair.** Rinse, replant gently, splint flexibly for two weeks, give amoxicillin or penicillin, and check tetanus status (Fouad et al, 2020, p.334-336). A closed apex needs root canal treatment within two weeks; Andreasen starts it at about one week (Andreasen et al, 2007, p.477). Review at 2 weeks, 4 weeks, 3 and 6 months, one year, then yearly (Fouad et al, 2020, p.337).""")

# ------------------------------------------------------------------ T16 (exam 568 -> ~390)
T16 = "T16_Avulsed_Maxillary_Central_Incisor_Open_Apex_10m.md"
set_line(T16, "Pre-replantation.", """**Pre-replantation.** Rinse visible contamination off with saline. Topical antibiotics are not supported: animal results were promising, but human studies have failed to show improved revascularisation (Fouad et al, 2020, p.336; Huang et al, 2024, PDF p.6). Systemic amoxicillin or penicillin are the IADT first choices (Fouad et al, 2020, p.336). The textbook doxycycline soak (Trope, n.d., p.345) is not an IADT recommendation.""")
set_line(T16, "Replantation.", """**Replantation.** Rinse the socket with saline, reposition any displaced socket wall, and replant gently (Andreasen et al, 2007, p.475). Splint for two weeks, or four if the alveolus is fractured (Fouad et al, 2020, p.334-335).""")
set_line(T16, "Choosing the endodontic route.", """**Choosing the endodontic route.** The IADT aim for an immature tooth is revascularisation. If it fails, apexification or root canal treatment follows, started only with definite necrosis and infection (Fouad et al, 2020, p.335). The three-hour rule is a textbook point (Andreasen et al, 2007, p.477).""")
set_line(T16, "Monitoring.", """**Monitoring.** Review at 2 weeks (splint removal), 1, 2, 3 and 6 months, one year, and yearly for at least five years (Fouad et al, 2020, p.337-338). Resorption is very rapid in children; if it starts, begin endodontic treatment with calcium hydroxide for up to one month (p.335, p.337).""")
set_line(T16, "Closed apex, for contrast.", """**Closed apex, for contrast.** No revascularisation is possible, so root canal treatment is needed within two weeks of replantation (Fouad et al, 2020, p.334). Trope gives 7 to 10 days from injury (Trope, n.d., p.341).""")

# ------------------------------------------------------------------ T11 (exam 425 -> ~380)
T11 = "T11_Splinting_in_Endodontics_10m.md"
set_line(T11, "Durations.", """**Durations.** IADT durations (Bourguignon et al, 2020, p.325-328): subluxation up to two weeks, only if mobility is excessive; extrusion two weeks, plus four if marginal bone breaks down; lateral luxation four weeks; intrusion four weeks after surgical repositioning; root fracture four weeks, up to four months cervically. Avulsed teeth: two weeks (Fouad et al, 2020, p.334). Andreasen et al give two to three weeks for extrusion and about three weeks for lateral luxation (Andreasen et al, 2007, p.442).""")
set_line(T11, "Materials.", """**Materials.** The IADT specifies a passive flexible wire of up to 0.4 mm, or nylon of 0.13 to 0.25 mm bonded with composite, and warns against nylon in children with few permanent teeth (Fouad et al, 2020, p.333-334).""")
reset_append(T11, "Technique.", "Kumari et al (2025) found very low-quality evidence, favouring flexible, short splints (PDF p.1).")

# ------------------------------------------------------------------ T10 (exam 476 -> ~390)
T10 = "T10_Fragment_Reattachment_10m.md"
reset_append(T10, "Technique.", "The IADT rehydrates the fragment for 20 minutes before bonding (Bourguignon et al, 2020, p.319).")
reset_append(T10, "Outcome.", "Khandelwal et al (2021) found 12 case reports and two case series, all favourable, with no randomised trials (PDF p.1, p.6).")

# ------------------------------------------------------------------ T09 (exam 617 -> <=600)
T09 = "T09_Ellis_Class_III_Fracture_Aesthetic_Restoration_15m.md"
reset_append(T09, "Pulp management.", "IADT: partial pulpotomy preferred in complete roots, with calcium silicate or non-setting calcium hydroxide (Bourguignon et al, 2020, p.320).")

# ------------------------------------------------------------------ T06 (exam 815 -> <=800)
T06 = "T06_Diagnosis_and_Management_of_Anterior_Fracture_in_an_18_Year_Old_20m.md"
set_line(T06, "Radiographs.", """**Radiographs.** For an uncomplicated crown fracture the IADT recommends one parallel periapical radiograph, with more only if other injury is suspected (Bourguignon et al, 2020, p.319). The films show pulp size, root stage, any root fracture and luxation, and serve as the baseline for review (Berman et al, n.d., p.33, p.74; Andreasen et al, 2007, p.320).""")
reset_append(T06, "Follow-up.", "IADT review: six to eight weeks and one year (Bourguignon et al, 2020, p.319).")

# ------------------------------------------------------------------ T05 (exam 2040 -> <=2000)
T05 = "T05_Fractured_Anterior_Teeth_Crown_Fracture_Management_50m.md"
reset_append(T05, "Uncomplicated fractures (no pulp exposure).", "The IADT rehydrates an intact fragment for 20 minutes and places calcium hydroxide where dentin is within 0.5 mm of the pulp (Bourguignon et al, 2020, p.319).")
reset_append(T05, "Complicated fractures (pulp exposure).", "The IADT prefers partial pulpotomy, including in complete roots, with non-setting calcium hydroxide or calcium silicate (Bourguignon et al, 2020, p.320); pulp removal is usually indicated in mature crown-root fractures (p.322).")
reset_append(T05, "Outcome figures.", "Krastl et al (2022) report pulp survival of 90-100% after pulpotomy in immature and 70-100% in mature teeth, on observational data (p.1007).")
reset_append(T05, "Follow-up.", "The IADT review is at six to eight weeks and one year (Bourguignon et al, 2020, p.319).")

# ------------------------------------------------------------------ T02 (exam 850 -> <=800)
T02 = "T02_Sequelae_of_a_Severely_Traumatised_Adult_Central_Incisor_20m.md"
set_line(T02, "Splinting.", """**Splinting.** Use a passive flexible splint for the IADT period for each injury (Bourguignon et al, 2020, p.323-328): up to two weeks for subluxation only if mobility is excessive; two weeks for extrusion, plus four if marginal bone breaks down; four weeks for lateral luxation and after surgical repositioning of an intruded tooth. Andreasen et al give about three weeks for lateral luxation (Andreasen et al, 2007, p.442). Rigid splints increase resorption (p.858).""")
reset_append(T02, "Endodontic decision.", "IADT: intracanal calcium hydroxide 1 to 2 weeks after trauma, for up to one month, in intruded, severely extruded or laterally luxated fully developed teeth (Bourguignon et al, 2020, p.317).")
reset_append(T02, "Long-term complications.", "The IADT notes high canal obliteration rates after extrusion, intrusion and lateral luxation (p.317); Abreu et al (2024) pool 27.6% in permanent teeth (PDF p.1).")
reset_append(T02, "Follow-up.", "IADT reviews for extrusive and lateral luxation: 2, 4, 8 and 12 weeks, then 6 months and one year (Bourguignon et al, 2020, p.326-327).")

# ------------------------------------------------------------------ T01 (exam 3671 -> <=3500)
T01 = "T01_Traumatic_Injuries_to_Teeth_and_Related_Tissues_100m.md"
set_line(T01, "Avulsion.", """**Avulsion.** Replant at once, after a gentle rinse if the tooth is dirty (IADT). If replantation is delayed, store the tooth in milk, HBSS, saliva or saline, in that order; water is poor but better than drying (Fouad et al, 2020, p.333). After 30 minutes most PDL cells are non-viable, and 60 minutes is the IADT management boundary (p.333-334). Splint for two weeks, and start root canal treatment of a closed apex within two weeks (p.334). The IADT gives avulsion as 0.5% to 16% of dental injuries (p.332).""")
set_line(T01, "Luxation injuries.", """**Luxation injuries.** Concussion needs no treatment; subluxation is splinted for up to two weeks only if mobility is excessive (Bourguignon et al, 2020, p.325). Extrusion is repositioned gently and splinted for two weeks, four if marginal bone breaks down (p.326). Lateral luxation is repositioned digitally and splinted for four weeks (p.327). Intruded immature teeth are allowed to re-erupt, with orthodontic repositioning if none within four weeks; mature teeth under 3 mm are observed, with surgical repositioning if none within eight weeks; 3 to 7 mm is repositioned surgically (preferably) or orthodontically, and beyond 7 mm surgically (p.328). Andreasen et al give pulp necrosis after concussion in about 3%, subluxation 6%, extrusion 26%, lateral luxation 58% and intrusion 85% (Andreasen et al, 2007, p.394).""")
set_line(T01, "Splinting.", """**Splinting.** Splints should be flexible for luxation and semi-rigid or rigid for root fracture; rigid splinting harms healing (Andreasen et al, 2007, p.858). The IADT durations are given in the luxation and root-fracture answers. Andreasen et al give two to three weeks for extrusion, about three weeks for lateral luxation, and 7 to 10 days for replantation into an intact socket (p.864-865).""")
reset_append(T01, "Pulp management and endodontic timing.", "The IADT advises calcium hydroxide intracanal for up to one month in intruded, severely extruded or laterally luxated fully developed teeth (Bourguignon et al, 2020, p.317).")
reset_append(T01, "Crown-root fractures.", "IADT options: orthodontic or surgical extrusion, root submergence and intentional replantation (Bourguignon et al, 2020, p.321-322). Crowder et al (2024) report 37 decoronated teeth, on limited evidence (PDF p.1).")
reset_append(T01, "Crown fractures.", "The IADT rehydrates a fragment for 20 minutes, places calcium hydroxide within 0.5 mm of the pulp, and prefers partial pulpotomy, even in complete roots (Bourguignon et al, 2020, p.319-320).")
set_line(T01, "A timetable for review.", """**A timetable for review.** At the injury visit, record, radiograph, reposition and splint. Review at two weeks, when the splint is removed, and start endodontic treatment of a closed apex within two weeks (Fouad et al, 2020, p.334, p.337). Then review at four weeks, three and six months, one year, and yearly for five years; open apices at 1, 2, 3 and 6 months (p.337-338).""")

# ------------------------------------------------------------------ P1, P2 (exam 445 / 437 -> <=400)
P1 = "P1_Pulp_Options_for_Complicated_Crown_Fracture_in_an_Adult_10m_PREDICTED.md"
reset_append(P1, "Options by state of the pulp.", "The IADT prefers partial pulpotomy or pulp capping, including in complete roots (Bourguignon et al, 2020, p.320); pulp removal is usually indicated in mature crown-root fractures (p.322).")
reset_append(P1, "Success figures.", "Krastl et al (2022) report 70-100% success for pulpotomy in mature teeth, on observational data (p.1007).")
P2 = "P2_Traumatised_Immature_Incisor_with_Necrotic_Pulp_10m_PREDICTED.md"
reset_append(P2, "Apical barrier.", "IADT: intracanal calcium hydroxide for up to one month (Fouad et al, 2020, p.337); endodontics only with definite necrosis and infection (p.335). Krastl et al (2022) report 81-96% periapical healing with apical barriers (PDF p.8).")
reset_append(P2, "Regenerative options and monitoring.", "The IADT aim is revascularisation; if it fails, apexification or root canal treatment follows (Fouad et al, 2020, p.335).")

# ------------------------------------------------------------------ move audit notes out of study sections
for f in ["T01_Traumatic_Injuries_to_Teeth_and_Related_Tissues_100m.md",
          "T02_Sequelae_of_a_Severely_Traumatised_Adult_Central_Incisor_20m.md",
          "T03_Root_Healing_following_Traumatic_Injuries_20m.md",
          "T04_Luxation_Injuries_in_the_Permanent_Dentition_50m.md",
          "T05_Fractured_Anterior_Teeth_Crown_Fracture_Management_50m.md",
          "T06_Diagnosis_and_Management_of_Anterior_Fracture_in_an_18_Year_Old_20m.md",
          "T07_Uncomplicated_Crown_Fracture_without_Pulpal_Exposure_in_a_12_Year_Old_20m.md",
          "T08_Class_IV_Fracture_of_Maxillary_Central_Incisor_in_a_25_Year_Old_20m.md",
          "T09_Ellis_Class_III_Fracture_Aesthetic_Restoration_15m.md",
          "T10_Fragment_Reattachment_10m.md",
          "T11_Splinting_in_Endodontics_10m.md",
          "T12_Classify_Traumatic_Injuries_and_Management_of_Horizontal_Root_Fractures_20m.md",
          "T13_Tooth_Avulsion_and_its_Management_10m.md",
          "T14_Avulsion_Media_used_in_Endodontics_20m.md",
          "T15_Newer_Philosophies_of_Replantation_10m.md",
          "T16_Avulsed_Maxillary_Central_Incisor_Open_Apex_10m.md",
          "T17_Intentional_Replantation_10m.md",
          "T18_Transplantation_Autotransplantation_10m.md",
          "T19_Forced_Eruption_or_Extrusion_7m.md",
          "T20_Dens_Invaginatus_Classification_and_Management_10m.md"]:
    move_notes(f)

print("DONE", len(DONE))
print("FAILS", len(FAILS))
for f in FAILS:
    print("  FAIL", f)
