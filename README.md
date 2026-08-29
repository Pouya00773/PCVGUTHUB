# Werkstudenten-Bewerbung – Wirtschaftsingenieur (mit Schweiz-Bezug)

ATS-/AI-Filter-optimierte Bewerbungsunterlagen für Werkstudenten-Stellen bei gut zahlenden
Firmen mit Schweiz-Standort. **Leitplanke:** keine erfundenen Qualifikationen – aufzubauende
Skills sind ehrlich als „(Grundkenntnisse)" markiert (Lernplan siehe `lernplan.md`).

## Inhalt
- `input/lebenslauf_original.md` – transkribierter Original-CV (persönliche Daten als Platzhalter)
- `analyse.md` – Stärken, Lücken, Skill-Einstufung (bitte bestätigen)
- `zielfirmen.md` – kuratierte Zielfirmen je Branche + ATS-Keyword-Bank
- `lernplan.md` – kostenlose Ressourcen für „in Aneignung"-Skills
- `pwc_qa_bewerbung.md` – Fit-Analyse, Lernplan und ATS-Keywords für die PwC-QA-Stelle
- `interview_vorbereitung_pwc.md` – 2-Tage-Vorbereitungsplan für das Gespräch am 04.09.2026
- `scripts/build_docs.py` – erzeugt die branchengenerischen DOCX-Dateien (datengetrieben)
- `scripts/build_pwc_docs.py` – erzeugt die stellenspezifischen PwC-QA-Dokumente
- `output/` – fertige Word-Dateien

## Erzeugte Dokumente (`output/`)
Branchenvarianten (generisch):
- `Lebenslauf_Industrie.docx`
- `Lebenslauf_Pharma-MedTech.docx`
- `Lebenslauf_Consulting-Finance.docx`
- `Lebenslauf_Tech-Konsum.docx`
- `Anschreiben_Vorlage.docx` (mit Platzhaltern `{{...}}`)

Stellenspezifisch – PwC, Werkstudent Quality Assurance Specialist (Public Sector & Energy):
- `Lebenslauf_PwC_QA.docx`
- `Anschreiben_PwC_QA.docx`

## Neu generieren
```bash
pip install python-docx
python3 scripts/build_docs.py       # Branchenvarianten
python3 scripts/build_pwc_docs.py   # PwC QA
```

## Vor dem Versand
1. Persönliche Daten in `scripts/build_docs.py` (Dict `PERSON`) eintragen und neu generieren –
   oder direkt in den DOCX-Dateien die `{{...}}`-Platzhalter ersetzen.
2. Skill-Einstufung in `analyse.md` bestätigen/korrigieren (im Skript Dict `SKILLS`).
3. Anschreiben pro Firma personalisieren (`{{FIRMA}}`, `{{ROLLE}}`, `{{CH_STANDORT}}` …).
4. AKG-Startdatum prüfen (Original „12/2026" – vermutlich 12/2025).
