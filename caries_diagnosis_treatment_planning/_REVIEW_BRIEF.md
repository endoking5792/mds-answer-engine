# Second-reader check and textbook audit brief — caries_diagnosis_treatment_planning

You are one of three parallel auditors (SESSION_PROMPT.md section 6). First read `_AGENT_BRIEF.md` in this folder (rules, sources, offsets, checks) and SESSION_PROMPT.md section 6. Work only on the answers assigned to you: edit only those answers, their sidecars and their `locators_<QID>.py`, plus your ledger `audit/AUDIT_u<N>.md`. Do not edit any other file. Do not commit, push or publish. `export MDS_TEXTBOOKS=/home/user/mds-textbooks/`.

Settled decisions (do not change):
- Sturdevant's 2e South Asia is cited by chapter contributors: Ch.2 (Ferreira Zandoná and Ritter, 2019), Ch.3 (Boushell and Shugars, 2019).
- `Textbook_of_Conservative_and_Restorative_Dentistry.md` is Sikri VK (CBS, 2020), cited (Sikri, 2020).
- Publish under Conservative Dentistry only; question wording as in `_QUESTIONS.md`.

For each assigned answer:
1. **Second reader:** read the answer against its sidecar ledger. Every factual statement must have a locator behind it or be written as reasoning; reword to what the book says, or remove. Check numbers against the located phrase. Fix wrong attributions (fact cited to an author whose page doesn't say it).
2. **Textbook audit:** check the standing Conservative books the drafter did not use (and the relevant *Detection and Assessment of Dental Caries* chapters) for (a) facts an examiner expects that the answer lacks (classifications, criteria, values, steps), (b) conflicts between books — show side by side with names, (c) textbook slips. Add a locator for anything added. Stay inside the word range (cut lower-value material to make room; note cuts in the sidecar).
3. Check the student file is clean: stands alone, headings form a usable exam sequence, blueprint present for 10/20m, references Vancouver, numbered by first citation, every reference cited and every citation referenced, no audit/locator/[RECALL] material, no mnemonics or generic recaps. Keep reference formats for the same book identical across your answers.
4. Re-run `python3 build_audit.py audit/<sidecar>` until clean (missing 0; quotes not found 0; words in range; surnames ok; review numbers flag), and add a revision-history row to the sidecar.

Ledger `audit/AUDIT_u<N>.md`: per answer — checks done, statements reworded/removed, additions (with source), conflicts shown, slips found, open points; final build_audit line.

Report back briefly: per answer the changes, final words vs range, and open points.
