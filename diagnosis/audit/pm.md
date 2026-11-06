# Audit ledger pm: second reader and Harty's audit (2026-11-06)

Answer: `canonical/B4_Inflammatory_Mediators_in_Pulpal_Disease_25m_CANONICAL.md` (25m). Locator file: `loc_pm.py`.

**Summary.** All 209 original locators were opened in context (about 220 characters either side of each phrase, script-dumped and read), plus the two statements that had no locator. 16 findings corrected or tightened; the rest held up. 24 locators added (233 in all). Final exam core: 999 words (range 850 to 1000; no FAILURE DISCLOSURE). `python3 locators.py pm_` gives checked 233, missing 0.

Offsets and author lines confirmed: Harty's Ch.5 (H. F. Duncan, A. J. Smith and P. R. Cooper) offset 16 (PDF 81 = p.65, PDF 93 = p.77); Harty's Ch.3 (N. P. Chandler and B. S. Chong) offset 16 (PDF 39 = p.23, PDF 51 = p.35); Ingle's Ch.4 offset -24 (PDF 102 = p.126, PDF 111 = p.135). Seltzer Ch.11 author line "Ashraf F. Fouad" seen on the opening page.

## Task A: corrections

| # | Location | Finding | Evidence | Action |
|---|---|---|---|---|
| 1 | S4 expl, leukotrienes | Cohen's Table 13.3 cited with no locator. The table exists, but it is a general nociceptor table "Modified from Fields H: Pain, New York, 1987", not pulp-specific, and gives ± for human volunteers. Fouad's "not conclusive" rests on two pulp studies with opposite results. | Cohen's Ch.13 PDF 1734 "Leukotrienes27,234 Sensitize"; Seltzer Ch.11 PDF 457 "LTB 4 increased pulpal nerve excitability under similar conditions in another study" | fixed: 4 locators; conflict kept side by side with these qualifiers; [Likely] on the reading |
| 2 | S6 expl, lymphatics | Ikeda and Suda statement had no locator. Also the conflict was understated. Ikeda and Suda say "Dental pulp contains lymphatic vessels", count lymph outflow as a factor keeping the pressure rise local, and say the vessels close in prolonged inflammation. Cohen's says "contradictory conclusions have been drawn", then concludes the pulp has no draining lymphatics. | Seltzer Ch.6 PDF 212, 218 ("Third, increased lymph outflow will reduce both interstitial tissue fluid volume"), 239; Cohen's Ch.13 PDF 1760 | fixed: rewritten with 6 locators; three books side by side, not ranked |
| 3 | S4 expl + exam table, IL-6 | The conflict was overstated. Ingle's lists IL-6 as pro-inflammatory, but its periapical section reports that endogenous IL-6 is anti-inflammatory (IL-6 knockout mice resorb more bone). The books differ in how they classify IL-6, not in the data. | Ingle's PDF 111 "modulating infection-stimulated bone destruction in vivo"; Seltzer PDF 479, 485 | fixed (explanation; exam row now "both report both actions") |
| 4 | S4 expl, SOD | The conflict was incomplete. Ingle's calls the SOD findings "controversial" and, after the study showing a reduction, reports that qRT-PCR mRNA for both SODs "does increase in pulpitis". Most of the data in both books point to an increase. | Ingle's PDF 102 | fixed: added, with [Likely] on the summary |
| 5 | S4 exam table, serotonin | The row set "vasoconstriction (Fristad and Berggreen)" against "raised flow (Fouad)". But Fouad also says serotonin "generally causes vasoconstriction". So the dog finding conflicts with Fouad's own summary as well as with Cohen's. | Seltzer PDF 442; Cohen's PDF 1764 | fixed (row reworded; explanation already correct) |
| 6 | S6 exam + expl, 84.4% | "Coronal abscess or necrosis" is not the book's wording, and the 84.4% comes from a single cited study with n=32. The book says "areas of coagulation or liquefaction necrosis with bacterial colonization ... in parts of the coronal pulp". The other 15.6% were histologically reversible. | Essential Endodontology PDF 78 (p.65) | fixed: "in one study ... partial coronal necrosis with bacteria"; n=32 and 15.6% added to the explanation |
| 7 | S6 exam + expl, 16.3 vs 7.0 mm Hg | The measurement was made in cat pulp; the answer did not say so. | Seltzer Ch.6 PDF 217 | fixed |
| 8 | S7 expl + exam, MTA | "MTA releases ... cytokines" misreads the book. Harty's says the cytokines "are released from mineralizing cells after exposure to MTA" (in vitro). | Harty's Ch.5 PDF 93 | fixed |
| 9 | S4 exam table, growth factors | "VEGF raises permeability" was cited to Duncan, Smith and Cooper. That claim is Cohen's (Fristad and Berggreen); Harty's gives the dentine-matrix release and angiogenesis. | Cohen's PDF 1765; Harty's PDF 93 | fixed (citation split) |
| 10 | S5 expl + exam, painless pulpitis | The exam core said "opioid receptors and NPY may explain painless pulpitis". Cohen's links only the opioid receptors to asymptomatic cases; it calls NPY a modulator of neurogenic inflammation. Fouad's own explanation (inhibitory transmitters such as GABA and gastrin-releasing peptide) was missing. | Cohen's Ch.14 PDF 1847; Seltzer PDF 447 | fixed (NPY removed from that claim; GABA added to the explanation; high-yield line amended) |
| 11 | S1 expl | "The pulp makes most known host mediators" overstates the book, which says "a large number". | Seltzer PDF 439 | fixed: now a verbatim quote with a locator |
| 12 | S5 exam | "Raised pressure on lying down explains nocturnal pain": Cohen's says PBF "probably increases". | Cohen's PDF 1766 | fixed: "may explain"; Harty's Ch.3 added as a source |
| 13 | S6 expl + exam | "Necrosis spreads compartment by compartment" was [Likely]. Ikeda and Suda state it: "total pulpal necrosis represents the gradual accumulation of local necrosis". | Seltzer Ch.6 PDF 239 | fixed: converted to [SRC], cited in the exam core |
| 14 | Exam conclusion | "Driven less by bacteria directly than by the host mediators" went beyond the source ("may contribute"). | Seltzer PDF 439 | fixed: reworded; 4 words saved |
| 15 | High-yield | "Strangulation is refuted" ranked one side of a reported conflict. | n/a | fixed: Ikeda and Suda and Fristad and Berggreen named, with Sikri alongside |
| 16 | Mnemonic | The answer did not say the mnemonic is the drafter's own. | n/a | fixed: labelled "Memory aid only (the drafter's own, not from any textbook)" |

**Checked and held up (selected):** Cohen's Ch.14 does call it "the vasoactive amine bradykinin" (PDF 1846, Fouad and Levin), and the flag that this is wrong stands: Seltzer calls BK "the nonapeptide bradykinin" (PDF 464), and Fouad's own vasoactive-amine list there omits BK. Complement "20 different plasma proteins" (Seltzer PDF 465) against "~45 proteins" (Ingle's PDF 98) is a real conflict. Strangulation conflict: Ikeda and Suda "have refuted the concept of pulpal strangulation" (PDF 218), with the "major insults" exception; Fristad and Berggreen "contradicting the old concept" (PDF 1764); Sikri "venules to collapse" (PDF 101); Fouad "stasis ... eventually ensues" (PDF 441). All are verbatim and correctly attributed. Serotonin: the Fouad dog-flow finding, Fristad and Berggreen's reduced PBF and the female-only CGRP effect (PDF 1843 to 1844) all verified. Other figures verified: 13-fold BK; 9.3-fold PGE2; about 23-fold IL-8; 4-fold histamine; PAF 100 to 1,000 times; VEGF 50,000 times; 200% flow; PGE2 60%; 40% to 60% painless pulpitis; 0.5 mm (Harty's) against noncavitated lesions (Cohen's). Also verified: catalase; NO maximum at 4 days; IL-1/TNF receptor-knockout protection; the neutrophil-first sequence (Fouad and Khan, Sikri) against chronic cells first (Cohen's); the Dohi eugenol data. The retrieval report already said that Fouad wrote or co-wrote four of the chapters (Seltzer Ch.11, Ingle's Ch.4, Cohen's Ch.14, Essential Endodontology Ch.3); confirmed and kept.

## Task B: Harty's additions and conflicts

| # | Section | Harty's chapter | Addition / conflict | Action |
|---|---|---|---|---|
| H1 | S5 | Ch.3 Chandler and Chong | Pain is worse lying down or bending over, through raised intrapulpal pressure. This agrees with Cohen's and states it more firmly. | added (explanation; exam core citation) |
| H2 | S5 | Ch.3 | After a thermal stimulus, a sharp Aδ pain, then "a dull, throbbing C-fibre ache". | added (explanation) |
| H3 | S5 | Ch.3 | Irreversible pulpitis may progress from symptom-free to necrosis (supports painless pulpitis). | added (explanation) |
| H4 | S4 | Ch.5 Duncan, Smith and Cooper | IL-1α, IL-1β and TNF-α named as the archetypal pro-inflammatory cytokines. | added (explanation) |
| H5 | S7 | Ch.5 | The reparative action of CH/MTA "appears to involve dampening pulpal inflammation". | added (explanation) |
| H6 | S1 to S7 | Ch.5 | All 20 existing Ch.5 locators re-verified. One misreading (MTA, row 8) and one misattribution (VEGF, row 9) fixed. The existing conflicts (lymph vessel formation; 0.5 mm) held up. | kept / fixed |

Harty's Ch.3 has no mediator content: no prostaglandins, bradykinin or neuropeptides. It adds only the clinical pain pattern.

## Open points for Niranjan
- The exam core is at 999/1000. Any later addition needs an equal cut.
- The Cohen's Table 13.3 locator is a table row and includes the reference numbers ("Leukotrienes27,234 Sensitize"). It is verbatim but reads awkwardly.
- BOOK entries: the Seltzer editors and the Ingle's Ch.4 author line (decoded from garbled OCR) are still flagged "verify against the printed book".
- Ingle's grammar "levels ... has been controversial" is quoted with (sic).
