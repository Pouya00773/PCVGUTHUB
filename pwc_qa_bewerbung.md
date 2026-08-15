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
| **Fortgeschrittenes Studium Informatik / SWE / Wirt.-Inf.** | ⚠️ Wirtschaftsingenieurwesen, 4. Semester | Ausbildung – als „vergleichbar“ positioniert |
| Testmanagement-Tools (TestRail, Jira) | ❌ noch nicht belegt | „In Aneignung“ |
| Testautomatisierung (Selenium, Cypress, JUnit) | ❌ noch nicht belegt | „In Aneignung“ |
| API-, Performance-, Sicherheitstests | ❌ noch nicht belegt | „In Aneignung“ |
| Versionskontrolle / Code-Repositories (Git) | ❌ noch nicht belegt | „In Aneignung“ |
| Agile Umgebungen (Scrum, Kanban) | ❌ noch nicht belegt | „In Aneignung“ |
| Testen von KI-Modellen (nur „von Vorteil“) | ❌ | „In Aneignung“ |
| Prozessoptimierung | ✅ Studieninhalt + kaufm. Praxis | Ausbildung |

**Realistische Einschätzung:** Für eine Werkstudentenstelle ist das ein guter, kein perfekter Fit.
Die vier ersten Punkte der Liste („Das erwartet dich“) triffst du bereits mit echter Praxis – das ist
mehr, als die meisten Bewerber:innen auf dieser Ebene mitbringen. Die Lücke liegt bei den Tools, und
Tools lernt man; das weiß PwC bei einer Werkstudentenstelle auch. Der Studiengang ist der schwächere
Punkt, aber „oder einem vergleichbaren Studiengang“ lässt Wirtschaftsingenieurwesen zu – zumal die
Stelle explizit an der Schnittstelle Business ↔ Technologie ↔ Beratung sitzt, wo dein Doppelprofil
(kaufmännische Ausbildung + technisches Studium) ein Argument ist statt eine Ausrede.

---

## 2. Was ich bewusst NICHT geschrieben habe

Leitplanke aus `README.md`: keine erfundenen Qualifikationen. Konkret heißt das:

- **Kein** „Erfahrung mit Selenium/Cypress/JUnit“, **kein** „TestRail“, **kein** „Scrum-Erfahrung“ im
  Erfahrungsteil. Diese Begriffe stehen ausschließlich im Block **„In Aneignung (Selbststudium)“**.
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
2. **„In Aneignung“ hochstufen, wo es stimmt.** Sehr wahrscheinlich nutzt du bei AKG bereits **Jira**
   (oder ein vergleichbares Ticketsystem) und arbeitest in **Sprints**. Falls ja: raus aus „In
   Aneignung“, rein in „Praxiserprobt“ und in die AKG-Bullets. Das schließt zwei Anforderungen der
   Anzeige auf einen Schlag. Gleiches gilt für Git.
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
| 1 | **Jira** (Testmanagement) | Atlassian Free Plan (bis 10 User gratis) + Atlassian University | Eigenes Projekt anlegen, Bugs mit Schweregrad/Reproduktionsschritten erfassen |
| 2 | **Git** | „Pro Git“ (kostenlos online), GitHub Skills | Branch, Commit, Pull Request, Merge-Konflikt lösen können |
| 3 | **Cypress** (E2E) | Cypress Docs „Real World App“ + offizielles Tutorial | 3 automatisierte E2E-Tests gegen eine Demo-Web-App |
| 4 | **API-Tests** | Postman Learning Center | Collection mit GET/POST, Status-Code- und Schema-Assertions |
| 5 | **Scrum/Kanban** | Scrum Guide (kostenlos, ~20 Seiten) | Rollen, Events, Artefakte in eigenen Worten erklären |
| 6 | **Selenium / JUnit** | Selenium Docs, JUnit 5 User Guide | Ein Selenium-Skript, das ein Login-Formular testet |
| 7 | **KI-Modelle testen** | Google „Testing ML Systems“, Artikel zu LLM-Evaluation | Erklären können, warum nicht-deterministische Outputs andere Testmethoden brauchen |

**Interview-Gold:** Leg die Ergebnisse in ein öffentliches GitHub-Repo (Cypress-Tests + Postman-
Collection + Testfall-Dokumentation). Dann belegt das Repo gleichzeitig Punkt 2, 3 und 4 – und du
kannst den Link ins Anschreiben oder in den CV-Kopf setzen. Für eine QA-Stelle ist das der
überzeugendste Nachweis, den ein Werkstudent liefern kann.

---

## 5. ATS-Keyword-Bank für diese Stelle

Alle Begriffe sind in den erzeugten Dokumenten enthalten – wahrheitsgemäß entweder in der Erfahrung
oder im „In Aneignung“-Block:

Quality Assurance · Qualitätssicherung · Testmanagement · Softwarequalität · manuelle Tests ·
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
