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
| casting_alloys_defects | IN PROGRESS (claimed 2026-10-18): drafting from the Dental Materials (sections 2, 9) and Conservative Dentistry (section 17) repositories: casting alloys, casting defects and porosity, casting shrinkage, wax-pattern distortion; also REWRITES Ceramics CD Q18 (alloys in metal-ceramic) and Ceramics DM Q8 (base metal alloys for bonded porcelain) from the new sources; nothing published yet | Medhinir | 2026-10-18 |

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
