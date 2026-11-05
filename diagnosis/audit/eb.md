# Audit ledger: eb (Q14 Clinical judgment and EBDM, 50m; Q10 Endograms, 5m)

Second reader, 2026-11-05. Locators: `python3 locators.py eb_` prints `checked 153 missing 0`. Final exam cores: Q14 1966 words (1700-2000), Q10 188 words (160-200). No FAILURE DISCLOSURE.

## Q14: Will the twain of clinical judgment meet with evidence-based decision making?

About 95 cited sentences checked against the chapter text (all 92 original locators opened in context; offsets and author lines confirmed for Kvist Ch.10, Setzer et al Ch.22, Johnson et al Ch.6, White and Torabinejad Ch.13, Gulabivala and Ng Ch.5, Ørstavik Ch.11). 6 corrected, 5 [RECALL] items converted to [SRC], the rest kept.

| # | Location | Finding | Evidence | Action |
|---|---|---|---|---|
| 1 | S6 explanation, exam table, CES claim 2 | White and Torabinejad were framed as "favouring the implant for replacement after failure" against Johnson et al. Wrong: "replacement of choice" is among replacement options (implant vs FPD/RPD); the same chapter calls RCT and implants "complementary therapies, not competing treatments", gives implant survival "equal to a NSRCT tooth", and puts nonsurgical retreatment first after failure | Endodontic Prognosis Ch.13, PDF p.237, 241 | fixed: conflict reframed as the narrower surgery-versus-implant disagreement (White and Torabinejad; review cited by Setzer et al) vs Johnson, Fayad and Berman; agreement on retreat-first stated |
| 2 | S6 Setzer "lack validity" | Holds: implant ranked superior on success in one review, criteria differ so "comparisons lack validity"; survival 97%; implants do not exceed compromised treated teeth | Torabinejad 6th ed Ch.22, PDF p.463-464 | kept |
| 3 | S6 Johnson, Fayad and Berman "roughly equal" | Holds, with "in broad terms and under ideal conditions"; 94% vs 59% is a meta-analysis of microsurgery vs traditional | Cohen's Ch.11, PDF p.1382-1383 | kept |
| 4 | S6 visits | Rosenberg and Malek, Ørstavik, Ng and Gulabivala all faithful. Ng and Gulabivala's bias point reworded to its real sense (undocumented variables will bias outcomes until large documented RCTs exist) | Cohen's Ch.5 p.600; EE Ch.11 p.332-333; Cohen's Ch.17 p.2204 | fixed (wording) |
| 5 | S1 Sackett [RECALL] | Book covers it: Friedman quotes Sackett et al 1991 verbatim | Endodontic Microbiology 2nd ed Ch.15, PDF p.357 | converted to [SRC] (cited by Friedman, 2017) |
| 6 | S1 triad / ADA definition [RECALL] | AAE Glossary defines evidence-based endodontics as best research evidence + clinician expertise + patient values; Harty's Ch.1 gives the same triad | AAE Glossary 2012, PDF p.21; Harty's Ch.1 PDF p.21 | converted to [SRC]; ADA claim dropped |
| 7 | S2 evidence pyramid [RECALL] | Books cover it, in differing forms: CEBM levels 1-5 (Friedman); AAE Glossary ranking; Gutmann (RCTs at peak, personal opinion at base); White and Torabinejad (SR highest) | EM Ch.15 PDF p.358; Glossary PDF p.32; Harty's Ch.10 PDF p.196 | converted; table rebuilt on CEBM; the difference shown side by side, not ranked |
| 8 | S2 "306 articles graded" | Over-read: 306 is the number published over 40 years in a review that assigned LOE; not stated that all 306 were graded | Ch.22 PDF p.463 | fixed |
| 9 | S3 Kvist gaps "how much healing is needed" | Misread: Kvist says the time needed for healing is hard to determine and radiographic assessment is unreliable | Guidebook Ch.10 PDF p.285 | fixed |
| 10 | S3 "healing takes 1 to 4 years; drop-out high" [RECALL] | Replaced by Friedman's appraisal criteria (follow-up long enough; at least 80% examined) | EM Ch.15 PDF p.357 | converted |
| 11 | S5 focal infection "an expert opinion" | Interpretation not in text; text adds that endodontics was rescued by practitioners who recorded outcomes, until around 1940 | Cohen's Ch.17 PDF p.2140 | fixed |
| 12 | S7 decision tree [RECALL] | Machtou and Ruddle: retreatment decision can be structured as a decision tree, a rational basis that involves the patient; dentists show two tendencies, specialists behave like students | Ingle's Ch.23 PDF p.647 | partly converted; expected-utility steps stay [RECALL] |
| 13 | S7 Balevi and Shepperd | Only in White and Torabinejad's reference list (ref 24, cited for cost); wording "cited by" acceptable | Ch.13 refs | kept |
| 14 | S8 GRADE [RECALL] | GRADE certainty grades given in a table note; use of GRADE in the ESE S3 guideline not in any book | VPT Ch.3 PDF p.72 | GRADE grades [SRC]; S3-GRADE link kept [RECALL] |
| 15 | S9 PICO [RECALL] | Phillips Ch.21 lists four EBP skills: PICO question, search, critical evaluation, clinical judgment on applicability | Phillips 12th ed PDF p.549 | converted |
| 16 | S5 cognitive biases [RECALL] | Searched anchoring, availability, confirmation bias, overconfidence, cognitive bias: only irrelevant hits (anchoring proteins, sutures) | all books | kept [RECALL] |
| 17 | S4 false sensibility results [RECALL] | Cohen's Ch.1 has false-positive/negative sections; not converted (word budget) | Cohen's Ch.1 ~PDF p.223 | kept, open point |
| 18 | Kvist, Cohen's Ch.1, 5, 11, 17, Gulabivala and Ng locators | Read in context; faithful (EPT, 86/81/71%, 50% agreement, thresholds, SDM, Markov, heuristics, consensus statements, phronesis) | as listed in SOURCE LIST | kept (about 75 sentences) |

### Harty's additions (Q14)
| # | Chapter (author, year, offset) | Content | Action |
|---|---|---|---|
| H1 | Ch.1 Chong, 2017, offset 16 | EBD triad; ESE quality guidelines; practitioners must monitor outcomes against accepted criteria; implants and endodontics complementary, natural tooth ideal, implant for selected poor prognosis | added (S1, S6, S8) |
| H2 | Ch.3 Chandler and Chong, 2017, offset 16 | "Watch and review" when diagnosis unclear | added (S4 explanation) |
| H3 | Ch.8 Siqueira and Rôças, 2017, offset 16 | Visits: decision by pulp/periapical status plus operator skill, difficulty, compliance; vital teeth single visit; SRs inconclusive; one large single-operator study favours two visits with Ca(OH)2 | added as a fourth voice in Conflict 1 (leans to two visits for infected teeth, unlike Ørstavik's "becoming difficult to maintain two visits as standard"; shown side by side) |
| H4 | Ch.10 Gutmann, 2017, offset 16 | Evidence pyramid with RCTs at peak; empirical decision-making replaced by evidence-based principles; clinician experience "should not be ignored" | added (S2 conflict with White and Torabinejad on top of pyramid; S5; S9 verdict) |
| H5 | Ch.15 Mannocci and Giovarruscio, 2017, offset 16 | Survival compares favourably with implant crowns; finance a factor; post rules from laboratory or anecdotal evidence | added (S3, S6) |
| H6 | Ch.14 Hülsmann and Chong, 2017 | Read for decision-making/outcome content: only generic statements (benefits must outweigh risks) | nothing added |

## Q10: Endograms

13 cited sentences checked, 2 corrected, 1 conflict added.

| # | Location | Finding | Evidence | Action |
|---|---|---|---|---|
| 1 | Retrieval report | Re-searched all books for endogram/endograph/Endographe: still only the two reference entries; but Common Complications Ch.6 also cites the endogramme paper in text (refs 302-307, spreader design and forces in lateral compaction) | CC Ch.6 PDF p.145 | fixed (report) |
| 2 | Meaning paragraph | "[Likely]" graph of force against time and "Endographe [RECALL]" are honestly tagged; no book defines the word | all books | kept |
| 3 | Harty's Ch.9 (Chandler, 2017) | Author line confirmed (N. P. Chandler), offset 16 (PDF 167 = p.151). "These forces can be considerable" cites Blum, Machtou and Micallef 1998 (ref 72); finger spreaders recommended to reduce root fracture risk from excessive pressure, not "to reduce force" | Harty's Ch.9 PDF p.177 | fixed exam line; added apical-direction rule and Blum 1998 title |
| 4 | Force findings | Book conflict found: Pontius (citing Blum et al 1998) says warm vertical wedging is significantly lower than cold lateral; Aminoshariae et al say forces not significantly different | Endodontology Ch.30 PDF p.256; Cohen's Ch.9 PDF p.1129 | added side by side in explanation and exam core |
| 5 | Force findings | Castellucci: Blum found Thermafil forces lower than lateral, vertical and System B | Ingle's Ch.22 PDF p.638 | added (explanation) |
| 6 | Schäfer 1.5-7.2 kg | Holds, but Schäfer cites Pitts et al 1983, not Blum; wording "vertical root fracture" changed to "root fracture" | Endodontology Ch.29 PDF p.245 | fixed (minor) |
| 7 | Clauder, Plotino, Baumann ref list | Faithful | Ch.31 p.263; CC p.127, 162 | kept |

## Open points for Niranjan
1. Q10: the meaning "force-time recording during obturation" rests only on the 2001 paper title; the paper itself was not opened. If the examiner meant something else, the answer cannot support it.
2. Q10: Pontius and Aminoshariae disagree on warm vertical vs lateral wedging forces while both cite Blum's group; worth checking Blum 1998 (J Endod 24:223) directly.
3. Q14: Phillips (a dental materials book) is the only source for PICO; Vital Pulp Treatment's GRADE grades come from a table note. Accept or keep as [RECALL]?
4. Q14: levels of evidence differ by book (CEBM via Friedman: SR top, no expert opinion; Gutmann: RCT top; AAE Glossary: multiple RCTs top, expert opinion with in vitro). Answer shows all; confirm the examiner-friendly order.
5. Phillips 12th ed year (2013) and AAE Glossary edition (preface says 2012, 8th ed) not verified beyond the file text.
6. Cohen's Ch.1 false-positive/negative sensibility content could replace one [RECALL] line in S4 if the word budget is relaxed (exam core is at 1966/2000).
