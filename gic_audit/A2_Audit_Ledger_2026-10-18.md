# A2. Audit ledger: glass_ionomer_cement, locator follow-up (2026-10-18)

**Scope:** locator check of every GIC source line (P1-P10, Q01-Q16, Q11b) against the textbooks in `mds-textbooks` and the vault chapterwise copies. This pass checks that each cited phrase is on the cited page. It does not re-read every claim; the A1 reader audit (2026-10-16) covers claim-level reading.

## Result
- 1,749 source lines checked. 1,736 pass: 1,684 have the phrase on the cited page under one of two page-marker conventions (see below); 52 cite files that carry no page markers and were checked file-wide.
- 7 fail, 6 cite study notes or dossier entries rather than textbooks.

## Fixed in this pass
- **Q01, RMGI date:** the "(Sakaguchi et al, 2019*)" study-note citation is replaced by Craig 14th ed, PDF p.146, "RMGIs were invented in the late 1980s".
- **Q01, Ngo 2010:** the sentence "The total water content of the set cement is somewhere between 11% and 24%." was verified on the DCNA PDF (p.2) and the locator now cites the PDF directly, replacing the dossier entry.
- **P4, Michigan 2002 quote:** the quoted wording now matches the source ("These cements also can be etched to"). The page (636) is kept because it follows this file's marker convention.

## Open (needs a decision; not changed)
- **P1 line 190**, "Water spray cooling is not recommended" (Sikri, cited 28_20 p.480). The chapter 28_20 runs pp.406-424 and the phrase is not in the Sikri text. P1 line 39 relies on the same claim ("no water spray (Sikri, 2020)"). The sentence may be unsupported.
- **P2 line 145**, "the finishing can be started earlier" (Sikri p.478). Not in the text. "Within 10 minutes" (P2 line 33) is also not in the text. The Sikri text has a related passage at p.461 ("finishing after one day ... delayed finishing after one week") whose context was not verified against the GIC claim.
- **P2 line 110 and Q11 line 143**, study-note citations (Sakaguchi 2019). Q11's "command set" claim has no matching RMGI passage: Craig p.300 "cure on command" refers to composites.
- **Q01 line 528**, study-note citation (Mount 1994, p.17). The claim is not located in the body.
- **Q11 line 187**, Potiprapanpong 2023 from the dossier. Abstract only; the quote was not re-checked.
- **P4 lines 162-165**, Atlas Chapter 5 (Type III lining). The four phrases are in the text but interleaved with the other column of a two-column scan, so they do not match as one string. They need a page read.

## Page-marker convention (resolved for 28_20; a formatting difference)
Vault chapterwise conversions place the "PDF page N" marker either at the end of page N (for example `28_20_Glass_Ionomer_Cement`, `23_ch_20_cements`) or at its start (the mds-textbooks convention). This is a difference in marker placement, not in page numbering. Each GIC citation matches the convention of its own file, so the answers are internally consistent.
Checked in the source PDF (Textbook of Conservative & Restorative Dentistry, 666 pages): PDF page 406 holds "Glass-ionomer cement, developed by Wilson and Kent (1972)" (printed page 387, so printed = PDF page minus 19). The vault copy (marker at end) and the mds-textbooks copy (marker at start) both give page 406 for that sentence. The P1/P2 out-of-range lines below are not affected by this, because their pages (478, 480) lie outside the chapter's pages (406-424).

## Attribution
The "Sikri, 2020" labels for the Textbook of Conservative and Restorative Dentistry are consistent with its front matter, which lists the author's other CBS books.

## Not done
- No sentence-level re-reading of GIC claims in this pass.
- Sturdevant 5th ed is still not in the library (its lines match against the vault's 5th-ed copy).

## Addendum (2026-10-18): manual page read and sentence-level triage
- **P4 lines 137 and 162-165, read on the source pages.** Atlas OCR PDF pp.88, 89 and 93 (printed 77, 78, 82) and Michigan 2002 p.636 (printed 627). All four Atlas phrases and the "4.9 MPa. These cements also can be etched to" line are on those pages. Michigan p.635 (printed 626) gives the subject of line 18: "Bond strengths measured in tension vary from 2.0 to 4.9 MPa". The mechanical checker still reports the Atlas lines NOT_FOUND because the vault chapterwise file interleaves the two columns.
- **P4 line 165 quote** now carries the full source wording, "10-15-second application of 10% poly(acrylic acid) to remove the smear layer". The earlier quote dropped "10-15-".
- **Sentence-level triage (all cited sentences).** 68 flags. 15 NUMBER and 10 LOWOVERLAP flags were read against the cited pages. 43 NO-LOCATOR flags were not read individually: they are labels written without a comma ("Ritter 2019"), comparison tables, and meta statements.
  - Supported on the page: Sikri 152 MPa, 48 KHN and 16,000-22,000 psi; Mount 4.5% and 15% residual HEMA; Bonsor 3-4% shrinkage; Mount 15-25% resin; Torres 0.2-1 mm liner; Anusavice 7-10 min and 0.75 mm base; Roberson 24-72 h and 30 days; Bhat 105 MPa, 20 MPa and 40 KHN; Mount 8 mm cavity; McCabe 30 days; Sikri core build-up; Banerjee "longer periods" discolouration; Sikri acid-base setting for conventional GIC.
  - Fixed: P1 "Colour stability 'might be suspect over longer periods'" replaces a reworded phrase in quote marks. Q06 "late 1970s" removed from the section heading and the Copolymers table cell (the cited source does not give that date). Q02 Banerjee "shorter lifespan" (not on the cited pages) is marked [Guessing].
  - Not verified: Q01 van Noort "low-load" restriction (not on the cited p.110).
- **Still open:** P1 line 190 and P2 line 145 (Sikri, out of chapter, not in the text); Q01 line 528 (Mount study note); P2 line 110 and Q11 line 143 (study notes); Q11 line 187 (dossier, abstract only).
