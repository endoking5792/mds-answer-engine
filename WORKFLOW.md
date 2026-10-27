# Parallel-work workflow (Niranjan + Roseline + Medhinir)

Read this before starting any topic work, alongside `HANDOFF.md`. Goal: three people, each driving their own Claude Code session, can work at the same time without silently overwriting each other.

Collaborators: `rosyposy0406` (Roseline), `medhinirbhagwat` (Medhinir) — both have Write access on all four repos (`mds-answer-engine`, `dental-study-material`, `Vault`, `dental-study-notes`) and editor access on the Answer Bank artifact.

## Why collisions are rare here

Work is split by **topic folder** (`amalgam/`, `calcium_silicate/`, `impression/`, `irrigants/`, `medicaments/`, `post_core/`, plus the matching folders in the `dental-study-notes` vault). People working on *different* topics never touch the same files. The only real collision risks are:
1. Two (or three) people working the **same topic** at once.
2. Both editing a **shared file** the same day (`HANDOFF.md`, vault `00_INDEX.md`, Answer Bank `manifest.json`).

The rules below just manage those two cases.

## Rule 1 — Claim a topic before starting

Before you (or your Claude session) start building/auditing a topic, check the table below and add/update your row. Commit and push **just that one-line change** immediately — don't wait until the topic is finished — so the other person sees it within seconds of pulling.

| Topic | Status | Owner | Since |
|---|---|---|---|
| amalgam | FINAL | Niranjan | done |
| calcium_silicate | FINAL | Niranjan | done |
| impression | unaudited draft | — unclaimed — | — |
| irrigants | unaudited draft | — unclaimed — | — |
| medicaments | unaudited draft | — unclaimed — | — |
| post_core | audited, Q1-Q8 patched/added, Answer Bank republished (OneDrive docx not rebuilt) | Roseline | 2026-10-14 |
| composites | FINAL across all three repositories, now including a deep textbook audit (6 parallel readers, 13 primary textbooks) on top of the original build — all 42 answers patched, vault + Answer Bank published and verified | Niranjan | 2026-10-15 |
| ceramics | FINAL — deep textbook audit complete (5 parallel readers, 11 primary textbooks), all 35 answers patched, vault + Answer Bank published and verified | Roseline (draft); Niranjan (audit) | 2026-10-14 |
| smart_materials | first-draft complete (4 questions: CD 10m+100m, RA 25m, Endo 100m) — literature-only topic (no standing textbook covers it), no audit applicable in the usual textbook-patch sense; vault + Answer Bank published and verified (157 live files, count-checked) | Niranjan | 2026-10-15 |
| endodontic_sealers | complete (10 answers); primary-textbook audit applied 2026-10-16 (Cohen's, Grossman's, Ingle's, Sikri, Jain, Azim and Aksel); second pass applied; Niranjan spot-check items 1, 2 and 5 done 2026-10-16 (item 1: printed-page checks, all 7 disputed editors/years confirmed; item 2: all 12 contradictions in the A0 table decided — resolved, clarified as non-conflicts, or explicitly kept side by side, including a new finding that Sikri misclassifies two epoxy-resin sealers as a "fifth" methacrylate generation; item 5: Q2/Q3 late additions verified accurate against Harty's and Applied Dental Materials, no corrections needed); checklist essentially closed for this topic, item 4 is acknowledgement-only; **published to the Answer Bank 2026-10-16** (additive, publish_guard.py merge + verify, VERIFY OK, 243 manifest entries / 247 files unchanged, 0 lost) | Roseline (spot-check: Niranjan) | 2026-10-16 |
| obturation | first draft complete (17 repository answers + 5 predicted), Exam Mode expanded to Section 7 ranges 2026-10-16, published to Answer Bank; textbook audit applied at drafting; claim ledger built (60/61); Niranjan spot-check items 1, 2, 3 and 5 done 2026-10-16 (item 1: editors/years confirmed; item 2: gutta-percha phase, Obtura temperature and chlorhexidine contradictions resolved or clarified; item 3: Karagenç et al 2006 read as the complete PubMed abstract (PMID 16831682, full text paywalled), a micro-CT source added for obturation quality (Hammad et al 2009, PMID 19345801) in Q13 and P3; item 5: Q8 technique-comparison table and Q14's Calamus 38-44°C figure verified directly against the printed books, both confirmed accurate as stated); item 4 is acknowledgement-only; a pre-existing Exam Mode word-count discrepancy flagged in Q02/Q08/Q03/Q13 for a later verification pass; checklist in HANDOFF_NIRANJAN_2026-10-16.md is closed except that pass; **published to the Answer Bank 2026-10-16** (additive, publish_guard.py merge + verify, VERIFY OK, 243 manifest entries / 247 files unchanged, 0 lost) | Roseline (audit: Niranjan) | 2026-10-16 |
| dental_burs | FINAL — deep textbook audit (Marzouk's/Sturdevant's/Summitt's/Pickard's) plus a second pass against 4 user-supplied primary-literature cutting-efficiency papers (JADA 1996/1998/2000 + EJPRD 2025); 8 answers total (new predicted Q8 added); corrected rake-angle-geometry error and a grit-size-vs-cutting-rate misconception; vault + Answer Bank republished and verified (248 live files, 0 lost) | Niranjan | 2026-10-16 |
| dentin_bonding | FINAL — deep textbook audit complete against 9 sources (Alani&Patel/Nakabayashi&Pashley/Perdigão/Sturdevant's/Summitt's/Pickard's/Marzouk's/Craig's/Van Noort's/McCabe's/Philips'), all 46 answers patched; smear layer deliberately kept as a separate future topic; vault + Answer Bank republished and verified (210 live files, 0 lost) | Niranjan | 2026-10-16 |
| glass_ionomer_cement | FINAL — deep textbook audit complete against `mds-textbooks` (11 verification readers, 6 gap readers, 3 readers on books new to the repo), all 26 answers patched with S-AUDIT addenda, new predicted P10 added, Answer Bank republished and verified (247 live files, 0 lost); vault/OneDrive copies NOT yet synced | Medhinir | 2026-10-16 |
| minimal_intervention | FINAL — 15 answers (Q1-Q11 from the Conservative Dentistry and Recent Advances repositories, one answer per distinct question, plus 4 predicted P1-P4) drafted from `mds-textbooks`; 4 verification readers re-checked every cited sentence, all findings that held up applied; 987 of 987 locators exact; Answer Bank republished (Conservative Dentistry / Minimally Invasive Dentistry, 260 manifest entries, 0 lost); vault/OneDrive copies NOT yet synced | Medhinir | 2026-10-18 |
| casting_alloys_defects | FINAL — 20 answers (Q1-Q17 from the Dental Materials and Conservative Dentistry repositories, one answer per distinct question, plus 3 predicted P1-P3) drafted from `mds-textbooks`; independent readers re-checked every cited sentence, findings that held up in the book applied; 740 of 740 locators exact; Answer Bank updated (Dental Materials / Casting Alloys and Defects, 373 manifest entries, 0 lost). Ceramics CD Q18 and Ceramics DM Q8 were REWRITTEN from the new sources and replaced at their existing Answer Bank paths (the old copies in `ceramics/` are replaced in this commit). No audit ledger written (user said not required); vault/OneDrive copies NOT yet synced | Medhinir | 2026-10-22 |
| endodontic_microbiology | IN PROGRESS (claimed 2026-10-18): 20 first-draft answers from the Endodontics repository section 19 (Endodontic Microbiology & Biofilms): biofilm, microflora/E. faecalis, culture, molecular methods, extraradicular biofilm, antibiotics, flare-ups, failure, biofilm models, biofilm-restoration, hard-tissue homeostasis; textbook-only first drafts; published to the Answer Bank 2026-10-18 (Q01-Q12 published additively 300 -> 312 manifest entries; Q13-Q20 added in a second additive publish); second-reader check and vault/OneDrive copies NOT done | Roseline | 2026-10-18 |
| microleakage | FINAL-DRAFT — 9 repository answers (Q1–Q9: 20m×4, 10m×3, 5m×2 incl. Endo cross-subject Q8/Q9), 2 predicted (P1, P2); Q10/Q11 unmarked titles mapped to Q2/Q4, not drafted separately; textbook + PubMed + Drive-PDF checks 2026-10-18 | Niranjan | 2026-10-18 |
| smear_layer | FIRST DRAFT — 10 repository answers (Q01 75m, Q02-Q03 50m, Q10 25m, Q04-Q06 20m, Q07-Q08 10m, Q09 5m) + 2 predicted (P1, P2) in `smear_layer/`; textbooks (mds-textbooks), 3 DCNA articles and PubMed abstracts; Exam Mode meets Section 7 range for Q01/Q02, 4-12% under for the rest (disclosed in each file); not audited; published to the Answer Bank 2026-10-18 (additive, publish_guard merge, manifest 271 -> 283, 0 lost, 275 -> 287 files, Version 34) | Niranjan | 2026-10-18 |
| surgical_endodontics | FIRST DRAFT — 14 repository answers (Q01 100m, Q02 50m, Q03-Q04 20m, Q06/Q08/Q11/Q12 25m, Q05/Q07/Q09/Q10/Q13 10m, Q14 7m) + 3 predicted (P1-P3) in `surgical_endo/`; Endodontics §25 plus Recent Advances §6 and the Manipal/TN-MGR addendum, with two Diagnosis-section items (healing, non-microbial causes); textbooks (mds-textbooks), DCNA articles and PubMed abstracts; Exam Mode in the Section 7 range except Q04 (815 words, 15 over, accepted by Niranjan); citations by chapter author; source conflicts flagged by author; not audited; published to the Answer Bank 2026-10-18 (additive, publish_guard merge, manifest 283 -> 300, 0 lost, Version 35); vault consolidated copy added, .docx not built | Niranjan | 2026-10-18 |
| traumatic_dental_injuries | FINAL-DRAFT, IADT-audited 2026-10-19 — 20 repository answers (T01-T20, 100m umbrella to 7m) + 3 predicted (P1-P3) in `traumatic_dental_injuries/`; every IADT 2020 claim checked against the supplied PDFs (ledger `AUDIT_IADT_2026-10-19.md`); Exam Mode within Section 7 ranges; published to the Answer Bank 2026-10-19 (Version 44; then Version 45 with the textbook re-audit corrections; publish_guard merge + verify, VERIFY OK, 344 manifest entries / 349 files, 0 lost); OneDrive .docx built; vault copies written (85 consolidated index entries not yet synced to the vault folder) | Niranjan | 2026-10-19 |
| endo_perio | FIRST DRAFT COMPLETE 2026-10-22: 10 repository answers (Q01 100m, Q02 75m, Q03 50m, Q04 25m, Q05 20m, Q06 25m, Q07 10m, Q08 5m, Q09 10m, Q10 10m) + 3 predicted (P1-P3) in `endo_perio/`; every Exam Mode within Section 7 ranges; 261 locators verified against `mds-textbooks`; Herrera 2018 read in full; published to the Answer Bank 2026-10-22 (Version 49, additive, 342 -> 355, 0 lost); vault and OneDrive .docx done; see `endo_perio/HANDOFF_endo_perio.md` | Niranjan | 2026-10-22 |
| single_multi_visit | FINAL — 7 canonical answers (Q1 75m umbrella, Q2-Q3 50m, Q4-Q5 20m, Q6-Q7 10m; Q3 merges 11 wordings at 50m) in `single_multi_visit/canonical/`; Endodontics §21 (4 off-topic items moved to new §21A); textbooks (mds-textbooks: Sikri, Endodontology, Siqueira & Rôças, Cohen's, Ingle's, Grossman, Harty's, Weine) + PubMed abstracts; two rounds of parallel source and rules review, all fixes applied; exam cores in Section 7 ranges; 310/310 locators verified; chapter-author citations; published to the Answer Bank 2026-10-22 (Version 53, publish_guard merge, 373 -> 380 entries, 378 -> 385 files, 0 lost); OneDrive .docx built; vault copies written | Niranjan | 2026-10-22 |
| procedural_errors | FINAL — 9 repository answers (Q01 75m; Q05 Perforation and Q09 Ledge upgraded to 100m; Q02-Q04 20m; Q07 25m; Q08, Q10 10m) + 3 predicted (P1-P3) as canonical answers in `procedural_errors/canonical/`; Endodontics §12 plus §5 separation items; textbooks (mds-textbooks: Cohen's Ch.10/20, Ingle's Ch.23, Grossman's Ch.17, Torabinejad 6th Ch.18, Harty's Ch.14, Endodontology Ch.43, Hülsmann & Schäfer Ch.17, Molar Guidebook Ch.11, Common Complications Ch.5-6, AAE Glossary); 378 locators verified; published to the Answer Bank 2026-10-22 (Version 54, publish_guard merge, 380 -> 392, 0 lost); vault copies written | Niranjan | 2026-10-22 |
| cavity_prep | FINAL-DRAFT — 16 repository answers (Q01 75m; Q02-Q04 50m; Q05-Q08, Q16 25m; Q09, Q10, Q15 20m; Q11, Q12 10m; Q13 7m; Q14 5m) + 3 predicted (P1 20m, P2-P3 10m) as canonical answers in `cavity_prep/canonical/`, drafted by six parallel agents; Conservative Dentistry §6 + Recent Advances §25 + Dental Materials §16; tooth separation deferred to Isolation; textbooks (mds-textbooks: Sturdevant's 2e SA, Summitt's, Marzouk, Harpreet Singh, Garg, Mount, Modern Operative, Sikri, Goldstein, Pickard's, Craig's, Phillips', McCabe); 1529 locators verified; published to the Answer Bank 2026-10-24 (Version 57, publish_guard merge, 418 -> 441, 0 lost); vault copies written | Niranjan | 2026-10-24 |
| gingival_tissue | FINAL-DRAFT — 8 canonical answers (Q1 100m umbrella, Q2 50m, Q3 25m, Q4-Q8 10m; Q7/Q8 set at 7m, rounded to 10m; no predicted) in `gingival_tissue/canonical/`, drafted by five parallel agents; Conservative Dentistry §8 + Recent Advances Apr 2013; textbooks (mds-textbooks: Sturdevant's Ch.8/10/23, Summitt's Ch.1/2/15/18, Sikri Ch.2/10, Goldstein Ch.41, Ricketts Ch.13, Valerio Ch.10, Marzouk Ch.20, Coluzzi Ch.15) + Martins 2020 meta-analysis (abstract); 523 locators verified; all exam cores in range; published to the Answer Bank 2026-10-24 (Version 58, publish_guard merge, 441 -> 450, 0 lost); vault copies written | Niranjan | 2026-10-24 |
| inlay_wax | FINAL — 3 canonical answers (Q1 100m umbrella absorbing 8 wordings, Q2 10m flow, Q3 100m indirect wax pattern; classification of waxes and direct-vs-indirect folded in as predicted) in `inlay_wax/canonical/`; Dental Materials §9 + Conservative Dentistry; drafted by three parallel agents; textbooks (mds-textbooks: Phillips', Craig 11th, Bhat, Powers & Wataha, McCabe, Bonsor & Pearson, Craig 14th, Marzouk, Sturdevant SA, Advanced Operative Dentistry, Garg, Singh, Sikri) + 3 PubMed abstracts; 306 locators verified; exam cores 3320/391/3338; no separate review pass yet; published to the Answer Bank 2026-10-27 (Version 64, publish_guard merge, 487 -> 490, 0 lost); vault copies written | Niranjan | 2026-10-27 |

If a topic says "— unclaimed —", it's free to take. If someone else's name is already there, pick a different topic or message them before jumping in. With three people and only four unclaimed topics, claim one at a time rather than reserving several in advance.

## Rule 2 — Push small and often, not in one big batch

Push after each finished question or audit pass, not at the end of a multi-hour session. This keeps the window where a conflict *could* happen as short as possible, and lets the other person actually see live progress (the point of doing this in the first place).

## Rule 3 — `git pull` before you start, every session

Always pull at the start of a working session in every repo you'll touch, even if you claimed the topic yourself last time — the other person may have touched a shared file.

```bash
git pull
```

## Rule 4 — Shared files: pull-edit-push quickly, don't sit on them

`HANDOFF.md`, each vault's `00_INDEX.md`, and `manifest.json` get touched regardless of topic. The Answer Bank's `manifest.json` and `00_INDEX.md` are covered by the stricter **Rule 7** below. Keep edits to these **small and immediate** — append your status line, commit, push, don't leave them modified locally for hours. If you do hit a merge conflict on one of these (rare, and low-stakes — they're append-mostly logs), resolve it by keeping both sides' lines; don't discard either person's entry.

## Rule 5 — `Vault` repo is a passive backup only

Nobody edits `Vault` directly — it's a known-stale snapshot kept on purpose (see HANDOFF.md 2026-10-14 entry). The canonical source for study notes is `dental-study-material/markdown`. If it's ever worth refreshing, that's a deliberate one-off sync, not part of day-to-day topic work.

## Rule 6 — One topic, one person, at a time

Don't split a single topic's audit across multiple people's sessions simultaneously — the per-question `.md` files are small enough that two agents touching the same file produces a real merge conflict, unlike the topic-folder split which avoids it structurally. If a topic is large, do it serially (one person finishes and pushes, then hands off) rather than in parallel.

## Rule 7 — Publishing to the Answer Bank / vault index is ADDITIVE ONLY (nobody's changes may disappear)

A publish to the Answer Bank artifact overwrites every path it lists, and `manifest.json` and `00_INDEX.md` are shared by everyone. Whoever publishes last wins unless you follow this rule. The artifact is owned by another organisation and several people have write access, so it has no safety net of its own.

**Never:**
- regenerate `manifest.json` or `00_INDEX.md` from a local folder, a vault copy or the OneDrive folder;
- publish an answer file from a copy that is older than the live one (check with `git pull` first and use the repo copy, not a vault/OneDrive copy);
- remove or shorten an existing manifest entry or file. If something genuinely has to be removed, say so in `HANDOFF.md` first and get the owner's agreement.

**Always — use `publish_guard.py` (stdlib only, no network, never deletes anything):**
1. `git pull` in this repo.
2. Read the *live* `manifest.json`, `00_INDEX.md` and the file listing from the artifact into a scratch folder `LIVE/` (the file listing is the text the Artifact "list files" action prints; save it as `LIVE/files.txt`).
3. Copy only the files you are adding or changing into `STAGE/<Subject>/<Topic>/`.
4. `python3 publish_guard.py merge LIVE/manifest.json LIVE/00_INDEX.md STAGE OUT/` — keeps every live entry and adds or updates only yours.
5. `python3 publish_guard.py stale LIVE/files.txt STAGE` — warns if a staged file is more than 25% smaller than the live copy (likely a stale overwrite). Fix and re-run before publishing.
6. Publish `STAGE/*` plus `OUT/manifest.json` and `OUT/00_INDEX.md` (leave `index.html` alone unless the page itself is being changed).
7. Re-list the live files, save the listing as `AFTER/files.txt` and the live manifest as `AFTER/manifest.json`, then run `python3 publish_guard.py verify LIVE/manifest.json AFTER/manifest.json LIVE/files.txt AFTER/files.txt`. It must print `VERIFY OK`. If it prints `VERIFY FAILED`, re-publish the missing entries immediately (the merged `OUT/` files contain them) and record it in `HANDOFF.md`.

**Same principle in git:** when a rebase or merge conflicts on `HANDOFF.md`, `WORKFLOW.md`, a vault `00_INDEX.md` or this file, keep both sides' lines — never resolve by discarding someone else's entry (this restates Rule 4 for the artifact).

**If the guard script itself is unavailable** (for example on a phone): do steps 2 and 7 by hand — read the live manifest before publishing, and after publishing confirm the number of manifest entries is not lower than before and that your own entries and everyone else's still appear. When in doubt, don't publish `manifest.json` at all; add your file and tell the other collaborators to add the manifest line.

## Quick checklist for starting a session

1. `git pull` in whichever repo(s) you'll touch.
2. Check the claim table above — claim your topic if unclaimed, push that change.
3. Do the work, pushing after each finished question/pass.
4. Update `HANDOFF.md`'s status line and the claim table when the topic is done.
5. Before publishing to the Answer Bank, follow Rule 7 (merge, stale-check, publish, verify). A Q-entry that disappears from the manifest is a bug in the process, not an accident.
