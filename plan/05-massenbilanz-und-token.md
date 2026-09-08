# 05 — Massenbilanz, Transformationsrezepturen und die Token-Frage

---

## 1. Vorbemerkung: Das ist Buchhaltung, keine Blockchain

Der Referenzfall beschreibt tokenisierte Massenbilanz: Input-Token werden bei Transformation nicht verbrannt, sondern mit Grund-Code gesperrt; Output-Token werden neu geprägt; eine Rezeptur-Tabelle verknüpft beide; erzwungen wird

```
Σ Token_Input  ≥  Σ Token_Output  +  Σ Token_Verlust
```

**Die Ungleichung ist richtig und wird übernommen. Der Token ist entbehrlich.** Dieselbe Bedingung lässt sich als Datenbank-Constraint erzwingen, mit denselben Garantien innerhalb eures Systems und ohne Schlüsselverwaltung, Gasgebühren oder Rechtsfragen. Ein Token wäre erst dann überlegen, wenn **mehrere Organisationen** dieselbe Bilanz führen und einander nicht vertrauen — bei euch führt die Bilanz genau eine Organisation.

**Was aus dem Referenzfall bleibt:**

- **Sperren statt Löschen.** Verbrauchte Inputs werden nie gelöscht, sondern mit Grund-Code auf `locked` gesetzt. Der Bestand bleibt rekonstruierbar.
- **Rezeptur-Tabelle** als eigene Entität, die Input- und Output-Chargen n:m verknüpft.
- **Erzwungene Ungleichung** als harte Prüfung bei jedem Transformationsereignis.

**Was wegfällt:** ERC-1155, On-Chain-Mint, Consumer-Ownership. Begründung in `04`, Abschn. 5.

---

## 2. Die Grundgleichung, kaffeespezifisch

Für jedes Transformationsereignis *T*:

```
Σ m_input  =  Σ m_output  +  m_prozessverlust  +  m_ausschuss  +  m_probe  +  ε
```

mit

- `m_prozessverlust` — systematischer, physikalisch erklärbarer Masseverlust (Wasser, Silberhäutchen, Feinstaub)
- `m_ausschuss` — verworfene Ware (Fehlröstung), mit Grund-Code
- `m_probe` — Musterröstung, Cupping, Qualitätsrückstellmuster
- `ε` — Messtoleranz, **explizit begrenzt** (Vorschlag: |ε| ≤ 0,5 % der Einwaage). Überschreitung = Alarm, keine automatische Verbuchung.

**Die entscheidende Designregel:** `m_output` und `m_input` werden **gewogen**, nicht gerechnet. Der Verlust ist die **Restgröße**, nicht der Eingabewert. Das dreht den Manipulationsvektor um — dazu Abschn. 4.

---

## 3. Rezepturen je Prozess

### 3.1 Rösten — 1:1 mit Masseverlust

| | |
|---|---|
| **Input** | 1 Grünkaffeepartie (`GreenLot`), Einwaage `m_grün` |
| **Output** | 1 Röstcharge (`RoastBatch`), Auswaage `m_röst` |
| **Verlustfaktor** | `v = 1 − m_röst / m_grün` |
| **Typischer Bereich** | **15–20 %** (Wasser, Silberhäutchen) **[recherchiert, Branchenwissen; im Auftrag korrekt genannt]**. Hell geröstet eher 13–16 %, dunkel 18–22 %. **[geschätzt]** |
| **Zusätzliche Attribute** | Röstprofil-ID, Ausgangsfeuchte des Grünkaffees, Chargengröße, Röstdauer, Endtemperatur |

**Wichtig:** Der Verlust ist **keine Konstante**, sondern eine Funktion von Röstgrad, Ausgangsfeuchte und Chargengröße. Ein einziger unternehmensweiter Verlustfaktor ist fachlich falsch und lädt zur Manipulation ein.

### 3.2 Blenden — n:1

| | |
|---|---|
| **Input** | n Röstchargen mit Ist-Massen `m_1 … m_n` |
| **Output** | 1 Blendcharge, Auswaage `m_blend` |
| **Verlust** | gering, typ. **0,2–1 %** (Handling, Restmengen im Mischer) **[geschätzt]** |
| **Rezeptur-Tabelle** | je Blendcharge eine Zeile pro Bestandteil: `blend_id, roast_batch_id, m_ist, anteil_ist = m_ist / Σm_ist, anteil_soll` |

**Die kaffeespezifische Komplikation:** Anteile werden chargenweise nachjustiert (Ernteschwankung, Verfügbarkeit, Cupping-Ergebnis). Deshalb:

- **`anteil_ist` ist die Wahrheit** und wird geführt. `anteil_soll` ist die Rezeptur und dient nur der Abweichungskontrolle.
- Ein **Toleranzband je Bestandteil** (z. B. Soll 60 % ± 5 pp) macht Nachjustierung zulässig und Ausreißer sichtbar.
- **Die DPP-Anzeige speist sich aus `anteil_ist` der konkreten Charge**, nie aus der Rezeptur. Regeln zur irreführungsfreien Darstellung in `03`, Abschn. 6.

**Sonderfall Pre-Blend (Rösten mehrerer Herkünfte gemeinsam):** Dann ist das Rösten selbst n:1, und die Herkunftsauflösung endet vor der Röstung statt danach. Beide Varianten müssen im Modell erlaubt sein — Post-Blend erhält mehr Information und ist rückverfolgbarkeitsseitig überlegen; das ist ein Argument für die Produktion, kein Zwang.

### 3.3 Mahlen — 1:1

Verlust typ. **0,1–0,5 %** (Mühlenrückstand, Feinstaub) **[geschätzt]**. Kritisch ist die **Mühlenspülung** beim Sortenwechsel: Die ersten Gramm nach dem Wechsel enthalten Reste der Vorcharge. → Als `m_ausschuss` mit Grund-Code `purge` buchen, nicht stillschweigend der neuen Charge zuschlagen.

### 3.4 Abpacken — 1:n (Aggregation)

Aus einer Blend- oder Röstcharge entstehen k Verpackungseinheiten. `Σ Füllgewichte + m_ausschuss + m_rest = m_input`. Der **Restbestand** (`m_rest`) geht als eigene, weiterhin herkunftsgebundene Teilmenge zurück ins Lager — er verschwindet nicht.

---

## 4. Der Verlustfaktor als Manipulationsvektor — und wie er belegt wird

**Das Problem, klar benannt:** Wer den Röstverlust hoch deklariert, kann Grünkaffee unbekannter Herkunft in die Bilanz einschleusen, ohne dass die Ungleichung verletzt wird. Bei 1.000 t/Jahr entspricht eine Verschiebung des deklarierten Verlusts um 2 Prozentpunkte rund **20 t Grünkaffee**, die „verschwinden" dürfen. Das ist keine theoretische Lücke.

**Die Antwort ist nicht Kryptografie, sondern Messung.** Fünf Ebenen, gestaffelt:

**Ebene 1 — Der Verlust wird nie deklariert, sondern gemessen.**
Ein- und Auswaage jeder Charge kommen aus der Waage, nicht aus einem Eingabefeld. `v` ist berechnete Restgröße. Ein manuell eingetragener Verlustfaktor ist im System **nicht vorgesehen**.

**Ebene 2 — Profilspezifischer Korridor statt Einzelwert.**
Je Röstprofil wird aus historischen Chargen ein Erwartungsbereich kalibriert (Median ± robuste Streuung, z. B. MAD-basiert). Neue Chargen werden dagegen geprüft. Ein Profil braucht eine Mindestzahl von Chargen (Vorschlag: 20), bevor es als kalibriert gilt.

**Ebene 3 — Automatische Ausreißerkennung mit Pflicht zur Begründung.**
Liegt `v` außerhalb des Korridors, ist die Charge nicht blockiert, aber **begründungspflichtig**: freier Text plus Grund-Code (z. B. `hohe Ausgangsfeuchte`, `Abbruch`, `Waagenfehler`). Die Begründung wird Teil der Chargenhistorie und ist im Audit sichtbar. Nicht begründete Ausreißer erscheinen im Monatsbericht.

**Ebene 4 — Statistische Kontrolle über die Zeit, nicht je Charge.**
Ein einzelner hoher Verlust ist Rauschen. Ein **Trend** ist das Signal. Kontrollkarte je Profil und je Röster-Schicht; monatlicher Abgleich der aggregierten Jahresausbeute gegen die Vorjahresverteilung.

**Ebene 5 — Der unabhängige Anker: Grünkaffee-Zugang vs. Röstkaffee-Abgang.**
Über einen Abrechnungszeitraum muss gelten:

```
Grünkaffee-Einkauf (Rechnungen, Zoll)  −  Bestandsveränderung  ≈  Σ Einwaagen aller Röstchargen
```

Diese Prüfung nutzt **Belege außerhalb der Produktion** (Einkaufsrechnungen, Zollanmeldungen, Inventur). Wer den Verlustfaktor manipulieren will, müsste zusätzlich Einkaufsbelege fälschen — und dann ist es kein Datenqualitätsproblem mehr, sondern Urkundenfälschung.

> **Ehrliches Fazit:** Diese fünf Ebenen reduzieren den Angriff auf „die Waage manipulieren **und** die Einkaufsbuchhaltung fälschen". Sie beseitigen ihn nicht. **Kein technisches System kann das** — auch das des Referenzfalls nicht, denn auch dort geht die Waagenmessung ungeprüft ins System. Wer etwas anderes behauptet, verwechselt Unveränderlichkeit mit Richtigkeit. Bewertung in `09`.

**Eine Ebene, die wirklich hilft und oft vergessen wird:** geeichte Waagen mit Kalibrierprotokoll, angebunden über die Schnittstelle statt per Abtippen. Das ist billiger als jede Kryptografie und schließt die häufigste Fehlerquelle — den Tippfehler.

---

## 5. Sonderfälle, vollständig

| Fall | Behandlung |
|---|---|
| **Fehlröstung / Ausschuss** | Eigene Buchung mit Grund-Code, Masse bleibt in der Bilanz. Verkauf als B-Ware nur mit eigener Chargen-ID und ohne Herkunftsauslobung. |
| **Musterröstung / Cupping** | Kleinstmengen (100–500 g), eigener Grund-Code `sample`. Wichtig, weil sie sonst als Verlust erscheinen und den Korridor verzerren. Vom Verlustkorridor **ausgeschlossen**. |
| **Retouren (B2B/B2C)** | Rückbuchung auf die **ursprüngliche** Chargen-ID, Status `returned`. Kein Wiedereinlagern in verkaufsfähigen Bestand ohne Qualitätsfreigabe. Bei Vernichtung: Grund-Code `destroyed`. |
| **Restbestände im Silo** | Herkunftsgebunden als Teilmenge geführt. **FIFO-Disziplin ist Voraussetzung** — ohne sie ist die Zuordnung Fiktion und muss als solche gekennzeichnet werden. Bei Vermischung mehrerer Partien derselben Herkunft: neue Misch-Partie mit dokumentierten Anteilen. |
| **Grünkaffee-Aufbereitung im Haus** (Verlesen, Sieben) | Eigene 1:1-Transformation mit Verlust, vor dem Rösten. Sonst erscheint der Verlesungsverlust fälschlich als Röstverlust. |
| **Entkoffeinierung (extern)** | Lohnverarbeitung: Transformation außer Haus, mit Ein- und Ausgangsgewicht des Dienstleisters. Verlust deutlich höher und **[angenommen]** verfahrensabhängig — eigener Korridor. |
| **Verschnitt bei Verpackungsumstellung** | `m_ausschuss` mit Grund-Code `packaging` |
| **Inventurdifferenz** | Nie stillschweigend ausbuchen. Eigener Grund-Code `inventory_adjustment`, Betragsgrenze, ab der eine Freigabe nötig ist. **Das ist das Schlupfloch, durch das in der Praxis am meisten verschwindet.** |

---

## 6. Was die Massenbilanz für EUDR leistet — und was nicht

**Leistet sie:** Sie beantwortet die Frage „welche Grünkaffeepartien stecken in dieser Tüte, und in welchem Verhältnis?" — und damit die Frage, welche DDS-Referenznummern an einen B2B-Kunden weiterzugeben sind.

**Leistet sie nicht:** Sie ersetzt **nicht** die Parzellen-Geolokation. Eine perfekte Massenbilanz über eine Grünkaffeepartie ohne Geodaten ist EUDR-seitig wertlos. Und sie ist ausdrücklich **nicht** das, was Zertifizierer unter Massenbilanz verstehen — dort dürfen zertifizierte und nicht-zertifizierte Ware gemischt werden, hier nicht. Siehe `01`, Abschn. 6.

**Konsequenz für die Praxis:** Wenn ihr Segregation (physische Trennung nach Herkunft) betreibt, ist die Bilanz einfach und aussagekräftig. Wenn ihr Silos gemeinsam nutzt, wird sie schnell zur Zuordnungsfiktion. **Die Entscheidung Segregation vs. Vermischung ist eine Produktions- und Lagerentscheidung, keine IT-Entscheidung** — und sie bestimmt, wie viel euer System überhaupt aussagen kann. Sie gehört in `10-offene-fragen.md`.
