# Lernplan

Der Plan ist nach **Punktdichte** sortiert, nicht nach Vorlesungsreihenfolge. Er
richtet sich nach zwei belastbaren Hinweisen aus deinen Unterlagen — belastbar
heisst: schriftlich vorhanden und nachprüfbar, nicht von mir geschlossen.

1. Die handschriftliche Notiz auf Übungsblatt 1: *„Klausuraufgabe: Ein Schaltplan
   wird vorgegeben und soll analysiert werden. Daraus sollen wir eine
   Wahrheitstabelle und ein KV-Diagramm darstellen."*
2. Der Punkteschlüssel von Übung 7: Von 13 Punkten liegen **6 auf der
   KV-Minimierung** — fast die Hälfte.

Beides zeigt in dieselbe Richtung. Die KV-Minimierung ist das Zentrum dieser
Klausur, und sie taucht in mindestens zwei verschiedenen Aufgabentypen auf
(Schaltnetzanalyse und Automatenanalyse). Wer sie sicher beherrscht, hat den
größten Teil der Punkte im Griff.

---

> **Grenze der Belege.** Sechzehn Folien tragen einen handschriftlichen
> Klausurhinweis; die Liste mit Wortlaut steht in `klausurmarker.md`. Die
> Reihenfolge der Blöcke unten geht darüber hinaus und ist **meine
> Einschätzung** — sie folgt der Punktverteilung von Übung 7 und dem Umfang der
> Themen, nicht einer Ansage des Dozenten.

## Die Reihenfolge in einem Satz

Erst das Rechenhandwerk (KV, DNF/KNF), dann die Automaten, die darauf aufbauen,
dann die Schaltungstechnik, zuletzt die Definitionsfragen — die kann man auch
noch am Vorabend sichern.

---

## Block 1 — KV-Minimierung sicher beherrschen

**Das wichtigste Thema. Plane hierfür am meisten Zeit ein.**

Lesen: Lernskript Teil 3, dazu die Erklärung „Das KV-Diagramm — Nachbarn
zusammenfassen".

Können musst du:

- Wahrheitstabelle aus einer Schaltung oder Beschreibung aufstellen
- KV-Tafel für 2, 3 und 4 Variablen korrekt anlegen (Gray-Code, Randfelder
  benachbart)
- Blöcke bilden: möglichst groß, Überlappung erlaubt, jede 1 mindestens einmal
- Minimalform ablesen: nur die Variablen, die im Block konstant bleiben
- Don't-Care als Joker verwenden — und wissen, dass man ihn **nicht** überdecken
  muss
- Die konjunktive Minimalform über die Nullen plus De Morgan

Üben an: Übung 2 (klausurrelevant, vollständig durchgerechnet in
`uebungsloesungen.md`), Übungsblatt 2 Wasserstandsregelung, Übung 1 Minimierung.

**Selbsttest:** Nimm Übung 2, decke die Lösung ab und rechne sie von vorn. Wenn
du in unter 20 Minuten von der Schaltung zur Minimalform kommst und die Probe
stimmt, sitzt das Thema.

---

## Block 2 — Automaten

Baut direkt auf Block 1 auf, denn Schritt 3 der Automatenaufgabe **ist** eine
KV-Minimierung. Deshalb direkt danach.

Lesen: Lernskript Teil 9, Erklärung „Mealy, Moore, Medwedjew".

Können musst du:

- Die drei Typen unterscheiden und die Zugehörigkeit **begründen**
  (Musterformulierung auswendig)
- Warum Mealy die wenigsten Zustände braucht
- Folgezustandstabelle aufstellen — Zeilenzahl ist 2^(Zustandsbits + Eingangsbits)
- Je ein KV für jedes Zustandsbit und für den Ausgang
- Schaltplan mit D-Flipflops und Gattern
- Typumwandlung Mealy ↔ Moore
- Unzulässige Eingangskombination als Don't-Care behandeln

Üben an: Übung 7 Aufgabe 1 komplett, danach Aufgabe 3 Baustellenampel.

**Achte auf:** Beim Moore-Automaten wird der Ausgang **nur** aus den Zustandsbits
gebildet, nicht aus den Eingängen. Das ist ein beliebter Flüchtigkeitsfehler beim
Zeichnen des Schaltplans.

---

## Block 3 — Stromlaufplan und Selbsthaltung

In den Folien mehrfach als klausurrelevant markiert und vom Umfang her
überschaubar.

Lesen: Lernskript Teil 5, Erklärungen „Selbsthaltung" und „Öffner und Schließer".

Können musst du:

- Reihe = UND, Parallel = ODER, Öffner = negiert
- Selbsthaltung zeichnen und erklären
- Schaltnetz ohne, Schaltwerk mit Selbsthaltung
- Warum AUS-Taster Öffner sind (Ruhestromprinzip)
- Verriegelung bei Wendeschützschaltung
- Darstellung immer im **nicht geschalteten** Zustand
- 24 V im Steuerkreis, L1/L2/L3 im Leistungsteil

Üben an: Übung Haltegliedsteuerung, Übung Förderband (Kap. 4/53), Übung 3
Aufgabe 3.

---

## Block 4 — Kontaktkennzeichnung

Reines Auswendiglernen, hohe Punktdichte, wenig Zeitaufwand. Auf der Folie steht
ausdrücklich „beschriften in Klausur".

Auswendig:

| | |
|---|---|
| K | Relais |
| Q | Schütz |
| A1, A2 | Spulenanschlüsse (+/−) |
| Hauptkontakte | einstellig: 3/4 Gleichstrom, 1/2 Wechselstrom |
| Steuerkontakte | zweistellig: Ordnungsziffer + Funktionsziffer |
| Funktionsziffer 1/2 | Öffner |
| Funktionsziffer 3/4 | Schließer |

Beispiel zum Selbsttest: Was ist 13/14? (Erster Schließer.) Was ist 21/22?
(Zweiter Öffner.)

Dazu die drei Kennzeichnungsaspekte: Produkt (−), Funktion (=), Ort (+).

---

## Block 5 — Ablaufkette / SFC

Klausurrelevant markiert (Kap. 6/36, drei Pumpen).

Lesen: Lernskript Teil 8, Erklärung „Die Ablaufkette — ein Kochrezept".

Können musst du:

- Schritte, Aktionen, Transitionen sauber unterscheiden
- Immer nur ein Schritt aktiv; bei erfüllter Bedingung **muss** weitergeschaltet
  werden
- ODER-Verzweigung: nur eine Bedingung darf wahr sein, sonst Priorität
- UND-Verzweigung: eine Bedingung aktiviert alle, eine gemeinsame führt zusammen
- Die vier Betriebsarten

Üben an: Übung 6 alle drei Aufgaben.

**Achte auf:** Der Flankenfehler bei den drei Pumpen. Derselbe Taster mehrfach
verwendet braucht R_TRIG, sonst rauscht die Kette in einem Zyklus durch.

---

## Block 6 — SPS-Grundlagen

Viele kleine, gut abfragbare Fakten.

Lesen: Lernskript Teil 7, Erklärung „Der SPS-Zyklus".

Können musst du:

- EVA-Prinzip und die drei Zyklusphasen (PAE → Programm → PAA)
- Zykluszeit gegen Reaktionszeit, und **warum** die Reaktionszeit länger ist
- Warum mit Prozessabbild gerechnet wird
- Mehrfachzuweisung als Programmfehler
- Die fünf Sprachen nach IEC 61131-3, plus CFC und HiGraph als proprietär
- POU: Programm, FB (mit Speicher), FC (ohne Speicher)
- Datentypen mit Größe und Wertebereich
- Namenskonvention: `gixS1` entschlüsseln können
- Adressierung `%IX136.1`, `%QW800`, `%MD10`
- Zuordnungstabelle in Kurz- und Langform

Üben an: Übung 4 Aufgabe 1a, Übung 5 Aufgabe 1a — beide beginnen mit der
Zuordnungstabelle.

---

## Block 7 — Grundlagen aus Kapitel 1

Reine Definitionsfragen, dafür sehr viele davon. Kapitel 1 trägt **keine**
handschriftlichen Klausurmarkierungen, deshalb steht es hier hinten — nicht weil
es unwichtig wäre, sondern weil es keine belegte Priorität hat.

Lesen: Lernskript Teil 0, Erklärung „Die Automatisierungspyramide".

Können musst du:

- Die vier Grunddefinitionen wörtlich: Automatisierung, System, Prozess, Automat
- Offen, geschlossen, abgeschlossen unterscheiden
- Die sieben Ziele der Automation mit je einem Beispiel
- Basisaufgaben Automation gegen Basisaufgaben Information trennen
- Prozessleitsystem definieren und die fünf Ebenen der Pyramide von oben nach
  unten benennen, mit den Abkürzungen ERP, MES, SCADA, PLC
- Die vier industriellen Revolutionen mit ihren Jahreszahlen
- Kognitive, assoziative und klassische Steuerungsebene mit harter gegen weicher
  Echtzeit

**Gut abfragbar sind die Jahreszahlen:** 1784 Webstuhl, 1870 Fließband, 1941 Z3,
1968/69 erste SPS „Modicon 084" von Richard E. Morley, 1975 TDC2000 von Honeywell.

---

## Block 8 — Systeme und Signale

Definitionsfragen. Am wenigsten Rechenaufwand, gut für kurze Lerneinheiten
zwischendurch.

Lesen: Lernskript Teil 1, Erklärungen „Steuern und Regeln", „Statisch oder
dynamisch", „Stabilität", „Abtastung und Aliasing".

Können musst du:

- Steuerung gegen Regelung, mit der Konsequenz für Störungen und Stabilisierung
- Steuerung nach DIN 19226 Teil 1 wörtlich
- Statisch gegen dynamisch — Energiespeicher als Kriterium
- Die sieben Systemeigenschaften
- Gleichgewichtsbedingung kontinuierlich und diskret
- Die drei Stabilitätsfälle am Kugelbild
- Blockschaltbild: drei Verkettungsarten, Rückwirkungsfreiheit
- Abtastung gegen Quantisierung, Aliasing
- **Shannon-Nyquist-Abtasttheorem** mit Formel: f_A > 2·f_max
- Die exakten Definitionen von Kausalität, Zeitinvarianz und Linearität — sie
  stehen wörtlich in den grünen Kästen und sind gut abfragbar
- Signale in geschlossener Darstellung (Kap. 2.1/30, klausurrelevant)

---

## Block 9 — Digitaltechnik-Grundlagen und Hazards

Teils Auswendiglernen, teils Verständnis.

Auswendig: die acht Regeln mit Konstanten (Kap. 3/12–13, klausurrelevant),
De Morgan, K = 2ⁿ und V = 2^K, Vorrangregeln deutsche gegen amerikanische Norm.

Verstehen: Glitch gegen Hazard, wie Hazards im KV entstehen und dass die
hazardfreie Schaltung einen **redundanten** Term braucht.

---

## Kurz vor der Klausur

Am Vorabend nur noch:

- Den **Spickzettel** einmal durchgehen
- Die Karten mit ★ in `karteikarten.md` durchklicken
- Die Musterbegründung für den Automatentyp laut aufsagen
- Übung 2 einmal im Kopf durchspielen: Schaltung → Tabelle → KV → Minimalform

Nichts Neues mehr anfangen.

## In der Klausur

1. Erst **alle** Aufgaben überfliegen und die KV-Aufgabe zuerst rechnen — dort
   liegen die meisten Punkte.
2. Bei Schaltnetzanalysen **immer** die Zwischenschritte hinschreiben.
   Wahrheitstabelle und KV werden getrennt bepunktet, auch wenn die Endformel
   falsch ist.
3. Bei Minimalformen die **Probe** machen: zwei, drei Zeilen der Wahrheitstabelle
   einsetzen. Kostet eine Minute, fängt Flüchtigkeitsfehler.
4. Genau lesen, ob **DNF oder KNF** verlangt ist. Bei KNF die **Nullen**
   zusammenfassen.
5. Bei Automaten den Typ **begründen**, nicht nur benennen — dafür gibt es einen
   eigenen Punkt.

---

## Vollständigkeit

Alle neun Foliensätze (Kapitel 1 bis 7), zehn Handouts und die Übungsblätter 1
bis 7 sind eingearbeitet. Es fehlt nichts mehr.
