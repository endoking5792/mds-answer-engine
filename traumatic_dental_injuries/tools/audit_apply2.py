"""Apply the IADT 2020 audit (2026-10-19) to the topic answers.

Only statements confirmed against the supplied guideline text (tools/verify_iadt.py) are written.
Exam-mode edits convert (Author, year, p.N) citations to the file's bracket style.
Study-mode audit notes keep parentheses. Failed anchors are collected in FAILS, not raised,
so one run shows every problem. Restore from the scratchpad backup before re-running.
"""
import os
import re

BASE = "/Users/niranjan/.claude/answer_tools/traumatic_dental_injuries"
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


def exam_span(t):
    return t.index("## EXAM MODE"), t.index("## HIGH-YIELD POINTS")


def exam_label(path, label, new, mode):
    t = read(path)
    a, b = exam_span(t)
    lines = t[a:b].split("\n")
    hits = [i for i, l in enumerate(lines) if l.startswith("**" + label)]
    if len(hits) != 1:
        FAILS.append((path, label, len(hits)))
        return
    i = hits[0]
    if mode == "set":
        lines[i] = brackets(new.strip())
    else:
        lines[i] = lines[i].rstrip() + " " + brackets(new.strip())
    write(path, t[:a] + "\n".join(lines) + t[b:])
    DONE.append((os.path.basename(path), mode, label))


def exam_set(path, label, new):
    exam_label(path, label, new, "set")


def exam_append(path, label, extra):
    exam_label(path, label, extra, "append")


def exam_table(path, label, rows):
    t = read(path)
    a, b = exam_span(t)
    seg = t[a:b].split("\n")
    hits = [k for k, l in enumerate(seg) if l.startswith("**" + label)]
    if len(hits) != 1:
        FAILS.append((path, label, len(hits)))
        return
    j = hits[0] + 1
    while j < len(seg) and seg[j].strip() == "":
        j += 1
    k = j
    while k < len(seg) and seg[k].startswith("|"):
        k += 1
    if k == j:
        FAILS.append((path, label, "no table rows"))
        return
    seg[j:k] = rows
    write(path, t[:a] + "\n".join(seg) + t[b:])
    DONE.append((os.path.basename(path), "table", label))


def exam_text(path, old, new):
    t = read(path)
    a, b = exam_span(t)
    n = t[a:b].count(old)
    if n != 1:
        FAILS.append((path, "exam text", n, old[:50]))
        return
    write(path, t[:a] + t[a:b].replace(old, new) + t[b:])
    DONE.append((os.path.basename(path), "text", old[:40]))


def replace_once(path, old, new):
    t = read(path)
    n = t.count(old)
    if n != 1:
        FAILS.append((path, "replace", n, old[:50]))
        return
    write(path, t.replace(old, new))
    DONE.append((os.path.basename(path), "replace", old[:40]))


def note(path, text):
    t = read(path)
    anchor = "## CRITICAL EVIDENCE SYNTHESIS" if "## CRITICAL EVIDENCE SYNTHESIS" in t else "## EXAM MODE"
    if t.count(anchor) != 1:
        FAILS.append((path, "anchor", anchor))
        return
    write(path, t.replace(anchor, text.strip() + "\n\n" + anchor, 1))
    DONE.append((os.path.basename(path), "note", ""))


def add_refs(path, lines):
    t = read(path)
    m = t.find("**SOURCE LOCATORS")
    if m < 0:
        FAILS.append((path, "no locators heading"))
        return
    new = [l for l in lines if l[:40] not in t]
    if not new:
        return
    pre = t[:m].rstrip("\n")
    write(path, pre + "\n" + "\n".join(new) + "\n\n" + t[m:])
    DONE.append((os.path.basename(path), "refs", str(len(new))))


def add_locs(path, lines):
    t = read(path)
    m = t.find("**Note on Sources")
    if m < 0:
        FAILS.append((path, "no note on sources"))
        return
    new = [l for l in lines if l[:40] not in t]
    if not new:
        return
    pre = t[:m].rstrip("\n")
    write(path, pre + "\n" + "\n".join(new) + "\n\n" + t[m:])
    DONE.append((os.path.basename(path), "locs", str(len(new))))


# ---------------------------------------------------------------- shared references
REF_FOUAD = "- Fouad AF, et al. International Association of Dental Traumatology guidelines for the management of traumatic dental injuries: 2. Avulsion of permanent teeth. Dent Traumatol. 2020;36:331-342. doi:10.1111/edt.12573."
REF_BOURG = "- Bourguignon C, et al. International Association of Dental Traumatology guidelines for the management of traumatic dental injuries: 1. Fractures and luxations of permanent teeth. Dent Traumatol. 2020;36:314-330. doi:10.1111/edt.12578."
REF_KHAN = "- Khandelwal P, et al. Fragment reattachment after complicated crown-root fractures of anterior teeth: a systematic review. Dent Traumatol. 2021;37:37-52. doi:10.1111/edt.12602."
REF_KRASTL = "- Krastl G, et al. Present status and future directions: endodontic management of traumatic injuries to permanent teeth. Int Endod J. 2022;55(Suppl 4):1003-1019. doi:10.1111/iej.13672."
REF_CROWDER = "- Crowder S, et al. Endodontic management of submerged roots following complicated traumatic dental injuries. Int J Paediatr Dent. 2024;34:608-620. doi:10.1111/ipd.13161."
REF_KUMARI = "- Kumari B, et al. Effect of splinting on outcomes of replantation of avulsed permanent teeth in children: a systematic review. J Indian Soc Pedod Prev Dent. 2025 (volume not confirmed; first page 307)."
REF_BLACK = "- Blackledge CA, et al. Comparison of storage media on periodontal cell viability before replantation of avulsed teeth: systematic review and meta-analysis. J Clin Med. 2025;14:1986. doi:10.3390/jcm14061986 (title and DOI as given on the uploaded PDF; not re-checked against the journal page)."
REF_HUANG = "- Huang R, et al. Expert consensus on management of tooth luxation and avulsion. Int J Oral Sci. 2024; article s41368-024-00321-z (volume not confirmed from the text layer)."
REF_ABREU = "- Abreu MGL, et al. Prevalence of pulp canal obliteration after traumatic dental injuries: a systematic review and meta-analysis. Braz Oral Res. 2024 (volume and article number not confirmed from the text layer)."
REF_SAIKIA = "- Saikia A, et al. Systematic review of clinical practice guidelines for traumatic dental injuries. Dent Traumatol. 2023;39:371-380. doi:10.1111/edt.12838."
REF_ANDR2002 = "- Andreasen JO, et al. Effect of treatment delay upon pulp and periodontal healing of traumatic dental injuries: a review article. Dent Traumatol. 2002;18:116-128."

LOC_FOUAD = [
    "- Fouad et al, 2020 (uploaded PDF, PDF p.2 = printed p.332): avulsion is '0.5%-16% of all dental injuries'.",
    "- Fouad et al, 2020 (PDF p.3 = printed p.333): 'After an extra-alveolar dry time of 30 minutes, most PDL cells are non-viable'; 'In descending order of preference, milk, HBSS, saliva ... or saline'; 'Although water is a poor medium'.",
    "- Fouad et al, 2020 (PDF p.4 = printed p.334): 'Stabilize the tooth for 2 weeks'; 'Initiate root canal treatment within 2 weeks after replantation'; 'Check tetanus status'; 'Delayed replantation has a poor long-term prognosis'.",
    "- Fouad et al, 2020 (PDF p.5 = printed p.335): 'should be left in place for 4 weeks' (alveolar or jawbone fracture); 'endodontic treatment should not be initiated unless there are definite signs'; 'Such resorption is very rapid in children'.",
    "- Fouad et al, 2020 (PDF p.6 = printed p.336): 'Amoxicillin or penicillin remain the first choices'; 'generally not recommended for patients under 12 years'; topical antibiotics 'failed to demonstrate improved pulp revascularization'.",
    "- Fouad et al, 2020 (PDF p.7 = printed p.337): 'Calcium hydroxide is recommended as an intracanal medicament for up to 1 month'; review at 2 weeks, 4 weeks, 3 months, 6 months, one year, yearly for at least five years.",
    "- Fouad et al, 2020 (PDF p.8 = printed p.338): open-apex review at 1, 2, 3 and 6 months; 'Pulp canal obliteration is expected' during the first year.",
]
LOC_BOURG = [
    "- Bourguignon et al, 2020 (uploaded PDF; printed = PDF + 313): PDF p.3 (p.316) CBCT for 'root fractures, crown/root fractures, and lateral luxations'.",
    "- Bourguignon et al, 2020 (PDF p.4 = p.317): 'Extrusion, intrusion, and lateral luxation injuries have high rates of PCO'; calcium hydroxide 'to be placed 1-2 weeks after trauma for up to 1 month'.",
    "- Bourguignon et al, 2020 (PDF p.6 = p.319): 'rehydrated by soaking in water or saline for 20 min'; 'within 0.5 mm of the pulp'; review 'after 6-8 wk' and 'after 1 y'.",
    "- Bourguignon et al, 2020 (PDF p.7 = p.320): 'partial pulpotomy) is also the preferred treatment in teeth with completed root development'; 'Non-setting calcium hydroxide or non-staining calcium silicate cements'.",
    "- Bourguignon et al, 2020 (PDF p.9 = p.322): 'In mature teeth with complete root formation, removal of the pulp is usually indicated' (crown-root fracture); options listed on PDF p.8-9 (p.321-322).",
    "- Bourguignon et al, 2020 (PDF p.10 = p.323): 'passive and flexible splint for 4 wk'; 'up to 4 mo' if cervical; review after 4 wk, 6-8 wk, 4 mo, 6 mo, 1 y.",
    "- Bourguignon et al, 2020 (PDF p.11 = p.324): 'Root canal treatment is contraindicated at the emergency visit'.",
    "- Bourguignon et al, 2020 (PDF p.12 = p.325): 'up to 2 wk may be used but only if there is excessive mobility or tenderness'.",
    "- Bourguignon et al, 2020 (PDF p.13 = p.326): Table 11, extrusive: 'splint for an additional 4 wk' if marginal bone breaks down; review after 2, 4, 8, 12 wk, 6 mo, 1 y.",
    "- Bourguignon et al, 2020 (PDF p.14 = p.327): Table 12, lateral: 'Stabilize the tooth for 4 wk using a passive and flexible splint'.",
    "- Bourguignon et al, 2020 (PDF p.15 = p.328): immature intrusion 'Allow re-eruption without intervention ... for all intruded teeth'; 'If no re-eruption within 4 wk'; 'intruded 3-7 mm, reposition surgically (preferably) or orthodontically'; 'beyond 7mm, reposition surgically'; 'Root canal treatment should be started at 2 wk'.",
]
LOC_KHAN = [
    "- Khandelwal et al, 2021 (uploaded PDF; printed = PDF + 36): PDF p.1 (p.37) 'Twelve case reports and two case series'; 'Treatment outcomes were favorable in all the included articles'; post in 85%; bevelling or groove formation in 42%.",
    "- Khandelwal et al, 2021 (PDF p.6 = p.42): 'there are no randomized clinical trials available on this topic'.",
]
LOC_KRASTL = [
    "- Krastl et al, 2022 (uploaded PDF; printed = PDF + 1002): PDF p.4 (p.1006) 'clinical success rate of 93% (Rao et al., 2020)'; PDF p.5 (p.1007) immature 90%-100%, mature 70%-100% with pulpotomy.",
    "- Krastl et al, 2022 (PDF p.8 = p.1010): apical barrier 'periapical healing ranging between 81% and 96%'; both apical barrier and revitalization 'currently recommended procedures'.",
]
LOC_CROWDER = [
    "- Crowder et al, 2024 (uploaded PDF; printed = PDF + 607): PDF p.1 (p.608) '18 articles' (17 case reports, one case series); 'A total of 37 teeth were treated with decoronation'; 'successful in apexogenesis and preserving alveolar bone'.",
]
LOC_KUMARI = [
    "- Kumari et al, 2025 (uploaded PDF; printed = PDF + 306): PDF p.1 (p.307) '7 studies were included in the qualitative synthesis and 4 in the meta-analysis', 975 avulsed teeth; 'GRADE analysis rated the overall evidence as very low'; trends favour 'flexible splints and shorter durations'.",
]
LOC_BLACK = [
    "- Blackledge et al, 2025 (uploaded PDF): PDF p.1 and p.3: 'Hank's balanced salt solution is the most effective storage medium in the preservation of periodontal cell viability' (in vitro evidence).",
]
LOC_HUANG = [
    "- Huang et al, 2024 (uploaded PDF, article s41368-024-00321-z): PDF p.5 'passive and flexible splint ... for 2 weeks' (subluxation, extrusive luxation); PDF p.6 'No significant improvement in clinical revascularization success rate ... topical antibiotics'; 'Amoxicillin and penicillin are the first antibiotics choice' (PDF p.6); PDF p.3 'Calcium hydroxide should not be firstly used' (intracanal, for external resorption context).",
]
LOC_ABREU = [
    "- Abreu et al, 2024 (uploaded PDF): PDF p.1 pooled PCO 27.6% (permanent) and 21.9% (deciduous); root fractures 78.6% in permanent teeth; lateral luxation 29.4% in deciduous teeth. PDF p.6: concussion 45.2% (high heterogeneity), subluxation 25.7%, lateral luxation 24.4%, intrusive 14.4%, avulsion 12.9%, crown fracture 8.1%.",
]
LOC_SAIKIA = [
    "- Saikia et al, 2023 (uploaded PDF, PDF p.2): 'Several deficiencies exist in the methodological quality of existing CPGs on TDI'.",
]
LOC_ANDR2002 = [
    "- Andreasen et al, 2002 (uploaded PDF; printed = PDF + 115): PDF p.1 (p.116) 'based on our present rather limited knowledge'; 'Crown and crown/root fractures: Subacute or delayed approach'.",
]

# ==================================================================== T13 avulsion
T13 = "T13_Tooth_Avulsion_and_its_Management_10m.md"
exam_set(T13, "Emergency phase.", """**Emergency phase.** Replant the tooth at once. If it is dirty, rinse it gently in milk, saline or the patient's saliva, then replant it in its socket and ask the patient to bite on gauze to hold it (Fouad et al, 2020, p.333). If replantation is not possible, use a medium in the order milk, HBSS, saliva, saline; water is a poor medium but better than letting the root dry (Fouad et al, 2020, p.333).""")
exam_set(T13, "Clinical phase.", """**Clinical phase.** Record the extra-alveolar dry time and the storage medium. After 30 minutes of dry time most PDL cells are non-viable, and 60 minutes is the IADT boundary between management categories (Fouad et al, 2020, p.333-334). Avoid touching the root. Stabilise with a passive flexible wire of up to 0.4 mm, or nylon fishing line of 0.13 to 0.25 mm bonded with composite, for two weeks; nylon is not recommended for children with only a few permanent teeth (Fouad et al, 2020, p.333-334). For an associated alveolar or jawbone fracture, use a more rigid splint for four weeks (Fouad et al, 2020, p.335). Check tetanus status (Fouad et al, 2020, p.334).""")
exam_set(T13, "Endodontic phase.", """**Endodontic phase.** A closed-apex tooth needs root canal treatment within two weeks of replantation (Fouad et al, 2020, p.334). For an open apex the IADT aim is pulp revascularisation; endodontic treatment starts only when there are definite signs of pulp necrosis and infection at follow-up (Fouad et al, 2020, p.335). Calcium hydroxide may be used intracanal for up to one month before root filling (Fouad et al, 2020, p.337). Systemic antibiotics: amoxicillin or penicillin are the first choices, and tetracycline or doxycycline are generally not recommended for patients under 12 years (Fouad et al, 2020, p.336).""")
exam_set(T13, "Follow-up.", """**Follow-up.** Review clinically and radiographically at 2 weeks (when the splint is removed), 4 weeks, 3 months, 6 months, one year, and yearly for at least five years (Fouad et al, 2020, p.337). An open-apex tooth is reviewed at 1, 2, 3 and 6 months as well (Fouad et al, 2020, p.338). Watch for inflammatory root resorption, which is very rapid in children (Fouad et al, 2020, p.335).""")
exam_set(T13, "Prognosis.", """**Prognosis.** Prognosis depends on the extra-alveolar dry time, the storage medium and the root stage. A delayed replantation has a poor long-term prognosis: the periodontal ligament becomes necrotic and ankylosis-related (replacement) root resorption is the expected outcome (Fouad et al, 2020, p.334).""")
note(T13, """**Audit note (IADT 2020, checked 2026-10-19).** Fouad et al (2020) was read in full for avulsion. Corrections to the earlier draft: (1) the rinse is gentle, in milk, saline or saliva, not a ten-second rinse under running water (p.333); (2) the splint is two weeks, not one week (p.334), with four weeks for alveolar or jawbone fracture (p.335); (3) the root canal window for a closed apex is two weeks after replantation, not one week or seven to ten days from injury (p.334); (4) amoxicillin or penicillin are the first antibiotic choice, and tetracycline or doxycycline are generally not recommended under 12 years (p.336), so the Harty's doxycycline statement is kept only as a textbook point; (5) the IADT review schedule is 2 weeks, 4 weeks, 3 and 6 months, one year and yearly (p.337), not radiographs at 2 and 3 weeks alone; (6) the IADT viability figure is 30 minutes, and 60 minutes is the management boundary (p.333-334), so the statement that PDL survival is unlikely at 60 minutes is restated. The textbook timings (Andreasen et al, 2007, p.477; Trope, n.d., p.341) are kept in the study text for comparison. Confidence: the IADT points are [Certain]; the textbook timings remain [Likely].""")
add_refs(T13, [REF_FOUAD])
add_locs(T13, LOC_FOUAD)

# ==================================================================== T14 media
T14 = "T14_Avulsion_Media_used_in_Endodontics_20m.md"
exam_set(T14, "Preferred media.", """**Preferred media.** The IADT lists storage media in descending order of preference: milk, Hank's balanced salt solution (HBSS), saliva and saline, and describes all four as suitable and convenient (Fouad et al, 2020, p.333). A 2025 systematic review and meta-analysis found HBSS the most effective medium for preserving PDL cell viability, on in vitro evidence (Blackledge et al, 2025, p.1, p.3). The two sources agree that HBSS is the best-supported medium; the IADT places milk first for practical reasons.""")
exam_set(T14, "Time.", """**Time.** The IADT figures are the operative ones. After 30 minutes of extra-alveolar dry time most PDL cells are non-viable (Fouad et al, 2020, p.333). If the tooth has been kept in a suitable medium with less than 60 minutes of dry time, the PDL cells may be viable but compromised; with more than 60 minutes, they are likely non-viable (Fouad et al, 2020, p.333). Harty's calls extra-alveolar time the most critical factor (Sigurdsson and Bourguignon, n.d., p.260).""")
note(T14, """**Audit note (IADT 2020; Blackledge et al, 2025, checked 2026-10-19).** The storage order in the IADT is milk, HBSS, saliva, saline (Fouad et al, 2020, p.333), which matches the milk-first ranking in Cohen's and differs from its clinical-section statement that HBSS is best. The 2025 meta-analysis supports HBSS in vitro (PDF p.1, p.3). Corrections: the 60-minute figure is the IADT management boundary, and the viability figure is 30 minutes; the earlier text presented 60 minutes as the point of PDL death. The Andreasen experimental comparison is a textbook point and is not claimed as IADT. The earlier figures attributed to Andreasen's 400-tooth study were removed because they could not be verified against the supplied text. The 'Viaspan' comparison was also removed because the IADT does not mention it.""")
add_refs(T14, [REF_FOUAD, REF_BLACK])
add_locs(T14, LOC_FOUAD[1:3] + LOC_BLACK)

# ==================================================================== T15 replantation
T15 = "T15_Newer_Philosophies_of_Replantation_10m.md"
exam_set(T15, "Delayed replantation.", """**Delayed replantation.** For a tooth with prolonged dry time and a contused socket, Andreasen et al describe delayed replantation: let the socket heal first, treat the root surface, then complete endodontic treatment (Andreasen et al, 2007, p.478). The IADT does not present delayed replantation as a route to a good outcome: it has a poor long-term prognosis, the periodontal ligament becomes necrotic, and ankylosis-related (replacement) root resorption is the expected outcome (Fouad et al, 2020, p.334).""")
exam_set(T15, "Root-surface treatment.", """**Root-surface treatment.** Andreasen et al report that sodium fluoride 2.4% at pH 5.5 for 20 minutes slowed the progression of root resorption by about 50% in replanted human teeth (Andreasen et al, 2007, p.477). The IADT avulsion guideline does not mention fluoride root treatment, so the measure is a textbook option with limited evidence.""")
exam_set(T15, "Splinting.", """**Splinting.** The IADT stabilises a replanted tooth for two weeks with a passive flexible splint (wire of up to 0.4 mm, or nylon), and uses a more rigid splint for four weeks when there is an alveolar or jawbone fracture (Fouad et al, 2020, p.334-335). Andreasen et al state that one week is normally sufficient and that rigid splinting increases resorption (Andreasen et al, 2007, p.477). The 2025 systematic review of splinting in children found very low-quality evidence, with trends favouring flexible, short splints, which it describes as tentative support for the IADT approach (Kumari et al, 2025, p.1).""")
exam_set(T15, "Sequence at the chair.", """**Sequence at the chair.** Rinse any visible contamination with saline or an osmolality-balanced medium, replant gently, stabilise with a passive flexible splint for two weeks, give systemic antibiotics (amoxicillin or penicillin first), and check tetanus status (Fouad et al, 2020, p.334-336). For a closed apex, start root canal treatment within two weeks of replantation. Review at 2 weeks, 4 weeks, 3 months, 6 months, one year, and yearly for at least five years (Fouad et al, 2020, p.337). Andreasen et al start endodontic treatment about one week after replantation (Andreasen et al, 2007, p.477), a difference to state in the exam.""")
note(T15, """**Audit note (IADT 2020; Kumari et al, 2025, checked 2026-10-19).** Corrections to the earlier draft: the IADT splint is two weeks, not one week (Fouad et al, 2020, p.334-335); the root canal window for a closed apex is two weeks, not one week (p.334); the first antibiotic choice is amoxicillin or penicillin (p.336). The IADT does not mention fluoride root treatment (no match in the guideline text), and it states that delayed replantation has a poor long-term prognosis (p.334). The Andreasen delayed-replantation and fluoride protocol is kept as a textbook option. The 2025 splinting review (Kumari et al, 2025, PDF p.1) supports flexible, short splints but rates the evidence very low.""")
add_refs(T15, [REF_FOUAD, REF_KUMARI])
add_locs(T15, LOC_FOUAD[2:5] + LOC_KUMARI)

# ==================================================================== T16 open apex
T16 = "T16_Avulsed_Maxillary_Central_Incisor_Open_Apex_10m.md"
exam_set(T16, "Pre-replantation.", """**Pre-replantation.** If there is visible contamination, rinse the root surface with a stream of saline or an osmolality-balanced medium to remove gross debris (Fouad et al, 2020, p.334). Topical antibiotics are not established. The IADT says animal results were promising, but human studies have failed to show improved pulp revascularisation after teeth are soaked in topical antibiotics (Fouad et al, 2020, p.336). Huang et al (2024) report no significant improvement in clinical revascularisation with topical antibiotics (PDF p.6). The doxycycline soak in the textbook sources (Andreasen et al, 2007, p.477; Trope, n.d., p.345; Kahler, n.d., p.2638) is therefore a textbook measure, not an IADT recommendation. Systemic antibiotics, with amoxicillin or penicillin as the first choice, are the IADT route (Fouad et al, 2020, p.336).""")
exam_set(T16, "Replantation.", """**Replantation.** Rinse the socket with saline to flush contaminated coagulum, reposition any displaced socket wall with light digital pressure, and replant gently (Andreasen et al, 2007, p.475). Stabilise with a passive flexible splint for two weeks, or for four weeks if there is an alveolar or jawbone fracture (Fouad et al, 2020, p.334-335).""")
exam_set(T16, "Choosing the endodontic route.", """**Choosing the endodontic route.** For an immature tooth the IADT goal is pulp revascularisation, which allows continued root development (Fouad et al, 2020, p.335). If spontaneous revascularisation does not occur, the IADT lists apexification, pulp revitalisation or root canal treatment, and endodontic treatment starts only when there are definite signs of necrosis and infection at follow-up (Fouad et al, 2020, p.335). The Andreasen three-hour rule for an open apex is not in the IADT text and remains a textbook point (Andreasen et al, 2007, p.477). Harty's suggests root canal treatment before replantation after a long dry time, but the sentence is incomplete in the extracted text (Sigurdsson and Bourguignon, n.d., p.262).""")
exam_set(T16, "Monitoring.", """**Monitoring.** Review at 2 weeks, when the splint is removed, then at 1, 2, 3 and 6 months, one year, and yearly for at least five years (Fouad et al, 2020, p.337-338). Inflammatory root resorption is weighed against the chance of revascularisation, and it is very rapid in children (Fouad et al, 2020, p.335). If resorption starts and revascularisation has not occurred, start endodontic treatment with calcium hydroxide intracanal for up to one month (Fouad et al, 2020, p.335, p.337).""")
exam_set(T16, "Closed apex, for contrast.", """**Closed apex, for contrast.** A closed apex cannot revascularise, so root canal treatment is needed within two weeks of replantation (Fouad et al, 2020, p.334). Trope puts root canal treatment within 7 to 10 days of injury (Trope, n.d., p.341), a difference to state in the exam.""")
replace_once(T16, "**Status:** DRAFTED, not audited. Textbook-only; IADT guideline not retrieved.", "**Status:** DRAFTED, audited against IADT 2020 on 2026-10-19 (see audit note).")
replace_once(T16, "The IADT guideline was not retrieved.", "The IADT 2020 guidelines were checked for this answer (see the audit note).")
note(T16, """**Audit note (IADT 2020; Huang et al, 2024, checked 2026-10-19).** Corrections: (1) the topical-antibiotic claim is restated: the IADT says the effect is unproven and that human studies have failed to show improved revascularisation (Fouad et al, 2020, p.336); Huang et al (2024, PDF p.6) report no significant improvement; (2) the splint is two weeks, four for an alveolar or jawbone fracture (p.334-335), not one week; (3) the root canal window for a closed apex is two weeks (p.334); (4) the IADT open-apex review is at 1, 2, 3 and 6 months (p.338), in addition to the schedule in the exam. Not in the IADT text: the three-hour rule (no match in the guideline text) and the 'radiographs at 2 and 3 weeks' schedule, which are kept as textbook points.""")
add_refs(T16, [REF_FOUAD, REF_HUANG])
add_locs(T16, LOC_FOUAD[1:5] + LOC_HUANG)

# ==================================================================== T04 luxation
T04 = "T04_Luxation_Injuries_in_the_Permanent_Dentition_50m.md"
exam_append(T04, "Concussion and subluxation.", "The IADT advises no treatment for concussion, and for subluxation a passive flexible splint for up to two weeks only if mobility or tenderness is excessive (Bourguignon et al, 2020, p.325).")
exam_set(T04, "Extrusive luxation.", """**Extrusive luxation.** The IADT repositions the tooth gently by pushing it back into the socket under local anaesthesia, then stabilises it with a passive flexible splint for two weeks, adding four weeks if the marginal bone breaks down (Bourguignon et al, 2020, p.326). The IADT radiographs are one parallel periapical view, two further views at different angulations, and an occlusal view (Bourguignon et al, 2020, p.326). Andreasen et al give two to three weeks (Andreasen et al, 2007, p.442).""")
exam_set(T04, "Lateral luxation.", """**Lateral luxation.** Local anaesthesia is needed. The IADT repositions the tooth digitally, releasing it from its locked position, and stabilises it with a passive flexible splint for four weeks, with additional splinting if the marginal bone or socket wall breaks down (Bourguignon et al, 2020, p.327). Andreasen et al give about three weeks, extended to six to eight weeks if bone breaks down (Andreasen et al, 2007, p.442), and Harty's table gives two weeks (Sigurdsson and Bourguignon, n.d., p.262). Lateral luxation with apical displacement is likely to need root canal treatment (Berman et al, n.d., p.75).""")
exam_set(T04, "Intrusive luxation.", """**Intrusive luxation.** Intrusion carries the highest risk of pulp necrosis, bone loss and resorption. For immature teeth the IADT allows spontaneous re-eruption for all intruded teeth, whatever the degree of intrusion; if there is no re-eruption within four weeks, orthodontic repositioning starts (Bourguignon et al, 2020, p.328). For mature teeth, an intrusion of less than 3 mm may re-erupt without intervention; if there is no re-eruption within eight weeks the tooth is repositioned surgically and splinted for four weeks. For 3 to 7 mm the IADT prefers surgical repositioning, with orthodontic as the alternative; beyond 7 mm it recommends surgical repositioning (Bourguignon et al, 2020, p.328). Andreasen et al prefer orthodontic extrusion to surgical repositioning (Andreasen et al, 2007, p.458), so the two sources disagree on the preferred method for 3 to 7 mm.""")
exam_set(T04, "Splinting.", """**Splinting.** Splints should be flexible or semi-rigid. The IADT durations are: concussion, no splint; subluxation up to two weeks only if mobility is excessive; extrusion two weeks, plus four weeks if the marginal bone breaks down; lateral luxation four weeks; intrusion four weeks after surgical repositioning; root fracture four weeks, up to four months for a cervical fracture; alveolar fracture four weeks (Bourguignon et al, 2020, p.323-328; Fouad et al, 2020, p.335). Andreasen et al give two to three weeks for extrusion and subluxation, and about three weeks for lateral luxation (Andreasen et al, 2007, p.442). The IADT figures are the current guideline figures.""")
exam_table(T04, "Summary by type.", [
    "| Type | Pulp necrosis (Andreasen et al) | Reposition | Splint: Andreasen / IADT 2020 | Key follow-up |",
    "|---|---|---|---|---|",
    "| Concussion | 3% | none | none / no treatment [Bourguignon et al, 2020, p.325] | monitor pulp for at least one year |",
    "| Subluxation | 6% | occlusal reduction if needed | short flexible splint if mobility significant / up to 2 weeks, only if mobility or tenderness is excessive | review at 2 weeks, 12 weeks, 6 months, 1 year |",
    "| Extrusion | 26% | gentle axial pressure under local anaesthesia | 2-3 weeks / 2 weeks, plus 4 weeks if marginal bone breaks down | review at 2, 4, 8, 12 weeks, 6 months, 1 year, then yearly for 5 years |",
    "| Lateral luxation | 58% | digital reposition under local anaesthesia | about 3 weeks, 6-8 if bone breaks down / 4 weeks, extended if marginal bone or socket wall breaks down | as for extrusion; immature teeth watched for revascularisation |",
    "| Intrusion | 85% | immature: spontaneous re-eruption, orthodontic if none by 4 weeks; mature: under 3 mm observed, surgical if none by 8 weeks; 3-7 mm surgical (preferred) or orthodontic; beyond 7 mm surgical | no fixed figure (Andreasen) / 4 weeks after surgical repositioning | root canal treatment at 2 weeks or as soon as position allows [Bourguignon et al, 2020, p.328] |",
])
exam_text(T04, "four weeks in the IADT figures reported by Ogle, so the lateral duration is contested among three sources [Harty's, n.d., p.262; Andreasen et al, 2007, p.442; Ogle, 2024, p.158] [Likely].", "four weeks in the IADT 2020 guideline [Bourguignon et al, 2020, p.327], so the lateral duration is contested among three sources [Harty's, n.d., p.262; Andreasen et al, 2007, p.442; Bourguignon et al, 2020, p.327] [Likely].")
exam_append(T04, "Follow-up.", "The IADT schedule for extrusive and lateral luxation is 2, 4, 8 and 12 weeks, then 6 months, one year, and yearly for at least five years (Bourguignon et al, 2020, p.326-327). Andreasen et al note late complications, including pulp canal obliteration (Andreasen et al, 2007, p.412-413).")
note(T04, """**Audit note (IADT 2020, Bourguignon et al, 2020, checked 2026-10-19).** Tables 11 and 12 (PDF p.13-14, printed p.326-327) and the intrusion rules (PDF p.15, printed p.328) were read in full. Corrections: (1) lateral luxation splint is four weeks (IADT), against three weeks (Andreasen) and two weeks (Harty's), so the IADT figure now leads; (2) extrusion splint is two weeks, plus four weeks if marginal bone breaks down, which agrees with Harty's and not with Andreasen's two to three weeks; (3) intrusion: for 3 to 7 mm the IADT prefers surgical repositioning, against Andreasen's preference for orthodontic extrusion (p.458), which remains a visible disagreement; (4) the IADT allows spontaneous re-eruption for all intruded immature teeth, and for mature teeth less than 3 mm; (5) the Ogle (2024) avulsion figure of four weeks for dry time over 60 minutes is not in the IADT avulsion text, which gives two weeks and four weeks only for an alveolar or jawbone fracture (Fouad et al, 2020, p.334-335). The sensibility schedule (Cohen's Ch.21) is unchanged, with the IADT lateral figure added for comparison.""")
add_refs(T04, [REF_BOURG])
add_locs(T04, LOC_BOURG)

# ==================================================================== T11 splinting
T11 = "T11_Splinting_in_Endodontics_10m.md"
exam_set(T11, "Durations.", """**Durations.** IADT durations (Bourguignon et al, 2020; Fouad et al, 2020): subluxation up to two weeks, only if mobility is excessive (p.325); extrusion two weeks, plus four weeks if marginal bone breaks down (p.326); lateral luxation four weeks (p.327); intrusion four weeks after surgical repositioning (p.328); root fracture four weeks, up to four months for cervical fractures (p.323); replanted avulsed teeth two weeks with a passive flexible wire (Fouad et al, 2020, p.334), and four weeks for an alveolar or jawbone fracture (p.335). Andreasen et al give two to three weeks for extrusion and subluxation, and about three weeks for lateral luxation (Andreasen et al, 2007, p.442). Harty's table gives two weeks for lateral luxation (Sigurdsson and Bourguignon, n.d., p.262). The IADT figures are the current guideline figures.""")
exam_set(T11, "Materials.", """**Materials.** The IADT specifies a passive flexible wire of up to 0.4 mm (0.016 inch), or nylon fishing line of 0.13 to 0.25 mm bonded with composite, and warns against nylon in children with only a few permanent teeth. Keep composite and bonding agent away from the gingival tissues and proximal areas (Fouad et al, 2020, p.333-334). Rigid splints increase resorption and can inhibit revascularisation (Andreasen et al, 2007, p.858).""")
exam_append(T11, "Technique.", "The 2025 pediatric systematic review of splinting for replanted avulsed teeth found very low-quality evidence, with trends favouring flexible, short splints in line with the IADT (Kumari et al, 2025, p.1).")
note(T11, """**Audit note (IADT 2020; Kumari et al, 2025, checked 2026-10-19).** Corrections: the avulsion splint is two weeks (Fouad et al, 2020, p.334), not one week; the IADT luxation durations are in Bourguignon et al (2020, p.323-328) and differ from the Andreasen figures for lateral luxation. The Ogle (2024) figure of four weeks for avulsion with dry time over 60 minutes is not in the IADT avulsion text, which gives two weeks and four weeks only for an alveolar or jawbone fracture (Fouad et al, 2020, p.334-335). The nylon and wire specifications are as in the IADT text (p.333-334). The 2025 splinting review found very low-quality evidence and supports the IADT's flexible, short-term approach (PDF p.1).""")
add_refs(T11, [REF_FOUAD, REF_BOURG, REF_KUMARI])
add_locs(T11, LOC_KUMARI + LOC_FOUAD[1:4] + LOC_BOURG)

# ==================================================================== T12 root fracture
T12 = "T12_Classify_Traumatic_Injuries_and_Management_of_Horizontal_Root_Fractures_20m.md"
exam_set(T12, "Diagnosis.", """**Diagnosis.** Take one parallel periapical radiograph, two further radiographs at different vertical or horizontal angulations, and an occlusal view, as the IADT lists for luxation and root injuries (Bourguignon et al, 2020, p.321, p.326). Berman's guide recommends two or three radiographs at different vertical angulations (Berman et al, n.d., p.52). Fractures can be missed on the first film and seen later (Andreasen et al, 2007, p.355). CBCT is useful for root fractures where it is available (Bourguignon et al, 2020, p.316).""")
exam_set(T12, "Management.", """**Management.** Reposition the coronal fragment completely under local anaesthesia and apply a passive flexible splint for four weeks, extended for a cervical fracture for up to four months (Bourguignon et al, 2020, p.323). Root canal treatment is contraindicated at the emergency visit (Bourguignon et al, 2020, p.324). Andreasen et al describe splinting until a hard-tissue callus forms, usually about three months, and report that rigid splints give the poorest results (Andreasen et al, 2007, p.369, p.377).""")
exam_set(T12, "Follow-up.", """**Follow-up.** Review clinically and radiographically at four weeks (splint removal), six to eight weeks, four months and six months, then at one year and yearly for at least five years (Bourguignon et al, 2020, p.323).""")
note(T12, """**Audit note (IADT 2020, checked 2026-10-19).** The radiograph set, the splint duration (four weeks, up to four months cervically), the emergency root canal contraindication and the review schedule were checked against Bourguignon et al (2020, p.316, p.321, p.323-324). The IADT figures agree with Harty's table. The IADT does not state a rigid-splint preference; the Andreasen comparison is kept as a textbook finding.""")
add_refs(T12, [REF_BOURG])
add_locs(T12, LOC_BOURG[0:1] + LOC_BOURG[5:7])

# ==================================================================== T10 reattachment
T10 = "T10_Fragment_Reattachment_10m.md"
exam_append(T10, "Technique.", "The IADT rehydrates the fragment in water or saline for 20 minutes before bonding, and covers exposed dentin with glass-ionomer or a bonding agent and composite (Bourguignon et al, 2020, p.319).")
exam_append(T10, "Outcome.", "A systematic review of fragment reattachment after complicated crown-root fractures included 12 case reports and two case series, all with favourable outcomes; a post was used in 85% of cases and bevelling or groove formation in 42%. It found no randomised clinical trials and describes the technique as viable where conditions are favourable (Khandelwal et al, 2021, p.1, p.6).")
note(T10, """**Audit note (IADT 2020; Khandelwal et al, 2021, checked 2026-10-19).** The IADT rehydration step (20 minutes) is added (Bourguignon et al, 2020, p.319). The Khandelwal review is case-level evidence (12 case reports and two case series); the answer states that no randomised trial exists and that the evidence grade is low. Figures verified: 85% post; 42% bevelling or groove formation; 'favorable in all the included articles' (PDF p.1).""")
add_refs(T10, [REF_BOURG, REF_KHAN])
add_locs(T10, LOC_BOURG[2:3] + LOC_KHAN)

# ==================================================================== T05 crown fractures
T05 = "T05_Fractured_Anterior_Teeth_Crown_Fracture_Management_50m.md"
exam_append(T05, "Uncomplicated fractures (no pulp exposure).", "The IADT rehydrates an intact fragment for 20 minutes before bonding; exposed dentin is covered with glass-ionomer or bonding and composite, and calcium hydroxide is placed where the dentin is within 0.5 mm of the pulp; review is at six to eight weeks and one year (Bourguignon et al, 2020, p.319).")
exam_append(T05, "Complicated fractures (pulp exposure).", "The IADT prefers partial pulpotomy for complicated crown fractures, including teeth with completed roots, with non-setting calcium hydroxide or non-staining calcium silicate cement on the pulp wound (Bourguignon et al, 2020, p.320). For complicated crown-root fractures in mature teeth the IADT usually indicates pulp removal (p.322), so the two IADT positions differ by fracture type.")
exam_append(T05, "Outcome figures.", "Krastl et al (2022) report pulp survival after partial pulpotomy of 90 to 100% in immature and 70 to 100% in mature traumatised teeth, and a 93% clinical success rate for calcium hydroxide in a study they cite (Rao et al, 2020) (Krastl et al, 2022, p.1006-1007). They note that trial data are lacking.")
exam_append(T05, "Follow-up.", "The IADT review schedule for an uncomplicated crown fracture is at six to eight weeks and one year (Bourguignon et al, 2020, p.319).")
note(T05, """**Audit note (IADT 2020; Krastl et al, 2022, checked 2026-10-19).** The IADT crown-fracture rules (rehydration, the 0.5 mm calcium hydroxide rule, the preference for partial pulpotomy, the review schedule) are added. Two points of internal IADT disagreement are recorded: partial pulpotomy is preferred for complicated crown fractures in complete roots (p.320), while pulp removal is usually indicated in mature crown-root fractures (p.322). The Krastl success figures are observational and are labelled as such.""")
add_refs(T05, [REF_BOURG, REF_KRASTL])
add_locs(T05, LOC_BOURG[2:4] + LOC_KRASTL)

# ==================================================================== T07 12-year-old
T07 = "T07_Uncomplicated_Crown_Fracture_without_Pulpal_Exposure_in_a_12_Year_Old_20m.md"
exam_append(T07, "Immediate care.", "Where the exposed dentin is within 0.5 mm of the pulp, the IADT places a calcium hydroxide lining before the glass-ionomer or bonded cover (Bourguignon et al, 2020, p.319).")
exam_append(T07, "Follow-up schedule.", "The IADT review for an uncomplicated crown fracture is at six to eight weeks and one year (Bourguignon et al, 2020, p.319).")
note(T07, """**Audit note (IADT 2020; Andreasen et al, 2002, checked 2026-10-19).** The IADT review interval for an uncomplicated crown fracture (six to eight weeks, one year) and the calcium hydroxide rule for dentin within 0.5 mm of the pulp are added (Bourguignon et al, 2020, p.319). The IADT radiograph recommendation is one parallel periapical view, with more only if other injuries are suspected (p.319). The treatment-delay review (Andreasen et al, 2002, printed p.116) gives a subacute or delayed approach for crown fractures, which is consistent with the exam text.""")
add_refs(T07, [REF_BOURG, REF_ANDR2002])
add_locs(T07, LOC_BOURG[2:3] + LOC_ANDR2002)

# ==================================================================== T06 18-year-old
T06 = "T06_Diagnosis_and_Management_of_Anterior_Fracture_in_an_18_Year_Old_20m.md"
exam_set(T06, "Radiographs.", """**Radiographs.** For an uncomplicated crown fracture the IADT recommends one parallel periapical radiograph, with additional radiographs only if there are signs or symptoms of other injury (Bourguignon et al, 2020, p.319). Take periapical views at more than one angle, with an occlusal view, where other injuries are suspected. The films show pulp size, root stage, any root fracture and any luxation, and they serve as the baseline for later review (Berman et al, n.d., p.33, p.74; Andreasen et al, 2007, p.320).""")
exam_append(T06, "Follow-up.", "The IADT review for an uncomplicated crown fracture is at six to eight weeks and one year (Bourguignon et al, 2020, p.319).")
add_refs(T06, [REF_BOURG])
add_locs(T06, LOC_BOURG[2:3])

# ==================================================================== T02 sequelae
T02 = "T02_Sequelae_of_a_Severely_Traumatised_Adult_Central_Incisor_20m.md"
exam_set(T02, "Splinting.", """**Splinting.** Use a passive flexible splint for the period the IADT specifies for each injury (Bourguignon et al, 2020, p.323-328): up to two weeks for subluxation only if mobility is excessive; two weeks for extrusion, plus four if the marginal bone breaks down; four weeks for lateral luxation; and four weeks after surgical repositioning of an intruded tooth. Andreasen et al give about three weeks for lateral luxation (Andreasen et al, 2007, p.442), and Harty's table gives two weeks (Sigurdsson and Bourguignon, n.d., p.262). Rigid splints increase resorption (Andreasen et al, 2007, p.858).""")
exam_append(T02, "Endodontic decision.", "The IADT recommends intracanal calcium hydroxide placed 1 to 2 weeks after trauma, for up to one month before root filling, in fully developed teeth that have been intruded, severely extruded or laterally luxated; a corticosteroid-antibiotic paste is an alternative (Bourguignon et al, 2020, p.317).")
exam_append(T02, "Long-term complications.", "The IADT notes high rates of pulp canal obliteration after extrusion, intrusion and lateral luxation (Bourguignon et al, 2020, p.317). A 2024 meta-analysis gives a pooled prevalence of 27.6% in permanent teeth, highest after root fracture (78.6%) (Abreu et al, 2024, PDF p.1, p.6).")
exam_append(T02, "Follow-up.", "The IADT review schedules vary by injury; for extrusive and lateral luxation they are 2, 4, 8 and 12 weeks, then 6 months, one year, and yearly for at least five years (Bourguignon et al, 2020, p.326-327).")
note(T02, """**Audit note (IADT 2020; Abreu et al, 2024, checked 2026-10-19).** Corrections: the splint durations are the IADT figures (lateral luxation four weeks, extrusion two weeks plus four for marginal bone breakdown; Bourguignon et al, 2020, p.325-328). The calcium hydroxide statement is restated from the IADT text: 1 to 2 weeks after trauma, for up to one month, in fully developed teeth with intrusion, severe extrusion or lateral luxation (p.317). The canal-obliteration figures from Abreu et al (2024, PDF p.1, p.6) are added beside the textbook range, and the IADT statement that obliteration is more frequent after extrusion, intrusion and lateral luxation is recorded (p.317).""")
add_refs(T02, [REF_BOURG, REF_ABREU])
add_locs(T02, LOC_BOURG + LOC_ABREU)

# ==================================================================== T03 healing
T03 = "T03_Root_Healing_following_Traumatic_Injuries_20m.md"
exam_append(T03, "Canal obliteration.", "The IADT says pulp canal obliteration is expected and can be recognised radiographically during the first year after injury (Fouad et al, 2020, p.338). A 2024 meta-analysis gives a pooled prevalence of 27.6% in permanent teeth, with root fractures highest at 78.6% and concussion at 45.2% with high heterogeneity (Abreu et al, 2024, PDF p.1, p.6).")
add_refs(T03, [REF_FOUAD, REF_ABREU])
add_locs(T03, LOC_FOUAD[6:7] + LOC_ABREU)

# ==================================================================== T01 umbrella
T01 = "T01_Traumatic_Injuries_to_Teeth_and_Related_Tissues_100m.md"
exam_set(T01, "Avulsion.", """**Avulsion.** Replant at once, after a gentle rinse if the tooth is dirty (IADT). If replantation must be delayed, store the tooth in an osmolality-balanced medium, in the IADT order milk, HBSS, saliva, saline; water is poor but better than drying (Fouad et al, 2020, p.333). After 30 minutes of dry time most PDL cells are non-viable, and 60 minutes is the IADT boundary between management categories (p.333-334). Stabilise with a passive flexible splint for two weeks, and start root canal treatment of a closed apex within two weeks of replantation (p.334). The IADT gives avulsion as 0.5% to 16% of dental injuries (Fouad et al, 2020, p.332), against 0.5 to 3% in Andreasen's permanent-dentition figure (Andreasen et al, 2007, p.460).""")
exam_set(T01, "Luxation injuries.", """**Luxation injuries.** Concussion needs no treatment; a passive flexible splint for up to two weeks is used for subluxation only if mobility is excessive (Bourguignon et al, 2020, p.325). For extrusion the tooth is pushed back gently under local anaesthesia and splinted for two weeks, four if the marginal bone breaks down (p.326). For lateral luxation the tooth is repositioned digitally and splinted for four weeks (p.327). For intrusion of immature teeth, spontaneous re-eruption is allowed, with orthodontic repositioning if there is none within four weeks; for mature teeth, under 3 mm is observed, surgical repositioning follows if there is none within eight weeks, 3 to 7 mm is repositioned surgically (preferably) or orthodontically, and beyond 7 mm surgically (p.328). Andreasen et al give pulp necrosis after concussion in about 3%, subluxation 6%, extrusion 26%, lateral luxation 58% and intrusion 85% (Andreasen et al, 2007, p.394).""")
exam_set(T01, "Splinting.", """**Splinting.** Splints should be flexible for luxation and semi-rigid or rigid for root fracture; rigid splinting harms healing (Andreasen et al, 2007, p.858). IADT durations (Bourguignon et al, 2020, p.323-328; Fouad et al, 2020, p.334-335): subluxation up to two weeks if mobile; extrusion two weeks, plus four if the marginal bone breaks down; lateral luxation four weeks; intrusion four weeks after surgical repositioning; root fracture four weeks, up to four months cervically; alveolar or jawbone fracture four weeks; replanted avulsed teeth two weeks. Andreasen et al give two to three weeks for extrusion, about three weeks for lateral luxation, and four to six weeks for root fracture, and 7 to 10 days for replantation into an intact socket (Andreasen et al, 2007, p.864-865).""")
exam_append(T01, "Pulp management and endodontic timing.", "The IADT treats root canal treatment of a closed-apex tooth as due within two weeks of replantation (Fouad et al, 2020, p.334). Calcium hydroxide may be placed intracanal 1 to 2 weeks after trauma, for up to one month, in fully developed intruded, severely extruded or laterally luxated teeth (Bourguignon et al, 2020, p.317).")
exam_append(T01, "Crown-root fractures.", "The IADT lists orthodontic extrusion of the apical or non-mobile fragment, surgical extrusion, root submergence and intentional replantation as options (Bourguignon et al, 2020, p.321-322). Crowder et al (2024) reviewed 18 articles (17 case reports and one case series) with 37 teeth treated by decoronation or submergence; immediate decoronation and vital root submergence were reported as successful for apexogenesis and bone preservation (PDF p.1).")
exam_append(T01, "Crown fractures.", "The IADT rehydrates an intact fragment for 20 minutes, places calcium hydroxide where dentin is within 0.5 mm of the pulp, and prefers partial pulpotomy for complicated crown fractures, including teeth with completed roots (Bourguignon et al, 2020, p.319-320). For complicated crown-root fractures in mature teeth it usually indicates pulp removal (p.322).")
exam_append(T01, "Timing.", "Crown and crown-root fractures are managed subacutely or in a delayed way (Andreasen et al, 2002, printed p.116).")
exam_set(T01, "A timetable for review.", """**A timetable for review.** At the injury visit: records, radiographs and reposition with a splint. Review at two weeks, when the splint is removed (Fouad et al, 2020, p.337). Start endodontic treatment of a closed-apex tooth within two weeks of replantation (p.334). Review again at four weeks, three and six months, and one year, then yearly for at least five years (Fouad et al, 2020, p.337). An open-apex tooth is reviewed at one, two, three and six months as well (p.338).""")
note(T01, """**Audit note (IADT 2020, checked 2026-10-19).** This umbrella answer was checked against the two IADT 2020 guidelines (Fouad et al, 2020; Bourguignon et al, 2020) and the 2002-2025 reviews. Corrections: the 60-minute figure is the IADT management boundary, and viability falls at 30 minutes (p.333-334); the avulsion splint is two weeks (p.334); the closed-apex root canal window is two weeks (p.334); the luxation splint durations and intrusion rules follow the IADT tables (p.325-328); the lateral-luxation splint is four weeks (p.327); the IADT avulsion figure is 0.5 to 16% of dental injuries (p.332). The IADT itself contains an internal distinction between complicated crown fractures (partial pulpotomy preferred, p.320) and crown-root fractures in mature teeth (pulp removal usually indicated, p.322). Saikia et al (2023, PDF p.2) found several deficiencies in the methodological quality of the guidelines, including the IADT, so the IADT is used as the primary source with that caveat.""")
add_refs(T01, [REF_FOUAD, REF_BOURG, REF_CROWDER, REF_ANDR2002, REF_SAIKIA])
add_locs(T01, LOC_FOUAD[1:4] + LOC_BOURG + LOC_CROWDER + LOC_ANDR2002 + LOC_SAIKIA)

# ==================================================================== T08 Class IV
T08 = "T08_Class_IV_Fracture_of_Maxillary_Central_Incisor_in_a_25_Year_Old_20m.md"
exam_append(T08, "Root fracture.", "The IADT recommends CBCT where available for root and crown-root fractures (Bourguignon et al, 2020, p.316), and lists orthodontic extrusion, surgical extrusion and root submergence among the options for crown-root fractures (p.321-322).")
add_refs(T08, [REF_BOURG])
add_locs(T08, LOC_BOURG[0:1] + LOC_BOURG[4:5])

# ==================================================================== T09 Ellis III
T09 = "T09_Ellis_Class_III_Fracture_Aesthetic_Restoration_15m.md"
exam_append(T09, "Pulp management.", "The IADT lists non-setting calcium hydroxide or non-staining calcium silicate cement for the pulp wound, and calls partial pulpotomy the preferred treatment for complicated crown fractures in teeth with completed roots (Bourguignon et al, 2020, p.320).")
add_refs(T09, [REF_BOURG])
add_locs(T09, LOC_BOURG[3:4])

# ==================================================================== T19 forced eruption
T19 = "T19_Forced_Eruption_or_Extrusion_7m.md"
exam_append(T19, "Method.", "The IADT lists orthodontic extrusion, surgical extrusion and root submergence as options for complicated crown-root fractures (Bourguignon et al, 2020, p.321-322).")
add_refs(T19, [REF_BOURG])
add_locs(T19, LOC_BOURG[4:5])

# ==================================================================== P1 adult pulp
P1 = "P1_Pulp_Options_for_Complicated_Crown_Fracture_in_an_Adult_10m_PREDICTED.md"
exam_append(P1, "Options by state of the pulp.", "The IADT prefers partial pulpotomy or pulp capping for complicated crown fractures, including teeth with completed roots, with non-setting calcium hydroxide or non-staining calcium silicate cement on the pulp wound (Bourguignon et al, 2020, p.320). For a complicated crown-root fracture in a mature tooth the IADT usually indicates pulp removal (p.322).")
exam_append(P1, "Success figures.", "Krastl et al (2022) report 70 to 100% success for partial pulpotomy in mature traumatised teeth, and note that trial data are lacking (Krastl et al, 2022, p.1007).")
add_refs(P1, [REF_BOURG, REF_KRASTL])
add_locs(P1, LOC_BOURG[3:5] + LOC_KRASTL[0:1])

# ==================================================================== P2 immature
P2 = "P2_Traumatised_Immature_Incisor_with_Necrotic_Pulp_10m_PREDICTED.md"
exam_append(P2, "Apical barrier.", "The IADT recommends intracanal calcium hydroxide for up to one month before root filling, and says endodontic treatment should not start unless there are definite signs of pulp necrosis and infection at follow-up (Fouad et al, 2020, p.335, p.337). Krastl et al (2022) report periapical healing of 81 to 96% with the apical barrier technique (PDF p.8).")
exam_append(P2, "Regenerative options and monitoring.", "The IADT aim for an immature tooth is pulp revascularisation; if it does not occur, the IADT lists apexification, pulp revitalisation or root canal treatment (Fouad et al, 2020, p.335).")
add_refs(P2, [REF_FOUAD, REF_KRASTL])
add_locs(P2, LOC_FOUAD[3:4] + LOC_FOUAD[5:6] + LOC_KRASTL[1:2])

# ==================================================================== P3 ankylosis
P3 = "P3_Replacement_Resorption_Ankylosis_in_a_Growing_Patient_10m_PREDICTED.md"
exam_append(P3, "Management.", "The IADT advises that parents be told decoronation or autotransplantation may be needed later if the replanted tooth ankyloses (Fouad et al, 2020, p.335-336). Crowder et al (2024) describe decoronation and root submergence in 37 teeth, mostly in case reports, with limited evidence (PDF p.1).")
add_refs(P3, [REF_FOUAD, REF_CROWDER])
add_locs(P3, LOC_FOUAD[3:5] + LOC_CROWDER)

# ==================================================================== study-only notes (not in the exam scope)
T17 = "T17_Intentional_Replantation_10m.md"
note(T17, """**Audit note (IADT 2020, checked 2026-10-19).** Bourguignon et al (2020, PDF p.8-9, printed p.321-322) list intentional replantation, with or without rotation of the root, among the future treatment options for complicated crown-root fractures. No separate IADT intentional-replantation protocol was found in the supplied text, so the exam sections are unchanged.""")
add_refs(T17, [REF_BOURG])

T18 = "T18_Transplantation_Autotransplantation_10m.md"
note(T18, """**Audit note (IADT 2020, checked 2026-10-19).** Bourguignon et al (2020, PDF p.8-9, printed p.321-322) list autotransplantation among the options for complicated crown-root fractures, and Fouad et al (2020, PDF p.5, printed p.335) advise parents that decoronation or autotransplantation may be needed later if a replanted tooth ankyloses. No further IADT autotransplantation protocol was found in the supplied text.""")
add_refs(T18, [REF_BOURG, REF_FOUAD])

T20 = "T20_Dens_Invaginatus_Classification_and_Management_10m.md"
note(T20, """**Audit note (IADT 2020, checked 2026-10-19).** A keyword search of the two IADT 2020 guidelines and the supplied reviews found no mention of dens invaginatus. The answer's classification and management rest on the textbook sources, and the IADT is not an audit source for this topic.""")

# ==================================================================== status lines and reports
for f in ["T02_Sequelae_of_a_Severely_Traumatised_Adult_Central_Incisor_20m.md",
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
          "T01_Traumatic_Injuries_to_Teeth_and_Related_Tissues_100m.md",
          "T13_Tooth_Avulsion_and_its_Management_10m.md",
          "T14_Avulsion_Media_used_in_Endodontics_20m.md",
          "T19_Forced_Eruption_or_Extrusion_7m.md",
          "P1_Pulp_Options_for_Complicated_Crown_Fracture_in_an_Adult_10m_PREDICTED.md",
          "P2_Traumatised_Immature_Incisor_with_Necrotic_Pulp_10m_PREDICTED.md",
          "P3_Replacement_Resorption_Ankylosis_in_a_Growing_Patient_10m_PREDICTED.md"]:
    t = read(f)
    m = re.search(r"^\*\*Status:\*\*[^\n]*$", t, re.M)
    if not m or "not audited" not in m.group(0):
        FAILS.append((f, "status", bool(m)))
        continue
    line = m.group(0).replace("not audited", "audited against IADT 2020 on 2026-10-19 (see audit note)")
    write(f, t[:m.start()] + line + t[m.end():])
    DONE.append((f[:3], "status", ""))

print("DONE", len(DONE))
for d in DONE:
    print("  ok", d)
print("FAILS", len(FAILS))
for f in FAILS:
    print("  FAIL", f)
