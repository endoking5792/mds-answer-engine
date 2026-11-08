# Auditor u3 notes — tooth_bleaching (2026-11-08): B06, B07, B09, P1, P2

Scope: endodontic-side audit. P1 and B09 against the resorption chapters (Gulabivala & Ng 4th Ch.11; Ingle's 7th Ch.15, Andreasen, Heithersay & Bakland; Endodontology Ch.42; Sikri Essentials Ch.27) and Cohen's 12th Ch.18 (Patel et al). B06/B07 against Sikri's Textbook of Conservative and Restorative Dentistry Ch.32, Goldstein Ch.24 (West et al), Andreasen Ch.29 and Sturdevant's Ch.21. P2 (and B09) against Craig's 14th Ch.6, Bhat et al, McCabe & Walls 9th, Powers & Wataha 10th Ch.6, Bonsor & Pearson Ch.18, Sturdevant's, Goldstein Ch.12. New locator file `loc_u3.py` (12 F, 66 L, 4 BOOK keys: Gulabivala2014, Andreasen2019, Baumann2010res, Sikri2019res); existing keys reused (a2_cr_concern, a4_cr_enamel, a4_cr_pulp, a2_pw_noeffect, a4_bon_aprism, a4_bon_transl, a4_bon_25bond, a4_bon_2wk, a4_bon_ascorb, a4_bon_metallic). No loc_a*.py file was edited.

## 1. Verification
| Check | Result |
|---|---|
| `check_answers.py` (5 files) | quotes not found 0; exam-core numbers without a locator: none in any file (before and after) |
| `locators.py u3_` | 2079 checked, missing 0 |
| Exam-core words | B06 395 → 396; B07 398 → 398; B09 339 → 387; P1 356 → 394; P2 349 → 398 (all within 320-400; no FAILURE DISCLOSURE) |
| Cohen's 18-25% (with heat) | Opened Cohen's Ch.26 PDF p.3004: "6% to 8% ... 35% hydrogen peroxide ... and 18% to 25% if the hydrogen peroxide was heat activated", refs 54, 73, 74, 94, 104, 141, 204 — clinical reports/series (Cvek & Lindvall 1985; Friedman 1997; Friedman et al 1988, 58 teeth; Harrington & Natkin 1979; Heithersay et al 1994; Lado et al 1983) plus one in-vitro penetration study (Rotstein et al 1991). Study type is not stated, and Cohen's does not cite Madison & Walton for it. Summitt (PDF p.836): "Animal studies have shown ... 18% to 25% when heat was applied and 0% to 6% without", refs 91-93 = Madison & Walton; Rotstein et al histological study; Heller et al. Now stated exactly in P1 and B09 (Explanation and exam core); B09's exam core previously gave Cohen's figure with no qualification — fixed |
| "Cohen's names sodium peroxide" | Confirmed verbatim, Cohen's Ch.26 PDF p.2987: "sodium peroxide for internal, nonvital bleaching". The same page describes only sodium perborate (NaBO3, "95% of the molecule ... close to 10% of the available oxygen"). No other book names sodium peroxide as a current agent (grep of all books: Summitt's reference title Kirk 1893 only; an exam manual on denture cleansers). B06 now calls it a probable slip for perborate [Likely] |
| P1 claim "Ch.18 has no bleaching-specific text" | Confirmed (grep "bleach" in Cohen's Ch.18 = 0 hits) |
| Unsourced exam-core statements | B06 "rebleaching usually works" had no locator or Explanation support — removed. P1 "10% CP" was attributed to Setzer — re-attributed to Haywood et al (Summitt). B06 "9.9% ... agent of choice (Rotstein, 2019)" — 9.9% is Ingle's, "agent of choice" is Torabinejad's; citation moved to the 9.9% |
| Offsets confirmed | Gulabivala Ch.11: 9 (PDF 305 = p.296, 306 = p.297); Ingle's Ch.15: −48 (PDF 380 = p.428, 382 = p.430); Endodontology Ch.42: 17 (350 = p.333, 354 = p.337); Sikri Essentials Ch.27: 21 (510 = p.489, 514 = p.493); Sikri Textbook Ch.32: 19 (PAGE 618 = p.599); Goldstein Ch.24: 35 (PAGE 819 = p.784) |

## 2. Additions
| Answer | Added (source) |
|---|---|
| P1 | Heithersay classes 1-4 (Endodontology Ch.42; Sikri Ch.27); success 100/100/77.8/12.5% in 101 cases, limitation to proximal lesions, Patel's 3D CBCT classification (Cohen's Ch.18); class 4 high failure (Endodontology), "no treatment can be generally recommended" (Ingle's Ch.15); TCA 90% with curettage, endodontic treatment for class 3 (Ingle's Ch.15); diagnosis: pink spot (Gulabivala; rare — Cohen's Ch.18), canal outline visible through the lesion (Gulabivala); mechanism: bleaching damages cementum, 10% bare CEJ, sustained by subgingival plaque (Gulabivala), cementoblast defect prerequisite (Ingle's); bleaching as predisposing factor (Endodontology, Sikri Ch.27); Heithersay 222 patients/257 teeth: orthodontics 21.2%, trauma 14%, trauma + bleaching 7.7%, bleaching alone 4.5% of patients (Ingle's); 6-8% prevalence, >30% risk, warn the patient (Bonsor & Pearson); Cohen's 18-25% basis (refs) vs Summitt animal data |
| B09 | Pulp: penetrates intact enamel to pulp in minutes, adverse pulpal effects in vivo, long-term concern (Craig's 14th); smear-layer removal → hypersensitivity (Powers); 6-8% resorption prevalence, risk >30% H2O2 (Bonsor); exact source of 18-25%; amalgam/RMGI/GIC effects (Powers); metallic taste, genotoxic in vitro not in vivo (Bonsor) |
| B06 | Sikri Textbook: thermocatalytic ≤20-30 min per visit, Liebenberg 1997 intracoronal 10% CP in a splint, combination = thermocatalytic + walking bleach, walking bleach 24-48 h to 7-10 days, perborate + 35% superoxol, 0.5-1.0 mm Ca(OH)2/GIC barrier, 2-3 mm GP removal; West: maximum effect within 48 h; Cohen's perborate 95%/≈10% oxygen |
| B07 | GP removal 1-2 mm apical of clinical crown (Sturdevant), 2-3 mm (Sikri Textbook); West's barrier transfer (three probings mesial/facial/distal; flowable composite, GIC, Cavit), 70% alcohol wash, 2 mm two-layer Cavit seal, max effect 48 h, 2-3 applications, overnight result, cure labial then lingual; Sturdevant 5-min bubble check of the seal, perborate changed weekly; Sikri Textbook timing and barrier |
| P2 | Bonsor: neutral-pH low-concentration CP no effect on enamel/dentine microhardness, aprismatic layer lost after a month of 10% CP, higher concentrations less damaging than etching, increased incisal translucency, ~25% bond loss, delay ≥2 weeks, sodium ascorbate before etching, no effect on established bonds; Craig's 14th enamel permeability; Powers smear layer, amalgam/GIC/RMGI effects |

## 3. Conflicts (shown side by side in the answers)
1. **18-25% resorption with heat** (P1, B09): Cohen's — no study type, clinical refs; Summitt — animal studies (Madison & Walton et al). Quote as animal/heat data; human ≈7%.
2. **Bleaching's share of ECR** (P1): Ingle's (co-author Heithersay) 4.5% of patients alone, 7.7% with trauma; Goldstein 3.9% "caused by" bleaching. Probably patients vs teeth denominators [Likely]; Goldstein's "caused by" overstates "predisposing factor". Cohen's Ch.18 (Mavridou series) lists no bleaching among factors.
3. **TCA sequence** (P1): Ingle's/Heithersay and Sikri's table — TCA then curettage; Cohen's Ch.18 and Sikri's text — curettage then TCA.
4. **"Combination technique"** (B06): Sikri Essentials — thermocatalytic + nightguard; Sikri Textbook — thermocatalytic + walking bleach; Goldstein — Settembrini & Liebenberg inside/outside 10% CP; Sikri Textbook lists Liebenberg's splint as *modified walking bleach*.
5. **Barrier thickness** (B06, B07): Sikri Textbook 0.5-1.0 mm Ca(OH)2/GIC vs ≥2 mm (Cohen's, Ingle's).
6. **Recall/change interval** (B07): 48 h (West) to 2-4 weeks (Torabinejad); weekly (Sturdevant, Andreasen).
7. **GP removal level** (B07): now also 1-2 mm apical of the clinical crown (Sturdevant), 2-3 mm (Sikri Textbook).
8. **Light-curing direction** (B07): labial rather than lingual (Torabinejad) vs labial then lingual (West).
9. **Pulp safety** (B09): Craig's — adverse pulpal effects in vivo, long-term concern; Summitt — pulp remains healthy, reversible.
10. **Acetone adhesives** (P2): Sikri, Setzer — help reverse bond loss; Bonsor — bond loss more marked with acetone than ethanol products.
11. **Amalgam** (P2, B09): Summitt — mercury release; Powers — amalgam not adversely affected (surface vs ion release; measure different things).

## 4. Slips
- Cohen's Ch.26 PDF p.2987: "sodium peroxide for internal, nonvital bleaching" — the chapter otherwise means sodium perborate [Likely slip].
- Sikri Essentials Ch.27 (PDF p.513): "Mostly the cervical resorption defects are transient ... cementum repair may occur within two to three weeks without any treatment" — describes transient surface resorption, not ECR (progressive/invasive in Gulabivala, Endodontology, Ingle's).
- Sikri Essentials Ch.27: text and summary table order TCA and curettage differently within one chapter.
- Sikri Textbook Ch.32: "pressure in the pulp chamber is required for bleaching" — no other book says this; and a 0.5-1.0 mm calcium hydroxide/GIC "barrier" (calcium hydroxide does not seal).
- Goldstein Ch.12: Heithersay's percentages given as "caused by" with no denominator.
- Andreasen Ch.29 (not used): "Nocturnal use of 10% hydrogen peroxide gel in a tray" — most books give 10% carbamide peroxide (≈3.5% H2O2) for nightguard use; possibly a slip [Guessing; not edited into any answer].

## 5. Open
- Ingle's Ch.15 author line decoded from cipher-damaged OCR (Andreasen JO, Heithersay GS, Bakland LK) — verify against the printed book.
- Gulabivala Ch.11 and Endodontology Ch.42 chapter authors not printed in the extraction (cited under editors). In-text citations "(Baumann and Beer, 2010, Ch.42)" and "(Sikri, 2019, Ch.27)" distinguish them from the bleaching chapters of the same books.
- Heithersay patients vs teeth (4.5% vs 3.9%) inferred, not read in the primary paper (no live search).
- Bonsor Table 18.2 (effects on restorative materials) is empty in the extraction.
- B06 (396) and B07 (398) are at the top of the range; further additions need cuts.
