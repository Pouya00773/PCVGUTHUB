# 02 — Stakeholder- und Prozesslandkarte

**Kernaussage dieses Dokuments:** Der Engpass des gesamten Vorhabens liegt bei zwei Akteuren, die weder eure Software benutzen noch euren Vertrag unterschreiben — der Kooperative und dem Exporteur. Jede Architekturentscheidung, die vor der Klärung ihrer Anreize getroffen wird, ist Spekulation.

---

## 1. Die Kette, ehrlich gezeichnet

```
Kleinbauer  →  Kooperative / Washing Station  →  Exporteur  →  [Importeur/Grünkaffeehändler]  →  RÖSTEREI  →  B2B-Kunde / B2C-Endkunde
   (Parzelle)        (Erntecharge, Aufbereitung)   (Exportlot)      (nur bei Zukauf)              (Röstcharge, Blend, VE)
```

Zwei Pfade, die euch unterschiedlich betreffen:

- **Pfad A — Direct Trade / Eigenimport:** Der Importeur entfällt oder ist reiner Dienstleister. Ihr seid Primärbetreiber, ihr braucht die Parzellendaten. **Hier liegt eure Arbeit.**
- **Pfad B — Zukauf über EU-Importeur:** Der Importeur ist Primärbetreiber. Ihr braucht von ihm nur die DDS-Referenznummer. **Hier liegt euer Vertragsrisiko, nicht euer Datenaufwand.**

**Die zentrale Realität:** Die Rösterei kauft fast nie am Feld. Selbst im Direct Trade steht in aller Regel eine Kooperative oder ein Exporteur dazwischen — und der erfasst die Geodaten, nicht ihr. **[angenommen, branchenüblich]**

---

## 2. Akteure im Einzelnen

### Kleinbauer / Erzeuger

| | |
|---|---|
| **Liefert an das System** | Parzellengrenzen, Erntemenge, Erntezeitpunkt, Legalitätsnachweise (Landtitel o. Ä.) |
| **Anreiz** | Marktzugang. Ohne EUDR-Daten kein Verkauf nach Europa — das ist der Anreiz, und es ist ein Zwang, kein Angebot. Preisaufschläge für Rückverfolgbarkeit sind selten und selten dauerhaft. |
| **Widerstand** | Kein Smartphone, keine Datenkompetenz, teils keine formalen Landtitel; berechtigte Sorge vor Datenweitergabe an Behörden oder Steuerverwaltung; Misstrauen gegen GPS-Erfassung durch Fremde |
| **Realistische Erfassung** | **Nicht durch ihn selbst.** Erfassung durch die Kooperative oder einen Feld-Enumerator mit GPS-Gerät/Smartphone. |
| **Vertrauensanker** | Schwach. Der Erzeuger signiert nichts, was kryptografisch prüfbar wäre. Wer behauptet, DIDs für Kleinbauern lösten das, hat nicht mit Kleinbauern gearbeitet. |

### Kooperative / Washing Station

| | |
|---|---|
| **Liefert** | Aggregation Parzelle→Erntecharge, Polygonerfassung, Mitgliederregister, Aufbereitungsart (gewaschen/natural/honey) |
| **Anreiz** | Existenziell: EUDR-Fähigkeit entscheidet über Absatzfähigkeit der gesamten Mitgliederernte. |
| **Widerstand** | Kosten und Personal für die Kartierung; parallele Datenanforderungen von fünf verschiedenen Käufern in fünf verschiedenen Formaten (der Hauptärger im Feld); Angst, dass Daten an Wettbewerber abfließen und die Kooperative als Zwischenhändler übersprungen wird |
| **Realistische Erfassung** | **Hier passiert es.** Mobile Erfassung durch Kooperativenpersonal. |
| **Vertrauensanker** | **Der praktisch stärkste verfügbare Anker.** Institution mit Bestandsinteresse, oft zertifiziert und damit bereits auditiert. Die Kooperative kann sinnvoll eine DID halten und Erfassungen signieren. |

> **Kostensenker:** Für Fairtrade-Lieferketten ist die Kartierung seit Juni 2026 über *Fairtrace* kostenlos verfügbar, mit Direktweitergabe an Importeure ab Oktober 2026 **[recherchiert]** ([Daily Coffee News](https://dailycoffeenews.com/2026/06/16/fairtrade-launches-free-eudr-geolocation-tool-for-coffee-cooperatives/)). Vor jeder kommerziellen Kartierungsbeauftragung prüfen, ob die Kooperative hier schon erfasst ist.

### Exporteur / Trockenmühle

| | |
|---|---|
| **Liefert** | Exportlot-Bildung, Sackzählung, Qualitätsanalyse, Phytosanitär- und Ursprungszeugnisse, ICO-Marks, Containerdaten |
| **Anreiz** | Hoch — er verliert sonst den EU-Absatz. Große Exporteure haben 2025/26 bereits investiert. |
| **Widerstand** | Die **Vermischungsstelle**: In der Trockenmühle laufen Chargen mehrerer Kooperativen zusammen. Rückverfolgbarkeit bis zur Parzelle bedeutet für ihn separate Verarbeitungsläufe und damit echte Zusatzkosten. Hier bricht die Kette in der Praxis am häufigsten. |
| **Vertrauensanker** | Mittel bis gut. Kommerzielles Interesse, aber auch das stärkste Motiv zur Aggregation über die Wahrheit hinweg. |

### Importeur / Grünkaffeehändler (nur Pfad B)

| | |
|---|---|
| **Liefert** | **Die DDS-Referenznummer.** Mehr braucht ihr rechtlich nicht. |
| **Anreiz** | Er ist Primärbetreiber und trägt das Compliance-Risiko selbst. |
| **Widerstand** | Schutz seiner Bezugsquellen. Er wird euch die Referenznummer geben und die Parzellendaten dahinter **nicht**. Das ist legitim und regulatorisch ausreichend. |
| **Euer Risiko** | Vertraglich, nicht technisch: Wenn die Nummer nicht rechtzeitig kommt, dürft ihr die Ware nicht weitergeben. → `10-offene-fragen.md` |

### Rösterei (ihr)

| | |
|---|---|
| **Liefert** | Röstchargen, Blendrezepturen, Verlustdaten, Verpackungseinheiten, Scope-1/2-Energiedaten |
| **Anreiz** | Compliance-Pflicht + Differenzierung im B2B + Rückruffähigkeit |
| **Widerstand — intern, und ernst zu nehmen** | Die Röstermannschaft. Jede zusätzliche Erfassungsminute je Charge wird umgangen, sobald der Betrieb hektisch wird. **Das ist das häufigste Scheiterkriterium solcher Projekte, nicht die Technik.** Erfassung muss aus ohnehin stattfindenden Handlungen fallen (Waage, Röstsoftware-Log), nicht zusätzlich sein. |
| **Vertrauensanker** | **Stark.** Eigene Geräte, eigene Waagen, eigene Zähler. Hier ist „Verified" im Sinne des Evidence Gradings tatsächlich erreichbar. |

### B2B-Kunde (Gastronomie, Handel, Büro)

| | |
|---|---|
| **Erwartet** | Bei Handelsketten: EUDR-Referenznummer, zunehmend CO₂-Angaben für die eigene Scope-3-Bilanz |
| **Anreiz** | Eigene Compliance. **Das ist der einzige Akteur, der für Verifizierbarkeit tatsächlich zahlen könnte.** |
| **Prüffrage** | Fordert heute ein konkreter Kunde mehr als die Referenznummer? Wenn nein, ist Phase 2 nicht begründbar. → `07`, `10` |

### B2C-Endkunde

| | |
|---|---|
| **Erwartet** | Ehrlich: fast nichts. Scanraten von Herkunfts-QR-Codes liegen typischerweise im niedrigen einstelligen Prozentbereich. **[geschätzt, branchenübliche Größenordnung]** |
| **Anreiz** | Neugier, Vertrauen, Story |
| **Realistische Bewertung** | Der Consumer-Layer ist **Marketing**, kein Compliance-Nutzen. Das ist nicht ehrenrührig — es muss nur so budgetiert und so gemessen werden. Wer den QR-Code mit Compliance begründet, verschiebt Marketingkosten in ein Pflichtbudget. |

---

## 3. Wo die Kette real bricht

Vier Bruchstellen, nach absteigender Wahrscheinlichkeit:

1. **Trockenmühle/Exporteur-Aggregation** — mehrere Kooperativen in einem Verarbeitungslauf. Ab hier ist Parzellenzuordnung nur noch statistisch, nicht physisch. → Vertraglich getrennte Verarbeitungsläufe verlangen oder Genauigkeitsverlust dokumentieren statt kaschieren.
2. **Kooperativen-Sammelstelle** — Kleinbauern liefern in gemeinsame Behälter. Parzellenauflösung nur, wenn beim Wiegen erfasst wird.
3. **Euer Blend** — n Herkünfte in einer SKU, chargenweise nachjustiert. Technisch beherrschbar (`05`), kommunikativ heikel (`03`, Abschnitt DPP).
4. **Euer Grünkaffee-Silo/Lager** — Restbestände aus mehreren Partien derselben Herkunft. Ohne FIFO-Disziplin ist die Zuordnung fiktiv.

> Der wichtigste Satz zu allen vieren: **Ein Ledger repariert keine dieser Bruchstellen.** Er macht sie nur unveränderlich dokumentiert. Siehe `09-risiken.md`.

---

## 4. Prozesse, die tatsächlich neu gebaut werden müssen

| Prozess | Auslöser | Verantwortlich | Phase |
|---|---|---|---|
| Lieferanten-Onboarding EUDR | neue Bezugsquelle | Einkauf | **0** |
| Geodatenbeschaffung + Qualitätsprüfung | vor Kontraktabschluss | Einkauf + Qualität | **0** |
| Entwaldungs-Risikoprüfung (Polygon gegen Waldverlustdaten) | je Lot | Qualität/Compliance | **0** |
| DDS-Erstellung und -Einreichung TRACES | vor Inverkehrbringen | Compliance | **0** |
| Referenznummern-Register (Eingang + Weitergabe) | je Wareneingang / je Verkauf | Warenwirtschaft | **0** |
| Chargenverknüpfung Grünkaffee → Röstung → Blend → VE | je Produktion | Produktion | 1 |
| Energiedatenerfassung je Röstcharge | je Röstung | Produktion/Technik | 1 |
| Rückruf-/Trace-Abfrage | Anlassfall | Qualität | 1 |
| DPP-Veröffentlichung | je SKU-Charge | Marketing/IT | 1 |

**Alles in Phase 0 ist Pflicht und terminkritisch. Alles in Phase 1 ist freiwillig und darf Phase 0 nicht verzögern.**

---

## 5. Was das für die Anbieterauswahl heißt

Weil der Engpass upstream liegt, ist das entscheidende Auswahlkriterium für Phase-0-Software **nicht** die Eleganz der Plattform, sondern:

1. Kann sie Geodaten in den Formaten aufnehmen, die eure Exporteure und Kooperativen **tatsächlich schon liefern**?
2. Reicht sie DDS direkt in TRACES ein?
3. Führt sie ein sauberes Referenznummern-Register für Pfad B?
4. Kommt man ohne Lock-in wieder heraus (Datenexport)?

Alles Weitere ist Phase 1. Bewertung in `04-architektur-optionen.md`.
