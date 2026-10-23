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
| T14 | Andreasen 400-tooth follow-up: 73% PDL healing within 5 min vs 18% when stored. First marked unverifiable in error; confirmed on p.485. | Kept; page corrected | Andreasen p.485 |
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

## Textbook and DCNA re-audit (2026-10-19)

**Scope.** Every citation to Andreasen 2007, Berman, Harty's (Sigurdsson and Bourguignon), Cohen's (Kahler), Ingle's (Trope), and the DCNA reviews (Kohli and Lee; Hexem and Eisler Parts 1 and 2; Ogle 2024; Trope 2010) in the 23 answers was checked against the local text extracts in `mds-textbooks`, the DCNA PDFs and the Berman OneDrive extract. The IADT and supplied-PDF citations were checked in the first audit above and are not repeated here.

**Coverage.** 589 citations to the named sources were resolved to a page. 466 matched automatically (the sentence's content words and numbers were found on the cited page, with a one-page tolerance for Andreasen and Harty's). 113 did not match and were judged one by one (113 verdicts): 27 supported, 32 supported in part or paraphrased, 7 page errors, 1 conflicts with the source, 5 metadata or tool artefacts, 41 not located on the cited page.

**Not audited.** Citations to Sikri, Grossman, Weine, Endodontic Radiology, Paranjpe and Noblett, and the AAE glossary (30 citations). Their extracts were not mapped in this pass.

**Corrections made in the answer files** (line numbers as at this re-audit):

- P2 Regenerative options: Kohli and Lee regenerative procedures cited to p.612 (was 619).
- T01 Crown-root/timing: Kohli 'two signs' cited to p.615 (was 610-611).
- T01 Antibiotics: Hexem and Eisler 'no clear consensus' cited to p.592 (was 594).
- T01 Pulp options: Andreasen 'capping contraindicated where degenerative change' cited to p.618 (was 624).
- T02 Splinting/intrusion: Andreasen 're-eruption in immature roots' cited to p.458 (was 431).
- T02 Kohli citations for canal obliteration, review schedule and five-year monitoring cited to p.616 (were 610 and 611).
- T02 Replacement resorption: 'no effective treatment' changed to 'no reliable treatment'; Kohli and Lee's point that 2% sodium fluoride for 20 minutes may slow it (p.619) added (exam and study). The ankylosis nuance (Kohli and Lee call it acceptable in some growing patients) moved to the Critical Evidence Synthesis section, which is excluded from the word count.
- T03 Canal obliteration: favourable-outcome statement cited to Kohli p.616 (was 619).
- T03 Revascularisation: '18 to 40%' and '1.1 mm' attributed to Harty's p.262 (not Andreasen 484-485); Kohli p.619 removed from the 7-16% claim, which Andreasen p.401 supports.
- T05 Hexem sealing claim cited to p.593 (was 596).
- T07 Hexem alveolar-bone statement cited to p.586 (was 589).
- T08 Kohli five-year monitoring cited to p.616 (was 611).
- T09 Hexem putty-index statement cited to p.594 (was 596).
- T14 Milk quotation: the quoted phrase ('by far the best alternative to the specialized transport media') is not in the source. Replaced with Harty's p.260 wording: milk or saline is the second-best transport medium after the specialised kits.
- T14 Storage: Andreasen quotations cited to p.485 and p.487 (were 486); time-to-dentist statement cited to p.475 (was 486).
- T16 Harty's pre-replantation root canal treatment: the sentence is complete on p.262. The text said it was cut off. Restored the reason: the apical portion is difficult to obturate hermetically by a traditional orthograde approach.
- T17 Intentional replantation definition: Harty's page corrected to p.225 (was p.1500-1502, an implausible page).
- P3 Kohli ridge preservation cited to p.621 (was 619-620); fluoride note added (Kohli p.619).
- T01 Pulp options and antibiotic citation: as above.

**Conflicts left visible.** (1) Kohli and Lee call ankylosis an acceptable outcome in some growing patients, against the textbook view that it is the most serious sequel (Critical Evidence Synthesis, T02). (2) Kohli and Lee and Harty's report that fluoride may slow replacement resorption; some answers still say there is no effective treatment (T02, P3 corrected; T02 Harty's p.266 'no treatment' wording not located). (3) Kohli and Lee's partial-pulpotomy figure (above 95%) and Krastl's observational 70-100% are both stated.

**Not located on the cited page (U), for checking in the book itself.**
- P1_ L23 ANDR: exposure-record list not located on Andreasen p304
- P3_ L20 BERM: ankylosis after periodontal damage not located on Berman p84
- P3_ L34 BERM: as item 58: not located on Berman p84
- P3_ L36 HARTY: no treatment for established replacement resorption not located on Harty p266
- T01 L37 ANDR: pulp treatment options by exposure size not located on Andreasen p304 (text on p621 in another context)
- T01 L51 OGLE: IADT figures attributed to Ogle p158 not located on that page (IADT itself checked in the IADT audit)
- T01 L80 ANDR: calcium hydroxide capping preference not located on p302-303
- T01 L147 BERM: several-angle radiographs before reduction not located on p74
- T01 L151 BERM: repeat-tests pattern not located on Berman p74
- T01 L171 KOHLI: record contents not located on Kohli 609-611
- T01 L171 ANDR: record contents not located on Andreasen p475
- T02 L24 ANDR: progressive irreversible replacement resorption wording not located on Andreasen p412; Kohli p619 conflict recorded at item 17
- T02 L36 HARTY: no-effective-treatment wording not located on Harty p266; Kohli p619 fluoride point (item 18)
- T02 L46 ANDR: CES note: textbook view on replacement resorption not located on Andreasen p412; check the cited page
- T02 L56 BERM: intrusion re-eruption wording not located on Berman p80
- T02 L62 HARTY: no reliable treatment wording not located on Harty p266 (Kohli p619 fluoride point is supported)
- T03 L31 ANDR: early treatment and low contamination not located on Andreasen p482 (figure caption only)
- T03 L35 KOHLI: canal obliteration as favourable not on Kohli p619
- T03 L35 ANDR: favourable-outcome statement not located on Andreasen p413 or Kohli p619
- T03 L62 ANDR: as item 80: not located on Andreasen p482
- T04 L69 BERM: list claim not on Berman p84 (page discusses orthodontic extrusion timing)
- T05 L73 ANDR: Ellis class 4 wording not located on Andreasen p234
- T05 L75 BERM: sensibility at 6-8 weeks not located on Andreasen p320 or Berman p28-29
- T05 L83 ANDR: apexification or regenerative endodontics not located on Andreasen p304; Kohli p612 supports it
- T05 L87 ANDR: composite as conservative default not on Andreasen p304 (p304 discusses GIC bandage)
- T06 L45 BERM: composite as usual alternative not located on Berman p27
- T06 L62 HEXEM1: 18 years and growth completion not in Hexem p589; teenagers statement is on p586
- T07 L24 ANDR: monitoring for missed luxation not located on Andreasen p302
- T07 L58 BERM: Berman p181-182 is the law chapter; parent-communication statement is on Hexem p604 only
- T08 L48 KOHLI: CBCT statement not located on Kohli p610 (abbreviation list only)
- T08 L58 HEXEM2: implant/ridge statement not located on Hexem Part 2 p603
- T12 L33 ANDR: RCT options for coronal/apical fragments not located on Andreasen 355-368
- T14 L20 ANDR: replacement resorption after drying not located on Andreasen p486 (figure caption)
- T14 L35 INGLE: Ingle printed p383 is not in the extract; cannot verify
- T14 L72 INGLE: Ingle printed p383 not present in the extract; cannot verify
- T16 L38 ANDR: three-hour rule not located on Andreasen p477 in the extract; verify the source sentence
- T17 L42 HARTY: opposing view not located on Harty p234
- T18 L26 HARTY: scope statement not located on Harty p225 (p225 gives replantation definition)
- T18 L32 ANDR: protect the PDL and cementum not located on Andreasen p760 (p760 has healing statement)
- T19 L32 ANDR: monitor periodontal condition not located on Andreasen p702
- T20 L38 HARTY: management by class not located on Harty p63

**Quotations.** Four quoted phrases were checked verbatim. T14 milk phrase: not in the source (corrected). T14 Andreasen phrases: found on p.485 and p.487 (corrected). T16 Harty phrase: found on p.262 (confirmed). T14 'the most critical factor' (Harty p.260): found. T04 'the 15 to 40% / 15 to 61%' phrase is the answer's own wording; the 40% figure is in Andreasen (ch.13) and the 61% figure was not checked. T07 'without pulpal exposure' is generic wording, not on the cited pages.

**Resolver limits.** Andreasen 2007 and Harty's: the answers cite PDF pages, which are the printed page + 16 (checked on T15/T16 locators and five Harty's anchors). Ingle's: PDF page = printed - 39 (checked on the doxycycline passage). Cohen's: page markers used directly. DCNA journal pages from PDF offsets: Kohli and Lee +608; Ogle +150; Trope 2010 +312; Hexem and Eisler Part 2 +600; Hexem and Eisler Part 1 +585 (weakest fit: four claims). Matching is by word and number overlap, not reading, so a claim can match on a neighbouring sentence. The 466 automatic matches were not individually read.

**Bookkeeping error found and fixed.** The verdict records for 25 items were stored against the wrong file, line and source because the batch order changed during the review. The 25 were rebuilt from the printed listing and every flagged citation was re-matched by file, line and source before this section was written.


## Textbook audit completion (2026-10-19)

**Previously unaudited citations (30), now checked.** Sikri's Ellis classes 1-6 are on printed p.463 (cited as p.484 in the PDF-page convention) and match the answers. The Endodontic Radiology text supports the dens invaginatus statements (maxillary lateral incisors, invagination of the dental papilla, Oehlers classes I-III, the figure legend that none directly communicates with the pulp). The AAE glossary definition matches. Grossman's lists HBSS first among storage media and has a 'DENS IN DENTE' heading in Chapter 13. Principles and Practice names HBSS the most common storage medium and milk an excellent alternative.

**Previously unlocated claims, resolved by searching the whole source.** Supported on the cited page: Harty's p.266 (no treatment for replacement resorption), Berman p.84 (ankylosis after intrusion), Berman p.74 (several radiographic angles), Kohli p.616 (canal obliteration as a favourable response), Harty's p.234 (Weine's 'case against intentional replantation') and p.225 (transplantation definition), the three-hour rule (Andreasen p.477). Corrected: Ingle's 60-minute statement is on p.343, not 344; the Andreasen 400-tooth figures are on p.485 (this also reverses an earlier wrong 'unverifiable' note); the T03 revascularisation sentence now states what Andreasen p.481 says (contamination and drying bring resorption on earlier); the T06 growth sentence now states what Hexem p.586 says; the T01 calcium hydroxide liner sentence now states what Andreasen p.302-303 says; Kohli CBCT cited to p.611; Hexem Part 2 implants cited to p.602-603.

**Still unverified (20).** The extracts hold no sentence matching these; they are generic clinical statements or the answer's own synthesis, and should be read as such. They were not rewritten.
- P1_ L23 ANDR: exposure-record list not located on Andreasen p304
- T01 L37 ANDR: pulp treatment options by exposure size not located on Andreasen p304 (text on p621 in another context)
- T01 L51 OGLE: IADT figures attributed to Ogle p158 not located on that page (IADT itself checked in the IADT audit)
- T01 L151 BERM: repeat-tests pattern not located on Berman p74
- T01 L171 KOHLI: record contents not located on Kohli 609-611
- T01 L171 ANDR: record contents not located on Andreasen p475
- T02 L24 ANDR: progressive irreversible replacement resorption wording not located on Andreasen p412; Kohli p619 conflict recorded at item 17
- T02 L46 ANDR: CES note: textbook view on replacement resorption not located on Andreasen p412; check the cited page
- T02 L56 BERM: intrusion re-eruption wording not located on Berman p80
- T03 L35 ANDR: favourable-outcome statement not located on Andreasen p413 or Kohli p619
- T04 L69 BERM: list claim not on Berman p84 (page discusses orthodontic extrusion timing)
- T05 L75 BERM: sensibility at 6-8 weeks not located on Andreasen p320 or Berman p28-29
- T05 L83 ANDR: apexification or regenerative endodontics not located on Andreasen p304; Kohli p612 supports it
- T05 L87 ANDR: composite as conservative default not on Andreasen p304 (p304 discusses GIC bandage)
- T06 L45 BERM: composite as usual alternative not located on Berman p27
- T07 L24 ANDR: monitoring for missed luxation not located on Andreasen p302
- T07 L58 BERM: Berman p181-182 is the law chapter; parent-communication statement is on Hexem p604 only
- T12 L33 ANDR: RCT options for coronal/apical fragments not located on Andreasen 355-368
- T18 L32 ANDR: protect the PDL and cementum not located on Andreasen p760 (p760 has healing statement)
- T19 L32 ANDR: monitor periodontal condition not located on Andreasen p702

**Ellis class 4.** Sikri's text supports 'pulp status, not fracture pattern'; the Andreasen p.234 half of that citation is the WHO table only.

