# 08 — Kostenschätzung

**Alle Zahlen sind [geschätzt]**, sofern nicht anders gekennzeichnet. Sie sind Bandbreiten für eine Investitionsentscheidung, keine Angebote. Marktpreise für EUDR-Software haben sich 2025/26 stark bewegt; vor Vertragsschluss drei Angebote einholen.

**Bezugsgröße:** >1.000 t Grünkaffee/Jahr, >50 Mitarbeitende, Mischform-Beschaffung, angenommen 8–15 Herkünfte/Jahr **[angenommen]**.

---

## 1. Die wichtigste Aussage zuerst: die Treiber

| Treiber | Wirkung auf die Gesamtkosten | Von euch beeinflussbar? |
|---|---|---|
| **Anzahl nicht kartierter Direct-Trade-Herkünfte** | **Größter Einzeltreiber.** Jede unkartierte Kooperative kostet vierstellig bis niedrig fünfstellig. | Teilweise — durch Bezugsentscheidung |
| **Anteil Pfad B (Importeursbezug)** | Senkt Kosten drastisch. Referenznummer verwalten kostet fast nichts. | Ja — Beschaffungsstrategie |
| **Zahl der Herkünfte gesamt** | Linear auf Beschaffung und Pflege | Ja |
| **Segregation vs. Silo-Vermischung** | Bestimmt, ob Chargenzuordnung real oder fiktiv ist | Ja — Lagerentscheidung |
| **Struktur der Röstchargen-Erfassung heute** | Ohne Röstsoftware ist die Datenerfassung Handarbeit | Ja |
| **Ledger-Transaktionskosten** | **Vernachlässigbar** — siehe Abschn. 5 | irrelevant |

> **Merksatz:** Die Software ist nicht das Teure. Die Daten sind das Teure, und die liegen in Äthiopien, Kolumbien und Honduras.

---

## 2. Phase 0 — EUDR-Compliance (Pflicht)

### Einmalig

| Position | Bandbreite | Bemerkung |
|---|---|---|
| Rechtsberatung Rollenklärung + Gutachten Rösten/Inverkehrbringen | 8.000 – 20.000 € | Zwei Fragen, beide entscheidungsrelevant |
| Auswahl, Einführung, Konfiguration EUDR-SaaS | 10.000 – 35.000 € | inkl. Datenmigration Lieferantenstammdaten |
| **Geodatenbeschaffung Direct-Trade-Herkünfte** | **5.000 – 60.000 €** | **größte Unsicherheit.** 0 € wenn Fairtrace/Exporteur bereits kartiert hat; 3.000–8.000 € je Kooperative bei Beauftragung eines Kartierungsdienstleisters |
| Vertragsanpassungen mit Importeuren (Referenznummern-Zusicherung) | 3.000 – 8.000 € | |
| ERP-Anbindung (Chargen, Referenznummern) | 8.000 – 25.000 € | abhängig von der ERP-Offenheit |
| Schulung, Prozessdokumentation | 5.000 – 12.000 € | |
| **Summe Phase 0 einmalig** | **≈ 40.000 – 160.000 €** | |

### Laufend p. a.

| Position | Bandbreite |
|---|---|
| EUDR-SaaS-Lizenz | 12.000 – 40.000 € |
| Geodatenpflege, neue Herkünfte, Nachkartierung | 5.000 – 25.000 € |
| Interner Aufwand Compliance (≈0,3–0,5 VZÄ) | 20.000 – 40.000 € |
| **Summe laufend** | **≈ 37.000 – 105.000 €** |

**Diese Kosten fallen an, unabhängig davon, ob ihr Phase 1 oder 2 macht.** Sie sind der Preis der Marktzugehörigkeit.

---

## 3. Phase 1 — Datenqualität, DPP, CO₂ (freiwillig)

### Einmalig

| Position | Option A (nur zugekauft) | Option B (Hybrid, **Empfehlung**) | Option C (Referenzfall-Klon) |
|---|---|---|---|
| Röstsoftware mit Chargenverwaltung (z. B. Cropster) | 10.000 – 25.000 € | 10.000 – 25.000 € | 10.000 – 25.000 € |
| Event Store + Konnektoren + Evidence Grading | — | 40.000 – 90.000 € | im Plattformpreis |
| DPP-Renderer, QR, B2B-API | — | 20.000 – 45.000 € | im Plattformpreis |
| Plattformlizenz/Implementierung DLT-Traceability | — | — | 120.000 – 400.000 € |
| DID/VC-Infrastruktur + Partner-Onboarding | — | — | 40.000 – 120.000 € |
| Gaszähler/Unterzähler Nachrüstung + Anbindung | 6.000 – 20.000 € | 6.000 – 20.000 € | 6.000 – 20.000 € |
| CO₂-Faktorbibliothek, Methodik, ggf. externe Prüfung | 8.000 – 25.000 € | 8.000 – 25.000 € | 8.000 – 25.000 € |
| Physische Marker (M-Trust o. ä.) | — | — | 30.000 – 100.000 €+ |
| **Summe einmalig** | **≈ 25.000 – 70.000 €** | **≈ 85.000 – 205.000 €** | **≈ 215.000 – 690.000 €** |

### Laufend p. a.

| Position | A | B | C |
|---|---|---|---|
| Lizenzen | 8.000 – 20.000 € | 10.000 – 25.000 € | 40.000 – 120.000 € |
| Hosting/Betrieb Eigenbau | — | 3.000 – 9.000 € | im Preis |
| Wartung/Weiterentwicklung (0,2–0,5 VZÄ) | 5.000 – 15.000 € | 20.000 – 50.000 € | 25.000 – 60.000 € |
| CO₂-Datenpflege | 5.000 – 15.000 € | 5.000 – 15.000 € | 5.000 – 15.000 € |
| Marker-Verifikation, Handgeräte | — | — | 10.000 – 30.000 € |
| **Summe laufend** | **≈ 18.000 – 50.000 €** | **≈ 38.000 – 99.000 €** | **≈ 80.000 – 225.000 €** |

---

## 4. Phase 2 — Verankerung (optional, nur bei Auslösekriterium)

| Position | Bandbreite |
|---|---|
| Anbindung Verankerungssenke (falls in Phase 1 vorbereitet) | 8.000 – 25.000 € |
| Schlüsselverwaltung, HSM oder Managed KMS | 3.000 – 12.000 € einmalig, 2.000 – 6.000 €/a |
| Rechtsprüfung DSGVO-Konstruktion (`03`, 4.3) | 5.000 – 15.000 € |
| Partner-Onboarding (je externer Signatar) | 3.000 – 10.000 € je Partei |
| **Ledger-Transaktionsgebühren** | **≈ 0 – 400 €/a** — siehe unten |

---

## 5. Die Ledger-Kosten, damit sie nicht als Argument dienen

Hedera `ConsensusSubmitMessage` kostet seit Januar 2026 **0,0008 USD** je Nachricht, in USD fixiert. **[recherchiert]** ([Hedera, Preisänderung Jan. 2026](https://hedera.com/blog/price-update-to-consensussubmitmessage-in-consensus-service-january-2026/))

| Granularität | Nachrichten/Jahr **[geschätzt]** | Kosten/Jahr |
|---|---|---|
| Jedes Einzelereignis | ~500.000 | **≈ 400 USD** |
| Je Charge | ~20.000 | ≈ 16 USD |
| Je Tages-Merkle-Root | 365 | ≈ 0,30 USD |

**Damit ist geklärt:** „Blockchain ist zu teuer" ist bei diesem Volumen falsch, und „Blockchain kostet fast nichts" ist als Argument *für* sie ebenso wertlos. Die Kosten von Option C liegen zu **über 99 %** in Lizenz, Integration, Onboarding und Betrieb — nicht in den Gebühren. Wer euch Option C mit den niedrigen Transaktionskosten verkauft, argumentiert an der Kostenstruktur vorbei.

Zum Vergleich: qualifizierte eIDAS-Zeitstempel liegen bei wenigen Cent je Stempel, bei einem Tages-Root also **unter 50 €/Jahr** **[geschätzt]**; OpenTimestamps ist kostenlos.

---

## 6. Gesamtbild über 3 Jahre

| Szenario | Jahr 1 | Jahre 2–3 p. a. | **3-Jahres-Summe** |
|---|---|---|---|
| **Nur Phase 0** (Minimalvariante) | 77.000 – 265.000 € | 37.000 – 105.000 € | **≈ 151.000 – 475.000 €** |
| **Phase 0 + 1, Option B** *(Empfehlung)* | 162.000 – 470.000 € | 75.000 – 204.000 € | **≈ 312.000 – 878.000 €** |
| **Phase 0 + 1 + 2, Option C** | 292.000 – 955.000 € | 117.000 – 330.000 € | **≈ 526.000 – 1.615.000 €** |

Die Spannen sind breit, weil die Geodatenbeschaffung und der Zustand eurer Lieferketten sie dominieren. **Vor Freigabe von Phase 1 sollte Meilenstein 0.3 (`07`) abgeschlossen sein — er halbiert die Unsicherheit der größten Position.**

---

## 7. Was ihr durch Streichungen spart

| Gestrichenes Element | Ersparnis |
|---|---|
| Physische Marker (M-Trust) für Grünkaffee | 30.000 – 100.000 € einmalig + laufende Verifikation |
| ERC-1155-Token / Consumer-Ownership | 25.000 – 80.000 € + Rechtsberatung Kryptorecht |
| jBPM/BPMN-Engine, Keycloak/SSO | 30.000 – 70.000 € einmalig + Betrieb |
| Consumer-App statt QR-Webseite | 40.000 – 120.000 € + laufende Store-Pflege |
| DID/VC für einzelne Erzeuger | 40.000 – 120.000 € |
| **Summe der Streichungen** | **≈ 165.000 – 490.000 €** |

Dem steht ein Nutzenverlust gegenüber, der sich auf einen Satz bringen lässt: Ihr könnt einem Dritten die Zeitgleichheit eurer Belege nicht ohne euer Zutun beweisen, und ihr könnt eine gefälschte Endverbraucherpackung nicht physisch entlarven. Beides fragt heute niemand nach. Ändert sich das, sind Phase 2 und ein Markerkonzept nachrüstbar — Option B ist genau darauf ausgelegt (`04`, Abschn. 2).

---

## 8. Nicht bezifferte, aber reale Kosten

- **Aufmerksamkeit der Geschäftsführung** in Phase 0 — der Rollen- und Zollstatus lässt sich nicht delegieren.
- **Beziehungskosten upstream:** Wer Kooperativen unter Zeitdruck zu Datenlieferungen drängt, ohne Aufwand zu vergüten, riskiert die Lieferbeziehung. Ein Datenbeschaffungsbudget je Herkunft ist ehrlicher als Erwartungsdruck.
- **Opportunitätskosten:** Jede Woche, die in Phase-2-Architekturdiskussionen fließt, fehlt in Phase 0.
