"""Replace the EXAM MODE section of a topic file with the text in an exam file.
Usage: python3 setexam.py TOPIC_FILE EXAM_TXT
The exam text must start with '## EXAM MODE'. The replaced span runs to the next '## HIGH-YIELD POINTS'.
Prints the new exam word count (split on whitespace) and the file's section counts."""
import re, sys
topic, exam = sys.argv[1], sys.argv[2]
t = open(topic, encoding='utf-8').read()
new = open(exam, encoding='utf-8').read().strip() + "\n\n"
assert new.startswith("## EXAM MODE"), "exam file must start with '## EXAM MODE'"
a = t.index("## EXAM MODE"); b = t.index("## HIGH-YIELD POINTS")
t = t[:a] + new + t[b:]
open(topic, 'w', encoding='utf-8').write(t)
secs = re.split(r'\n(?=## )', t)
for s in secs:
    h = s.split('\n', 1)[0]
    if h.startswith('## EXAM') or h.startswith('## STUDY'):
        print(f"{len(s.split()):6d} {h[:20]}")
