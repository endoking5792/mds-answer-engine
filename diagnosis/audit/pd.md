# Audit ledger pd: second reader and Harty's audit (2026-11-06)

Answers: `canonical/B2_Diseases_of_Pulp_and_Their_Etiology_25m_CANONICAL.md` (25m) and `canonical/B3_Classification_of_Pulpal_and_Periapical_Disease_20m_CANONICAL.md` (20m). Locator file: `loc_pd.py`.

**Summary.** Every locator the drafts used was opened in context (259 keys; B2 about 200 cited, B3 about 95, with heavy overlap), with the surrounding paragraph read. About 245 held up as written. 17 corrections were made across the two answers. 50 new locator keys and 3 BOOK entries were added. Final exam cores: B2 994 words (range 850 to 1000), B3 789 words (range 680 to 800). `python3 locators.py pd_` gives checked 309, missing 0.

**Offsets and author lines confirmed.** Grossman's 14th Ch.4 and Ch.5 offset 25 (PDF 93 = printed 68); editor V. Gopikrishna (front matter). Sikri offset 21 (PDF 73 = 52). Ingle's Ch.8 offset -24 (PDF 191 = 215; PDF 194 = 218); the author line "P$/0 V. A11(&&" decodes as Paul V. Abbott with the same letter mapping that turns "E*+(+(*&'%," into "Endodontics" (o = "(", t = "&"). Torabinejad's Ch.1 offset 7 (PDF 11 = 4). Endodontic Prognosis Ch.3 offset 10 (PDF 51 = 41). Essential Endodontology offset 13 (PDF 16 = 3; PDF 72 = 59); Ch.3 author line Fouad and Khan. Harty's: Ch.3 Chandler and Chong (PDF 39 = 23), Ch.5 Duncan, Smith and Cooper (PDF 81 = 65), Ch.12 Sigurdsson and Bourguignon (PDF 251 = 235), Ch.13 Rotstein (PDF 279 = 263), Ch.14 Hülsmann and Chong (PDF 303 = 287). All are offset 16. Cohen's Ch.1 and Ch.14 and Seltzer and Bender remain offset None; not re-derived.

## B2 (25m): Task A

| # | Location | Finding | Evidence (book, PDF page, short phrase) | Action |
|---|---|---|---|---|
| 1 | S2 expl, "no iatrogenic heading" | Partly wrong. Grossman's Box 4.1 lists "Iatrogenic dental procedures" under mechanical trauma, and the text lists "the iatrogenic causes of dental injuries". It has no top-level heading. "Idiopathic" is used for internal resorption and for cracked-tooth pain "of apparently idiopathic origin", not for unexplained necrosis. | Grossman's PDF 78-79 "The iatrogenic causes of dental injuries include the following"; PDF 80 "apparently idiopathic origin"; Sikri PDF 70 "no apparent etiologic factor" | fixed. The explanation now says the headings are the answer's own grouping. The "Iatrogenic" and "Idiopathic" headings in S3 and the exam core are labelled "(this answer's grouping)" and "(own grouping)". |
| 2 | S7 expl, necrotic and infected pulp | The conflict holds. Grossman's Box 4.3 has three necrosis types, with no "pulpless and infected" category, and says the key feature is "there will be a periapical radiolucency". Abbott (Table 8-1) has a separate "pulpless and infected root canal system" and says the infected stage shows "no periapical changes". The time course was misstated: the canal becomes pulpless within 1 to 2 months, and the radiolucency then develops "over the next few months". | Grossman's PDF 91 Box 4.3, PDF 93; Ingle's PDF 195 Table 8-1, PDF 199 | kept; time course corrected |
| 3 | S5 expl, Sikri's "Grossman's classification" | The mismatch holds. Sikri lists hyperaemia, reversible symptomatic/asymptomatic, irreversible acute/chronic, calcific/atrophic/fibrous degeneration and coagulative/liquefactive/caseation necrosis. Grossman's 14th Box 4.3 has no hyperaemia or atrophy, and its necrosis types are necrobiosis, without infection and infected. Whether it copies an older edition is unverified. | Sikri PDF 74; Grossman's PDF 91 | kept [Likely] |
| 4 | S5 expl (new) | Sikri's version of Abbott differs from Ingle's Table 8-1. It adds atrophy and internal resorption (surface, inflammatory, replacement) under degenerative changes. It also renders necrobiosis as "necrotic and inflamed", where Ingle's and Grossman's say "necrotic and infected", probably a slip. | Sikri PDF 75; Ingle's PDF 195 | added |
| 5 | S5 expl, AAE 2009 vs 2016 | Not a real disagreement. Endodontic Prognosis reproduces the 2009 consensus (J Endod 2009;35:1634). Cohen's ref 6 is the AAE Glossary of Endodontic Terms, 9th ed 2016. The categories are identical. | Endo Prognosis PDF 46; Cohen's Ch.1 PDF 251 and ref list "Glossary of endodontic terms, ed 9 2016" | fixed (explained as two documents) |
| 6 | S3 expl, caries distance | All four figures verified. Torabinejad's: enamel caries attract inflammatory cells. Sikri: 1.0 mm. Harty's: "≈0.5 mm" for significant inflammatory cells. Cohen's: "RDT is less than 0.5 mm" gives an increasingly severe reaction. Kept the "different end points" reading [Likely]. | Torabinejad's PDF 11; Sikri PDF 78; Harty's Ch.5 PDF 82; Cohen's Ch.14 PDF 1864 | kept |
| 7 | S3 RDT, Sikri 2.0 mm vs Harty's 0.3 mm | Verified. Sikri: minimal effects at 2.0 mm or more. Harty's: some pulp damage occurs only below 0.3 mm in very deep cavities. These are different thresholds rather than strictly contradictory statements. The exam core cited "(Harty's)" instead of the author and year. | Sikri PDF 71; Harty's Ch.5 PDF 84 | exam core fixed to Duncan, Smith and Cooper, 2017; high-yield line corrected ("2 mm safe" was an overstatement) |
| 8 | S3 expl, chemical | "Harty's takes a different position" overstated the contrast. Sikri also says most restorative materials, properly used, do not damage the pulp. | Sikri PDF 72 "most restorative materials, if properly used" | fixed |
| 9 | S3 exam, chemical | Cavity cleansers were attributed to Sikri. They come from Torabinejad's. | Torabinejad's PDF 9 | fixed |
| 10 | S6 expl/exam, reversible pulpitis treatment | Understated. Abbott says reversible pulpitis "will normally require" conservative pulp therapy, not "where needed". This is a genuine conflict with Grossman's and Harty's, who rely on removing the cause. | Ingle's PDF 234; Grossman's PDF 85; Harty's Ch.3 PDF 51 | fixed (side by side) |
| 11 | S6 expl, Grossman's subtypes "following Abbott's definitions" | Grossman's defines acute and chronic reversible pulpitis by duration. Abbott defines them by onset, severity and urgency. | Grossman's PDF 84; Ingle's PDF 195 | reworded |
| 12 | S7 expl, caseation | Unreported conflict. Grossman's calls caseation "a form of coagulation necrosis". Sikri says it combines features of coagulation and liquefaction. | Grossman's PDF 94; Sikri PDF 82 | added |
| 13 | S8, pulp stone conflict | Partial only. Torabinejad's gives CVD and statins. Seltzer and Bender cite no relationship with "systemic diseases" (Gulsahi) and none with renal disease or carotid calcification. "Found" was changed to "report", since it is a review. | Torabinejad's PDF 16; Seltzer and Bender PDF 783 | reworded, flagged partial [Likely] |
| 14 | S8 exam | "embedded" stones and a "yellow crown" have no source in the books read. Grossman's describes free and attached stones and crown discoloration. | Grossman's PDF 92-93 | fixed |
| 15 | Synthesis | Ricucci 96.6%/84.4% verified in Ingle's, and the same figures appear in Cohen's Ch.14. "Inflammation often limited to one pulp horn" overgeneralised Essential Endodontology ("in some teeth"). Cohen's says infection was often localized to the coronal pulp. | Ingle's PDF 194; Cohen's Ch.14 PDF 1845; EE PDF 78 | fixed |
| 16 | S3 exam, idiopathic | Anachoresis was listed as "idiopathic", but it is a bacterial route. It is now framed as the suggested explanation for necrosis with no apparent cause. | Sikri PDF 70 | fixed |
| 17 | S1 | "Reparative dentine" (Sikri) had no locator. | Sikri PDF 69 | locator added |

**Checked and held up (B2):** about 185 further locators. These include Kakehashi (Grossman's/Torabinejad's), Miller 1894, species, routes, by-products, 20°C/30°C dry cutting, Cohen's 10°C/15% and 20°C/60%, crowns 10-15%/10 years, 15.6%/32.5%, cumulative insults, adrenaline, barodontalgia 5,000 ft, trauma adults vs children, intrusion worst, all reversible and irreversible pulpitis features, referred pain (Grossman's ear vs Sikri's pre/postauricular), EPT stages, polyp features, internal resorption, necrosis 40% vs 40-60%, gases, odour, Abbott's PCC terminology, atrophy, the WHO list in Sikri, and Gofung, Stock and Walton-Torabinejad.

## B2: Task B, Harty's additions and conflicts

| # | Section | Harty's chapter | Addition / conflict | Action |
|---|---|---|---|---|
| H1 | S3 microbial | Ch.5 Duncan; Ch.13 Rotstein | Periodontal route disputed. Duncan: no necrosis unless disease reaches the apex. Rotstein: controversial; degenerative changes; necrosis once recession opens an accessory canal. Sikri: deep pockets via lateral canals may cause total necrosis. | added side by side (expl; exam core flags "disputed") |
| H2 | S3 trauma | Ch.12 | Severity order: intrusion and avulsion > lateral luxation > extrusion > subluxation > concussion (agrees with Torabinejad's). Subluxation survival 90% immature, 75% mature. | added (expl) |
| H3 | S3 cracks | Ch.5; Ch.14 | Mandibular molars most affected. 20% of cracked teeth without spontaneous pain became necrotic. | added (expl) |
| H4 | S3 iatrogenic | Ch.5; Ch.13 | Orthodontic necrosis rare, effects reversible, canal calcification may increase. Root surface debridement response not severe, versus Torabinejad's (deep scaling injures apical vessels); Rotstein: curette may sever a lateral-canal vessel. Drying gives no permanent damage (vs Sikri). Lasers in cavity preparation have no long-term effects (vs Sikri). Implants can devitalise teeth. | added side by side (expl) |
| H5 | S6 irreversible pulpitis | Ch.3; Ch.14 | Treatment conflict. Harty's: pulp removal necessary once irreversible pulpitis is confirmed; emergency pulpotomy is "a temporary measure"; antibiotics have no role. This sides with Grossman's against Essential Endodontology and Cohen's (pulpotomy definitive in selected cases). | added (expl + exam core) |
| H6 | S6 internal resorption | Ch.12 | Rare complication of trauma; RCT as soon as possible arrests it. | added (expl) |
| H7 | S7 necrosis | Ch.3; Ch.12 | Conflict with Abbott's "monitor" for uninfected necrosis. Harty's: RCT once necrosis is confirmed; after trauma to a mature tooth, start within 7 to 10 days to prevent infection. Harty's defines necrosis by loss of blood supply. | added (expl + exam core) |
| H8 | S8 calcification | Ch.12; Ch.13; Ch.5 | Root canal obliteration is common and a favourable mode of healing; RCT only if pain or a radiolucency develops (agrees with Grossman's; uses the term Abbott rejects). Calcification also follows periodontal disease and orthodontic movement. | added (expl + exam core citation) |
| H9 | Synthesis | Ch.3 | "Poor correlation... especially true with irreversible pulpitis" stands against Ricucci's 84.4%. | added side by side |
| H10 | S6 reversible | Ch.3 | Causes caries and coronal leakage; removal relieves it (against Abbott's pulp therapy). Already cited: 5 to 10 s. | added |

Re-verified existing Harty's claims: Ch.3 no agreed terminology, conservative terms retained, 5 to 10 s, Aδ then C-fibre ache, uninfected necrosis with normal periapex, phoenix, drainage, GP tracing; Ch.5 microbial/chemical/mechanical, synchrony, caries decline, ≈0.5 mm, materials questioned, microleakage, bleaching, water spray, 0.3 mm, crowns 10-15%, adrenaline, trauma calcification or necrosis, occlusion negligible, bacterial infection most common. All held.

## B3 (20m): Task A

| # | Location | Finding | Evidence | Action |
|---|---|---|---|---|
| 1 | S2 expl, AAE date | Same as B2 #5 | as above | fixed |
| 2 | S3 expl/exam, Grossman's periapical terms | Grossman's Box 5.2 says "alveolar abscess", not "apical abscess", and equates secondary symptomatic apical periodontitis with the phoenix abscess. | Grossman's Ch.5 PDF 96-97 Box 5.2 | fixed (expl + exam table) |
| 3 | S3 expl, Sikri's WHO codes | Codes 4.4 to 4.8 verified, with 4.5 "granuloma". New finding: Sikri's 4.6 heading reads "with sinus to maxillary antrum" and then lists nasal, oral and skin sinuses. Ørstavik's footnote says K04.6 is subdivided by sinus site, so Sikri's heading appears to have absorbed one subdivision. Also missing the "K0" prefix. | Sikri Ch.6 PDF 85; EE PDF 15 Table 1.1 | added [Likely] |
| 4 | S3 expl | Ørstavik also treats condensing osteitis as a variant of AAP/chronic AP, which agrees with Abbott. | EE PDF 15 | added |
| 5 | S6 expl/exam, reversible pulpitis | Same as B2 #10 | as above | fixed |
| 6 | Synthesis | Same as B2 #15 | as above | fixed |

**Checked and held up (B3):** about 90 locators, including Abbott's criteria and the 13 classifications, Gutmann's quotation, Tables 8-1 and 8-2 (cysts, scar, cellulitis, extra-radicular infection), Grossman's histopathologic classification, primary vs secondary SAP, percussion as the key sign, Cohen's AAE definitions (SAP, AAP, AAA febrile, CAA sinus), Sundqvist, cysts 7-54%, cysts and granulomas healing alike, true cysts possibly needing surgery, "pocket cysts only histologically", enostosis, nonendodontic lesions, sinus tracts healing, condensing osteitis, scar review, prognosis best for irreversible pulpitis, and Ingle's older painful/non-painful scheme (in Sikri).

## B3: Task B, Harty's additions and conflicts

| # | Section | Harty's chapter | Addition / conflict | Action |
|---|---|---|---|---|
| H1 | S2 expl | Ch.3 | Harty's own short scheme with acute/chronic terms (pulp: normal, reversible, irreversible, necrosis; periapex: normal, acute AP, acute periapical abscess, chronic AP with phoenix, chronic periapical abscess) | added (expl) |
| H2 | S6 | Ch.3; Ch.14 | Irreversible pulpitis: pulp removal necessary, emergency pulpotomy temporary, no antibiotics. This conflicts with the pulpotomy-as-definitive position. | added (expl + exam table) |
| H3 | S6 | Ch.3; Ch.12 | Necrosis: RCT once confirmed (vs Abbott's monitor); 7 to 10 days after trauma | added (expl + exam table) |
| H4 | S6 | Ch.14 | Antibiotics without drainage incorrect (supports the high-yield line) | added (expl) |
| H5 | S6 | Ch.3 | Reversible pulpitis: removal of the cause (vs Abbott) | added (expl + exam table) |
| H6 | Synthesis | Ch.3 | Poor correlation, especially with irreversible pulpitis | added |

## Open points for Niranjan
1. The treatment of irreversible pulpitis is now shown as a three-way disagreement: pulpectomy, with pulpotomy only as an emergency measure (Grossman's, Harty's), versus pulpotomy as a definitive option in selected cases (Essential Endodontology, Cohen's). Abbott's position, RCT as first choice, sits close to the first group. Examiners may expect one line on vital pulp therapy for irreversible pulpitis.
2. Necrosis without infection: Abbott says monitor; Harty's says RCT (within 7 to 10 days after trauma in mature teeth). The exam cores now show both.
3. Two points rest on inference and are kept [Likely]: Sikri's "Grossman's classification" reproduces an older Grossman's edition, and Sikri's WHO code 4.6 heading is a mis-rendering. Neither was checked against an older Grossman's edition or the ICD-10 text.
4. The B2 exam core is at 994 of 1000 words. Any further additions need matching cuts.
5. Cohen's chapter offsets remain None.
