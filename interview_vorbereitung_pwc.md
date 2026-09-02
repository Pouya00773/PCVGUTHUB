# Interviewvorbereitung – PwC Werkstudent QA (Public Sector & Energy)

**Gespräch: 04.09.2026 · Vorbereitungszeit: max. 2 Tage**

## Kontext

Beworben am 16.08.2026 im PET AI Tech-Hub (Ansprechpartnerin: Noemia Gryzia). Ausgangslage:
laufende QA-Werkstudentenstelle bei AKG Software Consulting (VESTRA INFRAVISION, GE/OFFICE),
Kunden sind Bund, Länder, Kommunen und Ingenieurbüros. Verfügbarkeit bis zu 20 Std./Woche.

Zwei Punkte aus den eingereichten Unterlagen bestimmen den Gesprächsverlauf:

1. **Testautomatisierung kommt in den Unterlagen nicht vor.** Der Block „Im Aufbau“ wurde aus dem
   Lebenslauf entfernt, das Anschreiben endet auf „bisher überwiegend manuell“. Die Anzeige nennt
   Selenium, Cypress und JUnit ausdrücklich. Diese Frage kommt sicher.
2. **Zwei prüfbare Selbstauskünfte:** Englisch „verhandlungssicher“ und Power BI „sicher“.

Bei zwei Tagen Vorbereitung ist Priorisierung wichtiger als Vollständigkeit. Das Gespräch
entscheidet sich an vier Stellen: Selbstvorstellung, Automatisierungsfrage, KI-Testing-Frage und
der Frage nach deiner bestehenden Werkstudentenstelle. Alles andere ist nachrangig.

**Nicht in den zwei Tagen, sondern nebenbei bei der Arbeit** (kostet je 5 Minuten, siehe
Abschnitt 3): Zahlen sammeln und die Freigabe für einen anonymisierten Testplan erfragen.

---

## 1. Selbstvorstellung  *(60 Min., Tag 1)*

90 Sekunden, drei Teile. Nicht den Lebenslauf nacherzählen.

- **Jetzt (40 Sek.):** „Ich studiere Wirtschaftsingenieurwesen an der HTW Berlin und arbeite seit
  Dezember als Werkstudent in der Qualitätssicherung bei AKG Software Consulting. Wir entwickeln
  Planungssoftware für Bahn- und Straßeninfrastruktur und für die Liegenschaftsverwaltung – unsere
  Kunden sind Bund, Länder, Kommunen und Ingenieurbüros. Ich teste die Software vor der Freigabe,
  erstelle die Testpläne zusammen mit dem Produktmanagement und verfolge Fehler bis zur Behebung
  nach.“
- **Weg dorthin (25 Sek.):** kaufmännische Ausbildung im Groß- und Außenhandel, dann bewusst das
  technische Studium. Ein Satz. Kernaussage: du kommst von der fachlichen Seite und liest
  Anforderungen deshalb anders als jemand, der nur Code kennt.
- **Warum hier (25 Sek.):** dasselbe Kundenumfeld, aber KI-gestützte Systeme statt klassischer
  Fachanwendungen – und der Schritt von manuellen Tests in Richtung Automatisierung.

**Der Kundenkreis (Bund, Länder, Kommunen) muss in die ersten 30 Sekunden.** Das ist die einzige
Aussage, die kein anderer Bewerber so machen kann. Keine Tool-Aufzählung in der Vorstellung.

Dreimal laut sprechen, einmal mit Aufnahme. Über zwei Minuten wird es eine Vorlesung.

---

## 2. Was du über PwC wissen musst  *(60 Min., Tag 1 – nicht mehr)*

**Struktur (10 Min.):** PwC Deutschland umfasst Wirtschaftsprüfung, Steuer- und Rechtsberatung
sowie Beratung. Deine Stelle sitzt in der **Beratung**, nicht in der Prüfung – dieses
Missverständnis darf dir nicht passieren. Die Kette lautet: Geschäftsbereich **Transformation** →
**Public & Energy Transformation (PET)** → Team **PET AI Tech-Hub**.

**Inhalte (30 Min.):** PwC berät Bund, Länder, Kommunen, öffentliche Unternehmen, Hochschulen und
gemeinnützige Organisationen zu Digitalisierung, Energiewende, Mobilität und demografischem
Wandel. Verschaff dir Grundwissen zu drei Themen:
- Verwaltungsdigitalisierung: Onlinezugangsgesetz, Registermodernisierung
- Energiewende: Netzausbau, Smart-Meter-Rollout
- **EU-KI-Verordnung (AI Act)** – für eine QA-Rolle direkt relevant, weil sie für
  Hochrisiko-Anwendungen dokumentierte Tests und menschliche Aufsicht verlangt. Vieles im
  öffentlichen Sektor fällt darunter.

**Praktisch (20 Min.):** Noemia Gryzia auf LinkedIn ansehen; rechne mit einer zweiten Person aus
dem Fachbereich. Format und Ort klären, Anfahrt oder Link vorher testen.

**Drei Rückfragen vorbereiten** – nicht mehr, aber gute:
1. Wie sieht euer Teststack aus, wo steht ihr zwischen manuellen und automatisierten Tests?
2. Wie prüft ihr bei KI-gestützten Produkten, ob ein Ergebnis korrekt ist – Referenzdaten, feste
   Bewertungskriterien?
3. Woran würde ich in den ersten drei Monaten konkret arbeiten?

Keine Fragen zu Urlaub, Übernahme oder Homeoffice im ersten Gespräch.

---

## 3. Was du bei AKG mitnehmen solltest  *(nebenbei bei der Arbeit, vor dem 04.09.)*

Kostet kaum Zeit, bringt aber am meisten – erledige es in den Arbeitstagen vor dem Gespräch.

- **Zahlen abschätzen.** Testfälle pro Release, gemeldete Fehler, Teamgröße, betreute Module. Das
  ist die größte Schwachstelle deiner Unterlagen; im Gespräch kannst du sie mit Größenordnungen
  ausgleichen. Grobe Werte reichen, solange du sie vertreten kannst.
- **Testplan freigeben lassen.** Frag deinen Produktmanager, ob du ein anonymisiertes Beispiel
  mitnehmen darfst. Bei der Frage „Wie gehen Sie an einen Testplan heran?“ ist ein echtes Dokument
  die stärkste Antwort, die möglich ist.
- **Zwei Dinge nachschlagen**, die du vermutlich tust, aber benennen können musst:
  - Womit du API-Tests machst (Postman? eingebaute Werkzeuge?) und was du prüfst: Statuscodes,
    Antwortstruktur, Negativfälle, Grenzwerte
  - Welche Kennzahlen bei den Performance-Tests gelten: Antwortzeit, Durchsatz, Fehlerrate unter
    Last, parallele Nutzer
- **Fragen, ob es automatisierte Tests gibt** – etwa in einer Azure Pipeline. Auch wenn du sie
  nicht schreibst: Wenn du erklären kannst, was bei euch automatisiert läuft und was nicht,
  verbessert das deine Automatisierungsantwort erheblich.

---

## 4. Was du privat noch aneignen solltest  *(auf 2 Tage zusammengestrichen)*

Der ursprüngliche Plan mit einem Cypress-Repo über zwei Wochenenden ist nicht mehr machbar.
Reduziert auf das, was in der Zeit ehrlich erreichbar ist:

| Priorität | Thema | Zeit | Ziel |
|---|---|---|---|
| 1 | **KI-Testing-Begriffe** | 90 Min. | 5 Minuten frei sprechen können |
| 2 | **Cypress-Schnelleinstieg** | 2–3 Std. | installieren, **einen** Test gegen eine Demo-Seite laufen lassen |
| 3 | **Selbstvorstellung auf Englisch** | 30 Min. | wenn umgeschaltet wird, sitzt der Einstieg |
| 4 | **Jira-Begriffe** | 10 Min. | Epic/Story/Bug, Board, Sprint, Test Plan – auf Azure DevOps mappen |

**Zu 1 – die sechs Begriffe, mehr brauchst du nicht:**
- Warum ein KI-System nicht gegen einen festen Sollwert prüfbar ist (Nicht-Determinismus)
- **Golden Dataset / Referenzdatensatz** als Ersatz für den Erwartungswert
- **Precision und Recall** – was sie aussagen, warum beides nötig ist
- **Halluzination** – warum eine falsche Antwort plausibel wirkt (steht schon in deinem
  Anschreiben; du musst es fachlich weiterführen können)
- **Bias-Test** – gleiche Anfrage, verändertes Merkmal, Ergebnis vergleichen
- **EU AI Act** – dokumentierte Tests und menschliche Aufsicht bei Hochrisiko-Anwendungen

Das ist die Stelle, an der du dich von anderen Werkstudenten abhebst. Sechs Begriffe, kein Studium.

**Zu 2:** Ein einziger laufender Test verändert deine Antwort von „habe ich vor“ zu „habe ich
angefangen“. Mehr ist in zwei Tagen nicht ehrlich behauptbar – und behaupte auch nicht mehr.

**Gestrichen:** Power BI auffrischen, Selenium, JUnit, Postman-Vertiefung, Sicherheitstests. Falls
Power BI zur Sprache kommt, sag ehrlich, auf welchem Stand du bist.

---

## 5. Vorbereitung auf die Fragen  *(Schwerpunkt Tag 2)*

**Methode:** Vier Geschichten aus deinem Job, jede in 60–90 Sekunden: Situation – was du getan
hast – was herauskam. Vier reichen bei diesem Zeitbudget.

1. Ein Fehler, der beinahe durchgerutscht wäre
2. Eine Anforderung mit zwei Lesarten und wie ihr sie geklärt habt
3. Ein Testplan von der Anforderung bis zur Abnahme
4. Eine Meinungsverschiedenheit mit der Entwicklung über einen Fehler

**Fachfragen – Stichworte genügen:**
- Wie gehen Sie an einen Testplan heran? → Geschichte 3, mit dem echten Dokument
- Was macht einen guten Fehlerbericht aus? → reproduzierbare Schritte, erwartetes vs.
  tatsächliches Verhalten, Umgebung, Schweregrad; Maßstab: Entwicklung arbeitet ohne Rückfrage
- Severity vs. Priority? → Schweregrad = technische Auswirkung, Priorität = Dringlichkeit; ein
  Anzeigefehler auf der Startseite kann hohe Priorität haben
- Wie testen Sie etwas ohne Anforderung? → nachfragen, was erwartet wird, und die Antwort
  schriftlich festhalten
- Was würden Sie automatisieren? → wiederkehrende, stabile Abläufe (Regressionstests); explorativ
  und selten Geändertes bleibt manuell

**Die vier unangenehmen Fragen – wörtlich vorbereiten, das sind die einzigen, bei denen
Improvisieren schadet:**

- **„Sie testen bisher nur manuell.“** → Manuelle Erfahrung als Grundlage: du weißt, welche Fälle
  sich zu automatisieren lohnen. Dazu dein angefangener Cypress-Test. Nicht entschuldigen.
- **„Sie studieren Wirtschaftsingenieurwesen, nicht Informatik.“** → Du arbeitest seit Dezember in
  genau dieser Rolle – Testplanung, API-Tests, Azure DevOps – und bringst die fachliche
  Perspektive mit, die beim Testen von Verwaltungssoftware zählt. Kurz, ohne Rechtfertigung.
- **„Sie haben bereits eine Werkstudentenstelle.“** → Kommt sicher. Entscheide **vor** dem
  Gespräch, ob du wechseln oder beides parallel machen willst, und antworte eindeutig. Zögern
  wirkt hier schlechter als jede Antwort.
- **Gehaltsvorstellung** → Werkstudenten bei Big Four in Berlin liegen üblicherweise bei etwa
  16–20 € pro Stunde. Nenn eine Spanne, keine Punktzahl.

---

## Zeitplan

**In den Arbeitstagen vor dem Gespräch** (je 5–10 Min.): Zahlen abschätzen, Testplan-Freigabe
erfragen, API-/Performance-Details und Pipeline-Frage klären.

**Tag 1 (ca. 5 Std.)**
| Block | Inhalt |
|---|---|
| 60 Min. | Selbstvorstellung schreiben, dreimal laut, einmal aufnehmen |
| 60 Min. | PwC-Recherche + drei Rückfragen notieren |
| 90 Min. | KI-Testing: die sechs Begriffe, jeden in eigenen Worten aufschreiben |
| 90 Min. | Vier Geschichten stichpunktartig aufschreiben |

**Tag 2 (ca. 5 Std.)**
| Block | Inhalt |
|---|---|
| 150 Min. | Cypress installieren, einen Test schreiben und laufen lassen |
| 60 Min. | Die vier unangenehmen Antworten wörtlich formulieren und laut üben |
| 45 Min. | Fachfragen durchgehen, Geschichten laut erzählen |
| 30 Min. | Selbstvorstellung auf Englisch |
| 15 Min. | Jira-Begriffe, Unterlagen ausdrucken, Anfahrt/Link prüfen |

**Am Tag davor:** nichts Neues mehr lernen. Selbstvorstellung und die vier Antworten einmal laut,
dann aufhören.
