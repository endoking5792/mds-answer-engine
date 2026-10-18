# Audit ledger: traumatic dental injuries against the supplied IADT 2020 guidelines and reviews (2026-10-19)

**Scope.** The answers in this folder were checked against the PDFs in the user's folder `trauma dental/`, extracted to `sources/guidelines/`:

- IADT 2020 Part 2, avulsion: Fouad et al, *Dent Traumatol* 2020 (DOI 10.1111/edt.12573). Printed page = PDF page + 330.
- IADT 2020 Part 1, fractures and luxations: Bourguignon et al, *Dent Traumatol* 2020 (DOI 10.1111/edt.12578). Printed page = PDF page + 313.
- Khandelwal et al, 2021 (fragment reattachment). Printed = PDF + 36.
- Krastl et al, 2022 (endodontic management of traumatised teeth). Printed = PDF + 1002.
- Saikia et al, 2023 (appraisal of clinical practice guidelines). Printed = PDF + 370.
- Crowder et al, 2024 (submerged roots). Printed = PDF + 607.
- Kumari et al, 2025 (splinting, systematic review). Printed = PDF + 306.
- Blackledge et al, 2025 (storage media, *J Clin Med*). PDF pages as cited.
- Huang et al, 2024 (expert consensus, *Int J Oral Sci*). PDF pages as cited.
- Abreu et al, 2024 (pulp canal obliteration, meta-analysis). PDF pages as cited.
- Andreasen et al, 2002 (treatment delay). Printed = PDF + 115.

**Method.** Each IADT-attributed statement was located with `tools/verify_iadt.py`, which matches phrases against the PDF text and reports the PDF page. Statements that were not found in the guideline text were not attributed to the IADT. The full text of Tables 3, 4, 11, 12 and 13 of Bourguignon et al (2020) was read directly. The intrusion rules were checked on PDF p.15.

**Edit method.** Exam Mode paragraphs were replaced or extended. Exam text was then trimmed to the Section 7 ranges. Study Mode content is unchanged apart from the audit-note section, which moved to the end of each file (heading `## AUDIT NOTE (IADT 2020, checked 2026-10-19)`), so Study word counts match the index.

## Corrections made, by answer

| File | Finding (what the earlier draft said, and what the IADT says) | Action | Source (PDF page, printed page) |
|---|---|---|---|
| T01 | 60 min presented as the point at which PDL cells die. IADT: 30 min is the point at which most PDL cells are non-viable; 60 min is the management boundary. | Corrected | Fouad p.3-4 (333-334) |
| T01 | Avulsion splint and endodontic window. IADT: splint 2 weeks; closed-apex root canal treatment within 2 weeks of replantation. | Corrected | Fouad p.4 (334) |
| T01 | Luxation splint durations and intrusion rules. IADT: subluxation up to 2 weeks only if mobility excessive; extrusion 2 weeks (+4 if marginal bone breaks down); lateral 4 weeks; intrusion rules by tooth stage and displacement. | Corrected | Bourguignon p.12-15 (325-328) |
| T01 | IADT avulsion frequency 0.5-16%. | Added | Fouad p.2 (332) |
| T01 | Complicated crown fractures prefer partial pulpotomy, including complete roots (p.320); complicated crown-root fractures in mature teeth usually pulp removal (p.322). The IADT itself distinguishes the two. | Added, both stated | Bourguignon p.7, p.9 (320, 322) |
| T02 | Lateral luxation splint, extrusion splint, intrusion splint. | Corrected | Bourguignon p.13-15 (326-328) |
| T02 | Calcium hydroxide intracanal 1-2 weeks after trauma, up to one month, in fully developed intruded, extruded or laterally luxated teeth. | Added | Bourguignon p.4 (317) |
| T02 | High PCO after extrusion, intrusion and lateral luxation. | Added | Bourguignon p.4 (317) |
| T02 | Abreu et al pooled PCO 27.6% (permanent), root fracture 78.6%. | Added | Abreu p.1, p.6 |
| T03 | Canal obliteration is expected and recognisable within the first year. | Added | Fouad p.8 (338) |
| T04 | Lateral luxation splint: earlier draft used Andreasen 3 weeks, Harty's 2 weeks and Ogle's 4 weeks. IADT: 4 weeks. | Corrected | Bourguignon p.14 (327) |
| T04 | Extrusion splint: IADT 2 weeks, +4 weeks if marginal bone breaks down. Andreasen 2-3 weeks. | Corrected; conflict stated | Bourguignon p.13 (326) |
| T04 | Intrusion: IADT prefers surgical repositioning for 3-7 mm (orthodontic as alternative) and surgical beyond 7 mm; spontaneous re-eruption allowed for immature teeth; <3 mm observed in mature teeth. Andreasen prefers orthodontic extrusion. | Corrected; conflict stated | Bourguignon p.15 (328); Andreasen p.458 |
| T04 | Earlier draft said reposition "within three to four days" and gave an Andreasen re-eruption age. Neither is in the IADT text. | Removed | Not found |
| T04 | Concussion: IADT gives no treatment. Subluxation: splint up to 2 weeks only if mobility excessive. | Corrected | Bourguignon p.12 (325) |
| T04 | Follow-up schedule for extrusion and lateral luxation: 2, 4, 8, 12 weeks, 6 months, 1 year, yearly for 5 years. | Added | Bourguignon p.13-14 (326-327) |
| T05 | Uncomplicated fracture: rehydrate 20 min; calcium hydroxide within 0.5 mm of pulp; review 6-8 weeks and 1 year. | Added | Bourguignon p.6 (319) |
| T05 | Partial pulpotomy preferred incl. complete roots; non-setting CH or calcium silicate on pulp wound. | Added | Bourguignon p.7 (320) |
| T05 | Krastl et al: pulp survival 90-100% immature, 70-100% mature (observational); CH 93% in a cited study. | Added, labelled observational | Krastl p.4-5 (1006-1007) |
| T06 | Radiographs: one parallel periapical for uncomplicated fracture; more only if other injury suspected. Follow-up 6-8 weeks and 1 year. | Corrected | Bourguignon p.6 (319) |
| T07 | Calcium hydroxide before GI cover when dentin within 0.5 mm; review 6-8 weeks and 1 year. | Added | Bourguignon p.6 (319) |
| T07 | Treatment-delay approach for crown fractures: subacute or delayed. | Confirmed | Andreasen 2002 p.1 (116) |
| T08 | CBCT for root and crown-root fractures; crown-root options. | Added | Bourguignon p.3, p.8-9 (316, 321-322) |
| T09 | Calcium silicate or non-setting CH on pulp wound; partial pulpotomy preferred. | Added | Bourguignon p.7 (320) |
| T10 | Rehydrate fragment 20 min before bonding; cover dentin with GI or bonding and composite. | Added | Bourguignon p.6 (319) |
| T10 | Khandelwal: 14 articles (12 case reports, 2 case series); all favourable; post 85%; bevelling 42%; no randomised trial. | Added; labelled case-level | Khandelwal p.1, p.6 (37, 42) |
| T11 | Avulsion splint 2 weeks, not 1 week; alveolar fracture 4 weeks. | Corrected | Fouad p.4-5 (334-335) |
| T11 | Wire up to 0.4 mm; nylon 0.13-0.25 mm; nylon not for children with few permanent teeth. | Added | Fouad p.3-4 (333-334) |
| T11 | Ogle (2024) figure of 4 weeks for avulsion with dry time over 60 min. Not in the IADT avulsion text. | Flagged in audit note | Fouad p.4-5 (334-335) |
| T11 | Kumari et al: very low-quality evidence; trends favour flexible short splints. | Added | Kumari p.1 (307) |
| T12 | Radiographs: one parallel periapical, two further angulations, occlusal. | Confirmed | Bourguignon p.8 (321); Tables 11-13 |
| T12 | Root fracture splint 4 weeks; cervical up to 4 months. Root canal treatment contraindicated at emergency visit. Review at 4 weeks, 6-8 weeks, 4 and 6 months, 1 year, yearly for 5 years. | Confirmed and added | Bourguignon p.10-11 (323-324) |
| T13 | Emergency rinse: earlier draft said 10 seconds under cold running water. IADT: rinse gently in milk, saline or saliva if dirty. | Corrected | Fouad p.3 (333) |
| T13 | Splint: earlier draft said 1 week. IADT: 2 weeks passive flexible; 4 weeks for alveolar or jaw fracture. | Corrected | Fouad p.3-5 (333-335) |
| T13 | Root canal window: earlier draft said 1 week or 7-10 days. IADT: within 2 weeks of replantation (closed apex). | Corrected | Fouad p.4 (334) |
| T13 | Antibiotics: earlier draft quoted Harty's doxycycline for over-12 patients. IADT: amoxicillin or penicillin first; tetracycline or doxycycline generally not recommended under 12. | Corrected | Fouad p.6 (336) |
| T13 | Follow-up: earlier draft gave radiographs at 2 and 3 weeks. IADT: 2 weeks (splint removal), 4 weeks, 3 and 6 months, 1 year, yearly for 5 years; open apex also at 1, 2, 3 and 6 months. | Corrected | Fouad p.7-8 (337-338) |
| T13 | Prognosis: delayed replantation poor long-term; ankylosis-related resorption expected. | Added | Fouad p.4 (334) |
| T14 | Storage order: IADT milk, HBSS, saliva, saline. Earlier draft placed HBSS first without the IADT order. | Corrected | Fouad p.3 (333) |
| T14 | Blackledge et al 2025: HBSS most effective in vitro. | Added; labelled in vitro | Blackledge p.1, p.3 |
| T14 | Earlier draft: ten-second rinse under cold running water in the storage paragraph. | Corrected to gentle rinse in milk, saline or saliva | Fouad p.3 (333) |
| T14 | Earlier draft: 73% of teeth replanted within 5 min healed PDL vs 18% stored (Andreasen p.486). Not verifiable in the supplied text. | Removed | Not found |
| T14 | Earlier draft: Viaspan named as a storage medium. Not in the IADT text. | Removed | Not found |
| T15 | Delayed replantation: IADT poor long-term prognosis, ankylosis expected. Andreasen's protocol kept as a textbook option. | Corrected | Fouad p.4, p.6 (334, 336) |
| T15 | Fluoride root treatment: not mentioned in IADT (no match in the guideline text). Kept as textbook. | Labelled | Not found (IADT) |
| T15 | Splint: IADT 2 weeks flexible; 4 weeks for alveolar or jaw fracture (earlier draft: 1 week rigid). | Corrected | Fouad p.5 (335) |
| T15 | Kumari et al 2025: very low-quality evidence; tentatively supports IADT flexible short splinting. | Added | Kumari p.1 (307) |
| T15 | Sequence: root canal treatment within 2 weeks of replantation for a closed apex (earlier draft: about 1 week). | Corrected | Fouad p.4 (334) |
| T16 | Topical doxycycline soak presented as standard. IADT: human studies failed to show improved revascularisation after topical antibiotics. Huang et al: no significant improvement. | Corrected; textbook soak kept and labelled | Fouad p.6 (336); Huang p.6 |
| T16 | Splint: IADT 2 weeks; 4 weeks for alveolar or jaw fracture (earlier draft: 1 week). | Corrected | Fouad p.4-5 (334-335) |
| T16 | Open apex follow-up: IADT at 2 weeks, then 1, 2, 3 and 6 months, 1 year, yearly for 5 years. Earlier draft: radiographs at 2 and 3 weeks. | Corrected | Fouad p.8 (338) |
| T16 | Calcium hydroxide intracanal up to one month if resorption starts. Inflammatory resorption very rapid in children. | Added | Fouad p.5, p.7 (335, 337) |
| T16 | Three-hour rule for open-apex revascularisation: not in IADT text. Kept as a textbook point. | Labelled | Not found (IADT) |
| T17 | IADT lists intentional replantation among options for crown-root fractures. No separate protocol in the supplied text. | Audit note only | Bourguignon p.8-9 (321-322) |
| T18 | IADT lists autotransplantation among options; parents informed of possible autotransplantation or decoronation if ankylosis. | Audit note only | Bourguignon p.8-9; Fouad p.5 (335) |
| T19 | Orthodontic extrusion, surgical extrusion, root submergence as options. | Added | Bourguignon p.8-9 (321-322) |
| T20 | Dens invaginatus: no mention in either IADT guideline (keyword search). No IADT content to audit against. | Audit note only | Not found (IADT) |
| P1 | Partial pulpotomy preferred incl. complete roots (IADT); pulp removal in mature crown-root fractures. | Added | Bourguignon p.7, p.9 (320, 322) |
| P1 | Kohli and Lee's "above 95%" statement retained as a narrative-review figure; Krastl 70-100% in mature teeth added. The two figures are kept side by side as different kinds of evidence. | Conflict stated | Krastl p.5 (1007) |
| P2 | Calcium hydroxide intracanal up to one month; endodontics only with definite necrosis and infection; revascularisation as the aim. | Added | Fouad p.5, p.7 (335, 337) |
| P2 | Krastl et al: apical barrier periapical healing 81-96%. | Added to note | Krastl p.8 (1010) |
| P3 | Parents informed decoronation or autotransplantation may be needed if ankylosis. | Added | Fouad p.5-6 (335-336) |
| P3 | Crowder et al: decoronation in 37 teeth; limited evidence. | Added | Crowder p.1 (608) |

## Points checked and not carried into the answers

- **Reposition up to 48 hours after injury** (Fouad p.3, printed p.333). This is in the IADT text but not added to the exam answers because of the Section 7 length limits. It is a candidate for the next revision of T13 and T14.
- **Pulp removal vs pulpotomy in complete roots.** The IADT gives different advice for complicated crown fractures (partial pulpotomy, p.320) and crown-root fractures (pulp removal, p.322). Both are stated in T01, T05, P1; this is recorded as an IADT-internal distinction, not a contradiction.

## Not audited (outside the supplied material)

- Textbook statements in Andreasen 2007, Berman, Harty's, Cohen's (Kahler), Ingle's (Trope), Sikri, Grossman's, Weine, Hexem and Eisler, Kohli and Lee, Ogle, and Trope 2010 (DCNA). These are retained as textbook or DCNA statements. Where they conflict with the IADT, the answer states the conflict.
- Full texts of Krastl 2022, Crowder 2024, Kumari 2025, Huang 2024, Abreu 2024, Khandelwal 2021, Saikia 2023 and Blackledge 2025 were searched for the phrases quoted in the answers. They were not read end to end.
- Citation metadata not confirmed from the journal page: Khandelwal first author initials; Krastl first author; Abreu journal and volume (Braz Oral Res, article e092 as given by the earlier draft); Huang author list and volume; Kumari volume (first page 307 only); Blackledge DOI (not checked against the journal); Fouad page range 331-342 (first page from the PDF's printed-page numbering; end page not checked).

## Result

- Exam Mode: every answer is within its Section 7 range (checked by `tools/count_words.py`, 2026-10-19). T14 is at 798 of 800.
- Study Mode: counts match 00_INDEX.md for the answers not changed in study.
- Confidence tags: IADT statements are [Certain] where the IADT text states them directly; reviews of observational or in vitro evidence are labelled as such.
