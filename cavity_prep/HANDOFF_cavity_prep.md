# Cavity preparation principles: handoff (2026-10-24)
STATUS: COMPLETE. 16 repository + 3 predicted canonical answers in `canonical/`, drafted by six parallel agents (groups A-F, brief in `BRIEF.md`), merged and checked. Published to the Answer Bank (Version 57, manifest 418 -> 441, files 423 -> 446, 0 lost, live manifest identical to the file sent). Filed under Conservative Dentistry (all 19), Recent Advances (Q03, Q04, Q06) and Dental Materials (Q15). Vault copies in Answers/<Subject>/Cavity Preparation Principles/ and the consolidated folder (vault manifest/index not regenerated, Rule 7).
Question set: `_QUESTIONS.md` (consolidated grouping agreed with Niranjan; non-rotary methods kept as its own 25m Q16; tooth separation deferred to a future Isolation topic; four questions point to existing answers: MI Q11, Composites Q10, Amalgam Q08, Dental Burs Q5).
Tooling: `python3 locators.py` merges `parts/A.py`-`parts/F.py` (1529 phrases, 0 missing; `python3 locators.py a_` checks one group); `python3 build_sources.py canonical/<file>` (safe to re-run).

| File | Marks | Exam core words | Group |
|---|---|---|---|
| Q01 Recent advances in cavity preparation methods | 75 | 2584 | A |
| Q16 Non-rotary methods of tooth preparation | 25 | 947 | A |
| Q02 C-factor and polymerization stress | 50 | 1811 | B |
| Q04 Tooth preparation for tooth-coloured materials | 50 | 1917 | B |
| Q03 Recent advances in Class II cavity design | 50 | 1845 | C |
| P3 Slot and box-only preparations | 10 | 362 | C |
| Q14 Class V cavity designs | 5 | 177 | C |
| Q05 Resistance and retention form, advanced materials | 25 | 862 | D |
| Q10 Cast restorations: indications and cavity design | 20 | 721 | D |
| P1 Principles of cavity preparation (Black's steps) | 20 | 728 | D |
| Q15 Class I amalgam cavity designs (marks assumed) | 20 | 784 | D |
| Q06 Cavosurface treatment for various restorations | 25 | 900 | E |
| Q07 Cavosurface bevel and rounded angles | 25 | 853 | E |
| Q09 Bevels, flares and finish lines | 20 | 775 | E |
| P2 Internal line angles | 10 | 340 | E |
| Q08 Tooth-coloured indirect restorations | 25 | 992 | F |
| Q11 Evolution in tooth preparation | 10 | 365 | F |
| Q12 Class III preparation for direct filling gold | 10 | 332 | F |
| Q13 Class III lesion: treatment plan and management | 7 | 261 | F |

Sources: Sturdevant's 7th ed (2nd South Asia ed), offset 19 in every printed chapter, chapter authors from the contributor list (cited 2019 throughout); Summitt's 4th ed 2013 (no printed pages, PDF page only); Marzouk, Simonton and Gross (offsets differ by chapter: Ch.1 4, Ch.2 4, Ch.5 3, Ch.6 3, Ch.7 2, Ch.9 1, Ch.17-18 -1, Ch.26 -3; year not printed, cited "Marzouk et al, undated" as in refs_meta.json); Harpreet Singh 2e 2020 (17); Garg and Garg 2011 (7); Mount 3e 2016 (16); Modern Operative Dentistry 2020 (chapter-specific); Sikri Indirect Restorations (None) and Textbook of Cons (19); Goldstein 3e 2018; Pickard's 9e/10e; Craig's 14e; Phillips' 12e; McCabe 9e; Lasers in Dentistry 2e; Alani and Patel; Bonsor and Pearson. Full lists in each answer's retrieval report and SOURCE LIST.
Open points: (1) Exam cores near the floor: Q01 2584 (floor 2550), Q07 853 (850), Q05 862 (850); any trim needs a matching addition. (2) Marzouk Class II Designs 3-4 unreadable (blank PDF pp.151-153). (3) Ceramics CD Q10 cites Sikri as ~10° taper and 1.0-1.5 mm depth; the Sikri file gives 10-12° and 2.0 mm: re-check that ceramics answer. (4) Book errors flagged in the answers: Garg (C-factor raises "shrinkage"; bevel angles differ on consecutive pages), Harpreet Singh ("75 mm" for 0.75 mm; Black's system "in the 1930s"), Sturdevant's (inlay "maximum" vs onlay "minimum" 2° taper), Mount (tunnel/slot ridge thresholds inconsistent). (5) Stress-concentration mechanism for sharp internal angles is [RECALL] in Q07/P2. (6) No live literature search, no DCNA articles used.


## Topic-wide optimisation — 2026-11-09

The complete 19-answer set is being aligned to the integrated examination-ready standard. Five previously migrated answers (P1, P2, P3, Q09, Q11) are retained and synchronised; fourteen legacy answers (Q01-Q08, Q10, Q12-Q16) are converted to one student-facing script each, with per-question audit sidecars. The Answer Bank branch updates titles and mark metadata for all 19 answers and regenerates the topic index. Q15 remains explicitly marked as an assumed 20-mark answer because the source paper was unmarked.

Targeted new evidence added:
- Q01 and Q16: Sae-Ferrández et al. (2026), systematic review of Er:YAG, Er,Cr:YSGG and Nd:YAG lasers; 11 studies, no meta-analysis due to heterogeneity and limited long-term outcomes. DOI 10.1016/j.jdent.2025.106264.
- Q02: Zhou et al. (2023), review of C-factor limitations; C-factor alone does not accurately predict shrinkage stress or interface behaviour and applies only under low, near-rigid compliance. DOI 10.1016/j.dental.2023.10.014.
- Q07: Hubsch et al. (2002), finite-element study of cavity shape and adhesive-interface stress; biomechanical evidence, not clinical outcome evidence. DOI 10.1080/1025584021000016861.
- P1 and Q13: Schwendicke et al. (2026), EFCD-ESE-ORCA S3 guideline; selective/stepwise caries removal over non-selective removal in appropriate deep lesions; routine liners not routinely recommended. DOI 10.1111/iej.70132.

Known limitations retained: original locators in the legacy topic dossier are preserved but not rerun in this formatting pass; source disagreements on bevel geometry, tunnel-preparation indications/outcomes and cast-restoration taper are not forced into a single numerical rule. See each audit sidecar for question-specific open points.

**Publication state:** proposed on feature branches; not in production until the paired pull requests are reviewed and merged.
