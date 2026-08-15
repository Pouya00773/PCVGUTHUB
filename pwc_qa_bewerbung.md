# PwC – Werkstudent Quality Assurance Specialist (Public Sector & Energy)

Zielstelle: **Werkstudent/Praktikant Quality Assurance Specialist – Public Sector & Energy (w/m/d)**
Bereich: PwC Deutschland, *Public & Energy Transformation*, Team „PET AI Tech-Hub“ · 21 Standorte

Dokumente: `output/Lebenslauf_PwC_QA.docx` · `output/Anschreiben_PwC_QA.docx`
Generator: `python3 scripts/build_pwc_docs.py`

---

## 1. Fit-Analyse: du gegen die Anzeige

Deine aktuelle Rolle bei AKG ist **exakt die Rolle, die PwC ausschreibt** – nur eine Stufe kleiner.
Das ist der stärkste Hebel, den du hast, und er steht deshalb im Lebenslauf ganz oben (eigener Block
„Qualitätssicherung & Testing“ noch vor der Berufserfahrung, damit der ATS-Parser und der 8-Sekunden-
Blick des Recruiters sofort darauf treffen).

| Anforderung der Anzeige | Dein Stand | Wo es im CV steht |
|---|---|---|
| Testmanagement & Qualitätssicherung, manuelle Tests | ✅ Praxis (AKG, Produktabnahme) | Kernkompetenzen + Bullet 1 |
| Softwarequalität über alle Entwicklungsphasen | ✅ Praxis (Test-/Projektdokumentation) | Bullet 4 |
| Teamübergreifende Zusammenarbeit mit Dev-/Produktteams | ✅ Praxis (Abstimmung mit Entwicklung) | Bullet 5 |
| Edge Cases / „Unlucky Paths“ systematisch analysieren | ✅ Praxis – wörtlich aus der Anzeige gespiegelt | Bullet 2 |
| Detailorientierung, kommunikationsstarkes Fehlerreporting | ✅ Praxis (reproduzierbare Fehlerberichte) | Bullet 3 + Anschreiben Abs. 2 |
| Dokumentationskompetenz | ✅ Praxis | Bullet 4 |
| **Testmanagement-Tools (TestRail, Jira)** | ✅ Praxis mit **Azure DevOps** – funktional äquivalent | Kernkompetenzen + AKG-Bullet 3 |
| **Agile Umgebungen (Scrum, Kanban)** | ✅ Praxis – Arbeit in **Sprints** | Kernkompetenzen + AKG-Bullet 5 |
| **Fortgeschrittenes Studium Informatik / SWE / Wirt.-Inf.** | ⚠️ Wirtschaftsingenieurwesen, 4. Semester | Ausbildung – als „vergleichbar“ positioniert |
| Testautomatisierung (Selenium, Cypress, JUnit) | ❌ noch nicht belegt | „In Aneignung“ |
| API-, Performance-, Sicherheitstests | ❌ noch nicht belegt | „In Aneignung“ |
| Versionskontrolle / Code-Repositories (Git) | ❔ zu klären – Azure Repos? | „In Aneignung“ |
| Testen von KI-Modellen (nur „von Vorteil“) | ❌ | „In Aneignung“ |
| Prozessoptimierung | ✅ Studieninhalt + kaufm. Praxis | Ausbildung |

**Realistische Einschätzung:** Für eine Werkstudentenstelle ist das ein starker Fit. Von den elf
Anforderungen der Anzeige triffst du **acht mit echter Praxis** – inklusive Testmanagement-Tool und
agilem Arbeiten. Dass dein Tool Azure DevOps heißt und nicht Jira, ist kein Minus: beides sind
Work-Item-/Bug-Tracking-Systeme mit Boards und Sprints, der Umstieg ist eine Frage von Tagen. Genau
so ist es im Anschreiben formuliert, statt es zu verschweigen.

Offen bleibt im Wesentlichen die **Testautomatisierung** (Selenium, Cypress, JUnit) samt API- und
Performance-Tests. Das ist die eine Lücke, an der es sich zu arbeiten lohnt – siehe Abschnitt 4. Der
Studiengang ist der zweite schwächere Punkt, aber „oder einem vergleichbaren Studiengang“ lässt
Wirtschaftsingenieurwesen zu – zumal die Stelle explizit an der Schnittstelle Business ↔ Technologie
↔ Beratung sitzt, wo dein Doppelprofil (kaufmännische Ausbildung + technisches Studium) ein Argument
ist statt eine Ausrede.

---

## 2. Was ich bewusst NICHT geschrieben habe

Leitplanke aus `README.md`: keine erfundenen Qualifikationen. Konkret heißt das:

- **Kein** „Erfahrung mit Selenium/Cypress/JUnit“, **kein** „Jira“, **kein** „TestRail“ im
  Erfahrungsteil. Diese Begriffe stehen ausschließlich im Block **„In Aneignung (Selbststudium)“**.
  Azure DevOps und Sprints stehen dagegen in der Praxis – die hast du.
- Das ist kein Nachteil beim ATS: Die Keywords sind im Dokument vorhanden und werden gematcht. Der
  Unterschied ist nur, dass du im Gespräch nicht auffliegst.
- **Eine Annahme, die du prüfen musst:** Im Ausbildungsteil steht, dass Programmierung (Python, C#),
  Datenbanken/SQL sowie Prozess- und Qualitätsmanagement Studieninhalte sind. Das ist aus deinem
  Original-CV abgeleitet (dort stehen Python, C# und SQL unter EDV-Kenntnissen) und für WI an der HTW
  üblich – aber du weißt es genauer als ich. Falls du diese Inhalte noch nicht im Studium hattest:
  Zeile streichen.
- **Keine erfundenen Zahlen** („350 Testfälle“, „Fehlerquote um 20 % gesenkt“). Wenn du echte Zahlen
  aus deiner AKG-Tätigkeit hast – ungefähre Anzahl Testfälle pro Sprint/Release, Anzahl gemeldeter
  Fehler, Größe des Teams, Anzahl betreuter Module –, sag sie mir, ich baue sie ein. Quantifizierte
  Bullets sind der größte verbleibende Hebel im CV.

---

## 3. Bevor du abschickst – 4 Dinge

1. **Platzhalter ersetzen.** `{{NAME}}`, `{{ANSCHRIFT}}`, `{{TELEFON}}`, `{{GEBURT}}`, `{{LINKEDIN}}`,
   `{{DATUM}}`, `{{REFERENZ}}`, `{{FIRMA_ADRESSE}}` (Adresse des Standorts, auf den du dich bewirbst).
   Entweder direkt im Dict `PERSON` in `scripts/build_pwc_docs.py` und neu generieren, oder in der DOCX.
   Die Hinweiszeilen am Dokumentende **löschen**.
2. **Zwei offene Azure-Fragen.** Azure DevOps und Sprints sind eingebaut. Noch zu klären: Nutzt du
   (a) **Azure Repos / Git** für Versionskontrolle und (b) **Azure Test Plans** für strukturierte
   Testfallverwaltung? Jedes „ja“ schließt eine weitere Anforderung der Anzeige – dann raus aus
   „In Aneignung“, rein in „Praxiserprobt“.
3. **Startdatum prüfen.** Im Original-CV steht „01.12.2026“ für den AKG-Start – hier ist 12/2025
   angenommen. Bitte bestätigen, sonst steht ein Datum in der Zukunft im Lebenslauf.
4. **Standort wählen.** Die Stelle ist an 21 Standorten ausgeschrieben. Berlin ist für dich naheliegend
   (HTW). Im Bewerbungsformular den Standort explizit angeben.

---

## 4. Lernplan für die Lücke (ergänzt `lernplan.md`)

Ziel: bis zum Gespräch sollen die „In Aneignung“-Punkte echt belegbar sein – dann sind sie im Interview
dein Trumpf statt deine Schwachstelle. Priorität nach Gewicht in der Anzeige:

| Priorität | Thema | Kostenlose Ressource | Mini-Ziel (~10 h) |
|---|---|---|---|
| 1 | **Cypress** (E2E) | Cypress Docs „Real World App“ + offizielles Tutorial | 3 automatisierte E2E-Tests gegen eine Demo-Web-App |
| 2 | **Git** | „Pro Git“ (kostenlos online), GitHub Skills | Branch, Commit, Pull Request, Merge-Konflikt lösen können |
| 3 | **API-Tests** | Postman Learning Center | Collection mit GET/POST, Status-Code- und Schema-Assertions |
| 4 | **Selenium / JUnit** | Selenium Docs, JUnit 5 User Guide | Ein Selenium-Skript, das ein Login-Formular testet |
| 5 | **KI-Modelle testen** | Google „Testing ML Systems“, Artikel zu LLM-Evaluation | Erklären können, warum nicht-deterministische Outputs andere Testmethoden brauchen |
| 6 | **Jira** (nur Vokabular) | Atlassian Free Plan (bis 10 User gratis) | Begriffe auf Azure DevOps mappen: Epic/Story/Bug, Board, Sprint, Workflow |

Scrum und Testmanagement stehen nicht mehr auf der Liste – die hast du über Azure DevOps und die
Sprint-Arbeit bei AKG bereits abgedeckt. Für Jira reicht das Vokabular: Wenn du im Interview sagen
kannst, welches Azure-DevOps-Konzept welchem Jira-Begriff entspricht, ist die Frage erledigt.

**Interview-Gold:** Leg die Ergebnisse in ein öffentliches GitHub-Repo (Cypress-Tests + Postman-
Collection + Testfall-Dokumentation). Dann belegt das Repo gleichzeitig Punkt 2, 3 und 4 – und du
kannst den Link ins Anschreiben oder in den CV-Kopf setzen. Für eine QA-Stelle ist das der
überzeugendste Nachweis, den ein Werkstudent liefern kann.

---

## 5. ATS-Keyword-Bank für diese Stelle

Alle Begriffe sind in den erzeugten Dokumenten enthalten – wahrheitsgemäß entweder in der Erfahrung
oder im „In Aneignung“-Block:

Quality Assurance · Qualitätssicherung · Testmanagement · Azure DevOps · Sprint · Softwarequalität · manuelle Tests ·
automatisierte Tests · Testautomatisierung · Testfall · Testdurchführung · Testdokumentation ·
Produktabnahme · Fehlerreporting · Fehlernachverfolgung · Retest · Edge Cases · Unlucky Paths ·
Ausnahmefälle · Jira · TestRail · Selenium · Cypress · JUnit · API-Tests · Performance-Tests ·
Sicherheitstests · Versionskontrolle · Git · Code-Repository · Scrum · Kanban · agile Entwicklung ·
cross-funktionales Team · KI-Modelle · datengetriebene Systeme · Detailorientierung ·
Prozessoptimierung · Dokumentationskompetenz · Public Sector · Energy · Digitalisierung

**Formatregeln, die im Dokument eingehalten sind:** einspaltig, keine Tabellen/Textboxen/Grafiken für
Inhalte, Kontaktdaten als reiner Text im Fließtext (nicht in der Kopfzeile – Kopfzeilen werden von
vielen Parsern ignoriert), Standardüberschriften, Standardschrift, Datumsformat MM/JJJJ.

**Dateinamen beim Upload:** `Lebenslauf_<Nachname>_PwC_QA.docx` und
`Anschreiben_<Nachname>_PwC_QA.docx`. Falls das Portal PDF verlangt: aus Word als PDF exportieren
(nicht drucken/scannen) – dann bleibt der Text maschinenlesbar.
