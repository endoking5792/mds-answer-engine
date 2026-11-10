# AUDIT u3 - second-reader check and textbook audit (Q03, P1, P3), 2026-11-09/10

## Checks done
- Opened the chapter text behind about 60 claims (mm values, thresholds, percentages, who-said-what, resorption/open-apex allowances, generation table, pacemaker, accuracy figures) in Q03, P1, P3; every sentence checked against its locator context, not just the phrase.
- Textbooks newly searched: Hülsmann and Schäfer (Problems in Endodontics 2009, Ch.10), Gulabivala and Ng Ch.1 (Table 1.6), Harty Ch.7 (paper point, radiographic method), Torabinejad 6e Ch.3 (Abramovitch and Fayad), Ingle 7e Ch.9 and Ch.20, Walton 2002 Part 9, Endodontic Radiology other chapters (CBCT/digital: nothing on working length beyond Ch.13/14), Common Complications Ch.5, Seltzer and Bender Ch.17 (no working length method), Weine Ch.6 (four methods, buccal object rule 25-35/20-30 degrees).
- build_audit.py clean on all three sidecars (see stamps in each sidecar; P3 "7" is the marks line only).

## Corrections
Q03: paper-point "foramen passed" -> over-extension; "Obsolete" -> Unreliable; average-values statement tied to constriction-apex distance; Root ZX 84% -> 96% was misplaced under triangulation; EAL choice "recommended, not mandatory"; accuracy figures labelled as single studies/types; pacemaker line made multi-source; "no radiation" -> book's wording; Weine "supplementary check" replaced by Harty/Hülsmann wording.
P1: "Weine's method" was Kuttler's method; "at least 1 mm" -> 1 mm; repeat thresholds reattached to what each book says; Barnett 32% reworded; parallax row relabelled; digital "instant" for phosphor removed.
P3: open-apex statement unsupported -> Jain wording; resorption "up to 2 mm" -> "2 mm or more" (Weine); apexification limit tied to calcium hydroxide protocol.
References reordered by first citation in all three.

## Additions (locators_U3.py, keys u3_)
Q03: mean tooth lengths; tactile least accurate/first constriction only; paper-point principle and "not primary"; EAL reads a point between constriction and foramen; cardiologist consult; Harty >90% within 0.5 mm held. P1: fictitious radiographic apex; CBCT first-choice/artefacts. P3: open-apex locator conflict and paper-point alternative.

## Conflicts shown
Pacemakers (Sikri contraindicated; Hülsmann consult; Munce unnecessary); EAL weighting (Gutmann primary; Walton confirm; Weine never replace); accuracy figures; terminus 0.5-1.0/1.0-1.5/1-2 mm; repeat thresholds 1/2/3 mm; open apex locators (Jain/Cohen/Attin); resorption allowances (Weine/Walton/Gutmann).

## Slips
Suzuki dog 6 kOhm (Attin) vs Sunada human 6.5 kOhm (Munce, Sikri); Custer/Cluster 1918; Hülsmann text OCR-damaged.

## Open points
Chapter authors of Hülsmann Ch.10 (probably Hör, Rödig, Hülsmann) and printed-page offset unverified, editors cited; Ingle 7e year unverified; held locators (u3_har_82, u3_har_2mm, u3_wal_3mm, u3_far_pt, u3_gut_5mm, u3_hul_arb, u3_att_6k) available if space allows. Q03 sits at 793/800 words.
