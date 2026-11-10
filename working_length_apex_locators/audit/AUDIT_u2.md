# AUDIT_u2: second-reader check and textbook audit of Q02 and P2 (2026-11-09)

Scope: `canonical/Q02_Electronic_Apex_Locators_25m_CANONICAL.md` and `canonical/P2_Factors_Affecting_Accuracy_of_Electronic_Apex_Locators_10m_PREDICTED_CANONICAL.md`, their sidecars, `locators_Q02.py`, new `locators_U2.py` (keys `u2_`). Method: each high-risk claim was traced to the chapter text around its locator phrase (not just the phrase), then checked against books not yet cited.

## 1. Checks done (claims opened in the chapter text, 40 items)
Q02: AAE definition; 6.5 kΩ (Gutmann, Jain) vs 6 kΩ (Baumann); impedance highest at constriction, lowest at foramen (Baumann); foramen not radiographic apex and the under-50% figure (Malkhassian); Custer 1918, Suzuki 1942, Sunada 1962 (Malkhassian); Root Canal Meter 1969 (Jain); Inoue 1969 (Weine); Sono-Explorer 1971 (Jain); Root ZX 1992 (Jain); first to sixth generation descriptions and limitations (Jain); Elements/Raypex 4 (fourth), Joypex 5 (fifth) (Jain); DenApex sixth (Sikri); Sikri six-generation list and "blue tooth" label; Gopikrishna four-generation scheme; Weine three types; third-generation frequencies (Jain, Gopikrishna, Cohen); accuracy 90 to 100% (Siqueira); "low 90 percentiles" (Weine); 84% and 96% (Malkhassian citing Kim); 90.4% vs 82.1% (Munce); 20% and 11% (Malkhassian citing Vieyra); 20% and 42% arch superimposition (Malkhassian citing Tamse); errors tend long (Weine); subtract 1 to 2 mm (Walton); withdraw 0.5 mm (Peters and Arias); zero reading (Gulabivala); size 100 K-file (Malkhassian); gutta-percha and clean file (Sikri, Roda); pacemaker positions (Malkhassian, Sikri, Munce, Cohen); Tri Auto ZX (Jain, Weine); motors with locators (Peters et al, Hülsmann and Schäfer); Gutmann primary means; Gopikrishna alone/combined; Jain 3 mm rule.
P2: Baumann false-positive and false-negative lists; Hülsmann and Schäfer 2009 false-negative list; Gopikrishna metal contact; plastic capillary tip, nail varnish, silicone stopper; Weine wet/dry canal and lip clip; Jain battery 50% and patency; Malkhassian size/file type/vital-necrotic findings; Jain small-file passage; preflaring.

## 2. Corrections made
Q02
1. Third-generation row gave "8 kHz, 400 Hz" for both Root ZX and Endex. Books split: Endex 1 and 5 kHz, subtraction (Cohen/Peters et al; Grossman); Root ZX 8 and 0.4 kHz, ratio (Cohen; Jain). Row rewritten, Peters et al added to references.
2. Accuracy: Weine's "low 90 percentiles" had been paired with the 0.5 mm figure. Weine's figure is "within 1 mm of the CDJ". Separated, and Walton's 80 to 95% (impedance locators, apical foramen) added.
3. "Sono-Explorer introduced impedance in 1971" overstated. Jain: Inoue's change-in-frequency method (1971) was introduced in the Sono-Explorer. History reworded; Weine's 1969 instrument identified as the resistance-type Sono-Explorer.
4. "Weine opposes the Tri Auto ZX" softened to criticises, because errors tend long.
5. Gutmann and Lovdahl "suggest it as the primary means" changed to "serious consideration" of locators as the primary means (their wording).
6. Tamse superimposition: now stated as zygomatic arch over first and second maxillary molars respectively.
7. Reference list reordered to first-citation order (Peters et al now cited early); uncited Tonini and Garo removed after the apical-plug bullet was cut.

P2
1. "Pulp vitality" sentence no longer cites Peters et al (reference removed).
2. File-size row restated to Jain's actual two-sided position (small files reduce reliability, but in wide canals a small file works as well).
3. "Calibrate" now carries Malkhassian's qualification (most new models need none).
4. Blueprint and headings: Verification merged into the conclusion; references reordered.

## 3. Additions (locators in `locators_U2.py`)
Q02: Sono-Explorer and Root ZX generation conflicts (Weine, Sikri, Grossman, Jain); device-specific frequencies (Cohen); endpoint wording (Weine narrowest; Baumann between constriction and foramen); Walton 80 to 95%; Weine 1 mm CDJ qualifier.
P2: canal-moisture conflict row (Walton wet or dry; Malkhassian first two generations; Jain fourth and fifth); secondary/tertiary dentine as a false-negative cause (Baumann); calibration qualification.
Cut to stay in range: Q02 CBCT bullet, apical-plug bullet, Bluetooth handpiece bullet, preflaring sentence (kept in P2), Sikri 1.0 to 1.5 mm, minor wording. P2: Pulp vitality citation, Verification heading, two table cells.

## 4. Conflicts recorded (side by side in the answers unless noted)
- Sono-Explorer: first generation (Weine; Sikri Mark I) vs second (Jain; Gopikrishna; Sikri Marks II and III).
- Root ZX: third (Jain, Weine, Sikri, Peters et al) vs fourth (Gopikrishna).
- Generation counts: four (Gopikrishna), three (Weine), six (Jain, Sikri, Ingle); fifth = capacitance/resistance (Jain) vs Bluetooth (Sikri).
- Locator accuracy: 90 to 100% (Siqueira), 80 to 95% (Walton), low 90s within 1 mm CDJ (Weine), above 90% (Harty, not cited).
- Locator endpoint: foramen vs narrowest constriction vs in between.
- Moisture: impedance units wet or dry (Walton) vs fourth needs dry, fifth struggles dry (Jain).
- Calibration: important (Jain) vs most new models need none (Malkhassian), in sidecar P2 only as a qualified remedy.
- Preflaring, pacemakers, alone vs combined, working-length offset (1 to 2 mm, 0.5 mm, zero): as before.
- Sono-Explorer / Mark IV and Torabinejad's "two impedance locators" were not used further.

## 5. Slips noted in books (not used)
- Jain lists the Root Canal Meter as first-generation "direct current" yet describes it as 150 Hz alternating current.
- Jain calls Ray-Pex 4 and 5 fourth-generation, Sikri puts Raypex 5 in the fifth.
- Sikri prints 40 mA for Suzuki/Sunada current, Malkhassian 40 μA (already in sidecar).
- Malkhassian prints accuracy "between 8% and 94%" (likely 80%).
- Hülsmann and Schäfer 2009 OCR garbles "too dry"; not located.

## 6. Standalone, headings, references
Both answers stand alone; heading sequences usable (Q02: definition, history, classification, technique, accuracy, radiographic comparison, limitations, advances, combining, conclusion; P2 matches its blueprint). No tags, locators or audit text in the student files. References are numbered in first-citation order, one format, and match in-text surnames (builder: none missing). No invented authors, years or pages. Chapter authors for Grossman 14e, Walton 3e, Endodontology Ch.19 and Problems in Endodontics are not printed, so editors are cited (stated in sidecars).

## 7. Open points
- Q02 sits exactly at 1000 words, P2 at 399; any further addition needs a matching cut.
- Not checked against Seltzer and Bender (no apex-locator hits), Weine front matter (contents only), Common Complications beyond the existing locator, or Ingle's Ch.22/28/37 to 39 (brief grep hits only); Torabinejad Ch.13 read and agrees with Walton.
- Ingle 7e chapter authors rest on the Contents page (verify against the printed book); Root ZX 1992 (Jain) vs 1994 (Munce) unresolved.
- Hülsmann and Schäfer 2009 chapter author unreadable.

## 8. Final check lines
Q02: LOC keys 116, missing 0; quotes not found 0; body 1000 words (850-1000); surnames not in references: none; body numbers without a locator: '25' (the Marks line).
P2: LOC keys 47, missing 0; quotes not found 0; body 399 words (320-400); surnames not in references: none; numbers without a locator: none.
