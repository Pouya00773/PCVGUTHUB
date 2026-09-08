# 10 — Offene Fragen und Entscheidungsbedarf

Sortiert nach Dringlichkeit. Die ersten fünf blockieren Phase 0 und damit die Einhaltung der Frist zum **30.12.2026**.

---

## A — Blockierend für Phase 0 (bis Ende September zu klären)

### A1. Wer ist Zollanmelder je Bezugsquelle?
**Warum es blockiert:** Es entscheidet, ob ihr für ein Lot Primärbetreiber (volle DDS-Pflicht, Geodaten) oder erster Downstream-Betreiber (nur Referenznummer) seid. Falsch beantwortet, beschafft ihr Daten, die ihr nicht braucht — oder ihr steht ohne DDS da.
**Wer klärt:** Zollabteilung/Zolldienstleister + Recht, je Lieferbeziehung, nicht pauschal.
**Ergebnis:** Liste aller Bezugsquellen mit Rollenzuordnung. → `01`, Abschn. 2.3

### A2. Löst Rösten ein erneutes Inverkehrbringen aus?
**Warum es blockiert:** Bestimmt, ob ihr für Ware aus Importeursbezug nach der Röstung eine **eigene** DDS braucht oder nur die Referenznummer weitergebt. Die Quellenlage ist widersprüchlich (`01`, 2.4).
**Wer klärt:** Rechtsgutachten, idealerweise abgestimmt mit dem Deutschen Kaffeeverband/ECF, um eine Branchenposition statt einer Einzelmeinung zu haben.
**Bis dahin:** Datenmodell deckt beide Auslegungen ab — das ist billig und macht die Klärung nicht zeitkritisch für die IT, aber sehr wohl für den Prozess.

### A3. Welche Herkünfte sind bereits kartiert?
**Warum es blockiert:** Es ist die größte Kostenposition **und** der kritische Pfad (`07`, 0.6; `08`, Abschn. 1).
**Konkret abzufragen:** je Kooperative — liegen Polygone vor? in welchem Format? über Fairtrace, den Zertifizierer, den Exporteur oder gar nicht? Wer besitzt die Daten und darf sie weitergeben?
**Wer klärt:** Einkauf, direkt bei Kooperativen und Exporteuren.

### A4. Geben eure Importeure die DDS-Referenznummern zu — vertraglich, mit Frist?
**Warum es blockiert:** Ohne Nummer dürft ihr die Ware nicht weitergeben. Eine mündliche Zusage reicht nicht, wenn im Dezember die Nummer fehlt.
**Zu vereinbaren:** Zusicherung, Übermittlungsfrist (Vorschlag: mit dem Lieferavis, spätestens bei Wareneingang), Haftung bei Nichtlieferung, Format der Übermittlung.
**Wer klärt:** Einkauf + Recht.

### A5. Seid ihr nach EU-Definition mittleres/großes Unternehmen — bestätigt?
**Warum es blockiert:** Es entscheidet zwischen Frist **30.12.2026** und **30.06.2027**. Die Einordnung folgt Mitarbeiterzahl **und** Umsatz/Bilanzsumme, nicht der Tonnage.
**Annahme in diesem Plan:** >50 MA und >1.000 t → mittleres oder großes Unternehmen → **30.12.2026**. **[angenommen]**
**Wer klärt:** Kaufmännische Leitung, eine Stunde Arbeit. Falls doch KMU, gewinnt ihr sechs Monate — das würde die gesamte Roadmap entspannen und sollte deshalb zuerst geprüft werden.

---

## B — Blockierend für Phase 1 (bis Q4 2026)

### B1. Segregation oder Silo-Vermischung im Grünkaffeelager?
Die folgenreichste **nicht-IT-Entscheidung** des gesamten Vorhabens. Bei Vermischung mehrerer Partien ist die Chargenzuordnung eine Rechenfiktion, und die Hypothese H1 (`07`) ist gar nicht mehr sinnvoll testbar. Segregation kostet Lagerplatz und Handling.
**Wer entscheidet:** Produktions- und Lagerleitung, mit bewusster Kenntnis der Konsequenz. → `05`, Abschn. 6

### B2. Welches ERP, und wie offen ist es?
Der Plan geht von vorhandener Warenwirtschaft aus, kennt aber Produkt und Schnittstellenfähigkeit nicht. Zu klären: REST-API oder nur Dateiexport? Chargenverwaltung vorhanden? Freifelder für DDS-Referenznummer? Interne ETL-Kompetenz? → bestimmt die Konnektorkosten in `08`.

### B3. Wie werden Röstchargen heute erfasst?
Wenn Röstprofile in Artisan liegen und die Mengen in Excel, ist die strukturierte Chargenerfassung selbst der Engpass — nicht die Verankerung. Dann ist die Einführung einer Röstsoftware mit Chargen- und Kontraktverwaltung (Cropster oder gleichwertig) der erste Schritt von Phase 1, nicht ein Nebenaspekt. → `04`, Abschn. 3

### B4. Sind die Röster mit Gaszählern ausgestattet?
Ohne separate Zähler je Maschine gibt es keinen chargengenauen Scope 1, sondern nur Monatsdurchschnitte. Das ist zulässig, muss aber so kommuniziert werden. → `06`, Abschn. 2

### B5. Fragt heute ein B2B-Kunde nach mehr als der Referenznummer?
**Die kommerziell wichtigste offene Frage des Plans.** Sie entscheidet über Umfang von Phase 1 und über die Existenzberechtigung von Phase 2 (Hypothese H4, `07`).
**Konkret:** Mit den fünf größten B2B-Kunden sprechen. Nicht fragen „fändet ihr das interessant?" — sondern „würdet ihr es vertraglich verlangen und dafür zahlen?".

---

## C — Rechtlich und methodisch zu klären

### C1. Sind Parzellen-Geodaten personenbezogene Daten — und mit welcher Rechtsgrundlage verarbeitet ihr sie?
Der Plan geht von der vorsichtigen Auslegung aus (ja) und leitet daraus die Drei-Zonen-Regel ab (`03`, 4.2). Zu bestätigen: Rechtsgrundlage Art. 6 Abs. 1 lit. c für den EUDR-Teil, und **welche** Grundlage für die freiwillige DPP-Nutzung — Einwilligung ist bei Kleinbauern über Sprach-, Macht- und Distanzgefälle praktisch kaum sauber einzuholen.

### C2. Hält die Crypto-Shredding-Konstruktion einer aufsichtsbehördlichen Prüfung stand?
Nur relevant, wenn Phase 2 kommt — dann aber zwingend **vor** der ersten Verankerung. Die Konstruktion (Hash + löschbares Salt) ist etabliert, aber nicht höchstrichterlich bestätigt. → `03`, 4.3

### C3. Seid ihr CSRD-berichtspflichtig, und was fragen berichtspflichtige Kunden ab?
Nach den Omnibus-Anhebungen der Schwellenwerte vermutlich nicht selbst pflichtig **[angenommen]**, aber über die Wertschöpfungskette von Kunden zur Auskunft gedrängt. Relevanz für den Plan: nur die Frage, ob die CO₂-Daten VSME-kompatibel exportierbar sein müssen. → `01`, Abschn. 5

### C4. Welche werblichen Aussagen wollt ihr treffen — und halten sie?
Betrifft CO₂-Angaben (`06`, Abschn. 5), Herkunftsangaben bei Blends (`03`, Abschn. 6) und die Formulierung des Evidence Gradings (`09`, A.4). **Vor** der ersten DPP-Veröffentlichung rechtlich prüfen, nicht danach.

### C5. Fällt ihr unter das Lieferkettensorgfaltspflichtengesetz / künftige CSDDD-Umsetzung?
Datenseitig überlappt es erheblich mit der EUDR-Lieferantenerfassung. Wenn ja, sollte die Lieferantenstammdatenerhebung in Phase 0 gleich beide Zwecke bedienen — nachträgliches Nacherheben ist teuer.

---

## D — Entscheidungen, die die Geschäftsführung treffen muss

| # | Entscheidung | Wann | Konsequenz |
|---|---|---|---|
| D1 | Freigabe Budget und Verantwortlicher für Phase 0 | **sofort** | Ohne benannte Person passiert nichts. |
| D2 | Rückfallstrategie: Welche Herkünfte werden auf Importeursbezug umgestellt, wenn Geodaten bis KW 43 fehlen? | **bis KW 41** | Kostet Marge und Direct-Trade-Beziehung, erhält aber die Verkaufsfähigkeit. Diese Entscheidung im Voraus zu treffen ist deutlich billiger, als sie im Dezember treffen zu müssen. |
| D3 | Segregation im Lager (B1) | bis Q4 2026 | Bestimmt die Aussagekraft des gesamten Systems |
| D4 | Freigabe Phase 1 nach Abschluss von Meilenstein 0.3 | Q4 2026 | Erst dann ist die Kostenspanne in `08` halbierbar |
| D5 | Grundsatzbeschluss: Phase 2 startet nur bei Auslösekriterium | jetzt festhalten | Verhindert, dass die Verankerung aus Eigendynamik zur gesetzten Anforderung wird |
| D6 | Budget für Datenbeschaffung upstream als **Vergütung**, nicht als Erwartung | Q4 2026 | Der wirksamste einzelne Hebel gegen das wahrscheinlichste Scheiterszenario (`09`, B.4) |

---

## E — Was dieser Plan bewusst nicht beantwortet

- **Konkrete Anbieterempfehlung.** Der Markt hat sich 2025/26 stark bewegt; eine Empfehlung ohne Angebotsvergleich und ohne Kenntnis eurer Herkunftsländer wäre geraten. `04`, Abschn. 3 nennt die Kandidaten und die Auswahlkriterien — die Auswahl selbst gehört in Meilenstein 0.4.
- **Detaillierte Schnittstellenspezifikation.** Setzt B2 (ERP-Produkt) voraus.
- **Genaue CO₂-Zahlen für eure Herkünfte.** Ohne Kenntnis von Land, Anbausystem und Aufbereitung wäre jede Zahl Scheingenauigkeit — genau das, was `06` vermeiden will.
- **Rechtsberatung.** Dieser Plan ist Architekturgrundlage. Die Fragen A1, A2, C1, C2 und C4 gehören zu Anwälten.
