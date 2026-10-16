# A1. Audit ledger: glass_ionomer_cement (2026-10-16)

**Marks: n/a (reviewer ledger)**

**Scope:** all 26 published glass-ionomer answers (P1-P9, Q01-Q16, Q11b) re-checked against the textbooks in the private repo `endoking5792/mds-textbooks` (37 operative and dental-materials books in one file each, plus the chapterwise endodontic books). One new predicted answer (P10, silver diamine fluoride and remineralisation) was added from the same books.

## Method
- **Sentence-level reading (17 parallel readers).** 11 readers took every cited sentence, bullet and table cell in the existing answers, found the passage in the cited chapter and judged whether the book says what the answer says. 6 readers then read the GIC chapters the answers had cited little or never and compared them with the answers. 3 more readers covered books that are new in `mds-textbooks`: the preclinical conservative texts, Sturdevant's 2nd South Asia edition, Goldstein, Braga (Oral Biofilms), Essentials of Dental Caries, and others.
- **Mechanical checks (by script).** Every source-locator line (phrase, book, PDF page) was searched in the `mds-textbooks` files; every cited figure with a unit was searched near its locator; all patched files were re-checked for structure, tables and locators.
- **Disagreeing sources:** where books differ, each author, edition and year is named and what each says is shown side by side. No source is ranked above another.

## Result
- **Locators:** 1,724 locator lines in the patched answers checked against the canonical books; 1,699 match the stated PDF page exactly, 7 are endodontic chapterwise files (phrase present, no page markers), 16 cite Sturdevant's 5th edition (Roberson et al, 2006; see limits), 1 is a Craig/Michigan 2002 two-column scan where the sentence is on the page (P4, 4.9 MPa), 1 is a phrase that also occurs in the 2nd South Asia edition at another page. In the original answers, 22 Sikri Ch.20 citations were one page above the marker (pages 408, 415, 421, 423) and were corrected.
- **Figures:** 403 cited figures with units checked near their locators; no figure was wrong. Sentences judged supported by their cited source: roughly 85% of about 1,800 reader-checked statements. About 260 problems were logged in the existing answers; none was a contradicted number. They were mostly attribution, overstatement, omitted caveats, internal differences between answers, and single-book values where books differ.
- **Edits applied:** more than 400 edits across the 26 answers (corrections, side-by-side author statements, added facts) plus the new P10; each answer has an `S-AUDIT` addendum before Exam Mode listing what was corrected, which sources disagree, what was added, and what was checked and kept. Exam Mode lengths grew by 10 to 29 percent because the side-by-side statements need words (Q10, Q16 and P1-P3 are the longest increases).

## Source disagreements now shown (author, edition and year are named in the answers)
- Year GIC was reported: 1972 (Mount et al; Sturdevant; Pickard; Sikri Ch.20; van Noort), 1971 (Sikri Ch.1), 1969 (Hill 2007); first commercial product 1976 (van Noort; Mount et al).
- Working time: 1.5 minutes (Bhat) to 2-3 minutes (Sikri); strength and hardness: Sikri, Mount, Phillips and Bhat values side by side (psi converted to MPa).
- Polyacrylic acid conditioner: 10% for 10 s (Mount; Pickard text), 20% for 10-20 s (Sikri Ch.20), 8-10 s (Sikri Ch.12), 15-30 s (Torres), 10% for 20 s (Ritter 2019).
- Fluoride release time course: about 24 hours (Sturdevant 2nd South Asia ed), 2 days then to 3 years (Brambilla and Ionescu 2021), about 3 weeks (Forsten via Summitt), 8-10 weeks (Pickard), 2-3 months (Mount).
- Etching set GIC under composite (5, 15 or 20 s; Bonsor, McCabe, Mount, Torres, Sikri); finishing time by GIC type; liner and base thickness; GIC over a pulp exposure; GIC as a core; compomer fluoride, etching and shrinkage; cermet status; sealant position (Mount and Phillips); redox, dual-cure and tri-cure definitions (Mount against Sikri, Bhat, Bonsor and Craig).
- SDF concentration: about 30% (Craig 14e) and 38% (Sikri; Ritter 2019).

## Added
- P10 (new, predicted): silver diamine fluoride, CPP-ACP, P11-4 and GIC in remineralisation, from Hill and Gillam, Craig 14e, Sikri, Ritter 2019, Braga 2021, Brambilla and Ionescu 2021.
- Facts added to existing answers include: Phillips fracture toughness and ART survival figures, surface-protection and mixing rules, varnish never placed under GIC (Garg and Garg; Singh), selective caries removal and ITR criteria (Q09), Braga's qualification of GIC antibacterial and remineralisation claims, pKa of polyacrylic acid (Nakabayashi and Pashley).

## Limits (what this ledger does not establish)
- **Sturdevant:** the answers cite the 5th edition (Roberson et al, 2006), which is not in `mds-textbooks` (it holds the 2nd South Asia edition, Ritter et al, 2019). 16 locators were checked against the older chapterwise 5th-edition copy; the 2nd-edition wording is shown beside the 5th where it differs or is silent.
- **Journal papers** (Ge 2023, Justen 2024, Frencken 2021, Miletic 2024, Oliveira 2019 as quoted by Hill and Gillam, and others) were checked only at abstract or quoted-table level.
- Phillips tables 14-2, 14-7 and 14-8 are garbled in the markdown; only the readable parts were quoted.
- The Dental Material Science Exam Manual is a secondary source and was not used to override any textbook.
- Reader reports are model-written. Every change was verified in the book by the patch writer; two samples were re-read in the book by hand (P10's silver diamine fluoride versus high-viscosity GIC statement from Hill and Gillam's table of Oliveira et al 2019; Q02's liner and resin-modified base statements against Sturdevant 2nd South Asia edition p.163). The locator and figure checks above cover the rest mechanically; not every one of the 400+ edits was re-read by a person.
