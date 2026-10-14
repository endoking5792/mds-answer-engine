#!/usr/bin/env python3
"""Additive-only helper for publishing to the Answer Bank artifact.

Why: a publish overwrites every path it lists, and `manifest.json` / `00_INDEX.md`
are shared files. Regenerating them from a local folder silently drops other
people's entries. This script makes the safe path the easy one. It never talks to
the network and never deletes anything; it only prepares files and checks them.

Typical session (see WORKFLOW.md, Rule 7):
  1. Read the live manifest + index + file listing from the artifact into a folder LIVE/.
  2. Put ONLY the answer files you are adding/changing into STAGE/<Subject>/<Topic>/*.md
     (copy them from the repo after `git pull`, never from an older vault copy).
  3. python3 publish_guard.py merge  LIVE/manifest.json LIVE/00_INDEX.md STAGE OUT/
       -> writes OUT/manifest.json and OUT/00_INDEX.md (live entries kept, yours added/updated)
  4. python3 publish_guard.py stale  LIVE/files.txt STAGE
       -> warns if a staged file is much smaller than the live copy (possible stale overwrite)
  5. Publish STAGE files + OUT/manifest.json + OUT/00_INDEX.md.
  6. Re-list the live files, save as AFTER/files.txt, re-read the live manifest as AFTER/manifest.json, then
     python3 publish_guard.py verify LIVE/manifest.json AFTER/manifest.json LIVE/files.txt AFTER/files.txt
       -> exits non-zero if anything that existed before is missing now.

`files.txt` is the text printed by the Artifact "list files" action (lines like:
  - "path/to/file.md"  text/markdown  1234 bytes).
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

LISTING_RE = re.compile(r'^\s*-\s*"(.+?)"\s+\S+\s+(\d+)\s+bytes', re.M)


def read_listing(path):
    return {p: int(n) for p, n in LISTING_RE.findall(Path(path).read_text())}


def scan_stage(stage):
    """Yield manifest entries for every .md under STAGE/<Subject>/<Topic>/..."""
    stage = Path(stage)
    for f in sorted(stage.rglob("*.md")):
        rel = f.relative_to(stage).as_posix()
        parts = rel.split("/")
        if len(parts) < 3 or parts[0].startswith("00_INDEX"):
            continue
        text = f.read_text()
        h = re.search(r"^#\s+(.+)$", text, re.M)
        m = re.search(r"\*\*Marks:\s*([^\n*]+)", text)
        yield {
            "subject": parts[0],
            "topic": parts[1],
            "title": h.group(1).strip() if h else f.stem,
            "marks": m.group(1).strip() if m else "",
            "path": rel,
        }


def merge_manifest(live, staged):
    out = list(live)
    by_path = {e["path"]: i for i, e in enumerate(out)}
    added, updated = [], []
    for e in staged:
        if e["path"] in by_path:
            out[by_path[e["path"]]].update({"title": e["title"], "marks": e["marks"]})
            updated.append(e["path"])
        else:
            # keep topic grouping: insert after the last entry of the same topic, else append
            idx = max((i for i, x in enumerate(out)
                       if x["subject"] == e["subject"] and x["topic"] == e["topic"]), default=None)
            if idx is None:
                out.append(e)
            else:
                out.insert(idx + 1, e)
            by_path = {x["path"]: i for i, x in enumerate(out)}
            added.append(e["path"])
    return out, added, updated


def merge_index(index_text, staged_new):
    """Additive: add one line per NEW entry under its '### Topic' heading (creating headings if needed)."""
    lines = index_text.split("\n")
    for e in staged_new:
        link = "- [%s](%s)" % (e["title"], quote(e["path"]))
        if any(quote(e["path"]) in l for l in lines):
            continue
        subj_h, topic_h = "## " + e["subject"], "### " + e["topic"]
        si = next((i for i, l in enumerate(lines) if l.strip() == subj_h), None)
        if si is None:
            lines += ["", subj_h, topic_h, link]
            continue
        end = next((i for i in range(si + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        ti = next((i for i in range(si + 1, end) if lines[i].strip() == topic_h), None)
        if ti is None:
            lines[end:end] = [topic_h, link, ""]
            continue
        tend = next((i for i in range(ti + 1, end) if lines[i].startswith("### ")), end)
        last = max(i for i in range(ti, tend) if lines[i].startswith("- ["))
        lines.insert(last + 1, link)
    return "\n".join(lines)


def cmd_merge(a):
    live_manifest, live_index, stage, out = a
    live = json.loads(Path(live_manifest).read_text())
    staged = list(scan_stage(stage))
    merged, added, updated = merge_manifest(live, staged)
    assert {e["path"] for e in live} <= {e["path"] for e in merged}, "internal error: entries lost"
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "manifest.json").write_text(json.dumps(merged, ensure_ascii=True, indent=1))
    new_entries = [e for e in staged if e["path"] in added]
    (out / "00_INDEX.md").write_text(merge_index(Path(live_index).read_text(), new_entries))
    print("live entries: %d | merged: %d | added: %d | updated: %d" % (len(live), len(merged), len(added), len(updated)))
    for p in added:
        print("  + " + p)
    for p in updated:
        print("  ~ " + p)


def cmd_stale(a):
    live_files, stage = a
    live = read_listing(live_files)
    bad = 0
    for f in sorted(Path(stage).rglob("*.md")):
        rel = f.relative_to(stage).as_posix()
        if rel in live and f.stat().st_size < 0.75 * live[rel]:
            bad += 1
            print("WARNING stale? %s is %d bytes locally vs %d live (>25%% smaller)" % (rel, f.stat().st_size, live[rel]))
    print("no staged file is much smaller than its live copy" if not bad else "%d warning(s): pull/rebuild before publishing" % bad)
    return 1 if bad else 0


def cmd_verify(a):
    before_m, after_m, before_f, after_f = a
    bm = {e["path"]: e for e in json.loads(Path(before_m).read_text())}
    am = {e["path"]: e for e in json.loads(Path(after_m).read_text())}
    bf, af = read_listing(before_f), read_listing(after_f)
    problems = []
    problems += ["manifest entry lost: " + p for p in bm if p not in am]
    problems += ["file lost: " + p for p in bf if p not in af]
    problems += ["manifest entry lost its title: " + p for p in bm if p in am and not am[p].get("title")]
    if problems:
        print("VERIFY FAILED:")
        print("\n".join("  " + p for p in problems))
        return 1
    print("VERIFY OK: %d manifest entries (was %d), %d files (was %d); nothing lost."
          % (len(am), len(bm), len(af), len(bf)))
    return 0


def main():
    cmds = {"merge": (cmd_merge, 4), "stale": (cmd_stale, 2), "verify": (cmd_verify, 4)}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds or len(sys.argv) - 2 != cmds[sys.argv[1]][1]:
        print(__doc__)
        return 2
    return cmds[sys.argv[1]][0](sys.argv[2:]) or 0


if __name__ == "__main__":
    sys.exit(main())
