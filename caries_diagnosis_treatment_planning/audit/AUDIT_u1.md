# Audit ledger u1 — caries_diagnosis_treatment_planning (Q01, Q02, Q08, Q16, Q17)

Auditor u1, 2026-11-14/15, per `_REVIEW_BRIEF.md` and SESSION_PROMPT §6. Files edited: the five canonical answers, their sidecars, `locators_Q01.py`, `locators_Q02.py`, `locators_Q08.py`, `locators_Q16.py`, `locators_Q17.py` (additions appended as `L.update` / `F_EXTRA[...]` blocks marked "Audit u1"). Nothing committed or published.

Checks done on every answer: second read against its LOC ledger (located phrase opened in the book for each doubtful statement); standing Conservative books not used by the drafter checked for missing exam content, conflicts and slips; student-file cleanliness (stands alone, heading sequence, blueprint at 10/20m, Vancouver list numbered by first citation, citations ↔ references, no audit material, no mnemonics/recaps); reference formats harmonised across the five answers (Kidd; Summitt place Hanover Park, IL from the copyright page; Sikri "CBS Publishers & Distributors; 2020. Ch.n, Title"; Singh; Sturdevant contributors per settled decision); `build_audit.py` re-run until clean.

## Q01 — Recent advances in diagnosis and management (100m)
- **Second reader:** no wrong attributions or number mismatches found; synthesis sentences remain framed as reasoning. Sidecar's open point on Sturdevant author order closed (settled decision).
- **Additions:** chemo-mechanical caries removal (Carisolv self-limiting action, no LA often needed, Papacarie) and other excavation technologies lacking clinical validation (Banerjee and Watson 2015, Pickard's Guide PDF 84, 92); Sikri 2020 Ch.28 (PDF 563-564) on bonding, cost, instruments, chlorine taste.
- **Conflicts shown:** Carisolv hypochlorite 0.1% gel (Banerjee and Watson) vs 0.5% liquid component (Sikri); ICDAS digit order — restoration first (Ekstrand and Braga) vs severity first (Boushell and Shugars); device evidence — untested in controlled trials (Amaechi et al. 2013, Summitt PDF 232) vs trial evidence for DIAGNOdent (Neuhaus and Lussi PDF 172).
- **Slips:** Ekstrand and Braga PDF 51 "ICDAS score 0–7" for the caries digit (codes are 0-6) — sidecar only.
- **References:** Summitt (Amaechi et al.) and Sikri added; list re-sorted by first citation (25 refs).
- **Open points:** none. Words 3410 (3200-3500; 90 below ceiling after additions).

## Q02 — Epidemiology, prevention, diagnosis and treatment planning (75m)
- **Reworded/removed:** Sikri genetic theory ("candidate enamel-formation genes" → genes via immune response, saliva, enamel); Borges "mainly" → "most likely" (book's wording); "floss or interdental brushes" removed (unlocated); "sugared medicines" removed, diet line reworded to Sturdevant's acidic drinks/bedtime bottle; sealant timing → "just after eruption in susceptible patients"; hyposalivation bullet replaced by Sturdevant Table 2.10 wording ("medication review" removed); "magnification" removed from Kidd's prerequisites; APF, rinse, SDF rows now cited.
- **Newly located (verified on page):** 26 locators, incl. incidence-rate denominator, extent/severity, deft "e", DMF reflects dentist numbers, gender pattern, familial caries, rinse programme abandoned, root lesions soft/leathery, FOTI orange-brown, NILT through alveolar bone, Sikri fluoride mechanism.
- **Conflict added:** treatment-plan phases — five (Boushell and Shugars, Ch.3) vs three for the high-risk caries patient (Ferreira Zandoná and Ritter, Ch.2: control 2-4 weeks, definitive, maintenance).
- **Slips (sidecar only):** Sturdevant Ch.2 calls xylitol evidence "very weak" yet Table 2.10 recommends xylitol/sugar substitutes; Kidd PDF 184 vs 186 define D2/D3 differently; Kidd Fig. 8.2 caption gives 1988 and 1998 for the same line.
- **References corrected:** Fontana and Huysmans title ("…role of caries detection and diagnosis"), Yanıkoğlu and Tağtekin title ("Use of ultrasound for caries detection"), Summitt place, Sikri format.
- **Open points:** none. Words 2947 (2550-3000). Body-number flags are section numbers 2.1-5.3 and the marks value 75.

## Q08 — Etiological factors and methods of diagnosis (20m)
- **Reworded:** "enamel lesions" → "early lesions" (bitewing sensitivity phrase); "root caries progresses faster" → "roots demineralise more readily" (Sikri's point); modifying factors reworded to Sturdevant's risk-factor list and cited; hyposalivation now cited (drug cause dropped); ICDAS and tooth-separation lines given Kidd citations; activity-test names located; stray semicolon fixed. Removed: uncited stickiness/clearance/bedtime bullet.
- **Addition:** Keyes 1960 triad and Newbrun 1982 time factor (Singh 2020 Ch.5, PDF 46/48).
- **Conflicts:** Sturdevant's Keyes–Jordan (1963 figure source) vs Singh's Keyes 1960 judged a citation difference, not a conflict; not shown.
- **Cuts for ceiling:** diagram modifier list shortened; separation + FOTI merged; pellicle + ecological-shift bullets merged; "clean, dry, well lit" folded into the standard-of-care line.
- **Open points:** none. Words 800 (680-800). Flag "20" = marks.

## Q16 — Newer classification of dental caries (10m)
- **Second reader:** claims verified (Sikri Table 2.4 confirms no size 0; Ekstrand two-digit definition).
- **Conflict added:** ICDAS digit order (Boushell and Shugars vs Ekstrand and Braga), alongside the existing ICDAS-date conflict. Drafter's judgement "2002 origin best documented" cut for room; intro tightened.
- **Slip:** Ekstrand and Braga "0–7" (sidecar).
- **References:** Boushell and Shugars added (ref 9); Sikri format harmonised.
- **Open points:** none. Words 396 (320-400). Flags: "2.1" = worked Site/Size example, "10" = marks.

## Q17 — Diagnosis of proximal caries (5m)
- **Reworded:** "clean (floss), dry" → "isolated, clean, dry" (Kidd's words; floss not on that page). Cavitation figures specified as dentine halves (Pitts and Rimmer, via Zeller et al.).
- **Addition:** inactive proximal lesion — hard brown spot below the contact, restoration not indicated (Boushell and Shugars, Sturdevant Ch.3 PDF 114).
- **Cut:** film holder/beam-aiming sentence (Amaechi et al.).
- **Conflict (unchanged):** cavitation probability — Pitts and Rimmer halves (Zeller et al.) vs Singh's 20-40% at D2.
- **References:** Boushell and Shugars added; Kidd and Singh formats harmonised; renumbered by first citation.
- **Open points:** none. Words 200 (160-200). Flag "5" = marks.

## Final build_audit lines
- Q01: LOC keys 205, missing 0; quotes not found 0; 3410 words (3200-3500); surnames none; numbers none.
- Q02: LOC keys 213, missing 0; quotes not found 0; 2947 words (2550-3000); surnames none; numbers = section numbers and 75.
- Q08: LOC keys 68, missing 0; quotes not found 0; 800 words (680-800); surnames none; numbers ['20'].
- Q16: LOC keys 46, missing 0; quotes not found 0; 396 words (320-400); surnames none; numbers ['2.1', '10'].
- Q17: LOC keys 22, missing 0; quotes not found 0; 200 words (160-200); surnames none; numbers ['5'].
