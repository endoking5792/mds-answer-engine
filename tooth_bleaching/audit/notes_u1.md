# Auditor u1 notes — tooth_bleaching (2026-11-08)

Answers: B01 (100m), B03 (100m), B13 (5m), P3 (10m). New locator file `loc_u1.py` (114 new L keys, 15 new F keys, all `u1_`); reused a1/a3/a5 keys where a phrase already existed. No loc_a*.py file was edited. New BOOK keys: Zachrisson2007, GoldsteinEsfandiari2018, Chu2010, Torres2020, Borges2020, Huhtala2020 (others copied verbatim from loc_a*.py; consistency checked, no differing strings).

## 1. Verification

| Check | Result |
|---|---|
| `python3 locators.py u1_` | missing 0 (2083 checked in all) |
| `check_answers.py` quotes not found | 0 in all four answers |
| Exam-core numbers without a locator | B01: `26` only — the product name AH26, acceptable. B03, B13, P3: none |
| Exam-core words (before → after) | B01 3273 → 3451; B03 3292 → 3435; B13 170 → 194; P3 345 → 390. All in range, no FAILURE DISCLOSURE |
| B01 Cohen walking-bleach trial (no locator) | Locators added (u1_coh_rctdesign, u1_coh_rct). Reworded: Cohen's trial was of walking bleach **or inside-outside** bleaching, and found "no significant changes in color and lightness" at 1 year (it was not a walking-bleach-only trial). Set beside Andreasen's long-term retreatment figures |
| B13 Bartlett 360 figure | Extract reads `about 360 \x01 130 mm` — ± is a control character and μ became m. Explanation now quotes both halves and states 360 ± 130 μm [Certain]; exam core (B13 and B03) now gives "about 360 ± 130 μm after about 100 s" (the ± 130 had been dropped). Locator u1_bar_130 added for the 130 |
| Citation form | B03 cited "Goldstein et al, 2018" (no letter) 9 times; all changed to 2018a (Ch.21, the only Goldstein et al entry in its REF) |
| P3 retrieval report | Said only Sikri's two books use the three-way scheme. Wrong: Goldstein Ch.39 (Goldstein, Esfandiari and Schultz, 2018) also names intrinsic, extrinsic and internalized. Grep of all books for "internali[sz]ed": only Sikri's two books and Goldstein's. Corrected |
| Sentences without a locator | B01 Section 12 "truest form of informed consent" already marked paraphrased/no locator by the drafter — left as is (open) |

## 2. Additions

| Answer | Added (source) |
|---|---|
| B01 | Walton's natural vs iatrogenic grouping (Walton and Torabinejad, 2002); three-way scheme in Goldstein Ch.39; Jordan and Boksman spelling and Goldstein's fourth degree (Kwon and Goldstein, 2018); tetracycline not prescribed up to 12 years, fluorosis critical window 20-30 months, risk gone by 8 years, MTA confined to apical 3 mm (Alani and Patel, 2025); barrier/GP table rows for Kwon, Endodontology, Andreasen, Alani and Patel; chamber etching, agent and heat conflict (Baumann and Beer, 2010; Dahl and Pallesen, 2007; Kwon and Goldstein, 2018); Walton's "more predictable" RCT + internal bleaching for tetracycline, Endodontology's caution on devitalization; calcific metamorphosis — Andreasen "cannot be expected", Walton "fair esthetic prognosis"; metal-ion stains do not bleach (Baumann and Beer, 2010; Kwon and Goldstein, 2018); bleaching first for discoloured endodontically treated teeth (Dahl and Pallesen, 2007); delay before bonding — 3 weeks (Endodontology), 1-3 weeks (Andreasen), 2 weeks (Kwon), 2-4 weeks and up to 60% loss (Alani and Patel); calcium hydroxide — Endodontology for, Walton against; prognosis — >90% immediate, retreatment 10% at 1-2 y, 20-25% at 3-5 y, 40% by 8 y (Dahl and Pallesen, 2007), 45-93% at 8-16 y (Baumann and Beer, 2010); Heithersay 3.9% (Kwon and Goldstein, 2018); peroxide cytotoxicity across dentin within minutes (Sakaguchi, Ferracane and Powers, 2019); critical synthesis Claim 1 resorption series (58 teeth 7% with heat, 0 in 95 and 250 perborate teeth; Cohen's perborate no resorption at 1 year) |
| B03 | Shade: Vita Bleachedguide, Group 0, Linear/Toothguide better than Classical, achromatic bleached teeth (value only), D55-D65 / CRI ≥90 / 1000 lux, 25-35 cm, 5-s glances, grey card, value-chroma-hue, shade before dehydration (Chu et al, 2010); canines need more bleaching (Alani and Patel, 2025); 10% CP and 6% HP commonest, 10% CP → ~3% HP over 4 h (Alani and Patel, 2025); in-office heat 52-60°C ≤30 min, NaF 3-5 min (Gopikrishna, 2021) vs light adds nothing (Zachrisson and Toreskog, 2007), Alani 3-4 × 15 min; resin infiltration 15% HCl 2 min, infiltrant 3 min, non-cavitated only (Borges, Torres and Schlueter, 2020); bleach before veneers (Huhtala et al, 2020); delay — 7-10 days (Grossman's in-office), 2-3 weeks (Cohen's), ≥2 weeks (Torres et al, 2020), 2-4 weeks (Alani and Patel, 2025); microabrasion timing from Cohen's, Walton's "not a true bleaching" |
| B13 | Kane 1916 and PREMA composition (Gopikrishna, 2021); 36% HCl diluted 1:1 to 18% (Walton); McInnes bleaches, acid-pumice does not (Walton); application 5 s + 15 s up to 12-15 times, stop to avoid enamel damage (Setzer, 2021); Walton 5-s swirl, 10-s rinse, bicarbonate neutralization, usually one visit, "relatively permanent"; Grossman 2-3 repeats; 360 ± 130 μm exceeds the 0.2-0.3 mm limit |
| P3 | Goldstein Ch.39 three-way scheme and ferric retraction fluid as an iatrogenic internalized stain; Walton natural vs iatrogenic; Goldstein Ch.12 extrinsic drugs and nicotine internalizing; Alani pigments vs dyes, black-brown bacterial stain in good hygiene |

## 3. Conflicts (shown side by side in the answers)

1. **Blood-pigment stains** (B01): Goldstein Ch.12 — bleaching "can be quite effective" (erythroblastosis) vs Walton — "not correctable by bleaching"; porphyria, AI, DI "not amenable". Neither gives data; trial with guarded prognosis [Likely].
2. **Chamber etching in walking bleach** (B01): Ingle's avoid vs Endodontology 37.5% phosphoric 15 s vs Andreasen 10 s.
3. **Walking-bleach agent and heat** (B01): Goldstein Ch.12 perborate + 35% H2O2 and higher temperature in pulpless teeth vs perborate + water, no heat (Ingle's, Endodontology, Andreasen, Walton). Followed the majority.
4. **GP removal / barrier level** (B01 table): now 11 books, from 1+ mm below the gingival margin (Alani) to 2-3 mm apical to the cervical line (Kwon); Andreasen removes GP only if the root is discoloured.
5. **Calcium hydroxide after bleaching** (B01): for — Sturdevant's, Grossman's, Endodontology (≥7 days); against — Ingle's, Cohen's, Torabinejad's, Walton's.
6. **Intentional devitalization for tetracycline** (B01): Walton "more predictable" vs Grossman's against; Endodontology cautious.
7. **Delay before bonding** (B01, B03): range now 24 h (Andreasen's lag) to 2-4 weeks (Alani); newer books trend longer.
8. **In-office heat** (B03): Grossman's 52-60°C vs Sturdevant's, Summitt's, Andreasen Ch.29 (no gain), Goldstein (no heat in children).
9. **Tray margin and reservoirs** (B03): short of gingiva (Sturdevant's), 0.5 mm away (Kwon), by viscosity (Grossman's), ~1 mm over the gingiva (Alani); reservoirs 1 mm short of the gingival margin (Grossman's) vs no evidence of benefit (Alani, Summitt's).
10. **Porcelain and bleach** (B03): Grossman's etched and weakened vs Summitt's no effect; Goldstein least on porcelain.
11. **Brown stain prognosis** (B03): Grossman's brown tetracycline least bleachable vs brown responsive (Sturdevant's, Goldstein's — for fluorosis). Reconciled as different stains [Likely].
12. **Older teeth** (B03): "excellent candidates" (Kwon) vs "more challenging to lighten" (Alani). Tolerance vs speed [Likely].
13. **Microabrasion application time** (B13): 5 s (Walton), 5 + 15 s (Cohen's), 20-30 s (Summitt's), 60 s (Sikri).
14. **Resin-infiltration etch** (B03): 90-120 s (Sikri) vs 2 min (Borges et al) — minor.

## 4. Slips

| Book | Slip | Why |
|---|---|---|
| Grossman's 14th Ch.23 Box 23.3 | "Jordon and Boskman, 1984" | Authors are Jordan and Boksman (Goldstein Ch.12 spells correctly). Walton 2002 ref 6 also prints "Boskman", so the error was probably copied |
| Grossman's 14th Ch.23 clinical note | "considerably faster and easier than microabrasion" | Means macroabrasion (Sturdevant's identical sentence); already in B01, now cross-referenced in B13 |
| Grossman's 14th Ch.23 | Microabrasion steps headed "The technique of vital bleaching" | Microabrasion is not bleaching (Walton, Sturdevant's); true only of the H2O2-containing McInnes mix |
| Grossman's 14th Box 23.4 | Modified McInnes: 20% NaOH "dissolves calcium of the enamel at a slower rate" | Doubtful chemistry — alkali does not dissolve hydroxyapatite as acid does [Likely; no book explains] |
| Sikri *Essentials* Ch.24 | Lists microabrasion as a type of in-office bleaching | Misclassification; it removes enamel, it does not oxidize |
| Andreasen 4th Ch.29 (Zachrisson and Toreskog) | "Nocturnal use of 10% hydrogen peroxide gel in a tray" | Its cited ref 14 tested two 10% **carbamide** peroxide gels; 10% HP is about three times stronger [Likely] |
| Bartlett 2011 (extract, not book) | "360 [ctrl] 130 mm" | ± and μ lost in extraction; 360 ± 130 μm |

## 5. Open

- B01 Section 12 Goldstein "truest form of informed consent" — paraphrase without locator, left as the drafter marked it.
- Fundamentals of Color: no printed page numbers in the extract; PDF pages only.
- Modern Operative Dentistry Ch.1 bleaching box may be by Torres and Zanatta (page footer) rather than the four chapter authors; cited under the chapter authors (Torres et al, 2020) — verify.
- B01 at 3451 and B03 at 3435 words: little headroom left (≤65 words) for the other auditors' or editor's changes. B13 at 194/200, P3 at 390/400.
- Bhat et al, McCabe and Walls, Pickard's: nothing usable on discoloration management or microabrasion (Bhat Ch.7 one-line peroxide cytotoxicity; McCabe denture "whitening" only).
