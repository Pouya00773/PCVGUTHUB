# Werkstudenten-Bewerbung – Wirtschaftsingenieur (mit Schweiz-Bezug)

ATS-/AI-Filter-optimierte Bewerbungsunterlagen für Werkstudenten-Stellen bei gut zahlenden
Firmen mit Schweiz-Standort. **Leitplanke:** keine erfundenen Qualifikationen – aufzubauende
Skills sind ehrlich als „(Grundkenntnisse)" markiert (Lernplan siehe `lernplan.md`).

## Inhalt
- `input/lebenslauf_original.md` – transkribierter Original-CV (persönliche Daten als Platzhalter)
- `analyse.md` – Stärken, Lücken, Skill-Einstufung (bitte bestätigen)
- `zielfirmen.md` – kuratierte Zielfirmen je Branche + ATS-Keyword-Bank
- `lernplan.md` – kostenlose Ressourcen für „in Aneignung"-Skills
- `scripts/build_docs.py` – erzeugt die DOCX-Dateien (datengetrieben)
- `scripts/docx_common.py` – gemeinsame DOCX-Formathelfer
- `output/` – fertige Word-Dateien

## Lernmaterial Automatisierungstechnik
Klausurvorbereitung „Grundlagen der Automation" (HTW Berlin, WIW, SS 2026).

Quelltexte in `lernskript/`:
- `klausurmarker.md` – die 16 belegten Klausurmarkierungen mit Wortlaut,
  einzige Wahrheitsquelle für das ★ auf den Karten
- `lernplan.md` – nach Punktdichte sortierte Lernreihenfolge
- `lernskript_at.md` – Skript, Teil 0 bis 9 plus Formelsammlung
- `karteikarten.md` – 183 Karten aus allen grün markierten Folienkästchen
- `erklaerungen.md` – die Kernthemen in Alltagssprache
- `uebungsloesungen.md` – Übungen 1–7, Minimalformen rechnerisch geprüft
- `aufgabentypen.md` – Klausur-Aufgabentypen mit Lösungsschema

Erzeugte Dateien in `output/`: `Lernplan_`, `Lernskript_`, `Karteikarten_`,
`Erklaerungen_`, `Uebungsloesungen_`, `Spickzettel_Automation.docx` sowie
`lernseite.html` (interaktive Karteikarten, läuft offline im Browser).

```bash
pip install python-docx
python3 scripts/build_lernskript.py    # Word-Dateien
python3 scripts/build_lernseite.py     # Lernseite
```

### Klausurmarkierungen

```bash
python3 scripts/finde_klausurmarker.py <ordner> [--marker]
```

Sucht die handschriftlichen Klausurhinweise — im Textlayer und optional über die
Spuren des türkisen Textmarkers. Beide Verfahren liefern nur **Kandidaten**: Die
Handschrifterkennung zerlegt das Wort regelmäßig, und türkise Flächen kommen auch
gedruckt vor. Was zählt, steht in `lernskript/klausurmarker.md`; dort ist jede
Fundstelle am Bild geprüft.

Das ★ auf den Karteikarten wird **mechanisch** aus dieser Liste vergeben, nicht
von Hand gesetzt. `scripts/karten.py` bricht den Build ab, wenn ein ★ ohne Beleg
auftaucht oder ein Beleg ohne ★ bleibt.

### Grüne Kästchen finden

```bash
pip install pymupdf
python3 scripts/finde_gruene_kaesten.py <ordner-mit-den-folien-pdfs>
```

Zwei Verfahren, weil eines allein nicht reicht: Der **Vektorpass** liest die
Füllfarbe der Zeichenobjekte, der **Pixelpass** rendert jede Folie und sucht
grüne Flächen im Bild. Letzterer ist nötig, weil ein erheblicher Teil der Kästen
als Rastergrafik eingebettet ist. Das Skript meldet zusätzlich, wo die
aufgedruckte Foliennummer von der PDF-Seite abweicht — in den Kapiteln 2 und 2.1
läuft sie um bis zu drei Folien vor.

Die Quell-PDFs sind bewusst nicht eingecheckt: urheberrechtlich geschütztes
Vorlesungsmaterial, und die Markdown-Quellen tragen den Inhalt.

## Erzeugte Dokumente (`output/`)
- `Lebenslauf_Industrie.docx`
- `Lebenslauf_Pharma-MedTech.docx`
- `Lebenslauf_Consulting-Finance.docx`
- `Lebenslauf_Tech-Konsum.docx`
- `Anschreiben_Vorlage.docx` (mit Platzhaltern `{{...}}`)

## Neu generieren
```bash
pip install python-docx
python3 scripts/build_docs.py
```

## Vor dem Versand
1. Persönliche Daten in `scripts/build_docs.py` (Dict `PERSON`) eintragen und neu generieren –
   oder direkt in den DOCX-Dateien die `{{...}}`-Platzhalter ersetzen.
2. Skill-Einstufung in `analyse.md` bestätigen/korrigieren (im Skript Dict `SKILLS`).
3. Anschreiben pro Firma personalisieren (`{{FIRMA}}`, `{{ROLLE}}`, `{{CH_STANDORT}}` …).
4. AKG-Startdatum prüfen (Original „12/2026" – vermutlich 12/2025).
