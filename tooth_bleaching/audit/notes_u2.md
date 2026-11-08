# Auditor u2 notes — tooth_bleaching (materials side), 2026-11-08

Scope: B02 (100m), B04, B05, B08 (10m), B10, B11 (7m), B12 (5m). New locator file `loc_u2.py`: 61 L keys, 7 new F keys (Craig's 11th Ch.5 and Ch.8, Phillips' Ch.11, Bhat Ch.7, van Noort Ch.2.1, Lasers Ch.2 and Ch.7). New BOOK keys: Craig2002, Anusavice2013, Bhat2019, vanNoort2013, Coluzzi2023, Cronshaw2023. No loc_a*.py file edited.

## 1. Verification
| Check | Result |
|---|---|
| `python3 locators.py u2_` | 2082 checked, missing 0 |
| `check_answers.py` on the 7 files | quotes not found 0; leftover numbers: B02 "13" only = cross-reference "(Section 13)", acceptable; all others none |
| B02 "1800" (mid-1800s) | Locator added: u2_sum_mid1800 (Summitt PDF p.817) plus u2_sum_1800s |
| B02 history core, "by 1910 in-office 30-35% hydrogen peroxide" | Summitt says only "high concentrations"; reworded to "high-concentration". "1968: Klusmier" reworded to "Late 1960s" (Summitt's wording; 1968 is Sturdevant's date for home bleaching). 1893 line now attributed (Ritter et al, 2019) |
| B02/B10 core "Final products are CO2 and water" | Had no locator. Source found: Cohen's — CO2 and water come from "Further degradation over this step" (disintegration of the organic matrix, i.e. beyond whitening). Core reworded "Further oxidation, beyond whitening, ends in CO2 and water (Setzer, 2021)"; u2_coh_co2 |
| B02/B10 "bleach = oxidizer, stain = reducer" | Locator added: Grossman's redox diagram (u2_gro_reduc, u2_gro_oxid); B02 core now cites Gopikrishna |
| B10 core "perhydroxyl most reactive, alkaline pH" | Had no locator; now Sikri 2020 Smartbleach passage (u2_tcr_perhyd) and Andreasen "basic solution, lower activation energy" (u2_and_basic) |
| B11 core "35% CP ≈ 9.5% H2O2" | Unattributed; now (Haywood, da Costa and Berry, 2013) |
| B05 core "TMD (Kwon and Goldstein)" | TMD is Summitt's point; re-attributed |
| B12 core "Nd:YAG, erbium — overheating or investigational (Sikri)" | Those words are Luk and Anagnostaki's; re-attributed |
| Phillips' has no bleaching section | Confirmed by grep (whitening/peroxide/bleach): only dentifrice paragraph (Ch.11, p.250), a colour-chapter mention, denture cleansers and benzoyl peroxide. The dentifrice paragraph is now used (B02, B08) |
| Exam-core words before → after | B02 3238 → 3285; B04 393 → 399 (tightened 2 phrases); B05 386 → 396; B08 357 → 385; B10 261 → 270; B11 262 → 277; B12 176 → 191 |

## 2. Additions
| Answer | Added (source) |
|---|---|
| B02, B04, B05, B10, B11 | One identical 10% carbamide peroxide breakdown block in each Explanation (9 books): Summitt 3.5% + 6.5% urea; Torabinejad ~3.5%; Cohen 3.5% (10-30% = 3.5-8.6%) but 4% in its home section; Grossman 3.4% + 6.5% (its scheme a page earlier says 3.5%); Bonsor and Pearson 3.3%; Sturdevant 3% + 7%; Sikri 2020 and Sikri 2019 3.0%; Alani and Patel ~3% "over a period of 4 h". Identical exam-core line in all five: "10% CP ≈ 3.5% H2O2 + 6.5% urea (Haywood, da Costa and Berry, 2013); 3.4% (Gopikrishna, 2021); 3% + 7% urea (Ritter et al, 2019)" |
| B02, B05, B11 | One identical activity-time block: Summitt up to 10 h, 50% used in 2 h, most potency lost after 5 h, Table 16-2 "2 to 10 hours due to carbopol amount"; Bonsor and Pearson active after 10 h; Grossman "up to several hours"; Alani and Patel 4 h; Cohen 40-90 min; Powers and Wataha replenish gel each hour; Cohen slower than H2O2. Identical core line: "Active up to 10 h (Haywood, da Costa and Berry, 2013; Bonsor and Pearson, 2013); Cohen's: 40-90 min (Setzer, 2021)" (B02 section 8 newly; B05; B11) |
| B02 | Andreasen history (1864 first publication, walking bleach 1961, orthodontist's late-1960s observation); Summitt's other 1800s agents; Bonsor perborate → sodium borate, less H2O2 than carbamide; Andreasen chromophore splitting and basic-solution activation energy; Craig's 11th enamel permeation "in just a few seconds"; Bonsor 15 min; Bhat exposed-dentin cytotoxicity; Powers 0.5 mm dentin; van Noort mercury release; toothpaste conflict (Phillips', Craig's 11th, Bonsor); core OTC toothpaste line reworded |
| B04 | Craig's 11th and Bhat penetration; Alani and Patel bond loss up to 60%, recovery ~4 weeks, delay 2-4 weeks; van Noort vs Powers and Wataha on amalgam |
| B05 | Wear time: Grossman 4 h per session; Powers and Wataha 3-4 h, gel replenished hourly |
| B08 | Whitening toothpaste conflict (core and Explanation); Craig's 14th Table 4.7 bleach-shade composites; confirmed by grep that no book mentions sodium chlorite |
| B10 | Endodontology radical list; Sikri perhydroxyl; Andreasen activation energy, chromophore splitting, ammonia uncertainty; Cohen CO2/water stage |
| B11 | Craig's 11th "generally carbamide peroxide" vs 14th "carbamide or hydrogen peroxide"; van Noort mercury; Andreasen ammonia uncertainty |
| B12 | Coluzzi Table 2.1: 445-nm InGaN and 532-nm GaN diodes for whitening; Cronshaw and Mylona: handpiece window 2.8-4.0 cm², 250-500 mW/cm²; PBM review (six studies, 660-810 nm, 12-60 J/cm², evidence insufficient) — core line added |

## 3. Conflicts (shown side by side)
1. 10% CP yield: 3.5 / 3.4 / 3.3 / 3.0 / ~3% (nine books, above). Stoichiometry from Cohen's "about 35%" gives 3.5%; the rest are rounded [Likely].
2. Higher strengths fall below proportion: Cohen 30% = 8.6% (proportional 10.5%), Summitt 35% ≈ 9.5% (proportional ~12%); neither explains (B02, B04, B05, B10, B11).
3. Activity time: 10 h (Summitt, Bonsor) / several hours (Grossman) / 4 h (Alani) / 40-90 min (Cohen) / hourly replenishment (Powers). Carbopol content probably explains it [Likely].
4. First non-vital bleaching report: 1848 (Sturdevant) vs 1864 (Andreasen) (B02).
5. Whitening toothpastes: stain removal only (Bonsor and Pearson) vs low-peroxide pastes effective daily (Craig's 11th) vs abrasion plus bleaching, benefit under investigation (Phillips') (B02, B08).
6. Peroxide penetration: seconds through enamel (Craig's 11th) vs minutes to the pulp (Craig's 14th, Summitt 5-15 min, Bonsor 15 min) — different end points (B02, B04).
7. Amalgam: mercury release (Summitt, van Noort) vs "do not adversely affect … amalgam" (Powers and Wataha) (B02, B04).
8. Bonding delay: Alani and Patel 2-4 weeks added to the existing 24 h-3 weeks range (B04).
9. PBM for post-bleaching sensitivity: "could be recommended" (Luk and Anagnostaki) vs evidence insufficient for guidelines (Cronshaw and Mylona), same book (B12).

## 4. Slips found
- Grossman's 14th: 10% CP gives 3.5% H2O2 in its reaction scheme (p.459) and 3.4% in its mechanism text (p.460); its sodium perborate text says metaborate + water + oxygen, its equation on the same page metaborate + H2O2 + O2.
- Cohen's 12th: 10% CP = 3.5% H2O2 (p.2988 PDF) but 10-22% = 4-7.5% (p.3003 PDF).
- Lasers in Dentistry Ch.16 Fig. 16.18 (Luk and Anagnostaki): calls carbamide peroxide breakdown a "reduction" into ammonia and CO2 and H2O2 "further reduced" — carbamide peroxide dissociates into urea + H2O2; only urea yields ammonia + CO2 (B10).
- Bonsor and Pearson and Alani and Patel: smaller molecules "reflect less light" — backwards; they absorb less (Luk: "absorb less and therefore reflect more light") (B02, B10).
- (Already in B02 from drafting: Cohen's "sodium peroxide" for sodium perborate.)

## 5. Open
- Craig's 11th Ch.10 bonding troubleshooting table lists "Recent bleaching procedure" as a cause of debonding but the solution column is garbled in the extraction; not used.
- Sodium chlorite whiteners: no book mentions them (grep of all books); stays [RECALL] in B08.
- Phillips' 12th year still not printed in the extraction.
- B04 exam core at 399/400 — no room for further additions without cuts.
