import os, re, json

ROOT = "/Users/niranjan/Documents/Obsidian Vault/Question Paper Bank/All Answers (Consolidated)"
entries = []
for dirpath, dirs, files in os.walk(ROOT):
    for fn in sorted(files):
        if not fn.endswith(".md") or fn.startswith("00_"):
            continue
        full = os.path.join(dirpath, fn)
        rel = os.path.relpath(full, ROOT)
        parts = rel.split(os.sep)
        if len(parts) < 3:
            continue
        subject, topic = parts[0], parts[1]
        with open(full, encoding="utf-8", errors="ignore") as f:
            text = f.read()
        title_m = re.search(r'^#\s+(.*)$', text, re.MULTILINE)
        marks_m = re.search(r'\*\*Marks:\*\*\s*([0-9]+)', text)
        title = title_m.group(1).strip() if title_m else fn
        marks = marks_m.group(1) if marks_m else None
        entries.append({
            "subject": subject,
            "topic": topic,
            "title": title,
            "marks": marks,
            "path": rel.replace(os.sep, "/"),
        })

entries.sort(key=lambda e: (e["subject"], e["topic"], e["path"]))

with open(os.path.join(ROOT, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2)

# index
by_subj = {}
for e in entries:
    by_subj.setdefault(e["subject"], {}).setdefault(e["topic"], []).append(e)

lines = ["# Answer Bank Index\n"]
for subject in sorted(by_subj):
    lines.append(f"## {subject}\n")
    for topic in sorted(by_subj[subject]):
        lines.append(f"### {topic}\n")
        for e in by_subj[subject][topic]:
            mk = f" ({e['marks']}m)" if e["marks"] else ""
            lines.append(f"- [{e['title']}{mk}]({e['path']})")
        lines.append("")
with open(os.path.join(ROOT, "00_INDEX.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("total entries:", len(entries))
print("subjects:", list(by_subj.keys()))
