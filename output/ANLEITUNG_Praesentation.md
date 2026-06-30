# Anleitung: Vortrag Weichenantriebe – Siemens Mobility Interview

## Dateien

| Datei | Beschreibung |
|---|---|
| `Vortrag_Weichenantriebe.pptx` | 2-Folien-Präsentation (Siemens-Design, Calibri, Petrol #009999) |
| `../input/marktdaten_weichenantriebe.xlsx` | Rohdaten für Power BI (3 Sheets) |

---

## Schritt-für-Schritt: Power BI Charts einbauen

### 1. Excel in Power BI Desktop öffnen
- Power BI Desktop starten → „Daten abrufen" → Excel
- Datei: `input/marktdaten_weichenantriebe.xlsx`
- Alle 3 Sheets laden

### 2. Chart für Folie 1 – Bubble Chart (Technologietrends)
- Sheet: **Technologische Trends**
- Visualisierung: **Punktediagramm (Scatter Chart)**
  - X-Achse: `Reifegrad (1–5)`
  - Y-Achse: `Relevanz Siemens (1–5)`
  - Größe der Blasen: `Marktpotenzial (Mrd. EUR)`
  - Legende/Details: `Trend`
- Farbe: Siemens Petrol (#009999) für alle Punkte
- Datenbeschriftungen einschalten (Trend-Name je Blase)
- Hintergrund: Weiß, kein Rahmen

### 3. Chart für Folie 2 – Balkendiagramm (Wettbewerber)
- Sheet: **Wettbewerb – Umsatz nach Region**
- Visualisierung: **Gruppiertes Balkendiagramm**
  - Achse (X): `Region`
  - Werte (Y): `Umsatz Signaling (Mrd. EUR)`
  - Legende: `Unternehmen`
- Siemens Mobility in Petrol (#009999) hervorheben
- Titel: „Umsatz Signaling-Segment nach Region (Mrd. EUR, Schätzung 2024)"

### 4. Charts exportieren
- Je Chart: `...` (Drei-Punkte-Menü) → **Als Bild exportieren** → PNG, 300 DPI
- Alternativ: Screenshot mit Snipping Tool bei maximiertem Chart-Bereich

### 5. Charts in PowerPoint einfügen
- `Vortrag_Weichenantriebe.pptx` öffnen
- Folie 1: Grauer Platzhalter links → löschen → PNG einfügen → Größe anpassen
- Folie 2: Gleich vorgehen
- Chart sollte ca. 6,1" × 4,7" groß sein (linke Hälfte der Folie)

---

## Folie-Design (Siemens Corporate Design)

| Element | Wert |
|---|---|
| Schrift | Calibri (Alternativ: Siemens Sans von fonts.siemens.com) |
| Primärfarbe | Petrol `#009999` |
| Sekundärfarbe | Dunkelblau `#00305E` |
| Hintergrund | Weiß `#FFFFFF` |
| Grau (Akzent) | `#A8A8A8` |

---

## Vortrag-Timing (Ziel: max. 7 Minuten)

| Abschnitt | Zeit |
|---|---|
| Einleitung: Marktkontext (1 Satz) | 30 Sek. |
| Folie 1: 5 Trends erklären | 2,5 Min. |
| Folie 2: Wettbewerber-Matrix | 2,5 Min. |
| Eigene Schlussfolgerung / Implikation für Siemens | 1 Min. |
| Übergabe ans Gespräch | 30 Sek. |

---

## Quellenangaben (bereits im Footer der Folien)

**Folie 1:**
- Siemens Mobility Geschäftsbericht 2024
- Europe's Rail JU Technology Roadmap 2025
- Bundesministerium für Digitales und Verkehr (Deutschlandtakt)
- Eigene Schätzung

**Folie 2:**
- Siemens Mobility GB 2024
- Alstom Annual Report 2024
- Hitachi Rail Annual Report 2024
- Mordor Intelligence Rail Signaling Market Summary 2024
- Eigene Schätzung
