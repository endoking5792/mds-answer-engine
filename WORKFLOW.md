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
