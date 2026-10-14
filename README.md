# MDS Answer Engine

Working repo for the MDS (Master of Dental Surgery) exam-answer generation project — the "engine" behind each topic's answer set, independent of the final deliverables (Obsidian vault copies, OneDrive `.docx` files), which stay local/OneDrive-synced and are **not** tracked here.

## What's in here

- **`HANDOFF.md`** — the standing status/handoff file. Read this first in any new session (local or cloud) before touching a topic. It tracks what's done, what's in progress, and lessons learned per topic.
- **`skill/dental-study-material-SKILL.md`** — a **mirrored copy** of the governing skill that drives this whole project (study-material compilation rules + Section 7, the MDS University Theory Answer Generator rules: citation format, confidence/evidence tags, marks-based word ceilings, the standing publish step, etc.).
  - **Canonical/live copy** (on this Mac): `~/.claude/skills/dental-study-material/SKILL.md`. That's the one Claude Code actually loads when the `dental-study-material` skill is invoked locally.
  - This repo copy exists so a Claude Code **cloud** session (which doesn't have access to `~/.claude/skills/` on this Mac) can still read the exact same governing rules.
  - **Keep these two in sync.** Whenever the live skill file changes, re-copy it into this repo (`cp ~/.claude/skills/dental-study-material/SKILL.md skill/dental-study-material-SKILL.md`) and commit. If you're working from a cloud session and need to *change* the skill itself, edit the copy here, then copy it back to `~/.claude/skills/dental-study-material/SKILL.md` on this Mac afterward.
- **Per-topic folders** (`amalgam/`, `calcium_silicate/`, `impression/`, `irrigants/`, `medicaments/`, `post_core/`, ...) — the finished per-question Markdown answers for each topic, one file per question.
- **Tooling** (`md2docx.py`, `assemble.py`, `dossier.py`, etc.) — scripts that convert this project's Markdown answer dialect into the final `.docx` deliverables.
- **`gic_dossier/`** and other dossier/registry files — source-tracking notes from earlier topic builds (e.g. GIC).

## What's deliberately excluded

- Final `.docx` builds, flowchart images, and `.bak` files (`.gitignore`) — binary/build artifacts, not source content, and they bloat git history on every rebuild.
- The Obsidian vault (`Question Paper Bank/...`) and OneDrive `MDS III/Answers/` — these are the published destinations for finished answers, kept wherever the user's own vault/OneDrive sync already lives, not duplicated into git.

## Workflow

1. A topic gets built or audited locally (per `HANDOFF.md` and the skill's Section 7 rules).
2. Finished/patched `.md` files land here, in the topic's folder.
3. `HANDOFF.md` gets updated with the new status.
4. This repo gets committed and pushed — normally automatically once a topic's work is finished, so GitHub always reflects current state.
5. Separately (outside this repo), finished `.md` files are copied to the Obsidian vault, the topic `.docx` is rebuilt, and the pinned Answer Bank artifact is republished, per the skill's standing publish step.

## Using this from Claude Code cloud / another device

This repo is the self-contained "brain" of the project — tools, working answers, and the governing skill copy — so a Claude Code cloud session (or any session on another machine) can `git clone` it and continue the same work: draft/patch a topic's `.md` files, update `HANDOFF.md`, run `md2docx.py` to preview a docx, and push back. The Obsidian-vault/OneDrive publish step still needs to happen from a session that has access to those local paths (i.e. back on this Mac), since those aren't part of this repo.
