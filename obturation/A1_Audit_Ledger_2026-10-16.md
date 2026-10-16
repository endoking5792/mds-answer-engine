# A1. Audit ledger: obturation (2026-10-16)

**Marks: n/a (reviewer ledger)**

**Scope:** 61 specific figures, definitions and attributions from the 22 obturation answers, re-checked by text search against the chapter cited, in the private repo `endoking5792/mds-textbooks`. Tool: `tools/endo_audit/verify_claims.py` with `claims_obturation.json`.

## Result
- Present in the cited chapter: 60 of 61. The one regex miss (claim 26, Trifecta "1.0-2.0 mm of alpha-phase Successfil") is a typographic mismatch (en dash and alpha sign); the text was read and matches.
- A hit proves the string is in the chapter, not that the answer reads it correctly; contradictions were read in context (see HANDOFF).
- **Not covered by this ledger:** statements from the journal articles (Jafari and Jafari 2017; Karagenc et al 2006 at abstract level) and [RECALL] items; general statements without a number.
- **Not verifiable from the textbooks:** primary studies cited second-hand (Schilder, McSpadden, Ricucci, Molven, Augsburger and Peters, Tennert, Barborka).

## Ledger
| # | Answer | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | Q1 | Grossman requirements, Cohen's Box 9.2 | Cohen's 12e Ch.9 | OK |
| 2 | Q1 | West's seventeen requirements | Ingle's 7e Ch.22 | OK |
| 3 | Q1 | Silver cones (Sikri) | Sikri 2e Ch.20 | OK |
| 4 | Q1 | Jasper silver points 1933 | Ingle's 7e Ch.22 | OK |
| 5 | Q2 | GP 18-22% (Sikri) | Sikri 2e Ch.20 | OK |
| 6 | Q2 | ZnO 59-67% (Sikri) | Sikri 2e Ch.20 | OK |
| 7 | Q2 | ZnO 59-76% (Ingle's) | Ingle's 7e Ch.22 | OK |
| 8 | Q2 | ZnO 50-79% (Azim and Aksel) | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |
| 9 | Q2 | Cohen composition 20/65/10/5 | Cohen's 12e Ch.9 | OK |
| 10 | Q2 | Weine beta to alpha 42-49 | Weine's Endodontic Therapy Ch.7 | OK |
| 11 | Q2 | Weine gamma 56-62 | Weine's Endodontic Therapy Ch.7 | OK |
| 12 | Q2 | Torabinejad et al amorphous 53-59 | Torabinejad et al, Endodontics: Principles and Practice Ch.15 | OK |
| 13 | Q2 | Azim and Aksel alpha at 70 C | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |
| 14 | Q2 | Cohen alpha melts above 65 C | Cohen's 12e Ch.9 | OK |
| 15 | Q2 | Hill 1847 | Grossman's 14e Ch.16 | OK |
| 16 | Q3 | Contamination 5-8% | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |
| 17 | Q3 | Contamination about 20% after opening | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |
| 18 | Q3 | 2% CHX effective (Sikri) | Sikri 2e Ch.20 | OK |
| 19 | Q3 | Cohen: CHX etc not effective vs spores | Cohen's 12e Ch.9 | OK |
| 20 | Q3 | PVP-iodine 10% (Sikri) | Sikri 2e Ch.20 | OK |
| 21 | Q6 | Thermafil 1978 (Grossman) | Grossman's 14e Ch.16 | OK |
| 22 | Q6 | ThermaPrep Plus 10 s | Grossman's 14e Ch.16 | OK |
| 23 | Q6 | Sikri oven 115 C 3-7 min | Sikri 2e Ch.20 | OK |
| 24 | Q6 | cool 2-4 min | Grossman's 14e Ch.16 | OK |
| 25 | Q6 | Thermafil gutta-percha resolidifies 90 s | Ingle's 7e Ch.22 | OK |
| 26 | Q7 | Trifecta 1-2 mm Successfil | Sikri 2e Ch.20 | OK* |
| 27 | Q7 | Trifecta named (Torabinejad et al) | Torabinejad et al, Endodontics: Principles and Practice Ch.15 | OK |
| 28 | Q7 | Ultrafil 70-90 C | Sikri 2e Ch.20 | OK |
| 29 | Q9 | McSpadden 8,000-20,000 rpm | Sikri 2e Ch.20 | OK |
| 30 | Q9 | MicroSeal 1000-4000 rpm | Sikri 2e Ch.20 | OK |
| 31 | Q10 | MTA plug 3-6 mm (Azim) | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |
| 32 | Q10 | MTA plug 4-5 mm (Sikri) | Sikri 2e Ch.20 | OK |
| 33 | Q11 | Double seal definition (Grossman) | Grossman's 14e Ch.15 | OK |
| 34 | Q11 | Cavit 3.5 mm | Grossman's 14e Ch.15 | OK |
| 35 | Q11 | leak after 3 weeks | Grossman's 14e Ch.15 | OK |
| 36 | Q12 | Cavit 85% / Super EBA 65% | Cohen's 12e Ch.9 | OK |
| 37 | Q12 | 12-14% per mm | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |
| 38 | Q12 | Coronal seal most controllable (Walton) | Walton and Torabinejad (2002) Part 19 | OK |
| 39 | Q13 | no standardised leakage technique (Cohen) | Cohen's 12e Ch.9 | OK |
| 40 | Q13 | clinical significance unknown (Walton) | Walton and Torabinejad (2002) Part 15 | OK |
| 41 | Q8 | System B <10 C | Cohen's 12e Ch.9 | OK |
| 42 | Q8 | Obtura II 160 C (Cohen) | Cohen's 12e Ch.9 | OK |
| 43 | Q8 | Obtura 160-200 (Sikri) | Sikri 2e Ch.20 | OK |
| 44 | Q8 | needle 4-6 mm (Ingle's) | Ingle's 7e Ch.22 | OK |
| 45 | Q8 | needle 3-5 mm (Sikri) | Sikri 2e Ch.20 | OK |
| 46 | Q8 | Endotec 350 C | Sikri 2e Ch.20 | OK |
| 47 | Q14 | BioConeless foramen cut-off 0.7 mm | Bioceramics in Endodontics Ch.12 | OK |
| 48 | Q14 | single cone sealer-dependent | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |
| 49 | Q15 | 96% repair (Augsburger and Peters) | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |
| 50 | Q15 | sealer extrusion ~50% | Azim and Aksel, Treatment of Endodontic Infections 2e Ch.15 | OK |
| 51 | Q15 | 25% reduction (Grossman) | Grossman's 14e Ch.16 | OK |
| 52 | Q15 | equivocal evidence (Harty) | Harty's 7e Ch.9 | OK |
| 53 | Q16 | All materials leak (Cohen) | Cohen's 12e Ch.9 | OK |
| 54 | Q17 | Toronto studies (Cohen) | Cohen's 12e Ch.9 | OK |
| 55 | Q17 | Single-visit criteria Box 16.12 | Grossman's 14e Ch.16 | OK |
| 56 | Q17 | A seal cannot be seen (Problem Solving) | Problem Solving Ch.12 | OK |
| 57 | P3 | older sealers same outcome (Prognosis) | Endodontic Prognosis Ch.9 | OK |
| 58 | P4 | Hedström retrieval (Problem Solving) | Problem Solving Ch.12 | OK |
| 59 | P4 | Ricucci overfilling (Bioceramics Ch.12) | Bioceramics in Endodontics Ch.12 | OK |
| 60 | P1 | GP not condensable (Ingle's) | Ingle's 7e Ch.22 | OK |
| 61 | P5 | ZAP and TAP (Sikri) | Sikri 2e Ch.20 | OK |

`OK*`: confirmed by reading the passage; the regex missed on punctuation.
