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
- `output/` – fertige Word-Dateien

## Erzeugte Dokumente (`output/`)
- `Lebenslauf_Industrie.docx`
- `Lebenslauf_Pharma-MedTech.docx`
- `Lebenslauf_Consulting-Finance.docx`
- `Lebenslauf_Tech-Konsum.docx`
- `Anschreiben_Vorlage.docx` (mit Platzhaltern `{{...}}`)

## Stellenspezifische Bewerbungen (`bewerbungen/`)
- `bewerbungen/pwc-ai-adoption/` – Werkstudent AI Adoption & Enablement (w/m/d), PwC Deutschland
  - `analyse.md` – Anforderungsabgleich, Differenzierung, offene Punkte vor dem Versand
  - `lebenslauf.md` / `anschreiben.md` – Textfassungen
  - erzeugt via `scripts/build_pwc.py` → `output/*_PwC.docx`
- `bewerbungen/pwc-qa-public-sector-energy/` – Praktikum / Werkstudent Quality Assurance
  Specialist – Public Sector & Energy (w/m/d), PwC Deutschland (Transformation, Berlin, Req. 2512)
  - `analyse.md` – Quellenlage, Anforderungsabgleich, ATS-Mechanik, offene Punkte
  - `lebenslauf.md` / `anschreiben.md` – Textfassungen
  - erzeugt via `scripts/build_pwc_qa.py` → `output/*_PwC_QA.docx`

## Neu generieren
```bash
pip install python-docx
python3 scripts/build_docs.py   # Branchen-Varianten
python3 scripts/build_pwc.py    # PwC AI Adoption & Enablement
python3 scripts/build_pwc_qa.py # PwC Quality Assurance – Public Sector & Energy
```

## Vor dem Versand
1. Persönliche Daten in `scripts/build_docs.py` (Dict `PERSON`) eintragen und neu generieren –
   oder direkt in den DOCX-Dateien die `{{...}}`-Platzhalter ersetzen.
2. Skill-Einstufung in `analyse.md` bestätigen/korrigieren (im Skript Dict `SKILLS`).
3. Anschreiben pro Firma personalisieren (`{{FIRMA}}`, `{{ROLLE}}`, `{{CH_STANDORT}}` …).
4. AKG-Startdatum prüfen (Original „12/2026" – vermutlich 12/2025).
