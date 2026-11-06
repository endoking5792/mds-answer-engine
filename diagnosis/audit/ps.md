# Second-reader audit: group `ps` (B6 Periapical cysts, B7 Sinuses of endodontic origin)

Reviewer pass 2026-11-06. Method: every `ps_` locator used by B6 and B7 was opened in its chapter with about 250 to 600 characters of surrounding text and read against the sentence that cites it. The author line was checked once per chapter and the offset at two places. Harty's Ch.3, 8, 10 and 13 were re-read in full for cyst and sinus-tract content, and Harty's Ch.1, 9, 11, 12 and 14 were searched. Seltzer and Bender 2nd ed and Endodontology (Baumann and Beer) were searched and read for cyst and sinus-tract content. `python3 locators.py ps_` gives `checked 235 missing 0`.

## Chapter author lines and offsets confirmed

| Book, chapter | Author(s) as cited | Offset check |
|---|---|---|
| Ingle's 7th Ch.6 | Ricucci, Rôças and Siqueira, 2019. The author line in the file is garbled, so the names were confirmed from the contents page ("Domenico Ricucci, Isabela N. Rôças, José F. Siqueira, Jr.", p.167) | -24 (PDF 143 = p.167) |
| Ingle's 7th Ch.30 | Baumgartner and Rosenberg, 2019 (contents page: "J. Craig Baumgartner, Paul A. Rosenberg", p.963) | -118 (PDF 845 = p.963; PDF 852 = p.970) |
| Cohen's 12th Ch.1, 3, 16 | Berman and Rotstein; Landwehr; Lin and Huang (chapter first lines) | none (no printed numbers) |
| Grossman's 14th Ch.5 | Gopikrishna (ed), 2021; Wolters Kluwer Health (India), copyright 2021 confirmed | 25 |
| Endodontics: Principles and Practice 6th Ch.1 / Ch.4 | Sedgley, Silva and Fouad / Blicher, Walton and Torabinejad (chapter first lines) | 7 (Ch.4: PDF 68 = p.61, PDF 80 = p.73) |
| Essential Endodontology 3rd Ch.3 | Fouad and Khan | 13 |
| Endodontic Radiology 2nd Ch.7, 8, 11, 15, 16, 19, 21 | Torneck; Lam; Lai and Basrani; Kishen and Messer; Ørstavik; Cotti and Campisi; Estrela, Bueno and Alencar (contents page) | 20 (Ch.11: PDF 186 = p.166, PDF 188 = p.168; Ch.15: PDF 255 = p.235, PDF 267 = p.247) |
| Sikri 2nd Ch.6 / Ch.7 | Sikri, 2019; CBS, 2nd eBook ed. 2019 confirmed | 21 (Ch.7: PDF 108 = p.87) |
| Harty's 7th Ch.3 / 8 / 9 / 10 / 12 / 13 | Chandler and Chong / Siqueira and Rôças / Chandler / Gutmann / Sigurdsson and Bourguignon / Rotstein; copyright 2017 | 16 at two pages each (Ch.3 PDF 39 = p.23; Ch.8 PDF 145 = p.129; Ch.9 PDF 167 = p.151, PDF 189 = p.173; Ch.10 PDF 195 = p.179; Ch.12 PDF 251 = p.235, PDF 260 = p.244; Ch.13 PDF 279 = p.263, PDF 285 = p.269) |
| Seltzer and Bender 2nd Ch.16 | Rotstein and Simon, 2012 (contents page; Quintessence, copyright 2012) | none (file has PDF markers only) |
| Endodontology Ch.2 | Beer, 2010 (contents page "R. Beer"; English translation of the 2nd German edition, copyright 2010) | 17 (PDF 24 = p.7, PDF 37 = p.20) |
| Weine 6th Ch.2 | Weine, 2004 (6th edition, Mosby, copyright 2004 confirmed) | none |

## B6 Periapical cysts

About 125 cited sentences checked; 10 corrected or qualified; the rest held up.

| # | Location (section) | Finding | Evidence (book, PDF page, short phrase) | Action |
|---|---|---|---|---|
| 1 | 1, incidence table and exam core | Landwehr's 6% to 55% is worded as the incidence of "periapical cysts and periapical granulomas", not of cysts alone | Cohen's Ch.3, PDF 454, "incidence of periapical cysts and periapical granulomas is highly variable" | fixed: the table quotes the wording; the exam core now cites Gopikrishna (Grossman's states it for cysts) |
| 2 | 1, Lin and Huang 15% to 20% | Holds; it applies to lesions from extracted teeth | Cohen's Ch.16, PDF 2082 | kept |
| 3 | 1, Sedgley et al 7% to 54% | Holds | E:P&P Ch.1, PDF 20, "from 7% to 54% of apical lesions" | kept |
| 4 | 1, Nair 15% = 9% true + 6% pocket | Holds (Estrela et al); Ricucci et al give the 15/50/35 split | ER Ch.21, PDF 327; Ingle Ch.6, PDF 158 | kept |
| 5 | 1, Bhaskar 2,308 vs 2400 | The conflict is real: Ricucci et al and Fouad and Khan give 2,308; Grossman's table gives 2400; the percentages agree | Ingle Ch.6 PDF 158; EE Table 3.3 PDF 88; Grossman Table 5.3 PDF 118 | kept |
| 6 | 1, Patterson 84% vs 20% flag | The flag stands, but the reasoning was weak: Fouad and Khan's table has no "other" column, and other rows also fall short of 100% (Bhaskar 90, Koivisto 73) | EE Table 3.3 PDF 88; Grossman Table 5.3 PDF 118 | fixed: the reasoning now rests on 66% being unaccounted for, far more than any other row; [Likely] kept |
| 7 | 2, osmotic-pressure conflict | The conflict exists, but Ricucci et al were misdescribed: they set the decompression evidence for the osmotic idea against the growth of open pocket cysts, and say pro-resorptive mediators "could be the main factor" | Ingle Ch.6 PDF 164 to 165 | fixed: three positions now shown. For osmotic pressure: Beer 2010 and Baumgartner and Rosenberg. Against: Lin and Huang. Weighing both: Ricucci et al |
| 8 | 5, "Lin and Huang take both positions" | Overstated. In the outcomes paragraph they say "no direct evidence" either way. They then state the self-sustaining, surgery-needed view (citing ref 191) and counter it at once ("Nonetheless ... should be able to heal"). Their healing section predicts regression by apoptosis | Cohen's Ch.16 PDF 2088 and 2103 | fixed: their stance is shown as a sequence; they are placed on the "may heal" side [Likely] |
| 9 | 3, Sikri "acute inflammatory cyst" | The error holds. It is stronger than stated: the sentence just before it calls the cyst "a chronic inflammatory response" | Sikri Ch.6 PDF 93 | fixed (strengthened) |
| 10 | 5, Sikri "surgical removal ... (marsupialization)" | The error holds: marsupialisation is exteriorisation and decompression (Glossary) | Sikri Ch.6 PDF 94; Glossary p.33 | kept |
| 11 | 4, Sikri's sclerotic border vs Ørstavik and Torneck | The conflict holds. Sikri is also inconsistent with himself: his body text lists the band only among features that "may suggest" a cyst, while his key-features box calls it "a diagnostic feature". Landwehr adds "irrespective of the size or cortication" | Sikri Ch.6 PDF 93 to 94; Cohen's Ch.3 PDF 451 | fixed (added) |
| 12 | 5, healing 80% to 98% | A qualifier was stripped. Grossman's figure is for "areas of rarefaction" in general ("a percentage of these ... may be cysts"); the exam core read as if it were for cysts | Grossman PDF 122 | fixed in the explanation and the exam core ("Periapical lesions heal in 80 to 98%") |
| 13 | 5, cysts heal more slowly | A qualifier was stripped: Torneck says "Subjectively, radiographic evidence appears to suggest" | ER Ch.7 PDF 114 | fixed |
| 14 | 5, Gutmann "cyst indication eliminated" | A qualifier was stripped: advances "have eliminated most of these indications" | Harty's Ch.10 PDF 196 | fixed |
| 15 | 5, Enislidis cohort "best evidence" | A qualifier was stripped: "perhaps the best evidence" | Ingle Ch.30 PDF 852 | fixed |
| 16 | 5, true-cyst conflict | Holds. Two voices on the "surgery" side were missing: Rotstein and Simon (Seltzer and Bender), "True cysts must be surgically removed", and Baumgartner and Rosenberg, cysts "truly independent ... nonsurgical ... may no longer be enough" | S&B Ch.16 PDF 686; Ingle Ch.30 PDF 852 | added |
| 17 | 4, CT, CBCT 76%, ultrasound, MSCT, albumin and globulin, electrophoresis | All hold | ER Ch.19 PDF 313; Cohen's Ch.3 PDF 452 to 453; Ingle Ch.30 PDF 852 | kept |
| 18 | 2, theories and three stages | Hold; Grossman's gives the same four theories and three stages | Grossman PDF 118 to 119 | kept |
| 19 | REFERENCES | Grossman's and Sikri publisher and year were marked "not re-verified" | front matter of both | fixed (confirmed) |

**Additions (Task B and other books):**
- Seltzer and Bender Ch.16 (Rotstein and Simon, 2012): Simon's estimate that true cysts are probably under 10% (incidence table and conflict box); on curetted tissue a bay cyst and a true cyst can give the same diagnosis (Section 3); Valderhaug found no cyst in monkeys until at least 6 months after necrosis (Section 2); true cysts must be surgically removed (conflict box).
- Endodontology Ch.2 (Beer, 2010): the third phase results from "osmotic and resorption-stimulating factors" (osmotic conflict). The cyst-wall details in that chapter are figure legends and were not used.

**Harty's additions and conflicts (B6):**
- Ch.3 (Chandler and Chong): no cyst passage (0 hits); confirmed.
- Ch.8 (Siqueira and Rôças): "weeping canal ... pocket cyst" re-verified (PDF 157). Added: apical canal biofilms were commoner in teeth with large lesions, especially those with a cyst (PDF 147). This sits on the infection-driven side of the true-cyst conflict.
- Ch.10 (Gutmann): the 0.7% to 5.0% "other" lesions were re-verified; "most of" was restored. Added: Table 10-6 lists "Recurrent cystic lesion" among the valid causes of surgical failure.
- Ch.13 (Rotstein): cysts appear only in its reference list.
- No Harty's statement contradicts the answer.

**Exam core (B6):** 393 words before, 398 after. Changes: the incidence citation now goes to Gopikrishna; stage 3 now reads "osmotic pressure (Beer, 2010; rejected by Lin and Huang, 2021)"; the healing line was qualified; Rotstein and Simon replaces Ørstavik on the "surgery" side of the controversy; to make room, "with serial sections" was cut from the Definitive line.

## B7 Sinuses of endodontic origin

About 72 cited sentences checked; 7 corrected or qualified; the [RECALL] was removed; the rest held up.

| # | Location (section) | Finding | Evidence | Action |
|---|---|---|---|---|
| 1 | 1, fistula vs sinus tract | Holds: the Glossary (p.23, p.46) and Cohen's Ch.1 (PDF 210) call "fistula" inappropriate; Weine uses "(fistulas)" (PDF 181). More books use "fistula": Harty's Ch.12 (Sigurdsson and Bourguignon) lists it among the signs of necrosis; Lai and Basrani write "Fistula tracking" | Harty's Ch.12 PDF 270; ER Ch.11 PDF 193 | added |
| 2 | 1, Sikri's definition | Sikri contradicts himself: the Ch.6 glossary has "A tract leading to a suppurating cavity", while the Ch.7 definition matches the AAE | Sikri Ch.6 PDF 86; Ch.7 PDF 107 | added |
| 3 | 2, "always" shows a tract (Lin and Huang) | Holds. Harty's Ch.3 says "usually" | Harty's Ch.3 PDF 52 | added side by side |
| 4 | 3, extraoral tracts | A qualifier was stripped: Sedgley et al say "In rare instances" | E:P&P Ch.1 PDF 21 | fixed (explanation and exam table) |
| 5 | 3, "particularly in a young person" | Conflict found: Sikri Ch.7 says cutaneous tracts are "seen more often in adults than in children" | Grossman PDF 106; Sikri Ch.7 PDF 108 | added as a conflict box; "Young patients" removed from the exam table |
| 6 | 3, site frequencies | Added from Sikri Ch.7 (Slutzky-Goldberg et al): buccal 82.4%, lingual or palatal 12.0%; maxillary 63.1% and mandibular 38.9%. The last two sum to 102%, so a misprint is likely. Cutaneous: chin and cheek, 80% mandibular | Sikri Ch.7 PDF 108 | added, flagged [Likely] |
| 7 | 5, [RECALL] "skin infection or tumour" | No book read lists the skin lesions that mimic a cutaneous tract. Searched: Cohen's Ch.1 and Ch.3, Ingle's Ch.6, Endodontic Radiology (all), Sikri Ch.6 and 7, E:P&P Ch.4, Guidebook to Molar Endodontics, Problems in Endodontics, Seltzer and Bender, Endodontology. Nothing could be converted | grep across `~/mds-textbooks` | removed; replaced by sourced non-endodontic causes: osteomyelitis (Blicher et al), MRONJ fistula criterion (Landwehr), oral syphilis (Weine); plus "dental infection first suspect" (Sikri Ch.7) |
| 8 | 5, Gutmann and Lovdahl "probe vertically only" | A qualifier was stripped: "tend to ... but in some cases ... tortuous path" | PS in Endo Ch.4 PDF 88 | fixed |
| 9 | 5, multiple tracts = fracture | Holds; Kishen and Messer add that buccal plus lingual tracts strongly suggest a VRF | ER Ch.15 PDF 256 | added |
| 10 | 7, time to closure conflict | Weine's "heals within a few days" is a figure legend. Rotstein's "a few weeks" is specifically for a tract into the sulcus or furcation | Weine Ch.2 PDF 181 (legend); Harty's Ch.13 PDF 282 | fixed: Weine dropped from the box (locator `ps_wei_few` deleted); Rotstein qualified by site; Rotstein and Simon "early stage" added; [Guessing] note on site |
| 11 | 7, extraoral management conflict | Holds, but Sikri Ch.7 narrows his own Ch.6 advice: cutaneous tracts "require no special therapy", but fibrosis of an older tract "is not uncommon" and then needs surgical removal | Sikri Ch.7 PDF 108 | added; exam core now "excise only an old fibrosed tract" |
| 12 | 4, tracing | Holds (Berman and Rotstein PDF 211; Ricucci et al PDF 157; Chandler and Chong PDF 52). Added: water-soluble radiopaque media (Sikri Ch.7) and CBCT (Blicher et al) | Sikri Ch.7 PDF 108; E:P&P Ch.4 PDF 70 | added |
| 13 | 6, histology 1 of 10 and two thirds | Holds | Cohen's Ch.1 PDF 210 | kept |

**Harty's additions and conflicts (B7):**
- Ch.3 (Chandler and Chong): tracing and the narrow marginal defect re-verified (PDF 52). Added: "usually" set against Lin and Huang's "always".
- Ch.13 (Rotstein): the mimic, the narrow probe, "a few weeks" and failure of periodontal treatment were re-verified (PDF 282). "A few weeks" is now qualified to sulcular or furcal tracts. Added: an untreated suppurating endodontic lesion may become secondarily involved with marginal periodontal breakdown (PDF 283 to 284).
- Ch.9 (Chandler, 2017), new: a tract that disappears after preparation and dressing does not mean success can be declared.
- Ch.12 (Sigurdsson and Bourguignon, 2017), new: "fistula" used as a sign of necrosis (terminology box).
- Ch.10 (Gutmann): only a table row ("Recurrent sinus tract or swelling" = clinical failure after surgery); not added for lack of room. Ch.1: historical only, not cited. Ch.11 and 14: passing mentions only.

**Exam core (B7):** 392 words before, 396 after. Added: the non-endodontic tract line (osteomyelitis, MRONJ, "suspect a tooth first"), "Rare; beyond facial muscle insertions" and "excise only an old fibrosed tract". Cut to make room: "gently", "periapical", the misdiagnosis sentence (shortened) and the [RECALL] clause.

## Open points for Niranjan
1. Patterson et al: whether the granuloma figure is 84% (Grossman's) or 20% (Fouad and Khan) can only be settled from the 1964 paper; the answer keeps it flagged as a probable slip [Likely].
2. Sikri Ch.7 quotes Slutzky-Goldberg et al with maxillary 63.1% plus mandibular 38.9%, which is 102%; the original paper is needed to say which figure is wrong.
3. Age of patients with cutaneous tracts: Grossman's says young people and Sikri says adults; neither cites a source.
4. Ricucci et al place themselves on the "no reason to expect a difference" side, yet on the same page they list true cysts with cholesterol among possible non-microbial causes of post-treatment disease (Ingle Ch.6, PDF 165). This was left as is; see whether you want it noted.
5. The new locators were appended at the end of each `<!--LOC-->` line, so the SOURCE LIST order no longer follows the text order exactly. This is cosmetic.
6. During this pass `loc_pa.py` (another group's file) briefly had a syntax error that stopped `locators.py`; it cleared on retry. It was not touched.
