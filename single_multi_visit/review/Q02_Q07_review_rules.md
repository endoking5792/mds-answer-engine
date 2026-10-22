# Q2-Q7 review: rules compliance, examiner coverage and cross-question consistency (2026-10-22)

Read-only review of `canonical/Q02`-`Q07` `*_CANONICAL.md`. Exam-core words were re-counted by script with Q1's method (each `#### ✎ Exam core` block up to the next `---` or heading of level 2 or 3; a first pass that stopped only at level-2 headings double-counted Q3's `###` subsections, so the corrected counter is used below). Every phrase quoted as evidence was located by script on the stated PDF page.

## Summary table

| Q | Marks | Exam core (re-counted) | Range | In range | Locators | Refs alphabetical | Citations ↔ refs |
|---|---|---|---|---|---|---|---|
| Q2 | 50 | 1752 | 1700-2000 | yes | 47 + 6 LIT | yes | match |
| Q3 | 50 | 1709 | 1700-2000 | yes (9 words above floor) | 39 + 6 LIT | yes (Siqueira entries in year order 2015, 2022a, 2022b) | match |
| Q4 | 20 | 711 | 680-800 | yes | 39 + 3 LIT | yes | match |
| Q5 | 20 | 682 | 680-800 | yes (2 words above floor) | 34 + 1 LIT | yes (Siqueira 2017, 2022a, 2022b) | match |
| Q6 | 10 | 342 | 320-400 | yes | 19 + 3 LIT | yes | match |
| Q7 | 10 | 342 | 320-400 | yes | 18 + 1 LIT | yes | match |

Headings are verbatim and repeats are listed where they exist. "Trope 1991" and "Sjögren et al (1997)" appear as in-text names but are correctly marked as reported in Sikri or Baumann and Beer, not as stand-alone references.

---

## HIGH (cross-question consistency; fix before the topic .docx)

1. **The overstatement corrected in Q1 is still present in Q2 and Q3.** "more pain in the first week after SVE ... mainly in vital teeth" appears at Q2 line 178, Q2 synthesis line 253, and the Q3 synthesis (line 227). The Q1 source review showed the vital-teeth subgroup was only 2 studies (316 teeth), that an equal subgroup with mechanical instrumentation showed the same excess, and that pain *at* one week did not differ (RR 1.05).
   - Fix: use Q1's wording: "seen in small subgroups of vital teeth and mechanical instrumentation; pain at the one-week time point itself did not differ (Mergoni et al, 2022)".

2. **"Standard of care" for vital teeth survives in Q2.** Q1 softened it because Harty's says only "preferably in a single visit if feasible".
   - Fix: use "generally accepted; preferred where feasible (Siqueira and Rôças, 2017)".

3. **Chapter authors are recoverable, so the "cited by editors" statements in Q1-Q7 audit blocks are wrong, and the style is inconsistent.**
   - Current state: Q1, Q2, Q5 and Q6 cite Cohen's chapters as "Berman et al, 2021" and Ingle's as "Rotstein and Ingle, 2019". Q3 cites Ingle's Ch.11 as "Rosenberg et al, 2019" and Ingle's Ch.34 as "Ingle's Ch.34, 2019". The last is not an author-year citation, and its reference entry "Ingle's Ch.34. Achieving..." sorts under "I".
   - Author lines found:
     - Cohen's Ch.5: `05_5_Case_assessment_and_treatment_planning.md`, PDF p.569: "Paul A. Rosenberg, Matthew Malek"
     - Cohen's Ch.17: `17_17_Evaluation_of_outcomes.md`, PDF p.2138: "Yuan-Ling Ng, Kishor Gulabivala"
     - Cohen's Ch.19: `19_19_Management_of_endodontic_emergencies.md`, PDF p.2365: "Fabricio B. Teixeira, Gary S.P. Cheung"
     - Ingle's Ch.11: garbled line on PDF p.323. Decoding with the same character map as Ch.34 gives Paul A. Rosenberg, Matthew Malek, K. Okamoto. Q3 decoded the same; verify against the printed book.
     - Ingle's Ch.34: `34_Chapter_34_...md`, PDF p.926: the garbled line `F%&'"'() G)*(+%&,` decodes letter-for-letter (e=%, r=&, n=', a=", d=(, o=)) to **Fernando Goldberg**.
   - Fix, for all seven answers in one pass:
     - (Rosenberg and Malek, 2021) for Cohen's Ch.5
     - (Ng and Gulabivala, 2021) for Cohen's Ch.17
     - (Teixeira and Cheung, 2021) for Cohen's Ch.19
     - (Rosenberg, Malek and Okamoto, 2019) for Ingle's Ch.11
     - (Goldberg, 2019) for Ingle's Ch.34
     - Give each a chapter-in-book reference; drop the "authors not recovered" lines.
   - Note: Cohen's Ch.17 and *Treatment of Endodontic Infections* Ch.20 share authors and wording, so "Gulabivala and Ng, 2022" and "Ng and Gulabivala, 2021" are one view; say so where both are cited. Ingle's Ch.11 and Cohen's Ch.5 share authors (Rosenberg, Malek), which explains Q2's near-identical-wording observation.

---

## Q2: Single visit endodontics Vs multiple visit endodontics (50m)

- **Format:** compliant. The "no other repeats" line is correct; the 2017 Recent Advances 75m essay is under Q1.
- **Coverage:** good. It has head-to-head tables, a decision algorithm, Grossman's box, Ingle's 5-7 days and the 6.3% review.
- **MEDIUM:**
  - Q2 does not state Grossman's flare-up incidence (1.4-19%) or that flare-ups are commonest in retreatment. Both are short, examinable facts for a comparison essay.
    - `07_Chapter_7_Endodontic_Emergencies.md`, PDF p.158: "ranges from 1.4 to 19%"
    - PDF p.159: "One of the highest incidences of flare-ups occur in retreat"
  - Fix: add one row to the outcomes comparison table.
- **LOW:** a mnemonic is present. Check it is genuinely useful; the rules say skip rather than force one.

## Q3: Current concepts and controversies (50m, merged)

- **Format:** compliant. The heading uses the Jul 2023 wording, with all 10 absorbed wordings and cut-down notes listed.
- **Strengthen (at 1709 words, 9 above the floor):** the 50m merged question absorbs "your view", "critically evaluate" and "advantages, disadvantages" variants, so 1850-1950 words is safer.
- **HIGH:** Grossman is not cited at all. For an Indian MDS examiner, Grossman's statement that rotary NiTi made single visit "the treatment of choice for most of the endodontic cases", and its favourable/unfavourable box, are the expected "current concept" anchors.
  - `16_Chapter_16_Obturation_of_the_Radicular_Space.md`, PDF p.363: "single-visit endodontics has gained increased acceptance as the treatment of choice"
  - PDF p.364: "Decision-Making Criteria for Single-Visit Endodontics"
  - Fix: add 2-3 lines to concept 2C (case selection) and one line to concept 1. This adds about 80-120 words.
- **MEDIUM:**
  - Q3's controversies table lacks the flare-up controversy as a row. Schwendicke's RR 2.13 (very weak evidence) against Cochrane 2022's no difference in flare-up is in Q1 and Q2, but Q3 omits RR 2.13 entirely.
    - Fix: add one table row, citing Schwendicke and Göstemeyer 2017 (abstract only) and Grossman p.158 for the incidence. This adds about 40-60 words.
  - Concept 2D lists "laser and photodynamic therapy", sourced to Siqueira and Rôças Ch.14, PDF p.807: "### Laser and photodynamic therapy". This is correct. Q1 still tags photodynamic therapy [RECALL] and could now cite this page; flag for the Q1 patch.

## Q4: What is SVE? Success and failures (20m)

- **Format:** compliant.
- **HIGH (examiner expectation):** Strindberg's criteria *are* available, contrary to Q4's audit line ("not found in the outcome chapters read"). Cohen's Ch.17 reproduces them in a comparison table with Bender et al and Friedman and Mor:
  - `17_17_Evaluation_of_outcomes.md`, PDF p.2153: "The widely accepted definition for endodontic success and failure by"
  - PDF p.2154: "Criteria for Determination of Periapical Status" (Table 17.2: Strindberg success means no symptoms and normal periodontal contours, width and structure; failure means symptoms, or a periradicular rarefaction that is decreased, unchanged, new or enlarged; uncertain means ambiguous radiographs, or extraction before the 3-year review because another root failed)
  - Cohen's also notes that Friedman and Mor's "healed" corresponds to Strindberg's "success", and "healing" to Bender's "success" (PDF p.2153).
  - *Endodontic Radiology* Ch.16 corroborates: `16_16_Healing_of_Chronic_Apical_Periodontitis.md`, PDF p.277: "A well-known set of cri­ teria for healing ar" (the line wraps).
  - Fix: add a compact three-column table (Strindberg / Bender / Friedman and Mor) to section 2's exam core, cited as (Ng and Gulabivala, 2021). This is about 70-90 words, which stays under 800. Remove the "not found" sentence from the audit block.
- **MEDIUM:** "Functional retention" (Friedman 2004) is in Ingle's Ch.34. Cohen's gives the coinage at PDF p.2152: "The term functional retention was coined by Friedman". Cite both for consistency.

## Q5: Relevance of multiple visits (20m)

- **Format:** compliant. The 5 repeats and the 10m cut-down note are present.
- **Strengthen (682 words, 2 above the floor):** a hand-counted 680 would be borderline. The case for multiple visits in Q5 is strong but misses two short, sourced points:
  1. Flare-ups are commonest in retreatment (Grossman Ch.7, PDF p.159: "One of the highest incidences of flare-ups occur in retreat"). This supports listing retreatment as a multiple-visit indication.
  2. The 5-7 day interval for vital multiple-visit cases (Ingle's Ch.11, `11_Chapter_11_Treatment_Planning_and_Case_Selection.md`, PDF p.332: "waits 5 to 7 days between canal instrumentation"). This is already in Q1 and Q2. Q5's protocol line says "at least one week" (Siqueira), which is for infected teeth. State both, with their different purposes, as Q2 does.
  - Together these add about 50-70 words and give a safe margin (about 740).
- **Consistency:** Q5 states "Fewer patients with pain in the first week (Mergoni et al, 2022)" as a pro-MVE point. That is correct, but add "(small effect; small subgroups)" to match the corrected Q1 wording.

## Q6: Relevance of single visit endodontics (10m)

- **Format and coverage:** compliant, within range, and appropriate for 10m (rotary NiTi, apex locator, 79% survey, Cochrane, limits).
- **Overlap:** Q6 shares 5.6% of 6-word sequences with Q3, the highest pair in the topic. It is still far below 30%, so no action is needed.
- **LOW:** the audit's contradiction ("Grossman says 'most' cases yet rules out all retreatment") is fair. Keep it.

## Q7: Single visit in asymptomatic pulpless teeth (10m, marks not printed)

- **Format:** compliant. The "treated as 10m" disclosure is present.
- **Coverage:** good for 10m. Optionally add the Weine condition (no radiolucency, not tender to percussion) as the strict-textbook counterpoint; it is in Q1 and in Q7's own explanation.
- **LOW:** the "favourable conditions" list is a synthesis, marked [Likely] in the audit. Acceptable.

---

## Cross-question section

- **Facts stated consistently across answers:**
  - Sjögren 94%/68%
  - Cochrane RR 0.93 (radiological failure)
  - 6.3% review
  - Siqueira 10-20%
  - >2 visits harmful
  - Peters and Wesselink's 4.5-5 years, where used
  - the 79% survey
  - flare-up incidence, where used
- **Inconsistent:**
  1. the vital-teeth pain subgroup wording (HIGH 1)
  2. "standard of care" (HIGH 2)
  3. author-attribution style for Cohen's and Ingle's chapters (HIGH 3)
  4. photodynamic therapy is [RECALL] in Q1 but sourced in Q3 (Ch.14 p.807); align Q1 to the source
  5. Strindberg is absent from Q4 (and Q1's outcome passages) although available in Cohen's Ch.17
- **No contradictions between answers** on the substantive positions. All seven present the same consensus: single visit for vital teeth; equivalence in pooled RCTs for necrotic teeth, with underpowered trials; two visits for symptomatic, exudative, retreatment and complex cases; never more than two.
- **Wording overlap of exam cores** (6-word sequences, as a share of the shorter answer): highest is Q3-Q6 at 5.6%, then Q1-Q4 at 3.5%; all others are below 3.5%. All are far below the 30% ceiling, and every exam core stands alone (no "see Q1" inside any exam block).
- **Hand-reproducibility:** the longest tables are Q3's controversies (about 7 rows by 4 columns) and Q2's head-to-head tables (4 tables). They are writable, but Q2's four tables together take about 12-15 minutes. Acceptable for 50m.

## Suggested fix order
1. Global pass over Q1-Q7: chapter-author citations and references (HIGH 3), vital-teeth pain wording (HIGH 1) and "standard of care" (HIGH 2).
2. Q4: Strindberg table.
3. Q3: Grossman lines and the flare-up row, to about 1850 words.
4. Q5: retreatment flare-up and the 5-7 day versus 1-week intervals, to about 740 words.
5. Q2: flare-up row.
6. Q1: source photodynamic therapy to Siqueira Ch.14 p.807.
7. Re-run locator verification and word counts.
