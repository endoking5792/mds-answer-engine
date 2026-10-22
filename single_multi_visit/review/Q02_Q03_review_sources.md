# Q2 and Q3 review: claim-by-claim source verification (2026-10-22)

Scope: author-year-cited sentences in `canonical/Q02_Single_vs_Multiple_Visit_Endodontics_50m_CANONICAL.md` and `canonical/Q03_Current_Concepts_and_Controversies_of_Single_Visit_RCT_50m_CANONICAL.md`, checked against the cited chapters in `mds-textbooks` and the PubMed abstracts. Also checked for conflict with the corrected Q1. Read-only: neither file was edited.

**Result:** no fabricated numbers and no wrong-book attributions in either answer. Numbers checked and exact:
- Q2: 94% vital pulpectomy; 6.3%; 10-20%; 5% failure; 5-7 days; 15-20 min; 79%; 19 days; RR 1.55/0.93/2.13; Risso 10.5/23%; trial sizes.
- Q3: 1-2 weeks; Lentulo 2-3 mm short; temporary 3-5 mm; at least 1 week; 6.3%; 4 RCTs; 150 and 100 teeth; 12 systematic reviews.

There are no [RECALL] tags in either file, but two protocol steps in Q3 are uncited (see below).

Counts:
- Q2: 0 high, 2 medium, 5 low.
- Q3: 0 high, 2 medium, 6 low.

## Q2

| # | Sev | Section | Quoted claim | Problem | Evidence | Suggested fix |
|---|---|---|---|---|---|---|
| 1 | MED | 6B table "Clinical outcomes"; 7 Exam core | "More after SVE, especially vital teeth"; "mainly in vital teeth (Mergoni et al, 2022)" | **Conflicts with corrected Q1, and overstated.** The vital-tooth excess comes from a subgroup of 2 studies (316 teeth); an equal mechanical-instrumentation subgroup also showed it; pain at the 1-week time point itself did not differ (RR 1.05). | Mergoni 2022 abstract (PMID 36512807): "higher in the single-visit groups for vital teeth"; "pain at one week postobturation (RR 1.05" | Use Q1's wording: "seen in small subgroups of vital teeth and mechanical instrumentation". |
| 2 | MED | 1 Explanation and Exam core, MVE definition | "the canal is dressed with an intracanal medicament (usually calcium hydroxide)… (Mergoni et al, 2022; Berman et al, 2021)" | **Attribution, same issue as fixed in Q1.** Cochrane defines MVE "with or without medication"; the medicament clause belongs to *Endodontology*. | Mergoni 2022: "with or without medication"; Baumann and Beer, 49_…md, PDF p.390: "an intracanal medicament should be placed between sittings" | Cite (Mergoni et al, 2022) for the definition and (Baumann and Beer, 2010) for the medicament. |
| 3 | LOW | 8A Exam core, Technology | "rotary nickel-titanium instruments, apex locators and magnification… making single visit practical for most cases (Gopikrishna, 2021)" | **Broadened.** Grossman links renewed acceptance only to rotary NiTi. Apex locators appear only in its working-length section, and magnification is not mentioned in this context. | Grossman 16_…md, PDF p.363: "with the advent of rotary nickel–titanium instruments" | Keep rotary NiTi with Grossman; tag apex locators and magnification [RECALL] or drop them. |
| 4 | LOW | 8A Explanation and Exam core | "supplementary protocols (irrigant activation, other adjuncts)… (Siqueira and Rôças, 2022)" | **Partial attribution.** Ch.11 p.544 says only that the search continues; the named options are on p.549. Q1 now cites p.549. | Siqueira and Rôças 2022, 11_…md, PDF p.549: "intravisit supplementary disinfection step using one of the following" | Name the p.549 options (ultrasonic or mechanical activation of NaOCl, final 2% chlorhexidine rinse) for consistency with Q1. |
| 5 | LOW | 7 Exam core, Quality of evidence | "often at high or unclear risk of bias… (Berman et al, 2021; Siqueira and Rôças, 2022)" | **Attribution, same as Q1 #13.** "High or unclear risk of bias" is Cochrane's wording. | Berman 2021, 17_…md, PDF p.2204: "they all lacked robust statistical power"; Siqueira 2022, PDF p.541: "low to medium" | Add (Mergoni et al, 2022), or use "low-to-medium quality". |
| 6 | LOW | 6C table | "Operator skill needed: High / Moderate" | **Inference, not stated.** Sources say beginners should not attempt SVE, but give no graded comparison. | Sikri, 21_…md, PDF p.392: "Operator at the beginning of their career should not" | Change to "High; not for beginners (Sikri, 2019)" against "Less critical". |
| 7 | LOW | 7 Exam core, trial table | Peters and Wesselink "39-42 teeth, up to 5 years" | **Sources differ** (4.5 years in Sikri, up to 5 in *Endodontology*). The range is fine, but the discrepancy should be in the audit block. | Sikri, PDF p.389: "Evaluation period: 4.5 years" | Write "4.5-5 years"; record it in the audit block. |

**Confirmed (no change):**
- Ingle's Ch.11 p.325: two extreme camps; second visit after an emergency "allows the clinician to determine the effect of the treatment on inflamed and infected tissues".
- Ingle's Ch.11 p.326: 6.3%, not significant; "regardless of the number of appointments, effective disinfection… is critical".
- Ingle's Ch.34 p.929: tubules; "may require more than one visit"; >94% vital pulpectomy.
- Ingle's Ch.34 p.930: properly done treatment shows no difference; bleeding, exudate, pain and acute symptoms.
- Grossman p.363-364: box, indications, contraindications, coronal seal.
- Siqueira Ch.11 p.532: 5% failure with CHPG.
- Harty p.156: leakage between visits.
- Trope 1999 conclusion (*Endodontology* p.390).

## Q3

| # | Sev | Section | Quoted claim | Problem | Evidence | Suggested fix |
|---|---|---|---|---|---|---|
| 1 | MED | Throughout | "(Rosenberg et al, 2019)" for Ingle's Ch.11; "(Ingle's Ch.34, 2019)" for Ch.34 | **Inconsistent citation format, and an unverified author.** Q1 and Q2 cite both chapters as (Rotstein and Ingle, 2019). "Ingle's Ch.34, 2019" is not author-year as rule 7.1(2) requires. "Rosenberg et al" was decoded from a garbled author line and has not been checked against the print. | Q1/Q2 references: "Rotstein I, Ingle JI, editors. Ingle's Endodontics. 7th ed." | Use (Rotstein and Ingle, 2019) for both, as in Q1/Q2; keep the decoded author name only in the audit block as "to verify". |
| 2 | MED | 5 Myths table | "Selected asymptomatic necrotic teeth can be treated in one visit by experienced operators (Ingle's Ch.34, 2019)" | **Overstated attribution.** Ch.34 p.930 says only that properly done treatment shows no significant difference; it does not mention asymptomatic necrotic teeth or experienced operators. | Ingle's 34_…md, PDF p.930: "if the treatment was properly done, there is no significant" | Cite Mergoni 2022 (no difference in radiological failure) plus Grossman's "experienced operator" factor (Gopikrishna, 2021, p.364), or reword to Ingle's actual statement. |
| 3 | LOW | 3 Exam core, Protocol steps 4 and 6 | "Working length (apex locator and radiograph)"; "NaOCl irrigation throughout; EDTA final rinse" | **Uncited, with no [RECALL] tag.** Siqueira's own protocol box gives a sourceable version. | Siqueira and Rôças 2022b, 14_…md, PDF p.781: "Smear layer removal: 17% EDTA (or 10% citric acid)" | Cite Ch.14 p.781 for EDTA, Grossman p.341 for apex locator plus radiograph, or tag [RECALL]. |
| 4 | LOW | 2F Exam core | "single visit caused less pain than two visits with calcium hydroxide or chlorhexidine (Erdem Hepsenoglu et al, 2018)" | **Slight overgeneralisation.** The differences were on day 1 (vs CHX only), day 2 and 1 month; there was no difference on days 3 and 7. | Erdem Hepsenoglu 2018 abstract (PMID 30054099): "There were no significant differences among the groups on the third and seventh days" | Add "at some time points (days 1-2 and 1 month)". |
| 5 | LOW | 4 Controversies table, row 4 | Evidence quality "Moderate certainty" | **Applies to only one side.** Moderate certainty is Cochrane's grade for first-week pain; the umbrella review reports confidence "limited by heterogeneity". | Gupta 2026 abstract (PMID 41856391): "Confidence in the evidence was limited by heterogeneity" | "Moderate (Cochrane first-week pain); limited (umbrella review)". |
| 6 | LOW | 4 Controversies table, row 6 | "Single visit is standard (Siqueira and Rôças, 2015)" | **Overstated, same as Q1 #12.** The source says "consensual… provided time, professional skills, and equipment are favorable". | Siqueira and Rôças 2015, 16_Intracanal_Medication.md, PDF p.279: "It seems consensual that treatment of uninfected teeth" | "Consensual where time, skill and equipment allow". |
| 7 | LOW | 2C Exam core | Decision factors "pulp and periapical status, and whether the canal can be dried (Rosenberg et al, 2019; Ingle's Ch.34, 2019)" | **Mixed attribution.** Ch.11 lists roots, anatomy, time, skill and symptoms; the dry-canal factor is Ch.34's bleeding/exudate list. Acceptable, but cite each to its own chapter after #1 is fixed. | Ingle's 11_…md, PDF p.325; 34_…md, PDF p.930 | Split the citations. |
| 8 | LOW | 2B Explanation | "infected canals are ideally treated in two visits… (Siqueira and Rôças, 2022b)" | **Context note, not an error.** Ch.14 p.757 says "As discussed in Chapter 11", so this is the same authors repeating their own view, not independent corroboration of Ch.11. | Siqueira and Rôças 2022b, 14_…md, PDF p.757: "infected root canals are ideally treated in two visits" | Note in the synthesis that 2022a and 2022b are one view. |

**Confirmed (no change):**
- Ch.14 p.795: "still one of the greatest current controversies".
- Ch.14 p.764: calcium hydroxide as a "physicochemical barrier" in unfinished vital cases.
- Ch.14 pp.794-795: two-visit protocol details (Lentulo 2-3 mm short, temporary 3-5 mm, at least 1 week, removal with the last instrument or one size larger).
- Ch.14 p.814: OSD "no consistent clinical evidence".
- OSD approaches present as Ch.14 subsections: chlorhexidine, mechanical activation (XP-endo/EndoActivator), ultrasonic activation, laser and PDT, GentleWave.
- Ingle's Ch.11 p.326: "inability to detect differences… might also be due to variations".
- Abstracts confirmed:
  - Gupta 2026: 12 systematic reviews; "did not show a consistent or clinically important difference".
  - Nunes 2021: 4 RCTs; lower mild pain; low certainty.
  - Karaoğlan 2025: 100 teeth; similar at 12-24 h, higher at 48 h after a single visit; interappointment pain greater than post-obturation.
- Q3's Cochrane pain wording ("slightly more patients… first week") is consistent with corrected Q1.

## Cross-answer consistency (Q1 corrected vs Q2/Q3)
1. **Vital-teeth wording of the Cochrane pain finding:** Q2 needs fixing (Q2 #1). Q3 is consistent.
2. **Supplementary disinfection:** Q3 is correctly sourced to Ch.14 (fuller than Q1). Q2 should name the p.549 options (Q2 #4).
3. **MVE definition attribution:** Q2 needs fixing (Q2 #2). Q3 cites Baumann and Beer for its SVE definition, which is consistent.
4. **Ingle's citation form:** Q3 differs from Q1/Q2 (Q3 #1).
