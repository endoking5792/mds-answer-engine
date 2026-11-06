# Second-reader audit, group sn (Q07, Q08, Q09), 2026-11-05

Method: every locator in the three answers was opened in its chapter with surrounding text (helper printing 200 to 900 characters around each phrase), checked for author, number, qualifier and context. Author lines checked on the first page of every chapter used; offsets checked at two pages for each Harty's chapter. `python3 locators.py sn_` prints `checked 190 missing 0`; all three files rebuilt inside 320-400 words.

## Author lines and offsets

| Chapter | Finding | Evidence | Action |
|---|---|---|---|
| Walton and Torabinejad 3rd ed (2002) Ch.29 Differential diagnosis of orofacial pain | Chapter author is **Graham Rex Holland**, not the editors | 00_Front_matter.md contents page (PDF p.8): "29 / Differential Diagnosis of Orofacial Pain, 520 / Graham Rex Holland" | fixed: F citation now "Holland, 2002"; new BOOK sn_Holland2002; all Q07 text and exam core changed |
| Same book Ch.4 Diagnosis and treatment planning | Contents page for Ch.1 to 13 is missing from the extracted file; author cannot be confirmed | front matter jumps from PDF p.7 to Ch.14 entries | kept "Walton and Torabinejad, 2002" (editors); BOOK note says why |
| Ingle's 7th Ch.8 | Letter-substituted author line "P$/0 V. A11(&&" decodes to Paul V. Abbott using the same cipher as the title line ("The Practice of Endodontics") | Ch.8 PDF p.191 | kept; BOOK note updated |
| Ingle's 7th Ch.13 | "L%'( K. B")*"+," decodes to Leif K. Bakland (same cipher as "C!"#$%&" = Chapter) | Ch.13 PDF p.349 | kept; BOOK note updated |
| Torabinejad 6th ed Ch.4, Ch.5; Seltzer and Bender 2nd ed | Editors verified in front matter (Torabinejad, Fouad, Shabahang, 2021; Hargreaves, Goodis, Tay, 2012) | front matter | "editor names not verified" notes removed |
| Harty's Ch.2 | Escudier, offset 16 | PDF 28 = p.12, PDF 29 = p.13 | added (F sn_har2) |
| Harty's Ch.3 | Chandler and Chong, offset 16 confirmed | PDF 44 = p.28, PDF 53 = p.37 | kept |
| Harty's Ch.5 | Duncan, Smith and Cooper, offset 16 | PDF 81 = p.65, PDF 97 = p.81 | added (sn_har5) |
| Harty's Ch.13 | Rotstein, offset 16 | PDF 279 = p.263, PDF 289 = p.273 | added (sn_har13) |
| Harty's Ch.14 | Hülsmann and Chong, offset 16 | PDF 303 = p.287, PDF 304 = p.288 | added (sn_har14) |

## Q07 Differential diagnosis of pain from and around the teeth

75 cited sentences/locators checked; 6 corrected; the rest held up (Law et al, Berman and Rotstein, Eli et al, Okeson, Gutmann and Lovdahl all faithful).

| # | Location | Finding | Evidence | Action |
|---|---|---|---|---|
| 1 | Throughout (8 places incl. exam core intro and psychogenic row) | Ch.29 claims attributed to "Walton and Torabinejad, 2002" are Holland's | contents page, above | fixed to (Holland, 2002) |
| 2 | S2 periodontal | "probing separates them" not what the locator says; Gutmann separates periodontal abscess by normal pulp sensibility and no periapical bone loss | Gutmann Ch.1 PDF p.20 "Usually periodontal abscesses can be distinguished by normal pulp sensibility tests" | fixed, new locator sn_g1_perioabs |
| 3 | S3 myofascial frequency | 3/4 MFP, 1/4 neuropathic is from a small subset of root-canal-treated patients, not all endodontic patients | Law et al PDF p.538 "in this small number of patients" | qualifier added |
| 4 | S3 cardiac | Holland "most commonly left mandible" vs Okeson's cited data left 45%, right 41% | Okeson PDF p.829 | added side by side |
| 5 | S3 sinus anaesthesia conflict | Real difference in wording only: Okeson intranasal 4% lidocaine diagnostic and intraoral block only partial; Eli et al topical anaesthesia "to the offending area" eliminates pain. Not a true contradiction | Okeson PDF p.813-814; Eli PDF p.94 | kept, header softened to "books word the anaesthetic test differently"; [Likely] reconciliation kept |
| 6 | S3 psychogenic conflict | Confirmed: Law et al "rare" (PDF p.537), Holland "common" (PDF p.549), Eli et al "not established" (PDF p.93). Okeson calls it somatoform with the same features | as cited | kept; Escudier added (below); [Likely] line revised |
| 7 | S3 neuropathic, Eli "do not often awaken" | Eli's sentence is about paroxysmal neuralgias generally, which include TN | Eli PDF p.93 | kept (faithful) |
| 8 | S4 conclusion (exam core) | "Never treat a tooth until pain is reproduced in it" over-states Gutmann, who says rule out dental cause and refer | Gutmann Ch.6 PDF p.130 | reworded |
| 9 | Common mistakes | "current books class it as neuropathic" over-generalised: Escudier 2017 still labels atypical facial pain psychogenic | Harty's Ch.2 PDF p.28 | reworded |

## Q08 Test cavity

43 cited sentences checked; 4 corrected; Cohen's, Grossman's, Gutmann, Gulabivala, W&T Ch.4, Torabinejad 6th Ch.4, Abbott all faithful.

| # | Location | Finding | Evidence | Action |
|---|---|---|---|---|
| 1 | S2 coolant conflict | Confirmed real: dry (Weine "airotor without water spray", Sikri "without coolant") vs water (Cohen's "air and water coolant", Grossman's "water coolant", Harty's "copious irrigation"). But Weine allows water spray through a restoration and warns against more heat once a response is felt | Weine PDF p.201-202 | qualifier added; exam core step 5 names Harty's and "Weine (in dentin)" |
| 2 | S4 Weine vs Abbott | Confirmed real ("unquestionably the most accurate" PDF p.200; "barbaric" PDF p.234). But Weine himself says "only as a last resort" | Weine PDF p.201 | added; exam core line updated |
| 3 | S4 | "as do Baumann and Beer" implied they call it subjective; they say "last diagnostic method of choice" | Endodontology PDF p.51 | fixed |
| 4 | S1 indications (exam core) | "radiolucency beside a crowned or splinted tooth" misstates Weine's two examples (radiolucency at a PJC incisor; acute mandibular swelling among splinted teeth) | Weine PDF p.201 | fixed, locator sn_w_splintswell |
| 5 | S4 Abbott false responses | Mechanism (apprehension makes patients report pain with necrotic pulps) added for accuracy | Ingle's Ch.8 PDF p.233 | added |
| 6 | S1 Baumann and Beer calcified pulps | Locator is a figure caption (Fig. 4.8) but read faithfully | Endodontology PDF p.52 | kept; flagged |

## Q09 Tooth Slooth

43 cited sentences checked plus the coordinator-added Abbott and Leow sentence; 4 corrected.

| # | Location | Finding | Evidence | Action |
|---|---|---|---|---|
| 1 | S4 Abbott and Leow sentence (d1_i_leow) | Numbers right (68% pressure, 8% release) but omitted 15% both and 9% no biting pain; exam core and high-yield said "Abbott found ... 68% of cracked teeth", over-generalising (population is cracked teeth with reversible pulpitis) and attributing the study to the chapter author | Ingle's Ch.8 PDF p.232 | fixed in explanation, exam note, high-yield, mistakes; Abbott's conclusion (not specific as a test on its own) added |
| 2 | S5 Krishnan and Swain | "against micro-CT none of these is highly accurate" applied to history and methylene blue; the cited study tested transillumination, DIAGNOcam, microscope, macrophotography only | Guidebook Ch.9 PDF p.261 | fixed |
| 3 | S2 release-pain mechanism | Fluid-movement explanation is Kahler et al, cited by Bakland | Ingle's Ch.13 PDF p.355 | attribution clarified |
| 4 | S4 table (exam core) | "Dull periodontal ache" embellishes Gulabivala's "periodontal sensation rather than a dentinal sensation" | Gulabivala PDF p.108 | fixed |
| 5 | S1 FracFinder maker | Cohen's: HuFriedy; Harty's and Bakland: Denbur, Oak Brook | Cohen's PDF p.229; Harty's PDF p.46; Ingle's Ch.13 PDF p.355 | conflict added; maker dropped from exam core |
| 6 | S4 release conflict | Confirmed and widened: release side Grossman's, Sikri, Witherspoon and Regan, Baumann and Beer, Cohen's Ch.1; either phase Berman and Tamse, Gulabivala and Ng; data against Abbott and Leow | as cited | added Gulabivala, Witherspoon, Baumann |
| 7 | S3 | Abbott: test opposing-arch cusps too (referred pain) | Ingle's Ch.8 PDF p.232 | added |

## Harty's additions (Task B)

| Answer | Harty's chapter | Agreement / disagreement | Action |
|---|---|---|---|
| Q07 | Ch.2 Escudier 2017 | Agrees dental pulpal pain is the commonest orofacial pain; sinus: whole-quadrant tenderness, rarely without a preceding cold (agrees Gutmann); records PDAP | added (explanation) |
| Q07 | Ch.2 Escudier 2017 | Lists atypical (persistent) facial pain as **psychogenic**, does not usually disturb sleep: sides with Holland against Law et al and Eli et al | added to the psychogenic conflict |
| Q07 | Ch.3 Chandler and Chong 2017 | Reversible pulpitis sharp pain up to 5 to 10 s; irreversible pulpitis may worsen lying down or bending over (so "worse on bending" is not specific to sinus pain) | added |
| Q07 | Ch.3 Chandler and Chong 2017 vs Holland 2002 | **Disagree on selective anaesthesia sequence:** Holland infiltrates maxillary teeth from the anterior teeth; Chandler and Chong use intraligamental injections from the most posterior tooth forward, and say it localises arch or quadrant better than a tooth | added side by side (explanation) |
| Q07 | Ch.13 Rotstein 2017 | Primary endodontic lesion draining via the sulcus mimics a periodontal abscess; narrow tract on probing; primary periodontal lesion has normal pulp sensitivity | added |
| Q07 | Ch.14 Hülsmann and Chong 2017 | Woken at night / prolonged pain = irreversible; nonendodontic emergency pain list including food packing | added (explanation; Hülsmann and Chong also cited in the exam-core table) |
| Q08 | Ch.3 Chandler and Chong 2017 | Re-verified: copious irrigation, A-delta false positive, tertiary dentine false negative all faithful. New: framed as "historically" suggested; CO2 snow particularly useful for full-coverage restorations (agrees Grossman's) | added |
| Q09 | Ch.3 Chandler and Chong 2017 | Re-verified indication and segment separation. Harty's says nothing about release pain | kept; FracFinder maker conflict added |
| Q09 | Ch.5 Duncan, Smith and Cooper 2017 | Pressure-phase mechanism: biting wedges the crack, fluid movement, pain in an inflamed pulp; contrasts with Kahler's release mechanism | added (explanation) |
| Q09 | Ch.14 Hülsmann and Chong 2017 | Only one cracked-tooth line (Krell and Rivera survey on necrosis); nothing on bite tests | not used |

## Open points for Niranjan
1. Walton and Torabinejad 3rd ed Ch.4 author could not be confirmed (contents page for Ch.1 to 13 missing in the extracted file); a printed copy would settle whether it should be cited by chapter author.
2. Abbott and Bakland author decodes are internally consistent but come from cipher-garbled text; worth one glance at the printed Ingle's 7th.
3. Any other answer in the repo citing "Walton and Torabinejad, 2002" for Ch.29 (Differential diagnosis of orofacial pain) should be changed to Holland, 2002. In diagnosis/ only Q07 used it.
4. Selective anaesthesia sequence (anterior-first vs posterior-first) now appears in Q07's explanation; the D1/D2 answers may want the same side-by-side.
