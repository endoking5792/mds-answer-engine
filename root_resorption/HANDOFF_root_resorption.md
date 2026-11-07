# Root Resorption — topic handoff (Roseline, 2026-11-07)

Question set: `_QUESTIONS.md` (Endodontics §13 + Recent Advances §12 + Manipal line; 4 answers + 2 predicted). Drafted by four parallel agents, checked and fixed by the coordinating session.

| File | Marks | Exam core (words) | Locators |
|---|---|---|---|
| `canonical/Q01_Root_Resorption_100m_CANONICAL.md` | 100 | 3490 | 324 |
| `canonical/Q02_Classification_and_Management_of_Internal_Resorption_25m_CANONICAL.md` | 25 | 996 | 190 in file |
| `canonical/Q03_Heithersay_Classification_of_External_Cervical_Resorption_and_Management_10m_CANONICAL.md` | 10 | 398 | 108 in file |
| `canonical/Q04_Apical_Resorption_10m_CANONICAL.md` | 10 | 398 | 84 |
| `canonical/P1_Differentiating_Internal_from_External_Cervical_Resorption_10m_PREDICTED_CANONICAL.md` | 10 | 394 | 74 |
| `canonical/P2_External_Inflammatory_Resorption_after_Trauma_10m_PREDICTED_CANONICAL.md` | 10 | 397 | 91 |

`python3 locators.py` → checked 871 missing 0 (after the second read). `python3 build_sources.py canonical/*.md` → all OK. Locators are split per question (`locators_<QID>.py`, keys prefixed) so parallel drafters never edit the same file; `locators.py` loads them.

## Sources and offsets (printed page = PDF marker − offset; checked at 2+ pages per chapter)
- Cohen's 12e Ch.18 (Patel, Durack, Ricucci, Bakhsh) — PDF page only. Tables 18.1 (Patel 3D ECR classification) and 18.2 are empty in the extract.
- Ingle's 7e Ch.15 (Andreasen, Heithersay, Bakland) — offset −48; author line decoded from garbled OCR, verify against the printed book.
- Gulabivala & Ng 4e Ch.11 (chapter authors Ng and Gulabivala, cited "Ng and Gulabivala, 2014") — offset 9.
- Endodontology Ch.42 (Baumann and Beer, 2010) — offset 17. Seltzer & Bender 2e Ch.17 (Levin, 2012) — PDF page only. Sikri 2e Ch.27 (2019) — offset 21. AAE Glossary 8th ed (2012) — PDF page only.
- Extra (in per-question files): Grossman 14e Ch.4/5/19 (offset 25), Cohen's Ch.21 (Kahler, PDF page only), Harty's 7e Ch.12 (Sigurdsson and Bourguignon, offset 16, year 2017 not printed in the file), Torabinejad 6e Ch.11 (Paranjpe and Noblett, offset 7; editor names not verified from the file), Endodontic Radiology 2e Ch.10 (offset 20).

## Book conflicts kept side by side
Classification schemes (Cohen's location / Andreasen biology / Ng and Gulabivala sustaining stimulus / Levin / AAE / Sikri); cervical terminology (ECR vs invasive cervical vs subepithelial inflammatory); pink spot (Sikri "usual" in internal resorption vs Cohen's rare in both vs others either); perforating internal defects (MTA from inside vs long-term Ca(OH)2 vs surgery); TCA by Heithersay class; class 4 management; Ca(OH)2 duration and fracture risk; RCT timing after replantation (7-10 days vs 2 weeks); replacement-resorption thresholds; transient apical breakdown (luxation vs orthodontic); cysts resorb vs displace roots.

## Fixes made at check
- Q03: "intentional replantation" removed from the exam core (in no chapter read); kept in the Explanation as [RECALL].
- All answers: Gulabivala citation changed from the editors' form to the chapter authors (Ng and Gulabivala, 2014).

## Second read (2026-11-07)
Five independent second readers (Q01 split in two halves, read-only with proposed edits applied by the coordinator; Q02; Q03+P1; Q04+P2) opened the cited locators in context. 81 findings, all fixed: Q01 39 (20 + 19), Q02 13, Q03/P1 14, Q04/P2 15. Typical: misattributions (Howship lacunae, pulpotomy, Bender's neuropeptides, obturation timing to Kahler), manufactured disagreements replaced by the real ones (TCA by class; calcium hydroxide duration), missed disagreements added, unsourced exam-core items removed (intentional replantation, cervical barrier, without coolant, 6-12-month recall). Ledgers in `audit/` (q01a, q01b, q02, q03_p1, q04_p2).

## Published
2026-11-07 to the Answer Bank site as Endodontics / Root Resorption (new topic): added 6, updated 0, manifest 541 -> 547 entries, 0 lost (site commit a683721).

## Open
- No [LIT]: PubMed and the article hosts for Patel's 3D ECR classification would not open, so its grades are [RECALL] in Q01.
- Q04 "loss of the apical constriction" is an inference tagged [Likely]; P2 does not say which apex group Grossman's timing table applies to (table garbled).
- Exam cores are at the ceiling: Q01 3490/3500, Q02 996/1000, Q03 398, Q04 398, P1 394, P2 397 (of 400); any addition needs an equal cut.
- Q01 section 9 exam core cites only Ng and Gulabivala for the impacted-teeth examples (sourced in the explanation; adding citations would cost 8 words). Ingle's garbled table lists corticosteroids among factors promoting resorption yet calls topical cortisone promising; not used.
- Grossman Ch.19 chart columns (open vs closed apex) unverified; Harty's year not in the file.
- Vault copies not made.
