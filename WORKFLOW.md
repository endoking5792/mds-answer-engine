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

If a topic says "— unclaimed —", it's free to take. If someone else's name is already there, pick a different topic or message them before jumping in. With three people and only four unclaimed topics, claim one at a time rather than reserving several in advance.

## Rule 2 — Push small and often, not in one big batch

Push after each finished question or audit pass, not at the end of a multi-hour session. This keeps the window where a conflict *could* happen as short as possible, and lets the other person actually see live progress (the point of doing this in the first place).

## Rule 3 — `git pull` before you start, every session

Always pull at the start of a working session in every repo you'll touch, even if you claimed the topic yourself last time — the other person may have touched a shared file.

```bash
git pull
```

## Rule 4 — Shared files: pull-edit-push quickly, don't sit on them

`HANDOFF.md`, each vault's `00_INDEX.md`, and `manifest.json` get touched regardless of topic. Keep edits to these **small and immediate** — append your status line, commit, push, don't leave them modified locally for hours. If you do hit a merge conflict on one of these (rare, and low-stakes — they're append-mostly logs), resolve it by keeping both sides' lines; don't discard either person's entry.

## Rule 5 — `Vault` repo is a passive backup only

Nobody edits `Vault` directly — it's a known-stale snapshot kept on purpose (see HANDOFF.md 2026-10-14 entry). The canonical source for study notes is `dental-study-material/markdown`. If it's ever worth refreshing, that's a deliberate one-off sync, not part of day-to-day topic work.

## Rule 6 — One topic, one person, at a time

Don't split a single topic's audit across multiple people's sessions simultaneously — the per-question `.md` files are small enough that two agents touching the same file produces a real merge conflict, unlike the topic-folder split which avoids it structurally. If a topic is large, do it serially (one person finishes and pushes, then hands off) rather than in parallel.

## Quick checklist for starting a session

1. `git pull` in whichever repo(s) you'll touch.
2. Check the claim table above — claim your topic if unclaimed, push that change.
3. Do the work, pushing after each finished question/pass.
4. Update `HANDOFF.md`'s status line and the claim table when the topic is done.
